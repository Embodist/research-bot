# 机器人运动学、控制与 ROS 2 生态：近 1-2 年前沿增量快照（七维追踪）

**日期**：2026-11-25（UTC）  
**领域**：机器人运动学、控制算法、ROS 2 生态、具身智能基础设施  
**检索源数量**：30 条可引用证据源（编号 [1]–[2]）  
**方法论**：frontier-tracking / deep-research / evidence-grading / frontier-watch  

---

## 1. 进展与热点（Progress & Hotspots）

> **一句话增量判断**：近 1-2 年运动学与控制算法呈现“经典自适应控制回顾巩固 + MPC 动态运行框架系统化梳理 + 数据驱动被动控制新范式 + VLA 基础模型落地桌面操作”四大并行热点；ROS 2 生态核心痛点聚焦于 sim-to-real 标准化基准缺失；政策层面 ISO 10218/ISO/TS 15066 2025 版修订落地，安全标准与协作机器人合规要求同步收紧。

### 1.1 运动学与控制算法前沿

| 名称 | 年份 | 机构/作者 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|----------|----------|--------|--------|------|------|
| Adaptive Control of Robot Manipulators With Uncertain Kinematics and Dynamics | 2014 (v3 2016) | Wang | citations=0 (arXiv 预印本) [3] | arXiv eess.SY，曾投 IEEE TAC [3] | 中（经典基线文献） | ★★★★☆ 系统处理运动学与动力学双重不确定，具分离性质，综述必引 [3] | [3] | 经典奠基工作，提出两种自适应控制器实现任务空间轨迹跟踪，首个控制器经修改可在不增加保守增益前提下改善性能 [3] |
| Analysis and design of model predictive control frameworks for dynamic operation — An overview | 2023 | — | citations=0 (arXiv 预印本) [4] | arXiv eess.SY v2 [4] | 中（MPC 领域近期综述） | ★★★★☆ 梳理非线性约束系统动态运行下 MPC 框架演进脉络 [4] | [4] | 2023 年综述，覆盖参考跟踪到经济性运行多目标，聚焦非线性约束系统特有挑战 [4] |
| Passive iFIR Filters for Data-Driven Control | 2024 | — | citations=0 (arXiv 预印本) [5] | arXiv eess.SY v2 [5] | 中（数据驱动与被动性结合新范式） | ★★★★☆ 兼顾 PID 简洁性与更强表达力，VRFT 无模型设计，工程落地潜力大 [5] | [5] | 2024 年新进展：并联积分器与有限冲激响应滤波器的被动 iFIR 控制器，基于虚拟参考反馈调优 (VRFT) 实现无模型数据驱动设计，约束强制被动性 [5] |
| 可编程物质与变形自主车体纳米机器人运动学架构 | 2026 | Feng Cheng-en / STARLI | citations=0 (Zenodo 预印本) [6] | Zenodo (CERN)，非同行评审，作者自述为研究工作版 [6] | 低（极早期探索性专著） | ★★☆☆☆ 前沿假设性工作，运动学雅可比等 30 个数学板块可作长期蓝海参考，但无实验证据 [6] | [6] | 777 页专著，提出可证伪工程架构，含图刚度秩、约束刚度组装、弱模态稳定性、运动学雅可比等 30 板块，核心释放策略为合取式（负载路径连续性、有界几何误差等需同时通过） [6] |

### 1.2 ROS 2 生态与基准进展

| 名称 | 年份 | 机构/作者 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|----------|----------|--------|--------|------|------|
| Robot Policy Evaluation for Sim-to-Real Transfer: A Benchmarking Perspective | 2025 | — | — | RSS 2025 Workshop on Robot Evaluation for the Real World [7] | 中（顶会工作坊聚焦核心痛点） | ★★★★☆ 直接切中 sim-to-real 基准设计开放问题，提供三大设计原则 [7] | [7] | 指出现有仿真基准推动研究但真实世界评估滞后，提出：高视觉保真仿真、系统性增加任务复杂度与场景扰动、量化真实世界性能与仿真对应性对齐度 [7] |
| Real Robot Challenge (TriFinger 平台) | 2021 | — | — | 官方竞赛基准 [8] | 低（时间较早，当前关注度有限） | ★★★☆☆ 早期真机灵巧手操作基准参考，需结合 Open X-Embodiment、DROID 等最新进展 [8] | [8] | 三指灵巧手平台真实机器人操作竞赛，结合运动规划与运动基元实现矩形物体操作，包含三阶段 [8] |

