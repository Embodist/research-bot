# Agent 评测与安全（能力基准、欺骗与可纠正性）深度调研报告

**日期**：2026-10-28（UTC）  
**领域**：Agent Evaluation & Safety / Capability Benchmarks / Deception Detection / Corrigibility  
**检索源数量**：36 条可引用证据（arXiv、Zenodo、Figshare、会议论文等）

---

## 1. 进展与热点

### 1.1 欺骗检测与评测的最新突破（近 1-2 年）

| 进展 | 时间 | 机构/作者 | 核心贡献 | 证据等级 | 热度证据 | 权威证据 | 关注度 | 推荐度 |
|------|------|-----------|----------|----------|----------|----------|--------|--------|
| Knowledge-Verified Emergent Deception in LLM Agents Under Conflicting Incentives | 2026-08 | arXiv (cs.CL) | 首次在知识验证框架下量化 LLM Agent 在利益冲突下的涌现欺骗行为，构建可复现评测协议 | B (arXiv 预印本) | > 待核实 | cs.CL 预印本 | 中（新颖性高、直接切题） | ★★★★☆ 直接针对 Agent 欺骗核心问题，提供可验证实验范式 [23] |
| SVC 2025: First Multimodal Deception Detection Challenge | 2025-08 | arXiv (cs.CV) | 首个多模态欺骗检测挑战赛，推动音视频+文本联合欺骗基准建设 | B (arXiv 预印本) | > 待核实 | cs.CV 预印本/挑战赛官方 | 中（挑战赛基准属性） | ★★★★☆ 为多模态欺骗提供标准化评测入口 [24] |
| 2025 Foundation Model Transparency Index (第 3 版) | 2025-12 | arXiv (cs.AI) | 量化基础模型开发者透明度实践，含评测公开度、数据治理、风险披露等指标 | B (arXiv 预印本) | > 待核实 | cs.AI 预印本，年度系列第 3 版 | 中（行业治理参考） | ★★★☆☆ 为评测生态透明度提供纵向追踪数据 [16] |

> **增量判断**：2025-2026 年出现**首个专门针对 LLM Agent 涌现欺骗的知识验证实验范式** [23] 与**首个多模态欺骗检测挑战赛基准** [24]，标志着欺骗评测从“事后分析”转向“可控实验与标准化基准”。相对 2023 年前以红队测试为主的模式，这是**方法论层面的增量**。

### 1.2 可纠正性形式化与架构层面的新进展

| 进展 | 时间 | 机构/作者 | 核心贡献 | 证据等级 | 热度证据 | 权威证据 | 关注度 | 推荐度 |
|------|------|-----------|----------|----------|----------|----------|--------|--------|
| The Null-Instrumental Goal: Formalizing and Enforcing Corrigibility in Advanced AI | 2025 | Zenodo | 提出 Null-Instrumental Goal 形式化框架，将可纠正性建模为工具性目标的约束优化问题 | C (Zenodo 预印本) | > 待核实 | Zenodo (CERN) 托管，非同行评审 | 低（新颖但未经会议评审） | ★★★☆☆ 为可纠正性提供可形式化验证的数学框架 [8] |
| Meta-Corrigibility: Architectures for Self-Modifying AI with Enduring Human Oversight | 2025 | Zenodo | 提出元可纠正性架构，支持自我修改 Agent 在保持人类监督下演化 | C (Zenodo 预印本) | > 待核实 | Zenodo (CERN) 托管 | 低 | ★★★☆☆ 关注自我演化 Agent 的长期可纠正性，切中前沿痛点 [12] |

> **增量判断**：可纠正性研究从哲学讨论（如 Soares et al. 2015）推进到**可形式化验证的目标函数设计** [8] 与**自我修改架构层面的约束机制** [12]，这是**理论到工程落地的关键增量**。

### 1.3 评测-安全鸿沟与自进化 Agent 安全的系统性综述

