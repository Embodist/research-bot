# AI 治理与监管（政策、法规与标准）增量追踪调研报告

**日期**：2026-11-04 | **领域**：AI Governance & Regulation | **检索源数量**：32 条（arXiv 预印本、技术报告、共识文件等）

---

## 1. 进展与热点

### 1.1 EU AI Act 合规落地工程化为核心热点
- **合规检查工具实证评估**：首批系统性评估现有 EU AI Act 合规检查工具，揭示中小企业与开发者面临工具可用性缺口 [28]。
- **机器可读合规证据架构**：提出基于 OSCAL（Open Security Controls Assessment Language）的三层 Compliance-as-Code 架构，覆盖 EU AI Act、ISO/IEC 42001、NIST AI RMF 三大框架，定义 16 个属性扩展实现互操作 [27]。
- **监管沙箱运行化挑战**：实证分析成员国建立国家级 AI 监管沙箱面临的“三重挑战”——能力约束、协调缺口、提供方吸引力不足 [29]。
- **生成式 AI 辅助合规**：探讨生成式 AI 在自动驾驶感知等安全关键场景下支持 EU AI Act 合规的潜力 [30]。
- **对抗鲁棒性与合规联动**：针对 LLM 的 EU AI Act 合规性与对抗鲁棒性联合保障方法 [25]。

> **热度证据**：arXiv 2025-2026 年密集涌现 5+ 篇聚焦 EU AI Act 落地的预印本 [25, 27, 28, 29, 30]。
> **权威证据**：均为 arXiv 预印本（cs.CY, cs.AI, cs.CR），未经同行评审 [27, 28, 29]。
> **关注度**：高 | 依据：EU AI Act 为全球首部综合性 AI 法规，合规工程化为当前核心增量。
> **推荐度**：★★★★☆ | 理由：直接对应“核心法规落地最新进展”，虽为预印本但紧扣实施细节。

### 1.2 运行层治理框架新提案涌现
- **OADA 框架**：提出 Operational AI Deployment Assurance，强调治理状态编排、阈值敏感部署条件下的整改进展与升级机制，填补“静态指标上报”到“部署就绪直接治理”空白 [14]。
- **五层治理框架**：将高层监管原则、标准、认证机制整合为结构化层级，解决“法规到合规落地”转化鸿沟 [15]。
- **Governance Control Stack**：针对高风险决策环境，从策略指导转向运行稳定性机制，关注可审计性与长期问责 [16]。
- **多层级治理框架 (2023)**：较早提出多层级治理结构，为后续五层框架提供理论基座 [13]。

> **热度证据**：4 篇 2025-2026 年预印本集中提出运行层框架 [13, 14, 15, 16]。
> **权威证据**：arXiv 预印本（cs.AI, cs.CY），无同行评审 [14, 15, 16]。
> **关注度**：中 | 依据：新预印本，无独立复现/榜单验证，但填补了运行保障视角空白。
> **推荐度**：★★★☆☆ | 理由：为高风险部署运行保障提供新视角，适合跟踪后续发展。

### 1.3 国际共识与专用领域治理推进
- **新加坡共识**：发布全球 AI 安全研究优先级共识，汇聚国际专家意见 [7]。
- **核能领域 AI 观测站**：提出面向核能领域的前瞻性治理工具 [21]。
- **临床决策治理失效分析**：实证揭示全球 AI 治理框架在临床决策点失效，呼吁非洲本土化方案 [22]。
- **企业级治理对象重构**：概念视角重新审视企业 AI 决策系统的治理对象 [23]。

> **热度证据**：跨领域共识文件与专用领域治理论文 2024-2025 年出现 [7, 21, 22, 23]。
> **权威证据**：arXiv 预印本、SSRN 工作论文、共识文件 [7, 21, 22, 23]。
> **关注度**：中 | 依据：共识文件具参考性，专用领域治理为增量方向。
> **推荐度**：★★★☆☆ | 理由：展示治理向垂直领域、全球南方延伸的趋势。

### 1.4 人机交互实证对治理的启示
- **AI 预测权威信任实验**：1,305 人实验发现超 40% 参与者视 AI 为个人行为预测权威，导致放弃确定性奖励，收益下降 10.7-42.9%，揭示“人在环”治理面临自动化偏见风险 [2]。

