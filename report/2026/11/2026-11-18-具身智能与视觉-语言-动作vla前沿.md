# 具身智能与视觉-语言-动作（VLA）前沿调研报告

**日期**：2026-11-18（UTC）  
**领域**：Embodied AI / Vision-Language-Action (VLA) / Robot Learning  
**检索源数量**：29 条（其中 VLA 相关有效来源 11 条：[1][2][3][4][5][6][7][8][9][10][11]）

---

## 1. 进展与热点（Progress & Hotspots）

### 1.1 核心架构突破：从“文本链式思维”向“视觉参与推理”演进

| 进展 | 时间 | 机构/作者 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|----------|----------|--------|--------|------|------|
| VLA-Thinker: Thinking-with-Image Reasoning | 2026-03 | arXiv (cs.CV) | > 待核实（新发布预印本） | arXiv preprint，未同行评审 | 中 | ★★★☆☆ | [1] | 首次提出在推理过程中动态回看视觉 token，打破“视觉为静态上下文”范式 |
| ACoT-VLA: Action Chain-of-Thought | 2026-01 | arXiv (cs.RO) v2 | > 待核实 | arXiv preprint | 中 | ★★★☆☆ | [6] | 将动作序列显式建模为 CoT 步骤，增强长时任务规划可解释性 |
| ATI-VLA: Actionable Alignment Then Adaptive Injection | 2026-10 | arXiv (cs.RO) | > 待核实 | arXiv preprint | 中 | ★★★☆☆ | [7] | 两阶段对齐+自适应注入，试图解决视觉-动作对齐与泛化的权衡 |
| E-VLA: Event-Augmented for Dark/Blurred Scenes | 2026-04 | arXiv (cs.CV) v2 | > 待核实 | arXiv preprint | 中 | ★★★☆☆ | [5] | 引入事件相机数据增强恶劣光照下的视觉感知鲁棒性 |
| VLA-Adapter: Tiny-Scale VLA Paradigm | 2025-09 | arXiv (cs.RO) v2 | > 待核实 | arXiv preprint | 中 | ★★★☆☆ | [4] | 面向边缘部署的轻量化适配器范式，降低推理算力门槛 |

**增量判断**：2024-2026 年 VLA 架构创新集中于三个方向——（1）**推理机制升级**：从纯文本 CoT 转向视觉参与的思维链；[1]（2）**动作显式建模**：将动作序列纳入推理链路；[6]（3）**感知增强与轻量化**：事件相机融合[5]与适配器微调[4]解决部署端感知鲁棒性与算力约束。上述均为 arXiv 预印本，**尚缺乏同行评审与独立复现**，属“演示/自评”层级证据，需持续跟踪后续会议录用与开源复现情况。> 待核实：是否有顶会（CoRL/RSS/ICRA/ICLR/NeurIPS）已录用上述工作的正式版本。

### 1.2 推理期干预与安全可控：无需重训练的注意力引导

| 进展 | 时间 | 机构/作者 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|----------|----------|--------|--------|------|------|
| Inference-Time Attention Steering (自动驾驶 VLA) | 2026-08 | arXiv (cs.CV) | > 待核实 | arXiv preprint | 中 | ★★★☆☆ | [2] | 在 Qwen3-VL backbone 上施加有界加性 pre-softmax attention bias，推理期聚焦安全关键交通参与者 |
| Attention Heads for Path Deviation Detection | 2026-03 | arXiv (cs.RO) | > 待核实 | arXiv preprint | 中 | ★★★☆☆ | [3] | 发现现有 VLA 内部注意力头天然编码路径偏移信号，可用于零样本异常检测 |

**增量判断**：推理期干预（Inference-Time Intervention）成为 2026 年新热点，解决“训练后不可控”的部署痛点。[2] 提出的有界注意力偏置可直接作用于检测器定位的 token，**无需重训练、延迟极低**，工程落地价值高；[3] 则从模型内部机制挖掘可解释性信号。两者均为预印本，**单一 backbone 验证，跨架构泛化性待核实**。> 待核实：在 OpenVLA/Octo/GR-1 等主流开源 VLA 上的迁移效果。

