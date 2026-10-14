# 机器人运动学、控制与 ROS 2：从实验室走向真机规模化进程中的增量快照（2024–2026）

**报告日期（UTC）**：2026-10-14 ｜ **领域**：机器人运动学（kinematics）、实时控制（real-time control）、ROS 2 软件栈 ｜ **检索源数量**：34 条候选引用（其中 14 条与主题直接或边缘相关、19 条主题错配、1 条已撤稿 [20]），3 个子问题抽取块（q1/q2/q3） ｜ **报告类型**：增量追踪（frontier-watch 七维骨架）

> **证据基础声明（必读）**
> 本轮检索的召回质量严重不足，必须先声明边界，否则任何"SOTA 变动"结论都是虚构。
> 1. **时间窗严重错配**：在"近 1–2 年"（2024-10 至 2026-10）窗口内，本可引用来源中与主题直接相关的只有 2025-05 的 [16] 与 2025-07 的 [8]（后者属人机接口，非运动学/控制）；其余相关条目全部落在 2018–2022 年（[6][11][12][13][14][15][17][19][21][28][31]）。
> 2. **热度证据整体缺失**：全部候选块均未提供 citations / GitHub stars / 下载量 / 榜单排名，因此本报告所有"热度"字段一律写 `> 待核实`，**这不是"0 引用/0 star"**。
> 3. **q1 与 q3 的候选证据集与子问题完全错配**（视频热度预测、天体物理、临床问答、多智能体竞赛等），因此 q1/q3 在方法论上**无法产出任何领域内容**，只能产出缺口清单——本报告如实照此处理，不以外推填补。
> 4. 凡本报告未能用 [n] 支撑的判断，一律标 `> 待核实`；凡属推演，一律显式标 `[P]`。

---

## 1. 进展与热点（Progress & Hotspots）

**一句话增量判断**：本周期内可核查的一手增量仅 **1 条**（2025-05 的受限空间联合抓取-运动规划框架及其 20 场景基准 [16]）；相对"2022 年基线"，运动学求解、MPC/WBC、ros2_control、可微运动学四个方向在本轮证据中**均无增量材料**，属检索缺口而非"领域无变化"。

### 1.1 近 1–2 年（2025）可核查增量

- **[16] A Framework for Joint Grasp and Motion Planning in Confined Spaces（2025-05-12，arXiv:2505.07259v1，cs.RO）**：把抓取与运动规划从"先抓后规划"的两段式，改为受限空间内的联合求解框架，并**自带评测资产**——20 个难度系统性递增的 benchmark 场景、带预计算抓取标注的真实物体、创建/共享更多场景的工具，作者以两个基线规划器验证难度分级确实带来有意义的递进。
  - 热度证据：`> 待核实`（候选块无 citations / 下载量 / 榜单）
  - 权威证据：arXiv 预印本，候选块未标注同行评审 venue [16]
  - 关注度：**中**——依据是候选块给出了可核查的场景数（20）、基线规划器数（2）与数据资产（预计算抓取标注），属"可复现评测要素完整"的少数条目，但无外部采纳信号 [16]
  - 推荐度：**★★★★☆**——本轮信息量最大、基准要素最完整的一篇，对"评测平台/基准"子问题直接可用 [16]
  - 验证状态：**仅论文自述**，第三方复现与真机口径 `> 待核实`
- **[8] LLM-based ambiguity detection in natural language instructions for collaborative surgical robots（2025-07，arXiv:2507.11525v1）**：把 LLM 用于协作手术机器人指令的歧义检测，属"自然语言 → 机器人任务接口"热点。与运动学求解、实时控制、ROS 2 软件栈**无直接关系**，仅作为热点外溢信号记录。
  - 热度证据：`> 待核实`；权威证据：arXiv 预印本 [8]；关注度：**低**（主题偏离本报告主轴）；推荐度：**★★☆☆☆**（仅作语言接口线索）

