# 具身智能与视觉-语言-动作（VLA）前沿增量报告（2024-10 → 2026-10）

**日期**：2026-10-24（UTC）｜**领域**：Embodied AI / Vision-Language-Action（VLA）/ Robot Learning｜**检索源**：34 条去重来源（arXiv 预印本 28 条、DOI 出版物 4 条、其他 2 条），其中与 VLA 强相关约 10 条

> **证据基线与检索噪声说明**：本轮召回的 34 条来源中，相当一部分（如短视频参与度预测 [4]、临床问答 [6]、多智能体竞赛 [7]、激流检测 [32]、开源软件工程 [25][26][30][31]）与 VLA 主题弱相关或无关，属于检索召回噪声。本报告只对可核查的 VLA 相关条目下结论；缺失的量化信号（引用数、GitHub star、下载量、榜单排名）一律标注 `> 待核实`，**不编造数字**。所有条目均为 arXiv 预印本或 DOI 预印本，**未见同行评审定稿证据**，按 evidence-grading 标准整体处于 B 级及以下。

---

## 1. 进展与热点（Progress & Hotspots）

**一句话增量判断**：相对 2024 年 OpenVLA [27] 所代表的“开源 VLA 基座”基线，2025–2026 的增量不在新架构范式，而集中在**任务适配登顶长时程基准、推理时干预、失败模式诊断、低资源部署**四条工程化支线上；且这些增量目前几乎全部是**仿真基准或预印本自评**，缺少独立真机复现。

### 1.1 最新进展（2025–2026）

1. **任务适配拿下长时程基准冠军**：[2] 报告了一个基于 Pi0.5 架构的视觉-动作策略，在 2025 BEHAVIOR Challenge 中获得第一名。该基准包含 50 个长时程家务任务、照片级仿真，要求双臂操作、导航与上下文决策。**证据性质**：官方技术报告（B 级），成绩为**仿真基准自评**，非真机独立验证。热度 `> 待核实`；权威：arXiv cs.RO 预印本 [2]；关注度：中（竞赛第一名是明确信号，但无第三方复现佐证）；推荐度 ★★★★☆（当前最完整的 VLA 长时程任务适配公开方案之一）。

2. **推理时注意力引导，免重训**：[1] 针对 VLA 驾驶模型，在视觉侧引入有界的 pre-softmax 加性注意力偏置，使推理阶段可将注意力重定向至安全关键目标，无需重训。**证据性质**：预印本（B 级），摘要未给出跨数据集复现。热度 `> 待核实`；权威：arXiv cs.CV [1]；关注度：低–中（新方向，尚无引用信号）；推荐度 ★★★☆☆（“推理时控制”思路对安全关键场景有迁移价值）。

3. **语言遵循的反事实失败被系统化诊断**：[15] 指出 VLA 在缺少强场景监督时会“视觉压过语言”，产生 counterfactual failures，并提出评测与缓解方法。这是**能力边界**层面最重要的增量：它把“VLA 是否真的听懂指令”从轶事变成可测量问题。热度 `> 待核实`；权威：arXiv cs.CV [15]；关注度：中（直指 VLA 共识性痛点）；推荐度 ★★★★☆（做 VLA 评测必读的负面结果类工作）。

4. **VLA 向 Agent 化演进**：[5] 探索将 VLA 演化为具备 on-the-fly tool-use 能力的智能体。**证据性质**：预印本 v3（B 级）。热度 `> 待核实`；权威：arXiv [5]；关注度：低–中；推荐度 ★★★☆☆（代表“VLA + 工具调用”这一新分支）。

5. **低资源推理加速**：[8] 提出 BLURR（Boosted Low-Resource Inference），面向 VLA 推理成本问题。热度 `> 待核实`；权威：arXiv [8]；关注度：低；推荐度 ★★★☆☆（部署侧相关，但需核实加速比与精度损失口径）。

6. **工业细粒度动作理解**：[3] 用 Compositional Context Fine-Tuning 将 VLM 适配到装配动作理解，处理细微动作与手-物交互。热度 `> 待核实`；权威：arXiv cs.CV [3]；关注度：低；推荐度 ★★★☆☆（人机协作装配场景的可迁移方法）。

