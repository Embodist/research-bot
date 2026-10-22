# 全球 AI 治理与监管的增量快照（2025–2026）

**报告日期**：2026-10-22（UTC） | **领域**：AI 治理与监管（政策 / 法规 / 标准） | **检索源**：本次可引用来源 32 条，其中与 AI 治理、法规文本分析与合规工程直接相关 18 条；一手法规原文 0 条 | **观察窗口**：2024-01 – 2026-09（年份以 arXiv ID 前缀 `YYMM` 的首次提交年月推断，SSRN / 书章 DOI 无法推断者标注 `> 待核实`）

**证据基线与质量声明（必读）**

1. 本批可引证据**全部为二手学术分析（arXiv 预印本、SSRN 工作论文、法律评注书章）**，**不含任何一手法规文本、官方标准文档、监管机构公告或 AI Safety Institute 网络官方页面**。因此本报告对"某条款是否已生效"的一切判断，均为**从学术文本的措辞反推**，属间接证据，一律加限定词或标注 `> 待核实`。
2. 上游检索结果存在明显噪声：分配给 q1/q2 的 `Faith in AI can narrow the futures individuals consider` [2]、`The New Shape of Search` [6] 与 AI 治理主题无关；`Foundations of GenIR` [3]、`Towards The Ultimate Brain` [8]、`Need of AI in Modern Education` [11]、`DeBiasMe` [13] 亦不构成治理证据。本报告**不将其作为治理论断的依据**，仅在必要时说明其被排除。
3. **所有条目的引用数（citations）、GitHub star、下载量均无法从本批来源中取得**，故"热度证据"一律写 `> 待核实`，**不填任何数字**。推荐度因此主要依据"权威 + 与主题相关性"给出，普遍不高于 ★★★☆☆。
4. 全文标注约定：`[R]` 传闻/未证实；`[P]` 预测（附可证伪条件）；`[Debated]` 存在争议；`> 待核实` 证据不足。

---

## 1. 进展与热点（Progress & Hotspots）

**一句话增量判断**：相对 2023–2024 年"原则宣言 + 风险分级框架"的基线，2025–2026 年真正的增量是**治理研究的重心从"该管什么"下移到"如何证明合规"**——即从伦理学与政策学转向合规工程（compliance engineering）、需求工程与证据基础设施；但**执法时间线与生效状态的权威确认在本批证据中完全缺失**。

### 1.1 从"原则"到"规格"：合规工程化成为新热点

- **EU AI Act 的义务正在被翻译成可验证的工程规格。** 一项 2026 年的综述系统梳理了在需求工程（RE）中验证 AI Act 要求的方法学现状，标题即点明"从义务到规格（From Obligation to Specification）" [31]。这是相对早期"原则清单"式研究的实质性推进：它把法条当作需求源，讨论如何 elicitation / traceability / validation。
  - 热度：`> 待核实` | 权威：arXiv cs.CY/SE 方向预印本，未经同行评审确认 [31] | 关注度：低（无可核引用/讨论数据） | 推荐度：★★★☆☆（主题高度相关，但预印本且方法学尚在早期）
- **"合规证据可机读"被明确识别为一个独立技术问题。** 2026 年的工作指出：AI Assurance 领域"政策脚手架已成熟，但缺乏将其操作化的基础设施"，构建高风险 AI 系统的组织面临框架（如模型卡、审计报告）与实际证据链之间的断裂 [27]。
  - 热度：`> 待核实` | 权威：arXiv 预印本 [27] | 关注度：低 | 推荐度：★★★☆☆（提出了本领域最关键的工程缺口之一）
- **监管—标准—认证的三层衔接首次被显式建模。** 2025 年的五层框架论文直言现有框架"缺乏对监管如何转化为符合性机制（conformity mechanisms）的清晰说明，导致合规缺口" [5]。
  - 热度：`> 待核实` | 权威：arXiv 预印本，期刊投稿体例（含 Purpose/Method 结构，疑为期刊论文）[5] | 关注度：低 | 推荐度：★★★☆☆

### 1.2 GPAI 义务：从法条走向操作，但边界仍模糊

- **GPAI Code of Practice 已进入"产业实践映射"阶段**：2025 年的研究将产业界实际做法逐条对照 AI Act GPAI 行为准则中的**安全与安保（Safety and Security）措施** [30]。这说明行为准则文本已足够具体，可以被拿来与工程实践做 gap 分析——是"已生效法律 + 软法准则"组合落地的直接信号。
  - 热度：`> 待核实` | 权威：arXiv 预印本 [30] | 关注度：低 | 推荐度：★★★☆☆
