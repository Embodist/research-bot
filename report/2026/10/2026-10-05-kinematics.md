# 机器人运动学、动力学与控制：证据化综述（2024–2026 前沿 + 经典奠基 + 工程栈）

**元信息**：报告日期 2026-10-05（UTC）｜领域：Robotics Kinematics / Dynamics / Control（含 WBC、轨迹优化、数值库与 ROS2 栈）｜检索源：本轮共获 133 条候选来源编号，经逐条核对后**约 50 条与主题相关**（含少量旁证），**约 80 条为明显误召回**（高能物理、天体物理、NLP 共享任务等），详见第八章「证据质量说明」。

> **阅读须知（证据透明度声明）**：本报告的编号引用**仅**来自本次提供的候选来源列表 [1]–[133]。其中子问题 q2（旋量/PoE、操作空间控制、可操作度、DDP/iLQR/TrajOpt 谱系）与 q5（WBC/QP 可行性/sim-to-real/负面结果）的候选证据**几乎全部为误召回**，因此这两条主线的部分内容只能依赖任务给定的**种子资源（seed）**，并明确标注 `> 待核实`。凡本报告未取得一手热度数字（citations / stars / 下载量）之处，一律写 `> 待核实`，**不编造任何数字或榜单排名**。

---

## 摘要（Executive Summary）

1. **2024–2026 运动学与控制的最重要变化，是"几何先验"与"学习策略"的合流**：SE(3) 等变扩散策略 [41][44][42]、运动学感知的全身/全臂扩散策略 [27]，以及用于扩散策略轨迹筛选的核密度估计后处理 [46]，共同把"运动学结构"重新放回学习型策略的中心，而不是把末端位姿当作唯一接口 [27][41]。
2. **接触隐式轨迹优化（CITO）从"早期演示"走向"求解器级工程化与理论收敛性"**：从正交配点法 [35]、四足微型机器人运动轨迹 [34]，到 SQP 全局收敛性分析 [37]，再到 2026 年的隐式 active-set 增广拉格朗日求解器 IMPACT [39]，CITO 已具备"无需预设接触序列"的统一规划-控制形态 [39]。
3. **实时 QP/MPC 求解器成为独立研究赛道**：面向 MPC 的逆矩阵更新快速 QP [123]、具备执行时间认证与不可行检测的 QP 求解器 [122]、大规模凸 QP 的改进版本 [118]，以及面向四足行走的 QP 形式化与求解器基准对比 [119]。注意 [119] 明确指出"QP 形式化 + 求解器选型"本身耗费大量工程时间，这是当前 WBC 落地的真实痛点 [119]。
4. **全身控制（WBC）的主战场已转向人形机器人**：人形全身羽毛球（退火 RL 课程）[47]、全身关节级遥操作 CHILD [103]、免机器人示教的全身操作接口 [105]、主动空间理解 + 可泛化动作小脑 [104]、跨姿态起立控制 [106]，以及域随机化对全身人形扩散策略的作用 [102]。
5. **经典运动学根基仍然稳固但本轮检索未能取得一手证据**：旋量/指数积（PoE）、操作空间控制（Khatib）、可操作度、DDP/iLQR/TrajOpt 谱系在本轮候选中**零命中**，只能引用任务给定种子资源（Murray-Li-Sastry、Lynch & Park、Khatib 1987、Crocoddyl），并标注 `> 待核实`（见第六章）。
6. **工程栈方面可核查的证据集中在 ROS2 侧**：Fanuc CRX 的 `ros2_control` 硬件接口与 MoveIt2 集成 [126]、MoveIt2 多机器人异步轨迹执行 [127]、模块化 robot-agnostic 控制器架构 [129]、ROS2 多节点延迟分析 [130]、跨广域网 ROS2 连接 [128]、云端机器人连通性 FogROS2-SGC [131]、ROS2 运行时监控 [132]、以及用 LLM 辅助理解 ROS2 软件架构 [133]。
7. **重大证据缺口**：本轮检索对 Pinocchio（机器人库）产生严重**同名误召回**——返回的是宇宙学暗物质晕代码 PINOCCHIO [48][49][50][51][52][53] 与一个童话主题 RL 论文 [55]，**不能**作为机器人刚体动力学库 Pinocchio 的证据（见第七章）。
8. **结论**：若要产出可作为选型/立项依据的结论，必须在 q2（经典谱系）与 q5（开放争议）上重做精确检索；本报告对这两章采取"结构化缺口 + 种子资源 + 待核实"的保守写法。

---

## 一、关键前沿进展（近 1–2 年）

### 1.1 几何先验 × 扩散/流式策略（运动学进入策略内部）

| 名称 | 时间 | 机构/作者 | 一句话贡献 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 来源 |
|---|---|---|---|---|---|---|---|---|
| Spherical Diffusion Policy (SDP), SE(3)-Equivariant Diffusion Policy in Spherical Fourier Space | 2025 | `> 待核实` | 在球面傅里叶空间构造 SE(3) 等变扩散策略，缓解物体三维重排下的泛化差问题 | `> 待核实`（无 citations/star 数据） | arXiv 预印本（cs.RO），候选块未显示同行评审 venue | 中：SE(3) 等变 + diffusion policy 属当前热点组合，但缺热度数字支撑 | ★★★★☆：与"运动学结构如何进入策略"高度相关，值得精读 | [41] |
| ET-SEED: Efficient Trajectory-Level SE(3) Equivariant Diffusion Policy | 2024 | `> 待核实` | 轨迹级（而非单步级）SE(3) 等变扩散策略，强调效率 | `> 待核实` | arXiv 预印本（候选块未给 venue） | 中：与 [41] 构成同一直线，标题即表明"轨迹级等变"这一改进方向 | ★★★★☆：与 [41] 对比阅读可看清"等变粒度"这一设计维度 | [44] |
| Leveraging SE(3) Equivariance for Learning 3D Geometric Shape Assembly | 2023 | `> 待核实` | 将 SE(3) 等变用于 3D 几何形状装配学习 | `> 待核实` | arXiv 预印本（候选块未给 venue） | 低–中：时间上属等变策略的较早节点 | ★★★☆☆：作为"等变先验"方法的承上节点可读 | [42] |
| Kinematics-Aware Diffusion Policy with Consistent 3D Observation and Action Space for Whole-Arm Robotic Manipulation | 2025 | `> 待核实` | 指出只考虑末端位姿不足，需让策略感知**全臂运动学**以支持机身避碰与机身-物体交互，并统一 3D 观测与动作空间 | `> 待核实` | arXiv 预印本（cs.RO），候选块未显示 venue | 高（相对）：直接挑战"末端位姿接口"这一默认范式，是本批次中最贴合"运动学×策略"的条目 | ★★★★★：本报告第一章最推荐精读的一篇 | [27] |
| KDPE: A Kernel Density Estimation Strategy for Diffusion Policy Trajectory Selection | 2025 | `> 待核实` | 用核密度估计从扩散策略生成的多条候选轨迹中做选择，以更好覆盖行为克隆数据中的多模态 | `> 待核实` | arXiv 预印本（cs.RO），候选块未显示 venue | 中：多模态轨迹选择是 diffusion policy 的共性痛点 | ★★★★☆：作为"生成式策略的后处理"补充视角很有用 | [46] |

> 注：本节四轴的"热度证据"字段在本批证据中**系统缺失**——所有候选块均未提供 citations / GitHub star / 下载量 / 榜单排名。因此"关注度"只能依据**主题热度与相互印证关系**作低置信判断，不能当作量化结论。

### 1.2 接触隐式轨迹优化（CITO）的工程化与理论化

- **起点与两条技术路线**：`Contact-Implicit Trajectory Optimization using Orthogonal Collocation` [35]（2018）确立了正交配点在 CITO 中的用法；`Contact-Implicit Optimization of Locomotion Trajectories for a Quadrupedal Microrobot` [34]（2019）把 CITO 落到具体四足微型机器人运动轨迹上。两者构成"方法 + 应用"的早期配对 [34][35]。
- **理论补强**：`Global Convergence of an SQP Method for Contact-Implicit Trajectory Optimization` [37]（2024）针对 CITO 中 SQP 的全局收敛性给出分析，这是把 CITO 从"能跑"推进到"有收敛保证"的关键一步 [37]。权威：arXiv 预印本（候选块未显示同行评审 venue）；热度：`> 待核实`；关注度：中（理论补强类工作，社区讨论通常弱于方法类）；推荐度 ★★★★☆（做 CITO 必读的收敛性参考）[37]。
- **最新求解器**：`IMPACT: An Implicit Active-Set Augmented Lagrangian for Fast Contact-Implicit Trajectory Optimization` [39]（2026）自述其动机为：CITO 作为接触丰富任务的规划与控制统一框架已获关注，近期方法在**不需要预设接触模式表（contact-mode schedule）**的前提下已在操作与运动任务上取得有希望的结果 [39]。权威：arXiv 预印本（cs.RO）；热度/关注度：`> 待核实`（2026 年新工作，引用数据通常尚未形成）；推荐度 ★★★★☆（"快"是 CITO 的核心瓶颈，此类求解器工作直接相关）[39]。

### 1.3 QP/MPC 实时求解器（WBC 的算力底座）

