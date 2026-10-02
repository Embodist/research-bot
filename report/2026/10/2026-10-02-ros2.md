# ROS 2 生态与机器人中间件：发行版、DDS/RMW 选型、实时执行器与工程实践调研报告

**报告日期**：待核实（未获得系统时间戳；本轮证据中最新 arXiv 编号为 `2512.*`，提示检索窗口末端不早于 2025 年 12 月）
**领域**：具身智能 / 机器人中间件（ROS 2、DDS、RMW、实时执行器、ros2_control、Nav2、MoveIt2）
**检索源数量**：25 条候选来源（含 4 条明显离题噪声 [4][5][13][14]，2 条仅跨领域弱相关 [2][18]，1 条跨界类比 [1]）

---

## 摘要（Executive Summary）

本报告的目标是梳理 ROS 2 发行版演进、DDS/RMW（Cyclone DDS / Fast DDS / Zenoh）选型与调优、实时执行器与 ros2_control/Nav2/MoveIt2 工程实践、基准与数据集，以及实时性、分布式部署与 VLA 集成等争议与开放问题。**必须首先声明一个关键限制：本轮提供的 25 条候选证据中，没有任何一条是关于 ROS 2 发行版路线图、DDS/RMW 或 Zenoh 的一手材料。** 四篇被召回的核心 arXiv 论文中，[5]（短视频参与度预测挑战赛）、[13]（图像超分辨率挑战赛）、[14]（抑郁检测）与机器人中间件毫无交集；[4] 是中文百科条目「活性氧」，属于 "ROS" 缩写歧义（*reactive oxygen species*）造成的检索污染。

因此，本报告采取**证据分级 + 缺口显式标注**的写法：

1. **可核查的实证结论集中在「实时执行器与调度」这一狭窄切口**：ROS 2 在 Linux 上的实时调度可被建模为「OS 线程调度 + 中间件层调度（Executor）」的嵌套调度 [21]；学术界已有针对多线程 Executor 上处理链（processing chains）的实时调度与分析工作（RTSS 2022）[24]，以及更早的实时 Executor 探索（ICESS 2020）[19]；并出现了「让回调与 OS 线程建立持久一对一映射、从而绕过中间件层调度」的在研方案（Work in Progress，2025）[21]。C++ 客户端库 rclcpp 为 ROS 2 标准安装的组成部分，有官方仓库可核 [16]。
2. **发行版节奏（Jazzy / Kilted / Rolling）、DDS 实现对比（Cyclone DDS / Fast DDS / Connext）、Zenoh RMW（rmw_zenoh）官方支持级别、micro-ROS 平台矩阵**：**本轮证据为零**，全部标注 `> 待核实`，仅保留人工维护的官方入口作为后续检索种子（`design.ros2.org`、`docs.ros.org`、`github.com/ros2/ros2`）。
3. **ros2_control / Nav2 / MoveIt2 的工程最佳实践**：本轮证据未覆盖其如何具体沉淀 executor、QoS、lifecycle node 的设计，仅能列出官方文档与仓库作为种子资源，标注 `> 待核实`。
4. **真机实时性抖动（jitter）、多机器人分布式部署失败模式、VLA 与 ROS 2 集成**：三者在本轮证据中**完全无一手数据**。仅有两条跨领域线索可作类比：一是时敏任务向邻近算力卸载及其资源分配在车载边缘计算（VEC）中仍是挑战 [1]，可作为「VLA 推理卸载到边缘算力」的类比参照；二是「信任」被 HRI 领域持续列为学习型/共生机器人系统的开放议题（TRUST 2025 @ RO-MAN 2025）[10]，可作为策略部署后安全与信任评估的背景引用。二者均**不可**直接作为 ROS 2 实时性证据。

**证据分级约定**：A = 同行评审论文 / 官方技术报告；B = arXiv 预印本 / 官方代码仓库；C = 第三方复现或权威媒体报道；D = 个人博客与社区帖；E = 不可用。本报告正文对 A/B 级直接陈述，C 级加限定词，D 级仅作线索并另找高等级来源，找不到即标注 `> 待核实`。

