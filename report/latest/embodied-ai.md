# 具身智能（Embodied AI）方法演进、仿真平台、Sim2Real 与评测基准调研报告

**日期**：2026-10-02（UTC） | **领域**：具身智能 / VLA / 机器人学习 / 仿真与 Sim2Real | **检索源规模**：可引用来源 36 条（[1]–[36]），其中与具身智能或机器人直接相关 21 条，远领域或检索噪声 15 条；结构化发现覆盖 3 个子问题（q1 方法变化、q2 经典脉络、q3 开源工程）；另有人工维护种子资源 12 条（无编号，仅保留原始链接）

**证据基础声明（务必先读）**：本次调研的候选证据存在结构性缺口。VLA 方向有可核查的会议论文与引用计数；但**世界模型驱动规划、人形全身控制、Sim2Real 迁移、主流仿真框架横向对比、数据集与榜单**五个维度，在本次候选证据中**几乎没有一手材料**。因此本报告在这五个维度上以"线索 + 待核实"方式呈现，不作强结论。所有引用计数均为 Crossref cited-by 口径，与 Google Scholar 口径不可直接比较。

---

## 摘要（Executive Summary）

1. **VLA 的边界正在从桌面机械臂向腿足式移动本体扩展**，这是一个可以核查的、有明确出处与引用计数的一手证据：NaVILA 发表于 RSS 2025（Robotics: Science and Systems XXI，2025-06-21），标题明确为面向 legged robot 导航的 Vision-Language-Action 模型，Crossref 引用计数 54，是本批候选中影响力最高的相关工作 [8]。

2. **"VLM 作为高层规划器"仍是一条独立且活跃的路线**，与端到端 VLA 并行演进：IROS 2025 收录的 *VLM See, Robot Do* 以 Vision Language Model 将人类示范视频转换为机器人动作计划（human demo video → robot action plan），Crossrent 引用计数 14 [3]。

3. **模仿学习是具身智能方法谱系中证据链最完整的一段**，且呈现 "2007 早期技能模仿 → 2023 扩散策略 → 2025 灵巧操作交互式模仿学习综述" 的清晰演进：早期人形机器人手势增量模仿工作引用计数 227 [16]，Diffusion Policy（RSS 2023）引用计数 556 [23]，其官方仓库 real-stanford/diffusion_policy 获得 4601 stars 并提供状态与视觉环境的自包含 Colab notebook [22]，2025 年 Frontiers in Robotics and AI 综述则聚焦灵巧操作的交互式模仿学习并指出传统强化学习路径的局限 [14]。

4. **"开源 VLA 模型"已成为一个独立议题，具备可被第三方独立复测的雏形**：存在专门的期刊论文 *Open-source vision-language-action models for robotics*（JMST Advances, 2025-07-24）作为入口文献 [30]；2026 年 SIU 会议论文以 OpenVLA 为对象评测土耳其语指令理解，说明开源权重使第三方再评估成为可能 [26]。但两条证据本次仅获取到题录，**无摘要与实验指标**。

5. **三大核心缺口（本报告的主要限制）**：
   - **世界模型线**：候选证据中无任何视频生成 / 潜在动力学 / model-based 规划相关工作，种子清单中的 *Learning to Act without Actions* 链接（arXiv 2312.10807）本次未检索验证，`> 待核实`。
   - **人形全身控制线**：仅有一条中文期刊线索——*Gait Switching Method for Humanoid Robot Integrating Vision-language Model and Proximal Policy Optimization Algorithm*（《机械工程学报》2025 年第 21 期）[1]，仅有标题级证据，无摘要、无实验口径，`> 待核实`。
   - **仿真平台与 Sim2Real**：候选证据中 Isaac Lab、MuJoCo MJX、ManiSkill、Genesis、LeRobot、octo、RoboVerse **零条目**；仅有 Isaac Lab/Isaac Sim 的三条外围线索 [33][34][35]，无法支撑"可复现性 vs 硬件门槛"的横向对比。

> 一句话结论：**本批证据足以支撑"VLA 向腿足扩展 + VLM 规划分离路线 + 模仿学习脉络"三条结论；不足以支撑世界模型、人形全身控制、仿真平台对比、Sim2Real、评测榜单的任一强结论。**

---

## 一、关键前沿进展（近 1–2 年，2024–2026）

### 1.1 时间线节点

