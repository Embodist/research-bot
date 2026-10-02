# 机器人运动学、动力学与控制：经典奠基、近两年前沿与开源工具链调研报告

**日期**：2026-10-02（UTC）　**领域**：Robotics Kinematics / Dynamics / Control（FK/IK、旋量理论、雅可比与奇异性、轨迹优化、全身控制 WBC）　**检索源数量**：36 条候选来源记录（去噪后与主题直接相关者约 15 条，其余为域偏移或同名词条噪声）

---

## 摘要（Executive Summary）

1. **本次调研的证据基础存在系统性缺口，报告结论的可信度必须按来源分级解读。** 36 条候选来源中，仅少数与"机器人运动学/动力学/控制"直接相关；其余包括高能物理实验论文 [4][8][12]、英文词典与百科词条 [1][5][9][13]、天体物理与童话条目 [29][30][34]、以及内容被哈希截断的检索片段 [16][22]。这意味着对**前沿方向**的判断在本轮中多数只能标注 `> 待核实`，而不能给出实质结论。

2. **唯一可直接使用的近期（近 1–2 年）一手前沿证据是关于整臂操作的运动学感知扩散策略**：*Kinematics-Aware Diffusion Policy with Consistent 3D Observation and Action Space for Whole-Arm Robotic Manipulation*（arXiv:2512.17568v1，2025-12-19 提交，cs.RO）[21]。其问题设定是：涉及本体避障或本体-物体交互的操作任务中，仅以末端执行器位姿建模不足，需要全臂运动学感知；而在关节空间学习动作又会带来"观测空间与动作空间不对齐"（unalignment）。该工作属"运动学先验 + 生成式策略 + 全身操作"的交叉点。**但其量化指标、任务数、本体/硬件平台、是否中稿、是否开源，在本轮候选证据中均缺失** `> 待核实`。

3. **多个被点名调研的前沿子方向在本轮**完全没有**获得证据**，包括：接触隐式轨迹优化（contact-implicit trajectory optimization）、SE(3) 等变策略（SE(3)-equivariant policy）、可微运动学/可微仿真（differentiable kinematics / simulation）、全身控制框架级对比与基准榜单、解析解 vs 学习式 IK 的路线争议、奇异性处理策略。这些方向一律标注 `> 待核实`，不可据本报告下结论。

4. **在经典与工程侧，本轮的可用锚点是清楚的**：旋量/指数积（PoE）的教材与教学资源链条完整 [2][3][6][7][10][11]；逆向运动学（IK）数值求解有同行评审的一手来源 TRAC-IK（Humanoids 2015，被引 286 次）[26]；开源栈有 Pinocchio [25][35]、Orocos KDL [27][32] 及社区库清单 [28]；IK 求解的启发式/元启发式分支有 BODE-CS [20]、IK-FA [36]、模糊自适应双足 IK [14] 等可核查条目。

5. **检索链路的域偏移是需要向委托方明确提示的方法论问题**：查询词 "product"（对应 Product of Exponentials）召回了词典与商品词条 [1][5][9]；"Pinocchio"（动力学库）召回了童话条目 [29][30] 与天体物理论文 [29]；"Drake"（机器人工具箱）召回了 Drake 方程 SETI 论文 [34]。后续补检必须采用带限定符的精确查询（如 `screw theory product of exponentials robotics`、`site:github.com stack-of-tasks/pinocchio`、`Drake robotics toolbox manipulation`），并优先走 arXiv API / GitHub API / OpenAlex 等结构化通道。

**证据分级说明**：本报告采用 A（同行评审/官方文档）、B（arXiv 预印本/官方仓库）、C（第三方复现/榜单/学位论文）、D（博客/社区帖）、E（不可用）五级。正文中每条论断均标注来源编号与等级；D/E 级来源仅作线索，不作结论支撑。

---

## 一、关键前沿进展

### 1.1 近 1–2 年（2024–2026）具备一手证据的进展

| 进展 | 时间 | 类型 | 证据等级 | 要点 |
|---|---|---|---|---|
| Kinematics-Aware Diffusion Policy（全臂操作） | 2025-12 | arXiv 预印本（cs.RO） | B | 提出在关节空间动作与 3D 观测/动作空间之间建立一致性，并将全臂运动学感知注入扩散策略，面向本体避障与本体-物体交互 [21] |

