# 具身智能与视觉-语言-动作（VLA）前沿快照（2024–2026）

**日期**：2026-10-12（UTC）｜**领域**：具身智能 / VLA（Vision-Language-Action）｜**检索源数量**：31 条可引用来源（其中与本主题直接相关 20 条；11 条经标题判定与 VLA/具身智能无关，已剔除且全文不再引用）

**证据基线说明（务必先读）**
- 本批可引用来源**全部为 arXiv 预印本记录或 IEEE DOI 记录**，无一篇标注同行评审 venue 字段；因此下文凡涉及「权威证据」，均只能写「预印本/DOI，评审状态 `> 待核实`」。
- 本批候选块**普遍缺失引用数（citations）、GitHub star、下载量、榜单排名**等热度字段。按方法论要求，热度证据一律标注 `> 待核实`，**不编造任何数字**。
- 仅有标题、无摘要内容的来源为 [9][10][11][12][27][28][29][30][31]，下文凡引用这些条目，均明确标注「仅标题可用」。
- 本批证据**完全未覆盖** RT-1、Diffusion Policy、ACT、π0、Open X-Embodiment、DROID、LIBERO、SimplerEnv 等公认奠基工作与基准（其名仅出现在 q3「开放问题」的举例中，无独立来源支撑）→ `> 待核实`，需另行检索补充。

---

## 1. 进展与热点（Progress & Hotspots）

**一句话增量判断**：相对 2023–2024 年「端到端 VLA 能否 work」的基线，2025–2026 年的增量集中在**推理期（inference-time）干预与效率**、**VLA 的智能体化（tool-use / 图像思维链）**、**开源权重与数据开放**三条线上，但**几乎没有一条获得独立第三方复现**。

### 1.1 推理期可控性与可解释性（新分支）

- **推理时注意力引导**（2026-08）：[2] 在 Alpamayo-R1 的 Qwen3-VL 骨干上，对检测器定位的交通参与者视觉 token 施加**有界加性 pre-softmax 注意力偏置**，以 fail-open forward pre-hook 实现、**不改动任何权重**；在 Physical AI World Model Synthetic dataset 的 50 个车道变换场景上，轨迹解码器随偏置幅度呈单调剂量响应，平均位移约 17 cm、钳位处横向位移最高约 140 cm；层消融显示动作相关信号位于较后层。
  - 热度：`> 待核实`（候选块无引用数/star/榜单）[2]；权威：arXiv:2608.17095v1（cs.CV）预印本，评审状态 `> 待核实`[2]；关注度：**低—中**（依据：仅凭「免重训练即可干预安全关键行为」这一痛点推测话题性，无量化热度信号）[2]；推荐度：**★★★☆☆**——可控性/安全可干预思路新，但仅 50 个**合成**场景、非真机，外推需谨慎 [2]。
- **VLA 内部注意力头即可做路径偏差检测**（2026-03）：[15] 主张 VLA 在导航任务中本就具备可用于路径偏差检测的注意力头，从而**免去训练外部检测模块**；摘要指出 VLA 受视觉推理幻觉导致的轨迹偏差困扰。
  - 热度：`> 待核实`[15]；权威：arXiv:2603.13782v1（cs.RO）预印本，评审状态 `> 待核实`[15]；关注度：**低**（无引用/star/榜单信号）[15]；推荐度：**★★★☆☆**——挑战「必须外挂检测器」的既有做法，属可解释性与失效监控方向，但候选摘要未给量化指标，需读全文核实 [15]。

### 1.2 智能体化：VLA + 工具调用 / 推理链

- **ART（Agentic Robot with Tool-use，2026）**：[4] 提出 tool-injection 框架，把任意 VLA 模型调优为可调用现成工具模块的智能体，覆盖低层视觉、高层 affordance 与本体增强；标题即包含 "Evolve … into an Agent with On-the-fly Tool-use"，且已更新至 v3。
  - 热度：`> 待核实`[4]；权威：arXiv:2608.14047v3（cs.RO）预印本，评审状态 `> 待核实`[4]；关注度：**低—中**（依据：v1→v3 的多次迭代可作作者持续投入的弱信号，但无引用/star 数据）[4]；推荐度：**★★★★☆**——「VLA agent 化」是 2026 年较清晰的新叙事，与端到端单模型路线形成对照 [4]。
- **VLA-Thinker（2026-03）**：[28] 标题显示其以 "Thinking-with-Image reasoning" 提升 VLA。**仅标题可用，摘要未提供** → 方法细节与结果 `> 待核实`[28]。
  - 热度：`> 待核实`[28]；权威：arXiv:2603.14523v1 预印本，评审状态 `> 待核实`[28]；关注度：`> 待核实`[28]；推荐度：**★★★☆☆**——线索价值高（推理链 × 具身），但当前证据仅到标题级 [28]。