> **热度证据**：arXiv:2603.28944v2 (cs.HC)，大样本行为实验 [2]。
> **权威证据**：arXiv 预印本，实证方法严谨 [2]。
> **关注度**：中 | 依据：为治理机制设计提供行为学证据。
> **推荐度**：★★★☆☆ | 理由：量化了“过度信任 AI”对人类监督有效性的侵蚀。

---

## 2. 工业界与产品

### 2.1 合规工具链雏形与认证框架
- **EU AI Act 合规检查器生态**：实证研究显示现有工具多为原型，中小企业适用性差，工程化产品尚缺 [28]。
- **UG AIMS 非洲认证框架**：提出可扩展的 AI 治理与认证框架，面向非洲语境工程落地 [20]。
- **生成式 AI 全生命周期工具包**：聚焦 LLM 应用质量提升的工程工具包，含合规相关模块 [6]。
- **Docling 文档转换工具**：开源文档处理工具链，可支持合规文档自动化 [5]。

> **热度证据**：合规检查器研究 [28]、非洲认证框架 [20]、通用工具包 [5, 6] 均为 2024-2026 年产出。
> **权威证据**：arXiv 预印本、Zenodo 存档、GitHub 开源项目 [5, 6, 20, 28]。
> **关注度**：中 | 依据：合规工具链处于早期原型阶段，尚无成熟商业产品广泛采用。
> **推荐度**：★★★☆☆ | 理由：反映工业界从“文档合规”向“工具化合规”过渡的早期信号。

> 待核实：主流红队测试框架（如 Garak, PyRIT）、模型卡/数据卡标准化库（如 Hugging Face Model Cards, Data Cards Playbook）的最新版本与采用情况，提供的证据源未覆盖 [q3 findings]。

---

## 3. 蓝海与缺口

| 缺口领域 | 具体描述 | 证据来源 | 优先级 |
|----------|----------|----------|--------|
| 跨司法管辖区互操作 | EU AI Act、NIST AI RMF、ISO 42001、中国算法备案等框架缺乏统一技术标准与互认机制 | [27, q1] | 高 |
| 机器可读合规证据标准 | OSCAL 扩展等交换格式尚未形成行业共识或官方采纳 | [27] | 高 |
| 监管沙箱能力建设 | 成员国层面能力不足、跨境协调缺失、提供方激励机制缺失 | [29] | 高 |
| 中小企业合规工具门槛 | 高风险 AI 系统合规工具链可用性低，缺乏低门槛工程化产品 | [28] | 高 |
| 监管风险敞口量化 | 算法故障、对抗攻击、监管责任等风险纳入投资决策的标准化方法论缺失 | [24] | 中 |
| 经典奠基文献缺失 | OECD AI Principles (2019)、UNESCO Recommendation (2021)、Asilomar Principles (2017) 等未在证据集覆盖 | [q2] | 中 |
| 开源审计/红队工具链 | 合规审计工具链、红队测试框架、模型卡/数据卡库的最新可用版本与采用情况无证据 | [q3] | 高 |
| 事件治理标准化 | AI 事件治理的开放问题（分类、报告、响应）缺乏通用标准 | [18] | 高 |
| 全球南方参与度 | 国际 AI 治理中“全球多数”话语权不足，非洲等地区本土化框架起步晚 | [19, 20] | 中 |
| 临床/高风险领域落地 | 通用框架在临床决策等高风险点失效，缺乏领域化实施规范 | [22] | 高 |
| 可复现性治理 | 治理过程本身的可复现性（数据、代码、证据链）尚未形成规范 | [17] | 中 |

> **热度证据**：上述缺口均源自 2024-2026 年文献明确指出的开放问题 [17, 18, 19, 20, 22, 24, 27, 28, 29, q1, q2, q3]。
> **权威证据**：arXiv 预印本、共识文件、工作论文 [17, 18, 19, 20, 22, 24, 27, 28, 29]。
> **关注度**：高 | 依据：覆盖技术、法律、地缘政治多维度，为高杠杆切入点。
> **推荐度**：★★★★★ | 理由：直接指导后续研究与工程投入方向。

---

## 4. 瓶颈与拐点

