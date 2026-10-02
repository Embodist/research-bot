# C++ 机器人工程与实时系统：数学/优化库生态、实时实践与互操作工具链调研报告

**日期**：2026-10-02（UTC）
**领域**：机器人 C++ 工程 / 实时系统 / 运动学与优化库 / 构建与互操作工具链
**检索源数量**：可引用候选来源 88 条（[1]–[88]）+ 领域种子资源 12 条（4 篇种子论文、8 个开源项目、0 个数据集）；本报告实际引用 38 条，其余因主题不匹配未引用。

> **证据可用性总声明（必读）**
> 1. 本轮全部候选块的 `heat` 字段为空，未提供任何引用数（citations）、GitHub star、下载量或榜单排名。因此本报告中所有"热度证据"栏一律为 `> 待核实`，**不做任何数字推断**。
> 2. 检索召回的**主题匹配率偏低**：子问题 q1 的 6 条 finding（[4][5][9][49][80][82]）与"C++ 机器人工程与实时系统"无实质交集；子问题 q4 的 5 条 finding 全部自述为"证据缺口"。这说明本主题的关键词召回（"real-time""C++""robot"）极易命中共用词而非共领域文献。
> 3. 因此，本报告对**库生态、构建系统、包管理**等无法从候选集中得到一手证据的部分，一律标注 `> 待核实`，仅提供真实可达的官方仓库/文档链接作为线索，不替代正式检索。

---

## 摘要（Executive Summary）

1. **本轮检索未获得 Eigen / Sophus / Ceres Solver / GTSAM / Pinocchio 的任何一手新版本文档、发布说明或性能数据**。这五个库仅能通过种子资源链接确认其官方入口存在，其"奠基性地位"在本报告中按领域共识陈述，但**具体版本号、API 变更、性能数字全部 `> 待核实`**。

2. **与"C++ 实时机器人"直接相关的近两年证据集中在三个方向**：
   - **ROS 2 图级实时调度与中间件性能**：[10]（单处理器上 ROS2 图的固定优先级与 EDF 调度）、[74]（ROS2 自动驾驶系统性能评估）、[78]（ROS2-DDS 中间件实现对比）；
   - **无锁/免协调并发与多核资源协议**：[3]（免协调并发无锁队列）、[8]（多核实时系统无锁容错资源共享协议 LEFT-RS）；
   - **ROS 2 真正零拷贝 IPC**：[72]（Agnocast，支持不定长消息类型）。

3. **C++/Python 互操作的一手证据仅一条**：为大型运动规划库 OMPL 生成 **nanobind** 绑定的"LLM 生成 + 专家在环"工作流，并系统记录 shared pointer / overload / trampoline 三类失败模式（[68]）。

4. **硬缺口**：**构建系统与包管理（CMake / Conan / vcpkg / Bazel / colcon）、静态分析（clang-tidy / cppcheck）、Sanitizer（ASan / UBSan / TSan）在本轮证据集中覆盖率为 0**。任何关于"最佳实践"的结论都必须先补检索官方文档与真实机器人仓库工件，否则即为无据推断。

5. **同名混淆是重大污染源**：[26][27] 的 "CERES" 是 CERN 的粒子物理实验（Dilepton measurements with CERES、CERES/NA45 径迹漂移室），[33] 的 "PINOCCHIO" 是天体物理暗物质晕分层构建模型，[23][24] 属核物理与 Belle 实验。若不做消歧，会直接污染 Ceres Solver 与 Pinocchio 库的引用链。

6. **检索噪声严重且性质异常**：[82]（LHC 物理 ML 年度综述）摘要自述"首句由人类撰写、其余由 agentic AI 系统生成"，这类条目不应作为任何机器人工程结论的依据；[9][29][32][37] 为短视频/图像质量/视觉觅食/越南语法律问答挑战赛，与本主题无交集。

---

## 一、关键前沿进展

### 1.1 关于检索覆盖的诚实说明

