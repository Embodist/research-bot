# Agent 评测与安全：能力基准、欺骗与可纠正性 —— 近两年增量调研报告

- **调研日期**：2026-10-16（UTC）
- **领域**：通用/具身 Agent 能力评测（OSWorld、WebArena、GAIA、SWE-bench、tau-bench 等）与安全评测（欺骗、sandbagging、可纠正性、AI Control）
- **可引用来源**：34 条（编号 [1]–[34]）；其中与主题直接相关者约 12 条，其余为术语噪声或弱相关共享任务论文
- **方法论**：deep-research / frontier-tracking / paper-survey / evidence-grading
- **覆盖自检（必读）**：子问题 q1（能力基准）为**部分覆盖**；q2（欺骗与可纠正性）与 q3（工程/治理基础设施）在本批检索中**基本未命中**目标证据 [13,16,17,18]。因此本报告多处标注 `> 待核实`，并显式区分「有证据的增量」与「证据缺口」。**未检索到的结论不得当领域事实使用。**

---

## 1. 进展与热点（Progress & Hotspots）

> **一句话增量判断**：能力侧评测已明确从「静态问答 / 短程 GUI 操作」迁移到「长程、真实职业、带经济价值」的任务范式；安全侧本批证据仅覆盖 prompt injection 与 sandbagging 的零星线索，scheming / alignment faking / agentic misalignment / sabotage **无直接证据**。

**能力基准：范式迁移（最新进展，2026）**
- **OSWorld 2.0 把计算机使用评测推进到长程真实职业任务** [11]：新增 `task horizon`、`professional-domain distribution`、`economic value` 等任务统计维度，引入 simulated user 与 dynamic environment，评测协议采用 fine-grained partial reward 与 functional/model-based evaluation。
  - **热度证据**：`> 待核实`（[11] 候选块无引用数/star/榜单数据）。
  - **权威证据**：[11] 为 arXiv 预印本 2606.29537v1，未见同行评审记录。
  - **关注度**：低（依据：[11] 无任何量化热度信号）。
  - **推荐度**：★★★★☆（直接命中「静态问答→长程真实任务」主线，但需核实发表状态与第三方复现）。
- **前沿模型仍未解决长程专业计算机使用** [11]：论文自述 Claude Opus 4.8 准确率更高、GPT-5.5 token 效率更高；每提升 1 点准确率的 token 成本呈非线性上升；「更多轮次不买来完成度」，轮次空间前沿由 batching 而非步数设定；额外推理只买到 partial credit 而非完成。
  - **热度证据**：`> 待核实`（[11] 无引用/star/榜单位次）。
  - **权威证据**：[11] 基准作者自评，**无第三方复现证据**。
  - **关注度**：中（依据：涉及 Claude Opus 4.8 / GPT-5.5 前沿模型相对排名，但来源为自评）。
  - **推荐度**：★★★★☆（提供「提升来自推理量还是架构」的量化式判断，是评估该基准是否饱和的关键数据）。

**终端 / 软件 Agent 与 harness 评测分化（最新进展，2026）**
- **Terminal-Bench 2.0 与 Claw-SWE-Bench / ClawBench** [1]：候选块提到面向 terminal agents 的 Terminal-Bench 2.0、面向 OpenClaw 类 harness 的 Claw-SWE-Bench（350 任务），并聚合为 ClawBench & Agentic Web Benchmarks 集合。
  - **热度证据**：ClawBench 数据集 downloads 534、likes 2 [1]。
  - **权威证据**：[1] 为 HuggingFace 社区集合页（Reacherx），非官方基准主页；提及 TIGER-AI-Lab/ClawBench 仓库与 arXiv:2604.08523。
  - **关注度**：低（依据：[1] 下载 534、likes 2，属小规模社区热度）。
  - **推荐度**：★★★☆☆（提示 terminal/harness 评测在分化，但任务数细节被截断，需回查原文）。

