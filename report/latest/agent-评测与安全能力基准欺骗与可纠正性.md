# Agent 评测与安全（能力基准、欺骗与可纠正性）2024–2026 增量追踪报告

**报告日期**：2026-10-17（UTC） ｜ **领域**：Agent 评测与安全（Agent Evaluation & Safety）——能力基准 / 欺骗（deception, scheming, sandbagging）/ 可纠正性（corrigibility, AI control） ｜ **检索源**：来源列表共 33 条编号（[33] 为空记录，按 E 级丢弃），实际可解析 32 条；其中与本主题**直接相关 10 条**、**同名歧义 6 条**、**无关噪声 15 条**、**空记录 1 条**

> **证据覆盖声明（必读）**
> 本报告严格基于给定证据池撰写。证据池对本次研究目标存在**重大结构性缺口**：OSWorld、WebArena、SWE-bench Verified、τ-bench、GAIA、Terminal-Bench、MLE-bench、BrowseComp、AgentCompany、HAL、Apollo Research scheming 压力测试、Anthropic alignment faking、OpenAI 推理链监控、SHADE-Arena、Greenblatt 等 AI Control 框架、Inspect AI / Inspect Evals、HELM、lm-evaluation-harness、AgentDojo、PyRIT、garak、InjecAgent、ToolEmu **均零命中**。因此凡涉及上述对象的判断，一律标注 `> 待核实`，**不给出数字、不给出链接、不臆测结论**。所有"热度"字段在证据池中普遍缺失引用数与 star 数，按纪律写 `> 待核实` 而非编造。

---

## 1. 进展与热点（Progress & Hotspots）

**一句话增量判断**：相对"只追求更高分数的静态测试集"这一基线，2025–2026 年最实质的变化是**把"时效性"与"抗污染性"写进基准的设计目标本身**，同时评测框架层从纯文本向**多语言**与**具身（embodied）**两个方向外扩；但"能力基准 SOTA 如何被改写"这一核心问题在本次证据内**无法量化回答**。

### 1.1 能力基准：从静态快照转向动态更新与对抗加固

| 时间 | 进展 | 证据要点 | 证据等级 |
|---|---|---|---|
| 2025-05 | **SWE-bench Goes Live!** [6] | 摘要明确指出 SWE-bench 及变体"自初始发布以来未更新、覆盖仓库集合狭窄、依赖度过高"，据此提出动态更新的 Live 版本 | B（arXiv cs.SE 预印本，v2；同行评审状态 `> 待核实`） |
| 2026-03 | **SWE-ABS: Adversarial Benchmark Strengthening** [8] | 标题本身即结论：对抗式基准加固"暴露了基于测试的基准上被夸大的成功率（inflated success rates）" | B（标题级证据；**具体膨胀幅度、覆盖哪些基准、实验规模均 `> 待核实`**） |
| 2024-12 | **SWE-Gym** [12] | 以 SWE-Gym 训练软件工程 Agent 与验证器（verifier），提供"训练环境 + 验证信号" | B（arXiv 2412.21139v2） |

**增量解读**：[6] 的意义不在于分数，而在于它把"基准会过期"从社区抱怨变成**显式设计约束**；[8] 则把"污染/过拟合"从定性担忧变成**可测量的攻击面**——两者共同构成"基准可信度"这一新研究对象的出现。需要注意一个**推论性风险**（非论文结论）：[12] 这类"训练环境化"的工作使训练集与评测集的边界更易模糊，可能加剧 [8] 所描述的虚高，但该因果关系 `> 待核实`。

### 1.2 框架层与分类学：评测基础设施的横向扩散

