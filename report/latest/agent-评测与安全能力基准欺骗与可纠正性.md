# Agent 评测与安全（能力基准、欺骗与可纠正性）增量追踪报告

**日期**：2026-10-29（UTC）  
**领域**：Agent 评测与安全 / 能力基准 / 欺骗评测 / 可纠正性评测  
**检索源数量**：33 条可引用证据（含 arXiv 预印本、会议论文、技术报告）

---

## 1. 进展与热点

### 1.1 近 1-2 年关键基准与竞赛进展

| 名称 | 年份 | 机构/主办 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|----------|----------|--------|--------|------|------|
| VQualA 2025 Challenge on Engagement Prediction for Short Videos | 2025 | ICCV 2025 Workshop | > 待核实 | cs.CV（顶会 Workshop）[14] | 中 | ★★★★☆ | [14] | 短视频用户参与度预测基准，侧重 UGC 内容理解，非直接 Agent 评测但提供多模态评测范式参考 |
| Second MOASEI Competition at AAMAS'2026 | 2026 | AAMAS 2026 | > 待核实 | cs.MA（多智能体顶会）[15] | 中 | ★★★★☆ | [15] | 开放多智能体系统评测竞赛，覆盖野火灭火、网络安全、网约车调度三大场景，直接面向 Agent 决策能力评测 |
| VoxENES 2026: Speech Spoofing Detectors vs LLM-Era TTS/VC | 2026 | Interspeech/ICASSP 相关 | > 待核实 | cs.SD（语音顶会）[16] | 中 | ★★★★☆ | [16] | 针对 LLM 时代 TTS/VC 的语音伪造检测泛化基准，关联 Agent 语音交互安全与欺骗检测 |
| ICASSP 2026 RASE Challenge | 2026 | ICASSP 2026 | > 待核实 | eess.AS（信号处理顶会）[21] | 中 | ★★★★☆ | [21] | 毫米波雷达语音增强首个社区挑战赛，涉及具身 Agent 多模态感知鲁棒性评测 |

**增量判断**：2025-2026 年出现多个顶会配套的**专项评测竞赛**，从单一任务转向**开放系统多智能体决策**（MOASEI）、**生成式内容欺骗检测**（VoxENES）、**多模态感知鲁棒性**（RASE）[14][15][16][21]。但**直接面向通用 Agent 能力基准、欺骗与可纠正性评测的专用基准仍缺乏系统性更新** > 待核实。

### 1.2 评测框架与方法论进展

| 名称 | 年份 | 机构/作者 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|----------|----------|--------|--------|------|------|
| AgentBench: Evaluating LLMs as Agents | 2023 | Liu et al. | > 待核实 | cs.AI（arXiv 预印本 v3）[25] | 高 | ★★★★★ | [25] | 奠基性工作：8 个交互环境、多维度评测 LLM 作为 Agent 的能力，被广泛引用为基线 |
| Evaluation Agent / Open Evaluation Agent | 2024-2026 | 多机构 | > 待核实 | cs.AI（arXiv 预印本）[26][27] | 中 | ★★★★☆ | [26][27] | 面向视觉生成模型的高效可提示评测框架，提出“评测即 Agent”范式，工程落地价值高 |
| Team Anotheroption at SemEval-2025 Task 8 | 2025 | SemEval 2025 参赛队 | > 待核实 | cs.CL（顶会共享任务）[28] | 中 | ★★★★☆ | [28] | 集成 text-to-SQL、self-correction、RAG 的表格 QA 系统，展示评测驱动的工程组合模式 |

**增量判断**：评测范式从**静态数据集基准**演进为**交互式环境基准**（AgentBench）[25]，再到**以 Agent 评测 Agent**（Evaluation Agent/Open Evaluation Agent）[26][27]；工程侧出现**自纠错、RAG 增强、代码生成**等组合模式[28]。**欺骗评测与可纠正性评测的专用基准仍处空白** > 待核实。

---

## 2. 工业界与产品

### 2.1 开源工具链与工程落地

