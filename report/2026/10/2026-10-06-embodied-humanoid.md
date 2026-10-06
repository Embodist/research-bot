# 具身智能 · 人形与腿足运动控制（Humanoid & Legged Locomotion）技术图谱调研报告

> **日期**：2026-10-06（UTC）
> **领域**：具身智能 / 人形机器人（Humanoid）/ 腿足运动控制（Legged Locomotion）/ 全身控制（WBC）
> **检索源**：97 条编号来源（含噪声召回）+ 7 项领域种子资源；经主题相关性筛选后可用来源约 60 条，另约 30 条为跨领域误召回（见 §8.3）
> **证据纪律**：本报告所有关键论断均标注编号引用 [n]。结构化抽取块中 `heat`／`citations`／`stars` 字段大面积为空，凡无法取到热度数字者一律写 `> 待核实`，**不编造任何引用数、star 数、成功率或榜单排名**。

---

## 摘要（Executive Summary）

近 1–2 年（2024–2026）人形与腿足运动控制的核心变化可归纳为五条主线：

1. **训练成本塌缩**：大规模并行仿真把 RL 训练从「数天」压缩到「分钟级」，「Learning Sim-to-Real Humanoid Locomotion in 15 Minutes」是这一趋势最直接的标题级宣言 [12][19]。这改变了 sim2real 的工程经济学——迭代速度本身成为竞争力。
2. **从「会走」到「全身体技」**：研究重心转向稀疏落脚点行走（BeamDojo [69]）、人形跑酷（Humanoid Parkour Learning [67]）、全身羽毛球（Humanoid Whole-Body Badminton [48]）、用膝/肘/手建立额外接触点的超足式运动（Locomotion Beyond Feet [54]）。
3. **统一全身控制器（unified WBC）取代模块化堆叠**：HOVER [21]、UniTracker [65]、TWIST [86] 代表「单一策略覆盖多形态、多任务」的路线，与经典的分层 MPC 形成对照。
4. **人体动作成为核心监督信号**：遥操作与动作模仿（H2O [87]、OmniH2O [92]、CHILD [3]）与动作重定向（retargeting）研究（Retargeting Matters [83]、Dense Temporal Motion Retargeting [78]）同步爆发，AMASS / LAFAN1 等动捕数据成为基础设施。
5. **评测仍是最薄弱环节**：HumanoidBench [22][74] 是少数被第三方复用的基准（见 MuJoCo MPC on HumanoidBench [75]），但真机可复现评测体系仍未建立 [76]。

> **总体判断**：方法层面已高度「学习化」，**瓶颈从算法的表达能力转移到评测可信度、硬件可获得性与安全/恢复鲁棒性**。当前绝大多数条目仍为 arXiv 预印本（confidence 低），跨论文的数字比较基本不可行。

---

## 一、关键前沿进展（近 1–2 年）

### 1.1 分钟级 sim-to-real 人形 RL 训练

- **要点**：在 massively parallel simulation 上把 humanoid RL 训练从数天压到分钟级，同时维持 sim-to-real 可靠性；难点被明确归因于高维状态与域随机化（domain randomization）带来的成本 [12][19]。
- **热度证据**：`> 待核实`（抽取块 `heat` 字段为空，无引用数/star 可查）
- **权威证据**：arXiv cs.RO 预印本 [12][19]（同一工作两个链接），**未见同行评审 venue 标注**
- **关注度**：中 —— 依据：「训练时间」是该领域被反复引用的工程瓶颈指标，且该工作同时出现在 q1 与 q3 两个子问题的召回结果中 [12][19]
- **推荐度**：★★★★☆ —— 理由：若结果成立，它直接改写 sim2real 的工程流程（快速迭代 + 快速重训），对选型决策影响最大；但需等独立复现。

### 1.2 稀疏落脚点上的敏捷人形行走

- **要点**：BeamDojo 面向稀疏落脚点（sparse footholds）的敏捷人形 locomotion [69]；与 Humanoid Parkour Learning [67]、Robot Parkour Learning [41] 构成「跑酷—落脚点」序列。
- **热度证据**：`> 待核实`
- **权威证据**：arXiv cs.RO 预印本 [67][69]；`Robot Parkour Learning` [41] 为同系列早期工作
- **关注度**：高 —— 依据：稀疏落脚点是四足→人形迁移中最常被引用的「能力分水岭」任务，跨 q1/q4 被多次召回 [69]
- **推荐度**：★★★★☆（[69]）—— 理由：稀疏落脚同时考验感知、规划与全身动力学，是当前人形敏捷性的代表题型。

### 1.3 动态交互类全身技能（非静止场景）

- **要点**：Humanoid Whole-Body Badminton 提出退火式（annealed）RL 课程，训练统一全身策略应对高速运动物体，明确指出动态真实世界交互仍是短板 [48]。
- **热度证据**：`> 待核实`
- **权威证据**：arXiv cs.RO 预印本 [48]（v4，说明经多轮修订）
- **关注度**：中 —— 依据：动态物体交互是人形从「locomotion」迈向「loco-manipulation」的标志性任务类型 [48]
- **推荐度**：★★★☆☆ —— 理由：任务新颖度高，但与 locomotion 主线（行走/地形）相关度中等。

### 1.4 无机器人演示的全身操作接口

- **要点**：Humanoid Manipulation Interface 主张绕过遥操作与视觉 sim2real RL 的硬件与奖励工程负担，用「robot-free demonstrations」获取人形全身操作技能 [64]。
- **热度证据**：`> 待核实`
- **权威证据**：arXiv cs.RO 预印本 [64]（2026）
- **关注度**：中 —— 依据：直指遥操作硬件成本与 reward engineering 两大公认痛点 [64]
- **推荐度**：★★★★☆ —— 理由：若成立，可显著降低真机数据采集门槛；属方法论级贡献。

### 1.5 轮椅—腿混合与超足式运动

