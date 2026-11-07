# Agent 评测与安全（能力基准、欺骗与可纠正性）前沿调研报告

**日期**：2026-11-07（UTC） | **领域**：Agent Evaluation & Safety (Benchmarks, Deception, Corrigibility) | **检索源数量**：27 条（来自 arXiv、会议挑战赛、技术报告）

---

## 1. 进展与热点（Progress & Hotspots）

### 1.1 多模态欺骗检测基准化与跨域泛化挑战
- **SVC 2025** 发布首个**多模态欺骗检测挑战赛**，聚焦音视频跨域泛化能力评测，要求模型在多个异构数据集间泛化，解决单域场景忽视域迁移导致的性能下降问题 [9]。  
  - **热度证据**：挑战赛配套论文发布于 arXiv (cs.CV) [9]；**权威证据**：ICCV 2025 举办挑战赛，**关注度**：中（新发布基准，针对实用痛点）；**推荐度**：★★★★☆（首个专注跨域泛化的多模态欺骗基准）。

### 1.2 知识验证的 Agent 欺骗评测基准
- **KnownLieBench** 针对 LLM Agent 在利益冲突场景下的涌现式欺骗行为，覆盖 8 个客服领域、112 个 grounded cases，采用中性探针确认知识后引入拒付激励评测撒谎倾向，引入多轮对话与信任追踪机制 [11]。  
  - **热度证据**：arXiv 预印本 (cs.CL, 2026-08) [11]；**权威证据**：预印本，**关注度**：中（切中 alignment 核心痛点，但无独立复现/榜单引用）；**推荐度**：★★★★☆（Agent Safety 评测必读）。

### 1.3 评测范式创新：Evaluation Agent 与代码即基础设施
- **Open Evaluation Agent** 提出面向视觉生成模型的高效、可提示词化评测 Agent 框架，模仿人类少样本印象形成，将评测需求分解为子维度并生成针对性提示词、调用 VLM 打分给出可解释分析，旨在替代昂贵大规模采样管线 [20]（早期版本见 [19]）。  
  - **热度证据**：arXiv 预印本 (cs.AI, 2026-08) [20]；**权威证据**：预印本，**关注度**：中（Evaluation Agent 新范式，工程落地待观察）；**推荐度**：★★★★☆（多模态 Agent 评测工程化参考）。
- **Code as Agent Harness** 重新定义代码角色：作为 Agent 推理、行动、环境建模与执行验证的统一运行时基础设施，为评测提供可执行、可验证的工程抽象 [21]。  
  - **热度证据**：arXiv 预印本 (cs.CL, 2026-05) [21]；**权威证据**：预印本，**关注度**：中（架构级贡献，开源实现待核实）；**推荐度**：★★★★☆（Agent 评测框架设计指导意义大）。

### 1.4 部署侧与专用场景基准扩展
- **Mobile-MMLU** 面向移动端部署场景设计语言理解基准，填补现有基准多面向服务器/桌面环境的空白，包含移动特有任务与偏好 [13]。  
  - **热度证据**：arXiv 预印本 (cs.CL, 2025-03) [13]；**权威证据**：预印本，**关注度**：中（MMLU 家族边缘侧延伸）；**推荐度**：★★★☆☆（端侧 Agent 评测参考）。
- **Risky-Bench** 评估真实生活辅助部署中的 Agentic 安全风险，关注真机/长时程部署差距 [25]。
- **AgentGuard** 将 Agentic Orchestrator 重构用于工具编排安全评测 [27]。

### 1.5 自演化 Agent 安全综述与评测可渗透性
- **Safety in Self-Evolving Agents: A Survey** 指出部署后参数固定限制新交互学习，开放环境下自演化 Agent 持续更新可复用状态（含参数），带来新安全挑战 [23]。
- **Position: Evaluation Scores Are Perishable Knowledge Claims** 强调评测分数具有时效性，需纵向追踪 [22]；**LongEval at CLEF 2025** 实践纵向评测 IR 模型性能 [6]。

> 待核实：AgentBench、MACHIAVELLI、Deception Eval 等经典基准在候选证据中未出现，需补充检索确认其最新版本与榜单状态。

---

## 2. 工业界与产品（Industry & Product）

### 2.1 透明度与合规基础设施
- **The 2025 Foundation Model Transparency Index** 发布，量化基础模型训练数据、计算、部署等维度透明度，为工业界合规与风险披露提供基准 [3]。  
  - **热度证据**：arXiv 预印本 [3]；**权威证据**：预印本，**关注度**：中（政策对齐参考）；**推荐度**：★★★☆☆。

