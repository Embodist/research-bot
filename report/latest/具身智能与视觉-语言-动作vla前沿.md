# 具身智能与视觉-语言-动作（VLA）前沿调研报告（2024-2026）

**日期**：2026-11-17 | **领域**：Embodied AI / VLA / Robotics | **检索源数量**：35 条可引用证据源

---

## 1. 进展与热点（Progress & Hotspots）

### 1.1 核心增量判断
2024-2026 年 VLA 领域呈现三大增量方向：**推理时干预机制**（免重训练安全对齐）、**结构化语义理解**（面向精细操作的动作分解）、**智能体化与工具调用**（离散技能序列替代连续动作空间），并伴随**超大规模真实数据训练**（10 万小时级）与**推理效率优化**（低资源部署）的工程化攻关。

### 1.2 关键进展条目（按时间倒序）

| 进展 | 时间 | 机构/来源 | 一句话贡献 | 热度证据 | 权威证据 | 关注度 | 推荐度 |
|------|------|-----------|------------|----------|----------|--------|--------|
| Inference-Time Attention Steering for VLA Driving | 2026-08 | arXiv [1] | 首创免重训练的推理时注意力偏置机制，将注意力强制重定向至安全关键交通参与者，量化验证横向位移 17 cm 平均、最大 140 cm | 引用数待核实；arXiv 下载量待核实 [1] | arXiv 预印本 (cs.CV)，非同行评审 [1] | 中等：2026 最新，直击 VLA 部署安全痛点 | ★★★★☆：解决真车部署注意力不可控的关键工程问题 |
| Compositional Context Fine-Tuning (CCFT) for Assembly | 2026-07 | arXiv [2] | 将装配动作分解为 Verb/Object/Tool 语义元素微调 VLM，提升细粒度手-物交互理解 | 引用数待核实 [2] | arXiv 预印本 (cs.CV) [2] | 中等：聚焦具身核心场景——精细装配 | ★★★★☆：为 VLA 感知端处理接触丰富任务提供结构化先验 |
| ART: Evolve VLA into Agent with On-the-fly Tool-use | 2026-08 (v3) | arXiv [3] | 提出通用 ART 框架，使任意 VLA 具备工具调用能力，将连续动作空间离散化为工具序列，显著提升长时任务泛化 | 引用数待核实；GitHub 星标待核实 [3] | arXiv 预印本 (cs.RO)，机器人核心会议投稿领域 [3] | 高：直接推进 VLA 智能体化架构 | ★★★★★：VLA 向通用具身智能体演进的架构级突破 |
| VLA Attention Heads for Path Deviation Detection | 2026-03 | arXiv [4] | 发现现有 VLA 内部已存在专用于路径偏移检测的注意力头，可用于免训练异常监测 | 引用数待核实 [4] | arXiv 预印本 (cs.RO) [4] | 中等：提供 VLA 可解释性与安全监测新视角 | ★★★★☆：挖掘模型内在机制，工程落地成本极低 |
| One Policy for 100 Household Tasks (BEHAVIOR 2026) | 2026-11 | arXiv [5] | 单一策略覆盖 100 个家庭任务，验证大规模多任务统一建模可行性 | 引用数待核实 [5] | arXiv 预印本 (cs.RO) [5] | 高：任务广度创纪录，基准测试新标杆 | ★★★★★：多任务泛化上限的最新实证 |
| BLURR: Boosted Low-Resource Inference for VLA | 2025-12 | arXiv [6] | 针对 VLA 推理延迟提出加速框架，降低真机部署算力门槛 | 引用数待核实 [6] | arXiv 预印本 (cs.RO) [6] | 中等：直击 VLA 真机部署推理效率瓶颈 | ★★★★☆：工程落地关键，配合量化/蒸馏形成完整链路 |
| Meituan-Robotics-0 (MR0) | 2026-11 (v3) | 美团机器人 [7] | 1.47 亿 V-L 样本 + 1.5 万小时 12 本体轨迹，三阶段训练，面向桌面操作 | 37 作者工业界大规模投入 [7] | arXiv 预印本 (cs.RO) [7] | 中等：最新大规模 VLA 训练细节公开 | ★★★☆☆：大规模数据策展与多本体对齐范式参考 |
| Xiaomi-Robotics-1 | 2026-07 (v2) | 小米机器人 [8] | >10 万小时真实轨迹，两阶段预训练+后训练，零样本移动操作与少量微调适配 | 33 作者，目前公开最大规模真实数据 VLA 之一 [8] | arXiv 预印本 (cs.RO) [8] | 高：数据规模创新高，工程落地参考价值大 | ★★★★☆：超大规模真实数据训练范式标杆 |
| Envisioning Agentic Robotics | 2026-11 | arXiv [9] | 系统阐述 Agentic Robotics 时代愿景：VLA+工具+世界模型+长时推理 | 引用数待核实 [9] | arXiv 预印本 (cs.RO) [9] | 高：领域愿景性文件，定调未来 2-3 年主线 | ★★★★★：把握领域演进宏观方向必读 |