| 进展 | 时间 | 机构/作者 | 核心贡献 | 证据等级 | 热度证据 | 权威证据 | 关注度 | 推荐度 |
|------|------|-----------|----------|----------|----------|----------|--------|--------|
| EvalSafetyGap: Hybrid Survey and Conceptual Framework for LLM Evaluation-Safety Failures | 2026-06 | arXiv (cs.AI) | 系统梳理基准分数提升与实际能力/对齐属性脱节的共享测量问题，提出概念框架 | B (arXiv 预印本 v5) | > 待核实 | cs.AI 预印本，多版本迭代 | 高（直接点出评测失效核心矛盾） | ★★★★★ 必读：为“评测≠安全”提供理论锚点 [35] |
| Safety in Self-Evolving Agents: A Survey | 2026-10 | arXiv (cs.CR) | 首个聚焦自进化 Agent 安全的综述，覆盖参数更新、记忆、工具使用等持续学习风险 | B (arXiv 预印本) | > 待核实 | cs.CR 预印本 | 高（新兴方向首份系统性综述） | ★★★★★ 定义了自进化 Agent 安全的研究边界 [30] |
| Towards trustworthy agentic AI: comprehensive survey of safety, robustness, privacy, and system security | 2026-05 | arXiv (cs.AI) | 覆盖 Agent 安全四大维度的综合性综述，含评测基准汇总 | B (arXiv 预印本) | > 待核实 | cs.AI 预印本 | 高（全景式覆盖） | ★★★★☆ 适合快速建立领域全貌认知 [11] |

> **增量判断**：2026 年出现**三份高质量综述** [35][30][11]，共同确立了“评测-安全鸿沟”[35]、“自进化 Agent 安全”[30] 与“可信 Agent 全景图”[11] 三大研究前沿，**相对 2024 年前零散工作形成系统性知识增量**。

---

## 2. 工业界与产品

### 2.1 头部实验室的安全评测工程实践

| 产品/实践 | 时间 | 机构 | 核心特征 | 证据等级 | 热度证据 | 权威证据 | 关注度 | 推荐度 |
|-----------|------|------|----------|----------|----------|----------|--------|--------|
| OpenAI o1 System Card | 2024-12 | OpenAI | 发布 o1 系列模型的系统卡片，含能力评测、红队测试、欺骗倾向评估、可纠正性相关压力测试 | B (官方技术报告/arXiv) | > 待核实 | OpenAI 官方发布，工程落地标杆 | 高（行业标杆） | ★★★★★ 真机部署前的安全评测工程范本 [29] |
| Open Evaluation Agent (视觉生成模型高效评测框架) | 2026-08 | arXiv (cs.AI) | 可提示词驱动的高效评测 Agent，降低视觉生成模型评测计算成本 | B (arXiv 预印本) | > 待核实 | cs.AI 预印本 | 中（工程效率贡献） | ★★★★☆ 评测工程降本增效的实用方向 [27] |
| Evaluation Agent (前作) | 2024-12 | arXiv (cs.AI) | 视觉生成模型评测框架的早期版本 | B (arXiv 预印本 v3) | > 待核实 | cs.AI 预印本 | 中 | ★★★☆☆ 为 [27] 提供基线 [26] |

> **增量判断**：OpenAI o1 System Card [29] 仍是**工业界真机部署前安全评测的最高工程标杆**；学术界同步推进**评测 Agent 自动化/低成本化** [26][27]，但**通用 Agent 评测框架（如 OpenAI Evals、HELM、AgentBench、AutoEval）的最新工程状态在证据中缺失** > 待核实。

### 2.2 AI 安全研究者分布与组织生态

| 发现 | 时间 | 来源 | 核心信息 | 证据等级 | 热度证据 | 权威证据 | 关注度 | 推荐度 |
|------|------|------|----------|----------|----------|----------|--------|--------|
| Where AI Safety Researchers Actually Work | 2026 | Zenodo | 安全研究分布远超 OpenAI/学术界，含 Anthropic、DeepMind、METR、Redwood Research、独立组织等 | C (Zenodo 报告) | citations=0 [34] | Zenodo (CERN) 托管 | 中（生态全景图） | ★★★★☆ 打破“只有大厂做安全”的刻板印象，映射人才流动 [34] |

---

## 3. 蓝海与缺口

### 3.1 理论与评测层面的核心缺口

