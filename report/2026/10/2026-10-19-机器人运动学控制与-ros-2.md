# 机器人运动学、控制与 ROS 2：2024–2026 实质增量快照

**日期**：2026-10-19（UTC）｜**领域**：机器人运动学 / 运动控制 / ROS 2 工程栈｜**可引用来源**：34 条编号来源，其中与本主题直接相关的约 12 条；其余为检索噪声（视觉挑战赛、天体物理、临床问答等），已在文末标注未使用。**检索口径**：以 arXiv 预印本元数据与摘要片段为主，**未取得全文表格级数据**，因此本报告多处结论只能停在“标题/摘要级证据”。

> **总体增量判断**：过去 12–24 个月，**唯一有可核查证据的实质增量集中在“人形机器人全身控制（whole-body control）的学习化路线”**——尤其是“无运动先验的 RL 统一全身控制器”[17]、约束式全身跟踪[23]、域随机化 diffusion policy[18]、全身遥操作[22]与“无机器人演示”的全身操作接口[20]。与此同时，**逆运动学（IK）、轨迹优化、MPC、`ros2_control`/`controller_manager` 生态在本次给定证据中零覆盖**——这是**检索缺口，不等于“无进展”**，相关章节一律标 `> 待核实`。

---

## 1. 进展与热点（Progress & Hotspots）

**一句话增量**：热点从“模块化 WBC + QP”向“统一学习型全身控制器”迁移，但迁移的证据强度仍停留在预印本自述层面。

### 1.1 最新进展（近 1–2 年，2025-01 至 2026-10）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Humanoid Whole-Body Badminton via an Annealed Reinforcement Learning Curriculum [17] | 2025-11 | > 待核实 | 引用数 `> 待核实` | arXiv 预印本（cs.RO），未见同行评审 venue | 低——仅一条预印本记录，无引用/榜单/社区信号 | ★★★☆☆ 与“学习增强全身控制”高度相关，但仅预印本自述 | http://arxiv.org/abs/2511.11218v4 | 用退火式 RL 课程训练**单一统一全身控制器**，无 motion priors/专家演示，协调步法与击球 |
| Constrained Whole-Body Tracking for Humanoid Robots [23] | 2026-06 | > 待核实 | `> 待核实` | arXiv 预印本，venue 待核实 | 低——无热度信号 | ★★★☆☆ 标题直指“约束式全身跟踪”，可能代表优化派 WBC 的延续，需读全文确认 | http://arxiv.org/abs/2606.00374v2 | 仅标题级证据：`> 待核实`（是否 QP/分层优化、是否真机） |
| Humanoid Manipulation Interface [20] | 2026-02 | > 待核实 | `> 待核实` | arXiv 预印本 | 低 | ★★★☆☆ “robot-free demonstrations”对数据采集范式有意义，细节待核实 | http://arxiv.org/abs/2602.06643v2 | 副标题：Humanoid Whole-Body Manipulation from Robot-Free Demonstrations |
| CHILD: Whole-Body Humanoid Teleoperation System [22] | 2025-08 | > 待核实 | `> 待核实` | arXiv 预印本 | 低 | ★★★☆☆ 全身遥操作是 WBC 的典型下游验证场景 | http://arxiv.org/abs/2508.00162v2 | 标题级证据：Controller for Humanoid Imitation and Live Demonstration |
| The Role of Domain Randomization in Training Diffusion Policies for Whole-Body Humanoid Control [18] | 2024-11 | > 待核实 | `> 待核实` | arXiv 预印本 | 低 | ★★★☆☆ 直接对应“仿真到真机”的域随机化归因问题 | http://arxiv.org/abs/2411.01349v1 | 标题级证据：域随机化在全身人形 diffusion policy 中的作用 |
| Learning Humanoid Standing-up Control across Diverse Postures [24] | 2025-02 | > 待核实 | `> 待核实` | arXiv 预印本 | 低 | ★★☆☆☆ 单技能（起身）学习控制，属窄任务验证 | http://arxiv.org/abs/2502.08378v2 | 标题级证据 |

