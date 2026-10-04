# 机器人运动学、动力学与控制：证据地图与前沿调研报告

**日期**：2026-10-04（UTC） ｜ **领域**：Robotics — Kinematics / Dynamics / Control（FK/IK、旋量/POE、雅可比与奇异性、轨迹优化、全身控制、数值库） ｜ **检索源数量**：候选证据 116 条（编号 [1]–[116]）+ 领域种子资源 10 项（教材/项目/数据集，含链接）

> **证据质量前置警示（必读）**
> 1. **候选池主题召回精度偏低**：116 条候选块中，与本主题（机器人运动学/动力学/控制）直接相关的约为 40 条；其余分布于高能物理（hep-ex）、天体物理（astro-ph）、NLP 共享任务、图像/音频评测等，**不可用于本主题论断** [48][49][23][100][110][114]。
> 2. **同名实体陷阱**：[25][32] 的 "PINOCCHIO" 是天体物理中的暗物质晕合并史预测算法（PINpointing Orbit-Crossing Collapsed HIerarchical Objects），**与机器人动力学库 pinocchio 无关**，是本次检索中最典型的实体消歧错误。
> 3. **热度字段缺失**：本次候选块**未附带** `citations=` / `stars=` 等字段，因此下文中所有"热度证据"与"关注度"在无法从候选数据内部推导时，一律标注 `> 待核实`，**未编造任何引用数、star 数或榜单排名**。

---

## 摘要（Executive Summary）

本报告面向"机器人运动学、动力学与控制"的系统性证据地图，结论分三层：

**（1）可确证的前沿主线。** 2024–2026 年该方向真正发生的变化集中在四条线：
- **接触隐式轨迹优化（Contact-Implicit Trajectory Optimization, CITO）从"能解"走向"快速、可收敛、少调参"**：2024 年出现 SQP 全局收敛性分析 [81]，2026 年出现隐式 active-set 增广拉格朗日加速方法 IMPACT [79]；早期奠基链条为 2018 正交配点 [80]、2019 四足微型机器人 [78]、2020 免调参 [85]、2022 液弹接触 + iLQR [83]、2023 逆动力学 + MPC [84]、2023 分阶段 [82]。
- **可微分仿真与接触的"硬-软梯度"矛盾被正面处理**：2025 年工作指出 penalty 型仿真器（如 MuJoCo）通过软化接触来换取可微性，而真实硬接触需要高刚度，二者存在结构性张力 [94]。
- **全身控制（WBC）向实时化与任务优先级平滑切换演进**：2024 年 MPC-Path Integral 实时四足全身控制 [73]；2021 年递归层级投影方法处理任务优先级切换 [112]；人形平台侧出现遥操作 [12]、无机器人演示的全身操作 [13]、空间感知 + 可泛化动作小脑 [14]、羽毛球动态全身交互 [10]、真实世界策略自适应 [6]。
- **奇异位形下的 IK 与学习式 IK**：2024 年出现"解析信息引导的奇异点 IK" [107]；2025 年出现面向变长工具的自适应 IK 框架 [87]；学习式 IK 的早期代表为 2021 年面向模型失配的结构化预测方法 CRiSP [34]。

**（2）必须承认的证据缺口。** 子问题 q1（经典奠基/旋量理论）、q3（Pinocchio/Drake/MuJoCo/KDL/TRAC-IK/cuRobo 对比）、q6（解析解 vs 数值解争议、学习式 IK 安全保证、真机实时性口径）的候选证据**几乎全军覆没**：q6 的 6 条候选块与本主题**零重叠** [100][23][110][111][113][114]。因此本报告对这三个子问题以"种子资源 + 明确缺口标注"方式作答，**不以推测替代证据**。

**（3）一句话判断。** 该方向当前的真前沿不是"新 FK/IK 算法"本身，而是**经典运动学/动力学结构（POE、SE(3)、任务空间、接触模型）如何被嵌入可微分优化、学习策略与实时全身控制器**；而"解析 vs 数值 IK""奇异性与冗余度""学习式 IK 的安全保证"这三个经典争议点，在本次证据池中**未被覆盖**，属于本报告的显式开放缺口。

**子问题覆盖度自评表**

| 子问题 | 候选块数 | 主题相关块数 | 覆盖度 | 关键缺口 |
|---|---|---|---|---|
| q1 经典奠基/旋量/POE/操作空间 | 6 | 2–3（[57][58][59]） | 低 | 无 POE/DH 的一手对比证据 |
| q2 2024–2026 前沿 | 6 | 5（[6][10][12][13][14]） | 中高 | 缺可微分运动学一手证据 |
| q3 开源生态对比 | 6 | 1（[34]） | 极低 | 零性能/维护度证据；PINOCCHIO 同名混淆 [25][32] |
| q4 数据/基准/评测 | 6 | 6（[79][86][87][90][91][11]） | 中 | 缺统一评测协议一手文档 |
| q5 轨迹优化/接触/MPC | 6 | 3（[79][94][10]） | 中 | 缺真机可行性边界数据 |
| q6 开放问题与争议 | 6 | **0** | **零** | 全部五个子议题均未覆盖 |

---

## 一、关键前沿进展（近 1–2 年，2024–2026）

### 1.1 接触隐式轨迹优化：收敛性与速度的双重攻坚

| 条目 | 时间 | 一句话贡献 | 证据 |
|---|---|---|---|
| Global Convergence of an SQP Method for CITO | 2024 | 为接触隐式轨迹优化的 SQP 方法给出全局收敛性分析，回应"每次求解是否可靠"的核心质疑 | [81] |
| IMPACT: Implicit Active-Set Augmented Lagrangian | 2026 | 用隐式 active-set 增广拉格朗日实现快速 CITO，目标是在无需预设接触模式序列的前提下提升求解速度 | [79] |
| Differentiable Simulation of Hard Contacts with Soft Gradients | 2025 | 直指 penalty 型仿真器（如 MuJoCo）"软化接触换梯度"与"硬接触需高刚度"的根本矛盾，面向学习与控制提供折中方案 | [94] |

- **热度证据**：`> 待核实`（候选块未提供 citations/stars）。**权威证据**：均为 arXiv 预印本（cs.RO），是否已中稿 `> 待核实` [79][81][94]。**关注度**：中——依据是 [79] 在 q4 与 q5 两个子问题中被重复命中，属候选池内部的弱交叉信号；`> 待核实` 更强信号。**推荐度**：★★★★☆——若关注接触优化工程落地，[79][81][94] 是当前证据池中唯一成体系的一组。
- **技术脉络**：2018 正交配点 [80] → 2019 四足微型机器人接触隐式轨迹 [78] → 2020 免调参 CITO [85] → 2022 液弹接触 + iLQR [83] → 2023 分阶段（staged）混合优化 [82]、逆动力学 CITO-MPC [84] → 2024 全局收敛 [81] → 2026 IMPACT [79]。

### 1.2 全身控制与人形机器人：实时性与任务优先级

- **实时 WBC**：2024 年将 Model-Predictive Path Integral Control 用于腿足机器人实时全身控制 [73]。**权威证据**：arXiv 预印本 [73]；**热度证据** `> 待核实`；**关注度** `> 待核实`；**推荐度** ★★★★☆（实时 WBC 是 WBC 落地的核心瓶颈）。
- **任务优先级切换**：2021 年提出 Recursive Hierarchical Projection，显式处理全身控制中任务优先级切换的连续性/一致性 [112]。这直接对应"优先级跳变导致控制抖动"的工程痛点。**推荐度** ★★★★☆。
- **人形全身操作与交互（2025–2026）**：CHILD 支持人形**全身关节级遥操作** [12]；Humanoid Manipulation Interface 主张**无需机器人本体**的演示采集以规避硬件物流与复杂奖励工程 [13]；另有空间感知 + 可泛化动作小脑的两段式架构 [14]；羽毛球动态全身交互通过退火 RL 课程获得统一全身策略 [10]；Robot Trains Robot 让机器人在真实世界自动适应与学习 [6]。**关注度**：中——[10] 在 q2 与 q5 中重复命中，候选池内部存在交叉信号；其余 `> 待核实`。**推荐度**：★★★★☆（[13][14] 对本主题中"全身性"与"任务空间接口"的关联最直接）。
- **相邻支撑**：[11] 研究域随机化在全身人形扩散策略训练中的作用（2024）；[17] 用层级世界模型作为视觉全身人形控制器（2024）；[15] 跨姿态人形起身控制（2025）。

