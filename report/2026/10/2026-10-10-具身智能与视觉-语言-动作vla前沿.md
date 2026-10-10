# 具身智能与视觉-语言-动作（VLA）前沿增量调研报告

> **日期**：2026-10-10（UTC） ｜ **领域**：具身智能 / Vision-Language-Action（VLA）/ Robot Learning ｜ **检索源**：30 条（编号 [1]–[30]，全部为公开 arXiv 预印本、workshop 论文或 DOI 文献）｜ **报告角色**：synthesizer

**阅读须知（证据基线声明）**

本次可用证据集存在严重的**召回噪声与覆盖缺口**，报告据此做了以下降级处理，请勿把本报告的"沉默"读作"领域无进展"：

1. 30 条来源中有相当一部分与 VLA/具身智能**无关**，属检索噪声：短视频参与度预测 [1]、图像超分挑战赛 [3]、肾脏肿瘤分割 [10]、IR 长周期评测 [14]、事件级图像理解 [15]、越南语法律问答 [16]、语音 MOS 挑战 [18]、机器生成文本检测 [4]、车联网计算卸载 [28]、LabVIEW 电机故障诊断 [30]、公共政策可解释机器学习 [26]。这些来源**不构成任何 VLA 论断的证据**。
2. 所有 VLA 相关条目**均为 arXiv 预印本或 workshop 论文**，证据集中**没有任何 benchmark 榜单、第三方复现报告或真机部署白皮书**。因此凡涉及 SOTA 数字、LIBERO / SimplerEnv / RoboArena / Open X-Embodiment / DROID 等基准的具体数值，本报告一律标注 `> 待核实`，**不编造任何数字**。
3. 时间标注规则：来源的"发表时间"由 **arXiv 编号前缀推断**（如 `2608` → 2026-08），此推断已在文中显式声明；无法推断者标 `> 时间待核实`。

---

## 1. 进展与热点（Progress & Hotspots）

**一句话增量判断**：相对 2024–2025 上半年"VLA 能不能做零样本操作"的基线，本周期（2025 H2–2026）的**真实增量不在通用操作 SOTA，而在三条边线——推理实时化、新本体的无示范适配、以及安全/遗忘与驾驶域方法分化**；且这些增量**全部尚未获得独立第三方验证**。

### 1.1 推理效率从"工程细节"升级为独立研究问题

- **BLURR: A Boosted Low-Resource Inference for VLA Models** [8]：提出可插入现有 VLA 控制器的轻量推理包装器，目标场景明确指向"响应式 web 演示"与"商用 GPU 上的高频机器人控制"，直接命中 VLA 的推理栈过重问题。时间：arXiv `2512.11769`（推断 2025-12）。
- **Running VLAs at Real-time Speed** [29]：标题即以"实时速度"为核心命题，时间：arXiv `2510.26742`（推断 2025-10）。
- **增量**：两篇互不引用的工作在同一季度（2025-10 与 2025-12）独立把"VLA 推理延迟"当作一等公民，这是相对 2024 年"VLA 只谈成功率"的明显基线位移。
- 四轴证据：**热度** `> 待核实`（证据集未提供引用数/star）｜**权威** arXiv 预印本（cs.RO），非同行评审 [8][29]｜**关注度** 低–中（预印本阶段，未见榜单或第三方复现引用，`> 待核实`）[8][29]｜**推荐度** ★★★☆☆（若你关心 ROS2 侧实时控制，这两篇是最直接的入口）。

### 1.2 驾驶域 VLA 形成方法分化（注意：不是操作域）

- **Inference-Time Attention Steering for VLA Driving Models** [2]：在 pre-softmax 注意力上施加有界加性偏置，实现**推理期**把注意力重定向到安全关键目标，无需重训练。时间：`2608.17095`（推断 2026-08）。
- **XCoT-VLA: Executable Chain-of-Thought for VLA Driving** [6]：指出自然语言 CoT 对实时控制不友好（开放性、解码成本高、难以优化），转而用**可执行**思维链。时间：`2608.10976`（推断 2026-08）。
- **Your VLA Model Already Has Attention Heads For Path Deviation Detection** [9]：主张路径偏离检测能力已内生于 VLA 的注意力头。时间：`2603.13782`（推断 2026-03）。
- **增量**：2026 年 3–8 月，一个可辨识的"**VLA 驾驶子领域**"正在形成自己的方法论（注意力干预 + 可执行 CoT + 内生可解释性），与操作域 VLA 的技术议程已明显分岔。
- 四轴证据：**热度** `> 待核实`｜**权威** arXiv 预印本（[2] cs.CV、[6] cs.AI、[9] 类别未标注）[2][6][9]｜**关注度** 中（同一子问题在 6 个月内出现 3 篇，属密集但未验证的赛道内讨论）[2][6][9]｜**推荐度** ★★★☆☆（若你的场景含自动驾驶/移动操作，值得读；若纯桌面机械臂，相关性一般）。

