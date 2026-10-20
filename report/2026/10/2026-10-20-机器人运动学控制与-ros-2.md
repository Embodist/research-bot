# 机器人运动学、控制与 ROS 2：2024–2026 相对基线增量追踪报告

**日期**：2026-10-20（UTC）｜**领域**：机器人运动学 / 控制 / ROS 2 中间件｜**检索源**：候选证据 35 条，去重后与本主题直接相关 7 条（[21][22][23][25][30][31][32][35]）

> **证据基线声明（必读）**：本次下发的候选证据池与本主题严重不匹配。q1（运动学/控制/ROS 2 新进展）返回 4 条候选，主题为短视频参与度预测[13]、HRI 信任 workshop[14]、基础模型透明度指数[16]、新闻主观性检测[18]；q2（工具链/基准）返回 3 条候选，分别为 NLP 文本检测[1]、天体物理 PINOCCHIO[5]、相对论弹性[7]。**没有任何一条涉及 ros2_control、ROS 2 Jazzy/Kilted/Rolling、DDS/Zenoh、MPC、可微运动学、Pinocchio、Drake、CasADi、Crocoddyl、OCS2、Ruckig、MoveIt 2、Nav2、OMPL、MuJoCo/MJX。** 因此本报告在控制算法与中间件层面的“增量”只能给出极稀疏的可核查结论，其余一律标 `> 待核实`，不做任何基于模型记忆的补写。另需注意同名歧义：文献 [5] 的 “PINOCCHIO” 是天体物理暗物质晕合并树算法，**不可**作为机器人刚体动力学库 Pinocchio 的证据[5]。

---

## 1. 进展与热点（Progress & Hotspots）

**一句话增量判断**：本批证据仅能确认两条可核查增量——(a) 人形全身控制继续沿“RL + 课程/域随机化”路线推进到高动态任务（羽毛球）[21][22]；(b) 工业机器人安全标准完成 2011→2025 的换代并与 ISO/TS 15066 整合[25][35]。**ros2_control、ROS 2 发行版与 DDS/Zenoh 层面：本批证据零覆盖，`> 待核实`。**

### 1.1 全身控制 / 人形机器人控制（最新进展，2024–2026）

- **Humanoid Whole-Body Badminton via an Annealed Reinforcement Learning Curriculum**（arXiv 2511.11218v4，2025-11，cs.RO）[21]。相对基线增量：把全身人形控制从“行走/搬运/ locomotion”推进到**高动态、强对抗的羽毛球击打**任务，方法侧的关键是 **annealed curriculum**（退火式课程）而非纯域随机化。
  - 热度证据：候选块未提供引用数、无 GitHub star 数据 `> 待核实`[21]。
  - 权威证据：arXiv 预印本（cs.RO），候选块未标注会议/期刊录用信息，同行评审状态 `> 待核实`[21]。
  - 关注度：**低**——依据：仅见预印本与 v4 修订记录，候选块无引用/榜单/社区信号可核[21]。
  - 推荐度：**★★★☆☆**——与本主题（全身控制）高度相关，但证据等级为 B 且缺第三方复现，适合追踪不宜作为结论依据[21]。

- **The Role of Domain Randomization in Training Diffusion Policies for Whole-Body Humanoid Control**（arXiv 2411.01349v1，2024-11，cs.RO）[22]。相对基线增量：把 **diffusion policy** 引入全身人形控制，并**系统消融 domain randomization 的作用**（而非把 DR 当作默认技巧）。
  - 热度证据：`> 待核实`（无引用数/star 数据）[22]。
  - 权威证据：arXiv 预印本（cs.RO），评审状态 `> 待核实`[22]。
  - 关注度：**低**——依据：候选块无任何热度信号[22]。
  - 推荐度：**★★★☆☆**——若关注“仿真到真机的迁移归因”（提升来自数据增强还是架构），这是本批唯一直接讨论该问题的条目[22]。

> **归因判断**：[21][22] 的改进主要归因于**训练范式（课程设计、DR 策略）**，而非新硬件或新算力；两篇均为单团队、单任务设定，尚未在多个本体/多任务上验证，尚未达到“已被独立验证”的门槛[21][22]。

### 1.2 ROS 2 与实时分布式控制（最新进展）

