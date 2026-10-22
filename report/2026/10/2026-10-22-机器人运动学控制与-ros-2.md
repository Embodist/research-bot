# 机器人运动学、控制与 ROS 2：2024–2026 增量追踪报告

**日期**：2026-10-22（UTC）｜**领域**：机器人运动学 / 运动控制 / ROS 2 生态｜**检索源**：候选来源 34 条，其中主题直接相关 21 条、检索噪声 13 条（[1][10][12][13][14][15][16][17][18][20][21][23][30]）

**证据纪律说明**：本报告仅使用给定编号来源，不引入外部记忆事实。**已核实**的关键局限：候选集中除 [11]（MDPI *Sensors*，DOI 可解析）与 [22]（IEEE/SICE SII 2019）外，其余机器人相关条目均为 arXiv 预印本，**评审状态与第三方复现均未得到确认**；候选集**未包含任何公开榜单排名、GitHub star 或下载量数据**。因此，"已独立验证"与"仅演示/自评"的分界，在本报告中主要表现为"是否经同行评审 + 是否有第三方信号"，而非"是否刷新 SOTA"。另需提示上游检索存在明显主题漂移：如 [1][10][13] 为视觉/视频质量挑战赛、[15][16][17] 为天体物理与经典力学的"rigid body"同名误召、[20][21] 为车联网与电机监测，均不可用于支撑运动学与控制论断。

---

## 1. 进展与热点（Progress & Hotspots）

**一句话增量判断**：2024–2026 年，运动控制的主线变化是**"RL 全身策略 + sim-to-real 流水线"从可行性演示转向工程效率竞赛**（训练时长、数据来源、接触表征），而模型式方法退守到"可证明安全 / 标准合规"一侧；但本轮证据中**没有任何一条给出第三方独立验证或公开榜单对比**。

**（1）人形全身动态交互：RL 成为默认路线，仍属演示级**

- [2]（2025）以退火式 RL 课程实现人形**全身羽毛球**动态交互，问题陈述明确区分"静态场景交互已具备"与"动态真实世界交互仍困难"；属一手预印本自评，无第三方复现。热度：> 待核实｜权威：arXiv cs.RO 预印本，评审状态待核实 [2]｜关注度：低（无引用/榜单信号）｜推荐度：★★★☆☆（主题最贴近"全身动态控制"的一手样本，但缺量化对比）
- [7]（2025）研究**跨多样姿态的人形起身控制**，说明"跌倒恢复/起身"已成为独立的全身控制子问题；同上，仅摘要级证据 [7]｜推荐度：★★★☆☆
- [3]（2024-11）用**domain randomization 训练 diffusion policy 做人形全身控制**，代表"生成式策略表征 + 域随机化"这一 2024 年出现的组合路线 [3]｜关注度：低｜推荐度：★★★☆☆

**（2）sim-to-real 的竞争点从"能不能"转向"多快、多少数据"**

- [9]（2025-12）标题即宣称**15 分钟内完成人形行走 sim-to-real**，是"训练效率"成为显性指标的信号 [9]｜热度：> 待核实｜推荐度：★★★☆☆（效率类宣称需核实硬件与任务规模）
- [4]（2025-08）提出**"机器人训练机器人"**：由真机自动完成策略适配与学习，直指"从零真机 RL 罕见"这一瓶颈 [4]｜推荐度：★★★☆☆
- [28]（2026-10，本窗口最新）**SARI: Phase-Split Sim-Real Co-Training**，把 sim-real 协同训练按阶段切分用于接触丰富操作，代表"混合数据配比"成为新变量 [28]｜推荐度：★★★☆☆（最新但仅标题级证据，方法细节待核实）

**（3）数据采集范式：从遥操作转向"无机器人演示"**

