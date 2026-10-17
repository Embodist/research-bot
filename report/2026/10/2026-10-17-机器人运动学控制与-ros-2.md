# 机器人运动学、控制与 ROS 2：七维增量追踪报告

**日期**：2026-10-17 ｜ **领域**：机器人运动学（kinematics）、控制（control）、ROS 2 工程栈 ｜ **检索源数量**：36 条候选来源（其中与本主题直接相关约 12 条）

> **证据基线与阅读约定**：本批 36 条候选中混入大量与主题无关的记录（粒子物理 hep-ex [3][5]、医学问答 [9]、图像超分 [26]、短视频/法律问答竞赛 [25][28] 等），有效证据以 arXiv 预印本为主，**没有任何机器人评测榜单或数据集一手来源**。因此本报告不给出任何"SOTA 已被刷新"的结论；凡涉及引用数、GitHub star、下载量、榜单排名而候选块未提供者，一律标注 `> 待核实` 并保持原编号引用。标记约定：`[R]` 传闻/未证实，`[P]` 预测，`[Debated]` 争议。

---

## 1. 进展与热点（Progress & Hotspots）

**增量判断**：相对"ROS 2 已替换 ROS 1"这一旧基线，本周期真正的增量不在中间件替换，而在两处：① **经典动力学/运动学算法被重新推导**以适配闭链、约束嵌入与实时约束求解 [16][24]；② **ROS 2 控制层出现"参考生成 / 控制律 / 柔顺接口"的解耦尝试** [29][31]。但关键条目全部为预印本或单篇会议论文，**尚无可核查的 SOTA 榜单**，任何"最优/最强"表述均不成立。

### 1.1 最新进展（2024–2026）

- **线性时间微分逆运动学（2024，RSS）**：[24] 以增广拉格朗日（Augmented Lagrangian）视角处理微分 IK，标题即宣称 linear-time。增量在于把约束 IK 从"逐迭代伪逆"路线转向可在线求解的优化视角；具体复杂度、约束类型（关节限位/任务优先级）与真机验证需读全文核实。**热度**：`> 待核实`（候选块未提供引用数）；**权威**：RSS 2024，同行评审（DOI 10.15607/rss.2024.xx.110）[24]；**关注度**：中 —— 依据为 RSS 主会 venue 与主题核心度，非量化热度；**推荐度**：★★★★☆ —— 运动学方向最值得精读的一篇，但数字须以原文表格为准。
- **闭链/约束嵌入模型的动力学导数（2026-09，预印本）**：[16] 明确指出既有高效导数算法"assume joint velocity effects are locally configuration invariant"，该假设在约束嵌入闭链下不成立，并移除该假设。[16] 是本批证据中**唯一直接推进"经典刚体动力学算法 → 更真实机构模型"的工作**。**热度**：`> 待核实`；**权威**：arXiv cs.RO 预印本，未见同行评审 [16]；**关注度**：低 —— 2026-09 新预印本，无引用/讨论信号；**推荐度**：★★★☆☆ —— 主题相关性高，但须读全文并等待评审。
- **ROS 2 参考生成与控制律解耦（2026-01，预印本）**：[29] 把参考的获取、校验、插值从跟踪该参考的控制律中分离，设计 Reference Generator 组件从规划器等外部节点接收单点/轨迹参考。**热度**：`> 待核实`；**权威**：arXiv 预印本，未见 venue [29]；**关注度**：低；**推荐度**：★★★☆☆ —— 直击 ros2_control "换本体要重写"的痛点，但仍是架构提案。
- **面向学习型策略的柔顺 ROS 2 控制器 CRISP（2025-09，v2）**：[31] 指出扩散策略/VLA 常产生低频或不连续的状态变化，需要低层控制器把高层目标转为关节力矩；自述为轻量 C++ 实现。这是"VLA → 实时控制"链路上少见的明确工程接口工作。**热度**：`> 待核实`（已更新至 v2，可视为弱活跃信号）；**权威**：arXiv 预印本 [31]；**关注度**：中 —— 主题正对 VLA 落地热点，但无 star/引用数据；**推荐度**：★★★★☆ —— 与"学习策略接入 ROS 2"高度相关，代码与许可 `> 待核实`。
- **多机械臂实时 ROS 2 与 sim-to-real（2026-02，v2）**：[36] 以 multipanda_ros2 为名给出面向多机械臂系统的实时 ROS 2 框架，标题即指向 sim-to-real gap。**热度**：`> 待核实`；**权威**：预印本 [36]；**关注度**：低–中；**推荐度**：★★★☆☆。
- **连接性与工具链外延**：ROS 2 over WAN 方案 [32]（2026-08）、云机器人平台 FogROS2-SGC [33]（2023）、ROS 2 自动驾驶系统性能评估 [34]（2024-11，v3）、LLM 辅助理解 ROS 2 软件架构 [35]（2026-04）。这组条目说明 ROS 2 的研究重心正从"通信可用"转向"跨网/跨机/可维护" [32][33][35]，但均非运动学或控制算法本身。
- **水下多体系统动力学仿真**：[20] 以 Julia 实现 Fossen 与 Featherstone 的融合并做实验验证，属"经典动力学形式在具体平台上被工程化"的一类进展，OCEANS 2024 同行评审。**热度**：`> 待核实`；**权威**：IEEE OCEANS 2024 [20]；**关注度**：低；**推荐度**：★★★☆☆。

