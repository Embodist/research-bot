# AgentGuard：LLM 护栏与 Agent 安全前沿调研报告

**日期**：2026-11-21 | **领域**：LLM Agent 安全 / 护栏工程 / 提示注入防御 / 沙箱与最小权限 / 红队基准  
**检索源数量**：28 条可引用证据源（含 arXiv 预印本、期刊文章、官方 GitHub 仓库、竞赛数据集）

---

## 1. 进展与热点

### 1.1 同名双轨 AgentGuard 工作：工具编排评估与编码代理执行护栏学习
2025-2026 年出现两篇同名但方法迥异的 **AgentGuard** 预印本，分别切入工具编排安全评估与编码代理执行护栏自动学习，显示该细分方向命名尚未收敛、研究范式正在快速分化 [1][2]。

| 维度 | AgentGuard (cs.CR, 2025-02) | AgentGuard (cs.SE, 2026-09) |
|------|----------------------------|----------------------------|
| 核心贡献 | 将代理编排器重新用于**自主发现并验证不安全工具使用工作流**，生成安全护栏 [1] | 从**异常编码代理轨迹**自动提取失败模式，泛化为**指令级条件执行约束**，动态激活轻量级护栏技能 [2] |
| 威胁模型 | 工具滥用、恶意工作流编排 | 代码执行异常、长尾执行风险、过度代理 |
| 方法范式 | 攻击者视角的红队式自动评估 → 护栏合成 | 从负样本（异常轨迹）学习正向约束 → 运行时动态激活 |
| 证据等级 | B（arXiv 预印本，未同行评审） | B（arXiv 预印本，未同行评审） |
| 热度证据 | > 待核实（引用数、下载量未公开） | > 待核实（2026-09 最新，引用数为 0） |
| 权威证据 | arXiv cs.CR，作者机构未在摘要披露 | arXiv cs.SE，作者机构未在摘要披露 |
| 关注度 | 中 | 中 |
| 推荐度 | ★★★☆☆ | ★★★★☆ |

> **增量判断**：相对 2024 年前以静态规则、分类器检测为主的护栏范式，2026 年 AgentGuard (cs.SE) 引入**从异常轨迹自动学习 + 指令级动态激活**的新范式，标志着护栏工程从「人工规则覆盖」向「数据驱动自动化 + 上下文感知激活」转型 [2]。

### 1.2 基础模型透明度倒退：护栏可审计性的宏观制约
2025 年 **Foundation Model Transparency Index (FMTI) 第三版**显示，行业平均透明度分数从 58 分降至 40 分，训练数据、算力、部署后影响三大维度最不透明 [3]。这直接导致 Agent 护栏难以覆盖上游模型的未知能力边界，构成结构性**风险**。

| 指标 | 2024 版 | 2025 版 | 变化 |
|------|---------|---------|------|
| 平均透明度分数 | 58 | 40 | -18 分 |
| 最不透明维度 | 训练数据、算力、部署后影响 | 同上 | 无改善 |
| 新增评估对象 | — | Alibaba、DeepSeek、xAI | 覆盖面扩大 |

- **热度证据**：年度权威基准，社区广泛引用 [3]
- **权威证据**：arXiv cs.AI，作者含 Percy Liang 等知名学者，第三版年度指数 [3]
- **关注度**：高 | 影响政策与工程实践的宏观证据
- **推荐度**：★★★★☆ | 必引背景文献，说明护栏建设的外部约束环境

### 1.3 护栏理论范式转向：从「拒绝」到「恢复」的控制理论视角
2025 年提出 **From Refusal to Recovery** 框架，主张将生成式 AI 安全视为**序贯决策问题**，而非单纯输出分类；有害条件检测后应提供恢复路径而非仅拒绝 [4]。这为下一代护栏架构提供了理论增量。

- **热度证据**：> 待核实（2025-10 预印本，引用数未公开）
- **权威证据**：arXiv cs.AI，v2 版本 [4]
- **关注度**：中 | 学术界关注度上升的新理论框架
- **推荐度**：★★★★☆ | 理论前沿，指导工程架构演进

### 1.4 统一检测框架探索：UniGuardian 多威胁联合防御
2025 年提出 **UniGuardian**，统一检测提示注入、后门攻击、对抗攻击三类威胁 [5]，体现防御侧向**多威胁融合检测**演进的趋势。

- **热度证据**：> 待核实
- **权威证据**：arXiv cs.CR，v2 版本 [5]
- **关注度**：中
- **推荐度**：★★★☆☆ | 多威胁统一检测方向有参考价值，但工程落地细节待补全

---

## 2. 工业界与产品

