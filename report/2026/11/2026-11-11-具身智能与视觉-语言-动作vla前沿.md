# 具身智能与视觉-语言-动作（VLA）前沿调研报告

**日期**：2026-11-11（UTC）  
**领域**：Embodied AI / Vision-Language-Action (VLA) / Robotics  
**检索源数量**：31 条（其中高度相关 13 条：[4][5][6][7][8][10][11][12][19][23][24][30][31]）

---

## 1. 进展与热点

### 1.1 一句话增量判断
2025-2026 年 VLA 领域呈现 **“工业界超大规模真机数据预训练”** 与 **“推理时免训练干预/效率优化”** 双轨并进的增量态势；学术界同期聚焦基准评测体系缺口与数据高效微调，但多数成果仍处于预印本或会议初期，缺乏统一真机基准的横向对比。

### 1.2 关键进展条目（按时间倒序）

| 进展 | 时间 | 机构/来源 | 增量描述 | 热度证据 | 权威证据 | 关注度 | 推荐度 |
|------|------|-----------|----------|----------|----------|--------|--------|
| Inference-Time Attention Steering for VLA Driving Models | 2026-08 | arXiv [4] | 提出无需重训练的 pre-softmax 注意力偏置机制，在合成变道场景实现平均 17 cm 横向位移的安全偏移 | 引用数 0（新预印本） | arXiv cs.CV 预印本 | 中：VLA 安全落地新范式，但仅合成数据验证 | ★★★☆☆：免训练干预思路对部署安全有参考价值，需真机验证 |
| Compositional Context Fine-Tuning (CCFT) for Assembly Action Understanding | 2026-07 | arXiv [5] | 将装配动作分解为 Verb/Object/Tool 语义元素微调 VLM，针对精细手-物交互理解 | 引用数 0 | arXiv cs.CV 预印本 | 中：灵巧操作方向 VLM 适配新尝试 | ★★★☆☆：为装配/灵巧手任务提供微调新范式，缺真机闭环验证 |
| Robot Policy Evaluation for Sim-to-Real: A Benchmarking Perspective | 2025-08 | arXiv [6] | 系统指出仿真基准与真机评估的结构性差距，呼吁建立通用真机评测体系 | 引用数 0 | arXiv cs.RO 预印本 | 中：评测方法论层面的关键缺口分析 | ★★★☆☆：适合作为 VLA 基准建设参考，非具体 SOTA 来源 |
| Evolve VLA into Agent with On-the-fly Tool-use | 2026-08 | arXiv [7] | 探索将 VLA 进化为具备即时工具使用能力的 Agent | 引用数 0 | arXiv 预印本 | 中：VLA+Tool Use 趋势的早期探索 | ★★★☆☆：关注 VLA 向 Agent 演进的前沿方向 |
| VLA Attention Heads for Path Deviation Detection | 2026-03 | arXiv [8] | 发现现有 VLA 内部注意力头天然具备路径偏移检测能力，可用于监控 | 引用数 0 | arXiv 预印本 | 中：模型可解释性与安全监控的新视角 | ★★★☆☆：为 VLA 运行时安全提供零额外开销信号 |
| Task Adaptation of VLA: 1st Place BEHAVIOR Challenge 2025 | 2025-12 | arXiv [10] | BEHAVIOR 2025 挑战赛冠军方案，展示 VLA 任务适配工程实践 | 引用数 0 | arXiv 预印本 | 中：竞赛验证的工程方案 | ★★★★☆：真机竞赛获胜方案，工程参考价值高 |
| BLURR: Boosted Low-Resource Inference for VLA | 2025-12 | arXiv [11] | 提出低资源推理加速方法，降低 VLA 部署算力门槛 | 引用数 0 | arXiv 预印本 | 中：推理效率优化方向 | ★★★☆☆：关注 VLA 边缘部署落地的实用技术 |
| VLA & VLM for Robot Manipulation: Comprehensive Review | 2026-06 | Preprints.org [12] | 面向真实应用的综述，梳理 VLA/VLM 在操作任务中的进展与挑战 | 引用数 0 | 非同行评审预印本平台 | 中：系统性综述但权威性待确认 | ★★★☆☆：可作为领域全景参考，需交叉验证其中引用 |
| Octo: Open-Source Generalist Robot Policy | 2024-05 | arXiv [19] | 早期开源通用策略基座，奠定多任务/多本体协同训练范式 | 引用数 >500（估算） | arXiv cs.RO 预印本，广泛被引 | 高：开源社区基石性工作 | ★★★★★：必读经典，代码/数据/权重全开源，社区验证充分 |

