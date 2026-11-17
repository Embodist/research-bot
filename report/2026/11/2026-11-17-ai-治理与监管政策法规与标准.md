# AI 治理与监管：增量快照与蓝海机会图谱（2024-2026）

**日期**：2026-11-17 | **领域**：AI Governance & Regulation（政策、法规与标准） | **检索源数量**：34 条可引用证据（均为 arXiv 预印本或会议论文，无官方政府文件/标准组织正式发布文本）

---

## 1. 进展与热点（Progress & Hotspots）

> **一句话增量判断**：近 1-2 年学术界聚焦 **EU AI Act 的落地细化**（高风险分类映射、通用 AI 模型系统性风险认定、内部部署适用范围）、**Agentic AI 可信技术栈的标准化对齐**、以及 **智能体级红队测试工程化**；但均为预印本阶段，**缺乏官方指导文件、跨司法管辖区对比时间表、真机合规审计案例**等一手实施证据。

### 1.1 EU AI Act 高风险要求的结构化映射与合规落地分析
- **核心进展**：系统将 AI Act 高风险要求与既有风险分类法对齐，指出从业者缺乏将监管义务转化为结构化风险分类的操作依据 [1]。
- **证据四轴**：
  - 热度：> 待核实（arXiv 预印本 2026-09-11 提交，引用数暂不可得）  
  - 权威：arXiv preprint (cs.AI)，未经同行评审 [1]  
  - 关注度：中 —— 新提交预印本，聚焦监管合规技术实现，学术社区开始关注  
  - 推荐度：★★★☆☆ —— 方法论价值高，为合规工程提供结构化基础，但仅覆盖 EU 单一司法管辖区且为预印本 [1]

### 1.2 医疗 AI 工具被归类为高风险系统的实证案例
- **核心进展**：工作残疾风险预测与阿尔茨海默病风险预测两个医疗 AI 案例均被判定为高风险，从研究走向生产面临大量合规工作 [2]。
- **证据四轴**：
  - 热度：> 待核实（arXiv 预印本 2026-06-07 提交，BAI'26 会议论文）  
  - 权威：arXiv preprint (cs.CY) + BAI'26 会议，经会议评审 [2]  
  - 关注度：中 —— 医疗 AI 合规细分领域有参考价值  
  - 推荐度：★★★☆☆ —— 提供具体高风险分类案例，对医疗 AI 合规有参考，但样本仅两例 [2]

### 1.3 前沿生物基础模型（ESM3）的系统性风险法律定性
- **核心进展**：将 ESM3 映射至生物风险链，分析其是否触发 EU AI Act 对通用 AI 模型（GPAI）系统性风险义务，指出 Act 措辞存在歧义 [3]。
- **证据四轴**：
  - 热度：> 待核实（arXiv 预印本 2026-05-02 提交）  
  - 权威：arXiv preprint (cs.CY)，未经同行评审 [3]  
  - 关注度：低 —— 聚焦特定模型法律定性，受众较窄  
  - 推荐度：★★☆☆☆ —— 探讨 GPAI 系统性风险认定边界，但单一模型分析泛化有限 [3]

### 1.4 AI Act「内部部署」适用范围的解释学争议
- **核心进展**：对第 2 条第 1、6、8 款进行解释性路径分析，压力测试将内部部署纳入/排除适用范围的正反方论据 [4]。
- **证据四轴**：
  - 热度：> 待核实（arXiv 预印本 v4 2025-12-05 提交）  
  - 权威：arXiv preprint (cs.CY)，法律备忘录性质 [4]  
  - 关注度：低 —— 法律学者群体关注  
  - 推荐度：★★☆☆☆ —— 为合规法务提供解释路径，非实证研究 [4]

