# 人工智能（Artificial Intelligence / 基础模型）前沿调研报告

**日期**：2026-10-04（UTC）　**领域**：基础模型 / 大语言模型（LLM）/ 多模态基础模型
**检索源**：132 条候选引用（编号 [1]–[132]），另附领域人工种子资源 3 篇论文、4 个开源项目、3 个数据集/基准清单
**证据分级口径**：A=同行评审/官方技术报告；B=arXiv 预印本/官方仓库；C=第三方复现或榜单；D=社区二手；E=不可访问
**阅读提示**：本报告严格遵守“无 [n] 不结论、无出处不写数字”的纪律。凡候选证据未覆盖者，一律写 `> 待核实`。

---

## 摘要（Executive Summary）

1. **证据覆盖极不均衡，报告只能给出“局部可验证结论”。** 本轮 132 条候选中，**关于推理模型（o3、DeepSeek-R1、Qwen3、s1、Kimi k1.5）、GPT-3/Chinchilla/Switch Transformer/Mixtral/FlashAttention、MCP/AutoGPT/LangGraph/OpenHands/SWE-agent、Sora/Genie 的一手论文几乎全部缺席**；而 Agent 评测、GUI Agent、MoE 路由与负载均衡、长上下文与 Mamba 替代架构、多模态基准这五个方向有较集中的 2025–2026 预印本 [87][89][90][101][107][28][35][41][124][125][126]。
2. 可验证的最强结论集中在三处：**(a) 计算机使用 Agent（computer-use agent）的“效率瓶颈”已被基准化**，SOTA 系统端到端延迟高达数十秒级，准确率导向的评测掩盖了可用性问题 [87]；**(b) GUI Agent 存在“知识—执行鸿沟”**，即使检索知识 90% 正确，实际执行成功率仅 41% [89]；**(c) MoE 的负载不均衡是可被系统性攻击的核心工程问题**，已有多种路由/负载均衡方案与理论框架提出 [100][103][104][97]。
3. 后训练方向只有 InstructGPT 一手的间接证据链（[21] 及其衍生分析 [23][24]）与若干规避 PPO 的替代方案 [15][17]，**DPO、RLVR（可验证奖励强化学习）的一手论文本轮均未检索到**。`> 待核实`
4. 长上下文方向出现**“声称长度 ≠ 有效长度”的共识性批评**，RULER 一类基准专门用于揭穿虚标上下文窗口 [35][28][29]，128K 级上下文还需要专门的数据工程 [30]。
5. **负面/失败证据被明确记录**：RL 微调后模型在非理想条件下推理能力下降 [58]；Mamba 在 COPY 与 CoT 类任务上存在结构性局限 [46]；大模型能耗测量此前长期被忽视 [37]。这些应与正向 SOTA 声明同等对待。

---

## 一、关键前沿进展（近 1–2 年）

> 本节只列候选证据中**可核查**的条目；每条给出热度 / 权威 / 关注度 / 推荐度四类证据。

- **计算机使用 Agent 的效率基准 OSWorld-Human（2025）** [87]：指出领域内 SOTA 只追求准确率，端到端延迟达数十秒至数分钟，系统“practically unusable”。热度：`> 待核实`（候选未提供 citations）[87]；权威：arXiv cs.AI 预印本（B 级）[87]；关注度：**中**——直接点名当时 SOTA 系统的可用性缺陷，属于基准类“泼冷水”工作 [87]；推荐度：★★★★☆——研究 computer-use agent 落地必读的效率维度补充 [87]。
- **UI-Evol：GUI Agent 的知识—执行鸿沟（2025）** [89]：量化给出“90% 正确知识 → 41% 执行成功”的落差。热度：`> 待核实` [89]；权威：arXiv cs.HC 预印本（B 级）[89]；关注度：**中**——提供可复述的量化数字，易被后续工作引用 [89]；推荐度：★★★★☆——把“检索增强”与“真实执行”解耦的关键证据 [89]。
- **Agent 基准论文自披露审计（2026）** [77]：直指“同一 benchmark、同一模型名、两篇论文结论互相矛盾”的复现性问题，并给出开放评分 schema。热度：`> 待核实` [77]；权威：arXiv cs.LG 预印本（B 级）[77]；关注度：**中高**——触及评测方法学痛点 [77]；推荐度：★★★★★——做 Agent 评测前的必读方法学警示 [77]。
- **MoE 架构演进技术综述（2026）** [101]：以一手论文与官方技术报告为素材，综合路由（routing）、拓扑（topology）、负载均衡与专家并行（expert parallelism）。热度：`> 待核实` [101]；权威：arXiv cs.CL 预印本综述（B 级）[101]；关注度：**中**——2026 年新出，尚无引用信号 [101]；推荐度：★★★★☆——MoE 方向最系统的入口文档之一 [101]。
- **MoE 负载均衡的两条技术路线**：[100] 提出 Latent Prototype Routing 声称近完美负载均衡；[104] 给出**无辅助损失（auxiliary-loss-free）**负载均衡的理论框架，[103] 用相似度保持路由（similarity preserving routers）解决同一问题。热度：均 `> 待核实` [100][103][104]；权威：均为 arXiv（cs.LG）预印本（B 级）[100][103][104]；关注度：**中**——同一问题三个月内多篇竞争，说明是工程刚需 [100][103][104]；推荐度：★★★★☆ [100][104]、★★★☆☆ [103]。
- **长上下文的三重证据**：RULER 基准追问“真实上下文尺寸” [35]；“Thus Spake Long-Context LLM”给出系统性梳理 [28]；128K 上下文需要专门数据工程 [30]。热度：`> 待核实` [28][30][35]；权威：arXiv 预印本（B 级），RULER 已被后续工作反复引用（候选未给数）[35]；关注度：**中高** [35]；推荐度：★★★★★ [35]、★★★★☆ [28][30]。
- **状态空间模型（SSM / Mamba）作为注意力替代**：Vision Mamba 把双向 SSM 用于视觉表征 [41]；Mamba-360 综述系统整理方法、应用与挑战 [47]；但 [46] 明确指出 Mamba 在 COPY 与 CoT 类推理上存在局限。热度：`> 待核实` [41][46][47]；权威：arXiv 预印本（B 级）[41][47]；关注度：**中高**——[41] 属该方向高讨论度代表作之一（候选未给 star/引用，`> 待核实`）[41]；推荐度：★★★★☆ [41][47]、★★★★★（作为反方证据）[46]。
- **多模态视频评测的迭代**：Video-MME 建立首个全面视频多模态评测 [125]，其后继 Video-MME-v2 试图推进到“下一阶段” [124]；Uni-MMMU 提供跨学科统一多模态基准 [126]。热度：`> 待核实` [124][125][126]；权威：均为 arXiv 预印本（B 级）[124][125][126]；关注度：**中高**（Video-MME 系列被广泛用作对比口径）[125]；推荐度：★★★★☆ [124][125][126]。

