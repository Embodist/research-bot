# 音乐与音频算法调研报告：MIR、音乐生成、理解与源分离

> **日期（UTC）**：2026-10-06
> **领域**：Music & Audio —— Music Information Retrieval (MIR) / 音乐生成（Text-to-Music、符号音乐）/ 音乐理解与自监督音频表征 / 歌声合成与转换（SVS/SVC）/ 翻唱识别（CSI）/ 音源分离（MSS）/ 神经音频编解码
> **引用池**：本报告所有引用编号取自本次检索的候选证据池 [1]–[164]，共 164 条条目；正文实际引用约 90 条，编号与来源列表一一对应，未引用任何池外编号或自造 URL
> **证据与数据纪律**：候选证据块**未附带** citations、GitHub star、下载量、榜单排名等热度字段，因此凡涉量化热度一律写 `> 待核实`，报告不做任何数字估算、不补造 URL
> **检索噪声警告（重要）**：候选池存在两组严重术语撞车，已在下文明确区分：(a) [35][39] 的 "SVC" 指 **Subtle Visual Cues（多模态欺骗检测）**，与 **Singing Voice Conversion** 无关；(b) [80][83] 的 "SDR" 分别指 **Standard Dynamic Range** 视频质量与 **Software Defined Radio**，与分离任务的 **Signal-to-Distortion Ratio** 无关。另有 [16][54][55][56][126][128][145][160] 等非音乐条目，属检索噪声，本报告不作为音乐领域证据使用

## 摘要（Executive Summary）

1. **生成侧的主线是「可控 + 全曲 + 长格式 + 偏好对齐」而非单纯音质提升**：开放基础模型（ACE-Step [123]、YuE [124]、Stable Audio Open [119]）与编辑/控制类工作（Instruct-MusicGen [118]、Audio Prompt Adapter [120]）并行推进，人类偏好奖励被直接用于 T2M 优化 [159]，学术赛道则出现低数据/小模型设定下的新竞赛 [112][113]。
2. **音乐表征从「通用 CLAP」走向「多域/多文化适配」**：M2D-CLAP 尝试超越 CLAP 的通用音频-语言表征 [49]，CultureMERT-95M 用持续预训练补足非西方音乐传统 [92]。这直接指向 MIR 领域的文化偏置问题。
3. **声音分离的架构收敛在 Band-Split / RoFormer 系**：[72][74] 为代表，[78] 用 bridging network 做集成式改进，[79] 把「四轨固定输出」推向 stem-agnostic 单解码器；任务定义本身也在扩展——从「分离」到「复原（Music Source Restoration）」[73]，以及训练数据含错条件下的 robust MSS 形式化 [147]。
4. **神经音频编解码的竞争焦点从纯比特率转向工程可用性**：低资源/鲁棒部署 [91][84]、流式实时通信 [138]、多尺度码本 [140]、量化结构改进 [137]、可解释性 [89]，以及**解码端能耗-比特率-质量**的实测 [139]；Codec-SUPERB 提供了跨任务码本评测 [135]。
5. **MIR 经典任务在「主流数据集」上接近饱和，但失败模式转移**：DNN 节拍跟踪在主流打击乐数据集近乎完美，却在 SMC 数据集系统性失败 [14]；2025 AMT 挑战 8 支有效提交中仅 2 支超过 MT3 基线 [95]。
6. **评测与治理是本领域最活跃的「元议题」**：评测分数被论证为有保质期的知识主张、多信号平均聚合会引发「信任膨胀」[47]；榜单运维本身被作为研究对象 [82]；音乐 AI 的争议从版权/深伪扩展到文化与流派偏见 [62]、产业「民主化」话语批判 [63]、以及机器遗忘作为 opt-out 机制 [64][67]。
7. **证据缺口需显式声明**：本报告在候选池内**找不到**任何直接讨论 SVC 滥用或 deepfake 检测的数据集/基准/指标来源，该分支只能标 `> 待核实`；CLAP、MERT 的**原始**论文亦不在本池内，相关论述经由 [49][92] 转述。

---

## 一、关键前沿进展（近 1–2 年）

### 1.1 文本到音乐与全曲生成

- **ACE-Step**（音乐生成基础模型方向）[123]、**YuE**（明确以「长格式音乐生成」为 scaling 目标的开源基础模型）[124]、**Stable Audio Open**（开放权重的文本到音频生成）[119] 构成 2024–2025 开放模型三条主线。
  **【热度】** `> 待核实`（候选块无 citations/star 快照）｜**【权威】** arXiv 预印本（cs.SD / eess.AS），未见同行评审记录｜**【关注度】** 中：开放音乐生成基础模型是社区持续热点，但本池无可量化信号｜**【推荐度】** ★★★★☆：理解开放 T2M 前沿的必读入口。
- **可控与编辑**：Instruct-MusicGen 通过指令微调解锁文本到音乐编辑 [118]；Audio Prompt Adapter 以轻量微调赋予 T2M 模型音乐编辑能力 [120]；[122] 提供同时探索文本 prompt 与音频先验的交互界面。
- **对齐与偏好**：[159] 将人类偏好奖励用于改进文本到音乐生成，是「从客观指标转向偏好优化」的代表。
  **【权威】** arXiv 预印本｜**【热度】** `> 待核实`｜**【关注度】** 中：偏好对齐是 2025–2026 生成模型的通用趋势｜**【推荐度】** ★★★★☆。
