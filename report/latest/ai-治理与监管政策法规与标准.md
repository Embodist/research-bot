# 全球 AI 治理与监管：政策法规演进、标准制定与工程落地深度调研报告

**日期**：2026-11-18 | **领域**：AI Governance & Regulation (Policy, Regulation, Standards) | **检索源数量**：35 条可引用证据源

---

## 1. 进展与热点

### 1.1 EU AI Act 落地层面的核心增量：高风险要求与风险分类学的映射缺口
最新研究系统分析了 EU AI Act 高风险要求隐性覆盖的风险源，发现其与既定风险分类学（如 ISO/IEC 23894、NIST AI RMF）之间**缺乏明确映射关系**，导致从业者难以将合规义务与风险管理实践协同 [1]。这是合规工程落地的关键痛点。**热度证据**：arXiv 预印本 (2026-09-11)，引用数待核实 [1]；**权威证据**：arXiv preprint (cs.AI)，未经同行评审 [1]；**关注度**：中，切中合规落地痛点 [1]；**推荐度**：★★★☆☆，框架性贡献明确，待同行评审与实务验证 [1]。

### 1.2 医疗 AI 产品化面临的高风险合规实证成本
通过工伤风险预测与阿尔茨海默病风险预测两个案例研究，证实此类医疗 AI 工具被归类为高风险系统，合规要求涉及数据治理、透明度、人工监督、准确性/鲁棒性/网络安全等多维义务，研发到生产的**合规成本显著** [2]。**热度证据**：arXiv 预印本 (2026-07)，BAI'26 会议论文 [2]；**权威证据**：arXiv preprint (cs.CY)，会议预印本 [2]；**关注度**：中，医疗 AI 落地团队直接参考 [2]；**推荐度**：★★★☆☆，案例细节丰富但样本极小 (n=2)，泛化性待验证 [2]。

### 1.3 前沿生物基础模型 (ESM3) 触发 GPAI 系统性风险条款的法律适用性分析
论文将 ESM3 映射至生物风险链，分析其在 EU AI Act 第 51 条（训练算力 >10^25 FLOPs 或同等能力）下的定性，建议提供方主动承担系统性风险 GPAI 合规责任 [3]。**热度证据**：arXiv 预印本 (2026-05) [3]；**权威证据**：arXiv preprint (cs.CY) [3]；**关注度**：中，生物 AI 治理早期法律讨论 [3]；**推荐度**：★★★☆☆，拓展《AI Act》适用边界，结论基于文本解释非监管指引 [3]。

### 1.4 “内部部署” 纳入监管范围的法律解释歧义
基于第 2 条、第 3 条等条款，梳理了企业内部使用的 AI 系统是否属于“投放市场”或“投入使用”的多条解释路径，为合规策略提供选项 [4]。**热度证据**：arXiv 预印本 v4 (2025-12-05) [4]；**权威证据**：arXiv preprint (cs.CY) [4]；**关注度**：中，适用范围核心灰色地带 [4]；**推荐度**：★★★☆☆，法律解释框架完整，无权威裁决效力 [4]。

### 1.5 AI 治理理论框架的最新演进：风险调整 ROI、风险缓解分类学、部署保障与机器身份治理
- **风险调整智能红利**：提出整合 ISO 42001 与监管敞口的量化 ROI 框架 [5]。
- **AI 风险缓解映射**：构建初步 AI Risk Mitigation Taxonomy，解决术语不一致与覆盖缺口 [6]。
- **运营级部署保障**：从静态指标转向阈值敏感的治理状态编排框架 [7]。
- **机器身份治理分类学 (MIGT)**：填补 AI Agent/Service Account/API Token 跨边界治理的盲区 [8]。
**热度证据**：均为 2025-2026 年 arXiv 预印本 (cs.CY/cs.AI/cs.CR) [5][6][7][8]；**权威证据**：预印本，未经同行评审 [5][6][7][8]；**关注度**：中，理论前沿活跃但工程落地验证缺失 [5][6][7][8]；**推荐度**：★★★★☆，提供结构化理论骨干，需实证研究跟进 [5][6][7][8]。