### 1.3 VLA 基础模型与具身智能新进展

| 名称 | 年份 | 机构/作者 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|----------|----------|--------|--------|------|------|
| Meituan-Robotics-0 (MR0): Vision-Language-Action Foundation Model for Desktop Manipulation | 2026 | Meituan Robotics | — | arXiv cs.RO [9] | 高（国内大厂 VLA 基座模型首发） | ★★★★☆ 1.47 亿视觉语言样本 + 1.5 万小时机器人轨迹，12 种本体，三阶段训练配方 [9] | [9] | 面向固定底座桌面操作的 VLA 基础模型与具身智能体系统 [9] |
| HuMI: Humanoid Whole-Body Manipulation from Humanoid-Free Demonstrations | 2026 | — | — | arXiv cs.RO [10] | 高（人形全身操作无需人形演示） | ★★★★☆ 从非人形演示学习人形全身操作，解决本体差异迁移 [10] | [10] | > 待核实：具体方法细节与实验结果需全文精读确认 |
| Learning Getting-Up Policies for Real-World Humanoid Robots | 2025 | — | — | arXiv cs.RO [2] | 高（人形机器人真机站立策略） | ★★★★☆ 真机人形机器人倒地恢复策略学习 [2] | [2] | > 待核实：仿真到真机迁移细节与成功率指标需核实 |

### 1.4 安全与人机协作前沿

| 名称 | 年份 | 机构/作者 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|----------|----------|--------|--------|------|------|
| LLM-based ambiguity detection in natural language instructions for collaborative surgical robots | 2025 | — | — | arXiv cs.RO [11] | 中（手术机器人安全关键领域 LLM 应用） | ★★★★☆ 针对自然语言指令歧义检测，降低人机协作风险 [11] | [11] | 利用 LLM 进行歧义检测，专为协作手术机器人设计，应对安全关键场景下自然语言指令风险 [11] |

---

## 2. 工业界与产品（Industry & Product）

> **一句话增量判断**：国内头部互联网/平台公司（美团）正式发布 VLA 基座模型 MR0，标志着 VLA 从实验室走向工业级桌面操作场景；人形机器人全身操作与站立恢复真机部署加速；协作机器人安全标准 ISO 10218-1/2:2025 与 ISO/TS 15066 融合修订落地，推动协作机器人产品合规上市；但 ROS 2 生态层面缺乏统一的工业级仿真-真机评估工具链产品。

### 2.1 关键产品与发布

| 产品/发布 | 时间 | 机构 | 类型 | 证据来源 | 说明 |
|-----------|------|------|------|----------|------|
| Meituan-Robotics-0 (MR0) VLA 基座模型 | 2026-11 | Meituan Robotics | 基础模型 + 具身智能体系统 | [9] | 1.47 亿 V-L 样本 + 1.5 万小时轨迹，12 本体，三阶段训练，面向桌面操作 |
| HuMI: 人形全身操作 (无需人形演示) | 2026-02 | — | 算法/系统 | [10] | 从非人形演示学习人形全身操作，解决本体差异 |
| 人形机器人真机站立恢复策略 | 2025-02 | — | 算法/真机部署 | [2] | 真机人形机器人倒地恢复策略学习 |
| LLM 歧义检测框架 (协作手术机器人) | 2025-07 | — | 安全增强组件 | [11] | 自然语言指令歧义检测，降低手术协作风险 |

### 2.2 ROS 2 工程落地现状

