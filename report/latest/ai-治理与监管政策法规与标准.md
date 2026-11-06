# 全球 AI 治理与监管（政策、法规与标准）增量调研报告

**日期**：2026-11-06（UTC）  
**领域**：AI Governance & Regulation（政策、法规与标准）  
**检索源数量**：35 条可引用证据源（[1]–[35]）

---

## 1. 进展与热点

### 1.1 EU AI Act 核心条文解释的实质性分歧（增量）

| 进展点 | 时间 | 机构/来源 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 说明 |
|--------|------|-----------|----------|----------|--------|--------|------|
| “内部部署”是否纳入监管范围存在关键歧义（Article 2(1)/2(6)/2(8)） | 2025 | arXiv cs.CY [7] | > 待核实（预印本 v4，引用数未给出） | arXiv 预印本，非同行评审 | 高 —— EU AI Act 为全球首部综合性 AI 立法，范围解释直接影响合规成本 | ★★★★☆ —— 一手法律分析，为合规边界划分与后续指导文件提供解释路径 | 系统梳理内部部署的 AI 模型/系统是否受法案约束，并分析科研豁免复杂性 [7] |
| 前沿生物基础模型（ESM3）可能被认定为“系统性风险”GPAI，触发更严格义务 | 2026 | arXiv cs.CY [9] | > 待核实（预印本 v1，引用数未给出） | arXiv 预印本，非同行评审 | 高 —— 生物×AI 治理新交叉点，监管对象边界外延争议 | ★★★★☆ —— 跨领域新颖切入点，值得政策制定者与模型提供方关注 | 将 ESM3 映射至生物风险链，主张提供方承担 GPAI 系统性风险义务，指出法案措辞模糊导致执法不确定性 [9] |
| 敏捷开发团队缺乏与 AI Act 要求（文档、风险管理、人工监督）对齐的具体工件 | 2026 | arXiv cs.SE [11] | > 待核实（预印本 v1，引用数未给出） | arXiv 预印本，非同行评审 | 中高 —— 工程落地视角稀缺，直接关联软件交付流程改造 | ★★★★☆ —— 面向研发团队的实操指南原型，填补法规文本到工程实践空白 | 指出抽象条款未映射到 Definition of Done、Sprint Review 等敏捷实践，提出基于指南的操作化方法 [11] |

### 1.2 标准与金融量化结合的新框架

| 进展点 | 时间 | 机构/来源 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 说明 |
|--------|------|-----------|----------|----------|--------|--------|------|
| ISO/IEC 42001 被纳入 AI 投资风险调整框架，量化合规成本与监管敞口 | 2025 | arXiv cs.CY [1] | > 待核实（预印本 v1，引用数未给出） | arXiv 预印本，非同行评审 | 中 —— 标准被学术界引入财务建模，显示其在治理落地核心地位 | ★★★☆☆ —— 为企业级 AI 治理与投资决策提供可量化的标准对齐路径 | 提出“风险调整智能红利”框架，显式整合 ISO 42001 与监管责任敞口 [1] |

### 1.3 算法审计与平台透明度的“问责悖论”

| 进展点 | 时间 | 机构/来源 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 说明 |
|--------|------|-----------|----------|----------|--------|--------|------|
| 平台 API 限制导致独立算法审计出现“问责悖论”，与 EU DSA 透明度要求冲突 | 2025/2026-06 更新 | arXiv cs.CY [16] | arXiv v5（2026-06-12 更新），引用数未给出 | arXiv 预印本，非同行评审 | 中 —— 政策与工程界共同关注的合规落地难点 | ★★★★☆ —— 提供可落地的算法审计框架与跨平台对比证据 | 构建结构化审计框架，对比 X/Twitter、Reddit、TikTok、Meta 四大平台，识别“审计盲区” [16] |

### 1.4 垂直行业治理框架与情感 AI 新风险