### 1.5 Agentic AI 可信度四维技术分类学（安全、鲁棒性、隐私、系统安全）
- **核心进展**：首个系统综述将 Agentic AI 多步轨迹引入的新失效模式拆解为 safety/robustness/privacy/system security 两维框架，直接对标 NIST RMF、ISO 42001 标准化需求 [5]。
- **证据四轴**：
  - 热度：> 待核实（arXiv 预印本 2026-05 提交）  
  - 权威：arXiv preprint (cs.AI)，综述类文献 [5]  
  - 关注度：高 —— 2026 年最新综述，覆盖 Agentic AI 治理热点，技术社区关注度高  
  - 推荐度：★★★★★ —— 系统梳理 Agentic AI 可信技术栈，为标准制定与合规工程提供技术映射表 [5]

### 1.6 智能体级红队测试框架 AgentSeer 与基准 HarmBench
- **核心进展**：提出 AgentSeer 将智能体系统分解为粒度动作，在 GPT-OSS-20B 上对比模型级与智能体级红队测试，使用 HarmBench 作为有害目标基准 [6]。
- **证据四轴**：
  - 热度：> 待核实（arXiv 预印本 2025-09 提交）  
  - 权威：arXiv preprint (cs.AI) [6]  
  - 关注度：高 —— 2025 年最新工作，针对智能体红队测试新兴工程需求  
  - 推荐度：★★★★★ —— 红队工具链前沿，给出具体框架名与基准，工程落地参考价值极高 [6]

### 1.7 红队测试方法论反思：宏观（全生命周期）与微观（模型级）双层框架
- **核心进展**：批评当前红队过度聚焦模型级漏洞，提出涵盖全开发生命周期的宏观红队与模型级微观红队综合框架 [7]。
- **证据四轴**：
  - 热度：> 待核实（arXiv 预印本 v2 2025-07 提交）  
  - 权威：arXiv preprint v2 (cs.AI)，经修订 [7]  
  - 关注度：中 —— 方法论反思性工作，适合作为合规 CI/CD 插件设计理论依据  
  - 推荐度：★★★★☆ —— 为合规工程中的红队集成提供架构级指导 [7]

### 1.8 数据集卡片生态大规模实证分析
- **核心进展**：对 Hugging Face 平台数据集卡片进行大规模分析，系统性理解当前数据文档实践现状与缺口 [8]。
- **证据四轴**：
  - 热度：> 待核实（arXiv 预印本 2024-01 提交）  
  - 权威：arXiv preprint (cs.LG) [8]  
  - 关注度：中 —— 数据治理社区常引用  
  - 推荐度：★★★★☆ —— 直接对应数据卡片工具链采用现状分析，权威性高 [8]

### 1.9 AI 生成文本检测共享任务基准（ALTA 2024）
- **核心进展**：面向人机混合文章的句级检测评测体系成熟，为水印/溯源 SDK 对抗鲁棒性评测提供参考 [9]。
- **证据四轴**：
  - 热度：> 待核实（arXiv 预印本 2024-12 提交，ALTA 共享任务官方概述）  
  - 权威：arXiv preprint (cs.CL)，共享任务官方文档 [9]  
  - 关注度：中 —— 检测基准常被引用  
  - 推荐度：★★★☆☆ —— 作为检测侧基准了解即可，与水印/溯源 SDK 直接关联较弱 [9]

---

## 2. 工业界与产品（Industry & Product）

> **一句话增量判断**：开源合规工程工具链呈现 **「文档层（数据卡片/模型卡片）有实证、红队层向智能体级延伸、检测层有共享任务、但水印/溯源 SDK 与审计日志标准缺位」** 的格局；**无厂商级合规 CI/CD 插件、跨云互操作性产品、真机部署审计案例** 的公开证据。

### 2.1 数据卡片工具链：Hugging Face 生态主导，但标准化采用度待量化
- **现状**：HF 数据集卡片已成事实标准，大规模实证揭示文档质量参差不齐 [8]。
- **缺口**：模型卡片工具链采用度缺乏同量级实证研究；CI/CD 集成最佳实践未形成共识 [q3-open_problems]。

