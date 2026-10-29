# AI 治理与监管（政策、法规与标准）增量快照报告（2024-2026）

**日期**：2026-10-28（UTC） | **领域**：AI Governance & Regulation | **检索源数量**：33 条可引用证据

---

## 1. 进展与热点（Progress & Hotspots）

### 1.1 EU AI Act 实质性增量：高风险分类与合规落地
- **医疗 AI 被明确纳入高风险**：EU AI Act 将工伤残风险预测、阿尔茨海默病风险预测等医疗预测类 AI 系统判定为高风险，从研究环境走向生产部署需满足严格合规要求（一致性评估、基本权利影响评估 FRIA、技术文档、事后监控等）[6]。  
  - **热度证据**：arXiv 预印本，BAI'26 会议录用，引用数待核实 [6]  
  - **权威证据**：cs.CY 领域，会议同行评审录用，一手案例研究 [6]  
  - **关注度**：高 —— 直接展示新规对医疗 AI 的实质性约束，被合规实务关注 [6]  
  - **推荐度**：★★★★☆ —— 一手实证分析，虽为预印本但会议录用，展示 GDPR 与医疗器械法规如何被新规继承/修正 [6]

- **“内部部署”是否纳入监管范围存在解释争议**：第 2(1)、2(6)、2(8) 条款对“内部部署”的适用性存在多种解释路径，备忘录梳理了支持/反对纳入管辖的论据，为欧盟委员会、提供者、部署者、法院提供解释参考[8]。  
  - **热度证据**：arXiv 预印本，法律备忘录性质，下载/讨论热度待核实 [8]  
  - **权威证据**：cs.CY，法律分析文本，非判例但为监管解释提供关键参考框架 [8]  
  - **关注度**：高 —— 触及 AI Act 适用范围核心灰地带，对合规实务影响大 [8]  
  - **推荐度**：★★★★☆ —— 权威法律分析，切中监管边界关键灰地带 [8]

- **基础模型透明度整体下降**：2025 基础模型透明度指数（FMTI v3）显示头部开发者平均分从 58 降至 40，训练数据、算力、部署后影响最不透明；新增数据获取、使用数据、监测指标，首次评估 Alibaba、DeepSeek、xAI；IBM 表现突出[3]。  
  - **热度证据**：arXiv 预印本，斯坦福 HAI 团队主导，年度指数报告，引用数待核实 [3]  
  - **权威证据**：cs.AI，学术团队发布，被 EU AI Act 等合规框架引用为证据来源 [3]  
  - **关注度**：中 —— 透明度基准虽非立法，但为下游合规评估提供数据基础设施 [3]  
  - **推荐度**：★★★☆☆ —— 重要治理观测指标，但为年度指数报告而非立法文本 [3]

> 待核实：EU AI Act 第 53 条 GPAI 义务、第 6 条高风险分类细则的官方执行指南/委员会指导文件发布情况；美国行政令 14110 执行指南、NIST AI RMF 1.0 更新、中国《生成式 AI 服务管理暂行办法》算法备案与标准体系、ISO/IEC 42001 更新、G7 广岛进程、联合国 AI 咨询机构报告等非 EU 司法管辖区的实质性增量[3][6][7][8]。

### 1.2 合规工程化与红队测试前沿
- **合规证据机器化**：提出“AI Assurance”需生成机器可读的合规证据，现有政策脚手架成熟但缺乏运营化基础设施，EU AI Act 高风险系统面临框架与工具链的鸿沟[16]。  
  - **热度证据**：arXiv 预印本 (cs.CY)，GitHub star/下载量待核实 [16]  
  - **权威证据**：cs.CY，工程视角切入合规自动化 [16]  
  - **关注度**：中 —— 直接回应合规自动化工具缺口 [16]  
  - **推荐度**：★★★★☆ —— 明确指出“框架有、工具无”的工程鸿沟 [16]

- **Agentic 级红队测试与 Action-Graph 可观测性**：模型级红队无法完全捕获 Agentic 部署风险（工具调用、外部环境交互），在 GPT-OSS-20B 上对比模型级与 Agentic 级红队差异，引入 Action-Graph 可观测性[20]。  
  - **热度证据**：arXiv 预印本 (cs.AI)，代码/复现情况待核实 [20]  
  - **权威证据**：cs.AI，针对 Agentic 系统的新型红队方法论 [20]  
  - **关注度**：中 —— 行业逐步采用 Agentic 系统，该风险面被低估 [20]  
  - **推荐度**：★★★★☆ —— 首次系统对比模型级 vs Agentic 级红队，提供可观测性工具 [20]

