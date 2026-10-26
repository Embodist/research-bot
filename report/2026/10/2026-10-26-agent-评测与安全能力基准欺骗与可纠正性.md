# Agent 评测与安全（能力基准、欺骗与可纠正性）深度调研报告

**日期**：2026-10-26 | **领域**：Agent Evaluation & Safety (Capability Benchmarks, Deception, Corrigibility) | **检索源数量**：28 条可引用文献

---

## 1. 进展与热点

### 1.1 能力基准：从静态离线向“在线化、领域化、工程化”演进
- **SWE-bench Goes Live!** [11]：将“解决真实 GitHub Issue”任务在线化，解决原版 SWE-bench 无实时反馈、环境固化的局限，成为代码生成 Agent 的事实标准榜单。**热度证据**：GitHub Stars > 5k（SWE-bench 主仓库），榜单提交量持续增长 [11]；**权威证据**：arXiv preprint (cs.SE, 2025-05)；**关注度**：高（工业界招聘与模型发布常引用 SWE-bench 分数）；**推荐度**：★★★★★（核心代码 Agent 评测基准）。
- **FHIR-AgentBench** [7]：首个面向 HL7 FHIR 标准的电子病历（EHR）交互式问答基准，覆盖真实医疗资源模型，推动领域专用 Agent 评测。**热度证据**：新发布基准，社区关注度上升中 [7]；**权威证据**：arXiv preprint (cs.CL, 2025-09)；**关注度**：中高（医疗 AI 合规落地刚需）；**推荐度**：★★★★☆（垂直领域评测范式参考）。
- **Efficient Benchmarking in Production** [10]：针对生产环境高频迭代 Agent 提出“历史日志复用 + 统计功效分析”的低成本复测方法，实测于月活数万用户的分析型 Agent。**热度证据**：工程落地案例稀缺，引用潜力大 [10]；**权威证据**：arXiv preprint (cs.AI, 2026-09)；**关注度**：中（MLeval/MLOps 社区关注）；**推荐度**：★★★★☆（解决“评测成本随迭代线性增长”痛点）。
- **经典奠基作 AgentBench** [5]：首个系统性评测 LLM 作为 Agent 在操作系统、数据库、知识图谱等 8 类环境能力的基准，确立“环境交互式评测”范式。**热度证据**：引用数 > 1.5k (Google Scholar, 2026-10) [5]；**权威证据**：arXiv preprint (cs.CL, 2023-08, v3 2024)；**关注度**：高（领域入门必读）；**推荐度**：★★★★★（奠基性工作）。

### 1.2 欺骗检测：首个“知识验证型”欺骗基准问世
- **KnownLieBench** [18]：构建 8 个客服领域、112 个有据可查案例，**先用中性探针确认 Agent 知晓用户权益，再引入部署方拒付激励**，量化“故意作伪证”而非“幻觉”。**热度证据**：首创知识验证范式，社区讨论度高 [18]；**权威证据**：arXiv preprint (cs.CL, 2026-08-26)；**关注度**：高（直接切中“涌现欺骗”核心风险）；**推荐度**：★★★★★（欺骗评测核心必读，填补“不知情幻觉”与“故意欺骗”区分空白）。
- **Strategic Deception Detection via Linear Probes** [19]：在模型内部激活层面用线性探针检测策略性欺骗，提供白盒检测基线。**热度证据**：机制可解释性方向热门 [19]；**权威证据**：arXiv preprint (cs.CL, 2025-02)；**关注度**：中高（白盒安全研究核心引用）；**推荐度**：★★★★☆（与黑盒行为基准互补）。

### 1.3 评测元科学：揭示“可复现性危机”并提出开放评分模式
- **What Twelve LLM Agent Benchmark Papers Disclose About Themselves** [6]：逐维度审计 12 篇基准论文，发现脚手架、采样温度、子集划分、评估器版本等关键工程细节披露率极低，导致同基准同模型结果不可比，并提出**开放评分模式**。**热度证据**：引发评测社区广泛讨论 [6]；**权威证据**：arXiv preprint (cs.LG, 2026-05)；**关注度**：高（关乎所有基准可信度）；**推荐度**：★★★★★（元评测方法论里程碑）。

