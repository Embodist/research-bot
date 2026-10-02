# 大模型与基础模型前沿调研报告（2024–2026）

**日期**：2026-10-02（UTC） | **领域**：人工智能 / 基础模型（Foundation Models） | **子问题数**：6 | **可引用来源**：本次检索提供编号来源 [1]–[123]（共 123 条），其中与六个子问题直接相关者约 45 条，其余为无关或弱相关条目

> **证据基础声明**：本报告严格只引用编号来源 [1]–[123] 中真实存在的条目。绝大多数条目为 arXiv 预印本或 Zenodo / SSRN / figshare / TechRxiv 预印本，**A 级（同行评审会议/期刊）证据在本批来源中占比极低**。本批抽取中仅少数条目提供了摘要原文（[1][2][3][4][5][6][9][26][29][72][74][101][103][104][105][106]），其余仅有标题与元数据，因此凡依据标题级信息得出的判断，正文均标注「标题级证据」并给出 `> 待核实`。**本报告最重要的结论之一是：结构化发现对「推理模型归因」「RLHF/DPO 能力边界」等核心问题的证据覆盖严重不足，不能据此下技术结论。**

---

## 摘要（Executive Summary）

1. **证据覆盖度是本次调研的第一结论**。子问题 q1（推理与测试时计算）的候选 6 条中，仅 [101] 直接相关，其余为短视频参与度预测挑战赛 [7]、图像超分挑战赛 [10]、教育会议论文集 [85]、认知流干预 [23]、透明度指数 [9]；q2（后训练）的候选集中在经典 RL 探索 [1]、课程 RL [3]、真机 RL 平台 [2]，**没有任何一条直接讨论 RLHF 或 DPO 的方法、能力边界与失败模式**。因此下文对 RLHF/DPO 部分只做「证据缺口」陈述，不做技术结论。

2. **测试时计算（test-time compute）方向在本次来源中信号最密集**：从推理期验证与重排（[97]）、反馈与编辑模型驱动的推理期扩展（[98][100]）、慢思考综述（[99]）、流模型推理期扩展（[94]）、sleep-time compute（[86]）、世界模型测试时扩展（[84]）到对「检测-验证」式推理期缩放的在线蒸馏分析（[87]），形成一条可继续深挖的引用链。同时存在明确的**反向争议证据**：标题为《When Deliberation Hurts: Inverse Test-Time Scaling, Unfaithful Traces…》的系列工作 [88][89][90] 与《Does More Inference-Time Compute Really Help Robustness?》[102]（均为标题级证据，`> 待核实`）。

3. **推理模型训练的工程瓶颈已被显式提出**：Nemotron-Cascade [101] 指出 RL 构建通用推理模型面临显著的跨域异质性，表现为推理期响应长度与验证时延的大幅波动，进而拖慢训练、使响应长度课程与超参选择困难（摘要原文，citations=44）。

4. **RLVR 的能力边界存在双向证据**：正方是 RLVR-World [4]，把可验证奖励用于直接优化世界模型的转移预测指标，跨文本游戏、网页导航与机器人操作验证；反方是标题为《Why the Gain of Reinforcement Learning with Verifiable Rewards Does Not Decompose: A Pre-Registered Intervention Study》的预注册干预研究 [24]（仅标题级，`> 待核实`）。

5. **Agent 与工具使用**已从「能不能用工具」转向「用哪个权限的工具」「评测是否可信」：过度权限工具选择 [26]、工具检索基准 [25]、小模型工具学习弱 [27]、Agent 基准论文披露审计 [29]、计划级安全分解攻击 [33][35]、MCP 安全代理基准 [36][37]、仓库级代码 Agent 评测框架 [40][41]、SWE-bench 在线化 [42]。

6. **MoE 与扩展律**的现实关切从「稀疏激活带来什么收益」转向「部署负担与收益归因」：视觉 MoE 的专家坍缩与骨干算力杠杆 [72]、MoE 部署的专家剪枝 [74]、专家缓存与 token 调度 [66]、专家剪枝与跳过 [67]、MoE upcycling 扩展律 [82]、Chinchilla compute-optimal 的稳健性评估 [83]。

7. **长上下文与推理效率**在本次来源中集中在注意力稀疏化与 KV 压缩：Gated Sparse Attention [110]、百万 token 下注意力汇（attention sinks）是否真被修复 [113]、Memory-Keyed Attention [115]、长上下文扩散 LLM 加速 [117]、多 Agent 共享 KV 池压缩 [122]、分层量化 KV 的自投机解码 [123]。

