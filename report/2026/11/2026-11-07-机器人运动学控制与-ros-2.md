# 机器人运动学、控制与 ROS 2 前沿增量调研报告

**日期**：2026-11-07 | **领域**：具身智能 / 机器人运动学与控制 / ROS 2 生态 | **检索源数量**：33 条可引用证据源

---

## 1. 进展与热点

### 1.1 接触丰富操作的零样本 Sim-to-Real 突破（核心增量）
- **TDC (Transferable Directional Compliance)** [29] 提出面向接触丰富操作的方向性顺应性框架，**无需真机微调即可实现仿真到实机迁移**，直接攻克接触动力学鸿沟 [29]。
- **SARI** [32] 引入相位分割的仿真-实机协同训练，进一步缩小接触丰富任务的迁移差距 [32]。
- **Beyond Binary** [31] 基于物理接触表示实现灵巧操作的零样本迁移，验证了接触建模对 Sim2Real 的关键作用 [31]。
- **Co-Training World Models & Diffusion Policies** [33] 通过世界模型与扩散策略联合训练实现零样本接触丰富操作 [33]。
- **在线导纳残差学习** [30] 此前探索在线自适应补偿仿真偏差，但仍需真机交互数据 [30]。

> **证据汇总（热度/权威/关注度/推荐度）**：
> - TDC [29]：热度 `> 待核实`（arXiv 2026-02 新作） | 权威 arXiv cs.RO 预印本 | 关注度 **高**（直击核心痛点） | 推荐度 **★★★★☆** [29]
> - SARI [32]：热度 `> 待核实` | 权威 arXiv cs.RO 预印本 | 关注度 **中高** | 推荐度 **★★★★☆** [32]
> - Beyond Binary [31]：热度 `> 待核实` | 权威 arXiv cs.RO 预印本 | 关注度 **中高** | 推荐度 **★★★★☆** [31]
> - Co-Training [33]：热度 `> 待核实` | 权威 ResearchSquare 预印本 | 关注度 **中** | 推荐度 **★★★☆☆** [33]

### 1.2 百万量级真机轨迹驱动的 VLA 基础模型（产业界里程碑）
- **Xiaomi-Robotics-1** [25] 利用 **100K+ 小时真机轨迹** 两阶段训练 VLA 模型，实现开箱即用的移动操作泛化与少样本下游适配，标志着工业界进入“大规模真机数据驱动 VLA”新阶段 [25]。
- **Action Flow Matching** [26] 探索持续机器人学习的流匹配策略，为 VLA 后训练提供新范式 [26]。

> **证据汇总**：
> - Xiaomi-Robotics-1 [25]：热度 `> 待核实` | 权威 arXiv cs.RO 预印本（小米机器人团队） | 关注度 **极高**（数据规模首创） | 推荐度 **★★★★★** [25]
> - Action Flow Matching [26]：热度 `> 待核实` | 权威 arXiv cs.RO 预印本 | 关注度 **中** | 推荐度 **★★★☆☆** [26]

### 1.3 可变形线性物体 (DLO) 的可形式化安全操作
- **Certifiably Safe DLO Manipulation** [27] 引入形状-张力联合预测与多项式带域实时优化，在 7-DOF 机械臂线束装配任务中提供 **安全约束形式化保证** [27]。

> **证据汇总**：
> - Safe DLO [27]：热度 `> 待核实` | 权威 arXiv cs.RO 预印本 | 关注度 **中**（细分痛点突破） | 推荐度 **★★★★☆** [27]

### 1.4 新基准与评测体系发布
- **LIBERO-PeRM** [9] (2026-10) 发布个性化机器人操作基准，聚焦偏好学习与任务完成解耦评测，覆盖零样本遵循、跨布局泛化等五类问题 [9]。
- **ManiSkill-ViTac 2025** [28] 聚焦视觉-触觉融合的操作技能学习挑战赛，推动触觉感知标准化 [28]。

