# 机器人运动学、控制与 ROS 2 生态增量快照（2024–2026）

**生成日期**：2026-10-23（UTC）｜**领域**：机器人运动学（robot kinematics）/ 控制（MPC、WBC、学习控制）/ ROS 2 软件栈｜**检索源数量**：30 条候选来源（[1]–[30]）｜**有效相关来源**：约 6 条（[11][12][21][22][23][30]），其余 24 条经核验与本主题无技术关联

> **证据基础说明（必须先读）**
> 本轮候选证据集存在严重召回污染：30 条来源中，含关键词 "inverse" 的数学谱反问题 [9]、Radon 变换反演 [4][7]、含 "kinematic" 的星系运动学形态-密度关系 [5]、含 "control" 的车联网卸载控制 [24]、以及天体物理 [2][8][17]、医学影像 [20]、NLP/语音评测 [15][16][19]、视觉挑战赛 [1][13] 等，均与机器人运动学/控制/ROS 2 无关。**因此本报告在多数子问题上只能给出"证据缺口告警"而非"技术进展结论"**。凡无来源支撑处一律标 `> 待核实`，不做推测性填充。

---

## 1. 进展与热点（Progress & Hotspots）

**增量判断**：本窗口内可被入集证据确认的方向性信号只有两条——(a) ROS 2 Humble + MoveIt 2 已进入医疗手术辅助的端到端原型流水线；(b) 人形全身高动态任务（羽毛球）开始采用带退火课程的强化学习范式。**运动学求解器（KDL/TRAC-IK/IKFast）与 MPC/WBC 的基准刷新在本轮证据中完全缺席**，这属于"未获证据"，不等于"无进展"。

**1.1 唯一可核的 ROS 2 系统级进展：手术辅助流水线**
Surgical Vision ROS2 是一套 ROS 2 Humble 流水线：视觉节点用改编自皮肤科的 ABCDE 五段框架对术中创面评分，行为管理器把评分映射为三级自主性（autonomy tiers），并驱动 MoveIt2 机械臂 [22]。
- **热度证据**：候选块给出 `citations=0` [22]。
- **权威证据**：DOI 指向 Research Square 预印本平台（`10.21203/rs.3.rs-10362132/v1`），候选块未显示同行评审 venue，按证据分级为 **B/C 级** [22]。
- **关注度**：**低** — 依据为 citations=0，且为单中心原型、无第三方复现记录 [22]。
- **推荐度**：**★★★☆☆** — 价值在于"ROS 2 Humble + MoveIt2 + 变自主性行为管理"的工程集成范式，而非运动学或控制算法创新 [22]。

**1.2 人形全身控制的学习化信号**
《Humanoid Whole-Body Badminton via an Annealed Reinforcement Learning Curriculum》出现在候选集中 [30]。
- **热度证据**：候选块未提供 citations 或代码仓库 star `> 待核实` [30]。
- **权威证据**：arXiv 预印本（编号 2511.11218v4，即 2025-11 提交、v4 修订），候选块未给出同行评审 venue 与学科分类 `> 待核实` [30]。
- **关注度**：**待核实** — 仅有标题级证据，无法判断社区讨论热度或是否含真机实验 [30]。
- **推荐度**：**★★★☆☆（暂定）** — 是"全身控制（WBC）由模型基转向学习基"这一趋势的候选样本，但**任务数、本体型号、成功率口径、是否真机均未入集，不得据此下结论** [30]。

**1.3 明确的负结论：运动学求解方向零证据**
候选集中所有形似"逆问题/运动学"的条目均为跨学科误召回：Sturm–Liouville 算子谱反问题 [9]、broken-ray Radon 变换反演公式 [4][7]、星系运动学形态-密度关系 [5]、强引力透镜宇宙学 [17]。这些文献不含机械臂、雅可比、奇异位形或求解耗时等任何运动学指标 [4][5][7][9][17]。故 **"KDL 之后是否出现了经基准验证的替代求解器"在本轮无法回答** `> 待核实`。