### 2.2 红队测试工程化：从 PyRIT 到 AgentSeer 的演进
- **现有工具**：PyRIT（微软，生成式 AI 安全风险识别框架）[10]；AgentSeer（智能体级可观测性红队）[6]；HarmBench（有害目标基准）[6]。
- **产品化信号**：> 待核实 —— 无商业化红队 SaaS、CI/CD 原生插件、企业级审计报告模板的公开发布记录。

### 2.3 水印/溯源 SDK 与检测基准
- **现状**：ALTA 2024 共享任务提供句级检测基准 [9]；但**水印嵌入/验证 SDK 的跨厂商互操作性、鲁棒性基准缺失** [q3-open_problems]。

### 2.4 合规审计日志与 CI/CD 插件
- **现状**：**标准格式与最小必要字段集未达成行业共识** [q3-open_problems]；无开源合规 CI/CD 插件项目被检索到。

---

## 3. 蓝海与缺口（Blue Ocean & Gaps）

> **一句话增量判断**：**跨司法管辖区合规互认机制、真机部署层面的合规工程实践、Agentic AI 多步决策可审计性标准、水印/溯源互操作性协议** 为核心蓝海；当前研究高度集中于 EU AI Act 单一法域的学术解读，**美/中法规、ISO/IEC 标准、产业落地工具链** 三大维度近乎空白。

| 蓝海方向 | 具体缺口 | 证据支撑 |
|----------|----------|----------|
| **跨司法管辖区立法对比与互认** | 缺失：美国联邦/州级 AI 立法（EO 14110 后续）、中国《生成式 AI 服务管理暂行办法》进展、ISO/IEC 42001 最新版与实施时间表、中美欧三大司法管辖区立法进程对比时间表 | [q1-open_problems] |
| **官方一手权威来源** | 所有 34 条证据均为 arXiv 预印本/会议论文，**零** 官方政府文件、监管机构指导文件、标准组织正式发布文本 | [q1-open_problems] |
| **真机合规工程实践** | 无第三方独立评测、合规审计案例、跨司法管辖区互认机制等实施层面证据 | [q1-open_problems] |
| **Agentic AI 可审计性与事后问责** | 多步决策的可审计性在 AIA、GDPR 等现有法律框架下的落地细则仍缺乏共识 | [q2-open_problems] |
| **模型卡片标准化采用度** | 缺乏大规模实证研究 | [q3-open_problems] |
| **红队 CI/CD 自动化集成最佳实践** | 尚未形成共识 | [q3-open_problems] |
| **水印/溯源 SDK 鲁棒性与互操作性基准** | 缺乏跨厂商基准 | [q3-open_problems] |
| **合规审计日志标准格式** | 最小必要字段集未达成行业共识 | [q3-open_problems] |
| **EU AI Act 最终版与提案差异影响** | 2024/2025 最终通过版本对 2021 年提案文本解读的影响待追踪 | [q2-open_problems] |

---

## 4. 瓶颈与拐点（Bottleneck & Inflection）

> **一句话增量判断**：**「证据等级倒挂」（预印本主导、一手权威源缺失）、**「法域碎片化与工程落地脱节」**、**「Agentic AI 涌现行为超出现有风险分类法」** 为三大瓶颈；**拐点信号**包括：EU AI Act 高风险合规强制生效倒计时、NIST/ISO 标准发布节奏加快、智能体级红队基准从学术走向工业基准。

