# 机器人运动学、控制与 ROS 2 增量追踪报告（7-facet）

- **报告日期**：2026-10-16（UTC）
- **领域**：机器人运动学与动力学、控制理论（WBC / MPC / 学习型控制）、ROS 2 软件栈（ros2_control、MoveIt 2、Nav2、DDS/Zenoh）
- **检索源数量**：35 条候选来源（编号 [1]–[35]），其中与本主题**直接相关**者 13 条（[3][4][5][6][7][8][9][10][11][12][20][24][33]），**间接方法学相关**者 10 条（[14][15][16][22][23][25][27][30][31][33][34][35]）
- **证据强度总览**：控制类进展基本为 arXiv 预印本（B 级），唯一经同行评审的机器人控制对比研究为 [9]（IEEE Access，据 DOI 前缀 `10.1109/access.2025.3582523` 判定）；**ROS 2 生态（ros2_control / MoveIt 2 / Nav2 / DDS / Zenoh）在本批候选中零覆盖**

> **证据边界声明**：本批候选来源以 arXiv cs.RO / cs.SE 为主，未包含任何 ROS 2 官方发行说明、官方文档、包管理索引或仓库活跃度数据。因此本报告在"软件栈"维度大量使用 `> 待核实`，**不以模型记忆补全版本号、star 数或榜单排名**。凡候选块未提供的热度数字，一律不填。

---

## 1. 进展与热点（Progress & Hotspots）

**一句话增量判断**：相对上一基线，最明确的增量集中在**人形全身控制（whole-body control, WBC）**与**全身演示数据获取范式**两条线上——2025-11 至 2026-06 间出现多篇人形全身控制/操作/遥操作预印本 [4][5][6][7][8][12]，但**在本批候选内无任何一项获得第三方独立复现或公开榜单确认**；ROS 2 侧的版本与栈重构增量在本批证据中**无支撑材料**。

### 1.1 最新进展（近 1–2 年，2024–2026）