### 1.6 红队测试工程化进展：面向搜索增强 LLM 的 Knowledge-to-Action 威胁框架
SearchAttack 框架针对在线网页搜索场景下的 RAG/LLM 红队测试，指出搜索返回内容可能直接包含有害载荷 [9]。**热度证据**：arXiv 预印本 v2 (2026-01) [9]；**权威证据**：arXiv preprint (cs.CL) [9]；**关注度**：中，RAG 安全新兴方向 [9]；**推荐度**：★★★☆☆，切中场景需求，但未见开源代码与采用度证据 [9]。

> 待核实：US (NIST AI RMF 进展、行政命令落地、州立法)、China (算法备案实施细则、标准体系)、UK (白皮书后续、DSIT 推进)、G7/OECD (广岛进程行为准则落地、原则更新) 在 2024-2026 年的最新立法、行政指令、技术标准实质性进展。现有证据源未覆盖上述司法管辖区的一手官方进展 [1][2][3][4][5][6][7][8][9]。

---

## 2. 工业界与产品

### 2.1 合规自动化工具链与评估基准的市场成熟度现状
现有证据显示，**高风险 AI 系统合规的工程化工具链、评估基准、第三方认证市场成熟度缺乏系统性调研** [1]。NIST AI RMF 官方框架存在 [10]，但其在企业级落地的工具化程度（如自动化映射、持续监控）缺乏公开量化数据 [10][11]。

### 2.2 红队测试与对抗鲁棒性工具的开源生态
- **SearchAttack**：针对搜索增强 LLM 的红队框架，处于预印本阶段，未见开源仓库与社区采用度证据 [9]。
- **Mind the Gap**：对比模型级与 Agent 级红队测试，引入 Action-Graph 可观测性，验证于 GPT-OSS-20B [12]。
- **Red Teaming at Scale**：针对数学任务幻觉的大规模红队方法 [13]。
**热度证据**：均为 arXiv 预印本，GitHub Star/下载量待核实 [13][9][12]；**权威证据**：预印本/会议论文 [13][9][12]；**关注度**：中，学术端活跃，工业界采用度不确定 [13][9][12]；**推荐度**：★★★☆☆，方法论有参考，工程化交付物缺失 [13][9][12]。

### 2.3 模型卡/数据卡生成与 AI 审计工具链
- **Unlocking Model Insights**：面向自动化 Model Card 生成的数据集 [14]。
- **Towards AI Accountability Infrastructure**：系统梳理 AI Audit Tooling 的缺口与机会，指出现有工具多为事后审计，缺乏运行时治理集成 [15]。
**热度证据**：[14] 数据集论文 (2023)；[15] 综述性预印本 v3 (2024-02) [15][14]；**权威证据**：arXiv 预印本 [15][14]；**关注度**：中，审计基础设施建设的关键参考 [15]；**推荐度**：★★★★☆，[15] 为工具选型提供全景缺口分析 [15]。

### 2.4 法律零日漏洞与对抗鲁棒性合规一体化
Legal Zero-Days 概念提出高级 AI 系统面临的新型法律风险向量 [16]；Towards Assuring EU AI Act Compliance and Adversarial Robustness 探讨合规与对抗鲁棒性的协同保障 [17]。
**热度证据**：arXiv 预印本 [17][16]；**权威证据**：预印本 [17][16]；**关注度**：低-中，前沿概念验证阶段 [17][16]；**推荐度**：★★★☆☆，跨学科视角有价值，落地路径不明 [17][16]。

> 待核实：主流云厂商、合规 SaaS 厂商、专业审计机构的具体产品矩阵、客户案例、定价模型与市场份额。现有证据源无工业界一手产品数据 [1][17][15][16][14][13][9][12]。

---

## 3. 蓝海与缺口

