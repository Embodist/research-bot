# 具身智能（Embodied AI）前沿进展与奠基工作调研报告

> **报告日期**：2026-10-02（UTC）
> **领域**：具身智能（Embodied AI）/ 视觉-语言-动作模型（Vision-Language-Action, VLA）/ 机器人学习、仿真与 Sim2Real
> **检索源**：本次调研候选来源共 133 条（编号 [1]–[133]）。经主题相关性筛查，本报告仅引用其中与具身智能直接相关、且元数据可核验的编号；与主题无关或证据不可用的条目已剔除，剔除说明见文末「检索质量说明」
> **证据纪律**：所有引用数（citations）、star 数、榜单排名均直接取自候选块字段，未取到处一律写 `> 待核实`；本报告不引用 [1]–[133] 之外任何编号，不编造 URL 与数字

---

## 摘要（Executive Summary）

1. **范式已经切换，但切换的「基础设施层」比「模型层」更可核查。** 近两年具身智能的主线叙事是从模块化流水线 → 端到端模仿学习 → 基础模型范式，而候选证据中最扎实的一条是：物理模拟器（physical simulators）与世界模型（world models）被并列为实现具身智能的**两项基础使能技术** [32]。这与「VLA 模型本身」的证据强度形成对比——后者的候选条目多为单点技术改进，且普遍缺少热度数据。

2. **VLA 的研究重心已从「能否成功」转向「推理效率、鲁棒性与失败恢复」。** 代表性证据包括低资源推理包装器 BLURR [118]、推理时注意力引导 [116]、把 VLA 已有注意力头复用于路径偏差检测 [119]、以及 LIBERO-Para 对指令改写的鲁棒性诊断 [10] 与 LIBERO-RECOVER 对失败恢复的评测 [11]。

3. **仿真栈的工程收敛点明确指向 GPU 原生并行仿真。** Isaac Lab 被表述为 Isaac Gym 的自然继任者，把 GPU 原生机器人仿真扩展到大规模多模态学习时代 [81]；Isaac Sim 则被定位为可扩展 GPU 加速仿真与合成数据生成管线 [87]；更早的 Isaac Gym 是这一路线的起点 [83]。

4. **Sim2Real 的技术路线正在分化。** 除经典域随机化外，出现离线域随机化 [103]、视觉编码器预训练迁移 [98]、以扩散模型桥接深度观测 sim2real gap 的 RealD²iff [96]、以及面向人形全身控制的域随机化分析 [112] 等分支。同时出现「Sim2Real 评测本身缺位」的反思性论文 [94]。

5. **基准正在从「静态成功率」转向「扰动下的闭环鲁棒性」。** LIBERO 系列衍生出三条独立诊断线：[9]（视觉鲁棒性）、[10]（指令改写鲁棒性）、[11]（失败恢复），其中 [11] 明确指出 LIBERO 上 SOTA 已接近 100% 成功率，但近乎完美的表现**并不能推出真机可部署**。

6. **数据瓶颈是公认共识，但解决方案尚未收敛。** 「机器人数据难以扩展」被明确表述为具身智能与机器人进一步发展的关键瓶颈，从人类活动视频学习操作技能因此成为近年快速增长的方向 [34]；跨本体数据侧以 Open X-Embodiment [3] 与 DROID [2] 为代表性语料。

7. **争议与缺口集中在四处**：基准饱和与真机脱节 [11]、复现困难 [57]、仿真器对外部复现的门槛 [89][90]、以及具身 AI 已被单独体系化为「风险—攻击—防御」综述主题 [28] 所反映的安全治理化趋势。**必须强调：本次候选来源中缺失 PaLM-E / SayCan / Code as Policies / RT-1 等一手经典论文的检索条目，因此「模块化 → 端到端 → 基础模型」的具体谱系在本次证据下无法完整构建，相关段落已标注 `> 待核实`。**

---

## 一、关键前沿进展（近 1–2 年，2024Q4–2026Q3）

### 1.1 VLA 模型的「后训练时代」：效率、可解释性与鲁棒性

近一年 VLA 方向的可见变化，不是新模型架构的发布，而是围绕**已训好的 VLA 做推理侧与诊断侧的改造**。

