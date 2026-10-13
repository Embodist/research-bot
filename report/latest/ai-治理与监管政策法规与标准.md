# AI 治理与监管：2024–2026 增量快照报告

**日期**：2026-10-13（UTC） | **领域**：AI Governance & Regulation（AI 治理与监管：政策、法规与标准） | **可引用来源**：32 条（[1]–[32]） | **结构化候选发现**：覆盖 q1（法规落地程度）、q2（理论框架与争议）、q3（工程实践与可量化证据）三个子问题

> **证据强度总说明**：本报告全部关键条目来自 arXiv 预印本（B 级）与 1 篇同行评审期刊论文（A 级）。候选块普遍**未提供引用数、GitHub star、下载量或榜单排名**，因此除 [23] 外，所有条目的「热度证据」一律标注 `> 待核实`，不填任何数字。凡候选证据未覆盖的分支（美国联邦行政令、州级立法、中国生成式 AI 管理办法与算法备案、Bletchley/Seoul/Paris 峰会承诺），均明确标为证据缺口而非结论。

---

## 1. 进展与热点（Progress & Hotspots）

> **一句话增量判断**：相对 2023 年"原则宣言"阶段，2024–2026 的增量是**从原则走向可执行义务与合规机制**——但增量集中在欧盟单一辖区，且核心争议（适用范围、系统性风险边界）正在被"压力测试"而非被解决；美国、中国、国际峰会三条分支在本轮证据中完全缺失。

### 1.1 EU AI Act：从条文到义务的落地增量

- **适用范围仍在解释争议中，而非已有明确规则**：2025-12 发布的备忘录对"内部部署（internal deployment）"是否落入 EU AI Act 适用范围进行双向压力测试，并基于第 2(1)、2(6)、2(8) 条为欧委会、AI 提供者/部署者、法院提供多条解释路径 [3]。这本身即证据：该问题尚处"需要解释指引"阶段。
  - 热度：`> 待核实`（候选块无引用/下载数据）｜权威：arXiv cs.CY 预印本（arXiv:2512.05742v4），**未经同行评审**，非欧盟官方解释文件 [3]｜关注度：**低**（候选块无外部热度信号，仅凭主题相关性判断）｜推荐度：**★★★☆☆**（直接对应"条文落地到何种程度"这一问题）[3]
- **GPAI / "具有系统性风险的通用 AI 模型"边界存在扩张主张**：有论文考察前沿生物基础模型（如 ESM3）在多大程度上受"具有系统性风险的 GPAI 模型"义务约束，作者将 ESM3 映射到 biorisk chain 并主张纳入是"可取的（desirable）"——即当前属**解释/主张层面**，尚无定论 [4]。
  - 热度：`> 待核实`｜权威：arXiv cs.CY 预印本（arXiv:2605.01611v1），未经同行评审 [4]｜关注度：**低**（无引用/讨论信号）｜推荐度：**★★★☆☆**（对理解 GPAI 义务边界与潜在扩张有直接价值）[4]
- **自愿守则与硬约束之间的衔接是当前最活跃的工程-政策接口**：一项工作系统映射了**产业实践**与 EU AI Act **GPAI Code of Practice（行为准则）**中的安全与安保（Safety and Security）措施之间的对应关系 [12]。这说明 Code of Practice 已进入"可被逐条对照落地"的阶段，但对照结果本身不等于合规认定。
  - 权威：arXiv 预印本（arXiv:2504.15181v2），未经同行评审 [12]｜热度/关注度：`> 待核实`｜推荐度：**★★★★☆**（理解"自愿承诺 → 可核查措施"转化的关键入口）[12]
- **监管沙盒（Regulatory Sandbox）进入操作化阶段，但面临"能力—协调—吸引力"三重挑战**：针对 AI Act 沙盒的研究指出欧委会提供者参与意愿、成员国主管机关能力与跨机构协调构成核心制约 [11]。
  - 权威：arXiv 预印本（arXiv:2509.05985v1）[11]｜热度/关注度：`> 待核实`｜推荐度：**★★★★☆**（沙盒是"实验室规则 → 真机部署"之间最直接的落地指标）[11]
- **合规保证与对抗鲁棒性被并列处理**：有工作面向"EU AI Act 合规保证 + LLM 对抗鲁棒性"提出方法 [5]。
  - 权威：arXiv 预印本（arXiv:2410.05306v1）[5]｜热度/关注度：`> 待核实`｜推荐度：**★★★☆☆**（把合规与安全鲁棒性统一，是合规工程化的典型路径）[5]