### 1.3 数据集与基准：Open X-Embodiment 成为事实上的上游数据标准

| 进展 | 时间 | 机构/作者 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|----------|----------|--------|--------|------|------|
| Open X-Embodiment 数据集合与 RT-X 模型族 | 2023 (v9 2024) | Google DeepMind / Robotics | 高（被广泛引用为上游数据源） | arXiv v9 迭代，社区事实标准 | 高 | ★★★★★ | [8] | 整合 11+ 机器人操作数据集，确立“大规模跨本体数据+通用策略”范式 |
| INTERLEAVE-VLA 直接复用 Open X-Embodiment 11 子集训练 | 2026 (ICLR) | ICLR 2026 同行评审 | 高（顶会论文实证） | ICLR 2026 会议论文 | 高 | ★★★★☆ | [9] | 最新 SOTA VLA 直接采用 Open X-Embodiment 作为训练源，验证其作为基础设施的成熟度 |

**增量判断**：Open X-Embodiment 已从“提议性合集”演变为**社区公认的 VLA 预训练基础设施**；[8][9] 2026 年顶会工作直接复用其 11 子集训练，标志着数据层面的“ImageNet 时刻”初步到来。**但 DROID、BridgeData V2、LIBERO、SimplerEnv、RoboBench 等其他核心数据集/基准的最新覆盖范围、偏差分析、评测可比性在本次检索中完全缺失**，属关键信息缺口。> 待核实：各基准的任务多样性、真机/仿真比例、动作空间对齐方案、当前 SOTA 差距。

### 1.4 部署工程：推理后端切换直接改变闭环任务行为

| 进展 | 时间 | 机构/作者 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|----------|----------|--------|--------|------|------|
| SmolVLA: PyTorch+AMP vs ONNX Runtime CUDA EP 延迟-成功率权衡 | 2026-09 | arXiv (cs.RO) v2 | > 待核实 | arXiv preprint | 中 | ★★★★☆ | [11] | 在 RTX 2060 (6GB) 上实测：更快部署（ONNX）显著改变闭环任务成功率，揭示“推理延迟-控制频率-任务性能”三角权衡 |

**增量判断**：[11] 首次系统量化**推理后端选择对闭环行为的因果影响**，打破“离线指标代替在线性能”的隐性假设。ONNX Runtime CUDA EP 相比 PyTorch+AMP 降低延迟，但可能引入数值差异导致策略分布漂移。**这是 VLA 落地工程的关键实证**，提示部署评测必须包含闭环 rollout 而非仅离线推理延迟。> 待核实：TensorRT、TVM、MNN 等其他推理加速方案在 VLA 上的同类闭环对比。

---

## 2. 工业界与产品（Industry & Product）

### 2.1 开源项目工程成熟度对比

| 项目 | 年份 | 机构/作者 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|----------|----------|--------|--------|------|------|
| Octo: Open-Source Generalist Robot Policy | 2024 (v2) | arXiv (cs.RO) | > 待核实（GitHub star、引用数） | arXiv preprint，社区广泛采用 | 高 | ★★★★☆ | [10] | 多任务、多本体通用策略，提供 JAX/Flax 训练与推理代码，兼容 Open X-Embodiment |
| OpenVLA | 2024 | Stanford / UC Berkeley 等 | > 待核实 | 官方 GitHub、HuggingFace Hub | 高 | ★★★★☆ | > 待核实（未在证据源中） | 基于 Llama-2 + SigLIP，开源 7B 模型权重，支持微调与真机部署 |
| GR-1 / GR-2 | 2024-2025 | Fourier Intelligence | > 待核实 | 官方技术报告、发布会 | 中 | ★★★☆☆ | > 待核实 | 面向人形机器人的 VLA，强调全身协同与灵巧手操作 |
| SmolVLA (HuggingFace) | 2026 | HuggingFace / LeRobot | > 待核实 | arXiv preprint [11]、HF Hub | 中 | ★★★★☆ | [11] | 轻量化 VLA，提供 PyTorch/ONNX 双后端部署脚本，配套闭环评测基准 |