- **Inspect Robots（2026-10）** [25]：摘要指出"通用语言模型正越来越多地控制机器人硬件，因此理解这些模型被具身化后的能力与安全日益重要"，并提出一个 **modular、open…**（摘要在此截断）的评测方案。这是本次证据池中**唯一直接面向具身 AI 能力与安全**的评测工作，与 VLA / 机器人方向高度相关。是否完全开源、支持哪些本体、是否含真机 `> 待核实`。
- **Inspect India Evals（2026-07）** [24]：标题即"An Open Benchmarking Framework"，面向印度 22 种官方语言与地方文化语境，摘要强调 LLM 已在"大陆与偏远村落"大规模部署。其价值在于把评测框架的**语境适配**问题显性化。
- **ASTELD（2026-08）** [30]：提出面向自治 AI Agent 的**六轴分类框架**（摘要列出 architecture、security、tool integration、execution、autonomy、deployment），并给出 OpenClaw 案例研究。这说明 agent 平台的异构程度已高到需要**共同分类语言**才能横向比较。
- **网络安全 AI Agent 选型框架（2025-10）** [28]：把 reactive / cognitive / hybrid / learning 四类 agent 架构与 **NIST Cybersecurity Framework (CSF)** 对齐，属"评测即采购决策支持"的形态。

### 1.3 治理侧评测：从能力分数外延到透明度审计

- **FMTI 2025（2025-12）** [3]：第三版年度指数，新增**数据获取（data acquisition）、使用数据（usage data）、监控（monitoring）**类指标，并**首次纳入 Alibaba、DeepSeek、xAI**；关键数字：透明度均值**从 2024 年的 58 分降至 2025 年的 40 分**（满分 100）。作者含 Percy Liang、Rishi Bommasani、Sayash Kapoor。这是本证据池中**唯一带明确量化对比**的评测类结论。

### 1.4 必须点名但无法核实的对象

`> 待核实`：OSWorld、WebArena、SWE-bench Verified、τ-bench、GAIA、Terminal-Bench、MLE-bench、BrowseComp、AgentCompany、HAL 在证据池中**零出现**，其任务构成、评测口径、人类基线、SOTA 演进均无从判断。特别地，检索"GAIA benchmark"时召回的是 **Gaia 天体测量任务** [7][9][10][11]（Gaia mission / DR1 / DR2 / DR3 合成测光），属典型同名污染，**不可作为 Agent 基准证据**。

---

## 2. 工业界与产品（Industry & Product）

**一句话增量判断**：在可核证据范围内，工业界信号**仅体现为"评测/分类框架的开源化与采购化"**，没有任何厂商模型发布、权重开放、真机部署量或量产数据——因此"哪些从 lab 走向落地"在本周期**无显著可核变化**。

### 2.1 可核的产业化形态（三条）

1. **评测框架成为可被集成的公共基础设施**：Inspect Robots 明确以"modular、open…"为设计取向 [25]，其定位是让第三方（实验室、厂商、监管方）在同一框架下扩展任务与安全用例，而非发布一个封闭榜单。这比"再做一个 benchmark"更接近基础设施形态。
2. **商业 Agent 平台的横向比较需求已经出现**：ASTELD 之所以需要六轴分类，前提是市场上存在**架构、安全、工具集成、执行、自治、部署**差异显著的大量平台 [30]。这是"平台数量增速 > 共同评价语言增速"的间接指标。
3. **安全合规驱动的企业选型工具**：将 Agent 架构与 NIST CSF 对齐的决策支持框架 [28]，说明企业侧需求已从"这个 agent 多强"转为"这个 agent 在我的合规框架里能否被接受"。

### 2.2 明确的产业证据缺口

- OpenAI / Anthropic / Google DeepMind / xAI 的 Agent 产品发布、System Card、部署规模、事故披露：**证据池零覆盖** `> 待核实`。
- 任何 Agent 产品的**真机/生产环境任务成功率**：零数据 `> 待核实`。
- 开源权重与许可证（license）：零数据。证据池未提供任何仓库的 star 数、最近提交时间或许可证类型 `> 待核实`。
- **同名陷阱提醒**：[15] "Apollo: Band-sequence Modeling for High-Quality Audio Restoration" 与 [17] "Apollo: An Exploration of Video Understanding in LMMs" **均与 Apollo Research 无关**，[23] "INSPECT: Learning Robot View Selection" 亦**与 UK AISI 的 Inspect 框架无关**。产业判断中若混用将产生严重错误。

