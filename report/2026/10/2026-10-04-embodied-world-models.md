# 具身智能 · 世界模型与仿真（World Models & Simulation）：技术地图与选型调研报告

> **元信息**｜撰写日期：2026-10-04（UTC）｜领域：具身智能 / 世界模型（World Models）/ 机器人仿真（Simulation）/ sim2real｜可引用证据来源：30 条（编号 [1]–[30]）＋人工维护种子资源 11 条｜检索口径：arXiv 预印本、期刊与会议 DOI、GitHub 项目主页｜**引用数（citations）为候选块给出的聚合字段，存在统计时滞，仅作热度参考，不等价于同行评审质量**。

---

## 摘要（Executive Summary）

1. **生成式世界模型正从"视频好看"走向"可控动力学"**。2025–2026 年的主线是把世界模型改造成能接受动作条件、可长时程滚动、并能与现有 VLA/通用策略闭环的**可控**模拟器：Ctrl-World 明确提出需支持多视角预测、细粒度动作控制与长时程一致交互，并指出真机 rollout 与纠正数据是评测与改进的瓶颈 [11]；Genie Envisioner 尝试把策略学习、评估与仿真整合进单一视频生成框架 [9]；Motus 则提出统一隐动作世界模型以打通理解、世界建模与控制三类割裂模型 [20]。
2. **"物理一致性"成为独立评测维度，且被证伪风险高**。T2VPhysBench 主张文本到视频模型在物理规律遵从性上"largely untested"，并给出 first-principles 基准 [14]；WoW 进一步提出物理直觉须 grounded 于具身交互与因果丰富的数据，而非被动观察 [15]。两者的结论均以 arXiv 预印本形式发布，尚需第三方复现与独立榜单验证 [14][15]。
3. **评测可信度是当前最尖锐的开放争议**：视频世界模型用于策略评测长期局限于分布内场景，Gemini Robotics 官方报告声称可扩展到全谱系策略评估用例，但属自评性质 [10]；1X World Model Challenge 则尝试用人形真机交互构建开源基准，提供 sampling 等互补赛道 [17]。
4. **仿真侧的主旋律是"GPU 并行 + 可微"双轮驱动**。ManiSkill3 是本轮证据中热度最高的仿真-基准工作（citations=344），主打 GPU 并行仿真与渲染 [30]；[26] 系统评测了大规模并行多任务 RL；可微物理路线由 Differentiable Particle Optimization [25] 与可微颗粒挖掘机器人 DDBot [27] 代表；触觉仿真在 Isaac Sim 中通过 TacEx 打通软体-视触觉链路 [3][6]。
5. **证据缺口必须显式声明**：本轮针对"世界模型/MBRL 经典奠基与演进脉络"（q2）与"sim2real 方法论与可微仿真系统对比"（q5）**未返回结构化发现**。本报告相应章节仅在人工维护种子资源层面给出条目，全部标注 `> 待核实`，请勿将其视为本轮实时检索结论。
6. **选型建议（简述）**：算法研究优先 ManiSkill3 生态（并行 + 渲染 + 已有基准沉淀）[30]；需要视频生成式动力学做策略评估/数据增强时，把 Ctrl-World [11]、Genie Envisioner [9]、Gemini+Veo [10] 视为**探索性**选项，必须自建物理一致性与分布外回归测试 [10][14]；接触密集/颗粒介质任务关注可微物理路线 [25][27]；触觉相关任务关注 Isaac Sim + TacEx [3][6]。

---

## 一、关键前沿进展（近 1–2 年，2024-10 至 2026-10）

### 1.1 前沿条目总览

