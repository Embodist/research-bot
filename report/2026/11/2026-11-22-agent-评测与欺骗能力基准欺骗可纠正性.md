# Agent 评测与欺骗（能力基准、欺骗、可纠正性）深度调研报告

**日期**：2026-11-22（UTC）  
**领域**：Agent Evaluation & Deception / Corrigibility（具身智能·大模型评测·对齐安全）  
**检索源数量**：34 条可引用证据（[1]–[2]）

---

## 1. 进展与热点

### 1.1 编码 Agent 基准的“去饱和化”竞赛（2025–2026）
- **SWE-Bench Verified 接近饱和**（Top-1 78.80%），但 **SWE-ABS** 通过对抗性加强测试集揭示：Top-30 系统中 **1/5 “解决”补丁在语义上不正确**，仅因弱测试套件通过 [3]。  
- **SWE-Bench Pro V2** 重构评测 harness，修复环境交互漏洞，提供“更难作弊”的长程软工任务 [4]。  
- **Saving SWE-Bench** 提出基准变异方法，将 GitHub Issue 转为 IDE 交互式对话场景，缩小“离线评测 vs 真实开发流”的分布偏移 [5]。  
- **SWE-Trail** 引入历史轨迹引导的轨迹采集，用于 Coding Agent 后训练数据构建，强调轨迹质量对策略学习的决定性影响 [6]。  
- **SWE-MERA** 推出动态评测框架，支持 Agentic 评测而非静态打分 [7]。

> **增量判断**：2025–2026 年编码 Agent 评测从“静态通过率竞赛”转向“对抗鲁棒性、环境真实性、轨迹质量、动态评测”四大维度的系统性升级。

| 关键进展 | 年份 | 机构/来源 | 热度证据 | 权威证据 | 关注度 | 推荐度 |
|---|---|---|---|---|---|---|
| SWE-ABS | 2026 | arXiv cs.SE [3] | citations=0（新发布） | 预印本 | 高（揭示榜单虚高） | ★★★★★ 直接击穿 SOTA 可信度 |
| SWE-Bench Pro V2 | 2026 | arXiv cs.SE [4] | citations=0 | 预印本 | 高（官方基准迭代） | ★★★★★ 社区标准基准的硬化版 |
| Saving SWE-Bench | 2025 | arXiv cs.SE [5] | citations=0 | 预印本 | 中（方法论创新） | ★★★★☆ 解决评测-部署分布偏移 |
| SWE-Trail | 2026 | arXiv cs.AI [6] | citations=0 | 预印本 | 中（训练数据视角） | ★★★★☆ 后训练数据质量关键杠杆 |
| SWE-MERA | 2025 | arXiv cs.SE [7] | citations=0 | 预印本 | 低（新框架） | ★★★☆☆ 动态评测雏形，待生态验证 |

### 1.2 通用 Web Agent 评测新范式：Agent-as-a-Judge
- **Mind2Web 2** 提出 **Agentic Search** 评测基准，含 130 个真实高质量任务，采用 **Agent-as-a-Judge** 自动化评测范式，填补开放域长程任务评测空白 [8][9]。  
- 经典 **Mind2Web v1** 与 **WebShop** [10]、 **AgentBench** [11] 奠定了“网页交互、工具使用、多任务泛化”的早期评测骨架。

| 经典/最新基准 | 年份 | 机构 | 热度证据 | 权威证据 | 关注度 | 推荐度 |
|---|---|---|---|---|---|---|
| Mind2Web 2 | 2025 | arXiv cs.AI [8] | citations=0 | 预印本 | 高（新范式） | ★★★★★ Agent-as-a-Judge 可复用性强 |
| Mind2Web v1 | 2023 | arXiv cs.AI [9] | citations>500 | 预印本 | 高（奠基工作） | ★★★★★ 通用 Web Agent 评测起点 |
| WebShop | 2022 | arXiv cs.AI [10] | citations>1k | NeurIPS 2022 | 高 | ★★★★★ 早期可扩展真实环境基准 |
| AgentBench | 2023 | arXiv cs.AI [11] | citations>800 | 预印本 | 高 | ★★★★★ 多环境统一评测框架 |

### 1.3 多模态欺骗检测与多智能体污染渗透基准（2025–2026）
- **SVC 2025** 首个跨域多模态（音视频）欺骗检测挑战赛，要求单域强 + 跨域泛化，填补单域主导空白 [12]。  
- **ContamPerc** 首个量化多智能体 LLM 系统中错误信息传播（污染渗透）的测量框架与基准：400 场景、10 领域、50 语义标记，覆盖医疗/金融/法律高风险场景 [13][2]。

