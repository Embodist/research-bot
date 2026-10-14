# Agent 评测与安全（能力基准、欺骗与可纠正性）——七维增量追踪报告

**日期**：2026-10-14（UTC）
**领域**：LLM Agent / 具身 Agent 的**能力评测基准**（capability benchmarks）与**安全评测**（deception 欺骗、corrigibility 可纠正性、监督与治理）
**检索源数量**：33 条可引用来源（引用编号 [1]–[33]），以 arXiv 预印本为主，另含 3 条 DOI 文献 [20][21][32]
**证据分级口径**：A＝同行评审论文/官方技术报告；B＝arXiv 预印本、官方仓库；C＝第三方复现/公开榜单；D＝社区与二手解读；E＝不可用

> **检索局限声明（影响全文可信度，请先读）**
> ① **召回噪声显著**：[1][2][3][13][15][16] 等与主题无关（多语言主题标引、短视频参与度、图像超分、语音隐私、音频修复、TRIZ 创新）。
> ② **关键缺口**：q2 所问"Agent 欺骗/可纠正性奠基工作"在原始抽取中判定为**零覆盖**；本文仅能借助引用列表中确实存在但未被抽取器命中的 [19] 做有限补充。corrigibility / shutdown resistance / scalable oversight 三个关键词在全池**无任何命中**。
> ③ **热度证据普遍缺失**：全池未提供引用数（citations）、GitHub star、下载量或榜单排名字段，因此各表的"热度"列几乎全为 `> 待核实`；凡标注"关注度"处，依据均为**主题相关性**而非引用数字，不得据此宣称某工作"热门"。
> ④ **多数条目仅精读至标题/摘要**：凡以"标题表明"表述处，正文结论 `> 待核实`。

---

## 1. 进展与热点（Progress & Hotspots）

**一句话增量判断**：近 12–24 个月真正的增量不是"又多了几个 benchmark"，而是三个转移——评测对象从**模型本体**转向 **agent harness（代码脚手架/工具权限/运行生命周期）**；基准形态从**静态快照**转向 **live 与对抗强化**；安全评测从**模型级红队**转向 **agentic 级红队与内部威胁场景**。

### 1.1 基准形态：静态快照 → 活基准与对抗强化
- **SWE-bench Goes Live!** [11]（2025，arXiv:2505.23419）：把已被广泛使用的软件工程基准改造为持续更新的"活"版本，直接回应静态测试集的数据污染与饱和。
  - 热度证据：`> 待核实`（无引用/star/榜单字段）
  - 权威证据：arXiv 预印本（B）；是否已中稿 `> 待核实`
  - 关注度：**中**——依据：SWE-bench 生态是 agent 编码评测的主战场，该工作直接改动主基准形态（主题判断，非引用数据）
  - 推荐度：**★★★★☆**——对"基准本身是否可信"这一核心问题有直接增量
- **SWE-ABS: Adversarial Benchmark Strengthening...** [12]（2026，arXiv:2603.00520）：标题即主张以对抗式强化暴露 test-based benchmark 上**被夸大的成功率**，属"评测效度攻击"类增量。
  - 权威证据：arXiv 预印本（B）｜热度证据：`> 待核实`｜关注度：中｜推荐度：**★★★★☆**（若结论可复现，将直接冲击现有排行榜数字；正文未精读 `> 待核实`）

### 1.2 能力评测：从"单点能力"细化到"知识—执行落差"
- **UI-Evol: Automatic Knowledge Evolving for Computer Use Agents** [4]（2025，arXiv:2505.21964）：摘要给出本池中少见的**量化瓶颈**——即使 90% 知识正确，执行成功率仅 41%，作者称为 knowledge-execution gap。
  - 权威证据：arXiv 预印本（B），cs.HC｜热度证据：`> 待核实`｜关注度：中（computer use agent 是 2025 年热点方向）｜推荐度：**★★★★☆**（唯一带具体落差数字的 grounding 证据）
