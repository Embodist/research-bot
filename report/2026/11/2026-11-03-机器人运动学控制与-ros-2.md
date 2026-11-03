# 机器人运动学、控制与 ROS 2 生态：2024-2026 年增量调研快照

**日期**：2026-11-03 | **领域**：具身智能 / 机器人运动学与控制 / ROS 2 工程生态 | **检索源数量**：33 条可引用证据源

---

## 1. 进展与热点

### 1.1 学术前沿：感知为主、控制/ROS 2 集成论文稀缺（增量判断）
- **ICRA 2025 GOOSE 3D 语义分割挑战赛** 聚焦异构机器人平台的非结构化户外点云语义分割，获胜方案采用 **Point Prompt Tuning (PPT) + Point Transformer** [11]。  
  - *热度证据*：ICRA 顶会挑战赛官方技术报告 [11]；*权威证据*：ICRA 2025 主办，同行评审挑战赛流程；*关注度*：中（领域聚焦感知而非运动学/控制/ROS2）[11]；*推荐度*：★★★☆☆（多平台点云数据集可供迁移学习参考，非核心运动学/控制进展）[11]。
- **通用机器人操作策略真机基准设计讨论** 指出仿真基准显著领先而真机评测滞后，呼吁从 sim-to-real 视角建立评测体系 [12]。  
  - *热度证据*：arXiv 预印本讨论热点 [12]；*权威证据*：arXiv cs.RO 预印本，未经同行评审；*关注度*：中（针对评测痛点的讨论性工作）[12]；*推荐度*：★★★☆☆（了解基准建设缺口的参考，非具体算法进展）[12]。
- **核心缺口**：候选证据中**缺乏 2024-2026 年机器人运动学建模、全身控制/MPC/RL 控制、ROS 2 实时控制集成（ros2_control、微内核、DDS 调优）的最新论文、基准与数据集** [11, 12]。> 待核实：是否存在未被检索到的运动学/控制顶会论文。

### 1.2 大规模真机数据驱动 VLA 训练（关键增量）
- **小米发布 Xiaomi-Robotics-1**，使用 **100K+ 小时真机轨迹** 两阶段预训练+后训练，实现零样本泛化与少样本适配 [22]。  
  - *热度证据*：arXiv 预印本，头部厂商大规模真机工作 [22]；*权威证据*：arXiv cs.RO 预印本，未经同行评审；*关注度*：高（定义真机数据规模化新基线）[22]；*推荐度*：★★★★★（必读，直接关联运动控制数据瓶颈）[22]。

### 1.3 ROS 2 跨域扩展：航天与海洋（增量信号）
- **Basilisk 天体动力学框架与 ROS 2 轻量级双向桥接**，支持编队飞行仿真与平面微重力试验台实机部署一致性 [24]。  
  - *热度证据*：arXiv 预印本 [24]；*权威证据*：arXiv cs.RO 预印本；*关注度*：中（航天领域 ROS 2 采用里程碑）[24]；*推荐度*：★★★★☆（仿真实一体化工程参考价值高）[24]。
- **OtterROS 为无人艇提供开源 ROS 2 完整栈并完成野外实验**，拓展非结构化环境下运动控制实践 [23]。  
  - *热度证据*：arXiv 预印本 [23]；*权威证据*：arXiv cs.RO 预印本；*关注度*：中（海洋机器人 ROS 2 罕见完整案例）[23]；*推荐度*：★★★☆☆（跨域参考价值，领域特异性强）[23]。

