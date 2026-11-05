# Agent 评测与安全（能力基准、欺骗与可纠正性）深度调研报告

**日期**：2026-11-05 | **领域**：Agent Evaluation & Safety (Capability Benchmarks, Deception, Corrigibility) | **检索源数量**：31

---

## 1. 进展与热点

### 1.1 最新评测范式创新：多角色协作评测
- **ELOQUENT 2025 Sensemaking 共享任务** 首创 **LLMs 作为教师、学生、评估者** 的三阶段评测范式，覆盖 7 个测试源（事实核查、教科书、讲座转录、教育视频）及英/德/乌/捷四语言，为生成式语言模型提供可复现的高层评测基准 [8]。  
  - **热度证据**：arXiv 预印本，引用数 > 待核实 [8]  
  - **权威证据**：ELOQUENT Lab 官方共享任务概述论文 (cs.CL) [8]  
  - **关注度**：中 —— 新发布共享任务，社区关注度尚在建立中 [8]  
  - **推荐度**：★★★★☆ —— 首创三角色评测范式，多语言多源材料，对 Agent 评测方法论有参考价值 [8]

### 1.2 多模态欺骗检测基准空白被填补
- **SVC 2025** 发布**首个多模态欺骗检测挑战赛**，旨在解决现有研究多局限于单领域、缺乏高质量多样欺骗样本的问题，推动跨域多模态欺骗检测基准建设，面向安全筛查、欺诈防范、可信度评估等真实场景 [10]。  
  - **热度证据**：arXiv 预印本，挑战赛首届，参赛队伍数 > 待核实 [10]  
  - **权威证据**：SVC 2025 官方挑战赛论文 (cs.CV) [10]  
  - **关注度**：中 —— 首个同类挑战赛，吸引安全与多模态社区关注 [10]  
  - **推荐度**：★★★★☆ —— 填补多模态欺骗检测基准空白，对具身智能中 Agent 诚实性评测有直接启发 [10]

### 1.3 基础模型透明度整体倒退，治理风险上升
- **2025 基础模型透明度指数（FMTI 第 3 版）** 显示平均分从 2024 年的 58 **降至 40**，新增数据获取、使用数据、监控指标，首次评估 Alibaba、DeepSeek、xAI 等公司；训练数据与算力、部署后使用影响最不透明 [5]。  
  - **热度证据**：连续三年追踪，被广泛引用的透明度基准，政策与产业界关注度高 [5]  
  - **权威证据**：arXiv 预印本 (cs.AI)，斯坦福 HAI 等机构发布 [5]  
  - **关注度**：高 —— 直接关联 Agent 安全治理与可审计性 [5]  
  - **推荐度**：★★★★★ —— 权威纵向追踪基础模型透明度，**增量** 表现为透明度显著下降，揭示治理**风险** [5]

### 1.4 其他近期评测基准进展
- **LongEval at CLEF 2025** 引入纵向评测范式，关注 IR 模型性能随时间漂移 [9]。  
- **ALTA 2024 Shared Task** 聚焦检测人机混合文章中的 AI 生成句子 [26]。  
- **CheckThat! 2024** 探索对抗性文本生成以评测事实核查鲁棒性 [7]。  
- **线性探针检测策略性欺骗** 方法提出，为可纠正性提供潜在技术路径 [11]。

---

## 2. 工业界与产品

- **本周期无显著变化**：提供的 31 个证据源中，**未包含** 具身智能/VLA/机器人领域或通用 Agent 领域的工业级产品发布、商业化部署案例、厂商安全工具链开源等工业界动态 [5, 8, 10, 28, 30, 31]。  
  - > 待核实：主流大模型厂商（OpenAI, Anthropic, Google, 国内头部厂商）在 Agent 评测平台、红队测试服务、可纠正性对齐产品上的最新发布与落地情况。  
  - **关注度**：低（基于现有证据）  
  - **推荐度**：★☆☆☆ —— 证据缺失，无法形成工业界图谱，需补充检索技术博客、发布会、财报会议纪要。

---

## 3. 蓝海与缺口

### 3.1 具身智能/VLA 专用评测与安全工具链缺失
- 候选证据 [28, 30, 31] 涉及通用迁移学习工具包、希腊语 NLP 工具包、AGI 安全理论建模，**均不涉及** 机器人本体、VLA 模型、ROS2 部署、仿真评测基准、实时安全控制器等工程栈要素 [28, 30, 31]。  
  - **热度证据**：GitHub Stars/下载量 > 待核实 [28, 30]  
  - **权威证据**：arXiv 预印本 (cs.LG/cs.CL/cs.AI) [28, 30, 31]  
  - **关注度**：低 —— 领域不匹配，无法为机器人开源项目选型提供参考 [28, 30, 31]  
  - **推荐度**：★☆☆☆ —— 仅说明通用 ML 工具包开源范式，需另寻机器人专用工程框架（如 Open X-Embodiment, LeRobot, Isaac Lab）[28, 30, 31]

