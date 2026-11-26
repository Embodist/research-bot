# 机器人运动学、控制与 ROS 2 生态：2024-2026 增量快照报告

**日期**：2026-11-26（UTC）  
**领域**：具身智能 / 机器人运动学 / 控制算法 / ROS 2 生态  
**检索源数量**：36 条可引用证据（含论文、预印本、竞赛报告、书籍章节、会议论文）

---

## 1. 进展与热点

### 1.1 最新前沿进展（2024-2026）

| 进展 | 时间 | 机构/来源 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 说明 |
|------|------|-----------|----------|----------|--------|--------|------|
| 基于 Dynamixel 舵机的六足机器人 Web 级关节控制桥接系统，集成 ROS、逆运动学与强化学习，面向树莓派部署 | 2026 | SSRN 预印本 [1] | citations=0（预印本） | SSRN 预印本，非同行评审 | 低 | ★★☆☆☆ | 工程实践参考价值，展示低成本六足平台 ROS 集成、关节级控制、IK 与 RL 融合完整系统 [1] |
| 面向真实世界通用策略的仿真基准设计三原则：高视觉保真仿真、系统性增加任务复杂度与场景扰动、量化真实性能与仿真对应性的对齐度 | 2025 | RSS 2025 Workshop [2] | 新发布，引用数待积累 | RSS 顶会工作坊论文 | 高 | ★★★★★ | 直接切中基准体系核心缺口，提出的三条原则可作为后续基准建设指导框架 [2] |
| ROS 2 实时执行器优化：基于环形缓冲区的执行器设计，面向空间应用的硬实时 ROS 2 | 2023 | IEEE SCC 会议 [3] | 会议论文，引用数待核实 | IEEE 会议同行评审 | 中 | ★★★★☆ | 解决 ROS 2 执行器确定性延迟问题，为硬实时控制提供工程可落地方案 [3] |
| 分布式实时 ROS 2 控制架构：面向多机协同的实时能力 ROS 2 设计 | 2022 | IEEE CASE 会议 [4] | 会议论文，引用数待核实 | IEEE 会议同行评审 | 中 | ★★★☆☆ | 探讨 DDS QoS 与实时调度在分布式控制中的配置最佳实践 [4] |
| 基于 ROS 的因果分析框架（ROS-Causal）：用于人机交互应用的因果推断集成 | 2024 | arXiv 预印本 [5] | arXiv 预印本，引用数待核实 | arXiv (cs.RO) | 中 | ★★★☆☆ | 将因果推断引入 ROS 生态，为可解释性人机交互提供工程框架 [5] |

> 待核实：2024-2026 年 MoveIt 2、ros2_control、Nav2、Isaac ROS 等新一代框架的基准测试与性能对比数据在候选证据中缺失，需补充官方文档与社区基准报告。

### 1.2 经典奠基性工作（基准参考）

| 名称 | 年份 | 机构/作者 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|----------|----------|--------|--------|------|------|
| Safe Control Synthesis via Input Constrained Control Barrier Functions (ICCBF) | 2021 | arXiv / CDC 2021 [6] | 被安全控制文献引用，具体引用数待核实 | arXiv 预印本，提交 CDC 2021（顶会） | 中 | ★★★★☆ | [6] | 将安全控制转化为实时可解 QP，适用于非均匀相对度系统，具身智能安全运动规划理论基石 |
| Adaptive Control of Robot Manipulators With Uncertain Kinematics and Dynamics | 2014 | arXiv (eess.SY) [7] | 经典控制理论文献，引用数待核实 | arXiv 预印本，非同行评审 | 中 | ★★★☆☆ | [7] | 运动学与动力学双重不确定性下的自适应控制理论基础 |
| A Real-Time Model-Based Reinforcement Learning Architecture for Robot Control | 2011 | arXiv (cs.AI) [8] | 早期工作，现代范式下关注度低 | arXiv 预印本 | 低 | ★★☆☆☆ | [8] | 实时模型基 RL 早期探索，历史脉络参考 |
| Robot Arm Kinematics (书籍章节) | 2017 | CRC Press [9] | 教材章节，引用数待核实 | 学术专著章节 | 中 | ★★★☆☆ | [9] | 机械臂运动学系统性教材参考 |
| A Concise Bézier Clipping Technique for Solving Inverse Kinematics Problems | 2013 | Springer [10] | 算法论文，引用数待核实 | 学术会议/书籍章节 | 中 | ★★★☆☆ | [10] | 贝塞尔剪枝求解逆运动学的数值方法 |
| Structure Design and Kinematics Analysis and Experiment of Rope-driven Continuum Robot | 2024 | IEEE CCDC 会议 [11] | 2024 年会议论文，引用数待核实 | IEEE 会议同行评审 | 中 | ★★★☆☆ | [11] | 绳驱连续体机器人运动学建模与实验验证 |