| 工作 | 时间 | 一句话贡献 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 来源 |
|---|---|---|---|---|---|---|---|
| imuQP: An Inverse-Matrix-Updates-Based Fast QP Solver Suitable for Real-Time MPC | 2025 | 基于逆矩阵更新的快速 QP 求解器，面向实时 MPC | `> 待核实` | arXiv 预印本（cs.RO） | 中：实时 MPC 求解器是持续需求 | ★★★★☆：WBC/MPC 选型时的候选求解器 | [123] |
| EIQP: Execution-time-certified and Infeasibility-detecting QP Solver | 2025 | 给出**执行时间认证**并**检测不可行**的 QP 求解器 | `> 待核实` | arXiv 预印本（cs.RO） | 中–高：不可行检测直接对应"QP 可行性"这一长期痛点 | ★★★★★：同时命中"实时性"与"可行性"两个开放问题 | [122] |
| PDHCG-II: An Enhanced Version of PDHCG for Large-Scale Convex QP | 2026 | 面向大规模凸 QP 的算子分裂/增广拉格朗日类求解器增强版 | `> 待核实` | arXiv 预印本（math.OC） | 中：大规模凸 QP 在 MPC 批量求解中有需求 | ★★★☆☆：偏 math.OC，需自行验证机器人实时场景适用性 | [118] |
| Benchmarking Different QP Formulations and Solvers for Dynamic Quadrupedal Walking | 2025 | 系统比较四足动态行走中不同 QP 形式化与求解器，指出"形式化 + 选型"本身耗时巨大 | `> 待核实` | arXiv 预印本（cs.RO） | 高（相对）：这是少数直接给出"选择困难"的实证证据 | ★★★★★：工程选型的第一手参考，强烈推荐 | [119] |
| Tailored Presolve Techniques in Branch-and-Bound Method for Fast Mixed-Integer Optimal Control Applications | 2022 | 为 MI-MPC/MIQP 提供定制 presolve 加速 | `> 待核实` | arXiv 预印本（math.OC） | 低–中：混合整数控制属小众但硬需求 | ★★★☆☆：接触序列离散决策场景的潜在工具 | [57] |
| Bridging the gap between QP-based and MPC-based RL | 2022 | 探讨 QP 型与 MPC 型 RL 之间的桥接 | `> 待核实` | arXiv 预印本（候选块未给 venue） | 低–中：时间较早 | ★★★☆☆：用于理解"模型型 vs 学习型"边界的一枚拼图 | [124] |

### 1.4 全身/人形控制：学习型 WBC 成为主流形态

- `Humanoid Whole-Body Badminton via an Annealed Reinforcement Learning Curriculum` [47]（2025）：摘要明确"人形机器人已在静态场景的运动与操作上展现强能力，但**动态真实世界交互**仍困难"，作为迈向快速运动物体交互的一步，给出产出**统一全身技能**的 RL 训练流程 + 退火课程 [47]。热度/关注度：`> 待核实`；权威：arXiv 预印本（cs.RO）[47]；推荐度 ★★★★☆（动态交互是 WBC 的难度天花板之一）。
- `CHILD (Controller for Humanoid Imitation and Live Demonstration): a Whole-Body Humanoid Teleoperation System` [103]（2025）：摘要指出既有遥操作工作**很少支持人形机器人的全身关节级遥操作**，限制了可完成任务的范围 [103]。权威：arXiv 预印本（cs.RO）；热度/关注度：`> 待核实`；推荐度 ★★★★☆（全身关节级遥操作是数据采集瓶颈的正面回应）[103]。
- `Humanoid Manipulation Interface: Humanoid Whole-Body Manipulation from Robot-Free Demonstrations` [105]（2026）：摘要指出当前人形全身操作主要依赖遥操作或视觉 sim-to-real RL，受**硬件物流**与**奖励工程复杂度**限制，导致自主技能数量有限且多局限于`（摘要被截断，具体范围 待核实）` [105]。权威：arXiv 预印本（cs.RO）；推荐度 ★★★★☆（"免机器人示教"直击数据规模化问题）[105]。
- `Humanoid Whole-Body Manipulation via Active Spatial Brain and Generalizable Action Cerebellum` [104]（2026）：摘要提出空间感知人形全身操作的两大挑战——复杂 3D 环境中的空间理解、以及动作生成的泛化能力 [104]。权威：arXiv 预印本（cs.RO）；推荐度 ★★★★☆（"脑-小脑"分层是与 WBC 分层 QP 不同的架构思路）[104]。
- `Learning Humanoid Standing-up Control across Diverse Postures` [106]（2025）与 `The Role of Domain Randomization in Training Diffusion Policies for Whole-Body Humanoid Control` [102]（2024）：分别覆盖"起立"这一典型大幅接触转换任务与"域随机化 × 全身扩散策略"的组合 [106][102]。热度/关注度均 `> 待核实`；权威：arXiv 预印本 [102][106]；推荐度 ★★★☆☆–★★★★☆。

### 1.5 学习型最优控制 / 数据驱动控制的旁证前沿

`FRIDAY: Real-time Learning DNN-based Stable LQR controller for Nonlinear Systems under Uncertain Disturbances` [88]（2024）、`Koopman-based control using sum-of-squares optimization` [89]（2024）、`Learning-Based Optimal Control with Performance Guarantees for Unknown Systems with Latent States` [90]（2023）、`Kernel-based error bounds of bilinear Koopman surrogate models for nonlinear data-driven control` [92]（2025）、`Tube-based Robust Model Predictive Control for a Distributed Parameter System Modeled as a Polytopic LPV` [93]（2020）——这一组构成"学习 + 稳定性/性能保证"的证据簇 [88][89][90][92][93]。其共同价值在于回答**"学习型控制器 vs 模型型 WBC 的边界"**这一问题中的"保证"一侧 [88][90][92]。热度/关注度：`> 待核实`（无引用数/star 数据）；权威：均为 arXiv 预印本，是否已中稿 `> 待核实`；推荐度 ★★★☆☆（与机械臂/人形 WBC 直接相关性中等，作为方法论旁证）。

---

## 二、建模表示：DH vs 旋量 / POE（指数积）

> **证据状态**：本轮候选来源中，`screw theory`、`product of exponentials`、`twist/wrench`、`SE(3) Lie group`（作为建模表示）等关键词**一手命中为零**。因此本章主要依赖任务给定的**种子资源**，并对所有无法用 [n] 支撑的判断标注 `> 待核实`。

### 2.1 两种建模范式的定位（依据种子资源，非实时检索）

| 维度 | DH 参数（Denavit–Hartenberg） | 旋量 / 指数积（PoE） |
|---|---|---|
| 经典出处 | `> 待核实`（本轮未检索到一手来源） | Murray, Li, Sastry《A Mathematical Introduction to Robotic Manipulation》(1994)，种子资源：https://www.cds.caltech.edu/~murray/mlswiki/ ；Lynch & Park《Modern Robotics》(2017)，种子资源：http://hades.mech.northwestern.edu/index.php/Modern_Robotics |
| 核心特点 | 每连杆一个 4×4 变换，参数少；坐标系依附于关节轴，约定敏感 | 以螺旋轴（twist）为基元，位姿写成矩阵指数之积，坐标系选择自由、无需逐关节显式坐标系 |
| 工程后果 | 广泛存在于传统工业机器人控制器与 DH 型解析 IK 推导中 | 更易与 Lie 群/几何控制、等变学习统一（与 [41][44] 的 SE(3) 等变思路呼应） |
| 热度证据 | `> 待核实` | `> 待核实`（本轮无 citations 数据；教材引用量级应按索引库另行核查） |
| 权威证据 | `> 待核实` | 种子资源为领域公认教材（Murray et al. 1994；Lynch & Park 2017），但**本次未实时检索** |
| 关注度 | 中：DH 仍是工业实践默认 | 中–高：PoE 在学术教学与几何控制中通行 |
| 推荐度 | ★★★☆☆ | ★★★★★（与 SE(3) 等变学习的现代主线天然衔接） |

### 2.2 与几何方法相邻的可核查旁证

- `On Controller Design for Systems on Manifolds in Euclidean Space` [10]（2018，math.OC）：把状态流形 M 嵌入 ℝⁿ、在环境空间设计控制器再限制回 M，从而只需**一套全局笛卡尔坐标**综合控制器，并在含全驱动系统在内的两个基准系统上验证跟踪 [10]。它**不是** PoE 文献，但属于"用几何/流形视角简化控制器设计"的同一思想族 [10]。热度：`> 待核实`；权威：arXiv 预印本（math.OC，单一作者），是否中稿 `> 待核实`；关注度：低（无热度信号）；推荐度 ★★☆☆☆（仅作邻域线索）。
- `Geometry-aware Manipulability Learning, Tracking and Transfer` [22]（2018）：把**可操作度**当作几何对象来学习、跟踪与迁移——这是"可操作度度量"这一经典概念与现代学习方法结合的少见可核查节点 [22]。热度/权威：`> 待核实`（候选块未给出 venue）；关注度：中（可操作度 + 学习是较独特交叉）；推荐度 ★★★★☆（用于第七章奇异性/可操作度讨论）。
- 平行/并联机构运动学分析类旁证：`Kinematic analysis of a parallel robot for minimally invasive surgery` [26]（2024）、`Kinematic analysis of the 3-RPR parallel manipulator` [31]（2007）、`The Orthoglide: Kinematics and Workspace Analysis` [33]（2007）、`Compensation of compliance errors in parallel manipulators composed of non-perfect kinematic chains` [30]（2012）——这组展示**几何/解析建模在并联机构上的持久价值**（工作空间分析、标定与柔性误差补偿）[26][30][31][33]。热度/权威：`> 待核实`；关注度：低；推荐度 ★★☆☆☆（若非并联机构场景，仅作建模方法论参考）。