- **要点**：ATRos 针对轮腿机器人（wheeled-legged）学习节能敏捷 locomotion [52]；Locomotion Beyond Feet 明确打破「腿式步态」假设，用手、膝、肘建立额外接触 [54]。
- **热度证据**：`> 待核实`
- **权威证据**：arXiv cs.RO 预印本 [52][54]
- **关注度**：中 —— 依据：轮腿混合在效率上有明确物理动机 [52]；超足式接触属新命题 [54]
- **推荐度**：★★★☆☆ —— 理由：与主流双足人形路线相关但不等同，适合作为扩展方向参考。

---

## 二、学习式 locomotion 与全身控制

### 2.1 路线分野

| 路线 | 代表工作 | 核心机制 | 证据 |
|---|---|---|---|
| **端到端 RL 单策略** | [14] Real-World Humanoid Locomotion with RL；[12][19] 15 Minutes | 单一神经网络直接输出关节动作，靠域随机化覆盖不确定性 | [12][14][19] |
| **分层 / 降阶模型 MPC** | [15] Hierarchical Reduced-Order MPC；[24] RoMoCo；[17] Bracing for Impact | 降阶模型（reduced-order model）做步态规划 + 全身跟踪，计算高效、可解释 | [15][17][24] |
| **统一神经全身控制器** | [21] HOVER；[65] UniTracker | 一个策略覆盖多任务/多形态，替代「每任务一策略」 | [21][65] |
| **模仿 / 动作跟踪器** | [86] TWIST；[87] H2O；[92] OmniH2O；[65] UniTracker | 以人体动作为跟踪目标，得到类人自然步态 | [65][86][87][92] |

### 2.2 「神经 WBC 统一化」是否已胜出？

- **要点**：HOVER 定位为 versatile neural whole-body controller [21]，UniTracker 用三阶段训练实现跨人类行为的鲁棒 motion tracking [65]；两者共同主张「统一」优于「模块化堆叠」。
- **热度证据**：`> 待核实`（无引用数/star 字段）；间接信号：LeCAR-Lab/human2humanoid 为该方向的公开仓库 [97]
- **权威证据**：arXiv cs.RO 预印本 [21][65][97]
- **关注度**：高 —— 依据：HOVER 同时出现在 q3（开源工程栈）与 q5（WBC 路线）的召回中，说明其被当作该路线的锚点工作 [21]
- **推荐度**：★★★★★（[21]）—— 理由：统一 WBC 是当前人形全身控制最集中的竞争赛道，阅读优先级最高。
- **反证与谨慎**：分层降阶 MPC 并未退场——[15][24] 仍在 2025 年发表并强调计算效率与鲁棒性 [15][24]，说明「学习式已全面取代模型式」是**过度简化**。`> 待核实`：两者的定量对比（同一硬件、同一任务的成功率/能耗）在本次来源中缺失。

### 2.3 开源工程栈

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| isaac-sim/IsaacLab | — | NVIDIA（种子资源） | `> 待核实` | 官方仓库（B 级） | 高（GPU 并行仿真的事实标准，[16] 亦在其上构建 MARL 框架） | ★★★★★ | https://github.com/isaac-sim/IsaacLab | GPU 仿真训练基座 |
| leggedrobotics/legged_gym | — | ETH Zurich（种子资源） | `> 待核实` | 官方仓库（B 级） | 高（腿足 RL 训练框架的经典起点） | ★★★★☆ | https://github.com/leggedrobotics/legged_gym | 腿足 RL 训练框架 |
| unitreerobotics/unitree_rl_gym | — | Unitree（种子资源） | `> 待核实` | 官方仓库（B 级） | 高（Unitree 硬件用户基数大） | ★★★★☆ | https://github.com/unitreerobotics/unitree_rl_gym | Unitree 强化学习训练环境 |
| LeCAR-Lab/human2humanoid | — | LeCAR-Lab（来源 [97]） | `> 待核实` | 官方仓库（B 级） | 中（H2O/OmniH2O 系列配套代码） | ★★★★☆ | https://github.com/LeCAR-Lab/human2humanoid | 人形真人到人形遥操作与学习 |
| NVlabs/ProtoMotions | — | NVIDIA（种子资源） | `> 待核实` | 官方仓库（B 级） | 中（人形物理仿真运动） | ★★★☆☆ | https://github.com/NVlabs/ProtoMotions | 人形物理仿真运动 |
| ARTEMIS | 2025 | 来源 [18]（Humanoids 2025） | `> 待核实` | **同行评审（A 级）** | 中（全尺寸开源人形硬件平台） | ★★★★☆ | https://doi.org/10.1109/Humanoids65713.2025.11203020 | 全尺寸开源动态 locomotion 平台 |
| Berkeley Humanoid Lite | 2025 | 来源 [20] | `> 待核实` | arXiv 预印本（B 级） | 中（3D 打印低成本路线） | ★★★★☆ | https://arxiv.org/abs/2504.17249 | 可定制 3D 打印人形 |
| NimbRo-OP / OP2 | 2018 | 来源 [1][2] | `> 待核实` | arXiv 预印本（B 级） | 低（已属早期开源平台） | ★★☆☆☆ | http://arxiv.org/abs/1809.11051v1 ; http://arxiv.org/abs/1809.11144v1 | 早期 ROS 人形开源平台 |

- **复现难度判断**：`> 待核实`——本次来源未提供各仓库的安装文档质量、权重是否放出、硬件依赖清单等可核查信息；**不建议**在未实际核查仓库 README / release / license 的情况下判断「开箱可用」。
- **硬件可获得性是隐性门槛**：ARTEMIS [18]、Berkeley Humanoid Lite [20] 的存在本身说明「没有硬件就无法验证」已成为社区共识问题；HECTOR 提供 loco-manipulation 开源研究平台 [23]。

---

## 三、sim2real 与地形适应

### 3.1 域随机化（domain randomization）：从技巧到正规对象

