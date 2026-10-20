# 具身智能与视觉-语言-动作（VLA）前沿：增量快照与证据审计

**日期**：2026-10-20（UTC）｜**领域**：Embodied AI / Vision-Language-Action（VLA）｜**检索源**：33 条编号候选来源，其中 21 条与 VLA/具身智能相关（含 1 条 VLM 边缘相关），12 条判定为无关噪声｜**时间窗**：2023-07 至 2026-08（以 arXiv 编号推断的投稿月为准）

> **证据基线与三点局限（请先读）**
> 1. **热度证据整体缺失**：本轮所有结构化发现的 `heat`/`citations`/`stars` 字段为空，因此下文所有「热度」列一律写 `> 待核实`，不填任何数字。
> 2. **问题—证据错配**：子问题 q1（新模型与榜单）、q2（经典脉络与数据集口径）的抽取结果大量落在「VLA 驾驶注意力引导」「装配动作理解」等边缘主题上（[1][2][14]），而 π0/π0.5、Gemini Robotics、RDT-1B、Octo、RT-1、Diffusion Policy、ACT/ALOHA、LIBERO、CALVIN、SimplerEnv、RoboArena、DROID **在本轮可引用来源中无一手证据**，下文一律标 `> 待核实`，不做转述式断言。
> 3. **证据等级口径**：arXiv 预印本 = B 级；带 IEEE DOI 的 proceedings 论文 = A−/B+（会议属性待核实）；无关来源 = E 级，直接剔除。

---

## 1. 进展与热点（Progress & Hotspots）

**一句话增量判断**：相对 2023–2024 年「把 VLM 接上动作头、把模型做大」的基线，2025–2026 年的真实增量不在参数规模，而在**三处结构性位移**——(a) VLA 之上加「分层 / 工具调用 / 世界模型」的认知外骨骼，(b) 把**推理时延与吞吐**独立成一个研究对象，(c) 失效检测与推理时干预成为可单独成文的子问题。

