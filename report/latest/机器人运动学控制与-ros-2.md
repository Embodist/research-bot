# 机器人运动学、控制与 ROS 2：2024–2026 增量调研报告

**元信息**｜日期：2026-10-12（UTC）｜领域：机器人运动学（kinematics）、控制（control）、ROS 2 生态｜可引用来源：34 条（[1]–[34]）｜子问题抽取结果：3 组（q1–q3）｜增量窗口：2024-01 – 2026-10

> **证据基线说明（必读）**：本轮回收的 34 条可引用来源中，存在**严重主题漂移**——q1 的候选块全部与运动学/控制/ROS 2 无关（HRI 信任工作坊 [2]、短视频热度预测 [3]、强引力透镜宇宙学 [4]、虫媒传染病 SIS 模型 [5]）；q3 同样只召回车联网边缘计算 [24] 与 NLP/多智能体竞赛 [28][29]。真正命中本主题的来源集中在 [1][7][8][9][10][11][12][13][14][15][16][17][19][22][23][31][34] 约 17 条。**因此本报告对"产业、资本、政策"等维度只能给出"证据为零"的判定，而非趋势结论**；所有无法核实的数字一律标注 `> 待核实`，不做推断性填充。

---

## 1. 进展与热点（Progress & Hotspots）

**增量判断**：相对 2024 年之前的基线，本批可核证据显示三处真实增量——① **人形全身控制从"平衡/行走"扩展到高动态任务**（羽毛球），并以强化学习课程退火实现 [9]；② **运动规划从"算法提出"转向"评测口径设计"**（基准化）[13][15]；③ **确定性实时性从理论模型进入可测量的工程指标**（LET 模型 [34]、DDS 分段延迟测试 [31]）。**未观察到任何 SOTA 榜单刷新类证据**（无 leaderboard 字段），故"最新 SOTA"在本报告中不可断言。

