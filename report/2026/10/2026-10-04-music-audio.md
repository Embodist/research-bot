# 音乐与音频算法调研报告：MIR、音乐生成与理解、歌声转换、音源分离与自监督音频表征

**日期**：2026-10-04（UTC） ｜ **领域**：Music & Audio（MIR / Generation / Understanding / Separation） ｜ **检索源数量**：可引用证据源 88 条（本报告正文引用 55 条）+ 题面提供的种子资源 12 条 ｜ **覆盖子问题**：8 个，其中 **3 个（q4 歌声转换/分离/翻唱识别、q5 数据集与挑战赛、r2q1 评测指标有效性）在本次抽取中零检出**，对应章节以显式证据缺口呈现

> **方法学与证据纪律说明**
> 1. 本报告严格只引用任务给定的 [1]–[88] 编号来源与题面种子资源链接，未新增任何 URL；凡检索结果未覆盖之处一律标注 `> 待核实`。
> 2. 四类证据轴（**热度** citations/star/下载、**权威** venue/同行评审/维护机构、**关注度** 高/中/低 + 依据、**推荐度** ★1–5）逐条给出；候选块未提供热度数字者一律写 `> 待核实`，**未编造任何引用数、star 数或榜单排名**。
> 3. 本次候选集合存在明显**检索噪声**：如遥感数据增强 [6]、拜占庭鲁棒 SGD [8]、引力波讲义 [67]、小行星大气进入 [68]、选举信息操作 [69]、图像超分挑战 [83]、越南法律问答 [84]、强透镜宇宙学 [86] 等与音乐音频无关，已剔除；另有实时视频生成 [59]、数字人视频合成 [55]、电信语音智能体 [53]、车辆边缘计算 [47]、多通道直播 [45]、LabVIEW 电机诊断 [49] 属于"实时/低延迟"关键词误召回，仅在本报告第五章作为**反例**说明检索偏差。
> 4. 证据等级：A=同行评审/官方技术报告；B=arXiv 预印本/官方仓库；C=第三方复现/榜单；D=社区内容。本次绝大多数条目为 **B 级预印本**，这是本报告最需要读者警惕的系统性局限。

---

## 摘要（Executive Summary）

- **音乐生成（Music Generation）**：2024–2026 年的主流叙事是"自回归 + 扩散两条路线并存"，但本次检索**未能取得任何自回归音乐 token 模型的具名一手证据**（模型名、架构、指标均缺失），因此"扩散 vs 自回归"的实证对比在本报告内**无法完成** [25] `> 待核实`。可核查的前沿集中在**可控/编辑式生成**：辅助条件分支的受控消融 [25]、指令微调编辑 [21]、音频提示轻量适配 [23]、情感对齐生成 [80]、低资源竞赛配方 [81]。
- **音乐理解与自监督表征**：CultureMERT-95M 用两阶段持续预训练在 650 小时希腊/土耳其/印度音乐数据上适配，非西方 auto-tagging 任务 ROC-AUC 与 AP 平均提升 **4.9%** 且对西方基准遗忘极小 [4]；音频-语言模型已用于开放集零样本音乐标注（MAE 编码器 + Falcon7B 解码器 + perceiver resampler）[11]；音乐字幕（music audio captioning）自 MusCaps 起被形式化 [9]；CLAP 类通用音频-语言表示仍在演进 [36]。
- **音乐源分离（Music Source Separation, MSS）**：方法演进呈现"架构改进（Band-Split RoPE Transformer [40]、X-scheme 多域损失+桥接 [10]）+ 低延迟/实时化 [46][62][57] + 评测反思 [43][39]"三条线；**波形域端到端分离的可行性早在 2018 年即被系统讨论** [42]，Demucs 系工程栈已开源（种子资源）。
- **翻唱识别（CSI）与歌声转换（SVC）**：本次检索**零检出**。仅有相邻任务的挑战赛证据——歌声深伪检测 SVDD 2024 [38] 与语音隐私 Voice Privacy 2024（非音乐 SVC）[65]。**任何关于 SVC/CSI 前沿方法的结论在本报告内都不可核查** `> 待核实`。
- **评测指标**：FAD 自 2018 年提出 [29] 后被发现存在**任务诱导的编码器偏置** [30]，并已被专门改造用于生成式音乐评测 [31]；SDR 早在 2018 年就被质疑"half-baked" [43]，2026 年进一步出现"Beyond SDR"的再反思 [39]。**指标滥用是本领域最稳固的批判性共识**。
- **版权、授权与治理**：已有针对 Suno/Udio 的文本条件 AI 音乐**真实使用数据**分析 [64]、以机器遗忘实现 opt-out 的初步实验 [7]、从"数据压缩"角度论证模型权重与版权关系的理论工作 [2]、隐私与版权的生命周期视角 [73]、以及公平性 [71][74] 与透明度指数 [66]。**训练数据披露与 opt-out 机制仍无统一行业标准**。
- **最大缺口**：数据集/基准章节（第五章）与评测指标章节（r2q1）在本次抽取中为空；翻唱识别与歌声转换无一手来源；音乐生成缺少跨模型可比榜单。以上均以 `> 待核实` 显式标注，不做事后补写。

