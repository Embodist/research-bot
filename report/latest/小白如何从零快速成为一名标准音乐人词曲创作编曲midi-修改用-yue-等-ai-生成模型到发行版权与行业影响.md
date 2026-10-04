# 从零到「标准音乐人」：词曲创作、编曲与 MIDI 修改、AI 生成（YuE/Suno 类）到发行与版权的可核查学习路径调研报告

> **日期**：2026-10-04（UTC）｜**领域**：音乐创作教育 · AI 音乐生成（Music Generation）· 音乐产业与版权｜**检索源**：候选证据库共 126 条编号来源，本报告实际引用约 80 条（见文末「参考来源」）｜**方法论**：deep-research 四阶段 + paper-survey 论文图谱 + frontier-tracking 时间线 + evidence-grading 四级评分 + knowledge-framework 七维 facet
>
> **证据纪律声明**：本报告严格只引用给定候选库中真实存在的编号 [1]–[126]，不新增、不编造编号与 URL。凡候选库未提供引用数 / star / 下载量者，一律写 `> 待核实`。音乐产业中存在大量与音频检索术语同名的干扰文献（如 [82] 为抗生素局部灌注的 "CLAP"、[86] 为 IMF 财政部门的 "FAD"），本报告**不采用**这些来源支撑任何音频指标论断，并在第 5 章单列说明。

---

## 1. 定位与背景（Positioning）

### 1.1 定义：什么是「标准音乐人」，什么**不是**

**结论**：在检索范围内，**不存在**一个被行业或学界普遍承认的「标准音乐人」认证或等级标准。可核查的做法是把「标准音乐人」还原为一个**能力集合 + 交付物集合**，而非一个头衔。

- [Convention] 「标准」在此应理解为**可交付**（deliverable-ready）而非**可认证**：能否独立产出一首结构完整、混音成型、权利清晰、可上架的录音作品。候选库中**没有任何**来源定义或认证「标准音乐人」这一称谓 → `> 待核实`。
- [F] 「音乐能力」的可教授部分在学理上被拆为**和声（Harmony）、节奏（Rhythm）、旋律（Melody）、曲式（Form）**四大模块，并被系统化为商业歌曲写作教材 [38][36][41]。
- [F] 「歌曲写作」作为独立教学单元，在流行音乐教育学中与即兴（Improvisation）、编曲（Arranging）并列为三个既分叉又耦合的能力域 [28]；针对零基础的入门层有专门的工作坊式材料 [34][42]。

**它不是什么**（避免新手误判）：

| 常见误判 | 实际情况 | 证据 |
|---|---|---|
| 「音乐人 = 会用 AI 生成一首歌」 | AI 系统被宣传为「音乐创作民主化」，但研究指出这类宣传掩盖了系统性偏差与「包容性作为营销」的问题 | [105] |
| 「AI 生成 = 无需乐理」 | 可控生成的**控制信号本身**就是乐理概念（和弦、节奏、结构），不会乐理就无法下达有效控制 | [55][62][65] |
| 「会 DAW 就是会制作」 | MIDI 表示、音符事件、通道/音色映射是可独立学习的工程层技能 | [59][50][53] |

### 1.2 它为何存在：需求侧的三个驱动力

- [E] **生成能力过剩、判断力稀缺**：文本到音乐/歌曲生成已能在歌词到整歌（lyrics-to-song）任务上输出数分钟级成品 [4]，因此竞争力的重心从「能不能生成」转移到「能不能筛选、修改、判断」。
- [E] **控制粒度成为新分水岭**：研究明确指出「多数系统无法建模歌曲随时间的属性变化，严重限制了对结构与动态的细粒度控制」[9]；符号域的可控生成（和弦条件、节奏条件）已有系统化对比 [55][62]。
- [E] **权利与合规成为发行前置条件**：生成式 AI 的版权与供应链问题被系统性讨论 [110][111][114]，去学习（unlearning）被提出作为「退出机制」[102]。

### 1.3 前置知识链（有序，缺一环即需回补）

```text
听觉与节奏感
  → 基础乐理（音阶/音程/调性）
    → 和声功能（级数、终止、转调、调式互换）[29][35][40]
      → 曲式与歌曲结构（verse/chorus/bridge）[38][41]
        → 词曲创作（韵律、音节数、情绪曲线）[42][18][2]
          → DAW + MIDI 事件操作 [59][61][63]
            → 编曲/配器（多轨、音色、织体）[28]
              → AI 生成与后编辑（提示词/条件控制/inpainting）[4][26][52]
                → 混音/母带（本报告检索缺口，见 1.4）
                  → 发行、权利与合规 [110][111][114]
```

**前置知识性质标记**：
- [P] 和声功能与调式关系是**原理性**知识，可形式化讲授 [29]（但 [29] 自身对「音乐的科学理论」持探索性立场，属 [Debated]）。
- [Convention] 歌曲结构模板（主歌-副歌-桥段）是**行业约定**而非自然律，教材层面高度标准化 [38][41]。
- [Heuristic] 「先写副歌再补主歌」等创作顺序是经验规则，非普适。
- [Unknown] 混音与母带（Mixing/Mastering）的可核查学术来源在本次候选库中**基本缺失** → `> 待核实`（检索缺口，见 1.4）。

### 1.4 检索缺口（诚实标注）

| 缺口 | 说明 |
|---|---|
| 混音/母带（Mixing / Mastering） | 候选库无对应来源 → `> 待核实` |
| DAW 具体操作（Ableton / Logic / FL Studio） | 仅有 MIDI 概念的书籍章节 [59][61][63]，无 DAW 软件层来源 → `> 待核实` |
| 美国版权局（U.S. Copyright Office）与中国生成式 AI 法规原文 | 候选库无官方文件 → `> 待核实` |
| 发行聚合商（DistroKid / TuneCore 等） | 候选库无来源 → `> 待核实` |

---

## 2. 问题域（Problem Space）

### 2.1 核心问题（一句话）

**如何把一个模糊的音乐意图，转化为一首结构完整、控制可解释、权利可追溯、可上架发行的录音作品。**

### 2.2 问题的形式化表述

```text
目标：Song = Render(Structure, Lyrics, Melody, Harmony, Arrangement, Timbre, Mix)
约束：
  C1 结构约束：Song ∈ 合法曲式模板空间（含段落顺序与时长的合理分布）[38][41][9]
  C2 和声约束：Harmony 满足调性/功能进行规则（可被违规，但违规需自觉）[29][35][40][60]
  C3 韵律约束：Lyrics 的音节数与重音须与 Melody 的音符时值对齐 [18][14]
  C4 时长约束：主流开源模型的上限约 5 分钟（YuE 生成至多约五分钟）[4]
  C5 权利约束：训练数据来源、生成物可版权性、平台政策 [110][111][114][102]
  C6 算力约束：长序列生成的计算复杂度（自注意力二次复杂度限制可扩展性）[49]
```

### 2.3 关键约束与不变量

- [P] **结构不变量**：商业歌曲的和声、节奏、旋律、曲式四维可被独立建模与教学 [38][36][41]；符号域研究进一步把「动机（Motif）—乐句（Phrase）—更大结构」视为结构建模的层级 [54]。
- [P] **可控性不变量**：控制信号越细粒度，可控性越强，但对生成模型的时序建模能力要求越高 [9][62]。
- [Convention] **歌词-旋律对齐**：音节数控制被作为整歌歌词生成的显式约束条件 [18]；条件式歌词到旋律生成（CSL-L2M）把细粒度歌词与音乐控制显式建模 [14]。
- [Debated] **「和弦条件是必要还是可选」**：和弦条件的旋律/低音生成被系统对比（含无和弦条件基线）[55]，说明该约束的价值依任务而变，尚无统一定论。