### 1.1 最新进展（近 1–2 年，2024-2026）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Humanoid Whole-Body Badminton via an Annealed Reinforcement Learning Curriculum [9] | 2025 | > 待核实 | > 待核实（候选块无 citations=） | arXiv 预印本（cs.RO），未标注同行评审 venue | 低 —— 无引用/star/榜单信号，> 待核实 | ★★★★☆ —— 直接命中"人形全身控制 + 高动态任务"前沿，是本批最贴近控制 SOTA 的一条 | http://arxiv.org/abs/2511.11218v4 | 用退火式 RL 课程实现人形全身羽毛球，属"任务难度—策略稳定性"折中路线 |
| The Role of Domain Randomization in Training Diffusion Policies for Whole-Body Humanoid Control [10] | 2024 | > 待核实 | > 待核实 | arXiv 预印本（cs.RO） | 低 —— 无热度字段，> 待核实 | ★★★★☆ —— 把 domain randomization 与 diffusion policy 组合用于全身控制，是"数据/随机化归因"问题的直接入口 | http://arxiv.org/abs/2411.01349v1 | 研究域随机化在扩散策略训练中的作用（归因于数据而非架构） |
| System Identification for Virtual Sensor-Based MPC: 2-DoF Direct-Drive Robotic Arm [7] | 2025 | > 待核实 | > 待核实 | arXiv 预印本（eess.SY/cs.RO 类），未标注 venue | 低 —— 无热度信号 | ★★★★☆ —— 用虚拟传感器做系统辨识以支撑 MPC，是"模型精度瓶颈"的工程级解法 | http://arxiv.org/abs/2505.23138v2 | 面向 2-DoF 直驱机械臂，把 MPC 对模型的依赖转化为可辨识问题 |
| Feedback Optimization with State Constraints through Control Barrier Functions [8] | 2025 | > 待核实 | > 待核实 | arXiv 预印本 | 低 —— 无热度信号 | ★★★☆☆ —— CBF 用作状态约束下的安全滤波，代表"控制+约束满足"合流方向 | http://arxiv.org/abs/2504.00813v3 | 反馈优化与 CBF 结合，处理状态约束 |
| Direct Kinematics, Inverse Kinematics, and Motion Planning of 1-DoF Rational Linkages [17] / 期刊版 [23] | 2024 / 2025 | > 待核实 | 期刊版 citations=6（候选块标注）[23]；arXiv 版 > 待核实 [17] | 期刊版：Mechanism and Machine Theory（Elsevier，同行评审）[23]；arXiv 版未标注 venue [17] | 低 —— 2025-10 新发表，引用数仅 6 [23] | ★★★☆☆ —— 正/逆运动学与运动规划统一解析处理，权威性可核实，但对象是特定 1-DoF 连杆机构 | [17] http://arxiv.org/abs/2409.01198v2 ；[23] https://doi.org/10.1016/j.mechmachtheory.2025.106074 | **跨版本交叉验证**：同一工作先出 arXiv [17] 后出期刊版 [23]，是本批唯一可做"预印本→期刊"校验的条目 |
| Optimizing Logical Execution Time Model for Both Determinism and Low Latency [34] | 2024 | > 待核实 | > 待核实 | RTAS 2024（IEEE 实时与嵌入式技术会议，同行评审） | 中 —— 属实时系统顶会，同行评审为权威信号；具体引用数 > 待核实 | ★★★★☆ —— 同时优化确定性与低延迟（LET 模型），是"实时性拐点"的机制级证据 | https://doi.org/10.1109/rtas61025.2024.00019 | 把 LET（Logical Execution Time）从牺牲延迟换成可同时兼顾 |
| Research on Segmented Latency Testing Method for in-Vehicle Real-Time Systems Based on DDS Middleware [31] | 2025 | > 待核实 | > 待核实 | SAE 技术论文（doi:10.4271/2025-01-8083），标准组织出版物 | 中 —— SAE 体系具备行业标准影响力；引用数 > 待核实 | ★★★★★ —— **本批唯一直接以 DDS 中间件延迟为题**的来源，对"ROS 2 QoS/DDS 确定性"议题不可替代 | https://doi.org/10.4271/2025-01-8083 | 分段式延迟测试方法，车载场景，但机制层可迁移至 ROS 2 的 DDS 层讨论 |
| The Open Ant: A Robot Platform for Reinforcement Learning Research [11] | 2026 | > 待核实 | > 待核实 | arXiv 预印本 | 低 —— 2026-07 新出，无热度信号 | ★★★☆☆ —— 提供 RL 研究用机器人平台，是"可复现硬件基线"的线索 | http://arxiv.org/abs/2607.18488v1 | 面向 RL 研究的开源式平台描述 |
| Evaluating Guiding Spaces for Motion Planning [13] | 2022（基线外但被本轮召回，说明评测议题延续） | > 待核实 | > 待核实 | arXiv 预印本（cs.RO），未标注录用信息 | 低 —— 无引用数/榜单信号，> 待核实 | ★★★☆☆ —— 讨论"如何评测采样启发式"，是评测口径设计的方法参考 | http://arxiv.org/abs/2210.08640v1 | 指出多数采样规划器已非均匀采样，而用启发式偏置 |

