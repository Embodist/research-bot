# 机器人运动学、控制与 ROS 2：最近 1–2 年增量快照

**报告日期**：2026-10-10（UTC）  
**领域**：机器人运动学（kinematics）、控制（LQR / MPC / 全身控制 WBC）、ROS 2 工程栈与评测基准  
**检索源数量**：本批可引用候选来源 27 条（编号 [1]–[27]），覆盖 3 个子问题（q1 前沿增量 / q2 开源工程栈与基准 / q3 争议·产业·政策·资本）  
**证据基线声明（必读）**：本批候选证据对「机器人运动学 / 控制 / ROS 2」主线**覆盖极不完整**。27 条中与主线直接相关的仅约 10 条，且集中在运动规划工程工具、人形全身控制、机械臂自适应控制与运动学教材章节；**候选块未提供任何 citations / GitHub stars / 榜单排名字段**，因此下文所有「热度证据」一律标注 `> 待核实`，不做任何数字推定。凡本批证据无法支撑的判断，均显式写为缺口而非结论。

---

## 1. 进展与热点（Progress & Hotspots）

**一句话增量判断**：本批证据中可核查的近期增量只出现在**两条支线**——人形全身控制（whole-body control, WBC）的 RL / 扩散策略路线 [20][21][23]，以及带状态约束的控制理论（control barrier functions, CBF）[14]；**相对 DH/雅可比/IK 解析数值解、LQR/MPC 控制器设计、ROS 1→ROS 2 架构迁移这三条主线，本批证据未提供任何可核查增量**。

**近 1–2 年（2024–2026）可核查进展**

| 条目 | 时间 | 相对经典基线的增量 | 证据强度 |
|---|---|---|---|
| 人形全身羽毛球（annealed RL curriculum）[21] | 2025-11（v1，arXiv:2511.11218，v4 修订时间 `> 待核实`） | 把 WBC 从「静态场景 locomotion/manipulation」推向**高速动态物体交互**，用退火 RL 课程训练统一全身策略；摘要自述动态真实交互仍是难点 [21] | arXiv cs.RO 预印本，**未见同行评审 venue**；无引用/star 数据 `> 待核实` |
| 域随机化对扩散策略训练全身人形控制的作用 [20] | 2024-11（arXiv:2411.01349v1） | 把 **domain randomization** 这一仿真-真机迁移手段系统性引入 diffusion policy × WBC 组合 | arXiv 预印本；venue `> 待核实` |
| CHILD：全身人形遥操作（imitation + live demonstration）[23] | 2025-08（arXiv:2508.00162v2） | 全身 WBC 与示教/遥操作链路的耦合，属「WBC + 数据采集」交叉 | arXiv 预印本；venue `> 待核实` |
| CBF 状态约束下的反馈优化 [14] | 2025-04（arXiv:2504.00813v3） | 在**安全约束控制**方向上把 CBF 与 feedback optimization 结合，属控制理论层而非机器人专属 | arXiv 预印本；venue `> 待核实` |

**相对经典基线的「没有增量」清单（同样重要）**
- **运动学求解**：DH 参数、雅可比、解析 IK / 数值 IK 的基线见教材级文献 [22]；本批证据中**无任何** 2024–2026 年对其的替代或改进工作 → 增量缺失 `> 待核实`。
- **LQR / MPC**：本批证据中未见任何 LQR/MPC 新方法、新基准或真机对比；近期控制侧证据只有 CBF [14] 与 RL 路线 [20][21] → 缺口 `> 待核实`。
- **ROS 1 → ROS 2 迁移**：本批唯一 ROS 相关文献 [24] 是 2018 年 ROS 1 时代的人形平台软件框架，**不含任何 ROS 2 量化迁移证据**（DDS 中间件、executor、实时性、`ros2_control`）→ 缺口 `> 待核实`。