### 2.4 零基础者的真实问题树（主干）

```text
主干：从零到可发行
├─ 子问题 A：我听不出好坏 → 听觉训练与参照系缺失
├─ 子问题 B：我写不出「完整的一首」→ 曲式与段落意识缺失 [38][41][9]
├─ 子问题 C：会用 AI 但改不动 → MIDI 事件层与符号表示不熟 [59][50][53][51]
├─ 子问题 D：改得动但不好听 → 和声/织体/音色选择能力不足 [55][65][28]
├─ 子问题 E：好听但不敢发 → 权利链与平台政策不清 [110][111][114][102]
└─ 叶节点（尚未解决）：评测指标与「人类可发行判断」的缺口 [78][76]
```

### 2.5 术语中英对照（关键）

| 中文 | 英文 | 说明 |
|---|---|---|
| 歌词到歌 | lyrics-to-song | 最具挑战性的整曲生成任务 [4] |
| 符号音乐 | symbolic music | 以 MIDI/乐谱等离散事件表示的音乐 [51][76] |
| 分轨 | stem separation / source separation | 从混音中分离人声/伴奏等 [70][44] |
| 补全 | inpainting / infilling | 填补缺失或指定区段 [26] |
| 分词化 | tokenization | 把 MIDI 离散化为模型可读 token [53][50] |
| 音节数控制 | syllable count control | 歌词生成的结构约束 [18] |
| 去学习 | unlearning | 让模型「遗忘」特定受版权保护内容 [102] |

---

## 3. 历史与演进（Evolution）

> **代际组织原则**：每一代写「解决了什么」，并**必须**写「新引入了什么代价/问题」。

### 第 1 代：手工与乐理规范化时代（前 AI）
**解决**：把音乐创作中可传授的部分系统化——和声功能、调式、平行小调、曲式被教材化 [29][35][40][38]。
**代价/新问题**：教材体系以西方商业流行音乐为中心，跨文化适用性受限；后续研究明确指出现有数据集「以西方歌曲为主、术语源自英语，可能限制跨语言跨文化泛化」[47][73]。

### 第 2 代：规则/统计式生成系统
**解决**：把「音乐生成」本身当作工程问题，形成功能分类法（functional taxonomy）[16]；早期歌曲写作系统尝试预训练 + 对齐约束 [87]。
**代价/新问题**：可控性弱、长程结构弱；评测体系缺失。

### 第 3 代：神经网络符号音乐生成
**解决**：引入神经网络处理符号域——可控音乐生成通过**音高与节奏的因子化表示**实现 [27]；旋律和声化用 Orderless NADE + 和弦平衡 + 分块 Gibbs 采样 [58]；和弦条件化和声化并支持可控制和声度 [60]；层次化音乐结构表示支持可控旋律生成 [56]。
**代价/新问题**：模型规模小、泛化弱；**表示法本身**成为性能瓶颈——符号音乐表示对分类任务的影响被系统性评估 [51]，byte-pair encoding 被引入符号音乐分词 [53]。

### 第 4 代：Transformer / 扩散 + 文本条件（音频域）
**解决**：文本到音乐（text-to-music）成为主流任务，MusiConGen 加入**节奏与和弦控制** [62]；LLM 被适配做多轨文本到 MIDI（MIDI-LLM 两阶段训练：单模态继续预训练 + 任务微调）[52]；扩散 + 结构化状态空间模型（SSM）用于长序列符号生成以规避二次复杂度 [49]。
**代价/新问题**：**评测与人类听感脱节**——生成音乐感知质量评估依赖 CLAP 类嵌入，其有效性被质疑并提出自监督替代方案 [78]。

### 第 5 代：全长歌曲与开源基础模型（2025—）
**解决**：全长歌曲（full-length song）与歌词到歌成为明确前沿。DiffRhythm 提出「极快且极为简单」的端到端全长歌曲潜在扩散方案 [23]；YuE 用 LLaMA2 架构扩展到万亿 token 级、生成至多约五分钟并保持歌词对齐 [4]；ACE-Step 走向音乐生成基础模型 [19]，并演进到 ACE-Step 1.5 [21]；DiffRhythm+ 引入偏好优化强化可控性 [17]。
**代价/新问题**：
- 可控性与音质的张力仍未解——SegTune 指出「多数系统无法建模随时间的属性变化」[9]；
- 结构可控性被进一步拆解：Segmented Full-Song Model 需要用户提供歌曲结构或种子片段 [11]；
- **权利与伦理代价浮现**：去学习作为退出机制 [102]、音乐 AI 系统的嵌入意识形态 [105]、公平性重审 [106]、论文伦理声明有效性 [107]、随机性与共创 [109]。

### 第 6 代（进行中）：细颗粒度控制与跨模态
**解决**：视觉到音乐生成形成综述 [10]；器乐文本到音乐引入辅助条件分支 [13]；可控音乐循环生成结合 MIDI + 文本、多阶段交叉注意力与乐器感知强化学习 [68]；文本可控复调符号音乐生成 [69]；情绪对齐的文本到 MIDI（Story2MIDI）[12]。
**代价/新问题**：任务碎片化、指标不统一，benchmark 建设滞后于模型发布（见第 5 章）。

---

## 4. 核心机制（Mechanism）

### 4.1 乐理层机制

- [P] **功能和声**：以调内级数与功能推进组织时间，是商业歌曲写作的核心骨架 [38][41]；调式（modal）与平行小调关系是重要扩展 [35][40]。
- [Debated] [29] 主张把和声解释推向「音乐的科学理论」，但该方向仍在进展中，**不应视作已确立的定论**。
- [P] **结构层级**：动机—乐句—更大段落被作为符号生成的结构建模对象 [54]；这正是「AI 写的东西为什么不完整」的第一性原因。

### 4.2 词曲创作机制

- [F] 歌词生成可引入**整歌形式感知 + 多粒度音节数控制** [18]；条件式歌词到旋律生成把细粒度歌词与音乐控制显式绑定 [14]。
- [E] 歌词的情绪动态可被状态空间模型建模 [2]，说明「情绪曲线」是可工程化的创作变量。
- [E] 歌词自动转写（lyrics transcription）在复调音乐上仍困难，被单独作为任务研究 [1]。

### 4.3 MIDI 与符号表示机制（小白最常被卡的一层）

| 机制 | 说明 | 边界/反例 | 证据 |
|---|---|---|---|
| MIDI 事件模型 | 音符事件、时值、通道、音色是可编辑的最小单位 | 编辑粒度越细，工程耗时越大 | [59][61][63] |
| 分词化 | 把 MIDI 离散为 token 供序列模型使用（含 BPE 方案） | 不同分词方案对结果影响显著 | [53][50] |
| 表示法选择 | 符号音乐表示对下游分类任务有系统性影响 | 「哪种表示最好」依任务而定，无普适答案 | [51][76] |
| 可视化/分析 | MidiTok Visualizer 用于分词结果可视化与分析 | 属工具层，不直接提升生成质量 | [50] |
| 特征提取 | musif 提供 Python 符号音乐特征提取 | 特征与音乐语义的映射并非自动成立 | [45] |