### 1.2 经典与奠基性工作（基线，2024 年之前）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Adaptive Control of Robot Manipulators With Uncertain Kinematics and Dynamics [1] | 2014（arXiv v3） | > 待核实 | > 待核实 | arXiv 预印本，候选块未标注同行评审 venue，> 待核实 | 低 —— 本批未提供引用数，> 待核实 | ★★★★☆ —— "运动学 + 动力学双重不确定性自适应"是控制领域的经典问题设定，理解后续工作的必要底座 | http://arxiv.org/abs/1403.5204v3 | 把运动学不确定性纳入自适应控制，而非假定 Jacobian 精确已知 |
| Motion planning in high-dimensional spaces [16] | 2018 | > 待核实 | > 待核实 | arXiv 预印本（综述性质） | 低 —— 无热度字段，> 待核实 | ★★★☆☆ —— 高维运动规划的全景梳理，作为术语与分类骨架仍可用 | http://arxiv.org/abs/1806.07457v2 | 高维空间中规划方法的综述性材料 |
| Predicted Composite Signed-Distance Fields for Real-Time Motion Planning in Dynamic Environments [19] | 2020 | > 待核实 | > 待核实 | arXiv 预印本 | 低 —— 无热度字段，> 待核实 | ★★★☆☆ —— "实时 + 动态环境"规划的代表性思路，与 §4 实时性瓶颈呼应 | http://arxiv.org/abs/2008.00969v2 | 用预测式复合 SDF 支撑动态环境实时规划 |
| One-Shot Reinforcement Learning for Robot Navigation with Interactive Replay [12] | 2017 | > 待核实 | > 待核实 | arXiv 预印本 | 低 —— 无热度字段，> 待核实 | ★★☆☆☆ —— 导航 RL 的早期样本效率路线，与 ROS 2 栈关联弱 | http://arxiv.org/abs/1711.10137v2 | 交互式回放实现单次学习 |
| Data-Efficient Learning of High-Quality Controls for Kinodynamic Planning used in Vehicular Navigation [14] | 2022 | > 待核实 | > 待核实 | arXiv 预印本 | 低 —— 无热度字段，> 待核实 | ★★★☆☆ —— 运动动力学规划（kinodynamic planning）中的控制质量学习，与运动学/控制交叉主题相关 | http://arxiv.org/abs/2201.02254v1 | 面向车辆导航的运动动力学规划控制学习 |
| Quantum control theory and applications: A survey [6] | 2009 | > 待核实 | > 待核实 | arXiv 预印本（综述） | 低 —— 无热度字段，> 待核实 | ★☆☆☆☆ —— **边界项**：控制理论综述，但对象是量子系统，不属机器人控制，仅作概念边界说明 | http://arxiv.org/abs/0910.2350v3 | 控制理论另一分支，不应混入机器人控制脉络 |
| The Relativistic Elasticity of Rigid Bodies [21] | 2003 | > 待核实 | > 待核实 | arXiv 预印本（physics） | 低 —— 无热度字段 | ★☆☆☆☆ —— **噪声项，建议剔除**；与机器人运动学无实质关联（"rigid bodies"为词面误召回） | http://arxiv.org/abs/physics/0307019v3 | 相对论弹性力学，非机器人刚体动力学 |

> **待核实**：本批来源均未提供 GitHub star、下载量或基准榜单排名字段，因此上表"热度/关注度"列大量为 `> 待核实`，**不得据此判断某工作"高影响力"**。

---

## 2. 工业界与产品（Industry & Product）

**增量判断**：本周期在该维度**证据近乎为零**——34 条来源中没有一条是厂商产品公告、官方发布说明或量产/真机部署报告。唯一可勉强归入"工程栈落地"的是 [22]（ROS 2 + MoveIt 2 的机械臂开发与运动规划库分析）与 [31]（车载 DDS 延迟测试，SAE 标准组织出版物）。因此本维度的正确结论是**"无法评估"，而非"无进展"**。

### 2.1 开源项目 / 工程栈

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Manipulator Robot Development and Analysis of Motion Planning Libraries Through ROS2 and MoveIt2 [22] | > 待核实（SSRN DOI 编号 5251139，年份未在本批标注） | > 待核实 | > 待核实（无 star/citations） | SSRN 预印本平台（doi:10.2139/ssrn.5251139），**非同行评审**，权威等级偏低 | 低 —— SSRN 预印本且无任何热度信号 | ★★★☆☆ —— **本批唯一明确出现 ROS2 + MoveIt2 字样的来源**，对"ROS 2 生态工程实践"维度不可替代，但需以官方文档交叉验证 | https://doi.org/10.2139/ssrn.5251139 | 对机械臂开发与运动规划库（MoveIt 2）做分析与对比 |
| The Open Ant: A Robot Platform for Reinforcement Learning Research [11] | 2026 | > 待核实 | > 待核实 | arXiv 预印本 | 低 —— 新出且无热度信号 | ★★★☆☆ —— 平台类工作，可能带来可复现硬件与代码线索，但本批未确认是否开源权重/代码 | http://arxiv.org/abs/2607.18488v1 | RL 研究用机器人平台，工程可复现性 > 待核实 |
| Research on Segmented Latency Testing Method for in-Vehicle Real-Time Systems Based on DDS Middleware [31] | 2025 | > 待核实 | > 待核实 | SAE 技术论文（标准组织出版物） | 中 —— SAE 体系具备行业标准影响力 | ★★★★★ —— 唯一以 DDS 中间件延迟为题，是 ROS 2 DDS 层工程测量的最近邻证据 | https://doi.org/10.4271/2025-01-8083 | 分段延迟测试方法，车载实时系统 |

