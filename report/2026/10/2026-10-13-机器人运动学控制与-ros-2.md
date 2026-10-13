# 机器人运动学、控制与 ROS 2：2024–2026 增量调研报告

**日期**：2026-10-13（UTC）
**领域**：机器人运动学 / 全身控制（WBC）/ 接触密集操作 / Sim-to-Real / ROS 2 生态
**检索源数量**：候选来源 32 条（[1]–[32]），其中与本主题**直接相关**约 18 条；**ROS 2 运动规划/控制/仿真栈**与 **LIBERO/DROID/SimplerEnv/RoboArena 等基准**在本次证据池中**近乎零覆盖**
**证据基础声明**：本报告仅基于 [1]–[32] 可核查条目撰写。证据池存在明显偏斜——条目高度集中于**人形全身控制与接触密集操作的 arXiv cs.RO 预印本**，而 ROS 2 生态、产业融资、政策法规、数据集榜单四类信息几乎缺失。凡证据不足处一律标注 `> 待核实`，并**不给出无来源的 URL、引用数或 star 数**。候选池中 [1][10][13][14][16][17][18][20][21][32] 经核对与本主题无关（短视频参与度预测、语音隐私、图像超分、宇宙学、词典条目等），仅作噪声登记，不参与论证；[15] 为 RO-MAN 2025 信任主题 workshop 论文，相关性弱，仅在社会维度谨慎引用。

---

## 1. 进展与热点（Progress & Hotspots）

**一句话增量判断**：相对经典「任务空间 IK + 分层二次规划 WBC + MPC/WBC 两段式」范式，2024–2026 的增量并不在运动学求解器本身，而在**三条迁移线**：①人形机器人从 locomotion 转向**全身操作与动态交互**（羽毛球、遥操作、无机器人示教）；②控制范式从「结构化模型控制」转向「**RL 策略 + 课程/随机化**」；③sim-to-real 的焦点从域随机化转向「**接触表征与在线合规残差学习**」。运动学/IK 层面的新算法证据在本批材料中**缺失**。

