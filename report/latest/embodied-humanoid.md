# 具身智能 · 人形与腿足运动（Humanoid & Legged Locomotion）调研报告

**日期**：2026-10-04（UTC）｜**领域**：具身智能 / 腿足与人形运动控制｜**检索源**：共 118 条候选来源编号（[1]–[118]），其中与主题直接相关约 60 条，另含种子资源（AMASS、LAFAN1、legged_gym、unitree_rl_gym、ProtoMotions、IsaacLab 仓库）

**证据强度声明（重要）**：本批候选块绝大多数只提供标题 + 摘要片段，**未提供引用数（citations）、GitHub star、下载量或榜单排名**。因此下文四类证据中的**热度证据**大量标注 `> 待核实`，**关注度**仅能依据作者机构、venue 与主题贴合度作弱判断。同时，候选集中存在明显检索噪声（与腿足/人形运动无关），包括 [21][22][39][43][55][57][58][59][60][61][62][64][65][66][67][68][69][82][83][99][101][103][104][105][109][114][115][117][118]，本报告不予采用（**经剔除处理后，q5/q6 子问题在候选集中返回的多数条目为噪声，其结论主要依赖人工补检的来源编号**）。

---

## 摘要（Executive Summary）

1. **学习式范式已成为人形/腿足运动的主流路线**：从 2023 年真机人形 RL 行走 [81]，到 2024–2025 年统一全身控制器 HOVER [72]、统一通用全身控制器 [73]、跨本体蒸馏 [71]，范式从"单技能策略"走向"多模式统一控制器 + 跨本体迁移"。
2. **sim2real 的关键技术组合已相对收敛**：域随机化 [2]、教师-学生特权信息蒸馏、参考运动先验（AMASS/LAFAN1 重定向）、以及 ASAP 式"仿真-真机物理对齐"两阶段训练 [80]。工程侧出现把训练时间压到分钟级的 off-policy 配方 [108]，以及 Isaac Sim + Isaac Lab 的零样本真机部署案例 [107]、Humanoid-Gym 零样本迁移 [112]。
3. **敏捷与恢复能力成为新的能力分界线**：parkour [40][45]、高速安全避障 [41]、全身起立/跌倒恢复 [46][47]、羽毛球等动态物体交互 [1]、非足部接触运动 [100]。
4. **工程栈层面，Isaac Lab [106] 是本批证据中最明确的 GPU 并行训练基座**，配合 Isaac Sim [107]；MuJoCo Playground [56] 提供另一条 GPU 加速 + sim2real 路线；Humanoid-Gym [112]、legged_gym、unitree_rl_gym（种子）面向具体硬件。
5. **评测与开放问题**：HumanoidBench [49] 是当前少见的全身人形基准，并有 MuJoCo MPC 基线对照 [50]，支撑"RL vs MPC"的可比评测；但**跨本体、跨方法、真机耐久**的统一评测仍缺失，且 ROS2 集成在本批证据中**完全空白**（仅有 2018 年的 NimbRo-OP ROS 框架 [6]），属最大工程缺口。

---

## 一、关键前沿进展（近 1–2 年）

### 1.1 时间线（按 arXiv 首次公开时间排序）

| 时间 | 工作 | 一句话贡献 | 引用 |
|---|---|---|---|
| 2023-03 | Real-World Humanoid Locomotion with RL | 真机人形 RL 行走的早期里程碑，奠定"仿真训练 → 真机零样本"路线 | [81] |
| 2024-03 | H2O | 人-人形实时全身遥操作（IROS 2024 种子资源） | [76] |
| 2024-05 | Hierarchical World Models as Visual Whole-Body Humanoid Controllers | 用分层世界模型做**视觉**全身人形控制 | [7] |
| 2024-06 | OmniH2O / HumanPlus | 通用灵巧人-人形全身遥操作与学习 [75]；人类动作影子模仿 [110] | [75][110] |
| 2024-10 | HOVER | 面向人形的多模式**神经全身控制器**（统一多种运动/操作模式） | [72] |
| 2024-11 | Domain Randomization for Diffusion Policies in Whole-Body Humanoid Control | 系统评估域随机化在扩散策略全身控制中的作用 | [2] |
| 2025-02 | ASAP / 统一通用全身控制器 / 起立控制 / STRIDE | 仿真-真机物理对齐 [80]；统一运动-操作控制器 [73]；多姿态起立 [47]；奖励自动化设计 [98] | [80][73][47][98] |
| 2025-02 | 真机人形起立策略 | 真实世界人形从跌倒姿态恢复 | [46] |
| 2025-05 | TWIST | 遥操作全身模仿系统 | [77] |
| 2025-07 | UniTracker | 三阶段通用全身运动追踪器 | [70] |
| 2025-09 | KungfuBot2 | 面向全身控制的多样运动技能学习 | [74] |
| 2025-10/11 | ATRos / 羽毛球全身控制 | 轮足能效敏捷运动 [29]；退火 RL 课程实现动态物体交互 [1] | [29][1] |
| 2025-12 | Learning Sim-to-Real Humanoid Locomotion in 15 Minutes | off-policy RL 的快速 sim2real 配方 | [108] |
| 2026-01 | Locomotion Beyond Feet | 物理关键帧动画 + RL，覆盖非足部接触运动 | [100] |
| 2026-02 | HMI / 具身感知蒸馏 / CLOT | 免机器人演示的全身操作 [3]；跨本体统一 WBC [71]；闭环全局运动追踪遥操作 [79] | [3][71][79] |
| 2026-05 | Active Spatial Brain / 神经形态 RL | 空间感知全身操作 [5]；四足神经形态在线适应 [36] | [5][36] |
| 2026-07 | 小型人形遥操作 / Isaac Sim-to-Real | VR+RL 分层栈下沉到低成本平台 [48]；Isaac 栈四足零样本真机 [107] | [48][107] |
| 2026-09 | 行星探测四足 | 本体-外感联合地形建图 | [34] |

**证据四轴（代表性节点）**

