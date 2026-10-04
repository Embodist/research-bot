# C++ 机器人工程与实时系统：证据化调研报告

**日期**：2026-10-04（UTC） ｜ **领域**：机器人 C++ 生态（Eigen / Sophus / Ceres / GTSAM / Pinocchio）、实时与确定性工程、构建与包管理、性能工程 ｜ **检索源数量**：候选来源 78 条（编号 [1]–[78]），另附领域预置种子资源 12 项（库与项目官方链接）

---

## 摘要（Executive Summary）

本报告基于 78 条候选检索结果撰写。必须首先给出**覆盖度警告**：本轮候选证据与主题的匹配度严重不均——机器人 C++ 数值库、构建与包管理、C++/Python 绑定三个子问题的候选块**几乎全部为检索噪声**（如图像超分挑战赛 [2]、音频 MOS 挑战赛 [4]、越南语法律问答 [5]、宇宙学 PINOCCHIO [20][41]），因此这些章节只能给出**证据缺口说明 + 预置种子资源**，而非"最新进展"结论。

可被证据支撑的结论限于以下几条：

1. **ROS 2 实时调度的新思路（最强的一条一手证据）**：有工作提出在 ROS 2/Linux 上建立「回调（callback）↔ OS 线程」的**持久一对一映射**，从而绕过中间件层（ROS 2 Executor）调度，直接把 OS 调度参数施加于回调，简化此前"嵌套调度"（OS 线程调度 + 中间件层调度）的分析框架 [69]。该工作标注为 Work in Progress、未见实验数据。
2. **无锁数据结构的复杂度重心被重新定位**：并发无锁队列的主要设计负担来自**内存回收危害（ABA、use-after-free、不安全回收）的防护机制**，这些协调机制"often dominate the design, overshadowing the queue itself"；有作者进一步主张对回收危害的"无限防护"形成**保护悖论**（过度保护反而降低系统韧性），并提出 coordination-free 方案 [66]。该结论为预印本自述，缺评测数据与第三方复现。
3. **实时资源分享方向存在标题级线索**：多核实时系统上的**无锁容错资源分享协议 LEFT-RS** [70]，仅取得标题级信息，内容与指标 `> 待核实`。

**最重要的三个证据缺口（均标注 `> 待核实`）**：
- **PREEMPT_RT、WCET 分析、实时内存分配器/页错误预分配**在 2024–2026 年的进展：本批证据**零覆盖**（仅在 [66] 中侧面涉及回收延迟）。
- **Eigen / Sophus / Ceres Solver / GTSAM / Pinocchio 近 1–2 年版本、API 与性能改进**：本批证据**零覆盖**，检索词遭遇严重同名假阳性（CERES 加速器实验 [13][14]、Ceres 矮行星 [16]、宇宙学 PINOCCHIO [20][41]）。
- **构建与包管理（现代 CMake / Conan / vcpkg / rosdep / C++20 modules）、C++/Python 绑定与零拷贝（pybind11 / nanobind / rclpy / rmw zero-copy）**：本批证据**零覆盖**。

方法学提示（非检索证据）：本报告刻意不把 demo、无数据预印本当作强结论；凡仅取得标题的条目一律降级为"线索"，并标注 `> 待核实`。

---

## 一、关键前沿进展（近 1–2 年）

### 1.1 ROS 2 on Linux 的实时调度：绕过中间件层

- **观点**：通过建立 callback 与 OS 线程之间**持久的一对一对应关系**，可以忽略 ROS 2 Executor 中间件层，把 OS 层调度参数直接作用于回调，从而把"嵌套调度"问题（OS 线程调度 + 中间件层调度）简化为单一层次 [69]。
- **热度证据**：`> 待核实`（候选块未提供引用数、star 或榜单信号 [69]）。
- **权威证据**：arXiv 预印本（cs.OS，arXiv:2505.06546v1，2025-05-10），标题自标 "Work in Progress"，未见同行评审 venue [69]。
- **关注度**：低 —— 依据：候选块仅有标题与摘要片段，无引用/讨论热度信号 [69]。
- **推荐度**：★★★☆☆ —— 与"ROS 2 执行器/实时调度"高度相关，思路（回调线程绑定）值得跟踪，但无实测延迟/抖动数据 [69]。

### 1.2 无锁并发与内存回收：从"队列逻辑"转向"回收危害防护"

