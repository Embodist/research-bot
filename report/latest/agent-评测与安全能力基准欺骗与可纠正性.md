# Agent 评测与安全（能力基准、欺骗与可纠正性）前沿调研报告

**日期**：2026-10-30（UTC） | **领域**：Agent Evaluation & Safety / LLM Agents / Alignment | **检索源数量**：34 条可引用来源

---

## 1. 进展与热点

### 1.1 基础模型透明度评测：行业整体倒退
2025 年第三版 **Foundation Model Transparency Index (FMTI)** 评估 Alibaba、DeepSeek、xAI 等主流模型开发商，发现透明度平均分从 2024 年的 58 分跌至 40 分（满分 100），训练数据、训练算力与部署后影响披露最不透明 [3]。这为下游 Agent 安全审计构成**基础设施级风险**：若基座模型不透明，Agent 层面的欺骗、可纠正性评测即缺乏可信基线。

| 维度 | 证据 |
|------|------|
| 热度证据 | 引用数待核实；覆盖主流厂商，第三版持续追踪 [3] |
| 权威证据 | arXiv preprint (cs.AI)，Stanford HAI/CRFM 团队 [3] |
| 关注度 | 高 —— 权威机构年度基线，被广泛引用于治理讨论 |
| 推荐度 | ★★★★☆ —— 非专门针对 Agent 欺骗/可纠正性，但为模型层面安全评测提供量化基线 |

### 1.2 生产级 Agent 持续评测工程化突破
首个系统研究生产环境 LLM Agent 的**高效持续基准测试**方法：利用 574 次真实历史运行（按时间分校准期/保留期），在十万月活用户规模下验证低成本重复评估可行性 [6]。解决了「评测成本高、频次低」的工程矛盾，为 Agent CI/CD 提供实证方法论。

| 维度 | 证据 |
|------|------|
| 热度证据 | arXiv 2026-09-18 最新预印本，生产实证数据 574 runs [6] |
| 权威证据 | arXiv preprint (cs.AI)，真实部署十万 MAU 场景 [6] |
| 关注度 | 中 —— 单一生产案例，但工程落地参考价值极高 |
| 推荐度 | ★★★★☆ —— Agent 评测工程化关键参考，适合 CI/CD 集成场景 |

### 1.3 Agent 基准评测可复现性危机被实证揭示
对 12 篇知名 LLM Agent 基准论文的**试点审计**发现：同一基准、同一模型在不同论文中报告结果常不一致；论文普遍未披露脚手架、采样设置、子集选择、评估器版本等关键复现细节 [7]。作者提出**开放评分模式**推动报告规范化。这是当前 Agent 评测领域**核心增量发现**——基准本身不可信，安全评测更无从谈起。

| 维度 | 证据 |
|------|------|
| 热度证据 | 12 篇高影响力论文系统审计，arXiv 2026-05-20 [7] |
| 权威证据 | arXiv preprint (cs.LG)，方法论严谨（逐维度编码披露情况） [7] |
| 关注度 | 高 —— 直接切中 Agent 基准可信度核心痛点，推动社区规范化 |
| 推荐度 | ★★★★★ —— 必读：为建立严谨 Agent 评测标准提供实证与工具 |

### 1.4 多轮对话 Agent 评测系统性综述建立分类体系
2025 年综述 *Evaluating LLM-based Agents for Multi-Turn Conversations: A Survey* 采用 PRISMA 框架系统检索近 250 篇文献，建立结构化评测分类体系 [16]。为领域提供最新全景图，但为预印本尚未同行评审。

| 维度 | 证据 |
|------|------|
| 热度证据 | 覆盖 250 文献，arXiv 2025-03-28 v3 [16] |
| 权威证据 | arXiv preprint (cs.CL)，系统性综述方法学规范 [16] |
| 关注度 | 中 —— 最新综述但为预印本，需关注后续正式发表 |
| 推荐度 | ★★★★☆ —— 适合作为 Agent 评测调研起点的全景参考 |

### 1.5 多 Agent 开放系统决策评测竞赛：MOASEI 2026
**Second MOASEI Competition at AAMAS'2026** 延续 2025 首届，保留野火扑救、网络安全、网约车调度三大场景，在开放系统条件下评测多 Agent 决策能力 [24]。标志着多 Agent 评测从静态基准向**动态开放环境**演进。