### 经典与奠基性工作（本轮入集的控制理论类，含相关度警示）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Analysis and design of MPC frameworks for dynamic operation — An overview [11] | 2023 | 作者/机构未在候选块显示 `> 待核实` | `> 待核实` | arXiv 预印本（eess.SY），综述性质，非同行评审确认 `> 待核实` [11] | 待核实 | ★★★☆☆ | http://arxiv.org/abs/2307.03004v2 | 非线性约束系统 MPC 框架综述；**非机器人专用**，仅可作 MPC 方法论背景，不可当作机器人 WBC 证据 [11] |
| On Controller Design for Systems on Manifolds in Euclidean Space [12] | 2018 | `> 待核实` | `> 待核实` | arXiv（math.OC）[12] | 待核实 | ★★★☆☆ | http://arxiv.org/abs/1807.03475v1 | 流形状态空间嵌入欧氏空间设计控制器；与 SO(3)/SE(3) 姿态控制有理论关联，但文中无机器人实验入集 [12] |
| The Synthesis of Optimal Control Laws Using Isaacs' Method [21] | 2021 | `> 待核实` | `> 待核实` | arXiv（2112.10849v2）[21] | 待核实 | ★★☆☆☆ | http://arxiv.org/abs/2112.10849v2 | 微分博弈/HJI 方法求最优控制律；与鲁棒/对抗性控制理论相关，机器人相关性未验证 [21] |
| Control of a Rigid Wing Pumping Airborne Wind Energy System [10] | 2020 | `> 待核实` | `> 待核实` | arXiv（eess.SY）[10] | 待核实 | ★★☆☆☆ | http://arxiv.org/abs/2006.11141v1 | 分层控制结构覆盖起降/发电全工况；属非机器人被控对象，仅作分层控制架构参考 [10] |

> **经典运动学与 WBC 的真正奠基文献（Lynch & Park、Siciliano、Sentis & Khatib 等）本轮未进入候选集，故不列出、不引用** `> 待核实`。

---

## 2. 工业界与产品（Industry & Product）

**增量判断**：本周期内**没有任何厂商发布、产品量产或融资并购的一手来源入集**，因此"从 lab 走向落地"的判断无法成立。可观测的仅有两类弱信号：MoveIt 生态的工具化延续性，与 ROS 2 在垂直行业（手术）中的原型化使用。

**2.1 MoveIt 生态的工具化延续**
MoveIt Grasps 被描述为"与 MoveIt 紧密集成的操作（manipulation）框架" [23]。
- **热度证据**：候选集未提供 GitHub star 或引用数 `> 待核实` [23]。
- **权威证据**：ROSCon 2019 官方摘要，具 DOI（`10.36288/roscon2019-900894`），属会议官方产出，**B 级** [23]。
- **关注度**：**待核实** — 无 star/下载数据入集；仅能确认其为 MoveIt 官方生态内工具 [23]。
- **推荐度**：**★★★☆☆** — 作为 ROS 操作栈历史脉络节点有价值；**注意其为 2019 年工作，不属 2024–2026 增量窗口** [23]。

**2.2 ROS 2 进入受监管垂直场景**
[22] 显示 ROS 2 Humble 被用于术中创面评估与机械臂变自主控制，是"ROS 2 从研究中间件走向临床辅助原型"的**单点**证据 [22]。
- **热度/权威/关注度/推荐度**：见 §1.1；`citations=0`、预印本、关注度低、★★★☆☆ [22]。
- **限定表述**：据该预印本自述，其为 Humble 流水线原型；**是否通过医疗器械审批、是否有临床数据，候选块未提供** `> 待核实` [22]。

**2.3 工业实时监测侧的旁证（相关度低）**
电机实时状态监测与故障诊断系统（基于 LabVIEW）[25] 与原材料处理的实时数据分析 [26] 属工业实时监控范畴，**均非 ROS 2、非机器人运动控制**，仅可作为"工业侧对实时性需求持续存在"的间接背景 [25][26]。
- **权威**：arXiv 预印本（2018 年），非同行评审确认 `> 待核实` [25][26]；**关注度低**；**推荐度 ★☆☆☆☆**（与本主题技术栈无交集）。

