# 具身智能 · 世界模型与仿真（World Models & Simulation）调研报告

**元信息**：报告日期 2026-10-02（UTC） ｜ 领域：具身智能 / 世界模型（World Models）/ 神经仿真（Neural Simulation）/ sim2real ｜ 可核查来源：33 条编号引用 [1]–[33] ＋ 11 条领域种子资源（本地维护清单，非本次实时检索命中）
**证据分级约定**：A=同行评审/官方技术报告；B=arXiv 预印本/官方仓库；C=第三方评测/榜单；D=个人博客/社区；E=不可用。本次证据集以 B 级为主，**无 A 级同行评审结论**，且存在明显召回噪声（见第七节）。

---

## 摘要（Executive Summary）

1. **2024–2026 年世界模型在具身智能中的主战场，已从「用世界模型做策略内部表征」转向「用生成式视频世界模型直接充当环境与评测器」。** WorldGym 明确把自回归、动作条件的视频生成模型定位为真实环境的代理，用蒙特卡洛 rollout 做策略评估 [17]；这代表了一类新的方法论定位：世界模型不只是 policy 的一部分，而是 **evaluation harness**。（证据等级 B）

2. **该路线当前最被反复指认的瓶颈是「视觉逼真 ≠ 物理可执行」。** GEM-4D 的动机陈述直言：视频世界模型能生成看似合理的未来，但无法跨时间一致地跟踪同一物理点，因而缺乏可靠动作执行（如机器人操作）所需的物理 grounding [15]。Imagined Rollouts are Kinematic, Not Dynamic 更进一步，把长时程世界模型的失败诊断为「运动学而非动力学」的 rollout 性质 [23]。（证据等级 B，属作者自述动机，尚缺第三方复现）

3. **世界模型的自改进与可验证性开始成为独立子方向。** World Action Verifier 提出通过「前向-逆向不对称（Forward-Inverse Asymmetry）」实现世界模型自改进 [20]。（证据等级 B；具体机制与实验规模在本轮候选块中不可见，`> 待核实`）

4. **仿真工程栈的世代交替已完成一次：Isaac Gym → Isaac Lab。** Isaac Lab 被官方定位为 Isaac Gym 的自然后继（natural successor），把 GPU-native 机器人仿真扩展到大规摸多模态学习 [27][26]。（证据等级 B）

5. **sim2real 的争议焦点已从「能不能迁」转为「怎么评」。** Robot Policy Evaluation for Sim-to-Real Transfer: A Benchmarking Perspective 直接以 benchmarking 视角讨论这一问题 [18]；真机侧则出现 Xiaomi-Robotics-1 这类以 10 万小时以上真机轨迹做 scaling 的工作 [29]，构成对「仿真优先」叙事的有力对冲。（证据等级 B）

6. **本轮检索存在严重证据缺口，必须显式声明**：①数据集/基准条目 **零命中**（Open X-Embodiment [10] 是唯一可引用者，但本轮抽取未提供其评测口径细节）；②物理引擎性能数字（吞吐、接触精度、可微性）**零命中**；③所有世界模型类条目的任务数、本体数、成功率定义 **全部缺失**；④33 条来源中约 15 条为跨领域噪声。**因此本报告在「性能对比」与「SOTA 榜单」层面不做任何断言。**

---

## 一、关键前沿进展（近 1–2 年）

本节只收录 2024–2026 年间的节点，经典工作见第六节。

### 1.1 趋势主线：世界模型的三次定位迁移

| 定位 | 代表工作 | 时间 | 含义 |
|---|---|---|---|
| 世界模型 = 策略内部表征 | DreamerV3（种子资源） | 2023 | 在潜空间想象 rollout 训练 policy |
| 世界模型 = 基础模型的应用对象 | Foundation Models as World Models (FWM) / Foundation Agents (FA) [9] | 2025 | 追问基础模型能否直接充当世界模型或决策者 |
| 世界模型 = 环境 / 评测器 | WorldGym [17]、GEM-4D [15] | 2025–2026 | 用视频生成模型替代真实环境做策略评估 |

