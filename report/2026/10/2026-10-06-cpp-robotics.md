# C++ 机器人工程与实时系统：生态、实时实践与工程工具链调研报告

**日期**：2026-10-06（UTC） ｜ **领域**：C++ 机器人工程、实时系统、数值/优化库、构建与包管理、Python 绑定 ｜ **检索源**：本轮候选证据 97 条（编号 [1]–[97]），其中与主题**直接相关约 12 条**；另有领域主题 YAML 种子资源（论文 4 条、开源项目 8 条），种子资源按其原始链接引用、不计入编号表

> **方法学声明（重要）**：本报告严格遵守「不得基于记忆下结论」。本轮 6 个子问题的召回池**主题匹配度偏低**：q2（Ceres/GTSAM/Pinocchio 奠基论文）与 q5（求解器/实时执行基准）召回到的绝大多数条目与主题无关（详见 §五、§七 的「召回噪声」说明）。因此本报告的形式是：**少量可核查的一手/官方证据锚点 + 明确的证据缺口清单 + 观测清单**，而非对每个子问题给出面面俱到的结论。所有无法用本轮证据支撑的判断一律标注 `> 待核实`。

---

## 摘要（Executive Summary）

1. **本轮证据中真正可核查的「最新锚点」集中在三类**：(a) 官方文档类——ROS 2 控制的官方文档 `ros2_control`（Rolling 系列）[60]、Pinocchio 3.9.0 版本文档 [70]；(b) 综述类——被 ACM Digital Library 全文收录的 ROS 2 综述 [48]；(c) 预印本类前沿——多核实时系统的内存带宽+缓存分区共分配 [23]、无协调 lock-free 队列 [52]、闭链刚体动力学导数扩展 [92]、连续时间 GP 因子图估计 [81]、因子图估计/控制 [80][84]。
2. **实时确定性工程的可验证手段在本轮仅覆盖「资源侧」**：把内存带宽调节与缓存分区联合建模为 0-1 线性规划的任务-资源共分配 [23]，以及缓存着色缓解非易失缓存集合间写差异 [59]、无协调并发队列 [52]。**未见**任何关于 PREEMPT_RT 补丁、确定性内存分配器、WCET 分析工具、优先级继承/无锁闭环实测的证据 → `> 待核实`。
3. **Python 绑定维度证据最「可用」**：Inria 官方 ViSP 3.7.0 文档给出从源码构建 Python bindings 的完整依赖链（pybind11 + nlohmann_json），并含用 Python 绑定控制 Franka FR1/Panda 的专章 [66]；另有预印本声称在 Python API 中经 pybind11 封装 C++ 并行运行时「绑定开销不显著」[64]。**但**候选池内**没有** nanobind / boost.python / SWIG 的对比数据，也没有 ROS 2（rclpy/rclcpp）绑定实践的对照 [66][64] → 选型结论 `> 待核实`。
4. **构建系统与包管理、求解器性能基准两个维度，本轮召回率接近 0**：仅得到社区级痛点讨论 [73] 与厂商博客榜单 [74]（证据等级 D），以及研究软件注册库的通用最佳实践 [61]（非机器人专用）。据此**不能**给出 CMake/colcon/Bazel、Conan/vcpkg/rosdep 的任何「事实标准」结论 [73][74][61]。
5. **横向求解器对比仅有 1 条可用于机器人场景**：`g2o vs. Ceres: Optimizing Scan Matching in Cartographer SLAM`（2025 预印本），是本轮唯一把「求解器选型」落到机器人 SLAM 任务上的可引证据 [32]；其数字口径与是否同行评审 `> 待核实`。
6. **命名碰撞是本次检索的主要噪声源**：检索 "CERES" 召回到粒子物理实验 [28][29] 与矮行星际卫星世界 [31]，检索 "PINOCCHIO" 召回到天体物理晕形成工作 [91][96]，「刚体动力学」召回到相对论弹性 [93] 与欧拉角不变量 [94]。这直接解释了 q2 子问题为何拿不到奠基论文。
7. **本报告的最终形态**：§一–§六 逐节给出「可用证据 + 四轴评估 + 缺口」，§七 用表格给出经典库/开源项目/数据集基准（含种子资源链接），§八 给出 10 条 Watchlist。

---

## 一、关键前沿进展

### 1.1 可核查的最新锚点（近 1–2 年）

- **ROS 2 生态出现被 ACM 收录的系统性综述**：`ROS 2 in a Nutshell: A Survey` 在 ACM Digital Library 有全文页（DOI `10.1145/3815113`），是本轮唯一由 ACM 收录的 ROS 2 综述类来源 [48]。
- **ROS 2 控制栈有一手官方文档且处于 Rolling（开发）分支**：`ros2_control Documentation (Rolling Ridley)` 为官方 PDF 文档，可作为实时控制框架的一手规范来源 [60]。
- **Pinocchio 已迭代至 3.9.x**：ROS 文档镜像存在 `pinocchio: Rolling 3.9.0 documentation` 的 Overview 页，可佐证版本号；其 changelog、发布日期与相对 3.8 的性能变化 `> 待核实` [70]。
- **刚体动力学「解析导数」的前沿推进**：`Adapting Rigid-Body Dynamics Derivatives for Constraint Embedding Closed-Chain Models`（2026, cs.RO）将已有的一阶导数算法扩展到约束嵌入（constraint embedding）建模的闭链系统 [92]。这与 Pinocchio 一脉的「解析导数优于数值/自动微分」路线同源。
- **连续时间 + 因子图后端的持续活跃**：`Smoothing Out the Edges: Continuous-Time Estimation with Gaussian Process Motion Priors on Factor Graphs`（2026, cs.RO）指出连续时间估计的两大范式——参数化（时间基函数、样条）与非参数化（高斯过程）——并把 GP 运动先验放到因子图上 [81]。早期同类工作 `NF-iSAM`（2021）用归一化流做增量平滑与建图 [80]，`Equality Constrained Linear Optimal Control With Factor Graphs`（2020）把等式约束线性最优控制写成因子图 [84]、`Occupancy-SLAM`（2024）联合优化位姿与连续占据栅格 [51]，共同构成「因子图 = 统一优化后端」的脉络。
- **实时系统的「资源侧」新进展**：`Multi-Objective Memory Bandwidth Regulation and Cache Partitioning for Multicore Real-Time Systems`（2025, math.OC）把内存带宽调节与缓存分区联合成任务-资源共分配问题，用 0-1 线性规划求解 [23]。
- **并发数据结构新进展**：`No Cords Attached: Coordination-Free Concurrent Lock-Free Queues`（2025, cs.DC）针对 lock-free 队列中为防止 ABA/hazard 等引入的协调机制带来的复杂度问题提出新方案 [52]。
- **优化求解器套件的版本化发布仍是「基准驱动」**：`The SCIP Optimization Suite 9.0`（2024）是求解器套件随版本发布同时给出基准的典型范式，可作为「求解器新版本如何报告性能」的写法参照 [49]。
- **C++ 社区会议已把机器人列为议题方向**：CppCon 2025 官网 2025-04 页面片段包含「… C++ in a robotics or AI context … the language that powers everyday robots」[13]。仅页面片段，具体议题清单 `> 待核实` [13]。
- **C→Rust 迁移成为可实证议题**：用户研究 `Translating C To Rust: Lessons from a User Study`（2024）[33] 与工具化工作 `SACTOR`（2025，静态分析 + FFI 验证）[34]，为 §六/§八 的「C++ vs Rust」争议提供了本轮唯一的实证材料。
- **机器人前沿热点的重心在模型/数据侧，而非 C++ 实时层**：`Xiaomi-Robotics-1` 以「10 万小时以上真实世界轨迹」的训练配方为卖点 [1]；持续学习方向亦有 `Action Flow Matching for Continual Robot Learning` [2]。本条与 C++ 工程关联弱，仅用于说明证据重心分布。

### 1.2 四轴证据表（§1）

