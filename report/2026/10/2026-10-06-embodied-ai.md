# 具身智能（Embodied AI）调研报告：从经典机器人学习到 VLA / 世界模型基础模型

**元信息**
- 日期（UTC）：2026-10-06
- 领域：具身智能（Embodied AI）/ 机器人学习 / VLA / 世界模型 / Sim2Real
- 检索源：本次可引用编号来源共 **121** 条（[1]–[121]）；经主题相关性筛查，直接可用者约 40 余条，其余为检索噪声（短视频流行度预测、蛋白质设计、图像超分、越南语法律问答等），已在正文中标注并剔除
- 证据纪律：一手论文标注 arXiv 编号与年份；无同行评审记录者标为预印本；无法核实的热度/榜单数字一律写 `> 待核实`，本报告不编造引用数与 star 数

---

## 摘要（Executive Summary）

1. **范式重心已从"单任务策略"迁移到"基础模型 + 数据规模化"。** 2024–2026 年的主导路线是把 VLM 主干接到动作头上（VLA），并用跨本体真机数据做预训练；代表性证据是 Xiaomi-Robotics-1 宣称以 **超过 10 万小时真机轨迹**训练可开箱即用的移动操作 VLA [3]，以及 Open X-Embodiment 的跨本体数据聚合范式 [70][84]。这类"规模即能力"的论断目前多数仅有单方论文，属预印本级证据。
2. **世界模型（World Model）从"视频生成炫技"走向"可执行动作 grounding"。** 2025–2026 年的新工作集中在几何一致性（GEM-4D [26]）、潜动作解耦（DiLA [29]）、极简可复现实现（Nano World Models [30]）与规划耦合（Embodied Tree of Thoughts [113]）；更早的 VidMan 已尝试用视频扩散的隐式动力学增强操作 [76]。核心未解问题是"生成逼真 ≠ 物理可用"，目前仍缺统一评测。
3. **人形全身控制成为独立热点，但验证集中在仿真与精心设计的任务。** 羽毛球课程学习 [114]、站起控制跨姿态 [119]、全身遥操作 CHILD [116] 与 Humanoid Manipulation Interface [118] 代表 2025–2026 的典型工作；域随机化被系统用于全身扩散策略训练 [115]。真机泛化证据仍稀缺。
4. **评测生态正处于"基准爆炸 + 可比性危机"并存的阶段。** LIBERO 系列被扩展为语言改写鲁棒性（LIBERO-Para [78]）与闭环视觉鲁棒性（LIBERO-VPro [82]）诊断；研究界已明确把"仿真榜单表现 ≠ 真机通用能力"作为公开质疑，并出现反事实失败（视觉压过语言）这类系统性失效分析 [85]。Sim2Real 评测本身被作为方法论问题提出 [60]。
5. **工程落地的瓶颈是推理时延与低资源推理，而非模型规模。** 2025–2026 出现"实时运行 VLA" [96]、BLURR 低资源推理包装器 [106]、稀疏采样替代迭代去噪 [15] 等工程化工作；LeRobot 这类端到端库试图统一数据采集→训练→部署链路 [90]。但硬件门槛、可复现性仍普遍缺第三方核验。

---

## 一、关键前沿进展（近 1–2 年，2024–2026）

> 说明：本节只收录能给出 arXiv 链接与年份的条目；同一主题下若有更权威（同行评审）证据缺失，均以"预印本"表述。

### 1.1 VLA（Vision-Language-Action）基础模型

| 工作 | 时间 | 机构/线索 | 一句话贡献 | 证据四轴 |
|---|---|---|---|---|
| **Xiaomi-Robotics-1** | 2026 | 小米（论文未标注机构，标题可推） | 宣称以 10 万小时级真机轨迹训练 VLA，支持未见环境中开箱移动操作与少样本下游适配 [3] | 热度：`> 待核实`；权威：arXiv cs.RO 预印本 [3]；关注度：中（主题热度高但尚无引用数据）[3]；推荐度：★★★★☆（数据规模论断是当前最激进者，需独立复现）[3] |
| **Task adaptation of VLA: 1st Place, 2025 BEHAVIOR Challenge** | 2025 | 挑战赛冠军方案 | 基于 **Pi0.5（π0.5）** 架构，在 BEHAVIOR 50 项长时程家务任务（双臂 + 导航 + 上下文决策）中夺冠，是"竞赛级第三方可比"较强的 VLA 证据 [105] | 热度：`> 待核实`；权威：arXiv cs.RO 预印本 + 公开竞赛排名 [105]；关注度：中高（BEHAVIOR Challenge 为公开榜单）[105]；推荐度：★★★★★（少见的可对照榜单结果）[105] |
| **VLA-Adapter** | 2025 | — | 面向"极小规模 VLA"的有效范式，回应大模型推理成本问题 [102] | 热度：`> 待核实`；权威：arXiv 预印本 [102]；关注度：中 [102]；推荐度：★★★★☆（轻量化路线代表）[102] |
| **MiMo-Embodied** | 2025 | 技术报告 | 提出 X-Embodied 基础模型技术报告，指向跨本体统一建模 [112] | 热度：`> 待核实`；权威：arXiv 预印本（技术报告性质）[112]；关注度：中 [112]；推荐度：★★★★☆ [112] |
| **Embodied-R1.5** | 2026 | — | 以"具身基础模型"路径演进物理智能 [111] | 热度：`> 待核实`；权威：arXiv 预印本 [111]；关注度：中 [111]；推荐度：★★★☆☆（信息量有限）[111] |
| **One Policy, Many Embodiments** | 2026 | — | 统一"相机中心动作几何"预训练，面向异构本体操作 [110] | 热度：`> 待核实`；权威：arXiv 预印本 [110]；关注度：中 [110]；推荐度：★★★★☆（直击跨本体动作空间这一核心难题）[110] |
| **VLA 综述（Survey of VLA Models for Embodied Manipulation）** | 2025 | — | 系统梳理 VLA 用于具身操作的方法分类，可作为谱系骨架 [107] | 热度：`> 待核实`；权威：arXiv 综述预印本 [107]；关注度：中 [107]；推荐度：★★★★★（入门与分类首选）[107] |

