# AI 治理与监管（政策、法规与标准）增量调研报告

**日期**：2026-11-25（UTC）  
**领域**：AI Governance & Regulation（政策、法规与标准）  
**检索源数量**：32 条可引用证据源（其中高度相关 14 条）  
**方法论**：frontier-watch + deep-research + evidence-grading

---

## 1. 进展与热点（Progress & Hotspots）

### 1.1 核心立法与标准里程碑（近 1-2 年增量）

| 进展 | 时间 | 机构/来源 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 说明 |
|------|------|-----------|----------|----------|--------|--------|------|
| **EU AI Act (2024/1689) 正式通过并进入实施阶段** | 2024 | 欧盟立法机构 | 被引 7 次 [1] | 同行评审期刊 *AI Magazine* (AAAI 官方刊) [1] | 高 | ★★★★★ | 全球首部全面 AI 法律，跨学科落地成核心挑战 [1] |
| **ISO/IEC 42001（AI 管理体系标准）开始进入工程落地与金融量化工具链** | 2025 | ISO/IEC JTC1 / 学术探索 | arXiv 预印本，引用数待核实 [2] | arXiv cs.CY 预印本 [2] | 中 | ★★★☆☆ | 首次被整合进 AI 投资风险量化框架（RAID），标志标准向合规工程化延伸 [2] |
| **FMTI 2025（第三版）发布：覆盖中美主流厂商，透明度整体倒退** | 2025-12 | Stanford CRFM / HAI | arXiv 预印本，社区关注度高 [3] | arXiv cs.AI 预印本，作者含 Percy Liang、Rishi Bommasani 等 [3] | 高 | ★★★★★ | 平均分 40/100（2024 年 58），新增数据获取/使用数据/监控指标，覆盖阿里巴巴、DeepSeek、xAI [3] |
| **AGILE Index 2025 发布：首个系统性跨国 AI 治理评价指数** | 2025-07 | 国际研究团队 | arXiv 预印本 v2 [4] | arXiv cs.CY 预印本 [4] | 中高 | ★★★★☆ | 追踪 2024 年多边框架强化与国家监管激增，填补系统性跟踪空白 [4] |
| **五层 AI 治理框架提出：连接法规-标准-认证-合规-执行** | 2025-09 | 学术团队 | arXiv 预印本 [5] | arXiv cs.CY 预印本 [5] | 中 | ★★★★☆ | 解决“高层原则到合格机制”断层，提供结构化落地路径 [5] |

> **增量判断**：2024-2025 年标志性增量是 **“立法从提案转入实施”（EU AI Act）**、**“标准从文本转入工程工具链”（ISO 42001 → RAID 框架）**、**“评价体系从单一维度转向全生命周期跨国横向对比”（FMTI/AGILE）**。

### 1.2 工程化合规工具链早期探索

- **OSCAL (NIST) 被提议为 AI 合规证据的机器可读交换格式**，填补 EU AI Act、ISO 42001、NIST AI RMF 缺乏可执行格式的空白；提出 16 个属性扩展覆盖生命周期、执行语义、风险追溯，并给出三层 Compliance-as-Code 架构（策略/证据/执行） [6]  
  - 热度：arXiv 2026-04 预印本，引用待核实  
  - 权威：arXiv cs.CY 预印本  
  - 关注度：中（针对高风险 AI 合规工程化痛点的直接回应）  
  - 推荐度：★★★★☆

- **Generative AI Toolkit**：面向 LLM 应用全生命周期质量提升的框架，覆盖开发、评测、部署、监控 [7]  
  - 热度/权威/关注度：arXiv 2024-12 预印本，待核实  
  - 推荐度：★★★☆☆

### 1.3 红队/安全评测基准演进