### 1.3 新本体的"零示范 / 弱示范"适配

- **RL Bootstrapping of OpenVLA-OFT for a Novel Robot Embodiment** [20]：明确指出现有做法默认需要**本体专属示范**，这对形态与大规模机器人数据集差异很大的自研机器人过于苛刻；该工作研究更难的设定，用 **RL 引导**已预训练的 OpenVLA-OFT 适配新本体。时间：`2608.01013`（推断 2026-08）。
- **增量**：把"跨本体迁移的示范成本"从隐含假设变成显式研究问题，这与后文 §3 的缺口、§4 的数据瓶颈直接呼应。
- 四轴证据：**热度** `> 待核实`｜**权威** arXiv 预印本（cs.RO），非同行评审 [20]｜**关注度** 中（自研机器人团队高频痛点问题，但无榜单信号）[20]｜**推荐度** ★★★★☆（对"C++/ROS2 自研硬件 + 开源 VLA"的实践者相关性最高）。

### 1.4 VLA 的 Agent 化 / 工具调用

- **Evolve Vision-Language-Action Model into an Agent with On-the-fly Tool-use** [19]：把 VLA 演进为可**即时调用工具**的 agent。时间：`2608.14047v3`（推断 2026-08，版本号 v3 表明已迭代三轮）。
- 四轴证据：**热度** `> 待核实`｜**权威** arXiv 预印本，非同行评审 [19]｜**关注度** 中（v3 迭代本身是弱信号，说明作者在持续推）[19]｜**推荐度** ★★★☆☆。

### 1.5 具身安全与机器遗忘（本周期出现的**新主题**）

- **VLA-Forget: Vision-Language-Action Unlearning for Embodied Foundation Models** [12]：把"机器遗忘"引入 VLA 具身基础模型。发表：DOI `10.18653/v1/2026.knowfm-1.5`（ACL 2026 KnowFM workshop，**有同行评审的 workshop 论文**）。
- **增量**：在 2024 年的 VLA 文献中，遗忘/合规几乎不出现；该主题的出现是相对基线的**结构性新变化**（详见 §3、§4）。
- 四轴证据：**热度** `> 待核实`｜**权威** workshop 同行评审（ACL 2026 KnowFM），强于纯预印本 [12]｜**关注度** 中（主题新颖，社区规模尚小）[12]｜**推荐度** ★★★★☆（蓝海方向，见 §3 缺口 3）。

### 1.6 通用/人形基础模型与后训练效率（2025 上半年基线）

- **GR00T N1: An Open Foundation Model for Generalist Humanoid Robots** [22]：自述为面向通用人形机器人的**开放**基础模型。时间：`2503.14734v2`（推断 2025-03）。机构 `> 待核实`（标题仅自述 "Open"）。
- **Fine-Tuning VLA Models: Optimizing Speed and Success** [23]：把"微调速度与成功率"并列为优化目标。时间：`2502.19645v2`（推断 2025-02）。
- **增量**：这两篇构成 2025 年上半年的基线，相对 2023–2024 年"统一动作空间 / 跨本体预训练"的议题，新增的是**开放权重 + 后训练性价比**这两个维度。
- 四轴证据：**热度** `> 待核实`（未取到 star / 下载量）｜**权威** arXiv 预印本，非同行评审 [22][23]；官方模型卡/仓库存在性 `> 待核实`｜**关注度** 中–高（人形+开放基础模型是 2025 年被反复讨论的议题，但本证据集无法给出量化热度）[22][23]｜**推荐度** ★★★★☆（[23] 对实际微调 VLA 有直接操作价值）。

### 1.7 细粒度动作理解与装配（相邻方向）

- **Compositional Context Fine-Tuning (CCFT) VLM for Complex Assembly Action Understanding from Videos** [5]：面向人机协作装配的细粒度手–物交互理解。时间：`2607.10797`（推断 2026-07）。
- 四轴证据：**热度** `> 待核实`｜**权威** arXiv 预印本（cs.CV），非同行评审 [5]｜**关注度** 低–中 [5]｜**推荐度** ★★☆☆☆（与 VLA 控制环相关性间接）。

### 1.8 SOTA 变动的核查结论