- **观点**：无锁队列的复杂度主要不来自 FIFO 逻辑，而来自为防 ABA、use-after-free 与不安全回收所引入的协调机制，这些机制常常"dominate the design"；作者提出 **coordination-free 的并发无锁队列**思路 [66]。
- **延伸主张**：追求对回收危害的"无限防护"是理论上自洽但成本高昂且不实用，并会形成 **protection paradox**（过度保护降低系统韧性）[66]。
- **热度证据**：`> 待核实`（无引用数/star/社区讨论数据 [66]）。
- **权威证据**：arXiv 预印本（cs.DC，arXiv:2511.09410v1，2025-11-12），单作者；未见同行评审信息 [66]。
- **关注度**：低 —— 依据：仅有标题与摘要，无第三方复现或榜单信号 [66]。
- **推荐度**：★★☆☆☆ —— "保护悖论"对实时系统内存回收策略设计有启发，但方案的正确性保证（lock-free / wait-free）、是否牺牲严格 FIFO 与无界容量在候选片段中未交代 [66]。

### 1.3 多核实时系统的无锁容错资源分享

- **线索**：**LEFT-RS: A Lock-Free Fault-Tolerant Resource Sharing Protocol for Multicore Real-Time Systems** [70]，从标题判断直接落在"实时 C++ 多核资源分享"这一核心议题上。
- **证据强度**：仅标题级（本轮未抽取到摘要/实验数据），内容、协议性质（是否含优先级继承/天花板）、可调度性分析结论**全部 `> 待核实`** [70]。
- **热度证据**：`> 待核实` [70]。**权威证据**：`> 待核实`（未取得 venue 信息）[70]。**关注度**：低（无可核查信号）[70]。**推荐度**：★★★☆☆ —— 主题命中度高，建议优先取证 [70]。

### 1.4 承上启下：预算式实时执行器（前序工作，2021）

- **观点线索**：**Budget-based real-time Executor for Micro-ROS** [67] 代表"执行器层引入预算（budget）语义"的路线，是理解 [69] 所批评的"中间件层调度"问题的必要背景。
- **热度/权威**：`> 待核实`（本轮仅有标题与链接，未取得摘要与 venue 信息）[67]。
- **关注度**：低 [67]。**推荐度**：★★★☆☆ —— 作为 ROS 2 实时执行器的历史锚点值得补读 [67]。

### 1.5 邻近领域：带截止期的任务卸载与资源分配

- **观点**：在车联网边缘计算（VEC）中，有工作把"带截止期的任务卸载与资源分配"形式化为 **DOAP** 问题（约束含带宽与算力，目标最大化车辆总效用），并提出 **SARound** 求解 [42]。
- **热度证据**：`> 待核实` [42]。**权威证据**：arXiv 预印本（cs.DC，arXiv:2512.14002v1，2025-12-16），作者含 Arvind Easwaran（实时系统方向）[42]。**关注度**：低 [42]。
- **推荐度**：★★☆☆☆ —— 领域为 VEC 而非机器人 C++，仅作"截止期约束下实时资源分配"方法论参考 [42]。

### 1.6 动力学导数算法：放宽"速度效应局部构型不变"假设

- **观点**：**Adapting Rigid-Body Dynamics Derivatives for Constraint Embedding Closed-Chain Models** 把刚体动力学一阶导数的既有高效算法扩展到以 **constraint embedding** 建模的闭链系统，取消了"关节速度效应局部构型不变"这一既有导数方法的假设 [21]。
- **热度证据**：`> 待核实`（候选块未提供引用数）[21]。**权威证据**：arXiv 预印本（cs.RO，arXiv:2609.21024v1），未见会议/期刊信息 [21]。**关注度**：低 [21]。
- **推荐度**：★★★☆☆ —— 与 Pinocchio 类库的解析导数/闭链计算直接相关，但"是否已被主流库采纳实现" `> 待核实` [21]。

### 1.7 本批证据明确缺失的前沿主题

> 待核实：**PREEMPT_RT（内核实时补丁）2024–2026 新进展**、**WCET（最坏执行时间）分析新方法/工具**、**实时内存分配器与页错误确定性**在本批证据中**无任何条目覆盖**。这不是"没有进展"，而是**本轮检索未召回**，任何结论都不可写。

---

## 二、数值与优化库生态对比

**核心结论（缺口声明）**：本批候选证据**未包含任何** Eigen / Sophus / Ceres Solver / GTSAM / Pinocchio 的 release notes、API 变更或性能 benchmark。候选 6 条证据分别属于图像超分挑战赛 [2]、音频 MOS 挑战赛 [4]、越南语多模态法律问答 [5]、机器人持续学习 [7]、闭链刚体动力学导数 [21]、宇宙学 PINOCCHIO [20]，**无一条可支撑库版本/性能对比** [2][4][5][7][20][21]。