| 名称 | 年份 | 机构/作者线索 | 热度证据 | 权威证据 | 关注度 | 推荐度 |
|---|---|---|---|---|---|---|
| Motus: A Unified Latent Action World Model [20] | 2025 | `> 待核实` | citations=270 [20] | arXiv 预印本（cs.RO），非同行评审 [20] | 高（citations=270，本轮热度第二）[20] | ★★★★★ 统一隐动作世界模型，直击世界模型与策略割裂问题 [20] |
| Ctrl-World: A Controllable Generative World Model for Robot Manipulation [11] | 2025 | 作者含 Chelsea Finn 等 [11] | citations=163 [11] | arXiv 预印本（cs.RO），非同行评审 [11] | 高（citations=163，且为本主题最对题条目之一）[11] | ★★★★★ 可控生成式世界模型用于操作，直接支撑决策可用性讨论 [11] |
| Genie Envisioner: A Unified World Foundation Platform [9] | 2025 | 作者含 Shuicheng Yan 等 [9] | citations=136 [9] | arXiv 预印本（cs.RO），非同行评审 [9] | 高（citations=136，统一世界基础平台为热点方向）[9] | ★★★★☆ 代表性统一范式，但可控性与可复现性待独立验证 [9] |
| Evaluating Gemini Robotics Policies in a Veo World Simulator [10] | 2025 | Gemini Robotics Team [10] | citations=55 [10] | arXiv 预印本；官方技术报告性质，非同行评审 [10] | 高（citations=55，一线机器人团队背书）[10] | ★★★★☆ 直击分布外策略评测可信度，但为官方自评 [10] |
| WoW: Towards a World omniscient World model Through Embodied Interaction [15] | 2025 | `> 待核实` | citations=62 [15] | arXiv 预印本（cs.RO），非同行评审 [15] | 中高（citations=62，涉及物理因果争议）[15] | ★★★★☆ 提出物理直觉须来自具身交互，观点性强 [15] |
| PAN: A World Model for General, Actionable, and Long-Horizon World Simulation [12] | 2025 | `> 待核实` | citations=36 [12] | arXiv 预印本，非同行评审 [12] | 中（citations=36，方向性论述）[12] | ★★★☆☆ 适合作为开放问题线索，实验细节在本轮证据中缺失 [12] |
| MinD: Learning A Dual-System World Model for Real-Time Planning and Implicit Risk Analysis [21] | 2025 | `> 待核实` | citations=11 [21] | `> 待核实`（候选块 authority 字段为空）[21] | 中（citations=11）[21] | ★★★☆☆ 双系统世界模型用于实时规划与隐式风险分析，热度尚低 [21] |
| Generative World Modelling for Humanoids: 1X World Model Challenge Technical Report [17] | 2025 | 1X（挑战赛官方技术报告）[17] | citations=8 [17] | arXiv 预印本，官方技术报告，非同行评审 [17] | 中（citations=8，但为人形真机开源基准，赛道稀缺）[17] | ★★★★☆ 稀缺的人形真机世界模型基准，值得跟进 [17] |
| ManiSkill3: GPU Parallelized Robotics Simulation and Rendering [30] | 2024 | haosulab（项目主页线索）[30] | citations=344 [30] | arXiv 预印本，非同行评审 [30] | 高（citations=344，本轮仿真类最高）[30] | ★★★★★ 可计算扩展的并行仿真与渲染，工程落地首选之一 [30] |
| Benchmarking Massively Parallelized Multi-Task RL for Robotics Tasks [26] | 2025 | `> 待核实` | citations=13 [26] | arXiv 预印本，非同行评审 [26] | 中（citations=13）[26] | ★★★★☆ 为"并行训练是否真提升多任务泛化"提供对照评测 [26] |
| MobileManiBench: Simplifying Model Verification for Mobile Manipulation [7] | 2026 | `> 待核实` | citations=1 [7] | arXiv 预印本，非同行评审 [7] | 低（citations=1，发布时间新）[7] | ★★★★☆ 提出"仿真优先"的 VLA 验证流程，实用性导向 [7] |
| HumanoidVLN: Physics-Grounded Simulator and Benchmark [5] | 2026 | `> 待核实` | citations=0 [5] | `> 待核实`（候选块 authority 字段为空）[5] | 低（citations=0，刚发布）[5] | ★★★☆☆ 人形 VLN 物理落地仿真与基准，方向稀缺但尚无引用 [5] |

> **阅读提示**：上表"推荐度"综合权威 + 热度 + 与本主题相关性；Motus [20]、Ctrl-World [11] 的候选块 confidence 标为 low，其高推荐度**仅源于热度与主题契合度**，不代表结论已被验证。

### 1.2 值得单独说明的三条主线

