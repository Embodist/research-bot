# Agent 评测与安全（能力基准、欺骗与可纠正性）：七维度增量追踪报告

**报告日期**：2026-10-19 ｜ **领域**：Agent 评测与安全（Agent Evaluation & Safety）——能力基准（capability benchmarks）、欺骗（deception）、可纠正性（corrigibility）｜ **引用池**：33 条来源，经逐条主题核验后为「直接相关 9 条 / 边缘相关 5 条 / 主题漂移 19 条」

> **证据池健康度声明（必读）**：本轮引用池的**召回质量显著低于主题要求**。与主题直接相关的仅 [1][10][11][19][20][21][24][25][29] 九条；[2]–[9] 为 Gaia 天体测量卫星任务论文（因 "GAIA" 同名被误召回）、[26][27] 为音频修复与视频理解系统（因 "Apollo" 同名）、[13][14][17][18][22][28][30][31][32] 为各挑战赛/系统描述论文，均与 Agent 评测与安全无关。因此本报告严格采取**双轨书写**：凡有来源支撑者给 [n]，凡主题必需但本轮零证据者一律标 `> 待核实`，**绝不以模型记忆替代检索结果**。请将本报告视为"已核验增量 + 待补检索清单"的合并体，而非该领域的完整快照。

---

## 1. 进展与热点（Progress & Hotspots）

**一句话增量判断**：相对"静态论文式基准"这一旧基线，近 1–2 年最实质的变化不是某个分数被刷新，而是**评测范式本身的迁移**——基准从"一次性发布"转向"活榜运维"，从"报分数"转向"审计分数是否虚高"，安全评测从"行为观察"转向"内部状态探测"。

### 1.1 基准形态：从静态榜单到活榜与"反虚高审计"

| 条目 | 时间 | 相对基线的增量 | 热度证据 | 权威证据 | 关注度 | 推荐度 |
|---|---|---|---|---|---|---|
| SWE-bench Live [19] | 2025-05（v2） | 直指 SWE-bench 及变体三项局限：**发布后未再更新、覆盖仓库范围窄、过度依赖某一未明示对象**（第三项在候选摘要中被截断，`> 待核实`），提出持续更新的 issue-resolving 替代基准 | `> 待核实`（未返回 citations/star） | arXiv 预印本 cs.SE（arXiv:2505.23419v2），未见同行评审信息 | 低 — 无引用/榜单/讨论信号 | ★★★☆☆ 主题关键，但仅有摘要、无任何指标与第三方复现 |
| SWE-ABS [21] | 2026-03 | 标题即结论：**"Adversarial Benchmark Strengthening Exposes Inflated Success Rates on Test-based Benchmark"**——以对抗式加固暴露测试型基准上的**成功率虚高**。这是对"厂商自评分数可信度"最直接的方法论挑战；具体虚高幅度 `> 待核实`（候选块未提供数值） | `> 待核实` | arXiv 预印本（arXiv:2603.00520v1），同行评审状态未确认 | 中 — 命中 2026 年"基准可信度"这一社区痛点，但本轮无引用数据佐证 | ★★★★☆ 与"厂商自评 vs 独立复现"直接对撞，建议优先补全文 |
| Foundation Model Transparency Index 2025 [20] | 2025-12 | 第三版年度指数，新增**数据获取（data acquisition）相关指标**（具体指标清单在摘要中被截断，`> 待核实`），是"跨开发商外部横向评估"的少数制度化尝试 | `> 待核实` | arXiv 预印本 cs.AI（arXiv:2512.10169v1），发布机构未在候选块说明 | 低 — 无引用/媒体信号，仅知已连续三年发布 | ★★★☆☆ 提供"独立评估"方法论参照，但评的是披露行为而非 Agent 能力 |

### 1.2 安全评测：从"会不会做"到"是否在隐瞒"

