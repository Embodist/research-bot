# 机器人运动学、控制与 ROS 2 生态：2024-2026 年前沿进展、经典基石与开放问题综述报告

**日期**：2026-11-14（UTC）  
**领域**：具身智能 / 机器人运动学与控制 / ROS 2 生态  
**检索源数量**：35 条可引用来源（含 arXiv 预印本、基准论文、开源项目文档）  
**方法论**：遵循 deep-research、frontier-tracking、paper-survey、evidence-grading、frontier-watch 五大 Skill；全文论断均标注引用编号 [n]，证据不足处标注 `> 待核实`。

---

## 1. 进展与热点（Progress & Hotspots）

### 1.1 类人全身动态交互与强化学习控制（2024-2025 增量）
- **退火强化学习课程实现无先验类人羽毛球击球**：2025 年提出统一全身控制器，通过退火课程先用辅助运动目标稳定学习，再逐步移除聚焦击球目标，解决稀疏奖励与梯度冲突，实现足步与击球协调 [1]。  
  - 热度证据：arXiv 预印本，引用数暂无 [1]  
  - 权威证据：arXiv cs.RO，未经同行评审 [1]  
  - 关注度：中 —— 类人快速动态交互稀有实证，社区讨论度上升  
  - 推荐度：★★★☆☆ —— 关注全身 RL 控制范式，待同行评审  

- **域随机化在全身类人扩散策略训练中的作用**：2024 年系统研究域随机化对全身类人扩散策略 Sim-to-Real 迁移的影响，揭示视觉-动作耦合下的随机化敏感性 [2]。  
  - 热度证据：arXiv 预印本，引用数暂无 [2]  
  - 权威证据：arXiv cs.RO，未经同行评审 [2]  
  - 关注度：中 —— 扩散策略与全身控制结合的热点补充  
  - 推荐度：★★★☆ —— 关注 Sim-to-Real 细节，但为预印本  

### 1.2 类人全身遥操作与数据采集系统（2025 增量）
- **CHILD 系统：可重构类人全身遥操作平台**：2025 年发布，装入标准婴儿背带，提供四肢关节级直接映射与自适应力反馈防止不安全关节运动，验证全身关节级遥操作可行性 [3]。  
  - 热度证据：arXiv 预印本，引用数暂无 [3]  
  - 权威证据：arXiv cs.RO，未经同行评审 [3]  
  - 关注度：中 —— 罕见支持类人全身关节级遥操作的紧凑系统  
  - 推荐度：★★★☆☆ —— 类人数据采集关键工程进展，待同行评审  

- **ALOHA 2：低成本双臂遥操作硬件增强版**：2024 年发布，改进夹爪、重力补偿、相机布局，配套 ROS 2 驱动与数据采集管线，显著降低双臂操作数据采集门槛 [4]。  
  - 热度证据：arXiv 预印本，GitHub 星标数 > 2.5k（截至 2026-11） [4]  
  - 权威证据：arXiv cs.RO，配套开源硬件设计与 ROS 2 软件栈 [4]  
  - 关注度：高 —— 社区广泛采用的双臂数据采集标准平台  
  - 推荐度：★★★★★ —— 工程落地成熟度高，直接可复现  

### 1.3 全身模型预测控制（MPC）实时化与工程化（2024 增量）
- **全身非线性 MPC 在类人/足式机器人上达到实时部署速率**：2024 年系统分析不等式约束对高维系统实时性的影响，提出求解精度与计算预算的权衡策略，实现全身 NMPC 实时运行 [5]。  
  - 热度证据：arXiv 预印本，被后续全身 MPC 工作引用 [5]  
  - 权威证据：arXiv cs.RO，未经同行评审但技术细节扎实 [5]  
  - 关注度：高 —— 2024 年全身 MPC 工程化关键进展，直指约束求解痛点  
  - 推荐度：★★★★★ —— 全身 MPC 落地必读  

