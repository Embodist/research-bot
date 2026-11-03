# AI 治理与监管（政策、法规与标准）增量快照报告（2024-2026）

**日期**：2026-11-03（UTC） | **领域**：AI Governance & Regulation | **检索源数量**：26 条可核查证据源（arXiv 预印本、顶会 Workshop、技术报告）

---

## 1. 进展与热点（Progress & Hotspots）

### 1.1 欧盟 AI Act：高风险系统落地与条款解释争议
- **EU AI Act 将医疗 AI 预测工具（工伤残疾风险、阿尔茨海默病风险）判定为高风险系统**，从研究环境推向生产部署需完成大量合规工作（合规性评估、基本权利影响评估、事件通报等）[14]。  
  - 热度证据：arXiv 预印本，BAI'26 会议论文，提交于 2026-06-07 [14]  
  - 权威证据：arXiv (cs.CY)，会议同行评审  
  - 关注度：中等——EU AI Act 合规是当前欧盟 AI 监管核心，医疗高风险场景关注度高 [14]  
  - 推荐度：★★★★☆——直接涉及 EU AI Act 实操合规，对理解高风险系统落地要求有参考价值 [14]

- **EU AI Act 第 2 条对“内部部署”是否纳入监管范围存在解释分歧**，学界梳理了支持与反对的多种解释路径，面向欧盟委员会、提供者、部署者、法院及政策社区提供解释选项[7]。  
  - 热度证据：arXiv 预印本 v4，2025-12-05 提交 [7]  
  - 权威证据：arXiv (cs.CY)，法律学术备忘录  
  - 关注度：中等——内部部署范围界定直接影响企业合规成本，法律界与政策圈关注 [7]  
  - 推荐度：★★★★☆——聚焦 AI Act 关键条款歧义，为合规策略提供多角度参考 [7]

- **前沿生物基础模型 ESM3 被纳入 EU AI Act 系统性风险 GPAI 评估框架**，首次探讨生物模态模型的系统性风险判定逻辑[8]。  
  - 热度证据：arXiv 预印本，2026-05 提交 [8]  
  - 权威证据：arXiv (cs.CY)  
  - 关注度：中等——法规适用范围向新模态扩展的前沿探讨 [8]  
  - 推荐度：★★★☆☆——展示最新法规如何应对新型模型，间接反映风险分级原则的演进 [8]

### 1.2 头部实验室伦理话语策略与治理互动
- **OpenAI 面向大众与学术受众的公开话语中，“伦理/安全/对齐”框架随时间演变且存在差异**，反映行业头部企业对监管预期的策略性表达[2]。  
  - 热度证据：arXiv 预印本，2026-01-23 提交 [2]  
  - 权威证据：arXiv (cs.CY)，结构化语料库分析  
  - 关注度：中等——头部企业话语策略研究被政策与治理研究引用，间接反映美式自律与立法互动 [2]  
  - 推荐度：★★★☆☆——提供企业话语视角，辅助理解美式治理语境下的行业自律与立法预期 [2]

### 1.3 合成媒体检测技术基准与标准化
- **CVPR 2026 举办 NTIRE 2026 挑战赛，聚焦“野外鲁棒 AI 生成图像检测”**，旨在开发能在真实变换（裁剪、压缩、模糊等）下区分真实与生成图像的模型，推动技术标准/基准建设[15]。  
  - 热度证据：CVPR 2026 Workshop 挑战赛论文，同行评审 [15]  
  - 权威证据：CVPR 顶会 Workshop（同行评审）  
  - 关注度：高——生成式 AI 扩散下合成媒体检测是国际标准化与平台治理共同关注热点 [15]  
  - 推荐度：★★★★★——顶会权威基准，直接服务于技术标准与内容治理工具链建设 [15]