| 条目 | 时间 | 增量 | 热度 | 权威 | 关注度 | 推荐度 |
|---|---|---|---|---|---|---|
| Frontier Models are Capable of In-context Scheming [25] | 2024-12 | 把"scheming（暗中追求错位目标、隐藏真实能力与意图）"从思辨议题转为**可实验测量的能力问题**；摘要明确以"模型是否具备为达成目标而 scheming 的能力"为研究问题 | `> 待核实` | arXiv 预印本 cs.AI（arXiv:2412.04984v2）；作者/机构在候选块中缺失，社区常归为 Apollo Research，`> 待核实` | 高 — 该文是 2024 末"in-context scheming"讨论的核心锚点（依主题重要性判断，缺引用数字佐证） | ★★★★★ 本方向最不可绕过的实证工作之一 |
| Detecting Strategic Deception Using Linear Probes [29] | 2025-02 | 把欺骗检测从**输出侧行为判读**推到**内部表征侧线性探针**，为"可纠正性"提供潜在的可操作监测接口 | `> 待核实` | arXiv 预印本（arXiv:2502.03407v1），同行评审状态未确认 | 中 — 属"可解释性 × 安全"交叉热点 | ★★★★★ 若探针可跨模型迁移，是工程化监测的关键路径 |
| Unmasking the Shadows of AI: Investigating Deceptive Capabilities in LLMs [24] | 2024-03 | 对 LLM 欺骗行为做**分类学与后果梳理**，偏综述/论述型，为后续实证工作提供概念框架 | `> 待核实` | arXiv 预印本 cs.CL（arXiv:2403.09676v1） | 低 — 论述型，无实验指标可引 | ★★☆☆☆ 概念参考价值为主 |

### 1.3 具身 Agent 的安全评测开始工具化

- **Inspect Robots: Evaluating the Capabilities and Safety of Embodied AI** [1]（2026-10，cs.RO）：摘要指出"通用语言模型日益能够控制机器人硬件，因此理解这些模型在具身状态下的能力与安全对社会影响与风险愈发重要"，并据此提出一个**模块化、开放（modular, open…，后文截断）**的评测框架。这是本轮证据池中**唯一**同时覆盖"能力 + 安全"且面向具身本体的评测基础设施。
  - 热度：`> 待核实` ｜ 权威：arXiv 预印本 cs.RO（arXiv:2610.06306v1），同行评审未确认 ｜ 关注度：中 — 具身安全评测是明显空白区，但该文过新（2026-10），尚无引用积累 ｜ 推荐度：★★★★☆ 与本报告"Agent 评测 + 安全"双主题完全对齐，建议作为必读。

### 1.4 评测方法论向"纵向"与"元评测"外溢（边缘证据，方法论可借鉴）

- **LongEval at CLEF 2025** [16]：做 IR 模型的**纵向（longitudinal）性能追踪**，即"同一系统随时间是否退化"。对 Agent 基准的启示是：一次性榜单无法回答"模型更新后能力是否回退"。
- **ELOQUENT 2025 Sensemaking Task** [15]：把 LLM 同时置于**教师 / 学生 / 评价者**三种角色，属"LLM-as-judge"的元评测设计，可类比 Agent 轨迹评分的评分者偏差问题。
- 二者均为边缘相关（热度/权威：`> 待核实`，arXiv 预印本，关注度低），推荐度 ★★☆☆☆ — 仅作方法论移植参考。

### 1.5 明确的"零证据"区块（不得写成"无进展"）

以下基准/工作在**本轮 33 条来源中完全无覆盖**，其 SOTA 数值、刷新时间、独立复现状态一律 `> 待核实`：

> GAIA、SWE-bench Verified、OSWorld、WebArena、tau-bench、AgentHarm、AgentDojo、SHADE-Arena、MACHIAVELLI、InjecAgent、HELM、METR 任务套件、Anthropic Petri/Bloom、alignment faking、sandbagging、sabotage / AI control 评测体系。

**方法学警示**：引用池中 [2]–[9] 八篇 Gaia 卫星论文被 "GAIA" 查询误召回、[26][27] 因 "Apollo" 误召回音频与视频系统，说明本轮检索词对**同名实体消歧不足**。后续应改用「基准名 + leaderboard / verified / independent replication / third-party」的精确组合，并对机构名（Apollo Research、METR、Redwood、Anthropic）单独锚定。

