# 音乐与音频算法调研报告：MIR / 生成 / 理解 / 分离

**元信息**：生成日期 2026-10-04（UTC）｜领域：Music & Audio（MIR、文本到音乐生成、音乐理解与自监督音频表征、歌声转换与翻唱识别、音源分离与神经音频编解码）｜检索源：本次允许引用编号共 112 条，其中与主题直接相关约 60 条；另有领域种子资源（papers/projects/datasets）若干，按用户提供的真实 URL 保留。
**证据纪律说明**：本次候选证据块**普遍未提供引用数、GitHub star、下载量或榜单排名**，因此下文所有「热度证据」若无数值一律标注 `> 待核实`，不做任何数字编造；「权威证据」仅依据候选块给出的 arXiv 分类号与 Comments，「关注度」依据该条目的类型（挑战赛总结/获胜系统/数据集论文等）做定性判断。

---

## 摘要（Executive Summary）

1. **生成侧的主线变化是从「单段音频 token 自回归」走向「分层规划 + 流匹配/扩散渲染」的全曲生成**：最新工作把歌曲拆成结构、歌词、旋律、渲染多级来生成，并显式建模 song form [92][91][96]。典型可控性手段是节奏/和弦条件 [84]、指令式编辑 [88]、辅助条件分支 [80]。
2. **评测正从客观距离（FAD 类）向「主观质量 + 文本对齐」转移**：出现了面向合成音频主观质量预测的首个挑战赛 AudioMOS 2025 [79]，以及基于人类偏好研究来校准生成模型与指标的工作 [64]。
3. **音乐理解侧的关键词是「音乐基础模型 + 跨文化泛化」**：MERT 系做多文化持续预训练并在非西方 auto-tagging 上报告增益 [44]；MuQ 被第三方团队用于 AudioMOS 2025 Track1 获胜系统 [48]；另有把音乐基础模型当通用 booster 的下游迁移研究 [61]、半监督对比音乐表征 [54]、零样本音乐标注 [46]。**但「音乐基础模型 vs 通用语音 SSL（wav2vec2/HuBERT/WavLM）」的独立第三方对比在本次证据中缺失** [44][47][48] → `> 待核实`。
4. **音源分离已从「分离」演进为「修复/去制作化」**：Band-Split RNN [111] → BS-RoFormer [98] → Mel-Band RoFormer [99] → Mel-RoFormer（人声/旋律）[110]，并出现面向 Music Source Restoration 的多级系统 [100]；神经编解码侧关注点转向「编解码与波形生成之间的差距」与统一基准 [109][108]。
5. **歌声方向（SVC/SVS）近两年主线是零样本、多语种、可定制** [26][28][29]，并以潜空间扩散 TTS 为技术母体 [23]；经典 CNN SVS 仍具参考价值 [24][25]。
6. **证据缺口与争议**：审美主观性 [64][79]、版权与训练数据合规、伦理表述 [73][74][77]、榜单/挑战赛规模过小 [47]、以及「demo 视频 ≠ 实验证据」是反复出现的风险点。本次检索还存在明显噪声（短视频参与度预测 [20]、基础模型透明度指数 [21]、越南法律问答 [112] 等与本主题无关）。

---

## 一、关键前沿进展（近 1–2 年）