**术语假阳性警示（重要）**：以库名作为检索词会大量命中同名词条——`CERES` 命中 CERN SPS 的双轻子测量 [13] 与 CERES/NA45 径向漂移 TPC [14]，以及"Ceres 矮行星地球化"设想 [16]；`PINOCCHIO` 命中暗物质晕层级形成 [20][41]。后续检索必须加限定词（如 `Pinocchio robotics dynamics`、`Ceres Solver release notes`）。

### 表 2-1 种子资源：机器人 C++ 数值/动力学/优化核心库（预置清单，非 [1]–[78] 编号证据）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Eigen（线性代数基础库） | ongoing | 社区（libeigen） | `> 待核实` | 开源项目官方仓库（种子清单给定） | `> 待核实` | ★★★★★ | https://gitlab.com/libeigen/eigen | 机器人数值栈底座，模板表达式/对齐（ABI）问题源头 |
| Ceres Solver（非线性最小二乘） | ongoing | Google | `> 待核实` | 官方项目与文档（种子清单给定） | `> 待核实` | ★★★★☆ | http://ceres-solver.org/ ｜ https://github.com/ceres-solver/ceres-solver | 标定、BA、IK 常用；自动微分开销是性能关注点 |
| GTSAM（因子图优化） | ongoing | Georgia Tech（borglab） | `> 待核实` | 官方项目（种子清单给定） | `> 待核实` | ★★★★☆ | https://gtsam.org/ ｜ https://github.com/borglab/gtsam | SLAM/状态估计后端，iSAM 系谱 [38] |
| Pinocchio（刚体动力学与解析导数） | 2019（论文） | LAAS-CNRS（stack-of-tasks） | `> 待核实` | 论文 + 官方仓库（种子清单给定） | `> 待核实` | ★★★★★ | https://arxiv.org/abs/1906.09139 ｜ https://github.com/stack-of-tasks/pinocchio | 高效刚体算法与解析导数；与 [21] 的闭链导数改进相关 |
| Sophus（SO(3)/SE(3) 李群） | ongoing | strasdat | `> 待核实` | 官方仓库（种子清单给定） | `> 待核实` | ★★★★☆ | https://github.com/strasdat/Sophus | 流形上的位姿运算，常与 Ceres/GTSAM 搭配 |

> 说明：上表链接来自本次调研预置种子清单，**不在 [1]–[78] 编号证据列表内**；其 GitHub star、下载量等热度/关注度指标本轮**未采集**，故一律标 `> 待核实`，不做数字推测。推荐度为编辑判断（基于领域基础库地位与主题相关性），非热度推断。

### 表 2-2 与数值/优化主题**邻近但不对口**的可引用证据

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Fast Convergence for Weighted Least Squares Estimates | 2026 | `> 待核实` | `> 待核实` | arXiv（math.ST）[26] | 低 | ★★☆☆☆ | http://arxiv.org/abs/2605.00198v3 | 加权最小二乘的收敛速率理论，与 Ceres 类求解无关；Fisher 信息无穷时超经典收敛率 [26] |
| nlstac: Non-Gradient Separable Nonlinear Least Squares Fitting | 2024 | `> 待核实` | `> 待核实` | arXiv 预印本 [28] | 低 | ★★☆☆☆ | http://arxiv.org/abs/2402.04124v1 | 可分离非线性最小二乘，仅作方法参考 [28] |
| Convergence of Alternating Least Squares … High Order Tensors | 2015 | `> 待核实` | `> 待核实` | arXiv 预印本 [29] | 低 | ★☆☆☆☆ | http://arxiv.org/abs/1503.05431v1 | 张量 ALS 收敛性，与机器人栈相关性弱 [29] |
| Robust Incremental Smoothing and Mapping (riSAM) | 2022 | `> 待核实` | `> 待核实` | arXiv 预印本 [32] | `> 待核实` | ★★★☆☆ | http://arxiv.org/abs/2209.14359v2 | 增量平滑与建图的鲁棒化线索，与 GTSAM/iSAM 传统同源；具体指标 `> 待核实` [32] |
| Multi-modal and inertial sensor solutions for navigation-type factor graphs | 2017 | `> 待核实` | citations=19 [38] | 学位论文（DOI:10.1575/1912/9305）[38] | 中（citations=19）[38] | ★★★☆☆ | https://doi.org/10.1575/1912/9305 | 面向导航因子图的 sum-product 推理（Multi-modal iSAM）[38] |
| Adapting Rigid-Body Dynamics Derivatives for Constraint Embedding Closed-Chain Models | 2026 | `> 待核实` | `> 待核实` | arXiv（cs.RO）[21] | 低 | ★★★☆☆ | http://arxiv.org/abs/2609.21024v1 | 闭链约束嵌入模型的动力学一阶导数算法扩展 [21] |