### 1.4 经典与奠基性工作（表格汇总）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| Inherently Robust Economic MPC Without Dissipativity | 2024 | arXiv | > 待核实 | 预印本 | 低 | ★★☆☆☆ | [3] | 理论 MPC 鲁棒性，非 ROS2 专用 |
| Preconditioning for Continuation MPC | 2015 | arXiv | > 待核实 | 预印本 | 低 | ★★☆☆☆ | [4] | MPC 数值求解经典 |
| Asynchronous Splitting Design for MPC | 2016 | arXiv | > 待核实 | 预印本 | 低 | ★★☆☆☆ | [5] | 分布式 MPC 算法基础 |
| Output-Feedback MPC with Online Identification | 2020 | arXiv | > 待核实 | 预印本 | 低 | ★★☆☆☆ | [6] | 自适应 MPC 方向 |
| Hybrid GP Modeling for Economic Stochastic MPC | 2021 | arXiv | > 待核实 | 预印本 | 低 | ★★☆☆☆ | [7] | 数据驱动 MPC 早期探索 |
| Uncertainty-Cognizant MPC for Energy Management | 2022 | arXiv | > 待核实 | 预印本 | 低 | ★★☆☆☆ | [8] | 不确定性感知 MPC 应用 |
| Balancing Risk Averseness in MPC for Flood Control | 2024 | arXiv | > 待核实 | 预印本 | 低 | ★★☆☆☆ | [9] | 风险敏感 MPC |
| Learning-based NMPC for Go-Kart (GP Dynamics) | 2023 | arXiv | > 待核实 | 预印本 | 中 | ★★★☆☆ | [10] | 真机部署学习型 NMPC 稀有案例 |
| Grasp and Motion Planning for Dexterous Manipulation | 2021 | arXiv | > 待核实 | 预印本 | 中 | ★★★☆☆ | [16] | 灵巧手规划基准参考 |
| Impact of ROS 2 Node Composition | 2023 | arXiv | > 待核实 | 预印本 | 中 | ★★★☆☆ | [26] | ROS 2 节点组合性能分析 |
| RoboKube: Cloud Native Evolution in Robotics | 2024 | arXiv | > 待核实 | 预印本 | 中 | ★★★★☆ | [27] | 云原生机器人架构奠基 |
| TSN for Industrial Automation: Advances & Directions | 2023 | arXiv | > 待核实 | 综述预印本 | 高 | ★★★★☆ | [33] | 工业实时网络标准演进 |

---

## 2. 工业界与产品

### 2.1 ROS 2 真机部署工程实践（现有证据覆盖）
- **自适应 ROS 2 节点部署框架** 面向移动边缘-机器人系统，在 IROS 2025 发表，验证边缘侧动态部署可行性 [20]。  
  - *热度证据*：IROS 2025 会议论文 [20]；*权威证据*：IEEE IROS 同行评审；*关注度*：中（边缘部署工程化参考）[20]；*推荐度*：★★★★☆（ROS 2 分布式部署工程范式）。
- **基于 ROS 2 的工业物料搬运自主移动机器人实现**，含实时导航验证 [21]。  
  - *热度证据*：ResearchSquare 预印本 [21]；*权威证据*：预印本平台，未经同行评审；*关注度*：中（工业落地案例）[21]；*推荐度*：★★★☆☆（ROS 2 Navigation 2 工程化参考）。
- **ROS 2 节点组合对机器人系统性能影响** 量化分析，指导实时系统设计 [26]。  
  - *热度证据*：arXiv 预印本 [26]；*权威证据*：预印本；*关注度*：中（性能调优参考）[26]；*推荐度*：★★★☆☆（ros2_control/Composition 实时性调优依据）。

### 2.2 主流开源栈成熟度与商业化（证据缺口）
- **MoveIt 2 / ros2_control / Nav2 / Micro-ROS / Isaac ROS** 的商业化产品进展、真机成熟度量化指标（MTBF、延迟分布、安全认证）**在现有证据中无直接覆盖** [11, 12, 20, 21, 22, 23, 24, 26, 27]。  
  > 待核实：各栈最新 LTS 版本支持周期、主要 OEM 采用案例、功能安全（ISO 13849/ISO 26262）认证进度。
- **RoboKube** 提出云原生机器人新基座，标志生态向 Kubernetes 边缘编排演进 [27]。  
  - *热度证据*：arXiv 预印本 [27]；*权威证据*：预印本；*关注度*：中（云原生机器人架构趋势）[27]；*推荐度*：★★★★☆（生态演进信号）。

### 2.3 开源项目成熟度速览（表格，指标待核实）

| 名称 | 年份 | 机构/维护者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-------------|------|------|--------|--------|------|------|
| MoveIt 2 | > 待核实 | PickNik / Community | > 待核实 | 官方文档/ROS 2 核心库 | 高 | ★★★★★ | > 待核实 | 运动规划标准栈，ROS 2 迁移中 |
| ros2_control | > 待核实 | ROS 2 Controls Community | > 待核实 | 官方文档/ROS 2 核心库 | 高 | ★★★★★ | > 待核实 | 实时控制器管理框架核心 |
| Nav2 | > 待核实 | Steve Macenski / Community | > 待核实 | 官方文档/ROS 2 核心库 | 高 | ★★★★★ | > 待核实 | 导航标准栈，行为树架构 |
| Micro-ROS | > 待核实 | eProsima / OFERA | > 待核实 | 官方文档/微控制器移植 | 中 | ★★★★☆ | > 待核实 | 资源受限平台 ROS 2 子集 |
| Isaac ROS | > 待核实 | NVIDIA | > 待核实 | 官方文档/GPU 加速包 | 高 | ★★★★★ | > 待核实 | 感知/规划 GPU 加速生态 |
| RoboKube | 2024 | arXiv 作者团队 | > 待核实 | 预印本 [27] | 中 | ★★★★☆ | [27] | 云原生编排原型 |