> **检索噪声提示**：候选块中 [49][50][51][53][54]（认知流、印度计算教育会议、意大利语物理常识、价值奖励探索、Open Ant 机器人平台）与“推理模型与测试时计算”主题无实质关联，属召回噪声，本报告不予采信。

---

## 二、推理与测试时计算（Test-Time Compute / Inference-Time Scaling）

**可支撑的结论**

- **官方系统卡是本方向最高等级证据。** OpenAI o1 System Card 以官方系统卡形式发布 [67]，属 A/B 级权威来源。热度：`> 待核实` [67]；权威：官方系统卡（arXiv 载体，A 级）[67]；关注度：**高**——系统卡格式被后续推理模型普遍沿用 [67]；推荐度：★★★★★——任何 o1 能力断言都应以系统卡而非二手解读为准 [67]。
- **第三方评测已出现，但口径有限。** [66] 用 o1-preview 评估教育场景高阶思维；[68] 在法律推理任务上横向对比 o1 与 DeepSeek-R1 的测试时扩展（test-time scaling）表现。热度：`> 待核实` [66][68]；权威：arXiv 预印本（B 级），非同行评审 [66][68]；关注度：**中**——属早期第三方评测 [66][68]；推荐度：★★★☆☆——可作口径参考，但单一领域结论不可外推 [66][68]。
- **“把计算从测试时前移”的新范式：Sleep-time Compute（2025）** [69]：提出在非推理时段预计算，突破纯测试时扩展的边界。热度：`> 待核实` [69]；权威：arXiv 预印本（B 级）[69]；关注度：**中**——概念新颖，但候选无独立复现证据 [69]；推荐度：★★★★☆——test-time scaling 之外值得跟踪的替代路线 [69]。
- **RL 与 LLM 全生命周期综述（2025）** [52]：覆盖 RL 在 LLM 全流程（含推理增强）的作用。热度：`> 待核实` [52]；权威：arXiv cs.CL 综述（B 级）[52]；关注度：**中** [52]；推荐度：★★★★☆——用于建立 RL↔LLM 的术语地图 [52]。
- **对齐可提升推理，但收益有条件。** [57] 用 alignment 让 LLM 成为更好的推理者；[58] 给出反向证据：**RL 微调后，模型在非理想条件下的推理能力下降**。热度：`> 待核实` [57][58]；权威：arXiv 预印本（B 级）[57][58]；关注度：**中**——[58] 的负向结论对“RL 必然提升推理”的叙事构成重要制衡 [58]；推荐度：★★★★☆ [58]、★★★☆☆ [57]。
- **RLVR 与世界模型：RLVR-World（2025）** [70] 用强化学习训练世界模型。**注意**：该文标题中的 RLVR 语境为世界模型训练，**不能据此推断等同于“可验证奖励强化学习（RLVR）”**。热度：`> 待核实` [70]；权威：arXiv 预印本（B 级）[70]；关注度：**中** [70]；推荐度：★★★☆☆——需先核实术语口径再引用 `> 待核实` [70]。

**证据缺口（关键）**

> 候选证据中**不存在** OpenAI o3、DeepSeek-R1 原始技术报告、Qwen3、s1（test-time scaling 极简基线）、Kimi k1.5 的任何一手条目，也不存在上述模型在 **AIME / MATH / GPQA** 上的可核对数字（含硬件、采样数、评测口径）。任何关于“某模型在某推理榜达到 X%”的陈述，本轮**无法验证**，一律 `> 待核实`。

---

## 三、后训练：RLHF / RLVR / 偏好优化

**可支撑的结论**

