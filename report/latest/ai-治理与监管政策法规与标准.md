# 全球 AI 治理与监管增量调研报告（2024–2026）：从「条文生效」到「可执行合规」

**元信息**：日期 2026-10-20 ｜ 领域：AI 治理与监管（政策、法规、标准）｜ 证据集：29 条候选来源，其中 20 条直接讨论治理/合规/标准，3 条为相邻技术证据（[10][22][28]），6 条与本主题无关已剔除（[5][6][7][12][13][17]，其中 [5] 虽被上游抽取误置于治理子问题，实为人类决策行为实验，不纳入治理增量）｜ 证据分级：A=同行评审/官方标准文本，B=arXiv 预印本/官方仓库，C=第三方复现/榜单，D=社区转述｜ **本报告不含任何未经来源支撑的日期、罚则数额或引用计数**

> **方法论声明（重要）**：本证据集的 20 条相关来源中，**19 条为 arXiv 预印本或 GitHub 仓库，仅 1 条为同行评审会议论文（[29]，IEEE ZINC 2025）**；OECD 三条为官方出版物（[19][20][21]）。因此本报告对「已生效法律义务」的判断**只能间接推断，不能给出条文级生效时间表**——这一缺口在正文中逐处标注 `> 待核实`，而非用模型记忆补齐。凡涉及具体生效日、过渡期、罚则金额、执法案例的表述，一律不写入正文结论。

---

## 1. 进展与热点（Progress & Hotspots）

**一句话增量**：相对 2024 年「要不要立法」的基线，2025–2026 年的研究增量整体迁移到**「义务适用于谁」与「如何证明合规」**两个下游问题；但候选证据中**没有任何官方一手文本**（EUR-Lex、欧委会指南、成员国执法公告），因此「哪些已从提案变为生效义务」在本次证据集内**无法闭环回答**。

### 1.1 增量时间线（按证据可定位时间排序）

| 时间 | 事件/成果 | 类型 | 证据 |
|---|---|---|---|
| 2024 | OECD 更新「AI 系统」定义并发布解释性备忘录 | 官方定义/标准 | [19] |
| 2024 | OECD AI Principles（原则层文本） | 官方原则 | [20] |
| 2024-10 | 面向 EU AI Act 合规保证与 LLM 对抗鲁棒性的研究 | 预印本 | [9] |
| 2024-11 | 可信 AI 的建立与评估：综述与研究挑战 | 预印本 | [18] |
| 2024 | 从「原则主义」转向研究实践中的可操作策略 | 预印本 | [16] |
| 2025-04 | 将产业实践映射到 EU AI Act GPAI Code of Practice 的安全与安保措施 | 预印本 | [2] |
| 2025-11 | 将 ISO 42001 与监管暴露纳入 AI ROI 的量化框架 | 预印本 | [14] |
| 2025 | 用开源库确保高风险 AI 系统符合 EU AI Act | **同行评审会议论文** | [29] |
| 2025-12 | 《AI 法案中的内部部署》v1 提交（v4 于 2026-08 修订） | 预印本（法律分析） | [3] |
| 2025-12 | 可执行治理：把政策翻译为规则 | 预印本 | [26] |
| 2026-01 | OpenAI 伦理/安全话语的量化案例研究 | 预印本 | [1] |
| 2026-02 | International AI Safety Report 2026 | 国际专家评估报告 | [11] |
| 2026-03 | AI 治理控制栈：面向运行稳定性的加固治理 | 预印本 | [24] |
| 2026-04 | 让 AI 合规证据成为机器可读 | 预印本 | [23] |
| 2026-04 | NTIRE 2026 真实场景 AI 生成图像鲁棒检测挑战 | 基准/挑战赛 | [10] |
| 2026-05 | 论证 ESM3 属「具系统性风险的通用目的 AI 模型」 | 预印本（规范主张） | [4] |
| 2026-05 | 可信 agentic AI 综述：安全、鲁棒、隐私与系统安全 | 预印本 | [15] |
| 2026-07 | AI 事件治理的开放问题 | 预印本 | [25] |
| 2026-07 | 工作残疾风险与阿尔茨海默病风险预测中的伦理与 EU AI Act | 预印本 | [8] |
| 2026-08 | 《AI 法案中的内部部署》v4 修订，争议延续 | 预印本（法律分析） | [3] |
| 未标注 | 微软 agent-governance-toolkit 的 `eu-ai-act-checklist.md` | 官方仓库文档 | [27] |

