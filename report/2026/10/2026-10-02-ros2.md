# ROS 2 生态与机器人中间件深度调研报告

> **日期**：2026-10-02（UTC）　|　**领域**：具身智能 / 机器人操作系统与中间件（ROS 2、DDS/RMW、ros2_control、Nav2/MoveIt2、VLA 集成）　|　**检索源数量**：候选来源 114 条（编号 [1]–[114]），经主题相关性筛查后，与 ROS 2 生态直接相关者约 25 条，其余为检索漂移噪声（详见各节"证据缺口"说明）。
>
> **本次调研的诚实声明**：本报告所依据的结构化发现中，子问题 q1（ROS 2 发行版演进）、q4 前半（Nav2/MoveIt2 架构演进）、q5（仿真/分布式部署工具链）的候选证据与主题几乎零交集。因此本报告**不对** ROS 2 发行版发布日期、EOL 时间、Tier 平台层级等事实性内容作任何陈述，一律标注 `> 待核实`，并给出官方核实入口。所有可核查结论集中在 DDS/QoS 行为学、实时执行器、sim-to-real 与单篇 VLA 竞赛方案上。

---

## 摘要（Executive Summary）

1. **本次检索的召回质量严重偏斜，构成本报告最重要的元结论。** 子问题 q1 的 6 条候选全部为计算机视觉挑战赛、NLP 健康检测、AI 治理与天体物理论文 [35][36][37][38][39][62]；q5 的候选同样混入短视频参与度预测 [35]、基础模型透明度指数 [37] 等噪声。**唯一勉强沾边 cs.RO 的是 HRI 信任主题 workshop [36]**。据此可以判断：任何关于"ROS 2 发行版节奏"的细节叙述在本证据集下都不可回答 `> 待核实`。

2. **中间件行为学是本次唯一成建制的证据链。** 三条互补的一手预印本构成核心：[1] 把 DDS 20+ 条 QoS 策略的运行语义形式化为**依赖链**并给出 41 条依赖违规规则；[2] 揭示 ROS 2 在 `RELIABLE` 主题上的**跨订阅者背压放大**效应，并给出基于代理的关键路径隔离方案；[15] 对 DDS 心跳/重传机制下的**概率性延迟**建模。三者共同指向一个结论：**ROS 2 通信的性能瓶颈不在 UDP 带宽，而在 QoS 组合语义与可靠性机制的耦合**。

3. **Zenoh 作为 DDS 替代路径，目前缺乏 ROS 2 RMW 层面的可核查对比证据。** 唯一直接命中"Zenoh vs DDS"的是跨中间件横向性能研究 [10]（Zenoh / MQTT / Kafka / DDS），其口径为通用中间件吞吐与延迟，**不涉及 rmw_zenoh 或 ROS 2 消息语义**；广域网方案 [22] 与容器化多主机代理 [45] 则提供了互补的分布式部署思路。

4. **实时性方面存在一篇高价值综述**：[34] 自述系统梳理了 ROS 2 近六年的实时支持与分析进展，可作为本主题的入门骨架。执行器侧的具体工程证据包括 micro-ROS 的预算式实时执行器 [33]、FPGA 加速的 ReconROS 事件驱动执行器 [52]，以及中间件透明的回调约束工作 [50]。此外，[56] 给出 ARM DynamIQ 平台的实时性实测，[53] 讨论实时 I/O 控制的软硬件协同设计。

5. **控制与导航栈的一手证据极为稀薄。** ros2_control 侧仅有一篇工程论文 [24]（把参考值的获取/校验/插值与跟踪控制律解耦，引入独立的 Reference Generator 组件）；MoveIt 侧仅有较早期的 Robowflex 抽象层 [93]；Nav2 的官方架构演进（行为树导航、MTC、Servo、混合规划器）**在候选集中完全没有一手来源** `> 待核实`。行为树方向有若干邻近论文 [94][96][98][99]，但其机器人域分别为水下、化学实验、多机器人协作与部分已知环境 TAMP。