- **RLHF 的奠基范式来自 InstructGPT** [21]（“Training language models to follow instructions with human feedback”）：确立“监督微调 + 人类偏好奖励模型 + RL 优化”的三段式。热度：`> 待核实`（候选未提供引用数）；权威：arXiv 预印本条目（原工作发表于 NeurIPS，A 级）；关注度：**高**——被几乎所有后续对齐工作作为基线引用 [21]；推荐度：★★★★★——后训练方向第一必读 [21]。
- **语言反馈（language feedback）作为替代信号** [24]：探索用自然语言反馈而非标量偏好训练语言模型。热度：`> 待核实` [24]；权威：arXiv 预印本（B 级）[24]；关注度：**中** [24]；推荐度：★★★★☆——RLHF 之外的第二类监督信号 [24]。
- **去除 PPO 的排序式对齐：RRHF（2023）** [15]：以“对响应排序”对齐语言模型，宣称无需 PPO 的复杂实现。热度：`> 待核实` [15]；权威：arXiv 预印本（B 级，v3）[15]；关注度：**中**——属 DPO 同期“简化 RLHF”路线之一 [15]；推荐度：★★★★☆——理解偏好优化谱系的重要坐标 [15]。
- **人机交互式 RLHF 工具链：RLHF-Blender（2023）** [17]：提供可配置的交互界面，用于从多样人类反馈中学习。热度：`> 待核实` [17]；权威：arXiv 预印本（B 级）[17]；关注度：**中** [17]；推荐度：★★★☆☆——工程/实验平台视角 [17]。
- **下游能力观测：用 InstructGPT 做类比生成** [23]：说明指令跟随模型在抽象类比任务上的实际表现。热度：`> 待核实` [23]；权威：arXiv 预印本（B 级）[23]；关注度：**低中** [23]；推荐度：★★★☆☆——仅作能力侧写 [23]。
- **后训练透明度开始被外部索引化**：2025 Foundation Model Transparency Index 为第三版年度量化工作 [39]。热度：`> 待核实` [39]；权威：arXiv cs.AI 预印本（B 级），由研究机构年度发布 [39]；关注度：**中高** [39]；推荐度：★★★★☆——评估厂商后训练/数据披露程度的唯一系统性指标之一 [39]。

**证据缺口（关键）**

> **DPO（Direct Preference Optimization）原始论文、RLVR（可验证奖励强化学习）原始论文、GRPO 及其变体、过程奖励模型（PRM）的一手条目在本轮候选中全部缺失**，因此“后训练从 RLHF/DPO 演进到 RLVR”这一命题在本轮**只能作为待验证假设**，不能写成结论。`> 待核实`

---

## 四、Agent、工具使用与评测

**4.1 评测与可复现性（本方向最强的一手证据）**

- **同一 benchmark 结果不可复现已被系统记录** [77]：审计 12 篇知名 Agent 基准论文，指出论文对“如何运行评测”披露不足，导致同名模型结论冲突。热度：`> 待核实` [77]；权威：arXiv cs.LG 预印本（B 级）[77]；关注度：**中高** [77]；推荐度：★★★★★——写/读 Agent 评测论文的方法学底线 [77]。
- **GUI Agent 综述已迭代至 v12** [90]：说明该方向文献更新速度极快（arXiv 版本号可作为社区活跃度的间接信号）。热度：`> 待核实` [90]；权威：arXiv 预印本综述（B 级）[90]；关注度：**中高** [90]；推荐度：★★★★★——GUI Agent 的最佳入口 [90]。
- **效率维度基准 OSWorld-Human** [87]（见第一章）；**科学软件方向新基准 OSWorld-Science** [94]。热度：`> 待核实` [94]；权威：arXiv 预印本（B 级）[94]；关注度：**中**——2026 年新出 [94]；推荐度：★★★★☆ [94]。
- **GUI 视频理解数据集 GUI-World** [85]：提供多模态 GUI 导向理解的视频基准。热度：`> 待核实` [85]；权威：arXiv 预印本（B 级）[85]；关注度：**中** [85]；推荐度：★★★★☆ [85]。

**4.2 工具检索与工具选择**

- **工具检索被单独基准化** [74]：“Retrieval Models Aren't Tool-Savvy”指出通用检索模型并不适配工具检索场景。热度：`> 待核实` [74]；权威：arXiv 预印本（B 级）[74]；关注度：**中** [74]；推荐度：★★★★☆——工具调用链路中常被忽略的一环 [74]。
- **小模型工具学习能力不足** [76]：多 LLM Agent 分工以弥补单体弱工具学习能力。热度：`> 待核实` [76]；权威：arXiv 预印本（B 级）[76]；关注度：**中** [76]；推荐度：★★★☆☆ [76]。
- **权限安全：Agent 倾向选择过度权限的工具** [75]：把“工具选择”从元数据偏好推进到**权限敏感**维度。热度：`> 待核实` [75]；权威：arXiv cs.SE 预印本（B 级）[75]；关注度：**中** [75]；推荐度：★★★★☆——Agent 安全的新切面 [75]。

**4.3 多智能体与编排**

- **多智能体污染传播的测量框架** [83]：提出错误在多 Agent 系统中的传播度量与基准。热度：`> 待核实` [83]；权威：预印本（B/C 级，平台 DOI 载体）[83]；关注度：**低中** [83]；推荐度：★★★☆☆ [83]。
- **计划级安全存在“逐步检查 ≠ 整体检查”的裂缝** [80][81]：分解攻击（decomposition attacks）利用该裂缝。热度：`> 待核实` [80][81]；权威：Zenodo 预印本（B/C 级）[80][81]；关注度：**中** [80][81]；推荐度：★★★★☆——Agent 安全评估的重要反例集合 [80][81]。
- **企业级工具编排框架 Z-SPACE** [84]、**Agent-as-a-Graph** [93]、**多 Agent 协调基准** [91]：分别代表工程框架与检索式编排两条路线。热度：`> 待核实` [84][91][93]；权威：[84] 为 SSRN 预印本（C 级）、[93] 为会议论文 DOI（B 级）、[91] 为期刊补充材料（B 级）[84][91][93]；关注度：**低中** [84][93]；推荐度：★★★☆☆ [84][93]。
- **垂域多 Agent 应用**：ASIC 设计多 Agent 系统 [73]（2025 IEEE ICLAD，**citations=5**，为本报告候选中唯一带可核查引用数的条目）；AI Hospital 多 Agent 综述 [86][88]；Java 测试用例生成竞赛 [79]。热度：citations=5 [73]，其余 `> 待核实`；权威：[73] 为 IEEE 会议论文（A 级），[86][88] 为 OSF 预印本（C 级）[73][86]；关注度：**中**（[73] 有 5 次引用）[73]；推荐度：★★★★☆ [73]、★★★☆☆ [79][86]。