- [5]（2026-02）**Humanoid Manipulation Interface** 明确批评现有全身操作依赖遥操作或视觉 sim-to-real RL，受"硬件物流与奖励工程"拖累，导致自主技能有限；提出**无机器人（robot-free）演示**路线 [5]｜权威：arXiv 预印本 [5]｜推荐度：★★★★☆（问题陈述具体、指向数据瓶颈，是本窗口最值得跟进的方向之一，但需核实真机规模）

**（4）接触丰富操作：从"二值接触"走向"物理接地接触表征"**

- [27]（2026-05）指出触觉等高信息密度模态在 sim-to-real 中常被压成**粗糙低维特征**而损失信息，主张 physics-grounded contact representation [27]｜推荐度：★★★☆☆
- [25]（2026-02）**TDC** 主张"可迁移方向柔顺性"，并明确指出既有 sim-to-real 方法要么依赖真实世界自适应、要么**以牺牲自适应柔顺为代价** [25]｜推荐度：★★★☆☆
- [26]（2023）**Online Admittance Residual Learning** 是本窗口之前的对照基线：以在线导纳残差学习实现接触丰富技能的 sim-to-real 迁移 [26]｜推荐度：★★★☆☆（作为"上一代基线"定位，非 2024–2026 增量）

**（5）模型式一侧：可证明安全 + 实时优化仍在推进，但验证停留在仿真**

- [24]（2025-05）对**柔线物体（DLO）**联合预测 shape 与 tension，并接入基于 polynomial zonotopes 的实时轨迹优化施加全程安全约束；实验为**仿真线束装配 + 7-DOF 机械臂单一场景**，候选块未显示真机结果 [24]｜推荐度：★★★☆☆（"学习 vs 模型"边界的对照样本；仿真 SOTA ≠ 真机 SOTA，须明示）

**（6）唯一同行评审样本**

- [11]（MDPI *Sensors*，DOI 10.3390/s26196324）**Scooter-Driving Humanoid Robot: Sim-to-Real Transfer Through Deep Reinforcement Learning**，是本候选集中唯一具备期刊 DOI 的运动控制实证条目，证据等级高于其余预印本 [11]｜关注度：低（无引用数据）｜推荐度：★★★★☆（同行评审 + 完整 sim-to-real 链条，可作为"已发表"参照）

**（7）ROS 2 侧**

- [19]（2022）**YASMIN: Yet Another State MachINe library for ROS 2**，是候选集中唯一直接命中 ROS 2 软件栈的条目，但发表于 2022 年，**不属于 2024–2026 增量**，只能定位为生态基础设施 [19]。

### 表 1｜经典与奠基性工作（与"最新进展"严格分节）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| The Pinocchio C++ library: rigid body dynamics algorithms and their analytical derivatives | 2019 | 候选块未提供 > 待核实 | citations=407 [22] | IEEE/SICE SII 2019，同行评审，DOI 可解析 [22] | 中（407 次引用，但无近期 star/讨论信号）[22] | ★★★★☆ 动力学与解析导数的开源内核，是 MPC/WBC/轨迹优化的共同底座 | https://doi.org/10.1109/sii.2019.8700380 | 刚体动力学算法 + 解析导数 |
| Learning Contact-Rich Manipulation Skills with Guided Policy Search | 2015 | 候选块未提供 > 待核实 | > 待核实 | arXiv 预印本，评审状态待核实 [29] | 低（候选块无引用数据）[29] | ★★★☆☆ 接触丰富操作"引导策略搜索"路线的奠基样本 | http://arxiv.org/abs/1501.05611v2 | 模仿/策略搜索用于接触任务 |
| One-Shot Reinforcement Learning for Robot Navigation with Interactive Replay | 2017 | > 待核实 | > 待核实 | arXiv 预印本 [6] | 低 [6] | ★★☆☆☆ 早期"交互式 replay + 单次学习"导航工作，历史定位为主 | http://arxiv.org/abs/1711.10137v2 | 交互式 replay RL 导航 |
| Efficient Sim-to-real Transfer of Contact-Rich Manipulation Skills with Online Admittance Residual Learning | 2023 | > 待核实 | > 待核实 | arXiv 预印本 [26] | 低 [26] | ★★★☆☆ 本窗口之前的力控残差 sim-to-real 基线，用于对比 [25][27] | http://arxiv.org/abs/2310.10509v1 | 在线导纳残差学习 |