### 1.1 最新进展（2024–2026）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Humanoid Whole-Body Badminton via an Annealed Reinforcement Learning Curriculum | 2025 | cs.RO 预印本（作者信息未在候选块展开） | `> 待核实`（候选块无 citations/stars） | arXiv 预印本，非同行评审 [3] | 中——全身动态交互属于人形控制当前高讨论方向，但缺量化热度信号 | ★★★★☆ 全身动态物体交互的代表性尝试，值得读方法而非读数字 | http://arxiv.org/abs/2511.11218v4 | 用退火 RL 课程产出统一全身策略，面向快速运动物体交互 [3] |
| CHILD: Controller for Humanoid Imitation and Live Demonstration | 2025 | cs.RO 预印本 | `> 待核实` | arXiv 预印本 [4] | 中——现有工作少支持人形**关节级全身遥操作**，填补空白 | ★★★★☆ 全身关节级遥操作数据采集的关键基础设施候选 | http://arxiv.org/abs/2508.00162v2 | 指出现有遥操作很少支持人形全身关节级操作，限制任务多样性 [4] |
| Humanoid Manipulation Interface（无机器人示教的人形全身操作） | 2026 | cs.RO 预印本 | `> 待核实` | arXiv 预印本 [5] | 高（相对基线：把「机器人本体」从数据采集回路中拿掉，直击硬件物流瓶颈） | ★★★★☆ 若成立可大幅降低人形操作数据采集成本，但需真机复现验证 | http://arxiv.org/abs/2602.06643v2 | 现有路线依赖遥操作或视觉 sim-to-real RL，受硬件物流与奖励工程拖累，已演示技能有限 [5] |
| Humanoid Whole-Body Manipulation via Active Spatial Brain and Generalizable Action Cerebellum | 2026 | cs.RO 预印本 | `> 待核实` | arXiv 预印本 [7] | 中——"脑–小脑"分层与可泛化动作层是分层架构的新表述 | ★★★☆☆ 分层命名新颖，需看是否与经典分层 WBC 有本质差异 | http://arxiv.org/abs/2605.21133v2 | 全身操作的分层架构路线 [7] |
| Real-Time Whole-Body Control of Legged Robots with Model-Predictive Path Integral Control | 2024 | cs.RO 预印本 | `> 待核实` | arXiv 预印本 [8] | 中——采样型 MPC 用于实时 WBC，属对经典 MPC/WBC 两段式的直接替代尝试 | ★★★★☆ 与经典优化式 WBC 的对比价值高，建议精读其实时性论证 [8] | http://arxiv.org/abs/2409.10469v1 | 以模型预测路径积分（MPPI）实现腿式机器人实时全身控制 [8] |
| Learning Humanoid Standing-up Control across Diverse Postures | 2025 | cs.RO 预印本 | `> 待核实` | arXiv 预印本 [9] | 中——"多样姿态起立"连接 locomotion 与全身操作的能力边界 | ★★★☆☆ 单一技能但覆盖姿态多样性，可作 WBC 鲁棒性参照 [9] | http://arxiv.org/abs/2502.08378v2 | 跨多样姿态的学习式起立控制 [9] |
| Learning Getting-Up Policies for Real-World Humanoid Robots | 2025 | cs.RO 预印本 | `> 待核实` | arXiv 预印本 [23] | 中——面向真机的起身策略，与 [9] 构成同一问题簇 | ★★★☆☆ 与 [9] 交叉对读可判断「真机 vs 仿真」口径差异 [23] | http://arxiv.org/abs/2502.12152v2 | 真机人形起身策略学习 [23] |
| Robot Trains Robot: Automatic Real-World Policy Adaptation and Learning for Humanoids | 2025 | cs.RO 预印本 | `> 待核实` | arXiv 预印本 [25] | 中高——直指"真机 RL 从零训练/适配仍罕见"这一缺口 | ★★★★☆ 若可复现，是真机持续学习的关键增量 [25] | http://arxiv.org/abs/2508.12252v2 | 基于仿真的 RL 已推进人形 locomotion，但真机直接 RL 或从预训练策略适配仍少见 [25] |
| TDC: Sim-to-Real Transferable Directional Compliance for Contact-Rich Manipulation | 2026 | cs.RO 预印本 | `> 待核实` | arXiv 预印本 [28] | 中——"方向性合规（directional compliance）"是可迁移表征的新提法 | ★★★★☆ 与 [29] 的在线导纳残差学习形成演进对照 | http://arxiv.org/abs/2602.14174v2 | 面向接触密集操作的可迁移方向性合规 [28] |
| SARI: Phase-Split Sim-Real Co-Training for Contact-Rich Manipulation | 2026 | cs.RO 预印本 | `> 待核实`（2026-10 新近上线） | arXiv 预印本，**最新周期条目** [30] | 中——"分阶段 sim-real 协同训练"是 sim-to-real 流程层的新方案 | ★★★★☆ 属本周期最新信号，建议跟踪第三方复现 | http://arxiv.org/abs/2610.02804v1 | 阶段切分的仿真–真机协同训练 [30] |
| Beyond Binary: Sim-to-Real Dexterous Manipulation with Physics-Grounded Contact Representation | 2026 | cs.RO 预印本 | `> 待核实` | arXiv 预印本 [27] | 高——指出二值化接触表征是触觉模态无法 sim-to-real 的根因 | ★★★★☆ 接触表征问题是接触密集操作的核心痛点，方法层面值得精读 | http://arxiv.org/abs/2605.28812v1 | 现有 sim-to-real 方法因仿真–现实差距，无法有效利用触觉这类信息密集模态 [27] |
| Certifiably Safe Manipulation of Deformable Linear Objects via Joint Shape and Tension Prediction | 2025 | cs.RO 预印本 | `> 待核实` | arXiv 预印本 [26] | 中——「可证明安全 + 形状/张力联合预测」在 DLO 操作中较少见 | ★★★★☆ 安全性与接触约束联合建模，属尚未拥挤的方向 | http://arxiv.org/abs/2505.13889v1 | 多数现有模型只预测形状、忽略接触与张力约束，可能损伤物体和工具 [26] |
| The Role of Domain Randomization in Training Diffusion Policies for Whole-Body Humanoid Control | 2024 | cs.RO 预印本 | `> 待核实` | arXiv 预印本 [2] | 中——对"域随机化到底贡献多少"的消融式追问 | ★★★☆☆ 适合作为 sim-to-real 归因分析的基线 [2] | http://arxiv.org/abs/2411.01349v1 | 域随机化在全身人形扩散策略训练中的作用分析 [2] |

**注**：上表所有「热度」列在本批证据中**均无 citations 或 star 数据**，一律标注 `> 待核实`；这是证据池的结构性缺口，不代表这些工作影响力低。