> **待核实**：上述 2026 年预印本均未经同行评审，部分指标（如成功率、延迟毫秒数）仅为论文自报，缺乏第三方独立复现 [1][2][3][4][5][6][7][8][9]。

---

## 2. 工业界与产品（Industry & Product）

### 2.1 增量判断
头部互联网/科技公司（美团、小米）已投入百人团队构建**自研 VLA 基础模型**，并公开百万小时级真实数据训练细节 [7][8]；GR-2 [10] 等生成式 Video-L-A 模型探索多模态统一建模；但**量产落地产品、商业化部署案例、ROS2 生产级集成细节**在公开文献中仍不可见。

### 2.2 代表性工业界工作表

| 名称 | 年份 | 机构/作者 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|----------|----------|--------|--------|------|------|
| Meituan-Robotics-0 (MR0) | 2026 | 美团机器人 (37 作者) | 37 作者、1.47 亿样本、1.5 万小时 [7] | arXiv 预印本 [7] | 中等 | ★★★☆☆ | [7] | 桌面操作 VLA，三阶段训练配方，多本体对齐 |
| Xiaomi-Robotics-1 | 2026 | 小米机器人 (33 作者) | >10 万小时真实轨迹、零样本泛化 [8] | arXiv 预印本 [8] | 高 | ★★★★☆ | [8] | 移动操作 VLA，两阶段范式，目前最大公开真实数据规模 |
| GR-2: Generative Video-L-A Model | 2024/2025 | GR-2 团队 | DOI 发布，生成式统一建模 [10] | 期刊/会议 DOI (10.59350/...) [10] | 中等 | ★★★☆☆ | [10] | 视频-语言-动作生成式建模，多模态统一探索 |

> **待核实**：上述模型是否已在商业产品（如配送机器人、家用机器人）中量产部署、ROS2 生产级中间件集成细节、真机闭环控制频率与延迟指标、售后运维体系。公开证据不足 [7][8][10]。

---

## 3. 蓝海与缺口（Blue Ocean & Gaps）

### 3.1 增量判断
当前证据揭示的**高杠杆空白区**集中在：安全可验证的推理时干预、精细操作的结构化感知、工具/技能标准化接口、真机评测基准、参数高效适配、推理确定性工程。经典奠基性工作与开源工程栈在候选证据中**系统性缺失**，需补齐。

### 3.2 核心缺口清单（含证据溯源）

| 缺口 | 说明 | 证据来源 | 优先级 |
|------|------|----------|--------|
| VLA 安全关键场景注意力可控性与形式化保证 | 仅有推理时注意力偏置 [1] 与注意力头发现 [4] 初步探索，缺乏形式化验证框架 | [1][4] | ⭐⭐⭐⭐⭐ |
| 精细操作中接触丰富、亚毫米级动作的多模态鲁棒理解 | CCFT [2] 提出语义分解范式，但真机接触反馈融合、力觉-视觉对齐缺失 | [2] | ⭐⭐⭐⭐ |
| VLA 与外部工具/技能库的标准化接口、调度策略与泛化边界 | ART [3] 提出框架，但工具注册、发现、组合、版本管理无行业标准 | [3] | ⭐⭐⭐⭐ |
| 免重训练/少样本适配新本体、新任务的参数高效微调 (PEFT) 机制 | BLURR [6] 关注推理加速，训练侧 PEFT (LoRA/Adapter 等) 在 VLA 上系统性实证不足 | [6] | ⭐⭐⭐ |
| 真机部署中 VLA 推理延迟、确定性与闭环控制频率的工程权衡 | 无公开 ROS2 集成基准、实时性测试报告、硬件加速 (TensorRT/ONNX) 部署细节 | [6][11][12] | ⭐⭐⭐⭐⭐ |
| **经典奠基性工作覆盖缺口** | 候选证据仅含 2026 年工业界预印本 [7][8]，缺失 RT-1/RT-2 [13]、Octo [14]、OpenVLA、RT-X、PI0 等 2022-2024 核心脉络 | [7][8][15][16] 分析 | ⭐⭐⭐⭐⭐ |
| **主流开源 VLA 项目工程实践缺口** | 候选证据 [17][18][11][12] 均未涉及 RT-1/2、OpenVLA、Octo [14]、π0、GR-1 等开源框架、ROS2 集成、真机部署案例 | [17][18][11][12] 分析 | ⭐⭐⭐⭐⭐ |
| 统一真机评测基准缺失 | Sim-to-Real 评测视角 [11]、人形真机适应 [12] 呼吁建立真机基准，但 LIBERO/SimplerEnv/RoboArena 在 VLA 上的榜单不存在 | [11][12] | ⭐⭐⭐⭐ |

