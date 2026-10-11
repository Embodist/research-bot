# AI 治理与监管（政策、法规与标准）增量调研快照

**日期（UTC）**：2026-10-11　|　**领域**：AI Governance & Regulation（政策、法规、标准、合规工程）　|　**增量窗口**：2024-01 ～ 2026-10　|　**检索源**：26 条可引用来源（[1]–[26]），其中与 AI 治理主题**强相关 17 条**，弱相关/主题漂移 9 条

> **证据基线说明（务必先读）**：本次检索**未返回任何 citations、GitHub star、下载量或榜单排名数据**，也**未返回可核实的官方政策原文链接**（EU AI Act 条文、NIST AI RMF 官方页面、ISO/IEC 42001 标准页均不在可引用列表内）。因此本报告所有「热度证据」一律标注 `> 待核实`，**不编造任何数字**。文中「关注度」为基于主题相关性、辖区核心程度与是否为该议题主文本的**编辑判断**，非引用计量结果。凡涉及具体法条编号、生效日期、适用范围者，均需回到官方法律文本核对，本报告仅基于 [1]–[26] 的摘要层证据陈述。
> **引用消歧警告**：来源 [15] 与 [16] 同名 `AIR-Bench`，但为两个完全不同的工作（前者为监管风险分类安全基准，后者为音频-语言模型理解基准）。本文只将 [15] 计入本主题证据。

---

## 1. 进展与热点（Progress & Hotspots）

**一句话增量判断**：2024-2026 的主线增量不是"又出了几份原则宣言"，而是治理对象从**应用层**上移到**模型层（GPAI）**，并随之出现三类新研究：合规要求到行业实践的**映射工程**、法律边界的**归类判定**、以及治理研究自身的**方法论反思（监管俘获 / 可复现性 / 测量标准化）**。

**最新进展（2024-2026）**

1. **GPAI 行为准则与行业实践的映射（2025-04）**——把业界既有的安全与安保措施逐一映射到 EU AI Act 的 GPAI Code of Practice 条款，属于"义务—实践"对表工作 [8]。
　权威：arXiv 2504.15181v2，cs 类预印本，未见同行评审信息 ｜ 热度：`> 待核实` ｜ 关注度：高（依据：EU AI Act GPAI 义务是该窗口全球最具约束力的模型级监管文本，此类映射研究是合规落地的直接前置件）｜ 推荐度：★★★★★（对做合规工程最直接可用）[8]
2. **前沿生物基础模型的系统性风险归类争议（2026-05）**——因 EU AI Act 措辞歧义，论文论证 ESM3 一类生物基础模型在多大程度上落入"具系统性风险的通用目的 AI 模型"义务 [6]。这是把**领域基础模型**而非聊天助手纳入监管的判定先例讨论。
　权威：arXiv 2605.01611v1，cs.CY ｜ 热度：`> 待核实` ｜ 关注度：中（依据：属于法律解释型研究，受众窄但直接触及监管边界）｜ 推荐度：★★★★（法律定性方法论有价值）[6]
3. **"内部部署"是否受 AI Act 约束（2025-12）**——讨论企业/公共部门自研自用的 AI 系统是否构成"投放市场/投入使用"，即监管触发点的边界问题 [7]。
　权威：arXiv 2512.05742v4，cs 类 ｜ 热度：`> 待核实` ｜ 关注度：中（依据：所有自建 AI 能力的机构都会遇到此问题）｜ 推荐度：★★★★ [7]
4. **治理研究的元反思三连（2024-10 / 2025-10 / 2025-12）**——① 监管俘获：AI 公司如何"微调"政策 [13]；② 可复现性被提为治理新前沿，直指政策制定者所获信息的信噪比过低会助长监管俘获 [21]；③ 面向前瞻性风险检测的测量标准化框架（"AI 流行病学"）[24]。
　权威：arXiv 2410.13042v1 / 2510.11595v1 / 2512.15783v4 ｜ 热度：`> 待核实` ｜ 关注度：中—高（依据：三者共同指向治理证据基础本身的可信度）｜ 推荐度：★★★★★（[21] 是本批次中"问题定义"最锋利的一篇）[13][21][24]
5. **伦理话语的经验研究（2026-01）**——以 OpenAI 为案例，量化其公开话语中 ethics / safety / alignment 等概念的历史使用变化 [3]；另有 2024 年主张"超越原则主义"、给出研究场景可操作策略的工作 [4]。
　权威：arXiv 2601.16513v1（cs.CY）/ 2401.15284v6 ｜ 热度：`> 待核实` ｜ 关注度：中（依据：[3] 为单机构案例研究，外部效度有限）｜ 推荐度：★★★☆ [3][4]
6. **弱相关召回（明确排除，不计入治理结论）**：AI 预测对人类决策的影响 [1]、GenIR 基础 [2]、教育场景去偏干预 [5]、ChatGPT 科学发现叙事 [9]、教育可解释 AI [10]、对话式搜索 [11]、短视频参与度评测 [12]、对抗文本生成 [18]。这些条目说明本次召回存在**主题漂移**，不应作为治理证据使用；其中 [18] 仅在"信息完整性/对抗操纵"意义上与本主题弱相关。