| 条目 | 时间 | 一句话贡献 | 四类证据 |
|---|---|---|---|
| BLURR | 2025 | 轻量推理包装器，可插入现有 VLA 控制器，面向商品级 GPU 上的高频机器人控制与 Web 演示 [118] | **热度**：`> 待核实`（候选块未给 citations/star）<br>**权威**：arXiv 预印本（cs.RO），非同行评审 [118]<br>**关注度**：低——无引用数、无 star、无榜单可依<br>**推荐度**：★★★☆☆ 工程落地视角有价值，但缺第三方验证 |
| Inference-Time Attention Steering for VLA Driving Models | 2026 | 在 pre-softmax 注意力上加有界加性偏置，推理时把注意力导向安全关键目标，无需重训练 [116] | **热度**：`> 待核实`<br>**权威**：arXiv 预印本（cs.CV）[116]<br>**关注度**：低——无量化信号<br>**推荐度**：★★★☆☆ 思路（推理时可控）可迁移，但属自动驾驶域 |
| Your VLA Already Has Attention Heads For Path Deviation Detection | 2026 | 主张 VLA 内部已有可用于路径偏差检测的注意力头，针对视觉推理幻觉问题 [119] | **热度**：`> 待核实`<br>**权威**：arXiv 预印本（cs.RO）[119]<br>**关注度**：低<br>**推荐度**：★★★☆☆ 可解释性线索，需复现验证 |
| VLA-Thinker | 2026 | 通过 thinking-with-image 推理增强 VLA [123] | **热度**：`> 待核实`<br>**权威**：arXiv 预印本 [123]<br>**关注度**：低<br>**推荐度**：★★★☆☆ 与「具身推理链」热点相关，待全文核 |
| Evolve VLA into an Agent with On-the-fly Tool-use | 2026 | 把 VLA 演进为具备即时工具调用能力的 agent [121] | **热度**：`> 待核实`<br>**权威**：arXiv 预印本，v3 修订 [121]<br>**关注度**：低<br>**推荐度**：★★★☆☆ 反映 VLA→Agent 的融合趋势 |
| One Policy, Many Embodiments | 2026 | 统一的相机中心（camera-centric）动作几何预训练，面向异构本体操作 [132] | **热度**：`> 待核实`<br>**权威**：arXiv 预印本 [132]<br>**关注度**：低<br>**推荐度**：★★★★☆ 直击「跨本体统一动作空间」这一核心难题 |
| MiMo-Embodied | 2025 | X-Embodied 基础模型技术报告 [131] | **热度**：`> 待核实`<br>**权威**：技术报告（arXiv v2），非同行评审 [131]<br>**关注度**：中——「X-Embodied」命名指向跨本体基础模型主线，但无引用数据佐证<br>**推荐度**：★★★☆☆ 技术报告类，需交叉验证 |

> **待核实**：上表所有「关注度」判断均为低/中，依据是候选块中**完全没有**引用数、GitHub star、下载量或榜单排名字段。这不代表这些工作不重要，而代表本次检索未采集到可量化热度信号。

**综述层证据**：候选来源中确实存在多篇 VLA 综述（[120][122][124]），其中 [122] 与 [124] 标题完全相同、仅 DOI 不同，说明存在重复收录，引用时需注意。这类条目的权威性为「预印本 / Zenodo 归档」，`> 待核实` 其是否已被同行评审会议接收。

### 1.2 本体规模化律（Embodiment Scaling Laws）

- **[115]** 提出并检验「增加训练本体数量可提升对未见本体泛化」的假设，即具身规模化律。**热度**：`> 待核实`；**权威**：arXiv 预印本（cs.RO），v2 [115]；**关注度**：中——该假设若成立将直接影响数据采集策略，但候选块无引用数；**推荐度**：★★★★☆ 与「数据规模化」主线高度相关，是少见的把 scaling law 显式搬到本体维度的尝试。

### 1.3 具身导航侧：长程与 VLA 化

- **[22]** LongNav-R1 提出面向长程 VLA 导航的 horizon-adaptive 多轮 RL；**[23]** ABot-N0 是具身导航 VLA 基础模型技术报告。**热度**：均为 `> 待核实`；**权威**：均为 arXiv 预印本（技术报告性质），非同行评审 [22][23]；**关注度**：中——导航是 VLA 落地相对成熟的子域，但两项均无引用数据；**推荐度**：★★★☆☆ 可作为「VLA 向导航泛化」的样本，需核实真机结果。
- **[20]** 提出「Move to Understand」：把视觉 grounding 与主动探索耦合，用于高效具身导航。**权威**：arXiv 预印本（cs.CV）v2 [20]；**热度**：`> 待核实`；**关注度**：中；**推荐度**：★★★☆☆。

### 1.4 仿真基础设施的代际更替