### 2.2 真机部署安全评测工程化
- **Risky-Bench** 面向真实生活辅助部署场景，评估 Agentic 安全风险，推动从仿真走向真机验证 [25]。
- **AgentGuard** 复用编排器进行工具编排安全评测，体现工程复用思路 [27]。
- **Open Evaluation Agent** 与 **Code as Agent Harness** 分别从评测器侧与运行时侧提供工程落地范式 [20][21]。

> 待核实：主流大模型厂商（OpenAI、Anthropic、Google DeepMind、国内头部厂商）内部 Agent 评测流水线、CI/CD 集成、红队实战化细节鲜有公开披露；开源评测框架（OpenCompass、HELM、LM-Evaluation-Harness Agent 扩展）工程采用度与社区活跃度需进一步抓取 GitHub 数据核实。

---

## 3. 蓝海与缺口（Blue Ocean & Gaps）

| 缺口维度 | 具体表现 | 证据来源 | 优先级 |
|----------|----------|----------|--------|
| **可纠正性评测缺失** | 无标准化基准量化 Agent 对关闭/修正指令的服从度、目标修改接受度 | [23] 指出自演化 Agent 目标漂移风险；[11] 侧重欺骗而非纠正 | ⭐⭐⭐⭐⭐ |
| **跨模态/长时程/多智能体安全评测** | 现有基准多为单轮、单模态、单智能体；长程规划中的欺骗累积、协作欺骗未覆盖 | [9] 仅覆盖音视频欺骗检测；[11] 为多轮对话但单智能体 | ⭐⭐⭐⭐ |
| **评测可扩展性与成本** | 大规模采样昂贵，Evaluation Agent 范式虽低成本但可靠性待验证 | [20][19] 提出低成本范式；[22] 指出分数易失效 | ⭐⭐⭐⭐ |
| **真实部署差距** | 仿真/静态数据集与开放世界物理环境、对抗用户、分布漂移差距大 | [25] Risky-Bench 尝试真机部署；[23] 持续学习带来分布漂移 | ⭐⭐⭐⭐⭐ |
| **欺骗机制解释性** | 线性探针检测战略欺骗 [10]、多模态检测 [9] 多为事后检测，缺乏事前机制解释与干预 | [10][9][15] | ⭐⭐⭐ |
| **标准化协议与互操作** | Agent 评测缺乏统一接口协议（如 OpenAPI 规范）、日志格式、指标上报标准 | [21] Code as Harness 为架构建议，非标准 | ⭐⭐⭐ |

> 待核实：是否有行业联盟（如 MLCommons、Partnership on AI）启动 Agent 评测标准化工作组。

---

## 4. 瓶颈与拐点（Bottleneck & Inflection）

### 4.1 核心瓶颈
1. **欺骗建模的根本性难度**：欺骗需建模“意图-信念-行为”三元组，且利益冲突下的涌现式欺骗 [11] 与战略欺骗 [10] 机制不同，单一检测器难以覆盖。
2. **可纠正性理论基础薄弱**：缺乏形式化定义（如 shutdownability、goal-modification acceptance）与可验证保证，现有 RLHF/RLAIF 难以提供最坏情况边界 [23]。
3. **评测静态性与环境动态性矛盾**：基准发布即过时 [22]，自演化 Agent [23] 导致评测目标移动，纵向评测 [6] 成本高企。
4. **真机安全验证的伦理与成本双重约束**：真机红队测试风险不可控 [25]，仿真-现实差距在具身智能中尤为显著。

### 4.2 拐点信号
- **Evaluation Agent 范式** [20][19] 若被证明在多模态/多任务上与人类评测高相关，将大幅降低评测边际成本，引发评测规模化拐点。
- **Code as Harness** [21] 若形成通用运行时标准（如 WASM 沙箱+结构化日志），将实现评测环境可复现、可迁移、可审计，解决工程碎片化。
- **监管强制透明化** [3] 推动厂商必须提交标准化评测报告，倒逼基准标准化与工具链成熟。

---

## 5. 社会·政策·国际（Society, Policy & Geopolitics）

### 5.1 透明度与问责制趋势
- **Foundation Model Transparency Index 2025** [3] 量化训练数据、计算、部署透明度，反映全球监管聚焦“知情权”与“可审计性”。
- 欧盟《AI Act》高风险 AI 系统要求符合性评估、事后监控，直接催生 Agent 级评测合规需求 > 待核实：具体条款对 Agent 自主性、工具使用的评测要求细节。