### 2.3 结论与缺口

- 可以确定的是：**2024–2026 的"几何表示"热度主要来自 SE(3) 等变学习一侧** [41][42][44]，而非新的旋量理论本体研究。
- **待核实**：旋量/PoE 是否有 2024–2026 的新综述或新公式化工作（本轮零命中，需以 `product of exponentials robot 2025 survey`、`screw theory Lie group robot control` 重检）。

---

## 三、逆运动学：解析 / 数值 / 学习

> **证据状态**：本轮在 IK 方向取得**少量但可直接使用**的一手条目，集中在"解析解 × 冗余度 × 奇异性"三处 [96][97][32]。传统数值 IK 求解器（KDL/IKFast/TRAC-IK）本身的一手论文**未命中**，只能依种子资源并标注 `> 待核实`。

### 3.1 三种范式与代表证据

| 范式 | 代表工作 | 时间 | 一句话贡献 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 来源 |
|---|---|---|---|---|---|---|---|---|
| 解析（Analytical） | Machine Learning-based Framework for Optimally Solving the Analytical Inverse Kinematics for Redundant Manipulators | 2022 | 用机器学习框架**优化求解**冗余机械臂的解析 IK（即把解析推导中的参数选择/分支选择问题学习化） | `> 待核实` | arXiv 预印本 | 中：解析 IK + 冗余是真机部署痛点 | ★★★★☆：把"解析解推导"与"学习"结合的少见节点 | [96] |
| 冗余参数化 + 解析 | Redundancy parameterization and inverse kinematics of 7-DOF revolute manipulators | 2023 | 系统处理 **7-DOF 转动关节机械臂**的冗余参数化与 IK | `> 待核实` | arXiv 预印本 | 中–高：7-DOF 冗余臂是主流工业/协作臂构型 | ★★★★★：冗余度解析（零空间/自运动）最实用的一手参考 | [97] |
| 奇异性专门处理 | Analytically Informed Inverse Kinematics Solution at Singularities | 2024 | 在**奇异位形处**给出"解析信息引导"的 IK 解 | `> 待核实` | arXiv 预印本 | 中–高：奇异性是 IK 失败的首要来源 | ★★★★★：直击"奇异性与任务优先级冲突"开放问题的地基 | [32] |
| 数值（通用） | Orocos KDL 的 IK、IKFast、TRAC-IK | `> 待核实` | KDL 提供 FK/IK/Jacobian；IKFast 生成解析闭式解；TRAC-IK 改善收敛 | `> 待核实`（本轮无 star 数据） | GitHub 官方仓库（种子资源：https://github.com/orocos/orocos_kinematics_dynamics ）；IKFast/TRAC-IK 未在本次候选列表中，`> 待核实` | 中（KDL 长期作为 ROS 生态默认） | ★★★★☆（KDL 部分）：与 ROS2 集成紧密度使其仍有工程价值 | 种子 / `> 待核实` |
| 学习（Learning） | 见第一章的等变/运动学感知策略 [27][41][44] | 2024–2025 | 用学习替代或包裹解析/数值 IK，在策略内部隐式完成运动学映射 | `> 待核实` | arXiv 预印本（cs.RO） | 高：目前最活跃的一支 | ★★★★★：与 [96][97] 对照可看清"学习是否真的替代了 IK" | [27][41][44] |

### 3.2 关键判读

- **解析解并未过时**：冗余（7-DOF）[97] 与奇异位形 [32] 上的解析工作仍在 2023–2024 产出，说明"纯学习 IK"尚未接管高可靠场景。
- **学习化解析 IK 的定位**：[96] 的目标是"最优地求解解析 IK"，即把学习用于**选择/优化**而非替代解析结构——这是一个比"端到端学 IK"更工程可落地的折中 [96]。
- **与不确定性的交叉**：`Adaptive Control of Robot Manipulators With Uncertain Kinematics and Dynamics` [12]（2014）在**运动学与动力学均不确定**的前提下实现任务空间轨迹跟踪，且控制器具备 separation property，是"IK/雅可比不精确时怎么办"这一问题的经典处理方式（早于本节时间窗，属经典层）[12]。权威：arXiv 预印本（eess.SY），是否中稿 `> 待核实`；热度：`> 待核实`；关注度：低（无热度信号）；推荐度 ★★★☆☆（作为"不确定性下任务空间跟踪"的一手线索）[12]。
- **缺口**：IKFast、TRAC-IK、KDL 的**原始论文与仓库 star/许可信息本轮全部缺失**，任何关于其许可（如 IKFast 的生成器许可）与维护活跃度的断言都 `> 待核实`。

---

## 四、轨迹规划与最优控制

> **证据状态**：DDP / iLQR / TrajOpt 三条经典谱线的**一手论文本轮零命中**（q2 候选块为该子问题提供的 6 条来源全部无关，已逐条核对 [1][9][10][11][12][13]）。因此本节把可核查证据放在 (a) 接触隐式优化、(b) 最优控制/MPC 综述与鲁棒 MPC、(c) Crocoddyl 框架，并对 DDP/iLQR/TrajOpt 谱系标注缺口。

### 4.1 经典谱系：DDP → iLQR → TrajOpt（证据缺口）

| 方法 | 地位 | 本轮证据 | 热度证据 | 权威证据 | 关注度 | 推荐度 |
|---|---|---|---|---|---|---|
| DDP（Differential Dynamic Policy） | 轨迹优化的二阶基线 | **零命中**（q2 候选 6 条均无关 [1][9][10][11][12][13]） | `> 待核实` | `> 待核实` | `> 待核实` | 需重检后再评 |
| iLQR | DDP 的高效近似，机器人 MPC/轨迹优化常用 | **零命中** | `> 待核实` | `> 待核实` | `> 待核实` | 需重检后再评 |
| TrajOpt（Sequential Convex Optimization） | 把非凸轨迹优化序列化为凸子问题，工业界广泛使用 | **零命中** | `> 待核实` | `> 待核实` | `> 待核实` | 需重检后再评 |
| Crocoddyl | DDP 族在接触丰富多接触场景下的现代开源实现 | 有：arXiv:1909.04947 [56] | `> 待核实`（无 star/citations 数据） | arXiv 预印本（cs.RO），LAAS-CNRS 系（种子资源标注），是否中稿 IEEE RA-L `> 待核实` | 中–高：多接触最优控制的主流开源框架之一 | ★★★★★：本章最推荐的一手条目 | [56] |

> **待核实**：Crocoddyl 的版本号、star 数、许可（BSD-2/BSD-3 之说）均未在本轮证据中出现，禁止据此下许可结论；需查 GitHub 仓库页与官方文档。

### 4.2 接触隐式优化（CITO）谱系（证据充分）

- 谱系链：**正交配点法** [35]（2018）→ **四足微型机器人运动轨迹** [34]（2019）→ **SQP 全局收敛性** [37]（2024）→ **隐式 active-set 增广拉格朗日（IMPACT）** [39]（2026）。
- 这条链的判读：CITO 的演进重心从"配点/离散化方案的可行性" [35][34]，转移到"**收敛性保证**" [37] 与"**求解速度**" [39]——正是一个方法从"论文演示"走向"控制器可用"的标准轨迹 [34][35][37][39]。
- 权威：全部为 arXiv 预印本；[56] 标注为 LAAS-CNRS（种子资源）；热度/关注度：`> 待核实`；推荐度：★ ★★★★（CITO 主线）[34][35][37][39][56]。

### 4.3 MPC / 鲁棒 MPC / 约束处理（可核查）

- `Analysis and design of model predictive control frameworks for dynamic operation — An overview` [11]（2023，eess.SY）：关于**动态运行条件下 MPC 框架**的分析与设计综述 [11]。它属于"通用控制"而非机器人专用，作为 MPC 设计范式参考有价值。权威：arXiv 预印本综述；热度/关注度：`> 待核实`；推荐度 ★★★☆☆（通用性高、机器人针对性弱）。
- `Tube-based Robust Model Predictive Control for a Distributed Parameter System Modeled as a Polytopic LPV` [93]（2020）：tube-based 鲁棒 MPC 在 LPV 模型上的实例，代表"如何在存在扰动时保持约束满足"的技术族 [93]。热度/关注度：`> 待核实`；权威：arXiv 预印本；推荐度 ★★☆☆☆（偏过程控制，作为 tube MPC 参考）。
- `Duality-based Convex Optimization for Real-time Obstacle Avoidance between Polytopes with Control Barrier Functions` [62]（2021）：用对偶凸优化 + CBF 实时求解**多面体之间的避障**——这是"轨迹优化中几何约束如何保持实时"的直接相关证据 [62]。热度/关注度：`> 待核实`；推荐度 ★★★★☆（机械臂/人形避障约束的可用工具思路）。
- `Tailored Presolve Techniques in Branch-and-Bound Method for Fast Mixed-Integer Optimal Control Applications` [57]（2022）：混合整数最优控制（含接触序列离散决策的对应问题）的加速手段 [57]。推荐度 ★★★☆☆。

---

## 五、全身控制与任务空间控制

### 5.1 任务空间 / 操作空间控制（奠基层，种子资源）

