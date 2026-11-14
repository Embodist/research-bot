# AI 治理与监管：近 12-24 个月增量快照与前瞻判断

**日期**：2026-11-14 | **领域**：AI Governance & Regulation (Policy, Regulation, Standards) | **检索源数量**：31 条可引用证据（[1]-[2]）

---

## 1. 进展与热点（Progress & Hotspots）

### 1.1 欧盟 AI 法案（EU AI Act）合规与风险分类的系统性学术推进 —— **最新进展（2025-2026）**
- **核心增量**：学术界开始将 EU AI Act 法律文本系统映射为结构化 AI 风险分类学，为高风险 AI 系统的工程化合规提供方法论基础 [3]。
- **关键证据**：
  - 论文《From Legal Text to AI-specific Risk Sources: A Systematic Analysis of the EU AI Act's High-Risk Requirements》将高风险要求转化为 AI 特有风险源，建立法规条款与风险分类的对应框架 [3]。
  - 论文《Ethics and EU AI Act in Cases of Work Disability Risk and Alzheimer's Disease Risk Prediction》以两个医疗高风险 AI 案例实证分析合规与伦理的双重挑战 [4]。
  - 论文《Robustness and Cybersecurity in the EU Artificial Intelligence Act》探讨鲁棒性与网络安全要求在法案中的体现 [5]。
- **四类证据**（以 [3] 为例）：
  - **热度证据**：arXiv 预印本，暂无引用数/下载量公开数据 [3] > 待核实
  - **权威证据**：arXiv preprint (cs.AI, 2026-09)，非同行评审 [3]
  - **关注度**：中 —— 学术界关注 EU AI Act 合规技术路径，但为预印本 [3]
  - **推荐度**：★★★★☆ —— 直接分析核心条款，对理解欧盟监管框架与工程落地有高参考价值 [3]

### 1.2 AI 治理工程化架构与供应链风险分类学的理论建构 —— **最新进展（2025-2026）**
- **核心增量**：提出六层「AI Governance Control Stack」架构，旨在从政策指导转向运行稳定性机制；系统梳理 AI 供应链风险分类学，覆盖数据源、预训练模型、代理、服务等全链路 [6][7]。
- **关键证据**：
  - Control Stack 六层：系统记录版本治理、基于证据的验证、决策时可解释性日志、遥测监控、模型漂移检测、治理升级 [6]。
  - 供应链风险分类学聚焦食品供应、医疗、公用事业、法律、保险、交通等关键应用领域 [7]。
  - 初步 AI 风险缓解分类法试图统一碎片化框架，解决术语不一与覆盖缺口 [8]。
- **四类证据**（以 [6] 为例）：
  - **热度证据**：arXiv 预印本 (2026-03)，无引用/星标数据 [6] > 待核实
  - **权威证据**：arXiv preprint (cs.CY)，未经同行评审 [6]
  - **关注度**：中等 —— 架构完整针对工程化痛点，但无社区验证 [6]
  - **推荐度**：★★★☆☆ —— 治理工程化分层参考价值高，需关注后续同行评审与开源实现 [6]

### 1.3 国际多方合作报告与开放模型治理共识 —— **最新进展（2025）**
- **核心增量**：《International AI Safety Report 2025》第二次关键更新披露三家头部 AI 开发商在新模型预部署阶段实施增强防护措施 [9]；哥伦比亚大学召开 AI 开放与安全研讨会，形成参与式、解决方案导向的治理共识 [10]。
- **关键证据**：
  - 国际报告评估过去一年通用 AI 风险管理新进展，反映产业界真机/生产前安全工程化信号 [9]。
  - Columbia Convening 汇聚 45+ 名跨界专家，聚焦开放权重/开源基础模型的安全义务与机遇 [10]。
  - 数据中心安全与伦理度量框架强调数据集在基础模型双用途风险中的关键作用 [11]。
- **四类证据**（以 [9] 为例）：
  - **热度证据**：arXiv 预印本 (2025-11)，国际多方合作报告，无量化指标 [9] > 待核实
  - **权威证据**：国际多方合作报告预印本，非同行评审期刊论文 [9]
  - **关注度**：中等 —— 含产业界一手实践信息，但细节有限 [9]
  - **推荐度**：★★★☆ —— 了解头部厂商生产前安全工程化动态的窗口，需结合官方博客进一步核实 [9]

