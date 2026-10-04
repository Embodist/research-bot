# 具身智能·灵巧操作（Dexterous Manipulation & Grasping）技术地图

**日期**：2026-10-04（UTC） | **领域**：具身智能 / 灵巧操作与抓取（Dexterous Manipulation & Grasping） | **检索源数量**：候选来源 119 条（编号 [1]–[119]），其中与本主题直接相关约 55 条，其余为跨领域检索噪声（如面部识别、短视频生成、天文学等） | **方法论**：deep-research + frontier-tracking + paper-survey + evidence-grading

> **证据可得性声明**：本次候选块中绝大多数条目的 `citations` / `stars` 字段为空，因此下文"热度证据"大量标注 `> 待核实`，绝不填充推测数字。凡"机构""venue 等级"等超出候选块元数据的判断，均加限定词或标注 `> 待核实`。

---

## 摘要（Executive Summary）

2024–2026 年，灵巧操作与抓取的主导范式已从"模块化抓取检测 + 规划"转向"多模态端到端策略 + 大规模数据"。三个可核查的趋势最为突出：

1. **触觉从"可选增益"变为"接触丰富任务的必需模态"**，且出现"训练时用触觉、推理时不用触觉"的新折衷（HapticVLA [90]），以及视觉-触觉潜在世界模型（ContactWorld [86]）等表征层探索。
2. **动作分块（action chunking）与扩散策略成为灵巧操作的默认动作头**，并针对灵巧域做专门改造（VQ-ACE [13]、SERNF [15]、Factorizing Diffusion Policies [64]）。
3. **评测基础设施严重滞后于算法**：真机评测缺乏标准协议 [84]，新出现的 ManipulationNet [116]、ManiFeel [97]、ManiSkill-ViTac 2025 [75] 正试图填补，但灵巧抓取专用基准（DexGraspNet / DexYCB / OakInk 一类）在本次候选证据中**完全缺席**（见第七章缺口）。

**证据强度总体判断**：一手 arXiv 预印本充足（B 级），同行评审长文与官方榜单数据稀缺；本报告对方法论类结论给较高置信度，对"性能 SOTA""复现性""热度排名"一律留白为 `> 待核实`。

---

## 一、关键前沿进展（近 1–2 年）

### 1.1 时间线：可核查的关键节点

| 时间 | 事件 | 贡献一句话 | 证据强度 | 引用 |
|---|---|---|---|---|
| 2025 | BEHAVIOR Challenge 冠军方案 | 基于 Pi0.5 架构的 VLA 策略，在 50 个长时程家务任务（需双臂操作+导航+上下文决策）的照片级仿真基准中获第一 | 论文宣称，有官方竞赛语境 | [11] |
| 2025 | 灵巧缆线操作分类学与多指手设计 | 首次系统化提出缆线灵巧操作分类学，并配套多指手硬件与长时程操作方案 | arXiv 预印本 | [2] |
| 2025 | Factorizing Diffusion Policies | 针对观测模态（本体/视觉/触觉）对不同任务影响不均，提出因子化扩散策略以重排模态优先级 | arXiv 预印本（cs.RO） | [64] |
| 2025 | ManiFeel 基准 | 面向视觉-触觉操作策略学习的基准与理解性分析 | arXiv 预印本 | [97] |
| 2026 | 手内钢笔书写快速学习 | 通过实时 Jacobian 估计，让拟人手快速习得手内书写的接触丰富动态技能 | arXiv 预印本（cs.RO） | [12] |
| 2026 | HapticVLA | 提出**推理时不需要触觉传感**的触觉增强 VLA，缓解真机触觉部署成本 | arXiv 预印本 | [90] |
| 2026 | ContactWorld | 系统比较视觉-触觉潜在世界模型"什么表征才重要" | arXiv 预印本 | [86] |
| 2026 | LeRobot 论文 | 将已被广泛使用的开源端到端机器人学习库正式成文 | arXiv 预印本（cs.RO） | [23] |
| 2026 | ManipulationNet | 真机操作评测基础设施，含物理技能挑战与具身多模态推理 | arXiv 预印本，citations=15 | [116] |

### 1.2 判断"真前沿"的说明

按 frontier-tracking 四问逐条追问，**本次候选证据只能支撑到第二问（是否开源）的一部分**：

- **多任务/多本体验证**：[11] 在 50 任务仿真基准上验证，但**为仿真、非真机**；[12] 为真机但属单技能（写字）。跨本体泛化证据在本次候选中**不足** `> 待核实`。
- **开源情况**：[23] 明确为开源库论文，但其代码/权重可用性、许可证与复现难度需查官方仓库 `> 待核实`。
- **提升归因（数据/架构/算力）**：候选证据均为摘要级，无消融表，**无法归因** `> 待核实`。
- **第三方独立评测**：除 [11] 有竞赛名次外，其余均无第三方榜单，**不构成强证据**。

> **检索噪声提示（重要）**：结构化发现 q1 中列出的 [1] Foundation Model Transparency Index、[7] MOASEI、[8] IJCB-AFMFR、[9] VLA 驾驶注意力引导，分别属于 AI 治理、多智能体竞赛、人脸识别、自动驾驶，与本主题**无关**，本报告不予采信。q6 中的 [4] 短视频参与度预测、[17] NTIRE 超分同属噪声。

**四类证据（本章总体）**
- **热度证据**：除 [116]（citations=15）外均 `> 待核实`。
- **权威证据**：均为 arXiv 预印本（cs.RO 为主）；[11] 具竞赛官方背景。
- **关注度**：**中**——BEHAVIOR 挑战与 HapticVLA 类议题在社区讨论度较高，但无 star/榜单量化信号可援引 [11][90]。
- **推荐度**：**★★★☆☆～★★★★☆**——[11][12][90][86] 值得精读摘要与实验节，[2] 具综述价值；因缺第三方验证不给予满分。

---

