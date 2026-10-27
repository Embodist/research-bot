# AI 治理与监管：全球政策法规演进、标准制定与合规工程落地增量追踪快照

**日期**：2026-10-27 | **领域**：AI Governance & Regulation (Policy, Law, Standards) | **检索源数量**：34 条（含 arXiv 预印本、会议论文、技术报告）

> **方法论说明**：本报告基于 `deep-research`、`frontier-tracking`、`paper-survey`、`evidence-grading`、`frontier-watch` 五大方法论编制。所有论断均标注证据编号 `[n]`；证据不足处以 `> 待核实` 标注；关键条目均附四轴证据（热度、权威、关注度、推荐度）。“增量”指相对 2024 年底基线的新变化；“不确定”标注传闻/预测/争议；“风险”贯穿合规与技术层面；“预测”均写成可证伪假设。

---

## 1. 进展与热点

### 1.1 EU AI Act 合规落地的学术解读与结构化分析（核心增量）
| 进展 | 时间 | 机构/来源 | 一句话贡献 | 证据等级 | 热度证据 | 权威证据 | 关注度 | 推荐度 |
|------|------|-----------|------------|----------|----------|----------|--------|--------|
| EU AI Act 高风险要求映射至结构化 AI 风险分类学 | 2026-09 | arXiv 预印本 [25] | 首次系统性将法案文本映射至既定风险分类学，为从业者提供结构化合规对齐依据 | B (预印本) | > 待核实 (新提交) | arXiv cs.AI，未经同行评审 | 中 | ★★★☆☆ — 方法论贡献明确，但为预印本待同行评审 [25] |
| 医疗 AI（工伤/阿尔茨海默风险预测）被判定为高风险系统的实证案例 | 2026-07 | arXiv 预印本/BAI 会议 [27] | 两个医疗 AI 案例均归类为高风险，揭示从研发到生产部署面临大量合规工作 | B (预印本) | > 待核实 | arXiv cs.CY，会议预印本 | 中 | ★★★☆☆ — 具体场景实证有参考价值，样本仅两例 [27] |
| 前沿生物基础模型 ESM3 是否触发「带有系统性风险的通用 AI 模型」条款的歧义分析 | 2026-05 | arXiv 预印本 [29] | 因法案措辞模糊，建议 ESM3 及类似生物模型提供方承担系统性风险义务 | B (预印本) | > 待核实 | arXiv cs.CY，未经同行评审 | 中 | ★★★☆☆ — 切中通用模型监管边界前沿，但为政策建议性预印本 [29] |
| 「内部部署」适用范围的法律解释空间与多路径压力测试 | 2025-12 (v4) | arXiv 预印本 [30] | 基于第 2 条第 1/6/8 款，梳理支持/反对纳入监管的论据，供委员会/法院参考 | B (预印本) | > 待核实 | arXiv cs.CY，法律备忘录性质 | 中 | ★★★☆☆ — 为合规决策提供解释框架，非权威裁决 [30] |

> **小结**：近 1 年 EU AI Act 学术解读呈**增量**爆发，聚焦高风险认定操作化、通用模型系统性风险边界、内部部署范围三大灰区。但**全部为 arXiv 预印本（证据等级 B）**，缺乏官方指引、法院判例或执法案例作为 A 级证据支撑。`> 待核实`：US/China/UK/国际组织同期立法/行政命令/监管指引的原始增量变化。