| 时间 | 节点 | 类型 | 证据强度 | 来源 |
|---|---|---|---|---|
| 2025-06-21 | NaVILA：腿足机器人导航 VLA 模型，RSS 2025 收录，citations=54 | 会议论文 | 强（A/B 级，含出处与引用） | [8] |
| 2025-07-24 | *Open-source vision-language-action models for robotics*，JMST Advances 刊出 | 期刊论文（仅题录） | 弱（E 级内容缺失） | [30] |
| 2025-10-19 | *VLM See, Robot Do*：人类示范视频 → 机器人动作计划，IROS 2025 收录，citations=14 | 会议论文 | 中 | [3] |
| 2025-12-19 | 灵巧操作交互式模仿学习综述（Frontiers in Robotics and AI），citations=7 | 期刊综述 | 中 | [14] |
| 2025（月份待核实） | 人形机器人 VLM + PPO 步态切换方法，《机械工程学报》2025(21):204 | 中文期刊论文（仅题录） | 弱（标题级线索） | [1] |
| 2025-08（arXiv v2） | *Robotic Manipulation via Imitation Learning: Taxonomy, Evolution…* 预印本 | arXiv 预印本 | 中 | [21][24] |
| 2026-05-21 | VLA 基础模型在开源机械臂上的微调与部署，ICHORA 2026，citations=0 | 会议论文 | 弱 | [2] |
| 2026（会议年份） | OpenVLA 土耳其语指令理解第三方评测，SIU 2026 | 会议论文（仅题录） | 弱 | [26] |

### 1.2 分线叙述

**（A）VLA 向移动 / 腿足本体扩展——本批证据中最坚实的一条。** NaVILA 是 RSS 2025 同行评审论文，DOI 明确（10.15607/rss.2025.xxi.018），Crossref 引用计数 54，在本次全部候选中最高 [8]。其意义在于：VLA 范式不再局限于固定基座机械臂的操作任务，而开始处理 legged robot 的导航这一强空间推理任务。这是"具身"属性增强的直接标志。

> 待核实：NaVILA 的任务数量、评测环境（仿真/真机）、本体型号、第三方复现情况，本批证据均未提供。

**（B）VLM 作为高层规划器：与端到端 VLA 并行的一条独立路线。** *VLM See, Robot Do* 被 IROS 2025 收录，核心设定是"用 VLM 把人类示范视频转成机器人动作计划" [3]。这与端到端 VLA（直接输出动作）构成方法论上的对立：前者把 VLM 放在规划层、把可执行性交给下游，后者把语言-视觉-动作压进单一策略网络。两条路线在 2025 年同时存在并被会议接收，说明**"VLM 规划 + 技能执行"与"端到端 VLA"的分野尚未收敛**。

**（C）人形本体与 VLA / RL 的结合：仅有标题级线索。** [1] 的标题同时包含 "Humanoid Robot"、"Vision-language Model"、"Proximal Policy Optimization"，指向"VLM 提供高层/语义信息 + PPO 负责底层步态"的混合架构，发表于《机械工程学报》2025 年第 21 期 [1]。

> 待核实：该文的具体架构（VLM 输出什么、PPO 优化什么奖励、是否真机）、任务口径、是否与 locomotion-manipulation 统一策略相关。仅有题录，不能作为"人形全身控制"线的结论性证据。

**（D）开源 VLA 的可复现性议题开始被专门讨论。** [30] 是本次唯一直接命中"机器人开源 VLA 模型"主题的期刊论文，可作为后续综述的骨架文献；[26] 用 OpenVLA 做非英语指令理解评测，是"开源权重 → 第三方可复测"的一个弱例证。但两者本次均只有题录。

**（E）仿真基础设施：只有外围线索。** [33] 标题为 *Accelerate Robot Learning With NVIDIA Isaac Lab and Newton*（ACM 会议 DOI，年份待核实），[34][35] 为同一篇 *An Integrated Simulation Framework for Vision-Based Robotic Manipulation Using NVIDIA Isaac Sim* 的机构库版本。这三条只能证明"Isaac Lab / Isaac Sim 被作为论文对象讨论"，**不能支撑任何性能或可复现性比较**。

### 1.3 用"真前沿四问"评估本批进展

| 追问 | NaVILA [8] | VLM See, Robot Do [3] | 人形 VLM+PPO [1] |
|---|---|---|---|
| 是否多任务/多本体验证 | `> 待核实` | `> 待核实` | `> 待核实` |
| 是否开源（代码/数据/权重） | `> 待核实` | `> 待核实` | `> 待核实` |
| 提升归因（数据/架构/算力） | `> 待核实` | `> 待核实` | `> 待核实` |
| 是否有独立第三方评测 | `> 待核实` | `> 待核实` | `> 待核实` |

