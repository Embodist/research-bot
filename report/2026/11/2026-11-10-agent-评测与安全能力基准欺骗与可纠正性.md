# Agent 评测与安全（能力基准、欺骗与可纠正性）深度调研报告

**日期**：2026-11-10（UTC）  
**领域**：Agent 评测与安全 / 能力基准 / 欺骗检测 / 可纠正性  
**检索源数量**：31 条可引用证据源  

---

## 1. 进展与热点（Progress & Hotspots）

### 1.1 最新基准与竞赛进展（2024-2026 增量）

| 名称 | 年份 | 机构/作者 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|----------|----------|--------|--------|------|------|
| MOASEI 2026 (Second Competition) | 2026 | AAMAS 2026 竞赛组委会 | 注册 8 队、仅 1 队提交最终作品 [14] | arXiv 预印本 (cs.MA)，AAMAS 2026 官方技术报告 [14] | 中：标志性多智能体开放系统基准赛事第二届，但参与度极低 | ★★★☆☆：跟踪开放多智能体评测演进必读 | [14] | 保留野火灭火、网络安全、网约车三大赛道，新增装备状态随时间变化的野火额外赛道；指标扩展为总任务完成数、平均任务完成时间、平均完成任务价值 [14] |
| ASIC-Agent Benchmark | 2025 | IEEE ICLAD 2025 | citations=8 [13] | IEEE ICLAD 2025 会议论文（同行评审）[13] | 中：EDA+LLM-Agent 交叉小众方向基准工作 | ★★★☆☆：专用 Agent 基准构建范式参考 | [13] | 面向 ASIC 设计的自主多智能体系统及配套基准评测，展示领域专用 Agent 基准构建新尝试 [13] |
| VoxENES 2026 | 2026 | arXiv (cs.SD) | 新发布基准，热度待观测 [16] | arXiv 预印本 (cs.SD) [16] | 中：语音安全/反欺骗细分社区关注 | ★★★☆☆：语音伪造检测专用基准 | [16] | 双语（英/西）语音伪造检测基准，针对 LLM 时代 TTS/VC 生成语音的泛化评测，填补传统基准与新生成模型的时域泛化鸿沟 [16] |
| UZH Shared Task 2026 | 2026 | ArgMining 2026 / UZH | 共享任务技术报告 [17] | arXiv 预印本 (cs.CL)，ArgMining 2026 共享任务 [17] | 低：NLP 论证挖掘细分任务 | ★★☆☆☆：仅作 NLP 基准参考 | [17] | 段落级论证挖掘（类型分类、141 标签预测、有向关系预测），限制 ≤8B 开放权重模型，LLM-INSTRUCT 系统获胜 [17] |
| SVC 2025 Multimodal Deception Detection Challenge | 2025 | ICCV 2025 相关挑战赛 | 首个跨域多模态欺骗检测挑战赛 [21] | arXiv 预印本 (cs.CV) [21] | 中：填补跨域欺骗检测基准空白 | ★★★★☆：直接切中欺骗检测可迁移性痛点 | [21] | 首个专门针对跨域多模态欺骗检测的挑战赛，要求模型在多个异构数据集上同时表现良好，旨在建立跨域泛化基准 [21] |

### 1.2 透明度治理与基础模型评测进展

| 名称 | 年份 | 机构/作者 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|----------|----------|--------|--------|------|------|
| Foundation Model Transparency Index (FMTI) 2025 | 2025 | Stanford CRFM 等 (Percy Liang, Rishi Bommasani 等) | 第三版年度榜单，政策与产业界高度关注 [9] | arXiv 预印本 (cs.AI)，核心作者含知名学者 [9] | 高：基础模型透明度治理权威年度量化评估 | ★★★★☆：模型安全/治理研究关键数据来源 | [9] | 评估 Alibaba、DeepSeek、xAI 等公司，平均分从 2024 年 58 下降至 40，引入数据获取、使用数据、监控新指标，揭示训练数据、算力及部署后影响的不透明趋势 [9] |

### 1.3 经典奠基性工作（基线）