- **Performance Evaluation of ROS2 and Micro-ROS for Real-Time Distributed Control of Omnidirectional Mobile Robots**（DOI: 10.61961/injei.v3i1.87）[23]。相对基线增量：本批**唯一**对 ROS 2 / Micro-ROS 在真实控制回路中做性能评测的条目，提供了“ROS 2 能否承担实时分布式控制”的实证口径。
  - 热度证据：`> 待核实`（候选块未提供引用数/下载量）[23]。
  - 权威证据：有 DOI、发表于 *Injei* v3(1)，属期刊出版；但期刊影响力与是否严格同行评审 `> 待核实`[23]。
  - 关注度：**低**——依据：非机器人顶会/顶刊，候选块无引用与社区讨论信号[23]。
  - 推荐度：**★★☆☆☆**——主题相关但证据等级 C，且是单篇孤证，不能据此判断 ROS 2 实时性整体水平[23]。

### 1.3 安全监控与运行时保障（最新进展）

- **Initiation Safety: A Missing Dimension in Generalist-Robot Safety**（arXiv 2607.07420v2，2026-07，cs.RO）[30]。增量：提出通用机器人安全的**第三维度 “initiation authorization”**——机器人是否应当采取第一个难以撤销的社会性动作（打招呼、未受邀抓取、进入他人空间），区别于既有的 motion safety 与 dialogue safety。
- **Robot Safety Monitoring using Programmable Light Curtains**（arXiv 2404.03556v1，2024-04）[31]。增量：用**可编程光幕**做运行时安全监控，属“感知即安全层”的工程化路径。
- **Conformal Safety Monitoring for Flight Testing: A Case Study in Data-Driven Safety Learning**（arXiv 2511.20811v1，2025-11）[32]。增量：把 **conformal prediction** 用于安全监控，提供**有统计保证**的运行时告警口径（航空试飞案例，非机器人）。
  - 热度证据：三条均为 `> 待核实`（候选块无引用数/star）[30][31][32]。
  - 权威证据：[30] arXiv 预印本 cs.RO（2026）[30]；[31] arXiv 预印本 cs.RO（2024）[31]；[32] arXiv 预印本（2025）[32]；均为预印本，评审状态 `> 待核实`。
  - 关注度：**低**——依据：候选块无引用、无榜单、无开源仓库信号[30][31][32]。
  - 推荐度：**★★★☆☆**（[30]，提出了新的问题维度）/ **★★☆☆☆**（[31][32]，方法可借鉴但非本主题核心）[30][31][32]。

### 1.4 本批次明确的证据缺口（SOTA 无法判定）

| 待判定项 | 本批证据状态 |
|---|---|
| ros2_control 新能力（控制器生命周期、硬件接口、实时调度） | 零覆盖，`> 待核实` |
| ROS 2 Jazzy / Kilted / Rolling 发行版变更 | 零覆盖，`> 待核实` |
| DDS / Zenoh（rmw_zenoh、零拷贝、executor）定量对比 | 零覆盖（仅 [23] 一篇 ROS2/Micro-ROS 评测），`> 待核实` |
| MPC 与 RL 混合控制 | 零覆盖（[21][22] 均为纯 RL/策略学习），`> 待核实` |
| 可微运动学 / 可微动力学 | 零覆盖，`> 待核实` |
| Pinocchio / Drake / CasADi / Crocoddyl / OCS2 / Ruckig / MoveIt 2 / Nav2 / OMPL / MuJoCo / MJX 版本演进 | 零覆盖，`> 待核实` |

---

## 2. 工业界与产品（Industry & Product）

**一句话增量判断**：本批证据**没有任何厂商产品发布、官方技术博客、量产或真机部署材料**；唯一具备“产业结构性影响”的增量是工业机器人安全标准的换代[25][35]，以及 ROS 2/Micro-ROS 在移动机器人控制中的工程化评测[23]。

- **标准换代即产业准入门槛变化**：ISO 10218-1/2 由 2011 版更新至 2025 版，并整合 ISO/TS 15066（协作机器人）要求[25][35]。对厂商的直接含义是：安全功能（speed & separation monitoring、power & force limiting）的实现与文档需按新版重写。
  - 热度证据：`> 待核实`（候选块未提供引用数）[25][35]。
  - 权威证据：**A 级**——[35] 发表于 *Results in Engineering*（Elsevier，DOI: 10.1016/j.rineng.2026.110486），同行评审期刊；[25] 为同文 arXiv 版（2602.17822v1，2026-02）[25][35]。
  - 关注度：**中**——依据：同一成果同时以 arXiv 与期刊形式发布，说明作者侧重视；但候选块无引用/标准委员会公告类信号，终端用户关注度 `> 待核实`[25][35]。
  - 推荐度：**★★★★☆**——本报告中证据等级最高、与“标准/合规”主线最相关的条目[25][35]。