- **学术赛道与低资源设定**：ICME 2026 学术文本到音乐生成 Grand Challenge 的参赛工作研究低数据、小模型下的训练批采样策略 [112]；[113] 用辅助条件分支做器乐 T2M，并强调「难以归因」的问题（大模型依赖大规模数据与外部预训练）。
  **【权威】** Grand Challenge 技术报告 / arXiv 预印本（cs.SD）｜**【热度】** `> 待核实`｜**【关注度】** 低–中：竞赛类工作社区扩散有限｜**【推荐度】** ★★★☆☆：适合关注「可归因性」与低资源复现者。
- **质量评价侧的新基准**：AudioMOS Challenge 2025 是**首个**面向合成音频自动主观质量预测的挑战，其中一轨专门评 T2M 的整体质量与文本对齐 [114]；SongEval 提供歌曲美学评测基准 [161]。
- **情感对齐生成**：Story2MIDI 以 seq2seq Transformer 从文本生成情感对齐音乐，并合并情感分析与情绪分类数据集构建 Story2MIDI 数据集 [115]。

### 1.2 表征与理解基础模型

- CultureMERT-95M：面向跨文化音乐表征的持续预训练（continual pre-training）模型 [92]。
- M2D-CLAP：探索超越 CLAP 的通用音频-语言表征 [49]。
- 音乐域自监督：wav2vec 2.0 在音乐表征上的迁移 [131]、大规模 Patchout Audio Transformer 的通用音频表征 [130]、COALA 的共对齐自编码器 [132]。
  **【权威】** 均为 arXiv 预印本（cs.SD / eess.AS / cs.CL）｜**【热度】** `> 待核实`｜**【关注度】** 中高：音乐基础模型是 2024–2026 MIR 的主战场（依据：本子问题检索命中集中于此方向）｜**【推荐度】** ★★★★★（[92][49]）／★★★★☆（[130][131][132]）。

### 1.3 分离与编解码

- 分离架构：[72]（Mel-Band RoFormer）、[74]（Band-Split RoPE Transformer）、[78]（bridging network 集成）、[79]（stem-agnostic 单解码器，突破四轨假设）。
- 任务扩展：CP-JKU 团队的 MSR（Music Source Restoration）系统，用 BandSplit-RoFormer + HiFi++ GAN 从「已混音母带」中恢复未处理音轨，明确指出现有线性混合假设被制作效果破坏 [73]；SDX'23 正式提出 robust MSS（训练数据含错）形式化 [147]。
- 编解码：LRAC 2025 挑战描述与基线 [91][84]、SNAC 多尺度码本 [140]、WavTokenizer [86]、ERVQ 码本内/间优化 [137]、流式 RSVQ 实时通信编解码 [138]、编解码重合成差距分析 [90]、DAC 的 JAX 实现 [141]、可解释性 [89]、解码端能耗实测 [139]、Codec-SUPERB 跨任务评测 [135]。
  **【权威】** arXiv 预印本（eess.AS / cs.SD）｜**【热度】** `> 待核实`｜**【关注度】** 高（工程侧）：低资源部署与能耗是 2025–2026 新增焦点（依据：[91][139] 的选题本身即针对部署约束）｜**【推荐度】** ★★★★☆。

### 1.4 评测与治理（元议题）

- [47] 论证评测分数需具备 formality / scope / validity windows 三属性，并警示多信号平均聚合导致「信任膨胀」。
- [82] 把基础模型榜单的运维（Leaderboard Operations）本身作为实证研究对象，指出运维层面的「坏味道」。
- 音乐 AI 治理：公平性与文化偏见 [62]、生成式音乐系统的内嵌意识形态 [63]、AI 音乐论文伦理声明的有效性 [66]、AI 音乐工具中的结构化不确定性与共创 [68]、机器遗忘作为版权 opt-out [64]、生成式 AI 隐私与版权的生命周期视角 [67]。
  **【权威】** [47] 为 cs.AI position paper（未见同行评审）；[62] 摘要标注 Accepted at NeurIPS'2…（**具体年份/会议名被截断，`> 待核实`**）｜**【热度】** `> 待核实`｜**【关注度】** 中：评测失效与音乐 AI 伦理是当前高频社区议题（依据：本池在同一子问题下聚集多条此类来源）｜**【推荐度】** ★★★★☆（[47][62]）／★★★☆☆（[63][64]，内容为摘要片段，证据强度低）。

---

## 二、音乐信息检索（MIR / 翻唱识别 CSI / 节拍与和声）

**节拍跟踪（Beat Tracking）**
- 关键失败模式证据：DNN 节拍跟踪在主流打击乐数据集近乎完美，但在 SMC 数据集上系统性失败；论文将此定义为「SMC 盲点」并做失败模式分析 [14]。
  **【权威】** arXiv 预印本（eess.AS）｜**【热度】** `> 待核实`｜**【关注度】** 中：以「复现失败/分布外泛化」切入，契合评测争议趋势｜**【推荐度】** ★★★★☆：MIR 领域少见的负结果导向研究，与第七章评测争议强相关。

**和弦识别（Chord Recognition）**
- [17] 用 LLM 的 Chain-of-Thought 推理增强自动和弦识别；[9] 以和声区间（harmonic interval）表示做和弦标签个性化；[23] 基于调式和声的概率建模。
  **【权威】** [17] arXiv 预印本；[9][23] Semantic Scholar 收录条目｜**【热度】** `> 待核实`｜**【关注度】** 中｜**【推荐度】** ★★★☆☆–★★★★☆（[17] 因 LLM 融合方向相关性强）。

**自动音乐转录（AMT）**
- Omnizart 提供通用 AMT 工具箱 [18]；多音高 F0 的深度显著性表示 [21]；2025 AMT 挑战赛总结显示 8 支有效提交中 2 支超过 MT3 基线 [95]。
- 跨模态统一：将乐谱图像、符号乐谱、MIDI 与演奏音频的互译统一到一个框架 [142]，把 AMT 与 OMR 视为同一翻译问题的不同方向。
  **【权威】** [18][21] 为工具/经典方法类论文，[95][142] 为 arXiv 预印本（cs.SD）｜**【热度】** `> 待核实`｜**【关注度】** 中（[95][142]）｜**【推荐度】** ★★★★☆：转录任务的「统一视角」值得关注。

