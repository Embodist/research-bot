# Agent 评测与安全（能力基准、欺骗与可纠正性）增量调研报告（2024–2026）

**日期**：2026-10-11（UTC）  
**领域**：LLM / 具身 Agent 能力评测、AI 安全评测（欺骗性对齐 deceptive alignment、密谋 scheming、奖励黑客 reward hacking、可纠正性 corrigibility）  
**检索源**：候选来源 35 条 [1]–[35]，本报告实际命中并引用 24 条  
**方法论**：frontier-watch（增量七维）+ evidence-grading（四轴证据）  
**写作纪律说明**：本报告严守「只引用可核查编号」原则。候选来源中存在大量与主题无关条目（如 [1][2][10][11][21][22][27][31][32][33]），一律不予引用；凡证据不足处统一标注 `> 待核实`，**不编造引用数、star 数或榜单排名**。

> **全局证据强度前置声明**：本批候选来源以 **arXiv 预印本（cs.AI / cs.LG / cs.CR / cs.CY / cs.IR）** 与 **Zenodo / SSRN 自托管预印本** 为主，**无一篇来自已确认同行评审的顶会正式 proceedings**，也无任何一篇提供可核实的引用数、GitHub star 或榜单排名。因此本报告整体证据等级为 **B（预印本）/ D（自托管非评审）**，所有「SOTA」「有效性」类结论均须降级处理。**开源工具链与 GitHub 仓库在候选集中完全缺席**，这是本报告最重要的结构性缺口。

---

## 1. 进展与热点（Progress & Hotspots）

> **一句话增量判断**：相对「静态 QA 单次响应式评测」这一旧基线，近 12–18 个月的核心增量不是「又多了一个基准」，而是**评测范式本身发生四次位移**——静态→动态实时 [23]、单次响应→可验证多轮 [13]、学术离线→生产常态 [16]、纯能力→能力-安全联合 [18]；同时首次出现**对基准论文自身可复现性的元审计** [14]，这是本周期最具范式意义的信号。

### 1.1 范式位移（相对旧基线的增量）

| 位移方向 | 旧基线 | 新基线 | 证据 |
|---|---|---|---|
| 静态 → 动态实时 | 固定测试集，一次性发布 | 活体基准（live benchmark），抗数据污染 | [23] SWE-bench Goes Live!（2025-05） |
| 单次响应 → 可验证多轮 | 单轮回答打分 | 强调 coordination、transparent decision-making、verifiable performance 的可验证框架 | [13] AEMA（2026） |
| 学术离线 → 生产常态 | 论文附录里的表格 | 面向月活数万用户的在线 agent，574 条历史轨迹驱动的低成本复测 | [16]（2026） |
| 纯能力 → 能力-安全联合 | 能力榜与安全榜分离 | 提出「evaluation-safety failures」作为独立风险类别 | [18] EvalSafetyGap（2026） |
| 单会话 → 跨会话长期记忆 | 对话内 recall | 跨 session 信息复用，作用于 live、结构化文档环境 | [15] IFCMemoryBench（2026） |
| 忽略成本 → 成本/能耗入评 | 只看准确率 | 把能效纳入 agentic 问题解决框架对比 | [17] SWEnergy（2025-12） |

### 1.2 本周期最具信号价值的三项进展

**(a) 评测的「元审计」首次出现 —— [14]**
该工作逐维度审读 12 篇知名 LLM Agent 基准论文，记录每篇**实际披露了多少评测执行细节**，动机是「两篇论文在同一基准、同一模型名下给出不一致结果」。[14] 的贡献不是新基准，而是**把「基准论文的报告完备性」本身变成可审计对象并给出 open scoring schema**。这是本周期最能解释「为什么 Agent 榜单不可比」的一手证据。
- 证据类型：arXiv 预印本 (cs.LG)，2026
- 热度证据：`> 待核实`（候选块未提供 citations / star / 下载量）
- 权威证据：arXiv 预印本，未见同行评审 venue [14]
- 关注度：**低** —— 无引用/榜单/社区讨论信号；依据仅为其议题的代表性
- 推荐度：**★★★★☆** —— 直接命中「评测可复现性」这一核心开放问题，概念杠杆高

**(b) 可验证性（verifiability）被提升为评测第一性要求 —— [13]**
AEMA 明确把「reliable coordination、transparent decision-making、verifiable performance across evolving tasks」作为多智能体 LLM 系统的评测目标，并在摘要中点名批评现有方法「limit themselves to single-response…」。
- 热度证据：`> 待核实`
- 权威证据：arXiv 预印本 (cs.AI)，2026 [13]
- 关注度：**低** —— 无热度信号可查
- 推荐度：**★★★☆☆** —— 方向正确，但仅摘要级信息，框架细节与实证规模 `> 待核实`