### 1.1 最新进展（近 1–2 年，2025-01 至 2026-08）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| ART（Agentic Robot with Tool-use） | 2026 | 标题/摘要未标明 `> 待核实` | `> 待核实` | arXiv preprint, cs.RO（B 级）[3] | 中：把 agent 工具调用正式嫁接到端到端 VLA，属范式级组合 [3] | ★★★★☆ 想做「VLA+工具」必读，但需核实是否有真机实验 [3] | http://arxiv.org/abs/2608.14047v3 | 工具注入框架，可调低层视觉/高层 affordance/本体增强模块 [3] |
| Grounding Hierarchical VLA（显式语言-动作对齐） | 2026 | 未标明 `> 待核实` | `> 待核实` | IEEE DOI, cvprf71909.2026（会议属性 `> 待核实`）[6] | 中：直指分层 VLA 的「语言指令与动作段如何对齐」痛点 [6] | ★★★★☆ 分层路线的关键补丁 [6] | https://doi.org/10.1109/cvprf71909.2026.00889 | 用显式 language-action alignment 给分层结构做 grounding [6] |
| IRL-VLA（Reward World Model 训练） | 2026 | 未标明 `> 待核实` | `> 待核实` | IEEE DOI, cvprf71909.2026 [12] | 中：把「奖励世界模型」引入 VLA 训练，绕开纯模仿 [12] | ★★★★☆ 想看 VLA 脱离 behavior cloning 的读者优先 [12] | https://doi.org/10.1109/cvprf71909.2026.00098 | 用奖励世界模型做 VLA 训练信号 [12] |
| A₁（Adaptive Truncated VLA：affordance→action） | 2026 | 未标明 `> 待核实` | `> 待核实` | IEEE DOI, cvprf71909.2026 [5] | 中低：截断式两段结构，属效率/结构混合优化 [5] | ★★★☆☆ 选题巧，但增量偏工程 [5] | https://doi.org/10.1109/cvprf71909.2026.00149 | 自适应截断，从 affordance 到 action 分段生成 [5] |
| Running VLAs at Real-time Speed | 2025 | 未标明 `> 待核实` | `> 待核实` | arXiv preprint, cs.RO [24] | 高：摘要声称在**单张消费级 GPU** 上跑 π0 级多视角 VLA，30Hz 帧率、最高 480Hz 轨迹频率 [24] | ★★★★★ 本轮最值得精读的工程突破（若数字可复现）[24] | http://arxiv.org/abs/2510.26742v1 | 一组策略实现实时化，摘要明确针对「此前被认为大 VLA 做不到」的动态任务 [24] |
| VLAgents（Policy Server） | 2026 | 未标明 `> 待核实` | `> 待核实` | arXiv preprint [27] | 中：把 VLA 推理做成「策略服务器」，是部署形态的抽象 [27] | ★★★★☆ 工程落地视角必读 [27] | http://arxiv.org/abs/2601.11250v1 | 面向高效 VLA 推理的服务化架构 [27] |
| BLURR（低资源推理包装） | 2025 | 未标明 `> 待核实` | `> 待核实` | arXiv preprint, cs.RO [16] | 中低：明确指向「网页 demo / 商品 GPU 高频控制」两类受限场景 [16] | ★★★☆☆ 即插即用的推理降本方案 [16] | http://arxiv.org/abs/2512.11769v1 | 轻量推理 wrapper，可插入现有 VLA 控制器 [16] |
| VLA-Adapter（微小规模 VLA） | 2025 | 未标明 `> 待核实` | `> 待核实` | arXiv preprint [26] | 中：对抗「VLA 必须大」的默认假设 [26] | ★★★★☆ 小模型路线的代表候选 [26] | http://arxiv.org/abs/2509.09372v2 | tiny-scale VLA 的有效范式 [26] |
| 2025 BEHAVIOR Challenge 冠军方案 | 2025 | 未标明 `> 待核实` | `> 待核实` | arXiv preprint, cs.RO [9] | 高：唯一带「榜单名次」的硬证据 [9] | ★★★★★ 判断 SOTA 变动的锚点 [9] | http://arxiv.org/abs/2512.06951v2 | 基于 **π0.5 架构**，50 个长程家务任务、需双臂操作+导航+上下文决策，照片级**仿真** [9] |
| 微调 VLA：速度与成功率联合优化 | 2025 | 未标明 `> 待核实` | `> 待核实` | arXiv preprint [8] | 中：把「微调成本」当成一等公民 [8] | ★★★★☆ 落地团队直接可用 [8] | http://arxiv.org/abs/2502.19645v2 | 优化微调的速度与成功率权衡 [8] |
| From Foundation to Application | 2026 | 未标明 `> 待核实` | `> 待核实` | arXiv preprint [30] | 中：标题即指向「基础模型→实践」的落差 [30] | ★★★★☆ 与本章「落地缺口」互为印证 [30] | http://arxiv.org/abs/2607.06403v1 | 讨论如何在实践中改进 VLA [30] |
| Motion Image Diffusion 联合学习 | 2025 | 未标明 `> 待核实` | `> 待核实` | arXiv preprint, cs.RO [25] | 中：指出纯模仿缺乏预测性运动推理 [25] | ★★★★☆ 「VLA+生成式运动先验」方向样本 [25] | http://arxiv.org/abs/2512.18007v1 | 与运动图像扩散联合训练以补足 motion reasoning [25] |
| VLA 驾驶：推理时注意力引导 | 2026 | 未标明 `> 待核实` | `> 待核实` | arXiv preprint, cs.CV [1] | 低中：驾驶域专门问题，与操作域 VLA 仅有方法论交集 [1] | ★★★☆☆ 关注「推理时可干预性」可读 [1] | http://arxiv.org/abs/2608.17095v1 | 在 pre-softmax 上加有界加性注意力偏置，**无需重训练**即可把注意力导向安全关键目标 [1] |
| VLA 导航：注意力头即路径偏差检测器 | 2026 | 未标明 `> 待核实` | `> 待核实` | arXiv preprint, cs.RO [14] | 低中：主张 VLA 内部已含可复用的失效检测信号 [14] | ★★★★☆ 「免费可解释性」思路很有杠杆 [14] | http://arxiv.org/abs/2603.13782v1 | 指出视觉推理幻觉是导航瓶颈，而特定注意力头可用于路径偏差检测 [14] |
| 土耳其语指令理解评测（OpenVLA） | 2026 | 未标明 `> 待核实` | `> 待核实` | IEEE DOI, SIU 2026 [11] | 低：非英语评测稀缺，因而有独特价值 [11] | ★★★☆☆ 多语言泛化的少数实证 [11] | https://doi.org/10.1109/siu71813.2026.11636432 | 对 OpenVLA 做土耳其语命令理解的性能分析 [11] |