- **ROS 2 工程化落地的可核查信号**：[23] 以全向移动机器人为对象评测 ROS 2 与 Micro-ROS 的实时分布式控制表现，说明 ROS 2 已被用于**嵌入式 + 分布式**控制回路的可行性验证场景[23]。
  - 热度 `> 待核实`；权威：期刊论文，等级 C[23]；关注度 **低**（非顶会、无社区信号）[23]；推荐度 **★★☆☆☆**。
- **厂商/产品动态（Franka、Universal Robots、Boston Dynamics、Unitree、Agility 等）**：本批证据零覆盖，`> 待核实`，本报告不作任何推测。

---

## 3. 蓝海与缺口（Blue Ocean & Gaps）

**一句话增量判断**：本批证据指出的高杠杆空白集中在**“通用机器人的安全语义层”**与**“ROS 2 实时性的定量证据层”**，而非控制算法本身。

1. **通用机器人安全的“发起授权”维度（initiation authorization）**——[30] 明确指出这是被 motion safety / dialogue safety 遮蔽的空白：机器人是否应当执行第一个不可逆社会动作，目前既无形式化定义也无评测方法[30]。这是**没人做**的方向，且与 ISO 10218 传统工业安全框架不重叠（后者关注力/速度/间距，不关注社会性发起行为）[25][30][35]。
2. **标准合规的可执行化工具**——[25][35] 系统对比了 2011 与 2025 版条款并要求整合 TS 15066，但本批证据中**不存在**任何把新版条款转化为可执行检查项（测试用例、仿真场景库、认证 checklist）的工作[25][35]。这是标准落地与工程实践之间的空白，`> 待核实`（无法确认是否已有人在做）。
3. **ROS 2 实时性的独立第三方基准**——仅 [23] 一篇、单机器人形态、单期刊的评测，缺乏跨 DDS 实现（Fast DDS / Cyclone DDS / rmw_zenoh）的横向对比与可复现实验脚本[23]。该空白使得所有“ROS 2 够不够实时”的论断目前都无法被核查。
4. **全身人形控制的多任务/多本体验证**——[21][22] 各自只覆盖单一任务（羽毛球 / 通用全身控制），未在多个本体上验证，也未见公开 benchmark 或权重[21][22]。`> 待核实`：无法判断是否存在未检索到的公开评测。

---

## 4. 瓶颈与拐点（Bottleneck & Inflection）

**一句话增量判断**：本周期最明确的**拐点信号是“标准拐点”而非“算法拐点”**——ISO 10218 从 2011 版切换到 2025 版并整合 TS 15066，构成一次全行业合规重写窗口[25][35]；算法侧的瓶颈（实时性、仿真到真机归因、安全评测缺失）在本批证据中均未显示被突破。

| 瓶颈 | 证据 | 是否临近拐点 | 拐点信号（可观测） |
|---|---|---|---|
| 标准合规成本 | ISO 10218-1/2 2011→2025 + TS 15066 整合[25][35] | **是**（已发生） | 2026–2027 出现第三方认证机构指南更新、开源合规检查工具 |
| 通用机器人安全评测缺失 | [30] 指出 initiation 维度无定义无评测[30] | 否，`> 待核实` | 出现 ≥2 个独立安全 benchmark |
| ROS 2 实时性证据薄弱 | 仅 [23] 单篇、单形态[23] | 否 | 出现跨 DDS 实现的公开对比与复现脚本 |
| 仿真到真机的归因困难 | [22] 专门消融 DR 的作用[22] | 部分（研究已开始拆解归因） | 出现跨团队复用同一 DR 消融协议 |
| 数据/算力 | 本批证据零覆盖 | `> 待核实` | — |

**判断**：[21][22] 显示人形控制的性能提升仍主要来自训练范式（课程退火、域随机化、扩散策略）而非新硬件，说明该方向当前处于**“方法工程化”阶段而非“能力跃迁”阶段**[21][22]。

