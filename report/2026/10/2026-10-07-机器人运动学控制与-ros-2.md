# 机器人运动学、控制与 ROS 2：2024–2026 增量调研报告

**日期**：2026-10-07（UTC）
**领域**：Robotics Kinematics / Control / ROS 2（含 humanoid whole-body control、loco-manipulation、sim-to-real RL、VLA–低层控制器接口）
**检索源数量**：34 条候选来源（编号 [1]–[34]）
**证据基线说明**：本报告严格只引用 [1]–[34]。候选池中存在大量**关键词漂移误召回**（相对论弹性力学 [14]、交换代数 [15][17][20][21]、空间数据算法 [16]、网络传染病控制 [22]、天体物理 PINOCCHIO [34]、以及 2025 年各类 CV/NLP/Audio 挑战赛 [24]–[31]、[33]），这些条目**不可**作为机器人学证据；凡本主题证据缺失处一律标注 `> 待核实`，**不编造引用数、star 数与榜单排名**。

---

## 1. 进展与热点（Progress & Hotspots）

**一句话增量判断**：相对 2023 年以前「MPC + iLQR + 模块化规划-控制栈」的基线，2024–2026 的真实增量集中在**用 RL/扩散策略统一全身（whole-body）控制与 loco-manipulation**、**视觉–本体感知的多模态策略**、以及**VLA/基础模型作为高层、学习型控制器作为底层的分层接口**；但本批证据中**几乎全部为 arXiv 预印本（B 级）**，缺少独立第三方复现与统一榜单，SOTA 归属 `> 待核实`。

### 1.1 最新进展（近 1–2 年，2024–2026）

