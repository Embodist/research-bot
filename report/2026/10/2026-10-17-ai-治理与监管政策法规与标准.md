# AI 治理与监管（政策、法规与标准）调研报告：2024–2026 年增量快照

**日期**：2026-10-17（UTC）｜**领域**：AI Governance & Regulation（AI 治理与监管：政策、法规与标准）｜**检索源**：候选证据库共 33 条编号来源（[1]–[33]），其中 20 条进入实质分析，13 条因主题相关性弱或摘要截断仅作边界说明｜**观察窗口**：2024-01 至 2026-10

> **方法学免责声明（必读）**：本报告所依据的 33 条来源**全部为 arXiv 预印本或预印本平台（OSF/SSRN）文本，无一条为监管机构官方一手文件**（EUR-Lex 法条正文、欧盟委员会指南、NIST AI RMF、OECD AI Principles、中国网信办规章等均未进入本次证据集）。因此本报告**不能**用于陈述"某法规第几条规定了什么、何时生效"这类法条事实，只能用于刻画**研究界与实务界围绕监管正在讨论什么、缺什么**。所有法条级结论一律标注 `> 待核实`。热度证据（引用数、GitHub star、下载量、榜单排名）在候选块中**全部缺失**，故一律写 `> 待核实`，不做任何数字估计。

---

## 1. 进展与热点（Progress & Hotspots）

**一句话增量判断**：相对"原则宣言"阶段（2019–2023），2024–2026 年的真实增量不是新法条，而是**研究界开始把监管当作工程约束来拆解**——合规证据、合规检查器、行为准则解释、行业架构落地四类工作同时出现，但**证据强度整体停留在 B 级（预印本）**。

### 1.1 从"是否监管"转向"如何合规"：EU AI Act 进入解释与实施争论

- **适用范围仍未收敛**：截至 2025 年底，"内部部署（internal deployment）"是否落入 EU AI Act 适用范围仍是开放的法律解释问题。相关备忘录以压力测试方式并列支持与反对论据，并基于 Art. 2(1)、2(6)、2(8) 给出多条可供欧委会、AI provider/deployer 与法院采用的解释路径 [17]。这是本证据集中**唯一直接做法条级条文分析**的材料。
  - 热度：`> 待核实`（候选块未提供引用数/下载量）｜权威：arXiv cs.CY 预印本 v4，政策备忘录体裁，非同行评审 [17]｜关注度：**低**（无引用、无媒体/榜单信号）｜推荐度：**★★★★☆**（法条定位最具体，是理解实施期边界争议的入口）
- **行为准则（Code of Practice）成为独立研究对象**：围绕 EU GPAI Code of Practice 已形成三条并行讨论线——业界实践如何映射到其安全与保障措施 [19]；其带来的"非对称法律不确定性"（同一文本对不同规模/类型主体产生不同确定性）[20][21]；以及在执法间隔期（enforcement interval）内"延迟执法但报告义务先行"的制度张力 [22]。
  - 热度：`> 待核实`｜权威：三份文本分别走 arXiv 预印本 [19]、OSF 预印本 [20]、SSRN 预印本 [21] 与期刊 DOI [22]；同一主题跨四渠道发布本身说明该议题正被多学科同时争夺 [19][20][21][22]｜关注度：**中**（同一议题出现 4 个独立出版渠道，是本次证据集中最密集的议题簇）｜推荐度：**★★★★☆**（研究 GPAI 行为准则的最佳切入点，但须回原文核实其对条文的具体解读）
- **合规已被当作硬性工程输入**：以奥地利/德国受监管保险公司为对象的通用多智能体 AI 架构，明确把 Solvency II 与 AI Act 作为并列设计约束 [16]，说明合规义务开始进入企业架构层，而非停留在法务文本层。
  - 热度：`> 待核实`｜权威：arXiv q-fin.GN 预印本 [16]｜关注度：**低**（细分行业单案例）｜推荐度：**★★★☆☆**（"立法→行业实施"的间接证据，不能外推为全法域实施进度）
- **合规证据基础设施成为独立命题**：有研究直接指出，AI Assurance（产出可机器读取的合规证据）"政策脚手架已成熟但缺少基础设施"，构建高风险 AI 系统的组织因此存在落地断层 [27]。
  - 热度：`> 待核实`｜权威：arXiv cs.CY 预印本 [27]｜关注度：**低**｜推荐度：**★★★★☆**（把"合规成本"具体化为"证据可读性"问题，是本报告最具解释力的单一论断之一）