### 2.1 NeMo Guardrails：当前最成熟的开源护栏工程框架
NVIDIA 官方维护的 **NeMo Guardrails** 为主流开源护栏工具包，支持可编程 rails、对话流控制、话题限制、语言风格约束等工程化功能 [6]。

| 项目 | 详情 |
|------|------|
| 名称 | NeMo Guardrails |
| 年份 | 2023 |
| 机构/作者 | NVIDIA |
| 热度证据 | GitHub 星标数高、社区活跃、生产环境有采用案例 [6] |
| 权威证据 | NVIDIA 官方开源项目，配套 arXiv 论文 [6] |
| 关注度 | 高 | 生态成熟度最高的开源护栏框架 |
| 推荐度 | ★★★★★ | 工程落地首选，直接对应主流开源护栏框架 |
| 链接 | https://github.com/NVIDIA/NeMo-Guardrails |
| 说明 | 支持可编程 rails、对话流控制、话题限制、语言风格约束；与 LangChain/LlamaIndex 集成良好 |

### 2.2 沙箱运行时与 LLM 防火墙：公开工程文献缺失
候选证据中**未覆盖**沙箱运行时（如 gVisor、Firecracker 在 Agent 场景的适配）与 LLM 防火墙（如 LlamaGuard、Prompt Guard 等生产级部署）的工程实践文献 [q3-open_problems]。

> 待核实：主流云厂商（AWS/Azure/GCP）的 Agent 沙箱产品化进展、开源社区（如 E2B、Modal）的运行时安全实践。

### 2.3 伦理/合规护栏框架：AI Ethics by Design
2024 年提出可定制伦理护栏框架，强调规则、策略与 AI 助手集成以适应多样化用户价值观 [7]，为合规层面提供参考但工程细节较少。

- **热度证据**：> 待核实
- **权威证据**：arXiv cs.CY，v2 版本 [7]
- **关注度**：低
- **推荐度**：★★★☆☆ | 适合关注合规与治理的工程团队参考

---

## 3. 蓝海与缺口

综合三个子问题的开放问题，提炼以下高杠杆**蓝海方向**：

| # | 蓝海缺口 | 说明 | 关联证据 |
|---|----------|------|----------|
| 1 | **跨任务/跨本体统一护栏评测基准缺失** | 无通用安全性指标覆盖提示注入、越狱、工具滥用、过度代理的联合评测 | [q1-open_problems][q2-open_problems] |
| 2 | **自动化护栏学习在真机长周期部署的鲁棒性未验证** | AgentGuard (cs.SE) 等自动学习方法缺乏真机连续运行的误报率/漏报率数据 | [2][q1-open_problems] |
| 3 | **上游模型透明度下降导致的「未知未知」风险覆盖** | FMTI 显示透明度倒退，护栏难以审计模型内部未知能力边界 | [3][q1-open_problems] |
| 4 | **护栏与自主性的动态平衡机制** | 过度限制降低任务成功率、过度放松引发事故，缺乏在线自适应调节理论与实现 | [q1-open_problems][4] |
| 5 | **多模态/多智能体场景下护栏一致性与性能开销基准** | 无标准化基准测试多模态输入、多智能体协作下的护栏一致性保证 | [q3-open_problems][8] |
| 6 | **组合威胁下的联合防御评测框架** | 现有防御多针对单一威胁（提示注入），缺乏注入+越狱+工具滥用组合攻击的联合防御基准 | [q2-open_problems][5] |
| 7 | **护栏框架与编排层的标准化集成接口** | NeMo Guardrails 等与 LangChain/LlamaIndex/AutoGen 等编排层缺乏行业共识接口 | [q3-open_problems] |

> **增量判断**：相对 2023-2024 年以单点检测器、静态规则为主的工程现状，上述缺口指向**自动化学习、动态激活、统一评测、标准化集成**四大方向的系统性机会。

---

## 4. 瓶颈与拐点

### 4.1 核心瓶颈

| 瓶颈 | 表现 | 证据来源 |
|------|------|----------|
| **评测基准碎片化** | 无统一基准覆盖四大威胁模型；红队基准多为单任务、单模态 | [q1-open_problems][q2-open_problems][5] |
| **上游透明度倒退** | FMTI 平均分 58→40，训练数据/算力/部署后影响最不透明，护栏无法审计模型内部能力边界 | [3] |
| **静态规则/分类器的长尾覆盖失效** | 人工规则难以覆盖长尾风险；分类器依赖标签数据，对新危险情况脆弱 | [4][2] |
| **护栏与任务成功率的零和博弈** | 过度限制导致拒绝率上升、任务失败；动态平衡机制缺失 | [q1-open_problems][4] |
| **工程集成标准缺失** | 护栏框架与推理引擎/编排层无标准化接口，集成成本高 | [q3-open_problems] |