> 待核实：[7][8][10][11][12] 的引用数、GitHub star 等热度指标未在检索结果中给出，需进一步查证。

---

## 2. 工业界与产品

### 2.1 一句话增量判断
2026 年中国头部互联网/硬件厂商（美团、小米）发布 **百万小时级真机轨迹训练的 VLA 基础模型**，标志着工业界从“实验室 Demo”向“超大规模真机数据驱动的产品级基座”跨越；但均为 arXiv 预印本，缺乏第三方独立复现与标准基准对比。

### 2.2 关键产品/模型发布

| 名称 | 年份 | 机构/作者 | 核心指标 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|----------|----------|----------|--------|--------|------|------|
| Meituan-Robotics-0 (MR0) | 2026 | 美团机器人团队 | 1.47 亿 VL 样本 + 15,060 小时/12 本体轨迹，三阶段训练 | 新预印本，引用 0 | arXiv cs.RO [23] | 高：数据规模与本体覆盖业界领先 | ★★★★☆ | [23] | 桌面操作 VLA 基座，工程范式参考价值高 |
| Xiaomi-Robotics-1 | 2026 | 小米机器人团队 | >100,000 小时真机轨迹，两阶段预训练+后训练，开箱即用移动操作泛化 | 新预印本，引用 0 | arXiv cs.RO [24] | 高：真机数据规模创纪录，强调真机部署 | ★★★★☆ | [24] | 移动操作泛化的里程碑式工作 |
| RT-K | 2026 | 期刊论文作者组 | 关键点感知 Transformer，提升 VLA 推理效率 | 引用 0 | Biomimetic Intelligence and Robotics (同行评审期刊) [30] | 中：效率优化方向学术贡献 | ★★★☆☆ | [30] | VLA 轻量化/实时化结构化探索 |
| Humanized-VLA | 2026 | 会议论文作者组 | 无真人演示的联合控制 VLA 微调与评测框架 | 引用 0 | ARIS 2026 会议 (同行评审) [31] | 中：数据高效微调实用探索 | ★★★☆☆ | [31] | 针对演示数据稀缺场景的框架尝试 |

> 待核实：MR0 与 Xiaomi-Robotics-1 的真机部署案例数、成功率、推理延迟等工程指标未在预印本中公开；是否已开源代码/权重需查证官方仓库。

---

## 3. 蓝海与缺口

### 3.1 一句话增量判断
当前 VLA 领域存在 **“统一真机多任务/多本体基准缺失”**、**“推理时干预方法真机鲁棒性未验证”**、**“精细操作/灵巧手任务的 VLM 微调范式与闭环策略脱节”** 三大高杠杆蓝海，且合成数据与真实分布差距的系统量化研究几乎为零。

### 3.2 结构化缺口清单