| 论断/条目 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 来源 |
|---|---|---|---|---|---|
| ROS 2 已有 ACM 收录综述 | citations/下载 `> 待核实`（候选块未给） | ACM Digital Library 全文（DOI 10.1145/3815113），同行评审出版物，刊名卷期 `> 待核实` | 中——唯一被 ACM 收录的 ROS 2 综述，但无引用/下载数字 | ★★★★☆ — 建立 ROS 2 全景最经济的一手入口 | [48] |
| `ros2_control` 官方文档（Rolling） | `> 待核实`（未给 star/下载） | 官方项目文档（维护方一手） | 中——实时控制栈的规范来源 | ★★★★☆ — 实时 C++ 控制落地必须先读官方文档 | [60] |
| Pinocchio 3.9.0 文档存在 | `> 待核实` | 官方文档镜像（docs.ros.org Rolling） | 中——可佐证版本迭代 | ★★★★☆ — 刚体动力学/解析导数首选库的版本证据 | [70] |
| 闭链动力学一阶导数扩展 | `> 待核实`（无引用数） | arXiv 预印本（cs.RO），未见同行评审 venue | 低——2026 新预印本，无社区信号 | ★★★☆☆ — 与解析导数路线直接相关，但需自行验证 | [92] |
| 连续时间 GP 因子图估计 | `> 待核实` | arXiv 预印本（cs.RO） | 低——同上 | ★★★★☆ — 因子图后端前沿叙事的核心引用 | [81] |
| 无协调 lock-free 队列 | `> 待核实` | arXiv 预印本（cs.DC） | 低——无热度信号 | ★★★☆☆ — 实时并发容器设计的候选参考 | [52] |
| 内存带宽+缓存分区共分配 | `> 待核实` | arXiv 预印本（math.OC），未见 venue | 低——无热度信号 | ★★★☆☆ — 实时确定性「资源侧」唯一强相关证据 | [23] |
| CppCon 2025 含机器人议题方向 | `> 待核实`（未给演讲数/规模） | 会议官网页面片段，非同行评审 | 低——无法判断议程强度 | ★★☆☆☆ — 弱线索，需回官方 schedule 核实 | [13] |
| C→Rust 迁移的实证/工具 | `> 待核实` | arXiv 预印本（用户研究 + 工具） | 低—中——议题热度高但候选块无量化信号 | ★★★☆☆ — 「C++ vs Rust」争议的唯一实证入口 | [33][34] |
| 求解器套件版本化 + 基准 | `> 待核实` | arXiv 预印本（优化套件技术报告） | 中——SCIP 为知名套件，但无引用数字 | ★★★☆☆ — 作「如何发布求解器基准」的范式参考 | [49] |

### 1.3 本节缺口

> 待核实：① C++23/C++26 在机器人栈中的落地（WG21 提案状态、GCC/Clang 支持矩阵、实时场景下异常/RTTI/分配器策略）；② ROS 2 近 1–2 年各发行版的实时性能改进、executor 重构与 DDS 选型对抖动的影响——本轮仅有文档入口 [60] 与综述入口 [48]，**无 release notes、无基准数字**；③ 核心求解器（QP/非线性优化/刚体动力学）在 2024–2026 的新版本与性能变化——仅有 Pinocchio 版本号侧面证据 [70]，其余 `> 待核实`。

---

## 二、数值与优化库生态对比

### 2.1 可用证据

- **求解器选型的唯一机器人域对比**：`g2o vs. Ceres: Optimizing Scan Matching in Cartographer SLAM`（2025 预印本）把 g2o 与 Ceres 放在同一 SLAM 前端任务上比较 [32]。这是本轮唯一可直接支撑「Ceres vs g2o 选型」的证据；其任务设置、硬件、指标口径与是否被会议接收 `> 待核实` [32]。
- **最小二乘的数学基础侧证据**：线性最小二乘教程 [85]、加权最小二乘估计的收敛速率（Fisher 信息无穷时的快于 √n 收敛）[87]，可作为 Ceres/Ceres-like 求解器「为什么是 WLS」的理论背景；另有一类可分非线性最小二乘专用拟合工具 [88]。
- **因子图后端生态**：`NF-iSAM`（增量平滑与建图 + 归一化流）[80]、等式约束线性最优控制的因子图表式 [84]、连续时间 GP 因子图 [81]、占据栅格与位姿联合优化 [51]——共同说明「因子图」是 SLAM/状态估计的统一表达，GTSAM 类库的设计理念在此脉络中 [80][81][84][51]。
- **刚体动力学的解析导数路线**：闭链约束嵌入模型的一阶导数扩展 [92] 与种子资源 Pinocchio 论文（arXiv 1906.09139，2019，LAAS-CNRS）同属「解析导数优于数值差分/AD 的性能取舍」议题。

### 2.2 生态对比表（本轮可核查范围内）

| 库 | 定位（按证据） | 关键证据 | 热度 | 权威 | 关注度 | 推荐度 | 链接 |
|---|---|---|---|---|---|---|---|
| Ceres Solver | 非线性最小二乘（标定/BA/IK 常用） | 与 g2o 在 Cartographer 扫描匹配上的对比研究 [32] | `> 待核实`（未给 star/引用） | 种子资源指向 Google 官方站点；对比证据为 arXiv 预印本 [32] | 中——存在独立第三方对比研究即是采用度信号 [32] | ★★★★☆ — 有机器人域横向对比可依 | ceres-solver.org；github.com/ceres-solver/ceres-solver |
| g2o | 图优化（作为对照求解器） | 同上对比研究 [32] | `> 待核实` | 同上 | 中——同上 | ★★★☆☆ — 对比结论依赖该单篇证据 | 见 [32] |
| GTSAM | 因子图/增量式 SLAM 与状态估计 | 因子图后端脉络 [80][81][84][51]；种子资源指向 gtsam.org / borglab/gtsam | `> 待核实` | 官方站点 + 社区仓库（种子）；本轮无同行评审论文直接对应 | 中——因子图范式在 2020–2026 持续有论文产出 [80][81][84][51] | ★★★★☆ — 状态估计/SLAM 主线库 | gtsam.org；github.com/borglab/gtsam |
| Pinocchio | 刚体动力学/运动学 + 解析导数 | 3.9.0 官方文档 [70]；闭链导数扩展预印本 [92]；种子论文 arXiv 1906.09139 | `> 待核实` | 官方文档（docs.ros.org 镜像）[70] + LAAS-CNRS 论文（种子） | 中——有 2026 新预印本延续其导数主线 [92] | ★★★★★ — 若目标是解析导数与控制，本轮相关性最高 | github.com/stack-of-tasks/pinocchio |
| Sophus | SO(3)/SE(3) 李群运算 | **本轮无任何编号证据**；仅种子资源 github.com/strasdat/Sophus | `> 待核实` | 种子仓库（未编号，未在本次证据表内） | `> 待核实` | ★★★★☆（工程直觉，非证据结论）— 李群接口在 SLAM/控制中普遍需要，但须自行核实其维护状态 | github.com/strasdat/Sophus |
| Eigen | 线性代数基础库 | **本轮无任何编号证据**；仅种子资源 | `> 待核实` | 官方仓库（种子） | `> 待核实` | ★★★★☆（工程直觉）— 上述库的公共数学底座，但本轮无可引证据 | gitlab.com/libeigen/eigen |
| SCIP | 约束整数规划/优化套件 | 9.0 版本技术报告（含基准）[49] | `> 待核实` | arXiv 技术报告（套件官方作者群） | 中——知名套件版本发布，但无引用数字 | ★★★☆☆ — 作为「求解器版本+基准」范式参考 | 见 [49] |

> **重要警示（命名碰撞）**：检索 "CERES" 在本轮召回到粒子物理实验（`Dilepton measurements with CERES` [28]、`The CERES/NA45 Radial Drift TPC` [29]）与矮行星际卫星世界 [31]；检索 "PINOCCHIO" 召回到天体物理晕形成系列 [91][96]；「刚体」相关查询召回到相对论弹性 [93] 与欧拉角不变量 [94]。**这意味着任何以裸词 `CERES`/`PINOCCHIO` 做的检索都会严重污染结果**，必须加限定词（如 `Ceres Solver least squares C++`、`pinocchio rigid body dynamics library`）。

### 2.3 本节缺口

> 待核实：Ceres/GTSAM/Pinocchio/Sophus 的**奠基性论文原文**在本轮编号证据中缺失（q2 召回被噪声占满）；解析导数 vs 自动微分的**定量对比**（精度、内存、编译期开销）无任何可引证据；Ceres 与 g2o 之外的其他后端（如基于 AD 的框架）无对比 [32]。

