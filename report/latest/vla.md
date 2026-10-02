# Vision-Language-Action (VLA) 基础模型调研报告：方法脉络、开源工程与真机评测前沿

**报告日期**：2026-10-02（UTC）
**领域**：具身智能 / Vision-Language-Action (VLA) / 机器人基础模型（Robot Foundation Models）
**检索与证据源**：本批次候选来源共 **124 条**（编号 [1]–[124]）。经人工清点，与 VLA/机器人策略学习*直接相关*的约 **55 条**；其余为同批次召回中混入的无关领域条目（LLM 微调、信息检索评测、天文、实时系统等），本报告已显式排除，并在必要处说明其对结论的支持力为零。
**证据等级约定**：A = 同行评审论文 / 官方技术报告；B = arXiv 预印本 / 官方仓库 / 官方数据集主页；C = 第三方复现与榜单；D = 社区二手解读；E = 不可访问。本批证据以 **B 级（arXiv 预印本）为主**，结构化抽取中绝大多数条目 `confidence = low`，报告中已逐条标注。

---

## 摘要（Executive Summary）

1. **本批证据的整体强度有限，必须先声明。** 124 条候选中约 55 条与 VLA 直接相关，但结构化抽取对绝大多数条目给出的 `confidence` 为 `low`，且 **heat 字段（引用数/star）几乎全部为空**；只有 [13]（citations=31）、[17]（citations=39）两条带真实引用数字。因此本报告的结论以"**趋势识别**"为主，**不提供 SOTA 排名或量化胜负结论**。

2. **动作表征正在从"离散动作 token"向"连续生成式动作头"迁移，但离散路线并未退场，而是被改良。** 连续一侧涌现 Flow Matching 策略 [74]、扩散式动作模型 [35][17][14]、无扩散的配对表征预测（JEPA Policy）[39]；离散一侧则通过随机化与顺序化 token 优化自回归 VLA，代表为 TOAST [16]、Ordered Action Tokens [18]、Behavior-Aligned Action Tokenization [12]。

3. **跨本体（cross-embodiment）已成为独立的方法学议题，而非附属实验。** 本批证据覆盖统一动作/手部空间 [1][6]、人类-机器人统一表征 [8]、潜动作模型 [20][13]、扩散 Transformer 跨本体策略 [15]、统一视频-动作模型 [4]，以及"本体数量是否构成 scaling law"这一更根本的问题 [2]。

4. **真机评测与仿真榜单之间存在结构性、被明确论证的落差**，这是本批证据中质量最高的一条结论：[49] 指出机器人本质是真机问题而通用策略的真机评测滞后，[62] 直接批判"固定任务/集中式挑战赛"的重标准化路线不可扩展，并提出分布式真机评测。但 **两者均未给出任何可比较的量化成功率数字**，因此"差距有多大"在本批证据中**无法回答**（见第六章）。

5. **工程实践侧的证据最薄弱。** 与"VLA 微调与部署门槛"最相关的候选条目中，[79][93][115] 直接针对 VLA 但结构化抽取仅提供了标题或极短摘要；而 [87][88][89][90][91][92] 这批 LoRA 论文**全部不属于 VLA 领域**（LLM 微调、视频生成、CNN 量化、跨语言对齐），不能作为 VLA 工程证据使用。显存、推理频率、真机延迟的具体数字在本批证据中**完全缺失**。

6. **失败模式研究正在成为一个独立子方向**：语言被视觉覆盖的反事实失败 [110]、导航路径偏离的注意力头探测 [112]、推理期注意力引导 [25]、以及失败恢复策略 [111]。

---

## 一、关键前沿进展（近 12-24 个月）

> 判定口径：以结构化抽取中标注的 `year` 字段为准，并核对 arXiv 编号所对应的提交月份。2025–2026 年条目视为"最新进展"；2024 年及以前视为"经典/奠基"。

### 1.1 动作表征：离散 token 的改良 vs. 连续生成头的兴起