> **三点必须外显的不确定性**
> - [24] 的「30Hz / 480Hz / 单消费级 GPU」为**作者摘要自述**，本轮未检索到第三方复现，按 C 级处理。
> - [9] 的冠军成绩建立在**照片级仿真**的 50 任务长程家务基准上，**不等于真机 SOTA**；摘要中未出现真机部署描述 [9]。
> - 「工具调用」「分层」「世界模型」三条线（[3][6][12]）目前均只有单篇自证，**尚无独立对比实验**。

### 1.2 经典与奠基性工作（明确区分：以下为 2023–2025 的脉络锚点，非最新进展）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| RT-2 | 2023 | 标题未标明 `> 待核实` | `> 待核实` | arXiv preprint [15] | 高：确立「VLA = 把 web 知识迁移到机器人控制」的范式命名 [15] | ★★★★★ 领域起点定义文献 [15] | http://arxiv.org/abs/2307.15818v1 | VLA 概念与 co-fine-tuning 范式的奠基 [15] |
| Open X-Embodiment / RT-X | 2023 | 标题未标明（多方合作，具体名单 `> 待核实`） | `> 待核实` | arXiv preprint v9 [18] | 高：跨本体数据聚合 + RT-X 模型，是「统一动作空间」叙事的源头 [18] | ★★★★★ 数据集与跨本体叙事的必引原点 [18] | http://arxiv.org/abs/2310.08864v9 | 机器人学习数据集与 RT-X 模型；多本体混合训练 [18] |
| OpenVLA | 2024 | 标题未标明 `> 待核实` | `> 待核实` | arXiv preprint v3 [10] | 高：开源 VLA 的代名词，「开放权重」成为后续对比基线 [10] | ★★★★★ 复现与二次开发的默认起点 [10] | http://arxiv.org/abs/2406.09246v3 | 开源 VLA 模型；后续被用作多语言评测对象 [11] |
| GR00T N1 | 2025 | 标题未标明（人形机器人方向，机构归属 `> 待核实`） | `> 待核实` | arXiv preprint v2 [7] | 高：明确面向**通用人形机器人**的开放基础模型 [7] | ★★★★★ 人形本体路线的关键开源锚点 [7] | http://arxiv.org/abs/2503.14734v2 | 开放基础模型，面向 generalist humanoid robots [7] |

> **本轮未取得一手证据的经典工作（严格标注，不转述记忆）**
> RT-1、Diffusion Policy、ACT / ALOHA、π0 与 π0.5 原始论文、Gemini Robotics、RDT-1B、Octo —— 这些在 q1/q2 中被点名，但**未出现在可引用来源列表**中，因此本报告不对其贡献、指标或时间做任何断言：`> 待核实（需补充 arXiv 一手引用）`。其中 π0.5 仅通过二手方式出现——[9] 自述「Building on the Pi0.5 architecture」，可作为 π0.5 存在且被沿用的间接旁证，但**不是 π0.5 的一手来源** [9]。

---

## 2. 工业界与产品（Industry & Product）

**一句话增量判断**：本周期可见的增量集中在**「开源栈被论文化、部署栈被组件化」**——即从「一个 GitHub 仓库」变成「一篇可引用的系统论文 + 若干可插拔服务组件」；而**产品化/量产/客户部署的证据在本轮来源中为零**。

