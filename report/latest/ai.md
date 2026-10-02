# 人工智能（基础模型）前沿调研报告：测试时计算与推理、RLVR 后训练、Agent 与工具使用、多模态、MoE 与长上下文

**日期**：2026-10-02（UTC） | **领域**：AI 基础模型（Foundation Models / LLM） | **检索源数量**：可用引用编号 35 条（[1]–[35]），其中与本主题直接相关者约 13 条 | **证据等级基线**：本次全部可用来源均为 arXiv 预印本或论文集条目（B 级为主），**未获得任何 A 级同行评审期刊论文的直接全文证据**

---

## 摘要（Executive Summary）

1. **最重要的结论是证据层面的，而非技术层面的**：本次候选证据池与研究主题存在**大面积错配**。在 35 条可用来源中，可直接支撑「测试时计算 / RLVR 后训练 / Agent 工具使用 / MoE / 多模态与长上下文效率」主题的仅约 13 条（[5][6][7][9][10][11][13][14][15][16][24][29][35]），其余 22 条分别属于计算机教育、凝聚态物理、图像超分挑战赛、情感强度分析、低资源语言研讨会等无关领域（[1][2][4][8][17][18][19][20][21][22][23][25][26][27][28][30][31][32][33][34]），其中 [17] 更是一篇**已撤回论文**（标题即 "This paper has been withdrawn"）。**热度证据（citations/stars）在全部候选块中均为空字段**，因此本报告中所有热度类论断一律标注 `> 待核实`，不编造任何数字。
   - 热度：`> 待核实`（候选块无 citations/stars 字段）｜权威：候选块为 arXiv 元数据 [1]–[35]｜关注度：低（主题重叠率约 37%）｜推荐度：★5 —— 该判断决定了本报告必须以「缺口清单」为主要交付物之一。

2. **可确认的前沿信号集中在四条线**：
   - **测试时计算的焦点已从「算得多」转向「何时算、算多少」**：[29] 提出 Sleep-time Compute，把部分计算从测试时前移到空闲期；[35] 直接研究 Test-Time Compute 的「思考最优扩展」；[11] 把 RLVR 的训练信号调度纳入时间维度。
   - **推理效率开始正面处理「过度思考（overthinking）」**：[15] 提出自适应推理抑制，[14] 通过正则化提示优化压缩推理 token 成本。
   - **RLVR 概念外溢到非语言模型**：[10] 用强化学习训练世界模型（RLVR-World）。
   - **推理服务栈从「引擎」升级为「控制平面」**：[5] 描述 vLLM → llm-d 的分布式控制化演进，[6] 给出 vLLM 与 HuggingFace TGI 的第三方性能对比，[7] 用 33,228 个 PR 的纵向数据刻画 vLLM/SGLang 的 agentic coding 协作模式。

3. **必须明确标注为证据缺口的领域**：**MoE 架构与路由、MoE 扩展律、多模态基础模型能力、长上下文「有效长度」、社区关心的主流基准（MMLU/MMLU-Pro、GPQA、AIME、SWE-bench、ARC-AGI、τ-bench、AgentBench、LIBERO、SimplerEnv）在本次证据池中均无一手评测证据**。本报告第五节与第四节相应部分以「待核实 + 补检索建议」形式呈现，不做任何结论性陈述。`> 待核实`

---

## 一、关键前沿进展（近 1–2 年）

> 判定口径：以来源的 arXiv 提交/修订时间戳为准（一手元数据），而非模型训练知识。时间窗取 2024-10 至 2026-10（当前日期 2026-10-02），并对 2024 年上半年的条目单列「过渡期节点」。

### 1.1 时间线（按证据强度分层）