**证据缺口（关键）**

> **MCP（Model Context Protocol）规范、AutoGPT、LangGraph、OpenHands、SWE-agent 的一手条目或官方仓库条目在本轮候选中全部缺失**；“这些项目的成熟度、可复现性与部署门槛”**无法在本轮给出任何可核查结论**。vLLM / SGLang 仅出现在人工种子资源清单中（非实时检索），其 star、版本、性能数字均 `> 待核实`。

---

## 五、多模态与架构（MoE / 长上下文 / 效率）

### 5.1 MoE 架构与扩展律

- **DeepSeek-V3 官方技术报告** [107]：MoE 大模型最具分量的一手技术文档之一。热度：`> 待核实` [107]；权威：官方技术报告（arXiv 载体，A 级）[107]；关注度：**高**——MoE 训练成本与架构披露的关键一手来源 [107]；推荐度：★★★★★。
- **无辅助损失负载均衡的理论框架** [104] 与 **Latent Prototype Routing** [100]：前者为辅助损失去除提供理论支撑，后者声称近完美均衡。热度：`> 待核实` [100][104]；权威：arXiv cs.LG 预印本（B 级）[100][104]；关注度：**中** [100][104]；推荐度：★★★★☆ [104]、★★★★☆ [100]。
- **路由可解释性**：Task-Conditioned Routing Signatures 用向量表示刻画专家选择模式 [97]。热度：`> 待核实` [97]；权威：arXiv cs.LG 预印本（B 级）[97]；关注度：**中** [97]；推荐度：★★★★☆——理解 MoE 内部行为的少数尝试 [97]。
- **推理/部署侧效率**：ExpertFlow 提出预测式专家缓存与 token 调度 [98]；FlexMoE 提出嵌套式专家内剪枝以适配部署预算 [95]；TAOT 用拓扑感知最优传输做专家副本放置 [109]。热度：`> 待核实` [95][98][109]；权威：均为 arXiv 预印本（B 级）[95][98][109]；关注度：**中** [95][98]；推荐度：★★★★☆ [95][98]、★★★☆☆ [109]。
- **量化代价的量化分析** [106]：对 DeepSeek 模型量化后的性能下降做定量分析。热度：`> 待核实` [106]；权威：arXiv 预印本（B 级）[106]；关注度：**中** [106]；推荐度：★★★★☆——部署前的必要风险数据 [106]。
- **扩展律方面**：候选仅提供一篇把神经扩展律根植于数据分布的工作 [112]。热度：`> 待核实` [112]；权威：arXiv 预印本（B 级）[112]；关注度：**中** [112]；推荐度：★★★★☆。
  > **Chinchilla 扩展律、数据墙争议及其反驳，在本轮候选中无任何一手条目**，无法验证。`> 待核实`

### 5.2 长上下文与 KV 效率

- **Thus Spake Long-Context LLM** [28]、**RULER** [35]、**128K 数据工程** [30]：共同构成“宣称长度 vs 有效长度”的证据三角。热度：`> 待核实` [28][30][35]；权威：arXiv 预印本（B 级）[28][30][35]；关注度：**中高** [35]；推荐度：★★★★★ [35]。
- **黑盒上下文长度探测** [29]：用探测方法推断模型对上下文的实际使用能力，作为 RULER 之外的方法学补充。热度：`> 待核实` [29]；权威：arXiv 预印本（B 级）[29]；关注度：**中** [29]；推荐度：★★★☆☆ [29]。
- **多 Agent 场景的 KV cache 共享压缩** [48]：PolyKV 提出共享的非对称压缩 KV 池。热度：`> 待核实` [48]；权威：arXiv 预印本（B 级）[48]；关注度：**中** [48]；推荐度：★★★★☆——KV cache 成本问题的直接工程答案 [48]。
- **长上下文在视频/机器人上的外延**：Long Context Tuning for Video Generation [34]；机器人长上下文扩散策略用 past-token prediction 降低训练内存与提升性能 [33]。热度：`> 待核实` [33][34]；权威：arXiv 预印本（B 级，[33] 为 cs.RO）[33][34]；关注度：**中** [33]；推荐度：★★★★☆ [33]、★★★☆☆ [34]。

### 5.3 效率、能耗与替代架构

- **ML.ENERGY Benchmark** [37]：指出能耗在 ML 系统工程中长期被忽视、被低估，并提供自动化测量方法。热度：`> 待核实` [37]；权威：arXiv cs.LG 预印本（B 级）[37]；关注度：**中** [37]；推荐度：★★★★★——做部署选型时不可替代的第三方口径 [37]。
- **Mamba 家族**：Vision Mamba [41]、Differential Mamba [45]、Mamba-360 综述 [47]、医学/红外/语音等应用变体 [42][43][44]。热度：`> 待核实` [41][47]；权威：arXiv 预印本（B 级）[41][47]；关注度：**中高** [41]；推荐度：★★★★☆ [41][47]。
- **反向证据**：Mamba 在 COPY 与 CoT 推理上的局限被专门研究 [46]。关注度：**中高**（对 SSM 替代论的关键制衡）[46]；推荐度：★★★★★。

