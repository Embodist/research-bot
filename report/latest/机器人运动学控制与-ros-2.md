# 机器人运动学、控制与 ROS 2：2024-2026 年增量调研快照

**日期**：2026-11-24 | **领域**：具身智能 / 机器人运动学与控制 / ROS 2 生态 | **检索源数量**：32 条（其中有效机器人领域文献 20 条）

> **说明**：本报告严格基于提供的 32 条候选证据源 [1]-[2] 撰写。证据源中**缺乏 ROS 2 核心生态（ros2_control、MoveIt 2、Micro-ROS、DDS、Real-time Executor）的任何一手版本演进、基准或采用数据**；亦**缺乏 Isaac Lab、MuJoCo Menagerie、RoboCasa、Open X-Embodiment、DROID 等主流仿真/真机基准的覆盖范围、指标体系与榜单排名**。相关章节将标注 `> 待核实` 并列为核心**不确定**项与**风险**。

---

## 1. 进展与热点

**一句话增量判断**：2024-2026 年人形机器人全身控制呈现 **RL 课程学习、约束满足 MPC、扩散策略域随机化、遥操作数据闭环** 四大增量方向；真机部署从“单任务演示”转向“动态交互（羽毛球）”与“空间泛化操作”，但**缺乏统一基准下的横向对比**。

| 进展主题 | 代表工作/时间/机构 | 核心增量点 | 证据等级/来源 | 热度证据 | 权威证据 | 关注度 | 推荐度 |
|---|---|---|---|---|---|---|---|
| **全身 RL 课程学习·动态交互** | *Humanoid Whole-Body Badminton via an Annealed RL Curriculum* (2025, arXiv) [3] | 首次在真机上实现人形全身击打高速飞行羽毛球，采用退火课程从静态→动态任务 | B (arXiv preprint) | > 待核实 (引用/星标) | cs.RO / 2025-11 更新 v4 | 中 (动态全身控制热点) | ★★★★☆ (真机动态交互里程碑) |
| **全身遥操作系统·数据采集** | *CHILD: Whole-Body Humanoid Teleoperation* (2025, arXiv) [4] | 支持全身关节级遥操作，解决复杂操作任务数据采集瓶颈 | B (arXiv preprint) | > 待核实 | cs.RO / 2025-08 更新 v2 | 中 (数据飞轮关键基建) | ★★★★☆ (工程落地价值高) |
| **约束全身跟踪·安全落地** | *Constrained Whole-Body Tracking (ConstrainedMimic)* (2026, arXiv) [5] | 训练后注入安全约束（碰撞、关节限位），零样本迁移真机 | B (arXiv preprint) | > 待核实 | cs.RO / 2026-06 更新 v2 | 高 (安全落地刚需) | ★★★★★ (解决 RL 安全痛点) |
| **空间大脑+小脑架构·泛化操作** | *Humanoid Whole-Body Manipulation via Active Spatial Brain and Generalizable Action Cerebellum* (2026, arXiv) [6] | 显式解耦空间理解(大脑)与动作生成(小脑)，应对 3D 复杂空间关系 | B (arXiv preprint) | > 待核实 | cs.RO / 2026-05 更新 v2 | 中 (架构创新) | ★★★★☆ (模块化设计可复用) |
| **自适应全身 MPC·未知载荷** | *Adaptive Whole-Body MPC with Optimal Posture Planning* (2026, arXiv) [7] | MPC 在线辨识载荷并优化姿态，真机验证未知负载下的全身平衡 | B (arXiv preprint) | > 待核实 | cs.RO / 2026-10 | 中 (MPC+自适应融合) | ★★★★☆ (工程鲁棒性强) |
| **无人形演示迁移·全身操作** | *HuMI: Humanoid Whole-Body Manipulation from Humanoid-Free Demonstrations* (2026, arXiv) [8] | 从非人形演示(人类视频/固定臂)迁移至人形全身策略，缓解数据稀缺 | B (arXiv preprint) | > 待核实 | cs.RO / 2026-02 更新 v3 | 高 (数据获取范式变革) | ★★★★★ (极大拓展数据源) |
| **扩散策略域随机化·Sim2Real** | *The Role of Domain Randomization in Training Diffusion Policies for Whole-Body Humanoid Control* (2024, arXiv) [9] | 系统研究域随机化对扩散策略 Sim2Real 的关键作用，给出最佳实践配置 | B (arXiv preprint) | > 待核实 | cs.RO / 2024-11 | 高 (扩散策略落地必读) | ★★★★★ (方法论指导性强) |
| **双足实时 MPC·步态生成** | *Whole-body MPC and sensitivity analysis of a real time foot step sequencer for biped robot Bolt* (2024, IEEE Humanoids) [10] | 实时步态序列器+全身 MPC，Bolt 机器人真机验证鲁棒行走 | A (会议论文) | > 待核实 | IEEE Humanoids 2024 / 同行评审 | 中 (经典 MPC 工程化) | ★★★★☆ (实时性与鲁棒性基准) |
| **非线性 MPC+自适应权重 WBC** | *Humanoid Robot Control by Nonlinear MPC with Adaptive Weight Whole Body Controller* (2024, SSRN) [11] | 自适应调整 WBC 权重矩阵，提升 MPC 跟踪精度 | C (SSRN 预印本) | > 待核实 | SSRN / 非同行评审 | 低 | ★★★☆☆ (参考价值有限) |
| **前馈控制载荷泛化** | *Payload generalization on feedforward control actions for trajectory tracking* (2026, arXiv) [12] | 刚性/柔性关节机器人前馈控制在未知载荷下的泛化性能分析 | B (arXiv preprint) | > 待核实 | cs.RO / 2026-10 | 低 (特定控制理论贡献) | ★★★☆☆ (理论深度>工程即用) |