### 2.2 边界与噪声条目（不纳入结论）

- [32] Edge Computing in Telecommunication: Reducing Latency for Real-Time Services 与 [33] Latency Revolution: How Edge Data Centers are Reshaping Real-Time Computing 均为 SSRN 平台的边缘计算时延材料（doi:10.2139/ssrn.6081611 / 10.2139/ssrn.5733985），**权威等级低（非同行评审，疑似白皮书/营销文本）**，与机器人控制栈无直接关系，仅可作"低延迟叙事在 IT 侧升温"的旁证。热度/关注度：`> 待核实`。
- [25] Real time state monitoring and fault diagnosis system for motor based on LabVIEW（arXiv:1806.09998v1，2018）：属电机状态监测/故障诊断，与"控制"仅词面相邻。热度 `> 待核实`，推荐度 ★☆☆☆☆。

> **待核实**：Nav2、ros2_control、MoveIt 2、Gazebo/Isaac 的版本演进、维护活跃度、star 数，在本批 34 条来源中**完全缺失**，本报告不做任何版本号或活跃度断言。

---

## 3. 蓝海与缺口（Blue Ocean & Gaps）

**增量判断**：本维度的增量不是"发现了新缺口"，而是**用可核查方式确认了若干关键缺口在文献层真的没有被本轮召回覆盖**——这本身就是高价值信息：说明这些方向要么证据分散在非 arXiv 渠道（官方文档、GitHub、标准文档），要么相关研究确实稀少。

### 3.1 数据集与基准

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Local Planner Bench: Benchmarking for Local Motion Planning [15] | 2022 | > 待核实 | > 待核实（无 star/citations 字段） | arXiv 预印本（cs.RO），是否已正式发表 > 待核实 | 低 —— 无榜单排名/引用信号 | ★★★★☆ —— **本批唯一的运动规划专用基准**，是"规划评测口径"议题的锚点，缺口分析必引 | http://arxiv.org/abs/2210.06033v1 | 面向局部运动规划的基准化评测 |
| Second MOASEI Competition at AAMAS'2026: A Technical Report [29] | 2026 | > 待核实 | > 待核实 | arXiv 技术报告（cs.MA），AAMAS'2026 关联竞赛报告 | 中 —— AAMAS 关联年度竞赛具备会议社区持续关注度；参赛规模 > 待核实 | ★★★☆☆ —— 引入 **frame openness**（智能体装备随帧变化），代表"开放动态环境如何评测"的新尝试 | http://arxiv.org/abs/2607.03399v1 | 保留 wildfire/cybersecurity/ride-sharing 三域，新增 frame openness 加分赛道 |
| Evaluating Guiding Spaces for Motion Planning [13] | 2022 | > 待核实 | > 待核实 | arXiv 预印本（cs.RO） | 低 —— 无热度信号 | ★★★☆☆ —— 作为"评测方法论"而非数据集使用 | http://arxiv.org/abs/2210.08640v1 | 评估采样启发式（guiding space）有效性 |
| VQualA 2025 Challenge on Engagement Prediction for Short Videos [3] | 2025 | 42 位作者（名单见原文） | > 待核实 | arXiv 综述（cs.CV），ICCV 2025 同期挑战赛官方总结 | 中 —— ICCV 关联挑战赛，但**与机器人无关** | ★☆☆☆☆ —— 领域外，仅作"挑战赛 + 专用数据集"组织形态样例 | http://arxiv.org/abs/2509.02969v1 | UGC 短视频参与度预测 |
| AIM 2025 Challenge on High FPS Motion Deblurring [18] | 2025 | > 待核实 | > 待核实 | arXiv 综述（cs.CV），ICCV 2025 挑战赛总结 | 低 —— 与机器人无关 | ★☆☆☆☆ —— 纯噪声项，建议剔除 | http://arxiv.org/abs/2509.06793v1 | 高帧率运动去模糊 |
| AutoRestTest at the SBFT 2026 Tool Competition [30] | 2026 | > 待核实 | > 待核实 | arXiv 竞赛工具报告（软件测试） | 低 —— 与机器人无关 | ★☆☆☆☆ —— 噪声项 | http://arxiv.org/abs/2607.01063v1 | 软件测试工具竞赛 |