**安全评测：prompt injection 攻防（最新进展）**
- **AgentDojo** 提供动态环境以评测 LLM Agent 的 prompt injection 攻击与防御 [31]；**SecAlign** 用偏好优化防御 prompt injection [32]；**StruQ** 用结构化查询防御 prompt injection [33]。
  - **热度证据**：`> 待核实`（三条来源在本批中仅以标题/URL 形式出现，无引用/star 数据）。
  - **权威证据**：均为 arXiv 预印本（[31] 2406.13352v3；[32] 2410.05451v3；[33] 2402.06363v2）。
  - **关注度**：中（依据：prompt injection 为 agent 安全高频议题，但本批无量化信号）。
  - **推荐度**：★★★★☆（Agent 安全评测中最具工程可复现性的方向，建议优先核实）。

**Sandbagging：唯一直接线索（最新进展，2026）**
- [21] 标题为 *Option-Order Randomisation Reveals a Distributional Position Attractor in Prompted Sandbagging*：提示**选项顺序会系统性影响所测得的 sandbagging 行为**，属评测方法学信号（arXiv 2604.26206v1，2026 预印本）。
  - **热度/权威/关注度**：`> 待核实`（本批仅有标题级信息，未见摘要、引用或代码）。
  - **推荐度**：★★★★☆（本主题下唯一直接命中 sandbagging 的可引用来源，务必精读原文后再引用其结论）。

**欺骗评测的边界辨析（最新进展，2025）**
- **SVC 2025 是首个多模态欺骗检测挑战赛，但检测对象是人类的欺骗行为**（安检、反欺诈、可信度评估），**不等同于 AI 策略性欺骗（scheming / alignment faking）评测** [17]。可作为术语边界对照，不可作为后者的验证证据。
  - **权威证据**：[17] arXiv 预印本（cs.CV），挑战赛概述，未见同行评审信息。
  - **关注度**：低（依据：[17] 属细分方向，本批无参赛规模/引用信号）。
  - **推荐度**：★★☆☆☆（仅作边界对照）。

**方法学争议（最新进展，2025）**
- [18] 评阅 2023–2025 年 63 篇同行评审研究，指出合成人格（synthetic persona）实验存在系统性外部效度缺陷：任务与目标人群常被欠说明、生态效度差异大，**削弱依赖人格设定诱发的欺骗 / 对齐伪装类结论的可解释性**。
  - **权威证据**：[18] arXiv 预印本（cs.CY），主体为对 63 篇同行评审研究的二次综述。
  - **关注度**：中（依据：覆盖 63 篇主流会议论文的方法学批评）。
  - **推荐度**：★★★☆☆（元层面证据，评估该类结论可信度时值得参考，但非直接复现）。

**覆盖缺口（必须显式声明）**
- 本批证据**未覆盖** in-context scheming / alignment faking / agentic misalignment / sabotage 的任何评测或其独立复现，也未提供结论争议与反例 [13,16,17,18] → `> 待核实`。
- 时间分布集中在 2025 年，**未覆盖 2024 与 2026 年**的对应安全评测 [13,16,17,18] → 无法据此判断 2024–2026 增量趋势。

**术语噪声提示**
- 「GAIA」在天文语境下指 Gaia 卫星系列 DR1/DR2/DR3 [2,4,6,7,8,9,10]，与通用助手基准 GAIA 无关。检索中此类噪声占比较高，提示基准命名需规范化。

> **最新 vs 经典**：本节条目均为 2025–2026 进展。OSWorld / WebArena / GAIA / SWE-bench / tau-bench 的**原始论文不在本次可引用来源清单内**，其基线定义、任务数与硬件口径均 `> 待核实`，不得凭记忆补写。

---

## 2. 工业界与产品（Industry & Product）

> **一句话增量判断**：本批证据**几乎不覆盖厂商产品、真机部署与量产**，仅有少量第三方团队与社区工件可佐证评测生态的工程化；其余 `> 待核实`。