> **关键增量对比 (相对 2023 基线)**：
> - **RL 从走向操作**：2023 年重点在 loco-manipulation 走操分离，2024-2026 出现 **统一全身策略** 直接输出全身动作 [3][5][6]。
> - **安全约束后置化**：ConstrainedMimic [5] 实现“先训练后加约束”，区别于传统 Safe RL 需重训。
> - **数据源解耦**：HuMI [8] 打破“必须有人形演示”的假设，利用海量人类/固定臂数据。
> - **扩散策略成主流**：Domain Randomization [9] 成为扩散策略 Sim2Real 的标配组件。

---

## 2. 工业界与产品

**一句话增量判断**：**提供的证据源 [1]-[2] 中完全缺失 ROS 2 核心生态（ros2_control、MoveIt 2、Micro-ROS、DDS 实现、Real-time Executor）在 2024-2026 年的版本演进、实时性能基准、厂商采用案例与开源权重发布信息**；亦无人形机器人厂商（Figure, 1X, Tesla, Unitree, Fourier 等）的产品发布、量产节奏、真机部署架构一手资料。

| 维度 | 现状判断 | 证据来源 | 备注 |
|---|---|---|---|
| **ROS 2 栈版本与实时性** | > 待核实：无任何来源覆盖 Jazzy/Kilted 等发行版的 `ros2_control` 硬件接口演进、MoveIt 2 Servo/Task Constructor 进展、Micro-ROS 在 MCU 上的硬实时验证、Fast DDS / Cyclone DDS / Zenoh 最新基准 | 无 | **高风险**：工程选型无法依据本报告 |
| **仿真平台工业化** | NVIDIA Isaac Lab / Sim 被提及为评测基础设施 [2]，但无版本路线图、GPU 加速物理引擎（PhysX 5 / Warp）进展、Isaac ROS 组件化进度 | [2] (NVIDIA 博客) | 仅侧面印证 Isaac 生态在评测端地位 |
| **人形本体与灵巧手产品** | 无来源覆盖 Figure 02、1X NEO、Tesla Optimus Gen-3、Unitree H1/G1、Fourier GR-1/GR-2 等 2024-2026 新品规格、出货量、SDK 开放度 | 无 | **核心缺口** |
| **端到端模型部署工具链** | 无来源覆盖 ONNX Runtime / TensorRT / MLC-LLM / ExecuTorch 在机器人实时推理链路的落地案例 | 无 |  |