### 经典与奠基性工作（区别于上述最新进展）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Meaningful human control: actionable properties for AI system development | 2021（据 arXiv 编号推定） | `> 待核实` | `> 待核实` | arXiv 2112.01298v2；未见同行评审信息 | 中（依据：为后续"人类监督"类条款提供可操作化语言） | ★★★★（把"有意义的人类控制"拆成工程属性，是治理话语→系统设计的桥梁） | http://arxiv.org/abs/2112.01298v2 | 对"人类监督"义务的落地建模有价值，但其对 EU AI Act 文本的直接影响 `> 待核实` [14] |
| Actionable Guidance for High-Consequence AI Risk Management: Towards Standards Addressing AI Catastrophic Risks | 2022 | `> 待核实` | `> 待核实` | arXiv 2206.08966v3 | 中（依据：面向灾难性风险的标准建议，属标准层早期奠基） | ★★★★（高后果风险的标准起草参考） | http://arxiv.org/abs/2206.08966v3 | 早于本轮监管浪潮，可作为"标准先行"路线的对照基线 [22] |
| Beyond principlism: Practical strategies for ethical AI use in research practices | 2024（v6 修订时间 `> 待核实`） | `> 待核实` | `> 待核实` | arXiv 2401.15284v6 | 中 | ★★★☆（原则主义批判的代表性表述） | http://arxiv.org/abs/2401.15284v6 | 用于论证"原则宣言→可执行策略"的转向 [4] |
| A five-layer framework for AI governance: integrating regulation, standards, and certification | 2025 | `> 待核实` | `> 待核实` | arXiv 2509.11332v1 | 中 | ★★★★（把法规/标准/认证串成分层骨架，适合作为报告结构参照） | http://arxiv.org/abs/2509.11332v1 | 本报告第 4 节瓶颈分析的重要框架来源 [26] |

> 表中所有年份均据 arXiv 编号前缀（YYMM）推定，**非官方 published 时间**，请以 arXiv 页面为准 `> 待核实`。

---

## 2. 工业界与产品（Industry & Product）

**一句话增量判断**：工业侧的可核证增量集中在**RegTech（监管科技）与企业级合规架构**的早期论文，尚无任何可核实的开源仓库、商用产品或真机/真系统部署证据进入本批来源。

1. **监管文本 → 机器可用的检索与问答（2025-02）**——面向监管文本的混合式信息检索 + 答案生成方法 [17]，是"把法条变成可查询知识库"的基础工作。
　权威：arXiv 2502.16767v1 ｜ 热度：`> 待核实` ｜ 关注度：中（依据：直接服务于合规问答这一刚需场景）｜ 推荐度：★★★★ [17]
2. **受监管保险企业的多智能体合规架构（2026-09）**——在 Solvency II 与 AI Act 双重约束下（奥地利/德国），提出形式化多智能体架构，融合 Arrow 风险汇聚理论与制度设计 [19]。这是本批来源中**唯一明确落到具体行业与具体辖区**的工程框架。
　权威：arXiv 2609.27636v2（q-fin.GN，非计算机类）｜ 热度：`> 待核实` ｜ 关注度：中（依据：跨金融监管与 AI 监管的交叉少数派）｜ 推荐度：★★★★（对受监管行业落地最有参考价值）[19]
3. **ISO/IEC 42001 与监管暴露的量化 ROI 框架（2025-11）**——"风险调整后的智能红利"框架，把 ISO 42001 认证与监管风险敞口纳入投资回报计算 [23]。这是把合规从成本项重构为财务变量的尝试。
　权威：arXiv 2511.21975v1 ｜ 热度：`> 待核实` ｜ 关注度：中 ｜ 推荐度：★★★☆（方法论新颖，但具体参数需核验）[23]
4. **行业级前瞻治理工具：核领域 AI Observatory（2025-04）**——面向核能部门的 AI 观察站，作为**预期性治理（anticipatory governance）**的机构化工具 [20]。
　权威：arXiv 2504.12358v1 ｜ 热度：`> 待核实` ｜ 关注度：中（依据：高后果行业自建治理基础设施的样例）｜ 推荐度：★★★★ [20]