> **重要缺口声明**：具身智能/机器人领域常被引用的基准与数据集（Open X-Embodiment、DROID、LIBERO、SimplerEnv、RoboArena 等）**在本批 34 条可引用来源中没有任何条目**，因此本报告**不引用它们**，其现状一律 `> 待核实`，需另行定向检索。

### 3.2 高杠杆蓝海缺口（均基于本批证据的"零覆盖"判定）

1. **ROS 2 中间件确定性（DDS/QoS）与机器人控制的联合研究**：本批唯一 DDS 相关来源是车载场景的 [31]，唯一确定性机制来源是通用实时系统的 [34]；**没有一条把 DDS QoS 策略与机械臂/人形控制回路的稳定性直接关联**。这是一个可核查的空白。依据：[31][34]，缺口判定依据 q3 抽取结果（[3][24][28][29] 均无 DDS/ROS 2/QoS 关键词）。
2. **标定（calibration）**：本批 34 条来源中**零覆盖**（无手眼标定、无运动学参数辨识专文；[7] 做的是系统辨识用于 MPC，非标定）。`> 待核实`
3. **接触丰富与柔顺控制（contact-rich / compliant control）**：本批**零覆盖**。人形控制相关条目 [9][10] 属全身运动与 RL 策略，未涉及接触力/阻抗控制。`> 待核实`
4. **仿真-真机（sim-to-real）评测口径**：本批**零覆盖**——没有任何条目给出硬件平台 + 任务数 + 成功率统计口径的三元组。q2 抽取已明确将该点列为 open problem。`> 待核实`
5. **运动规划基准与 ROS 2 Nav2 的打通**：已有规划基准 [15] 与 ROS 2 栈分析 [22]，但**两者之间无桥接证据**，即"标准规划基准如何映射到 Nav2 实际评测"仍属空白。

---

## 4. 瓶颈与拐点（Bottleneck & Inflection）

**增量判断**：本周期最清晰的拐点信号出现在**实时性/确定性**——它正从"理论性质"变成"可测量、可优化、可写入标准的工程指标"（[34] 同时优化确定性与低延迟；[31] 分段延迟测试方法）。第二个信号是**模型精度瓶颈的工程化绕行**：当 MPC 依赖精确模型时，路线不是换算法而是补辨识（[7]）或把不确定性显式建模进控制器（[1]）。

| # | 瓶颈 | 证据 | 拐点信号 / 强度 |
|---|---|---|---|
| 1 | **实时性与确定性**：时间关键系统在带宽与算力双约束、严格截止期下仍难求解 | [24]（车联网语境，DOAP 问题 + SARound；arXiv:2512.14002v1，cs.DC，未标注同行评审；热度 `> 待核实`） | **较大概率已临近拐点**：LET 模型可同时优化确定性与低延迟 [34]（RTAS 2024，同行评审）；DDS 层已有分段延迟测试方法 [31]（SAE） |
| 2 | **中间件机制层证据缺失**：DDS / ROS 2 QoS / 确定性实时中间件在 q3 候选中零覆盖 | q3 抽取结论（[3][24][28][29] 均无相关关键词） | **未知**——需补检 ROS 2 官方文档与实时 DDS 实现（`> 待核实`） |
| 3 | **模型精度依赖**：MPC/控制质量受制于模型与传感器可观测性 | [7]（虚拟传感器 + 系统辨识，2-DoF 直驱臂） | **推测**：从"换更复杂模型"转向"补辨识 + 虚拟传感"的路线正在成型；单条证据，强度弱 |
| 4 | **不确定性建模**：运动学与动力学同时不确定 | [1]（2014 基线，运动学+动力学双重不确定性自适应） | **无新证据**表明该问题在 2024–2026 被新范式取代；`> 待核实` |
| 5 | **安全约束满足**：状态约束下如何不牺牲闭环性能 | [8]（CBF 用于反馈优化，2025） | **较大概率**：CBF 作为"安全滤波层"与主流控制/学习策略合流的趋势信号；但仅单条来源，需交叉验证 |
| 6 | **评测口径不统一**：规划启发式、局部规划器缺乏共识度量 | [13]（guiding space 如何评测）、[15]（Local Planner Bench） | **中**：已有基准尝试，但均为 2022 年且是否与 ROS 2 生态对齐 `> 待核实` |
| 7 | **证据层瓶颈**：本批来源无 star/下载/榜单字段，"谁在工业界真正部署"不可判定 | §2、§3 表 | **未知**——属检索瓶颈而非技术瓶颈，需补 GitHub/官方文档源 |