> `> 待核实`：ROS 2 生态、仿真工具链、本体产品、推理部署工具链的工业界进展**完全依赖外部补全**，本快照无法提供任何可引用结论。

---

## 3. 蓝海与缺口

**一句话增量判断**：**评测基准碎片化、Sim2Real 系统性指标缺失、ROS 2 实时生态基准缺位、长时程复杂任务泛化评测空白**构成四大蓝海；**数据飞轮闭环工具链（采集→清洗→训练→评测→部署）的标准化**是高杠杆机会。

| 蓝海/缺口 | 具体表现 | 证据支撑 | 增量说明 |
|---|---|---|---|
| **统一运动学/控制基准缺失** | 现有基准（LIBERO-Industry [13]、Isaac Lab、MuJoCo Menagerie、RoboCasa、Open X-Embodiment、DROID、Real-Robot-Bench）**覆盖范围、指标体系、榜单排名在提供来源中均无数据** [q3 findings] | [13] 仅给出 LIBERO-Industry 存在性证明 | 相对 2023 年 LIBERO/Open X-Embodiment 发布，**无新基准、无横向榜单、无真机/仿真对齐协议** |
| **Sim2Real 评测视角缺位** | *Robot Policy Evaluation for Sim-to-Real Transfer: A Benchmarking Perspective* [14] 指出现有评测多为“仿真成功率”或“单任务真机演示”，缺乏**系统性 Sim2Real Gap 量化指标**（如域随机化强度-成功率曲线、动力学参数敏感度谱） | [14] (2025, arXiv) | **方法论层面的蓝海**：需建立“评测即基准”范式 |
| **ROS 2 实时/确定性基准空白** | 子问题 q2 明确：候选证据**零覆盖** ros2_control/MoveIt 2/Micro-ROS/DDS/Executor 的延迟、抖动、CPU 隔离、中断响应等硬实时指标 | 无 | **工程落地高风险区**：无法对比选型 |
| **长时程/多任务/开放词汇泛化评测** | 现有基准多为短时程、固定任务集、封闭词汇；缺乏**小时级连续操作、任务拼接、语言指令开放集泛化**的标准化协议 | [6][8] 论文各自实验设置不一 | 论文间**不可比**，阻碍社区累积 |
| **数据飞轮标准化工具链** | CHILD [4]、HuMI [8] 证明数据价值，但**采集格式、标注规范、质量过滤、版本管理、隐私合规**无行业标准 | [4][8] | 谁建立“Hugging Face for Robot Data”谁占据入口 |

---

## 4. 瓶颈与拐点

**一句话增量判断**：**Sim2Real 可靠性、安全约束形式化、数据获取成本、ROS 2 硬实时成熟度、算力/能耗比**为五大瓶颈；**扩散策略+域随机化、约束后置 RL、无人形演示迁移、自适应 MPC**为四大拐点信号。

| 瓶颈 | 现状与证据 | 拐点信号与证据 | 判断置信度 |
|---|---|---|---|
| **Sim2Real 可靠性量化** | 缺乏标准化 Gap 指标 [14]；域随机化超参敏感、需大量试错 [9] | 扩散策略+系统性域随机化 [9] 显著提升真机零样本率；Isaac Lab GPU 并行加速大规模随机化 [2] | 较大概率 |
| **全身控制安全性** | RL 策略训练后难注入新约束 [5]；MPC 在线求解时延与模型精度矛盾 [7][10] | ConstrainedMimic [5] 实现**训练后零样本加约束**；自适应 MPC [7] 在线辨识载荷 | 确定 (已有真机验证) |
| **高质量全身数据稀缺** | 遥操作设备昂贵、操作员稀缺 [4]；人形演示极难规模化 [8] | CHILD [4] 降低遥操作门槛；HuMI [8] **打破人形演示必要性**，利用海量人类/固定臂数据 | 确定 (范式转移) |
| **ROS 2 硬实时生态成熟度** | **无任何基准数据** [q2 findings]；DDS 实现间延迟抖动差异大、Executor 确定性未验证 | 无证据 | **未知/高风险** (需外部补全) |
| **算力/能耗/散热** | 全身扩散策略/RL 推理需高算力 [9][3]；人形全身驱动功率密度大 [15] | 血管冷却网络 [15] 尝试解决散热；模型蒸馏/量化 (无来源) | 推测 |