- HOVER [72]：热度 `> 待核实`（候选块无引用数）；权威=arXiv cs.RO 预印本（**非**同行评审确认）；关注度=中（作为统一全身控制器的代表被后续工作反复对照，但本批无量化热度信号）；推荐度 ★★★★★（"统一多模式全身控制器"是理解 2025 年后人形控制架构的关键起点）。
- ASAP [80]：热度 `> 待核实`；权威=arXiv 预印本 cs.RO（v3）；关注度=高（"仿真-真机物理对齐"被本批多个子问题反复引为关键范式，且标题直指敏捷全身技能）；推荐度 ★★★★★（关注 sim2real 归因问题必读）。
- OmniH2O [75]：热度 `> 待核实`；权威=arXiv 预印本；关注度=高（通用灵巧人-人形遥操作的代表工作，与 [76][77] 构成遥操作主线）；推荐度 ★★★★★。
- Learning Sim-to-Real Humanoid Locomotion in 15 Minutes [108]：热度 `> 待核实`（标题指标具传播性但无引用/star 数据）；权威=arXiv 预印本 cs.RO（2025-12-01，未标注会议）；关注度=中；推荐度 ★★★★☆（工程配方价值高，**分钟级训练时间需在原文实验设置下核实**）。
- 羽毛球全身控制 [1]：热度 `> 待核实`；权威=arXiv cs.RO v4；关注度=中（"动态移动物体交互"是新能力维度）；推荐度 ★★★☆☆（v4 版本提示持续修订，但缺同行评审与真机量化信息）。

---

## 二、学习式 locomotion 与全身控制（WBC）

**主线判断：2024 年后，"全身控制"从"分层 MPC+WBC 的经典结构"转向"单一神经网络统一输出全身关节动作，并用多种运动模式/参考运动调制"** [72][73][70]。

- **多模式统一控制器**：HOVER [72] 主张一个神经全身控制器覆盖多种运动与操作模式；[73] 提出"统一且通用的全身控制器"面向多样运动。二者共同回答了"能否一个策略替代多个技能策略"的问题。证据四轴：热度 `> 待核实`；权威=arXiv 预印本 cs.RO（**无** A 级同行评审确认）；关注度=高（是本批 q1 中被重复检索到的核心簇）；推荐度 ★★★★★。
- **通用运动追踪**：UniTracker [70] 用三阶段训练框架实现跨人类行为的鲁棒运动追踪，把"模仿一段参考动作"扩展为"通用运动追踪器"。热度 `> 待核实`；权威=arXiv cs.RO v3；关注度=中；推荐度 ★★★★☆。
- **跨本体统一控制**：Embodiment-Aware Generalist Specialist Distillation [71] 明确指出"多数 RL 全身控制器只针对单一本体，动力学、自由度与运动学拓扑差异阻碍单一策略控制多种人形"，并提出通用-专家蒸馏。这是**跨本体泛化**这一开放问题的直接证据。热度 `> 待核实`；权威=arXiv cs.RO v2（2026）；关注度=中（2026 新作，尚无独立复现）；推荐度 ★★★★☆。
- **技能库式控制**：KungfuBot2 [74] 学习多样运动技能以支撑全身控制；Locomotion Beyond Feet [100] 用物理关键帧动画 + RL 覆盖非足部接触，关键帧"具身相关、可在仿真或硬件上快速验证"。热度 `> 待核实`；权威=[100] 作者含 Shuran Song、C. Karen Liu 等知名学者，但候选块未标注会议 → 权威中高、非 A 级确认；关注度=中；推荐度 ★★★★☆（[100]）。
- **视觉 + 世界模型切入全身控制**：[7] 用分层世界模型做视觉全身人形控制器，提示"视觉全身控制"是相较本体感知控制的新前沿。热度 `> 待核实`；权威=arXiv cs.RO v3；关注度=中；推荐度 ★★★★☆。
- **全身操作（loco-manipulation）**：HMI [3] 从"无机器人演示"学习全身操作，直指遥操作/视觉 sim2real 的硬件物流与奖励工程瓶颈；[5] 用"空间脑 + 可泛化动作小脑"处理空间感知全身操作；HumanPlus [110] 用人类数据做影子模仿。热度均 `> 待核实`；权威=arXiv 预印本（[3][5] 为 2026 年新预印本）；关注度=中；推荐度 ★★★☆☆–★★★★☆。
- **小平台下沉**：[48] 指出"VR 遥操作上身 + RL 平衡下身"的分层栈此前多局限于昂贵全尺寸机器人，作者将其带到小型人形。热度 `> 待核实`；权威=arXiv 预印本 cs.RO（2026-07）；关注度=中；推荐度 ★★★☆☆。

> **待核实**：上述工作在本批证据中**均无引用数、无榜单成绩、无第三方复现报告**；"统一控制器是否真的优于 MPC+WBC 分层基线"在本批证据中缺少同硬件同任务的对照数字。

---

## 三、sim2real 与地形适应

**技术组件在本批证据中的分布：**

1. **域随机化**：[2] 专门研究域随机化在全身人形扩散策略训练中的作用——这是少数把"域随机化"本身当作研究对象的工作。热度 `> 待核实`；权威=arXiv cs.RO（2024-11）；关注度=中；推荐度 ★★★★☆（想理解 DR 收益边界者优先）。
2. **快速训练配方与 off-policy RL**：[108] 指出"大规模并行仿真已把 RL 训练从数天压到数分钟，但人形 sim2real 仍困难（高维 + 域随机化）"，提出基于 off-policy 的实用配方。热度 `> 待核实`；权威=arXiv 预印本 cs.RO（2025-12，未标注会议）；关注度=中；推荐度 ★★★★☆（**配方需在原文设置下复现核实**）。
3. **仿真栈驱动的零样本迁移**：[107] 用 Isaac Sim + Isaac Lab 训练，在 Unitree Go1 上实现零样本 sim2real，同时承认"仿真表现好但部署时仍存在 sim2real gap"。热度 `> 待核实`；权威=arXiv 预印本 cs.RO（2026-07）；关注度=中；推荐度 ★★★★☆。另有 Humanoid-Gym [112] 面向人形零样本 sim2real。
4. **内部模型 / 特权信息路线**：[32] Hybrid Internal Model 用"模拟机器人响应"学习敏捷腿足运动，是"隐式系统辨识替代显式域随机化"的代表。热度 `> 待核实`；权威=arXiv cs.RO v3；关注度=中高（被广泛视作特权信息路线的代表）；推荐度 ★★★★☆。
5. **感知式/本体感知式地形适应**：[30] 地形感知运动综述性工作；[37] 用本体感知实现地形感知安全运动；[33] 非刚性地形四足 RL；[38] 塌陷地形承载能力评估；[35][34] 行星永久阴影区与行星探测中的本体感知地形建图。热度均 `> 待核实`；权威=arXiv cs.RO 预印本（[34] 为 2026-09 最新）；关注度=中；推荐度 ★★★☆☆–★★★★☆（[37][38] 对"安全性"议题价值更高）。
6. **在线适应与神经形态**：[36] 指出主流 RL 控制器"离线训练、部署为固定策略，限制了对地形变化、负载变化、执行器磨损的适应"，提出神经形态 RL。热度 `> 待核实`；权威=arXiv cs.NE v2（2026-05）；关注度=中；推荐度 ★★★★☆（直指"部署后不退化"这一真机耐久问题）。
7. **真机在线微调**：[31] "Legged Robots that Keep on Learning" 提出真机微调运动策略，是"离线→在线"过渡的早期奠基。热度 `> 待核实`；权威=arXiv（2021）；关注度=中；推荐度 ★★★★☆。