> 时间标注方式：年份/月份取自候选块给出的 arXiv 编号与提交信息；`[27]` 的发布时间在候选块中未给出，`> 待核实`。

### 1.2 三条主线热点

**（1）适用范围之争：从「是否立法」转向「内部部署算不算」**
[3] 是本次证据集中与本问题最贴近的一篇：它以第 2(1)、2(6)、2(8) 条为骨架，论证「内部部署」（in-house deployment）的模型与系统是否落入法案范围，检验以科研与开发例外（2(6)）为基础的抗辩，并把第 3 条定义链（3(1)…3(11)）作为解释支撑。v1 于 2025-12-05 提交、v4 于 2026-08-10 修订，**版本迭代本身即是「争议未定」的可核验信号**。证据强度：B（预印本、单作者备忘录），非官方解释或执法文件。关注度：低（候选块无引用/讨论信号）。

**（2）义务分类学尚未固化：GPAI + 系统性风险的边界**
[4] 指出法案措辞模糊，使「具系统性风险的通用目的 AI 模型」这一类别在**前沿生物基础模型（ESM3）**上是否适用需要专门论证；作者把 ESM3 映射到 biorisk chain 后主张其提供者「宜」受该类义务约束。这是**规范主张（ought）而非已确定的法定归属（is）**，报告在此明确区分。关注度：低。推荐度 ★★★☆☆（说明「门槛未固化」有说服力，但不能当法律结论引用）。

**（3）从「政策脚手架」到「可执行证据」的工程化转向**
这是 2026 年最清晰的一条新增主线，四篇预印本构成互证链条：
- [23] 直接断言 AI Assurance（产出证明符合治理框架所需的**机器可读证据**）「has mature policy scaffolding but lacks the infrastructure to operationalize it」，并点名 EU AI Act、ISO/IEC 42001、NIST AI RMF「specify what to assure but provide no executable form」；
- [26] 提出把政策翻译为规则的「可执行治理」（executable governance）；
- [24] 提出「AI Governance Control Stack」，批评既有方法「focus primarily on policy guidance rather than operational stability mechanisms」，主张维持可审计、可问责的长期运行行为；
- [25] 把议题推进到 **AI 事件治理（incident governance）** 的开放问题层。

四者时间集中在 2025-12 至 2026-07，**构成「问题陈述 → 架构设想 → 议题扩展」的连续增量**，而非孤立观点。关注度：均为低（无引用/star 信号）；推荐度 [23] ★★★★☆、[24] ★★★☆☆、[26] ★★★☆☆、[25] ★★★☆☆。