### 1.2 框架层面的收敛尝试

- **框架碎片化已被明确诊断**：AI 风险缓解框架"碎片化、术语不一致、覆盖有缺口"，因此需要共同参照系来对齐组织与政府的协作，并据此提出初步的 AI Risk Mitigation Taxonomy [3]。
  - 热度：`> 待核实`｜权威：arXiv cs.CY 预印本，2025-12-12 提交，自称 preliminary [3]｜关注度：**低**｜推荐度：**★★★★☆**（最贴"共同参照系"提问，可作框架族谱对照表）
- **"原则→落地"被形式化为层级栈**：五层框架把 broad regulatory mandates 逐层收窄为 specific standards → assessment methodologies → certification processes，并以 AI fairness、AI incident reporting 两个案例演示 [2]。
  - 热度：`> 待核实`｜权威：arXiv cs.CY 预印本，非同行评审 [2]｜关注度：**低**｜推荐度：**★★★☆☆**（骨架可用，但"验证"仅为两个自选案例）

### 1.3 表 1：经典与奠基性工作（区分于上文最新进展）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Principles alone cannot guarantee ethical AI [11] | 2019（arXiv v2） | 作者/机构信息未在候选块给出 `> 待核实` | `> 待核实` | arXiv 预印本；该标题是"原则主义不足"这一批判路线的标志性表述 [11] | **中**（作为被后续工作反复回指的问题起点，标题本身已成领域通用表述；但本次无引用数佐证） | ★★★★☆ | http://arxiv.org/abs/1906.06668v2 | 全部"原则—落地缺口"论证的经典锚点 |
| Beyond principlism: Practical strategies for ethical AI use in research practices [10] | 2024 | 未在候选块给出 `> 待核实` | `> 待核实` | arXiv 预印本 v6（多次修订）[10] | **低** | ★★★☆☆ | http://arxiv.org/abs/2401.15284v6 | 从"批判原则主义"转向"可操作策略"，属过渡性文献 |
| Operationalising AI governance through ethics-based auditing: An industry case study [12] | 2024 | 未在候选块给出 `> 待核实` | `> 待核实` | arXiv 预印本；产业案例研究 [12] | **低** | ★★★★☆ | http://arxiv.org/abs/2407.06232v1 | 把"伦理审计"从概念推到企业案例，是"落地"链条上稀缺的实证环节 |
| A five-layer framework for AI governance [2] | 2025 | Agarwal & Nene | `> 待核实` | arXiv cs.CY 预印本，非同行评审 [2] | **低** | ★★★☆☆ | http://arxiv.org/abs/2509.11332v1 | 监管→标准→评估→认证的层级栈骨架 |
| Mapping AI Risk Mitigations（preliminary taxonomy）[3] | 2025 | 未在候选块给出 `> 待核实` | `> 待核实` | arXiv cs.CY 预印本，自称 preliminary [3] | **低** | ★★★★☆ | http://arxiv.org/abs/2512.11931v1 | 风险缓解框架的收敛尝试 |
| The Nuclear Analogy in AI Governance Research [7] | 2025（arXiv 2510） | 未在候选块给出 `> 待核实` | `> 待核实` | arXiv 预印本 [7] | **低** | ★★★☆☆ | http://arxiv.org/abs/2510.21203v1 | 核类比是 IAEA 式国际机构方案的主要论据来源，需辨析其可迁移性 |
| The Global Majority in International AI Governance [6] | 2026（arXiv 2601） | 未在候选块给出 `> 待核实` | `> 待核实` | arXiv 预印本 [6] | **低** | ★★★★☆ | http://arxiv.org/abs/2601.17191v1 | 国际治理的代表性/分配正义维度，是主流英语文献的结构性盲区 |

> 说明：表 1 中"热度"一列全部无法填写，因为候选块未提供任何引用数或下载量。按证据纪律，此处**不估算、不引用记忆中的数字**。

---

## 2. 工业界与产品（Industry & Product）

**一句话增量判断**：本周期出现的"产品"不是商业 SaaS，而是**合规方法学与工具原型**——工具化仍处学术原型阶段，未见被监管机构或大型企业正式采用的记录。

### 2.1 落地形态：工具、检查器、方法学