### 开源项目（仅列本轮有来源支撑者）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| MoveIt Grasps [23] | 2019 | ROSCon 2019 讲者（候选块未给作者名）`> 待核实` | star/引用 `> 待核实` | ROSCon 官方摘要 + DOI，B 级 [23] | 待核实 | ★★★☆☆ | https://doi.org/10.36288/roscon2019-900894 | 与 MoveIt 紧耦合的抓取框架；**窗口外历史工作** [23] |
| MoveIt 2（作为被使用组件）[22] | 2026（论文年） | 使用方为 Surgical Vision ROS2 作者群 `> 待核实` | `citations=0`（论文侧）[22] | 仅经预印本间接引用，非 MoveIt 官方文档，C 级 [22] | 低 [22] | ★★☆☆☆ | https://doi.org/10.21203/rs.3.rs-10362132/v1 | 仅证明"被用于 ROS 2 Humble 流水线驱动机械臂"，**不构成 MoveIt 2 版本演进或维护活跃度证据** [22] |
| ros2_control / Nav2 / Pinocchio / Drake / MuJoCo / Isaac ROS / micro-ROS | — | — | `> 待核实` | **本轮无任何来源入集** | 未知 | — | `> 待核实` | 该 7 个项目的维护活跃度、版本演进与工业采用**在本轮证据中完全缺失**，不得给出任何判断 |

---

## 3. 蓝海与缺口（Blue Ocean & Gaps）

**增量判断**：本领域最显著的"缺口"首先出现在**证据层**——现有检索管线无法把"inverse / kinematic / control / real-time"这类高歧义术语约束到机器人语义空间，导致 24/30 条为跨学科误召回 [4][5][7][9][24]。这本身是可观测的工程缺口。

**3.1 方法论缺口：术语歧义导致的召回归因失败**
- "inverse" 同时命中数学谱反问题 [9] 与 Radon 变换反演 [4][7]；"kinematic" 命中星系运动学 [5]；"control" 命中车联网卸载控制 [24]。上述四类文献均不含机器人本体、控制器或中间件内容 [4][5][7][9][24]。
- **可核证据**：车联网文献明确其问题为 Deadline-Constrained Task Offloading and Resource Allocation Problem（DOAP），优化目标为车辆总效用，方法为 SARound，无任何机械臂/人形本体或真机实验 [24]。
- **关注度**：低（主题与机器人控制社区关注点不同）[24]；**推荐度 ★☆☆☆☆**（负例，仅用于说明检索污染）[24]。

**3.2 技术缺口（本轮无法证实，仅登记为待检索项）**
- 逆运动学求解器的**横向基准**（成功率 / 耗时分位数 / 奇异位形鲁棒性，跨 KDL、TRAC-IK、优化类求解器）在本轮候选集中零命中 `> 待核实`。
- 足式/人形 **MPC 与 WBC** 的第三方复现与真机部署证据零命中 `> 待核实`。
- ROS 2 **DDS 实时性开销**与 **Zenoh 替代**的对立说法零命中 `> 待核实`。

### 数据集与基准（本轮候选集中的"基准类"条目及其相关度）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| VQualA 2025 短视频互动度预测挑战赛 [1] | 2025 | 候选块未给作者；声明与 ICCV 2025 联合举办 | `> 待核实` | arXiv（cs.CV），联合举办声明，未确认正式收录 [1] | 低（与本主题无关） | ★☆☆☆☆ | http://arxiv.org/abs/2509.02969v1 | **非机器人基准**，纯误召回 [1] |
| TRUST 2025: SCRITA & RTSS @ RO-MAN 2025 [18] | 2025 | `> 待核实` | `> 待核实` | RO-MAN 2025 关联 workshop（候选块未给收录细节）`> 待核实` [18] | 待核实 | ★★☆☆☆ | http://arxiv.org/abs/2509.11402v1 | 机器人领域 workshop，但主题为信任（trust），**非运动学/控制基准** [18] |
| NTIRE 2025 图像超分挑战赛 [13] | 2025 | `> 待核实` | `> 待核实` | arXiv（2504.14582v3）[13] | 低（无关） | ★☆☆☆☆ | http://arxiv.org/abs/2504.14582v3 | 计算机视觉基准，误召回 [13] |
| AudioMOS Challenge 2025 [15] | 2025 | `> 待核实` | `> 待核实` | arXiv（2509.01336v1）[15] | 低（无关） | ★☆☆☆☆ | http://arxiv.org/abs/2509.01336v1 | 语音质量评测，误召回 [15] |
| VLSP 2025 MLQA-TSR [16] | 2025 | `> 待核实` | `> 待核实` | arXiv（2510.20381v1）[16] | 低（无关） | ★☆☆☆☆ | http://arxiv.org/abs/2510.20381v1 | 越南语法律问答，误召回 [16] |
| eRisk@CLEF 2025（SINAI）[19] | 2025 | `> 待核实` | `> 待核实` | arXiv（2509.19861v1）[19] | 低（无关） | ★☆☆☆☆ | http://arxiv.org/abs/2509.19861v1 | 抑郁检测，误召回 [19] |
| MIDOG 2025 Track 2 [20] | 2025 | `> 待核实` | `> 待核实` | arXiv（2508.18831v1）[20] | 低（无关） | ★☆☆☆☆ | http://arxiv.org/abs/2508.18831v1 | 病理核分裂象分类，误召回 [20] |