### 1.3 经典与奠基性工作（相对「最新进展」单列）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| OECD 更新版「AI 系统」定义解释备忘录 | 2024 | OECD（官方） | > 待核实（无引用数） | A：官方出版物 DOI | 中 — OECD 定义为多国立法共同参照系 | ★★★★★ — 定义层是所有下游义务的锚点 | https://doi.org/10.1787/623da898-en | 概念框架的源头文本 [19] |
| OECD Principles on AI | 2024（版本待核实） | OECD（官方） | > 待核实 | A：官方出版物 | 中 — 原则层被广泛引述但难量化 | ★★★★★ — 负责任 AI 原则的基准文本 | https://doi.org/10.1787/6ff2a1c4-en | 原则层奠基 [20] |
| Tools for trustworthy AI | 年份待核实 | OECD（官方） | > 待核实 | A：官方出版物 | 中 — 面向落地工具的政策侧清单 | ★★★★☆ — 连接原则与工具实践 | https://doi.org/10.1787/008232ec-en | 原则→工具桥接 [21] |
| Beyond principlism: Practical strategies for ethical AI use | 2024 | 学术（预印本 v6） | > 待核实 | B：arXiv 预印本 | 低 — 无热度信号 | ★★★☆☆ — 「脱离原则主义」的操作化主张可作演进主线注脚 | http://arxiv.org/abs/2401.15284v6 | 原则主义批判 [16] |
| Establishing and Evaluating Trustworthy AI | 2024-11 | 学术（预印本） | > 待核实 | B：arXiv 预印本 | 低 | ★★★☆☆ — 可信 AI 评估挑战综述 | http://arxiv.org/abs/2411.09973v1 | 评估维度 [18] |
| Internal Deployment in the AI Act | 2025-12 / 2026-08 | 学术（预印本 v4） | > 待核实 | B：预印本，非同行评审 | 低 | ★★★★☆ — 本主题相关性最高的法律分析 | http://arxiv.org/abs/2512.05742v4 | 范围解释 [3] |

> **证据错配提示（须显式纠正）**：上游抽取的 q2（「奠基性文本与学术基础」）四条 findings 实际指向 [5][1][13][14]，其中 [5][13] 与治理主题无关。**本证据集中真正对应「奠基性文本」的只有 [19][20][21] 三条 OECD 官方来源**；NIST AI RMF 与 ISO/IEC 42001 仅在 [14][23] 中被**提及**（作为「有框架但无可执行形式」的对象），**没有任何一手标准文本进入证据集**——故本报告不对 NIST/ISO 条款内容作任何断言，相关描述一律 `> 待核实`。

---

## 2. 工业界与产品（Industry & Product）

**一句话增量**：产业侧出现两类可核验动作——**大厂把合规清单直接写进开源治理仓库**（[27]）与**把标准合规纳入财务决策模型**（[14]）；但真机/生产环境的部署证据、备案流程与水印工具链在候选集中**完全缺失**。

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| agent-governance-toolkit：`eu-ai-act-checklist.md` | 未标注 | Microsoft（官方仓库） | > 待核实（未取 star 数） | B：厂商官方仓库文档 | 中 — 大厂仓库 + 直接面向合规清单，工程侧可即取即用 | ★★★★☆ — 少数可直接落地的产业侧合规工件 | https://github.com/microsoft/agent-governance-toolkit/blob/main/docs/compliance/eu-ai-act-checklist.md | agent 治理工具箱中的法案检查清单 [27] |
| Ensuring Compliance of High-Risk AI Systems with the EU AI Act Using Open Source Libraries | 2025 | IEEE ZINC 2025（同行评审） | > 待核实 | **A：会议论文** | 低-中 — 证据集中唯一同行评审的合规工程论文 | ★★★★★ — 唯一 A 级合规工具链证据，优先精读 | https://doi.org/10.1109/zinc65316.2025.11103517 | 用开源库实现高风险系统合规 [29] |
| Generative AI Toolkit（LLM 应用全生命周期质量框架） | 2024-12 | 学术（预印本） | > 待核实 | B：预印本 | 低 | ★★☆☆☆ — 定位为质量/生命周期框架，非合规定位 | http://arxiv.org/abs/2412.14215v1 | 相邻工具 [28] |
| Docling（开源文档转换工具） | 2025-01 | 学术/开源（预印本） | > 待核实 | B：预印本 + 开源 | 低（本证据集内） | ★★☆☆☆ — 仅作文档流水线组件，与治理无直接关系 | http://arxiv.org/abs/2501.17887v1 | 相邻工具 [22] |

**产业实践与准则的映射已有初步研究**：[2] 把产业实践映射到 EU AI Act GPAI Code of Practice 的安全与安保措施，说明「准则条款 ↔ 企业实际做法」之间已出现对照性研究。但需注意两点限界：① 本证据集仅有标题级信息，**映射覆盖率、样本企业数量、方法均 `> 待核实`**；② 该 Code of Practice 的**法律地位（自愿/强制）在证据集中无来源支撑，`> 待核实`**，因此不能把它归入「已生效义务」或「自愿承诺」任一侧。