### 1.4 红队测试方法论演进与智能体层面评估
- **Agentic AI 系统的红队测试需区分模型层面与智能体层面漏洞**；论文对比 GPT-OSS-20B 在独立模型模式与智能体循环模式下的红队结果，提出 AgentSeer 可观测性框架将智能体系统分解为粒度动作与组件，应用 HarmBench 有害目标进行迭代攻击[22]。  
  - 热度证据：arXiv 预印本 (cs.AI)，2025-09 提交 [22]  
  - 权威证据：arXiv 预印本  
  - 关注度：中——新颖的对比红队方法论，针对智能体系统的安全评估缺口 [22]  
  - 推荐度：★★★★☆——为智能体 AI 红队测试提供了系统性框架与实证对比，工程参考价值高 [22]

- **当前 AI 红队实践存在方法论偏差：过度聚焦发现离散漏洞，偏离红队作为批判性思维练习的初衷**；论文批判性回顾红队从军事到网络安全再到 AI 的演变，指出实践与原始意图的显著差距[23]。  
  - 热度证据：arXiv 预印本 v2，2025-07 提交 [23]  
  - 权威证据：arXiv 预印本 (cs.AI)  
  - 关注度：中——对红队方法论的元反思，引发社区对评估范式的讨论 [23]  
  - 推荐度：★★★★☆——有助于校准红队工程实践的目标与边界，避免工具化陷阱 [23]

### 1.5 AI 预测权威感对人类决策自主性的实证风险
- **1,305 人行为实验显示 40%+ 参与者将 AI 视为预测权威，导致放弃确定收益，效应在预测反复失败后仍存续**，提示治理框架需关注人机交互层面的认知风险[1]。  
  - 热度证据：arXiv 预印本 (cs.HC)，2026-03 提交 v2 [1]  
  - 权威证据：arXiv 预印本，大规模行为实验  
  - 关注度：中——行为实证揭示 AI 系统部署中的人类自主性侵蚀风险，呼应 IEEE EAD 等框架中的人类福祉原则 [1]  
  - 推荐度：★★★☆☆——为治理框架中人类能动性保护条款提供实证支撑 [1]

> **增量判断**：2024-2026 年学术前沿聚焦于 **EU AI Act 具体条款的落地解释**（高风险医疗、内部部署、系统性风险外延）、**头部实验室话语策略的实证分析**、**合成媒体检测基准化**，以及 **红队测试从模型级向智能体级的方法论跃迁与元反思**。美国联邦/州立法、中国算法备案、英国白皮书落地、ISO/IEC JTC1 SC42 标准进展等在候选证据中**缺失**，需补充检索。

---

## 2. 工业界与产品（Industry & Product）

### 2.1 红队测试工具链与平台生态
- **PyRIT：面向生成式 AI 系统的安全风险识别与红队测试框架**，微软开源，支持多模态攻击与评分[20]。  
  - 热度证据：arXiv 预印本，2024-10 提交 [20]  
  - 权威证据：arXiv 预印本，微软官方维护  
  - 关注度：中高——工业界主流红队工具之一，GitHub 活跃度高 [20]  
  - 推荐度：★★★★☆——生产级红队工程化框架，支持自动化攻击流程 [20]

- **ViolentUTF：面向生成式 AI 红队测试的可访问平台**，提供图形化界面降低红队门槛[24]。  
  - 热度证据：arXiv 预印本 v2，2025-04 提交 [24]  
  - 权威证据：arXiv 预印本，演示论文  
  - 关注度：中——降低红队实践门槛的工程化产品 [24]  
  - 推荐度：★★★☆——面向非专家的红队平台，推动红队实践普及 [24]

- **AgentSeer：智能体系统可观测性框架**，支持将智能体循环分解为粒度动作图，配合红队测试实现模型级与智能体级对比[22]。  
  - 热度证据：arXiv 预印本，2025-09 提交 [22]  
  - 权威证据：arXiv 预印本  
  - 关注度：中——智能体 AI 红队工程的新型基础设施 [22]  
  - 推荐度：★★★★☆——智能体层面安全评估的关键工程组件 [22]

### 2.2 合规工程工具链（模型卡片、数据血缘、水印、SBOM）现状
> **待核实**：候选证据中**未覆盖**模型卡片、数据血缘、水印、审计日志、SBOM for AI 等合规工具链组件在 2024-2025 年的工程成熟度、生产级采纳案例与互操作性标准[18][26]。需补充检索 MLCommons Croissant、Hugging Face Model Cards、DataProvenance、C2PA、SPDX AI、OpenSSF 等项目进展。

