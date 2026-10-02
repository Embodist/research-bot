# 音乐与音频算法领域地图：MIR / 生成 / 理解 / 分离（2024–2026 前沿 + 经典谱系）

**日期**：2026-10-02（UTC）
**领域**：Music & Audio —— 音乐信息检索（MIR）、翻唱识别（CSI）、音乐生成、音乐理解与自监督表征、歌声转换（SVC）、音乐源分离（MSS）
**检索源规模**：119 条编号证据来源（arXiv / TISMIR / DOI 期刊与会议）+ 12 条人工维护种子资源（仅保留链接，未实时核验热度）
**证据分级约定**：A = 同行评审期刊/会议正式论文；B = arXiv 预印本、官方仓库/挑战赛技术报告；C = 第三方榜单/复现；D = 社区解读。**本报告中绝大多数条目为 B 级（预印本），仅少量为 A 级（DOI 期刊论文）**；凡候选块未提供的数字（引用数、star、下载量），一律写 `> 待核实`，不进行任何估算或补全。

---

## 摘要（Executive Summary）

1. **范式三段式已经成立并正在被基础模型收口**：从手工特征/符号序列建模，到深度表征学习，再到"自监督预训练 + 下游微调/持续预训练"的音乐基础模型。这一判断的支撑证据包括：在 25 年 ISMIR  authorship 的计量分析 [31]、符号音乐表征的系统评估 [26]、以及以"音乐基础模型"为出发点做跨文化持续预训练的 CultureMERT-95M [103]。
2. **近两年最密集的增量出现在四个位置**：(a) 自监督/潜空间预测类音频表征（Audio-JEPA [109]、MATPAC++ [107]、USAD [118]）；(b) 神经音频编解码（Low-Resource Audio Codec Challenge 基线 [57]、HiFi-Codec [117]、codec 可解释性 [119]）；(c) 零样本歌声转换（HQ-SVC [83]、YingMusic-SVC [84]、Poly-SVC [87]、kNN-SVC [85]）；(d) 音乐源分离/修复的架构迭代（Band-Split RoPE Transformer [54]、多阶段 MSR 系统 [52]）。
3. **生成侧的主流仍是"文本/符号条件 + 可控性"两条线**：文本到音乐（Instrumental TTM with auxiliary conditioning [3]、ICME 2026 学术赛道 [4]）与符号音乐生成（SSM/扩散 [5]、Transformer 规模-数据-指标对比研究 [8]、SegTune 细粒度控制 [22]）。
4. **评测体系"跟不上"是有据可查的**：歌唱转换挑战赛（SVC Challenge 2025）给出了系统性结果分析 [90][95]；双耳源分离指标可靠性被专门质疑 [72]；最先进 beat tracking 在主流打击乐数据集上近乎完美，但在 SMC 数据集上存在明显失败模式 [43]；自动歌词转写仍受伴奏干扰制约 [53]。
5. **伦理与版权议题已进入顶会论文正文**：生成式 AI 音乐系统的"民主化"修辞与实际落差 [49]；AI 音乐系统公平性 [60]；AI 音乐论文伦理声明的有效性 [61]；生成模型"遗忘/退出"机制 [65]；针对非法翻唱的防御方案 SongBsAb [20]；音频 deepfake 溯源 [59]。
6. **检索缺口须诚实标注**：本次结构化发现中的 q6（"开源项目/权重/数据集/开放争议"）候选批次**整体与子问题主题不匹配**，多为 cs.SD 音频条目且未能覆盖该子问题所列清单；相关结论在下文以 `> 待核实` 标注，并以种子资源表格与挑战赛信息作为替代证据。详见第七章。

---

## 一、关键前沿进展（近 1–2 年）

> 本章条目均按"名称 / 时间 / 一句话贡献 / 四类证据"给出。所有时间以来源标注年份为准。

### 1.1 表征与基础模型（2025–2026）