> **LIBERO / SimplerEnv / RoboArena / Open X-Embodiment / DROID 等机器人操作基准本轮均无来源入集**，故不列表、不给指标 `> 待核实`。

---

## 4. 瓶颈与拐点（Bottleneck & Inflection）

**增量判断**：本周期**无法确认任何技术拐点**。唯一可讨论的"瓶颈"是检索与评测基础设施瓶颈；技术侧瓶颈（实时性、奇异位形、sim-to-real 差距）在本轮仅有待核实项。

**4.1 评测基础设施瓶颈（有证据）**
- 现有召回的领域约束失效，导致 30 条中约 24 条为跨学科噪声（[1][2][4][5][6][7][8][9][13][14][15][16][17][19][20][24][27][28][29] 等）。这意味着**"对某方向是否无进展"的判断本身不可靠**——噪声会伪装成"已检索但无结果"。
- **推荐度**：作为方法论告警 ★★★★☆；作为技术证据 ★☆☆☆☆。

**4.2 模型基控制的体系化压力（理论侧）**
MPC 综述明确指出其处理对象为"非线性约束系统的动态运行"，涵盖从参考信号跟踪到一般经济优化 [11]。这提示模型基控制的方法论框架仍在扩展，但**该文献为 2023 年、非机器人专用、非窗口内增量**，不能用于论证 2024–2026 的机器人 MPC 进展 [11]。
- **权威**：arXiv（eess.SY）预印本，综述性质，同行评审状态 `> 待核实` [11]；**关注度待核实**；**推荐度 ★★★☆☆**。

**4.3 学习控制向高动态全身任务渗透（早期信号，未验证）**
[30] 的标题显示其以"退火强化学习课程"处理人形全身羽毛球任务，若成立，则属"学习控制从准静态操作扩展到高动态全身技能"的信号 [30]。但**是否为真机、任务成功率、对手设置、baseline 对比均未入集** `> 待核实` [30]。
- **可证伪拐点信号**：若 12 个月内出现该工作的第三方复现或独立榜单成绩，则"学习式 WBC 进入可比评测阶段"成立；否则仍属 demo 级证据 [30]。

**4.4 明确无证据的瓶颈项**
- ROS 2 executor / DDS 的实时性开销量化对比 `> 待核实`。
- Zenoh 作为 DDS 替代的实测数据与迁移案例 `> 待核实`。
- 仿真到真机（sim-to-real）迁移的失败案例汇编 `> 待核实`。

---

## 5. 社会·政策·国际（Society, Policy & Geopolitics）

**增量判断**：本周期内**没有任何机器人功能安全标准（如 ISO 10218 系列）、出口管制或行业监管的一手来源入集**，该维度基本为空白；仅有一条 AI 治理侧的间接信号。

**5.1 AI 治理与透明度压力（间接信号）**
《2025 Foundation Model Transparency Index》是年度透明度评估的第三版，新增与数据获取相关的指标，用于量化基础模型开发者的透明度实践 [14]。
- **热度证据**：候选块未提供引用/下载数据 `> 待核实` [14]。
- **权威证据**：arXiv（cs.AI）预印本，候选块未显示同行评审 venue，**B 级** [14]。
- **关注度**：**待核实** — 属 AI 治理议题，与机器人标准体系无直接映射 [14]。
- **推荐度**：**★☆☆☆☆（对本主题）** — 与运动学/控制/ROS 2 无技术关联；仅在讨论"基础模型进入机器人后所面临的透明度与合规压力"时可作类比引用 [14]。

**5.2 明确缺失项**
- ISO 10218（工业机器人安全）最新修订版本号与生效日期：**本轮无来源** `> 待核实`。
- 医疗机器人监管路径（[22] 所述手术辅助流水线是否受 FDA/CE/NMPA 约束）：**候选块未提供** `> 待核实` [22]。
- 机器人相关出口管制、供应链（减速器/伺服/芯片）与地缘政治影响：**本轮无来源** `> 待核实`。

