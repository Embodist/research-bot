# C++ 机器人工程与实时系统：证据化调研报告

> **日期**：2026-10-04（UTC）
> **研究领域**：机器人 C++ 软件生态 / 实时系统 / 数值与优化库 / 构建与包管理 / 学习型策略部署
> **检索源规模**：106 条可引用候选编号（[1]–[106]）+ 12 项人工维护种子资源（无检索编号，链接单独标注）
> **证据分级约定**：**A** = 同行评审论文 / 官方标准与文档；**B** = arXiv 预印本 / 官方代码仓库 / 官方数据集主页；**C** = 第三方复现 / 榜单；**D** = 社区帖子；**E** = 不可用
> **引用纪律**：本报告只引用上述编号中真实存在的条目，不使用编号外的论文/项目/数字。种子资源因无编号，一律标注为「种子资源，无检索编号」，其热度/引用数不得据本报告断言。
> **重大提示**：本次候选证据在 **C++ 语言标准、ROS2 执行器/DDS 实时化、CMake/Conan/vcpkg 构建与包管理、数值库横向基准、实时内存与模板代价争议** 五个子问题上存在 **系统性证据真空**。下文凡无一手证据处均以 `> 待核实` 显式标注，**不得将其读作「该方向无进展」**。

---

## 摘要（Executive Summary）

**结论 1｜本次调研的首要产出是一个负面但重要的元发现：候选证据在核心子问题上系统性缺失。**
q1（C++ 语言标准与实时执行框架）、q3（构建与包管理）、q4（库横向基准）、q5（实时内存/对齐/模板代价争议）四个子问题的候选块中，**没有任何一条**直接涉及 ISO C++ 标准编号、rclcpp 执行器、DDS/零拷贝、Conan/vcpkg、CMake 现代实践、clang-tidy、交叉编译或数值库对比基准 [2][25][48][80][82][87]。该缺口横跨多个子问题，属于**检索词构造失败**而非领域沉寂（依据：同一批检索中出现了大量与机器人无关的跨领域命中）。

**结论 2｜但在候选池的完整编号表（[1]–[106]）中，确实存在若干高相关的可核查一手证据，构成报告的实体骨架：**