- **Isaac Lab**：被明确表述为 Isaac Gym 的「natural successor」，把 GPU 原生机器人仿真范式扩展至大规模多模态学习，结合高保真 GPU 并行物理、照片级渲染与模块化可组合架构 [81]。
- **NVIDIA Isaac Sim**：定位为「可扩展、GPU 加速的机器人仿真」，并强调合成数据生成管线缓解高质量训练数据稀缺 [87]。
- **Isaac Gym**（2021）：GPU 并行物理仿真用于机器人学习的起点 [83]。

**四类证据（合并）**：**热度**：`> 待核实`（三条均无 citations/star 字段）；**权威**：Isaac Lab [81] 与 Isaac Sim [87] 为 arXiv 预印本，Isaac Gym [83] 为 arXiv 预印本 v2，三者均非同行评审，但其官方实现对应真实开源仓库（见第五章）；**关注度**：中——生态层面的实际使用面广为人知，但本报告不使用未采集到的 star 数作为依据；**推荐度**：★★★★★（Isaac Lab [81]）——作为当前 GPU 并行学习栈的事实基准，是工程选型必读。

---

## 二、方法谱系（模块化 / 端到端 / 基础模型 / 世界模型）

> **重要缺口声明**：本次候选来源中，**没有检索到**模块化流水线时代（如预编程 CAD 级流水线）之外的一手方法论文、也没有端到端模仿学习的代表作原文、更没有 VLA 基础模型的原始论文（如 RT-1/RT-2、PaLM-E、SayCan）。因此下表的「谱系归属」是基于综述类证据 [27][32][33][34] 与种子资源清单的**结构性描述**，凡涉及具体论文首创权与指标的判断，一律标注 `> 待核实`。

| 阶段 | 核心特征 | 支撑证据 | 证据强度 |
|---|---|---|---|
| **① 模块化流水线** | 感知 / 规划 / 控制分离，任务边界由人工定义 | [1] 早期 CAD 驱动的高层机器人编程需应对不可预测环境；[33] 把运动规划与控制定位为机器人与环境交互的基础能力 | [1] 为 arXiv 预印本（2013 年，历史文献）；[33] 为 IEEE TNNLS 同行评审期刊，**citations=8**（候选块字段）[33] → 权威性最高 |
| **② 端到端学习** | 从示教/交互直接学策略，减少人工接口 | [38] on-policy 模仿学习；[45] 单样本视觉模仿元学习；[48] 机器人操作模仿学习综述（同行评审期刊，DOI 10.1007/s41315-019-00103-5）[48]；[64] 从人类示教轨迹学习与「类人性」评估 [64] | [48] 为同行评审综述，权威中高；[38][45] 为经典预印本；热度均 `> 待核实`（候选块未给 citations） |
| **③ 基础模型范式** | 视觉-语言预训练骨干 + 动作头；跨任务/跨本体泛化 | [120] VLA 操作综述；[122]/[124] VLA 具身 AI 综述；[131] MiMo-Embodied 技术报告 [131]；[132] 跨本体统一动作几何预训练 [132] | 全部为预印本/技术报告，**无同行评审证据**，热度 `> 待核实` |
| **④ 世界模型** | 学习环境动力学表征，用于规划或替代真实交互 | [32] 明确把物理模拟器与世界模型并列为具身智能学习的两项基础使能技术 [32]；[41] 具身 AI 世界模型综合综述 [41]；[129][130] Physical AI: World Models and Embodied Intelligence [129][130] | [32] 为 arXiv 预印本 v3（v1 2025-07-01，v3 2025-09-03），非同行评审，热度 `> 待核实`；[41] 为 arXiv 2510.16732，`> 待核实` 是否已中稿 |

**谱系叙述（谨慎版）**：

- 从模块化到端到端的驱动因素，可被证据支持的部分是**数据与接口瓶颈**：[34] 明确指出机器人数据难以扩展（scaling robot data）是瓶颈，并催生「从人类视频学习操作技能」这一快速增长的研究方向 [34]。**权威**：arXiv 预印本（cs.RO，v1 2026-04-30），非同行评审；**热度**：`> 待核实`；**关注度**：中；**推荐度**：★★★☆☆。
- 端到端 → 基础模型的转折，在本次证据中只能被**间接**支持：[27]《Aligning Cyber Space with Physical World: A Comprehensive Survey on Embodied AI》v8 是覆盖该演进的大型综述 [27]，但候选块未提供其分类骨架细节，因此该转折的具体技术因果链 `> 待核实`。
- 世界模型分支的定位证据：[32] 与 [41] 均把世界模型作为独立技术线，`> 待核实` 二者对「世界模型是否已能替代真实交互」是否给出正面结论。