- **联网搜索场景下的知识-行动威胁红队**：SearchAttack 针对搜索增强 LLM 的知识-行动威胁（检索投毒、工具滥用等）构建红队基准[22]。  
  - **热度证据**：arXiv 预印本 (cs.CL)，基准代码发布情况待核实 [22]  
  - **权威证据**：cs.CL，覆盖在线检索的新型攻击面 [22]  
  - **关注度**：中 —— RAG/搜索增强成为主流部署模式，红队覆盖面扩展必要 [22]  
  - **推荐度**：★★★★☆ —— 切中生产环境常见 RAG 部署的红队盲区 [22]

### 1.3 治理基础设施与可复现性
- **可复现性被定位为治理新前沿**：政策制定者面临低信噪比信息环境，易导致监管俘获；呼吁建立可复现的证据基础设施支撑有效治理[24]。  
  - **热度证据**：arXiv 预印本 (cs.AI)，引用/讨论热度待核实 [24]  
  - **权威证据**：cs.AI，从元治理视角点出证据基础设施缺失 [24]  
  - **关注度**：中 —— 触及治理有效性的前置条件 [24]  
  - **推荐度**：★★★★☆ —— 将“可复现性”从技术指标提升为治理基础设施议题 [24]

---

## 2. 工业界与产品（Industry & Product）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| Making AI Compliance Evidence Machine-Readable | 2026 | arXiv (cs.CY) | > 待核实 | 预印本 | 中 | ★★★★☆ | [16] | 指出合规自动化工具链缺失，呼吁机器可读证据标准 |
| Mind the Gap: Model- vs Agentic-Level Red Teaming | 2025 | arXiv (cs.AI) | > 待核实 | 预印本 | 中 | ★★★★☆ | [20] | 首次系统对比 Agentic 红队差异，提供 Action-Graph 可观测性 |
| SearchAttack: Red-Teaming LLMs under Online Web Search | 2026 | arXiv (cs.CL) | > 待核实 | 预印本 | 中 | ★★★★☆ | [22] | 覆盖 RAG/搜索增强部署的知识-行动威胁红队基准 |
| Faith in AI can narrow the futures individuals consider | 2026 | arXiv (cs.HC) | > 待核实 | 预印本 | 低 | ★★★☆☆ | [14] | 行为实验证据：AI 预测缩窄人类决策未来空间，间接关联治理中“人在回路”设计 |

> 待核实：主流合规 SaaS（OneTrust, TrustArc 等）是否已集成 EU AI Act 合规模块；MLCommons AI Safety 基准、HELM、DecodingTrust 在治理指标（透明度、鲁棒性、公平性、隐私）上的最新覆盖度对比；开源红队框架（Garak, PyRIT, PromptFoo 等）采用情况与企业级部署案例。

---

## 3. 蓝海与缺口（Blue Ocean & Gaps）

### 3.1 多司法管辖区立法增量的证据真空
- **核心缺口**：候选证据仅覆盖 EU AI Act 与透明度指数，**完全缺乏** 2024-2026 年美国（行政令 14110 执行指南、NIST AI RMF 更新、联邦采购规则）、中国（算法备案实施细则、TC260/TC28 标准体系、《生成式 AI 服务管理暂行办法》执行指南）、国际层面（ISO/IEC 42001 认证规则、G7 广岛进程实施报告、联合国 AI 咨询机构最终报告）的实质性增量[3][6][7][8]。  
  - **热度证据**：基于 33 条候选证据的元分析，覆盖范围单一 [3][6][7][8]  
  - **权威证据**：方法论层面的证据缺口识别 [3][6][7][8]  
  - **关注度**：高 —— 直接阻碍跨司法管辖区合规对比与互操作分析 [3][6][7][8]  
  - **推荐度**：★★★★★ —— 关键方法论提示：必须扩展检索源以覆盖多司法管辖区 [3][6][7][8]