> **争议与失败案例**：本批证据中**未出现**任何负面结果、复现失败报告或方法间直接对照争议。q3 抽取明确指出"本批次候选块未提供任何关于 DDS/ROS 2 确定性、标定、接触丰富与柔顺控制的可核查材料"。因此本报告不臆造争议。`> 待核实`

---

## 5. 社会·政策·国际（Society, Policy & Geopolitics）

**增量判断**：**本周期在该维度无显著变化**——在 34 条可引用来源中，没有任何一条是机器人领域的监管文件、国家标准、出口管制、供应链报告或伦理/劳动影响研究。

可观察的边缘信号（均为弱证据，仅作线索，不构成结论）：

- [31] SAE 技术论文（doi:10.4271/2025-01-8083）表明**标准组织仍在推进车载实时系统的延迟测试方法学**，属"工程标准活动"而非政策/监管。权威：SAE 标准组织出版物；热度 `> 待核实`；关注度：中（标准体系影响力）；推荐度 ★★★★☆（因唯一可核实的标准侧来源）。
- [28] 涉及 UN/UNESCO 决议的段落级论点挖掘任务（arXiv:2607.20430v1，cs.CL；"获胜系统"为作者自述，官方榜单未附），**其研究对象是文本而非政策本体**，不能作为国际政策动向证据。推荐度 ★☆☆☆☆，`> 待核实`。
- 关于机器人领域的国际标准（如 ISO 10218 / ISO/TS 15066）、各国具身智能政策、供应链（减速器/伺服/芯片）与出口管制：**本批来源零覆盖**，一律 `> 待核实`，需另行检索官方公报与标准组织页面。

> **结论**：本维度**不做任何趋势判断**。任何"某国政策推动/限制机器人产业"的表述在本次证据下均不可成立。

---

## 6. 资本与生态（Capital & Ecosystem）

**增量判断**：**本周期在该维度无显著变化（证据为零）**。34 条来源中没有任何一条包含融资额、并购、估值、人才流动、公司格局或社区活跃度数据。本批所有条目均无 `stars=`、下载量、榜单排名字段（q1/q2 抽取已两次确认这一点）。

可间接观察到的生态信号（弱，仅作"生态组织形态"参考，不作资本结论）：

- **评测竞赛化已成常态**：ICCV 2025 体系内存在稳定挑战赛 + 专用数据集组织形态 [3][18]；软件测试领域有 SBFT 2026 工具竞赛 [30]；多智能体领域有 AAMAS 年度延续竞赛（MOASEI 第二届，2026）[29]。这些说明**会议驱动的评测生态在扩张**，但不等于资本流入。
- **机器人方向的评测生态证据薄弱**：本批中真正与机器人相关的竞赛/基准仅 [15]（Local Planner Bench，2022）与 [29]（多智能体仿真，非机器人本体），**与 VLA/操作领域的竞赛生态无任何可引用证据**。`> 待核实`
- **开源生态热度无法评估**：[11] The Open Ant（2026）、[22] ROS2/MoveIt2 分析均无 star 或维护活跃度数据。推荐度仅基于相关性给出（[11] ★★★☆☆、[22] ★★★☆☆），**不代表采用度或商业价值**。

> **结论**：任何关于"资本正在涌入/撤离某方向""人才向某公司集中"的表述，在本次证据下均属编造，**不予输出**。

---

## 7. 信号与预测（Signals & Forecast）

**增量判断**：本批证据足以支撑的预测很少且偏工程侧；以下每条均写成**可证伪假设**，并标注依据链与置信度。不确定处标 `[P]`（预测）、`[R]`（传闻，本轮无此类条目）、`[Debated]`（争议，本轮无）。

