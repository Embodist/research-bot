# 机器人运动学、动力学与控制：奠基工作、2024–2026 前沿、工程栈与评测基准调研报告

> **日期**：2026-10-06（UTC） ｜ **领域**：Robotics — Kinematics / Dynamics / Control（运动学、动力学与控制） ｜ **检索源数量**：126 条编号来源（[1]–[126]）+ 主题 YAML 人工维护种子资源（教材 4 项、开源项目 5 项、数据集 1 项）
> **证据规则**：所有关键论断带 [n] 引用；引用编号仅限本次提供的 [1]–[126]。种子资源不在编号列表内，其链接来自主题 YAML，**未实时检索**，相关热度指标一律标 `> 待核实`。
> **检索偏差声明（重要）**：本次结构化发现中混入大量与本主题无关的命中——高能物理（[65][66][67][68][69][71][72]）、天体物理与宇宙学（[6][24][28][31][98][99]）、超导与量子光学（[86][122]）、图像/音频/法律 NLP 挑战赛（[4][43][45][46][89][90][96][125][108]）、非机器人最优控制（[116]）。这些条目已从正文结论中剔除，不作为任何论断依据。剔除后，**直接以「经典 FK/IK/旋量/雅可比/WBC」为主题的 2024–2026 命中偏少**，本报告在经典部分依赖教材/种子资源，并以 `> 待核实` 标注该结构性缺口。

---

## 摘要（Executive Summary）

1. **理论底座未变，但表达形式在迁移。** 旋量理论 / 指数积（Product of Exponentials, PoE）与操作空间控制（Operational Space Control, OSC）仍是现代系统教科书的骨架（种子资源：Murray-Li-Sastry 1994；Lynch & Park 2017；Khatib 1987）。工程侧出现明确的「脱离 DH、转向几何/元素变换序列（Elementary Transform Sequence, ETS）」趋势，其系统化表述见 [84]（2020），并在机器人自动设计中作为可优化表示被讨论 [63][64]。**权威证据**：教材与同行评审论文（种子资源 + [84][63][64]）；**热度证据**：`> 待核实`（未取到引用数）。

2. **奇异性处理正从「避开」转向「解析知情地穿越」。** [9]（arXiv 2412.20409，2024-12）提出在奇异位形处用解析信息增强逆运动学求解，是该主线近年最直接的一手工作。**权威证据**：arXiv 预印本（cs.RO），未见同行评审记录 `> 待核实`；**关注度**：中（主题命中本期检索关键词，引用数 `> 待核实`）；**推荐度**：★★★★☆（与主题高度相关）。

3. **学习型运动学生成已成主流范式，且开始显式注入运动学约束。** [2]（arXiv 2512.17568，2025-12）提出 Kinematics-Aware Diffusion Policy，强调「仅考虑末端位姿不足够」，需覆盖全臂运动学以支持避碰与臂-物交互；[16]（2022）以 SE(3) 等变能量模型（Equivariant Descriptor Fields）提供几何归纳偏置；[14][100] 分别从轨迹选择与少步生成（2-NFE）角度降低扩散/流匹配策略的推理代价。**权威证据**：均为 arXiv 预印本，[16] 为已发表方向的后续版本 `> 待核实`；**热度证据**：`> 待核实`。

4. **接触隐式轨迹优化（contact-implicit TO）在 2024–2026 出现方法论层面的硬进展**：全局收敛性证明（[120]，arXiv 2406.01763，2024-06）、快速内点/增广拉格朗日实现（[119] IMPACT，arXiv 2605.09127，2026-05）、多阶段混合与接触隐式统一（[121]，2023）、正交配点离散（[117]，2018）构成技术谱系；全身多接触操作的可扩展性见 [115]（2025-08）。**权威证据**：arXiv 预印本；[117] 为该方向被广泛引用的奠基实现 `> 待核实`（引用数未取到）。

5. **实时全身控制（WBC）出现「采样型 MPC 回归」信号。** [126]（arXiv 2409.10469，2024-09）报告了基于 Model-Predictive Path Integral（MPPI）的腿足机器人实时全身控制；人形侧集中在遥操作（[112] CHILD，2025-08）、无机器人演示的全身操作（[113] HMI，2026-02）、动态物体交互（[110] 羽毛球，2025-11）与空间理解+可泛化动作生成（[114]，2026-05）。具体实时频率、接触切换成功率等量化指标 **未能从所见摘要确认** → `> 待核实`。

6. **评测侧存在明确的结构性缺口：没有专门评测 IK/奇异性/可操作度或全身控制鲁棒性的公认基准。** 现有基准集中于策略层面的操作能力与泛化鲁棒性：LIBERO 及其变体（[93][94][95]）、ManiSkill / ManiSkill-ViTac（[101][102][104]）、robosuite（[103]）、RMMBench（[105]）、ManipBench（[106]）、ROBEL（[50]）。可操作度与雅可比质量评估目前只能依赖文献内自建指标（[82][83][87][88]）。**关注度**：高（2026 年仍有新基准持续发布）；**证据强度**：B 级（arXiv）。

7. **可复现性与「刷榜」争议有独立证据链。** 连续控制的基准可复现性问题早在 [55]（2017）即被系统讨论；sim-to-real 评测的方法论批判见 [20]（2025）；真机评测与经济型机器人基准见 [54][50][91]。

8. **工程栈格局稳定但版本/许可证细节无法在本次检索中核实。** Pinocchio、KDL/Orocos、Drake、Crocoddyl、MoveIt2 作为种子项目列入第七章；其 star 数、最近提交、许可证与 ROS2 集成细节 **本次未实时检索** → `> 待核实`。需要强调：**任何「谁在用 Pinocchio / Drake」的采用方断言，本报告均不作肯定陈述**，仅给出可核查入口。

---

## 一、关键前沿进展（近 1–2 年，2024–2026）

> 时间标注以 arXiv 编号前缀（YYMM）为准。以下条目均为 arXiv 预印本或已发表论文的预印本版本，除特别说明外**未见同行评审确认**（`> 待核实`）。

### 1.1 运动学感知的策略学习（Kinematics-aware policy learning）

| 条目 | 时间 | 贡献 | 引用 |
|---|---|---|---|
| Kinematics-Aware Diffusion Policy（全臂操作） | 2025-12 | 指出仅建模末端位姿不足，需在全臂运动学层面保持一致 3D 观测/动作空间，以支持本体避碰与臂-物交互 | [2] |
| Equivariant Descriptor Fields | 2022（v3） | SE(3) 等变能量模型，为端到端视觉操作提供几何归纳偏置 | [16] |
| KDPE（扩散策略轨迹选择） | 2025-08 | 用核密度估计在扩散策略生成的多模态轨迹中做选择 | [14] |
| HybridFlow（2-NFE 生成策略） | 2026-02 | 三阶段推理、仅 2 次函数评估，针对实时操作延迟 | [100] |
| Action Flow Matching for Continual Robot Learning | 2025-04 | 面向持续学习下的动力学模型精化与安全自适应 | [34] |

