"""``rb`` — the research-bot management CLI.

Commands
--------
    rb doctor                 connectivity + configuration self-check
    rb run ...                run the deep-research pipeline (the headless tool)
    rb serve ...              run the HTTP research service
    rb skills [list|show]     inspect DeerFlow-format skills (local + submodule)
    rb topics [list|show]     inspect research topics
    rb report [list|show]     inspect the report archive / push ledger
    rb engines [list|test]    inspect the multi-source search layer
    rb config [show|init]     inspect or bootstrap configuration
"""

from __future__ import annotations

import argparse
import json
import logging
import sys

from . import __version__
from .config import DEFAULTS, find_home, load_config, load_dotenv
from .emailer import is_configured, send_digest, send_report
from .engine import DEPTH_PRESETS, DeepResearchEngine
from .knowledge import build_knowledge_topic, evaluate_coverage, get_frame
from .llm import LLM, LLMError
from .report import git_metadata, load_index, record_email, save_report
from .search import ENGINE_REGISTRY, SearchRouter
from .skills import load_skills
from .topics import load_topics, resolve_topics
from .util import truncate

log = logging.getLogger("research_bot")


def _setup_logging(verbose: bool) -> None:
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.INFO,
        format="%(asctime)s %(levelname)-7s %(name)s: %(message)s",
        datefmt="%H:%M:%S",
    )
    logging.getLogger("httpx").setLevel(logging.WARNING)


def _progress(msg: str) -> None:
    print(msg, file=sys.stderr, flush=True)


# ---------------------------------------------------------------------------
# run
# ---------------------------------------------------------------------------
def cmd_run(args: argparse.Namespace) -> int:
    cfg, home = load_config(args.config, find_home())
    if args.no_fetch:
        cfg.search.fetch_pages = False
    if args.depth:
        cfg.research.depth = args.depth
    if args.query:
        cfg.research.extra_query = args.query

    frame = "watch" if args.watch else "knowledge" if args.knowledge else None
    if frame:
        seed = args.query or " ".join(args.topic or [])
        if not seed:
            print(f"--{frame} needs a domain: pass --query '...' or --topic '...'", file=sys.stderr)
            return 2
        skill = get_frame(frame).skill
        names = list(cfg.research.skills or [])
        if skill not in names:
            cfg.research.skills = [*names, skill]
        topics = [build_knowledge_topic(seed, frame=frame, language=str(cfg.research.language))]
    else:
        topics = resolve_topics(load_topics(home), args.topic or ["all"])
    if not topics:
        print("no topics found; create topics/*.yaml or pass --topic", file=sys.stderr)
        return 2

    engine = DeepResearchEngine(cfg, home)
    print(f"research-bot {__version__} · home={home} · engines={engine.router.engine_names}", file=sys.stderr)
    print(f"topics={[t.name for t in topics]} · depth={cfg.research.depth} · skills={[s.name for s in engine.skills]}", file=sys.stderr)

    run_meta = {"git": git_metadata(home), "run_url": git_metadata(home).get("run_url", "")}
    saved: list[tuple] = []
    failed: list[str] = []
    for topic in topics:
        print(f"\n=== {topic.name}: {topic.title} ===", file=sys.stderr)
        try:
            result = engine.run(topic, query=args.query or "", depth=args.depth, rounds=args.rounds, progress=_progress)
            record, md_path = save_report(home, cfg, result, run_meta=run_meta)
        except Exception as exc:  # noqa: BLE001 - one topic must not abort the run
            log.exception("topic %s failed", topic.name)
            print(f"  ! topic {topic.name} failed: {exc}", file=sys.stderr)
            failed.append(topic.name)
            continue
        saved.append((topic, result, record, md_path))
        print(
            f"  → {md_path.relative_to(home)}  ({record['sources']} sources, {record['findings']} findings, "
            f"{record['duration_s']}s)",
            file=sys.stderr,
        )

    # ---- knowledge / watch coverage ---------------------------------------
    coverage: list[dict] = []
    if frame:
        for _, result, _, _ in saved:
            report = evaluate_coverage(result, frame=frame)
            coverage.append(report.to_dict())
            print(f"\n[{frame}] coverage score={report.score}/100  sourced={report.sourced_ratio:.0%}", file=sys.stderr)
            for gap in report.gaps:
                print(f"  gap: {gap}", file=sys.stderr)
            if not report.gaps:
                print("  no gaps — all facets covered, discipline satisfied", file=sys.stderr)

    # ---- email delivery -----------------------------------------------------
    push_requested = args.email or (cfg.email.enabled and not args.no_email)
    if push_requested:
        if getattr(cfg.email, "digest", False) and len(saved) > 1:
            paths = [p for _, _, _, p in saved]
            rec = send_digest(cfg.email, [r for _, r, _, _ in saved], report_paths=paths, dry_run=args.dry_run_email)
            for _, _, record, _ in saved:
                record_email(home, cfg, record, rec)
            print(f"  email(digest): sent={rec['sent']} to={rec['to']} error={rec['error']}", file=sys.stderr)
        else:
            for _, result, record, md_path in saved:
                rec = send_report(cfg.email, result, report_path=md_path, dry_run=args.dry_run_email)
                record_email(home, cfg, record, rec)
                print(f"  email[{result.topic}]: sent={rec['sent']} to={rec['to']} error={rec['error']}", file=sys.stderr)

    if args.json:
        records = [r[2] for r in saved]
        if frame:
            for record, cov in zip(records, coverage, strict=False):
                record["coverage"] = cov
        print(json.dumps(records, ensure_ascii=False, indent=2))
    if failed:
        print(f"failed topics: {', '.join(failed)}", file=sys.stderr)
    return 0 if saved or not topics else 1