| 名称 | 年份/时间 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Humanoid Whole-Body Badminton via an Annealed RL Curriculum | 2025-11 首发，2026-09 修订至 v4 | 候选块未提供 | 引用数 `> 待核实` [4] | arXiv 预印本（cs.RO），未标注会议/期刊 [4] | 低 —— 候选块无引用/star/榜单信号，仅可确认时间线 [4] | ★★★★☆ 动态全身耦合控制的直接增量（退火课程解决稀疏奖励与梯度冲突） | http://arxiv.org/abs/2511.11218v4 | 无需运动先验或专家演示的统一全身控制器；步法与击球强耦合 |
| CHILD（Controller for Humanoid Imitation and Live Demonstration） | 2025-07（v2） | 候选块未提供 | 引用数 `> 待核实` [5] | arXiv 预印本（cs.RO），未标注会议/期刊 [5] | 低 —— 无热度信号 [5] | ★★★★☆ 补足"人形全身关节级遥操作"的空白，属数据采集使能层 | http://arxiv.org/abs/2508.00162v2 | 紧凑、可重构的全身关节级遥操作系统 |
| HuMI（Humanoid Manipulation Interface） | 2026-02（v2） | 候选块未提供 | 引用数 `> 待核实` [6] | arXiv 预印本（cs.RO），未标注会议/期刊 [6] | 低 —— 无热度信号 [6] | ★★★★☆ 代表"免机器人实体演示（robot-free demonstrations）"范式迁移 | http://arxiv.org/abs/2602.06643v2 | 绕开遥操作硬件物流与复杂奖励工程两类瓶颈 |
| Constrained Whole-Body Tracking for Humanoid Robots | 2026（v2） | 候选块未提供 | `> 待核实` [7] | arXiv 预印本（cs.RO）[7] | 低 —— 候选块仅提供标题与链接 [7] | ★★★☆☆ 标题指向"受约束全身跟踪"，与 WBC 主题相关，但**内容未抽取** | http://arxiv.org/abs/2606.00374v2 | 具体方法、实验口径 `> 待核实` |
| Humanoid Whole-Body Manipulation via Active Spatial Brain and Generalizable Action Cerebellum | 2026（v2） | 候选块未提供 | `> 待核实` [8] | arXiv 预印本（cs.RO）[8] | 低 —— 候选块仅提供标题与链接 [8] | ★★★☆☆ "脑—小脑"分层架构线索，与全身操作控制相关，内容待读 | http://arxiv.org/abs/2605.21133v2 | 具体方法、实验口径 `> 待核实` |
| Next-Generation Whole-Body Control System of Humanoid Robots | 2025-06（v5） | 候选块未提供 | `> 待核实` [12] | arXiv HTML 版本（v5），未标注同行评审 [12] | 低 —— 无热度信号 [12] | ★★★☆☆ 标题直接对应"下一代 WBC 系统"，是栈级线索；内容待核实 | https://arxiv.org/html/2506.20487v5 | 版本迭代至 v5 说明持续演进 |
| Real-Time Whole-Body Control of Legged Robots with Model-Predictive Path Integral Control | 2024-09 | 候选块未提供 | `> 待核实` [11] | arXiv 预印本（cs.RO）[11] | 低 —— 无热度信号 [11] | ★★★★☆ 代表"MPC 与控制论采样方法（path integral）"路线，与 MPC facet 直接相关 | http://arxiv.org/abs/2409.10469v1 | 实时性、真机口径 `> 待核实` |
| The Role of Domain Randomization in Training Diffusion Policies for Whole-Body Humanoid Control | 2024-11 | 候选块未提供 | `> 待核实` [3] | arXiv 预印本 [3] | 低 —— 无热度信号 [3] | ★★★★☆ 学习型 WBC 的 sim-to-real 关键变量（域随机化）的消融视角 | http://arxiv.org/abs/2411.01349v1 | 具体结论与消融数字 `> 待核实` |
| Benchmarking Model Predictive Control and Reinforcement Learning-Based Control for Legged Robot Locomotion in MuJoCo Simulation | 2025 | 候选块未提供 | 引用数 `> 待核实` [9] | **同行评审期刊**（IEEE Access，据 DOI 前缀判定）[9] | 低 —— 无引用/榜单信号，但**权威等级为 A/B 级** [9] | ★★★★☆ 本批唯一 MPC vs RL 的受控对比研究，是"流派对比"最可信证据 | https://doi.org/10.1109/access.2025.3582523 | 仅 MuJoCo 仿真；真机结论不可外推 |

**证据四轴要点（最新进展中最值得追的三条）**

- **[4] 人形羽毛球全身控制**：热度 `> 待核实`（候选块无引用数/star）[4]；权威为 arXiv cs.RO 预印本、无会议标注 [4]；关注度**低**（无可量化热度信号）[4]；推荐度 **★★★★☆**，理由是它直接命中"控制新算法 + 动态全身耦合"这一子问题核心，但真机验证与成功率口径必须读全文核实 [4]。
- **[5] CHILD 全身遥操作**：热度 `> 待核实` [5]；权威为 arXiv cs.RO 预印本 [5]；关注度**低** [5]；推荐度 **★★★★☆**，理由是全身关节级遥操作是策略学习的数据闭环入口 [5]；硬件成本、延迟指标与开源状态 `> 待核实`。
- **[6] HuMI 免机器人演示**：热度 `> 待核实` [6]；权威为 arXiv cs.RO 预印本 [6]；关注度**低** [6]；推荐度 **★★★★☆**，理由是它把"演示采集"从机器人本体解耦，与人形操作数据规模化的瓶颈直接相关 [6]。

> **待核实**：以上条目均**未**获本批候选内的第三方评测支持；本批候选不含 LIBERO / SimplerEnv / RoboArena / Open X-Embodiment 等榜单来源，故"是否 SOTA"无法判定。