**FWM vs FA 的问题设定** [9]：该工作在文本型 GridWorld（text-based GridWorlds）中评估两种策略——FWM（利用基础模型先验，用模拟交互训练与评测智能体）与 FA（利用基础模型推理能力做决策），并指出「RL from scratch 在高效模拟器中表现好，但真实世界应用交互代价高、需要更高样本效率的智能体」，且「如何将 FMs 有效整合进 RL 框架仍不清楚」。
- **热度证据**：`> 待核实`（候选块未提供 citations 数据）
- **权威证据**：arXiv 预印本（arXiv:2509.15915v1, cs.LG），未标注同行评审 venue [9]
- **关注度**：低 —— 2025-09 预印本，候选块无引用/榜单/社区讨论信号 [9]
- **推荐度**：★★★☆☆ —— 概念框架有参考价值，但评测载体是文本 GridWorld，离机器人具身口径较远 [9]

### 1.2 工程栈代际：Isaac Gym → Isaac Lab

Isaac Lab 被描述为「Isaac Gym 的自然后继（natural successor）」，把 GPU-native 机器人仿真范式扩展到大规模多模态学习时代，组合高保真 GPU 并行物理、照片级渲染与模块化可组合架构 [27][26]。
- **热度证据**：`> 待核实`（候选块未提供 citations/star 数据）
- **权威证据**：Isaac Lab 为 arXiv cs.RO 预印本（arXiv:2511.04831v1）[27]；Isaac Gym 为 arXiv cs.RO 预印本（arXiv:2108.10470v2, 2021）[26]；二者均有 NVIDIA 官方仓库对应（种子项目 `isaac-sim/IsaacLab`）
- **关注度**：中 —— 作为机器人学习主流 GPU 仿真栈的后继版本，工程社区存在持续关注；但本轮候选块无 star/下载等可核查数字，`> 待核实` [27]
- **推荐度**：★★★★★ —— 若做大规模并行机器人学习，这是当前最主流的工程入口 [27]

### 1.3 表征层的前沿：对象中心世界模型的受控研究

Better Slots, Better Worlds 指出，此前的 object-centric world models（OCWMs）**把 slot encoder 当作既定组件（take the slot encoder as given）**，且**只在分布内（in-distribution）评测**；该文沿两条轴做受控研究：对象中心表征质量、以及相对 scene-centric 模型在分布偏移下的泛化 [5]。
- **热度证据**：`> 待核实`（候选块未提供 citations/下载量）
- **权威证据**：arXiv 预印本（arXiv:2608.12078v1, cs.CV），未标注同行评审 venue [5]
- **关注度**：低 —— 2026-08 新预印本，无引用、无 star、无榜单排名信号 [5]
- **推荐度**：★★★★☆ —— 本主题中「世界模型 + 评测口径」相关性最强的条目，建议精读全文补齐任务数、本体数与成功率定义 [5]
- **关键结论**：OCWM 相对 scene-centric 模型是否真因对象中心归纳偏置带来规划收益，候选块在结论处被截断，`> 待核实` [5]

---

## 二、生成式 / 视频世界模型

### 2.1 GEM-4D：几何增强的视频世界模型（2026）

GEM-4D 是面向机器人操作的「几何增强视频世界模型」，直接针对视频世界模型的物理一致性缺陷 [15]。

**核心问题陈述（论文原文级证据）**：视频世界模型生成的视频「appear plausible, yet lack the physical grounding required for reliable action execution, such as robot manipulation」；根因是难以跨时间一致地跟踪同一物理点 [15]。

