# 具身智能 · 世界模型与仿真（World Models & Simulation）深度调研报告

**日期**：2026-10-02（UTC） ｜ **领域**：Embodied AI — World Models & Simulation ｜ **候选证据源**：71 条编号来源 + 11 条人工维护种子资源（3 论文 / 5 项目 / 3 数据集） ｜ **实际采用**：41 条编号来源 + 11 条种子资源 ｜ **方法**：按 `deep-research` 四阶段（广域探索 → 定向深潜 → 交叉验证 → 缺口检查），检索源覆盖 arXiv（cs.RO / cs.LG / cs.CV）、NeurIPS、IEEE RA-L、GitHub、HuggingFace。

> **证据质量前置声明（重要）**：本次抽取的候选发现中存在**显著检索噪声**。子问题 q4、q5 的多数条目（如 IWSLT 语音翻译 [28][29]、多语种 ASR [31]、LiveRAG 挑战赛 [30]、短视频参与度预测 [6]、越南法律问答 [57]、HDR 视频质量评测 [10]）与"具身智能世界模型与仿真"无实质关联；子问题 q3 的 findings 为**空集**。本报告据此执行降级策略：剔除不相关条目，对缺口章节显式标注 `> 待核实`，不以噪声填充结论。此外，少数候选来源的编号形态异常（如 [23] 标题含 "GPT-6-Astra"），已单独标注为低置信。

---

## 摘要（Executive Summary）

1. **范式迁移已发生：世界模型正从"RL 内部组件"升级为"物理 AI 的基础模型"**。经典路线（World Models 2018 → DreamerV3, Nature 2023）把世界模型作为 model-based RL 的潜空间动力学预测器；2024–2026 的新路线（NVIDIA Cosmos 平台 [38][39][40]、视频扩散世界模型 [45][46][47][48]）则把它当作可独立预训练、可多模态条件生成的**世界基础模型（World Foundation Model, WFM）**。

2. **自监督视频表征成为"理解—预测—规划"一体化的重要技术路径**。V-JEPA 2 [52] 明确以"互联网级视频 + 少量机器人轨迹"训练，声称同时支持理解、预测与规划，是本报告热度最高的单篇证据（citations=806，据检索元数据）。

3. **"把视频生成模型当仿真器"是当前最活跃也最受质疑的方向**。AVID [45]、Cosmos-Predict 系列 [40]、GEM-4D [5]、FlowDreamer [49]、ChronoDreamer [48] 都在尝试用生成模型做动作条件的未来预测，但物理一致性（physical grounding）被反复指出是瓶颈 [5][7]。

4. **GPU 并行仿真是工程侧最确定的技术红利**。ManiSkill3 [58] 代表了"GPU 并行化仿真 + 渲染"的路线，与 MuJoCo / IsaacLab / Genesis 共同构成 2026 年的主流仿真栈（后三者来自种子资源，热度数字 `> 待核实`）。

5. **sim2real 的方法体系成熟但差距仍在**。域随机化 [26]、视觉编码器预训练 [24]、多模态（含音频）迁移 [20]、真机自动适配 [17] 是可核查的四条主线；R:SS 2020 的结论"sim2real 不是单一问题而是问题集合"至今仍有解释力 [21]。

6. **评测口径的脆弱性是本领域最大的系统性风险**。LIBERO-Para [61]、LIBERO-VPro [62]、ManipBench [60]、Sim-to-Real 基准视角 [35] 共同揭示：现有基准多假设"干净、及时、一致的视觉观测"，与真实部署条件严重脱节。

7. **明确的证据缺口**：Genie 3、WorldVLA、GAIA 系列、Dreamer 4、MJX / Brax / Warp / DiffTaichi 在本轮证据集中**均无一手可核查来源**，全部标注 `> 待核实`（详见第七、八节）。

---

## 一、关键前沿进展（近 1–2 年）