**生态对比结论**：在缺少各库官方 release 与第三方基准的前提下，**不对任何库做性能优劣排序**。可核查的仅是"谱系关系"：GTSAM 的增量平滑传统可由 [38]（2017，citations=19）与 [32] 追溯，Pinocchio 的解析导数议题可由 [21] 侧面呼应。

---

## 三、实时 C++ 与确定性工程

| 主题 | 可用证据 | 热度 | 权威 | 关注度 | 推荐度 |
|---|---|---|---|---|---|
| ROS 2 回调↔OS 线程一对一映射，绕过 Executor 中间件层 | [69]（观点见 §1.1） | `> 待核实` | arXiv 预印本，Work in Progress [69] | 低 | ★★★☆☆ |
| 无锁队列的内存回收危害与 coordination-free 设计 | [66]（观点见 §1.2） | `> 待核实` | arXiv 预印本（cs.DC）[66] | 低 | ★★☆☆☆ |
| 多核实时无锁容错资源分享协议 LEFT-RS | [70]（仅标题级） | `> 待核实` | `> 待核实` [70] | 低 | ★★★☆☆ |
| 预算式实时执行器（Micro-ROS） | [67]（仅标题级） | `> 待核实` | `> 待核实` [67] | 低 | ★★★☆☆ |
| ROS 2 节点组合（Node Composition）对系统的影响 | [48]（仅标题级；组合与 intra-process 通路相关） | `> 待核实` | arXiv 预印本（2023）[48] | `> 待核实` | ★★★☆☆ |
| ROS 2 移动机器人算法与维护者视角综述 | [49]（仅标题级，survey） | `> 待核实` | arXiv 预印本（2023，survey）[49] | `> 待核实` | ★★★☆☆ |

### 确定性工程的关键空白（必须显式记录）

> 待核实：**异常/RTTI 禁用、ABI 对齐、实时性 vs 现代 C++ 特性（异常、dynamic_cast、std::function 分配、`new`/`delete` 在热路径）的冲突**——本次候选证据**零覆盖**。这是业界公认争议点，但**本报告不据记忆下结论**，需补充检索 ROS 2 官方设计文档、`-fno-exceptions`/`-fno-rtti` 实践、Eigen 对齐（`EIGEN_MAX_ALIGN_BYTES`、`aligned_allocator`）与 ABI 兼容性资料。
>
> 待核实：**PREEMPT_RT 主线化后的版本节奏、`cyclictest`/`rtla` 工作流、WCET 静态分析工具链**，本轮均未召回。

---

## 四、构建系统与包管理

**核心结论（缺口声明）**：本轮针对 q4 的 5 条候选证据**全部与构建/包管理无关**：分别为机器人持续学习 [7]、Basilisk 天体动力学与 ROS 2 桥接 [47]、ROS 系统 PHM 工具 [63]、ROS2swarm 群体行为包 [64]、OtterROS 无人水面艇 [65]。**没有一条**涉及现代 CMake、Conan/vcpkg/rosdep、C++20/23 modules、静态分析或 CI [7][47][63][64][65]。

### 表 4-1 种子资源：构建与包管理相关项目（预置清单，非编号证据）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| vcpkg | ongoing | Microsoft | `> 待核实` | 官方仓库（种子清单给定） | `> 待核实` | ★★★★☆ | https://github.com/microsoft/vcpkg | 面向 C/C++ 的跨平台依赖管理，与 CMake 集成 |
| Conan | ongoing | conan-io | `> 待核实` | 官方仓库（种子清单给定） | `> 待核实` | ★★★★☆ | https://github.com/conan-io/conan | C/C++ 包管理器，二进制包与交叉编译场景 |
| pybind11 | ongoing | pybind（社区） | `> 待核实` | 官方仓库（种子清单给定） | `> 待核实` | ★★★★★ | https://github.com/pybind/pybind11 | C++/Python 绑定事实标准，见 §6 |
| nanobind | ongoing | wjakob（nanobind） | `> 待核实` | 官方仓库（种子清单给定） | `> 待核实` | ★★★★☆ | https://github.com/wjakob/nanobind | 更轻量的绑定方案（宣称更小体积/更低开销，`> 待核实`） |