| 进展 | 时间 | 机构/作者 | 一句话贡献 | 四条证据轴 |
|---|---|---|---|---|
| Hierarchical Autoregressive Planning + Flow-Matching Rendering（全曲生成）[92] | 2026 | arXiv cs.SD | 用分层自回归规划 + 流匹配渲染推进全曲生成前沿 | 热度 `> 待核实`；权威：arXiv 预印本 cs.SD；关注度 中（命题直接命中全曲生成热点）；推荐度 ★★★★☆（相关度最高，但需等同行评审与复现） |
| Song Form-aware Full-Song Text-to-Lyrics [91] | 2024–2026 | arXiv cs.SD | 按歌曲结构生成歌词，并做多级粒度音节数控制 | 热度 `> 待核实`；权威：arXiv 预印本 cs.SD；关注度 中；推荐度 ★★★★☆（歌词可控性是生成链路薄弱环节） |
| MusiConGen：Transformer 文本到音乐的节奏与和弦控制 [84] | 2024 | arXiv cs.SD | 在 Transformer T2M 上加入节奏/和弦条件，提升音乐学可控性 | 热度 `> 待核实`；权威：arXiv 预印本 cs.SD；关注度 高（可控性是被反复点名的痛点）；推荐度 ★★★★☆ |
| Instruct-MusicGen：指令微调实现音乐编辑 [88] | 2024 | arXiv cs.SD | 用指令微调解锁音乐语言模型的「编辑」能力（增删乐器、改风格） | 热度 `> 待核实`；权威：arXiv 预印本 cs.SD；关注度 高；推荐度 ★★★★☆ |
| AudioMOS Challenge 2025（合成音频主观质量预测）[79] | 2025 | arXiv cs.SD | 首个面向合成音频「整体质量 + 文本对齐」主观质量自动预测的挑战赛 | 热度 `> 待核实`；权威：挑战赛总结论文，arXiv cs.SD；关注度 高（评测范式转向）；推荐度 ★★★★★ |
| Benchmarking Music Generation Models and Metrics via Human Preference Studies [64] | 2025 | arXiv cs.LG | 用人类偏好研究同时校准生成模型与客观指标 | 热度 `> 待核实`；权威：arXiv 预印本 cs.LG；关注度 高；推荐度 ★★★★★ |
| CultureMERT：多文化持续预训练的音乐表征 [44] | 2025 | arXiv cs.SD | 两阶段持续预训练（lr re-warming/re-decaying）+ 650 小时多文化数据，非西方 auto-tagging 平均提升，西方基准遗忘小 | 热度 `> 待核实`；权威：arXiv 预印本 cs.SD，未见同行评审 venue；关注度 中；推荐度 ★★★★☆ |
| Music Foundation Model as Generic Booster for Music Downstream Tasks [61] | 2024– | arXiv | 把音乐基础模型当作通用增强器复用到多下游任务 | 热度 `> 待核实`；权威：arXiv 预印本；关注度 中；推荐度 ★★★★☆（直接回应「跨任务可迁移性」） |
| Stable Audio Open（开放权重 T2A/T2M）[76] | 2024 | Stability AI（预印本） | 开放模型与数据配方，推动可复现生成研究 | 热度 `> 待核实`；权威：arXiv 预印本；关注度 高；推荐度 ★★★★★ |
| Stable Audio 3 [90] | 2026 | arXiv cs.SD | 该系列的后续代际（标题仅示版本号，能力细节 `> 待核实`） | 热度 `> 待核实`；权威：arXiv 预印本；关注度 中；推荐度 ★★★☆☆（正文细节待读全文） |
| BS-RoFormer / Mel-Band RoFormer / Mel-RoFormer [98][99][110] | 2023–2024 | arXiv cs.SD | 以 band-split + RoPE 注意力取代/增强 RNN 与纯频域方案，成为分离主流架构 | 热度 `> 待核实`；权威：arXiv 预印本 cs.SD；关注度 高（社区广泛复现，音乐分离榜单常用）；推荐度 ★★★★★ |
| Music Source Restoration（MSR，ICASSP Challenge 系统）[100] | 2026 | arXiv cs.SD | 目标不是「分轨」而是恢复未做过母带处理的原始 stems，BandSplit-RoFormer + HiFi++ GAN 多级方案 | 热度 `> 待核实`；权威：技术报告/arXiv cs.SD；关注度 中高（任务定义是新的）；推荐度 ★★★★☆ |
| 神经编解码评测与再合成差距 [108][109][106][105][104] | 2023–2025 | 多团队 | 从「高保真 codec」转向「统一基准 + codec↔波形生成差距」 | 热度 `> 待核实`；权威：含 SLT 2024 关联基准 [108]；关注度 中高；推荐度 ★★★★☆ |
| 零样本多语种歌声转换（FreeSVC、Everyone-Can-Sing）[28][29] | 2025 | arXiv | 无需目标歌手微调的跨语种 SVC/SVS，语音参考即可唱 | 热度 `> 待核实`；权威：arXiv 预印本；关注度 中高；推荐度 ★★★★☆ |

**被点名但本次证据缺失的方向**：MusicGen 之外的 AudioLDM2、YuE、ACE-Step、DiffRhythm 的**具体贡献与代际关系**在本次可引用编号中未见对应条目（[12][76][84][88][90][92] 均非上述模型）→ `> 待核实`，需补充一手论文与官方仓库后再下结论。

---

## 二、音乐信息检索（MIR / 翻唱识别 CSI / 节拍与和声）

**和声与结构（经典任务仍在演进）**
- 和弦识别作为 MIR 基础任务，其任务定义与特征/模型演进在 [7] 中有系统梳理。
- 音乐结构分析（MSA）方向，[4] 扩展了 Correlation Block-Matching 分割算法，提出 barwise 结构分析，说明「小节级」结构粒度仍是活跃方向。
- 符号音乐的表征选择（图像式 vs 语言式）缺乏统一结论，[3] 做了系统性评测，指出符号音乐既非图像也非句子。

**多模态与跨模态转换**
- [19] 提出乐谱图像、符号音乐、演奏音频之间的统一跨模态翻译，把 AMT、OMR 等核心 MIR 任务纳入同一框架。
- [8] 用实例分割增强光学音乐识别（OMR）的信息检索；[10] 用循环模型做 audio-sheet 检索的段落摘要；[9] 用潜空间遍历做乐谱 inpainting——这三条构成「乐谱—音频」双向检索与生成的老中青脉络。
- [5] 与 [69]（MOSA：Music Motion with Semantic Annotation）把「音乐诱发的身体运动」纳入 MIR，代表多模态 MIR 的扩展方向。

**自动标注 / 转写**
- 零样本音乐标注：[46] 提出联合音乐与语言注意力模型（Joint Music and Language Attention），是「标注即检索/对齐」路线的代表。
- 多乐器自动音乐转写（AMT）现状：2025 AMT Challenge 共 8 支队伍提交有效方案，**仅 2 支超过 baseline MT3**，作者把剩余难点归为 polyphony（复调）与 timbre variation（音色变化）[47]。这是本报告中**少见的带可比口径的失败案例证据**。
- 歌词转写（ALT）：[103] 用音源分离预处理 + Whisper 提升自动歌词转写；工程侧另有 [96] SongPrep 做全曲结构解析与歌词转写的端到端预处理框架。
- 工具链：[2] 提供可扩展的模块化音乐特征抽取库（key、downbeat、genre、乐器识别等），是复现实验的实用基础设施。

**翻唱识别（CSI）**
- 从 CNN 表征学习 [36]，到多损失训练的 ByteCover [37]，到 ByteCover 系列之后的 CoverHunter（精炼注意力与对齐）[39]，构成深度学习 CSI 的主干；[38] 则讨论了数字音乐库规模下的元数据+歌词+音频特征组合策略。**注意**：本次证据未提供 Covers80、Da-TACOS、SHS100K 等基准上的具体数字，也未见跨版本/跨语言/跨音色的统一评测结论 → `> 待核实`。

