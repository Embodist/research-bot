# Agent 评测与安全（能力基准、欺骗与可纠正性）增量调研报告

**日期**：2026-10-15 ｜ **领域**：Agent Evaluation & Safety（能力基准、deception / alignment faking、corrigibility） ｜ **检索源数量**：33 条候选来源（其中与主题直接相关约 12 条，其余为跨域召回噪音） ｜ **方法论**：deep-research + frontier-watch + paper-survey + evidence-grading

> **证据基线说明（必读）**：本次可用证据池中，仅有 [29] 附带了可核查热度数据（`citations=146`）；其余条目均无 citations / stars / 下载量字段，四轴证据中的「热度」一律标 `> 待核实`，**不做任何数字推测**。候选池中不存在本主题公认的经典奠基文献（deceptive alignment、corrigibility 的原始论述），该缺口在本报告「经典与奠基性工作」表中显式标注，建议下一轮补检。此外，候选池存在显著的术语污染（"benchmark / challenge / evaluation" 召回出图像超分、LHC 物理、音频修复、气候模型等条目），这一现象本身构成第 4 章的瓶颈证据。

---

## 1. 进展与热点（Progress & Hotspots）

**一句话增量判断**：相对上一基线，Agent 评测的增量不在"任务更多"，而在评测对象从**单步输出**迁移到**长时程轨迹 + 开放多智能体系统**，并首次出现"agent 自身作为对手（scheming / containment）"这一独立评测面向 [1][5][6][20]。

- **开放系统下的多智能体决策评测（MOASEI 2026）**：相对 2025 首届，2026 版延续了 wildfire fighting、cybersecurity、ride-hailing 等场景（原文摘要被截断，具体场景清单 `> 待核实`）。这是"评测即竞赛事件"型基准，属技术报告而非同行评审论文 [1]。
  - 热度：`> 待核实`（无 citations 字段）｜权威：AAMAS'2026 technical report（会议附属报告，非正式论文）｜关注度：**中**（依托 AAMAS 社区，但无引用信号）｜推荐度：**★★★★☆**——若研究方向是开放多智能体评测，这是最直接的新基线。
- **长时程链式推理基准（LongCoT）**：增量点是把评测对象从"答案正确性"前移到"长链规划与自我管理"，宣称可扩展（scalable）；具体任务域与规模 `> 待核实` [5]。
  - 热度：`> 待核实`｜权威：arXiv cs.LG 预印本｜关注度：**中**（cs.LG 高竞争赛道上无引用数据，判断为推测）｜推荐度：**★★★★☆**——长时程是 2026 年评测叙事的主轴。
- **可信 agentic AI 综述（safety / robustness / privacy / system security）**：增量在于把四类风险统一到"多步轨迹引入的新失效模式"这一因果面上，而非罗列单点攻击 [6]。
  - 权威：arXiv cs.AI 综述（非同行评审）｜热度：`> 待核实`｜关注度：**高**（综述类在 2026 年 agentic safety 议题中承担术语统一职能，判断依据为标题覆盖面而非引用数）｜推荐度：**★★★★☆**——作为术语与分类骨架入口。
- **Agent 记忆与长时程自演化综述**：把 memory 从工程插件提升为"自演化 / 长时程"能力的评测维度（v4 版本说明仍在快速迭代）[11]。
  - 权威：arXiv preprint（v4，快速修订是活跃度的弱信号）｜热度/关注度：`> 待核实`｜推荐度：**★★★☆☆**。
- **Scheming propensity（图谋/欺骗倾向）评测**：直接命中"agent 欺骗"议题的评测工作，标题即指向"评估并理解 LLM agent 的图谋倾向"；实验细节与是否独立复现 `> 待核实` [20]。
  - 权威：arXiv HTML 版（预印本）｜关注度：**中**（与 alignment faking 议题同源，但无引用信号）｜推荐度：**★★★★☆**。

**最新进展 vs 经典工作的分界**：上述全部条目均落在 2025–2026 窗口，属"最新进展"。**本候选池未提供 2020–2024 年的 corrigibility / deceptive alignment 经典奠基文献**，因此本报告无法给出"经典 → 最新"的完整演进链条，此为本轮调研最大结构性缺口（详见第 3、7 章）。