- **要点**：The Role of Domain Randomization in Training Diffusion Policies for Whole-Body Humanoid Control 把 DR 本身作为研究对象，专门考察其对全身人形策略的影响 [63]；Sim-to-Real Transfer in DRL for Bipedal Locomotion 则系统剖析「仿真诅咒」（curse of simulation）的来源 [37]。
- **热度证据**：`> 待核实`
- **权威证据**：arXiv cs.RO 预印本 [37][63]；DR 概念在机器人领域的早期共识性文档见 R:SS 2020 workshop 总结 [29]
- **关注度**：高 —— 依据：DR 被 [12][63] 等多篇工作同时指认为 sim2real 的核心成本项与失败来源
- **推荐度**：★★★★☆（[37]）—— 理由：把「为什么 sim2real 会失败」讲清楚，比又一个 SOTA 更有方法论价值。
- **注意**：来源 [34] 的标题虽含 "Domain-randomized"，但属神经影像（neuroimage, eess.IV）领域 [34]，**不构成本主题证据**，仅说明该术语已跨领域扩散。

### 3.2 地形适应：显式几何表征回归

- **要点**：Foot Position Maps 论文指出，先前 RL locomotion 方法依赖从关节角**隐式推断**落脚点，缺乏显式表达，因而提出以 foot position map + 稳定性奖励提升复杂地形表现 [27]。
- **热度证据**：`> 待核实`
- **权威证据**：arXiv cs.RO 预印本 [27]（2026）
- **关注度**：中 —— 依据：该文以「隐式推断 vs 显式表征」作为核心论点，属于对既有范式的方法论批评 [27]
- **推荐度**：★★★★☆ —— 理由：为「感知到底该以何种形式进入策略」提供了具体答案。
- **相关支撑**：视觉地形感知路线另有 ViTAL [26]、AI-Based Terrain Adaptation Algorithms for Walking Robots [42]；课程学习路线见 Guided Curriculum Learning for Walking Over Complex Terrain [31]。

### 3.3 真实世界持续学习

- **要点**：Legged Robots that Keep on Learning 提出在真实世界对 locomotion 策略做在线微调，直面 sim2real 之后的分布漂移 [53]。
- **热度证据**：`> 待核实`
- **权威证据**：arXiv 预印本 [53]
- **关注度**：中 —— 依据：2021 年工作，在 2024–2026 的召回中仍被检索到 [53]，说明问题未被解决
- **推荐度**：★★★☆☆ —— 理由：属奠基性思路，但需结合最新方法重新评估。

### 3.4 状态估计与感知缺口

- **要点**：Learning Inertial Odometry for Dynamic Legged Robot State Estimation 处理动态运动下的状态估计 [72]，是 sim2real 落地中常被忽视的一环。
- **热度证据**：`> 待核实`
- **权威证据**：arXiv 预印本 [72]
- **关注度**：中 —— 依据：[72] 在本次「经典/奠基」语境下被召回
- **推荐度**：★★★☆☆ —— 理由：工程必需，但非当前研究热点中心。
- **批评性证据**：Bridging the Sim2Real Gap: Vision Encoder Pre-Training 主张用视觉编码器预训练缓解差距 [49]；而 Sim2Real 局限性的早期批评（含 precision agriculture 场景）指出 sim2real 在精细操作上存在根本限制 [51]。

---

## 四、敏捷动作、跑跳与恢复

### 4.1 跑酷与超足式运动

| 工作 | 年份 | 类型 | 关键贡献 | 证据 |
|---|---|---|---|---|
| Robot Parkour Learning | 2023 | 预印本 | 跑酷任务的学习式解法，四足敏捷性代表 | [41] |
| Humanoid Parkour Learning | 2024 | 预印本 | 将跑酷范式迁移到人形 | [67] |
| BeamDojo | 2025 | 预印本 | 稀疏落脚点上的敏捷人形 locomotion | [69] |
| Locomotion Beyond Feet | 2026 | 预印本 | 用膝/肘/手建立额外接触，突破「仅靠脚」的范式 | [54] |
| Agile But Safe | 2024 | 预印本 | 高速腿足运动中的无碰撞安全约束 | [68] |

- **四类证据（以 [69] 为例）**：热度 `> 待核实`｜权威：arXiv cs.RO 预印本 [69]｜关注度：高（稀疏落脚是对比 SOTA 的常见题型）｜推荐度：★★★★☆（敏捷人形最直接的能力检验）。

### 4.2 跌倒恢复与站立

- **要点**：FR-Net 针对复杂地形上四足机器人从任意姿态恢复，核心机制为 mass-contact prediction，指出传统控制器在感知不完整与交互不确定下失效 [28]；Learning Humanoid Standing-up Control across Diverse Postures 则处理人形从多种姿态站起 [47]。
- **热度证据**：`> 待核实`
- **权威证据**：arXiv cs.RO 预印本 [28][47]
- **关注度**：中 —— 依据：恢复能力被多篇工作（[47][48][54]）作为「真实部署前提」提及
- **推荐度**：★★★★☆（[47]）—— 理由：站起/恢复是人形走出实验室的必经关卡，且与安全议题直接耦合。

### 4.3 推力恢复（push recovery）：模型式传统的持续存在

- **要点**：Bracing for Impact 用降阶模型处理人形推力恢复与 locomotion [17]；更早的 DCM 轨迹生成 [57]、capture point 反馈 [58]、滚动时域策略（iCub）[59]、在线平衡运动生成 [60] 构成一条完整的经典脉络。
- **热度证据**：`> 待核实`
- **权威证据**：arXiv 预印本 [17][57][58][59][60]
- **关注度**：中 —— 依据：2025 年的 [17] 仍在该主题下发表，说明模型式方法未被替代 [17]
- **推荐度**：★★★☆☆（[17]）—— 理由：抗扰动的可解释性与可证明性，是学习式方法短期内难以给出的。

### 4.4 安全性

- **要点**：Safe Reinforcement Learning for Legged Locomotion 明确将约束满足纳入 locomotion 训练 [71]；Agile But Safe 在高速场景下处理碰撞规避 [68]。
- **热度证据**：`> 待核实`
- **权威证据**：arXiv 预印本 [68][71]
- **关注度**：中 —— 依据：安全约束在本次召回中出现频次低于性能类工作，可能反映社区关注度不足 `> 待核实`
- **推荐度**：★★★☆☆ —— 理由：安全是人形进入人类环境的前置条件，但目前证据显示投入相对偏少。