- **合规检查器已形成可被实证评估的品类**：EU AI Act 对开发、部署、集成 AI 的组织提出大量合规要求，其中许多直接关联安全与隐私，并延伸到数据治理、透明度、准确性与鲁棒性；已有工作对市面合规检查器做实证研究与评估 [29]。这说明"AI Act 合规检查"已从概念走向**可被比较的产品类别**，但各检查器的覆盖度与正确性结论 `> 待核实`（摘要截断）。
  - 热度：`> 待核实`｜权威：arXiv cs.AI 预印本，2026-09 [29]｜关注度：**低**｜推荐度：**★★★★☆**（本次证据集中唯一对"合规工具本身做评估"的工作，方法学价值高）
- **工具化的公平性维度被提出**：面向 EU AI Act 的 pro-justice 工具包研究指出，AI 实务者确定将需要额外指导与工具来满足要求，而此前关于工具包的研究存在不足，因此主张跨部门专家共创 [25]。
  - 热度：`> 待核实`｜权威：arXiv cs.CY 预印本，2025-05 [25]｜关注度：**低**｜推荐度：**★★★★☆**（少见地把"合规工具的分配正义后果"纳入设计目标）
- **合规证据的可读性被视为产品级缺口**：见 [27]，"政策脚手架成熟 / 基础设施缺失"的判断直接指向一个尚未被产品化的中间层。
  - 热度：`> 待核实`｜权威：arXiv cs.CY 预印本，2026-04 [27]｜关注度：**低**｜推荐度：**★★★★☆**
- **安全关键产品的合规方法学**：面向 safety-critical 产品的 EU AI Act 合规方法论，把合规路径与产品安全工程流程对接 [30]；另有工作把 AI Act 合规保证与 LLM 对抗鲁棒性合并讨论 [24]。
  - 热度：`> 待核实`｜权威：均为 arXiv 预印本（2024-03 [30]、2024-10 [24]）｜关注度：**低**｜推荐度：**★★★☆☆**（合规与安全工程的接缝，是被低估的工程议题）

### 2.2 表 2：开源项目与工具（含"工具型"研究原型）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Pro-justice EU AI Act Toolkit [25] | 2025 | 未在候选块给出 `> 待核实` | `> 待核实` | arXiv cs.CY 预印本 [25] | **低** | ★★★★☆ | http://arxiv.org/abs/2505.17165v1 | 合规工具包设计研究；**是否已开源代码未在候选块中说明** `> 待核实` |
| Making AI Compliance Evidence Machine-Readable [27] | 2026 | 未在候选块给出 `> 待核实` | `> 待核实` | arXiv cs.CY 预印本 [27] | **低** | ★★★★☆ | http://arxiv.org/abs/2604.13767v1 | 机器可读合规证据的基础设施提案；实现与开源状态 `> 待核实` |
| EU AI Act Compliance Checkers 实证评估 [29] | 2026 | 未在候选块给出 `> 待核实` | `> 待核实` | arXiv cs.AI 预印本 [29] | **低** | ★★★★☆ | http://arxiv.org/abs/2609.36228v1 | 对既有检查器做评测；被评工具清单 `> 待核实` |
| Safety-critical Products 合规方法学 [30] | 2024 | 未在候选块给出 `> 待核实` | `> 待核实` | arXiv 预印本 v2 [30] | **低** | ★★★☆☆ | http://arxiv.org/abs/2403.16808v2 | 合规流程与安全工程流程的对接 |
| EU AI Act 合规 + LLM 对抗鲁棒性 [24] | 2024 | 未在候选块给出 `> 待核实` | `> 待核实` | arXiv 预印本 [24] | **低** | ★★★☆☆ | http://arxiv.org/abs/2410.05306v1 | 把"合规"与"可攻击性"放在同一保证框架内 |
| Docling（文档转换工具）[26] | 2025 | 未在候选块给出 `> 待核实` | `> 待核实` | arXiv 预印本；通用开源文档转换工具 [26] | **低** | ★★☆☆☆ | http://arxiv.org/abs/2501.17887v1 | **非治理工具**；仅在"合规文档→机器可读证据"流水线中可能充当组件（此关联为推断，`> 待核实`） |
| Generative AI Toolkit [28] | 2024 | 未在候选块给出 `> 待核实` | `> 待核实` | arXiv 预印本；LLM 应用全生命周期质量框架 [28] | **低** | ★★☆☆☆ | http://arxiv.org/abs/2412.14215v1 | **非合规工具**；与治理仅间接相关，列出以说明"工具"标签易被误用 |