### 4.2 拐点信号

| 拐点方向 | 信号 | 判断依据 | 不确定性 |
|----------|------|----------|----------|
| **自动化护栏学习 → 生产可用** | AgentGuard (cs.SE) 实现从异常轨迹自动提取约束 + 动态激活 [2] | 方法具备工程落地潜力，但缺乏真机长周期验证 | **较大概率** 需 6-12 个月开源复现与基准测试验证 |
| **控制理论范式 → 架构重构** | From Refusal to Recovery 提出序贯决策视角 [4] | 理论完备度高，但工程落地路径不明 | **推测** 需框架级重构（如 NeMo Guardrails 2.0） |
| **透明度治理 → 强制合规** | FMTI 持续下降、EU AI Act 等法规推进 [3] | 外部压力倒逼上游开放，可能改变护栏构建前提 | **需要数据** 取决于监管执行力度与行业自律 |
| **统一红队基准 → 行业标准** | UniGuardian 多威胁统一检测 [5]、HackAPrompt 持续运营 [9] | 社区呼声高，但缺乏权威主导组织 | **不确定** 可能由 NIST/MLCommons/学术联盟推动 |

---

## 5. 社会·政策·国际

### 5.1 透明度治理与合规压力
2025 FMTI 揭示基础模型开发者透明度整体倒退，训练数据、算力、部署后影响最不透明 [3]。这直接影响：
- **可审计性**：护栏无法基于完整模型卡构建精准威胁模型
- **合规风险**：EU AI Act、美国行政命令要求高风险 AI 系统具备透明度与风险管理文档
- **供应链安全**：下游 Agent 开发者面临「黑盒上游」的系统性**风险**

### 5.2 伦理护栏与价值观对齐的多元化需求
AI Ethics by Design 框架强调可定制护栏适应多样化用户价值观 [7]，反映：
- 全球化部署需满足不同司法辖区的内容安全标准
- 企业级应用需支持租户级策略定制（如金融/医疗/教育垂域合规）
- **地缘政治**因素可能导致护栏规则集的分裂与碎片化

### 5.3 红队基准的国际化与标准化趋势
HackAPrompt 等众包红队竞赛持续运营 [9]，UniGuardian 探索多威胁统一检测 [5]，显示社区向**标准化红队评测**聚合，但尚未形成国际标准（如 ISO/IEC 42001 关联测试规范）。

> 待核实：NIST AI RMF、MLCommons、ISO/IEC JTC1 SC42 在 Agent 安全测试标准上的最新进展。

---

## 6. 资本与生态

### 6.1 核心开源项目生态图谱

| 项目 | 机构 | 星标/活跃度 | 定位 | 生态集成 |
|------|------|-------------|------|----------|
| **NeMo Guardrails** | NVIDIA | 高 [6] | 通用可编程护栏框架 | LangChain、LlamaIndex、AutoGen、OpenAI API |
| **HackAPrompt** | 社区/竞赛 | 中高 [9] | 提示注入红队数据集与基准 | 评测基准、检测器训练数据源 |
| **AgentGuard (cs.SE)** | 未披露 | 低（2026-09 新） | 编码代理执行护栏自动学习 | 暂无公开集成 |
| **AgentGuard (cs.CR)** | 未披露 | 低（2025-02） | 工具编排安全自主评估 | 暂无公开集成 |

### 6.2 人才与投资流向信号
- **NVIDIA** 持续投入 NeMo Guardrails 生态，体现算力厂商向上游安全工具链延伸 [6]
- **学术界** 从静态检测转向自动化学习（AgentGuard cs.SE）、控制理论（Refusal to Recovery）、多威胁统一检测，显示研究资金向**自动化、动态、统一**方向倾斜 [2][4][5]
- **缺乏** 专门针对 Agent 沙箱运行时、LLM 防火墙的大规模开源项目与商业融资公开信息

> 待核实：E2B、Modal、Firecracker 等沙箱厂商的融资轮次、Agent 安全初创公司（如 Lakera、Prompt Security、Protect AI）的最新融资与产品路线图。

---

## 7. 信号与预测

### 7.1 早期信号

| 信号 | 来源 | 时间 | 强度 |
|------|------|------|------|
| 同名双轨 AgentGuard 出现，命名空间未收敛 | [1][2] | 2025-02 / 2026-09 | 中 |
| 从异常轨迹自动学习护栏 + 动态激活范式首现 | [2] | 2026-09 | 中高 |
| 控制理论「拒绝→恢复」范式提出 | [4] | 2025-10 | 中 |
| FMTI 透明度连续两年下降 | [3] | 2025-12 | 高 |
| 多威胁统一检测框架探索 | [5] | 2025-02 | 中 |