- **"系统性风险"的认定标准仍是开放问题。** 一项 2026 年研究以生物基础模型 ESM3 为例，论证因 AI Act 措辞模糊，**前沿生物基础模型是否落入"具系统性风险的通用目的 AI 模型"义务范围并不确定** [14]；法律评注书章则专门处理第 51、52、55 条的**分类与具体义务** [21]。二者共同说明：条款文本已存在且可被逐条评注，但**分类判据的可操作性未收敛** [Debated]。
  - 热度：`> 待核实` | 权威：[21] 为 Bloomsbury 法律评注书章，权威性高于一般预印本；[14] 为 arXiv 预印本 | 关注度：低 | 推荐度：★★★★☆（[21] 是本次证据集中最接近"权威法条释义"的来源）
- **适用范围争议：内部部署（internal deployment）是否受管辖。** 2025–2026 年的一份备忘录专门对"AI Act 是否应涵盖内部部署"的正反论证做压力测试，并给出多条解释路径 [15]。这是"法律文本已定、解释未定"的典型增量信号。
  - 热度：`> 待核实` | 权威：arXiv 预印本（v4，经多轮修订）[15] | 关注度：低 | 推荐度：★★★☆☆

### 1.3 实施层机制：上市后监测与合规保证

- **上市后监测（post-market monitoring）已形成"义务—架构—实现"三段式讨论**，说明监管重心从准入前审批延伸到全生命周期 [20]（SSRN 工作论文，年份 `> 待核实`）。
- **合规保证与对抗鲁棒性被放在同一框架下讨论**（2024）[17]，是较早把"法条合规"与"模型鲁棒性测试"接起来的尝试。
  - 热度：`> 待核实` | 权威：arXiv 预印本 [17][20] | 关注度：低 | 推荐度：★★★☆☆

### 1.4 立法回摆信号：Digital Omnibus

- 一项 SSRN 研究讨论 **Digital Omnibus 与工人权利**，标题指向"权利行使与执行条件的重构" [18]。这提示 2025–2026 年欧盟层面出现了**以简化/减负为名的立法调整**，可能改变既有数字法规（含 AI 相关义务）的执行条件。
  - 热度：`> 待核实` | 权威：SSRN 工作论文，未经同行评审 [18] | 关注度：低 | 推荐度：★★★☆☆ | **注意**：本报告仅能确认"存在这一学术讨论"，**Digital Omnibus 的具体条文内容与对 AI Act 的修改范围 `> 待核实`**。

### 1.5 明确未能确认的事项（缺口，不是结论）

- **主要司法辖区立法与执法时间线**：本批证据中**没有任何**美国行政令 / 联邦立法、中国生成式 AI 管理办法、英国 / 日本 / 新加坡立法的可引来源 → 该子问题 `> 待核实`，不做陈述。
- **AI 安全研究所网络（AISI Network）与多边机制进展**：本批证据中**无一手或二手可引来源** → `> 待核实`。任何"国际AI安全研究所网络已扩展至 N 国"之类的表述在本报告中**不予给出**，因为无来源支撑。
- **"哪些已生效"的权威裁定**：仅能间接推断 EU AI Act 已通过并进入实施（依据是学术界已在讨论其"上市后监测义务"[20]、"行为准则措施"[30]、"第 51/52/55 条释义"[21]）。此推断标为**中等置信度的间接证据**。

---

## 2. 工业界与产品（Industry & Product）

**一句话增量判断**：产业侧的可核增量集中在**审计与红队两类"合规生产工具"的方法论反思**上，而非成熟产品；本批证据**不含任何厂商产品页、GitHub 仓库或模型卡工具链官方文档**，故"工具链成熟度"无法评级。

### 2.1 审计工具：被明确判定为"存在系统性缺口"

- 2024 年的系统性调研 `Towards AI Accountability Infrastructure` 直接以"AI 审计工具的缺口与机会"为题，对审计工具生态做了盘点 [22]。这是本次证据集中唯一一篇**以工具生态为对象**的研究。
  - 热度：`> 待核实` | 权威：arXiv 预印本（v3，多轮修订）[22] | 关注度：低（无可核引用/star） | 推荐度：★★★★☆（主题相关度最高、且是少见的生态级盘点）
- 与 [27]（合规证据可机读，2026）合起来看，可形成一个**跨两年的连续判断**：2024 年识别出审计工具缺口 [22] → 2026 年该缺口被重新表述为"证据基础设施缺失" [27]。**增量在于问题被更精确地命名，而非已被解决**（此判断为分析性归纳，非来源原话）。