### 1.2 经典与奠基性工作（作为「相对基线」的参照）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Whole-Body Geometric Retargeting for Humanoid Robots | 2019 | cs.RO 预印本（作者未在候选块展开） | `> 待核实` | arXiv 预印本 [6] | 中——人形全身"几何重定向"的思路在 2025–2026 遥操作工作中仍被沿用（见 [4]） | ★★★★☆ 理解 [4][5] 的前置经典读本 | http://arxiv.org/abs/1909.10080v1 | 全身几何重定向方法 [6] |
| Balance control in whole body coordination framework for biped humanoid robot MAHRU-R | 2008 | IEEE RO-MAN 2008（DOI 指向会议论文） | `> 待核实` | 同行评审会议论文（RO-MAN 2008），证据等级 A [11] | 低——年代久远，属历史脉络 | ★★☆☆☆ 仅作"全身协调框架"历史锚点，非当前工程首选 [11] | https://doi.org/10.1109/roman.2008.4600699 | 双足人形 MAHRU-R 的全身协调平衡控制 [11] |
| Learning Contact-Rich Manipulation Skills with Guided Policy Search | 2015 | cs.RO 预印本（Levine 等，作者信息见原论文） | `> 待核实` | arXiv 预印本，该方向被广泛引用的早期工作 [31] | 中——接触密集操作的"经典起点" | ★★★★☆ 理解从 GPS → 在线导纳残差 [29] → 方向性合规 [28] → 协同训练 [30] 演进的起点 | http://arxiv.org/abs/1501.05611v2 | 引导式策略搜索学习接触密集操作技能 [31] |
| Efficient Sim-to-real Transfer of Contact-Rich Manipulation Skills with Online Admittance Residual Learning | 2023 | cs.RO 预印本 | `> 待核实` | arXiv 预印本 [29] | 中——在线导纳残差是 [28][30] 的直接前作 | ★★★★☆ 接触密集 sim-to-real 的承上启下节点 | http://arxiv.org/abs/2310.10509v1 | 用在线导纳残差学习实现高效的 sim-to-real 迁移 [29] |
| Optimization of Humanoid Robot Designs for Human-Robot Ergonomic Payload Lifting | 2022 | cs.RO 预印本 | `> 待核实` | arXiv 预印本 [24] | 低——机械设计优化，属邻近分支 | ★★☆☆☆ 与"控制/运动学"主题交叉但不直接 | http://arxiv.org/abs/2211.13503v1 | 面向人机工效学负载搬运的人形设计优化 [24] |

**脉络叙事（承上启下）**：接触密集操作线可读作 **GPS（2015）[31] → 在线导纳残差（2023）[29] → 方向性合规 TDC（2026）[28] 与 阶段切分协同训练 SARI（2026）[30]**；人形全身线可读作 **几何重定向（2019）[6] → 关节级全身遥操作 CHILD（2025）[4] → 无机器人示教 HuMI（2026）[5]**。**但需强调**：本批证据**未能提供任何引用数或第三方复现**，上述脉络是基于方法问题的相似性推断，属**编辑性梳理而非引文链证据**，`> 待核实`。

---

## 2. 工业界与产品（Industry & Product）

**一句话增量判断**：本批证据中**工业界一手材料近乎为零**；可确认的产业侧增量只有一项——**ALOHA 2 开源全部硬件设计并提供经系统辨识的 MuJoCo 模型**[19]；ROS 2 侧仅检索到一篇**零引用**的架构综述类期刊论文 [22]，无法支撑"事实标准"判断。

### 2.1 开源项目（可确认者）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| ALOHA 2 开源硬件与 MuJoCo 模型 | 2024 | ALOHA 2 Team 等 26 位作者（含 Chelsea Finn、Tony Z. Zhao），arXiv cs.RO，2024-02-07 提交 | `> 待核实`（候选块未给 star / 引用数） | 官方项目论文（arXiv 预印本），证据等级 B [19] | 中——被候选块描述为双臂遥操作硬件的事实参考设计之一，但**无量化信号**支撑 | ★★★★☆ 开源硬件 + 系统辨识 MuJoCo 模型，对**可复现性**有直接价值；但**与 ROS 2 栈的对接方式在证据中未体现** | http://arxiv.org/abs/2405.02292v1 | 开源全部硬件设计与详细教程，并给出经系统辨识的 ALOHA 2 MuJoCo 模型，目标是降低双臂操作数据采集的硬件成本与复现门槛 [19] |

### 2.2 ROS 2 侧产业/工程证据

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| ROS 2: Architecture and Practical Implementation Features | 2025 | 期刊论文（Taurida National V.I. Vernadsky University, Series: Technical Sciences），2025-01-01 | **citations=0**（候选块标注） | 非机器人主流会议/期刊；证据等级 C [22] | 低——引用数为 0，候选块无社区讨论或榜单信号 | ★☆☆☆☆ 未涉及运动规划/控制/仿真标准，作为"事实标准"证据价值低，仅作线索 | https://doi.org/10.32782/2663-5941/2025.3.2/22 | 仅讨论 ROS 2 架构与实现特征，摘要/片段未提运动规划、控制或仿真框架及其标准地位 [22] |

