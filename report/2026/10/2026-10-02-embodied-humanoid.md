# 具身智能·人形与腿足运动（Humanoid & Legged Locomotion）学习式控制前沿调研报告

> **日期**：2026-10-02（UTC）　**领域**：具身智能 / 人形与腿足运动控制（RL sim2real、WBC、地形适应、敏捷运动）　**检索源数量**：候选来源 101 条，本报告实际引用 68 条（编号见文末）
> **证据口径声明**：本次可用证据集中，除 [72] 标注为 IEEE Transactions on Robotics 外，其余条目均以 arXiv 预印本（cs.RO / cs.LG）形式提供，缺乏引用数、GitHub star、榜单排名等第三方热度指标。因此本报告凡未获得真实热度指标的条目，一律标注 `热度 > 待核实`；凡"关注度"给分者，均在括号内写明其依据口径（多为"本次多子问题检索中重复召回"这类**检索层面信号**，而非社区热度信号），请勿将其误读为引用量或社区共识。所有关键论断均带 [n] 引用，未核实内容均显式标注 `> 待核实`。

---

## 摘要（Executive Summary）

本报告围绕六个子问题（q1 敏捷突破、q2 全身控制与遥操作、q3 经典脉络、q4 开源工程栈、q5 数据集与基准、q6 地形适应与 sim2real 边界）对人形与腿足运动的学习式范式做了系统梳理，主要结论如下：

1. **仿真吞吐量已经成为方法论的"前置变量"**。GPU 并行仿真把 RL 训练从"天"压到"分钟"，从 Isaac Gym 的"几分钟学会走路"[19][56] 到 2025 年的"15 分钟 sim2real 人形行走"[63]，训练时长本身被当作可优化目标，而不仅是工程细节。
2. **人形运动的重心正在从"稳定行走"转向"敏捷 + 全身 loco-manipulation"**。parkour[66]、稀疏落脚点[67]、推力恢复[68]、全身羽毛球[7]、手/膝/肘多接触移动[12]、无机器人演示的全身操作[11] 共同构成 2024–2026 的新前沿。
3. **sim2real 的主线仍是"特权学习 + 教师-学生蒸馏 + 域随机化"**，从 RMA[25] 到双足适配[27][29][31] 到真机人形 RL[75]，这条技术路线在 2026 年仍是主流基线；新增变量是**真机在环学习**[3][57] 与**扩散策略下的域随机化标定**[6]。
4. **地形适应正从"盲走本体感知"走向"感知 + 步态自适应 + 地形编码"**，代表工作包括人形挑战地形行走[42]、实时足下地形重建的步态自适应[43]、全局-局部注意力地形编码[44]、上下文感知地形适配[33] 与间隙地形穿越[72]。
5. **MPC/凸优化 WBC 并未被 RL 取代，而是与之分层混合**：快速全身 MPC 精度裁剪[8]、降阶模型分层控制[64]、降阶模型推力恢复[68] 表明"模型法做骨架、学习法做细节"是当前工程上更稳的组合。
6. **评测与数据仍是最大缺口**。仿真侧有 HumanoidBench[80]、MuJoCo Playground[82]、地形鲁棒性基准[84]，但 **真机 SOTA 与仿真 SOTA 不可直接比较**（任务数、本体、硬件、是否真机均不一致，多数条目未报告统一口径），人形 loco-manipulation 也缺乏公认真机榜单 `> 待核实`。
7. **开源栈门槛已明显下降但仍不低**：Isaac Lab[54]/Isaac Gym[56]/legged_gym（种子）/unitree_rl_gym（种子）/ProtoMotions（种子）/MuJoCo Playground[82] 构成可复用训练栈，但普遍需要 NVIDIA GPU 与并行仿真经验，真机复现还需硬件与安全回退设计。

---

## 一、关键前沿进展（近 1–2 年，2024–2026）

> 本节"热度"列统一说明：本次证据集未提供任何条目的引用数/star/下载量，故除 [72]（citations=14）外，热度一律 `> 待核实`。关注度列的依据已写入括号，多为**检索层面重复召回信号**，不构成社区热度证据。四类证据轴均以行内 [n] 为该行唯一来源。