**热度证据**：`> 待核实`（未取到 citations/stars）。**权威证据**：arXiv cs.RO 预印本；[16] 为多次修订的成熟预印本。**关注度**：中—高（2025–2026 连续出现同主题投稿，说明注意力集中；依据为检索命中频次，非引用数）。**推荐度**：★★★★☆（与「策略学习中注入运动学结构」这一核心问题直接相关）。

### 1.2 接触隐式与多接触轨迹优化

- [120]（2024-06）：为 contact-implicit TO 的 SQP 方法给出**全局收敛性**结果——这是「能否放心用」的关键理论补强。
- [119] IMPACT（2026-05）：隐式 active-set 增广拉格朗日，目标是**快速**接触隐式轨迹优化。
- [121]（2023）：Staged Contact Optimization，把接触隐式与多阶段混合轨迹优化合并。
- [117]（2018）：正交配点离散的 contact-implicit TO，为该线早期系统化实现。
- [60]（2019）：四足微型机器人的接触隐式运动轨迹优化（早期真实验证场景）。
- [115]（2025-08）：Scaling Whole-body Multi-contact Manipulation with Contact Optimization，指向**多接触操作的可扩展性**。

**权威证据**：均为 arXiv 预印本，[117][60] 为该方向常被后续引用的起点（引用数 `> 待核实`）。**关注度**：高（同一问题在 2024 与 2026 分别出现理论（收敛性）与实现（速度）两条推进线，属于典型的「方法成熟化」信号）。**推荐度**：★★★★★（对接触丰富的 WBC 与操作直接可用）。

### 1.3 实时全身控制与腿足/人形

- [126]（2024-09）：腿足机器人**实时**全身控制，采用 Model-Predictive Path Integral 控制。
- [111]（2024-11）：域随机化在**全身人形扩散策略**训练中的作用。
- [112]（2025-08）：CHILD，全身关节级人形遥操作系统。
- [110]（2025-11）：人形全身羽毛球，退火 RL 课程学习动态物体交互。
- [113]（2026-02）：HMI，从「无机器人」演示学习人形全身操作。
- [114]（2026-05）：「主动空间脑 + 可泛化动作小脑」的人形全身操作。
- [3]（2025-08）：Robot Trains Robot，人形真机策略自适应与学习。

**权威证据**：arXiv cs.RO。**热度证据**：`> 待核实`。**关注度**：高（人形全身操作/控制在 2025-08 至 2026-05 之间形成密集投稿带）。**推荐度**：★★★★☆（若关注 WBC 与学习型控制的交汇）。量化指标（关节跟随误差、接触切换成功率、真机成功率、控制频率）**均未在所见摘要中确认** → `> 待核实`。

### 1.4 仿真到真机（Sim-to-Real）与评测方法论

- [20]（2025）：从基准化视角批判当前 sim-to-real 评测的不足，主张真机评测需要独立方法论。
- [57]（2025-11）：双足运动的深度 RL sim-to-real。
- [58]（2020）：光学触觉的 sim-to-real。
- [59]（2024-04）：以表示（representation）视角统一技能迁移与发现。
- [56]（2026-06）：从合成先验高效迁移 world-action 模型。
- [48]（2025-07）：用生成式音频做多模态 sim-to-real 策略学习（提示：视听之外模态的仿真差距）。

**权威证据**：arXiv；[58][20] 为方法论文献。**关注度**：高。**推荐度**：★★★★☆（做真机部署必读的「评测陷阱」清单）。

### 1.5 验证与安全（与控制器/策略安全性相关）

- [22] VNN-COMP 2025（2025-12）：神经网络验证竞赛总结——是**控制器/策略安全性形式化验证**目前最成熟的年度可对比口径。

**权威证据**：竞赛总结报告（arXiv cs.LG），同行评审状态 `> 待核实`。**关注度**：中—高。**推荐度**：★★★☆☆（与运动学控制间接相关，但对「学习型控制器的安全保证」这一争议点有直接价值）。

---

## 二、建模表示：DH vs 旋量 / POE

### 2.1 结论要点

1. **DH 参数与旋量/PoE 并非「对错之争」，而是**在奇异点、参数连续性与可微性上的工程权衡**。PoE 以螺旋轴（screw axis）为参数，避免 DH 在平行轴附近参数退化；该观点在经典教材中被系统化（种子资源：Murray-Li-Sastry 1994；Lynch & Park 2017）。**权威证据**：经典教材（种子资源，链接见第六章表）；**热度**：`> 待核实`。

2. **工程侧出现 ETS（Elementary Transform Sequence）替代 DH 的系统化表述。** [84]（2020）给出用 ETS 计算机械臂 **Jacobian 与 Hessian** 的系统方法——Hessian 对二阶优化与可操作度梯度至关重要。**权威证据**：arXiv 预印本；**关注度**：中（属工具型方法，被下游集成情况 `> 待核实`）；**推荐度**：★★★★☆（要做基于梯度的 IK / 轨迹优化时，Hessian 的解析来源是硬需求）。

3. **表示选择直接决定设计与优化能力。** [63] 讨论机器人设计中形式化与表示的作用；[64] 研究任务特定机械臂的自动设计——两者都隐含「表示需可微、可优化」的要求。**权威证据**：arXiv；**关注度**：低—中（引用数 `> 待核实`）；**推荐度**：★★★☆☆。

4. **雅可比的质量度量本身存在争议（详见第八章）。** [88]（2023）提出用扩展选择矩阵构造**量纲齐次（dimensionally homogeneous）雅可比**，以用于并联机构性能评价与优化——这是对「原始雅可比混合了长度与角度量纲，导致可操作度不可比」这一经典批评的技术回应。**权威证据**：arXiv 预印本；**关注度**：中；**推荐度**：★★★★☆（做并联机构/混合自由度优化时必看）。

### 2.2 对照表

| 维度 | DH 参数 | 旋量 / PoE / ETS | 证据 |
|---|---|---|---|
| 参数退化 | 相邻平行轴附近病态 | 螺旋轴参数化，规避该问题 | 种子教材；[84] |
| 解析导数 | 需链式展开，Hessian 繁琐 | ETS 可系统导出 Jacobian/Hessian | [84] |
| 可微/可学习 | 离散关节框架，不利端到端 | 更适合可微实现 | [2][16]（间接） |
| 工业界现状 | 广泛 | 逐步被现代框架采用 | `> 待核实`（无 Pinocchio/Drake 内部实现的实时核查） |

> `> 待核实`：**「Pinocchio / Drake 是否默认使用旋量表示」** 这一具体实现断言，本次未取得可核查的一手文档证据。

---

## 三、逆运动学：解析 / 数值 / 学习

### 3.1 解析 IK 与并联机构