- **开源栈论文化（最强增量信号）**：`LeRobot` 以系统论文形式出现（2026-02），摘要明确把「可负担的遥操作硬件普及」列为机器人学习加速的动因 [23]。这意味着开源机器人学习库从工程实践进入可被引用的学术基础设施层。热度 `> 待核实`（未取到 star 数）；权威：arXiv preprint（B 级）[23]；关注度：中（作为库被系统化总结通常反映社区规模，但本轮无量化信号）[23]；推荐度 ★★★★★（工程落地首选入口）[23]。
- **开放权重基础模型两条并行路线**：通用操作侧 `OpenVLA` [10] 与人形侧 `GR00T N1` [7]。二者均以 "Open" 命名并在标题中明示开放属性 [7][10]；但**许可证、权重发布范围、商用限制本轮均未核实** `> 待核实`。
- **部署栈开始分层为独立组件**：推理服务层 `VLAgents`（policy server）[27]、低资源推理层 `BLURR` [16]、实时化策略层 [24]、小模型层 `VLA-Adapter` [26]。这是**从「模型」到「模型+服务」的产业形态前兆**。
- **适配层服务化**：微调效率 [8] 与「从基础模型到应用」的实践改进 [30]，对应交付侧的定制成本问题。
- **产品化证据缺口（重要）**：本轮来源中**没有任何出货量、客户数、单价、量产时间表、真机连续运行时长**类一手数据。因此「哪些 VLA 已从 lab 走向产线」在本报告内**无法回答** `> 待核实`。任何「已量产」表述都不应基于本报告。

---

## 3. 蓝海与缺口（Blue Ocean & Gaps）

**一句话增量判断**：本领域最明显的「无人区」不是模型架构，而是**验证与失效侧**——真机独立验证、负面结果、安全认证、非英语/非西方场景评测，四者在本轮 21 条相关来源中合计仅命中 1 篇 [11]。

1. **真机 vs 仿真的独立验证缺口**：唯一带榜单名次的成果 [9] 明确是**照片级仿真 + 50 任务长程家务**；[24] 的实时性主张为作者自述。**没有一篇第三方复现报告**。→ 机会：做「同一 checkpoint 在仿真榜单与真机上的差距量化」。
2. **负面结果与失效分类学缺失**：本轮零篇 negative results。仅 [14] 从「视觉推理幻觉」角度切入失效机理 [14]，[1] 从推理时可干预角度切入 [1]。→ 机会：VLA 失效模式分类学（failure taxonomy）+ 可复现的失败数据集。
3. **安全与认证级证据空白**：[1] 的注意力偏置与 [14] 的注意力头检测都属于**事后可解释/可干预**，距离功能安全（functional safety）认证证据链极远 [1][14]。→ 机会：把「注意力信号」工程化为运行时安全监控器（runtime monitor）。
4. **多语言与本地化评测几乎无人区**：仅 [11] 一篇土耳其语 OpenVLA 分析 [11]。中文、阿拉伯语、低资源语言、方言指令的 VLA 鲁棒性**本轮无任何证据** `> 待核实`。
5. **VLA × 工具调用刚起步**：[3] 是唯一一篇把 agentic tool-use 注入 VLA 的工作 [3]，尚无与「分层 VLA」[6] 或「世界模型训练」[12] 的交叉对比。→ 机会：tool-use vs hierarchy vs world-model 的三方对照实验。
6. **驾驶域与操作域的桥接空白**：[1][14] 属驾驶/导航域，与操作域 VLA（[9][10][18]）共享方法论但**无跨域迁移研究**。→ 机会：把驾驶域的推理时干预方法迁移到操作域。
7. **「成本」作为一等指标的缺失**：已有实时化 [24]、低资源 [16]、小模型 [26] 三条降本线索，但**没有一篇建立统一的「成功率 / 时延 / 显存 / 单任务成本」四维报告规范**。→ 机会：成本感知的评测协议。

---

## 4. 瓶颈与拐点（Bottleneck & Inflection）

**一句话增量判断**：瓶颈正从**「模型不够大」迁移到「推理不够快 + 评测不够可信」**；拐点信号是「推理层」在 2025-10 至 2026-01 这四个月内独立成文四篇（[16][24][26][27]），这在一年前不存在。

**瓶颈 A：推理时延与算力成本（已有明确缓解路径）**
[24] 直接以「此前被认为大 VLA 做不到的动态实时任务」为问题陈述 [24]；[16] 以「网页 demo / 商品 GPU 高频控制」为受限场景 [16]；[27] 把推理做成服务 [27]；[26] 走小模型 [26]。四条独立路线指向同一瓶颈，构成**瓶颈存在的交叉印证**。但四条均为自评，无横向对比 `> 待核实`。

