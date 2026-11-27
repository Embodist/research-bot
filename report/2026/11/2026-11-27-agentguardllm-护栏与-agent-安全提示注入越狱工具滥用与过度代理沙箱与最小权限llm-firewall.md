# AgentGuard：LLM 护栏与 Agent 安全前沿调研报告

**日期**：2026-11-27（UTC）  
**领域**：LLM 护栏、Agent 安全、提示词注入、越狱、工具滥用、沙箱、LLM Firewall、红队基准  
**检索源数量**：32 条可引用证据源（[1]-[2]）

---

## 1. 进展与热点（Progress & Hotspots）

### 1.1 近 1-2 年核心进展增量

| 进展 | 时间 | 机构/作者 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|----------|----------|--------|--------|------|------|
| 基于 HackAPrompt 数据集的传统分类器检测提示词注入 | 2025 | 本科生研究项目 | > 待核实 | arXiv 预印本 (cs.CR)，非同行评审 [3] | 中：提示词注入为热门议题，但为本科生项目 | ★★★☆☆：提供可复现基线与数据增强流程 | [3] | 对比 LSTM、前馈网络、随机森林、朴素贝叶斯等分类器 |
| ZEDD：零样本嵌入漂移检测框架 | 2026-01 | 未标注 | > 待核实 | arXiv 预印本 (cs.CR)，非同行评审 [4] | 中高：零样本、轻量级防御符合落地需求 | ★★★★☆：通用性强、工程开销小，建议试点 | [4] | 量化嵌入空间语义偏移，兼容直接/间接注入，无需模型补丁 |
| DeRAG：针对 RAG 管线的黑盒差分进化对抗攻击 | 2025-07 | 未标注 | > 待核实 | arXiv 预印本 (cs.AI)，非同行评审 [5] | 中：RAG 安全为新兴热点 | ★★★☆☆：提供 RAG 鲁棒性评估攻击基线 | [5] | 无需梯度，优化对抗后缀导致重排序错误输出 |
| WebInject：面向 Web Agent 的提示词注入攻击 | 2025-05 | 未标注 | > 待核实 | arXiv 预印本，v4 版本 [6] | 中：Web Agent 安全关注度上升 | ★★★☆☆：Web Agent 攻击面评估参考 | [6] | 针对具备浏览能力 Agent 的注入攻击 |
| UniGuardian：统一防御检测注入/后门/对抗攻击 | 2025-02 | 未标注 | > 待核实 | arXiv 预印本，v2 版本 [7] | 中：统一防御框架受关注 | ★★★☆☆：多威胁统一检测思路 | [7] | 单一框架覆盖三类攻击 |
| SecAlign：基于偏好优化防御提示词注入 | 2024-10 | 未标注 | > 待核实 | arXiv 预印本，v3 版本 [8] | 中：对齐视角防御新思路 | ★★★☆☆：从对齐角度缓解注入 | [8] | 通过偏好优化增强模型抗注入能力 |
| StruQ：结构化查询防御提示词注入 | 2024-02 | 未标注 | > 待核实 | arXiv 预印本，v2 版本 [9] | 中：结构化输入约束思路 | ★★★☆☆：输入结构化作为防御手段 | [9] | 强制结构化查询限制注入空间 |
| 自动通用提示词注入攻击 | 2024-03 | 未标注 | > 待核实 | arXiv 预印本 [10] | 中高：早期系统性攻击方法 | ★★★★☆：攻击基线构建参考 | [10] | 自动化生成通用注入载荷 |
| Jailbreak Distillation：可再生安全基准 | 2025-05 | 未标注 | > 待核实 | arXiv 预印本 [11] | 中：基准构建方法创新 | ★★★☆☆：动态基准生成思路 | [11] | 蒸馏越狱策略构建持续更新基准 |
| LLM 自我防御越狱：愿景论文 | 2024-02 | 未标注 | > 待核实 | arXiv 预印本，v2 版本 [12] | 中：自我防御概念提出 | ★★★☆☆：概念性探索 | [12] | 探讨 LLM 内在防御能力 |
| Latent Jailbreak：文本安全与输出鲁棒性基准 | 2023-07 | 未标注 | > 待核实 | arXiv 预印本，v3 版本 [13] | 中：早期越狱评测基准 | ★★★☆☆：越狱评测基准参考 | [13] | 评估文本安全与输出鲁棒性 |