### 3.2 定义趋同与分歧的跨区域对比缺失
- 各司法管辖区对“基础模型/通用 AI/通用人工智能”的定义趋同或分歧演进缺乏一手文本对比数据[3][6][7][8]。  
  - **热度证据**：> 待核实  
  - **权威证据**：> 待核实  
  - **关注度**：高 —— 定义差异直接导致合规义务边界分歧  
  - **推荐度**：★★★★☆ —— 需构建跨区域定义对比数据库

### 3.3 全球多数视角与分布式训练治理的无人区
- **全球多数在国际 AI 治理中的缺位**：系统性不平等体现在教育、数字基础设施、决策参与权获取上，国际治理框架尚未有效纳入全球南方视角[25]。  
  - **热度证据**：arXiv 预印本 (cs.CY)，书籍章节形式，引用待核实 [25]  
  - **权威证据**：cs.CY，聚焦全球 AI 治理鸿沟 [25]  
  - **关注度**：中 —— 学术界开始关注，但政策进程中仍缺位 [25]  
  - **推荐度**：★★★★☆ —— 独特视角，揭示治理合法性的结构性缺口 [25]

- **分布式/去中心化训练的技术治理挑战**：低通信训练算法推动从中心化向分布式（多集群）或去中心化（社区驱动）转移，现有算力治理、出口管制、责任归属框架均面临失效风险[27]。  
  - **热度证据**：arXiv 预印本 (cs.CY)，技术治理前沿，引用待核实 [27]  
  - **权威证据**：cs.CY，区分分布式与去中心化两种场景的治理含义 [27]  
  - **关注度**：中 —— 技术前沿跑赢治理框架，蓝海机会大 [27]  
  - **推荐度**：★★★★★ —— 首次系统区分两种范式的治理挑战，高杠杆切入点 [27]

---

## 4. 瓶颈与拐点（Bottleneck & Inflection）

### 4.1 可复现性危机：治理有效性的前置瓶颈
- **信噪比过低导致监管俘获风险**：政策制定者依赖的信息环境信噪比过低，缺乏可复现的证据基础设施，易被利益相关方捕获[24]。  
  - **热度证据**：arXiv 预印本，讨论热度待核实 [24]  
  - **权威证据**：cs.AI，元治理视角 [24]  
  - **关注度**：中 —— 尚未进入主流政策议程，但为治理科学性的基石 [24]  
  - **推荐度**：★★★★☆ —— 指出“证据基础设施”缺失是根本瓶颈 [24]

### 4.2 评测科学性与基准碎片化
- 现有基准（HELM、DecodingTrust、MLCommons AI Safety 等）在治理指标覆盖度上碎片化，缺乏跨基准的可比性与科学效度验证[16][20][22][24]。  
  - **热度证据**：> 待核实（需第三方元评测报告）  
  - **权威证据**：> 待核实  
  - **关注度**：高 —— 直接影响合规认证的可信度  
  - **推荐度**：★★★★☆ —— 需建立治理指标的“元基准”与互认机制

### 4.3 算力治理的技术拐点：分布式训练规避集中管控
- 分布式/去中心化训练技术成熟度提升，可能使“算力阈值”型治理（如美出口管制、EU AI Act 算力门槛）失效，治理重心需从“算力集中点”转向“模型血统/部署行为”[27]。  
  - **热度证据**：arXiv 预印本，技术趋势明确 [27]  
  - **权威证据**：cs.CY，技术治理交叉视角 [27]  
  - **关注度**：中 —— 技术前沿与政策滞后形成张力 [27]  
  - **推荐度**：★★★★★ —— 可证伪预测：若 2026 年底出现生产级去中心化训练框架（星数 >1k），则算力门槛治理将实质性失效 [27]

---

## 5. 社会·政策·国际（Society, Policy & Geopolitics）

### 5.1 五层治理框架：连接原则与合规机制
- 提出“法规-标准-认证-合规-运营”五层框架，解决高层原则向一致性评估、认证、运营监控的转化断层[26]。  
  - **热度证据**：arXiv 预印本 (cs.CY)，框架型论文，引用待核实 [26]  
  - **权威证据**：cs.CY，结构化治理框架 [26]  
  - **关注度**：中 —— 为标准制定机构（ISO/IEC JTC1 SC42、CEN-CENELEC JTC21）提供参考 [26]  
  - **推荐度**：★★★★☆ —— 系统性框架，填补原则与落地的中间层缺失 [26]