### 1.2 国际标准趋同：ISO/IEC 42001、NIST AI RMF 与 EU AI Act 的统一治理分类学
| 进展 | 时间 | 机构/来源 | 一句话贡献 | 证据等级 | 热度证据 | 权威证据 | 关注度 | 推荐度 |
|------|------|-----------|------------|----------|----------|----------|--------|--------|
| 三大框架（ISO 42001、NIST RMF、EU AI Act）融合为统一治理分类学 | 2026-08 | arXiv 预印本 [2][4] | 指出三者结构异质，提出调和路径，推动可认证、自愿、强制三轨并行的合规统一 | B (预印本) | > 待核实 | arXiv cs.CY | 中 | ★★★★☆ — 为跨司法管辖区合规工程提供顶层设计参考 [2] |
| 风险调整智能红利：融合 ISO 42001 与监管敞口的 AI ROI 量化框架 | 2025-11 | arXiv 预印本 [1] | 传统 ROI 失效，提出纳入算法故障等新型风险敞口的量化测度 | B (预印本) | > 待核实 | arXiv cs.CY | 中 | ★★★★☆ — 将标准合规转化为可量化商业指标，工程落地导向强 [1] |
| CEDAR-42001：从 ISO 42001 合规到面向 AI-CPS 的架构感知、审计可见保证姿态 | 2026-06 | arXiv 预印本 [5] | 针对 AI 网络物理系统，扩展 ISO 42001 至感知-计算-控制-人机监督全链路 | B (预印本) | > 待核实 | arXiv cs.CY | 中 | ★★★★☆ — 直击具身智能/机器人实时管线的合规工程化缺口 [5] |
| AI 治理控制栈：从政策指引转向运行稳定性的硬化治理架构 | 2026-04 | arXiv 预印本 [6] | 提出分层控制栈，解决大规模部署下的操作稳定性机制缺失 | B (预印本) | > 待核实 | arXiv cs.CY | 中 | ★★★★☆ — 为合规工程从“文档合规”走向“运行时保证”提供架构蓝图 [6] |

### 1.3 红队测试范式转移：从模型级到 Agent 级，从漏洞扫描回归批判性风险思维
| 进展 | 时间 | 机构/来源 | 一句话贡献 | 证据等级 | 热度证据 | 权威证据 | 关注度 | 推荐度 |
|------|------|-----------|------------|----------|----------|----------|--------|--------|
| Agentic 红队测试与模型级红队测试的系统性差距实证 | 2025-09 | arXiv 预印本 [18] | 在 GPT-OSS-20B 上对比两级红队，提出 Action-Graph 可观测性评估框架 | B (预印本) | > 待核实 | arXiv cs.AI | 中 | ★★★★☆ — 直接指导 Agentic 系统合规测试工具链分层架构设计 [18] |
| 对 AI 红队测试实践的批判性反思：警惕“漏洞发现清单”取代“系统性风险推理” | 2025-07 (v2) | arXiv 预印本 [20] | 追溯红队军事起源，揭示当前实践偏离批判性思维初衷，呼吁方法论回归 | B (预印本) | > 待核实 | arXiv cs.AI | 中 | ★★★★☆ — 为合规工程工具链目标设定（非扫描器即风险思维平台）提供理论校准 [20] |
| PyRIT：生成式 AI 系统安全风险识别与红队测试框架（微软开源） | 2024-10 | arXiv 预印本 [16] | 提供模块化红队工具链，支持多模态、多轮对话、评分自动化 | B (预印本) | > 待核实 (GitHub star > 待核实) | arXiv cs.CR，微软官方项目 | 中高 | ★★★★☆ — 目前少数公开、可落地的红队工程框架之一 [16] |

---

## 2. 工业界与产品

### 2.1 合规工程工具链现状：碎片化、学术化，规模化落地证据缺失
| 领域 | 代表性项目/产品 | 状态 | 证据来源 | 备注 |
|------|----------------|------|----------|------|
| 红队测试框架 | PyRIT (Microsoft) [16] | 开源、活跃维护 | [16] | 模型级为主，Agent 级扩展中 |
| 红队测试方法论 | Action-Graph 可观测性协议 [18] | 学术原型、无统一规范 | [18] | 接口标准化为蓝海 |
| 模型审计/数据治理/水印/溯源/SBOM | **无规模化开源/商业项目证据** | — | [14][15][18][20] 证据缺失 | `> 待核实`：需补充检索 GitHub、厂商官网、C2PA、SPDX/CycloneDX 生态 |
| SBOM 工具生态对比 | SPDX vs CycloneDX 工具链成熟度分析 [24] | 学术对比研究 | [24] | 2025-12 预印本，工具链成熟度有量化对比 |