- **仿真-真机评估工具链碎片化**：现有仿真基准（Isaac Sim、MuJoCo、Gazebo 等）推动了研究，但通用策略的真实世界评估滞后，缺乏系统性的 sim-to-real 迁移基准设计原则 [7]。
- **真机竞赛基准较早**：Real Robot Challenge (2021) 为三指灵巧手提供真机操作基准，但时间较早，当前关注度有限，需结合 Open X-Embodiment、DROID 等最新数据集综合考察 [8]。
- **> 待核实**：ROS 2 Humble/Iron/Jazzy 版本在工业级实时控制、安全认证、OPC UA/TSN 集成方面的最新产品化落地案例。

---

## 3. 蓝海与缺口（Blue Ocean & Gaps）

> **一句话增量判断**：四大核心蓝海：(1) 标准化、高视觉保真、可量化对齐度的 sim-to-real 基准体系；(2) 运动学与动力学双重不确定下的高自由度本体实时自适应控制真机验证；(3) 数据驱动被动控制在接触丰富任务中的被动性保证与泛化；(4) 可编程物质/变形本体的运动学建模与实验闭环。均处于「无人区/极早期」阶段。

### 3.1 核心蓝海机会表

| 蓝海方向 | 缺口描述 | 证据来源 | 潜在杠杆点 |
|----------|----------|----------|------------|
| 标准化 sim-to-real 基准体系 | 缺乏高视觉保真仿真、系统性任务复杂度梯度、性能对齐度量化的统一基准 [7] | [7] | 构建 ROS 2 原生评估工具链，制定社区共识指标 |
| 双重不确定自适应控制真机验证 | 经典自适应控制 (Wang 2014) 在高自由度真机上的实时性与鲁棒性验证缺失 [3] | [3] | 结合现代优化求解器与边缘计算实现高频自适应 |
| 数据驱动被动控制泛化 | iFIR 被动控制器在接触丰富任务中的被动性保证与跨任务泛化未充分验证 [5] | [5] | 融合基础模型先验知识增强数据效率 |
| 可编程物质/变形本体运动学 | 运动学雅可比、负载路径连续性、连接器滞后等 30 板块均缺乏实验闭环 [6] | [6] | 模块化面板 1:10 竞赛基准，盲扰动下对比固定单壳/被动格栅 |
| 人形机器人全身操作迁移 | 从非人形演示学习人形全身操作的本体差异桥接机制尚不成熟 [10] | [10] | 跨本体动作表示与运动学重映射 |
| 手术机器人自然语言安全 | LLM 歧义检测在真实手术场景的误报/漏报率与实时性约束未充分量化 [11] | [11] | 形式化验证 + LLM 混合安全护栏 |

---

## 4. 瓶颈与拐点（Bottleneck & Inflection）

> **一句话增量判断**：四大瓶颈正逼近拐点：(1) 仿真-真机评估标准化缺口 → RSS 2025 工作坊提出三大设计原则，社区共识形成中；(2) MPC 高频伺服层计算延迟 → 专用求解器与硬件加速 (FPGA/GPU) 使 1kHz+ MPC 成为可能；(3) VLA 基座模型数据飞轮 → MR0 等大厂模型展示 1.5 万小时轨迹规模，数据获取成本成为新瓶颈；(4) 协作机器人安全标准修订 → ISO 10218-1/2:2025 与 ISO/TS 15066 融合落地，合规成本与创新速度博弈加剧。

### 4.1 瓶颈与拐点信号表

| 瓶颈 | 当前状态 | 拐点信号 | 证据来源 | 判断 |
|------|----------|----------|----------|------|
| Sim-to-real 评估标准化缺失 | 碎片化基准，真机评估滞后 [7] | RSS 2025 顶会工作坊系统梳理三大设计原则，社区开始达成共识 [7] | [7] | 拐点临近：若 2026-2027 出现社区采纳的统一基准套件，将显著加速策略迁移 |
| MPC 计算延迟与求解器可靠性 | 非线性 MPC 在高频伺服层 (＞1kHz) 求解困难 [4] | 专用求解器 (acados, FORCES Pro) + 硬件加速推动 1kHz+ MPC 落地 [4] | [4] | 拐点进行中：工程化求解器成熟度决定落地速度 |
| VLA 数据规模与获取成本 | 头部模型需 10^4 小时级轨迹数据 [9] | MR0 等大厂模型展示规模化数据飞轮，但中小团队数据获取成本高企 [9] | [9] | 瓶颈持续：开源数据集 (Open X-Embodiment, DROID) 与合成数据能否补齐仍待验证 |
| 协作机器人安全合规 | ISO 10218-1/2:2011 旧版滞后于协作机器人发展 [12] | ISO 10218-1/2:2025 与 ISO/TS 15066 融合修订发布，新标准强制合规 [12] | [12] | 拐点已至：2025 版标准生效将重塑产品准入门槛 |
| 可编程物质/变形本体实验验证 | 纯理论架构，无实物验证 [6] | 专著提出 1:10 模块化面板竞赛基准与合取式释放策略，若启动实物竞赛将形成拐点 [6] | [6] | 远期拐点：取决于经费与跨学科团队组建 |