**争议点（sim2real gap 归因）**：[84] 以章节形式系统剖析"仿真的诅咒"，把 sim2real 迁移问题放在多种控制架构背景下讨论——这是本批证据中**唯一**专门为"归因：数据/架构/仿真保真度"提供结构化讨论的来源。热度 `> 待核实`；权威=arXiv cs.RO（2025-11，章节体裁，非明确同行评审）；关注度=中；推荐度 ★★★★★（归因讨论的首选入口）。相关背景性材料还有 R:SS 2020 sim2real 工作坊总结 [116]。sim2real 的跨域通用性讨论见 [113]（视觉编码器预训练）与 [114][115][118]（**与腿足运动弱相关，仅作背景**）。

> **待核实**：[107][108][112] 的"零样本/分钟级"宣称均**缺少第三方复现**与统一硬件口径（GPU 型号、显存、仿真步长、任务数），无法横向比较。

---

## 四、敏捷动作、跑跳与恢复

- **跑酷（parkour）**：[40] 四足机器人跑酷学习；[45] 人形跑酷学习。热度 `> 待核实`；权威=arXiv cs.RO 预印本（[40] v2, 2023-09；[45] v2, 2024-06）；关注度=高（parkour 是"敏捷 + 感知"的标杆任务，且是本批 q2 的核心）；推荐度 ★★★★★。
- **高速避障与安全**：[41] "Agile But Safe" 学习无碰撞高速腿足运动；安全控制侧有输入受限 CBF [15] 与机会约束 MPC 的安全 RL [86]。热度 `> 待核实`；权威=arXiv（[41] cs.RO v3）；关注度=中高（安全性是可解释性/认证的关键）；推荐度 ★★★★☆。
- **自然/野外敏捷运动**：[25] Learning Robust, Agile, Natural Legged Locomotion Skills in the Wild。热度 `> 待核实`；权威=arXiv cs.RO v3；关注度=中；推荐度 ★★★★☆。
- **技能发现与最优控制对照**：[42] 用无监督技能发现作为敏捷运动的探索机制；[44] 从最优控制学习敏捷路径。这表明"RL 探索"与"最优控制先验"正在融合。热度 `> 待核实`；权威=arXiv cs.RO；关注度=中；推荐度 ★★★☆☆。
- **跌倒恢复 / 起立**：[46] 真实世界人形 get-up 策略；[47] 跨多种姿态的起立控制。热度 `> 待核实`；权威=arXiv cs.RO（均 2025-02）；关注度=高（"跌倒恢复"被认为是真机可用性的硬门槛，本批检索在 q4/q1 多次命中）；推荐度 ★★★★☆。
- **动态物体交互**：[1] 羽毛球全身控制（退火 RL 课程）。热度 `> 待核实`；权威=arXiv cs.RO v4；关注度=中；推荐度 ★★★☆☆。
- **非足部接触与非常规运动**：[100] Locomotion Beyond Feet。热度 `> 待核实`；权威=知名作者团队，未标注会议（中高）；关注度=中；推荐度 ★★★★☆。
- **轮足混合与负载**：ATRos [29] 学习能效敏捷轮足运动；[85] 轮式人形未知负载的平衡点估计（real-to-sim 适应）。热度 `> 待核实`；权威=arXiv cs.RO；关注度=中；推荐度 ★★★☆☆。

> **待核实**：本节所有"敏捷"宣称的量化口径（成功率、速度、地形难度分级、真机 vs 仿真）在候选块中**均未给出**；不得据此下"已解决"的结论。

---

## 五、遥操作与动作先验

**（1）遥操作主线**：OmniH2O [75]（通用灵巧人-人形全身遥操作）→ H2O [76]（实时全身遥操作，IROS 2024 种子资源）→ TWIST [77]（遥操作全身模仿系统）→ CLOT [79]（闭环全局运动追踪，2026-02）→ CHILD [4]（关节级全身遥操作，2025-08）→ HMI [3]（免机器人演示的全身操作，2026-02）→ 小型人形 VR+RL 分层遥操作 [48]。热度均 `> 待核实`；权威=arXiv 预印本（[76] 为 IROS 2024 正式发表，权威等级相对更高）；关注度=高（本批 q1/q5 多次重复命中该簇）；推荐度 ★★★★☆–★★★★★。

**（2）动作重定向与全身几何**：[8] Whole-Body Geometric Retargeting 提供人→人形的几何重定向基础；[9] 全身操作空间控制（point-foot 弹性双足）是 WBC 经典对照；[110] HumanPlus 用人类数据做影子模仿。热度 `> 待核实`；权威=[8] arXiv（2019）、[9] arXiv（2015）早期预印本；关注度=中；推荐度 ★★★★☆（理解"为什么现在用 RL 而不用纯几何重定向"的关键）。

**（3）动作先验数据**：AMASS（人体动捕）与 LAFAN1（动画数据集）为本领域常用的动作先验来源（种子资源，链接见第七节）。**NVIDIA ProtoMotions** 提供人形物理仿真运动工具（种子资源）。热度（AMASS/LAFAN1 的下载量、引用数）在本批证据中 `> 待核实`；权威=官方数据集主页（B 级）；关注度=高（人形运动先验的标准来源，被本批多篇工作以"参考动作"形式隐含依赖）；推荐度 ★★★★★。

