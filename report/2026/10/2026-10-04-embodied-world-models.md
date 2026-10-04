# 具身智能·世界模型与仿真（World Models & Simulation）调研报告

> **日期**：2026-10-04（UTC）　**领域**：具身智能 / 世界模型 / 物理仿真 / Sim2Real　**检索源数量**：125 条候选（arXiv 为主，含 seed 项目与数据集主页）
> **方法说明**：本报告严格限定在所提供的引用池 [1]–[125] 内引用；结构化发现中混入了大量与本主题无关的检索噪声（如药物设计 [1][2][3]、短视频热度预测 [25]、GPU 图算法 [29][31]、CheckThat! 事实核查 [43][45] 等），已剔除。凡无法从检索证据核实的热度数字（引用数、star、下载量）一律标注 `> 待核实`，**不编造任何数字或榜单**。

---

## 摘要（Executive Summary）

- **生成式视频世界模型正从"能生成"转向"可用于控制与评测"**：GEM-4D [51] 针对视频世界模型"点轨迹不一致、缺乏物理接地"的问题提出几何增强；WorldGym [52] 直接把自回归、动作条件化视频模型当作策略评测环境；Genie Envisioner [56] 与 Cosmos 世界基础模型平台 [57][60] 则定位为机器人操作/物理 AI 的统一世界模型底座。**但这批工作多为 2025–2026 年的 arXiv 预印本，第三方复现与真机验证仍稀缺**，需要区分"论文宣称"与"独立验证"。
- **经典谱系清晰**：World Models（2018）[seed] → Dreamer 系列 / DreamerV3（Nature 2023）[seed] → 无重构潜在想象 [9] 与 latent action world model [4]，构成 latent world model 主线；MuJoCo（IROS 2012）[seed] 是 model-based control 的经典物理引擎。
- **神经/可微仿真与 GPU 并行引擎成为工程主流**：Isaac Gym [44] → Isaac Lab [41]、ManiSkill3 [108] 代表了 GPU 原生并行仿真 + 光真实渲染的路线；Genesis 等生成式物理引擎以开源项目形式存在 [seed]，但性能与精度声明 `> 待核实`。
- **sim2real 形成三条主线**：域随机化及其理论分析 [17][18][22]、系统辨识/数字孪生 [72][75]、以及在真实世界继续学习（real-world adaptation）[54][67]。迁移差距的具体数值在检索证据中缺失，`> 待核实`。
- **评测正在从"仿真 SOTA"转向"真机 + 鲁棒性 + 长程"**：RoboArena 做分布式真机评测 [125]、RoboDojo 做 sim-and-real 统一评测 [98]、H2RBench 做 real-to-sim 的 human-to-robot 迁移评测 [97]、LIBERO 系列扩展到视觉鲁棒性 [113]、paraphrase 鲁棒性 [114] 与安全 [117]。**仿真 SOTA 与真机 SOTA 的错位是被明确指出的结构性问题** [15]。
- **开放问题聚焦**：世界模型的误差累积被重新解释为"运动学想象而非动力学想象" [88]；长程规划与世界模型变量长度 rollout [93][95]；评测效度与可复现算力门槛 [15][65]。**争议点**：demo 视频能否作为证据、生成式世界模型是否真正"理解物理" [53]。

---

## 一、关键前沿进展（近 1–2 年）

> 本节只列 2025–2026 年（含少量 2024 末）证据，先分"最新"，第 6 节再列"经典"。所有条目均标注四类证据轴；由于检索结果未提供引用数/star，热度数字多为 `> 待核实`。

### 1.1 世界模型作为"环境/评测器"

- **WorldGym（2025，cs.RO）** [52]：把自回归、动作条件化视频生成模型封装成策略评测环境，用于替代昂贵真机与手工仿真器。"世界模型即评测环境"是 2025 年一个显著新范式。
  - 热度：`> 待核实`（无 citations 字段）｜权威：arXiv 预印本（cs.RO），未见同行评审 [52]｜关注度：中（主题新颖，但 `> 待核实`）｜推荐度：★★★★☆（直接回答"世界模型能否替代仿真评测"）。
- **Robot Policy Evaluation for Sim-to-Real Transfer: A Benchmarking Perspective（2025，cs.RO）** [15]：明确讨论现有视觉机器人仿真基准"在通用策略的真机评测上滞后"，是可引用的"评测效度"论点来源。
  - 权威：arXiv 预印本 [15]｜关注度：中｜推荐度：★★★★☆。

### 1.2 几何接地的视频世界模型

- **GEM-4D: Geometry-Enhanced Video World Models for Robot Manipulation（2026，cs.CV）** [51]：指出视频世界模型"能生成合理未来，却无法在时间上一致追踪同一物理点"，从而缺乏可靠动作执行所需的物理接地；以几何增强弥补。
  - 权威：arXiv 预印本（cs.CV）[51]｜关注度：中（`> 待核实`）｜推荐度：★★★★★（直面"视频逼真 ≠ 物理可用"的核心矛盾）。
- **Cosmos-Transfer1（2025）** [60]：条件化世界生成，带自适应多模态控制，用于可控的场景/域生成。

### 1.3 世界模型 × VLA / 策略

- **ForeTime-VLA（2026）** [63]：从 world-action model 做因果未来 token 蒸馏，面向传送带操作。属"world model 作为策略训练信号"的路线。
- **DECOWAM（2026）** [62]：解耦的 whole-body world-action model，面向腿足移动操作。
- **Direct Experience World-Model Optimization（2026）** [61]：提出"学习动作模仿之外的世界"，把世界模型优化与直接经验结合。
- **Communicating Plans, Not Percepts（2025）** [106]：用具身世界模型做可扩展多智能体协调，通信内容从"感知"转向"计划"。