> **边界说明**：以上机制在**符号域**适用；一旦目标是有音色、有混音的**音频成品**，就必须跨到音频生成/分轨层，符号域的控制力不能直接迁移 → `> 边界待核实`（候选库无直接对比研究）。

### 4.4 可控生成机制

- [P] **和弦条件**：和弦条件化旋律与低音生成有五类 Transformer 策略对比（无和弦条件 / 独立线条件 / 等）[55]；和弦感知符号生成可用多轨 Transformer + MusicBERT 组合（MMT-BERT）[65]。
- [P] **节奏 + 和弦联合控制**：MusiConGen 把节奏与和弦作为 transformer 文本到音乐的可控条件 [62]。
- [P] **区段补全**：乐谱 inpainting 用「同时看过去与未来上下文」的深度模型实现 [26]。
- [P] **多轨文本到 MIDI**：通过扩展 LLM 词表纳入 MIDI token + 两阶段训练实现 [52]。
- [P] **MIDI + 文本双模控制**：多阶段交叉注意力 + 乐器感知强化学习用于可控音乐循环生成 [68]。
- [P] **长序列可扩展性**：扩散 + 结构化状态空间模型降低二次复杂度约束 [49]；Mamba-扩散 + 可学习小波用于可控符号生成 [67]。

### 4.5 分轨与后期修改机制

- [E] 端到端波形域音乐源分离已被系统研究 [70]；合唱音乐分离可通过采样乐器合成数据增强 [44]。
- **适用边界**：分轨质量与源信号复杂度强相关（合唱/复调场景显著更难 [44]）；分离后的音轨是**近似**而非原轨。
- **失败模式**：把分离轨当作「原始分轨」再处理，会累积伪影 → `> 边界待核实`（候选库无量化伪影传播研究）。

### 4.6 整曲生成的机制难点（用以解释「为什么 AI 出的歌常常不完整」）

1. **长程一致性**：需要在分钟级时间尺度维持调性、主题、音色的一致，而自注意力有二次复杂度上限 [49]。
2. **歌词-人声对齐**：YuE 明确把「歌词到歌」列为最具挑战的任务并强调保持对齐 [4]。
3. **时序变化的细粒度属性**：多数系统不建模随时间变化的属性，导致结构/动态控制弱 [9]。
4. **算力-质量权衡**：DiffRhythm 以「极快」为目标 [23]，其代价是需要 DiffRhythm+ 用偏好优化补回可控性 [17]。

### 4.7 评测机制

- [E] 感知质量评测长期依赖 **CLAP** 类音频-文本嵌入，ConvM2D2 明确质疑该做法并提出自监督替代 [78]；M2D-CLAP 探索超越 CLAP 的通用音频-语言表示 [71]。
- [E] 跨文化情绪标注基准 GlobalMood 指出既有数据集以西方歌曲为主 [47]；CultureMERT 用持续预训练提升跨文化音乐表示 [73]。
- **适用边界**：这些指标测的是**表示/嵌入空间的相似性**，与「是否可发行」之间没有已建立的映射 → `> 待核实`。

---

## 5. 证据与评估（Evaluation）

### 5.1 指标层级与「可发行」的缺口

| 层级 | 代表指标/方法 | 它测什么 | 能否代表「可发行」 | 证据 |
|---|---|---|---|---|
| 嵌入相似度 | CLAP 类对比音频-文本 | 音频与文本描述的一致性 | **否**（有效性受质疑） | [78][71] |
| 情绪/语义标注 | 跨文化情绪基准 | 人类情绪标注一致性 | 部分（情绪维度） | [47] |
| 转写精度 | AMT Challenge（多乐器转写） | 音符/乐器还原精度 | 否（属分析任务） | [72] |
| 表示质量 | SyMuRBench | 符号表示的基准对比 | 否（属表示层） | [76] |
| 描述生成 | LP-MusicCaps（LLM 伪标注） | 音乐描述质量 | 否（属描述层） | [79] |
| 跨模态 | MOSA（音乐-动作语义标注） | 跨模态对齐 | 否（属相邻任务） | [81] |
| 数据集质量 | Sanidha（录音室级多模态 Carnatic 音乐） | 非西方音乐的数据覆盖 | 否（属数据层） | [77] |

**核心判断**：在本次检索范围内，**没有任何基准或指标被证明可以直接衡量「可发行水准」** → `> 待核实`。[76][78] 的工作恰恰说明该方向仍在修补中。

### 5.2 「仿真 / 真机」类比：离线指标 vs 人类听感

沿用机器人学的 sim2real 语言，此处存在一个同构的 **metric-to-perception gap**：

- **离线指标**（FAD/CLAP/MOS 代理）≈ 仿真评估
- **人类听感与商业判断** ≈ 真机评估
- [E] ConvM2D2 的动机正是「CLAP 依赖」导致评测不可靠 [78] → 表明 gap 真实存在。
- [Debated] 该 gap 的量级尚无统一结论 → `> 待核实`。

### 5.3 可复现性评估

- 候选库中音乐生成相关来源**绝大多数为 arXiv 预印本**（[4][9][11][12][13][14][17][19][21][23][49][52][55][62][67] 等），**同行评审**来源相对较少（如 [67] 为 IJCNN 2025、[68] 为 ACM Multimedia 系列、[18] 为 Interspeech 2025、[69] 为 ITE Transactions）。
- [E] 唯一在抽取结果中给出非零引用数的音乐相关条目为 [67]（citations=2），其余多为 0 或未提供 → 热度证据普遍缺失，本报告对绝大多数条目写 `> 待核实`。

### 5.4 检索噪声与同名陷阱（负面结果，须显式记录）

本次候选库含若干**术语同名但领域无关**的来源，若误用会直接导致错误结论：

| 编号 | 表面关键词 | 实际领域 | 处理 |
|---|---|---|---|
| [82] | CLAP | 关节置换术后抗生素局部灌注 | **不采用**（非音频 CLAP） |
| [86] | FAD | IMF 财政事务部门文件 | **不采用**（非音频 FAD 指标） |
| [75] | Dataset | 腹部创伤 CT 数据集 | **不采用** |
| [88][89] | SAM | 手术器械分割 | **不采用** |
| [90][91] | 天体 | 大质量恒星 / 变星提取器 | **不采用** |
| [92] | License | 车牌识别 | **不采用** |
| [30] | Curriculum | 量子课程学习 | **不采用** |
| [112] | Copyright | 图像水印篡改定位 | **领域不符**（图像非音乐） |
| [115] | Copyright | 图像生成推理期版权屏蔽 | **领域不符**（可作类比，不可作音乐证据） |

### 5.5 争议与分歧

- [Debated] **AI 是否在「民主化」音乐创作**：一边是被宣传为赋能无音乐背景者 [105]，另一边被指出是「包容性作为营销」并掩盖系统性偏差 [105]；公平性议题被重审 [106]。
- [Debated] **版权归属**：生成式 AI 供应链视角 [110]、全生命周期隐私与版权保护 [111]、生成式深度学习中的版权 [114] 给出不同侧重；学术出版场景的类比讨论 [113]。
- [Debated] **模型透明度**：基座模型透明度指数显示各开发方透明度实践仍在演进 [8]，但该指数并非音乐专用 → `> 待核实`。
- [Debated] **随机性的角色**：随机性既能激发新颖性也可能导致不连贯，设计者如何嵌入不确定性被作为专题综述 [109]。