### 1.3 训练范式：世界模型奖励、分层对齐、多模态联合

- **IRL-VLA（2026）**：[10] 标题显示其「通过奖励世界模型（Reward World Model）进行 VLA 训练」，DOI 指向 CVPRF 2026。**仅标题+DOI 可用** → 方法细节 `> 待核实`[10]。
  - 热度：`> 待核实`[10]；权威：IEEE DOI 10.1109/cvprf71909.2026.00098，是否同行评审、属主会或 workshop `> 待核实`[10]；关注度：`> 待核实`[10]；推荐度：**★★★☆☆**——「世界模型 + RL 训练 VLA」是相对模仿学习的少数派路线，值得跟读 [10]。
- **分层 VLA 的显式语言—动作对齐**：[11] 标题显示其「通过显式 Language-Action Alignment 支撑层级 VLA」。**仅标题可用** → `> 待核实`[11]。热度 `> 待核实`；权威：IEEE DOI 10.1109/cvprf71909.2026.00889，评审状态 `> 待核实`[11]；关注度 `> 待核实`[11]；推荐度 **★★★☆☆**。
- **A₁：从 affordance 到 action 的自适应截断 VLA**：[9] 标题显示「Adaptive Truncated VLA」，DOI 同属 CVPRF 2026。**仅标题可用** → `> 待核实`[9]。热度 `> 待核实`；权威：IEEE DOI 10.1109/cvprf71909.2026.00149，评审状态 `> 待核实`[9]；关注度 `> 待核实`[9]；推荐度 **★★★☆☆**——「自适应截断」暗示推理深度按需分配，与效率主线呼应 [9]。
- **运动图像扩散联合学习**：[27] 标题显示「Robotic VLA Benefits from Joint Learning with Motion Image Diffusion」。**仅标题可用** → `> 待核实`[27]。热度 `> 待核实`；权威：arXiv:2512.18007v1 预印本，评审状态 `> 待核实`[27]；关注度 `> 待核实`[27]；推荐度 **★★★☆☆**。

### 1.4 推理效率与实时性（部署侧最硬的一类增量）

- **Running VLAs at Real-time Speed（2025-10-30）**：[24] 声称在**单张消费级 GPU** 上以 **30 Hz 帧率、最高 480 Hz 轨迹频率**运行 pi0 级多视角 VLA，使此前被认为大 VLA 无法承担的动态实时任务成为可能，并报告了真实世界实验。
  - 热度：`> 待核实`（候选块无引用数/star/榜单）[24]；权威：arXiv:2510.26742v1（cs.RO）预印本，评审状态 `> 待核实`[24]；关注度：**低—中**（依据：直接回应「大 VLA 能否实时」这一社区焦点，但无热度数据支撑）[24]；推荐度：**★★★★☆**——本批证据中真机部署门槛信息密度最高的一条，**但结论为作者自评，未见独立复现**，引用时必须加限定词 [24]。
- **BLURR（2025-12）**：[8] 被描述为轻量级推理 wrapper，可插入现有 VLA 控制器而**无需重训练或改动 checkpoint**，针对 VLA 推理栈在响应式 web demo 与消费级 GPU 高频机器人控制中过重的问题，实例化载体为 pi-zero 控制器。
  - 热度：`> 待核实`[8]；权威：arXiv:2512.11769v1（cs.RO）预印本，评审状态 `> 待核实`[8]；关注度：**低**（无引用/star/榜单信号）[8]；推荐度：**★★★☆☆**——「不改权重、可插拔降本」工程价值明确，但**候选块未给延迟/吞吐量化指标**，收益 `> 待核实`[8]。
- **VLA-Adapter（v1 2025-09-11 / v2 2025-09-22）**：[23] 研究如何高效地把视觉-语言（VL）表征桥接到动作（A），以减少对大规模 VLM 机器人数据预训练的依赖，目标是小规模（tiny-scale）VLA 范式。
  - 热度：`> 待核实`[23]；权威：arXiv:2509.09372v2（cs.RO）预印本（16 人作者团队），评审状态 `> 待核实`[23]；关注度：**低**（无引用/star/榜单；仅 v1→v2 两周内更新为弱活跃信号）[23]；推荐度：**★★★☆☆**——直击训练成本，但**代码/权重开放状态在候选证据中未确认** [23]。

### 1.5 竞赛与垂直落地

- **BEHAVIOR Challenge 2025 冠军方案（2025-12）**：[5] 题目为 "Task adaptation of Vision-Language-Action model: 1st Place Solution"，是目前本批证据中**唯一带明确第三方竞赛名次**的条目，属相对可信的「榜单级」证据。
  - 热度：`> 待核实`（候选块无榜单规模/队伍数/引用数）[5]；权威：arXiv:2512.06951v2 预印本 + 竞赛名次，评审状态 `> 待核实`[5]；关注度：**中**（依据：竞赛冠军身份本身构成社区关注信号）[5]；推荐度：**★★★★☆**——竞赛名次是可核实的外部锚点，建议优先精读核实其评测口径与硬件 [5]。