> 说明：候选集**未包含** operational space control（Khatib）与 impedance control 的原始文献，无法据此评估二者对当代开源控制栈的理论塑造路径——此项为**明确证据缺口**，不做推断。

---

## 2. 工业界与产品（Industry & Product）

**一句话增量判断**：本候选集对"厂商产品 / 量产 / 权重开放"维度的覆盖**近乎为零**，因此该维度**本周期无可核实变化**；唯一可确认的产业侧信号是"开放硬件平台化"与"ROS 2 工具库持续供给"。

- **开放硬件平台信号**：[8]（2026-07）**The Open Ant: A Robot Platform for Reinforcement Learning Research**，定位为面向 RL 研究的机器人平台 [8]｜热度：> 待核实｜权威：arXiv 预印本，评审状态待核实 [8]｜关注度：低｜推荐度：★★★☆☆（"开放平台 + RL 研究"是教学与复现基础设施，具体本体形态与开放程度需核实）。
- **ROS 2 工具链供给**：[19] YASMIN 提供 ROS 2 状态机库，属生态层组件而非产品发布 [19]｜推荐度：★★★☆☆。
- **明确的未覆盖清单（全部 > 待核实）**：Drake、MuJoCo、ros2_control、MoveIt 2、OCS2、crocoddyl 的 2024–2026 工程实践与实时性数据；ROS 2 发行版演进（Jazzy / Kilted / Rolling）对实时控制栈的影响；任何厂商的产品发布、量产或权重开放公告。**本报告不对上述内容作任何判断**，因候选集内无一手来源可引。

> 结论性提示：该维度的空白是**检索覆盖不足**的证据，而非"产业无变化"的证据；在补齐官方 Release Notes、REP 文档与厂商技术报告前，不应得出"ROS 2 生态停滞"之类结论。

### 表 2｜开源项目

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Pinocchio | 2019 | > 待核实 | citations=407（论文层）[22]；GitHub star > 待核实 | 同行评审会议论文 + DOI [22] | 中（学术引用稳固，近期活跃度无证据）[22] | ★★★★☆ 动力学/导数计算的核心依赖，MPC 与 WBC 的事实标准底座之一 | https://doi.org/10.1109/sii.2019.8700380 | 刚体动力学 + 解析导数 |
| YASMIN | 2022 | > 待核实 | > 待核实（候选块无 star/下载） | arXiv 预印本，评审状态待核实 [19] | 低 [19] | ★★★☆☆ ROS 2 状态机库，适合任务编排层，非实时控制内核 | http://arxiv.org/abs/2205.13284v1 | ROS 2 状态机 |
| The Open Ant | 2026 | > 待核实 | > 待核实 | arXiv 预印本 [8] | 低 [8] | ★★★☆☆ 面向 RL 研究的开放机器人平台，复现价值取决于开源完备度 | http://arxiv.org/abs/2607.18488v1 | 开放 RL 研究平台 |
| ros2_control / MoveIt 2 / Drake / MuJoCo / OCS2 / crocoddyl | — | — | > 待核实 | > 待核实 | 未知 | —（不评） | 无可用来源 | **本候选集未覆盖，一律 > 待核实**，不做任何性能或版本判断 |

---

## 3. 蓝海与缺口（Blue Ocean & Gaps）

**一句话增量判断**：本轮证据暴露出的高杠杆缺口集中在**"仿真接触保真度 → 真机可迁移柔顺"这一段**，以及**"实时性从未被量化"这一共同语言缺失**。