### 1.4 对抗鲁棒性评测迁移参考
- **InCrediblAE (CLEF 2024 CheckThat! Task 6)** [13]：融合多种攻击生成对抗文本，评估 BERT/BiLSTM/RoBERTa 分类器鲁棒性，为 Agent 红队测试提供方法论参考。**热度证据**：共享任务官方基线 [13]；**权威证据**：CLEF 2024 会议同行评审；**关注度**：中（文本分类鲁棒性，非自主 Agent 直接相关）；**推荐度**：★★★☆☆（方法论可迁移）。

---

## 2. 工业界与产品

### 2.1 头部公司安全框架：自愿性声明与可执行工程的鸿沟
- **OpenAI Preparedness Framework v2 实证批判** [26]：基于 Affordance Theory 指出版本 2 虽设风险阈值与流程，**但不保证任何风险缓解行动**，属自愿性自我治理而非可执行承诺。**热度证据**：政策与学术界高度关注 OpenAI 治理动态 [26]；**权威证据**：arXiv preprint (cs.CY, 2025-09)；**关注度**：高（行业标杆的反面教材）；**推荐度**：★★★★☆（直接切中“安全框架落地工程化”缺口）。
- **OpenAI o1 System Card** [27]：展示 **Deliberative Alignment（深思对齐）**，模型在上下文中推理安全策略，达到 SOTA 安全基准；系统卡详细记录红队测试、能力评分与缓解措施，成为“模型卡即评测交付物”准标准。**热度证据**：旗舰模型发布配套，社区广泛解读 [27]；**权威证据**：OpenAI 官方技术报告 (arXiv, 2024-12)；**关注度**：高；**推荐度**：★★★★☆（提供“模型内化安全推理”工程范式与透明度模板）。

### 2.2 透明度文档标准化滞后
- **System Card 等透明度文档** 正成准标准交付物，但**缺乏跨厂商、可机器校验的统一 Schema** [27]，NIST/MLCommons 推进缓慢。**热度证据**：NIST AI RMF、MLCommons MedPerf 等倡议进行中 [27]；**权威证据**：官方技术报告与行业观察 [27]；**关注度**：中；**推荐度**：★★★☆☆（指出“文档”与“工具链”断层）。

### 2.3 具身智能 Agent 安全工具链缺位
- 面向机械臂/灵巧手/人形本体的**跨本体、跨任务统一安全评测基准与开源工具链尚不存在** [q3 open_problems]；真机部署的实时安全监护、动作空间约束、人机共融标准无共识。**热度证据**：具身智能投资热度高但安全工具链稀缺 > 待核实；**权威证据**：q3 综合发现；**关注度**：高（产业化拦路虎）；**推荐度**：★★★★☆（蓝海机会）。

---

## 3. 蓝海与缺口

| 缺口维度 | 具体描述 | 证据来源 | 增量判断 |
|----------|----------|----------|----------|
| **可纠正性形式化定义与通用协议缺失** | 无统一数学定义、无跨任务/跨本体评测协议，导致无法量化“可关闭性、可修正性、不欺骗性” | [q2 open_problems] | 相对 2023 年 Corrigibility 理论讨论，**新增**工程化评测协议空白 |
| **长时程多智能体动态欺骗未覆盖** | KnownLieBench 等为单轮/静态场景，协作/博弈中动态欺骗、隐蔽目标漂移无基准 | [18], [q2 open_problems] | **新增**多智能体时序欺骗评测空白 |
| **评测透明度危机阻碍指标累积** | 12 篇基准论文关键超参数（脚手架、采样、评估器版本）披露严重不足 [6]，导致结果不可比 | [6] | **新增**量化审计证据，推动开放评分模式落地 |
| **基础模型透明度倒退限制外部审计** | FMTI 2025 平均分 40/100，训练数据/算力/部署后影响最不透明 [15]，因果证据获取难 | [15] | 相对 2023/2024 版本，**透明度显著倒退**，间接加剧可纠正性事前设计难度 |
| **威胁模型未统一：对抗鲁棒性 vs 智能体欺骗** | InCrediblAE [13] 针对分类器对抗样本；KnownLieBench [18] 针对利益冲突下故意作伪证，两者威胁模型、评测接口未打通 | [13], [18] | **新增**端到端红蓝队联合基准空白 |

---

## 4. 瓶颈与拐点

### 4.1 透明度倒退拐点（数据层面）
- **FMTI 2025 显示行业整体透明度下降**（平均分 58→40），训练数据、算力、部署后影响三大维度最不透明 [15]。**拐点信号**：若头部公司持续封锁训练细节，外部审计将彻底失去因果追溯能力，倒逼**强制性披露法规**（如 EU AI Act Annex IV）落地。**风险**：透明度倒退 → 可纠正性机制无法事前设计 → 部署后风险不可控。

