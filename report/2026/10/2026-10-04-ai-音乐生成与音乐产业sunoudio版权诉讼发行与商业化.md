# AI 音乐生成与音乐产业增量追踪报告（2024–2026 基线窗口）

**日期**：2026-10-04（UTC）  
**领域**：AI 音乐生成（Text-to-Music / Full-Song Generation）、开源工程栈、评测基准、版权与监管、发行与商业化  
**检索源数量**：115 条候选来源（其中与本主题直接相关者约 40 条；其余为跨领域噪声来源，已在正文中排除）  
**方法论**：deep-research（四阶段）+ frontier-tracking（时间线/证据强度）+ frontier-watch（七维增量）+ evidence-grading（A–E 分级）

> **证据可用性前置声明**：本次候选证据集存在两类结构性缺口。第一，**产业与法律一手证据严重缺失**——RIAA 诉 Suno/Udio 的案号、阶段、和解/授权条款，Spotify/Deezer 官方 AI 政策原文，Suno/Udio/Stability 的融资额与估值，均**未出现在候选块中**，本报告对此类内容一律标注 `> 待核实`，不作推测性陈述。第二，候选集中大量条目与本主题无关（高能物理 [88]–[95]、图像超分辨率 [19]、rip current 分割 [107] 等），本报告已剔除。因此本报告的可证实结论集中在**学术侧（评测基准、开源模型、版权技术路径、政策批评文献）**，产业侧只能给出间接信号。

---

## 1. 进展与热点（Progress & Hotspots）

**一句话增量判断**：相对 MusicGen/MusicLM 时期（2023）的"单轮文本→短音频片段"基线，2024–2026 的增量不在"能否生成音乐"，而在**评测的组织化（ICME 2026 ATTM 挑战赛、AudioMOS 2025）、编辑可控化（指令调优、音频提示适配器）、以及全长歌曲（full-song）结构化生成**三个方向。

### 1.1 评测从"自建指标"走向"挑战赛化"（本轮最强增量信号）

| 条目 | 时间 | 增量相对基线 |
|---|---|---|
| ICME 2026 Academic Text-to-Music (ATTM) Grand Challenge | 2026 | 首次出现**统一的学术 T2M 竞赛协议**（FAD-CLAP + CLAP 为基线指标），并要求在**低保真数据 + 小模型**条件下竞争 [1] |
| AudioMOS Challenge 2025 | 2025 | 自称**首个面向合成音频自动主观质量预测**的挑战，Track1 同时评估 text-to-music 的 overall quality 与 textual alignment，Track2 采用 Meta Audiobox Aesthetics 四维 [49] |

- **热度证据**：候选块未提供任意一方的引用数或参赛队伍数 `> 待核实`。  
- **权威证据**：[49] 为挑战官方 summary paper（arXiv cs.SD 预印本，B 级）；[1] 为参赛方案（arXiv cs.SD 预印本，B 级）。  
- **关注度**：**中**——依据：两项挑战均为 2025–2026 新设，属"机制性新增"而非既有热点的延续；但候选块无引用/榜单数据可量化 [1][49]。  
- **推荐度**：**★★★★☆**——若需跟踪 T2M 评测口径演化，这两项是本周期最可比的锚点。

### 1.2 可控性与编辑能力：从"重新生成"到"就地编辑"

- **指令调优编辑**：Instruct-MusicGen 通过 instruction tuning 解锁文本到音乐的**编辑**能力（而非仅生成），相对 MusicGen 的增量是"对既有音频做定向修改" [48]。  
- **轻量微调编辑**：Audio Prompt Adapter 以轻量微调为 T2M 释放音乐编辑能力，强调**低训练成本**路线 [52]。  
- **辅助条件分支**：针对**器乐** T2M，研究以辅助 conditioning branches 分离"哪些设计选择真正起作用"，指出该领域进展高度依赖大规模数据与外部预训练，难以归因 [2]。  

> 归因缺口：上述工作均未在候选块中提供与商业系统（Suno/Udio）的**同口径对比**；[2] 明确点出"性能提升难以归因于数据还是架构"，这是本轮增量中最值得警惕的一点。

### 1.3 全长歌曲（full-song）与结构化生成

- Segment-Factorized Full-Song Generation on Symbolic Piano Music [85]  
- Song Form-aware Full-Song Text-to-Lyrics Generation with Multi-Level Granularity Syllable Count Control（**Interspeech 2025，同行评审**）[12]  
- RapVerse: Coherent Vocals and Whole-Body Motion Generation from Text（**ICCV 2025**）[22]  
- Story2MIDI: Emotionally Aligned Music Generation from Text [4]

**增量判断**：相对 2023 年"30 秒片段"基线，符号域已出现**分段因子化 + 曲式感知**的全曲生成方案 [85][12]，但**音频域全长人声歌曲**的可比证据在候选块中缺失 `> 待核实`。

### 1.4 偏好优化与"人类偏好奖励"进入 T2M