---

## 2. 工业界与产品

### 2.1 真机部署与商业化进展

| 产品/项目 | 时间 | 机构/厂商 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 说明 |
|-----------|------|-----------|----------|----------|--------|--------|------|
| Real Robot Challenge (RRC) — 基于 TriFinger 平台的灵巧操作真机竞赛基准 | 2021 | 官方竞赛组织方 [12] | 竞赛已结束，历史基准 | 官方竞赛报告，arXiv 预印本 | 中 | ★★★☆☆ | 首个真实 TriFinger 平台灵巧操作竞赛，提供真机评测基础设施参考，但任务限于矩形物体、平台单一 [12] |
| ROS 2 实时控制在工业机器人中的应用案例（分布式实时架构） | 2022 | IEEE CASE [4] | 会议论文，工程落地案例 | IEEE 会议同行评审 | 中 | ★★★☆☆ | 展示 ROS 2 在分布式实时控制场景的工程配置最佳实践 [4] |
| 空间级硬实时 ROS 2 执行器（环形缓冲区设计） | 2023 | IEEE SCC [3] | 会议论文，航天级验证 | IEEE 会议同行评审 | 中 | ★★★★☆ | 面向空间应用的硬实时 ROS 2 执行器，工程成熟度高 [3] |

> 待核实：主流人形机器人厂商（如 Figure, Tesla, Unitree, Fourier 等）在 ROS 2 Humble/Iron/Jazzy 上的运动学/控制栈开源项目实证、真机部署规模与性能指标在候选证据中缺失。

### 2.2 开源核心项目生态（社区维护状态）

| 项目 | 维护机构 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 说明 |
|------|----------|----------|----------|--------|--------|------|
| ros2_control | ROS 2 Controls 社区 | GitHub stars/活跃度待核实 | 官方 ROS 2 核心框架，文档完善 | 高 | ★★★★★ | 统一硬件抽象层，控制器管理器，实时控制核心 [待核实] |
| MoveIt 2 | PickNik / MoveIt 社区 | GitHub stars/活跃度待核实 | 官方运动规划框架，ROS 2 原生 | 高 | ★★★★★ | 运动规划、运动学求解、碰撞检测、Servo 实时伺服 [待核实] |
| Nav2 | Open Robotics / 社区 | GitHub stars/活跃度待核实 | ROS 2 官方导航框架 | 高 | ★★★★★ | 行为树导航、成本地图、控制器插件化 [待核实] |
| Isaac ROS | NVIDIA | GitHub stars/活跃度待核实 | NVIDIA 官方维护，GPU 加速感知/规划 | 高 | ★★★★☆ | CUDA 加速图像处理、深度感知、运动规划 [待核实] |
| Pinocchio | INRIA / Stack-of-Tasks | GitHub stars/活跃度待核实 | C++ 高性能刚体动力学库，头文件-only | 高 | ★★★★★ | 前向/逆运动学、动力学导数、自动微分，广泛用于实时控制 [待核实] |