补充：更宏观的领域综述为 *Aligning Cyber Space with Physical World: A Comprehensive Survey on Embodied AI* [33]，可用于交代"具身智能"整体范畴与术语体系。

### 1.2 世界模型驱动的策略 / 规划

- **GEM-4D**：几何增强的视频世界模型，针对"生成视频看似合理但无法跨帧跟踪同一物理点、缺物理 grounding"的问题 [26]。热度 `> 待核实`；权威 arXiv cs.CV 预印本 [26]；关注度中 [26]；推荐度 ★★★★☆（切中世界模型用于操作的真正痛点）[26]。
- **DiLA（Disentangled Latent Action World Models）**：指出潜动作模型（LAM）在"动作抽象 vs 生成保真"之间存在根本权衡，并提出解耦方案 [29]。权威 arXiv 预印本 [29]；推荐度 ★★★★☆ [29]。
- **Nano World Models**：极简、可复现的未来视频预测实现，回应社区"缺紧凑可扩展代码库"的抱怨 [30]。权威 arXiv 预印本 [30]；推荐度 ★★★★☆（工程可复现性价值高）[30]。
- **Embodied Tree of Thoughts**：把具身世界模型接入"深思式"操作规划 [113]。权威 arXiv 预印本 [113]；推荐度 ★★★★☆ [113]。
- **VidMan**（2024，较早）：从视频扩散模型中挖掘隐式动力学用于机器人操作 [76]。
- 经典线路：**Learning to Act without Actions**（UniSim / 世界模型驱动策略，2023）作为种子文献保留，链接 https://arxiv.org/abs/2312.10807 （种子资源，未含于本次编号来源）。

### 1.3 人形全身控制学习

- **Humanoid Whole-Body Badminton via Annealed RL Curriculum**：以退火式 RL 课程实现人形全身羽毛球 [114]。权威 arXiv cs.RO 预印本 [114]；关注度中 [114]；推荐度 ★★★★☆（高动态全身任务的代表）[114]。
- **Humanoid Manipulation Interface**：从"无机器人演示"中学习人形全身操作 [118]。
- **CHILD**：面向人形模仿与实时演示的全身遥操作系统 [116]。
- **Learning Humanoid Standing-up Control across Diverse Postures**：跨姿态站起控制，属于人形基础能力学习 [119]。
- **Miniature Humanoid Tele-Loco-Manipulation**：VR + RL 的小型人形遥操作移动操作 [120]。
- **The Role of Domain Randomization in Training Diffusion Policies for Whole-Body Humanoid Control**（2024）：全身人形扩散策略中域随机化的作用分析 [115] —— 这是"Sim2Real 手段归因"的少见系统性研究。
- 以上各条热度数据均 `> 待核实`（检索结果未返回引用数）；权威等级为 arXiv 预印本（B 级）。

### 1.4 鲁棒性与失效分析（新兴子方向）

- **When Vision Overrides Language**：系统刻画 VLA 的"反事实失败"——指令缺少场景强监督时，模型按视觉而非语言行动 [85]。权威 arXiv cs.CV 预印本 [85]；推荐度 ★★★★★（负面结果，价值高）[85]。
- **LIBERO-Para**：语言改写（paraphrase）鲁棒性诊断基准与指标 [78]。
- **LIBERO-VPro**：闭环视觉鲁棒性基准，指出标准评测默认"观测干净、及时、一致"这一不现实假设 [82]。
- **BLURR**：低资源 VLA 推理包装器，面向消费级 GPU 高频控制 [106]。
- **Running VLAs at Real-time Speed**：实时速度运行 VLA 的工程路径 [96]。
- **FLASH**：以稀疏 Legendre 多项式动作采样替代迭代去噪，直指 diffusion/flow matching 推理时延瓶颈 [15]。

### 1.5 检索噪声声明（必须显式剔除）

以下被检索系统召回但**与具身智能主题无关**，本报告不作为证据使用：短视频参与度预测挑战 [25]、蛋白质/抗体设计模型 [27][28][31]、图像超分辨率挑战 [49]、越南语法律问答挑战 [51]、事件图像分析挑战 [52]、对话机器人竞赛 [1]、机器生成文本检测 [2]、群体机器人连续环境估计 [8]。保留其编号仅为引用完整性。

---

## 二、方法谱系（模块化 → 端到端 → 基础模型 → 世界模型）

**2.1 模块化流水线（2022–2023，奠基期）**
- 语言规划 + 可行技能 grounding：**SayCan**（https://arxiv.org/abs/2204.01691 ，种子资源）
- LLM 直接生成策略代码：**Code as Policies**（https://arxiv.org/abs/2209.07753 ，种子资源）
- 具身多模态 LLM：**PaLM-E**（https://arxiv.org/abs/2303.03378 ，种子资源）
- 早期视觉运动表征学习铺垫：*Self-Supervised Correspondence in Visuomotor Policy Learning*（2019）[10]。
- 谱系定位可参考具身智能综述 [33] 与 VLA 综述 [107]。

**2.2 端到端模仿学习 / 强化学习（承上启下）**
- 低成本双臂遥操作硬件与数据范式：**ALOHA 2** [17]、**Mobile ALOHA** [18] —— 这两条是"数据从哪来"的关键工程答案。
- 模仿 + 规划 + RL 协同：**SPIRE**（长时程操作）[19]。
- 离线 RL 工程基础设施：**CORL** [20]。
- 早期 on-policy 模仿与异构动作空间： [21][22]。
- Diffusion Policy 与 RT-1/RT-2：本次检索**未返回其一手来源**，`> 待核实`（仅可经综述 [107] 间接引用其谱系位置）。