- 本次证据集**未能提供任何 benchmark 榜单、成功率数字或跨方法对照表**，因此**无法确认任何"VLA SOTA 被刷新"的论断**。Q1/Q2 子问题中关于"多任务/多本体独立验证 vs 论文自评"的判定：**证据集内 100% 为自评型预印本，独立验证条目数为 0**。
- 上述所有 VLA 相关条目，其"验证状态"一律记为：**仅论文自评，尚无第三方复现证据** `> 待核实`。

---

## 2. 工业界与产品（Industry & Product）

**一句话增量判断**：本周期产业侧的**唯一可信信号是"开源权重 + 开源工具链"在硬件侧同步推进**（人形开放基础模型 [22]、端到端机器人学习开源库 [21]、低资源推理包装器 [8]）；而**量产、真机部署规模、客户案例、商业化收入——本次证据集为零覆盖**。

### 2.1 从 lab 走向落地的可见线索

| 线索 | 时间 | 证据 | 落地性质 | 四轴摘要 |
|---|---|---|---|---|
| 人形通用基础模型以"开放"姿态发布 | 2025-03（`2503.14734v2`） | [22] | 开放权重/开放基础模型（自述） | 权威：预印本非评审 [22]；关注度：中–高；推荐度 ★★★★☆；热度 `> 待核实` |
| 端到端机器人学习开源库 | 2026-02（`2602.22818`） | [21] | 工具链与生态基础设施 | 权威：预印本 [21]；关注度：中–高（摘要提到可负担遥操作系统普及化的行业趋势）；推荐度 ★★★★★（工程落地最关键的一环） |
| 低资源 VLA 推理包装器 | 2025-12（`2512.11769`） | [8] | 面向 web demo / 商用 GPU 的部署层 | 权威：预印本（cs.RO）[8]；推荐度 ★★★☆☆；热度 `> 待核实` |
| VLA 即插即用工具调用 agent | 2026-08（`2608.14047v3`） | [19] | 能力扩展层 | 推荐度 ★★★☆☆ |

- **LeRobot** [21] 摘要明确指出：机器人学习近期的加速由"**可负担的遥操作系统**与数据可获得性提升"驱动——这是本证据集中唯一一条关于"产业供给侧变化"的可核实陈述。
- 四轴：**热度** `> 待核实`（未取到 GitHub star / 下载量）｜**权威** arXiv 预印本，非同行评审；"官方库"属性需以其官方仓库核实 `> 待核实` [21]｜**关注度** 中–高（工具链类工作通常由社区规模驱动，但本证据集无量化信号）[21]｜**推荐度** ★★★★★（若目标是 ROS2 侧复现，这是首查项）。

### 2.2 无法证实的部分（必须显式声明）

- **真机部署规模、量产时间表、客户/订单、订阅或授权模式、价格**：本次证据集**零覆盖** `> 待核实`。
- **企业透明度议题**：*The 2025 Foundation Model Transparency Index* [13] 是第三版年度透明度量化工作，但其评估对象是**通用基础模型开发者**，**不是机器人/VLA 厂商**。将其外推到具身智能产业属过度解读，标 **间接相关** `[13]`。
  - 四轴：**热度** `> 待核实`｜**权威** arXiv（cs.AI）预印本，但其为沿袭性年度项目，前两版方法论连续性 `> 待核实` [13]｜**关注度** 中（治理议题的稳定产物）｜**推荐度** ★★★☆☆（若做合规/采购尽调有用，做技术选型无用）。

---

## 3. 蓝海与缺口（Blue Ocean & Gaps）

**一句话增量判断**：本证据集**暴露出的空白本身就是最有价值的发现**——VLA 的"独立评测层""ROS2 工程层""安全合规层"三块几乎无人认领，而论文层已相当拥挤。

