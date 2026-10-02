# 具身智能·灵巧操作（Dexterous Manipulation & Grasping）技术地图

**元信息**：调研日期 2026-10-02（UTC）｜领域：具身智能 / 灵巧操作与抓取（dexterous manipulation & grasping）｜可引用检索源：94 条编号来源（[1]–[94]）｜证据基线：本轮候选块以 arXiv 摘要级抽取为主，`citations`/`stars` 等热度字段普遍为空，绝大多数条目的发表 venue 与第三方复现均未覆盖

---

## 摘要（Executive Summary）

1. **语言/VLA 接入灵巧手已有明确候选，但仍是"孤证"**：UniHM 提出以自由形式语言指令统一驱动多指灵巧手操作，作者自述为"首个由开放词汇自由语言引导的统一灵巧手操作框架"，用以替代依赖物体中心线索或精确手-物交互序列的旧范式 [42]。
2. **出现一条绕开大规模示教数据的路线**：在物理本体上实时估计"手+物体"联合系统的任务 Jacobian，约 18 s 初始化后即可在类人手上执行在握笔书写并在线自适应，仅用笔记本 CPU [29]。该工作同时指出 RL 仿真器难以复现所需接触复杂度、灵巧示教采集仍是 open problem [29]。
3. **触觉进入 RL 的观测与奖励两条通路**：Tac2Motion 通过触觉奖励塑形 + 触觉 embedding 入观测空间，鼓励稳固抓取与 finger gaiting，在开盖场景验证并声称对多种物体与扭转摩擦等动力学变化具泛化性 [32]。
4. **扩散策略的近期改进主要在通用三维操作，而非灵巧手专用**：Attention-DP3 通过开放词汇分割 + 几何对齐注意力条件化注入物体级几何先验，且不改动 DP3 扩散骨干 [39]；视觉-触觉方向有 Reactive/Tube Diffusion Policy 一脉 [66][67]。**"扩散策略 × 多指灵巧手"的直接证据在本轮检索中缺位** `> 待核实`。
5. **动作分块（action chunking）**在本轮仅有工业接触操作的间接证据（PAC-ACT，面向 action chunking transformers 的后训练 actor-critic）[61]，**未见"action chunking × 灵巧手"的直接证据** `> 待核实`。
6. **抓取/抓取合成方向证据相对完整**：轻量图神经网络集成的高精度抓取位姿检测 [12]、基于接触场的程序化抓取合成 [17]、任务导向 6-DoF 抓取 [2]、语言驱动抓取（负提示引导）[8]、域先验泛化的 6-DoF 抓取检测 [7]。
7. **数据集与基准的可用证据集中在少数几条**：Open X-Embodiment [80]、ManiSkill-ViTac 2025 三赛道挑战 [64]、Grasp-Anything [15]、BEHAVIOR Challenge 2025 的 VLA 任务适配方案 [44]。研究目标中提到的 LIBERO、DROID、SimplerEnv、RoboArena 在本轮可引用来源中**没有直接条目** `> 待核实`。
8. **证据强度总体偏弱**：灵巧操作相关条目几乎全为 arXiv 预印本（B 级）、摘要级抽取，无同行评审确认、无第三方复现、无引用数/star 数字，因此本报告中所有"SOTA/泛化"类宣称均降级表述。
9. **检索噪声必须显式剔除**：q2 候选块混入引力波与天体物理条目（如 [50][52][55]），q3/q6 混入基础模型透明度指数与短视频竞赛 [18][19]，q1 混入自动驾驶 VLA 与室外点云分割 [41]，q5/q6 混入医学影像与外科机器人 [82][91][92]。这些条目与灵巧操作无主题关联，不作为本报告证据。

---

## 一、关键前沿进展（近 1–2 年）

### 1.1 时间线视图