> 待核实：上述开源项目的具体 GitHub stars、最近提交频率、Issue 解决率、ROS 2 版本兼容性矩阵需实时查证。

---

## 3. 蓝海与缺口

### 3.1 基准体系与评测缺口

| 缺口 | 证据来源 | 严重程度 | 说明 |
|------|----------|----------|------|
| 缺乏面向通用策略的标准化 sim-to-real 评测协议：无法在仿真中系统性量化鲁棒性并预测真实性能 | [2] | 高 | RSS 2025 Workshop 明确指出评测通用策略的真实应用滞后，提出三大设计原则但尚无标准化协议落地 [2] |
| 基准体系碎片化：无覆盖多本体（机械臂/灵巧手/移动/人形）、多任务、真实部署的统一榜单 | [2], [12], [13] | 高 | 跨越 8 年三篇工作共同指向同一结构性缺口：RRC 单一平台 [12]、单任务导航 [13]、通用策略评测滞后 [2] |
| 高视觉保真仿真与真实世界的性能对齐度量缺失：缺乏公认的 sim-to-real gap 定量指标 | [2] | 高 | 论文 [2] 提出需量化真实与仿真性能对齐度，但现有体系缺失此类标准化度量 |
| 真实世界长尾分布与安全关键场景的基准覆盖不足：现有基准多为常规任务，罕见边缘案例 | [2] | 中 | 评测体系缺乏对分布外泛化、安全关键边界条件的系统性覆盖 |
| 数据集与基准的持续维护机制缺失：竞赛结束即停止更新，缺乏社区驱动的长期演进机制 | [12] | 中 | RRC 竞赛已结束 [12]，典型“一次性基准”问题 |

### 3.2 运动学与控制工程落地缺口

| 缺口 | 证据来源 | 严重程度 | 说明 |
|------|----------|----------|------|
| ROS 2 生态中实时运动学/动力学求解器（Pinocchio、KDL、MoveIt Servo）在硬实时内核上的确定性延迟基准缺乏统一评测 | [4], [3] | 高 | 实时 ROS 2 工作组方案存在 [4][3]，但求解器层面的延迟抖动分布、最坏情况执行时间（WCET）缺乏横向对比 |
| 基于控制屏障函数（CBF/ICCBF）的安全层在 ros2_control 框架下的标准化集成方案尚未形成社区共识 | [6] | 高 | ICCBF 理论成熟 [6]，但 ros2_control 中 HardwareInterface / ControllerInterface 标准化安全层插件缺失 |
| 从仿真到真机的 Sim2Real 迁移中，运动学标定误差、动力学参数辨识、实时通信抖动对 VLA 策略部署的定量影响缺乏系统性基准 | [2] | 高 | 论文 [2] 指出量化真实性能与仿真对应性的对齐度缺失，直接影响 VLA 部署风险评估 |
| ROS 2 中 DDS QoS 策略与实时调度器在多机协同、灵巧手控制等高频场景下的工程最佳实践文档不足 | [4], [3] | 中 | 会议论文 [4][3] 提供点状案例，缺乏系统性配置指南与压测数据 |

> 待核实：VLA（Vision-Language-Action）模型在 ROS 2 实时控制回路中的推理延迟分布、动作分块与实时插值的工程方案对比。

---

## 4. 瓶颈与拐点

### 4.1 核心技术瓶颈