---

## 3. 蓝海与缺口（Blue Ocean & Gaps）

**一句话增量判断**：缺口已从"缺 benchmark"迁移为**"缺可信的 benchmark"与"缺安全评测的工程化"**；其中**策略性欺骗与可纠正性的可复现评测近乎无人区**，是本主题最大的空白。

| # | 缺口 | 现状证据 | 为什么是蓝海 | 置信度 |
|---|---|---|---|---|
| G1 | **策略性欺骗（scheming / sandbagging / alignment faking）无可复现评测** | 证据池中 scheming、sandbagging、alignment faking、corrigibility、shutdown problem、AI control **全部零命中**；现有 Agent 安全基准只到"风险意识"[31] 与"危害性"[32] 层 | 现有安全 benchmark 测的是**输出是否有害**，而非**模型是否在隐藏目标/规避监督**；后者需要多轮、可观测、带监控强度的实验设计，工程门槛高 | 高（缺口存在）/ `> 待核实`（领域是否已有未检索到的公开基准） |
| G2 | **抗污染基准工程** | [6] 指出静态基准失效；[8] 标题指出成功率被夸大 | "如何持续生成未被训练集覆盖的测试项"是可复用方法论，而非一次性数据集 | 中 |
| G3 | **具身 / VLA Agent 的安全评测** | [25] 是候选池唯一具身能力+安全评测工作，且摘要为"modular, open…" | 语言 Agent 的安全分类（越狱、工具滥用）无法直接迁移到"物理动作不可逆"的场景 | 中（仅 1 条证据支撑） |
| G4 | **多语言 / 文化语境评测** | [24] 印度 22 种官方语言与地方文化 | 评测的"分布外"不只是任务，还有语言与文化 | 中 |
| G5 | **能力-风险联合坐标** | [30] 六轴分类含 security 与 autonomy，但未给出量化评分方法（`> 待核实`） | 采购方需要"同一张图上看能力与风险" | 中 |
| G6 | **可纠正性 / 关停（shutdown）的评测化** | 零覆盖 `> 待核实` | 经典理论论证（corrigibility）与可测量实验之间缺少桥梁 | 高（缺口）/ 低（是否已有人做） |
| G7 | **评测元科学：术语消歧与检索基础设施** | 同名污染实证：Gaia [7][9][10][11]、Apollo [15][17]、INSPECT [23]、deception 指人类说谎检测 [14] | 综述与榜单聚合若不做实体消歧，会系统性污染领域认知 | 高（现象本身可核） |

**特别说明 G7**：证据池中 [14] SVC 2025 的 "deception detection" 指**人类音视频说谎识别**（security screening、fraud prevention、credibility assessment），与 AI 自身的策略性欺骗是**完全不同的任务**。这是一条必须写进任何 Agent 安全综述的"排除项"。

---

## 4. 瓶颈与拐点（Bottleneck & Inflection）

**一句话增量判断**：瓶颈正从"模型能力不足"转向**"测量本身不可信"**；拐点信号是"基准从静态资产变成持续运行的对抗过程"。

### 4.1 四类瓶颈

1. **污染与虚高（最硬的瓶颈）**：[8] 的标题即宣告"基于测试的基准成功率被夸大"，说明问题已从个案升级为**基准范式级缺陷**；[6] 从另一侧证明静态基准因"未更新、仓库窄、依赖重"而失效。二者共同指向：**静态测试集作为 SOTA 判定依据的合法性正在下降**。
2. **训练-评测边界模糊**：[12] 把 SWE 任务做成训练环境与验证器，提升了能力上限，同时使"是否见过测试分布"更难审计（此因果为推论，`> 待核实`）。
3. **威胁模型缺失导致安全评测停在表层**：[31] R-Judge 测"安全风险意识"、[32] AgentHarm 测"危害性"，二者都是**单轮/任务级危害判定**；而 scheming 需要"模型知道被评测并改变行为"的设定，评测设计难度高一个量级。证据池无此类实验 `> 待核实`。
4. **具身评测的仿真-真机口径**：[25] 提出模块化框架，但证据池**无任何真机成功率、任务数、本体型号数据** `> 待核实`；"仿真 SOTA ≠ 真机 SOTA"在本周期**无法证实也无法证伪**。