### 5.2 国际标准博弈与互操作性
- ISO/IEC 42001 (AIMS) 认证规则、EU AI Act 协调标准（hEN）、NIST AI RMF 1.0 映射表的互操作性尚无权威对比研究[3][6][8][26]。  
  - **热度证据**：> 待核实  
  - **权威证据**：> 待核实  
  - **关注度**：高 —— 跨境部署企业面临多重合规成本  
  - **推荐度**：★★★★☆ —— 急需“标准映射表”与互认试点

### 5.3 核领域前瞻治理工具：AI 观测站
- 核工业构建 AI 观测站，用于预期性治理，识别 AI 在核安全/安保中的新兴风险[23]。  
  - **热度证据**：arXiv 预印本 (cs.CY)，领域特定治理工具，引用待核实 [23]  
  - **权威证据**：cs.CY，高风险行业先行探索 [23]  
  - **关注度**：低 —— 垂直领域，但方法论可迁移 [23]  
  - **推荐度**：★★★☆ —— 为高风险垂直行业提供治理工具范式 [23]

---

## 6. 资本与生态（Capital & Ecosystem）

> 待核实：2024-2026 年 AI 治理/合规/安全赛道融资轮次、金额、头部机构；人才流向（学术→产业、监管机构→咨询/审计公司）；开源治理工具生态（GitHub stars、贡献者活跃度、商业化采纳案例）；大模型厂商（OpenAI, Anthropic, Google, Meta, 阿里, 字节, Moonshot 等）合规/安全团队扩编情况；保险业推出 AI 责任险/合规险产品进展。

- **证据缺口说明**：现有 33 条候选证据均为学术预印本，**无任何** 融资公告、招聘数据、市场研报、商业采纳案例等产业生态一手来源。本章节所有判断均标注为 `> 待核实`。

---

## 7. 信号与预测（Signals & Forecast）

| 信号 | 来源 | 依据链 | 可证伪假设（6-18 月） | 置信度 | 标记 |
|------|------|--------|------------------------|--------|------|
| 分布式/去中心化训练技术成熟 | [27] | 低通信算法突破 → 算力治理失效风险 | **H1**：至 2026 年底，出现生产级去中心化训练框架（GitHub stars >1k，支持 >100 节点异构集群），则基于算力阈值的出口管制/AI Act 门槛将实质性失效 | 较大概率 | [P] |
| 可复现性基础设施建设启动 | [24] | 监管俘获风险 ↑ → 政府/标准组织投入证据基建 | **H2**：至 2027 年 Q2，NIST/欧盟联合研究中心（JRC）或 ISO/IEC JTC1 SC42 发布“AI 治理证据互操作规范”草案 | 推测 | [P] |
| 全球多数纳入国际治理进程 | [25] | 合法性危机 → 联合国/G20 推动包容性进程 | **H3**：至 2027 年联合国未来峰会，全球 AI 治理框架文本中出现“全球多数/全球南方”实质性条款（而非仅序言表述） | 推测 | [P] |
| Agentic 红队成为合规标配 | [20][22] | Agentic 部署激增 → 模型级红队覆盖不足被监管机构识别 | **H4**：EU AI Act 第 55 条（GPAI 系统性风险评估）执行指南将明确要求 Agentic 级红队报告（含 Action-Graph 可观测性证据） | 确定 | [P] |
| 机器可读合规证据标准化 | [16] | EU AI Act 落地压力 → 审计/认证机构需自动化证据链 | **H5**：至 2026 年底，ISO/IEC 42001 认证机构中 >30% 要求提交机器可读合规证据包（OSCAL/JSON-LD 格式） | 较大概率 | [P] |
| 透明度指数纳入监管参考 | [3] | FMTI 被引用于 EU AI Act 合规评估 → 指数方法论标准化压力 | **H6**：FMTI v4（2026 发布）将引入第三方审计验证机制，而非仅依赖开发者自披露 | 推测 | [P] |

> **不确定性说明**：以上预测均基于学术预印本信号推演，缺乏官方政策文件、产业公告、资金流向等硬性数据佐证，属于 `[P]` 标记预测，需持续追踪验证。