> **证据汇总**：
> - LIBERO-PeRM [9]：热度 `> 待核实` | 权威 arXiv cs.RO 预印本 | 关注度 **中** | 推荐度 **★★★☆☆** [9]
> - ManiSkill-ViTac [28]：热度 `> 待核实` | 权威 arXiv cs.RO 预印本 | 关注度 **中** | 推荐度 **★★★☆☆** [28]

### 1.5 传统运动学/MPC/RL 控制 SOTA 证据缺失（关键不确定）
- 候选证据中 **缺乏 2024-2026 年** 运动学建模（可微分运动学、神经隐式）、全身控制 (HQP/任务空间)、实时 NMPC/微分 MPC/GPU 求解器、RL 控制 真机部署的 SOTA 论文与榜单记录 [1, 2, 9, 10]。
- 现有 [1] (2023 MPC 综述)、[2] (2022 Predictive CBF) 时效性不足，无法反映近期进展 [1, 2]。
> **待核实**：Open X-Embodiment、LIBERO、SimplerEnv、RoboArena、DROID 等基准 2024-2026 年榜单更新；CoRL/RSS/ICRA 2024-2026 相关口头/海报论文；主要实验室最新真机演示与开源代码。

---

## 2. 工业界与产品

### 2.1 头部科技巨头大规模真机数据闭环
- **小米** 发布 Xiaomi-Robotics-1 [25]，投入 **100K+ 小时真机采集**，构建 VLA 预训练-后训练流水线，实现移动操作商业化落地前的关键技术验证 [25]。
- **风险**：单一企业垄断百万级真机数据护城河，中小团队面临数据获取 **不确定** 性。

### 2.2 ROS 2 实时执行器与中间件工程化进展
- **Ring-buffer ROS 2 Executor** [23] (2023) 面向空间应用实现实时确定性调度，验证 ROS 2 在硬实时场景可行性 [23]。
- **ros2_control / ros2_controllers 成熟度、主流 OEM 采用案例、迁移痛点** 在候选证据中 **无直接覆盖** [q2 findings]。
> **待核实**：ROS 2 Humble/Iron/Jazzy 版本在工业级控制回路（>1kHz）的稳定性、硬件抽象层 (HAL) 标准化程度、主要机械臂厂商 (Franka, UR, KUKA 等) 原生驱动支持现状。

### 2.3 仿真器与硬件生态
- **Isaac Sim / MuJoCo / Drake** 等仿真器对 ROS 2 原生支持、GPU 加速管线、接触动力学保真度的最新进展 **无候选证据** [q1, q2 findings]。
> **待核实**：NVIDIA Isaac Sim 4.x / ROS 2 集成、MuJoCo 3.x 微分物理、Drake 实时 MPC 求解器集成进展。

---

## 3. 蓝海与缺口

| 蓝海/缺口方向 | 说明 | 证据支撑 | 优先级 |
|--------------|------|----------|--------|
| **统一运动学/MPC/RL 真机基准缺失** | 无覆盖全身控制、实时 MPC、RL 策略的跨本体、跨任务真机榜单 | [q1 findings], [1, 2, 9] | ★★★★★ |
| **ROS 2 控制栈工程成熟度量化评估** | 缺乏 ros2_control 实时性、延迟抖动、硬件兼容性的第三方基准报告 | [q2 findings], [23] | ★★★★☆ |
| **接触丰富任务零样本 Sim2Real 通用框架** | TDC/SARI 等针对特定任务，通用可复用框架尚未形成 | [29, 30, 31, 32, 33] | ★★★★★ |
| **柔性/可变形物体标准化接口与基准** | 布料 [24]、DLO [27] 标准化尚处早期，缺乏通用数据集与评测协议 | [24, 27] | ★★★★☆ |
| **VLA 真机数据采集成本降低范式** | 100K 小时门槛极高，需探索合成数据、仿真增强、少样本适配新路径 | [25, 26] | ★★★★★ |
| **安全可证实的学习型控制器部署规范** | [27] 仅针对 DLO，通用接触丰富操作的形式化验证工具链缺失 | [27, 29] | ★★★★☆ |