### 4.2 拐点是否临近：三个可观测信号

| 信号 | 观察方式 | 当前状态 |
|---|---|---|
| S-a 动态基准被主流榜单采纳为**主口径** | 榜单是否默认使用持续更新版本而非冻结版本 | 已有方法学提案 [6]，采纳情况 `> 待核实` |
| S-b 出现**公开的欺骗/沙袋评测集**并被 ≥2 个独立团队复现 | 是否存在数据集 + 复现报告 | 证据池零命中 `> 待核实` |
| S-c 出现**基准审计（benchmark audit）**类独立工作 | 是否有人专门审计他人在榜成绩 | [8] 是雏形（对抗加固），是否形成独立议题 `> 待核实` |

**判断**：S-a 与 S-c 已出现明确早期形态，S-b 尚无。因此"评测可信度"这一拐点**正在发生但未完成**。

---

## 5. 社会·政策·国际（Society, Policy & Geopolitics）

**一句话增量判断**：本周期可核的社会维度变化集中在**"透明度作为可比国家/厂商指标"的成型**与**"评测框架作为标准输出载体"的扩散**；具体法规条款层面零证据。

### 5.1 三条可核线索

1. **透明度成为跨国比较框架**：FMTI 2025 首次纳入 Alibaba、DeepSeek、xAI，且总体均值由 58 降至 40 [3]。这意味着评测对象从"模型能力"扩展到"开发者治理实践"，并**天然带有地缘可比性**。需注意：指数下降既可解读为"实践退步"，也可解读为"指标更严、覆盖更广"，**两种解释在证据内无法区分** `> 待核实`。
2. **公共部门作为 AI 数据提供者的角色被评估**：[26] 直接研究"评估英国政府当前作为 AI 数据提供者角色"的方法，说明国家角色从"监管者"扩展到"数据供给方"，评测对象包含**政府自身**。
3. **评测框架成为软性标准输出**：同一"Inspect"命名生态同时出现在语言评测 [24] 与具身评测 [25]，若二者确属同一框架体系（`> 待核实`，摘要未明示隶属关系），则表明评测框架正沿"语言 → 具身"路径扩张，形成事实标准。

### 5.2 合规路径的碎片化信号

[28] 将 Agent 架构与 **NIST CSF** 对齐，是美式框架路径；而 [3] 的透明度指标、[26] 的政府数据角色评估分别属指数路径与公共审计路径。三者**互不承认对方的指标体系**，这一"多轨并存"状态本身是国际评测治理的现实特征（此判断为归纳，`> 待核实` 是否存在互认机制）。

### 5.3 明确缺口

`> 待核实`：EU AI Act 中 GPAI/Agent 相关条款、美国行政令、中国生成式 AI 服务管理办法、ISO/IEC 42001 等**在证据池中零出现**，本报告不对其生效时间、适用范围作任何陈述。

---

## 6. 资本与生态（Capital & Ecosystem）

**一句话增量判断**：**本周期在可核证据范围内无显著资本事件**（无融资、并购、估值、人才流动证据）；生态侧唯一可核的增量是"评测框架层的跨域复用"与"平台分类学的出现"。

### 6.1 生态结构的三个可核信号