---

## 三、实时 C++ 与确定性工程

### 3.1 可核查的最佳实践线索

- **资源侧确定性（多核）**：把「内存带宽调节」与「缓存分区」视为联合资源，与任务一起分配到核心上，用 0-1 线性规划求解；论文动机明确指出二者组合后任务执行时间强依赖所分配资源 [23]。**这是本轮与「硬实时确定性执行」最直接相关的一手证据。**
- **缓存侧干扰抑制**：缓存着色（cache coloring）用于缓解非易失缓存中的集合间写差异 [59]（2013，较早，证据强度偏低，仅作技术脉络）。
- **并发容器**：lock-free 队列的问题在于为防 hazard 而引入的协调机制使实现远超「FIFO 容器」的复杂度 [52]；对「感知-控制数据通路中的无锁环形缓冲」类设计有直接参考价值。
- **时限约束的形式化**：车辆边缘计算中把问题定义为 Deadline-Constrained Task Offloading and Resource Allocation Problem (DOAP)，在带宽与算力双约束下最大化总效用（提出 SARound）[5]。**注意**：该工作对象是车联网卸载策略，**不是**机器人本体实时栈 [5]，仅可作「截止期约束建模」的远距离类比。
- **非 C++ 实时栈的现实存在**：基于 LabVIEW 的电机实时状态监测与故障诊断系统（2018）[6]，说明工业实时监测长期存在图形化/专用栈路线，C++ 并非唯一选择（该条年代较早，仅作生态对照）[6]。
- **嵌入式大趋势的厂商视角**：厂商博客把嵌入式开发趋势归纳为若干方向 [72]（证据等级 D，仅作线索，需一手标准/文档复核）。

### 3.2 四轴证据表（§3）

| 论断 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 来源 |
|---|---|---|---|---|---|
| 内存带宽+缓存分区应联合共分配（0-1 LP） | `> 待核实` | arXiv 预印本（math.OC），无 venue | 低——无引用/复现信号 | ★★★☆☆ — 实时确定性资源分配的关键线索，但缺真机/基准数据 | [23] |
| 缓存着色缓解集合间写差异 | `> 待核实` | arXiv 预印本（2013），年代久 | 低——无热度信号 | ★★☆☆☆ — 仅作技术脉络 | [59] |
| 无协调 lock-free 队列可降低队列实现复杂度 | `> 待核实` | arXiv 预印本（cs.DC） | 低——无热度信号 | ★★★☆☆ — 无锁数据结构选型参考 | [52] |
| 截止期约束在分布式场景被形式化为 DOAP | `> 待核实` | arXiv 预印本（cs.DC） | 低——非机器人域 | ★★☆☆☆ — 仅作建模类比 | [5] |
| 工业实时监测存在 LabVIEW 等非 C++ 路线 | `> 待核实` | arXiv 预印本（2018） | 低——年代早、无热度信号 | ★★☆☆☆ — 生态对照用 | [6] |
| 嵌入式趋势（厂商视角） | `> 待核实` | 厂商博客（证据 D） | 低——商业内容 | ★★☆☆☆ — 仅线索 | [72] |

### 3.3 本节缺口（明确写「无证据」）

> 待核实：① PREEMPT_RT 与实时内核配置在机器人栈中的实测数据；② 确定性内存（预分配、内存池、无锁分配器、`malloc` 抖动抑制）的定量效果；③ 优先级继承/优先级天花板、executor 调度对端到端时延分布的影响——本轮仅找到官方文档入口 [60]，**无任何测量数据**；④ WCET 分析工具与实时 C++ 代码规范的可核查材料为零 [23][52][59]。

---

## 四、构建系统与包管理

### 4.1 可用证据（强度普遍偏低）

- **社区痛点被明确表述**：博客/讨论帖《Why C++ project setup is still painful in 2025 (and my attempt to fix it)》[73]——证据等级 D，仅说明「工程搭建仍痛」这一社区共识倾向，**不能**作为采用度数据。
- **研究软件注册库/仓库的通用最佳实践**：`Nine Best Practices for Research Software Registries and Repositories`（2020）[61]——对「如何组织可复现的软件发布与依赖元数据」有方法论意义，但**不是** C++ 包管理（Conan/vcpkg/rosdep）的对比证据。
- **厂商榜单类内容**：`Top 10 C++ libraries for your next project` 属厂商博客营销内容 [74]，**不得**作为事实标准依据（证据 D）；同类还有个人学习路线文章 [75]（与主题无关，仅示召回噪声）。
- **教育/最佳实践会议论文集**：ACM COMPUTE 2025 Best Practices Track Proceedings [8]——与 C++ 机器人工程无直接关系，仅说明「最佳实践」类议题有独立社区。
- **构建工具链的唯一强相关「官方」入口**：`ros2_control` Rolling 官方文档 [60]——ROS 2 生态的实际构建/依赖组织方式应从该类官方文档与仓库读起（CMake/ament/colcon 的具体配置需查仓库，`> 待核实`）。

### 4.2 四轴证据表（§4）

| 论断 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 来源 |
|---|---|---|---|---|---|
| C++ 项目搭建在 2025 仍被视为痛点 | `> 待核实`（无 upvote/评论数据） | Reddit 个人博客帖，证据 D | 低—中——社区讨论存在但无量化信号 | ★★☆☆☆ — 仅可作「问题存在」的线索 | [73] |
| 研究软件注册/仓库有可循最佳实践 | `> 待核实` | arXiv 预印本（2020） | 低 | ★★★☆☆ — 元数据/可复现性规范可迁移 | [61] |
| 存在「十大 C++ 库」类榜单内容 | `> 待核实` | 厂商博客（证据 D，营销导向） | 低 | ★☆☆☆☆ — 不可作为标准依据 | [74] |
| ROS 2 控制栈有官方构建/使用文档 | `> 待核实` | 官方项目文档 [60] | 中 | ★★★★☆ — 构建事实的唯一官方入口 | [60] |

### 4.3 本节缺口（q3 明确判定）

> 待核实：① 构建系统维度**零证据**——CMake / colcon / ament_cmake / Bazel 在机器人 C++ 项目中的使用现状与对比完全缺失；② 包管理维度**零证据**——Conan / vcpkg / rosdep / apt-ros 的采用度与冲突处理无任何数据（种子资源列出的 vcpkg [microsoft/vcpkg] 与 conan [conan-io/conan] 仅提供链接）；③ 静态分析/代码质量维度**零证据**——clang-tidy / clang-format / cppcheck / pre-commit / CI 流水线实践在本轮候选中完全未出现。

---

## 五、性能剖析与基准

### 5.1 本轮可用证据

- **SLAM 轨迹评估的口径问题有专门工作**：`Rethinking Trajectory Evaluation for SLAM: a Probabilistic, Continuous-Time Approach`（2019）针对轨迹评估提出概率化、连续时间的方法——即「ATE/RPE 类离散对齐指标」本身存在可比性争议 [44]。这为「基准口径必须写清对齐方式、时间同步、采样率」提供了一手依据。
- **SLAM 系统基准的另一类口径**：`Occupancy-SLAM` 同时优化位姿与连续占据图 [51]、`HS-SLAM` 以混合表征做稠密 SLAM [30]——说明 SLAM 评测常以重建/定位精度为主指标。
- **机器人域确实存在挑战赛式组织**：`Technical Report for ICRA 2025 GOOSE 3D Semantic Segmentation Challenge` 面向异构机器人系统的自适应点云理解 [26]——是本轮候选池中**唯一**明确以机器人任务为对象的挑战赛技术报告，可作为「机器人基准如何组织（统一数据 + 排行榜 + 总结报告）」的实例 [26]。
- **求解器/库的横向对比只有 1 条**：[32]（见 §二）。
- **绑定开销的基准主张**：单一预印本片段称在 Python API 中经 pybind11 使用 HPX「无显著绑定开销」[64]——**无具体数字、无硬件口径、被测对象为通用并行运行时而非机器人栈** [64]。
- **绑定层质量的实证研究**：ACM 收录的 `Studying the Impact of TensorFlow and PyTorch Bindings on …`（标题在候选列表中被截断）研究 TF/PyTorch 绑定的影响 [67]；研究方向有参考价值，但研究问题与结论 `> 待核实` [67]。
- **SLAM/机器人系统评测工具的可用性缺口**：本轮**未**召回任何「机器人 C++ 求解器/优化库/实时执行性能」专用基准（q5 召回率为 0），仅召回视觉与编程检索类基准 [21][24][41][46][47][42]，以及医学影像数据集 [40][43]——证明本轮检索严重偏离主题。