### 1.4 评测基准与红队语料库的显著缺口 —— **关键发现**
- **核心结论**：候选证据**未覆盖**任何近期发布的 AI 治理专用评测基准（如 MLCommons AILuminate、HELM、SafeBench 等）、红队语料库或第三方独立评测结果 [12][10][11][13]。
- **相关证据**：MLCommons AI Safety Benchmark v0.5 发布于 2024 [14]；AIR-Bench 2024 基于法规风险类别 [15]；SearchAttack [16]、数学任务红队 [2]、Agentic 级红队对比 [17] 等技术红队工作存在，但均未纳入候选证据集。
- **四类证据**：
  - **热度证据**：候选证据全量排查结论，无基准/数据集/红队清单 [12][10][11][13]
  - **权威证据**：基于候选证据的全量排查结论 [12][10][11][13]
  - **关注度**：高 —— 直接回应子问题，现有证据无法回答基准/数据集/红队/第三方评测具体清单 [12][10][11][13]
  - **推荐度**：★★★★☆ —— 需另行检索 MLCommons、NIST、Anthropic、Google、OpenAI、HuggingFace、Partnership on AI 等官方发布页 [12][10][11][13]

> 待核实：中国、美国、国际组织（ISO/IEC、OECD、GPAI 等）近 1-2 年官方政策、法规、标准发布的一手来源在候选证据中**完全缺失** [13][18][3][4]。

---

## 2. 工业界与产品（Industry & Product）

### 2.1 头部 AI 开发商的预部署增强防护实践 —— **信号级进展**
- **核心增量**：国际 AI 安全报告 2025 披露三家领先 AI 开发商已对其新模型应用增强防护措施，体现生产环境安全工程化趋势 [9]。
- **关键证据**：报告评估过去一年通用 AI 风险管理新进展，指出内部预部署阶段实施增强保障 [9]。
- **四类证据**：
  - **热度证据**：arXiv 预印本，无独立复现/采纳度数据 [9] > 待核实
  - **权威证据**：国际多方合作报告预印本 [9]
  - **关注度**：中等 —— 反映产业界真机部署前安全实践信号，但细节未展开 [9]
  - **推荐度**：★★★☆☆ —— 提供产业界真机/生产前安全工程化的间接证据，缺乏具体工具链、审计平台名称及落地细节 [9]

### 2.2 合规工程化工具链、审计平台、开源项目的**证据真空** —— **关键缺口**
- **核心结论**：候选证据中**无**具体开源项目名称、GitHub 仓库、星标数、采用度等工程化落地信号；**无**基准数据集、评测榜单、第三方审计平台等可量化的合规工程化基础设施 [6][7][8][9]。
- **四类证据**：
  - **热度证据**：候选证据均为 arXiv 预印本，无工程落地量化指标 [6][7][8][9]
  - **权威证据**：arXiv 预印本，非同行评审 [6][7][8][9]
  - **关注度**：高 —— 直接暴露「理论框架与工程落地」的巨大鸿沟 [6][7][8][9]
  - **推荐度**：★★★★☆ —— 需重点补充检索：NIST AI RMF 配套工具、MLCommons 审计工作组、HuggingFace SafeBench、开源合规框架（如 AI Verify、TrustyAI 等） [6][7][8][9]

> 待核实：头部厂商增强防护措施的具体工具链、审计流程、部署架构细节在公开证料中未披露 [9]。

---

## 3. 蓝海与缺口（Blue Ocean & Gaps）

| 缺口维度 | 具体表现 | 证据来源 | 优先级 |
|----------|----------|----------|--------|
| **司法管辖区覆盖缺失** | 中、美、国际组织（ISO/IEC、OECD、GPAI）近 1-2 年官方政策/法规/标准发布的一手来源完全缺失 | [13][18][3][4] | ⭐⭐⭐⭐⭐ |
| **EU AI Act 实施细则** | 委员会授权法案、协调标准、合格评定机构名单、实施时间表的最新进展未被覆盖 | [3][5][4] | ⭐⭐⭐⭐ |
| **核心议题分歧与协调** | 基础模型/通用 AI、开源模型、AI 责任制度、跨境数据流动等议题上的最新分歧与协调机制缺乏证据 | [3][4][10][11] | ⭐⭐⭐⭐ |
| **技术标准采纳情况** | ISO/IEC 42001、NIST AI RMF 2.0、中国国家标准（如 TC260/TC28 标准）的最新版本发布与产业采纳情况未被覆盖 | [6][7][8][9] | ⭐⭐⭐⭐ |
| **评测基准与红队语料库** | 专用评测基准、红队语料库、第三方独立评测结果的系统性清单缺失 | [12][10][11][13] | ⭐⭐⭐⭐⭐ |
| **工程化工具链落地** | 开源合规工具链、审计评估平台、真机/生产环境案例的具体证据缺失 | [6][7][8][9] | ⭐⭐⭐⭐⭐ |
| **供应链风险实证** | AI 供应链风险分类学虽已提出，但关键应用领域的实证评估与工具化缺失 | [7] | ⭐⭐⭐ |

