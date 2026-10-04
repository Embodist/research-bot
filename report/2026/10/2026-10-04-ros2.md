# ROS 2 生态与机器人中间件：发行版、DDS/RMW/Zenoh、实时控制与工程栈前沿综述（2024–2026）

**日期**：2026-10-04（UTC） ｜ **领域**：机器人中间件 / ROS 2 生态（DDS、RMW、Zenoh、实时执行、Nav2/MoveIt2/仿真、分布式与安全） ｜ **可引用候选来源**：98 条，编号 [1]–[98] ｜ **实际引用编号**：见文末「参考来源」 ｜ **证据分级**：A（同行评审）> B（arXiv/官方仓库）> C（第三方评测）> D（社区）> E（不可用）

---

## 摘要（Executive Summary）

**证据基础与方法说明**：本轮候选来源共 [1]–[98]，但结构化发现显示检索召回质量严重不均。子问题 q1（发行版与生态进展）的候选块 **3/3 全部为误召回**（天文光谱合成代码 Cloudy 2025 版 [90]、高能物理 PDF 演化程序 HOPPET v2 [91]、2013 年行星历表 INPOP10e [86]），全部为「release / 新版本」关键词导致的跨领域噪声；q2/q4/q5 亦混入短视频参与度预测 [2]、基础模型透明度指数 [67]、LabVIEW 电机监测 [46] 等无关条目。因此本报告以「**已确证结论 + 明确标注的证据缺口**」双轨组织，凡候选证据不支持的判断一律写 `> 待核实`，不作推测性补全。

**三条最稳固的结论（均有可核查来源）**

1. **近两年 ROS 2 的一手学术关注重心在「通信的可预测性与鲁棒性」，而非发行版特性本身。** 代表工作集中在 DDS QoS 策略组合的静态验证 [3]、RELIABLE topic 的 backpressure 解耦 [4]、DDS 心跳/重传机制的概率化延迟建模 [20]、无线大负载链路优化 [41]、WAN 组网 [22]。这构成 2024–2026 年最密集的一条技术线。
2. **综述体裁从「ROS 2 是什么」升级为「ROS 2 的限制在哪里」。** [62] 以三个研究问题系统梳理 ROS 2 相对 ROS 1 的改进、新限制与生态演进（ACM Computing Surveys，同行评审，citations=14）；[80] 汇总近六年实时性分析与增强工作；[30] 提出 Space（物理拓扑）/Time（控制回路时间可预测性）/State（状态管理）三维框架，明确把 DDS 与 Zenoh 并列为 ROS 2 的核心中间件基础设施。
3. **评测层面尚无统一基准，评测方法以「自建实验」与「需求引出」两类为主。** [50] 用产业界软件工程师引出的需求作为标尺比较 ROS 2 Jazzy 与 AUTOSAR Adaptive R24-11；[61] 指出网络层检测存在盲区，评测需转向物理一致性监测（运动学/动力学不变量、电机级信号）。候选集中 **未出现任何 ROS 2 专属基准套件、数据集或榜单** `> 待核实`。

**主要证据缺口（须补检索后再断言）**
- ROS 2 发行版时间线与版本节奏、各发行版新增特性：**无一手证据** `> 待核实`；唯一可核查锚点是 [50] 中出现的「ROS 2 Jazzy」被用作 2026 年研究的对比基线。
- rcl / rclcpp / rclpy / rmw 分层抽象的官方设计动机文献：候选集缺失，仅可指向种子设计文档 `> 待核实`。
- Nav2 / MoveIt2 / micro-ROS / rosbag2 四个组件的近两年具体进展：除 Nav2 一篇实现导向综述 [63] 外**基本空白**。
- Zenoh RMW（rmw_zenoh）的官方量化数据：候选集仅有第三方对比 [18]，无官方基准 `> 待核实`。
- VLA 策略与 ROS 2 接口（节点/action/topic 化）的规范或实践：无一手证据 `> 待核实`。

---

## 一、关键前沿进展与发行版节奏

### 1.1 发行版节奏：本轮无一手证据（最重要的缺口）

本批次候选中**不存在**任何 ROS 2 官方发行公告、distro 文档、REP 提案或变更日志。结构化发现 q1 的全部候选条目均属天文/高能物理软件的版本发布说明：[90] 为 Cloudy 2025 版（j-resolved Lyman α 双线、Stout 数据库更新，arXiv:2508.01102v1）、[91] 为 HOPPET v2（N³LO QCD 演化、新增 Python 接口与 CMake 构建选项，arXiv:2510.09310v3）、[86] 为 2013 年 INPOP10e 行星历表。三者与 ROS 2 零相关。

> 待核实：ROS 2 近 1–2 年（2024–2026）的发行版清单、发布节奏、各发行版新增核心特性与支持周期。核实路径建议以官方 distro 文档、REP 提案与本仓库 issue/PR 为准（种子资源见第七章）。
> 待核实：工具链层面（colcon/ament、ros2cli、rosbag2、rviz2、ros2_control 发布变更）的任何版本化结论。

