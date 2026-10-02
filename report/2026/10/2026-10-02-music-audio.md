# 音乐与音频算法综述：MIR / 音乐生成 / 音乐理解 / 音源分离与歌声转换

**元信息**：报告日期 2026-10-02（UTC） | 领域：Music & Audio（Music Information Retrieval、Music Generation、Music Understanding、Singing Voice Conversion、Music Source Separation、Self-supervised Audio Representation） | 检索源：本次候选来源共 34 条编号（[1]–[34]），其中 2 条为无效/非相关来源（[12] 撤稿页、[31][32][33] 为 GitHub 首页或登录页），有效来源约 30 条 | 引用纪律：仅使用编号 [1]–[34] 中真实存在的来源，未编号的种子资源单独标注

**证据强度总声明（务必先读）**：本次候选块中绝大多数条目缺失 `citations`/`stars` 字段，且 `authority` 字段多为 arXiv 学科分类（`cs.SD`/`eess.AS`/`cs.IR`/`cs.LG`），**arXiv 分类不等于同行评审 venue**。因此本报告中凡涉及「引用数、GitHub star、下载量、榜单排名」的热度证据，一律标注 `> 待核实`，不做任何数字推测；凡结论仅基于单条 arXiv 预印本，证据等级标为 B（中高）或更低，并加限定词。全篇不使用任何未在本文件来源列表中出现的 URL 作为引用。

---

## 摘要（Executive Summary）

1. **音乐生成已进入「基础模型 + 开源权重 + 编辑能力」阶段。** 2025 年的 ACE-Step 明确自我定位为开源音乐生成基础模型，并以「生成速度 vs 音乐连贯性」的权衡为切入点宣称达到 SOTA [13]；2026 年的工作则开始系统性地剥离「大规模数据 + 外部预训练」的贡献，用辅助条件分支隔离设计变量 [18]。同时，音乐**编辑**（而非纯生成）成为独立子方向：Instruct-MusicGen 用指令微调解锁文本到音乐编辑 [10]，Audio Prompt Adapter 用轻量微调赋予音乐编辑能力 [14]。

2. **文本到音频的音乐/音效生成正在被「推理效率」重构。** IMPACT 直接指出 Tango、AudioLDM 系列虽保真度高但推理代价昂贵，提出基于掩码的并行解码扩散方案 [16]；EzAudio 走高效扩散 Transformer 路线并在 Interspeech 2025 发表 [21]；Stable Audio Open 与 Fast Timing-Conditioned Latent Audio Diffusion 则推动了时序条件化的潜空间扩散 [17][20]。

3. **音源分离（MSS）的技术主线已收敛到 Band-Split + RoPE Transformer 家族。** BS-RoFormer 确立 band-split 前端 + 分层 Transformer 的主干 [25]，Mel-Band RoFormer 进一步把人声分离与人声旋律转录合并到同一模型 [29][24]，X-scheme/Bridging 网络则给出几乎零额外算力的多域损失与跨域耦合改进 [23]。2026 年的 MSR（Music Source Restoration）ICASSP 挑战把问题从「分离」推进到「从成品母带恢复未处理原始 stem」，用 BandSplit-RoFormer + HiFi++ GAN 的多阶段方案处理制作效应与分布伪影 [26]。

4. **音乐理解侧的焦点从「单文化基准」转向「跨文化泛化」。** GlobalMood 明确指出既有音乐情绪数据集以西方歌曲与英文术语为主，构建跨文化音乐情绪识别基准 [2]；CultureMERT 用持续预训练（continual pre-training）做跨文化音乐表征学习 [22]。这与 ISMIR 2025 的学科动向一致 [11]。

5. **符号音乐（symbolic music）的表征问题被系统化提出。** 有工作指出符号音乐既不是图像也不是句子，对「类图像/类语言」编码方式做了系统评估 [3]；MIRFLEX 则提供统一的 MIR 特征提取库 [5]，小节级结构分析有 Correlation Block-Matching 分割算法 [6]。

6. **最大缺口：歌声转换（SVC）与翻唱识别（CSI）在本次检索中证据严重不足。** SVC 侧仅有 2021 年的 DiffSVC 扩散概率模型 [34]，以及 2024 年 Mel-RoFormer 附带的人声旋律转录能力 [29]；**翻唱识别（Cover Song Identification）在有效来源中完全没有对应文献**，本报告该部分标注 `> 待核实`，不做展开。