| 条目 | 热度证据 | 权威证据 | 关注度 | 推荐度 |
|---|---|---|---|---|
| ByteCover（多损失训练 CSI）[37] | `> 待核实` | arXiv 预印本 cs.SD（arXiv:2010.14022v2） | 高——CSI 领域被广泛引用的方法名，但本次无引用数 | ★★★★☆（CSI 主线必读，需自查榜单数字） |
| CoverHunter [39] | `> 待核实` | arXiv 预印本（arXiv:2306.09025v1） | 中高 | ★★★★☆ |
| CNN cover song representation [36] | `> 待核实` | arXiv 预印本（arXiv:1911.00334v1） | 中 | ★★★☆☆（更偏历史脉络） |
| 2025 AMT Challenge 结果 [47] | `> 待核实`（未给引用/榜单链接） | arXiv 预印本，Comments 标注 Accepted to the AI for Music Workshop at NeurIPS 2025 | 中——workshop 级基准，参赛 8 队 | ★★★☆☆（作为难度与评测口径证据有用） |
| MIRFLEX [2] | `> 待核实` | arXiv 预印本 cs.SD（arXiv:2411.00469v1） | 中——工具型工作 | ★★★★☆（工程复用价值高） |

---

## 三、音乐生成（文本/符号/音频）

**（1）文本到音频/音乐：从奠基到开放权重**
- 奠基脉络见第六节：[12] MusicLM（文本到音乐奠基）与 [6] 功能分类学。
- 开放权重与可复现：[76] Stable Audio Open 明确提供开放模型/数据配方；[90] 为该系列 2026 年的后续版本（细节 `> 待核实`）。
- 低数据/小模型场景：[82] 在 ICME 2026 Academic Text-to-Music Grand Challenge 中研究 batch sampling 策略对低数据、小模型 T2M 的影响，是难得的「学术约束下」生成研究。
- 乐器化生成的条件分支：[80] 用 auxiliary conditioning branches 研究在剥离大规模数据/外部预训练影响后，哪些设计真正起作用——方法论上很有价值。
- 情感对齐的符号生成：[83] Story2MIDI 用 seq2seq Transformer 从文本生成情感对齐的 MIDI，并自建文本情感 + 音乐情感合并数据集。

**（2）可控性与长时结构**
- 节奏/和弦条件：[84] MusiConGen。
- 指令编辑：[88] Instruct-MusicGen。
- 歌词侧结构控制：[91] 按 song form 生成歌词并控制音节数粒度；[94] CSL-L2M 用条件 Transformer 做歌曲级「歌词→旋律」生成，并给出细粒度歌词与音乐控制。
- 全曲分层生成：[92] 自回归规划 + flow-matching 渲染。
- 音频修复/补全作为生成子问题：[14] 扩散式音频 inpainting（补充音乐生成的可控编辑能力）。

**（3）生成评测与挑战赛生态**
- AudioMOS 2025 [79]：首个针对合成音频的主观质量预测挑战赛，含整体质量与文本对齐跟踪。
- 人类偏好校准研究 [64]：把主观偏好与客观指标对齐。
- 相关音频生成挑战赛：[86] ICAGC 2024（启发式与可信音频生成）、[87] Sound Scene Synthesis 文本到音频生成评测、[89] NPU-HWC 参赛系统——虽非纯音乐，但共享评测方法论。
- 综述：[63] Vision-to-Music Generation 综述（视觉→音乐的生成综述）。

> **待核实**：AudioLDM2、YuE、ACE-Step、DiffRhythm 的具体架构与代际关系；MusicGen 论文 [种子] 与上述模型的可比数字；生成模型的 FAD/KL/CLAP 分数口径。本次证据块不含这些数值。

---

## 四、音乐理解与自监督表征

**预训练范式**
- **两阶段持续预训练（跨文化适配）**：[44] CultureMERT-95M 在既有音乐基础模型上做持续预训练，提出含 learning rate re-warming 与 re-decaying 的两阶段策略，训练数据为 650 小时 Greek/Turkish/Indian 混合；报告在多种非西方音乐 auto-tagging 上 ROC-AUC 与 AP 平均提升 4.9%，且对西方中心基准遗忘小。**注意这是作者自报，且为预印本** [44]。
- **音乐基础模型作为下游 booster**：[61] 直接探讨把音乐基础模型复用到多个下游任务，是回答「跨任务可迁移性」的最相关条目之一。
- **半监督/对比学习路线**：[54] 用半监督对比学习得到音乐表征，代表「不依赖超大标注」的方向。
- **标注/理解即对齐**：[46] 联合音乐与语言注意力做零样本音乐标注。
- **音频描述生成**：[107] MusCaps 从音频生成音乐描述，是音乐理解→自然语言输出的早期代表。
- **情感/文化基准**：[1] GlobalMood 指出既有情感数据集以西方歌曲 + 英文术语为主，提出跨文化音乐情绪识别基准。这与 [44] 的动机完全一致，形成**两条独立来源的交叉印证**（跨文化泛化是公认短板）[1][44]。
- **非西方音乐数据**：[62] Sanidha 提供 Carnatic（南印度古典）音乐的工作室级多模态数据集。

**关键缺口（必须标注）**
- 候选证据中**没有** MusicFM、CLAP 的任何条目；也**没有** MERT/MusicFM/MuQ/CLAP 相对 wav2vec2 / HuBERT / WavLM 在音乐任务上的独立第三方系统对比。唯一接近的第三方复用证据是 AudioMOS 2025 Track1 获胜系统采用预训练 MuQ + RoBERTa 双分支 [48]，但该工作并未与通用语音 SSL 对比 [44][47][48] → `> 待核实`。