> **证据缺口提示**：本批证据**不存在**任何 ROS 2 发行版 release note、MoveIt 2 / ros2_control 官方文档或榜单数据，因此"2024–2026 年 SOTA 如何变化"这一问题**在本批证据下不可回答** `> 待核实`。

### 1.2 经典与奠基性工作

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Forward Dynamics, Elimination Methods, and Formulation Stiffness in Robot Simulation | 1997 | IJRR（作者 `> 待核实`） | citations=54 [23] | IJRR 同行评审，DOI 10.1177/027836499701600603 [23] | 中 —— 54 次引用，动力学/仿真领域常被引但非当下热点 [23] | ★★★★☆ —— 解释"为何步长与稳定性受限"的原始依据 | https://doi.org/10.1177/027836499701600603 | 指出前向动力学与数值积分耦合产生"公式刚性（formulation stiffness）"，二者不应被当作独立问题 [23] |
| Comparative Study on Serial and Parallel Forward Dynamics Algorithms for Kinematic Chains | 2009（依 DOI，`> 待核实`） | IJRR（作者 `> 待核实`） | `> 待核实`（候选块未提供引用数）[22] | IJRR 同行评审，DOI 10.1177/0278364909102350 [22] | `> 待核实` | ★★★☆☆ —— 算法选型的对照基准，但元数据缺失较多 | https://doi.org/10.1177/0278364909102350 | 串联 vs 并联前向动力学算法的比较研究；结论口径需读原文 [22] |
| A ROS2 based communication architecture for control in collaborative and intelligent automation systems | 2019 | `> 待核实`（arXiv 1905.09654） | `> 待核实` [30] | arXiv 预印本 [30] | `> 待核实` | ★★★☆☆ —— ROS 2 早期控制架构文献，宜作历史基线 | http://arxiv.org/abs/1905.09654v1 | ROS 2 用于协作/智能自动化控制通信架构的早期工作 [30] |
| Robotic Arm Control System based on ROS and MoveIt: A Practical Educational Approach | 2025 | IEEE WAIE 2025（作者 `> 待核实`） | citations=0 [11] | IEEE workshop，同行评审，非机器人主会 [11] | 低 —— 零引用 + 教育类 venue [11] | ★★☆☆☆ —— 仅作 ROS+MoveIt 教学案例，不能支撑 SOTA | https://doi.org/10.1109/waie67422.2025.11381096 | 明确写 "ROS and MoveIt"，无 ROS 2/DDS/ros2_control 关键词，系统指标不可见 [11] |