| 时间 | 工作 | 类型 | 验证场景/本体 | 证据强度 | 引用 |
|---|---|---|---|---|---|
| 2025-09（v2 2025-11） | Tac2Motion | 触觉 RL | 开盖（opening a lid）；multi-fingered robot | 预印本摘要 | [32] |
| 2025 | Grasp the Graph 2.0 | 抓取位姿检测 | 杂乱场景（clutter） | 预印本摘要 | [12] |
| 2025 | Lightning Grasp | 程序化抓取合成 | 灵巧手实时多样抓取合成 | 预印本摘要 | [17] |
| 2025 | Task-Oriented 6-DoF Grasp Pose Detection | 任务导向抓取 | 杂乱场景 | 预印本摘要 | [2] |
| 2026-02 | UniHM | VLA/语言 → 灵巧手 | 自由形式语言指令驱动多指手 | 预印本摘要 | [42] |
| 2026-02 | DexRepNet++ | 几何/空间手-物表示 | 多指手高自由度操作 | 预印本摘要 | [46] |
| 2026-06（v3） | ContactWorld | 视觉-触觉世界模型 | 接触丰富操作的受控基准 | 预印本摘要 | [70] |
| 2026-09-10 | Rapid Learning of In-Hand Pen Writing | 在线 Jacobian 估计 | 类人手上在握笔书写 | 预印本摘要 | [29] |
| 2026-09 | Attention-DP3 | 扩散策略条件化 | 三维操作（非灵巧手专用） | 预印本摘要 | [39] |
| 2026 | Tube Diffusion Policy | 视觉-触觉扩散策略 | 接触丰富操作 | 预印本摘要 | [67] |
| 2026 | PAC-ACT | 动作分块后训练 | 精密工业接触操作 | 预印本摘要 | [61] |

> 表中"时间"取自候选块给出的 arXiv 版本信息（如 [32] v1 2025-09-22、v2 2025-11-18）；未给出精确日期的仅标年份 `> 待核实`。

### 1.2 三条值得注意的路线（逐条四轴证据）

**路线 A：语言/VLA 统一驱动灵巧手 —— UniHM（2026）** [42]