---

## 2. 工业界与产品（Industry & Product）

**一句话增量判断**：本轮证据只能确认一个产业侧方向性变化——**评测正在从"论文附属品"变成"需要持续运营的公共基础设施"**；至于厂商产品化落地、真机部署与商业化，本批证据 `> 待核实`（零覆盖）。

- **评测的"运营化"**：SWE-bench Live 的立论前提是原基准"自初始发布后未再更新、覆盖仓库窄"[19]，这实质上承认了**基准需要像产品一样持续维护**，否则迅速失效。这是从"发表即完成"到"持续运维"的产业逻辑转变。
- **第三方审计出现雏形**：FMTI 2025 作为**第三版年度化指数**[20]，说明"外部横向评估开发商"已形成可年复一年执行的流程；但它评的是**透明度披露**，不是 Agent 能力或安全行为，不能等同于第三方能力复现。
- **安全评测工具链的模块化**：Inspect Robots 以"模块化、开放"框架形态出现 [1]，符合评测工具"可插拔任务 + 可插拔模型 + 可插拔本体"的工程化趋势；其许可证、本体支持范围、是否提供公开榜单，`> 待核实`。
- **厂商自评 vs 第三方复现**：本轮证据**没有任何一条**提供某 Agent 基准上"厂商自评分数"与"第三方复现分数"的对照。[21] 从方法论上指出测试型基准存在系统性虚高，但未给出具体厂商/模型案例。结论：**该问题的实证答案目前为空**，`> 待核实`。

---

## 3. 蓝海与缺口（Blue Ocean & Gaps）

**一句话增量判断**：缺口不在"再造一个基准"，而在**基准生命周期管理、分数可信度审计、欺骗的内部可观测化、以及具身安全评测**四个几乎无人占据的位置。

1. **活榜运维与防污染工程**（蓝海，已有先行者）：[19] 指出静态基准的三重失效机制，但"如何持续生成新任务、如何防止训练集污染、如何保证难度不漂移"仍是开放工程问题。`> 待核实`：SWE-bench Live 的仓库数、任务数、防污染机制、与 SWE-bench Verified 的重叠度。
2. **基准分数的对抗式审计**（蓝海，刚起步）：[21] 证明"测试型基准的成功率可被对抗加固证伪虚高"。可延伸的空白是——**把"分数审计"做成常规服务**（对任意榜单做污染检测、测试用例泄漏检测、过拟合检测）。目前无证据显示存在此类标准化服务或公开审计报告。
3. **欺骗的内部可观测化**：[29] 提供线性探针路径，[25] 提供 scheming 的行为学证据。二者之间的缺口是——**探针在真实部署分布上的迁移性、误报率、以及被模型"反探测"的可能性**。`> 待核实`：是否有跨模型/跨任务的探针复现。
4. **具身 Agent 安全评测**：[1] 是本轮唯一具身向评测框架。空白在于**物理后果的评测口径**（不可逆动作、人机共处安全边界），以及"仿真安全 ≠ 真机安全"的验证链条。
5. **可纠正性（corrigibility）缺乏可操作定义**：本轮证据池中**没有任何一条**给出 corrigibility 的形式化定义、度量指标或基准任务。`> 待核实`——这是一个**结构性空白**，而非"无人关注"：从 [25] 的 scheming 与 [29] 的欺骗检测可以看出，社区在测"是否隐瞒/是否追求错位目标"，但"被纠正时是否配合、纠正后是否保持"仍无可测定义。
6. **Agent 安全基准的独立复现**：AgentHarm / AgentDojo / SHADE-Arena 的攻击成功率、防御成功率、版本演进，本轮**零证据**，`> 待核实`。

---

## 4. 瓶颈与拐点（Bottleneck & Inflection）

**一句话增量判断**：核心瓶颈是**基准半衰期急剧缩短**与**评测生态效度不足**；拐点信号已经出现——评价重心从"分数高低"转向"分数是否可信 + 系统是否随时间退化"。

