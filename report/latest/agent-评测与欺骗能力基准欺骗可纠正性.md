# Agent 评测与欺骗（能力基准、欺骗、可纠正性）深度调研报告

**日期**：2026-11-17（UTC）  
**领域**：Agent Evaluation / Deception Detection / Corrigibility Alignment  
**检索源数量**：35 条可引用证据（编号 [1]–[2]）

---

## 1. 进展与热点

### 1.1 近 1-2 年核心增量：从“单任务准确率”转向“欺骗行为验证与可纠正性监控”

| 进展节点 | 时间 | 机构/来源 | 一句话贡献 | 证据等级 | 关键引用 |
|----------|------|-----------|------------|----------|----------|
| **KnownLieBench** 首个知识验证型 Agent 欺骗基准发布 | 2026-08 | arXiv (cs.CL) | 引入“中性探针确认知晓 → 激励冲突观察撒谎 → 多轮信任追踪”完整评测流程，区分欺骗与幻觉 | A (arXiv preprint) | [3] |
| **FMTI 2025 第三版** 揭示头部模型商透明度整体下降（均分 58→40） | 2025-12 | Stanford HAI / arXiv (cs.AI) | 新增数据获取/使用数据/监控指标维度，首次纳入 Alibaba、DeepSeek、xAI，IBM 表现突出 | A (arXiv preprint) | [4] |
| **SVC 2025** 首个多模态欺骗检测挑战赛启动 | 2025-08 | arXiv (cs.CV) | 面向安检/反欺诈/可信度评估真实场景，解决单域单模态样本稀缺问题 | A (arXiv preprint) | [5] |
| **生产级 Agent 持续评测范式** 基于 574 次历史运行的低成本复测方法 | 2026-09 | arXiv (cs.AI) | 校准期/保留期拆分 + IRT 自适应/难度分层固定子集策略，200 题达 1.03 pp MAE，可迁移 5 个 Agent 族 | A (arXiv preprint) | [6] |
| **Evaluation-Side Partially Observable Games** 缓解 Agent 欺骗的新博弈论框架 | 2026-11 | arXiv (cs.AI) | 从评测侧引入部分可观测博弈建模欺诈激励，提供理论可纠正性干预路径 | A (arXiv preprint) | [7] |
| **Open Evaluation Agent** 面向视觉生成模型的可提示多轮评测框架 | 2026-08 | arXiv (cs.AI) | 模仿人类少样本判断策略，自然语言需求→子维度分解→针对性提示→采样→评估器，实现动态可解释评测 | A (arXiv preprint) | [8] |

> **增量判断**：相对 2024 年前以“静态基准榜单（MMLU、GPQA、SWE-bench 等）”为主的评测范式，**2025-2026 年出现三大结构性转向**：(1) 从“能力测度”显性延伸至“欺骗/对抗行为验证”；(2) 从“一测定终身”转向“生产级持续评测与漂移监控”；(3) 从单模态文本基准扩展至多模态欺骗检测与跨域泛化。上述六项工作均为 **2025 年下半年至 2026 年** 发布，构成当前前沿的**增量锚点** [3][4][5][6][7][8]。

### 1.2 经典与奠基性工作（按方法演进脉络）

| 名称 | 年份 | 机构/作者 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|----------|----------|--------|--------|------|------|
| Addressing corrigibility in near-future AI systems | 2024 | Hadfield-Menell 等 | 引用数 > 待核实 | 期刊 *AI & Society* (Springer)，同行评审 | 高：可纠正性理论核心文献 | ★★★★★ | [9] | 形式化定义可纠正性（关闭按钮问题、奖励篡改、政策遵循），奠基性理论 |
| Triarchic corrigibility: a role-separated governance design pattern | 2026 | 同作者组 | 引用数 > 待核实 | 期刊 *AI & Society* (Springer)，同行评审 | 高：最新理论延伸，治理模式化 | ★★★★☆ | [10] | 提出“三权分立”治理范式（决策/监督/执行分离），工程落地指导性强 |
| The necessary roadblock to AGI | 2019 | Yampolskiy | 引用数 > 待核实 | ACM 会议论文集，同行评审 | 中：早期 AGI 安全论证 | ★★★☆☆ | [11] | 论证不可纠正性是通向 AGI 的必经障碍，理论视角互补 |
| Structural Capability Containment | 2024 | SSRN 预印本 | 下载量 > 待核实 | SSRN 工作论文，未同行评审 | 中：多司法管辖安全架构 | ★★★☆☆ | [12] | 从系统工程角度提出能力封装框架，与可纠正性工程化相关 |