**唯一可核查的发行版锚点**：[50] 的对照实验以 **ROS 2 Jazzy** 与 **AUTOSAR Adaptive Platform R24-11** 为对象，说明 Jazzy 在 2026 年的汽车中间件研究中被作为 ROS 2 侧基线使用。
- 热度证据：`> 待核实`（候选块未提供引用数）[50]
- 权威证据：arXiv 预印本 cs.SE，未见同行评审信息 [50]
- 关注度：低 — 依据：无引用数、无社区热度信号，仅 2026-04 预印本 [50]
- 推荐度：★★★☆☆ — 作为「发行版存在性与产业对照」的锚点可用，不能作为节奏结论 [50]

### 1.2 生态级与结构级进展（最新进展，2024–2026）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| ROS 2 in a Nutshell: A Survey | 2026 | `> 待核实` | citations=14 [62] | ACM Computing Surveys（同行评审期刊）[62] | 中 — 发表数月即 14 次引用，权威综述期刊 [62] | ★★★★★ | https://doi.org/10.1145/3815113 | 以 RQ1/RQ2 梳理 ROS 2 相对 ROS 1 的改进、新限制与重设计挑战进展，可作分类骨架 [62] |
| A Survey of Real-Time Support, Analysis, and Advancements in ROS 2 | 2025 | `> 待核实` | `> 待核实` [80] | arXiv 预印本 cs.RO，候选块未标 venue [80] | 中 — 依据：cs.RO 综述体裁，无引用/下载数据 [80] | ★★★★☆ | http://arxiv.org/abs/2601.10722v2 | 汇总近六年对 ROS 2 的分析、增强与扩展工作，工程栈主干预备文献 [80] |
| The Three Dimensions of ROS 2 Middleware | 2026 | 作者含 Angelo Corsaro `> 待核实其他作者` [30] | `> 待核实` [30] | arXiv 预印本 cs.RO（未评审）[30] | 中 — 依据：2026-07 新出预印本 + 综述定位，无引用数据 [30] | ★★★★☆ | http://arxiv.org/abs/2607.01304v1 | 提出 Space/Time/State 三维分析框架，指出 DDS/Zenoh 在动态受限无线网下的结构性局限 [30] |
| Harness Engineering for Physical AI: Robot Middleware Is the Harness Layer | 2026 | `> 待核实` | `> 待核实` [32] | `> 待核实`（候选块未提供 venue/摘要）[32] | `> 待核实` [32] | ★★★☆☆ | http://arxiv.org/abs/2606.09416v1 | 标题即主张：机器人中间件是 Physical AI 的 harness 层；需读全文核实论证强度 [32] |

**要点**
- 生态叙事正在从「ROS 2 的通信能力」转向「ROS 2 作为 AI 系统的 harness/约束层」[32]，与 [62] 关于「新限制」的问题设定方向一致。
- 分布式执行被反复描述为 ROS 2 的既有定位（modularity / distributed execution / communication）[80]，但候选证据中**没有任何多机部署的实操细节或性能数字** `> 待核实`。

---

## 二、中间件与实时性（DDS / RMW / Executor）

### 2.1 通信与 DDS（最新进展，2024–2026）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Dependency Chain Analysis of ROS 2 DDS QoS Policies: From Lifecycle Tutorial to Static Verification | 2025 | `> 待核实` | `> 待核实` [3] | arXiv 预印本 cs.NI [3] | 中 — 依据：针对 20+ QoS 策略「安全组合 + 静态验证」的空白 [3] | ★★★★☆ | http://arxiv.org/abs/2509.03381v1 | 指出 ROS 2 用户缺乏策略组合安全性指导，提出依赖链分析与静态验证路径 [3] |
| Adaptive Bridge: A Proxy-Based Decoupling Layer for Mitigating DDS Backpressure in ROS 2 | 2026 | `> 待核实` | `> 待核实` [4] | arXiv 预印本 cs.NI [4] | 中 — 依据：直击 RELIABLE topic 上单订阅者拖垮全链路的真实痛点 [4] | ★★★★☆ | http://arxiv.org/abs/2608.15380v2 | 用代理式解耦层隔离受限订阅者，保护其余（含安全关键）订阅者的吞吐与延迟 [4] |
| Probabilistic Latency Analysis of the Data Distribution Service in ROS 2 | 2025 | `> 待核实` | `> 待核实` [20] | arXiv 预印本 cs.NI [20] | 中 — 依据：对 DDS 心跳/选择性重传机制做概率化延迟建模 [20] | ★★★★☆ | http://arxiv.org/abs/2508.10413v1 | 把 UDP + DDS 的可靠性机制（周期心跳、ACK、重传）纳入延迟分布分析 [20] |
| Optimizing ROS 2 Communication for Wireless Robotic Systems | 2025 | `> 待核实` | `> 待核实` [41] | arXiv 预印本 cs.NI [41] | 中 — 依据：无线链路上大负载（图像、点云）是公认瓶颈 [41] | ★★★★☆ | http://arxiv.org/abs/2508.11366v1 | 指出默认 DDS 栈在丢包链路下显著退化，并给出优化方向 [41] |
| ROS2 Connect: A new ROS2 over WAN Solution | 2026 | `> 待核实` | `> 待核实` [22] | arXiv 预印本 cs.RO [22] | 中 — 依据：DDS/RTPS 依赖组播发现，WAN 环境通常不可用，属长期痛点 [22] | ★★★★☆ | http://arxiv.org/abs/2608.25102v1 | 针对广域网场景绕过组播发现限制的 ROS 2 组网方案 [22] |
| Performance Evaluation of ROS2-DDS middleware implementations facilitating Cooperative Driving in Autonomous Vehicle | 2024 | `> 待核实` | `> 待核实` [21] | arXiv 预印本 [21] | 低 — 依据：无引用/下载数据，领域限于协同驾驶 [21] | ★★★☆☆ | http://arxiv.org/abs/2412.07485v1 | 面向自动驾驶协同场景的多 DDS 实现性能对比 [21] |

