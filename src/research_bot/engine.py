"""The deep-research orchestrator.

This is the head-less equivalent of DeerFlow's *lead agent*: it plans, delegates
to per-sub-question researchers (search + fetch + extract), critiques coverage,
fills gaps and finally synthesises a cited report. Skills (DeerFlow ``SKILL.md``
format) are injected into every LLM system prompt.

Pipeline
--------
    plan → [ retrieve → rank → fetch → extract ] × rounds → critique → synthesize

Every stage degrades gracefully: if the LLM is unreachable the run still emits a
source-grounded report, and if a search engine is blocked the router drops it.
"""

from __future__ import annotations

import logging
import re
from collections.abc import Callable
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from .config import DotDict
from .fetch import Page, fetch_many
from .llm import LLM, LLMError, dumps
from .search import SearchResult, SearchRouter
from .skills import Skill, load_skills, select_skills
from .topics import Topic
from .util import is_recent, now_utc, truncate

log = logging.getLogger(__name__)

Progress = Callable[[str], None]

# HTML engines cast a wide net and return homonym noise (ROS → "reactive oxygen
# species", "Pinocchio" → the fairy tale); keyword-matching academic engines
# (Crossref/OpenAlex) also return loose matches ("pi0" → π⁰ meson physics). The
# gate below applies to every engine: a hit is kept only if it contains a topic
# keyword or overlaps the query on at least two *distinctive* terms.
#
# Query words too generic to prove relevance on their own.
_GENERIC_TOKENS = frozenset({
    "best", "practices", "practice", "project", "projects", "modern", "study", "studies",
    "analysis", "survey", "review", "learning", "model", "models", "data", "dataset",
    "datasets", "using", "based", "evaluation", "evaluate", "performance", "research",
    "paper", "papers", "method", "methods", "approach", "approaches", "overview", "guide",
    "introduction", "tutorial", "application", "applications", "system", "systems", "new",
    "recent", "towards", "toward", "state", "art", "case",
})


def _content_tokens(text: str) -> set[str]:
    return {t for t in re.split(r"[^0-9a-z一-鿿]+", (text or "").lower()) if len(t) >= 2}


def _distinctive_tokens(text: str) -> set[str]:
    return {t for t in _content_tokens(text) if t not in _GENERIC_TOKENS}


def _is_offtopic(res: SearchResult, distinct_query: set[str], keywords: set[str]) -> bool:
    text = f"{res.title} {res.snippet}".lower()
    if any(kw in text for kw in keywords):
        return False
    return len(_distinctive_tokens(text) & distinct_query) < 2


def _heat_text(res: SearchResult) -> str:
    bits = []
    if res.citations is not None:
        bits.append(f"citations={res.citations}")
    if res.stars is not None:
        bits.append(f"stars={res.stars}")
    return ", ".join(bits)


def _authority_text(res: SearchResult) -> str:
    return res.venue or ""


def _attention_text(res: SearchResult) -> str:
    if res.stars is not None:
        level = "高" if res.stars >= 1000 else "中" if res.stars >= 100 else "低"
        return f"{level}（stars={res.stars}）"
    if res.citations is not None:
        level = "高" if res.citations >= 50 else "中" if res.citations >= 5 else "低"
        return f"{level}（citations={res.citations}）"
    return ""


def _recommendation_text(res: SearchResult) -> str:
    score = 3  # already passed the relevance gate, so baseline is "worth a look"
    reasons: list[str] = []
    if res.venue:
        score += 1
        reasons.append(f"venue={res.venue}")
    if (res.citations or 0) >= 50 or (res.stars or 0) >= 1000:
        score += 1
        reasons.append("高热度")
    if not res.venue and res.citations is None and res.stars is None:
        score -= 1  # no authority and no heat signal -> downgrade
    score = max(1, min(5, score))
    return "★" * score + "☆" * (5 - score) + (f"（{', '.join(reasons)}）" if reasons else "")


DEPTH_PRESETS: dict[str, dict[str, int]] = {
    "quick": {"max_subquestions": 3, "max_rounds": 1, "results_per_subquestion": 4, "fetch_top_n": 2, "candidates": 12},
    "standard": {"max_subquestions": 5, "max_rounds": 2, "results_per_subquestion": 6, "fetch_top_n": 4, "candidates": 24},
    "deep": {"max_subquestions": 8, "max_rounds": 3, "results_per_subquestion": 8, "fetch_top_n": 6, "candidates": 32},
}


