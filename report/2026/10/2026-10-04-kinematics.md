# 机器人运动学、动力学与控制：方法演进、开源栈盘点与 2024–2026 前沿追踪

**日期**：2026-10-04（UTC）｜**领域**：Robotics Kinematics / Dynamics / Control（具身智能基础栈）｜**检索源数量**：可引用编号来源 17 条（[1]–[17]），覆盖 6 个子问题（q1–q6）｜**证据可用性声明**：本次检索对核心主题（FK/IK、旋量理论、雅可比与奇异性、全身控制、开源库对比、数据集基准）**未产出可核查的一手证据**；仅「接触隐式轨迹优化（CITO）」与「可微仿真」两条支线有可引用命中 [10][11][12][13][15][16][17]。本报告因此采取**缺口地图（gap map）+ 可信来源清单**的写法，凡无编号来源支撑的论断一律标注 `> 待核实`，不做记忆化断言。

---

## 摘要（Executive Summary）

1. **本次调研的证据覆盖率严重不均衡。** 6 个子问题中，q3（开源数值库盘点）、q4（数据集与基准）、q6（开放问题与失败案例）**返回零条发现**；q2（旋量/POE/操作空间控制奠基文献）仅命中一个与主题无关的个人参考文献集合仓库 [1]；q1（前沿进展）命中的 6 条中 5 条属机器人学习/导航/绳结操作等**主题漂移文献**（[2][3][5][7][8]），另 1 条 [9] 已被 arXiv 管理员**以虚构内容为由撤稿**（E 级证据，应直接丢弃）。唯一有效覆盖集中在 q5。

2. **唯一证据充分的前沿支线是接触隐式轨迹优化（Contact-Implicit Trajectory Optimization, CITO）。** 2024–2026 年该方向有连续产出：SQP 全局收敛性分析 [11]（2024，citations=1）、单轨两轮机器人斜坡跳跃姿态控制 [10]（2024，citations=1）、四足无固定接触序列框架 [16]（2025，citations=0）、IMPACT 隐式主动集增广拉格朗日 [17]（2026，citations=2）、分布式接触丰富轨迹优化 DisCo [12] 与非脉冲接触隐式运动规划 [13]（均见来源列表，内容未抽取）。**该方向仍是小体量、低引用、以仿真/单平台验证为主的早期领域**[10][11][16][17]。

3. **可微仿真（Differentiable Simulation）是与 CITO 相邻的活跃支线**[15]（2024，citations=12，本次命中中引用数最高的条目），但同样未提供真机对比口径。

4. **运动学主干（旋量理论、POE 建模、雅可比与奇异性、解析/数值/学习式 IK、任务空间控制）在本次检索中完全无一手证据。** 相关结论只能依赖领域种子资源清单（Murray–Li–Sastry 1994、Lynch–Park 2017、Khatib 1987、Crocoddyl 2020 等），**这些条目不占用 [n] 编号，且本次未做实时核实**，全部标 `> 待核实`。

5. **选型建议在本轮证据下只能给出「不可决策」级别结论。** 对 Pinocchio / Drake / MuJoCo / TRAC-IK / IKFast / Crocoddyl / OCS2 / CasADi / RBDL / Orocos KDL / JAX 生态的能力边界、性能与维护活跃度，本次**未获取任何 star 数、提交频率、许可证、基准数字**，故不提供排名或定量对比，仅给出下一轮检索的可执行清单（见第八节）。

---

## 一、关键前沿进展（近 1–2 年）

### 1.1 接触隐式轨迹优化（CITO）是本次唯一达到可陈述强度的方法线

CITO 将接触模式（contact mode）本身作为优化变量，无需预设接触序列，被视为富接触规划与控制的统一框架 [17]。