### 1.3 表示与等变性：SE(3) 进入策略学习

- [18] 在球面傅里叶空间中构造 SE(3)-等变扩散策略（2025）；[22] ET-SEED 实现轨迹层级的 SE(3) 等变扩散策略（2024）；[19] 用 SE(3) 等变性学习 3D 几何形状装配（2023）。
- **意义**：这说明**李群/旋量式几何表示正在从"运动学建模工具"外溢为"策略网络的归纳偏置"**——是 POE 数学框架在基础模型时代最直接的延伸方向。**权威证据**：arXiv 预印本 [18][19][22]；**热度证据** `> 待核实`；**推荐度** ★★★★☆。

### 1.4 运动学感知的策略与可操作度评估

- [90] 提出运动学感知扩散策略，强调**仅考虑末端位姿不足**，需覆盖全臂运动学以支持本体避障与本体-物体交互（2025）。
- [71] 提出伪椭球（Pseudo-Ellipsoid）方法，提升可操作度（manipulability）评估的鲁棒性（2024）；其前身为 [67] 的几何感知可操作度学习/跟踪/迁移（2018）与 [68] 的人体运动可操作度迁移（2020），数学工具层面可回溯到多维离散数据的椭球拟合 [70]（2019）。

### 1.5 学习式数值求解器与安全约束

- [99] 用自监督方式学习**约束优化的迭代求解器**（2024）——这是"学习替代数值优化内循环"的直接尝试。
- [95] 通过控制屏障函数（CBF）处理带状态约束的反馈优化（2025）；[96] 将 CBF 用于共享控制与车辆安全（2025）。**注意**：[95][96] 的安全保证面向一般非线性控制与车辆场景，**不能直接等同于机械臂 IK 的安全保证**，迁移性 `> 待核实`。

---

## 二、建模表示：DH 参数 vs 旋量/POE

**本节结论强度受限**：候选证据池中**没有任何一条**是关于 DH 与 POE 的一手对比研究，因此以下内容以种子教材为骨架，其余为标注缺口的结构性说明。

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| A Mathematical Introduction to Robotic Manipulation | 1994 | Murray, Li, Sastry（Caltech） | `> 待核实` | 经典教材，官方 wiki 页面 | `> 待核实` | ★★★★★ | https://www.cds.caltech.edu/~murray/mlswiki/ | 旋量理论与指数积（POE）公式的奠基性教材；POE 用螺旋轴 + 指数映射统一描述串联机构 FK |
| Modern Robotics: Mechanics, Planning, and Control | 2017 | Lynch & Park（Northwestern） | `> 待核实` | 教材，作者官方页面 | `> 待核实` | ★★★★★ | http://hades.mech.northwestern.edu/index.php/Modern_Robotics | 以旋量/POE 为主线重构现代运动学与控制，含配套代码与课程 |

**可确证的关联证据：**

- **流形/李群上的控制设计**：[57] 提出把状态流形 $M$ 嵌入欧氏空间 $\mathbb{R}^n$、在环境空间中扩展系统并在外部修正控制器的方法（2018）。这为"为什么应在流形上而非局部坐标（如 Euler 角/DH 局部参数）上做控制"提供了方法论支撑。**权威证据**：arXiv（math.OC）预印本 [57]；**热度证据** `> 待核实`；**推荐度** ★★★★☆。
- **欧拉角本身的固有困难**：[30] 讨论刚体绕定点转动在 Euler 角下的不变运动（广义 Euler 情形）（2016）。可作为"局部角度参数化存在表示奇异性"的侧面证据，但**该文属 physics.gen-ph**，与机器人学惯例不完全一致，**引用时须限定**。`> 待核实`
- **表示选择向学习侧外溢**：SE(3) 等变策略 [18][22] 表明，选择 POE/李群式表示而非局部角度表示，在数据效率与泛化上具有可检验收益（具体量化结论需回原文核对，本报告未获得其数值表）。`> 待核实`

**开放争议（本报告未能证实，仅登记为问题）**：
- DH 参数与 POE 在**数值条件数、奇异位形附近的参数连续性、对平行轴/近奇异构型的鲁棒性**上是否存在系统性差异？——`> 待核实`，本次证据池无一手对比数据。
- 主流库是否已统一到 POE/MDH 混合建模？——`> 待核实`（见第七章）。

---

## 三、逆运动学：解析解 / 数值解 / 学习式

### 3.1 解析与半解析路线

| 条目 | 年份 | 一句话贡献 | 证据 |
|---|---|---|---|
| Analytically Informed Inverse Kinematics Solution at Singularities | 2024 | 标题即表明其针对**奇异位形**下的 IK，引入解析信息来改善数值求解（仅获标题，方法与实验 `> 待核实`） | [107] |
| An Efficient Multi-solution Solver for the IK of 3-Section Constant-Curvature Robots | 2023 | 面向 3 段常曲率连续体机器人给出**多解高效求解器**，对应连续体/超冗余机构的解析-半解析路线（仅获标题） | [39] |

- **热度证据** `> 待核实`；**权威证据**：arXiv 预印本 [107][39]，是否中稿 `> 待核实`；**关注度** `> 待核实`；**推荐度**：[107] ★★★★☆（奇异点 IK 是经典未解区域的直接攻击）；[39] ★★★☆☆（连续体机器人，与串联刚性臂相关性中等）。

### 3.2 学习式 IK 与"模型失配"

| 条目 | 年份 | 一句话贡献 | 证据 |
|---|---|---|---|
| Structured Prediction for CRiSP Inverse Kinematics Learning with Misspecified Robot Models | 2021 | 明确以**机器人模型失配**为前提，用结构化预测学习 IK，而非假设精确模型 | [34] |
| Adaptive Inverse Kinematics Framework for Learning Variable-Length Tool Manipulation | 2025 | 指出传统机器人对自身运动学理解有限、受限于预编程任务；提出自适应 IK 框架以支持变长工具操作 | [87] |

- **权威证据**：arXiv 预印本 [34][87]；**热度证据** `> 待核实`；**关注度** `> 待核实`；**推荐度**：[34] ★★★★☆（"模型失配 + 结构化预测"是学习式 IK 的关键问题设定）；[87] ★★★★☆（面向工具使用，与可变运动学链的实际需求对齐）。

### 3.3 运动学不确定下的控制（连接 IK 与控制的桥梁）

- [59] 针对**运动学与动力学同时不确定**的机械臂，提出两种自适应控制方案以实现任务空间轨迹跟踪（2014）。这在逻辑上等价于"**把 IK 的误差吸收进闭环控制**"，是处理解析 IK 不可得/模型不准的经典范式。
- **权威证据**：arXiv 1403.5204，正式发表 venue `> 待核实`；**热度证据** `> 待核实`；**推荐度** ★★★★☆（对 q6 "解析 vs 数值"之争给出了第三条路：不精确求解，改为鲁棒/自适应闭环）。

### 3.4 本节缺口（关键）

- 解析 IK 与数值 IK 在**精度、速度、可微性、多解选择**上的定量对比：**本次证据池无任何材料** `> 待核实`。
- 奇异点规避的工程手段（DLS / 阻尼最小二乘 / 零空间投影）在**真机上的实际表现**：**无材料** `> 待核实`。
- 学习式 IK 的**分布外泛化边界与安全保证**（安全层、可达性约束、失败检测）：**无材料** `> 待核实`。

---

## 四、轨迹规划与最优控制