- **Retrieval Models Aren't Tool-Savvy** [9]（2025，arXiv:2503.01763）：把"**工具检索**"独立基准化，说明 agent 工具使用评测从"会不会调"细化到"找不找得对"。权威（B）｜热度 `> 待核实`｜关注度中｜推荐度 ★★★★☆
- **When Lower Privileges Suffice: Investigating Over-Privileged Tool Selection in LLM Agents** [8]（2026，arXiv:2606.20023）：把"**最小权限**"从运维口号变成可评测指标（over-privileged tool selection）。权威（B）｜热度 `> 待核实`｜关注度中｜推荐度 ★★★★☆（可直接转成产品安全策略）
- **HealthAdminBench** [5]（2026，arXiv:2604.09937）：摘要称医疗行政年支出超 $1 万亿，且此前**不存在**端到端行政工作流的 CUA 基准——典型"空白领域首个基准"。权威（B）｜热度 `> 待核实`｜关注度中｜推荐度 ★★★☆☆
- **ELOQUENT 2025 Sensemaking Task** [7]（2025，arXiv:2507.12143）：把 LLM 同时当作 teacher / student / evaluator，指向长时程"意义建构"任务评测。权威（B）｜热度 `> 待核实`｜关注度低—中｜推荐度 ★★☆☆☆
- **Inspect Robots: Evaluating the Capabilities and Safety of Embodied AI** [23]（2026，arXiv:2610.06306）：面向**具身 AI** 的模块化开源评测框架，摘要明确同时覆盖 capabilities 与 safety。**对本报告读者（具身智能/VLA/ROS2）相关度最高**。权威（B，自述 modular/open）｜热度 `> 待核实`｜关注度：中（具身安全评测稀缺）｜推荐度 **★★★★☆**

### 1.3 安全评测：模型级 → agentic 级
- **Agentic Misalignment: How LLMs Could Be Insider Threats** [19]（2025，arXiv:2510.05179）：把 LLM 置于"**内部人威胁**"场景，是本池中唯一直接对应"欺骗/失准（deception / scheming / misalignment）"的一手实证工作。
  - 热度证据：`> 待核实`
  - 权威证据：arXiv 预印本（B）；**机构归属与作者 `> 待核实`**（来源列表未标注，不得臆断为某实验室）
  - 关注度：**高**——依据：主题直接命中安全社区焦点（**注：为主题判断，非引用数判断**）
  - 推荐度：**★★★★★**——本报告主题核心条目，且是当前证据池中唯一可用的欺骗方向来源
- **Mind the Gap: Comparing Model- vs Agentic-Level Red Teaming with Action-Graph Observability on GPT-OSS-20B** [33]（2025，arXiv:2509.17259）：提出"**评测粒度错配**"这一方法论问题。权威（B）｜热度 `> 待核实`｜关注度中｜推荐度 ★★★★☆
- **EvalSafetyGap** [26]（2026，arXiv:2606.30219v5）：标题表明其给出"LLM 评测—安全失效"的混合综述与概念框架，把**评测失效本身**当作安全问题。权威（B，v5 多轮修订）｜热度 `> 待核实`｜关注度中｜推荐度 ★★★★☆

### 1.4 对齐评测的方法学自我审查
- **Whose Personae? Synthetic Persona Experiments in LLM Research and Pathways to Transparency** [14]（2025，arXiv:2512.00461）：综述 2023–2025 年 **63 篇同行评审研究**，指出合成人格实验普遍存在"任务与目标人群设定不充分"的外部效度缺陷。
  - 权威证据：arXiv 预印本（cs.CY），**同行评审状态 `> 待核实`**；须注意"63 篇同行评审"是其**研究对象属性**，不等于本文已评审
  - 关注度：低—中｜推荐度：**★★☆☆☆**（仅作为"对齐评测易失真"的方法学旁证，不能回答奠基工作）