**「宣示 vs 义务」的实证切口**：[1] 用结构化语料（区分面向公众与面向学术的沟通）+ 定性编码 + NLP 主题建模，量化 OpenAI 对「ethics/safety/alignment」等概念的使用如何随**时间与受众**变化，结论指向这些概念被用作**框架化话语**而非合规承诺。该研究并声明「For reproducible results, we have released our code」，但候选块中仓库地址被截断为「this https URL」，**无法定位与核实，`> 待核实`**。限界：单公司案例，不可外推到行业整体。

**明确的产业侧证据缺口**：
- 企业实际采用的模型卡（model card）工具、风险评估表单、AI 生成内容标识（水印/元数据）工具：**候选集零覆盖**，采用率、成熟度、可复现性均无实证 → `> 待核实`；
- 中国算法备案/大模型备案的工程实践：**零覆盖**；
- 「从演示到生产」的部署量、客户数、事故率：**零覆盖**。

---

## 3. 蓝海与缺口（Blue Ocean & Gaps）

**一句话增量**：本领域当前最明确的无人区不是「再写一份原则」，而是**合规证据的机器可读格式标准 + 运行时治理的开源实现 + 事件治理的分类法**三者同时缺位——这三条缺口已被 2026 年的文献显式命名，但尚无可核验的公共实现。

| 缺口 | 证据 | 为何是蓝海 | 可核验性 |
|---|---|---|---|
| 合规证据的可执行/可机读格式 | [23] 明确指出 EU AI Act、ISO/IEC 42001、NIST AI RMF「provide no executable form」，AI Assurance 缺 operationalize 的基础设施 | 需求已被法规侧锁定、供给侧尚无标准，属「标准空白 + 强需求」 | B 级问题陈述；无实现证据 |
| 运行时治理/控制栈的开源实现与评测 | [24] 主张治理需从政策指引转向维持「reliable, auditable, and accountable behavior over time」；[26] 提出 policy→rules 的可执行治理 | 现有工作停在概念架构，缺代码、缺 benchmark | B 级；【无 star/采用度信号】`> 待核实` |
| AI 事件治理（incident governance） | [25] 直接以「开放问题」形式提出 | 事件上报、分类、根因分析的治理 schema 尚未成形 | B 级，标题级证据 `> 待核实` |
| 第三方独立审计/榜单 | 候选集内**无任何 benchmark 类治理条目** | 无第三方评测 → 无法区分「自评合规」与「实测合规」 | 缺口本身可核验（候选集为空） |
| 跨辖区比较（美/英/中/日/新） | 候选集几乎全为 EU + OECD 视角 | 「全球」叙事与证据覆盖严重不匹配 | 缺口可核验 |
| 弱势群体与劳动力场景的合规落地 | [8] 以工作残疾风险与阿尔茨海默病风险预测为案例讨论伦理与法案适用 | 高风险场景的「场景化合规」尚缺方法学 | B 级，标题级 |

**数据集与基准（本主题下几近空白）**

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| NTIRE 2026 Challenge on Robust AI-Generated Image Detection in the Wild | 2026-04 | NTIRE 挑战赛（预印本报告） | > 待核实 | B：挑战赛报告 | 低（本证据集内） | ★★★☆☆ — 与「AI 生成内容标识/检测」技术侧相邻，可作标识能力的间接指标 | http://arxiv.org/abs/2604.11487v1 | 相邻技术基准，**非治理合规基准** [10] |
| 治理/合规评测基准 | — | — | — | — | — | — | — | **候选集中不存在**，`> 待核实` |

> 结论：**「合规工具有效性」目前没有公认基准**。任何声称某工具「通过 EU AI Act 合规」的说法，在本证据集内都无法被第三方评测支持。

---