**音乐结构分析（MSA）**
- Barwise 音乐结构分析：扩展 Correlation Block-Matching 分割算法，按小节（barwise）粒度做结构分割 [3]。

**音乐情感 / 情绪**
- GlobalMood：跨文化音乐情绪识别基准，明确指出既有数据集以西方歌曲与英语术语为主，泛化性受限 [4]。
- 歌词情绪动态：用状态空间模型对歌词情绪动态建模 [46]。

**检索与文本-音乐问答**
- MUST-RAG：面向音乐文本问答的检索增强生成，指出 LLM 在音乐领域因音乐语料占比低而效果受限 [106]。
- 文本到音频检索中的**时间理解**被单独剖析 [111]。
- 多域音频问答基准（DCASE 2025 Task 5，含 Complex QA 等三个子集）[105]。

**工具与特征库**
- MIRFLEX [5]、librosa（种子资源）、musif 符号音乐特征提取 [162]、Digital Audio Processing Tools for Music Corpus Studies [143] 构成 MIR 特征工程栈。
- 大规模中文音乐 MIR 数据库 CCMusic [7]。

**翻唱识别（CSI）**
- CNN 表征学习用于翻唱识别 [41]；大规模数字音乐库中结合元数据、歌词与音频特征的翻唱检测 [42]。
  **【权威】** [41][42] 为较早的 arXiv 预印本（2018/2019），非 2024–2026 最新工作｜**【热度】** `> 待核实`｜**【关注度】** 低：本池中 CSI 近两年条目缺失，属检索缺口｜**【推荐度】** ★★★☆☆：可作 CSI 起点，但**已不足以代表 2024–2026 现状** `> 待核实`。

**多模态 MIR**
- 从音乐引发的身体运动预测个体差异 [6]，代表音乐-运动多模态 MIR 方向。

---

## 三、音乐生成（文本 / 符号 / 音频）

**（a）文本到音乐（音频域）**
- 奠基与开放模型：MusicLM（Google Research, 2023）https://arxiv.org/abs/2301.11325 ；MusicGen（Meta, NeurIPS 2023）https://arxiv.org/abs/2306.05284 ；后续开放模型 ACE-Step [123]、YuE [124]、Stable Audio Open [119]。
- 控制/编辑：Instruct-MusicGen [118]、Audio Prompt Adapter [120]、IteraTTA（文本 prompt 与音频先验交互）[122]。
- 偏好优化：[159]。
- 竞赛与低资源：[112][113]。

**（b）符号音乐生成**
- Music SketchNet：通过音高与节奏的因子化表示实现可控生成 [51]。
- 潜空间遍历用于乐谱补全（inpainting）[50]。
- 钢琴 Transformer 的系统性比较研究：跨数据集、架构、模型规模与训练策略做消融，并**显式检验量化指标与人类听测的相关性**；最佳配置为 950M 参数 Transformer、80K 多风格 MIDI 训练，输出在图灵式测试中常被判为人作 [53]。
  **【权威】** arXiv 预印本（cs.SD），v2 2026-01-04 修订，未见同行评审｜**【热度】** `> 待核实`｜**【关注度】** 中：直接回应「生成音乐指标是否可靠」争议｜**【推荐度】** ★★★★☆：本池内唯一给出「指标 vs 听感」实证对照的符号生成工作。
- 歌词到旋律：CSL-L2M 基于条件 Transformer 做歌曲级、细粒度歌词与音乐控制 [127]；曲式感知的全曲歌词生成与多级音节数控制 [125]。

**（c）跨模态生成**
- Vision-to-Music 生成综述 [52]，以及配套的 Awesome-Vision-to-Music-Generation 资源库 [164]（见第八章与开源项目表）。
- 采样乐器音色的神经编解码语言模型生成 [136]，把 codec LM 用于乐器采样生成。

**（d）综述与分类骨架**
- 功能分类学（A Functional Taxonomy of Music Generation Systems）[1] 提供任务级分类骨架；Deep Learning Techniques for Music Generation — A Survey [12] 与 Music Generation by Deep Learning — Challenges and Directions [10] 提供早期方法脉络。
  **【权威】** [1][10][12] 为综述/立场类，年份较早（2017–2018）｜**【热度】** `> 待核实`｜**【关注度】** 中（作为骨架被持续引用）｜**【推荐度】** ★★★★☆：分类骨架仍有效，但**不覆盖基础模型时代**，需与 [123][124] 等结合阅读。

---

## 四、音乐理解与自监督表征

**自监督源头方法（经典）**
- wav2vec 2.0：语音自监督表征框架，定义掩码潜变量 + 对比学习范式 [134]。
- HuBERT：通过掩码预测隐藏单元做自监督语音表征 [24]。
- 迁移到音乐域：Learning Music Representations with wav2vec 2.0 [131]；COALA 共对齐自编码器学习语义增强音频表征 [132]；大规模 Patchout Audio Transformer 训练通用音频表征 [130]。
- 语音侧应用佐证泛化性：wav2vec 2.0 用于说话人验证与语种识别 [20]；微调 wav2vec2/HuBERT 在情感识别、说话人验证、口语理解上的基准 [133]；知识蒸馏多任务语音表征 [22]。

