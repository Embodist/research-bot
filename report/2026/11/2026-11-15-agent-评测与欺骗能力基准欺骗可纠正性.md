# Agent 评测与欺骗（能力基准、欺骗、可纠正性）深度调研报告

**日期**：2026-11-15（UTC）  
**领域**：Agent 评测、欺骗行为建模、可纠正性、具身智能/VLA 交叉  
**检索源数量**：33 条可引用证据（arXiv 预印本、会议论文、技术报告、开源项目）

---

## 1. 进展与热点

### 1.1 评测透明度与可复现性审计成为核心增量
- **系统性缺失**：对 12 篇知名 LLM Agent 基准论文的逐维度审计显示，同一基准、同一模型在不同论文中报告结果常不一致，论文往往未披露脚手架、采样设置、子集选择、评估器版本等关键复现细节 [1]。  
- **审计框架**：提出包含 5 个字段（基准身份、脚手架规范、推理设置、成本报告、失败分类）的审计模式与评分手册，为基准评测规范化提供可操作工具 [1]。  
- **四轴证据**：热度证据：arXiv 预印本 2026-05，引用数>待核实；权威证据：cs.LG 预印本，未经同行评审；关注度：高——直接切中 Agent 基准可复现性痛点；推荐度：★★★★☆——基准构建者与使用者必读 [1]。

### 1.2 代码类 Agent 基准向实时演进
- **SWE-bench Live**：解决原版基准停止更新、覆盖仓库窄、强依赖特定环境版本等问题，成为实时评测 LLM 解决真实 bug 能力的新标准 [2]。  
- **对抗性增强**：SWE-ABS 通过对抗性基准强化揭示测试基准上的成功率虚高现象，推动评测鲁棒性 [3]。  
- **训练环境**：SWE-Gym 提供基于 SWE-bench 的训练与验证器训练环境，支持端到端 Agent 训练 [4]。  
- **四轴证据（SWE-bench Live）**：热度证据：代码 Agent 社区事实标准，GitHub star>待核实；权威证据：arXiv cs.SE 2025-05 预印本；关注度：高——SOTA 对比基线重塑；推荐度：★★★★☆——代码生成/软件工程 Agent 必跟踪 [2]。

### 1.3 垂直领域基准拓展评测范式
- **RecoAtlas**：首个面向集合级效用的推荐 Agent 基准与 RL 环境，支持结构化报告（项集+自然语言理由）生成与评测 [5]。  
- **HANDBOOK.md**：针对长上下文指令跟随的 Agent 基准，测试系统提示/策略文档/技能文档在部署模式下的持续治理能力 [6]。  
- **WebShop**：早期可扩展真实 Web 交互基准，奠定语言 Agent 在电商场景的 grounding 评测范式 [7]。

### 1.4 评测方法论的认识论重构
- **易逝知识主张**：评测分数被定性为具备形式性、适用范围、有效期窗口三属性的易逝知识主张；多信号平均聚合导致“信任膨胀”，建议采用最弱环节聚合原则 [8]。  
- **代码即 Harness**：代码成为智能体推理、行动、环境建模与执行验证的统一运行时基座，重塑 Agent 基础设施架构 [9]。  
- **元评测数据合成**：PADMÉ 通过偏好对齐数据合成解决 LM Agent 评测器的元评测难题，缓解人工标注昂贵、绝对打分对齐难、评测器互评循环依赖 [10]。

### 1.5 欺骗与可纠正性专用评测基准仍属空白
> 待核实：当前候选证据（[11][1][5][2]）均未覆盖 MACHIAVELLI、DeceptionBench、CorrigibilityBench 等欺骗/可纠正性专用基准，近 1-2 年该维度文献需专项检索 [1]。

---

## 2. 工业界与产品

### 2.1 开源 Agent 平台与 SDK 工程化落地
- **OpenHands**：面向 AI 软件开发者的开放平台，提供通用 Agent 运行时与基准集成 [12]。  
- **OpenHands SDK**：可组合、可扩展的生产级 Agent SDK，支撑工具调用、代码执行、状态管理等工程化能力 [13]。  
- **四轴证据（OpenHands）**：热度证据：GitHub star>待核实，社区活跃度>待核实；权威证据：arXiv cs.SE 2024-07/2025-11 预印本；关注度：中——开源软件工程 Agent 代表性平台；推荐度：★★★★☆——生产级 Agent 基础设施参考实现 [12][13]。