**连续生成侧。** [74] *VITA: Vision-to-Action Flow Matching Policy*（2025）标题即表明采用 flow matching 直接由视觉生成动作；[17] *3DFlowAction*（2025）以 3D flow world model 学习跨本体操作，是候选块中**唯一带真实引用数的前沿条目之一（citations=39）**[17]；[14] *Geometric Action Model for Robot Policy Learning*（2026）与 [15] *Tenma: Robust Cross-Embodiment Robot Manipulation with Diffusion Transformer*（2025）代表扩散/几何动作建模在跨本体上的推进；[39] *JEPA Policy*（2026）则明确以"**diffusion-free**"为卖点，用"动作块 + 其观测到的未来表征"配对监督替代扩散生成，摘要指出标准行为克隆并未显式约束与动作块配对的未来表征 [39]。

> 热度证据：仅 [17] 有 citations=39 [17]；[74][14][15][39] 的引用数 `> 待核实`。
> 权威证据：[17][14][39] 标注为 arXiv `cs.RO` 预印本；[15] 无 venue 字段。均非同行评审 [14][15][17][39][74]。
> 关注度：**中**——依据：[17] citations=39 为候选块中最高信号之一；其余条目无引用/star/榜单信号 [14][15][39][74]。
> 推荐度：★★★☆☆——概念上重要（代表"去扩散化"与"几何/流表征"两条相邻路线），但仅有标题级证据，需精读全文后方可采信 [14][39][74]。

**离散 token 侧。** [16] *TOAST: Stochastic Robot Action Tokenization for Autoregressive VLA*（2026）与 [18] *Ordered Action Tokens for Visuomotor Policy Learning*（2026）、[12] *Behavior-Aligned Action Tokenization for Robot Policy Learning*（2026）三条共同指向一个判断：**自回归离散动作并未被淘汰，研究者正通过"随机化 token 化"与"顺序敏感 token 化"来修补其固有缺陷**（离散化损失、token 顺序无语义、采样单一）。[12][16][18] 均为 2026 年新预印本。

> 热度证据：`> 待核实`（[12][16][18] 候选块均未提供引用数或下载量）。
> 权威证据：均为 arXiv 预印本，非同行评审 [12][16][18]。
> 关注度：**低**——依据：无引用/star/榜单信号，且均为极新预印本（2026 年）。
> 推荐度：★★★☆☆——若研究动作 tokenization 的具体设计取舍，这三条是当前最直接的一手线索，但证据强度不足以支撑"哪种 tokenization 更优"的结论 [12][16][18]。

### 1.2 通用策略与开源基础模型

[81] *GR00T N1: An Open Foundation Model for Generalist Humanoid Robots*（2025）是候选块中少见的、标题即表明"开放基础模型 + 通用人形"定位的工作 [81]。[114] *VLA-Adapter*（2025）提出"tiny-scale VLA"的有效范式，指向**小参数规模 VLA 的可行性**；[19] *BLM1*（2025）主张跨空间、跨任务、跨本体的"boundless large model"；[115] *From Foundation to Application: Improving VLA Models in Practice*（2026）标题直指从基础模型到落地应用的落差。

> 热度证据：`> 待核实`（[19][81][114][115] 候选块均未提供引用数/star/下载量）。
> 权威证据：均为 arXiv 预印本；[81] 为 NVIDIA 系工作但候选块未标注 peer-review venue，故按 B 级处理 [81]。
> 关注度：**中**——依据：[81] 以"人形通用基础模型"为定位，属当时热点方向；[114] 指向轻量化 VLA 这一工程强需求。但均无引用数/star 等硬信号 [81][114][115]。
> 推荐度：★★★★☆——[81][114][115] 分别覆盖人形、轻量、落地三个高相关维度，建议优先精读全文 [81][114][115]。

### 1.3 推理效率与实时性：VLA 落地的硬约束被单独提出