> **工业界维度的诚实结论**：本次证据集**未包含任何厂商官方博客、产品发布页、采购或部署公告**，因此"哪家企业真正上线了 AI 治理产品""合规市场规模"等问题在本报告中**无法回答**，标注 `> 待核实`。

---

## 3. 蓝海与缺口（Blue Ocean & Gaps）

**一句话增量判断**：缺口不是"没人研究 AI 治理"，而是**"治理研究"与"法域事实"之间、以及"原则文本"与"可审计证据"之间，各存在一条无人填补的中间层**。

### 3.1 法域覆盖缺口（最为严重）

- **美国维度完全缺失**：候选证据中无任何联邦行政令/立法进展、亦无州级 AI 法案（前沿模型、陪伴型聊天机器人等）的一手或二手来源 → `> 待核实`。
- **中国维度完全缺失**：无生成式 AI 服务管理办法、算法备案、AI 生成内容标识等规则的任何进展来源 → `> 待核实`。
- **英国与国际组织维度完全缺失**：无英国 AI 安全研究所/立法草案、无 OECD / UN / ISO-IEC 42001 等标准与行为准则的落地信息 → `> 待核实`。
- **无"相对上一版基线"的可比信息**：候选材料未给出任何法规的生效日期、过渡期截止日或实施阶段时间表，因此本报告**无法进行真正的增量比对**，只能做"议题增量"比对。

> 这一缺口本身是本报告最重要的发现之一：**中文语境下做 AI 治理调研，若仅依赖 arXiv cs.CY 检索，会系统性漏掉中国、美国州法与标准组织的全部进展**。建议后续以官方源（EUR-Lex、NIST、OECD.AI、网信办、UK DSIT）为主干重建基线。

### 3.2 制度转译缺口

- **原则→机制的结构性断层**：现有框架"缺乏关于法规如何转译为一致性机制（conformity mechanisms）的清晰说明"，导致 compliance 与 enforcement 出现 gaps [2]；这一判断与 [11] 的经典批判构成同一脉络的两端（2019 年指出原则不足 → 2025 年指出转译路径缺失）。
- **风险缓解框架碎片化**：术语不一致、覆盖有缺口，缺少共同参照系 [3]。

### 3.3 新兴无人区

- **机器身份治理（machine identity）**：AI agent、服务账号、API token 在企业环境中数量已远超人类身份，却缺乏整合性治理框架，据此提出 Machine Identity Governance Taxonomy (MIGT) [5]。
  - 热度：`> 待核实`｜权威：arXiv cs.CR 预印本，2026-04 [5]｜关注度：**低**（新兴议题，尚无引用信号）｜推荐度：**★★☆☆☆**
  - **重要警示**：该文摘要称机器身份与人类身份比例"exceeding 80 to 1"，并援引 2024 年一起损失 `$5.4–10 billion` 的事件，但候选摘要被截断、损失口径（企业样本、损失定义）不明 → **这两个数字必须回原文核实后方可引用** `> 待核实`。
- **AI 事故治理（incident governance）**：事故报告制度是"原则→证据"链条上最容易被制度化的接口，但其开放问题尚未被系统梳理 [8]（arXiv 2607，2026-07）。
  - 热度：`> 待核实`｜权威：arXiv 预印本 [8]｜关注度：**低**｜推荐度：**★★★★☆**（事故报告是唯一能生成"可核查合规证据"的常规机制，判为高杠杆缺口）
- **可复现性作为治理对象**：有工作主张把 reproducibility 本身作为 AI 治理的新前沿 [9]，即"可复现"从科研规范升级为准入/审计要求。
  - 热度：`> 待核实`｜权威：arXiv 预印本，2025-10 [9]｜关注度：**低**｜推荐度：**★★★★☆**（与 [27] 的"机器可读证据"形成互补，合起来构成"可核查性"议程）
- **前沿生物模型的监管归类**：因 EU AI Act 措辞存在模糊性，有研究专门论证生物前沿基础模型 ESM3 在多大程度上落入"具系统性风险的通用目的 AI 模型"义务，并把 ESM3 映射到 biorisk chain [18]。
  - 热度：`> 待核实`｜权威：arXiv cs.CY 预印本 [18]｜关注度：**低**｜推荐度：**★★★★☆**（"模型能力→监管类别"的归类方法是可复用的分析模板）
- **国际治理的代表性缺口**：国际 AI 治理讨论中的"全球多数（Global Majority）"缺席问题 [6]。
  - 热度：`> 待核实`｜权威：arXiv 预印本 [6]｜关注度：**低**｜推荐度：**★★★★☆**（地缘维度上最稀缺的视角）
