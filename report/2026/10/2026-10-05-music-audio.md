# 音乐与音频算法调研报告：MIR / 生成 / 理解 / 分离

> **日期**：2026-10-05（UTC）
> **领域**：Music & Audio —— 音乐信息检索（Music Information Retrieval, MIR）、音乐生成（Music Generation）、音乐理解（Music Understanding）、歌声转换（Singing Voice Conversion, SVC）、音源分离（Music Source Separation, MSS）、神经音频编解码（Neural Audio Codec）、自监督音频表征（Self-Supervised Audio Representation）
> **检索源规模**：可核查引用 112 条编号来源 [1]–[112]；另有 12 条领域种子资源（论文 3 / 开源项目 5 / 数据集 4，含直链，标注为「种子」）
> **证据纪律**：本报告只引用 [1]–[112] 中真实存在的编号，不引用未出现在来源清单中的编号；种子资源链接单独标注为「种子」；凡引用数（citations）、GitHub star、下载量、榜单排名等热度信号在候选证据中缺失的，一律写 `> 待核实`，不编造数字。
> **重要限定**：本次抽取到的一手证据**绝大多数为 arXiv 标题与摘要片段（confidence=low）**，缺少实验表格、指标数值与算力配置。因此本报告在「范式判断」层面结论较强，在「具体数字对比」层面大量标注 `> 待核实`。此外，候选证据中存在明显检索噪声（[21] 短视频参与度预测、[49] 基础模型透明度指数、[51] 图像超分辨率、[52] 越南语法律问答、[73] 遥感数据增强、[77] 通用 critique RL、[90] 医学 CT、[93] 短视频超分），本报告已将其排除出音乐相关论断，仅在缺口说明中提及。

---

## 摘要（Executive Summary）

1. **本方向近两年最确定的变化是「评估」而非「生成」**：2025 年前后集中出现了多个独立基准与挑战——合成音频自动主观质量预测（AudioMOS Challenge 2025，含专门的 text-to-music track）[50]、文本到音乐情感传达评测基准（AImoclips）[63]、人类撰写的音乐理解问答基准（HumMusQA）[92]、多乐器自动转谱挑战（AMT Challenge 2025）[88]、音乐解混挑战（Sound Demixing Challenge 2023 Music Demixing Track）[100]、神经音频编解码轻量基准（Codec-SUPERB）[108] 与低资源音频编解码挑战基线（LRAC 2025）[105]。这说明该领域正从「能生成」转向「可量化、可复现地比较」。

2. **跨文化与去西方中心成为显性议题**：ISMIR 首个 25 年作者群文献计量分析 [32]、跨文化音乐情绪识别基准 GlobalMood [25]、跨文化音乐表征持续预训练 CultureMERT [36] 三条独立证据同时出现，构成一个可交叉验证的趋势信号。

3. **零样本 / 多语言歌唱合成与转换是工程最活跃的分支**：TCSinger 2（可定制多语言零样本 SVS）[8]、FreeSVC（零样本多语言歌声转换）[10]、LDM-SVC（潜扩散零样本 any-to-any SVC + 歌手引导）[16]、Poly-SVC（复音感知 SVC）[15]、SPA-SVC（自监督音高增强）[13]、LHQ-SVC（轻量高质量 SVC）[14] 构成密集谱系。但候选证据未提供任何一条的统一指标对比表，**各方法之间的真实强弱 `> 待核实`**。

4. **音源分离的架构主线已从时域卷积转向 Band-Split + RoPE Transformer**：Band-Split RoPE Transformer（BS-RoFormer）[84] 成为新一代骨干；2026 年进一步出现「音乐源修复（Music Source Restoration, MSR）」这一新任务定义，处理母带处理与分发伪影导致的非线性和混假设失效 [85]。经典时域端到端路线由 [82] 开启，[91] 用 Slakh 系统研究了训练数据质量与数量的影响。

5. **神经音频编解码从「压缩」走向「可解释 + 评测 + 安全」**：Codec-SUPERB 提供轻量基准 [108]，可解释性工作尝试为声学 token 赋予语义 [112]，低资源场景出现专门挑战 [105]，另有工作揭示有损压缩可被复用为天然后门攻击载体 [83]。

6. **版权、反学习（unlearning）与伦理治理已进入技术论文正文**：No Encore 提出以「反学习」作为音乐生成中的 opt-out 机制 [71]；有工作系统评估 AI 音乐论文伦理声明的有效性 [72]；另有从信息论与模型权重角度讨论训练数据与版权法关系的研究 [70]。

7. **最大缺口**：候选证据**未覆盖**统一音乐语言模型、音频 tokenizer 作为音乐生成/理解枢纽的系统对比、自回归 vs 扩散 vs 流匹配（flow matching）三条路线在音乐上的直接对照、以及任何模型的具体硬件（GPU 型号/算力）验证。**自监督音频表征的 wav2vec / HuBERT / CLMR / MERT 一脉在候选证据中几乎完全缺位**，仅有下游适配工作 CultureMERT [36] 间接出现。相关谱系梳理 `> 待核实`。

---

## 一、关键前沿进展（近 1–2 年）

### 1.1 评估与基准的「建制化」（最扎实的趋势）

- **AudioMOS Challenge 2025** 被描述为「首个针对合成音频自动主观质量预测的挑战」，设三个 track：Track 1 评估 text-to-music 的整体质量与文本对齐；Track 2 基于 Meta Audiobox Aesthetics 的四维度、测试集混入 text-to-speech / text-to-audio / text-to-music 样本；Track 3 关注不同采样率下合成语音质量。共 24 支学术界与工业界团队参加，且确认相对基线有提升 [50]。另有一份针对 Track 1 的参赛系统技术报告 [66]。
  - 热度：`> 待核实`（候选证据未给出引用数或 star）
  - 权威：IEEE ASRU 2025，同行评审会议论文 [50]
  - 关注度：**中** —— 首个合成音频主观质量预测挑战，24 支团队参与 [50]
  - 推荐度：**★★★★☆** —— 目前与「音乐生成基准与评估」最直接相关的同行评审来源 [50]

- **AImoclips** 是评估 text-to-music 生成中**情感传达**的基准 [63]；**HumMusQA** 是针对大音频语言模型（Large Audio-Language Models, LALMs）音乐理解能力的人类撰写问答基准，明确指出当前数据方法学常无法真正测试模型是否「感知并解释」音乐 [92]。二者共同指向同一件事：**生成质量与理解能力的评测正在从「像不像」拆分为可分解维度**。
  - 权威：均为 arXiv 预印本（cs.SD / cs.CL）[63][92]，未见明确的同行评审 venue
  - 关注度：**低至中** —— 候选证据无引用/star 信号 [63][92]
  - 推荐度：**★★★☆☆** —— 基准设计思路可引用，但基准本身的采纳度 `> 待核实` [63][92]

- **AMT Challenge 2025**：多乐器自动转谱在线竞赛，8 支队伍提交有效方案，其中 2 支超过基线 MT3 模型 [88]。
  - 权威：arXiv 预印本，挑战总结报告 [88]
  - 关注度：**中** —— 有明确参赛队伍数与基线超越结论 [88]
  - 推荐度：**★★★★☆** —— 提供了「多乐器转谱」这一任务的可比进度快照 [88]

- **Sound Demixing Challenge 2023（Music Demixing Track）** 及冠军系统技术报告 **TFC-TDF-UNet v3** [100][102] 仍是音乐解混领域被广泛引用的竞赛基准与强基线。
  - 权威：挑战报告 + 系统技术报告 [100][102]
  - 关注度：**中** —— 挑战赛体系的持续影响力 [100]
  - 推荐度：**★★★★☆** —— 若要复现/对比 MDX 类分离系统，这是绕不开的锚点 [100][102]

### 1.2 跨文化与去西方中心

- **ISMIR 25 年作者群文献计量分析**：直接追问「谁被代表、谁没有」，指出西方视角塑造了 MIR 研究议程 [32]。**citations=5**，发表于 *Transactions of the International Society for Music Information Retrieval*（同行评审期刊）。
  - 关注度：**中** —— citations=5 [32]
  - 推荐度：**★★★★☆** —— 社区自省的权威量化证据，适合用于论证数据集与评测的文化偏差 [32]

- **GlobalMood** 提出跨文化音乐情绪识别基准，指出已有数据集以西方歌曲与英语情绪词为主，限制跨语言文化泛化 [25]。
  - 权威：arXiv 预印本（cs.IR）[25]
  - 关注度：**低** —— 无热度信号 [25]
  - 推荐度：**★★★★☆** —— 与「情绪识别 + 跨文化」子问题直接相关 [25]

- **CultureMERT** 提出 **CultureMERT-95M**，通过持续预训练把音乐基础模型适配到多文化音乐传统，明确指出「现有音乐基础模型的跨音乐传统有效性仍然有限」[36]。
  - 权威：arXiv 预印本（cs.SD）[36]
  - 关注度：**低** —— 无热度信号 [36]
  - 推荐度：**★★★★☆** —— 是「音乐基础模型 + 跨文化适配」目前可见的少数具体方案 [36]

### 1.3 版权、反学习与治理

- **No Encore: Unlearning as Opt-Out in Music Generation** 提出把「反学习」作为版权方 opt-out 的技术机制，并给出初步结果，明确指向 AI 音乐生成对受版权保护创作的使用风险 [71]。
  - 权威：arXiv 预印本（cs.CL）[71]
  - 关注度：**低至中** —— 无引用/star 信号，但议题属社区热点领域 [71]
  - 推荐度：**★★★★☆** —— 「opt-out 技术化」是政策与算法交叉的关键切口 [71]