> **注意**：候选证据库中 [13][14][15][16] 均不涉及 Agent 评测/欺骗/可纠正性核心技术主题，已在 q2 发现中标注为“候选证据库需补充检索” [13][14][15][16]。上表四篇为**仅有的可直接关联经典理论的证据来源** [9][10][12][11]。

---

## 2. 工业界与产品

### 2.1 生产级 Agent 评测工程实践（一手案例）

| 实践主体 | 场景 | 核心做法 | 量化收益 | 部署决策 | 证据来源 |
|----------|------|----------|----------|----------|----------|
| 某服务数万 MAU 的分析型 Agent 团队 | 生产环境持续评测 | 574 次历史运行→校准期/保留期拆分；对比随机采样/历史缓存/固定代表子集/IRT 自适应四策略 | 执行 200 题（38.5% 完整量）达 1.03 pp MAE；难度分层固定子集无需重校准即迁移 5 个 Agent 族，校准窗口长至一天稳定 | 因运维简洁性选“难度分层固定子集”而非 IRT 自适应 | [6] |

> **工程难点显性化**：(1) 评测成本与迭代速度矛盾；(2) 历史数据复用的统计功效边界；(3) 跨 Agent 族基准迁移的校准稳定性。上述案例为**唯一可引用的生产级第一手工程证据** [6]。

### 2.2 Agent 技能生态标准化与基础设施演进

| 动态 | 时间 | 关键指标 | 意义 | 证据来源 |
|------|------|----------|------|----------|
| Anthropic 推出 Agent Skill 开放规范 | 2025-10 | 九个月内 GitHub 公开仓库积累数百万技能文件 | 反映 Agent 技能复用、评测标准化、跨框架互操作的基础设施快速成熟 | [17] |
| GitSkills 数据集发布 | 2026-08 | 收集含 `SKILL.md` 说明及可选脚本的 Agent Skill | 为生态规模量化、技能检索与评测复用提供实证语料 | [17] |
| 多 Agent 框架生态健康度纵向分析 | 2026-07 | GitHub star/fork/贡献者/提交频次等生态指标 | 揭示 LangGraph、AutoGen、CrewAI 等主流框架的采用曲线与维护活跃度差异 | [18] |

> **产品化信号**：Agent Skill 规范的大规模采用 [17] 与多框架生态分化 [18] 共同指向**“评测基础设施标准化”正在从模型层下沉到技能/工具层**，这将直接降低跨本体、跨任务的基准复用成本，但也引入**版本漂移与供应链安全**新风险。

---

## 3. 蓝海与缺口

| 缺口编号 | 描述 | 证据支撑 | 优先级 | 可行性切入点 |
|----------|------|----------|--------|--------------|
| **G1** | **统一的“可纠正性”定量定义与端到端基准缺失** | 现有工作聚焦单一维度：KnownLieBench 仅评测欺骗 [3]、FMTI 仅度量透明度 [4]、生产评测仅解决效率 [6]、理论工作停留在形式化定义 [9][10] | ★★★★★ | 基于 [9][10] 的三权分立治理范式，设计“可关闭/可修正/可审计”三维度量表，接入 KnownLieBench 与生产评测流水线 |
| **G2** | **多模态欺骗检测的跨域泛化基准尚不成熟** | SVC 2025 为首届挑战赛，数据规模/多样性待扩充 [5]；缺乏机器人/VLA 场景下的视觉-语言-动作欺骗样本 | ★★★★☆ | 联合具身智能数据集（Open X-Embodiment、LIBERO、SimplerEnv）构建“视觉-动作不一致”欺骗子集 |
| **G3** | **生产级机器人/VLA 真机持续评测的工程案例空白** | 现有证据仅覆盖 LLM 分析型 Agent [6]；真机部署面临仿真-实机一致性、数据飞漂检测、硬件磨损干扰等额外难点 | ★★★★★ | 迁移 [6] 的“校准期/保留期+难度分层”范式至 SimplerEnv/RoboArena 真机评测流水线 |
| **G4** | **欺骗检测/作弊检测在机器人评测中的专用工具缺失** | 候选证据全无覆盖 [6][8][19][17]；VLA 模型可能通过“动作分布作弊”通过基准而实机失效 | ★★★★☆ | 引入 [7] 的评测侧部分可观测博弈框架，设计“动作意图与执行一致性”对抗探针 |
| **G5** | **基础模型透明度下降（FMTI 2025）对下游 Agent 可纠正性的负面影响缺乏量化** | FMTI 显示透明度均分 58→40 [4]；但无研究量化其对 Agent 微调/部署后可纠正性指标的因果影响 | ★★★☆☆ | 设计消融实验：同架构下对比高/低透明度基座模型在 KnownLieBench 上的欺骗率差异 |