- [10]（2007）：Orthoglide 的运动学与工作空间分析——并联机构工作空间/奇异性分析的经典案例。
- [8]（2007）：3-RPR 并联机械臂运动学分析。
- [5]（2024-06）：微创手术并联机器人的运动学分析——解析 IK 仍在**安全关键医疗场景**中使用。
- [7]（2012）：非理想运动链并联机构的柔顺误差补偿——说明**几何模型与实际机构存在偏差**这一现实问题。

**权威证据**：arXiv（[10][8][7] 属较早期预印本，可能对应已发表版本 `> 待核实`）；**关注度**：低（主题冷但稳定）；**推荐度**：★★★☆☆（做并联/医疗机器人时直接相关）。

### 3.2 数值 IK 与奇异点

- [9]（2024-12）：**Analytically Informed Inverse Kinematics Solution at Singularities** —— 在奇异位形处用解析信息辅助数值求解，是本主题 2024 年最直接的一手进展。**权威证据**：arXiv 预印本，同行评审 `> 待核实`；**热度**：`> 待核实`；**关注度**：中；**推荐度**：★★★★★（本调研最贴合「雅可比与奇异性」子问题的新近工作）。
- [61]（2018）：多项式优化问题解的存在性与稳定性——与「IK 作为多项式方程组求解」的数值基础相关（关联性中等，`> 待核实` 是否被 IK 文献直接引用）。

### 3.3 学习型 IK / 数据驱动 IK

本次检索**未获得**标题明确为「learning-based IK 与几何 IK 直接对比」的一手论文。可用的间接证据是：

- [2]：策略学习必须显式编码全臂运动学，说明纯末端位姿监督不够。
- [16]：SE(3) 等变性能模型，把几何对称性作为归纳偏置。
- [92]（2013）：基于 CAD 的高层机器人编程，应对不可预测环境——反映「几何模型驱动编程」与「感知驱动」的张力。

> **明确缺口**：`> 待核实` —— 「学习型 IK 是否在精度/成功率上超越阻尼最小二乘 / TRAC-IK 类数值解法」**本次检索无一手对比证据**，不作结论。该问题列入第八章 Watchlist。

### 3.4 不确定性下的运动学

- [75]（2014）：机器人机械臂在**运动学与动力学同时不确定**下的自适应控制，证明任务空间轨迹跟踪可在两者皆未知时实现（自适应方案）。**权威证据**：arXiv（对应 IEEE 期刊工作的预印本 `> 待核实`）；**关注度**：中（被后续自适应控制工作引用，引用数 `> 待核实`）；**推荐度**：★★★★☆（「运动学不确定性」在标定误差/柔性场景中仍是实际瓶颈）。

---

## 四、轨迹规划与最优控制

### 4.1 iLQR / DDP 系与约束处理

- [123]（2021）：**Inequality Constrained Trajectory Optimization with a Hybrid Multiple-shooting iLQR** —— 在 iLQR 中处理不等式约束的混合多打靶方案。这是 DDP/iLQR 系处理接触与摩擦锥约束的关键技术点。**权威证据**：arXiv；**关注度**：中；**推荐度**：★★★★☆。
- [73]（2023）：非线性约束系统动态运行的 MPC 框架综述——从跟踪到经济运行的统一视角。**权威证据**：arXiv 综述（对应期刊综述 `> 待核实`）；**关注度**：中—高；**推荐度**：★★★★☆（做 WBC-MPC 选型时的分类骨架）。

### 4.2 直接法与接触隐式

见 1.2 节。谱系整理：

| 阶段 | 工作 | 年份 | 关键点 |
|---|---|---|---|
| 离散化 | 正交配点 contact-implicit TO [117] | 2018 | 正交配点下的接触隐式建模 |
| 迁移验证 | 四足微型机器人接触隐式运动优化 [60] | 2019 | 早期硬件域验证 |
| 结构统一 | Staged Contact Optimization [121] | 2023 | 接触隐式 + 多阶段混合 |
| 理论补强 | SQP 全局收敛 [120] | 2024 | 收敛性保证 |
| 速度补强 | IMPACT（隐式 active-set AL） [119] | 2026 | 面向快速求解 |
| 规模化 | 多接触操作扩展 [115] | 2025 | 全身多接触 |

**权威证据**：全部为 arXiv 预印本；**热度证据**：`> 待核实`；**关注度**：高；**推荐度**：★★★★★（接触隐式是本主题里 2024–2026 推进最「硬」的一条线）。

### 4.3 采样型最优控制

- [126]（2024-09）：MPPI 用于腿足机器人实时全身控制——采样型方法在实时性上对基于梯度的 MPC 构成替代路径。**权威证据**：arXiv；**关注度**：中—高；**推荐度**：★★★★☆。

### 4.4 无关命中提示

[116]（分数阶最优控制必要条件）、[62]（点阵结构屈曲优化）属于最优控制/优化的其他分支，**不用于机器人结论**。`> 待核实` 其与机器人轨迹优化的实际关联。

---

## 五、全身控制与任务空间控制

### 5.1 任务空间 / 操作空间控制（OSC）

Khatib 1987 操作空间表述（种子资源）确立了「任务空间动力学解耦 + 任务优先级」的框架，至今是分层 QP 型 WBC 的概念祖先。**权威证据**：同行评审期刊论文（IJRR 前身 JRA，DOI 见第六章）；**热度**：`> 待核实`（经典工作引用数极高，但本次未取到数值）。

### 5.2 分层与优化型 WBC（2024–2026）

| 系统/工作 | 时间 | 本体 | 关键点 | 引用 |
|---|---|---|---|---|
| MPPI 实时 WBC | 2024-09 | 腿足机器人 | 采样型 MPC 做全身控制 | [126] |
| 多接触操作规模化 | 2025-08 | 全身操作 | 接触优化驱动的多接触扩展 | [115] |
| CHILD 遥操作 | 2025-08 | 人形 | 全身关节级 imitation + live demo | [112] |
| 人形羽毛球 | 2025-11 | 人形 | 退火 RL 课程，统一全身策略 | [110] |
| HMI | 2026-02 | 人形 | 无机器人演示 → 全身操作 | [113] |
| Active Spatial Brain + Action Cerebellum | 2026-05 | 人形 | 空间理解与动作生成解耦 | [114] |
| Robot Trains Robot | 2025-08 | 人形 | 真机策略自适应 | [3] |
| 域随机化 + 扩散策略 | 2024-11 | 全身人形 | 训练策略对鲁棒性的作用 | [111] |

**权威证据**：arXiv cs.RO 预印本。**热度证据**：`> 待核实`。**关注度**：高（2025-08 起人形全身方向投稿密集）。**推荐度**：★★★★☆。

> **证据强度警示**：上述工作多数以**视频/摘要级证据**呈现，接触切换鲁棒性、控制频率、真机成功率等「实时性与鲁棒性达到什么水平」的问题，**本次无法给出可核查数字** → `> 待核实`。按 evidence-grading 纪律，不得把演示视频当实验证据。