- [3] 在 ATTM 协议标准之外**额外引入学得的人类偏好奖励**（TuneJury twin pairwise ranker，基于开放音乐偏好数据集训练）。  
- **增量**：这是 RLHF/偏好对齐范式**从 LLM 迁移到音乐生成**的明确信号，相对上一代"纯客观指标优化"是方法学增量 [3]。  
- **热度证据**：`> 待核实`（候选块无引用数）。— **权威**：arXiv cs.SD 预印本（B 级）。— **关注度**：中（新方法范式，但无量化热度）。— **推荐度**：**★★★★☆**（偏好对齐在音频域落地是值得跟进的方向）。

---

## 2. 工业界与产品（Industry & Product）

**一句话增量判断**：本周期唯一具备**可核查体量证据**的产业事实，是 Suno/Udio 已从"玩具演示"进入**规模化使用 + 商业化落地（广告、多国榜单）**阶段 [5]；开源侧 ACE-Step 系列与 Stable Audio Open 构成对闭源系统的工程替代路径 [53][56][67]。**融资、估值、并购、平台政策均无候选证据，全部待核实。**

### 2.1 可核查的产业事实（仅此一条具备量化证据）

- **Suno / Udio 的规模化与商业落地**：[5] 基于大规模生成歌曲集合做文本条件生成分析，指出两平台"被数十万用户使用"，且"部分 AI 音乐已出现在广告中，甚至在多个国家进入榜单" [5]。  
  - **热度证据**：`> 待核实`（候选块未提供该文引用数）。  
  - **权威证据**：arXiv cs.IR 预印本（B 级），非同行评审 `> 待核实` 是否已中稿。  
  - **关注度**：**高**——依据：直接覆盖两大**涉诉平台**的使用规模与商业落地，是版权争议"现实体量"的关键经验材料 [5]。  
  - **推荐度**：**★★★★☆**——为任何关于诉讼/授权谈判的讨论提供可引用背景。

### 2.2 开源产品与工程栈

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| ACE-Step | 2025 | `> 待核实` | `> 待核实`（无 star/引用） | arXiv cs.SD 预印本（B 级）；标题自称 "Music Generation Foundation Model" [53] | 中：以"音乐生成基础模型"定位开源，属本周期开源侧关键节点 | ★★★★☆：开源音乐基础模型的核心候选，需核实权重与许可 | http://arxiv.org/abs/2506.00045v1 | 面向音乐生成的基础模型尝试 [53] |
| ACE-Step 1.5 | 2026 | `> 待核实` | `> 待核实` | arXiv 预印本（B 级）；标题明确 "Open-Source Music Generation" [56] | 中：标题层面确认为开源续作，但候选块无仓库/权重信息 | ★★★★☆：判断开源 T2M 能力天花板的优先线索 | http://arxiv.org/abs/2602.00744v3 | 开源音乐生成边界推进 [56] |
| Stable Audio Open | 2024 | `> 待核实`（Stability AI 关联，待核实） | `> 待核实` | arXiv 预印本（B 级）[67] | 中：开源音频生成的代表性工作之一 | ★★★★☆：开源 T2M 基线之一 | http://arxiv.org/abs/2407.14358v2 | 开放权重音频生成模型 [67] |
| Instruct-MusicGen | 2024 | `> 待核实` | `> 待核实` | arXiv 预印本 v3（B 级）[48] | 中：指令编辑方向的高相关工作 | ★★★★☆：做"编辑而非重生成"的工程入口 | http://arxiv.org/abs/2405.18386v3 | 文本到音乐编辑的指令调优 [48] |
| Audio Prompt Adapter | 2024 | `> 待核实` | `> 待核实` | arXiv 预印本 v2（B 级）[52] | 中：轻量微调路线 | ★★★☆☆：关注低成本编辑微调时参考 | http://arxiv.org/abs/2407.16564v2 | 轻量微调释放音乐编辑能力 [52] |

> **工程落地缺口**：DAW 插件集成方面，候选块仅有**VST 插件开发生态的挖掘研究**（MSR 2025，DOI 10.1109/msr66628.2025.00085）[57]，它分析的是 GitHub 上 VST 插件的开发实践，**并不证实任何 AI 音乐模型已集成进 DAW**。LoRA 微调 MusicGen 的实际工作流、本地推理成本（显存/延迟/单曲秒数）在候选块中**完全无证据** `> 待核实`。

### 2.3 作曲者工作流中的真实使用

- [51] 是**用户研究**（user study），考察 T2M 模型对音乐制作人工作流的实际影响，明确指出"T2M 模型与音乐人工作流的整合仍未被充分探索" [51]。  
  - **关注度**：中——依据：本主题下少数直接研究"人机协作落地"的实证工作，但候选块无引用数据。  
  - **推荐度**：**★★★★☆**——用于回答"AI 到底进入了制作流程的哪一环"，比厂商演示更可信。

---

## 3. 蓝海与缺口（Blue Ocean & Gaps）

