# 具身智能·灵巧操作（Dexterous Manipulation & Grasping）深度调研报告

**元信息**：日期 2026-10-05（UTC） | 领域：具身智能 / 灵巧操作与抓取（Dexterous Manipulation & Grasping） | 覆盖方向：模仿学习与扩散/动作分块策略、灵巧手与手内操作（in-hand manipulation）、接触丰富任务与触觉力感知、双臂协同与 sim2real、数据集与基准 | 检索源规模：本轮可引用证据来源 [1]–[110] 共 110 条，覆盖 6 个子问题（q1–q6）的结构化发现，另纳入 3 类人工维护种子资源（论文/项目/数据集） | 证据纪律：所有关键论断带 [n] 引用；无法核实的数字与结论标 `> 待核实`；本轮候选证据存在明显主题偏移，已在正文中显式标注。

---

## 摘要（Executive Summary）

1. **灵巧操作的技术主线已从"抓取检测 + 分模块规划"转向"多模态策略学习 + 动作分块/扩散生成 + 触觉闭环"**。低成本双臂精细操作的学习范式由 ALOHA/ACT 一脉奠定，其奠基论文累计引用 2564 次（Semantic Scholar），至今仍是可复用基线与被改进对象 [93][94]。
2. **in-hand manipulation 的 RL 路线仍在推进**：从单物体重定向系统 [81]、手指级多智能体影子奖励 [84]、约束 RL [88]，到 2026 年新提出的"单手内两刚体装配"任务（纯仿真训练、零样本迁移真机）[83]，任务复杂度显著上升；但 [83] 为单一预印本自述，尚无第三方复现 `> 待核实`。
3. **触觉与力感知已形成独立子生态**：视觉触觉仿真（GelSight 类图像生成 [103]、复杂形貌光学触觉传感器仿真 [105]）、触觉预训练 [96]、视触觉灵巧操作 [97][110]、触觉皮肤剪切/法向力 [106]、触觉反馈 RL [109]，并有专门基准 ManiFeel [100] 与 ManiSkill-ViTac 2025 挑战赛 [95]、世界模型表示研究 ContactWorld [102]。**但"触觉是否被主流 VLA 策略用于真机闭环"在本轮证据中未获直接证据** `> 待核实`。
4. **双臂协同出现多个可复用结构与基准**：ALOHA 2 [17]、Mobile ALOHA [18]、InterACT 层级注意力动作分块 [65]、RoboTwin 双臂协作挑战赛 [66]、DAIR 解耦注意力正则 [67]、Stabilize to Act [69]、VoxAct-B [71]。
5. **数据集与基准层面存在两处显著风险**：(a) 本轮候选证据**完全未覆盖** Open X-Embodiment、DROID、RoboMimic、SimplerEnv、RoboArena、Adroit/DexArt 之外的多数基准细节对比，仅取得 Open X-Embodiment [31]、DROID [33]、DexArt [43] 的论文链接；(b) LIBERO 生态正被衍生出语言泛化 [35] 与闭环视觉鲁棒性 [36] 两类诊断基准，**标准评测分数的可比性假设正被系统性质疑**——指令改写可导致 VLA 性能下降 22–52 个百分点 [35]。
6. **证据偏移警告**：本轮候选中包含大量与具身智能无关的条目（短视频参与度预测 [45]、图像超分挑战 [53]、医学影像数据集 [28]、语音匿名化 [27] 等）。这些条目**不构成灵巧操作领域的证据**，本报告仅在"证据缺口"语境下引用，不做领域结论。
7. **输出侧重**：第八章给出可直接执行的 Watchlist，附每条目的四类证据（热度/权威/关注度/推荐度）。

---

## 一、关键前沿进展（近 1–2 年）

### 1.1 VLA 与统一灵巧手操作

- **UniHM: Unified Dexterous Hand Manipulation with Vision Language Model**（2026，arXiv 预印本）[73]：提出以开放词汇指令的"组合式引导"替代纯物体中心线索或精确手-物交互序列，用于规划物理可行的灵巧手操作。
  - **热度证据**：候选块未提供引用数 `> 待核实` [73]
  - **权威证据**：arXiv 预印本（cs.RO），未标注同行评审 venue [73]
  - **关注度**：中 — 依据为 2026 年新发布、主题直击 VLA×灵巧手交叉点，但无引用/star/榜单信号 [73]
  - **推荐度**：★★★☆☆ — 与"VLA 大模型进入灵巧手"主线高度相关，需等待正式发表或第三方复现后再升级判断 [73]
- **Generalist Robot Manipulation beyond Action Labeled Data**（2025）[70]：指出泛化操作的关键瓶颈在于"动作标注数据难以规模化"，尝试突破对动作标注的依赖。
  - **热度证据**：`> 待核实` [70]
  - **权威证据**：arXiv 预印本（cs.RO）[70]
  - **关注度**：中 — 依据为直接命中"数据规模律是否成立"这一开放问题，但无引用数据 [70]
  - **推荐度**：★★★★☆ — 与第五章 sim2real / 数据规模化主题直接相关 [70]

### 1.2 双臂协作基准化

- **RoboTwin Dual-Arm Collaboration Challenge**（CVPR 2025 MEIS Workshop）[66]：将"双臂协作系统的泛化能力评测"从单臂范式分离出来，明确指出现有单臂高性能系统不足以代表协作双臂能力。
  - **热度证据**：`> 待核实` [66]
  - **权威证据**：arXiv 预印本（cs.RO），关联 CVPR 2025 Workshop（非主会全文）[66]
  - **关注度**：中 — 依据为 CVPR workshop 挑战赛形式带来的短期社区聚焦 [66]
  - **推荐度**：★★★★☆ — 双臂协同评测的少数公开基准之一 [66]

### 1.3 具身/长时程任务挑战赛

- **BEHAVIOR Challenge 2025 第一名方案** [74]：面向 VLA 模型的任务自适应，属长时程家庭任务方向的竞赛级证据。
  - **热度证据**：`> 待核实` [74]
  - **权威证据**：arXiv 预印本（cs.RO），竞赛技术报告体裁 [74]
  - **关注度**：中 — 依据为"1st Place Solution"标签与 2025 年时效性 [74]
  - **推荐度**：★★★☆☆ — 对 VLA 任务适配有工程参考，但与灵巧手/触觉联系间接 [74]