| 条目 | 年份 | venue / 来源 | 热度证据 | 权威证据 | 关注度 | 推荐度 |
|---|---|---|---|---|---|---|
| IMPACT: An Implicit Active-Set Augmented Lagrangian for Fast Contact-Implicit Trajectory Optimization [17] | 2026 | arXiv 预印本（编号 2605.09127） | citations=2（候选块字段）[17] | arXiv 预印本，未标注同行评审 [17] | 低 —— 依据：citations=2 [17] | ★★★☆☆ —— 主题高度相关且时间最新，但引用极少、未经同行评审，适合作为入口而非结论依据 [17] |
| A Novel Contact-Implicit Trajectory Optimization Framework for Quadruped Locomotion without Fixed Contact Sequences [16] | 2025 | Advanced Intelligent Systems（期刊，据候选块字段） | citations=0 [16] | 期刊论文（候选块标注 Advanced Intelligent Systems）[16] | 低 —— 依据：citations=0 [16] | ★★★☆☆ —— 与「四足 + 无固定接触序列」直接对应，但零引用，需等待独立验证 [16] |
| Global Convergence of an SQP Method for Contact-Implicit Trajectory Optimization [11] | 2024 | arXiv 预印本 2406.01763 | citations=1 [11] | arXiv 预印本，未标注同行评审 [11] | 低 —— 依据：citations=1 [11] | ★★★★☆ —— CITO 收敛性理论刻画是领域公认难点（其摘要明示现有公式依赖商业 NLP 求解器或缺乏保证）[11]，方法论价值高 |
| Ramp Jump Attitude Control of Single-Track Two-Wheeled Robot via Contact-Implicit Trajectory Optimization [10] | 2024 | IEEE ROBIO 2024（会议，DOI 10.1109/ROBIO64047.2024.10907480） | citations=1 [10] | 同行评审会议论文 [10] | 低 —— 依据：citations=1 [10] | ★★★☆☆ —— 提供非足式平台（单轨两轮）的落地案例，可作跨本体适用性线索 [10] |

**方法学解读（限定表述）**：CITO 的共识性痛点是**收敛性难以刻画**——现有工作在「用现成非线性规划求解器（其保证不适用于接触问题）」与「自研方法缺乏收敛保证」之间取舍 [11]；IMPACT 的切入点是把主动集（active-set）内隐化并配合增广拉格朗日以提速 [17]。**上述均为论文自述（B 级证据），无第三方复现或榜单验证** `> 待核实`。

### 1.2 相邻支线：可微仿真与失败恢复

- **Highly-Efficient Differentiable Simulation for Robotics [15]**（2024，arXiv 2409.07107）：摘要指出「高效且准确地计算仿真导数仍是开放挑战」[15]。热度：citations=12（候选块字段）；权威：arXiv 预印本，候选块未标注 venue；关注度：中（本次命中中引用最高）；推荐度 ★★★☆☆——与本主题（轨迹优化需要梯度）相关，但需核实是否含真机与 ROS2 集成 [15]。
- **Fall prediction, control, and recovery of quadruped robots [14]**（2024，ISA Transactions，DOI 10.1016/j.isatra.2024.05.039）：摘要称提出面向非结构化环境的跌倒决策与控制框架 [14]。热度：citations=15（本次最高）；权威：同行评审期刊；关注度：中；推荐度 ★★★☆☆——属「失败案例」类稀缺证据，但需核实是否为真机实验 `> 待核实` [14]。

### 1.3 来源列表中主题相关但本轮未抽取内容的条目（仅登记标题，内容 `> 待核实`）

- **DisCo: distributed contact-rich trajectory optimization for forceful multi-robot collaboration**（arXiv 2410.23283，2024-10）[12]
- **Non-impulsive Contact-Implicit Motion Planning for Morpho-functional Loco-manipulation**（arXiv 2404.08714，2024-04）[13]
- **Robot Learning: A Tutorial**（arXiv 2510.12403，2025-10）[6]——可能覆盖学习式控制入口，但标题未限定运动学/动力学，相关性 `> 待核实`。
- **State-of-the-art in Robot Learning for Multi-Robot Collaboration: A Comprehensive Survey**（arXiv 2408.11822）[4]——多机协作综述，与本主题交集限于控制层 `> 待核实`。

### 1.4 **未获得任何证据的前沿点（重要缺口）**

以下均为研究目标点名、但本次检索**零命中**的方向，任何描述都属无证据推测，故仅记录缺口：