### 5.3 学习型 WBC 与模型型 WBC 的关系

- 学习型侧：扩散策略 [111][2][14]、流匹配 [34][100]、真机自适应 [3]。
- 优化型侧：接触隐式 [117][119][120][121]、iLQR [123]、MPC 综述 [73]、MPPI [126]。
- **共识**：混合架构（学习前端 + 优化/QP 后端）是当前事实上的工程折中；**分歧**：是否需要保留显式动力学模型——无一手对比证据 → `> 待核实`。

---

## 六、经典教材与奠基工作

> 表中「热度」列凡未取到引用数/下载量者标 `> 待核实`。「链接」列中带 `doi.org`/`arxiv.org` 者与 [n] 对应；教材与 Khatib 条目为**主题 YAML 种子资源**（未实时检索）。

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| A Mathematical Introduction to Robotic Manipulation | 1994 | Murray, Li, Sastry（Caltech/Berkeley） | > 待核实 | 经典教材，旋量/PoE 的标准表述 | 高（领域标准教材，依据：长期作为课程主教材） | ★★★★★ | https://www.cds.caltech.edu/~murray/mlswiki/ | 旋量理论、指数积、雅可比与操作空间的统一几何框架 |
| Modern Robotics: Mechanics, Planning, and Control | 2017 | Lynch & Park（Northwestern） | > 待核实 | 教材 + 官方 MOOC/代码 | 高 | ★★★★★ | http://hades.mech.northwestern.edu/index.php/Modern_Robotics | 现代运动学/规划/控制；PoE 与 DH 并列讲解，配套库 |
| Task Space Control / Operational Space Formulation | 1987 | Oussama Khatib（Stanford） | > 待核实 | 同行评审（IEEE J. Robotics and Automation） | 高（OSC 概念源头） | ★★★★★ | https://doi.org/10.1109/JRA.1987.1087109 | 操作空间动力学与任务优先级框架的奠基 |
| Crocoddyl: Multi-Contact Optimal Control Framework | 2020 | LAAS-CNRS | > 待核实 | 开源框架论文（arXiv 1909.04947） | 高（接触最优控制主流开源实现之一） | ★★★★★ | https://arxiv.org/abs/1909.04947 | 多接触最优控制（DDP 系）框架 |
| A Systematic Approach to Computing the Manipulator Jacobian and Hessian using ETS | 2020 | arXiv | > 待核实 | arXiv 预印本 | 中 | ★★★★☆ | http://arxiv.org/abs/2010.08696v1 [84] | 用元素变换序列系统推导 Jacobian/Hessian |
| Contact-Implicit Trajectory Optimization using Orthogonal Collocation | 2018 | arXiv | > 待核实 | arXiv 预印本 | 中—高（接触隐式线起点之一） | ★★★★★ | http://arxiv.org/abs/1809.06436v3 [117] | 正交配点下的接触隐式建模 |
| Contact-Implicit Optimization of Locomotion Trajectories for a Quadrupedal Microrobot | 2019 | arXiv | > 待核实 | arXiv 预印本 | 中 | ★★★★☆ | http://arxiv.org/abs/1901.09065v1 [60] | 接触隐式在微型四足上的落地验证 |
| Inequality Constrained Trajectory Optimization with Hybrid Multiple-shooting iLQR | 2021 | arXiv | > 待核实 | arXiv 预印本 | 中 | ★★★★☆ | http://arxiv.org/abs/2109.07131v2 [123] | iLQR 处理不等式约束的工程方案 |
| Adaptive Control of Robot Manipulators With Uncertain Kinematics and Dynamics | 2014 | arXiv | > 待核实 | arXiv 预印本（对应期刊工作） | 中 | ★★★★☆ | http://arxiv.org/abs/1403.5204v3 [75] | 运动学+动力学双不确定下的自适应控制 |
| Equivariant Descriptor Fields (SE(3)-Equivariant EBM) | 2022 | arXiv | > 待核实 | arXiv 预印本 | 中—高 | ★★★★☆ | http://arxiv.org/abs/2206.08321v3 [16] | 几何等变性作为端到端操作的归纳偏置 |
| Geometry-aware Manipulability Learning, Tracking and Transfer | 2018 | arXiv | > 待核实 | arXiv 预印本 | 中 | ★★★★☆ | http://arxiv.org/abs/1811.11050v5 [82] | 可操作度的学习、跟踪与跨体迁移 |
| Analysis and Transfer of Human Movement Manipulability in Industry-like Activities | 2020 | arXiv | > 待核实 | arXiv 预印本 | 中 | ★★★☆☆ | http://arxiv.org/abs/2008.01402v2 [83] | 人体可操作度分析并迁移到工业场景 |
| Dimensionally Homogeneous Jacobian using Extended Selection Matrix | 2023 | arXiv | > 待核实 | arXiv 预印本 | 中 | ★★★★☆ | http://arxiv.org/abs/2310.17863v1 [88] | 并联机构性能评价中的量纲齐次雅可比 |
| An Overview of MPC Frameworks for Dynamic Operation | 2023 | arXiv | > 待核实 | arXiv 综述（对应期刊综述） | 中—高 | ★★★★☆ | http://arxiv.org/abs/2307.03004v2 [73] | 非线性约束系统 MPC 框架分类 |
| Analytically Informed Inverse Kinematics Solution at Singularities | 2024 | arXiv | > 待核实 | arXiv 预印本 | 中 | ★★★★★ | http://arxiv.org/abs/2412.20409v1 [9] | 奇异位形下的解析知情 IK |
| Robot Design: Formalisms, Representations, and the Role of the Designer | 2018 | arXiv | > 待核实 | arXiv 预印本 | 低 | ★★★☆☆ | http://arxiv.org/abs/1806.05157v1 [63] | 设计表示与设计者角色的形式化讨论 |
| Automatic Design of Task-specific Robotic Arms | 2018 | arXiv | > 待核实 | arXiv 预印本 | 低—中 | ★★★☆☆ | http://arxiv.org/abs/1806.07419v1 [64] | 任务特定机械臂自动设计（运动学可优化） |

> `> 待核实`：上表所有「热度」数值（引用数、下载量）本次均未从权威数据库取到；「关注度」评级依据为教材地位与该方向在本期检索中的命中频次，不含引用数值支撑。

---

## 七、开源库与工具链对比