| 条目 | 时间 | 类别 | 一句话贡献 | 权威 | 热度 | 关注度 | 推荐度 |
|---|---|---|---|---|---|---|---|
| [Humanoid Parkour Learning](http://arxiv.org/abs/2406.10759v2) [66] | 2024 | 敏捷运动 | 用单一学习式策略完成人形跑酷式越障，把 parkour 引入人形 | arXiv 预印本 cs.RO，非同行评审（B 级） | > 待核实 | 中（本次 q1/q2 检索重复召回） | ★★★★☆（人形敏捷运动代表性工作，直接相关） |
| [BeamDojo](http://arxiv.org/abs/2502.10363v3) [67] | 2025 | 稀疏落脚点 | 面向稀疏落脚点地形的敏捷人形 locomotion | arXiv 预印本 cs.RO（B 级） | > 待核实 | 中（q1 命中） | ★★★★☆（稀疏立足点是人形感知式运动的硬场景） |
| [Bracing for Impact](http://arxiv.org/abs/2505.11495v2) [68] | 2025 | 推力恢复 | 统一行走控制与推力恢复，动态行走时用双臂辅助恢复 | arXiv 预印本 cs.RO（B 级） | > 待核实 | 中（q1/q3 命中） | ★★★★☆（把手臂纳入平衡回路，思路有工程价值） |
| [Learning Sim-to-Real Humanoid Locomotion in 15 Minutes](http://arxiv.org/abs/2512.01996v1) [63] | 2025 | 快速 sim2real | 主张把高维人形 sim2real 训练压缩到分钟级 | arXiv 预印本 cs.RO；摘要自述训练时长（B 级） | > 待核实 | 中（q1/q5 重复召回） | ★★★★☆（若可复现将显著降低迭代成本，需第三方验证） |
| [Gait-Adaptive Perceptive Humanoid Locomotion](http://arxiv.org/abs/2512.07464v1) [43] | 2025 | 感知式地形 | 实时足下地形重建 + 步态时序自适应，面向长楼梯等复杂地形 | arXiv 预印本 cs.RO（B 级） | > 待核实 | 中（q6 命中） | ★★★★☆（明确指出步态时序不适配是失败主因，问题定位清晰） |
| [MARG](https://arxiv.org/abs/2509.20036) [72] | 2025 | 间隙地形 | 结合高程图的腿足危险间隙地形穿越 | IEEE Transactions on Robotics（A 级，疑似已录用） | citations=14 | 中（citations=14） | ★★★★☆（本次证据集中唯一有引用数且为期刊者，证据等级最高） |
| [Global-Local Attention Decomposition for Terrain Encoding](http://arxiv.org/abs/2606.00637v3) [44] | 2026 | 地形编码 | 把"广域地形感知"与"精确落脚选择"两种感知角色解耦 | arXiv 预印本 cs.RO（B 级） | > 待核实 | 中（q6 命中） | ★★★★☆（对感知式运动的结构性归因，可迁移到四足） |
| [TWIST](http://arxiv.org/abs/2505.02833v1) [90] | 2025 | 全身遥操作 | 全身模仿式遥操作，覆盖全部自由度 | arXiv 预印本 cs.RO（B 级） | > 待核实 | 中（q2 命中） | ★★★★★（人形全身遥操作关键工作，与动作先验强相关） |
| [CLOT](http://arxiv.org/abs/2602.15060v2) [95] | 2026 | 全局运动跟踪 | 闭环全局运动跟踪，缓解全尺寸人形长时序全局位姿漂移 | arXiv 预印本 cs.RO（B 级） | > 待核实 | 中（q2 命中） | ★★★★☆（指出"局部坐标系"是长时序失败的根因） |
| [Humanoid Manipulation Interface](http://arxiv.org/abs/2602.06643v2) [11] | 2026 | 无机器人演示 | 从"无机器人"的人类演示学习人形全身操作，绕开遥操作硬件 | arXiv 预印本 cs.RO（B 级） | > 待核实 | 中（q2/q3/q5 重复召回） | ★★★★☆（降低数据采集的硬件门槛，方向性强） |
| [Locomotion Beyond Feet](http://arxiv.org/abs/2601.03607v1) [12] | 2026 | 多接触全身运动 | 引入手、膝、肘等额外接触点的全身移动系统 | arXiv 预印本 cs.RO（B 级） | > 待核实 | 中（q3/q4/q6 重复召回） | ★★★★☆（拓展"移动"定义，接触丰富控制的代表） |
| [Humanoid Whole-Body Badminton](http://arxiv.org/abs/2511.11218v4) [7] | 2025 | 动态物体交互 | 退火式 RL 课程训练统一全身控制器打羽毛球 | arXiv 预印本 cs.RO（B 级） | > 待核实 | 中（q2/q3 重复召回） | ★★★★☆（高速动态交互，验证全身控制上限） |
| [Hierarchical Reduced-Order MPC](http://arxiv.org/abs/2509.04722v1) [64] | 2025 | 模型式控制 | 基于降阶模型的分层高效 MPC 人形行走框架 | arXiv 预印本 cs.RO（B 级） | > 待核实 | 中（q1 命中） | ★★★★☆（学习式之外的强基线，选型必看） |
| [CART](http://arxiv.org/abs/2604.14344v2) [33] | 2026 | 地形适配 | 用时序序列选择做上下文感知地形适配 | arXiv 预印本 cs.RO（B 级） | > 待核实 | 中（q6 命中） | ★★★☆☆（思路清晰，但需真机证据） |
| [Towards Miniature Humanoid Tele-Loco-Manipulation](http://arxiv.org/abs/2607.20399v1) [65] | 2026 | 遥操作 + RL | VR 上半身遥操作 + RL 下半身平衡的微型人形系统 | arXiv 预印本 cs.RO（B 级） | > 待核实 | 中（q1/q5 重复召回） | ★★★☆☆（小型化平台，成本友好但性能上限待验证） |
| [S-Cheetah](http://arxiv.org/abs/2605.27909v1) [18] | 2026 | 硬件 + 学习 | 3 自由度主动脊柱四足平台与敏捷运动学习 | arXiv 预印本 cs.RO（B 级） | > 待核实 | 中（q3 命中） | ★★★☆☆（说明"形态-学习协同设计"分支仍活跃） |

**时间线判读**：2024 年以"人形挑战地形 + parkour"为主（[42][66]）；2025 年集中在稀疏落脚点、感知式步态自适应、快速 sim2real 与全身遥操作（[67][43][63][90]）；2026 年则明显向 **全身多接触、全局运动跟踪、无机器人演示学习** 迁移（[12][95][11][44]）。以上年份均取自各条目的 arXiv 标识与证据集标注，未做第三方录用状态核实 `> 待核实`。

---

## 二、学习式 locomotion 与全身控制

### 2.1 全身控制器（Whole-Body Controller, WBC）的学习化路线

| 条目 | 时间 | 核心贡献 | 权威 | 热度 | 关注度 | 推荐度 |
|---|---|---|---|---|---|---|
| [HOVER](http://arxiv.org/abs/2410.21229v2) [92] | 2024 | 面向人形的通用神经全身控制器，统一多种运动模式 | arXiv 预印本 cs.RO（B 级） | > 待核实 | 中（q2 命中） | ★★★★★（神经 WBC 的枢纽型工作） |
| [OmniH2O](http://arxiv.org/abs/2406.08858v1) [93] | 2024 | 通用灵巧人-人

## 参考来源

[1] Learning Robust, Agile, Natural Legged Locomotion Skills in the Wild — http://arxiv.org/abs/2304.10888v3
[2] ATRos: Learning Energy-Efficient Agile Locomotion for Wheeled-legged Robots — http://arxiv.org/abs/2510.09980v1
[3] Legged Robots that Keep on Learning: Fine-Tuning Locomotion Policies in the Real World — http://arxiv.org/abs/2110.05457v1
[4] HyperCLOVA X Technical Report — http://arxiv.org/abs/2404.01954v2
[5] Whole-Body Geometric Retargeting for Humanoid Robots — http://arxiv.org/abs/1909.10080v1
[6] The Role of Domain Randomization in Training Diffusion Policies for Whole-Body Humanoid Control — http://arxiv.org/abs/2411.01349v1
[7] Humanoid Whole-Body Badminton via an Annealed Reinforcement Learning Curriculum — http://arxiv.org/abs/2511.11218v4
[8] Tailoring Solution Accuracy for Fast Whole-body Model Predictive Control of Legged Robots — http://arxiv.org/abs/2407.10789v2
[9] The MIT Humanoid Robot: Design, Motion Planning, and Control For Acrobatic Behaviors — http://arxiv.org/abs/2104.09025v1
[10] Optimization of Humanoid Robot Designs for Human-Robot Ergonomic Payload Lifting — http://arxiv.org/abs/2211.13503v1
[11] Humanoid Manipulation Interface: Humanoid Whole-Body Manipulation from Robot-Free Demonstrations — http://arxiv.org/abs/2602.06643v2
[12] Locomotion Beyond Feet — http://arxiv.org/abs/2601.03607v1
[13] A Robust Version of Convex Integral Functionals — http://arxiv.org/abs/1305.6023v3
[14] Adaptive Blind Sparse-Channel Equalization — http://arxiv.org/abs/1708.01824v1
[15] Convex Integration and Legendrian Approximation of Curves — http://arxiv.org/abs/1507.07661v2
[16] Real-time Optimal Landing Control of the MIT Mini Cheetah — http://arxiv.org/abs/2110.02799v1
[17] Adaptive Locomotion on Mud through Proprioceptive Sensing of Substrate Properties — http://arxiv.org/abs/2504.19607v2
[18] S-Cheetah: A Novel Quadrupedal Robot with a 3-DOF Active Spine Learning Agile Locomotion — http://arxiv.org/abs/2605.27909v1
[19] Learning to Walk in Minutes Using Massively Parallel Deep Reinforcement Learning — http://arxiv.org/abs/2109.11978v3
[20] CHC-COMP 2022: Competition Report — http://arxiv.org/abs/2211.12231v1
[21] Motif Mining and Unsupervised Representation Learning for BirdCLEF 2022 — http://arxiv.org/abs/2206.04805v1
[22] Advanced Skills by Learning Locomotion and Local Navigation End-to-End — http://arxiv.org/abs/2209.12827v1
[23] A Walk in the Park: Learning to Walk in 20 Minutes With Model-Free Reinforcement Learning — http://arxiv.org/abs/2208.07860v1
[24] The Open Ant: A Robot Platform for Reinforcement Learning Research — http://arxiv.org/abs/2607.18488v1
[25] RMA: Rapid Motor Adaptation for Legged Robots — http://arxiv.org/abs/2107.04034v1
[26] This paper has been withdrawn — http://arxiv.org/abs/cond-mat/0309395v2
[27] Adapting Rapid Motor Adaptation for Bipedal Robots — http://arxiv.org/abs/2205.15299v2
[28] Leveraging MPI RMA to optimise halo-swapping communications in MONC on Cray machines — http://arxiv.org/abs/2010.13437v1
[29] Adapting Rapid Motor Adaptation for Bipedal Robots — https://doi.org/10.1109/iros47612.2022.9981091
[30] On Terrain-Aware Locomotion for Legged Robots — http://arxiv.org/abs/2212.00683v1
[31] Adapting Rapid Motor Adaptation for Bipedal Robots — https://doi.org/10.48550/arxiv.2205.15299
[32] Deploying COTS Legged Robot Platforms into a Heterogeneous Robot Team — http://arxiv.org/abs/2106.07182v1
[33] CART: Context-Aware Terrain Adaptation using Temporal Sequence Selection for Legged Robots — http://arxiv.org/abs/2604.14344v2
[34] TOP-Nav: Legged Navigation Integrating Terrain, Obstacle and Proprioception Estimation — http://arxiv.org/abs/2404.15256v4
[35] Terrain Classification for the Spot Quadrupedal Mobile Robot Using Only Proprioceptive Sensing — http://arxiv.org/abs/2508.16504v1
[36] Proprioceptive State Estimation of Legged Robots with Kinematic Chain Modeling — http://arxiv.org/abs/2209.05644v3
[37] Bridging the Sim2Real Gap: Vision Encoder Pre-Training for Visuomotor Policy Transfer — http://arxiv.org/abs/2501.16389v2
[38] The Importance and the Limitations of Sim2Real for Robotic Manipulation in Precision Agriculture — http://arxiv.org/abs/2008.03983v1
[39] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1
[40] NTIRE 2025 Challenge on Image Super-Resolution (x4): Methods and Results — http://arxiv.org/abs/2504.14582v3
[41] VLSP 2025 MLQA-TSR Challenge: Vietnamese Multimodal Legal Question Answering on Traffic Sign Regulation — http://arxiv.org/abs/2510.20381v1
[42] Learning Humanoid Locomotion over Challenging Terrain — http://arxiv.org/abs/2410.03654v1
[43] Gait-Adaptive Perceptive Humanoid Locomotion with Real-Time Under-Base Terrain Reconstruction — http://arxiv.org/abs/2512.07464v1
[44] Global-Local Attention Decomposition for Terrain Encoding in Humanoid Perceptive Locomotion — http://arxiv.org/abs/2606.00637v3
[45] The Electronics of the H1 Lead/Scintillating-Fibre Calorimeters — http://arxiv.org/abs/physics/9812042v1
[46] Measurement of the Charm and Beauty Structure Functions using the H1 Vertex Detector at HERA — http://arxiv.org/abs/0907.2643v2
[47] Measurement of F_2^ccbar and F_2^bbbar at High Q^2 using the H1 Vertex Detector at HERA — http://arxiv.org/abs/hep-ex/0411046v1
[48] Measurement of Beauty Photoproduction near Threshold using Di-electron Events with the H1 Detector at HERA — http://arxiv.org/abs/1206.4346v1
[49] A Purity Monitoring System for the H1 Liquid Argon Calorimeter — http://arxiv.org/abs/hep-ex/0111066v1
[50] Measurement of Charm and Beauty Dijet Cross Sections in Photoproduction at HERA using the H1 Vertex Detector — http://arxiv.org/abs/hep-ex/0605016v1
[51] Measurement of F_2^{c\bar{c}} and F_2^{b\bar{b}} at Low Q^2 and x using the H1 Vertex Detector at HERA — http://arxiv.org/abs/hep-ex/0507081v1
[52] One-Shot Reinforcement Learning for Robot Navigation with Interactive Replay — http://arxiv.org/abs/1711.10137v2
[53] Value Bonuses using Ensemble Errors for Exploration in Reinforcement Learning — http://arxiv.org/abs/2602.12375v1
[54] Isaac Lab: A GPU-Accelerated Simulation Framework for Multi-Modal Robot Learning — http://arxiv.org/abs/2511.04831v1
[55] Causal-Paced Deep Reinforcement Learning — http://arxiv.org/abs/2507.02910v1
[56] Isaac Gym: High Performance GPU-Based Physics Simulation For Robot Learning — http://arxiv.org/abs/2108.10470v2
[57] Robot Trains Robot: Automatic Real-World Policy Adaptation and Learning for Humanoids — http://arxiv.org/abs/2508.12252v2
[58] Wheeled Lab: Modern Sim2Real for Low-cost, Open-source Wheeled Robotics — http://arxiv.org/abs/2502.07380v2
[59] CHILD (Controller for Humanoid Imitation and Live Demonstration): a Whole-Body Humanoid Teleoperation System — http://arxiv.org/abs/2508.00162v2
[60] A ROS-based Software Framework for the NimbRo-OP Humanoid Open Platform — http://arxiv.org/abs/1809.11051v1
[61] Humanoid Whole-Body Manipulation via Active Spatial Brain and Generalizable Action Cerebellum — http://arxiv.org/abs/2605.21133v2
[62] NimbRo-OP2: Grown-up 3D Printed Open Humanoid Platform for Research — http://arxiv.org/abs/1809.11144v1
[63] Learning Sim-to-Real Humanoid Locomotion in 15 Minutes — http://arxiv.org/abs/2512.01996v1
[64] Hierarchical Reduced-Order Model Predictive Control for Robust Locomotion on Humanoid Robots — http://arxiv.org/abs/2509.04722v1
[65] Towards Miniature Humanoid Tele-Loco-Manipulation Using Virtual Reality and Reinforcement Learning — http://arxiv.org/abs/2607.20399v1
[66] Humanoid Parkour Learning — http://arxiv.org/abs/2406.10759v2
[67] BeamDojo: Learning Agile Humanoid Locomotion on Sparse Footholds — http://arxiv.org/abs/2502.10363v3
[68] Bracing for Impact: Robust Humanoid Push Recovery and Locomotion with Reduced Order Models — http://arxiv.org/abs/2505.11495v2
[69] Mastering Agile Jumping Skills from Simple Practices with Iterative Learning Control — http://arxiv.org/abs/2408.02619v1
[70] Sim-to-Real Transfer in Deep Reinforcement Learning for Bipedal Locomotion — http://arxiv.org/abs/2511.06465v1
[71] Grasp and Motion Planning for Dexterous Manipulation for the Real Robot Challenge — http://arxiv.org/abs/2101.02842v1
[72] MARG: MAstering Risky Gap Terrains for Legged Robots With Elevation Mapping — https://arxiv.org/abs/2509.20036
[73] Unsupervised Skill Discovery as Exploration for Learning Agile Locomotion — https://arxiv.org/abs/2508.08982
[74] Impedance Matching: Enabling an RL-Based Running Jump in a Quadruped Robot — https://arxiv.org/abs/2404.15096
[75] Real-World Humanoid Locomotion with Reinforcement Learning — http://arxiv.org/abs/2303.03381v2
[76] State Estimation Transformers for Agile Legged Locomotion — https://arxiv.org/abs/2410.13496
[77] Squat and tuck jump maneuver for single-legged robot with an active toe joint using model-free deep reinforcement learning — https://doi.org/10.1007/s40430-024-05028-0
[78] Continuous Jumping for Legged Robots on Stepping Stones via Trajectory Optimization and Model Predictive Control — https://arxiv.org/abs/2204.01147
[79] Cat-Like Jumping and Landing of Legged Robots in Low Gravity Using Deep Reinforcement Learning — https://arxiv.org/abs/2106.09357
[80] HumanoidBench: Simulated Humanoid Benchmark for Whole-Body Locomotion and Manipulation — http://arxiv.org/abs/2403.10506v2
[81] Humanoid Agent via Embodied Chain-of-Action Reasoning with Multimodal Foundation Models for Zero-Shot Loco-Manipulation — http://arxiv.org/abs/2504.09532v3
[82] MuJoCo Playground — http://arxiv.org/abs/2502.08844v1
[83] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1
[84] Generating a Terrain-Robustness Benchmark for Legged Locomotion: A Prototype via Terrain Authoring and Active Learning — http://arxiv.org/abs/2208.07681v3
[85] Sim2Real Transfer for Audio-Visual Navigation with Frequency-Adaptive Acoustic Field Prediction — http://arxiv.org/abs/2405.02821v2
[86] A Human-Grounded Evaluation Benchmark for Local Explanations of Machine Learning — http://arxiv.org/abs/1801.05075v2
[87] Dense Temporal Motion Retargeting for Legged Robots — http://arxiv.org/abs/2609.38617v1
[88] Spatio-Temporal Motion Retargeting for Quadruped Robots — http://arxiv.org/abs/2404.11557v3
[89] Retargeting Matters: General Motion Retargeting for Humanoid Motion Tracking — http://arxiv.org/abs/2510.02252v1
[90] TWIST: Teleoperated Whole-Body Imitation System — http://arxiv.org/abs/2505.02833v1
[91] Learning Human-to-Humanoid Real-Time Whole-Body Teleoperation — http://arxiv.org/abs/2403.04436v1
[92] HOVER: Versatile Neural Whole-Body Controller for Humanoid Robots — http://arxiv.org/abs/2410.21229v2
[93] OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning — http://arxiv.org/abs/2406.08858v1
[94] Dynamic Locomotion Teleoperation of a Wheeled Humanoid Robot Reduced Model with a Whole-Body Human-Machine Interface — http://arxiv.org/abs/2109.03906v1
[95] CLOT: Closed-Loop Global Motion Tracking for Whole-Body Humanoid Teleoperation — http://arxiv.org/abs/2602.15060v2
[96] The AudioMOS Challenge 2025 — http://arxiv.org/abs/2509.01336v1
[97] TDCOSMO 2025: Cosmological constraints from strong lensing time delays — http://arxiv.org/abs/2506.03023v4
[98] TRUST 2025: SCRITA and RTSS @ RO-MAN 2025 — http://arxiv.org/abs/2509.11402v1
[99] Event-Enriched Image Analysis Grand Challenge at ACM Multimedia 2025 — http://arxiv.org/abs/2508.18904v1
[100] weijian/2026-USCAP-AI-Pathology-Report: 2026-USCAP-AI-Pathology-Report把脉:学术发现→产业映射——2026年USCAP年会新兴技术与AI整合报告(完整版) — https://doi.org/10.5281/zenodo.20241691
[101] weijian/2026-USCAP-AI-Pathology-Report: 2026-USCAP-AI-Pathology-Report把脉:学术发现→产业映射——2026年USCAP年会新兴技术与AI整合报告(完整版) — https://doi.org/10.5281/zenodo.20241601


---

*Generated by research-bot · topic=`embodied-humanoid` · depth=`standard` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading · model=`deepseek-v4-flash` · sources=101 · duration=421s · 2026-10-02T22:29:22+00:00*
