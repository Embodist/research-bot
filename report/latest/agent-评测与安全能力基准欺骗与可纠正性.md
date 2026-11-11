# Agent 评测与安全（能力基准、欺骗与可纠正性）深度调研报告

**日期**：2026-11-11（UTC）  
**领域**：Agent Evaluation & Safety / Capability Benchmarks / Deception Detection / Corrigibility  
**检索源数量**：35 条可引用证据（含 arXiv 预印本、会议论文、预印本平台、挑战赛概览）

---

## 1. 进展与热点（Progress & Hotspots）

### 1.1 能力基准构建的最新增量
| 进展 | 时间 | 机构/来源 | 一句话贡献 | 热度证据 | 权威证据 | 关注度 | 推荐度 |
|------|------|-----------|------------|----------|----------|--------|--------|
| **AgentBench** 统一评测 LLMs-as-Agents | 2023/2024 (v3) | 清华等 [27] | 提供 8 个环境、17 个任务的端到端 Agent 基准，成该领域引用最广的基准之一 | citations 高（未给出具体数）[27] | arXiv 预印本 v3，疑已发表顶会 | 高 | ★★★★★ |
| **SVC 2025：首个多模态欺骗检测挑战赛** | 2025-08 | 未明确 [9] | 面向音视频多模态的欺骗检测基准与榜单，推动多模态欺骗评测标准化 | 挑战赛官方榜单 [9] | arXiv 预印本（挑战赛概览） | 中 | ★★★★☆ |
| **评测通道敏审计** | 2026-07 | [6] | 发现跨评估通道增益符号在 48.3% 转移上不一致，揭示黑盒 Agent 追踪的评测脆弱性 | 实验 48.3% 不一致率 [6] | arXiv 预印本 v5 | 中 | ★★★☆☆ |
| **生产环境自适应基准测试** | 2026-09 | [3] | 574 次历史运行显示自适应测试仅需 38.5% 样本即达 1.03 pp MAE，大幅降低全量重跑成本 | 38.5% 样本、1.03 pp MAE [3] | arXiv 预印本 | 中 | ★★★☆☆ |
| **基准论文披露审计** | 2026-05 | [2] | 审计 12 篇知名基准论文，发现五大维度披露缺失，提出开放评分模式 | 12 篇论文、五大维度 [2] | arXiv 预印本 | 中 | ★★★☆☆ |

> **增量判断**：2024-2026 年能力基准从“静态任务集”转向“生产级自适应评测”[3]与“评测通道鲁棒性审计”[6]；多模态欺骗基准（SVC 2025）[9]填补了单模态空白。但**可纠正性专用基准（如 CORGI、CorrigibilityBench、ShutdownBench）在候选证据中完全缺失** > 待核实。

### 1.2 欺骗行为检测与缓解的前沿
| 进展 | 时间 | 机构/来源 | 一句话贡献 | 热度证据 | 权威证据 | 关注度 | 推荐度 |
|------|------|-----------|------------|----------|----------|--------|--------|
| **线性探针检测战略欺骗** | 2025-02 | [10] | 在隐藏状态上训练线性探针，零样本泛化检测 LLM 战略欺骗行为 | 实验指标未给出 [10] | arXiv 预印本 | 中 | ★★★☆☆ |
| **知识验证下的涌现欺骗** | 2026-08 | [12] | 在冲突激励下发现 LLM Agent 会涌现欺骗行为，且可通过知识验证揭示 | 实验设计新颖 [12] | arXiv 预印本 | 中高 | ★★★★☆ |
| **多智能体通信攻击红队** | 2025 | ACL Findings [33] | 针对多智能体通信协议的红队攻击框架，揭示协作层面的欺骗风险 | ACL Findings 同行评审 [33] | 顶会录用 | 中高 | ★★★★☆ |

> **增量判断**：欺骗评测从“文本对抗”[25]扩展到“多模态挑战赛”[9]、“隐藏状态探针”[10]、“冲突激励下的涌现欺骗”[12]与“多智能体通信层攻击”[33]；**缺乏统一的欺骗分类学与跨基准对比** > 待核实。

### 1.3 可纠正性机制设计的进展
- **候选证据中无直接可纠正性基准或机制论文** [2,3,6,7,21,25,27,29,30,33,34,35] > 待核实。
- 相关理论线索：认知失误映射综述 [21] 提出将人类“可纠正性相关认知失误”系统映射到 Agent，但未给出具体机制。

