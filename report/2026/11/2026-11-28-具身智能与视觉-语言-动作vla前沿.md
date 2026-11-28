# 具身智能与视觉-语言-动作（VLA）前沿调研报告

**日期**：2026-11-28（UTC）  
**领域**：Embodied AI / Vision-Language-Action (VLA) / Robot Learning  
**检索源数量**：36 条可引用来源（[1]-[2]）  
**方法论**：deep-research + frontier-tracking + paper-survey + evidence-grading + frontier-watch

---

## 1. 进展与热点（Progress & Hotspots）

### 1.1 一句话增量判断
**相对 2024 年基线，2024-2026 年 VLA 领域的核心增量在于：从“端到端单体策略”向“可控推理、工具增强智能体、大规模真机数据扩展”三大方向演进，且出现首批 100k+ 小时真机轨迹级基础模型。**

### 1.2 关键模型与架构演进（近 1-2 年）

| 名称 | 年份 | 机构/作者 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|----------|----------|--------|--------|------|------|
| Inference-Time Attention Steering (Alpamayo-R1/Qwen3-VL) | 2026 | 未明确（arXiv） | > 待核实 | arXiv 预印本 (cs.CV, 2026-08-17) [3] | 中：新颖推理时干预范式，合成数据验证 | ★★★★☆：免重训练注意力控制，VLA 安全性关键探索 | [3] | 有界加性 pre-softmax 注意力偏置，50 变道场景平均横向位移 ~17 cm，最大 ~140 cm，剂量-响应单调 |
| ART (Agentic Robot with Tool-use) | 2026 | 未明确（arXiv v3） | > 待核实 | arXiv 预印本 (cs.RO, 2026-08-14, v3) [4] | 中高：VLA+工具使用早期系统性探索 | ★★★★☆：工具注入范式工程落地潜力大 | [4] | 将任意 VLA 扩展为即时工具使用智能体，注入低级视觉/高级可供性/本体增强工具 |
| CCFT (Compositional Context Fine-Tuning) | 2026 | 未明确（arXiv） | > 待核实 | arXiv 预印本 (cs.CV, 2026-07-12) [5] | 中：面向装配细粒度手-物交互 | ★★★☆☆：结构化微调思路，下游闭环待验证 | [5] | 将装配动作分解 Verb/Object/Tool 三语义元素分别微调 |
| Motion Image Diffusion 双头架构 | 2025 | 未明确（arXiv） | > 待核实 | arXiv 预印本 (cs.RO, 2025-12) [6] | 中：针对 VLA 运动推理短板 | ★★★★☆：核心瓶颈分析+可复现方案 | [6] | 联合学习动作预测与光流运动图像扩散，增强预测性运动推理 |
| Scaling Sim-to-Real VLA RL with Generative 3D Worlds | 2026 | 未明确（arXiv v4） | > 待核实 | arXiv 预印本 (cs.RO, 2026-03, v4) [7] | 中高：Sim-to-Real 扩展路径 | ★★★★☆：生成式 3D 世界缩小 Sim-to-Real Gap | [7] | 用生成式 3D 世界支撑大规模 VLA RL 微调，规避真机采样成本 |
| Envisioning Agentic Robotics | 2026 | 未明确（arXiv v2） | > 待核实 | arXiv 预印本 (cs.RO, 2026-11, v2) [8] | 高：定义 Agentic Robotics 新范式 | ★★★★☆：前沿愿景定性，引用 GPT-6 Astra 等 | [8] | 提出“智能体机器人”范式：通用前沿模型+智能体框架替代任务专用策略 |
| Xiaomi-Robotics-1 | 2026 | Xiaomi Robotics | > 待核实 | arXiv 预印本 (cs.RO, 2026-07, v2) [9] | 高：100k+ 小时真机轨迹基础模型 | ★★★★★：规模化真机数据里程碑 | [9] | 100k+ 小时真机轨迹，移动操作零样本泛化，少量微调适配新任务 |
| Meituan-Robotics-0 (MR0) | 2026 | Meituan Robotics | > 待核实 | arXiv 预印本 (cs.RO, 2026-11, v3) [10] | 高：桌面操作 15k 小时+1.47 亿 V-L 样本 | ★★★★★：工业级桌面操作基础模型 | [10] | 三阶段训练，12 本体 15,060 小时轨迹，桌面操作 SOTA |
| Action Flow Matching for Continual Robot Learning | 2025 | 未明确（arXiv v2） | > 待核实 | arXiv 预印本 (cs.RO, 2025-04, v2) [2] | 中：持续学习新范式 | ★★★★☆：Flow Matching 解决灾难性遗忘 | [2] | 基于流匹配的持续机器人学习，避免重放缓冲区 |