结论：本批证据只能判定**"发生了什么"（有无此工作、发表在哪、被引多少）**，无法判定**"是否是真前沿"**。这是本报告最重要的方法学限制。

---

## 二、方法谱系（模块化 / 端到端 / 基础模型 / 世界模型）

### 2.1 模块化与经典模仿学习阶段

本批证据中最早的工作可追溯至 2007 年：*Incremental learning of gestures by imitation in a humanoid robot*（ACM/IEEE HRI, 2007-03-10，citations=227）[16]；同一主题另有书章版本 *Learning of gestures by imitation in a humanoid robot*（Cambridge，DOI 10.1017/cbo9780511489808.012）[13]。

> 待核实：[13] 与 [16] 是否为同一研究的不同发表形式（会议版/书章版）。两者标题与主题高度重叠，需核对作者与年份后再决定是否合并引用。

**承上启下**：这一阶段的方法特征是"把示范拆成可增量学习的技能片段"，监督信号来自人类示范，学习对象是低维运动技能（手势），系统仍是"感知-学习-执行"的松散耦合结构，而非端到端可微策略。

后续拓展包括：生成对抗式模仿学习用于机器人操作（GAIL，IJCAI 2021）[17]；序列化物体操作任务中的统计模仿学习 [18]；面向约束操作的任务流形学习（Autonomous Robots，2017）[19]；以及单次示范（single-shot）操作任务模仿学习（IJCNN 2022）[20]。

**这一段的共同演化方向**：从"多次示范 + 增量技能"走向"少样本/单次示范 + 结构化任务表征"，即降低示范成本、提高泛化。2025 年 arXiv 预印本 *Robotic Manipulation via Imitation Learning: Taxonomy, Evolution…* 提供了这一脉络的分类学整理 [21][24]。

### 2.2 端到端策略学习阶段：Diffusion Policy 是关键节点

*Diffusion Policy: Visuomotor Policy Learning via Action Diffusion*（RSS XIX, 2023-07-10，citations=556）是本批证据中引用最高的单篇工作 [23]。其方法关键词是"用动作扩散（action diffusion）建模视运动策略"，即把生成式建模引入动作空间，以处理人类示范数据固有的多模态动作分布问题。

**承上启下**：相比 GAIL [17]、单次模仿 [20] 等前作，Diffusion Policy 的转变在于**把"策略"从判别式回归重构为条件生成问题**，从而在不引入对抗训练不稳定性的前提下表达多模态行为 [23]。它同时成为后续大量工作的对比基线。

工程侧证据：官方实现 real-stanford/diffusion_policy 获得 **4601 stars**（记录时间 2024-12-24），并提供基于状态与基于视觉环境的自包含 Colab notebook [22]。

> 待核实：stars 数为快照值，随时间为变量；该仓库的最近提交活跃度、支持的本体与数据集范围，本批证据未覆盖（stars 记录时间 2024-12-24，距报告日期已近两年，`> 待核实` 其当前维护状态）。
> 待核实：**ACT（Action Chunking Transformer）在本次候选证据中零条目**，不能将其纳入谱系叙述。

### 2.3 基础模型 / VLA 阶段

代表节点见 1.1 表。谱系上的关键转变是：策略的输入输出从"状态/图像 → 动作"扩展为"自然语言指令 + 视觉观测 → 动作序列或子任务计划"，并由此派生两条分支：

- **端到端 VLA**：单一模型直接输出动作，语言作为条件输入。腿足导航方向的代表是 NaVILA [8]。
- **VLM 规划 + 下游执行**：VLM 只负责把人类视频/语言转成任务计划，执行交给下游 [3]。

**承上启下**：相对于 Diffusion Policy 阶段"用生成模型解决动作多模态性"，基础模型阶段的新增变量是**跨任务/跨本体的语义泛化能力**——即用大规模视觉-语言预训练替代从零学习的任务表征。这一范式的"外溢"也可以从旁证看到：[5] 是一篇把"视觉-语言预训练 → 下游领域适配"范式迁移到医学图像理解的学位论文，说明该范式已成为通用模板，但**与机器人本体或动作生成无直接关系，不计入具身智能方法结论** [5]。

同类外溢还包括植物病害识别 [6]、临床肿瘤学 [7] 等视觉-语言基础模型应用，同样属于远领域，仅作范式扩散的旁证。

### 2.4 世界模型路线

**本批候选证据中，世界模型（视频生成 / 潜在动力学 / model-based RL / 无动作策略学习）相关工作为零条目。** 种子资源清单提供了一条链接：