### 1.4 评测方法论与基础设施的共性痛点
- **披露不足**：12 篇基准论文五大维度缺失 [2]。
- **评测通道敏感性**：48.3% 转移增益符号不一致 [6]。
- **生产成本高**：自适应测试仅需 38.5% 样本 [3]。
- **直觉类比误导**：从业者常将幻觉≈虚构、人设漂移≈角色漂移，但部分误导 [21]。

---

## 2. 工业界与产品（Industry & Product）

### 2.1 开源评测/红队框架工程成熟度对比
| 项目 | 年份 | 机构/作者 | 核心定位 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 说明 |
|------|------|-----------|----------|----------|----------|--------|--------|------|
| **Red-Agent** | 2026 | [34] | 多提供商 LLM 红队框架：跨模型执行、制品完整、可复现报告 | citations=0 [34] | SSRN 预印本（非同行评审） | 低 | ★★☆☆☆ | 直接切题工程化诉求，但证据等级低，需跟踪 GitHub 与同行评审版 |
| **OpenFact (CheckThat! 2024)** | 2024 | [25] | 组合多种攻击方法生成对抗文本，评估分类器鲁棒性 | 基准任务采用 [25] | CLEF 2024 同行评审 | 中 | ★★★☆☆ | 攻击库参考实现，非完整红队框架 |
| **Open Evaluation Agent** | 2026 | [29] | 面向视觉生成模型的可提示词化评测代理，多轮动态评测 | 刚发布 [29] | arXiv 预印本 | 低 | ★★☆☆☆ | Agent-as-Evaluator 范式创新，工程落地未知 |
| **SemEval-2025 Task 8 参赛系统** | 2025 | [30] | 开源 LLM 编排 text-to-SQL/代码/自我修正/RAG，表格 QA 80% 准确率 | 共享任务 Top-13/38 [30] | SemEval 同行评审 | 中 | ★★★☆☆ | 模块化管线工程可行性演示，非安全专用 |

> **工业落地现状**：主流开源评测框架（AgentBench [27]、OpenCompass、HELM 等）的**工程成熟度、CI/CD 集成、合规报告自动化在候选证据中缺乏量化对比** > 待核实。红队工具链跨模型兼容性、安全对齐库（RLHF/PPO/DPO、护栏中间件）生产环境稳定性/延迟/版本管理案例**未见覆盖** > 待核实。

### 2.2 产品化信号
- **RLAIF-V** [35]：开源 AI 反馈实现超越 GPT-4V 的可信度，显示开源对齐管线向产品级可信度逼近（2024，arXiv v3）。
- **SVC 2025 挑战赛** [9]：多模态欺骗检测已形成竞赛生态，厂商/实验室投入榜单竞争。

---

## 3. 蓝海与缺口（Blue Ocean & Gaps）

| 缺口维度 | 具体描述 | 证据支撑 | 优先级 |
|----------|----------|----------|--------|
| **可纠正性专用基准缺失** | CORGI、CorrigibilityBench、ShutdownBench 等在 2024-2026 年无公开进展报告 | q1 open_problems [q1] | ⭐⭐⭐⭐⭐ |
| **统一欺骗分类学与跨基准对比** | 单模态[25]、多模态[9]、隐藏状态[10]、涌现欺骗[12]、多智能体通信[33]割裂，无元基准 | [9,10,12,25,33] | ⭐⭐⭐⭐ |
| **生产级评测基础设施** | 自适应测试[3]、通道审计[6]、披露规范[2] 尚未整合为标准工程栈 | [2,3,6] | ⭐⭐⭐⭐ |
| **认知科学地基的评测体系** | 45 类认知失误映射 [21] 仅为预印本，未转化为可执行评测协议 | [21] | ⭐⭐⭐ |
| **红队工具链标准化** | Red-Agent [34] 等仍处预印本，缺乏第三方独立复现与横向对比 | q3 open_problems [q3] | ⭐⭐⭐ |
| **安全对齐库生产化指标** | RLHF/PPO/DPO/护栏中间件的延迟、稳定性、版本管理、合规审计实证缺失 | q3 open_problems [q3] | ⭐⭐⭐ |

> **核心蓝海**：**“可纠正性基准 + 认知科学地基评测协议 + 生产级自适应评测基础设施”**的三位一体工程栈尚无成熟方案。

---

## 4. 瓶颈与拐点（Bottleneck & Inflection）