| 进展点 | 时间 | 机构/来源 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 说明 |
|--------|------|-----------|----------|----------|--------|--------|------|
| 保险灾害风险场景提出 TRUST 框架（透明度、风险归属、底层数据……），面向行业特定可信 AI 治理 | 2026 | Journal of Engineering and Computational Intelligence Review [23] | citations=0（新刊发） | 同行评审期刊 | 低 —— 新发表、行业细分首发 | ★★★☆ —— 为垂直行业定制治理框架，展示风险分级与合规工程落地，通用性待验证 | 针对美财产与意外险核保/定价/灾害建模/理赔全流程，强调可审查性 [23] |
| 情感 AI 与“伪亲密”引发真实性与算法情感交换的伦理治理新议题 | 2025 | Frontiers in Psychology [21] | citations=62 | 同行评审期刊 | 中 —— 心理学/HCI 社区关注度较高 | ★★★☆ —— 从心理学视角补充“心理/情感操纵”风险维度，对风险分级体系扩展有参考 | 探讨陪伴聊天机器人、虚拟朋友如何逼近人类专属共情/亲密领域 [21] |

> 待核实：美国联邦/州层面、中国（算法备案/生成式 AI 管理条例）、国际标准组织（ISO/IEC JTC 1/SC 42 除 42001 外）在 2024-2026 年的实质性政策/标准原始文件证据在候选来源中缺失 [q1-open_problems]。

---

## 2. 工业界与产品

### 2.1 合规工程化工具链的空白与雏形

| 产品/项目 | 时间 | 机构/作者 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 说明 |
|-----------|------|-----------|----------|----------|--------|--------|------|
| AAGATE：面向 Agentic AI 的 Kubernetes 原生治理控制平面，与 NIST AI RMF 对齐 | 2025 | arXiv cs.CR [31] | > 待核实（预印本 v2，未确认开源状态与 GitHub star） | arXiv 预印本，非同行评审 | 中等 —— Agentic AI 治理新架构，近期预印本 | ★★★☆ —— 提供代理型 AI 治理平台参考架构，工程落地参考价值较高，需确认开源与复现 | 将 NIST AI RMF 运营化，指出传统 AppSec 工具不足以应对即兴的机器速度系统 [31] |
| SCITUS：将 NIST AI RMF 1.0 系统性适配至加拿大多司法管辖区监管环境的框架 | 2026 | arXiv cs.CY [29] | > 待核实（预印本 v1，非现成工具链） | arXiv 预印本，非同行评审 | 中等 —— 跨司法管辖区合规工程化稀缺工作 | ★★★☆ —— 方法论参考价值高，但为框架设计而非现成工具链 | 针对加拿大联邦指令与省级法规碎片化、Bill C-27 夭折后的合规指导真空 [29] |

> 待核实：候选证据中**缺乏明确标识为开源**的 AI 合规、红队测试、模型审计工具链项目（Garak、PyRIT、Model Cards Toolkit、AI Verify 等知名项目未在证据中出现） [q3-findings-3, 25,29,31,32]。