### 1.2 经典与奠基性工作

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Open X-Embodiment / RT-X | 2023 | 未在摘要给出（`> 待核实`） | `> 待核实` | arXiv v9 预印本，跨机构数据集 [22] | 高（跨本体数据事实标准，依据：被后续工作广泛用作训练底座）| ★★★★★ | http://arxiv.org/abs/2310.08864v9 | 跨本体机器人学习数据集与 RT-X 模型，VLA 数据范式奠基 |
| OpenVLA | 2024 | 未在摘要给出（`> 待核实`） | `> 待核实` | arXiv cs.RO v3 预印本 [27] | 高（开源 VLA 权重代表，依据：开源可复现定位）| ★★★★★ | http://arxiv.org/abs/2406.09246v3 | 开源 VLA 模型，确立“开放权重 + 可微调”基线 |
| DROID | 2024 | 未在摘要给出（`> 待核实`） | `> 待核实` | arXiv v2 预印本 [21] | 高（大规模真实场景操作数据集）| ★★★★★ | http://arxiv.org/abs/2403.12945v2 | 大规模 in-the-wild 机器人操作数据集，真机多样性关键来源 |
| VLP: A Survey on Vision-Language Pre-training | 2022 | 未在摘要给出（`> 待核实`） | `> 待核实` | arXiv v4 综述 [14] | 中（早期综述，时效偏旧）| ★★★☆☆ | http://arxiv.org/abs/2202.09061v4 | 视觉-语言预训练谱系，理解 VLA 表征来源的背景读物 |
| Vision Mamba: A Comprehensive Survey and Taxonomy | 2024 | 未在摘要给出（`> 待核实`） | `> 待核实` | arXiv v1 综述 [13] | 中 | ★★☆☆☆ | http://arxiv.org/abs/2405.04404v1 | 状态空间架构综述，供 VLA 骨干选型参考，非 VLA 本体 |

> 说明：本窗口内**未见**可直接归入“VLA 奠基”的新经典；上表经典工作均早于 2024-10 窗口起点，用于建立基线。

---

## 2. 工业界与产品（Industry & Product）

**一句话增量判断**：本窗口内可核查的“产品化”信号仅有一条明确的行业垂直应用（电力操作机器人）与一条开源工程栈（LeRobot），**没有**可核实的量产、出货量或真机部署规模数据。

1. **行业垂直落地：电力操作机器人 VLA**：[9] 提出面向电力作业机器人的 VLA 模型。**证据性质**：DOI 预印本（Authorea 平台），非同行评审，证据等级偏 B/C；摘要层面无法确认是否真机部署、任务数与成功率。热度 `> 待核实`；权威：DOI 出版物 [9]（非顶会/期刊）；关注度：低（无引用/榜单信号）；推荐度 ★★☆☆☆（唯一可核实的电力行业 VLA 应用线索，但需核实实验口径）。**真机部署结论：`> 待核实`**。

2. **开源工程栈：LeRobot**：[24] 将 LeRobot 定位为端到端机器人学习开源库，覆盖低成本遥操作、数据采集与策略训练。**证据性质**：arXiv cs.RO 预印本（B 级）；论文本身为 2026 年发表，但库的开源历史早于论文，**论文未在摘要中给出 star/下载量**，热度 `> 待核实`；权威：arXiv cs.RO [24]；关注度：高（依据：端到端机器人学习开源库的生态位，但缺量化信号佐证）；推荐度 ★★★★★（工程落地首选参考栈）。**ROS2 集成成熟度：`> 待核实`**——证据池内唯一 ROS 相关来源 [34] 是 2018 年 NimbRo-OP 的 ROS1 时代框架，不能作为当前 ROS2 + VLA 集成的证据。

3. **开源权重路线延续**：OpenVLA [27] 所代表的“开放权重 + 社区微调”路线仍是生态主轴，但本窗口内**未见**其后续版本的官方发布证据，`> 待核实`。

> 结论：产业侧证据薄弱。**商业化、量产、客户数、成本曲线均无一手来源支撑，统一标注 `> 待核实`**，不应在汇报中作为已知事实陈述。

---

## 3. 蓝海与缺口（Blue Ocean & Gaps）

**一句话增量判断**：当前最明显的空白不是“更强的 VLA”，而是**“VLA 到底有没有听懂”的可测量性、跨本体真机独立评测、以及推理时延/边缘部署的工程闭环**。

1. **语言遵循的可测量性缺口**：[15] 证明 VLA 存在系统性的反事实失败（视觉压过语言）。这意味着现有基准 [2][21][22] 的高分**可能高估了指令遵循能力**。谁先建立“语言-视觉冲突”标准测试集，谁就占据评测话语权。证据：[15]（B 级，预印本自评）；热度 `> 待核实`。