| 名称 | 年份 | 机构/作者 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|----------|----------|--------|--------|------|------|
| AgentBench: Evaluating LLMs as Agents | 2023 | arXiv (cs.AI) | 被后续 Agent 评测工作广泛引用为基线 [12] | arXiv 预印本 v3 [12] | 高：Agent 评测领域里程碑，开创 LLM-as-Agent 系统评测范式 | ★★★★★：Agent 评测必读奠基之作 | [12] | 首个系统性评估 LLM 作为 Agent 能力的多维基准，包含 8 个交互式环境，覆盖推理与决策能力测试 [12] |
| AuTexTification at IberLEF 2023 | 2023 | SEPLN 2023 / IberLEF Workshop | 多语言生成文本检测早期基准 [4] | IberLEF 2023 Workshop / SEPLN 2023 会议 [4] | 中：主要影响力在西班牙语/葡萄牙语社区 | ★★★☆☆：多语言安全评测参考 | [4] | 多领域机器生成文本检测与归因共享任务，包含人工/机器文本二分类与模型归因两子任务 [4] |

> **增量判断**：2024-2026 年呈现**垂直领域基准爆发**（EDA、语音反欺骗、论证挖掘、多智能体开放系统）与**跨域泛化基准启动**（SVC 2025 欺骗检测）并行态势；但通用 Agent 能力/安全统一大规模基准仍缺失，MOASEI 2026 参与度极低（仅 1 队提交）暴露社区动员**不确定**性 [14][21]。

---

## 2. 工业界与产品（Industry & Product）

### 2.1 透明度治理驱动的产业响应

| 现象 | 时间 | 证据来源 | 说明 |
|------|------|----------|------|
| 基础模型厂商透明度评分下降（平均 58→40） | 2025 | [9] | FMTI 2025 显示 Alibaba、DeepSeek、xAI 等主要厂商透明度整体下滑，IBM 表现突出，反映行业在训练数据、算力披露上的**风险**规避倾向 [9] |
| 政策合规压力传导至模型发布流程 | 2024-2025 | [9] | FMTI 指标体系被政策端引用，倒逼厂商建立模型卡、数据表、风险评估报告等工程化合规产物 [9] |

### 2.2 专用 Agent 产品化早期信号

| 产品/项目 | 领域 | 进展阶段 | 证据来源 | 说明 |
|-----------|------|----------|----------|------|
| ASIC-Agent 系统 | EDA/芯片设计 | 会议论文+基准发布阶段 | [13] | 自主多智能体系统已具备端到端 ASIC 设计流程能力，配套基准评测为产品化提供量化依据 [13] |
| 语音伪造检测商用化 | 语音安全/反欺诈 | 基准发布阶段 | [16] | VoxENES 2026 为商用检测器提供 LLM 时代 TTS/VC 泛化评测标准，推动产品迭代 [16] |

> **待核实**：缺乏通用 Agent 平台型产品（如 AutoGPT、LangChain 生态、企业级 Agent Orchestration）在安全评测、红队测试、可纠正性机制上的工程落地公开案例。当前公开信息多集中于基准构建而非产品化部署 [12][13][16]。

---

## 3. 蓝海与缺口（Blue Ocean & Gaps）

### 3.1 核心蓝海机会

| 蓝海方向 | 缺口描述 | 支撑证据 | 潜在杠杆 |
|----------|----------|----------|----------|
| **跨域欺骗检测统一基准** | 现有研究多为单域，忽视领域偏移导致的性能大幅下降，缺乏跨异构数据集统一评测基准 | SVC 2025 首个挑战赛旨在填补此空白 [21] | 建立跨模态、跨语言、跨攻击类型的欺骗检测基准套件，推动通用检测器研发 |
| **具身智能/VLA/机器人本体 Agent 评测基准** | 现有基准多为纯文本/代码环境，缺乏面向物理交互、运动控制、多模态感知的 Agent 评测体系 | AgentBench 等经典工作仅覆盖数字环境 [12] | 引入仿真-真机统一评测管线，整合 Open X-Embodiment、LIBERO 等数据集构建具身 Agent 基准 |
| **透明度指标与下游安全风险的因果量化** | FMTI 等透明度指标与实际欺骗、可纠正性失效等安全事件的因果关联尚未充分量化 | FMTI 2025 平均分下降但缺乏风险关联分析 [9] | 建立透明度-风险因果模型，指导监管资源分配与模型发布准入 |
| **多智能体开放系统基准的社区活跃度提升** | MOASEI 2026 仅 1 队提交，基准建设与算法投入严重脱节 | MOASEI 2026 技术报告 [14] | 设计分阶段任务、提供基线代码与算力补贴、引入榜单激励机制 |