**基础模型层（2024–2026）**
- M2D-CLAP：超越 CLAP 的通用音频-语言表征 [49]。
- CultureMERT-95M：跨文化持续预训练的音乐基础模型 [92]。
  **说明**：CLAP 与 MERT 的**原始论文不在本次可引用池内**，相关论述经由 [49][92] 转述；其原始引用信息 `> 待核实`。
  **【权威】** [134][24] 为奠基性预印本（后成为该领域标准引用）；[49][92] 为 2025 年预印本｜**【热度】** `> 待核实`｜**【关注度】** 高（[134][24]：已成为语音/音频自监督的标准基线；[92][49]：本子问题检索命中集中于此）｜**【推荐度】** ★★★★★（[134][24][92][49]）。

**音乐标注、描述与问答**
- 零样本音乐标注的联合音乐-语言注意力模型 [94]。
- MusCaps 音乐描述生成 [93]；MusiLingo 用预训练语言模型桥接音乐与文本 [108]；扩散模型用于多样化音频描述 [107]；EnCLAP + 辅助检索模型的自动音频描述 [110]；细粒度音频特征与 LLM mix-up 增强的描述改进 [109]。
- 音乐文本问答：MUST-RAG [106]；多域音频问答基准 [105]。
- 歌词与语言侧：歌词情绪动态建模 [46]；歌词性内容量化方法 [129]；歌词性内容与 LLM 结合的分级方法 `> 待核实`（[129] 为 2026 预印本）。

**MIR 通用工具链**
- MIRFLEX 特征库 [5]、musif [162]、CCMusic 中文音乐数据库 [7]、GlobalMood 情绪基准 [4]。

---

## 五、歌声转换（SVC）与音源分离

### 5.1 歌声合成与转换（SVS / SVC）

- **早期与经典**：基于 CNN 的歌声合成 [26]、快速高质量 CNN 歌声合成系统 [27]、Conditional DSVAE 改进零样本语音转换 [32]。
- **扩散/流匹配路线**：NaturalSpeech 2 用潜扩散实现零样本语音与歌声合成 [28]；LDM-SVC 用潜扩散做零样本 any-to-any 歌声转换并引入 singer guidance [33]；ConSinger 以极少步数实现高效高保真歌声生成 [25]；FlashSpeech 高效零样本语音合成 [34]。
- **零样本/少样本 SVC 的近期进展**：基于聚类音素表示的零样本歌声转换 [30]；Everyone-Can-Sing 用语音参考做零样本 SVS 与转换 [31]；TCSinger 2 支持可定制多语言零样本歌声合成，明确指出既有模型过度依赖音素与音符边界标注、零样本鲁棒性差 [29]；YingMusic-SVC 针对真实歌曲中的和声干扰、F0 误差与缺乏歌唱归纳偏置问题，结合 Flow-GRPO 与歌唱特定归纳偏置 [36]。
  **【权威】** 均为 arXiv 预印本（eess.AS / cs.SD），未见同行评审记录｜**【热度】** `> 待核实`｜**【关注度】** 中高：零样本 SVC/SVS 是 2024–2026 音频生成热点之一（依据：本子问题检索命中 8+ 条同方向工作）｜**【推荐度】** ★★★★☆（[29][36]）／★★★☆☆（[25][33][34]）。

- **⚠️ 术语撞车澄清（必读）**：候选池中的 [35]（SVC 2025: the First Multimodal Deception Detection Challenge）与 [39]（SVC 2026: the Second Multimodal Deception Detection Challenge…）中的 "SVC" 指 **Subtle Visual Cues**，属于多模态欺骗检测/远程生理测量挑战，**与 Singing Voice Conversion 无关**，本报告不将其作为 SVC 证据。
- **SVC 滥用与检测**：在给定候选证据池中，**不存在**任何直接讨论歌声转换滥用或 deepfake 检测的数据集、基准或论文。该分支在当前证据下无法评估，`> 待核实`（需补充检索）。

### 5.2 音源分离（MSS）

- **波形域端到端可行性的早期论证**：[75]（End-to-end music source separation: is it possible in the waveform domain?）；Demucs（Meta, 2019）https://arxiv.org/abs/1911.13254 为波形域分离奠基工作。
- **当前主流架构**：Mel-Band RoFormer [72]、Band-Split RoPE Transformer [74]；集成式改进（bridging network）[78]；stem-agnostic 单解码器突破固定四轨 [79]。
- **任务定义演进**：SDX'23 音乐分离赛道提出 robust MSS（训练数据含错）形式化 [147]；SDX'23 技术报告 TFC-TDF-UNet v3 [149]；MSR（Music Source Restoration）从已混音/母带音频恢复未处理音轨 [73]。
- **场景化分离**：合唱音乐分离（用采样乐器合成数据增强）[76]；Cadenza Challenge 面向助听器的音乐分离/重混 [148]。
- **下游耦合**：利用音乐分离改进 Whisper 的自动歌词转录（ALT），解决伴奏干扰问题 [77]。
  **【权威】** [75][147][149] 为 arXiv 预印本/挑战赛总结（eess.AS），[147][149] 具挑战赛官方总结性质；[72][74][79] 为预印本｜**【热度】** `> 待核实`（注：本报告**未获得** MUSDB18/SDX25 上的可信 SDR 数值，故不列任何 SDR 数字）｜**【关注度】** 高：分离是本领域工程落地最成熟的分支之一（依据：本池中 MSS 相关条目最多且覆盖架构/竞赛/部署）｜**【推荐度】** ★★★★★（[72][74][79][147]）／★★★★☆（[73][76][77][148]）。

---