### 2.2 实时性与 Executor 模型

- **综述主干**：[80] 覆盖 ROS 2 实时支持的分析与增强工作，可作入口，但需注意其为预印本、无引用数据（热度 `> 待核实`；权威 arXiv cs.RO 未评审；关注度 中；推荐度 ★★★★☆）[80]。
- **嵌套调度问题**：[65] 指出 ROS 2 on Linux 存在 OS 线程调度 + 中间件层调度（ROS 2 Executor）的嵌套调度问题，并尝试在中间件层做透明的 callback 约束（"Work in Progress" 状态）。热度 `> 待核实`；权威 arXiv cs.OS 预印本；关注度 中（问题指向明确）；推荐度 ★★★★☆ [65]。
- **与控制理论调度对接**：[66] 处理 ROS 2 与经典实时周期任务调度之间的语义鸿沟（2024）。热度 `> 待核实`；权威 arXiv 预印本；关注度 中；推荐度 ★★★★☆ [66]。
- **嵌入式实时**：[64] 面向 micro-ROS 的预算式实时 Executor（2021），属该方向的经典工作。热度 `> 待核实`；权威 arXiv 预印本（2105.05590）；关注度 中（被后续 micro-ROS 实时讨论反复引用，但候选块无引用数佐证）；推荐度 ★★★★☆ [64]。
- **延迟基础分析**：[23] ROS 2 多节点系统延迟分析（2021），是 [20] 一类后续工作的前置。热度 `> 待核实`；权威 arXiv 预印本；关注度 中；推荐度 ★★★☆☆ [23]。
- **DDS 实现横评**：[7] 对 DDS 实现的实验性性能评测做综述（2023）。热度 `> 待核实`；权威 arXiv 预印本（候选块未标 venue）；关注度 中（选型时的常见入口）；推荐度 ★★★★☆ [7]。另 [5] 专门考察组播对 DDS 性能的影响（2022），是「默认配置为何在真实网络退化」的机制性补充。热度 `> 待核实`；权威 arXiv 预印本；关注度 低–中；推荐度 ★★★☆☆ [5]。

### 2.3 本节明确缺口

> 待核实：rcl / rclcpp / rclpy / rmw 的分层抽象与 QoS 设计动机的一手权威文献（官方设计文档 + REP）在本批候选中缺失。
> 待核实：rmw_zenoh 与 rmw_cyclonedds / rmw_fastrtps 的可比量化数据（同一硬件、同一负载口径下的延迟/吞吐/CPU）。候选集中仅有 [18] 的 Zenoh/MQTT/Kafka/DDS 通用对比：热度 `> 待核实`；权威 arXiv 预印本（2023）；关注度 `> 待核实`（无下载/引用数据）；推荐度 ★★★☆☆ [18]。
> 待核实：Executor 在 2024–2026 的官方实现变更（如回调组、并行执行策略的接口演进）无版本级证据。

---

## 三、控制与导航（ros2_control / Nav2 / MoveIt2）

### 3.1 ros2_control

- **[24] 模块化参考生成架构（2026）**：把「采集—校验—插值参考」的逻辑与控制律解耦，引入独立的 Reference Generator 组件，使控制器与机器人形态解耦。热度 `> 待核实`；权威 arXiv 预印本 cs.RO；关注度 中 — 依据：直接对应 ros2_control 长期痛点的架构性提案 [24]；推荐度 ★★★★☆。
- **实时硬化路径**：[64]（micro-ROS 预算式 Executor）与 [65]（嵌套调度下的 callback 约束）为控制器实时性提供底层支撑思路 [64][65]。
- **产业对照**：[50] 以汽车域引出的需求比较 ROS 2 Jazzy 与 AUTOSAR Adaptive R24-11，可作为控制/通信中间件的合规性参照；热度 `> 待核实`；权威 arXiv cs.SE 预印本；关注度 低；推荐度 ★★★☆☆ [50]。