**瓶颈 B：评测可信度（本轮出现元层面证据，价值最高）**
本轮检索出现**明确的文献层噪声**：VQualA 短视频参与度预测 [22]、RSNA 腹部创伤 CT 数据集 [21]、Point Transformer V3 Extreme [19]、开放式学习智能体 [20]、AP 定义语言建模 [17]、AuTexTification 文本检测 [13]、K0s/Λ 粒子物理 [28][29]、以及中文土地确权/土壤重金属/矿区复垦 [31][32][33] 被召回进 VLA 主题。这不是无关紧要的细节——它说明**基于关键词/向量的文献召回在「VLA」这类高歧义缩写上系统性失真**，进而使「某方向有多少篇论文」这类计量结论不可靠。证据等级：E 级（内容与主题无关），但作为**方法论证据**为 A 级观察。

**瓶颈 C：自动抽取管线与子问题的错配**
q2 问的是「RT-1/RT-2/OpenVLA/π0 的承上启下 + 数据集口径」，实际返回的是「路径偏差检测」[14]、「装配动作理解」[2]、「低资源推理」[16]。即**抽取层把「含 VLA 关键词」误当作「回答问题」**。结论：任何基于该管线的综述都需人工回填经典文献。

**瓶颈 D：数据瓶颈**
本轮**无任何数据规模、采集成本、标注工时的一手数字** `> 待核实`。[18] 只确立「多本体聚合」这一路线 [18]，未提供本报告可引用的规模数字。

### 数据集与基准（口径与可比性边界）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明（口径 / 可比性边界） |
|---|---|---|---|---|---|---|---|---|
| Open X-Embodiment（含 RT-X 模型） | 2023 | 多方合作，名单 `> 待核实` | `> 待核实` | arXiv preprint v9 [18] | 高：跨本体聚合的事实标准叙事源头 [18] | ★★★★★ 跨本体比较的起点，但**异构本体动作空间对齐口径需查原文** `> 待核实` | http://arxiv.org/abs/2310.08864v9 | 真机多本体数据；任务是「混合多本体训练能否正迁移」[18] |
| 2025 BEHAVIOR Challenge | 2025 | 未标明 `> 待核实` | `> 待核实` | arXiv preprint [9] | 高：本轮唯一有名次的榜单证据 [9] | ★★★★☆ 长程家务评测的代表，但**纯仿真**，不能外推真机 [9] | http://arxiv.org/abs/2512.06951v2 | **50 个**长程家务任务；需**双臂操作 + 导航 + 上下文决策**；照片级仿真 [9] |
| LIBERO / CALVIN / SimplerEnv / RoboArena / DROID | — | — | `> 待核实` | `> 待核实` | 未知 | `> 待核实` | — | **本轮来源列表未覆盖**，因此不给出任务数、本体数、仿真/真机属性。任何具体数字均属编造风险，一律不作断言 `> 待核实` |

**拐点判断**：`较大概率`（依据：四篇独立推理优化论文在 4 个月内出现 [16][24][26][27]，且均以「部署可行性」为动机陈述）。**可证伪条件**：若到 2027-06，主流 VLA 论文的方法章节仍普遍不报告吞吐/时延，则「推理已成核心瓶颈」判断不成立。

---

## 5. 社会·政策·国际（Society, Policy & Geopolitics）

**一句话增量判断**：**本周期在给定来源内无显著变化**——21 条相关来源中，**没有任何一条**涉及监管、标准、出口管制、供应链、劳动影响或伦理治理的一手材料。此处不填充推测性内容。

可谨慎陈述的三点（并明确其证据边界）：