@dataclass
class SubQuestion:
    id: str
    question: str
    queries: list[str] = field(default_factory=list)
    rationale: str = ""
    prefer: list[str] = field(default_factory=list)
    results: list[SearchResult] = field(default_factory=list)
    pages: dict[str, Page] = field(default_factory=dict)
    extraction: dict[str, Any] = field(default_factory=dict)
    round: int = 1

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "question": self.question,
            "queries": self.queries,
            "rationale": self.rationale,
            "round": self.round,
            "results": [r.to_dict() for r in self.results],
            "extraction": self.extraction,
        }


class SourceRegistry:
    """Assigns stable, global citation numbers to unique sources."""

    def __init__(self) -> None:
        self.items: list[SearchResult] = []
        self._by_key: dict[str, int] = {}

    @staticmethod
    def _key(res: SearchResult) -> str:
        from .util import norm_url

        return norm_url(res.url) or (res.title or "").strip().lower()

    def add(self, res: SearchResult) -> int:
        key = self._key(res)
        if key in self._by_key:
            return self._by_key[key]
        self.items.append(res)
        idx = len(self.items)
        self._by_key[key] = idx
        return idx

    def add_many(self, results: list[SearchResult]) -> None:
        for res in results:
            self.add(res)

    def index_of(self, res: SearchResult) -> int | None:
        return self._by_key.get(self._key(res))

    def reference_list(self) -> list[dict[str, Any]]:
        refs: list[dict[str, Any]] = []
        for i, res in enumerate(self.items, start=1):
            refs.append(
                {
                    "n": i,
                    "title": res.title,
                    "url": res.url,
                    "kind": res.kind,
                    "venue": res.venue,
                    "published": res.published,
                    "citations": res.citations,
                    "stars": res.stars,
                }
            )
        return refs


@dataclass
class ResearchResult:
    topic: str
    title: str
    query: str
    depth: str
    language: str
    started_at: str
    finished_at: str = ""
    duration_s: float = 0.0
    rounds: int = 1
    plan: dict[str, Any] = field(default_factory=dict)
    subquestions: list[SubQuestion] = field(default_factory=list)
    critiques: list[dict[str, Any]] = field(default_factory=list)
    report_md: str = ""
    references: list[dict[str, Any]] = field(default_factory=list)
    engines: list[str] = field(default_factory=list)
    skills: list[str] = field(default_factory=list)
    llm_stats: dict[str, Any] = field(default_factory=dict)
    models: dict[str, str] = field(default_factory=dict)

    def to_dict(self, include_sources: bool = True) -> dict[str, Any]:
        data: dict[str, Any] = {
            "topic": self.topic,
            "title": self.title,
            "query": self.query,
            "depth": self.depth,
            "language": self.language,
            "started_at": self.started_at,
            "finished_at": self.finished_at,
            "duration_s": round(self.duration_s, 1),
            "rounds": self.rounds,
            "plan": self.plan,
            "subquestions": [s.to_dict() for s in self.subquestions],
            "critiques": self.critiques,
            "engines": self.engines,
            "skills": self.skills,
            "llm_stats": self.llm_stats,
            "models": self.models,
            "report_md": self.report_md,
        }
        if include_sources:
            data["references"] = self.references
        return data


LANG_INSTRUCTIONS = {
    "zh": "用简体中文撰写报告（专有名词、模型名、库名保留英文原文）。",
    "en": "Write the report in English.",
    "bilingual": "使用简体中文撰写报告，关键术语、模型名、论文标题和库名保留英文原文（中英对照）。",
}