- **热度证据**：`> 待核实`（候选块未提供 citations/star）
- **权威证据**：arXiv 预印本（arXiv:2605.22882v4，2026-05-20 提交，cs.CV），v4 版本；候选块未标注同行评审 venue [15]
- **关注度**：中 —— 直接命中「视频世界模型 + 机器人操作」这一子问题核心，且以 v4 迭代说明作者在持续修订；但无引用/star 信号支撑更高判断 [15]
- **推荐度**：★★★★☆ —— 子问题核心候选；需精读全文核实其真机/仿真验证设置与具体几何 grounding 机制（摘要该处被截断）[15]
- **验证强度**：`> 待核实` —— 任务数、本体数、真机 vs 仿真占比在候选块中完全缺失 [15]

### 2.2 WorldGym：世界模型即环境，用于策略评估（2025）

WorldGym 把真实机器人策略评估的困难明确为两点：真机测试昂贵、手工仿真器需人工投入提升真实性与通用性。其方案是**自回归、动作条件的视频生成模型作为真实世界环境的代理**，策略通过**蒙特卡洛 rollout** 进行评估 [17]。

- **热度证据**：`> 待核实`（候选块未提供 citations/star）
- **权威证据**：arXiv 预印本（arXiv:2506.00613v3，2025-05-31 提交，cs.RO），v3 版本；未标注同行评审 venue [17]
- **关注度**：中 —— 是少数把视频世界模型定位为**评估环境**而非 policy 组件的工作，方法论定位稀缺；但候选块无引用/榜单信号 [17]
- **推荐度**：★★★★☆ —— 覆盖本主题「交互式 rollout / 策略评估」维度，建议核实其代理保真度（proxy fidelity）实验设计 [17]
- **开放问题**：蒙特卡洛 rollout 的评估结论能否迁移到真机，候选证据未给出边界，`> 待核实` [17]

### 2.3 长时程失败的机理诊断（2026）

Imagined Rollouts are Kinematic, Not Dynamic: A Diagnosis of Long-Horizon World-Model Failure 从标题层面即给出强论断：**想象出的 rollout 是运动学的，而非动力学的**，并以此诊断长时程世界模型失败 [23]。

- **热度证据**：`> 待核实`（本轮未提供 citations 数据）
- **权威证据**：arXiv 预印本（arXiv:2607.05966v1），未标注同行评审 venue [23]
- **关注度**：中 —— 该论断与 GEM-4D 的「物理点一致性」问题 [15] 形成呼应，指向同一类失效模式
- **推荐度**：★★★★☆ —— 若该诊断成立，则对「视频世界模型能否替代物理仿真」给出否定性线索；但**属单篇论文论断，需独立第三方复现，`> 待核实`** [23]

### 2.4 世界模型的自改进（2026）

World Action Verifier: Self-Improving World Models via Forward-Inverse Asymmetry 提出以「前向-逆向不对称」作为自改进机制 [20]。

- **热度证据**：`> 待核实`
- **权威证据**：arXiv 预印本（arXiv:2604.01985v2），未标注同行评审 venue [20]
- **关注度**：低至中 —— 本轮候选块仅有标题级信息，无摘要细节
- **推荐度**：★★★☆☆ —— 方向（世界模型自我验证）有价值，但本轮证据不足以评估 [20]

### 2.5 生成式 VLA 与视频生成的交叉

GR-2 被描述为「A Generative Video-Language-Action Model for Robot Manipulation」，在本轮证据中以两个 DOI 形式出现 [21][22]。

- **热度证据**：`> 待核实`
- **权威证据**：DOI 10.59350/18ct2-xbf48 [21] 与 DOI 10.59350/m5s7m-3kd85 [22]；`> 待核实` 二者是否为同一工作的不同版本
- **关注度**：`> 待核实`
- **推荐度**：★★★☆☆ —— 与「生成式模型 + 动作」交叉主题相关，但本轮无摘要级证据，暂列观察 [21][22]

### 2.6 文本到视频生成的综述视角