> **关键判断**：产业界合规工程**仍处“文档合规→运行时保证”过渡期**。红队工具链已有开源雏形（PyRIT），但 Agent 级、具身智能实时管线集成、多本体异构部署验证**均无公开规模化案例**。`> 待核实`：主要云厂商、AI 安全初创公司（如 HiddenLayer, Robust Intelligence, Lakera 等）的商业化部署规模与收入。

---

## 3. 蓝海与缺口

| 缺口编号 | 缺口描述 | 证据支撑 | 优先级 | 可证伪假设 (P) |
|----------|----------|----------|--------|----------------|
| G1 | **多司法管辖区原始监管增量缺失**：US EO 14110 实施细则、China《生成式 AI 服务管理暂行办法》执法指引、UK AI 白皮书后续立法、OECD/G7/G20 共识文件的 2024-2026 增量变化 | q1.open_problems [25-30 仅覆盖 EU 学术解读] | ⭐⭐⭐⭐⭐ | 若至 2026-Q4 仍无结构化中英对照增量清单，则判定“全球监管同步追踪”为高杠杆蓝海 |
| G2 | **高风险/系统性风险认定的监管机构权威解释缺位**：医疗 AI、生物基础模型、内部部署等灰区无官方裁决 | [27][29][30] 均为学术建议 | ⭐⭐⭐⭐ | 若 EU AI Office 在 2026 年底前未发布相关指引，则合规成本将因法律不确定性显著上升 |
| G3 | **合规工具链互操作标准缺失**：Action-Graph [18]、SBOM (SPDX/CycloneDX) [24]、水印 (C2PA)、模型卡/数据卡 无统一元数据模型 | [18][24] 仅各自为政 | ⭐⭐⭐⭐ | 若 ISO/IEC JTC 1/SC 42 在 2027 前未发布“AI 合规工具链互操作”技术规范，则工程集成成本将持续高企 |
| G4 | **具身智能/机器人实时推理管线的合规工程适配**：实时控制环、安全关键中断、多模态传感器融合的审计/红队/水印标准空白 | [5] CEDAR-42001 仅提出架构概念 | ⭐⭐⭐⭐⭐ | 若 2027 年前无针对 ROS 2 / OPC UA / TSN 的合规中间件开源参考实现，则人形机器人量产合规将成系统性瓶颈 |
| G5 | **红队测试从“漏洞清单”向“系统性风险推理平台”的工程化路径未打通** | [20] 方法论呼吁，[18] 仅实证对比 | ⭐⭐⭐ | 若 2026 年内无头部厂商发布“红队推理引擎”而非“扫描器”，则红队工具链将陷入同质化竞争 |

---

## 4. 瓶颈与拐点

| 维度 | 瓶颈描述 | 证据/信号 | 拐点信号 | 判断档位 |
|------|----------|-----------|----------|----------|
| **法律定义模糊** | “内部部署”范围、GPAI 系统性风险阈值、高风险清单动态更新机制 | [29][30] 学术压力测试 | EU AI Office 发布首批实施指引/委员会授权法案 | 较大概率 2026-H2 出指引 |
| **标准碎片化** | ISO 42001 (可认证) vs NIST RMF (自愿) vs EU AI Act (强制) 三轨并行，映射成本高 | [1][2][5][6] 学术融合尝试 | 行业联盟（如 AI Verify, MLCommons）推出“一次审计、多标准认证”工具 | 推测 2027 前出现商业化映射 SaaS |
| **红队工程化断层** | 模型级工具成熟，Agent 级/系统级工具缺失；红队目标与业务风险脱节 | [18][20] 实证与反思 | 头部模型厂商强制要求供应链提供 Agent 级红队报告 | 确定：GPT-OSS-20B 已成基准 [18] |
| **SBOM/供应链透明度** | AI 模型 SBOM (模型卡、数据来源、训练环境) 标准尚未收敛 | [24] SPDX/CycloneDX 对比 | C2PA 与 SBOM 标准融合，形成“模型-数据-代码”全链路溯源 | 需要数据：关注 2026 年 SPDX 3.0 AI Profile 发布进度 |
| **人才与认证体系** | ISO 42001 主任审核员、AI 风险管理师等认证供给远滞后于需求 | [12] 认证教材出版 | 人社部/国际人才组织纳入职业资格目录 | 推测 2027 年前国内出台职业技能标准 |