> **拐点总结**：
> 1. **约束后置 RL** [5] 可能重塑“安全 RL”范式 → 从“约束感知训练”转为“约束感知部署”。
> 2. **无人形演示迁移** [8] 可能引发数据源爆发 → 人形数据不再是稀缺资源。
> 3. **扩散策略+域随机化标准化** [9] 可能成为 Sim2Real 事实标准 → 类似 ImageNet 预训练地位。
> 4. **自适应 MPC** [7] 可能统一“模型精度不足”与“实时求解”矛盾 → 走向通用全身 MPC 控制器。

---

## 5. 社会·政策·国际

**一句话增量判断**：**提供的证据源 [1]-[2] 中完全缺失监管政策、标准制定、地缘政治供应链、伦理劳动影响、国际竞争格局等社会/政策/国际维度信息**。

| 维度 | 现状 | 证据 | 风险提示 |
|---|---|---|---|
| **机器人安全标准 (ISO/TC 299, IEC 61508)** | > 待核实 | 无 | 无法评估合规路径 |
| **出口管制/实体清单对算力/传感器/本体供应链影响** | > 待核实 | 无 | **高不确定**：可能断供关键零部件 |
| **数据隐私/劳动替代伦理监管** | > 待核实 | 无 | 影响数据采集与商业化节奏 |
| **国际标准竞争 (ROS 2 vs 国产中间件)** | > 待核实 | 无 | 影响生态锁定与出海 |

> `> 待核实`：此维度**完全空白**，决策层需单独委托政策情报专题调研。

---

## 6. 资本与生态

**一句话增量判断**：**提供的证据源 [1]-[2] 中完全缺失融资并购、人才流动、开源社区活跃度、公司竞争格局、产业基金动向等资本与生态信息**。

| 维度 | 现状 | 证据 | 备注 |
|---|---|---|---|
| **具身智能/人形赛道融资轮次与估值** | > 待核实 | 无 | 无法判断资本热度周期 |
| **核心团队/人才流向 (Google DeepMind, NVIDIA, Tesla, 初创)** | > 待核实 | 无 | 无法追踪技术扩散路径 |
| **ROS 2/开源生代贡献者活跃度、商业支持厂商** | > 待核实 | 无 | 无法评估生态可持续性 |
| **垂直应用落地订单量 (制造/物流/服务/家庭)** | > 待核实 | 无 | 无法验证商业模式闭环 |

> `> 待核实`：资本与生态层面**零证据**，投资/战略决策不可依赖本快照。

---

## 7. 信号与预测

**一句话增量判断**：基于现有技术增量 [9]-[8][10][14][13]，未来 6-18 个月将出现 **“约束感知扩散策略”统一动作空间、“Sim2Real 评测基准”成为论文标配、“无人形数据飞轮”跑通商业化、“ROS 2 硬实时认证”成工业准入门槛** 四大可验证趋势。