> **重要提示**：本章 5 个种子项目的 star 数、最近提交时间、许可证（License）与 ROS2 集成细节 **本次均未实时检索**。下表「热度」全部为 `> 待核实`；任何「被某主流人形项目采用」的断言本报告**不予给出**。

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| stack-of-tasks/pinocchio | > 待核实 | LAAS-CNRS / stack-of-tasks | > 待核实 | 官方 GitHub 仓库（B 级） | 高（依据：机器人动力学/运动学社区长期讨论焦点，但 star 数 `> 待核实`） | ★★★★★ | https://github.com/stack-of-tasks/pinocchio | 刚体运动学/动力学，含解析导数；WBC 与最优控制的常见后端 |
| orocos/orocos_kinematics_dynamics（KDL） | > 待核实 | Orocos 社区 | > 待核实 | 官方 GitHub 仓库（B 级） | 中—高 | ★★★★☆ | https://github.com/orocos/orocos_kinematics_dynamics | KDL：FK/IK/Jacobian；ROS 生态历史依赖 |
| RobotLocomotion/drake | > 待核实 | Toyota Research Institute / MIT | > 待核实 | 官方 GitHub 仓库（B 级） | 高 | ★★★★★ | https://github.com/RobotLocomotion/drake | 优化与控制的 C++ 工具箱，含数学规划与系统框架 |
| loco-3d/crocoddyl | > 待核实 | LAAS-CNRS | > 待核实 | 官方 GitHub 仓库（B 级）；方法见 [种子] arXiv 1909.04947 | 中—高 | ★★★★★ | https://github.com/loco-3d/crocoddyl | 多接触最优控制（DDP 系），与 [117] 线互补 |
| moveit/moveit2 | > 待核实 | MoveIt 社区 / ROS 2 | > 待核实 | 官方 GitHub 仓库（B 级） | 高（ROS2 生态运动规划事实标准，依据：ROS2 集成惯例，具体采用方数据 `> 待核实`） | ★★★★★ | https://github.com/moveit/moveit2 | ROS2 运动规划框架（IK 插件、碰撞、规划） |
| MuJoCo / MJX | > 待核实 | > 待核实 | > 待核实 | > 待核实 | > 待核实 | > 待核实 | > 待核实 | 问题 q4 提及，但**本次未提供任何可核查引用**；不作任何现状断言 |
| PyRoki / robot-descriptions | > 待核实 | > 待核实 | > 待核实 | > 待核实 | > 待核实 | > 待核实 | > 待核实 | 同上，**无可用一手证据**，仅列为待补检索项 |

### 7.1 选型建议（基于可核查证据的保守判断）

1. **需要解析导数与最优控制闭环** → 优先评估 Pinocchio + Crocoddyl 组合（前者提供运动学/动力学导数，后者提供多接触 DDP）[种子资源；[117] 谱系]。
2. **需要数学规划/形式化保证** → Drake（含优化与验证工具链）[种子资源]，并与神经验证口径（[22]）配合考虑。
3. **ROS2 集成与工程化落地** → MoveIt2 [种子资源]；注意 KDL 在 ROS 生态中的历史地位 [种子资源]。
4. **DH vs PoE 的实现选择** → 若需 Hessian/二阶优化，参考 ETS 的系统化导出 [84]。

> `> 待核实`：上述组合的**性能对比数据**（求解时间、内存、稳定性）本次未取得，禁止据此宣称某库「最快/最优」。

---

## 八、开放问题与关注清单

### 8.1 争议一：学习型 IK 是否取代几何/数值 IK？

- **可用证据**：[2] 表明策略学习需显式运动学约束；[16] 表明几何等变可提升样本效率；[9] 表明奇异点仍需解析洞察。
- **结论**：**尚无一手对比证据支持「取代」** → `> 待核实`。当前可陈述的判断仅为：**二者在 2025–2026 呈现互补态势**（几何/解析用于约束与奇异点处理，学习用于高维/感知耦合场景）。
- **关注度**：高。**推荐度**：★★★★★（最值得追踪的开放问题）。

### 8.2 争议二：接触隐式的可迁移性与安全性

- [120] 提供全局收敛性，[119] 提速，[115] 规模化——三点分别对应「可靠性/速度/规模」。
- **缺口**：**跨本体迁移**与**安全保证**（接触模型失配、摩擦不确定性）缺乏统一评测 → `> 待核实`。神经验证工具（[22]）尚未见与接触隐式 TO 的直接结合证据。

### 8.3 争议三：可操作度指标的有效性

- 支持推进：[82][83]（可操作度的学习/迁移/人因分析）；[87]（任务空间一致性中的分离性与可操作度）。
- 批评回应：[88]（量纲不齐导致原始雅可比不可比 → 构造量纲齐次雅可比）。
- **结论**：可操作度作为**优化目标**有效（有梯度可用），作为**绝对性能指标**存在量纲与尺度争议 → `> 待核实`（缺少跨机构共识声明）。
- **关注度**：中。**推荐度**：★★★★☆。

### 8.4 争议四：仿真到真机差距与基准刷榜

- 方法论批判：[20]（sim-to-real 评测落后于通用策略评估需求）。
- 复现性证据：[55]（连续控制深度 RL 任务的可复现性问题，2017 年即已系统化）；[54]（真机 RL 算法基准）；[91]（用真实世界数据集评测仿真操作）；[50]（低成本机器人基准 ROBEL）。
- **结论**：**榜单 SOTA 与真机能力不等价**是学界共识级判断，有独立证据链支撑（[20][55][54][91][50]）。**关注度**：高。**推荐度**：★★★★★。

### 8.5 争议五：可微分物理的梯度可信度

- **本次检索未获得**直接讨论可微分物理梯度可信度的一手论文 → `> 待核实`。间接相关者仅有 [16]（等变能量模型）与 [2]（运动学一致性），不足以支撑结论。
- 列入 Watchlist 待补检。

### 8.6 基准缺口清单

| 缺口 | 现状 | 证据 |
|---|---|---|
| 专门评测 **IK 精度/奇异性穿越** 的基准 | **未发现** | 本期检索无对应条目 → `> 待核实` |
| 专门评测 **可操作度** 的标准化基准 | 未发现；仅文献内自建指标 | [82][83][88][87] |
| 专门评测 **全身控制鲁棒性/接触切换** 的基准 | 未发现统一口径；人形工作各自设定任务 | [110][112][113][114][126] |
| 操作策略层基准（已有，较成熟） | LIBERO 系、ManiSkill 系、robosuite、RMMBench、ManipBench、ROBEL | [93][94][95][101][102][103][104][105][106][50] |
| 视觉鲁棒性 / 指令改写鲁棒性 | 已有专门基准 | [94]（LIBERO-VPro，2026）、[95]（LIBERO-Para，2026） |
| 策略/控制器安全性形式化验证 | 有年度竞赛口径 | [22]（VNN-COMP 2025） |