## 六、经典与奠基性工作

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| MusicLM: Generating Music From Text | 2023 | Google Research | `> 待核实` | 官方技术报告/arXiv | 高：文本到音乐奠基，社区引用广泛 | ★★★★★ | https://arxiv.org/abs/2301.11325 | 文本到音乐生成奠基工作 |
| MusicGen: Simple and Controllable Music Generation | 2023 | Meta（NeurIPS） | `> 待核实` | 同行评审（NeurIPS 2023） | 高：可控音乐生成代表 | ★★★★★ | https://arxiv.org/abs/2306.05284 | 可控音乐生成与单阶段 token 建模 |
| Music Source Separation in the Waveform Domain (Demucs) | 2019 | Meta | `> 待核实` | arXiv 预印本 | 高：波形域分离奠基 | ★★★★★ | https://arxiv.org/abs/1911.13254 | 波形域端到端分离 |
| End-to-end music source separation: is it possible in the waveform domain? | 2018 | arXiv 作者 | `> 待核实` | arXiv 预印本 | 中高：早期关键论证 | ★★★★☆ | http://arxiv.org/abs/1810.12187v2 | 波形域可行性论证 [75] |
| wav2vec 2.0 | 2020 | Meta AI | `> 待核实` | arXiv 预印本（后成领域标准） | 高：自监督语音/音频表征源头 | ★★★★★ | http://arxiv.org/abs/2006.11477v3 | 掩码潜变量 + 对比学习 [134] |
| HuBERT | 2021 | Meta AI | `> 待核实` | arXiv 预印本（后成领域标准） | 高：掩码预测隐藏单元范式 | ★★★★★ | http://arxiv.org/abs/2106.07447v1 | 自监督语音表征 [24] |
| A Functional Taxonomy of Music Generation Systems | 2018 | arXiv 作者 | `> 待核实` | arXiv 预印本（综述） | 中：分类骨架被持续引用 | ★★★★☆ | http://arxiv.org/abs/1812.04186v1 | 音乐生成功能分类学 [1] |
| Deep Learning Techniques for Music Generation — A Survey | 2017 | arXiv 作者 | `> 待核实` | arXiv 预印本（综述） | 中：DL 音乐生成早期综述 | ★★★★☆ | http://arxiv.org/abs/1709.01620v4 | 方法脉络梳理 [12] |
| Music SketchNet | 2020 | arXiv 作者 | `> 待核实` | arXiv 预印本 | 中：可控符号生成早期代表 | ★★★★☆ | http://arxiv.org/abs/2008.01291v1 | 音高/节奏因子化可控生成 [51] |
| Omnizart | 2021 | 台湾大学等 | `> 待核实` | arXiv 预印本 | 中：AMT 通用工具箱 | ★★★★☆ | https://arxiv.org/abs/2106.00497 | 自动音乐转录工具箱 [18] |
| Deep Salience Representations for F0 Estimation | — | — | `> 待核实` | Semantic Scholar 收录 | 中：多音高 F0 经典方法 | ★★★★☆ | https://www.semanticscholar.org/paper/859a5a49c6f1c1a508e19b23ca9c945585c27a0d | 深度显著性 F0 估计 [21] |
| Learning a Representation for Cover Song Identification Using CNN | 2019 | arXiv 作者 | `> 待核实` | arXiv 预印本 | 中：CSI 深度方法起点 | ★★★☆☆ | http://arxiv.org/abs/1911.00334v1 | 翻唱识别 CNN 表征 [41] |
| SDX'23 Music Demixing Track 总结 | 2023 | 挑战赛组织方 | `> 待核实` | 挑战赛官方总结（arXiv eess.AS） | 高：robust MSS 形式化来源 | ★★★★★ | http://arxiv.org/abs/2308.06979v4 | 定义训练数据含错下的 MSS [147] |

> **说明**：表中「热度」列全部为 `> 待核实`，原因是本次候选证据块未提供任何 citations / star / 下载量字段；报告不做数字估算。

---

## 七、数据集、评测与开放问题

### 7.1 数据集与基准

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| MUSDB18 / MUSDB18-HQ | — | sigsep 社区 | `> 待核实` | 社区标准数据集主页 | 高：音源分离事实标准 | ★★★★★ | https://sigsep.github.io/datasets/musdb.html | 分离训练/评测标准集 |
| MTG-Jamendo | — | MTG (UPF) | `> 待核实` | 官方 GitHub 仓库 | 中高：标签/情绪/乐器标注 | ★★★★☆ | https://github.com/MTG/mtg-jamendo-dataset | 多标签 MIR 数据集 |
| Million Song Dataset / AcousticBrainz | — | LabROSA / MTG | `> 待核实` | 官方主页 | 中高：大规模 MIR 元数据 | ★★★★☆ | http://millionsongdataset.com/ | 大规模元数据与音频特征 |
| Slakh2100 | — | 官方站点 | `> 待核实` | 官方主页 | 中：合成多轨分离集 | ★★★★☆ | http://www.slakh.com/ | 合成多轨数据 |
| GlobalMood | 2025 | arXiv 作者 | `> 待核实` | arXiv 预印本（cs.IR） | 中：跨文化情绪识别基准 | ★★★★☆ | http://arxiv.org/abs/2505.09539v2 | 明确批判西方/英语中心偏置 [4] |
| CCMusic | 2025 | arXiv 作者 | `> 待核实` | arXiv 预印本 | 中：中文音乐 MIR 数据库稀缺 | ★★★★☆ | http://arxiv.org/abs/2503.18802v1 | 中文音乐 MIR 开放数据库 [7] |
| PIAST | 2024 | arXiv 作者 | `> 待核实` | arXiv 预印本 | 中：钢琴多模态（音频+符号+文本） | ★★★★☆ | http://arxiv.org/abs/2411.02551v2 | 多模态钢琴数据集 [121] |
| Sanidha | 2025 | arXiv 作者 | `> 待核实` | arXiv 预印本 | 中：非西方古典音乐（Carnatic）录音室级多模态 | ★★★★☆ | http://arxiv.org/abs/2501.06959v1 | 文化多样性数据补充 [69] |
| SongEval | 2025 | arXiv 作者 | `> 待核实` | arXiv 预印本（eess.AS） | 中高：歌曲美学评测基准 | ★★★★☆ | http://arxiv.org/abs/2505.10793v1 | 面向主观美学的评测数据集 [161] |
| Story2MIDI 数据集 | 2025 | arXiv 作者 | `> 待核实` | arXiv 预印本（自建，公开性 `> 待核实`） | 低–中 | ★★★☆☆ | http://arxiv.org/abs/2512.02192v1 | 文本情感 ↔ 音乐情绪配对 [115] |
| 80K MIDI 多风格钢琴训练集 | 2025 | arXiv 作者（自建） | `> 待核实` | 论文自述，是否公开 `> 待核实` | 低 | ★★★☆☆ | http://arxiv.org/abs/2511.07268v2 | 用于规模/数据/指标对照实验 [53] |

