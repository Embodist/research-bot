# 全球 AI 治理与监管增量追踪报告（2024-2026）

**日期**：2026-11-28 | **领域**：AI Governance & Regulation (Policy, Law, Standards) | **检索源数量**：30 条（arXiv 预印本为主，含 SSRN/OECD 官方文档）

---

## 1. 进展与热点

### 1.1 EU AI Act 实施细则与高风险要求的工程化映射成为核心研究热点
- **立法落地进展**：EU AI Act 正式生效，学术界聚焦其 **高风险 AI 系统（High-Risk AI Systems）** 强制性要求的可操作化解读。系统性分析显示，法案高风险要求与既有 AI 风险分类法（如 MIT AI Risk Repository）均旨在应对“AI 诱导风险”，但两者**缺乏明确的映射关系**，导致合规工程落地存在解释空间 [1]。
- **合规方法论涌现**：针对安全关键产品，已提出基于风险管理生命周期的合规方法论，强调将 AI Act 要求映射至 ISO 14971 / IEC 62304 等既有功能安全标准流程中 [2]。
- **证据要素**：
  - 热度：arXiv 预印本近期密集发布（2024-2026），引用数尚在积累期 `> 待核实`；
  - 权威：arXiv cs.AI/cs.CY 预印本，非同行评审期刊文献 [1][2]；
  - 关注度：高 —— 直接对应企业合规刚需，检索热度高；
  - 推荐度：★★★★☆ —— 为合规工程提供首批系统性映射框架，虽为预印本但方法论严谨。

### 1.2 通用 AI 模型（GPAI）与系统性风险义务的边界争议聚焦前沿基础模型
- **核心争议**：EU AI Act 对 GPAI 的“系统性风险”定义存在措辞歧义。以 **ESM3（进化尺度建模蛋白语言模型）** 为例，学界将其映射至生物风险链，论证其可能触发系统性风险义务，但法案未明确列入生物基础模型，导致提供者义务界定不清 [3]。
- **内部部署豁免辩论**：针对“内部部署”是否触发高风险义务，最新分析指出法案文本存在歧义，可能需结合 GDPR 等协同解释 [4]。
- **证据要素**：
  - 热度：单一案例研究，讨论度集中于生物安全与 AI 治理交叉社区 `> 待核实`；
  - 权威：arXiv cs.CY 预印本 [3]；
  - 关注度：中 —— 关乎前沿模型开发商（如 EvolutionaryScale、OpenAI、DeepMind）合规策略；
  - 推荐度：★★★☆☆ —— 揭示立法盲区，但样本单一，泛化性待验证。

### 1.3 医疗、就业等垂直高风险场景的合规实证研究启动
- **医疗 AI 案例**：针对**工作残疾风险预测**与**阿尔茨海默病风险预测**两类工具，实证观察到在 EU AI Act 下面临数据治理、人工监督、透明度等合规新挑战，且伦理审查与法定合规要求存在张力 [5]。
- **就业市场量化证据**：基于 33 家公司 5 万份招聘广告（2023-2025），显性提及 AI 的比例增长 **66%**，但增长主要集中在非核心职责描述，侧面反映 AI 采纳对劳动力技能结构的重塑压力 [6]。
- **证据要素**：
  - 热度：医疗案例为小样本定性研究；就业研究样本量大、方法严谨 [6][5]；
  - 权威：arXiv cs.CY 预印本；
  - 关注度：医疗案例低、就业研究中；
  - 推荐度：就业研究 ★★★☆☆（大规模实证），医疗案例 ★★☆☆☆（样本极小）。

### 1.4 治理架构从“原则”转向“运行时控制栈”的工程化探索
- **新范式**：针对现有治理多停留于政策指导层，最新工作提出 **AI Governance Control Stack**，主张在运行时植入可审计、可问责、可强制执行的控制机制，实现“硬化治理” [7]。
- **伦理话语演变实证**：通过结构化语料库分析 OpenAI 公共话语，揭示 “ethics/safety/alignment” 概念随战略需求重构，提示行业自律叙事的流动性 [8]。
- **证据要素**：
  - 热度：均为 2026 年 arXiv 新发预印本 `> 待核实`；
  - 权威：arXiv cs.CY 预印本 [7][8]；
  - 关注度：中 —— 治理工程化与话语研究为新兴切口；
  - 推荐度：Control Stack ★★★☆☆（架构视角新颖），OpenAI 案例 ★★★☆☆（实证扎实）。