**说明与限定**：
- [21] 的核心论点（"只考虑末端位姿对策略学习不充分"；"关节空间学习动作存在观测-动作空间不对齐"）来自其摘要，属**论文自述**，尚无可核查的第三方复现或基准对比 `> 待核实`。
- 该工作的实验设置（任务数量、真机 or 仿真、机械臂型号、成功率口径）在本轮候选片段中**完全缺失**，因此**不能**将其写为"刷新了某项 SOTA" `> 待核实`。
- 是否已被 RSS/CoRL/ICRA/NeurIPS 等会议接收、是否有开源代码与权重，本轮无证据 `> 待核实`。

### 1.2 与运动学相关但非控制主线的近期线索

- **医疗手术并联机器人运动学分析**（arXiv:2406.02047v1，2024-06）：提供了专用并联机构运动学分析的近期一手预印本线索 [15]。其与通用 FK/IK、WBC 的关系需要阅读全文后才能定位 `> 待核实`。
- **微机器人逆运动学标定采用迭代学习方法**：仅见于文档分享站条目，无作者、年份、发表处，属 D/E 级线索，**不可作为结论依据** [17]。

### 1.3 本轮未获得任何证据的前沿方向（明确缺口）

以下均为本次调研**点名但对证据缺失**的方向，一律标注 `> 待核实`：

- **接触隐式轨迹优化（contact-implicit trajectory optimization）**：无候选条目涉及 contact-implicit、complementarity、接触力规划或可微接触模型 [21][13][16][17]。
- **SE(3) 等变策略（SE(3)-equivariant policy）**：无候选条目涉及 equivariance / symmetry / group-equivariant / SE(3) 相关方法 [13][16][17]。
- **可微运动学（differentiable kinematics）**：仅有词典释义 [13] 与中文科普 [19]，无任何机器人学意义的研究来源，**不能作为依据**。
- **全身控制（WBC）框架级新进展与基准**：本轮无框架对比、无基准榜单、无多库集成方案证据。

> **小结**：本轮"最新进展"章节的可交付内容实质只有一条 B 级证据 [21] 及两条弱线索 [15][17]。若要形成可信的前沿综述，必须先补齐 1.3 节列出的四类检索。

---

## 二、建模表示：DH vs 旋量/POE

### 2.1 旋量理论与指数积（PoE）——本轮最完整的证据链条

PoE 的两种标准表述在本轮均有教学资源佐证：

- **空间坐标系下的 PoE 公式**（Product of Exponentials Formula in the Space Frame）[10]；
- **末端执行器坐标系下的 PoE 公式**（Product of Exponentials Formula in the End-Effector Frame）[2][6]，其中 [6] 明确标注来自教材 *Modern Robotics: Mechanics, Planning, and Control* 的对应章节。

其经典理论出处为 Murray、Li、Sastry 的 *A Mathematical Introduction to Robotic Manipulation*（1994），本轮获得三个可访问链接：Lehigh 课程 PDF 全文 [3]、Taylor & Francis 开放获取专著页 [7]、FreeComputerBooks 书目页 [11]。该书是把刚体运动统一到 Lie 群 SE(3)/so(3) 与旋量坐标框架下的奠基性教材。

### 2.2 DH 参数法

> **证据缺口**：本轮候选中**没有**任何一条直接讨论 Denavit–Hartenberg（DH）参数法定义、建系规则或与 PoE 对比的一手来源。仅有的正运动学相关条目是 MATLAB delta 机器人正运动学的中文博客 [23]，属 D 级，且不涉及 DH vs PoE 的表述选择问题。

因此，关于"DH 与 PoE 各自的优劣（如 DH 需逐关节建系、相邻轴平行时的参数奇异性、PoE 与李代数/优化框架的天然契合）"的通行说法，**在本轮检索中未获得可核查出处** `> 待核实`。相关判断需以 [3][7][11] 教材正文与 [2][6][10] 教学章节为一级来源重新核对后再行陈述。

---