| 时间 | 名称 | 机构/出处 | 一句话贡献 | 证据强度 | 引用 |
|---|---|---|---|---|---|
| 2025-06 | **V-JEPA 2** | arXiv | 自监督视频 + 少量机器人轨迹，统一理解/预测/规划 | 预印本 | [52] |
| 2025-01 | **Cosmos WFM Platform** | arXiv (cs.CV) | 面向 Physical AI 的世界基础模型平台化 | 预印本 | [38] |
| 2025-11 | **Cosmos-Predict 2.5** | arXiv (cs.CV) | flow-based 架构统一 Text2World/Image2World/Video2World | 预印本 | [40] |
| 2026-06 | **Cosmos 3** | arXiv (cs.CV) | 语言/图像/视频/音频/动作统一 MoT 架构 | 预印本 | [39] |
| 2025-12 | **mimic-video** | Robotics | 以 video-action model 替代 VLA 静态骨干 | 预印本 | [50] |
| 2025-05 | **FlowDreamer** | IEEE RA-L | RGB-D + 光流运动表征的机器人世界模型 | 期刊（RA-L） | [49] |
| 2025-06 | **3DFlowAction** | arXiv | 3D flow 世界模型实现跨本体操作学习 | 预印本 | [54] |
| 2025-12 | **ChronoDreamer** | arXiv | 动作条件世界模型作为在线规划仿真器 | 预印本 | [48] |
| 2026-04 | **World Action Verifier** | arXiv | 利用前向-逆向不对称性自改进世界模型 | 预印本 | [47] |
| 2026-05 | **GEM-4D** | arXiv (cs.CV) | 几何增强，解决视频世界模型物理点追踪不一致 | 预印本 | [5] |
| 2026-05 | **Causal Physics Steering** | arXiv (cs.CV) | 用概念激活向量在推理期干预物理合理性 | 预印本 | [7] |
| 2024-10 | **AVID** | arXiv | 将视频扩散模型适配为世界模型 | 预印本 | [45] |

### 1.1 V-JEPA 2：自监督视频路线的旗舰

V-JEPA 2 的核心主张是：**结合互联网级视频数据与少量交互数据（机器人轨迹），可以得到同时具备理解、预测与规划能力的模型** [52]。

- **热度证据**：citations=806（据检索元数据，可能含预印本引用）[52]。
- **权威证据**：arXiv 预印本，尚无同行评审记录可查 [52]。
- **关注度**：高 — 引文数为本报告全部条目之首 [52]。
- **推荐度**：★★★★★ — 自监督视频→具身规划的代表性工作，必读；但引用数需以官方 arXiv/Scholar 页面复核 `> 待核实`。

> ⚠️ **待核实**：本报告未能从候选来源中确认 V-JEPA 2 在真机任务上的具体成功率数字与任务数口径；引用其指标前须回原文表格核对。

### 1.2 视频-动作模型 vs VLA：mimic-video 的问题重述

mimic-video 明确提出一个尖锐批评：**主流 VLA 建立在静态网络数据预训练的视觉-语言骨干上，因而必须"隐式推断复杂物理动力学与时间结构"**，其替代方案是 video-action model [50]。

- **热度证据**：citations=147 [50]。
- **权威证据**：venue 标注为 *Robotics*（据检索元数据，具体期刊/会议 `> 待核实`）[50]。
- **关注度**：高 — 引用数在 2025 年新作中居前 [50]。
- **推荐度**：★★★★★ — 直接触及"VLA 是否足以承载物理动力学"这一核心争议。

### 1.3 Cosmos：世界模型平台化

NVIDIA Cosmos 系列构成一条清晰的三代演进链：平台论文 [38] → 统一生成模型 Cosmos-Predict 2.5 [40] → 全模态 Cosmos 3 [39]。

- **热度证据**：`> 待核实`（候选数据未提供引用数）。
- **权威证据**：三篇均为 arXiv cs.CV 预印本，标注为 NVIDIA 方向（机构名未在证据文本中给出，`> 待核实`）[38][39][40]。
- **关注度**：中—高 — 作为少数"平台级"世界模型工程，产业侧讨论度高；但无榜单/引用支撑，判断保守 [38][39][40]。
- **推荐度**：★★★★☆ — 若关注**工程栈与开源权重**，这是本主题最相关的一手来源之一。

> ⚠️ **待核实**：Cosmos 3 [39] 与 Cosmos-Predict 2.5 [40] 的 arXiv 编号形态需以 arXiv 页面核实；Cosmos 是否开放权重、许可证类型未在候选证据中体现。