### 1.3 SOTA 基准与竞赛进展

| 基准/竞赛 | 年份 | 机构/平台 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 链接 | 说明 |
|-----------|------|-----------|----------|----------|--------|--------|------|------|
| MOASEI 2026 (AAMAS) | 2026 | AAMAS 2026 | > 待核实 | AAMAS 2026 竞赛技术报告 [11] | 低：仅 1 队提交最终方案 | ★★☆☆☆：多智能体基准，VLA 关联弱 | [11] | 保留野火/网安/网约车三赛道，新增帧开放性野火；8 队注册仅 1 队提交（网约车赛道） |
| BEHAVIOR Challenge 2025 | 2025 | 未明确 | > 待核实 | arXiv 预印本 [12] | 中：任务适配方案获一等奖 | ★★★☆☆：VLA 任务适配实战参考 | [12] | VLA 任务适配一等奖方案，细节需全文确认 |

> 待核实：LIBERO、Open X-Embodiment、DROID、SimplerEnv、RoboArena 等主流 VLA 基准在 2024-2026 年的最新榜单排名与 SOTA 变动，当前证据源未覆盖。

---

## 2. 工业界与产品（Industry & Product）

### 2.1 一句话增量判断
**头部科技公司（小米、美团、Hugging Face）在 2026 年集中发布大规模真机数据训练的 VLA 基础模型与全栈开源工程库，标志着 VLA 从实验室走向工程化落地的基础设施就绪期。**

### 2.2 核心开源框架与工程栈

| 名称 | 年份 | 机构/作者 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|----------|----------|--------|--------|------|------|
| LeRobot | 2026 | Hugging Face (16 作者) | > 待核实 | arXiv 预印本 (cs.RO, 2026-02) [13] | 高：官方维护、全栈覆盖、近期发布 | ★★★★★：生产级全栈库，VLA 落地首选 | [13] / GitHub | 覆盖数据收集、训练、评估、部署全栈，解决工具碎片化痛点 |
| Octo | 2024 | Octo Models 团队 | > 待核实 | arXiv 预印本 (cs.RO, 2024-05, v2) [14] | 高：早期开源通用策略代表 | ★★★★☆：经典基线，可直接下载权重微调 | [14] / 官网 | 大规模预训练通用策略，少量 in-domain 数据微调跨任务/本体泛化 |
| Awesome-VLA | 持续 | yueen-ma (社区) | > 待核实 | 社区 GitHub 仓库 [15] | 中：聚合导航入口 | ★★★☆☆：快速检索全景资源，需回溯一手来源 | [15] | 汇总 OpenVLA 等核心模型、论文、代码链接 |

### 2.3 产业级基础模型发布

| 模型 | 发布时间 | 公司 | 核心指标 | 权威证据 | 关注度 | 推荐度 | 链接 | 说明 |
|------|----------|------|----------|----------|--------|--------|------|------|
| Xiaomi-Robotics-1 | 2026-07 (v2) | Xiaomi Robotics | 100k+ 小时真机轨迹，移动操作零样本泛化 | arXiv [9] | 高：规模化真机数据里程碑 | ★★★★★ | [9] | 多样语言指令跟随，少量微调适配新任务 |
| Meituan-Robotics-0 (MR0) | 2026-11 (v3) | Meituan Robotics | 15,060 小时轨迹 + 1.47 亿 V-L 样本，12 本体 | arXiv [10] | 高：工业级桌面操作基础模型 | ★★★★★ | [10] | 三阶段训练，桌面操作 SOTA，具身智能体系统 |

> 待核实：Google DeepMind (RT-X, RT-2 系列)、NVIDIA (GR00T, Isaac Lab)、Tesla (Optimus)、Figure AI、1X Technologies、Agility Robotics 等头部玩家 2024-2026 年最新产品发布、真机部署规模与商业化进展，当前证据源未覆盖。

---

## 3. 蓝海与缺口（Blue Ocean & Gaps）

### 3.1 一句话增量判断
**当前 VLA 领域存在四大高杠杆蓝海：(1) 统一的“VLA+工具/智能体”评测基准缺失；(2) 免重训练的推理时可控性/安全性机制在真机长时程任务中的系统性验证；(3) 细粒度动作理解到端到端策略闭环的桥接范式；(4) 生成式 3D 世界驱动的 Sim-to-Real VLA RL 规模化管线。**

### 3.2 结构化缺口清单