### 1.1 经典与奠基性工作（表格）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Mobile Robot Kinematics（教材章节）[22] | `> 待核实` | `> 待核实` | `> 待核实` | DOI 正式出版物（Elsevier 书章，DOI:10.1016/b978-0-12-417049-0.00002-x），非预印本 | 低–中：无引用/下载数据可依 [22] | ★★★★☆ 运动学基线的必读起点，DH/雅可比/轮式非完整约束的规范表述 | [22] | 本批唯一「正式出版」的运动学基础文献 |
| Adaptive Control of Robot Manipulators With Uncertain Kinematics and Dynamics [15] | 2014-03（arXiv:1403.5204v3） | `> 待核实` | `> 待核实` | arXiv 预印本，venue `> 待核实` | 低–中：候选块无引用数据 [15] | ★★★★☆ **同时处理运动学与动力学不确定性**，正是「运动学×控制」交叉的经典锚点 | [15] | 用于界定「不确定运动学下的控制」基线 |
| Quantum control theory and applications: A survey [16] | 2009-10（arXiv:0910.2350v3） | `> 待核实` | `> 待核实` | arXiv 综述预印本 | 低（对本主题）：术语「control」跨领域噪声 [16] | ★☆☆☆☆ 与机器人控制无关，仅作检索噪声记录 | [16] | 说明 “control” 检索词的歧义 |

### 1.2 数据集与基准（表格）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Local Planner Bench（局部运动规划基准）[9] | 2022-10（arXiv:2210.06033v1） | `> 待核实` | `> 待核实` | arXiv 预印本，venue `> 待核实` | 低–中：无榜单排名/引用数据 [9] | ★★★☆☆ 局部运动规划可比评测的少见显式 benchmark，值得核查其任务口径 | [9] | 与运动规划控制链路的「可复现评测」直接相关 |
| Evaluating Guiding Spaces for Motion Planning [11] | 2022-10（arXiv:2210.08640v1） | `> 待核实` | `> 待核实` | arXiv 预印本 | 低–中 [11] | ★★☆☆☆ 关注采样/引导空间评估方法学，非 SOTA 榜单 | [11] | 规划器评测方法论 |
| Data-Efficient Learning of High-Quality Controls for Kinodynamic Planning（车载导航）[12] | 2022-01（arXiv:2201.02254v1） | `> 待核实` | `> 待核实` | arXiv 预印本 | 低–中 [12] | ★★☆☆☆ kinodynamic 规划中的控制学习，跨到车载域，相关但非机械臂/人形 | [12] | 与「规划—控制」接口相关 |
| LIBERO / SimplerEnv / RoboArena / Open X-Embodiment / DROID | — | — | `> 待核实` | — | — | — | — | **在本批 27 条证据中出现次数为 0**，其任务规模、评测口径、榜单状态均 `> 待核实` |

**检索噪声与术语歧义（可核查观察）**：本批证据被三类跨领域关键词污染——(a) “control” → 量子控制综述 [16]；(b) “DDS” → DPU 分离式存储（disaggregated storage）[25]，**与 Data Distribution Service 中间件同名异义**；(c) “real-time” → 车载边缘卸载 [4]、TSN 时延协商 [27]、DDR 内存时延 [26]、电流环电机监测 [5]。这解释了为何 ROS 2 / DDS 相关召回质量低。

---

## 2. 工业界与产品（Industry & Product）

**一句话增量判断**：本批证据**不含任何厂商官方博客、产品发布、技术报告或量产部署证据**，产业维度的可核查增量 = 0，全部 `> 待核实`。

### 2.1 开源项目与工程栈（表格）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Robowflex: Robot Motion Planning with MoveIt Made Easy [10] | 2021-03（arXiv:2103.12826v2） | `> 待核实` | `> 待核实`（stars 未在候选块提供） | arXiv 预印本；面向 MoveIt 生态的官方式工程封装 | 中：本批唯一直接挂靠 MoveIt 的工程工具 [10] | ★★★☆☆ 与 MoveIt 工程实践直接相关；但**是否兼容 MoveIt 2 / ROS 2 `> 待核实`** | [10] | 本批最能代表「运动规划工程栈」的条目 |
| A ROS-based Software Framework for the NimbRo-OP Humanoid Open Platform [24] | 2018-09（arXiv:1809.11051v1） | `> 待核实` | `> 待核实` | arXiv 预印本；属 **ROS 1 时代**人形平台框架 | 低（对 2024–2026 前沿）：时间距今约 8 年 [24] | ★★☆☆☆ 具历史基线价值，可用于论证「ROS 1→ROS 2 迁移缺证据」 | [24] | 唯一 ROS 平台框架证据，且非 ROS 2 |
| `ros2_control` / MoveIt 2 / Pinocchio / Drake / MuJoCo / Crocoddyl / Fast DDS / Cyclone DDS / Zenoh / PREEMPT_RT | — | — | `> 待核实` | — | — | — | — | **在本批 27 条证据中出现次数为 0**：可用性、维护状态、实时实测均 `> 待核实` |