| 名称 | 时间 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Humanoid Whole-Body Badminton via an Annealed Reinforcement Learning Curriculum | 2025 | 未给出（arXiv cs.RO）[1] | > 待核实（候选块无 citations）[1] | arXiv 预印本，cs.RO，未见同行评审 venue [1] | 中（动态全身交互为当前热点方向）[1] | ★★★★☆ 代表「RL 课程学习 → 快速运动物体全身交互」新范式 [1] | http://arxiv.org/abs/2511.11218v4 | 用退火式 RL 课程训练统一全身策略，面向**运动物体**（羽毛球）交互，超出静态场景操作 [1] |
| Humanoid Whole-Body Manipulation via Active Spatial Brain and Generalizable Action Cerebellum | 2026 | 未给出（arXiv cs.RO）[2] | > 待核实 [2] | arXiv 预印本，cs.RO [2] | 中（"空间大脑 + 动作小脑"分层与 VLA 叙事同频）[2] | ★★★★☆ 直接把高层空间理解与低层动作生成**解耦为两个模块**，是本主题「接口方式」的关键样本 [2] | http://arxiv.org/abs/2605.21133v2 | 明确针对 3D 复杂空间关系理解 + 动作泛化两大难点，属分层（brain/cerebellum）架构 [2] |
| CHILD: Controller for Humanoid Imitation and Live Demonstration | 2025 | 未给出（arXiv cs.RO）[3] | > 待核实 [3] | arXiv 预印本，cs.RO [3] | 中（全身关节级遥操作为人形数据采集刚需）[3] | ★★★★☆ 指出既有遥操作「很少支持全身关节级」，填补真机数据采集缺口 [3] | http://arxiv.org/abs/2508.00162v2 | 全身人形遥操作系统，面向模仿学习/实时示教的控制器 [3] |
| The Role of Domain Randomization in Training Diffusion Policies for Whole-Body Humanoid Control | 2024 | 未给出（arXiv cs.RO）[4] | > 待核实 [4] | arXiv 预印本，cs.RO [4] | 中（域随机化 × 扩散策略的组合是 sim-to-real 核心疑点）[4] | ★★★★☆ 直接检验"域随机化对扩散策略是否必要/有效"，属方法归因类工作 [4] | http://arxiv.org/abs/2411.01349v1 | 主题为 domain randomization 在 diffusion policy 全身人形控制中的作用（据标题）[4] |
| ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation | 2026 | 未给出（arXiv cs.RO）[6] | > 待核实 [6] | arXiv 预印本，cs.RO [6] | 中（"统一多模态控制"直指模块化栈被替代）[6] | ★★★★☆ 与本题「相对 2023 模块化栈新增什么」最直接相关 [6] | http://arxiv.org/abs/2603.03279v2 | 统一多模态控制的自主全身 loco-manipulation（据标题）[6] |
| ViLoMan: Learning Visual-Proprioceptive Whole-Body Loco-Manipulation Skills | 2026 | 未给出（arXiv cs.RO）[7] | > 待核实 [7] | arXiv 预印本，cs.RO [7] | 中（视觉+本体感知融合为近年主流配方）[7] | ★★★★☆ 代表「视觉–本体感知技能学习」路线 [7] | http://arxiv.org/abs/2609.19340v1 | 视觉-本体感知全身 loco-manipulation 技能学习（据标题）[7] |
| Towards Miniature Humanoid Tele-Loco-Manipulation Using Virtual Reality and Reinforcement Learning | 2026 | 未给出（arXiv cs.RO）[5] | > 待核实 [5] | arXiv 预印本，cs.RO [5] | 中（揭示了厂商主流做法：VR 上半身 + RL 下半身）[5] | ★★★★☆ 明确描述「VR 遥操上体 + RL 平衡下体」的工业界现实控制架构 [5] | http://arxiv.org/abs/2607.20399v1 | 摘要指出制造商常用方案为 VR 上半身遥操作 + RL 下半身平衡 [5] |
| Learning Humanoid Standing-up Control across Diverse Postures | 2025 | 未给出（arXiv cs.RO）[8] | > 待核实 [8] | arXiv 预印本，cs.RO [8] | 中 | ★★★☆☆ 面向跌倒恢复这一"非结构化长尾能力"[8] | http://arxiv.org/abs/2502.08378v2 | 多样姿态起身控制（据标题）[8] |
| Sim-to-Real Transfer in Deep Reinforcement Learning for Bipedal Locomotion | 2025 | 未给出（arXiv cs.RO）[9] | > 待核实 [9] | arXiv 预印本，cs.RO [9] | 中 | ★★★★☆ sim-to-real 迁移是本节所有工作的共同瓶颈 [9] | http://arxiv.org/abs/2511.06465v1 | 双足 locomotion 的深度 RL sim-to-real 迁移（据标题）[9] |
| Learning Sim-to-Real Humanoid Locomotion in 15 Minutes | 2025 | 未给出（arXiv cs.RO）[10] | > 待核实 [10] | arXiv 预印本，cs.RO [10] | 中（"15 分钟"是极强的效率宣称，需第三方复现）[10] | ★★★★☆ 训练效率的数量级宣称，是判断拐点的关键信号（但**未获独立验证**）[10] | http://arxiv.org/abs/2512.01996v1 | 宣称 15 分钟内完成 sim-to-real 人形 locomotion 学习 [10] |
| Isaac Sim-to-Real: Reinforcement Learning based Locomotion for Quadrupeds | 2026 | 未给出（arXiv cs.RO）[12] | > 待核实 [12] | arXiv 预印本，cs.RO [12] | 中 | ★★★☆☆ 四足 sim-to-real 在 Isaac 生态内的工程化复现样本 [12] | http://arxiv.org/abs/2607.18135v1 | 基于 Isaac 的四足 RL locomotion sim-to-real（据标题）[12] |
| Robust Visuomotor Control for Humanoid Loco-Manipulation Using Hybrid Reinforcement Learning | 2025 | 未给出（DOI 指向 MDPI *Biomimetics*）[11] | > 待核实 [11] | **同行评审期刊**（MDPI Biomimetics，DOI:10.3390/biomimetics10070469），本批中唯一非预印本 [11] | 中（B 级以上证据，但 MDPI 期刊影响力需另评）[11] | ★★★★☆ 本批证据中**权威等级最高**的一条：混合 RL + 视觉运动控制 [11] | https://doi.org/10.3390/biomimetics10070469 | 混合 RL 的人形 loco-manipulation 视觉运动控制器 [11] |

**相对 2023 基线的三条实质增量**（每条均标注证据强度）：

1. **控制范式：从「模型 → 优化」转向「策略 → 学习」**。2024–2026 的工作普遍以 RL/模仿学习策略承担全身协调，而非在线求解 MPC/iLQR [1][6][7][11]。**证据强度：中**——全部为论文自述，未见与 MPC 基线的同条件 head-to-head 对比 → 具体性能差值 `> 待核实`。
2. **架构范式：模块化规划-控制栈被「分层/统一多模态」替代**。[2] 明确采用「空间大脑（高层理解）+ 动作小脑（低层泛化动作）」两段式；[6] 直接以 "Unified Multimodal Control" 命名。**证据强度：中**，均为 arXiv 预印本 [2][6]。
3. **交互对象：从静态场景扩展到动态/快速运动物体**。[1] 以羽毛球（badminton）全身交互为任务，明确区别于既有静态场景操作。**证据强度：低**（单篇、无第三方复现）[1]。