> 待核实：ros2_control 的硬件接口（hardware_interface）规范、控制器管理器（controller_manager）与实时循环在 2024–2026 的变更细节与最佳实践。官方文档见第七章种子资源。

### 3.2 Nav2

- 唯一直接来源：**[63] Nav2 for Autonomous Mobile Robots: An Implementation Oriented Survey of Architecture, Components, and Practical Limitations**（IJMERR，DOI 10.18178/ijmerr.15.5.496-513）。热度 `> 待核实`（候选块未提供 citations）；权威：同行评审期刊（IJMERR）；关注度 中 — 依据：实现导向综述且专述 practical limitations，填补官方文档不写的边界条件 [63]；推荐度 ★★★★☆。
- 该综述定位为「架构 + 组件 + 实际限制」，是候选集中唯一可用于 Nav2 章节的主干文献 [63]。

> 待核实：Nav2 的 2024–2026 版本演进（行为树节点、控制器插件、costmap 层、生命周期管理）具体变化；官方文档见第七章种子资源。
> 待核实：Nav2 的多机器人/分布式导航实践与量化性能数据。

### 3.3 MoveIt2

**候选证据完全空白**。逐条核查 [2][13][67][71][78][80] 均未提及 MoveIt2 或运动规划库在 ROS 2 下的工程实践。仅有的相关规划类来源（[74] 引导空间评估、[76] 局部运动规划基准、[79] 预测性复合 SDF 实时规划）**均非 MoveIt2 相关**，属运动规划领域的一般性文献 [74][76][79]。

> 待核实：MoveIt2 在 2024–2026 的进展、与 ros2_control 的集成方式、以及与 VLA/学习型策略的接口实践。种子仓库见第七章。
> 待核实：MoveIt2 的基准与数据集（如规划器成功率/耗时对比）在候选集中无任何来源。

---

## 四、仿真与数据（gz-sim / rosbag2 / Foxglove）

### 4.1 仿真

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Bridging the Basilisk Astrodynamics Framework with ROS 2 for Modular Spacecraft Simulation and Hardware Integration | 2025 | `> 待核实` | `> 待核实` [11] | arXiv 预印本 cs.RO [11] | 中 — 依据：开源轻量桥接器，支持实时性与硬件在环，属仿真/ROS 2 集成的少见具体工程 [11] | ★★★☆☆ | http://arxiv.org/abs/2512.09833v2 | 把高保真航天动力学仿真器 Basilisk 与 ROS 2 打通，面向模块化仿真与硬件集成 [11] |
| Task adaptation of Vision-Language-Action model: 1st Place Solution for the 2025 BEHAVIOR Challenge | 2025 | `> 待核实` | `> 待核实` [71] | arXiv 预印本 cs.RO，竞赛方案报告，非同行评审 [71] | 中 — 依据：挑战赛冠军方案属性带来关注，但候选块无榜单/讨论量化信号 [71] | ★★☆☆☆ | http://arxiv.org/abs/2512.06951v2 | 照片级仿真中 50 项长程家务任务（双臂操作 + 导航 + 上下文决策），基于 Pi0.5 架构改造（flow matching 相关噪声、可学习混合层注意力、System 2 阶段跟踪）[71] |

**要点与缺口**
- 仿真侧证据集中在「**仿真器与 ROS 2 的桥接**」[11] 与「**照片级仿真中的长程任务基准**」[71] 两类，前者是工程集成，后者是策略评测。
- gz-sim（新一代 Gazebo）、Isaac 系仿真器的 ROS 2 侧版本进展在候选集中**无一手证据** `> 待核实`（种子仓库见第七章）。
- [71] 的贡献主体是 VLA 策略而非 ROS 工程栈，引用时应严格限定其证据范围 [71]。

### 4.2 数据记录格式

- 候选集中**没有** rosbag2 或 MCAP 的技术来源 `> 待核实`。可用的可核查资产仅为种子资源中的 rosbag2 / MCAP 官方站点（见第七章「数据集与基准」表），其内容未在本轮实时检索中验证。
- **Foxglove** 在候选集中**无任何来源** `> 待核实`。

> 待核实：rosbag2 的存储后端（MCAP / sqlite3）、序列化与 QoS 交互、以及大规模回放性能的 2024–2026 演进。

---

## 五、分布式与安全（Zenoh / DDS Security）

### 5.1 Zenoh 与分布式组网