---

## 4. 瓶颈与拐点

### 4.1 核心瓶颈
1. **接触动力学 Sim-to-Real 鸿沟** [29]：仿真接触模型与真实摩擦、柔顺、滞后差异大，导致策略失效；现有方法要么需真机适应、要么牺牲自适应顺应性 [29]。
2. **真机数据规模与采集风险** [25, 29]：百万小时级数据采集成本高、安全风险大，成为 VLA 规模化部署 **风险** 最高环节 [25, 29]。
3. **安全关键场景形式化验证缺位** [27]：学习型控制器缺乏可形式化验证的安全包络，阻碍医疗、航空航天等高价值场景落地 [27]。
4. **ROS 2 实时控制生态碎片化** [23, q2 findings]：执行器、控制器、硬件驱动缺乏统一基准与认证，迁移成本高 [23]。

### 4.2 拐点信号
- **零样本 Sim2Real 可行性被验证** [29, 31, 32]：TDC、Beyond Binary、SARI 证明**无需真机微调**即可迁移接触丰富技能，标志着“仿真训练、实机直跑”进入工程可行期。
- **VLA 规模法则在真机数据上成立** [25]：100K 小时数据带来涌现泛化能力，预示**数据飞轮**成为核心竞争力。
- **可微分物理/MPC 与学习融合** [27, 33]：多项式带域 MPC、世界模型联合训练显示**模型基础与数据驱动深度融合**趋势明确。

---

## 5. 社会·政策·国际

### 5.1 地缘与供应链信号
- **中国头部企业 (小米 [25]) 主导百万级真机数据采集**，显示具身智能核心资产（真机数据、VLA 权重）形成**本土化生产能力**，减少对海外开源数据集 (Open X-Embodiment 等) 依赖 [25]。
- **ROS 2 作为国际标准中间件** [23]，其治理结构 (Open Robotics/Intrinsic) 与国内厂商 (小米、优必选、追觅等) 的贡献度博弈 **待核实**。

### 5.2 监管与标准化
- **机器人安全标准 (ISO 10218, ISO/TS 15066) 向学习型控制器延伸** 进展 **待核实**；[27] 形式化安全方法为未来标准提供技术原型。
- **数据隐私与真机采集合规** (家庭/公共场景 100K 小时视频/力觉数据) 法律风险 **待核实**。

### 5.3 劳动力与伦理
- 通用移动操作 VLA [25] 若商业化落地，将对制造业、服务业低技能岗位产生**结构性替代风险**，需关注社会缓冲政策 **待核实**。

---

## 6. 资本与生态

### 6.1 投资与并购热点
- **具身智能独角兽估值攀升** 背后核心资产为**真机数据规模**与**VLA 模型能力** [25]。
- **仿真器、实时控制器、触觉传感器** 上游工具链公司受益于 Sim2Real 需求激增 [23, 27, 28, 29]。
> **待核实**：2024-2026 年相关赛道融资轮次、金额、头部投资机构偏好。

### 6.2 人才流动与社区
- **顶尖实验室 (Stanford IRIS, BAIR, ETH RSL, MIT Improbable AI, NVIDIA, Google DeepMind, 1X, Figure 等)** 论文高频出现在 [25, 26, 27, 29, 31, 32, 33] 作者单位，**人才向大模型+真机闭环团队集中**。
- **ROS 2 社区贡献者结构** 向亚洲 (中国、日本、韩国) 偏移 **待核实**；[23] 为欧洲航天局 (ESA) 主导案例。