- **电力操作机器人 VLA（2026）**：[12] 标题显示面向电力行业操作机器人的 VLA。**仅标题可用** → `> 待核实`[12]。热度 `> 待核实`；权威：DOI 10.22541/authorea.15004596/v1（Authorea 预印本平台），评审状态 `> 待核实`[12]；关注度：`> 待核实`[12]；推荐度 **★★★☆☆**——垂直行业落地样本，但载体为预印本平台，可信度低于会议论文 [12]。
- **LingBot-VLA 2.0（2026-07-07）**：[26] 明确指出现有 VLA 基础模型虽近期有进展，但**实验室条件与真实应用之间的差距**仍阻碍落地；相对 LingBot-VLA 的改进含跨任务/跨本体泛化与数据改造（候选摘要截断，后续改进点未知）。
  - 热度：`> 待核实`[26]；权威：arXiv:2607.06403v1（cs.RO）预印本，评审状态 `> 待核实`[26]；关注度：**低**（无引用/star/榜单，且候选片段信息不完整）[26]；推荐度：**★★★☆☆**——时间点最新且直击「落地落差」，但证据不完整，结论需谨慎 [26]。

### 1.6 感知理解侧（非策略闭环）

- **CCFT（2026-07）**：[3] 把装配动作分解为 Verb / Object / Tool 语义元素，用模板化问答对微调 VLM 以获得近乎确定的输出，并提出 Layer-Partitioned Alternating Training（LP-AT）把不同模型层分配给识别特定动作元素，面向人机协作装配的细粒度手-物交互理解。
  - 热度：`> 待核实`[3]；权威：arXiv:2607.10797v1（cs.CV）预印本，评审状态 `> 待核实`[3]；关注度：**低**（无引用/star/榜单）[3]；推荐度：**★★★☆☆**——属**动作理解**而非具身策略闭环，与 VLA 控制主线为邻接关系 [3]。

### 1.7 入门/教学材料

- **Robot Learning: A Tutorial（2025-10）**：[30] 为综述/教程性质材料，适合作为领域骨架。**仅标题可用**，覆盖范围 `> 待核实`[30]。热度 `> 待核实`；权威：arXiv:2510.12403v1 预印本，评审状态 `> 待核实`[30]；关注度 `> 待核实`[30]；推荐度 **★★★☆☆**。

> **本批证据中最重要的一条元结论**：VLA 领域 2025–2026 的方法新增量几乎全部以**作者自评 + 小型合成或单一硬件设置**呈现；仅 [5] 带有竞赛名次这一外部锚点，其余**均无第三方复现或公开榜单背书** [2][3][4][8][15][21][23][24][26]。这本身是判断该领域「热 vs 实」的关键信号。

---

## 2. 工业界与产品（Industry & Product）

**一句话增量判断**：本批证据中**没有任何厂商产品发布、量产、出货量或客户案例的一手来源**；「从基础模型走向应用」只能通过少数论文标题间接观察，产业化证据链 **显著缺失**。

- **从 lab 到应用的自我定位（2026-07）**：[26] 明确把「实验室条件与真实应用的落差」立为待解问题，并以跨任务/跨本体泛化与数据改造为改进方向——这是本批证据中唯一直接讨论**落地落差**的条目。热度 `> 待核实`；权威：预印本，评审状态 `> 待核实`[26]；关注度 **低**；推荐度 **★★★☆☆**（摘要截断，需补检）[26]。
- **垂直行业产品化样本（2026）**：[12] 面向电力操作机器人，属「VLA 进入特定工业场景」的早期信号；但载体为 Authorea 预印本，**无企业主体、无部署规模、无客户信息** → 产业化程度 `> 待核实`[12]。
- **消费级硬件上的实时推理**：[24] 的 30 Hz / 480 Hz 口径若成立，意味着**部署成本下探到单卡消费级 GPU**，是产业化最关键的一类指标；但为作者自评、未见独立复现 → 商用可行性 `> 待核实`[24]。同类工程化诉求见 [8]（不改权重的推理 wrapper）[8]。
- **开放式基础设施**：[29] 标题为 "LeRobot: An Open-Source Library for End-to-End Robot Learning"（2026-02），属生态型工具链。**仅标题可用**，其维护机构、star 数、发布节奏 `> 待核实`[29]；关注度 `> 待核实`；推荐度 **★★★★☆**（若确为活跃开源库，是复现与入门的关键入口，须核实仓库活跃度）[29]。
- **开源权重与数据的产品化前哨**：[21] 以 "Open Weights and Open Data" 为标题卖点，发布 80,000+ 条精筛自动驾驶 VLA 视频片段；若权重与数据实际可下载，则构成可直接被产业复用的资产 → 实际可获取性 `> 待核实`[21]。