- **Mind the Gap (2025)**：对比模型级 vs Agentic 级红队，引入 Action-Graph 可观测性，在 GPT-OSS-20B 上验证 [8]  
- **Learning diverse attacks for robust red-teaming (2024)**：多样化攻击生成用于安全微调 [9]  
- **Red Teaming at Scale for Math Hallucinations (2024)**：大规模数学幻觉红队 [10]  
  > 以上三项均为 arXiv 预印本，属于“评测基准工程化”早期信号，尚无独立第三方复现报告。

---

## 2. 工业界与产品（Industry & Product）

### 2.1 主流模型厂商透明度实况（FMTI 2025 实测）

| 厂商 | FMTI 2025 得分 | 关键不透明维度 | 来源 |
|------|----------------|----------------|------|
| IBM | 表现突出（具体分值待核实） | — | [3] |
| 阿里巴巴 | 首次被纳入评估 | 训练数据、算力、部署后影响 | [3] |
| DeepSeek | 首次被纳入评估 | 训练数据、算力、部署后影响 | [3] |
| xAI | 首次被纳入评估 | 训练数据、算力、部署后影响 | [3] |
| **整体均值** | **40/100**（2024 年 58） | 训练数据/算力/部署后影响最不透明 | [3] |

> **增量**：FMTI 2025 首次将中国头部厂商纳入同一评价体系，揭示**透明度整体倒退**趋势，且新增指标直指全生命周期（数据获取、使用数据、监控）[3]。

### 2.2 合规工具与认证早期产品化信号

- **ISO 42001 认证实践**：已进入 AI 投资风险量化框架（RAID），但早期认证案例、审核方法论成熟度、与 EU AI Act/NIST AI RMF 映射关系在公开文献中**缺失** [2]  
- **EU AI Act 高风险 AI 合格评估、通用模型义务、监管沙箱**的落地细则与跨成员国协调机制在候选证据中**未覆盖** [1]  
- **AI 在 GRC（治理、风险、合规）领域的应用研究**：调研显示潜力大但落地案例少 [11]

> 待核实：主要云厂商（Microsoft、Google、AWS）、专业合规 SaaS（OneTrust、TrustArc 等）是否已推出基于 ISO 42001/EU AI Act 的商业化合规套件。

---

## 3. 蓝海与缺口（Blue Ocean & Gaps）

| 蓝海/缺口 | 说明 | 证据支撑 | 优先级 |
|-----------|------|----------|--------|
| **跨司法管辖区合规互认机制** | EU-US AI 协作、全球峰会成果、ISO 42001 与 EU AI Act/NIST AI RMF 的正式映射表均缺乏公开权威版本 | [1][2][4] | ★★★★★ |
| **全生命周期合规证据的机器可读标准落地** | OSCAL 扩展提案虽出现 [6]，但工具链、CI/CD 集成、审计员接受度均处早期 | [6] | ★★★★☆ |
| **基础模型透明度指标与监管条文的对齐度量** | FMTI 指标 vs EU AI Act 第 53 条、美行政命令报告义务的映射表缺失 | [3][1] | ★★★★☆ |
| **AI 事件治理的开放问题体系化** | 事件定义、报告门槛、跨境通报、责任归因均无共识标准 | [12] | ★★★★★ |
| **核能/医疗等高风险垂域的 AI 监管观测站** | 核领域 AI Observatory 概念提出 [13]，但医疗器械（EU MDR + AI Act 交互）[14]、自动驾驶等垂域缺乏同类机制 | [13][14] | ★★★★☆ |
| **非西方视角的包容性/可及性治理研究** | Global South 无障碍实践研究 [15] 提示治理框架存在文化/语言盲区 | [15] | ★★★☆☆ |
| **可复现性作为治理新前沿** | 复现性被提出为治理新边疆 [16]，但基准、工具、激励机制均缺失 | [16] | ★★★★☆ |

> **核心洞察**：当前治理工具链多停留在“原则/标准文本”层，**“可执行证据格式”“跨域互认映射”“垂域观测站”“事件治理标准”**是工程落地与国际协同的最大蓝海。

---