### 5.4 多模态模型与基准

| 条目 | 年份 | 权威（等级） | 热度 | 关注度 | 推荐度 |
|---|---|---|---|---|---|
| Qwen-VL [128] | 2023 | arXiv 预印本（B） | `> 待核实` | 中 | ★★★★★ |
| LLaVA-OneVision-1.5（开源多模态训练框架）[130] | 2025 | arXiv 预印本（B） | `> 待核实` | 中高 | ★★★★★ |
| ME-VLM（具身认知统一 VLM，4B / 35B-A3B）[118] | 2026 | arXiv cs.CV 预印本（B） | `> 待核实` | 中 | ★★★★☆ |
| Hierarchical Pre-Training of Vision Encoders [120] | 2026 | arXiv cs.CV 预印本（B） | `> 待核实` | 低中 | ★★★★☆ |
| VLM 目标检测/分割的综述与评测 [122] | 2025 | arXiv cs.CV 预印本综述（B） | `> 待核实` | 中 | ★★★★☆ |
| MLLM 综述 [121] | 2023 | arXiv 预印本综述（B） | `> 待核实` | 中高 | ★★★★☆ |
| VLN 基础模型时代综述 [119] | 2024 | arXiv 预印本综述（B） | `> 待核实` | 中 | ★★★★☆ |
| 文生视频/世界模型综述（Sora 讨论）[132] | 2024 | arXiv 预印本综述（B） | `> 待核实` | 中 | ★★★★☆ |
| 医学多模态基准 GMAI-MMBench [127] | 2024 | arXiv 预印本（B） | `> 待核实` | 中 | ★★★☆☆ |

> **缺口提示**：**GPT-4o、Gemini 系列、Chameleon、Emu、Sora、Genie 的一手技术报告或官方条目在本轮候选中全部缺失**；MMMU / MMBench / MathVista 的可核对榜单数字同样缺失。任何“某模型在 MMMU 上达到 X”的表述均 `> 待核实`。此外，候选中的 VQualA 短视频参与度预测 [26] 与多模态基础模型评测无实质关系，属召回噪声。

---

## 六、经典与奠基性工作

> **重要说明**：本轮 132 条候选引用中，**仅 InstructGPT 一项奠基工作有一手/准一手条目 [21]**；Transformer 原论文、CoT、ReAct、GPT-3、Chinchilla、Switch Transformer、Mixtral、FlashAttention 均**未出现在引用列表中**。下表这些行来自**领域人工种子资源清单**（未实时检索），**因此热度列一律标 `> 待核实`，且不赋予 [n] 引用编号**——这是刻意的诚实性约束，而非遗漏。

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Attention Is All You Need | 2017 | NeurIPS（Vaswani et al.） | `> 待核实` | 人工种子清单，无 [n]，`> 待核实` | 中（其命名模因在 arXiv 上持续扩散，2025 年仍有 200 篇同句式标题）[7] | ★★★★★ | https://arxiv.org/abs/1706.03762 | Transformer 奠基；**本行未获本轮 [n] 直接支撑** |
| GPT-3（few-shot / in-context learning） | 2020 | OpenAI | `> 待核实` | 候选未覆盖，`> 待核实` | `> 待核实` | ★★★★★ | `> 待核实` | 少样本学习范式奠基；本轮无任何条目 |
| Chinchilla 扩展律 | 2022 | DeepMind | `> 待核实` | 候选未覆盖，`> 待核实` | `> 待核实` | ★★★★★ | `> 待核实` | 数据/参数配比；本轮无任何条目 |
| InstructGPT（RLHF） | 2022 | OpenAI / NeurIPS | `> 待核实`（候选未给引用数）[21] | arXiv 条目对应 NeurIPS 论文，A 级 [21] | 高——对齐研究的通用基线 [21] | ★★★★★ | https://arxiv.org/abs/2203.02155 | 后训练三段式范式 |
| Chain-of-Thought Prompting | 2022 | Google / NeurIPS | `> 待核实` | 人工种子清单，无 [n] | `> 待核实` | ★★★★★ | https://arxiv.org/abs/2201.11903 | 思维链；**本轮无 [n] 支撑** |
| ReAct | 2022 | Princeton / ICLR | `> 待核实` | 候选未覆盖，`> 待核实` | `> 待核实` | ★★★★★ | `> 待核实` | 推理+行动范式；本轮无条目 |
| Switch Transformer / Mixtral（MoE） | 2021 / 2023 | Google / Mistral | `> 待核实` | 候选未覆盖其一手条目；MoE 机制由综述间接覆盖 [101] | 中——MoE 方向现状见 [100][101][104] | ★★★★☆ | `> 待核实` | 稀疏专家路由；**仅能通过 [101] 间接了解** |
| FlashAttention | 2022 | Stanford | `> 待核实` | 候选未覆盖，`> 待核实` | `> 待核实` | ★★★★★ | `> 待核实` | IO 感知注意力；本轮无条目 |
| Mamba（选择性 SSM） | 2023 | CMU / MIT | `> 待核实` | 家族演进由综述 [47] 与 Vision Mamba [41] 间接覆盖 | 中高 [41][46][47] | ★★★★☆ | https://arxiv.org/abs/2401.09417 | 线性复杂度替代；局限见 [46] |
| RLHF 简化路线：RRHF | 2023 | 阿里（作者信息以原文为准） | `> 待核实` [15] | arXiv 预印本，B 级 [15] | 中 [15] | ★★★★☆ | http://arxiv.org/abs/2304.05302v3 | 免 PPO 的排序式对齐 |