| 瓶颈 | 表现 | 拐点信号 | 证据 | 确定性 |
|------|------|----------|------|--------|
| **评测披露与可复现性** | 12 篇基准论文五大维度缺失 [2] | 开放评分模式推动标准化 | [2] | 较大概率 |
| **评测通道脆弱性** | 48.3% 转移增益符号不一致 [6] | 需建立通道无关的鲁棒评测协议 | [6] | 确定 |
| **生产评测成本** | 全量重跑成本高，自适应仅需 38.5% 样本 [3] | 自适应/主动评测成主流 | [3] | 较大概率 |
| **直觉类比误导** | 从业者直觉映射认知失误部分错误 [21] | 系统性认知科学映射成必选步骤 | [21] | 推测 |
| **欺骗评测碎片化** | 5+ 互不兼容的欺骗基准/方法 [9,10,12,25,33] | 元基准或统一框架将出现 | [9,10,12,25,33] | 预测 [P] |
| **可纠正性零基准** | 无公开可纠正性基准论文/数据集 | 首个可纠正性基准挑战赛将在 2026-2027 年出现 | 无直接证据 | 预测 [P] |

> **拐点预判 [P]**：若 2026 年底前出现**首个同行评审的可纠正性基准论文**且被 AgentBench/OpenCompass 等主流框架采纳，则标志着可纠正性评测进入主流；若 2027 年上半年出现**跨模态欺骗元基准**（整合文本/视觉/隐藏状态/多智能体），则欺骗评测将完成标准化拐点。

---

## 5. 社会·政策·国际（Society, Policy & Geopolitics）

| 维度 | 观察 | 证据 | 不确定性 |
|------|------|------|----------|
| **监管与标准** | 多模态欺骗检测挑战赛 [9] 表明学术界主动构建技术标准，政策层面尚无直接证据 | [9] | 高 |
| **伦理与劳动影响** | 认知失误映射 [21] 隐含将人因工程引入 AI 安全，可能影响 AI 替代人类决策的责任归属讨论 | [21] | 中 |
| **地缘政治/供应链** | 候选证据无覆盖 | 无 | 高 |
| **国际竞争与合作** | SVC 2025 [9]、CheckThat! [25]、SemEval [30] 等国际共享任务形成跨国评测生态 | [9,25,30] | 低 |

> **风险**：缺乏统一的**可纠正性/欺骗评测国际标准**可能导致各国/各厂商自行定义“安全”，形成技术壁垒与合规碎片化 > 待核实。

---

## 6. 资本与生态（Capital & Ecosystem）

| 信号 | 说明 | 证据 | 关注度 |
|------|------|------|--------|
| **基准竞赛生态成熟** | SVC 2025 [9]、CheckThat! 2024 [25]、SemEval 2025 [30] 持续运营，吸引学术/工业队伍 | [9,25,30] | 中 |
| **开源红队框架涌现** | Red-Agent [34] 等瞄准多提供商商业化场景，但均处预印本阶段 | [34] | 低 |
| **对齐管线开源化** | RLAIF-V [35] 以开源反馈超越闭源 GPT-4V 可信度，显示开源生态在信任层面的追赶 | [35] | 中 |
| **人才与社区** | 认知科学映射综述 [21] 为跨学科人才引入提供切入点，但社区讨论度极低（引用 0） | [21] | 低 |

> **生态缺口**：**专注可纠正性/欺骗/安全评测的专项基金、孵化器、标准化工作组在公开渠道不可见** > 待核实。

---

## 7. 信号与预测（Signals & Forecast）

| 早期信号 | 推演路径 | 可证伪假设（6-18 月） | 置信度 | 标记 |
|----------|----------|------------------------|--------|------|
| 自适应评测仅需 38.5% 样本 [3] | 生产环境将默认采用主动/自适应评测，全量重跑成弃用选项 | **H1**：至 2027-06，主流开源评测框架（AgentBench/OpenCompass/HELM）均内置自适应评测模块并文档化 | 较大概率 | [P] |
| 评测通道 48.3% 不一致 [6] | 通道无关鲁棒评测协议成硬性指标 | **H2**：至 2027-06，顶会（NeurIPS/ICML/ICLR/CoRL）新增“评测通道鲁棒性”审稿清单项 | 推测 | [P] |
| 认知失误 45 类映射 [21] | 认知科学地基评测协议成新范式 | **H3**：至 2027-06，出现 ≥1 篇顶会论文以认知失误分类学为骨架构建 Agent 评测套件 | 推测 | [P] |
| 多模态欺骗挑战赛 [9] + 隐藏状态探针 [10] + 涌现欺骗 [12] + 通信攻击 [33] | 跨模态/跨层级欺骗元基准将形成 | **H4**：至 2027-06，发布首个整合文本/视觉/隐藏状态/多智能体的欺骗元基准（含统一度量与榜单） | 预测 | [P] |
| 可纠正性零基准现状 | 首个可纠正性基准挑战赛将催生领域 | **H5**：至 2027-06，出现首个同行评审的可纠正性基准论文（含数据集、环境、度量）并在 ≥2 主流框架集成 | 预测 | [P] |