**（4）参考轨迹工程化**：[100] 把"物理关键帧动画"作为技能编码载体，并强调关键帧"具身相关且在仿真或硬件上可快速验证"，是"动作先验 → RL 可训练目标"的工程化范式。热度 `> 待核实`；权威=中高（知名作者，未标注会议）；关注度=中；推荐度 ★★★★☆。

> **待核实**：遥操作系统的**延迟、穿戴设备、数据规模、是否需要动捕**等工程细节在候选块中均未给出；跨系统可比性无法评估。

---

## 六、经典与奠基性工作

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Learning Quadrupedal Locomotion over Challenging Terrain | 2020 | Science Robotics（ETH） | `> 待核实`（候选块无引用数） | A（同行评审期刊） | 高（领域公认奠基，本批未给量化热度） | ★★★★★ | https://www.science.org/doi/10.1126/scirobotics.abc5986 | 学习式腿足运动奠基（种子资源） |
| Learning Agile and Dynamic Motor Skills for Legged Robots (ANYmal) | 2019 | Science Robotics（ETH） | `> 待核实` | A（同行评审期刊） | 高 | ★★★★★ | https://www.science.org/doi/10.1126/scirobotics.aau5872 | sim2real 强化学习奠基（种子资源） |
| Learning Human-to-Humanoid Real-Time Whole-Body Teleoperation (H2O) | 2024 | IROS | `> 待核实` | A（IROS 2024，种子资源标注） | 高（遥操作主线起点） | ★★★★★ | https://arxiv.org/abs/2403.04436 | 人形全身实时遥操作 [76] |
| Real-World Humanoid Locomotion with Reinforcement Learning | 2023 | arXiv cs.RO（v2） | `> 待核实` | B（预印本；**是否已中稿未在本批证据标注**） | 高（真机人形 RL 里程碑） | ★★★★★ | http://arxiv.org/abs/2303.03381v2 | 真机人形 RL 行走 [81] |
| Virtual Constraints and Hybrid Zero Dynamics for Realizing Underactuated Bipedal Locomotion | 2017 | arXiv（math.OC/cs.RO） | `> 待核实` | B（早期预印本/教材式综述） | 高（HZD 理论基石，学习式方法的经典对照） | ★★★★★ | http://arxiv.org/abs/1706.01127v1 | HZD / 虚拟约束 [23] |
| Extended Hybrid Zero Dynamics for Bipedal Walking of the Knee-less Robot SLIDER | 2025 | arXiv cs.RO（v2） | `> 待核实` | B（预印本） | 中（HZD 的新近扩展） | ★★★★☆ | http://arxiv.org/abs/2504.01165v2 | 无膝机器人 HZD 扩展 [20] |
| Hybrid Zero Dynamics Control for Bipedal Walking with a Non-Instantaneous Double Support Phase | 2023 | arXiv | `> 待核实` | B | 中 | ★★★★☆ | http://arxiv.org/abs/2303.05165v1 | HZD 双支撑扩展 [24] |
| Feedback Control of a Cassie Bipedal Robot: Walking, Standing, and Riding a Segway | 2018 | arXiv（Caltech/密歇根系） | `> 待核实` | B | 高（Cassie 系列经典报告） | ★★★★★ | http://arxiv.org/abs/1809.07279v1 | 反馈控制与腿足硬件经典 [19] |
| Dynamic Walking with Compliance on a Cassie Bipedal Robot | 2019 | arXiv | `> 待核实` | B | 中 | ★★★★☆ | http://arxiv.org/abs/1904.11104v1 | 柔顺动态行走 [17] |
| Generation of and Switching among Limit-Cycle Bipedal Walking Gaits | 2017 | arXiv | `> 待核实` | B | 中（极限环步态理论） | ★★★★☆ | http://arxiv.org/abs/1703.07197v1 | 极限环步态切换 [18] |
| Assessing Whole-Body Operational Space Control in a Point-Foot Series Elastic Biped | 2015 | arXiv | `> 待核实` | B（早期预印本） | 中（WBC 经典基线与评估） | ★★★★☆ | http://arxiv.org/abs/1501.02855v1 | 全身操作空间控制评估 [9] |
| Whole-Body Geometric Retargeting for Humanoid Robots | 2019 | arXiv | `> 待核实` | B | 中（重定向基线） | ★★★★☆ | http://arxiv.org/abs/1909.10080v1 | 人形全身几何重定向 [8] |
| Regret of H∞ Preview Controllers | 2026 | arXiv math.OC（v2） | `> 待核实` | B（预印本，控制理论） | 低–中（与经典预观控制相关，非腿足专用） | ★★★☆☆ | http://arxiv.org/abs/2602.01420v2 | 预观控制/H∞ 的 regret 分析 [10] |
| Modeling and Analysis of Walking Pattern for a Biped Robot | 2015 | arXiv | `> 待核实` | B | 低–中（ZMP/行走模式分析传统） | ★★★☆☆ | http://arxiv.org/abs/1508.02873v1 | 步态模式建模 [13] |
| Isaac Gym: High Performance GPU-Based Physics Simulation for Robot Learning | 2021 | NVIDIA | `> 待核实` | B（NVIDIA 官方技术报告/预印本） | 高（大规模并行 RL 的事实标准前代） | ★★★★★ | http://arxiv.org/abs/2108.10470v2 | 并行仿真基座 [102] |
| A ROS-based Software Framework for the NimbRo-OP Humanoid Open Platform | 2018 | arXiv cs.RO（Bonn） | `> 待核实` | B | 中（**本批唯一 ROS 人形框架证据，时效性差**） | ★★★☆☆ | http://arxiv.org/abs/1809.11051v1 | ROS 集成经典参考 [6] |
| NimbRo-OP2: Grown-up 3D Printed Open Humanoid Platform | 2018 | arXiv cs.RO | `> 待核实` | B | 中 | ★★★☆☆ | http://arxiv.org/abs/1809.11144v1 | 开源人形平台 [51] |

> **待核实（经典工作的重大缺口）**：ZMP 原始文献（Vukobratović）、Raibert 的 SLIP/跳跃控制专著、MIT Cheetah 系列、以及 [11] 神经振荡器步态演化等方向，本批来源**未提供可核查的一手链接或直接证据**（[11] 为 2010 年 arXiv 预印本，属 D 级线索，不足以支撑"经典"论断）。上述缺口建议由人工补检补齐后再写入正式综述。

---

## 七、数据集、基准与开放问题