### 7.1 早期信号（已确证的事实层）
1. 实时性研究已从"提出确定性模型"演进到"同时优化确定性与延迟" [34]，并出现 DDS 中间件分层延迟测量的工程方法 [31]。**证据等级：A（[34] 同行评审） / B（[31] 标准组织技术论文）**。
2. 运动规划研究的注意力部分转向评测方法论 [13][15]，而非新算法。**证据等级：B（预印本）**。
3. 全身人形控制开始覆盖高动态任务 [9] 并通过域随机化 + 扩散策略探索泛化 [10]。**证据等级：B（预印本）**。

### 7.2 可证伪预测

| # | 预测（可证伪假设） | 标记 | 依据链 | 置信度 | 证伪条件 |
|---|---|---|---|---|---|
| P1 | 到 2027 年底前，会出现把 **ROS 2 的 DDS QoS 配置与实时控制回路稳定性做联合量化**的公开研究（论文或官方基准） | [P] | 信号 ①：LET 可同时优化确定性与延迟 [34]；信号 ②：DDS 层已有可用的分段延迟测试方法 [31]；信号 ③：本批中"DDS × 机器人控制"为零覆盖（§3.1 缺口 1），空白越大越易被填补 | 推测（中低） | 若到 2027-12-31 仍未检索到任何将 QoS 策略与控制性能指标联合建模的公开论文或官方文档，则 P1 不成立 |
| P2 | 运动规划评测将向"统一基准 + 可复现实验协议"收敛，出现至少 1 个被多个团队在论文中共同引用的局部规划基准 | [P] | 信号：已有基准化尝试 [15]，且已有专门讨论"评测怎么做"的方法学工作 [13]；但两者均为 2022 年，本批未见 2024–2026 的替代品 | 推测（中低） | 若到 2027-12-31，运动规划论文仍普遍各用自建场景、无共同基准被反复引用，则 P2 不成立 |
| P3 | "系统辨识 / 虚拟传感"会被更多作为 MPC 在真实机械臂上的前置步骤写入工程流程，而非仅在特定论文中出现 | [P] | 信号：[7] 以虚拟传感 + 辨识支撑 2-DoF 直驱臂 MPC；[1] 显示运动学不确定性长期是被显式处理的对象 | 推测（低，仅单条直接证据） | 若 2027-12-31 前的真实机械臂 MPC 工作仍普遍假设精确模型且不报告辨识环节，则 P3 不成立 |
| P4 | CBF（控制屏障函数）会从"独立方法"更多转为"叠加在既有控制器/学习策略之上的安全层" | [P] | 信号：[8] 将 CBF 用于状态约束下的反馈优化（2025） | 推测（低，单条证据） | 若 2027-12-31 前 CBF 相关工作仍主要作为独立最优控制问题求解、而非附加滤波层，则 P4 不成立 |
| P5 | 具身智能**仿真-真机评测口径**（硬件 + 任务数 + 成功率统计）会成为下一轮公开讨论焦点 | [P] | 信号：本批 34 条来源对该口径**零覆盖**（§3.2 缺口 4），而人形全身任务 [9][10] 已进入需要标准化评测的阶段 | 推测（中低） | 若 2027-12-31 前仍未出现被广泛采用的 sim-to-real 报告规范或榜单，则 P5 不成立 |

### 7.3 明确不可预测项（证据不足，禁止外推）
- 资本流向、厂商产品路线、政策与出口管制、供应链变化：**本批证据为零**，`> 待核实`，不做预测。
- 任何"SOTA 已被刷新至 X%"的断言：本批**无任何基准榜单数据**，不做预测。
- 争议性判断（如"端到端是否优于模块化"）：本批**无对立证据**，不标 `[Debated]` 以免虚构争议。

---

## 参考来源