- 可微运动学（Differentiable Kinematics）`> 待核实`
- 学习式逆运动学（Learning-based IK）`> 待核实`
- SE(3) 等变策略（SE(3)-Equivariant Policy）`> 待核实`
- 实时全身 QP 控制（Real-time Whole-Body QP）`> 待核实`

### 1.5 证据质量警示（可复用的方法论结论）

命中条目 [9]（A Simulation and Modeling of Access Points with Definition Language）的摘要明示：**该投稿因包含虚构内容并冒名提交，已被 arXiv 管理员撤稿** [9]。该条属 E 级证据，应直接丢弃。这提示本领域关键词检索会显著受噪声污染，必须以「venue + DOI/arXiv 编号 + 撤稿状态」三重校验。

---

## 二、建模表示：DH 参数 vs 旋量理论 / 指数积（PoE）

**本节结论状态：`> 待核实`（本次零证据）。**

q2 检索未返回任何关于 screw theory、Product of Exponentials（PoE）、Jacobian 或 manipulability 的原始文献 [1]。唯一命中的仓库 [1] 是跨主题杂项参考文献合集：stars=43，个人维护、无机构背书、无同行评审，且内容为条目堆叠（含认知发展机器人学综述、4-D/RCS 架构等）[1]，**不构成本节证据**。

**可陈述的唯一事实**：本次检索**完全缺失**旋量理论与 PoE 的奠基文献记录（Ball 的螺旋理论著作、Brockett 的指数积公式化、Murray–Li–Sastry 教材脉络），亦缺失 DH 参数体系与旋量体系的可比性材料 [1]。`> 待核实`

**领域种子资源（不占用 [n] 编号，本次未实时核实，链接为用户提供的原始链接）**：

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| A Mathematical Introduction to Robotic Manipulation (screw theory / POE) | 1994 | Murray, Li, Sastry | `> 待核实` | 经典专著（种子清单） | `> 待核实` | ★★★★★（依据：种子清单标注为旋量/指数积经典教材，非本次检索一手证据） | https://www.cds.caltech.edu/~murray/mlswiki/ | 旋量/指数积经典教材 |
| Modern Robotics: Mechanics, Planning, and Control | 2017 | Lynch & Park | `> 待核实` | 现代教材（种子清单） | `> 待核实` | ★★★★★（依据同上） | http://hades.mech.northwestern.edu/index.php/Modern_Robotics | 现代运动学与控制教材 |

**下一轮检索建议（缺口的可执行补全路径）**：`screw theory robotics` + `site:arxiv.org`、`Product of Exponentials forward kinematics 2024..2026`、`DH parameters vs screw representation comparison`、`manipulability measure Yoshikawa`，并把 Crossref/IEEE Xplore 作为元数据（DOI、venue、引用数）来源。

---

## 三、逆运动学：解析 / 数值 / 学习式

**本节结论状态：`> 待核实`（本次零证据）。**

- 解析解（Analytical IK）与数值解（Numerical IK）的适用边界、闭式解存在条件、冗余自由度下的零空间处理：**无任何 [n] 级证据** `> 待核实`
- 学习式 IK：**无任何 [n] 级证据** `> 待核实`
- IK 求解精度口径（位置/姿态误差、成功率、迭代次数、超时率）：**无任何 [n] 级证据** `> 待核实`
- 常见工具（TRAC-IK、IKFast、KDL IK、Pinocchio IK 等）：仅见于研究目标与种子清单，本次**未获得 star 数、许可证、维护状态或性能数字**，故不做对比 [1]（[1] 仅提供与本主题无关的 43 stars 仓库数据）。

**🔍 关键提醒**：第 1.3 节登记的条目均未涉及 IK 求解器，因此**本报告不对「解析 vs 数值 vs 学习」给出任何倾向性结论**。任何未标注 [n] 的此类比较都属不可核查内容。

---

## 四、轨迹规划与最优控制

本节是本报告**唯一可实质展开**的技术章节，证据来自 q5 的 6 条命中（[10][11][14][15][16][17]）与来源列表中的 2 条登记条目（[12][13]）。

### 4.1 方法脉络（基于可引用摘要）