---

## 一、关键前沿进展（近 1–2 年）

### 1.1 可控与编辑式文本到音乐生成（Controllable & Editable Text-to-Music）

**受控消融下的条件分支作用。** 在仅器乐（instrumental-only）文本到音乐任务上，作者以 DiT（Diffusion Transformer）为骨干，引入歌词（lyric）与音色（timbre）辅助条件分支，并做"退化条件信号"的受控消融：去掉这些分支后模型在 **AudioBox aesthetics、LLM-as-judge、human MOS** 三类口径上得分下降，而把节省出的参数转为更深的 DiT 仅能带来**边际恢复**；作者据此提出辅助分支"可能充当训练期架构锚点（training-time architectural anchors）"的推断性解释 [25]。
> **热度**：`> 待核实`（候选块未提供 citations/star/下载数据）[25]
> **权威**：arXiv 预印本（cs.SD），单作者，未见同行评审 venue [25]
> **关注度**：低 —— 依据：新预印本，候选块无引用/讨论/榜单信号 [25]
> **推荐度**：★★★★☆ —— 三类评测口径齐全、消融设计可控，是"条件机制是否真在起作用"这一问题的高相关样本，但结论需独立复现 [25]

**编辑与指令化路线。** Instruct-MusicGen 通过指令微调把音乐语言模型开放给文本到音乐**编辑**任务 [21]；Audio Prompt Adapter 用轻量微调释放文本到音乐的编辑能力 [23]；IteraTTA 提供同时探索文本提示与音频先验的交互界面 [26]。这三者共同指向"生成 → 编辑 → 人机迭代"的工作流转变。
> **热度**：`> 待核实`（候选块未给引用数/star）[21][23][26]
> **权威**：均为 arXiv 预印本（cs.SD / eess.AS），未标注同行评审 [21][23][26]
> **关注度**：低 —— 依据：候选块无热度信号 `> 待核实` [21][23][26]
> **推荐度**：★★★☆☆ —— 属"可控生成"主线但本报告仅有标题级信息，具体指标与基线对比 `> 待核实` [21][23]

**情感对齐生成。** Story2MIDI 用序列到序列 Transformer 从文本生成情感一致的音乐：先合并"文本情感分析数据集"与"音乐情感分类数据集"构造 **Story2MIDI dataset**（唤起相同情感的文本短句—音乐片段配对），输出 MIDI 序列而非音频波形 [80]。
> **热度**：`> 待核实` [80]
> **权威**：arXiv 预印本（cs.SD），8 页短文，多作者（含 Johanna Devaney、Sarah Ita Levitan），未见同行评审 venue [80]
> **关注度**：低 —— 依据：候选块无引用/榜单信号，数据集为作者自建 [80]
> **推荐度**：★★★★☆ —— 是"情感条件"这一可控生成分支中少见的、附数据集构建流程的工作，输出 MIDI 可解释性强；受限于小数据与有限算力 [80]

**低资源竞赛配方。** ICME 2026 Academic Text-to-Music Generation Grand Challenge 的参赛报告指出：训练数据按**文本嵌入聚类**分组优于按音频嵌入聚类，且聚类粒度对不同评测指标影响方向不一致（中等聚类数表现较优），研究场景限定为低数据、小模型 [81]。
> **热度**：`> 待核实`（候选块未给名次）[81]
> **权威**：arXiv 预印本（cs.SD），竞赛参赛提交（含竞赛评测背景）[81]
> **关注度**：低 —— 依据：单队提交预印本，无引用/名次信号 [81]
> **推荐度**：★★★☆☆ —— 对低资源训练配方有直接工程参考价值，但为单队自述，须对照挑战赛官方结果 [81]