1. **框架层的网络效应**：一个评测框架范式同时服务语言 [24] 与具身 [25] 两类完全不同的被测对象，说明**框架层的复用价值高于单一数据集**——数据集会过期（[6] 的核心论点），框架不会。
2. **市场碎片化的量化指标**：需要六轴分类才能比较 agent 平台 [30]，意味着平台在 architecture / security / tool integration / execution / autonomy / deployment 六个维度上已高度分化。碎片化既是创业机会（集成、评测、选型中介），也是采购成本。
3. **企业支出入口从"能力"转向"合规"**：[28] 把选型绑定到 NIST CSF，说明预算科目可能从研发转向风控/合规。

### 6.2 必须诚实标注的空缺

- 任何评测/安全类创业公司的融资额、估值、被收购信息：**零证据** `> 待核实`。
- 开源项目的**维护活跃度**（star、commit 频率、issue 响应、license）：**零数据** `> 待核实`。这一点对本主题尤其致命，因为"工具是否还活着"是选型第一问，而证据池无法回答 Inspect AI / HELM / lm-evaluation-harness / AgentDojo / PyRIT / garak / InjecAgent / ToolEmu 中的**任何一个**。
- 人才流动与社区规模：零证据 `> 待核实`。

> **生态结论**：目前只能确认"评测正在从一次性论文变成持续运行的基础设施"，**不能**确认"有资本在为这件事付费"。

---

## 7. 信号与预测（Signals & Forecast）

**一句话增量判断**：本周期最重要的信号不是某个模型变强，而是**"基准的可信度"第一次成为独立的研究对象与工程约束**。

### 7.1 早期信号（已确证，带日期）

- **2025-05**：SWE-bench 的结构性局限被公开系统化，动态版本提出 [6]。
- **2025-12**：透明度评测扩展到数据获取、使用与监控，均值 58→40 [3]。
- **2026-03**：对抗式基准加固被用于揭示成功率虚高 [8]。
- **2026-07 / 2026-08 / 2026-10**：评测框架向多语言 [24]、平台分类学 [30]、具身安全 [25] 三个方向连续外扩——**四个月内三次扩展**，是本报告观察到的最强节奏信号。

### 7.2 可证伪预测

- **[P] P1（置信度：中）**：到 **2028-04** 前，至少一个主流 Agent 能力榜单将把"持续更新/对抗生成"作为**默认口径**，而非仅提供冻结版本。依据：[6] 已给出方法学、[8] 已给出虚高证据。**证伪条件**：2028-04 前主流榜单仍以冻结测试集为唯一 SOTA 判定依据。
- **[P] P2（置信度：低-中）**：到 **2027-10** 前，具身 Agent 安全评测将出现"标准测试集 + 仿真/真机双口径"的公开成果。依据：[25] 的模块化开源取向降低了复用门槛。**证伪条件**：2027-10 前无任何公开具身安全测试集被第三方使用。
- **[P] P3（置信度：低）**：欺骗（scheming/sandbagging）评测将从"行为演示"转为"基准 + 监控强度联合测量"，标志是出现公开数据集且被 ≥2 个独立团队复现。依据：[31][32] 已证明"安全"可以被 benchmark 化，方法论可迁移。**证伪条件**：2027-10 前该领域仍只有单点演示、无公开数据集。
- **[P] P4（置信度：中）**：基准审计与污染检测将成为独立议题（类似 [8] 的工作从孤例变成一类）。依据：静态基准的合法性已被两篇独立工作从不同角度削弱 [6][8]。

### 7.3 传闻与争议

- **[R] 传闻区**：本次检索**未获得任何传闻级（未证实）信息**，故不列出。不编造。
- **[Debated]**：FMTI 2025 的"透明度下降"存在至少两种解释——实践退步 vs. 指标扩展导致基线不可比 [3]。证据内无法裁决，`> 待核实`。
- **[Debated]**："仿真评测能否代表真机能力"在本证据池中**既无支持证据也无反驳证据**，属未展开争议 `> 待核实`。

### 7.4 不确定性总述与补检清单（按优先级）