### 7.2 未来 6-18 月预判（可证伪假设）

| # | 预测 | 依据链 | 可证伪条件 | 置信度 |
|---|------|--------|------------|--------|
| P1 | **AgentGuard (cs.SE) 或同类自动化护栏学习方法将在 2026 年底前开源，并在 SimplerEnv/LIBERO 等基准上公布真机评测结果** | 方法具备工程落地设计（轻量级技能、动态激活）[2]；社区对自动化护栏需求强烈 | 若 2026-12-31 前无开源仓库或无真机基准报告，则判断不成立 | 较大概率 (70%) |
| P2 | **NeMo Guardrails 将在 2027 年上半年发布 2.0 版本，引入控制理论恢复机制与标准化编排层接口** | NVIDIA 持续维护 [6]；学术界提出理论范式 [4]；工程集成痛点明确 [q3-open_problems] | 若 2027-06-30 前无 2.0 发布或无恢复机制/标准接口，则判断不成立 | 推测 (50%) |
| P3 | **MLCommons 或 NIST 将在 2027 年前发布 Agent 安全评测基准 v1.0，覆盖提示注入/越狱/工具滥用/过度代理四大威胁模型** | 社区呼声高 [q1-open_problems][q2-open_problems]；UniGuardian 等多威胁融合探索 [5]；HackAPrompt 持续运营 [9] | 若 2027-12-31 前无权威机构发布此类基准，则判断不成立 | 推测 (40%) |
| P4 | **基础模型透明度将在 2026-2027 年触底反弹，受 EU AI Act 执行与保险/合规压力驱动** | FMTI 下降趋势 [3]；监管时间表明确；企业合规成本上升 | 若 2027 年 FMTI 平均分仍 < 45，则判断不成立 | 需要数据 (不确定) |

### 7.3 关键不确定性

| 不确定性 | 影响 | 观测指标 |
|----------|------|----------|
| 自动化护栏学习的**误报率在真机长周期**能否控制在 < 1% | 决定能否用于生产环境 | AgentGuard 等开源项目的真机部署报告 |
| 控制理论恢复机制的**计算开销与延迟**是否满足实时交互需求 | 决定架构重构可行性 | NeMo Guardrails / LangGraph 等框架的原型实现基准 |
| 监管对**开源模型透明度**的强制力度 | 决定上游风险可审计性改善速度 | EU AI Act 执法案例、美国行政命令落地细则 |
| 红队基准的**标准化主导权**归属（学术 vs 产业 vs 政府） | 决定评测生态统一时间线 | MLCommons/NIST/ISO 相关工作组进展 |

---

## 经典与奠基性工作

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| Automatic and Universal Prompt Injection Attacks against Large Language Models | 2024 | arXiv cs.AI | > 待核实 | arXiv 预印本 | 中 | ★★★★☆ | [10] | 首个系统性自动化通用提示注入攻击方法，定义攻击面与评测基准 |
| SecAlign: Defending Against Prompt Injection with Preference Optimization | 2024 | arXiv cs.CR | > 待核实 | arXiv 预印本 v3 | 中高 | ★★★★☆ | [11] | 从模型对齐/偏好优化角度防御提示注入，关注外部数据源注入面 |
| Detecting Prompt Injection Attacks Against Application Using Classifiers | 2025 | arXiv cs.CR | > 待核实 | arXiv 预印本 | 中 | ★★★☆☆ | [9] | 基于 HackAPrompt 语料库构建检测数据集，训练多种经典分类器基线 |
| Agentic workflows in large language models: a comprehensive review | 2026 | Discover Computing | citations=0 [8] | 期刊同行评审 | 低 | ★★★☆☆ | [8] | 系统梳理 Agentic 架构/规划/工具使用/多智能体，指出分类混淆问题 |
| NeMo Guardrails: A Toolkit for Controllable and Safe LLM Applications | 2023 | NVIDIA / arXiv cs.CL | > 待核实 | arXiv 预印本 + 官方开源 | 高 | ★★★★★ | [6] | 主流开源护栏框架奠基性论文，详述可编程 rails 架构 |
| From Refusal to Recovery: A Control-Theoretic Approach to Generative AI Guardrails | 2025 | arXiv cs.AI | > 待核实 | arXiv 预印本 v2 | 中 | ★★★★☆ | [4] | 提出护栏从静态拒绝转向动态恢复的控制理论新范式 |
| AI Ethics by Design: Implementing Customizable Guardrails for Responsible AI Development | 2024 | arXiv cs.CY | > 待核实 | arXiv 预印本 v2 | 低 | ★★★☆☆ | [7] | 伦理治理视角的可定制护栏框架，补充合规与价值观对齐维度 |
| UniGuardian: A Unified Defense for Detecting Prompt Injection, Backdoor and Adversarial Attacks | 2025 | arXiv cs.CR | > 待核实 | arXiv 预印本 v2 | 中 | ★★★☆☆ | [5] | 统一检测提示注入/后门/对抗攻击的多威胁融合框架 |
| The 2025 Foundation Model Transparency Index | 2025 | arXiv cs.AI | > 待核实 | arXiv 预印本，年度权威指数第三版 | 高 | ★★★★☆ | [3] | 量化基础模型透明度下降趋势，为护栏可审计性提供宏观证据 |