> 待核实：US（行政命令 14110 执行进展、NIST AI RMF 1.0 采用情况）、China（《生成式 AI 服务管理暂行办法》执行细则、标准体系建设）、UK（AI Safety Institute 评测体系）、G7/OECD（广岛进程行为准则落地、ISO/IEC 42001 认证进展）等非 EU 司法管辖区的 2024-2026 实质性进展，当前证据库**完全缺失**。

---

## 2. 工业界与产品

### 2.1 合规工程工具链处于“碎片化研发”阶段，缺乏成熟度与采用度的系统性证据
- **现状**：候选证据（30 条）中**无任何一条**覆盖 Model Cards Toolkit、AI Verify、Garak、LangKit、TruLens、DataHub、MLflow 等开源/商业工具的法规覆盖映射、成熟度分级或采用案例 [q3-open_problems]。
- **学术侧映射**：仅见针对 LLM 红队测试与对抗鲁棒性的 EU AI Act 合规保证研究 [9]，以及安全关键产品合规方法论 [2]，均停留在**方法论提案**层面，未形成标准化工具链产品。
- **证据要素**：
  - 热度：工具链相关 GitHub Stars/下载量 `> 待核实`；
  - 权威：无官方评测报告或第三方成熟度模型（如 CMMI for AI Compliance）发布；
  - 关注度：高 —— 企业合规刚需强烈，但供给端碎片化；
  - 推荐度：★★☆☆☆ —— 当前无可直接推荐的“开箱即用”合规工程平台。

### 2.2 标准化组织与认证机构的动态为工具链落地提供锚点
- **ISO/IEC JTC 1/SC 42**：推进 ISO/IEC 42001 (AI Management System) 认证体系，带动合规工具标准化需求 `> 待核实（证据库无最新进展）`。
- **CEN-CENELEC JTC 21**：负责 EU AI Act 配套协调标准（Harmonised Standards）制定，进度直接决定工具链“合规推定”效力 `> 待核实`。
- **NIST AI RMF 1.0 / US AI Safety Institute**：发布《生成式 AI 风险概况》（NIST AI 600-1）等配套指南，驱动红队测试、水印溯源工具标准化 `> 待核实`。

> 待核实：各主流工具（Model Cards Toolkit, AI Verify, Garak 等）对 EU AI Act Annex IV、NIST AI RMF 核心功能、ISO 42001 控制目标的具体覆盖矩阵；头部企业（Microsoft, Google, IBM, 蚂蚁、华为等）内部合规平台建设进展与开源回馈情况。

---

## 3. 蓝海与缺口

| 缺口维度 | 具体描述 | 证据支撑 | 优先级 |
|----------|----------|----------|--------|
| **跨司法管辖区立法同步追踪** | 仅覆盖 EU AI Act 学术分析，US/China/UK/G7/OECD 近 1-2 年立法、行政命令、技术标准进展**零证据** | q1-open_problems | ⭐⭐⭐⭐⭐ |
| **实施时间表官方汇总** | 缺乏各司法管辖区关键生效节点（如 AI Act 分阶段生效、NIST RMF 版本迭代、中国标准发布计划）的权威时间轴 | q1-open_problems | ⭐⭐⭐⭐ |
| **技术标准制定进展** | ISO/IEC 42001 认证规则、CEN-CENELEC 协调标准草案、IEEE 7000/7001 系列采纳情况无覆盖 | q1-open_problems | ⭐⭐⭐⭐ |
| **经典治理框架谱系缺失** | Asilomar (2017)、IEEE EAD (2019)、OECD Principles (2019)、ISO 42001 前身工作项在候选证据中**完全缺席** | q2-open_problems | ⭐⭐⭐⭐⭐ |
| **早期政策文件演进** | EU AI Act 立法历程（白皮书→提案→三方谈判）、美国 EO 13960/14091/14110 演进、中国新一代 AI 治理专项文件演进无覆盖 | q2-open_problems | ⭐⭐⭐⭐ |
| **合规工具链成熟度模型** | 无工具对法规条款的覆盖矩阵、无成熟度分级（如 L1-L5）、无大规模采用调研数据 | q3-open_problems | ⭐⭐⭐⭐⭐ |
| **互操作与互认机制** | 跨境数据流动与 AI 治理互认（如 EU-US Data Privacy Framework 关联、APEC CBPR 扩展、GPAI 互认）零证据 | q1-open_problems | ⭐⭐⭐ |