### 1.2 经典与奠基性工作（2018–2022 基线，非本周期增量）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| IK-Geo: Unified Robot Inverse Kinematics Using Subproblem Decomposition | 2022（v3 修订，据 arXiv ID 2211） | `> 待核实` | `> 待核实` | arXiv 预印本；是否已被期刊/会议接收 `> 待核实` [6] | 低——无引用/榜单数据 [6] | ★★★★☆ 统一 IK 子问题分解路线，是"解析式 IK 求解器"的代表性工程化工作 | http://arxiv.org/abs/2211.05737v3 | 用子问题分解统一多类机械臂 IK；v3 修订说明作者仍在维护，但 2024–2026 是否续更 `> 待核实` [6] |
| SLInKi: State Lattice based Inverse Kinematics — Fast, Accurate, Flexible IK for Soft Continuum Robot Manipulators | 2021 | `> 待核实` | `> 待核实` | **同行评审**：DOI 前缀 10.1109/CASE49439.2021 指向 IEEE CASE 2021 [12] | 低——无引用/榜单数据 [12] | ★★★☆☆ 说明"通用 IK 求解器"之外仍存在本体专用求解器这一并行路线 | https://doi.org/10.1109/case49439.2021.9551686 | 面向软连续体机械臂的 state-lattice IK 求解器，强调速度/精度/灵活性 [12] |
| Evaluating Guiding Spaces for Motion Planning | 2022 | `> 待核实` | `> 待核实` | 据候选块 Comments 字段标注为 **IROS 2022 Workshop** 接收（workshop 级，非主会） [13] | 低——无引用/榜单数据 [13] | ★★★☆☆ 提供"如何评测带引导采样规划质量"的方法论视角 | http://arxiv.org/abs/2210.08640v1 | 提出 motion planning guiding space 统一框架 + 信息论式评估偏置采样质量 [13] |
| Predicted Composite Signed-Distance Fields for Real-Time Motion Planning in Dynamic Environments | 2020 | `> 待核实` | `> 待核实` | arXiv 预印本 [19] | 低——无引用/榜单数据 [19] | ★★★☆☆ 动态环境下实时规划的 SDF 预测路线代表 | http://arxiv.org/abs/2008.00969v2 | 用预测的复合符号距离场支撑动态环境实时规划，是"感知-规划耦合"的早期基线 [19] |
| Data-Efficient Learning of High-Quality Controls for Kinodynamic Planning used in Vehicular Navigation | 2022 | `> 待核实` | `> 待核实` | arXiv 预印本 [17] | 低——无引用/榜单数据 [17] | ★★★☆☆ "学习方法化控制"支线的早期证据，补足纯几何规划之外的监督信号视角 | http://arxiv.org/abs/2201.02254v1 | 数据高效地学习运动动力学规划所需的高质量控制量 [17] |
| Can ROS be used securely in industry? Red teaming ROS-Industrial | 2020 | `> 待核实` | `> 待核实` | arXiv 预印本；正式 venue `> 待核实` [28] | 低——无引用/讨论热度数据 [28] | ★★★★☆ 工业 ROS 安全议题的奠基性一手材料，是判断"6 年后是否解决"的唯一锚点 | http://arxiv.org/abs/2009.08211v1 | 对 ROS-Industrial 做红队测试，系统暴露工业部署下的安全攻击面 [28] |

> 覆盖说明：候选集中 [11]（2018，LabVIEW 电机状态监测与故障诊断）与 [22]（2019，RoboCup SSL 冠军队伍 CUDA 传球射门算法）同属机器人/实时系统边缘相关，但因非 ROS 生态、且与运动学/控制主问题关联弱，未纳入上表，仅作召回完整性记录。