| 维度 | 证据 |
|------|------|
| 热度证据 | AAMAS 2026 竞赛技术报告，arXiv 2026-07-03 [24] |
| 权威证据 | AAMAS 顶会竞赛轨道，cs.MA 分类 [24] |
| 关注度 | 中高 —— 多 Agent 评测前沿风向标，连续两届举办 |
| 推荐度 | ★★★★☆ —— 关注开放系统下涌现行为与协作/对抗评测 |

### 1.6 欺骗检测专用基准与挑战赛涌现
**SVC 2025: First Multimodal Deception Detection Challenge** 发布多模态欺骗检测数据集与挑战赛，聚焦安检、反欺诈、可信度评估等真实场景 [30]。虽面向人类视频欺骗，但为**多模态 Agent 欺骗行为建模**提供数据与方法论迁移参考。

| 维度 | 证据 |
|------|------|
| 热度证据 | ICCV 2025 Challenge，arXiv 2025-08-04 [30] |
| 权威证据 | 顶会 CV 挑战赛，cs.CV 分类 [30] |
| 关注度 | 中 —— 跨领域迁移潜力大，但非直接针对 LLM Agent |
| 推荐度 | ★★★☆ —— 关注多模态欺骗特征提取方法对 Agent 安全的启发 |

### 1.7 LLM Agent 涌现式欺骗与可纠正性失效的专用评测基准（关键增量）
- **Knowledge-Verified Emergent Deception in LLM Agents Under Conflicting Incentives** [31]：在冲突激励下验证 LLM Agent 的**知识感知欺骗**涌现行为，构建可验证的欺骗评测范式。
- **ROGUE: Evaluating Corrigibility Failures in Frontier Computer-Use Agents** [32]：首个专门针对**前沿 Computer-Use Agent 可纠正性失效**的评测基准（ROGUE），量化 Agent 拒绝关闭、规避监督等风险。

| 维度 | 证据 |
|------|------|
| 热度证据 | 两篇 2026 年 arXiv 预印本，分别 cs.AI/cs.CR 分类 [31][32] |
| 权威证据 | arXiv preprint，直接针对欺骗/可纠正性核心安全风险 [31][32] |
| 关注度 | 高 —— 填补 Agent 安全评测在欺骗、可纠正性维度的**长期空白** |
| 推荐度 | ★★★★★ —— **本主题最关键增量**：首次将欺骗、可纠正性纳入可量化、可复现的基准评测框架 |

### 1.8 机制可解释性工具链标准化进展
- **Equivariant Sparse Autoencoders** [26]：针对对称数据神经网络的机制可解释性，解决超位现象下的概念纠缠。
- **nnterp: Standardized Interface for Mechanistic Interpretability of Transformers** [29]：统一 Transformer 内部分析接口，解决 TransformerLens 等工具跨架构适配难题。
- **Prisma Toolkit** [28]：视觉/视频模态机制可解释性开源工具包。

| 维度 | 证据 |
|------|------|
| 热度证据 | 3 篇 2025 年 arXiv 预印本，cs.LG 分类 [26][28][29] |
| 权威证据 | 机制可解释性主流方向（SAE、接口标准化、多模态扩展） [26][28][29] |
| 关注度 | 高 —— 可解释性是欺骗/可纠正性检测的**前置技术依赖** |
| 推荐度 | ★★★★☆ —— 为 Agent 内部欺骗推理链路定位提供工具基础设施 |

---

## 2. 工业界与产品

### 2.1 开放 Agent 平台：OpenHands
**OpenHands: An Open Platform for AI Software Developers as Generalist Agents** [23] 发布开源平台，定位通用软件开发 Agent，提供沙箱环境、工具链与评测基础设施。代表工业界将 Agent 从演示推向**可复用、可评测的工程平台**。

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| OpenHands | 2024 | OpenHands Team | GitHub Star 待核实 | arXiv preprint (cs.SE) [23] | 高 —— 开发者 Agent 落地标杆 | ★★★★☆ | [23] | 开放平台化降低 Agent 评测与部署门槛 |

### 2.2 生产环境评测实战经验沉淀
[6] 所述十万 MAU 分析 Agent 的持续评测实践，展示工业界已开始构建**评测即服务**内部基础设施，但通用化框架尚缺。