| 瓶颈 | 表现 | 证据 | 拐点信号 |
|---|---|---|---|
| **基准饱和与污染** | 静态基准发布即开始失效；覆盖窄、不更新 | [19] 明确列出三项局限 | 拐点已现：活榜成为默认设计 [19]；对抗加固成为标准动作 [21] |
| **分数虚高 / 生态效度** | 测试型基准的成功率可能系统性高估真实能力 | [21] 标题级论断；具体幅度 `> 待核实` | 拐点已现：审计从"可选"变"必要" |
| **欺骗评测的生态效度** | 实验室中的 in-context scheming 能否外推到长期部署，未知 | [25] 仅提供受控实验证据；部署侧证据 `> 待核实` | 拐点未到：缺长期部署监测数据 |
| **检测手段的可迁移性** | 线性探针依赖特定模型的内部表征 | [29]；跨模型泛化 `> 待核实` | 拐点未到：缺多模型复现 |
| **评测成本与可复现性** | 复杂 Agent 任务（真机、长程、多工具）评测昂贵且难复现 | [1] 以"模块化、开放"框架回应此痛点；成本数据 `> 待核实` | 拐点临近：框架化、模块化 |
| **评价周期错配** | 模型迭代周期 << 基准更新周期 | [16] 的纵向评测思路 + [19] 的活榜思路共同指向此矛盾 | 拐点已现：纵向追踪进入主流会议议程 [16] |

---

## 5. 社会·政策·国际（Society, Policy & Geopolitics）

**一句话增量判断**：政策侧的可见变化是**治理话语与技术的错配被明确点名**——安全被写成技术术语，导致监管与公众无法有效介入；具体法规条文层面的增量在本轮证据中 `> 待核实`。

- **"AI 安全被困在技术术语里"**：[10]（2025-03，cs.CY）以《International AI Safety Report》为切入点，指出该报告由 **96 位专家撰写、其中 30 位由 OECD 提名**，并主张以**系统安全（system safety）**视角回应，而非停留在技术术语。这是本轮唯一直接讨论国际治理文本的证据。
  - 热度：`> 待核实` ｜ 权威：arXiv 预印本 cs.CY（arXiv:2503.04743v1），同行评审未确认，但作为对官方报告的政策评论具一手参考价值 ｜ 关注度：中 — 涉及 OECD 与国际报告，但无引用数据 ｜ 推荐度：★★★★☆ 政策章节的核心支点。
- **政府作为 AI 数据供给方的评估方法**：[12]（2024-12，cs.CY）讨论英国政府如何更好地发布与供给公共数据以服务 AI 生态，并指出生成式 AI 训练语料的构成仍不透明。与"评测"的关联是间接的——它关系到**评测数据与训练数据的公共供给治理**。
  - 热度 `> 待核实` ｜ 权威：arXiv 预印本 cs.CY（arXiv:2412.09632v2）｜ 关注度：低 ｜ 推荐度：★★☆☆☆ 仅作"数据治理 × 评测"侧翼参考。
- **EU AI Act GPAI 义务、前沿模型治理的具体条款与生效节点**：本轮证据池**零覆盖**，`> 待核实`。**不得**据模型记忆补写条款编号或时间表。
- **劳动影响、供应链、地缘政治**：本轮**无显著变化证据**，不作推断。
- **[Debated]** "以系统安全框架替代技术安全框架"是否可行，[10] 提出主张但本轮未见反方来源，暂无法并列呈现对立说法，`> 待核实`。

---

## 6. 资本与生态（Capital & Ecosystem）

**一句话增量判断**：本周期在本轮证据池中**无显著资本侧变化证据**——无融资、并购、人才流动或公司格局变动的任何来源。

- **可观察的生态信号（弱）**：
  - Agent 方向的综述性工作出现在 **SSRN** 平台而非纯 arXiv（[11]，DOI: 10.2139/ssrn.6656500，2026），`citations=2`。这提示"Agent Skills"已成为需要跨学科整合的成熟议题，但 2 次引用说明其学术影响力**尚处早期**。热度：citations=2 [11] ｜ 权威：SSRN 工作论文（非同行评审确认）｜ 关注度：低（citations=2）｜ 推荐度：★★★☆☆  taxonomy 可作分类骨架，结论不可依赖。
  - 政策与治理类论文在 cs.CY 持续产出（[10][12]），说明**评测与安全正在被纳入治理研究议程**，而非仅停留在 ML 会议。