---

## 6. 实践与生态（Practice）

### 6.1 经典与奠基性工作

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Harmony Explained: Progress Towards A Scientific Theory of Music | 2012 | > 待核实 | > 待核实 | arXiv（math/CS 交叉）[29] | 低（引用数未提供） | ★★★☆☆ | http://arxiv.org/abs/1202.4212v2 | 试图把和声解释理论化；立场探索性，属 [Debated] |
| A Functional Taxonomy of Music Generation Systems | 2018 | > 待核实 | > 待核实 | arXiv [16] | 中（领域综述常见引用位） | ★★★★☆ | http://arxiv.org/abs/1812.04186v1 | 音乐生成系统的功能分类骨架，用于建立领域地图 |
| Working with MIDI | — | > 待核实 | > 待核实 | 书籍章节（Routledge）[59] | > 待核实 | ★★★★☆ | https://doi.org/10.4324/9780080926865-9 | MIDI 工作流的教材级入口；另有 [61][63] 同类章节 |
| SongMASS: Automatic Song Writing with Pre-training and Alignment Constraint | 2020 | > 待核实 | > 待核实 | arXiv [87] | 中（早期歌曲写作代表作） | ★★★★☆ | http://arxiv.org/abs/2012.05168v1 | 预训练 + 对齐约束的早期整歌写作方案 |
| Music SketchNet: Controllable Music Generation via Factorized Representations of Pitch and Rhythm | 2020 | > 待核实 | > 待核实 | arXiv [27] | 中 | ★★★★☆ | http://arxiv.org/abs/2008.01291v1 | 音高/节奏因子化 = 可控性机制的早期范式 |
| Melody Harmonization Using Orderless NADE, Chord Balancing, and Blocked Gibbs Sampling | 2020 | > 待核实 | > 待核实 | arXiv [58] | 中 | ★★★☆☆ | http://arxiv.org/abs/2010.13468v2 | 和弦平衡 + 分块采样的和声化经典路线 |
| Symbolic Music Representations for Classification Tasks: A Systematic Evaluation | 2023 | > 待核实 | > 待核实 | arXiv [51] | 中 | ★★★★☆ | http://arxiv.org/abs/2309.02567v2 | 证明「表示法选择」本身是性能变量 |
| Byte Pair Encoding for Symbolic Music | 2023 | > 待核实 | > 待核实 | arXiv [53] | 中 | ★★★★☆ | http://arxiv.org/abs/2301.11975v3 | 把 BPE 引入符号音乐分词，是 MIDI-LLM 路线的前置 |
| The Practice of Popular Music（教材 + 两篇书评） | 2025 | Trevor de Clercq / Routledge | 书评 citations=0 [36] | Routledge 出版；书评见 Journal of Music Theory Pedagogy [36]、Music Theory Online [41] | 低（书评为新） | ★★★★☆ | https://doi.org/10.4324/9781003331155 | 商业歌曲写作的和声/节奏/旋律/曲式四模块系统教材 [38][36][41] |
| Motifs, Phrases, and Beyond: The Modelling of Structure in Symbolic Music Generation | 2024 | > 待核实 | > 待核实 | arXiv [54] | > 待核实 | ★★★★☆ | http://arxiv.org/abs/2403.07995v1 | 结构建模的层级视角，解释「AI 歌不完整」 |

### 6.2 最新进展（近 1–2 年，2024–2026）与经典工作严格分节

**最新进展（2024–2026）**

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| **YuE: Scaling Open Foundation Models for Long-Form Music Generation** | 2025 | > 待核实 | > 待核实 | arXiv（eess.AS）[4] | 中–高（开源整歌基础模型话题度高，引用数待核实） | ★★★★★ | http://arxiv.org/abs/2503.08638v2 | 基于 LLaMA2 架构、扩展到万亿 token、生成至多约五分钟并保持歌词对齐；本主题的**核心开源对象** |
| ACE-Step: A Step Towards Music Generation Foundation Model | 2025 | > 待核实 | > 待核实 | arXiv [19] | 中 | ★★★★☆ | http://arxiv.org/abs/2506.00045v1 | 开源音乐生成基础模型路线的代表 |
| ACE-Step 1.5: Pushing the Boundaries of Open-Source Music Generation | 2026 | > 待核实 | > 待核实 | arXiv [21] | > 待核实 | ★★★★☆ | http://arxiv.org/abs/2602.00744v3 | 同一路线的迭代；版本号与能力声明以官方仓库为准 → `> 待核实` |
| DiffRhythm: Blazingly Fast and Embarrassingly Simple End-to-End Full-Length Song Generation with Latent Diffusion | 2025 | > 待核实 | > 待核实 | arXiv [23] | 中 | ★★★★☆ | http://arxiv.org/abs/2503.01183v1 | 潜在扩散做全长歌曲，主打速度与简洁 |
| DiffRhythm+: Controllable and Flexible Full-Length Song Generation with Preference Optimization | 2025 | > 待核实 | > 待核实 | arXiv [17] | > 待核实 | ★★★★☆ | http://arxiv.org/abs/2507.12890v2 | 用偏好优化补回可控性——「速度路线的代价」的解法 |
| SegTune: Structured and Fine-Grained Control for Song Generation | 2026 | > 待核实 | > 待核实 | arXiv [9] | > 待核实 | ★★★★☆ | http://arxiv.org/abs/2606.02638v1 | 直击「系统不建模时序变化属性」的痛点，是可控性前沿 |
| Segment-Factorized Full-Song Generation on Symbolic Piano Music | 2025 | > 待核实 | > 待核实 | arXiv [11] | > 待核实 | ★★★☆☆ | http://arxiv.org/abs/2510.05881v1 | 需要用户给结构/种子段落——把结构控制权交还创作者 |
| MIDI-LLM: Improving Text-to-MIDI Music Generation via Adapting LLMs | 2025 | > 待核实 | > 待核实 | arXiv [52] | > 待核实 | ★★★★★ | http://arxiv.org/abs/2511.03942v2 | 小白做「MIDI 修改 + 生成」最可操作的技术路线（文本→多轨 MIDI） |
| Chord-conditioned Melody and Bass Generation | 2025 | > 待核实 | > 待核实 | arXiv [55] | > 待核实 | ★★★★☆ | http://arxiv.org/abs/2511.08755v1 | 用音乐理论驱动的指标评估五种和弦条件策略 |
| MusiConGen: Rhythm and Chord Control for Transformer-Based Text-to-Music Generation | 2024 | > 待核实 | > 待核实 | arXiv [62] | 中 | ★★★★☆ | http://arxiv.org/abs/2407.15060v1 | 节奏 + 和弦可控的文本到音乐 |
| CSL-L2M: Controllable Song-Level Lyric-to-Melody Generation | 2024 | > 待核实 | > 待核实 | arXiv [14] | > 待核实 | ★★★★☆ | http://arxiv.org/abs/2412.09887v2 | 细粒度歌词 + 音乐双控制 |
| Song Form-aware Full-Song Text-to-Lyrics Generation with Multi-Level Granularity Syllable Count Control | 2025 | > 待核实 | > 待核实 | Interspeech 2025（同行评审）[18] | > 待核实 | ★★★★☆ | https://doi.org/10.21437/interspeech.2025-1247 | 歌词生成的音节数控制——词曲对齐的可操作抓手 |
| Diffusion-based Symbolic Music Generation with Structured State Space Models | 2025 | > 待核实 | > 待核实 | arXiv [49] | > 待核实 | ★★★★☆ | http://arxiv.org/abs/2507.20128v2 | 用 SSM 绕开二次复杂度，长序列符号生成 |
| No Encore: Unlearning as Opt-Out in Music Generation | 2025 | > 待核实 | > 待核实 | arXiv [102] | > 待核实 | ★★★★☆ | http://arxiv.org/abs/2509.06277v2 | 权利冲突的技术侧解——可遗忘机制 |
| Talkin' 'Bout AI Generation: Copyright and the Generative-AI Supply Chain | 2023 | > 待核实 | > 待核实 | arXiv [110] | 中–高 | ★★★★★ | http://arxiv.org/abs/2309.08133v2 | 生成式 AI 供应链的版权分析框架 |
| Copyright in Generative Deep Learning | 2021 | > 待核实 | > 待核实 | arXiv [114] | 中 | ★★★★☆ | http://arxiv.org/abs/2105.09266v5 | 生成式深度学习的版权基础讨论 |