| 缺口编号 | 缺口描述 | 证据来源 | 优先级 | 潜在切入点 |
|----------|----------|----------|--------|------------|
| Gap-1 | **VLA+工具/智能体统一基准缺失**：ART 等工作缺乏标准化基准对比，无法量化工具注入收益 | [4] | 高 | 建立包含工具调用、长时程规划、多技能切换的统一评测套件 |
| Gap-2 | **推理时注意力/干预机制真机验证不足**：Alpamayo-R1 仅在合成数据集 50 变道场景验证，真机多任务泛化未知 | [3] | 高 | 真机多场景（导航、操作、交互）系统性评测注意力引导的安全边界 |
| Gap-3 | **细粒度动作理解→端到端策略闭环断层**：CCFT 等停留在动作识别/理解，未接入 VLA 策略学习验证下游性能提升 | [5] | 中 | 设计“理解-策略”联合训练或两阶段管线，量化理解质量对策略成功率的贡献 |
| Gap-4 | **生成式 3D 世界驱动 VLA RL 规模化管线未成熟**：Scaling Sim-to-Real VLA RL 提出但工程落地细节（世界模型保真度、奖励设计、分布偏移）待解 | [7] | 高 | 端到端管线：生成式 3D 场景→多样化任务生成→VLA RL 微调→Sim-to-Real 部署 |
| Gap-5 | **持续/终身学习基准缺失**：Action Flow Matching [2] 提出持续学习方案，但缺乏标准化灾难性遗忘评测协议 | [2] | 中 | 定义任务序列、遗忘指标、前向迁移指标的持续 VLA 学习基准 |
| Gap-6 | **多模态推理链可解释性**：VLA 内部决策过程（视觉→语言→动作）缺乏可解释性工具与评测 | [3] [4] | 中 | 引入注意力可视化、概念瓶颈、因果干预等可解释性方法进 VLA 评测标准 |

> 待核实：数据高效 VLA（<1k 轨迹实用化）、跨本体统一动作空间标准化、实时推理加速（量化/蒸馏/专家混合）工程落地成熟度。

---

## 4. 瓶颈与拐点（Bottleneck & Inflection）

### 4.1 一句话增量判断
**核心瓶颈正从“模型架构”向“数据规模与质量、Sim-to-Real 闭环、真机部署工程化”转移；拐点信号为：100k+ 小时真机数据集发布、全栈开源工程库成熟、Agentic Robotics 范式形成。**

### 4.2 关键瓶颈分析

| 瓶颈 | 现状描述 | 证据来源 | 严重度 | 拐点信号 |
|------|----------|----------|--------|----------|
| **运动推理缺失** | 典型 VLA 仅模仿专家轨迹，缺乏预测性运动推理 | [6] | 高 | Motion Image Diffusion 双头架构提供可验证改进路径 |
| **Sim-to-Real Gap** | 仿真训练策略真机部署性能大幅下降，真机数据采集成本高 | [7] | 高 | 生成式 3D 世界+大规模 RL 微调管线雏形出现 |
| **长时程/多任务鲁棒性** | 单体 VLA 在长时程、多技能切换任务中易失败 | [4] | 高 | ART 工具注入、Agentic Robotics 范式尝试破局 |
| **真机数据规模不足** | 学术界公开真机轨迹数据集通常 <10k 小时，远小于视觉/语言预训练规模 | [9] [10] | 中 | 小米 100k+ 小时、美团 15k 小时真机数据集发布 |
| **工程基础设施碎片化** | 数据收集、训练、评估、部署工具链割裂、闭源 | [13] | 中 | LeRobot 全栈开源库发布，Hugging Face 官方维护 |
| **评测基准碎片化/不统一** | 缺乏覆盖“感知-推理-动作-工具-长时程”全链路的统一基准 | [11] [12] | 中 | BEHAVIOR Challenge 等任务级竞赛存在，但全链路基准缺失 |

### 4.3 拐点判断与依据

| 拐点假设 | 判断依据 | 置信度 | 可证伪条件 |
|----------|----------|--------|------------|
| **P1: 2026-2027 年真机数据规模将成为 VLA 竞争核心护城河** | 小米 100k+ 小时、美团 15k 小时基础模型发布 [9][10] | 较大概率 | 若 2027 年底学术界开源数据集规模追平工业界，或合成数据完全替代真机数据 |
| **P2: Agentic Robotics（VLA+LLM 规划+工具）将在 2027 年成为主流范式** | ART [8][4]、Envisioning Agentic Robotics [8] 理论奠基 | 推测 | 若纯端到端 VLA 在长时程基准上持续超越 Agentic 方案 |
| **P3: 生成式 3D 世界将在 2026-2027 年实现 Sim-to-Real “零样本”迁移** | Scaling Sim-to-Real VLA RL [7] 提出管线 | 推测 | 若真机部署仍需大量真机微调（>1k 轨迹） |
| **P4: 全栈开源工程库将在 2026 年底前实现“开箱即用”生产级部署** | LeRobot [13] 覆盖全栈，HF 官方维护 | 确定 | 若 LeRobot 社区活跃度下降或出现重大架构重构不兼容 |