### 表 4-2 可引用（但主题邻近度有限）的工程规范证据

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Nine Best Practices for Research Software Registries and Repositories | 2020 | `> 待核实` | `> 待核实` | arXiv 预印本 [62] | `> 待核实` | ★★☆☆☆ | http://arxiv.org/abs/2012.13117v1 | 科研软件注册/仓库治理规范，可映射到内部包仓库与 rosdep 治理，但**非 C++ 构建技术** [62] |
| ACM COMPUTE 2025 Best Practices Track Proceedings | 2025 | `> 待核实` | `> 待核实` | arXiv（会议论文集）[61] | 低 | ★☆☆☆☆ | http://arxiv.org/abs/2512.02349v2 | 仅会议论文集条目，未见可抽取的具体工程实践 [61] |

> 待核实：ROS 2 生态的**构建层事实**（`ament_cmake` 与 `colcon`、`rosdep` 与系统包/Conan 的分工、`package.xml` 依赖语义、C++20 modules 在 ROS 2 中的可用性）本轮**无一手来源**。不要基于记忆填写版本号或兼容矩阵。

---

## 五、性能剖析与基准

**核心结论（缺口声明）**：本轮**未召回任何**针对机器人 C++ 栈的性能基准（如因子图求解时间、自动微分开销、刚体动力学批处理吞吐、ROS 2 通信时延抖动、rmw 实现对比）。候选块中与"性能"沾边的条目要么领域错配，要么仅为标题级：

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Impact of ROS 2 Node Composition in Robotic Systems | 2023 | `> 待核实` | `> 待核实` | arXiv 预印本 [48] | `> 待核实` | ★★★☆☆ | http://arxiv.org/abs/2305.09933v1 | 节点组合（同进程/跨进程）对性能的影响，是理解 intra-process 通路的直接入口；具体数字 `> 待核实` [48] |
| Performance Analysis of Software to Hardware Task Migration in Codesign | 2010 | `> 待核实` | `> 待核实` | arXiv 预印本 [50] | 低 | ★☆☆☆☆ | http://arxiv.org/abs/1002.1154v1 | 软硬件任务迁移性能分析，与机器人栈无关 [50] |
| Performance of Genetic Algorithms in the Context of Software Model Refactoring | 2023 | `> 待核实` | `> 待核实` | arXiv 预印本 [51] | 低 | ★☆☆☆☆ | http://arxiv.org/abs/2308.13875v1 | 领域错配（软件重构），检索噪声 [51] |
| Real-Time-Data Analytics in Raw Materials Handling | 2018 | `> 待核实` | `> 待核实` | arXiv 预印本 [57] | 低 | ★☆☆☆☆ | http://arxiv.org/abs/1802.00625v1 | 工业实时数据分析，非机器人 C++ 基准 [57] |
| Technical Report for ICRA 2025 GOOSE 3D Semantic Segmentation Challenge | 2025 | `> 待核实` | `> 待核实` | arXiv 预印本（ICRA 2025 挑战赛技术报告）[11] | `> 待核实` | ★★☆☆☆ | http://arxiv.org/abs/2506.06995v1 | 属**感知任务**基准，非系统工程性能基准；可用于说明机器人领域基准多为任务指标而非系统指标 [11] |

**基准方法论建议（编辑判断，非检索证据）**：机器人系统级性能报告应至少显式给出四要素——(a) 硬件与 CPU 隔离/亲和性配置；(b) 负载规模（回调数、线程数、消息频率/大小）；(c) 延迟分布而非均值（p50/p99/p99.9 与抖动最大值）；(d) 仿真 or 真机边界。本轮证据 [69] 恰恰在这四项上全部缺失，因此其结论只能视为**设计假设**而非**实测结论** [69]。

---

## 六、C++ 与 Python 协作（绑定/部署）

**核心结论（缺口声明）**：q5 的候选证据**完全无关**——[5] 为越南语交通标志法规多模态法律问答（检索 F2 64.55%、问答准确率 86.30%）[5]，[73] 为 ACM MM 2025 Event-Enriched Image Analysis Grand Challenge [73]，二者均不涉及 C++/Python 绑定、序列化、内存共享或 ROS 2 中间件性能。因此本节**不产出任何技术结论**。