---

## 6. 资本与生态（Capital & Ecosystem）

**增量判断**：**本周期无显著可核变化**。无融资额、并购、人才流动或公司格局的一手来源入集，任何相关陈述都将构成编造。

**6.1 生态侧的弱可核信号**
- **工具链延续性**：MoveIt 生态在 2019 年即产出紧耦合抓取框架 [23]，并在 2026 年的 ROS 2 Humble 流水线中继续作为机械臂控制组件被使用 [22]。这可支持"MoveIt 作为 ROS 操作栈事实标准具有跨版本延续性"的**弱判断**，但**不能**用于推断维护活跃度或市场份额 [22][23]。
- **垂直行业渗透**：ROS 2 出现在手术辅助原型中 [22]，属"研究中间件向受监管行业渗透"的单点证据；**无商业化、无量产、无客户数** `> 待核实` [22]。

**6.2 明确缺失项**
- ros2_control / Nav2 / Pinocchio / Drake / MuJoCo / Isaac ROS / micro-ROS 的 star 数、提交频率、发布节奏：**本轮无来源** `> 待核实`。
- 机器人中间件与运动控制领域的融资、并购、人才流动：**本轮无来源** `> 待核实`。
- 开源基金会治理变化（如 OSRA 等）：**本轮无来源** `> 待核实`。

---

## 7. 信号与预测（Signals & Forecast）

**增量判断**：本报告能给出的**不是趋势结论，而是三条可证伪的观察假设**，每条都明确标注了当前证据缺口。

**7.1 早期信号清单（证据强度：低）**
| 信号 | 时间 | 证据强度 | 依据 |
|---|---|---|---|
| ROS 2 + MoveIt2 进入医疗垂直原型 | 2026 [22] | 低（预印本、citations=0、无临床数据） | [22] |
| 人形全身高动态任务采用 RL 课程学习 | 2025-11 [30] | 低（仅标题级，无指标/真机信息） | [30] |
| 模型基控制方法论仍在综述层面体系化 | 2023 [11] | 中低（非机器人专用、窗口外） | [11] |
| 移动端/工业侧实时监测需求持续 | 2018 [25][26] | 低（与本主题技术栈无交集） | [25][26] |

**7.2 可证伪预测（[P]，附依据链与置信度）**

- **[P-1] 运动学求解器基准空白假设**（置信度：**推测**）
  依据链：本轮"inverse / kinematic"检索全部落入数学与天体物理 [4][5][7][9] → 说明该术语在通用检索中未被机器人语义主导 → 若社区存在活跃的 IK 横向基准，理应更易被召回 → 而实际零命中。
  **可证伪条件**：若 2027-10 前出现经同行评审（ICRA/RSS/CoRL/IROS）的 IK 求解器横向对比，报告成功率与耗时分位数并覆盖 KDL/TRAC-IK/优化类求解器，则本假设被推翻，判定"运动学求解器重新成为评测焦点"。

- **[P-2] 实时中间件拐点假设**（置信度：**未知**，证据不足）
  依据链：ROS 2 DDS 实时性与 Zenoh 替代的讨论在本轮**零来源** `> 待核实` → 无法判断该议题处于"已被解决"还是"仍在争论"。
  **可证伪条件**：若 ROS 官方文档或 REP 出现可核查的中间件选型/默认实现变更公告，则"实时中间件进入拐点"成立；若两年内仅有社区帖而无官方变更，则判定为持续性争论而非拐点。

- **[P-3] 学习式 WBC 可比化假设**（置信度：**推测**）
  依据链：[30] 显示学习方法已触及人形高动态全身任务 → 但候选块无任务数、本体、成功率、真机与否 → 当前属"演示级"。
  **可证伪条件**：若 12 个月内出现 [30] 类工作的第三方复现或独立榜单（含真机量化指标），则"学习式全身控制进入可比评测阶段"成立；若仅有视频演示累积而无量化对比，则判定其仍停留在 demo 阶段。

**7.3 不确定性声明**
- 本轮候选集的召回污染率约 80%（24/30），任何"某方向无进展"的判断都可能是检索失败而非事实 [1][2][4][5][6][7][8][9][13][14][15][16][17][19][20][24][27][28][29]。
- 本报告**未**对 2024–2026 年机器人运动学、MPC/WBC、ROS 2 发行版演进的实质进展作出任何肯定性结论；相关章节的全部技术判断均为 `> 待核实`。
- 建议下一轮检索以 ROS 官方文档/REP、MoveIt 2 与 ros2_control 官方仓库 release notes、ICRA/IROS/RSS/CoRL 会议论文集为**强制一手来源**，并对每个 SOTA 追问"benchmark / 硬件 / 任务数 / 是否真机"。