- **Ethics Statements in AI Music Papers: The Effective and the Ineffective** 直接评估 AI 音乐论文中伦理声明的实效性，指出研究者对伦理后果的参与度落后于研究规模与影响 [72]。
  - 权威：arXiv 预印本（cs.CY）[72]
  - 关注度：**低** —— 无热度信号 [72]
  - 推荐度：**★★★☆☆** —— 元研究性质，适合用于治理章节 [72]

- **Training Foundation Models as Data Compression: On Information, Model Weights and Copyright Law** 从信息论/模型权重视角讨论训练数据与版权法的关系 [70]。
  - 权威：arXiv 预印本 [70]
  - 关注度：`> 待核实`
  - 推荐度：**★★★☆☆** —— 提供版权论证的技术-法律桥梁，但非音乐专论 [70]

### 1.4 评测方法论自身的反思

- **Position: Evaluation Scores Are Perishable Knowledge Claims** 主张评测分数是「会过期的知识主张」[74]；**(Towards) Scalable Reliable Automated Evaluation with LLMs** 讨论 LLM 自动评测的可靠性 [75]；**Reproducible Subjective Evaluation** 提出主观评测的可复现框架 [81]。三者共同回应了「榜单刷分」与「主观指标不可复现」这两个争议。
  - 权威：均为 arXiv 预印本/立场论文 [74][75][81]
  - 关注度：**低** —— 无热度信号
  - 推荐度：**★★★☆☆** —— 为第七章「指标可信度」提供方法论弹药，但需注意 [74][75] 并非音乐领域专论

### 1.5 检索噪声提示

以下候选来源经核实与音乐/音频无关，已排除：短视频参与度预测 [21]、图像超分辨率挑战 [51]、越南语多模态法律问答 [52]、基础模型透明度指数 [49]、遥感布局生成 [73]、通用 critique 强化学习 [77]、医学 CT 数据集 [90]、短视频超分数据集 [93]。**这也提示：本主题的检索召回仍存在明显污染，需在后续轮次收紧查询词。**

---

## 二、音乐信息检索（MIR / 翻唱识别 CSI / 节拍与和声）

### 2.1 综述与谱系

- **Natural Language Processing Methods for Symbolic Music Generation and Information Retrieval: A Survey**：把符号音乐视为符号序列，系统梳理 NLP 方法在符号音乐生成与检索中的迁移。发表 **ACM Computing Surveys**，**citations=51** [41]。
  - 权威：ACM Computing Surveys（同行评审顶级综述期刊）[41]
  - 关注度：**高** —— citations=51 [41]
  - 推荐度：**★★★★★** —— 目前候选证据中权威度与热度最高的音乐+语言交叉综述，建议作为符号音乐方向的入门骨架 [41]

- **A Functional Taxonomy of Music Generation Systems**：为音乐生成系统提供功能性分类法 [27]。属早期分类框架，适合作为「方法演进」章节的对照基线。
  - 权威：arXiv 预印本 [27]
  - 关注度：`> 待核实`
  - 推荐度：**★★★★☆** —— 分类学框架经典，可作为 taxonomy 骨架 [27]

- **Symbolic Music Representations for Classification Tasks: A Systematic Evaluation**：指出符号音乐既不是图像也不是句子，系统评估了类图像/类语言编码在分类任务上的表现 [26]。
  - 权威：arXiv 预印本（eess.AS）[26]
  - 关注度：**低** —— 无热度信号
  - 推荐度：**★★★★☆** —— 「表征选择」这一常见工程盲区的系统证据 [26]

### 2.2 表征、特征与结构

- **MIRFLEX**：MIR 特征提取库 [28]。
- **musif**：符号音乐特征提取 Python 包 [103]。
- **Barwise Music Structure Analysis with the Correlation Block-Matching Segmentation Algorithm**：音乐结构分析的分段算法 [29]。
- **Towards Multimodal MIR: Predicting individual differences from music-induced movement**：从音乐诱发动作预测个体差异，代表 MIR 的多模态扩展 [30]。
  - 上述四条权威度均为 arXiv 预印本/工具论文，**热度信号均 `> 待核实`** [28][29][30][103]
  - 推荐度：**★★★☆☆** —— 作为工程栈与任务扩展线索可用，但均为候选证据摘要级信息，未读到实验细节 [28][29][30][103]

- **Modelling Emotion Dynamics in Song Lyrics with State Space Models**：用状态空间模型建模歌词中的情绪动态 [6]，属于「歌词侧」情感建模，与「音频侧」情绪识别 [25] 互补。
  - 权威：arXiv 预印本 [6]
  - 关注度：`> 待核实`
  - 推荐度：**★★★☆☆** —— 情绪动态建模的具体技术路线 [6]

### 2.3 翻唱识别（Cover Song Identification, CSI）

- **Learning a Representation for Cover Song Identification Using Convolutional Neural Network**：用 CNN 学习翻唱识别的表征 [4]。
- **Large-Scale Cover Song Detection in Digital Music Libraries Using Metadata, Lyrics and Audio Features**：在大规模数字音乐库中结合元数据、歌词与音频特征做翻唱检测 [5]。
  - 权威：均为 arXiv 预印本 [4][5]，**未标注同行评审 venue**
  - 关注度：**低** —— 候选证据未提供引用数或 star，**且未见 2024–2026 年的 CSI 新工作**
  - 推荐度：**★★★☆☆** —— 作为经典方法线索可引用，但**近两年 CSI 是否出现零样本/少样本新范式，候选证据完全无法支撑，`> 待核实`** [4][5]

> **缺口警告（q3 相关）**：子问题 q3 明确询问「翻唱识别在零样本/少样本设定下的最新方法」，但候选证据中 CSI 仅命中 2018/2019 年的两条 [4][5]，**没有任何 2024–2026 年 CSI 新方法、开源实现（如 CoverHunter 一脉）或评测口径证据**。此为该子问题的**重大证据缺口**，必须补充检索后才能下判断。

### 2.4 社区与会议生态

ISMIR 系列会议论文集/报告构成该领域主要发表场所：ISMIR 2022 报告 [39]、ISMIR 2023 论文集 [43]、ISMIR 2024 论文集 [35]、ISMIR 2025 论文集 [34]，以及 Human-Centric MIR 2023 工作坊 [45]。
  - 权威：国际会议论文集（同行评审）[34][35][39][43][45]
  - 关注度：**中** —— ISMIR 为 MIR 领域首要会议
  - 推荐度：**★★★★☆** —— 追踪 MIR 前沿的一手会议入口 [34][35]

---

## 三、音乐生成（文本 / 符号 / 音频）

### 3.1 符号音乐生成

- **Music Transformer**：使用相对位置表示的长程音乐生成 Transformer，是符号音乐生成的奠基性架构 [53]。
- **Music SketchNet**：通过音高与节奏的因子化表示实现可控音乐生成 [31]。
- **Improving Polyphonic Music Models with Feature-Rich Encoding**：以特征丰富编码改进复音音乐模型 [61]。
- **Diffusion-based Symbolic Music Generation with Structured State Space Models**：把扩散模型与结构化状态空间模型（SSM）结合用于符号音乐生成 [57]。
- **Generating Piano Music with Transformers: A Comparative Study of Scale, Data, and Metrics**：对 Transformer 钢琴音乐生成做规模、数据与指标的对比研究 [59]，直接回应「提升来自数据还是架构」这一关键追问。
- **Learning to Traverse Latent Spaces for Musical Score Inpainting**：乐谱补全的潜空间遍历方法 [33]。
  - 权威：均为 arXiv 预印本；[53] 为经典架构论文 [53][57][59][61][33][31]
  - 关注度：**低** —— 候选证据均无引用数/star 信号，`> 待核实` [57][59][61]
  - 推荐度：**★★★★☆（[53]）** / **★★★☆☆（其余）** —— [53] 为必读奠基；[57][59] 分别代表扩散+SSM 与「规模-数据-指标」归因研究，方向价值高但需自行核验实验 [53][57][59][61]

### 3.2 文本到音乐（Text-to-Music）

- **Story2MIDI: Emotionally Aligned Music Generation from Text**：sequence-to-sequence Transformer，从文本生成情感对齐的 MIDI；关键贡献是**数据构建**——合并文本情感分析数据集与音乐情感分类数据集，得到「唤起相同情感的文本片段—音乐片段」配对 [54]。
  - 权威：arXiv 预印本（cs.SD，2025-12）[54]，**未标注会议**
  - 关注度：**低** —— 候选块无引用/star/榜单信号 [54]
  - 推荐度：**★★★☆☆** —— 提供「文本情感—音乐情感」对齐的具体建模与数据路线，但为预印本且缺实验数字 [54]

- **Instrumental Text-to-Music Generation with Auxiliary Conditioning Branches** [55]、**UT-AIST imprt submission for ICME 2026 Grand Challenge on Academic Text-to-Music Generation** [56]：分别指向「辅助条件分支」与「ICME 2026 学术文本到音乐生成挑战」。
  - 权威：arXiv 预印本；[56] 为挑战参赛系统报告 [55][56]
  - 关注度：**低至中** —— [56] 背后有 ICME 2026 Grand Challenge 这一竞赛场景 [56]
  - 推荐度：**★★★☆☆** —— [56] 是观察「学术文本到音乐生成」竞赛口径的直接窗口 [55][56]

- **Vision-to-Music Generation: A Survey**：把「视觉到音乐」作为独立生成方向做综述 [60]，说明文本之外的条件模态正在扩张。
  - 权威：arXiv 综述 [60]
  - 关注度：**低** —— 无热度信号
  - 推荐度：**★★★☆☆** —— 拓展条件模态视野，但综述时效与覆盖度 `> 待核实` [60]

### 3.3 生成评估（本节为全文最强证据）