Sora as a World Model? A Complete Survey on Text-to-Video Generation 以「Sora 是否是世界模型」为切入点做文本到视频生成综述 [16]。
- **热度证据**：`> 待核实`
- **权威证据**：arXiv 预印本（arXiv:2403.05131v3），未标注同行评审 venue [16]
- **关注度**：中 —— 标题命中了「视频生成是否构成世界模型」这一社区争议命题
- **推荐度**：★★★☆☆ —— 可作为争议背景引用，但需核实其是否覆盖机器人动作条件场景（text-to-video ≠ action-conditioned video）[16]

---

## 三、神经仿真与可微物理

**本章是本报告证据最薄弱的章节，必须首先声明：本轮候选块中，关于可微仿真（differentiable simulation）、Brax / Warp / MJX 的可用性、性能与精度，`零命中`。以下仅能就 GPU 并行仿真工程栈给出 B 级证据。**

### 3.1 GPU 并行物理仿真工程栈

| 引擎 | 年份 | 权威证据 | 定位 | 链接 |
|---|---|---|---|---|
| Isaac Gym | 2021 | arXiv cs.RO 预印本（arXiv:2108.10470v2）[26] | GPU-based 高性能物理仿真，面向机器人学习 | http://arxiv.org/abs/2108.10470v2 |
| Isaac Lab | 2025 | arXiv cs.RO 预印本（arXiv:2511.04831v1）[27] | Isaac Gym 的自然后继；GPU 并行物理 + 照片级渲染 + 模块化可组合架构，面向大规模多模态学习 | http://arxiv.org/abs/2511.04831v1 |
| MuJoCo | 2012 | IROS 论文（种子资源，**非本次实时检索命中**） | 基于模型的经典物理引擎 | https://ieeexplore.ieee.org/document/6386109 |
| Genesis | — | 官方 GitHub（种子项目，**非本次实时检索命中**） | 生成式物理仿真引擎 | https://github.com/Genesis-Embodied-AI/Genesis |
| ManiSkill | — | 官方仓库（种子项目） | 操作仿真与基准 | https://github.com/haosulab/ManiSkill |

**关于 Isaac Lab 的四轴证据：**
- **热度证据**：`> 待核实` —— 候选块未提供 citations / star / 下载量 [27]
- **权威证据**：arXiv cs.RO 预印本（arXiv:2511.04831v1）[27]，并有 NVIDIA 官方仓库 `isaac-sim/IsaacLab` 作为工程事实标准（种子项目）
- **关注度**：中 —— 作为 Isaac Gym 的官方后继 [26][27]，在机器人学习工程社区具有事实上的主流地位；但无可核查数字，`> 待核实`
- **推荐度**：★★★★★ —— 大规模并行 RL / 多模态机器人学习的首选工程栈 [27]

**关于 MuJoCo 的四轴证据：**
- **热度证据**：`> 待核实`（种子资源未提供 star/引用数）
- **权威证据**：IROS 2012 论文（**同行评审**，本报告中少数 A 级证据之一），官方仓库 `google-deepmind/mujoco` 由 Google DeepMind 维护（种子资源）
- **关注度**：高 —— 长期作为机器人学习与 model-based control 的默认物理引擎；本判断基于领域共识而非本轮检索数字，`> 待核实`
- **推荐度**：★★★★★ —— 无论做 model-based control 还是作为仿真基线，MuJoCo 都是必选项（种子资源）

**关于 Genesis 的四轴证据：**
- **热度证据**：`> 待核实` —— 本轮检索未命中其论文或仓库指标
- **权威证据**：官方 GitHub 仓库 `Genesis-Embodied-AI/Genesis`（种子项目，B 级）
- **关注度**：`> 待核实` —— 无法基于本轮证据判断
- **推荐度**：★★★☆☆ —— 定位为「生成式物理仿真引擎」，与本主题高度相关，但本轮**无任何一手证据**支撑其可用性或保真度，建议单独立项核实

### 3.2 可微仿真的证据缺口（显式负面发现）