### 7.2 评测口径与已知失效模式

- **分离任务口径**：SDR 类客观指标 + 挑战赛统一测试集；关键变化是 [147] 把「训练数据含错」纳入评测设定，[73] 进一步把评测目标从「分离」推向「复原」——**两者口径不可直接对比**。本报告**未获得**任何 MUSDB18/SDX25 的可信 SDR 数值，故不列数字。
- **生成任务口径**：客观指标与人类听感的一致性需要显式检验 [53]；主观质量预测被挑战赛化（AudioMOS 2025，含 T2M 整体质量与文本对齐两维度）[114]；美学评价被基准化（SongEval）[161]。
- **转录任务口径**：2025 AMT 挑战 8 支有效提交、2 支超过 MT3 基线 [95]——说明**基线仍然很强、进步幅度有限**。
- **评测方法论**：分数是有保质期的知识主张，多信号平均聚合导致信任膨胀 [47]；榜单运维本身存在系统性问题 [82]；基准中重复/相似题目会同时损害竞赛公平性与基准有效性，[59] 为此提供检索式检测基准（**注：CPRet 属竞赛编程领域，为方法论迁移参考，非音乐数据集**）。
- **音乐问答/检索口径**：多域 AQA 被拆为 Bioacoustics / Temporal Soundscapes / Complex QA 三个子集 [105]；文本到音频检索的时间理解被单独评测 [111]。

### 7.3 开放问题与争议

1. **评测可复现性与榜单有效性**：评测分数会随数据污染与分布漂移「过期」，多信号平均聚合造成信任膨胀 [47]；榜单运维存在系统性问题 [82]；基准重复题损害有效性 [59]。
2. **生成音乐评价指标**：量化指标与人类听感的一致性尚需系统检验，缺乏统一认可口径 [53]；尽管已有 AudioMOS [114] 与 SongEval [161] 等基准，仍未收敛。
3. **版权与数据合法性**：生成式音乐存在利用受版权保护创作的风险 [64]；隐私与版权的生命周期治理 [67]；机器遗忘作为 opt-out 机制仍处初步结果阶段 [64]。
4. **公平性与文化偏见**：偏见会错误表征边缘传统（尤其全球南方），产生不真实输出，并有文化消解风险，缓解建议落在 dataset / model / interface 三级 [62]；「民主化」话语可能仅是营销修辞 [63]；伦理声明本身的有效性亦被质疑 [66]。
5. **MIR 任务的分布外泛化**：节拍跟踪在 SMC 数据集上的系统性失败表明主流榜单饱和可能掩盖真实鲁棒性差距 [14]。
6. **SVC 滥用与检测**：给定证据池内**无任何直接来源**，当前无法评估，`> 待核实`。
7. **检索噪声带来的判断风险**：术语撞车（[35][39] 的 SVC、[80][83] 的 SDR）说明自动检索在音频领域需做术语消歧，否则会把无关噪声误读为领域进展。

---

## 八、建议关注清单（Watchlist）

**模型与方向**
1. 开放 T2M 基础模型的规模/可控性路线：ACE-Step [123]、YuE [124]、Stable Audio Open [119]；重点观察**是否开源权重与训练数据** `> 待核实`。
2. 音乐/音频-语言通用表征：M2D-CLAP [49] 与 CultureMERT [92]；跟踪其在 MIR 下游（标注 [94]、检索 [111]、问答 [106]）上的迁移结果。
3. 分离架构与任务定义的分离化：Band-Split RoFormer 系 [72][74][79] 与 MSR 方向 [73]；建议持续跟踪 SDX 系列榜单与 MUSDB18/SDX25 上的**官方榜单数值**（本报告未获得可信数值）。
4. 神经音频编解码的部署化指标：LRAC [91][84]、流式编码 [138]、能耗-质量权衡 [139]、Codec-SUPERB [135]。
5. 评测治理：评测分数时效性 [47]、榜单运维 [82]、生成音乐指标-听感对齐 [53][114][161]。
6. 音乐 AI 的公平性与合规：文化与流派偏见 [62]、产业话语批判 [63]、opt-out/遗忘 [64][67]、伦理声明实践 [66]。
7. 零样本 SVC/SVS 的真实鲁棒性：[29][36] 是否给出可复现实验与真歌场景指标 `> 待核实`。