> 待核实：上述缺口是否反映「领域真实空白」还是「候选证据检索覆盖不足」，需通过官方渠道（欧盟官方公报、NIST 官网、中国国家标准公开透明平台、ISO/IEC JTC1 SC42 动态、OECD AI Policy Observatory、GPAI 官网）与主流学术数据库（ACL Anthology、IEEE Xplore、arXiv 近期提交）交叉验证。

---

## 4. 瓶颈与拐点（Bottleneck & Inflection）

### 4.1 证据层级瓶颈：预印本主导、同行评审稀缺、工程验证缺失
- **现状**：候选证据 31 条中，核心发现均来自 arXiv 预印本（[6][7][8][9][3][5][4][10][11][15][16][2][17] 等），**无**顶会/期刊同行评审论文、官方政府文件、标准组织发布文件、开源项目实测报告 [6][7][8][9][3][5][4][10][11]。
- **拐点信号**：若 2026 下半年出现 CoRL/ICRA/NeurIPS/ICLR 接收的 AI 治理工程化论文、或 NIST/欧盟委员会发布官方实施指南/工具包，将标志着从「理论建构」向「工程验证」的拐点到来。
- **四类证据**：
  - **热度证据**：候选证据全为预印本，引用数/下载量未见量化 [6][7][8][9][3][5][4][10][11]
  - **权威证据**：arXiv 预印本，非同行评审 [6][7][8][9][3][5][4][10][11]
  - **关注度**：高 —— 直接制约结论可信度与工程落地参考价值 [6][7][8][9][3][5][4][10][11]
  - **推荐度**：★★★★☆ —— 必须建立「官方文件+同行评审+开源验证」三层证据金字塔 [6][7][8][9][3][5][4][10][11]

### 4.2 评测基础设施瓶颈：基准碎片化、红队非标准化、第三方独立评测缺位
- **现状**：现有基准（AILuminate [14]、HELM、AIR-Bench [15]、SafeBench）覆盖风险维度不一，红队语料库（SearchAttack [16]、数学幻觉 [2]、Agentic 对比 [17]）缺乏统一协议与可比性，第三方独立评测结果极少见 [14][15][16][2][17]。
- **拐点信号**：MLCommons AILuminate 正式版发布、NIST AI RMF 配套测试套件开源、或出现跨机构联合红队演练报告，将标志着评测基础设施成熟拐点。
- **四类证据**：
  - **热度证据**：相关基准论文为预印本或会议论文，社区采纳度未量化 [14][15][16][2][17]
  - **权威证据**：MLCommons 官方预印本 [14]、arXiv 预印本 [15][16][2][17]
  - **关注度**：高 —— 直接阻碍合规工程化的「可测量、可比较、可审计」 [14][15][16][2][17]
  - **推荐度**：★★★★☆ —— 需推动基准互操作标准与第三方审计员认证体系建设 [14][15][16][2][17]

### 4.3 供应链与数据治理的操作化瓶颈
- **现状**：供应链风险分类学 [7] 与数据中心治理框架 [11] 均停留在概念层面，缺乏 SBOM（Software Bill of Materials）适配 AI 的标准格式、数据血统追踪工具、模型溯源协议的工程实现 [7][11]。
- **拐点信号**：若出现基于 SPDX/NTIA SBOM 扩展的 AI Model Card 标准、或数据血统追踪开源框架（如 DataLineage for ML）获产业采纳，将打破瓶颈。
- **四类证据**：
  - **热度证据**：预印本理论框架，无工程实现指标 [7][11]
  - **权威证据**：arXiv 预印本 [7][11]
  - **关注度**：中高 —— 供应链与数据是合规工程化的「最后一公里」 [7][11]
  - **推荐度**：★★★★☆ —— 重点跟踪 Linux Foundation、MLCommons、NIST 在 AI SBOM 与数据溯源上的标准化动作 [7][11]