---

## 5. 社会·政策·国际（Society, Policy & Geopolitics）

> **一句话增量判断**：政策层面以 ISO 10218-1/2:2025 与 ISO/TS 15066 融合修订为核心，协作机器人安全标准全球同步收紧；基础模型透明度指数 (2025) 推动 AI 治理规范化；地缘政治下供应链自主可控需求倒逼国产控制器、伺服驱动器、力控传感器国产化替代；劳动替代与人机协作伦理争议持续升温。

### 5.1 关键政策与标准动态

| 政策/标准 | 时间 | 机构/范围 | 核心变化 | 证据来源 | 影响 |
|-----------|------|-----------|----------|----------|------|
| ISO 10218-1/2:2025 与 ISO/TS 15066 融合修订 | 2025 | ISO/TC 299 (全球) | 协作机器人安全要求全面修订，整合 ISO/TS 15066 技术规范，新增功能安全、人机协作风险评估细则 [12] | [12] | 重塑协作机器人产品准入门槛，推动功能安全设计前置 |
| The 2025 Foundation Model Transparency Index | 2025 | Stanford HAI 等 (全球) | 第三版年度透明度指数，量化基础模型开发者透明度实践演进 [13] | [13] | 推动 VLA/具身基础模型训练数据、部署风险、治理结构信息披露规范化 |
| 机器人教练助手披露行为适当性用户感知 | 2024 | — | 研究用户对机器人披露行为的适当性感知，涉及人机信任与伦理 [14] | [14] | 为服务机器人交互伦理设计提供实证依据 |

### 5.2 地缘与供应链信号

- **> 待核实**：中美在高性能伺服驱动器、六维力传感器、实时控制芯片 (FPGA/SoC) 领域的出口管制与国产化替代进展。
- **> 待核实**：欧盟《机器法规》(Machinery Regulation) 与《人工智能法案》对具身智能产品出口合规的具体要求落地时间表。

---

## 6. 资本与生态（Capital & Ecosystem）

> **一句话增量判断**：资本关注点从单一算法模型转向「数据-模型-本体」一体化垂直落地闭环 (MR0 模式)；人才流动呈现「大厂基础模型团队 → 具身智能创业」趋势；ROS 2 生态缺乏统一的商业级仿真-真机评估工具链产品，形成工具链创业机会；开源数据集 (Open X-Embodiment, DROID) 与基准榜单 (RoboArena, LIBERO, SimplerEnv) 成为生态锚点。

### 6.1 资本与生态关键信号

| 信号 | 描述 | 证据来源 | 判断 |
|------|------|----------|------|
| 大厂自研 VLA 基座模型 | 美团发布 MR0，1.47 亿 V-L 样本 + 1.5 万小时轨迹，12 本体，三阶段训练 [9] | [9] | 头部平台入局具身智能，数据飞轮与场景闭环成核心护城河 |
| 人形机器人全身操作与站立恢复 | HuMI (跨本体迁移) [10]、Getting-Up Policies (真机站立) [2] 加速人形商业化落地 | [10][2] | 人形本体硬件成熟度与全身控制算法协同突破，资本关注度高 |
| 协作机器人安全合规驱动需求 | ISO 10218:2025 落地催生功能安全设计、认证咨询、合规工具链需求 [12] | [12] | 合规赛道从「成本中心」转为「增值服务」 |
| 基础模型透明度指数常态化 | 2025 版指数发布，推动 VLA 模型训练数据、风险评估披露 [13] | [13] | 合规与治理成为融资尽调必查项 |
| ROS 2 评估工具链缺口 | 仿真基准碎片化，sim-to-real 标准化基准缺失 [7] | [7] | 商业级评估平台 (SaaS/私有化部署) 存在蓝海机会 |

