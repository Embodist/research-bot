# Vision-Language-Action (VLA) 基础模型调研报告：前沿进展、方法范式、工程栈与开放问题

> **日期**：2026-10-02（UTC）｜**领域**：具身智能 / VLA 基础模型（Vision-Language-Action）｜**可引用编号来源**：36 条（其中与主题直接相关约 20 条）＋ 人工维护种子资源 8 篇论文 / 5 个开源项目 / 5 个数据集
> **证据基线**：本报告严格只引用下方 [1]–[36] 编号来源与提示中给出的种子资源链接。凡无一手材料支撑者一律标注 `> 待核实`。

---

## 摘要（Executive Summary）

1. **VLA 范式的一手奠基证据明确可查**：RT-2 论文摘要直接表述"把互联网规模训练的视觉语言模型纳入端到端机器人控制以提升泛化"，并给出 arXiv 一手预印本 [14] 与 CoRL 2023 同行评审版本（PMLR v229）[16]，是本批证据中证据等级最高（A 级）的 VLA 源头工作。
2. **本批证据中，VLA 主线模型的覆盖存在重大缺口**：子问题点名的主线模型 **π0 / π0-FAST、OpenVLA-OFT、GR00T N1、Gemini Robotics、RDT-1B 均无一手材料**，因此无法就其架构、动作表征与真机部署差异作出可核查结论。唯一与 π0 主线直接相关的证据是第三方竞赛方案在 **Pi0.5** 架构上做任务适配并获 2025 BEHAVIOR Challenge 第 1 名 [12]，说明该架构已被第三方复用作基座，而非停留在论文原型。
3. **动作表征侧出现两条可核查的新线索**：(a) "VLM 主干 + 扩散式轨迹解码器"，并可在**推理时以不改变权重**的方式偏置动作输出（注意力干预，带剂量响应与层级消融）[3]；(b) flow matching 基座被外部团队复用于长程双臂任务 [12]。离散动作 token 路线的具体细节仅有种子资源备注，`> 待核实`。
4. **架构取向出现分化**：一端是端到端连续动作解空间的 vanilla VLA，另一端是 **工具注入 / agentic 化**（ART 框架）[9]；但 [9] 的摘要片段被截断（原文 "ART reduces t..."），定量收益不可引用，`> 待核实`。
5. **工程侧**：OpenVLA 官方仓库可核查地记录了 2024-06-13 初始发布与 2024-07-08 新增 LoRA / 全量微调章节 [25]，其项目页给出 **LoRA 仅微调 1.4% 参数即匹配全量微调性能**的说法 [28]；另有 StarVLA（Lego-like codebase）[10]、rMuscle（推理效率）[4]、AWS SageMaker LoRA 微调实践 [31] 等工程线索。
6. **评测仍以仿真/合成为主**：本批证据中唯一具名评测场域是 BEHAVIOR Challenge（photo-realistic simulation）[12] 与 Physical AI World Model Synthetic 合成数据集 [3]，**候选证据中没有任何真机部署成功率数据**，论文宣称与真机表现之间的差距 `> 待核实`。
7. **存在一条值得追踪的争议线索**：IEEE RA-L 2026 论文 "Robot Independent Intelligence: When Language Vanishes in Vision-language-action Models" [15]（同论文另有补充材料 [17][19][21]）质疑语言模态在 VLA 中的实际作用；但本批仅获取到补充材料链接，正文、作者与实验结论均未获取，`> 待核实`。

**证据与检索质量说明（供读者校准置信度）**：
- 本批来源中**大量条目为搜索引擎跳转链接（so.com）**，如 [1][4][7][10][26][29][35]，属 D 级证据，仅作线索，不能单独支撑结论。
- [27][30][33][36] 为与 VLA 无关的 LLM/LoRA 文献（如中文拼写纠错 [27]、尼泊尔语理解 [30]、波束成形 [36]），**已识别为检索噪声并排除**。
- [15][17][19][21] 实为同一篇论文的正文/补充材料入口，本批仅见附件文件名，正文缺失。
- 因此本报告在"最新进展"部分**只陈述本批已获证据可支撑的内容**，其余全部显式标注缺口。

---

## 一、关键前沿进展（近 12-24 个月）