**证据分级与“宣称 vs 验证”**：
- [17] 的“协调步法与击球、完成快速动态物体交互”属于**论文宣称（作者自评 + 演示级证据）**：候选证据中**没有**真机成功率、对打回合数、硬件型号、基线对比表或第三方复现/榜单结果，因此**不能计为已被独立验证的 SOTA 变动**。confidence = low–medium。
- [23][20][22][18][24] 在本次证据中**仅有标题**，其方法、指标、真机验证情况全部 `> 待核实`；将它们写成“已验证进展”会构成过度外推。

**零覆盖警示（关键）**：在 2024–2026 窗口内，**IK、轨迹优化、MPC、`ros2_control`/`controller_manager` 控制栈没有任何一条可核查证据**进入本批候选。按方法论，这些维度应写 `> 待核实`，**不得**由“人形 WBC 有进展”推断“经典运动学/控制栈无进展”。

### 1.2 经典与奠基性工作（严格与上表分节）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Modern Robotics: Mechanics, Planning, and Control [10] | 2017 | > 待核实（候选块未给作者字段） | citations=1190（候选块口径，未独立核验） | 剑桥大学出版社专著（DOI 可解析） | 高——唯一有明确引用数的条目 | ★★★★★ 旋量/李群运动学的统一教材，仍是当前学习型控制论文的数学基线 | https://doi.org/10.1017/9781316661239 | 以旋量（screw）理论统一运动学、规划与控制 |
| DQ Robotics: a Library for Robot Modeling and Control [5] | 2019 | > 待核实 | `> 待核实` | arXiv（cs.RO）预印本，期刊版本待核实 | 低——无热度信号 | ★★★★☆ 对偶四元数（dual quaternion）建模的开源实现，是“李群/对偶四元数替代齐次变换”路线的工程载体 | http://arxiv.org/abs/1910.11612v3 | 对偶四元数代数用于机器人建模与控制 |
| Infusing model predictive control into meta-reinforcement learning [3] | 2021 | > 待核实 | `> 待核实` | arXiv（cs.RO） | 低 | ★★★☆☆ MPC + meta-RL 混合的早期代表，是当前“学习型 WBC vs 优化型 WBC”争论的前史 | http://arxiv.org/abs/2109.07120v3 | 面向动态环境的移动机器人自适应决策 |
| Active Uncertainty Reduction for HRI: An Implicit Dual Control Approach [7] | 2022 | > 待核实 | `> 待核实` | arXiv（cs.RO） | 低 | ★★☆☆☆ 控制论视角（对偶控制）用于人机交互，属方法论旁支 | http://arxiv.org/abs/2202.07720v2 | 主动不确定性消减 |
| Robotics Simulation [12] | > 待核实 | > 待核实 | `> 待核实` | CRC Press 书籍章节（DOI） | 低 | ★★★☆☆ 仿真方法论参考，可作为 Isaac/MuJoCo 生态讨论的教科书锚点 | https://doi.org/10.1201/9781003216858-8 | 仿真在机器人研发中的角色 |
| Grasp and Motion Planning for Dexterous Manipulation (Real Robot Challenge) [34] | 2021 | > 待核实 | `> 待核实` | arXiv（cs.RO） | 低 | ★★★☆☆ 少量“抓取+运动规划+真机竞赛”型基准证据 | http://arxiv.org/abs/2101.02842v1 | 真机挑战赛中的抓取与运动规划方案 |

> **分类纠偏**：结构化发现 q2 把 2026 年的 VLA 论文 *Xiaomi-Robotics-1* [2] 归入“奠基性工作”，属于**抽取阶段的分类错误**——它是 2026 年新工作，应归入“最新进展/产业”，不应作为教科书级基线。

---

## 2. 工业界与产品（Industry & Product）

**一句话增量**：可核查的产业化信号只有一条——**真机轨迹数据规模被推到 10 万小时量级**；其余（发行版、商业支持、量产部署）本批证据为零。