### 4.1 接触隐式轨迹优化（CITO）谱系（本节证据最完整）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Contact-Implicit Trajectory Optimization using Orthogonal Collocation | 2018 | — | `> 待核实` | arXiv 预印本（cs.RO） | `> 待核实` | ★★★★☆ | http://arxiv.org/abs/1809.06436v3 | 正交配点法用于 CITO，奠基性求解策略 [80] |
| Contact-Implicit Optimization of Locomotion Trajectories for a Quadrupedal Microrobot | 2019 | — | `> 待核实` | arXiv 预印本 | `> 待核实` | ★★★☆☆ | http://arxiv.org/abs/1901.09065v1 | 把 CITO 落到微型四足平台 [78] |
| Tuning-Free Contact-Implicit Trajectory Optimization | 2020 | — | `> 待核实` | arXiv 预印本 | `> 待核实` | ★★★★☆ | http://arxiv.org/abs/2006.06176v1 | 直击 CITO"难调参"的可用性痛点 [85] |
| CITO with Hydroelastic Contact and iLQR | 2022 | — | `> 待核实` | arXiv 预印本 | `> 待核实` | ★★★★☆ | http://arxiv.org/abs/2202.13986v2 | 液弹接触模型 + iLQR，改善接触力建模与求解 [83] |
| Staged Contact Optimization | 2023 | — | `> 待核实` | arXiv 预印本 | `> 待核实` | ★★★★☆ | http://arxiv.org/abs/2304.04923v2 | 融合接触隐式与多阶段混合轨迹优化 [82] |
| Inverse Dynamics Trajectory Optimization for Contact-Implicit MPC | 2023 | — | `> 待核实` | arXiv 预印本 | `> 待核实` | ★★★★★ | http://arxiv.org/abs/2309.01813v3 | 逆动力学 + CITO-MPC，向实时控制靠拢 [84] |
| Global Convergence of an SQP Method for CITO | 2024 | — | `> 待核实` | arXiv 预印本 | `> 待核实` | ★★★★★ | http://arxiv.org/abs/2406.01763v5 | 全局收敛性分析，理论保证 [81] |
| IMPACT: Implicit Active-Set Augmented Lagrangian for Fast CITO | 2026 | — | `> 待核实` | arXiv 预印本 | 中（跨 q4/q5 重复命中） | ★★★★★ | http://arxiv.org/abs/2605.09127v3 | 当前证据池中最新的 CITO 加速工作 [79] |

### 4.2 MPC 与最优控制的一般框架

- [58] 系统综述了非线性约束系统**动态运行**（跟踪参考信号 → 经济型运行）的 MPC 框架设计与分析（2023）。**权威证据**：arXiv（eess.SY）综述；**热度证据** `> 待核实`；**推荐度** ★★★★☆（WBC/轨迹优化的通用方法论入口）。
- [37] 从**不完整轨迹观测**中做逆最优控制（2018），对应"从演示中恢复代价函数"这一与模仿学习直接相关的问题。**推荐度** ★★★☆☆。

### 4.3 特定平台的轨迹规划

- [38] 自由漂浮空间机器人的**最优预设时间轨迹规划**（2020）——非固定终端时间的规划问题，与非完整/欠驱动系统相关。**推荐度** ★★★☆☆。
- [40] 非完整球形机器人方向与轨迹跟踪控制：滑模控制器 + 模型预测控制器组合（2022）。**推荐度** ★★★☆☆。

### 4.4 可微分仿真与接触梯度

- [94]（2025）明确指出：接触力在机器人动力学中引入不连续性，严重限制仿真器用于基于梯度的优化；penalty 型仿真器（如 MuJoCo）通过软化接触分辨率换取梯度可计算性，但要真实模拟硬接触又需要高刚度 [94]。这是**可微分仿真在接触场景的核心张力**，也是 CITO 与可微 RL 的公共瓶颈。**推荐度** ★★★★★。

### 4.5 本节真机可行性边界

- 证据池提供了方法层面的进展 [79][81][83][84][94]，但**未提供**任何真机控制频率、端到端延迟、算力平台或成功率口径的量化数据。**"真机可行性边界"在本轮证据中不可回答** `> 待核实`。

---

## 五、全身控制与任务空间控制

### 5.1 任务空间控制的奠基与延伸

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Task Space Control / Operational Space Formulation | 1987 | Oussama Khatib | `> 待核实` | IEEE J. Robotics and Automation（DOI 可查） | `> 待核实` | ★★★★★ | https://doi.org/10.1109/JRA.1987.1087109 | 操作空间控制奠基：把任务描述在末端操作空间，通过动力学一致映射实现解耦控制 |
| Prioritized motion-force control of constrained fully-actuated robots: "Task Space Inverse Dynamics" | 2014 | — | `> 待核实` | arXiv 预印本（正式发表 `> 待核实`） | `> 待核实` | ★★★★★ | http://arxiv.org/abs/1410.3863v1 | TSID：把任务优先级、运动-力混合控制统一在任务空间逆动力学框架下 [35] |
| Recursive Hierarchical Projection for WBC with Task Priority Transition | 2021 | — | `> 待核实` | arXiv 预印本 | `> 待核实` | ★★★★☆ | http://arxiv.org/abs/2109.07236v2 | 递归层级投影，解决任务优先级切换的不连续问题 [112] |
| Real-Time Whole-Body Control of Legged Robots with Model-Predictive Path Integral Control | 2024 | — | `> 待核实` | arXiv 预印本 | `> 待核实` | ★★★★☆ | http://arxiv.org/abs/2409.10469v1 | 以 MPPI 实现腿足机器人实时 WBC [73] |

**结构判断**：从 1987 的 Khatib 操作空间控制，到 2014 的 TSID 优先级框架 [35]，再到 2021 的递归层级投影 [112]，**"任务优先级如何在保持连续性前提下切换"是贯穿近 40 年的核心工程议题**；2024 年的实时 MPPI-WBC [73] 则代表采样式/概率式求解器进入实时全身控制环路。

### 5.2 人形全身控制的 2024–2026 进展

- **遥操作与演示接口**：[12] 支持全身关节级人形遥操作；[13] 走"无机器人演示"路线以规避硬件与奖励工程成本。**推荐度** ★★★★☆。
- **层级/解耦架构**：[14] 提出"主动空间大脑 + 可泛化动作小脑"两段式结构，分别应对 3D 空间理解与动作泛化。**推荐度** ★★★★☆。
- **动态交互**：[10] 通过退火 RL 课程得到统一全身策略，用于羽毛球这类快速移动物体的交互。**推荐度** ★★★★☆。
- **真实世界自适应**：[6] 让机器人在真实世界自动适应与学习，直指"仿真 RL 到真机适配"的瓶颈。**推荐度** ★★★★☆。
- **训练侧要素**：[11] 分析域随机化在全身人形扩散策略训练中的作用。**推荐度** ★★★☆☆。
- **交叉支撑**：[15] 跨姿态起身；[17] 层级世界模型作为视觉全身控制器。

### 5.3 全身操作中的运动学感知

- [90]（2025）的核心论断具有直接的本主题价值：**全身/全臂操作的策略学习不能只依赖末端位姿**，需在全臂运动学层面保持一致 3D 观测与动作空间，才能处理本体避障与本体-物体交互 [90]。这是"运动学表示重新回到策略设计中心"的最清晰证据。**推荐度** ★★★★☆。

### 5.4 本节缺口

- 零空间优化目标（关节限位、避障、姿态保持）与学习式策略的结合：**证据池无材料** `> 待核实`。
- 奇异性处理（DLS、任务优先级/零空间投影）在真机上的实际表现对比：**证据池无材料** `> 待核实`。

---

## 六、经典教材与奠基工作