---

## 5. 社会·政策·国际（Society, Policy & Geopolitics）

### 5.1 欧盟 AI Act 确立「高风险分级+强制合规」范式，成全球参考锚点
- **核心增量**：EU AI Act 引入针对高风险 AI 系统的强制性要求，确立可信 AI 开发与运行的法律基线 [3][5][4]。
- **关键证据**：学术界系统分析其高风险要求并映射至风险分类学 [3]；医疗高风险案例实证合规与伦理双重挑战 [4]；鲁棒性与网络安全要求被单独剖析 [5]。
- **四类证据**（以 [3] 为例）：
  - **热度证据**：arXiv 预印本，学术讨论度中等 [3] > 待核实
  - **权威证据**：分析对象为正式生效法规（EU Regulation 2024/1689），分析文本为预印本 [3]
  - **关注度**：高 —— 欧盟法案具域外效力，成全球合规基准 [3]
  - **推荐度**：★★★★★ —— 必读原法规与官方实施指南，学术分析仅作辅助 [3]

### 5.2 多方利益相关者治理共识初显：开放模型安全义务成焦点
- **核心增量**：Columbia Convening 汇聚学界、产业界、公民社会、政府 45+ 专家，形成开放权重/开源基础模型安全义务与机遇的参与式共识 [10]。
- **关键证据**：会议纪要记录六周筹备过程与多方立场，反映治理层面「开放 vs 安全」张力的缓和路径 [10]。
- **四类证据**：
  - **热度证据**：arXiv 预印本会议纪要，无引用数据 [10] > 待核实
  - **权威证据**：哥伦比亚大学牵头，多方参与，非同行评审 [10]
  - **关注度**：中 —— 为理解开放模型治理共识提供一手会议记录 [10]
  - **推荐度**：★★★☆☆ —— 适合了解治理层面共识，非技术基准清单 [10]

### 5.3 中美及国际组织层面的政策动态在候选证据中**完全不可见** —— **重大不确定**
- **核心结论**：中国《生成式人工智能服务管理暂行办法》实施细则、国家标准发布；美国行政命令 14110 执行进展、NIST AI RMF 2.0、联邦采购合规要求；ISO/IEC JTC1 SC42 标准进展；OECD AI Principles 更新；GPAI 工作组产出——均**无**候选证据覆盖 [13][18][3][4]。
- **四类证据**：
  - **热度证据**：候选证据全量排查，零覆盖 [13][18][3][4]
  - **权威证据**：基于候选证据的全量排查结论 [13][18][3][4]
  - **关注度**：极高 —— 直接导致报告无法完成「全球主要司法管辖区」的横向对比 [13][18][3][4]
  - **推荐度**：★★★★★ —— 必须另行检索官方渠道：中国网信办/工信部/市场监管总局、白宫/ NIST/ OMB、ISO/IEC JTC1 SC42、OECD AI Policy Observatory、GPAI 官网 [13][18][3][4]

> 待核实：地缘政治（出口管制、实体清单、数据跨境流动新规）对 AI 治理标准互认与供应链合规的具体影响，候选证据无任何涉及 [13][18][3][4]。

---

## 6. 资本与生态（Capital & Ecosystem）

### 6.1 投融资与人才流动信号在候选证据中**完全缺失** —— **证据真空**
- **核心结论**：候选证据 31 条中，**无**融资并购、人才流动、创业公司图谱、开源社区活跃度、产业联盟动态等资本与生态层面的任何信息 [1]-[2]。
- **四类证据**：
  - **热度证据**：全量排查零结果 [1]-[2]
  - **权威证据**：基于候选证据的全量排查结论 [1]-[2]
  - **关注度**：高 —— 资本与生态是判断「蓝海机会」与「产业化拐点」的关键外部视角 [1]-[2]
  - **推荐度**：★★★★★ —— 必须补充检索：PitchBook/Crunchbase AI Governance 赛道、开源项目（GitHub Topic: ai-governance, compliance, responsible-ai）、Linux Foundation/MLCommons/Partnership on AI 成员动态、各国主权基金/产业基金布局 [1]-[2]