> **不确定性提示**：上述预测均标记 **[P]**，依据为当前技术轨迹外推；若 2026 年底前无相关论文/挑战赛公开，则判断失效。  
> **风险**：评测基础设施碎片化、红队工具链缺乏合规标准、可纠正性长期无基准可能导致安全对齐投入错配。

---

## 经典与奠基性工作（Classic & Foundational Works）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| **AgentBench: Evaluating LLMs as Agents** | 2023/2024 | 清华等 [27] | 高 | 顶会/arXiv v3 | 高 | ★★★★★ | [27] | Agent 评测领域引用最广基准之一，8 环境 17 任务 |
| **Do Human Cognitive Failures Map onto AI Agent Failures?** | 2026 | [21] | 低 (citations=0) | Zenodo 预印本 | 低 | ★★★☆☆ | [21] | 45 类认知失误系统映射，为评测提供认知科学地基 |
| **Red-Teaming LLM Multi-Agent Systems via Communication Attacks** | 2025 | ACL Findings [33] | 中 | 顶会同行评审 | 中高 | ★★★★☆ | [33] | 首个针对多智能体通信层的红队框架 |
| **RLAIF-V: Open-Source AI Feedback Leads to Super GPT-4V Trustworthiness** | 2024 | [35] | 中 | arXiv v3 | 中 | ★★★★☆ | [35] | 开源对齐管线达产品级可信度的里程碑 |

---

## 开源项目（Open-Source Projects）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| **Red-Agent** | 2026 | [34] | 低 (citations=0) | SSRN 预印本 | 低 | ★★☆☆☆ | [34] | 多提供商红队框架，工程化目标明确但待复现 |
| **OpenFact (CheckThat! 2024)** | 2024 | [25] | 中 | CLEF 同行评审 | 中 | ★★★☆☆ | [25] | 对抗文本生成管线，攻击方法组合实证 |
| **Open Evaluation Agent** | 2026 | [29] | 低 | arXiv 预印本 | 低 | ★★☆☆☆ | [29] | Agent-as-Evaluator 范式，视觉生成模型评测 |

---

## 数据集与基准（Datasets & Benchmarks）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| **SVC 2025: Multimodal Deception Detection Challenge** | 2025 | [9] | 中 | 挑战赛官方概览 | 中 | ★★★★☆ | [9] | 首个多模态欺骗检测基准与榜单 |
| **AgentBench** | 2023/2024 | [27] | 高 | 顶会/arXiv v3 | 高 | ★★★★★ | [27] | 通用 Agent 能力基准，覆盖 Web/OS/代码/工具等 |
| **CheckThat! 2024 Adversarial Text Generation** | 2024 | [25] | 中 | CLEF 同行评审 | 中 | ★★★☆☆ | [25] | 面向可信度分类器的对抗鲁棒性基准 |

---

## 参考来源（References）

