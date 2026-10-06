# 具身智能·灵巧操作（Dexterous Manipulation & Grasping）证据化调研报告

**日期**：2026-10-06（UTC） ｜ **领域**：具身智能 / 灵巧操作与抓取（Dexterous Manipulation & Grasping）｜ **检索源数量**：121 条编号来源（[1]–[121]），另含 3 篇论文、4 个开源项目、3 个数据集的领域种子资源清单（无编号，凡引用处均标注 `> 待核实`）

> **阅读约定**：本文所有关键条目给出四类可核查证据——**热度**（citations / star / 下载量）、**权威**（venue / 是否同行评审 / 维护机构）、**关注度**（高 / 中 / 低 + 依据）、**推荐度**（★1–5 + 理由），均带 [n] 引用。凡检索结果未返回量化指标者，统一写 `热度：> 待核实`，**不编造任何数字或榜单**。**关注度**在缺少量化信号时，仅依据「发布时间新近度 + 主题相关性 + 可得的 venue 信息」做初判并明示依据。

---

## 摘要（Executive Summary）

1. **范式主线已从「单任务 RL / 单任务模仿」转向「VLA + 操作基础模型」**。2025 年 BEHAVIOR Challenge（50 个长程家务任务、双手机器人操作 + 导航、照片级仿真）的冠军方案即基于 Pi0.5 架构做任务适配，说明「通用 VLA 骨干 + 任务适配」已成为长程操作的主流解法 [89]。同期综述亦把灵巧操作划分为「机械编程 → 学习驱动 → 具身智能」的演进脉络 [69]。
2. **触觉/力感知进入「可归因增益」的研究阶段，但结论仍不统一**。一方面有工作主张接触感知的奖励塑形与观测融合能显著改善手内操作（装拆盖等接触丰富任务）[6]，另一方面出现明确的**反向命题**——HapticVLA 主张在**推理期不使用触觉硬件**也能完成接触丰富任务，认为触觉依赖抬高成本、损害可复现性 [9]。这类冲突是本领域当前最值得追踪的争论点。
3. **灵巧手的硬件—仿真协同设计成为新热点**：腱驱动、低成本、仿真就绪（simulation-ready）的手部平台被专门提出以支撑学习型灵巧操作 [49]；LEAP Hand 与 GelSight Svelte Hand 则代表低成本拟人手的另一条路线 [48][11]。
4. **评测与复现是最大短板**。已有工作明确指出现有视觉操作仿真基准在「通用策略的真实世界评价」上显著滞后 [120]，并出现面向真机、面向推理能力的评测协议尝试（ManipArena，citations=6）[78]。**仿真 SOTA 与真机 SOTA 不可互相替代**是本报告的基线立场。
5. **检索噪声率偏高**：本次 121 条来源中，相当比例（如 [1][2][30][31][52][71][100][101][102] 等）与灵巧操作主题无关，已在第七章集中标注，未用作任何论断依据。

---

## 一、关键前沿进展（近 1–2 年）

**1.1 通用 VLA 在长程双臂操作上的落地（2025）**
- 2025 BEHAVIOR Challenge 冠军方案：50 个多样化长程家务任务、照片级仿真、需双臂操作 + 导航 + 上下文决策；方法建立在 Pi0.5 架构之上做任务适配 [89]。
- 热度：`> 待核实`（检索未返回 citations）｜权威：arXiv cs.RO 预印本，暂未见同行评审记录 [89]｜关注度：**高**（依据：BEHAVIOR 为大规模公开挑战赛，冠军方案具强示范性）｜推荐度：**★★★★☆**（长程双臂 VLA 落地的一手证据，但需注意其评测域为仿真而非真机）。

**1.2 VLA 推理期干预（2026）**
- 通过对 pre-softmax 注意力施加有界加性偏置，在**不重训练**的前提下把注意力导向安全关键目标；该工作面向 VLA **驾驶**模型而非操作 [88]。
- 热度：`> 待核实`｜权威：arXiv cs.CV 预印本 [88]｜关注度：**中**（依据：方法层面可迁移到操作域，但本体/任务域不同）｜推荐度：**★★★☆☆**（作为「推理期免训练干预」的跨域线索阅读，直接用于灵巧操作需自行验证，`> 待核实`）。

**1.3 灵巧操作 VLA 的后训练与人机回环（2026）**
- DexHiL 提出面向灵巧操作的 VLA **human-in-the-loop 后训练**框架 [92]。
- 热度：`> 待核实`｜权威：arXiv 预印本（题录层级）[92]｜关注度：**中**（依据：后训练是通用策略落到具体灵巧硬件的关键环节，但本次仅得标题级证据）｜推荐度：**★★★☆☆**（方向关键，细节 `> 待核实`）。

**1.4 通用操作的数据瓶颈被正面处理（2025）**
- 「Generalist Robot Manipulation beyond Action Labeled Data」直面**动作标注数据难以规模化**这一核心瓶颈 [74]。
- 热度：`> 待核实`｜权威：arXiv cs.RO 预印本 [74]｜关注度：**中高**（依据：数据规模化是通用操作公认卡点）｜推荐度：**★★★★☆**（若关注「非动作标注数据」路线，属必读）。

**1.5 手内操作的高效学习（2026）**
- 通过**实时 Jacobian 估计**实现拟人手手内转笔（in-hand pen writing）的快速学习，试图绕开接触丰富、高动态交互通常所需的繁重建模或大数据采集 [29]。
- 热度：`> 待核实`｜权威：arXiv cs.RO 预印本 [29]｜关注度：**中**（依据：手内书写是典型 high-DoF 接触丰富任务，属新近预印本）｜推荐度：**★★★★☆**（手内操作少见的「免大规模数据」路线样本）。

**1.6 综述级图景（2025）**
- 《The Developments and Challenges towards Dexterous and Embodied Robotic Manipulation: A Survey》总结从机械编程到具身智能的演进与挑战 [69]；《Interactive Imitation Learning for Dexterous Robotic Manipulation》聚焦交互式模仿学习的挑战与展望 [70]；《Large VLM-based Vision-Language-Action Models for Robotic Manipulation: A Survey》提供 VLA 侧图景 [81]。
- 热度：均 `> 待核实`｜权威：均为 arXiv 预印本 [69][70][81]｜关注度：**中高**（依据：综述通常是进入该方向的入口文献）｜推荐度：**★★★★☆**（[69][70] 与本主题相关度最高，作为分类骨架使用）。