- **LabDex: A Hierarchical Benchmark for Dexterous Manipulation in Laboratories**（2026）[11]：指出既有基准**未能同时刻画**多样实验室器具的灵巧操作与长时程、状态依赖的实验流程，定位为分层基准。
  - **热度证据**：`> 待核实` [11]
  - **权威证据**：arXiv 预印本（cs.RO）[11]
  - **关注度**：中 — 依据为填补"灵巧操作 × 长时程 × 实验室场景"交叉空白 [11]
  - **推荐度**：★★★★☆ — 灵巧操作专用基准的新增候选，值得跟踪榜单是否落地 [11]

### 1.4 必须标注的检索偏移

本轮 q1/q5/q6 候选中混入大量非机器人条目：[45]（短视频参与度预测）、[46]（事件级图像理解）、[53]（图像超分 x4）、[52]（HRI 信任 workshop）、[76]（基础模型透明度指数）、[77]（越南语法律问答）、[68]（Ego4D 长时程动作预测）。**这些条目不得作为灵巧操作进展的证据**，仅提示检索召回质量需改进 [45][46][52][53][68][76][77]。

---

## 二、模仿学习与扩散/动作分块策略

### 2.1 动作分块（action chunking）范式的奠基与现状

- **Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware**（RSS 2023，即 ALOHA/ACT 一脉源头）[93]：论证"学习 + 低成本硬件"可胜任穿扎带、插电池等需要精度、接触力协调与闭环视觉反馈的任务。
  - **热度证据**：citations=2564（Semantic Scholar）[93]
  - **权威证据**：Robotics: Science and Systems Conference（RSS），同行评审机器人顶会 [93]
  - **关注度**：高 — 依据为 2564 次引用，是本方向被引最高的奠基成果之一 [93]
  - **推荐度**：★★★★★ — 动作分块模仿学习必读源头论文，权威、热度、相关性三者兼备 [93]
- **ACT 作为可复用基线**：2025 年出现以 ACT 为改进对象的嵌入式版本（DPB-Embedded ACT），指出模仿学习累积误差、多模态信息融合、传感器空间感知仍是挑战 [94]。
  - **热度证据**：citations=0（Semantic Scholar）[94]
  - **权威证据**：Applied and Computational Engineering（非机器人顶会/顶刊）[94]
  - **关注度**：低 — 依据为零引用、非权威 venue [94]
  - **推荐度**：★★☆☆☆ — 仅作"ACT 已成为通用基线"的旁证，ACT 真实架构与真机成功率口径须回到原文核实 [93] `> 待核实` [94]

### 2.2 扩散/生成式策略在灵巧操作中的扩散

- **Dexterous Functional Pre-Grasp Manipulation with Diffusion Policy** [63]：标题即表明将扩散策略用于灵巧的功能性抓取前操作（pre-grasp manipulation）。
  - **热度证据**：`> 待核实` [63]
  - **权威证据**：arXiv 预印本 [63]
  - **关注度**：中 — 依据为"扩散策略 × 灵巧手"交叉点，但本轮未取得引用/star 数据 [63]
  - **推荐度**：★★★★☆ — 与第二章与第三章交叉主题直接相关 [63]
- **扩散策略奠基工作（Diffusion Policy: Visuomotor Policy Learning via Action Diffusion, RSS 2023）**：来自种子资源，链接 https://arxiv.org/abs/2303.04137 。
  - **热度证据**：`> 待核实`（本报告未取得可核查的引用数来源）
  - **权威证据**：种子资源标注为 RSS，但**本轮检索未取回该文的一手页面**，故同行评审状态 `> 待核实`
  - **关注度**：高 — 依据为"扩散策略"已成为具身策略生成的主流命名范式，本轮多项 2024–2026 工作（如 [63]）在标题层面即体现该范式延续 [63]
  - **推荐度**：★★★★★ — 该方向的方法论起点，建议以原文与官方实现为准补全证据

### 2.3 模仿学习的方法演进（种子块外的一手线索）

本轮取回多条模仿学习/技能学习的一手论文链接，可作为脉络补全的入口：单演示由粗到精模仿 [55]、收敛监督者的 on-policy 模仿 [56]、元学习一次性视觉模仿 [57]、单相机遥操作驱动的多手灵巧模仿 [59]、异质人类演示的偏好与表征学习 [61]、基于先验数据的技能级模仿 [62]、长时程"规划+模仿+RL"协同 SPIRE [60]、层级感知逆强化学习 [89]。
- **热度证据**：以上各条 `> 待核实`（候选块未提供引用数）
- **权威证据**：均为 arXiv 预印本，本轮未取回 venue 字段
- **关注度**：低–中 — 依据为缺少引用/榜单信号，仅能凭标题判断主题相关性
- **推荐度**：★★★☆☆ 起的跟踪清单，其中 [59]（灵巧手 × 模仿学习 × 单相机遥操作）与本题相关度最高

---

## 三、灵巧手与手内操作

### 3.1 手内操作（in-hand manipulation）最新进展

| 工作 | 时间 | 关键点 | 四类证据 |
|---|---|---|---|
| **Assembling Two Parts in One Hand** [83] | 2026-09 预印本 | 单只灵巧手内配合两个刚体完成装配，无第二臂、无夹具；RL 由两部件目标相对位姿驱动，函数式辅助奖励塑造手指协同，域随机化 + 历史本体感知/物体观测融合抗遮挡；同一配方覆盖 Bottle/Syringe/Marker 三任务，纯仿真训练零样本迁移真机 | 热度：`> 待核实`；权威：arXiv 预印本 cs.RO，无同行评审记录；关注度：中（2026-09 新预印本，主题稀缺）；推荐度：★★★☆☆ — 前沿跟踪价值高，真机与复现细节待核实 [83] |
| **Rapid Learning of Dexterous In-Hand Pen Writing through Real-Time Jacobian Estimation** [14] | 2026 | 以实时雅可比估计实现手内书写，摘要指出"手内操作仍是未解前沿"，接触丰富与高动态使建模/数据采集成本高 | 热度：`> 待核实`；权威：arXiv 预印本 cs.RO；关注度：中（目标新颖：书写）；推荐度：★★★★☆ — 与"接触丰富 + 手内"主线强相关 [14] |
| **Stable In-hand Manipulation with Finger Specific Multi-agent Shadow Reward** [84] | 2023 | 手指级多智能体影子奖励 | 热度：`> 待核实`；权威：arXiv 预印本；关注度：中；推荐度：★★★★☆ [84] |
| **A System for General In-Hand Object Re-Orientation** [81] | 2021 | 通用手内物体重定向系统 | 热度：`> 待核实`；权威：arXiv 预印本；关注度：中–高（该问题线的代表性系统之一）；推荐度：★★★★★ — in-hand re-orientation 必读线索 [81] |
| **Constrained RL for Dexterous Manipulation** [88] | 2023 | 带约束的灵巧操作 RL | 热度：`> 待核实`；权威：arXiv 预印本；关注度：中；推荐度：★★★☆☆ [88] |