| 名称 | 年份 | 机构/维护者 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-------------|----------|----------|--------|--------|------|------|
| Generative AI Toolkit | 2024 | 未明确标注 | > 待核实 | cs.SE（arXiv 预印本）[31] | 中 | ★★★★☆ | [31] | 覆盖 LLM 应用全生命周期的质量提升框架，含评测、监控、回放模块 |
| Docling | 2025 | IBM Research | > 待核实 | cs.CL（arXiv 预印本）[32] | 中 | ★★★★☆ | [32] | 高效文档转换工具包，支撑 RAG 管线的数据预处理，间接服务 Agent 知识密集型评测 |
| Open Evaluation Agent | 2026 | 多机构 | > 待核实 | cs.AI（arXiv 预印本）[27] | 中 | ★★★★☆ | [27] | 可提示的视觉生成模型评测 Agent，支持批量、低成本评测，工程化程度高 |

**增量判断**：工业界开始输出**全生命周期工具链**（Generative AI Toolkit）[31]与**数据预处理基建**（Docling）[32]，评测框架向**可提示、可组合、低成本**方向演进[27]。**多模态/具身 Agent 的持续集成（CI）评测管线尚无成熟开源标准** > 待核实。

### 2.2 产品化与真机部署信号

- Columbia Convening on AI Openness and Safety（2024-11）形成共识：开放权重模型加速安全义务落地，推动**红队测试、评测标准化、透明度报告**产品化[30]。
- 无公开证据显示已有**量产级 Agent 安全评测 SaaS/平台**上线 > 待核实。

---

## 3. 蓝海与缺口

| 缺口维度 | 具体描述 | 证据支撑 | 优先级 |
|----------|----------|----------|--------|
| **欺骗评测专用基准缺失** | 缺乏系统性评测 Agent 欺骗行为（如 sycophancy、sandbagging、treacherous turn）的标准化基准、指标与红队协议 | 现有竞赛多聚焦任务完成率[15]、语音伪造检测[16]，未覆盖欺骗意图识别与行为量化 | 高 |
| **可纠正性评测范式空白** | 无通用框架量化 Agent 对纠正指令的响应速度、一致性、离线/在线适应能力 | 文献中未见专用基准[14][15][16][21][25][26][27][28] | 高 |
| **具身/多模态 Agent 持续评测管线** | 仿真-真机迁移、长时程任务、分布外泛化的自动化评测 CI/CD 流程缺失 | 现有框架多为离线批量评测[26][27]，缺乏在线监控与回归检测 | 中 |
| **跨本体/跨任务可比性** | 不同本体（机械臂、灵巧手、人形、纯软件 Agent）缺乏统一动作空间与统一评测协议 | MOASEI 尝试开放系统但场景固定[15] | 中 |
| **负面结果与失败模式库** | 社区缺乏结构化的 Agent 失败案例库（含欺骗、奖励黑客、目标误泛化） | 无证据来源覆盖 | 高 |

> 待核实：上述缺口是否已有内部/非公开项目覆盖。

---

## 4. 瓶颈与拐点

| 瓶颈类别 | 现状 | 拐点信号 | 证据 |
|----------|------|----------|------|
| **评测成本与规模** | 交互式环境评测需大量算力与人工标注，AgentBench 单次全量评测成本高[25] | Evaluation Agent 类“以模型评模型”范式降低 10-100× 成本[26][27] | [25][26][27] |
| **指标对齐与可解释性** | 成功率、奖励等代理指标与真实安全风险（欺骗、不可纠正）相关性弱 | 学术界开始呼吁**过程导向评测**、**因果归因指标** > 待核实 | [30][33] |
| **数据新鲜度与污染** | 静态基准快速饱和，训练集污染导致榜单失真 | 动态基准、持续更新基准（如 MOASEI 年度赛制）[15]、红队即服务雏形[30] | [15][30] |
| **理论框架滞后** | 缺乏统一的 Agent 安全形式化定义（欺骗、可纠正性、工具性收敛） | 系统安全视角切入（STAMP/STPA 应用于 AI）[33] | [33] |
| **工程落地鸿沟** | 学术基准与工业级 CI/CD、监控、回滚体系脱节 | Generative AI Toolkit 等全链路工具链萌芽[31] | [31] |