**1.7 仿真与工程底座更新（2025–2026）**
- Isaac Lab 作为 Isaac Gym 的继任者，把 GPU 原生机器人仿真扩展到大规模多模态学习，融合 GPU 并行物理、照片级渲染与模块化架构 [53]；LeRobot 提供端到端机器人学习开源库 [56]；LabDex 提出实验室场景的层次化灵巧操作基准 [55]。
- 热度：`> 待核实`｜权威：arXiv cs.RO 预印本 [53][55][56]；Isaac Lab 由 NVIDIA 系生态维护（本体属工程系统，官方文档为补充权威，本次未检索到）[53]｜关注度：**高**（依据：训练栈与开源库是社区基础设施，使用面广；但 star/下载量 `> 待核实`）｜推荐度：**★★★★★（工程选型用途）**（[53][56] 为搭建训练/部署链路的首选起点）。

---

## 二、模仿学习与扩散/动作分块策略

**2.1 动作分块 + 低成本双臂硬件（ACT/ALOHA，奠基）**
- 「Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware」解决扎带穿线、电池插槽等精细双臂任务——这类任务需要精度、接触力协调与闭环视觉反馈，传统上依赖高端机器人或高精度传感器 [41]。
- **热度：citations=2589** [41]｜权威：**Robotics: Science and Systems (RSS)** 会议论文（同行评审，A 级）[41]｜关注度：**高**（依据：citations=2589）[41]｜推荐度：**★★★★★**（本方向模仿学习的基石论文与事实标准基线）。

**2.2 扩散策略的推理效率问题被单列研究（2026）**
- OnlineCache 针对扩散模型迭代去噪的高延迟，提出**动态缓存策略 + 误差校正**，指出既有缓存方法依赖静态、与样本无关的调度 [47]。
- 热度：`> 待核实`｜权威：arXiv cs.LG 预印本 [47]｜关注度：**中**（依据：扩散策略推理延迟是落地痛点，但该工作为通用生成模型加速，非机器人专用）｜推荐度：**★★★☆☆**（若需部署高频扩散策略可关注，需自行验证机器人域适用性，`> 待核实`）。

**2.3 ACT 的工程化改进（2025）**
- 「Enhancement of Position Accuracy via DPB-Embedded ACT Model」在 ACT 中嵌入 DPB 以改善精细操作的位置精度 [43]。
- **热度：citations=0** [43]｜权威：*Applied and Computational Engineering*（非机器人顶会/顶刊，权威性弱）[43]｜关注度：**低**（依据：citations=0）[43]｜推荐度：**★★☆☆☆**（作为 ACT 精度改进的工程参考，但证据等级低，结论不可外推）。

**2.4 抓取预训练增强模仿策略（2025）**
- GPA-RAM（Grasp-Pretraining Augmented Robotic Attention Mamba）把任务演示中的抓取先验注入模仿策略，**不额外采集抓取位姿数据**，以缓解初始抓取不准导致的误差传播 [46]。
- **热度：citations=1** [46]｜权威：arXiv.org 预印本 [46]｜关注度：**低**（依据：citations=1）[46]｜推荐度：**★★★★☆**（首次抓取误差传播是精细操作的真实失败模式，该切入点有价值）。

**2.5 力/功感知的模仿学习（2026）**
- 「Energy-Regularized Imitation Learning for Force- and Work-Aware Robotic Manipulation」以能量正则化把力/功纳入模仿学习 [20]。
- 热度：`> 待核实`｜权威：arXiv 预印本（题录级）[20]｜关注度：**中**（依据：力感知与接触丰富操作强相关）｜推荐度：**★★★☆☆**（与第四章触觉路线互补）。

**2.6 经典模仿学习脉络（作为对照基线）**
- Self-Supervised Correspondence in Visuomotor Policy Learning [42]、On-Policy Robot Imitation Learning from a Converging Supervisor [59]、交互式模仿学习综述 [70] 构成从「表征对齐 → 数据效率 → 交互式改进」的线索；[57] 为机器人学习教程。
- 热度：均 `> 待核实`（[42][59][57]）｜权威：arXiv 预印本 [42][59][57]；[70] 为综述 [70]｜关注度：**低–中**（依据：无量化指标；[57] 为教学性质）｜推荐度：**★★★☆☆**（作为方法演进背景阅读）。

> **待核实**：领域种子清单中的 *Diffusion Policy: Visuomotor Policy Learning via Action Diffusion*（RSS 2023, https://arxiv.org/abs/2303.04137）与 *QT-Opt*（CoRL 2018, https://arxiv.org/abs/1806.10293）在本轮 121 条编号来源中**无对应编号**，故本文不对其给出 [n] 引用、也不对其宣称任何指标，仅作为种子资源列于第六章表格并标注待核实。

---

## 三、灵巧手与手内操作

**3.1 手内操作 RL 的源头与延续**
- OpenAI「Learning Dexterous In-Hand Manipulation」用 RL 在物理 Shadow Dexterous Hand 上完成**基于视觉的物体重定向**，训练在仿真中进行并对系统物理属性做域随机化 [25]；更早的「Learning Complex Dexterous Manipulation with Deep RL and Demonstrations」把演示与深度 RL 结合 [27]。
- 热度：`> 待核实`（[25][27] 检索未返回 citations）｜权威：arXiv [25][27]（[25] 标为 cs.LG）[25]｜关注度：**高**（依据：作为域随机化 + 手内操作 RL 的奠基范式，长期被该方向引用；具体引用数 `> 待核实`）｜推荐度：**★★★★★**（理解 sim2real 随机化与手内操作目标函数的必读起点）。

**3.2 快速学习手内书写（2026）**
- 通过实时 Jacobian 估计减少对建模与非同构数据采集的依赖，实现在拟人手上的手内转笔书写 [29]。四类证据见 1.5。