子问题 q1 的候选 finding（[9] VQualA 短视频参与度预测、[4] Xiaomi-Robotics-1 VLA 模型、[5] Action Flow Matching 持续学习、[49] TRUST 2025 HRI 工作坊、[80] MOASEI 多智能体竞赛、[82] LHC ML 综述）**全部与"C++ 库、C++20/23 落地、实时与部署范式"不匹配**。

- 热度：`> 待核实`（候选块无引用数/star/榜单）[9][4][5][49][80][82]
- 权威：[4][5][49] 为 arXiv 预印本（cs.RO），[80] 为 cs.MA 预印本，[82] 为 hep-ph 预印本且非人类主导撰写，均未经同行评审 [4][5][49][80][82]
- 关注度：低 — 无任何引用/star/榜单/社区讨论信号，且主题与"C++ 工程"不相关 [9][4][5][49][80][82]
- 推荐度：★☆☆☆☆ — 均不建议作为本主题证据使用，仅作为"召回偏离"的记录 [9][4][5][49][80][82]

> 由此，本节改以候选来源集中**真实相关**的条目重建前沿图景，并逐条标注证据强度。

### 1.2 实时 ROS 2 调度与中间件（最贴近主题的一线）

**（1）ROS 2 图在单处理器上的固定优先级与 EDF 调度分析** — [10]（arXiv:2512.16926v1，编号指示提交时间为 2025-12）

- 论断：存在针对 ROS 2 计算图（graph）在单处理器上进行 **Fixed-Priority（固定优先级）** 与 **EDF（最早截止期优先）** 调度分析的专门工作 [10]。
- 热度：`> 待核实`（候选块未提供引用数/star）[10]
- 权威：arXiv 预印本，未经同行评审；`> 待核实`（venue 与作者机构未在候选块中给出）[10]
- 关注度：低 — 无引用/star/榜单信号可依据 [10]
- 推荐度：★★★★☆ — 若要做 ROS 2 节点的可调度性分析（而非经验调参），这是本轮**最直接相关的单条来源**，建议精读全文 [10]

**（2）ROS 2 + DDS 中间件实现的性能评估** — [78]（arXiv:2412.07485v1，编号指示 2024-12）

- 论断：存在面向自动驾驶协同驾驶场景、对**多种 ROS2-DDS 中间件实现**做性能评估的研究 [78]。
- 热度：`> 待核实` [78]
- 权威：arXiv 预印本，未经同行评审（仅标题级证据，摘要未在候选块中给出）[78]
- 关注度：低 — 无引用/star/榜单信号 [78]
- 推荐度：★★★★☆ — DDS 实现选型（Fast DDS / Cyclone DDS 等）是 ROS 2 实时性的关键变量；但本报告**仅基于标题级证据**，具体对比维度与数字必须回原文核实 [78]

**（3）基于 ROS 2 的自动驾驶系统性能评估** — [74]（arXiv:2411.11607v3，编号指示 2024-11，已修订至 v3）

- 论断：存在对完整 ROS 2 自动驾驶系统做端到端性能评估的工作，且已迭代到 v3 [74]。
- 热度：`> 待核实` [74]
- 权威：arXiv 预印本，未经同行评审；v1→v3 修订说明作者持续维护，但不等于同行评审 [74]
- 关注度：低 — 无引用/star/榜单信号 [74]
- 推荐度：★★★☆☆ — 作为"ROS 2 性能工程在真实系统上的落地样本"有参考价值，但仅标题级证据，结论待核实 [74]

### 1.3 无锁并发与多核实时资源管理

**（4）免协调（coordination-free）并发无锁队列** — [3]（arXiv:2511.09410v1，编号指示 2025-11）

- 论断：论文指出队列是最简单的数据结构之一，但在并发正确性要求下，现有无锁实现因需引入防危险（hazard）协调机制而显著复杂化；该工作探索免协调的无锁队列实现 [3]。
- 热度：`> 待核实` [3]
- 权威：arXiv 预印本（cs.DC），未经同行评审

## 参考来源