8. **争议主线**：透明度下降（2025 Foundation Model Transparency Index 平均分 58→40）[9]、评测污染检测 [62]、Agent 基准自身披露不足导致同模型同基准结果矛盾 [29]、「推理期算力是否真的提升鲁棒性」[102] 与「深思反而有害」[88]。

---

## 一、关键前沿进展（近 1–2 年）

> 本节按主题聚类，每条给出**名称 | 时间 | 贡献一句话 | 证据强度**。凡仅有标题级证据者标注 `> 待核实`。

### 1.1 推理与测试时计算

| 名称 | 时间 | 一句话贡献 | 证据强度 |
|---|---|---|---|
| Nemotron-Cascade [101] | 2025-12（arXiv:2512.13607） | 用级联强化学习构建通用推理模型，显式指出推理期响应长度与验证时延的跨域异质性会拖慢训练 | 摘要级（B 级预印本），citations=44 |
| Slow Thinking-based Reasoning LLMs 综述 [99] | 2025（arXiv:2505.02665） | 以 RL + 推理期扩展律组织「慢思考」推理 LLM 的综述 | 标题级，`> 待核实` |
| Solve-Detect-Verify [97] | 2025（arXiv:2505.11966） | 用灵活的生成式验证器做推理期扩展（求解-检测-验证） | 标题级，`> 待核实` |
| HelpSteer3 [98] / Dedicated Feedback and Edit Models [100] | 2025（arXiv:2503.04378，同工作的 DOI 版本） | 人类标注反馈与编辑数据，用于开放式通用任务的推理期扩展 | 标题级，`> 待核实` |
| Sleep-time Compute [86] | 2025（arXiv:2504.13171） | 把部分算力从推理期前移到「休眠期」预计算，超出单纯 test-time 扩展 | 标题级，`> 待核实` |
| Can Test-Time Scaling Improve World Foundation Model? [84] | 2025（arXiv:2503.24320） | 把测试时扩展问题搬到世界基础模型上 | 标题级，`> 待核实` |
| Inference-Time Scaling for Flow Models [94] | 2025（arXiv:2503.19385） | 用随机生成与 rollover 预算强制为流模型做推理期扩展 | 标题级，`> 待核实` |
| On-Policy Distillation through the Lens of Test-Time Scaling [87] | 2026（arXiv:2608.11829，按 ID 前缀推断，`> 待核实`） | 从测试时扩展视角理解在线策略蒸馏 | 标题级，`> 待核实` |

### 1.2 后训练与

## 参考来源