| # | 缺口 / 无人区 | 为何是蓝海 | 现有线索 | 四轴证据 |
|---|---|---|---|---|
| G1 | **独立第三方评测与复现** | 本证据集 30 条来源中，**0 条**为第三方复现或榜单报告；所有 VLA 结论均为自评 | 无 | 热度 `> 待核实`；权威：无来源可引（属"证据缺失"，非"证据为空"）；关注度 高（领域普遍痛点，但本次无可引用来源）`> 待核实`；推荐度 ★★★★★（若做评测工具，杠杆最高） |
| G2 | **ROS2 / 中间件集成层** | **全部 30 条来源中无一条提及 ROS2**；开源库 [21] 是否提供官方 ROS2 接口 `> 待核实` | [21][8] | 权威：无；热度 `> 待核实`；关注度：未知 `> 待核实`；推荐度 ★★★★☆（对 C++/ROS2 工程师是明确机会窗口，但缺口存在性基于"检索未覆盖"，不等于"无人做"）`> 待核实` |
| G3 | **具身模型的安全、遗忘与合规** | 唯一命中该主题的来源仅 1 篇 workshop 论文 [12]，与 VLA 的论文总量严重不匹配 | [12]、外围治理信号 [13] | 权威：ACL 2026 KnowFM workshop（同行评审）[12]；热度 `> 待核实`；关注度 中；推荐度 ★★★★☆ |
| G4 | **无本体专属示范的新硬件适配** | 现有范式默认需要本体示范，自研形态机器人是最大受害者 | [20] | 权威：arXiv 预印本（cs.RO）[20]；关注的量化信号 `> 待核实`；推荐度 ★★★★☆ |
| G5 | **统一的"实时 VLA"系统级口径** | 出现多篇各自表述的实时化工作 [8][29]，但**缺统一延迟/吞吐/成功率口径** | [8][29] | 权威：均为预印本 [8][29]；热度 `> 待核实`；关注度 低–中；推荐度 ★★★☆☆ |
| G6 | **驾驶域 VLA 与操作域 VLA 的方法迁移** | 驾驶域已分化出注意力干预/可执行 CoT [2][6][9]，操作域证据集内未见对应工作 | [2][6][9] vs [20][22][23] | 权威：预印本 [2][6][9]；关注度：未知 `> 待核实`；推荐度 ★★★☆☆ |
| G7 | **人形与机械臂的统一动作空间** | 只有 [22] 一条弱线索 | [22] | `> 待核实`（证据不足以支撑结论） |

- **必须澄清的方法论问题**：上表 G2、G6、G7 的"缺口"部分建立在**"本次检索未覆盖"**之上，属于**检索缺口**，不能等同于**领域空白**。所有此类判断已在表中显式标注 `> 待核实`。

---

## 4. 瓶颈与拐点（Bottleneck & Inflection）

**一句话增量判断**：当前最临近拐点的瓶颈是**推理延迟/算力**（2025 H2 出现专门化论文，属拐点前兆）；最未临近拐点的瓶颈是**评测可信度**（证据集内零进展）。

| 瓶颈 | 类型 | 本周期证据 | 拐点信号 | 是否临近拐点 |
|---|---|---|---|---|
| B1 推理延迟与算力成本 | 算力/工程 | VLA 推理栈"对响应式 web demo 与商用 GPU 高频控制过重" [8]；"以实时速度运行 VLA" 成为独立命题 [29] | 2025-10 与 2025-12 出现两篇**专门针对推理效率**的工作，说明问题已从"隐痛"变为"显学" | **较大概率临近**（依据：论文主题专门化 [8][29]）；热度量化 `> 待核实` |
| B2 本体示范数据依赖 | 数据 | 现有范式假设需要本体专属示范，对形态差异大的自研机器人过于苛刻 [20] | 出现 RL bootstrapping 作为示范替代路线 [20] | **推测临近**（仅 1 条证据，`> 待核实`） |
| B3 评测可信度 | 评测 | 证据集内 **0** 条第三方复现/榜单 | 无 | **未知** `> 待核实` |
| B4 安全与合规成本 | 治理/算法 | 具身遗忘被首次系统化提出 [12]；通用基础模型透明度被年度化量化 [13] | 治理工具（透明度指数）已连续三版 [13]；具身侧对应工具尚未出现 | **推测为早期**（具身侧仅 [12] 一篇）`> 待核实` |
| B5 仿真 SOTA 与真机 SOTA 的可比性 | 评测 | 证据集**零覆盖**；无任何来源区分仿真/真机口径 | 无 | **未知** `> 待核实` |
| B6 ROS2 / 真机集成工程 | 工程/人力 | **零覆盖** | 无 | **未知** `> 待核实` |

- **拐点判定的诚实边界**：上表所有"临近/推测"均基于**证据集中出现的工作主题分布**，而非可观测指标（部署量、榜单变化、融资额）。方法论上，这种推断强度低于挂载可观测指标的推断，请按"较弱的编辑判断"使用。

---

## 5. 社会·政策·国际（Society, Policy & Geopolitics）

**一句话增量判断**：本周期可见的社会维度增量集中在**"透明度治理工具化"**与**"机器人信任/可变自主的持续议题化"**两条线；**监管法规、出口管制、供应链与地缘政治——本次证据集零覆盖，按方法论应写"本周期无显著变化（就本次证据集而言）"，而非编造内容。**