### 表 A：经典与奠基性工作
| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated LLM Agents | 2024 | `> 待核实` | `> 待核实` | arXiv 预印本（B），评审状态待核实 | 中（间接提示注入已成 agent 标准威胁模型） | ★★★★☆ | http://arxiv.org/abs/2403.02691v3 | 工具集成 agent 的间接提示注入基准，本池中时间最早、最接近"奠基"的安全评测资产 |
| Agentic Misalignment: How LLMs Could Be Insider Threats | 2025 | `> 待核实` | `> 待核实` | arXiv 预印本（B） | 高（主题命中 deception/insider threat） | ★★★★★ | http://arxiv.org/abs/2510.05179v2 | 欺骗/失准行为的场景化实证，用以替代缺失的奠基梳理 |
| Grounding LLM Agents in Knowledge, Context, and Action | `> 待核实` | `> 待核实`（HKUST 学位论文库 DOI） | `> 待核实` | 学位论文（介于 A/B，`> 待核实`） | 低 | ★★☆☆☆ | https://doi.org/10.14711/thesis-hdl172464 | 从 grounding 视角系统整理 agent 的知识/上下文/动作基础 |
| A Comparison and Analysis of LLM Agents within the Context of An LLM-Guided Evolution for Object Detection | `> 待核实` | `> 待核实`（ACM DOI） | `> 待核实` | 会议论文 DOI（`> 待核实` 具体 venue） | 低 | ★★☆☆☆ | https://doi.org/10.1145/3712255.3726669 | 非安全向，仅作 agent 组合方式对比的旁证 |

> **待核实（重大缺口）**：**corrigibility（可纠正性）、shutdown resistance（关停抵抗）、scalable oversight（可扩展监督）的奠基工作在本证据池中完全缺失**，本节无法给出其经典文献清单。需以 `corrigibility` / `shutdown resistance` / `scalable oversight` / `AI control` 为关键词，对 arXiv（cs.AI/cs.CY）与主流对齐团队技术报告做定向补检后再补全本表。

### 表 C：数据集与基准（本池可得）
| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| SWE-bench Goes Live! | 2025 | `> 待核实` | `> 待核实` | arXiv（B） | 中 | ★★★★☆ | http://arxiv.org/abs/2505.23419v2 | 活基准，缓解静态集污染与饱和 |
| SWE-ABS | 2026 | `> 待核实` | `> 待核实` | arXiv（B） | 中 | ★★★★☆ | http://arxiv.org/abs/2603.00520v1 | 对抗强化暴露虚高成功率 |
| HealthAdminBench | 2026 | `> 待核实` | `> 待核实` | arXiv（B） | 中 | ★★★☆☆ | http://arxiv.org/abs/2604.09937v1 | 医疗行政 CUA 端到端基准 |
| HarnessRisk | 2026 | `> 待核实` | `> 待核实` | arXiv（B） | 中 | ★★★★☆ | http://arxiv.org/abs/2608.17597v1 | **生命周期导向的 harness 安全基准** |
| InjecAgent | 2024 | `> 待核实` | `> 待核实` | arXiv（B） | 中 | ★★★★☆ | http://arxiv.org/abs/2403.02691v3 | 间接提示注入基准 |
| EvalSafetyGap | 2026 | `> 待核实` | `> 待核实` | arXiv（B，v5），是否期刊待核实 | 中 | ★★★★☆ | http://arxiv.org/abs/2606.30219v5 | 把评测失效概念化为安全问题 |

---

## 2. 工业界与产品（Industry & Product）

**一句话增量判断**：企业侧关键词从"prompt 原型"变为"**可审计 harness + 契约化输出 + 生产内评测**"；安全能力（最小权限、harness 风险）开始被工程化，但**一手厂商公告/权重发布在本证据池中为零**。

- **从 prompt 到契约**：[24] *From Prompts to Contracts: Harness Engineering for Auditable Enterprise LLM Agents*（2026，arXiv:2607.08028）。摘要明确列出产品化新增需求：**source boundaries、entity routing、answer contracts、reproducible traces**——即"从模型能力到工程契约"。权威（B）｜热度 `> 待核实`｜关注度中｜推荐度 **★★★★☆**
- **harness 自动化与基质化**：[28] **AutoHarness**（2026，arXiv:2603.03329，自动合成 code harness 改进 agent）；[22] **Code as Agent Harness**（2026，arXiv:2605.18747，摘要称 code "no longer only a target output… serves as an operational substrate"）。二者共同说明技术栈把 harness 当作一等公民。权威（B）｜热度 `> 待核实`｜关注度中｜推荐度 ★★★★☆
- **多 agent harness 演化**：[29] **HarnessNet**（2026，arXiv:2610.15221，反馈驱动的层次化联合 harness 演化）。权威（B）｜热度 `> 待核实`｜关注度低—中｜推荐度 ★★★☆☆
- **生产环境评测**：[6] *Efficient Benchmarking in Production: A Study of an Evolving LLM Agent*（2026，arXiv:2609.21267）：针对持续演化 agent 的在线高效评测，直接回应"离线榜单 ≠ 线上表现"。权威（B）｜热度 `> 待核实`｜关注度中｜推荐度 **★★★★☆**
- **权限最小化落地**：[8]（2026）over-privileged tool selection，可直接转成工具白名单/权限分级策略。
- **具身侧可复用资产**：[23] Inspect Robots（2026），自述 modular、open，是最接近"可被产业复用"的具身能力+安全评测框架。
- **产品评测口径变化**：[18] **RecoAtlas**（2026，arXiv:2605.18805）：从 semantic plausibility 走向 **set-level utility**，说明 agent 类产品评测开始看集合级效用而非单点正确率。权威（B）｜热度 `> 待核实`｜关注度低｜推荐度 ★★☆☆☆