- **benchflow-ai/awesome-evals** [12]：系统性整理 WebArena、OSWorld、Terminal-Bench、Cybench 等基准与评测方法学讨论，并提及 Agentic AI MOOC (Fall 2025)、Predictable Noise in LLM Benchmarks。
  - **热度证据**：`> 待核实`（[12] 未给 star 或讨论热度）。
  - **权威证据**：GitHub 第三方仓库（benchflow-ai），非官方组织。
  - **关注度**：低（依据：[12] 无量化热度信号）。
  - **推荐度**：★★★☆☆（作为基准发现索引有用）。
- **TIGER-AI-Lab/ClawBench** [1]：HF 数据集 + GitHub 仓库 + 项目主页 claw-bench.com，代表长程 SWE / harness 评测的工程化尝试。
  - **热度证据**：downloads 534、likes 2 [1]。**权威证据**：TIGER-AI-Lab 团队维护。**关注度**：低。**推荐度**：★★★☆☆。
- **零信任安全架构（部署侧线索）**：[34] 提出面向医疗自主 AI 的零信任安全架构，属产品/部署安全工程线索，非厂商产品证据；细节 `> 待核实`。
- **无**任何厂商官方博客、权重开源、量产部署的一手证据 → `> 待核实`。

---

## 3. 蓝海与缺口（Blue Ocean & Gaps）

> **一句话增量判断**：**长程「完成度」度量、token 效率统一指标、以及安全评测的独立复现机制**，是当前最明显的三个无人区。

| # | 缺口 | 证据 | 为什么是蓝海 |
|---|------|------|--------------|
| G1 | 长程任务「最后一公里」度量：额外推理只买到 partial reward 而非完成 [11] | [11] | 现有协议奖励部分得分，缺少「真实完工」指标 |
| G2 | 成本–收益非线性：准确率每升 1 点 token 成本飙升，缺统一指标 [11] | [11] | 需 accuracy–token 联合指标与预算标准化 |
| G3 | SOTA 归属与推理预算口径不统一，缺第三方独立复现 [11] | [11] | 「谁在什么预算下更强」无中立仲裁 |
| G4 | 长程/经济价值任务的规模与难度分级不统一（283 行 vs 350 任务）[1] | [1] | 缺通用任务规模/难度分类标准 |
| G5 | 基准命名与索引规范缺失（GAIA 歧义）[2,4] | [2,4] | 术语治理直接影响检索与引用可靠性 |
| G6 | AI scheming / alignment faking / sandbagging / corrigibility / AI Control 评测证据空白 [13,16,17,18]；唯一 sandbagging 线索仅方法学 [21] | [13,16,17,18,21] | 安全侧最核心的开口 |
| G7 | prompt injection 攻防评测与越狱/欺骗评测尚未整合 [31,32,33] | [31,32,33] | 缺少统一 agent 安全评测栈 |
| G8 | 合成人格实验的任务/人群欠说明与生态效度不足 [18] | [18] | 直接影响欺骗/对齐伪装结论可信度 |

---

## 4. 瓶颈与拐点（Bottleneck & Inflection）

> **一句话增量判断**：能力侧瓶颈已从「会不会做」转为「**能否完工 + 成本是否可控**」；安全侧瓶颈是「**缺可复现的欺骗/可纠正性评测**」。

- **完成度瓶颈**（是否临近拐点：较大概率已到）[11]：额外推理与更多轮次换成 partial credit，而非完成；轮次前沿由 batching 设定。
  - **权威**：[11] 预印本自评；**关注度**：中；**推荐度**：★★★★☆。
- **成本拐点** [11]：每点准确率的 token 成本非线性上升 → 性价比拐点未知，`> 待核实`（缺公开成本-性能表）。
- **评测协议瓶颈** [11]：partial reward 与 completion 之间的度量缺口，是把「分数提升」误读为「能力提升」的主要来源。
- **安全评测缺口即拐点信号**：若 scheming/alignment faking 类结论长期无独立复现，则该方向结论无法定论 `> 待核实` [17,18,21]。
- **方法学瓶颈** [18]：合成人格实验外部效度不足，可能系统性抬高/压低对齐相关结论。

---

## 5. 社会·政策·国际（Society, Policy & Geopolitics）

> **一句话增量判断**：本批来源**几无直接的 AI 治理/标准证据**，仅有间接线索，全部需标 `> 待核实`。