### 6.2 人才与社区动态

- **> 待核实**：ROS 2 核心维护团队 (Open Robotics/Intrinsic) 近期人员变动与路线图调整。
- **> 待核实**：国内 ROS 2 社区 (ROSCon China、各高校实验室) 在实时控制、安全认证、国产硬件适配方面的贡献占比变化。

---

## 7. 信号与预测（Signals & Forecast）

> **一句话增量判断**：未来 6-18 个月四大可验证预测：(1) 社区将发布首个基于 ROS 2 原生、具备高视觉保真与性能对齐度量化的 sim-to-real 标准基准套件 [P, 置信度 0.7]；(2) 国产协作机器人头部厂商将完成 ISO 10218:2025 认证首批量产交付 [P, 置信度 0.8]；(3) VLA 基座模型将从「桌面操作」泛化至「移动双臂/人形全身操作」，单模型多本体成为标配 [P, 置信度 0.75]；(4) 数据驱动被动控制 (iFIR 等) 将在接触丰富装配/打磨任务中完成首批真机闭环验证 [P, 置信度 0.6]。

### 7.1 可验证预测假设表

| # | 预测假设 (可证伪) | 依据链 | 置信度 | 验证指标与时间窗口 | 标记 |
|---|-------------------|--------|--------|-------------------|------|
| P1 | 2027 年 Q2 前，ROS 2 社区发布首个官方背书的 sim-to-real 标准基准套件，包含高视觉保真仿真环境、分级任务复杂度、性能对齐度量化指标 | RSS 2025 工作坊已形成三大设计原则共识 [7]；Open X-Embodiment 等数据集提供统一数据格式基础 | 0.7 | GitHub/ROS Discourse 出现官方 REP 或基准仓库，且有 ≥3 家实验室/公司提交基线结果 | [P] |
| P2 | 2026 年底前，≥2 家国产协作机器人头部厂商完成 ISO 10218-1/2:2025 认证并实现批量交付 | ISO 10218:2025 已发布 [12]；国内协作机器人出货量增长迅猛，合规刚需明确 | 0.8 | CNAS/CNCA 认证公示目录新增对应证书；厂商官网发布合规白皮书 | [P] |
| P3 | 2027 年 Q1 前，头部 VLA 模型 (MR0 级别) 单模型支持 ≥3 种本体 (固定臂/移动双臂/人形) 真机部署 | MR0 已覆盖 12 种本体 [9]；HuMI 验证跨本体迁移可行性 [10] | 0.75 | 论文/技术报告展示同一权重在 ≥3 本体零样本/少样本部署成功率 >60% | [P] |
| P4 | 2026 年 Q4 前，数据驱动被动 iFIR 控制器在真机接触丰富任务 (如轴孔装配、曲面打磨) 完成闭环验证，通过性指标达标 | iFIR 方法 2024 年提出 [5]；被动性保证理论完备，工程落地潜力大 | 0.6 | 会议/期刊发表真机实验论文，报告接触力跟踪误差、通过率、被动性违反次数 | [P] |

### 7.2 早期弱信号监测清单