## 4. 瓶颈与拐点（Bottleneck & Inflection）

### 4.1 核心瓶颈

| 瓶颈 | 表现 | 证据 | 严重度 |
|------|------|------|--------|
| **原则到代码的“最后一公里”断层** | 法规/标准缺乏机器可读执行格式，合规靠人工文档 | [5][6] | 高 |
| **透明度倒退与信息不对称加剧** | FMTI 得分下降 18 分，头部厂商核心资产（数据/算力/部署后）不透明 | [3] | 高 |
| **跨域定义不一致** | “高风险 AI”“基础模型”“系统性风险”在 EU/US/ISO/中文语境下定义不同 | [1][4][3] | 高 |
| **审计/认证人才与方法论短缺** | ISO 42001 审核员认证体系、红队标准化、事件调查取证规范均缺失 | [2][12][8] | 中高 |
| **地缘政治碎片化导致合规成本指数级上升** | 多司法管辖区并行合规、数据本地化、出口管制叠加 | [4][17] | 高 |

### 4.2 拐点信号

| 信号 | 说明 | 判断依据 | 置信度 |
|------|------|----------|--------|
| **Compliance-as-Code 从概念走向原型** | OSCAL 扩展 [6]、五层框架 [5]、RAID 框架 [2] 同期出现 | 多独立来源在 2025-2026 窗口期汇聚 | 中高 |
| **透明度指数成为“软法”基准被政策引用** | FMTI 连续三年、AGILE Index 首发，被学术/政策讨论高频引用 | [3][4] | 高 |
| **核类比进入主流治理话语** | Nuclear Analogy 论文 [17] 系统梳理许可/监管/责任类比，可能推动“许可制”立法提案 | [17] | 中 |
| **红队从模型级向 Agentic 级跃迁** | Action-Graph 可观测性 [8]、多样化攻击生成 [9] 标志评测范式升级 | [8][9] | 中 |

> **拐点预判**：若 2026 年内出现 **首个基于 OSCAL 的跨司法管辖区合规互认试点**，或 **ISO 42001 认证数量突破 1000 家**，将标志工程化落地拐点到来。

---

## 5. 社会·政策·国际（Society, Policy & Geopolitics）

### 5.1 多边框架与国家监管并行加速（2024-2025）

- **多边层面**：G7 广岛进程、OECD AI 原则更新、UN 全球数字契约、全球 AI 安全峰会（首尔/巴黎）形成“软法密集期” [4]  
- **国家层面**：EU AI Act 生效 [1]；美国联邦行政命令（EO 14110）推动 NIST AI RMF 与机构落地；中国《生成式 AI 服务管理暂行办法》实施、“人工智能安全治理框架”发布（候选证据中**缺失原文**，需补核）  
- **标准层面**：ISO/IEC 42001:2023 发布，ISO/IEC 23894（风险管理）、ISO/IEC 42006（审计要求）配套推进 [2][4]

### 5.2 地缘政治与供应链冲突外溢至治理

- **出口管制与合规双重压力**：高端算力出口管制、实体清单、数据跨境流动限制，迫使企业建立“双轨/多轨”合规体系 [4]  
- **核类比推动“算力许可制”讨论**：将前沿模型训练类比核设施许可，涉及算力阈值、查验机制、国际原子能机构式监督提案 [17]  
- **全球南方话语权缺失**：非西方视角的包容性/可及性研究 [15] 指出治理标准制定中缺乏 Global South 参与机制

### 5.3 伦理与劳动影响的新议题

- **红队/数据标注劳动保护**：大规模红队 [10][9]、多样化攻击生成 [9] 背后的众包劳动条件、心理健康风险未纳入治理框架  
- **生成式内容版权与责任归属**：EU AI Act 第 53 条训练数据透明度要求 [1] 与版权指令交互复杂，司法判例尚少  
- **核能/医疗等高后果领域的预期性治理**：AI Observatory 概念 [13] 试图在事故发生前建立监测预警

