# 机器人运动学、动力学与控制：2024–2026 前沿进展与工程实践调研报告

**日期**：2026-10-02（UTC） ｜ **领域**：Robotics Kinematics, Dynamics & Control（FK/IK、旋量/PoE、雅可比与可操作度、轨迹优化、全身/操作空间控制、数值库） ｜ **检索源**：101 条候选证据条目 [1]–[101] + 10 条领域种子资源（4 篇经典论文、5 个开源项目、1 个数据集） ｜ **证据分级**：A（同行评审）/ B（预印本、官方仓库）/ C（第三方复现、榜单）/ D（二手解读）/ E（不可用）

---

## 摘要（Executive Summary）

**本次检索的证据覆盖严重不均衡，必须先把缺口说清楚，再谈结论。**

1. **候选集中约三分之二为领域外噪声。** 101 条候选中，与机器人运动学/动力学/控制**完全无关**的条目包括：粒子物理与中微子实验 [73][74][75][76][77][79][80]、天体物理与宇宙学 [23][40][45][56][57][59]、纯数学（Lie 群逼近性、Leibniz 代数、子因子）[83][84][85][87][88][96]、图像/视频/音频挑战赛 [17][18][20][21][27][28][29][37][72][89]。这类条目在 q2（旋量理论原始出处）中占比最高，导致该子问题**事实上未被回答**。

2. **三处系统性证据缺口**：(a) **q1（FK/IK、可微分运动学、学习式 IK 的最新进展）**——6 条候选 [17][19][23][24][25][70] 中命中 IK/FK 关键词的条数为 **0/6**，检索级别的失败而非结论级别的失败；(b) **q2（旋量/PoE 奠基性工作的原始出处与标准表述）**——候选被高能物理与纯数学文献占据；(c) **q5（Pinocchio/Drake/RBDL/KDL/cuRobo/OCS2/CasADi/JAX/MuJoCo MJX 的能力边界、许可证、活跃度）**——候选块中**不含任何一份官方文档、README 或排行榜数据**，因此本报告对该子问题**只能给出定性框架，不能给出许可证/性能/活跃度结论**。

3. **可确认的实质进展集中在三处**（详见第一章）：
   - **人形全身控制/全身操作**成为 2024–2026 最密集的方向，候选集内即有 [1][2][3][4][5][6][8][33][39][70] 共 10 条，覆盖 RL 课程、遥操作、扩散策略、分层世界模型等路线；但**全部为 arXiv 预印本（B 级）**，无一条具备同行评审 venue 信息。
   - **接触隐式轨迹优化的"隐式微分"路线**出现明确的方法谱系划分（有限差分 / 展开式 AD / 隐式微分）与"摊销 + 残差 MPC"新组合 [99]，但该条为 **v1 预印本且仅有摘要**，无代码、无实验数字。
   - **可操作度的鲁棒性重估**：从经典可操作度椭球转向**伪椭球（pseudo-ellipsoid）**以提升评估鲁棒性 [95]，并伴随"可操作度学习/迁移"这一条 2018–2024 的连续线索 [92][93]。

4. **最关键的负面结论（本报告最重要的产出）**：**本次候选证据不支持"学习式/可微分 IK 相比 Newton、DLS、TRAC-IK 在精度、实时性或多解处理上取得了可归因改进"这一论断，也不支持任何关于开源库性能/许可证的可核查比较。** 相关判断一律标注 `> 待核实`，并列入第八节开放问题。

5. **使用建议**：本报告可用于（a）确定研究缺口与补检方向；（b）获取一份经过证据分级的经典与种子资源清单（第六、七章表格）；（c）避免把"人形全身控制的热度"误读为"运动学求解器已有共识性突破"。**不可**用于支撑求解器选型、许可证合规或 SOTA 性能声明。

---

## 一、关键前沿进展

> **时间口径**：本节"最新进展"= 2024-10 至 2026-10 期间首次公开的条目；更早的条目归入"经典/脉络"。

### 1.1 热点一：人形全身控制与全身操作（2024–2026）