**一句话增量判断**：本周期被反复点名的**三段无人区**是——(a) 版权合规的**评测维度**（而非法律条文）完全缺位；(b) 音乐生成的**机器遗忘 / opt-out 技术**刚起步；(c) **跨文化与流派公平性**刚刚进入议程。

### 3.1 缺口清单（按杠杆率排序）

1. **版权合规评测基准缺位**（最高杠杆）。候选证据覆盖的评测维度为：整体质量、文本对齐、美学四维、音乐印象、情绪传达 [49][50][68][80]；**无任何条目覆盖"版权合规/训练数据来源合规"的评测维度** `> 待核实`（本判断基于候选集覆盖范围，非外部权威统计）。
2. **Full-song / 人声级评测维度未明确**。SongEval 面向"歌曲"美学，但其摘要未明确声明是否覆盖 full-song 与人声 [80]；其余基准均以"文本到音乐样本"或情绪为对象 [49][50][68] `> 待核实`。
3. **模型侧 opt-out 机制刚起步**。[62] 自述为"机器遗忘（machine unlearning）在音乐生成中的**首次应用**"，用于抑制对受版权保护作品的非授权使用，动机表述为版权与伦理关切；但作者自述为 **ongoing research 的 preliminary results**，属早期探索 [62]。
4. **透明度义务缺乏可量化度量**。[100] 直指 EU AI Act "缺乏可量化的公平性指标"，且 transparency / explainability / interpretability 三词被互换使用造成术语歧义 [100]；[14] 则为透明度提供了**年度可比指数量表**并新增"data acquisition"相关指标 [14]——两者之间的落差即是空白。
5. **跨文化与流派偏置**。[97] 指出音乐-AI 的关切已从 copyright / deepfakes / transparency **扩展**到 cultural and genre biases，影响 creators / distributors / listeners 等各方的 representation [97]；[59] 的 CultureMERT 用**持续预训练**做跨文化音乐表示学习，属对该缺口的技术回应 [59]。
6. **"民主化"话语与设计原则的落差**。[86] 断言在产业环境中，"inclusivity often functions as marketable rhetoric rather than a genuine guiding principle" [86]。

### 3.2 竞争空白

- **全长人声音频生成的统一评测**：符号域已有全曲方案 [85][12]，音频域缺乏可比基准 `> 待核实`。
- **AI 音乐伦理声明的质量评估**：[103] 专文研究 AI 音乐论文中的伦理声明"哪些有效、哪些无效"，说明连**学术共同体自身的伦理披露**都尚未形成有效规范 [103]——这是一个低成本高影响的空白。

---

## 4. 瓶颈与拐点（Bottleneck & Inflection）

**一句话增量判断**：当前最硬的瓶颈**不是生成能力，而是评测口径的可比性与合规的可度量性**；拐点信号是"评测挑战赛化 + 透明度指数化"同时发生。

| 瓶颈 | 证据 | 是否临近拐点 | 拐点信号 |
|---|---|---|---|
| **评测成本**：专家主观评分昂贵且稀缺 | AudioMOS 2025 的设立动机即"降低收集专家评估的成本与难度" [49][50] | 是 | 已出现可参赛的**自动预测系统**（MuQ + RoBERTa 双分支），说明主观维度正被自动化建模 [50] |
| **数据/归因**：性能提升无法分离数据与架构贡献 | [2] 明确称"much of this progress relies on large-scale training data and external pretraining, making it difficult to isolate which design choices…" [2] | 待观察 | 尚无控制变量式研究出现 |
| **术语与指标不可比** | transparency/explainability/interpretability 混用 [100]；TA 与美学指标口径未统一（见 §3.1） | 否 | 需要监管或标准组织介入 `> 待核实` |
| **长序列生成** | 符号域存在二次复杂度限制，SSM 被引入以突破 [32] | 是 | 结构化状态空间模型（SSM）替代 self-attention 的路线已出现 [32] |
| **合规工具链** | 仅 unlearning 初步结果 [62] | 否 | 需出现可复现的 opt-out 工程实现 `> 待核实` |
| **透明度合规** | FMTI 第三版新增数据获取指标 [14] | 是 | 透明度从"自愿披露"走向"年度指数化问责" [14] |

- **热度证据**：上述条目在候选块中**均无引用数/star/榜单数据** `> 待核实`。  
- **权威证据**：[32] arXiv cs.SD v2；[14] arXiv cs.AI（第三版年度报告）；[62] arXiv cs.CL v2；[2] arXiv cs.SD；[100] arXiv cs.CY——**全部为预印本，均未在候选块中显示同行评审 venue**（B 级）。  
- **关注度**：中（依据：多为机制性/方向性工作，非引用驱动的热点）。  
- **推荐度**：**★★★★☆**（[14][49] 作为"可观测指标"的来源，价值最高，因其提供了可年度对比的口径）。

---

## 5. 社会·政策·国际（Society, Policy & Geopolitics）