| 名称 | 年份 | 机构/作者 | 链接 | 说明 |
|---|---|---|---|---|
| Learning to Act without Actions（种子清单标注为 UniSim / world models line） | 2023 | 种子清单标注 "Various" | https://arxiv.org/abs/2312.10807 | **种子资源，本次未实时检索验证**；其与 UniSim 的准确关系、是否属世界模型路线，`> 待核实` |

> 待核实：世界模型驱动的规划是否为 2024–2026 年的活跃主线、代表工作、时间线节点，**本次调研无证据支撑，不作任何断言**。这是本报告最大的一处结构性空白。

---

## 三、仿真平台与基准对比

### 3.1 本次可用的（有限）证据

| 平台 | 定位（依证据描述） | 证据来源 | 可复现性 / 硬件门槛 | 来源 |
|---|---|---|---|---|
| NVIDIA Isaac Lab（+ Newton） | GPU 加速机器人学习框架，被论文标题描述为"加速机器人学习" | ACM 会议论文（年份待核实） | `> 待核实`（未获取正文，无法给出 GPU/显存门槛） | [33] |
| NVIDIA Isaac Sim | 用于视觉机器人操作的集成仿真框架（同一工作有两个机构库版本） | 机构库 DOI，年份待核实 | `> 待核实` | [34][35] |

### 3.2 种子资源清单中的平台（本次未实时检索验证）

| 平台 | 链接 | 说明 |
|---|---|---|
| Genesis | https://github.com/Genesis-Embodied-AI/Genesis | 种子清单标注为"生成式物理仿真引擎"；`> 待核实`（未验证其当前能力与路线声明） |
| Isaac Lab | https://github.com/isaac-sim/IsaacLab | 种子清单标注为"GPU 并行机器人学习框架" |
| ManiSkill | https://github.com/haosulab/ManiSkill | 种子清单标注为"GPU 并行操作基准" |
| BEHAVIOR-1K / OmniGibson | https://github.com/StanfordVL/BEHAVIOR-1K | 种子清单标注为"BEHAVIOR 基准与 OmniGibson" |

### 3.3 明确的对比缺口

本报告**无法**给出 Isaac Lab / MuJoCo MJX / ManiSkill / Genesis 在以下维度的比较：并行规模、渲染保真度与可微性、本体与资产生态、安装与硬件门槛、真机部署链路。

原因（可核查）：q3 的结构化发现明确指出，上述项目名在候选证据中**均无任何条目**，且多条候选证据正文抓取为空或返回反爬页面，无法进行证据分级 [26][30]。

> 待核实：MuJoCo MJX 在本次候选证据中零条目，连题录级证据都没有。

---

## 四、经典与奠基性工作

> 说明：下表中标注"种子资源"的行来自人工维护清单，**本次未实时检索验证其链接可达性与元数据**，因此不分配引用编号。标注编号的行来自本次可引用的证据来源。

| 名称 | 年份 | 机构/作者 | 链接 | 说明 |
|---|---|---|---|---|
| SayCan: Do As I Can, Not As I Say（种子资源） | 2022 | Google | https://arxiv.org/abs/2204.01691 | LLM 规划 + 可行技能 grounding 的奠基工作 `> 待核实` |
| Code as Policies（种子资源） | 2022 | Google | https://arxiv.org/abs/2209.07753 | LLM 生成机器人策略代码 `> 待核实` |
| PaLM-E: An Embodied Multimodal Language Model（种子资源） | 2023 | Google | https://arxiv.org/abs/2303.03378 | 具身多模态 LLM 奠基 `> 待核实` |
| Learning to Act without Actions（种子资源） | 2023 | 种子清单标注 Various | https

## 参考来源