- **说明**：结构化发现明确指出，本轮候选**未覆盖** OpenAI Dactyl、DextrAH、Visual Dexterity 的一手细节（任务设置、硬件、指标）`> 待核实`（见 [85][86][87] 均为通用 RL 平台/算法，与灵巧操作里程碑无直接关联）。**注意**：可引用来源 [2]《Learning Dexterous In-Hand Manipulation》与 [3]《Learning Complex Dexterous Manipulation with Deep RL and Demonstrations》即该一脉的关键原始入口，建议以原文补全。

### 3.2 手硬件与开源手

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| **LEAP Hand** [13] | 2023 | 学术团队（arXiv cs.RO） | `> 待核实` | arXiv 预印本 | 中 — 依据为被广泛用作低成本拟人手选型 | ★★★★☆ 低成本拟人手做 robot learning 的主流选项 | http://arxiv.org/abs/2309.06440v1 |
| **GelSight Svelte Hand** [104] | 2023 | 学术团队 | `> 待核实` | arXiv 预印本 | 中 — 三指两自由度、触觉丰富、低成本 | ★★★★☆ 触觉手硬件与低成本路线参考 | http://arxiv.org/abs/2309.10886v1 |
| **Aero Hand Open** [16] | 2026 | 学术团队 | `> 待核实` | arXiv 预印本 | 中 — 仿真就绪的腱驱手 | ★★★☆☆ 面向仿真到学习的腱驱手 | http://arxiv.org/abs/2608.28578v2 |

- **GraspNet / AnyGrasp / 接触点表示**：**本轮候选证据完全未覆盖**，需补充检索后作答 `> 待核实`（结构化发现 q2 明确记录该缺口）。

### 3.3 灵巧操作的安全与变形体

- **Certifiably Safe Manipulation of Deformable Linear Objects via Joint Shape and Tension Prediction** [99]：指出既有模型只做形状预测、忽略接触与张力约束，可能导致工具与人体损伤，提出形状+张力联合预测的可证明安全方案。
  - 热度：`> 待核实`；权威：arXiv 预印本 cs.RO；关注度：中；推荐度：★★★★☆ — 唯一同时涉及"安全约束 + 接触力"的线缆操作条 [99]

---

## 四、接触丰富任务与触觉/力感知

### 4.1 触觉表征与视触觉策略

| 工作 | 年份 | 关键贡献 | 四类证据 |
|---|---|---|---|
| **ManiFeel** [100] | 2025 | 视触觉操作策略学习的基准与理解性研究：针对视觉受限（狭小空间、暗光）或需精细物体属性/交互感知的任务 | 热度 `> 待核实`；权威 arXiv 预印本 cs.RO；关注度 中–高（少见的视触觉专用基准）；推荐度 ★★★★★ — 触觉策略评测的核心参考 [100] |
| **ContactWorld** [102] | 2026 | 面向接触丰富操作的"视觉-触觉隐世界模型"表示研究，指出视觉与触觉捕获交互的不同侧面，效用取决于表示方式 | 热度 `> 待核实`；权威 arXiv 预印本 cs.RO；关注度 中（世界模型×触觉交叉）；推荐度 ★★★★☆ [102] |
| **ManiSkill-ViTac 2025 挑战赛** [95] | 2024 | 视觉+触觉感知的操作技能学习挑战赛 | 热度 `> 待核实`；权威 arXiv 预印本（challenge 综述）；关注度 中–高（有挑战赛形式）；推荐度 ★★★★☆ — 触觉赛题与基线入口 [95] |
| **VITaL Pretraining** [96] | 2024 | 视触觉预训练，同时服务触觉与非触觉操作策略 | 热度 `> 待核实`；权威 arXiv 预印本；关注度 中；推荐度 ★★★★☆ [96] |
| **Robot Synesthesia** [97] | 2023 | 视触觉感知下的手内操作 | 热度 `> 待核实`；权威 arXiv 预印本；关注度 中–高；推荐度 ★★★★☆ [97] |
| **3D-ViTac** [110] | 2024 | 视触觉精细操作 | 热度 `> 待核实`；权威 arXiv 预印本；关注度 中；推荐度 ★★★★☆ [110] |
| **Learning In-Hand Translation Using Tactile Skin with Shear and Normal Force Sensing** [106] | 2024 | 触觉皮肤同时感知剪切力与法向力，用于手内平移 | 热度 `> 待核实`；权威 arXiv 预印本；关注度 中；推荐度 ★★★★☆ [106] |
| **Tac2Motion** [109] | 2025 | 接触感知 RL + 触觉反馈用于机械手操作 | 热度 `> 待核实`；权威 arXiv 预印本；关注度 中；推荐度 ★★★★☆ [109] |
| **TransDex** [8] | 2026 | 面向透明物体的视触觉融合策略 + 点云重建预训练，针对自遮挡、深度噪声与透明物深度丢失 | 热度 `> 待核实`；权威 arXiv 预印本 cs.RO；关注度 中（透明物难题）；推荐度 ★★★★☆ [8] |

### 4.2 触觉仿真与 sim2real

- **Generation of GelSight Tactile Images for Sim2Real Learning** [103]：为 sim2real 学习生成 GelSight 触觉图像。
  - 热度 `> 待核实`；权威 arXiv 预印本；关注度 中；推荐度 ★★★★☆ — 触觉 sim2real 的早期关键条 [103]
- **Beyond Flat GelSight Sensors** [105]：指出平面 GelSight 的局限，仿真复杂形貌光学触觉传感器以支持 sim2real。
  - 热度 `> 待核实`；权威 arXiv 预印本；关注度 中；推荐度 ★★★★☆ [105]
- **关键判断**：**"触觉是否已被主流 VLA/扩散策略真正用于真机闭环"在本轮证据中无法证实** `> 待核实`。现有证据只能说明触觉在独立子生态（基准 [100]、挑战赛 [95]、预训练 [96]、RL [109]）中活跃，缺少"触觉 × 主流 VLA 真机闭环"的一手证据。

### 4.3 接触丰富操作的经典线

- **Learning Contact-Rich Manipulation Skills with Guided Policy Search** [101]（2015）：接触丰富操作技能学习的早期代表。
  - 热度 `> 待核实`；权威 arXiv 预印本（该工作历史地位显著，但本轮未取得 venue/引用字段）；关注度 中（历史奠基意义）；推荐度 ★★★★★ — 接触丰富操作的方法论源头之一 [101]