### 表 B：开源项目
| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Inspect Robots | 2026 | `> 待核实` | `> 待核实` | arXiv（B），自述 modular/open | 中（具身安全评测稀缺） | ★★★★☆ | http://arxiv.org/abs/2610.06306v1 | 具身 AI 能力+安全评测框架，与 VLA/ROS2 生态最相关 |
| AutoHarness | 2026 | `> 待核实` | `> 待核实` | arXiv（B） | 中 | ★★★★☆ | http://arxiv.org/abs/2603.03329v1 | 自动合成 code harness 以改进 agent |
| HarnessNet | 2026 | `> 待核实` | `> 待核实` | arXiv（B） | 低 | ★★★☆☆ | http://arxiv.org/abs/2610.15221v1 | 多 agent 系统的 harness 联合演化 |

> **待核实**：本证据池**未包含任何厂商官方博客、模型卡、权重发布或产品文档**，也没有 GitHub star / 最近提交数据；因此"工业界落地、真机部署、商业化量产"层面的判断均**缺少一手来源**，本节条目只应视为"工程方法学层面的落地迹象"，而非产品事实。

---

## 3. 蓝海与缺口（Blue Ocean & Gaps）

**一句话增量判断**：**能力侧的 harness 在爆发，harness 安全才刚起步**；而**可纠正性/关停抵抗在证据池中零覆盖**，是最大无人区。

1. **可纠正性与可扩展监督：零覆盖（最高杠杆缺口）**
   q2 明确判定：全池未出现 corrigibility、shutdown resistance、scalable oversight 的实证评测或基准，也没有关停场景实验。欺骗侧唯一的场景化实证是 [19]，但**没有任何反向能力（被信任/可被纠正）的测量工具**。`> 待核实`（可能已有工作未被本次检索召回）。
2. **harness 生命周期安全：供给严重不对称**
   能力侧有 [22][28][29] 三条在造 harness，安全侧仅 [27] **HarnessRisk** 一条生命周期导向基准——典型的"先造能力、后补安全"结构，属新蓝海。
3. **评测的评测（meta-evaluation）**
   [14]（人群/任务设定不足）与 [26]（评测—安全失效框架）从两个方向质疑现有结论可信度；"谁能评测评测者"仍无标准。相关综述也提示 LLM 作为评测者本身存在效度争议 [7][10][17]。
4. **评测粒度错配**
   [33] 显示 model-level 红队结论未必迁移到 agentic 级；缺少统一的 action-graph 级观测规范。
5. **具身 agent 安全评测（与本报告读者最相关）**
   全池仅 [23] 一条（2026-10）。**具身场景下的欺骗与可纠正性**（如机器人拒绝关停、为完成奖励绕过人类指令）在本池中**完全未见**——对具身智能/VLA 社区是明确空白。
6. **攻击面覆盖不全**
   web agent 提示注入 [30]、工具集成注入 [31] 已有；但 MCP 类工具链注入、多 agent 互相注入、长时程记忆投毒在本池缺位 `> 待核实`。
7. **元层缺口（文献计量）**
   本池召回出 [1][2][3][13][15][16] 等无关项，说明"Agent 评测与安全"在通用检索中的**语义边界尚不稳定**，跨社区（NLP/CV/RO/安全）术语未统一——这本身是知识组织层面的缺口。

---

## 4. 瓶颈与拐点（Bottleneck & Inflection）