---

## 3. 蓝海与缺口

### 3.1 跨本体统一运动学/控制抽象层缺失（核心蓝海）
- **现状**：Basilisk-ROS2 [24]、OtterROS [23] 均为点对点适配，**未形成通用中间件层** 支持机械臂/灵巧手/移动底盘/水下/航天统一接口 [24, 23]。  
  - *热度证据*：两篇跨域论文工程现象归纳 [24, 23]；*权威证据*：基于论文观察的工程归纳；*关注度*：中（社区普遍痛点）[24, 23]；*推荐度*：★★★★☆（指向高杠杆机会：构建跨本体统一 ROS 2 运动学/控制抽象层）[24, 23]。

### 3.2 真机大规模数据工程化工具链缺位
- **小米 100K+ 小时轨迹** 暗示头部厂商具备数据规模化能力，但**采集、标注、清洗的标准化低成本工具链对外不可见** [22]。  
  - *热度证据*：论文披露数据规模 [22]；*权威证据*：arXiv 预印本；*关注度*：高（具身智能商业化护城河）[22]；*推荐度*：★★★★★（数据自动化/仿真迁移/联邦学习将在 6-18 个月爆发）[22]。

### 3.3 仿真-实机一致性验证基准与 CI/CD 缺失
- 尽管 Basilisk [24]、OtterROS [23] 展示一致性部署，但**通用验证基准、自动化回归流程在 ROS 2 生态中缺位** [24, 23]。  
  > 待核实：是否存在开源的 sim2real CI/CD 模板（如基于 GitHub Actions + Isaac Sim / Gazebo + 真机硬件农场）。

### 3.4 分布式边缘-云架构下实时控制确定性保障
- **车路协同边缘计算 (VEC)** 场景下，无线信道波动与算力约束导致任务卸载与资源调度成为运动控制链路瓶颈 [31]。  
  - *热度证据*：arXiv cs.DC 预印本 [31]；*权威证据*：预印本；*关注度*：低（通信视角，与运动控制核心关联中等）[31]；*推荐度*：★★★☆☆（提示分布式算力下实时控制新挑战）[31]。

### 3.5 VLA 真机部署的安全性、可解释性与硬实时约束
- 端到端 VLA 模型在真机部署时，**安全性验证、可解释性、硬实时调度（如 ros2_control 回路频率 > 1kHz）缺乏成熟方案** [22]。  
  > 待核实：是否有结合形式化验证、运行时监护的 VLA 部署框架开源。

---

## 4. 瓶颈与拐点

### 4.1 核心瓶颈：真机数据规模与获取成本（供应链瓶颈）
- **小米 100K+ 小时** 真机轨迹训练 VLA，确立**数据规模法则** 在具身智能的有效性，但中小团队面临**数据护城河** [22]。  
  - *热度证据*：论文披露规模 [22]；*权威证据*：arXiv 预印本；*关注度*：高（直接关联商业化竞争格局）[22]；*推荐度*：★★★★★（核心瓶颈，驱动数据自动化/仿真迁移技术爆发）[22]。

### 4.2 算法瓶颈：碎片化驱动与缺乏统一硬件抽象层 (HAL)
- 跨域适配（航天 [24]、海洋 [23]）均为**定制化桥接**，未复用通用 `ros2_control` Hardware Interface 体系，导致**重复造轮子、实时性难保证** [24, 23]。  
  - *热度证据*：两篇论文工程现象 [24, 23]；*权威证据*：工程归纳；*关注度*：中；*推荐度*：★★★★☆（推动 ros2_control 向非标本体扩展的标准化工作）。