## 4. 瓶颈与拐点（Bottleneck & Inflection）

**一句话增量**：瓶颈已从「政策供给不足」转为**「政策供给过剩而执行形式缺失」**；拐点信号是「policy-as-code / 机器可读证据」从口号进入具体架构提案（2025-12 至 2026-04 集中出现），但尚未出现可验证的实现。

**瓶颈分层**

| 层 | 瓶颈 | 证据 | 强度 |
|---|---|---|---|
| 知识/形式化 | 法规规定「保证什么」，未规定「以什么形式保证」 | [23] | 强（直接陈述） |
| 架构 | 缺运行时控制面，治理止于文档 | [24] | 强 |
| 工具 | 高风险系统合规需靠拼装开源库实现 | [29] | 强（同行评审） |
| 技术保证 | LLM 的对抗鲁棒性与法案合规保证难以同时成立 | [9] | 中（预印本，2024-10，时效偏旧） |
| 分类学 | 「系统性风险 GPAI」边界模糊，连生物基础模型归属都需专文论证 | [4] | 中（规范主张） |
| 评测 | 无 benchmark、无第三方复现、无事故数据 | 候选集空缺 | 强（缺口可核验） |
| 人才/组织 | 治理从「政策团队」转向「平台工程团队」的组织成本 | 无来源 | `> 待核实` |

**拐点信号（三条，按可观测性排序）**
1. **大厂把合规清单放进开源治理仓库**（[27]）——意味着合规知识正在被**代码化、版本化**，而不再只存在于咨询报告；这是「文档合规 → 工程合规」最可观测的迁移。
2. **学术侧从「原则批判」转向「执行架构」**：[16]（2024，批判原则主义）→ [24][26]（2025-12/2026-03，提出执行架构）→ [23]（2026-04，指出证据格式缺口），三年内问题陈述逐级下沉。
3. **agentic 系统进入治理视野**：[15] 对 agentic AI 的安全、鲁棒、隐私与系统安全做综述，意味着治理对象从「模型」扩展到「会自主行动的系統」，将迫使合规证据从静态文档转向运行时日志。`> 待核实`（该综述的具体分类未在证据中展开）。

**反向信号（不宜过度乐观）**：上述拐点信号**全部来自预印本与厂商仓库，无一例来自监管机构执法或第三方评测**。因此现阶段更准确的判断是「**方法学拐点已现，制度拐点未至**」。

---

## 5. 社会·政策·国际（Society, Policy & Geopolitics）

**一句话增量**：国际层面出现一个可核验的**科学评估类公共产品**（[11] International AI Safety Report 2026）与 OECD 定义/原则的持续维护（[19][20][21]）；但**地缘政治竞争、出口管制、供应链、劳动替代**四条线在候选证据中**无显著增量材料**，不做推测。

**（1）定义与原则层的国际公共基础设施**
OECD 在 2024 年更新「AI 系统」定义并配以解释性备忘录（[19]），同时维护 AI Principles（[20]）与面向可信 AI 的工具清单（[21]）。这三条是本证据集内**唯一的官方（A 级）治理文本**，其意义在于：定义层一旦收敛，各国立法的适用对象就获得共同参照，**这是「互操作性」的真正来源，而非宣言式的国际合作声明**。`> 待核实`：三份文件的版本号、更新周期与其被哪些辖区正式采纳，候选块未提供。

**（2）科学评估作为独立信道**
[11] International AI Safety Report 2026（2026-02）代表一种不同于「法规」与「企业承诺」的第三种治理载体：**由科学家群体产出的风险评估**。其治理价值在于为立法者提供可引用的公共事实基础；其局限在于**不产生法律义务**。证据等级：B（预印本载体），但其组织形态具国际公共产品属性。关注度：中（作为年度性国际报告具议程设置能力，但本证据集无引用/下载数据，`> 待核实`）。