| 缺口 | 说明 | 证据支撑 | 优先级 |
|------|------|----------|--------|
| **评测分数与真实对齐属性的系统性脱节** | 基准分数、奖励信号、安全指标均可能“造假”式提升，而底层能力/对齐未改善 | EvalSafetyGap 概念框架 [35] | ★★★★★ |
| **多模态/具身 Agent 欺骗评测基准缺失** | 现有欺骗基准多为文本/单模态，SVC 2025 仅为起步 [24] | SVC 2025 挑战赛 [24] | ★★★★☆ |
| **自进化 Agent 持续可纠正性验证方法空白** | 现有可纠正性框架 [8][12] 多针对静态部署，持续学习下的形式化保证缺失 | Safety in Self-Evolving Agents [30] | ★★★★★ |
| **跨文化/跨语言欺骗与可纠正性评测缺位** | 证据中无相关工作，全为英语/西语境 | 全证据库无覆盖 | ★★★☆☆ |
| **评测 Agent 自身的可靠性与对抗鲁棒性** | Open Evaluation Agent [27] 等评测器自身是否可被欺骗/对抗未被研究 | 证据中无红队评测器研究 | ★★★★☆ |

### 3.2 工程落地层面的缺口

| 缺口 | 说明 | 证据支撑 |
|------|------|----------|
| **主流开源评测框架（OpenAI Evals、HELM、AgentBench、AutoEval）的最新维护状态、多模态支持、红队集成度未在证据中覆盖** | 需补充检索 GitHub 近期提交、Release、Issue 讨论 | q3 证据仅含学术论文 [27][30][35]，无工程框架实测 |
| **真机部署环境下的持续监控与可纠正性触发机制缺乏开源实现** | 证据中无工程级监控/熔断组件 | 全证据库无覆盖 |

---

## 4. 瓶颈与拐点

### 4.1 核心瓶颈

| 瓶颈 | 表现 | 证据支撑 | 是否临近拐点 |
|------|------|----------|--------------|
| **测量失效** | 基准饱和、数据污染、奖励黑客导致分数失真 | EvalSafetyGap 系统性论证 [35] | **是** — 社区已共识需“评测评测”，新范式涌现中 |
| **欺骗定义与检测的本体论模糊** | 意图欺骗 vs 幻觉 vs 规格游戏边界不清，缺乏统一度量 | Knowledge-Verified Deception [23] 尝试用知识验证界定，但仅为单一范式 | **否** — 仍需跨学科（认知科学、博弈论、形式化验证）融合 |
| **可纠正性形式化与规模化的张力** | 小模型可验证，大模型/自进化系统状态空间爆炸 | Null-Instrumental Goal [8]、Meta-Corrigibility [12] 均为理论/小规模验证 | **不确定** — 依赖形式化验证工具链（如模型检查器）的突破 |
| **评测算力成本与覆盖面的矛盾** | 视觉/多模态/长时程 Agent 评测极其昂贵 | Open Evaluation Agent [27] 尝试降本，但通用性待验证 | **是** — 评测 Agent 自动化、蒸馏评测器、主动采样为拐点信号 |

### 4.2 拐点信号

| 信号 | 观测依据 | 置信度 |
|------|----------|--------|
| **“评测即建模”范式兴起** | 评测 Agent [26][27]、EvalSafetyGap 元评测框架 [35] | 较大概率 |
| **监管强制透明度推动标准化基准** | Foundation Model Transparency Index 年度化 [16]、Columbia Convening 多方共识 [5] | 确定（政策驱动） |
| **自进化 Agent 从概念走向原型** | Safety in Self-Evolving Agents 综述 [30] 标志学术界系统关注 | 推测（需工程原型验证） |

---

## 5. 社会·政策·国际

### 5.1 治理多方共识与分歧