## 三、逆运动学：解析 / 数值 / 学习

### 3.1 数值 IK（本轮证据最扎实的分支）

- **TRAC-IK**：*TRAC-IK: An open-source library for improved solving of generic inverse kinematics*，发表于 2015 IEEE-RAS 15th International Conference on Humanoid Robots (Humanoids)，DOI `10.1109/humanoids.2015.7363472`，被引 286 次 [26]。其定位是"改进通用逆运动学求解"的开源库，工程上常被用于替代 Orocos KDL 的默认 IK 求解器 [26][32]。这是本轮**唯一**具备同行评审出处且直接对应"开源数值/运动学库 + 数值 IK"议题的一手证据（A/B 级）。

### 3.2 启发式与元启发式 IK

当解析解不可得、且梯度类数值 IK 易陷入局部极小或对初值敏感时，一类工作转向随机/群体智能搜索：

| 方法 | 年份 | 出处 | 链接/编号 | 说明 |
|---|---|---|---|---|
| BODE-CS Algorithm | 2023 | *Machines*（MDPI） | [20] | 基于 BODE-CS 算法的机械臂逆运动学求解 |
| IK-FA（Firefly Algorithm） | 2015 | Springer 章节 | [36] | 使用萤火虫算法的启发式 IK 求解器 |
| 模糊自适应算法（双足机器人 IK） | 2010 | 《机器人》期刊（DOI 前缀 10.3724/sp.j.1218） | [14] | 模糊自适应策略用于双足机器人逆运动学 |

> 上述三者的**性能口径（收敛率、求解时间、是否真机验证、对比基线）在本轮候选证据中均未提供**，不能用于横向性能比较 `> 待核实`。它们仅能证明"IK 求解存在非梯度、启发式分支"这一事实性判断。

### 3.3 解析 IK 与专用机构

- 医疗微创手术并联机器人的运动学分析（arXiv:2406.02047v1，2024-06）[15] 属专用机构解析/半解析运动学建模的近期预印本线索，具体方法（几何法/代数法/数值校验）与验证口径 `> 待核实`。
- 逆运动学工作流的流程示意可由 [31] 提供，但该来源为论文配图页，仅具示意价值（D 级）。

### 3.4 学习式 IK 与"解析 vs 学习"的路线争议

> **证据缺口**：本轮候选中**不存在**任何以神经网络/学习方式直接求解 IK 并能与数值或解析基线对比的一手来源（[21] 属策略学习，不是 IK 求解器，且解决的是动作空间表征问题）。因此，"解析解 vs 学习式 IK 哪条路线更优"这一争议**在本轮无法给出任何有证据的判断** `> 待核实`，需要针对 `learning inverse kinematics`、`neural IK solver benchmark` 等查询补检。

---

## 四、轨迹规划与最优控制

### 4.1 多接触最优控制（种子资源，未实时核验）

领域种子资源中，**Crocoddyl**（LAAS-CNRS，2020）被列为"高效通用的多接触最优控制框架"，其论文为 *Crocoddyl: An Efficient and Versatile Framework for Multi-Contact Optimal Control*（arXiv:1909.04947），官方实现位于 `loco-3d/crocoddyl`。

> 该条目来自委托方提供的领域种子清单，**本轮检索未获得其一手页面内容的实时核验**，因此其版本状态、维护活跃度与基准结果 `> 待核实`。其与接触隐式优化的关系（是否采用接触序列给定 vs 接触序列优化）同样 `> 待核实`。

### 4.2 接触隐式轨迹优化（contact-implicit TO）

> **证据缺口（本次最大缺口之一）**：本轮候选来源中无一条涉及接触隐式优化、互补性约束（complementarity）、接触力平滑、可微接触仿真。该方向在 2024–2026 年的新进展**完全无法评估** `> 待核实`。建议补检查询：`contact-implicit trajectory optimization 2024..2026`、`complementarity robotics control site:arxiv.org`、`differentiable contact simulation robot`。

### 4.3 仿真到现实（sim-to-real）差距