- **AudioMOS Challenge 2025**：见 1.1 节详述 [50][66]。这是目前唯一有明确「首个挑战 + 24 支团队 + 相对基线提升」三重可核查描述的生成评估来源 [50]。
- **AImoclips**：专测 text-to-music 的**情感传达**能力 [63]，与 Story2MIDI 的「情感对齐生成」[54] 形成「生成目标 ↔ 评估维度」的对应闭环。
  - 推荐度：**★★★★☆** —— 生成与评估两端都有证据，闭环可讲通 [50][63]

### 3.4 明确缺位

> 子问题 q1 询问的以下内容在候选证据中**完全无覆盖**：
> - 统一音乐语言模型（unified music language model）的架构、训练目标与评测 —— `> 待核实`
> - 音频 tokenizer 在音乐生成中的代表工作与作用 —— `> 待核实`
> - 自回归 vs 扩散 vs 流匹配（flow matching）三条路线在音乐生成上的直接对比 —— `> 待核实`
> - 任一音乐生成模型的硬件（GPU 型号、训练/推理算力）验证 —— `> 待核实`
>
> 因此**本报告不对上述范式作任何技术结论**。

---

## 四、音乐理解与自监督音频表征

### 4.1 音乐理解与评测

- **HumMusQA**：面向大音频语言模型（LALMs）的人类撰写音乐理解问答基准，明确批评现有数据方法学「频繁无法满足真正测试模型是否感知与解释音乐的标准」[92]。
  - 权威：arXiv 预印本（cs.CL）[92]
  - 关注度：**低** —— 无热度信号
  - 推荐度：**★★★★☆** —— 音乐理解评测的关键切口，尤其适合检验 LALM 的「真理解 vs 表面匹配」[92]

- **MARBLE: Music Audio Representation Benchmark for Universal Evaluation**：音乐音频表征的通用评测基准 [95]，是评估音乐自监督/基础模型表征的标准枢纽之一。
  - 权威：arXiv 预印本 [95]
  - 关注度：`> 待核实`
  - 推荐度：**★★★★★** —— 若要做音乐表征评测，这是最直接可用的基准候选，但采纳度与版本需自行核验 [95]

- **LP-MusicCaps: LLM-Based Pseudo Music Captioning**：用 LLM 生成伪音乐描述，解决音乐-文本配对数据稀缺问题 [96]。是当前「音乐描述 / 音乐-语言对齐」的数据侧基础设施。
  - 权威：arXiv 预印本 [96]
  - 关注度：`> 待核实`
  - 推荐度：**★★★★☆** —— 音乐-语言数据构造的关键思路 [96]

### 4.2 音乐基础模型与跨文化适配

- **CultureMERT-95M**：通过对音乐基础模型做持续预训练，增强跨文化音乐表征学习，明确指出既有音乐基础模型在不同音乐传统上有效性有限 [36]。
  - 权威：arXiv 预印本（cs.SD）[36]
  - 关注度：**低** —— 无热度信号 [36]
  - 推荐度：**★★★★☆** —— 「基础模型 + 跨文化持续预训练」的少见具体方案 [36]

### 4.3 自监督音频表征谱系：**重大缺位**

> 子问题 q2 明确要求梳理 **wav2vec / HuBERT / CLMR / MERT 一脉** 的自监督预训练谱系及其如何构成今日技术谱系。候选证据中：
> - **wav2vec、HuBERT、CLMR、MERT 均未作为独立来源出现**；
> - 只有 CultureMERT [36] 作为「MERT 系的下游适配」间接暗示该谱系存在；
> - 另有若干通用自监督方法论文（[38][42][44][47][48]）与 **音乐无关**（分别涉及辅助自监督 pretext 任务、交互环境自监督、半监督学习、图像聚类、天文图像表征），**不可用于支撑音乐自监督谱系**。
>
> **结论：本报告无法给出音乐自监督表征的谱系梳理，该部分整体标注 `> 待核实`，必须补充检索（建议查询词：`MERT music understanding self-supervised`、`CLMR contrastive learning music representation`、`music foundation model survey 2025`）后才可下笔。**

### 4.4 情感与跨文化理解

- **GlobalMood** [25] 与 **CultureMERT** [36] 共同支撑「音乐情绪识别存在西方中心偏差」这一判断；**ISMIR 作者群分析** [32] 从社区结构侧提供旁证。
  - 交叉验证：三条独立来源指向同一问题，**该判断可视为中等强度共识** [25][32][36]
  - 关注度：**中** —— [32] citations=5，为唯一可量化热度信号

---

## 五、歌声转换（SVC）与音源分离

### 5.1 歌声合成与转换（SVS / SVC）

**经典/早期 SVS：**
- **Singing voice synthesis based on convolutional neural networks**（2019）：CNN 用于歌声合成，改善 DNN 系统在声学特征关系建模上的不足 [1]。
- **Fast and High-Quality Singing Voice Synthesis System based on Convolutional Neural Networks**（2019）：强调速度与质量兼顾的 CNN SVS [3]。
  - 权威：arXiv 预印本（eess.AS）[1][3]
  - 关注度：**低** —— 无热度信号
  - 推荐度：**★★★☆☆** —— 作为 CNN-SVS 谱系起点引用 [1][3]

**扩散/零样本路线：**
- **NaturalSpeech 2**：潜扩散模型实现零样本语音与**歌声**合成 [7]。
- **ConSinger**（2024）：以最少步数实现高效高保真歌声生成，明确针对扩散模型「牺牲推理速度换质量」的问题 [2]。
- **TCSinger 2**（2025）：可定制多语言**零样本**歌声合成，指出既有 SVS 模型过度依赖音素与音符边界标注，导致零样本鲁棒性差 [8]。
- **LDM-SVC**：基于潜扩散模型的零样本 any-to-any 歌声转换，带歌手引导 [16]。
  - 权威：均为 arXiv 预印本（[2] cs.SD；[7] arXiv；[8] eess.AS）[2][7][8][16]
  - 关注度：**低** —— 候选证据均无引用数/star/榜单信号，`> 待核实`
  - 推荐度：**★★★★☆** —— [8] 与 [16] 分别代表零样本 SVS 与零样本 SVC 的当前公开路线；[2] 针对推理效率的工程切口清晰 [2][8][16]

**轻量/增强/复音路线：**
- **FreeSVC**：零样本多语言歌声转换 [10]。
- **Zero-Shot Sing Voice Conversion: built upon clustering-based phoneme representations**：用聚类音素表征做零样本歌声转换 [11]。
- **SPA-SVC: Self-supervised Pitch Augmentation for Singing Voice Conversion**：自监督音高增强 [13]。
- **LHQ-SVC: Lightweight and High Quality Singing Voice Conversion Modeling**：轻量高质量 SVC [14]。
- **Poly-SVC: Polyphony-Aware Singing Voice Conversion with Harmonic Modeling**：复音感知 SVC + 谐波建模，明确指出**现有方法都无法从伴奏中可靠提取干净人声**，因此多数 SVC 依赖 F0 提取器从干净人声中取主旋律 [15]。
- **Towards Improved Zero-shot Voice Conversion with Conditional DSVAE**：条件 DSVAE 改进零样本语音转换 [9]（语音而非歌声，作为方法迁移来源）。
  - 权威：均为 arXiv 预印本 [9][10][11][13][14][15]
  - 关注度：**低** —— 候选证据均无热度信号，`> 待核实`
  - 推荐度：**★★★★☆（[15]）** / **★★★☆☆（其余）** —— [15] 准确指出了「伴奏下提取干净人声」这一被普遍回避的工程痛点；[14] 面向轻量部署，工程相关性强 [14][15]

**⚠️ 术语冲突警告：**
> [12] 标题为 "SVC 2025: the First Multimodal Deception Detection Challenge"，其 SVC 指**欺骗检测（Deception Detection）**，属 cs.CV，**与 Singing Voice Conversion 完全无关**。这是一条典型的同缩写检索污染，**不得作为歌声转换证据引用**。同理 [12] 也不应出现在任何 SVC 谱系表中。

> **SVC 复现性与评测口径缺口**：子问题 q3 要求核验「so-vits-svc、RVC、Seed-VC、CoverHunter 一脉开源实现的可复现性与评测口径」。候选证据中**这些开源仓库一个都没有出现**（无 GitHub 链接、无 star 数据、无许可协议信息），**评测口径（MCD、F0 RMSE、主观 MOS、说话人相似度等指标）也无任何证据**。该部分整体 `> 待核实`。

### 5.2 音源分离（Music Source Separation）

- **End-to-end music source separation: is it possible in the waveform domain?**（2018）：挑战「幅度谱输入默认丢弃相位」的行业惯例，研究波形域端到端分离的可行性 [82]。这是时域分离路线的奠基性追问。
  - 权威：arXiv 预印本（cs.SD）[82]
  - 关注度：**低** —— 候选证据无热度信号
  - 推荐度：**★★★★★** —— 作为「为何走向时域/波形域」的论证起点必引 [82]

- **Music Source Separation with Band-Split RoPE Transformer（BS-RoFormer）**：引入频带切分（band-split）+ RoPE Transformer 骨干 [84]，是当前分离架构主线。
  - 权威：arXiv 预印本 [84]
  - 关注度：`> 待核实`
  - 推荐度：**★★★★★** —— 现代 SOTA 骨干，工程选型优先级高 [84]

- **Multi-Stage Music Source Restoration with BandSplit-RoFormer Separation and HiFi++ GAN**（2026）：定义 **Music Source Restoration (MSR)** 任务——从完全混音与母带处理后的音频中恢复原始未处理分轨，指出制作效果与分发伪影**破坏了常见的线性混音假设**；系统由 BandSplit-RoFormer 分离 + HiFi++ GAN 组成 [85]。
  - 权威：arXiv 技术报告（cs.SD），ICASSP Challenge 参赛系统 [85]
  - 关注度：**中** —— 竞赛背景，但无引用/star 信号
  - 推荐度：**★★★★★** —— **本报告中最具"新任务定义"价值的一条**：它把评估从"分离得多准"推进到"能否逆转母带处理"，是评估口径级别的变化 [85]