> 风险：上述拐点均面临**算力成本**、**数据隐私/合规**、**真机安全监管**三大不确定约束。

---

## 5. 社会·政策·国际（Society, Policy & Geopolitics）

### 5.1 一句话增量判断
**当前证据源未直接覆盖 VLA 领域的政策法规、地缘政治、供应链、伦理劳动影响等社会外部性；需引入外部政策追踪源补充。**

### 5.2 已知信号与缺口

| 维度 | 已知信号 | 证据来源 | 评估 |
|------|----------|----------|------|
| **监管/标准** | 无直接证据 | - | > 待核实：ISO/TC 299 机器人标准、EU AI Act 对具身 AI 影响、中国《机器人+》应用行动方案等 |
| **地缘/供应链** | 无直接证据 | - | > 待核实：高端 GPU/传感器/精密减速器出口管制对 VLA 训练与本体制造的影响 |
| **伦理/劳动** | 无直接证据 | - | > 待核实：VLA 替代人工操作的就业影响、责任归属、数据隐私（家庭/工厂采集） |
| **国际合作/竞争** | 头部模型多来自中美企业/实验室 | [9][10] | 中美在大规模真机数据、基础模型发布上呈并行竞争态势 |

> 待核实：需引入政策文件库、行业协会发布、智库报告作为独立证据源。

---

## 6. 资本与生态（Capital & Ecosystem）

### 6.1 一句话增量判断
**资本关注点从“单一模型创业”转向“全栈基础设施+垂直场景数据飞轮”，Hugging Face 等平台型玩家通过开源生态构建护城河；头部科技大厂内部孵化为主，独角兽融资轮次趋于理性。**

### 6.2 生态关键节点

| 节点 | 角色 | 关键动作/信号 | 证据来源 | 评估 |
|------|------|---------------|----------|------|
| **Hugging Face** | 平台/基础设施 | 发布 LeRobot 全栈库 [13]，聚合模型/数据/空间 | [13] [15] | 核心生态枢纽，降低 VLA 入门门槛 |
| **Xiaomi / Meituan** | 垂直场景数据持有者 | 发布 100k+/15k 小时真机基础模型 [9][10] | [9][10] | 数据飞轮闭环：业务场景→数据→模型→业务增强 |
| **学术开源社区** | 基线/创新源 | Octo [14]、Motion Diffusion [6]、Action Flow Matching [2] | [14][6][2] | 提供可复现基线与方法创新，但工程化程度参差 |
| **Awesome-VLA 等聚合仓库** | 知识导航 | 汇总论文/模型/代码 [15] | [15] | 降低信息检索成本，非权威来源 |

> 待核实：2024-2026 年 VLA 相关融资轮次、金额、估值变化；核心人才流动（学术界→产业界、大厂→创业）；开源社区贡献者活跃度指标（PR、Issue、Star 增长）。

---

## 7. 信号与预测（Signals & Forecast）

### 7.1 早期信号汇总

| 信号 | 来源 | 时间 | 证据强度 | 含义 |
|------|------|------|----------|------|
| 100k+ 小时真机轨迹基础模型发布 | Xiaomi-Robotics-1 [9] | 2026-07 | 确定 | 真机数据规模进入“百万小时级”竞赛 |
| 桌面操作 15k 小时+1.47 亿 V-L 样本模型 | Meituan-Robotics-0 [10] | 2026-11 | 确定 | 垂直场景大模型落地成熟度跃升 |
| 全栈开源工程库 LeRobot 发布 | Hugging Face [13] | 2026-02 | 确定 | 工程基础设施就绪，降低部署门槛 |
| Agentic Robotics 范式显性提出 | Envisioning Agentic Robotics [8] | 2026-11 | 推测 | 范式从“单体策略”向“智能体系统”转型 |
| 生成式 3D 世界支撑 VLA RL | Scaling Sim-to-Real VLA RL [7] | 2026-03 (v4) | 推测 | Sim-to-Real 瓶颈有望通过生成式世界缓解 |
| 推理时注意力免重训练控制 | Alpamayo-R1 [3] | 2026-08 | 推测 | VLA 可控性/安全性新技术路线 |
| VLA 运动推理短板被显性化并给出双头扩散方案 | Motion Image Diffusion [6] | 2025-12 | 确定 | 核心架构瓶颈获得针对性改进方向 |
| 持续学习引入 Flow Matching | Action Flow Matching [2] | 2025-04 | 推测 | 灾难性遗忘问题有新数学工具 |