- **透明度治理工具化**：*The 2025 Foundation Model Transparency Index* [13] 为其**第三版年度工作**，说明"对企业透明度进行系统化、可量化评估"已从一次性研究变为**年度化治理基础设施**。
  - 四轴：**热度** `> 待核实`｜**权威** arXiv（cs.AI）预印本；年度项目的方法论延续性待核实 [13]｜**关注度** 中｜**推荐度** ★★★☆☆
  - **重要限定**：其评估对象为通用基础模型开发者，**不是机器人/VLA 厂商**；对具身智能的结构性影响属**待观察** `> 待核实`。
- **机器人信任与人机交互议题**：*TRUST 2025: SCRITA and RTSS @ RO-MAN 2025* [17] 由既有 HRI workshop（SCRITA：人机交互中的信任、接受与社会线索；RTSS：共生社会中的机器人信任）合并而成。
  - **增量**：两个既有 workshop 合并，说明"机器人信任"议题已足够成熟到可以汇聚（学术组织层面的信号，而非技术层面的信号）。
  - 四轴：**热度** `> 待核实`｜**权威** RO-MAN 2025 workshop（同行评审的 workshop 层级）[17]｜**关注度** 中｜**推荐度** ★★★☆☆
- **LLM 参与下的自主权分配**：*Exploring Large Language Models to Facilitate Variable Autonomy for Human-Robot Teaming* [27] 指向"可变自主"——即人与机器人之间动态转移控制权。
  - 四轴：**热度** `> 待核实`｜**权威** arXiv 预印本，非同行评审 [27]｜**关注度** 低–中｜**推荐度** ★★★☆☆（涉及责任归属与劳动影响的接口议题）。
- **监管/标准/地缘/供应链**：**本证据集零覆盖**，本周期**无显著变化可报**（这不是"没有发生"，而是"本次未检索到可引用证据"）。

---

## 6. 资本与生态（Capital & Ecosystem）

**一句话增量判断**：本周期可核实的增量**全部在"开源生态"维度**（开源库、开放权重模型、推理工具、agent 化工具调用），**资本维度（融资、并购、人才流动、公司格局）在本次证据集中零覆盖**。

**生态侧的四条可见线索**

| 生态位 | 代表 | 时间 | 四轴证据 |
|---|---|---|---|
| 端到端机器人学习开源库 | LeRobot [21] | 2026-02（`2602.22818`） | 权威：预印本 [21]；热度 `> 待核实`；关注度 中–高；推荐度 ★★★★★ |
| 开放人形基础模型 | GR00T N1 [22] | 2025-03（`2503.14734v2`） | 权威：预印本自述 "Open"，官方仓库/权重发布状态 `> 待核实` [22]；关注度 中–高；推荐度 ★★★★☆ |
| 推理部署工具链 | BLURR [8] | 2025-12（`2512.11769`） | 权威：预印本（cs.RO）[8]；关注度 低–中；推荐度 ★★★☆☆ |
| 可插拔能力扩展 | On-the-fly Tool-use VLA [19] | 2026-08（`2608.14047v3`） | 权威：预印本 [19]；关注度 中（v3 迭代）；推荐度 ★★★☆☆ |
| 学术社区载体 | TRUST 2025 workshop [17]；KnowFM 2026 workshop 论文 [12] | 2025–2026 | 权威：workshop 同行评审 [12][17]；关注度 低–中 |

- **资本维度的诚实结论**：**投资额、并购、估值、人才流动、公司竞争格局——本次证据集零覆盖** `> 待核实`。任何关于"资本正涌入 VLA"的叙述在本报告证据基线下**无法成立**，故不写。
- **生态结构观察**：证据集呈现"**论文层拥挤、工具层与评测层稀薄**"的倒挂结构——这与 §3 的 G1/G2 缺口一致。

---

## 7. 信号与预测（Signals & Forecast）

### 7.1 本周期观测到的早期信号（带日期与引用）

| # | 信号 | 时间 | 依据 | 强度 |
|---|---|---|---|---|
| S1 | VLA 推理效率成为独立研究命题 | 2025-10 / 2025-12 | [29] / [8] 两篇独立工作，间隔约 2 个月 | 中（主题专门化，但均为预印本，无量化热度） |
| S2 | 出现可辨识的"驾驶域 VLA"方法论簇 | 2026-03 / 2026-08 / 2026-08 | [9]、[2]、[6] 三篇在 6 个月内密集出现 | 中（口径为 arXiv 主题分布） |
| S3 | 具身安全/遗忘作为新主题出现 | 2026（KnowFM workshop） | [12] 唯一命中，属主题首次出现级别 | 弱–中（单篇，但发表于同行评审 workshop） |
| S4 | 跨本体适配的示范依赖被显式问题化 | 2026-08 | [20] | 弱–中（单篇预印本） |
| S5 | 人形开放基础模型 + 端到端开源库构成工具链骨架 | 2025-03 / 2026-02 | [22]、[21] | 中（工具链是生态类信号，但缺 star/下载量等量化支撑 `> 待核实`） |
| S6 | 治理工具年度化（透明度指数第三版） | 2025 | [13] | 中（年度项目连续性），但对机器人厂商为**间接**影响 `> 待核实` |