**2.3 基础模型（2024–2026）**
- **Octo**：开源通用机器人策略，RSS 会议论文，1998 次引用 [74] —— 本报告中最强的"开源 + 同行评审 + 高引用"三重证据。
- **OpenVLA**：开源 VLA 模型 [79][98]（同一工作两个 arXiv 版本）。
- **π0.5 / Pi0.5**：在 BEHAVIOR Challenge 冠军方案中被作为基础架构 [105]；其原始论文未在本次来源中，`> 待核实`。
- 跨本体统一：**One Policy, Many Embodiments** [110]、**MiMo-Embodied** [112]、**Open X-Embodiment / RT-X** [70][84]。
- 数据配比与规模化定律：**Re-Mix**（大规模模仿学习的数据混合优化）[77]。

**2.4 世界模型（并行分支）**
- 视频扩散隐式动力学 → 操作增强：VidMan [76]
- 几何一致性世界模型：GEM-4D [26]
- 潜动作解耦：DiLA [29]
- 极简可复现实现：Nano World Models [30]
- 世界模型 + 规划搜索：Embodied Tree of Thoughts [113]
- 无动作标签学习：Learning to Act without Actions（种子资源）

> **谱系判断**：模块化 → 端到端 → 基础模型的演化证据较充分（[74][79][107][70]）；**"世界模型是否已构成第三条主流路线"目前证据不足**，多数工作仍停留在生成质量与规划可行性验证，缺少跨本体真机大规模验证 `> 待核实`。

---

## 三、仿真平台与基准对比

| 平台 | 年份 | 关键能力 | 开源/许可 | 权威与热度 | 关注度 | 推荐度 |
|---|---|---|---|---|---|---|
| **Isaac Lab** | 2025 | GPU 加速、多模态机器人学习框架 [41] | 开源（NVIDIA 生态）[41] | arXiv 预印本 [41]；热度 `> 待核实` | 中高（NVIDIA 生态默认选择）[41] | ★★★★★ [41] |
| **NVIDIA Isaac Sim** | 2026 | 可扩展 GPU 加速机器人仿真 [44] | 官方产品线 [44] | arXiv 预印本/官方技术文 [44] | 中高 [44] | ★★★★★ [44] |
| **Isaac Gym** | 2021 | GPU 并行物理仿真，Isaac Lab 前身 [42] | 开源 [42] | arXiv 预印本 [42] | 高（历史影响力）[42] | ★★★★☆（已被 Isaac Lab 接续）[42] |
| **Isaac Sim 生态扩展** | 2026 | 事件相机插件 EsaacSim [43]；结构光虚拟传感器 VIRTUS-FPP [47] | 研究原型 [43][47] | arXiv 预印本 [43][47] | 低—中 [43][47] | ★★★☆☆（传感器仿真补强，细分用途）[43][47] |
| **MuJoCo Playground** | 2025 | MuJoCo 上的 GPU 并行学习 playground [48] | 开源 [48] | arXiv 预印本 [48] | 中高 [48] | ★★★★★ [48] |
| **RoboTwin 2.0** | 2025 | 可扩展数据生成 + 强域随机化的双臂操作基准 [91] | 开源（论文宣称）[91] | arXiv 预印本，**citations=569** [91] | 高（569 次引用）[91] | ★★★★★ [91] |
| **Genesis** | 2024– | 生成式物理仿真引擎 | 开源 | 种子项目，链接 https://github.com/Genesis-Embodied-AI/Genesis ；热度 `> 待核实` | 高（社区讨论度高，但本次未取得量化证据）`> 待核实` | ★★★★☆（需自行核验成熟度） |
| **ManiSkill** | 2023– | GPU 并行操作基准 | 开源 | 种子项目 https://github.com/haosulab/ManiSkill ；热度 `> 待核实` | 中高 `> 待核实` | ★★★★☆ |
| **BEHAVIOR-1K / OmniGibson** | 2024 | 1000 项日常活动、以人为中心的具身基准 | 开源 | 种子论文 https://arxiv.org/abs/2403.09227 、https://github.com/StanfordVL/BEHAVIOR-1K ；其 2025 挑战赛有论文记录 [105] | 高（有公开挑战赛）[105] | ★★★★★ [105] |
| **Habitat 3.0** | — | 室内导航/社交仿真 | — | 本次**无来源** `> 待核实` | `> 待核实` | `> 待核实` |
| **SAPIEN** | — | 部件级关节物体仿真 | — | 本次**无来源** `> 待核实` | `> 待核实` | `> 待核实` |

**仿真→真机桥接的工程证据**：从 Isaac Sim 到 Gazebo 再到真实 ROS 2 机器人的迁移流程已在移动机器人 RL 上给出实证 [46]；跨引擎统一建模框架 EAGERx 提供了图结构化的 Sim2Real 抽象 [99]。

---

## 四、经典与奠基性工作