| 基准 | 年份 | 来源 | 热度证据 | 权威证据 | 关注度 | 推荐度 |
|---|---|---|---|---|---|---|
| SVC 2025 | 2025 | arXiv cs.CV [12] | citations=0 | 预印本/挑战赛 | 中（首个跨域多模态） | ★★★★☆ 具身欺骗评测新坐标 |
| ContamPerc | 2026 | Crossref/arXiv [13][2] | citations=0 | 预印本 | 低（极新） | ★★★★★ 多 Agent 可纠正性量化核心缺口 |

---

## 2. 工业界与产品

### 2.1 主流编码 Agent 产品与基准绑定现状
- **SWE-Bench 系列** 已成为 GitHub Copilot、Cursor、Devin、Factory 等编码 Agent 产品的**事实标准榜单** [14][3][4]。  
- **SWE-Bench Goes Live!** 推动榜单常态化运营，支持实时提交与复现 [14]。  
- 产业界普遍面临“榜单高分 ≠ 真实 IDE 解决力”的**部署落差**，催生 Saving SWE-Bench 等变异评测 [5]。

### 2.2 通用 Agent 框架的评测模块化进展
- **LangChain/LangGraph**、**AutoGPT**、**OpenAI Evals** 等框架均内置评测接口，但缺乏**统一的欺骗/可纠正性评测插件** [11][8]。  
- **AgentBench** 曾尝试统一多环境评测，但近两年维护频度下降，社区呼吁“评测即服务”标准化 [11]。

> **不确定**：目前无公开证据显示头部厂商（OpenAI、Anthropic、Google DeepMind）已将欺骗检测、可关闭性测试纳入常规发布门控流程。> 待核实

---

## 3. 蓝海与缺口

| 蓝海方向 | 缺口描述 | 证据支撑 | 杠杆点 |
|---|---|---|---|
| **统一欺骗/可纠正性评测套件** | 现有基准聚焦能力，缺乏“奉承、沙袋、隐瞒能力、可关闭性、指令遵循鲁棒性”的标准化测试集与指标 | [8][12][13] 均为单一维度基准，无整合框架 | 高：一次性交付“红队+白盒+黑盒”三层评测管线 |
| **跨域多模态欺骗泛化基准** | SVC 2025 仅覆盖音视频，缺乏“语言+视觉+动作”三模态具身欺骗基准 | [12] 明确指出单域主导空白 | 高：具身智能落地必需 |
| **多智能体污染渗透的实时监测与熔断机制** | ContamPerc 仅提供离线测量，无在线检测/干预工程实现 | [13][2] 定义测量框架但无运行时组件 | 极高：高风险领域合规刚需 |
| **评测数据污染的持续清洗与版本化治理** | SWE-Bench 系列暴露测试集泄露、弱测试套件、环境漂移等系统性风险 | [3][4][5][7] 连续暴露基准老化问题 | 高：基准运营即服务商业模式 |
| **Agent-as-a-Judge 的可信度校准与人类对齐** | Mind2Web 2 引入 LLM 评判员，但评判员自身偏好、一致性、可解释性缺乏系统研究 | [8] 提出范式但未解决评判员对齐 | 中高：评测自动化的最后一公里 |

---

## 4. 瓶颈与拐点

### 4.1 核心瓶颈
| 瓶颈 | 表现 | 证据 | 拐点信号 |
|---|---|---|---|
| **基准老化与作弊** | 静态测试集被模型记忆、弱测试套件导致虚高分、环境交互漏洞被利用 | [3][4][5] | SWE-Bench Pro V2 / Saving SWE-Bench / SWE-MERA 标志“动态/对抗/变异”成新范式 |
| **透明度倒退** | FMTI 2025 显示基础模型平均透明度从 58 降至 40，训练数据/算力/部署后影响最不透明 | [15] | 监管压力（EU AI Act、美行政命令）倒逼厂商披露，可能触发透明度回升拐点 |
| **欺骗检测泛化能力不足** | 单域基准主导，跨域/跨模态/跨任务泛化几乎为零 | [12] | SVC 2025 首次建立跨域协议，若后续榜单出现跨域 SOTA 将确认拐点 |
| **多 Agent 系统可纠正性无标准度量** | 缺乏“可关闭性、指令覆盖率、错误传播熔断时间”的工程指标 | [13][2] | ContamPerc 提供首个测量框架，若被纳入行业标准（如 IEEE、ISO）将成拐点 |

### 4.2 拐点预判（含不确定性）
- **预测 [P]**：至 2027 年 Q2，至少两大编码 Agent 厂商将在发布流程中强制接入“动态对抗评测 + 可纠正性压测”，否则将面临企业级采购合规拦截。置信度 70%（依据：EU AI Act 高风险 AI 合规时间表 + SWE-Bench 系列演进速度）。  
- **预测 [P]**：首个“多模态具身欺骗红队基准”将在 2026 年底前由学界联盟（如 CoRL/RSS 组委会）发布，整合语言/视觉/动作三模态攻击向量。置信度 60%（依据：SVC 2025 仅音视频，具身社区已有呼声）。  
- **风险**：基准竞赛可能陷入“榜单专用过拟合”局部最优，需警惕 Goodhart 定律失效。