> **缺口声明**：本批证据中**无任何厂商官方博客、发布会、产品页或供应链来源**，故「哪些从 lab 走向落地」「商业化与量产进度」在本周期**无法给出可核查结论** → `> 待核实`。

---

## 3. 蓝海与缺口（Blue Ocean & Gaps）

**一句话增量判断**：真正的无人区不在「再训一个更大的 VLA」，而在**推理期行为控制**、**跨本体泛化的可验证方法**、**统一评测口径**与**失败案例的公开**四处。

1. **推理期行为控制（inference-time control）尚未形成成熟子领域**：[2] 展示免重训练的注意力偏置可单调改变轨迹输出（平均位移约 17 cm，钳位处最高约 140 cm）[2]，[15] 主张内部注意力头可直接用于偏差检测、免去外挂模块 [15]。二者都指向「**不重训练即可监控/纠偏 VLA**」这一空白，但均在少量合成场景或单一控制器上验证，**真机与多任务验证缺失** [2][15]。
2. **跨本体（cross-embodiment）泛化的可验证方法**：[26] 把跨任务/跨本体泛化列为头号改进方向，侧面说明该问题**仍未解决**；本批证据中无任何跨本体定量结果 [26]。
3. **统一评测口径缺失**：q3 的检索结论明确指出，本批来源**无法在同一 benchmark（LIBERO / SimplerEnv / Open X-Embodiment 等）上横向比较**，这些基准名称仅作为举例出现、无独立来源支撑 → `> 待核实`。相对而言，[5] 的 BEHAVIOR Challenge 冠军身份与 [21] 的明确数据规模口径（80,000+ 片段 / 源自 8 个开源数据集的 200 万+ 源片段）是本批中仅有的可对齐锚点 [5][21]。
4. **VLA 智能体化（工具调用、图像思维链）刚起步**：[4] 的 tool-injection 框架与 [28] 的 thinking-with-image 都属新叙事，但均无热度与复现信号 [4][28]。
5. **垂直行业渗透几乎是空白地带**：本批仅 [12]（电力操作机器人）一例 [12]。
6. **负面结果与失败案例完全缺失**：本批全部 20 条相关来源**无一报告失败模式或复现困难**，但这恰恰是「演示 ≠ 验证」的判别关键 → `> 待核实`。
7. **细粒度操作理解与策略闭环之间存在断点**：[3] 做装配动作理解但未验证于机器人策略闭环 [3]。

> **判断**：若以「有热度 + 有真机 + 有第三方复现」三重标准衡量，本批证据中**没有任何一条满足**，因此上述缺口与其说是「无人发现」，不如说是「**已有人试水但尚未被验证**」——这本身就是高杠杆机会所在。

---

## 4. 瓶颈与拐点（Bottleneck & Inflection）

**一句话增量判断**：本周期最清晰的瓶颈是**推理开销/实时性**与**训练算力成本**；是否临近拐点，取决于消费级 GPU 上的实时性声称能否被独立复现。

| 瓶颈 | 证据与口径 | 是否临近拐点 |
|---|---|---|
| 推理开销 / 实时性 | [24] 声称单张消费级 GPU 上 30 Hz 帧率、最高 480 Hz 轨迹频率运行 pi0 级多视角 VLA，并报告真机实验（**作者自评**）[24]；[8] 以不改权重的可插拔 wrapper 降低推理开销，实例化于 pi-zero 控制器，**候选块未给延迟/吞吐数字** [8]；[9] 的「自适应截断」亦属同类思路 [9] | **信号出现但未确认**——若 [24] 的数字被第三方复现，即构成拐点；当前 `> 待核实` |
| 训练算力/数据成本 | [23] 明确以减少「在机器人数据上预训练大规模 VLM」的依赖为目标，走 tiny-scale 路线 [23]；[21] 以「从 8 个开源数据集 200 万+ 片段蒸馏出 8 万+ 片段」降低数据采集成本 [21] | **较大概率是渐进式而非突变** |
| 评测与复现 | 本批仅 [5] 有竞赛名次外部锚点 [5]；其余无榜单、无 star、无下载量 [2][3][4][8][15][21][23][24][26][29] | **仍未突破**——评测缺失是当前最硬的瓶颈 |
| 真机与仿真落差 | [26] 直接把「实验室条件 vs 真实应用」的落差列为核心问题 [26]；[2] 仅 50 个合成场景 [2] | **未临近拐点**，需真机规模数据 |
| 可控性与安全 | [2] 给出剂量响应与层消融，显示「后层承载动作相关信号」这一可复核结构 [2]；[15] 指向内部一致性检测 [15] | **早期**，但方法论上具可证伪性 |