### 7.2 可证伪预测（[P]）

> 以下均为**可被证伪的假设**，并标注证据链与置信度；未达成即判定不成立。

- **[P1]（置信度：中）** 若到 **2027-06**，出现 **≥2 份由非原作者团队发布的、针对 [8] 或 [29] 类推理优化方法的独立复现或对比评测**，则"**VLA 的竞争轴已从成功率转向吞吐/延迟**"的判断成立；若届时仍只有自评预印本，则本判断证伪。
  - 依据链：S1（2025 H2 出现专门化论文）→ 推演：专门化通常先于标准化评测出现 → 结论。
- **[P2]（置信度：低）** 若到 **2027-12**，主流开源 VLA 工具链（如 [21] 类）发布**官方 ROS2 集成文档或示例**，则"**ROS2 集成是下一段工程瓶颈**"成立；若届时仍无官方支持，则本判断证伪。
  - 不确定性：本判断的前置观察是"**本次 30 条来源中零条提及 ROS2**"，这**可能只是检索覆盖不足**，而非领域真空白。**该假设的可信度因此显著低于 P1。** `> 待核实`
- **[P3]（置信度：中）** 若到 **2027-12**，VLA/具身模型安全或机器遗忘（cf. [12]）累计出现 **≥3 篇同行评审论文或一个专门 workshop**，则"具身安全/合规是蓝海"成立；若仍只有零星预印本，则证伪。
  - 依据链：S3（首篇 workshop 论文出现）→ 推演：合规需求由采购与监管侧倒逼 → 结论。
- **[P4]（置信度：低）** 若到 **2027-06**，出现至少 1 篇把驾驶域注意力干预/可执行 CoT 方法（[2][6]）**迁移并验证于操作域机械臂**的工作，则"两个子领域正在合流"成立；若两域继续各写各的，则证伪。
  - 依据链：S2（驾驶域方法论簇）→ 推演：方法论可迁移性通常由后续跨域工作检验 → 结论。

### 7.3 争议与不确定项（[Debated] / 待核实）

- **[Debated]** 通用基础模型的透明度治理工具（[13]）能否迁移到机器人/VLA 领域？本证据集**无法判定**：支持迁移者会指出治理框架的通用性，反对者会指出机器人涉及物理安全与人身风险，属不同风险类别。**本次证据不足，不作结论** `> 待核实`。
- **[Debated]** 驾驶域 VLA（[2][6][9]）与操作域 VLA（[20][22][23]）是否为同一技术栈的两个应用？本证据集里两域的工作**互不引用**，但"互不引用"也可能是检索分片所致 `> 待核实`。
- **整体不确定性声明**：本报告的"增量"判断建立在 **30 条高度噪声化的 arXiv 召回**之上；证据集中 **0 条独立复现、0 条榜单、0 条真机部署报告**。因此 §1–§7 的所有判断应被读作**"在本次证据基线下最合理的解读"**，而非领域共识。凡涉及数字（引用数、star、成功率、延迟、融资额）的位置，本报告一律以 `> 待核实` 处理，未做任何数值估计。

### 7.4 Watchlist（持续关注）

1. **推理效率条线**：持续跟踪 [8][29] 及其后续引用/复现，判断 P1。`> 热度待核实`
2. **ROS2 与开源库集成**：[21] 官方仓库的 ROS2 支持状态（本次未取到，`> 待核实`），据此判断 P2。
3. **具身安全/遗忘**：[12] 所在的 KnowFM workshop 后续届次的主题分布，据此判断 P3。
4. **跨域迁移**：[2][6][9] 是否被操作域工作引用，据此判断 P4。
5. **独立评测平台**：需另起检索补齐 LIBERO / SimplerEnv / RoboArena / Open X-Embodiment / DROID 的一手来源（本次**全部缺失**，见下表）。

---