| 瓶颈 | 证据来源 | 瓶颈性质 | 拐点信号 | 说明 |
|------|----------|----------|----------|------|
| **实时性与确定性**：ROS 2 在非实时内核上难以满足高频控制（>1kHz）确定性延迟需求 | [4], [3] | 工程/系统级 | PREEMPT_RT 内核主线化、ROS 2 Real-Time Working Group 成果落地 [3] | 环形缓冲区执行器 [3]、分布式实时架构 [4] 显示社区正攻克该瓶颈 |
| **Sim-to-Real Gap 量化缺失**：缺乏标准化协议预测仿真性能向真实性能的迁移 | [2] | 方法论/基础设施 | RSS 2025 提出三大设计原则 [2]、Isaac Sim / MuJoCo / Genesis 视觉保真度提升 | 高视觉保真仿真 + 系统性扰动评估 + 对齐度量三原则若落地将形成拐点 |
| **安全关键控制标准化**：CBF/ICBF 理论成熟但工程集成碎片化 | [6], [14] | 理论-工程鸿沟 | 双凸优化 CBF 实时避障 [14]、ICCBF QP 形式 [6] 为标准化提供数学基础 | ros2_control 安全层插件标准化若达成共识将加速落地 |
| **多模态感知融合与控制协同延迟**：VLA 大模型推理延迟（~100-500ms）与控制回路（1-10ms）时尺度错配 | [2], [5] | 架构/算力 | ROS-Causal 因果框架 [5]、行为树/运动基元分层控制 | 分层架构（高层 VLA 规划 + 低层实时控制器）为主流缓解方向 |
| **运动学标定与动力学辨识自动化**：真机部署仍依赖人工标定，缺乏在线自适应标定通用框架 | [7], [11] | 工程/运维 | 2014 自适应控制理论 [7]、2024 连续体机器人实验验证 [11] | 在线参数估计与自适应控制融合为潜在拐点方向 |

### 4.2 拐点判断与不确定性

| 拐点假设 | 依据链 | 置信度 | 可证伪条件 | 标记 |
|----------|--------|--------|------------|------|
| 2026-2027 年 ROS 2 硬实时执行器（如 ring-buffer executor）将在主流发行版（Humble/Iron/Jazzy）成为默认选项 | [3] IEEE SCC 2023 已验证空间级应用，Real-Time WG 持续推进 | 较大概率 | 若 2027 年底主流发行版仍未默认集成实时执行器，则判断不成立 | [P] |
| 2025-2026 年出现首个社区广泛采用的 sim-to-real 标准化评测协议（基于 RSS 2025 三原则） | [2] RSS 2025 Workshop 顶会背书，三原则明确可操作 | 推测 | 若 2026 年底无开源基准库实现三原则且被 ≥3 组独立采用，则判断不成立 | [P] |
| CBF/ICBF 安全层将在 2026 年形成 ros2_control 标准插件规范 | [6] 理论成熟，[14] 实时 QP 求解验证，工程需求明确 | 推测 | 若 2026 年底 ros2_control 官方仓库无合并安全层接口 PR，则判断不成立 | [P] |
| VLA 部署将普遍采用“高层语义规划（~10Hz）+ 低层实时全身控制（>1kHz）”分层架构 | [2] 仿真评测滞后倒逼真机部署，[5] 因果框架探索分层 | 较大概率 | 若主流 VLA 开源项目（如 OpenVLA, π0, GR-1）2026 年均未发布分层 ROS 2 部署栈，则判断不成立 | [P] |

> 待核实：实时内核（PREEMPT_RT）完全主线化对 ROS 2 实时性能的边际提升量化数据。

---

## 5. 社会·政策·国际

### 5.1 监管与标准

| 维度 | 现状 | 证据来源 | 趋势判断 | 说明 |
|------|------|----------|----------|------|
| 机器人安全标准（ISO 10218, ISO/TS 15066）与 ROS 2 集成 | 标准存在但 ROS 2 合规工具链缺失 | [6], [4] | 推测：CBF/ICBF 形式化验证将成合规路径 [P] | ICCBF 提供前向不变集证明 [6]，符合功能安全（ISO 13849）证据链需求 |
| 实时系统认证（DO-178C, IEC 61508）在 ROS 2 上的落地 | 空间/航空领域有探索 [3] | [3] | 确定：航天级实时 ROS 2 已验证 [3] | 环形缓冲区执行器通过空间应用验证，为高可靠认证积累证据 |
| 数据隐私与模型出口管制对 VLA 训练数据/权重分发的影响 | 无直接证据 | 无 | 待核实 | > 待核实：需关注《人工智能法案》（EU）、出口管制清单对开源权重影响 |