[1] Real-Time Service Subscription and Adaptive Offloading Control in Vehicular Edge Computing — http://arxiv.org/abs/2512.14002v1
[2] Real time state monitoring and fault diagnosis system for motor based on LabVIEW — http://arxiv.org/abs/1806.09998v1
[3] No Cords Attached: Coordination-Free Concurrent Lock-Free Queues — http://arxiv.org/abs/2511.09410v1
[4] Xiaomi-Robotics-1: Scaling Vision-Language-Action Models with over 100K Hours of Real-World Trajectories — http://arxiv.org/abs/2607.15330v2
[5] Action Flow Matching for Continual Robot Learning — http://arxiv.org/abs/2504.18471v2
[6] Using Physiological Measures, Gaze, and Facial Expressions to Model Human Trust in a Robot Partner — http://arxiv.org/abs/2504.05291v1
[7] Scalable Aerial GNSS Localization for Marine Robots — http://arxiv.org/abs/2505.04095v2
[8] LEFT-RS: A Lock-Free Fault-Tolerant Resource Sharing Protocol for Multicore Real-Time Systems — http://arxiv.org/abs/2512.21701v1
[9] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1
[10] Fixed-Priority and EDF Schedules for ROS2 Graphs on Uniprocessor — http://arxiv.org/abs/2512.16926v1
[11] Real-Time-Data Analytics in Raw Materials Handling — http://arxiv.org/abs/1802.00625v1
[12] Flow Network Models for Online Scheduling Real-time Tasks on Multiprocessors — http://arxiv.org/abs/1810.08342v1
[13] NTIRE 2025 Challenge on Image Super-Resolution (x4): Methods and Results — http://arxiv.org/abs/2504.14582v3
[14] Energy-Efficient Real-Time Scheduling for Two-Type Heterogeneous Multiprocessors — http://arxiv.org/abs/1607.07763v1
[15] Deterministic Control of Stochastic Reaction-Diffusion Equations — http://arxiv.org/abs/1905.09074v5
[16] A Unified Robust Motion Controller Synthesis for Compliant Robots Driven by Series Elastic Actuators — http://arxiv.org/abs/2202.00168v1
[17] Can Decentralized Control Outperform Centralized? The Role of Communication Latency — http://arxiv.org/abs/2109.00359v5
[18] On Frequency Response Function Identification for Advanced Motion Control — http://arxiv.org/abs/2006.10373v1
[19] Design Constraints of Disturbance Observer-based Motion Control Systems are Stricter in the Discrete-Time Domain — http://arxiv.org/abs/2202.00165v1
[20] A Control-Oriented Notion of Finite State Approximation — http://arxiv.org/abs/1105.3788v3
[21] Predicting radial-velocity jitter induced by stellar oscillations based on Kepler data — http://arxiv.org/abs/1807.00096v1
[22] Control of a Rigid Wing Pumping Airborne Wind Energy System in all Operational Phases — http://arxiv.org/abs/2006.11141v1
[23] The $^{12}$C(n, 2n)$^{11}$C cross section from threshold to 26.5 MeV — http://arxiv.org/abs/1707.09375v2
[24] Observation of $Ξ_{c}(2930)^0$ and updated measurement of $B^{-} \to K^{-} Λ_{c}^{+} \barΛ_{c}^{-}$ at Belle — http://arxiv.org/abs/1712.03612v3
[25] Model-Based Capacitive Touch Sensing in Soft Robotics: Achieving Robust Tactile Interactions for Artistic Applications — http://arxiv.org/abs/2503.02280v1
[26] Dilepton measurements with CERES — http://arxiv.org/abs/0802.2679v1
[27] The CERES/NA45 Radial Drift Time Projection Chamber — http://arxiv.org/abs/0802.1443v2
[28] AMB3R-SLAM: Kilometer-scale SLAM with Hierarchical Backend — http://arxiv.org/abs/2609.19518v1
[29] VQualA 2025 Challenge on Visual Quality Comparison for Large Multimodal Models: Methods and Results — http://arxiv.org/abs/2509.09190v1
[30] Characterizing SLAM Benchmarks and Methods for the Robust Perception Age — http://arxiv.org/abs/1905.07808v1
[31] HS-SLAM: Hybrid Representation with Structural Supervision for Improved Dense SLAM — http://arxiv.org/abs/2503.21778v1
[32] Navigating Simply, Aligning Deeply: Winning Solutions for Mouse vs. AI 2025 — http://arxiv.org/abs/2602.00982v1
[33] PINOCCHIO and the hierarchical build-up of dark matter haloes — http://arxiv.org/abs/astro-ph/0109324v1
[34] Objective vs. Search: Decomposing What Makes a Good Tokeniser — http://arxiv.org/abs/2609.19145v1
[35] VS-Net: Voting with Segmentation for Visual Localization — http://arxiv.org/abs/2105.10886v1
[36] Area Coverage of Expanding E.T. Signals in the Galaxy: SETI and Drake's N — http://arxiv.org/abs/1802.09399v2
[37] VLSP 2025 MLQA-TSR Challenge: Vietnamese Multimodal Legal Question Answering on Traffic Sign Regulation — http://arxiv.org/abs/2510.20381v1
[38] Linear Mappings of Free Algebra — http://arxiv.org/abs/1003.1544v2
[39] Non-linear positive maps between $C^*$-algebras — http://arxiv.org/abs/1811.03128v1
[40] Grüss type inequalities for positive linear maps on $C^*$-algebras — http://arxiv.org/abs/1610.03868v1
[41] DQ Robotics: a Library for Robot Modeling and Control — http://arxiv.org/abs/1910.11612v3
[42] Technical Report for ICRA 2025 GOOSE 3D Semantic Segmentation Challenge: Adaptive Point Cloud Understanding for Heterogeneous Robotic Systems — http://arxiv.org/abs/2506.06995v1
[43] Influence of Operator Expertise on Robot Supervision and Intervention — http://arxiv.org/abs/2601.15069v2
[44] ACM COMPUTE 2025 Best Practices Track Proceedings — http://arxiv.org/abs/2512.02349v2
[45] Nine Best Practices for Research Software Registries and Repositories: A Concise Guide — http://arxiv.org/abs/2012.13117v1
[46] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1
[47] The AudioMOS Challenge 2025 — http://arxiv.org/abs/2509.01336v1
[48] TDCOSMO 2025: Cosmological constraints from strong lensing time delays — http://arxiv.org/abs/2506.03023v4
[49] TRUST 2025: SCRITA and RTSS @ RO-MAN 2025 — http://arxiv.org/abs/2509.11402v1
[50] Event-Enriched Image Analysis Grand Challenge at ACM Multimedia 2025 — http://arxiv.org/abs/2508.18904v1
[51] Robotic Template Library — http://arxiv.org/abs/2107.00324v1
[52] ROBUSfT: Robust Real-Time Shape-from-Template, a C++ Library — http://arxiv.org/abs/2301.04037v3
[53] Robotic Template Library — https://doi.org/10.5334/jors.353
[54] Bandicoot: A Templated C++ Library for GPU Linear Algebra — http://arxiv.org/abs/2508.11385v3
[55] EduRob: An Educational Robot for Teaching Kinematics of Wheeled Mobile Robots — https://doi.org/10.1007/978-3-031-67059-6_25
[56] The Geometry and Kinematics of the Matrix Lie Group $SE_K(3)$ — http://arxiv.org/abs/2012.00950v4
[57] Tevatron-for-LHC Report of the QCD Working Group — http://arxiv.org/abs/hep-ph/0610012v1
[58] On the Manifold: Representing Geometry in C++ for State Estimation — https://openalex.org/W2908988736
[59] Approximation properties of simple Lie groups made discrete — http://arxiv.org/abs/1408.5238v2
[60] On properties of principal elements of Frobenius Lie algebras — http://arxiv.org/abs/1212.5380v2
[61] The Strong Trotter Property for Locally $μ$-convex Lie Groups — http://arxiv.org/abs/1802.08923v2
[62] Diophantine properties of nilpotent Lie groups — http://arxiv.org/abs/1307.1489v2
[63] Secure and secret cooperation in robotic swarms — http://arxiv.org/abs/1904.09266v3
[64] Student's T Robust Bundle Adjustment Algorithm — http://arxiv.org/abs/1111.1400v1
[65] A Hessian for Gaussian Mixture Likelihoods in Nonlinear Least Squares — http://arxiv.org/abs/2404.05452v2
[66] A Molecular Implementation of the Least Mean Squares Estimator — http://arxiv.org/abs/1701.00602v1
[67] Fast Convergence for Weighted Least Squares Estimates — http://arxiv.org/abs/2605.00198v3
[68] Python Bindings for a Large C++ Robotics Library: The Case of OMPL — http://arxiv.org/abs/2603.04668v1
[69] LongEval at CLEF 2025: Longitudinal Evaluation of IR Model Performance — http://arxiv.org/abs/2503.08541v1
[70] SINAI at eRisk@CLEF 2025: Transformer-Based and Conversational Strategies for Depression Detection — http://arxiv.org/abs/2509.19861v1
[71] Performance of Genetic Algorithms in the Context of Software Model Refactoring — http://arxiv.org/abs/2308.13875v1
[72] ROS 2 Agnocast: Supporting Unsized Message Types for True Zero-Copy Publish/Subscribe IPC — http://arxiv.org/abs/2506.16882v1
[73] A Performance Study of GA and LSH in Multiprocessor Job Scheduling — http://arxiv.org/abs/1002.1149v1
[74] Performance evaluation of a ROS2 based Automated Driving System — http://arxiv.org/abs/2411.11607v3
[75] Performance Analysis of Software to Hardware Task Migration in Codesign — http://arxiv.org/abs/1002.1154v1
[76] A Metric for Performance Portability — http://arxiv.org/abs/1611.07409v1
[77] Enhanced Cluster Computing Performance Through Proportional Fairness — http://arxiv.org/abs/1404.2266v1
[78] Performance Evaluation of ROS2-DDS middleware implementations facilitating Cooperative Driving in Autonomous Vehicle — http://arxiv.org/abs/2412.07485v1
[79] UIC-AIHealth4All at ArchEHR-QA 2026: Answer-First Evidence Grounding for Clinical Question Answering — http://arxiv.org/abs/2608.27467v1
[80] Second MOASEI Competition at AAMAS'2026: A Technical Report — http://arxiv.org/abs/2607.03399v1
[81] AutoRestTest at the SBFT 2026 Tool Competition — http://arxiv.org/abs/2607.01063v1
[82] Machine learning for the LHC physics program: a 2025-2026 stocktake — http://arxiv.org/abs/2609.32874v1
[83] LLM-based ambiguity detection in natural language instructions for collaborative surgical robots — http://arxiv.org/abs/2507.11525v1
[84] Correction: Distributed multi-robot active gathering for non-uniform agriculture and forestry information — https://doi.org/10.3389/fpls.2025.1730134
[85] First D-FUMT₈ Silicon with SELF⟲ Logic Primitive: Native 8-Valued Hardware Realization with Lean 4 Refinement Proof, Four-Substrate Cross-Verification (Two FPGA Silicon Families + Aer Simulator + IBM Heron r2 Real Hardware) — https://doi.org/10.5281/zenodo.20192813
[86] First D-FUMT₈ Silicon with SELF⟲ Logic Primitive: Native 8-Valued Hardware Realization with Lean 4 Refinement Proof, Four-Substrate Cross-Verification (Two FPGA Silicon Families + Aer Simulator + IBM Heron r2 Real Hardware) — https://doi.org/10.5281/zenodo.20101174
[87] Autonomous Planning In-space Assembly Reinforcement-learning free-flYer (APIARY) International Space Station Astrobee Testing — http://arxiv.org/abs/2512.03729v1
[88] Artificial Intelligence and Civil Justice: U.S. Practice, Policy, and Principles — https://doi.org/10.1093/ajcl/avag028


---

*Generated by research-bot · topic=`cpp-robotics` · depth=`standard` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading · model=`deepseek-v4-flash` · sources=88 · duration=287s · 2026-10-02T22:12:30+00:00*