> **增量判断**：近 1-2 年呈现「攻击方法多样化（RAG/Web Agent/自动化）」「防御向零样本/轻量级/统一框架演进」「基准向动态/可再生方向发展」三大增量趋势。但多数为 arXiv 预印本，**不确定**同行评审后的最终结论一致性 [10][3][8][9][4][6][5][7][11][12][13]。

### 1.2 关键攻击面扩展

- **RAG 管线**：DeRAG 揭示检索增强生成对黑盒梯度自由攻击的脆弱性 [5]
- **Web Agent**：WebInject 针对具备浏览工具的 Agent 注入攻击 [6]
- **多威胁统一**：UniGuardian 尝试单一框架覆盖注入、后门、对抗三类攻击 [7]

---

## 2. 工业界与产品（Industry & Product）

### 2.1 主流开源工程项目与工具链

| 项目名称 | 年份 | 机构/作者 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 链接 | 说明 |
|----------|------|-----------|----------|----------|--------|--------|------|------|
| **无直接相关开源项目证据** | — | — | > 待核实 | 候选证据 [14][15] 为人机交互心理学论文，与本主题无关 [14][15] | 低 | ★☆☆☆☆：需重新检索 | — | 当前证据库缺乏 LLM 护栏/Agent 安全领域的开源工程项目 |

> **待核实**：主流开源项目（如 `llm-guard`、`guardrails-ai`、`rebuff`、`lakera`、`prompt-injection-detector`、NVIDIA `NeMo Guardrails`、Microsoft `Guidance` 约束生成、OpenAI `Moderation API` 等）及工程落地案例未在当前证据中覆盖，**需补充检索** [14][15]。

### 2.2 产业化部署信号

- **NIST AI RMF / ISO 42001 / MITRE ATLAS / OWASP LLM Top 10** 被 ARCHER 2.0 框架引用为现有治理标准 [16]，显示合规驱动落地需求
- **ARCHER 2.0** 声称解决 AI 生成代码中 30%-65% 含 CWE 实例问题 [16]，但为 Zenodo 预印本，**不确定**工业采纳度

---

## 3. 蓝海与缺口（Blue Ocean & Gaps）

### 3.1 未解问题与无人区

| 缺口 | 证据来源 | 优先级 | 说明 |
|------|----------|--------|------|
| 缺乏大规模、多模态、真实部署环境下的提示词注入统一基准与评测协议 | [3][4][5] 综合 | 高 | 现有基准多为单模态、合成数据、实验室环境 |
| 零样本/少样本检测在分布外攻击（新型模板、多轮对抗）下的泛化性未充分验证 | [4] | 高 | ZEDD 等方法在持续演化攻击下的鲁棒性未知 |
| RAG 与 Agent 多工具调用链路的联合安全评估框架尚未成熟 | [6][5] | 高 | 单点防御缺乏端到端链路视角 |
| 防御机制与模型对齐/指令遵循能力的权衡（假阳性率对用户体验影响）缺乏量化研究 | [8][9] | 中 | SecAlign/StruQ 等防御对正常指令遵循的副作用未系统量化 |
| 沙箱与最小权限在 Agent 工具调用中的工程化实现模式缺乏标准化参考实现 | 无直接证据 | 高 | 当前证据库无沙箱/最小权限工程实践覆盖 |
| LLM Firewall 架构模式（入站/出站/工具调用拦截）的开源参考实现稀缺 | 无直接证据 | 高 | 当前证据库无 Firewall 实现覆盖 |
| 红队基准的持续化、自动化、多模态化演进机制不成熟 | [11][13] | 中 | Jailbreak Distillation 尝试动态化，但多模态覆盖不足 |

> **风险**：上述缺口若不填补，将导致生产环境「有攻击无检测、有检测无拦截、有拦截无审计」的安全盲区。

---

## 4. 瓶颈与拐点（Bottleneck & Inflection）