---

## 三、仿真平台与基准对比

### 3.1 主流仿真器 / 物理引擎

| 平台 | 年份 | 机构 | 定位 | 热度 | 权威 | 关注度 | 推荐度 | 链接 |
|---|---|---|---|---|---|---|---|---|
| **Isaac Lab** | 2025 | NVIDIA | GPU 原生并行物理 + 照片级渲染 + 模块化组合，面向大规模多模态学习 [81] | `> 待核实` | arXiv 预印本（cs.RO），非同行评审 [81] | 中（生态事实标准，但无 star/citations 数据） | ★★★★★ | https://arxiv.org/abs/2511.04831v1 ；代码见 [isaac-sim/IsaacLab](https://github.com/isaac-sim/IsaacLab) |
| **NVIDIA Isaac Sim** | 2026 | NVIDIA | 可扩展 GPU 加速仿真 + 合成数据生成，缓解训练数据稀缺 [87] | `> 待核实` | arXiv 预印本（cs.RO）[87] | 中 | ★★★★☆ | https://arxiv.org/abs/2606.03551v1 |
| **Isaac Gym** | 2021 | NVIDIA | GPU 并行物理仿真先驱，Isaac Lab 前身 [83] | `> 待核实` | arXiv 预印本 v2 [83] | 中（历史奠基地位） | ★★★★☆ | https://arxiv.org/abs/2108.10470v2 |
| **Genesis** | 2024+ | Genesis-Embodied-AI | 生成式物理仿真引擎 | `> 待核实` | 仅开源仓库，**未在本次引用列表中取得论文条目** | `> 待核实` | ★★★☆☆（工程可用性高，但缺可核查论文证据） | https://github.com/Genesis-Embodied-AI/Genesis |
| **ManiSkill** | — | haosulab | GPU 并行操作基准 | `> 待核实` | 仅开源仓库，**未在本次引用列表中取得论文条目** | `> 待核实` | ★★★☆☆ | https://github.com/haosulab/ManiSkill |
| **TacEx** | 2024 | — | 在 Isaac Sim 中结合软体与视触觉仿真，实现 GelSight 触觉仿真 [85] | `> 待核实` | arXiv 预印本 [85] | 低（无量化信号） | ★★★☆☆ | https://arxiv.org/abs/2411.04776v1 |
| **BEHAVIOR-1K / OmniGibson** | 2024 | Stanford | 1000 项日常活动的仿真环境与基准 [30] | `> 待核实` | arXiv 预印本 v1 [30] | 中（大规模人本基准，但无 star/citations 数据） | ★★★★☆ | https://arxiv.org/abs/2403.09227v1 ；代码 https://github.com/StanfordVL/BEHAVIOR-1K |
| **AssemblyGrid v1** | 2026 | — | 多机器人产线基准，含临时联盟、局部信息与几何约束 [66] | `> 待核实` | arXiv 预印本 [66] | 低 | ★★☆☆☆ | https://arxiv.org/abs/2609.16075 |

> **对比要点**：从 [81][87][83] 三条证据可确认的**唯一无争议趋势**是「GPU 并行 + 渲染保真度 + 模块化 API」三者的合流；但**没有任何候选来源给出仿真器之间的定量吞吐/精度对比表**，因此「谁更快、谁更准」在本次证据下 `> 待核实`。

### 3.2 仿真侧迁移研究的代表性设置