### 表 6-1 种子资源与邻近线索

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| pybind11 | ongoing | pybind（社区） | `> 待核实` | 官方仓库（种子清单给定） | `> 待核实` | ★★★★★ | https://github.com/pybind/pybind11 | ROS 2 Python 绑定（rclpy）与大量机器人库的绑定底座 |
| nanobind | ongoing | wjakob（nanobind） | `> 待核实` | 官方仓库（种子清单给定） | `> 待核实` | ★★★★☆ | https://github.com/wjakob/nanobind | 轻量绑定替代方案；相对 pybind11 的开销/体积改进**宣称**内容 `> 待核实` |
| ePython: An implementation of Python for the many-core Epiphany coprocessor | 2020 | `> 待核实` | `> 待核实` | arXiv 预印本 [77] | 低 | ★☆☆☆☆ | http://arxiv.org/abs/2010.14827v1 | 异构多核上的 Python 实现，仅作"跨语言/异构部署"边缘线索，与 pybind11/nanobind 不可类比 [77] |

> 待核实（三项关键问题，本轮均无一手来源）：
> 1. **pybind11 vs nanobind 的调用开销对比**（参数类型转换、GIL 持有开销、编译期与运行期权衡）——需检索两者官方的 benchmark/文档页面，而非社区转述。
> 2. **rclpy 相对 rclcpp 的额外开销来源与量级**（解释器、绑定层、序列化与内存分配路径）——需 ROS 2 官方 performance/design 文档与 rclpy 仓库 issue。
> 3. **ROS 2 零拷贝通路的真实边界**（intra-process communication、Loaned Messages、rmw 层 zero-copy；以及 Python 侧是否可能真正零拷贝）——需 ROS 2 官方文档与 rmw 实现（如 rmw_iceoryx、Cyclone DDS）资料；本轮唯一相关标题级入口为节点组合研究 [48]。

---

## 七、经典参考资料与工程规范

### 表 7-1 经典与奠基性资料

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Pinocchio: analytical derivatives of rigid body dynamics | 2019 | LAAS-CNRS | `> 待核实` | 论文 + 官方仓库（种子清单给定） | `> 待核实` | ★★★★★ | https://arxiv.org/abs/1906.09139 | 高效刚体算法与解析导数的奠基性参考；其导数假设正被 [21] 在闭链约束嵌入情形下放宽 |
| Sophus（SO(3)/SE(3) 李群） | ongoing | strasdat | `> 待核实` | 官方文档/仓库（种子清单给定） | `> 待核实` | ★★★★☆ | https://github.com/strasdat/Sophus | 流形位姿运算的经典实现 |
| Ceres Solver（非线性最小二乘） | ongoing | Google | `> 待核实` | 官方文档（种子清单给定） | `> 待核实` | ★★★★☆ | http://ceres-solver.org/ | 标定/BA/IK 的经典求解器 |
| GTSAM（因子图） | ongoing | Georgia Tech | `> 待核实` | 官方站点（种子清单给定） | `> 待核实` | ★★★★☆ | https://gtsam.org/ | SLAM/状态估计的因子图范式代表 |
| Multi-modal and inertial sensor solutions for navigation-type factor graphs | 2017 | `> 待核实` | citations=19 [38] | 学位论文（DOI:10.1575/1912/9305）[38] | 中（citations=19）[38] | ★★★☆☆ | https://doi.org/10.1575/1912/9305 | 导航型因子图的 sum-product 推理（Multi-modal iSAM），因子图传统的可核查文献锚点 [38] |
| Robust Incremental Smoothing and Mapping (riSAM) | 2022 | `> 待核实` | `> 待核实` | arXiv 预印本 [32] | `> 待核实` | ★★★☆☆ | http://arxiv.org/abs/2209.14359v2 | 增量平滑的鲁棒化方向 [32] |
| Fast Convergence for Weighted Least Squares Estimates | 2026 | `> 待核实` | `> 待核实` | arXiv（math.ST）[26] | 低 | ★★☆☆☆ | http://arxiv.org/abs/2605.00198v3 | 最小二乘估计的收敛率理论（Fisher 信息无穷时的超经典速率），方法论背景 [26] |
| From the Desks of ROS Maintainers: A Survey of Modern & Capable Mobile Robotics Algorithms in ROS 2 | 2023 | ROS 维护者群体 | `> 待核实` | arXiv 预印本（survey）[49] | `> 待核实` | ★★★☆☆ | http://arxiv.org/abs/2307.15236v2 | 从维护者视角看 ROS 2 算法生态与工程取舍，适合作为工程实践章节的入口读物 [49] |
| Nine Best Practices for Research Software Registries and Repositories | 2020 | `> 待核实` | `> 待核实` | arXiv 预印本 [62] | `> 待核实` | ★★☆☆☆ | http://arxiv.org/abs/2012.13117v1 | 科研软件仓库治理规范，可迁移到内部 C++ 包仓库/发布流程 [62] |

### 术语消歧备忘（供后续检索使用）