### 开源项目与工程实践

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Regulatory Text Hybrid IR + Answer Generation | 2025 | `> 待核实` | `> 待核实` | arXiv 2502.16767v1 | 中 | ★★★★ | http://arxiv.org/abs/2502.16767v1 | 合规问答的检索侧工程；**是否开源 `> 待核实`** [17] |
| Multi-Agent AI Architecture for Regulated Insurers | 2026 | `> 待核实` | `> 待核实` | arXiv 2609.27636v2 | 中 | ★★★★ | http://arxiv.org/abs/2609.27636v2 | Solvency II + AI Act 双约束架构；**代码开源状态 `> 待核实`** [19] |
| Five-Layer AI Governance Framework | 2025 | `> 待核实` | `> 待核实` | arXiv 2509.11332v1 | 中 | ★★★★ | http://arxiv.org/abs/2509.11332v1 | 法规/标准/认证分层框架；**工具化程度 `> 待核实`** [26] |
| NIST AI RMF / GenAI Profile / ISO/IEC 42001 Alignment | `> 待核实` | `> 待核实` | `> 待核实` | Zenodo DOI（非 arXiv，是否同行评审 `> 待核实`） | 中 | ★★★★ | https://doi.org/10.5281/zenodo.20997139 | 三套标准体系的对齐梳理，是合规映射的实用起点 [25] |

> **缺口声明**：本批来源**未提供任何 GitHub 仓库 URL 或 star 数据**。上表"开源"属性全部为 `> 待核实`，请勿据此认定为已开源项目。

---

## 3. 蓝海与缺口（Blue Ocean & Gaps）

**一句话增量判断**：子问题 q3（数据集与基准）的检索返回**空结果**；本主题的**可比评测层几乎是无人区**——这正是最清晰的高杠杆机会。

### 数据集与基准

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| AIR-Bench 2024: A Safety Benchmark Based on Risk Categories from Regulations and Policies | 2024 | `> 待核实` | `> 待核实` | arXiv 2407.17436v2；未见同行评审信息 | 中（依据：本批来源中唯一"由监管风险分类反推评测维度"的基准） | ★★★★★（治理评测的直接起点） | http://arxiv.org/abs/2407.17436v2 | 注意与 [16] 同名但不同工作 [15] |
| AIR-Bench: Benchmarking Large Audio-Language Models via Generative Comprehension | 2024 | `> 待核实` | `> 待核实` | arXiv 2402.07729v2 | 低（与本主题无关） | ★（仅用于消歧，不建议作为治理证据） | http://arxiv.org/abs/2402.07729v2 | **同名冲突风险**，引用时必须区分 [16] |
| OpenFact at CheckThat! 2024: Adversarial Text Generation | 2024 | `> 待核实` | `> 待核实` | arXiv 2409.02649v2 | 低—中（依据：信息完整性/对抗操纵议题边缘相关） | ★★ | http://arxiv.org/abs/2409.02649v2 | 与 AI 治理的关联需另行论证 [18] |
| AI epidemiology: a measurement standardisation framework for prospective risk detection | 2025 | `> 待核实` | `> 待核实` | arXiv 2512.15783v4 | 中 | ★★★★ | http://arxiv.org/abs/2512.15783v4 | 不是数据集，但提供了**测量标准化框架**，可视为"如何造治理数据集"的方法论缺口填补 [24] |

**三条明确缺口**：