### 6.3 开源项目

| 名称 | 年份 | 机构/作者 | 热度（star/下载） | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| YuE | 2025 | > 待核实 | > 待核实（须查官方仓库实时 star） | arXiv 预印本 [4] | 高（开源自回归整歌生成的代表） | ★★★★★ | http://arxiv.org/abs/2503.08638v2 | lyrics-to-song 开源基础模型；**许可证与权重可得性须查官方仓库** → `> 待核实` |
| ACE-Step | 2025 | > 待核实 | > 待核实 | arXiv [19] | 中–高 | ★★★★☆ | http://arxiv.org/abs/2506.00045v1 | 音乐生成基础模型 |
| ACE-Step 1.5 | 2026 | > 待核实 | > 待核实 | arXiv [21] | > 待核实 | ★★★★☆ | http://arxiv.org/abs/2602.00744v3 | 迭代版本，能力与许可须以官方为准 |
| DiffRhythm | 2025 | > 待核实 | > 待核实 | arXiv [23] | 中 | ★★★★☆ | http://arxiv.org/abs/2503.01183v1 | 快速全长歌曲生成 |
| DiffRhythm+ | 2025 | > 待核实 | > 待核实 | arXiv [17] | > 待核实 | ★★★★☆ | http://arxiv.org/abs/2507.12890v2 | 可控版 |
| MidiTok Visualizer | 2024 | > 待核实 | > 待核实 | arXiv [50] | > 待核实 | ★★★★☆ | http://arxiv.org/abs/2410.20518v1 | MIDI 分词可视化/分析工具，调参必备 |
| musif | 2023 | > 待核实 | > 待核实 | arXiv [45] | > 待核实 | ★★★☆☆ | http://arxiv.org/abs/2307.01120v1 | Python 符号音乐特征提取 |
| Segment-Factorized Full-Song Model (SFS) | 2025 | > 待核实 | > 待核实 | arXiv [11] | > 待核实 | ★★★☆☆ | http://arxiv.org/abs/2510.05881v1 | 结构驱动的符号整曲生成 |

> **许可与合规警示**：候选库中关于开源许可违约的研究（Java 项目代码借用与许可违规分析 [93]、GitHub 许可使用大规模研究 [96]）表明**开源不等于无条件商用**。将 YuE/ACE-Step/DiffRhythm 用于商业发行前，必须逐一核实其代码与**权重**的许可条款 → `> 待核实`（候选库无音乐模型许可原文）。

### 6.4 数据集与基准

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| LP-MusicCaps | 2023 | > 待核实 | > 待核实 | arXiv [79] | 中 | ★★★★☆ | http://arxiv.org/abs/2307.16372v1 | LLM 伪标注音乐描述，文本-音乐对齐评测基础 |
| GlobalMood | 2025 | > 待核实 | > 待核实 | arXiv [47] | > 待核实 | ★★★★☆ | http://arxiv.org/abs/2505.09539v2 | 跨文化音乐情绪基准；明确批评西方中心偏差 |
| 2025 AMT Challenge | 2026 | > 待核实 | > 待核实 | arXiv [72] | > 待核实 | ★★★★☆ | http://arxiv.org/abs/2603.27528v1 | 八队提交、两队超越 MT3 基线——**少见的可对照榜单信息** |
| CultureMERT-95M | 2025 | > 待核实 | > 待核实 | arXiv [73] | > 待核实 | ★★★★☆ | http://arxiv.org/abs/2506.17818v1 | 跨文化音乐表示持续预训练 |
| SyMuRBench | 2025 | > 待核实 | citations=0 | 学术工作坊（ACM 系列）[76] | 低（citations=0） | ★★★☆☆ | https://doi.org/10.1145/3746278.3759392 | 符号音乐表示基准 |
| M2D-CLAP | 2025 | > 待核实 | > 待核实 | arXiv [71] | > 待核实 | ★★★★☆ | http://arxiv.org/abs/2503.22104v2 | 超越 CLAP 的通用音频-语言表示 |
| ConvM2D2 | 2025 | > 待核实 | citations=0 | TechRxiv 预印本 [78] | 低（citations=0） | ★★★★☆ | https://doi.org/10.36227/techrxiv.175614002.20847889/v1 | 批判 CLAP 评测依赖并提出自监督替代 |
| Sanidha | 2025 | > 待核实 | > 待核实 | arXiv [77] | > 待核实 | ★★★☆☆ | http://arxiv.org/abs/2501.06959v1 | 录音室级多模态 Carnatic 音乐数据集 |
| MOSA | 2024 | > 待核实 | > 待核实 | arXiv [81] | > 待核实 | ★★★☆☆ | http://arxiv.org/abs/2406.06375v1 | 音乐-动作语义标注，跨模态 |
| Real-Time Human-Classified Emotional MIDI Dataset | 2024 | > 待核实 | > 待核实 | IEEE ICMLA 2024 [66] | > 待核实 | ★★★☆☆ | https://doi.org/10.1109/icmla61862.2024.00076 | 带人工情绪标注的 MIDI 数据 |

> **指标口径提醒**：候选库中**没有** MusicCaps、MusicBench、SongEval 的直接来源 → `> 待核实`。凡看到第三方转述这些基准的分数，均须回到其官方主页核对口径（任务数、人类评分协议、是否真机/真听感）。

### 6.5 学习路径（面向零基础，[Heuristic]，依据见各行引用）

| 阶段 | 时长 | 目标能力 | 可检验能力点 | 依据 |
|---|---|---|---|---|
| S0 听觉与节奏 | 1–2 周 | 能稳定数拍、分辨段落切换 | 给任意流行歌标出 verse/chorus/bridge 时间点 | [38][41] |
| S1 乐理与和声 | 4–6 周 | 能识别与构造 I–V–vi–IV 类进行 | 听 10 首歌写出级数 | [29][35][40][38] |
| S2 词曲创作 | 4–6 周 | 能写出一段可唱的主歌+副歌 | 产出 1 首含音节数受控歌词的 demo | [42][34][18][2] |
| S3 DAW + MIDI | 6–8 周 | 能手工编辑音符事件、改和弦、换音色 | 对一段 MIDI 做出指定修改并导出 | [59][61][63][50][53] |
| S4 编曲与织体 | 4–6 周 | 能在 4–8 轨上分配功能（低音/和声/旋律/节奏） | 提交多轨编曲工程 | [28][55][65] |
| S5 AI 生成与后编辑 | 4 周 | 能用条件控制生成 + 用 inpainting 修补 | 用和弦/节奏条件生成一段旋律并局部修补 | [4][23][62][55][26][52] |
| S6 分轨与后期 | 2–4 周 | 能做 stem separation 并再加工 | 分离出人声/伴奏并重混 | [70][44] |
| S7 发行与权利 | 持续 | 能说明作品的权利链与平台政策 | 写出一页权利链说明 | [110][111][114][102] |