- **前瞻性治理工具**：面向核领域提出 AI Observatory 作为 anticipatory governance 工具 [4]，与 [7] 的"核类比"研究互为表里——类比既是制度想象力的来源，也是最容易被误用的论证捷径。
  - 热度：`> 待核实`｜权威：arXiv 预印本，2025-04 [4]；[7] 2025-10｜关注度：**低**｜推荐度：**★★★☆☆**

---

## 4. 瓶颈与拐点（Bottleneck & Inflection）

**一句话增量判断**：当前瓶颈已从"缺原则"转为"**缺可机器读取、可第三方复核的合规证据**"；拐点信号是合规检查器与证据格式同时出现，但尚未出现任何被官方承认的合规证据标准。

### 4.1 四类瓶颈

| 瓶颈类型 | 具体表现 | 证据 |
|---|---|---|
| **证据/基础设施瓶颈** | 政策脚手架成熟，但"产出机器可读合规证据"的基础设施缺失，构建高风险 AI 系统的组织因此断层 | [27] |
| **法律确定性瓶颈** | GPAI Code of Practice 带来"非对称法律不确定性"：同一文本对不同主体产生不同确定性；且存在"延迟执法但报告义务先行"的间隔期张力 | [20][21][22] |
| **条文解释瓶颈** | 适用范围（internal deployment）、模型归类（生物基础模型是否 GPAI systemic risk）等边界问题仍未收敛 | [17][18] |
| **评测错配瓶颈** | 现有公开基准集中在**模型能力与内容安全**（音频理解、开放问答、视频安全），与"是否满足 AI Act 某条款"不构成映射关系；合规侧则只有对检查器的实证评估，尚无公认的合规基准 | [29][31][32][33]（错配判断为本报告推断，`> 待核实`） |
| **成本瓶颈** | 合规成本被表述为"证据生产成本"而非"法律咨询成本"，但本次证据集**无任何量化成本数据** | `> 待核实` |

### 4.2 表 3：数据集与基准（附相关性判定）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| EU AI Act Compliance Checkers 实证评估 [29] | 2026 | 未在候选块给出 `> 待核实` | `> 待核实` | arXiv cs.AI 预印本 [29] | **低** | ★★★★☆ | http://arxiv.org/abs/2609.36228v1 | 最接近"合规评测"的工作，但是对工具而非模型的评估；是否发布数据集 `> 待核实` |
| Video-SafetyBench [33] | 2025 | 未在候选块给出 `> 待核实` | `> 待核实` | arXiv 预印本 v3 [33] | **低** | ★★★☆☆ | http://arxiv.org/abs/2505.11842v3 | 视频 LVLM 安全评测；**属内容安全，非监管合规** |
| AIR-Bench [31] | 2024 | 未在候选块给出 `> 待核实` | `> 待核实` | arXiv 预印本 v2 [31] | **低** | ★★☆☆☆ | http://arxiv.org/abs/2402.07729v2 | 音频-语言模型生成式理解基准；**与治理无直接关系** |
| Open-LLM-Leaderboard [32] | 2024 | 未在候选块给出 `> 待核实` | `> 待核实` | arXiv 预印本 [32] | **低** | ★★☆☆☆ | http://arxiv.org/abs/2406.07545v1 | 开放式问答评测与 arena；**与治理无直接关系** |

> **基准章节的诚实结论**：本次检索**未发现任何专为 AI 治理/监管合规设计的公开数据集或基准**。表 3 中三条模型基准与治理的相关性均弱，列出是为了**证明缺口存在**，而非推荐使用。
> 另有 [14] Foundations of GenIR、[15] DeBiasMe、[23] VQualA 三条来源经核与治理主题无关，已剔除，不作引用。

### 4.3 拐点信号清单

1. **合规从"文本"变成"证据格式"**：[27] 提出机器可读合规证据，若该方向被标准化组织采纳，则治理重心将从立法转向审计技术 [27]。
2. **合规工具开始被"评测"而非仅被"提出"**：[29] 对检查器做实证评估，意味着该品类已进入可比阶段 [29]。
3. **行业架构文档开始并列引用金融监管与 AI 监管**：[16] 中 Solvency II 与 AI Act 并列作为设计约束，说明合规正在被工程化吸收 [16]。
4. **执法间隔期制度设计成为独立议题**：[22]。

---

## 5. 社会·政策·国际（Society, Policy & Geopolitics）