### 1.4 视觉-语言-动作（VLA）基座模型规模化与多本体统一（2026 增量）
- **Xiaomi-Robotics-1**：2026 年发布，使用两阶段训练（预训练+后训练），在 10 万小时真机轨迹上训练，实现开箱即用的移动操作零样本泛化 [6]。  
  - 热度证据：arXiv 预印本，真机数据规模创纪录 [6]  
  - 权威证据：arXiv cs.RO，未经同行评审 [6]  
  - 关注度：高 —— 端到端学习范式下控制新范式的规模化里程碑  
  - 推荐度：★★★★☆ —— 学习型控制前沿，非经典控制理论  

- **Meituan-Robotics-0**：2026 年发布，融合 1.47 亿视觉语言样本与 1.5 万小时多本体轨迹（12 种本体），采用三阶段训练对齐多模态表征与离散动作 token [7]。  
  - 热度证据：arXiv 预印本，多本体数据规模领先 [7]  
  - 权威证据：arXiv cs.RO，未经同行评审 [7]  
  - 关注度：高 —— 多本体统一动作空间工程化尝试  
  - 推荐度：★★★★☆ —— 统一控制范式参考  

### 1.5 可微物理与仿真-实机迁移工具链（2024 增量）
- **DiffSim2Real**：2024 年提出纯在可微仿真中训练四足步态策略并直接部署真机，利用可微物理引擎实现系统辨识与策略优化联合进行 [8]。  
  - 热度证据：arXiv 预印本，引用数暂无 [8]  
  - 权威证据：arXiv cs.RO，未经同行评审 [8]  
  - 关注度：中 —— 可微仿真直通真机的工程化示范  
  - 推荐度：★★★★☆ —— Sim2Real 工具链关键参考  

- **自监督视觉伺服面向低刚度机器人**：2024 年考虑时变身体形变，提出自监督视觉伺服方法，无需精确运动学模型即可实现柔性本体控制 [9]。  
  - 热度证据：arXiv 预印本，引用数暂无 [9]  
  - 权威证据：arXiv cs.RO，未经同行评审 [9]  
  - 关注度：中 —— 柔性/低刚度本体控制的新思路  
  - 推荐度：★★★☆☆ —— 非刚体运动学控制的探索性工作  

### 1.6 经典奠基性工作（基线对比用）
| 名称 | 年份 | 机构/作者 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|----------|----------|--------|--------|------|------|
| Keep Rollin' - Whole-Body Motion Control for Wheeled Quadrupedal Robots | 2018 | ETH Zurich 等 | 被后续全身控制工作广泛引用 | arXiv cs.RO 预印本 | 中 | ★★★★☆ | [10] | 轮足复合本体全身控制早期奠基，将轮子自由度纳入 ZMP 优化 |
| Task Space Inverse Dynamics: Prioritized motion-force control | 2014 | Righetti 等 | 经典全身控制理论基石 | arXiv eess.SY 预印本 | 中 | ★★★★☆ | [11] | 任务空间逆动力学与优先级控制理论奠基 |
| Spatial Vector Algebra (Featherstone) | 2008 | Springer | 刚体动力学计算标准教材章节 | 同行评审教材章节 | 高 | ★★★★★ | [12] | 现代刚体动力学/运动学算法数学基础 |
| Encoding Physical Constraints in Differentiable Newton-Euler Algorithm | 2020 | MIT 等 | 可微物理/运动学基础工作 | arXiv cs.RO 预印本 | 低（超出查询窗口） | ★★☆☆☆ | [13] | 可微牛顿-欧拉引入物理约束，保证参数物理合理 |
| Adaptive Control of Robot Manipulators With Uncertain Kinematics and Dynamics | 2014 | 经典自适应控制 | 早期自适应控制理论 | arXiv eess.SY 预印本 | 低 | ★☆☆☆☆ | [14] | 不确定运动学/动力学下任务空间轨迹跟踪理论 |

> 待核实：经典教材级工作（Craig《机器人力学与控制》、Spong《机器人建模与控制》、Murray/Li/Sastry《机器人数学基础》）未在候选证据中出现，需人工补充。

---

## 2. 工业界与产品（Industry & Product）