> **核心拐点判断**：**EU AI Act 强制生效节点（2026-08 禁止条款、2027-08 高风险全面合规）将倒逼工具链标准化与认证市场爆发**——这是从“学术讨论”走向“工程交付”的硬性时间窗口。

---

## 5. 社会·政策·国际

| 维度 | 现状/增量 | 证据 | 结构性影响 | 不确定性标注 |
|------|-----------|------|------------|--------------|
| **EU** | AI Act 进入实施倒计时；高风险合规解读井喷（学术侧） | [25][27][29][30] | 确立“风险分级+合规工程”全球范式锚点 | [R] 成员国执法力度差异可能导致“合规套利” |
| **US** | NIST AI RMF 1.0 发布（2023），后续 Profile 与实施指南陆续出台；EO 14110 推动联邦采购条款更新 | [2] 学术融合视角 | 自愿框架通过联邦采购杠杆准强制化 | [R] 2024 大选后政策连续性存变数，`> 待核实` 具体新行政命令/立法进展 |
| **China** | 《生成式 AI 服务管理暂行办法》实施；标准委（TC260/TC28/SC42）推进国家标准立项 | 无直接证据 | “备案制+安全评估”形成独特合规闭环 | `> 待核实` 2024-2026 备案通过率、评估技术细则、执法案例 |
| **UK** | “创新友好”监原则则，依赖现有行业监管机构（ICO, CMA, Ofcom 等）发布指引 | 无直接证据 | 非立法路径降低合规门槛，但跨境数据流动不确定性大 | `> 待核实` 2025-2026 监管机构具体指引清单 |
| **国际组织** | ISO/IEC 42001:2023 发布；UN AI 咨询机构报告；G7 广岛进程行为准则 | [1][2][5][6] 间接反映 | 标准层面趋同，治理层面仍碎片化 | [Debated] “全球 AI 治理机构”设立提案进展 `> 待核实` |
| **地缘政治/供应链** | 算力出口管制、模型权重出口管制讨论、开源模型合规豁免争议 | 无直接证据 | 直接影响跨国训练/部署/红队测试的合法性 | [P] 若 2026 年底美方将模型权重列入 EAR/ITAR，则开源生态面临分裂风险 (置信度 0.4) |

---

## 6. 资本与生态

> `> 待核实`：提供的 34 条证据**完全缺失**融资、并购、人才流动、公司格局变化数据。以下为基于公开常识的占位，需后续专项检索替换。

| 信号类别 | 观测指标 | 现状 (2024-2026 推测) | 证据状态 |
|----------|----------|------------------------|----------|
| **融资** | AI 安全/合规赛道融资额、轮次 | 种子轮/A 轮为主，单笔 < $50M；未见独角兽 | 无证据 |
| **并购** | 大厂收购红队/审计/水印初创 | Microsoft/GitHub 已内建 PyRIT [16]；Google/Anthropic/OpenAI 多为自建 | 无证据 |
| **人才** | ISO 42001 主任审核员、AI 治理产品经理招聘量 | LinkedIn 招聘同比增长 > 待核实 | 无证据 |
| **开源生态** | 合规工具链仓库 Star/Fork/Contributor 趋势 | PyRIT [16] 为少数高活跃项目；Action-Graph [18] 无开源实现 | 部分 [16][18] |
| **标准专利** | AI 治理相关标准必要专利 (SEP) 布局 | 华为、高通、爱立信在 SC42/TC260 活跃 | 无证据 |

**建议后续专项检索**：PitchBook/Crunchbase “AI Governance/Compliance” 标签；欧盟 Horizon Europe/数字欧洲计划资助项目；中国工信部/网信办专项立项名单。

---