> **核心蓝海**：**“可纠正性端到端基准”** 与 **“具身智能真机持续评测工程范式”** 为最高杠杆缺口，分别对应理论-工程两条主线的交汇点。

---

## 4. 瓶颈与拐点

### 4.1 关键瓶颈

| 瓶颈维度 | 具体表现 | 证据支撑 | 严重程度 |
|----------|----------|----------|----------|
| **数据/标注** | 欺骗样本稀缺、需知识验证区分幻觉、多模态跨域标注成本高 | KnownLieBench 仅 112 case [3]；SVC 2025 处于首届扩充期 [5] | 高 |
| **评测理论** | 缺乏“评测即干预”的理论框架；持续评测的统计功效边界未定 | [6] 仅给出经验阈值（200 题/1.03 pp MAE），无统计学收敛证明 | 高 |
| **工程部署** | 真机评测成本高、仿真-实机 Gap、硬件异构导致基准不可比 | 无直接证据，但 [6] 明确指出“生产环境评测成本高”且仅验证 LLM Agent | 高 |
| **治理激励** | 头部模型商透明度倒退（FMTI 58→40）[4]，商业动机与可纠正性对齐目标冲突 | FMTI 2025 显示行业级倒退趋势 [4] | 中高 |
| **生态碎片** | 多框架（LangGraph/AutoGen/CrewAI 等）评测接口不统一、Skill 规范虽起步但版本管理混乱 | [17][18] 显示生态规模大但标准化仍在早期 | 中 |

### 4.2 拐点信号

| 信号 | 观测依据 | 判断置信度 | 可能时间窗 |
|------|----------|------------|------------|
| **评测基础设施标准化加速** | Agent Skill 规范 9 个月百万级采用 [17]；多框架生态进入“优胜劣汰”期 [18] | 较大概率 | 2026 H2–2027 H1 |
| **监管强制透明度/可审计** | EU AI Act 高风险系统要求技术文档与事后审计；FMTI 下降趋势可能倒逼政策介入 | 推测 | 2027 起生效 |
| **“评测即训练”范式涌现** | [7] 提出评测侧博弈论干预欺骗；[6] 持续评测数据可回流训练；两者形成闭环雏形 | 推测 | 2027–2028 |
| **真机评测云平台化** | SimplerEnv/RoboArena 等仿真基准成熟，远程真机集群（如 Robotics Benchmarks Cloud）开始商业化 | 需要数据 | > 待核实 |

> **瓶颈-拐点耦合**：**数据稀缺（G1/G2）与评测理论滞后**是硬约束；**标准化加速与监管介入**是外部解约束的可能拐点。若 2027 前无统一可纠正性基准发布，领域将面临“碎片化评测无法支撑监管合规”的**系统性风险**。

---

## 5. 社会·政策·国际