- **间接数据治理线索**：[27] 研究「评估英国政府作为 AI 数据提供者角色」的方法，与数据供给/治理相关，但**不涉及 Agent 评测规则**；细节 `> 待核实`。
- **EU AI Act GPAI、NIST 框架、前沿安全框架、实验室红队承诺**：**不在本次可引用来源清单内** → `> 待核实`，不得据记忆补写具体条款与生效日。
- **标准化缺口具治理外溢**：基准命名歧义 [2,4] 与任务规模口径不一 [1]，会影响监管可核验性与跨机构对比 → 属潜在标准议题。

---

## 6. 资本与生态（Capital & Ecosystem）

> **一句话增量判断**：本周期**无显著可核查的资本/融资/并购证据**。

- 仅见小规模社区生态信号：awesome-evals 索引仓库 [12]（热度 `> 待核实`）；ClawBench 数据集 downloads 534、likes 2 [1]。
- 无融资额、并购、人才流动、公司格局变化的一手证据 → `> 待核实`。
- **本周期无显著变化**。

---

## 7. 信号与预测（Signals & Forecast）

> **一句话增量判断**：三个早期信号——长程完成度、prompt injection 攻防、sandbagging 方法学——最可能在 6–18 个月内形成新评测轴。

- **[P] 长程「完成度」将取代部分「部分得分」成为新 SOTA 轴**（依据：[11] 指出 partial credit 与 completion 脱钩）。**置信度**：中。**可证伪假设**：若到 2027 年底前主流 Agent 榜单出现以「completion rate」而非仅「partial score」为主报指标的基准，则判断成立。
- **[P] prompt injection 攻防将并入 Agent 安全标准评测栈**（依据：[31,32,33] 已成体系）。**置信度**：中高。**可证伪假设**：若 2027 年前出现至少一个被多方独立复现的「agent 安全综合榜」包含注入攻防子项，则成立。
- **[P] sandbagging / corrigibility 评测将从「prompted」走向系统性基准**（依据：[21] 为唯一早期方法学信号）。**置信度**：低–中。**可证伪假设**：若 12 个月内出现含沙箱式放水/可纠正性任务的公开基准与第三方复现，则成立。
- **[P] 第三方复现基础设施仍是蓝海**（依据：[11] SOTA 为作者自评、无独立复现）。**置信度**：中高。
- **[Debated] 合成人格实验效度**：[18] 提出系统性外部效度批评；是否有反方证据 `> 待核实`。
- **[R]**：本批未出现可标注的传闻类信息。
- **Watchlist**：OSWorld 2.0 [11]、ClawBench/Claw-SWE-Bench [1]、AgentDojo 及 inject 攻防 [31,32,33]、Prompted Sandbagging 方法学 [21]、零信任 Agent 部署架构 [34]。

---

## 附：经典与奠基性工作

> 说明：本主题公认的奠基基准（OSWorld、WebArena、GAIA、SWE-bench、tau-bench 等）**其原始论文不在本次可引用来源清单内**，故下表不作数据填列，统一标 `> 待核实`，仅提示后续需补检。

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| OSWorld（原始版） | 待核实 | 待核实 | 待核实 | 待核实 | 待核实 | 待核实 | 待核实 | 公认经典计算机使用基准，本批未检索到原文，`> 待核实` |
| WebArena | 待核实 | 待核实 | 待核实 | 待核实 | 待核实 | 待核实 | 待核实 | 被 [12] 列名但无原文数据，`> 待核实` |
| GAIA（通用助手基准） | 待核实 | 待核实 | 待核实 | 待核实 | 待核实 | 待核实 | 待核实 | 与天文 Gaia [2,4] 术语冲突，`> 待核实` |
| SWE-bench / tau-bench | 待核实 | 待核实 | 待核实 | 待核实 | 待核实 | 待核实 | 待核实 | 本批未检索到原文，`> 待核实` |

---