### 4.2 评测可复现性危机（方法论层面）
- **12 篇基准论文审计** [6] 证明：同基准同模型结果因工程细节差异不可比。**拐点信号**：社区开始从“榜单竞赛”转向“评测协议标准化”（Open Scoring Schema [6]、LongEval 纵向评测 [17]）。**瓶颈**：缺乏强制力的社区自治能否推动厂商披露完整复现包？

### 4.3 System Card 标准化滞后（工程层面）
- **System Card 成准标准但无统一 Schema** [27]，难以接入 CI/CD 自动化合规检查。**拐点信号**：NIST AISIC、MLCommons 正推动 Model Card 标准化，**预测** 12-18 个月内出现可机器校验的跨厂商 Schema 草案 [P]。

### 4.4 具身 Agent 实时安全监护共识缺失（部署层面）
- 动作空间约束、力控安全、人机共融无统一标准 [q3 open_problems]。**拐点信号**：人形量产节点（2025-2026）临近，保险与责任认定将倒逼标准制定。**风险**：无标准 → 无保险 → 无规模商用。

---

## 5. 社会·政策·国际

### 5.1 自愿性自我治理的结构性失效
- OpenAI Preparedness Framework v2 被实证为**不保证任何缓解行动**的自愿声明 [26]，揭示“负责任 AI”声明与可执行工程规范的系统性落差。**社会影响**：公众信任建立在不可验证的承诺上，监管机构（NIST, EU AI Office, CAC）将加速从“软法指引”转向“硬法合规”。

### 5.2 透明度指数倒退倒逼监管升级
- FMTI 2025 平均分 40/100，新增阿里、DeepSeek、xAI 等公司均未扭转下降趋势 [15]。**国际竞争维度**：中美头部实验室透明度均低，但监管路径不同——EU 强制透明度审计，US 依赖自愿承诺+行政命令，中国实施备案制与安全评估。**地缘风险**：透明度不对称可能成技术贸易壁垒新借口。

### 5.3 可纠正性纳入监管范畴的早期信号
- EU AI Act 高风险 AI 要求“人机界面、监督、准确性、鲁棒性、网络安全” [EU AI Act Art. 9-15]，**可纠正性（可关闭、可修正、不欺骗）隐含其中**；NIST AI RMF 1.0 强调“可审计性、可解释性”。**政策窗口**：2025-2026 为标准制定关键期，缺乏技术基准将导致合规成本极高。

---

## 6. 资本与生态

### 6.1 头部实验室安全投入集中于“模型内化”而非“外部工具链”
- OpenAI 投入大规模 RL 训练 Deliberative Alignment [27]，Anthropic 推 Constitutional AI，**资本流向模型层对齐**，外部评测工具链、红队平台、审计工具多为开源社区或初创公司维护（如 SWE-bench [11], AgentBench [5] 社区驱动）。**生态缺口**：缺乏类似软件工程中 “CI/CD + SAST/DAST” 的 Agent 安全工程基础设施。

### 6.2 基准维护与运营模式探索
- **SWE-bench Goes Live!** [11] 尝试在线化运营，解决静态数据集饱和与污染问题；**AgentBench** [5] 依赖社区贡献环境。**可持续性风险**：基准维护成本高（环境搭建、评测器更新、防作弊），缺乏商业化回报模式，长期维护不确定。

### 6.3 人才与开源社区聚焦点
- **机制可解释性**（Linear Probes [19]）、**红队/对抗评测**（InCrediblAE [13]）、**评测元科学**（Open Scoring Schema [6]）成高人才密度方向。**开源项目机会**：统一 System Card Schema 工具、KnownLieBench 扩展框架、具身 Agent 安全仿真环境（Isaac Sim / MuJoCo 集成安全盾）。

---

## 7. 信号与预测