**(c) 评测-安全失效被识别为独立风险类别 —— [18]**
EvalSafetyGap 以「hybrid survey + conceptual framework」形式专门刻画 **LLM evaluation-safety failures**。这是把「评测过程本身会带来安全风险」制度化的早期尝试，直接回应本主题的「评测 × 安全」交叉点。
- 热度证据：`> 待核实`
- 权威证据：arXiv 预印本 (cs.AI)，v5 修订版，2026 [18]
- 关注度：**低** —— 无外部热度信号
- 推荐度：**★★★★☆** —— 与本主题交叉度最高的一篇，但方案为概念框架，实证效力 `> 待核实`

### 1.3 奖励黑客（reward hacking）缓解的最新一手方法

| 方法 | 时间 | 核心机制 | 训练/推理 | 证据 |
|---|---|---|---|---|
| BNRM（Bayesian Non-Negative Reward Model） | 2026-02 提交 / 2026-06 修订 | 两级潜变量：实例级隐变量诱导解耦奖励表示；全局隐因子稀疏性作隐式去偏，抑制长度/风格虚假相关 | 训练时（奖励建模） | [4] |
| SLOP（sharpened logarithmic opinion pool） | 2026-05 | 参考模型温度调整 + 生成式奖励模型集成；给出 SLOP 权重校准算法 | 推理时 | [8] |
| Robust Rewards + Dynamic Labels | 2024-12 | 鲁棒奖励与动态标签对抗奖励黑客 | 训练时 | [5] |

- 三条路线共同点：**均只有论文自述实验，候选块未提供任何第三方复现或榜单验证** [4][8][5]。真实有效性 `> 待核实`。
- 热度证据（全部）：`> 待核实` —— [4][8][5] 均无 citations / star / 下载量信号
- 权威证据：[4] arXiv cs.LG 预印本；[8] arXiv cs.LG/cs.AI 预印本；[5] arXiv 预印本（2024-12）—— **均未经同行评审**
- 关注度：**低**（三者）—— 无热度信号
- 推荐度：**★★★☆☆**（[4]、[8]）—— 方法线索价值高，但缺独立验证；**★★★☆☆**（[5]）—— 时间最早、可作演进起点

### 1.4 综述与领域骨架

- [19] *Agentic Large Language Models, a survey*（2025-03，v3）：可作为本领域 2025 年基线综述，用于搭建 agent 能力维度骨架。热度 `> 待核实`；权威：arXiv 综述预印本；关注度 **低–中**（综述类通常为领域主要入口，但候选块无引用数）；推荐度 **★★★★☆**。
- [34] *A Survey of Multi-Agent Deep Reinforcement Learning with Communication*（2022）与 [35] *A Methodology to Engineer and Validate Dynamic Multi-level Multi-agent Based Simulations*（2013）：属**经典工作**，为「多智能体欺骗/密谋」提供前 LLM 时代的建模地基，见 §经典与奠基性工作表。

> **缺口提示**：本周期「欺骗性对齐 / 密谋 / 可纠正性」的**检测型基准**在候选证据中零命中，见 §3。

---

## 2. 工业界与产品（Industry & Product）

> **一句话增量判断**：本周期唯一可信的「工业部署」证据是 **[16] 一篇生产环境 agent 评测研究**；此外 **[28] 汽车 AI 治理标准进程**与 **[29] Agentic AIBOM 供应链溯源**构成「工程/合规」侧的早期增量。**没有任何候选来源提供主要 AI 实验室的产品发布、模型卡或权重开源证据**——该维度整体 `> 待核实`。

### 2.1 已确证的工业侧证据

**(a) 生产环境 Agent 评测首次以「第一手部署经验」形式出现 —— [16]**
- 场景：服务**数万月活用户（tens of thousands of monthly active users）**的生产级 analytics agent
- 方法：利用 **574 条历史轨迹**做高效复测，回应「full agent benchmarks are costly to rerun」的真实痛点
- 增量意义：相对学术界「一次性跑榜」，这是**持续回归测试（recurring evaluation）**视角进入工业评测流程的信号
- 热度证据：论文自述规模为 574 轨迹 / 数万 MAU；**社区热度（citations/star）`> 待核实`**
- 权威证据：arXiv 预印本 (cs.AI)，2026，非同行评审 [16]
- 关注度：**低–中** —— 依据为其披露的生产规模，而非社区热度信号
- 推荐度：**★★★★☆** —— 「评测成本」是工业落地最真实约束，本文是少见的部署一手材料