## 二、模仿学习与扩散/动作分块策略

### 2.1 动作头演进：扩散 → 因子化 → 分块加速

- **扩散策略仍为主导动作头，但已进入"精修期"。** Factorizing Diffusion Policies [64] 直面一个被忽视的问题：本体感知、视觉、触觉对**不同任务**的贡献权重不同，统一条件化会导致次优；其方案是对观测模态做因子化并重排优先级 [64]。**权威**：arXiv 2509.16830v1（cs.RO），2025；**热度** `> 待核实`；**关注度** 中；**推荐度** ★★★★☆（直击多模态条件化痛点，适合做基线改进）。
- **扩散推理延迟问题被显式处理。** OnlineCache [62] 指出基于缓存（cache）的加速多依赖静态、样本无关的调度，提出带误差校正的动态缓存策略 [62]。**注意**：该文署名 cs.LG，属**通用扩散模型推理**领域，迁移到机器人策略需自行验证，**相关性中等** [62]。**热度** `> 待核实`；**关注度** 低—中；**推荐度** ★★★☆☆。
- **动作分块（action chunking）成为灵巧域的默认解法。** VQ-ACE [13] 通过"动作分块嵌入"实现高效策略搜索；SERNF [15] 用"动作分块评论家 + 归一化流"实现样本高效的真机灵巧策略微调 [13][15]。**权威**：[13] arXiv:2411.03556v1；[15] arXiv:2602.09580v4；**热度** `> 待核实`；**关注度** 中；**推荐度** ★★★★☆（真机样本效率是灵巧操作的核心瓶颈）。

### 2.2 异构数据与分布偏移

- **CLASS** [117] 指出行为克隆（BC）在**异构数据**（视觉偏移等）下性能显著退化，提出用动作序列监督做对比学习 [117]。**热度**：citations=13（候选块抽取值，**口径未核实**）；**权威**：arXiv:2508.01600，2025；**关注度** 中；**推荐度** ★★★★☆（异构数据正是 Open X-Embodiment [68] 类数据集的核心难题）。
- **分布偏移下的安全策略学习**：Conformal Policy Learning [60] 面向传感器运动控制中的分布偏移 [60]。**热度** `> 待核实`；**推荐度** ★★★☆☆。

### 2.3 模仿学习的奠基脉络

- **从监督对齐到自监督对应**：Self-Supervised Correspondence in Visuomotor Policy Learning [59] 用自监督对应关系降低对动作标注的依赖 [59]。
- **单样本/元学习路线**：One-Shot Visual Imitation Learning via Meta-Learning [118]、Coarse-to-Fine Imitation Learning（单演示）[115]。
- **在线模仿与理论收敛**：On-Policy Robot Imitation Learning from a Converging Supervisor [28]。
- **教程级综述**：Robot Learning: A Tutorial [24] 描述该领域正从经典模型驱动向数据驱动范式转变，并强调大规模机器人数据的可得性是其驱动力 [24]——可作为本报告的背景锚点 [24]。

**本章总体证据**：权威 A/B 级混合（多为预印本，少数有 DOI）；**热度普遍缺失** `> 待核实`；**关注度** 中；**推荐度** ★★★☆☆～★★★★☆。

---

## 三、灵巧手与手内操作

### 3.1 手内操作的技能前沿

- **[12] 手内钢笔书写（2026）**：摘要明确指出"带拟人手的物体手内灵巧操作仍未解决"，接触丰富性与高动态性通常要求大量建模或数据采集；该工作用**实时 Jacobian 估计**显著降低数据需求 [12]。这是本次候选中**最贴近"灵巧度极限"的新进展**。**权威**：arXiv:2609.11775v1（cs.RO）；**热度** `> 待核实`；**关注度** 中（议题天然高关注，但缺量化信号）；**推荐度** ★★★★☆。
- **[95] FBI 动态视觉触觉捷径策略**：以 shortcut policy 形式做手内操作的视觉-触觉学习 [95]，与第四章触觉线交叉。
- **[96] Robot Synesthesia**：以视觉触觉传感做手内操作，属"触觉-视觉通感"路线 [96]。
- **[13][15]**：见第二章，动作分块被明确用于灵巧操作策略搜索与真机微调 [13][15]。

### 3.2 硬件与本体设计

- **[98] GelSight Svelte Hand**：三指、两自由度、低成本、触觉丰富的灵巧手，明确面向灵巧操作 [98]。
- **[101] 多 GelSight 触觉传感器的全驱动机器人手设计** [101]——灵巧手 + 高分辨触觉的早期硬件范式。
- **[2] 多指手设计与长时程缆线操作（2025）**：指出既有缆线操作研究多依赖两指夹爪，难以完成人类式操作；该文给出分类学 + 多指手设计 + 长时程方案 [2]。**权威**：arXiv:2502.00396v2（cs.RO）；**热度** `> 待核实`；**关注度** 中；**推荐度** ★★★★☆（分类学部分对本报告结构有直接参考价值）。
- **[107] 空中移动机械臂系统**：以提升精度为目标的空中移动操作平台，属"扩展灵巧操作可达域"的非主流路线 [107]。**关注度** 低；**推荐度** ★★☆☆☆（与多指灵巧手主线关系较远）。

### 3.3 灵巧手的真机策略微调与遥操作数据采集

- **[10] DEFT: Dexterous Fine-Tuning for Real-World Hand Policies** 与 **[15] SERNF** 共同指向一个关键工程事实：**真机灵巧策略微调的样本效率是瓶颈**，业界正分别用"微调"与"动作分块评论家+归一化流"两条路应对 [10][15]。
- **[38] LeVR**：面向灵巧操作模仿学习的模块化 VR 遥操作框架 [38]——数据采集侧的工具链补位。
- **[33] ALOHA 2 / [39] Mobile ALOHA / [41] Tele-Aloha**：低成本双臂遥操作硬件系列（详见第五章）。