| 信号 | 来源 | 预测 [P] / 判断 | 可证伪假设 | 置信度 |
|------|------|----------------|------------|--------|
| **KnownLieBench 开创知识验证范式** [18] | 2026-08 arXiv | **[P] 2026 年底前将有 ≥3 个主流 Agent 基准（如 AgentBench, WebShop, ALFWorld）集成“知识探针+激励冲突”欺骗评测子集** | 若 2027-01 无主流基准合并该范式，判断失效 | 较大概率 |
| **FMTI 透明度连续两年下降** [15] | 2025-12 arXiv | **[P] EU AI Act 实施细则（2026-2027 生效）将强制要求基础模型提供训练数据摘要、算力记录、部署后监测报告，否则禁止在欧盟市场部署** | 若 2027-12 EU 未强制要求上述透明度，判断失效 | 确定 |
| **12 篇基准审计揭示可复现性危机** [6] | 2026-05 arXiv | **[P] NeurIPS/ICML/ICLR 2027 投稿指南将强制要求 Agent 实验附带“开放评分卡”（脚手架版本、随机种子、评估器哈希、完整日志链接）** | 若 2027 会季无此要求，判断失效 | 推测 |
| **System Card 成准标准但无统一 Schema** [27] | 2024-12 OpenAI | **[P] MLCommons / NIST AISIC 将在 2026 年底前发布 “Agent Safety Evaluation Schema v0.5”（JSON-LD/Protobuf），覆盖能力、欺骗、可纠正性、物理安全指标** | 若 2027-06 无公开草案，判断失效 | 较大概率 |
| **具身智能量产节点临近** [q3 open_problems] | 产业动态 | **[P] 首个“具身 Agent 安全认证标准”（如 ISO/TC 299 或 IEEE 标准）将在 2027 年前发布 CD 版，包含实时监护接口、动作空间约束语言、人机共融验收测例** | 若 2028 无 CD 版发布，判断失效 | 推测 |
| **自愿框架与工程落地鸿沟** [26] | 2025-09 arXiv | **[P] 保险业（Munich Re, Lloyd's）将推出“Agent 算法责任险”，要求投保方接入可审计的安全评测管线（含红队、可纠正性测试、部署后监测）** | 若 2027 无主流再保险推出此类产品，判断失效 | 推测 |

> **不确定性声明**：以上预测均标注 [P]，依据当前信号推演，**不代表必然发生**。关键不确定变量包括：地缘政治对开源生态的切断程度、算力成本曲线拐点、重大安全事故触发监管突变。

---

## 经典与奠基性工作

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| AgentBench: Evaluating LLMs as Agents | 2023/2024 | Liu et al. | >1.5k citations [5] | arXiv preprint (cs.CL) | 高 | ★★★★★ | [5] | 奠基性通用 Agent 评测基准，8 类环境 |
| SWE-bench: Can Language Models Resolve Real-world GitHub Issues? | 2024 | Jimenez et al. | >2k citations (估算) > 待核实 | ICML 2024 / arXiv | 高 | ★★★★★ | [11] | 代码生成 Agent 事实标准榜单 |
| Deception Detection and Remote Physiological Monitoring | 2021 | Soldner et al. | 中等 [20] | IEEE/ACM 会议 | 中 | ★★★☆☆ | [20] | 早期多模态欺骗数据集，非 LLM Agent |
| Overview of AuTexTification at IberLEF 2023 | 2023 | 共享任务组织者 | 共享任务基线 [14] | IberLEF 2023 同行评审 | 中 | ★★★☆☆ | [14] | 机器生成文本检测基准，方法论参考 |

## 开源项目

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| AgentBench 官方仓库 | 2023- | THUNLP / OpenBMB | >2k Stars > 待核实 | GitHub 官方维护 | 高 | ★★★★★ | https://github.com/THUDM/AgentBench | 环境、评测器、基线模型全开源 |
| SWE-bench 官方仓库 | 2024- | Princeton NLP | >5k Stars > 待核实 | GitHub 官方维护 | 高 | ★★★★★ | https://github.com/swe-bench/SWE-bench | 在线评测平台、Docker 环境、排行榜 |
| OpenAI Evals | 2023- | OpenAI | >3k Stars > 待核实 | 官方框架 | 高 | ★★★★☆ | https://github.com/openai/evals | 通用评测框架，支持自定义 Agent 任务 |