### 3.2 结构性缺口

- **基准碎片化严重**：垂直任务基准（EDA、语音、论证挖掘、多智能体路由）各自为政，缺乏跨任务、跨本体的统一评测框架 [13][14][16][17]
- **可纠正性机制评测缺位**：现有基准聚焦能力与欺骗检测，缺乏对 Agent 可关闭性、目标修正接受度、人类干预响应性的标量化评测协议 > 待核实
- **对抗鲁棒性评测标准化滞后**：BenchAudit 等工作揭示榜单排名可靠性存疑，但尚未形成社区公认的审计标准 [23]

---

## 4. 瓶颈与拐点（Bottleneck & Inflection）

### 4.1 关键瓶颈

| 瓶颈维度 | 具体表现 | 证据支撑 | 严重程度 |
|----------|----------|----------|----------|
| **基准参与度与可持续性** | MOASEI 2026 注册 8 队仅 1 队提交，基准维护成本高、算法投入低 | [14] | 高：基准无算法验证将失去演进动力 |
| **欺骗检测泛化能力** | 单域模型在跨域数据集上性能显著退化，缺乏鲁棒特征表征 | SVC 2025 挑战赛动机 [21] | 高：直接阻碍实用化部署 |
| **透明度治理与创新张力** | FMTI 平均分下降（58→40），厂商倾向于减少核心信息披露以规避竞争/监管风险 | [9] | 中：可能导致“合规造假”与真安全脱节 |
| **评测指标标准化缺失** | MOASEI 2026 新增指标（总完成数、平均时间、平均价值）未形成社区共识 | [14] | 中：跨基准结果不可比 |

### 4.2 拐点信号

| 拐点方向 | 信号描述 | 观测依据 | 判断置信度 |
|----------|----------|----------|------------|
| **跨域泛化基准从“倡议”走向“常态”** | SVC 2025 作为首个跨域多模态欺骗检测挑战赛落地 ICCV，后续或成系列化 | [21] | 较大概率 |
| **基准审计与可复现性成硬性要求** | BenchAudit 等工作推动榜单审计工具化，顶会可能强制要求评测复现包 | [23] | 推测 |
| **透明度指标纳入监管强制披露清单** | FMTI 方法论被 EU AI Act、美行政命令等政策文件引用频次上升 | [9] | 需要数据 |
| **具身 Agent 评测成新战场** | VLA 模型、人形机器人本体加速落地，急需统一评测协议 | > 待核实 | 推测 |

---

## 5. 社会·政策·国际（Society, Policy & Geopolitics）

### 5.1 监管与标准化进展

| 维度 | 进展 | 证据 | 影响 |
|------|------|------|------|
| **基础模型透明度量化治理** | FMTI 2025 为第三版年度评估，指标体系被政策端采纳为合规参考基准 | [9] | 推动全球主要厂商建立模型卡、数据表、风险报告标准化流程 |
| **多语言内容安全治理** | AuTexTification 等非英语基准推动伊比利亚语言区生成内容检测标准化 | [4] | 缓解英语中心主义导致的低资源语言安全监管盲区 |
| **语音合成滥用治理** | VoxENES 2026 针对 LLM 时代 TTS/VC 提供泛化评测，支撑深度伪造音频立法取证标准 | [16] | 为 EU AI Act 第 50 条（深度伪造标识）、中国《网络信息内容生成标识管理规定》提供技术验收依据 |

### 5.2 地缘政治与供应链影响

> **待核实**：当前公开证据未直接覆盖出口管制、算力分配、数据主权对 Agent 评测基准建设（如基准数据集托管、榜单运营、红队测试基础设施）的结构性影响。需关注 Hugging Face Hub、GitHub、arXiv 等基础设施在合规审查下的可用性变化。

---

## 6. 资本与生态（Capital & Ecosystem）