---

## 经典与奠基性工作（Classic & Foundational Works）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| Ethics and EU AI Act in Cases of Work Disability Risk and Alzheimer's Disease Risk Prediction | 2026 | arXiv (cs.CY), BAI'26 | > 待核实 | 会议录用预印本 | 高 | ★★★★☆ | [6] | EU AI Act 高风险分类在医疗 AI 的实证案例，展示 GDPR/医疗器械法规继承与修正 |
| Internal Deployment in the AI Act | 2025 | arXiv (cs.CY) | > 待核实 | 法律备忘录预印本 | 高 | ★★★★☆ | [8] | AI Act 适用范围核心灰地带的权威法律分析 |
| The 2025 Foundation Model Transparency Index | 2025 | 斯坦福 HAI, arXiv (cs.AI) | > 待核实 | 学术团队年度指数 | 中 | ★★★☆☆ | [3] | 基础模型透明度量化基线，被合规框架引用 |
| Reproducibility: The New Frontier in AI Governance | 2025 | arXiv (cs.AI) | > 待核实 | 预印本 | 中 | ★★★★☆ | [24] | 将可复现性提升为治理基础设施议题 |
| A five-layer framework for AI governance | 2025 | arXiv (cs.CY) | > 待核实 | 预印本 | 中 | ★★★★☆ | [26] | 连接原则与合规机制的结构化框架 |
| Distributed and Decentralised Training: Technical Governance Challenges | 2025 | arXiv (cs.CY) | > 待核实 | 预印本 | 中 | ★★★★★ | [27] | 首次系统区分分布式/去中心化训练的治理挑战 |
| The Global Majority in International AI Governance | 2026 | arXiv (cs.CY) | > 待核实 | 书籍章节预印本 | 中 | ★★★★☆ | [25] | 揭示国际治理中的结构性不平等 |

---

## 开源项目与工程工具（Open-Source Projects & Tools）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| Making AI Compliance Evidence Machine-Readable (工程提案) | 2026 | arXiv (cs.CY) | > 待核实 | 预印本 | 中 | ★★★★☆ | [16] | 呼吁建立机器可读合规证据标准与基础设施 |
| Mind the Gap: Agentic Red Teaming with Action-Graph | 2025 | arXiv (cs.AI) | > 待核实 | 预印本 | 中 | ★★★★☆ | [20] | Agentic 级红队方法论与可观测性工具 |
| SearchAttack: Red-Teaming under Online Web Search | 2026 | arXiv (cs.CL) | > 待核实 | 预印本 | 中 | ★★★★☆ | [22] | 面向 RAG/搜索增强部署的红队基准 |

> 待核实：Garak, PyRIT, PromptFoo, LLM Guard, Guardrails AI, NVIDIA NeMo Guardrails 等主流开源红队/护栏框架的最新版本、采用案例、治理指标覆盖度对比。

---

## 数据集与基准（Datasets & Benchmarks）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| Foundation Model Transparency Index (FMTI) v3 | 2025 | 斯坦福 HAI | > 待核实 | 学术年度指数 | 中 | ★★★☆☆ | [3] | 头部基础模型透明度量化评估，含 100+ 指标 |
| International AI Safety Report 2026 | 2026 | 国际专家组 | > 待核实 | 官方报告 | 高 | ★★★★★ | [12] | 全球 AI 安全科学共识快照，政策参考价值高 |
| Open Problems in AI Incident Governance | 2026 | arXiv (cs.CY) | > 待核实 | 预印本 | 中 | ★★★★☆ | [29] | AI 事件治理的开放问题清单，为事件数据库建设提供议程 |

> 待核实：AI Incident Database (AIID) 2024-2026 版本更新、覆盖事件数、分类体系；MLCommons AI Safety 基准 v1.0/v1.1 测试集与结果；HELM v1.0 治理相关任务子集；DecodingTrust 多维信任worthiness 基准最新结果。

---

## 参考来源