### 5.2 地缘政治与供应链

| 因素 | 影响 | 证据来源 | 判断 |
|------|------|----------|------|
| GPU/加速芯片出口管制 | 影响 Isaac ROS、VLA 训练推理算力获取 | 无直接证据 | > 待核实 |
| 实时操作系统（RTOS）自主化需求 | 推动 ROS 2 on PREEMPT_RT / 国产 RTOS 适配 | [4], [3] | 确定：分布式实时 ROS 2 [4]、空间级实时 [3] 验证了非专有 RTOS 路线可行性 |
| 开源生态去中心化韧性 | ROS 2 社区治理模式对单一厂商依赖风险对冲 | 无直接证据 | > 待核实 |

### 5.3 伦理与劳动影响

| 议题 | 现状 | 证据来源 | 说明 |
|------|------|----------|------|
| 机器人教练助手的披露行为对用户感知影响 | 有实证研究 [15] | [15] | 非核心运动学/控制议题，但涉及人机交互安全透明度 |
| 语言流畅度与任务胜任力对社交机器人感知影响 | 有实证研究 [16] | [16] | 同上，属 HRI 范畴 |

---

## 6. 资本与生态

### 6.1 投资与并购信号

| 信号 | 时间 | 来源 | 判断 |
|------|------|------|------|
| NVIDIA 持续投入 Isaac ROS 生态（GPU 加速感知/规划） | 2023-2026 持续 | 官方发布 [待核实] | > 待核实：需查证 Isaac ROS 发布节奏与资源投入 |
| 实时 ROS 2 商业化支持厂商（PickNik, Open Robotics, 华为等）扩充团队 | 2022-2024 | 招聘公开信息 [待核实] | > 待核实 |
| 人形机器人独角兽融资轮次中明确提及“ROS 2 原生控制栈” | 2024-2025 | 融资公告 [待核实] | > 待核实 |

### 6.2 人才流动与社区活跃度

| 指标 | 现状 | 证据来源 | 说明 |
|------|------|----------|------|
| ROS 2 核心仓库（ros2/ros2_control, moveit/moveit2, ros-planning/navigation2）贡献者数量趋势 | 待核实 | GitHub Insights [待核实] | > 待核实 |
| 实时 ROS 2 工作组会议参与度、PR 合并率 | 待核实 | ROS Discourse / GitHub [待核实] | > 待核实 |
| VLA 相关开源项目（OpenVLA, π0, GR-1, Octo）ROS 2 集成 PR 活跃度 | 待核实 | GitHub [待核实] | > 待核实 |

### 6.3 生态成熟度评估

| 维度 | 成熟度 | 证据来源 | 说明 |
|------|--------|----------|------|
| 硬件抽象层（ros2_control） | 高 | 官方文档、广泛采用 [待核实] | 多主流机械臂厂商提供 ros2_control 驱动 |
| 运动规划 | 高 | MoveIt 2 官方维护 [待核实] | 运动学求解、碰撞检测、Servo 实时伺服完备 |
| 导航 | 高 | Nav2 官方维护 [待核实] | 行为树、插件化架构成熟 |
| 实时执行器 | 中高 | [3] 空间级验证，主流发行版集成进行中 | Ring-buffer executor 为关键里程碑 |
| 安全控制层（CBF/ICBF） | 低 | [6] 理论成熟，工程集成碎片化 | 缺乏 ros2_control 标准插件 |
| Sim-to-Real 评测基础设施 | 低 | [2] 明确缺口，无标准化协议 | RSS 2025 三原则为建设指引 |
| VLA 部署栈 | 早期 | [2], [5] 探索分层架构 | 无统一最佳实践，各项目自行集成 |