---

## 一、关键前沿进展与发行版节奏

### 1.1 本轮证据的可核查事实

| 论断 | 证据 | 等级 | 引用 |
|---|---|---|---|
| ROS（Robot Operating System）被官方描述为一套软件库与工具集 | 官网首页摘要：「ROS - Robot Operating System … a set of software libraries and tools…」 | B（官方站点入口描述） | [3] |
| rclcpp（ROS Client Library for C++）源代码包含在任意 ROS 2 的标准安装中 | 官方 GitHub 仓库描述 | B（官方仓库） | [16] |
| 中文社区存在成体系的 ROS/ROS 2 入门材料（概念、安装、常见问题） | Autolabor 课程、知乎专栏、CSDN 系列帖 | D（个人/机构博客，仅作生态线索） | [6][7][9][11][15][17] |

### 1.2 发行版节奏：**证据缺口**

关于 **Jazzy Jalisco / Kilted Kaiju / Rolling** 的发布说明、支持周期（EOL）、以及各发行版对应的 DDS 默认实现与 RMW 变更，本轮证据中**没有任何可核查来源**——[3] 仅为官网入口描述，[6][7][9][15] 为入门级二手材料且未涉及具体发行版节奏。

> 待核实：ROS 2 各发行版（Jazzy / Kilted / Rolling）的官方发布说明、LTS 支持窗口、默认 RMW 变更记录、REP 相关提案状态。建议一手来源：`docs.ros.org`（发行版文档）、`design.ros2.org`（设计文档）、`github.com/ros2/ros2`（主仓库 release 页）、ROS Discourse 的 release 公告。以上均为**人工维护种子资源，本轮未实时检索**。

> 待核实：micro-ROS 的最新版本、支持的 MCU/RTOS 平台矩阵。种子入口：`https://github.com/micro-ROS/micro_ros_agent`。

### 1.3 检索方法论缺口（必须随报告一并交付）

本轮召回呈现出**严重的术语歧义污染**：英文缩写 "ROS" 同时命中 *reactive oxygen species*（活性氧）[4]，中文检索则大量返回入门博客 [6][8][9][11][15]。此外，[17] 与 [23] 的来源链接在证据集中被截断（形如 `hedJjaC291OfPyaFZYFLI4KQWvqt63NB7dOeveA8wKAaSqX4aplYzQ..`），**链接不可达，等级判定为 E/待核实**，其内容主张本报告不予采信。

下一轮定向检索建议：`ROS 2 Jazzy release notes`、`rmw_zenoh support level`、`ROS 2 real-time executor jitter`、`DDS QoS ROS 2 benchmark`、`micro-ROS RTOS`，并限定 `site:docs.ros.org`、`site:github.com/ros2`、`site:arxiv.org`（cs.RO）+ 时间窗 `2024..2026`。

---

## 二、中间件与实时性（DDS / RMW / Executor）

这是本轮证据**唯一具备实质内容**的章节。

### 2.1 嵌套调度视角：OS 层 + 中间件层

商品化的组件化实时系统（如 Linux 上的 ROS 2 系统）的实时调度，已在「嵌套调度（nested scheduling）」框架下被研究：既存在操作系统线程调度，也存在中间件层调度（例如 ROS 2 Executor）[21]。这一视角的价值在于——**调参必须同时在两层进行**，只调 OS 优先级或只调 Executor 结构都可能失效。

### 2.2 绕过中间件调度的在研方案

一篇标注为 Work in Progress 的工作提出：**通过建立回调（callback）与 OS 线程之间持久的一对一对应关系，来绕过中间件层调度，从而直接套用 OS 调度参数** [21]。

> 待核实：该方案对 ROS 2 Executor 的通用性、最坏情况实时性能、以及对现有多线程 Executor 语义的兼容边界。[21] 自述为 Work in Progress，尚无同行评审结论。