**工业界与工程落地**
- 本批无任何「lab → 落地」的直接证据（无厂商发布、无量产、无真机部署报告）`> 待核实`。
- 唯一可间接观察的生态信号是：本批的工程类文献时间戳集中在 2018 [24] 与 2021–2022 [9][10][11][12]，**近 1–2 年的工程栈条目缺失**，这一「时间断档」本身是检索覆盖问题，而非产业停滞的判断依据 `> 待核实`。

---

## 3. 蓝海与缺口（Blue Ocean & Gaps）

**一句话增量判断**：本批证据反向暴露出的**最大蓝海是「可核查的 ROS 2 实时性与运动学/控制评测基础设施」**——文献侧多、证据侧空。

**可核查的无人区/缺口**
- **可微 / 学习式运动学求解**：本批 2024–2026 证据零覆盖 [1][17][18][19]；经典基线仅 [22] → 缺口 `> 待核实`。
- **WBC 与抓取的统一**：仅有全身动态交互的 RL 尝试 [21] 与遥操作 [23]，**无统一「移动 + 操作 + 抓取」的基准或可比口径** `> 待核实`。
- **ROS 2 实时确定性 / DDS 开销的实测证据**：本批仅有跨领域实时性文献 [4][26][27] 可作类比，**无一条针对 ROS 2 中间件** → 高杠杆缺口 `> 待核实`。
- **仿真到真机鸿沟的量化**：唯一相关线索是域随机化 × 扩散策略 [20]，但**无仿真 SOTA 与真机 SOTA 的对照数字** `> 待核实`。
- **评测不可比**：本批基准类证据仅 [9][11] 两条（2022 年），且无排行榜/第三方复现数据 `> 待核实`。

**[P] 预测（低–中置信）**：若到 **2027-06** 前，公开可检索的「ROS 2 中间件（≥2 种 DDS 实现）× PREEMPT_RT × 真机」第三方实测报告仍少于 3 篇，则「ROS 2 实时性评测是蓝海缺口」的判断成立。依据链：工程栈文献时间断档（2018/2021–2022）→ 本批零 ROS 2 实测 → 推演为缺口；不确定性：本批检索召回质量差，可能低估实际文献量。

---

## 4. 瓶颈与拐点（Bottleneck & Inflection）

**一句话增量判断**：可识别的瓶颈有三个——**评测与数据瓶颈、实时性实证瓶颈、检索/术语瓶颈**；拐点信号目前**只有「人形全身控制从静态走向高速动态交互」**一条，且证据等级偏低（预印本、无独立复现）。

| 瓶颈 | 本批证据 | 是否临近拐点 |
|---|---|---|
| 数据与评测不可比 | 基准仅 [9][11]（2022），LIBERO/SimplerEnv/RoboArena/OX-Embodiment/DROID 覆盖为 0 | 未知 `> 待核实` |
| 实时确定性与中间件开销 | 无 ROS 2 证据；仅有跨领域实时文献 [4][26][27]（车载卸载、TSN、DDR 时延） | 未知 `> 待核实` |
| 仿真到真机 | 仅 [20] 域随机化 × 扩散策略一条线索 | 推测：正在从「随机化调参」转向「策略级鲁棒性」，证据不足 `> 待核实` |
| 检索与术语歧义 | “control” → [16]；“DDS” → [25]；“real-time” → [4][26][27] | 已确证（可由候选块标题直接核查） |

**拐点信号（低置信）**
- 人形全身策略从静态交互转向**高速动态物体交互**（羽毛球）[21]，若被独立复现或中稿顶会，可视为 WBC 路线的拐点；当前仅为预印本，**无第三方复现** `> 待核实`。
- CBF 从纯理论走向与反馈优化的结合 [14]，可能预示「约束控制进入通用优化框架」，但无机器人真机验证 `> 待核实`。

---

## 5. 社会·政策·国际（Society, Policy & Geopolitics）

**一句话增量判断**：本批证据对机器人专属监管标准（ISO 10218 / ISO-TS 15066 / EU AI Act）**零覆盖**；唯一可核查的社会/治理增量来自 AI 基础模型透明度治理 [3]，可作 VLA 基础模型数据披露议题的旁证。