**一句话增量判断**：**法律事实层面本报告无法给出任何确证**（RIAA 诉 Suno/Udio、三大唱片授权协议在候选块中零覆盖）；能确证的增量是**学术侧对 AI 音乐监管议题范围的扩张**：从版权 → 透明度 → 公平性/代表性 → 伦理披露规范。

### 5.1 监管与合规度量

| 条目 | 时间 | 增量 | 四类证据 |
|---|---|---|---|
| The 2025 Foundation Model Transparency Index | 2025 | 第三版，**新增 data acquisition 相关指标**，把"训练数据来源透明度"纳入可比量表 [14] | 热度 `> 待核实`；权威：arXiv cs.AI 预印本，年度系列第三版，**未显示同行评审 venue**（B 级）；关注度 **中**（依据：连续第三年发布，但无引用/榜单数据）；推荐度 **★★★★☆**——透明度合规度量的首选口径 |
| An Analysis of the New EU AI Act and A Proposed Standardization Framework for ML Fairness | 2025 | 直指法案**缺少可量化公平性指标**、术语混用 [100] | 热度 `> 待核实`；权威：arXiv cs.CY 预印本，**学者分析而非官方解释文件**（B 级）；关注度 **中**；推荐度 **★★★★☆**——讨论 EU AI Act 可操作性的核心批评文献 |
| Towards Assuring EU AI Act Compliance and Adversarial Robustness of LLMs | 2024 | 面向合规保证与对抗鲁棒性的技术路径 [99] | 热度 `> 待核实`；权威：arXiv cs.LG/cs.CY 预印本（B 级）；关注度 中；推荐度 ★★★☆☆——非音乐专用，作方法学参考 |
| Privacy and Copyright Protection in Generative AI: A Lifecycle Perspective | 2023–2024 | 以**生命周期视角**统合隐私与版权保护 [98] | 热度 `> 待核实`；权威：arXiv 预印本（B 级）；关注度 中；推荐度 ★★★☆☆——框架性参考，时效偏早 |

> **待核实（关键缺口）**：EU AI Act 透明度义务的具体**生效/适用时间表及其对音乐生成模型的直接约束**，候选证据仅给出学术批评，未给出条文与日期 `> 待核实`。各法域判例进展、集体管理组织诉讼进程 `> 待核实`。

### 5.2 版权技术路径与产业话语

- **技术性 opt-out**：[62] 首次将机器遗忘用于音乐生成以规避版权作品非授权使用，作者自述为初步结果 [62]。  
  - 权威：arXiv cs.CL v2 预印本，**未显示同行评审**；关注度 中；推荐度 **★★★☆☆**（趋势线索，非确证结论）。
- **元数据与版权/数据法**：Music metadata improvement—copyright, fundamental rights and data law（JIPLP，DOI 10.1093/jiplp/jpag041）[101]——**期刊文献，A/B 级**，但候选块无摘要细节，仅可作"元数据治理"线索。  
- **产业正当性话语受质疑**：[86] 指"民主化"多属营销修辞 [86]；**权威**：arXiv cs.SD 预印本；**关注度** 中；**推荐度** ★★★☆☆（立场性证据，法律价值有限）。
- **议题范围扩张**：[97] 将关切从 copyright/deepfakes/transparency 扩展到文化/流派偏置与代表性 [97]。  
  - 权威：arXiv cs.CY 预印本；关注度 中；推荐度 ★★★☆☆。
- **伦理披露规范**：[103] 研究 AI 音乐论文伦理声明的有效与无效 [103]。  
  - 权威：arXiv cs.CY 预印本；关注度 中；推荐度 ★★★☆☆——用于评估学术共同体自律现状。

### 5.3 AI 内容检测与真实性（外溢议题）

- AINL-Eval 2025 共享任务：俄语 AI 生成科学摘要检测 [108]；AuTexTification 2023：多领域机器生成文本检测与归因 [30]。  
  - **相关性说明**：二者**非音乐领域**，仅作为"AI 生成内容可检测性"的邻近信号列出，**不构成对 AI 音乐检测能力的证据**。关注度 低；推荐度 ★☆☆☆☆。

---

## 6. 资本与生态（Capital & Ecosystem）

**一句话增量判断**：**本周期该维度在候选证据中无显著可核查变化。** 本报告拒绝在无证据的情况下编造融资额、估值或并购信息。

### 6.1 证据状态

| 应回答的问题 | 候选证据状态 |
|---|---|
| Suno / Udio / Stability 融资额、估值 | **零覆盖** `> 待核实` |
| 唱片公司对生成式音乐公司的投资/并购 | **零覆盖** `> 待核实` |
| 三大唱片公司与生成式音乐公司的和解/授权协议条款、签约主体、时间点 | **零覆盖** `> 待核实` |
| 流媒体平台 AI 标注/反欺诈政策（Spotify/Deezer） | **零覆盖** `> 待核实` |
| 版税与分成机制变化 | **零覆盖** `> 待核实` |
| AI 声音/肖像授权市场 | **零覆盖** `> 待核实` |
| 人才流动 | **零覆盖** `> 待核实` |

### 6.2 唯一可用的生态线索