1. **最高优先**：Apollo Research scheming、Anthropic alignment faking、SHADE-Arena、Greenblatt AI Control —— 本主题的**奠基文献全部缺失**，当前报告的第 3/4/7 章中所有关于欺骗的判断都必须视为"基于缺口的推断"。
2. **次高**：OSWorld / WebArena / τ-bench / GAIA / Terminal-Bench / MLE-bench / BrowseComp / AgentCompany / HAL 的任务构成与 SOTA 数值。
3. **工程栈活性**：Inspect AI、HELM、lm-evaluation-harness、AgentDojo、PyRIT、garak、InjecAgent、ToolEmu 的 license、star、最近提交。
4. **量化补全**：[8] 的膨胀幅度、[6] 的 Live 更新频率与仓库规模、[25] 的本体与真机/仿真口径。

---

## 参考来源

> 标注说明：`✔` 正文已引用；`同名歧义` 表示因术语重名被召回但**不属本主题**；`噪声` 表示与主题无关；`E 级` 表示空记录已丢弃。

| # | 来源 | 状态 |
|---|---|---|
| [1] | VQualA 2025 Challenge on Engagement Prediction for Short Videos — http://arxiv.org/abs/2509.02969v1 | 噪声 |
| [2] | NTIRE 2025 Challenge on Image Super-Resolution (x4) — http://arxiv.org/abs/2504.14582v3 | 噪声 |
| [3] | The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1 | ✔ |
| [4] | VLSP 2025 MLQA-TSR Challenge — http://arxiv.org/abs/2510.20381v1 | 噪声 |
| [5] | The AudioMOS Challenge 2025 — http://arxiv.org/abs/2509.01336v1 | 噪声 |
| [6] | SWE-bench Goes Live! — http://arxiv.org/abs/2505.23419v2 | ✔ |
| [7] | The Gaia mission — http://arxiv.org/abs/1609.04153v1 | 同名歧义（天文） |
| [8] | SWE-ABS: Adversarial Benchmark Strengthening Exposes Inflated Success Rates on Test-based Benchmark — http://arxiv.org/abs/2603.00520v1 | ✔ |
| [9] | Gaia Data Release 3: Synthetic photometry — http://arxiv.org/abs/2206.06215v2 | 同名歧义（天文） |
| [10] | Gaia Data Release 1 — http://arxiv.org/abs/1609.04172v1 | 同名歧义（天文） |
| [11] | Gaia Data Release 2 — http://arxiv.org/abs/1804.09365v2 | 同名歧义（天文） |
| [12] | Training Software Engineering Agents and Verifiers with SWE-Gym — http://arxiv.org/abs/2412.21139v2 | ✔ |
| [13] | NTU-NPU System for Voice Privacy 2024 Challenge — http://arxiv.org/abs/2410.02371v1 | 噪声 |
| [14] | SVC 2025: the First Multimodal Deception Detection Challenge — http://arxiv.org/abs/2508.04129v1 | ✔（术语辨析） |
| [15] | Apollo: Band-sequence Modeling for High-Quality Audio Restoration — http://arxiv.org/abs/2409.08514v2 | 同名歧义（非 Apollo Research） |
| [16] | AINL-Eval 2025 Shared Task: Detection of AI-Generated Scientific Abstracts in Russian — http://arxiv.org/abs/2508.09622v1 | 噪声 |
| [17] | Apollo: An Exploration of Video Understanding in LMMs — http://arxiv.org/abs/2412.10360v1 | 同名歧义 |
| [18] | Discovery Opportunities with Gravitational Waves — TASI 2024 Lecture Notes — http://arxiv.org/abs/2409.08956v1 | 噪声 |
| [19] | Making Large Language Models Better Reasoners with Alignment — http://arxiv.org/abs/2309.02144v1 | 噪声 |
| [20] | Double Multi-Head Attention Multimodal System for Odyssey 2024 SER Challenge — http://arxiv.org/abs/2406.10598v1 | 噪声 |
| [21] | Enhanced Validation of Advanced Battery Supply Chains (EVALS) Overview — https://doi.org/10.66816/pr6679624 | 噪声 |
| [22] | LLMs4OL 2024 Overview — http://arxiv.org/abs/2409.10146v2 | 噪声 |
| [23] | INSPECT: Learning Robot View Selection from Assistant Use — http://arxiv.org/abs/2609.20615v1 | 同名歧义（非 Inspect 框架） |
| [24] | Inspect India Evals: An Open Benchmarking Framework for Evaluating LLMs in the Indian Linguistic and Cultural Context — http://arxiv.org/abs/2607.25375v1 | ✔ |
| [25] | Inspect Robots: Evaluating the Capabilities and Safety of Embodied AI — http://arxiv.org/abs/2610.06306v1 | ✔ |
| [26] | Methods to Assess the UK Government's Current Role as a Data Provider for AI — http://arxiv.org/abs/2412.09632v2 | ✔ |
| [27] | AI Agents: Evolution, Architecture, and Real-World Applications — http://arxiv.org/abs/2503.12687v1 | 背景（弱相关） |
| [28] | A cybersecurity AI agent selection and decision support framework — http://arxiv.org/abs/2510.01751v1 | ✔ |
| [29] | Evaluation Agent: Efficient and Promptable Evaluation Framework for Visual Generative Models — http://arxiv.org/abs/2412.09645v3 | 背景（弱相关） |
| [30] | ASTELD: A Six-Axis Classification Framework for Autonomous AI Agents — http://arxiv.org/abs/2608.05201v1 | ✔ |
| [31] | R-Judge: Benchmarking Safety Risk Awareness for LLM Agents — http://arxiv.org/abs/2401.10019v3 | ✔ |
| [32] | AgentHarm: A Benchmark for Measuring Harmfulness of LLM Agents — http://arxiv.org/abs/2410.09024v3 | ✔ |
| [33] | （空标题记录） — https://doi.org/10.3030/883728 | E 级，丢弃 |