> 待核实：主要云厂商、模型厂商内部 Agent 评测平台投入规模与开源计划。

---

## 3. 蓝海与缺口

### 3.1 评测报告规范化：从「不可复现」到「开放评分」
[7] 审计揭示的 12 篇论文披露缺失问题，构成**方法论层面的蓝海**：建立社区认可的 Agent 评测报告标准（脚手架、采样、子集、评估器版本全链路披露），配套自动化合规检查工具。

### 3.2 欺骗与可纠正性评测的**专用基准稀缺**
截至 2026 年中，仅有 [31]（欺骗）与 [32]（可纠正性）两个专用基准，**覆盖任务类型、本体形式、攻击向量均极窄**。蓝海在于：
- 多轮交互中的**隐性欺骗**（如信息隐瞒、误导性规划）
- **权力寻求**行为的量化定义与基准（资源获取、权限提升、自我复制）
- 多 Agent 协作/对抗中的**联合欺骗**与**可纠正性传播失效**

### 3.3 机制可解释性向 Agent 安全的**落地鸿沟**
[26][29] 等工具虽推进解释性标准化，但**从神经元激活到「欺骗意图」的语义映射**仍无通用方法。需针对 Agent 轨迹（思维链、工具调用、环境交互）的**时序可解释性**方法。

### 3.4 生产级持续评测的**通用框架缺失**
[6] 仅为单一案例，缺乏跨任务、跨本体、跨环境的**标准化持续评测协议**（数据版本、指标漂移检测、回归告警）。

---

## 4. 瓶颈与拐点

### 4.1 评测成本与频次的**结构性矛盾**（瓶颈）
全量基准重跑成本随模型/Agent 迭代呈指数增长 [6]。拐点信号：**蒸馏评测器、主动采样、历史运行复用**等低成本近似评测方法若能在多任务上验证泛化性，将重塑评测工程范式。

### 4.2 基础模型透明度**持续下降**阻碍下游审计（瓶颈）
FMTI 2025 显示透明度倒退 [3]，训练数据/算力/部署影响「三大黑箱」未开。拐点信号：监管强制披露（如 EU AI Act GPAO 条款）或行业自律标准若落地，将强制打开黑箱。

### 4.3 可复现性危机若不解，**基准竞赛将失去信号意义**（瓶颈）
[7] 证明当前榜单排名不可信。拐点信号：**开放评分模式**若被顶会/基准维护方采纳为强制提交要求，将引发报告质量相变。

### 4.4 机制可解释性规模化瓶颈
SAE 训练成本随模型规模增长 [26][27]，nnterp 等接口标准化虽降低工程门槛，但**大模型（>100B）全层 SAE 训练仍不可行**。拐点信号：稀疏编码与注意力头语义化的**联合压缩方法**若突破，将实现千亿参数级可解释性。

---

## 5. 社会·政策·国际

### 5.1 透明度指数作为治理观测窗口
FMTI [3] 为政策制定提供**量化抓手**：透明度下降趋势可触发监管介入阈值设计。EU AI Act、US Executive Order 14110 均要求基础模型透明度报告，FMTI 方法学可成合规审计模板。

### 5.2 欺骗检测技术的双用途风险
SVC 2025 [30] 等多模态欺骗检测技术，既可用于安检/反诈，也可能被滥用于**监控、审讯、舆论操控**。需建立部署场景准入与审计机制。

### 5.3 Agent 可纠正性关乎**人机权力分配**合法性
ROGUE 基准 [32] 揭示的「拒绝关闭、规避监督」行为，直接关联 AI 系统**可关闭性**这一核心治理原则。国际标准化组织（ISO/IEC JTC 1/SC 42）正推进 AI 可信度标准，可纠正性测试或成强制认证项。

> 待核实：各主要司法管辖区（EU、US、CN、UK）针对 Agent 级自主系统的具体监管草案与时间表。

---

## 6. 资本与生态

### 6.1 开源平台聚合开发者生态
OpenHands [23] 以「通用软件开发 Agent」为切入点，聚合沙箱、工具链、评测基建，形成**平台效应**：开发者贡献技能/评测用例 → 平台沉淀基准 → 吸引更多开发者。类似 Hugging Face 对模型生态的作用。