- **开源生产工具生态**：The Ecosystem of Open-Source Music Production Software – A Mining Study on the Development Practices of VST Plugins on GitHub（**MSR 2025，同行评审**，DOI 10.1109/msr66628.2025.00085）[57]。  
  - **热度证据**：`> 待核实`（候选块无引用数/star）。  
  - **权威证据**：MSR 2025（Mining Software Repositories）——**同行评审会议，A 级**。  
  - **关注度**：**低**——依据：属于音乐软件工程研究，与 AI 音乐投资/资本流向无直接关联。  
  - **推荐度**：**★★☆☆☆**——仅在研究"AI 工具如何进入 DAW 生态"时作为背景。  
- **VC 匹配预测**：Predicting Startup-VC Fund Matches with Structural Embeddings and Temporal Investment Data [111]。  
  - **相关性说明**：该文为**通用 VC 匹配方法**，候选块标题未涉及音乐产业，**不能**作为音乐 AI 融资证据使用。  
  - **权威**：arXiv 预印本；**关注度** 低；**推荐度** ★☆☆☆☆。

> **结论**：第 6 维本周期**无显著可核查变化（no verifiable increment）**。任何关于估值、融资、并购的数字在本次证据下均**不可陈述**。

---

## 7. 信号与预测（Signals & Forecast）

**一句话增量判断**：早期信号集中在"**评测自动化**"与"**合规可度量**"两条线；据此给出的预判全部写成可证伪假设，并标注置信度。

### 7.1 早期信号（[P] 前置）

| 信号 | 时间 | 依据 |
|---|---|---|
| 主观音乐质量正被自动化建模（TA/MI 双分支系统已在挑战赛中出现） | 2025 | [50]（自称获胜系统，需官方结果交叉验证） |
| 透明度从自愿披露转向年度指数化问责，且新增"数据获取"维度 | 2025 | [14] |
| 机器遗忘被用于音乐版权 opt-out 的**首次尝试** | 2025 | [62]（author 自述初步结果） |
| 偏好对齐（human preference reward）进入 T2M 训练目标 | 2026 | [3] |
| 跨文化表示学习被用于对抗流派/文化偏置 | 2025 | [59][97] |

### 7.2 可证伪预测

- **[P-1]｜模型侧 opt-out 将在 12–18 个月内从"初步结果"进入可复现工程实现。**  
  依据链：侵权关切持续 [62] → 透明度指数化压力 [14] → 监管术语尚未统一但方向明确 [100]。  
  **证伪条件**：若到 **2027-10** 前仍**没有**出现公开权重/代码的音乐 unlearning 实现（可验证其能抑制指定风格或艺术家特征），则判断不成立。  
  **置信度**：**推测（medium-low）**。

- **[P-2]｜"版权合规"将成为 T2M 评测基准的下一个新增维度。**  
  依据链：现有基准仅覆盖质量/对齐/美学/情绪 [49][80][68] → 产业体量已足够大（数十万用户、进榜单、上广告）[5] → 合规压力从法律侧传导至评测侧。  
  **证伪条件**：若到 **2027-12**，主流 T2M 挑战赛（如 ATTM 后续届次 [1]）的官方协议中**仍未加入**训练数据来源或生成内容相似度合规类指标，则判断不成立。  
  **置信度**：**较大概率（medium-high，因压力源明确，但取决于组织者意愿）**。

- **[P-3]｜全长（full-song）人声音频生成会出现首个被多方引用的可比基准。**  
  依据链：符号域已先行（Segment-Factorized Full-Song [85]、Song Form-aware Lyrics [12]）→ 音频域仍是空白 §§3.1。  
  **证伪条件**：若到 **2027-12** 前，仍无一个明确声明覆盖 **full-song + 人声**的公开评测基准被至少两个独立团队使用，则判断不成立。  
  **置信度**：**未知**（符号域与音频域存在技术鸿沟，迁移不确定）。

- **[P-4]｜"透明度/合规"将成为音乐生成研究与法律实务之间的接口议题，而非单纯的模型能力议题。**  
  依据链：[14] 提供量表、[100] 指出量表缺失、[101] 讨论元数据与版权法 → 三者尚未汇合。  
  **证伪条件**：若到 **2027-06** 前，仍未出现将 FMTI 式透明度指标 [14] **具体应用到音乐生成模型**的公开评估报告，则判断不成立。  
  **置信度**：**需要数据**。

### 7.3 Watchlist（值得持续关注）

1. **ICME 2026 ATTM Grand Challenge 的后续届次与协议演化** —— 观察评测口径是否纳入合规维度 [1][2][3]。
2. **AudioMOS Challenge 的官方结果与 Track1 获胜方案的可复现性** —— 需交叉验证 [50] 的自述结论 [49][50]。
3. **ACE-Step 系列的权重、许可与推理成本披露** —— 决定开源 T2M 工程栈的真实可用性 [53][56]。
4. **Foundation Model Transparency Index 第四版** —— 观察"data acquisition"指标是否延伸到音频/音乐模态 [14]。
5. **音乐 unlearning / opt-out 的工程化落地** —— 从 [62] 的初步结果到可复现实现的进程。
6. **跨文化音乐表示的进展** —— [59] CultureMERT 后续与 [97] 的公平性框架是否合流。