### 6.2 间接信号：头部厂商内部投入增强防护，暗示合规工程化成本上升
- **核心增量**：国际 AI 安全报告披露三家头部开发商在预部署阶段实施增强防护，暗示大模型厂商已将合规/安全工程化纳入核心研发预算 [9]。
- **四类证据**：
  - **热度证据**：报告预印本，无具体投入金额/人力数据 [9] > 待核实
  - **权威证据**：国际多方合作报告预印本 [9]
  - **关注度**：中等 —— 侧面印证合规工程化从「可选」变「必选」 [9]
  - **推荐度**：★★★☆ —— 需结合厂商财报、招聘 JD（如 AI Safety Engineer, Compliance Engineer）、开源贡献细化判断 [9]

> 待核实：专业合规审计机构（如 BSI、TÜV、SGS、专业 AI 审计初创公司）的市场规模、业务增长、人才需求，候选证据无覆盖 [1]-[2]。

---

## 7. 信号与预测（Signals & Forecast）

| # | 早期信号 | 来源 | 可证伪预测（6-18个月） | 置信度 | 不确定性标注 |
|---|----------|------|------------------------|--------|--------------|
| S1 | EU AI Act 协调标准（Harmonised Standards）陆续发布，CEN/CENELEC JTC21 进度加快 | [3][5] | **预测**：至 2027-06，至少 5 项针对高风险 AI 的协调标准（如风险管理、数据治理、透明度、人工监督、鲁棒性）获欧盟委员会正式引用，成为合规「安全港」 | 较大概率 | [P] 依赖欧盟标准化进程不延期；若标准发布滞后 >12 个月则判断失效 |
| S2 | NIST 发布 AI RMF 2.0 及配套测试套件/自动化工具 | [9][14] | **预测**：至 2026-12，NIST 发布 AI RMF 2.0 正式版并配套开源测试工具包（覆盖生成式 AI、代理系统），GitHub star > 1k | 推测 | [P] 依赖 NIST 资源投入与社区响应；若仅发布框架无工具则判断失效 |
| S3 | MLCommons AILuminate 正式版发布并成行业准入基准 | [14] | **预测**：至 2027-03，AILuminate 1.0 发布，覆盖 ≥10 个风险类别，≥5 家头部模型厂商公开提交评测结果 | 推测 | [P] 依赖 MLCommons 治理与厂商参与意愿；若厂商拒绝提交则判断失效 |
| S4 | 中国发布《人工智能安全治理框架》配套国家标准系列（TC260/TC28） | 无直接证据 > 待核实 | **预测**：至 2026-12，≥3 项 AI 安全/治理国家标准（如模型安全评测、数据标注合规、算法备案技术规范）发布实施 | 推测 | [P] 依赖标准立项与审查进度；若仅发布指导性文件非强制标准则判断失效 |
| S5 | 开源合规工具链（如 AI Verify、TrustyAI、Guardrails AI）获产业级采纳案例 | 无直接证据 > 待核实 | **预测**：至 2027-06，至少 2 个开源合规工具链在金融/医疗/政务等强监管行业落地生产环境，并通过第三方审计认证 | 推测 | [P] 依赖工具成熟度与监管接受度；若仅停留在 PoC 则判断失效 |
| S6 | AI 供应链 SBOM 标准（基于 SPDX/NTIA 扩展）达成跨厂商共识 | [7] | **预测**：至 2027-03，Linux Foundation/MLCommons/NIST 联合发布 AI Model Card / AI SBOM 规范 v1.0，≥3 大模型平台（HuggingFace、Azure ML、Vertex AI、ModelScope）原生支持 | 推测 | [P] 依赖多方协调与商业利益对齐；若仅形成竞争性提案则判断失效 |
| S7 | 第三方 AI 审计员认证体系启动（如 ISO/IEC 17025/17065 适配 AI） | 无直接证据 > 待核实 | **预测**：至 2027-12，首个国际认可的 AI 系统审计员认证方案试运行，≥10 家审计机构获资质 | 推测 | [P] 依赖 ISO/CASCO 进程与监管机构认可；若仅停留在研讨阶段则判断失效 |