## 附录 A：经典与奠基性工作（含证据不足标注）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control | 2023 | `> 待核实` | `> 待核实` | arXiv 预印本；正式发表 venue `> 待核实` [7] | 高（VLA 范式的奠基性引用源；量化依据 `> 待核实`）[7] | ★★★★★ | https://arxiv.org/abs/2307.15818v1 | 将 VLM 的 web 知识迁移到机器人控制，是后续所有 VLA 工作的参照起点 |
| Robot Learning: A Tutorial | 2025 | `> 待核实` | `> 待核实` | arXiv 预印本（cs.RO）[24] | 中（教程类，适合入门）[24] | ★★★☆☆ | https://arxiv.org/abs/2510.12403v1 | 综述/教程性质，可作方法论入门骨架 |
| Exploring Large Language Models to Facilitate Variable Autonomy for Human-Robot Teaming | 2023 | `> 待核实` | `> 待核实` | arXiv 预印本 [27] | 低–中 [27] | ★★★☆☆ | https://arxiv.org/abs/2312.07214v3 | 可变自主与人机团队，属人因/治理侧经典线索 |
| High-level robot programming based on CAD: dealing with unpredictable environments | 2013 | `> 待核实` | `> 待核实` | arXiv 预印本 [25] | 低（年代久远，与 VLA 无直接血缘）[25] | ★★☆☆☆ | https://arxiv.org/abs/1309.2086v1 | 经典机器人编程范式，可作为"前 VLA 时代"对照 |
| Foundation Model Adaptation: From Vision-Language Pretraining to Medical Image Understanding | `> 时间待核实` | `> 待核实` | `> 待核实` | 学位论文（DOI 指向 HKUST 学位库域名）[11] | 低（领域为医学图像，与具身智能相关性间接）[11] | ★★☆☆☆ | https://doi.org/10.14711/thesis-hdl172499 | 仅作"VLM→领域适配"方法论参考 |

> **说明**：本表中 [7] 的引用数、作者机构、正式会议信息，本次证据集均未提供，故一律 `> 待核实`，未做任何数值估计。

## 附录 B：开源项目

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| LeRobot: An Open-Source Library for End-to-End Robot Learning | 2026（`2602.22818`，推断 2026-02） | `> 待核实` | `> 待核实`（未取到 GitHub star / 下载量） | arXiv 预印本（cs.RO），非同行评审；官方仓库状态 `> 待核实` [21] | 中–高（工具链型工作，由社区规模驱动；量化信号缺失）[21] | ★★★★★ | https://arxiv.org/abs/2602.22818v1 | 端到端机器人学习开源库，摘要指出可负担遥操作系统与数据可得性推动了机器人学习加速 |
| GR00T N1: An Open Foundation Model for Generalist Humanoid Robots | 2025（`2503.14734v2`） | `> 待核实` | `> 待核实` | arXiv 预印本；"Open" 为论文自述，权重是否公开 `> 待核实` [22] | 中–高 [22] | ★★★★☆ | https://arxiv.org/abs/2503.14734v2 | 面向通用人形机器人的开放基础模型 |
| OpenVLA-OFT（Fine-Tuning VLA Models: Optimizing Speed and Success） | 2025（`2502.19645v2`） | `> 待核实` | `> 待核实` | arXiv 预印本，非同行评审 [23] | 中–高（被 [20] 用作基座，形成衍生工作链）[20][23] | ★★★★☆ | https://arxiv.org/abs/2502.19645v2 | VLA 微调中"速度 vs 成功率"的联合优化配方 |
| BLURR: A Boosted Low-Resource Inference for Vision-Language-Action Models | 2025（`2512.11769`） | `> 待核实` | `> 待核实` | arXiv 预印本（cs.RO）[8] | 低–中 [8] | ★★★☆☆ | https://arxiv.org/abs/2512.11769v1 | 可插入现有 VLA 控制器的轻量推理包装器 |
| Evolve Vision-Language-Action Model into an Agent with On-the-fly Tool-use | 2026（`2608.14047v3`） | `> 待核实` | `> 待核实` | arXiv 预印本，非同行评审 [19] | 中（v3 版本迭代）[19] | ★★★☆☆ | https://arxiv.org/abs/2608.14047v3 | VLA 的 agent 化与即时工具调用 |

> **诚实提示**：本表所有项目的 **star 数、fork 数、下载量、最近提交时间**均**未在本次证据集中出现**，故 `> 待核实`；不要基于本表做"生态热度"量化结论。

## 附录 C：数据集与基准（**本次证据集严重缺失**）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| LIBERO | — | — | `> 待核实` | **本次证据集中无对应来源** | `> 待核实` | `> 待核实` | `> 待核实` | Q2 题设基准，**未检索到一手来源**，无法描述 |
| SimplerEnv | — | — | `> 待核实` | **本次证据集中无对应来源** | `> 待核实` | `> 待核实` | `> 待核实` | 同上 |
| RoboArena | — | — | `> 待核实` | **本次证据集中无对应来源** | `> 待核实` | `> 待核实` | `> 待核实` | 同上 |
| Open X-Embodiment | — | — | `> 待核实` | **本次证据集中无对应来源** | `> 待核实` | `> 待核实` | `> 待核实` | 同上（[20] 提到"大规模机器人数据集"但未指名） |
| DROID | — | — | `> 待核实` | **本次证据集中无对应来源** | `> 待核实` | `> 待核实` | `> 待核实` | 同上 |