### 8.7 数据集与基准对照表

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| LIBERO | 2023 | arXiv | > 待核实 | arXiv 预印本 | 高（VLA/终身学习常用基准） | ★★★★★ | http://arxiv.org/abs/2306.03310v2 [93] | 终身机器人学习的知识迁移基准 |
| LIBERO-VPro | 2026 | arXiv | > 待核实 | arXiv 预印本 | 中—高（新） | ★★★★☆ | http://arxiv.org/abs/2609.24350v1 [94] | 闭环视觉鲁棒性评测 |
| LIBERO-Para | 2026 | arXiv | > 待核实 | arXiv 预印本 | 中—高（新） | ★★★★☆ | http://arxiv.org/abs/2603.28301v3 [95] | VLA 指令改写鲁棒性的诊断基准与指标 |
| ManiSkill | 2021 | arXiv | > 待核实 | arXiv 预印本 | 高 | ★★★★★ | http://arxiv.org/abs/2107.14483v5 [101] | 通用操作技能基准 + 大规模演示 |
| ManiSkill-ViTac 2025 Challenge | 2024-11 | arXiv | > 待核实 | 竞赛 Challenge 报告 | 中 | ★★★★☆ | http://arxiv.org/abs/2411.12503v1 [102] | 视觉 + 触觉操作技能学习挑战 |
| robosuite | 2020 | arXiv | > 待核实 | arXiv 预印本 | 高 | ★★★★★ | http://arxiv.org/abs/2009.12293v3 [103] | 模块化仿真框架与基准 |
| RMMBench | 2026 | arXiv | > 待核实 | arXiv 预印本 | 中（新） | ★★★★☆ | http://arxiv.org/abs/2610.05414v1 [105] | 移动操作综合基准 |
| ManipBench | 2025 | arXiv | > 待核实 | arXiv 预印本 | 中—高 | ★★★★☆ | http://arxiv.org/abs/2505.09698v2 [106] | 评测 VLM 的低层操作推理能力 |
| ROBEL | 2019 | arXiv | > 待核实 | arXiv 预印本 | 中 | ★★★★☆ | http://arxiv.org/abs/1909.11639v3 [50] | 低成本机器人学习基准 |
| 真机数据集评测（sim 基准 vs 真机数据） | 2019 | arXiv | > 待核实 | arXiv 预印本 | 中 | ★★★★☆ | http://arxiv.org/abs/1911.01557v2 [91] | 用真实世界数据集检验仿真基准 |
| RoboMimic | > 待核实 | 种子资源（Stanford 等） | > 待核实 | 官方项目主页 | > 待核实 | ★★★★☆ | https://robomimic.github.io/ | 模仿学习演示数据与基准（**种子资源，未实时检索**） |
| SoftGym | 2020 | arXiv | > 待核实 | arXiv 预印本 | 中 | ★★★☆☆ | http://arxiv.org/abs/2011.07215v2 [53] | 可变形物体操作的深度 RL 基准 |
| DROID / Open X-Embodiment / RoboArena / SimplerEnv | > 待核实 | — | > 待核实 | > 待核实 | > 待核实 | > 待核实 | > 待核实 | 问题 q5 提及，但**本次未提供任何可核查引用**，不作现状断言 |

### 8.8 Watchlist（值得持续关注）

1. **奇异点感知的 IK 与可微运动学**：[9]（2024）→ 观察后续是否有真机/多本体验证与开源实现。
2. **接触隐式的理论—实现双线**：[120]（收敛性）与 [119]（速度）是否会合并为统一求解器。
3. **运动学约束注入生成式策略**：[2]（全臂感知）→ 是否成为 VLA/扩散策略的默认做法（相关规模化工作 [33]）。
4. **采样型 WBC vs 梯度型 WBC**：[126] vs [123][119]——实时性/鲁棒性权衡的一手对比。
5. **人形全身操作的数据来源之争**：遥操作 [112] vs 无机器人演示 [113] vs 真机自学习 [3] vs 仿真+域随机化 [111]。
6. **评测缺口填补**：IK/奇异性/可操作度/接触切换基准是否在 2026–2027 出现。
7. **待补检索项**：MuJoCo/MJX、PyRoki、robot-descriptions、DROID、Open X-Embodiment、RoboArena、SimplerEnv 的一手来源（官方仓库/论文主页），以及**可微分物理梯度可信度**的直接文献。

---

## 二、建模表示：DH vs 旋量/POE

> 本章说明：本次检索给出的可引用来源 [n] 中，直接讨论「DH 与 PoE 之争」的一手文献较少，多数条目为具体方法论文（ETS、等变模型、并行机构运动学）。因此凡涉及经典教材与非 [n] 来源的判断，统一以 `> 待核实` 标注；凡可归因到具体 [n] 的技术论断，均给出编号。

### 2.1 争点的准确表述

建模表示的差异不在「能不能算出正运动学」，而在三件事：

1. **参数化是否平滑、是否利于优化**：以关节轴（screw axis）为参数的指数积（Product of Exponentials, PoE）表述把运动学写成矩阵指数连乘，参数与几何量（轴方向、轴上一点）直接对应，便于求导与代入数值优化；
2. **是否依赖逐连杆建系约定**：DH 参数以「相邻连杆坐标系」的四个参数为单位，表示紧凑，但需要严格遵守建系约定，不同约定之间不可混用；
3. **是否支持统一的雅可比/海森推导**：PoE 体系下雅可比可直接由螺旋轴与关节构型写出，进而系统化地推到二阶导。

需要强调的是：**DH 与 PoE 在现代工程栈中并非互斥，而是并存**。工业控制器与部分规划库仍沿用 DH，而面向优化/可微分/全身控制的研究栈更倾向 PoE 与轴角表示。

### 2.2 建模表示对照表

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| DH 参数（Denavit–Hartenberg） | 1955 | Denavit & Hartenberg | > 待核实 | > 待核实（本次检索未获得该原始文献的 [n] 来源） | > 待核实 | ★★★★☆（工业界事实标准，但本章无可核查引用，建议补检原始 ASME 文献） | > 待核实 | 4 参数/连杆的最小表示，机械臂建模传统标准 |
| 旋量理论 / 指数积（PoE） | 1994 | Murray, Li, Sastry | > 待核实 | 经典教材，官方 wiki 可访问 | 中–高（作为教学与理论底座长期被引用） | ★★★★★（理解 PoE 与旋量体系的首选入口） | https://www.cds.caltech.edu/~murray/mlswiki/ | 以旋量描述关节，免逐连杆建系，几何直观 |
| Modern Robotics（PoE 体系化教材 + 配套代码） | 2017 | Lynch & Park | > 待核实 | 教材 + 官方 wiki/公开课程 | 高（广泛作为现代运动学教学标准） | ★★★★★（PoE 体系下的现代运动学/规划与控制一体教材） | http://hades.mech.northwestern.edu/index.php/Modern_Robotics | PoE 表述、雅可比、规划与控制统一处理 |
| ETS（Elementary Transform Sequence）雅可比/海森推导 | 2020 | 见 [84] | > 待核实 | arXiv 预印本（cs.RO），未见同行评审信息 [84] | 低–中（面向运动学数值推导的工具性工作） | ★★★★☆（需要系统化求雅可比/海森时直接有用） | http://arxiv.org/abs/2010.08696v1 | 提出用基本变换序列系统计算机械臂雅可比与海森矩阵 [84] |
| SE(3) 等变表示（Equivariant Descriptor Fields） | 2022 | 见 [16] | > 待核实 | arXiv 预印本（v3，未见同行评审信息）[16] | 中（等变表示是操作学习的热点方向） | ★★★★☆（理解 SE(3) 等变如何进入端到端视觉操作） | http://arxiv.org/abs/2206.08321v3 | 以 SE(3) 等变能量基模型做端到端视觉操作学习 [16] |
| 全臂运动学感知观测/动作空间 | 2025 | 见 [2] | > 待核实 | arXiv 预印本（cs.RO）[2] | 中（面向全身/全臂操作的新近工作） | ★★★★☆（把运动学结构显式写进策略表示的代表） | http://arxiv.org/abs/2512.17568v1 | 指出仅考虑末端位姿不足，主张一致的 3D 观测与动作空间并显式建模全臂运动学 [2] |
| 机器人形式化表示与设计 | 2018 | 见 [63] | > 待核实 | arXiv 预印本 [63] | 低（偏设计方法论） | ★★★☆（关注「表示如何影响设计空间」时值得一读） | http://arxiv.org/abs/1806.05157v1 | 讨论机器人设计中的形式化与表示选择 [63] |
| 任务特定机械臂自动设计 | 2018 | 见 [64] | > 待核实 | arXiv 预印本 [64] | 低 | ★★★☆（表示与设计耦合的早期探索） | http://arxiv.org/abs/1806.07419v1 | 面向任务自动生成机械臂构型 [64] |