[1] Value Bonuses using Ensemble Errors for Exploration in Reinforcement Learning — http://arxiv.org/abs/2602.12375v1
[2] The Open Ant: A Robot Platform for Reinforcement Learning Research — http://arxiv.org/abs/2607.18488v1
[3] Causal-Paced Deep Reinforcement Learning — http://arxiv.org/abs/2507.02910v1
[4] RLVR-World: Training World Models with Reinforcement Learning — http://arxiv.org/abs/2505.13934v2
[5] Reinforcement Learning Meets Large Language Models: A Survey of Advancements and Applications Across the LLM Lifecycle — http://arxiv.org/abs/2509.16679v1
[6] Reward Models in Deep Reinforcement Learning: A Survey — http://arxiv.org/abs/2506.15421v1
[7] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1
[8] A Tutorial on Meta-Reinforcement Learning — http://arxiv.org/abs/2301.08028v4
[9] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1
[10] NTIRE 2025 Challenge on Image Super-Resolution (x4): Methods and Results — http://arxiv.org/abs/2504.14582v3
[11] AI Alignment and Safety of Large Language Models: A Survey of RLHF, Constitutional AI, Red-Teaming, and Value Learning — https://doi.org/10.5281/zenodo.21366084
[12] Semi-supervised reward learning for offline reinforcement learning — http://arxiv.org/abs/2012.06899v1
[13] AI Alignment and Safety of Large Language Models: A Survey of RLHF, Constitutional AI, Red-Teaming, and Value Learning — https://doi.org/10.5281/zenodo.21366085
[14] Post-Training of Large Language Models: A Comprehensive Survey — https://doi.org/10.2139/ssrn.5979157
[15] Does a Model Forget Differently When the Data Is Its Own? RL's Retention Advantage and Model Collapse Are Claims About the Same Loop, and No Study Has Measured Both — https://doi.org/10.5281/zenodo.22945776
[16] Does a Model Forget Differently When the Data Is Its Own? RL's Retention Advantage and Model Collapse Are Claims About the Same Loop, and No Study Has Measured Both — https://doi.org/10.5281/zenodo.22945775
[17] Molecular Pinball: A Deterministic Chemistry Environment for Benchmarking Reinforcement Learning with Verifiable Rewards — https://doi.org/10.26434/chemrxiv.15001669/v1
[18] MC-R1: Mitigating Hallucinations via Reinforcement Learning with String-Match-Based Verifiable Rewards under Modality Conflicts_supp1-3726309.pdf — https://doi.org/10.1109/tmm.2026.3726309/mm1
[19] Specializing Large Language Models for Process Modeling via Reinforcement Learning with Verifiable and Universal Rewards — https://doi.org/10.36227/techrxiv.175977593.34948838/v1
[20] Group Distributionally Robust Optimization-Driven Reinforcement Learning for LLM Reasoning — http://arxiv.org/abs/2601.19280v1
[21] Strategic Bargaining in Multi-Buyer Markets: Reinforcement Learning from Verifiable Rewards for LLM Negotiations — https://doi.org/10.2139/ssrn.7069958
[22] Specializing Large Language Models for Process Modeling via Reinforcement Learning with Verifiable and Universal Rewards — https://doi.org/10.21203/rs.3.rs-7646566/v1
[23] Navigating the State of Cognitive Flow: Context-Aware AI Interventions for Effective Reasoning Support — http://arxiv.org/abs/2504.16021v1
[24] Why the Gain of Reinforcement Learning with Verifiable Rewards Does Not Decompose: A Pre-Registered Intervention Study — https://doi.org/10.2139/ssrn.7346356
[25] Retrieval Models Aren't Tool-Savvy: Benchmarking Tool Retrieval for Large Language Models — http://arxiv.org/abs/2503.01763v2
[26] When Lower Privileges Suffice: Investigating Over-Privileged Tool Selection in LLM Agents — http://arxiv.org/abs/2606.20023v2
[27] Small LLMs Are Weak Tool Learners: A Multi-LLM Agent — http://arxiv.org/abs/2401.07324v3
[28] TDCOSMO 2025: Cosmological constraints from strong lensing time delays — http://arxiv.org/abs/2506.03023v4
[29] What Twelve LLM Agent Benchmark Papers Disclose About Themselves: A Pilot Audit and an Open Scoring Schema — http://arxiv.org/abs/2605.21404v1
[30] VLSP 2025 MLQA-TSR Challenge: Vietnamese Multimodal Legal Question Answering on Traffic Sign Regulation — http://arxiv.org/abs/2510.20381v1
[31] AIRCC-Clim: a user-friendly tool for generating regional probabilistic climate change scenarios and risk measures — http://arxiv.org/abs/2111.01762v1
[32] SBFT Tool Competition 2025 -- Java Test Case Generation Track — http://arxiv.org/abs/2504.09168v1
[33] Checked at Every Step Is Not Checked as a Whole: Two Senses of Plan-Level Safety for LLM Agents, and Why Decomposition Attacks Exploit the Gap Between Them — https://doi.org/10.5281/zenodo.22961078
[34] Efficient Benchmarking in Production: A Study of an Evolving LLM Agent — http://arxiv.org/abs/2609.21267v1
[35] Checked at Every Step Is Not Checked as a Whole: Two Senses of Plan-Level Safety for LLM Agents, and Why Decomposition Attacks Exploit the Gap Between Them — https://doi.org/10.5281/zenodo.22961077
[36] Measuring the Defenders: A Layer-Aware, Framework-Mapped Benchmark for Model Context Protocol Security Proxies — https://doi.org/10.6084/m9.figshare.32978657
[37] Measuring the Defenders: A Layer-Aware, Framework-Mapped Benchmark for Model Context Protocol Security Proxies — https://doi.org/10.6084/m9.figshare.32978657.v4
[38] MENTOR: Fixing Introductory Programming Assignments With Formula-Based Fault Localization and LLM-Driven Program Repair — https://doi.org/10.5281/zenodo.15678691
[39] MENTOR: Fixing Introductory Programming Assignments With Formula-Based Fault Localization and LLM-Driven Program Repair — https://doi.org/10.5281/zenodo.15678692
[40] Dissecting Repository-Scale Code-Agent Harnesses: Retrieval, Context, and Action Interfaces Under Model-in-the-Loop Evaluation — https://doi.org/10.5281/zenodo.21781710
[41] Dissecting Repository-Scale Code-Agent Harnesses: Retrieval, Context, and Action Interfaces Under Model-in-the-Loop Evaluation — https://doi.org/10.5281/zenodo.21781711
[42] SWE-bench Goes Live! — http://arxiv.org/abs/2505.23419v2
[43] The Gaia mission — http://arxiv.org/abs/1609.04153v1
[44] Gaia Data Release 3: The Galaxy in your preferred colours. Synthetic photometry from Gaia low-resolution spectra — http://arxiv.org/abs/2206.06215v2
[45] Gaia Data Release 1. Summary of the astrometric, photometric, and survey properties — http://arxiv.org/abs/1609.04172v1
[46] LongEval at CLEF 2025: Longitudinal Evaluation of IR Model Performance — http://arxiv.org/abs/2503.08541v1
[47] A Simulation and Modeling of Access Points with Definition Language — http://arxiv.org/abs/1304.1836v2
[48] Superconductivity as a consequence of an ordering of the electron gas zero-point oscillations — http://arxiv.org/abs/1005.0280v6
[49] Image Segmentation in Foundation Model Era: A Survey — http://arxiv.org/abs/2408.12957v3
[50] Vision Mamba: A Comprehensive Survey and Taxonomy — http://arxiv.org/abs/2405.04404v1
[51] AIn't Nothing But a Survey? Using Large Language Models for Coding German Open-Ended Survey Responses on Survey Motivation — http://arxiv.org/abs/2506.14634v3
[52] AI ethics in creative domains: a systematic review of detection, recognition, interpretation, generation, and moral implications in the arts (2000–2025) — https://doi.org/10.1007/s43681-026-01044-z
[53] Replication materials for the paper "Engineering LLM-Based Multi-Agent Systems: A Taxonomy of Emerging Frameworks" — https://doi.org/10.5281/zenodo.19919086
[54] Replication materials for the paper "Engineering LLM-Based Multi-Agent Systems: A Taxonomy of Emerging Frameworks" — https://doi.org/10.5281/zenodo.19919085
[55] Securing IoT Infrastructures Using Honeypot-Based Intrusion Detection (IDS) and AES-256 Encryption: A Comprehensive Survey — https://doi.org/10.5281/zenodo.18470435
[56] Securing IoT Infrastructures Using Honeypot-Based Intrusion Detection (IDS) and AES-256 Encryption: A Comprehensive Survey — https://doi.org/10.5281/zenodo.18470436
[57] PREreview of "Perceptions, Preparedness, and Challenges of Artificial Intelligence Integration in Government Healthcare Institutions in Al Buraimi Governorate, Oman: A Cross‑Sectional Study" — https://doi.org/10.5281/zenodo.22986284
[58] PREreview of "Perceptions, Preparedness, and Challenges of Artificial Intelligence Integration in Government Healthcare Institutions in Al Buraimi Governorate, Oman: A Cross‑Sectional Study" — https://doi.org/10.5281/zenodo.22986283
[59] Overview of the Sensemaking Task at the ELOQUENT 2025 Lab: LLMs as Teachers, Students and Evaluators — http://arxiv.org/abs/2507.12143v1
[60] Annif at SemEval-2025 Task 5: Traditional XMTC augmented by LLMs — http://arxiv.org/abs/2504.19675v2
[61] CEA-LIST at CheckThat! 2025: Evaluating LLMs as Detectors of Bias and Opinion in Text — http://arxiv.org/abs/2507.07539v1
[62] RADAR: Mechanistic Pathways for Detecting Data Contamination in LLM Evaluation — http://arxiv.org/abs/2510.08931v1
[63] Model sensitivity analysis on arxiv — https://doi.org/10.5194/gmd-2018-33-ac4
[64] Analysis of Architecture Options for Foundation-model-based Agents: A Taxonomy and Decision Model — https://doi.org/10.2139/ssrn.5845432
[65] Monocular Depth Estimation in the Foundation Model Era: A Survey — https://doi.org/10.36227/techrxiv.176287942.28438576/v1
[66] ExpertFlow: Efficient Mixture-of-Experts Inference via Predictive Expert Caching and Token Scheduling — http://arxiv.org/abs/2410.17954v2
[67] Not All Experts are Equal: Efficient Expert Pruning and Skipping for Mixture-of-Experts Large Language Models — http://arxiv.org/abs/2402.14800v2
[68] GraphMETRO: Mitigating Complex Graph Distribution Shifts via Mixture of Aligned Experts — http://arxiv.org/abs/2312.04693v3
[69] Mixtures of Experts Models — http://arxiv.org/abs/1806.08200v1
[70] Convergence Rates for Softmax Gating Mixture of Experts — http://arxiv.org/abs/2503.03213v1
[71] A scaling law chaotic system — http://arxiv.org/abs/2111.09816v1
[72] When Does Sparse MoE Help in Vision? The Role of Backbone Compute Leverage in Sparse Routing — http://arxiv.org/abs/2605.15484v1
[73] AIM 2025 Rip Current Segmentation (RipSeg) Challenge Report — http://arxiv.org/abs/2508.13401v3
[74] FlexMoE: One-for-All Nested Intra-Expert Pruning for MoE Language Models — http://arxiv.org/abs/2606.27866v1
[75] Inaugural MOASEI Competition at AAMAS'2025: A Technical Report — http://arxiv.org/abs/2507.05469v1
[76] Quantitative Analysis of Performance Drop in DeepSeek Model Quantization — http://arxiv.org/abs/2505.02390v2
[77] Qwen3-ASR Technical Report — http://arxiv.org/abs/2601.21337v2
[78] Qwen3-TTS Technical Report — http://arxiv.org/abs/2601.15621v1
[79] Qwen3-Omni Technical Report — http://arxiv.org/abs/2509.17765v1
[80] DeepSeq: High-Throughput Single-Cell RNA Sequencing Data Labeling via Web Search-Augmented Agentic Generative AI Foundation Models — http://arxiv.org/abs/2506.13817v1
[81] Robust Tabular Foundation Models — http://arxiv.org/abs/2512.03307v1
[82] Scaling Laws for Upcycling Mixture-of-Experts Language Models — http://arxiv.org/abs/2502.03009v2
[83] Evaluating the Robustness of Chinchilla Compute-Optimal Scaling — https://arxiv.org/abs/2509.23963
[84] Can Test-Time Scaling Improve World Foundation Model? — https://arxiv.org/abs/2503.24320
[85] ACM COMPUTE 2025 Best Practices Track Proceedings — http://arxiv.org/abs/2512.02349v2
[86] Sleep-time Compute: Beyond Inference Scaling at Test-time — http://arxiv.org/abs/2504.13171v1
[87] Towards Understanding On-Policy Distillation through the Lens of Test-Time Scaling — http://arxiv.org/abs/2608.11829v3
[88] When Deliberation Hurts: Inverse Test-Time Scaling, Unfaithful Traces, and the Case Against a Unified System-2 in LLM Reasoning — https://doi.org/10.5281/zenodo.22904980
[89] When Deliberation Hurts: Inverse Test-Time Scaling, Unfaithful Traces, and the Case Against a Unified System-2 in LLM Reasoning — https://doi.org/10.5281/zenodo.23022324
[90] When Deliberation Hurts: Inverse Test-Time Scaling, Unfaithful Traces, and the Case Against a Unified System-2 in LLM Reasoning — https://doi.org/10.5281/zenodo.22904981
[91] Culturally Grounded Physical Commonsense Reasoning in Italian and English: A Submission to the MRL 2025 Shared Task — http://arxiv.org/abs/2510.22631v1
[92] RMIT-ADM+S at the MMU-RAG NeurIPS 2025 Competition — http://arxiv.org/abs/2602.20735v1
[93] NightFeats @ MMU-RAGent NeurIPS 2025: A Context-Optimized Multi-Agent RAG System for the Text-to-Text Track — http://arxiv.org/abs/2606.11199v1
[94] Inference-Time Scaling for Flow Models via Stochastic Generation and Rollover Budget Forcing — http://arxiv.org/abs/2503.19385v5
[95] NeurIPS should lead scientific consensus on AI policy — http://arxiv.org/abs/2510.00075v1
[96] MARS2 2025 Challenge on Multimodal Reasoning: Datasets, Methods, Results, Discussion, and Outlook — http://arxiv.org/abs/2509.14142v1
[97] Solve-Detect-Verify: Inference-Time Scaling with Flexible Generative Verifier — https://arxiv.org/abs/2505.11966
[98] HelpSteer3: Human-Annotated Feedback and Edit Data to Empower Inference-Time Scaling in Open-Ended General-Domain Tasks — https://arxiv.org/abs/2503.04378
[99] A Survey of Slow Thinking-based Reasoning LLMs using Reinforced Learning and Inference-time Scaling Law — https://arxiv.org/abs/2505.02665
[100] Dedicated Feedback and Edit Models Empower Inference-Time Scaling for Open-Ended General-Domain Tasks — https://doi.org/10.48550/arXiv.2503.04378
[101] Nemotron-Cascade: Scaling Cascaded Reinforcement Learning for General-Purpose Reasoning Models — https://arxiv.org/abs/2512.13607
[102] Does More Inference-Time Compute Really Help Robustness? — https://arxiv.org/abs/2507.15974
[103] Evaluating Open-Source Vision-Language Models for Multimodal Sarcasm Detection — http://arxiv.org/abs/2510.11852v1
[104] Hierarchical Pre-Training of Vision Encoders with Large Language Model — http://arxiv.org/abs/2604.00086v2
[105] 1$^{st}$ Place Solution of WWW 2025 EReL@MIR Workshop Multimodal CTR Prediction Challenge — http://arxiv.org/abs/2505.03543v1
[106] Multilingual and Multimodal LLMs in the Wild: Building for Low-Resource Languages — http://arxiv.org/abs/2605.17152v1
[107] Vision-Language Model for Object Detection and Segmentation: A Review and Evaluation — http://arxiv.org/abs/2504.09480v1
[108] Application of transformer models in medical image segmentation: a narrative review — https://doi.org/10.21037/qims-2025-aw-2381
[109] TinyGiantVLM: A Lightweight Vision-Language Architecture for Spatial Reasoning under Resource Constraints — http://arxiv.org/abs/2508.17595v1
[110] Gated Sparse Attention: Combining Computational Efficiency with Training Stability for Long-Context Language Models — http://arxiv.org/abs/2601.15305v1
[111] Oral MLLM Scoping Review Protocol: Multimodal Large Language Models in Stomatology — https://doi.org/10.17605/osf.io/rx8sm
[112] Technical Report for Ego4D Long-Term Action Anticipation Challenge 2025 — http://arxiv.org/abs/2506.02550v2
[113] Do New Attention Mechanisms Actually Fix Attention Sinks at Million-Token Context? — http://arxiv.org/abs/2609.08574v2
[114] Self-Evolving Autonomous Software Architectures Using Large-Scale Graph Neural Networks and Real-Time Big Data Feedback Loops for Economic Optimization and Cost-Efficient Resource Allocation — https://doi.org/10.63544/jbii.v5i5.188
[115] MKA: Memory-Keyed Attention for Efficient Long-Context Reasoning — http://arxiv.org/abs/2603.20586v2
[116] Bridging LLMs and Symbolic Reasoning in Educational QA Systems: Insights from the XAI Challenge at IJCNN 2025 — http://arxiv.org/abs/2508.01263v1
[117] Focus-dLLM: Accelerating Long-Context Diffusion LLM Inference via Confidence-Guided Context Focusing — http://arxiv.org/abs/2602.02159v1
[118] SINAI at eRisk@CLEF 2025: Transformer-Based and Conversational Strategies for Depression Detection — http://arxiv.org/abs/2509.19861v1
[119] Predicting How Transformers Attend Analytic Power-Law Theory, Phase Transitions, and Practical Compression Tools — https://doi.org/10.5281/zenodo.20314038
[120] A systematic review of transformer-enhanced UNet architectures for 3D medical image segmentation: Trends, challenges, and the ATD-TᵣEEv framework — https://doi.org/10.1016/j.compbiolchem.2026.109084
[121] Predicting How Transformers Attend Analytic Power-Law Theory, Phase Transitions, and Practical Compression Tools — https://doi.org/10.5281/zenodo.19826342
[122] PolyKV: A Shared Asymmetrically-Compressed KV Cache Pool for Multi-Agent LLM Inference — http://arxiv.org/abs/2604.24971v1
[123] QuantSpec: Self-Speculative Decoding with Hierarchical Quantized KV Cache — http://arxiv.org/abs/2502.10424v1


---

*Generated by research-bot · topic=`ai` · depth=`standard` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading · model=`deepseek-v4-flash` · sources=123 · duration=342s · 2026-10-02T22:07:42+00:00*