| 时间 | 节点 | 一句话贡献 | 证据强度 | 来源 |
|---|---|---|---|---|
| 2024-01 | Beyond Chinchilla-Optimal | 在缩放律中显式计入**推理成本**，挑战纯训练算力最优口径 | 标题级（B） | [24] |
| 2024-05 | OpenRLHF | 面向 RLHF 的易用/可扩展/高性能训练框架（v6 持续更新） | 标题级（B） | [9] |
| 2025-03 | LongEval @ CLEF 2025 | 面向 IR 模型的**纵向**性能评测方法学 | 标题级（B） | [12] |
| 2025-04 | Sleep-time Compute | 在测试时推理扩展之外，新增「睡眠时间预计算」维度 | 标题级（B） | [29] |
| 2025-05 | RLVR-World | 将 RLVR 范式用于**世界模型**训练 | 标题级（B） | [10] |
| 2025-10 | ARS | 自适应抑制推理冗余，直面 overthinking 与效率权衡 | 摘要级（B） | [15] |
| 2025-11 | vLLM vs TGI | 推理服务系统的第三方对比性能研究 | 标题级（B/C） | [6] |
| 2025-12 | 2025 Foundation Model Transparency Index | 年度透明度指数第三版 | 摘要级（B） | [3] |
| 2026-04 | CROP | 用正则化提示优化降低推理 token 成本 | 摘要级（B） | [14] |
| 2026-05 | RLVR Temporal Scheduling | RLVR 训练中的**时序调度**（"not only where, but when"） | 标题级（B） | [11] |
| 2026-08 | Agentic Coding 纵向分析 | 33,228 个 vLLM/SGLang PR 的人机协作实证 | 标题级（B） | [7] |
| 2026-09 | Inference Control Plane | 推理从引擎局部优化转向分布式控制问题 | 摘要级（B） | [5] |
| 时间待核实 | Thinking-Optimal Scaling of TTC | 测试时计算的思考最优扩展 | 标题级（会议论文集条目） | [35] |

- 热度：`> 待核实`（全部候选块 citations 字段为空）｜权威：多为 arXiv 预印本（cs.AI/cs.CL/cs.CV），[35] 为 DOI 指向的会议论文集条目，未见同行评审标注｜关注度：中 —— 依据为「测试时计算」与「vLLM 生态」是当前社区高频讨论主题（[5][7][29][35] 集中出现）｜推荐度：★★★ —— 时间线可用于定位检索方向，但单条证据强度均不足以支撑 SOTA 结论。

### 1.2 被明确排除的「伪相关」信号

- **[2] NTIRE 2025 图像超分挑战赛**、**[8] ACM MM 2025 事件增强图像分析挑战赛**：属计算机视觉竞赛结果，**不构成基础模型多模态能力证据**。`> 待核实`
- **[4] VLSP 2025 越南语多模态法律问答**：属领域应用 shared task，覆盖面窄，不能外推为多模态基础模型进展。
- **[16] "All You Need" is Not All You Need**：属科学计量学（cs.CY），其对 Transformer 的意义仅在于**量化命名范式的传播**（分析 2009–2025 年 717 篇含 "All You Need" 的 arXiv 预印本，报告指数增长趋势；具体拟合系数被摘要截断，`> 待核实`），可作为 Transformer 影响力的**间接**证据，但**不能作为技术进展证据**。

---

## 二、推理与测试时计算

### 2.1 已获证据支持的三条子线索

**（1）测试时计算的时间维度被打开：从「测试时」到「睡眠时」。**
[29] 的标题即指出研究边界为 "Beyond Inference Scaling at Test-time"，提出 Sleep-time Compute 概念。
- 热度：`> 待核实`｜权威：arXiv 预印本 [29]，未见 venue 标注｜关注度：中 —— 依据为「测试时计算扩展」是该窗口内的显性热点（[29][35] 同期出现）｜推荐度：★★★★ —— 直接命中本报告第二节主题，是当前证据池中最贴题的一条。

**（2）测试时计算的「最优思考量」问题被形式化。**
[35] 直接以 "Towards Thinking-Optimal Scaling of Test-Time Compute for LLM Reasoning" 为题，指向「推理链长度/采样量并非越多越好」这一命题。
- 热度：`> 待核实`（DOI 条目，无引用数）｜权威：`> 待核实`（条目形态为会议论文集，具体 venue 与评审状态未在证据中给出）｜关注度：中 —— 与 [15] 的 overthinking 问题构成同一议题的两面｜推荐度：★★★ —— 主题高度相关，但权威性未能确认。