### 1.1 主线基座被第三方复用：π0 系列（Pi0.5）
- **[12]（2025，preprint）** Task adaptation of Vision-Language-Action model: 1st Place Solution for the 2025 BEHAVIOR Challenge —— 方案建立在 **Pi0.5 架构**之上，获 2025 BEHAVIOR Challenge 第 1 名。该基准含 **50 个多样化长程家庭任务**，要求双臂操作、导航与上下文感知决策；作者的首要贡献是为 flow matching 引入 **correlated noise（相关噪声）**[12]。
- **意义**：这是本批证据中唯一直接构建在 π0 主线架构之上、并给出大规模长程基准结果的工作，可作为"π0 系列具备可复用基座属性"的关键证据（证据等级 B/C：arXiv 预印本 + 竞赛方案）。

### 1.2 动作表征可控性：VLM 主干 + 扩散轨迹解码器 + 推理时注意力干预
- **[3]（2026，preprint）** Inference-Time Attention Steering for Vision-Language-Action Driving Models —— 把 VLA 推理阶段与基于扩散的 **trajectory decoder** 耦合；在 **Alpamayo-R1 的 Qwen3-VL 主干**上，对检测器定位的交通参与者视觉 token 施加**有界加性 pre-softmax attention bias**，以 fail-open forward pre-hook 实现、**不改变任何权重**[3]。
- **量化结果（据原文报告）**：在 Physical AI World Model Synthetic 数据集的 **50 个换道场景**中，轨迹解码器对偏置幅度呈单调剂量响应，且在每个测试幅度上都与成对零偏置对照可区分；平均位移约 **17 cm**，clamp 处横向偏移最高约 **140 cm**；层级消融将动作相关信号定位于 **late layers**[3]。
- **限定**：仅在单一模型 + 合成数据 + 50 场景验证，缺乏跨模型、跨本体证据（见第六节）。

### 1.3 架构分化：VLA 的 agentic 化与工具注入
- **[9]（2026，preprint）** Evolve Vision-Language-Action Model into an Agent with On-the-fly Tool-use —— 提出 **Agentic Robot with Tool-use (ART)**，定位为 tool-injection 框架，可调优任意 VLA 模型以利用 off-the-shelf 工具模块，覆盖低层视觉、高层 affordance 与 embodiment 增强；文中与"拥有整段连续动作解空间的 vanilla VLA 模型"对比 [9]。
- `> 待核实`：候选片段在 "ART reduces t..." 处被截断，工具注入相对 vanilla VLA 的**具体收益数值与指标口径不可引用**，需取全文核实。

### 1.4 动作的语义分解与参数高效适配（VLM 路线）
- **[6]（2026，preprint）** Compositional Context Fine-Tuning VLM for Complex Assembly Action Understanding from Videos —— 提出 **CCFT**，把装配动作分解为语义要素（Verb、Object、Tool），用模板化问答对微调 VLM 逐个识别动作要素以实现近确定性输出；并提出 **Layer-Partitioned Alternating Training (LP-AT)**，把不同模型层分配给特定动作要素识别，以在有限数据下完成高效多任务学习 [6]。
- **限定**：该工作解决的是**动作理解/识别**，**不产出可执行动作策略**，不能与端到端 VLA 政策混为一谈。

### 1.5 效率与工程化：本批的"效率线"线索
- **[2]/[5]（2025）** A Survey on Efficient Vision-Language-Action Models —— 本批检索到该综述的摘要页 [2] 与 HTML 版本 [5]，为效率方向提供入口性线索（具体分类与数字未获取）。
- **[4]** rMuscle: Robotic Muscle Memory for Efficient VLA Model Inference —— 仅见标题（搜索引擎跳转链接），属 D 级线索，`> 待核实`。
- **[10]** StarVLA: A Lego-like Codebase for VLA Model Developing —— 仅见标题与跳转链接，`> 待核实`。
- **[32]（2026）** An Empirical Study on Stage-Information Interfaces for VLA Fine-Tuning —— 仅见标题（arXiv 2607.13605v1），`> 待核实`。
- **[29]（2026）** Enhancing Linguistic Generalization of VLA: Fine-Tuning OpenVLA via Synthetic Instruction Augmentation —— 仅见标题（arXiv 2603.16044v1），`> 待核实`。
- **[31]** Fine-tuning OpenVLA on Amazon SageMaker AI with LoRA —— 云厂商工程实践教程，属 B/C 级工程证据（内容未全文获取）。