**注**：[22][23] 的作者与机构信息在候选块中缺失，按引用纪律标注 `> 待核实`，不作推断。

---

## 2. 工业界与产品（Industry & Product）

**增量判断**：本批证据**没有任何厂商产品发布、量产、官方技术报告或版本 release 说明**；所谓"工业界"信号全部是学术侧的可复用组件与框架，因此本章只能给出"工程栈层面的落地候选"，不能给出产品化结论。

- **落地候选一：学习策略的低层力矩接口**。CRISP 以轻量 C++ 柔顺控制器形式，试图填补"扩散策略/VLA 输出 → 关节力矩"的空白 [31]，对应真机部署中最高频的工程断点。但其代码仓库、开源许可、依赖的 ROS 2 发行版、控制频率与力矩跟踪误差在候选证据中均未出现 `> 待核实` [31]。
- **落地候选二：多本体/多机械臂复用**。Reference Generator 的模块化思路 [29] 与 multipanda_ros2 的实时多机械臂框架 [36] 分别从"控制层解耦"和"系统集成"两侧回应同一需求；两者均无第三方复现或采用度数据 `> 待核实`。
- **间接采用信号**：ROS 2 已被放入自动驾驶系统的性能评估语境 [34]，并被用于广域/云侧连接 [32][33]，说明其工程边界在扩展；但这些证据不涉及机械臂运动学或控制性能。
- **硬件侧生态信号**：[2] ALOHA 2 作为增强型低成本双臂遥操作硬件，代表"低成本 + 可复制硬件"的路线；其是否随论文开源、是否提供 ROS 2 驱动 `> 待核实` [2]。

**明确排除**：本批证据**不含** MoveIt 2、Pinocchio、Isaac Lab、MuJoCo 的任何一手来源（无官方文档、无仓库、无 release note），相关"工程实践现状"一律 `> 待核实`。

### 2.2 开源项目（本批证据涉及的可复用实现）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| CRISP — Compliant ROS2 Controllers | 2025（v2） | `> 待核实`（arXiv 2509.06819） | `> 待核实`（无 star/引用数据）[31] | 学术预印本配套实现，非官方 ros2_control 组件 [31] | 中 —— 对应 VLA/扩散策略部署热点，但无量化信号 [31] | ★★★★☆ —— 若代码开放，是"VLA→力矩"最直接的可试实现 | http://arxiv.org/abs/2509.06819v2 | 自述轻量 C++ 柔顺控制器；仓库地址、许可、实时性指标均 `> 待核实` [31] |
| multipanda_ros2 | 2026（v2） | `> 待核实`（arXiv 2602.02269） | `> 待核实` [36] | 预印本框架 [36] | 低–中 —— 新预印本 [36] | ★★★☆☆ —— 多机械臂实时集成的参考架构 | http://arxiv.org/abs/2602.02269v2 | 面向多机械臂系统的实时 ROS 2 框架，主打 sim-to-real [36] |
| Reference Generator（ROS 2 模块化架构提案） | 2026 | `> 待核实`（arXiv 2601.08514） | `> 待核实` [29] | 预印本，架构提案 [29] | 低 [29] | ★★★☆☆ —— 控制层解耦的设计参考，非成熟组件 | http://arxiv.org/abs/2601.08514v3 | 参考获取/校验/插值从控制律中分离 [29] |
| FogROS2-SGC | 2023 | `> 待核实`（arXiv 2306.17157） | `> 待核实` [33] | 预印本 [33] | `> 待核实` | ★★★☆☆ —— 云/跨网 ROS 2 部署参考 | http://arxiv.org/abs/2306.17157v1 | ROS 2 云机器人平台，主打安全全局连接 [33] |
| ALOHA 2 | 2024 | `> 待核实`（arXiv 2405.02292） | `> 待核实` [2] | 预印本（硬件平台论文）[2] | `> 待核实` | ★★★☆☆ —— 低成本双臂遥操作的硬件基线 | http://arxiv.org/abs/2405.02292v1 | 增强型低成本双臂遥操作硬件；开源程度 `> 待核实` [2] |