| 瓶颈维度 | 具体表现 | 证据支撑 | 拐点信号 |
|----------|----------|----------|----------|
| **证据等级倒挂** | 核心结论全赖 A/B 级缺失、B/C 级预印本支撑；无官方指导文件、审计案例 | [q1-open_problems] | 欧盟委员会发布合规指南、ISO/IEC 42001:2023 认证机构名单公布 |
| **法域碎片化** | 仅覆盖 EU AI Act 学术分析，美/中法规、国际标准完全缺位 | [q1-open_problems] | 美国 NIST AI RMF 1.0/2.0 迭代、中国国家标准立项公示 |
| **风险分类法滞后** | Agentic AI 多步轨迹引入新失效模式，现有高风险分类法覆盖不足 | [5] | AgentSeer/HarmBench 等智能体级基准被纳入标准化工作项 |
| **合规工程工具链断层** | 文档层有实证、红队层有框架、但水印/溯源/审计日志/CI/CD 插件全链路贯通产品缺失 | [q3-open_problems] | 主流 MLOps 平台（Vertex AI, MLflow, Kubeflow）原生集成合规检查点 |
| **内部部署范围不确定** | 第 2 条解释争议未决，企业合规边界模糊 | [4] | 欧盟委员会发布解释性指南或法院首例判决 |

---

## 5. 社会·政策·国际（Society, Policy & Geopolitics）

> **一句话增量判断**：**EU AI Act 成为全球 AI 监管话语的「参照基准」**，但**美/中/国际标准并行演进**导致合规成本指数级上升；**医疗/生物等高风险垂类**率先面临强制合规压力；**内部部署豁免争议**折射出监管边界与创新激励的博弈。

### 5.1 EU AI Act 的全球溢出效应
- **核心地位**：AIA 为首个主要经济体通用 AI 法律框架，其合格评定与上市后监管双机制成为后续治理讨论关键参考点 [11]。
- **实施时间表**：> 待核实 —— 缺乏官方生效/强制执行节点的权威时间表证据。

### 5.2 医疗 AI 与生物基础模型的差异化监管压力
- **医疗 AI**：工作残疾/阿尔茨海默风险预测工具被明确归类高风险，合规负担重 [2]。
- **生物基础模型**：ESM3 等前沿模型可能触发 GPAI 系统性风险义务，但 Act 措辞存在歧义 [3]。
- **社会影响**：高合规成本可能挤出中小创新主体，加剧「合规护城河」效应 [q1-findings 综合]。

### 5.3 国际标准化进程（ISO/IEC 42001 等）
- **现状**：**零证据覆盖** ISO/IEC 42001 最新版本、实施时间表、认证机构名单、与 EU AI Act 的协调机制 [q1-open_problems]。
- **地缘竞争**：> 待核实 —— 中美欧在 ISO/IEC JTC 1/SC 42 等标准组织中的提案博弈、互认谈判进展无公开可核查来源。

### 5.4 内部部署豁免争议的政策含义
- **争议核心**：第 2 条第 1、6、8 款对「内部部署」是否纳入适用范围存在正反方论据，直接影响企业私有化部署合规成本 [4]。
- **政策信号**：欧盟委员会后续指导文件或法院判例将成为拐点 [4]。

---

## 6. 资本与生态（Capital & Ecosystem）

> **一句话增量判断**：**学术预印本生态活跃但产业生态早期**；**红队/检测基准**形成开源社区聚合点，**合规工程工具链尚未形成独角兽或标准化开源项目**；**人才流向**偏向法务/政策岗而非合规工程研发岗。

### 6.1 开源社区热度分布
| 领域 | 代表项目/基准 | 证据 | 生态成熟度 |
|------|--------------|------|------------|
| 数据文档 | HF Dataset Cards | [8] | 高（事实标准） |
| 模型红队 | PyRIT [10], AgentSeer [6], HarmBench [6] | [31,33] | 中高（学术主导，工程化进行中） |
| 红队方法论 | 宏观/微观双层框架 | [7] | 早期（理论阶段） |
| 文本检测 | ALTA 2024 Shared Task | [9] | 中（共享任务周期性） |
| 水印/溯源 | 无主导开源 SDK | [q3-open_problems] | 低（碎片化） |
| 审计日志/CI/CD | 无标准化项目 | [q3-open_problems] | 空白 |