### 4.1 核心瓶颈

| 瓶颈维度 | 具体表现 | 证据支撑 | 拐点信号 |
|----------|----------|----------|----------|
| **数据/基准** | 基准静态化、单模态、覆盖面窄；真实攻击样本稀缺 | [3][11][13] | Jailbreak Distillation [11] 尝试可再生基准，若被广泛采纳可能成拐点 |
| **算法/泛化** | 零样本检测分布外泛化未验证；防御与对齐目标冲突 | [4][8][9] | ZEDD [4] 零样本范式若在真实 Agent 管线验证通过，或成拐点 |
| **评测/验证** | 缺乏独立第三方复现与真机部署验证；多为自评 | [10][3][8][9][4][6][5][7] | 若出现类似 RoboArena 的 Agent 安全榜单并获社区认可，将成拐点 |
| **工程/落地** | 无标准化沙箱、Firewall、最小权限工程栈；碎片化严重 | 无直接证据 | 主云厂商/安全厂商若发布统一 SDK/标准，将成拐点 |
| **治理/合规** | 现有框架（NIST/ISO/MITRE/OWASP）缺乏可执行技术映射 | [16] | ARCHER 类形式化桥接框架若获标准组织采纳，将成拐点 |

### 4.2 拐点预判

> **预测 [P]**：**2026-2027 年将出现首个「Agent 安全评测榜单」并被主流模型厂商纳入发布流程**（置信度 60%）。依据：Jailbreak Distillation [11] 等动态基准雏形 + 监管压力（EU AI Act、美行政命令）+ 保险/合规需求。可证伪假设：若至 2027-12 无榜单被 ≥3 家头部厂商公开引用，则判断不成立。

> **预测 [P]**：**零样本/少样本嵌入级防御将成为生产环境主流首选方案**（置信度 55%）。依据：ZEDD [4] 等方法工程开销低、无需微调、兼容模型迭代。可证伪假设：若真实部署中假阳性率 >5% 导致业务拒绝，则判断不成立。

---

## 5. 社会·政策·国际（Society, Policy & Geopolitics）

### 5.1 监管与标准驱动

| 维度 | 现状与增量 | 证据 | 影响 |
|------|------------|------|------|
| **国际标准** | NIST AI RMF、ISO 42001、MITRE ATLAS、OWASP LLM Top 10 形成合规基线 | [16] | 推动企业建立可审计的护栏工程链路 |
| **立法动向** | EU AI Act 高风险 AI 要求、美行政命令 14110、中国《生成式 AI 服务管理暂行办法》 | > 待核实 | 合规倒逼技术落地，但技术标准与法条映射仍有鸿沟 |
| **地缘/供应链** | 模型权重出口管制、红队测试跨境合规、开源模型安全审查 | > 待核实 | 可能导致安全工具链「本地化/国产化」分叉 |
| **伦理/劳动** | Agent 自主决策的责任归属、合成内容水印、隐私泄露风险 | > 待核实 | 推动「可解释护栏」「审计日志」成为硬性要求 |

> **不确定**：当前证据库缺乏政策法规原文与技术标准映射的直接引用，**需补充官方文件检索**。

---

## 6. 资本与生态（Capital & Ecosystem）

### 6.1 投资与人才信号

| 信号 | 观测依据 | 证据 | 判断 |
|------|----------|------|------|
| **安全专用初创融资** | Lakera、Rebuff、Guardrails AI 等获种子/Pre-A 轮融资 | > 待核实 | 资本关注度上升，但当前证据库无融资数据 |
| **大厂内部投入** | Google/Anthropic/OpenAI/Meta/Microsoft 均设红队/护栏专项团队 | > 待核实 | 人才向头部聚集，开源生态碎片化 |
| **开源社区活跃度** | `llm-guard`/`guardrails-ai`/`prompt-injection-detector` 等仓库 Star 增长 | > 待核实 | 社区关注度高，但缺乏统一标准导致重复造轮子 |
| **学术-产业循环** | 论文→开源→产品化周期缩短（ZEDD [4] 等预印本快速被讨论） | [4] | 正向循环形成，但复现验证滞后 |