7. **可复现工程栈（Demucs、Spleeter、audiocraft、librosa、MUSDB18 等）来自本次调研的人工维护种子资源清单，未获得独立编号引用**，其 star 数、许可证与实时性 `> 待核实`，需要二次检索（GitHub API / HuggingFace Hub）补齐。

---

## 一、关键前沿进展（近 1–2 年）

时间窗界定：以 2026-10-02 为基准，**近期 = 2024-10 至 2026-10**；2023 年及以前归入「经典/奠基」（见第六章）。

### 1.1 进展总览表

| 名称 | 时间 | 机构/作者 | 类别 | 热度证据 | 权威证据 | 关注度 | 推荐度 |
|---|---|---|---|---|---|---|---|
| ACE-Step [13] | 2025 | > 待核实 | 音乐生成基础模型 | > 待核实（无 citations/stars 字段） | arXiv `cs.SD` 预印本，非同行评审 venue | 中（自我定位「开源基础模型 + SOTA」具备话题性，但无第三方榜单佐证） | ★★★★☆ 开源音乐生成基础模型的直接对标对象，值得精读其架构与权衡设计 [13] |
| Instrumental Text-to-Music w/ Auxiliary Conditioning [18] | 2026 | > 待核实 | 文本到音乐生成 | > 待核实 | arXiv `cs.SD` 预印本 | 中（提出「隔离设计变量」的方法论价值高于指标） | ★★★★☆ 少见的消融导向研究，适合用来判断「提升来自数据还是架构」 [18] |
| IMPACT [16] | 2025 | > 待核实 | 文本到音频（扩散） | > 待核实 | arXiv `eess.AS` 预印本 | 中高（直击扩散模型推理成本痛点） | ★★★★☆ 若你在做实时音频生成，并行解码思路优先级高 [16] |
| EzAudio [21] | 2025 | > 待核实 | 文本到音频 | > 待核实 | **Interspeech 2025（同行评审会议，DOI 10.21437/interspeech.2025-1137）** | 中高（本批来源中少数经同行评审者） | ★★★★☆ 权威证据为本批最强之一，音频生成工程落地首选参考 [21] |
| Stable Audio Open [17] | 2024 | > 待核实 | 文本到音频/音乐 | > 待核实 | arXiv 预印本 | 中高（开源音频生成代表基座） | ★★★★☆ 常被用作开源基线与微调起点 [17] |
| Fast Timing-Conditioned Latent Audio Diffusion [20] | 2024 | > 待核实 | 潜空间扩散音频 | > 待核实 | arXiv 预印本 | 中（时序条件化 + 快速采样） | ★★★★☆ 与 Stable Audio 系同源技术路线的关键论文 [20] |
| Instruct-MusicGen [10] | 2024 | > 待核实 | 文本到音乐编辑 | > 待核实 | arXiv 预印本（v3） | 中高（把「编辑」从生成中独立出来） | ★★★★☆ 音乐编辑任务的定义性工作之一 [10] |
| Audio Prompt Adapter [14] | 2024 | > 待核实 | 音乐编辑（轻量微调） | > 待核实 | arXiv 预印本（v2） | 中（强调 lightweight finetuning 的工程可行性） | ★★★★☆ 低成本把编辑能力挂到已有 TTM 模型上 [14] |
| LRAC 2025 Baseline [15] | 2025 | > 待核实 | 神经音频编解码 | > 待核实 | arXiv `cs.SD` 预印本 / 挑战基线系统 | 中（低资源 + 噪声混响鲁棒性约束） | ★★★☆ 与「音频生成」交集在 codec tokenizer，属支撑性工作 [15] |
| CultureMERT [22] | 2025 | > 待核实 | 自监督音乐表征 | > 待核实 | arXiv 预印本 | 中高（跨文化泛化是当前明确的未解问题） | ★★★★☆ 跨文化音乐表征的少数直接工作 [22] |
| GlobalMood [2] | 2025 | > 待核实 | 音乐情绪识别基准 | > 待核实 | arXiv `cs.IR` 预印本 | 中高（直指 Western-centric 偏差） | ★★★★☆ 做音乐情绪/推荐时的必查基准 [2] |
| MSR ICASSP Challenge 系统 [26] | 2026 | CP-JKU 团队 | 音源恢复（分离下游） | > 待核实 | 挑战赛技术报告（arXiv `cs.SD`） | 中高（挑战赛体系本身带来可比性） | ★★★★☆ 把分离推进到「去制作效应」的现实问题 [26] |
| Sanidha 数据集 [30] | 2025 | > 待核实 | 多模态音乐数据集 | > 待核实 | arXiv 预印本 | 中（Carnatic 音乐，studio quality） | ★★★☆ 非西方音乐数据资源，跨文化研究的稀缺补位 [30] |