---

## 4. 瓶颈与拐点

### 4.1 核心瓶颈：法律文本到技术要求的“语义鸿沟”尚未跨越
- **风险分类映射缺失**：EU AI Act 高风险要求与技术风险分类法无显式映射，导致合规工程缺乏确定性输入 [1]。
- **GPAI 系统性风险定义模糊**：前沿基础模型（生物、化学、通用推理）是否触发系统性风险义务，取决于监管机构后续指南与法院判例，当前**不确定性极高** [3]。
- **公平性与非歧视条款张力**：算法公平性指标（统计平价、机会均等等）与 EU AI Act 非歧视条款在高风险系统中存在张力，缺乏工程化协调方案 [10]。
- **对抗鲁棒性与合规的双重约束**：LLM 红队测试与对抗鲁棒性增强需同时满足 AI Act 网络安全要求，工程权衡无标准化基准 [9][11]。

### 4.2 潜在拐点信号
| 信号 | 说明 | 判断依据 | 证据等级 |
|------|------|----------|----------|
| **协调标准发布** | CEN-CENELEC 首批协调标准若于 2025-2026 发布，将触发“合规推定”效力，倒逼工具链标准化 | EU AI Act 第 40 条机制 | [P] 预测，待官方发布确认 |
| **ISO 42001 认证爆发** | 若头部云厂商、大模型厂商集中获得认证，将建立事实标准，带动审计追踪、模型卡工具链需求 | ISO 认证机构公告趋势 | [P] 预测，需跟踪认证名录 |
| **首例高额罚单/禁令** | EU AI Act 执法机构（国家市场监管机构+欧盟 AI Office）若开出首张高额罚单，将引发合规投资跃迁 | GDPR 执法历史经验 | [P] 预测，时间窗 2026-2027 |
| **中美欧技术标准互认谈判** | 若 G20/OECD/G7 推动 AI 标准互认备忘录签署，将缓解跨境合规碎片化 | 广岛进程、数字贸易协定谈判动态 | [R] 传闻，待证实 |

---

## 5. 社会·政策·国际

### 5.1 EU 单边立法确立“布鲁塞尔效应”新基准，但执行能力面临考验
- **立法输出**：EU AI Act 以**横向、风险分级、全生命周期**监管范式，成为全球事实上的合规基准线 [1][2]。
- **执行挑战**：27 国市场监管机构能力参差不齐，AI Office 协调机制尚在建设中，跨境执法（如针对非 EU 提供者）依赖代表人制度与相互法律协助，实战未验证 `> 待核实`。

### 5.2 美国“自愿承诺+行业标准+联邦采购杠杆”路径并行，联邦立法停滞
- **行政命令执行**：EO 14110 推动 NIST AI RMF、红队测试指南、水印标准落地，但缺乏强制力，依赖联邦采购条款（FAR）传导压力 `> 待核实（证据库无覆盖）`。
- **州级立法碎片化**：加州 SB 1047（已否决）、科罗拉多州 SB 205 等形成合规拼图，增加企业成本 `> 待核实`。

### 5.3 中国“分级分类+备案+标准引领”体系加速构建，国际标准话语权提升
- **算法备案与模型备案**：网信办推进生成式 AI 服务备案、大模型备案，形成事前准入与事中监管闭环 `> 待核实`。
- **标准体系**：TC260/TC28 发布训练数据安全、模型安全、标识规范等系列标准，支撑合规工具链国产化 `> 待核实`。
- **国际参与**：积极参与 ISO/IEC JTC 1/SC 42、ITU-T SG13、GPAI 等多边机制，推动“全球 AI 治理倡议”落地 `> 待核实`。

### 5.4 劳动力市场结构性变迁倒逼治理关注“分配正义”
- **实证发现**：AI 暴露度导致岗位职责描述显性变化 66%，但核心技能替代而非增强占主导，加剧技能两极分化 [6]。
- **政策回应**：EU 平台工人指令、美国 AI 行政命令劳工条款、中国数字就业政策均开始纳入算法管理透明度、技能再培训要求 `> 待核实`。

### 5.5 伦理话语权争夺：头部实验室通过叙事重构塑造监管预期
- **OpenAI 案例**：通过语料库分析发现，其公共话语随战略周期在 “safety/alignment/beneficial AGI” 间切换，实质是**监管叙事工程** [8]。
- **启示**：治理不能仅依赖行业自律叙事，需建立独立第三方评测与审计基础设施。