### 2.2 红队（red teaming）：从"做红队"到"质疑红队"

- **模型级 vs 智能体级红队的可比性研究**（2025）：在开源权重模型 GPT-OSS-20B 上，结合"动作图可观测性（action-graph observability）"，发现模型层安全缺陷**不能完整刻画智能体部署中的风险** [23]。这是把红队对象从"模型"扩展到"工具调用轨迹"的实质推进。
  - 热度：`> 待核实` | 权威：arXiv cs.AI 预印本 [23] | 关注度：低 | 推荐度：★★★★☆（提出 agentic 级评估这一新对象）
- **对红队方法本身的批判**（2025）：`Red Teaming AI Red Teaming` 指出尽管红队在 AI 治理中被广泛采用，但其**作为治理手段的有效性存在显著缺口** [25]。
  - 热度：`> 待核实` | 权威：arXiv cs.AI 预印本（v2）[25] | 关注度：低 | 推荐度：★★★★☆（治理有效性质疑，属"negative results"，方法论上应重视）
- **规模化红队方法**：面向数学任务幻觉的大规模红队 [24]、多样攻击学习用于鲁棒红队与安全微调 [26]，构成红队"技术侧"的补充，但与"治理合规"关联较弱。
  - 热度：`> 待核实` | 权威：arXiv 预印本 [24][26] | 关注度：低 | 推荐度：★★★☆☆

### 2.3 企业实践与期望演化（弱相关，仅作背景）

- 一项 2023–2025 两阶段访谈研究追踪了企业 AI 在项目型软件团队中期望的**分化过程** [28]。它可作为"企业侧需求已从个人助理转向团队协作"的定性证据，但**不构成合规实践证据**。
  - 热度：`> 待核实` | 权威：arXiv cs.HC 预印本 [28] | 关注度：低 | 推荐度：★★☆☆☆（与治理主题弱相关）

### 2.4 无法评级的事项

- **开源治理项目成熟度**（模型卡工具、数据溯源、审计平台）：本批证据**无任何可核仓库或官方文档** → `> 待核实`，不给出成熟度结论。
- **开源权重模型与监管义务的张力**：本批证据仅在 [23] 中以 GPT-OSS-20B 作为**评测对象**出现，**并未讨论开源权重与合规义务的法律张力** → 该子问题 `> 待核实`。
- **训练数据版权、算力出口管制、监管俘获 / "安全洗白"**：本批证据**无一条直接来源** → 全部 `> 待核实`，本报告不做任何事实性陈述。

---

## 3. 蓝海与缺口（Blue Ocean & Gaps）

**一句话增量判断**：本领域最清晰的"无人区"不是"再写一个治理框架"（框架已过剩），而是**把法律义务转成机器可判定的证据、并让第三方能独立核验**——这一层在 2024–2026 年间被反复识别为空白却始终未被填补。

| # | 缺口 | 证据 | 缺口性质 | 证据等级 |
|---|------|------|----------|----------|
| G1 | **合规证据基础设施**：政策脚手架成熟，但把证据做成机器可读、可交换、可审计的基础设施缺失 [27] | [27] | 工程/标准空白 | B（预印本） |
| G2 | **AI 审计工具生态**：工具零散、覆盖不全，缺乏统一接口与可追责链路 [22] | [22] | 工具生态空白 | B |
| G3 | **义务→规格的转换方法**：法条如何落到可测试需求，缺乏系统方法学 [31] | [31] | 方法学空白 | B |
| G4 | **红队作为治理手段的有效性未验证**：广泛采用但缺乏有效性证据 [25] | [25] | 评估科学空白 | B |
| G5 | **智能体级（agentic）评估与可观测性**：模型级红队无法覆盖工具调用风险，缺乏动作级观测标准 [23] | [23] | 评测与可观测性空白 | B |
| G6 | **法律归类判据缺失**：GPAI"系统性风险"的判定门槛对前沿科学模型（如生物基础模型）不可操作 [14]；第 51/52/55 条虽有评注但判据仍模糊 [21] | [14][21] | 法律解释空白 | [21] A-/B+、[14] B |
| G7 | **管辖边界未定**：内部部署是否属于 AI Act 适用范围无定论 [15] | [15] | 法律解释空白 | B |
| G8 | **垂直行业观测站**：核领域已有"AI 观测站"作为预见性治理工具的构想 [1]，其他高风险垂直行业（医疗、能源、交通）**未见对应设计** | [1] | 制度设计空白（推论） | B |
| G9 | **风险缓解措施的分类学**：2025 年的 evidence scan 仍只给出"初步（preliminary）"分类学 [12] | [12] | 知识组织空白 | B |