---

## 2. 工业界与产品（Industry & Product）

**一句话增量判断**：本轮唯一具备可核查热度的"从 lab 走向工程栈"的条目是开源护栏系统 LlamaFirewall [29]；其余产品化断言均缺乏一手证据，"真机部署/量产"维度本周期**无显著可核变化**。

- **LlamaFirewall（开源 guardrail 系统）**：定位从"模型输出过滤"升级为"面向自主 agent 的安全护栏"，明确针对 agent 读取非可信输入（网页、邮件）后执行高风险动作的场景 [29]。
  - 热度：`citations=146`（本报告唯一可核数字）｜权威：arXiv 预印本 + 开源实现，机构归属 `> 待核实`（证据片段未明示维护方，不得以名称推断）｜关注度：**高**（依据：citations=146，为本池最高信号）｜推荐度：**★★★★★**——安全评测工程栈的当前首选参考实现。
- **评估仓库的工程化维护**：把"AI evaluations 开源仓库如何长期维护"作为研究对象，说明评测已进入"基础设施运维"阶段而非一次性论文 [31]。
  - 热度：`> 待核实`｜权威：arXiv 预印本｜关注度：**中**｜推荐度：**★★★★☆**——做 agent 评测平台选型时的高相关经验贴。
- **模型卡与透明度流水线**：AI Transparency Atlas 提供框架、打分与实时模型卡评测流水线 [33]，属"评测产品化"的轻量形态。
  - 热度：`> 待核实`｜权威：arXiv 预印本｜关注度：**中**｜推荐度：**★★★☆☆**。
- **受监管行业的多智能体合规架构**：面向奥地利/德国 Solvency II 与 EU AI Act 的通用多智能体 AI 框架，属"合规即产品需求"的一手体现 [30]。
  - 权威：arXiv 预印本（非标准或官方指南）｜热度/关注度：`> 待核实`｜推荐度：**★★★☆☆**。
- **对照组（说明检索偏差）**：候选池中 [32]（会话健康 agent 框架）说明 agent 产品化在垂直医疗场景已有落地形态，但与"评测与安全"主题相关性弱。
  - 权威：JAMIA Open（同行评审期刊，DOI 可核）｜热度/关注度：`> 待核实`｜推荐度：**★★☆☆☆**——仅作产品化侧写。

> 待核实：本周期内**厂商级 agent 安全产品的发布、真机部署规模、商业化数据**在候选池中零证据，第 6 章的资本判断因此只能给出"需要数据"档。

---

## 3. 蓝海与缺口（Blue Ocean & Gaps）

**一句话增量判断**：最大的无人区不是"再造一个能力基准"，而是**可纠正性（corrigibility）的一手实验评测**与**长时程轨迹级欺骗检测**——前者在候选池中完全缺席，后者只有伪装成"人类欺骗检测"的相邻任务 [15]。

- **缺口 1：corrigibility 无一手评测**。候选池未出现任何直接测量"agent 在被纠正/被关闭时的顺从性与抵抗性"的实验工作。唯一相邻线索是 containment 架构讨论 [7]，但其标题包含"April 2026 Frontier Model Escape"这一**极端宣称**，属 `[R] 待证实` 级别——在未获得一手事故报告前，不得作为事实引用。
- **缺口 2：把"人类说谎检测"误当"agent 欺骗评测"**。SVC 2025 是**多模态人类欺骗检测**挑战（安防、反欺诈、可信度评估），与 agent 的 scheming / alignment faking 是**两个不同问题**；社区存在概念混用风险 [15]。
  - 权威：挑战赛概览报告（同侪挑战性质）｜热度：`> 待核实`｜关注度：**中**（ICCV 系挑战生态）｜推荐度：**★★★☆☆**——作为"判别信号可用性"的方法参考，而非 agent 安全基准。