| 条目 | 时间 | 增量内容 | 四类证据 |
|---|---|---|---|
| 2025 Foundation Model Transparency Index（FMTI 第三版）[3] | 2025-12（arXiv:2512.10169v1） | 新增「数据获取 / 用量数据 / 监测」指标，**首次评估 Alibaba、DeepSeek、xAI**；**平均分由 2024 年 58 降至 2025 年 40（满分 100）**，训练数据与训练算力最不透明 [3] | 热度：`> 待核实`（无引用数）；权威：arXiv cs.AI 预印本，署名含 Percy Liang、Rishi Bommasani 等（据候选块元数据），**同行评审 status `> 待核实`**；关注度：中（AI 治理话题的年度性公开指标）；推荐度：★★☆☆☆（与运动学/控制主线无关，仅作 VLA 数据披露的旁证） |
| ISO 10218 / ISO-TS 15066 / EU AI Act 及其对机器人部署的影响 | — | 本批证据**零覆盖**，无法给出任何可核查增量 | 全部 `> 待核实` |
| 供应链、地缘政治对 ROS 2 生态的影响 | — | 本批证据**零覆盖** | `> 待核实` |

**说明**：FMTI 的分数下降（58 → 40）是**基础模型开发者透明度**的指标，不等于机器人行业监管强度变化，二者不可混用 [3]。机器人功能安全标准（ISO 系列）与 EU AI Act 在机器人本体上的生效/合规细节，本批无来源支撑 → `> 待核实`。

---

## 6. 资本与生态（Capital & Ecosystem）

**一句话增量判断**：本批证据对融资、并购、人才流动、公司格局**零覆盖**，资本维度无法给出任何可核查增量；生态侧只能从开源工具的时间分布间接观察。

- **融资 / 并购 / 人才流动**：本批 27 条证据中无一条涉及 → 全部 `> 待核实`。
- **社区与生态结构（间接观察）**：与本主题相关的工程条目时间戳集中在 2018 [24] 与 2021–2022 [9][10][11][12]，2024–2026 的工程栈条目在本批中缺失 → 这**只说明召回不足**，不能推断生态萎缩 `> 待核实`。
- **学术社区动态**：本批唯一的社区组织性文献是 RO-MAN 2025 的 HRI 信任联合工作坊（SCRITA + RTSS）[19]，属 HRI 子社区，与运动学/控制/ROS 2 无实质交集。热度：`> 待核实`；权威：arXiv:2509.11402v1，**workshop overview，非同行评审研究论文**；关注度：低（议题局限于 HRI 信任子社区）；推荐度：★☆☆☆☆（可略过）。
- **VLA/基础模型生态的资本侧面**：仅能借 [3] 的透明度指标间接观察开发者披露行为，**不构成资本流动证据** `> 待核实`。

---

## 7. 信号与预测（Signals & Forecast）

**一句话增量判断**：本批证据能支撑的「信号」只有两条（人形全身动态控制 [21]、约束控制理论化 [14]），其余维度信号缺失；预测全部写成可证伪假设。

**已确证信号**
1. 人形全身控制的近期工作方向从「静态场景」转向「动态真实交互」[21]，同方向有域随机化 × 扩散策略 [20] 与遥操作 [23] 支撑。
2. 安全约束控制以 CBF 形式继续理论化并与优化框架结合 [14]。
3. **检索层面已确证**：`control` / `DDS` / `real-time` 三个词在本批召回中造成大量跨领域噪声 [16][25][4][26][27]，后续检索必须显式消歧。

**[P] 预测（可证伪假设）**

| 假设 | 依据链 | 置信度 | 证伪条件 |
|---|---|---|---|
| **[P1]** 到 2027-06，ROS 2 实时性（DDS 实现对比 + PREEMPT_RT + 真机）第三方实测报告仍是稀缺资源（< 3 篇公开可检索） | 本批 ROS 2 实测证据为 0 [24] 为 ROS 1 时代 → 推演工程侧评测供给不足 | 低–中 | 若届时出现 ≥3 篇公开第三方基准，则假设被推翻 |
| **[P2]** 人形全身动态控制（[21] 路线）在 2026–2027 会被独立复现或进入顶会正刊 | 该路线 2025-11 起有 [20][21][23] 多条同向工作聚集 → 方向活跃 | 中 | 若 2027-12 前无同行评审版本、无开源复现，则假设被推翻 |
| **[P3]** 「运动学求解（可微/学习式 IK）」相对经典解析/数值解 [22] 的增量，在补检后会被证实**少于**控制与规划侧的增量 | 本批 2024–2026 证据在运动学侧完全空白 [1][17][18][19] | 未知（需数据） | 补充检索后若运动学侧出现多条 SOTA 级工作，则假设被推翻 |