---

## 6. 资本与生态（Capital & Ecosystem）

### 6.1 投资与估值信号

- **ISO 42001 进入金融量化框架（RAID）**：标志合规成本可量化、可定价，将直接影响 AI 项目融资估值、保险定价、并购尽调 [2]  
- **合规 SaaS 赛道早期**：OneTrust、TrustArc、Vanta 等扩展 AI 模块；初创公司切入 OSCAL 工具链、红队平台、事件管理（公开融资数据在候选证据中**缺失**）  
- **开源生态**：OSCAL、Open Policy Agent (OPA)、Rego 策略语言、Sigstore 供应链签名等 CNCF 项目被复用于 AI 合规 [6][18]

### 6.2 人才流动与社区格局

| 群体 | 动向 | 证据 |
|------|------|------|
| 学术界（CRFM/HAI、Stanford、MIT、Oxford 等） | 主导 FMTI、AGILE、红队基准、核类比等议程设定 | [3][4][17][8] |
| 标准组织（ISO/IEC JTC1 SC42、NIST、CEN-CENELEC JTC21） | 制定 42001/23894/42006、AI RMF、EU 协调标准 | [2][1][4] |
| 监管机构（EU AI Office、美 NIST/OMB、中 CAC/工信部） | 推动实施细则、沙箱、认证机构授权 | [1][4] |
| 产业联盟（Partnership on AI、MLCommons、Frontier Model Forum） | 发布最佳实践、基准、事件共享框架 | [16][12] |

> **生态缺口**：**审计员认证体系**、**红队师标准化**、**事件调查员培训**三大人才缺口尚无系统性解决方案。

---

## 7. 信号与预测（Signals & Forecast）

### 7.1 早期信号（2025-2026 观测到）

| 信号 | 来源 | 含义 |
|------|------|------|
| Compliance-as-Code 原型多点涌现 | [6][5][2] | 工程化落地从 0→1 |
| FMTI/AGILE 成为跨国对话“共同语言” | [3][4] | 软法基准地位确立 |
| 核类比进入政策提案讨论 | [17] | 许可制立法窗口打开 |
| Agentic 红队基准发布 | [8] | 评测范式代际跃迁 |
| AI 事件治理开放问题清单发布 | [12] | 事件治理标准化启动 |

### 7.2 未来 6-18 月可验证预测（含置信度与可证伪条件）

| # | 预测 | 依据链 | 置信度 | 可证伪条件（若不发生则判断失效） |
|---|------|--------|--------|----------------------------------|
| P1 | **EU AI Act 高风险 AI 合格评估指南（第 43 条）正式发布，且至少 3 个成员国指定通知机构** | EU 立法时间表 + AI Office 设立 [1] | 较大概率 | 2026-12-31 前未发布指南或通知机构 < 3 家 |
| P2 | **ISO 42001 全球有效证书数突破 500 张** | RAID 框架引入 [2]、认证机构扩容趋势 | 推测 | 2026-12-31 前 ISO 官网公示证书数 < 500 |
| P3 | **FMTI 2026 版发布，新增“第三方审计/红队报告公开”指标，且至少 2 家头部厂商得分回升 > 10 分** | FMTI 方法论演进趋势 [3]、外部压力增大 | 推测 | 2026 年无新版发布，或均分继续下降 |
| P4 | **首个基于 OSCAL 的跨司法管辖区合规互认试点（EU-US 或 EU-SG）启动** | OSCAL 扩展提案 [6]、EU-US TTC AI 工作组 | 推测 | 2026-12-31 前无官方公告 |
| P5 | **中国发布“AI 安全治理标准体系 1.0”（含基础模型、具身智能、红队、事件分级系列标准）** | 标准化管理委员会规划、AGILE 指数跟踪 [4] | 推测 | 2026-12-31 前无国家标准公告 |
| P6 | **至少一起跨境 AI 事件触发多司法管辖区联合调查（依据《开放问题》框架）** | AI 事件治理开放问题 [12]、全球峰会共识 | 推测 | 2026-12-31 前无此类公开案例 |