### 1.2 经典与奠基性工作（当前技术演进的地基）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Operational Space Control of Constrained and Underactuated Systems | 2011 | 候选块未提供 | citations = 75 [20] | 同行评审会议论文集（DOI 前缀 `10.15607/rss.2011.vii.031`，RSS 2011）[20] | **高** —— citations=75，为本批唯一带真实引用数的条目 [20] | ★★★★☆ 操作空间控制（operational space）在受约束/欠驱动系统上的奠基性形式化 | https://doi.org/10.15607/rss.2011.vii.031 | 把任务空间与零空间动力学解耦；本批另见同一论文的 MIT Press 版本 [22] |
| Operational Space Control of Constrained and Underactuated Systems（MIT Press 版） | 2011 | 候选块未提供 | `> 待核实` [22] | 出版社正式版本（DOI `10.7551/mitpress/9481.003.0034`）[22] | 低 —— 无热度信号 [22] | ★★★☆☆ 与 [20] 为同一工作的另一出版载体，引用时避免重复计数 | https://doi.org/10.7551/mitpress/9481.003.0034 | 同上 |
| Exact decoupling of the force-position control using the operational space formulation | 1992 | 候选块未提供 | `> 待核实` [23] | IEEE 会议/期刊（DOI `10.1109/robot.1992.220155`）[23] | 低 —— 无热度信号 [23] | ★★★★☆ 力—位混合解耦的经典源头之一，构成阻抗/力控类 WBC 的理论地基 | https://doi.org/10.1109/robot.1992.220155 | 具体推导与适用范围 `> 待核实` |
| Newton-Euler, Lagrange and Kirchhoff formulations of rigid body dynamics: a unified approach | 2016 | 候选块未提供 | `> 待核实` [24] | arXiv 预印本（cs.RO / 数学物理交叉）[24] | 低 —— 无热度信号 [24] | ★★★★☆ 刚体动力学三种形式化的统一视角，是 WBC/MPC 动力学建模的基础读物 | http://arxiv.org/abs/1607.00156v1 | 与运动学/动力学算法教学脉络直接相关 |
| Adaptive Control of Robot Manipulators With Uncertain Kinematics and Dynamics | 2014（v3） | 候选块未提供 | `> 待核实` [16] | arXiv 预印本（v3）[16] | 低 —— 无热度信号 [16] | ★★★★☆ 同时处理运动学与动力学不确定性的自适应控制奠基线 | http://arxiv.org/abs/1403.5204v3 | 与"标定误差 + 参数不确定"的工程问题对应 |
| On Controller Design for Systems on Manifolds in Euclidean Space | 2018 | 候选块未提供 | `> 待核实` [14] | arXiv（math.OC）[14] | 低 —— 无热度信号 [14] | ★★★☆☆ 流形上系统在欧氏空间做控制器设计的通用方法，与人形/浮动基座控制的坐标选择相关 | http://arxiv.org/abs/1807.03475v1 | 应用层验证 `> 待核实` |
| Analysis and design of model predictive control frameworks for dynamic operation — An overview | 2023 | 候选块未提供 | `> 待核实` [15] | arXiv（eess.SY）综述 [15] | 低 —— 无热度信号 [15] | ★★★★☆ MPC 框架设计的综述型入口，适合作为 MPC facet 的分类骨架 | http://arxiv.org/abs/2307.03004v2 | 注意：2023 年综述，未覆盖 2024–2026 学习型 MPC 新范式 |
| Whole-Body Geometric Retargeting for Humanoid Robots | 2019 | 候选块未提供 | `> 待核实` [10] | arXiv 预印本（cs.RO）[10] | 低 —— 无热度信号 [10] | ★★★★☆ 人形全身"几何重定向"经典，是当前全身遥操作/示教（如 [5][6]）的直接前作脉络 | http://arxiv.org/abs/1909.10080v1 | 与 [5][6] 构成"重定向→全身示教→免机器人演示"的演进线 |
| Robowflex: Robot Motion Planning with MoveIt Made Easy | 2021 | 候选块未提供 | `> 待核实` [33] | arXiv 预印本 [33] | 低 —— 无热度信号 [33] | ★★★★☆ 本批**唯一**与 MoveIt 直接相关的工程化工作，是"MoveIt 用于批量运动规划实验"的关键线索 | http://arxiv.org/abs/2103.12826v2 | 面向 MoveIt 1 还是 MoveIt 2 `> 待核实` |
| Evaluating Guiding Spaces for Motion planning | 2022 | 候选块未提供 | `> 待核实` [34] | arXiv 预印本 [34] | 低 —— 无热度信号 [34] | ★★★☆☆ 运动规划引导空间（guiding space）的评测方法，可用于规划器横评设计 | http://arxiv.org/abs/2210.08640v1 | 与 MoveIt 2 默认规划器（OMPL 系）的关系 `> 待核实` |
| Data-Efficient Learning of High-Quality Controls for Kinodynamic Planning | 2022 | 候选块未提供 | `> 待核实` [35] | arXiv 预印本 [35] | 低 —— 无热度信号 [35] | ★★★☆☆ 动力学规划中控制序列的数据高效学习，属"规划 + 学习"交叉经典 | http://arxiv.org/abs/2201.02254v1 | 应用于车辆导航场景 |