### 7.1 数据集与基准

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| HumanoidBench | 2024 | arXiv cs.RO（v2） | `> 待核实`（候选块无引用数/榜单） | B（预印本） | 高（本批唯一的全身人形仿真基准） | ★★★★★ | http://arxiv.org/abs/2403.10506v2 | 全身运动+操作仿真基准 [49] |
| MuJoCo MPC for Humanoid Control: Evaluation on HumanoidBench | 2024 | arXiv cs.RO | `> 待核实` | B | 中高（提供 MPC 基线，支撑 RL vs 优化对照） | ★★★★★ | http://arxiv.org/abs/2408.00342v1 | HumanoidBench 上的 MPC 基线评估 [50] |
| MuJoCo Playground | 2025 | arXiv cs.RO（v1） | `> 待核实` | B | 高（GPU 加速 + sim2real 环境的新选项） | ★★★★★ | http://arxiv.org/abs/2502.08844v1 | 并行环境/训练基座 [56] |
| Isaac Lab | 2025 | NVIDIA 官方团队 | `> 待核实`（仓库 star 未在候选块给出） | B（NVIDIA 官方技术报告） | 高（本批 q4 中唯一被明确称为"模块化、可组合、GPU 加速"的框架） | ★★★★★ | http://arxiv.org/abs/2511.04831v1 ；仓库 https://github.com/isaac-sim/IsaacLab | 训练/仿真框架，Isaac Gym 继任者 [106] |
| Isaac Gym | 2021 | NVIDIA | `> 待核实` | B | 高 | ★★★★★ | http://arxiv.org/abs/2108.10470v2 | 前代并行仿真 [102] |
| Open X-Embodiment (Robotic Learning Datasets and RT-X Models) | 2023 | 多机构联合 | `> 待核实`（候选块无引用数） | B（预印本 v9，后续多中稿） | 高（跨本体操作数据的事实标准） | ★★★★☆（**与本报告腿足运动主题相关性中**） | http://arxiv.org/abs/2310.08864v9 | 跨本体机器人数据 [63] |
| AMASS（motion capture） | — | MPI（种子资源） | `> 待核实`（未实时检索） | B（官方数据集主页） | 高（人体动捕事实标准，被广泛用作运动先验） | ★★★★★ | https://amass.is.tue.mpg.de/ | 人体动作捕捉数据（种子资源，未实时检索） |
| Lafan1 / LAFAN1 retargeted | — | Ubisoft La Forge（种子资源） | `> 待核实` | B（官方 GitHub 数据集） | 高（人形动画先验） | ★★★★★ | https://github.com/ubisoft/ubisoft-laforge-animation-dataset | 人形动作先验（种子资源，未实时检索） |
| DROID / LIBERO / SimplerEnv / RoboArena | — | — | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | **本批候选来源中完全未出现**，无法评估其对腿足/人形运动的可比评测支撑能力 |
| HumanoidBench 之外的跨本体评测 | — | — | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | 跨本体（Unitree G1/H1、Cassie、小型平台）统一评测在本批证据中**缺失** [71][48] |

### 7.2 开源项目与工程实践栈

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| IsaacLab | 2023– | NVIDIA（种子资源；[106] 为官方技术报告） | `> 待核实`（star 未在候选块给出） | B（官方仓库 + NVIDIA 技术报告） | 高 | ★★★★★ | https://github.com/isaac-sim/IsaacLab ；论文 http://arxiv.org/abs/2511.04831v1 | GPU 并行训练首选复用对象 [106] |
| legged_gym | 2021– | ETH Zurich Robotic Systems Lab（种子资源） | `> 待核实` | B（官方仓库，ETH 团队） | 高（腿足 RL 训练框架的经典开源实现） | ★★★★★ | https://github.com/leggedrobotics/legged_gym | 腿足 RL 训练框架（种子资源，未实时检索 star/提交） |
| unitree_rl_gym | — | Unitree（种子资源） | `> 待核实` | B（厂商官方仓库） | 中高（面向 Unitree 硬件的标准训练环境） | ★★★★☆ | https://github.com/unitreerobotics/unitree_rl_gym | Unitree 强化学习训练环境（种子资源，未实时检索） |
| NVlabs/ProtoMotions | — | NVIDIA（种子资源） | `> 待核实` | B（官方仓库） | 中高（人形物理仿真运动工具） | ★★★★☆ | https://github.com/NVlabs/ProtoMotions | 人形物理仿真运动（种子资源，未实时检索） |
| Humanoid-Gym | 2024 | arXiv cs.RO（v2） | `> 待核实` | B（预印本） | 中（人形零样本 sim2real 的可复现指向） | ★★★★☆ | http://arxiv.org/abs/2404.05695v2 | 人形 RL 零样本 sim2real [112] |
| MuJoCo Playground | 2025 | arXiv cs.RO | `> 待核实` | B | 高 | ★★★★★ | http://arxiv.org/abs/2502.08844v1 | 并行环境 + sim2real [56] |
| NimbRo-OP ROS framework | 2018 | Bonn | `> 待核实` | B（预印本） | 低–中（**时效性明显不足**） | ★★★☆☆ | http://arxiv.org/abs/1809.11051v1 | ROS 集成历史参考 [6] |

> **工程侧关键缺口（必须点明）**
> 1. **ROS2 集成在本批 118 条来源中完全未出现**；唯一 ROS 相关证据是 2018 年的 NimbRo-OP 框架 [6]，无法据此判断当下 ROS2 中间件/实时通信/部署实践。
> 2. **仓库维护活跃度（最近提交、star、license）在本批证据中无任何数据**，全部 `> 待核实`；"活跃度"只能依据机构与发布时间间接推断（例如 [106] 为 NVIDIA 官方团队 2025-11 报告）。
> 3. Isaac Lab / Isaac Sim 的硬件要求（GPU 型号、显存）与版本兼容性在候选块中未给出，**复现门槛待核实** [106][107]。

### 7.3 开放问题与争议