| 名称 | 时间 | 一句话贡献 | 热度 | 权威 | 关注度 | 推荐度 |
|---|---|---|---|---|---|---|
| CultureMERT-95M [103] | 2025 | 对既有音乐基础模型做跨文化持续预训练，缓解多音乐传统下的表征不足 | `> 待核实` [103] | arXiv 预印本（cs.SD），未见同行评审 venue [103] | `> 待核实`（候选块无引用/star）[103] | ★★★★☆ 跨文化偏差是该领域公认痛点，值得跟进 [103] |
| Audio-JEPA [109] | 2025 | 将 JEPA（在高层特征空间预测被掩码区域潜表征）迁移到音频 | citations=22 [109] | arXiv 预印本 [109] | 中（citations=22）[109] | ★★★★☆ 新自监督范式在音频上的代表性尝试 [109] |
| MATPAC++ [107] | 2025 | 系统研究掩码潜预测中 predictor 模块的作用 | citations=9 [107] | arXiv 预印本 [107] | 中（citations=9）[107] | ★★★★☆ 直接回答"SSL 里哪个组件真正起作用" [107] |
| USAD [118] | 2025 | 通过蒸馏获得统一的语音+音频表征 | `> 待核实` [118] | arXiv 预印本 [118] | `> 待核实` [118] | ★★★★☆ "语音/音乐统一表征"路线的可复用节点 [118] |
| M2D-CLAP [63] | 2025 | 探索超越 CLAP 的通用音频-语言表征 | `> 待核实` [63] | arXiv 预印本 [63] | `> 待核实` [63] | ★★★★☆ 音频-语言对齐基线的下一代候选 [63] |

### 1.2 歌声转换（零样本、真实歌曲鲁棒性）

- **YingMusic-SVC** [84]：面向真实歌曲的零样本 SVC，显式处理**和声干扰、F0 误差、缺乏歌唱归纳偏置**三类失败源，采用 Flow-GRPO。热度 `> 待核实` [84]；权威 arXiv 预印本 [84]；关注度 `> 待核实` [84]；推荐度 ★★★★☆（把"真实混音"作为一等公民，[84]）。
- **Poly-SVC** [87]：指出既有 SVC 依赖 F0 提取器从"干净人声"取主旋律，而在有伴奏场景下无从可靠提取，因此引入和声建模做复音感知转换。推荐度 ★★★★☆ [87]。
- **HQ-SVC** [83]：低资源场景下的高质量零样本 SVC，批评既有方法"分离建模音色与内容"导致声学信息丢失。推荐度 ★★★★☆ [83]。
- **kNN-SVC** [85]：加法合成 + 拼接平滑度优化的鲁棒零样本路线。推荐度 ★★★☆☆ [85]。
- **SVC Challenge 2025 结果深度分析** [90][95]：受控环境下对多系统做比较与归因，是本领域最重要的公开评测复盘之一。权威：挑战赛分析论文（B 级）[90]；热度 `> 待核实`；推荐度 ★★★★★（评测口径必读）。

### 1.3 音乐源分离与修复

- **多阶段 MSR（CP-JKU，ICASSP 2026 MSR Challenge）** [52]：BandSplit-RoFormer 分离 8 个 stem + 1 辅助 stem，采用三阶段课程（4-stem LoRA 热启动微调 → head expansion 扩展到 8-stem），再以 HiFi++ GAN 做波形修复并为 8 种乐器特化专家。权威：会议挑战赛技术报告 [52]；热度 `> 待核实` [52]；关注度 `> 待核实` [52]；推荐度 ★★★★☆（当前 MSR 任务最完整的工程解法）[52]。
- **Band-Split RoPE Transformer** [54]：MSS 的骨干架构之一，被后续系统复用 [52][54]。推荐度 ★★★★☆。
- **双耳 MSS 指标可靠性** [72]：直接质疑双耳音乐源分离评测指标的可信度——这是"榜单数字是否可信"的关键一手质疑。推荐度 ★★★★★（评测方法论必读）[72]。
- **音乐分离辅助歌词转写** [53]：用 MSS 前端抑制伴奏以提升 Whisper 的自动歌词转写（ALT）表现，说明 ALT 的核心瓶颈仍是伴奏高能量干扰 [53]。