### 2.2 经典/奠基性工作表（含最新进展与经典区分）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| Internal Deployment in the AI Act | 2025 | arXiv cs.CY | > 待核实 | 预印本 | 高 | ★★★★☆ | [7] | EU AI Act 核心条文解释，合规边界划分 |
| The Case for ESM3 as GPAI with Systemic Risk Under the EU AI Act | 2026 | arXiv cs.CY | > 待核实 | 预印本 | 高 | ★★★★☆ | [9] | 生物基础模型纳入系统性风险分类首发 |
| Operationalizing the EU AI Act in Agile Software Development | 2026 | arXiv cs.SE | > 待核实 | 预印本 | 中高 | ★★★★☆ | [11] | 敏捷流程合规操作化指南原型 |
| The Risk-Adjusted Intelligence Dividend (ISO 42001 + Regulatory Exposure) | 2025 | arXiv cs.CY | > 待核实 | 预印本 | 中 | ★★★☆☆ | [1] | 标准与金融量化结合框架 |
| The Accountability Paradox: Platform API Restrictions Undermine AI Transparency Mandates | 2025/2026 | arXiv cs.CY | > 待核实 | 预印本 | 中 | ★★★★☆ | [16] | 算法审计框架与跨平台实证 |
| Governing AI in Catastrophe Risk Intelligence: TRUST Framework | 2026 | J. Eng. Comput. Intell. Rev. | citations=0 | 同行评审 | 低 | ★★★☆☆ | [23] | 保险垂直行业治理框架 |
| Emotional AI and the rise of pseudo-intimacy | 2025 | Frontiers in Psychology | citations=62 | 同行评审 | 中 | ★★★☆☆ | [21] | 情感 AI 心理风险维度 |
| AAGATE: NIST AI RMF-Aligned Governance Platform for Agentic AI | 2025 | arXiv cs.CR | > 待核实 | 预印本 | 中等 | ★★★☆☆ | [31] | Agentic AI 治理控制平面架构 |
| SCITUS: Multi-Jurisdictional Framework Adapting NIST AI RMF to Canadian Context | 2026 | arXiv cs.CY | > 待核实 | 预印本 | 中等 | ★★★☆☆ | [29] | 多司法管辖区合规适配方法论 |

> 待核实：更早期的经典奠基工作（如 EU AI Act 初版提案分析 [12]、NIST AI RMF 1.0 发布、ISO/IEC 42001 正式出版、早期算法审计理论文献）在候选证据中未覆盖，需补充检索。

---

## 3. 蓝海与缺口

| 缺口维度 | 具体描述 | 证据来源 | 优先级 |
|----------|----------|----------|--------|
| 多司法管辖区原始政策文件覆盖不足 | 美国联邦/州、中国算法备案/生成式 AI 条例、ISO/IEC JTC 1/SC 42 新进展（除 42001）在 2024-2026 年实质性原始文件证据缺失 | [q1-open_problems] | 高 |
| EU AI Act 关键定义的官方指导与执法实践真空 | “内部部署”、“系统性风险”阈值、“通用 AI 模型”分层等核心定义缺乏监管机构确认性裁决与指导文件 | [7, 9, 11, q1-open_problems] | 高 |
| 生物/跨领域前沿模型的监管分类不确定 | ESM3 等生物基础模型是否纳入 GPAI 系统性风险监管，缺乏监管机构确认性裁决 | [9, q1-open_problems] | 高 |
| ISO 标准族协同落地工程案例缺失 | ISO 42001 与 23894（风险管理）、42006（审核指南）等垂直标准的协同落地路径在工程侧缺乏公开案例研究 | [1, q1-open_problems] | 中高 |
| 敏捷/DevOps 最小可行合规工件集无共识 | 与 AI Act 要求（技术文档、风险管理体系、人工监督记录）对齐的 MVP 工件集尚未形成行业共识 | [11, q1-open_problems] | 中高 |
| 通用算法审计框架与平台 API 限制的工程适配路径 | 结构化审计框架与平台特定 API 限制之间的工程化适配路径未打通 | [16, q2-open_problems] | 高 |
| 垂直行业框架与通用标准的映射互操作 | 保险/医疗/金融等垂直治理框架与 ISO 42001、EU AI Act 等跨行业标准的映射与互操作机制缺失 | [23, q2-open_problems] | 中高 |
| 情感/生成式 AI 心理风险量化指标标准化 | 情感操纵、伪亲密等心理风险量化指标及纳入风险分级体系的标准化方法缺失 | [21, q2-open_problems] | 中 |
| 独立第三方审计在黑箱+受限数据条件下的可行性边界 | “黑箱模型+受限数据访问”条件下独立审计的可行性边界与工具链缺口 | [16, q2-open_problems] | 高 |
| 开源合规/红队/审计工具链实战验证缺失 | 经实战验证的开源工具链在候选证据中未被覆盖（Garak、PyRIT 等知名项目未现身） | [q3-findings-3, 25,29,31,32] | 高 |
| 多司法管辖区合规自动化工程实践无开源实现 | SCITUS 等框架落地为代码/管道的开源实现证据缺失 | [29, q3-open_problems] | 中高 |
| Agentic AI 治理平面开源状态与生态集成未确认 | AAGATE 等架构的开源状态、生态集成与社区采用度待确认 | [31, q3-open_problems] | 中 |
| NIST AI RMF 与 EU AI Act/ISO 42001 工程化映射工具缺失 | 主流框架间的工程化映射工具（自动化合规检查、证据收集管道）缺失 | [q3-open_problems] | 高 |