### 7.2 未来 6-18 月预测（可证伪假设）

| 编号 | 预测假设 | 依据链 | 置信度 | 可证伪观测指标（截止 2027-06） |
|------|----------|--------|--------|----------------------------------|
| **F1** | **至少 3 家公司/实验室发布 >500k 小时真机轨迹训练的 VLA 基础模型** | 小米 100k [9]、美团 15k [10] 起步，数据飞轮效应显现 | 较大概率 | 统计 arXiv/官方博客发布的模型卡真机小时数 |
| **F2** | **LeRobot 成为 GitHub 星标增速最快的机器人学习库（月增 >2k stars）** | HF 官方维护 [13]、全栈覆盖、社区生态 | 较大概率 | GitHub Insights 星标增长曲线 |
| **F3** | **出现首个“VLA+工具使用”标准化基准（含 ≥10 种工具、≥50 任务、真机评测协议）** | ART [4] 缺基准、Agentic 范式 [8] 推动 | 推测 | 会议/期刊/官网发布基准论文及评测服务器 |
| **F4** | **生成式 3D 世界实现 VLA 策略零样本 Sim-to-Real 成功率 >60%（在 ≥10 真机任务）** | Scaling Sim-to-Real VLA RL [7] 管线提出 | 推测 | 独立第三方复现报告或基准榜单 |
| **F5** | **推理时注意力干预在真机自动驾驶/导航任务中将碰撞率降低 >30%（对比无干预基线）** | Alpamayo-R1 合成数据剂量-响应 [3] | 推测 | 真机实验论文/技术报告披露碰撞率对比 |
| **F6** | **持续 VLA 学习基准（任务序列≥20、遗忘率指标）被社区采纳为标准评测** | Action Flow Matching [2] 提出方案但缺基准 | 推测 | CoRL/ICRA/ICLR 等顶会出现基准论文或官方评测网站 |

> 不确定：宏观算力供给、地缘政治冲击、监管政策突变可能使上述预测失效。

---

## 参考来源
[1] Refined CMA-ES for CEC 2026 Bound-Constrained Single-Objective Optimization — http://arxiv.org/abs/2611.04620v1
[2] Action Flow Matching for Continual Robot Learning — http://arxiv.org/abs/2504.18471v2
[3] Inference-Time Attention Steering for Vision-Language-Action Driving Models — http://arxiv.org/abs/2608.17095v1
[4] Evolve Vision-Language-Action Model into an Agent with On-the-fly Tool-use — http://arxiv.org/abs/2608.14047v3
[5] Compositional Context Fine-Tuning Vision-Language Model for Complex Assembly Action Understanding from Videos — http://arxiv.org/abs/2607.10797v1
[6] Robotic VLA Benefits from Joint Learning with Motion Image Diffusion — http://arxiv.org/abs/2512.18007v1
[7] Scaling Sim-to-Real VLA Reinforcement Learning with Generative 3D Worlds — http://arxiv.org/abs/2603.18532v4
[8] Envisioning Agentic Robotics: A New Era of Robotic Systems — http://arxiv.org/abs/2611.18359v2
[9] Xiaomi-Robotics-1: Scaling Vision-Language-Action Models with over 100K Hours of Real-World Trajectories — http://arxiv.org/abs/2607.15330v2
[10] Meituan-Robotics-0: A Vision-Language-Action Foundation Model for Desktop Manipulation — http://arxiv.org/abs/2611.08577v3
[11] Second MOASEI Competition at AAMAS'2026: A Technical Report — http://arxiv.org/abs/2607.03399v1
[12] Task adaptation of Vision-Language-Action model: 1st Place Solution for the 2025 BEHAVIOR Challenge — http://arxiv.org/abs/2512.06951v2
[13] LeRobot: An Open-Source Library for End-to-End Robot Learning — http://arxiv.org/abs/2602.22818v1
[14] Octo: An Open-Source Generalist Robot Policy — http://arxiv.org/abs/2405.12213v2
[15] Awesome-VLA - yueen-ma - GitHub — https://github.com/yueen-ma/awesome-vla

---

*Generated by research-bot · topic=`具身智能与视觉-语言-动作vla前沿` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`nvidia/nemotron-3-ultra-550b-a55b` · sources=36 · duration=342s · 2026-11-28T03:41:50+00:00*