| 名称 | 年份 | 机构/作者 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| **SayCan: Do As I Can, Not As I Say** | 2022 | Google | `> 待核实` | 种子资源（未含编号来源） | 高（LLM 机器人规划开山作）`> 待核实` | ★★★★★ | https://arxiv.org/abs/2204.01691 | LLM 规划 + 技能可行性 grounding |
| **Code as Policies** | 2022 | Google | `> 待核实` | 种子资源 | 高 `> 待核实` | ★★★★★ | https://arxiv.org/abs/2209.07753 | LLM 生成机器人策略代码 |
| **PaLM-E** | 2023 | Google | `> 待核实` | 种子资源 | 高 `> 待核实` | ★★★★★ | https://arxiv.org/abs/2303.03378 | 具身多模态 LLM 奠基 |
| **Learning to Act without Actions（世界模型线）** | 2023 | Various | `> 待核实` | 种子资源 | 中高 `> 待核实` | ★★★★☆ | https://arxiv.org/abs/2312.10807 | 无动作标签的潜动作学习 |
| **ALOHA 2** | 2024 | Stanford / Google DeepMind（论文题注） | `> 待核实` | arXiv 预印本 [17] | 高（开源硬件生态）`> 待核实` | ★★★★★ | http://arxiv.org/abs/2405.02292v1 | 低成本双臂遥操作硬件 |
| **Mobile ALOHA** | 2024 | Stanford | `> 待核实` | arXiv 预印本 [18] | 高 `> 待核实` | ★★★★★ | http://arxiv.org/abs/2401.02117v1 | 低成本全身遥操作双臂移动操作 |
| **Octo: An Open-Source Generalist Robot Policy** | 2024 | Octo 团队 | **citations=1998** [74] | **RSS 会议（同行评审）** [74] | 高（1998 次引用）[74] | ★★★★★ | https://arxiv.org/abs/2405.12213 | 开源通用机器人策略，开源复现基线 |
| **OpenVLA** | 2024 | Stanford 等 | `> 待核实` | arXiv 预印本 [79][98] | 高（社区广泛使用）`> 待核实` | ★★★★★ | https://arxiv.org/abs/2406.09246 | 开源 VLA 模型基线 |
| **Open X-Embodiment / RT-X** | 2024 | Open X-Embodiment Collaboration | `> 待核实` | arXiv 预印本 [70][84] | 高（跨本体数据标准）`> 待核实` | ★★★★★ | http://arxiv.org/abs/2310.08864v9 | 跨本体真机数据与 RT-X 模型 |
| **DROID** | 2024 | 多机构协作 | `> 待核实` | arXiv 预印本 [68] | 高（真实场景大规模数据）`> 待核实` | ★★★★★ | http://arxiv.org/abs/2403.12945v2 | 野外（in-the-wild）机器人操作数据集 |
| **BEHAVIOR-1K** | 2024 | Stanford | `> 待核实` | 种子资源 + 挑战赛论文 [105] | 高 [105] | ★★★★★ | https://arxiv.org/abs/2403.09227 | 1000 项日常活动基准 |
| **Self-Supervised Correspondence in Visuomotor Policy Learning** | 2019 | — | `> 待核实` | arXiv 预印本 [10] | 中（历史线索）[10] | ★★★☆☆ | http://arxiv.org/abs/1909.06933v1 | 视觉运动表征学习前史 |
| **RT-1 / RT-2 / Diffusion Policy** | 2022–2023 | Google / Columbia 等 | `> 待核实` | **本次检索未返回一手来源** `> 待核实` | 高（公认经典） | ★★★★★（建议另行补检） | `> 待核实` | 谱系位置关键，但本报告不为其数字背书 |

---

## 五、开源项目与工程实践

| 项目 | 年份 | 维护方 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| **LeRobot** | 2026 | Hugging Face 生态（论文题注） | `> 待核实` | arXiv 预印本 [90]；官方库 | 高（端到端一站式）`> 待核实` | ★★★★★ | http://arxiv.org/abs/2602.22818v1 | 数据采集→训练→部署的端到端库 |
| **Octo** | 2024 | Octo 团队 | **citations=1998** [74] | RSS 同行评审 [74] | 高 [74] | ★★★★★ | https://arxiv.org/abs/2405.12213 | 开源通用策略，复现友好 |
| **OpenVLA** | 2024 | Stanford 等 | `> 待核实` | arXiv 预印本 [79][98] | 高 `> 待核实` | ★★★★★ | https://arxiv.org/abs/2406.09246 | 开源 VLA 权重与训练代码 |
| **Isaac Lab** | 2025 | NVIDIA | `> 待核实` | arXiv 预印本 + 官方仓库 [41] | 高 [41] | ★★★★★ | http://arxiv.org/abs/2511.04831v1 | GPU 并行训练主力框架 |
| **RoboTwin 2.0** | 2025 | — | **citations=569** [91] | arXiv 预印本 [91] | 高（569 次引用）[91] | ★★★★★ | https://arxiv.org/abs/2506.18088 | 双臂操作数据生成 + 强域随机化 |
| **Genesis** | 2024– | Genesis-Embodied-AI | `> 待核实` | GitHub 开源项目（种子） | 高（社区热度）`> 待核实` | ★★★★☆ | https://github.com/Genesis-Embodied-AI/Genesis | 生成式物理引擎 |
| **ManiSkill** | 2023– | haosulab | `> 待核实` | GitHub 开源项目（种子） | 中高 `> 待核实` | ★★★★☆ | https://github.com/haosulab/ManiSkill | GPU 并行操作基准 |
| **BEHAVIOR-1K / OmniGibson** | 2024 | Stanford VL | `> 待核实` | GitHub + 论文 [种子]、挑战赛 [105] | 高 [105] | ★★★★★ | https://github.com/StanfordVL/BEHAVIOR-1K | 基准 + 仿真 + 挑战赛闭环 |
| **CORL** | 2022 | — | `> 待核实` | arXiv 预印本 [20] | 中 [20] | ★★★☆☆ | http://arxiv.org/abs/2210.07105v4 | 面向研究的离线 RL 库 |
| **EAGERx** | 2024 | — | `> 待核实` | IEEE Robotics & Automation Magazine（期刊）[99] | 中 [99] | ★★★★☆ | https://doi.org/10.1109/MRA.2024.3433172 | 图结构的引擎无关 Sim2Real 框架 |
| **ROS 2 + Isaac Sim 迁移管线** | 2025 | — | `> 待核实` | arXiv 预印本 [46] | 中 [46] | ★★★★☆ | http://arxiv.org/abs/2501.02902v1 | 移动机器人 RL 从 Isaac Sim 到 Gazebo/真机 ROS 2 |