1. **问题设定**：CITO 作为「潜在接触任务中统一规划与控制」的框架受到越来越多关注，其吸引力在于**无需预先指定接触模式时间表（contact-mode schedule）** [17]。
2. **收敛性障碍**：CITO 的收敛行为难以刻画，现有公式化「要么依赖现成非线性规划求解器（其保证不覆盖接触问题），要么缺乏保证」[11]。
3. **求解器层创新**：IMPACT 提出隐式主动集（implicit active-set）+ 增广拉格朗日（augmented Lagrangian）以加速 [17]。
4. **本体扩展**：从足式（四足无固定接触序列 [16]）扩展到轮式跳跃（单轨两轮斜坡跳跃 [10]）与 loco-manipulation（非脉冲接触隐式运动规划 [13]）。
5. **梯度来源**：可微仿真为导数计算提供基础设施，但「高效且准确计算仿真导数仍是开放挑战」[15]。
6. **失败态处理**：四足跌倒的预测—控制—恢复一体化决策框架被提出，以应对非结构化环境中的不可避免跌倒 [14]。

### 4.2 证据强度评估

| 维度 | 状态 | 依据 |
|---|---|---|
| 真机验证 | **不可判定** | 全部 6 条命中中，仅 [14] 摘要提及「非结构化环境」但未明示真机；[16] 摘要提及「四足运动」未明示真机 `> 待核实` [14][16] |
| 任务数与本体数 | **不可判定** | 无任何命中提供任务数统计 `> 待核实` |
| 计算时间/实时性 | **不可判定** | IMPACT 摘要以「Fast」自述但未在抽取内容中给出数字 `> 待核实` [17] |
| 第三方复现/榜单 | **不存在** | 无任何命中提及权威榜单或独立复现 [10][11][14][15][16][17] |
| 引用体量 | **低** | citations：0–15（候选块字段），除 [14] 外均 ≤2 [10][11][14][15][16][17] |

### 4.3 对比与权衡的诚实结论

**本轮证据不支持「接触隐式 vs 接触显式」「优化 vs 学习」的定量比较。** 可陈述的仅是定位差异：CITO 的价值主张是免除接触序列预设 [17]，代价是收敛性刻画困难 [11]；学习式控制方向（[6] 教程 [4] 综述，内容 `> 待核实`）与本支线**尚无直接对照实验证据**。

---

## 五、全身控制与任务空间控制

**本节结论状态：`> 待核实`（本次零证据）。**

q6（开放问题与失败案例）与全身控制子问题均**返回零发现**。因此以下内容**全部为缺口登记**，不含结论：

- Operational Space Formulation（Khatib 1987）的后续演进与「任务空间 vs 关节空间」取舍：`> 待核实`（仅存于种子清单，链接 https://doi.org/10.1109/JRA.1987.1087109）
- 全身 QP（Whole-Body QP）的实时性预算、层级优先级（hierarchical task）与硬约束可行性：`> 待核实`
- 接触约束下的全身控制与 CITO 的耦合方式：**仅有间接线索**——[13] 标题含 "Morpho-functional Loco-manipulation"，提示存在接触隐式与 loco-manipulation 全身控制的交叉，但内容未抽取 `> 待核实` [13]
- 奇异性（singularity）处理、可操作度（manipulability）退化、任务优先级冲突：`> 待核实`

---

## 六、经典教材与奠基工作