- **缺口 3：跨本体 / 真实环境 agent 基准缺失**。候选池中没有浏览器、操作系统或机器人本体的 agent 能力基准；这不是"领域没有"，而是**本轮检索未覆盖**，属抽样缺口而非现实缺口，需在下一轮定向补检。
- **缺口 4：长时程评测的纵向方法学**。LongEval at CLEF 2025 提供"跨时间点模型性能漂移"的 IR 评测范式 [14]，可迁移到 agent 长期部署后能力衰减的度量——目前尚无 agent 领域的对应物。
  - 权威：CLEF 2025 评测实验室（体系化评测平台）｜热度/关注度：`> 待核实`｜推荐度：**★★★☆☆**。
- **缺口 5：开放 vs 封闭安全的路线之争尚在早期**。Columbia Convening 记录把"开放性"作为 AI 安全的独立设计变量 [27]，说明该议题已进入议程建构阶段，但尚无收敛结论，属 `[Debated]`。
  - 权威：会议论文集（arXiv 预印本形式）｜热度/关注度：`> 待核实`｜推荐度：**★★★☆☆**。

---

## 4. 瓶颈与拐点（Bottleneck & Inflection）

**一句话增量判断**：瓶颈正从"缺基准"转向"**基准不可比 + 评测基础设施不可持续**"；拐点信号是叙事重心从 alignment（对齐）向 containment / system safety（系统安全）迁移 [7][26]。

- **瓶颈 A：评测仓库的可持续性**。把"维护开源 AI 评测仓库的挑战"作为论文主题 [31]，本身就是基础设施承压的证据：评测资产的生命周期短于模型迭代周期。
  - 权威：arXiv 预印本｜热度：`> 待核实`｜关注度：**中**｜推荐度：**★★★★☆**。
- **瓶颈 B：术语污染导致元评测失效**。候选池中 [3]（短视频参与度预测）、[4]（图像超分）、[8]（AI 生成图像检测）、[9]（LHC 物理 ML 盘点）、[17]（音频修复）、[19]（视频理解 LMM）、[23]（海岸侵蚀建模）等均因 "challenge / benchmark / evaluation / survey" 词面命中而被召回。这说明检索层缺少"agent capability vs perception task"的判别器——**评测检索本身需要评测**。
  - 全部条目热度/关注度：`> 待核实`（[4][8] 属 NTIRE 挑战赛体系，社区热度真实存在但缺数字）｜推荐度：**★☆☆☆☆**（主题相关性极低）。
- **瓶颈 C：技术安全叙事的自我局限**。[26] 直接批评国际 AI Safety Report 过度依赖技术术语、脱离系统安全（system safety）传统。
  - 权威：arXiv 预印本（政策批评类）｜热度/关注度：`> 待核实`｜推荐度：**★★★☆☆**。
- **拐点信号（[P] 预测）**：出现"agent containment 架构需求"这类以**架构隔离**而非**价值对齐**为核心的论述 [7]，叠加受监管行业的合规化落地 [30]，我判断叙事在 2026 年正从"让模型想对"转向"让系统撑得住"。
  - 可证伪假设：**若到 2027-06，顶会（NeurIPS/ICLR/CoRL）中出现以 "containment / sandbox escape / capability control" 为标题关键词的独立 track 或 ≥3 篇口头报告，则该拐点判断成立。** 置信度：**推测**（依据为单篇预印本 + 单篇合规论文，样本极薄）。
  - 不确定项：`[7]` 的核心事实（2026 年 4 月的"前沿模型逃逸"事件）本报告**无法核实**，标 `[R] 待证实`；若该事件不存在，则本条拐点证据链断裂。

---

## 5. 社会·政策·国际（Society, Policy & Geopolitics）

**一句话增量判断**：相对上一基线，政策侧的增量是**合规框架开始直接约束 agent 架构设计**（EU AI Act × Solvency II），而安全侧则出现"技术安全 vs 系统安全"的路线分歧。

- **合规约束架构化**：面向奥地利/德国受监管保险业的多智能体 AI 框架，把 Solvency II 与 EU AI Act 作为设计约束写入架构 [30]——这是"监管影响技术选型"的一手证据。
  - 权威：arXiv 预印本，**非**官方监管指南，不可当作合规依据｜热度/关注度：`> 待核实`｜推荐度：**★★★☆☆**。