- **[30] 把 DDS 与 Zenoh 并列为 ROS 2 的核心中间件基础设施**，并提出 Space/Time/State 三维框架，指出两者在动态、资源受限的无线环境下都暴露**结构性局限**。热度 `> 待核实`；权威 arXiv 预印本 cs.RO（未评审），作者含 Angelo Corsaro（与 Zenoh/Eclipse 生态相关）；关注度 中 — 依据：2026-07 新预印本、综述定位 [30]；推荐度 ★★★★☆。
- **[22] ROS2 over WAN**：直指 DDS/RTPS 的组播发现机制在 WAN 不可用这一根因，是分布式部署的关键工程约束。热度 `> 待核实`；权威 arXiv 预印本 cs.RO；关注度 中；推荐度 ★★★★☆ [22]。
- **[41] 无线优化**：默认 DDS 栈在丢包/高带宽需求下退化，是野外与移动机器人部署的核心障碍 [41]。热度 `> 待核实`；权威 arXiv cs.NI 预印本；关注度 中；推荐度 ★★★★☆。
- **[18] Zenoh vs MQTT vs Kafka vs DDS 吞吐/延迟对比**：候选集中唯一的 Zenoh 量化对比来源，但**为第三方对比、非官方基准**。热度 `> 待核实`；权威 arXiv 预印本（2023）；关注度 `> 待核实`；推荐度 ★★★☆☆ [18]。按证据分级纪律，其数字应加限定词使用。

> 待核实：rmw_zenoh 的官方性能数字、与 rmw_cyclonedds/rmw_fastrtps 的同口径对比、以及 zenoh-plugin-ros2dds 桥接模式的适用边界。种子项目见第七章。

### 5.2 安全

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Physics-Based Attack Detection for ROS 2 Robotic Systems: A Survey of Physics-Based Validation and Open Challenges | 2026 | `> 待核实` | citations=0 [61] | IEEE Open Journal of the Industrial Electronics Society（同行评审期刊）[61] | 低 — 依据：引用数 0，属新发表综述 [61] | ★★★★☆ | https://doi.org/10.1109/OJIES.2026.3731477 | 指出通过网络层检查的攻击仍可能违反运动/感知/控制的物理规律，评测转向物理一致性监测（运动学/动力学不变量、功率平衡、电流–速度相关性）[61] |
| SROS2: Usable Cyber Security Tools for ROS 2 | 2022 | `> 待核实` | `> 待核实` [59] | arXiv 预印本（2208.02615）[59] | 中 — 依据：SROS2 是 ROS 2 官方安全工具链的核心组件，属入门必读 [59] | ★★★★☆ | http://arxiv.org/abs/2208.02615v1 | ROS 2 安全工具链与可用性讨论 [59] |
| Credential Masquerading and OpenSSL Spy: Exploring ROS 2 using DDS security | 2019 | `> 待核实` | `> 待核实` [6] | arXiv 预印本 [6] | 低–中 — 依据：较早的 DDS Security 攻击面分析，仍被安全章节引用 [6] | ★★★☆☆ | http://arxiv.org/abs/1904.09179v2 | 对 ROS 2 使用 DDS Security 时的凭证伪装与 OpenSSL 侧信道问题做剖析 [6] |
| Security and Performance Considerations in ROS 2: A Balancing Act | 2018 | `> 待核实` | `> 待核实` [8] | arXiv 预印本 [8] | 低 — 依据：发表较早，作为「安全 vs 性能」权衡的经典起点 [8] | ★★★☆☆ | http://arxiv.org/abs/1809.09566v1 | 提出安全机制引入后性能开销的权衡框架 [8] |

**要点**
- 安全评测的核心张力被明确表述为：**网络层合规 ≠ 物理层合规**，因此需要电机级/动力学级监测 [61]。
- **多机器人分布式协作**的间接相关证据：[84] 多机器人协作机器人学习综述（2024，热度 `> 待核实`，权威 arXiv 预印本，关注度 中，推荐度 ★★★☆☆）[84]；[83] 面向多机器人 SLAM 的分布式位姿图优化强化学习方法（2025，热度 `> 待核实`，权威 arXiv 预印本，关注度 `> 待核实`，推荐度 ★★☆☆☆）[83]。二者均**不涉及 ROS 2 通信层实现**，仅作分布式协作的方向参考。

> 待核实：DDS Security 的 2024–2026 实践（插件选型、证书分发、性能代价实测）与 ROS 2 官方安全指南的一致性。种子与官方文档见第七章。

---

## 六、AI 策略与 ROS 2 集成