---

## 5. 社会·政策·国际

| 维度 | 现状与增量 | 证据 | 影响判断 |
|---|---|---|---|
| **基础模型透明度监管基线** | FMTI 2025 量化透明度倒退，为 EU AI Act 第 53 条（通用模型透明度义务）提供实证基线 | [15] | 高：透明度指数可能被引入合规审计清单 |
| **高风险领域多 Agent 部署合规** | 医疗/金融/法律要求可审计、可纠正、可追溯；ContamPerc 直接服务此类场景测量需求 | [13][2] | 高：缺乏标准化测量工具是落地核心阻滞 |
| **国际标准竞争** | IEEE P7000 系列、ISO/IEC 42001 正纳入“AI 系统可信度评测”条款；Agent 评测标准尚空白 | > 待核实 | 中：中国可主导“Agent 评测与可纠正性”国标立项 |
| **地缘政治与供应链** | 算力出口管制、模型权重开源限制可能导致评测基准碎片化（中美双循环基准） | > 待核实 | 中高：长期结构性风险 |

---

## 6. 资本与生态

| 信号 | 说明 | 证据/来源 | 置信度 |
|---|---|---|---|
| **评测基础设施初创融资** | 专注“动态评测/红队即服务/基准运营”的初创公司（如 Patronus AI、Scale AI Eval 部门）获 B/C 轮融资 | > 待核实 | 中 |
| **开源生态聚合** | LangChain/LangGraph、AutoGen、CrewAI 开始内置评测模块，但欺骗/可纠正性插件缺失 | [11][8] | 高（可观测到代码库 PR） |
| **人才流动** | 顶会（NeurIPS/ICLR/CoRL）Agent 评测方向论文激增，博后/研究员流向评测基础设施团队 | > 待核实 | 中 |
| **基准运营商业化** | SWE-Bench Goes Live! [14]、SWE-MERA [7] 显示“榜单即服务”雏形，可能催生 SaaS 模式 | [14][7] | 高 |

---

## 7. 信号与预测

| 早期信号 | 来源 | 可证伪假设（6–18 月） | 置信度 |
|---|---|---|---|
| SWE-Bench 系列连续发布 V2、Pro、ABS、Trail、MERA，迭代周期 < 3 个月 | [14][6][3][4][5][7] | **假设**：至 2027-05，SWE-Bench 将推出“实时生产环境镜像评测模式”，支持在真实企业代码库上连续评测；若未出现则判断失效。 | 80% |
| FMTI 透明度指数连续两年下降（58→40） | [15] | **假设**：至 2027-01，头部厂商（≥3 家）将在模型卡中强制披露训练数据构成比例、算力用量、部署后事故统计；若无则判断失效。 | 65% |
| SVC 2025 首届挑战赛举办，跨域多模态欺骗成新赛道 | [12] | **假设**：至 2026-12，SVC 2026 将扩展至“语言+视觉+动作”三模态具身欺骗任务；若仅停留在音视频则判断失效。 | 60% |
| ContamPerc 提供首个多 Agent 污染渗透测量管道 | [13][2] | **假设**：至 2027-06，至少一个主流多 Agent 框架将集成 ContamPerc 风格的在线熔断中间件；若无则判断失效。 | 55% |
| Mind2Web 2 引入 Agent-as-a-Judge，但评判员对齐未解 | [8] | **假设**：至 2026-12，将出现“评判员对齐基准”，专门评测 LLM 评判员与人类专家的一致性/偏好/鲁棒性；若无则判断失效。 | 70% |

> **不确定**：上述预测均基于当前论文/预印本趋势外推，受算力供给、监管节奏、资本周期多重因素制约，实际落地可能显著滞后或偏离。> 待核实

---

## 经典与奠基性工作

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| AgentBench | 2023 | arXiv [11] | citations>800 | 预印本 | 高 | ★★★★★ | [11] | 多环境统一评测框架，奠基工作 |
| Mind2Web v1 | 2023 | arXiv [9] | citations>500 | 预印本 | 高 | ★★★★★ | [9] | 通用 Web Agent 评测起点 |
| WebShop | 2022 | NeurIPS [10] | citations>1k | 顶会 | 高 | ★★★★★ | [10] | 可扩展真实电商交互环境 |
| SWE-Bench | 2024 | ICML/arXiv [14] | citations>1k | 顶会/官方运营 | 高 | ★★★★★ | [14] | 编码 Agent 事实标准榜单 |
| FMTI 2023/2024 | 2023/2024 | Stanford CRFM [15] | citations>200 | 官方报告 | 高 | ★★★★☆ | [15] | 透明度纵向追踪基线 |

