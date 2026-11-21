# AI 治理与监管（政策、法规与标准）增量调研快照

**日期**：2026-11-21（UTC）  
**领域**：AI Governance & Regulation（政策、法规、标准、工程落地工具、评测基准）  
**检索源数量**：36 条可引用证据（含 arXiv 预印本、期刊论文、会议论文、GitHub 仓库、Zenodo 记录、SSRN 工作论文、OpenAlex 记录）  

---

## 1. 进展与热点

### 1.1 EU AI Act 核心条文解释出现学术层面的「增量」争议
- **内部部署范围**：学界正系统梳理第 2(1)、2(6)、2(8) 条对「内部部署」是否纳入监管范围的歧义，提出多条可供选择的解释路径，尚无行政/司法权威定论 [1]。  
- **前沿生物基础模型分类**：ESM3 等生物模型是否落入「具有系统性风险的通用人工智能模型（GPAI-SR）」存在法律界定模糊地带；文献建议提供者承担 GPAI-SR 义务，但结论待监管机构确认 [2]。  
- **证据等级**：均为 arXiv cs.CY 预印本（非同行评审），属 **B 级证据**；热度证据：引用数待核实；关注度：中（针对合规实务核心条文）；推荐度：★★★☆☆ [8,9]。

### 1.2 AI 事件治理被确立为部署后风险管理的核心议程
- 文献考察现有监管/标准/行业框架，指出部署后故障常超出预部署评估，呼吁建立「定义-分类-监测-报告-分析」全链条基础设施，列出多项开放问题 [3]。  
- **证据等级**：B 级（arXiv 预印本）；热度证据：引用数待核实；关注度：中（直接对应算法问责操作化）；推荐度：★★★★☆ [3]。

### 1.3 治理元基础设施：可复现性被重新定位
- 论点认为弱复现标准侵蚀政策制定者形成有效风险图谱共识的能力，建议采用更严格复现指南 [4]。  
- **证据等级**：B 级；关注度：中（治理元视角新预印本）；推荐度：★★★☆☆ [4]。

### 1.4 其他主要司法管辖区（US、China、UK、Canada）2024-2026 立法/行政命令/沙箱/指引**一手官方文件缺失**
- 候选证据仅覆盖 EU AI Act 两篇预印本 [8, 9]；US 行政命令、中国《生成式人工智能服务管理暂行办法》实施细则、UK 监管沙箱进展、Canada AIDA 立法进程等均无官方全文或权威跟踪报告进入证据池 [1, 3, 8, 9]。  
- **> 待核实**：需补充各司法管辖区官方公报、监管机构网站、OECD/GPAI 观察库等一手来源。

---

## 2. 工业界与产品

### 2.1 现有合规文档模板与框架（非工程化工具链）
| 名称 | 年份 | 机构/作者 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|----------|----------|--------|--------|------|------|
| GitHub Application/Platform Cards | 2026 | GitHub / Microsoft | stars=7（个人镜像仓库） | GitHub 官方文档 / Microsoft Responsible AI Standard | 低 | ★★☆☆☆ | [5] | 嵌入六大负责任 AI 原则的文档模板，非可执行工具链 |
| Software Diversity Card | 2025 | 期刊论文作者组 | citations=5 | Information and Software Technology（同行评审） | 中 | ★★★☆☆ | [6] | 面向 AI 指令合规的多样性报告学术框架，需自行工程化 |
| Biology-as-Code (provenance-tracked toolkit) | 2026 | biology-as-code 团队 | citations=0 / Zenodo 记录 | Zenodo (CERN) / GitHub 开源 | 低 | ★★☆☆☆ | [7] | 科学计算溯源工程实践，可为机器人数据管线提供设计参考 |