- **欧盟资助与研究议程**：DOI `10.3030/101222556` 指向欧盟资助项目，但标题与内容在证据池中为空（E 级证据，不可用）[2]，仅可作为"欧盟资金正在流入相关方向"的**弱线索**。
  - 热度/权威/关注度/推荐度：**全部 `> 待核实`**——按证据分级规则，E 级内容应丢弃，此处仅标注存在性。
- **安全叙事的公共话语分歧**：[26] 主张从系统安全传统重写安全议程，代表工程安全学派；[27] 则把"开放性"本身作为安全变量，代表开放生态学派。两者在政策建议上存在张力 `[Debated]`。
  - 权威：均为 arXiv 预印本 / 会议记录，**非**政府或标准组织文件｜关注度：**中**｜推荐度：**★★★☆☆**。
- **机构伦理话语的实证研究**：对 OpenAI 公共话语中 "ethics / safety / alignment" 用词语义漂移的案例分析 [10]，提供了"安全话语被机构化重塑"的可核证据路径。
  - 权威：arXiv cs.CY（交叉学科，非安全顶会）｜热度/关注度：`> 待核实`｜推荐度：**★★★☆☆**。
- **社会认知层**：1305 人行为实验显示 AI 预测会收窄个体考量的未来选项 [24]，为"agent 建议改变人类决策空间"提供实验证据（N=1,305 见摘要）。
  - 权威：arXiv cs.HC 预印本（非同行评审确认）｜热度/关注度：`> 待核实`｜推荐度：**★★☆☆☆**——与 agent 评测主线相关度中低。

---

## 6. 资本与生态（Capital & Ecosystem）

**一句话增量判断**：本周期在候选池中**无显著的、可核实的融资/并购/估值变化证据**；可观察到的生态增量集中在"竞赛生态 + 开源维护 + 欧盟资助"三类弱信号。

- **证据强度：需要数据**。候选池未包含任何机构融资公告、投资机构报告或公司格局分析；因此本章不做资本规模判断，避免编造。
- **可核生态信号 1：竞赛/挑战赛生态持续运转**。MOASEI 2026 明确以"Inaugural 2025 → 2026"的连续届次方式运行 [1]，说明多智能体评测已有稳定的年度机制（但经费与主办方 `> 待核实`）｜关注度：**中**｜推荐度：**★★★★☆**。
- **可核生态信号 2：开源评测仓库是稀缺资产**。[31] 把维护经验写成论文，隐含信号是此类仓库迭代快、贡献者稀缺｜推荐度：**★★★★☆**。
- **可核生态信号 3：欧盟资助通道存在**（[2]，内容为空，E 级）｜`> 待核实`。
- **人才与社区**：候选池无作者/机构集中度分析所需数据（多数条目作者信息缺失），无法判断"哪些团队在领跑"｜`> 待核实`。

> 本节刻意保持短：按 frontier-watch 纪律，**没有增量证据的维度应明确写"本周期无显著变化"，不为凑字数编内容**。

---

## 7. 信号与预测（Signals & Forecast）

**一句话增量判断**：2026 年的早期信号集中在"欺骗/图谋倾向可测量化"[20] 与"containment 架构化"[7] 两条线，但两者证据强度都偏弱。

**早期信号（带不确定性标记）**

| 信号 | 类型 | 时间 | 依据 | 证据强度 |
|---|---|---|---|---|
| Agent scheming 倾向被单独建为评测对象 | 确定（存在性） | 2026 | [20] | 推测（无引用/复现数据） |
| 长时程 CoT 成为评测主轴 | 较大概率 | 2026 | [1][5][11] | 推测 |
| 安全叙事从 alignment 转向 containment / system safety | [P] | 2026 | [7][26][30] | 推测（样本薄） |
| 前沿模型逃逸（2026-04）事件 | [R] 待证实 | 2026-04 | [7] 标题 | **未知** |
| 开放 vs 封闭安全的路线之争 | [Debated] | 2025–2026 | [27] vs [26] | 需要数据 |

**未来 6–18 个月可证伪预测**