---

## 五、遥操作与动作先验

### 5.1 human-to-humanoid 遥操作主线

| 工作 | 年份 | 关键贡献 | 证据 |
|---|---|---|---|
| H2O（Learning Human-to-Humanoid Real-Time Whole-Body Teleoperation） | 2024 | 人形全身实时遥操作，该方向的锚点工作 | [87] |
| OmniH2O | 2024 | 通用且灵巧的人到人形全身遥操作与学习 | [92] |
| TWIST（Teleoperated Whole-Body Imitation System） | 2025 | 面向全身模仿的遥操作系统 | [86] |
| CHILD | 2025 | 强调**关节级**全身遥操作，指出现有系统很少支持 | [3] |
| CLOT | 2026 | 闭环全局运动跟踪用于全身遥操作 | [94] |
| Miniature Humanoid Tele-Loco-Manipulation | 2026 | VR 上半身遥操作 + RL 下半身平衡的厂商常见组合 | [46] |
| HMI（Humanoid Manipulation Interface） | 2026 | 用无机器人演示替代遥操作采数据 | [64] |

- **四类证据（以 [87] 为例）**：热度 `> 待核实`（配套仓库 LeCAR-Lab/human2humanoid [97] 的 star 数未在本次来源中给出）｜权威：arXiv 预印本，且为种子资源标注为 IROS 2024 方向工作 [87]｜关注度：高（H2O/OmniH2O/TWIST 三条线共享同一代码生态 [97]，是当前人形数据采集的主流范式）｜推荐度：★★★★★ —— 理由：遥操作既是数据来源也是部署接口，是当前投入产出比最高的方向之一。

### 5.2 动作重定向（retargeting）：被低估的关键环节

- **要点**：Retargeting Matters 直接质疑重定向环节常被当作实现细节，主张其对 humanoid motion tracking 结果有决定性影响 [83]；Dense Temporal Motion Retargeting 针对跳跃等**动态动作**指出形态差异（morphology gap）需要精细的时序适配 [78]；Spatio-Temporal Motion Retargeting 面向四足 [79]；Kinodynamic Motion Retargeting 用多接触全身轨迹优化处理动力学可行性 [84]；From Language to Locomotion 更进一步提出免重定向（retargeting-free）路线 [81]。
- **热度证据**：`> 待核实`
- **权威证据**：arXiv 预印本 [78][79][81][83][84]；早期几何重定向工作见 [82]
- **关注度**：高 —— 依据：2025–2026 年密集出现同主题论文 [78][81][83][84]，且 [83] 以「Matters」为题主张该环节被系统性忽视，属典型范式争议信号
- **推荐度**：★★★★★（[83]）—— 理由：若重定向质量主导下游指标，则此前大量「策略改进」的对比可能被混淆变量污染——这对复现与评测的影响极大。

### 5.3 动作先验与传感器运动经验

- **要点**：Simulating Infant First-Person Sensorimotor Experience 指出多数重定向只复现运动学而忽略伴随的感觉运动经验，尝试从婴儿动作重定向到人形以生成第一人称经验数据 [80]。
- **热度证据**：`> 待核实`
- **权威证据**：arXiv **q-bio.NC** 预印本 [80]（跨领域提交，非 cs.RO 主通道）
- **关注度**：低 —— 依据：来源分类为 q-bio.NC [80]，与机器人主社区交集有限 `> 待核实`
- **推荐度**：★★☆☆☆ —— 理由：概念新颖（认知科学视角），但技术可迁移性与实验证据在本次来源中无法确认。

---

## 六、经典与奠基性工作