- **The Whole Is Greater than the Sum of Its Parts: Improving Music Source Separation by Bridging Network** [86]、**Audio query-based music source separation** [87]、**Improving Choral Music Separation through Expressive Synthesized Data from Sampled Instruments** [68]：分别代表网络桥接集成、查询驱动分离、合唱分离的合成数据增强。
  - 权威：arXiv 预印本 [68][86][87]
  - 关注度：**低** —— 无热度信号
  - 推荐度：**★★★☆☆** —— [68] 的「用采样乐器合成数据补数据」思路对数据稀缺场景有直接借鉴价值 [68][86][87]

- **Exploiting Music Source Separation for Automatic Lyrics Transcription with Whisper**（2025）：用分离前端提升基于 Whisper 的自动歌词转写，指出 ALT 的核心难点之一是伴奏的高幅度干扰 [99]。
  - 权威：arXiv 预印本（cs.SD）[99]
  - 关注度：**低** —— 无热度信号
  - 推荐度：**★★★★☆** —— 「分离即前端」的典型级联系统，任务耦合关系清晰 [99]

- **Slakh2100 数据集**：系统研究训练数据质量与数量对分离的影响 [91]。
  - 权威：arXiv 预印本（含数据集）[91]
  - 关注度：`> 待核实`
  - 推荐度：**★★★★☆** —— 合成多轨数据用于研究数据规模效应的标准参考 [91]

### 5.3 神经音频编解码（Neural Audio Codec）

- **SoundStream: An End-to-End Neural Audio Codec**：端到端神经音频编解码的奠基工作 [107]。
- **HiFi-Codec: Group-residual Vector quantization for High Fidelity Audio Codec**：分组残差矢量量化提升音质 [106]。
- **APCodec: A Neural Audio Codec with Parallel Amplitude and Phase Spectrum Encoding and Decoding**：并行幅度与相位谱编解码 [109]。
- **A Closer Look at Neural Codec Resynthesis: Bridging the Gap between Codec and Waveform Generation**：研究编解码与波形生成之间的鸿沟 [110]。
- **Codec-SUPERB @ SLT 2024**：神经音频编解码的轻量基准 [108]。
- **Baseline Systems For The 2025 Low-Resource Audio Codec Challenge (LRAC)**：面向资源受限环境的神经音频编码，必须在日常噪声与混响下稳定工作并满足严格约束 [105]。
- **Bringing Interpretability to Neural Audio Codecs**：指出声学 token（acoustic units）相对语义 token 可能缺乏可解释性，并尝试引入可解释性 [112]。
- **ICAGC 2024: Inspirational and Convincing Audio Generation Challenge 2024**：音频生成挑战 [111]。
- **Everyone Can Attack: Repurpose Lossy Compression as a Natural Backdoor Attack**：揭示有损压缩可被复用为天然后门载体 [83]——对依赖有损编解码的音频流水线构成安全警示。
  - 权威：均为 arXiv 预印本；[108] 为 SLT 2024 关联基准 [83][105][106][107][108][109][110][111][112]
  - 关注度：**低至中** —— 候选证据均无引用/star 信号；[105][108] 因挑战/基准属性略高
  - 推荐度：**★★★★★（[107]）** / **★★★★☆（[105][108][112]）** / **★★★☆☆（其余）** —— [107] 是必读奠基；[108] 提供统一评测口径；[112] 直击"token 语义化"这一音乐生成/理解共同瓶颈 [107][108][112]

> **指标口径缺口**：子问题 q4 要求给出 MUSDB18 等基准上的**具体指标口径（SDR/SI-SDR、BSSEval 版本等）与硬件要求**。候选证据**未包含任何数值指标**，也未包含任何 GPU/算力信息。**所有分离与编解码的性能数字 `> 待核实`。**

---

## 六、经典与奠基性工作

> 说明：本节分两部分。**(A)** 为可引用编号来源 [1]–[112] 中具备奠基性质的工作；**(B)** 为**用户预置的领域种子资源**（含直链，标注「种子」，未在本次引用列表中，其热度与指标一律 `> 待核实`，不得转述为已核验事实）。

### (A) 编号来源中的奠基性工作

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Music Transformer | 2018 | — | `> 待核实` | arXiv 预印本 [53] | 低（无热度信号） | ★★★★★ | http://arxiv.org/abs/1809.04281v3 | 相对位置表示实现长程音乐生成，符号音乐 Transformer 奠基 [53] |
| End-to-end music source separation: is it possible in the waveform domain? | 2018 | — | `> 待核实` | arXiv 预印本（cs.SD）[82] | 低 | ★★★★★ | http://arxiv.org/abs/1810.12187v2 | 质疑幅度谱范式、开启波形域端到端分离讨论 [82] |
| A Functional Taxonomy of Music Generation Systems | 2018 | — | `> 待核实` | arXiv 预印本 [27] | 低 | ★★★★☆ | http://arxiv.org/abs/1812.04186v1 | 音乐生成系统的功能性分类学骨架 [27] |
| Singing voice synthesis based on convolutional neural networks | 2019 | — | `> 待核实` | arXiv 预印本（eess.AS）[1] | 低 | ★★★☆☆ | http://arxiv.org/abs/1904.06868v2 | CNN-SVS 谱系起点 [1] |
| Fast and High-Quality Singing Voice Synthesis System based on CNN | 2019 | — | `> 待核实` | arXiv 预印本（eess.AS）[3] | 低 | ★★★☆☆ | http://arxiv.org/abs/1910.11690v2 | 速度-质量权衡的 CNN SVS [3] |
| Learning a Representation for Cover Song Identification Using CNN | 2019 | — | `> 待核实` | arXiv 预印本 [4] | 低 | ★★★☆☆ | http://arxiv.org/abs/1911.00334v1 | CNN 翻唱识别表征学习 [4] |
| Slakh2100（Cutting Music Source Separation Some Slakh） | 2019 | — | `> 待核实` | arXiv 预印本 + 数据集 [91] | 低 | ★★★★☆ | http://arxiv.org/abs/1909.08494v1 | 合成多轨集，研究训练数据质量/数量对分离的影响 [91] |
| Symbolic Music Representations for Classification Tasks | 2023 | — | `> 待核实` | arXiv 预印本（eess.AS）[26] | 低 | ★★★★☆ | http://arxiv.org/abs/2309.02567v2 | 系统评估符号音乐表征，指出"非图非句"的本质困难 [26] |
| MARBLE: Music Audio Representation Benchmark | 2023 | — | `> 待核实` | arXiv 预印本 [95] | `> 待核实` | ★★★★★ | http://arxiv.org/abs/2306.10548v4 | 音乐音频表征通用评测基准 [95] |
| LP-MusicCaps: LLM-Based Pseudo Music Captioning | 2023 | — | `> 待核实` | arXiv 预印本 [96] | `> 待核实` | ★★★★☆ | http://arxiv.org/abs/2307.16372v1 | LLM 伪标注解决音乐-文本配对稀缺 [96] |
| Music Source Separation with Band-Split RoPE Transformer | 2023 | — | `> 待核实` | arXiv 预印本 [84] | `> 待核实` | ★★★★★ | http://arxiv.org/abs/2309.02612v2 | 现代分离骨干 BS-RoFormer [84] |
| SoundStream: An End-to-End Neural Audio Codec | 2021 | — | `> 待核实` | arXiv 预印本 [107] | `> 待核实` | ★★★★★ | http://arxiv.org/abs/2107.03312v1 | 神经音频编解码奠基 [107] |
| NaturalSpeech 2 | 2023 | — | `> 待核实` | arXiv 预印本 [7] | 低 | ★★★★☆ | http://arxiv.org/abs/2304.09116v3 | 潜扩散实现零样本语音与歌声合成 [7] |
| Sound Demixing Challenge 2023 – Music Demixing Track | 2023 | — | `> 待核实` | 挑战报告 [100] | 中（竞赛体系影响力） | ★★★★☆ | http://arxiv.org/abs/2308.06979v4 | MDX 类任务的锚点基准 [100] |
| TFC-TDF-UNet v3（SDX23 系统报告） | 2023 | — | `> 待核实` | 系统技术报告 [102] | `> 待核实` | ★★★★☆ | http://arxiv.org/abs/2306.09382v3 | 强基线系统技术细节 [102] |
| Natural Language Processing Methods for Symbolic Music Generation and IR: A Survey | 2024 | — | citations=51 | ACM Computing Surveys（同行评审）[41] | **高**（citations=51） | ★★★★★ | https://arxiv.org/abs/2402.17467 | 符号音乐 + NLP 的权威综述 [41] |
| HiFi-Codec | 2023 | — | `> 待核实` | arXiv 预印本 [106] | 低 | ★★★★☆ | http://arxiv.org/abs/2305.02765v2 | 分组残差矢量量化编解码 [106] |

### (B) 用户预置种子资源（未在本次引用列表中）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| MusicLM: Generating Music From Text | 2023 | Google Research | `> 待核实` | 种子资源；arXiv:2301.11325（未在引用列表） | `> 待核实` | ★★★★★ | https://arxiv.org/abs/2301.11325 | 文本到音乐奠基（种子） |
| MusicGen: Simple and Controllable Music Generation | 2023 | Meta（NeurIPS） | `> 待核实` | 种子资源；arXiv:2306.05284（未在引用列表） | `> 待核实` | ★★★★★ | https://arxiv.org/abs/2306.05284 | 可控音乐生成（种子） |
| Music Source Separation in the Waveform Domain（Demucs） | 2019 | Meta | `> 待核实` | 种子资源；arXiv:1911.13254（未在引用列表） | `> 待核实` | ★★★★★ | https://arxiv.org/abs/1911.13254 | 波形域音源分离（种子） |