---

## 五、双臂协同与 sim2real

### 5.1 双臂协同

| 工作 | 年份 | 关键点 | 四类证据 |
|---|---|---|---|
| **ALOHA 2** [17] | 2024 | 低成本双臂遥操作硬件增强版 | 热度 `> 待核实`；权威 arXiv 预印本；关注度 中–高（ALOHA 生态延续）；推荐度 ★★★★☆ [17] |
| **Mobile ALOHA** [18] | 2024 | 低成本全身遥操作实现双臂移动操作 | 热度 `> 待核实`；权威 arXiv 预印本；关注度 高 — 依据为"低成本全身遥操作"成为社区广泛复刻的范式；推荐度 ★★★★★ [18] |
| **InterACT** [65] | 2024 | 依赖关系感知的层级注意力 Transformer 动作分块，面向双臂操作 | 热度 `> 待核实`；权威 arXiv 预印本；关注度 中；推荐度 ★★★★☆ — 动作分块在双臂上的直接延伸 [65] |
| **DAIR** [67] | 2021 | 解耦注意力内在正则，实现安全高效双臂操作 | 热度 `> 待核实`；权威 arXiv 预印本；关注度 中；推荐度 ★★★★☆ [67] |
| **Stabilize to Act** [69] | 2023 | 学习双臂协同中的"先稳定后动作"协调 | 热度 `> 待核实`；权威 arXiv 预印本；关注度 中；推荐度 ★★★★★ — 对"协调"这一双臂核心难题给出显式机制 [69] |
| **VoxAct-B** [71] | 2024 | 体素表示的双臂动作与稳定策略 | 热度 `> 待核实`；权威 arXiv 预印本；关注度 中；推荐度 ★★★★☆ [71] |
| **RoboTwin 双臂协作挑战赛** [66] | 2025 | 泛化双臂操作的基准化评测 | 热度 `> 待核实`；权威 arXiv 预印本 + CVPR 2025 Workshop；关注度 中；推荐度 ★★★★☆ [66] |

### 5.2 sim2real

- **Bridging the Sim2Real Gap: Vision Encoder Pre-Training for Visuomotor Policy Transfer** [47]：以视觉编码器预训练缩小 sim2real 差距。
  - 热度 `> 待核实`；权威 arXiv 预印本；关注度 中；推荐度 ★★★★★ — 直接对应 sim2real 主线，是本报告该章最相关的可核查条目 [47]
- **The Importance and the Limitations of Sim2Real for Robotic Manipulation in Precision Agriculture** [48]：**标题即表明讨论 sim2real 的局限性**，是"负结果/边界条件"类证据的少数候选。
  - 热度 `> 待核实`；权威 arXiv 预印本；关注度 中；推荐度 ★★★★★ — 明确以"局限"为论述对象，对平衡报道有价值 [48]
- **Benchmarking Simulated Robotic Manipulation through a Real World Dataset** [32]：用真机数据集校验仿真操作评测，直接指向"仿真 SOTA ≠ 真机 SOTA"的口径问题。
  - 热度 `> 待核实`；权威 arXiv 预印本；关注度 中；推荐度 ★★★★★ [32]
- **ManiWAV** [34]：从野外音视频数据学习机器人操作，属跨模态数据来源扩展。
  - 热度 `> 待核实`；权威 arXiv 预印本；关注度 中；推荐度 ★★★☆☆ [34]
- **缺口声明**：结构化发现 q6 明确记录，本轮候选证据**没有任何一条直接讨论 sim2real 差距、数据规模律（scaling law）或跨本体泛化**，这三项在本轮证据下无法给出结论 `> 待核实`（该缺口判断由 [45][46][52][53][54][1] 的构成分析得出）。

---

## 六、经典与奠基性工作

> 说明：下表中的热度与权威字段，凡本轮检索未取回可核查数据者一律标 `> 待核实`；种子资源条目的同行评审状态 **本轮未实时检索核实**，仅转述种子元数据。

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| **Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware (ALOHA / ACT)** [93] | 2023 | 学术团队（RSS） | citations=2564（Semantic Scholar）[93] | RSS 同行评审顶会 [93] | 高 — 2564 次引用，本方向被引最高奠基成果之一 [93] | ★★★★★ 低成本双臂精细操作与动作分块必读源头 | https://arxiv.org/abs/2304.13705 |
| **Diffusion Policy: Visuomotor Policy Learning via Action Diffusion**（种子资源） | 2023 | 种子标注 RSS | `> 待核实` | `> 待核实`（本轮未取回一手页面） | 高 — 依据为扩散策略已成为本方向主流范式命名（见 [63]） | ★★★★★ 扩散策略方法论起点 | https://arxiv.org/abs/2303.04137 |
| **QT-Opt: Scalable Deep RL for Vision-Based Robotic Manipulation**（种子资源） | 2018 | 种子标注 CoRL | `> 待核实` | `> 待核实`（本轮未取回一手页面） | 中 — 依据为视觉抓取 RL 的早期规模化代表（本报告未取得引用数据） | ★★★★☆ 视觉抓取 RL 经典入口 | https://arxiv.org/abs/1806.10293 |
| **Learning Dexterous In-Hand Manipulation** [2] | 2018 | OpenAI（据标题与来源） | `> 待核实` | arXiv 预印本 | 高 — 依据为 in-hand manipulation RL 的命名性里程碑 | ★★★★★ 手内操作 RL 必读 | http://arxiv.org/abs/1808.00177v5 |
| **Learning Complex Dexterous Manipulation with Deep RL and Demonstrations** [3] | 2017 | 学术团队 | `> 待核实` | arXiv 预印本 | 中–高 — 依据为"RL + 演示"用于灵巧手的历史奠基 | ★★★★★ 演示增强 RL 灵巧操作源头 | http://arxiv.org/abs/1709.10087v2 |
| **DEFT: Dexterous Fine-Tuning for Real-World Hand Policies** [4] | 2023 | 学术团队 | `> 待核实` | arXiv 预印本 | 中 — 依据为"真机手部策略微调"路线 | ★★★★☆ 真机灵巧策略微调 | http://arxiv.org/abs/2310.19797v2 |
| **Learning Contact-Rich Manipulation Skills with Guided Policy Search** [101] | 2015 | 学术团队 | `> 待核实` | arXiv 预印本 | 中 — 接触丰富操作方法论源头 | ★★★★★ 接触丰富操作经典 | http://arxiv.org/abs/1501.05611v2 |
| **A System for General In-Hand Object Re-Orientation** [81] | 2021 | 学术团队 | `> 待核实` | arXiv 预印本 | 中–高 — 通用物体重定向代表系统 | ★★★★★ 手内重定向经典 | http://arxiv.org/abs/2111.03043v1 |
| **DexArt: Benchmarking Generalizable Dexterous Manipulation with Articulated Objects** [43] | 2023 | 学术团队 | `> 待核实` | arXiv 预印本 | 中 — 依据为铰接物体灵巧操作基准 | ★★★★★ 灵巧操作泛化基准经典 | http://arxiv.org/abs/2305.05706v1 |
| **Open X-Embodiment: Robotic Learning Datasets and RT-X Models** [31] | 2023 | 多机构协作 | `> 待核实` | arXiv 预印本（v9 持续修订） | 高 — 依据为跨本体数据聚合与 RT-X 模型成为跨本体研究基准起点 | ★★★★★ 跨本体泛化必读 | http://arxiv.org/abs/2310.08864v9 |