---

## 5. 社会·政策·国际（Society, Policy & Geopolitics）

**一句话增量判断**：本批证据唯一可确证的政策级变化是**工业机器人功能安全标准的版本换代**[25][35]；地缘政治、出口管制、供应链、劳动影响在本批证据中**零覆盖**，`> 待核实`。

- **ISO 10218-1/2:2011 → 2025 的条款级变化 + ISO/TS 15066 整合**：论文对两版做比较分析，覆盖协作机器人（collaborative robotics）带来的新交互范式对安全要求的冲击[25][35]。
  - 热度：`> 待核实`[25][35]；权威：**A 级**，同行评审期刊 *Results in Engineering*[35]；关注度：**中**（arXiv + 期刊双发布）[25][35]；推荐度 **★★★★☆**——合规、产品认证、出海准入的必读基线[25][35]。
- **功能安全与网络安全的融合**：[27] 讨论智能电动汽车中 cybersecurity 与 functional safety 的协同发展[27]。**限定说明**：该文对象是 SEV 而非机器人，仅可作为“安全工程范式正在从纯功能安全扩展到 cyber-physical 安全”的**相邻领域信号**，不能直接外推到机器人法规[27]。
  - 热度 `> 待核实`；权威：arXiv eess.SY 预印本（2025-11），评审状态 `> 待核实`[27]；关注度 **低**；推荐度 **★★☆☆☆**（相关但非本领域）[27]。
- **社会性安全尚未进入标准视野**：[30] 指出通用机器人的“首次社会动作”缺乏授权机制，而现行工业安全框架（力/速度/间距）不覆盖此类风险[25][30][35]。这是**监管空白**而非监管失败。
- **地缘/供应链/出口管制/劳动影响**：零覆盖，`> 待核实`，本报告不作陈述。

---

## 6. 资本与生态（Capital & Ecosystem）

**一句话增量判断**：**本周期（就本批证据而言）无显著变化可报告**——融资、并购、人才流动、公司格局四条线**全部零覆盖**，一律 `> 待核实`。任何关于“人形机器人融资热度”“ROS 2 生态被某厂商主导”的表述在本批证据下都无法成立。

可观测的**生态侧弱信号**（非资本信号）：

- **预印本迭代活跃度**：[21] 已至 v4 修订（arXiv 2511.11218v4）[21]，[30] 已至 v2（2607.07420v2）[30]，[32] 为 v1（2511.20811v1）[32] —— 说明相关团队在持续迭代，但不构成资本或采用率证据。
- **学术—标准耦合**：[25] 以 arXiv 预印本形式先行、[35] 随后进入同行评审期刊，反映标准解读类工作正在被正式学术渠道接收[25][35]。
- **ROS 2 生态的学术渗透**：Micro-ROS 被纳入移动机器人实时控制评测[23]，说明“ROS 2 + 微控制器”的栈组合已进入可发表研究的视野，但**无采用率、下载量、star 数据**支撑生态规模判断，`> 待核实`[23]。

---

## 7. 信号与预测（Signals & Forecast）

**一句话增量判断**：未来 6–18 个月最可检验的信号来自**标准合规工具化**与**通用机器人安全评测**两条线，而非控制算法 SOTA。

### 可证伪假设

| 编号 | 假设（可证伪） | 依据链 | 置信度 | 检验方式 |
|---|---|---|---|---|
| H1 [P] | 到 **2027-06**，若出现 ≥2 个**独立**的通用机器人安全评测基准，且其中至少 1 个覆盖 “initiation authorization” 维度，则判定 [30] 提出的维度被社区采纳 | [30] 明确将该维度定义为“missing”；当前无评测 → 若被采纳必先出现基准 | 中低 | 检索 benchmark/leaderboard 与引用 [30] 的后续工作 |
| H2 [P] | ISO 10218:2025 落地后 18 个月内，出现至少 1 个**开源合规检查/测试用例工具链**（覆盖 speed & separation monitoring 或 PFL） | [25][35] 完成条款对比但未提供可执行检查项 → 工程界必然补位 | 中 | 检索 GitHub 上 ISO 10218 / TS 15066 相关仓库与认证机构公告 |
| H3 [P] | 到 **2027-10**，若跨 DDS 实现（Fast DDS / Cyclone DDS / rmw_zenoh）的**公开、可复现**定量对比仍 <3 篇，则判定“ROS 2 实时性”瓶颈未被社区解决 | 当前仅 [23] 单篇单形态评测[23] → 证据密度是瓶颈是否被攻克的代理指标 | 中 | 统计 cs.RO/会议论文与公开 benchmark 数量 |
| H4 [P] | 到 **2027-10**，若 [21][22] 路线（RL 课程 / diffusion + DR）仍无**跨团队、跨本体**的第三方复现，则“人形全身控制已达可复现 SOTA”这一说法不成立 | [21][22] 均为单团队单任务，无公开权重/基准[21][22] | 中 | 检索是否出现复用其协议或权重的独立工作 |
| H5 [P] | 若 2026–2027 年 MPC+RL 混合控制、可微运动学在真机上的第三方复现证据仍为零，则本报告对该两项的“SOTA 变动”判定维持 `> 待核实` | q1 证据池零覆盖该类材料 | 低（依据不足） | 定向补检 cs.RO + ICRA/CoRL/RSS 2026 |