**3.3 低成本拟人手平台**
| 平台 | 关键点 | 证据 |
|---|---|---|
| LEAP Hand | 低成本、高效、拟人手，面向机器人学习 [48] | 热度 `> 待核实`；权威 arXiv 预印本 [48]；关注度 中（依据：无量化指标，仅按平台类工作相关性初判）；推荐度 ★★★★☆（低成本拟人手复现的常见选型） |
| GelSight Svelte Hand | 三指、两自由度、触觉丰富、低成本，面向灵巧操作 [11] | 热度 `> 待核实`；权威 arXiv 预印本 [11]；关注度 中；推荐度 ★★★★☆（触觉 + 低成本手硬件组合） |
| Aero Hand Open | 腱驱动、**仿真就绪**，论证把执行器移出关节可显著降本 [49] | 热度 `> 待核实`；权威 arXiv cs.RO [49]；关注度 中；推荐度 ★★★★☆（首个强调「仿真就绪」的手部平台之一，利于 sim2real 流水线） |

**3.4 手内操作的数据与迁移**
- DEFT（Dexterous Fine-Tuning）面向真实世界手部策略的微调 [32]；Progressive Transfer Learning 面向多指拟人手的手内操作渐进迁移 [87]；Tilde 使用 DeltaHand 做手内操作遥操作数据采集 [86]；«Dexterous Cable Manipulation» 给出线缆操作分类学 + 多指手设计 + 长程操作 [26]。
- 热度：均 `> 待核实`｜权威：均为 arXiv 预印本 [32][86][87][26]｜关注度：**中**（依据：数据采集与迁移是手内操作的核心工程瓶颈，但无量化指标）｜推荐度：**★★★★☆**（[86] 遥操作采数、[32] 真机微调两条路线最值得细读，具体数字 `> 待核实`）。

**3.5 整手抓取的实时力调控（2026）**
- 指出预计算力分布在物体运动、建模误差或外部扰动下容易失效，提出**整手实时力调节**框架以维持物理稳定 [50]。
- 热度：`> 待核实`｜权威：arXiv cs.RO [50]｜关注度：**中高**（依据：抓取稳定性是灵巧操作的前置条件）｜推荐度：**★★★★☆**（从「力分配静态化」失败模式切入，问题定义清晰）。

**3.6 抓取与运动规划**
- «Grasp and Motion Planning for Dexterous Manipulation for the Real Robot Challenge» 针对真实机器人挑战赛给出抓取与运动规划方案 [121]；Humanoid Manipulation Interface 用「无机器人演示」驱动机器人全身操作 [85]。
- 热度：`> 待核实`｜权威：arXiv 预印本 [121][85]｜关注度：**中**（依据：[121] 属挑战赛方案，[85] 属人形全身操作新方向）｜推荐度：**★★★☆☆**（作为规划侧与全身操作侧的对照）。

---

## 四、接触丰富任务与触觉/力感知

**4.1 触觉表征的「哪种表征有用」被系统化（2026）**
- ContactWorld 指出视觉与触觉观测捕获物理交互的不同侧面，其效用**关键取决于表征方式**，并构建受控基准与实证研究 [4]。
- 热度：`> 待核实`｜权威：arXiv cs.RO [4]｜关注度：**高**（依据：把「触觉是否有用」转化为「何种表征下有用」，是该争论的关键方法论进展）｜推荐度：**★★★★★**（本报告最推荐的触觉表征阅读对象）。

**4.2 触觉 RL 的奖励塑形与观测融合（2025）**
- Tac2Motion 提出基于触觉的**奖励塑形**，并把触觉并入观测空间，面向开盖等接触丰富手内操作 [6]。
- 热度：`> 待核实`｜权威：arXiv cs.RO [6]｜关注度：**中高**（依据：直接针对手内接触丰富任务的 RL 方案）｜推荐度：**★★★★☆**（触觉进入 RL 奖励设计的可核查样本）。

**4.3 反向命题：推理期不用触觉（2026）**
- HapticVLA 明确主张：对触觉硬件的依赖增加成本、降低跨平台可复现性，因此提出**推理期无需触觉传感**的 VLA 方案完成接触丰富操作 [9]。
- 热度：`> 待核实`｜权威：arXiv cs.RO [9]｜关注度：**高**（依据：与 4.2 及主流触觉投入方向形成直接张力，属可辩之争）｜推荐度：**★★★★★**（与 [4][6] 对读可构成「触觉增益是否可归因」的三角验证）。
- **争议处理**：[6] 与 [9] 结论相左，二者均为 arXiv 预印本、同一证据等级，**暂不采信任一方**；判定需要第三方复现或统一基准，当前 `> 待核实`。

**4.4 多传感器异构触觉融合（2026）**
- Multi-Resolution Tactile Imitation Learning 指出异构触觉传感器的融合利用仍被低估，提出多分辨率触觉模仿学习 [10]。
- 热度：`> 待核实`｜权威：arXiv cs.RO [10]｜关注度：**中**（依据：填补「单一触觉传感器」假设的空白）｜推荐度：**★★★★☆**。

**4.5 触觉数据采集与人机演示**
- MimicTouch 利用**多模态人类触觉演示**做接触丰富操作 [8]；XRoboToolKit-T 针对现有采数方案难以获得稳定高频触觉反馈的问题，提出高稳定高精度带触觉遥操作 [5]。
- 热度：`> 待核实`｜权威：arXiv 预印本 [8][5]（[5] 为 cs.RO）[5]｜关注度：**中高**（依据：触觉数据采集是触觉策略规模化的前置瓶颈）｜推荐度：**★★★★☆**（[5] 的「高频稳定触觉」是常被忽略但关键的工程指标）。