> 说明：以下「经典」判定以**是否被后续工作反复用作基线/出发点**及**是否构成范式转折**为依据；热度字段因本次来源未提供引用数而多为 `> 待核实`。

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Learning Agile and Dynamic Motor Skills for Legged Robots（ANYmal） | 2019 | Science Robotics（种子资源标注 ETH） | `> 待核实` | **同行评审期刊（A 级）** | 高（sim2real RL 腿足的起点性工作） | ★★★★★ | https://www.science.org/doi/10.1126/scirobotics.aau5872 | sim2real 强化学习奠基 |
| Learning Quadrupedal Locomotion over Challenging Terrain | 2020 | Science Robotics（种子资源标注 ETH） | `> 待核实` | **同行评审期刊（A 级）** | 高（学习式腿足运动奠基） | ★★★★★ | https://www.science.org/doi/10.1126/scirobotics.abc5986 ; http://arxiv.org/abs/2010.11251v1 | 学习式腿足运动奠基 [25] |
| RMA: Rapid Motor Adaptation for Legged Robots | 2021 | 来源 [73] | `> 待核实` | arXiv 预印本（B 级） | 高（在线自适应范式的锚点） | ★★★★★ | http://arxiv.org/abs/2107.04034v1 | 快速电机自适应 |
| Real-World Humanoid Locomotion with Reinforcement Learning | 2023 | 来源 [14] | `> 待核实` | arXiv 预印本（B 级） | 高（真机人形 RL 的代表性早期工作） | ★★★★★ | http://arxiv.org/abs/2303.03381v2 | 真机人形 RL locomotion |
| Learning Human-to-Humanoid Real-Time Whole-Body Teleoperation（H2O） | 2024 | 种子资源标注 IROS | `> 待核实` | 预印本 + 会议标注（B/A 级待核） | 高 | ★★★★★ | https://arxiv.org/abs/2403.04436 ; http://arxiv.org/abs/2403.04436v1 | 人形全身实时遥操作 [87] |
| OmniH2O | 2024 | 来源 [92] | `> 待核实` | arXiv 预印本（B 级） | 高 | ★★★★★ | http://arxiv.org/abs/2406.08858v1 | 通用灵巧人到人形遥操作与学习 |
| Learning Humanoid Locomotion over Challenging Terrain | 2024 | 来源 [13] | `> 待核实` | arXiv 预印本（B 级） | 中高 | ★★★★☆ | http://arxiv.org/abs/2410.03654v1 | 复杂地形人形 locomotion |
| HOVER | 2024 | 来源 [21] | `> 待核实` | arXiv 预印本（B 级） | 高 | ★★★★★ | http://arxiv.org/abs/2410.21229v2 | 通用神经全身控制器 |
| Online DCM Trajectory Generation for Push Recovery | 2019 | 来源 [57] | `> 待核实` | arXiv 预印本（B 级） | 中 | ★★★☆☆ | http://arxiv.org/abs/1909.10403v2 | 力矩控制人形推力恢复 |
| Push Recovery via Capture Point Feedback | 2017 | 来源 [58] | `> 待核实` | arXiv 预印本（B 级） | 中 | ★★★☆☆ | http://arxiv.org/abs/1710.10598v1 | 位置控制人形推力恢复 |
| A Receding Horizon Push Recovery Strategy（iCub） | 2017 | 来源 [59] | `> 待核实` | arXiv 预印本（B 级） | 中 | ★★★☆☆ | http://arxiv.org/abs/1705.10638v1 | 滚动时域恢复策略 |
| Online Balanced Motion Generation for Humanoid Robots | 2018 | 来源 [60] | `> 待核实` | arXiv 预印本（B 级） | 中 | ★★★☆☆ | http://arxiv.org/abs/1810.08388v1 | 在线平衡运动生成 |
| Whole-Body Geometric Retargeting for Humanoid Robots | 2019 | 来源 [82] | `> 待核实` | arXiv 预印本（B 级） | 中 | ★★★☆☆ | http://arxiv.org/abs/1909.10080v1 | 全身几何重定向 |
| Keep Rollin' — Whole-Body Motion Control and Planning for Wheeled Quadrupedal | 2018 | 来源 [30] | `> 待核实` | arXiv 预印本（B 级） | 中 | ★★★☆☆ | http://arxiv.org/abs/1809.03557v2 | 轮腿全身运动控制与规划 |
| Legged Robots that Keep on Learning | 2021 | 来源 [53] | `> 待核实` | arXiv 预印本（B 级） | 中 | ★★★☆☆ | http://arxiv.org/abs/2110.05457v1 | 真机在线微调 |
| Perspectives on Sim2Real Transfer for Robotics（R:SS 2020 Workshop 总结） | 2020 | 来源 [29] | `> 待核实` | 研讨会总结报告（B 级） | 中 | ★★★★☆ | http://arxiv.org/abs/2012.03806v1 | sim2real 共识性问题清单 |
| Reproducibility of Benchmarked DRL Tasks for Continuous Control | 2017 | 来源 [61] | `> 待核实` | arXiv 预印本（B 级） | 中 | ★★★★☆ | http://arxiv.org/abs/1708.04133v1 | 连续控制可复现性警示（负面结果价值高） |

**范式转变小结**：2019–2021 年的奠基工作确立了「大规模并行仿真 + 域随机化 + 策略蒸馏」的 sim2real 路线 [25][73]；2023 年该路线在人形上完成真机验证 [14]；2024 年后重心转向统一全身控制器与动作接口 [21][87]。与此同时，模型式（MPC / 降阶模型）路线并未消亡，2025 年仍有 [15][17][24] 发表。

---

## 七、数据集、基准与开放问题

### 7.1 数据集与基准

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| HumanoidBench | 2024 | 来源 [22][74] | `> 待核实` | arXiv 预印本（B 级） | 高（**被第三方复用于评测**，见 [75]） | ★★★★★ | https://arxiv.org/abs/2403.10506 | 人形全身 locomotion+manipulation 仿真基准 |
| MuJoCo MPC for Humanoid Control: Evaluation on HumanoidBench | 2024 | 来源 [75] | `> 待核实` | arXiv 预印本（B 级） | 中高（作为 HumanoidBench 的第三方使用证据） | ★★★★☆ | http://arxiv.org/abs/2408.00342v1 | 在 HumanoidBench 上评测模型式 MPC |
| Robot Policy Evaluation for Sim-to-Real Transfer: A Benchmarking Perspective | 2025 | 来源 [76] | `> 待核实` | arXiv 预印本（B 级） | 中（直指评测方法论缺失） | ★★★★★ | http://arxiv.org/abs/2508.11117v1 | sim2real 评测基准化的方法论 |
| PHUMA: Physically Reliable Humanoid Locomotion Dataset | 2025 | 来源 [85] | citations=12 [85] | arXiv 预印本（B 级） | 中（citations=12）[85] | ★★★☆☆ | https://arxiv.org/abs/2510.26236 | 物理可靠的人形 locomotion 数据 |
| Motion-X | 2023 | 来源 [95] | `> 待核实` | arXiv 预印本（B 级） | 中高（大规模 3D 全身动作数据） | ★★★★☆ | http://arxiv.org/abs/2307.00818v2 | 大规模表达性全身人体动作数据 |
| AMASS（mocap） | — | 种子资源 | `> 待核实` | 官方数据集主页（B 级） | 高（多篇工作以其为动作来源，如 [85] 指出其稀缺昂贵） | ★★★★★ | https://amass.is.tue.mpg.de/ | 人体动捕聚合数据（未被本次编号来源收录，来自种子清单） |
| LAFAN1 / LAFAN1 retargeted | — | Ubisoft（种子资源） | `> 待核实` | 官方数据集仓库（B 级） | 高 | ★★★★★ | https://github.com/ubisoft/ubisoft-laforge-animation-dataset | 人形动作先验 |
| The Open Ant | 2026 | 来源 [4] | `> 待核实` | arXiv 预印本（B 级） | 中（主张仿真主导导致真机迁移不确定） | ★★★☆☆ | http://arxiv.org/abs/2607.18488v1 | RL 研究的实体机器人平台 |