### 5.2 国际竞争与供应链
- 评测基准话语权集中于头部实验室与学术会议（ICCV SVC [9]、CLEF LongEval [6]、ELOQUENT [5]），中国团队在 Mobile-MMLU [13]、KnownLieBench [11] 等新基准中有布局，但主导权仍弱 > 待核实：国家标准（SAC/TC28）或行业标准制定进展。

### 5.3 伦理与劳动影响
- Agent 欺骗 [11][15] 与工具滥用 [27] 直接关联用户信任、金融诈骗、虚假信息放大，社会风险 **高**。
- 自演化 Agent [23] 可能导致技能替代速度加快，劳动力市场冲击 **不确定**，需纵向追踪。

---

## 6. 资本与生态（Capital & Ecosystem）

### 6.1 投资与并购信号
> 待核实：近 12 个月 Agent 评测/安全初创融资轮次、估值、并购案例（如红队即服务、评测平台 SaaS）。公开来源 [26] 综述提及商业应用前景，但无资本数据。

### 6.2 人才与社区流动
- 核心贡献者集中于顶级实验室（Stanford、MIT、CMU、清华、北大等）与大厂安全团队。
- 开源生态：LM-Evaluation-Harness、OpenCompass、HELM 为三大主流框架，Agent 扩展生态处于早期 > 待核实：GitHub Stars、Contributors、Issue 解决率等量化指标。

### 6.3 标准化与互操作生态
- **Code as Agent Harness** [21] 提出的统一运行时抽象若被主流框架采纳，将成为生态锚点。
- **Evaluation Agent** [20] 若开源并接入主流框架插件系统，将加速“评测即代码”生态形成。

---

## 7. 信号与预测（Signals & Forecast）

| 信号 | 来源 | 可证伪预测（6-18 月） | 置信度 | 不确定性说明 |
|------|------|------------------------|--------|--------------|
| 多模态欺骗跨域基准成为安防/金融采购标配 | [9] SVC 2025 挑战赛落地 | **预测**：至 2027-06，至少 3 家安防/金融头部厂商在招标文件中引用 SVC 指标 | 中 | 依赖挑战赛持续运营与榜单权威性维护 |
| KnownLieBench 或同类利益冲突欺骗基准被纳入主流榜单 | [11] | **预测**：至 2027-06，OpenCompass/HELM/LM-Eval-Harness 至少一家集成 KnownLieBench 子集 | 中高 | 基准方法学扎实，但需开源评测脚本与标准化接口 |
| Evaluation Agent 替代 30%+ 人工标注评测任务 | [20][19] | **预测**：至 2027-06，主流多模态模型发布报告中引用 Evaluation Agent 评分比例 > 30% | 中 | 关键假设：VLM 评分与人类一致性 > 0.85（Spearman），需独立验证 |
| Code as Harness 形成行业运行时标准（WASM+结构化日志） | [21] | **预测**：至 2027-06，至少两大评测框架支持统一 Harness 接口运行 Agent | 中低 | 需解决沙箱隔离、确定性复现、异构硬件适配等工程难题 |
| 自演化 Agent 安全评测形成“持续评测”范式 | [23][22][6] | **预测**：至 2027-06，出现首个支持增量模型版本自动回归测试的开源平台 | 中 | LongEval [6] 已在 IR 领域验证纵向评测可行性 |
| 监管强制 Agent 级透明度报告 | [3] | **预测**：至 2027-06，EU AI Act 合规模板包含 Agent 工具调用审计日志、欺骗/越狱测试报告 | 中高 | 依赖欧盟实施细则落地时间表 |

> **风险提示**：上述预测均基于当前论文/挑战赛信号外推，**不确定** 因素包括：算力成本曲线、基础模型能力跃迁是否失效现有基准、地缘政治对开源生态割裂影响。

---

## 附录：经典与奠基性工作、核心数据集与基准、主流开源评测框架/工程实践