**并行解码与扩散提速。** IMPACT 提出迭代式掩码并行解码（iterative mask-based parallel decoding）用于扩散建模的文本到音频生成，直面 Tango/AudioLDM 系列"高保真但推理开销大"的问题 [22]；Fast Timing-Conditioned Latent Audio Diffusion 关注快速、带时序条件的潜空间音频扩散 [28]。
> **热度**：`> 待核实` [22][28]
> **权威**：arXiv 预印本（eess.AS / cs.SD），未标注同行评审 [22][28]
> **关注度**：低 —— 依据：候选块无热度信号 [22]
> **推荐度**：★★★☆☆ —— 推理效率是生成音乐落地的关键瓶颈，值得与实时化工作交叉阅读 [22][28]

### 1.2 跨文化表征与音乐基础模型（Cross-Cultural Representation）

CultureMERT-95M 在 650 小时融合希腊、土耳其、印度音乐传统的数据混合上做**两阶段持续预训练**（learning rate re-warming + re-decaying），在多种非西方音乐 auto-tagging 任务上 ROC-AUC 与 AP **平均提升 4.9%**，超过此前 SOTA，且对以西方为中心的基准仅有**极小遗忘** [4]。
> **热度**：`> 待核实`（候选块未提供 citations/star/榜单）[4]
> **权威**：arXiv 预印本（cs.SD，2506.17818v1），未标注同行评审或会议录用 [4]
> **关注度**：低 —— 依据：候选块无引用/下载/榜单信号，无法判断社区关注度 [4]
> **推荐度**：★★★★☆ —— 同时回应"跨文化泛化"与"灾难性遗忘"两个真实痛点，指标具体可核查，是本报告中最值得精读的音乐表征工作；但缺乏第三方复现 [4]

跨文化评测侧，GlobalMood 提出跨文化音乐情绪识别（music emotion recognition）基准，指出既有数据集**以西方歌曲与英文派生术语为主**

## 参考来源