- **多语言能力的不均衡已可被实证**：[11] 对 OpenVLA 做土耳其语指令理解评测 [11]，这是本轮唯一触及「非英语场景」的来源。它间接提示：开放权重模型的能力扩散是**全球性**的，而评测覆盖是**局部性**的。热度 `> 待核实`；权威：IEEE SIU 2026 [11]；关注度：低（区域性会议 + 单一模型）[11]；推荐度 ★★★☆☆（稀缺性大于影响力）[11]。
- **开放权重带来的治理张力（推断，非事实）**：[7][10][23] 均以 "Open" 为核心属性 [7][10][23]，而本轮**未取得任何许可证条款、商用限制、双重用途审查**的一手证据 `> 待核实`。因此「开放权重是否加速能力扩散快于标准制定」只能作为 `[P]` 预测（见第 7 章 H4），不能作为现状陈述。
- **地缘与供应链**：`> 待核实`。本轮来源中唯一涉及硬件可得性的表述是 [23] 摘要提到的「可负担遥操作系统的普及」作为研究加速动因 [23]，属研究基础设施层面，**不构成供应链或产业政策证据**。

---

## 6. 资本与生态（Capital & Ecosystem）

**一句话增量判断**：**融资、并购、人才流动数据在本轮来源中为零**，因此本章只能给出「生态结构」的增量，不能给出「资本流向」的增量。结构上的真实变化是：生态从「论文 + 仓库」两层，变成「基础模型 — 推理服务 — 应用适配」三层。

**生态三层结构（由来源自身定位推断）**

| 层 | 代表条目 | 该层存在的证据 | 四类证据 |
|---|---|---|---|
| 基础模型层 | OpenVLA [10]、GR00T N1 [7]、VLA-Adapter [26] | 标题即自述为 model / foundation model [7][10][26] | 热度 `> 待核实`；权威 arXiv preprint [7][10][26]；关注度：高（OpenVLA/GR00T 为社区通用基线名）但**无量化支撑** `> 待核实`；推荐度 ★★★★★ [10][7] / ★★★★☆ [26] |
| 推理服务层 | VLAgents [27]、BLURR [16]、实时化 [24] | 标题自述为 server / inference wrapper / real-time [16][24][27] | 热度 `> 待核实`；权威 arXiv preprint [16][24][27]；关注度：中（新近出现，尚无引用积累）[16][24][27]；推荐度 ★★★★☆ [27][24]、★★★☆☆ [16] |
| 应用适配层 | 微调优化 [8]、实践改进 [30]、榜单方案 [9]、评测分析 [11] | 标题指向 fine-tuning / in practice / challenge solution [8][9][30] | 热度 `> 待核实`；权威 arXiv preprint + IEEE SIU [8][9][11][30]；关注度：中（[9] 因榜单名次最高）[9]；推荐度 ★★★★☆ [8][30]、★★★★★ [9] |

**生态缺口（结构性）**
- **缺少中立的第三方评测组织**：本轮所有比较性主张均来自作者自评（[9] 是自我参赛并自我报告）[9]，无独立复现方。
- **缺少「跨层」整合工作**：基础模型 [7][10]、推理服务 [27][16]、适配 [8][30] 三层之间**没有一篇端到端报告各层组合后的总收益**。这是生态中最明显的整合空白。
- **开源库的可持续性指标缺失**：LeRobot 已论文化 [23]，但维护者规模、发布节奏、issue 响应等本轮均 `> 待核实`。

**资本侧**：融资额、并购、团队流动 —— `> 待核实（本轮无来源）`。**结论：本周期资本维度无显著变化证据，不作出判断。**

---

## 7. 信号与预测（Signals & Forecast）

**一句话增量判断**：本轮最强的可观测信号是「**推理层在 4 个月内独立成文四篇**」[16][24][26][27]；最弱的是「架构层 SOTA 变动」——因为 π0/π0.5、Gemini Robotics 等一手来源缺失，架构判断的置信度必须下调。

### 7.1 早期信号（已确证事实）

| 信号 | 时间 | 证据 | 强度 |
|---|---|---|---|
| 推理优化从「附带讨论」变为「论文主题」 | 2025-10 至 2026-01 | [24][16][26][27] | 确定（四篇独立来源） |
| VLA 与 agentic tool-use 合流 | 2026-08 | [3] | 较大概率（单篇，无独立验证） |
| 分层 VLA 开始补「对齐」短板 | 2026 | [6] | 较大概率（单篇） |
| 训练信号从纯模仿扩展到奖励世界模型 | 2026 | [12] | 推测（单篇，摘要级） |
| 失效检测从「外部模块」转向「复用内部注意力」 | 2026-03 | [14]、辅以 [1] | 较大概率（两篇同向） |
| 开源库论文化 | 2026-02 | [23] | 确定（单点，但形态明确） |