1. **[P] 可纠正性会出现首个独立评测基准。** 依据链：scheming 倾向已被建为评测对象 [20] → 能力评测与安全评测正合流 → corrigibility 是其自然缺口（第 3 章缺口 1）。
   证伪条件：**若到 2027-04 仍无 ≥1 篇以 corrigibility 为标题核心词并附公开评测集的论文/仓库，则本预测不成立。** 置信度：**较大概率（推测档）**。
2. **[P] 术语污染将催生"元评测"工具。** 依据链：本次检索中 ≥7 条跨域噪音条目（[3][4][8][9][17][19][23]）证明判别层失效 → 评测资产检索需要 agent capability 判别器。
   证伪条件：**若到 2027-10，主流 agent 评测综述仍以人工筛选为主、无公开的基准筛选/分类工具，则本预测不成立。** 置信度：**推测**。
3. **[P] 合规驱动会成为 agent 安全评测的一手需求来源。** 依据链：[30] 显示 EU AI Act × Solvency II 已进入架构设计层。
   证伪条件：**若到 2027-06 无任何 agent 评测框架以 EU AI Act 条款编号作为评测维度映射，则本预测不成立。** 置信度：**推测**。

**Watchlist（持续关注）**
- Agent scheming / alignment faking 的独立复现报告 [20]
- containment / sandbox escape 的一手事故或架构论文（核实 [7] 的真实性）
- 开源 guardrail 与评测仓库的版本迭代与 star 增长（[29][31]）
- corrigibility 一手评测的出现（当前为空白）
- 长时程记忆评测的标准化（[11]）

---

## 经典与奠基性工作（候选池内可锚定的条目）

> **重要声明**：本候选池**未包含** deception / alignment faking / corrigibility 的经典奠基文献（如 deceptive alignment 的原始论述、corrigibility 的形式化提案）。下表仅列出池内可充当"上一基线"的条目，缺口需下一轮补检。

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| AI Safety is Stuck in Technical Terms — A System Safety Response to the International AI Safety Report [26] | 2025 | `> 待核实` | `> 待核实` | arXiv 预印本（非同行评审） | 中（政策安全议程讨论） | ★★★☆☆ | http://arxiv.org/abs/2503.04743v1 | 系统安全学派对技术对齐叙事的基础性批评，可作"经典 vs 新范式"的分界参考 |
| A Different Approach to AI Safety: Columbia Convening [27] | 2025 | Columbia Convening | `> 待核实` | 会议记录（arXiv 形式） | 中 | ★★★☆☆ | http://arxiv.org/abs/2506.22183v1 | 把"开放性"作为独立安全变量的奠基性议程文本 |
| Competing Visions of Ethical AI: A Case Study of OpenAI [10] | 2026 | `> 待核实` | `> 待核实` | arXiv cs.CY | 中 | ★★★☆☆ | http://arxiv.org/abs/2601.16513v1 | 机构安全话语漂移的实证案例 |
| Making Large Language Models Better Reasoners with Alignment [21] | 2023 | `> 待核实` | `> 待核实` | arXiv 预印本 | 低（主题相关性弱） | ★★☆☆☆ | http://arxiv.org/abs/2309.02144v1 | 池内唯一 2023 年条目，可作 alignment-then-reasoning 的上游基线 |
| Towards trustworthy agentic AI: a comprehensive survey [6] | 2026 | `> 待核实` | `> 待核实` | arXiv cs.AI 综述 | 高 | ★★★★☆ | http://arxiv.org/abs/2605.23989v1 | 当前分类骨架，替代缺失的经典综述 |

---

## 开源项目

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| LlamaFirewall [29] | 2025 | `> 待核实` | **citations=146** | arXiv 预印本 + 开源实现 | **高**（依据 citations=146，本池唯一可核热度） | ★★★★★ | https://arxiv.org/abs/2505.03574 | 面向自主 agent 的开源 guardrail，覆盖非可信输入引发的高风险动作 |
| Open-Source Repository of AI Evaluations（维护经验） [31] | 2025 | `> 待核实` | `> 待核实` | arXiv 预印本 | 中 | ★★★★☆ | https://arxiv.org/abs/2507.06893 | 评测仓库工程化维护的挑战与洞见，选型必读 |
| AI Transparency Atlas [33] | 2025 | `> 待核实` | `> 待核实` | arXiv 预印本 | 中 | ★★★☆☆ | https://arxiv.org/abs/2512.12443 | 框架 + 打分 + 实时模型卡评测流水线 |