**明确的缺口陈述**：
- **MoveIt 2、ros2_control、Nav2、Gazebo / Isaac Sim 等工程事实标准**——本批候选证据中**没有任何一条**提供其版本演进、采用度或官方文档证据 [22]，因此"已成为工程事实标准"这一论断在本次材料中**无法成立** `> 待核实`。
- **厂商产品发布、量产、真机部署规模、商业化数据**——本批证据**零覆盖** `> 待核实`。
- 唯一可提及的产业邻近信号是 **Robot Trains Robot**[25]：它把"真机 RL 从零训练或从预训练策略适配仍属罕见"点名为限制人形机器人潜力释放的瓶颈，隐含的是**部署后持续学习**的产品化需求，但该文是 arXiv 预印本，**非厂商官方公告** [25] `> 待核实`。

---

## 3. 蓝海与缺口（Blue Ocean & Gaps）

**一句话增量判断**：本批证据暴露出的最大蓝海不在"再做一个全身控制策略"，而在**两处无人区**：①**ROS 2 工程栈与具身基础模型/基准之间的接口层与标准**（证据池完全空白）；②**接触约束下的可证明安全 + 多物理量联合预测**（如 DLO 的形状与张力联合建模 [26]）。

### 3.1 未解问题与无人区

| 缺口 | 现状证据 | 缺口性质 | 关注度 | 推荐度 |
|---|---|---|---|---|
| ROS 2 与具身基础模型/数据集基准的**集成与接口标准** | 候选证据未覆盖任何 ROS 2 运动规划、控制或仿真项目，也未出现任何基准名称 [22] | **生态级空白**（无人区） | 高（若无人做即意味着高杠杆） | ★★★★★ 谁先定义"ROS 2 ↔ VLA/基准"的接口层，谁占生态位 |
| **可证明安全**的接触密集操作（形状 + 张力**联合**预测） | 现有模型多数只预测形状，忽略接触与张力约束，可能损伤物体与工具 [26] | **方法级空白** | 中 | ★★★★☆ 安全约束与多物理量联合建模尚未拥挤 [26] |
| 人形**全身操作**的真机长时序自主技能 | 现有路线受硬件物流与复杂奖励工程阻碍，已演示的自主技能仍有限且受限 [5] | **验证级空白**（演示多、验证少） | 高 | ★★★★☆ 从"能演"到"能长期用"是最大落差 [5] |
| 触觉等**信息密集模态**在 sim-to-real 中的可用性 | 仿真–现实差距使触觉无法被有效使用；现有方法多依赖二值化接触表征 [27] | **表征级空白** | 中高 | ★★★★☆ 接触表征是接触密集操作的核心卡点 [27] |
| **真机强化学习**（从零或从预训练策略适配） | 基于仿真的 RL 大幅推进 locomotion，但真机 RL 仍罕见 [25] | **流程级空白** | 中高 | ★★★★☆ 若复现成立，将改变数据采集经济学 [25] |
| **评测口径不一致** | 本批证据无法给出任何统一基准的任务数/成功率口径 `> 待核实` | **评测基础设施空白** | 高 | ★★★★☆ 无统一口径则跨论文数字不可比 |

### 3.2 数据集与基准

> **重要声明**：本批 32 条候选证据中，**未出现 LIBERO、DROID、SimplerEnv、RoboArena 或任何同类具身智能基准的名称与指标**，因此下表第二块全部列项**无法评估**，不做任何数字或链接性推断。

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| ALOHA 2 系统辨识 MuJoCo 模型（仿真资产，非通用基准） | 2024 | ALOHA 2 Team 等 [19] | `> 待核实` | 官方项目论文（arXiv 预印本）[19] | 中——候选块描述其为双臂遥操作代表性开源方案，无量化信号 | ★★★★☆ 是**仿真模型可复现性**的直接相关条目，但**不属于 ROS 2 生态**，也不是任务基准 | http://arxiv.org/abs/2405.02292v1 | 提供经系统辨识的 MuJoCo 模型，服务于双臂操作数据采集与仿真复现 [19] |
| LIBERO | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实（本批证据未检索到）` | 本批候选块标题、摘要与可见内容中均未出现该基准名称与指标 |
| DROID | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实（本批证据未检索到）` | 同上 |
| SimplerEnv | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实（本批证据未检索到）` | 同上 |
| RoboArena | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实（本批证据未检索到）` | 同上 |