- **主线 A：统一化（unified）**。Motus 的出发点是"当前方法由理解、世界建模、控制三类孤立模型拼装，阻碍了从大规模异构数据学习" [20]；Genie Envisioner 的 GE-Base 是 instruction-conditioned 大规模视频扩散模型，在结构化隐空间中捕捉真实机器人交互的空间、时间与语义动态，GE-Act 通过轻量 flow-matching 解码器把隐表示映射为可执行动作轨迹，支持多样本体的策略推理 [9]。
- **主线 B：可控化（controllable）**。Ctrl-World 明确指出挑战在于构建能处理与通用机器人策略多步交互的可控世界模型 [11]；MinD 则报告视频生成模型（VGM）已成为 VLA 骨干，但**未充分利用其分布建模能力预测未来状态**，并提出双系统世界模型用于实时规划与隐式风险分析 [21]。
- **主线 C：评测化（evaluatable）**。Gemini Robotics 报告称视频模型在机器人中的使用**长期主要局限于分布内评测**（与策略训练或基础视频模型微调场景相似），并声称可展示覆盖整个谱系的策略评估用例 [10]；1X 挑战赛提供两条互补赛道（含 sampling）的人形真机交互开源基准 [17]。

---

## 二、生成式 / 视频世界模型

### 2.1 能力边界：可控性、物理一致性、长时程

- **可控性是决策可用性的前提**：世界模型需兼容现代通用策略，并支持多视角预测、细粒度动作控制与长时程一致交互；同时，严格评测需大量真机 rollout，系统性改进需带专家标签的纠正数据，二者都"慢、贵、难扩展" [11]。
- **视觉真实 ≠ 物理一致**：T2VPhysBench 指出文本到视频生成模型在美学吸引力与指令跟随上进步显著，但尊重基本物理定律的能力仍"largely untested"，许多输出仍违反基本物理规律，故提出 first-principles 基准 [14]。这是把"视频好看"与"物理可用"解耦的关键证据。热度：citations=39 [14]；权威：arXiv 预印本，非同行评审，自称 first-principles benchmark [14]；关注度：中 [14]；推荐度：★★★★☆（直接对应本主题的边界问题）[14]。
- **物理直觉的来源存在争议**：WoW 以"人类通过主动交互形成直觉物理理解"为出发点，对比 Sora 等依赖被动观察、因此"struggle with grasping physical causality"的视频模型，中心假设是真实物理直觉必须 grounded 于 extensive、causally rich 的交互 [15]。热度：citations=62 [15]；权威：arXiv 预印本（cs.RO），非同行评审 [15]；关注度：中高 [15]；推荐度：★★★★☆（争议性观点，需独立验证）[15]。

### 2.2 生成式评测本身也是一个子问题

VideoScore2 定位为"在生成式视频评测中先思考再打分"的方法 [13]。本轮证据仅含标题级信息，未获取摘要与实验细节 `> 待核实` [13]。同一类需求也出现在气候降尺度场景中对生成模型"地理泛化与物理一致性"的评估上 [16]，其方法论可作跨域借鉴，但对具身场景的直接适用性 `> 待核实` [16]。

### 2.3 综述层面

- [18] 是生成式 AI 的近期进展、模型变体与真实应用综述，发表于 *Journal of Big Data*，citations=31；权威：期刊（同行评审），关注度：中；推荐度：★★★★☆（用于补 GAN/VAE/扩散谱系背景）[18]。注意其主题为通用生成式 AI，**并非机器人世界模型专论** [18]。
- [22] 题为 *Generative Physical AI in Vision: A Survey*，标题层面属于"视觉生成式物理 AI"综述，与本章高度相关，但本轮未获取其内容，全文结论 `> 待核实` [22]。
- [19] 题为 *Object-Centric World Model for Language-Guided Manipulation*，标题层面指向语言引导操作的对象中心世界模型，内容与实验口径 `> 待核实` [19]。

---

## 三、神经仿真与可微物理

### 3.1 GPU 并行仿真与渲染

- **ManiSkill3**（2024）是本轮仿真类热度最高条目：摘要指出既有仿真框架通常只支持窄范围场景/任务，且缺乏扩展通用机器人与 sim2real 所需的关键特性，ManiSkill3 即为补足这些缺口而开源 [30]。热度：citations=344 [30]；权威：arXiv 预印本，非同行评审 [30]；关注度：高 [30]；推荐度：★★★★★（可作为并行仿真与渲染的主力工程栈）[30]。
- **并行多任务 RL 的系统评测**：[26] 面向"大规模并行训练"在多任务 RL 中的实际收益给出基准，摘要指出多任务 RL 是复杂真实机器人任务的关键训练范式，对策略的泛化性与鲁棒性提出要求 [26]。热度：citations=13 [26]；权威：arXiv 预印本 [26]；关注度：中 [26]；推荐度：★★★★☆ [26]。
- **训练效率**：[23] 讨论 GPU 并行机器人仿真下的操作任务训练提速，发表在 *International Journal of Software Science and Computational Intelligence* [23]。热度：citations=1 [23]；权威：期刊（同行评审，但非机器人顶刊/顶会）[23]；关注度：低 [23]；推荐度：★★★★☆（作为训练加速的工程参考，结论外推需谨慎）[23]。
- **采样优化 + 并行物理**：[24] 将采样式优化与并行化物理仿真器结合用于双臂操作，指出端到端学习方法在新场景泛化上存在关键限制 [24]。热度：citations=1 [24]；权威：arXiv 预印本 [24]；关注度：低 [24]；推荐度：★★★★☆（对"放弃纯端到端、回到优化"的路线有参考价值）[24]。