### 5.2 四轴证据表（§5）

| 论断 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 来源 |
|---|---|---|---|---|---|
| SLAM 轨迹评估需要概率化/连续时间口径 | `> 待核实` | arXiv 预印本（2019），被广泛视为该问题经典讨论 | 中——长期被轨迹评估实践引用（引用数 `> 待核实`） | ★★★★☆ — 写基准口径时必须引用 | [44] |
| 机器人域存在挑战赛式基准组织（ICRA 2025 GOOSE） | `> 待核实` | ICRA 2025 挑战赛技术报告（arXiv 预印本） | 中——ICRA 关联，社区可见度高 | ★★★★☆ — 机器人基准组织方式的可用范例 | [26] |
| 求解器选型有机器人域横向对比（1 篇） | `> 待核实` | arXiv 预印本 | 低 | ★★★☆☆ — 唯一可用，需核实其口径 | [32] |
| pybind11 绑定开销「不显著」 | `> 待核实`（无数字） | arXiv 预印本（cs.LG），非机器人栈 | 低 | ★★☆☆☆ — 不可作为工程结论 | [64] |
| TF/PyTorch 绑定影响的实证研究存在 | `> 待核实` | ACM DL（DOI 10.1145/3678168），同行评审 | 中——ACM 收录 | ★★★☆☆ — 绑定层质量研究的方法参考 | [67] |
| 本轮不存在机器人 C++ 求解器/实时执行基准 | — | 判定基于候选池主题分布 [21][24][41][46][47][42][40][43] | 低 | ★☆☆☆☆ — 记为缺口 | [21][24][41][46][47][42][40][43] |

### 5.3 本节缺口（q5 结论）

> 待核实：① 机器人 C++ 生态中评估求解器（运动学/动力学/轨迹优化）与优化库（非线性优化、QP）**功能正确性与数值精度**的公开基准：本轮零召回；② 实时执行性能口径（WCET、周期抖动、调度可预测性、端到端时延分布）：本轮零召回；③ 跨库可比性前提（统一问题集、规模标注、硬件/编译选项/线程数透明、结果可复现）：本轮零召回；④ 「功能/数值正确性基准」与「性能/实时性基准」的评价权重：无证据可判断。

---

## 六、C++ 与 Python 协作（绑定 / 部署）

### 6.1 可核查证据

- **官方绑定教程（最强证据）**：Inria 的 ViSP 3.7.0 文档给出「从源码构建 Python bindings」教程，显式列出 pybind11 与 nlohmann_json 依赖，并含「使用 Panda 机器人 + Python bindings」与 Franka Research (FR1) 的专门说明 [66]。可见绑定构建是官方安装流程的一等公民，而非附加项 [66]。
- **绑定开销主张**：预印本片段称在 Python API 中经 pybind11 封装 C++ 并行运行时

## 七、经典参考资料与工程规范

> 本章的“经典/奠基”条目来自**题面提供的种子资源**（Sophus / Ceres / GTSAM / Pinocchio / Eigen / vcpkg / conan / nanobind 等），它们在本轮可引用来源清单 [1]–[97] 中**没有对应编号**，因此其热度、权威、关注度一律标 `> 待核实`，仅保留题面给定的链接与说明；凡能锚定到本轮来源编号的条目，均按要求补齐四轴证据。

### 7.1 经典与奠基性工作

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Sophus（李群运算库文档） | ongoing | strasdat | `> 待核实`（种子资源，本轮来源无编号） | `> 待核实`；种子资源标注为库文档，非同行评审 | `> 待核实` | ★★★★☆ + SO(3)/SE(3) 李群运算是机器人状态估计与几何优化的最低层公共依赖，属必读基础 | https://github.com/strasdat/Sophus | SO(3)/SE(3) 李群运算 |
| Ceres Solver（非线性最小二乘文档） | ongoing | Google | `> 待核实`（种子资源，本轮来源无编号） | `> 待核实`；种子资源标注为官方文档 | `> 待核实` | ★★★★★ + 标定、BA、IK 的事实级工具，机器人 C++ 栈不可绕过 | http://ceres-solver.org/ | 标定、BA、IK 常用 |
| GTSAM（因子图优化） | ongoing | Georgia Tech | `> 待核实`（种子资源，本轮来源无编号） | `> 待核实`；种子资源标注为官方站点 | `> 待核实` | ★★★★★ + SLAM/状态估计主线的因子图范式承载者 | https://gtsam.org/ | SLAM / 状态估计 |
| Pinocchio（刚体动力学解析导数） | 2019 | LAAS-CNRS | `> 待核实`（种子资源，本轮来源无编号） | `> 待核实`；种子资源未标注 venue | `> 待核实` | ★★★★★ + 高效刚体算法与解析导数的奠基工作，是“解析导数 vs 自动微分”争论的核心参照 | https://arxiv.org/abs/1906.09139 | 高效刚体算法与解析导数 |
| 因子图约束线性最优控制 | 2020 | 候选块未给出机构 | `> 待核实`：候选块未提供引用数 [84] | arXiv 预印本 [84]，候选块未标注同行评审 venue | 低 + 依据：候选块无引用/star/榜单信号 [84] | ★★★☆☆ + 展示因子图求解器可承载最优控制问题，是 GTSAM/Ceres 边界讨论的方法学补充 [84] | http://arxiv.org/abs/2011.01360v2 | Equality Constrained Linear Optimal Control With Factor Graphs |
| 连续时间 SLAM 轨迹评估的概率方法 | 2019 | 候选块未给出机构 | `> 待核实`：候选块未提供引用数 [44] | arXiv 预印本 [44]，未标注 venue | 低 + 依据：候选块无热度数字 [44] | ★★★☆☆ + 为“如何公平评估连续时间估计器”提供口径参考，与 GP 先验等新工作构成前后脉络 [44][81] | http://arxiv.org/abs/1906.03996v1 | Rethinking Trajectory Evaluation for SLAM: a Probabilistic, Continuous-Time Approach |
| 连续时间估计（GP 运动先验 + 因子图） | 2026 | 候选块未给出机构 | `> 待核实`：候选块未提供引用数 [81] | arXiv 预印本（cs.RO）[81]，未标注 venue | 中 + 依据：候选块明确其属连续时间估计主线，且摘要被完整摘录、主题与因子图生态直接相关 [81] | ★★★★☆ + 是“GP 非参数 vs 样条参数化”两条连续时间范式的当代综述式入口，适合作为经典脉络的延伸阅读 [81] | http://arxiv.org/abs/2605.09073v1 | Smoothing Out the Edges: Continuous-Time Estimation with Gaussian Process Motion Priors on Factor Graphs |
| 刚体动力学解析导数的闭链扩展 | 2026 | 候选块未给出机构 | `> 待核实`：候选块未提供引用数 [92] | arXiv 预印本（cs.RO）[92]，未标注 venue | 中 + 依据：直接承接“刚体动力学导数”这一经典算法线并扩展到约束嵌入闭链模型 [92] | ★★★★☆ + 与 Pinocchio 的解析导数路线同源，是判断“解析导数是否仍是主流”的关键新证据 [92] | http://arxiv.org/abs/2609.21024v1 | Adapting Rigid-Body Dynamics Derivatives for Constraint Embedding Closed-Chain Models |