### 4.3 网络/通信瓶颈：TSN/5G 确定性与 ROS 2 DDS 融合
- **TSN (IEEE 802.1Qbv) 与 5G 融合** 实验评估显示混合系统可行性，但调度复杂度高 [28, 30, 33]。  
  - *热度证据*：多篇 TSN 实验/综述论文 [28, 30, 33]；*权威证据*：arXiv 预印本/综述；*关注度*：高（工业自动化确定性网络标准演进）[33]；*推荐度*：★★★★☆（ROS 2 DDS over TSN/5G 是实时分布式控制关键拐点）[28, 30, 33]。
- **DoS 防护与信用计量机制** 在车载 TSN 中被仿真验证，提示安全性是实时网络新维度 [29]。  
  > 待核实：ROS 2 DDS Security 插件在 TSN 环境下的性能开销实测。

### 4.4 拐点信号：大规模真机数据 → VLA 泛化能力跃迁
- **Xiaomi-Robotics-1** 以 100K 小时数据实现零样本泛化，标志**“数据规模 > 模型架构微创新”** 成为当前主导范式 [22]。  
  - *预测*：未来 12 个月，头部厂商将竞相发布 500K-1M 小时级数据集，**数据采集自动化（自主探索、人机协同遥操作批量化）将成为核心竞争力** [P, 置信度 0.8] [22]。

---

## 5. 社会·政策·国际

### 5.1 标准化与供应链信号（证据间接）
- **TSN (IEEE 802.1Qbv) 国际标准演进** 与工业自动化融合加速，中国在 IEC/IEEE 标准制定中话语权上升 [33]。  
  - *热度证据*：TSN 综述论文 [33]；*权威证据*：arXiv 综述预印本；*关注度*：高（关乎实时控制网络自主可控）[33]；*推荐度*：★★★★☆（政策层面关注工业互联网标准自主化）。
- **ROS 2 作为事实上的机器人软件标准**，其 DDS 实现（Fast DDS, Cyclone DDS, Zenoh）的**供应链安全（国产化替代）** 成为潜在政策关注点 [26, 27]。  
  > 待核实：是否有明确政策文件指向 ROS 2/DDS 国产化替代清单。

### 5.2 跨域应用拓展的社会价值
- **航天 (Basilisk-ROS2) [24]、海洋 (OtterROS) [23]** 验证 ROS 2 在极端环境（微重力、非结构化水面）的鲁棒性，支撑深空探测、深海作业等国家战略需求。  
  - *热度证据*：两篇应用论文 [24, 23]；*权威证据*：arXiv 预印本；*关注度*：中；*推荐度*：★★★★☆（展示 ROS 2 生态战略广度）。

### 5.3 地缘政治与人才流动
- 现有证据**无直接覆盖** 芯片禁令对 ROS 2 实时控制器硬件选型（如 NVIDIA Jetson, Xilinx/AMD MPSoC, 国产 GPU/NPU）的影响。  
  > 待核实：国产芯片（华为昇腾、寒武纪、地平线等）对 `ros2_control` / `Isaac ROS` / `Micro-ROS` 的适配成熟度。

---

## 6. 资本与生态

### 6.1 头部厂商数据资本化投入（强信号）
- **小米投入 100K+ 小时真机采集** [22]，暗示**单项目数据获取成本达千万级人民币**，形成高准入壁垒。  
  - *热度证据*：论文披露 [22]；*权威证据*：arXiv 预印本；*关注度*：高；*推荐度*：★★★★★（资本密集型竞争格局已形成）。

### 6.2 云原生机器人生态雏形
- **RoboKube** [27] 提出 Kubernetes 原生机器人运行时，标志**资本开始关注“机器人即服务”基础设施层**（边缘编排、多租户、OTA）。  
  - *热度证据*：arXiv 预印本 [27]；*权威证据*：预印本；*关注度*：中；*推荐度*：★★★★☆（生态基建投资方向）。

### 6.3 开源生态商业化路径分化
- **NVIDIA Isaac ROS** 以 GPU 加速生态绑定硬件销售；**PickNik (MoveIt 2)** 走专业服务/商业许可；**eProsima (Micro-ROS/Fast DDS)** 走中间件商业支持。  
  > 待核实：2024-2026 年上述主体融资轮次、营收占比、社区贡献者活跃度量化对比。

### 6.4 人才与社区信号
- **ROS 2 核心仓库贡献者集中度高**，维护者倦怠风险存在；**Micro-ROS/Zephyr 社区** 嵌入式方向活跃度上升 [26, 27]。  
  > 待核实：GitHub Insights 量化数据（PR 延迟、Issue 积压、核心维护者变动）。