### 6.2 投资与人才信号
- **融资/并购**：> 待核实 —— 无公开可核查的合规工程工具链融资轮次、并购案例。
- **人才流动**：> 待核实 —— 缺乏合规工程师、AI 审计师、红队工程师等新岗位的招聘薪资/需求量数据。
- **社区规模**：AgentSeer/HarmBench 等新框架 GitHub star、贡献者数 > 待核实。

---

## 7. 信号与预测（Signals & Forecast）

> **一句话增量判断**：**未来 6-18 个月**，EU AI Act 强制合规倒计时将倒逼 **「合规即代码」工具链爆发**；**Agentic AI 红队基准将进入 ISO/IEC 标准化工作项**；**跨司法管辖区互认谈判**可能产出首个双边互认备忘录；**水印/溯源互操作性协议**或成下一个标准化战场。

### 7.1 早期信号（已观测到）
| 信号 | 来源 | 强度 |
|------|------|------|
| Agentic AI 可信四维分类学成文，直接对标标准化需求 | [5] | 强 |
| 智能体级红队框架 AgentSeer + 基准 HarmBench 发布 | [6] | 强 |
| 红队方法论反思形成宏观/微观双层框架 | [7] | 中 |
| 医疗 AI 高风险分类实证案例积累 | [2] | 中 |
| GPAI 系统性风险法律定性探讨（ESM3 案例） | [3] | 弱/特定 |

### 7.2 可验证预测假设（未来 6-18 月）
| # | 预测假设（可证伪） | 依据链 | 置信度 | 验证指标 |
|---|-------------------|--------|--------|----------|
| P1 | **欧盟委员会将在 2026 Q4 前发布《高风险 AI 系统合规指南》v1.0**，明确内部部署范围、技术文档模板 | EU AI Act 实施倒计时 + 学术界解读争议 [14,20] | 较大概率 | 官方期刊/欧盟委员会网站发布指南 PDF |
| P2 | **ISO/IEC 42001:2023 认证机构名单将扩展至 ≥20 家**，且首批包含中国/美国机构 | 国际标准落地节奏 + 地缘互认需求 | 推测 | ISO/IEC 官网认证机构目录更新 |
| P3 | **AgentSeer 或同类智能体级红队框架将被纳入 NIST AI RMF 补充指南或 ISO/IEC 42001 附录** | 标准化急需技术细化 + 学术基准成熟 [7,33] | 推测 | NIST/ISO 官方工作组会议纪要、公开征求意见稿 |
| P4 | **主流 MLOps 平台（Vertex AI, MLflow, Azure ML）将原生集成「模型卡片/数据卡片/红队检查点」CI/CD 模板** | 合规工程工具链断层 + 企业级需求 [q3-open_problems] | 推测 | 平台 Release Notes、官方文档新增合规章节 |
| P5 | **中美欧将就 AI 合规互认启动首轮政府间对话**，产出非约束性联合声明 | 全球治理碎片化成本过高 + 产业界游说 | 推测 | 外交部/商务部/欧委会官网新闻稿 |

### 7.3 不确定性与争议标注
- **[Debated]** 内部部署是否豁免：学术界正反方论据并存，待欧盟委员会权威解释或法院判例 [4]。
- **[R]** 美国联邦 AI 立法是否在 2026 年通过：取决于大选后国会组成与两党共识，传闻多、实质进展少 [q1-open_problems]。
- **[P]** 中国国家标准《生成式 AI 服务安全规范》发布时间：> 待核实，依赖标准立项公示与征求意见进度。
- **不确定**：所有预测均基于预印本学术信号推演，**缺乏官方政策文件、标准组织工作计划、厂商路线图**等高等级证书支撑。

---