1. **无跨司法辖区可比基准**：仅有基于单一监管体系风险分类构建的 [15]；不同辖区（欧盟/美国/其他）之间**没有可比口径**。`> 待核实` 是否存在此类基准，本批来源无法回答。
2. **无治理工具自身的评测**：[17][19][23][26] 均未报告基于公开榜单的第三方复现结果，也未见基准对比。
3. **"合规可复现性"作为评测维度尚未建立**：[21] 指出政策制定者获得的信息信噪比过低，但本批来源**未见**任何可复现性榜单或审计评测数据集。

---

## 4. 瓶颈与拐点（Bottleneck & Inflection）

**一句话增量判断**：本领域的核心瓶颈不是算法，而是**法律文本的歧义**与**证据链的可复现性**；拐点信号将出现在"标准互认 + 认证披露"规模化之时。

**四个瓶颈**

1. **法律文本歧义 → 归类不确定**：EU AI Act 措辞使"某模型是否属于系统性风险 GPAI"无法机械判定 [6]；"内部部署"是否构成投放市场同样模糊 [7]。
　权威：arXiv 2605.01611v1 / 2512.05742v4 ｜ 热度：`> 待核实` ｜ 关注度：中 ｜ 推荐度：★★★★ [6][7]
2. **信噪比与监管俘获**：政策制定者面对的信息环境信噪比过低，会系统性偏向监管俘获；论文主张以**可复现性**作为治理基础设施 [21]，另一条线经验性刻画了企业如何"微调"政策 [13]。
　权威：arXiv 2510.11595v1 / 2410.13042v1 ｜ 热度：`> 待核实` ｜ 关注度：高（依据：直击治理失效机制而非表层合规）｜ 推荐度：★★★★★ [13][21]
3. **标准互操作**：NIST AI RMF、生成式 AI Profile、ISO/IEC 42001 与 EU AI Act 之间需要对齐层 [25][26]，否则企业面对 N 套并行义务。
　权威：Zenodo DOI [25] / arXiv 2509.11332v1 [26] ｜ 热度：`> 待核实` ｜ 关注度：中—高 ｜ 推荐度：★★★★ [25][26]
4. **测量基础设施缺失**：缺乏面向前瞻性风险检测的标准化测量 [24]，且缺少把合规成本量化进财务模型的共识口径 [23]。
　权威：arXiv 2512.15783v4 / 2511.21975v1 ｜ 热度：`> 待核实` ｜ 关注度：中 ｜ 推荐度：★★★☆ [23][24]

**拐点信号（可观测）**：若在可观察窗口内出现**多个 GPAI 提供方公开披露通过 ISO/IEC 42001 或等效认证的审计报告**，则标准层从"纸面"转入"市场准入凭证"阶段 [P]（依据链：认证—监管暴露—财务回报的量化框架已被提出 [23]，标准对齐层已具备 [25][26]；置信度：中）。

---

## 5. 社会·政策·国际（Society, Policy & Geopolitics）

**一句话增量判断**：本批证据呈现**单极锚定**格局——EU AI Act 是唯一被多篇独立来源反复作为强制约束的文本；美国路径以**标准/框架**（功能性、非强制）形式出现；其他辖区在本次检索中**无任何证据**。

1. **欧盟：强制义务锚点**——GPAI Code of Practice 映射 [8]、系统性风险归类 [6]、内部部署边界 [7]、成员国（奥/德）金融业落地 [19] 均以 AI Act 为轴。
　权威：四篇均为 arXiv 预印本（2504.15181v2 / 2605.01611v1 / 2512.05742v4 / 2609.27636v2）｜ 热度：`> 待核实` ｜ 关注度：高（依据：唯一在本批来源中形成多篇交叉的监管体系）｜ 推荐度：★★★★★ [6][7][8][19]
2. **美国：标准与风险管理路径**——面向高后果风险的标准建议 [22] 与 NIST AI RMF / 生成式 AI Profile / ISO/IEC 42001 的三方对齐 [25] 构成"框架 + 国际标准"路线。
　权威：arXiv 2206.08966v3 [22]；Zenodo DOI（评审状态 `> 待核实`）[25] ｜ 热度：`> 待核实` ｜ 关注度：中—高 ｜ 推荐度：★★★★ [22][25]
3. **其他辖区（中国、英国、日本、加拿大等）**：**本次检索未返回任何可引用来源**。因此本报告**不对其立法进展作任何陈述**。`> 待核实`——需补充各国官方法律文本与监管机构公告后才能比较。
4. **伦理与话语争议 `[Debated]`**：OpenAI 案例研究显示 ethics / safety / alignment 概念在其公开话语中被差异化使用 [3]；同时有研究主张超越原则主义路径 [4]。两种立场并存：一方认为原则话语是治理资源，另一方认为原则主义已失效。本报告不做裁决。`[Debated]` [3][4]
5. **劳动影响、伦理与供应链**：本批来源**无相关证据**。`> 待核实`。