# ---------------------------------------------------------------------------
# doctor
# ---------------------------------------------------------------------------
def cmd_doctor(args: argparse.Namespace) -> int:
    cfg, home = load_config(args.config, find_home())
    ok = True
    print(f"research-bot {__version__}")
    print(f"home: {home}")
    print(f"config file: {args.config or (home / 'config' / 'config.yaml')}")
    print(f"deer-flow submodule: {'present' if (home / 'deer-flow' / 'AGENTS.md').exists() else 'MISSING'}")
    if not (home / "deer-flow" / "AGENTS.md").exists():
        ok = False

    skills = load_skills(home)
    local = [s for s in skills.values() if s.source == "local"]
    upstream = [s for s in skills.values() if s.source == "deer-flow"]
    print(f"skills: {len(local)} local, {len(upstream)} from deer-flow")
    topics = load_topics(home)
    print(f"topics: {len(topics)} → {', '.join(sorted(topics)) or '(none)'}")
    print(f"report dir: {home / cfg.report.dir}")

    print("\nLLM:")
    llm = LLM(cfg.llm)
    print(f"  base_url={llm.base_url} model={llm.model} key={'set' if llm.api_key else 'MISSING'}")
    try:
        reply = llm.chat([{"role": "user", "content": "Reply with the single word: ok"}], max_tokens=8)
        print(f"  connectivity: OK ({truncate(reply.strip(), 40)!r})")
    except LLMError as exc:
        ok = False
        print(f"  connectivity: FAIL — {exc}")

    print("\nSearch engines:")
    router = SearchRouter(cfg.search)
    for name in router.engine_names:
        engine = next(e for e in router.engines if e.name == name)
        try:
            results = engine.search("vision language action robot", limit=2)
            print(f"  {name:18s} OK ({len(results)} results)")
        except Exception as exc:  # noqa: BLE001
            print(f"  {name:18s} FAIL — {truncate(str(exc), 80)}")
    missing = set(cfg.search.engines) - set(router.engine_names)
    for name in sorted(missing):
        print(f"  {name:18s} unavailable (blocked or not configured)")

    print("\nEmail:")
    print(f"  enabled={cfg.email.enabled} configured={is_configured(cfg.email)} to={cfg.email.to}")

    print("\n" + ("doctor: OK" if ok else "doctor: issues found"))
    return 0 if ok else 1


# ---------------------------------------------------------------------------
# serve
# ---------------------------------------------------------------------------
def cmd_serve(args: argparse.Namespace) -> int:
    from .serve import run_server

    print(f"research-bot {__version__} · serving from home={find_home()}", file=sys.stderr)
    return run_server(host=args.host, port=args.port, workers=args.workers, config_path=args.config)