**一句话增量判断**：本周期最实质的社会侧增量是**"AI 输出被赋予权威后会收窄人的决策空间"获得了行为学量化证据**，这为监管必要性提供了少见的实证支点；国际维度则仍停留在规范性呼吁。

- **监管必要性的行为学证据**：大规模行为实验（1,305 名被试）显示，当 AI 预测被赋予权威后，个体放弃确定收益的几率提高 **3.39 倍（95% CI 2.45–4.70）**，即"对 AI 的信任会收窄个体所考虑的未来选项集合" [13]。
  - 热度：`> 待核实`｜权威：arXiv cs.HC 预印本 v2，非同行评审，但为大规模行为实验、方法可核查性较强 [13]｜关注度：**低**｜推荐度：**★★★☆☆**（**注意**：该文与"法规进展"无直接关系，仅在论证"为何需要监管介入"时可引用）
- **国际治理的代表性与分配正义**：国际 AI 治理中的"全球多数"缺席问题被单独提出 [6]。
  - 热度：`> 待核实`｜权威：arXiv 预印本 [6]｜关注度：**低**｜推荐度：**★★★★☆**
- **制度类比的滥用风险**：核类比在 AI 治理研究中被系统检视 [7]；同时核领域自身提出了 AI Observatory 作为前瞻性治理工具 [4]——两条线共同说明"借用成熟高风险行业的制度模板"是当前国际治理想象力的主要来源，也是最需警惕的论证捷径。
  - 热度：`> 待核实`｜权威：均为 arXiv 预印本 [4][7]｜关注度：**低**｜推荐度：**★★★☆☆**
- **企业自我治理与硬监管的落差**：对 OpenAI 的个案研究以结构化语料 + 定性编码 + NLP 主题建模，量化 ethics / safety / alignment 等术语随**受众**（一般公众 vs 学术受众）与**时间**的变化，代码已公开以便复现 [1]。
  - 热度：`> 待核实`｜权威：arXiv cs.CY 预印本，2026-01 [1]｜关注度：**低**｜推荐度：**★★★☆☆**（方法可复现是其最大价值；单一个案不可外推至全行业）
- **原则主义的替代路径**：从"原则不足" [11] 到"超越原则主义、给出可操作策略" [10]，再到"以伦理审计落地治理"的产业案例 [12]，构成一条清晰的学理修正链条。
  - 热度：`> 待核实`｜权威：均为 arXiv 预印本 [10][11][12]｜关注度：**中**（该链条已成为领域共同语汇）｜推荐度：**★★★★☆**
- **地缘与供应链维度**：本次证据集**无任何**关于出口管制、算力供应链、数据跨境、AI 军事应用或劳动影响的来源 → `> 待核实`。

---

## 6. 资本与生态（Capital & Ecosystem）

**一句话增量判断**：**本周期在资本维度无显著可核证据**——本次检索未获得任何融资额、并购、估值、人才流动或市场规模数据。以下仅陈述"生态结构"层面可观察到的变化，且强度有限。

- **出版生态：同一议题在多渠道并行**。GPAI Code of Practice 的"非对称法律不确定性"研究同时以 OSF 预印本 [20]、SSRN 预印本 [21] 出现，另有期刊 DOI 版本讨论执法间隔期 [22]。这提示**法学/政策学界正在快速进入 AI 治理议题**，与 arXiv cs.CY 的计算机-社会交叉群体形成两套并行话语。
  - 热度：`> 待核实`（无引用数）｜权威：[20][21] 为预印本平台文本，[22] 为期刊 DOI（同行评审状态 `> 待核实`）｜关注度：**中**（同题多平台投放是资源投入的信号）｜推荐度：**★★★★☆**
- **工具生态：原型多、采用记录为零**。合规工具 [25]、合规证据基础设施 [27]、合规检查器 [29]、安全关键产品方法学 [30] 各自独立出现，彼此**未形成引用网络**（候选块无互引证据）。这更像"多点开花的前标准化阶段"，而非成熟生态。
  - 热度：`> 待核实`｜权威：均为预印本 [25][27][29][30]｜关注度：**低**｜推荐度：**★★★★☆**（对判断"何时会出现合规工具整合者"有指示意义）
- **机构格局**：本次证据集**无法识别**任何机构的主导地位（作者所属机构在候选块中缺失比例高）→ `> 待核实`。
- **明确不做的判断**：不评估"AI 治理赛道融资规模""合规 SaaS 市场空间""人才缺口数量"。这些均无来源支撑，任何数字都会是编造。