- **关键结构性缺口（可核查）**：PHUMA 明确指出既有方法依赖 AMASS 等高质量动捕数据，而这类数据**稀缺且昂贵**，限制可扩展性与多样性 [85]。这是数据集层面最明确的瓶颈陈述。
- **对比不可行性**：HumanoidBench 是目前唯一在本次来源中可确认「有第三方在其上评测」的人形基准（[75] 的标题即为 Evaluation on HumanoidBench）[22][75]。除此之外，**本次来源未提供任何人形 locomotion 的可比榜单**，因此任何「SOTA」表述都应视为论文自述。

### 7.2 开放问题与争议

1. **sim2real gap 仍未闭合**：既有系统剖析 [37]，也有对 sim2real 在精细任务上根本局限的质疑 [51]，以及强调「仿真主导使真机迁移对算法与研究者都不确定」的立场 [4]。
2. **评测不可复现**：可复现性警示早在 2017 年已提出 [61]，2025 年仍有专文主张 sim2real 策略评测需要基准化视角 [76]，说明问题长期未解。**争议点**：论文宣称的成功率缺乏统一口径（任务数、硬件、仿真/真机）——本次抽取块中**无任何一篇提供可横向比较的定量表格**。
3. **恢复与安全被低估**：跌倒恢复 [28]、站立 [47]、安全约束 RL [71] 均存在，但在地形/敏捷类工作中的整合程度 `> 待核实`。
4. **失效机理研究稀缺**：Failure Mechanisms and Risk Estimation for Legged Robot Locomotion on Granular Slopes 通过可倾斜颗粒床系统测量速度与失效，属**少见的负面/失效导向研究** [55]。
5. **硬件成本与可获得性**：3D 打印低成本路线 [20]、全尺寸开源平台 [18]、开源 loco-manipulation 平台 [23] 的出现本身反映了硬件瓶颈。
6. **术语歧义污染检索**：见 §8.3。

---

## 八、建议关注清单（Watchlist）

### 8.1 技术路线（按优先级）

| 优先级 | 关注对象 | 理由 | 证据 |
|---|---|---|---|
| P0 | 统一神经全身控制器：HOVER / UniTracker / TWIST | 决定人形「一个策略还是多个策略」的架构选择 | [21][65][86] |
| P0 | 分钟级 sim2real 训练 | 直接改变迭代速度与实验设计空间 | [12][19] |
| P0 | 动作重定向质量：Retargeting Matters | 可能是下游指标的主要混淆变量，影响所有模仿式结论 | [83] |
| P1 | 分层降阶 MPC：Hierarchical Reduced-Order MPC / RoMoCo | 学习式并未取代模型式，混合路线可能最优 | [15][24] |
| P1 | human-to-humanoid 遥操作数据栈：H2O / OmniH2O / CHILD | 数据来源与部署接口双重价值 | [3][87][92] |
| P1 | 稀疏落脚与跑酷：BeamDojo / Humanoid Parkour Learning | 敏捷性能力分水岭 | [67][69] |
| P2 | 恢复与安全：FR-Net / standing-up / Safe RL | 真实部署前置条件，当前投入相对不足 | [28][47][71] |
| P2 | 无机器人演示数据采集：HMI | 若成立可大幅降低数据成本 | [64] |

### 8.2 基础设施（需实际核查后再采信）

- **仿真与训练**：IsaacLab、legged_gym、unitree_rl_gym `> 待核实`（star/活跃度/文档质量未经核查）
- **基准**：HumanoidBench [22][74] —— 当前唯一可确认有第三方使用的可复现基准
- **数据**：AMASS、LAFAN1、Motion-X [95]、PHUMA [85]
- **批判性阅读必读**：[37]（sim2real 失败来源）、[51]（sim2real 局限）、[61]（可复现性）、[76]（评测基准化）、[83]（重定向的重要性）

### 8.3 检索噪声与污染警示（重要方法论提示）

本次来源列表中存在**明显跨领域误召回**，直接暴露了该主题的检索脆弱性：

- **"H1" 歧义**：来源 [6][7][8] 均为 H1 粒子物理/量能器与 HERA 实验论文，与 Unitree H1 无任何关系。
- **"G1" 歧义**：来源 [10] 的 "G1" 指视觉语言模型在游戏环境中的 RL 训练，与 Unitree G1 机器人无关 [10]。
- **"Domain randomization" 跨领域**：来源 [34] 属神经影像分析（eess.IV）[34]。
- **其他无关条目**：NLP/评测类 [38][40][43][45]、天体物理 [88][90][91]、音频隐私 [89]、对话系统 [32]、情感 RL 综述 [70]、GPT-6-Astra 机器人操作 [77]（属操作而非腿足运动）等。

> **结论**：任何「按关键词统计前沿趋势」的做法在本领域都会因机器人型号命名（H1/G1）与通用术语（domain randomization）的歧义而严重失真。建议后续检索强制加入 `cs.RO` 分类限定与硬件型号消歧。

---

## 参考来源

**引用编号与链接（本报告实际引用）**