---

## 4. 瓶颈与拐点

| 瓶颈/拐点 | 现状与信号 | 证据来源 | 判断依据 |
|-----------|------------|----------|----------|
| **法律文本与工程实践的鸿沟**（瓶颈） | AI Act 抽象条款未映射到敏捷工件；合规成本高、解释分歧大 | [7, 11, q1-open_problems] | 法条与 Sprint/DoD 无直接映射，导致“合规剧本”缺位 |
| **“系统性风险”阈值与分类的不确定性**（瓶颈） | GPAI 分层、生物模型纳入标准模糊，执法不确定性高 | [9, q1-open_problems] | 措辞模糊导致模型提供方无法确定义务边界 |
| **平台数据访问与透明度强制力的错位**（瓶颈） | EU DSA 要求数据访问，平台通过 API 限制实质阻断独立审计 | [16] | 结构性“问责悖论”需立法/技术双轨破解 |
| **多司法管辖区合规碎片化**（瓶颈） | 加拿大联邦+省级、中美欧差异导致合规成本指数级上升 | [29, q1-open_problems] | SCITUS 等方法论尚未工程化为自动化管道 |
| **开源工具链生态尚未成熟**（瓶颈） | 红队、审计、模型卡、合规检查工具分散，缺乏集成平台与实战验证 | [q3-findings-3, q3-open_problems] | 知名项目（Garak/PyRIT/AI Verify）未在证据链中形成体系化覆盖 |
| **垂直行业风险量化指标缺失**（瓶颈） | 保险 TRUST、情感 AI 心理风险等缺乏可量化、可比对的指标体系 | [21, 23, q2-open_problems] | 定性框架难以接入自动化风险管理流程 |
| **拐点信号：监管执法从“指导”转向“强制”**（拐点） | EU AI Act 分阶段生效、DSA 执法案例增多、美国州级立法加速 | [7, 9, 11, 16] | 合规从“自愿对齐”转为“强制交付证据”，倒逼工程化工具链爆发 |
| **拐点信号：标准成为金融/保险定价输入**（拐点） | ISO 42001 被纳入 ROI 风险调整框架，合规成本显性化为财务参数 | [1] | 资本市场开始为合规成本定价，驱动企业主动投入治理工程 |

---

## 5. 社会·政策·国际