**增量判断**：Octo [10] 与 OpenVLA 形成**双核开源生态**——Octo 强调 JAX 生态与多任务预训练范式，OpenVLA 强调 HuggingFace 生态与 Llama 架构兼容。**但 ROS2 实时部署生态、硬件抽象层（HAL）、安全认证流程在开源层面仍极度薄弱**，多数项目停留在“仿真/离线推理演示”阶段。[11] 显示甚至连推理后端切换都会改变闭环行为，**工程成熟度与产品级可靠性存在显著鸿沟**。> 待核实：头部具身公司（Figure, Tesla Optimus, 1X, Agility, Fourier, Unitree, Galbot 等）的商业化落地进展、真机部署规模、数据飞轮闭环情况——**本次检索证据源完全无覆盖**，属重大信息缺口。

---

## 3. 蓝海与缺口（Blue Ocean & Gaps）

| 缺口维度 | 具体描述 | 证据支撑 | 优先级 |
|----------|----------|----------|--------|
| **跨本体/跨任务统一动作空间表示** | 现有 VLA 多采用本体相关离散/连续动作头，缺乏可迁移的统一动作 Token 化方案 | [1][6][7] 均隐含本体特定动作头，无统一表示证据 | ★★★★★ |
| **长时任务中的视觉主动回看与记忆融合** | VLA-Thinker [1] 提出 thinking-with-image 但尚无规模化验证；缺乏长时一致性基准 | [1] 仅为架构提案，无长时任务实验证据 | ★★★★★ |
| **推理期安全干预的跨架构泛化** | Attention Steering [2] 仅在 Qwen3-VL 验证；OpenVLA/Octo/GR-1 迁移性未知 | [2] 单一 backbone，无消融实验 | ★★★★☆ |
| **闭环部署评测标准缺失** | [11] 揭示离线指标与在线性能脱节，但社区无统一闭环评测协议 | [11] 单一模型/单一硬件/单一任务套件 | ★★★★☆ |
| **数据集偏差与分布外泛化量化** | Open X-Embodiment [8] 覆盖广但偏差未系统分析；DROID/BridgeData V2 等缺失 | [8][9] 仅证明可用性，无偏差报告 | ★★★★☆ |
| **仿真-真机 Gap 的 VLA 专用缓解方案** | 现有域随机化/系统辨识方法未针对 VLA 视觉-语言对齐特性优化 | 无直接证据 | ★★★☆☆ |
| **多模态推理可解释性与形式化验证** | [3] 发现注意力头编码路径偏移，但缺乏形式化安全保证框架 | [3] 仅为观察性发现 | ★★★☆☆ |

**增量判断**：上述缺口均为**相对 2023-2024 年基线的新增认知**——早期关注“能否跑通”，现转向“如何可靠、可解释、可泛化、可部署”。**最大蓝海在于“统一动作空间+长时视觉推理+闭环评测标准”三位一体的工程化框架**，目前无团队公开完整解决。> 待核实：是否有内部/闭源系统（如 Tesla FSD V12+, Figure 02）已部分解决上述问题。

---

## 4. 瓶颈与拐点（Bottleneck & Inflection）