**4.6 视觉触觉传感器（GelSight 系）的仿真与建模链条**
- 该链条可辨识为：接触事件检测与预测 [16] → GelSight 触觉图像的 sim2real 生成 [17] → 基于样例的 GelSight 仿真模型 Taxim [19] → 模块化 GelSight 传感器设计 [13] → Isaac Sim 内 GelSight 触觉仿真 TacEx（软体 + 视觉触觉仿真器结合）[14] → 指尖级传感器 Minsight [18]。
- 热度：均 `> 待核实`｜权威：均为 arXiv 预印本 [16][17][19][13][14][18]｜关注度：**中高**（依据：构成触觉 sim2real 的完整工具链，被后续工作反复复用）｜推荐度：**★★★★☆**（[19] 与 [17] 是仿真侧核心；[13] 是硬件侧）。
- 低成本的触觉遥操作亦有对应工作：通过视觉触觉传感器提供力反馈 [15]。热度 `> 待核实`｜权威 arXiv [15]｜关注度 中｜推荐度 ★★★☆☆。

**4.7 触觉基准与挑战赛**
- ManiSkill-ViTac 2025 为「视觉 + 触觉」的操作技能学习挑战赛 [3]（同一文献在 [12] 以另一 URL 重复出现，属**条目重复**，非两项独立证据）。
- 热度：`> 待核实`｜权威：arXiv 预印本 [3][12]｜关注度：**中高**（依据：公开挑战赛通常形成可比基线）｜推荐度：**★★★★☆**（触觉操作少有的统一评测入口）。

**4.8 力/接触优化与仿真可靠性**
- 接触丰富操作的引导式策略搜索可上溯到 Guided Policy Search [23]；仿真侧则出现对**可微物理优化数值可靠性**的质疑性研究，指出其用于机器人材料操作时的数值可靠性问题 [84]。
- 热度：`> 待核实`｜权威：arXiv 预印本 [23][84]｜关注度：**中**（依据：[84] 触及可微仿真这一热门工具的可信度边界）｜推荐度：**★★★★☆**（[84] 属于对主流工具链的**负面/审慎证据**，价值高于增量改进）。

---

## 五、双臂协同与 sim2real

**5.1 双臂精细操作的开源起点与迭代**
- ACT/ALOHA 定义「低成本硬件 + 动作分块模仿学习」的双臂精细操作范式 [41]（热度 citations=2589，RSS 2023）[41]。
- 后续硬件与算法迭代：ALOHA 2 增强型低成本双臂遥操作 [33]、Mobile ALOHA 全身移动双臂遥操作 [36]、Stabilize to Act 学习「稳定—执行」的协调 [34]、DAIR 用解耦注意力内在正则化提升双臂操作的安全与效率 [35]、VoxAct-B 基于体素的「执行 + 稳定」策略 [37]。
- 热度：均 `> 待核实`（[33][34][35][36][37]）｜权威：均为 arXiv 预印本 [33][34][35][36][37]｜关注度：**高–中**（依据：[33][36] 因 ALOHA 生态被广泛复现，实际 star/引用 `> 待核实`；[34][35][37] 关注度中）｜推荐度：**★★★★☆**（[33][36] 为硬件与遥操作事实基准；[34][35][37] 为双臂协调的算法型线索）。

**5.2 双臂长程操作的 VLA 化（2026）**
- LatentVLA 直面「扩散模型运动保真度 vs 逆动力学模型数据可扩展性」的取舍，指出后者学到的潜在动作空间常与物理现实脱节，并提出驯化潜空间以支撑可泛化长程双臂操作 [80]。
- **热度：citations=4** [80]｜权威：**AAAI Conference on Artificial Intelligence**（同行评审，A 级）[80]｜关注度：**低**（依据：citations=4，发表时间新近）[80]｜推荐度：**★★★★☆**（顶会 + 直指潜在动作空间失配这一真实缺陷；引用尚少属时滞）。

**5.3 sim2real：从「随机化」到「表征预训练」**
- 已有工作主张用**视觉编码器预训练**弥合 visuomotor 策略迁移的 sim2real 差距 [67]；同时有工作明确指出 sim2real 在精密操作（农业场景）中的**重要性有限、局限明显** [68]。
- 热度：均 `> 待核实`｜权威：arXiv 预印本 [67][68]｜关注度：**中**（依据：[67] 为可操作的技术路线，[68] 为限定性反证）｜推荐度：**★★★★☆**（[67][68] 应成对阅读：前者给方案，后者给边界条件）。

**5.4 评测口径的滞后被公开指出**
- 「Robot Policy Evaluation for Sim-to-Real Transfer: A Benchmarking Perspective」明确指出现有视觉操作仿真基准虽推动了研究，但**机器人本质是真实世界问题，通用策略的真实世界评价显著滞后** [120]。
- 热度：`> 待核实`｜权威：arXiv cs.RO [120]｜关注度：**高**（依据：直击「仿真 SOTA ≠ 真机 SOTA」这一全领域共识性痛点）[120]｜推荐度：**★★★★★**（做基线选型与结果解读前应先读）。

**5.5 跨本体规模化假设的检验**
- «Towards Embodiment Scaling Laws in Robot Locomotion» 检验「增加训练本体数量可提升对未见本体的泛化」这一假设 [77]。
- 热度：`> 待核实`｜权威：arXiv cs.RO [77]｜关注度：**中高**（依据：跨本体泛化是通用策略的前提假设）｜推荐度：**★★★☆☆**（任务域为**运动 locomotion 而非操作**，迁移到灵巧操作需谨慎，`> 待核实`）。

---

## 六、经典与奠基性工作