---

## 6. 资本与生态（Capital & Ecosystem）

**一句话增量判断**：可核证的只有**治理失效的经济学**（监管俘获）与**认证经济的萌芽**（ISO 42001 与 ROI 挂钩）；融资额、并购、人才流动数据在本次检索中**完全缺失**。

1. **监管俘获与政策游说**：经验性刻画 AI 企业影响政策的过程 [13]；并指出信息环境低信噪比会加剧俘获 [21]。
　权威：arXiv 2410.13042v1 / 2510.11595v1 ｜ 热度：`> 待核实` ｜ 关注度：高（依据：解释为何"好政策"可能被稀释的机制性证据）｜ 推荐度：★★★★★ [13][21]
2. **认证与审计市场的经济逻辑**：ISO/IEC 42001 与监管暴露被纳入 ROI 量化 [23]；标准—认证分层框架 [26] 与三标准对齐 [25] 共同暗示一个**合规认证服务市场**正在形成。
　权威：arXiv 2511.21975v1 / 2509.11332v1 / Zenodo DOI ｜ 热度：`> 待核实` ｜ 关注度：中 ｜ 推荐度：★★★★ [23][25][26]
3. **受监管行业的采纳压力**：保险业在 Solvency II + AI Act 双重约束下的架构化应对 [19]，显示合规需求已从科技公司外溢到传统金融。
　权威：arXiv 2609.27636v2 ｜ 热度：`> 待核实` ｜ 关注度：中 ｜ 推荐度：★★★★ [19]
4. **投融资 / 并购 / 人才流动 / 社区活跃度**：**本批来源无任何相关证据**，不提供任何估算。`> 待核实`。

---

## 7. 信号与预测（Signals & Forecast）

以下均为 `[P]` 预测，写成可证伪假设，并附依据链、置信度与证伪条件。**不构成事实陈述。**

**信号 S1（早期）**：治理研究正从"提原则"转向"做测量与可复现"——[21] 提出可复现性为治理新前沿，[24] 提出测量标准化框架，[23] 尝试把合规量化进财务模型。三条独立来源同向 `[P]`。[21][23][24]

**假设 H1**：若在 12 个月内（至 2027-10）出现**≥3 篇**独立论文针对同一监管辖区构建**可复现的合规评测基准**（含公开代码与数据），则判定"治理评测层已启动"。
—— 依据链：现有 [15] 已给出"监管风险分类 → 评测维度"的范式，但仅此一例；[24] 提供测量框架但尚未落地为数据集 ｜ 置信度：中 ｜ 证伪条件：至 2027-10 无第三个可复现基准出现。[15][24]

**假设 H2**：若在 18 个月内（至 2028-04）**系统性风险 GPAI 的法律界定**仍未通过官方指南或判例收敛，则"归类不确定性"将持续成为合规成本的主要来源。
—— 依据链：[6] 已展示措辞歧义导致 ESM3 归类需专门论证；[7] 显示"内部部署"边界同样未定 ｜ 置信度：中高 ｜ 证伪条件：官方发布明确的分类判定指南或出现约束性判例。[6][7]

**假设 H3**：标准互认（NIST AI RMF ↔ ISO/IEC 42001 ↔ EU AI Act）在 2027 年前仍以**人工映射文档**而非**机器可执行合规规则**为主。
—— 依据链：[25] 为对齐梳理、[26] 为分层框架，均未提供机器可执行形式；[17] 的监管文本检索问答是最接近自动化的工程尝试，但尚属检索侧 ｜ 置信度：中 ｜ 证伪条件：出现被主要监管机构采纳的机器可读合规规则集。[17][25][26]