### 1.3 数据集与基准

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Confined-Space Joint Grasp & Motion Planning Benchmarks（20 场景） | 2025 | `> 待核实` | `> 待核实` | 论文作者自建（arXiv 预印本配套），非第三方标准基准 [16] | 中——候选块明确给出场景数（20）、预计算抓取标注与 2 个基线规划器 [16] | ★★★★☆ 唯一同时给出任务数、标注与基线实测的评测资产 | http://arxiv.org/abs/2505.07259v1 | 难度递进的受限空间抓取+规划场景集，附场景创建/共享工具；真机口径与本体范围 `> 待核实` [16] |
| localPlannerBench | 2022 | `> 待核实` | `> 待核实` | arXiv 预印本；官方主页与维护状态 `> 待核实` [15] | 低——无使用度/榜单数据 [15] | ★★★☆☆ 直击"局部规划算法难以公平对比"的痛点，但覆盖范围待核 | http://arxiv.org/abs/2210.06033v1 | 面向局部运动规划算法的统一对比套件，目标是让算法间比较快速无缝 [15] |
| Motion Planning Guiding Space（评估方法论，非数据集） | 2022 | `> 待核实` | `> 待核实` | IROS 2022 Workshop（据候选块 Comments）[13] | 低——无引用数据 [13] | ★★★☆☆ 属评测方法学而非数据集，可作指标设计参考 | http://arxiv.org/abs/2210.08640v1 | 统一带引导采样规划框架 + 信息论评估 [13] |

> **关键缺口**：本报告中**不存在**任何 ROS 2 原生的运动学/控制基准、多本体真机基准或公开榜单。三个评测资产 [13][15][16] 互不衔接、均为作者自建、均无第三方复现记录。

### 1.4 本周期"应出现但无证据"的 SOTA 项（全部 `> 待核实`）

| 方向 | 期望证据类型 | 本轮状态 |
|---|---|---|
| 可微运动学 / 可微刚体动力学 / 学习式 IK-FK 求解器 | 2024–2026 arXiv cs.RO、CoRL/ICRA/RSS 论文 | 零命中 `> 待核实` |
| MPC / WBC 全身控制实时求解性能与新算法 | 论文 + 开源实现 + 实时性基准 | 零命中 `> 待核实` |
| ros2_control / MoveIt 2 / Nav2 的新特性与版本演进 | 官方 release notes、仓库提交记录 | 零命中 `> 待核实` |
| ROS 2 实时性与确定性（DDS QoS、executor、PREEMPT_RT） | 官方文档 + 实测报告 | 零命中 `> 待核实` |

---

## 2. 工业界与产品（Industry & Product）

**一句话增量判断**：本周期**可核查的产业化证据为 0 条**。没有任何厂商产品发布、预训练权重、量产或真机部署材料进入本轮证据集；唯一与"工业落地/工程化"相关的一手材料全部来自 2020–2022 年，且处于"工具发布"而非"规模部署"证据层级。

| 开源项目 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Robowflex | 2021 | `> 待核实` | `> 待核实` | arXiv 预印本；构建于 MoveIt + ROS 之上，非官方文档 [14] | 低——无 star/下载/讨论数据 [14] | ★★★☆☆ 候选证据中唯一的 ROS 生态运动规划封装库，但 ROS 2 兼容性与维护活跃度 `> 待核实` | http://arxiv.org/abs/2103.12826v2 | 为 MoveIt 提供增强 API，单程序内构造与操作规划查询，简化常见用例 [14] |
| Extending the Motion Planning Framework — MoveIt with Advanced Manipulation Functions for Industrial Applications | `> 待核实` | `> 待核实` | `> 待核实` | **SSRN 预印本（10.2139 前缀），非同行评审**，权威性偏低 [21] | `> 待核实`——无使用度数据 [21] | ★★☆☆☆ 主题对口（MoveIt 工业扩展），但证据平台较弱，仅作线索 | https://doi.org/10.2139/ssrn.4251344 | 面向工业应用的 MoveIt 操作功能扩展 [21] |
| Prognostic and Health Management (PHM) tool for ROS | 2020 | `> 待核实` | `> 待核实` | arXiv 预印本 [31] | `> 待核实` | ★★☆☆☆ 属运维/诊断层工具，证明 ROS 生态在"可用性工程"上早有布局，但与运动控制本体关系间接 | http://arxiv.org/abs/2011.09222v1 | 为 ROS 提供的预测与健康管理（PHM）工具 [31] |