## 附：开源项目

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| benchflow-ai/awesome-evals | 2025 | benchflow-ai | 待核实（[12] 无 star） | GitHub 第三方仓库 | 低（无量化信号）[12] | ★★★☆☆ | https://github.com/benchflow-ai/awesome-evals | 基准与评测方法学索引 [12] |
| TIGER-AI-Lab/ClawBench | 2026 | TIGER-AI-Lab | downloads 534、likes 2 [1] | 第三方团队维护 | 低 [1] | ★★★☆☆ | https://github.com/TIGER-AI-Lab/ClawBench | 长程 SWE/harness 评测实现 [1]；任务数口径待核实 |
| AgentDojo | 2024 | 待核实 | 待核实 | arXiv 2406.13352v3 [31] | 中 | ★★★★☆ | http://arxiv.org/abs/2406.13352v3 | prompt injection 攻防评测动态环境 [31] |
| SecAlign | 2024 | 待核实 | 待核实 | arXiv 2410.05451v3 [32] | 中 | ★★★★☆ | http://arxiv.org/abs/2410.05451v3 | 用偏好优化防御 prompt injection [32] |
| StruQ | 2024 | 待核实 | 待核实 | arXiv 2402.06363v2 [33] | 中 | ★★★★☆ | http://arxiv.org/abs/2402.06363v2 | 用结构化查询防御 prompt injection [33] |

---

## 附：数据集与基准

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| OSWorld 2.0 | 2026 | 待核实 | 待核实（[11] 无引用/star） | arXiv 2606.29537v1（预印本，未见同行评审）[11] | 低–中 [11] | ★★★★☆ | https://arxiv.org/html/2606.29537v1 | 长程职业计算机使用 + partial reward + 模拟用户 [11] |
| ClawBench（dataset） | 2026 | TIGER-Lab | downloads 534、likes 2 [1] | HuggingFace 第三方数据集 [1] | 低 [1] | ★★★☆☆ | https://huggingface.co/datasets/TIGER-Lab/ClawBench | 283 行任务/评分标准；与 Claw-SWE-Bench 350 任务口径不一致，`> 待核实` [1] |
| Terminal-Bench 2.0 | 2026 | 待核实 | 待核实 | 仅见于社区集合页 [1] | 低 [1] | ★★☆☆☆ | https://huggingface.co/collections/Reacherx/clawbench-and-agentic-web-benchmarks | 终端 agent 评测数据集；二手线索，需回查官方 [1] |
| AgentDojo | 2024 | 待核实 | 待核实 | arXiv 2406.13352v3 [31] | 中 | ★★★★☆ | http://arxiv.org/abs/2406.13352v3 | prompt injection 攻击/防御评测环境 [31] |
| SVC 2025（多模态欺骗检测） | 2025 | 待核实 | 待核实 | arXiv 2508.04129v1 [17] | 低 [17] | ★★☆☆☆ | http://arxiv.org/abs/2508.04129v1 | **人类**欺骗检测挑战赛，非 AI scheming 评测，仅作边界对照 [17] |

---

## 参考来源