### 2.3 逐条论断与四轴证据

**论断 1：PoE/ETS 体系可直接支撑雅可比与海森的系统化推导，这使其在需要高阶导数的优化/控制中具备工程优势。**
- 证据：已有工作提出用基本变换序列（ETS）系统计算机械臂雅可比与海森矩阵 [84]。
- 热度证据：> 待核实（抽取结果未提供 citations/stars 字段）。
- 权威证据：arXiv 预印本（cs.RO 分类），本次检索未见同行评审信息 [84]。
- 关注度：低–中，依据为该来源为工具性方法论预印本，未观察到榜单或社区热度信号 [84]。
- 推荐度：★★★★☆——需要写二阶导或做可微分运动学时，这类系统化推导路径具有直接工程价值 [84]。

**论断 2：仅以末端位姿刻画操作策略不足以覆盖本体碰撞与本体-物体交互，显式建模全臂运动学正在进入策略学习表示层。**
- 证据：Kinematics-Aware Diffusion Policy 明确指出全身/全臂运动学感知对这类场景关键，而只考虑末端位姿的做法不够 [2]。
- 热度证据：> 待核实。
- 权威证据：arXiv 预印本（cs.RO），2025 年，未见同行评审信息 [2]。
- 关注度：中，依据为其发表于 2025 年，属于扩散策略与运动学交叉的近期方向 [2]。
- 推荐度：★★★★☆——是「运动学表示进入策略学习」的清晰样本 [2]。

**论断 3：SE(3) 等变表示已作为一类独立的建模范式出现在端到端视觉操作学习中。**
- 证据：Equivariant Descriptor Fields 将 SE(3) 等变能量基模型用于端到端视觉操作学习 [16]。
- 热度证据：> 待核实。
- 权威证据：arXiv 预印本（已更新至 v3），未见同行评审信息 [16]。
- 关注度：中，依据为等变/几何深度学习在操作学习中是持续被讨论的方向 [16]。
- 推荐度：★★★★☆——若关心「几何先验写进网络表示」的路线，这是入口文献 [16]。

**论断 4：雅可比本身的量纲与条件数指标在并行机构性能评价中存在专门方法学讨论。**
- 证据：有工作提出用扩展选择矩阵构造量纲齐次（dimensionally homogeneous）雅可比，用于并行机构的性能评价与优化 [88]。相关工作还包括可操作度的几何感知学习、跟踪与迁移 [82]。
- 热度证据：> 待核实。
- 权威证据：arXiv 预印本 [88][82]，未见同行评审信息。
- 关注度：低–中，依据为属于指标方法学而非热点任务论文 [88][82]。
- 推荐度：★★★★☆——做雅可比口径对比或可操作度度量时，需先处理量纲不一致问题 [88][82]。

**论断 5：并行机构的运动学与奇异性/工作空间分析形成了相对独立的一支文献，其建模表示与串联臂不同（闭环约束）。**
- 证据：包括微创手术并行机器人运动学分析 [5]、3-RPR 并行机械臂运动学分析 [8]、Orthoglide 的运动学与工作空间分析 [10]，以及由非完美运动链构成的并行机构柔顺误差补偿 [7]。
- 热度证据：> 待核实。
- 权威证据：上述均为 arXiv 预印本（部分为较早版本），未见同行评审信息 [5][7][8][10]。
- 关注度：低（在 2024–2026 前沿讨论中占比小）[5][7][8][10]。
- 推荐度：★★★☆——若涉及闭环机构或标定误差补偿，这几篇提供建模视角 [5][7][8][10]。

**论断 6：运动学模型不确定性本身是被显式处理的控制问题，而非可以忽略的建模细节。**
- 证据：有工作针对「运动学与动力学均不确定」的机械臂提出自适应控制方案，以实现任务空间轨迹跟踪 [75]。
- 热度证据：> 待核实。
- 权威证据：arXiv 预印本（2014 年，v3 更新），未见同行评审信息 [75]。
- 关注度：中，依据为该问题在标定误差/柔性关节场景中持续被引用 [75]。
- 推荐度：★★★★☆——连接「建模表示」与「鲁棒控制」的关键一环 [75]。

**论断 7：在流形上直接设计控制器（而非在欧氏空间近似）是一条独立的技术路线。**
- 证据：见「On Controller Design for Systems on Manifolds in Euclidean Space」[77]。
- 热度证据：> 待核实。
- 权威证据：arXiv 预印本 [77]，未见同行评审信息。
- 关注度：低–中 [77]。
- 推荐度：★★★☆——与 SE(3)/旋量表示直接相关，但需自行判断适用边界 [77]。

**论断 8：经典教材（PoE 与 DH 两条体系）的引用数与影响力指标本次未能取到可核查数字。**
- 说明：本章所列 Murray/Li/Sastry（1994）与 Lynch & Park（2017）的链接来自本次调研任务给定的领域种子资源清单，其引用数、下载量、课程采用数等热度信号本次未实时检索。
- 热度证据：> 待核实。
- 权威证据：官方 wiki / 教材页面可访问（链接见 2.2 表）。
- 关注度：> 待核实（无检索信号支撑高/中/低的量化判断）。
- 推荐度：★★★★★（作为体系化学习入口的编辑判断，非基于热度数字）。

### 2.4 选型建议（工程视角）

