# 具身智能·人形与腿足运动控制（Humanoid & Legged Locomotion）深度调研报告

**报告日期**：2026-10-04 ｜ **领域**：具身智能 · 人形与腿足机器人运动控制（learning-based WBC / legged locomotion）｜ **检索源**：157 条候选来源（以 arXiv cs.RO / cs.LG 预印本为主，含少量官方 GitHub 仓库）+ 9 条领域种子资源（3 篇论文 / 4 个开源项目 / 2 个数据集）

> **证据纪律声明**：本报告严格只引用所给来源编号 [1]–[157] 与领域种子资源链接。候选块普遍**未提供引用数（citations）、GitHub star、下载量或榜单排名**，因此凡涉及热度类数字，一律标注 `> 待核实`，**不作任何数字推测**。凡仅有论文标题、摘要片段被截断而无法确认本体型号、任务数与评测口径的，一律标注 `> 待核实`。

---

## 摘要（Executive Summary）

1. **学习式方法已成为人形与腿足运动控制的主导范式**，其技术主干为「大规模并行仿真 + 强化学习 + 域随机化 + 教师-学生蒸馏」，代表性基础设施为 Isaac Gym [48] 及其后继 Isaac Lab [50]，代表性训练框架为 Humanoid-Gym [47] 与 Distillation-PPO [119]。
2. **近 18 个月的重心从「单任务策略」转向「可复用全身控制器（WBC）」**：Expressive Whole-Body Control [81]、ExBody2 [80]、HOVER [73] 与 ASAP [82]、ULTRA [148] 等，目标是把运动、操作与多模态指令统一到一个人形全身控制器中。
3. **人形 loco-manipulation 正沿两条路线并行**：一是遥操作/人类示教驱动（H2O [76]、OmniH2O [75]、TWIST [77]、CHILD [71]、HumanPlus [153]），二是仿真 RL + 视频/动作先验驱动（SUGAR [152]、ViLoMan [151]、OpenHLM [150]、HMI [70]）。两条路线的**共同瓶颈是高质量全身数据稀缺**，HMI [70] 明确以「无机器人演示（robot-free demonstrations）」绕开该瓶颈。
4. **sim2real 的方法论正在从「域随机化」升级为「仿真器本身的自适应/物理对齐」**：Simulator Adaptation via Proprioceptive Distribution Matching [19] 主张免时间对齐、免外部动捕地适配仿真动力学；ASAP [82] 则走「仿真-真机物理对齐」路线。相关工作综述见 [60]、[107]。
5. **评测口径高度不可比**：HumanoidBench [90] 提供仿真全身基准，Open X-Embodiment [104] 提供跨本体操作数据，但**人形运动/全身控制在真机上的统一榜单在本次候选集中未出现** `> 待核实`。多数论文的「SOTA」是在自建任务集与自选本体上报告，跨论文不可直接比较。
6. **主要开放争议**：真机 RL 的安全性、奖励设计与样本效率三大障碍 [12]；视觉跑酷的泛化与专一化权衡 [2][11]；跌倒/受击恢复缺乏统一安全评测 [100][118]；跨本体缩放律（embodiment scaling laws）仅处于初步探索 [103]。
7. **证据强度整体偏弱**：绝大多数条目为 arXiv 预印本（B 级），少数对应期刊级发表（如 [26] 对应种子资源中的 Science Robotics 论文）。**本报告所有「关注度/推荐度」均基于可核查的权威性与主题相关性给出，热度数字一律留空待核实。**

---

## 一、关键前沿进展（近 1–2 年）

### 1.1 时间线（按年份/季度组织，证据强度逐条标注）