### 1.6 综述与本体外延
- **综述入口（本批共 4 条）**：[2][5] 高效 VLA 综述；**[8]** Survey of Vision-Language-Action Models for Embodied Manipulation（arXiv 2508.15201）；**[11]** VLA in Robotics: A Survey of Datasets...（arXiv 2604.23001v1）；**[20]** Large VLM-based VLA Models for Robotic Manipulation（arXiv 2508.13073v3）。
  `> 待核实`：上述综述的 taxonomy 与结论未逐篇精读，本报告的范式对比以本批已取证的一手材料为限。
- **本体外延线索**：**[7]** AutoVLA（端到端自动驾驶 + 自适应推理 + 强化微调，仅见标题/跳转链接）；**[22]** VLA Models for Unmanned Aerial ...（MDPI Drones, 10(6):412）；**[13]** Daily Assistive View Control Learning of Low-Cost Low-Rigidity Robot via Large-Scale VLM（IEEE Humanoids 2023, DOI 10.1109/humanoids57100.2023.10375239）。三条均仅有标题/DOI 级信息，`> 待核实`。
- **分析性观察（本文判断，非原文献结论）**：本批证据中，标称 "VLA" 的工作已明显外溢到**自动驾驶 [3][7] 与无人机 [22]**；这会使"VLA 基础模型水位"的横向比较进一步复杂化——因为操作类 VLA 与驾驶类 VLA 的动作空间、评测场域几乎不可通约。

### 1.7 可靠性与安全（衍生方向）
- **[23]（2026）** Time-aware failure detection for VLA models in robot manipulation（学位论文，机构库编号 10356/218808）—— 把 VLA 从能力研究推进到**时序失效检测**；仅见标题与 "Human Verification" 标注，`> 待核实`。
- **[24]（2026）** Predictive vision-language monitoring for proactive safety in robot ...（Frontiers in Robotics and AI）—— 主动安全监控方向线索，`> 待核实`。
- **[15][17][19][21]（2026，IEEE RA-L）** Robot Independent Intelligence: When Language Vanishes in Vision-language-action Models（DOI 10.1109/lra.2026.3728316）—— 本批仅获取到补充材料图片/视频入口（_supp1–_supp4），引用数为 0；**"语言在 VLA 中消失"的具体论断、作者与实验结论均未获取**，`> 待核实`。

### 1.8 前沿进展一览（按证据强度排序）

| # | 进展 | 时间 | 类型 | 证据强度 | 来源 |
|---|------|------|------|----------|------|
| 1 | Pi0.5 架构被第三方复用于 BEHAVIOR Challenge 并夺冠（50 长程家庭任务；correlated noise for flow matching） | 2025 | 竞赛方案 / preprint | B–C | [12] |
| 2 | VLM 主干 + 扩散轨迹解码器；推理时注意力偏置可调制动作，无需重训练（17 cm 平均位移；late layers 定位） | 2026 | preprint | B | [3] |
| 3 | ART：VLA 的 tool-injection / agentic 化 | 2026 | preprint（摘要截断） | C | [9] |
| 4 | CCFT + LP-AT：动作语义要素分解与分层参数高效适配（仅动作理解） | 2026 | preprint | B | [6] |
| 5 | 高效 VLA 综述（效率线入口） | 2025 | 综述 | C（仅入口） | [2][5] |
| 6 | OpenVLA 微调工程化（LoRA，1.4% 参数匹配全量微调） | 2024 | 官方项目页 | B | [25][28] |
| 7 | VLA 可靠性 / 失效检测 / 主动安全监控 | 2026 | 学位论文 / 期刊 | C–D | [23][24] |
| 8 | "语言在 VLA 中消失"的反思性争议 | 2026 | RA-L（正文缺失） | D（仅附件入口） | [15][17][19][21] |
| 9 | rMuscle / StarVLA / stage-info 微调 / 合成指令增强 | 2026 | 仅标题 | D | [4][10][29][32] |

---

## 二、方法范式对比（离散动作 / 扩散 / Flow Matching / 双系统）

> **重要限定**：本批候选证据**未覆盖** π0 / π0-FAST、OpenVLA-OFT、GR00T N1、Gemini Robotics、RDT-1B 的一手材料，因此下表不能作为"四大范式全景对比"使用。表中"可核查证据"列只写本批 [n] 来源实际支撑的内容；范式归属本身（如"离散动作 token"）部分来自种子资源备注，已逐条标注。

| 范式 | 代表工作 | 可核查证据（本批） | 置信度 |
|------|----------|--------------------|--------|
| **离散动作 token（VLM 直接输出）** | RT-2 | RT-2 摘要确认"把互联网规模 VLM 纳入端到端机器人控制