### 4.1 核心瓶颈
- **静态合规与动态运行脱节**：现有治理多停留在政策指导/事后审计层面，缺乏运行时状态编排与阈值敏感整改机制 [14, 16]。
- **监管沙箱“三重困境”**：能力建设滞后、跨境协调机制缺失、提供方参与动力不足，制约创新友好监管落地 [29]。
- **合规工具链碎片化**：检查器、证据生成、红队测试等工具割裂，缺乏 Compliance-as-Code 统一基础设施 [27, 28]。
- **人类监督有效性受侵蚀**：实证显示人类对 AI 预测权威的过度信任显著窄化决策空间，挑战“人在环”假设 [2]。
- **原则到实践的“最后一公里”**：高层原则（公平、透明等）到具体阈值、指标、认证的可量化映射缺失 [15, 22, 31]。
- **可复现性危机延伸至治理**：治理证据链（数据、模型、审计日志）自身缺乏可复现性标准 [17]。

### 4.2 拐点信号
- **Compliance-as-Code 基础设施成型**：OSCAL 扩展与三层架构提出，标志着合规从“文档工作”向“代码化基础设施”转型 [27]。
- **运行层框架竞争涌现**：OADA、五层框架、Control Stack 同期出现，预示运行保障将成标准化竞争焦点 [14, 15, 16]。
- **监管沙箱强制落地倒逼能力建设**：EU AI Act 强制要求成员国建立沙箱，将迫使协调机制与激励设计在 2025-2026 年实质化 [29]。
- **全球南方自主框架崛起**：UG AIMS 等非洲本土框架发布，打破欧美主导叙事，推动多极治理格局形成 [19, 20]。

> **热度证据**：瓶颈与拐点均提炼自 2024-2026 年最新文献的实证分析与框架提案 [2, 14, 15, 16, 17, 22, 27, 29]。
> **权威证据**：arXiv 预印本、共识文件 [2, 14, 15, 16, 17, 22, 27, 29]。
> **关注度**：高 | 依据：直接关联法规生效时间表与工程落地可行性。
> **推荐度**：★★★★☆ | 理由：识别出“合规工程化”与“运行保障”双轨并行的关键拐点窗口。

---

## 5. 社会·政策·国际

### 5.1 欧盟主导全球监管基准
- EU AI Act (2024/1689) 为全球首部综合性 AI 法规，其合规要求、风险分级、监管沙箱机制成为事实上的国际基准，驱动全球合规工程化投入 [26, 27, 28, 29, 30, 31]。
- EC 提出简化 EU MDR/IVDR 与 AI Act 衔接，信号监管协调复杂度上升 [32]。

### 5.2 美国 NIST 路线：自愿框架+技术标准
- NIST AI RMF 与 OSCAL（FedRAMP 标准）结合，推动机器可读合规证据技术路线，影响联邦采购与行业实践 [27]。

### 5.3 国际标准化组织（ISO/IEC）桥梁作用
- ISO/IEC 42001 (AI 管理体系) 成为连接法规与工程实践的锚点，被纳入 ROI 量化框架与机器可读证据架构 [24, 27]。

### 5.4 全球南方与多极治理诉求
- “全球多数”倡议呼吁重构国际治理话语权，非洲 UG AIMS 提出本土化认证框架，挑战单极标准输出 [19, 20]。
- 新加坡共识聚焦 AI 安全研究优先级，展示中小国家主导专议题共识能力 [7]。

### 5.5 垂直领域专用治理萌芽
- 核能领域 AI 观测站 [21]、临床决策治理失效分析 [22]、自动驾驶感知合规 [30]、企业决策系统治理对象重构 [23]，显示治理向专用领域渗透。

> **热度证据**：多司法管辖区法规/标准/共识文件 2024-2026 年密集发布 [7, 19, 20, 21, 22, 23, 26, 27, 29, 30, 31, 32]。
> **权威证据**：官方法规 (EU AI Act)、官方标准 (NIST, ISO)、共识文件、arXiv/SSRN 预印本 [7, 19, 20, 21, 22, 23, 26, 27, 29, 30, 31, 32]。
> **关注度**：高 | 依据：地缘政治与监管竞争直接塑造合规成本与市场准入。
> **推荐度**：★★★★★ | 理由：必须建立多司法管辖区合规映射表作为工程基线。

---

## 6. 资本与生态

### 6.1 合规成本内部化与投资决策量化
- **风险调整智能红利框架**：将 ISO 42001 与监管风险敞口（算法故障、对抗攻击、监管责任）纳入 AI 项目 ROI 量化，反映资本对合规成本显性定价趋势 [24]。

### 6.2 开源生态早期形态
- 合规检查器、文档转换 (Docling [5])、LLM 应用全生命周期工具包 [6] 等开源工具涌现，但红队框架、模型卡库等核心治理基础设施在证据集中缺失 [q3]。
- 非洲 UG AIMS [20]、新加坡共识 [7] 等非商业生态节点形成。