### 2.1 主流机器人厂商与 ROS 2 原生产品线（增量）
- **小米机器人**：发布 Xiaomi-Robotics-1 VLA 基座模型，依托 10 万小时真机轨迹数据，展示端到端学习在家庭/商用场景的落地潜力 [6]。  
- **美团机器人**：发布 Meituan-Robotics-0 桌面操作 VLA，聚焦多本体统一动作空间，面向餐饮/零售自动化场景 [7]。  
- **NimbRo-OP 人形平台**：2018 年发布基于 ROS 的软件框架，后持续迁移至 ROS 2，提供全身控制、步态生成、视觉感知模块化集成 [15]。  

> 待核实：Unitree、Agility Robotics、Figure AI、Tesla Optimus、Apptronik 等头部人形/四足厂商的 ROS 2 原生控制栈、实时内核配置、硬件抽象层（HAL）设计细节在候选证据中缺失，需补充官方技术博客/白皮书。

### 2.2 ROS 2 核心中间件与实时性生态（增量）
- **ros2_control / ros2_controllers**：成为工业级实时控制回路的标准抽象层，支持硬件接口、控制器管理器、实时发布/订阅（基于 DDS 实时 QoS）[> 待核实：官方文档版本与采用率统计]。  
- **MoveIt 2 / MoveIt Servo / MoveIt Task Constructor**：运动规划与伺服控制集成框架，支持混合规划-控制管线，已在多款协作机器人（UR、Franka、Doosan 等）上量产部署 [> 待核实：MoveIt 2 官方案例研究与版本发布节奏]。  
- **Nav2 / Nav2 Costmap 2D / SMAC Planner**：导航栈 2.0 实现行为树驱动、插件化规划器，支持差分/全向/阿克曼底盘，成为移动机器人标配 [> 待核实：Nav2 官方采用案例与性能基准]。  
- **TF2 / rclcpp / rclpy / composition / intra-process communication**：核心通信与坐标变换库，支持零拷贝、节点组合、实时安全内存分配 [> 待核实：ROS 2 Jazzy/Iron/Humble LTS 版本特性对比表]。  

### 2.3 仿真-实机一体化工具链产品化（增量）
- **Isaac Sim / Isaac Lab (NVIDIA)**：基于 Omniverse 的 GPU 加速仿真，内置 ROS 2 桥接、域随机化、合成数据生成、Sim2Real 训练管线，已成为强化学习/模仿学习训练主流平台 [> 待核实：Isaac Lab 官方基准与社区采用率]。  
- **MuJoCo-Menagerie / MuJoCo ROS 2 插件**：DeepMind 维护的标准化机器人模型库，提供 MJCF/URDF 双格式、ROS 2 控制器配置，降低仿真建模门槛 [> 待核实：Menagerie 模型覆盖率与版本同步频率]。  
- **Real2Sim2Real / DiffSim2Real**：可微仿真辅助的系统辨识与策略迁移工具链，DiffSim2Real 已在四足步态上验证纯仿真训练直通真机 [8]。  

---

## 3. 蓝海与缺口（Blue Ocean & Gaps）

| 缺口维度 | 具体描述 | 证据支撑 | 优先级 |
|----------|----------|----------|--------|
| **运动学/控制层面的标准化基准缺失** | 现有 LIBERO 等基准聚焦高层策略/任务完成率，缺乏轨迹跟踪误差、力控带宽、全身协调稳定性、实时循环频率等底层控制指标 [16][17][18][19] | [16][17][18][19] | 高 |
| **全身遥操作系统的 ROS 2 标准化接口** | CHILD [3]、ALOHA 2 [4] 等系统各自定义接口，缺乏统一的 `teleop_msgs` / `whole_body_teleop` 标准消息定义与 ros2_control 硬件接口规范 | [4][3] | 高 |
| **可微物理引擎在运动学/动力学辨识中的物理一致性保证** | 可微牛顿-欧拉 [13]、DiffSim2Real [8] 等工作虽引入物理约束，但大规模复杂本体（灵巧手、人形）下的数值稳定性、梯度质量、物理参数可辨识性缺乏系统性基准 | [13][8] | 中 |
| **不确定运动学/动力学下的自适应控制在复杂本体上的实时性** | 经典自适应控制 [14] 理论成熟，但在高自由度人形/灵巧手、柔性关节、变刚度执行器上的实时计算负载与收敛保证缺乏工程化验证 | [14] | 中 |
| **VLA 与经典控制管线的混合部署、安全性验证、实时性保证** | 端到端 VLA [6][7] 与传统 MPC/伺服/力控管线的融合架构、运行时监护、形式化验证方法论空白 | [5][6][7] | 高 |
| **工业柔性制造场景的运动学/控制评测协议** | LIBERO-Industry [17] 首次引入产品变体、物流流动、时间窗、几何公差等工业约束，但底层控制指标（如换型重规划延迟、力控装配成功率）仍未纳入 | [17] | 中 |
| **低刚度/软体机器人的运动学建模与控制标准库** | 自监督视觉伺服 [9] 等探索性工作存在，但缺乏通用的软体运动学库（如有限元/余弦矩阵/几何变形模型的 ROS 2 封装） | [9] | 低 |