### 1.2 与 VLA / 基础模型的接口方式

- **VLA 侧规模跃升信号**：Xiaomi-Robotics-1 宣称以「超过 100K 小时真实世界轨迹」扩展 VLA 模型（2026）[13]。热度：> 待核实（候选块无 citations/stars）[13]；权威：arXiv 预印本 [13]；关注度：**高**（超大规模真机数据 + 厂商参与，属当前具身智能最热叙事）[13]；推荐度 ★★★★★（直接命中"VLA 与底层控制器接口"子问题，但**数据规模宣称未获独立审计**）[13]。
- **接口方式的具体形态**：本批证据显示两条路线——(a) 高层语义/空间理解 + 低层可泛化动作生成的分层接口 [2]；(b) 面向控制器侧的「策略推理引擎」化，即把学习型策略作为控制器管线中的一等公民（见 §2 ros2_control 的 RL inference engine 方向）[32]。
- **接口的量化评测**：候选池中**无任何**同时覆盖 VLA 高层与底层控制器、并在统一基准上对比的条目 → `> 待核实`。

---

## 2. 工业界与产品（Industry & Product）

**一句话增量判断**：可核查的工业界证据仅两条——**厂商级 VLA 数据规模化** [13] 与 **ROS 2 官方控制框架 ros2_control 正在主动接纳 RL 推理** [32]；其余产品化、量产、部署数量均 `> 待核实`。

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Xiaomi-Robotics-1（100K+ 小时真机轨迹的 VLA） | 2026 | Xiaomi（据标题）[13] | > 待核实 [13] | arXiv 预印本，非同行评审 [13] | 高（大厂 + 100K 小时真机数据，为当前最强叙事之一）[13] | ★★★★★ 判断"VLA 是否进入数据规模竞赛"的一手信号 [13] | http://arxiv.org/abs/2607.15330v2 | 以 10 万+ 小时真实轨迹扩展 VLA；**数据口径与真机部署量待核实** [13] |
| ros2_control（Rolling 文档 / 官方生态） | 2026 | ros2_control 项目治理组（control.ros.org）[32] | > 待核实（无 star/下载数）[32] | **官方文档**（ROS 2 官方生态项目，含 Project Governance / Release Notes / Migration Guides 章节）[32] | 中（2023→2026 连续多年 ROSCon 专题 workshop，最近为 2026-09 ROSCon 2026）[32] | ★★★★★ 回答「ROS 2 控制栈现状」的首要一手来源 [32] | https://control.ros.org/rolling/doc/resources/resources.html | 见 §开源项目表 |
| 「VR 上半身遥操 + RL 下半身平衡」的制造商主流方案 | 2026 | 未给出 [5] | > 待核实 [5] | arXiv 预印本 [5] | 中 | ★★★★☆ 摘要直接陈述**制造商在用**的控制架构，是本报告少见的"工业实态"证据 [5] | http://arxiv.org/abs/2607.20399v1 | 原文：manufacturers 常用 VR 上体遥操作 + RL 下体平衡 [5] |
| 全身关节级遥操作产品形态 | 2025 | 未给出 [3] | > 待核实 [3] | arXiv 预印本 [3] | 中 | ★★★★☆ 全身遥操作是人形真机数据采集的产业化前置条件 [3] | http://arxiv.org/abs/2508.00162v2 | 指出既有工作很少支持全身关节级遥操 [3] |
| 训练效率产品化宣称（"15 分钟"） | 2025 | 未给出 [10] | > 待核实 [10] | arXiv 预印本（**仅有宣称**）[10] | 中 | ★★★☆☆ 若被复现则显著降低工程成本，当前仅单方宣称 [10] | http://arxiv.org/abs/2512.01996v1 | 见 §4 拐点信号 |

**工业界证据缺口（必须显式声明）**：
- 无任何候选来源覆盖**人形/四足的出货量、量产计划、客户部署数、商业合同或定价** → `> 待核实`。
- 无任何候选来源覆盖 **MoveIt 2 / Nav2 的工业采用率** → `> 待核实`。
- 唯一可确认的"官方级"工程信号来自 ros2_control 官方文档 [32]；**厂商官方博客、技术报告、发布会材料在本批候选中为 0 条**。

---

## 3. 蓝海与缺口（Blue Ocean & Gaps）

**一句话增量判断**：本主题最大的、可由证据直接指认的缺口有三类——**评测/基线的结构性缺失**、**ros2_control 与学习型策略的接口尚未标准化** [32]、以及**经典动力学基线与现代 RL 全身控制的桥接研究近乎空白**（候选池覆盖 0/4）[14][15][16][22]。