**奠基脉络小结（承上启下）**：操作空间形式化 [20][23] → 刚体动力学统一形式 [24] 与不确定参数自适应 [16] → 全身几何重定向 [10] → 现代人形 WBC（[4][5][6][7][8][11][12]）与 MoveIt 工程化 [33]。注意：Khatib 1987 操作空间原始论文在本批候选中**未被单独列出**，仅由 [20] 的正文引用提及，其一手出处 `> 待核实`。

---

## 2. 工业界与产品（Industry & Product）

**一句话增量判断**：在本批候选中，**本周期无显著工业界增量**——没有任何产品发布、量产披露、厂商技术报告或官方博客类候选来源。

- **从 lab 走向产品**：`> 待核实`。候选块中无工业界/产品类来源，无法证实任何真机部署案例 [2][25][27][31]。
- **MoveIt 侧工程化**：唯一相关条目是 Robowflex [33]（把 MoveIt 封装为可批量实验的规划框架），但它面向的是**研究实验效率**而非产品交付；其是否支持 MoveIt 2、当前维护状态、star 数与最近提交时间 `> 待核实` [33]。
- **ros2_control / Nav2 / DDS / Zenoh**：本批候选**完全未覆盖**。ROS 2 发行版（如候选块提到的 Jazzy/Kilted/Rolling 对应关系）、许可证清单、发布节奏均 `> 待核实`。
- **热度证据**：所有工业界相关判断的热度证据缺失，`> 待核实`；本批唯一"仓库热度可量化"的方法学来源 [25] 发表于 2016 年，已不能反映 2026 年生态，且其结论仅为"star 数是流行度的直接度量" [25]。

### 2.1 开源项目与工程实践（本批证据覆盖情况）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Robowflex（MoveIt 封装） | 2021 | 候选块未提供 | star 数 `> 待核实` [33] | arXiv 预印本，非官方文档 [33] | 低 —— 无 star/引用信号 [33] | ★★★★☆ 唯一 MoveIt 相关工程实践线索，但需核实是否对应 MoveIt 2 | http://arxiv.org/abs/2103.12826v2 | 用于运动规划实验的自动化 |
| ros2_control / controller_manager | — | — | `> 待核实` | `> 待核实` | `> 待核实` | 无法评分 —— **本批候选零覆盖** | `> 待核实` | 需补充官方仓库与发行说明 |
| MoveIt 2 | — | — | `> 待核实` | `> 待核实` | `> 待核实` | 无法评分 —— 本批无 MoveIt 2 直接来源 | `> 待核实` | 仅 [33][34] 为间接线索 |
| Nav2 | — | — | `> 待核实` | `> 待核实` | `> 待核实` | 无法评分 —— 本批候选零覆盖 | `> 待核实` | 需补充官方仓库与 release 记录 |
| DDS / Zenoh 中间件 | — | — | `> 待核实` | `> 待核实` | `> 待核实` | 无法评分 —— 本批候选零覆盖 | `> 待核实` | 需补充 RTPS/Zenoh 官方规范与基准 |
| GitHub 仓库可复现性评估方法（通用） | 2025 / 2026 / 2016 | 候选块未提供 | `> 待核实` [27][31] | 均为 arXiv 预印本，非 ROS 2 官方标准 [27][31] | 低 —— 无引用数/star 信号 [27][31] | ★★☆☆☆–★★★☆☆ 仅作"文档完整性→复现门槛"的方法线索 | http://arxiv.org/abs/2507.21899v1 ；http://arxiv.org/abs/2605.16701v2 | [31] 对 1 万个仓库做内容实证统计 [31]；[25] 为 2016 年 star 热度代理 [25] |