| 条目 | 热度证据 | 权威证据 | 关注度 | 推荐度 |
|---|---|---|---|---|
| CultureMERT [44] | `> 待核实`（无引用数） | arXiv 预印本 cs.SD（arXiv:2506.17818v1），未见 venue | 中——2025-06 新预印本，直击 MERT/跨文化 | ★★★★☆（数据配方与指标口径可核查，但增益为自报） |
| Music Foundation Model as Booster [61] | `> 待核实` | arXiv 预印本（arXiv:2411.01135v3） | 中 | ★★★★☆ |
| ASTAR-NTU @ AudioMOS 2025 Track1（用 MuQ）[48] | `> 待核实` | arXiv 预印本 cs.SD；挑战赛获胜系统，团队自报 | 中——唯一跨团队下游复用证据 | ★★★★☆ |
| GlobalMood [1] | `> 待核实` | arXiv 预印本 cs.IR（arXiv:2505.09539v2） | 中 | ★★★★☆（与 [44] 互相印证跨文化缺口） |
| Sanidha（Carnatic 多模态数据）[62] | `> 待核实` | arXiv 预印本（arXiv:2501.06959v1） | 中低 | ★★★☆☆ |
| Semi-Supervised Contrastive Musical Representations [54] | `> 待核实` | arXiv 预印本（arXiv:2407.13840v1） | 中低 | ★★★☆☆ |

---

## 五、歌声转换（SVC）与音源分离

**（1）歌声合成/转换（SVS/SVC）**
- 经典 CNN 路线：[24]（CNN-based SVS）与 [25]（快速高质量 CNN SVS 系统）确立了从 DNN 到 CNN 的过渡，强调合成自然度与速度的权衡。
- 潜空间扩散母体：[23] NaturalSpeech 2 用潜扩散实现零样本语音与**歌声**合成，是后续 SVC/SVS 扩散方案的共同技术祖先（**注**：该文 2023 年，属经典而非最新）。
- 近两年主线=零样本 + 多语种 + 可定制：[26] TCSinger 2 指出既有 SVS 过度依赖音素与音符边界标注，导致零样本鲁棒性差，转向可定制多语种零样本 SVS；[28] FreeSVC 做零样本多语种**歌声转换**；[29] Everyone-Can-Sing 用语音参考实现零样本 SVS + SVC。
- 效率方向：[22] ConSinger 用极少步数做高保真歌声生成，直接针对扩散推理慢的问题。
- 语音侧可迁移方法：[27] Conditional DSVAE 零样本语音转换，为「内容-音色解耦」提供早期方案（音色泄漏问题的经典切入点）。
- **待核实**：音高/音色泄漏（pitch leakage / timbre leakage）的定量评测协议与跨语种 SVC 的公开榜单，本次证据未见。

**（2）音源分离（MSS）**
架构演进链条（本报告可核查）：
1. 波形域端到端是否可行：[102]（2018）提出并讨论端到端波形域分离的可行性，是 Demucs 之后/同期问题意识的代表。
2. Band-Split RNN：[111]（2022）提出 band-split RNN 用于音乐分离，成为后续 RoFormer 系列的结构基础。
3. Band-Split RoPE Transformer（BS-RoFormer）：[98]（2023）把 RoPE 注意力引入 band-split 框架。
4. Mel-Band RoFormer：[99]（2023）在 Mel 频带划分下应用 RoFormer，改善高频/人声表现。
5. Mel-RoFormer（人声分离 + 人声旋律转写）：[110]（2024）把分离与旋律转写联合。
6. 工程基线：[101] KUIELab-MDX-Net 双流网络（MDX 框架下的经典基线）；[70] 用采样乐器合成的表现力数据改进合唱分离（数据合成路线）。
7. 任务升级：Music Source Restoration [100] 指出母带处理与发行伪影破坏线性混合假设，因此目标从「分轨」变为「恢复未处理 stems」，并用 BandSplit-RoFormer + HiFi++ GAN 多级系统参赛。
8. 下游复用：分离作为前端提升歌词转写 [103]。

**（3）神经音频编解码**
- 高保真 codec：[104] HiFi-Codec 提出 group-residual vector quantization，改善 codec 保真度。
- 频谱建模：[105] APCodec 并行编码幅度与相位谱。
- 面向音乐声码器：[106] 用神经音频 codec 构建高保真音乐声码器（2025）。
- 评测基准：[108] Codec-SUPERB @ SLT 2024 提出轻量神经音频 codec 统一基准，是「可比性」问题的直接答案。
- 关键分析：[109] 检视神经 codec 再合成，指出 codec 与波形生成之间存在差距（对下游生成/理解复用性至关重要）。
- 资源受限与鲁棒性：[85] 2025 Low-Resource Audio Codec Challenge 基线系统（低保真预算 + 噪声/混响条件下的神经语音 codec）；[45] IEEE-IS2 2024 Music Packet Loss Concealment Challenge（音乐传输丢包补偿）。
- **待核实**：SoundStream、EnCodec、DAC、Mimi、SNAC 在音乐上的重建质量、token 率与下游复用的对比数字，本次证据块**完全缺失** → 必须补检索后再断言。