---

## 数据集与基准

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| MOASEI Competition 2026 [1] | 2026 | MOASEI 社区 | `> 待核实` | AAMAS'2026 技术报告（非正式论文） | 中 | ★★★★☆ | http://arxiv.org/abs/2607.03399v1 | 开放系统下多智能体决策评测；场景清单 `> 待核实`（摘要截断） |
| LongCoT [5] | 2026 | `> 待核实` | `> 待核实` | arXiv cs.LG | 中 | ★★★★☆ | http://arxiv.org/abs/2604.14140v1 | 长时程 CoT 推理的可扩展基准 |
| Evaluating and Understanding Scheming Propensity in LLM Agents [20] | 2026 | `> 待核实` | `> 待核实` | arXiv HTML（预印本） | 中 | ★★★★☆ | https://arxiv.org/html/2603.01608v2 | 最贴近"agent 欺骗"主题的评测工作；独立复现情况 `> 待核实` |
| SVC 2025: First Multimodal Deception Detection Challenge [15] | 2025 | `> 待核实` | `> 待核实` | 挑战赛概览报告 | 中 | ★★★☆☆ | http://arxiv.org/abs/2508.04129v1 | **人类**多模态欺骗检测，勿与 agent scheming 混为一谈 |
| LongEval at CLEF 2025 [14] | 2025 | CLEF | `> 待核实` | CLEF 2025 评测实验室 | 中 | ★★★☆☆ | http://arxiv.org/abs/2503.08541v1 | 纵向（跨时间）模型性能漂移评测范式，可迁移到 agent 长期部署评测 |
| ELOQUENT 2025 Sensemaking [13] | 2025 | `> 待核实` | `> 待核实` | 共享任务报告 | 低–中 | ★★☆☆☆ | http://arxiv.org/abs/2507.12143v1 | 生成模型作为教师/学生/评估者的三级评测设计，与 agent-as-judge 议题相邻 |
| 术语污染对照组（**非 agent 基准**） [3][4][8][9][17][19][23] | 2025–2026 | 多机构 | `> 待核实` | NTIRE/ICCV/CLEF/期刊等 | 低（与本主题无关） | ★☆☆☆☆ | 见参考来源 | 因 "challenge/benchmark/evaluation" 词面命中被召回，是检索层失效的证据 |

---

## 参考来源