### 3.1 经典与奠基性工作（作为增量对照的基线）

> 说明：q2 子问题的候选池（[14][15][16][22]）与四类经典基线**完全错配，覆盖率 0/4** [14][15][16][22]。全批来源中**唯一**真正对应该基线的条目是 [23]（Featherstone 体系的 Spatial Vector Algebra 章节）。因此下表**只能给出一行可信条目，其余为证据缺口**。

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Spatial Vector Algebra（刚体动力学算法，空间向量 6D 代数） | > 待核实（Springer 版本，DOI 前缀 1-4899 对应 2014 重印）| Roy Featherstone（据 DOI 所属专著）| > 待核实（候选块未给 citations）[23] | 学术专著章节（Springer），非预印本 [23] | 中（机器人动力学教材级基础，长期被引用语境）[23] | ★★★★★ 本批**唯一**可信的经典动力学基线锚点 [23] | https://doi.org/10.1007/978-1-4899-7560-7_2 | 空间向量代数：关节体递推动力学（RNEA/CRBA）与浮基系统的数学基础 [23] |
| Khatib 操作空间 / 全身控制（operational space & whole-body control） | — | — | > 待核实 | > 待核实 | — | — | > 待核实 | **候选池 0 条覆盖** [14][15][16][22]，需重新检索 |
| DDP / iLQR / MPC 轨迹优化与最优控制 | — | — | > 待核实 | > 待核实 | — | — | > 待核实 | 候选池 0 条覆盖；[22] 虽属 eess.SY「控制」但对象为网络传染病隔离，**不可替代** [22] |
| 旋量 / SE(3) 运动学数学基础 | — | — | > 待核实 | > 待核实 | — | — | > 待核实 | [15][16] 仅为"vector space / geometrical"字面相似，属交换代数与空间数据算法，**不构成数学基础证据** [15][16] |
| 刚体旋转不变量（Euler 角） | 2016 | 未给出 [18] | > 待核实 [18] | arXiv 预印本（非机器人学 venue）[18] | 低 | ★★☆☆☆ 仅与刚体旋转数学相关，**不覆盖**递推动力学与最优控制 [18] | http://arxiv.org/abs/1601.04526v1 | 固定点刚体旋转不变量（欧拉角），可作为数学侧旁证，非控制基线 |

### 3.2 蓝海缺口（可操作的无人区）

1. **RL 全身控制与经典动力学基线的桥接研究缺失**：2024–2026 的全身控制工作 [1][2][6][7][11] 与 Featherstone 空间向量代数 [23] 之间**没有出现在同一候选来源中**；是否存在「以空间向量代数/操作空间控制作为 RL 先验或对照」的工作，本批证据无法回答 → `> 待核实`。这是本报告识别出的**最高杠杆学术空白**。
2. **ros2_control 的学习型策略接口尚未标准化**：官方侧仅以 GSoC 2026 项目「Physical AI Inference and Trajectory Upscaling for ros2_control」与 2026-09 ROSCon workshop「Scaling ros2_control: From Async Hardware Drivers to RL Inference Engines」给出**方向性信号**，尚无标准接口规范 [32]。关注度：**中**（有明确年度工程投入与会议议程）[32]；推荐度 ★★★★☆（控制栈 × 学习策略的标准化是最接近落地的空白）[32]。
3. **全身 loco-manipulation 的统一评测缺失**：候选池中**没有任何数据集或基准来源**（见 §数据集与基准表），因此 [1][2][6][7] 之间的能力无法横向比较 → `> 待核实`。
4. **真机数据采集瓶颈的补位机会**：全身关节级遥操作被明确指认为既有工作的稀缺能力 [3]，而 VLA 侧又在索要 100K 小时量级真机轨迹 [13] → 二者张力构成明确工程空白（本报告判断，依据链见 §7）。
5. **检索/术语治理缺口（元层面）**：本批候选中，机器人 Pinocchio 库被天体物理 PINOCCHIO 论文 [34] 误召回，且 [24]–[31]、[33] 为 2025 年各类视觉/NLP/音频挑战赛噪声 → 说明主题检索式严重污染，**任何基于本批未精检候选的"最新进展"结论都应降级** [24][25][26][29][30][31][33][34]。