> **注**：三篇种子论文在概念上与编号来源 [82]（波形域分离可行性 [82]）、[41]（符号音乐综述 [41]）形成互补，但因不在本次引用列表中，本报告**不对其指标、引用数或榜单表现作任何陈述**。

---

## 七、数据集、评测与开放问题

### 7.1 数据集与基准

> 编号来源可见的音频/音乐数据集（含音乐理解与评测基准）：

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Slakh2100 | 2019 | — | `> 待核实` | arXiv 预印本 + 数据集页 [91] | 低 | ★★★★☆ | http://arxiv.org/abs/1909.08494v1 | 合成多轨分离集，用于研究数据规模效应 [91] |
| FMA: A Dataset For Music Analysis | 2016 | — | `> 待核实` | arXiv 预印本 [94] | `> 待核实` | ★★★★☆ | http://arxiv.org/abs/1612.01840v3 | 大规模音乐分析数据集 [94] |
| MARBLE | 2023 | — | `> 待核实` | arXiv 预印本 [95] | `> 待核实` | ★★★★★ | http://arxiv.org/abs/2306.10548v4 | 音乐音频表征通用评测基准 [95] |
| LP-MusicCaps / MusicCaps 类描述数据 | 2023 | — | `> 待核实` | arXiv 预印本 [96] | `> 待核实` | ★★★★☆ | http://arxiv.org/abs/2307.16372v1 | 音乐描述数据构造 [96] |
| GlobalMood | 2025 | — | `> 待核实` | arXiv 预印本（cs.IR）[25] | 低 | ★★★★☆ | http://arxiv.org/abs/2505.09539v2 | 跨文化音乐情绪识别基准 [25] |
| HumMusQA | 2026 | — | `> 待核实` | arXiv 预印本（cs.CL）[92] | 低 | ★★★★☆ | http://arxiv.org/abs/2603.27877v1 | 人类撰写的音乐理解问答基准，面向 LALMs [92] |
| Sanidha | 2025 | — | `> 待核实` | arXiv 预印本 [89] | 低 | ★★★☆☆ | http://arxiv.org/abs/2501.06959v1 | 工作室级 Carnatic 音乐多模态数据集，属跨文化数据补充 [89] |
| Story2MIDI dataset | 2025 | — | `> 待核实` | 随 arXiv 预印本发布 [54] | 低 | ★★★☆☆ | http://arxiv.org/abs/2512.02192v1 | 文本情感—音乐情感配对数据集；**规模与许可 `> 待核实`** [54] |
| Codec-SUPERB @ SLT 2024 | 2024 | — | `> 待核实` | SLT 2024 关联基准 [108] | 中 | ★★★★☆ | http://arxiv.org/abs/2409.14085v1 | 神经音频编解码轻量基准 [108] |
| AMT Challenge 2025（多乐器转谱） | 2026 | — | `> 待核实` | 挑战总结报告 [88] | 中（8 支队、2 支超基线） | ★★★★☆ | http://arxiv.org/abs/2603.27528v1 | 多乐器自动转谱基准与结果 [88] |

> 用户预置种子数据集（含直链，未在引用列表）：

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| MUSDB18 / MUSDB18-HQ | — | sigsep 社区 | `> 待核实` | 种子资源（官方数据集页） | `> 待核实` | ★★★★★ | https://sigsep.github.io/datasets/musdb.html | 音源分离标准集（种子） |
| MTG-Jamendo | — | MTG（UPF） | `> 待核实` | 种子资源（GitHub 仓库） | `> 待核实` | ★★★★☆ | https://github.com/MTG/mtg-jamendo-dataset | 标签/情绪/乐器标注（种子） |
| Million Song Dataset / AcousticBrainz | — | — | `> 待核实` | 种子资源 | `> 待核实` | ★★★★☆ | http://millionsongdataset.com/ | 大规模 MIR 元数据（种子） |
| Slakh2100（数据集页） | — | — | `> 待核实` | 种子资源 | `> 待核实` | ★★★★☆ | http://www.slakh.com/ | 合成多轨分离集（种子，与 [91] 对应） |

> **可比性边界缺口**：子问题 q5 要求说明各数据集的**任务定义、许可协议与可比性边界**。候选证据中**没有任何一条提供了许可协议（license）信息**，MUSDB18 的指标口径、MoisesDB / AudioSet / MARBLE 的任务切分细节均 `> 待核实`。**本报告不对任何数据集的许可与可比性下结论。**

### 7.2 开源项目

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| facebookresearch/audiocraft | — | Meta | `> 待核实` | 种子资源（官方 GitHub） | `> 待核实` | ★★★★★ | https://github.com/facebookresearch/audiocraft | MusicGen / AudioGen 工具链（种子） |
| facebookresearch/demucs | — | Meta | `> 待核实` | 种子资源（官方 GitHub） | `> 待核实` | ★★★★★ | https://github.com/facebookresearch/demucs | SOTA 音源分离（种子），与 [82] 谱系相关 [82] |
| deezer/spleeter | — | Deezer | `> 待核实` | 种子资源（官方 GitHub） | `> 待核实` | ★★★★☆ | https://github.com/deezer/spleeter | 经典分离基线（种子） |
| k2-fsa/k2 | — | k2 社区 | `> 待核实` | 种子资源（GitHub） | `> 待核实` | ★★☆☆☆ | https://github.com/k2-fsa/k2 | 语音/音频建模工具（种子）；**与音乐任务的直接相关性 `> 待核实`** |
| librosa/librosa | — | librosa 社区 | `> 待核实` | 种子资源（官方 GitHub） | `> 待核实` | ★★★★★ | https://github.com/librosa/librosa | MIR 特征与工具事实标准（种子） |

> **关键缺口**：子问题 q3 点名的 **so-vits-svc、RVC、Seed-VC、CoverHunter** 等开源实现，在本次候选证据中**完全缺席**——既无仓库链接，也无 star、许可协议或复现报告。**该子问题关于开源实现可复现性的部分整体 `> 待核实`。**

### 7.3 开放问题与争议

1. **生成音乐的版权与训练数据合规**
   - 证据：No Encore 提出以反学习（unlearning）作为版权 opt-out 技术机制 [71]；

## 四、音乐理解与自监督表征

> 本章定位：音乐理解在近两年从「判别式 MIR 任务（tagging / 情绪 / 结构）」向两条线迁移——(a) 面向 Large Audio-Language Model（LALM）的**问答式理解基准**，(b) 面向跨文化泛化的**自监督/持续预训练表征**。但需先申明一个证据缺口：**MERT、CLMR、wav2vec 2.0、HuBERT、Jukebox、MusicFM 等自监督音乐表征的原始论文与其开源权重，均未出现在本次可引用来源列表中**，因此其引用数、star、榜单排名一律 `> 待核实`，本章只能就「有编号可查」的来源展开。

### 4.1 音乐理解的基准化：从标签预测走向问答与主观质量预测

| 条目 | 年份 | 机构/作者线索 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 链接/说明 |
|---|---|---|---|---|---|---|---|
| HumMusQA: A Human-written Music Understanding QA Benchmark Dataset [92] | 2026 | cs.CL 预印本 | `> 待核实`（候选块未给 citations/star） | arXiv 预印本，候选块未标注同行评审 venue [92] | 低——候选块无热度信号，仅可确认是 2026 年新预印本 [92] | ★★★☆☆ —— 直接回应「LALM 是否真能感知音乐」这一评测缺口，主张现有多数数据方法论不满足该标准，但无榜单数字 [92] | http://arxiv.org/abs/2603.27877v1 |
| MARBLE: Music Audio Representation Benchmark for Universal Evaluation [95] | 2023 | 多机构 | `> 待核实` | arXiv 预印本，候选块未标注 venue [95] | 中——作为通用音乐表征评测基准被广泛用作下游评估口径，但本报告候选证据未含其榜单 [95] | ★★★★☆ —— 比较自监督音乐表征（MERT 一脉）时绕不开的评测套件，是「表征好不好」的可比性前提 [95] | http://arxiv.org/abs/2306.10548v4 |
| AImoclips: A Benchmark for Evaluating Emotion Conveyance in Text-to-Music Generation [63] | 2025 | cs.SD 预印本 | `> 待核实` | arXiv 预印本 [63] | 低——候选块未提供引用/下载/榜单信号 [63] | ★★★★☆ —— 把「情感传达」从生成目标变成可评测对象，与 [54] 的文本情感—音乐情感对齐形成生成/评测闭环 [63][54] | http://arxiv.org/abs/2509.00813v2 |
| The AudioMOS Challenge 2025（Track 1/2 含 text-to-music）[50]；参赛系统 ASTAR-NTU Track1 [66] | 2025 | IEEE ASRU 2025 | `> 待核实` | IEEE ASRU 2025，同行评审会议 [50]；[66] 为参赛系统技术报告（arXiv） | 中——首个合成音频自动主观质量预测挑战，24 支团队参与 [50] | ★★★★☆ —— 把 MOS 从人工听测推向可复现的自动预测，且已有第三方参赛系统报告 [50][66] | http://arxiv.org/abs/2509.01336v1 ；http://arxiv.org/abs/2507.09904v1 |

**要点**
- 音乐理解的评测正在「问题化」：从固定标签分类，转向 QA 式（[92]）与主观质量/情感传达式（[50][63]）评测。这是评估口径层面的范式变化，而非单一模型刷新 [50][92]。
- 需注意口径差异：[50] 的 Track 1 评的是「整质量 + 文本对齐」，Track 2 基于 Meta Audiobox Aesthetics 的四维度且混入 TTS/TTA/TTM 样本，**与纯 MIR 标签体系的指标不可直接互换** [50]。`> 待核实`：候选证据未给出各 track 的具体指标数值与基线改进幅度。