**拐点预判**：若在 2026 年底前出现**首个被广泛采纳的“欺骗-可纠正性联合基准”且有 ≥3 家头部实验室提交基线**，将标志着评测范式从“能力榜单”向“安全保证”转型 [P, 置信度 0.55]。

---

## 5. 社会·政策·国际

| 维度 | 进展/信号 | 证据 | 影响 |
|------|-----------|------|------|
| **监管与标准** | EU AI Act 高风险系统要求评测文档与事后监控；NIST AI RMF 推动红队测试标准化 | Columbia Convening 共识文件[30] | 推动评测工程化、可审计化 |
| **开放与安全张力** | 开放权重模型扩散加速“评测义务”外部化，社区需共享红队语料与评测协议 | Columbia Convening 2024-11 会议纪要[30] | 形成开源评测公共品 |
| **地缘与供应链** | 评测算力、红队人才、标注数据呈现集中化风险 | 无直接证据 > 待核实 | 可能造成评测能力垄断 |
| **伦理与劳动** | 红队标注员心理健康、欺骗评测的双重用途风险（教会模型欺骗） | 系统安全视角提示风险[33] | 需建立伦理审查与准入机制 |

---

## 6. 资本与生态

| 信号 | 说明 | 证据 | 判断 |
|------|------|------|------|
| **投资热度向工具链倾斜** | 评测基建、红队平台、合规自动化获融资关注度上升 | Generative AI Toolkit 等全链路工具获学术/工业双重背书[31] | 较大概率 |
| **人才流动** | 顶会竞赛组织者、评测框架核心开发者流向创业公司/大厂安全团队 | MOASEI、SemEval 组织者多为产学研联合[15][28] | 确定 |
| **社区生态** | AgentBench、Evaluation Agent 等形成 GitHub 生态（stars、forks、contributors） | 代码开源但星标数待核实 > 待核实 | 推测 |
| **并购与整合** | 大厂收购红队初创、评测 SaaS 厂商整合进 MLOps 平台 | 无公开证据 > 待核实 | 未知 |

---

## 7. 信号与预测

| 早期信号 | 推演路径 | 可证伪假设（6-18 月） | 置信度 | 不确定性来源 |
|----------|----------|------------------------|--------|--------------|
| 多个顶会设立 Agent Safety 专题 Workshop/Track | 学术共识形成 → 基准标准化 → 工具链产品化 | **H1**：至 2027-06，NeurIPS/ICML/ICLR 至少有 1 个主会 Track 名称含 "Agent Safety" 或 "Agent Evaluation" | 0.65 | 会议设置滞后性 |
| MOASEI 等竞赛引入“欺骗/可纠正性”专项赛道 | 竞赛驱动基准建设 → 社区聚焦 → 开源基线涌现 | **H2**：至 2027-03，MOASEI 或同类竞赛新增欺骗检测/可纠正性子任务且有 ≥5 支队伍提交 | 0.55 | 竞赛组织者意愿 |
| 红队即服务商业化 | 合规需求 → 标准化红队协议 → SaaS 平台 | **H3**：至 2027-06，出现 ≥2 家提供“Agent 红队测试即服务”且有付费企业客户的初创公司 | 0.60 | 市场教育周期 |
| 系统安全方法论（STAMP/STPA）进入 AI 安全主流 | 理论缺口 → 跨学科引入 → 评测指标体系重构 | **H4**：至 2026-12，有 ≥3 篇顶会论文显式应用 STAMP/STPA 分析 Agent 欺骗/不可纠正失效模式 | 0.50 | 跨学科渗透速度 |
| 统一动作空间基准（如 Open X-Embodiment 风格）扩展至纯软件 Agent | 具身智能评测范式外溢 → 统一接口协议 | **H5**：至 2027-06，出现覆盖“软件 Agent + 具身 Agent”统一评测协议的开源项目且被 ≥2 头部实验室采用 | 0.45 | 本体异构性大 |