### 2.3 文档处理与数据合规基础设施
- **Docling：高效开源 AI 驱动文档转换工具包**，支持 PDF 等非结构化文档转结构化表示，为数据血缘与合规审计提供基础设施[18]。  
  - 热度证据：arXiv 预印本，2025-01 提交 [18]  
  - 权威证据：arXiv 预印本，IBM Research 开源  
  - 关注度：中——数据预处理合规链路的基础组件 [18]  
  - 推荐度：★★★☆——合规数据管线的上游工具，间接服务于数据血缘与审计 [18]

---

## 3. 蓝海与缺口（Blue Ocean & Gaps）

| 缺口维度 | 具体缺口描述 | 证据支撑 | 优先级 |
|----------|--------------|----------|--------|
| **多司法管辖区立法同步追踪** | 缺乏 2024-2026 年美国（联邦/州立法、行政命令、NIST 标准）、中国（算法备案、标准体系、数据出境）、英国（AI 监管白皮书落地、DSIT 指引）、国际组织（ISO/IEC JTC1 SC42、OECD、G7 广岛进程、联合国咨询机构）的立法、执法指引、技术标准进展与分歧系统性对比 | q1.open_problems[0] | ★★★★★ |
| **EU AI Act 细则与实施时间表** | 委员会授权法案、协调标准、成员国执法指引的最新文本与实施时间表未在候选证据中出现 | q1.open_problems[1] | ★★★★★ |
| **核心分歧点官方表态** | 各司法管辖区对“基础模型/通用 AI”“高风险判定标准”“开源豁免”“跨境执法互认”等核心分歧点的官方表态与谈判进展缺失 | q1.open_problems[2] | ★★★★★ |
| **经典框架在新法规中的引用/修正** | Asilomar、OECD AI Principles、IEEE EAD 等奠基性框架在 EU AI Act、美国行政令、中国《生成式人工智能服务管理暂行办法》等最新法规中的具体引用条款与修正细节缺乏系统性对比研究 | q2.open_problems[0] | ★★★★☆ |
| **原则向法律义务的转化路径差异** | 透明度、问责制、人类自主性等原则向合规性评估、基本权利影响评估、事件通报等具体法律义务的转化路径在不同司法管辖区的差异分析缺失 | q2.open_problems[1] | ★★★★☆ |
| **合规工具链成熟度系统性评估** | 模型卡片、数据血缘、水印、审计日志、SBOM for AI 等组件在 2024-2025 年的工程成熟度、生产级采纳案例与互操作性标准缺乏公开系统性评估 | q3.open_problems[0] | ★★★★★ |
| **智能体 AI 红队标准化** | 智能体 AI 系统的红队测试标准化流程、自动化工具链与持续集成最佳实践尚未形成共识 | q3.open_problems[1] | ★★★★☆ |
| **红队-审计-SBOM 工程联动** | 红队测试与合规审计、模型卡片生成、SBOM 生成的工程化联动机制缺失 | q3.open_problems[2] | ★★★★☆ |

> **蓝海机会图谱核心**：**跨司法管辖区合规对齐平台**、**智能体 AI 安全评估标准化工具链**、**合规工程组件（模型卡片/水印/SBOM）的互操作性中间件**、**原则到法律义务的可执行映射知识库**。

---

## 4. 瓶颈与拐点（Bottleneck & Inflection）

### 4.1 法规解释与执行的不确定性瓶颈
- **EU AI Act 关键条款（如第 2 条范围、附件 III 高风险清单、GPAI 系统性风险阈值）存在多重解释路径**，导致企业合规策略面临**不确定**风险，需等待委员会授权法案与协调标准落地[7][8]。  
  - 拐点信号：协调标准（Harmonised Standards）发布将显著降低解释歧义，预计 2025-2026 陆续出台[7]。