### 2.3 Executor 实时性的学术脉络

| 名称 | 年份 | 机构/出处 | 链接 | 说明 |
|---|---|---|---|---|
| Exploring Real-Time Executor on ROS 2 | 2020 | IEEE ICESS | https://doi.org/10.1109/icess49830.2020.9301530 | 较早面向 ROS 2 实时 Executor 的探索性工作 [19]（A 级，论断限于标题所述范围） |
| Real-Time Scheduling and Analysis of Processing Chains on Multi-threaded Executor in ROS 2 | 2022 | IEEE RTSS | https://doi.org/10.1109/rtss55097.2022.00013 | 针对 ROS 2 多线程 Executor 上处理链的实时调度与分析 [24]（A 级，顶级实时系统会议） |
| Middleware-Transparent Callback Enforcement in Commoditized Component-Oriented Real-time Systems | 2025 | arXiv (WIP) | http://arxiv.org/abs/2505.06546v1 | 嵌套调度框架 + 回调/OS 线程一对一映射思路 [21]（B 级，预印本） |

**演进脉络（谨慎表述）**：从 2020 年的「探索实时 Executor 是否可行」[19]，到 2022 年的「对多线程 Executor 上的处理链做可分析的实时调度理论」[24]，再到 2025 年的「干脆绕开中间件层调度、把回调绑定到 OS 线程」[21]。这条线索显示出社区的一个持续张力：**Executor 作为中间件抽象带来的灵活性，与硬实时可分析性之间存在取舍**。

### 2.4 Executor / callback group 的工程细节

中文社区材料对 ROS 2 回调处理机制、executor 与 callback group 的关系、以及 rclcpp 的 parameter callback 有教程级说明 [20][22][23][25]。

> 待核实：[20][22][23][25] 均为 CSDN/知乎博客（D 级）。其中 [23] 的链接在证据集中被截断、不可达。上述内容**不得作为设计依据**，工程决策应回到 `design.ros2.org` 的 Executor 与 callback group 设计文档（种子资源，本轮未检索）。

### 2.5 DDS / RMW 选型：**全章证据为零**

关于 **Cyclone DDS、Fast DDS、Connext 的吞吐/延迟/发现机制对比**，以及 **RMW 抽象层（`rmw_*`）的兼容性与调优参数**，本轮 25 条来源中无一涉及。

> 待核实：DDS 实现对比（延迟、吞吐、发现开销、QoS 支持矩阵）；RMW 抽象层的版本兼容策略；QoS 不匹配的诊断路径。**结论缺位，不做任何推测性排序。** 建议一手来源：各 DDS 厂商官方文档与基准页、`github.com/ros2/rmw`、ROS 2 QoS 官方文档。

### 2.6 实时 Linux 内核背景

作为接地气的底层前提，已有工作量化评估了用 **Linux RT-Preempt 替换双内核实时方案（RTAI）** 的迁移效果，场景为分布式实时网络 [12]（2016 年 IEEE IECON，A 级；论断限于标题所述范围）。

> 待核实：在 PREEMPT_RT 内核 + ROS 2 的组合下，真机端到端抖动（jitter）与最坏执行时间（WCET）的实测数据。本轮证据中**没有任何此类数字**。

---

## 三、控制与导航（ros2_control / Nav2 / MoveIt2）

### 3.1 结论：本轮证据不足以支撑任何工程结论

子问题 q2 明确指出：候选证据中「除 ROS 2 Executor 调度与 rclcpp 仓库入口外，没有关于 QoS、lifecycle node、rclpy、ros2_control、Nav2、MoveIt2 的设计演进或最佳实践的直接材料」。

因此本节**不做实质性论断**，仅定位缺口：