| 条目 | 热度证据 | 权威证据 | 关注度 | 推荐度 |
|---|---|---|---|---|
| Band-Split RNN [111] | `> 待核实` | arXiv 预印本（arXiv:2209.15174v1） | 高——后续 RoFormer 系列的结构基础 | ★★★★★ |
| BS-RoFormer [98] | `> 待核实` | arXiv 预印本 cs.SD（arXiv:2309.02612v2） | 高——社区复现/榜单常用 | ★★★★★ |
| Mel-Band RoFormer [99] / Mel-RoFormer [110] | `> 待核实` | arXiv 预印本（2310.01809v1 / 2409.04702v1） | 高 | ★★★★★ |
| Music Source Restoration [100] | `> 待核实` | arXiv 技术报告 cs.SD（arXiv:2603.04032v1） | 中高——新任务定义 | ★★★★☆ |
| Codec-SUPERB @ SLT 2024 [108] | `> 待核实` | 与 SLT 2024 关联的基准论文（arXiv:2409.14085v1） | 中高 | ★★★★★（codec 可比性必读） |
| Neural Codec Resynthesis 分析 [109] | `> 待核实` | arXiv 预印本（arXiv:2410.22448v1） | 中 | ★★★★☆ |
| TCSinger 2 [26] / FreeSVC [28] / Everyone-Can-Sing [29] | `> 待核实` | 均为 arXiv 预印本（2505.14910v3 / 2501.05586v1 / 2501.13870v1） | 中高——零样本多语种 SVC 热点 | ★★★★☆ |
| ConSinger [22] | `> 待核实` | arXiv 预印本（arXiv:2410.15342v3） | 中 | ★★★★☆（效率视角） |

---

## 六、经典与奠基性工作

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| MusicLM: Generating Music From Text [12] | 2023 | Google Research | `> 待核实` | arXiv 预印本 cs.SD（arXiv:2301.11325v1） | 高——文本到音乐奠基性工作 | ★★★★★ | http://arxiv.org/abs/2301.11325v1 | 文本到音乐生成范式奠基 |
| MusicGen: Simple and Controllable Music Generation | 2023 | Meta（NeurIPS） | `> 待核实` | 种子资源标注 NeurIPS 2023（`> 待核实` 原文 venue） | 高——可控生成代表作 | ★★★★★ | https://arxiv.org/abs/2306.05284 | 可控音乐生成，audiocraft 工具链母体 |
| Music Source Separation in the Waveform Domain (Demucs) | 2019 | Meta | `> 待核实` | 种子资源（arXiv 1911.13254） | 高——波形域分离里程碑 | ★★★★★ | https://arxiv.org/abs/1911.13254 | 波形域音源分离奠基 |
| A Functional Taxonomy of Music Generation Systems [6] | 2018 | arXiv | `> 待核实` | arXiv 预印本（arXiv:1812.04186v1） | 中——分类学参考 | ★★★★☆ | http://arxiv.org/abs/1812.04186v1 | 音乐生成系统的功能分类骨架 |
| Chord Recognition – Music and Audio Information Retrieval [7] | 2021 | arXiv | `> 待核实` | arXiv 预印本（arXiv:2105.07019v2） | 中 | ★★★☆☆ | http://arxiv.org/abs/2105.07019v2 | 和弦识别任务与路线梳理 |
| Music SketchNet [11] | 2020 | arXiv | `> 待核实` | arXiv 预印本（arXiv:2008.01291v1） | 中 | ★★★☆☆ | http://arxiv.org/abs/2008.01291v1 | 通过音高/节奏因式分解实现可控生成（可控性思想源头之一） |
| Learning to Traverse Latent Spaces for Musical Score Inpainting [9] | 2019 | arXiv | `> 待核实` | arXiv 预印本（arXiv:1907.01164v1） | 中低 | ★★★☆☆ | http://arxiv.org/abs/1907.01164v1 | 乐谱补全的潜空间方法 |
| Passage Summarization with Recurrent Models for Audio-Sheet Music Retrieval [10] | 2023 | arXiv | `> 待核实` | arXiv 预印本（arXiv:2309.12111v1） | 中低 | ★★★☆☆ | http://arxiv.org/abs/2309.12111v1 | 跨模态乐谱检索 |
| Symbolic Music Representations for Classification Tasks [3] | 2023 | arXiv | `> 待核实` | arXiv 预印本（arXiv:2309.02567v2） | 中 | ★★★★☆ | http://arxiv.org/abs/2309.02567v2 | 符号音乐表征的系统性评测 |
| Barwise Music Structure Analysis (CBM) [4] | 2023 | arXiv | `> 待核实` | arXiv 预印本（arXiv:2311.18604v1） | 中 | ★★★☆☆ | http://arxiv.org/abs/2311.18604v1 | MSA 的小节级结构分割 |
| Singing voice synthesis based on CNN [24] / Fast & High-Quality CNN SVS [25] | 2019 | arXiv | `> 待核实` | arXiv 预印本（1904.06868v2 / 1910.11690v2） | 中 | ★★★☆☆ | http://arxiv.org/abs/1904.06868v2 ｜ http://arxiv.org/abs/1910.11690v2 | CNN 时代 SVS 代表 |
| NaturalSpeech 2 [23] | 2023 | Microsoft（预印本） | `> 待核实` | arXiv 预印本 eess.AS（arXiv:2304.09116v3） | 高——零样本语音/歌声扩散合成母体 | ★★★★★ | http://arxiv.org/abs/2304.09116v3 | 潜扩散 + 零样本语音与歌声合成 |
| Towards Improved Zero-shot Voice Conversion with Conditional DSVAE [27] | 2022 | arXiv | `> 待核实` | arXiv 预印本（arXiv:2205.05227v2） | 中 | ★★★★☆ | http://arxiv.org/abs/2205.05227v2 | 内容-说话人解耦的经典零样本 VC |
| ByteCover [37] / CoverHunter [39] | 2020 / 2023 | arXiv | `> 待核实` | arXiv 预印本（2010.14022v2 / 2306.09025v1） | 高（CSI 主线） | ★★★★☆ | http://arxiv.org/abs/2010.14022v2 ｜ http://arxiv.org/abs/2306.09025v1 | 翻唱识别深度学习方法主线 |
| Large-Scale Cover Song Detection [38] | 2018 | arXiv | `> 待核实` | arXiv 预印本（arXiv:1808.10351v1） | 中低 | ★★★☆☆ | http://arxiv.org/abs/1808.10351v1 | 元数据+歌词+音频特征的大规模检索 |
| End-to-end music source separation in the waveform domain [102] | 2018 | arXiv | `> 待核实` | arXiv 预印本（arXiv:1810.12187v2） | 中 | ★★★★☆ | http://arxiv.org/abs/1810.12187v2 | 波形域端到端分离的可行性讨论 |
| Music Source Separation with Band-split RNN [111] | 2022 | arXiv | `> 待核实` | arXiv 预印本（arXiv:2209.15174v1） | 高 | ★★★★★ | http://arxiv.org/abs/2209.15174v1 | RoFormer 系列的结构前身 |
| KUIELab-MDX-Net [101] | 2021 | arXiv | `> 待核实` | arXiv 预印本（arXiv:2111.12203v1） | 中 | ★★★☆☆ | http://arxiv.org/abs/2111.12203v1 | MDX 框架下的双流基线 |
| MusCaps: Generating Captions for Music Audio [107] | 2021 | arXiv | `> 待核实` | arXiv 预印本（arXiv:2104.11984v1） | 中低 | ★★★☆☆ | http://arxiv.org/abs/2104.11984v1 | 音乐字幕/描述生成 |
| FMA: A Dataset For Music Analysis [67] | 2016 | arXiv | `> 待核实` | arXiv 预印本（arXiv:1612.01840v3） | 高——MIR 经典数据集 | ★★★★★ | http://arxiv.org/abs/1612.01840v3 | 音乐分析数据集基石 |