- 埃塞克斯大学博士论文 *Bridging the Simulation to Reality Gap in Robotics* [33] 可作为 sim-to-real 问题的 C 级二手综述性材料，用于界定"轨迹优化在仿真中可行、真机部署受阻"的问题背景。其具体实验结论需阅读原文后引用 `> 待核实`。

---

## 五、全身控制与任务空间控制

### 5.1 操作空间控制（Operational Space Formulation，经典）

领域种子资源指出，Khatib 的操作空间/任务空间控制表述为 1987 年奠基工作（DOI `10.1109/JRA.1987.1087109`），是"把任务描述直接定义在操作空间、并在该空间设计控制律"的源头。

> 本轮**未获得该文献正文或引用统计的实时核验**，其公式体系（操作空间惯性矩阵 Λ、零空间投影算子、任务优先级）在被引用处的具体形式 `> 待核实`。

### 5.2 冗余分解与全身控制（WBC）

> **证据缺口**：本轮无任何来源覆盖冗余分解（零空间投影、任务优先级、分层 QP）或 WBC 整体框架（例如基于 QP 的层次化全身控制、WBC 与 MPC 的耦合）。该方向的框架级对比、开源实现对照与基准结果一律 `> 待核实`。

### 5.3 唯一的交叉线索：策略学习侧的"全身"表述

[21] 从**策略学习**（而非优化控制）角度处理"整臂（whole-arm）"操作：其出发点是全身/全臂运动学感知与动作空间一致性 [21]，与本节的 WBC 优化控制路线属不同技术路线，**不可混为一谈**。

---

## 六、经典教材与奠基工作

| 名称 | 年份 | 机构/作者 | 链接 | 说明 |
|---|---|---|---|---|
| A Mathematical Introduction to Robotic Manipulation | 1994 | Murray, Li, Sastry | [3]（PDF）/ [7]（出版社 OA 页）/ [11]（书目页） | 旋量理论与指数积（PoE）的经典教材；将刚体运动统一到 SE(3)/so(3) 与旋量坐标框架 [3][7][11] |
| Modern Robotics: Mechanics, Planning, and Control | 2017 | Lynch & Park | 种子链接 `hades.mech.northwestern.edu`（本轮未实时核验） | 现代运动学与控制教材；其 PoE 章节（空间坐标系/末端坐标系两种表述）有教学视频资源 [2][6][10] |
| Task Space Control / Operational Space Formulation | 1987 | Oussama Khatib | 种子链接 `doi.org/10.1109/JRA.1987.1087109`（本轮未实时核验） | 操作空间控制的奠基性表述 `> 待核实` |
| TRAC-IK: An open-source library for improved solving of generic inverse kinematics | 2015 | Humanoids 2015（IEEE-RAS） | [26] | 通用 IK 数值求解的同行评审一手来源，被引 286 次 [26] |
| Crocoddyl: An Efficient and Versatile Framework for Multi-Contact Optimal Control | 2020 | LAAS-CNRS | 种子链接 `arxiv.org/abs/1909.04947`（本轮未实时核验） | 多接触最优控制框架 `> 待核实` |
| Fuzzy Adaptive Algorithm for Biped Robot Inverse Kinematics | 2010 | 《机器人》期刊 | [14] | 模糊自适应 IK 分支的代表性条目 |
| IK-FA, a New Heuristic Inverse Kinematics Solver Using Firefly Algorithm | 2015 | Springer | [36] | 元启发式 IK 求解 |
| Inverse Kinematics of Robot Manipulator Based on BODE-CS Algorithm | 2023 | *Machines* (MDPI) | [20] | 元启发式 IK 求解 |

---

## 七、开源库与工具链对比

### 7.1 开源项目