### 7.2 开源项目与工程规范

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Eigen（线性代数基础库） | ongoing | eigenteam | `> 待核实`（种子资源，本轮来源无编号） | `> 待核实` | `> 待核实` | ★★★★★ + 机器人 C++ 生态的公共分母，几乎所有下游库的模板基座 | https://gitlab.com/libeigen/eigen | 线性代数基础库 |
| stack-of-tasks/pinocchio | ongoing | LAAS-CNRS / stack-of-tasks | `> 待核实`（种子资源，本轮来源无编号） | `> 待核实` | 中 + 依据：其 Rolling 3.9.0 文档已进入 ROS 官方文档站点，说明已纳入 ROS 发行分发链 [70] | ★★★★★ + 刚体动力学/运动学主力实现，且具备官方文档与 ROS 打包路径 [70] | https://github.com/stack-of-tasks/pinocchio | 刚体动力学/运动学 |
| ceres-solver/ceres-solver | ongoing | Google | `> 待核实`（种子资源，本轮来源无编号） | `> 待核实` | 中 + 依据：第三方研究以 Ceres 作为 Cartographer SLAM 中与 g2o 对比的对象，构成实际选型证据 [32] | ★★★★★ + 非线性优化默认选项，且有独立第三方对比研究可用 [32] | https://github.com/ceres-solver/ceres-solver | 非线性优化 |
| borglab/gtsam | ongoing | Georgia Tech (borglab) | `> 待核实`（种子资源，本轮来源无编号） | `> 待核实` | 中 + 依据：因子图思路被复用到最优控制与连续时间估计等相邻问题 [84][81] | ★★★★★ + 因子图/SLAM 主线实现 | https://github.com/borglab/gtsam | 因子图优化 |
| pybind/pybind11 | ongoing | pybind | `> 待核实`：候选块未提供 star/下载量 [66][64] | Inria 官方 ViSP 文档将其列为绑定构建依赖（维护方一手文档）；另有 arXiv 预印本独立采用 [66][64] | 中 + 依据：两个相互独立工程来源重复出现，但无量化热度数字 [66][64] | ★★★★☆ + 本批证据中“Python 绑定事实标准”的最强信号，但缺备选方案对比 [66][64][68] | https://github.com/pybind/pybind11 | C++/Python 绑定 |
| nanobind/nanobind | ongoing | wjakob | `> 待核实`（种子资源；本轮来源未覆盖，候选块中未出现该方案） | `> 待核实` | `> 待核实` | ★★★☆☆ + 作为 pybind11 的轻量替代应纳入选型矩阵，但本轮**无任何证据**支撑其采用度 [68] | https://github.com/wjakob/nanobind | 更轻量的绑定方案 |
| microsoft/vcpkg | ongoing | Microsoft | `> 待核实`（种子资源；本轮来源未覆盖） | `> 待核实` | 低 + 依据：仅在社区层面出现“C++ 项目搭建依然痛苦”的抱怨，未指向具体包管理器采用度 [73] | ★★★☆☆ + 包管理维度证据缺口未闭合，暂作候选而非结论 [73] | https://github.com/microsoft/vcpkg | C++ 包管理 |
| conan-io/conan | ongoing | Conan | `> 待核实`（种子资源；本轮来源未覆盖） | `> 待核实` | 低 + 依据：同上，仅有“项目搭建痛感”的社群信号 [73] | ★★★☆☆ + 与 vcpkg 并列的候选方案，需补充采用度证据 | https://github.com/conan-io/conan | C++ 包管理 |
| ros2_control（Rolling Ridley 文档） | ongoing | ROS 2 社区（Rolling） | `> 待核实`：候选块未提供 star/下载量 [60] | 官方发布文档（PDF），属维护方一手材料 [60] | 中 + 依据：作为 ROS 2 实时控制的标准接入层，是机器人实时 C++ 工程的核心规范文档 [60] | ★★★★★ + 回答“实时控制环路如何标准化接入”的第一手规范 [60] | https://control.ros.org/rolling/downloads/ros2_control_rolling.pdf | ROS 2 控制器管理框架官方文档 |
| CXXStateTree（现代 C++ 层次状态机库） | 候选块未给出年份 | 候选块未给出作者 | `> 待核实`：仅有 Hacker News 讨论帖，无 star [71] | 无同行评审；Hacker News 帖子属社区来源（证据等级 D）[71] | 中 + 依据：登上 Hacker News 说明存在社区讨论热度，但候选块未给出评论数/点赞数 [71] | ★★☆☆☆ + 可作行为编排库选型线索，须另找官方仓库核实 [71] | https://news.ycombinator.com/item?id=44487221 | 现代 C++ 层次状态机库 |
| 机器人行为树的质量需求扩展 | 2025 | 候选块未给出机构 | `> 待核实`：候选块未提供引用数 [62] | arXiv 预印本 [62]，未标注 venue | 低 + 依据：候选块无热度数字 [62] | ★★★☆☆ + 把非功能（质量）需求写进行为树，是“功能编排”与“实时约束”衔接的少见尝试 [62] | http://arxiv.org/abs/2503.16969v1 | Extending Behavior Trees for Robotic Missions with Quality Requirements |

### 7.3 工程规范与协作惯例

- 科研软件仓库的发布与登记存在成文的最佳实践指南（九条），可迁移到机器人 C++ 库的发布治理（版本、元数据、长期归档）[61]。热度：`> 待核实`（候选块未提供引用数）[61]；权威：arXiv 预印本 [61]，未标注 venue；关注度：低 + 依据：候选块无量化热度信号 [61]；推荐度：★★★☆☆ + 可作为“库/数据集如何被长期可复现地登记”的规范参考 [61]。
- ROS 2 已有系统级综述性文献可供引用为生态基线 [48]。热度：`> 待核实`（候选块未提供引用数）[48]；权威：ACM Digital Library 收录（同行评审出版物页面）[48]；关注度：中 + 依据：被 ACM DL 收录且以 survey 形式覆盖 ROS 2 整体，是生态级入门引用 [48]；推荐度：★★★★☆ + 用于替代“凭记忆描述 ROS 2”的写法 [48]。
- **必须同时用于规范引用的版本级证据**：pinocchio 在 ROS 滚动发行中已有 3.9.0 版本文档 [70]，ros2_control 已有 Rolling 发行版官方手册 [60]。
  > 待核实：两份文档的具体版本发布日期、相对上一版本的变更摘要（changelog）与实时性能改进项，候选块仅给出文档链接标题，未提供正文内容 [60][70]。

### 7.4 命名歧义与证据卫生（本轮检索的一手教训）

- 检索 “Ceres” 会大量召回**粒子物理实验探测器**相关论文（如 CERES 双轻子测量、CERES/NA45 漂移时间投影室）[28][29]、以及**矮行星 Ceres 的地球化/巨型卫星世界**设想 [31]，与 Google Ceres Solver 完全无关。热度：均 `> 待核实`（候选块未提供引用数）[28][29][31]；权威：均为 arXiv 预印本，前者属核物理/天体物理方向 [28][29][31]；关注度：低 + 依据：与机器人 C++ 主题无交集 [28][29][31]；推荐度：★☆☆☆☆ + **不建议引用**，仅作为检索式必须加限定词（如 `site:ceres-solver.org`）的反面证据。
- 同理，检索 “Pinocchio” 会召回宇宙学线性密度场中的**星系形成算法**（PINOCCHIO）[91][96]，与 LAAS-CNRS 的刚体动力学库同名不同物。四轴：热度 `> 待核实` [91][96]；权威：arXiv 预印本，天体物理方向 [91][96]；关注度：低 + 依据：主题不相关 [91][96]；推荐度：★☆☆☆☆ + 不建议引用。
- 本轮来源中还出现了一条 **withdrawn（已撤稿）** 的 arXiv 记录 [77]，说明在建立参考清单时必须核对“是否撤稿/是否被替换版本”，而不能仅凭标题入库。四轴：热度 `> 待核实` [77]；权威：已撤回记录，不可作为证据 [77]；关注度：低 + 依据：内容不可用 [77]；推荐度：★☆☆☆☆ + 仅作为引用卫生的警示样本（证据等级 E，应丢弃）。
- 结论：**“Ceres/Pinocchio/Sophus”这类短名库必须使用限定检索（官方域名、`site:github.com`、附加 “robotics / solver / Lie group”）**，否则召回污染会直接导致综述出现张冠李戴 [28][29][31][91][96]。

---

## 八、建议关注清单（Watchlist）

以下按“与本主题相关性 × 证据可核查度”排序。所有条目均标注四轴证据；证据不足者明确写 `> 待核实`。