候选集中最密集的簇，全部为 arXiv 预印本（证据等级 B），且**候选块均未提供引用数、GitHub star 或榜单排名**，因此热度证据一律 `> 待核实`。

| 名称 | 年份 | 机构/作者 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 链接 |
|---|---|---|---|---|---|---|---|
| Humanoid Whole-Body Badminton via an Annealed Reinforcement Learning Curriculum [1] | 2025（v4） | 未在候选块给出，`> 待核实` | `> 待核实`（无引用数） | arXiv 预印本（cs.RO），未见同行评审 | 中 + 依据：以"动态高速物体交互"为人形全身控制的少数尝试，属 RL 课程学习路线 | ★★★☆☆ 人形全身 RL 的代表性入口，但无同行评审与开源信号 | http://arxiv.org/abs/2511.11218v4 |
| CHILD: Controller for Humanoid Imitation and Live Demonstration [3] | 2025（v2） | `> 待核实` | `> 待核实` | arXiv 预印本（cs.RO） | 中 + 依据：明确指出"现有工作很少支持人形**关节级全身遥操作**"这一空白 | ★★★☆☆ 若研究关节级全身遥操作映射，该条为直接相关的现状陈述 | http://arxiv.org/abs/2508.00162v2 |
| Humanoid Manipulation Interface: Humanoid Whole-Body Manipulation from Robot-Free Demonstrations [4] | 2026（v2） | `> 待核实` | `> 待核实` | arXiv 预印本（cs.RO） | 中 + 依据：指向"无机器人本体演示（robot-free demonstration）"这一降低硬件门槛的路线 | ★★★★☆ 若关注演示数据采集成本，该路线值得优先精读 | http://arxiv.org/abs/2602.06643v2 |
| Humanoid Whole-Body Manipulation via Active Spatial Brain and Generalizable Action Cerebellum [5] | 2026（v2） | `> 待核实` | `> 待核实` | arXiv 预印本（cs.RO） | 中 + 依据：明确点出**空间理解**与**动作泛化**两大挑战，是全文中最清晰的"问题定义"式摘要之一 | ★★★☆☆ 双系统（brain/cerebellum）思路可对照 VLA 架构讨论 | http://arxiv.org/abs/2605.21133v2 |
| Hierarchical World Models as Visual Whole-Body Humanoid Controllers [8] | 2024（v3） | `> 待核实` | `> 待核实` | arXiv 预印本（cs.RO） | 中 + 依据：以"分层世界模型"作为视觉全身控制器，与 RL 端到端路线形成方法对照 | ★★★☆☆ 世界模型 × 全身控制的交叉点，适合做方法论对比 | http://arxiv.org/abs/2405.18418v3 |
| Learning Humanoid Standing-up Control across Diverse Postures [6] | 2025（v2） | `> 待核实` | `> 待核实` | arXiv 预印本（cs.RO） | 低 + 依据：单任务（起身）泛化，范围窄于全身操作 | ★★☆☆☆ 仅在需要起身/恢复行为时参考 | http://arxiv.org/abs/2502.08378v2 |
| The Role of Domain Randomization in Training Diffusion Policies for Whole-Body Humanoid Control [2] | 2024（v1） | `> 待核实` | `> 待核实` | arXiv 预印本（cs.RO） | 中 + 依据：把 domain randomization 作为**自变量**研究而非技巧性堆叠，归因意识较强 | ★★★☆☆ 对"提升来自数据还是架构"这一四问之一有直接帮助 | http://arxiv.org/abs/2411.01349v1 |
| Kinematics-Aware Diffusion Policy with Consistent 3D Observation and Action Space [33] | 2025（v1） | `> 待核实` | `> 待核实` | arXiv 预印本（cs.RO） | 中 + 依据：明确指出"只考虑末端位姿不足够"，需**全臂运动学感知**——与本章主题相关性高 | ★★★★☆ 是候选集中少数把"运动学结构"显式注入策略学习的条目 | http://arxiv.org/abs/2512.17568v1 |
| Whole-Body Geometric Retargeting for Humanoid Robots [39] | 2019（v1） | `> 待核实` | `> 待核实` | arXiv 预印本（cs.RO） | 低–中 + 依据：时间较早，属"全身几何重定向"这一子线的早期工作 | ★★★☆☆ 若做全身遥操作映射，此条是应当引用的前作 | http://arxiv.org/abs/1909.10080v1 |
| Robot Trains Robot: Automatic Real-World Policy Adaptation and Learning for Humanoids [70] | 2025（v2） | `> 待核实` | `> 待核实` | arXiv 预印本（cs.RO） | 中 + 依据：摘要明确指出现有真机 RL 受限于**安全性、奖励设计、学习效率**，问题陈述具体 | ★★★☆☆ 作为"仿真→真机"落地瓶颈的一手问题陈述有效 | http://arxiv.org/abs/2508.12252v2 |