| 名称 | 年份 | 作者/机构 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Task Space Control / Operational Space Formulation | 1987 | Oussama Khatib | `> 待核实`（本轮无 citations 数据） | 种子资源标注为期刊论文（DOI: 10.1109/JRA.1987.1087109）；**本次未实时检索验证** | 高（学界公认奠基，但关注度数值依据 `> 待核实`） | ★★★★★：任务空间控制的概念源头，WBC 必读 | https://doi.org/10.1109/JRA.1987.1087109 | 操作空间控制奠基，种子资源 |
| Adaptive Control of Robot Manipulators With Uncertain Kinematics and Dynamics | 2014 | `> 待核实` | `> 待核实` | arXiv 预印本（eess.SY），中稿情况 `> 待核实` | 低 | ★★★☆☆ | http://arxiv.org/abs/1403.5204v3 | 运动学+动力学双重不确定下的任务空间跟踪 [12] |
| Geometry-aware Manipulability Learning, Tracking and Transfer | 2018 | `> 待核实` | `> 待核实` | arXiv 预印本 | 中 | ★★★★☆ | http://arxiv.org/abs/1811.11050v5 | 可操作度的几何化学习/跟踪/迁移 [22] |

### 5.2 现代 WBC 的两种主流实现路径

**路径 A：QP 求解的模型型 WBC。** 可核查证据是求解器与形式化层面：实时 QP 求解器 [123][122]、QP 形式化与求解器基准 [119]（该文明确指出 QP 形式化与求解器选型需耗费大量时间 [119]）、以及 presolve 加速 [57]、CBF 对偶凸优化 [62]。这一路径的**开放痛点**在 [119] 中被直接点出：形式化与选型的工程成本高 [119]。
- 热度/关注度：`> 待核实`（无引用数/star）；权威：arXiv 预印本（cs.RO）[119][122][123]；推荐度 ★★★★☆–★★★★★（选型必读）[119][122][123]。

**路径 B：学习型全身控制（RL / 扩散策略）。** 证据簇：[102] 域随机化 × 全身人形扩散策略；[47] 人形全身羽毛球（退火 RL 课程）；[106] 跨姿态起立；[103] 全身关节级遥操作；[104] 主动空间脑 + 可泛化动作小脑；[105] 免机器人示教的全身操作接口 [102][103][104][105][106][47]。
- 共同叙事：硬件物流成本 + 奖励工程复杂度 → 转向示教/遥操作/课程学习等更可扩展的数据获取方式 [103][105]。
- 热度/关注度：`> 待核实`；权威：均为 arXiv 预印本（cs.RO）；推荐度 ★★★★☆（人形 WBC 主线）[47][102][103][104][105][106]。

### 5.3 运动学进入 WBC 的关键论点

[27] 的核心论断值得单列：**"只考虑末端位姿是不充分的"**——在涉及机身避碰或机身-物体交互的操作场景中，策略必须感知**全臂运动学**，该文因此主张统一的 3D 观测与动作空间 [27]。这可以视为"任务空间控制"在**学习型 WBC 时代的重新表述**：任务空间不再是末端位姿的单点约束，而需要覆盖整条运动链 [27]。推荐度 ★★★★★ [27]。

### 5.4 工程入口（ROS2 侧）

- `ros2 fanuc interface: Design and Evaluation of a Fanuc CRX Hardware Interface in ROS2` [126]（2025）：介绍 Fanuc CRX 机器人家族的 `ros2_control` 与 Hardware Interface 集成、通信协议细节，以及**与 MoveIt2 运动规划库的集成**，并开展实验评估 [126]。这是"运动学/控制如何真正接到工业臂上"的可核查一手材料。权威：arXiv 预印本（cs.RO）；热度/关注度：`> 待核实`；推荐度 ★★★★☆ [126]。
- `Simplifying ROS2 controllers with a modular architecture for robot-agnostic reference generation` [129]（2026）：模块化、机器人无关的参考生成架构 [129]。推荐度 ★★★★☆（robot-agnostic 是复用 WBC 控制器的关键）[129]。
- `A Method for Multi-Robot Asynchronous Trajectory Execution in MoveIt2` [127]（2023）：MoveIt2 中多机器人**异步轨迹执行**方法 [127]。推荐度 ★★★★☆（多臂/人形双臂场景有用）[127]。

---

## 六、经典教材与奠基工作

> **严格说明**：本表分两类。①**种子资源**由任务给定（非本次实时检索所得），其热度/权威/关注度的量化依据一律 `> 待核实`，仅"领域公认度"可按常识陈述但不量化。②**有 [n] 支撑的条目**给出四轴。q2 的检索完全失败（候选 6 条与主题零重叠 [1][9][10][11][12][13]），这是本报告最大的证据缺口。

| 名称 | 年份 | 机构/作者 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| A Mathematical Introduction to Robotic Manipulation（旋量/指数积） | 1994 | Murray, Li, Sastry | `> 待核实` | 种子资源，领域经典教材；本次未实时检索 | 高（公认），但量化依据 `> 待核实` | ★★★★★ | https://www.cds.caltech.edu/~murray/mlswiki/ | 旋量/POE 建模范式的源头教材 |
| Modern Robotics: Mechanics, Planning, and Control | 2017 | Lynch & Park | `> 待核实` | 种子资源，现代教材（含配套课程/软件）；本次未实时检索 | 高（公认），量化依据 `> 待核实` | ★★★★★ | http://hades.mech.northwestern.edu/index.php/Modern_Robotics | 现代运动学 + 规划 + 控制一体 |
| Task Space Control / Operational Space Formulation | 1987 | Oussama Khatib | `> 待核实` | 种子资源（DOI 已给），本次未实时核验 | 高（公认） | ★★★★★ | https://doi.org/10.1109/JRA.1987.1087109 | 操作空间控制奠基 |
| Crocoddyl: An Efficient and Versatile Framework for Multi-Contact Optimal Control | 2019/2020 | LAAS-CNRS（种子标注） | `> 待核实` | arXiv:1909.04947（cs.RO）[56]，中稿 venue `> 待核实` | 中–高 | ★★★★★ | http://arxiv.org/abs/1909.04947v2 | 多接触最优控制开源框架 |
| Contact-Implicit Trajectory Optimization using Orthogonal Collocation | 2018 | `> 待核实` | `> 待核实` | arXiv 预印本 [35] | 低–中 | ★★★★☆ | http://arxiv.org/abs/1809.06436v3 | CITO 配点法起点 |
| Contact-Implicit Optimization of Locomotion Trajectories for a Quadrupedal Microrobot | 2019 | `> 待核实` | `> 待核实` | arXiv 预印本 [34] | 低–中 | ★★★☆☆ | http://arxiv.org/abs/1901.09065v1 | CITO 早期硬件落地 |
| Adaptive Control of Robot Manipulators With Uncertain Kinematics and Dynamics | 2014 | `> 待核实` | `> 待核实` | arXiv 预印本（eess.SY）[12] | 低 | ★★★☆☆ | http://arxiv.org/abs/1403.5204v3 | 运动学/动力学双重不确定 |
| Geometry-aware Manipulability Learning, Tracking and Transfer | 2018 | `> 待核实` | `> 待核实` | arXiv 预印本 [22] | 中 | ★★★★☆ | http://arxiv.org/abs/1811.11050v5 | 可操作度的学习化 |
| Redundancy parameterization and inverse kinematics of 7-DOF revolute manipulators | 2023 | `> 待核实` | `> 待核实` | arXiv 预印本 [97] | 中–高 | ★★★★★ | http://arxiv.org/abs/2307.13122v2 | 冗余度解析/7-DOF IK |
| Analytically Informed Inverse Kinematics Solution at Singularities | 2024 | `> 待核实` | `> 待核实` | arXiv 预印本 [32] | 中–高 | ★★★★★ | http://arxiv.org/abs/2412.20409v1 | 奇异位形处解析引导 IK |

**本章结论**：经典奠基工作（PoE、操作空间控制、DDP/iLQR/TrajOpt）在**本轮证据链中不可核查**。任何关于"某教材第几章定义了什么"或"某方法在某年首次提出"的断言，本报告一律不下结论，统一标注 `> 待核实`。

---

## 七、开源库与工具链对比

> **重大警告（同名误召回）**：本轮对 `Pinocchio` 的检索全部命中**宇宙学暗物质晕代码 PINOCCHIO** [48][49][50][51][52][53]，以及一篇童话主题 RL 论文 [55]。**这些与机器人刚体动力学库 `stack-of-tasks/pinocchio` 无任何关系**，不得作为该库的证据。该库的能力、star、许可、维护活跃度在本报告中一律 `> 待核实`。