## 经典与奠基性工作（Classic & Foundational Works）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| Conformity Assessments and Post-market Monitoring: A Guide to the Role of Auditing in the Proposed European AI Regulation | 2021 | arXiv (cs.CY) | > 待核实 | arXiv 预印本 | 中 | ★★★★☆ | [11] | 首批系统解读 EU AI Act 执行机制，确立合格评定与上市后监管为核心合规抓手 |
| Towards trustworthy agentic AI: a comprehensive survey of safety, robustness, privacy, and system security | 2026 | arXiv (cs.AI) | > 待核实 | arXiv 预印本 | 高 | ★★★★★ | [5] | 将 Agentic AI 可信度拆解为四维，为 NIST RMF、ISO 42001 等标准落地提供技术映射表 |
| From Legal Text to AI-specific Risk Sources: A Systematic Analysis of the EU AI Act's High-Risk Requirements | 2026 | arXiv (cs.AI) | > 待核实 | arXiv 预印本 | 中 | ★★★☆☆ | [1] | 系统映射高风险要求与风险分类法，为合规落地提供结构化基础 |
| Ethics and EU AI Act in Cases of Work Disability Risk and Alzheimer's Disease Risk Prediction | 2026 | arXiv (cs.CY); BAI'26 | > 待核实 | 会议论文 + 预印本 | 中 | ★★★☆☆ | [2] | 医疗 AI 高风险分类实证案例，展示从研究到生产的合规挑战 |
| The Case for ESM3 as a General-Purpose AI Model with Systemic Risk Under the EU AI Act | 2026 | arXiv (cs.CY) | > 待核实 | arXiv 预印本 | 低 | ★★☆☆☆ | [3] | 探讨前沿生物基础模型是否触发 GPAI 系统性风险义务 |
| Internal Deployment in the AI Act | 2025 | arXiv (cs.CY) | > 待核实 | arXiv 预印本 | 低 | ★★☆☆☆ | [4] | 梳理内部部署范围的法律解释争议 |
| Navigating Dataset Documentations in AI: A Large-Scale Analysis of Dataset Cards on Hugging Face | 2024 | arXiv (cs.LG) | > 待核实 | arXiv 预印本 | 中 | ★★★★☆ | [8] | 数据卡片生态大规模实证研究 |
| Mind the Gap: Comparing Model- vs Agentic-Level Red Teaming with Action-Graph Observability on GPT-OSS-20B | 2025 | arXiv (cs.AI) | > 待核实 | arXiv 预印本 | 高 | ★★★★★ | [6] | 首个对比模型级与智能体级红队测试，给出 AgentSeer 与 HarmBench |
| Red Teaming AI Red Teaming | 2025 | arXiv (cs.AI) v2 | > 待核实 | arXiv 预印本 | 中 | ★★★★☆ | [7] | 红队方法论反思，提出全生命周期宏观红队框架 |
| Overview of the 2024 ALTA Shared Task: Detect Automatic AI-Generated Sentences for Human-AI Hybrid Articles | 2024 | arXiv (cs.CL) | > 待核实 | 共享任务官方概述 | 中 | ★★★☆☆ | [9] | AI 文本检测共享任务基准 |

> **注**：上表所有条目均为 arXiv 预印本或会议论文，**缺乏** Asilomar AI Principles、OECD AI Principles [12]、NIST AI RMF 早期版 [13]、GDPR 对 AI 影响 [14]、ISO/IEC 42001 正式标准文本等经典一手权威来源的覆盖，需补充检索。

---

## 开源项目（Open Source Projects）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| PyRIT: A Framework for Security Risk Identification and Red Teaming in Generative AI System | 2024 | Microsoft | > 待核实 | arXiv 预印本 [10] | 中高 | ★★★★☆ | [10] | 微软开源生成式 AI 红队框架，工程化程度较高 |
| AgentSeer | 2025 | 学术团队 | > 待核实 | arXiv 预印本 [6] | 高 | ★★★★★ | [6] | 智能体级可观测性红队框架，配合 HarmBench 基准 |
| HarmBench | 2025 | 学术团队 | > 待核实 | arXiv 预印本 [6] | 高 | ★★★★★ | [6] | 智能体红队有害目标基准 |
| HF Dataset Cards | 2024- | Hugging Face | > 待核实 | 社区事实标准 | 高 | ★★★★★ | https://huggingface.co/docs/hub/datasets-cards | 数据文档事实标准，大规模采用 [8] |