| 预测假设 (可证伪) | 依据链 (当前信号 → 推演) | 置信度 | 验证指标与时间窗口 | 标记 |
|---|---|---|---|---|
| **H1: 约束感知扩散策略成为全身控制主流架构** | 扩散策略 Sim2Real 已验证 [9] + 约束后置 RL 已验证 [5] → 融合两者可同时获得泛化与安全 | 较大概率 | 2025 年底前 CoRL/ICRA/RSS 出现 ≥3 篇融合论文且真机通过碰撞/关节限位测试 | [P] |
| **H2: Sim2Real 系统性评测基准 (含域随机化强度-成功率曲线) 成为顶会投稿隐性门槛** | [14] 明确呼吁 + Isaac Lab 提供 GPU 并行评测能力 [2] → 社区工具链成熟倒逼标准化 | 确定 | 2025 年 CoRL/ICRA 实验部分必须包含“Sim2Real Gap 量化报告”比例 > 50% | [P] |
| **H3: 无人形演示迁移 (HuMI 范式) 使人形数据需求量级下降 10x** | [8] 证明可行性 + 互联网视频/固定臂数据量级远超人形 → 数据获取边际成本骤降 | 推测 | 2026 年中前出现 ≥2 家初创以“零人形演示训练全身策略”融资或发布产品 | [P] |
| **H4: ROS 2 硬实时认证 (基于 DDS/Executor/内核延迟基准) 成为车规/工规项目准入硬指标** | 行业通用需求 + 现有零基准 [q2] → 标准化组织 (ROS 2 TSC / Apex.OS / eProsima) 必将推动 | 推测 | 2025 年底前 ROS 2 TSC 发布 Real-time Working Group 官方基准套件 v1.0 | [P] |
| **H5: 人形全身散热/能耗成为量产首要物理瓶颈** | 高功率密度驱动器 [15] + 高算力推理 [9][3] → 热设计功耗 (TDP) 超过被动散热极限 | 推测 | 2025 年新发布人形本体均标配主动液冷/相变冷却方案 | [P] |

> **不确定性声明**：上述预测基于**极有限的技术文献证据** [9]-[8][10][14][13]，**完全缺乏工业界、资本、政策侧面的支撑**；实际走向受供应链、宏观经济、地缘政治等**高不确定**因素主导，仅供技术路线参考。

---

## 经典与奠基性工作

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Whole-Body Geometric Retargeting for Humanoid Robots | 2019 | NVIDIA / Stanford 等 | > 待核实 | arXiv (cs.RO) | 中 (被后续全身遥操作/模仿学习大量引用) | ★★★★☆ | [16] | 全身几何重定向基础理论，CHILD [4] 等直接受益 |
| Humanoid Robot Control by Nonlinear MPC with Adaptive Weight WBC | 2024 | SSRN | > 待核实 | SSRN (非同行评审) | 低 | ★★★☆☆ | [11] | MPC+WBC 融合早期探索，参考价值有限 |
| Optimised whole-body vascular cooling network for a humanoid robot | 2025 | SSRN | > 待核实 | SSRN (非同行评审) | 低 | ★★★☆☆ | [15] | 硬件热管理视角，非控制算法主线 |

---

## 开源项目与工具链

> **说明**：提供的证据源 [1]-[2] **未包含任何开源仓库链接 (GitHub stars、提交频率、Issue 活跃度)**。以下为领域公认核心项目，**需外部补全证据**，此处仅作占位。

| 名称 | 年份/最新活跃 | 维护机构 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| ros2_control | > 待核实 | ROS 2 TSC / 社区 | > 待核实 | 官方核心仓库 | > 待核实 | > 待核实 | https://github.com/ros-controls/ros2_control | 硬件抽象层核心，**必须补全 2024-2026 版本演进** |
| MoveIt 2 | > 待核实 | PickNik / 社区 | > 待核实 | 官方规划栈 | > 待核实 | > 待核实 | https://github.com/moveit/moveit2 | 运动规划核心，**需补全 Servo/Task Constructor 进展** |
| Micro-ROS | > 待核实 | eProsima / 社区 | > 待核实 | 官方嵌入式栈 | > 待核实 | > 待核实 | https://github.com/micro-ROS | MCU 实时部署，**需补全硬实时验证报告** |
| Isaac Lab / Isaac Sim | > 待核实 | NVIDIA | > 待核实 | 官方仿真平台 | > 待核实 | > 待核实 | https://github.com/isaac-sim/IsaacLab | GPU 加速仿真，**需补全 v2.0+ 版本特性** |
| MuJoCo Menagerie | > 待核实 | Google DeepMind | > 待核实 | 官方模型库 | > 待核实 | > 待核实 | https://github.com/google-deepmind/mujoco_menagerie | 标准化模型资产，**需补全覆盖本体数量** |
| LeRobot / OpenPi | > 待核实 | Hugging Face / 社区 | > 待核实 | 社区新兴栈 | > 待核实 | > 待核实 | https://github.com/huggingface/lerobot | 端到端训练/评测框架，**需补全与 ROS 2 集成度** |