**结论**：本子问题（ROS 2 事实标准 + 数据集基准现状）在本轮证据下**不可回答**，需另起针对性检索（官方仓库、官方文档、基准榜单主页）方能成立 `> 待核实`。

---

## 4. 瓶颈与拐点（Bottleneck & Inflection）

**一句话增量判断**：当前最主要的瓶颈已从"控制算法不够好"转移到**数据获取成本**与**接触物理的可迁移表征**；2026 年出现两个潜在拐点信号——**分阶段 sim-real 协同训练**[30] 与 **physics-grounded 接触表征**[27]。

### 4.1 瓶颈清单

| 瓶颈类型 | 具体表现 | 证据 | 是否临近拐点 | 拐点信号 |
|---|---|---|---|---|
| **数据/硬件物流** | 人形全身操作依赖遥操作或视觉 sim-to-real RL，受硬件物流与奖励工程拖累，已演示自主技能有限 [5] | [5] | 可能临近 | 出现"无机器人示教"路线 [5] 与 "robot trains robot" 真机自学习 [25] |
| **接触物理表征** | 仿真–现实差距使触觉等信息密集模态无法被有效使用；现有方法多依赖二值化接触表征 [27] | [27] | 可能临近 | 转向 physics-grounded 连续接触表征 [27]；方向性合规可迁移表征 [28] |
| **接触密集迁移效率** | 在线导纳残差 [29] 之后仍需更高样本效率 | [29][28] | 观察中 | 分阶段 sim-real 协同训练 [30] |
| **安全性** | 形状预测忽略接触与张力约束，可能导致物体/工具损坏 [26] | [26] | 否（早期） | 出现"可证明安全"（certifiably safe）表述 [26] |
| **奖励工程** | 复杂奖励工程被点名为人形操作路线的主要阻碍 [5] | [5] | 否 | 无直接拐点证据 `> 待核实` |
| **评测口径** | 无法从本批证据判断统一口径 `> 待核实` | — | 未知 | — |
| **ROS 2 工程栈与前沿方法脱节** | 本批证据中无 ROS 2 与现代控制/学习方法的集成证据 [22] | [22] | 未知 | `> 待核实` |

### 4.2 值得单独标记的两个拐点候选

- **[30] SARI（2026-10，最新周期）**：提出"分阶段 + 仿真–真机协同训练"的流程方案，若被独立复现，意味着 sim-to-real 从"单向迁移"转向"双向共同训练"，属**流程范式级**变化。当前仅有预印本，**无第三方复现证据**，判定为「**演示级**」而非「已验证」。推荐度 ★★★★☆。
- **[27] Beyond Binary（2026-05）**：把 sim-to-real 失败归因于**接触表征的二值化**，而非策略或数据量，这是**归因层面**的新提法。若能证明替换表征即可解锁触觉迁移，则是接触密集操作的拐点。当前同样**仅有预印本**，判定为「**待验证**」。推荐度 ★★★★☆。

---

## 5. 社会·政策·国际（Society, Policy & Geopolitics）

**一句话增量判断**：本周期内**未见与本主题（机器人运动学/控制/ROS 2）直接相关的政策、标准或地缘证据**；唯一可用的结构性背景是**基础模型开发者透明度的年度性倒退**，它对"开源可复现"的宏观环境构成负面信号。

| 议题 | 增量与证据 | 热度 | 权威 | 关注度 | 推荐度 | 链接 |
|---|---|---|---|---|---|---|
| 基础模型透明度（开源可复现性的宏观背景） | 2025 FMTI 报告：平均分从 2024 年 **58 分降至 40 分**（满分 100）；公司在**训练数据与训练算力**方面最不透明；2025 版新增数据获取、使用数据与监控类指标，并首次评估 Alibaba、DeepSeek、xAI | `> 待核实`（候选块未给引用数） | arXiv 预印本 cs.AI，年度系列报告，作者含 Percy Liang、Rishi Bommasani、Sayash Kapoor，属透明度研究核心团队；证据等级 B [12] | 中——年度旗舰指数，媒体与政策讨论频繁，但**缺量化引用数据** | ★★☆☆☆ 与 ROS 2/运动控制主题**相关性弱**，仅可作开源透明度背景引用 | http://arxiv.org/abs/2512.10169v1 |
| 人机信任（社会接受度） | TRUST 2025: SCRITA and RTSS @ RO-MAN 2025 — 机器人信任主题 workshop 论文 | `> 待核实` | RO-MAN 2025 配套 workshop 论文，**非正式主会论文**，证据等级 C/D [15] | 低——候选块未提供引用、讨论或榜单信号 | ★★☆☆☆ 仅作为"社会信任"维度的线索；因等级偏低，**不用于支撑强结论** | http://arxiv.org/abs/2509.11402v1 |