## 参考来源

[1] [2609.13053] Dynin-Robotics: Omnimodal Unified Diffusion  Vision-Language-Action   Model — https://www.so.com/link?m=bPnD8o%2FiPKIq6B3vcfzGI0qXh6evN50dKOlutSahMALS8hlHUdJoSmt4fvlQAe3pScgTLEz6XnNzPnXB6MXuzlKtKHfwyoOD6bV1TdY091tOAP%2F4nksE5Pje%2BS9qsrujkyhjD4WoQxhThtgA6bRpqOlxpsKsCtSTBBkij9R4cvmTR2LIEh5ElREZiNuGydsebGKKVBvxgnWbMDX2v
[2] [2510.24795] A Survey on Efficient Vision-Language-Action Models — https://arxiv.org/abs/2510.24795
[3] Inference-Time Attention Steering for Vision-Language-Action Driving Models — http://arxiv.org/abs/2608.17095v1
[4] rMuscle: Robotic Muscle Memory for Efficient  Vision-Language-Action   Model  Inference — https://www.so.com/link?m=zIkjUuyYeInWoisjnO%2B4cEwpB42LaCuVwdnU%2BkC6DxGU9mcOvwInaJwD4PucU48DM1a3mJxHoklRGVkOIieIbr3HxY8LSeaB7nR7NT8z%2BzhejvaLVL%2Bhin5GLSxhg0cuLWeXIjbzJ8KPrqgtV3FBzrmDbfe7TeNx0ork0ZmWOJsmpNLcxxZkG90u2XUT1StuC
[5] A Survey on Efficient Vision-Language-Action Models - arXiv — https://arxiv.org/html/2510.24795v3
[6] Compositional Context Fine-Tuning Vision-Language Model for Complex Assembly Action Understanding from Videos — http://arxiv.org/abs/2607.10797v1
[7] AutoVLA: A  Vision-Language-Action   Model  for End-to-End Autonomous Driving with Adaptive Reasoning and Reinforcement Fine-Tuning — https://www.so.com/link?m=bP1VjdosERYOreeD2gldumcWUHhllFTZArE6yYq8Vp8hJE643ORPfq0vFAcTR6YWlpCk4VHJaOxSsqJUuBHhCnK18WlPoibRMxde7EbKzWzJPJvUttk5xW2GfeI3LVwK1AuR9YIG%2FxshoY9sNhn2j6w1fYpFbNZqznujbyx4cjPydjOWkZHA4wE0dU0toC%2BIW
[8] Survey of Vision-Language-Action Models for Embodied Manipulation — https://arxiv.org/abs/2508.15201
[9] Evolve Vision-Language-Action Model into an Agent with On-the-fly Tool-use — http://arxiv.org/abs/2608.14047v3
[10] StarVLA: A Lego-like Codebase for  Vision-Language-Action   Model  Developing — https://www.so.com/link?m=bLmGOpV3WnKV7PC7wHSIqsK2O7b%2FdoQG5mONxJhnifotBnaxsesV1BTRXIGJTWwzCzMUTtYIrq14CuO43u6GldTseWye28hTFkXyb%2BQHviLC8FteQyan1gpPkE7yyp1kMDpG4cD3HUqCZAU%2BdEZAUxtVaeAiTMtfPIPXqsoh%2F5LAK4txa7VRfpNOwexGehXUf
[11] Vision-Language-Action in Robotics: A Survey of Datasets ... - arXiv — https://arxiv.org/html/2604.23001v1
[12] Task adaptation of Vision-Language-Action model: 1st Place Solution for the 2025 BEHAVIOR Challenge — http://arxiv.org/abs/2512.06951v2
[13] Daily Assistive View Control Learning of Low-Cost Low-Rigidity Robot via Large-Scale Vision-Language Model — https://doi.org/10.1109/humanoids57100.2023.10375239
[14] [2307.15818] RT-2: Vision-Language-Action Models Transfer Web ... — https://arxiv.org/abs/2307.15818
[15] Robot Independent Intelligence: When Language Vanishes in Vision-language-action Models_supp3-3728316.jpg — https://doi.org/10.1109/lra.2026.3728316/mm2
[16] RT-2: Vision-Language-Action Models Transfer Web Knowledge to ... — https://proceedings.mlr.press/v229/zitkovich23a.html
[17] Robot Independent Intelligence: When Language Vanishes in Vision-language-action Models_supp1-3728316.mp4 — https://doi.org/10.1109/lra.2026.3728316/mm3
[18] Papers — CoRL 2023 — https://www.corl2023.org/papers
[19] Robot Independent Intelligence: When Language Vanishes in Vision-language-action Models_supp4-3728316.jpg — https://doi.org/10.1109/lra.2026.3728316/mm1
[20] Large VLM-based Vision-Language-Action Models for Robotic ... — https://arxiv.org/html/2508.13073v3
[21] Robot Independent Intelligence: When Language Vanishes in Vision-language-action Models_supp2-3728316.mp4 — https://doi.org/10.1109/lra.2026.3728316/mm4
[22] Vision–Language–Action (VLA) Models for Unmanned Aerial ... - MDPI — https://www.mdpi.com/2504-446X/10/6/412
[23] Time-aware failure detection for vision-language-action models in robot manipulation — https://doi.org/10.32657/10356/218808
[24] Predictive vision-language monitoring for proactive safety in robot ... — https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2026.1870024/full
[25] OpenVLA: An open-source vision-language-action model - GitHub — https://github.com/openvla/openvla
[26] OpenVLA :开源端到端视觉-语言-动作机器人决策模型 — https://www.so.com/link?m=zMlR1IYS51jcAzbczYJqTsm%2FJn3oyJmOePJzXOaTex4jQgx8w98wxCUdH4vmfjXrGtW7345XhAe5MNMKaR5pfcihGYT%2FKCX9MqQdhG863gJHx1JkhHVtXq1CVWc7SbhzM%2BKtn8qgU4OYjZwxoHT%2FIIDfCWd9gbtWZeURO5xn4VkIxLAWnFtS11fxJv0X%2FZhlD8k9zY85%2BXz9EIlnqRq9j1E%2FtrQ22jc0xf7Yw3w%3D%3D
[27] Csclora: An Efficient Fine-Tuning Method for Open-Source Llms in Chinese Spelling Correction — https://doi.org/10.2139/ssrn.4757814
[28] OpenVLA: An Open-Source Vision-Language-Action Model — https://openvla.github.io/
[29] [2603.16044v1] Enhancing Linguistic Generalization of  VLA :  Fine-Tuning   OpenVLA  via Synthetic Instruction Augmentation — https://www.so.com/link?m=uG8uiNeAdrIEjNB3HIQxJaoeg5iFLop0rafPWqElrpwClKZULwSOOwXpsdga0fcWxIGYI8mSvE3kBYImY%2FIKWzWJR00EepvLbva7JsyyIc4DdvxS0qE0Ps7onKGlyNhtIRZbRXnyvTPr2KeE6wqsdTXJr4x3I98BkZ%2FOUCl9RWjp6Ai1jHkf0%2Foohu8I%3D
[30] Enhancing Nepali Text Understanding with Machine Translation and LoRA Fine-Tuning of Open-Source LLM — https://doi.org/10.1007/978-3-031-77915-2_23
[31] Fine-tuning OpenVLA on Amazon SageMaker AI with LoRA - AWS — https://aws.amazon.com/blogs/physical-ai/fine-tuning-openvla-on-amazon-sagemaker-ai-with-lora/
[32] An Empirical Study on Stage-Information Interfaces for  VLA   Fine-Tuning — https://arxiv.org/html/2607.13605v1
[33] Unified Efficient Fine-Tuning Techniques for Open-Source Large Language Models — https://doi.org/10.21203/rs.3.rs-4660140/v1
[34] heslabs/OpenVLA - GitHub — https://github.com/heslabs/OpenVLA
[35] OpenVLA : An  Open-Source  Vision-Language-Action Model — https://www.so.com/link?m=uNHMnpiELTwF02ejeif%2FvlrD1C%2B%2FT%2FSGZnbGSmV1pNMDkx5feh3GCRAKQwqUEWUhV4mWNQqrPKLMbEni7o5ufEvmxWuctcQZHca8Li4ag8xsyYhtV54K%2FtmgzmaloDvN8jgn2oo%2F5vZI0MMTG8lDUf7JvmNKx3yyPDVa7L0ox9PW%2Bq1Nt15tGHhLokyA%3D
[36] Parameter-Efficient Online Fine-Tuning of ML-Based Hybrid Beamforming with LoRA — https://doi.org/10.36227/techrxiv.173738499.93495833/v1


---

*Generated by research-bot · topic=`vla` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading · model=`deepseek-v4-flash` · sources=36 · duration=364s · 2026-10-02T04:08:18+00:00*