---

## 7. 信号与预测

### 7.1 早期信号汇总
| 信号 | 来源 | 时间 | 强度 | 说明 |
|------|------|------|------|------|
| 100K+ 小时真机轨迹训练 VLA 零样本泛化 | [22] | 2026-07 | 高 | 数据规模法则在具身智能验证 |
| ROS 2 进入航天高保真仿真-实机一体化流程 | [24] | 2025-12 | 中 | 非传统领域采用里程碑 |
| ROS 2 完整栈支撑无人艇野外长时实验 | [23] | 2024-04 | 中 | 海洋机器人开源罕见案例 |
| 车路协同边缘计算实时卸载成为控制链路瓶颈 | [31] | 2025-12 | 低 | 分布式实时控制新挑战 |
| TSN/5G 融合实验验证确定性网络可行性 | [28, 30, 33] | 2023-2024 | 高 | 工业实时网络标准落地加速 |

### 7.2 未来 6-18 月可验证预测（含不确定性与风险）

| # | 预测 (可证伪假设) | 依据链 | 置信度 | 验证指标/截止时间 | 风险/不确定因素 |
|---|-------------------|--------|--------|-------------------|-----------------|
| P1 | **至少 2 家头部中企（如小米、优必选、智元、追觅）发布 ≥500K 小时真机轨迹数据集或等效合成数据声明** | Xiaomi 100K 基线 [22] → 规模竞争逻辑 | 0.8 | 2027-05 前 arXiv/官网/发布会公开数据规模 | 数据隐私合规、采集成本超预期、合成数据替代真机 |
| P2 | **`ros2_control` 官方合并跨本体（移动底盘+机械臂+灵巧手）统一 Hardware Interface 规范 PR** | 碎片化痛点 [24, 23] → 社区标准化需求 | 0.6 | 2027-05 前 ros2_control GitHub Releases / ROS 2 Jazzy/Kilted 发布说明 | 维护者带宽、厂商利益博弈、实时性与通用性权衡 |
| P3 | **首个基于 ROS 2 + TSN/5G 的工业级分布式实时控制系统（回路 >1kHz, 抖动 <10us）通过第三方认证 (如 TÜV/CCC)** | TSN/5G 融合进展 [28, 30, 33] + ROS 2 DDS 实时性探索 [26] | 0.5 | 2027-05 前 认证证书公示 / 白皮书 | DDS over TSN 协议栈成熟度、硬件供应链稳定性、标准版本锁定 |
| P4 | **VLA 模型在真机部署时引入形式化运行时监护成为顶会主流投稿方向** | VLA 安全性缺口 [22] + 学界安全关注度上升 | 0.7 | 2027-05 前 CoRL/ICRA/RSS 接收论文关键词统计 | 监护器设计复杂度、实时性开销、仿真验证覆盖率 |
| P5 | **Micro-ROS 在国产 MCU（如 GD32, CH32, 国产 RISC-V 核）上实现全功能 CI/CD 通过率 >90%** | 嵌入式国产化趋势 + Micro-ROS 架构解耦 | 0.5 | 2027-05 前 Micro-ROS 官方 CI 矩阵 / 社区报告 | 厂商 SDK 成熟度、DDS-XRCE 移植工作量、工具链兼容性 |

> **不确定性声明**：上述预测基于当前公开论文/预印本信号推演，**不构成投资建议**。关键风险在于：地缘政治导致供应链断供、大模型范式切换（如 World Model 取代 VLA）、资本退潮导致数据采集投入减少。

---

## 参考来源