> **拐点信号清单（可观测）**：① 出现引用 [24] 并独立复现其 30 Hz 口径的第三方工作；② 出现同时报告真机 + 多任务 + 跨本体的 VLA 结果；③ 出现公开榜单对 [2][15] 类推理期方法的统一评测。以上三条当前均为 `> 待核实`。

---

## 5. 社会·政策·国际（Society, Policy & Geopolitics）

**一句话增量判断**：**本周期在本批证据中无显著变化**——检索结果中不存在任何监管、标准、地缘政治、供应链或劳动影响类来源。

- 本批 31 条来源均为技术论文/DOI 记录，**无一条**涉及监管文件、国家标准、出口管制、AI 法案或伦理治理议题 → 本维度 `> 待核实`，无法给出可核查结论。
- 可间接挂靠的唯一线索：**垂直行业部署**（[12] 电力操作机器人 [12]）暗示 VLA 正在进入**关键基础设施运维**场景，这类场景通常受行业安全规程约束；但该文为 Authorea 预印本，**未讨论合规、认证或安全标准** → 政策含义 `> 待核实`[12]。
- 另一可观察的结构性信号是**竞赛化治理**：[5] 的 BEHAVIOR Challenge、[7] 的 AAMAS'2026 MOASEI Competition 技术报告，显示具身智能正通过**标准化竞赛**形成事实上的评测规范。[5] 热度 `> 待核实`、权威为竞赛冠军方案预印本 [5]；[7] **仅标题可用**，其与具身智能的关联度 `> 待核实`[7]。
- **国际格局**：本批来源的作者/机构构成（含中英文团队混合）无法从候选块可靠统计 → `> 待核实`。

> 结论：本维度**不编造内容**。若报告需覆盖政策面，必须另行检索监管机构官网、行业标准组织与政府公告。

---

## 6. 资本与生态（Capital & Ecosystem）

**一句话增量判断**：可观察的「生态」增量主要集中在**竞赛生态**与**开源基础设施**两端；**投融资、并购、人才流动类证据为零**。

- **竞赛生态（可核查）**：[5] BEHAVIOR Challenge 2025 冠军方案公开 [5]；[7] AAMAS'2026 第二届 MOASEI 竞赛技术报告（**仅标题可用**，主题关联度 `> 待核实`）[7]。竞赛是当前最可见的「社区聚合器」。热度 `> 待核实`；权威：预印本，评审状态 `> 待核实`[5][7]；关注度 **中**（依据：竞赛名次本身构成外部关注锚点）[5]；推荐度 **★★★★☆**（[5]）／**★★☆☆☆**（[7]，关联待核实）。
- **学术会议生态**：[9][10][11] 三篇均带 IEEE DOI（10.1109/cvprf71909.2026.*），指向 CVPRF 2026 会议论文集，说明 VLA 已成为会议常规轨道。热度 `> 待核实`；权威：IEEE DOI，是否同行评审及主会/workshop 归属 `> 待核实`[9][10][11]；关注度 `> 待核实`；推荐度 **★★★☆☆**。
- **开源基础设施与「开放权重」路线**：[22] OpenVLA（开源 VLA 模型）、[21] Impromptu VLA（宣称开放权重 + 开放数据）、[29] LeRobot（端到端机器人学习开源库）三条构成生态骨架。三条的 **star / 引用 / 下载量全部缺失** → 热度 `> 待核实`[21][22][29]；权威均为预印本，评审状态 `> 待核实`[21][22][29]；关注度 `> 待核实`；推荐度 **★★★★☆—★★★★★**（取决于核实后的仓库活跃度）。
- **社区/公司格局**：本批证据**未提供任何投融资、并购、企业数量或人才流动数据** → `> 待核实`。
- **生态断点**：q3 的检索结论指出，全部四个开源相关来源**均未提供 GitHub 仓库、权重下载页或仿真环境信息**，因此「维护活跃度」与「社区采用度」**无法量化** → 这正是生态评估目前最大的信息空洞。

---

## 7. 信号与预测（Signals & Forecast）

**一句话增量判断**：早期信号指向「**效率与可控性优先于规模**」，但所有预测都必须以可复现性为条件变量。

### 已确证的早期信号
1. 2025Q4–2026Q3 间，围绕「不重训练即可改变/加速 VLA」的工作密集出现：[8]（不改 checkpoint 的推理 wrapper）[8]、[24]（消费级 GPU 实时推理）[24]、[9]（自适应截断）[9]、[2]（注意力偏置干预）[2]、[15]（内部注意力头做检测）[15]。→ **较大概率**代表研究重心从「更大模型」向「更好用模型」偏移。
2. 开放权重与开放数据被明确写进标题作为卖点：[21][22]。→ **较大概率**说明社区对可复现性的诉求已成竞争维度。

### 可证伪假设（`[P]`）