**这一簇的归因评估（按 frontier-tracking 四问）**：
- **多任务/多本体验证**：候选块仅提供摘要，无法判断任务数与本体数 → `> 待核实`。
- **开源情况**：候选块**无任何代码/权重链接** → `> 待核实`（这是本报告最强的缺口之一）。
- **提升归因（数据/架构/算力）**：仅 [2] 显式把 domain randomization 当作研究对象；其余无法归因。
- **独立第三方评测**：候选集内**无任何榜单或复现报告** → `> 待核实`。

> **谨慎声明**：以上 10 条**全部**为 arXiv 预印本，候选块未标注任何会议/期刊 acceptance 信息。任何"该方向已达 SOTA"的表述在本证据集下均不成立。

### 1.2 热点二：接触隐式轨迹优化的隐式微分路线（2026）

候选集中**唯一**直接讨论 contact-implicit trajectory optimization 方法谱系的条目是 [99]：

- **方法谱系（由 [99] 摘要转述）**：现有路线分为三类——(a) 有限差分（expensive and step-size sensitive）；(b) 对迭代接触求解器做自动微分展开（unrolling AD，需存储不断增长的计算图）；(c) 隐式微分（implicit differentiation，但需繁琐的、与求解器强绑定的推导）[99]。
- **新组合**：将 trajectory optimisation 的 **amortisation（摊销）** 与 **residual MPC（残差 MPC）** 结合，用隐式接触微分提供梯度 [99]。
- **交叉验证状态**：仅 **1 条候选**命中该主题，且为 **v1 预印本（arXiv:2607.24959v1，2026-07-27）**，无引用数、无代码链接、无第三方复现 [99]。按证据分级方法论，方法谱系划分这一"分类性结论"**不应仅凭单篇摘要采信**，标注为 **待核实**。
- **求解释义**：`> 待核实`——[99] 摘要未给出成功率、求解时间或数值鲁棒性的任何数字。

### 1.3 热点三：GPU 加速运动规划（2025）

- **Industrial Robot Motion Planning with GPUs: Integration of cuRobo for Extended DOF Systems [54]**（2025-08，v2）：将 NVIDIA cuRobo 集成到 Vention 的模块化自动化平台，面向**多轴/扩展自由度**工业系统 [54]。这是候选集中唯一涉及 cuRobo 的条目，也是第七章"工程实践"中仅有的一手工程证据。
  - 热度：`> 待核实` ｜ 权威：arXiv 预印本（cs.RO），未见同行评审 [54] ｜ 关注度：中 + 依据：GPU 加速规划在工业落地方向的少数具名集成案例 ｜ 推荐度：**★★★★☆** + 理由：是候选集中最接近"库在真实工业系统中的能力边界"的一手材料。

### 1.4 热点四：可操作度评估的鲁棒性重估（2024–2025）