| 名称 | 年份/状态 | 机构/作者 | 链接 | 说明 |
|---|---|---|---|---|
| Pinocchio | 活跃开源项目 | stack-of-tasks | [25] / [35]（中文入门教程） | 刚体动力学算法及其**解析导数**的高效实现，官方自述见 [25]；国内工程侧有入门教程传播（CSDN，2023-12-25，阅读 2.2 万）[35] |
| Orocos KDL | 经典开源库 | orocos | 种子链接 `github.com/orocos/orocos_kinematics_dynamics`；中文实践见 [27][32] | 提供 FK/IK/Jacobian；其默认 IK 常被 TRAC-IK 替代 [26][32] |
| TRAC-IK | 2015 | TRACLabs 等 | [26] | 改进通用 IK 求解的开源库，同行评审出处 |
| Drake | 活跃开源项目 | RobotLocomotion | 种子链接 `github.com/RobotLocomotion/drake` | 优化与控制的 C++ 工具箱；**本轮检索被 Drake 方程（SETI）文献污染 [34]，未获得其技术内容证据** `> 待核实` |
| Crocoddyl | 2020 | LAAS-CNRS | 种子链接 `github.com/loco-3d/crocoddyl` | 多接触最优控制 `> 待核实` |
| MoveIt 2 | 活跃开源项目 | moveit | 种子链接 `github.com/moveit/moveit2` | ROS2 运动规划框架 `> 待核实` |
| awesome-robotics-libraries | 社区维护 | jslee02 | [28] | 机器人软件库汇总清单，可作为工具链盘点的检索入口 [28] |

### 7.2 定位辨析（有证据支撑的一条）

Pinocchio 与 TRAC-IK **面向运动学/动力学栈的不同环节**：前者提供刚体动力学算法及其解析导数，供优化与控制层使用 [25]；后者专攻通用逆运动学的数值求解 [26]。二者公开描述中不存在功能重叠声明，属互补关系而非同类替代 [25][26]。

### 7.3 缺口

> 本轮**未获得任何可复核的性能基准**：既无 IK 求解的成功率/耗时对比，也无动力学库（Pinocchio / Drake / KDL / MuJoCo MJX）的吞吐或精度基准。这直接导致：
> - 无法对库做定量选型建议 `> 待核实`；
> - MuJoCo / MJX **在本轮

## 参考来源