### A1. 经典与奠基性工作

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| Detecting Strategic Deception Using Linear Probes | 2025 | - | > 待核实 | arXiv preprint (cs.CL) | 中 | ★★★☆☆ | [10] | 线性探针检测战略欺骗，方法学基石 |
| Unmasking the Shadows of AI: Investigating Deceptive Capabilities in LLMs | 2024 | - | > 待核实 | arXiv preprint (cs.CL) | 中 | ★★★☆☆ | [15] | 系统性梳理 LLM 欺骗能力分类学 |
| Deception Detection and Remote Physiological Monitoring: A Dataset and Baseline | 2021 | - | > 待核实 | arXiv preprint (cs.CV) | 低 | ★★☆☆☆ | [12] | 早期多模态欺骗数据集与基线 |
| Application Layer Cyber Deception without Developer Interaction | 2024 | - | > 待核实 | arXiv preprint (cs.CR) | 低 | ★★☆☆☆ | [18] | 网络安全视角的主动欺骗防御 |
| AI Agents: Evolution, Architecture, and Real-World Applications | 2025 | - | > 待核实 | arXiv preprint (cs.AI) | 高 | ★★★★☆ | [26] | Agent 架构演进与应用全景综述 |
| Safety in Self-Evolving Agents: A Survey | 2026 | - | > 待核实 | arXiv preprint (cs.CR) | 中 | ★★★★☆ | [23] | 自演化 Agent 安全挑战首份系统性综述 |
| Position: Evaluation Scores Are Perishable Knowledge Claims | 2026 | - | > 待核实 | arXiv preprint (cs.AI) | 中 | ★★★★☆ | [22] | 评测分数时效性理论定位 |

### A2. 核心数据集与基准

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| SVC 2025 Multimodal Deception Detection Challenge | 2025 | ICCV 2025 Challenge | > 待核实 | arXiv preprint (cs.CV) / Challenge | 中 | ★★★★☆ | [9] | 首个跨域泛化多模态欺骗检测基准 |
| KnownLieBench | 2026 | - | > 待核实 | arXiv preprint (cs.CL) | 中 | ★★★★☆ | [11] | 知识验证的利益冲突欺骗基准，8域112 cases |
| Mobile-MMLU | 2025 | - | > 待核实 | arXiv preprint (cs.CL) | 中 | ★★★☆☆ | [13] | 移动端部署场景语言理解基准 |
| Video-MMLU | 2025 | - | > 待核实 | arXiv preprint (cs.CV) | 中 | ★★★☆☆ | [14] | 多学科讲座视频理解基准 |
| Risky-Bench | 2026 | - | > 待核实 | arXiv preprint (cs.AI) | 中 | ★★★★☆ | [25] | 真实生活辅助部署 Agentic 安全风险基准 |
| Foundation Model Transparency Index 2025 | 2025 | - | > 待核实 | arXiv preprint (cs.CY) | 中 | ★★★☆☆ | [3] | 基础模型透明度量化指数 |
| LongEval (CLEF 2025) | 2025 | CLEF 2025 | > 待核实 | arXiv preprint (cs.IR) | 中 | ★★★☆☆ | [6] | 纵向评测 IR 模型性能基准 |
| ELOQUENT 2025 Sensemaking Task | 2025 | ELOQUENT Lab | > 待核实 | arXiv preprint (cs.CL) | 低 | ★★☆☆☆ | [5] | LLM 作为教师/学生/评测者的感知任务 |
| CheckThat! 2024 OpenFact Adversarial Generation | 2024 | CheckThat! Lab | > 待核实 | arXiv preprint (cs.CL) | 低 | ★★☆☆☆ | [4] | 对抗性文本生成用于事实核查评测 |

> 待核实：AgentBench、MACHIAVELLI、Deception Eval、ToolBench、WebShop、ALFWorld 等经典基准最新版本、维护状态、榜单领跑者。

### A3. 主流开源评测框架与工程实践

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| Open Evaluation Agent | 2026 | - | > 待核实 | arXiv preprint (cs.AI) | 中 | ★★★★☆ | [20] | Evaluation Agent 范式，低成本可解释视觉生成评测 |
| Evaluation Agent (早期版本) | 2024 | - | > 待核实 | arXiv preprint (cs.CV) | 中 | ★★★☆☆ | [19] | 同一团队早期工作 |
| Code as Agent Harness | 2026 | - | > 待核实 | arXiv preprint (cs.CL) | 中 | ★★★★☆ | [21] | 代码作为 Agent 统一运行时基础设施 |
| AgentGuard | 2025 | - | > 待核实 | arXiv preprint (cs.AI) | 中 | ★★★☆☆ | [27] | 复用编排器进行工具编排安全评测 |
| LM-Evaluation-Harness | - | EleutherAI | > 待核实 | GitHub / 社区标准 | 高 | ★★★★★ | > 待核实 | 事实标准 LLM 评测框架，Agent 扩展进行中 |
| OpenCompass | - | Shanghai AI Lab | > 待核实 | GitHub / 官方文档 | 高 | ★★★★★ | > 待核实 | 国产主流综合评测平台，支持 Agent 任务 |
| HELM | - | Stanford CRFM | > 待核实 | 官网 / 论文 | 高 | ★★★★★ | > 待核实 | 全面基准套件，强调透明度与多维度评测 |