### 6.3 人才与认证体系缺口
- 证据集未覆盖 AI 治理专业认证（如 AIGP）、人才流动、融资并购等资本层面数据 > 待核实。

> **热度证据**：量化 ROI 框架 [24]、开源工具 [5, 6] 为 2024-2026 年产出。
> **权威证据**：arXiv 预印本、GitHub 开源项目 [5, 6, 24]。
> **关注度**：中 | 依据：资本侧量化合规风险为早期信号，生态工具链尚不成熟。
> **推荐度**：★★★☆☆ | 理由：关注“合规即服务”赛道雏形与风险定价模型演进。

---

## 7. 信号与预测

| 信号 | 来源 | 可证伪预测 (6-18个月) | 置信度 | 不确定性说明 |
|------|------|------------------------|--------|--------------|
| OSCAL 成为合规证据交换事实标准 | [27] | **假设**：至 2027 年 Q2，至少 3 家主流 GRC 厂商或云厂商原生支持 OSCAL-AI 扩展导入/导出。 | 中 | 依赖 NIST/ISO 官方背书与 EU 监管机构认可，当前仅为预印本提案 [27]。 |
| 运行层治理框架 (OADA/Control Stack) 进入标准化竞争 | [14, 16] | **假设**：ISO/IEC JTC 1/SC 42 或 IEEE SA 启动“AI 运行治理”工作组，引用 OADA/Control Stack 概念。 | 中高 | 框架同期涌现表明需求明确，但标准化周期长，可能止步于技术报告。 |
| EU AI Act 监管沙箱在 ≥15 成员国实质运行 | [29] | **假设**：至 2026 年底，EU 官方沙箱名录显示 ≥15 成员国有活跃项目（>0 入驻提供方）。 | 中 | 当前面临“三重挑战” [29]，政治意愿与财政投入为关键变量。 |
| AI 事件报告强制化扩散至非 EU 司法管辖区 | [18] | **假设**：美国 (联邦/州)、英国、加拿大、韩国、新加坡中 ≥3 个出台强制 AI 事件报告法规/指引。 | 中 | [18] 指出开放问题，但立法滞后性大，可能止步于自愿指南。 |
| 全球南方自主认证框架获国际互认 | [19, 20] | **假设**：UG AIMS 或同类框架与 ISO 42001 / EU AI Act 合规路径建立映射互认试点。 | 低 | 地缘政治与标准霸权博弈激烈，互认阻力大 [19]。 |
| Compliance-as-Code 开源基础设施成熟 | [27, 28] | **假设**：GitHub 上出现 Star > 500 的开源“AI 合规编译器/运行时”项目，支持策略即代码、证据自动采集。 | 中高 | 工程需求刚性强 [27, 28]，但需厂商投入维护。 |
| 人类监督有效性量化指标纳入高风险 AI 认证 | [2] | **假设**：EU AI Act 高风险 AI 合规指引新增“人机交互可靠性测试”要求（含自动化偏见测量）。 | 低 | 当前法规文本未细化至行为学指标，修订周期长 [2, 26]。 |

> **热度证据**：预测基于 2024-2026 年文献明确的技术路线、政策文本与实证发现 [2, 14, 16, 18, 19, 20, 27, 28, 29]。
> **权威证据**：arXiv 预印本、官方法规、共识文件 [2, 14, 16, 18, 19, 20, 27, 28, 29]。
> **关注度**：高 | 依据：均为可观测、可证伪的工程/政策里程碑。
> **推荐度**：★★★★☆ | 理由：提供了具体的跟踪指标与验证节点，便于滚动更新追踪框架。

---