| 时间 | 代表工作 | 一句话贡献 | 证据强度 |
|---|---|---|---|
| 2024 | H2O / Learning Human-to-Humanoid Real-Time Whole-Body Teleoperation [76] | 人形实时全身遥操作，被种子资源标注为 IROS 2024 | 种子资源明确标注会议，B/A 之间 |
| 2024 | OmniH2O [75] | 通用灵巧的「人→人形」全身遥操作与学习 | arXiv 预印本（B）[75] |
| 2024 | Expressive Whole-Body Control [81] / ExBody2 [80] | 强调「表达性」全身控制，把运动与上半身表现统一 | arXiv 预印本（B）[81][80]，附官方仓库 [156] |
| 2024 | Humanoid Parkour Learning [11] / Extreme Parkour [14] / PIE [5] | 把人形与腿足的跑酷推向视觉驱动与隐式-显式混合框架 | arXiv 预印本（B）[11][14][5] |
| 2024 | Humanoid-Gym [47] | 人形 RL 零样本 sim2real 的开源训练环境 | arXiv 预印本（B）[47] |
| 2024 | HumanPlus [153] / 3D Diffusion Policies [155] | 人类示教影子模仿 + 3D 扩散策略的泛化人形操作 | arXiv 预印本（B）[153][155]，官方仓库 [157] |
| 2024 末 | HOVER [73] | 面向人形的多功能神经全身控制器 | arXiv 预印本（B）[73] |
| 2025 | ASAP [82] | 对齐仿真与真机物理以学习敏捷人形全身技能 | arXiv 预印本（B）[82] |
| 2025 | TWIST [77] / CHILD [71] | 全身模仿系统与关节级全身遥操作系统 | arXiv 预印本（B）[77][71] |
| 2025 | Robot Trains Robot [12] | 指出现有真机人形 RL 与策略自适应的稀缺性与三大障碍 | arXiv 预印本（B）[12] |
| 2025 | Learning Sim-to-Real Humanoid Locomotion in 15 Minutes [83] | 把并行仿真收益推向「分钟级」人形 sim2real | arXiv 预印本（B）[83]（标题数字即论文命题，非本报告推断） |
| 2025 | Bracing for Impact [100] / Hierarchical Reduced-Order MPC [101] | 降阶模型驱动的受击恢复与鲁棒行走（模型基对照路线） | arXiv 预印本（B）[100][101] |
| 2025 | Humanoid Whole-Body Badminton [68] | 用退火 RL 课程学习统一全身动态交互（羽毛球） | arXiv 预印本（B）[68] |
| 2025 | Towards Embodiment Scaling Laws in Robot Locomotion [103] | 提出并初步检验「增加训练本体数提升泛化」假设 | arXiv 预印本（B）[103] |
| 2026 | ULTRA [148] / OpenHLM [150] / ViLoMan [151] / SUGAR [152] | 多模态统一控制、全身 loco-manipulation 经验配方、视觉-本体感知技能、人类视频驱动 | 仅标题与年份可得（B，细节待核实）[148][150][151][152] |
| 2026 | Humanoid Manipulation Interface (HMI) [70] | 从「无机器人演示」学习人形全身操作 | arXiv 预印本（B）[70] |
| 2026 | Simulator Adaptation for Sim-to-Real Learning [19] | 用本体感知分布匹配替代时间对齐做仿真器适配 | arXiv 预印本（B）[19] |
| 2026 | The Open Ant [3] | 提供真机 RL 研究平台，报告可在一小时内从物理经验从

## 参考来源