---

## 7. 信号与预测

### 7.1 早期信号

| 信号 | 来源 | 时间 | 可信度 | 说明 |
|------|------|------|--------|------|
| RSS 2025 Workshop 系统性提出 sim-to-real 基准三设计原则 | [2] | 2025-08 | 高（顶会工作坊） | 标志着社区从“碎片化竞赛”转向“原则化基准建设” |
| IEEE SCC 2023 环形缓冲区执行器通过空间级验证 | [3] | 2023 | 高（会议同行评审） | 硬实时 ROS 2 在最高可靠性场景落地，技术风险大幅降低 |
| ROS-Causal 框架将因果推断引入 ROS 生态 | [5] | 2024 | 中（arXiv 预印本） | 为可解释性、安全对齐提供新工程抽象 |
| 绳驱连续体机器人运动学实验验证（2024 IEEE CCDC） | [11] | 2024 | 中（会议论文） | 欠驱动/连续体本体运动学建模工程化进展 |
| 2026 年六足低成本平台 Web+ROS+RL 集成完整系统 | [1] | 2026 | 低（SSRN 预印本，无引用） | 边缘部署工程参考，学术权威性待验证 |

### 7.2 未来 6-18 月预测（可证伪假设）

| 预测 | 依据链 | 置信度 | 可证伪条件 | 标记 |
|------|--------|--------|------------|------|
| **至少 2 个主流开源基准库（如 SimplerEnv, LIBERO, Open X-Embodiment 衍生）将实现 RSS 2025 三原则中的 ≥2 条** | [2] 三原则明确可操作，社区痛点强烈 | 推测 | 若 2027-06 前无基准库在文档/代码中显式声称实现三原则且被引用，则不成立 | [P] |
| **ros2_control 官方仓库将合并 CBF/ICBF 安全层标准接口（HardwareInterface 扩展或 ControllerInterface 新类型）** | [6] QP 形式实时可解，[14] 双凸优化验证，工程需求明确 | 推测 | 若 2027-06 前 ros2_control/main 无相关 PR 合并，则不成立 | [P] |
| **NVIDIA Isaac ROS 将发布原生支持 VLA 分层部署的参考架构（高层 VLA + 低层 MPC/全身控制器）** | [2] 仿真评测滞后倒逼真机，[5] 分层因果框架探索 | 较大概率 | 若 2027-06 前 Isaac ROS 文档/示例无 VLA 分层部署教程，则不成立 | [P] |
| **PREEMPT_RT 完全主线化（Linux 6.12+）将使 ROS 2 在标准内核上实现 <100μs 抖动的 1kHz 控制回路** | [3] 空间级验证，Real-Time WG 持续推进 | 较大概率 | 若 2027-06 社区基准测试显示标准内核 1kHz 抖动仍 >200μs，则不成立 | [P] |
| **首个覆盖 ≥3 种本体（机械臂/灵巧手/移动底盘/人形）、≥10 任务、真机部署的统一基准榜单上线** | [2], [12], [13] 碎片化痛点明确，RRC 单一平台教训 | 推测 | 若 2027-06 无此类榜单且有 ≥3 组独立团队提交成绩，则不成立 | [P] |

### 7.3 风险与不确定性