- **ROS 1 → ROS 2 迁移完成度**：本轮证据**完全无材料**。ROS 1（Noetic）EOL 的具体日期、各厂商与开源项目（MoveIt 2 / ros2_control / Nav2 / 本体厂商 SDK）的迁移与权重发布现状，`> 待核实`。
- **"从 lab 走向落地"的可核查证据**：**缺**。本轮唯一的 2025 年机器人相关条目 [16] 为单篇 arXiv 预印本，其真机部署与用户采纳情况 `> 待核实`。
- 边缘相关：`[11]` 的电机状态监测/故障诊断（LabVIEW 实现，2018）属"设备级实时监测"思路，与 ROS 2 控制栈无耦合关系，`> 待核实`其是否在 ROS/ROS 2 生态被复用。

---

## 3. 蓝海与缺口（Blue Ocean & Gaps）

**一句话增量判断**：**缺口本身是本次调研最确凿的发现**——"ROS 2 原生 + 多本体 + 可复现榜单"三位一体的评测基础设施在本轮证据中完全缺席，而三个现存评测资产 [13][15][16] 各自为政。

- **缺口 1：ROS 2 原生的运动学/控制基准与公开榜单**。现存资产 [13][15][16] 均为作者自建、无第三方榜单、无 ROS 2 依赖说明，且 [14] 基于 ROS 中间件但 ROS 2 兼容状态 `> 待核实`。四轴：热度 `> 待核实`；权威 `> 待核实`（无官方标准）；关注度 低；推荐度 ★★★★☆（**这正是高杠杆的空白位**）[13][14][15][16]
- **缺口 2：2024–2026 可微运动学 / 学习式 IK-FK 的公开可比结果**。当前唯一可核的 IK 路线证据是 2022 年的子问题分解 [6]（v3 修订说明线仍在维护）与 2021 年的软体专用求解器 [12]，二者之间**没有对比实验**。热度 `> 待核实`；权威 arXiv/IEEE CASE [6][12]；关注度 低；推荐度 ★★★★☆（存在无人区特征）
- **缺口 3：真机与多本体验证口径缺失**。[16] 的 20 场景基准未说明真机/仿真口径、本体自由度与机型范围 [16]；[15] 的算法与场景覆盖 `> 待核实` [15]。关注度 中（对 [16]）；推荐度 ★★★★☆——**"谁先把真机口径填上，谁就定义了可比性"**
- **缺口 4：ROS 2 安全与实时认证的当代证据真空**。唯一锚点是 2020 年的 ROS-Industrial 红队研究 [28]；此后 6 年多的进展（标准映射、认证路径、DDS 供应商锁定与供应链风险）**零证据** `> 待核实`。关注度 低（无热搜/榜单信号）；推荐度 ★★★★★（**这是工业规模化的硬门槛，且证据真空本身就是信号**）[28]
- **缺口 5：评测方法论与工具链脱节**。[13] 提供"引导空间质量"的信息论评估视角，[15] 提供局部规划对比套件，但二者未与 [16] 的场景资产或 ROS 2 工具链打通 [13][15][16]。关注度 低；推荐度 ★★★☆☆
- `[P]` **高杠杆机会（预判，置信度：低）**：依据"三个评测资产互不衔接 + 无第三方榜单"这一可观测现状，推演结论为——**未来 12–18 个月，最先被社区采纳的不会是又一个新规划器，而是把现有场景资产接入 ROS 2 可复现流水线的评测层**。可证伪条件见第 7 节 P1。

---

## 4. 瓶颈与拐点（Bottleneck & Inflection）

**一句话增量判断**：本周期**不能断言存在拐点**；能确认的是三类瓶颈，其中"证据链断层"使拐点判断在方法上不可完成。