---

## 七、数据集、基准与开放问题

### 7.1 数据集与基准

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| **Open X-Embodiment（RT-X）** [31] | 2023 | 多机构协作 | `> 待核实` | arXiv 预印本，v9 持续修订 [31] | 高 — 跨本体数据聚合的参照点 | ★★★★★ 跨本体泛化主线入口 | http://arxiv.org/abs/2310.08864v9 |
| **DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset** [33] | 2024 | 学术团队 | `> 待核实` | arXiv 预印本 [33] | 中–高 — 依据为"in-the-wild 大规模操作数据"定位 | ★★★★★ 大规模真机数据候选首选 | http://arxiv.org/abs/2403.12945v2 |
| **DexArt** [43] | 2023 | 学术团队 | `> 待核实` | arXiv 预印本 [43] | 中 | ★★★★★ 铰接物体灵巧操作基准 | http://arxiv.org/abs/2305.05706v1 |
| **RoboMimic**（种子资源） | — | 种子 | `> 待核实` | `> 待核实` | 中–高 — 依据为模仿学习基准的通行地位 | ★★★★★ 模仿学习基准入口 | https://robomimic.github.io/ |
| **DexGraspNet / DexArt 数据**（种子资源） | — | PKU-EPIC | `> 待核实` | `> 待核实` | 中 | ★★★★☆ 灵巧抓取数据入口 | https://github.com/PKU-EPIC/DexGraspNet |
| **BridgeData V2**（种子资源） | — | RAIL Berkeley | `> 待核实` | `> 待核实` | 中–高 — 依据为大规模操作数据常用来源 | ★★★★☆ 大规模操作数据入口 | https://rail-berkeley.github.io/bridgedata/ |
| **LIBERO-Para** [35] | 2026 | Chanyoung Kim 等（非官方 LIBERO 维护方） | `> 待核实` | arXiv 预印本 cs.LG，未经同行评审 [35] | 低 — 无引用/star/榜单信号 | ★★★☆☆ 语言泛化诊断，支撑"基准可比性存疑" | http://arxiv.org/abs/2603.28301v3 |
| **LIBERO-VPro** [36] | 2026 | Huiqiong Li, Zhiting Mei, Anirudha Majumdar, Jingjing Chen, Yu-Gang Jiang, Bin Zhu | `> 待核实` | arXiv 预印本 cs.RO，未经同行评审 [36] | 低 — 仅 v1 一次提交，无引用数据 | ★★★☆☆ 闭环视觉鲁棒性诊断 | http://arxiv.org/abs/2609.24350v1 |
| **ManiSkill-ViTac 2025** [95] | 2024 | 学术团队 | `> 待核实` | arXiv 预印本（challenge 综述）[95] | 中–高 — 触觉赛题形式 | ★★★★☆ 视触觉赛题与基线 | http://arxiv.org/abs/2411.12503v1 |
| **ManiFeel** [100] | 2025 | 学术团队 | `> 待核实` | arXiv 预印本 cs.RO [100] | 中–高 — 视触觉策略专用基准 | ★★★★★ 触觉策略评测核心 | http://arxiv.org/abs/2505.18472v2 |
| **LabDex** [11] | 2026 | 学术团队 | `> 待核实` | arXiv 预印本 cs.RO [11] | 中 | ★★★★☆ 实验室场景分层灵巧基准 | http://arxiv.org/abs/2608.18618v1 |
| **ManipBench** [54] | 2025 | 学术团队 | `> 待核实` | arXiv 预印本 cs.RO（v2 修订）[54] | 中 — 命中"低层 VLM 推理缺少统一基准"痛点 | ★★★★☆ 评测缺口的一手证据 | http://arxiv.org/abs/2505.09698v2 |

### 7.2 评测协议的可比性问题（本轮最值得注意的发现）

1. **LIBERO 衍生诊断基准揭示标准评测的口径缺陷**：
   - **LIBERO-Para** 在 7 个 VLA 配置（0.6B–7.5B）上观察到指令改写条件下 **22–52 个百分点**的一致性能下降，且下降主要由物体层级词汇变化驱动，简单同义词替换即可触发 [35]。
   - **LIBERO-VPro** 覆盖 4 个维度（Visual Evidence Degradation、Camera Staleness、Visual Source Consistency、Task-Relevant Scene Variation）、12 类挑战、96 个实验设置、3296 个 task-condition 用例，评测 3 个 VLA 模型与 3 个 world-action 模型，约 19.6 万个仿真 episode，另加 200 次真机 rollout [36]。
   - 四类证据（两者合并）：热度 `> 待核实`；权威：均为 arXiv 预印本，未经同行评审、非官方基准主页 [35][36]；关注度 低（无引用/star/榜单信号）；推荐度 ★★★☆☆ — 主题相关性强但证据等级为 B，宜作线索而非定论 [35][36]。
2. **仿真规模与真机验证严重不均衡**：LIBERO-VPro 的仿真侧约 196,000 episode，真机侧仅 200 次 rollout，相差三个数量级，真机结论的统计效力 `> 待核实` [36]。
3. **基准横向对比存在硬缺口**：Open X-Embodiment、DROID、RoboMimic、SimplerEnv、RoboArena、Adroit/DexArt/Meta-World 各自的任务数、本体数量、仿真/真机口径与榜单刷新状态，**在本轮证据下无法完成横向对比**，各项均 `> 待核实`（结构化发现 q4 明确记录，并指出 [28][26][27][29] 等候选为无关领域的医疗影像/语义分割/语音/选举 Discourse 数据集）[26][27][28][29]。
4. **评测协议细节缺失**：episode 数、随机种子数、成功判定阈值、是否允许重置等字段本轮均未取回，因此"基准之间可比性"只能给出方法论层面的怀疑，**无法量化** `> 待核实`。