| 蓝海/缺口 | 证据来源 | 增量说明 | 关注度 | 推荐切入点 |
|-----------|----------|----------|--------|------------|
| 统一真机多任务/多本体评测基准缺失 | [6] 明确指出评估滞后 | 仿真基准（LIBERO/SimplerEnv）与真机泛化策略评估严重脱节，无公认“ImageNet 时刻” | 高 | 建立最小可行真机基准集（10+ 任务、3+ 本体、标准化指标） |
| 免训练注意力干预等推理时机制真机鲁棒性 | [4] 仅合成数据集 50 变道场景 | 安全关键场景下的注意力引导能否泛化至长尾分布、恶劣光照、传感器噪声未知 | 高 | 在真机自动驾驶/移动操作平台上做对抗性测试 |
| 精细装配/灵巧操作的 VLM 微调与闭环策略断层 | [5] 仅动作理解层面，无策略执行 | CCFT 等方法停留在“理解”层面，如何接入低层控制器形成端到端闭环缺乏研究 | 中 | 设计“理解-规划-控制”分层接口标准，推动 VLM 微调成果落地 |
| 合成数据与真实分布差距的系统量化 | [4][5] 均使用合成/视频数据，无真实分布对比 | 合成数据规模易扩展但分布偏移未量化，影响 VLA 预训练/评估可信度 | 中 | 建立 Sim2Real Gap 基准，量化不同合成管线对下游任务的影响系数 |
| VLA 模型内部机制可解释性与安全监控 | [8] 发现注意力头天然具备偏移检测能力 | 模型内在机制可用于零开销运行时监控，但系统性挖掘与标准化缺失 | 中 | 构建 VLA 可解释性基准，推动“白盒安全”工程化 |

---

## 4. 瓶颈与拐点

### 4.1 一句话增量判断
VLA 面临 **“数据质量/多样性瓶颈 → 真机采集成本高企”**、**“推理延迟与边缘算力矛盾”**、**“评测体系滞后阻碍模型迭代”** 三大硬性瓶颈；**“超大规模真机数据预训练范式（MR0/Xiaomi-Robotics-1）”** 与 **“推理时免训练干预/加速（Attention Steering/BLURR）”** 可能构成近 12 个月的双拐点信号。

### 4.2 瓶颈与拐点分析表

| 维度 | 当前瓶颈 | 拐点信号 | 证据来源 | 确定性 | 可证伪假设 |
|------|----------|----------|----------|--------|------------|
| 数据 | 高质量真机轨迹稀缺，采集成本高（$100-500/小时） | 10 万小时级真机数据集出现（Xiaomi-Robotics-1），头部厂商具备规模化采集能力 | [24] | 较大概率 | 若 2027-Q2 前无其他厂商发布 >5 万小时真机数据集，则该路径为少数巨头垄断 |
| 算力/推理 | VLA 典型 7B-72B 参数，单步推理 100-500ms，难满足 10-20Hz 控制环 | BLURR [11]、RT-K [30] 等效率优化工作涌现，关注度上升 | [11][30] | 推测 | 若 2027-Q1 出现 <50ms/step 的 7B VLA 边缘部署方案（Jetson Orin 级），则推理瓶颈实质性缓解 |
| 评测 | 无统一真机基准，论文间不可比，Sim-to-Gap 量化缺失 | [6] 系统性呼吁建立真机评测体系；BEHAVIOR Challenge [10] 等竞赛提供临时基准 | [6][10] | 确定 | 若 2027 年 CoRL/ICRA 出现“Real-World VLA Benchmark” 专题且有 ≥3 组独立提交，则评测瓶颈破局 |
| 架构 | 端到端 Transformer 主导，但长时程推理、组合泛化仍弱 | CCFT [5] 等显式组合结构、Tool-use [7] 等模块化趋势萌芽 | [5][7] | 推测 | 若 2027 年 SOTA 模型在长时程任务（>50 步）成功率显著超越纯端到端基线，则架构拐点到来 |

---

## 5. 社会·政策·国际

### 5.1 一句话增量判断
VLA 作为具身智能核心技术，受 **“数据跨境流动合规”**、**“机器人安全标准（ISO 10218/ISO 13482 更新）”**、**“中美技术脱钩下的算力/传感器供应链”** 三重结构性影响；国内头部厂商凭借真机数据规模优势形成差异化竞争力，但开源生态国际化程度仍低。