6. **VLA 与 ROS 2 的集成是本调研最大的证据空白，但存在两个切入点。** [88]（ECMR 2025，正式会议论文）讨论**基础模型驱动的行为树动作选择用于导航**，是候选集中唯一同时触及"基础模型 + 导航决策"的同行评审来源；[82][87]（2025 BEHAVIOR Challenge 第一名方案）代表 VLA 策略架构的最新走向（Pi0.5 + flow matching 相关噪声），但其验证完全在照片级真实感仿真中完成，**无任何 ROS 2 节点封装、动作接口或推理部署描述**。

---

## 一、关键前沿进展与发行版节奏

### 1.1 证据缺口（本节结论的直接来源）

子问题 q1 的候选块共 6 条，主题分别为：短视频参与度预测挑战赛 [35]、人机交互信任 workshop [36]、图像超分挑战赛 [39]、抑郁检测 eRisk@CLEF [38]、基础模型透明度指数 [37]、强引力透镜宇宙学 [62]。**无一条涉及 ROS、ROS 2、中间件、发行版或构建系统。**

- 学科分布：cs.CV 3 条 [35][39]、cs.CL 1 条 [38]、cs.AI 1 条 [37]、cs.RO 1 条 [36]、astro-ph.CO 1 条 [62]。
- 发表时间集中于 2025 年 4 月至 12 月。
- **无一来自 Open Robotics / ROS 官方文档 / ROS Discourse / GitHub ros2 组织。**

> **证据四轴**（针对"q1 不可回答"这一元结论）：热度 `> 待核实`（候选块未提供任何引用数/star/下载/榜单信号）｜权威：候选来源多为 arXiv 预印本，含 1 条 workshop 论文集 [36]，**无一条为 ROS 生态一手来源**｜关注度：低（ROS 2 主题零交集，无社区信号）[35][36][37][38][39][62]｜推荐度：★☆☆☆☆（本结论仅为证据缺口说明，不含领域知识增量）。

### 1.2 本节不做的事实性陈述

以下内容在本证据集下**全部标注 `> 待核实`**，核实入口为用户提供的领域种子资源：

- Humble / Iron / Jazzy / Kilted 各发行版的发布日期、支持周期（EOL）与 REP-2000 平台 Tier 层级归属 `> 待核实`
- colcon / rosdep / ament_cmake / bloom 在各发行版间的具体变更 `> 待核实`
- ROS 2 技术指导委员会（TSC）治理结构、REP 流程、packages.ros.org 与 ROS Index 的迁移状态 `> 待核实`
- 与 ROS 1 及早期 ROS 2（Ardent–Dashing）奠基性设计原则（DDS 中间件抽象、节点生命周期、QoS、SROS2）的对照 `> 待核实`

**核实入口（种子资源，非编号引用）**：ROS 2 官方设计文档 <https://design.ros2.org/>；ROS 2 主仓库 <https://github.com/ros2/ros2>。

### 1.3 可间接引用的演进信号

唯一可作为"ROS 2 演进趋势"间接证据的是综述 [34]：其摘要自述 ROS 2 在过去六年中持续吸引实时系统社区与工业界的关注，成为具备模块化、分布式执行与通信能力的机器人中间件框架。

> **证据四轴**：[34] 热度 `> 待核实`（候选块未提供引用数/star）｜权威：arXiv 预印本（cs.RO），**非同行评审**｜关注度：低（无热度信号可核实）[34]｜推荐度：★★★★☆（若要撰写"ROS 2 实时性演进"，这是候选集中最合适的综述起点）[34]。

---

## 二、中间件与实时性（DDS / RMW / Executor）

这是本次调研证据密度最高的一节。

### 2.1 DDS QoS 的形式化与静态验证（最新进展）

[1] 的核心贡献：DDS 提供 **20 条以上 QoS 策略**，覆盖可用性、可靠性与资源占用；但 ROS 2 用户**缺乏安全策略组合的清晰指导与部署前验证流程**，常导致试错调参与意外运行时失败。该工作按 **Discovery / Data Exchange / Disassociation** 三阶段生命期解释 16 条 QoS 策略的运行方式，形式化一条 QoS 依赖链，并分类出 **41 条依赖违规规则**。

> **证据四轴**：热度 `> 待核实`（候选块未提供引用数/star/下载/榜单）｜权威：arXiv 预印本（cs.NI，arXiv:2509.03381v1，2025-09-03