**（3）推理冗余（overthinking）被作为一等工程问题处理。**
[15]（ARS）明确指出大型推理模型（LRLMs/LRMs）"因过度思考而存在显著计算低效"，现有高效推理方法需在推理质量与推理开销之间取得平衡；该文提出自适应推理抑制（Adaptive Reasoning Suppression）。
[14]（CROP）从提示优化角度指出：现有自动提示优化（APO）框架"以牺牲长推理链的生成为代价、只追求任务精度"，导致延迟与 token 成本上升；该文用正则化提示优化实现 token 高效推理。
- 热度：`> 待核实`｜权威：均为 arXiv 预印本（[15] cs.AI，[14] cs.CL），无同行评审标注｜关注度：中 —— overthinking 已成为效率方向的共识性问题（[14][15] 独立提出）｜推荐度：★★★★ —— 两篇构成「抑制推理」与「优化提示」的互补视角，是推理效率章节的一手素材。

### 2.2 测试时计算「扩展律」本身：证据不足

[24] 从**缩放律**角度提出应把推理成本计入语言模型缩放律（"Beyond Chinchilla-Optimal: Accounting for Inference in Language Model Scaling Laws"）。这为「推理期算力分配是否应改变训练期最优配比」提供了理论入口，但**本次证据池中没有任何一条给出测试时计算扩展律的经验曲线（如 accuracy vs. 采样数/搜索预算的拟合结论）**。`> 待核实`
- 热度：`> 待核实`｜权威：arXiv 预印本（v3）[24]，属缩放律方向的直接续作｜关注度：中｜推荐度：★★★★ —— 是把「测试时计算」与「扩展律」两节打通的关键引用，但需补检索其同行评审版本与后续引用文献。

### 2.3 检索缺口（本节必须补检）

1. 缺**采样/搜索策略对比**（best-of-n、self-consistency、tree search、verifier-guided）的一手口径。
2. 缺**推理算力口径**（生成 token 数、pass@k 预算、单题 FLOPs）的可比数据。
3. 缺 [29][35] 的**全文精读**（本轮仅获得标题级/条目级证据）。`> 待核实`

---

## 三、后训练：RLHF / RLVR / 偏好优化

### 3.1 框架层：OpenRLHF

[9]（OpenRLHF，v6）提供了本方向最明确的工程栈证据：定位为"easy-to-use, scalable and high-performance RLHF framework"。
- 热度：`> 待核实`（候选块未提供 stars/citations；GitHub 数据本轮未采集）｜权威：arXiv 预印本 [9]，属框架类论文，通常非同行评审主线｜关注度：中高 —— 依据为 RLHF 框架是社区实际训练入口，且在本次证据池中以 v6 形式持续更新，表明项目仍在维护｜推荐度：★★★★ —— 后训练工程栈章节的必要引用，但**可复现性、许可协议、star 数均需另行核查**。`> 待核实`

### 3.2 算法与范式层：RLVR 的两条非典型证据

**（1）RLVR 越出语言模型边界：RLVR-World。**
[10] 标题为 "RLVR-World: Training World Models with Reinforcement Learning"，把「可验证奖励」的强化学习思路用于**世界模型**训练，而非文本推理。
- 热度：`> 待核实`｜权威：arXiv 预印本（v2）[10]｜关注度：中 —— 作为 RLVR 概念外溢的信号具有前瞻指示性｜推荐度：★★★★ —— 若研究目标是 RLVR 的方法论边界，这是本次证据池中信息量最高的一条。

**（2）RLVR 的训练调度问题被显式提出。**
[11] 标题 "Not only where, But when: Temporal Scheduling for RLVR" 表明：RLVR 的研究重点从「奖励在哪里施加（where）」扩展到「**何时**施加（when）」。
- 热度：`> 待核实`｜权威：arXiv 预印本 [11]｜关注度：中 —— 属于 RLVR 训练的细化方向，非主流综述常见条目｜推荐度：★★★★ —— 直接命中本报告标题中的 RLVR 后训练主题。

### 3.3 对齐作为推理增强的早期线索（过渡期节点）

[13]（2023）提出 "Making Large Language Models Better Reasoners with Alignment"，摘要指出近期研究显示在含 Chain-of-Thought（CoT）数据上微调 LLM 可提升推理能力，该文从对齐角度切入。
- 热度：`> 待核实`｜权威：arXiv 预印本（cs.CL）[13]，2023 年，时效性偏旧｜关注度：低（时间上已属前 RLVR 时代）｜推荐度：★★★ —— 可作为「对齐 → 推理增强」脉络的早期节点，但不能代表 2024–2026 的 RLVR 进展。