[1] Adaptive Control of Robot Manipulators With Uncertain Kinematics and Dynamics — http://arxiv.org/abs/1403.5204v3
[2] TRUST 2025: SCRITA and RTSS @ RO-MAN 2025 — http://arxiv.org/abs/2509.11402v1
[3] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1
[4] TDCOSMO 2025: Cosmological constraints from strong lensing time delays — http://arxiv.org/abs/2506.03023v4
[5] A Human-Vector Susceptible-Infected-Susceptible Model for Analyzing and Controlling the Spread of Vector-Borne Diseases — http://arxiv.org/abs/2510.14787v2
[6] Quantum control theory and applications: A survey — http://arxiv.org/abs/0910.2350v3
[7] System Identification for Virtual Sensor-Based Model Predictive Control: Application to a 2-DoF Direct-Drive Robotic Arm — http://arxiv.org/abs/2505.23138v2
[8] Feedback Optimization with State Constraints through Control Barrier Functions — http://arxiv.org/abs/2504.00813v3
[9] Humanoid Whole-Body Badminton via an Annealed Reinforcement Learning Curriculum — http://arxiv.org/abs/2511.11218v4
[10] The Role of Domain Randomization in Training Diffusion Policies for Whole-Body Humanoid Control — http://arxiv.org/abs/2411.01349v1
[11] The Open Ant: A Robot Platform for Reinforcement Learning Research — http://arxiv.org/abs/2607.18488v1
[12] One-Shot Reinforcement Learning for Robot Navigation with Interactive Replay — http://arxiv.org/abs/1711.10137v2
[13] Evaluating Guiding Spaces for Motion Planning — http://arxiv.org/abs/2210.08640v1
[14] Data-Efficient Learning of High-Quality Controls for Kinodynamic Planning used in Vehicular Navigation — http://arxiv.org/abs/2201.02254v1
[15] Local Planner Bench: Benchmarking for Local Motion Planning — http://arxiv.org/abs/2210.06033v1
[16] Motion planning in high-dimensional spaces — http://arxiv.org/abs/1806.07457v2
[17] Direct Kinematics, Inverse Kinematics, and Motion Planning of 1-DoF Rational Linkages — http://arxiv.org/abs/2409.01198v2
[18] AIM 2025 Challenge on High FPS Motion Deblurring: Methods and Results — http://arxiv.org/abs/2509.06793v1
[19] Predicted Composite Signed-Distance Fields for Real-Time Motion Planning in Dynamic Environments — http://arxiv.org/abs/2008.00969v2
[20] PINOCCHIO and the hierarchical build-up of dark matter haloes — http://arxiv.org/abs/astro-ph/0109324v1
[21] The Relativistic Elasticity of Rigid Bodies — http://arxiv.org/abs/physics/0307019v3
[22] Manipulator Robot Development and Analysis of Motion Planning Libraries Through ROS2 and MoveIt2 — https://doi.org/10.2139/ssrn.5251139
[23] Direct kinematics, inverse kinematics, and motion planning of 1-DoF rational linkages — https://doi.org/10.1016/j.mechmachtheory.2025.106074
[24] Real-Time Service Subscription and Adaptive Offloading Control in Vehicular Edge Computing — http://arxiv.org/abs/2512.14002v1
[25] Real time state monitoring and fault diagnosis system for motor based on LabVIEW — http://arxiv.org/abs/1806.09998v1
[26] UIC-AIHealth4All at ArchEHR-QA 2026: Answer-First Evidence Grounding for Clinical Question Answering — http://arxiv.org/abs/2608.27467v1
[27] ZeroR@CHiPSAL 2026: Two-Stage Vision-Language Adaptation with Contrastive Learning for Nepali Meme Classification — http://arxiv.org/abs/2607.28637v1
[28] LLM-INSTRUCT at UZH Shared Task 2026: Constraint-Aware Retrieval and Selective Debate for Paragraph-Level Argument Mining — http://arxiv.org/abs/2607.20430v1
[29] Second MOASEI Competition at AAMAS'2026: A Technical Report — http://arxiv.org/abs/2607.03399v1
[30] AutoRestTest at the SBFT 2026 Tool Competition — http://arxiv.org/abs/2607.01063v1
[31] Research on Segmented Latency Testing Method for in-Vehicle Real-Time Systems Based on DDS Middleware — https://doi.org/10.4271/2025-01-8083
[32] Edge Computing in Telecommunication: Reducing Latency for Real-Time Services — https://doi.org/10.2139/ssrn.6081611
[33] Latency Revolution: How Edge Data Centers are Reshaping Real-Time Computing — https://doi.org/10.2139/ssrn.5733985
[34] Optimizing Logical Execution Time Model for Both Determinism and Low Latency — https://doi.org/10.1109/rtas61025.2024.00019

---

*Generated by research-bot · topic=`机器人运动学控制与-ros-2` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`deepseek-v4-flash` · sources=34 · duration=197s · 2026-10-12T22:13:44+00:00*