1. **物理接地的接触表征**：现有方法把触觉压成低维粗糙特征，信息在进入策略前即被丢弃 [27]。谁能定义"信息充分且可仿真"的接触表征，谁就掌握 sim-to-real 的入口 [27]。
2. **可迁移的方向柔顺性**：既有路线在"真机自适应"与"保留自适应柔顺"之间二选一 [25]；"无需真机微调即可迁移的柔顺策略"是明确空白 [25]。
3. **真机验证缺口（最大蓝海）**：候选集中唯一带安全约束的接触任务工作在**仿真单场景**完成 [24]；三篇 sim-to-real 工作的真机规模均未在摘要级证据中给出 [25][27][28]。**"同一基准上的真机横向对比"目前无人提供。**
4. **实时性与 DDS 取舍的量化空白**：候选集中"real-time"仅作为优化器的形容词出现，**无控制频率、求解时延、DDS 通信开销的任何数字** [24][25][27]。这一缺口使"学习式 vs 模型式"之争缺乏可比的工程口径。
5. **无机器人演示的数据范式**：[5] 提出的 robot-free 演示，若成立，将绕开遥操作的硬件物流成本，是数据侧的结构性机会 [5]。
6. **标准合规的可执行实现**：ISO/TS 15066 约束下的能量罐控制 [32]、变阻抗控制 [34]、深度学习安全框架 [33] 各自孤立，**尚未形成中间件级的复用组件**。

### 表 3｜数据集与基准

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| 未检出 | — | — | 无 | 无 | 低 | — | 无 | 本候选集**未包含任何数据集或基准条目**；Open X-Embodiment / DROID / LIBERO / SimplerEnv / RoboArena 等常见基准**均未检索到**，其 2024–2026 变动一律 `> 待核实` |

> 该空缺直接限制本报告对"SOTA 是否被刷新"的判断能力：**无基准即无 SOTA**，第 1 章全部进展只能按"一手宣称"而非"榜单验证"处理。

---

## 4. 瓶颈与拐点（Bottleneck & Inflection）

**一句话增量判断**：瓶颈依旧在**接触动力学 sim-to-real gap 与真机数据成本**；但 2024–2026 出现了三个**可观测的缓解信号**（训练时长压缩、真机自动适配、sim-real 协同训练），指向"工程化拐点"而非"科学拐点"。

| 瓶颈 | 证据 | 拐点信号 | 判断 |
|---|---|---|---|
| 接触动力学 sim-to-real gap | 摘要明确指出仿真在接触动力学上存在 gap，且现有方法以牺牲自适应柔顺为代价 [25] | 出现"物理接地接触表征"[27]与"阶段切分协同训练"[28]两条替代路径 | 较大概率处于**方法发散期**，尚未收敛 |
| 真机数据成本与风险 | "真实世界数据学习 costly and risky"[25]；遥操作受硬件物流拖累 [5] | robot-free 演示 [5]、robot-trains-robot [4] | 推测：数据范式可能在 12–18 个月内重构 |
| 训练/迭代效率 | "15 分钟"级 sim-to-real 宣称 [9] | 效率成为标题级卖点，说明竞争维度迁移 [9] | 需核实（硬件与任务规模未知） |
| 安全可证明性 | 可证明安全仅在小规模仿真 DLO 任务验证 [24] | 标准侧出现 2025 版对比分析 [31] | 标准先于能力落地 |
| 实时性无共同口径 | 无任何频率/时延/抖动数字 [24][25][27] | 无 | **未见拐点信号**，`> 待核实` |

> 判定纪律：上述"效率提升"均为**作者自评标题级宣称**，无独立复现，**不得**表述为"已实现 15 分钟 sim-to-real"。

---

## 5. 社会·政策·国际（Society, Policy & Geopolitics）

**一句话增量判断**：本窗口唯一可核实的政策变化是**工业机器人安全标准体系更新到 2025 版并与 ISO/TS 15066 整合**，其影响已下渗到控制算法论文层（能量罐、变阻抗、学习式安全框架）。