### 1.4 真机继续学习与 sim2real 闭环

- **Robot Trains Robot（2025，cs.RO）** [54]：面向人形的自动真机策略自适应与学习，绕开"仿真 RL 到真机迁移困难"的瓶颈。
  - 权威：arXiv 预印本 [54]｜关注度：中高（人形 + 真机 RL 是热点）｜推荐度：★★★★☆。
- **Efficient Sim-to-Real Transfer of World-Action Models from Synthetic Priors（2026）** [16]：合成先验到真机的 world-action 迁移。

### 1.5 长程与失败诊断

- **Imagined Rollouts are Kinematic, Not Dynamic（2026）** [88]：把世界模型长程失败从"误差累积"泛化叙事，细化为"运动学想象 vs 动力学想象"的诊断框架。
- **Foresight（2026）** [95]、**Beyond the Next Step（2026）** [93]：分别用动作条件世界模型 latent 做长程操作失败检测、以及变长 latent world model 支撑长程规划。

> **本节点的证据强度提醒**：上述条目几乎全部为 2025–2026 arXiv 预印本，**缺少 CoRL/RSS/ICRA 同行评审确认与第三方复现**，应视为"刚发布、待验证"，而非"已被验证的 SOTA"。

---

## 二、生成式/视频世界模型

### 2.1 路线分化

| 路线 | 代表 | 关键点 | 引用 |
|---|---|---|---|
| 潜在动力学世界模型（latent dynamics） | Dreamer 系列、[9]、[4] | 在压缩隐空间做 rollout，用于 RL/规划 | `> 待核实`（[9][4] 之外无新证据） |
| 视频生成式世界模型 | GEM-4D、Cosmos、Genie Envisioner | 像素级/几何级未来生成，视觉逼真 | [51][57][56] |
| 世界模型作为策略评测器 | WorldGym | 用生成模型替代仿真/真机评测 | [52] |

### 2.2 "是否真的用于机器人规划/控制"的判断

- **明确声称用于控制/评测的**：WorldGym 作为策略评测环境 [52]；GEM-4D 面向机器人操作的动作执行接地 [51]；Genie Envisioner 定位为机器人操作的统一世界基础平台 [56]；ForeTime-VLA [63]、DECOWAM [62] 将世界模型接入策略。
- **偏"生成能力/条件控制"的**：Cosmos [57][60] 定位物理 AI 的通用世界模型平台，机器人控制为其下游之一。
- **综述性怀疑视角**：*Is Sora a World Simulator? A Comprehensive Survey on General World Models and Beyond* [53] 对"生成即世界模拟"提出系统性审视，适合作为批判性引用。
  - 权威：arXiv 综述 [53]｜关注度：高（Sora 话题性，`> 待核实`具体热度）｜推荐度：★★★★☆。

### 2.3 待核实项

- 各视频世界模型在**多本体、多任务**上的验证规模、是否开源权重、推理成本与真实控制成功率：检索证据未提供，`> 待核实`。

---

## 三、神经仿真与可微物理

> **证据警示**：本次结构化发现中，q3 项下的多数条目（[29][31][43][45]）与神经/可微仿真完全无关（GPU 图聚类、体覆盖、事实核查），属检索噪声。真正可用的证据仅有 [41][44][108] 及 seed 项目。因此本节**结论有限，多处标注待核实**。

- **GPU 并行仿真的范式确立**：Isaac Gym [44]（2021）确立 GPU-native 大规模并行 RL 范式；**Isaac Lab** [41]（2025）作为其继任者，把"GPU 并行物理 + 光真实渲染 + 模块化组合架构"扩展到大规模多模态学习。
  - 权威：arXiv 预印本 [41][44]，Isaac 系列由 NVIDIA 主导（官方框架）｜关注度：高（机器人学习社区事实标准之一）｜推荐度：★★★★★。
- **操作仿真与渲染并行**：**ManiSkill3** [108]（2024）主打 GPU 并行仿真与渲染，服务可泛化具身 AI。
- **生成式/可微物理引擎**：Genesis [seed] 以"生成式物理引擎"定位存在开源仓库；但**其宣称的物理精度、速度与可微性证据未在本次检索中出现，`> 待核实`**。
- **可微物理与神经仿真**：本次检索**未获得**可微物理引擎（如 Warp、Brax、DiffTaichi 类）的可核实一手来源，相关技术路线与性能对比 `> 待核实`。
- **浏览器/CPU 经典引擎**：MuJoCo [seed]（IROS 2012）仍是精度与接触建模的经典基准；MJX 等 GPU 移植的大规模对比证据 `> 待核实`。

---

## 四、sim2real 迁移与方法

### 4.1 三条方法主线

**(A) 域随机化（Domain Randomization）**
- *Understanding Domain Randomization for Sim-to-real Transfer* [17]：理论化理解域随机化的作用机制。
- *DROPO: Sim-to-Real Transfer with Offline Domain Randomization* [18]：用离线数据做域随机化参数估计。
- *Benchmarking Domain Randomisation for Visual Sim-to-Real Transfer* [22]：对视觉域随机化做基准对比。
  - 权威：均为 arXiv 预印本 [17][18][22]｜关注度：中（早期经典方法论，被持续引用）｜推荐度：★★★★☆。