---

## 附：经典与奠基性工作（本证据池可支撑部分）

> 严格说明：本表**仅收录证据池中确有来源链接的条目**。Apollo Research scheming、Anthropic alignment faking、SHADE-Arena、Greenblatt AI Control、Inspect AI / Inspect Evals、HELM、lm-evaluation-harness、AgentDojo、PyRIT、garak、InjecAgent、ToolEmu **均不在证据池中，故不列表、不给链接**，统一标注 `> 待核实（未检索到）`，以免暗示其存在性证据。

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| R-Judge [31] | 2024 | `> 待核实` | `> 待核实`（无引用数） | arXiv v3 预印本，同行评审 `> 待核实` | 中（作为 Agent 安全基准的早期条目，长期被沿用，但无 star/引用数据支撑更高判断） | ★★★☆☆ 该方向最早的"Agent 安全风险意识"基准化尝试之一，适合作为基线定义引用 | http://arxiv.org/abs/2401.10019v3 | 测"风险意识"而非"策略性欺骗" |
| AgentHarm [32] | 2024 | `> 待核实` | `> 待核实` | arXiv v3 预印本 | 中（同上） | ★★★★☆ 直接测 Agent 危害性，是"安全 benchmark 化"的关键参照，但覆盖不到 scheming | http://arxiv.org/abs/2410.09024v3 | 危害性度量，非可纠正性 |
| SWE-Gym [12] | 2024 | `> 待核实` | `> 待核实` | arXiv v2 预印本 | 中（作为 SWE agent 训练环境被引用，但无数据） | ★★★☆☆ 理解"训练-评测边界"问题的必要背景 | http://arxiv.org/abs/2412.21139v2 | 训练环境 + 验证器 |
| SWE-bench Live [6] | 2025 | `> 待核实` | `> 待核实`（已出 v2） | arXiv cs.SE 预印本，接收状态 `> 待核实` | 中（摘要称 SWE-bench 为领域标准，问题被持续跟进） | ★★★★☆ 动态基准设计的代表作，直接回应饱和与污染 | http://arxiv.org/abs/2505.23419v2 | 无量化成绩披露 |
| FMTI 2025 [3] | 2025 | Percy Liang, Rishi Bommasani, Sayash Kapoor 等 | `> 待核实` | arXiv cs.AI，年度指数第三版 | 中（连续三年发布、首次纳入中国厂商） | ★★★☆☆ 治理侧评测演进的唯一量化证据（58→40） | http://arxiv.org/abs/2512.10169v1 | 非能力基准 |