> **待核实**：本轮 33 条来源中，**没有任何一条**提供关于 Brax、Warp、MJX、DiffTaichi 等可微仿真栈的可用性、性能或 sim2real 效果的可核查证据。第一节到第七节中所有涉及「可微物理」的对比结论，本次均无法支撑，需另行检索。

---

## 四、sim2real 迁移与方法

### 4.1 评测口径问题被提升为独立议题（2025）

Robot Policy Evaluation for Sim-to-Real Transfer: A Benchmarking Perspective 以**基准测试视角**处理 sim2real 的策略评估问题 [18]。这标志着该方向的讨论重心从「迁移算法」转向「如何公平地度量迁移」。
- **热度证据**：`> 待核实`
- **权威证据**：arXiv 预印本（arXiv:2508.11117v1, 2025），未标注同行评审 venue [18]
- **关注度**：中 —— 直接命中「sim2real 争议」这一必答议题
- **推荐度**：★★★★☆ —— 做 sim2real 评测方案设计时的关键参考；需核实其提出的 benchmark 协议细节 [18]

### 4.2 真机自适应的反向路径（2025）

Robot Trains Robot: Automatic Real-World Policy Adaptation and Learning for Humanoids 提出面向人形机器人的**自动真机策略自适应与学习**，即由机器人自身完成真机数据采集与策略改进 [19]。
- **热度证据**：`> 待核实`
- **权威证据**：arXiv 预印本（arXiv:2508.12252v2, 2025），未标注同行评审 venue [19]
- **关注度**：中 —— 人形 + 自动真机自适应，是对「仿真先行」路线的实践性替代
- **推荐度**：★★★★☆ —— sim2real 章节的重要对照案例；需核实其任务数与本体数，`> 待核实` [19]

### 4.3 Real-to-Sim 的反向迁移（2024）

Toward Control of Wheeled Humanoid Robots with Unknown Payloads: Equilibrium Point Estimation via Real-to-Sim Adaptation 处理轮式人形机器人在**未知负载**下的控制，方法为通过 **real-to-sim adaptation** 估计平衡点 [33]。
- **热度证据**：`> 待核实`
- **权威证据**：arXiv 预印本（arXiv:2403.10948v2, 2024），未标注同行评审 venue [33]
- **关注度**：中 —— real-to-sim（把真实系统的参数辨识回灌仿真）是 sim2real 的必要对偶方向
- **推荐度**：★★★★☆ —— 对「未知负载」这类难以纯仿真建模的场景提供具体方法范式 [33]

### 4.4 持续学习中的动作流匹配（2025）

Action Flow Matching for Continual Robot Learning 将 flow matching 用于持续机器人学习 [30]。
- **热度证据**：`> 待核实`
- **权威证据**：arXiv 预印本（arXiv:2504.18471v2, 2025），未标注同行评审 venue [30]
- **关注度**：低至中 —— 本轮候选块无摘要级细节
- **推荐度**：★★★☆☆ —— 与仿真/世界模型为间接相关（持续学习场景常依赖 sim 回放），建议按需核实 [30]

### 4.5 真机数据规模的量级参照（2026）

Xiaomi-Robotics-1 以 **over 100K Hours of Real-World Trajectories** 做 VLA 模型 scaling（标题级证据）[29]。
- **热度证据**：`> 待核实`（未提供 citations 数据）
- **权威证据**：arXiv 预印本（arXiv:2607.15330v2, 2026），未标注同行评审 venue [29]
- **关注度**：中 —— 「10 万小时真机轨迹」是当前 sim2real 辩论中真机路线一方的重要量级参照 [29]
- **推荐度**：★★★★☆ —— **对 sim2real 争议的关键对冲证据**：若真机数据规模的边际收益显著高于仿真，则「世界模型/仿真替代真机」的叙事需要重新审视。注意该数字来自标题，口径（是否含遥操作、多本体）`> 待核实` [29]