- **配套细分议题已形成专门文献**：AI Act 中的鲁棒性与网络安全条款 [10]、ML 公平性标准化框架 [8]、以及 AI Act 与 DMA 的交叉（生成式 AI 的"bigness"风险）[9] 表明监管正在向技术标准层渗透。
  - 权威：[8][10] 为 arXiv 预印本（[10] arXiv:2502.16184v3；[8] arXiv:2510.01281v1）；[9] 为 arXiv:2308.02033v1（2023 年）[8][9][10]｜热度/关注度：`> 待核实`｜推荐度：**★★★☆☆**（标准与条款级细节，适合作为合规设计依据）[8][9][10]

### 1.2 理论与治理机制的研究增量

- **"原则主义之外"的实操转向**：有工作主张超越 principlism，给出 AI 伦理在研究实践中的可操作策略 [7]——这是"原则导向 → 规则/流程导向"转向的体现。
- **风险基础模型（risk-based model）已成为跨辖区主流范式并被系统批判**：2025 年综述对该范式在欧洲、北美、澳大利亚的政策格局做汇总与批评 [14]，说明该范式已从"新兴"变为"需被审视的默认选项"。
- **治理框架层的整合尝试**：五层治理框架试图连接"监管原则—标准—认证"的断层（现有框架不清楚监管如何转为合格评定机制，导致合规缺口）[13]；风险缓解领域则被诊断出**术语不一致、覆盖有空白**，并给出初步的风险缓解分类学 [15]。
- **新兴治理对象**：机器身份（machine identities / AI agents / API tokens 在企业环境中数量比人类身份超过 80:1）被指为治理盲点，并给出 MIGT 分类学 [17]；AI 治理控制栈（governance control stack）被用于运行稳定性加固 [18]。
  - 权威：均为 arXiv 预印本（[13] arXiv:2509.11332v1；[14] arXiv:2507.15299v1；[15] arXiv:2512.11931v1；[17] arXiv:2604.06148v1；[18] arXiv:2604.03262v1）[13][14][15][17][18]｜热度/关注度：`> 待核实`｜推荐度：[13][14][15] **★★★★☆**（框架层可复用）；[17][18] **★★★☆☆**（企业/地缘边界治理，覆盖面较窄）[13][14][15][17][18]
- **AI 事件治理被明确列为开放问题集合**：2026-07 的工作系统梳理 AI 事件治理的开放问题 [20]。
  - 权威：arXiv 预印本（arXiv:2607.05163v1）[20]｜热度/关注度：`> 待核实`｜推荐度：**★★★★☆**（"事件—报告—问责"闭环是缺口最明确的环节）[20]

### 1.3 经典与奠基性工作（与近 1–2 年进展严格区分）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Accountability in an Algorithmic Society: Relationality, Responsibility, and Robustness in Machine Learning | 2022 | `> 待核实` | `> 待核实` | arXiv 预印本（arXiv:2202.05338v3），未经同行评审 | 低（候选块无热度信号） | ★★★★☆（算法问责的理论奠基，被后续供应链/后果工程文献反复引用为起点） | http://arxiv.org/abs/2202.05338v3 | 提出关系性/责任/鲁棒性三维问责视角，是"问责 ≠ 透明"这一命题的经典来源 [24] |
| Actionable Guidance for High-Consequence AI Risk Management: Towards Standards Addressing AI Catastrophic Risks | 2022 | `> 待核实` | `> 待核实` | arXiv 预印本（arXiv:2206.08966v3） | 低（无热度信号） | ★★★★☆（高后果风险标准化的早期系统化工作） | http://arxiv.org/abs/2206.08966v3 | 为后续 NIST RMF / ISO 42001 类体系提供"可操作指导"模板 [25] |
| AI and the EU Digital Markets Act: Addressing the Risks of Bigness in Generative AI | 2023 | `> 待核实` | `> 待核实` | arXiv 预印本（arXiv:2308.02033v1） | 低（无热度信号） | ★★★☆☆（理解 DMA × GenAI 交叉监管的较早文献） | http://arxiv.org/abs/2308.02033v1 | 把"规模集中风险"引入 AI 监管讨论，早于 AI Act 执行期 [9] |
| Understanding accountability in algorithmic supply chains | 2023 | `> 待核实` | `> 待核实` | arXiv 预印本（arXiv:2304.14749v2） | 低（无热度信号） | ★★★★☆（供应链问责是合规证据链的理论基础） | http://arxiv.org/abs/2304.14749v2 | 将问责从单体模型扩展到多方供应链，直接对应合规证据可追溯问题 [22] |
| Beyond principlism: Practical strategies for ethical AI use in research practices | 2024（v6） | `> 待核实` | `> 待核实` | arXiv 预印本（arXiv:2401.15284v6，多版本更新暗示期刊修回） | 低（无热度信号） | ★★★☆☆（"超越原则主义"的代表性论述） | http://arxiv.org/abs/2401.15284v6 | 标志从原则宣言转向流程性策略 [7] |
| European artificial intelligence "trusted throughout the world": Risk-based regulation and the fashioning of a competitive common AI market | `> 待核实`（2023–2024 区间） | `> 待核实` | `> 待核实` | **同行评审期刊**（*Regulation & Governance*, Wiley，DOI 10.1111/rego.12563）——本报告中唯一 A 级证据 | 低（候选块无热度信号） | ★★★★★（理解 EU"可信 AI × 统一市场"政治经济逻辑的最佳单篇） | https://doi.org/10.1111/rego.12563 | 解释了风险分级监管为何同时是产业政策工具 [23] |
| An Overview of the Risk-based Model of AI Governance | 2025 | `> 待核实` | `> 待核实` | arXiv cs.CY 预印本（arXiv:2507.15299v1） | 低（无热度信号） | ★★★★☆（跨辖区风险范式综述，适合作为分类骨架） | http://arxiv.org/abs/2507.15299v1 | 汇总欧盟/北美/澳洲政策格局并做批判性评述 [14] |

