# 大模型与基础模型前沿调研报告（2024–2026）：推理与测试时计算、后训练、Agent、多模态、MoE 与扩展律、长上下文与效率

**元信息**：报告日期 2026-10-02（UTC）｜领域：人工智能 / 基础模型（Foundation Models）｜可引用来源：34 条编号来源（[1]–[34]）｜检索方式：多角度检索 + 候选证据块抽取（结构化 API 优先）｜证据覆盖审计见「摘要」小节｜术语对照：LLM（大语言模型）、VLA（Vision-Language-Action）、RLHF（Reinforcement Learning from Human Feedback，人类反馈强化学习）、RLVR（Reinforcement Learning with Verifiable Rewards，可验证奖励强化学习）、MoE（Mixture-of-Experts，混合专家）、CoT（Chain-of-Thought，思维链）、TTT/TTS（test-time training / test-time scaling，测试时训练/扩展）

---

## 摘要（Executive Summary）

本报告严格遵循「不编造、可核查、带证据分级」的写作纪律。需要首先向读者说明一个关键事实：**本次检索召回的证据与主题存在严重错配**。在 34 条可引用来源中，与「大模型/基础模型」六条主线直接相关者仅 16 条（[7][8][9][10][11][12][13][14][20][21][22][23][24][26][27][32]），其中能真正支撑技术结论的约 8 条（[8][20][21][23][24][26][27][32]）；旁及强化学习/机器人 3 条（[15][16][17]）；明显离题 15 条（[1]–[6] 为 2017 年形式化方法与 NLP 论文，[18][19][25] 为会议论文集/低资源语言工作坊/短视频参与度预测，[28]–[31][33][34] 为 Gaia 天体测量任务论文）。因此，本报告的定位是**「可核查证据地图 + 明确的待补检索清单」**，而非一份声称完整的领域综述。

可确证的结论（均有可用来源支撑）：

1. **推理效率正在成为「大型推理模型」独立的工程主线**：[21] 提出 ARS（Adaptive Reasoning Suppression，自适应推理抑制），针对高效大型推理语言模型（Large Reasoning LMs），说明「减少冗余推理 token」已被作为一等研究问题处理，而非仅仅靠模型变小。[21]
2. **测试时计算/测试时优化已外溢到安全领域**：[20] 的 MetaSC 将「测试时安全规范规格优化」作为方法框架，说明 test-time optimization 已不只是推理能力提升手段，也被用于对齐与安全约束。[20]
3. **RLVR 思路正在从「语言推理」外溢到「世界模型」训练**：[24] 的 RLVR-World 直接用强化学习训练世界模型，标题层面即体现「可验证奖励 / RL 训练目标替代纯监督」的迁移路径；其方法细节与验证强度需回到原文核实。[24]
4. **Agent/代码类评测正从静态数据集转向动态、可对抗加固的形态**：[27]（SWE-bench Goes Live!）与 [32]（SWE-ABS）共同指向同一个问题域——静态测试型基准（test-based benchmark）存在饱和、污染与成功率虚高风险。[27][32]
5. **多模态推理已形成「挑战赛 + 数据集 + 榜单」的组织形态**：[26] MARS2 2025 多模态推理挑战赛汇总数据集、方法、结果与展望；[14] 则把物理常识推理评测扩展到意大利语/英语并做人工标注，说明多语言+多模态评测正在同步扩张。[26][14]
6. **Transformer 作为「学术叙事中心」的量化证据**：[7] 统计 2009–2025 年 717 篇含 "All You Need" 的 arXiv 预印本，发现 2017 年原论文后呈指数增长（R² > 0.994），2025 年单年 200 篇，并指出其中遵循规范结构的论文里 "Attention" 被声称「必要」的频次最高（28 次）。[7]

必须明确标注为「证据缺口」的结论（本批证据**零覆盖**，一律 `> 待核实`）：

- 后训练中的 RLHF / DPO / 偏好优化一手进展，以及 RLVR 是否真实提升推理能力（vs. 仅改变采样分布）的对照实验证据；
- MoE 稀疏化架构演进、路由策略、MoE 与稠密模型的质量-效率权衡；
- 扩展律（scaling law）的新结论，包括 Chinchilla 之后的数据/计算最优配方；
- 长上下文（long-context）的真实有效性与「lost in the middle」类争议；
- 主流开源训练框架与推理引擎（如 HuggingFace Transformers、vLLM、llama.cpp）的 stars、最近提交、生态采用度等工程可用性指标；
- 上述缺口不能由种子资源清单替代，因为种子清单仅提供条目与链接，未提供可核验的热度/权威信号（见第六节，全部标注 `> 待核实`）。