### 4.6 早期奠基性的样本效率动机（2017）

One-Shot Reinforcement Learning for Robot Navigation with Interactive Replay 针对「model-free RL 依赖大量环境交互，而迁移到机器人领域的重大问题是真实世界交互代价高，且在有限经验上训练易过拟合」这一动机，提出面向固定目标、结合交互式回放的样本高效导航学习 [1]。
- **热度证据**：`> 待核实`（候选块未提供引用数）
- **权威证据**：arXiv 预印本（arXiv:1711.10137v2, cs.AI, 2017），未标注同行评审 venue [1]
- **关注度**：低 —— 候选块无引用数等信号 [1]
- **推荐度**：★★★☆☆ —— 作为「真实交互昂贵 ⇒ 需要世界模型/样本高效方法」这一论证的早期引文；引用时须注意其年代与后续世界模型工作的代际差异 [1]

---

## 五、仿真引擎与基准

### 5.1 数据集与基准

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Open X-Embodiment (Robotic Learning Datasets and RT-X Models) | 2023 | 多机构联合（论文）[10] | `> 待核实` | arXiv 预印本（arXiv:2310.08864v9）[10] | 高 —— 是 VLA / 跨本体机器人学习的公开数据聚合事实标准；本轮无榜单数字，`> 待核实` [10] | ★★★★★ | http://arxiv.org/abs/2310.08864v9 | 跨本体机器人学习数据集与 RT-X 模型；本轮抽取未提供其评测口径细节，`> 待核实` [10] |
| ManiSkill3 / ManiSkill benchmarks | — | haosulab（种子资源） | `> 待核实` | 官方文档站（B 级，种子资源） | `> 待核实` | ★★★★☆ | https://maniskill.readthedocs.io/ | 操作仿真基准；本轮未命中其论文或榜单，需另行核实 [10 之外] |
| RoboCasa | — | 官方站点（种子资源） | `> 待核实` | 官方主页（B 级，种子资源） | `> 待核实` | ★★★★☆ | https://robocasa.ai/ | 日常任务仿真基准 |
| BEHAVIOR-1K | — | Stanford（种子资源） | `> 待核实` | 官方主页（B 级，种子资源） | `> 待核实` | ★★★★☆ | https://behavior.stanford.edu/ | 大规模家务仿真基准 |

> **显式负面发现（证据等级：高，基于证据集覆盖度判断）**：本轮 33 条来源中**不含任何 type=dataset 或 type=benchmark 的条目**；LIBERO、SimplerEnv、DROID、RoboArena 等被点名的基准**零命中**。因此**本报告不提供任何跨基准的横向对比或 SOTA 排名表**。上表中除 Open X-Embodiment [10] 外，其余均为领域种子资源，其四轴证据需单独检索核实。

### 5.2 开源项目

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| google-deepmind/mujoco | — | Google DeepMind（种子资源） | `> 待核实` | 官方仓库（B 级，种子资源）；底层方法有 IROS 2012 同行评审

## 参考来源