[29] *BLURR*（2025）摘要明确指出 VLA 的推理栈"often too heavy for responsive web demos or high frequency robot control on commodity GPUs"，并提出可插入现有 VLA 控制器的轻量推理封装 [29]；[69] *Running VLAs at Real-time Speed*（2025）标题直接对应"实时速度"这一工程瓶颈 [69]；[114] 亦从模型规模切入 [114]。此外 [34] *OnlineCache*（2026）针对扩散推理的动态缓存与纠错，虽非 VLA 专用，但属扩散策略推理加速的相邻证据 [34]。

> 热度证据：`> 待核实`（[29][69] 候选块未提供引用数/star）。
> 权威证据：arXiv `cs.RO` 预印本，非同行评审 [29][69]。
> 关注度：**高**——依据：推理频率与显存是 VLA 真机部署的第一道门槛，[29][69][114] 在同批次中集中出现，反映社区关注点从"能力"转向"可运行"。[29][69][114]
> 推荐度：★★★★☆——直接对应"真机部署门槛"这一研究目标，[29] 的摘要给出了问题陈述的原文表述，是工程实践章节最可用的一手材料 [29]。

### 1.4 从端到端策略到"智能体化 VLA"：工具注入范式

[71] *Evolve Vision-Language-Action Model into an Agent with On-the-fly Tool-use*（2026）提出 ART（Agentic Robot with Tool-use），摘要称其为一种 **tool-injection 框架**，可将任意 VLA 模型调优以调用现成工具模块，覆盖低层视觉、高层 affordance 与本体增强 [71]。这代表一条与"扩大端到端模型"相反的技术路线：**把不可控的端到端能力外包给可验证工具，模型只负责调度**。

> 热度证据：`> 待核实`。
> 权威证据：arXiv `cs.RO` 预印本（[71] URL 标注 v3，说明经过多轮修订），非同行评审 [71]。
> 关注度：**中**——依据：题目切中"端到端 VLA 可控性差"的争议点，但无引用/榜单信号 [71]。
> 推荐度：★★★☆☆——思路有区分度，值得与端到端路线对比阅读，但

## 参考来源

