# 具身智能（Embodied AI）方法谱系与前沿进展调研报告

**元信息**：日期 2026-10-05（UTC）｜领域：具身智能（Embodied AI）/ 视觉-语言-动作模型（VLA）/ 机器人学习与仿真｜检索源：编号来源 108 条（[1]–[108]），其中与主题直接相关约 60 条；另有种子资源 12 条（论文 5、开源项目 4、数据集 3，未实时核实）｜证据分级：A–E（本报告绝大多数条目为 arXiv 预印本，等级 B；未见同行评审 venue 字段）

> **阅读须知（证据纪律）**
> 1. 本次结构化发现中，`authority` 字段填写的是 **arXiv 分类（cs.RO / cs.LG / cs.CV …），不等于同行评审 venue**。凡未标注会议者，本报告一律按 **B 级（arXiv 预印本）** 处理。
> 2. 结构化发现中所有条目的 `heat`（引用数 / GitHub star / 下载量）字段为空，且无任何榜单排名数据。因此本报告所有条目的 **热度证据一律标注 `> 待核实`**，绝不填充数字。
> 3. 本次抽取结果存在明显**检索噪声（假阳性）**：q1、q3、q4、q5、q6 的 findings 中重复出现与具身智能无关的条目，例如短视频参与度预测挑战 [2]、基础模型透明度指数 [3]、图像超分辨率挑战 [21]、越南语法律问答 [22]、LMM 视觉质量比较 [43]、新闻主观性检测 [85]、实时系统 RowHammer [101]、中微子截面 [11] 等。这些条目已在正文剔除，仅在此说明，以免读者误以为检索覆盖全面。
> 4. 少数来源的题名/内容需人工复核（例如 [79] 提及的模型名称 [79]、[60] 的发表时间 [60]），已在对应位置标注 `> 待核实`。

---

## 摘要（Executive Summary）

1. **主线一：VLA 从"单本体模仿"走向"跨本体、跨域统一基础模型"。** 综述层面已出现多篇系统性梳理 [45][96][97]；工程侧出现宣称在自动驾驶与具身智能**双域同时达成 SOTA** 的跨本体基础模型（MiMo-Embodied，论文自述在 17 个具身基准刷新记录）[99]，以及面向通用人形机器人的开放基础模型 GR00T N1 [100] 与开源 VLA 基线 OpenVLA [63]。**注意：上述"SOTA/刷新记录"均为论文自述（B 级），缺少第三方复现。**

2. **主线二：对"大模型即策略"的三类修正同时出现。**（a）**效率与实时性**：有工作宣称在单张消费级 GPU 上以 30 Hz 帧率、最高 480 Hz 轨迹频率运行 pi0 级多视角 VLA [61]，以及 Tiny-Scale VLA 的适配范式 [107]；（b）**推理增强**：把"思考"引入动作生成，如 thinking-with-image 推理 [105]、动作与运动图像扩散联合学习 [64]、扩散策略轨迹筛选 [31]；（c）**安全与可控性**：具身安全综述系统性梳理风险/攻击/防御 [94]，并在推理期通过注意力偏置引导 VLA 关注安全关键目标（以自动驾驶 VLA 为对象）[95]。

3. **主线三：世界模型成为与 VLA 并行的独立路线。** 代表节点包括生成式交互环境 Genie [14]、以预训练视觉特征构建的可零样本规划世界模型 DINO-WM [13]、面向机器人操作的世界基础平台 Genie Envisioner [10]、以及针对"生成视频物理点不一致"问题提出几何增强的 GEM-4D [4]。但"世界模型是否等于可规划仿真器"仍存争议，综述性讨论见 [9][17][8]，神经闭环传感器仿真见 [12]。

4. **仿真与 Sim2Real：能力提升与评测滞后并存。** GPU 并行仿真框架 Isaac Lab 已形成论文级描述 [86]；而评测侧有工作明确指出"仿真基准进步显著，但真实世界泛化策略的评估明显滞后" [44]，早期社区共识（R:SS 2020 workshop 总结）[78] 与领域局限性讨论（精密农业）[80] 仍被反复引用；近期路线转向"在感知层做域对齐"（视觉编码器预训练 [82]、深度扩散校正 [83]、生成式音频补齐多模态 [20]）。

5. **数据与基准：从"更大"转向"更诊断性"。** 大规模真机数据集 DROID [40]、日常活动基准 BEHAVIOR-1K（1000 项活动）[51]、以及基于 LIBERO 的诊断型基准（指令改写鲁棒性 LIBERO-Para [41]、闭环视觉鲁棒性 LIBERO-VPro [42]）构成近期重点；统一评测平台出现 Embodied Arena [46]、RoboDojo（sim-and-real 统一）[49]。**跨榜单口径不可比是当前最突出的方法论问题** [44][41]。

6. **开放争议（证据强度分层）**：数据瓶颈与跨本体扩展律 [47]（弱证据：仅题名级）；安全与"可信认证" [94][75]（B 级综述/框架）；复现困难与负面结果——**本次检索未获得直接的一手负面结果报告，标注 `> 待核实`**。

---

## 一、关键前沿进展（近 1–2 年，2024–2026）

> 下表所有条目的**热度证据均为 `> 待核实`**（检索结果无引用数/star 数据）。"权威"按证据等级 + arXiv 分类给出（arXiv 分类非同行评审 venue）。

### 1.1 VLA / 具身基础模型

| 名称 | 时间 | 一句话贡献 | 权威 | 关注度 | 推荐度 |
|---|---|---|---|---|---|
| MiMo-Embodied（X-Embodied 基础模型技术报告）[99] | 2025 | 宣称首个在自动驾驶与具身智能双域同时 SOTA 的跨本体基础模型，覆盖任务规划/可供性/空间等 17 个具身基准（**论文自述**） | B（arXiv cs.RO，预印本） | 中（属"跨本体统一"核心议题，但无量化信号） | ★★★★（跨本体路线的重要信号，需第三方复现） |
| GR00T N1 [100] | 2025 | 面向通用人形机器人的开放基础模型 | B（arXiv 预印本） | 中（人形+开放权重方向枢纽，缺量化信号） | ★★★★（人形基础模型必读基线） |
| OpenVLA [63] | 2024 | 开源 VLA 模型，成为大量后续工作对比基线 | B（arXiv 预印本） | 中（开源基线属性，缺量化信号） | ★★★★★（复现与二次开发的起点） |
| VLA-Adapter [107] | 2025 | 提出 Tiny-Scale VLA 的有效适配范式（降参数量路线） | B（arXiv 预印本） | 中 | ★★★★（算力受限场景的可行方向） |
| Running VLAs at Real-time Speed [61] | 2025 | 宣称单张消费级 GPU 上 30 Hz 帧率、最高 480 Hz 轨迹频率运行 pi0 级多视角 VLA（**论文自述**） | B（arXiv cs.RO，预印本） | 高（直击 VLA 部署痛点，但无量化信号） | ★★★★★（实时性是落地第一门槛） |
| VLA-Thinker [105] | 2026 | 通过 thinking-with-image 推理增强 VLA | B（arXiv 预印本） | 中 | ★★★★（"推理→动作"融合的代表） |
| Robotic VLA + Motion Image Diffusion [64] | 2025 | 指出 VLA 仅模仿专家轨迹、缺乏预测性运动推理，联合运动图像扩散以补足 | B（arXiv cs.RO，预印本） | 中 | ★★★★（与世界模型路线交叉） |
| Inference-Time Attention Steering for VLA Driving [95] | 2026 | 在 pre-softmax 加有界加性注意力偏置，推理期把注意力导向安全关键对象、**无需重训练** | B（arXiv cs.CV，预印本） | 中 | ★★★（安全可控性思路，目前仅驾驶域） |
| VLA 综述（Embodied AI）[97] / （Embodied Manipulation）[96] / 具身智能总览 [45] | 2024–2025 | 三篇不同侧重的方法学与生态综述，可作为分类骨架 | B（arXiv 预印本，v8 版本表明持续更新） | 中（综述通常为该方向入口，无量化信号） | ★★★★★（入门与 taxonomy 首选） |

**分析**：近两年 VLA 的"新范式"并非单点突破，而是**四条补偿性修正**——跨本体/跨域（[99][100]）、效率（[61][107]）、推理（[105][64]）、安全（[94][95]）。四者的共同前提是承认"端到端大模型直接映射观测→动作"存在泛化、速度与安全缺口。