| 风险 | 影响面 | 证据来源 | 缓解建议 |
|------|--------|----------|----------|
| **Sim-to-Real 评测协议制定陷入“设计由委员会”僵局，长期无可用标准** | 全领域算法可比性、商业化风险评估 | [2] 指出缺口但未给出治理机制 | 推动“最小可行性基准”（MVP）先行，由头部实验室主导开源，再寻求标准化 |
| **CBF/ICBF 安全层标准化因 QP 求解器选型（OSQP/qpOASES/自研）分裂，导致生态碎片化** | 安全关键应用落地、认证成本 | [6] QP 形式通用，但求解器生态多元 | ros2_control 定义求解器抽象接口，官方提供 OSQP 默认实现 |
| **VLA 大模型推理算力成本与实时性矛盾导致“分层架构”成为事实上的闭源壁垒** | 开源生态健康度、中小团队参入门槛 | [2], [5] 分层架构为主流方向 | 推动开源低延迟推理引擎（TensorRT-LLM, vLLM 实时分支）与 ROS 2 原生集成 |
| **实时 ROS 2 核心维护者精力分散（Open Robotics 裁员/重组传闻）导致 LTS 版本维护滞后** | 生态稳定性、企业采信度 | 传闻 [R] | 关注 ROS 2 技术指导委员会（TSC）治理变化，建立企业联盟共同维护分支 |
| **地缘政治导致 GPU/加速芯片供应中断，迫使 VLA 部署转向 CPU/NPU 混合推理，延迟不可控** | 算力获取、部署成本、实时性 | 传闻 [R] | 备选：开源 CPU 推理优化（ONNX Runtime, OpenVINO）、国产加速卡适配 ROS 2 |

---

## 参考来源
[1] Development of a Web-Based Joint-Level Control Bridge for a Dynamixel-Based Hexapod Robot Toward Raspberry Pi, Inverse Kinematics, ROS, and Reinforcement Learning Integration — https://doi.org/10.2139/ssrn.7064338
[2] Robot Policy Evaluation for Sim-to-Real Transfer: A Benchmarking Perspective — http://arxiv.org/abs/2508.11117v1
[3] The ring-buffer ROS2 executor: a novel approach for real-time ROS2 Space applications — https://doi.org/10.1109/scc57168.2023.00021
[4] Towards Distributed Real-Time capable Robotic Control using ROS2 — https://doi.org/10.1109/case49997.2022.9926569
[5] ROS-Causal: A ROS-based Causal Analysis Framework for Human-Robot Interaction Applications — http://arxiv.org/abs/2402.16068v3
[6] Safe Control Synthesis via Input Constrained Control Barrier Functions — http://arxiv.org/abs/2104.01704v1
[7] Adaptive Control of Robot Manipulators With Uncertain Kinematics and Dynamics — http://arxiv.org/abs/1403.5204v3
[8] A Real-Time Model-Based Reinforcement Learning Architecture for Robot Control — http://arxiv.org/abs/1105.1749v2
[9] Robot Arm Kinematics — https://doi.org/10.1201/9781315152691-17
[10] A Concise Bézier Clipping Technique for Solving Inverse Kinematics Problems — https://doi.org/10.1007/978-94-011-4120-8_6
[11] Structure Design and Kinematics Analysis and Experiment of Rope-driven Continuum Robot — https://doi.org/10.1109/ccdc62350.2024.10587576
[12] Grasp and Motion Planning for Dexterous Manipulation for the Real Robot Challenge — http://arxiv.org/abs/2101.02842v1
[13] One-Shot Reinforcement Learning for Robot Navigation with Interactive Replay — http://arxiv.org/abs/1711.10137v2
[14] Duality-based Convex Optimization for Real-time Obstacle Avoidance between Polytopes with Control Barrier Functions — http://arxiv.org/abs/2107.08360v4
[15] Users' Perception on Appropriateness of Robotic Coaching Assistant's Disclosure Behaviors — http://arxiv.org/abs/2410.10550v1
[16] What Am I? Evaluating the Effect of Language Fluency and Task Competency on the Perception of a Social Robot — http://arxiv.org/abs/2410.11085v1

---

*Generated by research-bot · topic=`机器人运动学控制与-ros-2` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`nvidia/nemotron-3-ultra-550b-a55b` · sources=36 · duration=384s · 2026-11-26T04:12:21+00:00*