---

## 开源项目

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| NeMo Guardrails | 2023 | NVIDIA | GitHub 星标高、社区活跃、生产采用 [6] | NVIDIA 官方开源 | 高 | ★★★★★ | https://github.com/NVIDIA/NeMo-Guardrails | 通用可编程护栏框架，支持对话流控制、话题限制、风格约束，生态集成最完善 |
| HackAPrompt Playground | 2023-持续 | 社区/竞赛官方 | 红队基准常用数据源 [9] | 竞赛官方发布 | 中高 | ★★★★☆ | https://hackaprompt.com/ | 提示注入攻击样本大规模众包语料库，核心训练/评测数据集 |

> 待核实：AgentGuard (cs.SE/cs.CR) 官方开源仓库、E2B/Modal 等沙箱运行时的 Agent 安全适配项目、LlamaGuard/Prompt Guard 等防火墙组件开源情况。

---

## 数据集与基准

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| HackAPrompt Playground Submissions corpus | 2023-持续 | HackAPrompt 竞赛官方 | 社区公认基准 [9] | 官方发布，被 [9] 用于构建检测数据集 | 中高 | ★★★★☆ | https://hackaprompt.com/ | 提示注入攻击样本大规模众包语料库，核心训练/评测数据源 |
| Foundation Model Transparency Index (FMTI) 2025 | 2025 | Stanford CRFM 等 | 年度权威指数第三版 [3] | Percy Liang 等知名学者主导 | 高 | ★★★★☆ | [3] | 量化基础模型开发者透明度的基准，间接反映护栏可审计性环境 |

> 待核实：LIBERO/SimplerEnv/Open X-Embodiment 等具身基准中的安全子集、AgentBench/ToolBench 中的安全评测分榜、红队专用基准（如 Red-Teaming Benchmark、JailbreakBench）最新版本。

---

## 参考来源
[1] AgentGuard: Repurposing Agentic Orchestrator for Safety Evaluation of Tool Orchestration — http://arxiv.org/abs/2502.09809v1
[2] AgentGuard: Learning Execution Guardrails from Anomalous Coding-Agent Trajectories — http://arxiv.org/abs/2609.16287v1
[3] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1
[4] From Refusal to Recovery: A Control-Theoretic Approach to Generative AI Guardrails — http://arxiv.org/abs/2510.13727v2
[5] UniGuardian: A Unified Defense for Detecting Prompt Injection, Backdoor Attacks and Adversarial Attacks in Large Language Models — http://arxiv.org/abs/2502.13141v2
[6] NeMo Guardrails: A Toolkit for Controllable and Safe LLM Applications with Programmable Rails — http://arxiv.org/abs/2310.10501v1
[7] AI Ethics by Design: Implementing Customizable Guardrails for Responsible AI Development — http://arxiv.org/abs/2411.14442v2
[8] Agentic workflows in large language models: a comprehensive review of architectures, planning strategies, and real-world applications — https://doi.org/10.1007/s10791-026-10743-4
[9] Detecting Prompt Injection Attacks Against Application Using Classifiers — http://arxiv.org/abs/2512.12583v1
[10] Automatic and Universal Prompt Injection Attacks against Large Language Models — http://arxiv.org/abs/2403.04957v1
[11] SecAlign: Defending Against Prompt Injection with Preference Optimization — http://arxiv.org/abs/2410.05451v3

---

*Generated by research-bot · topic=`agentguardllm-护栏与-agent-安全提示注入越狱工具滥用与过度代理沙箱与最小权限llm-firewall` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`nvidia/nemotron-3-ultra-550b-a55b` · sources=28 · duration=441s · 2026-11-21T03:46:21+00:00*