**本章总体证据**：权威以 arXiv 预印本为主；**热度** 普遍 `> 待核实`；**关注度** 中；**推荐度** ★★★☆☆～★★★★☆。

---

## 四、接触丰富任务与触觉/力感知

> 结构化发现 q5 的 `findings` 为空数组，本章由候选来源 [86]–[104] 与 [75] 独立重建。

### 4.1 核心问题：触觉到底"有没有用、在哪一步有用"

- **[90] HapticVLA** 给出一个反直觉但极工程化的主张：在**推理时不需要触觉传感**，仍能完成接触丰富操作 [90]。这直接回应了"触觉硬件贵、易损、难部署"的产业痛点。**权威**：arXiv:2603.15257v2；**热度** `> 待核实`；**关注度** 中—高（议题具争议性）；**推荐度** ★★★★★（若能成立，将改写触觉部署经济性；但需查其真机实验规模 `> 待核实`）。
- **[86] ContactWorld** 从表征层面提问："视觉-触觉潜在世界模型到底什么表征重要？" [86]。**权威**：arXiv:2606.13877v3；**关注度** 中；**推荐度** ★★★★☆（为触觉表征选择提供可比较的实证基础）。
- **[97] ManiFeel**：明确以"基准 + 理解"为定位，评估视觉-触觉操作策略学习 [97]。**推荐度** ★★★★☆（本报告第四章最需要的可复现评测入口）。
- **[75] ManiSkill-ViTac 2025 Challenge**：以 ManiSkill 为基座的"操作技能学习 + 视觉触觉"竞赛 [75]。**权威**：arXiv:2411.12503v1（竞赛报告）；**关注度** 中；**推荐度** ★★★★☆（**唯一明确将触觉与操作技能绑定的竞赛基准**）。

### 4.2 触觉驱动的策略学习（2025–2026 密集产出）

| 工作 | 时间 | 一句话贡献 | 引用 |
|---|---|---|---|
| Tac2Motion | 2025 | 接触感知 RL + 触觉反馈用于机械手操作 | [88] |
| Multi-Resolution Tactile Imitation Learning | 2026 | 多分辨率触觉模仿学习，面向接触丰富操作 | [91] |
| XRoboToolKit-T | 2026 | 高稳定高精度且带触觉的遥操作系统，面向接触丰富操作 | [87] |
| TouchDrive | 2026 | 无电子元件的触觉传感接口，用于辅助抓取 | [89] |
| VITaL Pretraining | 2024 | 视觉-触觉预训练，同时服务有触觉/无触觉策略 | [92] |
| Reactive Diffusion Policy | 2025 | 慢-快视觉-触觉策略学习，面向接触丰富操作 | [16] |
| 布料视觉触觉可供性 | 2022 | 局部控制的布料操作 | [93] |
| 遮挡下非抓取操作 | 2024 | 视觉触觉估计与控制 | [94] |

**热度**：全部 `> 待核实`（候选块未提供引用数）；**权威**：均为 arXiv 预印本；**关注度**：中（2025–2026 产出密集，属活跃区）；**推荐度**：★★★☆☆～★★★★☆（[90][86][91][16] 优先）。

### 4.3 触觉硬件与仿真（Sim2Real 基础）

- **硬件谱系**：GelSight 系列 [99][100][101]、DigiTac（DIGIT-TacTip 混合低成本高分辨触觉）[103]、GelSight Svelte Hand [98]。
- **仿真谱系**：
  - **Taxim** [104]：GelSight 传感器的样例式仿真模型；
  - **GelSight 触觉图像生成 for Sim2Real** [99]：显式面向 sim2real 学习；
  - **TacEx** [102]：在 Isaac Sim 中结合软体仿真与视觉触觉仿真器——**工程栈意义最强**，因为 Isaac Sim 是当前主流仿真后端 [102]。
- **力/物性感知**：[100] 用深度学习 + GelSight 做**与形状无关的硬度估计** [100]，是"触觉→物理属性"的早期奠基。

**权威**：[99][100][101] 为 2017–2020 年预印本；[102][103][104] 为 2021–2024 年预印本；**热度** `> 待核实`；**关注度** 中（TacEx 因绑定 Isaac Sim 而更受工程关注 [102]）；**推荐度** ★★★★☆（[102][104] 对 sim2real 触觉管线最有实操价值）。

---

## 五、双臂协同与 sim2real

### 5.1 双臂协同：硬件先行、策略跟进

- **低成本双臂遥操作硬件族**：ALOHA 2 [33]、Mobile ALOHA [39]、Tele-Aloha [41]。Mobile ALOHA 明确以"低成本全身遥操作学习双臂移动操作"为定位 [39]；ALOHA 2 为增强版低成本双臂遥操作硬件 [33]。
- **双臂策略的关键洞察——"先稳定再动作"**：Stabilize to Act [52] 把双臂协调拆成"稳定物体 + 执行动作"，DAIR [53] 用解耦注意力内在正则化实现安全高效双臂操作，VoxAct-B [54] 用体素表示同时做 acting 与 stabilizing [52][53][54]。这三条构成双臂协同**方法论主线**。
- **双臂 + VLA 的规模化验证**：[11] 的 BEHAVIOR 冠军方案明确强调**双臂操作**是 50 个长时程家务任务的必要条件之一 [11]。

**热度**：`> 待核实`；**权威**：[52][53][54] 为 arXiv 预印本（2021–2024）；[33][39][41] 为 2024 年预印本；**关注度** 中—高（ALOHA 系硬件在社区知名度高，但本候选块无 star 数据支撑，`> 待核实`）；**推荐度** ★★★★☆。

### 5.2 Sim2Real：从"迁移技巧"到"评测方法论"