### 4.2 自监督音乐表征与跨文化泛化

- **CultureMERT-95M（[36]，2025）**：以 continual pre-training 构建「多文化适配」的音乐基础模型，目标是提升跨文化音乐表征学习效果，论文明确指出既有音乐基础模型在不同音乐传统上效果有限 [36]。
  - 热度证据：`> 待核实`（候选块无 citations/star/下载量 [36]）。
  - 权威证据：arXiv 预印本（cs.SD），候选块未标注同行评审 venue [36]。
  - 关注度：中 —— 依据是「基础模型跨文化迁移」是 2025 年 MIR 与公平性讨论的交汇议题，且该文同时出现在 q2/q5/q6 三个子问题的候选证据中 [36]。
  - 推荐度：★★★★☆ —— 与「跨文化泛化」这一开放问题直接相关 [36]，但**是否开源权重、其预训练基座是否为 MERT 一脉、是否在 MARBLE [95] 上有可比值，均 `> 待核实`**。
- **GetMood / 情绪侧数据（[25]，2025）**：GlobalMood 指出既有情绪数据集以西方歌曲 + 英文术语为主，限制跨语言文化泛化 [25]。
  - 热度证据：`> 待核实`；权威证据：arXiv（cs.IR），非同行评审 venue 标注 [25]；关注度：中（跨文化公平性议题受到持续讨论，见 [32]）；推荐度：★★★★☆ —— 是「情绪识别评测不可比」这一具体断点的可引用来源 [25]。
- **社区结构性问题（[32]）**：对 ISMIR 前 25 年作者群体的文献计量分析指出，西方视角塑造了 MIR 研究议程，社区代表性问题仍未解决 [32]。
  - 热度证据：citations=5 [32]；权威证据：*Transactions of the International Society for Music Information Retrieval*（同行评审期刊，DOI 可查）[32]；关注度：中——依据是 citations=5 且该文属期刊正式发表 [32]；推荐度：★★★★☆ —— 讨论 MIR 方法论偏倚与数据集正当性时的权威引证 [32]。
- **符号侧表征选择（[26]，2023）**：系统评估把符号音乐编码为「类图像」或「类语言」对分类任务的影响，指出符号音乐既不是图像也不是句子，编码方式本身会显著影响结论 [26]。
  - 热度证据：`> 待核实`；权威证据：arXiv（eess.AS），候选块未标注 venue [26]；关注度：低——候选块无热度信号 [26]；推荐度：★★★★☆ —— 做符号 MIR 特征工程或复现实验时的「表征选择」必读对照 [26]。
- **歌词—情绪动态（[6]）**：用状态空间模型建模歌词中的情绪动态演化，提示「音乐理解」不只属于音频侧 [6]。
  - 热度证据：`> 待核实`；权威证据：arXiv 预印本 [6]；关注度：低——候选块无热度信号；推荐度：★★★☆☆ —— 若做歌词侧情绪/结构建模可作补充线索 [6]。
- **工具链（[28][103]）**：MIRFLEX 提供音乐信息检索特征提取库 [28]；musif 提供符号音乐特征提取的 Python 包 [103]。两者热度均 `> 待核实`；权威证据为工具类 arXiv 预印本 [28][103]；关注度：低；推荐度：★★★☆☆ —— 属工程可用性线索，**维护活跃度与 star 数需另行核实** [28][103]。
- **结构分析（[29]）**：Barwise 相关块匹配分割算法用于音乐结构分析 [29]，热度 `> 待核实`，权威为 arXiv 预印本，关注度低，推荐度 ★★★☆☆（结构任务的可复现基线线索）。

### 4.3 本章证据矩阵小结与缺口

| 结论 | 证据等级 | 依据 |
|---|---|---|
| 音乐理解已出现「问答式基准 + 主观质量/情感传达评测」的评测方法论转向 | B（预印本 + 1 篇同行评审挑战论文） | [50][63][92] |
| 跨文化泛化被明确识别为音乐基础模型的短板，并已有持续预训练方案 | B | [36][25][32] |
| 自监督音乐表征的完整谱系（wav2vec/HuBERT/CLMR/MERT）无法在本报告内建立 | E（缺位） | 可引用来源中无对应编号 → `> 待核实` |
| 音乐生成与音乐理解是否统一到同一基础模型 | E | 候选证据无直接证据 → `> 待核实` |

---

## 八、建议关注清单（Watchlist）

> 说明：下表「热度证据」仅记录**候选来源中真实可查的数字**，未提供者一律 `> 待核实`；「关注度」是结合引用数、star、榜单排名、机构与议题热度的编辑判断；「推荐度」综合权威 + 热度 + 与本主题相关性。