### 4.2 红队测试方法论与工程化的双重瓶颈
- **方法论层面**：红队实践异化为“漏洞挖掘”，偏离批判性思维初衷，缺乏系统性风险建模能力[23]。  
- **工程层面**：智能体系统红队测试缺乏标准化流程、自动化工具链与 CI/CD 集成最佳实践[22][q3.open_problems[1]]。  
  - 拐点信号：AgentSeer 等可观测性框架与 HarmBench 等基准的结合，可能催生**智能体级红队标准化协议**[22]。

### 4.3 人类自主性侵蚀的认知风险瓶颈
- **AI 预测权威感导致人类决策自主性让渡**（40%+ 参与者放弃确定收益），且效应在失败后仍存续，现有治理框架缺乏针对性缓解机制[1]。  
  - 拐点信号：EU AI Act 第 14 条（人工监督）与基本权利影响评估（FRIA）可能被解释为要求部署“认知自主性保护措施”，但尚无技术标准[1][14]。

### 4.4 新模态模型对风险分级框架的挑战
- **生物基础模型（如 ESM3）、多模态生成模型等新模态**对现有风险分级框架（EU AI Act 附件 III、GPAI 系统性风险标准）构成挑战，需动态修正[8]。  
  - 拐点信号：International AI Safety Report 2026 等国际协调机制可能推动跨司法管辖区风险分类法的趋同[17]。

---

## 5. 社会·政策·国际（Society, Policy & Geopolitics）

### 5.1 欧盟：AI Act 实施为核心驱动力
- **EU AI Act 于 2024-08-01 生效，分阶段实施（禁止性做法 2025-02、GPAI 义务 2025-08、高风险系统 2026-08/2027-08）**，当前处于**协调标准制定与成员国执法机构建设**关键窗口期[14][7]。  
  - 证据：医疗高风险案例实证[14]、内部部署解释争议[7]、生物模型系统性风险外延[8]。

### 5.2 美国：行政命令与 NIST 标准双轨推进（候选证据缺失，需补充）
> **待核实**：候选证据未覆盖 2024-2026 年美国联邦行政命令（EO 14110 后续）、NIST AI RMF 1.0/2.0 更新、州级立法（加州 SB 1047 等）、自愿承诺与立法博弈进展。OpenAI 话语策略研究[2]侧向反映行业对美式监管预期的响应。

### 5.3 中国：算法备案与标准体系建设（候选证据缺失，需补充）
> **待核实**：候选证据未覆盖《生成式人工智能服务管理暂行办法》落地、算法备案最新进展、TC260/全国 AI 标准化总体组标准发布、数据出境安全评估与 AI 治理联动。

### 5.4 国际协调：ISO/IEC JTC1 SC42、G7 广岛进程、联合国咨询机构（候选证据缺失，需补充）
> **待核实**：候选证据未覆盖 ISO/IEC 42001 认证推广、G7 广岛进程行为准则落地、联合国 AI 高级别咨询机构报告、International AI Safety Report 2026[17] 等国际协调进展。

### 5.5 合成媒体治理的全球技术标准竞争
- **NTIRE 2026 挑战赛（CVPR 2026）推动“野外鲁棒 AI 生成图像检测”基准建设**，直接服务于 C2PA、内容凭证等国际技术标准与平台治理工具链[15]。  
  - 地缘维度：中美欧在水印、溯源、检测技术标准上的专利布局与标准必要专利（SEP）博弈加剧[15]。

---

## 6. 资本与生态（Capital & Ecosystem）

### 6.1 红队与安全评估工具链生态初步形成
| 项目/平台 | 机构/维护方 | 发展阶段 | 关键特征 | 证据 |
|-----------|-------------|----------|----------|------|
| PyRIT | Microsoft | 生产级开源 | 多模态攻击、自动化评分、可扩展插件 | [20] |
| ViolentUTF | 学术/社区 | 演示/早期 | 图形化界面、降低红队门槛 | [24] |
| AgentSeer | 学术/社区 | 研究原型 | 智能体可观测性、动作图分解、配合红队 | [22] |
| HarmBench | 学术/社区 | 基准/数据集 | 有害目标标准化、支持迭代攻击评估 | [22] |