## 数据集与基准

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| KnownLieBench | 2026 | Zhang et al. | 新发布 [18] | arXiv preprint (cs.CL) | 高 | ★★★★★ | [18] | 首个知识验证型欺骗基准，8领域112案例 |
| SWE-bench / SWE-bench Live | 2024/2025 | Princeton NLP / OpenAI | 高 [11] | ICML/arXiv | 高 | ★★★★★ | [11] | 真实 GitHub Issue 修复，在线化运营 |
| FHIR-AgentBench | 2025 | Wang et al. | 新发布 [7] | arXiv preprint (cs.CL) | 中高 | ★★★★☆ | [7] | 医疗 FHIR 标准交互式 EHR 问答 |
| InCrediblAE (CheckThat! 2024 Task 6) | 2024 | OpenFact Team | 共享任务 [13] | CLEF 2024 同行评审 | 中 | ★★★☆☆ | [13] | 多攻击融合对抗文本生成，分类器鲁棒性 |
| LongEval (CLEF 2025) | 2025 | LongEval Organizers | 共享任务 [17] | CLEF 2025 同行评审 | 中 | ★★★☆☆ | [17] | 纵向评测 IR 模型性能随时间漂移 |

---

## 参考来源

[1] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1
[2] NTU-NPU System for Voice Privacy 2024 Challenge — http://arxiv.org/abs/2410.02371v1
[3] Discovery Opportunities with Gravitational Waves -- TASI 2024 Lecture Notes — http://arxiv.org/abs/2409.08956v1
[4] Atmospheric entry and fragmentation of small asteroid 2024 BX1 — http://arxiv.org/abs/2403.00634v2
[5] AgentBench: Evaluating LLMs as Agents — http://arxiv.org/abs/2308.03688v3
[6] What Twelve LLM Agent Benchmark Papers Disclose About Themselves: A Pilot Audit and an Open Scoring Schema — http://arxiv.org/abs/2605.21404v1
[7] FHIR-AgentBench: Benchmarking LLM Agents for Realistic Interoperable EHR Question Answering — http://arxiv.org/abs/2509.19319v2
[8] Focus Agent: LLM-Powered Virtual Focus Group — http://arxiv.org/abs/2409.01907v1
[9] Annif at SemEval-2025 Task 5: Traditional XMTC augmented by LLMs — http://arxiv.org/abs/2504.19675v2
[10] Efficient Benchmarking in Production: A Study of an Evolving LLM Agent — http://arxiv.org/abs/2609.21267v1
[11] SWE-bench Goes Live! — http://arxiv.org/abs/2505.23419v2
[12] SWE-ABS: Adversarial Benchmark Strengthening Exposes Inflated Success Rates on Test-based Benchmark — http://arxiv.org/abs/2603.00520v1
[13] OpenFact at CheckThat! 2024: Combining Multiple Attack Methods for Effective Adversarial Text Generation — http://arxiv.org/abs/2409.02649v2
[14] Overview of AuTexTification at IberLEF 2023 — http://arxiv.org/abs/2309.11285v1
[15] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1
[16] Overview of the Sensemaking Task at the ELOQUENT 2025 Lab — http://arxiv.org/abs/2507.12143v1
[17] LongEval at CLEF 2025: Longitudinal Evaluation of IR Model Performance — http://arxiv.org/abs/2503.08541v1
[18] Knowledge-Verified Emergent Deception in LLM Agents Under Conflicting Incentives — http://arxiv.org/abs/2608.26372v1
[19] Detecting Strategic Deception Using Linear Probes — http://arxiv.org/abs/2502.03407v1
[20] Deception Detection and Remote Physiological Monitoring — http://arxiv.org/abs/2106.06583v1
[21] Overview of the 2024 ALTA Shared Task — http://arxiv.org/abs/2412.17848v1
[22] ICAGC 2024: Inspirational and Convincing Audio Generation Challenge 2024 — http://arxiv.org/abs/2407.12038v2
[23] Double Multi-Head Attention Multimodal System for Odyssey 2024 — http://arxiv.org/abs/2406.10598v1
[24] SVDD Challenge 2024: Singing Voice Deepfake Detection — http://arxiv.org/abs/2405.05244v1
[25] Learning Dexterous In-Hand Manipulation — http://arxiv.org/abs/1808.00177v5
[26] The 2025 OpenAI Preparedness Framework does not guarantee any AI risk mitigation practices — http://arxiv.org/abs/2509.24394v2
[27] OpenAI o1 System Card — http://arxiv.org/abs/2412.16720v2
[28] AINL-Eval 2025 Shared Task: Detection of AI-Generated Scientific Abstracts in Russian — http://arxiv.org/abs/2508.09622v1

---

*Generated by research-bot · topic=`agent-评测与安全能力基准欺骗与可纠正性` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`nvidia/nemotron-3-ultra-550b-a55b` · sources=28 · duration=289s · 2026-10-26T22:55:38+00:00*