**可间接量化的“范式影响”证据**：[7] 统计 2009–2025 年共 **717 篇**含 “All You Need” 句式的 arXiv 预印本，指出该模式在原论文后呈指数增长（**R² > 0.994**），仅 2025 年就有 **200 篇**；其中被宣称“必需”最多的对象是 “Attention”，共 **28 次** [7]。热度：`> 待核实`（该文自身引用数未提供）[7]；权威：arXiv cs.CY 预印本，**未见同行评审信息**（B/C 级）[7]；关注度：**中**——指标具体、可复查 [7]；推荐度：★★★☆☆——可作为“Transformer 范式长期支配性”的旁证，但**不是技术性结论** [7]。

> 候选中的 [9][10][11][12][13][14][16][18] 均为 “All You Need” 句式衍生条目，多数正文不可访问、`citations=0`，属 D/E 级，**不用于支撑任何技术结论**（[9][10][11] 为 SSRN/Crossref 条目且提示 “Just a moment...”，[12] 为糖尿病会议摘要）[9][10][11][12]。

---

## 七、争议与开放问题

1. **评测可复现性危机（强证据）**：同一 benchmark、同一模型名，不同论文结论不一致；12 篇 Agent 基准论文的披露质量被系统审计 [77]。这是**方法学层面的共识性问题**，而非个别疏漏 [77]。
2. **准确率 ≠ 可用性**：computer-use agent 的端到端延迟数十秒至分钟级，“SOTA”在实用意义上不可用 [87]；同时“90% 正确知识 → 41% 执行成功”说明知识与执行之间存在结构性鸿沟 [89]。
3. **上下文长度虚标**：RULER [35] 与上下文长度探测 [29] 表明“宣称窗口”与“有效窗口”分离；长上下文需要专门数据工程才可能对齐 [30]。取舍问题——**长上下文 vs 检索式 RAG**——本轮**缺乏直接对比实验证据**，`> 待核实`。
4. **架构替代论的反方证据**：SSM/Mamba 在 COPY 与 CoT 推理上的局限 [46] 与 Vision Mamba 等正向结果 [41] 并存，说明“注意力是否可被完全替代”仍无定论。
5. **RL 对推理的净效应存在争议**：正向 [57] 与负向 [58] 证据并存，说明“RL 微调一定提升推理”是被过度简化的叙事 [57][58]。
6. **Agent 安全的三条裂缝**：过度权限工具选择 [75]、计划级安全 vs 逐步检查的缺口与分解攻击 [80][81]、多智能体系统的错误污染传播 [83]。
7. **能耗与隐性成本被系统性低估**：能耗此前长期“overlooked, under-explored, or poorly understood” [37]。
8. **透明度**：厂商在数据、后训练、部署环节的披露程度被年度量化 [39]。
9. **“数据墙 / 扩展律失效”争议**：仅有一篇从数据分布出发的扩展律工作 [112]，**不足以判定争议走向**，`> 待核实`。
10. **本报告自身的元争议**：本轮候选证据与六个子问题之间存在大范围错配（详见摘要与各章缺口提示）。这提示“以检索批次为单位的证据池”本身可能产生系统性偏差，**任何基于单批候选的“前沿综述”都应显式声明覆盖边界**。

---

## 八、建议关注清单（Watchlist）

**高优先级（有可核查一手证据、且问题重要）**

1. **RULER 及长上下文“有效长度”评测线** [35][28][29] —— 长上下文选型的第一道防线。
2. **OSWorld 系列（Human / Science）** [87][94] —— computer-use agent 的“效率+真实科学软件”双维度评测。
3. **UI-Evol 的知识—执行鸿沟线** [89] —— 检索增强在真实执行中失效的量化研究。
4. **Agent 基准披露审计与评分 schema** [77] —— 读论文时的“可信度过滤器”。
5. **无辅助损失 MoE 负载均衡理论** [104] 与 **Latent Prototype Routing** [100] —— MoE 训练稳定性的关键杠杆。
6. **DeepSeek-V3 技术报告** [107] + **量化性能下降分析** [106] —— MoE 部署的成本/精度权衡一手证据。
7. **ML.ENERGY Benchmark** [37] —— 推理成本评估的能耗维度。

**中优先级（概念重要但证据待补）**

8. **Sleep-time Compute** [69] —— 测试时计算之外的计算分配范式。
9. **PolyKV** [48] —— 多 Agent 共享 KV cache 的成本工程。
10. **Mamba 推理局限** [46] 与 **Differential Mamba** [45] —— SSM 能力边界与改良。
11. **ME-VLM** [118] 与 **LLaVA-OneVision-1.5** [130] —— 开源多模态训练可复现性。
12. **Video-MME-v2** [124] 与 **Uni-MMMU** [126] —— 视频/跨学科多模态评测演进。
13. **2025 Foundation Model Transparency Index** [39] —— 后训练与数据披露的外部审计。

**必须补检的空白（本轮完全缺失，建议列为下一轮检索硬性清单）**