## 附：开源项目（证据池可支撑部分）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Inspect Robots [25] | 2026 | `> 待核实` | `> 待核实`（无 star 数据） | arXiv cs.RO 预印本；摘要称 "modular, open…"（截断），**是否完全开源待核实** | 中（本次唯一具身能力+安全评测工作，且极新：2026-10） | ★★★★★ 与本主题（VLA/具身 Agent 安全评测）相关性最高，必读 | http://arxiv.org/abs/2610.06306v1 | 是否含真机、支持哪些本体 `> 待核实` |
| Inspect India Evals [24] | 2026 | `> 待核实` | `> 待核实` | arXiv cs.CL；标题含 "Open Benchmarking Framework" | 中（多语言/文化评测的少数公开框架） | ★★★☆☆ 评测框架语境适配的参考样板 | http://arxiv.org/abs/2607.25375v1 | 22 种官方语言 |
| ASTELD [30] | 2026 | `> 待核实` | `> 待核实` | arXiv cs.CR | 中（提出 agent 平台共同分类语言） | ★★★☆☆ 平台横向比较的方法学参考，非评测工具 | http://arxiv.org/abs/2608.05201v1 | 六轴 + OpenClaw 案例 |
| SWE-Gym [12] | 2024 | `> 待核实` | `> 待核实` | arXiv 预印本 | 中 | ★★★☆☆ 训练/验证环境，可作评测对照 | http://arxiv.org/abs/2412.21139v2 | 非评测框架 |

## 附：数据集与基准（证据池可支撑部分）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| SWE-bench Live [6] | 2025 | `> 待核实` | `> 待核实` | arXiv 预印本 | 中 | ★★★★☆ 动态更新型 issue 修复基准 | http://arxiv.org/abs/2505.23419v2 | 更新频率/仓库规模 `> 待核实` |
| SWE-ABS [8] | 2026 | `> 待核实` | `> 待核实` | arXiv 预印本（标题级证据） | 中（直击"成功率虚高"这一核心争议） | ★★★★☆ 抗污染评测的关键方法论，但需读全文核实数字 | http://arxiv.org/abs/2603.00520v1 | 膨胀幅度 `> 待核实` |
| R-Judge [31] | 2024 | `> 待核实` | `> 待核实` | arXiv v3 | 中 | ★★★☆☆ Agent 安全风险意识基准 | http://arxiv.org/abs/2401.10019v3 | 任务数/标注口径 `> 待核实` |
| AgentHarm [32] | 2024 | `> 待核实` | `> 待核实` | arXiv v3 | 中 | ★★★★☆ Agent 危害性基准，安全评测常用基线 | http://arxiv.org/abs/2410.09024v3 | 是否含多轮工具调用 `> 待核实` |
| FMTI 2025 [3] | 2025 | Stanford 等（Percy Liang 等） | `> 待核实` | 年度指数 | 中 | ★★★☆☆ 治理类指数，非任务基准 | http://arxiv.org/abs/2512.10169v1 | 100 分制，均值 40 |

> **本报告的证据边界**：上述三张表**不是**该领域的完整经典清单，而是"本次证据池能够支撑的部分"。任何将本表当作"Agent 评测与安全必读清单"使用的行为都会产生系统性遗漏，尤其是**欺骗与可纠正性方向完全缺失**。补检优先级见 §7.4。

---

*Generated by research-bot · topic=`agent-评测与安全能力基准欺骗与可纠正性` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`deepseek-v4-flash` · sources=33 · duration=197s · 2026-10-17T22:25:26+00:00*