### 6.6 能力地图（掌握后可做什么）

1. 独立把一段情绪/主题转化为**结构完整的 3–5 分钟歌曲骨架**（[38][41][9]）。
2. 在 MIDI 层**定向修改**任意段落，而非推倒重来（[59][53][50]）。
3. 用**和弦/节奏/结构条件**而非纯文本提示驱动生成（[55][62][11]）。
4. 判断 AI 输出**该保留哪一段**，并用 inpainting 局部修补（[26][9]）。
5. 说清作品的**训练数据来源、生成痕迹、权利归属风险**（[110][111][102]）。

### 6.7 失败知识（新手最容易踩的坑）

| 坑 | 为什么错 | 证据 |
|---|---|---|
| 用纯文本提示生成整歌然后直接发行 | 多数系统不建模时序属性，结构与动态控制薄弱 | [9] |
| 相信 CLAP 类分数 = 好听 | 该指标的有效性被明确质疑 | [78] |
| 把符号域的控制力当成音频域的控制力 | 两域之间无已验证的迁移关系 | `> 待核实` |
| 把分轨结果当原始分轨 | 分离是近似，复调/合唱场景显著更难 | [70][44] |
| 认为「开源 = 可商用」 | 开源许可违规是已被大规模研究的现实问题 | [93][96] |
| 认为 AI 让音乐创作「无门槛」 | 宣传叙事掩盖系统性偏差与包容性营销问题 | [105][106] |
| 引用同名但异领域的术语文献 | 例如把 [82] 的 CLAP、[86] 的 FAD 当作音频指标 | 见 5.4 |

### 6.8 高杠杆压缩

**20 条核心要点**
1. 「标准音乐人」无官方定义，应还原为可交付能力集合（`> 待核实`）。
2. 乐理四模块：和声、节奏、旋律、曲式 [38][36][41]。
3. 歌曲写作与即兴、编曲是三分的教学域 [28]。
4. 零基础有专门的入门材料 [34][42]。
5. 前置链：听觉 → 乐理 → 和声 → 曲式 → 词曲 → DAW/MIDI → 编曲 → AI → 后期 → 发行。
6. MIDI 是最小可编辑单位层 [59][61][63]。
7. 表示法/分词方案本身影响性能 [51][53][76]。
8. 可控性来自条件，而非提示词长度 [55][62][65]。
9. 和弦条件策略已有五方案系统对比 [55]。
10. 节奏 + 和弦联合控制已可行 [62]。
11. 区段补全（inpainting）是核心修改手段 [26]。
12. 文本→多轨 MIDI 可用 LLM 适配实现 [52]。
13. 长序列瓶颈可用 SSM/Mamba 缓解 [49][67]。
14. YuE 是 lyrics-to-song 开源代表，约 5 分钟上限 [4]。
15. DiffRhythm 主打速度，DiffRhythm+ 用偏好优化补可控性 [23][17]。
16. SegTune 指出时序属性建模缺口 [9]。
17. 分轨是近似，复调更难 [70][44]。
18. CLAP 类评测有效性受质疑 [78]，M2D-CLAP 在补位 [71]。
19. 版权需从供应链与生命周期视角看 [110][111][114]。
20. 去学习提供「退出机制」技术侧思路 [102]。

**压缩为 5 条**
1. 先建听觉与乐理地基，再谈工具。
2. MIDI 事件层是你能真正「改得动」AI 输出的地方 [59][52]。
3. 可控性 = 条件信号（和弦/节奏/结构），不是更长的提示词 [55][62][9]。
4. 评测指标不等于好听，更不等于可发行 [78][76]。
5. 发行前必须解决权利链，开源许可与训练数据都要查 [93][110][102]。

**压成 1 句话**
**先练听得出的耳朵，再练改得动的手（MIDI），用条件和修补而非重来驱动 AI，最后把权利链查清再发。**

---

## 7. 关联与元层（Meta）

### 7.1 与相邻领域的关系与边界

| 邻域 | 关系 | 边界（何时不适用） |
|---|---|---|
| 音乐信息检索（MIR） | 提供表示、标注、转写、分离等基础能力 [51][72][70] | MIR 任务是**分析**，不等于**创作**；精度高不代表作品好 |
| 语音/NLP | 歌词生成、情绪建模、LLM 适配直接借用其方法 [2][52][87][1] | 语言的语义约束不能替代音乐的结构约束 |
| 生成式 AI 版权法 | 提供权利分析框架 [110][111][114] | 法律结论随司法辖区与时点变化，本报告无法给出定论 → `> 待核实` |
|

## 参考来源