### 1.4 生成与可控性

- **零大规模外部预训练的乐器化文本到音乐 + 辅助条件分支** [3]：刻意剥离大规模数据与外部预训练，试图**归因到底是哪一项设计起作用**。推荐度 ★★★★☆（归因型研究，稀缺）[3]。
- **ICME 2026 学术文本到音乐 Grand Challenge（UT-AISTimprt）** [4]：研究低数据、小模型设定下的批采样策略。推荐度 ★★★☆☆（赛道基线价值）[4]。
- **Story2MIDI** [2]：文本 → 情感对齐音乐的 seq2seq Transformer，并合并文本情感与音乐情感数据集构建配对数据。推荐度 ★★★☆☆ [2]。
- **结构化状态空间模型（SSM）扩散符号音乐生成** [5]：针对 Transformer 自注意力二次复杂度制约长序列的问题，改用 SSM [5]。
- **钢琴音乐 Transformer 的系统对比** [8]：系统比较不同数据集、架构、指标对生成质量的影响，属于"设计选择归因"类工作 [8]。
- **SegTune** [22]：面向歌曲生成的结构化、细粒度控制 [22]。

### 1.5 MIR 侧的前沿与"反榜单"研究

- **GlobalMood** [25]：跨文化音乐情绪识别基准，指出既有数据集以西方歌曲与英语词表为主，泛化受限 [25]。推荐度 ★★★★☆（数据偏差问题的一手基准）[25]。
- **The SMC Blind Spot** [43]：对最先进 beat tracking 做失败模式分析——在主流打击乐数据集近乎完美，但在 SMC 数据集上存在结构性失败 [43]。**这是"榜单 SOTA ≠ 真实场景可用"的强证据。**
- **ISMIR 作者群计量分析（前 25 年）** [31]：量化 MIR 社区的"西方中心"程度。热度 citations=5 [31]；权威 TISMIR（DOI，同行评审期刊，A 级）[31]；关注度 中（citations=5）[31]；推荐度 ★★★★☆（社区自省的一手数据）[31]。
- **统一跨模态翻译（乐谱图像 / 符号音乐 / 演奏音频）** [14]：把三类表示之间的翻译统一到一个框架 [14]。

## 参考来源