> **待核实**：本节的"开源项目"行多数为**空位**，原因是候选集不含任何机器人中间件仓库来源 [2][25][27][31]。任何关于维护活跃度、版本/许可证的判断都必须补充检索官方仓库后才能给出。

---

## 3. 蓝海与缺口（Blue Ocean & Gaps）

**一句话增量判断**：本批证据暴露出的最大缺口不是"某个算法没人做"，而是**整条 ROS 2 软件栈在本轮调研中没有任何可核证据**；同时，人形全身控制的证据链**缺少独立评测层**。

- **缺口语料 1（软件栈真空）**：候选集中不存在 ROS 2、DDS、实时控制、ros2_control、MoveIt 2、Nav2 相关的项目或文档来源 [2][25][27][31]；本子问题的核心（可复现性、维护活跃度、版本/许可证、lab→产品）在当前证据下**无法被直接回答**。
- **缺口 2（评测层缺失）**：没有公开基准或榜单来源，无法判断 [4][5][6][7][8][11][12] 中任何方法是否获得第三方独立验证——只有论文自述。
- **缺口 3（热度信号系统性缺失）**：35 条候选中仅 [20] 提供真实引用数（citations=75），其余热度字段全为 `> 待核实`；这本身是重要的方法论缺口——用 star/引用给 ROS 2 包排序的可靠口径尚不存在（[25] 的口径已过时近 10 年 [25]）。
- **高杠杆机会（相对本批证据的合理推断，标 [P]）**：
  - **[P]** "全套 WBC 论文 + 可复现 ROS 2 控制栈"的桥接工作是蓝海：一侧是密集的人形 WBC 预印本 [4][5][6][7][8][11][12]，另一侧是本批**零证据**的 ROS 2 控制栈。依据链：控制新方法持续产出 → 工程落地需要一个标准化部署载体 → 该载体在本批证据中不存在。**可证伪假设**：若到 2027-04 前仍无主流 ros2_control 级 WBC 部署参考实现伴随上述论文发布，则该缺口判断成立。
  - **[P]** "免机器人演示（robot-free demonstration）"的数据采集标准化（格式、重定向、质量筛选）是另一个缺口：HuMI [6] 与全身几何重定向 [10] 各自提供片段，但没有本批证据显示存在统一数据格式。置信度：推测。
- **竞争空白**：本批候选中没有任何 MPC-vs-RL 在**真机人形**上的受控对比（唯一的对比研究 [9] 限于 MuJoCo 仿真）[9]。

---

## 4. 瓶颈与拐点（Bottleneck & Inflection）

**一句话增量判断**：当前瓶颈主要不在"控制算法本身"，而在**评测与部署口径**；拐点信号是"仿真对比研究（[9]）出现"与"机器人本体被移出数据采集回路（[6]）"这两个方向性变化。

| 瓶颈 | 类型 | 证据 | 是否临近拐点 |
|---|---|---|---|
| 缺少真机、跨本体、可复现的横评 | 评测瓶颈 | 唯一 MPC vs RL 对比限于 MuJoCo 仿真 [9]；其余控制类进展均无第三方复现 [4][5][6][11] | **需要数据** —— 无时间序列证据可用于判断拐点 |
| 热度/影响力无法量化 | 方法论瓶颈 | 35 条候选中仅 [20] 有真实引用数；star 代理口径陈旧 [25] | 未知 |
| ROS 2 侧部署与实时性 | 工程瓶颈 | 本批候选**无任何**实时控制/中间件来源 [2][25][27][31] | `> 待核实` |
| 人形全身数据的采集成本 | 数据瓶颈 | 遥操作受硬件物流限制、RL 奖励工程复杂 → 催生免机器人演示 [6]；遥操作侧补位者为 [5] | **较大概率** —— 范式迁移信号已出现 [6] |
| 动力学建模/坐标表示 | 算法瓶颈 | 流形控制 [14]、刚体动力学统一形式 [24]、约束/欠驱动操作空间 [20] 构成基础，但对现代浮动基座全身控制的适配性 `> 待核实` | 未知 |