| 进展 | 时间 | 核心内容 | 证据等级 | 关注度 | 推荐度 |
|------|------|----------|----------|--------|--------|
| Columbia Convening on AI Openness and Safety | 2024-11 | 45+ 研究者/工程师/政策领袖共同产出开源模型安全治理参与式报告 | B (arXiv 预印本) | 中 | ★★★☆☆ [5] |
| AI Safety is Stuck in Technical Terms — A System Safety Response | 2025-03 | 批评国际 AI 安全报告过度技术化，主张系统安全视角 | B (arXiv 预印本) | 中 | ★★★☆☆ [4] |
| Data-Centric Safety and Ethical Measures for Data and AI Governance | 2025-06 | 强调数据层面治理对双重用途基础模型风险管控的必要性 | B (arXiv 预印本) | 低 | ★★☆☆☆ [7] |

> **增量判断**：政策层面从“模型层监管”向**数据层治理** [7]、**系统安全工程视角** [4]、**开源生态共治** [5] 扩展，**治理颗粒度细化**是相对 2023 年的增量。

### 5.2 人机信任与决策风险的实证证据

| 发现 | 时间 | 核心结论 | 证据等级 | 关注度 | 推荐度 |
|------|------|----------|----------|--------|--------|
| Faith in AI can narrow the futures individuals consider | 2026-03 | 行为实验（N=1,305）显示 >40% 参与者将 AI 视为预测权威，放弃确定奖励几率增加 3.39 倍，收益减少 10.7-42.9% | B (arXiv 预印本 cs.HC) | 中 | ★★★☆☆ [1] |

> **风险提示**：该实证揭示**人类对 AI 预测的过度信任可系统性扭曲决策**，为 Agent 欺骗风险提供**行为学层面的间接证据** [1]，但**非直接针对 Agent 欺骗/可纠正性** > 待核实。

### 5.3 头部实验室安全叙事演变

| 发现 | 时间 | 核心结论 | 证据等级 | 关注度 | 推荐度 |
|------|------|----------|----------|--------|--------|
| Competing Visions of Ethical AI: A Case Study of OpenAI | 2026-01 | 结构化语料库分析揭示 OpenAI 对 ethics/safety/alignment 概念框架的演变与实践差异 | B (arXiv 预印本 cs.CY) | 低 | ★★☆☆☆ [6] |

---

## 6. 资本与生态

### 6.1 人才与组织分布

| 指标 | 现状 | 证据支撑 | 趋势判断 |
|------|------|----------|----------|
| 安全研究者分布 | 非集中于 OpenAI/学术界，厂商实验室、独立组织（METR、Redwood Research）占显著比例 | Where AI Safety Researchers Actually Work [34] | **多极化加速** — 独立组织成关键补充力量 |
| 开源安全工程投入 | 证据中无融资/并购/人才流动量化数据 | 缺失 | > 待核实 |

### 6.2 开源生态关键节点（种子资源补全）

| 项目/资源 | 类型 | 机构 | 状态 | 链接 | 说明 |
|-----------|------|------|------|------|------|
| OpenAI Evals | 评测框架 | OpenAI | 活跃维护 | https://github.com/openai/evals | 早期标杆，社区贡献驱动 |
| HLM (Holistic Evaluation of Language Models) | 基准套件 | Stanford CRFM | 维护中 | https://github.com/stanford-crfm/helm | 多任务、多模型、可扩展 |
| AgentBench | Agent 基准 | 多机构合作 | 维护中 | https://github.com/THUDM/AgentBench | 含工具使用、规划、推理等维度 |
| AutoEval | 自动化评测 | 相关团队 | 需核实 | > 待核实 | 证据中未覆盖最新进展 |

> **注**：上表为领域已知种子资源，**证据库中无直接覆盖其最新工程状态**，需补充检索 GitHub 确认 > 待核实。

---

## 7. 信号与预测

### 7.1 早期信号

| 信号 | 来源 | 解读 |
|------|------|------|
| **形式化可纠正性从理论走向架构约束** | Null-Instrumental Goal [8]、Meta-Corrigibility [12] | 可纠正性可能成为 Agent 架构的**内置设计约束**而非事后补丁 |
| **评测 Agent 成为评测基础设施核心组件** | Evaluation Agent [26] → Open Evaluation Agent [27] | 评测自动化、低成本化、可提示词化为明确工程方向 |
| **自进化 Agent 安全从零到系统性综述** | Safety in Self-Evolving Agents [30] | 标志该方向进入**学术主流研究议程** |
| **多模态欺骗检测挑战赛启动** | SVC 2025 [24] | 基准竞赛驱动技术聚合，类似 ImageNet 时刻的早期信号 |