---

## 参考来源

[1] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1
[2] A rich bounty of AGN in the 9 square degree Bootes survey — http://arxiv.org/abs/astro-ph/0611654v1
[3] AIn't Nothing But a Survey? Using Large Language Models for Coding German Open-Ended Survey Responses — http://arxiv.org/abs/2506.14634v3
[4] Inversion of the star transform — http://arxiv.org/abs/1401.7655v2
[5] The Kinematic Morphology-Density Relation from the SAMI Pilot Survey — http://arxiv.org/abs/1409.7271v1
[6] The Methanol Multibeam Survey — http://arxiv.org/abs/1210.0979v1
[7] Inversion formulas for the broken-ray Radon transform — http://arxiv.org/abs/1007.4183v1
[8] The Dark Energy Survey — http://arxiv.org/abs/astro-ph/0510346v1
[9] Inverse spectral problems for Sturm-Liouville operators with singular potentials — http://arxiv.org/abs/math/0211247v1
[10] Control of a Rigid Wing Pumping Airborne Wind Energy System in all Operational Phases — http://arxiv.org/abs/2006.11141v1
[11] Analysis and design of model predictive control frameworks for dynamic operation -- An overview — http://arxiv.org/abs/2307.03004v2
[12] On Controller Design for Systems on Manifolds in Euclidean Space — http://arxiv.org/abs/1807.03475v1
[13] NTIRE 2025 Challenge on Image Super-Resolution (x4): Methods and Results — http://arxiv.org/abs/2504.14582v3
[14] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1
[15] The AudioMOS Challenge 2025 — http://arxiv.org/abs/2509.01336v1
[16] VLSP 2025 MLQA-TSR Challenge: Vietnamese Multimodal Legal Question Answering on Traffic Sign Regulation — http://arxiv.org/abs/2510.20381v1
[17] TDCOSMO 2025: Cosmological constraints from strong lensing time delays — http://arxiv.org/abs/2506.03023v4
[18] TRUST 2025: SCRITA and RTSS @ RO-MAN 2025 — http://arxiv.org/abs/2509.11402v1
[19] SINAI at eRisk@CLEF 2025: Transformer-Based and Conversational Strategies for Depression Detection — http://arxiv.org/abs/2509.19861v1
[20] Automated Classification of Normal and Atypical Mitotic Figures Using ConvNeXt V2: MIDOG 2025 Track 2 — http://arxiv.org/abs/2508.18831v1
[21] The Synthesis of Optimal Control Laws Using Isaacs' Method for the Solution of Differential Games — http://arxiv.org/abs/2112.10849v2
[22] Surgical Vision ROS2: a ROS2 Humble pipeline for intraoperative wound assessment and variable-autonomy arm control — https://doi.org/10.21203/rs.3.rs-10362132/v1
[23] Introducing MoveIt Grasps, a manipulation framework tightly integrated with MoveIt — https://doi.org/10.36288/roscon2019-900894
[24] Real-Time Service Subscription and Adaptive Offloading Control in Vehicular Edge Computing — http://arxiv.org/abs/2512.14002v1
[25] Real time state monitoring and fault diagnosis system for motor based on LabVIEW — http://arxiv.org/abs/1806.09998v1
[26] Real-Time-Data Analytics in Raw Materials Handling — http://arxiv.org/abs/1802.00625v1
[27] A Simulation and Modeling of Access Points with Definition Language — http://arxiv.org/abs/1304.1836v2
[28] Superconductivity as a consequence of an ordering of the electron gas zero-point oscillations — http://arxiv.org/abs/1005.0280v6
[29] Toward Real-Time Image Annotation Using Marginalized Coupled Dictionary Learning — http://arxiv.org/abs/2304.06907v2
[30] Humanoid Whole-Body Badminton via an Annealed Reinforcement Learning Curriculum — http://arxiv.org/abs/2511.11218v4

---

*Generated by research-bot · topic=`机器人运动学控制与-ros-2` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`deepseek-v4-flash` · sources=30 · duration=201s · 2026-10-23T22:25:49+00:00*