### 6.1 人才与社区流动信号

| 信号 | 观测 | 证据 | 解读 |
|------|------|------|------|
| **学术界主导基准建设** | MOASEI、SVC、VoxENES、UZH Shared Task 均由学术会议/实验室发起 | [14][21][16][17] | 基准建设仍处“公共品”阶段，商业化激励不足 |
| **开源评测框架缺乏统一入口** | AgentBench 等以论文+代码发布为主，缺乏类似 Hugging Face Evaluate 的统一生态平台 | [12] | 碎片化增加复现成本，阻碍生态网络效应 |

### 6.2 投资与并购线索

> **待核实**：缺乏 2024-2026 年专门针对 Agent 评测与安全初创公司的融资、并购公开数据。相关投资可能隐含在 LLM 基础设施、红队测试平台、合规 SaaS 等赛道中，需进一步追踪 PitchBook、Crunchbase 等数据源。

---

## 7. 信号与预测（Signals & Forecast）

### 7.1 早期信号

| 信号 | 来源 | 强度 | 说明 |
|------|------|------|------|
| 跨域欺骗检测挑战赛系列化 | SVC 2025 首届落地 ICCV [21] | 中 | 若 2026-2027 连续举办并扩展模态/语言，将成该方向事实标准 |
| 基准审计工具链开源化 | BenchAudit 提出榜单排名审计方法 [23] | 中 | 若被 NeurIPS/ICML/ICLR 采纳为投稿附件要求，将重塑评测文化 |
| 透明度指数纳入采购标准 | FMTI 2025 受政策关注度高 [9] | 中高 | 政府/企业采购清单若引入 FMTI 阈值，将倒逼厂商披露行为 |

### 7.2 未来 6-18 月预测（可证伪假设）

| 预测假设 | 依据链 | 置信度 | 证伪条件 |
|----------|--------|--------|----------|
| **P1**：至 2027 年中，将出现至少一个覆盖“文本/代码/具身/多智能体”四大本体的统一 Agent 评测套件 v1.0，并被 ≥3 家头部实验室采纳为基线 | AgentBench 奠基 [12] + 垂直基准爆发 [13][14][16] + 具身智能产业化加速 > 待核实 | 推测 | 2027-06 前无此类套件发布或采纳数 <3 |
| **P2**：跨域欺骗检测 SOTA 将从“单域微调”转向“检索增强+提示工程+轻量适配器”范式，SVC 2026/2027 冠军方案将验证此路线 | SVC 2025 定位跨域泛化 [21] + RAG/Adapter 在分布外泛化优势 > 待核实 | 推测 | SVC 后续届冠军仍为全参数微调单域模型 |
| **P3**：FMTI 平均分将在 2026 年触底回升（>45），因监管强制披露条款生效倒逼厂商补全指标 | FMTI 2025 下降趋势 [9] + EU AI Act/美行政命令落地时间表 > 待核实 | 推测 | 2026 版 FMTI 平均分继续下降或持平 |
| **P4**：MOASEI 等多智能体开放系统基准将引入“算力券+榜单奖金”双激励，参赛提交队数回升至 ≥10 | MOASEI 2026 仅 1 队提交 [14] + 社区对基准可持续性共识形成 > 待核实 | 推测 | 2027 届 MOASEI 提交队数仍 ≤3 |

### 7.3 关键不确定性

- **不确定**：通用 Agent 安全评测是否会形成类似 MLPerf 的产业联盟标准，还是继续碎片化演进？
- **不确定**：可纠正性机制（如可关闭性、目标修正）何时从理论提案进入标量化评测协议？
- **不确定**：地缘政治导致的开源基础设施分裂（如 Hugging Face 镜像、arXiv 访问）对基准数据集分发、榜单运营的冲击程度？

---

## 参考来源