---

## 七、数据集、评测与开放问题

### 7.1 数据集与基准

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| MUSDB18 / MUSDB18-HQ | 2017–2019 | sigsep 社区 | `> 待核实` | 种子资源（官方数据集主页） | 高——分离标准集 | ★★★★★ | https://sigsep.github.io/datasets/musdb.html | 音源分离标准评测集；**本次未见 MUSDB18-HQ 上的最新 SOTA 数字** `> 待核实` |
| MTG-Jamendo | 2019– | MTG（UPF） | `> 待核实` | 种子资源（官方 GitHub） | 高 | ★★★★★ | https://github.com/MTG/mtg-jamendo-dataset | 标签/情绪/乐器标注 |
| Million Song Dataset / AcousticBrainz | 2011– | LabROSA / MTG | `> 待核实` | 种子资源（官网） | 高 | ★★★★☆ | http://millionsongdataset.com/ | 大规模 MIR 元数据（API 可用性 `> 待核实`） |
| Slakh2100 | 2019 | 多机构 | `> 待核实` | 种子资源（官网） | 中高 | ★★★★☆ | http://www.slakh.com/ | 合成多轨分离集 |
| FMA [67] | 2016 | arXiv | `> 待核实` | arXiv 预印本（arXiv:1612.01840v3） | 高 | ★★★★★ | http://arxiv.org/abs/1612.01840v3 | 音乐分析大规模数据集 |
| GlobalMood [1] | 2025 | arXiv | `> 待核实` | arXiv 预印本 cs.IR | 中 | ★★★★☆ | http://arxiv.org/abs/2505.09539v2 | 跨文化音乐情绪基准（直面西方中心偏差） |
| Sanidha（Carnatic）[62] | 2025 | arXiv | `> 待核实` | arXiv 预印本 | 中低 | ★★★☆☆ | http://arxiv.org/abs/2501.06959v1 | 南印度古典音乐工作室级多模态数据 |
| MOSA（音乐-运动语义标注）[69] | 2024 | arXiv | `> 待核实` | arXiv 预印本（arXiv:2406.06375v1） | 中 | ★★★☆☆ | http://arxiv.org/abs/2406.06375v1 | 跨模态音乐处理数据 |
| CultureMERT 多文化混合（Greek/Turkish/Indian，650h）[44] | 2025 | 论文自建 | `> 待核实` | 论文自述数据配方，非独立公开榜单 | 中 | ★★★☆☆ | http://arxiv.org/abs/2506.17818v1 | 跨文化适配训练数据；可复现性待核实 |
| Codec-SUPERB @ SLT 2024 [108] | 2024 | 多机构 | `> 待核实` | 与 SLT 2024 关联的基准论文 | 中高 | ★★★★★ | http://arxiv.org/abs/2409.14085v1 | 神经音频 codec 轻量统一基准 |

### 7.2 评测可信度
- **主观评测正在被制度化**：[79] AudioMOS 2025 首次把「合成音频主观质量 + 文本对齐」做成挑战赛；[64] 用人类偏好研究同时评估模型与指标。二者共同指向一个结论：**单看客观指标不足以判定生成质量** [64][79]。
- **挑战赛规模与代表性**：[47] 2025 AMT Challenge 仅 8 支有效提交、仅 2 支超过 MT3 baseline，说明该任务仍难，也说明榜单样本量小、外推需谨慎。
- **可比性**：codec 侧有 [108] 统一基准；分离侧本次未见统一榜单页（如音乐分离排行榜）→ `> 待核实`。
- **证据等级提示**：本报告绝大多数条目为 arXiv 预印本（B 级）；带 workshop 收录标注的仅 [47]；挑战赛获胜系统为团队自报（C 级）。**没有**任何本文引用条目提供第三方复现报告 → 所有「SOTA」表述均应加限定词。