| 蓝海/缺口维度 | 具体描述 | 证据支撑 | 优先级 |
|--------------|----------|----------|--------|
| **跨司法管辖区合规互认与数据跨境协调机制** | EU-US TTC、G7 互认等实质性进展缺乏公开证据；多司法管辖区合规映射工具缺失 | [1] 明确列为 open problem | ★★★★★ |
| **EU AI Act 实施细则工程化落地** | 实施法案、协调标准、公告机构指定的最新进度与官方时间表缺乏一手来源确认 | [1] | ★★★★★ |
| **GPAI 系统性风险阈值操作化** | 算力阈值 (>10^25 FLOPs) 与能力评估方法的具体标准尚未由 AI Office 最终确定 | [1][3] | ★★★★★ |
| **高风险 AI 合规工程化工具链** | 从风险分类映射、证据收集、技术文档自动生成到持续监控的端到端工具链空白 | [1][15] | ★★★★★ |
| **内部部署合规策略确定性** | 企业内部 AI 系统是否触发义务缺乏权威裁决，合规策略面临多路径不确定性 | [4] | ★★★★☆ |
| **机器身份治理 (MIGT) 工程实现** | AI Agent/Service Account/API Token 跨边界生命周期管理、最小权限执行、审计追踪的基础设施缺失 | [8] | ★★★★☆ |
| **医疗/高风险垂直域合规加速器** | 针对特定高风险场景 (医疗、金融、关键基础设施) 的合规模板、测试基准、证据包自动生成 | [2] | ★★★★☆ |
| **红队测试标准化与基准化** | 缺乏跨模型、跨任务、跨攻击面的标准化红队评测基准与比较框架 | [13][9][12] | ★★★☆☆ |

---

## 4. 瓶颈与拐点

### 4.1 风险分类学碎片化与映射瓶颈
ISO/IEC 23894、NIST AI RMF、EU AI Act 高风险要求、OECD 分类体系并存，**术语不一致、覆盖有缺口、映射关系不明**，导致合规与风险管理难以协同 [1][6]。**拐点信号**：Mapping AI Risk Mitigations 工作尝试构建统一 Taxonomy [6]，若获国际标准组织 (ISO/IEC JTC 1/SC 42) 采纳，将成关键拐点。**热度证据**：[6] arXiv 预印本；**权威证据**：预印本；**关注度**：中；**推荐度**：★★★★☆。

### 4.2 高风险 AI 合规成本与创新速度的结构性矛盾
医疗 AI 案例显示，数据治理、透明度、人工监督、鲁棒性测试等义务使研发到生产周期显著拉长 [2]。**拐点信号**：若协调标准 (Harmonised Standards) 能提供“合规即代码” 的技术规范 (如自动化测试套件、证据模板)，可大幅降低边际合规成本。**热度证据**：[2] 案例研究；**权威证据**：预印本；**关注度**：中；**推荐度**：★★★☆☆。

### 4.3 机器身份爆发式增长与治理基础设施滞后
企业环境中机器身份 (AI Agent, Service Account, API Token) 与人类身份比例超 80:1，但**无一体化治理框架** [8]。**拐点信号**：MIGT 提出分类学 [8]，若结合 SPIFFE/SPIRE、Zero Trust 架构落地工程化，将成身份安全新蓝海。**热度证据**：[8] arXiv 预印本；**权威证据**：预印本；**关注度**：中；**推荐度**：★★★★☆。

### 4.4 法律零日漏洞：监管滞后于技术能力跃迁
Legal Zero-Days 指出先进 AI 系统能力跃迁可能绕过现有法律定义与责任归属机制 [16]。**拐点信号**：需建立“技术能力监测-法律动态解释-监管沙箱验证” 的快速响应机制。**热度证据**：[16] arXiv 预印本；**权威证据**：预印本；**关注度**：低；**推荐度**：★★★☆☆。

### 4.5 审计工具链从“事后静态”向“运行时动态”转型的工程鸿沟
现有 AI Audit Tooling 多为事后指标报告、仪表盘，缺乏直接治理运行时行为的编排能力 [15][7]。**拐点信号**：Operational AI Deployment Assurance 提出阈值敏感的治理状态编排 [7]，若与 eBPF、Service Mesh、Policy Engine (OPA) 融合，可实现运行时强制合规。**热度证据**：[15][7] 预印本；**权威证据**：预印本；**关注度**：中；**推荐度**：★★★★☆。

---

## 5. 社会·政策·国际

### 5.1 EU AI Act 作为全球合规基准的“布鲁塞尔效应”持续发酵
EU AI Act 的域外适用性、高风险分类体系、GPAI 系统性风险条款，正成为跨国企业合规基线的事实标准 [1][2][3][4]。**热度证据**：多篇预印本聚焦 EU AI Act 细节 [1][2][3][4]；**权威证据**：预印本分析，非官方指引；**关注度**：高，学术与法务关注度高；**推荐度**：★★★★☆。