> 说明：表中"热度"列全部为 `> 待核实`，因为候选块未提供任何 GitHub star、下载量或引用数字；**不得**据此表判断项目流行度。

---

## 3. 蓝海与缺口（Blue Ocean & Gaps）

**增量判断**：本批证据暴露出的最大无人区不是"再提一个新控制器"，而是**"实时性约束下的闭链动力学"与"学习策略到 ROS 2 实时层"这两段接口没有标准、没有基准、没有第三方复现** [16][29][31]。

1. **闭链/约束嵌入动力学的实时性空白**：现有高效导数算法依赖的假设在闭链下失效，而推广后的附加项"仅在只建模驱动运动学时代价低，更完整建模下代价可能上升"——具体阈值与量级在候选摘要中被截断 `> 待核实` [16]。这意味着"精度 vs 实时"的边界尚无人给出可复用的定量结论。
2. **控制层解耦缺少性能证据**：Reference Generator 在多本体、多规划器下的开销与实时性未量化 `> 待核实` [29]。
3. **学习策略 → 低层力矩的接口无标准**：CRISP 是单点尝试，缺少与 ros2_control 官方接口的对接规范与跨本体验证 `> 待核实` [31]。
4. **ROS 2 性能评估碎片化**：现有评估多绑定特定系统（如自动驾驶 [34]）或特定连接场景（广域 [32]、云 [33]），缺少跨 DDS 实现、跨发行版的系统对比 `> 待核实`。
5. **ROS 2 架构知识工程**：LLM 辅助理解 ROS 2 软件架构 [35] 提示"架构可读性/知识传承"是新兴缺口，但该工作本身无量化评测数据 `> 待核实`。
6. **完全缺失的一手生态证据**：MoveIt 2、Pinocchio、Isaac Lab、MuJoCo 在本批证据中零覆盖，其可复现性现状无法评估 `> 待核实`。

### 3.2 数据集与基准