### W1（高优先）多核实时系统的资源共分配
- **point**：把内存带宽调节与缓存分区联合建模为 0-1 线性规划的任务–资源共分配问题，是当前“实时执行时间可预测性”方向最直接的方法线索 [23]。
- **热度证据**：`> 待核实` —— 候选块未提供引用数、star 或下载量 [23]。
- **权威证据**：arXiv 预印本（math.OC），候选块未标注同行评审 venue [23]。
- **关注度**：低 + 依据：候选块无任何引用/榜单/讨论热度信号，且属数学优化与实时系统交叉的小众方向 [23]。
- **推荐度**：★★★☆☆ + 与“确定性执行”强相关，但仅为单篇预印本，需等待第三方复现或真机验证后再作为结论 [23]。
- **跟踪动作**：关注该文后续是否被 RTSS/ECRTS 类实时系统会议收录，并核查是否发布代码与真机/仿真基准数据 [23]。

### W2（高优先）无协调并发无锁队列
- **point**：现有无锁队列实现为防危险（hazard）引入了协调机制，导致实现复杂度上升；“协调无关（coordination-free）”的并发无锁队列尝试去掉这类协调 [52]。
- **热度证据**：`> 待核实` —— 候选块未提供引用数 [52]。
- **权威证据**：arXiv 预印本（cs.DC），候选块未标注 venue [52]。
- **关注度**：中 + 依据：摘要明确指出“队列是最简单数据结构却因并发正确性而显著复杂化”这一普遍痛点，属并发工程的高关注话题 [52]。
- **推荐度**：★★★★☆ + 直接对应机器人实时线程间通信（传感器→估计→控制）的数据结构选择，是最值得盯的技术点之一 [52]。
- **跟踪动作**：核实是否开源、是否给出与既有无锁队列在争用/尾延迟上的对比数据。[52]

### W3（中优先）缓存着色与内存侧干扰抑制
- **point**：缓存着色（cache coloring）可用于缓解非易失性缓存中的组间写变异（inter-set write variation）问题 [59]。
- **热度证据**：`> 待核实` —— 候选块未提供引用数 [59]。
- **权威证据**：arXiv 预印本 [59]，候选块未标注 venue；年份为 2013，属**经典而非前沿** [59]。
- **关注度**：低 + 依据：无热度数字，且属体系结构侧旧文 [59]。
- **推荐度**：★★★☆☆ + 作为 W1 的前置背景阅读（缓存分区/着色的既有手段），与实时确定性主题构成承上启下关系 [59][23]。

### W4（高优先）ROS 2 实时执行与控制器框架
- **point**：ROS 2 已有系统级综述 [48]；`ros2_control` 在 Rolling 发行版下提供官方控制器管理框架文档 [60]。
- **热度证据**：`> 待核实` —— 候选块未提供引用数或 star [48][60]。
- **权威证据**：ACM Digital Library 收录的 survey [48]；ROS 2 官方发布文档 PDF [60]。
- **关注度**：高 + 依据：ROS 2 是机器人 C++ 工程的事实平台，其官方文档与综述是被反复引用的基线材料 [48][60]。
- **推荐度**：★★★★★ + 任何关于“实时 C++ 机器人系统”的结论都必须先对齐 ROS 2 的执行器/控制器规范 [48][60]。
- **待核实**：执行器（executor）重构、DDS 中间件选择对抖动/延迟的影响，本轮**完全无证据**。[48][60]

### W5（中优先）解析导数路线在闭链模型上的延伸
- **point**：已有的刚体动力学一阶导数算法被扩展到使用**约束嵌入（constraint embedding）**建模的闭链运动学系统 [92]。
- **热度证据**：`> 待核实` —— 候选块未提供引用数 [92]。
- **权威证据**：arXiv 预印本（cs.RO），未标注 venue [92]。
- **关注度**：中 + 依据：直连 Pinocchio 式解析导数主线，对腿足/闭链机构工程有实际意义 [92]。
- **推荐度**：★★★★☆ + 是“解析导数 vs 自动微分”争议中解析侧的最新一手支撑点 [92]。

### W6（高优先）Python 绑定方案与绑定开销
- **point**：本批证据中 pybind11 被两个相互独立的工程来源采用（Inria 官方 ViSP 文档、arXiv 预印本）[66][64]；并有一处“绑定开销不显著”的基准主张 [64]。
- **热度证据**：`> 待核实` —— 候选块未提供 star、下载量或引用数 [66][64]。
- **权威证据**：Inria 官方 Doxygen 文档（维护方一手）[66]；arXiv 预印本（cs.LG）[64]；另有 ACM 收录的 TensorFlow/PyTorch 绑定影响研究页 [67]。
- **关注度**：高 + 依据：绑定是从 Python 侧使用机器人 C++ 库的必经环节，官方文档与独立预印本同时指向该方案 [66][64][67]。
- **推荐度**：★★★★☆ + 应作为选型基线，但**必须补做** boost.python/SWIG/nanobind 对比，并补 rclpy/rclcpp 侧证据 [64][66][67][68]。
- **待核实**：绑定开销结论的具体基准数字、任务与硬件口径；被测对象为通用并行运行时 HPX 而非机器人栈 [64]。

### W7（中优先）C++ 项目搭建与依赖管理痛点
- **point**：社区层面存在“2025 年 C++ 项目搭建依然痛苦”的直接抱怨，以及嵌入式开发趋势中对工具链的持续讨论 [73][72]。
- **热度证据**：`> 待核实` —— 候选块未提供帖子互动量、博客阅读量 [73][72]。
- **权威证据**：Reddit 帖子与厂商博客，均为**非同行评审、非官方标准**来源（证据等级 D）[73][72]。
- **关注度**：中 + 依据：话题在 C++ 社区持续复现，但当前只有低等级来源 [73][72]。
- **推荐度**：★★☆☆☆ + 只可作问题意识的佐证，不可用作“事实标准”的论断依据 [73][72]。
- **配套**：CppCon 2025 已把“机器人与 AI 语境下的 C++”列入议程方向，可作为生态活跃度的弱信号 [13]。
  > 待核实：具体议题清单与演讲内容。[13]

### W8（中优先）C++ → Rust 的迁移与互操作
- **point**：存在关于 C→Rust 翻译的用户研究 [33]，以及结合静态分析与 FFI 校验的 LLM 驱动 C→Rust 翻译工作 [34]。
- **热度证据**：`> 待核实` —— 候选块未提供引用数 [33][34]。
- **权威证据**：均为 arXiv 预印本，未标注 venue [33][34]。
- **关注度**：中 + 依据：C/C++ 与 Rust 的取舍是当下系统编程讨论热点，但候选块无量化热度 [33][34]。
- **推荐度**：★★★☆☆ + 为“C++ vs Rust 在机器人中如何取舍”提供经验研究视角，但需补充机器人领域专门证据 [33][34]。

### W9（中优先）图优化求解器选型（g2o vs Ceres）
- **point**：已有第三方研究以 Cartographer SLAM 的扫描匹配为场景，比较 g2o 与 Ceres 的优化表现 [32]。
- **热度证据**：`> 待核实` —— 候选块未提供引用数 [32]。
- **权威证据**：arXiv 预印本 [32]，未标注 venue。
- **关注度**：中 + 依据：直接回答工程界高频选型问题（哪一个更合适），具实用价值 [32]。
- **推荐度**：★★★★☆ + 是“GTSAM vs Ceres / g2o”争议中难得的可引用对比研究，建议精读其评测口径（任务、硬件、收敛判据）[32]。

### W10（中优先）连续时间与增量式估计
- **point**：连续时间估计在平滑解、异步传感器处理与数据插值上的优势被系统化讨论，参数化（样条/时基函数）与非参数化（高斯过程）两大范式并列 [81]；增量平滑方向亦有归一化流方案 [80]。
- **热度证据**：`> 待核实` —— 候选块未提供引用数 [81][80]。
- **权威证据**：均为 arXiv 预印本（[81] cs.RO）[81][80]。
- **关注度**：中 + 依据：与因子图/SLAM 主线直接相邻，属持续性研究议题 [81][80]。
- **推荐度**：★★★★☆ + 对“状态估计是选 Ceres 还是 GTSAM、用离散还是连续时间”的选型有直接帮助 [81][80][44]。