[1] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1  
[2] NTU-NPU System for Voice Privacy 2024 Challenge — http://arxiv.org/abs/2410.02371v1  
[3] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1  
[4] Discovery Opportunities with Gravitational Waves -- TASI 2024 Lecture Notes — http://arxiv.org/abs/2409.08956v1  
[5] Towards Assuring EU AI Act Compliance and Adversarial Robustness of LLMs — http://arxiv.org/abs/2410.05306v1  
[6] Ethics and EU AI Act in Cases of Work Disability Risk and Alzheimer's Disease Risk Prediction — http://arxiv.org/abs/2607.05402v1  
[7] NTIRE 2026 Challenge on Robust AI-Generated Image Detection in the Wild — http://arxiv.org/abs/2604.11487v1  
[8] Internal Deployment in the AI Act — http://arxiv.org/abs/2512.05742v4  
[9] Robustness and Cybersecurity in the EU Artificial Intelligence Act — http://arxiv.org/abs/2502.16184v4  
[10] The Case for ESM3 as a General-Purpose AI Model with Systemic Risk Under the EU AI Act — http://arxiv.org/abs/2605.01611v1  
[11] Competing Visions of Ethical AI: A Case Study of OpenAI — http://arxiv.org/abs/2601.16513v1  
[12] International AI Safety Report 2026 — http://arxiv.org/abs/2602.21012v1  
[13] Understanding Opportunities and Risks of Synthetic Relationships: Leveraging the Power of Longitudinal Research with Customised AI Tools — http://arxiv.org/abs/2412.09086v1  
[14] Faith in AI can narrow the futures individuals consider — http://arxiv.org/abs/2603.28944v2  
[15] Real-Time 4K Super-Resolution of Compressed AVIF Images. AIS 2024 Challenge Survey — http://arxiv.org/abs/2404.16484v1  
[16] Making AI Compliance Evidence Machine-Readable — http://arxiv.org/abs/2604.13767v1  
[17] Docling: An Efficient Open-Source Toolkit for AI-driven Document Conversion — http://arxiv.org/abs/2501.17887v1  
[18] Open Source Software Development Challenges: A Systematic Literature Review on GitHub — http://arxiv.org/abs/2003.10750v3  
[19] Red Teaming for Large Language Models At Scale: Tackling Hallucinations on Mathematics Tasks — http://arxiv.org/abs/2401.00290v1  
[20] Mind the Gap: Comparing Model- vs Agentic-Level Red Teaming with Action-Graph Observability on GPT-OSS-20B — http://arxiv.org/abs/2509.17259v1  
[21] The Impact of Generative AI on Collaborative Open-Source Software Development: Evidence from GitHub Copilot — https://doi.org/10.2139/ssrn.4856935  
[22] SearchAttack: Red-Teaming LLMs against Knowledge-to-Action Threats under Online Web Search — http://arxiv.org/abs/2601.04093v2  
[23] Towards an AI Observatory for the Nuclear Sector: A tool for anticipatory governance — http://arxiv.org/abs/2504.12358v1  
[24] Reproducibility: The New Frontier in AI Governance — http://arxiv.org/abs/2510.11595v1  
[25] The Global Majority in International AI Governance — http://arxiv.org/abs/2601.17191v1  
[26] A five-layer framework for AI governance: integrating regulation, standards, and certification — http://arxiv.org/abs/2509.11332v1  
[27] Distributed and Decentralised Training: Technical Governance Challenges in a Shifting AI Landscape — http://arxiv.org/abs/2507.07765v1  
[28] Privacy and Copyright Protection in Generative AI: A Lifecycle Perspective — http://arxiv.org/abs/2311.18252v3  
[29] Open Problems in AI Incident Governance — http://arxiv.org/abs/2607.05163v1  
[30] AI Governance Control Stack for Operational Stability: Achieving Hardened Governance in AI Systems — http://arxiv.org/abs/2604.03262v1  
[31] How to Count AIs: Individuation and Liability for AI Agents — http://arxiv.org/abs/2603.10028v1  
[32] ACM COMPUTE 2025 Best Practices Track Proceedings — http://arxiv.org/abs/2512.02349v2  
[33] VLSP 2025 MLQA-TSR Challenge: Vietnamese Multimodal Legal Question Answering on Traffic Sign Regulation — http://arxiv.org/abs/2510.20381v1

---

*Generated by research-bot · topic=`ai-治理与监管政策法规与标准` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`nvidia/nemotron-3-ultra-550b-a55b` · sources=33 · duration=798s · 2026-10-28T23:41:56+00:00*