- **[P-1] 置信度：中**。假设：**若到 2027-06 之前出现至少 1 篇独立第三方工作，复现 [24] 的「单张消费级 GPU + 30 Hz 帧率」口径并给出可比数字，则「VLA 实时部署拐点已在 2025Q4 出现」成立；否则该结论应降级为「厂商/作者自评」。** 依据链：当前仅作者自评、无第三方复现 [24] → 推演：实时性是产品化前置条件，社区有强动机复现 → 结论写成上句式可证伪假设。不确定性：候选块无引用数与榜单数据，无法估计复现意愿 `> 待核实`。
- **[P-2] 置信度：中**。假设：**若到 2027-12 前无任何公开榜单（如统一 VLA benchmark）收录 [2][15] 类推理期干预方法的对比结果，则「推理期可控性」将停留在论文层、不进入工程实践。** 依据：两类方法均缺乏统一评测与真机验证 [2][15]，而本批证据显示评测缺失是行业硬瓶颈（见 §4）。
- **[P-3] 置信度：中高**。假设：**若 2027 年前后出现的主流 VLA 论文中，报告「真机 + 多任务 + 跨本体」三项的比例显著上升，则 [26] 所指的「实验室—应用落差」开始收敛；反之说明该落差仍是结构性瓶颈。** 依据：[26] 已将跨任务/跨本体泛化列为头号改进方向 [26]，但本批无任何跨本体定量结果。
- **[P-4] 置信度：低—中**。假设：**若出现被广泛引用的 VLA 智能体化工作（工具调用或图像思维链）并公开评测，则 [4][28] 所代表的 agent 化分支会在 12 个月内成为独立子方向；若无，则该分支被端到端单模型吸收。** 依据：[4] 已迭代至 v3（作者持续投入的弱信号）[4]，[28] 仅有标题 [28]。

### 不确定性与争议
- `[Debated]`「推理期干预是否安全可靠」尚无定论：[2] 自称 fail-open、无权重改动、可剂量控制 [2]；但仅在 50 个合成场景验证，真实长尾风险未知 → 争议点在于**开环干预能否在真实安全关键场景成立**。
- `[R]`「消费级 GPU 可跑 pi0 级 VLA」目前属**单方声称**（[24]），**待证实** [24]。
- `[R]`「[21] 的权重与数据确实可下载」当前仅为**标题承诺**，**待证实** [21]。

### Watchlist（值得持续关注）
1. [24] Running VLAs at Real-time Speed — 是否有第三方复现 [24]
2. [5] BEHAVIOR Challenge 冠军方案 — 唯一带名次的锚点，核实评测口径 [5]
3. [21] Impromptu VLA — 开放权重/数据的实际可获取性 [21]
4. [29] LeRobot — 仓库活跃度与生态采纳度 [29]
5. [4] ART — VLA agent 化分支能否形成独立方向 [4]
6. [2][15] 推理期可控性 — 是否被统一榜单收录 [2][15]

---

## 附：经典与奠基性工作

> **重要限制**：本批证据**未覆盖** RT-1、Diffusion Policy、ACT、π0、Open X-Embodiment、DROID、LIBERO、SimplerEnv 等公认奠基工作与基准（无对应来源）→ `> 待核实`。下表仅列本批来源中可确认存在的经典/基础性条目。

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control | 2023 | arXiv:2307.15818v1 | `> 待核实`（候选块无引用数）[14] | arXiv 预印本，正式发表 venue `> 待核实`[14] | `> 待核实`[14] | ★★★★★ | http://arxiv.org/abs/2307.15818v1 | 将网页知识迁移到机器人控制的 VLA 奠基工作之一，是当前所有 VLA 叙事的起点参照 [14] |
| OpenVLA: An Open-Source Vision-Language-Action Model | 2024 | arXiv:2406.09246v3 | `> 待核实`（无 star/citations）[22] | arXiv 预印本（v3），评审状态 `> 待核实`[22] | `> 待核实`[22] | ★★★★★ | http://arxiv.org/abs/2406.09246v3 | 「开源权重 VLA」路线的关键参照，与 [21] 同属开放路线 [22] |
| One-Shot Reinforcement Learning for Robot Navigation with Interactive Replay | 2017 | arXiv:1711.10137v2 | `> 待核实`[31] | arXiv 预印本，评审状态 `> 待核实`[31] | `> 待核实`[31] | ★★★☆☆ | http://arxiv.org/abs/1711.10137v2 | 具身决策早期脉络（交互式回放的 one-shot 导航 RL），与 VLA 直接关系较弱 [31] |
| Robot Learning: A Tutorial | 2025 | arXiv:2510.12403v1 | `> 待核实`[30] | arXiv 预印本（教程性质），评审状态 `> 待核实`[30] | `> 待核实`[30] | ★★★☆☆ | http://arxiv.org/abs/2510.12403v1 | 入门/教学材料，可用于搭建领域骨架；**仅标题可用**，覆盖范围 `> 待核实`[30] |