### 1.2 四个值得注意的趋势判断

- **趋势一：从「能不能生成」转向「生成得多快、多可控」。** IMPACT 的立论完全建立在推理成本上 [16]，ACE-Step 也把 generation speed 与 musical coherence 的权衡写进动机 [13]。
- **趋势二：编辑（editing）成为一等任务。** [10][14] 两篇都聚焦于对既有音乐模型施加编辑能力，而非从零生成。
- **趋势三：数据效率与归因意识上升。** [18] 明确批评现有进展依赖大规模数据与外部预训练、「难以隔离哪些设计选择真正起作用」，这是一个方法论信号。
- **趋势四：跨文化泛化成为显式议题。** [2][22][30] 三条来源从基准、表征、数据三个层面同时指向该问题。

> **待核实**：上述模型是否在公开榜单（如音频生成类 leaderboard、MUSDB18 官方榜）上被第三方独立复现或刷新，本次检索未获得任何榜单数据，故所有「SOTA」表述均为**原论文自述**，不可当作第三方验证结论。

---

## 二、音乐信息检索（MIR / 翻唱识别 CSI / 节拍与和声）

### 2.1 特征与工具层

- **MIRFLEX（Music Information Retrieval Feature Library for Extraction）** 提供统一的 MIR 特征提取库，定位为特征工程的公共基础设施 [5]。**热度证据**：> 待核实；**权威证据**：arXiv `cs.SD` 预印本（2024，v1），非同行评审 venue [5]；**关注度**：中（工具库类工作通常以 GitHub star 而非引用衡量，本次未取得 star 数据）；**推荐度**：★★★★☆ 若你要搭 MIR pipeline，这是本批来源中最直接可用的特征层参考 [5]。
- **符号音乐表征的系统性评估**：该工作指出 MIR 领域深度学习方法常把符号音乐（离散音符事件）编码成「类图像」或「类语言」形式，但符号音乐既非图像也非句子，并对此做了系统评估 [3]。**热度证据**：> 待核实；**权威证据**：arXiv `eess.AS` 预印本（2023，v2）[3]；**关注度**：中（触及表征合理性的根本问题）；**推荐度**：★★★★☆ 做符号音乐分类/生成前应读，可避免表征选择上的想当然 [3]。

### 2.2 结构分析与小节级建模

- **Barwise Music Structure Analysis**：基于 Correlation Block-Matching 的分割算法，在小节（bar）粒度上做音乐结构分析 [6]。**热度证据**：> 待核实；**权威证据**：arXiv 预印本（2023，v1）[6]；**关注度**：中；**推荐度**：★★★★☆ 音乐结构分割是 MIR 中与生成/编辑强耦合的模块 [6]。

### 2.3 多模态 MIR

- **Towards Multimodal MIR**：从音乐诱发的**人体动作**预测个体差异，把 MIR 从「音频→标签」扩展到「音频 + 动作→个体属性」的多模态设定 [7]。**热度证据**：> 待核实；**权威证据**：arXiv 预印本（2020，v1）[7]；**关注度**：低到中（属较早的多模态探索线）；**推荐度**：★★★☆☆ 对做音乐—身体交互、多模态 MIR 的读者有参考价值 [7]。

### 2.4 翻唱识别（Cover Song Identification, CSI）

> **待核实**：本次 34 条候选来源中**没有任何一条**对应翻唱识别（CSI）任务，也无 chord/beat tracking 的专门文献。本小节因此无法给出可核查论断。
> 建议后续补齐方向：CSI 的经典评测集（如 covers80、Da-TACOS、SHS100K）与 2015–2024 年间的 chroma/DTW 系与深度嵌入系工作，需通过新的 arXiv/OpenAlex 检索获得，**不得凭记忆写入本报告**。

### 2.5 节拍与和声