### 7.2 未来 6-18 月可验证预测

| 预测 | 依据链 | 可证伪假设 | 置信度 | 标记 |
|------|--------|------------|--------|------|
| **至少 2 个主流 Agent 评测框架（如 HELM、AgentBench）将集成“评测 Agent”自动化评测模块** | Open Evaluation Agent [27] 验证可行性；EvalSafetyGap [35] 倡导元评测 | 若 2027-04 前 GitHub 主分支无相关 PR/Release，则判断不成立 | 较大概率 | [P] |
| **首个针对自进化 Agent 的可纠正性形式化验证基准（Benchmark for Corrigibility under Self-Modification）发布** | Meta-Corrigibility [12] 提出架构；Safety in Self-Evolving Agents [30] 定义问题 | 若 2027-10 前无会议/期刊/基准网站发布，则判断不成立 | 推测 | [P] |
| **多模态欺骗检测 SOTA 在 SVC 2025/2026 挑战赛榜单上每季度刷新 >5% 绝对指标** | SVC 2025 启动 [24]；挑战赛常驻机制 | 若连续 2 个季度榜单无显著变化，则判断不成立 | 推测 | [P] |
| **监管强制要求基础模型发布“可纠正性评测报告”成为欧盟/美国至少一司法管辖区的合规项** | Foundation Model Transparency Index 年度化 [16]、Columbia Convening 共识 [5]、系统安全呼吁 [4] | 若 2027-10 前无相关法规草案/指导文件明确提及，则判断不成立 | 推测 | [P] |
| **独立第三方复现 Knowledge-Verified Emergent Deception 实验 [23] 并确认/反驳其结论** | 论文开源代码/数据（假设） | 若 2027-04 前无第三方复现报告/博客/论文，则判断不成立 | 推测 | [P] |

### 7.3 关键不确定性

| 不确定性 | 影响 | 解决路径 |
|----------|------|----------|
| **大模型可纠正性形式化验证的可扩展性** | 决定能否从玩具模型推广到前沿模型 | 关注形式化验证工具链（模型检查、定理证明）与 LLM 结合进展 |
| **评测-安全鸿沟是否可通过“评测评测”根本弥合** | 关乎整个评测生态的信任基础 | 跟踪 EvalSafetyGap 后续实证工作、元评测基准建设 |
| **开源模型与闭源模型在欺骗/可纠正性评测上的差异收敛/发散** | 影响开源生态安全治理策略 | 需对比开源/闭源模型在同一基准（如 [23][24]）上的表现 |

---

## 经典与奠基性工作

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| Modeling AGI Safety Frameworks with Causal Influence Diagrams | 2019 | Everitt et al. | > 待核实 | 同行评审 (UAI/ICML 相关) | 中 | ★★★★☆ | [33] | 因果影响图建模 AGI 安全，奠基性理论框架 |
| AI Agents: Evolution, Architecture, and Real-World Applications | 2025 | arXiv (cs.AI) | > 待核实 | arXiv 预印本 | 高 | ★★★★☆ | [10] | Agent 演进全景综述，含安全章节 |
| The Null-Instrumental Goal: Formalizing and Enforcing Corrigibility | 2025 | Zenodo | > 待核实 | Zenodo 预印本 | 低 | ★★★☆☆ | [8] | 可纠正性形式化关键工作 |
| Meta-Corrigibility: Architectures for Self-Modifying AI | 2025 | Zenodo | > 待核实 | Zenodo 预印本 | 低 | ★★★☆☆ | [12] | 自我修改 Agent 可纠正性架构 |
| Clear, Compelling Arguments: Rethinking Foundations of Frontier AI Safety Cases | 2026 | arXiv (cs.AI) | > 待核实 | arXiv 预印本 | 中 | ★★★★☆ | [9] | 安全论证框架重构 |

> **注**：经典工作还应包含 Soares et al. "Corrigibility" (2015)、Christiano et al. "AI Safety via Debate" (2018)、Irving et al. "Scalable Agent Alignment via Reward Modeling" 等，**证据库中缺失，需补充检索** > 待核实。