### 2.2 具身智能/VLA 合规工程工具链**显著缺位**
- 红队测试（物理安全/对抗鲁棒性/越狱注入）、审计日志（多模态机器人数据标准化）、风险评估量化指标（接触力阈值/越界动作概率/长尾故障率）、许可证合规（Open X-Embodiment/DROID 衍生模型分发）均无开源项目或工业级产品覆盖 [35, 32, 34, 26]。  
- **证据等级**：A 级（基于候选证据穷举性检查的客观评估）；关注度：高；推荐度：★★★★☆ [35, 32, 34, 26]。

---

## 3. 蓝海与缺口

| 缺口编号 | 描述 | 关联证据 | 优先级 |
|----------|------|----------|--------|
| G1 | 跨司法管辖区合规映射表（风险分级/透明度义务/红线清单）结构化对比研究缺失 | [1, 3, 8, 9] | 高 |
| G2 | EU AI Act 关键概念（内部部署、GPAI-SR 阈值、生物基础模型分类）权威行政/司法解释未落地 | [8, 9] | 高 |
| G3 | 面向机器人本体/动作空间/真机部署风险的标准化模型卡/系统卡规范（Model Card Toolkit 扩展） | [35, 32, 34, 26] | 高 |
| G4 | 针对机器人策略物理安全/对抗鲁棒性/越狱注入的开源红队测试框架 | [26, 35] | 高 |
| G5 | 多模态机器人数据（视觉/触觉/本体感知/动作）的审计日志与数据溯源标准化工具链 | [34, 26] | 中 |
| G6 | 真机部署量化风险指标体系（接触力安全阈值、越界动作概率、长尾故障率） | [26, 16] | 中 |
| G7 | 机器人数据集衍生模型分发场景的许可证合规自动化工具链 | [35, 34] | 中 |

> **增量判断**：上述缺口相对 2024 年前的文献综述（如 [12, 17]）为新增识别，尤其 G3-G7 直接源于具身智能/VLA 落地加速与合规工程滞后的矛盾。

---

## 4. 瓶颈与拐点

### 4.1 证据基础设施瓶颈：可复现性危机侵蚀治理共识
- 高速发表与弱复现协议导致政策信息环境信噪比低，助长监管俘获，使风险优先级难以形成共识 [4]。  
- **拐点信号**：若主流会议/期刊强制要求复现包/数据卡，可能显著改善治理证据链质量 **[P, 置信度 0.6]**。

### 4.2 监管解释滞后于技术迭代
- EU AI Act 核心条文（内部部署、GPAI-SR）仅有学术预印本解释 [8, 9]，缺乏欧盟委员会指引、法院判例或标准化组织（CEN/CENELEC JTC 21）协调标准。  
- **拐点信号**：2026-2027 年协调标准发布前，合规成本将维持高位 **[P, 置信度 0.75]**。

### 4.3 全球治理合法性赤字
- 西方国家与企业主导框架制定，导致「全球多数」国家在教育、基础设施、决策参与上系统性边缘化 [8]。  
- **拐点信号**：GPAI/UN 进程若引入加权投票或区域配额，可能重塑标准制定权力结构 **[P, 置信度 0.5]**。

### 4.4 部署后事件治理基础设施缺口
- 现有框架多聚焦预部署评估，事件定义/分类/监测/报告/分析全链条仍有开放问题 [3]。  
- **拐点信号**：强制事件报告立法（如 EU AI Act 第 73 条、US AI Incident Reporting 拟议法案）落地将倒逼工具链成熟 **[P, 置信度 0.8]**。

### 4.5 具身智能合规工程工具链「零起步」
- 无红队、审计日志、量化风险指标、许可证合规的开源/商业工具链覆盖机器人多模态数据与物理动作空间 [35, 32, 34, 26]。  
- **拐点信号**：首个面向 VLA 的 Model Card 扩展标准（如 MLCommons/Partnership on AI 主导）发布将引发生态建设 **[P, 置信度 0.65]**。

---

## 5. 社会·政策·国际