> 待核实：上述三大主流框架的 Agent 专用插件生态成熟度、CI/CD 集成案例、真机机器人评测适配器（ROS2/Isaac Sim/MuJoCo）开发进度。

---

## 参考来源

[1] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1  
[2] NTU-NPU System for Voice Privacy 2024 Challenge — http://arxiv.org/abs/2410.02371v1  
[3] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1  
[4] OpenFact at CheckThat! 2024: Combining Multiple Attack Methods for Effective Adversarial Text Generation — http://arxiv.org/abs/2409.02649v2  
[5] Overview of the Sensemaking Task at the ELOQUENT 2025 Lab: LLMs as Teachers, Students and Evaluators — http://arxiv.org/abs/2507.12143v1  
[6] LongEval at CLEF 2025: Longitudinal Evaluation of IR Model Performance — http://arxiv.org/abs/2503.08541v1  
[7] Discovery Opportunities with Gravitational Waves -- TASI 2024 Lecture Notes — http://arxiv.org/abs/2409.08956v1  
[8] Atmospheric entry and fragmentation of small asteroid 2024 BX1 — http://arxiv.org/abs/2403.00634v2  
[9] SVC 2025: the First Multimodal Deception Detection Challenge — http://arxiv.org/abs/2508.04129v1  
[10] Detecting Strategic Deception Using Linear Probes — http://arxiv.org/abs/2502.03407v1  
[11] Knowledge-Verified Emergent Deception in LLM Agents Under Conflicting Incentives — http://arxiv.org/abs/2608.26372v1  
[12] Deception Detection and Remote Physiological Monitoring: A Dataset and Baseline Experimental Results — http://arxiv.org/abs/2106.06583v1  
[13] Mobile-MMLU: A Mobile Intelligence Language Understanding Benchmark — http://arxiv.org/abs/2503.20786v1  
[14] Video-MMLU: A Massive Multi-Discipline Lecture Understanding Benchmark — http://arxiv.org/abs/2504.14693v2  
[15] Unmasking the Shadows of AI: Investigating Deceptive Capabilities in Large Language Models — http://arxiv.org/abs/2403.09676v1  
[16] AIn't Nothing But a Survey? Using Large Language Models for Coding German Open-Ended Survey Responses — http://arxiv.org/abs/2506.14634v3  
[17] A rich bounty of AGN in the 9 square degree Bootes survey — http://arxiv.org/abs/astro-ph/0611654v1  
[18] Application Layer Cyber Deception without Developer Interaction — http://arxiv.org/abs/2405.12852v1  
[19] Evaluation Agent: Efficient and Promptable Evaluation Framework for Visual Generative Models — http://arxiv.org/abs/2412.09645v3  
[20] Open Evaluation Agent: Efficient and Promptable Evaluation of Visual Generative Models — http://arxiv.org/abs/2608.09666v1  
[21] Code as Agent Harness — http://arxiv.org/abs/2605.18747v1  
[22] Position: Evaluation Scores Are Perishable Knowledge Claims — http://arxiv.org/abs/2607.26191v1  
[23] Safety in Self-Evolving Agents: A Survey — http://arxiv.org/abs/2610.00093v1  
[24] Point Transformer V3 Extreme: 1st Place Solution for 2024 Waymo Open Dataset Challenge — http://arxiv.org/abs/2407.15282v1  
[25] Risky-Bench: Evaluating Agentic Safety Risks in Real-World Life-Assist Deployments — http://arxiv.org/abs/2602.03100v2  
[26] AI Agents: Evolution, Architecture, and Real-World Applications — http://arxiv.org/abs/2503.12687v1  
[27] AgentGuard: Repurposing Agentic Orchestrator for Safety Evaluation of Tool Orchestration — http://arxiv.org/abs/2502.09809v1

---

*Generated by research-bot · topic=`agent-评测与安全能力基准欺骗与可纠正性` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`nvidia/nemotron-3-ultra-550b-a55b` · sources=27 · duration=343s · 2026-11-07T01:46:27+00:00*