> 表中「热度」凡标 `> 待核实` 者，表示本轮检索未返回 citations/star 等量化指标；「关注度」为在可得信号基础上的编辑判断，依据已在括号内说明。种子资源条目无 [n] 编号，其指标一律 `> 待核实`。

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Learning Dexterous In-Hand Manipulation | 2018 | OpenAI（arXiv, 标 cs.LG）[25] | `> 待核实` | arXiv 预印本 [25] | 高（手内操作 RL + 域随机化奠基范式；引用数 `> 待核实`） | ★★★★★ | http://arxiv.org/abs/1808.00177v5 | 仿真域随机化 + 视觉物体重定向 [25] |
| Learning Complex Dexteruous Manipulation with Deep RL and Demonstrations | 2017 | arXiv [27] | `> 待核实` | arXiv 预印本 [27] | 中高（演示 + RL 结合的代表作） | ★★★★☆ | http://arxiv.org/abs/1709.10087v2 | 演示引导的复杂灵巧操作 [27] |
| Learning Contact-Rich Manipulation Skills with Guided Policy Search | 2015 | arXiv [23] | `> 待核实` | arXiv 预印本 [23] | 中（接触丰富操作策略搜索的早期代表） | ★★★★☆ | http://arxiv.org/abs/1501.05611v2 | 引导式策略搜索用于接触丰富技能 [23] |
| Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware (ACT/ALOHA) | 2023 | RSS [41] | **citations=2589** [41] | **RSS 会议论文（同行评审）** [41] | **高**（citations=2589）[41] | ★★★★★ | https://arxiv.org/abs/2304.13705 | 低成本双臂 + 动作分块模仿学习基石 [41] |
| Open X-Embodiment: Robotic Learning Datasets and RT-X Models | 2023 | arXiv（多机构协作）[103] | `> 待核实` | arXiv 预印本 [103] | 高（跨本体数据集整合与 RT-X 模型，被广泛作为预训练起点） | ★★★★★ | http://arxiv.org/abs/2310.08864v9 | 数据与模型双重整合的奠基工作 [103] |
| Towards Learning to Detect and Predict Contact Events on Vision-based Tactile Sensors | 2019 | arXiv [16] | `> 待核实` | arXiv 预印本 [16] | 中（接触事件检测的基础工作） | ★★★★☆ | http://arxiv.org/abs/1910.03973v1 | 视觉触觉传感器的接触事件检测与预测 [16] |
| Generation of GelSight Tactile Images for Sim2Real Learning | 2021 | arXiv [17] | `> 待核实` | arXiv 预印本 [17] | 中高（触觉 sim2real 图像生成的关键工具） | ★★★★☆ | http://arxiv.org/abs/2101.07169v1 | GelSight 触觉图像生成以支撑 sim2real [17] |
| Taxim: An Example-based Simulation Model for GelSight Tactile Sensors | 2021 | arXiv [19] | `> 待核实` | arXiv 预印本 [19] | 中高（GelSight 仿真的事实标准之一） | ★★★★☆ | http://arxiv.org/abs/2109.04027v2 | 基于样例的 GelSight 仿真模型 [19] |
| Self-Supervised Correspondence in Visuomotor Policy Learning | 2019 | arXiv [42] | `> 待核实` | arXiv 预印本 [42] | 中（表征对齐路线的代表） | ★★★☆☆ | http://arxiv.org/abs/1909.06933v1 | 自监督对应关系用于视觉运动策略 [42] |
| Grasp and Motion Planning for Dexterous Manipulation for the Real Robot Challenge | 2021 | arXiv [121] | `> 待核实` | arXiv 预印本 [121] | 中（挑战赛方案，工程参考） | ★★★☆☆ | http://arxiv.org/abs/2101.02842v1 | 真实机器人挑战赛的抓取与运动规划 [121] |
| Diffusion Policy: Visuomotor Policy Learning via Action Diffusion | 2023 | RSS | `> 待核实` | 种子清单标注 RSS（**本轮无 [n] 编号**，`> 待核实`） | 高（扩散策略奠基，领域共识；量化指标待核实） | ★★★★★ | https://arxiv.org/abs/2303.04137 | 扩散策略奠基；引用编号 `> 待核实` |
| QT-Opt: Scalable Deep RL for Vision-Based Robotic Manipulation | 2018 | CoRL | `> 待核实` | 种子清单标注 CoRL（**本轮无 [n] 编号**，`> 待核实`） | 中高（视觉抓取 RL 代表；量化指标待核实） | ★★★★☆ | https://arxiv.org/abs/1806.10293 | 视觉抓取 RL；引用编号 `> 待核实` |

---

## 七、数据集、基准与开放问题

### 7.1 数据集与基准对比

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Open X-Embodiment (RT-X) | 2023 | 多机构 [103] | `> 待核实` | arXiv 预印本 [103] | 高（跨本体整合，通用策略预训练入口） | ★★★★★ | http://arxiv.org/abs/2310.08864v9 | 大规模跨本体机器人学习数据集 + RT-X 模型 [103] |
| DROID: Large-Scale In-The-Wild Robot Manipulation Dataset | 2024 | arXiv [107] | `> 待核实` | arXiv 预印本（题录级）[107] | 中高（大规模野外操作数据，常与 OX-Embodiment 并用） | ★★★★☆ | http://arxiv.org/abs/2403.12945v2 | 野外场景大规模操作数据 [107] |
| LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning | 2023 | arXiv [114] | `> 待核实` | arXiv 预印本（题录级）[114] | 中高（终身学习/知识迁移基准） | ★★★★☆ | http://arxiv.org/abs/2306.03310v2 | 面向知识迁移的终身机器人学习基准 [114] |
| ManiSkill-ViTac 2025 Challenge | 2024/2025 | arXiv [3][12] | `> 待核实` | arXiv 预印本 [3][12] | 中高（视觉 + 触觉操作挑战赛） | ★★★★☆ | http://arxiv.org/abs/2411.12503v1 | 视觉与触觉联合的操作技能学习挑战 [3]（[12] 为同文重复条目） |
| LabDex | 2026 | arXiv [55] | `> 待核实` | arXiv cs.RO [55] | 中（实验室场景层次化基准，新近发布） | ★★★★☆ | http://arxiv.org/abs/2608.18618v1 | 面向实验室器皿与长程状态依赖流程的灵巧操作基准 [55] |
| ManipArena | 2026 | arXiv [78] | **citations=6** [78] | arXiv（编号缺失，`> 待核实`）[78] | 中（citations=6，真机评测稀缺，故相对突出）[78] | ★★★☆☆ | https://arxiv.org/abs/2603.28545 | 真实世界推理导向通用操作评测 [78] |
| Benchmarking Simulated Robotic Manipulation through a Real World Dataset | 2019 | arXiv [79] | `> 待核实` | arXiv 预印本 [79] | 中（仿真—真机对照评测的早期尝试） | ★★★☆☆ | http://arxiv.org/abs/1911.01557v2 | 用真机数据集检验仿真基准 [79] |
| Robot Policy Evaluation for Sim-to-Real Transfer: A Benchmarking Perspective | 2025 | arXiv [120] | `> 待核实` | arXiv cs.RO [120] | 高（直指评测滞后于真机需求） | ★★★★★ | http://arxiv.org/abs/2508.11117v1 | 通用策略真实世界评测的方法论讨论 [120] |
| RoboMimic | — | 种子清单 | `> 待核实` | **本轮无 [n] 编号**，`> 待核实` | 中高（模仿学习常用基准；量化指标待核实） | ★★★★☆ | https://robomimic.github.io/ | 模仿学习基准；引用编号 `> 待核实` |
| BridgeData V2 | — | 种子清单 | `> 待核实` | **本轮无 [n] 编号**，`> 待核实` | 中高（大规模操作数据；量化指标待核实） | ★★★★☆ | https://rail-berkeley.github.io/bridgedata/ | 大规模操作数据；引用编号 `> 待核实` |
| DexGraspNet / DexArt | — | 种子清单 | `> 待核实` | **本轮无 [n] 编号**，`> 待核实` | 中（灵巧抓取数据；量化指标待核实） | ★★★☆☆ | https://github.com/PKU-EPIC/DexGraspNet | 灵巧抓取数据；引用编号 `> 待核实` |
| SimplerEnv / RoboArena | — | — | `> 待核实` | **本轮检索未获得任何对应编号来源** | `> 待核实` | `> 待核实` | `> 待核实` | 在子问题中被提及，但本轮 121 条来源中**无对应文献**，故不对其规模、口径作任何陈述 |