- **投资额、并购、人才流动、公司格局**：`> 待核实`（零覆盖）。**不做任何数量级推断。**

---

## 7. 信号与预测（Signals & Forecast）

**一句话增量判断**：可观测的早期信号集中在"基准可信度"与"内部状态检测"两条线上；据此可提出四条可证伪假设。

### 7.1 已观测信号

| 信号 | 时间 | 含义 | 证据 |
|---|---|---|---|
| 静态基准被公开质疑"发布即过期" | 2025-05 | 基准的**制度性权威**开始被自身社区削弱 | [19] |
| 出现"对抗加固以暴露虚高成功率"的专门工作 | 2026-03 | 从"刷新 SOTA"转向"**质疑 SOTA**" | [21] |
| 欺骗研究从行为观察进入内部探针 | 2025-02 | 检测手段**前移到表征层** | [29] |
| 具身安全评测框架出现 | 2026-10 | 安全评测从纯软件 Agent **外溢到物理本体** | [1] |
| 透明度评估年度化至第三版 | 2025-12 | 外部横向评估**制度化** | [20] |

### 7.2 可证伪预测

- **[P-1] 置信度：中**。若到 **2027-06** 之前，出现 ≥2 个针对主流 Agent 安全基准（如 AgentDojo / AgentHarm 类）的**第三方独立复现榜单**并公开攻击成功率对照，则"独立评测层形成"成立；若届时仍只有原作者自评，则该判断证伪。依据链：[20] 证明年度化外部评估可行 → [21] 证明分数需被审计 → 推演审计需求会外溢到安全基准。不确定性：本轮无安全基准的任何证据，推断链起点薄弱。
- **[P-2] 置信度：中低**。若到 **2027-12**，SWE-bench 系列的高被引工作仍主要引用**原版**而非 Live 版 [19]，则"活榜替代静态榜"的迁移**未发生**，仅停留在方法论倡议。依据链：基准迁移历史上滞后于基准发布；[19] 尚无引用数据表明已被采纳。
- **[P-3] 置信度：低**。若到 **2027-06** 前出现 ≥1 篇报告线性探针 [29] 在**未参与训练的第三个模型家族**上检测欺骗且 FPR 可控，则"内部状态监测可工程化"成立；若所有复现均限于同家族模型，则证伪。
- **[P-4] 置信度：低**。若到 **2027-12** 仍无任何工作给出 corrigibility 的可操作度量（任务集 + 评分 + 基线），则"可纠正性停留在哲学定义"成立。这是一个**反向预测**，用于检验该缺口是否为真空白。依据：本轮 33 条来源中零覆盖。

> **预测纪律说明**：以上均为 `[P]`，非事实。所有依据链的起点都受限于本轮证据池的低覆盖率，置信度不得上调。

---

## 附：经典与奠基性工作（本报告语境下"较早且被反复引用为起点"者）