**本节是全报告证据最薄的一节**：候选集中与「VLA/具身智能 × ROS 2」直接相关的条目为零，仅有若干可迁移的相邻证据。

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Harness Engineering for Physical AI: Robot Middleware Is the Harness Layer | 2026 | `> 待核实` | `> 待核实` [32] | `> 待核实` [32] | `> 待核实` [32] | ★★★☆☆ | http://arxiv.org/abs/2606.09416v1 | 主张机器人中间件是 Physical AI 的 harness 层，是「中间件作为 AI 约束/编排层」这一叙事的代表条目，需读全文验证 [32] |
| Task adaptation of Vision-Language-Action model: 1st Place Solution for the 2025 BEHAVIOR Challenge | 2025 | `> 待核实` | `> 待核实` [71] | arXiv 预印本 cs.RO（竞赛方案，非同行评审）[71] | 中 [71] | ★★☆☆☆ | http://arxiv.org/abs/2512.06951v2 | 照片级仿真 50 项长程任务上的 VLA 策略改造（Pi0.5、flow matching、可学习混合层注意力、System 2 跟踪）[71]；与 ROS 2 集成方式未在摘要中体现 |
| CLIPSwarm: Converting text into formations of robots | 2023 | `> 待核实` | `> 待核实` [82] | arXiv 预印本 [82] | `> 待核实` [82] | ★★☆☆☆ | http://arxiv.org/abs/2311.11047v1 | 语言→机器人编队的早期尝试，可作为「语言接口驱动多机器人」的历史参照 [82] |
| ALOHA 2: An Enhanced Low-Cost Hardware for Bimanual Teleoperation | 2024 | `> 待核实` | `> 待核实` [27] | arXiv 预印本 [27] | 中 — 依据：低成本双臂遥操作硬件在具身智能社区广受关注，但候选块无量化热度信号 [27] | ★★★☆☆ | http://arxiv.org/abs/2405.02292v1 | 双臂遥操作硬件平台，是数据采集侧的基础设施，非中间件栈 [27] |
| State-of-the-art in Robot Learning for Multi-Robot Collaboration: A Comprehensive Survey | 2024 | `> 待核实` | `> 待核实` [84] | arXiv 预印本 [84] | 中 [84] | ★★★☆☆ | http://arxiv.org/abs/2408.11822v1 | 多机器人协作学习综述，提供学习侧全景 [84] |

**要点与缺口**

> 待核实：把 VLA / 策略模型封装为 ROS 2 节点或 Action 接口的规范与实践（含推理频率、消息 schema、生命周期管理），候选集中**无一手证据**。
> 待核实：ROS 2 侧面向具身智能的数据采集—训练—回放闭环（rosbag2/MCAP ↔ 策略训练 → 部署）的端到端工程报告。
> 注意术语噪声：[34] *Memory as Middleware for Self-Improving AI Agents* 属 AI Agent 记忆机制，与机器人中间件**同名不同域**，不应作为 ROS 2 章节证据（热度 `> 待核实`；权威 arXiv 预印本；关注度 `> 待核实`；推荐度 ★☆☆☆☆）[34]。

---

## 七、经典参考资料与工程规范

### 7.1 经典与奠基性工作

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| ROS 2 Design Docs（executors, lifecycle, QoS） | 持续更新 | Open Robotics / ROS 2 | `> 待核实` | 官方设计文档（第一手权威） | 高 — 依据：ROS 2 架构与 QoS 设计动机的规范性来源 | ★★★★★ | https://design.ros2.org/ | 本轮**未实时检索验证具体页面内容**；rcl/rclcpp/rclpy/rmw 分层与 Executor 设计动机的核实入口 |
| ROS 2 in a Nutshell: A Survey | 2026 | `> 待核实` | citations=14 [62] | ACM Computing Surveys（同行评审）[62] | 中 [62] | ★★★★★ | https://doi.org/10.1145/3815113 | 目前最系统的 ROS 2 综述之一，RQ1/RQ2 可直接作为「限制与挑战」分类骨架 [62] |
| A Survey on Experimental Performance Evaluation of DDS Implementations | 2023 | `> 待核实` | `> 待核实` [7] | arXiv 预印本 [7] | 中 — 依据：DDS 选型的常见入口 | ★★★★☆ | http://arxiv.org/abs/2310.16630v1 | DDS 实现性能评测方法的综述，选型方法论起点 [7] |
| Latency Analysis of ROS2 Multi-Node Systems | 2021 | `> 待核实` | `> 待核实` [23] | arXiv 预印本 [23] | 中 [23] | ★★★☆☆ | http://arxiv.org/abs/2101.02074v3 | ROS 2 多节点延迟分析的早期奠基工作，后续概率化模型 [20] 的前置 [23] |
| Budget-based real-time Executor for Micro-ROS | 2021 | `> 待核实` | `> 待核实` [64] | arXiv 预印本（2105.05590）[64] | 中 [64] | ★★★★☆ | http://arxiv.org/abs/2105.05590v2 | micro-ROS 实时 Executor 的经典设计 [64] |
| SROS2: Usable Cyber Security Tools for ROS 2 | 2022 | `> 待核实` | `> 待核实` [59] | arXiv 预印本 [59] | 中 [59] | ★★★★☆ | http://arxiv.org/abs/2208.02615v1 | ROS 2 安全工具链可用性讨论 [59] |
| Security and Performance Considerations in ROS 2: A Balancing Act | 2018 | `> 待核实` | `> 待核实` [8] | arXiv 预印本 [8] | 低 [8] | ★★★☆☆ | http://arxiv.org/abs/1809.09566v1 | 「安全 vs 性能」权衡的经典起点 [8] |
| ros2_control documentation | 持续更新 | ros-controls | `> 待核实` | 官方文档（第一手权威） | 高 — 依据：硬件接口与控制器管理的唯一规范来源 | ★★★★★ | https://control.ros.org/ | 本轮未实时检索验证版本页；ros2_control 章节的必备核实入口 |
| Nav2 documentation | 持续更新 | Open Navigation LLC | `> 待核实` | 官方文档（第一手权威） | 高 — 依据：导航栈与行为树的规范来源 | ★★★★★ | https://docs.nav2.org/ | 与 [63] 的 implementation-oriented 综述配合使用 |
| Nav2 for Autonomous Mobile Robots: An Implementation Oriented Survey of Architecture, Components, and Practical Limitations | `> 待核实` | `> 待核实` | `> 待核实` [63] | IJMERR（同行评审期刊）[63] | 中 [63] | ★★★★☆ | https://doi.org/10.18178/ijmerr.15.5.496-513 | 候选集中唯一的 Nav2 专述文献 [63] |