[1] NTU-NPU System for Voice Privacy 2024 Challenge — http://arxiv.org/abs/2410.02371v1  
[2] OpenFact at CheckThat! 2024: Combining Multiple Attack Methods for Effective Adversarial Text Generation — http://arxiv.org/abs/2409.02649v2  
[3] This paper has been withdrawn — http://arxiv.org/abs/cond-mat/0309395v2  
[4] Overview of AuTexTification at IberLEF 2023: Detection and Attribution of Machine-Generated Text in Multiple Domains — http://arxiv.org/abs/2309.11285v1  
[5] Discovery Opportunities with Gravitational Waves -- TASI 2024 Lecture Notes — http://arxiv.org/abs/2409.08956v1  
[6] UruBots Autonomous Car Team Two: Team Description Paper for FIRA 2024 — http://arxiv.org/abs/2406.08741v1  
[7] UruBots Autonomous Cars Team One Description Paper for FIRA 2024 — http://arxiv.org/abs/2406.08745v1  
[8] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1  
[9] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1  
[10] Neovationism Foundational Paper — https://doi.org/10.2139/ssrn.5671390  
[11] Trajectory Engineering: A Foundational Paper — https://doi.org/10.2139/ssrn.6589519  
[12] AgentBench: Evaluating LLMs as Agents — http://arxiv.org/abs/2308.03688v3  
[13] ASIC-Agent: An Autonomous Multi-Agent System for ASIC Design with Benchmark Evaluation — https://doi.org/10.1109/iclad65226.2025.00033  
[14] Second MOASEI Competition at AAMAS'2026: A Technical Report — http://arxiv.org/abs/2607.03399v1  
[15] Refined CMA-ES for CEC 2026 Bound-Constrained Single-Objective Optimization — http://arxiv.org/abs/2611.04620v1  
[16] VoxENES 2026: Benchmarking Generalization of Speech Spoofing Detectors Against LLM-Era TTS and Voice Conversion — http://arxiv.org/abs/2607.11706v1  
[17] LLM-INSTRUCT at UZH Shared Task 2026: Constraint-Aware Retrieval and Selective Debate for Paragraph-Level Argument Mining — http://arxiv.org/abs/2607.20430v1  
[18] Task-Specific Multimodal Question Answering Agents via Confidence Calibration and Incremental Reasoning for QANTA 2026 — http://arxiv.org/abs/2607.09623v1  
[19] VISA: A Visual Information Strengthened Audio-Reasoning System for the Interspeech 2026 ARC Agent Track — http://arxiv.org/abs/2606.07264v2  
[20] ICASSP 2026 Radar Acoustic Speech Enhancement (RASE) Challenge — http://arxiv.org/abs/2610.32202v1  
[21] SVC 2025: the First Multimodal Deception Detection Challenge — http://arxiv.org/abs/2508.04129v1  
[22] Detecting Strategic Deception Using Linear Probes — http://arxiv.org/abs/2502.03407v1  
[23] BenchAudit: checking whether benchmark leaderboard rankings actually hold up — https://doi.org/10.2139/ssrn.6905759  
[24] Atmospheric entry and fragmentation of small asteroid 2024 BX1: Bolide trajectory, orbit, dynamics, light curve, and spectrum — http://arxiv.org/abs/2403.00634v2  
[25] Roman Galactic Plane Survey Definition Committee Report — http://arxiv.org/abs/2511.07494v1  
[26] Knowledge-Verified Emergent Deception in LLM Agents Under Conflicting Incentives — http://arxiv.org/abs/2608.26372v1  
[27] Point Transformer V3 Extreme: 1st Place Solution for 2024 Waymo Open Dataset Challenge in Semantic Segmentation — http://arxiv.org/abs/2407.15282v1  
[28] A Survey of Multi-Agent Deep Reinforcement Learning with Communication — http://arxiv.org/abs/2203.08975v2  
[29] A Methodology to Engineer and Validate Dynamic Multi-level Multi-agent Based Simulations — http://arxiv.org/abs/1311.5108v1  
[30] AOAD-MAT: Transformer-based multi-agent deep reinforcement learning model considering agents' order of action decisions — http://arxiv.org/abs/2510.13343v1  
[31] Augmenting the action space with conventions to improve multi-agent cooperation in Hanabi — http://arxiv.org/abs/2412.06333v3

---

*Generated by research-bot · topic=`agent-评测与安全能力基准欺骗与可纠正性` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`nvidia/nemotron-3-ultra-550b-a55b` · sources=31 · duration=342s · 2026-11-10T04:36:57+00:00*