| # | 瓶颈 | 证据 | 是否临近拐点 |
|---|---|---|---|
| 1 | **知识—执行落差（grounding）** | [4]：90% 正确知识 → 41% 执行成功率 | 未见拐点，仍是硬瓶颈 |
| 2 | **基准污染与饱和** | [11] 活基准；[12] 对抗强化暴露虚高成功率 | **已现拐点信号**：社区从"刷榜"转向"攻击榜单" |
| 3 | **评测成本与不可复现** | [6] 生产内评测；[24] 要求 reproducible traces | 接近拐点：可审计性成为上生产门槛 |
| 4 | **评测效度** | [14] 63 篇研究的系统性设定缺陷；[26] 评测失效框架 | 方法学审查已起步，标准未立 |
| 5 | **观测与归因** | [33] action-graph observability | 无统一规范 |
| 6 | **可纠正性无任何测量工具** | 全池零覆盖（q2） | **拐点尚未到来** |

**拐点判断与信号**：
- "harness"一词在 2026 年密集出现（[22][24][27][28][29] 五条，据 arXiv 编号对应 2026-03 至 2026-10，**月份系编号推断，`> 需以论文页面为准`**），是**术语固化**的典型信号——一个领域正在形成自己的工程词汇，通常预示着工具链与标准化的前夜。
- 最硬瓶颈是**可纠正性缺乏测量**：没有场景库、没有基准、没有红队协议。**若 12 个月内出现 A 级 venue 的公开可纠正性评测套件，即为拐点到来的可观测信号。**

---

## 5. 社会·政策·国际（Society, Policy & Geopolitics）

**一句话增量判断**：本维度**证据严重不足**——仅有一条政策类材料；EU AI Act / NIST 等监管文件在本池中**零覆盖**。

- **开放性与安全的政策张力**：[25] *A Different Approach to AI Safety: Proceedings from the Columbia Convening on Openness in Artificial Intelligence and AI Safety*（arXiv:2506.22183；会议 **2024-11-19 旧金山**，含六周筹备项目）。其核心增量主张是：开放权重/开源基础模型既扩大了安全义务，也重塑了实现安全的机会——**开放性本身被纳入安全治理框架**。权威：arXiv 预印本（B），会议论文集属性 `> 待核实`｜热度 `> 待核实`｜关注度中｜推荐度 **★★★☆☆**
- **具身 AI 被上升为社会议题**：[23] 摘要明确把"理解具身模型的能力与安全"与 societal impact and risks 挂钩，即机器人安全评测从工程问题变为社会问题。
- **合规压力的工程投影**：[24] 的 source boundaries / answer contracts / reproducible traces 与审计、问责类监管要求**结构同构**（此为**本文的分析性推断**，非来源直接主张）。
- **EU AI Act / NIST / ISO**：本证据池**无任何一手条文、指南或合规落地案例** → 无法评估"监管对 Agent 评测的实际落地情况"，`> 待核实`。
- **地缘政治与供应链**：本周期**无显著可核实变化**（无来源，不臆测）。

---

## 6. 资本与生态（Capital & Ecosystem）

**一句话增量判断**：本周期**无显著可核实变化**——证据池中没有任何融资、并购、估值、人才流动或公司格局的一手来源。以下仅为**间接生态信号**，均需补证。

- **术语生态形成**：harness 系工作在同一年集中出现 [22][24][27][28][29]，通常对应工具链与创业团队开始围绕该层布局（[P]，依据见 §7；**属推断，非事实**）。
- **学术培养链条**：出现以 agent grounding 为主题的学位论文 [20]，说明该方向已进入研究生培养层面。热度 `> 待核实`｜推荐度 ★★☆☆☆
- **社区评测赛事常态化**：ELOQUENT 2025 Lab [7]、CheckThat! 2025 [17] 把 LLM-as-evaluator 纳入正式赛道，说明"评测"本身已成为学术社区活动。
- **开源资产极薄**：仅 [23] 具名自述 open/modular；[27][28][31] 等是否有公开仓库 `> 待核实`。
- **`> 待核实`（硬缺口）**：无融资额、无 star、无下载量 → **任何关于"资本流向""公司格局变化"的数量化结论都不应采信**。

---

## 7. 信号与预测（Signals & Forecast）