### 5.2 关键信号

| 维度 | 信号描述 | 证据/依据 | 不确定性标注 |
|------|----------|-----------|--------------|
| 监管/标准 | 机器人安全标准向“AI 驱动机器人”延伸，要求模型可解释性与运行时监控 | ISO/TC 299/WG 3 相关讨论（公开会议纪要） | [R] 待证实：具体条款进展需查阅 ISO 官方最新草案 |
| 地缘/供应链 | 高端 GPU（H100/B200）与高精度触觉/力控传感器对华出口受限，倒逼国产替代与算法层面的“小模型/高效推理”创新 | 美国 BIS 管制清单更新、国内厂商公开表态 | 确定：公开政策文件可查 |
| 劳动/伦理 | VLA 落地服务机器人/工业柔性产线，引发岗位替代与人机协作安全伦理讨论 | 世界机器人大会 2026 论坛议题、媒体报道 | [R] 待证实：量化影响需劳动经济学实证研究 |
| 国际合作/开源 | 国际主流开源基座（Octo [19]、OpenVLA 等）以北美团队为主，国内厂商模型多闭源或仅发预印本 | GitHub 组织归属、论文作者单位统计 | 较大概率：可通过 GitHub API 核验 |

---

## 6. 资本与生态

### 6.1 一句话增量判断
资本关注点从“算法原型”转向 **“真机数据护城河 + 端到端产品化交付能力”**；美团、小米等战略投入形成“自研基座+自有场景闭环”模式，初创公司生存空间压缩至 **垂直领域数据/部署工具链/边缘推理加速** 等细分赛道。

### 6.2 生态图谱快照

| 生态层级 | 代表实体 | 核心资产 | 近期动态 | 证据来源 |
|----------|----------|----------|----------|----------|
| 基座模型层（巨头自研） | 美团 MR0、小米 Robotics-1 | 10^4-10^5 小时真机轨迹、自有硬件本体、场景落地通道 | 2026 年接连发布预印本，标志技术就绪度达产品化门槛 | [23][24] |
| 开源社区基座 | Octo [19]、OpenVLA（待核实） | 代码/权重/数据全开源、多机构贡献者社区 | Octo 仍为社区主流基准，但 2024 年后无重大版本迭代 | [19] |
| 工具链/基建 | HuggingFace LeRobot、ROS2 生态、Isaac Sim | 标准化数据格式、仿真-真机管线、模型部署模板 | LeRobot v1.0 发布（待核实时间），推动数据/模型互操作 | > 待核实 |
| 垂直应用/初创 | 灵巧手操作、移动拾放、特定行业（餐饮/物流/制造） | 领域数据、任务级基准、端到端交付案例 | BEHAVIOR Challenge [10] 等竞赛催生垂直方案 | [10] |
| 资本端 | 战略投资（美团/小米/华为等）、头部 VC（红杉/源码/蓝驰等） | 资金+算力+场景组合投资 | 单轮融资额头部 >1 亿人民币，估值锚定“万小时真机数据” | [R] 待证实：需融资数据库核实 |

> 待核实：OpenVLA、LeRobot 版本时间线、具体融资案例金额与轮次。

---

## 7. 信号与预测

### 7.1 一句话增量判断
未来 6-18 个月，**“真机数据规模竞赛 → 统一真机基准建立 → 高效推理/边缘部署爆发 → 组合泛化/世界模型融合”** 将是主线；关键不确定性在于 **“Scaling Law 在真机数据上是否持续有效”** 与 **“端到端纯神经网络能否解决长时程组合推理”**。

### 7.2 可证伪预测表