### 3.2 多模态欺骗检测跨域泛化能力不足
- SVC 2025 指出现有研究多局限于单领域，缺乏高质量多样欺骗样本，跨域泛化为核心**蓝海** [10]。

### 3.3 基础模型透明度治理机制滞后
- FMTI 2025 揭示训练数据、算力披露、部署后影响评估三大维度最不透明，标准化审计协议与强制披露机制为政策**蓝海** [5]。

---

## 4. 瓶颈与拐点

### 4.1 透明度倒退构成治理瓶颈
- FMTI 平均分下降 18 分（58→40），表明**自愿性透明度机制失效**，监管介入或行业自律标准化为必然**拐点信号** [5]。

### 4.2 评测范式从静态基准向动态交互演进
- ELOQUENT 2025 三角色范式（教师-学生-评估者）标志着评测从“静态数据集分数”向“动态交互过程评价”的**拐点**转移 [8]。

### 4.3 欺骗检测从单模态走向多模态融合
- SVC 2025 首个多模态挑战赛确立了“文本-音频-视频联合欺骗检测”为新技术**瓶颈**突破方向 [10]。

### 4.4 可纠正性技术缺乏标准化度量
- 线性探针等方法虽在特定任务有效 [11]，但跨模型、跨任务、真机部署下的**可纠正性量化指标**仍缺失，为核心**瓶颈**。

---

## 5. 社会·政策·国际

### 5.1 透明度指数成为政策参考锚点
- FMTI 2025 首次纳入 Alibaba、DeepSeek、xAI，覆盖中美主要模型厂商，为**国际治理对话**提供可比数据基础 [5]。

### 5.2 多语言评测推动全球化包容性
- ELOQUENT 2025 覆盖英/德/乌/捷四语言，回应非英语低资源语言在 Agent 安全评测中被忽视的**社会公平**诉求 [8]。

### 5.3 欺骗检测关联国家安全与反欺诈
- SVC 2025 明确面向安全筛查、欺诈防范，直接关联**公共安全政策**与跨国执法合作需求 [10]。

---

## 6. 资本与生态

- **本周期无显著变化**：现有证据源 [1-31] **未覆盖** 融资并购、人才流动、开源社区活跃度、商业公司格局变化等资本生态信息。  
  - > 待核实：Agent 评测/安全赛道融资轮次、独角兽估值、大厂收购初创安全公司案例、核心开源仓库（如 LeRobot, Open X-Embodiment, AgentBench 相关）贡献者增长趋势。  
  - **关注度**：低（基于现有证据）  
  - **推荐度**：★☆☆☆ —— 需引入 PitchBook, Crunchbase, GitHub Archive, 产业研报等数据源补全。

---

## 7. 信号与预测

| 信号来源 | 早期信号 | 推演依据 | 可证伪预测 (6-18个月) | 不确定性标注 |
| :--- | :--- | :--- | :--- | :--- |
| **FMTI 2025** [5] | 透明度分数连续两年下降，头部厂商拒披露训练数据 | 监管压力（EU AI Act, 美行政命令）与商业机密保护博弈 | **[P] 预测**：至 2027 年 Q2，至少 3 家头部厂商被迫披露训练数据来源摘要或面临合规罚款；FMTI 平均分企稳回升。 | **[不确定]**：地缘政治可能导致中美监管标准分叉，指数可比性下降。 |
| **ELOQUENT 2025** [8] | 三角色评测范式被顶会/共享任务采纳 | 静态基准饱和，动态交互评测为必然趋势 | **[P] 预测**：至 2026 年底，NeurIPS/ICLR/ICRA 主流 Agent 评测基准中，采用“教师-学生-评估者”或类似多智能体交互范式的占比超 30%。 | **[不确定]**：复现成本高、评估者偏差大可能阻碍大规模采纳。 |
| **SVC 2025** [10] | 首个多模态欺骗挑战赛启动 | 单模态防御易被多模态攻击绕过（如语音+视频 Deepfake） | **[P] 预测**：至 2027 年，多模态欺骗检测 AUC 在 SVC 测试集上超 0.90 的开源模型出现，并被集成至主流 RAG/Agent 安全网关。 | **[R] 传闻**：部分厂商内部已有未公开 SOTA，挑战赛榜单可能不反映真实前沿。 |
| **开源生态缺口** [28, 30, 31] | 机器人/VLA 专用安全评测框架缺失 | LeRobot/Open X-Embodiment 社区高速增长，安全为量产前置条件 | **[P] 预测**：至 2026 年 Q4，LeRobot 或 Isaac Lab 官方合并“安全评测套件”（含碰撞避让、指令注入防御、可纠正性基准），成为社区默认标准。 | **[不确定]**：实时控制环（C++/ROS2）与大模型推理（Python）的工程融合难度被低估。 |