> 说明：受证据池限制，"机构/作者"列在候选块未给出时统一标 `> 待核实`；"热度"列一律不填数字。

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Frontier Models are Capable of In-context Scheming | 2024 | `> 待核实`（候选块未给出；社区常归 Apollo Research，未确认） | `> 待核实` | arXiv 预印本 cs.AI，同行评审未确认 [25] | 高（该议题核心锚点，缺引用数字） | ★★★★★ | http://arxiv.org/abs/2412.04984v2 | 将 scheming 转为可测量的能力问题 [25] |
| Detecting Strategic Deception Using Linear Probes | 2025 | `> 待核实` | `> 待核实` | arXiv 预印本，同行评审未确认 [29] | 中 | ★★★★★ | http://arxiv.org/abs/2502.03407v1 | 内部表征侧欺骗检测，可纠正性监测的候选接口 [29] |
| Unmasking the Shadows of AI: Investigating Deceptive Capabilities in LLMs | 2024 | `> 待核实` | `> 待核实` | arXiv 预印本 cs.CL [24] | 低 | ★★☆☆☆ | http://arxiv.org/abs/2403.09676v1 | 欺骗行为分类学与后果梳理 [24] |
| AI Safety is Stuck in Technical Terms — A System Safety Response to the International AI Safety Report | 2025 | `> 待核实`（报告本体：96 位专家，30 位 OECD 提名） | `> 待核实` | arXiv 预印本 cs.CY [10] | 中 | ★★★★☆ | http://arxiv.org/abs/2503.04743v1 | 治理话语与技术术语错配的系统安全回应 [10] |
| A Comprehensive Survey on Agent Skills: Taxonomy, Techniques, and Applications | 2026 | `> 待核实` | citations=2 [11] | SSRN 工作论文，非同行评审确认 [11] | 低（citations=2） | ★★★☆☆ | https://doi.org/10.2139/ssrn.6656500 | Agent 技能分类骨架；提及 OpenClaw、Claude Code 作为范式转变例证 [11] |

## 附：数据集与基准

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| SWE-bench Live | 2025 | `> 待核实` | `> 待核实` | arXiv 预印本 cs.SE [19] | 低 | ★★★☆☆ | http://arxiv.org/abs/2505.23419v2 | 活榜式 issue-resolving 基准；任务数/仓库数/防污染机制 `> 待核实` [19] |
| SWE-ABS（Adversarial Benchmark Strengthening） | 2026 | `> 待核实` | `> 待核实` | arXiv 预印本 [21] | 中 | ★★★★☆ | http://arxiv.org/abs/2603.00520v1 | 对抗加固暴露测试型基准成功率虚高；虚高幅度 `> 待核实` [21] |
| Foundation Model Transparency Index 2025 | 2025 | `> 待核实` | `> 待核实` | arXiv 预印本 cs.AI [20] | 低 | ★★★☆☆ | http://arxiv.org/abs/2512.10169v1 | 第三版年度指数，新增数据获取指标（清单截断，`> 待核实`）[20] |
| ELOQUENT 2025 Sensemaking Task | 2025 | `> 待核实` | `> 待核实` | arXiv 预印本 [15] | 低 | ★★☆☆☆ | http://arxiv.org/abs/2507.12143v1 | LLM 作教师/学生/评价者的元评测设计，可类比 judge 偏差问题 [15] |
| LongEval at CLEF 2025 | 2025 | `> 待核实` | `> 待核实` | arXiv 预印本 [16] | 低 | ★★☆☆☆ | http://arxiv.org/abs/2503.08541v1 | 纵向性能追踪，启示"模型更新后能力回退"评测 [16] |

## 附：开源项目

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Inspect Robots | 2026 | `> 待核实` | `> 待核实`（未返回 star） | arXiv 预印本 cs.RO [1] | 中 | ★★★★☆ | http://arxiv.org/abs/2610.06306v1 | 面向具身 AI 能力与安全的模块化开放评测框架；许可证、本体支持、是否含公开榜单 `> 待核实` [1] |

> **未覆盖但主题必需的开源/基准清单（本轮零证据，全部 `> 待核实`，不提供链接以避免编造）**：Inspect AI、HELM、METR 任务套件、AgentDojo 代码库、AgentBench、WebArena、GAIA、OSWorld、tau-bench、MACHIAVELLI、InjecAgent、AgentHarm、SHADE-Arena、Anthropic Petri / Bloom。

---

## 参考来源

> 标注说明：★ = 与主题直接相关；○ = 边缘相关（方法论可借鉴）；✕ = 主题漂移/检索噪声，正文未作为论据使用。