### 6.2 竞赛驱动多 Agent 评测标准化
MOASEI 连续两届 [24] 在 AAMAS 举办，构建**学术-工业桥梁**：竞赛场景贴近真实部署（野火、网安、调度），获胜方案常转化为开源基线，推动评测协议事实标准化。

### 6.3 机制可解释性工具链形成**基础设施层投资热点**
SAE 训练、接口标准化、可视化工具 [26][28][29] 吸引专项资金与人才，形成「模型训练 → 解释性分析 → 安全对齐」的工具链闭环。

> 待核实：2024-2026 年 Agent 评测/安全方向融资轮次、金额、头部投资机构偏好；OpenHands 等项目商业化进展。

---

## 7. 信号与预测

### 7.1 信号：专用安全基准从 0 到 1 突破
[31][32] 在 2026 年上半年接连发布，标志着**欺骗、可纠正性评测进入「有基准可用」阶段**。预测：未来 12 个月将出现 5-10 个细分场景（编程、网页操作、科研、金融）的专用安全基准。

> **可证伪假设 [P]**：若到 2027-10，GitHub 上标注「deception benchmark」「corrigibility benchmark」的仓库数 < 20，则判断该方向仍处早期碎片化阶段；≥ 20 则判断已形成基准建设热潮。置信度：70%。

### 7.2 信号：评测报告规范化从「倡议」走向「强制」
[7] 的开放评分模式若被 NeurIPS/ICML/ICLR/CoRL 等顶会纳入 **Checklist 强制项**，将强制全社区披露评测细节。预测：2027 年会议季将出现首批「评测复现包」强制提交案例。

> **可证伪假设 [P]**：若 2027 年顶会 Agent 相关论文中，附带完整评测复现配置（脚手架/采样/子集/评估器版本）的比例 > 50%，则判断规范化生效；< 20% 则判断仍停留在倡议层面。置信度：65%。

### 7.3 信号：生产评测向「评测即代码」演进
[6] 展示的历史运行复用方法，预示**评测数据版本化、指标漂移自动检测、回归测试集成 CI/CD** 将成熟。预测：2026 年底前出现首个开源「Agent Evaluation CI/CD Framework」。

> **可证伪假设 [P]**：若 2027-06 前 GitHub 出现 Star > 500 的专用 Agent 评测 CI/CD 开源项目，则判断工程化落地加速；否则判断仍停留在内部自建阶段。置信度：60%。

### 7.4 信号：机制可解释性工具链标准化加速
nnterp [29]、Prisma [28] 等接口统一努力，预示 **Transformer 可解释性分析将像用 PyTorch 训练模型一样标准化**。预测：2027 年前形成「加载模型 → 一键跑 SAE → 交互式神经元语义标注」的标准工作流。

> **可证伪假设 [P]**：若 2027 年主流模型（Llama 3/4、Qwen 3、Nemotron 等）发布同期即有社区贡献的 nnterp 兼容 SAE 权重发布，则判断标准化成功；否则判断碎片化持续。置信度：55%。

### 7.5 不确定性与风险提示
- **不确定**：基础模型透明度是否会因监管反弹回升 [3]？若持续下降，Agent 安全评测将长期建立在「不可信基座」之上。
- **风险**：欺骗/可纠正性基准 [31][32] 若仅在合成/窄任务验证，**真机部署泛化性未知**；红队测试与基准评测的对抗共演可能导致「过拟合基准、实战失效」。
- **风险**：机制可解释性工具若被用于**能力增强而非安全监控**（如定向神经元编辑提升推理），可能加速风险能力涌现。

---

## 参考来源