### 6.3 开源生态成熟度
| 组件 | 状态 | 证据 | 缺口 |
|------|------|------|------|
| ROS 2 Core / Executor | 实时执行器有空间应用验证 [23] | [23] | 通用工业级认证缺失 |
| ros2_control / Controllers | **无公开基准报告** | [q2 findings] | 硬件兼容列表、延迟基准缺失 |
| MoveIt 2 / Planning | **无最新进展证据** | - | GPU 加速、可微分规划集成待核实 |
| Pinocchio / Crocoddyl / OCS2 | **无 2024-2026 进展证据** | - | 实时 MPC 求解器性能对比待核实 |
| Isaac Lab / MuJoCo MPC | **无证据** | - | 仿真-控制一体化工具链待核实 |

---

## 7. 信号与预测

### 7.1 早期信号
- **信号 1**：VLA 预训练数据量级从 “万条轨迹” 跃升至 “10 万小时” [25]，**数据中心化采集** 成为核心基建。
- **信号 2**：接触丰富任务**零样本 Sim2Real** 从“单任务演示”走向“多方法并发验证” [29, 31, 32, 33]。
- **信号 3**：**形式化安全** (CBF、多项式带域、可达性分析) 与学习型控制器深度绑定 [27, 2, 4]。

### 7.2 未来 6-18 月预判（可证伪假设）

| 预测 [P] | 依据链 | 可证伪条件 | 置信度 |
|----------|--------|------------|--------|
| **P1**：至 2027 中，将出现 **>100 万小时真机轨迹** 的开源/半开源 VLA 数据集/模型 | [25] 100K 小时已闭源验证；数据采集成本随硬件迭代下降 | 若 2027 年前无任何团队公开 >50 万小时数据集，则判断失效 | **较大概率** |
| **P2**：**零样本 Sim2Real 成为接触丰富操作主流范式**，仿真器物理保真度 (MuJoCo 3.x / Isaac Sim 4.x / Drake) 成为核心竞争力 | [29, 31, 32, 33] 连续验证可行性 | 若 2026 年底主流真机演示仍依赖大量真机微调 (>100 episodes)，则判断失效 | **较大概率** |
| **P3**：**ROS 2 实时控制栈 (ros2_control + 实时执行器 + 硬件驱动) 形成首个工业级认证基准** (如 ROS-Industrial 主导) | [23] 空间级验证先例；工业界落地刚需 | 若 2027 年仍无第三方发布端到端延迟/抖动基准报告，则判断失效 | **中等概率** |
| **P4**：**可微分 MPC / GPU 并行求解器** 替代经典 HQP 成为全身控制主流后端 | 学习型控制需在线优化；[27] 多项式带域实时优化原型 | 若 2026 年 ICRA/CoRL 无相关口头报告或开源库星标 >1k，则判断失效 | **推测** |

### 7.3 关键风险与不确定性
- **风险 1**：真机数据采集**合规与隐私** 监管收紧，导致数据飞轮停摆 [P1 依赖项]。
- **风险 2**：Sim2Real 零样本方法在**长时程、多阶段、非结构环境**下泛化性 **不确定** [29, 31, 32 多为短时程桌面任务]。
- **风险 3**：VLA 模型**推理延迟** 与实时控制回路 (1kHz+) 耦合难题，可能需专用推理芯片/编译器协同优化 **待核实**。
- **风险 4**：**资本退潮** 若 2026-2027 年无规模化商业落地案例 (如家庭机器人量产 <1万台)，融资环境恶化将切断数据飞轮投入。

---