[1] One-Shot Reinforcement Learning for Robot Navigation with Interactive Replay — http://arxiv.org/abs/1711.10137v2
[2] The 1995 Pilot Campaign of PLANET: Searching for Microlensing Anomalies through Precise, Rapid, Round-the-Clock Monitoring — http://arxiv.org/abs/astro-ph/9807299v1
[3] QCD and High Energy Interactions: Moriond 2018 Theory Summary — http://arxiv.org/abs/1806.04982v2
[4] Evaluation of an open-source implementation of the SRP-PHAT algorithm within the 2018 LOCATA challenge — http://arxiv.org/abs/1812.05901v1
[5] Better Slots, Better Worlds: Representation Quality & Robustness in Object-Centric World Models — http://arxiv.org/abs/2608.12078v1
[6] Limb-Darkening of a K Giant in the Galactic Bulge: PLANET Photometry of MACHO 97-BLG-28 — http://arxiv.org/abs/astro-ph/9811479v3
[7] The 2018 PIRM Challenge on Perceptual Image Super-resolution — http://arxiv.org/abs/1809.07517v3
[8] Luminoso at SemEval-2018 Task 10: Distinguishing Attributes Using Text Corpora and Relational Knowledge — http://arxiv.org/abs/1806.01733v2
[9] Foundation Models as World Models: A Foundational Study in Text-Based GridWorlds — http://arxiv.org/abs/2509.15915v1
[10] Open X-Embodiment: Robotic Learning Datasets and RT-X Models — http://arxiv.org/abs/2310.08864v9
[11] Proceedings of the Dialogue Robot Competition 2023 — http://arxiv.org/abs/2312.14430v5
[12] A New Planet: The Tale of Genji as World Literature (Michael Emmerich) 177 — https://doi.org/10.3726/978-1-4539-0784-9/13
[13] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1
[14] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1
[15] GEM-4D: Geometry-Enhanced Video World Models for Robot Manipulation — http://arxiv.org/abs/2605.22882v4
[16] Sora as a World Model? A Complete Survey on Text-to-Video Generation — http://arxiv.org/abs/2403.05131v3
[17] WorldGym: World Model as An Environment for Policy Evaluation — http://arxiv.org/abs/2506.00613v3
[18] Robot Policy Evaluation for Sim-to-Real Transfer: A Benchmarking Perspective — http://arxiv.org/abs/2508.11117v1
[19] Robot Trains Robot: Automatic Real-World Policy Adaptation and Learning for Humanoids — http://arxiv.org/abs/2508.12252v2
[20] World Action Verifier: Self-Improving World Models via Forward-Inverse Asymmetry — http://arxiv.org/abs/2604.01985v2
[21] GR-2: A Generative Video-Language-Action Model for Robot Manipulation — https://doi.org/10.59350/18ct2-xbf48
[22] GR-2: A Generative Video-Language-Action Model for Robot Manipulation — https://doi.org/10.59350/m5s7m-3kd85
[23] Imagined Rollouts are Kinematic, Not Dynamic: A Diagnosis of Long-Horizon World-Model Failure — http://arxiv.org/abs/2607.05966v1
[24] The Synthesis of Optimal Control Laws Using Isaacs' Method for the Solution of Differential Games — http://arxiv.org/abs/2112.10849v2
[25] NTIRE 2025 Challenge on Image Super-Resolution (x4): Methods and Results — http://arxiv.org/abs/2504.14582v3
[26] Isaac Gym: High Performance GPU-Based Physics Simulation For Robot Learning — http://arxiv.org/abs/2108.10470v2
[27] Isaac Lab: A GPU-Accelerated Simulation Framework for Multi-Modal Robot Learning — http://arxiv.org/abs/2511.04831v1
[28] Event-Enriched Image Analysis Grand Challenge at ACM Multimedia 2025 — http://arxiv.org/abs/2508.18904v1
[29] Xiaomi-Robotics-1: Scaling Vision-Language-Action Models with over 100K Hours of Real-World Trajectories — http://arxiv.org/abs/2607.15330v2
[30] Action Flow Matching for Continual Robot Learning — http://arxiv.org/abs/2504.18471v2
[31] Scalable Aerial GNSS Localization for Marine Robots — http://arxiv.org/abs/2505.04095v2
[32] Using Physiological Measures, Gaze, and Facial Expressions to Model Human Trust in a Robot Partner — http://arxiv.org/abs/2504.05291v1
[33] Toward Control of Wheeled Humanoid Robots with Unknown Payloads: Equilibrium Point Estimation via Real-to-Sim Adaptation — http://arxiv.org/abs/2403.10948v2


---

*Generated by research-bot · topic=`embodied-world-models` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading · model=`deepseek-v4-flash` · sources=33 · duration=167s · 2026-10-02T11:00:02+00:00*