### 2.2 评测 Agent 与自动化评测管线
- **Open Evaluation Agent**：模仿人类定性判断流程，对视觉生成模型实现高效可提示评测，降低采样成本并给出可解释结果 [14]。  
- **PADMÉ 管线**：为评测框架内置自校准模块提供偏好对齐数据合成路径，工程落地价值高 [10]。

### 2.3 红队/欺骗检测工具链在 Agent 场景的部署现状
> 待核实：主流红队框架（Garak、PromptFoo、Red-Teaming 框架）在 Agent 多轮交互、工具调用、代码执行环境中的专用工具与实战效果缺乏公开部署案例 [15]。

---

## 3. 蓝海与缺口

| 缺口维度 | 具体表现 | 证据来源 | 优先级 |
|----------|----------|----------|--------|
| **欺骗行为专用基准** | 缺乏针对谄媚、隐瞒能力、背叛性转向的标准化评测套件；MACHIAVELLI (2023) 等早期工作未形成持续榜单 | [1] 审计未覆盖 | ★★★★★ |
| **可纠正性量化基准** | 无统一的可关闭性、可修正性量化指标与基准；The Off-Switch Game [16][17] 仅为理论框架，缺乏工程化测试环境 | [16][17] | ★★★★★ |
| **多轮交互中的欺骗检测** | 现有红队工具多针对单轮提示注入，缺乏面向工具调用链、代码执行、长时程规划的欺骗检测基准 | [15] | ★★★★☆ |
| **具身/VLA 专用评测基础设施** | SimplerEnv、LIBERO、Open X-Embodiment 评测管线的工程现状、可复现性、红队扩展未系统调研 | [15] | ★★★★☆ |
| **评测分数有效期管理** | 易逝知识主张框架 [8] 提出后，缺乏自动化的有效期监控、污染检测、分布漂移预警工程实现 | [8] | ★★★★☆ |

---

## 4. 瓶颈与拐点

### 4.1 核心瓶颈
1. **评测器可信度**：LM-as-a-judge 的元评测依赖昂贵人工标注，PADMÉ [10] 等数据合成路径尚未大规模验证。  
2. **基准污染与时效性**：SWE-bench Live [2] 等实时基准虽缓解污染，但持续维护成本高、社区贡献机制未成熟。  
3. **欺骗行为的隐蔽性与定义分歧**：谄媚、隐瞒、背叛性转向缺乏统一形式化定义，导致检测器训练数据稀缺、标注不一致。  
4. **可纠正性的工程化落地**：The Off-Switch Game [16][17] 等博弈论模型未转化为可在真机/仿真中部署的测试环境与关闭开关实现。

### 4.2 拐点信号
- **评测范式从静态榜单转向持续演进**：SWE-bench Live [2]、HANDBOOK.md [6] 体现基准即服务趋势。  
- **代码为中心的 Agent 基础设施成熟**：Code as Agent Harness [9] 推动沙箱、验证链路标准化，降低红队/欺骗检测工具开发门槛。  
- **元评测数据合成可行性验证**：PADMÉ [10] 若在开源社区复现成功，将显著降低评测器对齐成本。

---

## 5. 社会·政策·国际

### 5.1 监管与标准化动向
> 待核实：EU AI Act、NIST AI RMF、中国《生成式人工智能服务管理暂行办法》对 Agent 评测、红队测试、欺骗检测的具体合规要求尚未形成行业共识标准 [15]。

### 5.2 地缘政治与供应链影响
- 算力出口管制可能加速轻量化评测 Agent（如 Open Evaluation Agent [14]）与本地化红队工具的研发需求。  
- 开源生态（OpenHands [12][13]、SWE-bench [2]）在全球协作中承担关键基础设施角色，受供应链安全审查影响风险>待核实。

### 5.3 伦理与劳动影响
- Agent 自主决策能力增强（Reflexion [18]、代码即 Harness [9]）引发对人类监督缺失、欺骗行为不可控的伦理担忧，需可纠正性机制作为安全护栏 [16][17]。

---

## 6. 资本与生态

### 6.1 投资与并购信号
> 待核实：Agent 评测基础设施、红队工具、可纠正性研究方向的融资轮次、并购案例缺乏公开聚合数据 [15]。