**明确标注为不可得的内容**：
- 机器人安全标准（如 ISO 体系更新）、出口管制、供应链限制、各国机器人产业政策在 2025–2026 的**具体增量**——本批证据**零覆盖** `> 待核实`。
- ROS 2 治理机构（Open Robotics / 基金会）的组织与政策变化——**零覆盖** `> 待核实`。
- 劳动影响与伦理争议——**零覆盖**；本报告不基于记忆补写 `> 待核实`。

---

## 6. 资本与生态（Capital & Ecosystem）

**一句话增量判断**：本批证据对融资、并购、人才流动**零覆盖**；生态侧唯一可确认的增量是**开源硬件与仿真模型的持续开放**（ALOHA 2）[19]，以及**开源透明度宏观环境走弱**的背景信号 [12]。

| 维度 | 增量判断 | 证据 | 关注度 | 推荐度 |
|---|---|---|---|---|
| **开源硬件生态** | ALOHA 2 开源全部硬件设计、配套教程与系统辨识 MuJoCo 模型，目标降低双臂数据采集的硬件成本与复现门槛 [19] | [19]，arXiv 预印本，证据等级 B | 中——候选块视为代表性开源方案，但**无 star/采用度数字** | ★★★★☆ 对降低生态进入门槛有实际价值，但**与 ROS 2 栈的关系未在证据中体现** |
| **开源透明度环境** | 2025 年基础模型开发者透明度平均分由 58 降至 40（满分 100），训练数据与算力最不透明 [12] | [12]，arXiv 预印本，证据等级 B | 中 | ★★☆☆☆ 与机器人控制主题相关性弱，仅作生态背景 |
| **公司格局 / 融资 / 并购 / 人才流动** | **零覆盖** | — | `> 待核实` | `> 待核实`，本报告不填数 |
| **社区与标准组织动态（ROS 2 基金会、MoveIt/ros2_control 维护活跃度）** | **零覆盖**（仅一篇 citations=0 的架构论文 [22]） | [22]，证据等级 C | 低 | ★☆☆☆☆，无法支撑生态结论 |

> 说明：本维度缺口的成因是**检索证据池偏学术预印本**，而非该领域资本活动缺失。判断"资本活动强弱"需要融资数据库、厂商公告与并购新闻等一手来源，本批证据不具备 `> 待核实`。

---

## 7. 信号与预测（Signals & Forecast）

**一句话增量判断**：当前最强的两个早期信号是「**无机器人示教**」[5] 与「**接触表征归因转向**」[27]；两者都还停留在预印本+自评阶段，**尚未见独立复现**。

### 7.1 早期信号清单

| # | 信号 | 时间 | 证据强度 | 说明 |
|---|---|---|---|---|
| S1 | 人形全身操作的数据采集去机器人化（robot-free demonstrations） | 2026-02 [5] | 预印本 / 演示级 | 现有路线受硬件物流与奖励工程限制，已演示技能有限 [5] |
| S2 | sim-to-real 失败被归因于接触**表征**而非数据或策略 | 2026-05 [27] | 预印本 / 待验证 | 二值化接触表征阻碍触觉模态迁移 [27] |
| S3 | 仿真–真机从单向迁移转向**协同训练** | 2026-10 [30] | 预印本 / **本周期最新** | 阶段切分的 sim-real co-training [30] |
| S4 | 真机自学习（robot trains robot） | 2025-08 [25] | 预印本 / 演示级 | 真机 RL 从零或从预训练适配仍罕见 [25] |
| S5 | 接触密集操作引入**可证明安全**与多物理量联合预测 | 2025-05 [26] | 预印本 / 早期 | 只预测形状会忽略接触与张力约束 [26] |
| S6 | 全身动态物体交互（羽毛球等高动态任务） | 2025-11 [3] | 预印本 / 演示级 | 用退火 RL 课程训练统一全身策略 [3] |
| S7 | 基础模型透明度年度倒退 | 2025-12 [12] | 年度指数报告 / 已确证（报告内部口径） | 平均分 58 → 40 [12] |

### 7.2 可证伪预测（[P]，附依据与置信度）