---

## 一、关键前沿进展（近 1–2 年）

> 说明：以下条目按证据强度排序。本批来源全部为 arXiv 预印本 / SSRN 预印本 / 期刊摘要，**未见任何一条具备已确认的同行评审记录**，故权威证据等级最高为 B（arXiv 预印本），多数热度信号缺失。所有年份若未特别说明，均由 arXiv 编号（如 2505 → 2025-05）推断，精确提交日期 `> 待核实`。

| # | 名称（中英对照） | 年份 | 机构/作者 | 主线归属 | 证据强度 |
|---|---|---|---|---|---|
| F1 | ARS: Adaptive Reasoning Suppression for Efficient Large Reasoning Language Models（自适应推理抑制）[21] | 2025 | `> 待核实` | 推理与测试时计算 / 效率 | arXiv 预印本（B） |
| F2 | MetaSC: Test-Time Safety Specification Optimization for Language Models（测试时安全规格优化）[20] | 2025 | `> 待核实` | 后训练 / 测试时计算 / 安全 | arXiv 预印本（B） |
| F3 | RLVR-World: Training World Models with Reinforcement Learning（用 RL 训练世界模型）[24] | 2025 | `> 待核实` | 后训练（RLVR）/ 世界模型 | arXiv 预印本（B） |
| F4 | SWE-bench Goes Live!（动态化 SWE-bench）[27] | 2025 | `> 待核实` | Agent / 工具使用 / 评测 | arXiv 预印本（B，cs.SE） |
| F5 | SWE-ABS: Adversarial Benchmark Strengthening Exposes Inflated Success Rates on Test-based Benchmark（对抗式基准加固暴露虚高成功率）[32] | 2026 | `> 待核实` | 评测可靠性 / 争议 | arXiv 预印本（B，仅标题与题名信息） |
| F6 | MARS2 2025 Challenge on Multimodal Reasoning（多模态推理挑战赛）[26] | 2025 | `> 待核实` | 多模态 / 评测 | arXiv 预印本（B，cs.CV） |
| F7 | MRL 2025 Shared Task: Culturally Grounded Physical Commonsense Reasoning in Italian and English（多语言物理常识推理）[14] | 2025 | `> 待核实` | 多模态/多语言 / 评测数据集 | arXiv 预印本（B，cs.CL） |
| F8 | Making Large Language Models Better Reasoners with Alignment（用对齐提升推理）[23] | 2023 | `> 待核实` | 后训练（过渡期工作） | arXiv 预印本（B） |
| F9 | Dilated Neighborhood Attention Transformer（DiNAT，膨胀邻域注意力）[8] | 2022（v3 修订） | `> 待核实` | 架构 / 注意力效率 | arXiv 预印本（B） |

### 逐条四类可核查证据

**F1 ARS（自适应推理抑制）[21]**
- **热度证据**：`> 待核实`（候选块未给出 citations、GitHub star、下载量或榜单排名）[21]
- **权威证据**：arXiv 预印本（arXiv:2510.00071v2），本批证据未显示同行评审记录；作者与机构 `> 待核实` [21]
- **关注度**：`> 待核实`（无引用/star/榜单/社区讨论信号；仅知其针对「高效大型推理模型」这一 2025 年高关注问题域）[21]
- **推荐度**：★★★★☆——若关注「推理 token 成本控制 / 是否所有 token 都必要」这一 2025–2026 核心问题，此题名指向的研究问题高度相关，建议补读原文再引用结论。[21]

**F2 MetaSC（测试时安全规格优化）[20]**
- **热度证据**：`> 待核实` [20]
- **权威证据**：arXiv 预印本（arXiv:2502.07985v2），非同行评审；作者/机构 `> 待核实` [20]
- **关注度**：`> 待核实`（无热度信号）[20]
- **推荐度**：★★★★☆——把「测试时计算」用于安全规格优化，是 test-time 方法向对齐场景外溢的代表，与「后训练 + 测试时计算」交叉主题相关度高。[20]

**F3 RLVR-World（用 RL 训练世界模型）[24]

## 参考来源