- **[89

## 参考来源

[1] High-level robot programming based on CAD: dealing with unpredictable environments — http://arxiv.org/abs/1309.2086v1
[2] DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset — http://arxiv.org/abs/2403.12945v2
[3] Open X-Embodiment: Robotic Learning Datasets and RT-X Models — http://arxiv.org/abs/2310.08864v9
[4] The RSNA Abdominal Traumatic Injury CT (RATIC) Dataset — http://arxiv.org/abs/2405.19595v1
[5] The RSNA Lumbar Degenerative Imaging Spine Classification (LumbarDISC) Dataset — http://arxiv.org/abs/2506.09162v1
[6] Waymo Open Dataset: Panoramic Video Panoptic Segmentation — http://arxiv.org/abs/2206.07704v1
[7] Exploring Large Language Models to Facilitate Variable Autonomy for Human-Robot Teaming — http://arxiv.org/abs/2312.07214v3
[8] DROID-SLAM in the Wild — http://arxiv.org/abs/2603.19076v1
[9] LIBERO-VPro: Benchmarking Closed-Loop Visual Robustness of Robotic Foundation Models — http://arxiv.org/abs/2609.24350v1
[10] LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models — http://arxiv.org/abs/2603.28301v3
[11] LIBERO-RECOVER: Beyond Task Success Towards Failure Recovery in Robotic Manipulation Models — http://arxiv.org/abs/2609.05178v3
[12] Benchmarking Simulated Robotic Manipulation through a Real World Dataset — http://arxiv.org/abs/1911.01557v2
[13] ManipBench: Benchmarking Vision-Language Models for Low-Level Robot Manipulation — http://arxiv.org/abs/2505.09698v2
[14] Leveraging Passive Compliance of Soft Robotics for Physical Human-Robot Collaborative Manipulation — http://arxiv.org/abs/2504.08184v1
[15] Grasp and Motion Planning for Dexterous Manipulation for the Real Robot Challenge — http://arxiv.org/abs/2101.02842v1
[16] Towards Long-Horizon Vision-Language Navigation: Platform, Benchmark and Method — http://arxiv.org/abs/2412.09082v3
[17] A Simple Observer for Gyro and Accelerometer Biases in Land Navigation Systems — http://arxiv.org/abs/1501.06618v1
[18] The Road to Know-Where: An Object-and-Room Informed Sequential BERT for Indoor Vision-Language Navigation — http://arxiv.org/abs/2104.04167v2
[19] Navigation in the Ancient Mediterranean and Beyond — http://arxiv.org/abs/1708.07700v3
[20] Move to Understand a 3D Scene: Bridging Visual Grounding and Exploration for Efficient and Versatile Embodied Navigation — http://arxiv.org/abs/2507.04047v2
[21] Underwater Doppler Navigation with Self-calibration — http://arxiv.org/abs/1509.02054v1
[22] LongNav-R1: Horizon-Adaptive Multi-Turn RL for Long-Horizon VLA Navigation — http://arxiv.org/abs/2602.12351v2
[23] ABot-N0: Technical Report on the VLA Foundation Model for Versatile Embodied Navigation — http://arxiv.org/abs/2602.11598v1
[24] Editorial: Narrow and general intelligence: embodied, self-referential social cognition and novelty production in humans, AI and robots — https://doi.org/10.3389/frobt.2025.1766766
[25] One-Shot Reinforcement Learning for Robot Navigation with Interactive Replay — http://arxiv.org/abs/1711.10137v2
[26] Physical AI: The Next Frontier in AI and Robotics to Build Truly Autonomous Machines — https://doi.org/10.20944/preprints202604.0549.v1
[27] Aligning Cyber Space with Physical World: A Comprehensive Survey on Embodied AI — http://arxiv.org/abs/2407.06886v8
[28] Safety in Embodied AI: A Survey of Risks, Attacks, and Defenses — http://arxiv.org/abs/2605.02900v2
[29] Mapping AI Risk Mitigations: Evidence Scan and Preliminary AI Risk Mitigation Taxonomy — http://arxiv.org/abs/2512.11931v1
[30] BEHAVIOR-1K: A Human-Centered, Embodied AI Benchmark with 1,000 Everyday Activities and Realistic Simulation — http://arxiv.org/abs/2403.09227v1
[31] Vision Mamba: A Comprehensive Survey and Taxonomy — http://arxiv.org/abs/2405.04404v1
[32] A Survey: Learning Embodied Intelligence from Physical Simulators and World Models — http://arxiv.org/abs/2507.00917v3
[33] A Survey on Learning Motion Planning and Control for Mobile Robots: Toward Embodied Intelligence — https://doi.org/10.1109/tnnls.2026.3656889
[34] Robot Learning from Human Videos: A Survey — http://arxiv.org/abs/2604.27621v1
[35] A Comprehensive Review of Generative Physical Artificial Intelligence — https://doi.org/10.1109/jiot.2026.3671268
[36] End-to-End Reinforcement Learning for Torque Based Variable Height Hopping — http://arxiv.org/abs/2307.16676v2
[37] A Comprehensive Review of Physical Artificial Intelligence — https://doi.org/10.36227/techrxiv.176739762.23746519/v1
[38] On-Policy Robot Imitation Learning from a Converging Supervisor — http://arxiv.org/abs/1907.03423v7
[39] A Survey on Predictive Safety in Embodied AI — https://doi.org/10.2139/ssrn.6562019
[40] Emotion in Reinforcement Learning Agents and Robots: A Survey — http://arxiv.org/abs/1705.05172v1
[41] A Comprehensive Survey on World Models for Embodied AI — https://doi.org/10.48550/arxiv.2510.16732
[42] Robot Learning from Human Videos: A Survey — https://doi.org/10.48550/arxiv.2604.27621
[43] Imitation Learning for End to End Vehicle Longitudinal Control with Forward Camera — http://arxiv.org/abs/1812.05841v1
[44] Vision-Based Tactile Intelligence for Robotics: Sensing, Learning, and Embodied Manipulation — https://doi.org/10.48550/arxiv.2608.15490
[45] One-Shot Visual Imitation Learning via Meta-Learning — http://arxiv.org/abs/1709.04905v1
[46] Active learning for data streams: a survey — http://arxiv.org/abs/2302.08893v4
[47] Learning to Discern: Imitating Heterogeneous Human Demonstrations with Preference and Representation Learning — http://arxiv.org/abs/2310.14196v1
[48] Survey of imitation learning for robotic manipulation — https://doi.org/10.1007/s41315-019-00103-5
[49] ROBEL: Robotics Benchmarks for Learning with Low-Cost Robots — http://arxiv.org/abs/1909.11639v3
[50] Benchmarking Reinforcement Learning Algorithms on Real-World Robots — http://arxiv.org/abs/1809.07731v1
[51] Reproducibility of Benchmarked Deep Reinforcement Learning Tasks for Continuous Control — http://arxiv.org/abs/1708.04133v1
[52] Reproducibility in Machine Learning for Health — http://arxiv.org/abs/1907.01463v1
[53] On the Similarities of Embeddings in Contrastive Learning — http://arxiv.org/abs/2506.09781v2
[54] Off-Policy Actor-Critic with Sigmoid-Bounded Entropy for Real-World Robot Learning — https://arxiv.org/abs/2601.15761
[55] Multi-objective Model-based Policy Search for Data-efficient Learning with Sparse Rewards — http://arxiv.org/abs/1806.09351v3
[56] SURREAL: Open-Source Reinforcement Learning Framework and Robot Manipulation Benchmark — https://www.semanticscholar.org/paper/050a89a91b3e828c841972a81f17807f82c79713
[57] CoLI: A Reproducible Platform for Continuum Robot Learning via Monolithic 3D Printing and Isomorphic Teleoperation — https://arxiv.org/abs/2606.20389
[58] RoAd-RL: A Unified Library and Benchmark for Robust Adversarial Reinforcement Learning — https://arxiv.org/abs/2606.29867
[59] Competing Visions of Ethical AI: A Case Study of OpenAI — http://arxiv.org/abs/2601.16513v1
[60] Cross-Sensor and Cross-Population Generalization of Deep Learning Models for Digital Mammography: A Controlled Four-Country Benchmark of Five Backbone Architectures with Statistical Significance Testing — https://doi.org/10.3390/s26123911
[61] PANORAMA: The Rise of Omnidirectional Vision in the Embodied AI Era — http://arxiv.org/abs/2509.12989v1
[62] ManipulationNet: An Infrastructure for Benchmarking Real-World Robot Manipulation with Physical Skill Challenges and Embodied Multimodal Reasoning — https://arxiv.org/abs/2603.04363
[63] Toward Maturity-Based Certification of Embodied AI: Quantifying Trustworthiness Through Measurement Mechanisms — http://arxiv.org/abs/2601.03470v2
[64] Robot Learning from Human Demonstrations: Handwritten Alphabet Trajectories and Human-Likeness Evaluation — https://arxiv.org/abs/2608.06221
[65] Faith in AI can narrow the futures individuals consider — http://arxiv.org/abs/2603.28944v2
[66] AssemblyGrid v1: A Benchmark for Multi-Robot Production with Temporary Coalitions, Local Information, and Geometric Constraints — https://arxiv.org/abs/2609.16075
[67] Foundations of GenIR — http://arxiv.org/abs/2501.02842v1
[68] Boosting Robotic Manipulation Generalization with Minimal Costly Data — https://doi.org/10.48550/arxiv.2503.19516
[69] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1
[70] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1
[71] TRUST 2025: SCRITA and RTSS @ RO-MAN 2025 — http://arxiv.org/abs/2509.11402v1
[72] LLM-based ambiguity detection in natural language instructions for collaborative surgical robots — http://arxiv.org/abs/2507.11525v1
[73] HDDL 2.1: Towards Defining a Formalism and a Semantics for Temporal HTN Planning — http://arxiv.org/abs/2306.07353v1
[74] LongEval at CLEF 2025: Longitudinal Evaluation of IR Model Performance — http://arxiv.org/abs/2503.08541v1
[75] Autonomous Mobile Robot Path Planning Techniques—A Review: Metaheuristic and Cognitive Techniques — https://doi.org/10.3390/robotics15010023
[76] Approximate Computing for Robotic path planning -- Experimentation, Case Study and Practical Implications — http://arxiv.org/abs/2104.05773v2
[77] Decremental Dynamics Planning for Robot Navigation — https://doi.org/10.1109/iros60139.2025.11246580
[78] Construction robotics: a systematic review of robot types, applications and human robot collaborations — https://doi.org/10.1016/j.rineng.2026.110406
[79] The Synthesis of Optimal Control Laws Using Isaacs' Method for the Solution of Differential Games — http://arxiv.org/abs/2112.10849v2
[80] Artificial Intelligence and Orthopaedic Prosthetic Planning: A State-of-the-Art Review and Evolving Liability Perspectives — https://doi.org/10.3390/sci8020027
[81] Isaac Lab: A GPU-Accelerated Simulation Framework for Multi-Modal Robot Learning — http://arxiv.org/abs/2511.04831v1
[82] Social assistive robotics as an enabling technology for the inclusion of children with ASD in school settings: a systematic literature review — https://doi.org/10.1108/jet-01-2026-0003
[83] Isaac Gym: High Performance GPU-Based Physics Simulation For Robot Learning — http://arxiv.org/abs/2108.10470v2
[84] Agentic Large-Language-Model Systems in Medicine: A Systematic Review and Taxonomy — https://doi.org/10.36227/techrxiv.175736231.12300949/v1
[85] TacEx: GelSight Tactile Simulation in Isaac Sim -- Combining Soft-Body and Visuotactile Simulators — http://arxiv.org/abs/2411.04776v1
[86] Applications of artificial intelligence for real-world evidence generation: a protocol for a living scoping review — https://doi.org/10.1136/bmjopen-2025-109725
[87] NVIDIA Isaac Sim: Enabling Scalable, GPU-Accelerated Simulation for Robotics — http://arxiv.org/abs/2606.03551v1
[88] Plastic and Reconstructive Surgery Best Paper Awards 2025 — https://doi.org/10.1097/prs.0000000000012340
[89] Sim-to-Real gap in RL: Use Case with TIAGo and Isaac Sim/Gym — http://arxiv.org/abs/2403.07091v2
[90] Sim-to-Real Transfer for Mobile Robots with Reinforcement Learning: from NVIDIA Isaac Sim to Gazebo and Real ROS 2 Robots — http://arxiv.org/abs/2501.02902v1
[91] ISAAC Newton: Input-based Approximate Curvature for Newton's Method — http://arxiv.org/abs/2305.00604v1
[92] Perspectives on Sim2Real Transfer for Robotics: A Summary of the R:SS 2020 Workshop — http://arxiv.org/abs/2012.03806v1
[93] Robot Manipulation with GPT-6-Astra: Body Knowledge, Experience Reuse, Emergent Skills, and Sim2Real Transfer — http://arxiv.org/abs/2609.31770v1
[94] Robot Policy Evaluation for Sim-to-Real Transfer: A Benchmarking Perspective — http://arxiv.org/abs/2508.11117v1
[95] The Importance and the Limitations of Sim2Real for Robotic Manipulation in Precision Agriculture — http://arxiv.org/abs/2008.03983v1
[96] RealD$^2$iff: Bridging Real-World Gap in Robot Manipulation via Depth Diffusion — http://arxiv.org/abs/2511.22505v2
[97] Sim2Real Transfer for Audio-Visual Navigation with Frequency-Adaptive Acoustic Field Prediction — http://arxiv.org/abs/2405.02821v2
[98] Bridging the Sim2Real Gap: Vision Encoder Pre-Training for Visuomotor Policy Transfer — http://arxiv.org/abs/2501.16389v2
[99] A rich bounty of AGN in the 9 square degree Bootes survey: high-z obscured AGN and large-scale structure — http://arxiv.org/abs/astro-ph/0611654v1
[100] AIn't Nothing But a Survey? Using Large Language Models for Coding German Open-Ended Survey Responses on Survey Motivation — http://arxiv.org/abs/2506.14634v3
[101] Understanding Domain Randomization for Sim-to-real Transfer — http://arxiv.org/abs/2110.03239v2
[102] Sim-to-Real Transfer in Deep Reinforcement Learning for Bipedal Locomotion — http://arxiv.org/abs/2511.06465v1
[103] DROPO: Sim-to-Real Transfer with Offline Domain Randomization — http://arxiv.org/abs/2201.08434v2
[104] The Methanol Multibeam Survey — http://arxiv.org/abs/1210.0979v1
[105] A Survey on Cross-Domain Sequential Recommendation — http://arxiv.org/abs/2401.04971v4
[106] The Dark Energy Survey — http://arxiv.org/abs/astro-ph/0510346v1
[107] Sim-to-Real Transfer in Deep Reinforcement Learning for Robotics: a Survey — https://doi.org/10.1109/ssci47803.2020.9308468
[108] A Survey on Sim-to-Real Transfer Methods for Robotic Manipulation — https://doi.org/10.1109/sisy62279.2024.10737545
[109] Real-World Robotic Perception and Control Using Synthetic Data — https://openalex.org/W2973454014
[110] Humanoid Whole-Body Badminton via an Annealed Reinforcement Learning Curriculum — http://arxiv.org/abs/2511.11218v4
[111] Data-Driven Optimization of Discontinuous and Continuous Fiber Composite Processes Using Machine Learning: A Review — https://doi.org/10.3390/polym17182557
[112] The Role of Domain Randomization in Training Diffusion Policies for Whole-Body Humanoid Control — http://arxiv.org/abs/2411.01349v1
[113] Random Sampling of Quantum States: a Survey of Methods And Some Issues Regarding the Overparametrized Method — https://openalex.org/W1935436813
[114] Robot Trains Robot: Automatic Real-World Policy Adaptation and Learning for Humanoids — http://arxiv.org/abs/2508.12252v2
[115] Towards Embodiment Scaling Laws in Robot Locomotion — http://arxiv.org/abs/2505.05753v2
[116] Inference-Time Attention Steering for Vision-Language-Action Driving Models — http://arxiv.org/abs/2608.17095v1
[117] Compositional Context Fine-Tuning Vision-Language Model for Complex Assembly Action Understanding from Videos — http://arxiv.org/abs/2607.10797v1
[118] BLURR: A Boosted Low-Resource Inference for Vision-Language-Action Models — http://arxiv.org/abs/2512.11769v1
[119] Your Vision-Language-Action Model Already Has Attention Heads For Path Deviation Detection — http://arxiv.org/abs/2603.13782v1
[120] Survey of Vision-Language-Action Models for Embodied Manipulation — http://arxiv.org/abs/2508.15201v2
[121] Evolve Vision-Language-Action Model into an Agent with On-the-fly Tool-use — http://arxiv.org/abs/2608.14047v3
[122] Vision-Language-Action Models for Embodied AI: A Survey of Robotics, Manipulation, and Autonomous Agents — https://doi.org/10.5281/zenodo.21366292
[123] VLA-Thinker: Boosting Vision-Language-Action Models through Thinking-with-Image Reasoning — http://arxiv.org/abs/2603.14523v1
[124] Vision-Language-Action Models for Embodied AI: A Survey of Robotics, Manipulation, and Autonomous Agents — https://doi.org/10.5281/zenodo.21366291
[125] Multimodal Large Language Models: A Survey of Vision-Language Integration, Architectures, and Applications — https://doi.org/10.5281/zenodo.21365121
[126] Multimodal Large Language Models: A Survey of Vision-Language Integration, Architectures, and Applications — https://doi.org/10.5281/zenodo.21365120
[127] Editorial: Digital transformation and smart technologies for sustainable built environment: innovations, applications and future pathways — https://doi.org/10.1108/sasbe-02-2026-689
[128] Generating Facial Expressions to Understand Internal Representations of Facial Expressions in Large Language Models — https://doi.org/10.17605/osf.io/qpcy5
[129] Physical AI: World Models and Embodied Intelligence — https://doi.org/10.5281/zenodo.21332611
[130] Physical AI: World Models and Embodied Intelligence — https://doi.org/10.5281/zenodo.21332610
[131] MiMo-Embodied: X-Embodied Foundation Model Technical Report — http://arxiv.org/abs/2511.16518v2
[132] One Policy, Many Embodiments: Unified Camera-Centric Action Geometry Pre-training for Heterogeneous Embodied Manipulation — http://arxiv.org/abs/2608.26058v1
[133] ME-VLM: A Unified VLM for Embodied Cognition and Agent Coordination — http://arxiv.org/abs/2609.24526v2


---

*Generated by research-bot · topic=`embodied-ai` · depth=`standard` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading · model=`deepseek-v4-flash` · sources=133 · duration=386s · 2026-10-02T22:22:21+00:00*