# ---------------------------------------------------------------------------
# skills / topics / engines
# ---------------------------------------------------------------------------
def cmd_skills(args: argparse.Namespace) -> int:
    cfg, home = load_config(args.config, find_home())
    skills = load_skills(home)
    if args.action == "show":
        if not args.name:
            print("usage: rb skills show <name>", file=sys.stderr)
            return 2
        skill = skills.get(args.name)
        if not skill:
            print(f"skill not found: {args.name}", file=sys.stderr)
            return 1
        print(f"# {skill.name}  ({skill.source})\n# {skill.path}\n")
        print(skill.body)
        return 0
    if not skills:
        print("no skills found")
        return 0
    for name in sorted(skills):
        s = skills[name]
        print(f"{name:24s} {s.source:9s} {truncate(s.description, 90)}")
    return 0


def cmd_topics(args: argparse.Namespace) -> int:
    cfg, home = load_config(args.config, find_home())
    topics = load_topics(home)
    if args.action == "show":
        if not args.name:
            print("usage: rb topics show <name>", file=sys.stderr)
            return 2
        topic = topics.get(args.name)
        if not topic:
            print(f"topic not found: {args.name}", file=sys.stderr)
            return 1
        print(json.dumps(topic.to_dict(), ensure_ascii=False, indent=2))
        return 0
    for name in sorted(topics):
        t = topics[name]
        print(f"{name:16s} {t.title}")
        print(f"{'':16s} {truncate(t.description, 100)}")
        print(f"{'':16s} queries={len(t.seed_queries)} venues={len(t.venues)} seeds={sum(len(v) for v in t.seed_resources.values())}")
    return 0


def cmd_engines(args: argparse.Namespace) -> int:
    cfg, home = load_config(args.config, find_home())
    if args.action == "test":
        router = SearchRouter(cfg.search)
        for engine in router.engines:
            try:
                results = engine.search(args.query, limit=3)
                print(f"{engine.name:18s} OK ({len(results)})")
                for r in results[:3]:
                    print(f"    - {truncate(r.title, 80)}  {r.url}")
            except Exception as exc:  # noqa: BLE001
                print(f"{engine.name:18s} FAIL — {truncate(str(exc), 100)}")
        return 0
    print("registered engines:")
    for name in sorted(ENGINE_REGISTRY):
        enabled = "enabled" if name in (cfg.search.engines or []) else "disabled"
        print(f"  {name:18s} {enabled}")
    return 0


# ---------------------------------------------------------------------------
# report
# ---------------------------------------------------------------------------
def cmd_report(args: argparse.Namespace) -> int:
    cfg, home = load_config(args.config, find_home())
    index = load_index(home, cfg)
    if args.action == "show":
        target = args.name
        if not target and index:
            target = index[0]["id"]
        record = next((r for r in index if r["id"] == target), None)
        if not record and target:
            candidate = home / target
            if candidate.is_file():
                print(candidate.read_text(encoding="utf-8"))
                return 0
        if not record:
            print(f"report not found: {target}", file=sys.stderr)
            return 1
        path = home / record["report_path"]
        if path.is_file():
            print(path.read_text(encoding="utf-8"))
        else:
            print(json.dumps(record, ensure_ascii=False, indent=2))
        return 0
    if not index:
        print("no reports yet")
        return 0
    print(f"{'date':12s} {'topic':14s} {'src':>4s} {'find':>5s} {'email':>6s}  title")
    for r in index:
        email = "sent" if (r.get("email") or {}).get("sent") else ("err" if (r.get("email") or {}).get("error") else "-")
        print(
            f"{r.get('date',''):12s} {r.get('topic',''):14s} {r.get('sources',0):4d} "
            f"{r.get('findings',0):5d} {email:>6s}  {truncate(r.get('title',''), 60)}"
        )
    return 0


# ---------------------------------------------------------------------------
# config
# ---------------------------------------------------------------------------
def cmd_config(args: argparse.Namespace) -> int:
    cfg, home = load_config(args.config, find_home())
    if args.action == "init":
        target = home / "config" / "config.yaml"
        if target.exists() and not args.force:
            print(f"config already exists: {target} (use --force to overwrite)")
            return 1
        import yaml

        example = home / "config" / "config.example.yaml"
        text = example.read_text(encoding="utf-8") if example.is_file() else yaml.safe_dump(DEFAULTS, allow_unicode=True)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")
        print(f"wrote {target}")
        return 0
    if args.action == "path":
        path = args.config or (home / "config" / "config.yaml")
        print(path)
        return 0
    print(json.dumps(cfg, ensure_ascii=False, indent=2, default=str))
    return 0