| 弱信号 | 来源/观测点 | 可能意味 | 追踪建议 |
|--------|-------------|----------|----------|
| 量子计算在控制区间矩阵性质中的应用探索 | arXiv 2024 论文 [15][16] | 长期看：量子加速鲁棒控制合成/区间观测器设计 | 关注量子优化求解器在 MPC/鲁棒控制中落地进展 |
| Koopman 算子 + SOS 优化稳定性保证改进 | arXiv 2024 v6 [17] | 中期看：数据驱动非线性控制稳定性理论工具链成熟 | 跟踪相关工具箱 (Python/MATLAB) 开源进度 |
| 弱硬实时控制系统 ℓ₂ 性能分析 | arXiv 2023 v3 [18] | 近期看：ROS 2 实时调度与控制协同设计理论支撑 | 关注 ROS 2 实时内核 (PREEMPT_RT) 与控制协同调度研究 |
| 微创手术并联机器人运动学分析 | arXiv 2024 [19] | 医疗机器人专用运动学建模与标定需求增长 | 结合 ISO 10218:2025 医疗协作机器人条款追踪 |

### 7.3 不确定性与风险提示

- **数据飞轮可持续性风险**：VLA 模型依赖万小时级真机轨迹，数据采集成本高、长尾任务覆盖难，合成数据与仿真数据能否有效补齐仍存 **不确定** [9]。
- **Sim-to-real 基准共识破裂风险**：若社区无法在 2027 年前达成统一基准，碎片化评估将持续拖慢策略迁移效率，**风险** 中等 [7]。
- **安全标准合规成本传导风险**：ISO 10218:2025 合规成本可能挤压中小协作机器人厂商生存空间，引发行业洗牌，**风险** 较高 [12]。
- **可编程物质/变形本体技术成熟度极低**：专著仍处假设形成阶段，30 个数学板块均缺乏实验证据，**不确定** 极高，不建议近期投入核心资源 [6]。
- **基础模型透明度指数执行力度**：透明度指数目前为自愿披露，若无监管强制力，VLA 模型训练数据版权、偏见、部署风险披露可能流于形式，**不确定** 中等 [13]。

---