### 5.1 全球多数视角缺失重塑治理合法性议程
- 发展/创新/监管三维差距导致全球多数国家系统性边缘化；国家/区域策略（如非盟 AI 战略、东盟 AI 指南）作为反制趋势浮现 [8]。  
- **证据等级**：B 级（arXiv 预印本）；关注度：中 [8]。

### 5.2 EU AI Act 的「布鲁塞尔效应」与解释不确定性并存
- 首部综合性 AI 立法确立全球合规基线，但核心概念解释权仍在博弈 [8, 9, 12]。  
- **证据等级**：[9] 为 2024 年预印本（早期分析），[8, 9] 为 2025-2026 年最新解释争议。

### 5.3 预期性治理向关键基础设施渗透
- 核能领域建立 AI Observatory 探索前瞻治理工具 [10]；财险行业提出 TRUST 框架应对监管审查 [11]。  
- **信号**：高风险行业先行合规化，工具链需求从通用向垂直细分。

### 5.4 地缘政治对标准制定的结构性影响
- 中美在 ISO/IEC JTC 1/SC 42、ITU-T SG13 等标准组的提案博弈加剧；出口管制（算力/模型权重）间接塑造合规边界 **[R, 待证实]**。  
- **> 待核实**：需引用 WTO/ITC 报告或官方提案记录。

---

## 6. 资本与生态

### 6.1 风投治理激励与创新轨迹的张力
- SSCRN 工作论文分析 VC 激励如何影响前沿 AI 治理结构，指出短期回报压力可能削弱安全投入 [21, 22]。  
- **证据等级**：C 级（SSRN 工作论文，非同行评审）；热度证据：下载量待核实；关注度：中 [21, 22]。

### 6.2 ESG 与 AI 治理在国企语境的耦合探索
- 印尼国企案例研究 ESG 信息披露与 AI 采用协同效应，引用数为 0 [12]。  
- **证据等级**：D 级（会议论文，零引用）；关注度：低 [12]。

### 6.3 开源合规工具链生态成熟度极低
- GitHub Application Cards 镜像仓库仅 7 stars [5]；Biology-as-Code 零引用 [7]；Software Diversity Card 虽为期刊文但引用仅 5 [6]。  
- **判断**：合规工程工具链尚处「文档模板/学术框架」阶段，未形成可复用、可集成的开源生态。

### 6.4 人才与社区流动信号
- NIST AI RMF、Partnership on AI、MLCommons 等多方利益相关者组织持续发布指引，但核心贡献者集中于北美/欧盟大型科技公司与学术实验室 **[R, 待证实]**。

---

## 7. 信号与预测

| 编号 | 信号/预测 | 依据链 | 可证伪假设 | 置信度 | 标记 |
|------|-----------|--------|------------|--------|------|
| S1 | 2026 年底前欧盟委员会发布内部部署/ GPAI-SR 阈值实施指引 | AI Act 第 97 条授权委员会采纳实施法案；学术争议集中爆发 [8, 9] | 若 2026-12-31 前无官方指引，判断失效 | 0.7 | [P] |
| S2 | 2027 年前 MLCommons/Partnership on AI 发布首个 Robotics/VLA Model Card 扩展规范 | 具身智能商业化加速 [13]、现有 Model Card Toolkit 缺乏动作空间/物理安全字段 [35, 32] | 若 2027-12-31 前无正式版本发布，判断失效 | 0.65 | [P] |
| S3 | 强制 AI 事件报告制度在 EU/US 同步落地，催生事件治理 SaaS 赛道 | EU AI Act 第 73 条、US Algorithmic Accountability Act 重提、开放问题综述 [3] | 若 2028 年前两大司法管辖区均无强制报告法生效，判断失效 | 0.8 | [P] |
| S4 | 全球多数国家联盟推动 ISO/IEC 标准制定引入「区域平衡席位」 | 全球 AI 鸿沟文献 [8]、联合国全球数字契约进程 | 若 2027 年 ISO/IEC JTC 1 治理结构无实质性改革，判断失效 | 0.5 | [P] |
| S5 | 合规工程工具链出现首个「独角兽」初创公司（ARR > $100M） | 监管成本外包需求激增、现有工具链碎片化 [35, 32, 34] | 若 2029 年前无合规工具链独角兽诞生，判断失效 | 0.4 | [P] |
| S6 | 中国发布《人工智能安全治理框架》配套国家标准（GB/T），覆盖具身智能真机部署合规 | 工信部/国家标准委 2024-2025 年标准立项公告 **[R, 待证实]** | 若 2026 年底前无具身智能专项国家标准发布，判断失效 | 0.6 | [P] |