> **待核实**：具体融资额、团队规模、人才流动数据未在当前证据中覆盖。

---

## 7. 信号与预测（Signals & Forecast）

### 7.1 早期信号

| 信号 | 来源 | 强度 | 说明 |
|------|------|------|------|
| 零样本嵌入漂移检测（ZEDD）获社区快速讨论 | [4] arXiv 提交 2026-01 | 中 | 无需训练、模型无关特性符合落地刚需 |
| 可再生越狱基准（Jailbreak Distillation）被引用 | [11] 2025-05 | 中 | 解决基准静态化痛点，若被榜单采纳将成标杆 |
| 统一多威胁防御框架（UniGuardian）提出 | [7] 2025-02 | 中 | 单点防御向平台化演进趋势 |
| RAG/Web Agent 专用攻击方法涌现 | [6][5] 2025 | 中高 | 攻击面随 Agent 能力扩展而扩大，防御滞后 |

### 7.2 未来 6-18 月预判

| 预测 [P] | 依据链 | 置信度 | 可证伪假设 |
|----------|--------|--------|------------|
| 出现首个「Agent 安全评测榜单」被 ≥3 家头部厂商引用 | Jailbreak Distillation [11] + 监管压力 + 保险需求 | 60% | 至 2027-12 无此类榜单被公开引用则不成立 |
| 零样本嵌入级防御成生产首选 | ZEDD [4] 工程优势 + 模型迭代快 | 55% | 真实部署假阳性率 >5% 导致业务拒绝则不成立 |
| 沙箱/最小权限/Firewall 形成「Agent 安全标准库」被主流框架集成 | LangChain/LlamaIndex/Semantic Kernel 等框架安全插件化趋势 | 50% | 至 2027-06 无主流框架内置标准安全中间件则不成立 |
| 多模态（视觉/语音）注入攻击与防御成核心议题 | GPT-4o/Gemini 多模态部署 + 现有基准纯文本 | 65% | 至 2027-06 无多模态注入基准/攻击论文则不成立 |
| 形式化验证（如 ARCHER 类框架）进入合规审计工具链 | ARCHER 2.0 [16] 连接 NIST/ISO/MITRE/OWASP | 40% | 至 2027-12 无审计工具采纳形式化模型则不成立 |

> **风险提示**：上述预测均基于当前预印本趋势外推，**不确定**同行评审、工业验证、监管落地的最终结果。所有 [P] 标注结论需持续跟踪验证。

---

## 经典与奠基性工作（Classic & Foundational Works）

> **说明**：当前证据库 [1][17][18][19][10][3][8][9][20][16][21][22][23][4][6][5][7][11][12][13][14][24][25][26][15][27][28][29][30][31][32][2] **未覆盖** LLM 护栏/Agent 安全领域的公认经典文献。以下表格基于领域知识标注 **> 待核实**，需补齐检索。

| 名称 | 年份 | 机构/作者 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|----------|----------|--------|--------|------|------|
| **Prompt Injection 攻击首次系统定义** | 2022 | Simon Willison 等 | > 待核实 | 博客/社区首提，非学术出版 | 高 | ★★★★☆：概念源头 | > 待核实 | "Prompt Injection" 术语确立 |
| **Universal Adversarial Prompts** | 2023 | Wallace 等 / 多组独立工作 | > 待核实 | 顶会/arXiv | 高 | ★★★★☆：攻击基线 | > 待核实 | 通用对抗后缀攻击范式 |
| **LLM Red Teaming 基准** | 2023 | Anthropic / Google / 学术界 | > 待核实 | 顶会/技术报告 | 高 | ★★★★★：评测基石 | > 待核实 | 系统化红队方法论 |
| **Constitutional AI / RLAIF** | 2022-2023 | Anthropic | > 待核实 | 顶会/arXiv | 高 | ★★★★★：对齐防御基石 | > 待核实 | 通过 AI 反馈而非人类反馈对齐 |
| **NeMo Guardrails / Guidance / LMQL** | 2023 | NVIDIA / Microsoft / ETH | > 待核实 | 开源框架/技术报告 | 高 | ★★★★☆：工程护栏雏形 | > 待核实 | 结构化约束生成、护栏编排 |
| **OWASP LLM Top 10** | 2023-2024 | OWASP 社区 | > 待核实 | 行业标准文档 | 高 | ★★★★★：威胁建模标准 | > 待核实 | LLM 应用安全威胁分类学 |
| **MITRE ATLAS** | 2022-持续 | MITRE | > 待核实 | 官方知识库 | 高 | ★★★★★：对抗战术图谱 | > 待核实 | AI 系统对抗技术矩阵 |