[1] ClawBench & Agentic Web Benchmarks - a Reacherx Collection — https://huggingface.co/collections/Reacherx/clawbench-and-agentic-web-benchmarks
[2] The Gaia mission — http://arxiv.org/abs/1609.04153v1
[3] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1
[4] Gaia Data Release 2. Summary of the contents and survey properties — http://arxiv.org/abs/1804.09365v2
[5] Gaia Data Release 3: The Galaxy in your preferred colours — http://arxiv.org/abs/2206.06215v2
[6] Gaia Data Release 1. Summary of the astrometric, photometric, and survey properties — http://arxiv.org/abs/1609.04172v1
[7] Gaia Data Release 3: Exploring and mapping the diffuse interstellar band at 862 nm — http://arxiv.org/abs/2206.05536v1
[8] Gaia Data Release 2: Kinematics of globular clusters and dwarf galaxies — http://arxiv.org/abs/1804.09381v3
[9] Gaia Early Data Release 3: Structure and properties of the Magellanic Clouds — http://arxiv.org/abs/2012.01771v4
[10] Gaia Early Data Release 3: Summary of the contents and survey properties — http://arxiv.org/abs/2012.01533v2
[11] OSWorld 2.0: Benchmarking Computer Use Agents on Long-Horizon Real-World Tasks — https://arxiv.org/html/2606.29537v1
[12] GitHub - benchflow-ai/awesome-evals: A curated, non-BS library of ... — https://github.com/benchflow-ai/awesome-evals
[13] Overview of the Sensemaking Task at the ELOQUENT 2025 Lab — http://arxiv.org/abs/2507.12143v1
[14] LongEval at CLEF 2025: Longitudinal Evaluation of IR Model Performance — http://arxiv.org/abs/2503.08541v1
[15] Normalization of peer-evaluation measures of group research quality across academic disciplines — http://arxiv.org/abs/1006.3863v2
[16] Annif at SemEval-2025 Task 5: Traditional XMTC augmented by LLMs — http://arxiv.org/abs/2504.19675v2
[17] SVC 2025: the First Multimodal Deception Detection Challenge — http://arxiv.org/abs/2508.04129v1
[18] Whose Personae? Synthetic Persona Experiments in LLM Research and Pathways to Transparency — http://arxiv.org/abs/2512.00461v1
[19] CEA-LIST at CheckThat! 2025: Evaluating LLMs as Detectors of Bias and Opinion in Text — http://arxiv.org/abs/2507.07539v1
[20] Apollo: Band-sequence Modeling for High-Quality Audio Restoration — http://arxiv.org/abs/2409.08514v2
[21] Option-Order Randomisation Reveals a Distributional Position Attractor in Prompted Sandbagging — http://arxiv.org/abs/2604.26206v1
[22] A Simulation and Modeling of Access Points with Definition Language — http://arxiv.org/abs/1304.1836v2
[23] Superconductivity as a consequence of an ordering of the electron gas zero-point oscillations — http://arxiv.org/abs/1005.0280v6
[24] Intutionistic Fuzzy Ideals in Γ-semiring — http://arxiv.org/abs/1011.5746v2
[25] VLSP 2025 MLQA-TSR Challenge: Vietnamese Multimodal Legal QA on Traffic Sign Regulation — http://arxiv.org/abs/2510.20381v1
[26] Culturally Grounded Physical Commonsense Reasoning in Italian and English — http://arxiv.org/abs/2510.22631v1
[27] Methods to Assess the UK Government's Current Role as a Data Provider for AI — http://arxiv.org/abs/2412.09632v2
[28] DeDisCo at the DISRPT 2025 Shared Task: Discourse Relation Classification — http://arxiv.org/abs/2509.11498v4
[29] CLaC at SemEval-2025 Task 6: Corporate Environmental Promise Verification — http://arxiv.org/abs/2505.23538v1
[30] AINL-Eval 2025 Shared Task: Detection of AI-Generated Scientific Abstracts in Russian — http://arxiv.org/abs/2508.09622v1
[31] AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents — http://arxiv.org/abs/2406.13352v3
[32] SecAlign: Defending Against Prompt Injection with Preference Optimization — http://arxiv.org/abs/2410.05451v3
[33] StruQ: Defending Against Prompt Injection with Structured Queries — http://arxiv.org/abs/2402.06363v2
[34] Caging the Agents: A Zero Trust Security Architecture for Autonomous AI in Healthcare — http://arxiv.org/abs/2603.17419v1

---

> **检索局限声明**：本报告基于以上 34 条来源。子问题 q2（欺骗与可纠正性）与 q3（工程/治理基础设施）在本批检索中未命中目标证据，故 scheming / alignment faking / agentic misalignment / sabotage 的**评测存在性与独立复现结论均标 `> 待核实`**；EU AI Act GPAI、NIST、前沿安全框架等政策文本亦不在来源清单内，未作实质陈述。凡标 `> 待核实` 的判断，均不得作为领域事实引用，需补充检索后再定论。

---

*Generated by research-bot · topic=`agent-评测与安全能力基准欺骗与可纠正性` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`deepseek-v4-flash` · sources=34 · duration=214s · 2026-10-16T22:32:54+00:00*