[1] The IEEE-IS2 2024 Music Packet Loss Concealment Challenge — http://arxiv.org/abs/2409.18564v1
[2] Training Foundation Models as Data Compression: On Information, Model Weights and Copyright Law — http://arxiv.org/abs/2407.13493v4
[3] Improving Choral Music Separation through Expressive Synthesized Data from Sampled Instruments — http://arxiv.org/abs/2209.02871v1
[4] CultureMERT: Continual Pre-Training for Cross-Cultural Music Representation Learning — http://arxiv.org/abs/2506.17818v1
[5] Music SketchNet: Controllable Music Generation via Factorized Representations of Pitch and Rhythm — http://arxiv.org/abs/2008.01291v1
[6] TerraGen: A Unified Multi-Task Layout Generation Framework for Remote Sensing Data Augmentation — http://arxiv.org/abs/2510.21391v1
[7] No Encore: Unlearning as Opt-Out in Music Generation — http://arxiv.org/abs/2509.06277v2
[8] Byzantine-Resilient SGD in High Dimensions on Heterogeneous Data — http://arxiv.org/abs/2005.07866v1
[9] MusCaps: Generating Captions for Music Audio — http://arxiv.org/abs/2104.11984v1
[10] The Whole Is Greater than the Sum of Its Parts: Improving Music Source Separation by Bridging Network — http://arxiv.org/abs/2305.07855v2
[11] Joint Music and Language Attention Models for Zero-shot Music Tagging — http://arxiv.org/abs/2310.10159v1
[12] Introduction to Gestural Similarity in Music. An Application of Category Theory to the Orchestra — http://arxiv.org/abs/1904.10340v1
[13] Symbolic Music Representations for Classification Tasks: A Systematic Evaluation — http://arxiv.org/abs/2309.02567v2
[14] Network Modulation Synthesis: New Algorithms for Generating Musical Audio Using Autoencoder Networks — http://arxiv.org/abs/2109.01948v1
[15] Dorabella Cipher as Musical Inspiration — http://arxiv.org/abs/2509.17950v1
[16] GlobalMood: A cross-cultural benchmark for music emotion recognition — http://arxiv.org/abs/2505.09539v2
[17] A Functional Taxonomy of Music Generation Systems — http://arxiv.org/abs/1812.04186v1
[18] MIRFLEX: Music Information Retrieval Feature Library for Extraction — http://arxiv.org/abs/2411.00469v1
[19] Towards Multimodal MIR: Predicting individual differences from music-induced movement — http://arxiv.org/abs/2007.10695v1
[20] Barwise Music Structure Analysis with the Correlation Block-Matching Segmentation Algorithm — http://arxiv.org/abs/2311.18604v1
[21] Instruct-MusicGen: Unlocking Text-to-Music Editing for Music Language Models via Instruction Tuning — http://arxiv.org/abs/2405.18386v3
[22] IMPACT: Iterative Mask-based Parallel Decoding for Text-to-Audio Generation with Diffusion Modeling — http://arxiv.org/abs/2506.00736v1
[23] Audio Prompt Adapter: Unleashing Music Editing Abilities for Text-to-Music with Lightweight Finetuning — http://arxiv.org/abs/2407.16564v2
[24] Baseline Systems For The 2025 Low-Resource Audio Codec Challenge — http://arxiv.org/abs/2510.00264v3
[25] Instrumental Text-to-Music Generation with Auxiliary Conditioning Branches — http://arxiv.org/abs/2605.21433v1
[26] IteraTTA: An interface for exploring both text prompts and audio priors in generating music with text-to-audio models — http://arxiv.org/abs/2307.13005v1
[27] Vision-to-Music Generation: A Survey — http://arxiv.org/abs/2503.21254v1
[28] Fast Timing-Conditioned Latent Audio Diffusion — http://arxiv.org/abs/2402.04825v3
[29] Fréchet Audio Distance: A Metric for Evaluating Music Enhancement Algorithms — http://arxiv.org/abs/1812.08466v4
[30] An Empirical Analysis of Task-Induced Encoder Bias in Fréchet Audio Distance — http://arxiv.org/abs/2602.23958v2
[31] Adapting Frechet Audio Distance for Generative Music Evaluation — http://arxiv.org/abs/2311.01616v2
[32] Generation of lyrics lines conditioned on music audio clips — http://arxiv.org/abs/2009.14375v1
[33] Digital Audio Processing Tools for Music Corpus Studies — http://arxiv.org/abs/2111.03895v2
[34] Unified Cross-modal Translation of Score Images, Symbolic Music, and Performance Audio — http://arxiv.org/abs/2505.12863v1
[35] OpenFact at CheckThat! 2024: Combining Multiple Attack Methods for Effective Adversarial Text Generation — http://arxiv.org/abs/2409.02649v2
[36] M2D-CLAP: Exploring General-purpose Audio-Language Representations Beyond CLAP — http://arxiv.org/abs/2503.22104v2
[37] Learning to Traverse Latent Spaces for Musical Score Inpainting — http://arxiv.org/abs/1907.01164v1
[38] SVDD Challenge 2024: A Singing Voice Deepfake Detection Challenge Evaluation Plan — http://arxiv.org/abs/2405.05244v1
[39] Beyond SDR: How Music Source Separation Reshapes Rhythm-Relevant Signal Properties — http://arxiv.org/abs/2609.04224v1
[40] Music Source Separation with Band-Split RoPE Transformer — http://arxiv.org/abs/2309.02612v2
[41] Sanidha: A Studio Quality Multi-Modal Dataset for Carnatic Music — http://arxiv.org/abs/2501.06959v1
[42] End-to-end music source separation: is it possible in the waveform domain? — http://arxiv.org/abs/1810.12187v2
[43] SDR - half-baked or well done? — http://arxiv.org/abs/1811.02508v1
[44] Rights by Architecture: A Human-Compatible Sociotechnical Layer for Digital Protection Across Regulatory Regimes — http://arxiv.org/abs/2609.02455v1
[45] A 3D Framework for Improving Low-Latency Multi-Channel Live Streaming — http://arxiv.org/abs/2410.16284v2
[46] Towards Practical Real-Time Low-Latency Music Source Separation — https://arxiv.org/abs/2511.13146
[47] Real-Time Service Subscription and Adaptive Offloading Control in Vehicular Edge Computing — http://arxiv.org/abs/2512.14002v1
[48] LK Jam: System Architecture and Implementation of a Real-Time Human-AI Interactive Music Generation System using Role-Aware GRU — http://arxiv.org/abs/2606.21018v1
[49] Real time state monitoring and fault diagnosis system for motor based on LabVIEW — http://arxiv.org/abs/1806.09998v1
[50] Gesture2Music: A Low-Latency Real-Time Framework for Continuous Gesture-Driven Music Generation — http://arxiv.org/abs/2511.00793v2
[51] Gesture2Music: A Low-Latency Real-Time Framework for Continuous Gesture-Driven Music Generation — https://arxiv.org/abs/2511.00793
[52] Advancing Multi-Instrument Music Transcription: Results from the 2025 AMT Challenge — http://arxiv.org/abs/2603.27528v1
[53] Toward Low-Latency End-to-End Voice Agents for Telecommunications Using Streaming ASR, Quantized LLMs, and Real-Time TTS — https://arxiv.org/abs/2508.04721
[54] SAGE-Music: Low-Latency Symbolic Music Generation via Attribute-Specialized Key-Value Head Sharing — https://arxiv.org/abs/2510.00395
[55] MIDAS: Multimodal Interactive Digital-humAn Synthesis via Real-time Autoregressive Video Generation — https://arxiv.org/abs/2508.19320
[56] Real-Time and Low-Latency Processing in Computer Vision: ALiterature Review — https://doi.org/10.71063/djttt.2025.1204
[57] Low Latency Time Domain Multichannel Speech and Music Source Separation — http://arxiv.org/abs/2204.05609v1
[58] A Lightweight Video Streaming Framework for Low-End Systems Using FFMPEG and UDP for Real-Time Transmission — https://doi.org/10.1109/GCON65540.2025.11173312
[59] Rolling Forcing: Autoregressive Long Video Diffusion in Real Time — https://arxiv.org/abs/2509.25161
[60] Multi-Stage Music Source Restoration with BandSplit-RoFormer Separation and HiFi++ GAN — http://arxiv.org/abs/2603.04032v1
[61] Audio query-based music source separation — http://arxiv.org/abs/1908.06593v1
[62] Real-Time Low-Latency Music Source Separation Using Hybrid Spectrogram-Tasnet — https://arxiv.org/abs/2402.17701
[63] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1
[64] Data-Driven Analysis of Text-Conditioned AI-Generated Music: A Case Study with Suno and Udio — http://arxiv.org/abs/2509.11824v1
[65] NTU-NPU System for Voice Privacy 2024 Challenge — http://arxiv.org/abs/2410.02371v1
[66] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1
[67] Discovery Opportunities with Gravitational Waves -- TASI 2024 Lecture Notes — http://arxiv.org/abs/2409.08956v1
[68] Atmospheric entry and fragmentation of small asteroid 2024 BX1: Bolide trajectory, orbit, dynamics, light curve, and spectrum — http://arxiv.org/abs/2403.00634v2
[69] Uncovering Coordinated Cross-Platform Information Operations Threatening the Integrity of the 2024 U.S. Presidential Election Online Discussion — http://arxiv.org/abs/2409.15402v2
[70] ICAGC 2024: Inspirational and Convincing Audio Generation Challenge 2024 — http://arxiv.org/abs/2407.12038v2
[71] Who Gets Heard? Rethinking Fairness in AI for Music Systems — http://arxiv.org/abs/2511.05953v1
[72] Penalizing Transparency? How AI Disclosure and Author Demographics Shape Human and AI Judgments About Writing — http://arxiv.org/abs/2507.01418v1
[73] Privacy and Copyright Protection in Generative AI: A Lifecycle Perspective — http://arxiv.org/abs/2311.18252v3
[74] Opening Musical Creativity? Embedded Ideologies in Generative-AI Music Systems — http://arxiv.org/abs/2508.08805v1
[75] "Melatonin": A Case Study on AI-induced Musical Style — http://arxiv.org/abs/2208.08968v1
[76] Representation Learning of Music Using Artist Labels — http://arxiv.org/abs/1710.06648v2
[77] Representation Learning of Music Using Artist, Album, and Track Information — http://arxiv.org/abs/1906.11783v1
[78] Text-to-image Diffusion Models in Generative AI: A Survey — http://arxiv.org/abs/2303.07909v3
[79] Music Transformer — http://arxiv.org/abs/1809.04281v3
[80] Story2MIDI: Emotionally Aligned Music Generation from Text — http://arxiv.org/abs/2512.02192v1
[81] UT-AISTimprt submission for ICME 2026 Grand Challenge on Academic Text-to-Music Generation — http://arxiv.org/abs/2607.01669v1
[82] Controllable Generation with Text-to-Image Diffusion Models: A Survey — http://arxiv.org/abs/2403.04279v2
[83] NTIRE 2025 Challenge on Image Super-Resolution (x4): Methods and Results — http://arxiv.org/abs/2504.14582v3
[84] VLSP 2025 MLQA-TSR Challenge: Vietnamese Multimodal Legal Question Answering on Traffic Sign Regulation — http://arxiv.org/abs/2510.20381v1
[85] The AudioMOS Challenge 2025 — http://arxiv.org/abs/2509.01336v1
[86] TDCOSMO 2025: Cosmological constraints from strong lensing time delays — http://arxiv.org/abs/2506.03023v4
[87] TRUST 2025: SCRITA and RTSS @ RO-MAN 2025 — http://arxiv.org/abs/2509.11402v1
[88] Event-Enriched Image Analysis Grand Challenge at ACM Multimedia 2025 — http://arxiv.org/abs/2508.18904v1


---

*Generated by research-bot · topic=`music-audio` · depth=`standard` · rounds=2 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading · model=`deepseek-v4-flash` · sources=88 · duration=2029s · 2026-10-04T04:48:04+00:00*