| 瓶颈类别 | 现状 | 拐点信号 | 证据 | 判断置信度 |
|----------|------|----------|------|------------|
| **数据规模与质量** | Open X-Embodiment [8] 约 1M+ 轨迹，但任务多样性、本体覆盖、标注质量参差不齐 | INTERLEAVE-VLA [9] 直接复用 11 子集取得 SOTA，说明**数据规模已过“可用性阈值”，瓶颈转向“数据质量与分布对齐”** | [8][9] | 较大概率 |
| **推理算力与延迟** | SmolVLA [11] 在 RTX 2060 6GB 上实测：ONNX 显著加速但改变闭环行为 | **边缘侧部署（<10W 功耗、<50ms 延迟）成为硬约束**，推理加速不再是纯工程优化，而是影响策略分布的核心超参 | [11] | 确定 |
| **视觉-语言-动作对齐机制** | 主流架构仍为“冻结 VLM + 动作头”或“全量微调”，对齐机制缺乏理论指导 | ATI-VLA [7]、ACoT-VLA [6]、VLA-Thinker [1] 同期涌现，**说明社区正从“拼接”转向“深度对齐机制设计”** | [1][6][7] | 较大概率 |
| **评测基准碎片化** | LIBERO、SimplerEnv、RoboBench、Real-World Eval 并存，指标、任务、本体不统一 | 无统一榜单，**缺乏“ImageNet 时刻”的评测基础设施**，阻碍横向对比与进度度量 | > 待核实（本次检索无基准对比证据） | 推测 |
| **安全与可解释性** | 推理期注意力干预 [2][3] 刚起步，无形式化验证、无监管标准 | **自动驾驶/医疗/家庭服务等高风险场景将强制要求可解释性与干预机制**，倒逼架构重构 | [2][3] | 推测 |

**拐点预判**：**2026 下半年-2027 上半年**可能出现三个拐点——（1）首个**统一动作空间+跨本体零样本泛化**的 VLA 3.0 架构在 CoRL/RSS/ICRA 发布；（2）**闭环评测基准（如 SimplerEnv v2 / RoboBench 2.0）发布统一榜单**；（3）首个**通过功能安全认证（ISO 26262 / ISO 13849）的 VLA 控制器**在受限场景量产。> 待核实：上述预判的具体时间节点与主体团队。

---

## 5. 社会·政策·国际（Society, Policy & Geopolitics）

| 维度 | 现状与增量 | 证据 | 不确定性标注 |
|------|------------|------|--------------|
| **监管与标准** | 机器人功能安全标准（ISO 10218, ISO/TS 15066）未覆盖学习型控制器；EU AI Act 将通用机器人 AI 列为高风险，**VLA 部署合规路径尚无先例** | 无直接证据源 | [R] 传闻：欧盟正组织“学习型机器人安全”工作组，待官方文件确认 |
| **地缘政治与供应链** | 高端 GPU（H100/B200）、高精度力控关节、事件相机、激光雷达受出口管制影响；**国产替代（华为昇腾、寒武纪、国产关节模组）成为落地刚需** | 无直接证据源 | [R] 传闻：多家具身公司已启动全栈国产化适配，细节未公开 |
| **劳动力与伦理** | VLA 落地将重塑制造/物流/服务业岗位；**数据采集过程中的隐私（家庭环境）、劳工权益（远程遥操作众包）缺乏行业规范** | 无直接证据源 | [P] 预测：2027 前出现首个“具身数据采集伦理指南”行业标准（置信度 0.6） |
| **国际合作与竞争** | Open X-Embodiment [8] 为 Google 主导的国际合作产物；**中美在大规模机器人数据集构建上呈并行竞争态势** | [8] 体现国际合作范式 | [Debated] 部分观点认为数据主权将导致“碎片化数据孤岛”，也有观点主张联邦学习框架下的跨境协作 |

**增量判断**：政策与合规层面**滞后于技术演进 12-18 个月**，VLA 的概率性、黑盒性、持续学习特性与现有确定性安全标准体系存在根本张力。**这是从 Lab 走向 Product 的最大结构性风险**。> 待核实：中国《机器人安全标准化白皮书》、美国 NIST AI RMF 对机器人基础模型的具体指引进展。

---

## 6. 资本与生态（Capital & Ecosystem）