### 1.4 明确缺失的前沿项

用户问题中提及的 **Genie 3、WorldVLA、Dreamer 4、GAIA 系列**，在本轮 71 条候选来源中**均无对应编号**。按引用纪律，本报告不为其生成任何技术描述：

> **待核实**：Genie 3（DeepMind）、WorldVLA、Dreamer 4、GAIA-1/GAIA-2（Wayve）的发布时间、技术细节与开源状态均无法从本证据集核实。建议下一轮定向检索补齐，或在报告中明确标注"未检索到一手来源"。

---

## 二、生成式/视频世界模型

### 2.1 两条技术路线

**(A) 潜空间动力学路线（latent dynamics）**：在压缩表征上做前向预测，代表是 Dreamer 谱系（种子资源）与 FlowDreamer [49]、ChronoDreamer [48]。

**(B) 像素/视频生成路线（pixel-space generative）**：直接生成未来帧，代表是 Cosmos [38][39][40]、AVID [45]、GEM-4D [5]。

FlowDreamer 明确站在 (A) 一侧，并给出路线选择的理由：**相对于"标准世界模型"，它显式地使用 RGB-D 帧与基于流的运动表征**来处理机器人操作 [49]。

- **热度证据**：citations=24 [49]。
- **权威证据**：**IEEE Robotics and Automation Letters（RA-L）** — 本报告证据集中少见的同行评审期刊来源，证据等级 A [49]。
- **关注度**：中 — 引用数不高但发表渠道权威 [49]。
- **推荐度**：★★★★☆ — 若需要一个"可引用的、经同行评审的"世界模型基线，优先看它。

> ⚠️ **待核实**：FlowDreamer 的 arXiv URL（`arxiv.org/abs/2505.10075`）与 RA-L 正式版本是否一致、是否存在版本差异，未核实 [49]。

### 2.2 综述给出的领域地图

两篇 Sora 相关综述提供了本主题的宏观坐标系：

- **《Sora as a World Model? A Complete Survey on Text-to-Video Generation》** [8] — 系统梳理文生视频与世界模型的边界。
- **《Is Sora a World Simulator? A Comprehensive Survey on General World Models and Beyond》** [46] — 把"通用世界模型"作为独立研究纲领来讨论。