- **瓶颈 A：评测碎片化 + 无榜单**。[13][15][16] 三个资产使用不同口径、不同任务定义、无共享榜单；全部热度信号 `> 待核实`，即**无法证明其中任何一个被社区广泛采用**。关注度 中；推荐度 ★★★★☆ [13][15][16]
- **瓶颈 B：证据链断层（2018→2022→2025 跳跃）**。本轮相关材料密集在 2020–2022（[13][14][15][17][19][21][28][31]），2023–2024 **完全空白**，2025 仅 [16]。这是**检索/公开性瓶颈**，不等于领域停滞；但在当前证据下，任何"2024–2026 发生了什么变化"的强断言都不成立 `> 待核实`。
- **瓶颈 C：工业合规证据停留在 ROS 1 时代**。[28] 是 2020 年的 ROS-Industrial 红队研究；关于其时是否已催生后续标准或修复，本报告无证据 `> 待核实`。关注度 低；推荐度 ★★★★★（硬门槛）[28]
- **瓶颈 D：本体专用 vs 通用求解器的取舍**。[6] 走统一子问题分解，[12] 走软连续体专用 state-lattice——两条路线并存 5 年，缺乏统一的精度/速度对比口径 [6][12]。关注度 低；推荐度 ★★★☆☆
- **拐点信号清单（可观测、但本轮无法给出取值）**：
  1. ros2_control / MoveIt 2 官方仓库的 release 节奏与提交活跃度 `> 待核实`
  2. 是否出现 ≥2 个独立团队共同引用的 ROS 2 原生评测榜单 `> 待核实`
  3. 是否出现 ROS 2 与功能安全标准的官方映射文档 `> 待核实`
  4. 是否有论文把真机口径（本体型号/自由度/任务数）作为必填项 `> 待核实`
- **结论**：拐点判断**证据不足**；本次记为"待观察"，不记"已发生"。

---

## 5. 社会·政策·国际（Society, Policy & Geopolitics）

**一句话增量判断**：本维度**零命中**——没有任何监管、标准、地缘政治、供应链或伦理材料进入本轮证据集。

- **监管与标准**：ISO 10218 / ISO/TS 15066 / IEC 61508 / ISO 13849 等在 ROS 2 上的落地路径 `> 待核实`；本轮唯一相关锚点是 2020 年针对 ROS-Industrial 的安全红队研究 [28]，说明"ROS 用于工业安全吗"这一问题**至少在 2020 年已被系统提出**，但 2024–2026 的政策/标准状态无证据。权威：arXiv 预印本 [28]；关注度 低；推荐度 ★★★★☆
- **治理指标化的跨领域外溢（弱信号）**：[5] 2025 年版 Foundation Model Transparency Index（第三版）新增与数据获取相关的透明度指标，反映"对基础模型开发者透明度进行量化评级"的治理范式在持续演进 [5]。但该工作是**基础模型治理**，**不可外推**为机器人控制栈的监管趋势。权威：arXiv 预印本（cs.AI）[5]；热度 `> 待核实`；关注度 低（偏离主轴）；推荐度 ★★☆☆☆
- **地缘政治 / 供应链 / 出口管制 / 劳动影响**：本轮**无任何证据**，全部 `> 待核实`。按方法论要求，此维度写"本周期无可核查变化"，**不**写"无变化"。
- 提示：`[20]`（arXiv:cond-mat/0309395v2）标注为"This paper has been withdrawn"，属不可用来源，已丢弃。

---

## 6. 资本与生态（Capital & Ecosystem）

**一句话增量判断**：本维度**零命中**——无融资、并购、人才流动或公司格局材料；生态侧只能从工具条目的**时间分布**读出间接信号，且该信号本身受检索偏差污染。

- **投资 / 并购 / 人才**：`> 待核实`（零证据，不推测）。
- **生态工具的时间分布（可核查的间接信号）**：相关开源/工程条目集中于 2020–2022（[14] 2021 MoveIt 封装库、[21] MoveIt 工业扩展、[31] 2020 ROS PHM 工具、[28] 2020 ROS 安全红队），2025 年仅 [16] 一篇单组预印本。**可核事实是"本轮证据中没有 2023–2026 的新工具链条目"**，但这是召回质量问题，**不能**据此宣称生态降温 `> 待核实`。四轴：热度 `> 待核实`；权威 arXiv/SSRN（[21] 非同行评审）[14][21][31]；关注度 低；推荐度 ★★★☆☆（[14]）/★★☆☆☆（[21][31]）
- **社区与榜单**：无任何 star、下载、榜单排名数据进入本轮证据 `> 待核实`。
- **结论**：本维度按方法论写作"**本周期无可核查证据**"，而非"本周期无显著变化"。