## 经典与奠基性工作

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| OECD AI Principles | 2019 | OECD | > 待核实 | 官方政府间组织原则 | 高 | ★★★★★ | https://www.oecd.org/ai/principles/ | 全球 AI 治理基石性软法，后续法规通用引用源。 |
| UNESCO AI Ethics Recommendation | 2021 | UNESCO | > 待核实 | 联合国教科文组织规范性文书 | 高 | ★★★★★ | https://unesdoc.unesco.org/ark:/48223/pf0000377897 | 首个全球性 AI 伦理政府间协议。 |
| Asilomar AI Principles | 2017 | Future of Life Institute | > 待核实 | 学术/产业共识声明 | 高 | ★★★★☆ | https://futureoflife.org/ai-principles/ | 早期产学研共识，影响后续原则制定。 |
| Montreal Declaration for Responsible AI | 2018 | Univ. Montreal | > 待核实 | 学术主导宣言 | 中 | ★★★★☆ | https://reponsibleai.montrealdeclaration.org/ | 强调责任与包容，补充 Asilomar。 |
| A multilevel framework for AI governance | 2023 | arXiv:2307.03198v2 | > 待核实 | arXiv 预印本 | 中 | ★★★☆☆ | [13] | 提供多层级治理结构理论基座，被后续框架引用。 |
| Navigating the EU AI Act: A Methodological Approach to Compliance for Safety-critical Products | 2024 | arXiv:2403.16808v2 | > 待核实 | arXiv 预印本 | 高 | ★★★★☆ | [26] | 早期系统性合规方法论，工程落地参考。 |
| The Singapore Consensus on Global AI Safety Research Priorities | 2025 | arXiv:2506.20702v2 | > 待核实 | 国际专家共识文件 | 高 | ★★★★☆ | [7] | 全球 AI 安全研究议程设定，影响资助方向。 |

> 注：OECD/UNESCO/Asilomar/Montreal 等经典文献不在提供的 32 条证据源中，标注为 `> 待核实`，需补全引用。表中仅 [13, 26, 7] 来自证据源。

---

## 开源项目与工程实践

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| Docling | 2025 | IBM Research | > 待核实 | arXiv 预印本 / GitHub | 中 | ★★★☆☆ | [5] | 高效文档转换工具链，支持合规文档自动化预处理。 |
| Generative AI Toolkit | 2024 | arXiv:2412.14215v1 | > 待核实 | arXiv 预印本 | 中 | ★★★☆☆ | [6] | LLM 应用全生命周期质量保障框架，含合规相关模块。 |
| UG AIMS | 2024 | Zenodo:10.5281/zenodo.20723049 | > 待核实 | Zenodo 存档 | 低 | ★★★☆☆ | [20] | 面向非洲的可扩展 AI 治理与认证框架原型。 |
| EU AI Act Compliance Checkers (各类原型) | 2025-2026 | 多个研究组 | > 待核实 | arXiv:2609.36228v1 评估对象 | 高 | ★★★☆☆ | [28] | 实证研究评估对象，工程化程度参差，无统一主流库。 |
| 红队测试框架 / 模型卡库 | - | - | > 待核实 | - | 高 | ★★★★★ | > 待核实 | **证据集未覆盖**，需补全 Garak, PyRIT, HF Model Cards 等主流工具现状。 |

> 注：核心治理工具链（红队、模型卡/数据卡标准化库）在提供证据中缺失，标注为 `> 待核实`。

---

## 数据集与评测基准

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| AI Incident Database (AIID) | 持续更新 | Partnership on AI | > 待核实 | 非营利组织维护 | 高 | ★★★★★ | https://incidentdatabase.ai/ | 核心事件治理数据源，[18] 指出其治理价值。 |
| EU AI Act Compliance Benchmark | - | - | > 待核实 | - | 高 | ★★★★☆ | > 待核实 | 证据集未覆盖，[28] 评估检查器隐含基准需求。 |
| LLM Safety/Red-teaming Benchmarks (e.g., HarmBench, SafetyBench) | 2023-2024 | 多机构 | > 待核实 | 顶会论文 | 高 | ★★★★★ | > 待核实 | 证据集未覆盖，合规评测核心依据。 |
| Model Card / Data Card 采用率数据集 | - | - | > 待核实 | - | 中 | ★★★☆☆ | > 待核实 | 证据集未覆盖，衡量透明度落地关键指标。 |

> 注：提供的 32 条证据源中无专门的 AI 治理数据集/基准（[1, 3, 4, 8, 9, 10, 11, 12] 均为非治理领域挑战赛/工具），上表为领域已知核心资源，均标注 `> 待核实`。

---

## 参考来源