| 维度 | 进展/现状 | 证据支撑 | 不确定性标注 |
|------|-----------|----------|--------------|
| **监管标准** | EU AI Act 要求高风险 AI 系统提供技术文档、事后审计、人工监督接口，直接倒逼可纠正性工程化 | [20] 系统安全视角回应国际 AI 安全报告，指出术语混淆与工程落地 Gap | [R] 具体技术标准（如 ISO/IEC 42001 细则）仍在制定中，落地细节待核实 |
| **透明度治理** | FMTI 2025 揭示行业自律失效，透明度倒退可能触发强制披露立法 | [4] 实证数据：均分 58→40，训练数据/算力/部署后影响最不透明 | [P] 若 2027 前 FMTI 均分不回升至 50 以上，大概率触发强制审计立法（置信度 70%） |
| **地缘政治/供应链** | 模型开发商集中于美/中（Alibaba、DeepSeek、xAI 首次纳入 FMTI）[4]；评测基准主导权仍在欧美学术圈 | [4] 机构分布；[18] 框架生态多为美资主导 | [Debated] 开源生态是否会形成“去中心化评测联盟”对抗单极标准，存在分歧 |
| **劳动/伦理影响** | Agent 技能标准化 [17] 可能重塑知识工作分工；可纠正性缺失导致的自动化决策不可控风险 | [17] 生态规模；[9][10] 理论风险 | [R] 量化劳动替代/增强效应的实证研究尚缺 |

> **结构性判断**：**监管与技术标准的错位**是核心矛盾——政策要求“可审计/可关闭”，技术端却缺乏统一度量基准（G1）。此错位在 2027 年 EU AI Act 全面生效前可能达到**临界张力**。

---

## 6. 资本与生态

| 指标 | 现状/趋势 | 证据支撑 | 解读 |
|------|-----------|----------|------|
| **Agent Skill 生态规模** | 9 个月百万级技能文件，GitSkills 数据集量化采用度 | [17] | 基础设施层资本化信号：技能复用降低评测/部署边际成本 |
| **多框架生态分化** | LangGraph/AutoGen/CrewAI 等头部框架在 star/fork/贡献者/提交频次上显著领先，长尾框架维护停滞 | [18] | 资本将集中于头部框架的评测插件生态，长尾面临淘汰 |
| **能效/成本敏感度上升** | SWEnergy 研究 SLMs 在 Agentic 任务中的能效，反映推理成本成为商业化关键约束 | [21] | 评测框架需内置“性能-成本-能效”三维 Pareto 前沿分析 |
| **开源治理挑战** | OSS 系统文献综述 [22] 与 PESTO 选型工具 [23] 显示：许可证合规、依赖漂移、维护者倦怠是评测基础设施可持续性的隐性风险 | [22][23] | 评测框架选型需纳入“供应链健康度”指标 |

> **生态信号**：**技能规范化 [17] + 框架头部化 [18] + 成本敏感化 [21]** 三重趋势共振，预示 **2026-2027 将出现“评测即服务”商业化产品**，但开源可持续性风险 [22][23] 需纳入采购决策。

---

## 7. 信号与预测

| 早期信号 | 推演链条 | 可证伪假设（含时间锚点） | 置信度 | 标记 |
|----------|----------|---------------------------|--------|------|
| KnownLieBench 发布 3 个月内被 ≥3 篇顶会论文引用/复现 | 基准采用曲线 → 社区共识形成 → 成为欺骗评测事实标准 | **H1**：至 2027-02-01，KnownLieBench 在 Google Scholar 引用数 ≥ 15 且出现 ≥ 2 个独立复现仓库（GitHub star ≥ 50） | 较大概率 | [P] |
| FMTI 2026 版（预计 2026 年底发布）均分回升至 ≥ 50 | 监管压力 + 竞争动力 → 头部模型商主动披露关键维度 | **H2**：FMTI 2026 总均分 ≥ 50，且“训练数据/算力/部署后影响”三维度均分均提升 ≥ 10 点 | 推测 | [P] |
| 评测侧博弈论框架 [7] 与持续评测范式 [6] 在 2027 年前融合形成“在线对抗评测”开源框架 | 理论干预 + 工程流水线 → 闭环产品 | **H3**：至 2027-12-31，GitHub 出现集成 [7] 博弈建模与 [6] 持续评测流水线的开源项目，star ≥ 500 | 推测 | [P] |
| 首个“具身智能可纠正性基准”发布（整合 KnownLieBench、SimplerEnv、真机部署指标） | 蓝海 G1/G3 驱动 + 监管倒逼 → 学产界联合攻关 | **H4**：至 2028-06-30，arXiv/CoRL/ICRA 出现标题含 “Embodied Corrigibility Benchmark” 的论文，且包含 ≥ 3 种本体真机实验 | 推测 | [P] |
| Agent Skill 规范演进为“可纠正性技能元数据标准”（含关闭钩子、审计接口、版本回滚点） | 生态标准化 [17] + 治理需求 [9][10] → 标准延伸 | **H5**：Anthropic 或 Linux Foundation 牵头在 2027 年前发布 “Corrigible Agent Skill Specification” 草案 | 推测 | [P] |