---

## 7. 信号与预测（Signals & Forecast）

**一句话增量判断**：可确认的早期信号仅 3 条，且都指向"评测资产自建化"与"求解器长期维护化"两个慢变量，而非爆发式变化。

### 7.1 早期信号（可核查）

- **S1（2025-05）**：新工作倾向于**自带基准与基线**发布——[16] 一次性给出 20 个难度递进场景 + 预计算抓取标注 + 2 个基线规划器 + 场景共享工具。这可能反映"评测资产已是论文竞争力的一部分"，但也可能只是单篇案例 `> 待核实`。[16]
- **S2（2022–）**：解析式 IK 求解器仍在**持续修订**——[6] 已迭代至 v3，说明子问题分解路线未被视为已终结问题。[6]
- **S3（2021）**：本体专用 IK 求解器与通用求解器**并行演进**——[12] 为软连续体机械臂单独设计 state-lattice IK，说明通用求解器未必覆盖软体/连续体本体。[12]

### 7.2 预判 `[P]`（均为可证伪假设，依据链：现状 → 推演 → 结论）

- **P1（评测收敛）**：依据"三个评测资产 [13][15][16] 各自为政且全部缺第三方榜单"这一现状，推演"社区需要统一口径但尚无供给"，结论为——**若到 2027-06 出现被 ≥2 个独立团队（非原作者）引用的 ROS 2 原生运动学/控制评测榜单，则"评测碎片化正在收敛"成立；否则不成立**。置信度：**低**（依据仅 3 条自建资产，样本过小）。
- **P2（合规拐点）**：依据"唯一工业安全证据是 2020 年的 ROS-Industrial 红队研究 [28]，其后无证据"，推演"若工业规模化真在发生，合规文档应随之出现"，结论为——**若 2026-10 至 2027-12 之间出现 ros2_control 或 ROS 2 官方/半官方的实时性与功能安全（IEC 61508 / ISO 13849 类）映射文档或认证案例，则"工业级 ROS 2 控制栈合规拐点"成立；否则该拐点尚未到来**。置信度：**低**（本轮无 2023 年后合规证据，无法判断是"已解决但未检索到"还是"未解决"）。
- **P3（学习式运动学落地）**：依据"本轮 2024–2026 窗口内**零**可微运动学/学习式 IK 证据，而工作区之外的基线 [6][12] 均为解析/几何法"，结论为——**若到 2027-06 仍无可微运动学方法在公开真机基准上超过并行解析求解器，则"学习方法尚未取代解析 IK 在实时控制中的地位"成立**。置信度：**低**，且**高度可能是检索缺口所致**，不作为结论使用。

### 7.3 争议与传闻

- `[Debated]`：本轮证据量不足以形成任何可陈述的学术争议（不存在两方独立来源的冲突材料）。
- `[R]`：无（不记录未证实传闻）。

### 7.4 Watchlist 与下一轮检索式

| 观察对象 | 观察指标 | 建议检索式 |
|---|---|---|
| ros2_control / MoveIt 2 | release 与 commit 活跃度、官方文档新增章节 | `site:github.com ros2_control releases 2025..2026`、`ros2_control real-time determinism docs` |
| 可微运动学 / 学习式 IK | 新论文 + 真机对比 | `site:arxiv.org differentiable kinematics IK 2025..2026`、`learning inverse kinematics real robot benchmark` |
| MPC / WBC | 实时求解频率与开源实现 | `whole-body control MPC real-time 2025..2026 site:arxiv.org` |
| 评测榜单 | 第三方复现与榜单 | `simpler env libero benchmark leaderboard 2025..2026`、`motion planning benchmark leaderboard ros2` |
| 安全与合规 | 标准映射文档 | `ROS 2 functional safety IEC 61508 certification 2025..2026`、`ISO 10218 ROS 2` |
| ROS 1 EOL 迁移 | 迁移完成度报告 | `ROS 1 Noetic EOL migration status 2025..2026`、`ROS 2 migration survey robotics companies` |

**Watchlist 判定标准（延续 P1）**：是否出现**非原作者团队**引用的 ROS 2 原生基准/榜单 —— 这是本报告认为最值得盯的单一指标。