**说明**：本节包含两类来源——(a) 领域种子资源（教材/奠基论文，链接已保留）；(b) 候选证据池中可核查的早期关键论文。**两者均未提供引用数或 star 数，热度与关注度统一标注 `> 待核实`。**

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| A Mathematical Introduction to Robotic Manipulation | 1994 | Murray, Li, Sastry | `> 待核实` | 经典教材（Caltech 官方 wiki） | `> 待核实` | ★★★★★ | https://www.cds.caltech.edu/~murray/mlswiki/ | 旋量理论 / POE 公式奠基 |
| Modern Robotics | 2017 | Lynch & Park | `> 待核实` | 教材（作者官方页面） | `> 待核实` | ★★★★★ | http://hades.mech.northwestern.edu/index.php/Modern_Robotics | 现代运动学/规划/控制统一教材 |
| Operational Space Formulation | 1987 | Khatib | `> 待核实` | IEEE J. Robotics and Automation（DOI） | `> 待核实` | ★★★★★ | https://doi.org/10.1109/JRA.1987.1087109 | 任务空间控制奠基 |
| Adaptive Control of Robot Manipulators With Uncertain Kinematics and Dynamics | 2014 | — | `> 待核实` | arXiv 预印本 [59] | `> 待核实` | ★★★★☆ | http://arxiv.org/abs/1403.5204v3 | 运动学+动力学双不确定下的任务空间跟踪 |
| Task Space Inverse Dynamics (TSID) | 2014 | — | `> 待核实` | arXiv 预印本 [35] | `> 待核实` | ★★★★★ | http://arxiv.org/abs/1410.3863v1 | 优先级运动-力控制统一框架 |
| On Controller Design for Systems on Manifolds in Euclidean Space | 2018 | — | `> 待核实` | arXiv（math.OC）[57] | `> 待核实` | ★★★★☆ | http://arxiv.org/abs/1807.03475v1 | 流形系统在欧氏空间中的控制器设计 |
| Geometry-aware Manipulability Learning, Tracking and Transfer | 2018 | — | `> 待核实` | arXiv 预印本 [67] | `> 待核实` | ★★★★☆ | http://arxiv.org/abs/1811.11050v5 | 可操作度作为几何量学习/跟踪/迁移 |
| Direct ellipsoidal fitting of discrete multi-dimensional data | 2019 | — | `> 待核实` | arXiv 预印本 [70] | `> 待核实` | ★★★☆☆ | http://arxiv.org/abs/1901.05511v3 | 可操作度椭球估计的数学工具 |
| Analysis and Transfer of Human Movement Manipulability in Industry-like Activities | 2020 | — | `> 待核实` | arXiv 预印本 [68] | `> 待核实` | ★★★☆☆ | http://arxiv.org/abs/2008.01402v2 | 人体可操作度向工业任务的迁移 |
| Structured Prediction for CRiSP IK with Misspecified Robot Models | 2021 | — | `> 待核实` | arXiv 预印本 [34] | `> 待核实` | ★★★★☆ | http://arxiv.org/abs/2102.12942v3 | 模型失配下的学习式 IK |
| Recursive Hierarchical Projection for WBC | 2021 | — | `> 待核实` | arXiv 预印本 [112] | `> 待核实` | ★★★★☆ | http://arxiv.org/abs/2109.07236v2 | 任务优先级平滑切换 |
| Crocoddyl: Multi-Contact Optimal Control | 2020 | LAAS-CNRS | `> 待核实` | arXiv 预印本（arXiv:1909.04947） | `> 待核实` | ★★★★★ | https://arxiv.org/abs/1909.04947 | 多接触最优控制框架，DDP 家族代表实现 |
| Enhancing Robustness in Manipulability Assessment: The Pseudo-Ellipsoid Approach | 2024 | — | `> 待核实` | arXiv 预印本 [71] | `> 待核实` | ★★★★☆ | http://arxiv.org/abs/2412.18869v2 | 可操作度评估鲁棒性的最新推进 |

**未纳入的经典候选（本次检索无证据）**：Luh–Walker–Paul 的解析 IK 分治、Yoshikawa 可操作度度量、Nakamura 冗余度解析、Featherstone 刚体动力学算法（ABA/CRBA）、Liegeois 零空间梯度投影等——**全部标注 `> 待核实`，本轮未取得可引用来源**，不应据此引用。

---

## 七、开源库与工具链对比

**强烈的证据警示**：子问题 q3 的候选块**没有一条**提供了任何运动学库的性能数据、维护活跃度或 star 数；其中 [25][32] 更是天体物理同名论文。因此下表**只能给出定位与链接，性能/维护度一栏全部为 `> 待核实`**。

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| stack-of-tasks/pinocchio | `> 待核实` | LAAS-CNRS 等 | `> 待核实` | 官方 GitHub 仓库 | `> 待核实` | ★★★★★ | https://github.com/stack-of-tasks/pinocchio | 刚体运动学/动力学，含解析导数（可微分接口） |
| orocos/orocos_kinematics_dynamics (KDL) | `> 待核实` | Orocos 社区 | `> 待核实` | 官方 GitHub 仓库 | `> 待核实` | ★★★★☆ | https://github.com/orocos/orocos_kinematics_dynamics | FK/IK/Jacobian 基础实现，ROS 生态长期依赖 |
| RobotLocomotion/drake | `> 待核实` | Toyota Research / MIT | `> 待核实` | 官方 GitHub 仓库 | `> 待核实` | ★★★★★ | https://github.com/RobotLocomotion/drake | 优化与控制的 C++ 工具箱（含数学程序与系统框架） |
| loco-3d/crocoddyl | `> 待核实` | LAAS-CNRS | `> 待核实` | 官方 GitHub 仓库 | `> 待核实` | ★★★★★ | https://github.com/loco-3d/crocoddyl | 多接触最优控制（配套论文 [Crocoddyl]） |
| moveit/moveit2 | `> 待核实` | MoveIt 社区 | `> 待核实` | 官方 GitHub 仓库 | `> 待核实` | ★★★★★ | https://github.com/moveit/moveit2 | ROS2 运动规划框架（IK 插件宿主） |
| MuJoCo | `> 待核实` | — | `> 待核实` | 相对新颖的引用：[94] 将其描述为 penalty 型、软化接触分辨率以支持梯度计算 | `> 待核实` | ★★★★☆ | `> 待核实`（本次未取得官方链接引用） | 仅能确证"penalty 型仿真器"这一技术定位 [94] |
| NVIDIA cuRobo | `> 待核实` | — | `> 待核实` | **本次候选池无任何证据** | `> 待核实` | `> 待核实` | `> 待核实` | 无法给出任何可核查论断 |
| TRAC-IK | `> 待核实` | — | `> 待核实` | **本次候选池无任何证据** | `> 待核实` | `> 待核实` | `> 待核实` | 无法给出任何可核查论断 |
| HumanoidBench（基准，兼工具链） | 2024 | — | `> 待核实` | arXiv 预印本 [72] | `> 待核实` | ★★★★☆ | http://arxiv.org/abs/2403.10506v2 | 全身运动与操作的仿真基准 |
| NimbRo-OP ROS 软件框架 | 2018 | — | `> 待核实` | arXiv 预印本 [16] | `> 待核实` | ★★★☆☆ | http://arxiv.org/abs/1809.11051v1 | 人形开放平台的 ROS 软件框架，属工程实践类证据 |
| 学习式迭代求解器 | 2024 | — | `> 待核实` | arXiv 预印本 [99] | `> 待核实` | ★★★★☆ | http://arxiv.org/abs/2409.08066v3 | 自监督学习约束优化迭代求解器，可视为"数值内核"的新路线 |

**取舍建议（基于现有证据，非基于性能数据）**：
1. 若任务需要**解析导数/可微分运动学**（如 CITO、可微 RL、梯度优化），[pinocchio] 的定位与 [79][81][94] 的方法需求方向一致；**但具体性能对比 `> 待核实`**。
2. 若任务涉及**多接触最优控制**，[crocoddyl] 与 [79][81][83][84] 的方法谱系同源；**但"哪个更快"本轮无法回答**。
3. **不要**引用 [25][32] 作为 pinocchio 库的证据（同名陷阱）。

---

## 八、开放问题与关注清单

### 8.1 本轮证据**显式未覆盖**的五个开放问题（直接取自 q6 的缺口登记）

1. **解析解 vs 数值解的取舍依据**（精度 / 速度 / 可微性 / 多解选择）——`> 待核实`，需专门检索 [34][107] 的引用网络与方法对比表。
2. **奇异性规避**（DLS、阻尼最小二乘、任务优先级/零空间投影）在**真机上的实际表现**——`> 待核实`；仅有 [107] 从方法层面对奇异点 IK 作出回应。
3. **冗余机械臂的零空间优化目标**（关节限位、避障、姿态保持）及其与学习式策略的结合——`> 待核实`；仅 [90] 从"策略需感知全臂运动学"角度间接触及。
4. **学习式 IK/策略的分布外泛化边界与安全保证**（安全层、可达性约束、失败检测）——`> 待核实`；[34][87] 提供问题设定，[95][96] 提供 CBF 工具，但**二者之间的桥接证据缺失**。
5. **真机实时性约束下的指标口径**（控制频率、端到端延迟、算力平台）——`> 待核实`；[73] 的标题含 "Real-Time"，但本报告未取得其延迟/频率数值。