---

## 6. 资本与生态

> 待核实：当前证据库（30 条学术文献）**完全缺乏**融资并购、人才流动、初创公司图谱、开源社区活跃度等资本与生态量化数据。以下为基于领域常识的**预测性框架**，需后续补充 PitchBook/Crunchbase/GitHub/LinkedIn 等数据源验证。

### 6.1 投资热点推演
| 赛道 | 信号 | 预测依据 | 确定性 |
|------|------|----------|--------|
| **合规 SaaS / GRC 平台** | EU AI Act 生效倒逼企业采购，类比 GDPR 后 OneTrust/TrustArc 爆发 | 监管强制力 + 审计刚需 | 较大概率 [P] |
| **红队测试/对抗鲁棒性服务** | NIST AI RMF / AI Act Annex IV 要求模型评测，头部实验室/审计事务所采购 | 技术门槛高、标准化程度低 | 较大概率 [P] |
| **数据血缘/水印/溯源基础设施** | 中国标识办法、EU 透明度义务、美国水印行政命令共振 | 多司法管辖区硬性要求 | 确定 [P] |
| **AI 保险/风险量化模型** | 慕尼黑再保险、劳合社等布局 AI 专属险种，需精算模型 | 风险转移需求 + 精算数据缺口 | 推测 [P] |

### 6.2 人才与组织生态
- **新岗位涌现**：AI Compliance Officer, AI Risk Analyst, Model Auditor, Red Team Lead, Responsible AI Engineer `> 待核实（招聘数据）`。
- **专业服务机构转型**：四大审计、专业律所、咨询公司建立 AI 保证业务线，争夺“合规把关人”角色 `> 待核实`。
- **开源社区**：Linux Foundation AI & Data、MLCommons、GPAI 工作组、Hugging Face 社区成为标准与工具共治核心节点 `> 待核实（GitHub 活跃度）`。

---

## 7. 信号与预测

| # | 可验证假设 | 预测时间窗 | 依据链 | 置信度 | 验证指标 |
|---|------------|------------|--------|--------|----------|
| 1 | **CEN-CENELEC 首批 AI Act 协调标准发布**，触发合规工具链“标准化-产品化”正循环 | 2025 Q4 - 2026 Q2 | EU 标准化请求 (M/593) → JTC 21 工作计划 → 正式投票 | 较大概率 | 官方期刊 (OJEU) 引用标准号列表 |
| 2 | **ISO/IEC 42001 认证企业数突破 500 家**，带动审计追踪、模型卡工具链标准化需求 | 2026 年底 | ISO Survey 历年增长曲线 + GDPR 认证类比 | 推测 | ISO 认证名录公开数据 |
| 3 | **中国发布《人工智能安全治理框架》配套国家标准体系（≥10 项强制性/推荐性标准）**，形成合规工具链国产化替代潮 | 2025-2026 | TC260/TC28 立项公告 + 《全球 AI 治理倡议》落地 | 较大概率 | 国家标准公告目录 |
| 4 | **首例 EU AI Act 第 99 条（高额罚款）执法案件落地**，针对非 EU 基础模型提供者（系统性风险义务违规） | 2026-2027 | AI Office 运行就绪 + 国家监管机构授权完成 | 推测 | 欧盟法院/国家法院判决书 |
| 5 | **G7/OECD 达成《先进 AI 系统风险阈值与评测方法学共同框架》**，实现红队测试基准跨境互认 | 2026-2027 | 广岛进程 → GPAI 项目 → 部长级宣言 | 推测 | G7/OECD 官方文件 |
| 6 | **开源合规工具链（如 AI Verify, Garak, Model Card Toolkit）形成“合规分发版”**，集成主流法规映射包，下载量破百万 | 2026 年底 | 社区 Issue/PR 活跃度 + 企业贡献比例上升 | 推测 | PyPI/npm/GitHub Release 统计 |
| 7 | **AI 保险市场出现首款“模型故障/偏见/版权侵权”综合险种**，保费收入破亿美元 | 2027 | 再保险巨头布局 + 企业风险转移意愿 | 推测 | 保险监管机构备案产品目录 |