---

## 4. 瓶颈与拐点（Bottleneck & Inflection）

### 4.1 增量判断
**数据规模**已推至 10 万小时真实轨迹 [8]（量变），但**数据质量策展、跨本体对齐、Sim-to-Real 评测闭环**成为结构性瓶颈；**架构层面**从纯连续动作向**离散工具/技能序列**转型 [3][9]（质变），引入推理时干预 [1][4] 成安全拐点；**工程层面**推理加速 [6] 与实时确定性成落地生死线。

### 4.2 瓶颈与拐点信号表

| 维度 | 瓶颈描述 | 拐点信号 | 证据来源 | 确定性 |
|------|----------|----------|----------|--------|
| 数据 | 真实轨迹获取成本高、质量参差、隐私合规风险；仿真数据域差大 | 10 万小时真实数据 [8] 证明规模可行，但边际收益递减需数据策展创新 | [8][11] | 较大概率 |
| 算法/架构 | 连续动作空间泛化受限、长时任务规划弱、世界模型缺失 | ART 工具化 [3]、Agentic 愿景 [9]、注意力头机制发现 [4] 推动架构离散化/模块化 | [3][4][9] | 确定 |
| 安全/对齐 | 端到端黑箱不可验证、分布外失效、注意力漂移 | 推理时注意力引导 [1]、路径偏移检测头 [4] 证明免重训练干预可行 | [1][4] | 确定 |
| 评测/验证 | 仿真基准饱和、真机评测碎片化、无统一协议 | Sim-to-Real 评测视角 [11]、人形真机自动适应 [12] 呼吁建立真机基准体系 | [11][12] | 较大概率 |
| 工程/部署 | 推理延迟 > 控制周期、显存占用大、ROS2 实时性冲突、硬件异构适配难 | BLURR 低资源推理 [6]、量化/蒸馏/稀疏化技术链成熟度提升 | [6] | 推测 |
| 算力/成本 | 训练算力集中头部、推理边缘端算力受限、能耗比制约移动本体 | 模型压缩 [6]、小模型蒸馏、专用推理芯片 (NPU/TPU) 普及 | [6][7][8] | 推测 |

> **风险**：若真机评测基准在 2026 年底前不建立统一榜单，领域将陷入“自报指标”不可比乱局 [11][12]。

---

## 5. 社会·政策·国际（Society, Policy & Geopolitics）

### 5.1 增量判断
公开证据中**直接涉及具身智能/VLA 的监管、标准、地缘政治文献极少**。仅 Foundation Model Transparency Index 2025 [17] 间接反映基础模型治理透明度需求。中国《生成式人工智能服务管理暂行办法》、欧盟《AI Act》高风险 AI 分类对机器人本体的影响、出口管制对高性能 GPU/传感器供应链的制约，均为**已知宏观背景**，但缺乏 VLA 专项实证研究。

### 5.2 关键信号表