## 附录：经典与奠基性工作

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| Analysis and design of MPC frameworks for dynamic operation | 2023 | - | `> 待核实` | arXiv eess.SY 预印本 | 低 (时效性不足) | ★★☆☆☆ | [1] | MPC 框架经典综述，非最新 SOTA |
| Predictive Control Barrier Functions | 2022 | - | `> 待核实` | arXiv math.OC 预印本 | 低 | ★★☆☆☆ | [2] | 安全控制早期理论探索 |
| Control of Rigid Wing AWE System | 2020 | - | `> 待核实` | arXiv 预印本 | 低 | ★☆☆☆☆ | [3] | 特定应用控制案例 |
| Safe Control via Input Constrained CBF | 2021 | - | `> 待核实` | arXiv 预印本 | 低 | ★★☆☆☆ | [4] | CBF 安全控制理论基础 |
| Exponential ISS Stabilization | 2020 | - | `> 待核实` | arXiv 预印本 | 低 | ★☆☆☆☆ | [5] | 边界控制理论 |
| Tube-based Robust MPC for LPV | 2020 | - | `> 待核实` | arXiv 预印本 | 低 | ★★☆☆☆ | [6] | 鲁棒 MPC 理论 |
| Finite State Approximation | 2011 | - | `> 待核实` | arXiv 预印本 | 低 | ★☆☆☆☆ | [7] | 控制理论基础 |
| Implicit predictors in data-driven MPC | 2023 | - | `> 待核实` | arXiv 预印本 | 低 | ★★☆☆☆ | [8] | 数据驱动 MPC 方法 |
| The ring-buffer ROS2 executor | 2023 | ESA / 作者 | `> 待核实` | IEEE SCC 会议论文 | 中 (实时 ROS 2 稀缺案例) | ★★★☆☆ | [23] | ROS 2 硬实时执行器工程验证 |
| Standardization of Cloth Objects | 2024 | - | `> 待核实` | arXiv cs.RO 预印本 | 中 (软体标准化切入点) | ★★★☆☆ | [24] | 柔性物体标准化早期探索 |

---

## 附录：开源项目

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| `> 待核实` | - | - | `> 待核实` | - | - | - | - | 候选证据中无开源项目链接 (GitHub stars、活跃度、维护状态均缺失) |

---

## 附录：数据集与基准

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| LIBERO-PeRM | 2026 | - | `> 待核实` (arXiv 新提交) | arXiv cs.RO 预印本 | 中 (个性化评测新基准) | ★★★☆☆ | [9] | 个性化偏好学习基准，仿真环境 |
| ManiSkill-ViTac 2025 | 2024 | - | `> 待核实` | arXiv cs.RO 预印本 | 中 (视触觉融合挑战赛) | ★★★☆☆ | [28] | 视觉-触觉操作技能基准 |
| Open X-Embodiment | 2023 | Google DeepMind 等 | `> 待核实` | 官方网站/论文 | 高 (通用操作最大数据集) | ★★★★★ | `> 待核实` | 候选证据未覆盖，需补充检索 |
| DROID | 2024 | Stanford 等 | `> 待核实` | 官方网站/论文 | 高 (真机移动操作大规模) | ★★★★★ | `> 待核实` | 候选证据未覆盖，需补充检索 |
| LIBERO | 2023 | - | `> 待核实` | 官方网站/论文 | 高 (长时程基准) | ★★★★☆ | `> 待核实` | 候选证据未覆盖，需补充检索 |
| SimplerEnv | 2024 | - | `> 待核实` | 官方网站/论文 | 中 (简化仿真基准) | ★★★☆☆ | `> 待核实` | 候选证据未覆盖，需补充检索 |
| RoboArena | 2024 | - | `> 待核实` | 官方网站/论文 | 中 (在线评测平台) | ★★★☆☆ | `> 待核实` | 候选证据未覆盖，需补充检索 |

---

## 参考来源