### 5.2 美国联邦与州层面立法碎片化加剧
> 待核实：NIST AI RMF 2.0/跨部门实施进展、拜登行政命令 (EO 14110) 后续执行报告、加州 SB 1047 等州级立法最新状态、联邦两党 AI 法案推进情况。现有证据源仅含 NIST 官网链接 [10] 及应用案例 [11]，无 2024-2026 年实质性进展一手确认。

### 5.3 中国算法备案与生成式 AI 管理实施细则的工程化要求
> 待核实：网信办算法备案最新批次、生成式 AI 服务备案实施细则、TC260/全国 AI 标准化总体组最新标准发布目录、跨境数据流动与 AI 治理协调机制进展。现有证据源无覆盖。

### 5.4 UK “创新友好型”监管模式与 DSIT 推进实况
> 待核实：AI 监管白皮书后续咨询结果、DSIT 监管沙箱进展、与 EU/US 互认谈判进展。现有证据源无覆盖。

### 5.5 G7 广岛进程与 OECD AI 原则的操作化落地
> 待核实：G7 行为准则企业签署情况、监管互认试点、OECD AI 原则 2024/2025 更新内容、事件报告机制建设。现有证据源无覆盖。

---

## 6. 资本与生态

### 6.1 合规技术赛道投融资信号微弱，缺乏系统性披露
现有证据源**无任何融资、并购、独角兽企业、市场规模测算数据** [1][2][17][3][4][5][6][15][7][8][16][10][11][14][13][9][12]。**热度证据**：无；**权威证据**：无；**关注度**：低；**推荐度**：★☆☆☆☆。

### 6.2 开源社区活跃度集中在红队/评测基准层，合规工程化项目稀缺
- 活跃：Red Teaming (SearchAttack [9], Mind the Gap [12], Math Red Teaming [13])、Model Card 数据集 [14]、Audit Tooling 综述 [15]。
- 稀缺：EU AI Act 合规自动化、ISO 42001 认证证据链工具、GPAI 系统性风险评估平台、跨司法管辖区合规映射引擎。
**热度证据**：GitHub Star/贡献者数待核实 [14][13][9][12]；**权威证据**：arXiv 预印本/数据集论文 [14][13][9][12]；**关注度**：中；**推荐度**：★★★☆☆。

### 6.3 人才流动与技能缺口：法律-工程复合型人才极度短缺
> 待核实：招聘薪资趋势、高校课程设置、专业认证体系 (如 IAPP AIGP)、咨询巨头 (Big4/专业合规咨询) 业务增长数据。现有证据源无覆盖。

---

## 7. 信号与预测

| 信号/预测 | 依据链 | 可证伪假设 | 置信度 | 标记 |
|-----------|--------|------------|--------|------|
| **协调标准 (Harmonised Standards) 将于 2026-2027 陆续发布，触发合规工具链爆发式增长** | EU AI Act 生效时间表、CEN/CENELEC JTC 21 标准化工作计划、高风险合规成本痛点 [1][2] | 若至 2027-12 仍无核心高风险类别 (Annex III) 协调标准发布，则判断失效 | 较大概率 | [P] |
| **GPAI 系统性风险阈值将从纯算力 (>10^25 FLOPs) 转向“算力+能力评估”双轨制** | AI Office 咨询进展、ESM3 等前沿模型案例讨论 [3]、学术界对算力代理指标局限性共识 | 若 AI Office 最终指引仅保留算力阈值，则判断失效 | 推测 | [P] |
| **“合规即代码” 成为合规 SaaS 核心竞争力，推动 Policy-as-Code 标准化** | NIST AI RMF Playbook [10]、Operational Deployment Assurance 框架 [7]、MIGT 需求 [8] | 若 2028 年主流合规平台仍以文档/表单为主交付，则判断失效 | 推测 | [P] |
| **机器身份治理 (MIGT) 将并入 Zero Trust/身份安全主赛道，催生专用 PAM/IGA 扩展品类** | 机器身份量级超人类 80:1 [8]、SPIFFE/SPIRE 生态成熟、AI Agent 爆发 | 若 2027 年主流 IGA/PAM 厂商无 AI Agent 生命周期管理功能发布，则判断失效 | 较大概率 | [P] |
| **跨司法管辖区合规互认将从“原则共识”推进至“技术互操作” (可验证凭证/可信任务执行环境)** | EU-US TTC、G7 广岛进程、数据自由流动与信任 (DFFT) 倡议 | 若 2028 无双边/多边技术互认试点上线，则判断失效 | 推测 | [P] |
| **红队测试标准化将输出 ISO/IEC 标准 (如 ISO/IEC 42001 扩展)，并纳入高风险 AI 合规强制要求** | 红队学术爆发 [13][9][12]、NIST AI RMF Measure 功能 [10]、EU AI Act 第 55 条测试义务 | 若 ISO/IEC JTC 1/SC 42 2027 无红队标准立项，则判断失效 | 推测 | [P] |
| **法律零日漏洞将催生“监管科技监管沙箱”常态化机制，监管机构引入技术能力监测雷达** | Legal Zero-Days 概念 [16]、前沿模型能力跃迁速度、监管滞后性 | 若主要司法管辖区 (EU/US/UK) 2027 无常态化技术监测机制公开运行，则判断失效 | 推测 | [P] |