**（3）适用范围争议的社会含义：科研豁免与创新空间的张力**
[3] 对 2(6) 科研与开发例外的检验，实质是问：**监管成本由谁承担**——是产品化提供者，还是内部研发团队？这一争议直接决定中小机构与研究机构的合规负担。v1（2025-12）→ v4（2026-08）的持续修订说明该问题在 2026 年仍未被权威解释终结。`> 待核实`：欧委会是否已发布相关指南、是否已有成员国执法表态，候选集**无任何来源**。

**（4）高风险场景中的弱势群体**
[8] 以工作残疾风险预测与阿尔茨海默病风险预测为案例讨论伦理与法案适用，把「高风险」从抽象附件清单落到**就业与健康**两类敏感场景。这提示一条社会影响路径：AI 治理的实质争议将越来越多地出现在**保险、雇佣、医疗筛查**的边界上，而非通用聊天机器人。证据等级 B，标题级，`> 待核实`（其具体结论未展开）。

**（5）明确空白（不做推测）**
- 地缘政治与出口管制对 AI 治理的塑造：**候选集零覆盖**，`> 待核实`；
- 劳动替代与治理的互动：**零覆盖**（[8] 仅涉及风险预测，不涉及劳动政策）；
- 中国、美国联邦/州、英国、日本、新加坡的立法增量：**零覆盖**；
- 标准组织的正式投票、发布与过渡期安排：**零覆盖**。

---

## 6. 资本与生态（Capital & Ecosystem）

**一句话增量**：本周期唯一可核验的生态变化是**「合规开始被当作财务变量」**（[14]）与**「平台厂商进入合规工具供给端」**（[27]）；融资额、并购、人才流动三类硬数据在证据集中**完全缺失**，不做任何数量判断。

| 生态信号 | 证据 | 含义 | 强度 |
|---|---|---|---|
| 把 ISO 42001 与「监管暴露（regulatory exposure）」纳入 AI ROI 量化框架 | [14]（2025-11） | 合规成本/风险被建模为投资回报的一部分，意味着**合规从法务成本项变为财务决策变量** | B（预印本），`> 待核实`：模型假设与校准数据 |
| 微软开源 agent 治理工具箱内置 EU AI Act 检查清单 | [27] | 平台厂商把合规知识产品化，可能形成**事实标准**（de facto standard） | B（官方仓库），star/采用度 `> 待核实` |
| 同行评审会议开始接收「合规 + 开源库」类工程论文 | [29]（IEEE ZINC 2025） | 合规工程获得学术出版通道，是子领域形成的标志 | A |
| 学术预印本成为治理知识主产地 | 20 条相关来源中 19 条为预印本/仓库 | 知识生产快于同行评审，**权威性滞后于时效性** | 可核验（计数） |

**生态结构判断**：当前 AI 治理知识生态呈「**三层不对称**」——标准组织（OECD/ISO/NIST）产出定义但更新慢；学术预印本产出方法但缺评审；厂商仓库产出可执行工件但缺独立验证。三者之间**缺少转换层**（把标准条款转成可测规则、把论文方法转成可审计工具），这恰是 [23][26] 试图填补的位置。

**证据缺口**：投资金额、并购案、创业公司数量、人才流动、社区规模——**零覆盖，全部 `> 待核实`**。本报告拒绝对此给出任何数字。

---

## 7. 信号与预测（Signals & Forecast）

**一句话增量**：2026 年的主导信号是「**治理的工程化**」——不是更多原则，而是把原则编译成规则、把合规编译成证据；但制度侧（执法、认证、审计）尚未跟上，因此未来 6–18 个月最可能出现的是**工具与格式的碎片化竞争**，而非统一合规市场。

### 7.1 早期信号清单