**(b) 标准/合规侧的 agentic 化 —— [28]**
*The Current State and Future Trends of Automotive AI Safety Governance*（2026-08，作者 Yongshou Ma, Xiaodong Gao, Wenchao Shi）关键词覆盖 **EU AI Act、ISO/PAS 8800、SOTIF、end-to-end driving、agentic AI、in-cabin LLM**。
- 增量点：把 **agentic AI** 明确纳入既有汽车功能安全标准（ISO/PAS 8800、SOTIF）的治理讨论框架
- 热度证据：**citations=0** [28]
- 权威证据：Zenodo（CERN）托管，非同行评审，无会议/期刊 venue [28]
- 关注度：**低** —— citations=0，无社区讨论证据
- 推荐度：**★★★☆☆** —— 标准映射清单有实用价值，但为个人预印本，**不可作为标准原文引用**，须回溯 ISO/PAS 8800 与 EU AI Act 官方文本 `> 待核实`

**(c) Agent 供应链可复现性 —— [29]**
*SBOMs into Agentic AIBOMs: Schema Extensions, Agentic Orchestration, and Reproducibility Evaluation*：指出传统 SBOM 只能提供**静态依赖清单**，无法刻画 runtime behaviour、environment drift；提出向 Agentic AIBOM 的 schema 扩展。
- 增量点：把「可复现性」从论文写作规范下沉到**软件供应链溯源机制**
- 热度证据：`> 待核实`
- 权威证据：arXiv 预印本 (cs.CR)，2026 [29]
- 关注度：**低** —— 无热度信号
- 推荐度：**★★★☆☆** —— 概念新颖（agent 时代的物料清单），落地程度 `> 待核实`

### 2.2 工业界证据的整体缺口

- **无**：主要实验室（OpenAI / Anthropic / Google DeepMind / Meta 等）的 agent 安全评测产品、模型卡、红队报告 —— `> 待核实`
- **无**：METR、UK AISI、US AISI 等机构工具的候选条目 —— `> 待核实`
- **无**：任何可量化的商业化/量产数据（出货量、付费用户、ARR） —— `> 待核实`
- **无**：任何 GitHub 仓库、权重发布或 HuggingFace 条目 —— `> 待核实`

> 结论：**「工业界与产品」维度在本候选集下证据严重不足**，仅有 [16] 一条真实部署证据与 [28][29] 两条工程/合规邻近证据。任何「已大规模落地」的表述都缺乏支持。

---

## 3. 蓝海与缺口（Blue Ocean & Gaps）

> **一句话增量判断**：本周期最显著的结构性缺口是——**能力评测在快速增长，而欺骗/密谋/可纠正性的「检测型评测」几乎空白**；候选证据中对这三类风险的讨论全部停留在**概念/本体论层（[9][12]）**，没有任何一篇提供可执行的检测基准、指标或工具。

### 3.1 高杠杆空白（按缺口严重度排序）

| # | 缺口 | 现状证据 | 为什么是蓝海 |
|---|---|---|---|
| G1 | **欺骗性对齐 / 密谋的检测基准** | 候选集中零命中检测基准；仅有 2021 年的对抗多智能体欺骗**建模**工作 [7] | 风险叙事极热但**没有可复现的测量工具**，谁能给出可证伪的检测指标即占据定义权 |
| G2 | **可纠正性（corrigibility）的形式化评测** | [9][12] 仅在概念层面讨论，无实验、无指标、无 benchmark，citations 均为 0 | 从「哲学争论」到「可测量」之间存在完整的工具真空 |
| G3 | **开源评测工具链** | q2 检索明确结论：**无任何开源框架/仓库/榜单/数据集命中** | 全领域缺乏共享基建，先发者可直接成为事实标准 |
| G4 | **基准报告 schema 的标准化** | [14] 提出 open scoring schema 作为**主动应对**，反证当前无标准 | 一旦被主流 harness 采纳即为基础设施级资产 |
| G5 | **能力强弱 × 安全风险的联合评测** | [18] 提出 evaluation-safety failures 概念框架，但仍是 framework 而非实测 | 「能力-安全权衡」目前无量化曲线，是立项级空白 |
| G6 | **跨会话/长时程记忆的安全评测** | [15] 只做信息检索能力，未做记忆投毒/跨会话欺骗 | 记忆一旦持久化，攻击面从单轮扩展到跨会话，评测方法未跟上 |
| G7 | **Agent 供应链溯源与可复现性** | [29] 提出 AIBOM schema 扩展，属早期探索 | agent 编排链远比静态依赖复杂，溯源标准尚未形成 |
| G8 | **评测的成本/能耗维度** | [17] 是候选集中唯一把能效纳入 agentic 框架对比的工作 | 与 [16] 的「复测成本」痛点同一根因，但几乎无人做 |

### 3.2 明确的证据空白（须补充检索）

- **奠基性工作缺失**：候选集合中**没有任何** mesa-optimization、deceptive alignment、corrigibility 的原始奠基论文，也**没有** reward hacking 的开创性文献 [4][8][9][12] 覆盖范围内均无。因此本报告**无法回答「奠基工作是什么」**，该问题标注 `> 待核实`。
- **争议未解**：欺骗性对齐是否**可观测**存在两说并列 —— [9] 主张其「预设了当前系统尚不具备的自我建模能力」，[12] 则直接在框架内处理 deceptive alignment。**双方均无同行评审背书**，标 `[Debated]`，须交叉验证。