| 名称 | 年份 | 机构/作者 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| stack-of-tasks/pinocchio | `> 待核实` | `> 待核实` | `> 待核实`（本轮无 star/下载数据） | 种子资源（GitHub 官方仓库）；本次未实时检索 | 高（机器人社区公认），量化依据 `> 待核实` | ★★★★★ | https://github.com/stack-of-tasks/pinocchio | 刚体运动学/动力学 + 解析导数；**注意同名误召回 [48]-[53][55]** |
| orocos/orocos_kinematics_dynamics（KDL） | `> 待核实` | Orocos 社区 | `> 待核实` | 种子资源（GitHub 官方仓库）；本次未实时检索 | 中–高：长期作为 ROS 生态 FK/IK/Jacobian 默认实现 | ★★★★☆ | https://github.com/orocos/orocos_kinematics_dynamics | FK / IK / Jacobian；许可与维护活跃度 `> 待核实` |
| RobotLocomotion/drake | `> 待核实` | RobotLocomotion（MIT 系，种子标注） | `> 待核实` | 种子资源（GitHub 官方仓库）；本次未实时检索 | 高（公认），量化依据 `> 待核实` | ★★★★★ | https://github.com/RobotLocomotion/drake | 优化与控制的 C++ 工具箱；许可 `> 待核实` |
| loco-3d/crocoddyl | 2019/2020 | LAAS-CNRS（种子标注） | `> 待核实` | arXiv:1909.04947 [56] + 官方仓库；venue 与许可 `> 待核实` | 中–高 | ★★★★★ | https://github.com/loco-3d/crocoddyl | 多接触最优控制（DDP 族）[56] |
| moveit/moveit2 | `> 待核实` | MoveIt 社区 | `> 待核实` | 种子资源（GitHub 官方仓库）；有相关论文 [127] | 高（ROS2 事实标准规划框架），量化依据 `> 待核实` | ★★★★★ | https://github.com/moveit/moveit2 | ROS2 运动规划；多机异步执行见 [127]；与工业臂硬件接口集成见 [126] |
| OCS2 | `> 待核实` | `> 待核实` | `> 待核实` | **本轮检索零命中**，无 [n] 可引用 | `> 待核实` | 需重检后再评 | `> 待核实` | 本轮无任何证据，禁止评价 |
| IKFast | `> 待核实` | `> 待核实` | `> 待核实` | **本轮检索零命中** | `> 待核实` | 需重检后再评 | `> 待核实` | 本轮无证据；IKFast 常被与解析 IK 对比，但缺一手来源 |
| TRAC-IK | `> 待核实` | `> 待核实` | `> 待核实` | **本轮检索零命中** | `> 待核实` | 需重检后再评 | `> 待核实` | 本轮无证据 |
| MuJoCo / MJX | `> 待核实` | `> 待核实` | `> 待核实` | **本轮检索零命中** | `> 待核实` | 需重检后再评 | `> 待核实` | 本轮无证据（尽管 [102] 等使用仿真，但未给出仿真器细节） |
| CasADi | `> 待核实` | `> 待核实` | `> 待核实` | **本轮检索零命中** | `> 待核实` | 需重检后再评 | `> 待核实` | 本轮无证据 |

### 7.1 ROS2 生态集成（本章证据最扎实的部分）

- **`ros2_control` + 工业臂**：Fanuc CRX 硬件接口，含通信协议、与 MoveIt2 集成及实验评估 [126]。关注度：中–高（工业臂 ROS2 化是落地刚需）；推荐度 ★★★★☆ [126]。
- **控制器架构**：模块化、robot-agnostic 参考生成 [129]（2026），直接回应"不同本体复用同一控制器"的工程诉求 [129]。推荐度 ★★★★☆。
- **规划层多机**：MoveIt2 多机器人异步轨迹执行 [127]（2023）。推荐度 ★★★★☆。
- **通信与实时性**：ROS2 多节点系统延迟分析 [130]（2021）——对实时 WBC 部署至关重要（DDS 配置、QoS 与延迟抖动）[130]；跨广域网 ROS2 方案 ROS2 Connect [128]（2026）[128]；云端机器人安全全局连接 FogROS2-SGC [131]（2023）[131]。热度/关注度：`> 待核实`；推荐度 ★★★☆☆–★★★★☆。
- **可观测性与开发体验**：ROS2 需求到自主机器人的运行时监控 [132]（2022）[132]；LLM 辅助理解 ROS2 软件架构 [133]（2026）[133]——后者代表"用 LLM 降低机器人软件栈理解成本"的新方向 [133]。
- **早期平台参考**：NimbRo-OP 人形开源平台的 ROS 软件框架 [107]（2018），作为人形软件栈历史节点 [107]。推荐度 ★★☆☆☆。

**选型结论（保守）**：本轮证据**只能支撑 ROS2 集成层面的判断**（`ros2_control` + MoveIt2 + 控制器模块化 [126][127][129]），**无法支撑**关于 Pinocchio / Drake / OCS2 / CasADi / MuJoCo 的性能、许可、维护活跃度的任何比较性结论——这些必须在重检后补齐（需 GitHub API 取 star/最后提交、查官方仓库 LICENSE 文件）。

---

## 八、开放问题与关注清单

> **证据状态**：子问题 q5 的候选证据（[72][77][80][81][82][83]）**全部与主题无关**——分别为加权最小二乘估计收敛性、SEM 图像高斯过程回归去噪、SemEval-2025 主题标引、意/英物理常识推理基准、DISRPT 2025 篇章关系分类、越南语交通标志法律问答。因此本章按"可核查部分 + 明确缺口"组织，**不对无证据问题给出结论**。

### 8.1 有证据支撑的开放问题

1. **QP 形式化与求解器选型的工程成本（高置信）**：[119] 明确指出，QP 广泛用于行走机器人的 MPC 与 WBC，而控制器设计**既需要设计 QP 形式化、又需要选择合适求解器，两者都相当耗时** [119]。这是 WBC 落地最被低估的成本项。
2. **QP 实时性与不可行性检测（中–高置信）**：求解器侧已有正面回应——面向实时 MPC 的逆矩阵更新快速 QP [123]，以及具备**执行时间认证 + 不可行检测**的 EIQP [122]。"不可行时怎么办"从工程 hack 走向求解器特性 [122]。
3. **接触隐式的收敛与速度**：SQP 全局收敛性 [37] 与快速隐式 active-set 增广拉格朗日 [39] 分别代表"保证"与"速度"两个方向；但**接触穿透（penetration）与接触模型精度**在本轮证据中未被正面讨论，`> 待核实`。
4. **学习型 vs 模型型 WBC 的边界**：可用的可核查锚点是 [124]（QP 型与 MPC 型 RL 的桥接）[88][90][92]（学习型控制器的稳定性/性能保证）[102]（域随机化对全身扩散策略的作用）[124][88][90][92][102]。**结论性判断 `> 待核实`**：本轮证据不足以裁定"哪一侧在什么条件下更优"。
5. **sim-to-real 鸿沟**：[102] 以域随机化作为手段 [102]；[105] 指出视觉 sim-to-real RL 受奖励工程与硬件物流限制 [105]。这是**问题被承认**的证据，而非**问题被解决**的证据 [102][105]。
6. **奇异性**：IK 侧有专门工作 [32]，可操作度的几何化学习 [22]；但"奇异性 × 任务优先级冲突"在**全身控制层**的处理本轮无一手证据，`> 待核实`。
7. **运动学结构必须进入策略**：[27] 明确论证末端位姿接口不足，需要全臂运动学感知 [27]。这是 2025–2026 一条值得持续跟踪的论点。

### 8.2 明确缺口清单（必须重检）

| 缺失主题 | 本轮状态 | 建议检索式 |
|---|---|---|
| 旋量理论 / PoE 奠基与现代化 | 零命中 | `product of exponentials robot kinematics survey`、`screw theory Lie group robot 2024..2026` |
| 操作空间控制（Khatib）原始文献核验 | 仅种子资源，未实时核验 | DOI 直查 + 引用其的近年 WBC 论文 |
| 可操作度（manipulability）定义来源与经典指标口径 | 零命中（仅 [22] 为几何化变体） | `manipulability measure Yoshikawa definition` |
| 冗余度解析 / 零空间 / 任务优先级 | 仅 [97] 一条 | `null space projection task priority redundancy resolution` |
| DDP / iLQR / TrajOpt 谱系 | 零命中 | `DDP iLQR trajectory optimization robot`、`TrajOpt sequential convex optimization` |
| QP 可行性与实时性的系统性评测 | 部分（[119][122][123]） | `WBC QP solver benchmark feasibility real-time` |
| 接触建模与穿透 | 零命中 | `contact penetration implicit complementarity robotics` |
|

## 二、建模表示：DH vs 旋量/POE

### 2.1 本章证据状况（先声明缺口）

本轮结构化检索为「旋量理论与指数积（PoE）、DH 参数法、操作空间控制」这一子问题（q2）分配到的 6 条候选证据（[1][9][10][11][12][13]）与本主题几乎零重叠：其中 [1] 为高能物理非弹性散射测量、[9] 为刚性翼空中风能系统控制、[13] 为空间天气集合预报，均与机器人学无实质交集；候选块的全部标题与摘要片段中未出现 screw theory、product of exponentials、Denavit–Hartenberg、manipulability、operational space 等关键术语 [1][9][10][11][12][13]。因此**本章的经典脉络部分只能依赖任务给定的种子资源（Murray/Li/Sastry 教材、Lynch & Park 教材、Khatib 1987），其引用以种子链接形式给出，不对其热度/引用数做任何数字性断言**；涉及「DH vs PoE 谁更优」的具体工程结论，凡无一手来源者一律标注 `> 待核实`。

### 2.2 两种表示范式的基本分工（基于种子教材，细节待核实）