**高杠杆机会（编辑判断，非来源结论）**：G1 + G3 + G5 三者交集——**面向智能体系统的、机器可读的合规证据格式 + 对应测试方法**，同时满足法条要求 [30][31]、审计需求 [22] 与 agentic 风险评估需求 [23]，且目前无成熟方案。

---

## 4. 瓶颈与拐点（Bottleneck & Inflection）

**一句话增量判断**：瓶颈已从"缺乏治理原则"转移到**"法律文本的模糊性 × 证据不可机读 × 评估有效性未证"的三重耦合**；拐点信号表现为"标准/认证/需求工程"这三个中介层的首次同时出现，但尚未跨过临界点。

### 4.1 四个可定位的瓶颈

1. **文本模糊性瓶颈**：AI Act 措辞的歧义直接导致义务不可判定——[14] 以 ESM3 为例展示"是否属系统性风险"无法从文本唯一确定；[15] 展示"内部部署"在管辖内外均可自洽解释。[Debated]
2. **证据瓶颈**：合规需要"机器可读证据"，但当前只有政策脚手架 [27]；审计工具亦不足 [22]。
3. **评估有效性瓶颈**：红队被广泛用于治理，但其有效性证据缺失 [25]；模型级红队无法外推到 agentic 部署 [23]。
4. **规格化瓶颈**：法条到可验证需求的转换缺乏方法学 [31]；标准—认证中介层此前"缺乏清晰说明" [5]。

### 4.2 拐点信号（可观测，但方向双向）

| 信号 | 观测 | 指向 | 证据 |
|------|------|------|------|
| S1 中介层成型 | 2025 年出现"监管→标准→认证"五层衔接框架 | 治理从宣言走向可操作 | [5] |
| S2 行为准则可对照 | GPAI Code of Practice 的安全与安保措施已可与产业实践逐条映射 | 软法开始产生实际约束力 | [30] |
| S3 需求工程介入 | 2026 年出现"从义务到规格"的系统综述 | 法条进入软件工程流水线 | [31] |
| S4 证据格式被提出 | 2026 年明确提出"合规证据机器可读" | 自动化合规的前置条件被命名 | [27] |
| S5 立法简化回摆 | Digital Omnibus 与工人权利的执行条件被讨论 | **反向信号**：义务可能被简化/推迟 | [18] |

**判断**：S1–S4 构成"合规工程化"拐点的**早期信号**，但**尚无任何独立验证或落地部署证据**（无监管机构采纳记录、无产品发布、无第三方复现），因此**不能称为已发生的拐点**，只能说"拐点条件正在聚集"。

### 4.3 成本与人力瓶颈

- 本批证据**未提供**任何关于合规成本、审计人力供给、评测算力开销的量化数据 → `> 待核实`，不做估算。

---

## 5. 社会·政策·国际（Society, Policy & Geopolitics）

**一句话增量判断**：可核增量集中在**"风险分类本身具有政治性"这一批判性认识**，以及**劳动者权利在数字立法简化中被重新配置**；但本批证据对国际机制（多边协定、出口管制、地缘供应链）**几乎空白**，此维度只能给出有限结论。

### 5.1 风险分类的政治性

- 2024 年的工作提出把"(地缘)政治分类学"用于 AI 风险与监管措施，直接以 `Taxonomy to Regulation` 为题，主张 AI Act 中的风险分类并非价值中立 [32]。
  - 热度：`> 待核实` | 权威：arXiv 预印本 [32] | 关注度：低 | 推荐度：★★★☆☆
- 与之呼应，2026 年对 OpenAI 公共话语的案例研究显示，`ethics` / `safety` / `alignment` 等术语被不同行动者**战略性使用**，形成"竞争性的伦理 AI 愿景" [4]。
  - 热度：`> 待核实` | 权威：arXiv cs.CY 预印本 [4] | 关注度：低 | 推荐度：★★★☆☆（提供了"话语即治理"的经验材料）
- 更早的 `Beyond principlism`（2024）主张超越原则主义、转向可操作策略 [9]，构成上述批判的方法论前身。
  - 热度：`> 待核实` | 权威：arXiv 预印本（v6，多轮修订）[9] | 关注度：低 | 推荐度：★★★☆☆

### 5.2 劳动者权利与立法简化