---

## 8. 经典与奠基性工作、开源项目、数据集与基准

### 8.1 经典与奠基性工作（相对"最新进展"分节）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Jukebox: A Generative Model for Music | 2020 | OpenAI（候选块未标注作者，`> 待核实`） | `> 待核实` | arXiv cs.SD 预印本（B 级）[35] | 高：音乐生成领域公认的奠基性工作之一，是后续所有"原始音频域生成"路线的参照点 | ★★★★★：理解本轮技术脉络绕不开的起点 | http://arxiv.org/abs/2005.00341v1 | 原始音频域生成模型，确立"音乐 token 化 + 自回归"范式 [35] |
| MusicLM: Generating Music From Text | 2023 | Google（`> 待核实`） | `> 待核实` | arXiv cs.SD 预印本（B 级）[38] | 高：文本到音乐（T2M）任务的定义性工作之一 | ★★★★★：T2M 技术脉络的基准节点，本报告 §1 中所有"增量"均以此为对照基线 | http://arxiv.org/abs/2301.11325v1 | 文本条件音乐生成 [38] |
| Music SketchNet: Controllable Music Generation via Factorized Representations of Pitch and Rhythm | 2020 | `> 待核实` | `> 待核实` | arXiv cs.LG 预印本（B 级）[25] | 中：可控生成（pitch/rhythm 因子化）的早期代表 | ★★★★☆：理解"可控性"脉络的源头之一 | http://arxiv.org/abs/2008.01291v1 | 以 pitch/rhythm 因子化表示实现可控生成，类比图像补全 [25] |
| End-to-end learning for music audio tagging at scale | 2018 | `> 待核实` | `> 待核实` | arXiv（B 级）[106] | 中：音乐音频端到端学习的规模化早期工作 | ★★★☆☆：音乐音频表示学习的方法学源头 | http://arxiv.org/abs/1711.02520v4 | 大规模端到端音乐音频标注 [106] |
| Toward Interpretable Music Tagging with Self-Attention | 2019 | `> 待核实` | `> 待核实` | arXiv（B 级）[105] | 中：可解释音乐标注的代表工作 | ★★★☆☆：与今日"可解释性/透明度"议题形成呼应 | http://arxiv.org/abs/1906.04972v1 | 自注意力用于可解释音乐标注 [105] |
| Symbolic Music Representations for Classification Tasks: A Systematic Evaluation | 2023 | `> 待核实` | `> 待核实` | arXiv eess.AS v2（B 级）[27] | 中：系统评估符号音乐表示，指出"符号音乐既非图像也非句子" | ★★★★☆：符号域建模的方法学清点，避免表征误用 | http://arxiv.org/abs/2309.02567v2 | 符号音乐表示的体系化评估 [27] |
| musif: a Python package for symbolic music feature extraction | 2023 | `> 待核实` | `> 待核实` | arXiv cs.SD（B 级）[26] | 中：符号音乐特征工程工具包 | ★★★☆☆：符号域特征提取的现成工程件 | http://arxiv.org/abs/2307.01120v1 | 专家协作开发的符号音乐特征提取包 [26] |

> **脉络概括**：Jukebox [35] 确立原始音频域生成 → MusicLM [38] 确立文本条件 → 本轮增量转向**偏好对齐 [3]、指令编辑 [48][52]、全曲结构 [85][12]、评测组织化 [1][49]**。可控性线索可回溯至 Music SketchNet 的因子化表示 [25]。