### 8.2 可确证的真问题 vs 已明显推进的问题

| 议题 | 状态判断 | 依据 |
|---|---|---|
| CITO 的求解可靠性 | **正在被解决**：从经验调参走向收敛性保证与更快的 active-set 方法 | [81][79][85] |
| 接触梯度不可微 | **真问题、被正面攻击**：硬接触 vs 软梯度的结构性矛盾已被明确表述 | [94] |
| 任务优先级切换的连续性 | **已有可用方案**（递归层级投影），是否成为共识 `> 待核实` | [112] |
| 全身操作中"只看末端位姿"的不足 | **已被识别并给出方向**（全臂运动学一致的动作/观测空间） | [90] |
| 可操作度评估的鲁棒性 | **持续演进**：从几何感知学习到伪椭球方法 | [67][71] |
| 解析 vs 数值 IK 之争 | **本轮不可判定**：证据为零 | `> 待核实` |
| 学习式 IK 的安全保证 | **本轮不可判定**：证据为零 | `> 待核实` |

### 8.3 Watchlist（值得持续关注）

- **接触优化求解器**：IMPACT [79] 与其后续引用/复现；正交配点 [80] → SQP 收敛 [81] 的理论线索是否延伸到时变接触。
- **可微分接触仿真**：[94] 的"软梯度硬接触"方案能否进入真机在线优化环路。
- **人形全身操作接口**：[13] 的"无机器人演示"范式与 [12] 的关节级遥操作在数据成本上的取舍；[14] 的双模块架构是否可复用到非人形平台。
- **运动学感知策略**：[90] 提出的全臂一致观测/动作空间，能否与 SE(3) 等变策略 [18][22] 结合。
- **学习式数值内核**：[99] 自监督迭代求解器在 IK/QP 内循环上的替代潜力。
- **相邻压力源**：大规模真机轨迹数据驱动的 VLA/具身模型 [33] 会持续对底层运动学接口（动作空间、IK 可微性、实时性）提出新要求。
- **教程级入口**：[7] Robot Learning: A Tutorial（2025）可作为跨领域读者的当前状态导览。

### 8.4 下一次调研必须补齐的检索动作（给后续 Agent）

1. 直接检索 `screw theory vs Denavit-Hartenberg comparison`、`product of exponentials singularity robustness`，补齐第二章；
2. 检索 `TRAC-IK benchmark`、`cuRobo benchmark`、`pinocchio vs KDL performance`，并用 **GitHub API 取

## 二、建模表示：DH vs 旋量/POE

> **本章证据声明**：DH 参数与指数积（POE, Product of Exponentials）的数学框架属于教科书级共识，本轮检索到的可引用编号 [n] 中**没有直接讨论这两种表示对比的一手论文**。因此本节 2.1–2.2 的对比性论断按方法论以「教科书共识 + 人工维护种子资源」呈现，并逐条标记 `> 待核实`；2.3 给出本轮确有 [n] 证据的相关线索。

### 2.1 两种表示的定位（教科书级共识，待核实）

- **DH 参数（Denavit–Hartenberg parameters）**：用 4 个连杆参数（$a,\alpha,d,\theta$）描述相邻连杆坐标系之间的齐次变换，是前向运动学（FK, forward kinematics）最广为人知的最小参数化形式；其优点是参数少、便于手写推导与工业标定，代价是坐标系约定强、相邻平行/相交轴处易出现参数退化与奇异性。
  - 热度：`> 待核实`；权威：经典教材级共识，见种子资源 Murray/Li/Sastry (1994) 与 Lynch & Park (2017)；关注度：高（几乎所有机器人教材与 URDF/工业控制器都以此教学）；推荐度：★★★★☆（入门必备，但在 SE(3) 理论推导与可微优化中不如 POE 一致）。
  - 链接（人工维护种子，本轮未实时核验）：<https://www.cds.caltech.edu/~murray/mlswiki/>、<http://hades.mech.northwestern.edu/index.php/Modern_Robotics>
- **旋量 / 指数积（screw theory / POE）**：把每个关节建模为螺旋轴 $\xi_i \in \mathfrak{se}(3)$ 上的指数映射 $\exp(\hat\xi_i\theta_i)$，FK 写成有序乘积；其优点是直接用**全局坐标系**描述、无需为每个连杆挑选坐标系、对所有关节类型（转动/移动/螺旋）统一处理，且天然承接李群/李代数工具（Jacobian、可微展开、等价刚体变换）。
  - 热度：`> 待核实`；权威：经典教材级共识（同上种子资源，Murray–Li–Sastry 为 POE 体系的奠基教材）；关注度：高（现代运动学教材与基于优化的控制框架普遍采用）；推荐度：★★★★★（做可微运动学、轨迹优化与全身控制的推荐主干表示）。
  - 链接：同上。

### 2.2 对比速览（要点精炼，均标 `> 待核实`）

| 维度 | DH 参数 | 旋量 / POE |
|---|---|---|
| 参数最小性 | 最小参数化，参数少 | 冗余（每关节 6 维螺旋轴），但可用规范形式约束 |
| 全局描述一致性 | 需为每连杆定义坐标系，基座/工具系变化需重推 | 以 SE(3) 全局描述，基座/末端系变化只改变一个常量变换 |
| 奇异/退化参数 | 平行或相交轴附近参数退化 | 无参数化奇异（奇异来自机构本身，而非表示） |
| 与 SE(3)/李代数工具衔接 | 需额外转换 | 天然衔接，便于求导与可微实现 |
| 教学与工业惯性 | 极高（教材、标定、老式控制器） | 上升（现代教材与优化型框架） |

> 上表所有条目均 `> 待核实`：本轮未检索到可核查的一手对比实验或综述 [n]。

### 2.3 本轮有 [n] 证据的相关线索

1. **表示/局部几何与奇异性的纠缠仍未解决。** [71] 提出用「伪椭球（Pseudo-Ellipsoid）」方法增强可操作度（manipulability）评估的鲁棒性，直接回应传统可操作度椭球在奇异性附近退化的老问题。
   - 热度：`> 待核实` [71]；权威：arXiv 预印本（cs.RO），未见同行评审信息 [71]；关注度：`> 待核实`（无引用/榜单数据可查）[71]；推荐度：★★★☆☆（若你做可操作度指标或冗余度优化，值得一读；但尚无第三方复现证据）[71]。
2. **奇异性处的解析信息仍是建模表示选择的试金石。** [107] 明确以「Analytically Informed Inverse Kinematics Solution at Singularities」为题，说明奇异位形下纯数值迭代失效、需注入解析/几何信息，这直接指向「表示选择影响奇异处理」的论点。
   - 热度：`> 待核实` [107]；权威：arXiv 预印本（cs.RO）[107]；关注度：`> 待核实` [107]；推荐度：★★★★☆（与本章「POE 无参数化奇异但机构奇异仍在」的论点高度相关）[107]。
3. **表示选择会向下游控制栈传播。** [112] 的递归层次投影（Recursive Hierarchical Projection）面向任务优先级切换的全身控制，其可用性依赖一个能一致表达任务栈与零空间投影的运动学/动力学模型。
   - 热度：`> 待核实` [112]；权威：arXiv 预印本（cs.RO）[112]；关注度：`> 待核实` [112]；推荐度：★★★☆☆（对冗余度/优先级建模有直接方法论价值）[112]。
4. **表示选择也进入了学习式流水线。** [90] 提出「运动学感知（Kinematics-Aware）」的扩散策略，把整臂运动学一致性写入观测与动作空间，说明 SE(3)/运动学表示不再只是经典控制专属问题。
   - 热度：`> 待核实` [90]；权威：arXiv 预印本（cs.RO）[90]；关注度：`> 待核实` [90]；推荐度：★★★☆☆（为「表示如何影响策略泛化」提供 2025 年样本）[90]。