| # | 关注方向 / 条目 | 为何值得盯 | 关键来源 | 热度证据 | 权威证据 | 关注度 | 推荐度 |
|---|---|---|---|---|---|---|---|
| 1 | **合成音频自动主观质量评估**（AudioMOS 系列：MOS 预测替代人工听测） | 决定 text-to-music 与 TTS 是否具备可复现的「质量标尺」 | [50] 挑战总结；[66] Track1 参赛系统 | `> 待核实`（候选块未给引用数） | IEEE ASRU 2025 同行评审 [50]；arXiv 技术报告 [66] | 中——首个该方向挑战，24 支团队参与 [50] | ★★★★☆：基准+第三方解法双证据，是评估侧最可落地的一环 [50][66] |
| 2 | **文本到音乐的情感/语义对齐与情感传达评测** | 把「生成得像」升级为「生成得对（情感/文本一致）」 | [54] Story2MIDI（含自建数据集）；[63] AImoclips 基准 | `> 待核实` | arXiv 预印本（cs.SD），未标注 venue [54][63] | 低—中——候选块无引用/下载信号 [54][63] | ★★★☆☆：路线新颖但缺指标细节，引用前须核对实验表 [54][63] |
| 3 | **跨文化音乐基础模型与表征泛化** | 现有音乐基础模型在不同音乐传统上效果受限，公平性议题进入 MIR 主流 | [36] CultureMERT-95M；[25] GlobalMood；[32] ISMIR 作者群体文献计量 | citations=5 [32]；其余 `> 待核实` | TISMIR 同行评审期刊 [32]；arXiv 预印本 [36][25] | 中——期刊文献计量 + 多篇 2025 预印本形成议题簇 [32][25][36] | ★★★★☆：兼具学术正当性与工程影响（多语言/多文化曲库）[32][36] |
| 4 | **音乐理解 QA 基准（面向 LALM）** | 检验「音乐理解」是真听懂还是语言先验 | [92] HumMusQA | `> 待核实` | arXiv（cs.CL）预印本 [92] | 低——新预印本，候选块无热度信号 | ★★★☆☆：是评测缺口的第一手尝试，但可复现性待观察 [92] |
| 5 | **神经音频编解码的评测与可解释性** | 音频 tokenizer 是音乐生成/理解的上游，需可比的编解码基准与语义-声学单元可解释性 | [108] Codec-SUPERB 轻量基准；[112] Bringing Interpretability to Neural Audio Codecs；[105] 2025 低资源音频编解码挑战基线；[110] 编解码重合成；[109] APCodec；[106] HiFi-Codec | `> 待核实` | 均为 arXiv 预印本/技术报告，未标注同行评审 venue [105][106][108][109][110][112] | 中——多个基准/挑战与编码器工作在同一时期密集出现 [105][108][112] | ★★★★☆：是「音频 tokenizer 路线」唯一在本次可引用来源中有据可查的抓手 [108][112] |
| 6 | **低码率 / 低资源音频编解码部署** | 端侧与受限算力部署的实际约束 | [105] LRAC Challenge 2025 基线系统 | `> 待核实` | arXiv 技术报告 [105] | 低—中——挑战首设，候选块无参与规模数字 | ★★★☆☆：适合工程选型参考，指标口径需读原文 [105] |
| 7 | **音乐源分离→「修复/去制作痕迹」新任务（MSR）与 BandSplit-RoFormer 路线** | 从「分离乐器」转向「还原母带前原始分轨」，挑战线性混合假设 | [85] MSR ICASSP Challenge 技术报告（BandSplit-RoFormer + HiFi++）；[84] Band-Split RoPE Transformer；[86] Bridging Network；[100] SDX 2023 Music Demixing 综述；[102] TFC-TDF-UNet v3 | `> 待核实` | arXiv 预印本/技术报告，未标注同行评审 venue [84][85][86][100][102] | 中——SDX 与 MSR 形成连续挑战谱系 [100][85] | ★★★★☆：分离方向近两年最明确的任务重定义，工程与学术双相关 [85][100] |
| 8 | **歌声转换 / 歌声合成的零样本与复音鲁棒性** | 零样本多语言与「带伴奏」场景是落地关键瓶颈 | [8] TCSinger 2；[10] FreeSVC；[11] 聚类音素零样本 SVC；[13] SPA-SVC；[14] LHQ-SVC；[15] Poly-SVC；[16] LDM-SVC；[7] NaturalSpeech 2 | `> 待核实` | 均为 arXiv 预印本（cs.SD/eess.AS），未标注同行评审 venue | 中——同一子领域 2024–2026 多篇并发，Poly-SVC 明确针对「无法从伴奏中可靠提取干净人声」的实际问题 [15] | ★★★★☆：Poly-SVC 与 FreeSVC 指出的问题（伴奏干扰、多语言、音高鲁棒）是真实工程痛点 [10][15] |
| 9 | **翻唱识别（CSI）与版本识别** | 版权与曲库去重的基础能力，但近两年检索证据缺位 | [4] CNN 翻唱表征；[5] 大规模曲库翻唱检测（元数据+歌词+音频） | `> 待核实` | arXiv 预印本（2018/2019），属较早期工作 [4][5] | 低——候选块无近 1–2 年新证据 | ★★★☆☆：经典可用，但**近两年是否出现零样本/少样本 CSI 新方法无法确认 → `> 待核实`** [4][5] |
| 10 | **生成音乐的版权合规与「遗忘/退出」机制** | 从伦理呼吁走向技术可执行（unlearning、opt-out） | [71] No Encore（unlearning as opt-out）；[72] AI 音乐论文伦理声明实证研究；[70] 基础模型训练与版权法的压缩视角 | `> 待核实` | arXiv 预印本（cs.CL / cs.CY）[71][72][70] | 中——版权议题在 2025 年持续升温，出现专门的技术与实证研究 [71][72] | ★★★★☆：合规是文本到音乐产品化的硬约束，[71][72] 提供了「技术方案 + 声明有效性」两端证据 [71][72] |
| 11 | **评测本身的可信度：分数会「腐坏」、主观评测可复现性** | 决定榜单能否作为决策依据 | [74] Position: Evaluation Scores Are Perishable Knowledge Claims；[75] 可扩展可靠自动评测；[81] Reproducible Subjective Evaluation；[76] 生成模型评测指标 | `> 待核实` | arXiv 预印本（含 Position paper）[74][75][76][81] | 中——多个 2026 年预印本同时讨论评测可信度 [74][75] | ★★★★☆：与本章第 1 条互补，评「评测方法」而非评「模型」[74][81] |
| 12 | **符号音乐 × NLP/LLM 方法迁移** | 符号音乐与文本共享序列结构，是 LLM 方法迁移的低成本试验场 | [41] NLP 方法用于符号音乐生成与 IR 综述；[57] 结构化状态空间扩散符号生成；[59] Transformer 生成钢琴音乐对比研究；[55][56] 文本到音乐/学术 TTM 挑战参赛系统 | citations=51 [41]；其余 `> 待核实` | **ACM Computing Surveys（同行评审期刊）[41]** | 高——[41] 在候选块中热度最高（citations=51）[41] | ★★★★★：本主题下权威性与热度兼优的入口综述 [41]，配合 [57][59] 看新方法 [57][59] |
| 13 | **ISMIR 会议主线跟踪（一手论文集）** | 该领域论文主要在 ISMIR 而非 ML 顶会发布，跟踪会议论文集是覆盖度最有效手段 | [34] ISMIR 2025（Daejeon）；[35] ISMIR 2024；[43] ISMIR 2023；[39] ISMIR 2022 报告；[45] Human-Centric MIR Workshop 2023 | `> 待核实` | 会议论文集/官方报告（同行评审）[34][35][39][43][45] | 中——领域内主要发表渠道，但候选块未提供规模/引用数字 | ★★★★☆：补齐「会议级覆盖」的必需来源，可据此扩展本报告缺位的 MERT/CLMR 一脉 [34][35] |
| 14 | **音乐理解与生成的统一模型是否成立** | 决定未来 1–2 年是「两栈并行」还是「单模型统一」 | 无可直接引用来源 | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实`——本次候选证据未覆盖统一音音乐语言模型/音频 tokenizer 在统一建模中的角色，需补检索 [49][51][52] 等无关来源可排除在外 |

**每季度最小跟踪动作（建议）**：① 检索 ISMIR 最新一届论文集与 arXiv cs.SD 近 3 个月新增 [34][35]；② 跟踪 AudioMOS / SDX / MSR / LRAC 等挑战的下一届结果页以获取可比指标 [50][85][100][105]；③ 对 MARBLE [95] 与 HumMusQA [92] 等基准检查是否有第三方复现报告，避免把「论文自报」当作「榜单共识」。

## 参考来源

[1] Singing voice synthesis based on convolutional neural networks — http://arxiv.org/abs/1904.06868v2
[2] ConSinger: Efficient High-Fidelity Singing Voice Generation with Minimal Steps — http://arxiv.org/abs/2410.15342v3
[3] Fast and High-Quality Singing Voice Synthesis System based on Convolutional Neural Networks — http://arxiv.org/abs/1910.11690v2
[4] Learning a Representation for Cover Song Identification Using Convolutional Neural Network — http://arxiv.org/abs/1911.00334v1
[5] Large-Scale Cover Song Detection in Digital Music Libraries Using Metadata, Lyrics and Audio Features — http://arxiv.org/abs/1808.10351v1
[6] Modelling Emotion Dynamics in Song Lyrics with State Space Models — http://arxiv.org/abs/2210.09434v1
[7] NaturalSpeech 2: Latent Diffusion Models are Natural and Zero-Shot Speech and Singing Synthesizers — http://arxiv.org/abs/2304.09116v3
[8] TCSinger 2: Customizable Multilingual Zero-shot Singing Voice Synthesis — http://arxiv.org/abs/2505.14910v3
[9] Towards Improved Zero-shot Voice Conversion with Conditional DSVAE — http://arxiv.org/abs/2205.05227v2
[10] FreeSVC: Towards Zero-shot Multilingual Singing Voice Conversion — http://arxiv.org/abs/2501.05586v1
[11] Zero-Shot Sing Voice Conversion: built upon clustering-based phoneme representations — http://arxiv.org/abs/2409.08039v2
[12] SVC 2025: the First Multimodal Deception Detection Challenge — http://arxiv.org/abs/2508.04129v1
[13] SPA-SVC: Self-supervised Pitch Augmentation for Singing Voice Conversion — http://arxiv.org/abs/2406.05692v1
[14] LHQ-SVC: Lightweight and High Quality Singing Voice Conversion Modeling — http://arxiv.org/abs/2409.08583v2
[15] Poly-SVC: Polyphony-Aware Singing Voice Conversion with Harmonic Modeling — http://arxiv.org/abs/2605.12310v1
[16] LDM-SVC: Latent Diffusion Model Based Zero-Shot Any-to-Any Singing Voice Conversion with Singer Guidance — http://arxiv.org/abs/2406.05325v1
[17] Learn to Accumulate Evidence from All Training Samples: Theory and Practice — http://arxiv.org/abs/2306.11113v2
[18] The Modern Mathematics of Deep Learning — http://arxiv.org/abs/2105.04026v2
[19] Deep Learning and Computational Physics (Lecture Notes) — http://arxiv.org/abs/2301.00942v1
[20] The Sloop System for Individual Animal Identification with Deep Learning — http://arxiv.org/abs/2003.00559v1
[21] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1
[22] On the Popularity of GitHub Applications: A Preliminary Note — http://arxiv.org/abs/1507.00604v3
[23] What Challenges Do Developers Face in AI Agent Systems? An Empirical Study on Stack Overflow & GitHub Issues — http://arxiv.org/abs/2510.25423v2
[24] Emotional Contagion in Code: How GitHub Emoji Reactions Shape Developer Collaboration — http://arxiv.org/abs/2511.02515v1
[25] GlobalMood: A cross-cultural benchmark for music emotion recognition — http://arxiv.org/abs/2505.09539v2
[26] Symbolic Music Representations for Classification Tasks: A Systematic Evaluation — http://arxiv.org/abs/2309.02567v2
[27] A Functional Taxonomy of Music Generation Systems — http://arxiv.org/abs/1812.04186v1
[28] MIRFLEX: Music Information Retrieval Feature Library for Extraction — http://arxiv.org/abs/2411.00469v1
[29] Barwise Music Structure Analysis with the Correlation Block-Matching Segmentation Algorithm — http://arxiv.org/abs/2311.18604v1
[30] Towards Multimodal MIR: Predicting individual differences from music-induced movement — http://arxiv.org/abs/2007.10695v1
[31] Music SketchNet: Controllable Music Generation via Factorized Representations of Pitch and Rhythm — http://arxiv.org/abs/2008.01291v1
[32] Beyond a Western Center of Music Information Retrieval: A Bibliometric Analysis of the First 25 Years of ISMIR Authorship — https://doi.org/10.5334/tismir.265
[33] Learning to Traverse Latent Spaces for Musical Score Inpainting — http://arxiv.org/abs/1907.01164v1
[34] Proceedings of the 26th International Society for Music Information Retrieval Conference, ISMIR 2025, Daejeon, South Korea, September 21-25, 2025 — https://www.semanticscholar.org/paper/1fbd102a725a70ea20eb27ef42573d742c1455b4
[35] Proceedings of the 25th International Society for Music Information Retrieval Conference, ISMIR 2024, San Francisco, California, USA and Online, November 10-14, 2024 — https://www.semanticscholar.org/paper/61f878040ff416d27b3c25384fbe97229a764367
[36] CultureMERT: Continual Pre-Training for Cross-Cultural Music Representation Learning — http://arxiv.org/abs/2506.17818v1
[37] A Survey of Large Language Model Empowered Agents for Recommendation and Search: Towards Next-Generation Information Retrieval — https://arxiv.org/abs/2503.05659
[38] Improving Few-Shot Learning with Auxiliary Self-Supervised Pretext Tasks — http://arxiv.org/abs/2101.09825v1
[39] Report on the 23rd International Society for Music Information Retrieval Conference (ISMIR 2022) — https://doi.org/10.1145/3636341.3636350
[40] Towards Label-efficient Automatic Diagnosis and Analysis: A Comprehensive Survey of Advanced Deep Learning-based Weakly-supervised, Semi-supervised and Self-supervised Techniques in Histopathological Image Analysis — http://arxiv.org/abs/2208.08789v2
[41] Natural Language Processing Methods for Symbolic Music Generation and Information Retrieval: A Survey — https://arxiv.org/abs/2402.17467
[42] Supervise Thyself: Examining Self-Supervised Representations in Interactive Environments — http://arxiv.org/abs/1906.11951v1
[43] Proceedings of the 24th International Society for Music Information Retrieval Conference, ISMIR 2023, Milan, Italy, November 5-9, 2023 — https://www.semanticscholar.org/paper/fdcd30be63867dff918996d11fab5fed4a5b824f
[44] SelfMatch: Combining Contrastive Self-Supervision and Consistency for Semi-Supervised Learning — http://arxiv.org/abs/2101.06480v1
[45] Proceedings of the 2nd Workshop on Human-Centric Music Information Retrieval 2023 co-located with the 24th International Society for Music Information Retrieval Conference (ISMIR 2023), Milan, Italy, November 10, 2023 — https://www.semanticscholar.org/paper/d521ffbbf5fb058b6332067ee423123aba01fc1a
[46] Diffusion Models and Representation Learning: A Survey — http://arxiv.org/abs/2407.00783v1
[47] Self-Supervised Learning for Large-Scale Unsupervised Image Clustering — http://arxiv.org/abs/2008.10312v2
[48] Self-Supervised Representation Learning for Astronomical Images — http://arxiv.org/abs/2012.13083v2
[49] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1
[50] The AudioMOS Challenge 2025 — http://arxiv.org/abs/2509.01336v1
[51] NTIRE 2025 Challenge on Image Super-Resolution (x4): Methods and Results — http://arxiv.org/abs/2504.14582v3
[52] VLSP 2025 MLQA-TSR Challenge: Vietnamese Multimodal Legal Question Answering on Traffic Sign Regulation — http://arxiv.org/abs/2510.20381v1
[53] Music Transformer — http://arxiv.org/abs/1809.04281v3
[54] Story2MIDI: Emotionally Aligned Music Generation from Text — http://arxiv.org/abs/2512.02192v1
[55] Instrumental Text-to-Music Generation with Auxiliary Conditioning Branches — http://arxiv.org/abs/2605.21433v1
[56] UT-AISTimprt submission for ICME 2026 Grand Challenge on Academic Text-to-Music Generation — http://arxiv.org/abs/2607.01669v1
[57] Diffusion-based Symbolic Music Generation with Structured State Space Models — http://arxiv.org/abs/2507.20128v2
[58] Text-to-image Diffusion Models in Generative AI: A Survey — http://arxiv.org/abs/2303.07909v3
[59] Generating Piano Music with Transformers: A Comparative Study of Scale, Data, and Metrics — http://arxiv.org/abs/2511.07268v2
[60] Vision-to-Music Generation: A Survey — http://arxiv.org/abs/2503.21254v1
[61] Improving Polyphonic Music Models with Feature-Rich Encoding — http://arxiv.org/abs/1911.11775v3
[62] Image Segmentation in Foundation Model Era: A Survey — http://arxiv.org/abs/2408.12957v3
[63] AImoclips: A Benchmark for Evaluating Emotion Conveyance in Text-to-Music Generation — http://arxiv.org/abs/2509.00813v2
[64] Overview of the Sensemaking Task at the ELOQUENT 2025 Lab: LLMs as Teachers, Students and Evaluators — http://arxiv.org/abs/2507.12143v1
[65] LongEval at CLEF 2025: Longitudinal Evaluation of IR Model Performance — http://arxiv.org/abs/2503.08541v1
[66] ASTAR-NTU solution to AudioMOS Challenge 2025 Track1 — http://arxiv.org/abs/2507.09904v1
[67] TDCOSMO 2025: Cosmological constraints from strong lensing time delays — http://arxiv.org/abs/2506.03023v4
[68] Improving Choral Music Separation through Expressive Synthesized Data from Sampled Instruments — http://arxiv.org/abs/2209.02871v1
[69] Beyond principlism: Practical strategies for ethical AI use in research practices — http://arxiv.org/abs/2401.15284v6
[70] Training Foundation Models as Data Compression: On Information, Model Weights and Copyright Law — http://arxiv.org/abs/2407.13493v4
[71] No Encore: Unlearning as Opt-Out in Music Generation — http://arxiv.org/abs/2509.06277v2
[72] Ethics Statements in AI Music Papers: The Effective and the Ineffective — http://arxiv.org/abs/2509.25496v1
[73] TerraGen: A Unified Multi-Task Layout Generation Framework for Remote Sensing Data Augmentation — http://arxiv.org/abs/2510.21391v1
[74] Position: Evaluation Scores Are Perishable Knowledge Claims — http://arxiv.org/abs/2607.26191v1
[75] (Towards) Scalable Reliable Automated Evaluation with Large Language Models — http://arxiv.org/abs/2607.28282v1
[76] Evaluating Generative Models for Tabular Data: Novel Metrics and Benchmarking — http://arxiv.org/abs/2504.20900v1
[77] Critique-RL: Training Language Models for Critiquing through Two-Stage Reinforcement Learning — http://arxiv.org/abs/2510.24320v1
[78] Lexara-RF: Reference-Free Metrics for Evaluating Conversational Visual Analytics Agents — http://arxiv.org/abs/2609.17842v1
[79] SBOMs into Agentic AIBOMs: Schema Extensions, Agentic Orchestration, and Reproducibility Evaluation — http://arxiv.org/abs/2603.10057v1
[80] The expected value under the Yule model of the squared path-difference distance — http://arxiv.org/abs/1203.2503v1
[81] Reproducible Subjective Evaluation — http://arxiv.org/abs/2203.04444v1
[82] End-to-end music source separation: is it possible in the waveform domain? — http://arxiv.org/abs/1810.12187v2
[83] Everyone Can Attack: Repurpose Lossy Compression as a Natural Backdoor Attack — http://arxiv.org/abs/2308.16684v2
[84] Music Source Separation with Band-Split RoPE Transformer — http://arxiv.org/abs/2309.02612v2
[85] Multi-Stage Music Source Restoration with BandSplit-RoFormer Separation and HiFi++ GAN — http://arxiv.org/abs/2603.04032v1
[86] The Whole Is Greater than the Sum of Its Parts: Improving Music Source Separation by Bridging Network — http://arxiv.org/abs/2305.07855v2
[87] Audio query-based music source separation — http://arxiv.org/abs/1908.06593v1
[88] Advancing Multi-Instrument Music Transcription: Results from the 2025 AMT Challenge — http://arxiv.org/abs/2603.27528v1
[89] Sanidha: A Studio Quality Multi-Modal Dataset for Carnatic Music — http://arxiv.org/abs/2501.06959v1
[90] The RSNA Abdominal Traumatic Injury CT (RATIC) Dataset — http://arxiv.org/abs/2405.19595v1
[91] Cutting Music Source Separation Some Slakh: A Dataset to Study the Impact of Training Data Quality and Quantity — http://arxiv.org/abs/1909.08494v1
[92] HumMusQA: A Human-written Music Understanding QA Benchmark Dataset — http://arxiv.org/abs/2603.27877v1
[93] NTIRE 2025 Challenge on Short-form UGC Video Quality Assessment and Enhancement: KwaiSR Dataset and Study — http://arxiv.org/abs/2504.15003v1
[94] FMA: A Dataset For Music Analysis — http://arxiv.org/abs/1612.01840v3
[95] MARBLE: Music Audio Representation Benchmark for Universal Evaluation — http://arxiv.org/abs/2306.10548v4
[96] LP-MusicCaps: LLM-Based Pseudo Music Captioning — http://arxiv.org/abs/2307.16372v1
[97] Introduction to Gestural Similarity in Music. An Application of Category Theory to the Orchestra — http://arxiv.org/abs/1904.10340v1
[98] TRUST 2025: SCRITA and RTSS @ RO-MAN 2025 — http://arxiv.org/abs/2509.11402v1
[99] Exploiting Music Source Separation for Automatic Lyrics Transcription with Whisper — http://arxiv.org/abs/2506.15514v1
[100] The Sound Demixing Challenge 2023 $\unicode{x2013}$ Music Demixing Track — http://arxiv.org/abs/2308.06979v4
[101] The IEEE-IS2 2024 Music Packet Loss Concealment Challenge — http://arxiv.org/abs/2409.18564v1
[102] Sound Demixing Challenge 2023 Music Demixing Track Technical Report: TFC-TDF-UNet v3 — http://arxiv.org/abs/2306.09382v3
[103] musif: a Python package for symbolic music feature extraction — http://arxiv.org/abs/2307.01120v1
[104] Overview of AuTexTification at IberLEF 2023: Detection and Attribution of Machine-Generated Text in Multiple Domains — http://arxiv.org/abs/2309.11285v1
[105] Baseline Systems For The 2025 Low-Resource Audio Codec Challenge — http://arxiv.org/abs/2510.00264v3
[106] HiFi-Codec: Group-residual Vector quantization for High Fidelity Audio Codec — http://arxiv.org/abs/2305.02765v2
[107] SoundStream: An End-to-End Neural Audio Codec — http://arxiv.org/abs/2107.03312v1
[108] Codec-SUPERB @ SLT 2024: A lightweight benchmark for neural audio codec models — http://arxiv.org/abs/2409.14085v1
[109] APCodec: A Neural Audio Codec with Parallel Amplitude and Phase Spectrum Encoding and Decoding — http://arxiv.org/abs/2402.10533v2
[110] A Closer Look at Neural Codec Resynthesis: Bridging the Gap between Codec and Waveform Generation — http://arxiv.org/abs/2410.22448v1
[111] ICAGC 2024: Inspirational and Convincing Audio Generation Challenge 2024 — http://arxiv.org/abs/2407.12038v2
[112] Bringing Interpretability to Neural Audio Codecs — http://arxiv.org/abs/2506.04492v1


---

*Generated by research-bot · topic=`music-audio` · depth=`standard` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading · model=`deepseek-v4-flash` · sources=112 · duration=329s · 2026-10-05T22:52:18+00:00*