### 8.2 数据集与基准

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| SongEval | 2025 | `> 待核实` | `> 待核实` | arXiv eess.AS 预印本，自称 benchmark dataset，**候选块未标注会议**（B 级）[80] | 高：直接命中"歌曲级美学评测"这一核心缺口 | ★★★★★：衡量"美学"维度时优先级最高的候选 | http://arxiv.org/abs/2505.10793v1 | 主张以主观/感知美学维度弥补 embedding 距离类客观指标的局限 [80] |
| AudioMOS Challenge 2025 | 2025 | `> 待核实` | `> 待核实` | arXiv cs.SD，**挑战官方 summary paper**（B 级）[49] | 高：首个合成音频自动主观质量预测挑战 | ★★★★★：获取 T2M 质量/对齐可比设定的关键文献 | http://arxiv.org/abs/2509.01336v1 | Track1：overall quality + textual alignment；Track2：Meta Audiobox Aesthetics 四维 [49] |
| AImoclips | 2025 | `> 待核实` | `> 待核实` | arXiv cs.SD v2，自称 benchmark（B 级）[68] | 中：补充"情绪传达"维度 | ★★★★☆：补全评测维度清单 | http://arxiv.org/abs/2509.00813v2 | 评估 T2M 向人类听者传达目标情绪的能力，指出情绪保真度相对被忽视 [68] |
| MusicEval | 2025 | `> 待核实` | `> 待核实` | arXiv 预印本 v2（B 级）[75] | 中：**候选块中唯一直接出现"MusicEval"名称的条目** | ★★★★☆：q4 明确指出 MusicEval 需另行核实，本条为唯一候选线索 | http://arxiv.org/abs/2501.10811v2 | 标题自述为"with Expert Ratings for Automatic Text-to-Music Evaluation"的生成音乐数据集 [75] |
| GlobalMood | 2025 | `> 待核实` | `> 待核实` | arXiv 预印本 v2（B 级）[96] | 中：跨文化音乐情绪识别基准 | ★★★☆☆：与"文化/流派公平性"缺口 [97] 呼应 | http://arxiv.org/abs/2505.09539v2 | 跨文化音乐情绪识别基准 [96] |
| AMT Challenge 2025 (Multi-Instrument Music Transcription) | 2025 | `> 待核实` | `> 待核实` | arXiv 预印本（B 级）[64] | 低-中：多乐器转写，与生成任务相邻 | ★★☆☆☆：仅在需要"生成↔转写"闭环时参考 | http://arxiv.org/abs/2603.27528v1 | 多乐器音乐转写挑战结果 [64] |
| AudioMOS Track1 参赛方案（ASTAR-NTU） | 2025 | `> 待核实` | `> 待核实` | arXiv cs.SD，自称获胜系统，**需官方结果交叉验证**（B 级）[50] | 中：自动化 TA/MI 评测的实践参考 | ★★★★☆：理解对齐指标实现细节 | http://arxiv.org/abs/2507.09904v1 | 双分支架构，使用 MuQ 与 RoBERTa 同时预测 MI 与 TA [50] |

> **明确未覆盖的数据集（`> 待核实`）**：MusicCaps、MTG-Jamendo、FMA 在候选块中**无任何条目**（q4 已确认此缺口）；MusicEval 仅有一条标题级线索 [75]，其数据构成、评分维度、是否覆盖人声与 full-song **均待核实**。候选块中**完全不存在**版权合规相关的评测数据集。

---

## 9. 方法与局限说明

1. **证据等级分布**：本报告 90% 以上引用为 arXiv 预印本（B 级）。仅 [12]（Interspeech 2025）、[22]（ICCV 2025）、[57]（MSR 2025）、[101]（JIPLP）为同行评审/期刊来源（A/B 级）。
2. **热度指标系统性缺失**：候选块**未对任何条目提供** citations、GitHub stars、下载量或榜单排名。因此本报告所有"热度证据"栏均标注 `> 待核实`，**未编造任何数字**。"关注度"评级依据仅限于该条目与主题的相关性及其在证据集中的位置，已在各处注明。
3. **产业与法律一手证据为零**：第 6 章整章、第 2 章大部分、第 5 章的法律事实部分（RIAA 诉讼、授权协议、平台政策、EU AI Act 条文日期）均无可核查来源，已全部标注 `> 待核实`。
4. **噪声过滤记录**：候选集中 [33]（灵巧手操作）、[88]–[95]（高能物理）、[19]（图像超分）、[107]（rip current 分割）、[69]（医学 CT）、[71]–[74]、[76]–[79]、[81]–[84] 等与本主题无关，已剔除，不作为任何论断依据。
5. **时间口径**：全文以 2026-10-04 为基准，"最新/近 1–2 年"指 2024-10 至 2026-10；凡候选块标注年份为 2026 的条目（如 [1][2][3][56]）均按实际发表时间视为本窗口内新近工作。

---

## 参考来源