| 场景 | 建议表示 | 依据 |
|---|---|---|
| 教学、概念推导、几何直观 | 旋量/PoE | 轴角参数与运动学结构直接对应；体系化教材入口见 2.2 表 |
| 需要雅可比/海森并可微分 | ETS 或 PoE 参数化 | 已有系统化推导路径 [84] |
| 策略学习中的本体感知建模 | 全臂运动学感知的观测/动作空间 | 末端位姿不足的实证动机 [2] |
| 需要几何先验的视觉操作 | SE(3) 等变表示 | 等变能量基模型已用于端到端操作 [16] |
| 工业控制器/既有产线 | 多数仍为 DH 约定 | > 待核实（本章无 [n] 来源支撑该比例的定量说法） |
| 闭环/并行机构 | 需显式处理闭环约束 | 并行机构运动学与误差补偿文献 [5][7][8][10] |
| 雅可比指标对比 | 先处理量纲齐次性 | 扩展选择矩阵方法 [88]；可操作度学习 [82] |

与 ROS2 工程栈的衔接（Pinocchio / KDL / Drake / MoveIt2 等）以及各库对 DH、PoE、URDF 的实际支持程度，统一在**第七章「开源库与工具链对比」**展开，本章不重复。

### 2.5 本章小结与缺口

- **共识侧**：PoE/旋量提供了一套与几何量对齐、便于求导的表示，已被用于雅可比/海森的系统化推导 [84]；几何先验（SE(3) 等变）与结构先验（全臂运动学）正在向学习型策略渗透 [16][2]。
- **分歧侧**：DH 与 PoE 的「优劣」在实践中更多是工具链兼容性问题，而非理论正确性问题；本章未能找到以 [n] 形式可引用的、对两者做定量对比评测的文献。
- **缺口（需补检）**：DH 原始文献、两体系在数值条件数/奇异邻域行为上的定量对比实验、以及主流库（Pinocchio/KDL/Drake）对两种表示的原生支持差异，本章均标注 `> 待核实`，建议在第七章与后续补检中补齐。

## 参考来源

以下编号与本次提供的证据列表一一对应；未列出的条目（如高能物理、天体物理、竞赛报告中的非机器人项）已在正文中声明剔除，不作引用。

[1] One-Shot Reinforcement Learning for Robot Navigation with Interactive Replay — http://arxiv.org/abs/1711.10137v2
[2] Kinematics-Aware Diffusion Policy with Consistent 3D Observation and Action Space for Whole-Arm Robotic Manipulation — http://arxiv.org/abs/2512.17568v1
[3] Robot Trains Robot: Automatic Real-World Policy Adaptation and Learning for Humanoids — http://arxiv.org/abs/2508.12252v2
[5] Kinematic analysis of a parallel robot for minimally invasive surgery — http://arxiv.org/abs/2406.02047v1
[7] Compensation of compliance errors in parallel manipulators composed of non-perfect kinematic chains — http://arxiv.org/abs/1204.1757v1
[8] Kinematic analysis of the 3-RPR parallel manipulator — http://arxiv.org/abs/0708.3920v1
[9] Analytically Informed Inverse Kinematics Solution at Singularities — http://arxiv.org/abs/2412.20409v1
[10] The Orthoglide: Kinematics and Workspace Analysis — http://arxiv.org/abs/0705.1394v1
[11] On-Policy Robot Imitation Learning from a Converging Supervisor — http://arxiv.org/abs/1907.03423v7
[12] Multi-objective Model-based Policy Search for Data-efficient Learning with Sparse Rewards — http://arxiv.org/abs/1806.09351v3
[13] SPIRE: Synergistic Planning, Imitation, and Reinforcement Learning for Long-Horizon Manipulation — http://arxiv.org/abs/2410.18065v1
[14] KDPE: A Kernel Density Estimation Strategy for Diffusion Policy Trajectory Selection — http://arxiv.org/abs/2508.10511v2
[15] Untangling Dense Knots by Learning Task-Relevant Keypoints — http://arxiv.org/abs/2011.04999v1
[16] Equivariant Descriptor Fields: SE(3)-Equivariant Energy-Based Models for End-to-End Visual Robotic Manipulation Learning — http://arxiv.org/abs/2206.08321v3
[19] Grasp and Motion Planning for Dexterous Manipulation for the Real Robot Challenge — http://arxiv.org/abs/2101.02842v1
[20] Robot Policy Evaluation for Sim-to-Real Transfer: A Benchmarking Perspective — http://arxiv.org/abs/2508.11117v1
[22] The 6th International Verification of Neural Networks Competition (VNN-COMP 2025): Summary and Results — http://arxiv.org/abs/2512.19007v1
[33] Xiaomi-Robotics-1: Scaling Vision-Language-Action Models with over 100K Hours of Real-World Trajectories — http://arxiv.org/abs/2607.15330v2
[34] Action Flow Matching for Continual Robot Learning — http://arxiv.org/abs/2504.18471v2
[48] The Sound of Simulation: Learning Multimodal Sim-to-Real Robot Policies with Generative Audio — http://arxiv.org/abs/2507.02864v2
[49] LLM-based ambiguity detection in natural language instructions for collaborative surgical robots — http://arxiv.org/abs/2507.11525v1
[50] ROBEL: Robotics Benchmarks for Learning with Low-Cost Robots — http://arxiv.org/abs/1909.11639v3
[51] Learning Robot Manipulation from Cross-Morphology Demonstration — http://arxiv.org/abs/2304.03833v2
[53] SoftGym: Benchmarking Deep Reinforcement Learning for Deformable Object Manipulation — http://arxiv.org/abs/2011.07215v2
[54] Benchmarking Reinforcement Learning Algorithms on Real-World Robots — http://arxiv.org/abs/1809.07731v1
[55] Reproducibility of Benchmarked Deep Reinforcement Learning Tasks for Continuous Control — http://arxiv.org/abs/1708.04133v1
[56] Efficient Sim-to-Real Transfer of World-Action Models from Synthetic Priors — http://arxiv.org/abs/2606.31101v1
[57] Sim-to-Real Transfer in Deep Reinforcement Learning for Bipedal Locomotion — http://arxiv.org/abs/2511.06465v1
[58] Sim-to-Real Transfer for Optical Tactile Sensing — http://arxiv.org/abs/2004.00136v1
[59] Skill Transfer and Discovery for Sim-to-Real Learning: A Representation-Based Viewpoint — http://arxiv.org/abs/2404.05051v1
[60] Contact-Implicit Optimization of Locomotion Trajectories for a Quadrupedal Microrobot — http://arxiv.org/abs/1901.09065v1
[61] On the solution existence and stability of polynomial optimization problems — http://arxiv.org/abs/1808.06100v6
[63] Robot Design: Formalisms, Representations,

---

*Generated by research-bot · topic=`kinematics` · depth=`standard` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading · model=`deepseek-v4-flash` · sources=126 · duration=343s · 2026-10-06T22:51:48+00:00*