---

## 附：开源项目

> **限制**：下表所有条目的 **GitHub star、commit 活跃度、权重可下载性均无候选数据** → 热度一律 `> 待核实`。q3 的检索结论明确指出，四个来源**全部未提供 GitHub 仓库、HuggingFace 权重页或仿真环境信息**。

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| OpenVLA | 2024 | arXiv:2406.09246v3 作者团队 | `> 待核实`[22] | arXiv 预印本，评审状态 `> 待核实`[22] | `> 待核实`[22] | ★★★★★ | http://arxiv.org/abs/2406.09246v3 | 明确以开源 VLA 模型为定位，是复现与二次开发的常见起点 [22] |
| Impromptu VLA | 2025 | arXiv:2505.23757v1（作者含 Hang Zhao、Hao Zhao 等） | `> 待核实`[21] | arXiv 预印本（2025-05-29），评审状态 `> 待核实`[21] | 低（无引用/star/榜单信号）[21] | ★★★★☆ | http://arxiv.org/abs/2505.23757v1 | 标题即承诺 Open Weights + Open Data；数据规模口径明确（80,000+ 片段）[21] |
| VLA-Adapter | 2025 | arXiv:2509.09372v2（16 人团队） | `> 待核实`[23] | arXiv 预印本（v1 2025-09-11 / v2 2025-09-22），评审状态 `> 待核实`[23] | 低（仅 v1→v2 快速更新为弱活跃信号）[23] | ★★★☆☆ | http://arxiv.org/abs/2509.09372v2 | 降低对大规模 VLM 机器人数据预训练的依赖；**代码/权重开放状态未确认** [23] |
| BLURR | 2025 | arXiv:2512.11769v1 | `> 待核实`[8] | arXiv 预印本（cs.RO），评审状态 `> 待核实`[8] | 低（无引用/star/榜单）[8] | ★★★☆☆ | http://arxiv.org/abs/2512.11769v1 | 可插拔推理 wrapper，不改 checkpoint 即降低 VLA 推理开销；**量化收益 `> 待核实`** [8] |
| Running VLAs at Real-time Speed | 2025 | arXiv:2510.26742v1 | `> 待核实`[24] | arXiv 预印本（2025-10-30），评审状态 `> 待核实`[24] | 低—中（回应实时性焦点，无热度数据）[24] | ★★★★☆ | http://arxiv.org/abs/2510.26742v1 | 单卡消费级 GPU + 30 Hz 帧率 / 最高 480 Hz 轨迹频率（**作者自评**）[24] |
| LeRobot | 2026 | arXiv:2602.22818v1 | `> 待核实`[29] | arXiv 预印本，评审状态 `> 待核实`[29] | `> 待核实`（**仅标题可用**）[29] | ★★★★☆ | http://arxiv.org/abs/2602.22818v1 | 端到端机器人学习开源库，若活跃则为核心基础设施；活跃度待核实 [29] |
| LingBot-VLA 2.0 | 2026 | arXiv:2607.06403v1 | `> 待核实`[26] | arXiv 预印本（2026-07-07），评审状态 `> 待核实`[26] | 低（无热度信号，摘要截断）[26] | ★★★☆☆ | http://arxiv.org/abs/2607.06403v1 | 面向跨任务/跨本体泛化与数据改造的落地改进版；候选摘要不完整 [26] |

---

## 附：数据集与基准

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Impromptu VLA Dataset | 2025 | arXiv:2505.23757v1 作者团队 | `> 待核实`（无下载量/引用）[21] | 预印本附带数据集，宣称开放；**独立主页 URL 未给出** `> 待核实`[21] | 低（无下载/榜单/讨论信号）[21] | ★★★☆☆ | http://arxiv.org/abs/2505.23757v1 | 80,000+ 条精筛视频片段，从 8 个开源大规模数据集的 200 万+ 源片段蒸馏；按四类非结构化 corner case 分类，含规划导向 QA 标注与动作轨迹 [21] |
| BEHAVIOR Challenge 2025 | 2025 | arXiv:2512.06951v2（冠军方案） | `> 待核实`（无参赛规模/榜单数据）[5] | 竞赛 + 预印本；挑战赛组织方与评测协议 `> 待核实`[5] | 中（冠军名次本身构成外部关注锚点）[5] | ★★★★☆ | http://arxiv.org/abs/2512.06951v2 | 本批中**唯一带第三方竞赛名次**的锚点，是判断「演示 vs 验证」的关键参照 [5] |
| Physical AI World Model Synthetic dataset | 2026 | 仅见名称，来源方未给出 | `> 待核实`[2] | 候选块未给发布方、许可或是否公开基准 `> 待核实`[2] | 低（无引用/使用度）[2] | ★★☆☆☆ | http://arxiv.org/abs/2608.17095v1 | 被 [2] 用作注意力干预实验的评测来源（50 个车道变换场景）；是否为公开可复现基准 `> 待核实`[2] |