### 7.3 开源项目（可复现性与维护）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| facebookresearch/audiocraft | 2022– | Meta | `> 待核实`（star 数未在证据中） | 种子资源（官方仓库） | 高 | ★★★★★ | https://github.com/facebookresearch/audiocraft | MusicGen / AudioGen 工具链 |
| facebookresearch/demucs | 2019– | Meta | `> 待核实` | 种子资源（官方仓库） | 高 | ★★★★★ | https://github.com/facebookresearch/demucs | SOTA 音源分离参考实现（HTDemucs 等版本细节 `> 待核实`） |
| deezer/spleeter | 2019– | Deezer | `> 待核实` | 种子资源（官方仓库） | 中高 | ★★★★☆ | https://github.com/deezer/spleeter | 经典分离基线，工程易用 |
| k2-fsa/k2 | 2020– | k2 社区 | `> 待核实` | 种子资源（官方仓库） | 中 | ★★★☆☆ | https://github.com/k2-fsa/k2 | 语音/音频建模工具链（与 MIR 相关性间接） |
| librosa/librosa | 2012– | librosa 社区 | `> 待核实` | 种子资源（官方仓库） | 高——MIR 事实标准工具 | ★★★★★ | https://github.com/librosa/librosa | MIR 特征与工具 |

> **待核实**：mert、musicgen 之外的 MuQ/CLAP/MusicFM 官方仓库、stable-audio-tools 的许可证与最近提交活跃度，本次证据块未包含 → 需补检索 GitHub 与 HuggingFace 页面后再填。

### 7.4 开放问题与争议
1. **审美主观性与评测口径**：人类偏好是金标准，但如何转成可复现指标仍未解决 [64][79]。
2. **跨文化/非西方音乐泛化**：两条独立来源均指出既有基准西方中心 [1][44]；Carnatic 等数据开始补齐 [62]。
3. **音乐基础模型 vs 通用语音 SSL 的系统对比缺失** [44][47][48] → `> 待核实`。
4. **任务难度被低估**：多乐器 AMT 在复调与音色变化下仍差 [47]。
5. **版权、训练数据合规与伦理**：[73] 讨论生成式音乐系统内嵌的意识形态；[74] 提出 AI 音乐系统中的公平性（谁的声音被听到）问题；[77] 系统检视 AI 音乐论文中伦理声明的有效性；[75] 以案例研究 AI 诱导的音乐风格；[95] 用 LLM 方法量化歌词中的性内容——共同构成「数据/内容合规」议题簇。
6. **榜单过拟合与 demo 混淆**：本次证据**未提供**任何直接的过拟合实证研究；该判断仅作为方法论警告列出 → `> 待核实`。
7. **检索噪声**：本次候选块包含多条与主题无关条目（短视频参与度预测 [20]、基础模型透明度指数 [21]、越南多模态法律问答 [112]、医学影像数据集 [68]、XAI 评测 [66] 等），已在报告中剔除，不计入结论。

---

## 八、建议关注清单（Watchlist）

1. **全曲生成的分层架构**：Hierarchical Autoregressive Planning + Flow-Matching Rendering [92]，以及 Song Form-aware 歌词生成 [91]、CSL-L2M [94]、SongPrep [96]——观察其是否公开权重与评测协议。
2. **可控性接口标准化**：MusiConGen（节奏/和弦）[84] 与 Instruct-MusicGen（指令编辑）[88] 是否会形成统一的条件表示。
3. **开放权重生成模型**：Stable Audio Open [76] 与 Stable Audio 3 [90] 的模型卡、许可证与数据来源披露。
4. **主观评测基础设施**：AudioMOS Challenge [79] 后续届次与人类偏好校准方法 [64]。
5. **音乐基础模型的跨文化适配**：CultureMERT [44] 的两阶段持续预训练配方能否被第三方复现；GlobalMood [1] 与 Sanidha [62] 能否成为标准评测集。
6. **分离架构与任务升级**：BS-RoFormer [98] / Mel-Band RoFormer [99] / Mel-RoFormer [110] 的开源实现，以及 Music Source Restoration [100] 这一新任务定义是否被社区采纳。
7. **codec 与下游复用**：Codec-SUPERB [108] 与 codec↔波形再合成差距分析 [109]；关注的应是「token 率 + 重建质量 + 下游生成/理解」三元权衡。
8. **零样本多语种 SVC**：FreeSVC [28]、Everyone-Can-Sing [29]、TCSinger 2 [26]，重点跟踪音高/音色泄漏的定量评测是否出现。
9. **伦理与合规**：[73][74][77][95] 是否催生可操作的训练数据披露与署名规范。

---

## 参考来源