**工程实践要点**
- **推理时延是首个被解决的瓶颈**：实时 VLA [96]、低资源包装器 [106]、稀疏采样动作头 [15] 三条路径同时出现，说明"能不能跑得动"已被公认为落地前提。
- **数据链路正在标准化**：跨本体数据聚合 [70][84] + 数据配比优化 [77] + 端到端库 [90] 构成"数据—训练—部署"三段式。
- **可复现性仍是弱项**：除 Octo [74] 与 RoboTwin 2.0 [91] 有可量化的引用热度外，多数项目缺乏第三方复现报告 `> 待核实`。

---

## 六、数据集与评测协议

| 数据集/基准 | 年份 | 规模与本体 | 真机/仿真 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 链接 |
|---|---|---|---|---|---|---|---|---|
| **Open X-Embodiment** | 2024 | 跨本体真机数据聚合（多机器人）| 真机 | `> 待核实` | arXiv 预印本 [70][84] | 高 [70] | ★★★★★ | http://arxiv.org/abs/2310.08864v9 |
| **DROID** | 2024 | 大规模野外操作 | 真机 | `> 待核实` | arXiv 预印本 [68] | 高 [68] | ★★★★★ | http://arxiv.org/abs/2403.12945v2 |
| **BEHAVIOR-1K** | 2024–2025 | 1000 项日常活动；挑战赛含 50 项长时程家务任务 | 仿真（照片级真实感）[105] | `> 待核实` | 种子资源 + 挑战赛论文 [105] | 高 [105] | ★★★★★ | https://behavior.stanford.edu/ |
| **RoboTwin 2.0** | 2025 | 双臂操作数据生成 + 强域随机化 | 仿真 | **citations=569** [91] | arXiv 预印本 [91] | 高 [91] | ★★★★★ | https://arxiv.org/abs/2506.18088 |
| **LIBERO-Para** | 2026 | 语言改写鲁棒性诊断 + 指标 | 基于 LIBERO | `> 待核实` | arXiv cs.LG 预印本 [78] | 中高 [78] | ★★★★☆ | http://arxiv.org/abs/2603.28301v3 |
| **LIBERO-VPro** | 2026 | 闭环视觉鲁棒性（扰动观测）| 仿真 | `> 待核实` | arXiv cs.RO 预印本 [82] | 中高 [82] | ★★★★☆ | http://arxiv.org/abs/2609.24350v1 |
| **Impromptu VLA** | 2025 | 8 万+ 自动驾驶 corner case 片段 | 数据集（驾驶）| `> 待核实` | arXiv cs.CV 预印本 [94] | 中 [94] | ★★★☆☆（驾驶域，与操作域部分通用）[94] | http://arxiv.org/abs/2505.23757v1 |
| **AgiBot World** | — | 大规模真机具身数据集 | 真机 | `> 待核实` | 种子资源（官方站） | 中高 `> 待核实` | ★★★★☆ | https://agibot-world.com/ |
| **SimplerEnv** | — | 仿真复现真机策略评测 | 仿真 | 本次**无来源** `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` |
| **RoboArena** | — | 分布式真机评测协议 | 真机 | 本次**无来源** `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` |
| **RoboMIND** | — | 多本体操作数据 | — | 本次**无来源** `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` |
| **Re-Mix（数据配比方法）** | 2024 | 大规模模仿学习数据混合优化 | 通用方法 | `> 待核实` | arXiv 预印本 [77] | 中 [77] | ★★★★☆ | https://arxiv.org/abs/2408.14037 |

**可比性与评测可信度问题（有明确来源）**
1. **干净观测假设不成立**：LIBERO-VPro 明确指出主流评测默认执行全程视觉观测"干净、及时、一致"，与真实部署不符 [82]。
2. **语言条件脆弱**：LIBERO-Para 表明 VLA 在有限数据微调后过度拟合特定指令表述 [78]；进一步地，*When Vision Overrides Language* 揭示当指令缺乏场景强监督时，模型会按视觉而非语言行动（反事实失败）[85]。
3. **仿真 SOTA ≠ 真机 SOTA**：*Robot Policy Evaluation for Sim-to-Real Transfer: A Benchmarking Perspective* 直接把"真机评估方法论落后于仿真基准"作为问题提出 [60]。
4. **跨基准不可直接比较**：本体、任务数、观测口径、是否真机各不相同，本报告拒绝给出跨基准的"统一 SOTA 排名" `> 待核实`。

---

## 七、Sim2Real 与开放问题

### 7.1 Sim2Real 三类手段的 2024–2026 证据现状

| 手段 | 代表证据 | 结论强度 |
|---|---|---|
| **域随机化（Domain Randomization）** | 全身人形扩散策略的域随机化作用分析 [115]；RoboTwin 2.0 将强域随机化作为数据生成核心 [91]；随机化对 RL 操作迁移效果的系统分析（早期）[86]；导丝导航的 Sim2Real 域随机化（期刊）[87] | 中：结论集中在"有帮助但需调参"，跨任务稳定性 `> 待核实` |
| **系统辨识（System Identification）** | 本次检索**未返回** 2024–2026 的一手证据 `> 待核实` | 低：`> 待核实` |
| **真实数据微调 / 域适应** | 视觉编码器预训练以桥接 Sim2Real（两版） [61][97]；多模态融合用于视觉 RL 的 Sim2real [93]；在线域适应 + 视触觉高精度操作 [88]（期刊）；Sim2Real 后的安全持续域适应 [89] | 中高：多篇独立工作指向"预训练视觉表征 + 在线适应"是当前主流 |
| **感知层 gap（深度噪声）** | RealD²iff：用扩散模型反转真实深度噪声模式，桥接视觉 Sim2Real gap [66] | 中：单点证据，需复现 |
| **评测层** | Sim2Real 迁移的基准化视角 [60]；R:SS 2020 研讨会总结（领域共识文本）[63]；精密农业中 Sim2Real 的重要性与局限 [62] | 中高：已形成"评测滞后"的共识性问题 |
| **LLM/VLM 驱动的 Sim2Real** | GPT-6-Astra 驱动的机器人操作：身体知识、经验复用、涌现技能与 Sim2Real 迁移 [64] | 低：单篇预印本，且依赖具体商业模型版本 `> 待核实` |