1. **sim2real gap 的归因未收敛**：[84] 以"仿真的诅咒"框架剖析来源；[108] 把高维度与域随机化列为主要困难；[2] 单独研究 DR 的收益；[107] 承认零样本部署后仍存在 gap。**是数据、架构还是仿真保真度主导，本批证据无法给出定量归因** → `> 待核实`。
2. **RL 与 MPC/WBC 的边界**：HumanoidBench [49] + MuJoCo MPC 基线 [50] 提供了同类任务下的对照尝试；经典对照侧还有全身操作空间控制 [9] 与 HZD 系列 [23][20]。但**尚无证据表明学习式方法在同硬件、同任务上系统性超过调优后的 MPC/WBC** → `> 待核实`。
3. **奖励设计仍是瓶颈**：[98] 直接针对"人形运动中的奖励设计自动化、RL 训练与反馈优化"（STRIDE）；奖励设计相关方法论在 [92][94][95][96] 中有一般性讨论，但**这些来源与腿足/人形任务无直接绑定**，作为迁移性线索使用。
4. **安全性与可认证性**：[15] 输入受限 CBF、[86] 机会约束 MPC 的安全 RL 提供了形式化工具，但与学习式全身策略的耦合在本批证据中未见验证 → `> 待核实`。
5. **仿真主导导致的可迁移性不确定**：[27] 明确指出"RL 研究仍根植于仿真，使研究向物理现实的转化对算法与研究者都不确定"——这是对"仿真 SOTA ≠ 真机能力"的直接警示。热度 `> 待核实`；权威=arXiv cs.RO（2026-07）；关注度=中；推荐度 ★★★★☆（方法论反思类必读）。
6. **跨本体泛化**：单一策略控制多本体（不同动力学、DoF、运动学拓扑）被 [71] 明确列为未解问题。
7. **检索与证据层面的失败案例**：本批 q5/q6 的子问题检索返回大量无关条目（如短视频参与度预测 [55]、RowHammer 实时可预测性 [82]、基础模型透明度指数 [59]、越南法律问答 [58]），说明**关键词召回质量本身是不确定性来源**；相关结论必须依赖人工补检而非自动抽取结果。

---

## 八、建议关注清单（Watchlist）

| 关注对象 | 理由 | 建议跟踪信号 | 引用 |
|---|---|---|---|
| ASAP（仿真-真机物理对齐） | sim2real 归因问题的核心范式之一 | 是否开源、是否被第三方复现、是否扩展到人形以外本体 | [80] |
| HOVER / 统一通用全身控制器 | "一个策略覆盖多模式"的架构路线 | 是否与 MPC/WBC 在同任务上做定量对照 | [72][73] |
| UniTracker / 跨本体蒸馏 | 通用运动追踪与跨本体泛化 | 跨本体迁移的量化结果与失败模式 | [70][71] |
| OmniH2O / H2O / TWIST / CLOT | 遥操作数据闭环主线 | 数据规模、延迟、是否需要动捕/VR | [75][76][77][79] |
| 起立与跌倒恢复 | 真机可用性硬门槛 | 真机成功率、地形与姿态多样性 | [46][47] |
| Parkour（四足 + 人形） | 敏捷 + 感知的标杆任务 | 真机 vs 仿真成绩分离报告 | [40][45] |
| Learning Sim-to-Real Humanoid Locomotion in 15 Minutes | 训练效率与工程配方的强传播性宣称 | "15 分钟"的具体硬件口径与独立复现 | [108] |
| Isaac Lab / Isaac Sim / MuJoCo Playground | 训练与仿真基座选型 | 版本兼容、GPU 要求、ROS2 桥接进展 | [106][107][56][102] |
| HumanoidBench + MuJoCo MPC 基线 | 少见的"RL vs 优化"可比评测入口 | 是否出现跨本体与真机扩展版本 | [49][50] |
| Locomotion Beyond Feet | 非足部接触运动与关键帧工程化 | 是否开源关键帧管线、是否跨本体复用 | [100] |
| 神经形态 / 在线自适应控制 | 部署后退化与负载变化问题 | 真机长时运行数据 | [36][31] |
| AMASS / LAFAN1 / ProtoMotions | 动作先验与重定向数据基础 | 重定向质量、许可与商用限制 | 种子资源 |

---

## 参考来源