### 7.2 可证伪预测（`[P]`，含依据链与置信度）

- **H1（置信度：较大概率）**：到 2027-06，VLA 论文的实验表格将普遍包含推理吞吐/时延列。
  *依据链*：[16][24][26][27] 四篇同期以部署可行性为动机 → 社区问题意识已转移 → 报告规范随之改变。
  *证伪条件*：抽查 2027 年 CoRL/ICRA/RSS 的 VLA 论文 ≥10 篇，若含时延列的 <30%，则 H1 不成立。

- **H2（置信度：推测）**：到 2027-12，「分层/工具调用」将成为 VLA 论文中 ≥30% 采用的显式架构组件。
  *依据链*：[3] 提供工具注入、[6] 提供分层对齐 → 两条独立路线同向 → 组合成本低于端到端扩参。
  *证伪条件*：2027 年顶会 VLA 论文中显式采用 hierarchy/tool-use 的比例 <15%。

- **H3（置信度：推测）**：2027 年内将出现**强制真机赛道**的 VLA 基准，作为对纯仿真榜单 [9] 的回应。
  *依据链*：本轮唯一榜单为纯仿真 [9]，且实时性主张无第三方复现 [24] → 仿真-真机差距成为公认风险 → 基准设计者需回应。
  *证伪条件*：到 2027-12，无任何主流 VLA 基准增设真机/物理赛道。

- **H4（置信度：推测）**：开放权重 VLA（[7][10]）的能力扩散速度将快于相关安全标准与评测规范的出台。
  *依据链*：[7][10] 已开放 → 本轮来源中**零篇**标准/监管材料（见第 5 章）→ 扩散与治理存在时间差。
  *不确定性*：许可证与商用条款未核实 `> 待核实`，若实际限制严格则 H4 显著减弱。

- **H5（置信度：较大概率）**：2027 年前会出现「VLA 失效模式分类学」类论文。
  *依据链*：[14] 指出视觉推理幻觉是导航瓶颈、[1] 指出需在推理时重定向注意力 → 失效机理已被识别为独立问题 → 分类学是自然下一步。
  *证伪条件*：2027-12 前无标题含 failure taxonomy / failure modes 的 VLA 综述或实证论文。

### 7.3 Watchlist（需持续追踪）

1. **[24] 的可复现性**——30Hz/480Hz 与单消费级 GPU 是本轮最激进的主张，第三方复现与否决定「实时 VLA」是否成立。
2. **[9] 的后续**——π0.5 架构在 BEHAVIOR 上的冠军方案是否被移植到真机。
3. **[3] 的工具注入是否被复用**——决定「VLA+agent」是分支还是主干。
4. **π0 / π0.5 / Gemini Robotics / RDT-1B / Octo 的一手引用补全**——这是本报告最大的证据空洞，直接决定第 1 章架构判断能否升级。
5. **LIBERO / CALVIN / SimplerEnv / RoboArena / DROID 的官方口径**——补全后才能做跨基准可比性分析。
6. **LeRobot [23] 的仓库活跃度指标**（star / 提交频率 / 贡献者数）——本轮全部 `> 待核实`。

---

## 参考来源

> 说明：[1]–[33] 为本轮全部候选编号来源，编号与正文引用一一对应。标注「未采用」者为 E 级无关来源，已在第 4 章作为**文献召回噪声的方法论证据**使用。