### 7.2 开放问题清单

1. **泛化到新本体**：统一动作空间仍是难点，代表性尝试 [110][112] 均未给跨本体真机规模的第三方验证。`> 待核实`
2. **真机 vs 仿真 SOTA 落差**：评测方法论被明确指为滞后项 [60][82]。
3. **语言 grounding 的真实性**：反事实失败说明"看起来听指令"可能只是视觉驱动 [85]；指令改写敏感性 [78]。
4. **复现困难与负面结果披露不足**：除少数高引用开源基线 [74][91]，多数 2025–2026 工作未提供第三方复现；本报告未检索到系统性的负结果汇总 `> 待核实`。
5. **数据规模 vs 算力归因**：Xiaomi-Robotics-1 的 10 万小时真机轨迹 [3] 属"数据驱动"论断，但缺乏消融式归因（数据/架构/算力各占多少） `> 待核实`；Re-Mix 提供了数据配比层面的方法论 [77]。
6. **推理时延与部署成本**：[96][106][15] 说明这是被承认的工程瓶颈，但"多快才算够"缺统一指标。
7. **安全、可靠性与认证**：*Toward Maturity-Based Certification of Embodied AI* 提出以成熟度分级量化可信度 [36]；基础模型透明度指数（2025）从治理侧提出披露要求 [50]，但与机器人具体安全标准之间的衔接 `> 待核实`。
8. **感知硬件新维度**：全向视觉在具身时代的角色综述 [34]；边缘设备上的轻量扩散感知 [35] —— 说明"感知前端"仍在演化。

> **争议提示**：世界模型是否能作为独立于 VLA 的主流范式，本报告给出的判断是"证据不足、不宜定论"。理由：现有世界模型工作 [26][29][30][113] 多聚焦生成质量与规划可行性，缺少跨本体真机大规模评测 `> 待核实`。

---

## 八、建议关注清单（Watchlist）

| 序号 | 关注对象 | 为什么关注 | 关键证据 | 观察指标 |
|---|---|---|---|---|
| 1 | **BEHAVIOR Challenge 系列与冠军方案** | 少见的公开榜单 + 长时程双臂家务任务 | [105] | 榜单排名、是否开源方案、次日是否被复现 |
| 2 | **Octo / OpenVLA 开源基线生态** | 唯一有高引用与同行评审背书的开源基线 | [74][79][98] | GitHub star/issue 活跃度、下游微调论文数（`> 待核实`） |
| 3 | **RoboTwin 2.0 与域随机化数据生成** | 569 次引用，说明数据合成路线被广泛采用 | [91][115][86] | 是否有真机迁移的独立验证 |
| 4 | **LIBERO 系列鲁棒性基准（Para / VPro）** | 把"评测假设"变成可度量对象 | [78][82] | 是否被主流 VLA 论文采纳为报告项 |
| 5 | **VLA 推理加速（实时、低资源、稀疏采样）** | 决定能否上真机的硬约束 | [96][106][15] | 延迟/吞吐指标是否统一、硬件门槛是否下降 |
| 6 | **世界模型的可执行性（GEM-4D / DiLA / Nano WM）** | 几何一致性与潜动作解耦是当前最有希望的技术切口 | [26][29][30] | 是否出现真机闭环任务的成功率数据 |
| 7 | **人形全身控制（Badminton / CHILD / HMI / 站起）** | 2025–2026 数量增长明显，但验证条件分散 | [114][116][118][119][115] | 是否出现跨任务统一策略与真机长时程演示 |
| 8 | **跨本体统一动作空间（One Policy Many Embodiments / MiMo-Embodied）** | 直接对应"泛化到新本体"这一核心开放问题 | [110][112][70] | 新增本体的零样本/少样本迁移成功率 |
| 9 | **Sim2Real 评测方法论（基准化视角 / 持续域适应）** | 决定领域结论的可信度 | [60][89][93][61] | 是否形成社区公认的真机评测协议 |
| 10 | **可信与认证（成熟度分级 / 透明度指数）** | 规模化部署的前置条件 | [36][50] | 是否被厂商或标准组织采纳 |

---

## 参考来源