[1] The 4th Reactive Synthesis Competition (SYNTCOMP 2017): Benchmarks, Participants & Results — http://arxiv.org/abs/1711.11439v1
[2] Ghosts of Jupiter's past: is 2017 UV43 a relative of comet Shoemaker-Levy 9? — http://arxiv.org/abs/1712.03230v2
[3] EmoAtt at EmoInt-2017: Inner attention sentence embedding for Emotion Intensity — http://arxiv.org/abs/1708.05521v1
[4] Pre-proceedings of the 27th International Symposium on Logic-Based Program Synthesis and Transformation (LOPSTR 2017) — http://arxiv.org/abs/1708.07854v2
[5] ConceptNet at SemEval-2017 Task 2: Extending Word Embeddings with Multilingual Relational Knowledge — http://arxiv.org/abs/1704.03560v2
[6] SU-RUG at the CoNLL-SIGMORPHON 2017 shared task: Morphological Inflection with Attentional Sequence-to-Sequence Models — http://arxiv.org/abs/1706.03499v1
[7] "All You Need" is Not All You Need for a Paper Title: On the Origins of a Scientific Meme — http://arxiv.org/abs/2512.19700v1
[8] Dilated Neighborhood Attention Transformer — http://arxiv.org/abs/2209.15001v3
[9] Attention is All You Need... Unless You Are a CISO: The Inherent Incompatibility Between Transformer Architectures and Zero-Trust Environments — https://doi.org/10.2139/ssrn.5967774
[10] Attention via Synaptic Plasticity is All You Need A Biologically Inspired Spiking Neuromorphic Transformer — https://doi.org/10.2139/ssrn.6096874
[11] Failure Is All You Need — Attention as Reverse Diffusion: A Unified Geometric Control Law for Transformer Dynamics — https://doi.org/10.2139/ssrn.7499639
[12] 1882-P: Attention Is All You Need: Temporal Transformer-Based Personalization of Insulin Delivery Parameters from CGM and Pump Data — https://doi.org/10.2337/db26-1882-p
[13] Navigating the State of Cognitive Flow: Context-Aware AI Interventions for Effective Reasoning Support — http://arxiv.org/abs/2504.16021v1
[14] Culturally Grounded Physical Commonsense Reasoning in Italian and English: A Submission to the MRL 2025 Shared Task — http://arxiv.org/abs/2510.22631v1
[15] Value Bonuses using Ensemble Errors for Exploration in Reinforcement Learning — http://arxiv.org/abs/2602.12375v1
[16] The Open Ant: A Robot Platform for Reinforcement Learning Research — http://arxiv.org/abs/2607.18488v1
[17] Causal-Paced Deep Reinforcement Learning — http://arxiv.org/abs/2507.02910v1
[18] ACM COMPUTE 2025 Best Practices Track Proceedings — http://arxiv.org/abs/2512.02349v2
[19] Overview of the First Workshop on Language Models for Low-Resource Languages (LoResLM 2025) — http://arxiv.org/abs/2412.16365v1
[20] MetaSC: Test-Time Safety Specification Optimization for Language Models — http://arxiv.org/abs/2502.07985v2
[21] ARS: Adaptive Reasoning Suppression for Efficient Large Reasoning Language Models — http://arxiv.org/abs/2510.00071v2
[22] AIn't Nothing But a Survey? Using Large Language Models for Coding German Open-Ended Survey Responses on Survey Motivation — http://arxiv.org/abs/2506.14634v3
[23] Making Large Language Models Better Reasoners with Alignment — http://arxiv.org/abs/2309.02144v1
[24] RLVR-World: Training World Models with Reinforcement Learning — http://arxiv.org/abs/2505.13934v2
[25] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1
[26] MARS2 2025 Challenge on Multimodal Reasoning: Datasets, Methods, Results, Discussion, and Outlook — http://arxiv.org/abs/2509.14142v1
[27] SWE-bench Goes Live! — http://arxiv.org/abs/2505.23419v2
[28] The Gaia mission — http://arxiv.org/abs/1609.04153v1
[29] Gaia Data Release 3: The Galaxy in your preferred colours. Synthetic photometry from Gaia low-resolution spectra — http://arxiv.org/abs/2206.06215v2
[30] Gaia Data Release 2. Summary of the contents and survey properties — http://arxiv.org/abs/1804.09365v2
[31] Gaia Data Release 1. Summary of the astrometric, photometric, and survey properties — http://arxiv.org/abs/1609.04172v1
[32] SWE-ABS: Adversarial Benchmark Strengthening Exposes Inflated Success Rates on Test-based Benchmark — http://arxiv.org/abs/2603.00520v1
[33] Gaia Data Release 3: Exploring and mapping the diffuse interstellar band at 862 nm — http://arxiv.org/abs/2206.05536v1
[34] Gaia Data Release 2: Kinematics of globular clusters and dwarf galaxies around the Milky Way — http://arxiv.org/abs/1804.09381v3


---

*Generated by research-bot · topic=`ai` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading · model=`deepseek-v4-flash` · sources=34 · duration=170s · 2026-10-02T10:48:01+00:00*