class DeepResearchEngine:
    def __init__(
        self,
        cfg: DotDict,
        home: Path,
        *,
        llm: LLM | None = None,
        router: SearchRouter | None = None,
    ) -> None:
        self.cfg = cfg
        self.home = Path(home)
        self.llm = llm or LLM(cfg.llm)
        self.router = router or SearchRouter(cfg.search)
        self.all_skills: dict[str, Skill] = load_skills(self.home)
        skill_names = list(getattr(cfg.research, "skills", []) or [])
        self.skills: list[Skill] = select_skills(self.all_skills, skill_names)
        # Populated per-run from the topic; drives the relevance gate.
        self._topic_keywords: set[str] = set()

    # ------------------------------------------------------------------ utils
    def _say(self, progress: Progress | None, message: str) -> None:
        log.info(message)
        if progress:
            progress(message)

    def _skill_block(self) -> str:
        if not self.skills:
            return ""
        rendered = "\n\n".join(s.to_prompt() for s in self.skills)
        return (
            "以下是本次调研必须遵循的领域方法论 Skills（来自本地 skills/ 与 deer-flow 子模块）：\n\n"
            f"{rendered}\n"
        )

    def _system(self, role: str) -> str:
        from .util import date_stamp

        base = (
            "你是一个严谨的科研调研 Agent（robotics deep-research agent），服务于具身智能、VLA、"
            "运动学、C++ 与 ROS2 领域。你必须优先使用可核查的证据，禁止编造论文、项目、数据集或数字；"
            "无法确认的内容要明确标注“待核实”。所有关键论断都要给出真实的 URL 引用编号。\n"
            f"当前日期（UTC）：{date_stamp()}。涉及“最新/前沿/近一年”的判断以此为准，"
            "并据实际检索到的发表时间（published）判断新旧，不要把模型的训练知识当作最新进展。\n"
        )
        return f"{base}\n你的当前角色：{role}\n\n{self._skill_block()}"

    # ------------------------------------------------------------------- plan
    def plan(self, topic: Topic, extra_query: str = "", max_subquestions: int = 5) -> dict[str, Any]:
        seed = {
            "topic": topic.title,
            "description": topic.description,
            "keywords": topic.keywords,
            "venues": topic.venues,
            "seed_queries": topic.seed_queries,
        }
        messages = [
            {"role": "system", "content": self._system("研究规划者（planner）")},
            {
                "role": "user",
                "content": (
                    "请针对下面的研究主题设计一份深度调研计划，输出严格的 JSON。\n\n"
                    f"主题定义：\n{dumps(seed)}\n\n"
                    f"用户额外关注点：{extra_query or '（无）'}\n\n"
                    f"要求：\n"
                    f"1. 拆解为 {max(3, max_subquestions - 1)}-{max_subquestions} 个子问题（subquestions），覆盖：\n"
                    "   前沿进展(最近1-2年)、经典/奠基工作、开源项目与工程实践、数据集与基准、开放问题与争议。\n"
                    "2. 每个子问题给出 2-4 条可直接投喂给学术搜索/网页搜索的查询词（queries），"
                    "中英文混合、精确（含模型名/方法名/会议名/年份）。\n"
                    "3. prefer 字段给出优先检索源，取值集合：arxiv, openalex, crossref, semantic_scholar, "
                    "github, bing。\n"
                    "4. 只输出 JSON，不要输出任何解释文字，格式如下：\n"
                    '{"title":"报告标题","summary":"一句话研究目标",'
                    '"subquestions":[{"id":"q1","question":"...","rationale":"...","queries":["...","..."],'
                    '"prefer":["arxiv","github"]}]}'
                ),
            },
        ]
        try:
            data = self.llm.json(messages, tier="strong", temperature=0.2, max_tokens=3000)
        except LLMError as exc:
            log.warning("planner LLM failed (%s); using seed-query fallback plan", exc)
            data = self._fallback_plan(topic, extra_query, max_subquestions)
        return self._normalise_plan(data, topic, extra_query, max_subquestions)

    def _fallback_plan(self, topic: Topic, extra_query: str, max_subquestions: int) -> dict[str, Any]:
        queries = list(topic.seed_queries) or [topic.title]
        if extra_query:
            queries = [extra_query, *queries]
        subs = []
        for i, q in enumerate(queries[:max_subquestions], start=1):
            subs.append({"id": f"q{i}", "question": q, "rationale": "topic seed query", "queries": [q], "prefer": []})
        return {"title": f"{topic.title} 前沿调研", "summary": topic.description, "subquestions": subs}

    def _normalise_plan(self, data: Any, topic: Topic, extra_query: str, max_subquestions: int) -> dict[str, Any]:
        if not isinstance(data, dict):
            return self._fallback_plan(topic, extra_query, max_subquestions)
        subs = data.get("subquestions") or []
        clean: list[dict[str, Any]] = []
        for i, sub in enumerate(subs[:max_subquestions], start=1):
            if not isinstance(sub, dict):
                continue
            question = str(sub.get("question") or "").strip()
            if not question:
                continue
            queries = [str(q).strip() for q in (sub.get("queries") or []) if str(q).strip()]
            if not queries:
                queries = [question]
            clean.append(
                {
                    "id": str(sub.get("id") or f"q{i}"),
                    "question": question,
                    "rationale": str(sub.get("rationale") or ""),
                    "queries": queries[:4],
                    "prefer": [str(p) for p in (sub.get("prefer") or []) if str(p)][:6],
                }
            )
        if not clean:
            return self._fallback_plan(topic, extra_query, max_subquestions)
        return {
            "title": str(data.get("title") or f"{topic.title} 前沿调研"),
            "summary": str(data.get("summary") or topic.description),
            "subquestions": clean,
        }

    # --------------------------------------------------------------- retrieve
    def _filter_relevant(self, results: list[SearchResult], sub: SubQuestion) -> list[SearchResult]:
        distinct_query = _distinctive_tokens(" ".join([sub.question, *sub.queries]))
        keywords = self._topic_keywords
        if not keywords and not distinct_query:
            return results
        # If nothing clears the bar the sub-question is left empty on purpose: a
        # gap marked for follow-up beats fabricating relevance from junk.
        return [r for r in results if not _is_offtopic(r, distinct_query, keywords)]

    def _rank_results(self, results: list[SearchResult], sub: SubQuestion, max_keep: int, recency_days: int) -> list[SearchResult]:
        results = self._filter_relevant(results, sub)

        def score(res: SearchResult) -> float:
            s = float(res.extra.get("rrf_score") or 0)
            if sub.prefer and res.engine in sub.prefer:
                s *= 1.6
            if res.kind in ("paper", "project", "dataset"):
                s *= 1.15
            if res.citations:
                s += min(res.citations, 500) / 500 * 0.2
            if res.stars:
                s += min(res.stars, 5000) / 5000 * 0.15
            if res.published:
                s += 0.1 if is_recent(res.published, recency_days) else -0.1
            return s

        ranked = sorted(results, key=score, reverse=True)
        # De-dup identical titles from different URLs.
        seen_titles: set[str] = set()
        out: list[SearchResult] = []
        for res in ranked:
            tkey = re.sub(r"\W+", "", (res.title or "").lower())[:60]
            if tkey and tkey in seen_titles:
                continue
            seen_titles.add(tkey)
            out.append(res)
            if len(out) >= max_keep:
                break
        return out

    def _retrieve_subquestion(
        self,
        sub: SubQuestion,
        registry: SourceRegistry,
        *,
        candidates: int,
        max_keep: int,
        fetch_top_n: int,
        recency_days: int,
    ) -> None:
        raw: list[SearchResult] = []
        # Queries for one sub-question are independent: run them in parallel.
        workers = max(1, min(4, len(sub.queries)))
        with ThreadPoolExecutor(max_workers=workers) as pool:
            for results in pool.map(lambda q: self.router.search(q, per_engine=None), sub.queries):
                raw.extend(results)
        from .search import rrf_fuse

        fused = rrf_fuse([(r.engine, r, i) for i, r in enumerate(raw)], cap=candidates)
        registry.add_many(fused)
        sub.results = self._rank_results(fused, sub, max_keep, recency_days)

        if fetch_top_n > 0 and self.cfg.search.fetch_pages:
            urls = [r.url for r in sub.results[:fetch_top_n] if r.url]
            try:
                sub.pages = fetch_many(
                    urls,
                    timeout=float(self.cfg.search.fetch_timeout),
                    max_chars=int(self.cfg.search.max_page_chars),
                    user_agent=self.cfg.search.user_agent,
                )
            except Exception as exc:  # noqa: BLE001
                log.warning("fetch failed for %s: %s", sub.id, exc)

    # ---------------------------------------------------------------- extract
    def _candidate_block(self, sub: SubQuestion, registry: SourceRegistry) -> str:
        lines: list[str] = []
        for res in sub.results:
            n = registry.index_of(res)
            if n is None:
                continue
            meta = []
            if res.published:
                meta.append(res.published)
            if res.venue:
                meta.append(res.venue)
            if res.citations is not None:
                meta.append(f"citations={res.citations}")
            if res.stars is not None:
                meta.append(f"stars={res.stars}")
            header = f"[{n}] ({res.kind}; {res.engine}{'; ' + ', '.join(meta) if meta else ''}) {res.title}"
            lines.append(header)
            if res.url:
                lines.append(f"    URL: {res.url}")
            if res.snippet:
                lines.append(f"    Snippet: {truncate(res.snippet, 400)}")
            page = sub.pages.get(res.url) if res.url else None
            if page and page.text:
                lines.append(f"    Content: {truncate(page.text, 1500)}")
        return "\n".join(lines)

    def extract(self, sub: SubQuestion, registry: SourceRegistry) -> dict[str, Any]:
        block = self._candidate_block(sub, registry)
        if not block.strip():
            return {"subquestion_id": sub.id, "findings": [], "note": "no candidates retrieved"}
        messages = [
            {"role": "system", "content": self._system("信息抽取者（researcher/extractor）")},
            {
                "role": "user",
                "content": (
                    f"子问题：{sub.question}\n\n"
                    f"候选证据（方括号中的数字是引用编号，必须原样使用）：\n{block}\n\n"
                    "请只根据上面的候选证据进行抽取，输出严格 JSON：\n"
                    "{\n"
                    '  "subquestion_id": "' + sub.id + '",\n'
                    '  "findings": [{"point":"结论/事实","evidence":"支撑细节（可含数字/指标）",'
                    '"sources":[引用编号int,...],"type":"paper|project|dataset|trend|news|benchmark",'
                    '"confidence":"high|medium|low","year":"YYYY或空字符串",'
                    '"heat":"热度证据：引用数/star/下载量/讨论热度，取自候选块的 citations/stars，无则空字符串",'
                    '"authority":"权威证据：发表venue/是否同行评审/官方文档/标准，无则空字符串",'
                    '"attention":"关注度：高|中|低 + 一句依据（引用/star/下载/榜单排名/新闻或社区讨论热度）",'
                    '"recommendation":"推荐度：★1-5 + 一句推荐理由（综合权威+热度+与本主题的相关性；没把握给 ★★★☆☆）"}],\n'
                    '  "key_papers": [{"title":"...","url":"...","why":"为什么重要","year":"...",'
                    '"heat":"引用数等","authority":"venue/出版社","attention":"高|中|低+依据","recommendation":"★1-5+理由"}],\n'
                    '  "key_projects": [{"name":"...","url":"...","why":"...",'
                    '"heat":"stars/采用度","authority":"维护方/是否官方","attention":"高|中|低+依据","recommendation":"★1-5+理由"}],\n'
                    '  "key_datasets": [{"name":"...","url":"...","why":"...",'
                    '"heat":"引用/使用度","authority":"发布方/是否基准","attention":"高|中|低+依据","recommendation":"★1-5+理由"}],\n'
                    '  "open_problems": ["..."]\n'
                    "}\n"
                    "要求：findings 3-8 条，去重，按重要性排序；不确定的写 confidence=low；"
                    "每条 finding 都要给出 heat、authority、attention、recommendation——"
                    "候选块里出现 citations/stars/venue 时必须据此填入，确实没有才留空/给中性值；"
                    "attention 与 recommendation 必须基于候选块里的真实信号，不得编造数字或榜单；"
                    "没有证据的类别返回空数组。只输出 JSON。"
                ),
            },
        ]
        try:
            data = self.llm.json(messages, tier="fast", temperature=0.2, max_tokens=3000)
        except LLMError as exc:
            log.warning("extraction LLM failed for %s (%s); using raw candidates", sub.id, exc)
            data = self._fallback_extraction(sub, registry)
        if not isinstance(data, dict):
            data = self._fallback_extraction(sub, registry)
        data.setdefault("subquestion_id", sub.id)
        return data

    def _fallback_extraction(self, sub: SubQuestion, registry: SourceRegistry) -> dict[str, Any]:
        findings = []
        for res in sub.results[:6]:
            n = registry.index_of(res)
            findings.append(
                {
                    "point": res.title,
                    "evidence": truncate(res.snippet or "", 300),
                    "sources": [n] if n else [],
                    "type": res.kind,
                    "confidence": "low",
                    "year": (res.published or "")[:4],
                    "heat": _heat_text(res),
                    "authority": _authority_text(res),
                    "attention": _attention_text(res),
                    "recommendation": _recommendation_text(res),
                }
            )
        return {"subquestion_id": sub.id, "findings": findings, "key_papers": [], "key_projects": [], "key_datasets": [], "open_problems": []}

    # --------------------------------------------------------------- critique
    def critique(self, topic: Topic, subquestions: list[SubQuestion]) -> dict[str, Any]:
        digest = []
        for sub in subquestions:
            points = [f.get("point", "") for f in (sub.extraction.get("findings") or [])][:5]
            digest.append({"id": sub.id, "question": sub.question, "findings": points})
        messages = [
            {"role": "system", "content": self._system("评审者（critic）")},
            {
                "role": "user",
                "content": (
                    f"研究主题：{topic.title}\n\n已有子问题与发现摘要：\n{dumps(digest)}\n\n"
                    "请评估覆盖度并找出证据缺口，输出严格 JSON：\n"
                    '{"coverage":"一句话评价","gaps":["缺口1","缺口2"],'
                    '"additional_queries":["补充检索词1","补充检索词2"],'
                    '"additional_subquestions":[{"question":"...","queries":["..."]}]}\n'
                    "要求：如果覆盖已经充分，gaps 与 additional_queries 返回空数组。只输出 JSON。"
                ),
            },
        ]
        try:
            data = self.llm.json(messages, tier="strong", temperature=0.3, max_tokens=1500)
        except LLMError as exc:
            log.warning("critique LLM failed (%s)", exc)
            data = {"coverage": "critique unavailable", "gaps": [], "additional_queries": [], "additional_subquestions": []}
        if not isinstance(data, dict):
            data = {"coverage": "", "gaps": [], "additional_queries": [], "additional_subquestions": []}
        return data

    # -------------------------------------------------------------- synthesize
    def synthesize(self, topic: Topic, plan: dict[str, Any], subquestions: list[SubQuestion], registry: SourceRegistry) -> str:
        language = str(self.cfg.research.language)
        lang_rule = LANG_INSTRUCTIONS.get(language, LANG_INSTRUCTIONS["bilingual"])
        refs = registry.reference_list()
        ref_lines = [f"[{r['n']}] {r['title']} — {r['url']}" for r in refs]
        # Keep the synthesis prompt bounded: cap findings and references.
        findings_payload = []
        for sub in subquestions:
            findings_payload.append(
                {
                    "id": sub.id,
                    "question": sub.question,
                    "findings": (sub.extraction.get("findings") or [])[:8],
                    "key_papers": (sub.extraction.get("key_papers") or [])[:6],
                    "key_projects": (sub.extraction.get("key_projects") or [])[:6],
                    "key_datasets": (sub.extraction.get("key_datasets") or [])[:6],
                    "open_problems": (sub.extraction.get("open_problems") or [])[:5],
                }
            )
        seeds = topic.seed_resources
        sections = topic.sections or [
            "摘要（Executive Summary）",
            "一、关键前沿进展",
            "二、分主题深入分析",
            "三、经典与奠基性工作",
            "四、开源项目与工程实践",
            "五、数据集与基准",
            "六、趋势、争议与开放问题",
            "七、建议关注清单（Watchlist）",
        ]
        messages = [
            {"role": "system", "content": self._system("报告撰写者（synthesizer）")},
            {
                "role": "user",
                "content": (
                    f"{lang_rule}\n\n"
                    f"研究主题：{topic.title}\n研究目标：{plan.get('summary', '')}\n\n"
                    f"结构化发现（来自各子问题的检索与抽取）：\n{dumps(findings_payload)}\n\n"
                    f"领域已知的经典/种子资源（可一并纳入“经典/数据集”章节，需保留其链接）：\n{dumps(seeds)}\n\n"
                    f"可引用的证据来源（引用格式为 [n]，只能引用这些编号）：\n" + "\n".join(ref_lines) + "\n\n"
                    "请严格按以下章节结构撰写一份高质量 Markdown 调研报告：\n"
                    + "\n".join(f"- {s}" for s in sections)
                    + "\n\n写作要求：\n"
                    "1. 报告以 `# 标题` 开头，随后是元信息行（日期、领域、检索源数量）。\n"
                    "2. 每个关键论断必须带 [n] 引用；不得引用不存在的编号；不得编造 URL。\n"
                    "3. “经典与奠基性工作”“开源项目”“数据集与基准”用 Markdown 表格呈现"
                    "（列：名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明）。\n"
                    "4. 明确区分“最新进展（近1-2年）”与“经典工作”。\n"
                    "5. 用 `> 待核实` 标注证据不足的判断。\n"
                    "6. 每个关键条目/结论都要给出四类可核查证据：**热度证据**（引用数 citations、GitHub star、"
                    "下载量、讨论热度）、**权威证据**（发表 venue、是否同行评审、官方文档/标准、维护机构/作者）、"
                    "**关注度**（高/中/低，说明依据：引用/star/下载/榜单排名/新闻或社区讨论）、"
                    "**推荐度**（★1-5，附一句话推荐理由，综合权威+热度+与本主题的相关性）；"
                    "四类证据都必须带 [n] 引用，证据缺失时写 `> 待核实`，不得编造数字或榜单。\n"
                    "7. 结尾附“参考来源”编号列表（可直接复用上面的来源列表）。\n"
                    "只输出 Markdown 报告正文。"
                ),
            },
        ]
        try:
            text = self.llm.chat(messages, tier="strong", temperature=0.35, max_tokens=int(self.cfg.llm.max_tokens))
            if text and text.strip():
                return text.strip()
        except LLMError as exc:
            log.warning("synthesis LLM failed (%s); emitting deterministic report", exc)
        return self._fallback_report(topic, plan, subquestions, refs)

    def _fallback_report(self, topic: Topic, plan: dict[str, Any], subquestions: list[SubQuestion], refs: list[dict[str, Any]]) -> str:
        lines = [f"# {plan.get('title') or topic.title}", ""]
        lines.append("> 本报告在 LLM 不可用时由检索结果自动生成（降级模式），结论需人工复核。")
        lines.append("")
        lines.append("## 摘要")
        lines.append(plan.get("summary") or topic.description)
        lines.append("")
        for sub in subquestions:
            lines.append(f"## {sub.question}")
            for finding in sub.extraction.get("findings") or []:
                srcs = " ".join(f"[{n}]" for n in (finding.get("sources") or []) if isinstance(n, int))
                lines.append(f"- {finding.get('point', '')} {srcs}".rstrip())
            lines.append("")
        lines.append("## 参考来源")
        for r in refs:
            lines.append(f"[{r['n']}] {r['title']} — {r['url']}")
        return "\n".join(lines)

    # -------------------------------------------------------------------- run
    def run(
        self,
        topic: Topic,
        *,
        query: str = "",
        depth: str | None = None,
        rounds: int | None = None,
        progress: Progress | None = None,
    ) -> ResearchResult:
        depth = depth or str(self.cfg.research.depth)
        preset = DEPTH_PRESETS.get(depth, DEPTH_PRESETS["standard"])
        max_subquestions = int(self.cfg.research.max_subquestions)
        max_subquestions = min(max_subquestions, preset["max_subquestions"]) if depth != "standard" else max_subquestions
        max_rounds = int(rounds or self.cfg.research.max_rounds)
        max_rounds = max(1, min(max_rounds, preset["max_rounds"] if depth != "standard" else max_rounds))
        max_keep = int(preset["results_per_subquestion"])
        candidates = int(preset["candidates"])
        fetch_top_n = int(self.cfg.search.fetch_top_n)
        if depth != "standard":
            fetch_top_n = int(preset["fetch_top_n"])

        started = now_utc()
        registry = SourceRegistry()
        self._topic_keywords = {
            str(k).strip().lower() for k in (topic.keywords or []) if str(k).strip()
        } | {topic.name.lower()}
        self._say(progress, f"[plan] topic={topic.name} depth={depth} rounds={max_rounds}")

        plan = self.plan(topic, query, max_subquestions)
        subquestions = [
            SubQuestion(
                id=str(s["id"]),
                question=str(s["question"]),
                queries=list(s["queries"]),
                rationale=str(s.get("rationale", "")),
                prefer=list(s.get("prefer", [])),
            )
            for s in plan["subquestions"]
        ]

        critiques: list[dict[str, Any]] = []
        actual_rounds = 1
        for rnd in range(1, max_rounds + 1):
            actual_rounds = rnd
            self._say(progress, f"[round {rnd}] retrieving {len(subquestions)} sub-question(s) from {len(self.router.engines)} engines")
            with ThreadPoolExecutor(max_workers=6) as pool:
                futures = {
                    pool.submit(
                        self._retrieve_subquestion,
                        sub,
                        registry,
                        candidates=candidates,
                        max_keep=max_keep,
                        fetch_top_n=fetch_top_n,
                        recency_days=int(self.cfg.research.recency_days),
                    ): sub
                    for sub in subquestions
                }
                for fut in as_completed(futures):
                    sub = futures[fut]
                    try:
                        fut.result()
                    except Exception as exc:  # noqa: BLE001
                        log.warning("retrieve failed for %s: %s", sub.id, exc)
                    self._say(progress, f"    {sub.id}: {len(sub.results)} sources")

            for sub in subquestions:
                sub.extraction = self.extract(sub, registry)
                n = len(sub.extraction.get("findings") or [])
                self._say(progress, f"    {sub.id}: {n} findings")

            if rnd >= max_rounds:
                break
            critique = self.critique(topic, subquestions)
            critiques.append(critique)
            new_subs = self._subquestions_from_critique(critique, subquestions, rnd)
            keep_queries = [q for q in (critique.get("additional_queries") or []) if isinstance(q, str) and q.strip()]
            if keep_queries:
                # Attach extra queries to the most relevant existing sub-question.
                subquestions[0].queries = list(dict.fromkeys(subquestions[0].queries + keep_queries[:2]))
            if not new_subs:
                self._say(progress, "[critique] coverage sufficient; stopping early")
                break
            self._say(progress, f"[critique] gap-filling with {len(new_subs)} new sub-question(s)")
            subquestions.extend(new_subs)

        self._say(progress, "[synthesize] writing report")
        report_md = self.synthesize(topic, plan, subquestions, registry)
        finished = now_utc()
        result = ResearchResult(
            topic=topic.name,
            title=plan.get("title") or topic.title,
            query=query,
            depth=depth,
            language=str(self.cfg.research.language),
            started_at=started.replace(microsecond=0).isoformat(),
            finished_at=finished.replace(microsecond=0).isoformat(),
            duration_s=(finished - started).total_seconds(),
            rounds=actual_rounds,
            plan=plan,
            subquestions=subquestions,
            critiques=critiques,
            report_md=report_md,
            references=registry.reference_list(),
            engines=self.router.engine_names,
            skills=[s.name for s in self.skills],
            llm_stats=self.llm.stats(),
            models={"primary": self.llm.model, "tiers": dict(self.llm.tiers)},
        )
        return result

    def _subquestions_from_critique(self, critique: dict[str, Any], existing: list[SubQuestion], rnd: int) -> list[SubQuestion]:
        out: list[SubQuestion] = []
        seen = {s.question.strip().lower() for s in existing}
        raw = critique.get("additional_subquestions") or []
        for i, item in enumerate(raw, start=1):
            if not isinstance(item, dict):
                continue
            question = str(item.get("question") or "").strip()
            if not question or question.lower() in seen:
                continue
            queries = [str(q).strip() for q in (item.get("queries") or []) if str(q).strip()] or [question]
            out.append(
                SubQuestion(
                    id=f"r{rnd+1}q{i}",
                    question=question,
                    queries=queries[:4],
                    rationale="critique gap",
                    round=rnd + 1,
                )
            )
            seen.add(question.lower())
            if len(out) >= 3:
                break
        return out