[1] One-Shot Reinforcement Learning for Robot Navigation with Interactive Replay — http://arxiv.org/abs/1711.10137v2
[2] Robot Parkour Learning — http://arxiv.org/abs/2309.05665v2
[3] The Open Ant: A Robot Platform for Reinforcement Learning Research — http://arxiv.org/abs/2607.18488v1
[4] Value Bonuses using Ensemble Errors for Exploration in Reinforcement Learning — http://arxiv.org/abs/2602.12375v1
[5] PIE: Parkour with Implicit-Explicit Learning Framework for Legged Robots — http://arxiv.org/abs/2408.13740v3
[6] On-Policy Robot Imitation Learning from a Converging Supervisor — http://arxiv.org/abs/1907.03423v7
[7] Deception Game: Closing the Safety-Learning Loop in Interactive Robot Autonomy — http://arxiv.org/abs/2309.01267v2
[8] Proceedings of the Dialogue Robot Competition 2023 — http://arxiv.org/abs/2312.14430v5
[9] Multi-objective Model-based Policy Search for Data-efficient Learning with Sparse Rewards — http://arxiv.org/abs/1806.09351v3
[10] State-of-the-art in Robot Learning for Multi-Robot Collaboration: A Comprehensive Survey — http://arxiv.org/abs/2408.11822v1
[11] Humanoid Parkour Learning — http://arxiv.org/abs/2406.10759v2
[12] Robot Trains Robot: Automatic Real-World Policy Adaptation and Learning for Humanoids — http://arxiv.org/abs/2508.12252v2
[13] Stabilizing Extreme Q-learning by Maclaurin Expansion — http://arxiv.org/abs/2406.04896v2
[14] Extreme Parkour with Legged Robots — http://arxiv.org/abs/2309.14341v1
[15] On Terrain-Aware Locomotion for Legged Robots — http://arxiv.org/abs/2212.00683v1
[16] Learning Robust, Agile, Natural Legged Locomotion Skills in the Wild — http://arxiv.org/abs/2304.10888v3
[17] ATRos: Learning Energy-Efficient Agile Locomotion for Wheeled-legged Robots — http://arxiv.org/abs/2510.09980v1
[18] TOP-Nav: Legged Navigation Integrating Terrain, Obstacle and Proprioception Estimation — http://arxiv.org/abs/2404.15256v4
[19] Simulator Adaptation for Sim-to-Real Learning of Legged Locomotion via Proprioceptive Distribution Matching — http://arxiv.org/abs/2604.11090v1
[20] Generating a Terrain-Robustness Benchmark for Legged Locomotion: A Prototype via Terrain Authoring and Active Learning — http://arxiv.org/abs/2208.07681v3
[21] ICPR 2024 Competition on Domain Adaptation and GEneralization for Character Classification (DAGECC) — http://arxiv.org/abs/2412.17984v1
[22] On State Estimation for Legged Locomotion over Soft Terrain — http://arxiv.org/abs/2101.02279v1
[23] Learning Getting-Up Policies for Real-World Humanoid Robots — http://arxiv.org/abs/2502.12152v2
[24] Learning Humanoid Standing-up Control across Diverse Postures — http://arxiv.org/abs/2502.08378v2
[25] Deploying COTS Legged Robot Platforms into a Heterogeneous Robot Team — http://arxiv.org/abs/2106.07182v1
[26] Learning agile and dynamic motor skills for legged robots — http://arxiv.org/abs/1901.08652v1
[27] Prototyping fast and agile motions for legged robots with Horizon — http://arxiv.org/abs/2206.08587v1
[28] RMA: Rapid Motor Adaptation for Legged Robots — http://arxiv.org/abs/2107.04034v1
[29] Scalable Aerial GNSS Localization for Marine Robots — http://arxiv.org/abs/2505.04095v2
[30] Mastering Agile Jumping Skills from Simple Practices with Iterative Learning Control — http://arxiv.org/abs/2408.02619v1
[31] Advances, challenges, and opportunities for legged robots — http://arxiv.org/abs/2607.28952v1
[32] Agile But Safe: Learning Collision-Free High-Speed Legged Locomotion — http://arxiv.org/abs/2401.17583v3
[33] This paper has been withdrawn — http://arxiv.org/abs/cond-mat/0309395v2
[34] End-to-End Reinforcement Learning for Torque Based Variable Height Hopping — http://arxiv.org/abs/2307.16676v2
[35] Bed-inventory Overturn Mechanism for Pant-leg Circulating Fluidized Bed Boilers — http://arxiv.org/abs/1101.3661v1
[36] Laboratory Astrophysics White Paper (based on the 2010 NASA Laboratory Astrophysics Workshop in Gatlinberg, Tennessee, 25-28 October 2010) — http://arxiv.org/abs/1103.1341v1
[37] Maximize the Foot Clearance for a Hopping Robotic Leg Considering Motor Saturation — http://arxiv.org/abs/2107.13717v2
[38] Desperately Seeking Superstrings — http://arxiv.org/abs/physics/9403001v1
[39] Tunable Leg Stiffness in a Monopedal Hopper for Energy-Efficient Vertical Hopping Across Varying Ground Profiles — http://arxiv.org/abs/2508.02873v3
[40] Nonlinear dynamics of running: Speed, stability, symmetry and the effects of leg amputations — http://arxiv.org/abs/1305.6821v1
[41] On multi-step prediction models for receding horizon control — http://arxiv.org/abs/1802.09767v1
[42] Economic model predictive control for snake robot locomotion — http://arxiv.org/abs/1909.00795v2
[43] Model Predictive Control with Environment Adaptation for Legged Locomotion — http://arxiv.org/abs/2105.05998v4
[44] QCD and High Energy Interactions: Moriond 2018 Theory Summary — http://arxiv.org/abs/1806.04982v2
[45] Evaluation of an open-source implementation of the SRP-PHAT algorithm within the 2018 LOCATA challenge — http://arxiv.org/abs/1812.05901v1
[46] Asynchronous Splitting Design for Model Predictive Control — http://arxiv.org/abs/1609.05801v1
[47] Humanoid-Gym: Reinforcement Learning for Humanoid Robot with Zero-Shot Sim2Real Transfer — http://arxiv.org/abs/2404.05695v2
[48] Isaac Gym: High Performance GPU-Based Physics Simulation For Robot Learning — http://arxiv.org/abs/2108.10470v2
[49] A ROS-based Software Framework for the NimbRo-OP Humanoid Open Platform — http://arxiv.org/abs/1809.11051v1
[50] Isaac Lab: A GPU-Accelerated Simulation Framework for Multi-Modal Robot Learning — http://arxiv.org/abs/2511.04831v1
[51] The Synthesis of Optimal Control Laws Using Isaacs' Method for the Solution of Differential Games — http://arxiv.org/abs/2112.10849v2
[52] MARS-Gym: A Gym framework to model, train, and evaluate Recommender Systems for Marketplaces — http://arxiv.org/abs/2010.07035v1
[53] NimbRo-OP2: Grown-up 3D Printed Open Humanoid Platform for Research — http://arxiv.org/abs/1809.11144v1
[54] Training Software Engineering Agents and Verifiers with SWE-Gym — http://arxiv.org/abs/2412.21139v2
[55] Bridging the Sim2Real Gap: Vision Encoder Pre-Training for Visuomotor Policy Transfer — http://arxiv.org/abs/2501.16389v2
[56] The Importance and the Limitations of Sim2Real for Robotic Manipulation in Precision Agriculture — http://arxiv.org/abs/2008.03983v1
[57] Probing the Nature of the G1 Clump Stellar Overdensity in the Outskirts of M31 — http://arxiv.org/abs/astro-ph/0611852v1
[58] Sim2Real Transfer for Audio-Visual Navigation with Frequency-Adaptive Acoustic Field Prediction — http://arxiv.org/abs/2405.02821v2
[59] G1: Bootstrapping Perception and Reasoning Abilities of Vision-Language Model via Reinforcement Learning — http://arxiv.org/abs/2505.13426v1
[60] Perspectives on Sim2Real Transfer for Robotics: A Summary of the R:SS 2020 Workshop — http://arxiv.org/abs/2012.03806v1
[61] Massive stars with Pollux on LUVOIR — http://arxiv.org/abs/1811.05264v1
[62] Causal-Paced Deep Reinforcement Learning — http://arxiv.org/abs/2507.02910v1
[63] Exploring Hierarchy-Aware Inverse Reinforcement Learning — http://arxiv.org/abs/1807.05037v1
[64] Towards Formalizing Reinforcement Learning Theory: A Robbins-Siegmund Approach — http://arxiv.org/abs/2511.03618v2
[65] Anderson Acceleration for Reinforcement Learning — http://arxiv.org/abs/1809.09501v1
[66] A Tutorial on Meta-Reinforcement Learning — http://arxiv.org/abs/2301.08028v4
[67] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1
[68] Humanoid Whole-Body Badminton via an Annealed Reinforcement Learning Curriculum — http://arxiv.org/abs/2511.11218v4
[69] The Role of Domain Randomization in Training Diffusion Policies for Whole-Body Humanoid Control — http://arxiv.org/abs/2411.01349v1
[70] Humanoid Manipulation Interface: Humanoid Whole-Body Manipulation from Robot-Free Demonstrations — http://arxiv.org/abs/2602.06643v2
[71] CHILD (Controller for Humanoid Imitation and Live Demonstration): a Whole-Body Humanoid Teleoperation System — http://arxiv.org/abs/2508.00162v2
[72] Humanoid Whole-Body Manipulation via Active Spatial Brain and Generalizable Action Cerebellum — http://arxiv.org/abs/2605.21133v2
[73] HOVER: Versatile Neural Whole-Body Controller for Humanoid Robots — http://arxiv.org/abs/2410.21229v2
[74] Whole-Body Geometric Retargeting for Humanoid Robots — http://arxiv.org/abs/1909.10080v1
[75] OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning — http://arxiv.org/abs/2406.08858v1
[76] Learning Human-to-Humanoid Real-Time Whole-Body Teleoperation — http://arxiv.org/abs/2403.04436v1
[77] TWIST: Teleoperated Whole-Body Imitation System — http://arxiv.org/abs/2505.02833v1
[78] CLOT: Closed-Loop Global Motion Tracking for Whole-Body Humanoid Teleoperation — http://arxiv.org/abs/2602.15060v2
[79] Dynamic Locomotion Teleoperation of a Wheeled Humanoid Robot Reduced Model with a Whole-Body Human-Machine Interface — http://arxiv.org/abs/2109.03906v1
[80] ExBody2: Advanced Expressive Humanoid Whole-Body Control — http://arxiv.org/abs/2412.13196v2
[81] Expressive Whole-Body Control for Humanoid Robots — http://arxiv.org/abs/2402.16796v2
[82] ASAP: Aligning Simulation and Real-World Physics for Learning Agile Humanoid Whole-Body Skills — http://arxiv.org/abs/2502.01143v3
[83] Learning Sim-to-Real Humanoid Locomotion in 15 Minutes — http://arxiv.org/abs/2512.01996v1
[84] Towards Miniature Humanoid Tele-Loco-Manipulation Using Virtual Reality and Reinforcement Learning — http://arxiv.org/abs/2607.20399v1
[85] Physics Briefing Book — http://arxiv.org/abs/1910.11775v2
[86] Physics and Technology of the Next Linear Collider: A Report Submitted to Snowmass '96 — http://arxiv.org/abs/hep-ex/9605011v1
[87] LeCAR-Lab/human2humanoid — https://github.com/LeCAR-Lab/human2humanoid
[88] NTU-NPU System for Voice Privacy 2024 Challenge — http://arxiv.org/abs/2410.02371v1
[89] Real-World Humanoid Locomotion with Reinforcement Learning — http://arxiv.org/abs/2303.03381v2
[90] HumanoidBench: Simulated Humanoid Benchmark for Whole-Body Locomotion and Manipulation — http://arxiv.org/abs/2403.10506v2
[91] MuJoCo MPC for Humanoid Control: Evaluation on HumanoidBench — http://arxiv.org/abs/2408.00342v1
[92] ICML Topological Deep Learning Challenge 2024: Beyond the Graph Domain — http://arxiv.org/abs/2409.05211v1
[93] Discovery Opportunities with Gravitational Waves -- TASI 2024 Lecture Notes — http://arxiv.org/abs/2409.08956v1
[94] Atmospheric entry and fragmentation of small asteroid 2024 BX1: Bolide trajectory, orbit, dynamics, light curve, and spectrum — http://arxiv.org/abs/2403.00634v2
[95] Uncovering Coordinated Cross-Platform Information Operations Threatening the Integrity of the 2024 U.S. Presidential Election Online Discussion — http://arxiv.org/abs/2409.15402v2
[96] A Simulation and Modeling of Access Points with Definition Language — http://arxiv.org/abs/1304.1836v2
[97] ICAGC 2024: Inspirational and Convincing Audio Generation Challenge 2024 — http://arxiv.org/abs/2407.12038v2
[98] Double Multi-Head Attention Multimodal System for Odyssey 2024 Speech Emotion Recognition Challenge — http://arxiv.org/abs/2406.10598v1
[99] Superconductivity as a consequence of an ordering of the electron gas zero-point oscillations — http://arxiv.org/abs/1005.0280v6
[100] Bracing for Impact: Robust Humanoid Push Recovery and Locomotion with Reduced Order Models — http://arxiv.org/abs/2505.11495v2
[101] Hierarchical Reduced-Order Model Predictive Control for Robust Locomotion on Humanoid Robots — http://arxiv.org/abs/2509.04722v1
[102] Learning Humanoid Locomotion over Challenging Terrain — http://arxiv.org/abs/2410.03654v1
[103] Towards Embodiment Scaling Laws in Robot Locomotion — http://arxiv.org/abs/2505.05753v2
[104] Open X-Embodiment: Robotic Learning Datasets and RT-X Models — http://arxiv.org/abs/2310.08864v9
[105] Open-H-Embodiment: A Large-Scale Dataset for Enabling Foundation Models in Medical Robotics — http://arxiv.org/abs/2604.21017v3
[106] Open-Ended Learning Leads to Generally Capable Agents — http://arxiv.org/abs/2107.12808v2
[107] Sim-to-Real Transfer in Deep Reinforcement Learning for Bipedal Locomotion — http://arxiv.org/abs/2511.06465v1
[108] Legged Robots that Keep on Learning: Fine-Tuning Locomotion Policies in the Real World — http://arxiv.org/abs/2110.05457v1
[109] Locomotion Beyond Feet — http://arxiv.org/abs/2601.03607v1
[110] Failure Mechanisms and Risk Estimation for Legged Robot Locomotion on Granular Slopes — http://arxiv.org/abs/2603.06928v2
[111] Motion Planning for Agile Legged Locomotion using Failure Margin Constraints — http://arxiv.org/abs/2203.15107v1
[112] Deep Reinforcement Learning for Decentralized Multi-Robot Control: A DQN Approach to Robustness and Information Integration — http://arxiv.org/abs/2408.11339v1
[113] Improving Input-Output Linearizing Controllers for Bipedal Robots via Reinforcement Learning — http://arxiv.org/abs/2004.07276v2
[114] Continuous-Discrete Reinforcement Learning for Hybrid Control in Robotics — http://arxiv.org/abs/2001.00449v1
[115] A Real-Time Model-Based Reinforcement Learning Architecture for Robot Control — http://arxiv.org/abs/1105.1749v2
[116] Safe Reinforcement Learning with Chance-constrained Model Predictive Control — http://arxiv.org/abs/2112.13941v2
[117] Coordinated Humanoid Robot Locomotion with Symmetry Equivariant Reinforcement Learning Policy — https://arxiv.org/abs/2508.01247
[118] Discovering Self-Protective Falling Policy for Humanoid Robot via Deep Reinforcement Learning — https://arxiv.org/abs/2512.01336
[119] Distillation-PPO: A Novel Two-Stage Reinforcement Learning Framework for Humanoid Robot Perceptive Locomotion — https://arxiv.org/abs/2503.08299
[120] Control of a Rigid Wing Pumping Airborne Wind Energy System in all Operational Phases — http://arxiv.org/abs/2006.11141v1
[121] Safe Control Synthesis via Input Constrained Control Barrier Functions — http://arxiv.org/abs/2104.01704v1
[122] Exponential input-to-state stabilization of a class of diagonal boundary control systems with delay boundary control — http://arxiv.org/abs/2003.05711v1
[123] Real-time Optimal Landing Control of the MIT Mini Cheetah — http://arxiv.org/abs/2110.02799v1
[124] Kernel-based error bounds of bilinear Koopman surrogate models for nonlinear data-driven control — http://arxiv.org/abs/2503.13407v4
[125] Robust Local Stabilization of Nonlinear Systems with Controller-Dependent Norm Bounds: A Convex Approach with Input-Output Sampling — http://arxiv.org/abs/2212.03225v1
[126] Boundary Control of a Nonhomogeneous Flexible Wing with Bounded Input Disturbances — http://arxiv.org/abs/1709.00759v2
[127] Data-Driven Control of Nonlinear Systems: Beyond Polynomial Dynamics — http://arxiv.org/abs/2011.11355v3
[128] Optimal control of a single leg hopper by Liouvillian system reduction — http://arxiv.org/abs/1710.02133v1
[129] Faster Consensus via a Sparser Controller — http://arxiv.org/abs/2302.01021v2
[130] A Control-Oriented Notion of Finite State Approximation — http://arxiv.org/abs/1105.3788v3
[131] A Quantum-Compliant Formulation for Network Epidemic Control — http://arxiv.org/abs/2509.00337v1
[132] On $\ell_2$-performance of weakly-hard real-time control systems — http://arxiv.org/abs/2305.07875v3
[133] Capture Point Control in Thruster-Assisted Bipedal Locomotion — http://arxiv.org/abs/2406.14799v1
[134] Learning Bipedal Locomotion on Gear-Driven Humanoid Robot Using Foot-Mounted IMUs — http://arxiv.org/abs/2504.00614v2
[135] Deep Reinforcement Learning for Bipedal Locomotion: A Brief Survey — http://arxiv.org/abs/2404.17070v7
[136] Constrained Reinforcement Learning for Unstable Point-Feet Bipedal Locomotion Applied to the Bolt Robot — http://arxiv.org/abs/2508.02194v1
[137] Bipedal locomotion using variable stiffness actuation — http://arxiv.org/abs/1706.00339v1
[138] Socially Acceptable Bipedal Navigation: A Signal-Temporal-Logic- Driven Approach for Safe Locomotion — http://arxiv.org/abs/2310.09969v1
[139] Learning to Discern: Imitating Heterogeneous Human Demonstrations with Preference and Representation Learning — http://arxiv.org/abs/2310.14196v1
[140] Untangling Dense Knots by Learning Task-Relevant Keypoints — http://arxiv.org/abs/2011.04999v1
[141] CORL: Research-oriented Deep Offline Reinforcement Learning Library — http://arxiv.org/abs/2210.07105v4
[142] Accelerating Model Predictive Control for Legged Robots through Distributed Optimization — http://arxiv.org/abs/2403.11742v5
[143] Dense Temporal Motion Retargeting for Legged Robots — http://arxiv.org/abs/2609.38617v1
[144] Features characterizing safe aerial-aquatic robots — http://arxiv.org/abs/2410.23722v1
[145] OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning — https://arxiv.org/abs/2406.08858
[146] Coordinated Humanoid Manipulation with Choice Policies — https://arxiv.org/abs/2512.25072
[147] Real-Time Whole-Body Control of Legged Robots with Model-Predictive Path Integral Control — http://arxiv.org/abs/2409.10469v1
[148] ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation — http://arxiv.org/abs/2603.03279v2
[149] Humanoid Agent via Embodied Chain-of-Action Reasoning with Multimodal Foundation Models for Zero-Shot Loco-Manipulation — http://arxiv.org/abs/2504.09532v3
[150] OpenHLM: An Empirical Recipe for Whole-Body Humanoid Loco-Manipulation — http://arxiv.org/abs/2606.22174v1
[151] ViLoMan: Learning Visual-Proprioceptive Whole-Body Loco-Manipulation Skills for Humanoid Robots — http://arxiv.org/abs/2609.19340v1
[152] SUGAR: A Scalable Human-Video-Driven Generalizable Humanoid Loco-Manipulation Learning Framework — http://arxiv.org/abs/2605.20373v1
[153] HumanPlus: Humanoid Shadowing and Imitation from Humans — http://arxiv.org/abs/2406.10454v1
[154] VividFace: Real-Time and Realistic Facial Expression Shadowing for Humanoid Robots — http://arxiv.org/abs/2602.07506v2
[155] Generalizable Humanoid Manipulation with 3D Diffusion Policies — http://arxiv.org/abs/2410.10803v3
[156] edpsw/exbody2 — https://github.com/edpsw/exbody2
[157] MarkFzp/humanplus — https://github.com/MarkFzp/humanplus


---

*Generated by research-bot · topic=`embodied-humanoid` · depth=`standard` · rounds=2 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading · model=`deepseek-v4-flash` · sources=157 · duration=692s · 2026-10-04T03:21:20+00:00*