- Digital Omnibus 被分析为**重构权利行使与执行条件**的立法动作 [18]。这提示一个结构性影响：即便实体义务不变，**程序性条件（谁可主张、如何主张、由谁执行）的改变即可实质削弱保护**。
  - 热度：`> 待核实` | 权威：SSRN 工作论文 [18] | 关注度：低 | 推荐度：★★★☆☆ | 具体条文与生效状态 `> 待核实`
- **劳动影响、就业替代的量化证据**：本批来源**无** → `> 待核实`。

### 5.3 国际与地缘维度（重大缺口）

- **多边机制**（联合国决议、G7/G20 进程、AI Safety Institute 网络、国际标准组织 JTC 1/SC 42 进展）：本批可引证据**无一条**覆盖 → `> 待核实`，本报告**不陈述**。
- **算力/芯片出口管制与供应链约束**：本批来源**无** → `> 待核实`。
- **监管竞争与"布鲁塞尔效应"**：本批来源可间接支撑"EU AI Act 是全球学术分析的中心参照系"（18 条相关来源中至少 8 条以其为对象 [14][15][17][20][21][30][31][32]），但**这只是学术关注度分布，不是监管趋同的证据**。此区分必须保留。

---

## 6. 资本与生态（Capital & Ecosystem）

**一句话增量判断**：本批证据**不支持任何关于融资额、并购、公司格局或人才流动的结论**；唯一可核的"生态"变化是**学术出版形态向法律—工程交叉带迁移**（SSRN 工作论文、法律评注书章、需求工程会议体例同时出现）。

### 6.1 可核的生态信号

| 信号 | 观测事实 | 证据 | 说明 |
|------|----------|------|------|
| E1 法律评注体系化 | 出现针对 AI Act 第 51/52/55 条的书章级评注 | [21] | 表明该法已进入"教科书/评注"阶段，是制度成熟的中期标志 |
| E2 工作论文渠道活跃 | 多篇 SSRN 工作论文讨论 AI Act 实施细节（上市后监测、Digital Omnibus） | [18][20] | 法律学界快速响应，但未经同行评审 |
| E3 工程学科进入 | 需求工程、软件验证视角的论文出现 | [31][17] | 治理议题跨入 SE 社区 |
| E4 垂直领域外溢 | 核领域提出"AI 观测站"作为预见性治理工具 | [1] | 治理工具开始按行业定制 |
| E5 学术话语竞争 | OpenAI 伦理话语被作为案例研究对象 | [4] | 企业话语成为治理研究对象 |

### 6.2 明确无法确认的事项

- **投融资、并购、估值、人才流动**：本批证据**零覆盖** → `> 待核实`。**本周期该维度无显著可核变化**，本报告不填补。
- **开源生态（star 数、贡献者、下载量）**：零覆盖 → `> 待核实`。
- **第三方合规服务市场是否形成**：无来源 → `> 待核实`。仅能从 [22][27] 推断"需求被识别"，**不能推断"市场已存在"**。

---

## 7. 信号与预测（Signals & Forecast）

**一句话增量判断**：未来 6–18 个月最可检验的分歧点是——**"合规工程化"会不会在缺乏官方标准背书的情况下自行成势**；本报告给出 4 条可证伪假设，全部标注置信度与判据。

### 7.1 可证伪假设

**[P1] 机器可读合规证据将成为 GPAI/高风险 AI 合规的主流技术形态。**
- 依据链：政策脚手架已成熟但基础设施缺失 [27] → 审计工具缺口早已识别 [22] → 行为准则措施已可与实践映射 [30] → 需求工程开始承接法条 [31]。
- 可证伪条件：**若到 2027-06 仍未出现任何被监管机构、标准组织或主流云厂商采纳的合规证据 schema / 交换格式（公开可查），则本假设不成立。**
- 置信度：**中**。主要不确定性：官方标准（如 CEN-CENELEC 协调标准）进度在本批证据中完全不可见 `> 待核实`。

**[P2] 智能体（agentic）系统评估将成为下一个规范空白的主战场。**
- 依据链：模型级红队无法覆盖工具调用风险 [23] → 红队作为治理手段有效性未证 [25] → 现有 AI Act 义务结构以"模型/系统"为单位，未细化到动作轨迹。
- 可证伪条件：**若到 2027-06 前，主要辖区的正式指引/标准草案仍未出现"智能体""工具调用""动作轨迹"级别的评估要求，则本假设不成立。**
- 置信度：**中**。