- **标准更新（核心事实）**：[31]（2026-02）标题即表明对 **ISO 10218-1/2 的 2011 版与 2025 版做比较分析，并讨论 ISO/TS 15066 的整合** [31]。这构成本窗口政策维度的**最强信号**：标准已存在 2025 版，且人机协作安全条款（TS 15066）被纳入统一框架讨论 [31]。｜权威：arXiv 预印本，**条款级内容待核实**（仅有标题级证据）｜推荐度：★★★★☆（政策维度的唯一一手线索，须读全文核实条款差异）
- **合规控制实现的三条技术路径**（说明标准已转化为算法约束）：
  - 能量罐（energy tank）框架用于**满足 ISO/TS 15066 约束** [32]｜2023｜推荐度：★★★☆☆
  - 基于 ISO/TS 15066 的**变阻抗控制**实现安全物理人机交互 [34]｜2023｜推荐度：★★★☆☆
  - **ISO/TS 15066 合规框架下深度学习方法的分析** [33]｜2025-11｜推荐度：★★★☆☆（代表"学习方法被纳入合规评估"的新动向，安全性结论需核实）
- **未覆盖项（> 待核实）**：EU Machinery Regulation 的任何一手或二手来源在候选集中**完全缺失** [31][32][33][34] 均未涉及；地缘政治、供应链与出口管制维度**零证据**，本报告不作判断。
- **结构性含义**：标准更新 → 控制层必须提供"可证明的力/能量上界"→ 这一约束在客观上**有利于模型式与阻抗/能量罐方法**，对纯端到端学习策略构成合规门槛。此为推论，标注为 [P]，见第 7 章。

---

## 6. 资本与生态（Capital & Ecosystem）

**一句话增量判断**：本周期该维度**无显著可核实变化**——候选集内没有任何融资、并购、人才流动或治理结构的一手来源。

- **无证据项（一律 > 待核实）**：人形机器人融资额与估值、OSRA / ROS 治理结构变动、厂商供应链（减速器/灵巧手/力传感器）动态、开源许可证与权重开放策略变化。候选集 [2]–[34] 中无一条涉及资本或治理事件。
- **可间接观察的生态信号（弱）**：
  - 学术基础设施高度集中于少数动力学内核：Pinocchio 以 407 次引用成为 MPC/WBC 论文的公共依赖 [22]，形成"单点依赖"式生态结构。
  - ROS 2 生态的学术供给以**工具库**形式出现（状态机 [19]），而非控制内核；实时控制内核的学术披露在本候选集中缺席。
  - 开放硬件平台化尝试出现 [8]，可视为降低 RL 研究复现门槛的生态投入 [8]。
- **判断**：生态格局在本轮证据中**不可评估**；将其写成"人形融资热潮"或"ROS 治理改革"均属无据推断，本报告拒绝如此表述。

---

## 7. 信号与预测（Signals & Forecast）

**一句话增量判断**：可观测信号指向"**sim-to-real 工程效率**与**标准合规性**两条线同时收紧"，而"真机横向基准"与"实时性量化"两条线**仍为空**。

### 早期信号
- **[确定]** 接触表征正从二值/粗粒度走向物理接地建模 [27]。
- **[确定]** 安全标准已更新至 2025 版并整合 TS 15066，合规控制实现（能量罐 [32]、变阻抗 [34]）已成独立技术线。
- **[较大概率]** 数据范式正从遥操作转向无机器人演示与机器人自主产数据 [5][4]。
- **[推测]** 训练时长与数据配比（协同训练 [28]）将取代"能否 sim-to-real"成为论文主卖点 [9][28]。

### 可证伪假设（未来 6–18 个月）