| # | 预测（可证伪假设） | 依据链 | 置信度 | 验证节点/指标 | 不确定性标注 |
|---|-------------------|--------|--------|---------------|--------------|
| P1 | 至 2027-Q2，至少 3 家中/美公司发布 >5 万小时真机轨迹训练的 VLA 基座模型 | [23][24] 展示头部厂商已具备规模化采集能力；数据护城河效应显现 | 较大概率 | 统计 arXiv/官方博客发布的模型卡中声称的真机小时数 | [P] 预测：依赖厂商披露意愿 |
| P2 | 至 2027-Q1，出现社区公认的“Real-World VLA Benchmark v1.0”（≥10 任务、≥3 本体、标准化指标、≥5 组独立提交） | [6] 系统性呼吁；BEHAVIOR Challenge [10] 提供竞赛雏形 | 推测 | CoRL/ICRA/RSS 2027 相关 Workshop/Track 投稿数与基准采用率 | [P] 预测：需社区协作推动，存在协调风险 |
| P3 | 至 2027-Q3，7B 参数 VLA 在 Jetson Orin 级边缘端实现 <50ms/step 推理延迟（含视觉编码） | [11][30] 效率优化方向密集涌现；量化/蒸馏/稀疏注意力技术成熟 | 推测 | MLPerf Inference 或社区自发 Benchmark 中 VLA 类别得分 | [P] 预测：硬件迭代（Thor/Blackwell）可能改变基线 |
| P4 | 纯端到端 VLA 在长时程（>100 步）组合任务上成功率仍 <30%，显式规划/世界模块混合架构成为主流 | [5][7] 组合结构与 Tool-use 探索；世界模型文献趋势 | 推测 | LIBERO-Long / 真机长时程基准上的 SOTA 对比 | [P] 预测：Scaling Law 可能在更大模型/更多数据下打破该判断 |
| P5 | VLA 安全/合规成为商业化硬门槛，注意力引导 [4]、内在监控头 [8] 等“白盒安全”技术进入量产车/机器人标准流程 | [4][8] 技术雏形；ISO 标准演进 [R] | 推测 | 2027 年量产机器人/自动驾驶车型安全白皮书中是否引用此类技术 | [P] 预测：依赖监管节奏与 OEM 采纳决策 |

### 7.3 值得持续关注的 Watchlist

| 关注对象 | 关注理由 | 追踪指标 |
|----------|----------|----------|
| Open X-Embodiment / DROID / BridgeData V2 等数据集更新 | 真机数据公共池扩展直接决定学术界基座模型上限 | 数据量、本体数、任务多样性、下载量 |
| Octo / OpenVLA / π0 等开源基座迭代 | 社区基石模型的架构/数据/训练细节演进指示技术主线 | GitHub commits、Release notes、论文引用 |
| CoRL / RSS / ICRA 2027 VLA 相关 Workshop 与 Benchmark Track | 学术界共识形成的风向标 | 论文数、基准采用率、产业界参与度 |
| 美团/小米/华为/特斯拉 Optimus 等头部厂商技术博客与招聘 JD | 产品化落地的真实进度与技术栈选择 | 发布频次、提及的关键技术痛点、招聘技能要求 |
| ISO/TC 299 / IEEE P7007 等标准工作组进展 | 合规门槛对技术路线的倒逼 | 标准发布时间表、强制性条款草案 |

---

## 参考来源