> **不确定性提示**：上述预测均标注 `[P]`，受地缘政治突变、技术范式突变（如 AGI 时间线提前）、监管资源优先级调整影响大。**风险**在于：合规成本可能挤压中小创新主体，导致“合规护城河”强化寡头垄断 [17][2]。

---

## 经典与奠基性工作（Classic & Foundational Works）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| EU AI Act (2024/1689) | 2024 | 欧盟立法机构 | 高（全球首部综合 AI 法） | 正式法律文本 | 高 | ★★★★★ | https://eur-lex.europa.eu/eli/reg/2024/1689/oj | 所有 AI 治理研究的基准法律文本 |
| ISO/IEC 42001:2023 | 2023 | ISO/IEC JTC1 SC42 | 中高 | 国际标准 | 高 | ★★★★★ | https://www.iso.org/standard/81230.html | AI 管理体系核心标准 |
| NIST AI RMF 1.0 | 2023 | NIST | 高 | 美国官方框架 | 高 | ★★★★★ | https://doi.org/10.6028/NIST.AI.100-1 | 美国事实上的合规基准 |
| OECD AI Principles (Updated) | 2024 | OECD | 高 | 政府间组织软法 | 高 | ★★★★☆ | https://oecd.ai/en/ai-principles | 多边治理共同语言 |
| Foundation Model Transparency Index (FMTI) v1/v2 | 2023/2024 | Stanford CRFM | 高 | 学术基准 | 高 | ★★★★★ | https://crfm.stanford.edu/fmti/ | 透明度量化基准奠基作 |
| Nuclear Analogy in AI Governance | 2025 | 学术团队 | 中 | arXiv 预印本 | 中 | ★★★★☆ | [17] | 许可制/监管类比的系统性梳理 |

---

## 开源项目与工具链（Open-Source Projects & Toolchains）

| 名称 | 年份 | 维护机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|---------------|------|------|--------|--------|------|------|
| OSCAL (Open Security Controls Assessment Language) | 2020- | NIST | 高（星标/采用数待核实） | 美国联邦标准 | 中高 | ★★★★☆ | https://pages.nist.gov/OSCAL/ | 合规证据机器可读格式，AI 扩展中 [6] |
| Open Policy Agent (OPA) / Rego | 2018- | CNCF Graduated | 高 | CNCF 毕业项目 | 高 | ★★★★★ | https://www.openpolicyagent.org/ | 策略即代码，广泛用于云原生合规 |
| Sigstore / Cosign | 2020- | Linux Foundation / sigstore-dev | 高 | LF 项目 | 高 | ★★★★★ | https://www.sigstore.dev/ | 供应链签名/验证，可复用于模型溯源 |
| Generative AI Toolkit | 2024 | 学术/产业团队 | 低（早期） | arXiv 预印本 | 低 | ★★★☆☆ | [7] | LLM 全生命周期质量框架 |
| AI Incident Database (AIID) | 2020- | Partnership on AI | 中 | 产业联盟 | 中 | ★★★★☆ | https://incidentdatabase.ai/ | 事件治理数据基础设施 [12] |

---

## 数据集与评测基准（Datasets & Benchmarks）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| Foundation Model Transparency Index (FMTI) 2025 | 2025 | Stanford CRFM/HAI | 高 | 学术基准 | 高 | ★★★★★ | [3] | 跨国横向对比、全生命周期指标 |
| AGILE Index 2025 | 2025 | 国际研究团队 | 中 | arXiv 预印本 | 中高 | ★★★★☆ | [4] | 国家级治理进展跟踪 |
| AI Incident Database | 2020- | Partnership on AI | 中 | 产业联盟 | 中 | ★★★★☆ | https://incidentdatabase.ai/ | 事件治理实证基础 [12] |
| Red Teaming Benchmarks (Math Hallucination / Diverse Attacks / Agentic) | 2024-2025 | 多团队 | 中低 | arXiv 预印本 | 中 | ★★★☆☆ | [10][9][8] | 红队评测范式演进 |
| VQualA 2025 Engagement Prediction | 2025 | ICCV Workshop | 低 | 会议 Workshop | 低 | ★★☆☆☆ | [19] | 短视频互动预测，**非核心治理基准**（误入候选集） |