| 编号 | 信号 | 时间 | 证据 | 判读 |
|---|---|---|---|---|
| S1 | 「合规证据机器可读化」被明确命名并指认为基础设施缺口 | 2026-04 | [23] | 强信号：问题被命名是可解的前置条件 |
| S2 | 「可执行治理：政策→规则」提案出现 | 2025-12 | [26] | 中信号：架构层提案，未见实现 |
| S3 | 「治理控制栈」把治理目标从文档改为运行时行为 | 2026-03 | [24] | 中信号：概念框架 |
| S4 | 大厂仓库内置法案检查清单 | 未标注 | [27] | 强信号：可观测的产业动作 |
| S5 | 产业实践被系统映射到 GPAI 行为准则 | 2025-04 | [2] | 中信号：说明准则已具备可对照性 |
| S6 | 事件治理被列为开放问题 | 2026-07 | [25] | 弱-中：议题化阶段 |
| S7 | agentic 系统安全治理综述出现 | 2026-05 | [15] | 中信号：治理对象扩展 |

### 7.2 争议标记

- **[Debated] 内部部署是否受 EU AI Act 约束**：[3] 提供多条解释路径并检验 2(6)/2(8) 抗辩，说明学界内部亦非定论；v1→v4 的修订史支持「未定」判断。官方立场 `> 待核实`。
- **[Debated] 生物基础模型是否属「具系统性风险的 GPAI」**：[4] 明确将其作为**需要论证的规范问题**提出，而非既成事实。
- **[R] 传闻**：本证据集内**无可标记为传闻的条目**（不做填充）。

### 7.3 可证伪预测（[P]，附依据链与置信度）

**[P1] 到 2027-Q2，会出现至少一个被 ≥2 家独立机构采用的开源「合规证据 schema」，可映射到 AI Act 类文档结构。**
- 依据链：S1 命名缺口 [23] → S2 提出政策→规则翻译 [26] → S4 大厂已产出清单 [27] → 三者叠加使 schema 成为最小可行公共品。
- 置信度：**中低**（缺口被命名不等于有人填；无商业激励证据）。
- **证伪条件**：若 2027-06-30 前，GitHub 上不存在被两个及以上互不关联组织（非同一母公司）共同维护、且明确映射监管文档结构的合规证据 schema 项目，则本预测失败。

**[P2] 到 2027-12，「AI 事件治理」将从开放问题清单演进为可操作的分类法或上报 schema（学术或标准草案层面）。**
- 依据链：S6 [25] 已把事件治理议题化；S3/S7 表明治理对象正从静态模型转向运行时系统，事件数据成为必需品。
- 置信度：**中低**。
- **证伪条件**：若 2027-12-31 前无任何公开发布的事件分类法/schema 草案（学术预印本、标准草案或厂商规范均可），则本预测失败。

**[P3] 到 2027-12，「内部部署是否适用」的争议将由官方解释或首例执法/司法表态部分澄清。**
- 依据链：[3] 的持续修订表明解释需求真实存在；法律不确定性通常会以指南或首案收敛。
- 置信度：**中**（制度收敛的一般规律），但**时点高度不确定**。
- **证伪条件**：若 2027-12-31 前仍无欧委会层面指南/行为准则修订或成员国司法/执法表态涉及该问题，则本预测失败。
- 注：本条**不预测任何具体日期或文本编号**，因证据集无官方来源。

**[P4] GPAI 行为准则相关研究将从「实践映射」转向「可审计证据包」。**
- 依据链：S5 [2] 完成映射这一前置步骤 → 映射完成后自然下一步是证据化。
- 置信度：**低**（依赖 [2] 的实际方法细节，而该细节 `> 待核实`）。

### 7.4 观察清单（Watchlist）

1. `[27]` 仓库的后续演进：是否从 checklist 扩展为可执行校验脚本（可比对 commit 历史，`> 待核实`）。
2. `[23][26]` 作者是否发布配套实现或格式规范。
3. `[3]` 是否出现 v5 及之后版本，或其论点是否被官方文件引用。
4. 是否出现**独立的第三方合规评测**（当前为零，一旦出现即为结构性变化）。
5. `[11]` International AI Safety Report 是否形成年度序列并被立法引用。
6. NIST AI RMF / ISO/IEC 42001 的**一手文本**是否进入可核查渠道（本证据集完全缺失，是最优先的补检项）。

---

## 参考来源