[1] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1  
[2] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1  
[3] Inherently Robust Economic Model Predictive Control Without Dissipativity — http://arxiv.org/abs/2408.15743v1  
[4] Preconditioning for continuation model predictive control — http://arxiv.org/abs/1509.02861v1  
[5] Asynchronous Splitting Design for Model Predictive Control — http://arxiv.org/abs/1609.05801v1  
[6] Output-Feedback Model Predictive Control with Online Identification — http://arxiv.org/abs/2009.10631v1  
[7] Hybrid Gaussian Process Modeling Applied to Economic Stochastic Model Predictive Control of Batch Processes — http://arxiv.org/abs/2108.06430v1  
[8] Uncertainty-Cognizant Model Predictive Control for Energy Management of Residential Buildings with PVT and Thermal Energy Storage — http://arxiv.org/abs/2201.08909v1  
[9] Balancing Operators Risk Averseness in Model Predictive Control for Real-time Reservoir Flood Control — http://arxiv.org/abs/2407.04506v2  
[10] A Learning-based Nonlinear Model Predictive Controller for a Real Go-Kart based on Black-box Dynamics Modeling through Gaussian Processes — http://arxiv.org/abs/2305.17949v1  
[11] Technical Report for ICRA 2025 GOOSE 3D Semantic Segmentation Challenge: Adaptive Point Cloud Understanding for Heterogeneous Robotic Systems — http://arxiv.org/abs/2506.06995v1  
[12] Robot Policy Evaluation for Sim-to-Real Transfer: A Benchmarking Perspective — http://arxiv.org/abs/2508.11117v1  
[13] NTU-NPU System for Voice Privacy 2024 Challenge — http://arxiv.org/abs/2410.02371v1  
[14] NTIRE 2025 Challenge on Image Super-Resolution (x4): Methods and Results — http://arxiv.org/abs/2504.14582v3  
[15] JENGA: Exploiting Counter-Based RowHammer Countermeasures to Break Real-Time Predictability — http://arxiv.org/abs/2609.01077v1  
[16] Grasp and Motion Planning for Dexterous Manipulation for the Real Robot Challenge — http://arxiv.org/abs/2101.02842v1  
[17] One-Shot Reinforcement Learning for Robot Navigation with Interactive Replay — http://arxiv.org/abs/1711.10137v2  
[18] Users' Perception on Appropriateness of Robotic Coaching Assistant's Disclosure Behaviors — http://arxiv.org/abs/2410.10550v1  
[19] Which Depth Estimator for Jetson AGX Orin? A 2026 Benchmark of Monocular and Stereo Methods — http://arxiv.org/abs/2610.27199v1  
[20] An Adaptive ROS2 Node Deployment Framework in Mobile Edge-Robot Systems — https://doi.org/10.1109/iros60139.2025.11247728  
[21] Autonomous Mobile Robot for Industrial Material Handling: A ROS2-Based Implementation with Real-Time Navigation — https://doi.org/10.21203/rs.3.rs-7938184/v1  
[22] Xiaomi-Robotics-1: Scaling Vision-Language-Action Models with over 100K Hours of Real-World Trajectories — http://arxiv.org/abs/2607.15330v2  
[23] OtterROS: Picking and Programming an Uncrewed Surface Vessel for Experimental Field Robotics Research with ROS 2 — http://arxiv.org/abs/2404.05627v2  
[24] Bridging the Basilisk Astrodynamics Framework with ROS 2 for Modular Spacecraft Simulation and Hardware Integration — http://arxiv.org/abs/2512.09833v2  
[25] Action Flow Matching for Continual Robot Learning — http://arxiv.org/abs/2504.18471v2  
[26] Impact of ROS 2 Node Composition in Robotic Systems — http://arxiv.org/abs/2305.09933v1  
[27] RoboKube: Establishing a New Foundation for the Cloud Native Evolution in Robotics — http://arxiv.org/abs/2403.04440v1  
[28] Time-Sensitive Networking over 5G: Experimental Evaluation of a Hybrid 5G and TSN System with IEEE 802.1Qbv Traffic — http://arxiv.org/abs/2407.05989v1  
[29] DoS Protection through Credit Based Metering -- Simulation-Based Evaluation for Time-Sensitive Networking in Cars — http://arxiv.org/abs/1908.09646v2  
[30] Real-Time Scheduling for 802.1Qbv Time-Sensitive Networking (TSN): A Systematic Review and Experimental Study — http://arxiv.org/abs/2305.16772v4  
[31] Real-Time Service Subscription and Adaptive Offloading Control in Vehicular Edge Computing — http://arxiv.org/abs/2512.14002v1  
[32] A Survey of Scheduling Algorithms for the Time-Aware Shaper in Time-Sensitive Networking (TSN) — http://arxiv.org/abs/2211.10954v2  
[33] Time-Sensitive Networking (TSN) for Industrial Automation: Current Advances and Future Directions — http://arxiv.org/abs/2306.03691v4

---

*Generated by research-bot · topic=`机器人运动学控制与-ros-2` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`nvidia/nemotron-3-ultra-550b-a55b` · sources=33 · duration=268s · 2026-11-03T03:29:24+00:00*