> 待核实：ros2_control 的 hardware_interface 生命周期与实时控制循环（update rate、`controller_manager` 调度）如何与 ROS 2 Executor 协同；如何避免控制器更新链路上的锁竞争与非确定性。
> 待核实：Nav2 的行为树（Behavior Tree）导航架构如何沉淀 QoS profile 与 lifecycle node 模式；跨进程/跨机的 costmap 与 TF 分发约定。
> 待核实：MoveIt2 的运动规划管线与 ros2_control 的接口边界；规划频率与执行频率不匹配时的工程处理。
> 待核实：rclpy 与 rclcpp 在 lifecycle、QoS 上的抽象差异及其对上层框架的影响。

### 3.2 官方种子资源（人工维护，本轮未实时检索）

| 名称 | 年份 | 机构/作者 | 链接 | 说明 |
|---|---|---|---|---|
| ROS 2 Design Docs（executors / lifecycle / QoS） | ongoing | Open Robotics / ROS 2 | https://design.ros2.org/ | 官方设计文档，理解抽象层的第一入口（种子资源） |
| ros2_control documentation | ongoing | ros-controls | https://control.ros.org/ | 硬件接口与控制器管理（种子资源） |
| Nav2 documentation | ongoing | Open Navigation LLC | https://docs.nav2.org/ | 导航栈与行为树（种子资源） |

> 说明：上述三条为本次调研任务给定的**人工维护种子资源**，未纳入本轮 [1]–[25] 编号证据体系，亦未经实时检索验证其当前内容与版本。

---

## 四、仿真与数据（gz-sim / rosbag2 / Foxglove）

### 4.1 结论

本轮 25 条来源中**没有任何一条**涉及 Gazebo/gz-sim、rosbag2、MCAP 或 Foxglove 的技术细节、性能或版本状态。

> 待核实：gz-sim 与 ROS 2 的桥接（`ros_gz`）现状、物理引擎选择对 Sim2Real 的影响；rosbag2 的 MCAP 后端与默认 SQLite3 后端的读写性能、分片与压缩策略；Foxglove 在 ROS 2 数据可视化与远程调试中的实际采用度。
> 待核实：可用于 ROS 2 中间件评测的**公开基准与数据集**。本轮证据中未出现任何基准榜单、任务集或评测协议。

### 4.2 种子资源

| 名称 | 年份 | 机构/作者 | 链接 | 说明 |
|---|---|---|---|---|
| rosbag2 / MCAP | ongoing | MCAP 社区 | https://mcap.dev/ | 机器人数据记录格式（种子资源，未实时检索） |
| gz-sim | ongoing | GazeboSim | https://github.com/gazebosim/gz-sim | 新一代 Gazebo 仿真（种子资源，未实时检索） |

**注意**：本轮证据中**不存在**关于 SimplerEnv、LIBERO、Open X-Embodiment、DROID 等具身智能基准的可核查来源，因此本报告不将其列入「数据集与基准」表，避免引入未检索内容。

---

## 五、分布式与安全（Zenoh / DDS Security）

### 5.1 跨领域类比：时敏任务卸载

在本轮唯一涉及「分布式 + 时敏约束」的文献中，作者指出：车载边缘计算（VEC）通过将计算密集任务无线卸载到路侧单元来提升效率，但**时敏应用下的任务卸载与资源分配仍具挑战**（摘要原文：*efficient task offloading and resource allocation for time-critical applications in VEC remain challenging*）[1]。

**该文的边界必须说清楚**：它不涉及 ROS 2、机器人本体或 VLA，属于跨领域类比，**不能作为 ROS 2 分布式部署的证据** [1]（2025 年 arXiv 预印本，B 级，跨领域）。

> 待核实：把 VLA 大模型推理从机器人本体卸载到边缘/辅助算力，是否会因网络抖动破坏闭环控制的稳定性；这种「ROS 2 + 卸载」架构有无实验证据。本轮证据中**没有**。

### 5.2 Zenoh 与 DDS Security：**证据为零**