[1] GlobalMood: A cross-cultural benchmark for music emotion recognition — http://arxiv.org/abs/2505.09539v2
[2] MIRFLEX: Music Information Retrieval Feature Library for Extraction — http://arxiv.org/abs/2411.00469v1
[3] Symbolic Music Representations for Classification Tasks: A Systematic Evaluation — http://arxiv.org/abs/2309.02567v2
[4] Barwise Music Structure Analysis with the Correlation Block-Matching Segmentation Algorithm — http://arxiv.org/abs/2311.18604v1
[5] Towards Multimodal MIR: Predicting individual differences from music-induced movement — http://arxiv.org/abs/2007.10695v1
[6] A Functional Taxonomy of Music Generation Systems — http://arxiv.org/abs/1812.04186v1
[7] Chord Recognition- Music and Audio Information Retrieval — http://arxiv.org/abs/2105.07019v2
[8] Knowledge Discovery in Optical Music Recognition: Enhancing Information Retrieval with Instance Segmentation — http://arxiv.org/abs/2408.15002v2
[9] Learning to Traverse Latent Spaces for Musical Score Inpainting — http://arxiv.org/abs/1907.01164v1
[10] Passage Summarization with Recurrent Models for Audio-Sheet Music Retrieval — http://arxiv.org/abs/2309.12111v1
[11] Music SketchNet: Controllable Music Generation via Factorized Representations of Pitch and Rhythm — http://arxiv.org/abs/2008.01291v1
[12] MusicLM: Generating Music From Text — http://arxiv.org/abs/2301.11325v1
[14] Diffusion-Based Audio Inpainting — http://arxiv.org/abs/2305.15266v3
[19] Unified Cross-modal Translation of Score Images, Symbolic Music, and Performance Audio — http://arxiv.org/abs/2505.12863v1
[20] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1
[21] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1
[22] ConSinger: Efficient High-Fidelity Singing Voice Generation with Minimal Steps — http://arxiv.org/abs/2410.15342v3
[23] NaturalSpeech 2: Latent Diffusion Models are Natural and Zero-Shot Speech and Singing Synthesizers — http://arxiv.org/abs/2304.09116v3
[24] Singing voice synthesis based on convolutional neural networks — http://arxiv.org/abs/1904.06868v2
[25] Fast and High-Quality Singing Voice Synthesis System based on Convolutional Neural Networks — http://arxiv.org/abs/1910.11690v2
[26] TCSinger 2: Customizable Multilingual Zero-shot Singing Voice Synthesis — http://arxiv.org/abs/2505.14910v3
[27] Towards Improved Zero-shot Voice Conversion with Conditional DSVAE — http://arxiv.org/abs/2205.05227v2
[28] FreeSVC: Towards Zero-shot Multilingual Singing Voice Conversion — http://arxiv.org/abs/2501.05586v1
[29] Everyone-Can-Sing: Zero-Shot Singing Voice Synthesis and Conversion with Speech Reference — http://arxiv.org/abs/2501.13870v1
[36] Learning a Representation for Cover Song Identification Using Convolutional Neural Network — http://arxiv.org/abs/1911.00334v1
[37] ByteCover: Cover Song Identification via Multi-Loss Training — http://arxiv.org/abs/2010.14022v2
[38] Large-Scale Cover Song Detection in Digital Music Libraries Using Metadata, Lyrics and Audio Features — http://arxiv.org/abs/1808.10351v1
[39] CoverHunter: Cover Song Identification with Refined Attention and Alignments — http://arxiv.org/abs/2306.09025v1
[44] CultureMERT: Continual Pre-Training for Cross-Cultural Music Representation Learning — http://arxiv.org/abs/2506.17818v1
[45] The IEEE-IS2 2024 Music Packet Loss Concealment Challenge — http://arxiv.org/abs/2409.18564v1
[46] Joint Music and Language Attention Models for Zero-shot Music Tagging — http://arxiv.org/abs/2310.10159v1
[47] Advancing Multi-Instrument Music Transcription: Results from the 2025 AMT Challenge — http://arxiv.org/abs/2603.27528v1
[48] ASTAR-NTU solution to AudioMOS Challenge 2025 Track1 — http://arxiv.org/abs/2507.09904v1
[54] Semi-Supervised Contrastive Learning of Musical Representations — http://arxiv.org/abs/2407.13840v1
[61] Music Foundation Model as Generic Booster for Music Downstream Tasks — http://arxiv.org/abs/2411.01135v3
[62] Sanidha: A Studio Quality Multi-Modal Dataset for Carnatic Music — http://arxiv.org/abs/2501.06959v1
[63] Vision-to-Music Generation: A Survey — http://arxiv.org/abs/2503.21254v1
[64] Benchmarking Music Generation Models and Metrics via Human Preference Studies — http://arxiv.org/abs/2506.19085v1
[66] Are explainable AI (XAI) evaluation strategies aligned? — http://arxiv.org/abs/2504.17023v2
[67] FMA: A Dataset For Music Analysis — http://arxiv.org/abs/1612.01840v3
[68] The RSNA Abdominal Traumatic Injury CT (RATIC) Dataset — http://arxiv.org/abs/2405.19595v1
[69] MOSA: Music Motion with Semantic Annotation Dataset for Cross-Modal Music Processing — http://arxiv.org/abs/2406.06375v1
[70] Improving Choral Music Separation through Expressive Synthesized Data from Sampled Instruments — http://arxiv.org/abs/2209.02871v1
[73] Opening Musical Creativity? Embedded Ideologies in Generative-AI Music Systems — http://arxiv.org/abs/2508.08805v1
[74] Who Gets Heard? Rethinking Fairness in AI for Music Systems — http://arxiv.org/abs/2511.05953v1
[75] "Melatonin": A Case Study on AI-induced Musical Style — http://arxiv.org/abs/2208.08968v1
[76] Stable Audio Open — http://arxiv.org/abs/2407.14358v2
[77] Ethics Statements in AI Music Papers: The Effective and the Ineffective — http://arxiv.org/abs/2509.25496v1
[79] The AudioMOS Challenge 2025 — http://arxiv.org/abs/2509.01336v1
[80] Instrumental Text-to-Music Generation with Auxiliary Conditioning Branches — http://arxiv.org/abs/2605.21433v1
[82] UT-AISTimprt submission for ICME 2026 Grand Challenge on Academic Text-to-Music Generation — http://arxiv.org/abs/2607.01669v1
[83] Story2MIDI: Emotionally Aligned Music Generation from Text — http://arxiv.org/abs/2512.02192v1
[84] MusiConGen: Rhythm and Chord Control for Transformer-Based Text-to-Music Generation — http://arxiv.org/abs/2407.15060v1
[85] Baseline Systems For The 2025 Low-Resource Audio Codec Challenge — http://arxiv.org/abs/2510.00264v3
[86] ICAGC 2024: Inspirational and Convincing Audio Generation Challenge 2024 — http://arxiv.org/abs/2407.12038v2
[87] Challenge on Sound Scene Synthesis: Evaluating Text-to-A

---

*Generated by research-bot · topic=`music-audio` · depth=`standard` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading · model=`deepseek-v4-flash` · sources=112 · duration=387s · 2026-10-04T22:53:14+00:00*