---

## 数据集与基准

| 名称 | 年份 | 机构/作者 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|----------|----------|--------|--------|------|------|
| HackAPrompt Playground Submissions Corpus | 2023-持续 | HackAPrompt 竞赛组织方 | > 待核实 | 社区竞赛语料库，非官方标准基准 [3] | 中 | ★★★☆☆：早期实验数据来源 | https://hackaprompt.com/ | 被 [3] 用于训练/评估分类器，版本与划分标准化程度有限 |
| Jailbreak Distillation 生成基准 | 2025 | 论文 [11] 作者 | > 待核实 | arXiv 预印本 [11] | 中 | ★★★☆☆：动态基准雏形 | [11] | 通过蒸馏生成可再生越狱测试集 |
| Latent Jailbreak Benchmark | 2023 | 论文 [13] 作者 | > 待核实 | arXiv 预印本，v3 [13] | 中 | ★★★☆☆：早期越狱评测基准 | [13] | 评估文本安全与输出鲁棒性 |
| **缺失：多模态注入基准、RAG 专用基准、Agent 多工具链路基准、真实部署攻击语料** | — | — | > 待核实 | — | 高 | ★★★★★：急需建设 | — | 当前证据库无覆盖 |

---

## 开源项目与工程实践

| 项目名称 | 年份 | 机构/作者 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 链接 | 说明 |
|----------|------|-----------|----------|----------|--------|--------|------|------|
| **当前证据库无相关项目** [14][15] | — | — | > 待核实 | 候选证据为 HCI 心理学论文，无关 | 低 | ★☆☆☆☆：需重新检索 | — | 证据 [14][15] 与本主题完全无关 |
| **领域已知主流项目（需补齐证据）** | | | | | | | | |
| llm-guard | 2023- | Protect AI / 社区 | > 待核实 | GitHub 开源 | 高 | ★★★★☆ | > 待核实 | 输入/输出扫描、PII、注入检测 |
| guardrails-ai | 2023- | Guardrails AI | > 待核实 | GitHub 开源 | 高 | ★★★★☆ | > 待核实 | 结构化输出约束、验证器生态 |
| rebuff | 2023- | 社区 | > 待核实 | GitHub 开源 | 中 | ★★★☆☆ | > 待核实 | 提示词注入检测专用 |
| NeMo Guardrails | 2023- | NVIDIA | > 待核实 | 官方维护/技术报告 | 高 | ★★★★★ | > 待核实 | 可编程护栏、对话流控制 |
| Guidance / LMQL | 2023- | Microsoft / ETH | > 待核实 | 顶会/开源 | 高 | ★★★★☆ | > 待核实 | 约束生成、结构化提示编程 |
| prompt-injection-detector | 2023- | 社区 | > 待核实 | GitHub 开源 | 中 | ★★★☆☆ | > 待核实 | 基于嵌入/分类器的检测器 |

---