> 注：VQualA [19]、NTU-NPU Voice Privacy [20]、NTIRE Super-Resolution [21] 等属于视听信号处理基准，**不属于 AI 治理核心基准**，此处仅为完整性列出并标注。

---

## 参考来源（Reference Sources）
[1] Implementation of the EU AI act calls for interdisciplinary governance — https://doi.org/10.1002/aaai.12183
[2] The Risk-Adjusted Intelligence Dividend: A Quantitative Framework for Measuring AI Return on Investment Integrating ISO 42001 and Regulatory Exposure — http://arxiv.org/abs/2511.21975v1
[3] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1
[4] AI Governance InternationaL Evaluation Index (AGILE Index) 2025 — http://arxiv.org/abs/2507.11546v2
[5] A five-layer framework for AI governance: integrating regulation, standards, and certification — http://arxiv.org/abs/2509.11332v1
[6] Making AI Compliance Evidence Machine-Readable — http://arxiv.org/abs/2604.13767v1
[7] Generative AI Toolkit -- a framework for increasing the quality of LLM-based applications over their whole life cycle — http://arxiv.org/abs/2412.14215v1
[8] Mind the Gap: Comparing Model- vs Agentic-Level Red Teaming with Action-Graph Observability on GPT-OSS-20B — http://arxiv.org/abs/2509.17259v1
[9] Learning diverse attacks on large language models for robust red-teaming and safety tuning — http://arxiv.org/abs/2405.18540v3
[10] Red Teaming for Large Language Models At Scale: Tackling Hallucinations on Mathematics Tasks — http://arxiv.org/abs/2401.00290v1
[11] Artificial Intelligence in Governance, Risk and Compliance: Results of a study on potentials for the application of artificial intelligence (AI) in governance, risk and compliance (GRC) — http://arxiv.org/abs/2212.03601v2
[12] Open Problems in AI Incident Governance — http://arxiv.org/abs/2607.05163v1
[13] Towards an AI Observatory for the Nuclear Sector: A tool for anticipatory governance — http://arxiv.org/abs/2504.12358v1
[14] EU AI Act (2024/1689) and EU MDR (2017/745): Breaking the Expensive Myth: Why AI-Powered Medical Devices Under EU MDR Don’t Need EU AI Act Certification – A Detailed Analysis of Regulatory Requirements and Compliance — https://doi.org/10.70317/2025.02rw02
[15] Non-Western Perspectives on Web Inclusivity: A Study of Accessibility Practices in the Global South — http://arxiv.org/abs/2501.16601v1
[16] Reproducibility: The New Frontier in AI Governance — http://arxiv.org/abs/2510.11595v1
[17] The Nuclear Analogy in AI Governance Research — http://arxiv.org/abs/2510.21203v1
[18] Proceedings of the 3rd Workshop on Open-Source Design Automation (OSDA), 2023 — http://arxiv.org/abs/2303.18024v1
[19] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1
[20] NTU-NPU System for Voice Privacy 2024 Challenge — http://arxiv.org/abs/2410.02371v1
[21] NTIRE 2025 Challenge on Image Super-Resolution (x4): Methods and Results — http://arxiv.org/abs/2504.14582v3

---

*Generated by research-bot · topic=`ai-治理与监管政策法规与标准` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`nvidia/nemotron-3-ultra-550b-a55b` · sources=32 · duration=445s · 2026-11-25T05:33:13+00:00*