[1] Competing Visions of Ethical AI: A Case Study of OpenAI — http://arxiv.org/abs/2601.16513v1
[2] Mapping Industry Practices to the EU AI Act's GPAI Code of Practice Safety and Security Measures — http://arxiv.org/abs/2504.15181v2
[3] Internal Deployment in the AI Act — http://arxiv.org/abs/2512.05742v4
[4] The Case for ESM3 as a General-Purpose AI Model with Systemic Risk Under the EU AI Act — http://arxiv.org/abs/2605.01611v1
[5] Faith in AI can narrow the futures individuals consider — http://arxiv.org/abs/2603.28944v2
[6] Foundations of GenIR — http://arxiv.org/abs/2501.02842v1
[7] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1
[8] Ethics and EU AI Act in Cases of Work Disability Risk and Alzheimer's Disease Risk Prediction — http://arxiv.org/abs/2607.05402v1
[9] Towards Assuring EU AI Act Compliance and Adversarial Robustness of LLMs — http://arxiv.org/abs/2410.05306v1
[10] NTIRE 2026 Challenge on Robust AI-Generated Image Detection in the Wild — http://arxiv.org/abs/2604.11487v1
[11] International AI Safety Report 2026 — http://arxiv.org/abs/2602.21012v1
[12] 图 2临床任务，数据集与常规临床实践中实施人工智能（AI）解决方案的成功之间的关系。 — https://doi.org/10.17816/dd60635-39209
[13] The New Shape of Search: How Conversational AI Recomposes Information Seeking — http://arxiv.org/abs/2607.04282v3
[14] The Risk-Adjusted Intelligence Dividend: A Quantitative Framework for Measuring AI Return on Investment Integrating ISO 42001 and Regulatory Exposure — http://arxiv.org/abs/2511.21975v1
[15] Towards trustworthy agentic AI: a comprehensive survey of safety, robustness, privacy, and system security — http://arxiv.org/abs/2605.23989v1
[16] Beyond principlism: Practical strategies for ethical AI use in research practices — http://arxiv.org/abs/2401.15284v6
[17] Towards The Ultimate Brain: Exploring Scientific Discovery with ChatGPT AI — http://arxiv.org/abs/2308.12400v1
[18] Establishing and Evaluating Trustworthy AI: Overview and Research Challenges — http://arxiv.org/abs/2411.09973v1
[19] Explanatory memorandum on the updated OECD definition of an AI system — https://doi.org/10.1787/623da898-en
[20] What are the OECD Principles on AI? — https://doi.org/10.1787/6ff2a1c4-en
[21] Tools for trustworthy AI — https://doi.org/10.1787/008232ec-en
[22] Docling: An Efficient Open-Source Toolkit for AI-driven Document Conversion — http://arxiv.org/abs/2501.17887v1
[23] Making AI Compliance Evidence Machine-Readable — http://arxiv.org/abs/2604.13767v1
[24] AI Governance Control Stack for Operational Stability: Achieving Hardened Governance in AI Systems — http://arxiv.org/abs/2604.03262v1
[25] Open Problems in AI Incident Governance — http://arxiv.org/abs/2607.05163v1
[26] Executable Governance for AI: Translating Policies into Rules ... - arXiv — https://arxiv.org/html/2512.04408v1
[27] eu-ai-act-checklist.md - agent-governance-toolkit - GitHub — https://github.com/microsoft/agent-governance-toolkit/blob/main/docs/compliance/eu-ai-act-checklist.md
[28] Generative AI Toolkit -- a framework for increasing the quality of LLM-based applications over their whole life cycle — http://arxiv.org/abs/2412.14215v1
[29] Ensuring Compliance of High-Risk AI Systems with the EU AI Act Using Open Source Libraries — https://doi.org/10.1109/zinc65316.2025.11103517

---

*Generated by research-bot · topic=`ai-治理与监管政策法规与标准` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`deepseek-v4-flash` · sources=29 · duration=213s · 2026-10-20T22:34:41+00:00*