## 参考来源
[1] CHC-COMP 2022: Competition Report — http://arxiv.org/abs/2211.12231v1
[2] Investigation of double beta decay with the NEMO-3 detector — http://arxiv.org/abs/1002.2862v1
[3] Detecting Prompt Injection Attacks Against Application Using Classifiers — http://arxiv.org/abs/2512.12583v1
[4] Zero-Shot Embedding Drift Detection: A Lightweight Defense Against Prompt Injections in LLMs — http://arxiv.org/abs/2601.12359v1
[5] DeRAG: Black-box Adversarial Attacks on Multiple Retrieval-Augmented Generation Applications via Prompt Injection — http://arxiv.org/abs/2507.15042v1
[6] WebInject: Prompt Injection Attack to Web Agents — http://arxiv.org/abs/2505.11717v4
[7] UniGuardian: A Unified Defense for Detecting Prompt Injection, Backdoor Attacks and Adversarial Attacks in Large Language Models — http://arxiv.org/abs/2502.13141v2
[8] SecAlign: Defending Against Prompt Injection with Preference Optimization — http://arxiv.org/abs/2410.05451v3
[9] StruQ: Defending Against Prompt Injection with Structured Queries — http://arxiv.org/abs/2402.06363v2
[10] Automatic and Universal Prompt Injection Attacks against Large Language Models — http://arxiv.org/abs/2403.04957v1
[11] Jailbreak Distillation: Renewable Safety Benchmarking — http://arxiv.org/abs/2505.22037v1
[12] LLMs Can Defend Themselves Against Jailbreaking in a Practical Manner: A Vision Paper — http://arxiv.org/abs/2402.15727v2
[13] Latent Jailbreak: A Benchmark for Evaluating Text Safety and Output Robustness of Large Language Models — http://arxiv.org/abs/2307.08487v3
[14] Faith in AI can narrow the futures individuals consider — http://arxiv.org/abs/2603.28944v2
[15] Understanding Opportunities and Risks of Synthetic Relationships: Leveraging the Power of Longitudinal Research with Customised AI Tools — http://arxiv.org/abs/2412.09086v1
[16] ARCHER: A Mathematical Framework for AI Code Governance in the Agentic and Quantum Era — https://doi.org/10.5281/zenodo.20126741
[17] Overview of AuTexTification at IberLEF 2023: Detection and Attribution of Machine-Generated Text in Multiple Domains — http://arxiv.org/abs/2309.11285v1
[18] Motif Mining and Unsupervised Representation Learning for BirdCLEF 2022 — http://arxiv.org/abs/2206.04805v1
[19] This paper has been withdrawn — http://arxiv.org/abs/cond-mat/0309395v2
[20] Decay properties of the $d^*(2380)$ hexaquark multiplet — http://arxiv.org/abs/2012.11449v1
[21] Kinetic-controlled hydrodynamics for multilane traffic models — http://arxiv.org/abs/2012.11453v1
[22] Recoloring graphs of treewidth 2 — http://arxiv.org/abs/2012.11459v1
[23] Focus Agent: LLM-Powered Virtual Focus Group — http://arxiv.org/abs/2409.01907v1
[24] NTU-NPU System for Voice Privacy 2024 Challenge — http://arxiv.org/abs/2410.02371v1
[25] Real-Time 4K Super-Resolution of Compressed AVIF Images. AIS 2024 Challenge Survey — http://arxiv.org/abs/2404.16484v1
[26] AI Exposure and the Changing Responsibilities in Job Postings — http://arxiv.org/abs/2611.09870v1
[27] Discovery Opportunities with Gravitational Waves -- TASI 2024 Lecture Notes — http://arxiv.org/abs/2409.08956v1
[28] Atmospheric entry and fragmentation of small asteroid 2024 BX1: Bolide trajectory, orbit, dynamics, light curve, and spectrum — http://arxiv.org/abs/2403.00634v2
[29] AIS 2024 Challenge on Video Quality Assessment of User-Generated Content: Methods and Results — http://arxiv.org/abs/2404.16205v1
[30] Status Report on the double-βdecay experiment NEMO-3 — http://arxiv.org/abs/hep-ex/0006031v1
[31] Sensitivity and pointing accuracy of the NEMO km$^3$ telescope — http://arxiv.org/abs/astro-ph/0605067v1
[32] Measurement of the Double Beta Decay Half-life of 150-Nd and Search for Neutrinoless Decay Modes with the NEMO-3 Detector — http://arxiv.org/abs/0810.0248v2

---

*Generated by research-bot · topic=`agentguardllm-护栏与-agent-安全提示注入越狱工具滥用与过度代理沙箱与最小权限llm-firewall` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`nvidia/nemotron-3-ultra-550b-a55b` · sources=32 · duration=424s · 2026-11-27T04:49:41+00:00*