**[P3] 立法简化（Omnibus 类）将导致部分 AI 义务的时间表或程序性条件被调整。**
- 依据链：Digital Omnibus 已被分析为重构权利执行条件 [18]；同时学术界仍在密集解释既有义务 [15][21]，说明"义务已定、执行未定"的窗口期存在。
- 可证伪条件：**若到 2027-06，AI Act 相关义务的生效时间表与程序条件均无任何正式修订，则本假设不成立。**
- 置信度：**低–中**。仅有一条二手来源 [18]，且其具体条文内容 `> 待核实`。

**[P4] "系统性风险"的判定门槛将因前沿科学模型（生物、化学）而被迫给出正式澄清。**
- 依据链：ESM3 案例显示现有措辞无法唯一判定 [14]；第 51/52/55 条的评注已存在但判据不可操作 [21]。
- 可证伪条件：**若到 2027-12，欧盟层面仍未发布任何针对基础科学模型的分类指引或FAQ，则本假设不成立。**
- 置信度：**低**。属推测，依据为单一学术论证。

### 7.2 早期信号清单（Watchlist）

| 观察对象 | 为什么值得盯 | 触发阈值 | 证据 |
|----------|--------------|----------|------|
| GPAI 行为准则的后续版本与签署情况 | 判断软法是否产生硬约束 | 出现可核的签署方清单或多边互认 | [30] |
| 合规证据格式的公开实现 | P1 的直接判据 | 出现可核 schema + 至少一个采纳方 | [27][22] |
| 智能体评估标准的草案 | P2 的直接判据 | 任一标准组织立项/草案公开 | [23][25] |
| Omnibus 类立法的最终文本 | P3 的直接判据 | 正式公布文本并列出被修改条款 | [18] |
| 生物/科学基础模型的监管归类文件 | P4 的直接判据 | 监管机构发布分类指引 | [14][21] |
| 垂直行业观测站（核以外） | G8 缺口是否被填补 | 出现医疗/能源/交通领域的观测站设计 | [1] |

### 7.3 本报告的不确定性总账

- **高不确定性**：所有关于"已生效/执法时间线/国际机制/资本流动"的内容 —— 均因**一手来源缺失**而无法确认。
- **中不确定性**：EU AI Act 已进入实施阶段（间接推断，[20][21][30]）。
- **低不确定性（较可靠）**：该领域的研究重心已从伦理论辩转向合规工程（可由 [5][27][31] 的出版时间与主题分布直接支持）。

---

## 经典与奠基性工作（相对"近 1–2 年最新进展"的区分）

> 说明：真正的制度性奠基文献（EU AI Act 官方文本、NIST AI RMF、ISO/IEC 42001、OECD AI Principles）**未纳入本次可引证据集**，因此下表**不列**这些条目，以免出现无编号引用。下表仅列本次证据集中**具有范式梳理或长期参考价值**的工作。

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| A multilevel framework for AI governance | 2023 | `> 待核实` | `> 待核实` | arXiv 预印本（v2），未确认同行评审 | 低（无可核引用数据） | ★★★☆☆ | http://arxiv.org/abs/2307.03198v2 | 多层级治理框架，本批证据中**时间最早**的治理框架类工作，可作为"基线"参照 [10] |
| Taxonomy to Regulation: A (Geo)Political Taxonomy for AI Risks and Regulatory Measures in the EU AI Act | 2024 | `> 待核实` | `> 待核实` | arXiv 预印本 | 低 | ★★★☆☆ | http://arxiv.org/abs/2404.11476v1 | 把风险分类学与监管措施挂钩，并指出分类的政治性 [32] |
| Towards AI Accountability Infrastructure: Gaps and Opportunities in AI Audit Tooling | 2024 | `> 待核实` | `> 待核实` | arXiv 预印本（v3） | 低 | ★★★★☆ | http://arxiv.org/abs/2402.17861v3 | 审计工具生态的系统盘点，G2 缺口的原始出处 [22] |
| Towards Assuring EU AI Act Compliance and Adversarial Robustness of LLMs | 2024 | `> 待核实` | `> 待核实` | arXiv 预印本 | 低 | ★★★☆☆ | http://arxiv.org/abs/2410.05306v1 | 较早把法条合规与对抗鲁棒性测试合并讨论 [17] |
| An Overview of the Risk-based Model of AI Governance | 2025 | `> 待核实` | `> 待核实` | arXiv 预印本 | 低 | ★★★★☆ | http://arxiv.org/abs/2507.15299v1 | 风险分级治理范式的综述性梳理，适合作为范式入口 [7] |
| A five-layer framework for AI governance: integrating regulation, standards, and certification | 2025 | `> 待核实` | `> 待核实` | arXiv 预印本（期刊体例） | 低 | ★★★☆☆ | http://arxiv.org/abs/2509.11332v1 | 监管—标准—认证三层衔接的显式建模 [5] |
| General Purpose AI Models with Systemic Risks – Classification and Specific Obligations (Articles 51, 52, 55) | `> 待核实` | `> 待核实` | `> 待核实` | Bloomsbury 法律评注书章（DOI），权威性高于预印本 | 低 | ★★★★☆ | https://doi.org/10.5040/9781509988570.ch-023 | 本批证据中**最接近权威法条释义**的来源 [21] |
| Mapping AI Risk Mitigations: Evidence Scan and Preliminary AI Risk Mitigation Taxonomy | 2025 | `> 待核实` | `> 待核实` | arXiv 预印本 | 低 | ★★★☆☆ | http://arxiv.org/abs/2512.11931v1 | 风险缓解措施分类学，仍标"preliminary"，说明该层未成熟 [12] |
| Competing Visions of Ethical AI: A Case Study of OpenAI | 2026 | `> 待核实` | `> 待核实` | arXiv cs.CY 预印本 | 低 | ★★★☆☆ | http://arxiv.org/abs/2601.16513v1 | 企业伦理话语的实证案例，支撑"话语即治理" [4] |
| AI Alignment and Fiduciary Obligation | 2026 | `> 待核实` | `> 待核实` | arXiv 预印本（v3） | 低 | ★★★☆☆ | http://arxiv.org/abs/2608.02660v3 | 以信义义务（fiduciary duty）为 AI 对齐提供法律抓手，属跨法域思路 [16] |