> **热度证据说明**：上表所有"热度/引用数/star"候选块均未提供，按纪律一律 `> 待核实`，未做任何估计。

---

## 2. 工业界与产品（Industry & Product）

> **一句话增量判断**：本周期可见的"产品化"不是模型产品，而是**合规产品**——产业实践开始被逐条映射到 GPAI Code of Practice，第三方评估、保险与合规 ROI 计算成为新出现的商业形态；但**没有任何候选证据显示已出现被独立验证的真机/生产部署数字**。

- **产业实践已被系统映射到 GPAI Code of Practice 的安全与安保措施** [12] ——这是"自愿承诺 → 可核查清单"的产品化接口，也是最接近"行业自评表"的增量。
  - 热度：`> 待核实`｜权威：arXiv 预印本 [12]｜关注度：低（无外部信号）｜推荐度：★★★★☆（企业合规落地的直接参考）[12]
- **合规 ROI 成为可量化商业议题**：有工作提出"Risk-Adjusted Intelligence Dividend"，将 **ISO 42001** 与监管暴露（regulatory exposure）整合进 AI 投资回报的量化框架 [26]。这说明合规成本正在被纳入企业财务模型。
  - 热度：`> 待核实`｜权威：arXiv cs.CY 预印本（arXiv:2511.21975v1）[26]｜关注度：低｜推荐度：★★★☆☆（口径可参考，但框架未经第三方验证 `> 待核实`）[26]
- **受监管行业出现具体落地架构**：面向受监管保险公司（奥地利、德国，需同时满足 **Solvency II** 与 **AI Act**）的多智能体 AI 架构被提出 [29]。这是"双重监管叠加"场景下少见的行业级方案。
  - 热度：`> 待核实`｜权威：arXiv 预印本（arXiv:2609.27636v2，2026-09）[29]｜关注度：低｜推荐度：★★★☆☆（垂直行业合规架构的可迁移样本）[29]
- **监管沙盒的"吸引力"即产业参与意愿指标**：沙盒研究把"提供者是否愿意进入"列为三重挑战之一 [11]，可作为工业界对监管态度的一手间接信号。
- **治理工具化（governance tooling）**：机器身份治理分类学 [17]、AI 治理控制栈 [18]、合规证据机器可读化 [31] 共同构成"治理即软件"的新类别。
  - 权威：[17] arXiv:2604.06148v1；[18] arXiv:2604.03262v1；[31] arXiv:2604.13767v1，均为预印本 [17][18][31]｜热度/关注度：`> 待核实`｜推荐度：★★★☆☆（[31] 机读合规证据最接近可产品化方向）[17][18][31]
- **文档基础设施**：开源文档转换工具 **Docling** 被定位为 AI 驱动的文档转换工具包 [30]，是合规文档流水线的底层组件。
  - 权威：arXiv 预印本（arXiv:2501.17887v1），开源工具包 [30]｜热度：`> 待核实`（未取到 GitHub star）｜关注度：低（依据不足）｜推荐度：★★★☆☆（合规文档解析的实用依赖）[30]