1. Inference-Time Attention Steering for Vision-Language-Action Driving Models — http://arxiv.org/abs/2608.17095v1
2. Compositional Context Fine-Tuning Vision-Language Model for Complex Assembly Action Understanding from Videos — http://arxiv.org/abs/2607.10797v1
3. Evolve Vision-Language-Action Model into an Agent with On-the-fly Tool-use — http://arxiv.org/abs/2608.14047v3
4. UIC-AIHealth4All at ArchEHR-QA 2026: Answer-First Evidence Grounding for Clinical Question Answering — http://arxiv.org/abs/2608.27467v1（未采用，E 级）
5. $A_{1}$: Adaptive Truncated Vision-Language-Action Model From Affordance to Action — https://doi.org/10.1109/cvprf71909.2026.00149
6. Grounding Hierarchical Vision-Language-Action Models Through Explicit Language-Action Alignment — https://doi.org/10.1109/cvprf71909.2026.00889
7. GR00T N1: An Open Foundation Model for Generalist Humanoid Robots — http://arxiv.org/abs/2503.14734v2
8. Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success — http://arxiv.org/abs/2502.19645v2
9. Task adaptation of Vision-Language-Action model: 1st Place Solution for the 2025 BEHAVIOR Challenge — http://arxiv.org/abs/2512.06951v2
10. OpenVLA: An Open-Source Vision-Language-Action Model — http://arxiv.org/abs/2406.09246v3
11. Performance Analysis of Vision-Language-Action Models: Evaluating Turkish Command Understanding in OpenVLA — https://doi.org/10.1109/siu71813.2026.11636432
12. IRL-VLA: Vision-Language-Action Training via Reward World Model — https://doi.org/10.1109/cvprf71909.2026.00098
13. Overview of AuTexTification at IberLEF 2023 — http://arxiv.org/abs/2309.11285v1（未采用，E 级）
14. Your Vision-Language-Action Model Already Has Attention Heads For Path Deviation Detection — http://arxiv.org/abs/2603.13782v1
15. RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control — http://arxiv.org/abs/2307.15818v1
16. BLURR: A Boosted Low-Resource Inference for Vision-Language-Action Models — http://arxiv.org/abs/2512.11769v1
17. A Simulation and Modeling of Access Points with Definition Language — http://arxiv.org/abs/1304.1836v2（未采用，E 级）
18. Open X-Embodiment: Robotic Learning Datasets and RT-X Models — http://arxiv.org/abs/2310.08864v9
19. Point Transformer V3 Extreme — http://arxiv.org/abs/2407.15282v1（未采用，E 级）
20. Open-Ended Learning Leads to Generally Capable Agents — http://arxiv.org/abs/2107.12808v2（未采用，E 级）
21. The RSNA Abdominal Traumatic Injury CT (RATIC) Dataset — http://arxiv.org/abs/2405.19595v1（未采用，E 级）
22. VQualA 2025 Challenge on Engagement Prediction for Short Videos — http://arxiv.org/abs/2509.02969v1（未采用，E 级）
23. LeRobot: An Open-Source Library for End-to-End Robot Learning — http://arxiv.org/abs/2602.22818v1
24. Running VLAs at Real-time Speed — http://arxiv.org/abs/2510.26742v1
25. Robotic VLA Benefits from Joint Learning with Motion Image Diffusion — http://arxiv.org/abs/2512.18007v1
26. VLA-Adapter: An Effective Paradigm for Tiny-Scale Vision-Language-Action Model — http://arxiv.org/abs/2509.09372v2
27. VLAgents: A Policy Server for Efficient VLA Inference — http://arxiv.org/abs/2601.11250v1
28. Azimuthal anisotropy of K0s and Lambda production at mid-rapidity from Au+Au collisions — http://arxiv.org/abs/hep-ex/0205072v1（未采用，E 级）
29. Overview of results from the STAR experiment at RHIC — http://arxiv.org/abs/hep-ex/0306056v1（未采用，E 级）
30. From Foundation to Application: Improving VLA Models in Practice — http://arxiv.org/abs/2607.06403v1
31. 自然资源统一确权登记中的重难点分析及应对措施研究 — https://doi.org/10.37155/2811-0625-0204-15（未采用，E 级）
32. 土壤重金属污染来源、现状以及修复治理技术研究进展 — https://doi.org/10.36956/edc.v2i11.258（未采用，E 级）
33. 开采扰动区土地复垦改良技术与矿区生态修复配套开采方案研究 — https://doi.org/10.37155/2811-0595-0508-17（未采用，E 级）

---

*Generated by research-bot · topic=`具身智能与视觉-语言-动作vla前沿` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`deepseek-v4-flash` · sources=33 · duration=174s · 2026-10-20T22:19:29+00:00*