- **Xiaomi-Robotics-1** [2]（2026）：标题与摘要片段称其为“foundational VLA model”，具备（1）在未见环境中开箱执行多样化语言指令的移动操作，（2）以极少微调适配新下游任务；并宣称训练语料为 **over 100K hours of real-world trajectories**。四类证据：热度 `> 待核实`；权威=arXiv（cs.RO）预印本，未见同行评审；关注度=低（本批无引用/榜单信号，但“10 万小时真机数据”本身是强产业信号）；推荐度 ★★★★☆（对“数据规模决定具身能力”的判断有直接参考价值）。**注意**：这是**论文宣称**，数据规模与“开箱泛化”均无第三方复现。
- **Open Ant** [21]（2026-07）：标题显示为“面向强化学习研究的机器人平台”，属于**硬件/平台层产品化**信号，具体售价、开源程度、量产状态 `> 待核实`。
- **力感知硬件**：*Design, Calibration, and Control of Compliant Force-sensing Gripping Pads for Humanoid Robots* [8]（2024）显示人形末端力感知的标定与控制仍是独立工程问题；是否有厂商采用 `> 待核实`。
- **ROS 2 发行版、`ros2_control` 版本、MoveIt 2 发布、商业支持与真机量产部署**：本批证据**零覆盖**，全部 `> 待核实`。**不能**据此断言“无变化”。

---

## 3. 蓝海与缺口（Blue Ocean & Gaps）

**一句话增量**：最大的空白不是“再做一个人形 WBC”，而是**评测与工程可复现性基础设施**。

1. **人形动态交互无跨实验室基准**：羽毛球类动态交互[17]的成功率/回合数无法与其他工作横向比较；RoboArena 类榜单在人形全身控制上的适用性 `> 待核实`。谁先给出“多本体 + 多任务 + 真机长时”的公开榜单，谁就占据评测位。
2. **学习型控制器与优化型控制器的混合缺乏系统对比**：一边是 RL 统一控制器[17]，一边是约束式全身跟踪[23]，但本批证据中**没有任何一篇做二者的同任务同硬件对比**。这是一个高杠杆、低算力门槛的论文缺口。
3. **ROS 2 实时性与确定性缺乏一手实测**：`ros2_control` 硬件接口、PREEMPT_RT 补丁、DDS vs Zenoh 的延迟/抖动实测报告在本批证据中为零。中间件选型目前主要靠社区经验而非可复现测量。
4. **IK 的“现代化”落地**：对偶四元数[5]/旋量[10] 的数学体系成熟，但在学习型策略输出层（动作空间参数化）中的采用程度 `> 待核实`。
5. **实时系统的安全面**：[33]（2026-09）讨论“计数器型 RowHammer 防护破坏实时可预测性”，提示**实时性可被内存子系统攻击面侵蚀**；其结论向 ROS 2 调度栈的可迁移性 `> 待核实`，但作为“实时性不只是调度问题”的早期信号值得记录。

---

## 4. 瓶颈与拐点（Bottleneck & Inflection）

**一句话增量**：瓶颈正从“算法”转向“数据规模 + 评测口径 + 实时工程”，拐点信号是**真机数据量级跃升**[2]与**统一控制器范式出现**[17]。

| 瓶颈 | 现状证据 | 是否临近拐点 | 拐点信号（可观测指标） |
|---|---|---|---|
| 数据 | 宣称 10 万小时真机轨迹[2]（`> 待核实`） | 较大概率临近 | 出现**多家**公开同量级真机数据集，且有第三方复用报告 |
| 评测 | 人形全身控制无统一基准（本批零覆盖） | 未见拐点 | 出现跨实验室人形榜单并公布真机成功率口径 |
| 算法归因 | RL 统一控制器[17]未拆分“数据 vs 架构 vs 算力”贡献 | 未见拐点 | 出现同数据同算力的消融对比论文 |
| 仿真到真机 | 域随机化的作用被单独研究[18]（标题级） | 需数据 | 域随机化参数与真机成功率的公开映射曲线 |
| 实时工程 | ROS 2 中间件实测证据为零；实时可预测性存在新攻击面[33] | `> 待核实` | 公开的 DDS/Zenoh 抖动 benchmark 与 PREEMPT_RT 长时跑测报告 |
| 硬件力控 | 人形柔性力传感夹爪的标定与控制仍需专门工作[8]；制造业力控任务的 AI 方法被综述[4] | 需数据 | 力控任务的公开成功率与漂移指标 |

---

## 5. 社会·政策·国际（Society, Policy & Geopolitics）

**一句话判断**：**本周期本次检索无显著变化证据**——本批 34 条来源中没有任何监管文本、标准草案、出口管制或劳动影响研究。以下仅为可核查的间接事实，不做政策推断：