> 待核实：REP（ROS Enhancement Proposal）流程与具体提案编号在本批候选中**无任何来源**，本报告不对任何 REP 编号作断言。

### 7.2 开源项目

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| ros2/ros2 | 持续更新 | Open Robotics / ROS 2 社区 | `> 待核实`（本报告未核实 star 数） | 官方主仓库 | 高 — 依据：发行版与生态的权威源头 | ★★★★★ | https://github.com/ros2/ros2 | 核实发行版节奏与变更日志的首选入口 |
| ros-controls/ros2_control | 持续更新 | ros-controls | `> 待核实` | 官方组织仓库 | 高 | ★★★★★ | https://github.com/ros-controls/ros2_control | 与 [24] 的架构提案对照阅读 |
| ros-navigation/navigation2 | 持续更新 | Open Navigation LLC / 社区 | `> 待核实` | 官方仓库 | 高 | ★★★★★ | https://github.com/ros-navigation/navigation2 | 与 [63] 的 practical limitations 对照 |
| moveit/moveit2 | 持续更新 | MoveIt / PickNik | `> 待核实` | 官方仓库 | 中–高（本报告无候选证据支撑） | ★★★★☆ | https://github.com/moveit/moveit2 | 本报告第三章确认 MoveIt2 证据空白，此处仅为核实入口 |
| eclipse-zenoh/zenoh-plugin-ros2dds | 持续更新 | Eclipse Zenoh | `> 待核实` | 官方仓库 | 中–高 | ★★★★☆ | https://github.com/eclipse-zenoh/zenoh-plugin-ros2dds | 验证 Zenoh↔DDS 桥接边界；与 [30] 的三维框架、[22] 的 WAN 方案对照 |
| micro-ROS/micro_ros_agent | 持续更新 | micro-ROS | `> 待核实` | 官方仓库 | 中 | ★★★★☆ | https://github.com/micro-ROS/micro_ros_agent | 与 [64] 的实时 Executor 配套 |
| gazebosim/gz-sim | 持续更新 | Gazebo / Open Robotics | `> 待核实` | 官方仓库 | 中–高 | ★★★★☆ | https://github.com/gazebosim/gz-sim | 本报告第四章确认 gz-sim 无候选证据，此处仅为核实入口 |

### 7.3 数据集与基准

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| rosbag2 / MCAP | 持续更新 | MCAP 社区 / ROS 2 | `> 待核实` | 格式规范与官方站点 | 中–高 | ★★★★☆ | https://mcap.dev/ | 机器人数据记录格式；本报告第四章确认候选集中无 rosbag2/MCAP 技术来源 |
| `> 待核实`：ROS 2 专属性能基准 | — | — | — | — | — | — | — | 候选集中**未出现**任何 ROS 2 基准套件、数据集或榜单；[50] 采用「产业需求引出」式评测，[61] 采用物理一致性验证，均非通用基准 |

> 待核实：是否存在被社区广泛采用的 ROS 2 通信/实时性基准（如基于 `performance_test` 一类的工具链）与可比榜单；需以「ros2 benchmark」「DDS 评测」「executor 实时性基准」等专有词另行检索确认。

---

## 八、建议关注清单（Watchlist）