### 3.4 本节关键缺口

- **没有任何一条证据覆盖 GRPO / DPO / 偏好优化的算法变体、训练数据规模、对照 baseline 或训练算力口径。** [9][10][11][13] 仅提供框架、范式外溢与调度视角。`> 待核实`
- **「RLVR 是否真正提升推理能力，还是蒸馏/采样放大的伪提升」这一核心争议，在本次证据池中完全无支撑。** `> 待核实`
- 需要补检的关键词：`GRPO`、`RLVR verification reward`、`pass@k distillation`、`DeepSeek-R1`、`Kimi k1.5`、`Tulu 3`。`> 待核实`

---

## 四、Agent、工具使用与评测

### 4.1 已获证据：Agent 协作的真实工程信号（而非 benchmark 分数）

[7] 提供了本节唯一的高信息量证据：对 **vLLM 与 SGLang 两个推理引擎仓库的 33,228 个 Pull Request** 进行纵向分析，主题为 "Engineering Signals of Human-AI Collaboration in the Agentic Coding Era"，并讨论其对生物医学 AI Agent 与生信流水线开发的启示。
- 热度：`> 待核实`（无 stars/citations 字段）｜权威：arXiv 预印本（2026-08），属实证软件工程 + AI 交叉研究，未见 venue 标注｜关注度：中 —— 依据为样本量（33,228 PR）与研究对象（两个高活跃推理引擎仓库）本身构成社区关注度的代理信号，但**本轮无榜单或新闻热度数据**｜推荐度：★★★★ —— 是本次证据池中**唯一**以大规模实证数据刻画「Agent 参与真实工程」的条目，价值在于提供**可复现的量化研究设计**，而非 Agent 能力排名。

> 方法论提醒：该文的贡献是「Agent 在开源工程中的协作模式」，**不能**被引用为 Agent 在 SWE-bench / AgentBench / τ-bench 上的性能证据。两者口径完全不同。

### 4.2 工具协议与 Agent 框架：本轮无证据

- **MCP（Model Context Protocol）**、function calling 协议、多步工具链编排、Agent 记忆与规划框架：本次证据池**零覆盖**。`> 待核实`
- 种子资源中未提供 MCP 或 Agent 框架条目，因此**不列入任何表格**，避免编造链接。

### 4.3 基准体系的证据现状

社区常引用的 Agent 相关基准（SWE-bench、τ-bench、AgentBench、ARC-AGI）在本次证据池中**无任何一手评测结果**。可用信息仅来自种子资源提供的 SWE-bench 仓库链接（标注为「代码/Agent 评测」），该信息**未经过本次检索验证**，已在下节表格中标注来源性质。
- 热度：`> 待核实`｜权威：种子资源标注，非本次检索所得｜关注度：

## 参考来源