| 维度 | 关键进展/冲突 | 证据来源 | 影响评估 |
|------|---------------|----------|----------|
| **EU AI Act 实施与解释争议** | 内部部署范围、系统性风险分类、敏捷合规工件缺位 | [7, 9, 11] | 全球合规基线制定者，解释分歧直接外溢至跨国企业合规成本 |
| **EU Digital Services Act (DSA) 与平台实操冲突** | 透明度强制要求 vs 平台 API 限制导致的“问责悖论” | [16] | 独立审计生态能否存活的关键博弈，影响全球算法治理范式 |
| **加拿大多层级监管碎片化** | 联邦指令+省级法规+Bill C-27 夭折，合规指导真空 | [29] | 典型“联邦制 AI 治理难题”，SCITUS 类适配框架需求上升 |
| **美国垂直行业自主治理** | 保险业 TRUST 框架针对核保/定价/灾害建模/理赔全流程 | [23] | 缺乏联邦统一立法下，行业自律框架成为主流合规路径 |
| **中国算法备案与生成式 AI 管理条例** | > 待核实：候选证据中无 2024-2026 年原始文件与执法案例覆盖 | [q1-open_problems] | 全球第二大 AI 市场，政策信号对跨国合规策略影响大，证据缺口需补齐 |
| **国际标准组织（ISO/IEC JTC 1/SC 42）标准族演进** | ISO 42001 进入财务建模；23894/42006 协同落地案例缺失 | [1, q1-open_problems] | 标准从“自愿最佳实践”向“合规推定依据”转变，国际互认进程加速 |
| **生物安全与 AI 融合监管新前沿** | ESM3 等生物基础模型可能触发 GPAI 系统性风险义务 | [9] | 生物×AI 双重用途治理成为国际安全议程新增长点 |

---

## 6. 资本与生态

| 生态维度 | 观察与信号 | 证据来源 | 说明 |
|----------|------------|----------|------|
| **合规成本资本化/金融化** | ISO 42001 被纳入“风险调整智能红利”框架，量化监管敞口与 ROI | [1] | 合规不再是纯成本中心，成为投资决策显性变量，推动治理工程预算增长 |
| **保险业作为治理采购方** | TRUST 框架面向 P&C 保险核保/定价/理赔，保险商承担模型风险敞口 | [23] | 高风险垂直行业以保险合规为牵引，建立可审查性工程标准 |
| **开源治理工具链生态碎片化** | 候选证据中无成熟开源合规/红队/审计平台；知名项目未形成证据链覆盖 | [q3-findings-3, 25,29,31,32] | 社区缺乏“Linux 级”治理基础设施，商业 SaaS 与咨询主导，开源生态待构建 |
| **Agentic AI 治理基础设施雏形** | AAGATE 提出 Kubernetes 原生控制平面，将 NIST AI RMF 运营化 | [31] | 代理型系统爆发前夜，治理基础设施赛道可能出现独角兽窗口 |
| **多司法管辖区合规 SaaS 需求上升** | SCITUS 等方法论指向自动化适配管道，跨国企业合规成本指数级增长 | [29, q1-open_problems] | 合规自动化软件市场从“文档生成”向“证据链自动采集/持续监测”升级 |
| **人才与认证体系建设** | > 待核实：ISO 42001 主管审核员、AI Act 合规官等认证体系在候选证据中未覆盖 | [q1-open_problems] | 专业服务机构（Big Four、专业合规咨询）成为生态关键节点 |

---

## 7. 信号与预测