- **[84] 是本次候选中唯一直接讨论评测口径的文章**，提出三条准则：(1) 使用高视觉保真仿真以改善 sim2real 迁移；(2) 通过系统性增加任务复杂度与场景扰动来评估鲁棒性；(3) 量化真机表现与其仿真对应表现之间的 **performance alignment** [84]。作者包含 Dieter Fox、Stan Birchfield、Jonathan Tremblay 等 NVIDIA 机器人团队核心成员，发表于 2025 RSS Workshop on Robot Evaluation for the Real World（**workshop 级别，非长文同行评审**）[84]。
- **[105]** 从**视觉编码器预训练**角度切入 sim2real 迁移 [105]；**[106]** 则给出反向警示：以精准农业为例，讨论 sim2real 对机器人操作的**重要性与其局限** [106]——这是本报告需要的"负面结果/边界条件"证据 [106]。
- **[30] Wheeled Lab**：低成本开源轮式机器人的现代 sim2real 范式 [30]。
- **[34] Robo-DM**：指出将超大规模遥操作演示数据用于训练 Transformer 策略时，**数据的管理、分发与加载本身**成为瓶颈 [34]。**热度**：citations=5（候选块抽取值，口径未核实）；**权威**：标注为 IEEE ICRA（**同行评审，A 级**）；**关注度** 中；**推荐度** ★★★★☆（数据基础设施是被低估的瓶颈）。

**本章 sim2real 证据总体**：**权威**为 workshop 论文 [84] + 预印本 [105][106][30] + ICRA 论文 [34]；**热度** 多为 `> 待核实`；**关注度** 中；**推荐度** ★★★☆☆～★★★★☆。

---

## 六、经典与奠基性工作

> 判定标准：2017–2023 年间、被后续工作反复引用或定义范式者。**热度列**中 GitHub star 与引用数若候选块未提供，一律写 `> 待核实`。

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Learning Dexterous In-Hand Manipulation | 2018 | `> 待核实`（候选块仅标注 cs.LG） | `> 待核实` | arXiv:1808.00177v5（预印本） | 高（该工作确立"仿真大规模 RL + 域随机化→真机手内操作"范式） | ★★★★★ | http://arxiv.org/abs/1808.00177v5 | 用 RL 在物理 Shadow 手上完成基于视觉的物体重定向；训练中对系统物理属性做大量随机化 [3] |
| Learning Complex Dexterous Manipulation with Deep RL and Demonstrations | 2017 | `> 待核实` | `> 待核实` | arXiv:1709.10087v2（预印本） | 高（"RL + 演示"混合范式的早期代表作） | ★★★★★ | http://arxiv.org/abs/1709.10087v2 | 深度 RL 与演示结合完成复杂灵巧操作 [5] |
| QT-Opt | 2018 | `> 待核实`（种子资源标注为 CoRL） | `> 待核实` | CoRL（种子资源标注） | 高（视觉抓取 RL 规模化经典） | ★★★★★ | https://arxiv.org/abs/1806.10293 | 可扩展的视觉抓取深度 RL（**种子资源，无候选编号**） |
| Diffusion Policy | 2023 | `> 待核实`（种子资源标注为 RSS） | `> 待核实` | RSS（种子资源标注） | 高（当前扩散策略的奠基引用） | ★★★★★ | https://arxiv.org/abs/2303.04137 | 通过动作扩散做视觉运动策略学习（**种子资源，无候选编号**） |
| ACT / ALOHA | 2023 | `> 待核实`（种子资源标注为 RSS） | `> 待核实` | RSS（种子资源标注） | 高（低成本双臂精细操作的事实标准） | ★★★★★ | https://arxiv.org/abs/2304.13705 | 低成本硬件 + 双臂精细操作模仿（**种子资源，无候选编号**） |
| Self-Supervised Correspondence in Visuomotor Policy Learning | 2019 | `> 待核实` | `> 待核实` | arXiv:1909.06933v1（预印本） | 中—高 | ★★★★☆ | http://arxiv.org/abs/1909.06933v1 | 自监督对应关系降低动作标注依赖 [59] |
| One-Shot Visual Imitation Learning via Meta-Learning | 2017 | `> 待核实` | `> 待核实` | arXiv:1709.04905v1（预印本） | 中—高 | ★★★★☆ | http://arxiv.org/abs/1709.04905v1 | 元学习实现单演示视觉模仿 [118] |
| Shape-independent Hardness Estimation using DL and GelSight | 2017 | `> 待核实` | `> 待核实` | arXiv:1704.03955v1（预印本） | 中（触觉→物性感知奠基） | ★★★★☆ | http://arxiv.org/abs/1704.03955v1 | 与形状无关的硬度估计 [100] |
| Generation of GelSight Tactile Images for Sim2Real Learning | 2021 | `> 待核实` | `> 待核实` | arXiv:2101.07169v1（预印本） | 中（触觉 sim2real 奠基） | ★★★★☆ | http://arxiv.org/abs/2101.07169v1 | 生成触觉图像用于 sim2real [99] |
| Taxim: Example-based Simulation for GelSight | 2021 | `> 待核实` | `> 待核实` | arXiv:2109.04027v2（预印本） | 中—高（触觉仿真的常用基座） | ★★★★☆ | http://arxiv.org/abs/2109.04027v2 | GelSight 样例式仿真模型 [104] |
| panda-gym | 2021 | `> 待核实` | `> 待核实` | arXiv:2106.13687v2（预印本） | 中（入门级开源环境） | ★★★☆☆ | http://arxiv.org/abs/2106.13687v2 | 开源目标条件机器人学习环境 [27] |
| DAIR | 2021 | `> 待核实` | `> 待核实` | arXiv:2106.05907v4（预印本） | 中（双臂安全操作早期工作） | ★★★★☆ | http://arxiv.org/abs/2106.05907v4 | 解耦注意力内在正则化 [53] |
| Design of a Fully Actuated Robotic Hand with Multiple GelSight Sensors | 2020 | `> 待核实` | `> 待核实` | arXiv:2002.02474v1（预印本） | 中 | ★★★★☆ | http://arxiv.org/abs/2002.02474v1 | 高分辨触觉 + 全驱动灵巧手 [101] |