---

## 参考来源

**本报告实际引用**

- [5] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1
- [6] IK-Geo: Unified Robot Inverse Kinematics Using Subproblem Decomposition — http://arxiv.org/abs/2211.05737v3
- [8] LLM-based ambiguity detection in natural language instructions for collaborative surgical robots — http://arxiv.org/abs/2507.11525v1
- [11] Real time state monitoring and fault diagnosis system for motor based on LabVIEW — http://arxiv.org/abs/1806.09998v1
- [12] SLInKi: State Lattice based Inverse Kinematics - A Fast, Accurate, and Flexible IK Solver for Soft Continuum Robot Manipulators — https://doi.org/10.1109/case49439.2021.9551686
- [13] Evaluating Guiding Spaces for Motion Planning — http://arxiv.org/abs/2210.08640v1
- [14] Robowflex: Robot Motion Planning with MoveIt Made Easy — http://arxiv.org/abs/2103.12826v2
- [15] Local Planner Bench: Benchmarking for Local Motion Planning — http://arxiv.org/abs/2210.06033v1
- [16] A Framework for Joint Grasp and Motion Planning in Confined Spaces — http://arxiv.org/abs/2505.07259v1
- [17] Data-Efficient Learning of High-Quality Controls for Kinodynamic Planning used in Vehicular Navigation — http://arxiv.org/abs/2201.02254v1
- [19] Predicted Composite Signed-Distance Fields for Real-Time Motion Planning in Dynamic Environments — http://arxiv.org/abs/2008.00969v2
- [20] This paper has been withdrawn（不可用来源，已丢弃）— http://arxiv.org/abs/cond-mat/0309395v2
- [21] Extending the Motion Planning Framework—Moveit with Advanced Manipulation Functions for Industrial Applications — https://doi.org/10.2139/ssrn.4251344
- [22] Champion Team Paper: Dynamic Passing-Shooting Algorithm Based on CUDA of The RoboCup SSL 2019 Champion — http://arxiv.org/abs/1909.07717v1
- [28] Can ROS be used securely in industry? Red teaming ROS-Industrial — http://arxiv.org/abs/2009.08211v1
- [31] Prognostic and Health Management (PHM) tool for Robot Operating System (ROS) — http://arxiv.org/abs/2011.09222v1

**本轮未采用候选（主题错配，仅作召回质量记录，未用于任何论断）**

- 视觉/视频与图像挑战赛类：[1] VQualA 2025 短视频互动度预测、[2] NTIRE 2025 图像超分
- 天体物理与数学类：[3] TDCOSMO 2025、[7] PINOCCHIO 暗物质晕、[27] LaFeAsO 磁相互作用、[29] 3C309.1、[32] AGN Jets 运动学、[33] 相位延迟天体测量、[34] LIFE 干涉仪
- NLP / 评测 / 治理类：[9] 德语开放问卷编码、[10] 车联网边缘计算、[18] ELOQUENT 2025 Sensemaking
- 人机交互与工程管理类：[4] TRUST 2025（HRI 信任，cs.RO 但非本主题）
- 2026 年其他竞赛/应用类：[23] ArchEHR-QA 2026、[24] MOASEI 2026、[25] AutoRestTest SBFT 2026、[26] CHiPSAL 2026
- 其他：[30] Jayne–Rogers 定理注记

> **报告自评（覆盖检查）**：✅ 最新进展与经典工作已分节；✅ 三类必填表格（经典/开源/基准）已给出；✅ 四类证据轴已逐条标注，缺失处统一写 `待核实`；✅ 七维章节全部完成。❌ **未达成**：无法回答"2024–2026 年 ros2_control / MPC-WBC / 可微运动学的真实 SOTA 变动"，原因是本轮召回集与子问题错配 → 建议以第 7.4 节检索式重跑一轮后再出增量结论。

---

*Generated by research-bot · topic=`机器人运动学控制与-ros-2` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`deepseek-v4-flash` · sources=34 · duration=227s · 2026-10-14T22:25:22+00:00*