> **结论**：关于"当前 SOTA 在哪些 benchmark、以何口径被测量"，**本次证据集无法回答**。这是本报告最大的覆盖缺口，必须通过新一轮定向检索（arXiv `site:arxiv.org` + 各基准官方主页 + GitHub）补齐后方可下任何 SOTA 判定。

---

## 参考来源

[1] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1
[2] Inference-Time Attention Steering for Vision-Language-Action Driving Models — http://arxiv.org/abs/2608.17095v1
[3] NTIRE 2025 Challenge on Image Super-Resolution (x4): Methods and Results — http://arxiv.org/abs/2504.14582v3
[4] Overview of AuTexTification at IberLEF 2023: Detection and Attribution of Machine-Generated Text in Multiple Domains — http://arxiv.org/abs/2309.11285v1
[5] Compositional Context Fine-Tuning Vision-Language Model for Complex Assembly Action Understanding from Videos — http://arxiv.org/abs/2607.10797v1
[6] XCoT-VLA: Executable Chain-of-Thought for Vision-Language-Action Driving — http://arxiv.org/abs/2608.10976v1
[7] RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control — http://arxiv.org/abs/2307.15818v1
[8] BLURR: A Boosted Low-Resource Inference for Vision-Language-Action Models — http://arxiv.org/abs/2512.11769v1
[9] Your Vision-Language-Action Model Already Has Attention Heads For Path Deviation Detection — http://arxiv.org/abs/2603.13782v1
[10] Automated 3D Segmentation of Kidneys and Tumors in MICCAI KiTS 2023 Challenge — http://arxiv.org/abs/2310.04110v1
[11] Foundation Model Adaptation: From Vision-Language Pretraining to Medical Image Understanding — https://doi.org/10.14711/thesis-hdl172499
[12] VLA-Forget: Vision-Language-Action Unlearning for Embodied Foundation Models — https://doi.org/10.18653/v1/2026.knowfm-1.5
[13] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1
[14] LongEval at CLEF 2025: Longitudinal Evaluation of IR Model Performance — http://arxiv.org/abs/2503.08541v1
[15] Event-Enriched Image Analysis Grand Challenge at ACM Multimedia 2025 — http://arxiv.org/abs/2508.18904v1
[16] VLSP 2025 MLQA-TSR Challenge: Vietnamese Multimodal Legal Question Answering on Traffic Sign Regulation — http://arxiv.org/abs/2510.20381v1
[17] TRUST 2025: SCRITA and RTSS @ RO-MAN 2025 — http://arxiv.org/abs/2509.11402v1
[18] The AudioMOS Challenge 2025 — http://arxiv.org/abs/2509.01336v1
[19] Evolve Vision-Language-Action Model into an Agent with On-the-fly Tool-use — http://arxiv.org/abs/2608.14047v3
[20] RL Bootstrapping of OpenVLA-OFT for a Novel Robot Embodiment — http://arxiv.org/abs/2608.01013v1
[21] LeRobot: An Open-Source Library for End-to-End Robot Learning — http://arxiv.org/abs/2602.22818v1
[22] GR00T N1: An Open Foundation Model for Generalist Humanoid Robots — http://arxiv.org/abs/2503.14734v2
[23] Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success — http://arxiv.org/abs/2502.19645v2
[24] Robot Learning: A Tutorial — http://arxiv.org/abs/2510.12403v1
[25] High-level robot programming based on CAD: dealing with unpredictable environments — http://arxiv.org/abs/1309.2086v1
[26] Explainable Machine Learning for Public Policy: Use Cases, Gaps, and Research Directions — http://arxiv.org/abs/2010.14374v3
[27] Exploring Large Language Models to Facilitate Variable Autonomy for Human-Robot Teaming — http://arxiv.org/abs/2312.07214v3
[28] Real-Time Service Subscription and Adaptive Offloading Control in Vehicular Edge Computing — http://arxiv.org/abs/2512.14002v1
[29] Running VLAs at Real-time Speed — http://arxiv.org/abs/2510.26742v1
[30] Real time state monitoring and fault diagnosis system for motor based on LabVIEW — http://arxiv.org/abs/1806.09998v1

---

*Generated by research-bot · topic=`具身智能与视觉-语言-动作vla前沿` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`deepseek-v4-flash` · sources=30 · duration=184s · 2026-10-10T22:04:46+00:00*