> **表格说明**：种子资源（QT-Opt、Diffusion Policy、ACT/ALOHA）由本次调研的领域种子清单提供，**不在候选引用编号 [1]–[119] 内**，故不做编号引用，仅保留题录与链接。

---

## 七、数据集、基准与开放问题

### 7.1 数据集与基准总表

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Open X-Embodiment / RT-X | 2023 | `> 待核实` | `> 待核实` | arXiv:2310.08864v9（预印本，v9 表明长期迭代） | 高（跨本体大规模操作数据的核心汇聚） | ★★★★★ | http://arxiv.org/abs/2310.08864v9 | 机器人学习数据集与 RT-X 模型 [68] |
| DROID | 2024 | `> 待核实` | `> 待核实` | arXiv:2403.12945v2（预印本） | 高（野外真实场景大规模操作数据） | ★★★★★ | http://arxiv.org/abs/2403.12945v2 | 大规模 in-the-wild 操作数据集 [72] |
| LIBERO | 2023 | `> 待核实` | `> 待核实` | arXiv:2306.03310v2（预印本） | 高（终身机器人学习知识迁移基准） | ★★★★★ | http://arxiv.org/abs/2306.03310v2 | 终身学习基准 [79] |
| Train Offline, Test Online (TOTO) | 2023 | `> 待核实` | `> 待核实` | arXiv:2306.00942（预印本） | 中—高（离线训练-在线测试的真机基准协议） | ★★★★☆ | https://arxiv.org/abs/2306.00942 | 真机学习基准 [112] |
| ManipulationNet | 2026 | `> 待核实` | citations=15（候选块抽取值，口径未核实） | arXiv:2603.04363（预印本） | 中—高（**最新的真机操作评测基础设施**） | ★★★★★ | https://arxiv.org/abs/2603.04363 | 物理技能挑战 + 具身多模态推理的真机操作评测 [116] |
| ManiFeel | 2025 | `> 待核实` | `> 待核实` | arXiv:2505.18472v2（预印本） | 中（视觉触觉策略评测的唯一专门基准） | ★★★★★ | http://arxiv.org/abs/2505.18472v2 | 视觉触觉操作策略学习基准与理解 [97] |
| ManiSkill-ViTac 2025 Challenge | 2024/2025 | `> 待核实` | `> 待核实` | arXiv:2411.12503v1（竞赛报告） | 中 | ★★★★☆ | http://arxiv.org/abs/2411.12503v1 | 操作技能学习 + 视觉触觉竞赛 [75] |
| RoboAfford | 2025 | `> 待核实` | citations=23（候选块抽取值，口径未核实） | ACM Multimedia（**同行评审，A 级**） | 中 | ★★★★☆ | https://doi.org/10.1145/3746027.3758209 | 物体与空间可供性学习的数据集与基准 [113] |
| M4Bench | 2025 | `> 待核实` | citations=9（候选块抽取值，口径未核实） | Frontiers Robotics AI（**同行评审**） | 低—中 | ★★★☆☆ | https://doi.org/10.3389/frobt.2025.1528754 | 多用户多机器人多目标多设备 HRI 操作基准，针对 HRI 结果不可复现问题 [119] |
| SoftGym | 2020 | `> 待核实` | `> 待核实` | arXiv:2011.07215v2（预印本） | 中（可形变物体操作基准） | ★★★☆☆ | http://arxiv.org/abs/2011.07215v2 | 可形变物体操作 RL 基准 [111] |
| ROBEL | 2019 | `> 待核实` | `> 待核实` | arXiv:1909.11639v3（预印本） | 中（低成本机器人学习基准） | ★★★☆☆ | http://arxiv.org/abs/1909.11639v3 | 低成本机器人基准 [69] |
| Benchmarking RL Algorithms on Real-World Robots | 2018 | `> 待核实` | `> 待核实` | arXiv:1809.07731v1（预印本） | 中（真机 RL 基准化的早期尝试） | ★★★☆☆ | http://arxiv.org/abs/1809.07731v1 | 真机 RL 算法基准 [70] |
| RoboMimic | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | 高（模仿学习基准的常用入口） | ★★★★★ | https://robomimic.github.io/ | 模仿学习基准（**种子资源，无候选编号**） |
| DexArt / DexGraspNet | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | 高（灵巧抓取数据的主要公开来源） | ★★★★★ | https://github.com/PKU-EPIC/DexGraspNet | 灵巧抓取数据（**种子资源，无候选编号**） |
| BridgeData V2 | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | 高（大规模操作数据） | ★★★★★ | https://rail-berkeley.github.io/bridgedata/ | 大规模操作数据（**种子资源，无候选编号**） |

### 7.2 指标口径（仿真/真机、任务数、本体）——**重大证据缺口**

- **[84]** 是本次候选中唯一可直接用于"指标口径"讨论的方法学证据，它指出：基于视觉的机器人仿真基准已显著推动操作研究，但**面向通用策略的真实世界评测明显滞后**，因为机器人本质上是真实世界问题 [84]。
- 该文提出的三条准则为本报告提供口径框架：高视觉保真仿真、任务复杂度与场景扰动递增、真机-仿真性能一致性量化 [84]。**但这是方法学建议，不是任何具体数据集的任务数/本体口径** [84]。
- **本期候选证据完全未覆盖灵巧抓取专用基准**（如 DexGraspNet、DexYCB、OakInk 一类的任务数、物体数、手型口径），亦未提供任何可核查的数字。**任何"XX 任务 / XX 物体 / XX 手"的数字在本报告中一律不给出。** `> 待核实`

### 7.3 开放问题与失败案例