[1] Music Transformer — http://arxiv.org/abs/1809.04281v3
[2] Story2MIDI: Emotionally Aligned Music Generation from Text — http://arxiv.org/abs/2512.02192v1
[3] Instrumental Text-to-Music Generation with Auxiliary Conditioning Branches — http://arxiv.org/abs/2605.21433v1
[4] UT-AISTimprt submission for ICME 2026 Grand Challenge on Academic Text-to-Music Generation — http://arxiv.org/abs/2607.01669v1
[5] Diffusion-based Symbolic Music Generation with Structured State Space Models — http://arxiv.org/abs/2507.20128v2
[6] Music SketchNet: Controllable Music Generation via Factorized Representations of Pitch and Rhythm — http://arxiv.org/abs/2008.01291v1
[7] Text-to-image Diffusion Models in Generative AI: A Survey — http://arxiv.org/abs/2303.07909v3
[8] Generating Piano Music with Transformers: A Comparative Study of Scale, Data, and Metrics — http://arxiv.org/abs/2511.07268v2
[9] Joint Music and Language Attention Models for Zero-shot Music Tagging — http://arxiv.org/abs/2310.10159v1
[10] NGHIÊN CỨU CÁC MÔ HÌNH CHUYỂN ĐỔI HÌNH ẢNH THÀNH VIDEO: MỘT ĐÁNH GIÁ TOÀN DIỆN — https://doi.org/10.34238/tnu-jst.13790
[11] From Alignment to Advancement: Bootstrapping Audio-Language Alignment with Synthetic Data — http://arxiv.org/abs/2505.20166v3
[12] DeSTA2.5-Audio: Toward General-Purpose Large Audio Language Model with Self-Generated Cross-Modal Alignment — http://arxiv.org/abs/2507.02768v2
[13] MusCaps: Generating Captions for Music Audio — http://arxiv.org/abs/2104.11984v1
[14] Unified Cross-modal Translation of Score Images, Symbolic Music, and Performance Audio — http://arxiv.org/abs/2505.12863v1
[15] Acoustic Prompt Tuning: Empowering Large Language Models with Audition Capabilities — http://arxiv.org/abs/2312.00249v2
[16] Generation of lyrics lines conditioned on music audio clips — http://arxiv.org/abs/2009.14375v1
[17] Nested Music Transformer: Sequentially Decoding Compound Tokens in Symbolic Music and Audio Generation — http://arxiv.org/abs/2408.01180v2
[18] ConSinger: Efficient High-Fidelity Singing Voice Generation with Minimal Steps — http://arxiv.org/abs/2410.15342v3
[19] Modelling Emotion Dynamics in Song Lyrics with State Space Models — http://arxiv.org/abs/2210.09434v1
[20] SongBsAb: A Dual Prevention Approach against Singing Voice Conversion based Illegal Song Covers — http://arxiv.org/abs/2401.17133v2
[21] Towards an LLM-based method for quantifying the sexual content in song lyrics — http://arxiv.org/abs/2608.08885v1
[22] SegTune: Structured and Fine-Grained Control for Song Generation — http://arxiv.org/abs/2606.02638v1
[23] Singing voice synthesis based on convolutional neural networks — http://arxiv.org/abs/1904.06868v2
[24] SongMASS: Automatic Song Writing with Pre-training and Alignment Constraint — http://arxiv.org/abs/2012.05168v1
[25] GlobalMood: A cross-cultural benchmark for music emotion recognition — http://arxiv.org/abs/2505.09539v2
[26] Symbolic Music Representations for Classification Tasks: A Systematic Evaluation — http://arxiv.org/abs/2309.02567v2
[27] Barwise Music Structure Analysis with the Correlation Block-Matching Segmentation Algorithm — http://arxiv.org/abs/2311.18604v1
[28] MIRFLEX: Music Information Retrieval Feature Library for Extraction — http://arxiv.org/abs/2411.00469v1
[29] Towards Multimodal MIR: Predicting individual differences from music-induced movement — http://arxiv.org/abs/2007.10695v1
[30] A Functional Taxonomy of Music Generation Systems — http://arxiv.org/abs/1812.04186v1
[31] Beyond a Western Center of Music Information Retrieval: A Bibliometric Analysis of the First 25 Years of ISMIR Authorship — https://doi.org/10.5334/tismir.265
[32] Learning to Traverse Latent Spaces for Musical Score Inpainting — http://arxiv.org/abs/1907.01164v1
[33] Proceedings of the 26th International Society for Music Information Retrieval Conference, ISMIR 2025, Daejeon, South Korea, September 21-25, 2025 — https://www.semanticscholar.org/paper/1fbd102a725a70ea20eb27ef42573d742c1455b4
[34] Proceedings of the 25th International Society for Music Information Retrieval Conference, ISMIR 2024, San Francisco, California, USA and Online, November 10-14, 2024 — https://www.semanticscholar.org/paper/61f878040ff416d27b3c25384fbe97229a764367
[35] Chord Label Personalization through Deep Learning of Integrated Harmonic Interval-based Representations — http://arxiv.org/abs/1706.09552v1
[36] A Survey of Large Language Model Empowered Agents for Recommendation and Search: Towards Next-Generation Information Retrieval — https://arxiv.org/abs/2503.05659
[37] The Modern Mathematics of Deep Learning — http://arxiv.org/abs/2105.04026v2
[38] Report on the 23rd International Society for Music Information Retrieval Conference (ISMIR 2022) — https://doi.org/10.1145/3636341.3636350
[39] Learn to Accumulate Evidence from All Training Samples: Theory and Practice — http://arxiv.org/abs/2306.11113v2
[40] Natural Language Processing Methods for Symbolic Music Generation and Information Retrieval: A Survey — https://arxiv.org/abs/2402.17467
[41] Deep Learning in Palmprint Recognition-A Comprehensive Survey — http://arxiv.org/abs/2501.01166v2
[42] Proceedings of the 2nd Workshop on Human-Centric Music Information Retrieval 2023 co-located with the 24th International Society for Music Information Retrieval Conference (ISMIR 2023), Milan, Italy, November 10, 2023 — https://www.semanticscholar.org/paper/d521ffbbf5fb058b6332067ee423123aba01fc1a
[43] The SMC Blind Spot: A Failure Mode Analysis of State-of-the-Art Beat Tracking — http://arxiv.org/abs/2605.12287v1
[44] Proceedings of the 24th International Society for Music Information Retrieval Conference, ISMIR 2023, Milan, Italy, November 5-9, 2023 — https://www.semanticscholar.org/paper/fdcd30be63867dff918996d11fab5fed4a5b824f
[45] Deep Learning and Computational Physics (Lecture Notes) — http://arxiv.org/abs/2301.00942v1
[46] Monodense Deep Neural Model for Determining Item Price Elasticity — http://arxiv.org/abs/2603.29261v1
[47] A multitask deep learning model for real-time deployment in embedded systems — http://arxiv.org/abs/1711.00146v1
[48] The Whole Is Greater than the Sum of Its Parts: Improving Music Source Separation by Bridging Network — http://arxiv.org/abs/2305.07855v2
[49] Opening Musical Creativity? Embedded Ideologies in Generative-AI Music Systems — http://arxiv.org/abs/2508.08805v1
[50] End-to-end music source separation: is it possible in the waveform domain? — http://arxiv.org/abs/1810.12187v2
[51] Improving Choral Music Separation through Expressive Synthesized Data from Sampled Instruments — http://arxiv.org/abs/2209.02871v1
[52] Multi-Stage Music Source Restoration with BandSplit-RoFormer Separation and HiFi++ GAN — http://arxiv.org/abs/2603.04032v1
[53] Exploiting Music Source Separation for Automatic Lyrics Transcription with Whisper — http://arxiv.org/abs/2506.15514v1
[54] Music Source Separation with Band-Split RoPE Transformer — http://arxiv.org/abs/2309.02612v2
[55] Vision-to-Music Generation: A Survey — http://arxiv.org/abs/2503.21254v1
[56] LabelBuddy: An Open Source Music and Audio Language Annotation Tagging Tool Using AI Assistance — http://arxiv.org/abs/2603.04293v1
[57] Baseline Systems For The 2025 Low-Resource Audio Codec Challenge — http://arxiv.org/abs/2510.00264v3
[58] Digital Audio Processing Tools for Music Corpus Studies — http://arxiv.org/abs/2111.03895v2
[59] Open-Set Source Tracing of Audio Deepfake Systems — http://arxiv.org/abs/2507.06470v1
[60] Who Gets Heard? Rethinking Fairness in AI for Music Systems — http://arxiv.org/abs/2511.05953v1
[61] Ethics Statements in AI Music Papers: The Effective and the Ineffective — http://arxiv.org/abs/2509.25496v1
[62] The Shape of Surprise: Structured Uncertainty and Co-Creativity in AI Music Tools — http://arxiv.org/abs/2509.25028v1
[63] M2D-CLAP: Exploring General-purpose Audio-Language Representations Beyond CLAP — http://arxiv.org/abs/2503.22104v2
[64] "Melatonin": A Case Study on AI-induced Musical Style — http://arxiv.org/abs/2208.08968v1
[65] No Encore: Unlearning as Opt-Out in Music Generation — http://arxiv.org/abs/2509.06277v2
[66] Advancing Multi-Instrument Music Transcription: Results from the 2025 AMT Challenge — http://arxiv.org/abs/2603.27528v1
[67] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1
[68] NTIRE 2025 Challenge on Image Super-Resolution (x4): Methods and Results — http://arxiv.org/abs/2504.14582v3
[69] Event-Enriched Image Analysis Grand Challenge at ACM Multimedia 2025 — http://arxiv.org/abs/2508.18904v1
[70] ICME 2025 Generalizable HDR and SDR Video Quality Measurement Grand Challenge — http://arxiv.org/abs/2506.22790v2
[71] Audio query-based music source separation — http://arxiv.org/abs/1908.06593v1
[72] Spacing Out: On the Reliability of Binaural Music Source Separation Metrics — http://arxiv.org/abs/2607.25919v1
[73] Transfer Learning from Visual Speech Recognition to Mouthing Recognition in German Sign Language — http://arxiv.org/abs/2505.13784v2
[74] The Multimodal Information Based Speech Processing (MISP) 2025 Challenge: Audio-Visual Diarization and Recognition — http://arxiv.org/abs/2505.13971v2
[75] Human in the Loop: Interactive Passive Automata Learning via Evidence-Driven State-Merging Algorithms — http://arxiv.org/abs/1707.09430v1
[76] AlphaChimp: Tracking and Behavior Recognition of Chimpanzees — http://arxiv.org/abs/2410.17136v2
[77] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1
[78] VLSP 2025 MLQA-TSR Challenge: Vietnamese Multimodal Legal Question Answering on Traffic Sign Regulation — http://arxiv.org/abs/2510.20381v1
[79] The AudioMOS Challenge 2025 — http://arxiv.org/abs/2509.01336v1
[80] TDCOSMO 2025: Cosmological constraints from strong lensing time delays — http://arxiv.org/abs/2506.03023v4
[81] TRUST 2025: SCRITA and RTSS @ RO-MAN 2025 — http://arxiv.org/abs/2509.11402v1
[82] SVC 2025: the First Multimodal Deception Detection Challenge — http://arxiv.org/abs/2508.04129v1
[83] HQ-SVC: Towards High-Quality Zero-Shot Singing Voice Conversion in Low-Resource Scenarios — http://arxiv.org/abs/2511.08496v3
[84] YingMusic-SVC: Real-World Robust Zero-Shot Singing Voice Conversion with Flow-GRPO and Singing-Specific Inductive Biases — http://arxiv.org/abs/2512.04793v1
[85] kNN-SVC: Robust Zero-Shot Singing Voice Conversion with Additive Synthesis and Concatenation Smoothness Optimization — http://arxiv.org/abs/2504.05686v1
[86] SPA-SVC: Self-supervised Pitch Augmentation for Singing Voice Conversion — http://arxiv.org/abs/2406.05692v1
[87] Poly-SVC: Polyphony-Aware Singing Voice Conversion with Harmonic Modeling — http://arxiv.org/abs/2605.12310v1
[88] Fast and High-Quality Singing Voice Synthesis System based on Convolutional Neural Networks — http://arxiv.org/abs/1910.11690v2
[89] Latent linguistic embedding for cross-lingual text-to-speech and voice conversion — http://arxiv.org/abs/2010.03717v1
[90] An Extensive Analysis of the Singing Voice Conversion Challenge 2025 Evaluation Results — http://arxiv.org/abs/2509.15629v2
[91] Voice Conversion Challenge 2020: Intra-lingual semi-parallel and cross-lingual voice conversion — http://arxiv.org/abs/2008.12527v1
[92] The NeteaseGames System for Voice Conversion Challenge 2020 with Vector-quantization Variational Autoencoder and WaveNet — http://arxiv.org/abs/2010.07630v1
[93] The NU Voice Conversion System for the Voice Conversion Challenge 2020: On the Effectiveness of Sequence-to-sequence Models and Autoregressive Neural Vocoders — http://arxiv.org/abs/2010.04446v1
[94] DAFMSVC: One-Shot Singing Voice Conversion with Dual Attention Mechanism and Flow Matching — https://arxiv.org/abs/2508.05978
[95] An Extensive Analysis of the Singing Voice Conversion Challenge 2025 Evaluation Results — https://arxiv.org/abs/2509.15629
[96] MPFM-VC: A Voice Conversion Algorithm Based on Multi-Dimensional Perception Flow Matching — https://doi.org/10.3390/app15105503
[97] Learning a Representation for Cover Song Identification Using Convolutional Neural Network — http://arxiv.org/abs/1911.00334v1
[98] Enhancing Emotional Expressiveness in Voice Conversion Using Seq2Seq and CycleGAN — https://doi.org/10.71426/jcdt.v1.i2.pp98-103
[99] Large-Scale Cover Song Detection in Digital Music Libraries Using Metadata, Lyrics and Audio Features — http://arxiv.org/abs/1808.10351v1
[100] Artificial Intelligence Meets Your Voice: Transforming Turkish Text into Personalized Speech — https://doi.org/10.5152/electrica.2025.25034
[101] SenseFi: A Library and Benchmark on Deep-Learning-Empowered WiFi Human Sensing — http://arxiv.org/abs/2207.07859v3
[102] A Comparative Study of Voice Conversion Models With Large-Scale Speech and Singing Data: The T13 Systems for the Singing Voice Conversion Challenge 2023 — https://arxiv.org/abs/2310.05203
[103] CultureMERT: Continual Pre-Training for Cross-Cultural Music Representation Learning — http://arxiv.org/abs/2506.17818v1
[104] Learning Speech Representations from Raw Audio by Joint Audiovisual Self-Supervision — http://arxiv.org/abs/2007.04134v1
[105] DeLoRes: Decorrelating Latent Spaces for Low-Resource Audio Representation Learning — http://arxiv.org/abs/2203.13628v3
[106] Learning General Audio Representations with Large-Scale Training of Patchout Audio Transformers — http://arxiv.org/abs/2211.13956v2
[107] MATPAC++: Enhanced Masked Latent Prediction for Self-Supervised Audio Representation Learning — https://arxiv.org/abs/2508.12709
[108] One Deep Music Representation to Rule Them All? : A comparative analysis of different representation learning strategies — http://arxiv.org/abs/1802.04051v4
[109] Audio-JEPA: Joint-Embedding Predictive Architecture for Audio Representation Learning — https://arxiv.org/abs/2507.02915
[110] Balancing Information Preservation and Disentanglement in Self-Supervised Music Representation Learning — https://arxiv.org/abs/2507.22995
[111] Scaling Self-Supervised Representation Learning for Symbolic Piano Performance — https://arxiv.org/abs/2506.23869
[112] MIDI-Zero: A MIDI-driven Self-Supervised Learning Approach for Music Retrieval — https://doi.org/10.1145/3726302.3730034
[113] A Closer Look at Neural Codec Resynthesis: Bridging the Gap between Codec and Waveform Generation — http://arxiv.org/abs/2410.22448v1
[114] Singing Voice Conversion with Accompaniment Using Self-Supervised Representation-Based Melody Features — https://arxiv.org/abs/2502.04722
[115] Generating Sample-Based Musical Instruments Using Neural Audio Codec Language Models — http://arxiv.org/abs/2407.15641v1
[116] Evaluating Contrastive Methodologies for Music Representation Learning Using Playlist Data — https://doi.org/10.1109/ICASSP49660.2025.10888157
[117] HiFi-Codec: Group-residual Vector quantization for High Fidelity Audio Codec — http://arxiv.org/abs/2305.02765v2
[118] USAD: Universal Speech and Audio Representation via Distillation — https://arxiv.org/abs/2506.18843
[119] Bringing Interpretability to Neural Audio Codecs — http://arxiv.org/abs/2506.04492v1


---

*Generated by research-bot · topic=`music-audio` · depth=`standard` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading · model=`deepseek-v4-flash` · sources=119 · duration=318s · 2026-10-02T23:14:03+00:00*