| 编号 | 假设（可证伪） | 依据链 | 置信度 |
|---|---|---|---|
| H1 [P] | 若到 **2027-06** 仍未出现"含触觉模态、多任务、第三方复现"的接触丰富操作真机公开基准，则接触表征路线仍停留演示级，sim-to-real gap 未被实质性缩小 | [25][27] 均为摘要级自评、无基准 [24] 仅仿真单场景 | 中 |
| H2 [P] | 若"15 分钟级 sim-to-real"[9] 或 phase-split 协同训练 [28] 在 2027 年前被 **≥2 个独立团队在非人形本体**复现，则判定 sim-to-real 工程化拐点成立 | [9][28] 为单一团队宣称，尚无复现 | 中低 |
| H3 [P] | 若 2027 年前出现**ROS 2 生态内可复用的合规安全控制组件**（ISO/TS 15066 约束下的力/能量上界执行器），则标准→中间件的下渗路径成立 | ISO 10218-1/2 2025 版与 TS 15066 整合 [31]；现有实现为单篇论文级 [32][34][33] | 中 |
| H4 [P] | 若 2027 年前仍无**控制频率/抖动/QP 求解时延**的公开可比数据，则"学习式 vs 模型式"与"DDS 实时性取舍"之争将持续缺乏共同语言，工程选型继续依赖厂商口径 | 候选集零量化实时性证据 [24][25][27] | 高 |
| H5 [P] | 若模型式可证明安全方法在 2027 年前仍未扩展到**多任务真机**（当前仅仿真单场景 [24]），则其合规优势难以转化为部署优势 | [24] 实验范围有限 | 中 |

### [R] 未证实与不写项
- 人形机器人融资、量产爬坡、OSRA 治理变动、EU Machinery Regulation 生效影响：**本轮无任何可核实来源**，标注 `> 待核实`，不列入传闻清单以避免污染结论。

### Watchlist（建议下一轮优先补齐的检索目标）
1. **ROS 2 发行版与实时性一手文档**：Jazzy / Kilted / Rolling 的 Release Notes、REP 文档、ros2_control 与 MoveIt 2 的发行说明、1 kHz servo 循环实测报告 —— 本轮**完全缺失**。
2. **开源控制栈官方仓库**：Pinocchio、Drake、MuJoCo、OCS2、crocoddyl 的 star 数、最近提交与基准测试 —— 用于补齐 Pinocchio 的"热度/关注度"轴 [22]。
3. **接触丰富操作真机基准与榜单**：用于把 H1 从"待核实"转为可判定。
4. **[31] 全文**：ISO 10218-1/2 2011→2025 的条款级差异，是政策章节从"标题级"升级为"条款级"的关键一步 [31]。
5. **EU Machinery Regulation 一手文本**：本轮零覆盖。

---

## 参考来源

> 标注 † 者为检索噪声，未在正文用于支撑任何技术论断（仅在第 1 章前的证据纪律说明与来源统计中作为漂移示例引用）。