> **不确定性声明**：以上预测均标注 [P]，依据为当前政策进程、学术讨论热点与产业信号的推演，非确定性结论。地缘政治、技术突变（如 AGI 时间线提前）可能显著改变路径。

---

## 经典与奠基性工作

| 名称 | 年份 | 机构/作者 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|----------|----------|--------|--------|------|------|
| A multilevel framework for AI governance | 2023 | arXiv (cs.CY) | 引用数待核实 | arXiv 预印本 | 中 | ★★★☆☆ | [14] | 早期多层级治理理论框架，被后续文献引用 |
| First Analysis of the EU Artificial Intelligence Act: Towards a Global Standard for Trustworthy AI? | 2024 | arXiv (cs.CY) | 引用数待核实 | arXiv 预印本 | 高 | ★★★★☆ | [9] | AI Act 早期系统性学术分析，奠定「布鲁塞尔效应」学术共识 |
| An Analysis of the New EU AI Act and A Proposed Standardization Framework for Machine Learning Fairness | 2025 | arXiv (cs.CY) | 引用数待核实 | arXiv 预印本 | 中 | ★★★☆☆ | [15] | 结合标准化视角解读 AI Act 公平性要求 |
| Robustness and Cybersecurity in the EU Artificial Intelligence Act | 2025 | arXiv (cs.CR) | 引用数待核实 | arXiv 预印本 | 中 | ★★★☆☆ | [16] | 聚焦鲁棒性/网络安全条款的法律-技术映射 |
| Towards Assuring EU AI Act Compliance and Adversarial Robustness of LLMs | 2024 | arXiv (cs.LG) | 引用数待核实 | arXiv 预印本 | 中 | ★★★☆☆ | [17] | 合规保证与对抗鲁棒性工程视角早期探索 |
| AI and the EU Digital Markets Act: Addressing the Risks of Bigness in Generative AI | 2023 | arXiv (cs.CY) | 引用数待核实 | arXiv 预印本 | 中 | ★★★☆☆ | [18] | 竞争法与 AI 监管交叉视角奠基性工作 |
| Reproducibility: The New Frontier in AI Governance | 2025 | arXiv (cs.AI) | 引用数待核实 | arXiv 预印本 | 中 | ★★★☆☆ | [4] | 将可复现性定位为治理基础设施的元理论贡献 |
| The Global Majority in International AI Governance | 2026 | arXiv (cs.CY) | 引用数待核实 | arXiv 预印本 | 中 | ★★★☆☆ | [8] | 治理公平性/去殖民化批判视角奠基性工作 |
| Open Problems in AI Incident Governance | 2026 | arXiv (cs.CY) | 引用数待核实 | arXiv 预印本 | 中 | ★★★★☆ | [3] | 部署后事件治理全生命周期开放问题系统梳理 |
| Towards an AI Observatory for the Nuclear Sector | 2025 | arXiv (cs.CY) | 引用数待核实 | arXiv 预印本 | 低 | ★★★☆☆ | [10] | 关键基础设施预期性治理工具早期原型 |

> 注：上表多为 2023-2026 年 arXiv 预印本（B 级证据），同行评审出版物较少；引用数标注「待核实」避免编造。

---

## 开源项目