14. OpenAI o3 / DeepSeek-R1 / Qwen3 / s1 / Kimi k1.5 的官方技术报告与 AIME/MATH/GPQA 口径数字。
15. DPO、RLVR、GRPO、过程奖励模型（PRM）原始论文。
16. MCP 规范、AutoGPT、LangGraph、OpenHands、SWE-agent、SGLang 官方仓库与技术文档。
17. Chinchilla 扩展律原文与“数据墙”争议的正反双方一手材料。
18. GPT-3、CoT、ReAct、Switch Transformer、Mixtral、FlashAttention 原文（用于补齐第六章表格的热度与权威列）。
19. GPT-4o / Gemini / Chameleon / Emu / Sora / Genie 的官方技术报告与 MMMU / MMBench / MathVista 榜单原始数字。

---

## 参考来源

（编号与本轮候选证据池一致；未在正文引用的编号不列出）

[7] "All You Need" is Not All You Need for a Paper Title: On the Origins of a Scientific Meme — http://arxiv.org/abs/2512.19700v1
[9] Attention is All You Need... Unless You Are a CISO — https://doi.org/10.2139/ssrn.5967774
[10] Attention via Synaptic Plasticity is All You Need — https://doi.org/10.2139/ssrn.6096874
[11] Failure Is All You Need — Attention as Reverse Diffusion — https://doi.org/10.2139/ssrn.7499639
[12] 1882-P: Attention Is All You Need: Temporal Transformer-Based Personalization of Insulin Delivery Parameters — https://doi.org/10.2337/db26-1882-p
[15] RRHF: Rank Responses to Align Language Models with Human Feedback without tears — http://arxiv.org/abs/2304.05302v3
[17] RLHF-Blender: A Configurable Interactive Interface for Learning from Diverse Human Feedback — http://arxiv.org/abs/2308.04332v1
[21] Training language models to follow instructions with human feedback — http://arxiv.org/abs/2203.02155v1
[23] Analogy Generation by Prompting Large Language Models: A Case Study of InstructGPT — http://arxiv.org/abs/2210.04186v2
[24] Training Language Models with Language Feedback — http://arxiv.org/abs/2204.14146v4
[26] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1
[28] Thus Spake Long-Context Large Language Model — http://arxiv.org/abs/2502.17129v2
[29] Black-box language model explanation by context length probing — http://arxiv.org/abs/2212.14815v3
[30] Data Engineering for Scaling Language Models to 128K Context — http://arxiv.org/abs/2402.10171v1
[33] Learning Long-Context Diffusion Policies via Past-Token Prediction — http://arxiv.org/abs/2505.09561v2
[34] Long Context Tuning for Video Generation — http://arxiv.org/abs/2503.10589v1
[35] RULER: What's the Real Context Size of Your Long-Context Language Models? — http://arxiv.org/abs/2404.06654v3
[37] The ML.ENERGY Benchmark: Toward Automated Inference Energy Measurement and Optimization — http://arxiv.org/abs/2505.06371v2
[39] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1
[41] Vision Mamba: Efficient Visual Representation Learning with Bidirectional State Space Model — http://arxiv.org/abs/2401.09417v3
[42] Mamba-Sea: A Mamba-based Framework with Global-to-Local Sequence Augmentation — http://arxiv.org/abs/2504.17515v1
[43] MiM-ISTD: Mamba-in-Mamba for Efficient Infrared Small Target Detection — http://arxiv.org/abs/2403.02148v4
[44] Speech-Mamba: Long-Context Speech Recognition with Selective State Spaces Models — http://arxiv.org/abs/2409.18654v1
[45] Differential Mamba — http://arxiv.org/abs/2507.06204v2
[46] Exploring the Limitations of Mamba in COPY and CoT Reasoning — http://arxiv.org/abs/2410.03810v3
[47] Mamba-360: Survey of State Space Models as Transformer Alternative — https://doi.org/10.2139/ssrn.4930035
[48] PolyKV: A Shared Asymmetrically-Compressed KV Cache Pool for Multi-Agent LLM Inference — http://arxiv.org/abs/2604.24971v1
[49] Navigating the State of Cognitive Flow — http://arxiv.org/abs/2504.16021v1
[50] ACM COMPUTE 2025 Best Practices Track Proceedings — http://arxiv.org/abs/2512.02349v2
[51] Culturally Grounded Physical Commonsense Reasoning in Italian and English — http://arxiv.org/abs/2510.22631v1
[52] Reinforcement Learning Meets Large Language Models: A Survey — http://arxiv.org/abs/2509.16679v1
[53] Value Bonuses using Ensemble Errors for Exploration in Reinforcement Learning — http://arxiv.org/abs/2602.12375v1
[54] The Open Ant: A Robot Platform for Reinforcement Learning Research — http://arxiv.org/abs/2607.18488v1
[57] Making Large Language Models Better Reasoners with Alignment — http://arxiv.org/abs/2309.02144v1
[58] Large Language Models Reasoning Abilities Under Non-Ideal Conditions After RL-Fine-Tuning — http://arxiv.org/abs/2508.04848v1
[66] A Systematic Assessment of OpenAI o1-Preview for Higher Order Thinking in Education — http://arxiv.org/abs/2410.21287v1
[67] OpenAI o1 System Card — http://arxiv.org/abs/2412.16720v2
[68] Evaluating Test-Time Scaling LLMs for Legal Reasoning: OpenAI o1, DeepSeek-R1, and Beyond — http://arxiv.org/abs/2503.16040v2
[69] Sleep-time Compute: Beyond Inference Scaling at Test-time — http://arxiv.org/abs/2504.13171v1
[70] RLVR-World: Training World Models with Reinforcement Learning — http://arxiv.org/abs/2505.13934v2
[73] ASIC-Agent: An Autonomous Multi-Agent System for ASIC Design with Benchmark Evaluation — https://doi.org/10.1109/iclad65226.2025.00033
[74] Retrieval Models Aren't Tool-Savvy: Benchmarking Tool Retrieval for Large Language Models — http://arxiv.org/abs/2503.01763v2
[75] When Lower Privileges Suffice: Investigating Over-Privileged Tool Selection in LLM Agents — http://arxiv.org/abs/2606.20023v2
[76] Small LLMs Are Weak Tool Learners: A Multi-LLM Agent — http://arxiv.org/abs/2401.07324v3
[77] What Twelve LLM Agent Benchmark Papers Disclose About Themselves — http://arxiv.org/abs/2605.21404v1
[79] SBFT Tool Competition 2025 -- Java Test Case Generation Track — http://arxiv.org/abs/2504.09168v1
[80] Checked at Every Step Is Not Checked as a Whole (plan-level safety) — https://doi.org/10.5281/zenodo.22961078
[81] Checked at Every Step Is Not Checked as a Whole (plan-level safety) — https://doi.org/10.5281/zenodo.22961077
[83] Contamination Percolation in Multi-Agent LLM Systems: A Measurement Framework and Benchmark — https://doi.org/10.22541/au.177499048.88707055/v1
[84] Z-SPACE: A Multi-Agent Tool Orchestration Framework for Enterprise-Grade LLM Automation — https://doi.org/10.2139/ssrn.5896270
[85] GUI-World: A Video Benchmark and Dataset for Multimodal GUI-oriented Understanding — http://arxiv.org/abs/2406.10819v2
[86] A Survey on LLM-based Multi-Agent AI Hospital — https://doi.org/10.31219/osf.io/bv5sg_v1
[87] OSWorld-Human: Benchmarking the Efficiency of Computer-Use Agents — http://arxiv.org/abs/2506.16042v2
[88] A Survey on LLM-based Multi-Agent AI Hospital — https://doi.org/10.31219/osf.io/bv5sg_v2
[89] UI-Evol: Automatic Knowledge Evolving for Computer Use Agents — http://arxiv.org/abs/2505.21964v2
[90] Large Language Model-Brained GUI Agents: A Survey — http://arxiv.org/abs/2411.18279v12
[91] Harnessing Language for Coordination: A Framework and Benchmark for LLM-Driven Multi-Agent Control — https://doi.org/10.1109/tg.2025.3564042/mm1
[92] MobileUse: A GUI Agent with Hierarchical Reflection for Autonomous Mobile Operation — http://arxiv.org/abs/2507.16853v1
[93] Agent-as-a-Graph: Knowledge Graph-Based Tool and Agent Retrieval for LLM Multi-Agent Systems — https://doi.org/10.5220/0014473600004052
[94] OSWorld-Science: A Benchmark of Computer Use Agents for Learning and Using Scientific Software — http://arxiv.org/abs/2609.39903v1
[95] FlexMoE: One-for-All Nested Intra-Expert Pruning for MoE Language Models — http://arxiv.org/abs/2606.27866v1
[97] Task-Conditioned Routing Signatures in Sparse Mixture-of-Experts Transformers — http://arxiv.org/abs/2603.11114v1
[98] ExpertFlow: Efficient Mixture-of-Experts Inference via Predictive Expert Caching and Token Scheduling — http://arxiv.org/abs/2410.17954v2
[100] Latent Prototype Routing: Achieving Near-Perfect Load Balancing in Mixture-of-Experts — http://arxiv.org/abs/2506.21328v1
[101] The Evolution of Mixture-of-Experts Architectures in Large Language Models — http://arxiv.org/abs/2608.08650v1
[102] Mixture-of-Experts Models in Vision: Routing, Optimization, and Generalization — http://arxiv.org/abs/2601.15021v1
[103] Load Balancing Mixture of Experts with Similarity Preserving Routers — http://arxiv.org/abs/2506.14038v2
[104] A Theoretical Framework for Auxiliary-Loss-Free Load Balancing of Sparse Mixture-of-Experts — http://arxiv.org/abs/2512.03915v3
[106] Quantitative Analysis of Performance Drop in DeepSeek Model Quantization — http://arxiv.org/abs/2505.02390v2
[107] DeepSeek-V3 Technical Report — http://arxiv.org/abs/2412.19437v2
[109] TAOT: Topology-Aware Optimal Transport for Dynamic Expert Replica Placement in MoE Training — http://arxiv.org/abs/2608.03676v1
[112] Neural Scaling Laws Rooted in the Data Distribution — http://arxiv.org/abs/2412.07942v1
[116] VLP: A Survey on Vision-Language Pre-training — http://arxiv.org/abs/2202.09061v4
[117] Image Segmentation in Foundation Model Era: A Survey — http://arxiv.org/abs/2408.12957v3
[118] ME-VLM: A Unified VLM for Embodied Cognition and Agent Coordination — http://arxiv.org/abs/2609.24526v2
[119] Vision-and-Language Navigation Today and Tomorrow: A Survey in the Era of Foundation Models — http://arxiv.org/abs/2407.07035v2
[120] Hierarchical Pre-Training of Vision Encoders with Large Language Model — http://arxiv.org/abs/2604.00086v2
[

---

*Generated by research-bot · topic=`ai` · depth=`standard` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading · model=`deepseek-v4-flash` · sources=132 · duration=356s · 2026-10-04T22:08:36+00:00*