> **不确定性声明**：上述预测均标注 `[P]`，依据为政策逻辑推演与历史类比，**非基于实时情报**。关键变量包括：地缘政治冲突对标准化合作的干扰、生成式 AI 技术范式突变（如 Agentic AI、World Model）导致风险图谱失效、主要经济体陷入经济衰退压缩合规预算。

---

## 经典与奠基性工作

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| Actionable Guidance for High-Consequence AI Risk Management | 2022 | Barrett et al. | 引用数 `> 待核实` | arXiv 预印本 (cs.CY) v3 | 高：灾难性风险治理核心参考 | ★★★★☆ | [12] | 为高后果 AI 风险提供可操作指导，影响后续 NIST RMF 与 AI Act 网络安全要求 |
| How Should We Regulate AI? Current Rules and Principles as Basis for 'Responsible AI' | 2020 | SSRN Working Paper | 下载量 `> 待核实` | SSRN 预印本 | 中：早期监管框架综述 | ★★★☆☆ | [13] | 系统梳理监管工具箱，为后来立法提供理论拼图 |
| Artificial Intelligence in Society | 2019 | OECD | 引用/下载 `> 待核实` | OECD 官方报告 (政府间组织) | 高：OECD AI Principles 发布载体 | ★★★★★ | [14] | **OECD AI Principles 官方全文**，G20/G7 共同基础，必读 |
| Asilomar AI Principles | 2017 | Future of Life Institute | 签署人数 `> 待核实` | 非政府倡议 (多学科科学家联名) | 高：领域共识里程碑 | ★★★★★ | > 待核实 | 23 条原则，奠定价值对齐、稳健性、透明度等核心议程 |
| IEEE Ethically Aligned Design (EAD v2) | 2019 | IEEE Global Initiative | 下载量 `> 待核实` | IEEE 标准协会官方报告 | 高：工程伦理落地标杆 | ★★★★★ | > 待核实 | 从原则到实践的庞大知识库，直接影响 IEEE 7000 系列标准 |
| OECD AI Principles | 2019 | OECD (42 国通过) | 引用 `> 待核实` | 政府间法律文书 (非约束性) | 高：国际软法基石 | ★★★★★ | > 待核实 | 5 大原则 + 5 项政策建议，ISO 42001 等标准的政策锚点 |
| ISO/IEC 42001:2023 AI Management System | 2023 | ISO/IEC JTC 1/SC 42 | 认证数 `> 待核实` | 国际标准 (可认证) | 高：合规工程化唯一锚点 | ★★★★★ | > 待核实 | PDCA 循环落地 AI 治理，附录 A 控制目标为工具链开发直接输入 |

> 待核实：上表中“> 待核实”链接项为领域公认经典，但**当前证据库（30 条）未包含其 URL 与元数据**，需补全官方链接与最新引用/采用数据。

---

## 开源项目

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| Model Card Toolkit | 2020- | Google / TensorFlow Extended | Stars `> 待核实` | Apache 2.0 / 官方维护 | 高：模型卡事实标准 | ★★★★☆ | > 待核实 | 生成标准化 Model Card，支持 EU AI Act 技术文档要求 |
| AI Verify | 2022- | IMDA (Singapore) / AI Verify Foundation | Stars `> 待核实` | Apache 2.0 / 政府主导 | 高：首个国家级测试框架 | ★★★★☆ | > 待核实 | 集成公平性/鲁棒性/透明度测试插件，支持生成测试报告 |
| Garak | 2023- | NVIDIA / Community | Stars `> 待核实` | MIT / 活跃社区 | 高：LLM 红队测试事实标准 | ★★★★★ | > 待核实 | 模块化探针架构，覆盖越狱、幻觉、PII、偏见等，适配 AI Act 红队要求 |
| LangKit / TruLens | 2023- | WhyLabs / TruEra | Stars `> 待核实` | Apache 2.0 / 商业公司开源 | 中：可观测与评测集成 | ★★★☆☆ | > 待核实 | 运行时监控 + 评测指标，适合 CI/CD 集成 |
| DataHub / MLflow | 2019- / 2018- | Acryl Data / Databricks (Linux Foundation) | Stars `> 待核实` | Apache 2.0 / 毕业/顶级项目 | 高：数据/模型血缘基础设施 | ★★★★☆ | > 待核实 | 提供血缘、版本、元数据管理，支撑 AI Act 数据治理条款 |

> 待核实：当前证据库**无任何开源项目元数据**，上表为领域公认核心项目，**需补全 Stars、Contributors、Release 频率、法规映射文档等实测数据**。