> **重要**：本批 36 条证据中**没有任何一条**是机器人数据集、基准榜单或复现报告。下表仅列出该主题后续必须核查的对象，其全部元数据与链接均为 `> 待核实`，**不得**在正式报告中作为已核实事实引用。

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| LIBERO（操作策略基准） | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实`（本批未检索） | 本批证据零覆盖，需补检官方主页与榜单 |
| SimplerEnv（仿真评测） | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实`（本批未检索） | 同上；用于判断仿真 SOTA 与真机差距 |
| RoboArena（真机/众包评测） | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实`（本批未检索） | 同上 |
| Open X-Embodiment（跨本体数据） | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实`（本批未检索） | 同上 |
| DROID（大规模真机操作数据） | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实`（本批未检索） | 同上 |

**结论**：在补齐上述一手来源之前，"仿真 SOTA 与真机可用性的差距"这一问题**不可判定** `> 待核实`。

---

## 4. 瓶颈与拐点（Bottleneck & Inflection）

**增量判断**：瓶颈没有变——仍是**数值刚性、实时性、接口碎片化、可复现性**四件事；但本周期出现了三类"可能构成拐点"的信号：闭链模型被重新纳入实时算法视野 [16]、控制层开始被显式解耦 [29]、学习策略开始要求低层力矩接口 [31]。

- **数值刚性（长期瓶颈）**：前向动力学与数值积分的耦合会产生 formulation stiffness，直接约束仿真步长与稳定性 [23]；2026 年的闭链导数工作说明这一耦合在更真实机构模型下**更严重而非更轻** [16]。
- **精度 vs 实时（未消解的权衡）**：附加项在"仅建模驱动运动学"时代价低、在更完整建模下可能升高 [16]；该结论为作者自评，无第三方复现 `> 待核实`。
- **接口碎片化（工程瓶颈）**：参考生成与控制律耦合导致换本体需重写 [29]；学习策略输出低频/不连续导致需额外柔顺层 [31]。两者是同一问题的两端。
- **可复现性瓶颈**：关键条目 [16][29][31][36] 全为预印本，候选块未提供引用数，亦无第三方复现或榜单记录 `> 待核实`。
- **评测瓶颈**：无任何基准数据（见 3.2），导致"方法优劣"无法横向比较。
- **人的瓶颈**：ROS 2 架构理解成本被单独作为研究问题提出 [35]，说明工程门槛已成为采用阻力的一部分。

**拐点信号（可观测）**：① ros2_control / MoveIt 2 官方文档出现独立的 reference-generation 接口；② 柔顺控制器类组件被主流 ROS 2 仓库引用；③ 闭链动力学导数给出 <1 ms 级实时性实测。三条目前**均未观测到** `> 待核实`。

---

## 5. 社会·政策·国际（Society, Policy & Geopolitics）

**增量判断**：本周期在本批证据下**无显著变化**。没有任何监管、标准、出口管制、供应链或劳动影响的直接证据，以下仅为边缘信号，且关联度弱。

- **AI 治理的邻近信号**：[27] 2025 年基础模型透明度指数（FMTI）评估厂商在数据、算力等维度的透明度披露。该工作**不属于机器人领域**，仅可作为"AI 透明度治理"这一外部制度环境的旁证，不能推断机器人监管走向 [27] `> 待核实`。
- **工程教育与人才供给**：ROS + MoveIt 被作为教学型系统写入教育类 workshop 论文 [11]，说明该栈已进入课程层面；但其对人才供给的实际影响无数据 `> 待核实` [11]。
- **知识传承与软件可维护性**：LLM 辅助理解 ROS 2 架构 [35] 触及"复杂机器人软件的可读性与人员交接"这一组织性问题，属工程社会学层面的弱信号 `> 待核实`。
- **国际/地缘/供应链**：本批证据**完全未覆盖**，不得作任何推断 `> 待核实`。

---

## 6. 资本与生态（Capital & Ecosystem）

**增量判断**：本批证据**无任何融资、并购、人才流动或公司格局数据**；可观测的只有"开源生态的结构性位移"——从通信中间件，走向连接性、多机械臂与学习策略接口。

- **生态位移线**：2019 年 ROS 2 的控制通信架构 [30] → 2023 年云侧全局连接 [33] → 2026 年广域连接方案 [32] → 2026 年多机械臂实时框架 [36]。这条线显示社区关注点从"能不能通信"转向"跨网/多机/实时" [30][33][32][36]。
- **控制层组件化**：Reference Generator [29] 与 CRISP [31] 代表"把控制器拆成可复用组件"的尝试，是生态从"整机方案"转向"可插拔模块"的早期信号；但两者均未见维护机构与许可信息 `> 待核实`。
- **硬件成本线**：ALOHA 2 [2] 代表低成本双臂硬件路线，若其硬件设计与驱动开放，可能降低双臂研究的进入成本；开源程度 `> 待核实` [2]。
- **资本侧**：`> 待核实`（本批证据零覆盖，不作推测）。

---

## 7. 信号与预测（Signals & Forecast）

**增量判断**：可观测信号集中在"控制层解耦"与"学习策略下沉"两条线；两者都还没有跨过"预印本 → 被采纳"的门槛，因此以下预测置信度整体偏低，全部写成可证伪假设。

**早期信号**

- **S1 控制层解耦**：2026-01 出现把参考生成从控制律中剥离的 ROS 2 架构提案 [29]。
- **S2 学习策略下沉**：2025-09 出现专门把 VLA/扩散策略低频输出转成关节力矩的柔顺控制器，并已修订至 v2 [31]。
- **S3 闭链动力学回潮**：2026-09 有工作移除"关节速度效应局部构型不变"假设以适配约束嵌入闭链 [16]，暗示并联/闭链机构（如并联踝、四连杆膝关节）的实时控制需求上升 `[P]`。
- **S4 连接性外延**：ROS 2 over WAN [32] 与云机器人 [33] 并置，说明部署边界在扩展。
- **S5 工具链智能化**：LLM 被用于辅助理解 ROS 2 架构 [35]，属工程效率侧的新信号。

**可证伪预测**

- **P1（置信度：中低）**：若到 2027-06 前，ros2_control 或 MoveIt 2 的官方文档/发行说明中出现独立的"reference generator"或等价解耦接口，则"控制层解耦成为主流设计"成立；否则该判断证伪。依据链：S1 提案 [29] → 社区痛点（换本体重写）→ 官方采纳。`[P]`
- **P2（置信度：低）**：若 CRISP 类柔顺控制器在 2027 年前获得可观测的生态采用（被 ROS 2 生态仓库引用或出现在发行版示例中），则"VLA/扩散策略 → ROS 2 低层力矩接口"开始标准化；否则仍停留在论文级尝试。依据：S2 [31]。`[P]`
- **P3（置信度：中）**：若闭链动力学导数工作在 2027 年前给出完整建模下仍满足实时控制频率（如百 Hz 级以上）的实测数据，则闭链实时控制进入可用阶段；若只能离线运行，则该方向仍属理论推进。依据：S3 [16]。`[P]`
- **P4（置信度：中）**：若到 2027 年仍无第三方复现或基准榜单覆盖上述 ROS 2 控制组件，则"可复现性"将继续是采用的主要阻力。依据：本批关键条目全为预印本且无引用数据 [16][29][31][36]。`[P]`

**不确定性说明**：本批 36 条候选中主题相关者约 12 条，噪声率约 2/3（含 hep-ex [3][5]、医学问答 [9]、图像超分 [26]、视频/法律问答竞赛 [25][28]），说明当前查询词召回精度不足；上述预测均建立在**未经验证的预印本**之上，须在补齐官方文档与基准数据后重新评估 `> 待核实`。

**Watchlist（持续关注）**

1. ros2_control / MoveIt 2 官方接口与发行说明（本批未覆盖 `> 待核实`）
2. CRISP 代码仓库、许可与实时性指标 [31]
3. multipanda_ros2 的多机械臂实测数据 [36]
4. 闭链/约束嵌入动力学导数的实时性实测 [16]
5. ROS 2 跨网与云侧部署的性能对比 [32][33]
6. 机器人操作基准榜单（LIBERO / SimplerEnv / RoboArena / Open X-Embodiment / DROID，本批均未检索 `> 待核实`）

---

## 参考来源

[1] Two-dimensional magnetic interactions in LaFeAsO — http://arxiv.org/abs/1303.4033v1
[2] ALOHA 2: An Enhanced Low-Cost Hardware for Bimanual Teleoperation — http://arxiv.org/abs/2405.02292v1
[3] Observation of Atmospheric Neutrino Oscillations in Soudan 2 — http://arxiv.org/abs/hep-ex/0307069v1
[4] Search for the Proton Decay Mode proton to neutrino K+ in Soudan 2 — http://arxiv.org/abs/hep-ex/9803030v1
[5] Search for nucleon decay into lepton + K0 final states using Soudan 2 — http://arxiv.org/abs/hep-ex/9910026v2
[6] A Study of Cosmic Ray Composition in the Knee Region using Multiple Muon Events in the Soudan 2 Detector — http://arxiv.org/abs/hep-ex/9612004v2
[7] The Atmospheric Neutrino Flavor Ratio from a 3.9 Fiducial Kiloton-Year Exposure of Soudan 2 — http://arxiv.org/abs/hep-ex/9901024v1
[8] The Observation of a Shadow of the Moon in the Underground muon flux in the Soudan 2 detector — http://arxiv.org/abs/hep-ex/9905036v1
[9] UIC-AIHealth4All at ArchEHR-QA 2026: Answer-First Evidence Grounding for Clinical Question Answering — http://arxiv.org/abs/2608.27467v1
[10] ZeroR@CHiPSAL 2026: Two-Stage Vision-Language Adaptation with Contrastive Learning for Nepali Meme Classification — http://arxiv.org/abs/2607.28637v1
[11] Robotic Arm Control System based on ROS and MoveIt: A Practical Educational Approach — https://doi.org/10.1109/waie67422.2025.11381096
[12] AutoRestTest at the SBFT 2026 Tool Competition — http://arxiv.org/abs/2607.01063v1
[13] The Relativistic Elasticity of Rigid Bodies — http://arxiv.org/abs/physics/0307019v3
[14] On the invariant motions of rigid body rotation over the fixed point, via Euler angles — http://arxiv.org/abs/1601.04526v1
[15] A Parametric and Feasibility Study for Data Sampling of the Dynamic Mode Decomposition--Range, Resolution, and Universal Convergence States — http://arxiv.org/abs/2110.06573v2
[16] Adapting Rigid-Body Dynamics Derivatives for Constraint Embedding Closed-Chain Models — http://arxiv.org/abs/2609.21024v1
[17] Phase topology of one integrable case of the rigid body motion — http://arxiv.org/abs/1408.6028v1
[18] Hadronic few-body systems in chiral dynamics, -- Few-body systems in hadron physics -- — http://arxiv.org/abs/1210.1993v1
[19] Three-Body Dynamics in One Dimension — http://arxiv.org/abs/nucl-th/0211071v1
[20] The Coupling Effect: Experimental Validation of the Fusion of Fossen and Featherstone to Simulate UVMS Dynamics in Julia — https://doi.org/10.1109/oceans55160.2024.10754137
[21] Binding Energy in Two and Three-Body Relativistic Dynamics — http://arxiv.org/abs/hep-th/0111075v1
[22] Comparative Study on Serial and Parallel Forward Dynamics Algorithms for Kinematic Chains* — https://doi.org/10.1177/0278364909102350
[23] Forward Dynamics, Elimination Methods, and Formulation Stiffness in Robot Simulation — https://doi.org/10.1177/027836499701600603
[24] Linear-time Differential Inverse Kinematics: an Augmented Lagrangian Perspective — https://doi.org/10.15607/rss.2024.xx.110
[25] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1
[26] NTIRE 2025 Challenge on Image Super-Resolution (x4): Methods and Results — http://arxiv.org/abs/2504.14582v3
[27] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1
[28] VLSP 2025 MLQA-TSR Challenge: Vietnamese Multimodal Legal Question Answering on Traffic Sign Regulation — http://arxiv.org/abs/2510.20381v1
[29] Simplifying ROS2 controllers with a modular architecture for robot-agnostic reference generation — http://arxiv.org/abs/2601.08514v3
[30] A ROS2 based communication architecture for control in collaborative and intelligent automation systems — http://arxiv.org/abs/1905.09654v1
[31] CRISP -- Compliant ROS2 Controllers for Learning-Based Manipulation Policies and Teleoperation — http://arxiv.org/abs/2509.06819v2
[32] ROS2 Connect: A new ROS2 over WAN Solution — http://arxiv.org/abs/2608.25102v1
[33] FogROS2-SGC: A ROS2 Cloud Robotics Platform for Secure Global Connectivity — http://arxiv.org/abs/2306.17157v1
[34] Performance evaluation of a ROS2 based Automated Driving System — http://arxiv.org/abs/2411.11607v3
[35] Can Large Language Models Assist the Comprehension of ROS2 Software Architectures? — http://arxiv.org/abs/2604.21699v1
[36] Bridging the Sim-to-Real Gap with multipanda_ros2: A Real-Time ROS2 Framework for Multimanual Systems — http://arxiv.org/abs/2602.02269v2

---

*Generated by research-bot · topic=`机器人运动学控制与-ros-2` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`deepseek-v4-flash` · sources=36 · duration=183s · 2026-10-17T22:19:12+00:00*