### 2.1 开源项目与工具链

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Docling: An Efficient Open-Source Toolkit for AI-driven Document Conversion | 2025 | `> 待核实` | `> 待核实`（GitHub star 未取到） | arXiv 预印本 + 开源工具包（arXiv:2501.17887v1） | 低（无 star/下载信号） | ★★★☆☆（合规文档 → 结构化证据的通用底座） | http://arxiv.org/abs/2501.17887v1 | 用于把政策/标准/披露文件转为可处理结构 [30] |
| A Toolkit for Compliance, a Toolkit for Justice: Pro-justice EU AI Act Toolkit | 2025 | `> 待核实` | `> 待核实` | arXiv 预印本（arXiv:2505.17165v1） | 低（无热度信号） | ★★★★☆（少见地把"合规工具"与"正义评估"合并，具方法论增量） | http://arxiv.org/abs/2505.17165v1 | 跨部门专家共创的 AI Act 工具包 [32] |
| Towards Assuring EU AI Act Compliance and Adversarial Robustness of LLMs | 2024 | `> 待核实` | `> 待核实` | arXiv 预印本（arXiv:2410.05306v1） | 低（无热度信号） | ★★★☆☆（合规保证与对抗鲁棒性的联合方法） | http://arxiv.org/abs/2410.05306v1 | 是否附带可运行代码 `> 待核实` [5] |
| Competing Visions of Ethical AI: A Case Study of OpenAI（含公开可复现代码） | 2026 | `> 待核实` | `> 待核实` | arXiv cs.CY 预印本（arXiv:2601.16513v1） | 低（无热度信号） | ★★☆☆☆（话语分析工具，量化结论在候选片段中缺失） | http://arxiv.org/abs/2601.16513v1 | 结构化语料 + NLP 方法，作者声明公开可复现代码 [2] |

> **开源合规工具链结论**：候选证据中**没有任何一条提供 GitHub star、fork、Release 或下载量数据**，因此无法判断"NIST AI RMF 工具链、模型卡/系统卡自动化、审计工具"在开源生态中的成熟度——该判断 `> 待核实`。

---

## 3. 蓝海与缺口（Blue Ocean & Gaps）

> **一句话增量判断**：最明确的缺口不是"缺少原则"，而是**缺少可比较的测量口径、事件闭环与责任归属机制**；此外，GPAI 边界的非典型模型（生物基础模型）与"内部部署"两类对象处于规则真空。

- **AI 事件治理（incident governance）被正面列为开放问题集合**——即"事件发生→报告→归因→整改"闭环尚无成熟制度 [20]。这是杠杆最高的空白之一。
- **前瞻性风险探测缺少标准化测量**：有工作提出"AI epidemiology"测量标准化框架，目标是在**不访问模型内部**的前提下，把专家–AI 交互压缩为结构化、可比较字段用于部署中 AI 的风险探测 [28]。
  - 权威：arXiv cs.AI 预印本（arXiv:2512.15783v4）[28]｜热度/关注度：`> 待核实`｜推荐度：★★★★☆（直接指向"可量化治理证据"这一缺口）[28]
- **机器学习公平性的标准化框架仍属提案阶段**：针对新 EU AI Act 的分析同时提出 ML 公平性标准化框架 [8]，说明"公平"尚未进入与鲁棒性/网络安全同等成熟的标准层。
- **规则真空对象一：前沿生物基础模型**。是否属于"具有系统性风险的 GPAI"仍为学术主张 [4]。
- **规则真空对象二：内部部署（internal deployment）**。适用范围存在双向解释路径，尚无官方裁断 [3]。
- **治理盲点：机器身份**。企业环境中机器身份数量远超人类身份（比例超过 80:1），但缺乏整合框架 [17]。
- **风险缓解知识库碎片化**：术语不一致、覆盖有空白，只有初步分类学 [15]；五层框架指出"监管原则 → 合格评定机制"的转化断层 [13]。
- **正义导向的合规工具**仍属罕见：跨部门共创的 pro-justice AI Act Toolkit 是一个早期样本 [32]。
- **国际治理的代表性缺口**：有工作专门讨论"全球多数（Global Majority）在国际 AI 治理中的位置" [19]，暗示现有国际讨论的参与结构存在问题。
  - 权威：arXiv 预印本（arXiv:2601.17191v1）[19]｜热度/关注度：`> 待核实`｜推荐度：★★★★☆（理解国际合法性问题的高相关材料）[19]
- **行业化预见治理**：面向核部门的"AI 天文台（AI Observatory）"被提出作为预见性治理工具 [16]，是"高后果行业 + 持续监测"这一空白方向的代表。
  - 权威：arXiv 预印本（arXiv:2504.12358v1）[16]｜热度/关注度：`> 待核实`｜推荐度：★★★☆☆（跨行业监测机制的模板）[16]