1. **灵巧抓取专用基准缺位**：候选块中无任何灵巧抓取数据集主页或论文，无法给出仿真/真机、任务数、本体口径 `> 待核实`。
2. **仿真 SOTA 与真机 SOTA 不可混谈**：现有视觉仿真基准推动明显，但真机通用策略评测滞后 [84]；[11] 的冠军结果亦为照片级仿真环境，非真机 [11]。
3. **评测与结果不可复现**：HRI 研究长期缺乏标准化基准，导致结果不可复现，M4Bench 即为针对性回应 [119]；更早的 [108] 已专门讨论连续控制深度 RL 基准任务的可复现性问题 [108]。
4. **大规模数据的基础设施瓶颈**：超大规模遥操作演示数据的 curation、分发与加载本身即瓶颈 [34]。
5. **Sim2Real 的边界与局限**：不仅存在迁移收益，也存在明确局限，需按应用域（如精准农业）审视 [106]。
6. **异构数据下的 BC 退化**：视觉偏移等异构性问题会严重削弱行为克隆 [117]，而这正是跨本体大数据的常态 [68]。
7. **触觉部署的经济性争议**：触觉在接触丰富任务中被普遍认为必要，但 HapticVLA 主张推理时可不用触觉 [90]，与 VITaL/VITaL 类"触觉预训练同时服务无触觉策略" [92] 形成同一脉络；两者与"触觉必需论"的张力 `> 待核实` 尚无独立第三方对照实验。
8. **动作分块与扩散的推理延迟**：灵巧操作对实时性敏感，而扩散迭代去噪带来高延迟 [62]——机器人域内的靶向加速证据仍不足 `> 待核实`。

---

## 八、建议关注清单（Watchlist）

按"是否可能改变范式的杠杆点"排序，附追踪理由与所需补检动作：

| # | 追踪对象 | 类型 | 追踪理由 | 需补检的证据 |
|---|---|---|---|---|
| 1 | **HapticVLA** [90] | 触觉 + VLA | "推理时不需触觉"若在多任务真机成立，将大幅降低触觉部署门槛 | 真机任务数、本体型号、与带触觉基线的对照 `> 待核实` |
| 2 | **ManipulationNet** [116] | 真机评测基础设施 | 直击"真机评测滞后"这一最大缺口 [84] | 是否开放报名、是否公开榜单与提交记录 `> 待核实` |
| 3 | **ManiFeel** [97] + **ManiSkill-ViTac 2025** [75] | 视觉触觉基准 | 目前唯一能把"触觉是否有用"变成可复现实验的两条入口 | 任务数、本体、传感器型号口径 `> 待核实` |
| 4 | **手内书写 / 实时 Jacobian 估计** [12] | 灵巧技能极限 | 以极低数据量攻克高动态手内操作，方法可迁移性强 | 真机成功率、是否开源 `> 待核实` |
| 5 | **动作分块的灵巧域改造（VQ-ACE [13]、SERNF [15]）** | 动作头 | 真机样本效率是灵巧操作落地的第一约束 | 样本数对比表、开源权重 `> 待核实` |
| 6 | **ContactWorld** [86] | 表征学习 | 回答"视觉-触觉世界模型该用什么表征"，影响所有下游策略 | 表征消融的完整表格 `> 待核实` |
| 7 | **TacEx** [102] | 触觉仿真工程栈 | 将软体仿真与视觉触觉仿真器接进 Isaac Sim，直接影响 sim2real 管线可搭建性 | 与真实 GelSight 的一致性指标 `> 待核实` |
| 8 | **双臂协同三件套 [52][53][54]** | 双臂方法主线 | "稳定 + 动作"分解已成双臂通用范式，需追踪其在 VLA 时代的演化 | 是否被 [11] 类 VLA 方案吸收 `> 待核实` |
| 9 | **Open X-Embodiment [68] / DROID [72]** | 数据 | 灵巧操作的规模化依赖跨本体数据，且受加载/分发瓶颈制约 [34] | 最新版本与下载量/榜单使用情况 `> 待核实` |
| 10 | **DexGraspNet / DexYCB / OakInk 类灵巧抓取基准** | 基准（**本次未检索到**） | 第一章至第七章反复出现的核心缺口：灵巧抓取缺少可核查的评测口径 | **必须补检一手主页**，确认任务数、物体数、手型、仿真/真机 `> 待核实` |

**Watchlist 总体证据**：**热度证据**除 [116]（citations=15）外均 `> 待核实`；**权威证据**为 arXiv 预印本与竞赛报告（B 级），[113] 为 ACM MM（A 级）；**关注度** 中；**推荐度** ★★★★☆（列出的十条均与本主题强相关，但全部需要补检第三方验证）。

---

## 参考来源