> 不确定：上述预测高度依赖政策窗口期、地缘政治变量、算力供给曲线与范式突破节奏，存在显著不确定性。需持续追踪官方立法进程、标准化会议纪要、头部实验室能力发布、资本市场一级交易信号。

---

## 经典与奠基性工作

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| NIST AI Risk Management Framework (AI RMF 1.0) | 2023 | NIST | 高 (官方标准、广泛引用) | 官方标准文档 | 高 | ★★★★★ | [10] | 美国联邦层面 AI 风险管理基石，提供 Map/Measure/Manage/Govern 四功能 |
| ISO/IEC 42001:2023 AI Management System | 2023 | ISO/IEC JTC 1/SC 42 | 高 (国际标准、可认证) | 国际标准 | 高 | ★★★★★ | > 待核实 | 可认证的 AI 管理体系标准，合规工程化核心依据 |
| EU AI Act (Regulation (EU) 2024/1689) | 2024 | European Commission/Parliament | 极高 (法规、强制力) | 正式法规 | 极高 | ★★★★★ | > 待核实 | 全球首部综合性 AI 法规，域外适用，高风险/GPAI 核心条款 |
| OECD AI Principles (Updated 2024) | 2024 | OECD | 高 (政府间共识) | 政府间组织文件 | 高 | ★★★★☆ | > 待核实 | 价值观本位原则，影响全球立法基调 |
| G7 Hiroshima Process International Code of Conduct | 2023 | G7 | 高 (政治承诺) | 政府间声明 | 高 | ★★★★☆ | > 待核实 | 先进 AI 系统开发者行为准则，自愿性但具政治约束力 |
| Towards AI Accountability Infrastructure: Gaps and Opportunities in AI Audit Tooling | 2024 | Raji et al. | 中 (引用增长中) | arXiv preprint v3 | 中 | ★★★★☆ | [15] | 系统梳理审计工具缺口，工具选型参考 |
| Mapping AI Risk Mitigations: Evidence Scan and Preliminary AI Risk Mitigation Taxonomy | 2025 | NIST/合作者 | 中 (新预印本) | arXiv preprint | 中 | ★★★★☆ | [6] | 统一风险缓解术语与分类学尝试 |
| Operational AI Deployment Assurance: Governance-State Orchestration | 2026 | 作者组 | 低 (新预印本) | arXiv preprint | 中 | ★★★★☆ | [7] | 运行时治理编排框架，从静态转动态 |
| Who Governs the Machine? MIGT | 2026 | 作者组 | 低 (新预印本) | arXiv preprint | 中 | ★★★★☆ | [8] | 机器身份治理盲点填补 |
| From Legal Text to AI-specific Risk Sources | 2026 | 作者组 | 低 (新预印本) | arXiv preprint | 中 | ★★★☆☆ | [1] | EU AI Act 高风险要求到风险源的系统映射 |

---

## 开源项目与工程工具

| 名称 | 年份 | 机构/作者 | 热度 (Stars/Contributors) | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|---------------------------|------|--------|--------|------|------|
| SearchAttack | 2026 | 作者组 | > 待核实 | arXiv preprint | 中 | ★★★☆☆ | [9] | 搜索增强 LLM 红队框架，针对 Knowledge-to-Action 威胁 |
| Mind the Gap (Agentic Red Teaming) | 2025 | 作者组 | > 待核实 | arXiv preprint | 中 | ★★★☆☆ | [12] | 模型级 vs Agent 级红队对比，Action-Graph 可观测性 |
| Red Teaming for LLMs at Scale (Math) | 2024 | 作者组 | > 待核实 | arXiv preprint | 中 | ★★★☆☆ | [13] | 数学任务幻觉大规模红队方法 |
| Unlocking Model Insights (Model Card Dataset) | 2023 | 作者组 | > 待核实 | arXiv preprint | 中 | ★★★☆☆ | [14] | 自动化 Model Card 生成数据集 |
| NIST AI RMF Playbook / Crosswalks | 2023- | NIST | 官方维护 | 官方资源 | 高 | ★★★★★ | [10] | AI RMF 落地指南、与其他框架映射表 |