关于 **Zenoh 作为 ROS 2 RMW（`rmw_zenoh`）的落地状态与官方支持级别**、**`zenoh-plugin-ros2dds` 的桥接能力**、以及 **DDS Security（认证/加密/访问控制）在 ROS 2 中的启用方式与性能代价**，本轮 25 条来源中无一涉及。

> 待核实：`rmw_zenoh` 的支持等级（experimental / supported）、与 DDS 的安全模型差异、跨广域网场景下的发现与路由行为。
> 待核实：DDS Security 开启后对延迟与 CPU 占用的影响；多机器人跨组织域时的证书与权限分发实践。

| 名称 | 年份 | 机构/作者 | 链接 | 说明 |
|---|---|---|---|---|
| eclipse-zenoh/zenoh-plugin-ros2dds | ongoing | Eclipse Zenoh | https://github.com/eclipse-zenoh/zenoh-plugin-ros2dds | Zenoh 桥接 DDS（种子资源，未实时检索） |

---

## 六、AI 策略与 ROS 2 集成

### 6.1 可用的间接线索

| 论断 | 证据 | 等级 | 引用 |
|---|---|---|---|
| 「信任」是学习型/共生机器人系统需专门研讨的开放议题 | TRUST 2025（SCRITA + RTSS @ RO-MAN 2025）合并举办，目标为推进人与机器人双视角的信任研究；摘要未提及 ROS 2、实时性或 VLA | B（arXiv 预印本） | [10] |
| 时敏任务卸载仍需解决资源分配问题 | VEC 场景下任务卸载与资源分配对时敏应用仍是挑战 | B（arXiv 预印本，跨领域） | [1] |
| 基础模型透明度是被持续度量的议题 | 2025 Foundation Model Transparency Index 存在 | B（arXiv 预印本，跨领域） | [18] |

对 [18] 的使用需格外克制：该证据仅表明「基础模型透明度」这一议题在 2025 年被持续度量，**本轮证据未显示其覆盖机器人策略模型或 VLA**。

> 待核实：Foundation Model Transparency Index (2025) 是否包含 VLA / 机器人基础模型这一类别，以及其评估维度是否涉及策略部署的安全披露。

### 6.2 VLA 与 ROS 2 集成的工程缺口

> 待核实：学习型策略（VLA）与 ROS 2 集成的工程实践与失败案例，包括但不限于：推理延迟与控制频率不匹配、策略输出的非确定性、安全边界与急停机制、经 `ros2_control` 硬件接口适配时的时序约束。
> 待核实：VLA 推理的算力卸载（本体 GPU ↔ 边缘算力）在 ROS 2 通信框架下的可行性与代价 [1] 仅提供跨领域类比。

**本报告不给出任何 VLA 模型选型建议**，因为本轮证据中不存在相关模型、数据集或评测的可核查来源。

---

## 七、经典参考资料与工程规范

### 7.1 经典与奠基性工作（表格）

| 名称 | 年份 | 机构/作者 | 链接 | 说明 |
|---|---|---|---|---|
| ROS（Robot Operating System）官方网站 | ongoing | Open Robotics / ROS 2 社区 | https://www.ros.org/ | 官方入口，证据 [3] 仅提供工具/库定位描述，无技术指标 |
| ROS Wiki（中文页面） | 2007– | ROS 社区 | https://wiki.ros.org/cn | ROS 1 时代官方 Wiki 的中文入口 [8]（内容覆盖范围本轮未核实） |
| rclcpp（ROS Client Library for C++） | ongoing | ros2 组织 | https://github.com/ros2/rclcpp | ROS 2 官方 C++ 客户端库仓库；源代码包含在任意标准安装中 [16] |
| Exploring Real-Time Executor on ROS 2 | 2020 | IEEE ICESS | https://doi.org/10.1109/icess49830.2020.9301530 | ROS 2 实时 Executor 的早期探索 [19]（A 级） |
| Real-Time Scheduling and Analysis of Processing Chains on Multi-threaded Executor in ROS 2 | 2022 | IEEE RTSS | https://doi.org/10.1109/rtss55097.2022.00013 | 多线程 Executor 上处理链的实时调度与分析 [24]（