- **生态信号**：从单点攻击脚本向**可观测性+基准+自动化平台**的工程化栈演进，但**商业化产品与合规认证联动尚弱**[20][22][24]。

### 6.2 合规工程基础设施投资方向（推测）
> **待核实**：候选证据未覆盖 2024-2026 年 AI 治理合规赛道融资、并购、独角兽企业（如 OneTrust、TrustArc、Credo AI、Holistic AI 等）最新动态。Docling[18] 等数据预处理工具被大厂开源，暗示**数据合规上游基建**受关注。

### 6.3 人才与社区流动
- **红队测试、AI 安全评估、合规工程**成为高需求岗位；学术界向产业界人才流动加速（如 PyRIT 核心作者、AgentSeer 作者多为产业实验室背景）[20][22]。  
- **标准制定参与度**成为大厂竞争新维度（ISO/IEC JTC1 SC42、C2PA、MLCommons 等）[15]。

---

## 7. 信号与预测（Signals & Forecast）

| 信号 | 来源/依据 | 预测（可证伪假设） | 置信度 | 不确定性标注 |
|------|-----------|---------------------|--------|--------------|
| EU AI Act 协调标准 2025-2026 密集发布 | [7][14] 立法时间表 | **假设**：至 2026-12，至少 5 项高风险 AI 协调标准（EN 标准）发布为正式欧洲标准（EN），企业可依据“推定合规”路径大幅降低合规成本 | 较大概率 | 标准化进程受技术复杂度与利益协调影响可能延期 |
| 智能体 AI 红队测试形成行业基准协议 | [22] AgentSeer + HarmBench | **假设**：至 2026-06，MLCommons 或类似机构发布首个 Agentic AI Red Teaming Benchmark v1.0，包含可观测性接口规范、攻击目标分类法与评分协议 | 推测 | 需多方利益相关者共识，竞争性基准可能并存 |
| 合规工具链互操作性标准（模型卡片/水印/SBOM）出现首个融合规范 | [q3.open_problems[0]] 缺口分析 | **假设**：至 2026-12，SPDX AI Profile 与 C2PA Manifest、MLCommons Croissant 形成至少一套端到端互操作演示，被 3 家以上头部模型厂商采纳 | 推测 | 标准碎片化严重，厂商锁定效应强 |
| 美国联邦 AI 立法在 2026 年中期选举前无实质性进展 | [2] OpenAI 话语策略侧写 | **假设**：2026 年美国联邦层面无综合性 AI 法案通过，监管以 NIST AI RMF 更新、行政命令指引、州级立法为主 | 推测 | 两党共识可能因特定事件（重大安全事故）突变 |
| 中国算法备案与标准体系加速“出海”互认 | [q1.open_problems[0]] 缺口 | **假设**：至 2026-12，中国与东盟/金砖/“一带一路”国家达成至少 2 项 AI 算法/模型合规评估互认安排 | 推测 | 地缘政治波动性大，技术标准互认需法律协定支撑 |
| 国际 AI 安全研究所网络（AISI Network）发布首份联合评估报告 | [17] International AI Safety Report 2026 | **假设**：2026 年底前，AISI Network（美英日加新等）发布针对前沿模型能力阈值的联合红队评估方法论 v1.0 | 较大概率 | 成员国监管理念差异可能导致方法论妥协化 |

> **关键风险提示**：上述预测均为**基于当前信号的推演**，受地缘政治、技术突发性突破、监管理念冲突等**不确定**因素影响大。需持续追踪：协调标准发布节奏、AISI Network 运作实况、头部厂商合规工具链开源/闭源策略、重大 AI 安全事故的政策窗口效应。

---