- **[P1]**（置信度：较大概率）**若到 2027-06 之前，出现 ≥2 个独立团队在**真机**上复现"无机器人示教"人形全身操作 [5] 并开源数据/权重，则判断"人形控制重心已从 locomotion 迁移到全身操作"成立**；**若到 2027-06 仍只有原作者团队的演示，则该迁移判断降级为"叙事而非范式"**。依据链：S1 [5] + S4 [25] + 遥操作系统层面长期缺口 [4]。
- **[P2]**（置信度：推测）**若到 2027-06 之前，出现至少 1 篇论文证明**替换接触表征（二值 → physics-grounded）即可让触觉模态在真机 sim-to-real 中稳定生效** [27]，则判断"接触表征是当前接触密集操作的一级瓶颈"成立**；**若同期论文仍普遍依赖力/位混合调参或在线残差学习解决同一问题 [29][28]，则该归因被削弱**。
- **[P3]**（置信度：未知/需要数据）**若在 2027 年内出现 ROS 2 官方或主流社区（MoveIt 2 / ros2_control 层）与具身基础模型/评测基准之间的**标准化适配层**，则判断"ROS 2 生态正在被纳入具身智能技术栈"成立**；**目前本批证据中 ROS 2 与现代控制/学习方法之间**没有任何集成证据** [22]，因此该判断当前**不可评估** `> 待核实`**。
- **[P4]**（置信度：较大概率）**若到 2027-06 之前，"sim-real 协同/分阶段训练" [30] 未被任何第三方独立复现或引用式跟进，则该路线判定为"单点展示"而非拐点**。依据：S3 [30] 为 2026-10 新上线预印本，无复现证据。
- **[P5]**（置信度：推测）**若基础模型透明度指数在 2026 版继续下降或持平于 40 分区间 [12]，则"开源权重≠开源可复现"的落差将继续扩大**，进而抬高对**仿真模型/系统辨识资产**（如 ALOHA 2 的 MuJoCo 模型 [19]）这类"可复现基础设施"的相对价值。可观测指标：FMTI 2026 平均分、训练数据/算力维度的披露率。

### 7.3 Watchlist（值得持续关注）

1. **[30] SARI**（2026-10）——本周期最新 sim-real 协同训练信号，跟踪其第三方复现。
2. **[27] Beyond Binary**（2026-05）——接触表征归因，跟踪其是否被后续工作采纳为基线。
3. **[5] Humanoid Manipulation Interface**（2026-02）——去机器人示教的可行性边界。
4. **[7] Active Spatial Brain / Action Cerebellum**（2026-05）——分层架构是否带来可泛化动作层。
5. **[25] Robot Trains Robot**（2025-08）——真机自学习的样本效率与安全性。
6. **[19] ALOHA 2 MuJoCo 模型**——作为"可复现基础设施"的参照，观察其与 ROS 2 控制栈是否出现对接工作。
7. **ROS 2 官方生态（MoveIt 2 / ros2_control / Nav2 / Gazebo）版本与采用度**——**本轮无证据，需另起检索** `> 待核实`。
8. **LIBERO / DROID / SimplerEnv / RoboArena**——**本轮零覆盖，需另起检索** `> 待核实`。

---

## 8. 方法论自检与证据局限

| 自检项 | 结果 |
|---|---|
| 是否每条关键论断都带 [n]？ | 是；无来源处标 `> 待核实`，未编造编号 |
| 是否区分"最新进展"与"经典工作"？ | 是（§1.1 vs §1.2） |
| 是否给出热度/权威/关注度/推荐度四轴？ | 是；热度列因候选块缺 citations/stars 数据，绝大多数标 `> 待核实` |
| 是否区分"演示"与"独立验证"？ | 是；所有 2025–2026 条目均判定为**预印本/自评级**，未见第三方复现 |
| 是否覆盖七维？ | 是，§1–§7 逐一展开 |
| 是否点出蓝海与拐点？ | 是（§3、§4） |
| **最大局限** | 证据池偏斜：ROS 2 工程栈、数据集基准、产业资本、政策法规四类**近乎零覆盖**；结论不可外推至这些维度 |

---

## 参考来源

> 标注说明：`[相关]` 表示参与本报告论证；`[噪声]` 表示经核对与本主题无关，仅登记不引用为论据。