### 3.3 数据集与基准

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| > 待核实 | — | — | > 待核实 | > 待核实 | — | — | > 待核实 | **候选池 [1]–[34] 中不存在任何数据集/基准来源**：无 Open X-Embodiment / DROID / LIBERO / SimplerEnv / RoboArena 等条目 |
| > 待核实 | — | — | > 待核实 | > 待核实 | — | — | > 待核实 | 因此本报告**无法**给出任何仿真 SOTA vs 真机 SOTA 的对比，亦无法判断评测口径（任务数、本体数、成功率）[1][2][6][7][11][13] |

---

## 4. 瓶颈与拐点（Bottleneck & Inflection）

**一句话增量判断**：当前瓶颈从"算法能力"转移到**评测可信度**与**训练/迁移成本**；拐点信号（"15 分钟 sim-to-real" [10]）已出现但**仅有单方宣称，未获独立验证**，故拐点判定为 `推测`。

| # | 瓶颈 | 证据 | 是否临近拐点 | 拐点信号（可观测） |
|---|---|---|---|---|
| 1 | **sim-to-real 迁移仍是共同瓶颈** | [9] 专题研究双足 sim-to-real；[12] 四足 Isaac sim-to-real；[4] 检验域随机化对扩散策略的作用 [4][9][12] | 推测 | 若出现「同一策略在 ≥2 种本体上零样本迁移且被第三方复现」→ 判定成立；当前 `> 待核实` |
| 2 | **训练成本** | [10] 宣称 15 分钟完成 sim-to-real 人形 locomotion [10] | 推测（单方宣称） | 若 2027 年前有独立团队复现同等量级训练时长 → 判定成立 [10] |
| 3 | **评测与可信度** | 候选池 **无任何基准/榜单来源**；[1][2][6][7] 均为自评 | 未见拐点 | 需出现统一 benchmark 的第三方排名 → `> 待核实` |
| 4 | **实时性与中间件（DDS / Zenoh / micro-ROS / LTS 实时性）** | 候选池 **0 条覆盖** → [32] 仅提供官方文档入口 | 未知 | 需 REP 2000 与各发行版官方文档证据 → `> 待核实`（**关键缺口**）[32] |
| 5 | **控制栈与学习策略的集成复杂度** | [32] 以 2026 GSoC「Physical AI Inference and Trajectory Upscaling」与 2026-09 ROSCon workshop「Async Hardware Drivers → RL Inference Engines」为方向 [32] | 中（有官方议程，尚无标准） | 若 ros2_control 发布官方 RL 推理接口规范并进入 LTS → 判定成立 [32] |
| 6 | **数据采集人力成本** | [3] 指出全身关节级遥操作稀缺；[13] 需求 100K+ 小时真机轨迹 [3][13] | 中 | 若出现可规模化的全身遥操作/自动标注管线 → 判定成立 [3][13] |

**方法论风险（元瓶颈）**：本批候选中 [24]–[31]、[33] 为与主题无关的 2025 年挑战赛/QA 论文，[34] 为 2001 年天体物理 PINOCCHIO 论文（与机器人 Pinocchio **仅同名**）→ 若下游环节不做同名消歧，将产生**系统性误引**。此为本报告明确点出的知识治理瓶颈 [24][25][29][30][31][33][34]。

---

## 5. 社会·政策·国际（Society, Policy & Geopolitics）

**一句话增量判断**：**本周期在本批证据中无显著可核查变化**——候选池 34 条中**没有**任何监管文件、标准（ISO/IEEE/REP 类）、政府政策、出口管制、供应链或劳动影响的一手来源。

- **监管与标准**：`> 待核实`——无候选来源覆盖欧盟 AI Act、ISO 10218/ISO/TS 15066、或任何机器人安全标准更新。
- **国际/地缘与供应链**：`> 待核实`——无候选来源覆盖芯片/减速器/灵巧手供应链或出口限制。
- **伦理与人机信任（弱相关线索）**：TRUST 2025: SCRITA and RTSS @ RO-MAN 2025 [28] 属人机交互中的信任/可信度 workshop，可作为**社会接受度研究**的方向性旁证，但与运动学/控制/ROS 2 **不直接相关**。热度：> 待核实 [28]；权威：workshop（RO-MAN 2025 附属），非正式论文 [28]；关注度：低 [28]；推荐度 ★★☆☆☆（仅作社会维度线索）[28]。
- **劳动影响**：`> 待核实`——无证据。
- **说明**：按 frontier-watch 纪律，本维度**不凑字数**，明确记录为「本周期无显著变化 / 证据缺失」。

---

## 6. 资本与生态（Capital & Ecosystem）