[1] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1
[2] NTIRE 2025 Challenge on Image Super-Resolution (x4): Methods and Results — http://arxiv.org/abs/2504.14582v3
[3] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1
[4] VLSP 2025 MLQA-TSR Challenge: Vietnamese Multimodal Legal Question Answering on Traffic Sign Regulation — http://arxiv.org/abs/2510.20381v1
[5] From Inference Engine to Inference Control Plane: Connecting vLLM, llm-d, and the Evolution of Efficient Distributed LLM Serving — http://arxiv.org/abs/2609.23130v1
[6] Comparative Analysis of Large Language Model Inference Serving Systems: A Performance Study of vLLM and HuggingFace TGI — http://arxiv.org/abs/2511.17593v1
[7] Engineering Signals of Human-AI Collaboration in the Agentic Coding Era: A Longitudinal Analysis of 33,228 Pull Requests from vLLM and SGLang with Implications for Biomedical AI Agents and Bioinformatics Pipeline Developmen — http://arxiv.org/abs/2608.13884v1
[8] Event-Enriched Image Analysis Grand Challenge at ACM Multimedia 2025 — http://arxiv.org/abs/2508.18904v1
[9] OpenRLHF: An Easy-to-use, Scalable and High-performance RLHF Framework — http://arxiv.org/abs/2405.11143v6
[10] RLVR-World: Training World Models with Reinforcement Learning — http://arxiv.org/abs/2505.13934v2
[11] Not only where, But when: Temporal Scheduling for RLVR — http://arxiv.org/abs/2605.25381v1
[12] LongEval at CLEF 2025: Longitudinal Evaluation of IR Model Performance — http://arxiv.org/abs/2503.08541v1
[13] Making Large Language Models Better Reasoners with Alignment — http://arxiv.org/abs/2309.02144v1
[14] CROP: Token-Efficient Reasoning in Large Language Models via Regularized Prompt Optimization — http://arxiv.org/abs/2604.14214v1
[15] ARS: Adaptive Reasoning Suppression for Efficient Large Reasoning Language Models — http://arxiv.org/abs/2510.00071v2
[16] "All You Need" is Not All You Need for a Paper Title: On the Origins of a Scientific Meme — http://arxiv.org/abs/2512.19700v1
[17] This paper has been withdrawn — http://arxiv.org/abs/cond-mat/0309395v2
[18] The 4th Reactive Synthesis Competition (SYNTCOMP 2017): Benchmarks, Participants & Results — http://arxiv.org/abs/1711.11439v1
[19] EmoAtt at EmoInt-2017: Inner attention sentence embedding for Emotion Intensity — http://arxiv.org/abs/1708.05521v1
[20] Ghosts of Jupiter's past: is 2017 UV43 a relative of comet Shoemaker-Levy 9? — http://arxiv.org/abs/1712.03230v2
[21] Erratum to "The Homogeneous Coordinate Ring of a Toric Variety", along with the original paper — http://arxiv.org/abs/alg-geom/9210008v3
[22] Pre-proceedings of the 27th International Symposium on Logic-Based Program Synthesis and Transformation (LOPSTR 2017) — http://arxiv.org/abs/1708.07854v2
[23] ConceptNet at SemEval-2017 Task 2: Extending Word Embeddings with Multilingual Relational Knowledge — http://arxiv.org/abs/1704.03560v2
[24] Beyond Chinchilla-Optimal: Accounting for Inference in Language Model Scaling Laws — http://arxiv.org/abs/2401.00448v3
[25] Navigating the State of Cognitive Flow: Context-Aware AI Interventions for Effective Reasoning Support — http://arxiv.org/abs/2504.16021v1
[26] ACM COMPUTE 2025 Best Practices Track Proceedings — http://arxiv.org/abs/2512.02349v2
[27] Culturally Grounded Physical Commonsense Reasoning in Italian and English: A Submission to the MRL 2025 Shared Task — http://arxiv.org/abs/2510.22631v1
[28] AIn't Nothing But a Survey? Using Large Language Models for Coding German Open-Ended Survey Responses on Survey Motivation — http://arxiv.org/abs/2506.14634v3
[29] Sleep-time Compute: Beyond Inference Scaling at Test-time — http://arxiv.org/abs/2504.13171v1
[30] Overview of the First Workshop on Language Models for Low-Resource Languages (LoResLM 2025) — http://arxiv.org/abs/2412.16365v1
[31] Soft Inductive Bias Approach via Explicit Reasoning Perspectives in Inappropriate Utterance Detection Using Large Language Models — http://arxiv.org/abs/2512.08480v1
[32] Instituto de Telecomunicações at IWSLT 2025: Aligning Small-Scale Speech and Language Models for Speech-to-Text Learning — http://arxiv.org/abs/2506.17019v1
[33] Value Bonuses using Ensemble Errors for Exploration in Reinforcement Learning — http://arxiv.org/abs/2602.12375v1
[34] The Open Ant: A Robot Platform for Reinforcement Learning Research — http://arxiv.org/abs/2607.18488v1
[35] Towards Thinking-Optimal Scaling of Test-Time Compute for LLM Reasoning — https://doi.org/10.52202/085713-1452


---

*Generated by research-bot · topic=`ai` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading · model=`deepseek-v4-flash` · sources=35 · duration=171s · 2026-10-02T11:10:30+00:00*