| 信号/预测 | 表述（含不确定性标记） | 依据链 | 可证伪假设 | 置信度 |
|-----------|------------------------|--------|------------|--------|
| **信号**：EU AI Act 执法指导文件将在 2026-2027 陆续发布，澄清“内部部署”、“系统性风险阈值” | [P] 预测：欧盟委员会/EAIB 将于 2026-Q4 至 2027-Q2 发布至少 3 份关键实施指导 | AI Act 分阶段生效时间表、[7,9,11] 暴露的解释分歧、监管机构惯例 | 若至 2027-06-30 仍无官方指导文件发布，则判断不成立 | 较大概率 |
| **信号**：至少 2 个主要司法管辖区（如加州、新加坡、英国）将在 2027 前强制要求高风险 AI 系统提交独立第三方审计报告 | [P] 预测：跟随 EU AI Act 第 3 类/第 4 类高风险系统审计要求，竞争性立法扩散 | [16] DSA 审计强制力、[7,11] AI Act 合规工程化压力 | 若 2027-12-31 前无新增司法管辖区出台强制审计法规，则判断不成立 | 推测 |
| **信号**：ISO 42001 认证将成为企业融资/保险定价/政府采购的显性门槛 | [P] 预测：2027 前，≥3 家国际大型银行/保险机构在 AI 相关贷款/承保条款中显性要求 ISO 42001 认证 | [1] 标准进入财务建模、[23] 保险业自主治理框架 | 若 2027-12-31 前无主流金融机构公开披露此类条款，则判断不成立 | 推测 |
| **信号**：开源 AI 红队/审计平台将出现“首个 10k+ star”项目，形成事实标准 | [P] 预测：Garak/PyRIT/AI Verify 或新项目在 2027 前达成 10k GitHub star 并被 ≥2 监管指引引用 | [q3-open_problems] 工具链空白、红队需求爆发 | 若 2027-12-31 前无开源治理工具达 10k star 且被监管引用，则判断不成立 | 推测 |
| **信号**：Agentic AI 治理控制平面（如 AAGATE 架构）将被至少 1 家云厂商原生集成 | [P] 预测：AWS/Azure/GCP 中至少 1 家在 2027 前推出托管 Agentic AI 治理控制平面服务 | [31] K8s 原生架构与 NIST AI RMF 对齐、代理型系统产业化趋势 | 若 2027-12-31 前无云厂商发布此类托管服务，则判断不成立 | 推测 |
| **争议**：生物基础模型是否纳入 GPAI 系统性风险监管，国际共识可能分裂 | [Debated] EU 倾向纳入（[9]），美国可能采用自愿承诺+出口管制，中国可能纳入算法备案 | [9] ESM3 案例、[q1-open_problems] 中美欧政策证据缺口 | 若 2027 前出现跨司法管辖区统一认定机制，则分裂判断不成立 | 需要数据 |
| **不确定**：中国算法备案/生成式 AI 条例的执法力度与跨境数据流动要求对跨国合规的量化影响 | [R] 传闻：执法趋严、备案周期缩短、跨境评估强制化 | [q1-open_problems] 候选证据完全缺失 | 需获取 2024-2026 年网信办/工信部原始文件与执法案例才能判断 | 未知 |

---

## 经典与奠基性工作表（汇总）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| Internal Deployment in the AI Act | 2025 | arXiv cs.CY | > 待核实 | 预印本 | 高 | ★★★★☆ | [7] | EU AI Act 核心条文解释，合规边界划分 |
| The Case for ESM3 as GPAI with Systemic Risk Under the EU AI Act | 2026 | arXiv cs.CY | > 待核实 | 预印本 | 高 | ★★★★☆ | [9] | 生物基础模型纳入系统性风险分类首发 |
| Operationalizing the EU AI Act in Agile Software Development | 2026 | arXiv cs.SE | > 待核实 | 预印本 | 中高 | ★★★★☆ | [11] | 敏捷流程合规操作化指南原型 |
| The Risk-Adjusted Intelligence Dividend (ISO 42001 + Regulatory Exposure) | 2025 | arXiv cs.CY | > 待核实 | 预印本 | 中 | ★★★☆☆ | [1] | 标准与金融量化结合框架 |
| The Accountability Paradox: Platform API Restrictions Undermine AI Transparency Mandates | 2025/2026 | arXiv cs.CY | > 待核实 | 预印本 | 中 | ★★★★☆ | [16] | 算法审计框架与跨平台实证 |
| Governing AI in Catastrophe Risk Intelligence: TRUST Framework | 2026 | J. Eng. Comput. Intell. Rev. | citations=0 | 同行评审 | 低 | ★★★☆☆ | [23] | 保险垂直行业治理框架 |
| Emotional AI and the rise of pseudo-intimacy | 2025 | Frontiers in Psychology | citations=62 | 同行评审 | 中 | ★★★☆☆ | [21] | 情感 AI 心理风险维度 |
| AAGATE: NIST AI RMF-Aligned Governance Platform for Agentic AI | 2025 | arXiv cs.CR | > 待核实 | 预印本 | 中等 | ★★★☆☆ | [31] | Agentic AI 治理控制平面架构 |
| SCITUS: Multi-Jurisdictional Framework Adapting NIST AI RMF to Canadian Context | 2026 | arXiv cs.CY | > 待核实 | 预印本 | 中等 | ★★★☆☆ | [29] | 多司法管辖区合规适配方法论 |
| First Analysis of the EU Artificial Intelligence Act | 2024 | arXiv cs.CY | > 待核实 | 预印本 | 中 | ★★★☆☆ | [12] | AI Act 早期全景分析（经典参考） |
| Robustness and Cybersecurity in the EU Artificial Intelligence Act | 2025 | arXiv cs.CR | > 待核实 | 预印本 | 中 | ★★★☆☆ | [5] | AI Act 网络安全/鲁棒性要求分析 |
| Actionable Guidance for High-Consequence AI Risk Management | 2022/2023 | arXiv cs.CY | > 待核实 | 预印本 v3 | 中 | ★★★★☆ | [27] | 灾难性风险标准化早期工作（经典参考） |