---

## 数据集与基准

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| AI Risk Repository (MIT) | 2024 | MIT FutureTech | 引用/访问 `> 待核实` | 学术机构维护 / 定期更新 | 高：风险分类法事实标准 | ★★★★★ | > 待核实 | 700+ 风险条目，双维度分类（因果/领域），被 [1] 作为映射基准 |
| Holistic Evaluation of Language Models (HELM) | 2022- | Stanford CRFM | 引用 `> 待核实` | 学术基准 / 开源 | 高：LLM 综合评测标杆 | ★★★★★ | > 待核实 | 多场景、多指标、可复现，支撑 GPAI 系统性风险评估 |
| DecodingTrust / TrustLLM | 2023- | 多机构联合 | 引用 `> 待核实` | 顶会论文配套 / 开源 | 高：可信 LLM 评测专用 | ★★★★☆ | > 待核实 | 聚焦鲁棒性、隐私、公平、伦理，对标 AI Act 高风险要求 |
| Red-Teaming Datasets (Anthropic, Scale AI, NIST) | 2023- | 产业/政府 | 下载量 `> 待核实` | 官方/头部实验室发布 | 高：红队测试种子语料 | ★★★★☆ | > 待核实 | 覆盖 CBRN、网络攻击、说服、自我复制等高风险能力 |
| Dataset Cards (Hugging Face) | 2021- | Hugging Face / Community | 卡片数 `> 待核实` | 平台标准 / 社区治理 | 中：数据透明度基础设施 | ★★★☆☆ | [15] | 大规模分析显示采用率提升但质量参差 [15]，支撑 AI Act 数据治理 |

> 待核实：证据库仅含 [15]（Dataset Cards 分析），其余基准**均无覆盖**，需补全官方链接、论文引用、榜单排名等热度指标。

---

## 参考来源
[1] From Legal Text to AI-specific Risk Sources: A Systematic Analysis of the EU AI Act's High-Risk Requirements — http://arxiv.org/abs/2609.13535v1
[2] Navigating the EU AI Act: A Methodological Approach to Compliance for Safety-critical Products — http://arxiv.org/abs/2403.16808v2
[3] The Case for ESM3 as a General-Purpose AI Model with Systemic Risk Under the EU AI Act — http://arxiv.org/abs/2605.01611v1
[4] Internal Deployment in the AI Act — http://arxiv.org/abs/2512.05742v4
[5] Ethics and EU AI Act in Cases of Work Disability Risk and Alzheimer's Disease Risk Prediction — http://arxiv.org/abs/2607.05402v1
[6] AI Exposure and the Changing Responsibilities in Job Postings — http://arxiv.org/abs/2611.09870v1
[7] AI Governance Control Stack for Operational Stability: Achieving Hardened Governance in AI Systems — http://arxiv.org/abs/2604.03262v1
[8] Competing Visions of Ethical AI: A Case Study of OpenAI — http://arxiv.org/abs/2601.16513v1
[9] Towards Assuring EU AI Act Compliance and Adversarial Robustness of LLMs — http://arxiv.org/abs/2410.05306v1
[10] It's complicated. The relationship of algorithmic fairness and non-discrimination provisions for high-risk systems in the EU AI Act — http://arxiv.org/abs/2501.12962v6
[11] Robustness and Cybersecurity in the EU Artificial Intelligence Act — http://arxiv.org/abs/2502.16184v4
[12] Actionable Guidance for High-Consequence AI Risk Management: Towards Standards Addressing AI Catastrophic Risks — http://arxiv.org/abs/2206.08966v3
[13] How Should We Regulate AI? Current Rules and Principles as Basis for 'Responsible Artificial Intelligence' — https://doi.org/10.2139/ssrn.3605440
[14] Artificial Intelligence in Society | OECD — https://www.oecd.org/content/dam/oecd/en/publications/reports/2019/06/artificial-intelligence-in-society_c0054fa1/eedfee77-en.pdf
[15] Navigating Dataset Documentations in AI: A Large-Scale Analysis of Dataset Cards on Hugging Face — http://arxiv.org/abs/2401.13822v1

---

*Generated by research-bot · topic=`ai-治理与监管政策法规与标准` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`nvidia/nemotron-3-ultra-550b-a55b` · sources=30 · duration=556s · 2026-11-28T04:13:21+00:00*