> **待核实**：节拍跟踪（beat tracking）、和弦识别（chord recognition）、调性分析（key estimation）在本次有效来源中没有直接对应文献。可间接关联者仅为 [5]（特征提取库）与 [6]（结构分割，可能隐含节拍/和声线索），不足以支撑独立论断。

### 2.6 学科动向

- **ISMIR 2025 会议报告**（第 26 届国际音乐信息检索学会会议）作为学科年度综述性文献存在 [11]。**热度证据**：`citations=0`（候选块实测值，非推测）[11]；**权威证据**：发表于 *Journal of Music and Theory*（DOI 10.36364/jmt.45.6）[11]；**关注度**：低（citations=0，且为会议报告体裁）[11]；**推荐度**：★★★☆☆ 可作为了解 ISMIR 2025 议题分布的入口，但属二手综述而非一手方法论文 [11]。

---

## 三、音乐生成（文本 / 符号 / 音频）

### 3.1 文本到音乐（Text-to-Music, TTM）

- **ACE-Step（2025）**：开源音乐生成基础模型，宣称通过整体架构设计克服现有方法的固有权衡（生成速度 vs 音乐连贯性），达到 SOTA [13]。**热度证据**：> 待核实；**权威证据**：arXiv `cs.SD` 预印本（2506.00045v1），非同行评审 [13]；**关注度**：中（「foundation model + open source」的定位具备吸引力）；**推荐度**：★★★★☆ 当前开源 TTM 基础模型的直接候选，但 SOTA 声明未经第三方验证 [13]。
- **Instrumental Text-to-Music Generation with Auxiliary Conditioning Branches（2026）**：指出当前 TTM 进展多依赖大规模训练数据与外部预训练，导致难以隔离设计选择的影响，用辅助条件分支做受控研究 [18]。**热度证据**：> 待核实；**权威证据**：arXiv `cs.SD` 预印本（2605.21433v1）[18]；**关注度**：中；**推荐度**：★★★★☆ 方法论价值突出，适合作为「归因分析」范本 [18]。
- **MusicLM（2023）**：文本到音乐生成的开创性工作之一 [9]。**热度证据**：> 待核实；**权威证据**：arXiv 预印本（2301.11325v1），Google Research [9]；**关注度**：高（作为 TTM 奠基工作被广泛引用，具体引用数本次未取得）；**推荐度**：★★★★★ TTM 方向必读起点 [9]。详见第六章。
- **MusicGen**：Meta 的可控音乐生成工作（NeurIPS 2023），见种子资源清单，**本次未获得对应编号引用**，热度与引用数 `> 待核实`。
- **Instruct-MusicGen（2024）**：通过指令微调解锁音乐语言模型的文本到音乐编辑能力 [10]。**热度证据**：> 待核实；**权威证据**：arXiv 预印本（2405.18386v3）[10]；**关注度**：中高；**推荐度**：★★★★☆ 音乐编辑任务的关键参考 [10]。
- **Audio Prompt Adapter（2024）**：以轻量微调为文本到音乐模型释放音乐编辑能力 [14]。**热度证据**：> 待核实；**权威证据**：arXiv 预印本（2407.16564v2）[14]；**关注度**：中；**推荐度**：★★★★☆ 工程上更易落地 [14]。

### 3.2 文本到音频 / 音效（Text-to-Audio）

- **IMPACT（2025）**：指出基于扩散的 Tango / AudioLDM 系列虽保真度高但推理开销显著，提出迭代掩码并行解码 [16]。**热度证据**：> 待核实；**权威证据**：arXiv `eess.AS` 预印本（2506.00736v1）[16]；**关注度**：中高；**推荐度**：★★★★☆ 面向推理效率的明确改进路线 [16]。
- **EzAudio（Interspeech 2025）**：高效扩散 Transformer 用于文本到音频生成 [21]。**热度证据**：> 待核实；**权威证据**：**Interspeech 2025（同行评审，DOI 10.21437/interspeech.2025-1137）**——本批来源中权威等级最高者之一 [21]；**关注度**：中高；**推荐度**：★★★★☆ 若只读一篇文本到音频工程论文，优先此篇 [21]。
- **Stable Audio Open（2024）**：开源音频生成模型 [17]。**热度证据**：> 待核实；**权威证据**：arXiv 预印本（2407.14358v2）[17]；**关注度**：中高；**推荐度**：★★★★☆ 开源基线常用起点 [17]。
- **Fast Timing-Conditioned Latent Audio Diffusion（2024）**：潜空间音频扩散的时序条件化与快速采样 [20]。**热度证据**：> 待核实；**权威证据**：arXiv 预印本（2402.04825v3）[20]；**关注度**：中；**推荐度**：★★★★☆ 与 [17] 同属潜扩散主线 [20]。