**(B) 系统辨识 / 数字孪生（Digital Twin）**
- *A High-Fidelity Digital Twin for Robotic Manipulation Based on 3D Gaussian Splatting* [72]：3DGS 重建高保真可交互数字孪生，服务闭环运动规划与 sim2real。
- *MATTERIX* [75]：面向机器人辅助化学实验室自动化的数字孪生。
- 数字孪生平台化：DTaaS [71]、数字孪生降本 [73]、实时数字孪生研究方向 [76] 等构成外围支撑（与机器人操作直接相关性较弱）。
  - 权威：arXiv 预印本 [72][75]｜关注度：中高（3DGS + 数字孪生是 2025–2026 热点）｜推荐度：★★★★☆。

**(C) 真实世界继续学习（Real-world adaptation）**
- *Robot Trains Robot* [54]：人形真机自动策略自适应与学习。
- *Sim2Real with Vision Encoder Pre-Training* [64]：用仿真做视觉编码器预训练以缓解 sim2real 分布偏移。
- *Robot Manipulation with GPT-6-Astra* [67]：把身体知识、经验复用、可执行技能与 sim2real 结合。
  - 权威：arXiv 预印本 [54][64][67]｜关注度：中高｜推荐度：★★★★☆。

### 4.2 领域特化 sim2real

- 双足运动 [19]、光学触觉 [20]、音频-视觉导航 [68]、生成式音频辅助多模态 sim2real [96]、精密农业操作 [66]。
- 经典社区共识来源：**R:SS 2020 Sim2Real Workshop 总结** [65]，12 位领域学者就 sim2real 的定义、可行性与重要性进行辩论，是引用"sim2real 争议"的权威二手来源（workshop report）。

### 4.3 迁移差距的量化

- **本次检索未提供任何可核实的 sim2real 迁移差距数字（如成功率下降百分比）**。任何此类具体数字 `> 待核实`。这是本报告的一个明确证据缺口。
- 相关基准：H2RBench（real-to-sim 的 human-to-robot 迁移评测）[97]、RoboDojo（sim-and-real 统一评测）[98] 可作为后续量化迁移差距的工具。

---

## 五、仿真引擎与基准

### 5.1 仿真引擎

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| MuJoCo | 2012 | IROS | `> 待核实` | 同行评审（IROS）[seed] | 高 | ★★★★★ | https://ieeexplore.ieee.org/document/6386109 | 经典物理引擎，model-based control 基石 |
| Isaac Gym | 2021 | NVIDIA | `> 待核实` | arXiv 预印本 [44] | 高 | ★★★★★ | http://arxiv.org/abs/2108.10470v2 | GPU 并行仿真范式开创 |
| Isaac Lab | 2025 | NVIDIA | `> 待核实` | arXiv 预印本 [41] | 高 | ★★★★★ | http://arxiv.org/abs/2511.04831v1 | Isaac Gym 继任者，多模态学习框架 |
| ManiSkill3 | 2024 | 操作仿真社区 | `> 待核实` | arXiv 预印本 [108] | 高 | ★★★★★ | http://arxiv.org/abs/2410.00425v2 | GPU 并行仿真+渲染，可泛化具身 AI |
| Genesis | `> 待核实` | Genesis-Embodied-AI | `> 待核实` | 开源项目（非同行评审） | 中高 | ★★★☆☆ | https://github.com/Genesis-Embodied-AI/Genesis | 生成式物理仿真引擎，精度/速度声明待核实 |

### 5.2 数据集与基准

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Open X-Embodiment | 2023 | 多机构联合 | `> 待核实` | arXiv [119] | 高 | ★★★★★ | http://arxiv.org/abs/2310.08864v9 | 跨本体机器人学习数据集 + RT-X 模型 |
| DROID | 2024 | 多机构 | `> 待核实` | arXiv [118] | 高 | ★★★★★ | http://arxiv.org/abs/2403.12945v2 | 大规模真实世界操作数据集 |
| RoboArena | 2025 | — | `> 待核实` | arXiv [125] | 中高 | ★★★★☆ | http://arxiv.org/abs/2506.18123v2 | 分布式真机评测通用机器人策略 |
| ManiSkill3 / ManiSkill | 2024 | haosulab | `> 待核实` | arXiv [108] + 官方文档 | 高 | ★★★★★ | https://maniskill.readthedocs.io/ | 操作仿真基准 |
| RoboCasa | `> 待核实` | — | `> 待核实` | 官方站 | 中高 | ★★★★☆ | https://robocasa.ai/ | 日常任务仿真基准 |
| BEHAVIOR-1K | `> 待核实` | Stanford | `> 待核实` | 官方站 | 中高 | ★★★★☆ | https://behavior.stanford.edu/ | 大规模家务仿真基准（长程任务） |
| LIBERO-VPro | 2026 | — | `> 待核实` | arXiv [113] | 中 | ★★★★☆ | http://arxiv.org/abs/2609.24350v1 | 机器人基础模型闭环视觉鲁棒性基准 |
| LIBERO-Para | 2026 | — | `> 待核实` | arXiv [114] | 中 | ★★★★☆ | http://arxiv.org/abs/2603.28301v3 | VLA 改写鲁棒性诊断基准 |
| LIBERO-Safety | 2026 | — | `> 待核实` | arXiv [117] | 中 | ★★★★☆ | http://arxiv.org/abs/2606.23686v2 | VLA 物理与语义安全基准 |
| RoboDojo | 2026 | — | `> 待核实` | arXiv [98] | 中 | ★★★★☆ | http://arxiv.org/abs/2607.04434v3 | sim-and-real 统一评测 |
| H2RBench | 2026 | — | `> 待核实` | arXiv [97] | 中 | ★★★★☆ | http://arxiv.org/abs/2609.24778v2 | real-to-sim 的 human-to-robot 迁移评测 |
| Benchmarking Simulated Manipulation through a Real World Dataset | 2019 | — | `> 待核实` | arXiv [122] | 中 | ★★★☆☆ | http://arxiv.org/abs/1911.01557v2 | 早期"仿真-真机对照"工作 |
| Generalist Robot Manipulation beyond Action Labeled Data | 2025 | — | `> 待核实` | arXiv [124] | 中 | ★★★☆☆ | http://arxiv.org/abs/2509.19958v1 | 超越动作标注数据的通用操作 |