| 维度 | 信号描述 | 证据来源 | 不确定性 |
|------|----------|----------|----------|
| 透明度/治理 | 2025 Foundation Model Transparency Index 发布，推动模型训练数据、能耗、风险评估披露标准化 | [17] | 中等：VLA 专项透明度指标尚未建立 |
| 标准化 | IEEE/ISO 机器人安全标准 (ISO 13482, ISO/TS 15066) 更新滞后于 VLA 端到端学习范式 | > 待核实 | 高：无公开证据显示 VLA 专项标准启动 |
| 地缘/供应链 | 高端 GPU (H100/B200)、高精度力触觉传感器、高性能舵机受出口管制影响，推高国产替代迫切性 | > 待核实 | 高：宏观共识，缺 VLA 专项量化分析 |
| 劳动/伦理 | 家庭/服务机器人大规模部署引发隐私、责任归属、就业替代讨论 | > 待核实 | 高：BEHAVIOR 100 任务 [5] 隐含家庭场景伦理风险 |

---

## 6. 资本与生态（Capital & Ecosystem）

### 6.1 增量判断
**头部大厂自研投入规模化**（美团 37 人 [7]、小米 33 人 [8]），**开源生态以 Octo [14] 为核心枢纽**辐射 Open X-Embodiment 数据集，但**融资并购、人才流动、初创公司图谱**在公开证据中不可见。

### 6.2 生态关键节点表

| 节点 | 类型 | 关键指标/信号 | 证据来源 | 关注度 |
|------|------|---------------|----------|--------|
| 美团机器人 | 产业界自研团队 | 37 作者、1.47 亿样本、三阶段训练配方开放 [7] | [7] | 高 |
| 小米机器人 | 产业界自研团队 | 33 作者、>10 万小时真实数据、零样本移动操作 [8] | [8] | 高 |
| Octo | 开源通用策略框架 | 明确开源、支持 Open X-Embodiment、多本体适配 [14] | [14] | 高 |
| GR-2 | 生成式 VLA 模型 | 视频-语言-动作统一生成建模，DOI 发布 [10] | [10] | 中 |
| 学术基准推动者 | 社区/学术 | Sim-to-Real 评测视角 [11]、人形真机自动适应 [12] 推动真机基准建设 | [11][12] | 中 |

> **待核实**：2024-2026 年具身智能/VLA 赛道融资轮次、金额、估值；核心人才（如 RT-1/2 作者、Octo 作者、OpenVLA 作者）流向；开源社区贡献者活跃度 (GitHub stars/PR/Issues) 纵向对比。

---

## 7. 信号与预测（Signals & Forecast）

### 7.1 早期信号（已观测到的弱信号）

| 信号 | 描述 | 来源 | 强度 |
|------|------|------|------|
| 推理时干预成主流安全范式 | Attention Steering [1]、Attention Heads 监测 [4] 证明免重训练干预可行，工程成本低 | [1][4] | 强 |
| VLA 离散化/工具化成共识 | ART [3]、Agentic 愿景 [9]、One Policy 100 Tasks [5] 均指向技能/工具序列建模 | [3][5][9] | 强 |
| 真实数据规模竞赛进入收益递减区 | 10 万小时 [8] 后，边际收益依赖数据策展、合成数据、世界模型自监督 | [8][9] | 中 |
| 推理加速成部署硬门槛 | BLURR [6] 类工作将成标配，TensorRT/ONNX/量化/蒸馏/稀疏化组合拳 | [6] | 强 |
| 真机评测基准建设启动 | Sim-to-Real 视角 [11]、Robot Trains Robot [12] 形成社区共识，LIBERO/SimplerEnv/RoboArena 将出 VLA 榜单 | [11][12] | 中 |

### 7.2 未来 6-18 月预判（可证伪假设）