[1] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1 （**与本主题无关，检索噪声**）
[2] Dexterous Cable Manipulation: Taxonomy, Multi-Fingered Hand Design, and Long-Horizon Manipulation — http://arxiv.org/abs/2502.00396v2
[3] Learning Dexterous In-Hand Manipulation — http://arxiv.org/abs/1808.00177v5
[4] VQualA 2025 Challenge on Engagement Prediction for Short Videos — http://arxiv.org/abs/2509.02969v1 （**噪声**）
[5] Learning Complex Dexterous Manipulation with Deep RL and Demonstrations — http://arxiv.org/abs/1709.10087v2
[6] UIC-AIHealth4All at ArchEHR-QA 2026 — http://arxiv.org/abs/2608.27467v1 （**噪声**）
[7] Second MOASEI Competition at AAMAS'2026 — http://arxiv.org/abs/2607.03399v1 （**噪声**）
[8] IJCB-AFMFR 2026 — http://arxiv.org/abs/2607.24422v1 （**噪声**）
[9] Inference-Time Attention Steering for VLA Driving Models — http://arxiv.org/abs/2608.17095v1 （**噪声**）
[10] DEFT: Dexterous Fine-Tuning for Real-World Hand Policies — http://arxiv.org/abs/2310.19797v2
[11] Task adaptation of Vision-Language-Action model: 1st Place Solution for the 2025 BEHAVIOR Challenge — http://arxiv.org/abs/2512.06951v2
[12] Rapid Learning of Dexterous In-Hand Pen Writing through Real-Time Jacobian Estimation — http://arxiv.org/abs/2609.11775v1
[13] VQ-ACE: Efficient Policy Search for Dexterous Robotic Manipulation via Action Chunking Embedding — http://arxiv.org/abs/2411.03556v1
[14] Technical Report for Ego4D Long-Term Action Anticipation Challenge 2025 — http://arxiv.org/abs/2506.02550v2 （**噪声**）
[15] SERNF: Sample-Efficient Real-World Dexterous Policy Fine-Tuning — http://arxiv.org/abs/2602.09580v4
[16] Reactive Diffusion Policy: Slow-Fast Visual-Tactile Policy Learning for Contact-Rich Manipulation — http://arxiv.org/abs/2503.02881v3
[17] NTIRE 2025 Challenge on Image Super-Resolution (x4) — http://arxiv.org/abs/2504.14582v3 （**噪声**）
[18] VLSP 2025 MLQA-TSR Challenge — http://arxiv.org/abs/2510.20381v1 （**噪声**）
[19] The AudioMOS Challenge 2025 — http://arxiv.org/abs/2509.01336v1 （**噪声**）
[20] TDCOSMO 2025 — http://arxiv.org/abs/2506.03023v4 （**噪声**）
[21] TRUST 2025: SCRITA and RTSS @ RO-MAN 2025 — http://arxiv.org/abs/2509.11402v1
[22] Event-Enriched Image Analysis Grand Challenge at ACM MM 2025 — http://arxiv.org/abs/2508.18904v1 （**噪声**）
[23] LeRobot: An Open-Source Library for End-to-End Robot Learning — http://arxiv.org/abs/2602.22818v1
[24] Robot Learning: A Tutorial — http://arxiv.org/abs/2510.12403v1
[25] One-Shot Reinforcement Learning for Robot Navigation — http://arxiv.org/abs/1711.10137v2
[26] Open-Ended Learning Leads to Generally Capable Agents — http://arxiv.org/abs/2107.12808v2
[27] panda-gym: Open-source goal-conditioned environments — http://arxiv.org/abs/2106.13687v2
[28] On-Policy Robot Imitation Learning from a Converging Supervisor — http://arxiv.org/abs/1907.03423v7
[29] Facilitating Robot Learning in Virtual Environments — https://doi.org/10.3390/app15095016
[30] Wheeled Lab: Modern Sim2Real for Low-cost, Open-source Wheeled Robotics — http://arxiv.org/abs/2502.07380v2
[31] EASELAN — https://arxiv.org/abs/2510.15767 （**噪声**）
[32] Launch-Day Diffusion — https://arxiv.org/abs/2511.04453 （**噪声**）
[33] ALOHA 2: An Enhanced Low-Cost Hardware for Bimanual Teleoperation — http://arxiv.org/abs/2405.02292v1
[34] Robo-DM: Data Management for Large Robot Datasets — https://arxiv.org/abs/2505.15558
[35] Enhancing Contention Resolution ALOHA using Combining Techniques — http://arxiv.org/abs/1602.07636v3 （**同名噪声**）
[36] Overview of the IRSE track at FIRE 2025 — https://www.semanticscholar.org/paper/60c09da85437bbc91e89f23d44e471ee4ab7b2d2 （**噪声**）
[37] ALOHA: Artificial Learning of Human Attributes for Dialogue Agents — http://arxiv.org/abs/1910.08293v4 （**同名噪声**）
[38] LeVR: A Modular VR Teleoperation Framework for Imitation Learning in Dexterous Manipulation — https://arxiv.org/abs/2509.14349
[39] Mobile ALOHA — http://arxiv.org/abs/2401.02117v1
[40] SEBVS: Synthetic Event-based Visual Servoing — https://arxiv.org/abs/2508.17643
[41] Tele-Aloha — http://arxiv.org/abs/2405.14866v1
[42] Facilitating laboratory automation … — https://doi.org/10.1038/s41598-025-05670-1
[43] ALOHA Receivers … — http://arxiv.org/abs/2009.03145v1 （**同名噪声**）
[44] ALOHA Random Access … — http://arxiv.org/abs/1308.1503v1 （**同名噪声**）
[45] ALOHa: A New Measure for Hallucination — http://arxiv.org/abs/2404.02904v1 （**同名噪声**）
[46] ML4H Workshop at NeurIPS 2018 — http://arxiv.org/abs/1811.07216v2 （**噪声**）
[47] The Open Ant: A Robot Platform for RL Research — http://arxiv.org/abs/2607.18488v1
[48] Exploring Hierarchy-Aware Inverse Reinforcement Learning — http://arxiv.org/abs/1807.05037v1
[49] Value Bonuses using Ensemble Errors for Exploration in RL — http://arxiv.org/abs/2602.12375v1
[50] MAGIC and MWL monitoring of the blazar TXS 0506+056 — http://arxiv.org/abs/1909.04938v1 （**噪声**）
[51] Improved Exploration with Stochastic Policies in Deep RL — https://www.semanticscholar.org/paper/b9b4edac76e7e9e949fafaec4472715c5f3af8b6
[52] Stabilize to Act: Learning to Coordinate for Bimanual Manipulation — http://arxiv.org/abs/2309.01087v2
[53] DAIR: Disentangled Attention Intrinsic Regularization — http://arxiv.org/abs/2106.05907v4
[54] VoxAct-B: Voxel-Based Acting and Stabilizing Policy for Bimanual Manipulation — http://arxiv.org/abs/2407.04152v2
[55] Knowledge-Embedded Representation Learning — http://arxiv.org/abs/1807.00505v1 （**噪声**）
[56] Overview of AuTexTification at IberLEF 2023 — http://arxiv.org/abs/2309.11285v1 （**噪声**）
[57] Multi-entity Video Transformers — http://arxiv.org/abs/2311.10873v2 （**噪声**）
[58] Explainable ML for Public Policy — http://arxiv.org/abs/2010.14374v3 （**噪声**）
[59] Self-Supervised Correspondence in Visuomotor Policy Learning — http://arxiv.org/abs/1909.06933v1
[60] Conformal Policy Learning for Sensorimotor Control Under Distribution Shifts — http://arxiv.org/abs/2311.01457v1
[61] Policy Learning with Observational Data — http://arxiv.org/abs/1702.02896v6
[62] OnlineCache: Learning Dynamic Caching Policies for Efficient Diffusion Inference — http://arxiv.org/abs/2607.29398v1
[63] Policy Implications of Statistical Estimates — http://arxiv.org/abs/2008.10903v4 （**噪声**）
[64] Factorizing Diffusion Policies for Observation Modality Prioritization — http://arxiv.org/abs/2509.16830v1
[65] RSNA RATIC Dataset — http://arxiv.org/abs/2405.19595v1 （**噪声**）
[66] NTU-NPU System for Voice Privacy 2024 — http://arxiv.org/abs/2410.02371v1 （**噪声**）
[67] Point Transformer V3 Extreme (Waymo) — http://arxiv.org/abs/2407.15282v1 （**噪声**）
[68] Open X-Embodiment: Robotic Learning Datasets and RT-X Models — http://arxiv.org/abs/2310.08864v9
[69] ROBEL: Robotics Benchmarks for Learning with Low-Cost Robots — http://arxiv.org/abs/1909.11639v3
[70] Benchmarking Reinforcement Learning Algorithms on Real-World Robots — http://arxiv.org/abs/1809.07731v1
[71] Autonomous Improvement of Instruction Following Skills via Foundation Models — http://arxiv.org/abs/2407.20635v2
[72] DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset — http://arxiv.org/abs/2403.12945v2
[73] NTIRE 2025 KwaiSR — http://arxiv.org/abs/2504.15003v1 （**噪声**）
[74] AIM 2025 Low-light RAW Video Denoising — http://arxiv.org/abs/2508.16830v1 （**噪声**）
[75] ManiSkill-ViTac 2025: Challenge on Manipulation Skill Learning With Vision and Tactile Sensing — http://arxiv.org/abs/2411.12503v1
[76] LLM-based ambiguity detection … collaborative surgical robots — http://arxiv.org/abs/2507.11525v1
[77] Proceedings of the Dialogue Robot Competition 2023 — http://arxiv.org/abs/2312.14430v5
[78] An Introduction to Lifelong Supervised Learning — http://arxiv.org/abs/2207.04354v2
[79] LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning — http://arxiv.org/abs/2306.03310v2
[80] Latent Properties of Lifelong Learning Systems — http://arxiv.org/abs/2207.14378v1
[81] Lifelong Learning using Eigentasks — http://arxiv.org/abs/2007.06918v1
[82] Forgetting and Imbalance in Robot Lifelong Learning — http://arxiv.org/abs/2204.05893v2
[83] TAG: Task-based Accumulated Gradients — http://arxiv.org/abs/2105.05155v3
[84] Robot Policy Evaluation for Sim-to-Real Transfer: A Benchmarking Perspective — http://arxiv.org/abs/2508.11117v1
[85] OpenFact at CheckThat! 2024 — http://arxiv.org/abs/2409.02649v2 （**噪声**）
[86] ContactWorld: What Representations Matter for Vision-Tactile Latent World Models — http://arxiv.org/abs/2606.13877v3
[87] XRoboToolKit-T — http://arxiv.org/abs/2609.16437v1
[88] Tac2Motion: Contact-Aware RL with Tactile Feedback for Robotic Hand Manipulation — http://arxiv.org/abs/2509.17812v2
[89] TouchDrive: Electronics-Free Tactile Sensing Interface for Assistive Grasping — http://arxiv.org/abs/2605.06432v1
[90] HapticVLA: Contact-Rich Manipulation via VLA Model without Inference-Time Tactile Sensing — http://arxiv.org/abs/2603.15257v2
[91] Multi-Resolution Tactile Imitation Learning — http://arxiv.org/abs/2606.06281v1
[92] VITaL Pretraining: Visuo-Tactile Pretraining — http://arxiv.org/abs/2403.11898v2
[93] Visuotactile Affordances for Cloth Manipulation — http://arxiv.org/abs/2212.05108v1
[94] Learning Visuotactile Estimation and Control for Non-prehensile Manipulation — http://arxiv.org/abs/2412.13157v1
[95] FBI: Learning Dexterous In-hand Manipulation with Dynamic Visuotactile Shortcut Policy — http://arxiv.org/abs/2508.14441v1
[96] Robot Synesthesia: In-Hand Manipulation with Visuotactile Sensing — http://arxiv.org/abs/2312.01853v3
[97] ManiFeel: Benchmarking and Understanding Visuotactile Manipulation Policy Learning — http://arxiv.org/abs/2505.18472v2
[98] GelSight Svelte Hand — http://arxiv.org/abs/2309.10886v1
[99] Generation of GelSight Tactile Images for Sim2Real Learning — http://arxiv.org/abs/2101.07169v1
[100] Shape-independent Hardness Estimation Using Deep Learning and GelSight — http://arxiv.org/abs/1704.03955v1
[101] Design of a Fully Actuated Robotic Hand With Multiple GelSight Tactile Sensors — http://arxiv.org/abs/2002.02474v1
[102] TacEx

---

*Generated by research-bot · topic=`embodied-manipulation` · depth=`standard` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading · model=`deepseek-v4-flash` · sources=119 · duration=298s · 2026-10-04T22:35:37+00:00*