[3] CHILD (Controller for Humanoid Imitation and Live Demonstration): a Whole-Body Humanoid Teleoperation System — http://arxiv.org/abs/2508.00162v2
[4] The Open Ant: A Robot Platform for Reinforcement Learning Research — http://arxiv.org/abs/2607.18488v1
[6] The Electronics of the H1 Lead/Scintillating-Fibre Calorimeters — http://arxiv.org/abs/physics/9812042v1
[7] Measurement of the Charm and Beauty Structure Functions using the H1 Vertex Detector at HERA — http://arxiv.org/abs/0907.2643v2
[8] Measurement of F_2^ccbar and F_2^bbbar at High Q^2 using the H1 Vertex Detector at HERA — http://arxiv.org/abs/hep-ex/0411046v1
[10] G1: Bootstrapping Perception and Reasoning Abilities of Vision-Language Model via Reinforcement Learning — http://arxiv.org/abs/2505.13426v1
[12] Learning Sim-to-Real Humanoid Locomotion in 15 Minutes — http://arxiv.org/abs/2512.01996v1
[13] Learning Humanoid Locomotion over Challenging Terrain — http://arxiv.org/abs/2410.03654v1
[14] Real-World Humanoid Locomotion with Reinforcement Learning — http://arxiv.org/abs/2303.03381v2
[15] Hierarchical Reduced-Order Model Predictive Control for Robust Locomotion on Humanoid Robots — http://arxiv.org/abs/2509.04722v1
[16] A Framework for Scalable Heterogeneous Multi-Agent Adversarial Reinforcement Learning in IsaacLab — http://arxiv.org/abs/2510.01264v1
[17] Bracing for Impact: Robust Humanoid Push Recovery and Locomotion with Reduced Order Models — http://arxiv.org/abs/2505.11495v2
[18] ARTEMIS: An Open-Source, Full-Sized Humanoid Robot for Dynamic Locomotion — https://doi.org/10.1109/Humanoids65713.2025.11203020
[19] Learning Sim-to-Real Humanoid Locomotion in 15 Minutes — https://arxiv.org/abs/2512.01996
[20] Demonstrating Berkeley Humanoid Lite: An Open-source, Accessible, and Customizable 3D-printed Humanoid Robot — https://arxiv.org/abs/2504.17249
[21] HOVER: Versatile Neural Whole-Body Controller for Humanoid Robots — http://arxiv.org/abs/2410.21229v2
[22] HumanoidBench: Simulated Humanoid Benchmark for Whole-Body Locomotion and Manipulation — https://arxiv.org/abs/2403.10506
[23] Dynamic Loco-manipulation on HECTOR: Humanoid for Enhanced ConTrol and Open-source Research — https://arxiv.org/abs/2312.11868
[24] RoMoCo: Robotic Motion Control Toolbox for Reduced-Order Model-Based Locomotion on Bipedal and Humanoid Robots — https://arxiv.org/abs/2509.19545
[25] Learning Quadrupedal Locomotion over Challenging Terrain — http://arxiv.org/abs/2010.11251v1
[26] ViTAL: Vision-Based Terrain-Aware Locomotion for Legged Robots — http://arxiv.org/abs/2212.01246v1
[27] Learning Locomotion on Complex Terrain for Quadrupedal Robots with Foot Position Maps and Stability Rewards — http://arxiv.org/abs/2604.02744v1
[28] FR-Net: Learning Robust Quadrupedal Fall Recovery on Challenging Terrains through Mass-Contact Prediction — http://arxiv.org/abs/2509.11504v1
[29] Perspectives on Sim2Real Transfer for Robotics: A Summary of the R:SS 2020 Workshop — http://arxiv.org/abs/2012.03806v1
[30] Keep Rollin' - Whole-Body Motion Control and Planning for Wheeled Quadrupedal Robots — http://arxiv.org/abs/1809.03557v2
[31] Guided Curriculum Learning for Walking Over Complex Terrain — http://arxiv.org/abs/2010.03848v2
[32] Deep Reinforcement Learning for Multi-Domain Dialogue Systems — http://arxiv.org/abs/1611.08675v1
[34] Domain-randomized deep learning for neuroimage analysis — http://arxiv.org/abs/2507.13458v1
[37] Sim-to-Real Transfer in Deep Reinforcement Learning for Bipedal Locomotion — http://arxiv.org/abs/2511.06465v1
[38] Overview of AuTexTification at IberLEF 2023 — http://arxiv.org/abs/2309.11285v1
[40] UZH_CLyp at SemEval-2023 Task 9 — http://arxiv.org/abs/2303.01194v2
[41] Robot Parkour Learning — http://arxiv.org/abs/2309.05665v2
[42] AI-Based Terrain Adaptation Algorithms for Walking Robots — https://openalex.org/W7217170495
[43] MarsEclipse at SemEval-2023 Task 3 — http://arxiv.org/abs/2304.14339v1
[45] Strategies to Harness the Transformers' Potential: UNSL at eRisk 2023 — http://arxiv.org/abs/2310.19970v1
[46] Towards Miniature Humanoid Tele-Loco-Manipulation Using Virtual Reality and Reinforcement Learning — http://arxiv.org/abs/2607.20399v1
[47] Learning Humanoid Standing-up Control across Diverse Postures — http://arxiv.org/abs/2502.08378v2
[48] Humanoid Whole-Body Badminton via an Annealed Reinforcement Learning Curriculum — http://arxiv.org/abs/2511.11218v4
[49] Bridging the Sim2Real Gap: Vision Encoder Pre-Training for Visuomotor Policy Transfer — http://arxiv.org/abs/2501.16389v2
[51] The Importance and the Limitations of Sim2Real for Robotic Manipulation in Precision Agriculture — http://arxiv.org/abs/2008.03983v1
[52] ATRos: Learning Energy-Efficient Agile Locomotion for Wheeled-legged Robots — http://arxiv.org/abs/2510.09980v1
[53] Legged Robots that Keep on Learning: Fine-Tuning Locomotion Policies in the Real World — http://arxiv.org/abs/2110.05457v1
[54] Locomotion Beyond Feet — http://arxiv.org/abs/2601.03607v1
[55] Failure Mechanisms and Risk Estimation for Legged Robot Locomotion on Granular Slopes — http://arxiv.org/abs/2603.06928v2
[57] Online DCM Trajectory Generation for Push Recovery of Torque-Controlled Humanoid Robots — http://arxiv.org/abs/1909.10403v2
[58] Push Recovery of a Position-Controlled Humanoid Robot Based on Capture Point Feedback Control — http://arxiv.org/abs/1710.10598v1
[59] A Receding Horizon Push Recovery Strategy for Balancing the iCub Humanoid Robot — http://arxiv.org/abs/1705.10638v1
[60] Online Balanced Motion Generation for Humanoid Robots — http://arxiv.org/abs/1810.08388v1
[61] Reproducibility of Benchmarked Deep Reinforcement Learning Tasks for Continuous Control — http://arxiv.org/abs/1708.04133v1
[63] The Role of Domain Randomization in Training Diffusion Policies for Whole-Body Humanoid Control — http://arxiv.org/abs/2411.01349v1
[64] Humanoid Manipulation Interface: Humanoid Whole-Body Manipulation from Robot-Free Demonstrations — http://arxiv.org/abs/2602.06643v2
[65] UniTracker: Learning Universal Whole-Body Motion Tracker for Humanoid Robots — http://arxiv.org/abs/2507.07356v3
[66] Humanoid Whole-Body Manipulation via Active Spatial Brain and Generalizable Action Cerebellum — http://arxiv.org/abs/2605.21133v2
[67] Humanoid Parkour Learning — http://arxiv.org/abs/2406.10759v2
[68] Agile But Safe: Learning Collision-Free High-Speed Legged Locomotion — http://arxiv.org/abs/2401.17583v3
[69] BeamDojo: Learning Agile Humanoid Locomotion on Sparse Footholds — http://arxiv.org/abs/2502.10363v3
[70] Emotion in Reinforcement Learning Agents and Robots: A Survey — http://arxiv.org/abs/1705.05172v1
[71] Safe Reinforcement Learning for Legged Locomotion — http://arxiv.org/abs/2203.02638v1
[72] Learning Inertial Odometry for Dynamic Legged Robot State Estimation — http://arxiv.org/abs/2111.00789v1
[73] RMA: Rapid Motor Adaptation for Legged Robots — http://arxiv.org/abs/2107.04034v1
[74] HumanoidBench: Simulated Humanoid Benchmark for Whole-Body Locomotion and Manipulation — http://arxiv.org/abs/2403.10506v2
[75] MuJoCo MPC for Humanoid Control: Evaluation on HumanoidBench — http://arxiv.org/abs/2408.00342v1
[76] Robot Policy Evaluation for Sim-to-Real Transfer: A Benchmarking Perspective — http://arxiv.org/abs/2508.11117v1
[77] Robot Manipulation with GPT-6-Astra: Body Knowledge, Experience Reuse, Emergent Skills, and Sim2Real Transfer — http://arxiv.org/abs/2609.31770v1
[78] Dense Temporal Motion Retargeting for Legged Robots — http://arxiv.org/abs/2609.38617v1
[79] Spatio-Temporal Motion Retargeting for Quadruped Robots — http://arxiv.org/abs/2404.11557v3
[80] Simulating Infant First-Person Sensorimotor Experience via Motion Retargeting from Babies to Humanoids — http://arxiv.org/abs/2604.27583v2
[81] From Language to Locomotion: Retargeting-free Humanoid Control via Motion Latent Guidance — http://arxiv.org/abs/2510.14952v2
[82] Whole-Body Geometric Retargeting for Humanoid Robots — http://arxiv.org/abs/1909.10080v1
[83] Retargeting Matters: General Motion Retargeting for Humanoid Motion Tracking — http://arxiv.org/abs/2510.02252v1
[84] Kinodynamic Motion Retargeting for Humanoid Locomotion via Multi-Contact Whole-Body Trajectory Optimization — http://arxiv.org/abs/2603.09956v2
[85] PHUMA: Physically Reliable Humanoid Locomotion Dataset — https://arxiv.org/abs/2510.26236
[86] TWIST: Teleoperated Whole-Body Imitation System — http://arxiv.org/abs/2505.02833v1
[87] Learning Human-to-Humanoid Real-Time Whole-Body Teleoperation — http://arxiv.org/abs/2403.04436v1
[88] Experimental Summary of the Moriond 2024 conference — http://arxiv.org/abs/2409.07120v1
[89] NTU-NPU System for Voice Privacy 2024 Challenge — http://arxiv.org/abs/2410.02371v1
[90] Discovery Opportunities with Gravitational Waves -- TASI 2024 Lecture Notes — http://arxiv.org/abs/2409.08956v1
[91] Atmospheric entry and fragmentation of small asteroid 2024 BX1 — http://arxiv.org/abs/2403.00634v2
[92] OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning — http://arxiv.org/abs/2406.08858v1
[94] CLOT: Closed-Loop Global Motion Tracking for Whole-Body Humanoid Teleoperation — http://arxiv.org/abs/2602.15060v2
[95] Motion-X: A Large-scale 3D Expressive Whole-body Human Motion Dataset — http://arxiv.org/abs/2307.00818v2
[97] LeCAR-Lab/human2humanoid — https://github.com/LeCAR-Lab/human2humanoid