2. **仿真 SOTA 与真机 SOTA 的鸿沟**：[2] 的冠军成绩建立在 50 任务照片级仿真上；[21] 提供真实场景数据但不等同于统一真机榜单。**跨本体结论目前无法由单一 benchmark 支撑**：OXE [22] 提供数据多样性，DROID [21] 提供真实场景，BEHAVIOR [2] 提供长时程任务，但三者**评测协议不互通**。第三方独立复现：`> 待核实`。

3. **推理时延与低资源部署**：[8] 明确指出 VLA 推理成本问题并提出低资源推理方案，说明“把 VLA 塞进边缘算力”仍是未解工程缺口。量化加速比：`> 待核实`。

4. **长时程 + 工具使用的智能体化**：[5] 是少数把 VLA 推向 tool-use agent 的工作，属于竞争尚不拥挤的方向。证据：[5]（B 级）；热度 `> 待核实`。

5. **工业细粒度操作**：[3] 的装配动作理解、[9] 的电力作业，说明“通用 VLA → 垂直行业适配”仍是蓝海；但两者均缺真机规模验证。`> 待核实`。

6. **ROS2 原生 VLA 推理/部署包缺口**：证据池仅有 ROS1 时代的 [34]，**未检索到 ROS2 + VLA 的官方集成方案**，这是明确的工程空白（`> 待核实`，可能受检索覆盖限制）。

---

## 4. 瓶颈与拐点（Bottleneck & Inflection）

**一句话增量判断**：瓶颈正从“模型容量/数据规模”迁移到“**评测可比性 + 推理成本 + 指令遵循可信度**”；拐点信号是 2026 年出现的一批**免重训的推理时干预**工作 [1][8]，暗示范式从“堆数据重训”转向“推理时控制 + 高效部署”。

| 瓶颈 | 证据 | 现状 | 是否临近拐点 |
|---|---|---|---|
| 评测不可比（仿真 vs 真机、benchmark 协议不通） | [2][21][22] | 长时程仿真榜 [2] 与真实数据 [21] 无统一协议；跨本体结论缺第三方复现 `> 待核实` | 否，尚缺统一真机榜单 |
| 数据稀缺与多样性 | [21][22] | 已有大规模数据集，但真机任务分布仍窄；长尾任务覆盖 `> 待核实` | 部分（数据侧改善快于评测侧） |
| 推理时延 / 算力成本 | [8] | 已出现低资源推理方案，量化收益 `> 待核实` | **是**（工程解法开始出现） |
| 语言-视觉冲突导致指令不可信 | [15] | 已可诊断、可部分缓解，但无标准测试集 | 部分 |
| 真机安全与监管认证 | 证据池无 | 无一手来源 | `> 待核实` |

**拐点判断**：推理时干预（[1] 的注意力偏置、[8] 的低资源推理）代表一类**不改变训练管线、只在部署侧加控制**的新范式。若该范式在 12 个月内被主流开源栈 [24][27] 吸收，可视为明确拐点——这是可证伪的观察点（见第 7 节）。

---

## 5. 社会·政策·国际（Society, Policy & Geopolitics）

**一句话增量判断**：本窗口内唯一可核查的治理侧增量是**基础模型透明度年度评估**，机器人专属的安全监管、认证标准与地缘供应链证据在本轮检索中**完全缺失**，必须标注待核实。

1. **基础模型透明度**：[33] 发布 2025 年度 Foundation Model Transparency Index（第三版），量化基础模型开发者的透明度实践。**证据性质**：arXiv cs.AI 预印本（B 级）；热度 `> 待核实`；权威：arXiv [33]；关注度：中（年度性治理评估）；推荐度 ★★★☆☆（用于论证“VLA 基础模型透明度”时可作类比依据，但该指数**是否覆盖机器人/VLA 厂商 `> 待核实`**）。

2. **机器人安全监管、功能安全认证（如 ISO 10218 类）、责任归属**：本轮 34 条来源中**无任何一手政策/标准文本**，全部标注 `> 待核实`。不得据模型记忆补充。

3. **国际格局与供应链（算力出口管制、本体硬件供应）**：无来源支撑，`> 待核实`。

4. **伦理与劳动影响（装配/电力作业自动化）**：[3][9] 指向工业场景替代性，但两文均未讨论社会影响，`> 待核实`。

> 结论：第 5 维在本周期**证据严重不足**，除 [33] 外无显著可核实变化。这是一个明确的**检索缺口**，建议下一轮定向补检政策/标准数据库。

---

## 6. 资本与生态（Capital & Ecosystem）