### 3.3 符号音乐生成与可控生成

- **Music SketchNet（2020）**：通过音高与节奏的因子化表征实现可控音乐生成 [8]。**热度证据**：> 待核实；**权威证据**：arXiv 预印本（2008.01291v1）[8]；**关注度**：中（因子化可控生成是后续大量工作的思想来源）；**推荐度**：★★★★☆ 可控生成的思想源头之一 [8]。
- **A Functional Taxonomy of Music Generation Systems（2018）**：音乐生成系统的功能分类学，是建立分类骨架的综述性工作 [4]。**热度证据**：> 待核实；**权威证据**：arXiv 预印本（1812.04186v1）[4]；**关注度**：中高（taxonomy 类文献长尾引用）；**推荐度**：★★★★☆ 用于组织本领域分类体系，但需注意其时效已超 2 年，未覆盖基础模型时代 [4]。

### 3.4 音频修复 / 补全（Inpainting）

- **Diffusion-Based Audio Inpainting（2023）** 与 **Learning to Traverse Latent Spaces for Musical Score Inpainting（2019）** 分别代表音频域与符号乐谱域的补全工作 [19][1]。**热度证据**：均 > 待核实；**权威证据**：[19] arXiv 预印本（2305.15266v3）[19]，[1] arXiv `cs.LG` 预印本（1907.01164v1）[1]；**关注度**：中；**推荐度**：[19] ★★★★☆（扩散用于音频修复的代表）[19]，[1] ★★★☆☆（较早的交互式创作视角）[1]。

---

## 四、音乐理解与自监督表征

### 4.1 跨文化音乐理解（本批来源中最突出的新方向）

- **GlobalMood（2025）**：指出音乐情绪的人工标注对音乐生成与推荐系统至关重要，但既有数据集以西方歌曲与英文术语为主，可能限制跨语言、跨文化泛化；为此提出跨文化音乐情绪识别基准 GlobalMood [2]。**热度证据**：> 待核实；**权威证据**：arXiv `cs.IR` 预印本（2505.09539v2）[2]；**关注度**：中高（文化偏差是当前明确热点）；**推荐度**：★★★★☆ 音乐情绪识别与跨文化评估的首选基准候选 [2]。
- **CultureMERT（2025）**：面向跨文化音乐表征学习的持续预训练方法 [22]。**热度证据**：> 待核实；**权威证据**：arXiv 预印本（2506.17818v1）[22]；**关注度**：中高；**推荐度**：★★★★☆ 与 [2] 构成「基准 + 表征」的配套阅读组合 [22]。
- **Sanidha（2025）**：面向 Carnatic 音乐的工作室级多模态数据集 [30]。**热度证据**：> 待核实；**权威证据**：arXiv 预印本（2501.06959v1）[30]；**关注度**：中；**推荐度**：★★★☆☆ 非西方音乐数据稀缺，作为数据资源有价值 [30]。

### 4.2 自监督音频/音乐表征

> **待核实**：本批有效来源中，**没有**自监督音频表征的奠基性工作（如对比学习式音频-文本预训练、掩码建模式音乐 Transformer 预训练）的原始论文。唯一直接对应者为 CultureMERT [22]，属在既有音乐表征模型上做持续预训练，而非提出新预训练范式。因此本章无法给出「自监督表征奠基工作」的可核查清单，需后续专项检索补齐。

### 4.3 音乐结构理解

- 小节级结构分析见 [6]（Correlation Block-Matching 分割）[6]；符号音乐分类中的表征选择问题见 [3][3]。二者共同构成「结构/表征」这一理解子线。

---

## 五、歌声转换（SVC）与音源分离

### 5.1 歌声转换（Singing Voice Conversion, SVC）

- **DiffSVC（2021）**：用于歌声转换的

## 参考来源