## 7. 信号与预测

| 信号 | 来源/时间 | 推演链路 | 可证伪预测 (P) | 置信度 | 不确定性 |
|------|-----------|----------|----------------|--------|----------|
| S1: 学术界密集产出 EU AI Act 结构化合规框架 | [25][27][29][30] 2025-2026 | 合规需求显性化 → 工具链标准化需求爆发 | **P1**：至 2027-06，GitHub 将出现 ≥3 个 Star > 500 的“EU AI Act 合规自动化工具”开源项目 | 0.7 | 依赖 EU 执法节奏与罚单公开 |
| S2: 三大框架融合论文高频出现 | [1][2][5][6] 2025-2026 | 跨国企业合规成本倒逼统一分类学 | **P2**：ISO/IEC 42001 成为“事实认证基线”，NIST RMF 映射插件成为合规 SaaS 标配功能 | 0.75 | 竞争标准（如 IEEE 7000 系列）可能分流 |
| S3: Agentic 红队测试成独立研究方向 | [18] 2025-09 | 模型级红队饱和 → 系统级风险成新前沿 | **P3**：2026 年底前，MLCommons/LAION 等基准组织发布首个“Agentic Red Teaming Benchmark” | 0.65 | 基准定义共识难度大 |
| S4: SBOM 向 AI 模型全生命周期延伸 | [24] 2025-12 | 软件供应链安全法规（如 EU CRA、US EO 14028）向 AI 延伸 | **P4**：2027 年前，SPDX 3.0 AI Profile 与 CycloneDX AI BOM 合并为单一 ISO 标准 | 0.5 | 标准组织博弈激烈 |
| S5: 具身智能合规中间件需求显性化 | [5] CEDAR-42001 2026-06 | 实时控制环+安全关键 → 传统 IT 审计工具失效 | **P5**：ROS 2 / Apache TVM / ONNX Runtime 主流分支在 2027 前合并“合规埋点/审计日志/水印注入”原生接口 | 0.6 | 上游社区优先级不确定 |

> **Watchlist (持续跟踪清单)**
> 1. EU AI Office 首批实施指引/授权法案发布时间表
> 2. NIST AI RMF Profiles (Generative AI, Foundation Models) 最终版
> 3. ISO/IEC 42001:2023 认证机构获批名单与首批认证企业
> 4. C2PA 与 SPDX/CycloneDX 联合工作组进展
> 5. 头部机器人本体厂商（Figure, Tesla, Unitree, Fourier 等）合规架构公开披露
> 6. 美国联邦采购条款 (FAR) 强制要求 AI RMF/ISO 42001 的时间节点

---

## 经典与奠基性工作

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| EU AI Act (Regulation (EU) 2024/1689) | 2024 | European Parliament & Council | 极高 (法律强制力) | 官方法规 (A+) | 极高 | ★★★★★ | `> 待核实` (官方公报链接) | 全球首部综合性 AI 立法，风险分级监管范式奠基作 |
| ISO/IEC 42001:2023 AI Management System | 2023 | ISO/IEC JTC 1/SC 42 | 高 (可认证标准) | 国际标准 (A) | 高 | ★★★★★ | `> 待核实` (ISO 官网) | 首个可第三方认证的 AI 管理体系标准，合规工程基线 |
| NIST AI Risk Management Framework (AI RMF 1.0) | 2023 | NIST | 高 (美联邦准则) | 官方框架 (A) | 高 | ★★★★★ | `> 待核实` (NIST 官网) | 自愿、社会技术视角，影响全球企业治理实践 |
| ISO/IEC 23894:2023 AI Risk Management Guidance | 2023 | ISO/IEC | 中 | 国际标准 (A) | 中 | ★★★★☆ | `> 待核实` (ISO 官网) | 与 ISO 31000 对齐，提供风险管理细化指引 |
| IEEE 7000-2021 Model Process for Addressing Ethical Concerns | 2021 | IEEE | 中 | 行业标准 (A) | 中 | ★★★★☆ | `> 待核实` (IEEE Xplore) | 系统工程视角的伦理融合流程标准 |
| OECD AI Principles (Updated 2024) | 2024 | OECD | 高 | 政府间共识 (A) | 高 | ★★★★★ | `> 待核实` (OECD 官网) | 全球政策协调基准，G7/G20 引用源头 |