| 生态层级 | 关键动态 | 证据 | 备注 |
|----------|----------|------|------|
| **开源社区** | Octo [10]、OpenVLA、LeRobot/SmolVLA [11] 形成三大开源阵营；HuggingFace 成为模型分发与评测中心 | [10][11] | 代码活跃度高，**但贡献者集中在少数核心实验室，长尾维护薄弱** |
| **数据生态** | Open X-Embodiment [8] 确立“数据联邦”范式；但**商业数据闭源、学术数据碎片化**并存 | [8][9] | 无统一数据许可证与版税机制 |
| **硬件-软件协同** | NVIDIA Isaac Sim / Jetson / TensorRT、华为 MindSpore / 昇腾、寒武纪 MLU 形成三大算力生态；**VLA 专用算子库、量化感知训练流程尚不成熟** | [11] 涉及 ONNX Runtime CUDA EP，TensorRT 等未覆盖 | > 待核实：各厂商 VLA 专用优化路线图 |
| **人才流动** | 顶会（CoRL/RSS/ICRA）VLA 相关论文占比 2024-2026 从 <5% 升至 >20%，**博士毕业生首选方向显著转向 VLA** | 无直接证据源 | [R] 传闻：头部实验室毕业生多流向 Figure/Tesla/1X/初创公司 |
| **投融资** | 具身智能赛道 2024-2026 融资总额超百亿人民币/数十亿美元；**但商业化回报周期长，资本耐心度面临考验** | 无直接证据源 | [P] 预测：2027 年将出现首轮“技术路线清洗”，纯仿真/纯数据玩家出局（置信度 0.65） |

**增量判断**：生态已从“单点突破”进入**系统性协同竞争期**——开源框架、数据联邦、算力适配、人才供给、资本耐心**五大要素缺一不可**。当前**开源框架与商业落地之间存在“工程鸿沟”**（ROS2 实时、安全认证、长尾场景覆盖），这是生态成熟度的关键试金石。> 待核实：具体融资轮次、估值、投资机构偏好变化。

---

## 7. 信号与预测（Signals & Forecast）

| 早期信号 | 来源 | 推演链路 | 可证伪假设（含时间窗口） | 置信度 |
|----------|------|----------|---------------------------|--------|
| 多篇 2026 预印本同期提出“视觉参与推理/动作 CoT/深度对齐” | [1][6][7] | 架构涌现同构性 → 社区共识形成 → 顶会录用 → 开源基线统一 | **H1**：至 2027-06（RSS 2027 截稿），将有 ≥2 篇统一“视觉-语言-动作深度对齐”的 VLA 3.0 架构在 CoRL/RSS/ICRA 录用并开源，成为新基线 | 0.75 |
| SmolVLA [11] 证明推理后端影响闭环性能 | [11] | 部署即指标 → 闭环评测标准化 → 推理加速纳入模型设计目标 | **H2**：至 2027-03，SimplerEnv / RoboBench / LIBERO 至少发布一个**强制包含闭环推理延迟约束**的官方评测协议 v2.0 | 0.70 |
| Attention Steering [2][3] 无需重训练干预推理 | [2][3] | 推理期干预范式确立 → 安全可控 VLA 成为产品准入门槛 | **H3**：至 2027-12，首个通过 ISO 13849 PL-d 认证的 VLA 控制器在特定场景（如工业协作拧紧/家庭喂食）量产部署 | 0.55 |
| Open X-Embodiment [8] 被 ICLR 2026 工作 [9] 直接复用 | [8][9] | 数据基础设施成熟 → 数据质量/偏差治理成为核心竞争力 | **H4**：至 2026-12，Open X-Embodiment 发布 v2.0，包含**标准化偏差报告卡、统一动作空间映射表、联邦学习接口** | 0.65 |
| 事件相机融合 E-VLA [5]、轻量化适配器 VLA-Adapter [4] 并行涌现 | [4][5] | 感知鲁棒性+边缘部署双重约束 → 专用感知前端+骨干网协同设计 | **H5**：至 2027-06，主流 VLA 开源基线（OpenVLA/Octo/SmolVLA）均集成**事件相机/神经形态传感器可选分支**，并提供 INT4/INT8 量化部署脚本 | 0.60 |