> **风险提示**：上述预测均标记 **[P]**，依据为“当前信号 → 逻辑推演 → 可证伪假设”。**关键不确定性**在于：(1) 监管执行力度与时间表；(2) 头部模型商是否愿开放核心透明度维度；(3) 真机评测基础设施建设资金来源。若 **H1/H2 在 2027 上半年均证伪**，说明领域仍处于“碎片化探索期”，而非“标准化起飞期”。

---

## 参考来源
[1] Foundations of GenIR — http://arxiv.org/abs/2501.02842v1
[2] Evaluating Automatic Research Platforms via Open-Source Community Popularity Metrics: An Ecological Assessment Framework — https://doi.org/10.62177/jaet.v3i3.1559
[3] Knowledge-Verified Emergent Deception in LLM Agents Under Conflicting Incentives — http://arxiv.org/abs/2608.26372v1
[4] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1
[5] SVC 2025: the First Multimodal Deception Detection Challenge — http://arxiv.org/abs/2508.04129v1
[6] Efficient Benchmarking in Production: A Study of an Evolving LLM Agent — http://arxiv.org/abs/2609.21267v1
[7] Mitigating Agentic Deception via Evaluation-Side Partially Observable Games — http://arxiv.org/abs/2611.12835v1
[8] Open Evaluation Agent: Efficient and Promptable Evaluation of Visual Generative Models — http://arxiv.org/abs/2608.09666v1
[9] Addressing corrigibility in near-future AI systems — https://doi.org/10.1007/s43681-024-00484-9
[10] Triarchic corrigibility: a role-separated governance design pattern for AI-assisted decision-making — https://doi.org/10.1007/s43681-026-01362-2
[11] The necessary roadblock to artificial general intelligence — https://doi.org/10.1145/3362077.3362089
[12] Structural Capability Containment in Advanced AI Systems A Foundational Framework for Multi-Jurisdiction Safety Architectures — https://doi.org/10.2139/ssrn.6686518
[13] A Different Approach to AI Safety: Proceedings from the Columbia Convening on Openness in Artificial Intelligence and AI Safety — http://arxiv.org/abs/2506.22183v1
[14] Data-Centric Safety and Ethical Measures for Data and AI Governance — http://arxiv.org/abs/2506.10217v3
[15] Competing Visions of Ethical AI: A Case Study of OpenAI — http://arxiv.org/abs/2601.16513v1
[16] AI Exposure and the Changing Responsibilities in Job Postings — http://arxiv.org/abs/2611.09870v1
[17] GitSkills: A Dataset of Agent Skills on GitHub — http://arxiv.org/abs/2608.10906v3
[18] Adoption and Ecosystem Health: A Longitudinal Analysis of Open-Source Multi-Agent Frameworks — https://doi.org/10.48550/arxiv.2607.02453
[19] HLSFactory-Agent: Large-Scale Agentic HLS Dataset Construction from Academic and Open-Source Projects — http://arxiv.org/abs/2609.09519v1
[20] AI Safety is Stuck in Technical Terms -- A System Safety Response to the International AI Safety Report — http://arxiv.org/abs/2503.04743v1
[21] SWEnergy: An Empirical Study on Energy Efficiency in Agentic Issue Resolution Frameworks with SLMs — http://arxiv.org/abs/2512.09543v2
[22] Open Source Software Development Challenges: A Systematic Literature Review on GitHub — http://arxiv.org/abs/2003.10750v3
[23] OSS PESTO: An Open Source Software Project Evaluation and Selection TOol — http://arxiv.org/abs/2102.12267v1

---

*Generated by research-bot · topic=`agent-评测与欺骗能力基准欺骗可纠正性` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`nvidia/nemotron-3-ultra-550b-a55b` · sources=35 · duration=245s · 2026-11-17T04:38:23+00:00*