[1] Cross-Embodiment Robot Manipulation via a Unified Hand Action Space — http://arxiv.org/abs/2607.03570v1
[2] Towards Embodiment Scaling Laws in Robot Locomotion — http://arxiv.org/abs/2505.05753v2
[3] Technical Report for Ego4D Long-Term Action Anticipation Challenge 2025 — http://arxiv.org/abs/2506.02550v2
[4] Unified Video Action Model — http://arxiv.org/abs/2503.00200v3
[5] Help or Hindrance: Understanding the Impact of Robot Communication in Action Teams — http://arxiv.org/abs/2506.08892v3
[6] Learning a Unified Latent Space for Cross-Embodiment Robot Control — http://arxiv.org/abs/2601.15419v1
[7] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1
[8] Motion Tracks: A Unified Representation for Human-Robot Transfer in Few-Shot Imitation Learning — https://arxiv.org/abs/2501.06994
[9] LLM-based ambiguity detection in natural language instructions for collaborative surgical robots — http://arxiv.org/abs/2507.11525v1
[10] Humanoid Policy ~ Human Policy — https://arxiv.org/abs/2503.13441
[11] T (R,O) Grasp: Efficient Graph Diffusion of Robot-Object Spatial Transformation for Cross-Embodiment Dexterous Grasping — https://arxiv.org/abs/2510.12724
[12] Behavior-Aligned Action Tokenization for Robot Policy Learning — http://arxiv.org/abs/2609.27513v1
[13] Latent Action Diffusion for Cross-Embodiment Manipulation — https://arxiv.org/abs/2506.14608
[14] Geometric Action Model for Robot Policy Learning — http://arxiv.org/abs/2606.17046v2
[15] Tenma: Robust Cross-Embodiment Robot Manipulation with Diffusion Transformer — https://arxiv.org/abs/2509.11865
[16] TOAST: Stochastic Robot Action Tokenization for Autoregressive Vision-Language-Action Models — http://arxiv.org/abs/2610.00899v1
[17] 3DFlowAction: Learning Cross-Embodiment Manipulation from 3D Flow World Model — https://arxiv.org/abs/2506.06199
[18] Ordered Action Tokens for Visuomotor Policy Learning — http://arxiv.org/abs/2607.21670v1
[19] BLM1: A Boundless Large Model for Cross-Space, Cross-Task, and Cross-Embodiment Learning — https://arxiv.org/abs/2510.24161
[20] CLAM: Continuous Latent Action Models for Robot Learning from Unlabeled Demonstrations — http://arxiv.org/abs/2505.04999v2
[21] X-Nav: Learning End-to-End Cross-Embodiment Navigation for Mobile Robots — https://arxiv.org/abs/2507.14731
[22] High-level robot programming based on CAD: dealing with unpredictable environments — http://arxiv.org/abs/1309.2086v1
[23] Explainable Machine Learning for Public Policy: Use Cases, Gaps, and Research Directions — http://arxiv.org/abs/2010.14374v3
[24] End-User Programming of Low- and High-Level Actions for Robotic Task Planning — http://arxiv.org/abs/2103.14342v1
[25] Inference-Time Attention Steering for Vision-Language-Action Driving Models — http://arxiv.org/abs/2608.17095v1
[26] RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control — http://arxiv.org/abs/2307.15818v1
[27] Compositional Context Fine-Tuning Vision-Language Model for Complex Assembly Action Understanding from Videos — http://arxiv.org/abs/2607.10797v1
[28] Proceedings of the Dialogue Robot Competition 2023 — http://arxiv.org/abs/2312.14430v5
[29] BLURR: A Boosted Low-Resource Inference for Vision-Language-Action Models — http://arxiv.org/abs/2512.11769v1
[30] Overview of AuTexTification at IberLEF 2023: Detection and Attribution of Machine-Generated Text in Multiple Domains — http://arxiv.org/abs/2309.11285v1
[31] A Tricycle Model to Accurately Control an Autonomous Racecar with Locked Differential — http://arxiv.org/abs/2312.14808v1
[32] Soft-Minimum Barrier Functions for Safety-Critical Control Subject to Actuation Constraints — http://arxiv.org/abs/2304.00693v2
[33] Diffusion Policy Policy Optimization — http://arxiv.org/abs/2409.00588v3
[34] OnlineCache: Learning Dynamic Caching Policies with Error Correction for Efficient Diffusion Inference — http://arxiv.org/abs/2607.29398v1
[35] Diffusion Policy: Visuomotor Policy Learning via Action Diffusion — http://arxiv.org/abs/2303.04137v5
[36] Self-Supervised Correspondence in Visuomotor Policy Learning — http://arxiv.org/abs/1909.06933v1
[37] Factorizing Diffusion Policies for Observation Modality Prioritization — http://arxiv.org/abs/2509.16830v1
[38] Diffusion Co-Policy for Synergistic Human-Robot Collaborative Tasks — http://arxiv.org/abs/2305.12171v4
[39] JEPA Policy: Diffusion-Free Imitation Learning via Paired Action and Future Representation Prediction — http://arxiv.org/abs/2609.09630v1
[40] ALOHA 2: An Enhanced Low-Cost Hardware for Bimanual Teleoperation — http://arxiv.org/abs/2405.02292v1
[41] Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware — http://arxiv.org/abs/2304.13705v1
[42] Mobile ALOHA: Learning Bimanual Mobile Manipulation with Low-Cost Whole-Body Teleoperation — http://arxiv.org/abs/2401.02117v1
[43] Stabilize to Act: Learning to Coordinate for Bimanual Manipulation — http://arxiv.org/abs/2309.01087v2
[44] DAIR: Disentangled Attention Intrinsic Regularization for Safe and Efficient Bimanual Manipulation — http://arxiv.org/abs/2106.05907v4
[45] 3D-ViTac: Learning Fine-Grained Manipulation with Visuo-Tactile Sensing — http://arxiv.org/abs/2410.24091v2
[46] SnapperGPS: Open Hardware for Energy-Efficient, Low-Cost Wildlife Location Tracking with Snapshot GNSS — http://arxiv.org/abs/2207.06310v3
[47] VoxAct-B: Voxel-Based Acting and Stabilizing Policy for Bimanual Manipulation — http://arxiv.org/abs/2407.04152v2
[48] One-Shot Reinforcement Learning for Robot Navigation with Interactive Replay — http://arxiv.org/abs/1711.10137v2
[49] Robot Policy Evaluation for Sim-to-Real Transfer: A Benchmarking Perspective — http://arxiv.org/abs/2508.11117v1
[50] Grasp and Motion Planning for Dexterous Manipulation for the Real Robot Challenge — http://arxiv.org/abs/2101.02842v1
[51] JENGA: Exploiting Counter-Based RowHammer Countermeasures to Break Real-Time Predictability — http://arxiv.org/abs/2609.01077v1
[52] An Introduction to Lifelong Supervised Learning — http://arxiv.org/abs/2207.04354v2
[53] LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning — http://arxiv.org/abs/2306.03310v2
[54] Latent Properties of Lifelong Learning Systems — http://arxiv.org/abs/2207.14378v1
[55] Lifelong Learning using Eigentasks: Task Separation, Skill Acquisition, and Selective Transfer — http://arxiv.org/abs/2007.06918v1
[56] Forgetting and Imbalance in Robot Lifelong Learning with Off-policy Data — http://arxiv.org/abs/2204.05893v2
[57] TAG: Task-based Accumulated Gradients for Lifelong learning — http://arxiv.org/abs/2105.05155v3
[58] OpenFact at CheckThat! 2024: Combining Multiple Attack Methods for Effective Adversarial Text Generation — http://arxiv.org/abs/2409.02649v2
[59] NTU-NPU System for Voice Privacy 2024 Challenge — http://arxiv.org/abs/2410.02371v1
[60] Evaluating Real-World Robot Manipulation Policies in Simulation — http://arxiv.org/abs/2405.05941v1
[61] Discovery Opportunities with Gravitational Waves -- TASI 2024 Lecture Notes — http://arxiv.org/abs/2409.08956v1
[62] RoboArena: Distributed Real-World Evaluation of Generalist Robot Policies — http://arxiv.org/abs/2506.18123v2
[63] Overview of the Sensemaking Task at the ELOQUENT 2025 Lab: LLMs as Teachers, Students and Evaluators — http://arxiv.org/abs/2507.12143v1
[64] LongEval at CLEF 2025: Longitudinal Evaluation of IR Model Performance — http://arxiv.org/abs/2503.08541v1
[65] NTIRE 2025 Challenge on Image Super-Resolution (x4): Methods and Results — http://arxiv.org/abs/2504.14582v3
[66] VLSP 2025 MLQA-TSR Challenge: Vietnamese Multimodal Legal Question Answering on Traffic Sign Regulation — http://arxiv.org/abs/2510.20381v1
[67] Annif at SemEval-2025 Task 5: Traditional XMTC augmented by LLMs — http://arxiv.org/abs/2504.19675v2
[68] Robotic VLA Benefits from Joint Learning with Motion Image Diffusion — http://arxiv.org/abs/2512.18007v1
[69] Running VLAs at Real-time Speed — http://arxiv.org/abs/2510.26742v1
[70] Task adaptation of Vision-Language-Action model: 1st Place Solution for the 2025 BEHAVIOR Challenge — http://arxiv.org/abs/2512.06951v2
[71] Evolve Vision-Language-Action Model into an Agent with On-the-fly Tool-use — http://arxiv.org/abs/2608.14047v3
[72] UIC-AIHealth4All at ArchEHR-QA 2026: Answer-First Evidence Grounding for Clinical Question Answering — http://arxiv.org/abs/2608.27467v1
[73] Second MOASEI Competition at AAMAS'2026: A Technical Report — http://arxiv.org/abs/2607.03399v1
[74] VITA: Vision-to-Action Flow Matching Policy — http://arxiv.org/abs/2507.13231v4
[75] TinyGiantVLM: A Lightweight Vision-Language Architecture for Spatial Reasoning under Resource Constraints — http://arxiv.org/abs/2508.17595v1
[76] VLS: Steering Pretrained Robot Policies via Vision-Language Models — http://arxiv.org/abs/2602.03973v1
[77] Overview of the First Workshop on Language Models for Low-Resource Languages (LoResLM 2025) — http://arxiv.org/abs/2412.16365v1
[78] OpenVLA: An Open-Source Vision-Language-Action Model — http://arxiv.org/abs/2406.09246v3
[79] Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success — http://arxiv.org/abs/2502.19645v2
[80] Atmospheric entry and fragmentation of small asteroid 2024 BX1: Bolide trajectory, orbit, dynamics, light curve, and spectrum — http://arxiv.org/abs/2403.00634v2
[81] GR00T N1: An Open Foundation Model for Generalist Humanoid Robots — http://arxiv.org/abs/2503.14734v2
[82] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1
[83] AIM 2025 Rip Current Segmentation (RipSeg) Challenge Report — http://arxiv.org/abs/2508.13401v3
[84] Inaugural MOASEI Competition at AAMAS'2025: A Technical Report — http://arxiv.org/abs/2507.05469v1
[85] A ROS-based Software Framework for the NimbRo-OP Humanoid Open Platform — http://arxiv.org/abs/1809.11051v1
[86] NimbRo-OP2: Grown-up 3D Printed Open Humanoid Platform for Research — http://arxiv.org/abs/1809.11144v1
[87] Federated Sketching LoRA: A Flexible Framework for Heterogeneous Collaborative Fine-Tuning of LLMs — http://arxiv.org/abs/2501.19389v4
[88] LoRA-FAIR: Federated LoRA Fine-Tuning with Aggregation and Initialization Refinement — http://arxiv.org/abs/2411.14961v3
[89] Fine-Tuning Open Video Generators for Cinematic Scene Synthesis: A Small-Data Pipeline with LoRA and Wan2.1 I2V — http://arxiv.org/abs/2510.27364v1
[90] LoRA-C: Parameter-Efficient Fine-Tuning of Robust CNN for IoT Devices — http://arxiv.org/abs/2410.16954v2
[91] Learning Rate Matters: Vanilla LoRA May Suffice for LLM Fine-tuning — http://arxiv.org/abs/2602.04998v2
[92] Targeted Lexical Injection: Unlocking Latent Cross-Lingual Alignment in Lugha-Llama via Early-Layer LoRA Fine-Tuning — http://arxiv.org/abs/2506.15415v1
[93] Enhancing Linguistic Generalization of VLA: Fine-Tuning OpenVLA via Synthetic Instruction Augmentation — http://arxiv.org/abs/2603.16044v1
[94] Fine-tuning with Very Large Dropout — http://arxiv.org/abs/2403.00946v3
[95] ToxiFrench: Benchmarking and Enhancing Language Models via CoT Fine-Tuning for French Toxicity Detection — http://arxiv.org/abs/2508.11281v3
[96] ClaimIQ at CheckThat! 2025: Comparing Prompted and Fine-Tuned Language Models for Verifying Numerical Claims — http://arxiv.org/abs/2509.11492v1
[97] Open Source Software Development Challenges: A Systematic Literature Review on GitHub — http://arxiv.org/abs/2003.10750v3
[98] Impromptu VLA: Open Weights and Open Data for Driving Vision-Language-Action Models — http://arxiv.org/abs/2505.23757v1
[99] UM_FHS at the CLEF 2025 SimpleText Track: Comparing No-Context and Fine-Tune Approaches for GPT-4.1 Models in Sentence and Document-Level Text Simplification — http://arxiv.org/abs/2512.16541v1
[100] VQualA 2025 Challenge on Visual Quality Comparison for Large Multimodal Models: Methods and Results — http://arxiv.org/abs/2509.09190v1
[101] Real-Time Service Subscription and Adaptive Offloading Control in Vehicular Edge Computing — http://arxiv.org/abs/2512.14002v1
[102] Real time state monitoring and fault diagnosis system for motor based on LabVIEW — http://arxiv.org/abs/1806.09998v1
[103] On $\ell_2$-performance of weakly-hard real-time control systems — http://arxiv.org/abs/2305.07875v3
[104] Duality-based Convex Optimization for Real-time Obstacle Avoidance between Polytopes with Control Barrier Functions — http://arxiv.org/abs/2107.08360v4
[105] Real-Time-Data Analytics in Raw Materials Handling — http://arxiv.org/abs/1802.00625v1
[106] Erasure Coding and Congestion Control for Interactive Real-Time Communication — http://arxiv.org/abs/1207.2863v1
[107] On the Off-chip Memory Latency of Real-Time Systems: Is DDR DRAM Really the Best Option? — http://arxiv.org/abs/1810.07059v1
[108] User Study Exploring the Role of Explanation of Failures by Robots in Human Robot Collaboration Tasks — http://arxiv.org/abs/2303.16010v1
[109] AeroManip-VLA: Scalable Vision-Language-Action Learning for Aerial Manipulation with RL-Generated Demonstrations — http://arxiv.org/abs/2609.36915v1
[110] When Vision Overrides Language: Evaluating and Mitigating Counterfactual Failures in VLAs — http://arxiv.org/abs/2602.17659v2
[111] RACER: Rich Language-Guided Failure Recovery Policies for Imitation Learning — http://arxiv.org/abs/2409.14674v1
[112] Your Vision-Language-Action Model Already Has Attention Heads For Path Deviation Detection — http://arxiv.org/abs/2603.13782v1
[113] Critique-RL: Training Language Models for Critiquing through Two-Stage Reinforcement Learning — http://arxiv.org/abs/2510.24320v1
[114] VLA-Adapter: An Effective Paradigm for Tiny-Scale Vision-Language-Action Model — http://arxiv.org/abs/2509.09372v2
[115] From Foundation to Application: Improving VLA Models in Practice — http://arxiv.org/abs/2607.06403v1
[116] LongNav-R1: Horizon-Adaptive Multi-Turn RL for Long-Horizon VLA Navigation — http://arxiv.org/abs/2602.12351v2
[117] IVOA Recommendation: Spectrum Data Model 1.1 — http://arxiv.org/abs/1204.3055v1
[118] Byzantine-Resilient SGD in High Dimensions on Heterogeneous Data — http://arxiv.org/abs/2005.07866v1
[119] Data Encoding for Byzantine-Resilient Distributed Optimization — http://arxiv.org/abs/1907.02664v2
[120] Robust Tabular Foundation Models — http://arxiv.org/abs/2512.03307v1
[121] Constraints on dark energy from H II starburst galaxy apparent magnitude versus redshift data — http://arxiv.org/abs/1110.5626v1
[122] IVOA Recommendation: Data Model for Astronomical DataSet Characterisation — http://arxiv.org/abs/1111.2281v1
[123] TerraGen: A Unified Multi-Task Layout Generation Framework for Remote Sensing Data Augmentation — http://arxiv.org/abs/2510.21391v1
[124] Dalorex: A Data-Local Program Execution and Architecture for Memory-bound Applications — http://arxiv.org/abs/2207.13219v4


---

*Generated by research-bot · topic=`vla` · depth=`standard` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading · model=`deepseek-v4-flash` · sources=124 · duration=296s · 2026-10-02T23:23:19+00:00*