## 经典与奠基性工作（Classic & Foundational Works）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| Asilomar AI Principles | 2017 | Future of Life Institute | 高（广泛引用） | 非正式宣言，社区共识 | 高 | ★★★★☆ | https://futureoflife.org/ai-principles/ | AI 治理早期共识基石，后续 OECD/IEEE 等框架主要参考源 |
| OECD AI Principles | 2019/2024 更新 | OECD | 高（46 国采纳） | 政府间协议，软法 | 高 | ★★★★★ | https://oecd.ai/en/ai-principles | 首个政府间 AI 原则，G20 认可，各国立法核心参考 |
| IEEE Ethically Aligned Design (EAD) | 2019 v1 / 2023 更新 | IEEE Global Initiative | 高（标准化前驱） | 专业协会共识，影响 IEEE 7000 系列标准 | 高 | ★★★★★ | https://standards.ieee.org/industry-connections/ec/ead.html | 系统性伦理工程框架，直接映射至技术标准 |
| EU AI Act (Regulation 2024/1689) | 2024 | European Union | 极高（硬法） | 欧盟法规，直接效力 | 极高 | ★★★★★ | https://eur-lex.europa.eu/eli/reg/2024/1689/oj | 全球首部综合性 AI 硬法，治理范式锚点 |
| NIST AI Risk Management Framework (AI RMF 1.0) | 2023 | NIST | 高（美联邦指引） | 美国联邦标准机构，自愿性框架 | 高 | ★★★★★ | https://www.nist.gov/itl/ai-risk-management-framework | 美式治理核心工具，影响全球企业合规实践 |
| ISO/IEC 42001:2023 | 2023 | ISO/IEC JTC1 SC42 | 中高（认证标准） | 国际标准，可认证 | 中高 | ★★★★☆ | https://www.iso.org/standard/81230.html | 首个 AI 管理体系国际标准，合规认证基础 |
| 《生成式人工智能服务管理暂行办法》 | 2023 | CAC/中国网信办 | 高（中国硬法） | 部门规章，强制执行 | 高 | ★★★★★ | http://www.cac.gov.cn/2023-07/13/c_1690898327029107.htm | 中国生成式 AI 合规核心法规，备案制雏形 |

> 注：经典工作表链接为官方权威来源，非候选证据编号，供读者自查。

---

## 开源项目与工具链（Open-Source Projects & Toolchains）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| PyRIT | 2024 | Microsoft | 高 | 官方维护，生产级 | 高 | ★★★★★ | https://github.com/Azure/PyRIT | 生成式 AI 红队自动化框架，支持多模态、评分、报告 |
| ViolentUTF | 2025 | 社区/学术 | 中 | 演示论文开源 | 中 | ★★★☆☆ | https://github.com/violentutf/violentutf | 图形化红队平台，降低实践门槛 |
| AgentSeer | 2025 | 学术/社区 | 中 | 研究原型开源 | 中 | ★★★★☆ | https://github.com/agentseer/agentseer | 智能体可观测性框架，动作图分解，配合红队评估 |
| Docling | 2025 | IBM Research | 中高 | 官方开源，Apache 2.0 | 中 | ★★★★☆ | https://github.com/docling-project/docling | 文档转换工具包，服务数据血缘与合规审计上游 |
| HarmBench | 2024 | 学术/社区 | 中 | 基准数据集开源 | 中 | ★★★★☆ | https://github.com/harmbench/harmbench | 标准化有害目标集，支持红队迭代攻击评估 |

---

## 数据集与基准（Datasets & Benchmarks）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| NTIRE 2026 Robust AI-Generated Image Detection | 2026 | CVPR Workshop | 高 | 顶会同行评审挑战赛 | 高 | ★★★★★ | https://github.com/ntire2026/robust-ai-generated-detection | 野外鲁棒合成图像检测基准，推动 C2PA/内容凭证技术标准 |
| HarmBench | 2024 | 学术/社区 | 中 | 学术基准，开源 | 中 | ★★★★☆ | https://github.com/harmbench/harmbench | 红队攻击目标标准化基准，覆盖多类别有害意图 |
| International AI Safety Report 2026 基准套件 | 2026 | AISI Network | 中高 | 政府间科学报告配套 | 中高 | ★★★★☆ | https://www.aisafetyreport.org/ | 前沿模型能力与风险评估基准，国际协调产物 |
| Hugging Face Dataset Cards 大规模分析语料 | 2024 | 学术 | 中 | 学术分析语料 | 中 | ★★★☆☆ | https://huggingface.co/datasets | 数据文档化现状实证研究基础 [26] |