### 3.1 数据集与基准（口径参照）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Mapping AI Risk Mitigations: Evidence Scan and Preliminary AI Risk Mitigation Taxonomy | 2025 | `> 待核实` | `> 待核实` | arXiv 预印本（arXiv:2512.11931v1） | 低（无热度信号） | ★★★★☆（风险缓解措施的术语与覆盖对齐工具） | http://arxiv.org/abs/2512.11931v1 | 证据扫描 + 初步分类学，指出框架碎片化与术语不一致 [15] |
| Towards AI epidemiology: measurement standardisation framework | 2025 | `> 待核实` | `> 待核实` | arXiv cs.AI 预印本（arXiv:2512.15783v4） | 低（无热度信号） | ★★★★☆（部署后风险的可比较测量口径） | http://arxiv.org/abs/2512.15783v4 | 概念论文，定义范围与语义/统计口径 [28] |
| An Analysis of the New EU AI Act and A Proposed Standardization Framework for Machine Learning Fairness | 2025 | `> 待核实` | `> 待核实` | arXiv 预印本（arXiv:2510.01281v1） | 低（无热度信号） | ★★★☆☆（公平性标准化提案） | http://arxiv.org/abs/2510.01281v1 | 将 AI Act 条款与公平性度量对接 [8] |
| The Risk-Adjusted Intelligence Dividend（整合 ISO 42001） | 2025 | `> 待核实` | `> 待核实` | arXiv cs.CY 预印本（arXiv:2511.21975v1） | 低（无热度信号） | ★★★☆☆（合规投入的量化口径参考） | http://arxiv.org/abs/2511.21975v1 | 把监管暴露纳入 ROI 计算 [26] |
| Making AI Compliance Evidence Machine-Readable | 2026 | `> 待核实` | `> 待核实` | arXiv 预印本（arXiv:2604.13767v1） | 低（无热度信号） | ★★★★☆（合规证据机读化，是审计自动化的前置条件） | http://arxiv.org/abs/2604.13767v1 | 直接面向"合规证据可被机器核验" [31] |
| AI Incident Database / AIAAIC / Stanford AI Index / OECD AI Policy Observatory | — | — | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | **本轮候选证据中未出现任何一手材料**，其维度覆盖与统计口径无法核验，需补充检索 |
| NIST AI RMF 及其 Generative AI Profile | — | — | `> 待核实` | `> 待核实`（官方文档未在候选证据中出现） | `> 待核实` | `> 待核实` | `> 待核实` | q3 中提出但未获得一手来源，不得据此下结论 |

> **重要限定**：上表主体是**框架/分类学/方法论**，而非可直接复用的公开数据集或榜单。候选证据中**没有**任何一条提供榜单排名、样本量、任务数等基准口径数据。因此"AI 治理领域已有成熟评测基准"这一判断 `> 待核实`。

---

## 4. 瓶颈与拐点（Bottleneck & Inflection）

> **一句话增量判断**：瓶颈已从"是否要监管"转移到**"监管如何被机器可核查地执行"**；拐点信号是把合规证据转成机读格式、并把沙盒作为试验场——但两条线均未见独立验证。

**瓶颈清单**

1. **术语与框架碎片化**：风险缓解框架术语不一致、覆盖有空白 [15]；"监管原则 → 合格评定机制"转化断层 [13]。
2. **测量口径缺失**：部署中风险的比较性测量尚无标准，现有提案仍为概念论文 [28]。
3. **合规证据不可机读**：合规证明多为自然语言文档，导致自动化审计与跨辖区互认困难 [31]。
4. **技术—法律接口的鲁棒性缺口**：合规保证与对抗鲁棒性需联合处理 [5]；AI Act 中的鲁棒性/网络安全条款如何被技术性验证仍不清晰 [10]。
5. **供应链问责断裂**：模型/数据/部署多方参与时，责任如何沿供应链分配仍是理论难题 [22][24]。
6. **沙盒三重挑战**：主管机关能力（capacity）、跨机构协调（coordination）、对提供者的吸引力（attractiveness）同时受限 [11]。
7. **事件闭环缺失**：事件治理仍是一组开放问题，而非可运行制度 [20]。

**拐点信号（可观测）**

- **信号 A**：产业实践被逐条映射到 GPAI Code of Practice 安全/安保措施 [12] —— 表示自愿守则开始具备"可核验清单"形态。
- **信号 B**：合规证据机读化被明确提出 [31] —— 是审计自动化与监管科技（RegTech）的前置条件。
- **信号 C**：监管沙盒进入操作化讨论（而非原则呼吁）[11]。
- **信号 D**：ISO 42001 进入企业 ROI 计算框架 [26] —— 表示标准开始被当作财务变量而非道德变量。

> **拐点判断**：上述信号均为**单点论文证据**，尚无第三方复现、监管机构采纳记录或部署量数据支撑。是否已越过拐点：`> 待核实`。

---

## 5. 社会·政策·国际（Society, Policy & Geopolitics）

> **一句话增量判断**：欧盟路径的政治经济逻辑（风险分级 × 统一市场 × 全球输出"可信 AI"）已被学术性解释清楚 [23]；但**美国联邦行政令与州级立法、中国生成式 AI 管理办法与算法备案、Bletchley/Seoul/Paris 峰会承诺三条分支在本轮证据中完全缺失**，是本报告最大证据缺口。