[1] Music-robust Automatic Lyrics Transcription of Polyphonic Music — http://arxiv.org/abs/2204.03306v2
[2] Modelling Emotion Dynamics in Song Lyrics with State Space Models — http://arxiv.org/abs/2210.09434v1
[3] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1
[4] YuE: Scaling Open Foundation Models for Long-Form Music Generation — http://arxiv.org/abs/2503.08638v2
[5] Large-Scale Cover Song Detection in Digital Music Libraries Using Metadata, Lyrics and Audio Features — http://arxiv.org/abs/1808.10351v1
[6] Towards an LLM-based method for quantifying the sexual content in song lyrics — http://arxiv.org/abs/2608.08885v1
[7] Formal models of Structure Building in Music, Language and Animal Songs — http://arxiv.org/abs/1901.05180v1
[8] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1
[9] SegTune: Structured and Fine-Grained Control for Song Generation — http://arxiv.org/abs/2606.02638v1
[10] Vision-to-Music Generation: A Survey — http://arxiv.org/abs/2503.21254v1
[11] Segment-Factorized Full-Song Generation on Symbolic Piano Music — http://arxiv.org/abs/2510.05881v1
[12] Story2MIDI: Emotionally Aligned Music Generation from Text — http://arxiv.org/abs/2512.02192v1
[13] Instrumental Text-to-Music Generation with Auxiliary Conditioning Branches — http://arxiv.org/abs/2605.21433v1
[14] CSL-L2M: Controllable Song-Level Lyric-to-Melody Generation Based on Conditional Transformer with Fine-Grained Lyric and Musical Controls — http://arxiv.org/abs/2412.09887v2
[15] UT-AISTimprt submission for ICME 2026 Grand Challenge on Academic Text-to-Music Generation — http://arxiv.org/abs/2607.01669v1
[16] A Functional Taxonomy of Music Generation Systems — http://arxiv.org/abs/1812.04186v1
[17] DiffRhythm+: Controllable and Flexible Full-Length Song Generation with Preference Optimization — http://arxiv.org/abs/2507.12890v2
[18] Song Form-aware Full-Song Text-to-Lyrics Generation with Multi-Level Granularity Syllable Count Control — https://doi.org/10.21437/interspeech.2025-1247
[19] ACE-Step: A Step Towards Music Generation Foundation Model — http://arxiv.org/abs/2506.00045v1
[20]  — https://doi.org/10.54499/2024.02597.bd
[21] ACE-Step 1.5: Pushing the Boundaries of Open-Source Music Generation — http://arxiv.org/abs/2602.00744v3
[22] Indicators of depression in song lyrics of adolescents — https://doi.org/10.17918/00005046
[23] DiffRhythm: Blazingly Fast and Embarrassingly Simple End-to-End Full-Length Song Generation with Latent Diffusion — http://arxiv.org/abs/2503.01183v1
[24] Review of "Song Lyrics Generation Using Machine Learning Techniques" — https://doi.org/10.14293/s2199-1006.1.sor-compsci.apm49p.v1.rbzhho
[25] Introduction to Gestural Similarity in Music. An Application of Category Theory to the Orchestra — http://arxiv.org/abs/1904.10340v1
[26] Learning to Traverse Latent Spaces for Musical Score Inpainting — http://arxiv.org/abs/1907.01164v1
[27] Music SketchNet: Controllable Music Generation via Factorized Representations of Pitch and Rhythm — http://arxiv.org/abs/2008.01291v1
[28] Songwriting, Improvisation, and Arranging — https://doi.org/10.4324/9780429294440-16
[29] Harmony Explained: Progress Towards A Scientific Theory of Music — http://arxiv.org/abs/1202.4212v2
[30] Quantum Curriculum Learning — http://arxiv.org/abs/2407.02419v4
[31] Zero-shot Learning and Knowledge Transfer in Music Classification and Tagging — http://arxiv.org/abs/1906.08615v1
[32] Transforming Musical Signals through a Genre Classifying Convolutional Neural Network — http://arxiv.org/abs/1706.09553v1
[33] Modeling Musical Context with Word2vec — http://arxiv.org/abs/1706.09088v2
[34] A Songwriter’s Workshop Beginner Level — https://doi.org/10.5040/9798881835941.ch-8
[35] Modal Harmony — https://doi.org/10.4324/9781003331155-54
[36] Review of The Practice of Popular Music — https://doi.org/10.15763/issn.2994-7073.2026.39.251-266
[37] ESPnet2 pretrained model, kamo-naoyuki/hkust_asr_train_asr_transformer2_raw_zh_char_batch_bins20000000_ctc_confignore_nan_gradtrue_sp_valid.acc.ave, fs=16k, lang=zh — https://doi.org/10.5281/zenodo.4430974
[38] The Practice of Popular Music — https://doi.org/10.4324/9781003331155
[39] ESPnet2 pretrained model, Emiru Tsunoo/aishell_asr_train_asr_streaming_transformer_raw_zh_char_sp_valid.acc.ave, fs=16k, lang=zh — https://doi.org/10.5281/zenodo.4604023
[40] Harmony in Parallel Minor Keys — https://doi.org/10.4324/9781003331155-42
[41] Review of
                    <i>The Practice of Popular Music: Understanding Harmony, Rhythm, Melody, and Form in Commercial Songwriting</i>
                    by Trevor de Clercq (Routledge, 2025) — https://doi.org/10.30535/mto.31.4.11