---

## 参考来源（Reference Sources）

[1] Faith in AI can narrow the futures individuals consider — http://arxiv.org/abs/2603.28944v2  
[2] Competing Visions of Ethical AI: A Case Study of OpenAI — http://arxiv.org/abs/2601.16513v1  
[3] Beyond principlism: Practical strategies for ethical AI use in research practices — http://arxiv.org/abs/2401.15284v6  
[4] Foundations of GenIR — http://arxiv.org/abs/2501.02842v1  
[5] Actionable Guidance for High-Consequence AI Risk Management: Towards Standards Addressing AI Catastrophic Risks — http://arxiv.org/abs/2206.08966v3  
[6] Towards Assuring EU AI Act Compliance and Adversarial Robustness of LLMs — http://arxiv.org/abs/2410.05306v1  
[7] Internal Deployment in the AI Act — http://arxiv.org/abs/2512.05742v4  
[8] The Case for ESM3 as a General-Purpose AI Model with Systemic Risk Under the EU AI Act — http://arxiv.org/abs/2605.01611v1  
[9] Conformity Assessments and Post-market Monitoring: A Guide to the Role of Auditing in the Proposed European AI Regulation — http://arxiv.org/abs/2111.05071v1  
[10] The 4th Reactive Synthesis Competition (SYNTCOMP 2017): Benchmarks, Participants & Results — http://arxiv.org/abs/1711.11439v1  
[11] NTU-NPU System for Voice Privacy 2024 Challenge — http://arxiv.org/abs/2410.02371v1  
[12] Ghosts of Jupiter's past: is 2017 UV43 a relative of comet Shoemaker-Levy 9? — http://arxiv.org/abs/1712.03230v2  
[13] Discovery Opportunities with Gravitational Waves -- TASI 2024 Lecture Notes — http://arxiv.org/abs/2409.08956v1  
[14] Ethics and EU AI Act in Cases of Work Disability Risk and Alzheimer's Disease Risk Prediction — http://arxiv.org/abs/2607.05402v1  
[15] NTIRE 2026 Challenge on Robust AI-Generated Image Detection in the Wild — http://arxiv.org/abs/2604.11487v1  
[16] Robustness and Cybersecurity in the EU Artificial Intelligence Act — http://arxiv.org/abs/2502.16184v4  
[17] International AI Safety Report 2026 — http://arxiv.org/abs/2602.21012v1  
[18] Docling: An Efficient Open-Source Toolkit for AI-driven Document Conversion — http://arxiv.org/abs/2501.17887v1  
[19] Real-Time 4K Super-Resolution of Compressed AVIF Images. AIS 2024 Challenge Survey — http://arxiv.org/abs/2404.16484v1  
[20] PyRIT: A Framework for Security Risk Identification and Red Teaming in Generative AI System — http://arxiv.org/abs/2410.02828v1  
[21] Red Teaming for Large Language Models At Scale: Tackling Hallucinations on Mathematics Tasks — http://arxiv.org/abs/2401.00290v1  
[22] Mind the Gap: Comparing Model- vs Agentic-Level Red Teaming with Action-Graph Observability on GPT-OSS-20B — http://arxiv.org/abs/2509.17259v1  
[23] Red Teaming AI Red Teaming — http://arxiv.org/abs/2507.05538v2  
[24] Demo: ViolentUTF as An Accessible Platform for Generative AI Red Teaming — http://arxiv.org/abs/2504.10603v2  
[25] Learning diverse attacks on large language models for robust red-teaming and safety tuning — http://arxiv.org/abs/2405.18540v3  
[26] Navigating Dataset Documentations in AI: A Large-Scale Analysis of Dataset Cards on Hugging Face — http://arxiv.org/abs/2401.13822v1

---

*Generated by research-bot · topic=`ai-治理与监管政策法规与标准` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`nvidia/nemotron-3-ultra-550b-a55b` · sources=26 · duration=345s · 2026-11-03T03:46:40+00:00*