**本章结论（含不确定性）**：DH 与 POE 的选择在数学上主要是**参数化 vs 全局描述**的取舍，POE 与 SE(3)/李代数工具链的契合度更好；但「哪种表示在真机上带来可量化收益」本轮**未有 [n] 级证据支持**，`> 待核实`。

---

## 三、逆运动学：解析 / 数值 / 学习

> 本章可用的直接 [n] 证据为 [107]（奇异性处解析引导 IK）、[39]（连续体多解求解器）、[34]（模型失配下的学习式 IK）、[87]（学习式自适应 IK）、[90]（运动学感知策略）；关于 DLS/Gauss-Newton/零空间投影等**教科书级算法本体**，本轮无可核查 [n]，按 `> 待核实` 处理。

### 3.1 三条技术路线的定位（含 [n] 证据）

- **解析解（analytic / closed-form IK）**：仅在满足特定几何条件（如 Pieper 型三轴相交腕部）时存在封闭解；优点是求解快、可枚举多解，缺点是与机构强绑定、奇异位形处退化。`> 待核实`（本轮无直接 [n] 讨论 Pieper 条件的论文）。**与之相关的可核查线索**：[107] 针对**奇异位形**给出解析信息引导的 IK 解，说明解析手段在奇异邻域仍具价值。
  - 热度：`> 待核实` [107]；权威：arXiv 预印本（cs.RO），未见同行评审信息 [107]；关注度：`> 待核实` [107]；推荐度：★★★★☆（奇异点是解析/数值分界的经典痛点）[107]。
- **数值解（numerical IK）**：以雅可比伪逆、阻尼最小二乘（DLS, damped least squares）、Levenberg–Marquardt、QP 形式迭代逼近，可处理冗余与一般机构；代价是局部收敛、迭代次数与实时性的不确定性。`> 待核实`（算法本体无 [n]）。**相关可核查线索**：[35] 以「Task Space Inverse Dynamics」形式给出受约束全驱动机器人的**优先级运动-力控制**，是任务空间法与奇异性/冗余处理在同一框架内的经典工程化表述；[112] 进一步给出带**任务优先级切换**的递归层次投影。
  - 热度：`> 待核实` [35][112]；权威：arXiv 预印本（cs.RO / eess.SY 类）[35][112]；关注度：`> 待核实` [35][112]；推荐度：★★★★☆（凡涉及冗余机械臂的优先级/零空间投影，二者是绕不开的参考）[35][112]。
- **学习式 IK（learning-based IK）**：用回归/生成模型或多解分类直接预测关节角，绕开迭代；核心质疑是**模型失配**与**分布外泛化**。可核查证据：[34] 明确研究「misspecified robot models」下的 IK 学习，用结构化预测（structured prediction）处理模型不准确；[87] 提出自适应 IK 框架以学习**变长工具（variable-length tool）**操作，把未知运动学参数纳入学习回路；[90] 则在策略层保持整臂运动学一致性。
  - 热度：`> 待核实` [34][87][90]；权威：均为 arXiv 预印本（cs.RO）[34][87][90]；关注度：`> 待核实` [34][87][90]；推荐度：[34] ★★★★☆（模型失配是学习式 IK 的真问题，题目即点中要害）[34]；[87] ★★★☆☆（工具长度可变属真实工程场景）[87]；[90] ★★★☆☆（表示层与策略层的结合样本）[90]。

### 3.2 代表条目总览表

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Analytically Informed Inverse Kinematics Solution at Singularities | 2024 | `> 待核实` [107] | `> 待核实` [107] | arXiv 预印本 cs.RO [107] | `> 待核实` [107] | ★★★★☆ 奇异点解析引导 [107] | <http://arxiv.org/abs/2412.20409v1> | 针对奇异位形的解析信息增强 IK |
| An Efficient Multi-solution Solver for the Inverse Kinematics of 3-Section Constant-Curvature Robots | 2023 | `> 待核实` [39] | `> 待核实` [39] | arXiv 预印本 cs.RO [39] | `> 待核实` [39] | ★★★☆☆ 多解枚举 [39] | <http://arxiv.org/abs/2305.01458v1> | 连续体机器人 IK 的多解求解 |
| Structured Prediction for CRiSP Inverse Kinematics Learning with Misspecified Robot Models | 2021 | `> 待核实` [34] | `> 待核实` [34] | arXiv 预印本 cs.RO [34] | `> 待核实` [34] | ★★★★☆ 模型失配下学习 IK [34] | <http://arxiv.org/abs/2102.12942v1> | 结构化预测处理运动学误差 |
| Adaptive Inverse Kinematics Framework for Learning Variable-Length Tool Manipulation | 2025 | `> 待核实` [87] | `> 待核实` [87] | arXiv 预印本 cs.RO [87] | `> 待核实` [87] | ★★★☆☆ 工具运动学自适应 [87] | <http://arxiv.org/abs/2510.26551v1> | 变长工具下的 IK 学习 |
| Kinematics-Aware Diffusion Policy with Consistent 3D Observation and Action Space | 2025 | `> 待核实` [90] | `> 待核实` [90] | arXiv 预印本 cs.RO [90] | `> 待核实` [90] | ★★★☆☆ 整臂运动学一致性 [90] | <http://arxiv.org/abs/2512.17568v1> | 策略层引入运动学约束 |
| Task Space Inverse Dynamics (优先级运动-力控制) | 2014 | `> 待核实` [35] | `> 待核实` [35] | arXiv 预印本 [35] | `> 待核实` [35] | ★★★★☆ 任务空间/零空间经典形式 [35] | <http://arxiv.org/abs/1410.3863v1> | 受约束全驱动机器人优先级控制 |
| Recursive Hierarchical Projection for Whole-Body Control with Task Priority Transition | 2021 | `> 待核实` [112] | `> 待核实` [112] | arXiv 预印本 cs.RO [112] | `> 待核实` [112] | ★★★★☆ 任务优先级切换 [112] | <http://arxiv.org/abs/2109.07236v2> | 层次投影/零空间一致性 |

### 3.3 三条路线的取舍（本轮证据允许的结论）

- **解析解**：快且可枚举，但绑机构、奇异处退化；[107] 表明即使走解析路线，奇异邻域仍需专门处理 [107]。`> 待核实`：不同机构下解析解 vs 数值解的**量化精度/速度对比**本轮无 [n]。
- **数值解**：通用性最好，是冗余机械臂与任务优先级框架（[35][112]）的事实基座；但其**真机实时性口径（控制频率、端到端延迟、算力平台）**在本轮候选中完全缺失，`> 待核实`。
- **学习式 IK**：价值在绕过迭代与处理难建模对象（失配模型 [34]、变长工具 [87]、整臂动作空间 [90]）；但**安全保证与分布外泛化边界**在本轮候选中无任何可核查证据，`> 待核实`。用于评测低层运动学推理的基准亦刚起步（[91] ManipBench 面向 VLM 的低层操作能力评测，`> 待核实` 其对 IK 泛化性的覆盖度 [91]）。

**本章缺口（须补充检索后才能下结论）**：
- 解析解与数值解在同一本体、同一硬件下的精度/耗时/多解选择策略对比 —— `> 待核实`。
- 阻尼最小二乘（DLS）、零空间投影、任务优先级在真机上的实际表现数据 —— `> 待核实`（[35][112] 提供方法但不提供可迁移的真机指标）。
- 学习式 IK 的安全层、可达性约束与失败检测 —— `> 待核实`（本轮无 [n]）。
- 真机实时性指标（控制频率、端到端延迟、嵌入式算力）—— `> 待核实`（本轮候选中零覆盖）。

## 参考来源