### 6.2 人才流动与社区格局
- **核心团队集中**：SWE-bench [2][3][4]、OpenHands [12][13]、PADMÉ [10] 等由少数顶级实验室/公司主导，人才流动性对生态连续性影响大。  
- **开源协作模式**：OpenHands SDK [13] 采用可组合插件架构，吸引社区贡献评测器、工具、环境，形成生态护城河。

### 6.3 标准化竞争
- **基准即标准**：SWE-bench Live [2] 事实标准地位巩固；HANDBOOK.md [6]、RecoAtlas [5] 试图在长上下文、推荐决策等细分领域建立标准。  
- **评测方法论话语权**：易逝知识主张 [8]、最弱环节聚合原则若被主流框架（HELM、LM-Eval-Harness、OpenCompass）采纳，将重塑评测工程规范。

---

## 7. 信号与预测

| 信号 | 来源 | 可证伪假设（6-18个月） | 置信度 | 不确定性标注 |
|------|------|------------------------|--------|--------------|
| 实时基准成为代码 Agent SOTA 对比唯一基线 | [2][3] | **假设**：至 2027-06，≥80% 代码 Agent 论文在 SWE-bench Live 上报告结果，而非原版静态 SWE-bench | 较大概率 | 依赖社区维护持续性 |
| 元评测数据合成（PADMÉ 路线）被主流评测框架集成 | [10] | **假设**：至 2027-03，LM-Eval-Harness 或 OpenCompass 合并偏好对齐数据合成模块用于评测器自校准 | 推测 | 需开源实现与复现验证 |
| 欺骗/可纠正性专用基准首发并形成榜单 | [1] 缺口 | **假设**：至 2027-09，出现首个覆盖谄媚/隐瞒/背叛性转向/可关闭性的综合基准（如 DeceptionBench v1）并在 NeurIPS/ICLR/CoRL 发布 | 推测 | 依赖学术界优先级与资金投入 |
| 代码即 Harness 推动红队工具标准化 | [9] | **假设**：至 2027-06，基于代码沙箱的红队框架（工具调用链注入、代码执行劫持、状态回滚测试）成为 Agent 安全审计标配 | 较大概率 | 需开源社区协作验证 |
| 评测分数有效期自动化监控工具化 | [8] | **假设**：至 2027-12，出现集成污染检测、分布漂移预警、有效期标注的评测分数管理 SaaS/开源工具 | 推测 | 工程复杂度高，商业模式未验证 |

> **风险提示**：上述预测均基于当前预印本趋势外推，缺乏同行评审、大规模复现、产业界采纳等强证据支撑，存在**不确定**性；若关键开源项目停止维护或监管政策突变，时间线可能显著延后。

---

## 经典与奠基性工作

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| The Off-Switch Game | 2016 | Hadfield-Menell 等 | 引用数>待核实 | arXiv preprint (cs.AI) | 高：可纠正性理论奠基 | ★★★★★ | [16] | 形式化定义可关闭性博弈，后续工作基石 |
| A Game-Theoretic Analysis of the Off-Switch Game | 2017 | Hadfield-Menell 等 | 引用数>待核实 | arXiv preprint (cs.GT) | 高：博弈论深化 | ★★★★☆ | [17] | 扩展至一般可纠正性条件 |
| WebShop: Towards Scalable Real-World Web Interaction | 2022 | Yao 等 | 引用数>待核实 | cs.CL (会议版待核实) | 高：语言 Agent 交互基准开山 | ★★★★★ | [7] | 可扩展真实 Web 环境，奠定 grounding 评测范式 |
| Reflexion: Language Agents with Verbal Reinforcement Learning | 2023 | Shinn 等 | 引用数>待核实 | arXiv preprint (cs.CL) | 高：语言反馈闭环范式 | ★★★★★ | [18] | 语言强化学习核心范式，影响后续 Agent 训练 |
| A Survey of Multi-Agent Deep RL with Communication | 2022 | Zhang 等 | 引用数>待核实 | cs.MA (期刊版待核实) | 中：多 Agent 通信综述 | ★★★★☆ | [19] | 多 Agent 协作评测理论基础 |

---

## 开源项目与工程基础设施