- **欧盟：风险分级监管同时是产业政策**。研究指出风险基础监管与"构建有竞争力的共同 AI 市场"之间存在内在耦合——监管设计服务于市场整合与"全球可信"定位 [23]（A 级：同行评审期刊 *Regulation & Governance*）。
  - 热度：`> 待核实`｜权威：**同行评审期刊（Wiley, DOI 10.1111/rego.12563）** [23]｜关注度：低（候选块无引用/讨论信号）｜推荐度：**★★★★★**（唯一 A 级证据，理解欧盟结构性动机不可绕过）[23]
- **国际治理合法性问题**：有工作专论"全球多数（Global Majority）在国际 AI 治理中的处境" [19]，表明国际进程的参与结构与代表性已成独立研究议题。
- **竞争政策与 AI 集中度**：DMA 语境下"生成式 AI 的 bigness 风险"被单独讨论 [9]，指向少数厂商对基础设施与模型的集中控制。
- **高后果行业的预见性治理**：核部门提出建立 AI 天文台作为预见性工具 [16]，反映"关键基础设施 + AI"的治理外溢。
- **人机关系的社会后果有实证增量**：1,305 名参与者的 Newcomb 悖论行为实验显示，**超过 40%** 的参与者把 AI 视为关于自身行为的预测权威，放弃确定收益的几率显著提高 **3.39 倍（95% CI: 2.45–4.70）**，收益减少 **10.7–42.9%**；该效应在不同呈现方式与情境下均出现，且即便预测反复失败仍可检测 [1]。
  - 热度：`> 待核实`（未取到引用数）｜权威：arXiv cs.HC 预印本（arXiv:2603.28944v2, v1 2026-03-30 / v2 2026-07-03），未经同行评审 [1]｜关注度：低（无外部热度信号；数字本身为原文报告口径）｜推荐度：★★★☆☆（为透明度/信任治理提供可量化因果证据）[1]
- **合成关系（synthetic relationships）的纵向研究需求**：有工作讨论用定制 AI 工具开展纵向研究，以理解合成关系的机会与风险 [27]。
  - 权威：arXiv 预印本（arXiv:2412.09086v1）[27]｜热度/关注度：`> 待核实`｜推荐度：★★★☆☆（社会影响维度的方法论文）[27]
- **企业话语与治理话语的关系**：以 OpenAI 为案例的结构化语料 + 定量内容分析刻画其 ethics/safety/alignment 框架演变，作者公开可复现代码；候选片段**未给出量化结果数值** [2]。
  - 热度：`> 待核实`｜权威：arXiv cs.CY 预印本（arXiv:2601.16513v1），未经同行评审 [2]｜关注度：低｜推荐度：★★☆☆☆（仅作"自愿承诺 vs 硬规则"话语分析的背景线索，量化结论 `> 待核实`）[2]

**明确缺口（必须在补充检索后下结论）**

- **美国联邦行政令与州级立法**：本子问题的候选证据**零覆盖**。其是否生效、是否被撤销/替换、可执行性如何：`> 待核实`。
- **中国生成式 AI 管理办法与算法备案**：**零覆盖**。生效状态、覆盖范围、执法案例：`> 待核实`。
- **Bletchley / Seoul / Paris 国际 AI 安全峰会承诺**：**零覆盖**。究竟是自愿承诺还是已转化为国内法或有约束力机制：`> 待核实`。
- 上述三点在 [1]–[4][13][14][15][17] 中均无对应材料，属**检索缺口而非研究结论**。

---

## 6. 资本与生态（Capital & Ecosystem）

> **一句话增量判断**：本周期**没有出现可核验的融资额、并购或人才流动数据**；可见的增量仅为"合规成为企业财务与保险行业架构变量"的间接信号，故本章以揭示证据空白为主。

- **合规被纳入资本回报计算**：ISO 42001 + 监管暴露被整合进 AI 投资回报框架 [26]，说明合规从成本项转为可建模的资本变量。
  - 热度/权威/关注度：`> 待核实`（无引用数、无机构验证）｜推荐度：★★★☆☆（口径参考，非事实数据）[26]
- **受监管行业形成合规工程生态**：保险公司（Solvency II + AI Act 双重约束）出现多智能体架构方案 [29]，意味着合规能力成为垂直行业的准入门槛。
- **沙盒"吸引力"是生态参与指标**：提供者是否愿意进入沙盒，直接反映产业界对监管不确定性的定价 [11]。
- **竞争结构风险已被制度化讨论**：DMA 与 GenAI 的"bigness"议题 [9] 表明市场集中度已进入监管议程，但**无任何份额/融资数据**支持。
- **社区与工具生态**：Docling [30]、pro-justice AI Act Toolkit [32]、合规证据机读化 [31] 构成早期工具生态，但 star/贡献者/下载量全部 `> 待核实`。
- **人才与研究机构分布**：候选证据未提供作者机构信息（多数标 `> 待核实`），无法判断研究力量分布。
- **本周期无显著变化的维度**：投资、并购、人才流动、公司格局变化——**候选证据中无任何一手信号**，不为凑篇幅编造内容。