**重要说明**：本表条目来自**用户提供的领域种子资源清单**，**不占用 [1]–[17] 引用编号**，且**本次未实时检索核实**。热度（引用数/star）与关注度**全部为 `> 待核实`**——不得以本表数字作为影响力判断依据。

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| A Mathematical Introduction to Robotic Manipulation (screw theory / POE) | 1994 | Murray, Li, Sastry | `> 待核实` | 经典专著（种子清单，非本次检索证据） | `> 待核实` | ★★★★★（依据：种子清单定位为旋量/POE 奠基教材） | https://www.cds.caltech.edu/~murray/mlswiki/ | 旋量/指数积经典教材 |
| Modern Robotics: Mechanics, Planning, and Control | 2017 | Lynch & Park | `> 待核实` | 现代教材（种子清单） | `> 待核实` | ★★★★★（依据：种子清单定位为现代运动学与控制教材） | http://hades.mech.northwestern.edu/index.php/Modern_Robotics | 现代运动学与控制教材 |
| Task Space Control / Operational Space Formulation | 1987 | Oussama Khatib | `> 待核实` | DOI 10.1109/JRA.1987.1087109（种子清单提供） | `> 待核实` | ★★★★★（依据：种子清单定位为操作空间控制奠基） | https://doi.org/10.1109/JRA.1987.1087109 | 操作空间控制奠基 |
| Crocoddyl: An Efficient and Versatile Framework for Multi-Contact Optimal Control | 2020 | LAAS-CNRS | `> 待核实` | arXiv 预印本 1909.04947（种子清单提供） | `> 待核实` | ★★★★☆（依据：与第四节 CITO/多接触最优控制主题直接相关） | https://arxiv.org/abs/1909.04947 | 接触最优控制 |

**证据缺口（对应 q2 的 open_problems）**：旋量理论奠基文献、PoE 公式化原始文献、操作空间控制系列工作、可操作度指标口径（定义式、量纲、适用范围）在本次检索中**全部缺失**，且缺乏可核验的引用数与 DOI 元数据 [1]。`> 待核实`

---

## 七、开源库与工具链对比

**核心声明**：q3 **返回零条发现**。因此本节**不提供任何性能、star 数、维护活跃度、许可证或基准对比**——任何此类数字都将是编造的。

唯一在本次检索中携带 star 数据的仓库是 [1]（stars=43，个人维护，跨主题杂项参考文献合集，与本主题无关）[1]，**不可用作工具链对比依据**。

**种子项目清单（不占用 [n] 编号，链接来自用户提供；所有热度/权威/关注度字段 `> 待核实`）**：

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| stack-of-tasks/pinocchio | `> 待核实` | stack-of-tasks | `> 待核实`（未获取 star/提交频率） | 官方 GitHub 仓库（种子清单） | `> 待核实` | ★★★★☆（依据：种子清单定位为刚体运动学/动力学 + 解析导数，与三、四、五节均相关） | https://github.com/stack-of-tasks/pinocchio | 刚体运动学/动力学，含解析导数 |
| orocos/orocos_kinematics_dynamics | `> 待核实` | Orocos 社区 | `> 待核实` | 官方 GitHub 仓库（种子清单） | `> 待核实` | ★★★☆☆（依据：种子清单定位为 KDL：FK/IK/Jacobian） | https://github.com/orocos/orocos_kinematics_dynamics | KDL：FK/IK/Jacobian |
| RobotLocomotion/drake | `> 待核实` | RobotLocomotion（Toyota Research Institute） | `> 待核实` | 官方 GitHub 仓库（种子清单） | `> 待核实` | ★★★★☆（依据：种子清单定位为优化与控制的 C++ 工具箱） | https://github.com/RobotLocomotion/drake | 优化与控制的 C++ 工具箱 |
| loco-3d/crocoddyl | `> 待核实` | LAAS-CNRS | `> 待核实` | 官方 GitHub 仓库（种子清单） | `> 待核实` | ★★★★☆（依据：与第四节多接触最优控制直接对应，其论文见第六节） | https://github.com/loco-3d/crocoddyl | 多接触最优控制 |
| moveit/moveit2 | `> 待核实` | MoveIt 社区 | `> 待核实` | 官方 GitHub 仓库（种子清单） | `> 待核实` | ★★★★☆（依据：种子清单定位为 ROS2 运动规划框架，工程落地相关） | https://github.com/moveit/moveit2 | ROS2 运动规划框架 |

**研究目标点名但本次无任何来源覆盖的库**（无链接即不列出，避免编造）：MuJoCo、TRAC-IK、IKFast、OCS2、CasADi、RBDL、JAX 生态 `> 待核实`。

**下一轮检索建议**：逐个仓库核查 `stars / last commit / license / 是否有 ROS2 绑定 / 是否提供 C++ 与 Python 接口`，并以官方文档（A/B 级）而非聚合站（D 级）为准。

---

## 八、开放问题与关注清单