- **DH 参数法（Denavit–Hartenberg）**：用 4 个连杆参数（两扭转角、两连杆长度/偏置）逐关节建立相邻坐标系变换，形成串联链的正运动学闭式表达。其原始提出年份与出处在本轮候选中无一手来源，`> 待核实`。其工程优势（参数少、与厂商关节标定变量对应直观）与固有缺陷（关节轴平行或近似平行时参数不唯一/病态、不便表示树形与闭链机构、局部坐标系的语义不统一）在本轮检索中亦无一手来源支撑，`> 待核实`。
- **旋量理论 / 指数积（PoE, Product of Exponentials）**：以每条关节轴在基座（空间型）或末端（物体型）坐标系下的螺旋轴（twist）$\\xi_i$ 与关节位移 $\\theta_i$ 直接构造 $T(\\theta)=e^{[\\mathcal{S}_1]\\theta_1}\\cdots e^{[\\mathcal{S}_n]\\theta_n}M$，天然定义在 SE(3)/Lie 群上，与雅可比、可操作度、几何控制同构。该框架的经典系统化表述见 Murray, Li & Sastry《A Mathematical Introduction to Robotic Manipulation》（1994，种子资源）与 Lynch & Park《Modern Robotics》（2017，种子资源）；两书均为教材而非同行评审论文，**权威证据：经典教科书（种子资源，作者为领域核心团队）；热度证据：教材级影响力无 citations 字段，`> 待核实`**。

### 2.3 与雅可比、奇异性、可操作度的耦合

采用 PoE/SE(3) 表示的一个直接受益点是雅可比与奇异性分析的几何化：

- **可操作度（manipulability）与几何感知学习**：[22] 研究「几何感知的可操作度学习、跟踪与迁移」（Geometry-aware Manipulability Learning, Tracking and Transfer），把可操作度椭球作为几何对象来学习与迁移，说明可操作度指标并未停留在经典定义，而已被纳入数据驱动框架。**权威证据：arXiv 预印本（cs.RO），同行评审状态未知 `> 待核实`；热度证据：候选块未提供 citations/star 字段，`> 待核实`；关注度：`> 待核实`；推荐度：★★★☆☆（可作为「雅可比—可操作度—学习」交叉支线的入口，但需先核实其最终发表 venue 与实验口径）** [22]。
- **奇异性附近的解析信息利用**：[32] 标题为「Analytically Informed Inverse Kinematics Solution at Singularities」，直接针对奇异位形下的 IK 求解，提示当前工程界在奇异处理上仍倾向「解析结构 + 数值兜底」的混合路线。**权威证据：arXiv 预印本（cs.RO，2024），同行评审状态 `> 待核实`；热度证据：`> 待核实`；关注度：`> 待核实`；推荐度：★★★☆☆（与奇异性主题高度相关，建议全文精读后再引用其具体方法）** [32]。
- **冗余参数化与 7-DOF 转动关节**：[97] 标题为「Redundancy parameterization and inverse kinematics of 7-DOF revolute manipulators」，表明冗余自由度参数化（自运动流形的坐标选择）仍是 7-DOF 臂工程实现的关键环节；具体的参数化方式（臂角/自运动角/旋量参数等）在候选摘要片段中未给出，`> 待核实`。**权威证据：arXiv 预印本（cs.RO，2023），评审状态 `> 待核实`；热度/关注度：`> 待核实`；推荐度：★★★☆☆（冗余臂 IK 的实用参考，需核实是否中稿）** [97]。
- **解析 IK 的学习化加速**：[96] 提出面向冗余机械臂、以机器学习框架最优求解解析 IK 的方案，说明「解析解结构 + 学习」正在成为数值 IK 之外的第三条路线。**权威证据：arXiv 预印本（cs.RO，2022），评审状态 `> 待核实`；热度/关注度：`> 待核实`；推荐度：★★★☆☆（与第三章「解析/数值/学习三分类」直接呼应）** [96]。

### 2.4 并联机构：DH 与 PoE 之外的几何法传统

本轮候选中的并联机器人文献（[26][30][31][33]）多以显式几何/代数推导做运动学与工作空间分析，而非统一走 DH 或 PoE 形式，反映出闭链机构的表示选择至今缺乏如串联链 PoE 那样的单一标准：

- [26] 面向微创手术并联机器人的运动学分析（Kinematic analysis of a parallel robot for minimally invasive surgery）；[31] 3-RPR 并联机械手运动学分析；[33] Orthoglide 的运动学与工作空间分析；[30] 研究非完美运动链并联机械手的柔顺误差补偿。
- **四轴证据（合并陈述）：权威证据——四篇均为 arXiv 预印本（cs.RO / 相关分类），是否中稿 `> 待核实` [26][30][31][33]；热度证据——候选块未提供 citations/star，`> 待核实`；关注度——`> 待核实`；推荐度——★★☆☆☆（作为「闭链机构表示缺乏统一标准」这一论断的线索，需另找一手来源确认其方法与结论）**。

### 2.5 现代工程栈中的表示选择（与第七章交叉）

种子资源所列主流库在内部表示上普遍向 Lie 群/SE(3) 与「无 DH 依赖」方向演进，但**这些判断来自种子库的自述定位，而非本章可核查的一手技术文档，故标注 `> 待核实`**：

- `stack-of-tasks/pinocchio`：种子描述为「刚体运动学/动力学，含解析导数」，其在多体算法中采用 SE(3) 位姿与空间向量（spatial algebra）表示，使 FK/雅可比可解析求导；**权威证据：官方 GitHub 仓库（B 级，种子资源）；热度证据：star 数未在本轮检索中取得，`> 待核实`；关注度：`> 待核实`；推荐度：★★★★☆（种子库，与第 2、4、7 章均强相关）**。
- `orocos/orocos_kinematics_dynamics`（KDL）：种子描述为「FK/IK/Jacobian」；其在 ROS/ROS2 生态中长期作为传统运动学后端，历史上与 DH/关节链表示绑定，**具体表示选择 `> 待核实`**；**权威证据：官方 GitHub 仓库（B 级，种子资源）；热度/关注度：`> 待核实`；推荐度：★★★☆☆（工程可用，但需核实其在新版 ROS2 中的维护状态与替代关系）**。
- `loco-3d/crocoddyl`：其多接触最优控制求解依赖 Pinocchio 的多体表示，[56] 为其官方论文「Crocoddyl: An Efficient and Versatile Framework for Multi-Contact Optimal Control」；**权威证据：arXiv 预印本（cs.RO，2019/2020），同行评审状态 `> 待核实` [56]；热度证据：`> 待核实`；关注度：`> 待核实`；推荐度：★★★★☆（接触隐式优化与 SE(3) 表示的结合点，详见第四章）**。
- `RobotLocomotion/drake`：种子描述为「优化与控制的 C++ 工具箱」，其内部采用四元数/旋转矩阵与通用多体表示，而非 DH 参数；**权威证据：官方 GitHub 仓库（B 级，种子资源）；热度/关注度：`> 待核实`；推荐度：★★★★☆（跨第 4、5、7 章的核心工具）**。

### 2.6 小结与待核实清单

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| A Mathematical Introduction to Robotic Manipulation | 1994 | Murray, Li, Sastry | `> 待核实` | 经典教材（种子资源，非同行评审论文） | `> 待核实` | ★★★★★ | https://www.cds.caltech.edu/~murray/mlswiki/ | 旋量/指数积（PoE）系统化奠基教材 |
| Modern Robotics: Mechanics, Planning, and Control | 2017 | Lynch & Park | `> 待核实` | 经典教材（种子资源） | `> 待核实` | ★★★★★ | http://hades.mech.northwestern.edu/index.php/Modern_Robotics | 以 PoE 与 Lie 群为主线的现代运动学/控制教材 |
| Task Space Control / Operational Space Formulation | 1987 | Oussama Khatib | `> 待核实` | 期刊论文（种子资源给出 DOI） | `> 待核实` | ★★★★★ | https://doi.org/10.1109/JRA.1987.1087109 | 操作空间控制奠基，与任务空间雅可比直接相关 |
| Crocoddyl | 2020 | LAAS-CNRS | `> 待核实` | arXiv 预印本 cs.RO [56]，评审状态 `> 待核实` | `> 待核实` | ★★★★☆ | https://arxiv.org/abs/1909.04947 | 多接触最优控制，依赖 SE(3) 多体表示 |
| Geometry-aware Manipulability Learning, Tracking and Transfer | 2018 | 未在候选块给出 | `> 待核实` | arXiv 预印本 cs.RO [22]，评审状态 `> 待核实` | `> 待核实` | ★★★☆☆ | http://arxiv.org/abs/1811.11050v5 | 可操作度的几何化学习与迁移 |
| Analytically Informed Inverse Kinematics Solution at Singularities | 2024 | 未在候选块给出 | `> 待核实` | arXiv 预印本 cs.RO [32]，评审状态 `> 待核实` | `> 待核实` | ★★★☆☆ | http://arxiv.org/abs/2412.20409v1 | 奇异位形下的解析+数值混合 IK |
| Redundancy parameterization and inverse kinematics of 7-DOF revolute manipulators | 2023 | 未在候选块给出 | `> 待核实` | arXiv 预印本 cs.RO [97]，评审状态 `> 待核实` | `> 待核实` | ★★★☆☆ | http://arxiv.org/abs/2307.13122v2 | 冗余参数化与 7-DOF 臂 IK |

**本章待核实清单（须补充检索后才能定论）**：

1. DH 参数法的原始提出文献（年份、venue）在本轮候选中零命中 `> 待核实`。
2. 「DH 在关节轴平行/近似平行时参数病态」这一常见论断缺一手来源 `> 待核实`。
3. PoE 相对 DH 在数值条件数、与雅可比一致性上的定量对比实验（任务数、本体、仿真/真机）在本轮候选中零命中 `> 待核实`。
4. 主流库（Pinocchio / KDL / Drake / MuJoCo）内部旋转表示的官方技术文档本轮未逐条核验 `> 待核实`。
5. [22][32][96][97] 的最终发表 venue 与引用数未取得，暂不能作为「已被验证」的结论使用 [22][32][96][97]。