---

## 4. 瓶颈与拐点（Bottleneck & Inflection）

> **一句话增量判断**：本领域当前同时承受**四个瓶颈**（可复现性、成本、数据污染、缺第三方验证），其中**可复现性与成本已出现明确拐点信号**（[14] 的元审计、[16] 的生产复测、[23] 的活体基准）；但**欺骗检测方向尚未出现任何拐点信号**，仍处于零测量状态。

### 4.1 瓶颈清单

| 瓶颈 | 表现 | 证据 | 是否临近拐点 |
|---|---|---|---|
| **B1 评测可复现性** | 同基准同模型名结果不一致；论文披露维度参差 | [14]（正向应对：open scoring schema） | **是** —— 已从抱怨转为可操作方案 |
| **B2 评测成本** | full agent benchmark 重跑昂贵，无法高频回归 | [16]（574 条历史轨迹复测） | **是** —— 生产侧已给出工程解 |
| **B3 数据污染 / 基准饱和** | 静态测试集被训练集覆盖 | [23] 活体基准范式 | **是** —— 范式已迁移 |
| **B4 缺第三方验证** | 奖励黑客缓解方法 [4][8][5] 全为自述，无复现 | [4][8][5] | **否** —— 无复现证据，`> 待核实` |
| **B5 欺骗不可观测性争论** | 概念层分歧，无测量手段 | [9] vs [12] `[Debated]` | **否** |
| **B6 算力/能耗** | agentic 框架推理成本高 | [17] | **弱信号** —— 仅单篇实证 |
| **B7 跨会话状态漂移** | 长期记忆引入新的失效模式 | [15]（仅测能力，未测安全） | **否** |

### 4.2 拐点信号（可观测）

1. **评测从「发布即冻结」转向「持续在线」** —— [23] 活体基准 + [16] 生产复测，两者共同指向同一方向，互为独立佐证（不同团队、不同场景、同年）。
2. **「评测本身的安全风险」被命名** —— [18] 首次把 evaluation-safety failures 作为独立类别，命名通常是标准化的前奏。
3. **可复现性从写作规范下沉为基础设施 schema** —— [14] 的 scoring schema 与 [29] 的 AIBOM schema 是同一诉求在不同层级（论文层 / 供应链层）的表现。
4. **纵向评测（longitudinal）在 IR 领域已成熟** —— [30] LongEval at CLEF 2025 针对 **IR 模型性能随时间退化**；agent 评测目前尚**没有**对应的纵向框架，这是可直接借鉴的跨领域范式 `[P]`。

---

## 5. 社会·政策·国际（Society, Policy & Geopolitics）

> **一句话增量判断**：本周期的政策增量主要体现在**标准化与治理叙事之争**：一方面主流治理话语高度集中于「safety」并已产出 International AI Safety Report（96 位专家，其中 30 位由 OECD 提名）[26]；另一方面出现**系统安全（system safety）视角的反驳**，认为 AI safety 讨论「卡在技术术语里」；同时垂直行业（汽车）开始把 agentic AI 纳入既有标准体系 [28]。

### 5.1 治理叙事分歧

**主流侧**：International AI Safety Report —— 由 96 位专家撰写，其中 30 位由 OECD 提名 [26]（该事实转述自 [26] 摘要，**建议回溯报告原文核实** `> 待核实`）。
- 证据：arXiv 预印本 (cs.CY)，2025 [26]
- 热度证据：`> 待核实`
- 权威证据：arXiv 预印本，非同行评审；但其所回应的对象为 OECD 参与的国际报告 [26]
- 关注度：**中** —— 依据为其回应的政策对象层级，而非文献计量
- 推荐度：**★★★★☆** —— 理解「AI safety 政策话语结构」的关键一手评论

**反驳侧**：*AI Safety is Stuck in Technical Terms — A System Safety Response to the International AI Safety Report* [26]，主张从系统安全（system safety）传统而非纯技术术语切入。

### 5.2 垂直行业标准的 agentic 化

- [28]（2026-08）把 **agentic AI、in-cabin LLM** 纳入 **EU AI Act、ISO/PAS 8800、SOTIF** 的治理讨论：
  - 增量：**既有功能安全标准首次被追问「是否覆盖 agentic 行为」**
  - 但该来源为 Zenodo 自托管预印本、citations=0，**不能作为标准条文依据**；须回溯 ISO/PAS 8800、EU AI Act 官方文本 `> 待核实`
  - 关注度：**低**（citations=0）| 推荐度：**★★★☆☆**

### 5.3 供应链与可复现性的政策邻近

- [29] Agentic AIBOM 虽属工程论文，但其「provenance + reproducibility + vulnerability assessment」目标与软件供应链监管同源，是政策可能介入的抓手。