- **Enhancing Robustness in Manipulability Assessment: The Pseudo-Ellipsoid Approach [95]**（2024-12，v2）：针对经典可操作度椭球评估的脆弱性提出伪椭球方法。热度 `> 待核实`；权威：arXiv 预印本（cs.RO）；关注度：低–中（该子线社区规模小）；推荐度 **★★★☆☆**（若做可操作度指标选型，值得读）。
- 前序脉络：**Geometry-aware Manipulability Learning, Tracking and Transfer [92]**（2018-11，v5）与 **Analysis and Transfer of Human Movement Manipulability in Industry-like Activities [93]**（2020-08，v2），把可操作度从"瞬时椭球"扩展到"学习 + 迁移"；**Direct ellipsoidal fitting of discrete multi-dimensional data [94]**（2019-01）提供拟合工具。三者共同构成"可操作度椭球 → 学习/迁移 → 鲁棒评估"的演进链 [92][93][94][95]。
- **经典可操作度椭球理论（Yoshikawa 等）的原始出处未出现在候选集中**，`> 待核实`；本报告不引用其具体文献编号。

### 1.5 脉络小结（最新 vs 经典的分野）

| 类别 | 本报告处理方式 | 代表条目 |
|---|---|---|
| 最新进展（2024-10 之后） | 单列于 1.1–1.4 | [1][2][3][4][5][6][33][54][70][95][99] |
| 次新/脉络（2019–2024） | 作为演进链条引用 | [8][26][36][39][65][67][68][86][92][93][94] |
| 经典/奠基（≤2018 及种子资源） | 第六章表格，标注"经典" | 种子资源：Murray-Li-Sastry (1994)、Lynch-Park (2017)、Khatib (1987)、Crocoddyl (2020) |

---

## 二、建模表示：DH 参数化 vs 旋量理论 / 指数积（PoE）

> **先说结论：本子问题的证据链在本轮检索中未建立起来。** q2 的 6 条候选 [81][82][83][84][73][74] 中，[73][74] 为 BESIII 高能物理实验测量、[83][84] 为纯数学（Lie 群逼近性、Leibniz 代数），只有 [81][82][86] 与"机器人旋量/Lie 群"名义相关。因此**无法从候选集确认旋量理论与 PoE 的原始出处与标准表述**。

### 2.1 候选集中确实相关的条目

| 名称 | 年份 | 机构/作者 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 链接 |
|---|---|---|---|---|---|---|---|
| Screw and Lie Group Theory in Multibody Kinematics — Motion Representation and Recursive Kinematics of Tree-Topology Systems [86] | 2023（v1） | `> 待核实` | `> 待核实` | arXiv 预印本

## 参考来源