## 参考来源

[1] Measurement of inelastic scattering $Λ(\overlineΛ)+p\toΣ^{0}(\overlineΣ^{0})+p$ via $e^+e^-\to J/ψ\toΛ\overlineΛ$ — http://arxiv.org/abs/2609.02584v1
[2] Evidence of $ψ(3770) \to π^{0}J/ψ$ — http://arxiv.org/abs/2606.14105v1
[3] Measurement of the CKM angle $γ$ in $B^{\pm} \rightarrow D(\rightarrow K^{0}_{\rm S} h^{\prime+}h^{\prime-})h^{\pm}$ decays with a novel approach — http://arxiv.org/abs/2604.05701v1
[4] Model Independent Approach of the JUNO $^8$B Solar Neutrino Program — http://arxiv.org/abs/2210.08437v2
[5] Precise measurement of the CKM angle $γ$ with a novel approach — http://arxiv.org/abs/2604.05712v1
[6] Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, Long Context, and Next Generation Agentic Capabilities — http://arxiv.org/abs/2507.06261v6
[7] First measurement of reactor neutrino oscillations at JUNO — http://arxiv.org/abs/2511.14593v1
[8] Initial performance results of the JUNO detector — http://arxiv.org/abs/2511.14590v1
[9] Control of a Rigid Wing Pumping Airborne Wind Energy System in all Operational Phases — http://arxiv.org/abs/2006.11141v1
[10] On Controller Design for Systems on Manifolds in Euclidean Space — http://arxiv.org/abs/1807.03475v1
[11] Analysis and design of model predictive control frameworks for dynamic operation -- An overview — http://arxiv.org/abs/2307.03004v2
[12] Adaptive Control of Robot Manipulators With Uncertain Kinematics and Dynamics — http://arxiv.org/abs/1403.5204v3
[13] The importance of ensemble techniques for operational space weather forecasting — http://arxiv.org/abs/1806.09861v1
[14] Cold-Tip Temperature Control of Space-borne SatelliteStirlingCryocooler: Mathematical Modeling and Control Investigation — http://arxiv.org/abs/1905.11247v1
[15] Verification of Space Weather Forecasts issued by the Met Office Space Weather Operations Centre — http://arxiv.org/abs/1804.02985v1
[16] SPACE: the SPectroscopic All-sky Cosmic Explorer — http://arxiv.org/abs/0804.4433v1
[17] A rich bounty of AGN in the 9 square degree Bootes survey: high-z obscured AGN and large-scale structure — http://arxiv.org/abs/astro-ph/0611654v1
[18] AIn't Nothing But a Survey? Using Large Language Models for Coding German Open-Ended Survey Responses on Survey Motivation — http://arxiv.org/abs/2506.14634v3
[19] The Methanol Multibeam Survey — http://arxiv.org/abs/1210.0979v1
[20] The Dark Energy Survey — http://arxiv.org/abs/astro-ph/0510346v1
[21] Nonabelian Jacobian of Smooth Projective Surfaces - A Survey — http://arxiv.org/abs/1103.5323v1
[22] Geometry-aware Manipulability Learning, Tracking and Transfer — http://arxiv.org/abs/1811.11050v5
[23] The SAMI Galaxy Survey: first 1000 galaxies — http://arxiv.org/abs/1409.4147v1
[24] Roman Galactic Plane Survey Definition Committee Report — http://arxiv.org/abs/2511.07494v1
[25] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1
[26] Kinematic analysis of a parallel robot for minimally invasive surgery — http://arxiv.org/abs/2406.02047v1
[27] Kinematics-Aware Diffusion Policy with Consistent 3D Observation and Action Space for Whole-Arm Robotic Manipulation — http://arxiv.org/abs/2512.17568v1
[28] Triplets of Galaxies in the Local Supercluster. I. Kinematic and Virial Parameters — http://arxiv.org/abs/astro-ph/0609622v1
[29] One-Shot Reinforcement Learning for Robot Navigation with Interactive Replay — http://arxiv.org/abs/1711.10137v2
[30] Compensation of compliance errors in parallel manipulators composed of non-perfect kinematic chains — http://arxiv.org/abs/1204.1757v1
[31] Kinematic analysis of the 3-RPR parallel manipulator — http://arxiv.org/abs/0708.3920v1
[32] Analytically Informed Inverse Kinematics Solution at Singularities — http://arxiv.org/abs/2412.20409v1
[33] The Orthoglide: Kinematics and Workspace Analysis — http://arxiv.org/abs/0705.1394v1
[34] Contact-Implicit Optimization of Locomotion Trajectories for a Quadrupedal Microrobot — http://arxiv.org/abs/1901.09065v1
[35] Contact-Implicit Trajectory Optimization using Orthogonal Collocation — http://arxiv.org/abs/1809.06436v3
[36] A Simulation and Modeling of Access Points with Definition Language — http://arxiv.org/abs/1304.1836v2
[37] Global Convergence of an SQP Method for Contact-Implicit Trajectory Optimization — http://arxiv.org/abs/2406.01763v5
[38] Superconductivity as a consequence of an ordering of the electron gas zero-point oscillations — http://arxiv.org/abs/1005.0280v6
[39] IMPACT: An Implicit Active-Set Augmented Lagrangian for Fast Contact-Implicit Trajectory Optimization — http://arxiv.org/abs/2605.09127v3
[40] Technical Report for ICRA 2025 GOOSE 3D Semantic Segmentation Challenge: Adaptive Point Cloud Understanding for Heterogeneous Robotic Systems — http://arxiv.org/abs/2506.06995v1
[41] SE(3)-Equivariant Diffusion Policy in Spherical Fourier Space — http://arxiv.org/abs/2507.01723v1
[42] Leveraging SE(3) Equivariance for Learning 3D Geometric Shape Assembly — http://arxiv.org/abs/2309.06810v2
[43] LLM-based ambiguity detection in natural language instructions for collaborative surgical robots — http://arxiv.org/abs/2507.11525v1
[44] ET-SEED: Efficient Trajectory-Level SE(3) Equivariant Diffusion Policy — http://arxiv.org/abs/2411.03990v2
[45] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1
[46] KDPE: A Kernel Density Estimation Strategy for Diffusion Policy Trajectory Selection — http://arxiv.org/abs/2508.10511v2
[47] Humanoid Whole-Body Badminton via an Annealed Reinforcement Learning Curriculum — http://arxiv.org/abs/2511.11218v4
[48] PINOCCHIO and the hierarchical build-up of dark matter haloes — http://arxiv.org/abs/astro-ph/0109324v1
[49] PINOCCHIO: pinpointing orbit-crossing collapsed hierarchical objects in a linear density field — http://arxiv.org/abs/astro-ph/0109323v2
[50] An implementation of nDGP gravity in Pinocchio — http://arxiv.org/abs/2311.11840v1
[51] Simulating cosmologies beyond $Λ$CDM with PINOCCHIO — http://arxiv.org/abs/1610.07624v1
[52] A study of relative velocity statistics in Lagrangian perturbation theory with PINOCCHIO — http://arxiv.org/abs/1011.1559v3
[53] Testing the Reliability of Fast Methods for Weak Lensing Simulations: WL-MOKA on PINOCCHIO — http://arxiv.org/abs/2001.11512v2
[54] The Relativistic Elasticity of Rigid Bodies — http://arxiv.org/abs/physics/0307019v3
[55] What if Pinocchio Were a Reinforcement Learning Agent: A Normative End-to-End Pipeline — http://arxiv.org/abs/2603.16651v1
[56] Crocoddyl: An Efficient and Versatile Framework for Multi-Contact Optimal Control — http://arxiv.org/abs/1909.04947v2
[57] Tailored Presolve Techniques in Branch-and-Bound Method for Fast Mixed-Integer Optimal Control Applications — http://arxiv.org/abs/2211.12700v2
[58] Developing a 21st Century Global Library for Mathematics Research — http://arxiv.org/abs/1404.1905v1
[59] Optimal distributed control of a stochastic Cahn-Hilliard equation — http://arxiv.org/abs/1810.09292v2
[60] Numerical Approximations to Fractional Problems of the Calculus of Variations and Optimal Control — http://arxiv.org/abs/1310.5377v2
[61] Optimal Control of Vehicular Formations with Nearest Neighbor Interactions — http://arxiv.org/abs/1112.4113v1
[62] Duality-based Convex Optimization for Real-time Obstacle Avoidance between Polytopes with Control Barrier Functions — http://arxiv.org/abs/2107.08360v4
[63] Reduced modelling and optimal control of epidemiological individual-based models with contact heterogeneity — http://arxiv.org/abs/2205.06539v1
[64] Inversion of the star transform — http://arxiv.org/abs/1401.7655v2
[65] Inversion formulas for the broken-ray Radon transform — http://arxiv.org/abs/1007.4183v1
[66] Inverse spectral problems for Sturm-Liouville operators with singular potentials — http://arxiv.org/abs/math/0211247v1
[67] Inverse Problems in Magnetohydrodynamics: Theoretical and Experimental Aspects — http://arxiv.org/abs/physics/0312093v1
[68] A note on convergence of solutions of total variation regularized linear inverse problems — http://arxiv.org/abs/1711.06495v3
[69] Inverse Laplace Transform for Bi-Complex Variables — http://arxiv.org/abs/1403.3313v1
[70] The enclosure method for inverse obstacle scattering problems with dynamical data over a finite time interval: III. Sound-soft obstacle and bistatic data — http://arxiv.org/abs/1302.2389v1
[71] An inverse problem of radiative potentials and initial temperatures in parabolic equations with dynamic boundary conditions — http://arxiv.org/abs/2103.15116v1
[72] Fast Convergence for Weighted Least Squares Estimates — http://arxiv.org/abs/2605.00198v3
[73] A Molecular Implementation of the Least Mean Squares Estimator — http://arxiv.org/abs/1701.00602v1
[74] Convergence of Alternating Least Squares Optimisation for Rank-One Approximation to High Order Tensors — http://arxiv.org/abs/1503.05431v1
[75] The Cramer-Rao inequality to go beyond the $\mathbf{\sqrt{N}}$-limit of the standard least-squares method in track fitting — http://arxiv.org/abs/1910.14494v1
[76] Fast and forward stable randomized algorithms for linear least-squares problems — http://arxiv.org/abs/2311.04362v2
[77] Adaptive Optimizable Gaussian Process Regression Linear Least Squares Regression Filtering Method for SEM Images — http://arxiv.org/abs/2510.07895v1
[78] Detection of epileptic seizure in EEG signals using linear least squares preprocessing — http://arxiv.org/abs/1604.08500v1
[79] Acceleration Control in Nonlinear Vibrating Systems based on Damped Least Squares — http://arxiv.org/abs/1110.2811v2
[80] Annif at SemEval-2025 Task 5: Traditional XMTC augmented by LLMs — http://arxiv.org/abs/2504.19675v2
[81] Culturally Grounded Physical Commonsense Reasoning in Italian and English: A Submission to the MRL 2025 Shared Task — http://arxiv.org/abs/2510.22631v1
[82] DeDisCo at the DISRPT 2025 Shared Task: A System for Discourse Relation Classification — http://arxiv.org/abs/2509.11498v4
[83] VLSP 2025 MLQA-TSR Challenge: Vietnamese Multimodal Legal Question Answering on Traffic Sign Regulation — http://arxiv.org/abs/2510.20381v1
[84] NALA_MAINZ at BLP-2025 Task 2: A Multi-agent Approach for Bangla Instruction to Python Code Generation — http://arxiv.org/abs/2511.16787v1
[85] CLaC at SemEval-2025 Task 6: A Multi-Architecture Approach for Corporate Environmental Promise Verification — http://arxiv.org/abs/2505.23538v1
[86] MRT at IberLEF-2025 PRESTA Task: Maximizing Recovery from Tables with Multiple Steps — http://arxiv.org/abs/2507.12981v1
[87] DNB-AI-Project at SemEval-2025 Task 5: An LLM-Ensemble Approach for Automated Subject Indexing — http://arxiv.org/abs/2504.21589v1
[88] FRIDAY: Real-time Learning DNN-based Stable LQR controller for Nonlinear Systems under Uncertain Disturbances — http://arxiv.org/abs/2412.01103v1
[89] Koopman-based control using sum-of-squares optimization: Improved stability guarantees and data efficiency — http://arxiv.org/abs/2411.03875v6
[90] Learning-Based Optimal Control with Performance Guarantees for Unknown Systems with Latent States — http://arxiv.org/abs/2303.17963v4
[91] Geometric Programming-Based Control for Nonlinear, DAE-Constrained Water Distribution Networks — http://arxiv.org/abs/1902.06026v1
[92] Kernel-based error bounds of bilinear Koopman surrogate models for nonlinear data-driven control — http://arxiv.org/abs/2503.13407v4
[93] Tube-based Robust Model Predictive Control for a Distributed Parameter System Modeled as a Polytopic LPV (extended version) — http://arxiv.org/abs/2003.05962v4
[94] The RSNA Abdominal Traumatic Injury CT (RATIC) Dataset — http://arxiv.org/abs/2405.19595v1
[95] The RSNA Intracranial Aneurysm (RSNA-ICA) Dataset — http://arxiv.org/abs/2610.01135v2
[96] Machine Learning-based Framework for Optimally Solving the Analytical Inverse Kinematics for Redundant Manipulators — http://arxiv.org/abs/2211.04275v3
[97] Redundancy parameterization and inverse kinematics of 7-DOF revolute manipulators — http://arxiv.org/abs/2307.13122v2
[98] CPRet: A Dataset, Benchmark, and Model for Retrieval in Competitive Programming — http://arxiv.org/abs/2505.12925v2
[99] Bitstream-Corrupted Video Recovery: A Novel Benchmark Dataset and Method — http://arxiv.org/abs/2309.13890v2
[100] L-FAME: Longitudinal Focused Attention Meditation EEG Dataset and Benchmark — http://arxiv.org/abs/2605.22893v1
[101] The RSNA Lumbar Degenerative Imaging Spine Classification (LumbarDISC) Dataset — http://arxiv.org/abs/2506.09162v1
[102] The Role of Domain Randomization in Training Diffusion Policies for Whole-Body Humanoid Control — http://arxiv.org/abs/2411.01349v1
[103] CHILD (Controller for Humanoid Imitation and Live Demonstration): a Whole-Body Humanoid Teleoperation System — http://arxiv.org/abs/2508.00162v2
[104] Humanoid Whole-Body Manipulation via Active Spatial Brain and Generalizable Action Cerebellum — http://arxiv.org/abs/2605.21133v2
[105] Humanoid Manipulation Interface: Humanoid Whole-Body Manipulation from Robot-Free Demonstrations — http://arxiv.org/abs/2602.06643v2
[106] Learning Humanoid Standing-up Control across Diverse Postures — http://arxiv.org/abs/2502.08378v2
[107] A ROS-based Software Framework for the NimbRo-OP Humanoid Open Platform — http://arxiv.org/abs/1809.11051v1
[108] Motion-X: A Large-scale 3D Expressive Whole-body Human Motion Dataset — http://arxiv.org/abs/2307.00818v2
[109] LIBERO-VPro: Benchmarking Closed-Loop Visual Robustness of Robotic Foundation Models — http://arxiv.org/abs/2609.24350v1
[110] LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models — http://arxiv.org/abs/2603.28301v3
[111] VQualA 2025 Challenge on Visual Quality Comparison for Large Multimodal Models: Methods and Results — http://arxiv.org/abs/2509.09190v1
[112] Human-Robot collaboration in surgery: Advances and challenges towards autonomous surgical assistants — http://arxiv.org/abs/2507.11460v1
[113] TRUST 2025: SCRITA and RTSS @ RO-MAN 2025 — http://arxiv.org/abs/2509.11402v1
[114] NTIRE 2025 Challenge on Image Super-Resolution (x4): Methods and Results — http://arxiv.org/abs/2504.14582v3
[115] The AudioMOS Challenge 2025 — http://arxiv.org/abs/2509.01336v1
[116] TDCOSMO 2025: Cosmological constraints from strong lensing time delays — http://arxiv.org/abs/2506.03023v4
[117] Event-Enriched Image Analysis Grand Challenge at ACM Multimedia 2025 — http://arxiv.org/abs/2508.18904v1
[118] PDHCG-II: An Enhanced Version of PDHCG for Large-Scale Convex QP — http://arxiv.org/abs/2602.23967v1
[119] Benchmarking Different QP Formulations and Solvers for Dynamic Quadrupedal Walking — http://arxiv.org/abs/2502.01329v1
[120] Romans massive QP manifolds — http://arxiv.org/abs/2201.07807v2
[121] Current Algebras and QP Manifolds — http://arxiv.org/abs/1108.0473v3
[122] EIQP: Execution-time-certified and Infeasibility-detecting QP Solver — http://arxiv.org/abs/2502.07738v2
[123] imuQP: An Inverse-Matrix-Updates-Based Fast QP Solver Suitable for Real-Time MPC — http://arxiv.org/abs/2503.03581v1
[124] Bridging the gap between QP-based and MPC-based RL — http://arxiv.org/abs/2205.08856v1
[125] Efficient QP-ADMM Decoder for Binary LDPC Codes and Its Performance Analysis — http://arxiv.org/abs/1910.12712v1
[126] ros2 fanuc interface: Design and Evaluation of a Fanuc CRX Hardware Interface in ROS2 — http://arxiv.org/abs/2506.14487v2
[127] A Method for Multi-Robot Asynchronous Trajectory Execution in MoveIt2 — http://arxiv.org/abs/2310.08597v1
[128] ROS2 Connect: A new ROS2 over WAN Solution — http://arxiv.org/abs/2608.25102v1
[129] Simplifying ROS2 controllers with a modular architecture for robot-agnostic reference generation — http://arxiv.org/abs/2601.08514v3
[130] Latency Analysis of ROS2 Multi-Node Systems — http://arxiv.org/abs/2101.02074v3
[131] FogROS2-SGC: A ROS2 Cloud Robotics Platform for Secure Global Connectivity — http://arxiv.org/abs/2306.17157v1
[132] Monitoring ROS2: from Requirements to Autonomous Robots — http://arxiv.org/abs/2209.14030v1
[133] Can Large Language Models Assist the Comprehension of ROS2 Software Architectures? — http://arxiv.org/abs/2604.21699v1


---

*Generated by research-bot · topic=`kinematics` · depth=`standard` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading · model=`deepseek-v4-flash` · sources=133 · duration=333s · 2026-10-05T22:46:48+00:00*