---

## 数据集与基准

| 名称 | 年份 | 机构/作者 | 热度 (下载/引用) | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------------------|------|--------|--------|------|------|
| Unlocking Model Insights Dataset | 2023 | 作者组 | > 待核实 | arXiv preprint | 中 | ★★★☆☆ | [14] | Model Card 自动生成基准数据集 |
| AI Audit Tooling Landscape (隐性数据集) | 2024 | Raji et al. | > 待核实 | arXiv preprint | 中 | ★★★★☆ | [15] | 审计工具分类与缺口分析的底层调研数据 |
| NIST AI RMF Case Studies / Profiles | 2023- | NIST/社区 | > 待核实 | 官方发布 | 中 | ★★★★☆ | [10][11] | 监控技术应用案例等 |

---

## 参考来源
[1] From Legal Text to AI-specific Risk Sources: A Systematic Analysis of the EU AI Act's High-Risk Requirements — http://arxiv.org/abs/2609.13535v1
[2] Ethics and EU AI Act in Cases of Work Disability Risk and Alzheimer's Disease Risk Prediction — http://arxiv.org/abs/2607.05402v1
[3] The Case for ESM3 as a General-Purpose AI Model with Systemic Risk Under the EU AI Act — http://arxiv.org/abs/2605.01611v1
[4] Internal Deployment in the AI Act — http://arxiv.org/abs/2512.05742v4
[5] The Risk-Adjusted Intelligence Dividend: A Quantitative Framework for Measuring AI Return on Investment Integrating ISO 42001 and Regulatory Exposure — http://arxiv.org/abs/2511.21975v1
[6] Mapping AI Risk Mitigations: Evidence Scan and Preliminary AI Risk Mitigation Taxonomy — http://arxiv.org/abs/2512.11931v1
[7] Operational AI Deployment Assurance: Governance-State Orchestration Under Threshold-Sensitive Deployment Conditions -- A Governance Framework for High-Stakes AI Systems — http://arxiv.org/abs/2605.27827v1
[8] Who Governs the Machine? A Machine Identity Governance Taxonomy (MIGT) for AI Systems Operating Across Enterprise and Geopolitical Boundaries — http://arxiv.org/abs/2604.06148v1
[9] SearchAttack: Red-Teaming LLMs against Knowledge-to-Action Threats under Online Web Search — http://arxiv.org/abs/2601.04093v2
[10] AI Risk Management Framework - NIST — https://www.nist.gov/itl/ai-risk-management-framework
[11] Application of the NIST AI Risk Management Framework to Surveillance Technology — http://arxiv.org/abs/2403.15646v1
[12] Mind the Gap: Comparing Model- vs Agentic-Level Red Teaming with Action-Graph Observability on GPT-OSS-20B — http://arxiv.org/abs/2509.17259v1
[13] Red Teaming for Large Language Models At Scale: Tackling Hallucinations on Mathematics Tasks — http://arxiv.org/abs/2401.00290v1
[14] Unlocking Model Insights: A Dataset for Automated Model Card Generation — http://arxiv.org/abs/2309.12616v1
[15] Towards AI Accountability Infrastructure: Gaps and Opportunities in AI Audit Tooling — http://arxiv.org/abs/2402.17861v3
[16] Legal Zero-Days: A Novel Risk Vector for Advanced AI Systems — http://arxiv.org/abs/2508.10050v1
[17] Towards Assuring EU AI Act Compliance and Adversarial Robustness of LLMs — http://arxiv.org/abs/2410.05306v1

---

*Generated by research-bot · topic=`ai-治理与监管政策法规与标准` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`nvidia/nemotron-3-ultra-550b-a55b` · sources=35 · duration=526s · 2026-11-18T03:53:46+00:00*