### Watchlist（值得持续关注）

| 对象 | 类型 | 关注理由 | 证据 |
|---|---|---|---|
| ISO 10218-1/2:2025 + ISO/TS 15066 整合 | 标准 | 全行业合规重写窗口，直接影响产品认证与出海 | [25][35] |
| Initiation safety / generalist-robot safety | 概念+空白 | 明确指出未被覆盖的安全维度，蓝海 | [30] |
| Programmable light curtains / conformal safety monitoring | 方法 | 运行时安全保障的两条可落地技术路径 | [31][32] |
| ROS 2 + Micro-ROS 实时分布式控制 | 工程栈 | 唯一可核查的 ROS 2 实时性实证，但为孤证 | [23] |
| Annealed RL curriculum（人形羽毛球） | 方法 | 高动态全身控制的最新范式信号 | [21] |
| Domain randomization × diffusion policy（人形全身） | 方法 | 直接回答“提升来自数据还是架构”的归因问题 | [22] |

### 不确定性说明

- **[R] 传闻类**：本报告未采信任何传闻；候选池中无 rumor 级材料。
- **[Debated]**：本批证据未出现同一事实的多方冲突陈述，故无争议条目可列。
- **最大不确定性**：q1、q2 的证据池**完全失效**（4/4 与 3/3 条目离题）[1][5][7][13][14][16][18]，这意味着本报告在“控制算法 SOTA”与“工具链版本演进”两大核心问题上**不具备结论能力**。建议以 cs.RO + 官方 release notes + GitHub 仓库为主源重新召回后，再对本报告第 1、2、4 章做增补。

---

## 附：结构化表格

### 表 A：最新进展（近 1–2 年，2024–2026）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Humanoid Whole-Body Badminton via an Annealed RL Curriculum | 2025-11（v4） | 候选块未提供 | `> 待核实` | arXiv 预印本 cs.RO，评审状态`> 待核实` | 低（无引用/榜单信号） | ★★★☆☆ | http://arxiv.org/abs/2511.11218v4 | 高动态全身人形控制，课程退火[21] |
| The Role of Domain Randomization in Training Diffusion Policies for Whole-Body Humanoid Control | 2024-11 | 候选块未提供 | `> 待核实` | arXiv 预印本 cs.RO | 低 | ★★★☆☆ | http://arxiv.org/abs/2411.01349v1 | 扩散策略 + DR 消融，回答归因问题[22] |
| Performance Evaluation of ROS2 and Micro-ROS for Real-Time Distributed Control of Omnidirectional Mobile Robots | `> 待核实`（v3(1)） | 候选块未提供 | `> 待核实` | 期刊 *Injei*，有 DOI；影响力`> 待核实` | 低 | ★★☆☆☆ | https://doi.org/10.61961/injei.v3i1.87 | 唯一 ROS 2 实时性实证[23] |
| Initiation Safety: A Missing Dimension in Generalist-Robot Safety | 2026-07（v2） | 候选块未提供 | `> 待核实` | arXiv 预印本 cs.RO | 低 | ★★★☆☆ | http://arxiv.org/abs/2607.07420v2 | 提出通用机器人安全第三维度[30] |
| Robot Safety Monitoring using Programmable Light Curtains | 2024-04 | 候选块未提供 | `> 待核实` | arXiv 预印本 cs.RO | 低 | ★★☆☆☆ | http://arxiv.org/abs/2404.03556v1 | 可编程光幕运行时安全[31] |
| Conformal Safety Monitoring for Flight Testing | 2025-11 | 候选块未提供 | `> 待核实` | arXiv 预印本 | 低 | ★★☆☆☆ | http://arxiv.org/abs/2511.20811v1 | conformal prediction 安全监控[32] |
| Evolution of Safety Requirements in Industrial Robotics（ISO 10218-1/2 2011 vs 2025） | 2026-02（arXiv）/ 2026（期刊） | 候选块未提供 | `> 待核实` | **A 级**：*Results in Engineering* 同行评审 | 中（arXiv+期刊双发布） | ★★★★☆ | http://arxiv.org/abs/2602.17822v1 ；https://doi.org/10.1016/j.rineng.2026.110486 | 标准换代的条款级对比[25][35] |