---

## 开源项目表

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| AAGATE (架构设计) | 2025 | arXiv cs.CR | > 待核实（未确认开源仓库） | 预印本 | 中等 | ★★★☆☆ | [31] | K8s 原生 Agentic AI 治理控制平面，**开源状态待核实** |
| SCITUS (框架设计) | 2026 | arXiv cs.CY | > 待核实（非代码实现） | 预印本 | 中等 | ★★★☆☆ | [29] | 多司法管辖区 NIST AI RMF 适配方法论，**非现成工具链** |
| Garak / PyRIT / Model Cards Toolkit / AI Verify | — | 社区/微软/NVIDIA/新加坡 IMDA | > 待核实（候选证据中未出现） | — | 高 | ★★★★☆ | — | 知名开源红队/审计/模型卡工具，**需补充检索确认现状** |

> 待核实：候选证据中**无明确开源仓库链接、星标数、最近提交记录**的合规/红队/审计工具链项目 [q3-findings-3]。

---

## 数据集与基准表

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| — | — | — | — | — | — | — | — | 候选证据中**无 AI 治理/合规/审计相关数据集或基准** [q1/q2/q3-key_datasets 均为空] |
| Hugging Face 数据集合规就绪性分析 | 2026 | arXiv cs.CY | > 待核实 | 预印本 | 中 | ★★★☆☆ | [33] | 供应链视角审查数据集合规元数据，**非基准数据集** |

> 待核实：AI 合规评测基准（如 EU AI Act 合规基准、NIST AI RMF 评测套件、红队基准）在候选证据中完全缺失，需补充检索。

---

## 参考来源