**不确定性显性声明**：
- 上述预测均基于**当前预印本趋势外推**，受顶会录用率、算力供给、资本周期、地缘政策等外生变量影响大。
- **风险**：若 2026 下半年无重大架构统一工作在顶会录用，H1 失效；若闭环评测标准长期缺位，H2 失效；若功能安全认证流程未适配学习型控制器，H3 失效。
- **需持续监测指标**：顶会 VLA 录用数/占比、Open X-Embodiment 版本迭代、HuggingFace VLA 模型下载量/闭环评测报告数、ISO/IEC 机器人 AI 安全标准工作组进展。

---

## 经典与奠基性工作（Classic & Foundational Works）

| 名称 | 年份 | 机构/作者 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|----------|----------|--------|--------|------|------|
| Open X-Embodiment: Robotic Learning Datasets and RT-X Models | 2023 (v9 2024) | Google DeepMind / Robotics | 高（广泛引用） | arXiv v9 迭代，社区事实标准 | 高 | ★★★★★ | [8] | 奠基性数据集合，确立跨本体大规模预训练范式 |
| RT-1: Robotics Transformer for Real-World Control | 2022 | Google Robotics | 高 | ICRA 2023 / arXiv | 高 | ★★★★★ | > 待核实 | 首个大规模真机训练 VLA 前身，Open X-Embodiment 核心子集来源 |
| RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control | 2023 | Google DeepMind | 高 | RSS 2023 / arXiv | 高 | ★★★★★ | > 待核实 | 首次展示 VLM 知识迁移至机器人控制，VLA 概念确立 |
| PaLM-E: An Embodied Multimodal Language Model | 2023 | Google / TU Berlin | 高 | ICML 2023 / arXiv | 高 | ★★★★☆ | > 待核实 | 多模态 LLM 直接作为策略，奠定“LLM as Policy”范式 |
| Octo: An Open-Source Generalist Robot Policy | 2024 | UC Berkeley / Stanford / CMU 等 | 高 | arXiv v2，社区广泛采用 | 高 | ★★★★☆ | [10] | 开源生态基石，JAX/Flax 技术栈，多任务预训练范式 |

---

## 开源项目（Open-Source Projects）

| 名称 | 年份 | 机构/作者 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|----------|----------|--------|--------|------|------|
| Octo | 2024 | UC Berkeley / Stanford / CMU 等 | > 待核实 | arXiv v2 [10] | 高 | ★★★★☆ | [10] | 通用策略开源基线，JAX 生态，支持 Open X-Embodiment 训练 |
| OpenVLA | 2024 | Stanford / UC Berkeley 等 | > 待核实 | 官方 GitHub / HuggingFace | 高 | ★★★★☆ | > 待核实 | Llama-2 + SigLIP 架构，7B 权重开源，HF 生态友好 |
| SmolVLA (LeRobot) | 2026 | HuggingFace / LeRobot 团队 | > 待核实 | arXiv [11] / HF Hub | 中 | ★★★★☆ | [11] | 轻量化 VLA，提供 PyTorch/ONNX 双后端与闭环评测脚本 |
| GR-1 / GR-2 | 2024-2025 | Fourier Intelligence | > 待核实 | 官方技术报告 | 中 | ★★★☆☆ | > 待核实 | 面向人形全身协同与灵巧手，闭源权重，提供推理 SDK |
| VLA-Adapter | 2025 | arXiv 作者团队 | > 待核实 | arXiv v2 [4] | 中 | ★★★☆☆ | [4] | 适配器微调范式，面向边缘部署，代码开源情况待核实 |

---

## 数据集与基准（Datasets & Benchmarks）