### 3.2 可微物理

- **Differentiable Particle Optimization**（ICRA）面向快速序列操作：指出在高维构型空间中、跨多物体交互求满足几何约束的无碰撞轨迹，因算力限制长期难以实时、大规模求解 [25]。热度：citations=4 [25]；权威：IEEE ICRA（同行评审，等级 A）[25]；关注度：低（引用尚少）但 venue 权威 [25]；推荐度：★★★★☆（可微/优化路线中本主题内可信度最高的 venue 之一）[25]。
- **DDBot**：面向未知颗粒介质的可微物理挖掘机器人，指出颗粒材料操作因接触动力学复杂、材料属性不可预测而难以自动化，既有方法在效率与精度上均不足 [27]。热度：citations=3 [27]；权威：*IEEE Transactions on Robotics*（同行评审，领域顶级期刊）[27]；关注度：低（引用数少）但 venue 权威 [27]；推荐度：★★★★☆（颗粒/接触密集场景的少见可微方案）[27]。
- **可微仿真在具身主流任务上是否已替代域随机化**：本轮**无证据支持**该判断 `> 待核实`。

### 3.3 触觉与多物理场扩展

- **TacEx** 在 Isaac Sim 中组合软体与视触觉仿真器，用于 GelSight 类触觉传感器仿真 [3]。热度：候选块未给出 citations `> 待核实`；权威：arXiv 预印本 [3]；关注度：`> 待核实`；推荐度：★★★★☆（触觉 sim2real 的工程入口）[3]。
- [6] 为 GelSight 触觉传感器仿真用于强化学习的 Semantic Scholar 条目 [6]。热度/权威：`> 待核实`（仅有聚合站链接）[6]；关注度：`> 待核实`；推荐度：★★★☆☆（线索级，需回溯一手论文）[6]。

### 3.4 安全约束与并行 RL 融合

[4]（2026）指出 Isaac Lab 提供大规模并行 UAV 仿真、OmniSafe 与 safe-control-gym 提供受限 RL 基准、CBFKit 提供控制屏障函数合成工具，但**尚无框架把三者统一到端到端安全约束训练**，ParallelCBF 因此提出可组合安全过滤器与可审计性框架 [4]。热度：citations=0 [4]；权威：arXiv 预印本（2026）[4]；关注度：低（新发布）[4]；推荐度：★★★★☆（安全过滤 + 张量并行训练的组合，工程价值明确）[4]。

### 3.5 引擎横向对比：本轮证据不足

关于 **MuJoCo / MJX、Genesis、Isaac Sim / Isaac Lab、Brax、NVIDIA Warp、DiffTaichi** 在性能、GPU 并行、可微性与生态成熟度上的定量对比，本轮检索**未返回可核验的一手基准数据**（无第三方 benchmark 表、无统一硬件口径的吞吐量对比）。

> 待核实：上述引擎的吞吐量、可微支持范围、GPU 并行规模与生态成熟度排序。建议后续以各引擎官方文档 / 仓库 README 与独立基准论文为一级证据重新检索后补齐。
> 已知可用锚点：Isaac Lab 被 [4] 描述为提供"massive parallel UAV simulation" [4]；ManiSkill3 提供 GPU 并行仿真与渲染 [30]。

---

## 四、sim2real 迁移与方法

> **重要缺口声明**：本报告 q5（sim2real 与可微仿真方法进展）在本轮检索中**未产出任何结构化发现**。以下内容仅由 q3/q4 的边缘证据与人工种子资源拼合，**不构成对域随机化、系统辨识、real-to-sim-to-real 系统性对比的完整回答**。

### 4.1 有证据支撑的片段

- **仿真到真机复现难是共性问题**：[2] 指出四足移动操作平台的全身控制 RL 虽具潜力，但