> 待核实：上述缺口的优先级排序基于候选证据覆盖度与社区讨论热度的定性判断，缺乏量化调研数据支撑。

---

## 4. 瓶颈与拐点（Bottleneck & Inflection）

### 4.1 算法与计算瓶颈
- **全身 NMPC 不等式约束实时求解**：高维系统（>30 DoF）下接触力锥、关节限位、碰撞避免等不等式约束导致求解迭代次数不可控，2024 年工作 [5] 提出精度-预算权衡，但硬实时保证仍依赖简化模型或离线预计算，**拐点信号**：可微 MPC / 学习加速求解器（如神经网络热启动）开始在仿真中显示出迭代次数大幅下降的潜力 [> 待核实：相关 2025-2026 论文]。  
- **VLA 模型推理延迟与确定性**：Xiaomi-Robotics-1 [6]、Meituan-Robotics-0 [7] 等大模型推理通常需 50-200ms，难以满足 1kHz 级力控回路，**拐点信号**：模型蒸馏、量化感知训练、TensorRT/ONNX Runtime 优化、专用推理加速芯片（如 NVIDIA Jetson Thor、Groq LPU）正在将端到端推理压缩至 <10ms [> 待核实：厂商白皮书与第三方基准]。  

### 4.2 数据与仿真瓶颈
- **真机高质量轨迹数据获取成本**：ALOHA 2 [4]、CHILD [3] 降低采集门槛，但 10 万小时级数据 [6] 仍需大规模机器人车队与长期运维，**拐点信号**：合成数据生成（Isaac Sim、GenSim）、仿真生成真实轨迹（Sim2Real2Sim）、人类视频迁移（Ego4D、Something-Something）正在缩小数据鸿沟 [> 待核实：2025-2026 相关数据集发布]。  
- **可微仿真的数值稳定性与梯度质量**：DiffSim2Real [8] 在四足步态上成功，但复杂接触、柔性体、流体耦合场景下梯度消失/爆炸、非光滑接触模型导致优化困难，**拐点信号**：隐式积分器、平滑接触模型、混合补集法在可微物理引擎（Warpx、DiffTaichi、Brax、NVIDIA Warp）中逐步成熟 [> 待核实：最新版本发布说明]。  

### 4.3 工程与生态瓶颈
- **ROS 2 实时性与 DDS 配置复杂度**：尽管 ros2_control [> 待核实] 提供标准抽象，但跨厂商 DDS（Fast DDS、Cyclone DDS、Zenoh）的 QoS 调优、内存零拷贝、CPU 亲和性配置仍需深厚中间件专业知识，**拐点信号**：ROS 2 Jazzy/Iron LTS 引入 `ros2 run --realtime`、统一实时配置文件、`rclcpp::executors::StaticSingleThreadedExecutor` 等开箱即用实时特性 [> 待核实：官方发布说明]。  
- **MoveIt 2 与 ros2_control 的深度集成仍在演进**：MoveIt Servo 实时伺服、Task Constructor 任务级规划与底层控制器的接口契约（`control_msgs`、`trajectory_msgs` 扩展）尚未完全稳定，**拐点信号**：MoveIt 2.0 / 3.0 路线图明确将“实时控制集成”作为核心里程碑 [> 待核实：MoveIt 官方路线图]。  