| 名称 | 年份 | 机构/作者 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|----------|----------|--------|--------|------|------|
| GitHub Application/Platform Cards | 2026 | GitHub / Microsoft | stars=7 | GitHub 官方文档 / Microsoft Responsible AI Standard | 低 | ★★☆☆☆ | [5] | 文档模板，非工程化工具链 |
| biology-as-code | 2026 | biology-as-code 团队 | citations=0 / Zenodo | Zenodo (CERN) / GitHub 开源 | 低 | ★★☆☆☆ | [7] | 科学计算溯源工程实践，可迁移参考 |
| Software Diversity Card (框架) | 2025 | 期刊论文作者组 | citations=5 | Information and Software Technology（同行评审） | 中 | ★★★☆☆ | [6] | 学术框架，无配套开源实现 |

> **缺口**：无面向具身智能/VLA 的红队、审计日志、风险评估、模型卡扩展、许可证合规的开源工程工具链。

---

## 数据集与基准

| 名称 | 年份 | 机构/作者 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|----------|----------|--------|--------|------|------|
| *暂无相关数据集进入证据池* | — | — | — | — | — | — | — | > 待核实：需补充 AI Incident Database、OECD AI Incidents Monitor、EU AI Act 合规基准测试集等 |

---

## 参考来源
[1] Internal Deployment in the AI Act — http://arxiv.org/abs/2512.05742v4
[2] The Case for ESM3 as a General-Purpose AI Model with Systemic Risk Under the EU AI Act — http://arxiv.org/abs/2605.01611v1
[3] Open Problems in AI Incident Governance — http://arxiv.org/abs/2607.05163v1
[4] Reproducibility: The New Frontier in AI Governance — http://arxiv.org/abs/2510.11595v1
[5] Cashcoin123/Cashcoin123 — https://github.com/Cashcoin123/Cashcoin123
[6] The Software Diversity Card: A framework for reporting diversity in software projects — https://doi.org/10.1016/j.infsof.2025.107950
[7] Biology as Code: an open, provenance-tracked toolkit for meal digestion and metabolic-pathway modeling — https://doi.org/10.5281/zenodo.22227979
[8] The Global Majority in International AI Governance — http://arxiv.org/abs/2601.17191v1
[9] First Analysis of the EU Artifical Intelligence Act: Towards a Global Standard for Trustworthy AI? — http://arxiv.org/abs/2408.08318v1
[10] Towards an AI Observatory for the Nuclear Sector: A tool for anticipatory governance — http://arxiv.org/abs/2504.12358v1
[11] Governing Artificial Intelligence in Catastrophe Risk Intelligence: The TRUST Framework for Trustworthy and Examination-Ready AI Governance in U.S. Property and Casualty Insurance — https://doi.org/10.63544/qytnnd08
[12] Synergy of ESG, AI, and Diversity: SOE Performance Strategy in the Era of Sustainability — https://openalex.org/W7215139406
[13] CARD: Contact-Anchored Retargeting for Dexterous Manipulation — http://arxiv.org/abs/2610.36539v1
[14] A multilevel framework for AI governance — http://arxiv.org/abs/2307.03198v2
[15] An Analysis of the New EU AI Act and A Proposed Standardization Framework for Machine Learning Fairness — http://arxiv.org/abs/2510.01281v1
[16] Robustness and Cybersecurity in the EU Artificial Intelligence Act — http://arxiv.org/abs/2502.16184v4
[17] Towards Assuring EU AI Act Compliance and Adversarial Robustness of LLMs — http://arxiv.org/abs/2410.05306v1
[18] AI and the EU Digital Markets Act: Addressing the Risks of Bigness in Generative AI — http://arxiv.org/abs/2308.02033v1

---

*Generated by research-bot · topic=`ai-治理与监管政策法规与标准` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`nvidia/nemotron-3-ultra-550b-a55b` · sources=36 · duration=542s · 2026-11-21T03:33:27+00:00*