> **基准层缺口**：本批证据**未提供**任何关于 Open X-Embodiment、DROID、LIBERO、SimplerEnv、RoboArena 的可引用来源，q3 结论亦明确指出「缺少对同一 benchmark 的统一对比，无法横向比较各项目的可复现性与性能」→ `> 待核实`，需另行检索。

---

## 参考来源

[1] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1
[2] Inference-Time Attention Steering for Vision-Language-Action Driving Models — http://arxiv.org/abs/2608.17095v1
[3] Compositional Context Fine-Tuning Vision-Language Model for Complex Assembly Action Understanding from Videos — http://arxiv.org/abs/2607.10797v1
[4] Evolve Vision-Language-Action Model into an Agent with On-the-fly Tool-use — http://arxiv.org/abs/2608.14047v3
[5] Task adaptation of Vision-Language-Action model: 1st Place Solution for the 2025 BEHAVIOR Challenge — http://arxiv.org/abs/2512.06951v2
[6] UIC-AIHealth4All at ArchEHR-QA 2026: Answer-First Evidence Grounding for Clinical Question Answering — http://arxiv.org/abs/2608.27467v1
[7] Second MOASEI Competition at AAMAS'2026: A Technical Report — http://arxiv.org/abs/2607.03399v1
[8] BLURR: A Boosted Low-Resource Inference for Vision-Language-Action Models — http://arxiv.org/abs/2512.11769v1
[9] A₁: Adaptive Truncated Vision-Language-Action Model From Affordance to Action — https://doi.org/10.1109/cvprf71909.2026.00149
[10] IRL-VLA: Vision-Language-Action Training via Reward World Model — https://doi.org/10.1109/cvprf71909.2026.00098
[11] Grounding Hierarchical Vision-Language-Action Models Through Explicit Language-Action Alignment — https://doi.org/10.1109/cvprf71909.2026.00889
[12] Vision-Language-Action Model for Electrical Power Operation Robots — https://doi.org/10.22541/authorea.15004596/v1
[13] Overview of AuTexTification at IberLEF 2023: Detection and Attribution of Machine-Generated Text in Multiple Domains — http://arxiv.org/abs/2309.11285v1
[14] RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control — http://arxiv.org/abs/2307.15818v1
[15] Your Vision-Language-Action Model Already Has Attention Heads For Path Deviation Detection — http://arxiv.org/abs/2603.13782v1
[16] Strategies to Harness the Transformers' Potential: UNSL at eRisk 2023 — http://arxiv.org/abs/2310.19970v1
[17] CHC-COMP 2022: Competition Report — http://arxiv.org/abs/2211.12231v1
[18] Team PKU-WICT-MIPL PIC Makeup Temporal Video Grounding Challenge 2022 Technical Report — http://arxiv.org/abs/2207.02687v1
[19] Overview of Dialogue Robot Competition 2022 — http://arxiv.org/abs/2210.12863v1
[20] Motif Mining and Unsupervised Representation Learning for BirdCLEF 2022 — http://arxiv.org/abs/2206.04805v1
[21] Impromptu VLA: Open Weights and Open Data for Driving Vision-Language-Action Models — http://arxiv.org/abs/2505.23757v1
[22] OpenVLA: An Open-Source Vision-Language-Action Model — http://arxiv.org/abs/2406.09246v3
[23] VLA-Adapter: An Effective Paradigm for Tiny-Scale Vision-Language-Action Model — http://arxiv.org/abs/2509.09372v2
[24] Running VLAs at Real-time Speed — http://arxiv.org/abs/2510.26742v1
[25] Open-source tool for Airway Segmentation in Computed Tomography using 2.5D Modified EfficientDet: Contribution to the ATM22 Challenge — http://arxiv.org/abs/2209.15094v2
[26] From Foundation to Application: Improving VLA Models in Practice — http://arxiv.org/abs/2607.06403v1
[27] Robotic VLA Benefits from Joint Learning with Motion Image Diffusion — http://arxiv.org/abs/2512.18007v1
[28] VLA-Thinker: Boosting Vision-Language-Action Models through Thinking-with-Image Reasoning — http://arxiv.org/abs/2603.14523v1
[29] LeRobot: An Open-Source Library for End-to-End Robot Learning — http://arxiv.org/abs/2602.22818v1
[30] Robot Learning: A Tutorial — http://arxiv.org/abs/2510.12403v1
[31] One-Shot Reinforcement Learning for Robot Navigation with Interactive Replay — http://arxiv.org/abs/1711.10137v2

---

*Generated by research-bot · topic=`具身智能与视觉-语言-动作vla前沿` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`deepseek-v4-flash` · sources=31 · duration=238s · 2026-10-12T22:07:01+00:00*