> **榜单 SOTA 现状**：本次检索**未提供任何可核实的榜单排名数字**（LIBERO、SimplerEnv、ManiSkill3 等排行榜具体名次）。所有"某某模型在 X 上 SOTA"的表述均 `> 待核实`。

### 5.3 开源项目

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| google-deepmind/mujoco | 2012– | DeepMind | `> 待核实` | 官方仓库 | 高 | ★★★★★ | https://github.com/google-deepmind/mujoco | MuJoCo 主仓库 |
| google-deepmind/mujoco_menagerie | — | DeepMind | `> 待核实` | 官方仓库 | 中高 | ★★★★☆ | https://github.com/google-deepmind/mujoco_menagerie | MuJoCo 高质量模型集 |
| Genesis-Embodied-AI/Genesis | — | Genesis 团队 | `> 待核实` | 开源项目 | 中高 | ★★★☆☆ | https://github.com/Genesis-Embodied-AI/Genesis | 生成式物理仿真引擎 |
| haosulab/ManiSkill | 2024– | haosulab | `> 待核实` | 官方仓库 | 高 | ★★★★★ | https://github.com/haosulab/ManiSkill | 操作仿真与基准 |
| isaac-sim/IsaacLab | 2025 | NVIDIA | `> 待核实` | 官方仓库 | 高 | ★★★★★ | https://github.com/isaac-sim/IsaacLab | GPU 并行仿真 |

---

## 六、经典与奠基性工作

> 本节与第一节严格区分：以下为 2012–2023 年间，**构成本方向技术地基**的工作。

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| World Models | 2018 | Ha & Schmidhuber / NeurIPS | `> 待核实` | 同行评审（NeurIPS）[seed] | 高 | ★★★★★ | https://arxiv.org/abs/1803.10122 | 世界模型概念开创：V-M-C 三件套 |
| MuJoCo: A physics engine for model-based control | 2012 | Todorov et al. / IROS | `> 待核实` | 同行评审（IROS）[seed] | 高 | ★★★★★ | https://ieeexplore.ieee.org/document/6386109 | 经典物理引擎，接触建模标杆 |
| Mastering Diverse Domains through World Models (DreamerV3) | 2023 | DeepMind / Nature | `> 待核实` | 同行评审（Nature）[seed] | 高 | ★★★★★ | https://arxiv.org/abs/2301.04104 | 通用世界模型 RL 奠基，跨域单配置 |
| Dreaming: Model-based RL by Latent Imagination without Reconstruction | 2020 | — | `> 待核实` | arXiv [9] | 中 | ★★★★☆ | http://arxiv.org/abs/2007.14535v2 | 无重构隐想象，连接 Dreamer 与后续 latent WM |
| Learning Multimodal Transition Dynamics for Model-Based RL | 2017 | — | `> 待核实` | arXiv [14] | 中 | ★★★★☆ | http://arxiv.org/abs/1705.00470v2 | 多模态转移动力学，世界模型"多假设"先驱 |
| Maximum Entropy Model-based RL | 2021 | — | `> 待核实` | arXiv [13] | 中 | ★★★☆☆ | http://arxiv.org/abs/2112.01195v1 | 最大熵 model-based RL |
| Isaac Gym | 2021 | NVIDIA | `> 待核实` | arXiv [44] | 高 | ★★★★★ | http://arxiv.org/abs/2108.10470v2 | GPU 并行仿真范式奠基 |
| Perspectives on Sim2Real Transfer for Robotics（R:SS 2020 Workshop 总结） | 2020 | 12 位领域学者 | `> 待核实` | workshop report [65] | 中高 | ★★★★☆ | http://arxiv.org/abs/2012.03806v1 | sim2real 定义与可行性辩论的权威二手来源 |

**承上启下关系（简述）**：
- World Models（2018）[seed] 提出"学一个可 rollout 的隐空间环境"，Dreamer 系列将其推向 RL 实用；[9] 去掉重构项，[4]（2026）进一步引入 latent action，构成"latent world model → latent action world model"演进。
- MuJoCo（2012）[seed] 提供 model-based control 的经典仿真底座；Isaac Gym（2021）[44] 把 CPU 单步仿真推向 GPU 万级并行，Isaac Lab [41] 与 ManiSkill3 [108] 承其范式进入多模态时代。
- 域随机化理论化 [17][18][22] 是 sim2real 从"工程技巧"走向"可分析方法"的关键节点，影响了后续数字孪生 [72] 与真机自适应 [54] 两条路线。

---

## 七、评测、争议与开放问题

### 7.1 评测效度

- **仿真 SOTA ≠ 真机 SOTA**：[15] 明确指出机器人本质是真机问题，通用策略的真机评测滞后；[65] 从 workshop 层面记录了领域对 sim2real 可行性的分歧。这是一对可交叉验证的"评测效度"证据。
- **评测正在被分层**：RoboArena 用分布式真机评测 [125]；RoboDojo 做 sim-and-real 联合 [98]；H2RBench 做 real-to-sim 迁移 [97]；LIBERO 系列扩展到视觉鲁棒性 [113]、改写鲁棒性 [114]、安全 [117]。这标志评测从"单一成功率"转向"鲁棒性/安全性/迁移性"。

### 7.2 世界模型的误差累积与幻觉