### 1.2 世界模型

| 名称 | 时间 | 一句话贡献 | 权威 | 关注度 | 推荐度 |
|---|---|---|---|---|---|
| Genie [14] | 2024 | 生成式交互环境，从无标注视频学可控世界模型 | B（arXiv 预印本） | 高（生成式世界模型标志性节点，无量化信号） | ★★★★★（该路线奠基性预印本） |
| DINO-WM [13] | 2024 | 在预训练视觉特征上建世界模型，实现零样本规划 | B（arXiv 预印本） | 中高 | ★★★★★（"免训练表征 + 规划"最实用分支） |
| Genie Envisioner [10] | 2025 | 把策略学习、评估、仿真统一进单一视频生成框架（GE-Base 为指令条件视频扩散模型） | B（arXiv cs.RO） | 中高 | ★★★★★（世界模型即"统一平台"的代表主张） |
| GEM-4D [4] | 2026 | 指出视频世界模型无法在时间上一致跟踪同一物理点，导致"看起来合理但无法执行"，用几何增强修正 | B（arXiv cs.CV） | 中（直击该路线核心批评） | ★★★★★（世界模型可否用于操作的判据性工作） |
| UniSim [12] | 2023 | 神经闭环传感器仿真器（仿真→真实感知域对齐） | B（arXiv 预印本） | 中 | ★★★★（与 Sim2Real 强相关） |
| Sora 与世界模型综述 [9][17] + 决策生成模型综述 [8] | 2024–2025 | 系统讨论"通用世界模型"的边界与文本/视频生成的模型化能力 | B（arXiv 预印本） | 中 | ★★★★（厘清"世界模型≠视频生成"） |

**分析**：世界模型路线当前的**最强证据是自我批评**：[4] 明确指出视频世界模型生成的未来"物理点不可跨时间一致跟踪"，因此"看起来合理却无法可靠驱动动作执行"——这是该路线从"生成质量"转向"可执行性"的关键判据。

### 1.3 人形全身控制与操作（近 1–2 年）

| 名称 | 时间 | 一句话贡献 | 权威 | 关注度 | 推荐度 |
|---|---|---|---|---|---|
| Robot Trains Robot [16] | 2025 | 面向人形的真机策略自适应与学习，指出"真机 RL 从零或从预训练策略适配仍罕见" | B（arXiv cs.RO） | 中高（点出真机学习缺口） | ★★★★★（真机 RL 现状的诚实描述） |
| Humanoid Whole-Body Badminton（退火 RL 课程）[65] | 2025 | 全身动态任务（羽毛球）的课程式 RL | B（arXiv 预印本） | 中 | ★★★（动态全身控制案例） |
| CHILD：全身人形遥操作系统 [67] | 2025 | 控制器 + 实时演示的全身遥操作 | B（arXiv 预印本） | 中 | ★★★★（数据采集基础设施） |
| Humanoid Manipulation Interface [68] | 2026 | 无机器人本体也可采集演示的全身操作接口 | B（arXiv 预印本） | 中 | ★★★★（降低数据采集成本） |
| Learning Humanoid Standing-up Control across Diverse Postures [69] | 2025 | 多姿态起身控制 | B（arXiv 预印本） | 中 | ★★★ |
| Sim-to-Real Humanoid Locomotion in 15 Minutes [72] | 2025 | 宣称 15 分钟内完成 sim-to-real 人形行走（**题名即宣称，需核实**） | B（arXiv 预印本） | 中 | ★★★★（Sim2Real 效率的极端案例） |
| Miniature Humanoid Tele-Loco-Manipulation（VR + RL）[70] | 2026 | 小型人形遥操作移动-操作 | B（arXiv 预印本） | 低—中 | ★★ |
| HANDO [93] | 2025 | 分层自主导航 + 灵巧全向移动操作 | B（arXiv 预印本） | 低—中 | ★★★ |

---

## 二、方法谱系（模块化 / 端到端 / 基础模型 / 世界模型）

### 谱系一：模块化（感知—规划—控制分离，以模仿学习/RL 单点突破）
- **承上**：经典生成式/模型化控制与 RL 数据效率研究构成"前史"——一次示范的导航 RL [1]、稀疏奖励下的多目标模型化策略搜索 [18]、面向"监督者在学习中不断演化"的 on-policy 模仿学习 [19]。
- **启下**：状态空间交互式模仿学习 [29]、交互式（DAgger 系）扩展到异构人类示范的偏好+表征学习 [28]、跨形态示范迁移 [36]，为后续"数据从哪来"的问题铺垫。
- **证据轴**：热度 `> 待核实`｜权威 B（均为 arXiv 预印本，[18][19] 年份分别为 2018/2019，属早期工作）｜关注度 低—中（经典但本次无量化信号）｜推荐度 ★★★（做模仿学习谱系梳理时必引，否则可略读）。

### 谱系二：端到端（视觉/多模态观测 → 动作，生成式动作建模兴起）
- **代表**：扩散策略系的轨迹选择改进 [31]；多模态数据端到端策略（音频-视觉 in-the-wild 操作）[38]；自监督多物体关键点表示 [39]；稠密绳结等长时程操作的可学习关键点 [32]。
- **承上启下**：相比谱系一，其变化在于 **①动作分布建模从"确定性回归"转向"生成式多模态"**，[31] 明确指出"捕捉数据多模态性是行为克隆长期开放难题"；**②输入模态从视觉扩展到音频/触觉/关键点等任务相关表征**。
- **证据轴**：热度 `> 待核实`｜权威 B（arXiv，cs.RO/cs.LG）｜关注度 中（扩散策略是当前主流范式）｜推荐度 ★★★★（[31] 对多模态动作分布问题陈述清晰）。

### 谱系三：基础模型 / VLA（大规模预训练 + 指令条件动作）
- **代表**：[63][100][99]，以及综述骨架 [45][96][97]。
- **变化点**：从"单任务、单本体策略"→"跨本体、跨域、指令条件策略"；[99] 的代表性主张是**自动驾驶与具身操作用同一基础模型**，[100] 面向人形，[61] 解决推理速度。
- **证据轴**：热度 `> 待核实`｜权威 B（arXiv 预印本；[99] 为技术报告性质，"SOTA/刷新记录"为自述）｜关注度 高（VLA 是当前社区焦点议题，但缺量化信号）｜推荐度 ★★★★★（谱系主干）。

### 谱系四：世界模型 / 统一动作空间（在潜空间或视频空间"想象未来"再行动）
- **代表**：Genie [14]、DINO-WM [13]、Genie Envisioner [10]、GEM-4D [4]、UniSim [12]；讨论性综述 [8][9][17]。
- **与 VLA 的关系与分歧**：
  - **互补论**：世界模型提供"预测性运动推理"，弥补 VLA 只模仿轨迹的缺陷 [64]；Genie Envisioner 更进一步，试图把**策略学习、评估、仿真统一进一个视频生成框架** [10]。
  - **质疑论**：[4] 从物理点一致性出发，指出生成视频"plausible 但缺乏可靠动作执行所需的物理 grounding"——即世界模型若不能保持**跨时间几何一致性**，就不能替代仿真器。
  - **待核实**：两派目前都缺少第三方统一口径对比（无共用 benchmark 结果），本报告无法给出"A 优于 B"的结论。
- **证据轴**：热度 `> 待核实`｜权威 B（arXiv 预印本）｜关注度 高（Genie 系与"世界模型是否等于仿真器"争论活跃）｜推荐度 ★★★★★（争议本身即研究机会）。

### 谱系五：Sim2Real 方法学（横切）
感知层域对齐 [82][83][20] → 策略/评测层 [44][78][80] → 极端效率宣称 [72]。**该谱系尚无统一定论**，详见第七章。

---

## 三、仿真平台与基准对比

> 说明：本表只列本次检索**有编号来源**支撑的平台与基准；仅有仓库链接而无来源编号的种子项目在第五章单列。