**传闻与争议**
- 本批无标记为 `[R]` 的可报传闻（无社区帖子、无泄露信息类来源）。
- `[Debated]`：无本批来源支撑的实质性争议并列陈述 → `> 待核实`。

**Watchlist（需持续关注，本批均无证据）**
1. `ros2_control` 与 MoveIt 2 的 ROS 2 发行版配套状态与真机实测。
2. 人形 WBC 的仿真 SOTA vs 真机 SOTA 对照口径 [20][21]。
3. 运动规划/操作基准（[9][11] 之外）的榜单与第三方复现。
4. ISO 10218 / ISO-TS 15066 / EU AI Act 在机器人本体上的落地细节。
5. 基础模型数据透明度对 VLA 数据集披露的外溢效应 [3]。

---

## 参考来源

[1] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1  
[2] NTIRE 2025 Challenge on Image Super-Resolution (x4): Methods and Results — http://arxiv.org/abs/2504.14582v3  
[3] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1  
[4] Real-Time Service Subscription and Adaptive Offloading Control in Vehicular Edge Computing — http://arxiv.org/abs/2512.14002v1  
[5] Real time state monitoring and fault diagnosis system for motor based on LabVIEW — http://arxiv.org/abs/1806.09998v1  
[6] Real-Time-Data Analytics in Raw Materials Handling — http://arxiv.org/abs/1802.00625v1  
[7] Toward Real-Time Image Annotation Using Marginalized Coupled Dictionary Learning — http://arxiv.org/abs/2304.06907v2  
[8] Alchymical Mirror: Real-time Interactive Sound- and Simple Motion-Tracking Set of Jitter/Max/MSP Patches — http://arxiv.org/abs/1101.2219v1  
[9] Local Planner Bench: Benchmarking for Local Motion Planning — http://arxiv.org/abs/2210.06033v1  
[10] Robowflex: Robot Motion Planning with MoveIt Made Easy — http://arxiv.org/abs/2103.12826v2  
[11] Evaluating Guiding Spaces for Motion Planning — http://arxiv.org/abs/2210.08640v1  
[12] Data-Efficient Learning of High-Quality Controls for Kinodynamic Planning used in Vehicular Navigation — http://arxiv.org/abs/2201.02254v1  
[13] A Human-Vector Susceptible-Infected-Susceptible Model for Analyzing and Controlling the Spread of Vector-Borne Diseases — http://arxiv.org/abs/2510.14787v2  
[14] Feedback Optimization with State Constraints through Control Barrier Functions — http://arxiv.org/abs/2504.00813v3  
[15] Adaptive Control of Robot Manipulators With Uncertain Kinematics and Dynamics — http://arxiv.org/abs/1403.5204v3  
[16] Quantum control theory and applications: A survey — http://arxiv.org/abs/0910.2350v3  
[17] TDCOSMO 2025: Cosmological constraints from strong lensing time delays — http://arxiv.org/abs/2506.03023v4  
[18] LLM-based ambiguity detection in natural language instructions for collaborative surgical robots — http://arxiv.org/abs/2507.11525v1  
[19] TRUST 2025: SCRITA and RTSS @ RO-MAN 2025 — http://arxiv.org/abs/2509.11402v1  
[20] The Role of Domain Randomization in Training Diffusion Policies for Whole-Body Humanoid Control — http://arxiv.org/abs/2411.01349v1  
[21] Humanoid Whole-Body Badminton via an Annealed Reinforcement Learning Curriculum — http://arxiv.org/abs/2511.11218v4  
[22] Mobile Robot Kinematics — https://doi.org/10.1016/b978-0-12-417049-0.00002-x  
[23] CHILD (Controller for Humanoid Imitation and Live Demonstration): a Whole-Body Humanoid Teleoperation System — http://arxiv.org/abs/2508.00162v2  
[24] A ROS-based Software Framework for the NimbRo-OP Humanoid Open Platform — http://arxiv.org/abs/1809.11051v1  
[25] DDS: DPU-optimized Disaggregated Storage [Extended Report] — http://arxiv.org/abs/2407.13618v5  
[26] On the Off-chip Memory Latency of Real-Time Systems: Is DDR DRAM Really the Best Option? — http://arxiv.org/abs/1810.07059v1  
[27] Negotiating strict latency limits for dynamic real-time services in vehicular time-sensitive networks — http://arxiv.org/abs/2504.05793v3

---

*Generated by research-bot · topic=`机器人运动学控制与-ros-2` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`deepseek-v4-flash` · sources=27 · duration=148s · 2026-10-10T22:10:16+00:00*