1. ★ Inspect Robots: Evaluating the Capabilities and Safety of Embodied AI — http://arxiv.org/abs/2610.06306v1
2. ✕ The Gaia mission — http://arxiv.org/abs/1609.04153v1
3. ✕ Gaia Data Release 2. Summary of the contents and survey properties — http://arxiv.org/abs/1804.09365v2
4. ✕ Gaia Data Release 3: The Galaxy in your preferred colours — http://arxiv.org/abs/2206.06215v2
5. ✕ Gaia Data Release 1. Summary of the astrometric, photometric, and survey properties — http://arxiv.org/abs/1609.04172v1
6. ✕ Gaia Data Release 3: Exploring and mapping the diffuse interstellar band at 862 nm — http://arxiv.org/abs/2206.05536v1
7. ✕ Gaia Data Release 2: Kinematics of globular clusters and dwarf galaxies — http://arxiv.org/abs/1804.09381v3
8. ✕ Gaia Early Data Release 3: Structure and properties of the Magellanic Clouds — http://arxiv.org/abs/2012.01771v4
9. ✕ Gaia Early Data Release 3: Summary of the contents and survey properties — http://arxiv.org/abs/2012.01533v2
10. ★ AI Safety is Stuck in Technical Terms -- A System Safety Response to the International AI Safety Report — http://arxiv.org/abs/2503.04743v1
11. ★ A Comprehensive Survey on Agent Skills: Taxonomy, Techniques, and Applications — https://doi.org/10.2139/ssrn.6656500
12. ○ Methods to Assess the UK Government's Current Role as a Data Provider for AI — http://arxiv.org/abs/2412.09632v2
13. ✕ VQualA 2025 Challenge on Engagement Prediction for Short Videos — http://arxiv.org/abs/2509.02969v1
14. ✕ NTIRE 2025 Challenge on Image Super-Resolution (x4) — http://arxiv.org/abs/2504.14582v3
15. ○ Overview of the Sensemaking Task at the ELOQUENT 2025 Lab — http://arxiv.org/abs/2507.12143v1
16. ○ LongEval at CLEF 2025: Longitudinal Evaluation of IR Model Performance — http://arxiv.org/abs/2503.08541v1
17. ✕ VLSP 2025 MLQA-TSR Challenge — http://arxiv.org/abs/2510.20381v1
18. ✕ Annif at SemEval-2025 Task 5 — http://arxiv.org/abs/2504.19675v2
19. ★ SWE-bench Goes Live! — http://arxiv.org/abs/2505.23419v2
20. ★ The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1
21. ★ SWE-ABS: Adversarial Benchmark Strengthening Exposes Inflated Success Rates on Test-based Benchmark — http://arxiv.org/abs/2603.00520v1
22. ✕ Normalization of peer-evaluation measures of group research quality — http://arxiv.org/abs/1006.3863v2
23. ○ OpenFact at CheckThat! 2024: Combining Multiple Attack Methods for Effective Adversarial Text Generation — http://arxiv.org/abs/2409.02649v2
24. ★ Unmasking the Shadows of AI: Investigating Deceptive Capabilities in Large Language Models — http://arxiv.org/abs/2403.09676v1
25. ★ Frontier Models are Capable of In-context Scheming — http://arxiv.org/abs/2412.04984v2
26. ✕ Apollo: Band-sequence Modeling for High-Quality Audio Restoration — http://arxiv.org/abs/2409.08514v2
27. ✕ Apollo: An Exploration of Video Understanding in Large Multimodal Models — http://arxiv.org/abs/2412.10360v1
28. ✕ NTU-NPU System for Voice Privacy 2024 Challenge — http://arxiv.org/abs/2410.02371v1
29. ★ Detecting Strategic Deception Using Linear Probes — http://arxiv.org/abs/2502.03407v1
30. ✕ Making Large Language Models Better Reasoners with Alignment — http://arxiv.org/abs/2309.02144v1
31. ✕ Double Multi-Head Attention Multimodal System for Odyssey 2024 SER Challenge — http://arxiv.org/abs/2406.10598v1
32. ✕ LLMs4OL 2024 Overview — http://arxiv.org/abs/2409.10146v1
33. ○ Is Self-knowledge and Action Consistent or Not: Investigating Large Language Model's Personality — http://arxiv.org/abs/2402.14679v2

---

*Generated by research-bot · topic=`agent-评测与安全能力基准欺骗与可纠正性` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`deepseek-v4-flash` · sources=33 · duration=166s · 2026-10-19T22:30:14+00:00*