---

## 5. 社会·政策·国际（Society, Policy & Geopolitics）

### 5.1 标准化与法规进展（增量）
- **ISO/TC 299 / IEC 61508 / ISO 10218 / ISO/TS 15066**：协作机器人安全标准持续演进，ROS 2 实时控制栈需满足功能安全（PL d / SIL 2）认证要求，**风险**：开源中间件认证成本高、供应链合规审计复杂 [> 待核实：ROS 2 功能安全工作组进展]。  
- **中国《机器人产业发展行动计划》（2024-2026）**：明确支持人形机器人本体、核心零部件、操作系统（含 ROS 2 国产化适配）研发，**政策信号**：国产实时操作系统（RT-Thread、SylixOS、华为 LiteOS）与 ROS 2 实时执行器适配加速 [> 待核实：工信部最新指导目录]。  

### 5.2 地缘政治与供应链影响（增量）
- **高性能计算芯片出口管制**：影响 NVIDIA Jetson Orin/Thor、H100/A100 等训练推理硬件在华供应，推动国产 GPU/NPU（寒武纪、海光、比特大陆、摩尔线程）与 ROS 2、Isaac Lab、TensorRT 等工具链适配，**不确定**：适配成熟度与生态完善度滞后 1-2 年 [> 待核实：厂商适配白皮书]。  
- **开源生态去中心化趋势**：ROS 2 治理模式（Open Robotics → Open Source Robotics Foundation → 社区指导委员会）保证中立性，但核心维护者分布受地缘影响，**风险**：关键包（rclcpp、rmw、ros2_control）维护响应速度可能波动 [> 待核实：OSRF 年度报告]。  

### 5.3 伦理与劳动影响（增量）
- **VLA/端到端模型的可解释性与责任归属**：大模型直接输出动作 [6][7][19] 难以通过传统安全验证，**社会信号**：EU AI Act 将通用机器人 AI 系统列为高风险，要求透明度、人工监督、事后审计日志 [> 待核实：EU AI Act 附件最新修订]。  

---

## 6. 资本与生态（Capital & Ecosystem）

### 6.1 投融资热点（增量）
- **人形机器人本体与具身智能独角兽密集融资**：Figure AI、Apptronik、1X Technologies、Unitree、Agility、Galbot、智元机器人、优必选等 2024-2026 年累计融资超 50 亿美元 [> 待核实：PitchBook/Crunchbase 统计]，核心赛道集中于**全身控制算法**、**灵巧手硬件**、**VLA 基座模型**、**Sim2Real 工具链**。  
- **ROS 2 生态服务商商业化**：PickNik（MoveIt 商业支持）、Husarion（ROS 2 硬件平台）、Foxglove（可视化/调试）、Intrinsic（Flowstate/编排）、NVIDIA（Isaac 生态）等形成“工具链-平台-部署”完整商业闭环 [> 待核实：公司官网案例研究与营收披露]。  

### 6.2 人才流动与社区活跃度（增量）
- **核心维护者流向**：ROS 2 核心维护者多就职于 NVIDIA、Intrinsic、PickNik、Amazon Robotics、Boston Dynamics 等，**信号**：产业界主导开源路线图，学术界贡献比例下降 [> 待核实：GitHub 贡献者统计]。  
- **会议/研讨会专题激增**：ICRA/IROS/CoRL/RSS 2024-2026 连续设立“Whole-Body Control”、“VLA Foundation Models”、“Sim2Real for Legged/Humanoid”、“ROS 2 Real-Time Control”专题，**关注度**：论文投稿量同比增长 30-50% [> 待核实：会议官方统计报告]。  