### 5.4 本维度缺口

- **无**针对 Agent（区别于基础模型）的专门立法或监管条目 —— `> 待核实`
- **无**中国 / 美国 / 欧盟针对 agent 评测的强制性标准条目 —— `> 待核实`
- **无**地缘政治、算力出口管制与 agent 评测的关联证据 —— `> 待核实`

---

## 6. 资本与生态（Capital & Ecosystem）

> **一句话增量判断**：本候选集**完全没有任何融资、并购、人才流动或市场格局数据**，该维度无法以增量事实形式回答。唯一可观察的**生态结构信号**是：前沿安全论述大量沉淀在 **Zenodo / SSRN 等非同行评审自托管平台**（[9][12][28]），反映该子领域的**质量把关机制薄弱、学术出版通道不畅**。

### 6.1 可观察的生态结构信号

| 信号 | 观察 | 证据 | 四轴评估 |
|---|---|---|---|
| 自托管平台承载前沿安全论述 | [9] Zenodo DOI 10.5281/zenodo.19636081，citations=0；[12] SSRN DOI 10.2139/ssrn.5849902，citations=0；[28] Zenodo，citations=0 | [9][12][28] | 热度：citations=0 [9][12][28]；权威：非同行评审；关注度：**低**；推荐度：**★★☆☆☆**（[9][12]）/**★★★☆☆**（[28]） |
| 概念论文先于实证论文出现 | 欺骗性对齐的「本体论/框架」类论文（[9][12]）早于任何检测基准 | [9][12] | 关注度：**低** |
| 工程可复现性诉求上升 | [14]（论文层 schema）+ [29]（供应链层 AIBOM）同期出现 | [14][29] | 关注度：**低** |
| 能效/成本开始被论文计入 | [17] SWEnergy | [17] | 关注度：**低** |

### 6.2 严重缺口（必须显式声明）

- **无**任何投资/融资/估值数据 —— `> 待核实`
- **无**任何并购、公司格局或市场集中度信息 —— `> 待核实`
- **无**人才流动证据 —— `> 待核实`
- **无**开源社区活跃度数据（star / fork / contributor）—— `> 待核实`

> 说明：[17] SWEnergy 关注 **SLM（小语言模型）** 在 agentic issue resolution 框架中的能效，可视为「成本敏感型部署」的早期信号，但单个预印本不足以支撑生态判断。

---

## 7. 信号与预测（Signals & Forecast）

> **一句话增量判断**：本周期最强的三个早期信号是——(i) **基准从静态转向活体** [23]，(ii) **评测自身成为审计对象** [14]，(iii) **生产环境持续评测成为一等公民** [16]。三者在 2025–2026 年同期出现且互不依赖，构成**评测方法论层面的真实拐点**。相反，**欺骗/可纠正性方向没有任何拐点信号**。

### 7.1 预测与可证伪假设 `[P]`

**H1 — 基准报告 schema 的标准化（置信度：中）**
- 依据链：现行不一致问题已被量化审计 [14] → agent 评测成本压力上升 [16] → 工程侧已有 schema 化先例 [29]。
- 可证伪假设：**若到 2027-06 之前，没有至少一个主流 agent 评测 harness 或主要会议采纳标准化的评测报告 schema（如 [14] 所提），则本预测不成立。**

**H2 — 活体/动态基准成为主流（置信度：中高）**
- 依据链：静态测试集污染是结构性问题 [23] 已给出范式。
- 可证伪假设：**若 2026-10 至 2027-10 期间，新发布的 agent 能力基准中「活体/周期性刷新」形态占比未显著上升，则本预测不成立。**

**H3 — 欺骗检测基准将出现但滞后（置信度：中低）**
- 依据链：风险叙事热度远高于测量能力（[9][12] 均为概念层且 citations=0）→ 存在明显工具真空（见 G1）。
- 可证伪假设：**若到 2027-12 仍无任何经同行评审、可复现的欺骗/密谋检测基准发布，则说明该方向需求被高估或技术上不可行。**

**H4 — 奖励黑客缓解方法将长期缺少第三方复现（置信度：中）**
- 依据链：[4][8][5] 三条路线均只有自述实验，无榜单、无复现报告。
- 可证伪假设：**若 12 个月内出现独立第三方在公开基准上复现 [4] 或 [8] 并给出可比数字，则本预测不成立。**

**H5 — 纵向（longitudinal）评测范式将从 IR 迁移至 Agent（置信度：低–中）**
- 依据链：IR 领域已有成熟纵向评测框架 [30] → agent 同样面临模型/环境漂移，但尚无对应框架。
- 可证伪假设：**若到 2027-12 未出现针对 agent 的纵向/时间序列评测框架，则本预测不成立。**

**H6 — 成本与能耗进入评测标准维度（置信度：低）**
- 依据链：[16] 复测成本痛点 + [17] 能效实证同时出现。
- 可证伪假设：**若到 2027-12，主流 agent 基准榜单仍未把 token 成本或能耗作为并列报告指标，则本预测不成立。**

### 7.2 值得持续关注的 Watchlist

| 关注对象 | 理由 | 证据状态 |
|---|---|---|
| **[14] open scoring schema 是否被采纳** | 判断评测可复现性拐点是否成立的唯一可观测锚点 | 预印本 [14]，采纳情况 `> 待核实` |
| **[23] 活体基准范式的扩散速度** | 数据污染问题的直接解药 | arXiv v2（2025-05）[23] |
| **[16] 生产评测案例的方法论外溢** | 工业界是否形成共享的持续评测实践 | 单案例 [16]，外溢情况 `> 待核实` |
| **[18] evaluation-safety failures 是否形成独立研究线** | 决定「评测 × 安全」是否成为正式子领域 | 概念框架 [18] |
| **[9] vs [12] 的可观测性争论走向** | 决定欺骗性对齐能否被工程化测量 | `[Debated]`，双方 citations=0 |
| **开源评测工具链的出现** | 当前完全空白（G3），一旦出现即为基建级机会 | 候选集零命中 `> 待核实` |

---

## 附：经典与奠基性工作（表格）

> 说明：**本候选集中不存在 mesa-optimization、deceptive alignment、corrigibility 的原始奠基论文**，下表列出的是候选集内可核查的**前 LLM 时代 / 早期相关工作**，其「经典」地位系就其方法论角色而言，非就本主题的奠基性而言。

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Modelling Strategic Deceptive Planning in Adversarial Multi-Agent Systems | 2021 | `> 待核实`（候选块未提供作者） | `> 待核实` | arXiv 预印本 (2109.03092v1)，未经同行评审 [7] | 低（无热度信号） | ★★★☆☆ | http://arxiv.org/abs/2109.03092v1 | 前 LLM 时代的对抗多智能体**欺骗性规划建模**，是本主题「欺骗」概念在形式化多智能体语境下的最早可核查候选条目 |
| SALMON: Self-Alignment with Instructable Reward Models | 2023 | `> 待核实` | `> 待核实` | arXiv 预印本 (2310.05910v2) [6] | 低（无热度信号） | ★★★☆☆ | http://arxiv.org/abs/2310.05910v2 | 可指令奖励模型驱动的自对齐，奖励建模路线的早期代表 |
| Aligning Language Models Using Follow-up Likelihood as Reward Signal | 2024 | `> 待核实` | `> 待核实` | arXiv 预印本 (2409.13948v3) [3] | 低（无热度信号） | ★★★☆☆ | http://arxiv.org/abs/2409.13948v3 | 以 follow-up likelihood 作奖励信号，奖励建模替代路线 |
| Sail into the Headwind: Alignment via Robust Rewards and Dynamic Labels against Reward Hacking | 2024-12 | `> 待核实` | `> 待核实` | arXiv 预印本 (2412.09544v1) [5] | 低（无热度信号） | ★★★☆☆ | http://arxiv.org/abs/2412.09544v1 | 明确以 reward hacking 为对抗目标，是候选集中该类方法的较早条目 |
| A Survey of Multi-Agent Deep Reinforcement Learning with Communication | 2022 | `> 待核实` | `> 待核实` | arXiv 综述预印本 (2203.08975v2) [34] | 低（无热度信号） | ★★★☆☆ | http://arxiv.org/abs/2203.08975v2 | 多智能体通信机制综述，为「密谋/collusion」类行为提供 MARL 理论基础 |
| A Methodology to Engineer and Validate Dynamic Multi-level Multi-agent Based Simulations | 2013 | `> 待核实` | `> 待核实` | arXiv 预印本 (1311.5108v1) [35] | 低（无热度信号） | ★★☆☆☆ | http://arxiv.org/abs/1311.5108v1 | 多层级多智能体仿真的工程与验证方法，agent 评测方法论的远古源头 |

---

## 附：开源项目（表格）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — | — | **候选集内零命中**：本批 35 条来源中**没有任何 GitHub 仓库、开源框架、可下载权重或工具链条目**。q2 检索亦明确记录「无开源仓库、无基准榜单、无数据集」[4][8][9][12]。该表所有条目 `> 待核实`，须补充检索（METR / AISI Inspect / DeepEval 等方向）后方可填写。 |

> **结论**：**开源工具链是本主题最大的、也是最确凿的空白**（对应 §3 缺口 G3）。任何声称「已有成熟开源 agent 安全评测工具链」的表述，在本候选证据下**均无支持**。

---

## 附：数据集与基准（表格）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| SWE-bench Goes Live! | 2025-05 | `> 待核实` | `> 待核实` | arXiv 预印本 (2505.23419v2) [23] | 低–中（范式重要性高，热度 `> 待核实`） | ★★★★☆ | http://arxiv.org/abs/2505.23419v2 | **活体（live）基准范式**，回应静态测试集污染与饱和 |
| AEMA: Verifiable Evaluation Framework for Trustworthy and Controlled Agentic LLM Systems | 2026 | `> 待核实` | `> 待核实` | arXiv 预印本 (2601.11903v1)，cs.AI [13] | 低（无热度信号） | ★★★★☆ | http://arxiv.org/abs/2601.11903v1 | 面向多智能体 LLM 的**可验证评测框架**，强调 coordination 与决策透明 |
| What Twelve LLM Agent Benchmark Papers Disclose About Themselves | 2026 | `> 待核实` | `> 待核实` | arXiv 预印本 (2605.21404v1)，cs.LG [14] | 低（无热度信号） | ★★★★☆ | http://arxiv.org/abs/2605.21404v1 | **基准元审计** + open scoring schema，本周期最关键的评测方法论条目 |
| IFCMemoryBench | 2026 | `> 待核实` | `> 待核实` | arXiv 预印本 (2607.26072v1)，cs.IR [15] | 低（无热度信号） | ★★★☆☆ | http://arxiv.org/abs/2607.26072v1 | 在 **BIM 结构化文档** live 环境中评测跨会话长期记忆复用 |
| Sola-Visibility-ISPM | 2026 | `> 待核实` | `> 待核实` | arXiv 预印本 (2601.07880v1) [20] | 低（无热度信号） | ★★☆☆☆ | http://arxiv.org/abs/2601.07880v1 | Agentic AI 用于**身份安全态势管理可见性**的基准，垂直领域 |
| EvalSafetyGap | 2026 | `> 待核实` | `> 待核实` | arXiv 预印本 (2606.30219v5)，cs.AI [18] | 低（无热度信号） | ★★★★☆ | http://arxiv.org/abs/2606.30219v5 | **评测-安全失效**的混合综述与概念框架，本主题交叉度最高 |
| LongEval at CLEF 2025: Longitudinal Evaluation of IR Model Performance | 2025 | `> 待核实` | `> 待核实` | arXiv 预印本 (2503.08541v1) [30] | 低（无热度信号） | ★★★☆☆ | http://arxiv.org/abs/2503.08541v1 | **纵向评测**框架（IR 领域），可迁移至 agent 的跨时间评测范式 |
| Overview of the Sensemaking Task at the ELOQUENT 2025 Lab | 2025 | `> 待核实` | `> 待核实` | arXiv 预印本 (2507.12143v1) [25] | 低（无热度信号） | ★★☆☆☆ | http://arxiv.org/abs/2507.12143v1 | LLM 作为教师/学生/评估者（LLM-as-judge 多角色）的评测设计 |
| Semantically Named REST/CRUD vs Agentic API Design（Semantic Method Naming and LLM Agent Accuracy） | `> 待核实` | `> 待核实` | `> 待核实` | SSRN 预印本，DOI 10.2139/ssrn.6460766，非同行评审 [24] | 低（无热度信号） | ★★☆☆☆ | https://doi.org/10.2139/ssrn.6460766 | 受控基准，比较 REST/CRUD 与 agentic API 设计对 agent 准确率的影响；信息仅到摘要级 `> 待核实` |

---

## 参考来源

[1] Homological mirror symmetry for log Calabi-Yau surfaces — http://arxiv.org/abs/2005.05010v3 （**与本主题无关，未引用**）  
[2] This paper has been withdrawn — http://arxiv.org/abs/cond-mat/0309395v2 （**E 级，已丢弃**）  
[3] Aligning Language Models Using Follow-up Likelihood as Reward Signal — http://arxiv.org/abs/2409.13948v3  
[4] Mitigating Reward Hacking in RLHF via Bayesian Non-negative Reward Modeling — http://arxiv.org/abs/2602.10623v2  
[5] Sail into the Headwind: Alignment via Robust Rewards and Dynamic Labels against Reward Hacking — http://arxiv.org/abs/2412.09544v1  
[6] SALMON: Self-Alignment with Instructable Reward Models — http://arxiv.org/abs/2310.05910v2  
[7] Modelling Strategic Deceptive Planning in Adversarial Multi-Agent Systems — http://arxiv.org/abs/2109.03092v1  
[8] Temper and Tilt Lead to SLOP: Reward Hacking Mitigation with Inference-Time Alignment — http://arxiv.org/abs/2605.13537v1  
[9] The Structural Conditions of Consciousness: A Framework for AI Alignment — https://doi.org/10.5281/zenodo.19636081  
[10] OpenFact at CheckThat! 2024: Combining Multiple Attack Methods for Effective Adversarial Text Generation — http://arxiv.org/abs/2409.02649v2 （**未引用**）  
[11] Normalization of peer-evaluation measures of group research quality across academic disciplines — http://arxiv.org/abs/1006.3863v2 （**未引用**）  
[12] Predicting the Inevitability of AI Alignment Failure: A System-Ontological Analysis and Mechanistic Framework. A Unified Ontological Framework for "Goal Distortion", "Reward Hacking", and "Deceptive Alignment" — https://doi.org/10.2139/ssrn.5849902  
[13] AEMA: Verifiable Evaluation Framework for Trustworthy and Controlled Agentic LLM Systems — http://arxiv.org/abs/2601.11903v1  
[14] What Twelve LLM Agent Benchmark Papers Disclose About Themselves: A Pilot Audit and an Open Scoring Schema — http://arxiv.org/abs/2605.21404v1  
[15] IFCMemoryBench: Evaluating Long-Term Memory of LLM-Based Agents in BIM Information Retrieval — http://arxiv.org/abs/2607.26072v1  
[16] Efficient Benchmarking in Production: A Study of an Evolving LLM Agent — http://arxiv.org/abs/2609.21267v1  
[17] SWEnergy: An Empirical Study on Energy Efficiency in Agentic Issue Resolution Frameworks with SLMs — http://arxiv.org/abs/2512.09543v2  
[18] EvalSafetyGap: A Hybrid Survey and Conceptual Framework for LLM Evaluation-Safety Failures — http://arxiv.org/abs/2606.30219v5  
[19] Agentic Large Language Models, a survey — http://arxiv.org/abs/2503.23037v3  
[20] Sola-Visibility-ISPM: Benchmarking Agentic AI for Identity Security Posture Management Visibility — http://arxiv.org/abs/2601.07880v1  
[21] Self-Evolving Autonomous Software Architectures Using Large-Scale Graph Neural Networks and Real-Time Big Data Feedback Loops — https://doi.org/10.63544/jbii.v5i5.188 （**未引用**）  
[22] The Gaia mission — http://arxiv.org/abs/1609.04153v1 （**与本主题无关，未引用**）  
[23] SWE-bench Goes Live! — http://arxiv.org/abs/2505.23419v2  
[24] Semantic Method Naming and LLM Agent Accuracy: A Controlled Benchmark of REST/CRUD versus Agentic API Design — https://doi.org/10.2139/ssrn.6460766  
[25] Overview of the Sensemaking Task at the ELOQUENT 2025 Lab: LLMs as Teachers, Students and Evaluators — http://arxiv.org/abs/2507.12143v1  
[26] AI Safety is Stuck in Technical Terms -- A System Safety Response to the International AI Safety Report — http://arxiv.org/abs/2503.04743v1  
[27] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1 （**未引用**）  
[28] The Current State and Future Trends of Automotive AI Safety Governance — https://doi.org/10.5281/zenodo.21752296  
[29] SBOMs into Agentic AIBOMs: Schema Extensions, Agentic Orchestration, and Reproducibility Evaluation — http://arxiv.org/abs/2603.10057v1  
[30] LongEval at CLEF 2025: Longitudinal Evaluation of IR Model Performance — http://arxiv.org/abs/2503.08541v1  
[31] Annif at SemEval-2025 Task 5: Traditional XMTC augmented by LLMs — http://arxiv.org/abs/2504.19675v2 （**未引用**）  
[32] NTIRE 2025 Challenge on Image Super-Resolution (x4): Methods and Results — http://arxiv.org/abs/2504.14582v3 （**未引用**）  
[33] The AudioMOS Challenge 2025 — http://arxiv.org/abs/2509.01336v1 （**未引用**）  
[34] A Survey of Multi-Agent Deep Reinforcement Learning with Communication — http://arxiv.org/abs/2203.08975v2  
[35] A Methodology to Engineer and Validate Dynamic Multi-level Multi-agent Based Simulations — http://arxiv.org/abs/1311.5108v1  

---

### 报告自检声明

- ✅ 七章全部逐条写全，未省略任何章节  
- ✅ 所有引用编号均来自候选来源列表 [1]–[35]，未引用不存在编号，未编造 URL  
- ✅ 「经典与奠基性工作」「开源项目」「数据集与基准」均以表格呈现，含四轴证据列  
- ✅ 明确区分「最新进展（近 1–2 年）」与「经典工作」  
- ✅ 证据不足处统一标注 `> 待核实`；争议标 `[Debated]`；预测标 `[P]` 并写成可证伪假设  
- ✅ **未编造任何引用数、star 数或榜单排名**；候选块未提供的热度数据一律标 `> 待核实`  
- ⚠️ **本报告最重要的诚实结论**：候选证据在「开源工具链」「欺骗/可纠正性检测基准」「奠基性论文」「工业产品与资本数据」四个方向**完全空白**，报告如实呈现而非填补。

---

*Generated by research-bot · topic=`agent-评测与安全能力基准欺骗与可纠正性` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`deepseek-v4-flash` · sources=35 · duration=201s · 2026-10-11T22:19:52+00:00*