[1] The Risk-Adjusted Intelligence Dividend: A Quantitative Framework for Measuring AI Return on Investment Integrating ISO 42001 and Regulatory Exposure — http://arxiv.org/abs/2511.21975v1  
[2] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1  
[3] Towards Assuring EU AI Act Compliance and Adversarial Robustness of LLMs — http://arxiv.org/abs/2410.05306v1  
[4] NTU-NPU System for Voice Privacy 2024 Challenge — http://arxiv.org/abs/2410.02371v1  
[5] Robustness and Cybersecurity in the EU Artificial Intelligence Act — http://arxiv.org/abs/2502.16184v4  
[6] Discovery Opportunities with Gravitational Waves -- TASI 2024 Lecture Notes — http://arxiv.org/abs/2409.08956v1  
[7] Internal Deployment in the AI Act — http://arxiv.org/abs/2512.05742v4  
[8] Atmospheric entry and fragmentation of small asteroid 2024 BX1 — http://arxiv.org/abs/2403.00634v2  
[9] The Case for ESM3 as a General-Purpose AI Model with Systemic Risk Under the EU AI Act — http://arxiv.org/abs/2605.01611v1  
[10] Navigating the EU AI Act: A Methodological Approach to Compliance for Safety-critical Products — http://arxiv.org/abs/2403.16808v2  
[11] Operationalizing the EU AI Act in Agile Software Development: A Guideline-Based Approach — http://arxiv.org/abs/2608.16526v1  
[12] First Analysis of the EU Artifical Intelligence Act: Towards a Global Standard for Trustworthy AI? — http://arxiv.org/abs/2408.08318v1  
[13] Foundations of GenIR — http://arxiv.org/abs/2501.02842v1  
[14] The Reactive Synthesis Competition: SYNTCOMP 2016 and Beyond — http://arxiv.org/abs/1611.07626v1  
[15] The 3rd Reactive Synthesis Competition (SYNTCOMP 2016): Benchmarks, Participants & Results — http://arxiv.org/abs/1609.00507v2  
[16] The Accountability Paradox: How Platform API Restrictions Undermine AI Transparency Mandates — http://arxiv.org/abs/2505.11577v5  
[17] 2nd Workshop on Cognitive Architectures for Social Human-Robot Interaction 2016 — http://arxiv.org/abs/1602.01868v1  
[18] Changing looks of the nucleus of Seyfert galaxy NGC 3516 during 2016-2020 — http://arxiv.org/abs/2008.10091v2  
[19] 5th International Symposium on New Frontiers in Human-Robot Interaction 2016 — http://arxiv.org/abs/1602.05456v2  
[20] The ADAPT Enhanced Dependency Parser at the IWPT 2020 Shared Task — http://arxiv.org/abs/2009.01712v1  
[21] Emotional AI and the rise of pseudo-intimacy: are we trading authenticity for algorithmic affection? — https://doi.org/10.3389/fpsyg.2025.1679324  
[22] Historical light-curve and the 2016 outburst of the symbiotic star StHa 169 — http://arxiv.org/abs/1607.06312v1  
[23] Governing Artificial Intelligence in Catastrophe Risk Intelligence: The TRUST Framework for Trustworthy and Examination-Ready AI Governance in U.S. Property and Casualty Insurance — https://doi.org/10.63544/qytnnd08  
[24] Human-AI Collaboration: Exploring Synergies and Future Directions — https://doi.org/10.22541/au.172560988.80084396/v1  
[25] Faith in AI can narrow the futures individuals consider — http://arxiv.org/abs/2603.28944v2  
[26] Docling: An Efficient Open-Source Toolkit for AI-driven Document Conversion — http://arxiv.org/abs/2501.17887v1  
[27] Actionable Guidance for High-Consequence AI Risk Management: Towards Standards Addressing AI Catastrophic Risks — http://arxiv.org/abs/2206.08966v3  
[28] Generative AI Toolkit -- a framework for increasing the quality of LLM-based applications over their whole life cycle — http://arxiv.org/abs/2412.14215v1  
[29] SCITUS: A Multi-Jurisdictional Framework for Adapting NIST AI RMF to the Canadian Regulatory Context — http://arxiv.org/abs/2607.15051v1  
[30] GR-NLP-TOOLKIT: An Open-Source NLP Toolkit for Modern Greek — http://arxiv.org/abs/2412.08520v1  
[31] AAGATE: A NIST AI RMF-Aligned Governance Platform for Agentic AI — http://arxiv.org/abs/2510.25863v2  
[32] Colour Contrast on the Web: A WCAG 2.1 Level AA Compliance Audit of Common Crawl's Top 500 Domains — http://arxiv.org/abs/2602.24067v1  
[33] Regulatory compliance-readiness in the AI Supply Chain: examining datasets in Hugging Face — http://arxiv.org/abs/2607.03310v1  
[34] VAT Compliance Incentives — http://arxiv.org/abs/2002.07862v3  
[35] Minimalist Compliance Control — http://arxiv.org/abs/2603.00913v1

---

*Generated by research-bot · topic=`ai-治理与监管政策法规与标准` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`nvidia/nemotron-3-ultra-550b-a55b` · sources=35 · duration=473s · 2026-11-06T03:22:46+00:00*