[1] NTU-NPU System for Voice Privacy 2024 Challenge — http://arxiv.org/abs/2410.02371v1
[2] Faith in AI can narrow the futures individuals consider — http://arxiv.org/abs/2603.28944v2
[3] Real-Time 4K Super-Resolution of Compressed AVIF Images. AIS 2024 Challenge Survey — http://arxiv.org/abs/2404.16484v1
[4] Discovery Opportunities with Gravitational Waves -- TASI 2024 Lecture Notes — http://arxiv.org/abs/2409.08956v1
[5] Docling: An Efficient Open-Source Toolkit for AI-driven Document Conversion — http://arxiv.org/abs/2501.17887v1
[6] Generative AI Toolkit -- a framework for increasing the quality of LLM-based applications over their whole life cycle — http://arxiv.org/abs/2412.14215v1
[7] The Singapore Consensus on Global AI Safety Research Priorities — http://arxiv.org/abs/2506.20702v2
[8] GR-NLP-TOOLKIT: An Open-Source NLP Toolkit for Modern Greek — http://arxiv.org/abs/2412.08520v1
[9] Point Transformer V3 Extreme: 1st Place Solution for 2024 Waymo Open Dataset Challenge in Semantic Segmentation — http://arxiv.org/abs/2407.15282v1
[10] Atmospheric entry and fragmentation of small asteroid 2024 BX1: Bolide trajectory, orbit, dynamics, light curve, and spectrum — http://arxiv.org/abs/2403.00634v2
[11] Developing a 21st Century Global Library for Mathematics Research — http://arxiv.org/abs/1404.1905v1
[12] Double Multi-Head Attention Multimodal System for Odyssey 2024 Speech Emotion Recognition Challenge — http://arxiv.org/abs/2406.10598v1
[13] A multilevel framework for AI governance — http://arxiv.org/abs/2307.03198v2
[14] Operational AI Deployment Assurance: Governance-State Orchestration Under Threshold-Sensitive Deployment Conditions -- A Governance Framework for High-Stakes AI Systems — http://arxiv.org/abs/2605.27827v1
[15] A five-layer framework for AI governance: integrating regulation, standards, and certification — http://arxiv.org/abs/2509.11332v1
[16] AI Governance Control Stack for Operational Stability: Achieving Hardened Governance in AI Systems — http://arxiv.org/abs/2604.03262v1
[17] Reproducibility: The New Frontier in AI Governance — http://arxiv.org/abs/2510.11595v1
[18] Open Problems in AI Incident Governance — http://arxiv.org/abs/2607.05163v1
[19] The Global Majority in International AI Governance — http://arxiv.org/abs/2601.17191v1
[20] UG AIMS: A Scalable AI Governance and Certification Framework for Africa — https://doi.org/10.5281/zenodo.20723049
[21] Towards an AI Observatory for the Nuclear Sector: A tool for anticipatory governance — http://arxiv.org/abs/2504.12358v1
[22] From Principles to Practice: Why Global AI Governance Frameworks Fail at the Point of Clinical Decision-Making and What Africa Needs Instead — https://doi.org/10.2139/ssrn.6765739
[23] Beyond AI Governance: Rethinking the Governance Object in Enterprise AI A Conceptual Perspective on Enterprise Decision Systems — https://doi.org/10.2139/ssrn.7108858
[24] The Risk-Adjusted Intelligence Dividend: A Quantitative Framework for Measuring AI Return on Investment Integrating ISO 42001 and Regulatory Exposure — http://arxiv.org/abs/2511.21975v1
[25] Towards Assuring EU AI Act Compliance and Adversarial Robustness of LLMs — http://arxiv.org/abs/2410.05306v1
[26] Navigating the EU AI Act: A Methodological Approach to Compliance for Safety-critical Products — http://arxiv.org/abs/2403.16808v2
[27] Making AI Compliance Evidence Machine-Readable — http://arxiv.org/abs/2604.13767v1
[28] An Empirical Study and Assessment of EU AI Act Compliance Checkers — http://arxiv.org/abs/2609.36228v1
[29] Operationalising AI Regulatory Sandboxes under the EU AI Act: The Triple Challenge of Capacity, Coordination and Attractiveness to Providers — http://arxiv.org/abs/2509.05985v1
[30] How Could Generative AI Support Compliance with the EU AI Act? A Review for Safe Automated Driving Perception — http://arxiv.org/abs/2408.17222v1
[31] An Analysis of the New EU AI Act and A Proposed Standardization Framework for Machine Learning Fairness — http://arxiv.org/abs/2510.01281v1
[32] EC's Proposal for Simplification of EU MDR/IVDR Regulation in relation to the EU AI Act 2024/1689 — https://openalex.org/W7134993431

---

*Generated by research-bot · topic=`ai-治理与监管政策法规与标准` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`nvidia/nemotron-3-ultra-550b-a55b` · sources=32 · duration=332s · 2026-11-04T02:46:05+00:00*