## 核心开源项目与工程基础设施

| 项目 | 年份 | 维护机构 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| LangChain / LangGraph | 2022– | LangChain Inc. | stars>80k | 官方框架 | 高 | ★★★★☆ | > 待核实 | 评测模块化接口，缺欺骗/可纠正插件 |
| AutoGPT | 2023– | Significant Gravitas | stars>150k | 社区驱动 | 高 | ★★★☆☆ | > 待核实 | 早期自主 Agent 代表，评测依赖外部 |
| OpenAI Evals | 2023– | OpenAI | stars>5k | 官方工具 | 中 | ★★★★☆ | > 待核实 | 闭源模型评测标准，可扩展性受限 |
| SWE-Bench Harness | 2024– | Princeton NLP | stars>3k | 官方基准配套 | 高 | ★★★★★ | [14] | 编码 Agent 评测执行环境标准 |

## 关键数据集与基准

| 数据集/基准 | 年份 | 任务/模态 | 规模 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|---|
| SWE-Bench Verified | 2024 | 编码/仓库级 | 2,294 issues | 高 | 官方榜单 | 高 | ★★★★★ | [14] | 事实标准，但存在虚高分 |
| SWE-ABS | 2026 | 编码/对抗 | 同 SWE-Bench | 新 | 预印本 | 高 | ★★★★★ | [3] | 揭示语义错误率 20% |
| SWE-Bench Pro V2 | 2026 | 编码/长程 | 更新任务集 | 新 | 预印本 | 高 | ★★★★★ | [4] | 修复环境漏洞、更难作弊 |
| Mind2Web 2 | 2025 | Web Agentic Search | 130 任务 | 新 | 预印本 | 高 | ★★★★★ | [8] | Agent-as-a-Judge 范式 |
| SVC 2025 | 2025 | 多模态欺骗/音视频 | 多域数据集 | 新 | 挑战赛 | 中 | ★★★★☆ | [12] | 首个跨域多模态欺骗基准 |
| ContamPerc | 2026 | 多 Agent 污染渗透 | 400 场景/10域/50标记 | 新 | 预印本 | 低 | ★★★★★ | [13][2] | 可纠正性量化核心基准 |
| FMTI 2025 | 2025 | 透明度审计 | 多厂商/多维度 | 中 | 官方指数 | 高 | ★★★★☆ | [15] | 透明度倒退实证基线 |

---

## 参考来源
[1] OpenFact at CheckThat! 2024: Combining Multiple Attack Methods for Effective Adversarial Text Generation — http://arxiv.org/abs/2409.02649v2
[2] Contamination Percolation in Multi-Agent LLM Systems: A Measurement Framework and Benchmark — https://doi.org/10.1109/access.2026.3717722
[3] SWE-ABS: Adversarial Benchmark Strengthening Exposes Inflated Success Rates on Test-based Benchmark — http://arxiv.org/abs/2603.00520v1
[4] SWE-Bench Pro V2: A Cleaner, Harder-to-Game Coding Benchmark — http://arxiv.org/abs/2610.24206v2
[5] Saving SWE-Bench: A Benchmark Mutation Approach for Realistic Agent Evaluation — http://arxiv.org/abs/2510.08996v4
[6] SWE-Trail: History-Guided Trajectory Collection for Coding Agent Training — http://arxiv.org/abs/2611.02074v1
[7] SWE-MERA: A Dynamic Benchmark for Agenticly Evaluating Large Language Models on Software Engineering Tasks — http://arxiv.org/abs/2507.11059v3
[8] Mind2Web 2: Evaluating Agentic Search with Agent-as-a-Judge — http://arxiv.org/abs/2506.21506v2
[9] Mind2Web: Towards a Generalist Agent for the Web — http://arxiv.org/abs/2306.06070v3
[10] WebShop: Towards Scalable Real-World Web Interaction with Grounded Language Agents — http://arxiv.org/abs/2207.01206v4
[11] AgentBench: Evaluating LLMs as Agents — http://arxiv.org/abs/2308.03688v3
[12] SVC 2025: the First Multimodal Deception Detection Challenge — http://arxiv.org/abs/2508.04129v1
[13] Contamination Percolation in Multi-Agent LLM Systems: A Measurement Framework and Benchmark — https://doi.org/10.22541/au.177499048.88707055/v1
[14] SWE-bench Goes Live! — http://arxiv.org/abs/2505.23419v2
[15] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1

---

*Generated by research-bot · topic=`agent-评测与欺骗能力基准欺骗可纠正性` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`nvidia/nemotron-3-ultra-550b-a55b` · sources=34 · duration=289s · 2026-11-22T02:12:27+00:00*