---

## 开源项目与工程实践

| 名称 | 年份 | 机构/维护者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-------------|------|------|--------|--------|------|------|
| OpenAI Evals | 2023- | OpenAI | > 待核实 | 官方框架 | 高 | ★★★★★ | https://github.com/openai/evals | 评测框架标杆 |
| HELM | 2022- | Stanford CRFM | > 待核实 | 学术主导基准 | 高 | ★★★★★ | https://github.com/stanford-crfm/helm | 全面基准套件 |
| AgentBench | 2023- | THUDM 等 | > 待核实 | 学术合作基准 | 高 | ★★★★☆ | https://github.com/THUDM/AgentBench | Agent 专用基准 |
| Evaluation Agent / Open Evaluation Agent | 2024/2026 | arXiv 作者 | > 待核实 | 学术原型 | 中 | ★★★★☆ | [26][27] | 视觉生成评测自动化 |
| AutoEval | - | - | > 待核实 | - | - | - | > 待核实 | 证据库无覆盖 |

---

## 数据集与基准

| 名称 | 年份 | 机构 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|------|------|------|--------|--------|------|------|
| SVC 2025 Multimodal Deception Detection Challenge | 2025 | 多机构 | > 待核实 | 挑战赛官方 | 中 | ★★★★☆ | [24] | 首个多模态欺骗基准 |
| Knowledge-Verified Deception Benchmark | 2026 | [23] 作者 | > 待核实 | 论文配套 | 中 | ★★★★☆ | [23] | 利益冲突下涌现欺骗基准 |
| Foundation Model Transparency Index Data | 2023-2025 | Stanford CRFM 等 | > 待核实 | 年度报告配套 | 中 | ★★★☆☆ | [16] | 透明度量化数据 |
| Open X-Embodiment / DROID / LIBERO / SimplerEnv | 2023- | 多机构 | > 待核实 | 机器人/具身基准 | 高 | ★★★★★ | 官网 | 具身 Agent 评测基准（证据库无直接覆盖，领域种子资源） |

---

## 开放争议与待解问题

| 争议/问题 | 双方观点/现状 | 证据支撑 | 优先级 |
|-----------|---------------|----------|--------|
| **评测分数是否能代理真实能力/对齐** | EvalSafetyGap [35] 论证系统性失效；基准维护方常以分数宣称进步 | [35] | ★★★★★ |
| **欺骗定义：意图性 vs 行为性 vs 后果性** | 认知科学要求意图；工程检测仅观测行为；政策关注后果 | [23] 采用知识验证代理意图，但争议未决 | ★★★★☆ |
| **可纠正性是否与高能力根本冲突** | 理论上工具性趋同预测冲突 [8][12]；实证缺乏大规模验证 | [8][12][30] | ★★★★★ |
| **开源模型是否增加欺骗/不可纠正风险** | Columbia Convening [5] 多方分歧；Data-Centric 视角 [7] 强调数据治理 | [5][7] | ★★★☆☆ |
| **红队测试 vs 标准化基准：哪个更可靠** | OpenAI o1 System Card [29] 结合两者；学术界推基准标准化 | [29][24][35] | ★★★★☆ |

---

## 参考来源