**数据集与基准（本批证据覆盖情况）**

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| MuJoCo 腿式机器人 MPC vs RL 基准（论文自带实验） | 2025 | 候选块未提供 | 引用数 `> 待核实` [9] | 同行评审期刊（IEEE Access，据 DOI 判定）[9] | 低 —— 无榜单排名/引用信号 [9] | ★★★★☆ 本批唯一受控对比实验，是评测缺口判断的直接证据 | https://doi.org/10.1109/access.2025.3582523 | 仅仿真，真机外推 `> 待核实` |
| Domain Randomization for Diffusion Policies（全身人形控制） | 2024 | 候选块未提供 | `> 待核实` [3] | arXiv 预印本 [3] | 低 —— 无热度信号 [3] | ★★★★☆ 作为 sim-to-real 评估变量（域随机化）的方法参考 | http://arxiv.org/abs/2411.01349v1 | 具体消融结论 `> 待核实` |
| Evaluating Guiding Spaces for Motion Planning | 2022 | 候选块未提供 | `> 待核实` [34] | arXiv 预印本 [34] | 低 [34] | ★★★☆☆ 运动规划评测设计参考 | http://arxiv.org/abs/2210.08640v1 | 与 MoveIt 2 规划器族的关系 `> 待核实` |
| LIBERO / SimplerEnv / RoboArena / Open X-Embodiment | — | — | `> 待核实` | `> 待核实` | `> 待核实` | 无法评分 —— **本批候选零覆盖** | `> 待核实` | 需补充检索 |

> **待核实**：上表后 4 行的空缺是**检索覆盖缺口**，而非"该基准不存在"的结论。

---

## 5. 社会·政策·国际（Society, Policy & Geopolitics）

**一句话增量判断**：**本周期在候选证据内无显著变化**——候选集中不存在任何监管、标准、出口管制、供应链或伦理政策类来源。

- 监管与标准（如机器人安全标准、AI 法案对具身系统的适用）：`> 待核实`，本批候选零覆盖 [1][2][17][18][19][21]。
- 地缘政治与供应链（如控制芯片、传感器、开源许可的跨境影响）：`> 待核实`，无来源。
- 劳动与伦理影响：`> 待核实`，无来源。
- **可用的间接线索**：唯一与"开源治理/可及性"沾边的候选是仓库可及性与可追溯性方法学研究 [28][32]，但其对象是 PyPI/NPM 库与论文关联仓库，**不是机器人软件**；不能作为 ROS 2 生态治理结论 [28][32]。

> 本节遵循方法论要求：**没有增量证据就写"无显著变化"**，不为凑篇幅编造政策动向。

---

## 6. 资本与生态（Capital & Ecosystem）

**一句话增量判断**：**本周期在候选证据内无显著变化**——无融资、并购、人才流动或公司格局类来源。

- 投资/并购/人才：`> 待核实`，候选集零覆盖。
- **社区与生态的弱代理指标**：本批提供了若干"开源仓库计量学"方法来源——仓库流行度预测 [25]、仓库描述生成 [26]、README 内容分类 [27]、可及性分析 [28]、领域自动分类 [29]、应用流行度 [30]、1 万仓库内容实证 [31]、仓库与论文的关联追踪 [32]。它们可用于设计"ROS 2 包生态活跃度"的度量方案，但**均非针对机器人领域**：
  - 热度：`> 待核实`（[25][27][31] 等候选块未提供引用数）[25][27][31]
  - 权威：均为 arXiv 预印本（cs.SE / cs.AI），未标注同行评审 venue [25][27][31]
  - 关注度：低 —— 无 star/引用/榜单信号 [25][27][31]
  - 推荐度：★★☆☆☆–★★★☆☆，理由是它们只能作为**方法线索**，不能直接支撑 ROS 2 生态结论 [25][27][31]
- **公司格局变化**：`> 待核实`。本批候选不包含任何厂商官方博客或产业分析来源。

---

## 7. 信号与预测（Signals & Forecast）

**一句话增量判断**：本周期可观测的强信号是"人形全身控制论文密集出现 + 数据采集去机器人化"，弱信号是"仿真受控对比研究开始出现"；已确证的事实仅限于论文存在与时间戳，其余均为推测。

### 7.1 已确证信号（确定 / 较大概率）