---

## 附录：核心资源证据地图

### A. 经典与奠基性工作

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
| :--- | :--- | :--- | :--- | :--- | :--- | :---: | :--- | :--- |
| Modeling AGI Safety Frameworks with Causal Influence Diagrams | 2019 | Everitt et al. | > 待核实 | arXiv (cs.AI) | 低 | ★★☆☆☆ | [31] | 奠基性理论工作，用因果影响图对比 AGI 安全框架，非工程工具链 [31] |
| Pilot: Winner of the Human-Agent Negotiation Challenge at IJCAI 2020 | 2020 | Baarslag et al. | > 待核实 | IJCAI 2020 Challenge Winner | 中 | ★★★☆☆ | [18] | 早期人机博弈/谈判 Agent 评测基准，具备交互性 [18] |
| Transfer Learning Toolkit: Primers and Benchmarks | 2019 | NVIDIA et al. | > 待核实 | arXiv (cs.LG) | 低 | ★★☆☆☆ | [28] | 通用迁移学习基准封装，非机器人/VLA 专用 [28] |

### B. 开源项目与工程实践

| 名称 | 年份 | 维护机构 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
| :--- | :--- | :--- | :--- | :--- | :--- | :---: | :--- | :--- |
| Transfer Learning Toolkit | 2019 | NVIDIA | > 待核实 | arXiv (cs.LG) | 低 | ★☆☆☆☆ | [28] | 封装 17 个迁移学习模型，Python 包，无 C++/ROS2/实时控制要素 [28] |
| GR-NLP-TOOLKIT | 2024 | Univ. of Athens | > 待核实 | arXiv (cs.CL) | 低 | ★☆☆☆☆ | [30] | 现代希腊语 NLP 工具包，基于 Transformer，领域完全不匹配 [30] |
| Causal Influence Diagrams for AGI Safety | 2019 | DeepMind/FHI | > 待核实 | arXiv (cs.AI) | 低 | ★★☆☆☆ | [31] | 理论建模代码（如有），非运行时安全工具链 [31] |

> **关键缺口提示**：上述项目均**非**具身智能/VLA/机器人领域主流开源框架。真实生态核心项目（Open X-Embodiment, LeRobot, Isaac Lab, ROS2 Control, MoveIt, Nav2, AgentBench, RLAIF 安全对齐库等）**未在证据源中出现** > 待核实。

### C. 核心数据集与基准

| 名称 | 年份 | 机构/发布方 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
| :--- | :--- | :--- | :--- | :--- | :--- | :---: | :--- | :--- |
| **2025 Foundation Model Transparency Index (FMTI v3)** | 2025 | Stanford HAI et al. | 高 | arXiv (cs.AI) | 高 | ★★★★★ | [5] | 权威纵向基准，评估 20+ 头部模型透明度，平均分 40/100 [5] |
| **ELOQUENT 2025 Sensemaking Task** | 2025 | ELOQUENT Lab | 中 | arXiv (cs.CL) / Shared Task | 中 | ★★★★☆ | [8] | 首创教师-学生-评估者三角色范式，7源4语言 [8] |
| **SVC 2025: Multimodal Deception Detection Challenge** | 2025 | SVC Organizers | 中 | arXiv (cs.CV) / Challenge | 中 | ★★★★☆ | [10] | 首个多模态欺骗检测基准，面向安全筛查真实场景 [10] |
| **LongEval at CLEF 2025** | 2025 | CLEF | > 待核实 | CLEF 2025 Lab | 中 | ★★★☆☆ | [9] | 纵向评测 IR 模型性能随时间漂移 [9] |
| **ALTA 2024 Shared Task: Detect AI-Generated Sentences** | 2024 | ALTA | > 待核实 | ALTA 2024 Shared Task | 中 | ★★★☆☆ | [26] | 针对人机混合文本的句级 AI 生成检测 [26] |
| **CheckThat! 2024: Adversarial Text Generation** | 2024 | CheckThat! Lab | > 待核实 | CLEF 2024 Lab | 中 | ★★★☆☆ | [7] | 组合攻击方法生成对抗文本，评测事实核查鲁棒性 [7] |
| **Detecting Strategic Deception Using Linear Probes** | 2025 | Authors | > 待核实 | arXiv (cs.CL) | 中 | ★★★★☆ | [11] | 方法类基准，探测模型内部状态识别策略性欺骗 [11] |