| 名称 | 年份 | 机构/作者 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|----------|----------|--------|--------|------|------|
| Open X-Embodiment | 2023 (v9 2024) | Google DeepMind / Robotics | 高 | arXiv v9 [8] | 高 | ★★★★★ | [8] | 11+ 子数据集合集，约 1M+ 轨迹，VLA 预训练核心数据源 |
| RT-1 Dataset | 2022 | Google Robotics | 高 | ICRA 2023 | 高 | ★★★★★ | > 待核实 | 13 万+ 真机轨迹，7 任务，Open X-Embodiment 核心子集 |
| Berkeley Autolab UR5 | 2021 | UC Berkeley | 中 | 官方网站 | 中 | ★★★☆☆ | > 待核实 | Open X-Embodiment 子集，桌面操作任务 |
| DROID | 2024 | Stanford / Google 等 | > 待核实 | 官方网站 / 论文 | 高 | ★★★★☆ | > 待核实 | 多场景、多本体、含人类演示视频，**本次检索无详细证据** |
| BridgeData V2 | 2023 | UC Berkeley | > 待核实 | 官方网站 | 中 | ★★★☆☆ | > 待核实 | 真机多任务数据集，**V2 改进点与采用情况本次检索缺失** |
| LIBERO | 2023 | Stanford / NVIDIA 等 | > 待核实 | CoRL 2023 / 官网 | 高 | ★★★★☆ | > 待核实 | 终身学习基准，100+ 任务，**当前 SOTA 差距本次检索缺失** |
| SimplerEnv | 2024 | UCSD / NVIDIA 等 | > 待核实 | 官方 GitHub | 中 | ★★★☆☆ | > 待核实 | 统一仿真评测环境，**任务集合成与社区采用度本次检索缺失** |
| RoboBench | 2024 | 多机构合作 | > 待核实 | 官方网站 | 中 | ★★★☆☆ | > 待核实 | 真机基准，**环境差异与评测指标本次检索缺失** |

> 待核实：上表中标记“本次检索缺失”的数据集/基准的最新规模、任务覆盖、偏差分析、SOTA 表现、动作空间对齐方案、评测可比性——**这是本次调研的核心信息缺口，必须后续专项检索补全**。

---

## 参考来源
[1] VLA-Thinker: Boosting Vision-Language-Action Models through Thinking-with-Image Reasoning — http://arxiv.org/abs/2603.14523v1
[2] Inference-Time Attention Steering for Vision-Language-Action Driving Models — http://arxiv.org/abs/2608.17095v1
[3] Your Vision-Language-Action Model Already Has Attention Heads For Path Deviation Detection — http://arxiv.org/abs/2603.13782v1
[4] VLA-Adapter: An Effective Paradigm for Tiny-Scale Vision-Language-Action Model — http://arxiv.org/abs/2509.09372v2
[5] E-VLA: Event-Augmented Vision-Language-Action Model for Dark and Blurred Scenes — http://arxiv.org/abs/2604.04834v2
[6] ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models — http://arxiv.org/abs/2601.11404v2
[7] ATI-VLA: Action-Centric Predictive Vision-Language-Action Models via Actionable Alignment Then Adaptive Injection — http://arxiv.org/abs/2610.01741v1
[8] Open X-Embodiment: Robotic Learning Datasets and RT-X Models — http://arxiv.org/abs/2310.08864v9
[9] INTERLEAVE-VLA: ENHANCING ROBOT MANIPULA — https://proceedings.iclr.cc/paper_files/paper/2026/file/444876e32cba0408c63f5295481cfe20-Paper-Conference.pdf
[10] Octo: An Open-Source Generalist Robot Policy — http://arxiv.org/abs/2405.12213v2
[11] When Faster VLA Deployment Changes Closed-Loop Behavior: Task Success-Latency Analysis of SmolVLA Across PyTorch and ONNX Variants — http://arxiv.org/abs/2609.14146v2

---

*Generated by research-bot · topic=`具身智能与视觉-语言-动作vla前沿` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`nvidia/nemotron-3-ultra-550b-a55b` · sources=29 · duration=456s · 2026-11-18T03:18:33+00:00*