`CERES` 库名会命中：CERN SPS 双轻子测量 [13]、CERES/NA45 时间投影室 [14]、Ceres 矮行星巨型卫星世界设想 [16]；`PINOCCHIO` 会命中宇宙学暗物质晕层级形成 [20][41]。检索时应使用 `Ceres Solver`、`Pinocchio robotics`、`GTSAM factor graph` 等强限定组合。同理，`least squares` 类检索会召回分子实现 LMS [27]、可分离非线性最小二乘 [28]、张量 ALS 收敛 [29]，均**非机器人 C++ 工程证据**。

---

## 八、建议关注清单（Watchlist）

1. **ROS 2 回调↔OS 线程一对一映射方案** [69] —— 跟踪是否有正式发表与实测延迟/抖动数据；验证问题：回调数增长时线程数如何扩展？与 Micro-ROS 预算执行器 [67] 的路线差异与可组合性？
2. **LEFT-RS 多核实时无锁容错资源分享协议** [70] —— 本轮仅有标题，需优先取证：是否提供可调度性分析、与优先级天花板/继承协议的对比、是否给出最坏阻塞时间上界。
3. **无锁队列的 coordination-free 设计与"保护悖论"** [66] —— 跟踪其正式发表与复现；验证问题：其进展性保证（lock-free/wait-free）、是否牺牲严格 FIFO 与无界容量、最坏回收延迟上界。
4. **PREEMPT_RT 与 WCET 工具链（本轮完全缺失）** `> 待核实` —— 建议以专属检索补齐（内核实时补丁版本节奏、`cyclictest`/`rtla` 实践、静态 WCET 工具），本报告**不对其现状下任何结论**。
5. **Eigen / Sophus / Ceres / GTSAM / Pinocchio 的 releases 与 CHANGELOG** `> 待核实` —— 建议直接走各项目官方仓库的 release/CHANGELOG 页面取证，替代易受同名词污染的通用搜索。
6. **闭链约束嵌入模型的动力学导数算法** [21] —— 跟踪是否被主流动力学库采纳实现，以及相对既有导数方法的速度/精度实测。
7. **ROS 2 节点组合与进程内通信** [48] —— 作为 C++/Python 跨语言开销与零拷贝议题的入口，配合官方 performance 文档核实。
8. **ROS 2 维护者视角算法综述** [49] —— 用于校准"哪些软件实践是社区共识、哪些只是个别主张"。
9. **科研软件仓库治理规范** [62] —— 作为内部包管理/发布流程的规范化参考（需注意其领域为科研软件注册库，非 C++ 构建技术）。
10. **因子图增量平滑的鲁棒化（riSAM）** [32] 与**导航型因子图推理文献** [38] —— 用于建立 GTSAM 谱系的可核查阅读路径（[38] 是本批中少数带引用数信号的条目，citations=19）。

**整体检索策略建议**：本轮 6 个子问题中，仅 q1 与 q3 取得了可用证据，q2/q4/q5 基本为噪声。后续应放弃"库名 + 泛化词"的召回方式，改为**结构性来源优先**：GitHub Releases/CHANGELOG、项目官方文档站、ROS 2 官方 design/performance 文档、以及带 venue 限定的学术检索（ICRA/CoRL/RSS/RTSS/ECRTS + 年份区间）。

---

## 参考来源