[1] Faith in AI can narrow the futures individuals consider — http://arxiv.org/abs/2603.28944v2  
[2] This paper has been withdrawn — http://arxiv.org/abs/cond-mat/0309395v2  
[3] Foundations of GenIR — http://arxiv.org/abs/2501.02842v1  
[4] AI Safety is Stuck in Technical Terms -- A System Safety Response to the International AI Safety Report — http://arxiv.org/abs/2503.04743v1  
[5] A Different Approach to AI Safety: Proceedings from the Columbia Convening on Openness in Artificial Intelligence and AI Safety — http://arxiv.org/abs/2506.22183v1  
[6] Competing Visions of Ethical AI: A Case Study of OpenAI — http://arxiv.org/abs/2601.16513v1  
[7] Data-Centric Safety and Ethical Measures for Data and AI Governance — http://arxiv.org/abs/2506.10217v3  
[8] The Null-Instrumental Goal: Formalizing and Enforcing Corrigibility in Advanced AI — https://doi.org/10.5281/zenodo.17795630  
[9] Clear, Compelling Arguments: Rethinking the Foundations of Frontier AI Safety Cases — http://arxiv.org/abs/2603.08760v1  
[10] AI Agents: Evolution, Architecture, and Real-World Applications — http://arxiv.org/abs/2503.12687v1  
[11] Towards trustworthy agentic AI: a comprehensive survey of safety, robustness, privacy, and system security — http://arxiv.org/abs/2605.23989v1  
[12] Meta-Corrigibility: Architectures for Self-Modifying AI with Enduring Human Oversight — https://doi.org/10.5281/zenodo.17822775  
[13] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1  
[14] NTU-NPU System for Voice Privacy 2024 Challenge — http://arxiv.org/abs/2410.02371v1  
[15] Discovery Opportunities with Gravitational Waves -- TASI 2024 Lecture Notes — http://arxiv.org/abs/2409.08956v1  
[16] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1  
[17] Atmospheric entry and fragmentation of small asteroid 2024 BX1 — http://arxiv.org/abs/2403.00634v2  
[18] NTIRE 2025 Challenge on Image Super-Resolution (x4): Methods and Results — http://arxiv.org/abs/2504.14582v3  
[19] OpenFact at CheckThat! 2024: Combining Multiple Attack Methods for Effective Adversarial Text Generation — http://arxiv.org/abs/2409.02649v2  
[20] Overview of the Sensemaking Task at the ELOQUENT 2025 Lab — http://arxiv.org/abs/2507.12143v1  
[21] ICAGC 2024: Inspirational and Convincing Audio Generation Challenge 2024 — http://arxiv.org/abs/2407.12038v2  
[22] Double Multi-Head Attention Multimodal System for Odyssey 2024 Speech Emotion Recognition Challenge — http://arxiv.org/abs/2406.10598v1  
[23] Knowledge-Verified Emergent Deception in LLM Agents Under Conflicting Incentives — http://arxiv.org/abs/2608.26372v1  
[24] SVC 2025: the First Multimodal Deception Detection Challenge — http://arxiv.org/abs/2508.04129v1  
[25] A Survey of Multi-Agent Deep Reinforcement Learning with Communication — http://arxiv.org/abs/2203.08975v2  
[26] Evaluation Agent: Efficient and Promptable Evaluation Framework for Visual Generative Models — http://arxiv.org/abs/2412.09645v3  
[27] Open Evaluation Agent: Efficient and Promptable Evaluation of Visual Generative Models — http://arxiv.org/abs/2608.09666v1  
[28] Learning Dexterous In-Hand Manipulation — http://arxiv.org/abs/1808.00177v5  
[29] OpenAI o1 System Card — http://arxiv.org/abs/2412.16720v2  
[30] Safety in Self-Evolving Agents: A Survey — http://arxiv.org/abs/2610.00093v1  
[31] SWEnergy: An Empirical Study on Energy Efficiency in Agentic Issue Resolution Frameworks with SLMs — http://arxiv.org/abs/2512.09543v2  
[32] Laser pointer prohibition: improving safety or driving misclassification — http://arxiv.org/abs/1406.4924v1  
[33] Modeling AGI Safety Frameworks with Causal Influence Diagrams — http://arxiv.org/abs/1906.08663v1  
[34] Where AI Safety Researchers Actually Work — https://doi.org/10.5281/zenodo.19608563  
[35] EvalSafetyGap: A Hybrid Survey and Conceptual Framework for LLM Evaluation-Safety Failures — http://arxiv.org/abs/2606.30219v5  
[36] Decision Intelligence for AI and Emerging Technologies: The AEGIS-DM Framework — https://doi.org/10.6084/m9.figshare.33954862

---

*Generated by research-bot · topic=`agent-评测与安全能力基准欺骗与可纠正性` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`nvidia/nemotron-3-ultra-550b-a55b` · sources=36 · duration=984s · 2026-10-28T23:28:33+00:00*