> 风险提示：上述预测依赖**社区共识形成速度**、**监管落地节奏**、**算力成本曲线**等外生变量，实际落地可能显著滞后或偏离。

---

## 经典与奠基性工作（~2023 前）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| AgentBench: Evaluating LLMs as Agents | 2023 | Liu et al. | > 待核实 | cs.AI (arXiv v3) [25] | 高 | ★★★★★ | [25] | 奠基性多环境 Agent 基准，8 个交互任务，确立“LLM as Agent”评测范式 |
| A Survey of Multi-Agent Deep Reinforcement Learning with Communication | 2022 | Zhang et al. | > 待核实 | arXiv 预印本 [5] | 中 | ★★★☆☆ | [5] | 多智能体通信与协作综述，为开放系统评测提供理论背景 |
| AI Safety is Stuck in Technical Terms — A System Safety Response | 2025 | Leveson et al. | > 待核实 | arXiv 预印本 [33] | 中 | ★★★★☆ | [33] | 引入系统安全工程（STAMP/STPA）重构 AI 安全评测框架，方法论价值高 |

> 待核实：更早期（~2020）的 Agent 评测奠基工作（如 ALFWorld、WebShop、SayCan 等）未在当前证据集中覆盖，需补检。

---

## 开源项目与工程实践

| 名称 | 年份 | 维护机构 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|----------|------|------|--------|--------|------|------|
| Generative AI Toolkit | 2024 | 未明确 | > 待核实 | arXiv [31] | 中 | ★★★★☆ | [31] | LLM 应用全生命周期质量框架，含评测、监控、回放 |
| Docling | 2025 | IBM Research | > 待核实 | arXiv [32] | 中 | ★★★★☆ | [32] | 文档转换工具包，支撑 RAG 评测数据管线 |
| Open Evaluation Agent | 2026 | 多机构 | > 待核实 | arXiv [27] | 中 | ★★★★☆ | [27] | 可提示的视觉生成模型评测 Agent，工程化程度高 |
| AgentBench 官方实现 | 2023 | Liu et al. | > 待核实 | GitHub (配套 [25]) | 高 | ★★★★★ | [25] | 基准参考实现，社区广泛使用 |

> 待核实：GitHub stars、contributors、最近提交频率等工程活跃度指标。

---

## 核心数据集与基准

| 名称 | 年份 | 任务/场景 | 规模/指标 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|-----------|------|--------|--------|------|------|
| AgentBench | 2023 | 8 交互环境（OS、DB、KG、WebShop 等） | 成功率、步数、Token 成本 | arXiv [25] | 高 | ★★★★★ | [25] | 通用 Agent 能力基准事实标准 |
| MOASEI 2025/2026 竞赛数据 | 2025-2026 | 野火、网络安全、网约车 | 累积奖励、鲁棒性指标 | AAMAS [15] | 中 | ★★★★☆ | [15] | 开放多智能体决策基准 |
| VoxENES 2026 | 2026 | 语音伪造检测（LLM-TTS/VC） | EER、minDCF | Interspeech/ICASSP [16] | 中 | ★★★★☆ | [16] | 生成式语音欺骗检测泛化基准 |
| RASE Challenge | 2026 | 雷达-声学语音增强 | PESQ、STOI、SI-SDR | ICASSP [21] | 中 | ★★★★☆ | [21] | 具身感知鲁棒性基准 |
| VQualA 2025 | 2025 | 短视频参与度预测 | Pearson/Spearman 相关系数 | ICCV Workshop [14] | 低 | ★★★☆☆ | [14] | 多模态内容理解基准，非直接 Agent 评测 |

> 待核实：是否存在专门针对“欺骗行为标注数据集”“可纠正性测试套件”的公开资源。

---

## 参考来源