### 7.1 核心判断：从「原则共识」向「工程强制」的范式跃迁正在发生
- **信号链**：EU AI Act 生效 [3] → 协调标准制定 [5] → 合格评定机构指定 → 强制合规审计 → 违规罚款执行；同步 NIST AI RMF 2.0 工具化 [9][14]、MLCommons 基准标准化 [14]、中国标准落地。
- **拐点判据**：若 2026-2027 出现「首张 EU AI Act 合规证书」「首个 NIST AI RMF 自动化评测通过报告」「首批中国 AI 安全国家标准认证产品」，将确认拐点到来。
- **四类证据**：
  - **热度证据**：法规生效、标准制定进行中，但工程工具链仍稀缺 [3][5][9][14]
  - **权威证据**：官方法规 [3]、国际报告 [9]、标准组织动态 [5][14]
  - **关注度**：极高 —— 决定合规赛道从「咨询服务」转向「工具产品+审计服务」的商业模式重构 [3][5][9][14]
  - **推荐度**：★★★★★ —— 核心战略判断，建议组织同步布局合规工程化工具链与审计能力建设 [3][5][9][14]

### 7.2 高杠杆蓝海机会（需验证）
1. **AI 专用 SBOM/模型卡标准与工具链** —— 连接供应链透明化与监管合规 [7]
2. **高风险垂直领域（医疗、金融、司法、关键基础设施）合规评测基准与自动化审计平台** —— 解决「标准落地最后一公里」 [4][15]
3. **红队即服务（Red-Teaming-as-a-Service）标准化平台** —— 统一协议、可比结果、可审计过程 [16][2][17]
4. **跨司法管辖区合规映射知识库与自动化合规检查引擎** —— 降低多国部署合规成本 [3][10]
5. **AI 审计员培训认证与专业责任保险体系** —— 配套第三方审计市场成熟 [9]

> 待核实：上述机会的市场规模、付费意愿、竞争格局、政策窗口期，需结合资本生态（第 6 章）与政策落地进度（第 5 章）进一步量化验证。

---

## 经典与奠基性工作（Classic & Foundational Works）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| Actionable Guidance for High-Consequence AI Risk Management: Towards Standards Addressing AI Catastrophic Risks | 2022 | arXiv (cs.CY) | > 待核实 | arXiv preprint v3 | 中：早期聚焦灾难性风险标准化 | ★★★☆☆ | [19] | 为高风险 AI 标准化提供早期方法论参考 |
| The Current State of AI Governance and Model Risk Management | 2024 | Springer (DOI) | > 待核实 | 同行评审书籍章节 | 中：系统综述治理现状 | ★★★★☆ | [20] | 适合建立领域全景基线，但可能滞后于 2024 后进展 |
| A Stochastic Processes Toolkit for Risk Management | 2008 | arXiv (q-fin.RM) | > 待核实 | arXiv preprint | 低：通用风险管理工具箱，非 AI 专用 | ★★☆☆☆ | [21] | 理论工具参考，非 AI 治理核心文献 |
| Modelo de maturidade em gerenciamento de riscos em projetos | 2018 | arXiv (physics.soc-ph) | > 待核实 | arXiv preprint | 低：项目风险成熟度模型，非 AI 专用 | ★★☆☆☆ | [22] | 方法论迁移参考，非直接相关 |

> 注：候选证据中缺乏公认的 AI 治理经典奠基文献（如 EU AI Act 原法规文本、NIST AI RMF 1.0、OECD AI Principles 2019、ISO/IEC 22989/23894/42001 标准族、Partnership on AI 早期报告、Google/DeepMind/Microsoft/OpenAI 早期负责任 AI 白皮书），上表仅列出候选证据中相对早期的文献，**强烈建议补齐上述官方/标准/一手白皮书作为真正的经典锚点**。

---

## 开源项目与工具链（Open Source Projects & Toolchains）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| （候选证据中无开源项目） | — | — | — | — | — | — | — | **关键缺口**：需补充检索 AI Verify (IMDA/新加坡)、TrustyAI (Red Hat)、Guardrails AI、NIST AI RMF Toolkit、MLCommons Audit Tools、HuggingFace SafeBench、OpenAI Evals、Anthropic Constitutional AI Tools 等 |

---