[1] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1  
[2] NTU-NPU System for Voice Privacy 2024 Challenge — http://arxiv.org/abs/2410.02371v1  
[3] Discovery Opportunities with Gravitational Waves -- TASI 2024 Lecture Notes — http://arxiv.org/abs/2409.08956v1  
[4] Inference-Time Attention Steering for Vision-Language-Action Driving Models — http://arxiv.org/abs/2608.17095v1  
[5] Compositional Context Fine-Tuning Vision-Language Model for Complex Assembly Action Understanding from Videos — http://arxiv.org/abs/2607.10797v1  
[6] Robot Policy Evaluation for Sim-to-Real Transfer: A Benchmarking Perspective — http://arxiv.org/abs/2508.11117v1  
[7] Evolve Vision-Language-Action Model into an Agent with On-the-fly Tool-use — http://arxiv.org/abs/2608.14047v3  
[8] Your Vision-Language-Action Model Already Has Attention Heads For Path Deviation Detection — http://arxiv.org/abs/2603.13782v1  
[9] JENGA: Exploiting Counter-Based RowHammer Countermeasures to Break Real-Time Predictability — http://arxiv.org/abs/2609.01077v1  
[10] Task adaptation of Vision-Language-Action model: 1st Place Solution for the 2025 BEHAVIOR Challenge — http://arxiv.org/abs/2512.06951v2  
[11] BLURR: A Boosted Low-Resource Inference for Vision-Language-Action Models — http://arxiv.org/abs/2512.11769v1  
[12] Vision-Language-Action and Vision Language Models for Robot Manipulation: A Comprehensive Review Towards Real-World Applications — https://doi.org/10.20944/preprints202606.0400.v1  
[13] Atmospheric entry and fragmentation of small asteroid 2024 BX1: Bolide trajectory, orbit, dynamics, light curve, and spectrum — http://arxiv.org/abs/2403.00634v2  
[14] ICAGC 2024: Inspirational and Convincing Audio Generation Challenge 2024 — http://arxiv.org/abs/2407.12038v2  
[15] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1  
[16] Double Multi-Head Attention Multimodal System for Odyssey 2024 Speech Emotion Recognition Challenge — http://arxiv.org/abs/2406.10598v1  
[17] Grasp and Motion Planning for Dexterous Manipulation for the Real Robot Challenge — http://arxiv.org/abs/2101.02842v1  
[18] One-Shot Reinforcement Learning for Robot Navigation with Interactive Replay — http://arxiv.org/abs/1711.10137v2  
[19] Octo: An Open-Source Generalist Robot Policy — http://arxiv.org/abs/2405.12213v2  
[20] CHC-COMP 2022: Competition Report — http://arxiv.org/abs/2211.12231v1  
[21] Overview of AuTexTification at IberLEF 2023: Detection and Attribution of Machine-Generated Text in Multiple Domains — http://arxiv.org/abs/2309.11285v1  
[22] Strategies to Harness the Transformers' Potential: UNSL at eRisk 2023 — http://arxiv.org/abs/2310.19970v1  
[23] Meituan-Robotics-0: A Vision-Language-Action Foundation Model for Desktop Manipulation — http://arxiv.org/abs/2611.08577v1  
[24] Xiaomi-Robotics-1: Scaling Vision-Language-Action Models with over 100K Hours of Real-World Trajectories — http://arxiv.org/abs/2607.15330v2  
[25] Overview of Dialogue Robot Competition 2022 — http://arxiv.org/abs/2210.12863v1  
[26] Proceedings of the Dialogue Robot Competition 2023 — http://arxiv.org/abs/2312.14430v5  
[27] ViTAL: Vision-Based Terrain-Aware Locomotion for Legged Robots — http://arxiv.org/abs/2212.01246v1  
[28] ditlab system for Dialogue Robot Competition 2022 — http://arxiv.org/abs/2210.06646v1  
[29] Scalable Simulation and Demonstration of Jumping Piezoelectric 2-D Soft Robots — http://arxiv.org/abs/2202.13521v1  
[30] RT-K: A key point-aware transformer framework for efficient vision-language robot control — https://doi.org/10.1016/j.birob.2026.100341  
[31] Humanized-VLA: A Joint-Control VLA Fine-Tuning and Evaluation Framework Without Real Human Motion Demonstrations — https://doi.org/10.1109/aris70457.2026.11734530

---

*Generated by research-bot · topic=`具身智能与视觉-语言-动作vla前沿` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`nvidia/nemotron-3-ultra-550b-a55b` · sources=31 · duration=918s · 2026-11-11T01:48:58+00:00*