**一句话增量判断**：可核查的生态变化集中在**开源侧**（数据 [21][22] + 权重 [27] + 工程库 [24] 三层栈成型），资本侧（融资、并购、人才流动）在本轮证据池中**零覆盖**。

1. **开源三层栈雏形**：数据层 OXE [22] / DROID [21] → 权重层 OpenVLA [27] → 工程层 LeRobot [24]。这条链路使“复现一个 VLA”的门槛显著下降，是生态层面最实质的增量。热度 `> 待核实`（无 star/下载数据）；权威：均为 arXiv 预印本；关注度：高（依据：三层栈完整覆盖训练-数据-部署，但缺量化佐证）；推荐度 ★★★★★。

2. **社区化评测与竞赛生态**：BEHAVIOR Challenge [2] 表明“竞赛 + 仿真基准”正成为 VLA 的任务适配验证场。第三方独立榜单（如 RoboArena）在本轮证据池中**未检索到**，`> 待核实`。

3. **投融资、并购、人才流动、公司格局**：无一手来源，全部 `> 待核实`。**特别提示**：网络上关于 VLA 创业公司融资的传闻多属 [R] 级，未经官方公告核实不应写入汇报。

---

## 7. 信号与预测（Signals & Forecast）

**一句话增量判断**：早期信号指向“**推理时控制 + 高效部署 + 可信评测**”三条线；未来 6–18 个月最值得观察的是评测协议能否统一，而非模型参数量。

### 7.1 早期信号（已确证事实）

- 信号 A：2026 年出现免重训的推理时注意力干预 [1]，以及低资源推理方案 [8]——说明训练侧收益边际递减，部署侧优化开始被重视。
- 信号 B：[15] 把“VLA 不听指令”从轶事转为可测量问题，评测重心从“成功率”转向“忠实度”。
- 信号 C：竞赛冠军方案基于既有架构做任务适配 [2]，而非提出新架构——**架构收敛、适配为王**的信号。

### 7.2 可证伪预测

**[P1]** 若到 **2027 年中**，出现 ≥3 个在**真机多本体**上独立复现 BEHAVIOR 类长时程任务的结果（非同一团队自评），则“任务适配范式可跨本体迁移”成立。
- 依据链：当前 [2] 仅仿真自评 → [21][22] 提供真机数据但无统一协议 → 迁移性未被验证。
- 置信度：**推测**（30–40%）。若届时仍只有仿真榜，则判断不成立（证伪条件）。

**[P2]** 若 **12 个月内**（至 2027-10），推理时干预方法（[1] 类注意力引导、[8] 类低资源推理）被主流开源栈 [24][27] 以官方模块形式集成，则“推理时控制成为标配”成立。
- 依据链：开源栈迭代周期通常 < 12 个月；当前已有可插拔的方法原型。
- 置信度：**较大概率**（50–60%）。证伪条件：主流栈仍只提供端到端训练接口。

**[P3]** 若到 **2027 年底**仍无“语言-视觉冲突”标准测试集被 ≥2 个独立团队采用，则 [15] 指出的可信度缺口将持续被高估的成功率掩盖。
- 依据链：评测标准通常滞后方法 1–2 年；当前仅有单篇论文提出。
- 置信度：**推测**（40%）。证伪条件：出现被广泛引用的冲突测试集。

**[P4]** ROS2 原生 VLA 推理/部署包仍是空白（`> 待核实`，受检索覆盖限制）。若 2027 年前出现官方维护的 ROS2 + VLA 推理节点并进入 [24] 生态，则工程栈缺口收敛。
- 置信度：**未知**，需补充检索 ROS2 生态仓库后判断。

### 7.3 Watchlist（值得持续关注）

| 对象 | 类型 | 关注理由 | 引用 |
|---|---|---|---|
| BEHAVIOR Challenge 后续真机化 | 基准 | 长时程任务是否走出仿真 | [2] |
| 推理时注意力/控制方法 | 方法 | 免重训范式能否成为标配 | [1][8] |
| 语言-视觉冲突评测 | 评测 | VLA 可信度的关键缺口 | [15] |
| LeRobot 生态演进 | 工程栈 | 是否吸收推理时模块与 ROS2 集成 | [24] |
| VLA + tool-use agent | 方法 | 长时程任务的新解法分支 | [5] |
| 基础模型透明度指数 | 治理 | 是否扩展到机器人厂商 | [33] |

---

## 参考来源