## 开源项目

> **本批可引证据中不含任何 GitHub 仓库、开源治理工具或模型卡/溯源项目的可核链接**，因此无法按要求的列（stars、维护机构、最近提交）填表。为遵守"不编造"原则，本节仅列出**被作为评测对象或工具性讨论载体**的开源相关线索，并明确其非"治理开源项目"。

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| GPT-OSS-20B（作为红队评测对象） | 2025 | `> 待核实` | `> 待核实`（star 数未获取） | 仅见 arXiv 预印本对其实验描述 [23] | 低 | ★★★☆☆ | http://arxiv.org/abs/2509.17259v1 | 被用于对比模型级与智能体级红队，**本身不是治理工具** |
| 治理类开源工具（模型卡、数据溯源、审计平台） | — | — | `> 待核实` | `> 待核实` | 未知 | — | `> 待核实` | **本次检索未覆盖，需补充 GitHub / HuggingFace 专项检索** |

## 数据集与基准

> **本批证据集中不存在专门的"AI 治理合规评测基准"**。以下仅为与治理间接相关的评测/检测类资源，需明确其**不是合规基准**。

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| NTIRE 2026 Challenge on Robust AI-Generated Image Detection in the Wild | 2026 | `> 待核实`（NTIRE 系列挑战赛） | `> 待核实`（榜单数据未获取） | arXiv 预印本，挑战赛报告体例 | 低 | ★★★☆☆ | http://arxiv.org/abs/2604.11487v1 | 合成内容检测基准，与"内容溯源/透明度义务"间接相关，**非合规基准** [19] |
| 大规模红队幻觉评测（数学任务） | 2024 | `> 待核实` | `> 待核实` | arXiv 预印本 | 低 | ★★★☆☆ | http://arxiv.org/abs/2401.00290v1 | 提供规模化红队的任务设置，可作为红队基准的方法参考 [24] |
| 多样攻击数据集（用于鲁棒红队与安全微调） | 2024 | `> 待核实` | `> 待核实` | arXiv 预印本（v3） | 低 | ★★★☆☆ | http://arxiv.org/abs/2405.18540v3 | 攻击多样性方法，支撑红队可重复性讨论 [26] |
| Sources of Truth: 多平台多语言引文审计 | 2026 | `> 待核实` | `> 待核实` | arXiv 预印本 | 低 | ★★☆☆☆ | http://arxiv.org/abs/2609.00319v1 | 属"审计方法"示范（对 AI 心理健康信息引文做审计），可迁移为合规审计方法参考，**与 AI 治理法规无直接关系** [29] |

---

## 参考来源