- **产业能力的地理性**[2]：10 万小时级真机轨迹数据由企业（小米）主导采集，说明**大规模真机数据正成为企业级而非实验室级资产**；这对“学术机构能否参与基础模型竞赛”有结构性影响（判断，非事实，`> 待核实`）。
- **标准与合规**：ISO 10218 / TS 15066、ROS 2 安全认证、AI 法案对具身系统的影响，本次**无任何可引用来源**，全部 `> 待核实`。
- **伦理与劳动影响**：本批无证据，`> 待核实`。

> 方法论提醒：政策维度“无显著变化”是本报告的证据状态，**不是**对现实世界的断言。

---

## 6. 资本与生态（Capital & Ecosystem）

**一句话增量**：本批证据中没有融资、并购、人才流动数据；生态信号仅体现在**开源库与被引用教材**层面。

- **资本**：融资额、估值、并购事件 `> 待核实`（零来源）。
- **开源生态**：DQ Robotics[5] 代表“对偶四元数建模”的小而专生态；Open Ant[21] 代表“RL 研究用机器人平台”；二者 GitHub star、贡献者数、最近提交时间**均未采集**，`> 待核实`。
- **知识生态**：Modern Robotics[10] 以 citations=1190（候选块口径）显示其仍是该领域**引用最集中的单一知识入口**，说明“旋量/李群”教学体系没有被学习型控制范式取代，而是被其继续消费。
- **企业研究占比**：Xiaomi-Robotics-1[2] 是典型“企业主导、大规模自有数据”的产出形态，与高校单实验室论文[17][24]形成两种生产函数。

**开源项目表**

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| DQ Robotics [5] | 2019 | > 待核实 | star `> 待核实` | arXiv 预印本 + 开源库（期刊版待核实） | 低 | ★★★★☆ 对偶四元数建模/控制的可运行实现 | http://arxiv.org/abs/1910.11612v3 | 机器人建模与控制库 |
| Open Ant [21] | 2026 | > 待核实 | `> 待核实` | arXiv 预印本 | 低 | ★★★☆☆ RL 研究用硬件平台 | http://arxiv.org/abs/2607.18488v1 | 标题级证据 |
| MoveIt 2 / `ros2_control` / Pinocchio / Crocoddyl / OCS2 / Drake / MuJoCo / Isaac | — | — | `> 待核实` | 官方文档与 release notes **本次未取得** | `> 待核实` | ★☆☆☆☆ 无法评级（缺证据） | `> 待核实`（不得编造仓库链接） | 本批证据零覆盖，需补采官方发布说明与仓库活跃度后重做 |

---

## 7. 信号与预测（Signals & Forecast）

**早期信号（已确证的事实层）**：
1. 2025-11 出现“无 motion prior 的 RL 统一全身控制器”[17]——范式信号，但证据等级仅为预印本。
2. 2026 年出现“10 万小时真机轨迹”级 VLA 宣称[2]——数据规模信号。
3. 2026-06 仍有“约束式全身跟踪”[23]在发表——说明**优化派 WBC 并未退出**，两条路线并行。
4. 2026-09 出现“实时可预测性可被内存子系统攻击破坏”[33]——实时性议题的新维度。

**可证伪预测 [P]**：

- **[P1]（置信度：中）** 到 **2027-06**，若人形全身控制出现**跨实验室公开榜单**（含真机成功率与任务清单），则“评测基础设施成为瓶颈”的判断成立；若届时仍只有单篇论文自评，则本判断证伪。依据链：当前[17][23][18][20][22][24]全部缺少可比口径 → 社区存在明确未满足需求。
- **[P2]（置信度：中低）** 到 **2027-12**，若出现**同硬件同任务上“RL 统一控制器 vs 约束式 WBC”的公开对比论文**，则“混合/混合范式”将成为主流叙事；否则“两条路线各自为战”延续。依据：本批证据中二者零交叉。
- **[P3]（置信度：低）** 到 **2027-06**，若 `ros2_control` 或主流 DDS/Zenoh 实现发布**公开的抖动/延迟基准套件**，则 ROS 2 实时性从“经验选型”转为“可测量工程”；本报告中该维度零证据的状态才会被打破。依据：当前证据完全缺失，属结构性空白而非技术不可能。
- **[P4]（置信度：低）** “100K 小时真机数据”[2] 的**可复现性**：若到 2027-06 仍无第三方在该数据（或同量级公开数据）上复现其泛化宣称，则应把“数据规模决定泛化”降级为未经证实的假设。