## 参考来源

[1] RoboRAN: A Unified Robotics Framework for Reinforcement Learning-Based Autonomous Navigation — https://arxiv.org/abs/2505.14526
[2] A Framework for Deploying Learning-based Quadruped Loco-Manipulation — https://arxiv.org/abs/2512.18938
[3] TacEx: GelSight Tactile Simulation in Isaac Sim - Combining Soft-Body and Visuotactile Simulators — https://arxiv.org/abs/2411.04776
[4] parallelcbf: A composable safety-filter and auditability framework for tensor-parallel reinforcement learning — https://arxiv.org/abs/2605.15509
[5] HumanoidVLN: A Physics-Grounded Simulator and Benchmark for Vision-Language Navigation Across Diverse Humanoid Embodiments — https://arxiv.org/abs/2608.12860
[6] Simulation of GelSight Tactile Sensors for Reinforcement Learning — https://www.semanticscholar.org/paper/ff52becfdfcfeff6417232ecd286a4895a41cf05
[7] MobileManiBench: Simplifying Model Verification for Mobile Manipulation — https://arxiv.org/abs/2602.05233
[8] KlaskTron: An Open-Source Platform for Physical Adversarial Multi-Agent RL — https://doi.org/10.15607/rss.2026.xxii.038
[9] Genie Envisioner: A Unified World Foundation Platform for Robotic Manipulation — https://arxiv.org/abs/2508.05635
[10] Evaluating Gemini Robotics Policies in a Veo World Simulator — https://arxiv.org/abs/2512.10675
[11] Ctrl-World: A Controllable Generative World Model for Robot Manipulation — https://arxiv.org/abs/2510.10125
[12] PAN: A World Model for General, Actionable, and Long-Horizon World Simulation — https://arxiv.org/abs/2511.09057
[13] VideoScore2: Think before You Score in Generative Video Evaluation — https://arxiv.org/abs/2509.22799
[14] T2VPhysBench: A First-Principles Benchmark for Physical Consistency in Text-to-Video Generation — https://arxiv.org/abs/2505.00337
[15] WoW: Towards a World omniscient World model Through Embodied Interaction — https://arxiv.org/abs/2509.22642
[16] Assessing the Geographic Generalization and Physical Consistency of Generative Models for Climate Downscaling — https://arxiv.org/abs/2510.13722
[17] Generative World Modelling for Humanoids: 1X World Model Challenge Technical Report — https://arxiv.org/abs/2510.07092
[18] Generative AI in depth: A survey of recent advances, model variants, and real-world applications — https://arxiv.org/abs/2510.21887
[19] Object-Centric World Model for Language-Guided Manipulation — https://arxiv.org/abs/2503.06170
[20] Motus: A Unified Latent Action World Model — https://arxiv.org/abs/2512.13030
[21] MinD: Learning A Dual-System World Model for Real-Time Planning and Implicit Risk Analysis — https://arxiv.org/abs/2506.18897
[22] Generative Physical AI in Vision: A Survey — https://arxiv.org/abs/2501.10928
[23] Faster Training for Robotic Manipulation in GPU Parallelized Robotics Simulation — https://doi.org/10.4018/ijssci.374216
[24] Sampling-Based Optimization with Parallelized Physics Simulator for Bimanual Manipulation — https://arxiv.org/abs/2511.21264
[25] Differentiable Particle Optimization for Fast Sequential Manipulation — https://arxiv.org/abs/2510.07674
[26] Benchmarking Massively Parallelized Multi-Task Reinforcement Learning for Robotics Tasks — https://arxiv.org/abs/2507.23172
[27] DDBot: Differentiable Physics-Based Digging Robot for Unknown Granular Materials — https://arxiv.org/abs/2510.17335
[28] GenPO: Generative Diffusion Models Meet On-Policy Reinforcement Learning — https://arxiv.org/abs/2505.18763
[29] GraspMixer: Hybrid of Contact Surface Sampling and Grasp Feature Mixing for Grasp Synthesis — https://doi.org/10.1109/TASE.2025.3530795
[30] ManiSkill3: GPU Parallelized Robotics Simulation and Rendering for Generalizable Embodied AI — https://arxiv.org/abs/2410.00425


---

*Generated by research-bot · topic=`embodied-world-models` · depth=`standard` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading · model=`deepseek-v4-flash` · sources=30 · duration=1412s · 2026-10-04T03:59:59+00:00*