[42] Beginner Songwriting Seeds — https://doi.org/10.1093/oso/9780197693216.003.0011
[43] Dorabella Cipher as Musical Inspiration — http://arxiv.org/abs/2509.17950v1
[44] Improving Choral Music Separation through Expressive Synthesized Data from Sampled Instruments — http://arxiv.org/abs/2209.02871v1
[45] musif: a Python package for symbolic music feature extraction — http://arxiv.org/abs/2307.01120v1
[46] 传统戏曲唱腔元素融入高校声乐教学的路径与文化价值研究 — https://doi.org/10.63887/etr.2025.1.7.86
[47] GlobalMood: A cross-cultural benchmark for music emotion recognition — http://arxiv.org/abs/2505.09539v2
[48] 中职钢琴练习曲教学的困境与“趣学”模式的构建路径研究 —发现练习曲中的“趣”和“美” — https://doi.org/10.64224/rddx4115
[49] Diffusion-based Symbolic Music Generation with Structured State Space Models — http://arxiv.org/abs/2507.20128v2
[50] MidiTok Visualizer: a tool for visualization and analysis of tokenized MIDI symbolic music — http://arxiv.org/abs/2410.20518v1
[51] Symbolic Music Representations for Classification Tasks: A Systematic Evaluation — http://arxiv.org/abs/2309.02567v2
[52] MIDI-LLM: Improving Text-to-MIDI Music Generation via Adapting Large Language Models — http://arxiv.org/abs/2511.03942v2
[53] Byte Pair Encoding for Symbolic Music — http://arxiv.org/abs/2301.11975v3
[54] Motifs, Phrases, and Beyond: The Modelling of Structure in Symbolic Music Generation — http://arxiv.org/abs/2403.07995v1
[55] Chord-conditioned Melody and Bass Generation — http://arxiv.org/abs/2511.08755v1
[56] Controllable deep melody generation via hierarchical music structure representation — http://arxiv.org/abs/2109.00663v1
[57] LSTM-Based Procedural Symbolic Music Generation Using Sequential MIDI Pitch Modeling — https://doi.org/10.46254/an16.20260287
[58] Melody Harmonization Using Orderless NADE, Chord Balancing, and Blocked Gibbs Sampling — http://arxiv.org/abs/2010.13468v2
[59] Working with MIDI — https://doi.org/10.4324/9780080926865-9
[60] Chord-Conditioned Melody Harmonization with Controllable Harmonicity — http://arxiv.org/abs/2202.08423v4
[61] Working with MIDI — https://doi.org/10.4324/9780203066416-10
[62] MusiConGen: Rhythm and Chord Control for Transformer-Based Text-to-Music Generation — http://arxiv.org/abs/2407.15060v1
[63] Working with MIDI — https://doi.org/10.4324/9780240522494-8
[64] Striking a New Chord: Neural Networks in Music Information Dynamics — http://arxiv.org/abs/2410.17989v2
[65] MMT-BERT: Chord-aware Symbolic Music Generation Based on Multitrack Music Transformer and MusicBERT — http://arxiv.org/abs/2409.00919v1
[66] Real-Time Human-Classified Emotional MIDI Dataset Integration for Symbolic Music Generation — https://doi.org/10.1109/icmla61862.2024.00076
[67] Mamba-Diffusion Model with Learnable Wavelet for Controllable Symbolic Music Generation — https://doi.org/10.1109/ijcnn64981.2025.11228274
[68] Controllable Music Loops Generation with MIDI and Text via Multi-Stage Cross Attention and Instrument-Aware Reinforcement Learning — https://doi.org/10.1145/3664647.3681187
[69] [Paper] TPSMG: Text-Controllable Polyphonic Symbolic Music Generation — https://doi.org/10.3169/mta.14.110
[70] End-to-end music source separation: is it possible in the waveform domain? — http://arxiv.org/abs/1810.12187v2
[71] M2D-CLAP: Exploring General-purpose Audio-Language Representations Beyond CLAP — http://arxiv.org/abs/2503.22104v2
[72] Advancing Multi-Instrument Music Transcription: Results from the 2025 AMT Challenge — http://arxiv.org/abs/2603.27528v1
[73] CultureMERT: Continual Pre-Training for Cross-Cultural Music Representation Learning — http://arxiv.org/abs/2506.17818v1
[74] Overview of the Sensemaking Task at the ELOQUENT 2025 Lab: LLMs as Teachers, Students and Evaluators — http://arxiv.org/abs/2507.12143v1
[75] The RSNA Abdominal Traumatic Injury CT (RATIC) Dataset — http://arxiv.org/abs/2405.19595v1
[76] SyMuRBench: Benchmark for Symbolic Music Representations — https://doi.org/10.1145/3746278.3759392
[77] Sanidha: A Studio Quality Multi-Modal Dataset for Carnatic Music — http://arxiv.org/abs/2501.06959v1
[78] ConvM2D2: Improving Generative Music Evaluation using Self-Supervised Alternative to CLAP — https://doi.org/10.36227/techrxiv.175614002.20847889/v1
[79] LP-MusicCaps: LLM-Based Pseudo Music Captioning — http://arxiv.org/abs/2307.16372v1
[80] Meta-Evaluation Methodology and Benchmark for Automatic Story Generation — https://doi.org/10.70675/ec296eb8z87a1z4fdbzbbbdz12bb27449b8f
[81] MOSA: Music Motion with Semantic Annotation Dataset for Cross-Modal Music Processing — http://arxiv.org/abs/2406.06375v1
[82] EVALUATION OF THE EFFICACY OF CONTINUOUS LOCAL ANTIBIOTIC PERFUSION (CLAP) FOR PERIPROSTHETIC JOINT INFECTION: CLAP VERSUS NON-CLAP — https://doi.org/10.1302/1358-992x.2025.12.018
[83] The Trumpet “Fad” That Deposed the Cornet — https://doi.org/10.5406/19405103.43.1.2.09
[84] PPMI-Benchmark: A Dual Evaluation Framework for Imputation and Synthetic Data Generation in Longitudinal Parkinson's Disease Research — https://doi.org/10.5220/0013649700003967
[85] MIRAGE: A Metric-Intensive Benchmark for Retrieval-Augmented Generation Evaluation — https://doi.org/10.18653/v1/2025.findings-naacl.157
[86] Annex 4. FAD Support to Surveillance and Review — https://doi.org/10.5089/9798229032087.017.ch010
[87] SongMASS: Automatic Song Writing with Pre-training and Alignment Constraint — http://arxiv.org/abs/2012.05168v1
[88] SurgicalSAM: Efficient Class Promptable Surgical Instrument Segmentation — http://arxiv.org/abs/2308.08746v2
[89] SurgicalPart-SAM: Part-to-Whole Collaborative Prompting for Surgical Instrument Segmentation — http://arxiv.org/abs/2312.14481v2
[90] Massive stars with Pollux on LUVOIR — http://arxiv.org/abs/1811.05264v1
[91] Flexible Variable Star Extractor: new software for detection of variable stars — http://arxiv.org/abs/1812.06955v1
[92] Recognizing License Plates in Real-Time — http://arxiv.org/abs/1906.04376v6
[93] A Study of Potential Code Borrowing and License Violations in Java Projects on GitHub — http://arxiv.org/abs/2002.05237v2
[94] On the Popularity of GitHub Applications: A Preliminary Note — http://arxiv.org/abs/1507.00604v3
[95] ThankYouStars: Give your Dependencies Stars on GitHub! — https://doi.org/10.32614/cran.package.thankyoustars
[96] A Large Scale Study of License Usage on GitHub — https://doi.org/10.1109/icse.2015.245
[97] Table 10: Comparison with state of the art techniques for GitHub dataset. — https://doi.org/10.7717/peerj-cs.854/table-10
[98] Index — https://doi.org/10.1515/9783111025575-010
[99] Joint Music and Language Attention Models for Zero-shot Music Tagging — http://arxiv.org/abs/2310.10159v1
[100] References — https://doi.org/10.1515/9783111025575-009
[101] Contents — https://doi.org/10.1515/9783111025575-toc
[102] No Encore: Unlearning as Opt-Out in Music Generation — http://arxiv.org/abs/2509.06277v2
[103] Acknowledgments — https://doi.org/10.1515/9783111025575-202
[104] Frontmatter — https://doi.org/10.1515/9783111025575-fm
[105] Opening Musical Creativity? Embedded Ideologies in Generative-AI Music Systems — http://arxiv.org/abs/2508.08805v1
[106] Who Gets Heard? Rethinking Fairness in AI for Music Systems — http://arxiv.org/abs/2511.05953v1
[107] Ethics Statements in AI Music Papers: The Effective and the Ineffective — http://arxiv.org/abs/2509.25496v1
[108] "Melatonin": A Case Study on AI-induced Musical Style — http://arxiv.org/abs/2208.08968v1
[109] The Shape of Surprise: Structured Uncertainty and Co-Creativity in AI Music Tools — http://arxiv.org/abs/2509.25028v1
[110] Talkin' 'Bout AI Generation: Copyright and the Generative-AI Supply Chain — http://arxiv.org/abs/2309.08133v2
[111] Privacy and Copyright Protection in Generative AI: A Lifecycle Perspective — http://arxiv.org/abs/2311.18252v3
[112] EditGuard: Versatile Image Watermarking for Tamper Localization and Copyright Protection — http://arxiv.org/abs/2312.08883v1
[113] Who Owns the Knowledge? Copyright, GenAI, and the Future of Academic Publishing — http://arxiv.org/abs/2511.21755v2
[114] Copyright in Generative Deep Learning — http://arxiv.org/abs/2105.09266v5
[115] Guardians of Generation: Dynamic Inference-Time Copyright Shielding with Adaptive Guidance for AI Image Generation — http://arxiv.org/abs/2503.16171v1
[116] Faith in AI can narrow the futures individuals consider — http://arxiv.org/abs/2603.28944v2
[117] Music streaming practices. Spotify usage in Romania — https://doi.org/10.61789/pub.cdi.psm.en25
[118] How Does Spotify Package Music? — https://doi.org/10.7551/mitpress/10932.003.0008
[119] AI 工具集官网 | 1000+  AI 工具集合，国内外 AI 工具集导航大全 — https://ai-bot.cn/
[120] Intervention: Work at Spotify! — https://doi.org/10.7551/mitpress/10932.003.0013
[121] AI  工具完全指南（2026）：ChatGPT、Gemini、Kimi 与 ... — https://tanqingbo.cn/ai-tools-guide/
[122] Where Is Spotify? — https://doi.org/10.7551/mitpress/10932.003.0004
[123] 人工智能（智能科学与技术专业术语）_百度百科 — https://baike.baidu.com/item/%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD/9180
[124] Streaming: Vertrag zwischen Spotify und Sony Music veröffentlicht — https://doi.org/10.59350/mm36w-0nx37
[125] 目前有哪些主流的 AI ？ - 知乎 — https://www.zhihu.com/question/591009674
[126] When music becomes datafied: Streaming services and the case of Spotify — https://doi.org/10.5040/9781501345357.ch-18


---

*Generated by research-bot · topic=`小白如何从零快速成为一名标准音乐人词曲创作编曲midi-修改用-yue-等-ai-生成模型到发行版权与行业影响` · depth=`standard` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, knowledge-framework · model=`deepseek-v4-flash` · sources=126 · duration=497s · 2026-10-04T12:49:05+00:00*