二者共同支撑一个关键判断：**"视频生成 ≠ 世界模型"是领域内的公开争议，而非本报告的推断** [8

## 参考来源

[1] Revisiting "Recurrent World Models Facilitate Policy Evolution" — https://doi.org/10.1007/978-3-030-86230-5_26
[2] An Attention-Enhanced Transformer Framework for Intelligent Energy Management and Load Forecasting in U.S. Power Grids — https://doi.org/10.32996/jcsts.2025.8.1.1
[3] GRU-ODE-Bayes: Continuous modeling of sporadically-observed time series — https://arxiv.org/abs/1905.12374
[4] Dynamics Modeling between Learnable State Space Subsets for Data Efficient Reinforcement Learning — https://www.semanticscholar.org/paper/2a07d9a8ab711b248e89fbff696693ca51127224
[5] GEM-4D: Geometry-Enhanced Video World Models for Robot Manipulation — http://arxiv.org/abs/2605.22882v4
[6] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1
[7] Causal Physics Steering in Video World Models via Concept Activation Vectors — http://arxiv.org/abs/2605.24322v1
[8] Sora as a World Model? A Complete Survey on Text-to-Video Generation — http://arxiv.org/abs/2403.05131v3
[9] Culturally Grounded Physical Commonsense Reasoning in Italian and English: A Submission to the MRL 2025 Shared Task — http://arxiv.org/abs/2510.22631v1
[10] ICME 2025 Generalizable HDR and SDR Video Quality Measurement Grand Challenge — http://arxiv.org/abs/2506.22790v2
[11] LongEval at CLEF 2025: Longitudinal Evaluation of IR Model Performance — http://arxiv.org/abs/2503.08541v1
[12] Overview of the Sensemaking Task at the ELOQUENT 2025 Lab: LLMs as Teachers, Students and Evaluators — http://arxiv.org/abs/2507.12143v1
[13] Multi-objective Model-based Policy Search for Data-efficient Learning with Sparse Rewards — http://arxiv.org/abs/1806.09351v3
[14] On-Policy Robot Imitation Learning from a Converging Supervisor — http://arxiv.org/abs/1907.03423v7
[15] One-Shot Reinforcement Learning for Robot Navigation with Interactive Replay — http://arxiv.org/abs/1711.10137v2
[16] A Comprehensive Review of Propagation Models in Complex Networks: From Deterministic to Deep Learning Approaches — http://arxiv.org/abs/2410.02118v1
[17] Robot Trains Robot: Automatic Real-World Policy Adaptation and Learning for Humanoids — http://arxiv.org/abs/2508.12252v2
[18] KDPE: A Kernel Density Estimation Strategy for Diffusion Policy Trajectory Selection — http://arxiv.org/abs/2508.10511v2
[19] Model-Based Reinforcement Learning via Meta-Policy Optimization — http://arxiv.org/abs/1809.05214v1
[20] The Sound of Simulation: Learning Multimodal Sim-to-Real Robot Policies with Generative Audio — http://arxiv.org/abs/2507.02864v2
[21] Perspectives on Sim2Real Transfer for Robotics: A Summary of the R:SS 2020 Workshop — http://arxiv.org/abs/2012.03806v1
[22] The Importance and the Limitations of Sim2Real for Robotic Manipulation in Precision Agriculture — http://arxiv.org/abs/2008.03983v1
[23] Robot Manipulation with GPT-6-Astra: Body Knowledge, Experience Reuse, Emergent Skills, and Sim2Real Transfer — http://arxiv.org/abs/2609.31770v1
[24] Bridging the Sim2Real Gap: Vision Encoder Pre-Training for Visuomotor Policy Transfer — http://arxiv.org/abs/2501.16389v2
[25] Federated and Transfer Learning: A Survey on Adversaries and Defense Mechanisms — http://arxiv.org/abs/2207.02337v1
[26] Analysis of Randomization Effects on Sim2Real Transfer in Reinforcement Learning for Robotic Manipulation Tasks — http://arxiv.org/abs/2206.06282v2
[27] Sim2Real Transfer for Audio-Visual Navigation with Frequency-Adaptive Acoustic Field Prediction — http://arxiv.org/abs/2405.02821v2
[28] CMU's IWSLT 2025 Simultaneous Speech Translation System — http://arxiv.org/abs/2506.13143v1
[29] MLLP-VRAIN UPV system for the IWSLT 2025 Simultaneous Speech Translation Translation task — http://arxiv.org/abs/2506.18828v1
[30] RMIT-ADM+S at the SIGIR 2025 LiveRAG Challenge — http://arxiv.org/abs/2506.14516v2
[31] NTU Speechlab LLM-Based Multilingual ASR System for Interspeech MLC-SLM Challenge 2025 — http://arxiv.org/abs/2506.13339v2
[32] Human-Robot collaboration in surgery: Advances and challenges towards autonomous surgical assistants — http://arxiv.org/abs/2507.11460v1
[33] LLM-based ambiguity detection in natural language instructions for collaborative surgical robots — http://arxiv.org/abs/2507.11525v1
[34] TalTech Systems for the Interspeech 2025 ML-SUPERB 2.0 Challenge — http://arxiv.org/abs/2506.01458v1
[35] Robot Policy Evaluation for Sim-to-Real Transfer: A Benchmarking Perspective — http://arxiv.org/abs/2508.11117v1
[36] Grasp and Motion Planning for Dexterous Manipulation for the Real Robot Challenge — http://arxiv.org/abs/2101.02842v1
[37] Foundations of GenIR — http://arxiv.org/abs/2501.02842v1
[38] Cosmos World Foundation Model Platform for Physical AI — http://arxiv.org/abs/2501.03575v3
[39] Cosmos 3: Omnimodal World Models for Physical AI — http://arxiv.org/abs/2606.02800v4
[40] World Simulation with Video Foundation Models for Physical AI — http://arxiv.org/abs/2511.00062v2
[41] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1
[42] Inaugural MOASEI Competition at AAMAS'2025: A Technical Report — http://arxiv.org/abs/2507.05469v1
[43] AI Safety is Stuck in Technical Terms -- A System Safety Response to the International AI Safety Report — http://arxiv.org/abs/2503.04743v1
[44] AIM 2025 Rip Current Segmentation (RipSeg) Challenge Report — http://arxiv.org/abs/2508.13401v3
[45] AVID: Adapting Video Diffusion Models to World Models — http://arxiv.org/abs/2410.12822v2
[46] Is Sora a World Simulator? A Comprehensive Survey on General World Models and Beyond — http://arxiv.org/abs/2405.03520v2
[47] World Action Verifier: Self-Improving World Models via Forward-Inverse Asymmetry — http://arxiv.org/abs/2604.01985v2
[48] ChronoDreamer: Action-Conditioned World Model as an Online Simulator for Robotic Planning — https://arxiv.org/abs/2512.18619
[49] FlowDreamer: A RGB-D World Model With Flow-Based Motion Representations for Robot Manipulation — https://arxiv.org/abs/2505.10075
[50] mimic-video: Video-Action Models for Generalizable Robot Control Beyond VLAs — https://arxiv.org/abs/2512.15692
[51] Aligning Cyber Space with Physical World: A Comprehensive Survey on Embodied AI — http://arxiv.org/abs/2407.06886v8
[52] V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning — https://arxiv.org/abs/2506.09985
[53] mdok of KInIT: Robustly Fine-tuned LLM for Binary and Multiclass AI-Generated Text Detection — http://arxiv.org/abs/2506.01702v2
[54] 3DFlowAction: Learning Cross-Embodiment Manipulation from 3D Flow World Model — https://arxiv.org/abs/2506.06199
[55] NeurIPS should lead scientific consensus on AI policy — http://arxiv.org/abs/2510.00075v1
[56] NTIRE 2025 Challenge on Image Super-Resolution (x4): Methods and Results — http://arxiv.org/abs/2504.14582v3
[57] VLSP 2025 MLQA-TSR Challenge: Vietnamese Multimodal Legal Question Answering on Traffic Sign Regulation — http://arxiv.org/abs/2510.20381v1
[58] ManiSkill3: GPU Parallelized Robotics Simulation and Rendering for Generalizable Embodied AI — http://arxiv.org/abs/2410.00425v2
[59] TRUST 2025: SCRITA and RTSS @ RO-MAN 2025 — http://arxiv.org/abs/2509.11402v1
[60] ManipBench: Benchmarking Vision-Language Models for Low-Level Robot Manipulation — http://arxiv.org/abs/2505.09698v2
[61] LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models — http://arxiv.org/abs/2603.28301v3
[62] LIBERO-VPro: Benchmarking Closed-Loop Visual Robustness of Robotic Foundation Models — http://arxiv.org/abs/2609.24350v1
[63] Annif at SemEval-2025 Task 5: Traditional XMTC augmented by LLMs — http://arxiv.org/abs/2504.19675v2
[64] Event-Enriched Image Analysis Grand Challenge at ACM Multimedia 2025 — http://arxiv.org/abs/2508.18904v1
[65] The AudioMOS Challenge 2025 — http://arxiv.org/abs/2509.01336v1
[66] Openpi Comet: Competition Solution For 2025 BEHAVIOR Challenge — http://arxiv.org/abs/2512.10071v3
[67] TDCOSMO 2025: Cosmological constraints from strong lensing time delays — http://arxiv.org/abs/2506.03023v4
[68] What-If World: A Causal Benchmark for General World Models in Embodied Scenarios — http://arxiv.org/abs/2605.27589v1
[69] Engagement Prediction of Short Videos with Large Multimodal Models — http://arxiv.org/abs/2508.02516v2
[70] Nano World Models: A Minimalist Implementation of Future Video Prediction — http://arxiv.org/abs/2605.23993v2
[71] Video-SafetyBench: A Benchmark for Safety Evaluation of Video LVLMs — http://arxiv.org/abs/2505.11842v3


---

*Generated by research-bot · topic=`embodied-world-models` · depth=`standard` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading · model=`deepseek-v4-flash` · sources=71 · duration=935s · 2026-10-02T22:58:55+00:00*