---

## 7. 信号与预测（Signals & Forecast）

> **一句话增量判断**：当前最强信号是"合规工程化"（机读证据 + 沙盒 + Code of Practice 映射），弱信号是"非典型 GPAI 与内部部署的规则化"。以下预测均写成**可证伪假设**。

**标记约定**：`[P]` 预测（附依据链与置信度）；`[R]` 传闻/未证实；`[Debated]` 争议并存。本报告未引入任何 `[R]` 级传闻——候选证据中不存在未证实的行业爆料。

- **[P1]（置信度：中）到 2027 年 8 月前，若欧盟委员会仍未就"内部部署"是否属于 AI Act 适用范围发布正式解释指引或 FAQ，则"适用范围争议延续未决"成立。**
  - 依据链：2025-12 备忘录仍在提供"多条可能解释路径"而非结论 [3] → 说明无官方裁断 → 推出持续未决。反驳条件：出现欧委会/AI Office 的正式解释文件即推翻。
- **[P2]（置信度：中低）若到 2027 年上半年，GPAI Code of Practice 签署方中**无任何一家**被成员国市场监督机构公开认定不合规，则"自愿守则尚未转化为硬约束"成立。**
  - 依据链：Code of Practice 目前仅被"映射"到产业实践 [12]，且沙盒仍受能力/协调/吸引力三重挑战 [11] → 执行侧承载力不足 → 推出执行案例稀缺。反驳条件：出现首例公开不合规认定即推翻。
- **[P3]（置信度：中）若到 2027 年底，"生物基础模型类 GPAI"（如 ESM3 型）未被欧盟官方明确纳入或明确排除于"系统性风险 GPAI"义务，则该范围仍由学术主张主导 [4]。**
  - 依据链：当前仅有论文主张"可取" [4]，无官方归类 → 推出规则真空延续。反驳条件：欧委会/AI Office 发布归类决定即推翻。
- **[P4]（置信度：中）若到 2027 年底仍无跨辖区统一 AI 事件报告 schema 被任一主要辖区采纳，则"事件治理碎片化"瓶颈延续 [20]。**
  - 依据链：事件治理仍被表述为开放问题集合 [20]，且风险缓解术语本身碎片化 [15] → 推出统一 schema 短期难以落地。反驳条件：任一辖区立法或标准组织采纳统一事件报告格式即推翻。
- **[P5]（置信度：中低）若"合规证据机读格式"被至少一个成员国监管沙盒采纳为正式提交格式，则"合规工程化"拐点成立 [31][11]。**
  - 依据链：机读证据提案已出现 [31] + 沙盒正在操作化 [11] → 二者接口一旦接通即为拐点信号。反驳条件：2027 年底前无任何沙盒采纳机读格式即证伪。
- **[P6]（置信度：低—中）"合规投入可量化"将在 12–18 个月内从框架提案转为可比较数据**：若届时仍未出现公开的、可比较的 AI 合规成本/回报数据集，则 [26] 类框架仅是概念工具。
  - 依据链：ISO 42001 已被纳入 ROI 建模 [26] → 说明需求存在 → 但当前无第三方验证数据。反驳条件：出现公开可比数据集即证实。
- **[Debated] 待并列的争议（本报告仅能标出争点，不能裁断）**：AI Act 适用范围（内部部署）[3]、GPAI 系统性风险边界 [4]、风险基础模型的正当性 [14]、以及领域内公平性标准化路径 [8] —— 双方或多方论证在候选中均有呈现，但**均缺少官方解释文件或第三方裁决**佐证。

**Watchlist（值得持续关注）**

1. 欧盟委员会/AI Office 关于"内部部署"与"系统性风险 GPAI"的正式解释文件（对应 [P1][P3]）[3][4]。
2. GPAI Code of Practice 的首批合规/不合规公开案例（对应 [P2]）[12]。
3. 成员国监管沙盒的实际受理与提交格式要求（对应 [P5]）[11]。
4. AI 事件报告机制的跨辖区标准化进展（对应 [P4]）[20]。
5. AI Incident Database / AIAAIC / Stanford AI Index / OECD AI Policy Observatory 的一手页面与统计口径（本轮 `> 待核实`，需补充检索）。
6. 美国联邦行政令与州级立法、中国生成式 AI 管理办法与算法备案、Bletchley/Seoul/Paris 峰会承诺的落地状态（本轮**零覆盖**，最高优先级补充项）。

---

## 参考来源