**口径提醒**：上表中 **Open X-Embodiment / DROID / LIBERO / ManiSkill-ViTac** 的更细粒度信息（任务数、本体数、是否含触觉通道、是否支持双臂/灵巧手）**在本次可用证据中不足以核实**，一律 `> 待核实`，不做推测性描述。

### 7.2 开放问题与争议

1. **触觉的增益是否可归因？** [4] 把问题转化为「何种表征下有用」，[6] 主张触觉奖励塑形与观测融合有效，[9] 主张推理期可完全不用触觉。三者证据等级相同（arXiv 预印本），**冲突未解**，需统一基准与第三方复现 [4][6][9]。
2. **动作标注数据的规模化瓶颈**。[74] 明确指出既有方法依赖高质量动作标注演示，这是通用操作的核心约束 [74]；[103] 的跨本体整合是当前主要应对方式 [103]。
3. **仿真 SOTA ≠ 真机 SOTA**。[120] 指出真实世界通用策略评测显著滞后 [120]；[78] 尝试建立真机、推理导向的评测协议（citations=6）[78]；[79] 早已尝试用真机数据集检验仿真基准 [79]。
4. **可微物理与仿真可信度**。[84] 对可微物理优化用于机器人材料操作的**数值可靠性**提出质疑，属对主流工具链的负面证据 [84]。
5. **跨本体泛化的可扩展性假设仍需检验**。[77] 在运动域检验本体系规模律，操作域是否有同类规律 `> 待核实` [77]。
6. **仿真策略向真机迁移的表征侧方案与边界**。[67] 给方案（视觉编码器预训练），[68] 给边界（sim2real 在精密操作中重要性有限）[67][68]。
7. **手内操作的数据效率**。[29] 试图用实时 Jacobian 估计绕开大数据/重建模，此类「免大数据」路线的可扩展性 `> 待核实` [29]。
8. **灵巧手硬件的成本—仿真保真度张力**。[49] 以腱驱动 + 执行器外置降本并强调仿真就绪，[11][48] 提供低成本替代；三者之间**尚无统一硬件评测口径** `> 待核实` [49][11][48]。
9. **复现困难与失败案例披露不足**。本报告未检索到关于灵巧操作复现失败的专门研究或负面结果报告，此项 `> 待核实`，属本领域证据缺口。

### 7.3 检索噪声与不可用证据说明（诚实性声明）

本轮 121 条来源中，以下条目与灵巧操作/抓取主题**无关或仅弱相关**，**未被用作任何论断依据**，列出以避免读者误判证据总量：[1]（短视频参与度预测）、[2]（基础模型透明度指数）、[21]（接入点建模）、[22]（公共政策可解释 ML）、[24]（LeWiDi 立场建模）、[28]（ML4H workshop）、[30]（PIRM 超分挑战）、[31]（持续学习开放问题）、[38]（细粒度图像识别）、[39]（AuTexTification）、[40]（视频 Transformer）、[52]（微分对策最优控制）、[61]（多机器人协作综述）、[62]（绳结解缠，弱相关）、[63]（欺骗博弈与安全）、[64]（GitHub 应用流行度）、[65][66]（GitHub 开发者研究）、[71]（暗能量）、[72][73]（拜占庭容错 SGD / 分布式优化）、[75]（遥感布局生成）、[76]（Dalorex 体系结构）、[82][83]（农业机器人/农业 5.0，属邻域）、[90]（装配动作理解，邻域）、[93]–[99]（IR 评测、德语问卷、超分、宇宙学、AGN、越南法律 QA、AudioMOS）、[100][101]（RSNA 医学影像数据集）、[102][104]（对话机器人竞赛）、[105]（量子系统 Krotov 算法）、[106]（文档信息抽取）、[108]（音频-视觉操作，邻域）、[109]（语音隐私）、[110]（Waymo 语义分割）、[111]（选举话语数据集）、[112]（引力波讲义）、[113][115]–[119]（终身学习理论/持续学习）。此外 [3] 与 [12] 为**同一文献的重复条目**，不构成独立证据 [3][12]。

---

## 八、建议关注清单（Watchlist）