### 7.3 开放问题与争议（逐项标注证据状态）

| 开放问题 | 本轮证据状态 |
|---|---|
| 抓取检测与抓取合成（GraspNet / AnyGrasp、接触点表示） | **完全未覆盖** `> 待核实` — 需补充 arXiv/GitHub 一手检索 |
| in-hand RL 里程碑（OpenAI Dactyl、DextrAH、Visual Dexterity）的任务/硬件/指标 | **未覆盖细节** `> 待核实` — 可引用入口仅 [2][3][81][84] |
| 精细操作模仿学习的累积误差、多模态融合、传感器空间感知 | 仅由 [94] 提出，缺高等级证据支撑其严重程度 `> 待核实` |
| [83] 的三任务、零样本迁移结果 | 单一预印本宣称，无第三方复现或榜单验证 `> 待核实` |
| 低层 VLM 推理的统一评测基准缺失 | 有 [54] 摘要级一手证据，任务规模与第三方采用度待核实 [54] |
| 可变形物体（线缆）灵巧操作欠探索 | 有 [1][99] 支撑；真机实验规模与成本数据 `> 待核实` [1][99] |
| sim2real 差距 | **本轮候选无直接证据** `> 待核实`；仅 [47][48][32] 为可核查入口 [32][47][48] |
| 数据规模律（scaling law）是否在机器人学习成立 | **未覆盖** `> 待核实` |
| 跨本体（cross-embodiment）泛化是否成立 | **未覆盖结论** `> 待核实`；仅 [31] 为入口 [31] |
| 硬件耐久与成本 | 仅有 [1] 指出多指手设计与可变形物体挑战，无耐久/成本量化 `> 待核实` [1] |
| 公开失败案例与负结果 | **本轮候选无任何负结果/失败复盘** `> 待核实`；[48] 讨论 sim2real 局限，是唯一接近该维度的条目 [48] |
| HRI 信任与人机协作 | 有 [52]（RO-MAN 2025 workshop 论文集，7 篇，无 PDF）；与 sim2real/硬件主线相关度有限 [52] |

---

## 八、建议关注清单（Watchlist）

| 优先级 | 条目 | 类型 | 为什么关注 | 四类证据摘要 |
|---|---|---|---|---|
| P0 | **Action chunking 基线体系（ACT 及其改进）** [93][94] | 方法/基线 | 本方向使用最广的基线与被改进对象 | 热度 citations=2564 [93]；权威 RSS [93]；关注度 高 [93]；推荐度 ★★★★★ [93] |
| P0 | **LIBERO 衍生诊断基准（语言泛化 / 闭环视觉鲁棒性）** [35][36] | 评测 | 直接挑战"标准基准分数可比"的默认假设，改写导致 22–52 pp 下降 | 热度 `> 待核实`；权威 arXiv 预印本未评审 [35][36]；关注度 低；推荐度 ★★★☆☆ [35][36] |
| P0 | **触觉策略基准 ManiFeel + ManiSkill-ViTac 2025** [95][100] | 基准/赛题 | 判断触觉是否真正进入策略评测主线的关键坐标 | 热度 `> 待核实`；权威 arXiv 预印本 [95][100]；关注度 中–高；推荐度 ★★★★★/★★★★☆ |
| P0 | **跨本体数据与模型（Open X-Embodiment / RT-X）** [31] | 数据/模型 | 跨本体泛化是否成立的基础设施 | 热度 `> 待核实`；权威 arXiv 预印本 v9 [31]；关注度 高；推荐度 ★★★★★ |
| P1 | **单手内两刚体装配** [83] | 方法 | in-hand 任务复杂度跃升的代表；零样本仿真→真机 | 热度 `> 待核实`；权威预印本 [83]；关注度 中；推荐度 ★★★☆☆ |
| P1 | **VLA × 灵巧手统一框架 UniHM** [73] | 方法 | VLA 与灵巧手结合的开放词汇指令路线 | 热度 `> 待核实`；权威预印本 [73]；关注度 中；推荐度 ★★★☆☆ |
| P1 | **ContactWorld（视觉-触觉隐世界模型表示）** [102] | 方法/基准 | 回答"触觉该以什么表示进入世界模型" | 热度 `> 待核实`；权威预印本 [102]；关注度 中；推荐度 ★★★★☆ |
| P1 | **TransDex（透明物视触觉策略）** [8] | 方法 | 透明物自遮挡与深度丢失是硬场景 | 热度 `> 待核实`；权威预印本 [8]；关注度 中；推荐度 ★★★★☆ |
| P1 | **sim2real 局限与方法** [47][48][32] | 方法/评测 | 补充本轮最大证据缺口（sim2real 直接证据） | 热度 `> 待核实`；权威预印本 [32][47][48]；关注度 中；推荐度 ★★★★★ |
| P2 | **低成本双臂硬件与全身遥操作** [17][18] | 硬件/系统 | 真机可复现性的成本前提 | 热度 `> 待核实`；权威预印本 [17][18]；关注度 高（[18]）；推荐度 ★★★★☆/★★★★★ |
| P2 | **双臂协同结构与基准** [65][66][67][69][71] | 方法/基准 | 双臂"协调"机制的工程化选项集合 | 热度 `> 待核实`；权威预印本 [65][66][67][69][71]；关注度 中；推荐度 ★★★★☆ 起 |
| P2 | **触觉 sim2real 仿真链条** [103][105] | 仿真 | 触觉 sim2real 的可实现性证据 | 热度 `> 待核实`；权威预印本 [103][105]；关注度 中；推荐度 ★★★★☆ |
| P2 | **可变形线性物体（DLO）安全操作** [1][99] | 任务/安全 | 欠探索方向 + 接触力/张力约束 | 热度 `> 待核实`；权威预印本 [1][99]；关注度 中；推荐度 ★★★★☆ |
| P3 | **开源栈与工程平台** [6][10][13][16][104] | 工程 | 真机复现与仿真吞吐的基础设施 | 热度 `> 待核实`；权威 arXiv 预印本 [6][10][13][16][104]；关注度 中；推荐度 ★★★★☆ |

**必须补齐的检索动作（建议下一步）**：
1. GraspNet / AnyGrasp / 接触点表示 / 抓取合成的一手论文与官方仓库（本轮完全未覆盖）。
2. AnyGrasp SDK、MuJoCo Menagerie、Open-TeleVision、RoboSuite 的维护状态（最近提交、依赖、真机可复现性）——**本轮均未覆盖** `> 待核实`。
3. Open X-Embodiment / DROID / RoboMimic / SimplerEnv / RoboArena / Adroit / DexArt / Meta-World 的任务数、本体数、仿真 vs 真机口径与 leaderboard 刷新记录。
4. sim2real、scaling law、cross-embodiment 的专项检索（本轮**无直接证据**）。
5. 负结果与复现报告（本轮**无任何候选**）。