[1] Gait Switching Method for Humanoid Robot Integrating Vision-language Model and Proximal Policy Optimization Algorithm — https://doi.org/10.3901/jme.2025.21.204
[2] Fine-Tuning and Deployment of a Vision-Language-Action Based Robotic Foundation Model for Open-Source Robot Arms — https://doi.org/10.1109/ichora69329.2026.11537253
[3] VLM See, Robot Do: Human Demo Video to Robot Action Plan via Vision Language Model — https://doi.org/10.1109/iros60139.2025.11246682
[4] Bayesian Uncertainty for Bias Discovery and Mitigation in Vision-Language Foundation Model on CLIP/LLaVA — https://doi.org/10.2139/ssrn.5668211
[5] Foundation Model Adaptation: From Vision-Language Pretraining to Medical Image Understanding — https://doi.org/10.14711/thesis-hdl172499
[6] A Vision-Language Foundation Model for Leaf Disease Identification — https://doi.org/10.36227/techrxiv.174062971.11176782/v1
[7] A vision–language foundation model for clinical oncology — https://doi.org/10.1038/s43018-025-00923-4
[8] NaVILA: Legged Robot Vision-Language-Action Model for Navigation — https://doi.org/10.15607/rss.2025.xxi.018
[9] A Study of the decay pi0 ---&amp;gt; e+ e- e+ e- using K(L) ---&amp;gt; pi0 pi0 pi0 decays in flight — https://doi.org/10.2172/1419196
[10] Study of the Rare Decay B0 to pi0 pi0 at BaBar — https://doi.org/10.2172/815293
[11] MEASUREMENTS OF BRANCHING FRACTIONS AND DIRECT CP ASYMMETRIES IN PI+ PI0, K+ PI0 AND K0 PI0 B DECAYS — https://doi.org/10.2172/799955
[12] Branching Fraction Limits for B0 Decays to eta' eta, eta' pi0 and eta pi0 — https://doi.org/10.2172/877199
[13] Learning of gestures by imitation in a humanoid robot — https://doi.org/10.1017/cbo9780511489808.012
[14] Interactive imitation learning for dexterous robotic manipulation: challenges and perspectives—a survey — https://doi.org/10.3389/frobt.2025.1682437
[15] Session details: Learning, adaptation and imitation in HRI — https://doi.org/10.1145/3245502
[16] Incremental learning of gestures by imitation in a humanoid robot — https://doi.org/10.1145/1228716.1228751
[17] Robot Manipulation Learning Using Generative Adversarial Imitation Learning — https://doi.org/10.24963/ijcai.2021/678
[18] Statistical Imitation Learning in Sequential Object Manipulation Tasks — https://doi.org/10.5772/9662
[19] Learning task manifolds for constrained object manipulation — https://doi.org/10.1007/s10514-017-9643-z
[20] Robot learning by Single Shot Imitation for Manipulation Tasks — https://doi.org/10.1109/ijcnn55064.2022.9892529
[21] Robotic Manipulation via Imitation Learning: Taxonomy, Evolution ... — https://arxiv.org/html/2508.17449v2
[22] real-stanford/diffusion_policy — https://github.com/real-stanford/diffusion_policy
[23] Diffusion Policy: Visuomotor Policy Learning via Action Diffusion — https://doi.org/10.15607/rss.2023.xix.026
[24] [2508.17449] Robotic Manipulation via Imitation Learning: Taxonomy ... — https://arxiv.org/abs/2508.17449
[25] Predicting Stars on Open-Source GitHub Projects — https://doi.org/10.1109/stcr51658.2021.9588891
[26] Performance Analysis of Vision-Language-Action Models: Evaluating Turkish Command Understanding in OpenVLA — https://doi.org/10.1109/siu71813.2026.11636432
[27] HordeVision: An Open-Source Kazakh Vision-Language Model — https://doi.org/10.36227/techrxiv.176800904.47969417/v1
[28] The Impact of Large Language Models on Open-source Innovation: Evidence from GitHub Copilot — https://doi.org/10.2139/ssrn.4684662
[29] Support open source software as a GitHub sponsor — https://doi.org/10.53731/r8n4c91-97aq74v-ag6v9
[30] Open-source vision-language-action models for robotics — https://doi.org/10.1007/s42791-025-00108-1
[31] Support open source software as a GitHub sponsor — https://doi.org/10.53731/y79qt-zf894
[32] Ghqc: An R-based Open-Source Tool for Semi-Automated Quality Control on GitHub — https://doi.org/10.70534/qevr6966
[33] Accelerate Robot Learning With NVIDIA Isaac Lab and Newton — https://doi.org/10.1145/3799820.3812502
[34] An Integrated Simulation Framework for Vision-Based Robotic Manipulation Using NVIDIA Isaac Sim — https://doi.org/10.32920/32253717
[35] An Integrated Simulation Framework for Vision-Based Robotic Manipulation Using NVIDIA Isaac Sim — https://doi.org/10.32920/32253717.v1
[36] Figure 1: Architecture of an Nvidia GPU. — https://doi.org/10.7717/peerj-cs.185/fig-1


---

*Generated by research-bot · topic=`embodied-ai` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading · model=`deepseek-v4-flash` · sources=36 · duration=616s · 2026-10-02T10:04:34+00:00*