[1] Inference-Time Attention Steering for Vision-Language-Action Driving Models — http://arxiv.org/abs/2608.17095v1
[2] Task adaptation of Vision-Language-Action model: 1st Place Solution for the 2025 BEHAVIOR Challenge — http://arxiv.org/abs/2512.06951v2
[3] Compositional Context Fine-Tuning Vision-Language Model for Complex Assembly Action Understanding from Videos — http://arxiv.org/abs/2607.10797v1
[4] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1
[5] Evolve Vision-Language-Action Model into an Agent with On-the-fly Tool-use — http://arxiv.org/abs/2608.14047v3
[6] UIC-AIHealth4All at ArchEHR-QA 2026: Answer-First Evidence Grounding for Clinical Question Answering — http://arxiv.org/abs/2608.27467v1
[7] Second MOASEI Competition at AAMAS'2026: A Technical Report — http://arxiv.org/abs/2607.03399v1
[8] BLURR: A Boosted Low-Resource Inference for Vision-Language-Action Models — http://arxiv.org/abs/2512.11769v1
[9] Vision-Language-Action Model for Electrical Power Operation Robots — https://doi.org/10.22541/authorea.15004596/v1
[10] Review of: "Large Vision-Language Model Alignment and Misalignment: A Survey Through the Lens of Explainability" — https://doi.org/10.32388/p3ddoa
[11] Remote sensing image captioning: a survey from encoder-decoder model to large vision-language model — https://doi.org/10.1117/12.3107088
[12] Review of: "Large Vision-Language Model Alignment and Misalignment: A Survey Through the Lens of Explainability" — https://doi.org/10.32388/4m5jo4
[13] Vision Mamba: A Comprehensive Survey and Taxonomy — http://arxiv.org/abs/2405.04404v1
[14] VLP: A Survey on Vision-Language Pre-training — http://arxiv.org/abs/2202.09061v4
[15] When Vision Overrides Language: Evaluating and Mitigating Counterfactual Failures in VLAs — http://arxiv.org/abs/2602.17659v2
[16] Exploring the Frontier of Vision-Language Models: A Survey of Current Methodologies and Future Directions — http://arxiv.org/abs/2404.07214v4
[17] Understanding Survey Paper Taxonomy about Large Language Models via Graph Representation Learning — http://arxiv.org/abs/2402.10409v1
[18] Overview of the First Workshop on Language Models for Low-Resource Languages (LoResLM 2025) — http://arxiv.org/abs/2412.16365v1
[19] Technical Report for Ego4D Long-Term Action Anticipation Challenge 2025 — http://arxiv.org/abs/2506.02550v2
[20] Object Detection with Multimodal Large Vision-Language Models: An In-depth Review — http://arxiv.org/abs/2508.19294v2
[21] DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset — http://arxiv.org/abs/2403.12945v2
[22] Open X-Embodiment: Robotic Learning Datasets and RT-X Models — http://arxiv.org/abs/2310.08864v9
[23] One-Shot Reinforcement Learning for Robot Navigation with Interactive Replay — http://arxiv.org/abs/1711.10137v2
[24] LeRobot: An Open-Source Library for End-to-End Robot Learning — http://arxiv.org/abs/2602.22818v1
[25] Open Source Software Development Challenges: A Systematic Literature Review on GitHub — http://arxiv.org/abs/2003.10750v3
[26] OSS PESTO: An Open Source Software Project Evaluation and Selection TOol — http://arxiv.org/abs/2102.12267v1
[27] OpenVLA: An Open-Source Vision-Language-Action Model — http://arxiv.org/abs/2406.09246v3
[28] CoReCon: an open, community-powered collection of Reionization constraints — http://arxiv.org/abs/2309.06480v1
[29] OpenPodcar: an Open Source Vehicle for Self-Driving Car Research — http://arxiv.org/abs/2205.04454v2
[30] GitHub open source project recommendation system — http://arxiv.org/abs/1602.02594v1
[31] BotHawk: An Approach for Bots Detection in Open Source Software Projects — http://arxiv.org/abs/2307.13386v1
[32] NTIRE 2026 Rip Current Detection and Segmentation (RipDetSeg) Challenge Report — http://arxiv.org/abs/2604.17070v2
[33] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1
[34] A ROS-based Software Framework for the NimbRo-OP Humanoid Open Platform — http://arxiv.org/abs/1809.11051v1

---

*Generated by research-bot · topic=`具身智能与视觉-语言-动作vla前沿` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`deepseek-v4-flash` · sources=34 · duration=175s · 2026-10-24T15:15:24+00:00*