### 表 B：经典与奠基性工作（>2 年，仅限本批证据内可核查者）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| High-level programming and control for industrial robotics: hand-held accelerometer-based input device for gesture and posture recognition | 2013-09 | 候选块未提供 | `> 待核实` | arXiv 预印本 | 低 | ★★☆☆☆ | http://arxiv.org/abs/1309.2093v1 | 工业机器人高层编程/示教接口的早期工作，可作为“编程范式演进”的历史基线[28] |
| One-Shot Reinforcement Learning for Robot Navigation with Interactive Replay | 2017-11（v2） | 候选块未提供 | `> 待核实` | arXiv 预印本 | 低 | ★★☆☆☆ | http://arxiv.org/abs/1711.10137v2 | RL 导航的早期范式，可作为“RL 进入机器人控制”的历史基线[24] |
| Real time state monitoring and fault diagnosis system for motor based on LabVIEW | 2018-06 | 候选块未提供 | `> 待核实` | arXiv 预印本 | 低 | ★☆☆☆☆ | http://arxiv.org/abs/1806.09998v1 | 电机状态监测/故障诊断的工程实现，与 ros2_control 的 `hardware_interface` 诊断思路相邻[34] |

> **本表的重要缺口**：Pinocchio、Drake、CasADi、Crocoddyl、OCS2、Ruckig、MoveIt 2、Nav2、OMPL、MuJoCo/MJX 的**原始论文、版本演进与官方文档**在本批证据中零覆盖，`> 待核实`，故不列入表格，也不提供任何未经核实的链接。