---

## 参考来源

[1] Dexterous Cable Manipulation: Taxonomy, Multi-Fingered Hand Design, and Long-Horizon Manipulation — http://arxiv.org/abs/2502.00396v2
[2] Learning Dexterous In-Hand Manipulation — http://arxiv.org/abs/1808.00177v5
[3] Learning Complex Dexterous Manipulation with Deep Reinforcement Learning and Demonstrations — http://arxiv.org/abs/1709.10087v2
[4] DEFT: Dexterous Fine-Tuning for Real-World Hand Policies — http://arxiv.org/abs/2310.19797v2
[5] Aerial Mobile Manipulator System to Enable Dexterous Manipulations with Increased Precision — http://arxiv.org/abs/2010.09618v1
[6] LeRobot: An Open-Source Library for End-to-End Robot Learning — http://arxiv.org/abs/2602.22818v1
[7] HANDO: Hierarchical Autonomous Navigation and Dexterous Omni-loco-manipulation — http://arxiv.org/abs/2510.09221v1
[8] TransDex: Pre-training Visuo-Tactile Policy with Point Cloud Reconstruction for Dexterous Manipulation of Transparent Objects — http://arxiv.org/abs/2603.13869v2
[9] The Synthesis of Optimal Control Laws Using Isaacs' Method for the Solution of Differential Games — http://arxiv.org/abs/2112.10849v2
[10] Isaac Lab: A GPU-Accelerated Simulation Framework for Multi-Modal Robot Learning — http://arxiv.org/abs/2511.04831v1
[11] LabDex: A Hierarchical Benchmark for Dexterous Manipulation in Laboratories — http://arxiv.org/abs/2608.18618v1
[12] Fiatlux: A Long-Horizon Benchmark for Humanoid Ladder Climbing and Light-Bulb Replacement — https://arxiv.org/abs/2609.38216
[13] LEAP Hand: Low-Cost, Efficient, and Anthropomorphic Hand for Robot Learning — http://arxiv.org/abs/2309.06440v1
[14] Rapid Learning of Dexterous In-Hand Pen Writing through Real-Time Jacobian Estimation — http://arxiv.org/abs/2609.11775v1
[15] Open Source Software Development Challenges: A Systematic Literature Review on GitHub — http://arxiv.org/abs/2003.10750v3
[16] Aero Hand Open: A Simulation-Ready Tendon-Driven Hand for Dexterous Manipulation Learning — http://arxiv.org/abs/2608.28578v2
[17] ALOHA 2: An Enhanced Low-Cost Hardware for Bimanual Teleoperation — http://arxiv.org/abs/2405.02292v1
[18] Mobile ALOHA: Learning Bimanual Mobile Manipulation with Low-Cost Whole-Body Teleoperation — http://arxiv.org/abs/2401.02117v1
[19] RePO: Replay-Enhanced Policy Optimization — http://arxiv.org/abs/2506.09340v1
[20] Gap Risk KVA and Repo Pricing: An Economic Capital Approach in the Black-Scholes-Merton Framework — http://arxiv.org/abs/1604.05406v3
[21] ARMrayan Multimedia Mobile CMS: a Simplified Approach towards Content-Oriented Mobile Application Designing — http://arxiv.org/abs/1009.5347v1
[22] LEAP: TrustZone Based Developer-Friendly TEE for Intelligent Mobile Apps — http://arxiv.org/abs/2102.02465v3
[23] Enhancing Contention Resolution ALOHA using Combining Techniques — http://arxiv.org/abs/1602.07636v3
[24] A Low-Energy Fast Cyber Foraging Mechanism for Mobile Devices — http://arxiv.org/abs/1111.4499v1
[25] The RSNA Abdominal Traumatic Injury CT (RATIC) Dataset — http://arxiv.org/abs/2405.19595v1
[26] Point Transformer V3 Extreme: 1st Place Solution for 2024 Waymo Open Dataset Challenge in Semantic Segmentation — http://arxiv.org/abs/2407.15282v1
[27] NTU-NPU System for Voice Privacy 2024 Challenge — http://arxiv.org/abs/2410.02371v1
[28] The RSNA Intracranial Aneurysm (RSNA-ICA) Dataset — http://arxiv.org/abs/2610.01135v2
[29] Unfiltered Conversations: A Dataset of 2024 U.S. Presidential Election Discourse on Truth Social — http://arxiv.org/abs/2411.01330v1
[30] Discovery Opportunities with Gravitational Waves -- TASI 2024 Lecture Notes — http://arxiv.org/abs/2409.08956v1
[31] Open X-Embodiment: Robotic Learning Datasets and RT-X Models — http://arxiv.org/abs/2310.08864v9
[32] Benchmarking Simulated Robotic Manipulation through a Real World Dataset — http://arxiv.org/abs/1911.01557v2
[33] DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset — http://arxiv.org/abs/2403.12945v2
[34] ManiWAV: Learning Robot Manipulation from In-the-Wild Audio-Visual Data — http://arxiv.org/abs/2406.19464v2
[35] LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models — http://arxiv.org/abs/2603.28301v3
[36] LIBERO-VPro: Benchmarking Closed-Loop Visual Robustness of Robotic Foundation Models — http://arxiv.org/abs/2609.24350v1
[37] A Simulation and Modeling of Access Points with Definition Language — http://arxiv.org/abs/1304.1836v2
[38] Superconductivity as a consequence of an ordering of the electron gas zero-point oscillations — http://arxiv.org/abs/1005.0280v6
[39] Intutionistic Fuzzy Ideals in Γ-semiring — http://arxiv.org/abs/1011.5746v2
[40] Internal Location Based System For Mobile Devices Using Passive RFID And Wireless Technology — http://arxiv.org/abs/1001.2258v2
[41] The meaning of systematic errors, a comment to "Reply to On the Systematic Errors in the Detection of the Lense-Thirring Effect with a Mars Orbiter", by Lorenzo Iorio — http://arxiv.org/abs/gr-qc/0703020v3
[42] Explicit estimates on prime numbers — http://arxiv.org/abs/1407.7158v2
[43] DexArt: Benchmarking Generalizable Dexterous Manipulation with Articulated Objects — http://arxiv.org/abs/2305.05706v1
[44] Pneumatic Modelling for Adroit Manipulation Platform — http://arxiv.org/abs/1703.01653v1
[45] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1
[46] Event-Enriched Image Analysis Grand Challenge at ACM Multimedia 2025 — http://arxiv.org/abs/2508.18904v1
[47] Bridging the Sim2Real Gap: Vision Encoder Pre-Training for Visuomotor Policy Transfer — http://arxiv.org/abs/2501.16389v2
[48] The Importance and the Limitations of Sim2Real for Robotic Manipulation in Precision Agriculture — http://arxiv.org/abs/2008.03983v1
[49] LLM-based ambiguity detection in natural language instructions for collaborative surgical robots — http://arxiv.org/abs/2507.11525v1
[50] Human-Robot collaboration in surgery: Advances and challenges towards autonomous surgical assistants — http://arxiv.org/abs/2507.11460v1
[51] A Case for a "Refutations and Critiques" Track in Statistics Journals — http://arxiv.org/abs/2509.03702v3
[52] TRUST 2025: SCRITA and RTSS @ RO-MAN 2025 — http://arxiv.org/abs/2509.11402v1
[53] NTIRE 2025 Challenge on Image Super-Resolution (x4): Methods and Results — http://arxiv.org/abs/2504.14582v3
[54] ManipBench: Benchmarking Vision-Language Models for Low-Level Robot Manipulation — http://arxiv.org/abs/2505.09698v2
[55] Coarse-to-Fine Imitation Learning: Robot Manipulation from a Single Demonstration — http://arxiv.org/abs/2105.06411v2
[56] On-Policy Robot Imitation Learning from a Converging Supervisor — http://arxiv.org/abs/1907.03423v7
[57] One-Shot Visual Imitation Learning via Meta-Learning — http://arxiv.org/abs/1709.04905v1
[58] One-Shot Reinforcement Learning for Robot Navigation with Interactive Replay — http://arxiv.org/abs/1711.10137v2
[59] From One Hand to Multiple Hands: Imitation Learning for Dexterous Manipulation from Single-Camera Teleoperation — http://arxiv.org/abs/2204.12490v2
[60] SPIRE: Synergistic Planning, Imitation, and Reinforcement Learning for Long-Horizon Manipulation — http://arxiv.org/abs/2410.18065v1
[61] Learning to Discern: Imitating Heterogeneous Human Demonstrations with Preference and Representation Learning — http://arxiv.org/abs/2310.14196v1
[62] Learning and Retrieval from Prior Data for Skill-based Imitation Learning — http://arxiv.org/abs/2210.11435v2
[63] Dexterous Functional Pre-Grasp Manipulation with Diffusion Policy — http://arxiv.org/abs/2403.12421v2
[64] Grasp and Motion Planning for Dexterous Manipulation for the Real Robot Challenge — http://arxiv.org/abs/2101.02842v1
[65] InterACT: Inter-dependency Aware Action Chunking with Hierarchical Attention Transformers for Bimanual Manipulation — http://arxiv.org/abs/2409.07914v3
[66] Benchmarking Generalizable Bimanual Manipulation: RoboTwin Dual-Arm Collaboration Challenge at CVPR 2025 MEIS Workshop — http://arxiv.org/abs/2506.23351v2
[67] DAIR: Disentangled Attention Intrinsic Regularization for Safe and Efficient Bimanual Manipulation — http://arxiv.org/abs/2106.05907v4
[68] Technical Report for Ego4D Long-Term Action Anticipation Challenge 2025 — http://arxiv.org/abs/2506.02550v2
[69] Stabilize to Act: Learning to Coordinate for Bimanual Manipulation — http://arxiv.org/abs/2309.01087v2
[70] Generalist Robot Manipulation beyond Action Labeled Data — http://arxiv.org/abs/2509.19958v1
[71] VoxAct-B: Voxel-Based Acting and Stabilizing Policy for Bimanual Manipulation — http://arxiv.org/abs/2407.04152v2
[72] Inference-Time Attention Steering for Vision-Language-Action Driving Models — http://arxiv.org/abs/2608.17095v1
[73] UniHM: Unified Dexterous Hand Manipulation with Vision Language Model — http://arxiv.org/abs/2603.00732v1
[74] Task adaptation of Vision-Language-Action model: 1st Place Solution for the 2025 BEHAVIOR Challenge — http://arxiv.org/abs/2512.06951v2
[75] Compositional Context Fine-Tuning Vision-Language Model for Complex Assembly Action Understanding from Videos — http://arxiv.org/abs/2607.10797v1
[76] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1
[77] VLSP 2025 MLQA-TSR Challenge: Vietnamese Multimodal Legal Question Answering on Traffic Sign Regulation — http://arxiv.org/abs/2510.20381v1
[78] The AudioMOS Challenge 2025 — http://arxiv.org/abs/2509.01336v1
[79] MAGIC and MWL monitoring of the blazar TXS 0506+056 in the 2018/2019 season — http://arxiv.org/abs/1909.04938v1
[80] The 2018 PIRM Challenge on Perceptual Image Super-resolution — http://arxiv.org/abs/1809.07517v3
[81] A System for General In-Hand Object Re-Orientation — http://arxiv.org/abs/2111.03043v1
[82] QCD and High Energy Interactions: Moriond 2018 Theory Summary — http://arxiv.org/abs/1806.04982v2
[83] Assembling Two Parts in One Hand — http://arxiv.org/abs/2609.10137v1
[84] Stable In-hand Manipulation with Finger Specific Multi-agent Shadow Reward — http://arxiv.org/abs/2309.07349v1
[85] The Open Ant: A Robot Platform for Reinforcement Learning Research — http://arxiv.org/abs/2607.18488v1
[86] Value Bonuses using Ensemble Errors for Exploration in Reinforcement Learning — http://arxiv.org/abs/2602.12375v1
[87] Causal-Paced Deep Reinforcement Learning — http://arxiv.org/abs/2507.02910v1
[88] Constrained Reinforcement Learning for Dexterous Manipulation — http://arxiv.org/abs/2301.09766v1
[89] Exploring Hierarchy-Aware Inverse Reinforcement Learning — http://arxiv.org/abs/1807.05037v1
[90] Knowledge-Embedded Representation Learning for Fine-Grained Image Recognition — http://arxiv.org/abs/1807.00505v1
[91] Overview of AuTexTification at IberLEF 2023

---

*Generated by research-bot · topic=`embodied-manipulation` · depth=`standard` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading · model=`deepseek-v4-flash` · sources=110 · duration=297s · 2026-10-05T22:36:04+00:00*