[1] Learning to Traverse Latent Spaces for Musical Score Inpainting — http://arxiv.org/abs/1907.01164v1
[2] GlobalMood: A cross-cultural benchmark for music emotion recognition — http://arxiv.org/abs/2505.09539v2
[3] Symbolic Music Representations for Classification Tasks: A Systematic Evaluation — http://arxiv.org/abs/2309.02567v2
[4] A Functional Taxonomy of Music Generation Systems — http://arxiv.org/abs/1812.04186v1
[5] MIRFLEX: Music Information Retrieval Feature Library for Extraction — http://arxiv.org/abs/2411.00469v1
[6] Barwise Music Structure Analysis with the Correlation Block-Matching Segmentation Algorithm — http://arxiv.org/abs/2311.18604v1
[7] Towards Multimodal MIR: Predicting individual differences from music-induced movement — http://arxiv.org/abs/2007.10695v1
[8] Music SketchNet: Controllable Music Generation via Factorized Representations of Pitch and Rhythm — http://arxiv.org/abs/2008.01291v1
[9] MusicLM: Generating Music From Text — http://arxiv.org/abs/2301.11325v1
[10] Instruct-MusicGen: Unlocking Text-to-Music Editing for Music Language Models via Instruction Tuning — http://arxiv.org/abs/2405.18386v3
[11] Conference Report: The 26th International Society for Music Information Retrieval Conference (ISMIR 2025) — https://doi.org/10.36364/jmt.45.6
[12] This paper has been withdrawn — http://arxiv.org/abs/cond-mat/0309395v2
[13] ACE-Step: A Step Towards Music Generation Foundation Model — http://arxiv.org/abs/2506.00045v1
[14] Audio Prompt Adapter: Unleashing Music Editing Abilities for Text-to-Music with Lightweight Finetuning — http://arxiv.org/abs/2407.16564v2
[15] Baseline Systems For The 2025 Low-Resource Audio Codec Challenge — http://arxiv.org/abs/2510.00264v3
[16] IMPACT: Iterative Mask-based Parallel Decoding for Text-to-Audio Generation with Diffusion Modeling — http://arxiv.org/abs/2506.00736v1
[17] Stable Audio Open — http://arxiv.org/abs/2407.14358v2
[18] Instrumental Text-to-Music Generation with Auxiliary Conditioning Branches — http://arxiv.org/abs/2605.21433v1
[19] Diffusion-Based Audio Inpainting — http://arxiv.org/abs/2305.15266v3
[20] Fast Timing-Conditioned Latent Audio Diffusion — http://arxiv.org/abs/2402.04825v3
[21] EzAudio: Enhancing Text-to-Audio Generation with Efficient Diffusion Transformer — https://doi.org/10.21437/interspeech.2025-1137
[22] CultureMERT: Continual Pre-Training for Cross-Cultural Music Representation Learning — http://arxiv.org/abs/2506.17818v1
[23] The Whole Is Greater than the Sum of Its Parts: Improving Music Source Separation by Bridging Network — http://arxiv.org/abs/2305.07855v2
[24] Mel-Band RoFormer for Music Source Separation — http://arxiv.org/abs/2310.01809v1
[25] Music Source Separation with Band-Split RoPE Transformer — http://arxiv.org/abs/2309.02612v2
[26] Multi-Stage Music Source Restoration with BandSplit-RoFormer Separation and HiFi++ GAN — http://arxiv.org/abs/2603.04032v1
[27] End-to-end music source separation: is it possible in the waveform domain? — http://arxiv.org/abs/1810.12187v2
[28] Improving Choral Music Separation through Expressive Synthesized Data from Sampled Instruments — http://arxiv.org/abs/2209.02871v1
[29] Mel-RoFormer for Vocal Separation and Vocal Melody Transcription — http://arxiv.org/abs/2409.04702v1
[30] Sanidha: A Studio Quality Multi-Modal Dataset for Carnatic Music — http://arxiv.org/abs/2501.06959v1
[31] GitHub  · Change is constant.  GitHub  keeps you ahead. — https://github.com/
[32] Sign in to  GitHub  ·  GitHub — https://github.com/login
[33] GitHub 中文社区 — https://github.tw.cn/
[34] DiffSVC: A Diffusion Probabilistic Model for Singing Voice Conversion — http://arxiv.org/abs/2105.13871v1


---

*Generated by research-bot · topic=`music-audio` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading · model=`deepseek-v4-flash` · sources=34 · duration=163s · 2026-10-02T10:50:49+00:00*