## 参考来源

[1] Dependency Chain Analysis of ROS 2 DDS QoS Policies: From Lifecycle Tutorial to Static Verification — http://arxiv.org/abs/2509.03381v1
[2] Adaptive Bridge: A Proxy-Based Decoupling Layer for Mitigating DDS Backpressure in ROS 2 — http://arxiv.org/abs/2608.15380v2
[3] DDS: DPU-optimized Disaggregated Storage [Extended Report] — http://arxiv.org/abs/2407.13618v5
[4] Exploring the Effects of Multicast Communication on DDS Performance — http://arxiv.org/abs/2209.09001v1
[5] Performance Evaluation of ROS2-DDS middleware implementations facilitating Cooperative Driving in Autonomous Vehicle — http://arxiv.org/abs/2412.07485v1
[6] Two-dimensional magnetic interactions in LaFeAsO — http://arxiv.org/abs/1303.4033v1
[7] Credential Masquerading and OpenSSL Spy: Exploring ROS 2 using DDS security — http://arxiv.org/abs/1904.09179v2
[8] A Survey on Experimental Performance Evaluation of Data Distribution Service (DDS) Implementations — http://arxiv.org/abs/2310.16630v1
[9] DDS: A new device-degraded speech dataset for speech enhancement — http://arxiv.org/abs/2109.07931v4
[10] A Performance Study on the Throughput and Latency of Zenoh, MQTT, Kafka, and DDS — http://arxiv.org/abs/2303.09419v1
[11] Scaling Laws of the Throughput Capacity and Latency in Information-Centric Networks — http://arxiv.org/abs/1210.1185v3
[12] ALOHA 2: An Enhanced Low-Cost Hardware for Bimanual Teleoperation — http://arxiv.org/abs/2405.02292v1
[13] Observation of Atmospheric Neutrino Oscillations in Soudan 2 — http://arxiv.org/abs/hep-ex/0307069v1
[14] On the throughput of the common target area for robotic swarm strategies -- extended version — http://arxiv.org/abs/2201.09335v3
[15] Probabilistic Latency Analysis of the Data Distribution Service in ROS 2 — http://arxiv.org/abs/2508.10413v1
[16] ACM COMPUTE 2025 Best Practices Track Proceedings — http://arxiv.org/abs/2512.02349v2
[17] Nine Best Practices for Research Software Registries and Repositories: A Concise Guide — http://arxiv.org/abs/2012.13117v1
[18] Adaptive Sequential Test Planning for Multi-Mechanism Reliability Qualification via Bayesian Monte Carlo Tree Search — http://arxiv.org/abs/2608.09622v1
[19] Best Practices in the Creation and Use of Emotion Lexicons — http://arxiv.org/abs/2210.07206v2
[20] Explainable Machine Learning for Public Policy: Use Cases, Gaps, and Research Directions — http://arxiv.org/abs/2010.14374v3
[21] Taming Silent Failures: A Framework for Verifiable AI Reliability — http://arxiv.org/abs/2510.22224v1
[22] ROS2 Connect: A new ROS2 over WAN Solution — http://arxiv.org/abs/2608.25102v1
[23] Latency Analysis of ROS2 Multi-Node Systems — http://arxiv.org/abs/2101.02074v3
[24] Simplifying ROS2 controllers with a modular architecture for robot-agnostic reference generation — http://arxiv.org/abs/2601.08514v3
[25] Sim-to-Real Transfer for Mobile Robots with Reinforcement Learning: from NVIDIA Isaac Sim to Gazebo and Real ROS 2 Robots — http://arxiv.org/abs/2501.02902v1
[26] Sim-to-Real gap in RL: Use Case with TIAGo and Isaac Sim/Gym — http://arxiv.org/abs/2403.07091v2
[27] Sim-to-Real Transfer in Deep Reinforcement Learning for Bipedal Locomotion — http://arxiv.org/abs/2511.06465v1
[28] Reconciling Reality through Simulation: A Real-to-Sim-to-Real Approach for Robust Manipulation — http://arxiv.org/abs/2403.03949v3
[29] Sim-to-Real Transfer for Optical Tactile Sensing — http://arxiv.org/abs/2004.00136v1
[30] Skill Transfer and Discovery for Sim-to-Real Learning: A Representation-Based Viewpoint — http://arxiv.org/abs/2404.05051v1
[31] Isaac Sim-to-Real: Reinforcement Learning based Locomotion for Quadrupeds — http://arxiv.org/abs/2607.18135v1
[32] The Synthesis of Optimal Control Laws Using Isaacs' Method for the Solution of Differential Games — http://arxiv.org/abs/2112.10849v2
[33] Budget-based real-time Executor for Micro-ROS — http://arxiv.org/abs/2105.05590v2
[34] A Survey of Real-Time Support, Analysis, and Advancements in ROS 2 — http://arxiv.org/abs/2601.10722v2
[35] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1
[36] TRUST 2025: SCRITA and RTSS @ RO-MAN 2025 — http://arxiv.org/abs/2509.11402v1
[37] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1
[38] SINAI at eRisk@CLEF 2025: Transformer-Based and Conversational Strategies for Depression Detection — http://arxiv.org/abs/2509.19861v1
[39] NTIRE 2025 Challenge on Image Super-Resolution (x4): Methods and Results — http://arxiv.org/abs/2504.14582v3
[40] Microcontroller Based Testing of Digital IP-Core — http://arxiv.org/abs/1205.1866v1
[41] CLIPSwarm: Converting text into formations of robots — http://arxiv.org/abs/2311.11047v1
[42] State-of-the-art in Robot Learning for Multi-Robot Collaboration: A Comprehensive Survey — http://arxiv.org/abs/2408.11822v1
[43] Policies over Poses: Reinforcement Learning based Distributed Pose-Graph Optimization for Multi-Robot SLAM — http://arxiv.org/abs/2510.22740v1
[44] Experimental Validation of Stable Coordination for Multi-Robot Systems with Limited Fields of View using a PortableMulti-Robot Testbed — http://arxiv.org/abs/1909.07476v1
[45] Proxying ROS communications -- enabling containerized ROS deployments in distributed multi-host environments — http://arxiv.org/abs/2201.01613v2
[46] Influence of Team Interactions on Multi-Robot Cooperation: A Relational Network Perspective — http://arxiv.org/abs/2310.12910v1
[47] Real-Time Service Subscription and Adaptive Offloading Control in Vehicular Edge Computing — http://arxiv.org/abs/2512.14002v1
[48] Real time state monitoring and fault diagnosis system for motor based on LabVIEW — http://arxiv.org/abs/1806.09998v1
[49] Real-Time-Data Analytics in Raw Materials Handling — http://arxiv.org/abs/1802.00625v1
[50] Work in Progress: Middleware-Transparent Callback Enforcement in Commoditized Component-Oriented Real-time Systems — http://arxiv.org/abs/2505.06546v1
[51] Tevatron-for-LHC Report of the QCD Working Group — http://arxiv.org/abs/hep-ph/0610012v1
[52] ReconROS Executor: Event-Driven Programming of FPGA-accelerated ROS 2 Applications — http://arxiv.org/abs/2201.07454v1
[53] Hardware/Algorithm Co-design for Real-Time I/O Control with Improved Timing Accuracy and Robustness — http://arxiv.org/abs/2409.14779v1
[54] Toward Real-Time Image Annotation Using Marginalized Coupled Dictionary Learning — http://arxiv.org/abs/2304.06907v2
[55] SnapperGPS: Open Hardware for Energy-Efficient, Low-Cost Wildlife Location Tracking with Snapshot GNSS — http://arxiv.org/abs/2207.06310v3
[56] Arm DynamIQ Shared Unit and Real-Time: An Empirical Evaluation — http://arxiv.org/abs/2503.17038v3
[57] Scalable FPGA Framework for Real-Time Denoising in High-Throughput Imaging: A DRAM-Optimized Pipeline using High-Level Synthesis — http://arxiv.org/abs/2508.14917v2
[58] Tiered-Latency DRAM (TL-DRAM) — http://arxiv.org/abs/1601.06903v1
[59] Roman Observations Time Allocation Committee: Final Report and Recommendations — http://arxiv.org/abs/2505.10574v2
[60] Memory at Your Service: Fast Memory Allocation for Latency-critical Services — http://arxiv.org/abs/2109.02922v1
[61] M$^3$Eval: Multi-Modal Memory Evaluation through Cognitively-Grounded Video Tasks — http://arxiv.org/abs/2606.05008v1
[62] TDCOSMO 2025: Cosmological constraints from strong lensing time delays — http://arxiv.org/abs/2506.03023v4
[63] Fluid Antenna System: New Insights on Outage Probability and Diversity Gain — http://arxiv.org/abs/2301.00073v2
[64] AI Wizards at CheckThat! 2025: Enhancing Transformer-Based Embeddings with Sentiment for Subjectivity Detection in News Articles — http://arxiv.org/abs/2507.11764v1
[65] UIC-AIHealth4All at ArchEHR-QA 2026: Answer-First Evidence Grounding for Clinical Question Answering — http://arxiv.org/abs/2608.27467v1
[66] ZeroR@CHiPSAL 2026: Two-Stage Vision-Language Adaptation with Contrastive Learning for Nepali Meme Classification — http://arxiv.org/abs/2607.28637v1
[67] AutoRestTest at the SBFT 2026 Tool Competition — http://arxiv.org/abs/2607.01063v1
[68] Second MOASEI Competition at AAMAS'2026: A Technical Report — http://arxiv.org/abs/2607.03399v1
[69] NTIRE 2026 Rip Current Detection and Segmentation (RipDetSeg) Challenge Report — http://arxiv.org/abs/2604.17070v2
[70] Overview of BioASQ 2026: The fourteenth BioASQ Challenge on Large-Scale Biomedical Semantic Indexing and Question Answering — http://arxiv.org/abs/2609.39975v1
[71] VoxENES 2026: Benchmarking Generalization of Speech Spoofing Detectors Against LLM-Era TTS and Voice Conversion — http://arxiv.org/abs/2607.11706v1
[72] The 2026 Skyrmionics Roadmap — http://arxiv.org/abs/2601.16575v1
[73] Robot Operating System 2: Design, Architecture, and Uses In The Wild — http://arxiv.org/abs/2211.07752v1
[74] Robot Design: Formalisms, Representations, and the Role of the Designer — http://arxiv.org/abs/1806.05157v1
[75] Automatic Design of Task-specific Robotic Arms — http://arxiv.org/abs/1806.07419v1
[76] A rich bounty of AGN in the 9 square degree Bootes survey: high-z obscured AGN and large-scale structure — http://arxiv.org/abs/astro-ph/0611654v1
[77] AIn't Nothing But a Survey? Using Large Language Models for Coding German Open-Ended Survey Responses on Survey Motivation — http://arxiv.org/abs/2506.14634v3
[78] The Methanol Multibeam Survey — http://arxiv.org/abs/1210.0979v1
[79] Towards Assessing Spread in Sets of Software Architecture Designs — http://arxiv.org/abs/2402.19171v1
[80] High-level robot programming based on CAD: dealing with unpredictable environments — http://arxiv.org/abs/1309.2086v1
[81] VLSP 2025 MLQA-TSR Challenge: Vietnamese Multimodal Legal Question Answering on Traffic Sign Regulation — http://arxiv.org/abs/2510.20381v1
[82] Task adaptation of Vision-Language-Action model: 1st Place Solution for the 2025 BEHAVIOR Challenge — http://arxiv.org/abs/2512.06951v2
[83] The AudioMOS Challenge 2025 — http://arxiv.org/abs/2509.01336v1
[84] A Simple Observer for Gyro and Accelerometer Biases in Land Navigation Systems — http://arxiv.org/abs/1501.06618v1
[85] High-Resolution Water Sampling via a Solar-Powered Autonomous Surface Vehicle — https://arxiv.org/abs/2512.09798
[86] LSQCA: Resource-Efficient Load/Store Architecture for Limited-Scale Fault-Tolerant Quantum Computing — http://arxiv.org/abs/2412.20486v2
[87] Task adaptation of Vision-Language-Action model: 1st Place Solution for the 2025 BEHAVIOR Challenge — https://arxiv.org/abs/2512.06951
[88] Foundation-Model-Based Action Selection for Behavior Trees in Navigation — https://doi.org/10.1109/ECMR65884.2025.11163061
[89] Socially intelligent task and motion planning for human-robot interaction — http://arxiv.org/abs/2001.08398v1
[90] GNSS-T Forest Transmissivity Simulations Based on LiDAR-Derived Tree Structure — https://doi.org/10.23919/USNC-URSINRSM66067.2025.10907203
[91] Annif at SemEval-2025 Task 5: Traditional XMTC augmented by LLMs — http://arxiv.org/abs/2504.19675v2
[92] Methods of swarm artificial intelligence in autonomous navigation tasks of UAVs — https://doi.org/10.20535/srit.2308-8893.2025.3.11
[93] Robowflex: Robot Motion Planning with MoveIt Made Easy — http://arxiv.org/abs/2103.12826v2
[94] Dynamic Mission Planning Framework for Collaborative Underwater Operations Using Behavior Trees — https://doi.org/10.3390/jmse13081458
[95] Culturally Grounded Physical Commonsense Reasoning in Italian and English: A Submission to the MRL 2025 Shared Task — http://arxiv.org/abs/2510.22631v1
[96] PREVENT: Proactive Risk Evaluation and Vigilant Execution of Tasks for Mobile Robotic Chemists using Multi-Modal Behavior Trees — https://arxiv.org/abs/2510.21438
[97] DeDisCo at the DISRPT 2025 Shared Task: A System for Discourse Relation Classification — http://arxiv.org/abs/2509.11498v4
[98] Bridging Probabilistic Inference and Behavior Trees: An Interactive Framework for Adaptive Multi-Robot Cooperation — https://arxiv.org/abs/2512.04404
[99] Technical Report: A Hierarchical Deliberative-Reactive System Architecture for Task and Motion Planning in Partially Known Environments — http://arxiv.org/abs/2202.01385v1
[100] NALA_MAINZ at BLP-2025 Task 2: A Multi-agent Approach for Bangla Instruction to Python Code Generation — http://arxiv.org/abs/2511.16787v1
[101] Tree-of-Debate: Multi-Persona Debate Trees Elicit Critical Thinking for Scientific Comparative Analysis — http://arxiv.org/abs/2502.14767v2
[102] Complexity of Networks (reprise) — http://arxiv.org/abs/0911.3482v5
[103] RISC-V Functional Safety for Autonomous Automotive Systems: An Analytical Framework and Research Roadmap for ML-Assisted Certification — http://arxiv.org/abs/2604.17391v1
[104] Discussion Paper: The Threat of Real Time Deepfakes — http://arxiv.org/abs/2306.02487v1
[105] Real-Time Hard Peak Age-of-Information Safety with No-Regret Learning — http://arxiv.org/abs/2607.27626v2
[106] Distributed Model Predictive Safety Certification for Learning-based Control — http://arxiv.org/abs/1911.01832v2
[107] Proposal to upgrade the MIPP Experiment — http://arxiv.org/abs/hep-ex/0609057v1
[108] Mestra: Exploring Migration on Virtualized CGRAs — http://arxiv.org/abs/2604.04694v1
[109] Sawtooth control using electron cyclotron current drive in the presence of energetic particles in high performance ASDEX Upgrade plasmas — http://arxiv.org/abs/1306.6776v1
[110] MAST Upgrade - Construction Status — http://arxiv.org/abs/1503.06677v1
[111] Sensitivity of Microwave Interferometer in the Limiter Shadow to filaments in ASDEX Upgrade — http://arxiv.org/abs/2110.01314v1
[112] Electron runaway in ASDEX Upgrade experiments of varying core temperature — http://arxiv.org/abs/2101.04471v3
[113] Complex structure of turbulence across the ASDEX Upgrade pedestal — http://arxiv.org/abs/2303.10596v1
[114] Overview of the Sensemaking Task at the ELOQUENT 2025 Lab: LLMs as Teachers, Students and Evaluators — http://arxiv.org/abs/2507.12143v1


---

*Generated by research-bot · topic=`ros2` · depth=`standard` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading · model=`deepseek-v4-flash` · sources=114 · duration=260s · 2026-10-02T23:18:23+00:00*