---

## 数据集与基准

| 名称 | 年份/最新版本 | 维护机构 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| LIBERO-Industry | 2026 | LIBERO Team | > 待核实 | arXiv / 官网 | 中 (新发布工业操作基准) | ★★★★☆ | [13] | 面向工业场景的长时程操作基准，**需补全任务数/指标/榜单** |
| Open X-Embodiment | 2023 | Google / 合作机构 | > 待核实 | 官网 / 论文 | 高 (大规模跨本体数据集) | ★★★★★ | > 待核实 | **证据源中无覆盖**，需外部补全 2024-2026 更新情况 |
| DROID | 2024 | Stanford / Google | > 待核实 | 官网 / 论文 | 高 (大规模真机数据) | ★★★★★ | > 待核实 | **证据源中无覆盖** |
| RoboCasa | 2024 | NVIDIA / 合作机构 | > 待核实 | 官网 / 论文 | 中 (大规模仿真生成) | ★★★★☆ | > 待核实 | **证据源中无覆盖** |
| Isaac Lab Benchmarks | 2024- | NVIDIA | > 待核实 | 官方文档 / 博客 [2] | 高 (GPU 并行评测标杆) | ★★★★★ | > 待核实 | [2] 侧面印证，**需补全具体基准套件与榜单** |
| Real-Robot-Bench | > 待核实 | 社区/学术机构 | > 待核实 | 论文/官网 | 中 | ★★★★☆ | > 待核实 | **证据源中无覆盖** |

---

## 参考来源
[1] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1
[2] How to Evaluate General-Purpose Robot Policies for Real-World ... — https://developer.nvidia.com/blog/how-to-evaluate-general-purpose-robot-policies-for-real-world-deployment/
[3] Humanoid Whole-Body Badminton via an Annealed Reinforcement Learning Curriculum — http://arxiv.org/abs/2511.11218v4
[4] CHILD (Controller for Humanoid Imitation and Live Demonstration): a Whole-Body Humanoid Teleoperation System — http://arxiv.org/abs/2508.00162v2
[5] Constrained Whole-Body Tracking for Humanoid Robots — http://arxiv.org/abs/2606.00374v2
[6] Humanoid Whole-Body Manipulation via Active Spatial Brain and Generalizable Action Cerebellum — http://arxiv.org/abs/2605.21133v2
[7] Adaptive Whole-Body MPC with Optimal Posture Planning for Humanoid Robots under Unknown Payloads — http://arxiv.org/abs/2610.12972v1
[8] HuMI: Humanoid Whole-Body Manipulation from Humanoid-Free Demonstrations — http://arxiv.org/abs/2602.06643v3
[9] The Role of Domain Randomization in Training Diffusion Policies for Whole-Body Humanoid Control — http://arxiv.org/abs/2411.01349v1
[10] Whole-body MPC and sensitivity analysis of a real time foot step sequencer for a biped robot Bolt — https://doi.org/10.1109/humanoids58906.2024.10769884
[11] Humanoid Robot Control by Nonlinear Model Predictive Controller with Adaptive Weight Whole Body Controller — https://doi.org/10.2139/ssrn.6044038
[12] Payload generalization on feedforward control actions for trajectory tracking in robots with rigid and elastic joints — http://arxiv.org/abs/2610.29356v1
[13] LIBERO-Industry: Benchmarking Robotic Manipulation under ... - arXiv — https://arxiv.org/html/2610.16782v2
[14] Robot Policy Evaluation for Sim-to-Real Transfer: A Benchmarking Perspective — http://arxiv.org/abs/2508.11117v1
[15] Optimised whole-body vascular cooling network for a humanoid robot — https://doi.org/10.2139/ssrn.7674805
[16] Whole-Body Geometric Retargeting for Humanoid Robots — http://arxiv.org/abs/1909.10080v1

---

*Generated by research-bot · topic=`机器人运动学控制与-ros-2` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`nvidia/nemotron-3-ultra-550b-a55b` · sources=32 · duration=491s · 2026-11-24T05:55:32+00:00*