> **缺口**：模型卡片工具链、水印/溯源 SDK、合规审计日志库、合规 CI/CD 插件**无主导开源项目**被检索到 [q3-open_problems]。

---

## 数据集与基准（Datasets & Benchmarks）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| HarmBench | 2025 | 学术团队 | > 待核实 | arXiv 预印本 [6] | 高 | ★★★★★ | [6] | 智能体红队有害目标基准 |
| ALTA 2024 Shared Task: Detect AI-Generated Sentences | 2024 | ALTA 组委会 | > 待核实 | 共享任务官方 [9] | 中 | ★★★☆☆ | [9] | 人机混合文章句级检测基准 |
| HF Dataset Cards Corpus | 2024 | Hugging Face / 学术团队 | > 待核实 | arXiv 预印本 [8] | 中 | ★★★★☆ | [8] | 数据卡片大规模语料，支撑文档质量实证分析 |

> **缺口**：模型卡片质量基准、水印鲁棒性跨厂商基准、合规审计日志基准、跨司法管辖区合规测试集**均缺失** [q3-open_problems]。

---

## 参考来源（Sources）
[1] From Legal Text to AI-specific Risk Sources: A Systematic Analysis of the EU AI Act's High-Risk Requirements — http://arxiv.org/abs/2609.13535v1
[2] Ethics and EU AI Act in Cases of Work Disability Risk and Alzheimer's Disease Risk Prediction — http://arxiv.org/abs/2607.05402v1
[3] The Case for ESM3 as a General-Purpose AI Model with Systemic Risk Under the EU AI Act — http://arxiv.org/abs/2605.01611v1
[4] Internal Deployment in the AI Act — http://arxiv.org/abs/2512.05742v4
[5] Towards trustworthy agentic AI: a comprehensive survey of safety, robustness, privacy, and system security — http://arxiv.org/abs/2605.23989v1
[6] Mind the Gap: Comparing Model- vs Agentic-Level Red Teaming with Action-Graph Observability on GPT-OSS-20B — http://arxiv.org/abs/2509.17259v1
[7] Red Teaming AI Red Teaming — http://arxiv.org/abs/2507.05538v2
[8] Navigating Dataset Documentations in AI: A Large-Scale Analysis of Dataset Cards on Hugging Face — http://arxiv.org/abs/2401.13822v1
[9] Overview of the 2024 ALTA Shared Task: Detect Automatic AI-Generated Sentences for Human-AI Hybrid Articles — http://arxiv.org/abs/2412.17848v1
[10] PyRIT: A Framework for Security Risk Identification and Red Teaming in Generative AI System — http://arxiv.org/abs/2410.02828v1
[11] Conformity Assessments and Post-market Monitoring: A Guide to the Role of Auditing in the Proposed European AI Regulation — http://arxiv.org/abs/2111.05071v1
[12] What are the OECD Principles on AI? — https://doi.org/10.1787/6ff2a1c4-en
[13] Actionable Guidance for High-Consequence AI Risk Management: Towards Standards Addressing AI Catastrophic Risks — http://arxiv.org/abs/2206.08966v3
[14] Artificial Intelligence Accountability of Public Administration — https://doi.org/10.1093/ajcl/avac012

---

*Generated by research-bot · topic=`ai-治理与监管政策法规与标准` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`nvidia/nemotron-3-ultra-550b-a55b` · sources=34 · duration=487s · 2026-11-17T04:46:33+00:00*