**一句话增量判断**：仅能确认两类生态信号——**大厂以超大规模真机数据投入 VLA** [13] 与 **ROS 2 官方社区通过 ROSCon + GSoC 持续投入控制栈** [32]；融资、并购、人才流动数据**全部缺失**。

| 维度 | 可核查增量 | 时间 | 证据 | 强度 |
|---|---|---|---|---|
| 厂商资本投入 | Xiaomi-Robotics-1 以 100K+ 小时真机轨迹扩展 VLA，暗示重资产数据采集投入 [13] | 2026 | arXiv 预印本，厂商署名 [13] | 中（厂商自述，未经审计）[13] |
| 开源社区人力 | ros2_control 侧 GSoC 2026 立题「Physical AI Inference and Trajectory Upscaling」[32] | 2026 | 官方文档条目 [32] | 中高（官方项目页）[32] |
| 会议生态 | ros2_control 专题 workshop 连续出现：2023-10-18 (on Steroids) → 2024-10 (Fun with Controllers) → 2025-09 (ROSCon UK) / 2025-10 (ROSCon 2025) → **2026-09 (ROSCon 2026: Async Hardware Drivers → RL Inference Engines)** [32] | 2023–2026 | 官方文档 [32] | 高（官方一手，时间线完整）[32] |
| 学术方向重心 | 全身 loco-manipulation / sim-to-real 方向在 2024–2026 持续产出（[4]→[1][8][9][11]→[2][5][6][7][12][13]）[1][2][4][5][6][7][8][9][11][12][13] | 2024–2026 | 全部为 arXiv/期刊条目 | 中（数量信号，非质量信号） |
| 融资/并购/人才流动 | `> 待核实` | — | 候选池 0 条 | 无 |
| 公司格局变化 | `> 待核实` | — | 候选池 0 条 | 无 |

**注意**：本维度**不得**由论文数量直接推断资本热度；上表"学术方向重心"仅为产出行数信号，**不构成投资结论**。

---

## 7. 信号与预测（Signals & Forecast）

**一句话增量判断**：可识别的最强早期信号是「**控制栈官方化接纳学习型策略**」（ros2_control [32]）与「**VLA 数据规模竞赛**」[13]；两者在 2026 年同时出现，预示未来 6–18 个月"分层的、策略内嵌的机器人软件栈"可能成为主流形态。

### 7.1 早期信号

| 信号 | 时间 | 证据 | 强度 |
|---|---|---|---|
| ros2_control 从"异步硬件驱动"走向"RL 推理引擎" | 2026-09（ROSCon 2026 workshop 议题）[32] | 官方文档 workshop 列表 [32] | 确定（官方议程）[32] |
| GSoC 2026 立项 Physical AI Inference + Trajectory Upscaling | 2026 [32] | 官方文档 GSoC 条目 [32] | 确定（立项存在），产出未知 [32] |
| 全身关节级遥操作被明确指认为稀缺能力 | 2025 [3] | arXiv 预印本 [3] | 较大概率 [3] |
| VLA 真机数据量级跃迁至 100K+ 小时 | 2026 [13] | arXiv 预印本（单方宣称）[13] | 推测（未审计）[13] |
| 动态快速物体全身交互（羽毛球）从静态任务外扩 | 2025 [1] | arXiv 预印本（无复现）[1] | 推测 [1] |

### 7.2 预测（[P]，均写成可证伪假设）

- **[P1] 控制栈分层标准化**
  *依据链*：官方 workshop 议题（2026-09）已明确指向 async hardware drivers + RL inference engines [32]；GSoC 2026 已立项 Physical AI Inference [32] → 推演：官方接口规范会在 12–18 个月内成形。
  *可证伪假设*：**若到 2027-12 之前，ros2_control 官方文档中未出现面向学习型策略推理的接口章节/规范，则本预测不成立**。置信度：**中等** [32]。
- **[P2] 训练成本数量级下降**
  *依据链*：[10] 宣称 15 分钟完成 sim-to-real 人形 locomotion [10]，与 [9][12] 所述 sim-to-real 主题形成对照 → 推演：训练时长将不再是主要门槛。
  *可证伪假设*：**若到 2027-06 之前无任何独立团队在公开材料中复现同等量级的训练时长，则本预测不成立（当前仅有宣称）**。置信度：**低** [10]。
- **[P3] 动态全身交互成为下一个争夺点**
  *依据链*：[1] 将任务从静态场景推进到快速运动物体交互 [1]；[6] 以统一多模态控制覆盖自主 loco-manipulation [6] → 推演：2027 年前"动态物体全身操作"会出现多团队竞争。
  *可证伪假设*：**若到 2027-12 之前，该方向（运动物体的全身 loco-manipulation）仍未出现 ≥3 个独立团队的真机演示，则本预测不成立**。置信度：**低–中**（仅 1–2 条直接证据）[1][6]。