**开源项目与资源**

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| facebookresearch/audiocraft | — | Meta | `> 待核实` | 官方 GitHub 仓库 | 高：MusicGen/AudioGen 官方工具链 | ★★★★★ | https://github.com/facebookresearch/audiocraft | 生成模型官方实现 |
| facebookresearch/demucs | — | Meta | `> 待核实` | 官方 GitHub 仓库 | 高：分离事实标准实现 | ★★★★★ | https://github.com/facebookresearch/demucs | SOTA 分离工具链 |
| deezer/spleeter | — | Deezer | `> 待核实` | 官方 GitHub 仓库 | 中高：经典快速分离基线 | ★★★★☆ | https://github.com/deezer/spleeter | 经典分离基线 |
| k2-fsa/k2 | — | k2 社区 | `> 待核实` | 官方 GitHub 仓库 | 中：语音/音频建模工具 | ★★★☆☆ | https://github.com/k2-fsa/k2 | 与音乐任务间接相关 |
| librosa/librosa | — | librosa 社区 | `> 待核实` | 官方 GitHub 仓库 | 高：MIR 特征事实标准 | ★★★★★ | https://github.com/librosa/librosa | MIR 特征与工具 |
| wzk1015/Awesome-Vision-to-Music-Generation | — | wzk1015 | `> 待核实` | 个人维护的 Awesome 列表 | 中：视觉到音乐生成的文献入口 | ★★★★☆ | https://github.com/wzk1015/Awesome-Vision-to-Music-Generation | 与综述 [52] 配套 [164] |

> 注：ACE-Step [123]、YuE [124]、YingMusic-SVC [36] 等是否提供官方开源仓库与权重，本报告**未获得可核查的仓库链接**，`> 待核实`，故未列入上表。

---

## 参考来源

> 以下为本次报告实际引用的来源编号（编号体系对应检索候选池 [1]–[164]）。