1. **信号（确定）**：2025-11 → 2026-06 期间，人形全身控制/操作/遥操作预印本持续产出，且部分工作迭代至 v4/v5，说明该方向处于活跃修订期 [4][5][6][7][8][12]。
2. **信号（确定）**：出现"无需运动先验或专家演示"的课程式 RL 全身控制器 [4]，以及"免机器人演示"的全身操作学习方案 [6]——两者共同指向**降低对人形硬件与奖励工程的依赖**。
3. **信号（较大概率）**：受控对比研究开始进入该领域，但**仅限仿真**（MuJoCo，MPC vs RL）[9]。

### 7.2 预测与可证伪假设

- **[P] 预测 1（置信度：较大概率）**：未来 6–12 个月内，人形全身控制类工作会把"真机横评（≥2 项任务、≥1 台真机、与既有 MPC/WBC 基线对比）"作为差异化卖点。
  - 依据链：当前同方向预印本密集 [4][5][6][7][8][11][12]，但本批证据中无真机对比 [9 only 仿真] → 差异化必然转向验证质量。
  - **可证伪假设**：若到 2027-04 前，检索到的该方向新论文中带真机多任务对比的比例仍为 0，则本预测不成立。
- **[P] 预测 2（置信度：推测）**："免机器人演示 / 重定向式示教"会与全身控制器形成配对管线，即"人侧采集 → 几何重定向 [10] → 全身策略（[4][5][6]）"。
  - **可证伪假设**：若出现的工作只做其中一环、且显式声明该管线不可迁移，则本预测被削弱。
- **[P] 预测 3（置信度：需要数据）**：ROS 2 侧（ros2_control / MoveIt 2 / Nav2 / DDS / Zenoh）会出现与 WBC 论文配套的部署参考实现。
  - 依据链：控制侧方法供给充足 [4][5][6][11][12]，而部署侧在本批证据中完全空白 [2][25][27][31] → 供需缺口本身构成机会，但**本批无任何时间序列证据**支撑拐点判断。
  - **可证伪假设**：若到 2027-10 前，主流 ros2_control 生态仍无 WBC 参考实现被上述任一篇论文官方引用，则本预测不成立。
- **[R] 传闻类**：无。本批候选不含可靠传闻来源，故不列。

### 7.3 Watchlist（值得持续关注）

1. `[4]` Humanoid Whole-Body Badminton —— 关注其 v4 之后的真机指标与是否中稿（https://arxiv.org/abs/2511.11218v4）
2. `[6]` HuMI —— 关注 robot-free demonstration 的具体硬件形态与数据规模（https://arxiv.org/abs/2602.06643v2）
3. `[9]` MPC vs RL 腿式机器人 MuJoCo 基准 —— 关注是否出现真机扩展版（https://doi.org/10.1109/access.2025.3582523）
4. `[12]` Next-Generation Whole-Body Control System —— 关注其是否给出系统级（栈级）实现（https://arxiv.org/html/2506.20487v5）
5. `[33]` Robowflex —— 关注是否迁移到 MoveIt 2（http://arxiv.org/abs/2103.12826v2）
6. **必须补检的空白**：ros2_control 官方仓库与发行说明、MoveIt 2 / Nav2 release 记录、DDS/Zenoh 官方规范与基准、公开榜单（LIBERO / SimplerEnv 等）——当前**全部 `> 待核实`**。

---

## 参考来源