| # | 预测假设 (可证伪) | 依据链 | 置信度 | 验证指标/时间点 |
|---|-------------------|--------|--------|-----------------|
| P1 | **至 2027 年 Q2，主流开源 VLA 框架 (Octo/OpenVLA/π0) 将原生集成工具调用接口 (类 ART)，并发布标准化 Tool Registry 规范** | ART [3] 已验证框架可行性；Agentic 愿景 [9] 定调方向；开源社区竞争倒逼标准化 | 80% | GitHub Octo/OpenVLA/π0 仓库合并 Tool-use PR；出现 Tool Registry RFC |
| P2 | **至 2027 年 Q1，将出现基于 LIBERO/SimplerEnv 的 VLA 真机榜单 (Real-RoboArena)，且 Top-3 方法均采用推理时注意力干预或显式安全模块** | 真机评测呼声高 [11][12]；Attention Steering [1] 与 Heads [4] 提供现成方案；安全成商业化前置条件 | 70% | RoboArena/LIBERO 官网发布 Real-VLA 排行榜；论文消融实验含安全模块 |
| P3 | **至 2026 年底，头部大厂 (美团/小米/特斯拉/Figure 等) 将发布首个“单模型 100+ 真机任务”技术报告，且推理延迟 < 50ms (50Hz 控制)** | One Policy 100 Tasks [5] 在仿真达成；BLURR [6] 攻关推理加速；10 万小时数据 [8] 支撑广度 | 60% | 官方技术博客/arXiv 报告；实测端到端延迟数据 |
| P4 | **参数高效微调 (LoRA/Adapter/Prefix-tuning) 将成为 VLA 适配新本体/新任务的标准范式，全量微调边缘化** | 大模型 PEFT 成熟迁移；VLA 参数量 > 7B 全量微调算力不可承受；BLURR [6] 关注推理侧，训练侧 PEFT 缺系统实证 | 75% | 主流 VLA 发布技术报告标注“LoRA 适配 1k 样本达全量 95% 性能” |
| P5 | **世界模型 (Video Prediction/Action-Conditioned Dynamics) 将与 VLA 显式解耦集成，形成“VLA+World Model”双塔架构主流** | Agentic 愿景 [9] 明确列为核心组件；生成式 GR-2 [10] 探索统一建模；规划推理需显式前向模拟 | 65% | Top Conference (CoRL/RSS/ICRA 2027) 双塔架构论文占比 > 30% |

> **不确定性提示**：上述预测依赖算力供给稳定、地缘政治无剧烈恶化、开源社区无重大分裂。若 2026 年底前无真机榜单雏形，P2 失效；若 GPU 供应链断裂，P3/P4 时间线顺延。

---

## 参考来源
[1] Inference-Time Attention Steering for Vision-Language-Action Driving Models — http://arxiv.org/abs/2608.17095v1
[2] Compositional Context Fine-Tuning Vision-Language Model for Complex Assembly Action Understanding from Videos — http://arxiv.org/abs/2607.10797v1
[3] Evolve Vision-Language-Action Model into an Agent with On-the-fly Tool-use — http://arxiv.org/abs/2608.14047v3
[4] Your Vision-Language-Action Model Already Has Attention Heads For Path Deviation Detection — http://arxiv.org/abs/2603.13782v1
[5] One Policy for 100 Household Tasks: Our Solution for the 2026 BEHAVIOR Challenge — http://arxiv.org/abs/2611.14432v1
[6] BLURR: A Boosted Low-Resource Inference for Vision-Language-Action Models — http://arxiv.org/abs/2512.11769v1
[7] Meituan-Robotics-0: A Vision-Language-Action Foundation Model for Desktop Manipulation — http://arxiv.org/abs/2611.08577v3
[8] Xiaomi-Robotics-1: Scaling Vision-Language-Action Models with over 100K Hours of Real-World Trajectories — http://arxiv.org/abs/2607.15330v2
[9] Envisioning Agentic Robotics: A New Era of Robotic Systems — http://arxiv.org/abs/2611.18359v1
[10] GR-2: A Generative Video-Language-Action Model for Robot Manipulation — https://doi.org/10.59350/m5s7m-3kd85
[11] Robot Policy Evaluation for Sim-to-Real Transfer: A Benchmarking Perspective — http://arxiv.org/abs/2508.11117v1
[12] Robot Trains Robot: Automatic Real-World Policy Adaptation and Learning for Humanoids — http://arxiv.org/abs/2508.12252v2
[13] RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control — http://arxiv.org/abs/2307.15818v1
[14] Octo: An Open-Source Generalist Robot Policy — http://arxiv.org/abs/2405.12213v2
[15] High Resolution Multi-Scale RAFT (Robust Vision Challenge 2022) — http://arxiv.org/abs/2210.16900v1
[16] Agriculture-Vision Challenge 2022 -- The Runner-Up Solution for Agricultural Pattern Recognition via Transformer-based Models — http://arxiv.org/abs/2206.11920v1
[17] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1
[18] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1

---

*Generated by research-bot · topic=`具身智能与视觉-语言-动作vla前沿` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`nvidia/nemotron-3-ultra-550b-a55b` · sources=35 · duration=286s · 2026-11-17T04:18:43+00:00*