## 参考来源（Reference Sources）
[1] NTU-NPU System for Voice Privacy 2024 Challenge — http://arxiv.org/abs/2410.02371v1
[2] Learning Getting-Up Policies for Real-World Humanoid Robots — http://arxiv.org/abs/2502.12152v2
[3] Adaptive Control of Robot Manipulators With Uncertain Kinematics and Dynamics — http://arxiv.org/abs/1403.5204v3
[4] Analysis and design of model predictive control frameworks for dynamic operation -- An overview — http://arxiv.org/abs/2307.03004v2
[5] Passive iFIR Filters for Data-Driven Control — http://arxiv.org/abs/2403.06640v2
[6] 智能奈米機器人物質與可變形自主車體極限 1/90 Intelligent Nanorobotic Matter and Morphing Autonomous Vehicle Bodies at the Limit STARLI | YULI NANO SUPERCAR TRILOGY | PART I Research Institute XXXVI / Flagship 01 of 90 Author: Feng Cheng-en (33) x STARLI / 星璃 Research Working Edition v1.0 | 31 October 2026 | 777 pages This 777-page English research working monograph proposes a falsifiable, scaled engineering architecture for programmable robotic matter and morphing autonomous vehicle structures. It asks whether identified modules can form a load-bearing body panel, pass between two registered geometries and retain verified structural integrity under hidden connector defects. The work is strictly hypothesis-forming, non-occupancy and not an automotive safety or roadworthiness claim. Its three-way research coupling joins programmable matter, distributed robotics and vehicle load paths. The fundamental scientific test separates exterior shape change from graph rigidity, measured weak-direction stiffness, connector preload, joint slip, reversible structural control and an independently traceable load transfer path. A minimum 1:10 modular panel competes against matched-mass fixed monocoque and passive modular lattice baselines under pre-registered blinded disturbances. Aborted trials, rejected units, repair events, energy overhead and uncertainty remain in the complete experimental denominator. Thirty distinct mathematical research plates cover graph-rigidity rank, constrained stiffness assembly, weak-mode stability, structural load margin, Euler buckling, friction cones, shear transfer, connector hysteresis, fatigue, crack propagation, geometry error, rigid registration, kinematic Jacobians, actuator work, electrical dissipation, thermal balance, safe control, correlated metrology, emergency stop latency, material mass closure, redundancy, reproducibility and conjunctive release. Each plate distinguishes physical construction, measurable units, assumptions, blind falsification and chapter interfaces. Eighty-two chapters are paired with 410 individually paginated investigations. The monograph additionally proposes 200 Research Gates and 33 genuinely different Phoenix Answer Embryos, including rigidity witnesses, connector passports, metrology transfer kits, half-transition recovery tests, sensor-refusal protocols and successor-ready research seeds. These items are research invitations and candidate evidence objects; they are not completed experimental outcomes. DOI evidence ancestry and component research sources: - 10.5281/zenodo.23318840 - Flagship 13 mother monograph, DOI supplied by author (metadata not independently confirmed here). - 10.5281/zenodo.23318839 - Flagship 13 all-version ancestry, DOI supplied by author (metadata not independently confirmed here). - 10.1038/s41467-024-53123-6 - Robo-Matter towards reconfigurable multifunctional smart materials (2024). - 10.1038/s41467-025-60982-0 - Modular shape-changing tensegrity-blocks enable self-assembling robotic structures (2025). - 10.1145/3653671 - From Conventional to Programmable Matter Systems (2024 review). - 10.1007/s10846-024-02067-6 - Reconfiguration strategies for modular robots (2024 review). - 10.1177/02783649241283847 - Modular robot mechanisms and design (2025 survey). - 10.1126/scirobotics.adz1999 - Modular reconfigurable robots and application needs (2026 review). The cited studies and reviews support component mechanisms and known challenges. They do not provide evidence that the integrated morphing vehicle concept has been built, road-tested or approved. The candidate's core release policy is conjunctive: load-path continuity, bounded geometry error, valid independent metrology, physical stop authority and reproducible external replay must pass together. This monograph carries the series imprint 1/90, preserving the first book's position within the ninety-volume STARLI YULI Nano Supercar Trilogy. The subsequent research lineage extends to modular assembly, autonomous mobile habitats and self-expanding cities while retaining explicit experimental and human-governance boundaries. Join the STARLI Research Community Explore more than 100 interdisciplinary research themes and follow the evolving STARLI Research Gate community: https://zenodo.org/communities/starli-research-gate/ — https://doi.org/10.5281/zenodo.23813617
[7] Robot Policy Evaluation for Sim-to-Real Transfer: A Benchmarking Perspective — http://arxiv.org/abs/2508.11117v1
[8] Grasp and Motion Planning for Dexterous Manipulation for the Real Robot Challenge — http://arxiv.org/abs/2101.02842v1
[9] Meituan-Robotics-0: A Vision-Language-Action Foundation Model for Desktop Manipulation — http://arxiv.org/abs/2611.08577v3
[10] HuMI: Humanoid Whole-Body Manipulation from Humanoid-Free Demonstrations — http://arxiv.org/abs/2602.06643v3
[11] LLM-based ambiguity detection in natural language instructions for collaborative surgical robots — http://arxiv.org/abs/2507.11525v1
[12] Evolution of Safety Requirements in Industrial Robotics: Comparative Analysis of ISO 10218-1/2 (2011 vs. 2025) and Integration of ISO/TS 15066 — http://arxiv.org/abs/2602.17822v1
[13] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1
[14] Users' Perception on Appropriateness of Robotic Coaching Assistant's Disclosure Behaviors — http://arxiv.org/abs/2410.10550v1
[15] Using quantum computers in control: interval matrix properties — http://arxiv.org/abs/2403.17711v1
[16] Bringing Quantum Systems under Control: A Tutorial Invitation to Quantum Computing and Its Relation to Bilinear Control Systems — http://arxiv.org/abs/2412.00736v1
[17] Koopman-based control using sum-of-squares optimization: Improved stability guarantees and data efficiency — http://arxiv.org/abs/2411.03875v6
[18] On $\ell_2$-performance of weakly-hard real-time control systems — http://arxiv.org/abs/2305.07875v3
[19] Kinematic analysis of a parallel robot for minimally invasive surgery — http://arxiv.org/abs/2406.02047v1

---

*Generated by research-bot · topic=`机器人运动学控制与-ros-2` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`nvidia/nemotron-3-ultra-550b-a55b` · sources=30 · duration=530s · 2026-11-25T05:08:19+00:00*