[1] Proceedings of the Dialogue Robot Competition 2023 — http://arxiv.org/abs/2312.14430v5
[2] Overview of AuTexTification at IberLEF 2023 — http://arxiv.org/abs/2309.11285v1
[3] Xiaomi-Robotics-1: Scaling Vision-Language-Action Models with over 100K Hours of Real-World Trajectories — http://arxiv.org/abs/2607.15330v2
[4] CaRE: Finding Root Causes of Configuration Issues in Highly-Configurable Robots — http://arxiv.org/abs/2301.07690v2
[5] Deep Kernel and Image Quality Estimators for Optimizing Robotic Ultrasound Controller using Bayesian Optimization — http://arxiv.org/abs/2310.07392v1
[6] Strategies to Harness the Transformers' Potential: UNSL at eRisk 2023 — http://arxiv.org/abs/2310.19970v1
[7] Active Metric-Semantic Mapping by Multiple Aerial Robots — http://arxiv.org/abs/2209.08465v4
[8] Estimation of continuous environments by robot swarms — http://arxiv.org/abs/2302.13629v2
[9] Explainable Machine Learning for Public Policy — http://arxiv.org/abs/2010.14374v3
[10] Self-Supervised Correspondence in Visuomotor Policy Learning — http://arxiv.org/abs/1909.06933v1
[11] Conformal Policy Learning for Sensorimotor Control Under Distribution Shifts — http://arxiv.org/abs/2311.01457v1
[12] Policy Learning with Observational Data — http://arxiv.org/abs/1702.02896v6
[13] OnlineCache: Learning Dynamic Caching Policies with Error Correction for Efficient Diffusion Inference — http://arxiv.org/abs/2607.29398v1
[14] Policy Implications of Statistical Estimates — http://arxiv.org/abs/2008.10903v4
[15] FLASH: Efficient Visuomotor Policy via Sparse Sampling — http://arxiv.org/abs/2605.15492v2
[16] Factorizing Diffusion Policies for Observation Modality Prioritization — http://arxiv.org/abs/2509.16830v1
[17] ALOHA 2: An Enhanced Low-Cost Hardware for Bimanual Teleoperation — http://arxiv.org/abs/2405.02292v1
[18] Mobile ALOHA: Learning Bimanual Mobile Manipulation with Low-Cost Whole-Body Teleoperation — http://arxiv.org/abs/2401.02117v1
[19] SPIRE: Synergistic Planning, Imitation, and Reinforcement Learning for Long-Horizon Manipulation — http://arxiv.org/abs/2410.18065v1
[20] CORL: Research-oriented Deep Offline Reinforcement Learning Library — http://arxiv.org/abs/2210.07105v4
[21] On-Policy Robot Imitation Learning from a Converging Supervisor — http://arxiv.org/abs/1907.03423v7
[22] Reinforced Imitation in Heterogeneous Action Space — http://arxiv.org/abs/1904.03438v2
[23] Imitation Learning for End to End Vehicle Longitudinal Control with Forward Camera — http://arxiv.org/abs/1812.05841v1
[24] NTU-NPU System for Voice Privacy 2024 Challenge — http://arxiv.org/abs/2410.02371v1
[25] VQualA 2025 Challenge on Engagement Prediction for Short Videos — http://arxiv.org/abs/2509.02969v1
[26] GEM-4D: Geometry-Enhanced Video World Models for Robot Manipulation — http://arxiv.org/abs/2605.22882v4
[27] Latent-X: An Atom-level Frontier Model for De Novo Protein Binder Design — http://arxiv.org/abs/2507.19375v1
[28] Latent-Y: A Lab-Validated Autonomous Agent for De Novo Drug Design — http://arxiv.org/abs/2603.29727v2
[29] DiLA: Disentangled Latent Action World Models — http://arxiv.org/abs/2605.15725v1
[30] Nano World Models: A Minimalist Implementation of Future Video Prediction — http://arxiv.org/abs/2605.23993v2
[31] Drug-like antibodies with low immunogenicity in human panels designed with Latent-X2 — http://arxiv.org/abs/2512.20263v1
[32] Engagement Prediction of Short Videos with Large Multimodal Models — http://arxiv.org/abs/2508.02516v2
[33] Aligning Cyber Space with Physical World: A Comprehensive Survey on Embodied AI — http://arxiv.org/abs/2407.06886v8
[34] PANORAMA: The Rise of Omnidirectional Vision in the Embodied AI Era — http://arxiv.org/abs/2509.12989v1
[35] Multi-Step Guided Diffusion for Image Restoration on Edge Devices — http://arxiv.org/abs/2506.07286v1
[36] Toward Maturity-Based Certification of Embodied AI — http://arxiv.org/abs/2601.03470v2
[37] Physics Briefing Book — http://arxiv.org/abs/1910.11775v2
[38] Faith in AI can narrow the futures individuals consider — http://arxiv.org/abs/2603.28944v2
[39] Physics and Technology of the Next Linear Collider — http://arxiv.org/abs/hep-ex/9605011v1
[40] The Synthesis of Optimal Control Laws Using Isaacs' Method — http://arxiv.org/abs/2112.10849v2
[41] Isaac Lab: A GPU-Accelerated Simulation Framework for Multi-Modal Robot Learning — http://arxiv.org/abs/2511.04831v1
[42] Isaac Gym: High Performance GPU-Based Physics Simulation For Robot Learning — http://arxiv.org/abs/2108.10470v2
[43] EsaacSim: A Multimodal Event Camera Add-on for NVIDIA Isaac Sim — http://arxiv.org/abs/2608.08522v2
[44] NVIDIA Isaac Sim: Enabling Scalable, GPU-Accelerated Simulation for Robotics — http://arxiv.org/abs/2606.03551v1
[45] ISAAC Newton: Input-based Approximate Curvature for Newton's Method — http://arxiv.org/abs/2305.00604v1
[46] Sim-to-Real Transfer for Mobile Robots with Reinforcement Learning: from NVIDIA Isaac Sim to Gazebo and Real ROS 2 Robots — http://arxiv.org/abs/2501.02902v1
[47] VIRTUS-FPP: Virtual Sensor Modeling for Fringe Projection Profilometry in NVIDIA Isaac Sim — http://arxiv.org/abs/2509.22685v2
[48] MuJoCo Playground — http://arxiv.org/abs/2502.08844v1
[49] NTIRE 2025 Challenge on Image Super-Resolution (x4) — http://arxiv.org/abs/2504.14582v3
[50] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1
[51] VLSP 2025 MLQA-TSR Challenge — http://arxiv.org/abs/2510.20381v1
[52] Event-Enriched Image Analysis Grand Challenge at ACM Multimedia 2025 — http://arxiv.org/abs/2508.18904v1
[53] Competing Visions of Ethical AI: A Case Study of OpenAI — http://arxiv.org/abs/2601.16513v1
[54] mdok of KInIT: Robustly Fine-tuned LLM for AI-Generated Text Detection — http://arxiv.org/abs/2506.01702v2
[55] Search the Lightest Path in AI Contexts — https://doi.org/10.5281/zenodo.23000372
[56] Search the Lightest Path in AI Contexts — https://doi.org/10.5281/zenodo.23000371
[57] Atyaephyra at SemEval-2025 Task 4 — http://arxiv.org/abs/2503.13690v2
[58] The 6th International Verification of Neural Networks Competition (VNN-COMP 2025) — http://arxiv.org/abs/2512.19007v1
[59] LongEval at CLEF 2025 — http://arxiv.org/abs/2503.08541v1
[60] Robot Policy Evaluation for Sim-to-Real Transfer: A Benchmarking Perspective — http://arxiv.org/abs/2508.11117v1
[61] Bridging the Sim2Real Gap: Vision Encoder Pre-Training for Visuomotor Policy Transfer — http://arxiv.org/abs/2501.16389v2
[62] The Importance and the Limitations of Sim2Real for Robotic Manipulation in Precision Agriculture — http://arxiv.org/abs/2008.03983v1
[63] Perspectives on Sim2Real Transfer for Robotics: A Summary of the R:SS 2020 Workshop — http://arxiv.org/abs/2012.03806v1
[64] Robot Manipulation with GPT-6-Astra: Body Knowledge, Experience Reuse, Emergent Skills, and Sim2Real Transfer — http://arxiv.org/abs/2609.31770v1
[65] Grasp and Motion Planning for Dexterous Manipulation for the Real Robot Challenge — http://arxiv.org/abs/2101.02842v1
[66] RealD²iff: Bridging Real-World Gap in Robot Manipulation via Depth Diffusion — http://arxiv.org/abs/2511.22505v2
[67] Overview of the Sensemaking Task at the ELOQUENT 2025 Lab — http://arxiv.org/abs/2507.12143v1
[68] DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset — http://arxiv.org/abs/2403.12945v2
[69] Point Transformer V3 Extreme: 1st Place Solution for 2024 Waymo Open Dataset Challenge — http://arxiv.org/abs/2407.15282v1
[70] Open X-Embodiment: Robotic Learning Datasets and RT-X Models — http://arxiv.org/abs/2310.08864v9
[71] The RSNA Abdominal Traumatic Injury CT (RATIC) Dataset — http://arxiv.org/abs/2405.19595v1
[72] The RSNA Intracranial Aneurysm (RSNA-ICA) Dataset — http://arxiv.org/abs/2610.01135v2
[73] Unfiltered Conversations: A Dataset of 2024 U.S. Presidential Election Discourse on Truth Social — http://arxiv.org/abs/2411.01330v1
[74] Octo: An Open-Source Generalist Robot Policy — https://arxiv.org/abs/2405.12213
[75] Discovery Opportunities with Gravitational Waves -- TASI 2024 Lecture Notes — http://arxiv.org/abs/2409.08956v1
[76] VidMan: Exploiting Implicit Dynamics from Video Diffusion Model for Effective Robot Manipulation — https://arxiv.org/abs/2411.09153
[77] Re-Mix: Optimizing Data Mixtures for Large Scale Imitation Learning — https://arxiv.org/abs/2408.14037
[78] LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models — http://arxiv.org/abs/2603.28301v3
[79] OpenVLA: An Open-Source Vision-Language-Action Model — https://arxiv.org/abs/2406.09246
[80] Benchmarking Vision, Language, & Action Models on Robotic Learning Tasks — https://arxiv.org/abs/2411.05821
[81] TraceVLA: Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies — https://arxiv.org/abs/2412.10345
[82] LIBERO-VPro: Benchmarking Closed-Loop Visual Robustness of Robotic Foundation Models — http://arxiv.org/abs/2609.24350v1
[83] CLIP-RT: Learning Language-Conditioned Robotic Policies from Natural Language Supervision — https://arxiv.org/abs/2411.00508
[84] Open X-Embodiment: Robotic Learning Datasets and RT-X Models : Open X-Embodiment Collaboration — https://arxiv.org/abs/2310.08864
[85] When Vision Overrides Language: Evaluating and Mitigating Counterfactual Failures in VLAs — http://arxiv.org/abs/2602.17659v2
[86] Analysis of Randomization Effects on Sim2Real Transfer in Reinforcement Learning for Robotic Manipulation Tasks — http://arxiv.org/abs/2206.06282v2
[87] Sim2Real Learning With Domain Randomization for Autonomous Guidewire Navigation — https://doi.org/10.1109/TASE.2025.3555559
[88] Online Domain Adaption for Sim2Real Transfer of High-Precision Manipulation with Visuotactile Sensing — https://doi.org/10.1109/CYBER67662.2025.11168381
[89] Safe Continual Domain Adaptation after Sim2Real Transfer of Reinforcement Learning Policies in Robotics — http://arxiv.org/abs/2503.10949
[90] LeRobot: An Open-Source Library for End-to-End Robot Learning — http://arxiv.org/abs/2602.22818v1
[91] RoboTwin 2.0: A Scalable Data Generator and Benchmark with Strong Domain Randomization — https://arxiv.org/abs/2506.18088
[92] Open Source Software Development Challenges: A Systematic Literature Review on GitHub — http://arxiv.org/abs/2003.10750v3
[93] Multimodal Fusion for Sim2real Transfer in Visual Reinforcement Learning — http://arxiv.org/abs/2507.09180
[94] Impromptu VLA: Open Weights and Open Data for Driving Vision-Language-Action Models — http://arxiv.org/abs/2505.23757v1
[95] Sim2Real Rope Cutting With a Surgical Robot Using Vision-Based Reinforcement Learning — https://doi.org/10.1109/TASE.

---

*Generated by research-bot · topic=`embodied-ai` · depth=`standard` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading · model=`deepseek-v4-flash` · sources=121 · duration=297s · 2026-10-06T22:24:36+00:00*