[1] Humanoid Whole-Body Badminton via an Annealed Reinforcement Learning Curriculum — http://arxiv.org/abs/2511.11218v4
[2] The Role of Domain Randomization in Training Diffusion Policies for Whole-Body Humanoid Control — http://arxiv.org/abs/2411.01349v1
[3] CHILD (Controller for Humanoid Imitation and Live Demonstration): a Whole-Body Humanoid Teleoperation System — http://arxiv.org/abs/2508.00162v2
[4] Humanoid Manipulation Interface: Humanoid Whole-Body Manipulation from Robot-Free Demonstrations — http://arxiv.org/abs/2602.06643v2
[5] Humanoid Whole-Body Manipulation via Active Spatial Brain and Generalizable Action Cerebellum — http://arxiv.org/abs/2605.21133v2
[6] Learning Humanoid Standing-up Control across Diverse Postures — http://arxiv.org/abs/2502.08378v2
[7] A ROS-based Software Framework for the NimbRo-OP Humanoid Open Platform — http://arxiv.org/abs/1809.11051v1
[8] Hierarchical World Models as Visual Whole-Body Humanoid Controllers — http://arxiv.org/abs/2405.18418v3
[9] Task-Priority Control of Redundant Robotic Systems using Control Lyapunov and Control Barrier Function based Quadratic Programs — http://arxiv.org/abs/2001.07547v2
[10] Control of a Rigid Wing Pumping Airborne Wind Energy System in all Operational Phases — http://arxiv.org/abs/2006.11141v1
[11] State-dependent Priority Scheduling for Networked Control Systems — http://arxiv.org/abs/1703.08311v1
[12] On Controller Design for Systems on Manifolds in Euclidean Space — http://arxiv.org/abs/1807.03475v1
[13] Analysis and design of model predictive control frameworks for dynamic operation -- An overview — http://arxiv.org/abs/2307.03004v2
[14] The importance of ensemble techniques for operational space weather forecasting — http://arxiv.org/abs/1806.09861v1
[15] Cold-Tip Temperature Control of Space-borne SatelliteStirlingCryocooler: Mathematical Modeling and Control Investigation — http://arxiv.org/abs/1905.11247v1
[16] Verification of Space Weather Forecasts issued by the Met Office Space Weather Operations Centre — http://arxiv.org/abs/1804.02985v1
[17] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1
[18] NTIRE 2025 Challenge on Image Super-Resolution (x4): Methods and Results — http://arxiv.org/abs/2504.14582v3
[19] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1
[20] VLSP 2025 MLQA-TSR Challenge: Vietnamese Multimodal Legal Question Answering on Traffic Sign Regulation — http://arxiv.org/abs/2510.20381v1
[21] The AudioMOS Challenge 2025 — http://arxiv.org/abs/2509.01336v1
[22] PDHCG-II: An Enhanced Version of PDHCG for Large-Scale Convex QP — http://arxiv.org/abs/2602.23967v1
[23] TDCOSMO 2025: Cosmological constraints from strong lensing time delays — http://arxiv.org/abs/2506.03023v4
[24] TRUST 2025: SCRITA and RTSS @ RO-MAN 2025 — http://arxiv.org/abs/2509.11402v1
[25] Robot Policy Evaluation for Sim-to-Real Transfer: A Benchmarking Perspective — http://arxiv.org/abs/2508.11117v1
[26] IK-Geo: Unified Robot Inverse Kinematics Using Subproblem Decomposition — http://arxiv.org/abs/2211.05737v3
[27] AIM 2025 Low-light RAW Video Denoising Challenge: Dataset, Methods and Results — http://arxiv.org/abs/2508.16830v1
[28] Overview of the Sensemaking Task at the ELOQUENT 2025 Lab: LLMs as Teachers, Students and Evaluators — http://arxiv.org/abs/2507.12143v1
[29] LongEval at CLEF 2025: Longitudinal Evaluation of IR Model Performance — http://arxiv.org/abs/2503.08541v1
[30] LLM-based ambiguity detection in natural language instructions for collaborative surgical robots — http://arxiv.org/abs/2507.11525v1
[31] Kinematic analysis of a parallel robot for minimally invasive surgery — http://arxiv.org/abs/2406.02047v1
[32] Triplets of Galaxies in the Local Supercluster. I. Kinematic and Virial Parameters — http://arxiv.org/abs/astro-ph/0609622v1
[33] Kinematics-Aware Diffusion Policy with Consistent 3D Observation and Action Space for Whole-Arm Robotic Manipulation — http://arxiv.org/abs/2512.17568v1
[34] Compensation of compliance errors in parallel manipulators composed of non-perfect kinematic chains — http://arxiv.org/abs/1204.1757v1
[35] Kinematic analysis of the 3-RPR parallel manipulator — http://arxiv.org/abs/0708.3920v1
[36] Analytically Informed Inverse Kinematics Solution at Singularities — http://arxiv.org/abs/2412.20409v1
[37] Beyond the Ground Truth: Enhanced Supervision for Image Restoration — http://arxiv.org/abs/2512.03932v3
[38] The RSNA Abdominal Traumatic Injury CT (RATIC) Dataset — http://arxiv.org/abs/2405.19595v1
[39] Whole-Body Geometric Retargeting for Humanoid Robots — http://arxiv.org/abs/1909.10080v1
[40] PINOCCHIO and the hierarchical build-up of dark matter haloes — http://arxiv.org/abs/astro-ph/0109324v1
[41] Developing a 21st Century Global Library for Mathematics Research — http://arxiv.org/abs/1404.1905v1
[42] Inversion of the star transform — http://arxiv.org/abs/1401.7655v2
[43] Inversion formulas for the broken-ray Radon transform — http://arxiv.org/abs/1007.4183v1
[44] Inverse spectral problems for Sturm-Liouville operators with singular potentials — http://arxiv.org/abs/math/0211247v1
[45] PINOCCHIO: pinpointing orbit-crossing collapsed hierarchical objects in a linear density field — http://arxiv.org/abs/astro-ph/0109323v2
[46] Inverse Problems in Magnetohydrodynamics: Theoretical and Experimental Aspects — http://arxiv.org/abs/physics/0312093v1
[47] The Relativistic Elasticity of Rigid Bodies — http://arxiv.org/abs/physics/0307019v3
[48] Phase topology of one integrable case of the rigid body motion — http://arxiv.org/abs/1408.6028v1
[49] On the invariant motions of rigid body rotation over the fixed point, via Euler angles — http://arxiv.org/abs/1601.04526v1
[50] A Parametric and Feasibility Study for Data Sampling of the Dynamic Mode Decomposition--Range, Resolution, and Universal Convergence States — http://arxiv.org/abs/2110.06573v2
[51] Some multidimensional integrable cases of nonholonomic rigid body dynamics — http://arxiv.org/abs/math-ph/0304012v1
[52] A note on convergence of solutions of total variation regularized linear inverse problems — http://arxiv.org/abs/1711.06495v3
[53] Inverse Laplace Transform for Bi-Complex Variables — http://arxiv.org/abs/1403.3313v1
[54] Industrial Robot Motion Planning with GPUs: Integration of cuRobo for Extended DOF Systems — http://arxiv.org/abs/2508.04146v2
[55] The enclosure method for inverse obstacle scattering problems with dynamical data over a finite time interval: III. Sound-soft obstacle and bistatic data — http://arxiv.org/abs/1302.2389v1
[56] Area Coverage of Expanding E.T. Signals in the Galaxy: SETI and Drake's N — http://arxiv.org/abs/1802.09399v2
[57] A joint analysis of the Drake equation and the Fermi paradox — http://arxiv.org/abs/1301.6411v2
[58] A Variant of Concurrent Constraint Programming on GPU — http://arxiv.org/abs/2207.12116v1
[59] Transmitting signals over interstellar distances: Three approaches compared in the context of the Drake equation — http://arxiv.org/abs/1303.1100v1
[60] DQ Robotics: a Library for Robot Modeling and Control — http://arxiv.org/abs/1910.11612v3
[61] High-level robot programming based on CAD: dealing with unpredictable environments — http://arxiv.org/abs/1309.2086v1
[62] Exploring Large Language Models to Facilitate Variable Autonomy for Human-Robot Teaming — http://arxiv.org/abs/2312.07214v3
[63] A Simulation and Modeling of Access Points with Definition Language — http://arxiv.org/abs/1304.1836v2
[64] Superconductivity as a consequence of an ordering of the electron gas zero-point oscillations — http://arxiv.org/abs/1005.0280v6
[65] Redundancy parameterization and inverse kinematics of 7-DOF revolute manipulators — http://arxiv.org/abs/2307.13122v2
[66] Grasp and Motion Planning for Dexterous Manipulation for the Real Robot Challenge — http://arxiv.org/abs/2101.02842v1
[67] Real-time Whole-body Obstacle Avoidance for 7-DOF Redundant Manipulators — http://arxiv.org/abs/2012.14578v1
[68] Machine Learning-based Framework for Optimally Solving the Analytical Inverse Kinematics for Redundant Manipulators — http://arxiv.org/abs/2211.04275v3
[69] Backdoors in Learning-Based Industrial Robotic Arm Manipulation: An Empirical Security Study — http://arxiv.org/abs/2609.26868v1
[70] Robot Trains Robot: Automatic Real-World Policy Adaptation and Learning for Humanoids — http://arxiv.org/abs/2508.12252v2
[71] JENGA: Exploiting Counter-Based RowHammer Countermeasures to Break Real-Time Predictability — http://arxiv.org/abs/2609.01077v1
[72] Event-Enriched Image Analysis Grand Challenge at ACM Multimedia 2025 — http://arxiv.org/abs/2508.18904v1
[73] Measurement of inelastic scattering $Λ(\overlineΛ)+p\toΣ^{0}(\overlineΣ^{0})+p$ via $e^+e^-\to J/ψ\toΛ\overlineΛ$ — http://arxiv.org/abs/2609.02584v1
[74] Evidence of $ψ(3770) \to π^{0}J/ψ$ — http://arxiv.org/abs/2606.14105v1
[75] Measurement of the CKM angle $γ$ in $B^{\pm} \rightarrow D(\rightarrow K^{0}_{\rm S} h^{\prime+}h^{\prime-})h^{\pm}$ decays with a novel approach — http://arxiv.org/abs/2604.05701v1
[76] Model Independent Approach of the JUNO $^8$B Solar Neutrino Program — http://arxiv.org/abs/2210.08437v2
[77] Precise measurement of the CKM angle $γ$ with a novel approach — http://arxiv.org/abs/2604.05712v1
[78] Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, Long Context, and Next Generation Agentic Capabilities — http://arxiv.org/abs/2507.06261v6
[79] First measurement of reactor neutrino oscillations at JUNO — http://arxiv.org/abs/2511.14593v1
[80] Initial performance results of the JUNO detector — http://arxiv.org/abs/2511.14590v1
[81] The Geometry and Kinematics of the Matrix Lie Group $SE_K(3)$ — http://arxiv.org/abs/2012.00950v4
[82] Cohomological Equation for Robotic Screw Motion on the Lie Group SE(3) — http://arxiv.org/abs/2601.10734v1
[83] Approximation properties of simple Lie groups made discrete — http://arxiv.org/abs/1408.5238v2
[84] Leibniz algebras, Lie racks, and digroups — http://arxiv.org/abs/math/0403509v5
[85] Local spectral radius formulas on compact Lie groups — http://arxiv.org/abs/0805.3900v2
[86] Screw and Lie Group Theory in Multibody Kinematics -- Motion Representation and Recursive Kinematics of Tree-Topology Systems — http://arxiv.org/abs/2306.17415v1
[87] Curvature of matrix and reductive Lie groups — http://arxiv.org/abs/2108.00651v1
[88] Hom 3-Lie-Rinehart Algebras — http://arxiv.org/abs/2001.07570v2
[89] StyleHumanCLIP: Text-guided Garment Manipulation for StyleGAN-Human — http://arxiv.org/abs/2305.16759v4
[90] Generation of highly pure Schrödinger's cat states and real-time quadrature measurements via optical filtering — http://arxiv.org/abs/1708.04042v2
[91] Non-existence of an invariant measure for a homogeneous ellipsoid rolling on the plane — http://arxiv.org/abs/1306.4237v2
[92] Geometry-aware Manipulability Learning, Tracking and Transfer — http://arxiv.org/abs/1811.11050v5
[93] Analysis and Transfer of Human Movement Manipulability in Industry-like Activities — http://arxiv.org/abs/2008.01402v2
[94] Direct ellipsoidal fitting of discrete multi-dimensional data — http://arxiv.org/abs/1901.05511v3
[95] Enhancing Robustness in Manipulability Assessment: The Pseudo-Ellipsoid Approach — http://arxiv.org/abs/2412.18869v2
[96] Strong Singularity for Subfactors — http://arxiv.org/abs/math/0703673v3
[97] Physics Briefing Book — http://arxiv.org/abs/1910.11775v2
[98] Physics and Technology of the Next Linear Collider: A Report Submitted to Snowmass '96 — http://arxiv.org/abs/hep-ex/9605011v1
[99] Amortising Trajectory Optimisation for Residual MPC via Implicit Contact Differentiation — http://arxiv.org/abs/2607.24959v1
[100] Optimal design of frame structures with mixed categorical and continuous design variables using the Gumbel-Softmax method — http://arxiv.org/abs/2501.00258v1
[101] On the solution existence and stability of polynomial optimization problems — http://arxiv.org/abs/1808.06100v6


---

*Generated by research-bot · topic=`kinematics` · depth=`standard` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading · model=`deepseek-v4-flash` · sources=101 · duration=590s · 2026-10-02T23:08:45+00:00*