**Watchlist（值得持续关注）**：[17] 的同行评审与复现、[23] 的方法细节、[2] 的数据与权重开放情况、`ros2_control` 官方 release notes（待补采）、人形全身控制榜单动向。

**不确定性声明**：本报告 7 个维度中，第 1 章部分、第 2 章、第 3 章有 B 级（预印本/标题级）证据；第 4–6 章多为推论与空白标注；第 5 章基本无证据。**任何把本报告读成“ROS 2 与经典运动学在 2024–2026 无进展”的解读都是对证据缺口的误读。**

---

## 参考来源

**本报告实际引用**：
- [2] Xiaomi-Robotics-1: Scaling Vision-Language-Action Models with over 100K Hours of Real-World Trajectories — http://arxiv.org/abs/2607.15330v2
- [3] Infusing model predictive control into meta-reinforcement learning for mobile robots in dynamic environments — http://arxiv.org/abs/2109.07120v3
- [4] On the role of Artificial Intelligence methods in modern force-controlled manufacturing robotic tasks — http://arxiv.org/abs/2409.16828v3
- [5] DQ Robotics: a Library for Robot Modeling and Control — http://arxiv.org/abs/1910.11612v3
- [7] Active Uncertainty Reduction for Human-Robot Interaction: An Implicit Dual Control Approach — http://arxiv.org/abs/2202.07720v2
- [8] Design, Calibration, and Control of Compliant Force-sensing Gripping Pads for Humanoid Robots — http://arxiv.org/abs/2405.20969v1
- [10] Modern Robotics — https://doi.org/10.1017/9781316661239
- [12] Robotics Simulation — https://doi.org/10.1201/9781003216858-8
- [17] Humanoid Whole-Body Badminton via an Annealed Reinforcement Learning Curriculum — http://arxiv.org/abs/2511.11218v4
- [18] The Role of Domain Randomization in Training Diffusion Policies for Whole-Body Humanoid Control — http://arxiv.org/abs/2411.01349v1
- [20] Humanoid Manipulation Interface: Humanoid Whole-Body Manipulation from Robot-Free Demonstrations — http://arxiv.org/abs/2602.06643v2
- [21] The Open Ant: A Robot Platform for Reinforcement Learning Research — http://arxiv.org/abs/2607.18488v1
- [22] CHILD (Controller for Humanoid Imitation and Live Demonstration): a Whole-Body Humanoid Teleoperation System — http://arxiv.org/abs/2508.00162v2
- [23] Constrained Whole-Body Tracking for Humanoid Robots — http://arxiv.org/abs/2606.00374v2
- [24] Learning Humanoid Standing-up Control across Diverse Postures — http://arxiv.org/abs/2502.08378v2
- [33] JENGA: Exploiting Counter-Based RowHammer Countermeasures to Break Real-Time Predictability — http://arxiv.org/abs/2609.01077v1
- [34] Grasp and Motion Planning for Dexterous Manipulation for the Real Robot Challenge — http://arxiv.org/abs/2101.02842v1

**未引用的编号**（经主题判定与本调研无关或仅为噪声，未在正文使用）：[1] HyperCLOVA X、[6] 磁性软体皮肤、[9] 相对论弹性、[11] 三体力 Bethe-Salpeter、[13] VQualA 短视频参与度、[14] NTIRE 超分、[15] TDCOSMO 强透镜、[16] VLSP 越南语交通标志问答、[19] One-Shot RL 导航、[25] TRUST 2025 workshop、[26] ArchEHR-QA、[27] Nepali Meme 分类、[28] MOASEI 多智能体竞赛、[29] AutoRestTest、[30] LHC 机器学习综述、[31] eRisk 抑郁检测、[32] BioASQ 2026。

---

*Generated by research-bot · topic=`机器人运动学控制与-ros-2` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`deepseek-v4-flash` · sources=34 · duration=149s · 2026-10-19T22:24:28+00:00*