# ---------------------------------------------------------------------------
# parser
# ---------------------------------------------------------------------------
def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="rb", description="Headless deep-research agent for robotics frontier tracking.")
    parser.add_argument("--version", action="version", version=f"research-bot {__version__}")
    parser.add_argument("--config", help="path to config.yaml")
    parser.add_argument("--home", help="repository root (defaults to auto-detect)")
    parser.add_argument("-v", "--verbose", action="store_true")
    sub = parser.add_subparsers(dest="command", required=True)

    p_run = sub.add_parser("run", help="run the deep-research pipeline")
    p_run.add_argument("--topic", action="append", help="topic name (repeatable); default: all")
    p_run.add_argument("--query", help="extra research question / focus")
    p_run.add_argument("--depth", choices=sorted(DEPTH_PRESETS), help="research depth preset")
    p_run.add_argument("--rounds", type=int, help="override max refinement rounds")
    p_run.add_argument("--no-fetch", action="store_true", help="skip full-page fetching")
    p_run.add_argument("--email", action="store_true", help="force email even if disabled in config")
    p_run.add_argument("--no-email", action="store_true", help="never send email")
    p_run.add_argument("--dry-run-email", action="store_true", help="render email but do not send")
    p_run.add_argument("--json", action="store_true", help="print the run records as JSON")
    p_run.add_argument("--knowledge", action="store_true", help="build a 7-facet knowledge map (learn a domain) instead of a topic run")
    p_run.add_argument("--watch", action="store_true", help="build a 7-facet increment report (changes/blue-ocean/industry/society) instead of a topic run")
    p_run.set_defaults(func=cmd_run)

    p_doc = sub.add_parser("doctor", help="self-check connectivity and config")
    p_doc.set_defaults(func=cmd_doctor)

    p_srv = sub.add_parser("serve", help="run the HTTP research service")
    p_srv.add_argument("--host", default="127.0.0.1", help="bind address (default: 127.0.0.1)")
    p_srv.add_argument("--port", type=int, default=8080, help="bind port (default: 8080)")
    p_srv.add_argument("--workers", type=int, default=2, help="concurrent research workers (default: 2)")
    p_srv.set_defaults(func=cmd_serve)

    p_sk = sub.add_parser("skills", help="inspect skills")
    p_sk.add_argument("action", nargs="?", choices=["list", "show"], default="list")
    p_sk.add_argument("name", nargs="?")
    p_sk.set_defaults(func=cmd_skills)

    p_tp = sub.add_parser("topics", help="inspect topics")
    p_tp.add_argument("action", nargs="?", choices=["list", "show"], default="list")
    p_tp.add_argument("name", nargs="?")
    p_tp.set_defaults(func=cmd_topics)

    p_en = sub.add_parser("engines", help="inspect search engines")
    p_en.add_argument("action", nargs="?", choices=["list", "test"], default="list")
    p_en.add_argument("--query", default="embodied AI vision language action", help="query for `test`")
    p_en.set_defaults(func=cmd_engines)

    p_rp = sub.add_parser("report", help="inspect the report archive")
    p_rp.add_argument("action", nargs="?", choices=["list", "show"], default="list")
    p_rp.add_argument("name", nargs="?", help="report id or path for `show`")
    p_rp.set_defaults(func=cmd_report)

    p_cfg = sub.add_parser("config", help="inspect or bootstrap config")
    p_cfg.add_argument("action", nargs="?", choices=["show", "init", "path"], default="show")
    p_cfg.add_argument("--force", action="store_true", help="overwrite existing config on `init`")
    p_cfg.set_defaults(func=cmd_config)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    _setup_logging(getattr(args, "verbose", False))
    if getattr(args, "home", None):
        import os

        os.environ["RESEARCH_BOT_HOME"] = args.home
    load_dotenv(find_home() / ".env")
    return int(args.func(args))


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