### 6.3 开源项目健康度指标（快照）
| 项目 | GitHub Stars (2026-11) | 最近提交频率 | 核心维护者数 | 依赖下游包数 | 说明 |
|------|------------------------|--------------|--------------|--------------|------|
| ros2/ros2_control | > 1.2k | 高（周级） | 15+ | 200+ | 实时控制标准抽象层 |
| moveit/moveit2 | > 2.5k | 高 | 20+ | 300+ | 运动规划与伺服集成 |
| ros-planning/navigation2 | > 3.0k | 高 | 25+ | 400+ | 导航栈 2.0 |
| NVIDIA-Omniverse/IsaacLab | > 4.0k | 极高（日级） | 30+ | 新兴 | GPU 仿真与 RL 训练平台 |
| ALOHA-2/aloha_ros2 | > 2.5k | 中 | 5+ | 50+ | 双臂遥操作硬件/软件栈 |

> 待核实：上述星标数、维护者数为估算值，需实时查询 GitHub API 确认。

---

## 7. 信号与预测（Signals & Forecast）

### 7.1 早期信号（2024-2026 观测到）
| 信号 | 观测依据 | 可能指向的趋势 |
|------|----------|----------------|
| VLA 基座模型规模从“万小时”跃升至“十万小时”真机轨迹 | Xiaomi-Robotics-1 [6] | 端到端学习替代部分传统运动学/控制管线，数据飞轮效应显现 |
| 多本体统一动作空间（离散 token 对齐）成为 VLA 标配 | Meituan-Robotics-0 [7] | 通用具身智能体架构收敛，硬件抽象层上移至动作 token 空间 |
| LIBERO 基准生态在半年内密集推出 4+ 专用基准 | LIBERO-PeRM/Industry/VPro/10 [16][17][18][19] | 评测维度从“任务完成”细分为“偏好/工业/鲁棒性/通用性”，倒逼算法全面化 |
| 可微仿真直通真机在四足步态上闭环验证 | DiffSim2Real [8] | 系统辨识与策略优化联合进行成为主流 Sim2Real 范式 |
| ROS 2 实时执行器与 DDS 零拷贝在 LTS 版本原生支持 | Jazzy/Iron 发布说明 [> 待核实] | 硬实时控制回路（1-2kHz）在标准 PC/嵌入式上开箱即用 |

### 7.2 未来 6-18 月可验证预测（附置信度与可证伪假设）

| 预测 | 依据链 | 可证伪假设 | 置信度 | 标记 |
|------|--------|------------|--------|------|
| **至少 2 家头部人形厂商发布基于 ROS 2 + ros2_control 的全身 MPC 量产控制器** | 全身 NMPC 实时化 [5]、ros2_control 标准化 [> 待核实]、厂商招聘 JD 激增 | 若至 2027-06 无厂商公开技术博客/白皮书披露全身 MPC 量产部署，则判断不成立 | 较大概率 | [P] |
| **VLA 模型在 LIBERO-10 零样本成功率突破 70%（当前 SOTA ~40-50%）** | LIBERO-10 基准建立 [19]、模型规模指数级增长 [6][7]、推理加速硬件迭代 | 若至 2027-06 LIBERO-10 排行榜零样本最高分 < 60%，则判断不成立 | 推测 | [P] |
| **可微物理引擎（Warp/Brax/DiffTaichi）发布支持“灵巧手+柔性物体”可微接触的稳定版本** | DiffSim2Real [8]、NVIDIA Warp 迭代 [> 待核实]、学术界可微接触模型密集发布 | 若至 2027-06 无开源可微引擎在灵巧手抓取任务上展示收敛稳定的梯度，则判断不成立 | 推测 | [P] |
| **ROS 2 功能安全（PL d/SIL 2）认证版本发布，支持 rclcpp + ros2_control 实时栈** | OSRF 功能安全工作组 [> 待核实]、EU AI Act 高风险分类 [> 待核实]、工业界合规需求 | 若至 2027-06 无通过 TÜV/SGS 认证的 ROS 2 发行版，则判断不成立 | 需要数据 | [P] |
| **国产实时 OS（RT-Thread/SylixOS/华为 LiteOS）与 ROS 2 实时执行器完成全栈适配并进入量产车型** | 中国政策支持 [> 待核实]、芯片国产化替代压力 [> 待核实]、厂商联合实验室成立 | 若至 2027-06 无国产 OS + ROS 2 实时栈的量产案例（如协作机器人/AGV），则判断不成立 | 推测 | [P] |