[1] Towards an AI Observatory for the Nuclear Sector: A tool for anticipatory governance — http://arxiv.org/abs/2504.12358v1
[2] Faith in AI can narrow the futures individuals consider — http://arxiv.org/abs/2603.28944v2
[3] Foundations of GenIR — http://arxiv.org/abs/2501.02842v1
[4] Competing Visions of Ethical AI: A Case Study of OpenAI — http://arxiv.org/abs/2601.16513v1
[5] A five-layer framework for AI governance: integrating regulation, standards, and certification — http://arxiv.org/abs/2509.11332v1
[6] The New Shape of Search: How Conversational AI Recomposes Information Seeking — http://arxiv.org/abs/2607.04282v3
[7] An Overview of the Risk-based Model of AI Governance — http://arxiv.org/abs/2507.15299v1
[8] Towards The Ultimate Brain: Exploring Scientific Discovery with ChatGPT AI — http://arxiv.org/abs/2308.12400v1
[9] Beyond principlism: Practical strategies for ethical AI use in research practices — http://arxiv.org/abs/2401.15284v6
[10] A multilevel framework for AI governance — http://arxiv.org/abs/2307.03198v2
[11] Need of AI in Modern Education: in the Eyes of Explainable AI (xAI) — http://arxiv.org/abs/2408.00025v3
[12] Mapping AI Risk Mitigations: Evidence Scan and Preliminary AI Risk Mitigation Taxonomy — http://arxiv.org/abs/2512.11931v1
[13] DeBiasMe: De-biasing Human-AI Interactions with Metacognitive AIED (AI in Education) Interventions — http://arxiv.org/abs/2504.16770v1
[14] The Case for ESM3 as a General-Purpose AI Model with Systemic Risk Under the EU AI Act — http://arxiv.org/abs/2605.01611v1
[15] Internal Deployment in the AI Act — http://arxiv.org/abs/2512.05742v4
[16] AI Alignment and Fiduciary Obligation — http://arxiv.org/abs/2608.02660v3
[17] Towards Assuring EU AI Act Compliance and Adversarial Robustness of LLMs — http://arxiv.org/abs/2410.05306v1
[18] The Digital Omnibus and Workers' Rights: Reconfiguring the Conditions for the Exercise and Enforcement of Rights — https://doi.org/10.2139/ssrn.7259040
[19] NTIRE 2026 Challenge on Robust AI-Generated Image Detection in the Wild — http://arxiv.org/abs/2604.11487v1
[20] Post-Market Monitoring for AI Systems: Obligations, Architecture, and Implementation Under the EU AI Act — https://doi.org/10.2139/ssrn.6773119
[21] General Purpose AI Models with Systemic Risks – Classification and Specific Obligations (Articles 51, 52, 55) — https://doi.org/10.5040/9781509988570.ch-023
[22] Towards AI Accountability Infrastructure: Gaps and Opportunities in AI Audit Tooling — http://arxiv.org/abs/2402.17861v3
[23] Mind the Gap: Comparing Model- vs Agentic-Level Red Teaming with Action-Graph Observability on GPT-OSS-20B — http://arxiv.org/abs/2509.17259v1
[24] Red Teaming for Large Language Models At Scale: Tackling Hallucinations on Mathematics Tasks — http://arxiv.org/abs/2401.00290v1
[25] Red Teaming AI Red Teaming — http://arxiv.org/abs/2507.05538v2
[26] Learning diverse attacks on large language models for robust red-teaming and safety tuning — http://arxiv.org/abs/2405.18540v3
[27] Making AI Compliance Evidence Machine-Readable — http://arxiv.org/abs/2604.13767v1
[28] Beyond the Personal Assistant: How Expectations for Enterprise AI in Teamwork Diverged as Generative AI Took Shape, 2023-2025 — http://arxiv.org/abs/2509.10956v2
[29] Sources of Truth: A Multi-Platform, Multilingual Audit of Citations in AI Mental Health Information Queries — http://arxiv.org/abs/2609.00319v1
[30] Mapping Industry Practices to the EU AI Act's GPAI Code of Practice Safety and Security Measures — http://arxiv.org/abs/2504.15181v2
[31] From Obligation to Specification: A Survey on Validating EU AI Act Requirements in RE — http://arxiv.org/abs/2607.21608v1
[32] Taxonomy to Regulation: A (Geo)Political Taxonomy for AI Risks and Regulatory Measures in the EU AI Act — http://arxiv.org/abs/2404.11476v1

---

*Generated by research-bot · topic=`ai-治理与监管政策法规与标准` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`deepseek-v4-flash` · sources=32 · duration=211s · 2026-10-22T22:36:18+00:00*