### W11（低优先）实时约束向分布式/边缘延伸
- **point**：车载边缘计算把截止期约束形式化为带宽与算力双约束下的任务卸载与资源分配问题（DOAP，SARound 求解）[5]。
- **热度证据**：`> 待核实` —— 候选块未提供引用数 [5]。
- **权威证据**：arXiv 预印本（cs.DC），未标注 venue [5]。
- **关注度**：低 + 依据：场景为车联网，与机器人本体实时栈无直接交集 [5]。
- **推荐度**：★★☆☆☆ + 仅在需要跨节点实时调度建模时参考 [5]。

### W12 需要新增检索才能回答的问题（本轮证据缺口，全部标 `> 待核实`）
1. **C++ 标准落地**：C++23/C++26 特性（模块、`std::expected`、分配器与异常/RTTI 策略）在机器人栈中的实际采用与编译器支持矩阵。[13]
2. **实时内核与执行环境**：PREEMPT_RT、内存锁定、CPU 隔离、`SCHED_FIFO` 调优在机器人 C++ 项目中的可核查实践。
3. **构建系统与包管理**：CMake / colcon / ament_cmake / Bazel 与 Conan / vcpkg / rosdep 的采用度与对比证据。[73]
4. **静态分析与代码质量**：clang-tidy / clang-format / cppcheck / sanitizers / CI 在机器人 C++ 仓库中的落地现状。
5. **求解器与实时性能基准**：面向运动学/动力学/轨迹优化求解器的公开基准、实时抖动测量方法学、跨库可比性讨论——本轮召回率为 **0**。[21][5][24][41][46][47]
6. **SIMD 与缓存优化**：机器人感知-控制闭环中的 SIMD 向量化与缓存友好数据结构实证数据。
7. **热度量化补全**：本轮所有候选条目**均未提供引用数、star、下载量或榜单排名**，因此“事实标准”类判断只能维持中等或低置信度 [64][66][70][60]。

### W13 方法论纪律（建议长期保留）
- 用“四问”筛前沿：是否多任务/多本体验证、是否开源、提升能否归因（数据/架构/算力）、是否有独立第三方评测。对 W1–W11 逐条套用后可见，**多数条目目前止步于第 2 问（未见开源与复现证据）** [23][52][92][81][32]。
- 检索时必须做**同名消歧**（Ceres / Pinocchio 已被证明会召回粒子物理与天体物理文献）[28][29][31][91][96]，并核对**撤稿状态** [77]。
- 引用纪律：优先 A/B 级证据；C 级加限定词；D 级仅作线索；E 级（如已撤稿记录）直接丢弃 [77][73][68]。

## 参考来源