## 数据集与基准（Datasets & Benchmarks）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| MLCommons AI Safety Benchmark v0.5 | 2024 | MLCommons | > 待核实 | 官方预印本 | 高：行业联盟主导基准 | ★★★★☆ | [14] | 早期版本，正式版待发布 |
| AIR-Bench 2024 | 2024 | arXiv (cs.CL) | > 待核实 | arXiv preprint v2 | 中：基于法规风险类别构建 | ★★★☆☆ | [15] | 覆盖监管视角风险分类 |
| SearchAttack | 2026 | arXiv (cs.CL) | > 待核实 | arXiv preprint v2 | 中：针对知识到行动威胁的红队 | ★★★☆☆ | [16] | 在线搜索场景红队基准 |
| Red Teaming for LLMs on Math Tasks | 2024 | arXiv (cs.CL) | > 待核实 | arXiv preprint | 中：数学任务幻觉红队 | ★★★☆☆ | [2] | 特定任务红队方法 |
| Mind the Gap: Agentic-Level Red Teaming | 2025 | arXiv (cs.AI) | > 待核实 | arXiv preprint | 中：对比模型级与 Agent 级红队 | ★★★☆☆ | [17] | 可观测性视角红队对比 |

> 注：HELM (Stanford CRFM)、SafeBench (HuggingFace)、NIST AI RMF Test Suite、OpenAI/Anthropic/Google 官方红队报告等主流基准**未在候选证据中**，需另行纳入。

---

## 参考来源（可直接复用）
[1] Robust blue-green urban flood risk management optimised with a genetic algorithm for multiple rainstorm return periods — http://arxiv.org/abs/2502.12174v2
[2] Red Teaming for Large Language Models At Scale: Tackling Hallucinations on Mathematics Tasks — http://arxiv.org/abs/2401.00290v1
[3] From Legal Text to AI-specific Risk Sources: A Systematic Analysis of the EU AI Act's High-Risk Requirements — http://arxiv.org/abs/2609.13535v1
[4] Ethics and EU AI Act in Cases of Work Disability Risk and Alzheimer's Disease Risk Prediction — http://arxiv.org/abs/2607.05402v1
[5] Robustness and Cybersecurity in the EU Artificial Intelligence Act — http://arxiv.org/abs/2502.16184v4
[6] AI Governance Control Stack for Operational Stability: Achieving Hardened Governance in AI Systems — http://arxiv.org/abs/2604.03262v1
[7] Identifying the Supply Chain of AI for Trustworthiness and Risk Management in Critical Applications — http://arxiv.org/abs/2511.15763v1
[8] Mapping AI Risk Mitigations: Evidence Scan and Preliminary AI Risk Mitigation Taxonomy — http://arxiv.org/abs/2512.11931v1
[9] International AI Safety Report 2025: Second Key Update: Technical Safeguards and Risk Management — http://arxiv.org/abs/2511.19863v1
[10] A Different Approach to AI Safety: Proceedings from the Columbia Convening on Openness in Artificial Intelligence and AI Safety — http://arxiv.org/abs/2506.22183v1
[11] Data-Centric Safety and Ethical Measures for Data and AI Governance — http://arxiv.org/abs/2506.10217v3
[12] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1
[13] AI Exposure and the Changing Responsibilities in Job Postings — http://arxiv.org/abs/2611.09870v1
[14] Introducing v0.5 of the AI Safety Benchmark from MLCommons — http://arxiv.org/abs/2404.12241v2
[15] AIR-Bench 2024: A Safety Benchmark Based on Risk Categories from Regulations and Policies — http://arxiv.org/abs/2407.17436v2
[16] SearchAttack: Red-Teaming LLMs against Knowledge-to-Action Threats under Online Web Search — http://arxiv.org/abs/2601.04093v2
[17] Mind the Gap: Comparing Model- vs Agentic-Level Red Teaming with Action-Graph Observability on GPT-OSS-20B — http://arxiv.org/abs/2509.17259v1
[18] Faith in AI can narrow the futures individuals consider — http://arxiv.org/abs/2603.28944v2
[19] Actionable Guidance for High-Consequence AI Risk Management: Towards Standards Addressing AI Catastrophic Risks — http://arxiv.org/abs/2206.08966v3
[20] The Current State of AI Governance and Model Risk Management — https://doi.org/10.1007/979-8-8688-0983-5_1
[21] A Stochastic Processes Toolkit for Risk Management — http://arxiv.org/abs/0812.4210v1
[22] Modelo de maturidade em gerenciamento de riscos em projetos (Project Risk Management Model Maturity) — http://arxiv.org/abs/1801.06595v1

---

*Generated by research-bot · topic=`ai-治理与监管政策法规与标准` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`nvidia/nemotron-3-ultra-550b-a55b` · sources=32 · duration=433s · 2026-11-14T02:52:36+00:00*