[1] Humanoid Whole-Body Badminton via an Annealed Reinforcement Learning Curriculum — http://arxiv.org/abs/2511.11218v4
[2] The Role of Domain Randomization in Training Diffusion Policies for Whole-Body Humanoid Control — http://arxiv.org/abs/2411.01349v1
[3] Humanoid Manipulation Interface: Humanoid Whole-Body Manipulation from Robot-Free Demonstrations — http://arxiv.org/abs/2602.06643v2
[4] CHILD (Controller for Humanoid Imitation and Live Demonstration): a Whole-Body Humanoid Teleoperation System — http://arxiv.org/abs/2508.00162v2
[5] Humanoid Whole-Body Manipulation via Active Spatial Brain and Generalizable Action Cerebellum — http://arxiv.org/abs/2605.21133v2
[6] A ROS-based Software Framework for the NimbRo-OP Humanoid Open Platform — http://arxiv.org/abs/1809.11051v1
[7] Hierarchical World Models as Visual Whole-Body Humanoid Controllers — http://arxiv.org/abs/2405.18418v3
[8] Whole-Body Geometric Retargeting for Humanoid Robots — http://arxiv.org/abs/1909.10080v1
[9] Assessing Whole-Body Operational Space Control in a Point-Foot Series Elastic Biped: Balance on Split Terrain and Undirected Walking — http://arxiv.org/abs/1501.02855v1
[10] Regret of $H_\infty$ Preview Controllers — http://arxiv.org/abs/2602.01420v2
[11] Evolution of Biped Walking Using Neural Oscillators Controller and Harmony Search Algorithm Optimizer — http://arxiv.org/abs/1006.4553v1
[12] Nonlinear Model Predictive Control for Preview-Based Traction Control — http://arxiv.org/abs/2406.02206v1
[13] Modeling and Analysis of Walking Pattern for a Biped Robot — http://arxiv.org/abs/1508.02873v1
[14] Control of a Rigid Wing Pumping Airborne Wind Energy System in all Operational Phases — http://arxiv.org/abs/2006.11141v1
[15] Safe Control Synthesis via Input Constrained Control Barrier Functions — http://arxiv.org/abs/2104.01704v1
[16] Exponential input-to-state stabilization of a class of diagonal boundary control systems with delay boundary control — http://arxiv.org/abs/2003.05711v1
[17] Dynamic Walking with Compliance on a Cassie Bipedal Robot — http://arxiv.org/abs/1904.11104v1
[18] Generation of and Switching among Limit-Cycle Bipedal Walking Gaits — http://arxiv.org/abs/1703.07197v1
[19] Feedback Control of a Cassie Bipedal Robot: Walking, Standing, and Riding a Segway — http://arxiv.org/abs/1809.07279v1
[20] Extended Hybrid Zero Dynamics for Bipedal Walking of the Knee-less Robot SLIDER — http://arxiv.org/abs/2504.01165v2
[21] QCD and High Energy Interactions: Moriond 2018 Theory Summary — http://arxiv.org/abs/1806.04982v2
[22] Evaluation of an open-source implementation of the SRP-PHAT algorithm within the 2018 LOCATA challenge — http://arxiv.org/abs/1812.05901v1
[23] Virtual Constraints and Hybrid Zero Dynamics for Realizing Underactuated Bipedal Locomotion — http://arxiv.org/abs/1706.01127v1
[24] Hybrid Zero Dynamics Control for Bipedal Walking with a Non-Instantaneous Double Support Phase — http://arxiv.org/abs/2303.05165v1
[25] Learning Robust, Agile, Natural Legged Locomotion Skills in the Wild — http://arxiv.org/abs/2304.10888v3
[26] One-Shot Reinforcement Learning for Robot Navigation with Interactive Replay — http://arxiv.org/abs/1711.10137v2
[27] The Open Ant: A Robot Platform for Reinforcement Learning Research — http://arxiv.org/abs/2607.18488v1
[28] Value Bonuses using Ensemble Errors for Exploration in Reinforcement Learning — http://arxiv.org/abs/2602.12375v1
[29] ATRos: Learning Energy-Efficient Agile Locomotion for Wheeled-legged Robots — http://arxiv.org/abs/2510.09980v1
[30] On Terrain-Aware Locomotion for Legged Robots — http://arxiv.org/abs/2212.00683v1
[31] Legged Robots that Keep on Learning: Fine-Tuning Locomotion Policies in the Real World — http://arxiv.org/abs/2110.05457v1
[32] Hybrid Internal Model: Learning Agile Legged Locomotion with Simulated Robot Response — http://arxiv.org/abs/2312.11460v3
[33] Quadruped Locomotion on Non-Rigid Terrain using Reinforcement Learning — http://arxiv.org/abs/2107.02955v1
[34] Terrain-Aware Autonomous Planetary Exploration for Exteroceptive-Proprioceptive Mapping with Quadruped Scouts — http://arxiv.org/abs/2609.35493v1
[35] Towards Proprioceptive Terrain Mapping with Quadruped Robots for Exploration in Planetary Permanently Shadowed Regions — http://arxiv.org/abs/2510.18986v1
[36] Neuromorphic Reinforcement Learning for Quadruped Locomotion Control on Uneven Terrain — http://arxiv.org/abs/2605.09595v2
[37] Towards Terrain-Aware Safe Locomotion for Quadrupedal Robots Using Proprioceptive Sensing — http://arxiv.org/abs/2603.09585v1
[38] Load-bearing Assessment for Safe Locomotion of Quadruped Robots on Collapsing Terrain — http://arxiv.org/abs/2510.21369v1
[39] NTU-NPU System for Voice Privacy 2024 Challenge — http://arxiv.org/abs/2410.02371v1
[40] Robot Parkour Learning — http://arxiv.org/abs/2309.05665v2
[41] Agile But Safe: Learning Collision-Free High-Speed Legged Locomotion — http://arxiv.org/abs/2401.17583v3
[42] Unsupervised Skill Discovery as Exploration for Learning Agile Locomotion — http://arxiv.org/abs/2508.08982v1
[43] Learning in the Large - An Exploratory Study of Retrospectives in Large-Scale Agile Development — http://arxiv.org/abs/1805.10310v1
[44] Learning Agile Paths from Optimal Control — http://arxiv.org/abs/2212.00184v1
[45] Humanoid Parkour Learning — http://arxiv.org/abs/2406.10759v2
[46] Learning Getting-Up Policies for Real-World Humanoid Robots — http://arxiv.org/abs/2502.12152v2
[47] Learning Humanoid Standing-up Control across Diverse Postures — http://arxiv.org/abs/2502.08378v2
[48] Towards Miniature Humanoid Tele-Loco-Manipulation Using Virtual Reality and Reinforcement Learning — http://arxiv.org/abs/2607.20399v1
[49] HumanoidBench: Simulated Humanoid Benchmark for Whole-Body Locomotion and Manipulation — http://arxiv.org/abs/2403.10506v2
[50] MuJoCo MPC for Humanoid Control: Evaluation on HumanoidBench — http://arxiv.org/abs/2408.00342v1
[51] NimbRo-OP2: Grown-up 3D Printed Open Humanoid Platform for Research — http://arxiv.org/abs/1809.11144v1
[52] Optimization of Humanoid Robot Designs for Human-Robot Ergonomic Payload Lifting — http://arxiv.org/abs/2211.13503v1
[53] Design and implementation of computational platform for social-humanoid robot Lumen as an exhibition guide in Electrical Engineering Days 2015 — http://arxiv.org/abs/1607.04763v1
[54] Online Balanced Motion Generation for Humanoid Robots — http://arxiv.org/abs/1810.08388v1
[55] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1
[56] MuJoCo Playground — http://arxiv.org/abs/2502.08844v1
[57] NTIRE 2025 Challenge on Image Super-Resolution (x4): Methods and Results — http://arxiv.org/abs/2504.14582v3
[58] VLSP 2025 MLQA-TSR Challenge: Vietnamese Multimodal Legal Question Answering on Traffic Sign Regulation — http://arxiv.org/abs/2510.20381v1
[59] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1
[60] Event-Enriched Image Analysis Grand Challenge at ACM Multimedia 2025 — http://arxiv.org/abs/2508.18904v1
[61] The AudioMOS Challenge 2025 — http://arxiv.org/abs/2509.01336v1
[62] TDCOSMO 2025: Cosmological constraints from strong lensing time delays — http://arxiv.org/abs/2506.03023v4
[63] Open X-Embodiment: Robotic Learning Datasets and RT-X Models — http://arxiv.org/abs/2310.08864v9
[64] Open-Ended Learning Leads to Generally Capable Agents — http://arxiv.org/abs/2107.12808v2
[65] The RSNA Abdominal Traumatic Injury CT (RATIC) Dataset — http://arxiv.org/abs/2405.19595v1
[66] On-Policy Robot Imitation Learning from a Converging Supervisor — http://arxiv.org/abs/1907.03423v7
[67] panda-gym: Open-source goal-conditioned environments for robotic learning — http://arxiv.org/abs/2106.13687v2
[68] Multi-objective Model-based Policy Search for Data-efficient Learning with Sparse Rewards — http://arxiv.org/abs/1806.09351v3
[69] State-of-the-art in Robot Learning for Multi-Robot Collaboration: A Comprehensive Survey — http://arxiv.org/abs/2408.11822v1
[70] UniTracker: Learning Universal Whole-Body Motion Tracker for Humanoid Robots — http://arxiv.org/abs/2507.07356v3
[71] Embodiment-Aware Generalist Specialist Distillation for Unified Humanoid Whole-Body Control — http://arxiv.org/abs/2602.02960v2
[72] HOVER: Versatile Neural Whole-Body Controller for Humanoid Robots — http://arxiv.org/abs/2410.21229v2
[73] A Unified and General Humanoid Whole-Body Controller for Versatile Locomotion — http://arxiv.org/abs/2502.03206v3
[74] KungfuBot2: Learning Versatile Motion Skills for Humanoid Whole-Body Control — http://arxiv.org/abs/2509.16638v1
[75] OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning — http://arxiv.org/abs/2406.08858v1
[76] Learning Human-to-Humanoid Real-Time Whole-Body Teleoperation — http://arxiv.org/abs/2403.04436v1
[77] TWIST: Teleoperated Whole-Body Imitation System — http://arxiv.org/abs/2505.02833v1
[78] Dynamic Locomotion Teleoperation of a Wheeled Humanoid Robot Reduced Model with a Whole-Body Human-Machine Interface — http://arxiv.org/abs/2109.03906v1
[79] CLOT: Closed-Loop Global Motion Tracking for Whole-Body Humanoid Teleoperation — http://arxiv.org/abs/2602.15060v2
[80] ASAP: Aligning Simulation and Real-World Physics for Learning Agile Humanoid Whole-Body Skills — http://arxiv.org/abs/2502.01143v3
[81] Real-World Humanoid Locomotion with Reinforcement Learning — http://arxiv.org/abs/2303.03381v2
[82] JENGA: Exploiting Counter-Based RowHammer Countermeasures to Break Real-Time Predictability — http://arxiv.org/abs/2609.01077v1
[83] Efficient Real-World Deblurring using Single Images: AIM 2025 Challenge Report — http://arxiv.org/abs/2510.12788v1
[84] Sim-to-Real Transfer in Deep Reinforcement Learning for Bipedal Locomotion — http://arxiv.org/abs/2511.06465v1
[85] Toward Control of Wheeled Humanoid Robots with Unknown Payloads: Equilibrium Point Estimation via Real-to-Sim Adaptation — http://arxiv.org/abs/2403.10948v2
[86] Safe Reinforcement Learning with Chance-constrained Model Predictive Control — http://arxiv.org/abs/2112.13941v2
[87] Data-Efficient Deep Reinforcement Learning for Attitude Control of Fixed-Wing UAVs: Field Experiments — http://arxiv.org/abs/2111.04153v2
[88] Optimization of the Model Predictive Control Update Interval Using Reinforcement Learning — http://arxiv.org/abs/2011.13365v1
[89] On multi-step prediction models for receding horizon control — http://arxiv.org/abs/1802.09767v1
[90] Economic model predictive control for snake robot locomotion — http://arxiv.org/abs/1909.00795v2
[91] Sample-Efficient Reinforcement Learning with Maximum Entropy Mellowmax Episodic Control — http://arxiv.org/abs/1911.09615v1
[92] Tiered Reward: Designing Rewards for Specification and Fast Learning of Desired Behavior — http://arxiv.org/abs/2212.03733v3
[93] Reinforcement Learning with Stochastic Reward Machines — http://arxiv.org/abs/2510.14837v1
[94] Reward Shaping via Diffusion Process in Reinforcement Learning — http://arxiv.org/abs/2306.11885v1
[95] From Sparse to Dense: Toddler-inspired Reward Transition in Goal-Oriented Reinforcement Learning — http://arxiv.org/abs/2501.17842v1
[96] From Reward Shaping to Q-Shaping: Achieving Unbiased Learning with LLM-Guided Knowledge — http://arxiv.org/abs/2410.01458v1
[97] Semi-supervised reward learning for offline reinforcement learning — http://arxiv.org/abs/2012.06899v1
[98] STRIDE: Automating Reward Design, Deep Reinforcement Learning Training and Feedback Optimization in Humanoid Robotics Locomotion — https://arxiv.org/abs/2502.04692
[99] Reinforcement Learning Tuning for VideoLLMs: Reward Design and Data Efficiency — http://arxiv.org/abs/2506.01908
[100] Locomotion Beyond Feet — http://arxiv.org/abs/2601.03607v1
[101] On the Popularity of GitHub Applications: A Preliminary Note — http://arxiv.org/abs/1507.00604v3
[102] Isaac Gym: High Performance GPU-Based Physics Simulation For Robot Learning — http://arxiv.org/abs/2108.10470v2
[103] The Synthesis of Optimal Control Laws Using Isaacs' Method for the Solution of Differential Games — http://arxiv.org/abs/2112.10849v2
[104] Training Software Engineering Agents and Verifiers with SWE-Gym — http://arxiv.org/abs/2412.21139v2
[105] MARS-Gym: A Gym framework to model, train, and evaluate Recommender Systems for Marketplaces — http://arxiv.org/abs/2010.07035v1
[106] Isaac Lab: A GPU-Accelerated Simulation Framework for Multi-Modal Robot Learning — http://arxiv.org/abs/2511.04831v1
[107] Isaac Sim-to-Real: Reinforcement Learning based Locomotion for Quadrupeds — http://arxiv.org/abs/2607.18135v1
[108] Learning Sim-to-Real Humanoid Locomotion in 15 Minutes — http://arxiv.org/abs/2512.01996v1
[109] G1: Bootstrapping Perception and Reasoning Abilities of Vision-Language Model via Reinforcement Learning — http://arxiv.org/abs/2505.13426v1
[110] HumanPlus: Humanoid Shadowing and Imitation from

---

*Generated by research-bot · topic=`embodied-humanoid` · depth=`standard` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading · model=`deepseek-v4-flash` · sources=118 · duration=320s · 2026-10-04T22:30:39+00:00*