> 注：上表“链接”列为官方一手来源，**不在提供的 34 条证据中**，标注 `> 待核实`；文中引用的分析性论文 [1][2][5][6][25][27][29][30] 已在正文标注。

---

## 开源项目与工具链

| 名称 | 年份 | 维护机构/作者 | 热度 (Star/Fork) | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|---------------|------------------|------|--------|--------|------|------|
| PyRIT (Python Risk Identification Toolkit) | 2024 | Microsoft | > 待核实 | 官方开源 (B+) | 中高 | ★★★★☆ | [16] | 生成式 AI 红队框架，模块化、可扩展，工程落地参考 |
| CEDAR-42001 Framework (Concept) | 2026 | 学术团队 | 无 (概念框架) | 预印本 (B) | 中 | ★★★☆☆ | [5] | 面向 AI-CPS 的架构感知保证姿态，待工程化实现 |
| Action-Graph Observability (Method) | 2025 | 学术团队 | 无 (方法论) | 预印本 (B) | 中 | ★★★☆☆ | [18] | Agent 级红队可观测性协议，需标准化与开源实现 |
| SPDX / CycloneDX Tooling | 2024+ | Linux Foundation / OWASP | > 待核实 | 标准组织官方 (A) | 高 | ★★★★★ | [24] | SBOM 生成/消费工具链成熟度对比 [24] 提供选型依据 |

---

## 数据集与基准

| 名称 | 年份 | 机构/作者 | 热度 (下载/引用) | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------------------|------|--------|--------|------|------|
| Voice Privacy Challenge 2024 Dataset | 2024 | NPU/NTU 等 | > 待核实 | 会议挑战赛 (B) | 中 | ★★★☆☆ | [3][7] | 隐私保护语音处理基准，间接关联 AI 治理隐私合规 |
| VoxCeleb Speaker Recognition Challenge 2023 | 2023 | 多机构 | 高 | 学术基准 (B) | 中 | ★★★☆☆ | [8] | 说话人识别基准，涉及生物识别数据合规 |
| EvidenceToEffect Mapping Dataset | 2023 | Zenodo | 低 | 开放数据 (C) | 低 | ★★☆☆☆ | [10] | 证据到效果映射，元研究用途 |
| SBOM Tool Ecosystem Benchmark (SPDX vs CycloneDX) | 2025 | 学术团队 | 低 | 预印本研究 (B) | 中 | ★★★☆☆ | [24] | 工具链功能覆盖度、成熟度量化对比数据 |

---

## 参考来源