### 8.1 开放问题（本次检索可直接确证的）

1. **CITO 的收敛性理论仍不完整**：现有公式化或依赖不覆盖接触问题的商用 NLP 求解器，或缺乏收敛保证 [11]。IMPACT 试图以隐式主动集 + 增广拉格朗日加速，但属自述性能 [17]。
2. **可微仿真的导数计算仍是开放挑战**（论文自述）[15]。
3. **无固定接触序列的四足运动仍处早期**：相关工作 2025 年发表时引用数为 0 [16]。
4. **足式机器人在非结构化环境中的跌倒不可避免**，预测—恢复一体化框架仍在提出阶段 [14]。

### 8.2 开放问题（本次**无证据**，纯缺口登记 `> 待核实`）

1. 解析解与数值解的取舍边界；闭式解存在性与冗余自由度处理 `> 待核实`
2. 经典几何方法与学习方法的取舍争议 `> 待核实`
3. 奇异性（singularity）处理的工程与理论方案 `> 待核实`
4. 实时性预算与安全性保障（尤其全身 QP 的硬约束可行性）`> 待核实`
5. 该领域**失败案例与负面结果**的系统性记录：本次唯一相关命中为四足跌倒恢复 [14]，其余为空白 `> 待核实`

### 8.3 检索质量与证据纪律问题（本次调研的方法学产出）

| 现象 | 具体证据 | 处置 |
|---|---|---|
| 主题漂移污染 | q1 命中 [2][3][5][7][8] 均为导航/模仿学习/绳结操作，与本主题无对应性 |

## 参考来源

[1] Aryia-Behroziuan/Other-sources — https://github.com/Aryia-Behroziuan/Other-sources
[2] One-Shot Reinforcement Learning for Robot Navigation with Interactive Replay — http://arxiv.org/abs/1711.10137v2
[3] On-Policy Robot Imitation Learning from a Converging Supervisor — http://arxiv.org/abs/1907.03423v7
[4] State-of-the-art in Robot Learning for Multi-Robot Collaboration: A Comprehensive Survey — http://arxiv.org/abs/2408.11822v1
[5] Multi-objective Model-based Policy Search for Data-efficient Learning with Sparse Rewards — http://arxiv.org/abs/1806.09351v3
[6] Robot Learning: A Tutorial — http://arxiv.org/abs/2510.12403v1
[7] Untangling Dense Knots by Learning Task-Relevant Keypoints — http://arxiv.org/abs/2011.04999v1
[8] Deception Game: Closing the Safety-Learning Loop in Interactive Robot Autonomy — http://arxiv.org/abs/2309.01267v2
[9] A Simulation and Modeling of Access Points with Definition Language — http://arxiv.org/abs/1304.1836v2
[10] Ramp Jump Attitude Control of Single-Track Two-Wheeled Robot via Contact-Implicit Trajectory Optimization — https://doi.org/10.1109/ROBIO64047.2024.10907480
[11] Global Convergence of an SQP Method for Contact-Implicit Trajectory Optimization — https://arxiv.org/abs/2406.01763
[12] DisCo: distributed contact-rich trajectory optimization for forceful multi-robot collaboration — https://arxiv.org/abs/2410.23283
[13] Non-impulsive Contact-Implicit Motion Planning for Morpho-functional Loco-manipulation — https://arxiv.org/abs/2404.08714
[14] Fall prediction, control, and recovery of quadruped robots. — https://doi.org/10.1016/j.isatra.2024.05.039
[15] Highly-Efficient Differentiable Simulation for Robotics — https://arxiv.org/abs/2409.07107
[16] A Novel Contact‐Implicit Trajectory Optimization Framework for Quadruped Locomotion without Fixed Contact Sequences — https://doi.org/10.1002/aisy.202500654
[17] IMPACT: An Implicit Active-Set Augmented Lagrangian for Fast Contact-Implicit Trajectory Optimization — https://arxiv.org/abs/2605.09127


---

*Generated by research-bot · topic=`kinematics` · depth=`standard` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading · model=`deepseek-v4-flash` · sources=17 · duration=855s · 2026-10-04T04:14:15+00:00*