[1] Faith in AI can narrow the futures individuals consider — http://arxiv.org/abs/2603.28944v2
[2] Competing Visions of Ethical AI: A Case Study of OpenAI — http://arxiv.org/abs/2601.16513v1
[3] Internal Deployment in the AI Act — http://arxiv.org/abs/2512.05742v4
[4] The Case for ESM3 as a General-Purpose AI Model with Systemic Risk Under the EU AI Act — http://arxiv.org/abs/2605.01611v1
[5] Towards Assuring EU AI Act Compliance and Adversarial Robustness of LLMs — http://arxiv.org/abs/2410.05306v1
[6] Foundations of GenIR — http://arxiv.org/abs/2501.02842v1
[7] Beyond principlism: Practical strategies for ethical AI use in research practices — http://arxiv.org/abs/2401.15284v6
[8] An Analysis of the New EU AI Act and A Proposed Standardization Framework for Machine Learning Fairness — http://arxiv.org/abs/2510.01281v1
[9] AI and the EU Digital Markets Act: Addressing the Risks of Bigness in Generative AI — http://arxiv.org/abs/2308.02033v1
[10] Robustness and Cybersecurity in the EU Artificial Intelligence Act — http://arxiv.org/abs/2502.16184v3
[11] Operationalising AI Regulatory Sandboxes under the EU AI Act: The Triple Challenge of Capacity, Coordination and Attractiveness to Providers — http://arxiv.org/abs/2509.05985v1
[12] Mapping Industry Practices to the EU AI Act's GPAI Code of Practice Safety and Security Measures — http://arxiv.org/abs/2504.15181v2
[13] A five-layer framework for AI governance: integrating regulation, standards, and certification — http://arxiv.org/abs/2509.11332v1
[14] An Overview of the Risk-based Model of AI Governance — http://arxiv.org/abs/2507.15299v1
[15] Mapping AI Risk Mitigations: Evidence Scan and Preliminary AI Risk Mitigation Taxonomy — http://arxiv.org/abs/2512.11931v1
[16] Towards an AI Observatory for the Nuclear Sector: A tool for anticipatory governance — http://arxiv.org/abs/2504.12358v1
[17] Who Governs the Machine? A Machine Identity Governance Taxonomy (MIGT) for AI Systems Operating Across Enterprise and Geopolitical Boundaries — http://arxiv.org/abs/2604.06148v1
[18] AI Governance Control Stack for Operational Stability: Achieving Hardened Governance in AI Systems — http://arxiv.org/abs/2604.03262v1
[19] The Global Majority in International AI Governance — http://arxiv.org/abs/2601.17191v1
[20] Open Problems in AI Incident Governance — http://arxiv.org/abs/2607.05163v1
[21] Generalized Traveling Salesman Problem Reduction Algorithms — http://arxiv.org/abs/0804.0735v2
[22] Understanding accountability in algorithmic supply chains — http://arxiv.org/abs/2304.14749v2
[23] European artificial intelligence "trusted throughout the world": Risk‐based regulation and the fashioning of a competitive common AI market — https://doi.org/10.1111/rego.12563
[24] Accountability in an Algorithmic Society: Relationality, Responsibility, and Robustness in Machine Learning — http://arxiv.org/abs/2202.05338v3
[25] Actionable Guidance for High-Consequence AI Risk Management: Towards Standards Addressing AI Catastrophic Risks — http://arxiv.org/abs/2206.08966v3
[26] The Risk-Adjusted Intelligence Dividend: A Quantitative Framework for Measuring AI Return on Investment Integrating ISO 42001 and Regulatory Exposure — http://arxiv.org/abs/2511.21975v1
[27] Understanding Opportunities and Risks of Synthetic Relationships: Leveraging the Power of Longitudinal Research with Customised AI Tools — http://arxiv.org/abs/2412.09086v1
[28] Towards AI epidemiology: a measurement standardisation framework for prospective risk detection — http://arxiv.org/abs/2512.15783v4
[29] Multi-Agent AI Architecture for Regulated Insurers: A generic AI framework under Solvency II and the AI Act in Austria and Germany — http://arxiv.org/abs/2609.27636v2
[30] Docling: An Efficient Open-Source Toolkit for AI-driven Document Conversion — http://arxiv.org/abs/2501.17887v1
[31] Making AI Compliance Evidence Machine-Readable — http://arxiv.org/abs/2604.13767v1
[32] A Toolkit for Compliance, a Toolkit for Justice: Drawing on Cross-sectoral Expertise to Develop a Pro-justice EU AI Act Toolkit — http://arxiv.org/abs/2505.17165v1

> **来源使用说明**：[6]（Foundations of GenIR）与 [21]（Generalized Traveling Salesman Problem Reduction Algorithms）在候选证据中与本主题无实质关联，本报告未引用，仅保留于编号列表以维持引用编号一致性。

---

*Generated by research-bot · topic=`ai-治理与监管政策法规与标准` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`deepseek-v4-flash` · sources=32 · duration=209s · 2026-10-13T22:34:30+00:00*