| 平台 / 基准 | 类型 | 关键能力与证据 | 热度 | 权威 | 关注度 | 推荐度 |
|---|---|---|---|---|---|---|
| Isaac Lab [86] | GPU 并行仿真/学习框架 | 多模态机器人学习的 GPU 加速仿真框架（题名级证据） | `> 待核实` | B（arXiv 预印本；官方仓库为种子资源） | 高（GPU 并行已成大规模训练的默认前提） | ★★★★★ |
| Isaac Sim | 物理仿真器 | **本次检索无编号来源支撑，`> 待核实`** | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` |
| MuJoCo / Genesis / Habitat / RoboSuite | 仿真器 | **本次检索未获得这些平台的编号来源证据，`> 待核实`**；Genesis 仅有种子仓库链接 | `> 待核实` | `> 待核实`（Genesis 仓库为种子资源，未核实 star/活跃度） | `> 待核实` | ★★（建议后续单独立项检索） |
| RoboDojo [49] | sim-and-real 统一基准 | 面向通用操作策略的综合评测，同时覆盖仿真与真实 | `> 待核实` | B（arXiv 预印本） | 中高（"sim-real 双轨评测"正成为共识） | ★★★★★ |
| Embodied Arena [46] | 统一评测平台 | 综合、统一、可演进的具身智能评测平台 | `> 待核实` | B（arXiv 预印本） | 中高 | ★★★★ |
| EmbodiedCity [50] | 城市级具身智能体平台 | 真实城市环境中的具身智能体基准平台 | `> 待核实` | B（arXiv 预印本） | 中 | ★★★ |
| BEHAVIOR-1K [51] | 人本日常活动基准 | 1000 项日常活动 + 真实仿真 | `> 待核实` | B（arXiv 预印本；官方站点为种子资源） | 中高 | ★★★★★ |
| LIBERO-Para [41] / LIBERO-VPro [42] | 诊断型基准 | 前者测指令改写鲁棒性、后者测闭环视觉鲁棒性 | `> 待核实` | B（arXiv 预印本，cs.LG / cs.RO） | 中高（直指 VLA 过拟合问题） | ★★★★★ |
| VLN 相关：[52][55][57][59] | 连续环境导航 | 长时程 VLN 平台/基准 [52]、RFT 导航 [55]、连续环境避障 Safe-VLN [57]、NeRF 前瞻探索 [59] | `> 待核实` | B（arXiv 预印本） | 中 | ★★★★ |

**结论与口径警告**：**①** 仿真侧的"能力"（并行度、渲染真实度）与评测侧的"可信度"并不等价：[44] 明确指出现有视觉机器人仿真基准虽推进了操作研究，但**真实世界通用策略的评估显著滞后**。**②** 各基准的成功率口径（任务数、硬件、仿真/真机、初始状态分布）在本次检索中均未获得统一定义，**跨榜单数字不可直接比较**，任何"SOTA"表述都必须附带 benchmark/硬件/任务数三要素。**③** 本章缺失 MuJoCo/Genesis/Habitat/RoboSuite 的一手证据，属检索缺口，`> 待核实`。

---

## 四、经典与奠基性工作

> 表格列中：**热度**（引用/star/下载）——本次检索未提供任何量化字段，**全部 `> 待核实`**；**权威** = 证据等级 + 发表载体；**关注度** 为编辑判断并附依据；**推荐度** ★1–5。带 [n] 者为本次编号来源；标注"种子"者为用户提供的种子资源，**未实时核实**。

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| One-Shot RL for Robot Navigation with Interactive Replay [1] | 2017 | `> 待核实` | `> 待核实` | B（arXiv cs.AI，预印本） | 低（早期工作，无量化信号） | ★★ | http://arxiv.org/abs/1711.10137v2 | 交互式回放缓解真机采样成本，是"数据效率"问题的最早表述之一 |
| Multi-objective Model-based Policy Search for Data-efficient Learning with Sparse Rewards [18] | 2018 | `> 待核实` | `> 待核实` | B（arXiv cs.LG） | 低—中 | ★★ | http://arxiv.org/abs/1806.09351v3 | 模型化策略搜索 + 稀疏奖励，机器人数据高效 RL 的代表 |
| On-Policy Robot Imitation Learning from a Converging Supervisor [19] | 2019 | `> 待核实` | `> 待核实` | B（arXiv cs.LG） | 中（DAgger 系思想的推广） | ★★★ | http://arxiv.org/abs/1907.03423v7 | 把"监督者固定"假设放宽为"监督者随学习演化" |
| Learning Complex Dexterous Manipulation with Deep RL and Demonstrations（DAPG 系）[91] | 2017 | `> 待核实` | `> 待核实` | B（arXiv 预印本） | 高（灵巧操作 RL 奠基性方向） | ★★★★★ | http://arxiv.org/abs/1709.10087v2 | 演示引导 + 深度 RL 做灵巧手操作，奠定"示范+RL"范式 |
| Learning Dexterous In-Hand Manipulation [90] | 2018 | `> 待核实` | `> 待核实` | B（arXiv 预印本，v5 长生命周期） | 高（in-hand 操作基准性工作） | ★★★★★ | http://arxiv.org/abs/1808.00177v5 | 域随机化 + 大规模并行训练的经典范式来源 |
| R3M: A Universal Visual Representation for Robot Manipulation [34] | 2022 | `> 待核实` | `> 待核实` | B（arXiv 预印本） | 高（视觉预训练表示的标准基线） | ★★★★★ | http://arxiv.org/abs/2203.12601v3 | 把大规模人类视频预训练表示迁移到操作，是后来 VLA 视觉骨干的思想前身 |
| Untangling Dense Knots by Learning Task-Relevant Keypoints [32] | 2020 | `> 待核实` | `> 待核实` | B（arXiv 预印本） | 中 | ★★★ | http://arxiv.org/abs/2011.04999v1 | 长时程可变形物体操作的经典任务级抽象 |
| Interactive Imitation Learning in State-Space [29] | 2020 | `> 待核实` | `> 待核实` | B（arXiv 预印本） | 低—中 | ★★★ | http://arxiv.org/abs/2008.00524v2 | 交互式模仿学习的可分析形式化 |
| Learning to Discern: Imitating Heterogeneous Human Demonstrations [28] | 2023 | `> 待核实` | `> 待核实` | B（arXiv 预印本） | 中 | ★★★ | http://arxiv.org/abs/2310.14196v1 | 处理"示范质量不一致"的现实问题 |
| Learning Robot Manipulation from Cross-Morphology Demonstration [36] | 2023 | `> 待核实` | `> 待核实` | B（arXiv 预印本） | 中 | ★★★★ | http://arxiv.org/abs/2304.03833v2 | 跨形态示范迁移，是"跨本体"议题的前身 |
| UniSim: A Neural Closed-Loop Sensor Simulator [12] | 2023 | `> 待核实` | `> 待核实` | B（arXiv 预印本） | 中高 | ★★★★ | http://arxiv.org/abs/2308.01898v1 | 神经闭环传感器仿真，连接世界模型与 Sim2Real |
| Genie: Generative Interactive Environments [14] | 2024 | `> 待核实` | `> 待核实` | B（arXiv 预印本） | 高 | ★★★★★ | http://arxiv.org/abs/2402.15391v1 | 从视频学可控生成环境，世界模型路线分水岭 |
| OpenVLA [63] | 2024 | `> 待核实` | `> 待核实` | B（arXiv 预印本） | 高（开源 VLA 基线） | ★★★★★ | http://arxiv.org/abs/2406.09246v3 | 把 VLA 从闭源演示变成可复现研究对象 |
| ALOHA 2: Enhanced Low-Cost Hardware for Bimanual Teleoperation [30] | 2024 | `> 待核实` | `> 待核实` | B（arXiv 预印本） | 高（低成本双臂数据采集事实标准） | ★★★★★ | http://arxiv.org/abs/2405.02292v1 | 硬件即数据基础设施，直接决定数据分布 |
| SPIRE: Synergistic Planning, Imitation, and RL for Long-Horizon Manipulation [27] | 2024 | `> 待核实` | `> 待核实` | B（arXiv 预印本） | 中 | ★★★★ | http://arxiv.org/abs/2410.18065v1 | 规划/模仿/RL 协同，长时程操作混合方案 |
| BEHAVIOR-1K [51] | 2024 | Stanford（据种子） | `> 待核实` | B（arXiv 预印本；官方站点为种子） | 中高 | ★★★★★ | http://arxiv.org/abs/2403.09227v1 | 1000 项日常活动 + 真实仿真，人本具身基准 |
| PaLM-E: An Embodied Multimodal Language Model（种子） | 2023 | Google（据种子） | `> 待核实` | `> 待核实`（种子资源，未实时核实会议信息） | 高（具身多模态 LLM 奠基） | ★★★★★ | https://arxiv.org/abs/2303.03378 | 具身多模态 LLM 奠基；**未纳入本次编号来源，信息待核实** |
| SayCan: Do As I Can, Not As I Say（种子） | 2022 | Google（据种子） | `> 待核实` | `> 待核实` | 高 | ★★★★★ | https://arxiv.org/abs/2204.01691 | LLM 规划 + 技能可行性 grounding，模块化路线代表 |
| Code as Policies（种子） | 2022 | Google（据种子） | `> 待核实` | `> 待核实` | 高 | ★★★★ | https://arxiv.org/abs/2209.07753 | LLM 生成机器人策略代码，程序化策略先声 |
| Learning to Act without Actions（种子，世界模型线） | 2023 | Various（据种子） | `> 待核实` | `> 待核实` | 中 | ★★★★ | https://arxiv.org/abs/2312.10807 | 世界模型驱动的策略学习；**注意**：与本次编号来源 [12] UniSim（2308.01898）为不同论文，勿混淆，`> 待核实` |

**脉络总结（承上启下）**：
- **2017–2020**：把"真机采样昂贵"作为第一性问题（[1][18][19][29]），同时用域随机化+大规模并行在仿真里攻克灵巧操作（[90][91]）。
- **2020–2023**：转向"表示与任务抽象"——任务相关关键点 [32]、自监督关键点 [39]、通用视觉表示 [34]，并开始处理示范异质性与跨形态 [28][36]。
- **2023–2026**：表示/数据的积累直接催生基础模型路线（[63][100][99]）与世界模型路线（[14][13][10]），两条路线在 [64] 出现交汇，在 [4] 出现分歧。

---

## 五、开源项目与工程实践

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| LeRobot（端到端机器人学习开源库）[60] | 2026 | `> 待核实` | `> 待核实` | B（arXiv 预印本；是否对应官方仓库 **`> 待核实`**） | 中高（低成本遥操作 + 数据集 + 开源库的组合正降低入门门槛） | ★★★★★ | http://arxiv.org/abs/2602.22818v1 | 论文摘要指出：低成本遥操作系统与开源数据/库的可得性正在加速机器人学习；**发表时间与版本需复核** `> 待核实` |
| Isaac Lab [86] | 2025 | `> 待核实` | `> 待核实` | B（arXiv 预印本）+ 种子官方仓库 | 高（GPU 并行训练基础设施） | ★★★★★ | http://arxiv.org/abs/2511.04831v1 ／ https://github.com/isaac-sim/IsaacLab （种子） | GPU 加速多模态机器人学习仿真框架；star/活跃度 **`> 待核实`** |
| Genesis [种子] | `> 待核实` | Genesis-Embodied-AI | `> 待核实` | `> 待核实`（仅种子链接，本次无编号来源） | `> 待核实` | ★★★（建议单独立项核实其物理引擎能力与活跃度） | https://github.com/Genesis-Embodied-AI/Genesis | 生成式物理仿真引擎（据种子说明） |
| BEHAVIOR-1K / OmniGibson [51][种子] | 2024 | Stanford（据种子） | `> 待核实` | B（论文）+ 种子仓库 | 中高 | ★★★★ | https://github.com/StanfordVL/BEHAVIOR-1K | 基准 + 仿真环境一体化 |
| ManiSkill [种子] | `> 待核实` | haosulab | `> 待核实` | `> 待核实`（仅种子链接） | `> 待核实` | ★★★★（GPU 并行操作基准常见选择） | https://github.com/haosulab/ManiSkill | GPU 并行操作基准 |
| OpenVLA [63] | 2024 | `> 待核实` | `> 待核实` | B（arXiv 预印本） | 高 | ★★★★★ | http://arxiv.org/abs/2406.09246v3 | 开源 VLA 权重/代码（具体许可与权重链接 **`> 待核实`**） |
| Running VLAs at Real-time Speed [61] | 2025 | `> 待核实` | `> 待核实` | B（arXiv 预印本） | 高 | ★★★★★ | http://arxiv.org/abs/2510.26742v1 | 推理侧工程优化（多视角 VLA 实时化），是否开源 **`> 待核实`** |
| Robot Learning: A Tutorial [37] | 2025 | `> 待核实` | `> 待核实` | B（arXiv 预印本，教程性质） | 中 | ★★★★ | http://arxiv.org/abs/2510.12403v1 | 从模型化方法转向数据驱动范式的系统性教程，适合作为工程选型起点 |
| 人形/全身控制工程线：[67][68][69][93][66][71] | 2018–2026 | `> 待核实` | `> 待核实` | B（arXiv 预印本） | 中 | ★★★ | 见 [66][67][68][69][71][93] | 遥操作接口（[67][68]）、ROS 系软件框架（[66][71]，2018 年）、分层移动-操作（[93]） |
| 灵巧操作线：[89][90][91][92] | 2017–2025 | `> 待核实` | `> 待核实` | B（arXiv 预印本） | 中 | ★★★★ | 见对应链接 | 绳缆操作分类学 [89]、in-hand [90]、DAPG [91]、空中移动操作 [92] |

**工程实践要点**：
1. **ROS2 集成在本次检索中缺乏一手证据**——仅有 2018 年的 NimbRo-OP ROS 软件框架 [66][71]，**不能代表 ROS2 现状**，标注 `> 待核实`。
2. **实时性是绕不过的工程门槛**：[61] 把"大 VLA 无法做动态实时任务"作为问题陈述，说明"能跑分"与"能闭环动态执行"之间存在工程鸿沟。
3. **数据基础设施优先于模型**：[30]（低成本双臂遥操作）、[60]（低成本遥操作 + 开源库）表明社区把重心放在"降低采集与复现成本"，这与 [16] 指出"真机 RL 罕见"互为因果。
4. **复现困难**：本报告所引开源条目均**未能核实权重/许可证/最近提交时间**（热度与活跃度字段全部缺失），因此无法给出"开箱可用"的判断，一律 `> 待核实`。

---

## 六、数据集与评测协议

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| DROID（大规模 in-the-wild 真机操作数据集）[40] | 2024 | `> 待核实` | `> 待核实`（论文未提供下载量数据） | B（arXiv 预印本） | 高（真机多样性数据的主要来源之一） | ★★★★★ | http://arxiv.org/abs/2403.12945v2 | 大规模真实场景操作数据，用于通用策略训练与评测 |
| Open X-Embodiment（种子） | 2023 | `> 待核实` | `> 待核实`（**无 star/下载量数据，禁编造**） | `> 待核实`（种子资源，未实时核实） | 高（跨本体数据的事实标准） | ★★★★★ | https://robotics-transformer-x.github.io/ | 跨本体真机数据集合；规模与版本 **`> 待核实`** |
| AgiBot World（种子） | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | ★★★ | https://agibot-world.com/ | 大规模真机具身数据集（据种子说明）；**未实时核实，`> 待核实`** |
| BEHAVIOR-1K [51] | 2024 | Stanford（据种子） | `> 待核实` | B（arXiv 预印本） | 中高 | ★★★★★ | http://arxiv.org/abs/2403.09227v1 ／ https://behavior.stanford.edu/ | 1000 项日常活动 + 真实仿真，人本评测 |
| LIBERO-Para [41] | 2026 | `> 待核实` | `> 待核实` | B（arXiv cs.LG，预印本） | 中高（诊断式基准兴起） | ★★★★★ | http://arxiv.org/abs/2603.28301v3 | 揭示 VLA 在小数据微调下**过拟合特定指令表述**；提供改写鲁棒性指标与诊断基准 |
| LIBERO-VPro [42] | 2026 | `> 待核实` | `> 待核实` | B（arXiv cs.RO，预印本） | 中高 | ★★★★★ | http://arxiv.org/abs/2609.24350v1 | 指出常规评测假设"干净、及时、一致的视觉观测"，专测闭环视觉鲁棒性 |
| RoboDojo [49] | 2026 | `> 待核实` | `> 待核实` | B（arXiv 预印本） | 中高 | ★★★★★ | http://arxiv.org/abs/2607.04434v3 | 统一 sim-and-real 的通用操作策略评测 |
| Embodied Arena [46] | 2025 | `> 待核实` | `> 待核实` | B（arXiv 预印本） | 中高 | ★★★★ | http://arxiv.org/abs/2509.15273v2 | 统一、可演进的具身评测平台 |
| EmbodiedCity [50] | 2024 | `> 待核实` | `> 待核实` | B（arXiv 预印本） | 中 | ★★★ | http://arxiv.org/abs/2410.09604v1 | 真实城市环境具身智能体平台 |
| 长时程 VLN 平台 [52] / VLN-R1 [55] / Safe-VLN [57] / NeRF 前瞻探索 [59] / Know-Where [54] | 2021–2025 | `> 待核实` | `> 待核实` | B（arXiv 预印本） | 中 | ★★★★ | 见对应链接 | 导航类评测：连续性 [57][59]、长时程 [52]、RFT 训练 [55]、结构化空间先验 [54] |
| 2025 BEHAVIOR Challenge 任务适配方案 [108] | 2025 | `> 待核实` | `> 待核实` | B（arXiv 预印本） | 中（竞赛第一名方案具参考价值） | ★★★★ | http://arxiv.org/abs/2512.06951v2 | VLA 任务适配的竞赛级工程实践 |
| 扩展律研究：Towards Embodiment Scaling Laws in Robot Locomotion [47] | 2025 | `> 待核实` | `> 待核实` | B（arXiv 预印本，仅题名级证据） | 中（"跨本体扩展律"是重要未决问题） | ★★★★ | http://arxiv.org/abs/2505.05753v2 | 探索本体数量与性能的扩展关系；**结论细节未读取，`> 待核实`** |

**评测协议的关键结论**：
1. **"口径不可比"是本领域最主要的方法论障碍**：[44] 明确指出真实世界通用策略的评估滞后于仿真基准；[41] 与 [42] 分别指出常规评测在"指令改写"与"视觉扰动闭环"两个维度上系统性高估模型能力。因此，看到"SOTA"须追问：**哪个 benchmark、多少任务、什么硬件、仿真还是真机、是否闭环扰动**。
2. **诊断型基准正在取代"刷分型基准"**：[41][42] 的出版时间（2026）晚于多数 VLA 基线（2024–2025），反映社区从"比高低"转向"找失效模式"。
3. **第三方独立评测**：本次检索中 [46][49] 属于面向统一评测的平台型工作，但其**是否已形成排行榜/第三方复现记录，`> 待核实`**。

---

## 七、Sim2Real 与开放问题

### 7.

## 八、建议关注清单（Watchlist）

> 筛选原则：优先纳入（a）在本次检索中被多个子问题交叉召回、（b）提供代码/权重/基准可复现路径、（c）直接对应本报告争议点（统一动作空间、世界模型、Sim2Real、评测口径不可比）的条目。
> 证据口径说明：本次检索的结构化发现块**未附带 `citations=` / `stars=` / 下载量字段**，因此凡无第三方榜单或官方数字支撑的热度证据一律标注 `> 待核实`，不做数字推测；arXiv 编号与发表年份以来源列表为准。

---

### 8.1 模型与范式线

**W1｜跨本体 / 人形基础模型：GR00T N1 与 MiMo-Embodied**
- **关注理由**：代表"统一动作空间 + 跨本体预训练"路线，是判断 VLA 是否从"单本体调参"走向"跨本体迁移"的关键观测点。
- **热度证据**：`> 待核实`（本报告检索未获取 citations/stars 字段）；MiMo-Embodied 论文自述"在 17 个具身 AI 基准上刷新纪录" [99]（**自述，非第三方复现**）。
- **权威证据**：[100] GR00T N1 技术报告（arXiv, cs.RO）[100]；[99] MiMo-Embodied 技术报告（arXiv, cs.RO）[99]。
- **关注度**：中 — 依据：两条均被 q1 子问题作为前沿候选召回 [99][100]；第三方引用/榜单排名 `> 待核实`。
- **推荐度**：★★★★☆ — 值得读，但"17 基准纪录"属论文自述，需等独立评测或榜单复核后再采信 [99]。

**W2｜开源 VLA 与实时推理可行性**
- **关注理由**：VLA 落地的真正瓶颈常是推理频率而非精度；"能否在消费级 GPU 上跑到实时"决定其能否用于动态任务。
- **热度证据**：`> 待核实`（检索块未提供 citations/stars）[61][63]。
- **权威证据**：[63] OpenVLA（arXiv 预印本，开源 VLA 代表）[63]；[61] Running VLAs at Real-time Speed（arXiv, cs.RO）[61]；[107] VLA-Adapter 提出 tiny-scale VLA 范式（arXiv 预印本）[107]。
- **关注度**：高 — 依据："实时/轻量 VLA"在本次检索中被 q1、q6 两个子问题独立召回 [61][107]，属结构性工程痛点。
- **推荐度**：★★★★★ — 对 C++/ROS2 工程侧读者相关性最高，建议优先精读 [61][63][107]。

**W3｜VLA 的"思考式推理"与运动预测耦合**
- **关注理由**：直击"模仿专家轨迹、缺乏预测性运动推理"这一被指出的核心缺陷 [64]。
- **热度证据**：`> 待核实` [64][105]。
- **权威证据**：[64] Robotic VLA Benefits from Joint Learning with Motion Image Diffusion（arXiv, cs.RO）[64]；[105] VLA-Thinker（arXiv 预印本）[105]。
- **关注度**：中 — 依据：q6 子问题召回 [64]；[105] 仅出现在证据池，未在结构化发现中被展开 `> 待核实`。
- **推荐度**：★★★☆☆ — 方向重要，但目前仅见预印本层面证据，复现性待观察 [64][105]。

---

### 8.2 世界模型线

**W4｜视频生成式世界模型用于操作：Genie Envisioner**
- **关注理由**：把策略学习、评测、仿真压进单一视频生成框架，是"世界模型 vs 模仿学习"分歧的最直接实验载体 [10]。
- **热度证据**：`> 待核实`（无 citations/stars 字段）[10]。
- **权威证据**：[10] Genie Envisioner: A Unified World Foundation Platform for Robotic Manipulation（arXiv, cs.RO）[10]。
- **关注度**：高 — 依据：被 q3 子问题作为世界模型路线核心候选召回 [10]，且与本报告"世界模型/仿真/评测一体化"争议直接对应。
- **推荐度**：★★★★☆ — 若其生成式仿真能替代部分真实评测，将改变 Sim2Real 工作流，值得跟踪 [10]。

**W5｜几何一致性：GEM-4D 与 DINO-WM**
- **关注理由**：世界模型的已知软肋是"画面合理但物理点不守恒"，导致动作执行不可靠；几何增强与预训练特征世界模型是两条直接应对路径 [4][13]。
- **热度证据**：`> 待核实` [4][13]。
- **权威证据**：[4] GEM-4D（arXiv, cs.CV）[4]；[13] DINO-WM（arXiv 预印本，零样本规划）[13]。
- **关注度**：中 — 依据：q3 子问题召回 [4]；[13] 属世界模型经典路线代表，出现在证据池 [13]。
- **推荐度**：★★★★☆ — 是评估"世界模型是否真能用于规划"的判别性指标来源 [4][13]。

**W6｜世界模型的元争议：Sora 是否算世界模拟器**
- **关注理由**：为"世界模型"一词的滥用提供校准标尺，避免把视频生成质量误读为物理理解 [9][17]。
- **热度证据**：`> 待核实` [9][17]。
- **权威证据**：[9] Is Sora a World Simulator? 综述（arXiv）[9]；[17] Sora as a World Model? 文本到视频生成综述（arXiv）[17]。
- **关注度**：中 — 依据：两篇独立综述同期出现，说明该争论在检索窗口内仍活跃 [9][17]。
- **推荐度**：★★★☆☆ — 作为方法论校准读物，而非技术方案 [9][17]。

---

### 8.3 仿真平台与基准线

**W7｜GPU 并行仿真：Isaac Lab**
- **关注理由**：多模态机器人学习的规模化训练底座，直接决定 RL/Sim2Real 实验吞吐 [86]。
- **热度证据**：`> 待核实`（检索块无 star 字段；GitHub 仓库 `isaac-sim/IsaacLab` 为领域种子资源，**未实时检索**）。
- **权威证据**：[86] Isaac Lab: A GPU-Accelerated Simulation Framework for Multi-Modal Robot Learning（arXiv 预印本）[86]；官方仓库 https://github.com/isaac-sim/IsaacLab （领域种子资源）。
- **关注度**：高 — 依据：被 q4 仿真平台对比子问题直接点名，且为报告种子工程栈之一 [86]。
- **推荐度**：★★★★★ — 工程选型优先项，但版本/API 变动快，需以官方文档为准 [86]。

**W8｜VLA 鲁棒性诊断基准：LIBERO-Para 与 LIBERO-VPro**
- **关注理由**：标准 LIBERO 高分可能来自对固定指令表述与干净视觉的过拟合；这两条把"改写鲁棒性"与"闭环视觉鲁棒性"拆成可测指标 [41][42]。
- **热度证据**：`> 待核实` [41][42]。
- **权威证据**：[41] LIBERO-Para（arXiv, cs.LG）[41]；[42] LIBERO-VPro（arXiv, cs.RO）[42]。
- **关注度**：高 — 依据：q5 子问题将二者作为"口径不可比"证据召回 [41][42]。
- **推荐度**：★★★★★ — 若你要复现或对比 VLA，这两项是判断"分数是否虚高"的低成本前置检查 [41][42]。

**W9｜统一 sim-and-real 与聚合评测：RoboDojo、Embodied Arena、RoboPolicy 评测视角**
- **关注理由**：当前最大结构性问题是"仿真 SOTA 与真机 SOTA 不可比"；统一 sim-and-real 基准与聚合排行榜是解法候选 [44][46][49]。
- **热度证据**：`> 待核实`（无榜单排名数据）[44][46][49]。
- **权威证据**：[49] RoboDojo: A Unified Sim-and-Real Benchmark（arXiv）[49]；[46] Embodied Arena 评测平台（arXiv）[46]；[44] Robot Policy Evaluation for Sim-to-Real Transfer: A Benchmarking Perspective（arXiv, cs.RO）[44]。
- **关注度**：高 — 依据：q4、q5 两个子问题交叉召回 [44][49]，[46] 为独立评测平台类候选。
- **推荐度**：★★★★☆ — 做选型对比时的首选评测入口，但其自身第三方公信力 `> 待核实` [44][46][49]。

**W10｜长程任务基准与挑战赛：BEHAVIOR-1K / BEHAVIOR Challenge**
- **关注理由**：长程日常活动（1000 项）是检验规划—执行耦合与失败恢复的少数公开口径 [51][108]。
- **热度证据**：`> 待核实`（榜单成绩未在本次检索中获取）。
- **权威证据**：[51] BEHAVIOR-1K 论文（arXiv）[51]；[108] 2025 BEHAVIOR Challenge 第一名方案（任务适配 VLA，arXiv）[108]；官方仓库 https://github.com/StanfordVL/BEHAVIOR-1K （领域种子资源）。
- **关注度**：中 — 依据：q5 基准子问题提及，[108] 提供可对照的挑战赛解决方案 [108]。
- **推荐度**：★★★★☆ — 适合评估长程能力；注意仿真与真机口径差异 [51][108]。

---

### 8.4 Sim2Real 线

**W11｜Sim2Real 的"可测性"与"视觉/深度域对齐"**
- **关注理由**：Sim2Real 争论常停留在经验层面；需要可量化的评测视角与针对性的域差补偿手段 [44][82][83]。
- **热度证据**：`> 待核实` [82][83]。
- **权威证据**：[44] Sim-to-Real 评测基准视角（arXiv, cs.RO）[44]；[82] 视觉编码器预训练用于视运动策略迁移（arXiv）[82]；[83] RealD²iff 深度扩散（arXiv, cs.RO）[83]。
- **关注度**：中 — 依据：q4 子问题召回 [44][83]；[82] 为策略迁移路线代表 [82]。
- **推荐度**：★★★★☆ — 为"域差出在视觉还是动力学"提供可操作分解 [82][83]。

**W12｜负面结果与能力边界：Sim2Real 的受限场景**
- **关注理由**：正面案例偏多，而精度敏感任务（如精细农业）与仿真器不建模的物理效应往往是失败集中区 [80]。
- **热度证据**：`> 待核实` [80]。
- **权威证据**：[80] The Importance and the Limitations of Sim2Real for Robotic Manipulation in Precision Agriculture（arXiv）[80]；[78] R:SS 2020 Sim2Real Workshop 总结（arXiv）[78]。
- **关注度**：低—中 — 依据：仅在证据池出现，本轮结构化发现未展开 `> 待核实` [78][80]。
- **推荐度**：★★★☆☆ — 写作/立项时用于校正"Sim2Real 已解决"的过度乐观 [78][80]。

**W13｜低成本快速对齐：人形 Locomotion 的 15 分钟级 Sim2Real**
- **关注理由**：若"15 分钟完成 Sim2Real"成立，将显著降低人形运动的实验门槛，是强可复现性承诺 [72]。
- **热度证据**：`> 待核实` [72]。
- **权威证据**：[72] Learning Sim-to-Real Humanoid Locomotion in 15 Minutes（arXiv 预印本）[72]；对照 [16] Robot Trains Robot 的仿真预训练 + 真机自适应路线 [16]。
- **关注度**：中 — 依据：q2、q3 子问题均召回 [16]，[72] 为同方向更激进的效率主张 [16][72]。
- **推荐度**：★★★★☆ — 复现成本低，适合作为入门验证；"15 分钟"的具体口径（任务/硬件/成功率）需以全文核实 `> 待核实` [72]。

---

### 8.5 工程栈与开源生态

**W14｜端到端机器人学习库：LeRobot**
- **关注理由**：把遥操作硬件、数据格式与策略训练打通的端到端开源栈，直接影响具身项目的上手成本 [60]。
- **热度证据**：`> 待核实`（无 star/下载量字段）[60]。
- **权威证据**：[60] LeRobot: An Open-Source Library for End-to-End Robot Learning（arXiv, cs.RO）[60]。
- **关注度**：高 — 依据：q6 子问题将其作为开源工程实践核心候选召回 [60]。
- **推荐度**：★★★★★ — 与 ROS2 集成的实践首选入口之一；实际维护活跃度需现场核验 `> 待核实` [60]。

**W15｜开源机器人的"负面结果"风险：复现困难与维护衰减**
- **关注理由**：开源仓库的 star 不等于可复现；RL 策略的随机性、硬件差异与依赖漂移是常见失败源 [62]。
- **热度证据**：`> 待核实` [62]。
- **权威证据**：[62] Open Source Software Development Challenges: A Systematic Literature Review on GitHub（arXiv 综述）[62]。
- **关注度**：低 — 依据：非具身专用，属方法论迁移来源 `> 待核实` [62]。
- **推荐度**：★★☆☆☆ — 仅在需要论证"开源≠可复现"时引用 [62]。

---

### 8.6 人形与全身控制

**W16｜人形全身操作与遥操作**
- **关注理由**：全身 loco-manipulation 的数据获取仍依赖遥操作，接口设计与演示效率是关键瓶颈 [67][68][70]。
- **热度证据**：`> 待核实` [67][68][70]。
- **权威证据**：[67] CHILD 全身人形遥操作（arXiv）[67]；[68] Humanoid Manipulation Interface（arXiv）[68]；[70] 微型人形 Tele-Loco-Manipulation（arXiv）[70]；[65] 羽毛球全身控制 RL 课程（arXiv）[65]。
- **关注度**：中 — 依据：q6 子问题召回人形全身控制条目 [65][67][68]。
- **推荐度**：★★★★☆ — 若做真机演示采集，[67][68] 的接口设计值得对标 [67][68]。

---

### 8.7 安全、可信与治理

**W17｜具身安全与认证**
- **关注理由**：从"能力"转向"可信部署"的必经环节，含风险/攻击/防御分类与认证测量机制 [94][75]。
- **热度证据**：`> 待核实` [75][94]。
- **权威证据**：[94] Safety in Embodied AI: A Survey of Risks, Attacks, and Defenses（arXiv, cs.CR）[94]；[75] Toward Maturity-Based Certification of Embodied AI（arXiv）[75]。
- **关注度**：中 — 依据：q1 子问题召回 [94]，属新出现的独立议题 [94][75]。
- **推荐度**：★★★☆☆ — 目前多为综述/框架层证据，落地标准 `> 待核实` [75][94]。

---

### 8.8 检索噪声与复核提示（重要）

- 本次结构化发现中混入多条与具身智能**主题无关**的条目（如短视频热度预测、基础模型透明度指数、图像超分挑战、越南语法律问答、新闻主观性检测等）[2][3][21][22][43][85]。这些条目被召回的机制更可能是标题/类别相近而非主题相关，**不应作为具身智能领域结论的证据**，建议在后续轮次中从候选池剔除 [2][3][21][22]。
- 部分条目的年份为 2026 年（如 [4][41][42][79][94][95]），属检索窗口内最新预印本，尚未见同行评审与第三方复现，引用时应统一加"(preprint)"限定并标注 confidence 偏低 [4][41][42][79]。
- 全部条目的 citations / GitHub star / 榜单排名在本轮**均未获取**，因此本报告所有"热度证据"均为 `> 待核实`；如需支撑汇报中的影响力判断，建议下一轮直接查询 arXiv/OpenAlex API 与 GitHub API 补全 [63][86]。

---

### 8.9 建议的 90 天跟踪节奏

| 周期 | 动作 | 目标信号 |
|---|---|---|
| 每 2 周 | 复查 [10][13][100] 的代码/权重放出状态与官方更新 | 是否可复现、是否放出权重 [10][13][100] |
| 每月 | 抓取 [49][46] 榜单快照并记录评测口径（仿真/真机、任务数、本体） | 判断"仿真 SOTA vs 真机 SOTA"是否开始收敛 [46][49] |
| 每月 | 用 [41][42] 对你的候选 VLA 做一次鲁棒性前置体检 | 暴露指令改写/视觉扰动下的性能跌落 [41][42] |
| 每季度 | 复核 [94][75] 是否有标准化/认证进展 | 安全与可信是否出现可执行规范 [75][94] |

> 说明：以上"目标信号"均为待验证假设，当前检索尚未提供对应的定量证据，落地前需逐项核实。

## 参考来源

[1] One-Shot Reinforcement Learning for Robot Navigation with Interactive Replay — http://arxiv.org/abs/1711.10137v2
[2] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1
[3] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1
[4] GEM-4D: Geometry-Enhanced Video World Models for Robot Manipulation — http://arxiv.org/abs/2605.22882v4
[5] Quantum decision making by social agents — http://arxiv.org/abs/1202.4918v2
[6] Causality-enhanced Decision-Making for Autonomous Mobile Robots in Dynamic Environments — http://arxiv.org/abs/2504.11901v5
[7] Modeling and Interpreting Real-world Human Risk Decision Making with Inverse Reinforcement Learning — http://arxiv.org/abs/1906.05803v1
[8] Generative Models in Decision Making: A Survey — http://arxiv.org/abs/2502.17100v4
[9] Is Sora a World Simulator? A Comprehensive Survey on General World Models and Beyond — http://arxiv.org/abs/2405.03520v2
[10] Genie Envisioner: A Unified World Foundation Platform for Robotic Manipulation — http://arxiv.org/abs/2508.05635v3
[11] Neutrino-Nucleon Cross-Section Model Tuning in GENIE v3 — http://arxiv.org/abs/2104.09179v2
[12] UniSim: A Neural Closed-Loop Sensor Simulator — http://arxiv.org/abs/2308.01898v1
[13] DINO-WM: World Models on Pre-trained Visual Features enable Zero-shot Planning — http://arxiv.org/abs/2411.04983v2
[14] Genie: Generative Interactive Environments — http://arxiv.org/abs/2402.15391v1
[15] GeNIe: Generative Hard Negative Images Through Diffusion — http://arxiv.org/abs/2312.02548v3
[16] Robot Trains Robot: Automatic Real-World Policy Adaptation and Learning for Humanoids — http://arxiv.org/abs/2508.12252v2
[17] Sora as a World Model? A Complete Survey on Text-to-Video Generation — http://arxiv.org/abs/2403.05131v3
[18] Multi-objective Model-based Policy Search for Data-efficient Learning with Sparse Rewards — http://arxiv.org/abs/1806.09351v3
[19] On-Policy Robot Imitation Learning from a Converging Supervisor — http://arxiv.org/abs/1907.03423v7
[20] The Sound of Simulation: Learning Multimodal Sim-to-Real Robot Policies with Generative Audio — http://arxiv.org/abs/2507.02864v2
[21] NTIRE 2025 Challenge on Image Super-Resolution (x4): Methods and Results — http://arxiv.org/abs/2504.14582v3
[22] VLSP 2025 MLQA-TSR Challenge: Vietnamese Multimodal Legal Question Answering on Traffic Sign Regulation — http://arxiv.org/abs/2510.20381v1
[23] The AudioMOS Challenge 2025 — http://arxiv.org/abs/2509.01336v1
[24] TDCOSMO 2025: Cosmological constraints from strong lensing time delays — http://arxiv.org/abs/2506.03023v4
[25] Emotion in Reinforcement Learning Agents and Robots: A Survey — http://arxiv.org/abs/1705.05172v1
[26] Active learning for data streams: a survey — http://arxiv.org/abs/2302.08893v4
[27] SPIRE: Synergistic Planning, Imitation, and Reinforcement Learning for Long-Horizon Manipulation — http://arxiv.org/abs/2410.18065v1
[28] Learning to Discern: Imitating Heterogeneous Human Demonstrations with Preference and Representation Learning — http://arxiv.org/abs/2310.14196v1
[29] Interactive Imitation Learning in State-Space — http://arxiv.org/abs/2008.00524v2
[30] ALOHA 2: An Enhanced Low-Cost Hardware for Bimanual Teleoperation — http://arxiv.org/abs/2405.02292v1
[31] KDPE: A Kernel Density Estimation Strategy for Diffusion Policy Trajectory Selection — http://arxiv.org/abs/2508.10511v2
[32] Untangling Dense Knots by Learning Task-Relevant Keypoints — http://arxiv.org/abs/2011.04999v1
[33] RT-Bench: an Extensible Benchmark Framework for the Analysis and Management of Real-Time Applications — http://arxiv.org/abs/2203.11423v2
[34] R3M: A Universal Visual Representation for Robot Manipulation — http://arxiv.org/abs/2203.12601v3
[35] Learning Cross-Lingual Sentence Representations via a Multi-task Dual-Encoder Model — http://arxiv.org/abs/1810.12836v4
[36] Learning Robot Manipulation from Cross-Morphology Demonstration — http://arxiv.org/abs/2304.03833v2
[37] Robot Learning: A Tutorial — http://arxiv.org/abs/2510.12403v1
[38] ManiWAV: Learning Robot Manipulation from In-the-Wild Audio-Visual Data — http://arxiv.org/abs/2406.19464v2
[39] Self-Supervised Learning of Multi-Object Keypoints for Robotic Manipulation — http://arxiv.org/abs/2205.08316v2
[40] DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset — http://arxiv.org/abs/2403.12945v2
[41] LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models — http://arxiv.org/abs/2603.28301v3
[42] LIBERO-VPro: Benchmarking Closed-Loop Visual Robustness of Robotic Foundation Models — http://arxiv.org/abs/2609.24350v1
[43] VQualA 2025 Challenge on Visual Quality Comparison for Large Multimodal Models: Methods and Results — http://arxiv.org/abs/2509.09190v1
[44] Robot Policy Evaluation for Sim-to-Real Transfer: A Benchmarking Perspective — http://arxiv.org/abs/2508.11117v1
[45] Aligning Cyber Space with Physical World: A Comprehensive Survey on Embodied AI — http://arxiv.org/abs/2407.06886v8
[46] Embodied Arena: A Comprehensive, Unified, and Evolving Evaluation Platform for Embodied AI — http://arxiv.org/abs/2509.15273v2
[47] Towards Embodiment Scaling Laws in Robot Locomotion — http://arxiv.org/abs/2505.05753v2
[48] Grasp and Motion Planning for Dexterous Manipulation for the Real Robot Challenge — http://arxiv.org/abs/2101.02842v1
[49] RoboDojo: A Unified Sim-and-Real Benchmark for Comprehensive Evaluation of Generalist Robot Manipulation Policies — http://arxiv.org/abs/2607.04434v3
[50] EmbodiedCity: A Benchmark Platform for Embodied Agent in Real-world City Environment — http://arxiv.org/abs/2410.09604v1
[51] BEHAVIOR-1K: A Human-Centered, Embodied AI Benchmark with 1,000 Everyday Activities and Realistic Simulation — http://arxiv.org/abs/2403.09227v1
[52] Towards Long-Horizon Vision-Language Navigation: Platform, Benchmark and Method — http://arxiv.org/abs/2412.09082v3
[53] LVLM-eHub: A Comprehensive Evaluation Benchmark for Large Vision-Language Models — http://arxiv.org/abs/2306.09265v1
[54] The Road to Know-Where: An Object-and-Room Informed Sequential BERT for Indoor Vision-Language Navigation — http://arxiv.org/abs/2104.04167v2
[55] VLN-R1: Vision-Language Navigation via Reinforcement Fine-Tuning — http://arxiv.org/abs/2506.17221v2
[56] Vision-Language Model for Object Detection and Segmentation: A Review and Evaluation — http://arxiv.org/abs/2504.09480v1
[57] Safe-VLN: Collision Avoidance for Vision-and-Language Navigation of Autonomous Robots Operating in Continuous Environments — http://arxiv.org/abs/2311.02817v2
[58] TinyGiantVLM: A Lightweight Vision-Language Architecture for Spatial Reasoning under Resource Constraints — http://arxiv.org/abs/2508.17595v1
[59] Lookahead Exploration with Neural Radiance Representation for Continuous Vision-Language Navigation — http://arxiv.org/abs/2404.01943v1
[60] LeRobot: An Open-Source Library for End-to-End Robot Learning — http://arxiv.org/abs/2602.22818v1
[61] Running VLAs at Real-time Speed — http://arxiv.org/abs/2510.26742v1
[62] Open Source Software Development Challenges: A Systematic Literature Review on GitHub — http://arxiv.org/abs/2003.10750v3
[63] OpenVLA: An Open-Source Vision-Language-Action Model — http://arxiv.org/abs/2406.09246v3
[64] Robotic VLA Benefits from Joint Learning with Motion Image Diffusion — http://arxiv.org/abs/2512.18007v1
[65] Humanoid Whole-Body Badminton via an Annealed Reinforcement Learning Curriculum — http://arxiv.org/abs/2511.11218v4
[66] A ROS-based Software Framework for the NimbRo-OP Humanoid Open Platform — http://arxiv.org/abs/1809.11051v1
[67] CHILD (Controller for Humanoid Imitation and Live Demonstration): a Whole-Body Humanoid Teleoperation System — http://arxiv.org/abs/2508.00162v2
[68] Humanoid Manipulation Interface: Humanoid Whole-Body Manipulation from Robot-Free Demonstrations — http://arxiv.org/abs/2602.06643v2
[69] Learning Humanoid Standing-up Control across Diverse Postures — http://arxiv.org/abs/2502.08378v2
[70] Towards Miniature Humanoid Tele-Loco-Manipulation Using Virtual Reality and Reinforcement Learning — http://arxiv.org/abs/2607.20399v1
[71] NimbRo-OP2: Grown-up 3D Printed Open Humanoid Platform for Research — http://arxiv.org/abs/1809.11144v1
[72] Learning Sim-to-Real Humanoid Locomotion in 15 Minutes — http://arxiv.org/abs/2512.01996v1
[73] PANORAMA: The Rise of Omnidirectional Vision in the Embodied AI Era — http://arxiv.org/abs/2509.12989v1
[74] Multi-Step Guided Diffusion for Image Restoration on Edge Devices: Toward Lightweight Perception in Embodied AI — http://arxiv.org/abs/2506.07286v1
[75] Toward Maturity-Based Certification of Embodied AI: Quantifying Trustworthiness Through Measurement Mechanisms — http://arxiv.org/abs/2601.03470v2
[76] Faith in AI can narrow the futures individuals consider — http://arxiv.org/abs/2603.28944v2
[77] Embodied AI-Enhanced IoMT Edge Computing: UAV Trajectory Optimization and Task Offloading with Mobility Prediction — http://arxiv.org/abs/2512.20902v1
[78] Perspectives on Sim2Real Transfer for Robotics: A Summary of the R:SS 2020 Workshop — http://arxiv.org/abs/2012.03806v1
[79] Robot Manipulation with GPT-6-Astra: Body Knowledge, Experience Reuse, Emergent Skills, and Sim2Real Transfer — http://arxiv.org/abs/2609.31770v1
[80] The Importance and the Limitations of Sim2Real for Robotic Manipulation in Precision Agriculture — http://arxiv.org/abs/2008.03983v1
[81] Sim2Real Transfer for Audio-Visual Navigation with Frequency-Adaptive Acoustic Field Prediction — http://arxiv.org/abs/2405.02821v2
[82] Bridging the Sim2Real Gap: Vision Encoder Pre-Training for Visuomotor Policy Transfer — http://arxiv.org/abs/2501.16389v2
[83] RealD$^2$iff: Bridging Real-World Gap in Robot Manipulation via Depth Diffusion — http://arxiv.org/abs/2511.22505v2
[84] The Synthesis of Optimal Control Laws Using Isaacs' Method for the Solution of Differential Games — http://arxiv.org/abs/2112.10849v2
[85] AI Wizards at CheckThat! 2025: Enhancing Transformer-Based Embeddings with Sentiment for Subjectivity Detection in News Articles — http://arxiv.org/abs/2507.11764v1
[86] Isaac Lab: A GPU-Accelerated Simulation Framework for Multi-Modal Robot Learning — http://arxiv.org/abs/2511.04831v1
[87] ClaimIQ at CheckThat! 2025: Comparing Prompted and Fine-Tuned Language Models for Verifying Numerical Claims — http://arxiv.org/abs/2509.11492v1
[88] LongEval at CLEF 2025: Longitudinal Evaluation of IR Model Performance — http://arxiv.org/abs/2503.08541v1
[89] Dexterous Cable Manipulation: Taxonomy, Multi-Fingered Hand Design, and Long-Horizon Manipulation — http://arxiv.org/abs/2502.00396v2
[90] Learning Dexterous In-Hand Manipulation — http://arxiv.org/abs/1808.00177v5
[91] Learning Complex Dexterous Manipulation with Deep Reinforcement Learning and Demonstrations — http://arxiv.org/abs/1709.10087v2
[92] Aerial Mobile Manipulator System to Enable Dexterous Manipulations with Increased Precision — http://arxiv.org/abs/2010.09618v1
[93] HANDO: Hierarchical Autonomous Navigation and Dexterous Omni-loco-manipulation — http://arxiv.org/abs/2510.09221v1
[94] Safety in Embodied AI: A Survey of Risks, Attacks, and Defenses — http://arxiv.org/abs/2605.02900v2
[95] Inference-Time Attention Steering for Vision-Language-Action Driving Models — http://arxiv.org/abs/2608.17095v1
[96] Survey of Vision-Language-Action Models for Embodied Manipulation — http://arxiv.org/abs/2508.15201v2
[97] A Survey on Vision-Language-Action Models for Embodied AI — http://arxiv.org/abs/2405.14093v8
[98] Foundations of GenIR — http://arxiv.org/abs/2501.02842v1
[99] MiMo-Embodied: X-Embodied Foundation Model Technical Report — http://arxiv.org/abs/2511.16518v2
[100] GR00T N1: An Open Foundation Model for Generalist Humanoid Robots — http://arxiv.org/abs/2503.14734v2
[101] JENGA: Exploiting Counter-Based RowHammer Countermeasures to Break Real-Time Predictability — http://arxiv.org/abs/2609.01077v1
[102] LLM-based ambiguity detection in natural language instructions for collaborative surgical robots — http://arxiv.org/abs/2507.11525v1
[103] Technical Report for Ego4D Long-Term Action Anticipation Challenge 2025 — http://arxiv.org/abs/2506.02550v2
[104] Diffusion and Flow Matching Models for Tabular Data: A Survey — http://arxiv.org/abs/2502.17119v2
[105] VLA-Thinker: Boosting Vision-Language-Action Models through Thinking-with-Image Reasoning — http://arxiv.org/abs/2603.14523v1
[106] Divergence-Free Diffusion Models for Incompressible Fluid Flows — http://arxiv.org/abs/2601.19368v1
[107] VLA-Adapter: An Effective Paradigm for Tiny-Scale Vision-Language-Action Model — http://arxiv.org/abs/2509.09372v2
[108] Task adaptation of Vision-Language-Action model: 1st Place Solution for the 2025 BEHAVIOR Challenge — http://arxiv.org/abs/2512.06951v2


---

*Generated by research-bot · topic=`embodied-ai` · depth=`standard` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading · model=`deepseek-v4-flash` · sources=108 · duration=345s · 2026-10-05T22:24:38+00:00*