## 参考来源

[1] Real-Time Service Subscription and Adaptive Offloading Control in Vehicular Edge Computing — http://arxiv.org/abs/2512.14002v1
[2] Real time state monitoring and fault diagnosis system for motor based on LabVIEW — http://arxiv.org/abs/1806.09998v1
[3] ROS : Home — https://www.ros.org/
[4] 活性氧_百度百科 — https://baike.baidu.com/item/%E6%B4%BB%E6%80%A7%E6%B0%A7/6657751
[5] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1
[6] 终于有人把 ROS (机器人操作系统)讲明白了-CSDN博客 — https://blog.csdn.net/usstmiracle/article/details/134582549
[7] ROS  (机器人操作系统) - 云飞机器人中文维基 — https://yfrobotics.github.io/robowiki-cn/ros/
[8] cn -  ROS  Wiki — https://wiki.ros.org/cn
[9] ROS 简介-从零开始讲解 ROS （适合超零基础阅读）-CSDN博客 — https://blog.csdn.net/qq_25267657/article/details/84316111
[10] TRUST 2025: SCRITA and RTSS @ RO-MAN 2025 — http://arxiv.org/abs/2509.11402v1
[11] Introduction · Autolabor- ROS 机器人入门课程《 ROS 理论与 ... — https://www.autolabor.com.cn/book/ROSTutorials/
[12] From RTAI to RT-Preempt a quantative approach in replacing Linux based dual kernel real-time operating systems with Linux RT-Preempt in distributed real-time networks for educational ICT systems — https://doi.org/10.1109/iecon.2016.7793116
[13] NTIRE 2025 Challenge on Image Super-Resolution (x4): Methods and Results — http://arxiv.org/abs/2504.14582v3
[14] SINAI at eRisk@CLEF 2025: Transformer-Based and Conversational Strategies for Depression Detection — http://arxiv.org/abs/2509.19861v1
[15] ROS 从入门到精通0-3：  ROS 简介、安装与常见问题 — https://zhuanlan.zhihu.com/p/498742111
[16] GitHub - ros2/ rclcpp :  rclcpp  (ROS Client Library for C++) — https://github.com/ros2/rclcpp
[17] 20-ROS2  初探 - 知乎 — hedJjaC291OfPyaFZYFLI4KQWvqt63NB7dOeveA8wKAaSqX4aplYzQ..
[18] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1
[19] Exploring Real-Time Executor on ROS 2 — https://doi.org/10.1109/icess49830.2020.9301530
[20] ROS2 回调处理机制 executor+callbackgroup _ ros2   callback group -CSDN博客 — https://blog.csdn.net/weixin_60864335/article/details/131134956
[21] Work in Progress: Middleware-Transparent Callback Enforcement in Commoditized Component-Oriented Real-time Systems — http://arxiv.org/abs/2505.06546v1
[22] ROS2学习笔记4_ rclcpp -CSDN博客 — https://blog.csdn.net/m0_55260921/article/details/149706560
[23] ROS2     rclcpp   Parameter   Callback   [Tutorial]_知乎 — hedJjaC291OfPyaFZYFLI4KQWvqt63NBkqlHYkqB8P1sRolFyj5hmw..
[24] Real-Time Scheduling and Analysis of Processing Chains on Multi-threaded Executor in ROS 2 — https://doi.org/10.1109/rtss55097.2022.00013
[25] ROS2 探索(二) executor _ rclcpp :: executor s::multithreaded executor -CSDN博客 — https://blog.csdn.net/qq_16893195/article/details/113123386


---

*Generated by research-bot · topic=`ros2` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360 · skills=deep-research, frontier-tracking, paper-survey, evidence-grading · model=`deepseek-v4-flash` · sources=25 · duration=272s · 2026-10-02T03:26:42+00:00*