- **[P4] 评测缺口将成为显性争议焦点**
  *依据链*：本批 [1][2][6][7][11][13] 全部为自评、且候选池 0 条基准来源 → 推演：社区将被迫建立统一基准。
  *可证伪假设*：**若到 2027-12 之前没有出现被 ≥3 个独立团队报告结果的全身 loco-manipulation 公开基准，则本预测不成立**。置信度：**中等**（缺口由证据直接指认，但基准出现时间不可控）。
- **[P5] 经典动力学与现代 RL 的桥接研究将出现（本报告最高杠杆预测）**
  *依据链*：Featherstone 空间向量代数 [23] 作为唯一基线锚点，与 2024–2026 全身 RL 工作 [1][2][6][7] 在候选池中**零交集** → 推演：这是一个无人区。
  *可证伪假设*：**若到 2027-12 之前，arXiv cs.RO 上仍未出现将空间向量代数/操作空间控制作为 RL 结构化先验或对照基线的全身控制工作，则本预测不成立**。置信度：**中等** [23][1][2][6][7]。

### 7.3 Watchlist（值得持续关注）

| 对象 | 关注理由 | 跟踪指标 | 链接 |
|---|---|---|---|
| ros2_control（Rolling → 下一 LTS） | 官方控制栈是否落地 RL 推理接口 [32] | Release Notes / Migration Guides 新条目、ROSCon 2027 议题 [32] | https://control.ros.org/rolling/doc/resources/resources.html |
| Xiaomi-Robotics-1 | VLA 数据规模的工业级标杆 [13] | 是否公开数据/权重、是否有第三方复现 [13] | http://arxiv.org/abs/2607.15330v2 |
| Sim-to-real 训练效率 | "15 分钟"宣称能否被复现 [10] | 独立复现报告、成本对比 [10] | http://arxiv.org/abs/2512.01996v1 |
| 动态全身交互（badminton 类） | 是否从单篇扩展到多团队 [1] | 同任务真机演示数量 [1] | http://arxiv.org/abs/2511.11218v4 |
| 全身遥操作数据采集 | VLA 数据需求的正面瓶颈 [3][13] | 关节级遥操作开源实现与吞吐量 [3] | http://arxiv.org/abs/2508.00162v2 |
| ROS 2 实时性与中间件（DDS/Zenoh/micro-ROS） | **本报告最大证据缺口** | REP 2000、各发行版官方文档、DDS 基准 → 目前 `> 待核实` [32] | — |

---

## 附：证据强度自检（诚实声明）

| 检查项 | 结论 |
|---|---|
| 是否覆盖 2024–2026 最新进展？ | 部分覆盖：全身 RL / loco-manipulation / sim-to-real / VLA 有 [1][2][4]–[13]；**近 1–2 年运动学与经典控制（MPC/iLQR/DDP）本身的新进展为 0 条** |
| 是否覆盖经典工作？ | **仅 1 条**（[23] Featherstone 空间向量代数）；Khatib 全身控制、DDP/iLQR/MPC、SE(3)/旋量 均为 `> 待核实` [14][15][16][22] |
| 是否覆盖开源实现？ | **仅 1 条**（[32] ros2_control 官方文档）；MoveIt 2 / Nav2 / Pinocchio / Crocoddyl / OCS2 / Drake / MuJoCo / DDS / Zenoh / micro-ROS **全部缺失** [32][34] |
| 是否覆盖数据集与基准？ | **0 条** → 全表 `> 待核实` |
| 是否区分论文宣称 vs 第三方复现？ | 是：全部标注为「仅论文自述/单方宣称」，无第三方复现来源 [1]–[13] |
| 是否编造数字？ | **否**：所有 citations / star / 下载量字段均写 `> 待核实` [1]–[34] |

---

## 参考来源