**A. 必读核心（先读这 8 篇）**
1. [41] ACT/ALOHA（RSS 2023, citations=2589）——模仿学习基线事实标准 [41]。
2. [25] Learning Dexterous In-Hand Manipulation——手内操作 RL + 域随机化范式源头 [25]。
3. [103] Open X-Embodiment / RT-X——跨本体数据与模型整合 [103]。
4. [4] ContactWorld——「触觉在哪类表征下有用」的受控基准 [4]。
5. [9] HapticVLA——「推理期不用触觉」的反向命题 [9]（与 [6] 对读）。
6. [120] Sim-to-Real 策略评测的基准视角 [120]。
7. [69] 灵巧与具身操作综述——分类骨架 [69]。
8. [89] 2025 BEHAVIOR Challenge 冠军方案——通用 VLA 落到长程双臂任务 [89]。

**B. 方法线索（按主题）**
- 潜空间与双臂长程：[80]（AAAI 2026, citations=4）[80]。
- 触觉仿真与 sim2real 工具链：[19][17][14][13][16][18]。
- 触觉数据采集与遥操作：[5][8][15][86]。
- 手部硬件：[49][48][11][50]。
- 训练/软件栈：[53][56]。
- 数据效率与非动作标注数据：[74][29]。
- 评测与真机验证：[78][79][77]（注意 [77] 为运动域）[78][79][77]。

**C. 明确待核实事项（不得据本报告下结论）**
- 所有 `热度：> 待核实` 条目的 citations/star 数字；
- 种子资源（Diffusion Policy、QT-Opt、RoboMimic、BridgeData V2、DexGraspNet/DexArt）的引用编号与量化指标；
- SimplerEnv 与 RoboArena 的任何规模/口径描述（本轮**无来源**）；
- Open X-Embodiment / DROID / LIBERO 是否原生支持灵巧手、双臂与触觉通道；
- 触觉增益之争（[6] vs [9]）的最终判定，需第三方复现或统一基准。

**D. 三个月内应复查的问题**
1. [4][6][9] 三方是否出现同一基准上的可比结果；
2. [78] ManipArena（citations=6）是否形成后续引用与独立复现；
3. [80] LatentVLA 在 AAAI 2026 后是否公开代码与真机结果（`> 待核实`）；
4. [49] Aero Hand Open 的「仿真就绪」宣称是否有第三方复现（`> 待核实`）；
5. [89] BEHAVIOR 冠军方案是否迁移到真机（`> 待核实`）。

---

## 参考来源