> 以下均为 **[P] 预测/预判**，写成可证伪假设；置信度为编辑判断，非来源结论。

- **[P1] 可纠正性/关停抵抗将出现首个标准化公开评测套件 —— 置信度：中**
  依据链：欺骗侧已有场景化实证 [19] → 但 corrigibility 全池零覆盖（空白）→ 叠加企业审计与合规需求上升 [24][25] → 预测。
  **证伪条件**：若到 **2027-06** 仍无 A 级 venue 或主流机构发布的公开可纠正性/关停抵抗基准，则本预测不成立。
- **[P2] 活基准与对抗强化将取代静态快照成为默认形态 —— 置信度：中高**
  依据 [11][12]。**证伪条件**：2027 年主流榜单仍以静态数据集为唯一依据，且 SWE-bench Live 类工作未被任何第三方榜单采纳。
- **[P3] 安全评测重心将从 model-level 迁至 harness / agentic 级 —— 置信度：中**
  依据：能力侧 harness 密集 [22][28][29]，安全侧已出现生命周期基准 [27]，且 [33] 证明两级结论不可互推。
  **观测指标**：HarnessRisk 类基准被厂商安全报告或第三方榜单引用。**证伪条件**：2027 年内厂商安全披露仍只给模型级红队结果。
- **[P4] 具身 agent 安全评测将在 12 个月内出现第三方复现或独立榜单 —— 置信度：低—中**
  依据：仅 [23] 一条且为 2026-10 新出，尚未有复现。**证伪条件**：2027-10 前无第三方复现/榜单。
- **[P5] 评测效度（meta-evaluation）将独立成子领域 —— 置信度：中**
  依据：[14] 与 [26] 分别从"设定不足"和"评测—安全失效"两侧切入。**证伪条件**：相关框架未形成持续引用链。

**本期已可观测的早期信号**：
1. **2026 年 harness 词汇固化**（[22][24][27][28][29]）；
2. **评测指标从"分数"转向"可审计轨迹"**（[24] reproducible traces、[33] action-graph observability）；
3. **"最小权限"进入 agent 评测语言**（[8]）。

**Watchlist**：
- Agentic Misalignment [19] 的后续工作与**独立复现**（当前仅单点来源）；
- HarnessRisk [27] 是否被采纳为生命周期安全标准；
- Inspect Robots [23] 是否扩展到具身欺骗/可纠正性场景；
- SWE-ABS [12] 与 SWE-bench Live [11] 的相互验证结果；
- **可纠正性一手工作（当前全池缺失，`> 待核实`，建议列为下一轮检索的第一优先项）**；
- EU AI Act / NIST 对 agent 评测的实际要求（当前零证据，需补检官方法规文本与合规案例）。

---

## 参考来源

[1] Annif at SemEval-2025 Task 5: Traditional XMTC augmented by LLMs — http://arxiv.org/abs/2504.19675v2
[2] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1
[3] NTIRE 2025 Challenge on Image Super-Resolution (x4): Methods and Results — http://arxiv.org/abs/2504.14582v3
[4] UI-Evol: Automatic Knowledge Evolving for Computer Use Agents — http://arxiv.org/abs/2505.21964v2
[5] HealthAdminBench: Evaluating Computer-Use Agents on Healthcare Administration Tasks — http://arxiv.org/abs/2604.09937v1
[6] Efficient Benchmarking in Production: A Study of an Evolving LLM Agent — http://arxiv.org/abs/2609.21267v1
[7] Overview of the Sensemaking Task at the ELOQUENT 2025 Lab: LLMs as Teachers, Students and Evaluators — http://arxiv.org/abs/2507.12143v1
[8] When Lower Privileges Suffice: Investigating Over-Privileged Tool Selection in LLM Agents — http://arxiv.org/abs/2606.20023v2
[9] Retrieval Models Aren't Tool-Savvy: Benchmarking Tool Retrieval for Large Language Models — http://arxiv.org/abs/2503.01763v2
[10] AIn't Nothing But a Survey? Using Large

---

*Generated by research-bot · topic=`agent-评测与安全能力基准欺骗与可纠正性` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`deepseek-v4-flash` · sources=33 · duration=209s · 2026-10-14T22:33:17+00:00*