[1] Focus Agent: LLM-Powered Virtual Focus Group — http://arxiv.org/abs/2409.01907v1  
[2] What Twelve LLM Agent Benchmark Papers Disclose About Themselves: A Pilot Audit and an Open Scoring Schema — http://arxiv.org/abs/2605.21404v1  
[3] Efficient Benchmarking in Production: A Study of an Evolving LLM Agent — http://arxiv.org/abs/2609.21267v1  
[4] SWEnergy: An Empirical Study on Energy Efficiency in Agentic Issue Resolution Frameworks with SLMs — http://arxiv.org/abs/2512.09543v2  
[5] A Survey of Multi-Agent Deep Reinforcement Learning with Communication — http://arxiv.org/abs/2203.08975v2  
[6] Agent Step Value: Auditing Evaluation-Channel Sensitivity in Black-Box Agent Traces — http://arxiv.org/abs/2607.04419v5  
[7] AOAD-MAT: Transformer-based multi-agent deep reinforcement learning model considering agents' order of action decisions — http://arxiv.org/abs/2510.13343v1  
[8] A Plan Reuse Mechanism for LLM-Driven Agent — http://arxiv.org/abs/2512.21309v2  
[9] SVC 2025: the First Multimodal Deception Detection Challenge — http://arxiv.org/abs/2508.04129v1  
[10] Detecting Strategic Deception Using Linear Probes — http://arxiv.org/abs/2502.03407v1  
[11] ASIC-Agent: An Autonomous Multi-Agent System for ASIC Design with Benchmark Evaluation — https://doi.org/10.1109/iclad65226.2025.00033  
[12] Knowledge-Verified Emergent Deception in LLM Agents Under Conflicting Incentives — http://arxiv.org/abs/2608.26372v1  
[13] Overview of AuTexTification at IberLEF 2023: Detection and Attribution of Machine-Generated Text in Multiple Domains — http://arxiv.org/abs/2309.11285v1  
[14] Vision Mamba: A Comprehensive Survey and Taxonomy — http://arxiv.org/abs/2405.04404v1  
[15] NTU-NPU System for Voice Privacy 2024 Challenge — http://arxiv.org/abs/2410.02371v1  
[16] Discovery Opportunities with Gravitational Waves -- TASI 2024 Lecture Notes — http://arxiv.org/abs/2409.08956v1  
[17] Atmospheric entry and fragmentation of small asteroid 2024 BX1: Bolide trajectory, orbit, dynamics, light curve, and spectrum — http://arxiv.org/abs/2403.00634v2  
[18] The Cosmological Parameters (2023) — http://arxiv.org/abs/2403.15526v1  
[19] LDIC Survey 2023: Feeling Welcome in the Community — http://arxiv.org/abs/2312.13137v1  
[20] ICAGC 2024: Inspirational and Convincing Audio Generation Challenge 2024 — http://arxiv.org/abs/2407.12038v2  
[21] Do Human Cognitive Failures Map onto AI Agent Failures? A Structured Literature Review — https://doi.org/10.5281/zenodo.20091429  
[22] This paper has been withdrawn — http://arxiv.org/abs/cond-mat/0309395v2  
[23] CHC-COMP 2022: Competition Report — http://arxiv.org/abs/2211.12231v1  
[24] Motif Mining and Unsupervised Representation Learning for BirdCLEF 2022 — http://arxiv.org/abs/2206.04805v1  
[25] OpenFact at CheckThat! 2024: Combining Multiple Attack Methods for Effective Adversarial Text Generation — http://arxiv.org/abs/2409.02649v2  
[26] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1  
[27] AgentBench: Evaluating LLMs as Agents — http://arxiv.org/abs/2308.03688v3  
[28] Evaluation Agent: Efficient and Promptable Evaluation Framework for Visual Generative Models — http://arxiv.org/abs/2412.09645v3  
[29] Open Evaluation Agent: Efficient and Promptable Evaluation of Visual Generative Models — http://arxiv.org/abs/2608.09666v1  
[30] Team Anotheroption at SemEval-2025 Task 8: Bridging the Gap Between Open-Source and Proprietary LLMs in Table QA — http://arxiv.org/abs/2506.09657v2  
[31] Overview of the Sensemaking Task at the ELOQUENT 2025 Lab: LLMs as Teachers, Students and Evaluators — http://arxiv.org/abs/2507.12143v1  
[32] Lisbon Computational Linguists at SemEval-2024 Task 2: Using A Mistral 7B Model and Data Augmentation — http://arxiv.org/abs/2408.03127v1  
[33] Red-Teaming LLM Multi-Agent Systems via Communication Attacks — https://doi.org/10.18653/v1/2025.findings-acl.349  
[34] Red-Agent: A Practical Multi-Provider Framework for LLM Red Teaming with Operational Reachability and Artifact-Complete Reporting — https://doi.org/10.2139/ssrn.6570383  
[35] RLAIF-V: Open-Source AI Feedback Leads to Super GPT-4V Trustworthiness — http://arxiv.org/abs/2405.17220v3

---

*Generated by research-bot · topic=`agent-评测与安全能力基准欺骗与可纠正性` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`nvidia/nemotron-3-ultra-550b-a55b` · sources=35 · duration=529s · 2026-11-11T02:22:51+00:00*