[1]† VQualA 2025 Challenge on Engagement Prediction for Short Videos — http://arxiv.org/abs/2509.02969v1
[2] Humanoid Whole-Body Badminton via an Annealed Reinforcement Learning Curriculum — http://arxiv.org/abs/2511.11218v4
[3] The Role of Domain Randomization in Training Diffusion Policies for Whole-Body Humanoid Control — http://arxiv.org/abs/2411.01349v1
[4] Robot Trains Robot: Automatic Real-World Policy Adaptation and Learning for Humanoids — http://arxiv.org/abs/2508.12252v2
[5] Humanoid Manipulation Interface: Humanoid Whole-Body Manipulation from Robot-Free Demonstrations — http://arxiv.org/abs/2602.06643v2
[6] One-Shot Reinforcement Learning for Robot Navigation with Interactive Replay — http://arxiv.org/abs/1711.10137v2
[7] Learning Humanoid Standing-up Control across Diverse Postures — http://arxiv.org/abs/2502.08378v2
[8] The Open Ant: A Robot Platform for Reinforcement Learning Research — http://arxiv.org/abs/2607.18488v1
[9] Learning Sim-to-Real Humanoid Locomotion in 15 Minutes — http://arxiv.org/abs/2512.01996v1
[10]† VQualA 2025 Challenge on Visual Quality Comparison for Large Multimodal Models — http://arxiv.org/abs/2509.09190v1
[11] Scooter-Driving Humanoid Robot: Sim-to-Real Transfer Through Deep Reinforcement Learning — https://doi.org/10.3390/s26196324
[12]† NTU-NPU System for Voice Privacy 2024 Challenge — http://arxiv.org/abs/2410.02371v1
[13]† NTIRE 2025 Challenge on Image Super-Resolution (x4) — http://arxiv.org/abs/2504.14582v3
[14]† LongEval at CLEF 2025: Longitudinal Evaluation of IR Model Performance — http://arxiv.org/abs/2503.08541v1
[15]† PINOCCHIO and the hierarchical build-up of dark matter haloes — http://arxiv.org/abs/astro-ph/0109324v1
[16]† The Relativistic Elasticity of Rigid Bodies — http://arxiv.org/abs/physics/0307019v3
[17]† Phase topology of one integrable case of the rigid body motion — http://arxiv.org/abs/1408.6028v1
[18]† Developing a 21st Century Global Library for Mathematics Research — http://arxiv.org/abs/1404.1905v1
[19] YASMIN: Yet Another State MachINe library for ROS 2 — http://arxiv.org/abs/2205.13284v1
[20]† Real-Time Service Subscription and Adaptive Offloading Control in Vehicular Edge Computing — http://arxiv.org/abs/2512.14002v1
[21]† Real time state monitoring and fault diagnosis system for motor based on LabVIEW — http://arxiv.org/abs/1806.09998v1
[22] The Pinocchio C++ library: A fast and flexible implementation of rigid body dynamics algorithms and their analytical derivatives — https://doi.org/10.1109/sii.2019.8700380
[23]† Overview of the Sensemaking Task at the ELOQUENT 2025 Lab — http://arxiv.org/abs/2507.12143v1
[24] Certifiably Safe Manipulation of Deformable Linear Objects via Joint Shape and Tension Prediction — http://arxiv.org/abs/2505.13889v1
[25] TDC: Sim-to-Real Transferable Directional Compliance for Contact-Rich Manipulation — http://arxiv.org/abs/2602.14174v2
[26] Efficient Sim-to-real Transfer of Contact-Rich Manipulation Skills with Online Admittance Residual Learning — http://arxiv.org/abs/2310.10509v1
[27] Beyond Binary: Sim-to-Real Dexterous Manipulation with Physics-Grounded Contact Representation — http://arxiv.org/abs/2605.28812v1
[28] SARI: Phase-Split Sim-Real Co-Training for Contact-Rich Manipulation — http://arxiv.org/abs/2610.02804v1
[29] Learning Contact-Rich Manipulation Skills with Guided Policy Search — http://arxiv.org/abs/1501.05611v2
[30]† A Simulation and Modeling of Access Points with Definition Language — http://arxiv.org/abs/1304.1836v2
[31] Evolution of Safety Requirements in Industrial Robotics: Comparative Analysis of ISO 10218-1/2 (2011 vs. 2025) and Integration of ISO/TS 15066 — http://arxiv.org/abs/2602.17822v1
[32] Energy Tank-based Control Framework for Satisfying the ISO/TS 15066 Constraint — http://arxiv.org/abs/2304.14059v1
[33] Analysis of Deep-Learning Methods in an ISO/TS 15066-Compliant Human-Robot Safety Framework — http://arxiv.org/abs/2511.19094v1
[34] Safe Physical Human-Robot Interaction through Variable Impedance Control based on ISO/TS 15066 — http://arxiv.org/abs/2311.13814v1

---

*Generated by research-bot · topic=`机器人运动学控制与-ros-2` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`deepseek-v4-flash` · sources=34 · duration=186s · 2026-10-22T22:26:24+00:00*