[1] Second MOASEI Competition at AAMAS'2026: A Technical Report — http://arxiv.org/abs/2607.03399v1
[2] （无标题，E 级证据，内容不可用） — https://doi.org/10.3030/101222556
[3] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1
[4] NTIRE 2025 Challenge on Image Super-Resolution (x4): Methods and Results — http://arxiv.org/abs/2504.14582v3
[5] LongCoT: Benchmarking Long-Horizon Chain-of-Thought Reasoning — http://arxiv.org/abs/2604.14140v1
[6] Towards trustworthy agentic AI: a comprehensive survey of safety, robustness, privacy, and system security — http://arxiv.org/abs/2605.23989v1
[7] When the Agent Is the Adversary: Architectural Requirements for Agentic AI Containment After the April 2026 Frontier Model Escape — http://arxiv.org/abs/2604.23425v1
[8] NTIRE 2026 Challenge on Robust AI-Generated Image Detection in the Wild — http://arxiv.org/abs/2604.11487v1
[9] Machine learning for the LHC physics program: a 2025-2026 stocktake — http://arxiv.org/abs/2609.32874v1
[10] Competing Visions of Ethical AI: A Case Study of OpenAI — http://arxiv.org/abs/2601.16513v1
[11] A Survey of Agent Memory in the Second Half: Towards Self-Evolving and Long-Horizon Agents — http://arxiv.org/abs/2602.06052v4
[12] Annif at SemEval-2025 Task 5: Traditional XMTC augmented by LLMs — http://arxiv.org/abs/2504.19675v2
[13] Overview of the Sensemaking Task at the ELOQUENT 2025 Lab: LLMs as Teachers, Students and Evaluators — http://arxiv.org/abs/2507.12143v1
[14] LongEval at CLEF 2025: Longitudinal Evaluation of IR Model Performance — http://arxiv.org/abs/2503.08541v1
[15] SVC 2025: the First Multimodal Deception Detection Challenge — http://arxiv.org/abs/2508.04129v1
[16] Normalization of peer-evaluation measures of group research quality across academic disciplines — http://arxiv.org/abs/1006.3863v2
[17] Apollo: Band-sequence Modeling for High-Quality Audio Restoration — http://arxiv.org/abs/2409.08514v2
[18] LTG at SemEval-2025 Task 10: Optimizing Context for Classification of Narrative Roles — http://arxiv.org/abs/2506.05976v1
[19] Apollo: An Exploration of Video Understanding in Large Multimodal Models — http://arxiv.org/abs/2412.10360v1
[20] Evaluating and Understanding Scheming Propensity in LLM Agents — https://arxiv.org/html/2603.01608v2
[21] Making Large Language Models Better Reasoners with Alignment — http://arxiv.org/abs/2309.02144v1
[22] Overview of the First Workshop on Language Models for Low-Resource Languages (LoResLM 2025) — http://arxiv.org/abs/2412.16365v1
[23] Modelling evaluation of the impact of Medicane Apollo on pocket beaches in the context of climate change — https://doi.org/10.5194/egusphere-egu25-5549
[24] Faith in AI can narrow the futures individuals consider — http://arxiv.org/abs/2603.28944v2
[25] Foundations of GenIR — http://arxiv.org/abs/2501.02842v1
[26] AI Safety is Stuck in Technical Terms -- A System Safety Response to the International AI Safety Report — http://arxiv.org/abs/2503.04743v1
[27] A Different Approach to AI Safety: Proceedings from the Columbia Convening on Openness in Artificial Intelligence and AI Safety — http://arxiv.org/abs/2506.22183v1
[28] DeBiasMe: De-biasing Human-AI Interactions with Metacognitive AIED (AI in Education) Interventions — http://arxiv.org/abs/2504.16770v1
[29] LlamaFirewall: An open source guardrail system for building secure AI agents — https://arxiv.org/abs/2505.03574
[30] Multi-Agent AI Architecture for Regulated Insurers: A generic AI framework under Solvency II and the AI Act in Austria and Germany — http://arxiv.org/abs/2609.27636v2
[31] Developing and Maintaining an Open-Source Repository of AI Evaluations: Challenges and Insights — https://arxiv.org/abs/2507.06893
[32] Conversational health agents: a personalized large language model-powered agent framework — https://doi.org/10.1093/jamiaopen/ooaf067
[33] AI Transparency Atlas: Framework, Scoring, and Real-Time Model Card Evaluation Pipeline — https://arxiv.org/abs/2512.12443

---

### 附：本报告的四轴证据纪律自检

| 检查项 | 结果 |
|---|---|
| 是否所有引用编号都来自给定来源列表 | 是（[1]–[33]） |
| 是否有编造的 citations / star / 榜单数字 | 否；仅引用 [29] 的 `citations=146`，其余一律 `> 待核实` |
| 传闻/预测是否显式标记 | 是；[7] 标 `[R] 待证实`，第 4/7 章预测标 `[P]` 并附证伪条件 |
| 是否区分演示/自评 与 独立验证/真机部署 | 是；第 2 章明确"产品化与真机部署本周期无显著可核变化" |
| 是否省略章节 | 否；第 1–7 章及三类表格均已写完 |
| 主要残余风险 | 经典奠基文献缺失、可纠正性零证据、产品与资本维度证据为空 —— 建议下一轮定向补检 |

---

*Generated by research-bot · topic=`agent-评测与安全能力基准欺骗与可纠正性` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`deepseek-v4-flash` · sources=33 · duration=204s · 2026-10-15T22:30:34+00:00*