1. `[噪声]` VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1
2. `[相关]` The Role of Domain Randomization in Training Diffusion Policies for Whole-Body Humanoid Control — http://arxiv.org/abs/2411.01349v1
3. `[相关]` Humanoid Whole-Body Badminton via an Annealed Reinforcement Learning Curriculum — http://arxiv.org/abs/2511.11218v4
4. `[相关]` CHILD (Controller for Humanoid Imitation and Live Demonstration): a Whole-Body Humanoid Teleoperation System — http://arxiv.org/abs/2508.00162v2
5. `[相关]` Humanoid Manipulation Interface: Humanoid Whole-Body Manipulation from Robot-Free Demonstrations — http://arxiv.org/abs/2602.06643v2
6. `[相关]` Whole-Body Geometric Retargeting for Humanoid Robots — http://arxiv.org/abs/1909.10080v1
7. `[相关]` Humanoid Whole-Body Manipulation via Active Spatial Brain and Generalizable Action Cerebellum — http://arxiv.org/abs/2605.21133v2
8. `[相关]` Real-Time Whole-Body Control of Legged Robots with Model-Predictive Path Integral Control — http://arxiv.org/abs/2409.10469v1
9. `[相关]` Learning Humanoid Standing-up Control across Diverse Postures — http://arxiv.org/abs/2502.08378v2
10. `[噪声]` NTU-NPU System for Voice Privacy 2024 Challenge — http://arxiv.org/abs/2410.02371v1
11. `[相关]` Balance control in whole body coordination framework for biped humanoid robot MAHRU-R — https://doi.org/10.1109/roman.2008.4600699
12. `[相关]` The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1
13. `[噪声]` NTIRE 2025 Challenge on Image Super-Resolution (x4): Methods and Results — http://arxiv.org/abs/2504.14582v3
14. `[噪声]` SINAI at eRisk@CLEF 2025: Transformer-Based and Conversational Strategies for Depression Detection — http://arxiv.org/abs/2509.19861v1
15. `[弱相关]` TRUST 2025: SCRITA and RTSS @ RO-MAN 2025 — http://arxiv.org/abs/2509.11402v1
16. `[噪声]` Fluid Antenna System: New Insights on Outage Probability and Diversity Gain — http://arxiv.org/abs/2301.00073v2
17. `[噪声]` AI Wizards at CheckThat! 2025: Enhancing Transformer-Based Embeddings with Sentiment for Subjectivity Detection in News Articles — http://arxiv.org/abs/2507.11764v1
18. `[噪声]` TDCOSMO 2025: Cosmological constraints from strong lensing time delays — http://arxiv.org/abs/2506.03023v4
19. `[相关]` ALOHA 2: An Enhanced Low-Cost Hardware for Bimanual Teleoperation — http://arxiv.org/abs/2405.02292v1
20. `[噪声]` kilted, adj.¹ — https://doi.org/10.1093/oed/4035658682
21. `[噪声]` Wayward Husbands, Jazzy Jezebels, and Lost Children — https://doi.org/10.1017/9781009566711.008
22. `[相关]` ROS 2: ARCHITECTURE AND PRACTICAL IMPLEMENTATION FEATURES — https://doi.org/10.32782/2663-5941/2025.3.2/22
23. `[相关]` Learning Getting-Up Policies for Real-World Humanoid Robots — http://arxiv.org/abs/2502.12152v2
24. `[相关]` Optimization of Humanoid Robot Designs for Human-Robot Ergonomic Payload Lifting — http://arxiv.org/abs/2211.13503v1
25. `[相关]` Robot Trains Robot: Automatic Real-World Policy Adaptation and Learning for Humanoids — http://arxiv.org/abs/2508.12252v2
26. `[相关]` Certifiably Safe Manipulation of Deformable Linear Objects via Joint Shape and Tension Prediction — http://arxiv.org/abs/2505.13889v1
27. `[相关]` Beyond Binary: Sim-to-Real Dexterous Manipulation with Physics-Grounded Contact Representation — http://arxiv.org/abs/2605.28812v1
28. `[相关]` TDC: Sim-to-Real Transferable Directional Compliance for Contact-Rich Manipulation — http://arxiv.org/abs/2602.14174v2
29. `[相关]` Efficient Sim-to-real Transfer of Contact-Rich Manipulation Skills with Online Admittance Residual Learning — http://arxiv.org/abs/2310.10509v1
30. `[相关]` SARI: Phase-Split Sim-Real Co-Training for Contact-Rich Manipulation — http://arxiv.org/abs/2610.02804v1
31. `[相关]` Learning Contact-Rich Manipulation Skills with Guided Policy Search — http://arxiv.org/abs/1501.05611v2
32. `[噪声]` AIn't Nothing But a Survey? Using Large Language Models for Coding German Open-Ended Survey Responses on Survey Motivation — http://arxiv.org/abs/2506.14634v3

---

*Generated by research-bot · topic=`机器人运动学控制与-ros-2` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`deepseek-v4-flash` · sources=32 · duration=204s · 2026-10-13T22:23:41+00:00*