[1] UT-AISTimprt submission for ICME 2026 Grand Challenge on Academic Text-to-Music Generation — http://arxiv.org/abs/2607.01669v1  
[2] Instrumental Text-to-Music Generation with Auxiliary Conditioning Branches — http://arxiv.org/abs/2605.21433v1  
[3] Improving Text-to-Music Generation with Human Preference Rewards — http://arxiv.org/abs/2606.21670v1  
[4] Story2MIDI: Emotionally Aligned Music Generation from Text — http://arxiv.org/abs/2512.02192v1  
[5] Data-Driven Analysis of Text-Conditioned AI-Generated Music: A Case Study with Suno and Udio — http://arxiv.org/abs/2509.11824v1  
[6] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1  
[12] Song Form-aware Full-Song Text-to-Lyrics Generation with Multi-Level Granularity Syllable Count Control — https://doi.org/10.21437/interspeech.2025-1247  
[14] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1  
[22] RapVerse: Coherent Vocals and Whole-Body Motion Generation from Text — https://doi.org/10.1109/iccv51701.2025.00941  
[25] Music SketchNet: Controllable Music Generation via Factorized Representations of Pitch and Rhythm — http://arxiv.org/abs/2008.01291v1  
[26] musif: a Python package for symbolic music feature extraction — http://arxiv.org/abs/2307.01120v1  
[27] Symbolic Music Representations for Classification Tasks: A Systematic Evaluation — http://arxiv.org/abs/2309.02567v2  
[30] Overview of AuTexTification at IberLEF 2023 — http://arxiv.org/abs/2309.11285v1  
[32] Diffusion-based Symbolic Music Generation with Structured State Space Models — http://arxiv.org/abs/2507.20128v2  
[35] Jukebox: A Generative Model for Music — http://arxiv.org/abs/2005.00341v1  
[38] MusicLM: Generating Music From Text — http://arxiv.org/abs/2301.11325v1  
[43] MART: Learning Hierarchical Music Audio Representations with Part-Whole Transformer — http://arxiv.org/abs/2312.06197v3  
[48] Instruct-MusicGen: Unlocking Text-to-Music Editing for Music Language Models via Instruction Tuning — http://arxiv.org/abs/2405.18386v3  
[49] The AudioMOS Challenge 2025 — http://arxiv.org/abs/2509.01336v1  
[50] ASTAR-NTU solution to AudioMOS Challenge 2025 Track1 — http://arxiv.org/abs/2507.09904v1  
[51] AI-Assisted Music Production: A User Study on Text-to-Music Models — http://arxiv.org/abs/2509.23364v1  
[52] Audio Prompt Adapter: Unleashing Music Editing Abilities for Text-to-Music with Lightweight Finetuning — http://arxiv.org/abs/2407.16564v2  
[53] ACE-Step: A Step Towards Music Generation Foundation Model — http://arxiv.org/abs/2506.00045v1  
[56] ACE-Step 1.5: Pushing the Boundaries of Open-Source Music Generation — http://arxiv.org/abs/2602.00744v3  
[57] The Ecosystem of Open-Source Music Production Software – A Mining Study on the Development Practices of VST Plugins on GitHub — https://doi.org/10.1109/msr66628.2025.00085  
[59] CultureMERT: Continual Pre-Training for Cross-Cultural Music Representation Learning — http://arxiv.org/abs/2506.17818v1  
[62] No Encore: Unlearning as Opt-Out in Music Generation — http://arxiv.org/abs/2509.06277v2  
[64] Advancing Multi-Instrument Music Transcription: Results from the 2025 AMT Challenge — http://arxiv.org/abs/2603.27528v1  
[67] Stable Audio Open — http://arxiv.org/abs/2407.14358v2  
[68] AImoclips: A Benchmark for Evaluating Emotion Conveyance in Text-to-Music Generation — http://arxiv.org/abs/2509.00813v2  
[75] MusicEval: A Generative Music Dataset with Expert Ratings for Automatic Text-to-Music Evaluation — http://arxiv.org/abs/2501.10811v2  
[80] SongEval: A Benchmark Dataset for Song Aesthetics Evaluation — http://arxiv.org/abs/2505.10793v1  
[85] Segment-Factorized Full-Song Generation on Symbolic Piano Music — http://arxiv.org/abs/2510.05881v1  
[86] Opening Musical Creativity? Embedded Ideologies in Generative-AI Music Systems — http://arxiv.org/abs/2508.08805v1  
[96] GlobalMood: A cross-cultural benchmark for music emotion recognition — http://arxiv.org/abs/2505.09539v2  
[97] Who Gets Heard? Rethinking Fairness in AI for Music Systems — http://arxiv.org/abs/2511.05953v1  
[98] Privacy and Copyright Protection in Generative AI: A Lifecycle Perspective — http://arxiv.org/abs/2311.18252v3  
[99] Towards Assuring EU AI Act Compliance and Adversarial Robustness of LLMs — http://arxiv.org/abs/2410.05306v1  
[100] An Analysis of the New EU AI Act and A Proposed Standardization Framework for Machine Learning Fairness — http://arxiv.org/abs/2510.01281v1  
[101] Music metadata improvement—copyright, fundamental rights and data law — https://doi.org/10.1093/jiplp/jpag041  
[103] Ethics Statements in AI Music Papers: The Effective and the Ineffective — http://arxiv.org/abs/2509.25496v1  
[105] Toward Interpretable Music Tagging with Self-Attention — http://arxiv.org/abs/1906.04972v1  
[106] End-to-end learning for music audio tagging at scale — http://arxiv.org/abs/1711.02520v4  
[108] AINL-Eval 2025 Shared Task: Detection of AI-Generated Scientific Abstracts in Russian — http://arxiv.org/abs/2508.09622v1  
[110] The Shape of Surprise: Structured Uncertainty and Co-Creativity in AI Music Tools — http://arxiv.org/abs/2509.25028v1  
[111] Predicting Startup-VC Fund Matches with Structural Embeddings and Temporal Investment Data — http://arxiv.org/abs/2511.23364v1

---

*Generated by research-bot · topic=`ai-音乐生成与音乐产业sunoudio版权诉讼发行与商业化` · depth=`standard` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`deepseek-v4-flash` · sources=115 · duration=517s · 2026-10-04T12:57:44+00:00*