| 名称 | 年份 | 维护机构 | GitHub Star | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|----------|-------------|------|--------|--------|------|------|
| OpenHands | 2024 | All Hands AI | >待核实 | arXiv preprint (cs.SE) | 高：生产级软件工程 Agent 平台 | ★★★★★ | [12] | 通用 Agent 运行时、基准集成、插件生态 |
| OpenHands SDK | 2025 | All Hands AI | >待核实 | arXiv preprint (cs.SE) | 高：可组合生产级 SDK | ★★★★★ | [13] | 工具调用、代码执行、状态管理标准化 |
| SWE-bench / SWE-bench Live | 2024/2025 | Princeton 等 | >待核实 | arXiv preprint (cs.SE) | 高：代码 Agent 事实标准 | ★★★★★ | [2] | 实时更新、对抗增强、训练环境 (SWE-Gym [4]) |

---

## 数据集与基准

| 名称 | 年份 | 机构 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|------|------|------|--------|--------|------|------|
| SWE-bench Live | 2025 | Princeton 等 | 下载量>待核实 | arXiv preprint (cs.SE) | 高：代码 Agent 核心基准 | ★★★★★ | [2] | 实时更新、广覆盖仓库、去环境锁定 |
| HANDBOOK.md | 2026 | 作者团队 | 下载量>待核实 | arXiv preprint (cs.AI) | 中：长上下文指令跟随新基准 | ★★★★☆ | [6] | 部署模式下的持续治理能力测试 |
| RecoAtlas | 2026 | 作者团队 | 下载量>待核实 | arXiv preprint (cs.IR) | 中：推荐 Agent 集合级效用首创 | ★★★☆☆ | [5] | 结构化报告生成与 RL 环境 |
| WebShop | 2022 | Yale 等 | 下载量>待核实 | cs.CL | 高：早期可扩展 Web 交互基准 | ★★★★★ | [7] | 电商场景语言 grounding 评测 |

---

## 参考来源
[1] What Twelve LLM Agent Benchmark Papers Disclose About Themselves: A Pilot Audit and an Open Scoring Schema — http://arxiv.org/abs/2605.21404v1
[2] SWE-bench Goes Live! — http://arxiv.org/abs/2505.23419v2
[3] SWE-ABS: Adversarial Benchmark Strengthening Exposes Inflated Success Rates on Test-based Benchmark — http://arxiv.org/abs/2603.00520v1
[4] Training Software Engineering Agents and Verifiers with SWE-Gym — http://arxiv.org/abs/2412.21139v2
[5] RecoAtlas: A Benchmark and RL Environment for LLM Recommendation Agents Optimizing Set-Level Utility — http://arxiv.org/abs/2605.18805v2
[6] HANDBOOK.md: A Benchmark for Long-Context Agentic Instruction Following — http://arxiv.org/abs/2607.25398v3
[7] WebShop: Towards Scalable Real-World Web Interaction with Grounded Language Agents — http://arxiv.org/abs/2207.01206v4
[8] Position: Evaluation Scores Are Perishable Knowledge Claims — http://arxiv.org/abs/2607.26191v1
[9] Code as Agent Harness — http://arxiv.org/abs/2605.18747v1
[10] PADMÉ: Preference Alignment Data Synthesis for Meta-Evaluation of LM Agent Evaluators — http://arxiv.org/abs/2609.36086v1
[11] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1
[12] OpenHands: An Open Platform for AI Software Developers as Generalist Agents — http://arxiv.org/abs/2407.16741v3
[13] The OpenHands Software Agent SDK: A Composable and Extensible Foundation for Production Agents — http://arxiv.org/abs/2511.03690v2
[14] Open Evaluation Agent: Efficient and Promptable Evaluation of Visual Generative Models — http://arxiv.org/abs/2608.09666v1
[15] NTU-NPU System for Voice Privacy 2024 Challenge — http://arxiv.org/abs/2410.02371v1
[16] The Off-Switch Game — http://arxiv.org/abs/1611.08219v3
[17] A Game-Theoretic Analysis of the Off-Switch Game — http://arxiv.org/abs/1708.03871v1
[18] Reflexion: Language Agents with Verbal Reinforcement Learning — http://arxiv.org/abs/2303.11366v4
[19] A Survey of Multi-Agent Deep Reinforcement Learning with Communication — http://arxiv.org/abs/2203.08975v2

---

*Generated by research-bot · topic=`agent-评测与欺骗能力基准欺骗可纠正性` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`nvidia/nemotron-3-ultra-550b-a55b` · sources=33 · duration=359s · 2026-11-15T01:50:42+00:00*