1. A Functional Taxonomy of Music Generation Systems — http://arxiv.org/abs/1812.04186v1
2. Symbolic Music Representations for Classification Tasks: A Systematic Evaluation — http://arxiv.org/abs/2309.02567v2
3. Barwise Music Structure Analysis with the Correlation Block-Matching Segmentation Algorithm — http://arxiv.org/abs/2311.18604v1
4. GlobalMood: A cross-cultural benchmark for music emotion recognition — http://arxiv.org/abs/2505.09539v2
5. MIRFLEX: Music Information Retrieval Feature Library for Extraction — http://arxiv.org/abs/2411.00469v1
6. Towards Multimodal MIR: Predicting individual differences from music-induced movement — http://arxiv.org/abs/2007.10695v1
7. CCMusic: An Open and Diverse Database for Chinese Music Information Retrieval Research — http://arxiv.org/abs/2503.18802v1
9. Chord Label Personalization through Deep Learning of Integrated Harmonic Interval-based Representations — http://arxiv.org/abs/1706.09552v1
10. Music Generation by Deep Learning - Challenges and Directions — http://arxiv.org/abs/1712.04371v2
12. Deep Learning Techniques for Music Generation -- A Survey — http://arxiv.org/abs/1709.01620v4
14. The SMC Blind Spot: A Failure Mode Analysis of State-of-the-Art Beat Tracking — http://arxiv.org/abs/2605.12287v1
17. Enhancing Automatic Chord Recognition through LLM Chain-of-Thought Reasoning — https://arxiv.org/abs/2509.18700
18. Omnizart: A General Toolbox for Automatic Music Transcription — https://arxiv.org/abs/2106.00497
20. Exploring wav2vec 2.0 on speaker verification and language identification — http://arxiv.org/abs/2012.06185v2
21. Deep Salience Representations for F0 Estimation in Polyphonic Music — https://www.semanticscholar.org/paper/859a5a49c6f1c1a508e19b23ca9c945585c27a0d
22. Application of Knowledge Distillation to Multi-task Speech Representation Learning — http://arxiv.org/abs/2210.16611v2
23. Automatic chord recognition based on the probabilistic modeling of diatonic modal harmony — https://www.semanticscholar.org/paper/a0b420c54060abb97899f30c4466e8699617efc8
24. HuBERT: Self-Supervised Speech Representation Learning by Masked Prediction of Hidden Units — http://arxiv.org/abs/2106.07447v1
25. ConSinger: Efficient High-Fidelity Singing Voice Generation with Minimal Steps — http://arxiv.org/abs/2410.15342v3
26. Singing voice synthesis based on convolutional neural networks — http://arxiv.org/abs/1904.06868v2
27. Fast and High-Quality Singing Voice Synthesis System based on Convolutional Neural Networks — http://arxiv.org/abs/1910.11690v2
28. NaturalSpeech 2: Latent Diffusion Models are Natural and Zero-Shot Speech and Singing Synthesizers — http://arxiv.org/abs/2304.09116v3
29. TCSinger 2: Customizable Multilingual Zero-shot Singing Voice Synthesis — http://arxiv.org/abs/2505.14910v3
30. Zero-Shot Sing Voice Conversion: built upon clustering-based phoneme representations — http://arxiv.org/abs/2409.08039v2
31. Everyone-Can-Sing: Zero-Shot Singing Voice Synthesis and Conversion with Speech Reference — http://arxiv.org/abs/2501.13870v1
32. Towards Improved Zero-shot Voice Conversion with Conditional DSVAE — http://arxiv.org/abs/2205.05227v2
33. LDM-SVC: Latent Diffusion Model Based Zero-Shot Any-to-Any Singing Voice Conversion with Singer Guidance — http://arxiv.org/abs/2406.05325v1
34. FlashSpeech: Efficient Zero-Shot Speech Synthesis — http://arxiv.org/abs/2404.14700v4
35. SVC 2025: the First Multimodal Deception Detection Challenge — http://arxiv.org/abs/2508.04129v1 （**术语撞车：此处 SVC = Subtle Visual Cues，非歌声转换**）
36. YingMusic-SVC: Real-World Robust Zero-Shot Singing Voice Conversion with Flow-GRPO and Singing-Specific Inductive Biases — http://arxiv.org/abs/2512.04793v1
39. SVC 2026: the Second Multimodal Deception Detection Challenge and the First Domain Generalized Remote Physiological Measurement Challenge — http://arxiv.org/abs/2604.05748v1 （**术语撞车，同上**）
41. Learning a Representation for Cover Song Identification Using Convolutional Neural Network — http://arxiv.org/abs/1911.00334v1
42. Large-Scale Cover Song Detection in Digital Music Libraries Using Metadata, Lyrics and Audio Features — http://arxiv.org/abs/1808.10351v1
46. Modelling Emotion Dynamics in Song Lyrics with State Space Models — http://arxiv.org/abs/2210.09434v1
47. Position: Evaluation Scores Are Perishable Knowledge Claims — http://arxiv.org/abs/2607.26191v1
49. M2D-CLAP: Exploring General-purpose Audio-Language Representations Beyond CLAP — http://arxiv.org/abs/2503.22104v2
50. Learning to Traverse Latent Spaces for Musical Score Inpainting — http://arxiv.org/abs/1907.01164v1
51. Music SketchNet: Controllable Music Generation via Factorized Representations of Pitch and Rhythm — http://arxiv.org/abs/2008.01291v1
52. Vision-to-Music Generation: A Survey — http://arxiv.org/abs/2503.21254v1
53. Generating Piano Music with Transformers: A Comparative Study of Scale, Data, and Metrics — http://arxiv.org/abs/2511.07268v2
59. CPRet: A Dataset, Benchmark, and Model for Retrieval in Competitive Programming — http://arxiv.org/abs/2505.12925v2
62. Who Gets Heard? Rethinking Fairness in AI for Music Systems — http://arxiv.org/abs/2511.05953v1
63. Opening Musical Creativity? Embedded Ideologies in Generative-AI Music Systems — http://arxiv.org/abs/2508.08805v1
64. No Encore: Unlearning as Opt-Out in Music Generation — http://arxiv.org/abs/2509.06277v2
66. Ethics Statements in AI Music Papers: The Effective and the Ineffective — http://arxiv.org/abs/2509.25496v1
67. Privacy and Copyright Protection in Generative AI: A Lifecycle Perspective — http://arxiv.org/abs/2311.18252v3
68. The Shape of Surprise: Structured Uncertainty and Co-Creativity in AI Music Tools — http://arxiv.org/abs/2509.25028v1
69. Sanidha: A Studio Quality Multi-Modal Dataset for Carnatic Music — http://arxiv.org/abs/2501.06959v1
72. Mel-Band RoFormer for Music Source Separation — http://arxiv.org/abs/2310.01809v1
73. Multi-Stage Music Source Restoration with BandSplit-RoFormer Separation and HiFi++ GAN — http://arxiv.org/abs/2603.04032v1
74. Music Source Separation with Band-Split RoPE Transformer — http://arxiv.org/abs/2309.02612v2
75. End-to-end music source separation: is it possible in the waveform domain? — http://arxiv.org/abs/1810.12187v2
76. Improving Choral Music Separation through Expressive Synthesized Data from Sampled Instruments — http://arxiv.org/abs/2209.02871v1
77. Exploiting Music Source Separation for Automatic Lyrics Transcription with Whisper — http://arxiv.org/abs/2506.15514v1
78. The Whole Is Greater than the Sum of Its Parts: Improving Music Source Separation by Bridging Network — http://arxiv.org/abs/2305.07855v2
79. A Stem-Agnostic Single-Decoder System for Music Source Separation Beyond Four Stems — http://arxiv.org/abs/2406.18747v2
82. On the Workflows and Smells of Leaderboard Operations (LBOps): An Exploratory Study of Foundation Model Leaderboards — http://arxiv.org/abs/2407.04065v4
84. Baseline Systems For The 2025 Low-Resource Audio Codec Challenge — http://arxiv.org/abs/2510.00264v3
85. HiFi-Codec: Group-residual Vector quantization for High Fidelity Audio Codec — http://arxiv.org/abs/2305.02765v2
86. WavTokenizer: an Efficient Acoustic Discrete Codec Tokenizer for Audio Language Modeling — http://arxiv.org/abs/2408.16532v3
87. APCodec: A Neural Audio Codec with Parallel Amplitude and Phase Spectrum Encoding and Decoding — http://arxiv.org/abs/2402.10533v2
88. DualCodec: A Low-Frame-Rate, Semantically-Enhanced Neural Audio Codec for Speech Generation — http://arxiv.org/abs/2505.13000v2
89. Bringing Interpretability to Neural Audio Codecs — http://arxiv.org/abs/2506.04492v1
90. A Closer Look at Neural Codec Resynthesis: Bridging the Gap between Codec and Waveform Generation — http://arxiv.org/abs/2410.22448v1
91. Low-Resource Audio Codec (LRAC): 2025 Challenge Description — http://arxiv.org/abs/2510.23312v2
92. CultureMERT: Continual Pre-Training for Cross-Cultural Music Representation Learning — http://arxiv.org/abs/2506.17818v1
93. MusCaps: Generating Captions for Music Audio — http://arxiv.org/abs/2104.11984v1
94. Joint Music and Language Attention Models for Zero-shot Music Tagging — http://arxiv.org/abs/2310.10159v1
95. Advancing Multi

---

*Generated by research-bot · topic=`music-audio` · depth=`standard` · rounds=2 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading · model=`deepseek-v4-flash` · sources=164 · duration=695s · 2026-10-06T23:03:22+00:00*