| # | 关注对象 | 类型 | 为什么关注 | 观察指标 | 证据起点 |
|---|---|---|---|---|---|
| 1 | ROS 2 发行版节奏与 distro 变更 | 生态 | 本轮**完全无一手证据**，是最大缺口，直接决定所有工程结论的版本适用性 | 官方 distro 文档与变更日志的发布时间、支持周期、REP 编号 | [50]（Jazzy 作为 2026 年研究基线的间接锚点）+ 种子仓库 https://github.com/ros2/ros2 |
| 2 | DDS QoS 组合的静态验证 | 方法论 | 20+ QoS 策略缺乏安全组合指导，是生产事故的高发区 [3] | 是否形成可复用工具/规则集，是否被官方采纳 | [3] |
| 3 | RELIABLE topic 的 backpressure 治理 | 通信工程 | 单个弱网订阅者即可拖垮全链路（含安全关键订阅者）[4] | 是否出现官方或 RMW 层原生解耦机制 | [4] |
| 4 | DDS 概率化延迟模型 | 实时性 | 把心跳/重传机制纳入延迟分布，是实时保证的形式化前提 [20] | 模型是否被实验验证、是否覆盖多 DDS 实现 | [20][23] |
| 5 | Zenoh 在 ROS 2 中的定位与量化优势 | 中间件选型 | [30] 已把 Zenoh 与 DDS 并列为核心基础设施并指出共同的结构性局限；而定量对比目前只有第三方 [18] | 官方 rmw_zenoh 基准、WAN/弱网场景数据 | [30][18][22] + 种子 https://github.com/eclipse-zenoh/zenoh-plugin-ros2dds |
| 6 | WAN / 无组播环境下的 ROS 2 组网 | 分布式部署 | DDS/RTPS 依赖组播发现，是跨地域部署的根因约束 [22][41] | 是否有稳定方案与实测吞吐/延迟 | [22][41] |
| 7 | ROS 2 on Linux 的嵌套调度 | 实时系统 | OS 调度 + 中间件 Executor 调度的双层耦合问题仍处 "Work in Progress" [65][66] | 是否形成可用的 callback 约束机制与 WCET 分析 | [65][66][64] |
| 8 | ros2_control 的参考生成解耦 | 控制 | 把参考采集/校验/插值与控制律解耦，直接改善可复用性与安全性 [24] | 是否被上游合并/成为推荐架构 | [24] + 种子 https://control.ros.org/ |
| 9 | Nav2 的「实践限制」清单 | 导航 | 官方文档通常不写失败模式，[63] 的 implementation-oriented 视角补足这一点 | 限制条目是否随版本收敛 | [63] + 种子 https://docs.nav2.org/ |
| 10 | 物理一致性安全监测 | 安全 | 网络层检测存在结构性盲区，需电机级信号校验 [61] | 是否出现可复现的检测流水线与误报率数据 | [61][59] |
| 11 | 产业需求引出式评测方法 | 评测方法学 | 以真实工程师需求为标尺，比通用 benchmark 更贴近合规判断 [50] | 是否扩展到 ROS 2 之外的中间件对比 | [50] |
| 12 | 中间件作为 Physical AI harness 层 | AI 集成 | 若成立，将重新定义 ROS 2 在 VLA/具身栈中的位置 [32]；但目前缺乏 ROS 2↔VLA 接口的一手证据 | 是否出现具体接口规范与端到端实测 | [32][71] |

---

## 参考来源

以下为本报告**实际引用**的编号及其来源（完整候选集为 [1]–[98]，未引用编号均未在正文中作为证据使用）。

1. [2] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1 （仅作检索噪声例证）
2. [3] Dependency Chain Analysis of ROS 2 DDS QoS Policies: From Lifecycle Tutorial to Static Verification — http://arxiv.org/abs/2509.03381v1
3. [4] Adaptive Bridge: A Proxy-Based Decoupling Layer for Mitigating DDS Backpressure in ROS 2 — http://arxiv.org/abs/2608.15380v2
4. [5] Exploring the Effects of Multicast Communication on DDS Performance — http://arxiv.org/abs/2209.09001v1
5. [6] Credential Masquerading and OpenSSL Spy: Exploring ROS 2 using DDS security — http://arxiv.org/abs/1904.09179v2
6. [7] A Survey on Experimental Performance Evaluation of Data Distribution Service (DDS) Implementations — http://arxiv.org/abs/2310.16630v1
7. [8] Security and Performance Considerations in ROS 2: A Balancing Act — http://arxiv.org/abs/1809.09566v1
8. [11] Bridging the Basilisk Astrodynamics Framework with ROS 2 for Modular Spacecraft Simulation and Hardware Integration — http://arxiv.org/abs/2512.09833v2
9. [18] A Performance Study on the Throughput and Latency of Zenoh, MQTT, Kafka, and DDS — http://arxiv.org/abs/2303.09419v1
10. [20] Probabilistic Latency Analysis of the Data Distribution Service in ROS 2 — http://arxiv.org/abs/2508.10413v1
11. [21] Performance Evaluation of ROS2-DDS middleware implementations facilitating Cooperative Driving in Autonomous Vehicle — http://arxiv.org/abs/2412.07485v1
12. [22] ROS2 Connect

---

*Generated by research-bot · topic=`ros2` · depth=`standard` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading · model=`deepseek-v4-flash` · sources=98 · duration=315s · 2026-10-04T22:58:29+00:00*