[1] Xiaomi-Robotics-1: Scaling Vision-Language-Action Models with over 100K Hours of Real-World Trajectories — http://arxiv.org/abs/2607.15330v2
[2] Action Flow Matching for Continual Robot Learning — http://arxiv.org/abs/2504.18471v2
[3] Using Physiological Measures, Gaze, and Facial Expressions to Model Human Trust in a Robot Partner — http://arxiv.org/abs/2504.05291v1
[4] Scalable Aerial GNSS Localization for Marine Robots — http://arxiv.org/abs/2505.04095v2
[5] Real-Time Service Subscription and Adaptive Offloading Control in Vehicular Edge Computing — http://arxiv.org/abs/2512.14002v1
[6] Real time state monitoring and fault diagnosis system for motor based on LabVIEW — http://arxiv.org/abs/1806.09998v1
[7] Model-Based Capacitive Touch Sensing in Soft Robotics: Achieving Robust Tactile Interactions for Artistic Applications — http://arxiv.org/abs/2503.02280v1
[8] ACM COMPUTE 2025 Best Practices Track Proceedings — http://arxiv.org/abs/2512.02349v2
[9] Artificial Intelligence and Civil Justice: U.S. Practice, Policy, and Principles — https://doi.org/10.1093/ajcl/avag028
[10] Autonomous Planning In-space Assembly Reinforcement-learning free-flYer (APIARY) International Space Station Astrobee Testing — http://arxiv.org/abs/2512.03729v1
[11] Internal Audit of Pension Funds: The Case of Georgias Funded Pension Scheme — https://doi.org/10.52340/ekonomisti.2026.03.03
[12] Growing a Better Future through Responsible Crop Protection — https://doi.org/10.1093/ae/tmag004
[13] April | 2025 - CppCon — https://cppcon.org/2025/04/
[14] Developing a Robotic Surgery Training System for Wide Accessibility and Research — http://arxiv.org/abs/2505.20562v2
[15] CMU's IWSLT 2025 Simultaneous Speech Translation System — http://arxiv.org/abs/2506.13143v1
[16] Towards Transparent Ethical AI: A Roadmap for Trustworthy Robotic Systems — http://arxiv.org/abs/2508.05846v1
[17] Correction: Distributed multi-robot active gathering for non-uniform agriculture and forestry information — https://doi.org/10.3389/fpls.2025.1730134
[18] First D-FUMT₈ Silicon with SELF⟲ Logic Primitive: Native 8-Valued Hardware Realization with Lean 4 Refinement Proof, Four-Substrate Cross-Verification (Two FPGA Silicon Families + Aer Simulator + IBM Heron r2 Real Hardware) — https://doi.org/10.5281/zenodo.20192813
[19] First D-FUMT₈ Silicon with SELF⟲ Logic Primitive: Native 8-Valued Hardware Realization with Lean 4 Refinement Proof, Four-Substrate Cross-Verification (Two FPGA Silicon Families + Aer Simulator + IBM Heron r2 Real Hardware) — https://doi.org/10.5281/zenodo.20101174
[20] OSGNet @ Ego4D Episodic Memory Challenge 2025 — http://arxiv.org/abs/2506.03710v1
[21] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1
[22] Real-Time-Data Analytics in Raw Materials Handling — http://arxiv.org/abs/1802.00625v1
[23] Multi-Objective Memory Bandwidth Regulation and Cache Partitioning for Multicore Real-Time Systems — http://arxiv.org/abs/2505.11554v1
[24] NTIRE 2025 Challenge on Image Super-Resolution (x4): Methods and Results — http://arxiv.org/abs/2504.14582v3
[25] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1
[26] Technical Report for ICRA 2025 GOOSE 3D Semantic Segmentation Challenge: Adaptive Point Cloud Understanding for Heterogeneous Robotic Systems — http://arxiv.org/abs/2506.06995v1
[27] Influence of Operator Expertise on Robot Supervision and Intervention — http://arxiv.org/abs/2601.15069v2
[28] Dilepton measurements with CERES — http://arxiv.org/abs/0802.2679v1
[29] The CERES/NA45 Radial Drift Time Projection Chamber — http://arxiv.org/abs/0802.1443v2
[30] HS-SLAM: Hybrid Representation with Structural Supervision for Improved Dense SLAM — http://arxiv.org/abs/2503.21778v1
[31] Terraforming the dwarf planet: Interconnected and growable Ceres megasatellite world — http://arxiv.org/abs/2011.07487v5
[32] g2o vs. Ceres: Optimizing Scan Matching in Cartographer SLAM — http://arxiv.org/abs/2507.07142v1
[33] Translating C To Rust: Lessons from a User Study — http://arxiv.org/abs/2411.14174v2
[34] SACTOR: LLM-Driven Correct and Idiomatic C to Rust Translation with Static Analysis and FFI-Based Verification — http://arxiv.org/abs/2503.12511v3
[35] Surface sampling for mpox virus in multiple healthcare settings in Sierra Leone, June 2025 — https://doi.org/10.1101/2025.09.16.25335757
[36] Management of urinary stones by experts in stone disease (ESD 2025). — https://doi.org/10.4081/aiua.2025.14085
[37] Bi-specific T-cell engagers as a bridge to ciltacabtagene autoleucel in Relapsed/Refractory multiple myeloma: Real-world outcomes in an underserved urban population — https://doi.org/10.1182/blood-2025-4577
[38] SURG-42. Evaluating brainstem biopsy outcomes: Insights from frame-Based, MRI-Guided, and robot-Assisted techniques — https://doi.org/10.1093/neuonc/noaf201.1597
[39] Mapping the learning curve of robotic cholecystectomy: a multi‑surgeon cohort analysis — https://doi.org/10.1007/s00464-026-13196-4
[40] The RSNA Abdominal Traumatic Injury CT (RATIC) Dataset — http://arxiv.org/abs/2405.19595v1
[41] NTIRE 2025 Challenge on Short-form UGC Video Quality Assessment and Enhancement: KwaiSR Dataset and Study — http://arxiv.org/abs/2504.15003v1
[42] PDNS-Net: A Large Heterogeneous Graph Benchmark Dataset of Network Resolutions for Graph Learning — http://arxiv.org/abs/2203.07969v1
[43] The RSNA Intracranial Aneurysm (RSNA-ICA) Dataset — http://arxiv.org/abs/2610.01135v2
[44] Rethinking Trajectory Evaluation for SLAM: a Probabilistic, Continuous-Time Approach — http://arxiv.org/abs/1906.03996v1
[45] Overview of the Sensemaking Task at the ELOQUENT 2025 Lab: LLMs as Teachers, Students and Evaluators — http://arxiv.org/abs/2507.12143v1
[46] CPRet: A Dataset, Benchmark, and Model for Retrieval in Competitive Programming — http://arxiv.org/abs/2505.12925v2
[47] VQualA 2025 Challenge on Visual Quality Comparison for Large Multimodal Models: Methods and Results — http://arxiv.org/abs/2509.09190v1
[48] ROS 2 in a Nutshell: A Survey - ACM Digital Library — https://dl.acm.org/doi/full/10.1145/3815113
[49] The SCIP Optimization Suite 9.0 — http://arxiv.org/abs/2402.17702v2
[50] Soft robotic suits: State of the art, core technologies and open challenges — http://arxiv.org/abs/2105.10588v2
[51] Occupancy-SLAM: Simultaneously Optimizing Robot Poses and Continuous Occupancy Map — http://arxiv.org/abs/2405.10743v1
[52] No Cords Attached: Coordination-Free Concurrent Lock-Free Queues — http://arxiv.org/abs/2511.09410v1
[53] Optimal Algorithm Allocation for Robotic Network Cloud Systems — http://arxiv.org/abs/2104.12710v5
[54] VLSP 2025 MLQA-TSR Challenge: Vietnamese Multimodal Legal Question Answering on Traffic Sign Regulation — http://arxiv.org/abs/2510.20381v1
[55] Design of an Adaptive Lightweight LiDAR to Decouple Robot-Camera Geometry — http://arxiv.org/abs/2302.14334v2
[56] Secure and secret cooperation in robotic swarms — http://arxiv.org/abs/1904.09266v3
[57] A Survey of Robot Manipulation in Contact — http://arxiv.org/abs/2112.01942v3
[58] Malleable Robots — http://arxiv.org/abs/2502.04012v1
[59] Using Cache-coloring to Mitigate Inter-set Write Variation in Non-volatile Caches — http://arxiv.org/abs/1310.8494v1
[60] ros2_control Documentation (Rolling Ridley) — https://control.ros.org/rolling/downloads/ros2_control_rolling.pdf
[61] Nine Best Practices for Research Software Registries and Repositories: A Concise Guide — http://arxiv.org/abs/2012.13117v1
[62] Extending Behavior Trees for Robotic Missions with Quality Requirements — http://arxiv.org/abs/2503.16969v1
[63] Piezoelectric Soft Robot Inchworm Motion by Tuning Ground Friction through Robot Shape: Quasi-Static Modeling and Experimental Validation — http://arxiv.org/abs/2111.00944v2
[64] arXiv:2505.00136v1 [cs.LG] 30 Apr 2025 — https://arxiv.org/pdf/2505.00136
[65] Automate 3D Data Pipelines With USD Exchange SDK - NVIDIA — https://www.nvidia.com/en-us/on-demand/session/gtc26-dlit81639/
[66] Tutorial: Building ViSP Python bindings from source - Inria — https://visp-doc.inria.fr/doxygen/visp-3.7.0/tutorial-install-python-bindings.html
[67] Studying the Impact of TensorFlow and PyTorch Bindings on ... — https://dl.acm.org/doi/full/10.1145/3678168
[68] interfacing python with c/c++ performance : r/cpp - Reddit — https://www.reddit.com/r/cpp/comments/1e4z2m4/interfacing_python_with_cc_performance/
[69] Ark: An Open-source Python-based Framework for Robot Learning — https://arxiv.org/html/2506.21628v1
[70] Overview {#index} — pinocchio: Rolling 3.9.0 documentation — https://docs.ros.org/en/rolling/p/pinocchio/doc/Overview.html
[71] CXXStateTree – A modern C++ library for hierarchical state machines — https://news.ycombinator.com/item?id=44487221
[72] The Top Trends in Embedded Development for 2025 & Beyond — https://www.ezurio.com/resources/blog/the-top-trends-in-embedded-development-for-2025-beyond
[73] Why C++ project setup is still painful in 2025 (and my attempt to fix it) — https://www.reddit.com/r/cpp/comments/1pmmm5g/blog_why_c_project_setup_is_still_painful_in_2025/
[74] Top 10 C++ libraries for your next project - Incredibuild — https://www.incredibuild.com/blog/top-10-c-libraries-for-your-next-project
[75] The Self-Taught C/C++ Roadmap: From Zero to Systems ... - Medium — https://medium.com/@oz3dprinter/the-self-taught-c-c-roadmap-from-zero-to-systems-programming-in-8-weeks-e5ebaa9cd062
[76] Developing a 21st Century Global Library for Mathematics Research — http://arxiv.org/abs/1404.1905v1
[77] This paper has been withdrawn — http://arxiv.org/abs/cond-mat/0309395v2
[78] Four Simple Proprioceptive Estimators for Legged Robots — http://arxiv.org/abs/2605.23100v1
[79] Neural Volume Rendering: NeRF And Beyond — http://arxiv.org/abs/2101.05204v2
[80] NF-iSAM: Incremental Smoothing and Mapping via Normalizing Flows — http://arxiv.org/abs/2105.05045v1
[81] Smoothing Out the Edges: Continuous-Time Estimation with Gaussian Process Motion Priors on Factor Graphs — http://arxiv.org/abs/2605.09073v1
[82] On the maximum number of cliques in a graph — http://arxiv.org/abs/math/0602191v4
[83] Improved Multiscale Structural Mapping with Supervertex Vision Transformer for the Detection of Alzheimer's Disease Neurodegeneration — http://arxiv.org/abs/2604.14837v1
[84] Equality Constrained Linear Optimal Control With Factor Graphs — http://arxiv.org/abs/2011.01360v2
[85] A Tutorial on Linear Least Square Estimation — http://arxiv.org/abs/2211.15347v1
[86] A Molecular Implementation of the Least Mean Squares Estimator — http://arxiv.org/abs/1701.00602v1
[87] Fast Convergence for Weighted Least Squares Estimates — http://arxiv.org/abs/2605.00198v3
[88] nlstac: Non-Gradient Separable Nonlinear Least Squares Fitting — http://arxiv.org/abs/2402.04124v1
[89] Convergence of Alternating Least Squares Optimisation for Rank-One Approximation to High Order Tensors — http://arxiv.org/abs/1503.05431v1
[90] A Tutorial for Evaluating Cure Model Appropriateness — http://arxiv.org/abs/2605.04999v2
[91] PINOCCHIO and the hierarchical build-up of dark matter haloes — http://arxiv.org/abs/astro-ph/0109324v1
[92] Adapting Rigid-Body Dynamics Derivatives for Constraint Embedding Closed-Chain Models — http://arxiv.org/abs/2609.21024v1
[93] The Relativistic Elasticity of Rigid Bodies — http://arxiv.org/abs/physics/0307019v3
[94] On the invariant motions of rigid body rotation over the fixed point, via Euler angles — http://arxiv.org/abs/1601.04526v1
[95] On signal detection and confidence sets for low rank inference problems — http://arxiv.org/abs/1507.03829v2
[96] PINOCCHIO: pinpointing orbit-crossing collapsed hierarchical objects in a linear density field — http://arxiv.org/abs/astro-ph/0109323v2
[97] A Parametric and Feasibility Study for Data Sampling of the Dynamic Mode Decomposition--Range, Resolution, and Universal Convergence States — http://arxiv.org/abs/2110.06573v2


---

*Generated by research-bot · topic=`cpp-robotics` · depth=`standard` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading · model=`deepseek-v4-flash` · sources=97 · duration=353s · 2026-10-06T22:13:58+00:00*