- **重新定义**：Imagined Rollouts are Kinematic, Not Dynamic [88] 主张长程失败不是笼统的"误差累积"，而是"世界模型倾向运动学想象、缺乏动力学约束"。配套：[7] 从控制论角度分析 latent world model 的可预测性；[93] 提出变长 latent world model 以支撑长程规划；[95] 用世界模型 latent 做失败检测。
  - 权威：arXiv 预印本 [88][7][93][95]｜关注度：中高（`> 待核实`）｜推荐度：★★★★☆。
- **幻觉缓解**：[94] 提出带隐式逻辑推理与幻觉缓解的长程具身规划。
- **生成式世界模型是否"理解物理"**：[53] 提供系统性怀疑视角。

### 7.3 开放问题清单

1. **世界模型能否替代仿真评测？** WorldGym [52] 给出正面尝试，但缺乏与真机评测的一致性验证；`> 待核实`。
2. **视频逼真与物理可用的鸿沟**：GEM-4D [51] 指出视频世界模型无法一致追踪物理点，是当前最明确的"生成≠可用"证据。
3. **长程可信 rollout**：动力学 vs 运动学想象 [88]、变长世界模型 [93]、失败检测 [95]。
4. **sim2real 量化缺口**：检索证据中**没有任何可核实的迁移差距数字**，`> 待核实`；且数字结果对硬件、任务、本体高度敏感，易被误读。
5. **算力与可复现门槛**：GPU 并行仿真（Isaac Lab [41]、ManiSkill3 [108]）与视频世界模型（Cosmos [57]）均隐含高算力门槛，中小实验室复现困难。`> 待核实`（无具体算力/成本数据）。
6. **评测效度**：仿真 SOTA 与真机 SOTA 错位 [15]，跨基准可比性差（`> 待核实`）。
7. **domain gap 与数字孪生的保真度上限**：3DGS 数字孪生 [72] 的保真度与闭环规划收益，`> 待核实`。

### 7.4 争议与失败案例

- **"demo 视频 ≠ 实验证据"**：本报告未纳入任何仅凭演示视频论断的条目。
- **生成式物理引擎的性能声明**：Genesis [seed] 等项目的速度/精度宣称 `> 待核实`，未获一线论文交叉验证。
- **复现困难**：多数 2025–2026 条目为 arXiv 预印本 [51][52][54][56][61][62][63][67][88][93][95]，开源与复现状态 `> 待核实`。

---

## 八、建议关注清单（Watchlist）

| 关注对象 | 类型 | 为什么要关注 | 关键引用 | 关注度 |
|---|---|---|---|---|
| WorldGym | 世界模型即评测环境 | 若成立将改变机器人评测范式 | [52] | 中 |
| GEM-4D | 几何接地视频世界模型 | 直面"视频逼真≠物理可用" | [51] | 中 |
| Genie Envisioner | 机器人操作世界基础平台 | 统一世界模型底座路线 | [56] | 中高 |
| Cosmos / Cosmos-Transfer1 | 物理 AI 世界模型平台 | 通用可控世界生成 | [57][60] | 高 |
| Isaac Lab | GPU 并行仿真框架 | 当前事实标准继任者 | [41] | 高 |
| ManiSkill3 | 并行仿真+渲染基准 | 操作评测主力 | [108] | 高 |
| Genesis | 生成式物理引擎 | 宣称潜力大但 `> 待核实` | [seed] | 中高 |
| RoboArena | 分布式真机评测 | 补足真机 SOTA 缺位 | [125] | 中高 |
| RoboDojo | sim-and-real 统一评测 | 直接回应仿真-真机错位 | [98] | 中 |
| H2RBench | real-to-sim 迁移评测 | 新评测维度 | [97] | 中 |
| LIBERO-VPro / -Para / -Safety | 鲁棒性/安全基准族 | VLA 评测从准确率转向鲁棒安全 | [113][114][117] | 中 |
| 长程世界模型诊断 | 方法论 | 重新定义误差累积 | [88][7][93][95] | 中高 |
| 域随机化理论 | sim2real 方法论 | 经典但仍被引用 | [17][18][22] | 中 |
| 3DGS 数字孪生 | sim2real 工具链 | 2025–2026 热点 | [72] | 中高 |

**Watchlist 说明**：以上条目的**引用数、GitHub star、榜单排名均未在本次检索证据中出现**，故"关注度"仅基于主题新颖性、venue 类型与领域相关性的编辑判断，具体热度数字一律 `> 待核实`，请勿将这些定性判断当作量化结论引用。

---

## 参考来源