| 主题 | 关键证据 | 证据等级 | 一句话价值 |
|---|---|---|---|
| ROS2 实时执行器 | [86] ring-buffer ROS2 executor（IEEE SCC 2023，DOI 10.1109/SCC57168.2023.00021） | **A** | 面向航天实时场景对 ROS2 执行器做结构性改造的一手工程论文 |
| ROS2 多节点延迟 | [84

## 参考来源

[1] DQ Robotics: a Library for Robot Modeling and Control — http://arxiv.org/abs/1910.11612v3
[2] Xiaomi-Robotics-1: Scaling Vision-Language-Action Models with over 100K Hours of Real-World Trajectories — http://arxiv.org/abs/2607.15330v2
[3] Linear Mappings of Free Algebra — http://arxiv.org/abs/1003.1544v2
[4] Non-linear positive maps between $C^*$-algebras — http://arxiv.org/abs/1811.03128v1
[5] Robotic Template Library — http://arxiv.org/abs/2107.00324v1
[6] Design of an Adaptive Lightweight LiDAR to Decouple Robot-Camera Geometry — http://arxiv.org/abs/2302.14334v2
[7] Grüss type inequalities for positive linear maps on $C^*$-algebras — http://arxiv.org/abs/1610.03868v1
[8] G.O.G: A Versatile Gripper-On-Gripper Design for Bimanual Cloth Manipulation with a Single Robotic Arm — http://arxiv.org/abs/2401.10702v1
[9] Dilepton measurements with CERES — http://arxiv.org/abs/0802.2679v1
[10] The CERES/NA45 Radial Drift Time Projection Chamber — http://arxiv.org/abs/0802.1443v2
[11] BVRI photometric evolution of the very fast Nova Ophiuchi 2010 N.1 = V2673 Oph — http://arxiv.org/abs/1003.5371v1
[12] A Molecular Implementation of the Least Mean Squares Estimator — http://arxiv.org/abs/1701.00602v1
[13] Fast Convergence for Weighted Least Squares Estimates — http://arxiv.org/abs/2605.00198v3
[14] nlstac: Non-Gradient Separable Nonlinear Least Squares Fitting — http://arxiv.org/abs/2402.04124v1
[15] Convergence of Alternating Least Squares Optimisation for Rank-One Approximation to High Order Tensors — http://arxiv.org/abs/1503.05431v1
[16] The Cosmological Parameters 2010 — http://arxiv.org/abs/1002.3488v1
[17] Four Simple Proprioceptive Estimators for Legged Robots — http://arxiv.org/abs/2605.23100v1
[18] The 4th Reactive Synthesis Competition (SYNTCOMP 2017): Benchmarks, Participants & Results — http://arxiv.org/abs/1711.11439v1
[19] Ghosts of Jupiter's past: is 2017 UV43 a relative of comet Shoemaker-Levy 9? — http://arxiv.org/abs/1712.03230v2
[20] ConceptNet at SemEval-2017 Task 2: Extending Word Embeddings with Multilingual Relational Knowledge — http://arxiv.org/abs/1704.03560v2
[21] Smoothing Out the Edges: Continuous-Time Estimation with Gaussian Process Motion Priors on Factor Graphs — http://arxiv.org/abs/2605.09073v1
[22] Relevance Score of Triplets Using Knowledge Graph Embedding - The Pigweed Triple Scorer at WSDM Cup 2017 — http://arxiv.org/abs/1712.08353v1
[23] Batch and Incremental Kinodynamic Motion Planning using Dynamic Factor Graphs — http://arxiv.org/abs/2005.12514v2
[24] Pre-proceedings of the 27th International Symposium on Logic-Based Program Synthesis and Transformation (LOPSTR 2017) — http://arxiv.org/abs/1708.07854v2
[25] Action Flow Matching for Continual Robot Learning — http://arxiv.org/abs/2504.18471v2
[26] Scalable Aerial GNSS Localization for Marine Robots — http://arxiv.org/abs/2505.04095v2
[27] Using Physiological Measures, Gaze, and Facial Expressions to Model Human Trust in a Robot Partner — http://arxiv.org/abs/2504.05291v1
[28] Model-Based Capacitive Touch Sensing in Soft Robotics: Achieving Robust Tactile Interactions for Artistic Applications — http://arxiv.org/abs/2503.02280v1
[29] Technical Report for ICRA 2025 GOOSE 3D Semantic Segmentation Challenge: Adaptive Point Cloud Understanding for Heterogeneous Robotic Systems — http://arxiv.org/abs/2506.06995v1
[30] Influence of Operator Expertise on Robot Supervision and Intervention — http://arxiv.org/abs/2601.15069v2
[31] Python Bindings for a Large C++ Robotics Library: The Case of OMPL — http://arxiv.org/abs/2603.04668v1
[32] ACM COMPUTE 2025 Best Practices Track Proceedings — http://arxiv.org/abs/2512.02349v2
[33] Nine Best Practices for Research Software Registries and Repositories: A Concise Guide — http://arxiv.org/abs/2012.13117v1
[34] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1
[35] CONAN -- the cruncher of local exchange coefficients for strongly interacting confined systems in one dimension — http://arxiv.org/abs/1603.02662v2
[36] Conan: a platform for complex network analysis — http://arxiv.org/abs/1012.0091v1
[37] CONAN: Complementary Pattern Augmentation for Rare Disease Detection — http://arxiv.org/abs/1911.13232v1
[38] Fast Iterative Tomographic Wave-front Estimation with Recursive Toeplitz Reconstructor Structure for Large Scale Systems — http://arxiv.org/abs/1806.07938v1
[39] CONAN: A Python package for modeling lightcurve and radial velocity data of exoplanetary systems — http://arxiv.org/abs/2508.20196v1
[40] FC-CONAN: An Exhaustively Paired Dataset for Robust Evaluation of Retrieval Systems — http://arxiv.org/abs/2601.01350v1
[41] Python Bindings for a Large C++ Robotics Library:The Case of OMPL — https://arxiv.org/html/2603.04668v1
[42] The $^{12}$C(n, 2n)$^{11}$C cross section from threshold to 26.5 MeV — http://arxiv.org/abs/1707.09375v2
[43] Conan: Progressive Learning to Reason Like a Detective over Multi-Scale Visual Evidence — http://arxiv.org/abs/2510.20470v2
[44] Simple-Robotics/nanoeigenpy - GitHub — https://github.com/Simple-Robotics/nanoeigenpy
[45] RobotPy · Python 3 for the FIRST Robotics Competition (FRC) — https://robotpy.github.io/
[46] Creating a C++ Extension - Robot Control Stack — https://robotcontrolstack.org/development/cpp_extension.html
[47] Developing a Python Interface utilizing Pybind11 for SHOT - Doria — https://www.doria.fi/bitstream/handle/10024/192709/ekman_johan.pdf?sequence=2&isAllowed=y
[48] Real-Time Service Subscription and Adaptive Offloading Control in Vehicular Edge Computing — http://arxiv.org/abs/2512.14002v1
[49] Real time state monitoring and fault diagnosis system for motor based on LabVIEW — http://arxiv.org/abs/1806.09998v1
[50] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1
[51] NTIRE 2025 Challenge on Image Super-Resolution (x4): Methods and Results — http://arxiv.org/abs/2504.14582v3
[52] Developing a Robotic Surgery Training System for Wide Accessibility and Research — http://arxiv.org/abs/2505.20562v2
[53] When Faster VLA Deployment Changes Closed-Loop Behavior: Task Success-Latency Analysis of SmolVLA Across PyTorch and ONNX Variants — http://arxiv.org/abs/2609.14146v2
[54] Self-Supervised Policy Adaptation during Deployment — http://arxiv.org/abs/2007.04309v3
[55] Real-Time-Data Analytics in Raw Materials Handling — http://arxiv.org/abs/1802.00625v1
[56] Inference-Time Attention Steering for Vision-Language-Action Driving Models — http://arxiv.org/abs/2608.17095v1
[57] BLURR: A Boosted Low-Resource Inference for Vision-Language-Action Models — http://arxiv.org/abs/2512.11769v1
[58] Task adaptation of Vision-Language-Action model: 1st Place Solution for the 2025 BEHAVIOR Challenge — http://arxiv.org/abs/2512.06951v2
[59] Your Vision-Language-Action Model Already Has Attention Heads For Path Deviation Detection — http://arxiv.org/abs/2603.13782v1
[60] Compositional Context Fine-Tuning Vision-Language Model for Complex Assembly Action Understanding from Videos — http://arxiv.org/abs/2607.10797v1
[61] Observation of $Ξ_{c}(2930)^0$ and updated measurement of $B^{-} \to K^{-} Λ_{c}^{+} \barΛ_{c}^{-}$ at Belle — http://arxiv.org/abs/1712.03612v3
[62] Characterizing the astrophysical S-factor for $^{12}$C+$^{12}$C with wave-packet dynamics — http://arxiv.org/abs/1802.01160v6
[63] Measurement of Meson Resonance Production in $π^{-} + $C Interactions at SPS energies — http://arxiv.org/abs/1705.08206v1
[64] $^{15}$C: from Halo-EFT structure to the study of transfer, breakup and radiative-capture reactions — http://arxiv.org/abs/1907.11753v2
[65] Differentiable Physics-based System Identification for Robotic Manipulation of Elastoplastic Materials — http://arxiv.org/abs/2411.00554v3
[66] DDBot: Differentiable Physics-based Digging Robot for Unknown Granular Materials — http://arxiv.org/abs/2510.17335v4
[67] Automatically designing robot swarms in environments populated by other robots: an experiment in robot shepherding — http://arxiv.org/abs/2404.18221v1
[68] Secure and secret cooperation in robotic swarms — http://arxiv.org/abs/1904.09266v3
[69] A Survey of Robot Manipulation in Contact — http://arxiv.org/abs/2112.01942v3
[70] Optimal Algorithm Allocation for Robotic Network Cloud Systems — http://arxiv.org/abs/2104.12710v5
[71] Eigen mode selection in human subject game experiment — http://arxiv.org/abs/2204.08071v1
[72] Deliberative Technology for Alignment — http://arxiv.org/abs/2312.03893v1
[73] Stochastic invariance of closed sets for jump-diffusions with non-Lipschitz coefficients — http://arxiv.org/abs/1612.07647v2
[74] Measurement incompatibility under loss — http://arxiv.org/abs/2411.05920v3
[75] Aligning Artificial Superintelligence via a Multi-Box Protocol — http://arxiv.org/abs/2511.21779v1
[76] Gain Stabilization of SiPMs — http://arxiv.org/abs/1403.8104v1
[77] Incompatibility of the Copenhagen interpretation with quantum mechanics formalism — http://arxiv.org/abs/physics/0604111v2
[78] Towards Learning Geometric Eigen-Lengths Crucial for Fitting Tasks — http://arxiv.org/abs/2312.15610v1
[79] ROBUSfT: Robust Real-Time Shape-from-Template, a C++ Library — http://arxiv.org/abs/2301.04037v3
[80] VLSP 2025 MLQA-TSR Challenge: Vietnamese Multimodal Legal Question Answering on Traffic Sign Regulation — http://arxiv.org/abs/2510.20381v1
[81] Autonomous Planning In-space Assembly Reinforcement-learning free-flYer (APIARY) International Space Station Astrobee Testing — http://arxiv.org/abs/2512.03729v1
[82] CMU's IWSLT 2025 Simultaneous Speech Translation System — http://arxiv.org/abs/2506.13143v1
[83] Towards Transparent Ethical AI: A Roadmap for Trustworthy Robotic Systems — http://arxiv.org/abs/2508.05846v1
[84] Latency Analysis of ROS2 Multi-Node Systems — http://arxiv.org/abs/2101.02074v3
[85] On the Off-chip Memory Latency of Real-Time Systems: Is DDR DRAM Really the Best Option? — http://arxiv.org/abs/1810.07059v1
[86] The ring-buffer ROS2 executor: a novel approach for real-time ROS2 Space applications — https://doi.org/10.1109/SCC57168.2023.00021
[87] Edge Computing–Enabled Intelligent Financial Auditing: An Advanced Real-Time Framework for Automated Fraud Detection, Predictive Accounting Analytics, and Financial Risk Assessment — https://doi.org/10.63544/jbii.v5i5.194
[88] Self-Evolving Autonomous Software Architectures Using Large-Scale Graph Neural Networks and Real-Time Big Data Feedback Loops for Economic Optimization and Cost-Efficient Resource Allocation — https://doi.org/10.63544/jbii.v5i5.188
[89] A Task-Agnostic Algebraic Integrity Metric for Event-Camera Streams Toward SOTIF-Compliant Perception using Pearson Correlation Coefficient — https://arxiv.org/abs/2605.21500
[90] The AudioMOS Challenge 2025 — http://arxiv.org/abs/2509.01336v1
[91] VQualA 2025 Challenge on Visual Quality Comparison for Large Multimodal Models: Methods and Results — http://arxiv.org/abs/2509.09190v1
[92] Developing a 21st Century Global Library for Mathematics Research — http://arxiv.org/abs/1404.1905v1
[93] The RSNA Abdominal Traumatic Injury CT (RATIC) Dataset — http://arxiv.org/abs/2405.19595v1
[94] Student's T Robust Bundle Adjustment Algorithm — http://arxiv.org/abs/1111.1400v1
[95] Power Bundle Adjustment for Large-Scale 3D Reconstruction — http://arxiv.org/abs/2204.12834v4
[96] Pedestrian Attribute Recognition: A New Benchmark Dataset and A Large Language Model Augmented Framework — http://arxiv.org/abs/2408.09720v1
[97] The RSNA Lumbar Degenerative Imaging Spine Classification (LumbarDISC) Dataset — http://arxiv.org/abs/2506.09162v1
[98] Bitstream-Corrupted Video Recovery: A Novel Benchmark Dataset and Method — http://arxiv.org/abs/2309.13890v2
[99] CPRet: A Dataset, Benchmark, and Model for Retrieval in Competitive Programming — http://arxiv.org/abs/2505.12925v2
[100] L-FAME: Longitudinal Focused Attention Meditation EEG Dataset and Benchmark — http://arxiv.org/abs/2605.22893v1
[101] PINOCCHIO and the hierarchical build-up of dark matter haloes — http://arxiv.org/abs/astro-ph/0109324v1
[102] Robust bundle adjustment for large-scale structure from motion — https://doi.org/10.1007/s11042-017-4581-5
[103] The Relativistic Elasticity of Rigid Bodies — http://arxiv.org/abs/physics/0307019v3
[104] Caspar: CUDA Accelerator for Symbolic Programming with Adaptive Reordering — https://doi.org/10.48550/arxiv.2605.30583
[105] On the invariant motions of rigid body rotation over the fixed point, via Euler angles — http://arxiv.org/abs/1601.04526v1
[106] Network Anatomy and Real-Time Measurement of Nvidia GeForce NOW Cloud Gaming — http://arxiv.org/abs/2401.06366v2


---

*Generated by research-bot · topic=`cpp-robotics` · depth=`standard` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading · model=`deepseek-v4-flash` · sources=106 · duration=255s · 2026-10-04T02:59:09+00:00*