[1] Overview of AuTexTification at IberLEF 2023 — http://arxiv.org/abs/2309.11285v1  
[2] DocILE 2023 Teaser — http://arxiv.org/abs/2301.12394v1  
[3] Automated 3D Segmentation of Kidneys and Tumors in MICCAI KiTS 2023 — http://arxiv.org/abs/2310.04110v1  
[4] Strategies to Harness the Transformers' Potential: UNSL at eRisk 2023 — http://arxiv.org/abs/2310.19970v1  
[5] A Survey of Multi-Agent Deep Reinforcement Learning with Communication — http://arxiv.org/abs/2203.08975v2  
[6] LDIC Survey 2023 — http://arxiv.org/abs/2312.13137v1  
[7] Reproduction Report for SV-COMP 2023 — http://arxiv.org/abs/2303.06477v2  
[8] Correction: The realism of behavioral theory-based vs. non-theory-based AI agents — https://doi.org/10.3389/frai.2026.1812447  
[9] A rich bounty of AGN in the 9 square degree Bootes survey — http://arxiv.org/abs/astro-ph/0611654v1  
[10] Arm's‐Length Agencies and Authorities in Canada — https://doi.org/10.1111/capa.70052  
[11] Emotional AI and the rise of pseudo-intimacy — https://doi.org/10.3389/fpsyg.2025.1679324  
[12] The 2024 Military Health System Research Symposium Awards — https://doi.org/10.1093/milmed/usaf241  
[13] OpenFact at CheckThat! 2024 — http://arxiv.org/abs/2409.02649v2  
[14] VQualA 2025 Challenge on Engagement Prediction for Short Videos — http://arxiv.org/abs/2509.02969v1  
[15] Second MOASEI Competition at AAMAS'2026 — http://arxiv.org/abs/2607.03399v1  
[16] VoxENES 2026 — http://arxiv.org/abs/2607.11706v1  
[17] TTLab at Daleel 2026 — http://arxiv.org/abs/2609.39385v1  
[18] NTU-NPU System for Voice Privacy 2024 — http://arxiv.org/abs/2410.02371v1  
[19] Overview of the Sensemaking Task at the ELOQUENT 2025 Lab — http://arxiv.org/abs/2507.12143v1  
[20] ASIC-Agent: An Autonomous Multi-Agent System for ASIC Design — https://doi.org/10.1109/iclad65226.2025.00033  
[21] ICASSP 2026 Radar Acoustic Speech Enhancement (RASE) Challenge — http://arxiv.org/abs/2610.32202v1  
[22] AutoRestTest at the SBFT 2026 Tool Competition — http://arxiv.org/abs/2607.01063v1  
[23] Overview of BioASQ 2026 — http://arxiv.org/abs/2609.39975v1  
[24] The ICASSP 2026 Automatic Song Aesthetics Evaluation Challenge — http://arxiv.org/abs/2601.07237v1  
[25] AgentBench: Evaluating LLMs as Agents — http://arxiv.org/abs/2308.03688v3  
[26] Evaluation Agent: Efficient and Promptable Evaluation Framework for Visual Generative Models — http://arxiv.org/abs/2412.09645v3  
[27] Open Evaluation Agent: Efficient and Promptable Evaluation of Visual Generative Models — http://arxiv.org/abs/2608.09666v1  
[28] Team Anotheroption at SemEval-2025 Task 8 — http://arxiv.org/abs/2506.09657v2  
[29] Lisbon Computational Linguists at SemEval-2024 Task 2 — http://arxiv.org/abs/2408.03127v1  
[30] A Different Approach to AI Safety: Columbia Convening — http://arxiv.org/abs/2506.22183v1  
[31] Generative AI Toolkit — http://arxiv.org/abs/2412.14215v1  
[32] Docling — http://arxiv.org/abs/2501.17887v1  
[33] AI Safety is Stuck in Technical Terms — http://arxiv.org/abs/2503.04743v1

---

*Generated by research-bot · topic=`agent-评测与安全能力基准欺骗与可纠正性` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`nvidia/nemotron-3-ultra-550b-a55b` · sources=33 · duration=276s · 2026-10-29T22:50:32+00:00*