[1] product _百度百科 — https://baike.baidu.com/item/product/10552047
[2] Chapter 4.1.2- Product   of   Exponentials Formula  in the End-Effector Frame-教育-高清完整正版视频在线观看-优酷 — https://v.youku.com/v_show/id_XMzAzMjE2NTIyMA==.html
[3] A Mathematical Introduction to Robotic Manipulation — https://www.cse.lehigh.edu/~trink/Courses/RoboticsII/reading/murray-li-sastry-94-complete.pdf
[4] Measurement of inelastic scattering $Λ(\overlineΛ)+p\toΣ^{0}(\overlineΣ^{0})+p$ via $e^+e^-\to J/ψ\toΛ\overlineΛ$ — http://arxiv.org/abs/2609.02584v1
[5] product 是什么意思_ product 的翻译_音标_读音_用法_例句_爱 ... — https://www.iciba.com/word?w=product
[6] Product   of   Exponentials Formula  in the End-Effector Frame-Modern Robotics: Mechanics, Planning, and Control-EEWORLD大学堂 — https://m.eeworld.com.cn/training/video/20505
[7] A Mathematical Introduction to Robotic Manipulation — https://www.taylorfrancis.com/books/oa-mono/10.1201/9781315136370/mathematical-introduction-robotic-manipulation-richard-murray-zexiang-li-shankar-sastry
[8] Evidence of $ψ(3770) \to π^{0}J/ψ$ — http://arxiv.org/abs/2606.14105v1
[9] PRODUCT 中文 (简体)翻译：剑桥词典 - Cambridge Dictionary — https://dictionary.cambridge.org/zhs/%E8%AF%8D%E5%85%B8/%E8%8B%B1%E8%AF%AD-%E6%B1%89%E8%AF%AD-%E7%AE%80%E4%BD%93/product
[10] Chapter 4.1.1- Product   of   Exponentials Formula  in the Space Frame-创意视频-高清完整正版视频在线观看-优酷 — https://v.youku.com/v_show/id_XMzAzMjE1MTI2NA==.html
[11] A Mathematical Introduction to Robotic Manipulation — https://freecomputerbooks.com/A-Mathematical-Introduction-to-Robotic-Manipulation.html
[12] Measurement of the CKM angle $γ$ in $B^{\pm} \rightarrow D(\rightarrow K^{0}_{\rm S} h^{\prime+}h^{\prime-})h^{\pm}$ decays with a novel approach — http://arxiv.org/abs/2604.05701v1
[13] differentiable _百度百科 — https://baike.baidu.com/item/differentiable/52804600
[14] Fuzzy Adaptive Algorithm for Biped Robot Inverse Kinematics — https://doi.org/10.3724/sp.j.1218.2010.00534
[15] Kinematic analysis of a parallel robot for minimally invasive surgery — http://arxiv.org/abs/2406.02047v1
[16] 2024  年7月18日  Arxiv  人工智能相关论文_missing modality prediction for ... — hedJjaC291OB0PrGj_c3jKeWGo0CNeeAAoqVgpLQv06uSdKpCMIsLgMyACwDQkWHJZh-w3FxLBat5pUc3zy0dg..
[17] Calibration of Micro- robot   Inverse Kinematics  Using Iterative  Learning  Approach - 道客巴巴 — https://www.doc88.com/p-1661760421493.html
[18] Video-Based Markerless Motion Capture for Clinical and ... - arXiv — https://arxiv.org/pdf/2609.18667
[19] 连续，可微，可导和处处可导有什么区别和联系？ - 知乎 — https://zhuanlan.zhihu.com/p/653506292
[20] Inverse Kinematics of Robot Manipulator Based on BODE-CS Algorithm — https://doi.org/10.3390/machines11060648
[21] Kinematics-Aware Diffusion Policy with Consistent 3D Observation and Action Space for Whole-Arm Robotic Manipulation — http://arxiv.org/abs/2512.17568v1
[22] 深度  学习   |   arxiv2024   | Vision_xLSTM即插即用模块,适用于医学图像分... — hedJjaC291ObqPUCEo1zMuraEuczo-4WCU_PNz9JM0tEJsKMgtD2QwWx5lbW4vEA
[23] [ robot ] review forward  kinematics _matlab deltarobotforward-CSDN博客 — https://blog.csdn.net/myjiayan/article/details/72553018
[24] Self-Supervised Distillation of Biomechanical Pose from a 3D Body ... — https://arxiv.org/pdf/2608.29928
[25] GitHub - stack-of-tasks/ pinocchio : A fast and flexible … — https://github.com/stack-of-tasks/pinocchio
[26] TRAC-IK: An open-source library for improved solving of generic inverse kinematics — https://doi.org/10.1109/humanoids.2015.7363472
[27] orocos _ kdl 学习(一):坐标系变换-CSDN博客 — https://blog.csdn.net/weixin_33888907/article/details/94562409
[28] awesome-robotics-libraries/README.md at main - GitHub — https://github.com/jslee02/awesome-robotics-libraries/blob/main/README.md
[29] PINOCCHIO and the hierarchical build-up of dark matter haloes — http://arxiv.org/abs/astro-ph/0109324v1
[30] 木偶奇遇记（卡洛·科洛迪著童话）_百度百科 — https://baike.baidu.com/item/%E6%9C%A8%E5%81%B6%E5%A5%87%E9%81%87%E8%AE%B0/81187
[31] Figure 1: A diagram illustrating the working principle of the inverse kinematics (IK) workflow. — https://doi.org/10.7717/peerj.15097/fig-1
[32] 开源机器人库 orocos   KDL  学习笔记(五): Inverse  Kinematric_ orocos   kdl  逆解-CSDN博客 — https://blog.csdn.net/u014170067/article/details/83352636
[33] Bridging the Simulation to Reality Gap in Robotics — https://repository.essex.ac.uk/40339/1/KVasios-PhD.pdf
[34] Area Coverage of Expanding E.T. Signals in the Galaxy: SETI and Drake's N — http://arxiv.org/abs/1802.09399v2
[35] 从零上手机器人动力学库 pinocchio （一） pinocchio 简介 ... — https://blog.csdn.net/carrot1128/article/details/132796851
[36] IK-FA, a New Heuristic Inverse Kinematics Solver Using Firefly Algorithm — https://doi.org/10.1007/978-3-319-11017-2_15


---

*Generated by research-bot · topic=`kinematics` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading · model=`deepseek-v4-flash` · sources=36 · duration=296s · 2026-10-02T04:36:11+00:00*