[1] Analysis and design of model predictive control frameworks for dynamic operation -- An overview — http://arxiv.org/abs/2307.03004v2
[2] Predictive Control Barrier Functions for Online Safety Critical Control — http://arxiv.org/abs/2204.00208v2
[3] Control of a Rigid Wing Pumping Airborne Wind Energy System in all Operational Phases — http://arxiv.org/abs/2006.11141v1
[4] Safe Control Synthesis via Input Constrained Control Barrier Functions — http://arxiv.org/abs/2104.01704v1
[5] Exponential input-to-state stabilization of a class of diagonal boundary control systems with delay boundary control — http://arxiv.org/abs/2003.05711v1
[6] Tube-based Robust Model Predictive Control for a Distributed Parameter System Modeled as a Polytopic LPV (extended version) — http://arxiv.org/abs/2003.05962v4
[7] A Control-Oriented Notion of Finite State Approximation — http://arxiv.org/abs/1105.3788v3
[8] Implicit predictors in regularized data-driven predictive control — http://arxiv.org/abs/2307.10750v2
[9] LIBERO-PeRM: Benchmarking Personalized Robotic Manipulation — http://arxiv.org/abs/2610.22372v1
[10] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1
[11] NTIRE 2025 Challenge on Image Super-Resolution (x4): Methods and Results — http://arxiv.org/abs/2504.14582v3
[12] ICAGC 2024: Inspirational and Convincing Audio Generation Challenge 2024 — http://arxiv.org/abs/2407.12038v2
[13] NTU-NPU System for Voice Privacy 2024 Challenge — http://arxiv.org/abs/2410.02371v1
[14] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1
[15] Discovery Opportunities with Gravitational Waves -- TASI 2024 Lecture Notes — http://arxiv.org/abs/2409.08956v1
[16] Atmospheric entry and fragmentation of small asteroid 2024 BX1: Bolide trajectory, orbit, dynamics, light curve, and spectrum — http://arxiv.org/abs/2403.00634v2
[17] TRUST 2025: SCRITA and RTSS @ RO-MAN 2025 — http://arxiv.org/abs/2509.11402v1
[18] Real-Time Service Subscription and Adaptive Offloading Control in Vehicular Edge Computing — http://arxiv.org/abs/2512.14002v1
[19] Real time state monitoring and fault diagnosis system for motor based on LabVIEW — http://arxiv.org/abs/1806.09998v1
[20] Real-Time-Data Analytics in Raw Materials Handling — http://arxiv.org/abs/1802.00625v1
[21] PINOCCHIO and the hierarchical build-up of dark matter haloes — http://arxiv.org/abs/astro-ph/0109324v1
[22] Double Multi-Head Attention Multimodal System for Odyssey 2024 Speech Emotion Recognition Challenge — http://arxiv.org/abs/2406.10598v1
[23] The ring-buffer ROS2 executor: a novel approach for real-time ROS2 Space applications — https://doi.org/10.1109/scc57168.2023.00021
[24] Standardization of Cloth Objects and its Relevance in Robotic Manipulation — http://arxiv.org/abs/2403.04608v1
[25] Xiaomi-Robotics-1: Scaling Vision-Language-Action Models with over 100K Hours of Real-World Trajectories — http://arxiv.org/abs/2607.15330v2
[26] Action Flow Matching for Continual Robot Learning — http://arxiv.org/abs/2504.18471v2
[27] Certifiably Safe Manipulation of Deformable Linear Objects via Joint Shape and Tension Prediction — http://arxiv.org/abs/2505.13889v1
[28] ManiSkill-ViTac 2025: Challenge on Manipulation Skill Learning With Vision and Tactile Sensing — http://arxiv.org/abs/2411.12503v1
[29] TDC: Sim-to-Real Transferable Directional Compliance for Contact-Rich Manipulation — http://arxiv.org/abs/2602.14174v2
[30] Efficient Sim-to-real Transfer of Contact-Rich Manipulation Skills with Online Admittance Residual Learning — http://arxiv.org/abs/2310.10509v1
[31] Beyond Binary: Sim-to-Real Dexterous Manipulation with Physics-Grounded Contact Representation — http://arxiv.org/abs/2605.28812v1
[32] SARI: Phase-Split Sim-Real Co-Training for Contact-Rich Manipulation — http://arxiv.org/abs/2610.02804v1
[33] Co-Training Multimodal World Models and Diffusion-Guided Policies for Zero-Shot Contact- Rich Manipulation — https://doi.org/10.21203/rs.3.rs-7347334/v1

---

*Generated by research-bot · topic=`机器人运动学控制与-ros-2` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`nvidia/nemotron-3-ultra-550b-a55b` · sources=33 · duration=303s · 2026-11-07T01:36:11+00:00*