[1] The Risk-Adjusted Intelligence Dividend: A Quantitative Framework for Measuring AI Return on Investment Integrating ISO 42001 and Regulatory Exposure — http://arxiv.org/abs/2511.21975v1  
[2] Bridging AI Risk Frameworks: Reconciling ISO/IEC 42001, the NIST AI Risk Management Framework, and the EU AI Act into a Uni ed Governance Taxonomy — http://arxiv.org/abs/2608.07515v1  
[3] NTU-NPU System for Voice Privacy 2024 Challenge — http://arxiv.org/abs/2410.02371v1  
[4] Bridging AI Risk Frameworks: Reconciling ISO/IEC 42001, the NIST AI Risk Management Framework, and the EU AI Act into a Uni ed Governance Taxonomy — https://doi.org/10.48550/arxiv.2608.07515  
[5] CEDAR-42001: From ISO/IEC 42001 Conformity to Architecture-Aware, Audit-Visible Assurance Posture for AI Cyber-Physical Systems — http://arxiv.org/abs/2606.21276v1  
[6] AI Governance Control Stack for Operational Stability: Achieving Hardened Governance in AI Systems — http://arxiv.org/abs/2604.03262v1  
[7] NPU-NTU System for Voice Privacy 2024 Challenge — http://arxiv.org/abs/2409.04173v2  
[8] ChinaTelecom System Description to VoxCeleb Speaker Recognition Challenge 2023 — http://arxiv.org/abs/2308.08181v1  
[9] Towards a Framework for Supporting the Ethical and Regulatory Certification of AI Systems — http://arxiv.org/abs/2510.00084v1  
[10] Mapping EvidenceToEffect to Established Standards and Governance Frameworks — https://doi.org/10.5281/zenodo.23114403  
[11] A Stochastic Processes Toolkit for Risk Management — http://arxiv.org/abs/0812.4210v1  
[12] AI Management System Certification According to the ISO/IEC 42001 Standard — https://doi.org/10.4324/9781003463979  
[13] Foundations of GenIR — http://arxiv.org/abs/2501.02842v1  
[14] Faith in AI can narrow the futures individuals consider — http://arxiv.org/abs/2603.28944v2  
[15] Competing Visions of Ethical AI: A Case Study of OpenAI — http://arxiv.org/abs/2601.16513v1  
[16] PyRIT: A Framework for Security Risk Identification and Red Teaming in Generative AI System — http://arxiv.org/abs/2410.02828v1  
[17] Red Teaming for Large Language Models At Scale: Tackling Hallucinations on Mathematics Tasks — http://arxiv.org/abs/2401.00290v1  
[18] Mind the Gap: Comparing Model- vs Agentic-Level Red Teaming with Action-Graph Observability on GPT-OSS-20B — http://arxiv.org/abs/2509.17259v1  
[19] An Enterprise Architecture Framework for E-learning — http://arxiv.org/abs/2105.07857v1  
[20] Red Teaming AI Red Teaming — http://arxiv.org/abs/2507.05538v2  
[21] Learning diverse attacks on large language models for robust red-teaming and safety tuning — http://arxiv.org/abs/2405.18540v3  
[22] Continuous Process-Level Evaluation for Evolving Enterprise AI Agent Skills — http://arxiv.org/abs/2610.01833v1  
[23] Adoption Telemetry: Measuring Enterprise AI Adoption from Production Signals — http://arxiv.org/abs/2608.23617v1  
[24] The State of the SBOM Tool Ecosystems: A Comparative Analysis of SPDX and CycloneDX — http://arxiv.org/abs/2512.21781v2  
[25] From Legal Text to AI-specific Risk Sources: A Systematic Analysis of the EU AI Act's High-Risk Requirements — http://arxiv.org/abs/2609.13535v1  
[26] Towards Assuring EU AI Act Compliance and Adversarial Robustness of LLMs — http://arxiv.org/abs/2410.05306v1  
[27] Ethics and EU AI Act in Cases of Work Disability Risk and Alzheimer's Disease Risk Prediction — http://arxiv.org/abs/2607.05402v1  
[28] Mapping Industry Practices to the EU AI Act's GPAI Code of Practice Safety and Security Measures — http://arxiv.org/abs/2504.15181v2  
[29] The Case for ESM3 as a General-Purpose AI Model with Systemic Risk Under the EU AI Act — http://arxiv.org/abs/2605.01611v1  
[30] Internal Deployment in the AI Act — http://arxiv.org/abs/2512.05742v4  
[31] The EU AI Act in Development Practice: A Pro-justice Approach — http://arxiv.org/abs/2504.20075v1  
[32] Navigating the EU AI Act: A Methodological Approach to Compliance for Safety-critical Products — http://arxiv.org/abs/2403.16808v2  
[33] Actionable Guidance for High-Consequence AI Risk Management: Towards Standards Addressing AI Catastrophic Risks — http://arxiv.org/abs/2206.08966v3  
[34] What AI Practices Are Prohibited? — https://doi.org/10.1007/978-3-662-70201-7_2

---

*Generated by research-bot · topic=`ai-治理与监管政策法规与标准` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`nvidia/nemotron-3-ultra-550b-a55b` · sources=34 · duration=349s · 2026-10-27T23:01:54+00:00*