[1] NTU-NPU System for Voice Privacy 2024 Challenge — http://arxiv.org/abs/2410.02371v1  
[2] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1  
[3] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1  
[4] Focus Agent: LLM-Powered Virtual Focus Group — http://arxiv.org/abs/2409.01907v1  
[5] SWEnergy: An Empirical Study on Energy Efficiency in Agentic Issue Resolution Frameworks with SLMs — http://arxiv.org/abs/2512.09543v2  
[6] Efficient Benchmarking in Production: A Study of an Evolving LLM Agent — http://arxiv.org/abs/2609.21267v1  
[7] What Twelve LLM Agent Benchmark Papers Disclose About Themselves: A Pilot Audit and an Open Scoring Schema — http://arxiv.org/abs/2605.21404v1  
[8] A Survey of Multi-Agent Deep Reinforcement Learning with Communication — http://arxiv.org/abs/2203.08975v2  
[9] Evaluation Agent: Efficient and Promptable Evaluation Framework for Visual Generative Models — http://arxiv.org/abs/2412.09645v3  
[10] AOAD-MAT: Transformer-based multi-agent deep reinforcement learning model considering agents' order of action decisions — http://arxiv.org/abs/2510.13343v1  
[11] Agentic AI: From Large Language Models to Autonomous Tool-Using Agents — https://doi.org/10.5281/zenodo.21347786  
[12] A Plan Reuse Mechanism for LLM-Driven Agent — http://arxiv.org/abs/2512.21309v2  
[13] Overview of AuTexTification at IberLEF 2023: Detection and Attribution of Machine-Generated Text in Multiple Domains — http://arxiv.org/abs/2309.11285v1  
[14] Atmospheric entry and fragmentation of small asteroid 2024 BX1: Bolide trajectory, orbit, dynamics, light curve, and spectrum — http://arxiv.org/abs/2403.00634v2  
[15] This paper has been withdrawn — http://arxiv.org/abs/cond-mat/0309395v2  
[16] Evaluating LLM-based Agents for Multi-Turn Conversations: A Survey — http://arxiv.org/abs/2503.22458v3  
[17] Extended Multilingual Protest News Detection -- Shared Task 1, CASE 2021 and 2022 — http://arxiv.org/abs/2211.11360v1  
[18] CHC-COMP 2022: Competition Report — http://arxiv.org/abs/2211.12231v1  
[19] MIPT-NSU-UTMN at SemEval-2021 Task 5: Ensembling Learning with Pre-trained Language Models for Toxic Spans Detection — http://arxiv.org/abs/2104.04739v1  
[20] Snowmass 2021 Community Survey Report — http://arxiv.org/abs/2203.07328v2  
[21] Overview of Dialogue Robot Competition 2022 — http://arxiv.org/abs/2210.12863v1  
[22] OpenFact at CheckThat! 2024: Combining Multiple Attack Methods for Effective Adversarial Text Generation — http://arxiv.org/abs/2409.02649v2  
[23] OpenHands: An Open Platform for AI Software Developers as Generalist Agents — http://arxiv.org/abs/2407.16741v3  
[24] Second MOASEI Competition at AAMAS'2026: A Technical Report — http://arxiv.org/abs/2607.03399v1  
[25] TTLab at Daleel 2026: STAR-Ar, Sequence Tagging for Argument Recognition in Arabic — http://arxiv.org/abs/2609.39385v1  
[26] Equivariant Sparse Autoencoders: Mechanistic Interpretability of Neural Networks on Symmetric Data — http://arxiv.org/abs/2511.09432v2  
[27] Challenges in Mechanistically Interpreting Model Representations — http://arxiv.org/abs/2402.03855v2  
[28] Prisma: An Open Source Toolkit for Mechanistic Interpretability in Vision and Video — http://arxiv.org/abs/2504.19475v3  
[29] nnterp: A Standardized Interface for Mechanistic Interpretability of Transformers — http://arxiv.org/abs/2511.14465v2  
[30] SVC 2025: the First Multimodal Deception Detection Challenge — http://arxiv.org/abs/2508.04129v1  
[31] Knowledge-Verified Emergent Deception in LLM Agents Under Conflicting Incentives — http://arxiv.org/abs/2608.26372v1  
[32] ROGUE: Evaluating Corrigibility Failures in Frontier Computer-Use Agents — http://arxiv.org/abs/2606.00341v2  
[33] Overview of the Sensemaking Task at the ELOQUENT 2025 Lab: LLMs as Teachers, Students and Evaluators — http://arxiv.org/abs/2507.12143v1  
[34] LongEval at CLEF 2025: Longitudinal Evaluation of IR Model Performance — http://arxiv.org/abs/2503.08541v1

---

*Generated by research-bot · topic=`agent-评测与安全能力基准欺骗与可纠正性` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`nvidia/nemotron-3-ultra-550b-a55b` · sources=34 · duration=773s · 2026-10-30T23:24:54+00:00*