---

## 参考来源

[1] NTU-NPU System for Voice Privacy 2024 Challenge — http://arxiv.org/abs/2410.02371v1  
[2] VQualA 2025 Challenge on Engagement Prediction for Short Videos — http://arxiv.org/abs/2509.02969v1  
[3] Discovery Opportunities with Gravitational Waves -- TASI 2024 Lecture Notes — http://arxiv.org/abs/2409.08956v1  
[4] Atmospheric entry and fragmentation of small asteroid 2024 BX1 — http://arxiv.org/abs/2403.00634v2  
[5] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1  
[6] ICAGC 2024: Inspirational and Convincing Audio Generation Challenge 2024 — http://arxiv.org/abs/2407.12038v2  
[7] OpenFact at CheckThat! 2024: Combining Multiple Attack Methods for Effective Adversarial Text Generation — http://arxiv.org/abs/2409.02649v2  
[8] Overview of the Sensemaking Task at the ELOQUENT 2025 Lab — http://arxiv.org/abs/2507.12143v1  
[9] LongEval at CLEF 2025: Longitudinal Evaluation of IR Model Performance — http://arxiv.org/abs/2503.08541v1  
[10] SVC 2025: the First Multimodal Deception Detection Challenge — http://arxiv.org/abs/2508.04129v1  
[11] Detecting Strategic Deception Using Linear Probes — http://arxiv.org/abs/2502.03407v1  
[12] Preprint site arXiv is banning computer-science reviews — https://doi.org/10.1038/d41586-025-03664-7  
[13] Extended Multilingual Protest News Detection -- Shared Task 1, CASE 2021 and 2022 — http://arxiv.org/abs/2211.11360v1  
[14] CHC-COMP 2022: Competition Report — http://arxiv.org/abs/2211.12231v1  
[15] MIPT-NSU-UTMN at SemEval-2021 Task 5 — http://arxiv.org/abs/2104.04739v1  
[16] Snowmass 2021 Community Survey Report — http://arxiv.org/abs/2203.07328v2  
[17] Evaluating LLM-based Agents for Multi-Turn Conversations: A Survey — http://arxiv.org/abs/2503.22458v3  
[18] Pilot: Winner of the Human-Agent Negotiation Challenge at IJCAI 2020 — http://arxiv.org/abs/2009.06781v2  
[19] WVOQ at SemEval-2021 Task 6 — http://arxiv.org/abs/2107.05467v1  
[20] TRANSMEDCON 2022: E-Poster Abstracts — https://doi.org/10.4103/0973-6247.377170  
[21] Motif Mining and Unsupervised Representation Learning for BirdCLEF 2022 — http://arxiv.org/abs/2206.04805v1  
[22] 2022 Association for Vascular Access Scientific Meeting — https://doi.org/10.2309/jvad-28-03-49  
[23] CPNP 2022 Annual Meeting Poster Abstracts — https://doi.org/10.9740/mhc.2022.04.089  
[24] PHA 2022 International Pulmonary Hypertension Conference Abstracts — https://doi.org/10.21693/1933-088x-22.1.4  
[25] Double Multi-Head Attention Multimodal System for Odyssey 2024 — http://arxiv.org/abs/2406.10598v1  
[26] Overview of the 2024 ALTA Shared Task — http://arxiv.org/abs/2412.17848v1  
[27] NTIRE 2024 Challenge on Image Super-Resolution (x4) — http://arxiv.org/abs/2404.09790v2  
[28] Transfer Learning Toolkit: Primers and Benchmarks — http://arxiv.org/abs/1911.08967v1  
[29] Laser pointer prohibition: improving safety or driving misclassification — http://arxiv.org/abs/1406.4924v1  
[30] GR-NLP-TOOLKIT: An Open-Source NLP Toolkit for Modern Greek — http://arxiv.org/abs/2412.08520v1  
[31] Modeling AGI Safety Frameworks with Causal Influence Diagrams — http://arxiv.org/abs/1906.08663v1

---

*Generated by research-bot · topic=`agent-评测与安全能力基准欺骗与可纠正性` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`nvidia/nemotron-3-ultra-550b-a55b` · sources=31 · duration=249s · 2026-11-05T02:44:23+00:00*