---

## 7. 信号与预测（Signals & Forecast）

> 标记约定：`[P]` = 预测（附依据链与可证伪条件）；`[R]` = 传闻/未证实；`[Debated]` = 存在争议；未标记者为已确证事实（限本证据集范围）。

### 7.1 早期信号（已可观察）

1. **证据化的合规**：合规讨论的关键词从"原则/承诺"迁移到"机器可读证据/审计轨迹" [27][9]。
2. **工具被评测**：合规检查器进入实证评估阶段 [29]，说明其数量已足以构成比较对象。
3. **归类争议显性化**：模型是否属于"GPAI with systemic risk"成为独立论文主题 [18]，与适用范围争议 [17] 同源——**法律边界问题正在被"案例化"处理**。
4. **执法节奏本身被研究**：延迟执法与报告义务的时间差被单独讨论 [22]。

### 7.2 未来 6–18 个月预判（可证伪假设）

| # | 假设（`[P]`） | 依据链 | 置信度 | 证伪条件 |
|---|---|---|---|---|
| P1 | 到 2027 年中，会出现**至少一个**面向 EU AI Act 的公开"合规证据格式/模式（schema）"提案，并被 ≥2 篇后续论文引用 | 政策脚手架成熟 + 基础设施缺失的诊断 [27] + 检查器已可被评测 [29] → 中间层必然被填补 | 中 | 若 2027-06 前检索不到任何 schema 类工作，则判断失败 |
| P2 | 合规工具将**先分裂后整合**：2026–2027 仍以单点工具（工具包/检查器/证据格式）为主，不出现统一平台 | 现有工具彼此无引用网络（本次证据集观察）[25][27][29][30] | 中 | 若出现被多篇工作共同引用的整合型框架，则判断失败 |
| P3 | **美国州法与中国的规章进展，在 arXiv cs.CY 类文献中将继续被系统性低估**，中英双语双源检索成为必要方法 | 本次 33 条来源中美国/中国/英国维度为 0 [1]–[33] | 较高 | 若后续同类检索能自然召回 ≥3 条中国或美国州法一手分析，则判断失败 |
| P4 | **"机器身份/agent 问责"将成为独立治理议题**，出现 ≥3 篇专门讨论 agent 身份、权限与责任归属的论文 | [5] 已提出 MIGT 且指出数量失衡（80:1 数字待核实）[5] | 中低 | 若 2027-06 前该主题仍只有零星 1–2 篇，则判断失败 |
| P5 | **事故报告（incident reporting）会成为"原则→证据"的第一个制度化接口**，优先于认证与审计 | 事故报告是唯一能常规生成可核查记录的机制 [8]，且已在五层框架中被选为验证案例之一 [2] | 中 | 若认证/审计路径先于事故报告形成可操作标准，则判断失败 |

### 7.3 争议与不确定性（`[Debated]` / `[R]`）

- `[Debated]` **内部部署是否受 AI Act 约束**：备忘录并列支持与反对论据，说明学界内部亦未收敛 [17]。
- `[Debated]` **核类比是否成立**：核领域自身在建设 AI Observatory [4]，而类比的有效性被专门检视 [7]——支持方与质疑方并存。
- `[R]` **机器身份 80:1 比例与 2024 年 `$5.4–10B` 损失**：仅见于被截断的摘要片段，**待证实** [5]。
- `> 待核实` **合规成本量级**：本证据集无任何量化数据，任何"合规成本占研发预算 X%"的说法均不可引用。

### 7.4 Watchlist（值得持续跟踪）

1. EU GPAI Code of Practice 的执法间隔期实践与首批报告义务履行情况 [19][20][21][22]。
2. 机器可读合规证据的格式标准化进展 [27]。
3. 合规检查器的第三方横评（是否出现榜单式比较）[29]。
4. 事故报告的公共数据库与治理规则 [8]。
5. 可复现性要求是否被写入采购/审计条款 [9]。
6. 中国、美国州法、ISO/IEC 42001 的一手进展（**本次完全缺失，须另建检索基线**）`> 待核实`。

---

## 参考来源