- [2] NTIRE 2025 Challenge on Image Super-Resolution (x4): Methods and Results — http://arxiv.org/abs/2504.14582v3
- [4] The AudioMOS Challenge 2025 — http://arxiv.org/abs/2509.01336v1
- [5] VLSP 2025 MLQA-TSR Challenge: Vietnamese Multimodal Legal Question Answering on Traffic Sign Regulation — http://arxiv.org/abs/2510.20381v1
- [7] Action Flow Matching for Continual Robot Learning — http://arxiv.org/abs/2504.18471v2
- [11] Technical Report for ICRA 2025 GOOSE 3D Semantic Segmentation Challenge — http://arxiv.org/abs/2506.06995v1
- [13] Dilepton measurements with CERES — http://arxiv.org/abs/0802.2679v1
- [14] The CERES/NA45 Radial Drift Time Projection Chamber — http://arxiv.org/abs/0802.1443v2
- [16] Terraforming the dwarf planet: Interconnected and growable Ceres megasatellite world — http://arxiv.org/abs/2011.07487v5
- [20] PINOCCHIO and the hierarchical build-up of dark matter haloes — http://arxiv.org/abs/astro-ph/0109324v1
- [21] Adapting Rigid-Body Dynamics Derivatives for Constraint Embedding Closed-Chain Models — http://arxiv.org/abs/2609.21024v1
- [26] Fast Convergence for Weighted Least Squares Estimates — http://arxiv.org/abs/2605.00198v3
- [27] A Molecular Implementation of the Least Mean Squares Estimator — http://arxiv.org/abs/1701.00602v1
- [28] nlstac: Non-Gradient Separable Nonlinear Least Squares Fitting — http://arxiv.org/abs/2402.04124v1
- [29] Convergence of Alternating Least Squares Optimisation for Rank-One Approximation to High Order Tensors — http://arxiv.org/abs/1503.05431v1
- [32] Robust Incremental Smoothing and Mapping (riSAM) — http://arxiv.org/abs/2209.14359v2
- [38] Multi-modal and inertial sensor solutions for navigation-type factor graphs — https://doi.org/10.1575/1912/9305
- [41] PINOCCHIO: pinpointing orbit-crossing collapsed hierarchical objects in a linear density field — http://arxiv.org/abs/astro-ph/0109323v2
- [42] Real-Time Service Subscription and Adaptive Offloading Control in Vehicular Edge Computing — http://arxiv.org/abs/2512.14002v1
- [47] Bridging the Basilisk Astrodynamics Framework with ROS 2 for Modular Spacecraft Simulation and Hardware Integration — http://arxiv.org/abs/2512.09833v2
- [48] Impact of ROS 2 Node Composition in Robotic Systems — http://arxiv.org/abs/2305.09933v1
- [49] From the Desks of ROS Maintainers: A Survey of Modern & Capable Mobile Robotics Algorithms in the Robot Operating System 2 — http://arxiv.org/abs/2307.15236v2
- [50] Performance Analysis of Software to Hardware Task Migration in Codesign — http://arxiv.org/abs/1002.1154v1
- [51] Performance of Genetic Algorithms in the Context of Software Model Refactoring — http://arxiv.org/abs/2308.13875v1
- [57] Real-Time-Data Analytics in Raw Materials Handling — http://arxiv.org/abs/1802.00625v1
- [61] ACM COMPUTE 2025 Best Practices Track Proceedings — http://arxiv.org/abs/2512.02349v2
- [62] Nine Best Practices for Research Software Registries and Repositories: A Concise Guide — http://arxiv.org/abs/2012.13117v1
- [63] Prognostic and Health Management (PHM) tool for Robot Operating System (ROS) — http://arxiv.org/abs/2011.09222v1
- [64] ROS2swarm - A ROS 2 Package for Swarm Robot Behaviors — http://arxiv.org/abs/2405.02438v1
- [65] OtterROS: Picking and Programming an Uncrewed Surface Vessel for Experimental Field Robotics Research with ROS 2 — http://arxiv.org/abs/2404.05627v2
- [66] No Cords Attached: Coordination-Free Concurrent Lock-Free Queues — http://arxiv.org/abs/2511.09410v1
- [67] Budget-based real-time Executor for Micro-Ros — http://arxiv.org/abs/2105.05590v2
- [69] Work in Progress: Middleware-Transparent Callback Enforcement in Commoditized Component-Oriented Real-time Systems — http://arxiv.org/abs/2505.06546v1
- [70] LEFT-RS: A Lock-Free Fault-Tolerant Resource Sharing Protocol for Multicore Real-Time Systems — http://arxiv.org/abs/2512.21701v1
- [73] Event-Enriched Image Analysis Grand Challenge at ACM Multimedia 2025 — http://arxiv.org/abs/2508.18904v1
- [77] ePython: An implementation of Python for the many-core Epiphany coprocessor — http://arxiv.org/abs/2010.14827v1

**种子资源（非 [1]–[78] 编号证据，链接为官方站点/仓库）**：Eigen（https://gitlab.com/libeigen/eigen ）、Pinocchio（https://github.com/stack-of-tasks/pinocchio 、https://arxiv.org/abs/1906.09139 ）、Ceres Solver（http://ceres-solver.org/ 、https://github.com/ceres-solver/ceres-solver ）、GTSAM（https://gtsam.org/ 、https://github.com/borglab/gtsam ）、Sophus（https://github.com/strasdat/Sophus ）、pybind11（https://github.com/pybind/pybind11 ）、nanobind（https://github.com/wjakob/nanobind ）、vcpkg（https://github.com/microsoft/vcpkg ）、Conan（https://github.com/conan-io/conan ）。

---

*Generated by research-bot · topic=`cpp-robotics` · depth=`standard` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading · model=`deepseek-v4-flash` · sources=78 · duration=314s · 2026-10-04T22:13:50+00:00*