**领域种子资源（未被编号来源收录，来自人工维护清单，需另行核查）**

- leggedrobotics/legged_gym — https://github.com/leggedrobotics/legged_gym
- unitreerobotics/unitree_rl_gym — https://github.com/unitreerobotics/unitree_rl_gym
- NVlabs/ProtoMotions — https://github.com/NVlabs/ProtoMotions
- isaac-sim/IsaacLab — https://github.com/isaac-sim/IsaacLab
- AMASS — https://amass.is.tue.mpg.de/
- LAFAN1 — https://github.com/ubisoft/ubisoft-laforge-animation-dataset
- Learning Human-to-Humanoid Real-Time Whole-Body Teleoperation (H2O) — https://arxiv.org/abs/2403.04436
- Learning Quadrupedal Locomotion over Challenging Terrain — https://www.science.org/doi/10.1126/scirobotics.abc5986
- Learning Agile and Dynamic Motor Skills for Legged Robots (ANYmal) — https://www.science.org/doi/10.1126/scirobotics.aau5872

---

> **报告局限声明**：本次结构化抽取块中 `heat`（引用数、star、下载量、榜单排名）字段大面积为空，因此**本报告不具备任何跨论文的定量比较能力**，所有「SOTA」「最强」类表述均被有意规避。四类证据中的「热度证据」在绝大多数条目上只能标注 `> 待核实`。若需形成可用于选型决策的结论，必须先补做以下核查：(1) 各预印本是否已中稿及 venue 等级；(2) 各开源仓库的 star 数、最近提交时间、权重/数据许可；(3) HumanoidBench 榜单的实际参与与排名情况。

---

*Generated by research-bot · topic=`embodied-humanoid` · depth=`standard` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading · model=`deepseek-v4-flash` · sources=97 · duration=339s · 2026-10-06T22:30:15+00:00*