[1] A Human-Vector Susceptible-Infected-Susceptible Model for Analyzing and Controlling the Spread of Vector-Borne Diseases — http://arxiv.org/abs/2510.14787v2
[2] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1
[3] The Role of Domain Randomization in Training Diffusion Policies for Whole-Body Humanoid Control — http://arxiv.org/abs/2411.01349v1
[4] Humanoid Whole-Body Badminton via an Annealed Reinforcement Learning Curriculum — http://arxiv.org/abs/2511.11218v4
[5] CHILD (Controller for Humanoid Imitation and Live Demonstration): a Whole-Body Humanoid Teleoperation System — http://arxiv.org/abs/2508.00162v2
[6] Humanoid Manipulation Interface: Humanoid Whole-Body Manipulation from Robot-Free Demonstrations — http://arxiv.org/abs/2602.06643v2
[7] Constrained Whole-Body Tracking for Humanoid Robots — http://arxiv.org/abs/2606.00374v2
[8] Humanoid Whole-Body Manipulation via Active Spatial Brain and Generalizable Action Cerebellum — http://arxiv.org/abs/2605.21133v2
[9] Benchmarking Model Predictive Control and Reinforcement Learning-Based Control for Legged Robot Locomotion in MuJoCo Simulation — https://doi.org/10.1109/access.2025.3582523
[10] Whole-Body Geometric Retargeting for Humanoid Robots — http://arxiv.org/abs/1909.10080v1
[11] Real-Time Whole-Body Control of Legged Robots with Model-Predictive Path Integral Control — http://arxiv.org/abs/2409.10469v1
[12] Next-Generation Whole-Body Control System of Humanoid Robots — https://arxiv.org/html/2506.20487v5
[13] Control of a Rigid Wing Pumping Airborne Wind Energy System in all Operational Phases — http://arxiv.org/abs/2006.11141v1
[14] On Controller Design for Systems on Manifolds in Euclidean Space — http://arxiv.org/abs/1807.03475v1
[15] Analysis and design of model predictive control frameworks for dynamic operation -- An overview — http://arxiv.org/abs/2307.03004v2
[16] Adaptive Control of Robot Manipulators With Uncertain Kinematics and Dynamics — http://arxiv.org/abs/1403.5204v3
[17] The importance of ensemble techniques for operational space weather forecasting — http://arxiv.org/abs/1806.09861v1
[18] Cold-Tip Temperature Control of Space-borne SatelliteStirlingCryocooler: Mathematical Modeling and Control Investigation — http://arxiv.org/abs/1905.11247v1
[19] Verification of Space Weather Forecasts issued by the Met Office Space Weather Operations Centre — http://arxiv.org/abs/1804.02985v1
[20] Operational Space Control of Constrained and Underactuated Systems — https://doi.org/10.15607/rss.2011.vii.031
[21] SPACE: the SPectroscopic All-sky Cosmic Explorer — http://arxiv.org/abs/0804.4433v1
[22] Operational Space Control of Constrained and Underactuated Systems — https://doi.org/10.7551/mitpress/9481.003.0034
[23] Exact decoupling of the force-position control using the operational space formulation — https://doi.org/10.1109/robot.1992.220155
[24] Newton-Euler, Lagrange and Kirchhoff formulations of rigid body dynamics: a unified approach — http://arxiv.org/abs/1607.00156v1
[25] Predicting the Popularity of GitHub Repositories — http://arxiv.org/abs/1607.04342v1
[26] Generating GitHub Repository Descriptions: A Comparison of Manual and Automated Approaches — http://arxiv.org/abs/2110.13283v1
[27] LLM-based Content Classification Approach for GitHub Repositories by the README Files — http://arxiv.org/abs/2507.21899v1
[28] Analyzing the Accessibility of GitHub Repositories for PyPI and NPM Libraries — http://arxiv.org/abs/2404.17403v2
[29] Automatically Categorising GitHub Repositories by Application Domain — http://arxiv.org/abs/2208.00269v1
[30] On the Popularity of GitHub Applications: A Preliminary Note — http://arxiv.org/abs/1507.00604v3
[31] What's Inside a GitHub Repository? An Empirical Study on the Contents of 10K Projects — http://arxiv.org/abs/2605.16701v2
[32] GitHub Repositories with Links to Academic Papers: Public Access, Traceability, and Evolution — http://arxiv.org/abs/2004.00199v3
[33] Robowflex: Robot Motion Planning with MoveIt Made Easy — http://arxiv.org/abs/2103.12826v2
[34] Evaluating Guiding Spaces for Motion Planning — http://arxiv.org/abs/2210.08640v1
[35] Data-Efficient Learning of High-Quality Controls for Kinodynamic Planning used in Vehicular Navigation — http://arxiv.org/abs/2201.02254v1

---

*Generated by research-bot · topic=`机器人运动学控制与-ros-2` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`deepseek-v4-flash` · sources=35 · duration=211s · 2026-10-16T22:25:21+00:00*