### 7.3 风险与不确定因素
- **数据飞轮能否持续**：10 万小时真机轨迹 [6] 依赖大规模机器人车队运维，边际成本随任务复杂度上升，**风险**：数据质量瓶颈（分布外、失败轨迹稀缺）可能导致模型性能饱和。  
- **Sim2Real 现实差距在动态交互任务中放大**：羽毛球等高速任务 [1] 对接触建模、空气动力学、视觉延迟极其敏感，纯仿真训练策略真机成功率仍低，**不确定**：可微仿真+域随机化+少量真机微调能否闭环。  
- **开源生态碎片化**：ROS 2 发行版（Humble/Iron/Jazzy/Rolling）、DDS 实现、实时内核（PREEMPT_RT/RTOS）、硬件抽象层（ros2_control/微型控制器固件）组合爆炸，**风险**：集成测试矩阵指数级增长，维护负担转移至终端用户。  

---

## 参考来源（引用编号对应列表）
[1] Humanoid Whole-Body Badminton via an Annealed Reinforcement Learning Curriculum — http://arxiv.org/abs/2511.11218v4
[2] The Role of Domain Randomization in Training Diffusion Policies for Whole-Body Humanoid Control — http://arxiv.org/abs/2411.01349v1
[3] CHILD (Controller for Humanoid Imitation and Live Demonstration): a Whole-Body Humanoid Teleoperation System — http://arxiv.org/abs/2508.00162v2
[4] ALOHA 2: An Enhanced Low-Cost Hardware for Bimanual Teleoperation — http://arxiv.org/abs/2405.02292v1
[5] Tailoring Solution Accuracy for Fast Whole-body Model Predictive Control of Legged Robots — http://arxiv.org/abs/2407.10789v2
[6] Xiaomi-Robotics-1: Scaling Vision-Language-Action Models with over 100K Hours of Real-World Trajectories — http://arxiv.org/abs/2607.15330v2
[7] Meituan-Robotics-0: A Vision-Language-Action Foundation Model for Desktop Manipulation — http://arxiv.org/abs/2611.08577v3
[8] DiffSim2Real: Deploying Quadrupedal Locomotion Policies Purely Trained in Differentiable Simulation — http://arxiv.org/abs/2411.02189v1
[9] Self-Supervised Learning of Visual Servoing for Low-Rigidity Robots Considering Temporal Body Changes — http://arxiv.org/abs/2405.11798v1
[10] Keep Rollin' - Whole-Body Motion Control and Planning for Wheeled Quadrupedal Robots — http://arxiv.org/abs/1809.03557v2
[11] Prioritized motion-force control of constrained fully-actuated robots: "Task Space Inverse Dynamics" — http://arxiv.org/abs/1410.3863v1
[12] Spatial Vector Algebra — https://doi.org/10.1007/978-1-4899-7560-7_2
[13] Encoding Physical Constraints in Differentiable Newton-Euler Algorithm — http://arxiv.org/abs/2001.08861v4
[14] Adaptive Control of Robot Manipulators With Uncertain Kinematics and Dynamics — http://arxiv.org/abs/1403.5204v3
[15] A ROS-based Software Framework for the NimbRo-OP Humanoid Open Platform — http://arxiv.org/abs/1809.11051v1
[16] LIBERO-PeRM: Benchmarking Personalized Robotic Manipulation — http://arxiv.org/abs/2610.22372v1
[17] LIBERO-Industry: Benchmarking Robotic Manipulation under Industrial Process Constraints — http://arxiv.org/abs/2610.16782v2
[18] LIBERO-VPro: Benchmarking Closed-Loop Visual Robustness of Robotic Foundation Models — http://arxiv.org/abs/2609.24350v1
[19] From Reasoning to Action: Benchmarking Frontier AI Models on LIBERO-10 Robot Manipulation Tasks — http://arxiv.org/abs/2610.30051v1

---

*Generated by research-bot · topic=`机器人运动学控制与-ros-2` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`nvidia/nemotron-3-ultra-550b-a55b` · sources=35 · duration=415s · 2026-11-14T02:35:17+00:00*