[1] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1
[2] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1
[3] ManiSkill-ViTac 2025: Challenge on Manipulation Skill Learning With Vision and Tactile Sensing — http://arxiv.org/abs/2411.12503v1
[4] ContactWorld: What Representations Matter for Vision-Tactile Latent World Models in Contact-Rich Manipulation — http://arxiv.org/abs/2606.13877v3
[5] XRoboToolKit-T: Teleoperation with High Stability and Precision with Tactile Sensing for Contact-rich Manipulation — http://arxiv.org/abs/2609.16437v1
[6] Tac2Motion: Contact-Aware Reinforcement Learning with Tactile Feedback for Robotic Hand Manipulation — http://arxiv.org/abs/2509.17812v2
[7] TouchDrive: Electronics-Free Tactile Sensing Interface for Assistive Grasping — http://arxiv.org/abs/2605.06432v1
[8] MimicTouch: Leveraging Multi-modal Human Tactile Demonstrations for Contact-rich Manipulation — http://arxiv.org/abs/2310.16917v4
[9] HapticVLA: Contact-Rich Manipulation via Vision-Language-Action Model without Inference-Time Tactile Sensing — http://arxiv.org/abs/2603.15257v2
[10] Multi-Resolution Tactile Imitation Learning for Contact-Rich Robotic Manipulation — http://arxiv.org/abs/2606.06281v1
[11] GelSight Svelte Hand: A Three-finger, Two-DoF, Tactile-rich, Low-cost Robot Hand for Dexterous Manipulation — http://arxiv.org/abs/2309.10886v1
[12] ManiSkill-ViTac 2025: Challenge on Manipulation Skill Learning With Vision and Tactile Sensing — https://arxiv.org/abs/2411.12503
[13] A Modularized Design Approach for GelSight Family of Vision-based Tactile Sensors — http://arxiv.org/abs/2504.14739v1
[14] TacEx: GelSight Tactile Simulation in Isaac Sim -- Combining Soft-Body and Visuotactile Simulators — http://arxiv.org/abs/2411.04776v1
[15] Low-Cost Teleoperation with Haptic Feedback through Vision-based Tactile Sensors for Rigid and Soft Object Manipulation — http://arxiv.org/abs/2403.16764v1
[16] Towards Learning to Detect and Predict Contact Events on Vision-based Tactile Sensors — http://arxiv.org/abs/1910.03973v1
[17] Generation of GelSight Tactile Images for Sim2Real Learning — http://arxiv.org/abs/2101.07169v1
[18] Minsight: A Fingertip-Sized Vision-Based Tactile Sensor for Robotic Manipulation — http://arxiv.org/abs/2304.10990v1
[19] Taxim: An Example-based Simulation Model for GelSight Tactile Sensors — http://arxiv.org/abs/2109.04027v2
[20] Energy-Regularized Imitation Learning for Force- and Work-Aware Robotic Manipulation — http://arxiv.org/abs/2609.18164v1
[21] A Simulation and Modeling of Access Points with Definition Language — http://arxiv.org/abs/1304.1836v2
[22] Explainable Machine Learning for Public Policy: Use Cases, Gaps, and Research Directions — http://arxiv.org/abs/2010.14374v3
[23] Learning Contact-Rich Manipulation Skills with Guided Policy Search — http://arxiv.org/abs/1501.05611v2
[24] DeMeVa at LeWiDi-2025: Modeling Perspectives with In-Context Learning and Label Distribution Learning — http://arxiv.org/abs/2509.09524v1
[25] Learning Dexterous In-Hand Manipulation — http://arxiv.org/abs/1808.00177v5
[26] Dexterous Cable Manipulation: Taxonomy, Multi-Fingered Hand Design, and Long-Horizon Manipulation — http://arxiv.org/abs/2502.00396v2
[27] Learning Complex Dexterous Manipulation with Deep Reinforcement Learning and Demonstrations — http://arxiv.org/abs/1709.10087v2
[28] Machine Learning for Health (ML4H) Workshop at NeurIPS 2018 — http://arxiv.org/abs/1811.07216v2
[29] Rapid Learning of Dexterous In-Hand Pen Writing through Real-Time Jacobian Estimation — http://arxiv.org/abs/2609.11775v1
[30] The 2018 PIRM Challenge on Perceptual Image Super-resolution — http://arxiv.org/abs/1809.07517v3
[31] The Barbados 2018 List of Open Issues in Continual Learning — http://arxiv.org/abs/1811.07004v1
[32] DEFT: Dexterous Fine-Tuning for Real-World Hand Policies — http://arxiv.org/abs/2310.19797v2
[33] ALOHA 2: An Enhanced Low-Cost Hardware for Bimanual Teleoperation — http://arxiv.org/abs/2405.02292v1
[34] Stabilize to Act: Learning to Coordinate for Bimanual Manipulation — http://arxiv.org/abs/2309.01087v2
[35] DAIR: Disentangled Attention Intrinsic Regularization for Safe and Efficient Bimanual Manipulation — http://arxiv.org/abs/2106.05907v4
[36] Mobile ALOHA: Learning Bimanual Mobile Manipulation with Low-Cost Whole-Body Teleoperation — http://arxiv.org/abs/2401.02117v1
[37] VoxAct-B: Voxel-Based Acting and Stabilizing Policy for Bimanual Manipulation — http://arxiv.org/abs/2407.04152v2
[38] Knowledge-Embedded Representation Learning for Fine-Grained Image Recognition — http://arxiv.org/abs/1807.00505v1
[39] Overview of AuTexTification at IberLEF 2023: Detection and Attribution of Machine-Generated Text in Multiple Domains — http://arxiv.org/abs/2309.11285v1
[40] Multi-entity Video Transformers for Fine-Grained Video Representation Learning — http://arxiv.org/abs/2311.10873v2
[41] Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware — https://arxiv.org/abs/2304.13705
[42] Self-Supervised Correspondence in Visuomotor Policy Learning — http://arxiv.org/abs/1909.06933v1
[43] Enhancement of Position Accuracy via DPB-Embedded ACT Model for Fine-Grained Manipulation — https://doi.org/10.54254/2755-2721/2025.22913
[44] Conformal Policy Learning for Sensorimotor Control Under Distribution Shifts — http://arxiv.org/abs/2311.01457v1
[45] Policy Learning with Observational Data — http://arxiv.org/abs/1702.02896v6
[46] GPA-RAM: Grasp-Pretraining Augmented Robotic Attention Mamba for Spatial Task Learning — https://arxiv.org/abs/2504.19683
[47] OnlineCache: Learning Dynamic Caching Policies with Error Correction for Efficient Diffusion Inference — http://arxiv.org/abs/2607.29398v1
[48] LEAP Hand: Low-Cost, Efficient, and Anthropomorphic Hand for Robot Learning — http://arxiv.org/abs/2309.06440v1
[49] Aero Hand Open: A Simulation-Ready Tendon-Driven Hand for Dexterous Manipulation Learning — http://arxiv.org/abs/2608.28578v2
[50] Real-Time Force Regulation for Whole-Hand Dexterous Grasping — http://arxiv.org/abs/2609.30082v1
[51] Hand-4DGS: Feed-Forward 3D Gaussian Splatting for 4D Hand Reconstruction from Egocentric Videos — http://arxiv.org/abs/2606.19156v1
[52] The Synthesis of Optimal Control Laws Using Isaacs' Method for the Solution of Differential Games — http://arxiv.org/abs/2112.10849v2
[53] Isaac Lab: A GPU-Accelerated Simulation Framework for Multi-Modal Robot Learning — http://arxiv.org/abs/2511.04831v1
[54] Aerial Mobile Manipulator System to Enable Dexterous Manipulations with Increased Precision — http://arxiv.org/abs/2010.09618v1
[55] LabDex: A Hierarchical Benchmark for Dexterous Manipulation in Laboratories — http://arxiv.org/abs/2608.18618v1
[56] LeRobot: An Open-Source Library for End-to-End Robot Learning — http://arxiv.org/abs/2602.22818v1
[57] Robot Learning: A Tutorial — http://arxiv.org/abs/2510.12403v1
[58] One-Shot Reinforcement Learning for Robot Navigation with Interactive Replay — http://arxiv.org/abs/1711.10137v2
[59] On-Policy Robot Imitation Learning from a Converging Supervisor — http://arxiv.org/abs/1907.03423v7
[60] Multi-objective Model-based Policy Search for Data-efficient Learning with Sparse Rewards — http://arxiv.org/abs/1806.09351v3
[61] State-of-the-art in Robot Learning for Multi-Robot Collaboration: A Comprehensive Survey — http://arxiv.org/abs/2408.11822v1
[62] Untangling Dense Knots by Learning Task-Relevant Keypoints — http://arxiv.org/abs/2011.04999v1
[63] Deception Game: Closing the Safety-Learning Loop in Interactive Robot Autonomy — http://arxiv.org/abs/2309.01267v2
[64] On the Popularity of GitHub Applications: A Preliminary Note — http://arxiv.org/abs/1507.00604v3
[65] What Challenges Do Developers Face in AI Agent Systems? An Empirical Study on Stack Overflow & GitHub Issues — http://arxiv.org/abs/2510.25423v2
[66] Emotional Contagion in Code: How GitHub Emoji Reactions Shape Developer Collaboration — http://arxiv.org/abs/2511.02515v1
[67] Bridging the Sim2Real Gap: Vision Encoder Pre-Training for Visuomotor Policy Transfer — http://arxiv.org/abs/2501.16389v2
[68] The Importance and the Limitations of Sim2Real for Robotic Manipulation in Precision Agriculture — http://arxiv.org/abs/2008.03983v1
[69] The Developments and Challenges towards Dexterous and Embodied Robotic Manipulation: A Survey — http://arxiv.org/abs/2507.118

---

*Generated by research-bot · topic=`embodied-manipulation` · depth=`standard` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading · model=`deepseek-v4-flash` · sources=121 · duration=312s · 2026-10-06T22:35:26+00:00*