### 表 C：开源项目 / 工程栈

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| ROS 2 + Micro-ROS（作为被评测对象） | `> 待核实` | 候选块未提供 | `> 待核实`（无 star/下载数据） | 期刊论文 [23] 提供第三方评测而非官方文档 | 低 | ★★☆☆☆ | https://doi.org/10.61961/injei.v3i1.87 | 仅能确认“被用于全向移动机器人实时分布式控制评测”，不能确认其版本、发行版与实时性指标[23] |
| ros2_control / MoveIt 2 / Nav2 / Pinocchio / Drake / CasADi / Crocoddyl / OCS2 / Ruckig / OMPL / MuJoCo / MJX | — | — | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实`（本批证据未提供任何官方仓库链接） | **零覆盖**：无法给出定位、版本号或 star 数，禁止据记忆补写 |

### 表 D：数据集与基准

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| 全身人形控制评测（[21][22] 各自自定义任务） | 2024–2025 | 候选块未提供 | `> 待核实` | 无公开 benchmark / 无公开权重 | 低 | ★★☆☆☆ | `> 待核实` | 两文均未使用公共基准，**无法横向比较**，不构成 “SOTA 榜单”[21][22] |
| Generalist-robot safety benchmark（含 initiation authorization 维度） | — | — | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | [30] 指出该维度**尚不存在**评测，属空白而非已有基准[30] |
| ROS 2 / DDS 实时性基准（跨实现横向对比） | — | — | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | 仅 [23] 单篇单形态评测，无公开基准[23] |

---

## 参考来源

[1] Overview of AuTexTification at IberLEF 2023 — http://arxiv.org/abs/2309.11285v1
[2] NTU-NPU System for Voice Privacy 2024 Challenge — http://arxiv.org/abs/2410.02371v1
[3] Discovery Opportunities with Gravitational Waves -- TASI 2024 Lecture Notes — http://arxiv.org/abs/2409.08956v1
[4] Strategies to Harness the Transformers' Potential: UNSL at eRisk 2023 — http://arxiv.org/abs/2310.19970v1
[5] PINOCCHIO and the hierarchical build-up of dark matter haloes — http://arxiv.org/abs/astro-ph/0109324v1
[6] WVOQ at SemEval-2021 Task 6: BART for Span Detection and Classification — http://arxiv.org/abs/2107.05467v1
[7] The Relativistic Elasticity of Rigid Bodies — http://arxiv.org/abs/physics/0307019v3
[8] MAGIC and MWL monitoring of the blazar TXS 0506+056 in the 2018/2019 season — http://arxiv.org/abs/1909.04938v1
[9] MIPT-NSU-UTMN at SemEval-2021 Task 5 — http://arxiv.org/abs/2104.04739v1
[10] Handshakes AI Research at CASE 2021 Task 1 — http://arxiv.org/abs/2110.15599v1
[11] Overview and Results: CL-SciSumm Shared Task 2019 — http://arxiv.org/abs/1907.09854v1
[12] Overview of ADoBo 2021 — http://arxiv.org/abs/2110.15682v1
[13] VQualA 2025 Challenge on Engagement Prediction for Short Videos — http://arxiv.org/abs/2509.02969v1
[14] TRUST 2025: SCRITA and RTSS @ RO-MAN 2025 — http://arxiv.org/abs/2509.11402v1
[15] NTIRE 2025 Challenge on Image Super-Resolution (x4) — http://arxiv.org/abs/2504.14582v3
[16] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1
[17] Fluid Antenna System: New Insights on Outage Probability and Diversity Gain — http://arxiv.org/abs/2301.00073v2
[18] AI Wizards at CheckThat! 2025 — http://arxiv.org/abs/2507.11764v1
[19] TDCOSMO 2025: Cosmological constraints from strong lensing time delays — http://arxiv.org/abs/2506.03023v4
[20] Event-Enriched Image Analysis Grand Challenge at ACM Multimedia 2025 — http://arxiv.org/abs/2508.18904v1
[21] Humanoid Whole-Body Badminton via an Annealed Reinforcement Learning Curriculum — http://arxiv.org/abs/2511.11218v4
[22] The Role of Domain Randomization in Training Diffusion Policies for Whole-Body Humanoid Control — http://arxiv.org/abs/2411.01349v1
[23] Performance Evaluation of ROS2 and Micro-ROS for Real-Time Distributed Control of Omnidirectional Mobile Robots — https://doi.org/10.61961/injei.v3i1.87
[24] One-Shot Reinforcement Learning for Robot Navigation with Interactive Replay — http://arxiv.org/abs/1711.10137v2
[25] Evolution of Safety Requirements in Industrial Robotics (arXiv 版) — http://arxiv.org/abs/2602.17822v1
[26] Laser pointer prohibition: improving safety or driving misclassification — http://arxiv.org/abs/1406.4924v1
[27] Synergistic Development of Cybersecurity and Functional Safety for Smart Electric Vehicles — http://arxiv.org/abs/2511.07713v1
[28] High-level programming and control for industrial robotics: using a hand-held accelerometer-based input device — http://arxiv.org/abs/1309.2093v1
[29] Safety in Batches? Understanding and Mitigating Safety Failures in Batch Prompting — http://arxiv.org/abs/2608.02681v2
[30] Initiation Safety: A Missing Dimension in Generalist-Robot Safety — http://arxiv.org/abs/2607.07420v2
[31] Robot Safety Monitoring using Programmable Light Curtains — http://arxiv.org/abs/2404.03556v1
[32] Conformal Safety Monitoring for Flight Testing — http://arxiv.org/abs/2511.20811v1
[33] Real-Time Service Subscription and Adaptive Offloading Control in Vehicular Edge Computing — http://arxiv.org/abs/2512.14002v1
[34] Real time state monitoring and fault diagnosis system for motor based on LabVIEW — http://arxiv.org/abs/1806.09998v1
[35] Evolution of safety requirements in industrial robotics (期刊版, *Results in Engineering*) — https://doi.org/10.1016/j.rineng.2026.110486

---

*Generated by research-bot · topic=`机器人运动学控制与-ros-2` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`deepseek-v4-flash` · sources=35 · duration=158s · 2026-10-20T22:25:14+00:00*