[1] Competing Visions of Ethical AI: A Case Study of OpenAI — http://arxiv.org/abs/2601.16513v1
[2] A five-layer framework for AI governance: integrating regulation, standards, and certification — http://arxiv.org/abs/2509.11332v1
[3] Mapping AI Risk Mitigations: Evidence Scan and Preliminary AI Risk Mitigation Taxonomy — http://arxiv.org/abs/2512.11931v1
[4] Towards an AI Observatory for the Nuclear Sector: A tool for anticipatory governance — http://arxiv.org/abs/2504.12358v1
[5] Who Governs the Machine? A Machine Identity Governance Taxonomy (MIGT) for AI Systems Operating Across Enterprise and Geopolitical Boundaries — http://arxiv.org/abs/2604.06148v1
[6] The Global Majority in International AI Governance — http://arxiv.org/abs/2601.17191v1
[7] The Nuclear Analogy in AI Governance Research — http://arxiv.org/abs/2510.21203v1
[8] Open Problems in AI Incident Governance — http://arxiv.org/abs/2607.05163v1
[9] Reproducibility: The New Frontier in AI Governance — http://arxiv.org/abs/2510.11595v1
[10] Beyond principlism: Practical strategies for ethical AI use in research practices — http://arxiv.org/abs/2401.15284v6
[11] Principles alone cannot guarantee ethical AI — http://arxiv.org/abs/1906.06668v2
[12] Operationalising AI governance through ethics-based auditing: An industry case study — http://arxiv.org/abs/2407.06232v1
[13] Faith in AI can narrow the futures individuals consider — http://arxiv.org/abs/2603.28944v2
[14] Foundations of GenIR — http://arxiv.org/abs/2501.02842v1
[15] DeBiasMe: De-biasing Human-AI Interactions with Metacognitive AIED (AI in Education) Interventions — http://arxiv.org/abs/2504.16770v1
[16] Multi-Agent AI Architecture for Regulated Insurers: A generic AI framework under Solvency II and the AI Act in Austria and Germany — http://arxiv.org/abs/2609.27636v2
[17] Internal Deployment in the AI Act — http://arxiv.org/abs/2512.05742v4
[18] The Case for ESM3 as a General-Purpose AI Model with Systemic Risk Under the EU AI Act — http://arxiv.org/abs/2605.01611v1
[19] Mapping Industry Practices to the EU AI Act's GPAI Code of Practice Safety and Security Measures — http://arxiv.org/abs/2504.15181v2
[20] Regulating emerging technologies: Asymmetric legal uncertainty and the EU General-Purpose AI Code of Practice — https://doi.org/10.31235/osf.io/tykag_v1
[21] Regulating emerging technologies: Asymmetric legal uncertainty and the EU General-Purpose AI Code of Practice — https://doi.org/10.2139/ssrn.6425898
[22] Deferred Enforcement, Applicable Reporting: The General-Purpose AI Code of Practice in the EU AI Act's Enforcement Interval — https://doi.org/10.62432/appe.cc.2026.10.26
[23] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1
[24] Towards Assuring EU AI Act Compliance and Adversarial Robustness of LLMs — http://arxiv.org/abs/2410.05306v1
[25] A Toolkit for Compliance, a Toolkit for Justice: Drawing on Cross-sectoral Expertise to Develop a Pro-justice EU AI Act Toolkit — http://arxiv.org/abs/2505.17165v1
[26] Docling: An Efficient Open-Source Toolkit for AI-driven Document Conversion — http://arxiv.org/abs/2501.17887v1
[27] Making AI Compliance Evidence Machine-Readable — http://arxiv.org/abs/2604.13767v1
[28] Generative AI Toolkit -- a framework for increasing the quality of LLM-based applications over their whole life cycle — http://arxiv.org/abs/2412.14215v1
[29] An Empirical Study and Assessment of EU AI Act Compliance Checkers — http://arxiv.org/abs/2609.36228v1
[30] Navigating the EU AI Act: A Methodological Approach to Compliance for Safety-critical Products — http://arxiv.org/abs/2403.16808v2
[31] AIR-Bench: Benchmarking Large Audio-Language Models via Generative Comprehension — http://arxiv.org/abs/2402.07729v2
[32] Open-LLM-Leaderboard: From Multi-choice to Open-style Questions for LLMs Evaluation, Benchmark, and Arena — http://arxiv.org/abs/2406.07545v1
[33] Video-SafetyBench: A Benchmark for Safety Evaluation of Video LVLMs — http://arxiv.org/abs/2505.11842v3

---

*Generated by research-bot · topic=`ai-治理与监管政策法规与标准` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`deepseek-v4-flash` · sources=33 · duration=172s · 2026-10-17T22:28:22+00:00*