**假设 H4（观察项，非预测）**：本主题的**最大无人区是跨辖区可比基准 + 治理工具第三方评测**。若该缺口在 2027 年前被填补，治理研究将从"规范讨论"进入"可测量科学"阶段；否则将持续停留在文档层。

**不确定性声明**：上述置信度均为定性判断，未使用任何量化先验；本次检索**无热度数据**（引用数/star/下载/榜单）支撑，故不对"何者更受关注"做任何排名性断言。所有涉及具体法条、生效日期、官方指南编号的结论，均需对照官方法律文本与监管机构公告核实。`> 待核实`

---

## 参考来源

1. Faith in AI can narrow the futures individuals consider — http://arxiv.org/abs/2603.28944v2
2. Foundations of GenIR — http://arxiv.org/abs/2501.02842v1
3. Competing Visions of Ethical AI: A Case Study of OpenAI — http://arxiv.org/abs/2601.16513v1
4. Beyond principlism: Practical strategies for ethical AI use in research practices — http://arxiv.org/abs/2401.15284v6
5. DeBiasMe: De-biasing Human-AI Interactions with Metacognitive AIED (AI in Education) Interventions — http://arxiv.org/abs/2504.16770v1
6. The Case for ESM3 as a General-Purpose AI Model with Systemic Risk Under the EU AI Act — http://arxiv.org/abs/2605.01611v1
7. Internal Deployment in the AI Act — http://arxiv.org/abs/2512.05742v4
8. Mapping Industry Practices to the EU AI Act's GPAI Code of Practice Safety and Security Measures — http://arxiv.org/abs/2504.15181v2
9. Towards The Ultimate Brain: Exploring Scientific Discovery with ChatGPT AI — http://arxiv.org/abs/2308.12400v1
10. Need of AI in Modern Education: in the Eyes of Explainable AI (xAI) — http://arxiv.org/abs/2408.00025v3
11. The New Shape of Search: How Conversational AI Recomposes Information Seeking — http://arxiv.org/abs/2607.04282v3
12. VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1
13. How Do AI Companies "Fine-Tune" Policy? Examining Regulatory Capture in AI Governance — http://arxiv.org/abs/2410.13042v1
14. Meaningful human control: actionable properties for AI system development — http://arxiv.org/abs/2112.01298v2
15. AIR-Bench 2024: A Safety Benchmark Based on Risk Categories from Regulations and Policies — http://arxiv.org/abs/2407.17436v2
16. AIR-Bench: Benchmarking Large Audio-Language Models via Generative Comprehension — http://arxiv.org/abs/2402.07729v2
17. A Hybrid Approach to Information Retrieval and Answer Generation for Regulatory Texts — http://arxiv.org/abs/2502.16767v1
18. OpenFact at CheckThat! 2024: Combining Multiple Attack Methods for Effective Adversarial Text Generation — http://arxiv.org/abs/2409.02649v2
19. Multi-Agent AI Architecture for Regulated Insurers: A generic AI framework under Solvency II and the AI Act in Austria and Germany — http://arxiv.org/abs/2609.27636v2
20. Towards an AI Observatory for the Nuclear Sector: A tool for anticipatory governance — http://arxiv.org/abs/2504.12358v1
21. Reproducibility: The New Frontier in AI Governance — http://arxiv.org/abs/2510.11595v1
22. Actionable Guidance for High-Consequence AI Risk Management: Towards Standards Addressing AI Catastrophic Risks — http://arxiv.org/abs/2206.08966v3
23. The Risk-Adjusted Intelligence Dividend: A Quantitative Framework for Measuring AI Return on Investment Integrating ISO 42001 and Regulatory Exposure — http://arxiv.org/abs/2511.21975v1
24. Towards AI epidemiology: a measurement standardisation framework for prospective risk detection — http://arxiv.org/abs/2512.15783v4
25. Trustworthy AI Starts Here: Aligning NIST AI RMF, Generative AI Profiles, and ISO/IEC 42001 — https://doi.org/10.5281/zenodo.20997139
26. A five-layer framework for AI governance: integrating regulation, standards, and certification — http://arxiv.org/abs/2509.11332v1

---

*Generated by research-bot · topic=`ai-治理与监管政策法规与标准` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`deepseek-v4-flash` · sources=26 · duration=178s · 2026-10-11T22:22:54+00:00*