[1] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1
[2] LLM-based ambiguity detection in natural language instructions for collaborative surgical robots — http://arxiv.org/abs/2507.11525v1
[3] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1
[4] One-Shot Reinforcement Learning for Robot Navigation with Interactive Replay — http://arxiv.org/abs/1711.10137v2
[5] On-Policy Robot Imitation Learning from a Converging Supervisor — http://arxiv.org/abs/1907.03423v7
[6] Robot Trains Robot: Automatic Real-World Policy Adaptation and Learning for Humanoids — http://arxiv.org/abs/2508.12252v2
[7] Robot Learning: A Tutorial — http://arxiv.org/abs/2510.12403v1
[8] Multi-objective Model-based Policy Search for Data-efficient Learning with Sparse Rewards — http://arxiv.org/abs/1806.09351v3
[9] State-of-the-art in Robot Learning for Multi-Robot Collaboration: A Comprehensive Survey — http://arxiv.org/abs/2408.11822v1
[10] Humanoid Whole-Body Badminton via an Annealed Reinforcement Learning Curriculum — http://arxiv.org/abs/2511.11218v4
[11] The Role of Domain Randomization in Training Diffusion Policies for Whole-Body Humanoid Control — http://arxiv.org/abs/2411.01349v1
[12] CHILD (Controller for Humanoid Imitation and Live Demonstration): a Whole-Body Humanoid Teleoperation System — http://arxiv.org/abs/2508.00162v2
[13] Humanoid Manipulation Interface: Humanoid Whole-Body Manipulation from Robot-Free Demonstrations — http://arxiv.org/abs/2602.06643v2
[14] Humanoid Whole-Body Manipulation via Active Spatial Brain and Generalizable Action Cerebellum — http://arxiv.org/abs/2605.21133v2
[15] Learning Humanoid Standing-up Control across Diverse Postures — http://arxiv.org/abs/2502.08378v2
[16] A ROS-based Software Framework for the NimbRo-OP Humanoid Open Platform — http://arxiv.org/abs/1809.11051v1
[17] Hierarchical World Models as Visual Whole-Body Humanoid Controllers — http://arxiv.org/abs/2405.18418v3
[18] SE(3)-Equivariant Diffusion Policy in Spherical Fourier Space — http://arxiv.org/abs/2507.01723v1
[19] Leveraging SE(3) Equivariance for Learning 3D Geometric Shape Assembly — http://arxiv.org/abs/2309.06810v2
[20] NTU-NPU System for Voice Privacy 2024 Challenge — http://arxiv.org/abs/2410.02371v1
[21] SemEval-2024 Task 3: Multimodal Emotion Cause Analysis in Conversations — http://arxiv.org/abs/2405.13049v3
[22] ET-SEED: Efficient Trajectory-Level SE(3) Equivariant Diffusion Policy — http://arxiv.org/abs/2411.03990v2
[23] TDCOSMO 2025: Cosmological constraints from strong lensing time delays — http://arxiv.org/abs/2506.03023v4
[24] AIn't Nothing But a Survey? Using Large Language Models for Coding German Open-Ended Survey Responses on Survey Motivation — http://arxiv.org/abs/2506.14634v3
[25] PINOCCHIO and the hierarchical build-up of dark matter haloes — http://arxiv.org/abs/astro-ph/0109324v1
[26] The Relativistic Elasticity of Rigid Bodies — http://arxiv.org/abs/physics/0307019v3
[27] Developing a 21st Century Global Library for Mathematics Research — http://arxiv.org/abs/1404.1905v1
[28] A Simulation and Modeling of Access Points with Definition Language — http://arxiv.org/abs/1304.1836v2
[29] Superconductivity as a consequence of an ordering of the electron gas zero-point oscillations — http://arxiv.org/abs/1005.0280v6
[30] On the invariant motions of rigid body rotation over the fixed point, via Euler angles — http://arxiv.org/abs/1601.04526v1
[31] Intutionistic Fuzzy Ideals in Γ-semiring — http://arxiv.org/abs/1011.5746v2
[32] PINOCCHIO: pinpointing orbit-crossing collapsed hierarchical objects in a linear density field — http://arxiv.org/abs/astro-ph/0109323v2
[33] Xiaomi-Robotics-1: Scaling Vision-Language-Action Models with over 100K Hours of Real-World Trajectories — http://arxiv.org/abs/2607.15330v2
[34] Structured Prediction for CRiSP Inverse Kinematics Learning with Misspecified Robot Models — http://arxiv.org/abs/2102.12942v3
[35] Prioritized motion-force control of constrained fully-actuated robots: "Task Space Inverse Dynamics" — http://arxiv.org/abs/1410.3863v1
[36] Occupancy-SLAM: Simultaneously Optimizing Robot Poses and Continuous Occupancy Map — http://arxiv.org/abs/2405.10743v1
[37] Inverse Optimal Control from Incomplete Trajectory Observations — http://arxiv.org/abs/1803.07696v4
[38] Optimal Predefined-time Trajectory Planning for a Free-floating Space Robot — http://arxiv.org/abs/2011.04193v3
[39] An Efficient Multi-solution Solver for the Inverse Kinematics of 3-Section Constant-Curvature Robots — http://arxiv.org/abs/2305.01458v1
[40] Direction and Trajectory Tracking Control for Nonholonomic Spherical Robot by Combining Sliding Mode Controller and Model Prediction Controller — http://arxiv.org/abs/2205.14181v1
[41] GPU Multisplit: an extended study of a parallel algorithm — http://arxiv.org/abs/1701.01189v2
[42] GPU-Accelerated Multilevel Graph Clustering: A Parallel Perspective on Louvain and Leiden — http://arxiv.org/abs/2608.01503v1
[43] Performance Comparison on Parallel CPU and GPU Algorithms for Unified Gas-Kinetic Scheme — http://arxiv.org/abs/1810.08137v3
[44] Heterogeneous Highly Parallel Implementation of Matrix Exponentiation Using GPU — http://arxiv.org/abs/1204.3052v1
[45] cuPC: CUDA-based Parallel PC Algorithm for Causal Structure Learning on GPU — http://arxiv.org/abs/1812.08491v4
[46] Performance Comparison Between OpenCV Built in CPU and GPU Functions on Image Processing Operations — http://arxiv.org/abs/1906.08819v1
[47] Faster Vertex Cover Algorithms on GPUs with Component-Aware Parallel Branching — http://arxiv.org/abs/2512.18334v1
[48] Measurement of inelastic scattering $Λ(\overlineΛ)+p\toΣ^{0}(\overlineΣ^{0})+p$ via $e^+e^-\to J/ψ\toΛ\overlineΛ$ — http://arxiv.org/abs/2609.02584v1
[49] Evidence of $ψ(3770) \to π^{0}J/ψ$ — http://arxiv.org/abs/2606.14105v1
[50] Measurement of the CKM angle $γ$ in $B^{\pm} \rightarrow D(\rightarrow K^{0}_{\rm S} h^{\prime+}h^{\prime-})h^{\pm}$ decays with a novel approach — http://arxiv.org/abs/2604.05701v1
[51] Model Independent Approach of the JUNO $^8$B Solar Neutrino Program — http://arxiv.org/abs/2210.08437v2
[52] Precise measurement of the CKM angle $γ$ with a novel approach — http://arxiv.org/abs/2604.05712v1
[53] Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, Long Context, and Next Generation Agentic Capabilities — http://arxiv.org/abs/2507.06261v6
[54] First measurement of reactor neutrino oscillations at JUNO — http://arxiv.org/abs/2511.14593v1
[55] Initial performance results of the JUNO detector — http://arxiv.org/abs/2511.14590v1
[56] Control of a Rigid Wing Pumping Airborne Wind Energy System in all Operational Phases — http://arxiv.org/abs/2006.11141v1
[57] On Controller Design for Systems on Manifolds in Euclidean Space — http://arxiv.org/abs/1807.03475v1
[58] Analysis and design of model predictive control frameworks for dynamic operation -- An overview — http://arxiv.org/abs/2307.03004v2
[59] Adaptive Control of Robot Manipulators With Uncertain Kinematics and Dynamics — http://arxiv.org/abs/1403.5204v3
[60] The importance of ensemble techniques for operational space weather forecasting — http://arxiv.org/abs/1806.09861v1
[61] Cold-Tip Temperature Control of Space-borne SatelliteStirlingCryocooler: Mathematical Modeling and Control Investigation — http://arxiv.org/abs/1905.11247v1
[62] Verification of Space Weather Forecasts issued by the Met Office Space Weather Operations Centre — http://arxiv.org/abs/1804.02985v1
[63] SPACE: the SPectroscopic All-sky Cosmic Explorer — http://arxiv.org/abs/0804.4433v1
[64] StyleHumanCLIP: Text-guided Garment Manipulation for StyleGAN-Human — http://arxiv.org/abs/2305.16759v4
[65] Non-existence of an invariant measure for a homogeneous ellipsoid rolling on the plane — http://arxiv.org/abs/1306.4237v2
[66] Generation of highly pure Schrödinger's cat states and real-time quadrature measurements via optical filtering — http://arxiv.org/abs/1708.04042v2
[67] Geometry-aware Manipulability Learning, Tracking and Transfer — http://arxiv.org/abs/1811.11050v5
[68] Analysis and Transfer of Human Movement Manipulability in Industry-like Activities — http://arxiv.org/abs/2008.01402v2
[69] Deep Inelastic Scattering with Application to Nuclear Targets: Lectures at the 1985 Los Alamos School on Relativistic Dynamics and Quark Nuclear Physics — http://arxiv.org/abs/2212.05616v1
[70] Direct ellipsoidal fitting of discrete multi-dimensional data — http://arxiv.org/abs/1901.05511v3
[71] Enhancing Robustness in Manipulability Assessment: The Pseudo-Ellipsoid Approach — http://arxiv.org/abs/2412.18869v2
[72] HumanoidBench: Simulated Humanoid Benchmark for Whole-Body Locomotion and Manipulation — http://arxiv.org/abs/2403.10506v2
[73] Real-Time Whole-Body Control of Legged Robots with Model-Predictive Path Integral Control — http://arxiv.org/abs/2409.10469v1
[74] Passive iFIR Filters for Data-Driven Control — http://arxiv.org/abs/2403.06640v2
[75] Using quantum computers in control: interval matrix properties — http://arxiv.org/abs/2403.17711v1
[76] Bringing Quantum Systems under Control: A Tutorial Invitation to Quantum Computing and Its Relation to Bilinear Control Systems — http://arxiv.org/abs/2412.00736v1
[77] Discovery Opportunities with Gravitational Waves -- TASI 2024 Lecture Notes — http://arxiv.org/abs/2409.08956v1
[78] Contact-Implicit Optimization of Locomotion Trajectories for a Quadrupedal Microrobot — http://arxiv.org/abs/1901.09065v1
[79] IMPACT: An Implicit Active-Set Augmented Lagrangian for Fast Contact-Implicit Trajectory Optimization — http://arxiv.org/abs/2605.09127v3
[80] Contact-Implicit Trajectory Optimization using Orthogonal Collocation — http://arxiv.org/abs/1809.06436v3
[81] Global Convergence of an SQP Method for Contact-Implicit Trajectory Optimization — http://arxiv.org/abs/2406.01763v5
[82] Staged Contact Optimization: Combining Contact-Implicit and Multi-Phase Hybrid Trajectory Optimization — http://arxiv.org/abs/2304.04923v2
[83] Contact-Implicit Trajectory Optimization with Hydroelastic Contact and iLQR — http://arxiv.org/abs/2202.13986v2
[84] Inverse Dynamics Trajectory Optimization for Contact-Implicit Model Predictive Control — http://arxiv.org/abs/2309.01813v3
[85] Tuning-Free Contact-Implicit Trajectory Optimization — http://arxiv.org/abs/2006.06176v1
[86] Robot Policy Evaluation for Sim-to-Real Transfer: A Benchmarking Perspective — http://arxiv.org/abs/2508.11117v1
[87] Adaptive Inverse Kinematics Framework for Learning Variable-Length Tool Manipulation in Robotics — http://arxiv.org/abs/2510.26551v1
[88] Overview of the Sensemaking Task at the ELOQUENT 2025 Lab: LLMs as Teachers, Students and Evaluators — http://arxiv.org/abs/2507.12143v1
[89] LongEval at CLEF 2025: Longitudinal Evaluation of IR Model Performance — http://arxiv.org/abs/2503.08541v1
[90] Kinematics-Aware Diffusion Policy with Consistent 3D Observation and Action Space for Whole-Arm Robotic Manipulation — http://arxiv.org/abs/2512.17568v1
[91] ManipBench: Benchmarking Vision-Language Models for Low-Level Robot Manipulation — http://arxiv.org/abs/2505.09698v2
[92] NTIRE 2025 Challenge on Image Super-Resolution (x4): Methods and Results — http://arxiv.org/abs/2504.14582v3
[93] A Human-Vector Susceptible-Infected-Susceptible Model for Analyzing and Controlling the Spread of Vector-Borne Diseases — http://arxiv.org/abs/2510.14787v2
[94] Differentiable Simulation of Hard Contacts with Soft Gradients for Learning and Control — http://arxiv.org/abs/2506.14186v2
[95] Feedback Optimization with State Constraints through Control Barrier Functions — http://arxiv.org/abs/2504.00813v3
[96] Control Barrier Functions for Shared Control and Vehicle Safety — http://arxiv.org/abs/2503.19994v1
[97] TRUST 2025: SCRITA and RTSS @ RO-MAN 2025 — http://arxiv.org/abs/2509.11402v1
[98] Real-Time Service Subscription and Adaptive Offloading Control in Vehicular Edge Computing — http://arxiv.org/abs/2512.14002v1
[99] Self-Supervised Learning of Iterative Solvers for Constrained Optimization — http://arxiv.org/abs/2409.08066v3
[100] VLSP 2025 MLQA-TSR Challenge: Vietnamese Multimodal Legal Question Answering on Traffic Sign Regulation — http://arxiv.org/abs/2510.20381v1
[101] Inverse spectral problems for Sturm-Liouville operators with singular potentials — http://arxiv.org/abs/math/0211247v1
[102] A rich bounty of AGN in the 9 square degree Bootes survey: high-z obscured AGN and large-scale structure — http://arxiv.org/abs/astro-ph/0611654v1
[103] Inversion of the star transform — http://arxiv.org/abs/1401.7655v2
[104] The Kinematic Morphology-Density Relation from the SAMI Pilot Survey — http://arxiv.org/abs/1409.7271v1
[105] The Methanol Multibeam Survey — http://arxiv.org/abs/1210.0979v1
[106] Inversion formulas for the broken-ray Radon transform — http://arxiv.org/abs/1007.4183v1
[107] Analytically Informed Inverse Kinematics Solution at Singularities — http://arxiv.org/abs/2412.20409v1
[108] Event-Enriched Image Analysis Grand Challenge at ACM Multimedia 2025 — http://arxiv.org/abs/2508.18904v1
[109] The AudioMOS Challenge 2025 — http://arxiv.org/abs/2509.01336v1
[110] SINAI at eRisk@CLEF 2025: Transformer-Based and Conversational Strategies for Depression Detection — http://arxiv.org/abs/2509.19861v1
[111] Annif at SemEval-2025 Task 5: Traditional XMTC augmented by LLMs — http://arxiv.org/abs/2504.19675v2
[112] Recursive Hierarchical Projection for Whole-Body Control with Task Priority Transition — http://arxiv.org/abs/2109.07236v2
[113] Culturally Grounded Physical Commonsense Reasoning in Italian and English: A Submission to the MRL 2025 Shared Task — http://arxiv.org/abs/2510.22631v1
[114] DeDisCo at the DISRPT 2025 Shared Task: A System for Discourse Relation Classification — http://arxiv.org/abs/2509.11498v4
[115] NALA_MAINZ at BLP-2025 Task 2: A Multi-agent Approach for Bangla Instruction to Python Code Generation — http://arxiv.org/abs/2511.16787v1
[116] CLaC at SemEval-2025 Task 6: A Multi-Architecture Approach for Corporate Environmental Promise Verification — http://arxiv.org/abs/2505.23538v1


---

*Generated by research-bot · topic=`kinematics` · depth=`standard` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading · model=`deepseek-v4-flash` · sources=116 · duration=361s · 2026-10-04T22:46:47+00:00*