- **热度证据**：`> 待

## 参考来源

[1] Oriented object detection in optical remote sensing images using deep learning: a survey — http://arxiv.org/abs/2302.10473v6
[2] Task-Oriented 6-DoF Grasp Pose Detection in Clutters — http://arxiv.org/abs/2502.16976v1
[3] Ground-Based Optical Deep Pencil Beam Surveys — http://arxiv.org/abs/astro-ph/0208209v1
[4] Shear-selected clusters from the Deep Lens Survey — http://arxiv.org/abs/astro-ph/0303381v1
[5] Learn to Accumulate Evidence from All Training Samples: Theory and Practice — http://arxiv.org/abs/2306.11113v2
[6] The Modern Mathematics of Deep Learning — http://arxiv.org/abs/2105.04026v2
[7] Generalizing 6-DoF Grasp Detection via Domain Prior Knowledge — http://arxiv.org/abs/2404.01727v1
[8] Language-Driven 6-DoF Grasp Detection Using Negative Prompt Guidance — http://arxiv.org/abs/2407.13842v2
[9] 2nd Place Solution to ECCV 2020 VIPriors Object Detection Challenge — http://arxiv.org/abs/2007.08849v1
[10] A Report on the 2020 Sarcasm Detection Shared Task — http://arxiv.org/abs/2005.05814v2
[11] The ADAPT Enhanced Dependency Parser at the IWPT 2020 Shared Task — http://arxiv.org/abs/2009.01712v1
[12] Grasp the Graph (GtG) 2.0: Ensemble of Graph Neural Networks for High-Precision Grasp Pose Detection in Clutter — http://arxiv.org/abs/2505.02664v2
[13] UIT-HSE at WNUT-2020 Task 2: Exploiting CT-BERT for Identifying COVID-19 Information on the Twitter Social Network — http://arxiv.org/abs/2009.02935v3
[14] Bitwuzla at the SMT-COMP 2020 — http://arxiv.org/abs/2006.01621v1
[15] Grasp-Anything: Large-scale Grasp Dataset from Foundation Models — http://arxiv.org/abs/2309.09818v1
[16] AO-Grasp: Articulated Object Grasp Generation — http://arxiv.org/abs/2310.15928v4
[17] Lightning Grasp: High Performance Procedural Grasp Synthesis with Contact Fields — http://arxiv.org/abs/2511.07418v1
[18] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1
[19] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1
[20] Generative Dataset Distillation Based on Diffusion Model — http://arxiv.org/abs/2408.08610v1
[21] NTU-NPU System for Voice Privacy 2024 Challenge — http://arxiv.org/abs/2410.02371v1
[22] ICAGC 2024: Inspirational and Convincing Audio Generation Challenge 2024 — http://arxiv.org/abs/2407.12038v2
[23] D-Grasp: Physically Plausible Dynamic Grasp Synthesis for Hand-Object Interactions — http://arxiv.org/abs/2112.03028v2
[24] cWDM: Conditional Wavelet Diffusion Models for Cross-Modality 3D Medical Image Synthesis — http://arxiv.org/abs/2411.17203v1
[25] Learning Dexterous In-Hand Manipulation — http://arxiv.org/abs/1808.00177v5
[26] Dexterous Cable Manipulation: Taxonomy, Multi-Fingered Hand Design, and Long-Horizon Manipulation — http://arxiv.org/abs/2502.00396v2
[27] Learning Complex Dexterous Manipulation with Deep Reinforcement Learning and Demonstrations — http://arxiv.org/abs/1709.10087v2
[28] DEFT: Dexterous Fine-Tuning for Real-World Hand Policies — http://arxiv.org/abs/2310.19797v2
[29] Rapid Learning of Dexterous In-Hand Pen Writing through Real-Time Jacobian Estimation — http://arxiv.org/abs/2609.11775v1
[30] CORL: Research-oriented Deep Offline Reinforcement Learning Library — http://arxiv.org/abs/2210.07105v4
[31] Tilde: Teleoperation for Dexterous In-Hand Manipulation Learning with a DeltaHand — http://arxiv.org/abs/2405.18804v2
[32] Tac2Motion: Contact-Aware Reinforcement Learning with Tactile Feedback for Robotic Hand Manipulation — http://arxiv.org/abs/2509.17812v2
[33] A study of the link between cosmic rays and clouds with a cloud chamber at the CERN PS — http://arxiv.org/abs/physics/0104048v1
[34] CLOUD: an atmospheric research facility at CERN — http://arxiv.org/abs/physics/0104076v1
[35] Addendum to the CLOUD proposal — http://arxiv.org/abs/physics/0104068v1
[36] 3D Diffusion Policy: Generalizable Visuomotor Policy Learning via Simple 3D Representations — http://arxiv.org/abs/2403.03954v7
[37] $PC^2$: Projection-Conditioned Point Cloud Diffusion for Single-Image 3D Reconstruction — http://arxiv.org/abs/2302.10668v2
[38] Technical Report for ICRA 2025 GOOSE 3D Semantic Segmentation Challenge: Adaptive Point Cloud Understanding for Heterogeneous Robotic Systems — http://arxiv.org/abs/2506.06995v1
[39] Attention-DP3: Spatially Object-aware 3D Diffusion Policy via Geometry-aligned Attentional Conditioning — http://arxiv.org/abs/2609.13318v1
[40] Neural Point Cloud Diffusion for Disentangled 3D Shape and Appearance Generation — http://arxiv.org/abs/2312.14124v2
[41] Inference-Time Attention Steering for Vision-Language-Action Driving Models — http://arxiv.org/abs/2608.17095v1
[42] UniHM: Unified Dexterous Hand Manipulation with Vision Language Model — http://arxiv.org/abs/2603.00732v1
[43] Compositional Context Fine-Tuning Vision-Language Model for Complex Assembly Action Understanding from Videos — http://arxiv.org/abs/2607.10797v1
[44] Task adaptation of Vision-Language-Action model: 1st Place Solution for the 2025 BEHAVIOR Challenge — http://arxiv.org/abs/2512.06951v2
[45] Technical Report for Ego4D Long-Term Action Anticipation Challenge 2025 — http://arxiv.org/abs/2506.02550v2
[46] DexRepNet++: Learning Dexterous Robotic Manipulation with Geometric and Spatial Hand-Object Representations — http://arxiv.org/abs/2602.21811v1
[47] Progressive Transfer Learning for Dexterous In-Hand Manipulation with Multi-Fingered Anthropomorphic Hand — http://arxiv.org/abs/2304.09526v1
[48] Observation of the rare $B^0_s\toμ^+μ^-$ decay from the combined analysis of CMS and LHCb data — http://arxiv.org/abs/1411.4413v2
[49] Expected Performance of the ATLAS Experiment - Detector, Trigger and Physics — http://arxiv.org/abs/0901.0512v4
[50] Deep Search for Joint Sources of Gravitational Waves and High-Energy Neutrinos with IceCube During the Third Observing Run of LIGO and Virgo — http://arxiv.org/abs/2601.07595v3
[51] Search for High-energy Neutrinos from Binary Neutron Star Merger GW170817 with ANTARES, IceCube, and the Pierre Auger Observatory — http://arxiv.org/abs/1710.05839v2
[52] GWTC-4.0: Methods for Identifying and Characterizing Gravitational-wave Transients — http://arxiv.org/abs/2508.18081v3
[53] Ultralight vector dark matter search using data from the KAGRA O3GK run — http://arxiv.org/abs/2403.03004v1
[54] GWTC-5.0: Tests of General Relativity — http://arxiv.org/abs/2607.19293v1
[55] GWTC-5.0: Observations from the Second Part of the Fourth LIGO-Virgo-KAGRA Observing Run and Updates to the Gravitational-Wave Transient Catalog — http://arxiv.org/abs/2605.27225v3
[56] ALOHA 2: An Enhanced Low-Cost Hardware for Bimanual Teleoperation — http://arxiv.org/abs/2405.02292v1
[57] Overview of AuTexTification at IberLEF 2023: Detection and Attribution of Machine-Generated Text in Multiple Domains — http://arxiv.org/abs/2309.11285v1
[58] Strategies to Harness the Transformers' Potential: UNSL at eRisk 2023 — http://arxiv.org/abs/2310.19970v1
[59] Automated 3D Segmentation of Kidneys and Tumors in MICCAI KiTS 2023 Challenge — http://arxiv.org/abs/2310.04110v1
[60] UZH_CLyp at SemEval-2023 Task 9: Head-First Fine-Tuning and ChatGPT Data Generation for Cross-Lingual Learning in Tweet Intimacy Prediction — http://arxiv.org/abs/2303.01194v2
[61] PAC-ACT: Post-training Actor-Critic for Action Chunking Transformers — http://arxiv.org/abs/2607.09590v1
[62] DocILE 2023 Teaser: Document Information Localization and Extraction — http://arxiv.org/abs/2301.12394v1
[63] Action Sensitivity Learning for the Ego4D Episodic Memory Challenge 2023 — http://arxiv.org/abs/2306.09172v2
[64] ManiSkill-ViTac 2025: Challenge on Manipulation Skill Learning With Vision and Tactile Sensing — http://arxiv.org/abs/2411.12503v1
[65] Learning Contact-Rich Manipulation Skills with Guided Policy Search — http://arxiv.org/abs/1501.05611v2
[66] Reactive Diffusion Policy: Slow-Fast Visual-Tactile Policy Learning for Contact-Rich Manipulation — http://arxiv.org/abs/2503.02881v3
[67] Tube Diffusion Policy: Reactive Visual-Tactile Policy Learning for Contact-rich Manipulation — http://arxiv.org/abs/2604.23609v1
[68] PolyTouch: A Robust Multi-Modal Tactile Sensor for Contact-rich Manipulation Using Tactile-Diffusion Policies — http://arxiv.org/abs/2504.19341v1
[69] VITaL Pretraining: Visuo-Tactile Pretraining for Tactile and Non-Tactile Manipulation Policies — http://arxiv.org/abs/2403.11898v2
[70] ContactWorld: What Representations Matter for Vision-Tactile Latent World Models in Contact-Rich Manipulation — http://arxiv.org/abs/2606.13877v3
[71] A Modularized Design Approach for GelSight Family of Vision-based Tactile Sensors — http://arxiv.org/abs/2504.14739v1
[72] Towards Learning to Detect and Predict Contact Events on Vision-based Tactile Sensors — http://arxiv.org/abs/1910.03973v1
[73] GelSight Svelte Hand: A Three-finger, Two-DoF, Tactile-rich, Low-cost Robot Hand for Dexterous Manipulation — http://arxiv.org/abs/2309.10886v1
[74] Taxim: An Example-based Simulation Model for GelSight Tactile Sensors — http://arxiv.org/abs/2109.04027v2
[75] Generation of GelSight Tactile Images for Sim2Real Learning — http://arxiv.org/abs/2101.07169v1
[76] Low-Cost Teleoperation with Haptic Feedback through Vision-based Tactile Sensors for Rigid and Soft Object Manipulation — http://arxiv.org/abs/2403.16764v1
[77] TacEx: GelSight Tactile Simulation in Isaac Sim -- Combining Soft-Body and Visuotactile Simulators — http://arxiv.org/abs/2411.04776v1
[78] Proceedings of the Dialogue Robot Competition 2023 — http://arxiv.org/abs/2312.14430v5
[79] Point Transformer V3 Extreme: 1st Place Solution for 2024 Waymo Open Dataset Challenge in Semantic Segmentation — http://arxiv.org/abs/2407.15282v1
[80] Open X-Embodiment: Robotic Learning Datasets and RT-X Models — http://arxiv.org/abs/2310.08864v9
[81] One-Shot Reinforcement Learning for Robot Navigation with Interactive Replay — http://arxiv.org/abs/1711.10137v2
[82] The RSNA Abdominal Traumatic Injury CT (RATIC) Dataset — http://arxiv.org/abs/2405.19595v1
[83] Open-Ended Learning Leads to Generally Capable Agents — http://arxiv.org/abs/2107.12808v2
[84] Learning to Discern: Imitating Heterogeneous Human Demonstrations with Preference and Representation Learning — http://arxiv.org/abs/2310.14196v1
[85] Robot Policy Evaluation for Sim-to-Real Transfer: A Benchmarking Perspective — http://arxiv.org/abs/2508.11117v1
[86] AI Models to Reduce Surgical Complications Through Intraoperative Video Analysis: Protocol for a Prospective Cohort Study. — https://doi.org/10.2196/62734
[87] Generalist Robot Manipulation beyond Action Labeled Data — http://arxiv.org/abs/2509.19958v1
[88] The Role of AI and Automation in Improving Accounting Efficiency — https://doi.org/10.63544/jbii.v5i8.126
[89] Modularity through Attention: Efficient Training and Transfer of Language-Conditioned Policies for Robot Manipulation — http://arxiv.org/abs/2212.04573v1
[90] Growth, Carbon Emissions, and Public Health Spending: Long-Run Evidence from South Asia — https://doi.org/10.63544/jbii.v5i9.230
[91] LLM-based ambiguity detection in natural language instructions for collaborative surgical robots — http://arxiv.org/abs/2507.11525v1
[92] Human-Robot collaboration in surgery: Advances and challenges towards autonomous surgical assistants — http://arxiv.org/abs/2507.11460v1
[93] An Open-Source Soft Robotic Platform for Autonomous Aerial Manipulation in the Wild — http://arxiv.org/abs/2409.07662v2
[94] TRUST 2025: SCRITA and RTSS @ RO-MAN 2025 — http://arxiv.org/abs/2509.11402v1


---

*Generated by research-bot · topic=`embodied-manipulation` · depth=`standard` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading · model=`deepseek-v4-flash` · sources=94 · duration=837s · 2026-10-02T22:43:20+00:00*