[1] Latent-Y: A Lab-Validated Autonomous Agent for De Novo Drug Design — http://arxiv.org/abs/2603.29727v2
[2] Latent-X: An Atom-level Frontier Model for De Novo Protein Binder Design — http://arxiv.org/abs/2507.19375v1
[3] Drug-like antibodies with low immunogenicity in human panels designed with Latent-X2 — http://arxiv.org/abs/2512.20263v1
[4] DiLA: Disentangled Latent Action World Models — http://arxiv.org/abs/2605.15725v1
[5] QCD and High Energy Interactions: Moriond 2018 Theory Summary — http://arxiv.org/abs/1806.04982v2
[6] Evaluation of an open-source implementation of the SRP-PHAT algorithm within the 2018 LOCATA challenge — http://arxiv.org/abs/1812.05901v1
[7] A Control Theory of Predictability in Latent World Models — http://arxiv.org/abs/2607.10362v1
[8] The 2018 PIRM Challenge on Perceptual Image Super-resolution — http://arxiv.org/abs/1809.07517v3
[9] Dreaming: Model-based Reinforcement Learning by Latent Imagination without Reconstruction — http://arxiv.org/abs/2007.14535v2
[10] The Open Ant: A Robot Platform for Reinforcement Learning Research — http://arxiv.org/abs/2607.18488v1
[11] Value Bonuses using Ensemble Errors for Exploration in Reinforcement Learning — http://arxiv.org/abs/2602.12375v1
[12] GIRL: Generative Imagination Reinforcement Learning via Information-Theoretic Hallucination Control — http://arxiv.org/abs/2604.07426v1
[13] Maximum Entropy Model-based Reinforcement Learning — http://arxiv.org/abs/2112.01195v1
[14] Learning Multimodal Transition Dynamics for Model-Based Reinforcement Learning — http://arxiv.org/abs/1705.00470v2
[15] Robot Policy Evaluation for Sim-to-Real Transfer: A Benchmarking Perspective — http://arxiv.org/abs/2508.11117v1
[16] Efficient Sim-to-Real Transfer of World-Action Models from Synthetic Priors — http://arxiv.org/abs/2606.31101v1
[17] Understanding Domain Randomization for Sim-to-real Transfer — http://arxiv.org/abs/2110.03239v2
[18] DROPO: Sim-to-Real Transfer with Offline Domain Randomization — http://arxiv.org/abs/2201.08434v2
[19] Sim-to-Real Transfer in Deep Reinforcement Learning for Bipedal Locomotion — http://arxiv.org/abs/2511.06465v1
[20] Sim-to-Real Transfer for Optical Tactile Sensing — http://arxiv.org/abs/2004.00136v1
[21] The 4th Reactive Synthesis Competition (SYNTCOMP 2017): Benchmarks, Participants & Results — http://arxiv.org/abs/1711.11439v1
[22] Benchmarking Domain Randomisation for Visual Sim-to-Real Transfer — http://arxiv.org/abs/2011.07112v3
[23] Meta-Learning Probabilistic Inference For Prediction — http://arxiv.org/abs/1805.09921v4
[24] FRIDAY: Real-time Learning DNN-based Stable LQR controller for Nonlinear Systems under Uncertain Disturbances — http://arxiv.org/abs/2412.01103v1
[25] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1
[26] Xiaomi-Robotics-1: Scaling Vision-Language-Action Models with over 100K Hours of Real-World Trajectories — http://arxiv.org/abs/2607.15330v2
[27] Planning for robotic exploration based on forward simulation — http://arxiv.org/abs/1502.02474v2
[28] GPU Multisplit: an extended study of a parallel algorithm — http://arxiv.org/abs/1701.01189v2
[29] GPU-Accelerated Multilevel Graph Clustering: A Parallel Perspective on Louvain and Leiden — http://arxiv.org/abs/2608.01503v1
[30] Performance Comparison on Parallel CPU and GPU Algorithms for Unified Gas-Kinetic Scheme — http://arxiv.org/abs/1810.08137v3
[31] Faster Vertex Cover Algorithms on GPUs with Component-Aware Parallel Branching — http://arxiv.org/abs/2512.18334v1
[32] Heterogeneous Highly Parallel Implementation of Matrix Exponentiation Using GPU — http://arxiv.org/abs/1204.3052v1
[33] cuPC: CUDA-based Parallel PC Algorithm for Causal Structure Learning on GPU — http://arxiv.org/abs/1812.08491v4
[34] Static task mapping for heterogeneous systems based on series-parallel decompositions — http://arxiv.org/abs/2502.19745v1
[35] Action Flow Matching for Continual Robot Learning — http://arxiv.org/abs/2504.18471v2
[36] Scalable Aerial GNSS Localization for Marine Robots — http://arxiv.org/abs/2505.04095v2
[37] Using Physiological Measures, Gaze, and Facial Expressions to Model Human Trust in a Robot Partner — http://arxiv.org/abs/2504.05291v1
[38] Model-Based Capacitive Touch Sensing in Soft Robotics — http://arxiv.org/abs/2503.02280v1
[39] Scalable Simulation and Demonstration of Jumping Piezoelectric 2-D Soft Robots — http://arxiv.org/abs/2202.13521v1
[40] Influence of Operator Expertise on Robot Supervision and Intervention — http://arxiv.org/abs/2601.15069v2
[41] Isaac Lab: A GPU-Accelerated Simulation Framework for Multi-Modal Robot Learning — http://arxiv.org/abs/2511.04831v1
[42] The Synthesis of Optimal Control Laws Using Isaacs' Method for the Solution of Differential Games — http://arxiv.org/abs/2112.10849v2
[43] AI Wizards at CheckThat! 2025 — http://arxiv.org/abs/2507.11764v1
[44] Isaac Gym: High Performance GPU-Based Physics Simulation For Robot Learning — http://arxiv.org/abs/2108.10470v2
[45] ClaimIQ at CheckThat! 2025 — http://arxiv.org/abs/2509.11492v1
[46] LongEval at CLEF 2025: Longitudinal Evaluation of IR Model Performance — http://arxiv.org/abs/2503.08541v1
[47] NTIRE 2025 Challenge on Image Super-Resolution (x4) — http://arxiv.org/abs/2504.14582v3
[48] A Survey of Robot Manipulation in Contact — http://arxiv.org/abs/2112.01942v3
[49] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1
[50] One-Shot Reinforcement Learning for Robot Navigation with Interactive Replay — http://arxiv.org/abs/1711.10137v2
[51] GEM-4D: Geometry-Enhanced Video World Models for Robot Manipulation — http://arxiv.org/abs/2605.22882v4
[52] WorldGym: World Model as An Environment for Policy Evaluation — http://arxiv.org/abs/2506.00613v3
[53] Is Sora a World Simulator? A Comprehensive Survey on General World Models and Beyond — http://arxiv.org/abs/2405.03520v2
[54] Robot Trains Robot: Automatic Real-World Policy Adaptation and Learning for Humanoids — http://arxiv.org/abs/2508.12252v2
[55] A Human-Vector Susceptible-Infected-Susceptible Model for Analyzing and Controlling the Spread of Vector-Borne Diseases — http://arxiv.org/abs/2510.14787v2
[56] Genie Envisioner: A Unified World Foundation Platform for Robotic Manipulation — http://arxiv.org/abs/2508.05635v3
[57] Cosmos World Foundation Model Platform for Physical AI — http://arxiv.org/abs/2501.03575v3
[58] Embodied AI with Foundation Models for Mobile Service Robots: A Systematic Review — http://arxiv.org/abs/2505.20503v2
[59] Neutrino-Nucleon Cross-Section Model Tuning in GENIE v3 — http://arxiv.org/abs/2104.09179v2
[60] Cosmos-Transfer1: Conditional World Generation with Adaptive Multimodal Control — http://arxiv.org/abs/2503.14492v2
[61] Direct Experience World-Model Optimization: Learning the World Beyond Action Imitation — http://arxiv.org/abs/2609.37398v1
[62] DECOWAM: Decoupled Whole-Body World-Action Model for Legged Mobile Manipulation — http://arxiv.org/abs/2608.20114v2
[63] ForeTime-VLA: Causal Future-Token Distillation from a World Action Model for Conveyor-Belt Manipulation — http://arxiv.org/abs/2608.20735v2
[64] Bridging the Sim2Real Gap: Vision Encoder Pre-Training for Visuomotor Policy Transfer — http://arxiv.org/abs/2501.16389v2
[65] Perspectives on Sim2Real Transfer for Robotics: A Summary of the R:SS 2020 Workshop — http://arxiv.org/abs/2012.03806v1
[66] The Importance and the Limitations of Sim2Real for Robotic Manipulation in Precision Agriculture — http://arxiv.org/abs/2008.03983v1
[67] Robot Manipulation with GPT-6-Astra: Body Knowledge, Experience Reuse, Emergent Skills, and Sim2Real Transfer — http://arxiv.org/abs/2609.31770v1
[68] Sim2Real Transfer for Audio-Visual Navigation with Frequency-Adaptive Acoustic Field Prediction — http://arxiv.org/abs/2405.02821v2
[69] Federated and Transfer Learning: A Survey on Adversaries and Defense Mechanisms — http://arxiv.org/abs/2207.02337v1
[70] State-of-the-art in Robot Learning for Multi-Robot Collaboration: A Comprehensive Survey — http://arxiv.org/abs/2408.11822v1
[71] Digital Twin as a Service (DTaaS): A Platform for Digital Twin Developers and Users — http://arxiv.org/abs/2305.07244v2
[72] A High-Fidelity Digital Twin for Robotic Manipulation Based on 3D Gaussian Splatting — http://arxiv.org/abs/2601.03200v2
[73] Digital Twin As A Cost Reduction Method — http://arxiv.org/abs/2107.14109v1
[74] Enabling Automated Integration Testing of Smart Farming Applications via Digital Twin Prototypes — http://arxiv.org/abs/2311.05748v1
[75] MATTERIX: toward a digital twin for robotics-assisted chemistry laboratory automation — http://arxiv.org/abs/2601.13232v1
[76] Real-Time Digital Twins: Vision and Research Directions for 6G and Beyond — http://arxiv.org/abs/2301.11283v1
[77] Embedded Software Development with Digital Twins — http://arxiv.org/abs/2309.09216v1
[78] tFUSOperator: Operator Learning for Transcranial Focused Ultrasound Digital Twins — http://arxiv.org/abs/2608.01839v1
[79] NTU-NPU System for Voice Privacy 2024 Challenge — http://arxiv.org/abs/2410.02371v1
[80] NPU-NTU System for Voice Privacy 2024 Challenge — http://arxiv.org/abs/2409.04173v2
[81] ICPR 2024 Competition on DAGECC — http://arxiv.org/abs/2412.17984v1
[82] NAIST Simultaneous Speech Translation System for IWSLT 2024 — http://arxiv.org/abs/2407.00826v1
[83] Double Multi-Head Attention Multimodal System for Odyssey 2024 SER Challenge — http://arxiv.org/abs/2406.10598v1
[84] Discovery Opportunities with Gravitational Waves -- TASI 2024 Lecture Notes — http://arxiv.org/abs/2409.08956v1
[85] Atmospheric entry and fragmentation of small asteroid 2024 BX1 — http://arxiv.org/abs/2403.00634v2
[86] Uncovering Coordinated Cross-Platform Information Operations (2024 U.S. Election) — http://arxiv.org/abs/2409.15402v2
[87] On-Policy Robot Imitation Learning from a Converging Supervisor — http://arxiv.org/abs/1907.03423v7
[88] Imagined Rollouts are Kinematic, Not Dynamic: A Diagnosis of Long-Horizon World-Model Failure — http://arxiv.org/abs/2607.05966v1
[89] LongCoT: Benchmarking Long-Horizon Chain-of-Thought Reasoning — http://arxiv.org/abs/2604.14140v1
[90] SAGA: Scene-Aware, Goal-Evolving Agents for Long-Horizon Strategy Game Planning — http://arxiv.org/abs/2606.29932v4
[91] Dynamic Intelligence Ceilings: Measuring Long-Horizon Limits of Planning and Creativity — http://arxiv.org/abs/2601.06102v1
[92] Think Fast and Far: Long-Horizon Online POMDP Planning via Rapid State Sampling — http://arxiv.org/abs/2606.04355v1
[93] Beyond the Next Step: Variable-Length Latent World Models for Long-Horizon Planning — http://arxiv.org/abs/2606.21775v1
[94] Long-horizon Embodied Planning with Implicit Logical Inference and Hallucination Mitigation — http://arxiv.org/abs/2409.15658v2
[95] Foresight: Failure Detection for Long-Horizon Robotic Manipulation with Action-Conditioned World Model Latents — http://arxiv.org/abs/2606.23085v1
[96] The Sound of Simulation: Learning Multimodal Sim-to-Real Robot Policies with Generative Audio — http://arxiv.org/abs/2507.02864v2
[97] H2RBench: A Real-to-Sim Benchmark for Evaluating Human-to-Robot Transfer — http://arxiv.org/abs/2609.24778v2
[98] RoboDojo: A Unified Sim-and-Real Benchmark for Comprehensive Evaluation of Generalist Robot Manipulation Policies — http://arxiv.org/abs/2607.04434v3
[99] Overview of the Sensemaking Task at the ELOQUENT 2025 Lab — http://arxiv.org/abs/2507.12143v1
[100] LLM-based ambiguity detection in natural language instructions for collaborative surgical robots — http://arxiv.org/abs/2507.11525v1
[101] Reinforced Imitation in Heterogeneous Action Space — http://arxiv.org/abs/1904.03438v2
[102] Imitation Learning for End to End Vehicle Longitudinal Control with Forward Camera — http://arxiv.org/abs/1812.05841v1
[103] RIZE: Adaptive Regularization for Imitation Learning — http://arxiv.org/abs/2502.20089v3
[104] One-Shot Visual Imitation Learning via Meta-Learning — http://arxiv.org/abs/1709.04905v1
[105] Coarse-to-Fine Imitation Learning: Robot Manipulation from a Single Demonstration — http://arxiv.org/abs/2105.06411v2
[106] Communicating Plans, Not Percepts: Scalable Multi-Agent Coordination with Embodied World Models — http://arxiv.org/abs/2508.02912v4
[107] High-level robot programming based on CAD — http://arxiv.org/abs/1309.2086v1
[108] ManiSkill3: GPU Parallelized Robotics Simulation and Rendering for Generalizable Embodied AI — http://arxiv.org/abs/2410.00425v2
[109] VLSP 2025 MLQA-TSR Challenge — http://arxiv.org/abs/2510.20381v1
[110] Event-Enriched Image Analysis Grand Challenge at ACM Multimedia 2025 — http://arxiv.org/abs/2508.18904v1
[111] AIM 2025 Low-light RAW Video Denoising Challenge — http://arxiv.org/abs/2508.16830v1
[112] The AudioMOS Challenge 2025 — http://arxiv.org/abs/2509.01336v1
[113] LIBERO-VPro: Benchmarking Closed-Loop Visual Robustness of Robotic Foundation Models — http://arxiv.org/abs/2609.24350v1
[114] LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models — http://arxiv.org/abs/2603.28301v3
[115] A Human-Grounded Evaluation Benchmark for Local Explanations of Machine Learning — http://arxiv.org/abs/1801.05075v2
[116] Exploring Large Language Models to Facilitate Variable Autonomy for Human-Robot Teaming — http://arxiv.org/abs/2312.07214v3
[117] LIBERO-Safety: A Comprehensive Benchmark for Physical and Semantic Safety in VLA Models — http://arxiv.org/abs/2606.23686v2
[118] DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset — http://arxiv.org/abs/2403.12945v2
[119] Open X-Embodiment: Robotic Learning Datasets and RT-X Models — http://arxiv.org/abs/2310.08864v9
[120] The RSNA Abdominal Traumatic Injury CT (RATIC) Dataset — http://arxiv.org/abs/2405.19595v1
[121] The RSNA Lumbar Degenerative Imaging Spine Classification (LumbarDISC) Dataset — http://arxiv.org/abs/2506.09162v1
[122] Benchmarking Simulated Robotic Manipulation through a Real World Dataset — http://arxiv.org/abs/1911.01557v2
[123] Waymo Open Dataset: Panoramic Video Panoptic Segmentation — http://arxiv.org/abs/2206.07704v1
[124] Generalist Robot Manipulation beyond Action Labeled Data — http://arxiv.org/abs/2509.19958v1
[125] RoboArena: Distributed Real-World Evaluation of Generalist Robot Policies — http://arxiv.org/abs/2506.18123v2

**Seed 资源（无 arXiv 编号，以链接引用）**：
- DreamerV3 — https://arxiv.org/abs/2301.04104
- World Models (2018) — https://arxiv.org/abs/1803.10122
- MuJoCo (IROS 2012) — https://ieeexplore.ieee.org/document/6386109
- google-deepmind/mujoco — https://github.com/google-deepmind/mujoco
- google-deepmind/mujoco_menagerie — https://github.com/google-deepmind/mujoco_menagerie
- Genesis-Embodied-AI/Genesis — https://github.com/Genesis-Embodied-AI/Genesis
- haosulab/ManiSkill — https://github.com/haosulab/ManiSkill
- isaac-sim/IsaacLab — https://github.com/isaac-sim/IsaacLab
- ManiSkill 文档 — https://maniskill.readthedocs.io/
- RoboCasa — https://robocasa.ai/
- BEHAVIOR-1K — https://behavior.stanford.edu/

---

*Generated by research-bot · topic=`embodied-world-models` · depth=`standard` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading · model=`deepseek-v4-flash` · sources=125 · duration=309s · 2026-10-04T22:40:46+00:00*