[1] Humanoid Whole-Body Badminton via an Annealed Reinforcement Learning Curriculum — http://arxiv.org/abs/2511.11218v4
[2] Humanoid Whole-Body Manipulation via Active Spatial Brain and Generalizable Action Cerebellum — http://arxiv.org/abs/2605.21133v2
[3] CHILD (Controller for Humanoid Imitation and Live Demonstration): a Whole-Body Humanoid Teleoperation System — http://arxiv.org/abs/2508.00162v2
[4] The Role of Domain Randomization in Training Diffusion Policies for Whole-Body Humanoid Control — http://arxiv.org/abs/2411.01349v1
[5] Towards Miniature Humanoid Tele-Loco-Manipulation Using Virtual Reality and Reinforcement Learning — http://arxiv.org/abs/2607.20399v1
[6] ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation — http://arxiv.org/abs/2603.03279v2
[7] ViLoMan: Learning Visual-Proprioceptive Whole-Body Loco-Manipulation Skills for Humanoid Robots — http://arxiv.org/abs/2609.19340v1
[8] Learning Humanoid Standing-up Control across Diverse Postures — http://arxiv.org/abs/2502.08378v2
[9] Sim-to-Real Transfer in Deep Reinforcement Learning for Bipedal Locomotion — http://arxiv.org/abs/2511.06465v1
[10] Learning Sim-to-Real Humanoid Locomotion in 15 Minutes — http://arxiv.org/abs/2512.01996v1
[11] Robust Visuomotor Control for Humanoid Loco-Manipulation Using Hybrid Reinforcement Learning — https://doi.org/10.3390/biomimetics10070469
[12] Isaac Sim-to-Real: Reinforcement Learning based Locomotion for Quadrupeds — http://arxiv.org/abs/2607.18135v1
[13] Xiaomi-Robotics-1: Scaling Vision-Language-Action Models with over 100K Hours of Real-World Trajectories — http://arxiv.org/abs/2607.15330v2
[14] The Relativistic Elasticity of Rigid Bodies — http://arxiv.org/abs/physics/0307019v3（**主题误召回，非机器人学**）
[15] Ancestor ideals of vector spaces of forms, and level algebras — http://arxiv.org/abs/math/0307281v1（**无关**）
[16] Connection errors in networks of linear features and the application of geometrical reduction in spatial data algorithms — http://arxiv.org/abs/1101.5410v4（**无关**）
[17] The $h$-vector of a relatively compressed level algebra — http://arxiv.org/abs/math/0503526v2（**无关**）
[18] On the invariant motions of rigid body rotation over the fixed point, via Euler angles — http://arxiv.org/abs/1601.04526v1（弱相关：刚体旋转数学）
[19] A Parametric and Feasibility Study for Data Sampling of the Dynamic Mode Decomposition — http://arxiv.org/abs/2110.06573v2（**无关**）
[20] Invariant theory and coefficient algebras of Lie algebras — http://arxiv.org/abs/2411.11095v3（**无关**）
[21] Categorical Constructions for Hopf Algebras — http://arxiv.org/abs/0905.2613v3（**无关**）
[22] A Quantum-Compliant Formulation for Network Epidemic Control — http://arxiv.org/abs/2509.00337v1（**控制关键词误召回，非机器人轨迹优化**）
[23] Spatial Vector Algebra — https://doi.org/10.1007/978-1-4899-7560-7_2
[24] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1（**无关**）
[25] NTIRE 2025 Challenge on Image Super-Resolution (x4): Methods and Results — http://arxiv.org/abs/2504.14582v3（**无关**）
[26] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1（**无关**）
[27] TDCOSMO 2025: Cosmological constraints from strong lensing time delays — http://arxiv.org/abs/2506.03023v4（**无关**）
[28] TRUST 2025: SCRITA and RTSS @ RO-MAN 2025 — http://arxiv.org/abs/2509.11402v1（弱相关：人机信任/HRI）
[29] VLSP 2025 MLQA-TSR Challenge: Vietnamese Multimodal Legal Question Answering on Traffic Sign Regulation — http://arxiv.org/abs/2510.20381v1（**无关**）
[30] The AudioMOS Challenge 2025 — http://arxiv.org/abs/2509.01336v1（**无关**）
[31] SINAI at eRisk@CLEF 2025: Transformer-Based and Conversational Strategies for Depression Detection — http://arxiv.org/abs/2509.19861v1（**无关**）
[32] Resources — ROS2_Control: Rolling Oct 2026 documentation — https://control.ros.org/rolling/doc/resources/resources.html
[33] RealTime QA: What's the Answer Right Now? — http://arxiv.org/abs/2207.13332v2（**无关**）
[34] PINOCCHIO and the hierarchical build-up of dark matter haloes — http://arxiv.org/abs/astro-ph/0109324v1（**同名误召回，与机器人 Pinocchio 库无关**）

---

*Generated by research-bot · topic=`机器人运动学控制与-ros-2` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`deepseek-v4-flash` · sources=34 · duration=182s · 2026-10-07T22:12:36+00:00*
