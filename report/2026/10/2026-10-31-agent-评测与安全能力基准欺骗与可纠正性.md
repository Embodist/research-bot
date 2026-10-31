# Agent 评测与安全（能力基准、欺骗与可纠正性）深度调研报告

**日期**：2026-10-31 | **领域**：Agent Evaluation & Safety (Benchmarks, Deception, Corrigibility) | **检索源数量**：34

---

## 1. 进展与热点

### 1.1 开放多智能体系统评测基准演进：MOASEI 2026
- **核心增量**：MOASEI 第二届竞赛在 AAMAS 2026 发布技术报告，保留野火灭火、网络安全、网约车三大领域，**新增“框架开放性”野火额外赛道**，引入智能体装备状态（灭火剂容量、灭火范围）随时间动态变化的设定，标志着开放系统评测从静态环境向**动态适应性**维度扩展 [15]。
- **指标体系升级**：扩展评测指标为总任务完成数、平均任务完成时间、完成任务平均价值三大核心指标，从单一完成率转向多维效能度量，更贴近开放系统实际运营目标 [15]。
- **参与度瓶颈**：8 支队伍注册，**仅 1 支队伍（DLC 方法）提交最终参赛作品**（针对网约车赛道），采用规划与重规划解决路由问题，暴露开放多智能体基准的落地与参与门槛极高 [15]。
- **证据四维**：
  - 热度：> 待核实（参赛队伍极少，GitHub stars/下载量未披露）[15]
  - 权威：AAMAS 2026 顶会技术报告，arXiv 预印本 [15]
  - 关注度：中（基准设计创新但社区采纳度低）[15]
  - 推荐度：★★★☆☆（为开放系统基准引入动态装备约束新范式，值得关注后续采纳情况）[15]

### 1.2 评测-安全测量鸿沟的系统性框架化：EvalSafetyGap (2026)
- **核心增量**：首个系统综述 2018–2026 年 373 项研究，提出 **EvalSafetyGap 概念框架**，揭示 LLM 评测分数、奖励信号与安全指标可能提升而真实能力/对齐属性仍不确定的「评测-安全测量鸿沟」[1]。
- **方法论贡献**：构建八流证据分类法（基准有效性、污染、动态评测、LLM-as-a-judge、对抗安全测试、奖励/代理优化、机制可解释性、AI 治理），为领域提供统一分析骨架 [1]。
- **证据四维**：
  - 热度：> 待核实（2026 年最新预印本，引用数尚未积累）[1]
  - 权威：arXiv 预印本 (cs.AI)，未经同行评审，但覆盖文献极广 [1]
  - 关注度：高（系统梳理评测与安全交叉核心问题，被引潜力大）[1]
  - 推荐度：★★★★☆（权威综述框架，直接对应评测与安全交叉核心，适合作为文献综述锚点）[1]

### 1.3 Agent 基准评测复现性危机的实证审计
- **核心增量**：对 12 篇知名 LLM Agent 基准论文飞行审计发现，**同一基准、同一模型的报告结果常不一致**，且论文普遍未披露脚手架、采样设置、子集选择、评估器版本等关键复现细节 [2]。
- **工具化产出**：设计 5 字段审计模式（基准身份、哈尼斯规范、推理设置、成本报告、失败分解）与评分代码本，提供可落地的审计工具 [2]。
- **证据四维**：
  - 热度：> 待核实（2026 年预印本，社区讨论度待观察）[2]
  - 权威：arXiv 预印本 (cs.LG)，未经同行评审 [2]
  - 关注度：高（直击评测可复现性痛点，提供标准化审计范式）[2]
  - 推荐度：★★★★☆（实证方法论强，适合制定评测报告规范的直接参考）[2]

### 1.4 生产级 Agent 持续评测工程实践
- **核心增量**：首个生产环境演化 Agent 循证评测案例，利用 574 次历史运行按时间切分校准/保留期，验证真实服务数万 MAU 的分析型 Agent 上低成本重复评测可行性 [9]。
- **工程意义**：从静态离线基准转向**持续集成/持续评测 (CI/CD)** 范式，解决模型/提示词/工具链频繁迭代下的评测成本与时效性矛盾 [9]。
- **证据四维**：
  - 热度：> 待核实（单一案例研究，泛化性待验证）[9]
  - 权威：arXiv 预印本 (cs.AI)，未经同行评审 [9]
  - 关注度：中（真机生产数据稀缺，工程落地参考价值高）[9]
  - 推荐度：★★★☆☆（适合关注 CI/CD 评测管线的团队参考）[9]

### 1.5 欺骗检测基准与方法突破
- **SVC 2025 挑战赛**：首个多模态欺骗检测基准挑战赛发布，推动音视频多模态欺骗行为建模与检测标准化 [23]。
- **线性探针检测策略性欺骗**：提出利用线性探针在激活空间检测策略性欺骗行为，为可解释的欺骗检测提供新范式 [24]。
- **证据四维 (SVC 2025)**：
  - 热度：> 待核实（挑战赛首届，参赛规模未披露）[23]
  - 权威：arXiv 预印本，挑战赛官方报告 [23]
  - 关注度：中（填补多模态欺骗基准空白）[23]
  - 推荐度：★★★☆☆（多模态欺骗评测的重要起点）[23]
- **证据四维 (Linear Probes)**：
  - 热度：> 待核实（2025 预印本，引用待积累）[24]
  - 权威：arXiv 预印本 [24]
  - 关注度：中（机制可解释性视角切入欺骗检测）[24]
  - 推荐度：★★★☆☆（为可纠正性前置条件——欺骗感知提供技术路径）[24]

### 1.6 对抗鲁棒性与文本生成攻击评测
- **CheckThat! 2024 OpenFact 任务**：结合多种攻击方法生成有效对抗文本，推动对抗鲁棒性评测向自动化、组合化攻击演进 [31]。
- **证据四维**：
  - 热度：> 待核实（共享任务论文，关注度局限于社区）[31]
  - 权威：CheckThat! 2024 共享任务官方论文 [31]
  - 关注度：中（对抗评测工程化的实证）[31]
  - 推荐度：★★★☆☆（安全红队自动化评测的参考案例）[31]

### 1.7 Agent 评测领域全景分类法建立
- **核心增量**：2025 年综述提出二维分类法（评测目标 × 评测方法），梳理行为、能力、可靠性等目标与静态/动态、人工/自动方法矩阵，为新兴领域提供早期全景图 [11]。
- **证据四维**：
  - 热度：> 待核实（2025 年早期综述，引用积累中）[11]
  - 权威：arXiv 预印本 (cs.LG) [11]
  - 关注度：中（提供领域认知骨架，时效性不如 2026 新作）[11]
  - 推荐度：★★★☆☆（快速建立领域全景认知的入门综述）[11]

---

## 2. 工业界与产品

### 2.1 生产环境评测管线的工程化落地
- **增量判断**：仅有 [9] 披露单一生产级 Agent（分析型、数万 MAU）的持续评测实证，**缺乏头部厂商（OpenAI, Anthropic, Google, 国内大厂）内部评测平台、红队体系、合规发布流程的公开技术细节**。
- **透明度指数作为代理信号**：2025 Foundation Model Transparency Index [27] 发布，虽聚焦基础模型而非 Agent 专用，但其指标体系（数据、计算、部署、风险缓解等）反映工业界对**评测透明度与合规报告**的重视度上升 [27]。
- **证据四维 (生产案例 [9])**：
  - 热度：> 待核实
  - 权威：arXiv 预印本
  - 关注度：中
  - 推荐度：★★★☆☆
- **证据四维 (透明度指数 [27])**：
  - 热度：> 待核实
  - 权威：arXiv 预印本，Stanford HAI 等机构主导
  - 关注度：中（政策与合规驱动下的行业自律信号）
  - 推荐度：★★★☆☆（可作为 Agent 评测合规化的间接参考）
- **> 待核实**：主流 Agent 框架（LangChain, AutoGen, CrewAI 等）内置评测模块的采用率与效果；商业化评测 SaaS（如 Patronus AI, Galileo, Braintrust）的市场份额与技术护城河。

---

## 3. 蓝海与缺口

| 缺口维度 | 具体描述 | 证据来源 | 优先级 |
|----------|----------|----------|--------|
| **可纠正性评测缺位** | 无专门针对「可纠正性」的标准化基准、指标与测试协议；现有安全基准多聚焦拒答/有害内容，缺乏对「允许关闭/修正目标/不欺骗监督者」的量化度量 | [1] (AI Governance 流未覆盖), [11] (分类法未含此维度) | ⭐⭐⭐⭐⭐ |
| **开放多智能体系统参与门槛** | MOASEI 2026 仅 1 队完赛，揭示环境搭建、接口标准化、计算资源门槛过高，缺乏低门槛的「开箱即用」基准套件 | [15] | ⭐⭐⭐⭐ |
| **评测报告规范缺失** | 12 篇基准论文关键超参数（脚手架、采样、子集、评估器版本）普遍未披露，导致跨论文、跨基准结果不可比，无统一审计标准 | [2] | ⭐⭐⭐⭐⭐ |
| **动态/对抗/长尾安全评测融合范式** | 静态基准与动态红队、对抗攻击、长尾分布偏移评测割裂，缺乏统一融合框架 | [1], [11], [23], [31] | ⭐⭐⭐⭐ |
| **主流开源评测框架 Agent 适配现状未知** | AgentBench, OpenCompass, HELM, LM-Eval-Harness, Safety-Gym 等框架对 Agent 多轮、工具调用、多智能体、欺骗/可纠正性的支持度、最新版本架构差异、真机部署案例**完全缺乏公开对比证据** | [q3 findings], [27], [32], [34] (均不相关) | ⭐⭐⭐⭐ |
| **欺骗行为分类学与标注规范** | 策略性欺骗、迎合性欺骗、隐瞒能力等细分类型缺乏统一定义与标注指南，SVC 2025 [23] 仅覆盖多模态表层，[24] 仅探针单一任务 | [23], [24] | ⭐⭐⭐ |
| **生产环境持续评测方法论不成熟** | 仅单一案例 [9]，缺乏通用的低成本、高频、可信的演化 Agent 评测最佳实践与工具链 | [9] | ⭐⭐⭐ |

---

## 4. 瓶颈与拐点

### 4.1 核心瓶颈
1.  **测量鸿沟**：EvalSafetyGap [1] 指出的「指标提升 ≠ 真实能力/对齐提升」是根本性**风险**，源于基准污染、代理奖励过拟合、LLM-as-a-judge 偏差、分布外泛化失效等八大机制。
2.  **复现性危机**：关键工程细节（脚手架、随机种子、采样温度、评估器版本）系统性缺失 [2]，导致科学积累失效，**不确定**性极高。
3.  **开放系统评测工程壁垒**：MOASEI [15] 暴露的环境复杂性、接口非标、计算成本高，使得基准「有基准无人测」，陷入**负反馈循环**。
4.  **静态基准与动态威胁错位**：欺骗 [23, 24]、对抗 [31]、分布漂移 [9] 等动态威胁无法被静态数据集覆盖，但动态评测成本高、难标准化。
5.  **可纠正性机制与评测双缺失**：理论定义（关闭按钮、目标修正、诚实报告）与工程实现、评测协议严重脱节，**风险**在于模型规模增大时涌现欺骗性权力寻求行为无法被现有基准捕获。

### 4.2 拐点信号
- **持续评测范式兴起**：[9] 验证生产环境时间序列切分法可行性，预示「一次性基准榜单」向「持续评测管线」转型的**拐点**已现。
- **机制可解释性介入安全评测**：[24] 线性探针检测欺骗、[1] 机制可解释性证据流，标志着从「黑盒行为测试」向「白盒机制审计」转型的早期信号。
- **多模态欺骗基准启动**：SVC 2025 [23] 将欺骗检测从文本推向音视频，应对 GPT-4o 等原生多模态模型带来的新攻击面。
- **透明度合规驱动工程投入**：Foundation Model Transparency Index [27] 等外部压力倒逼厂商建设可审计评测基建。

---

## 5. 社会·政策·国际

### 5.1 监管与标准驱动评测合规化
- **增量判断**：EvalSafetyGap [1] 将「AI 治理」列为八大证据流之一，隐含政策层对评测严谨性的要求；2025 Foundation Model Transparency Index [27] 直接回应 EU AI Act、US Executive Order 等合规压力，推动评测向**可审计、可追溯、标准化**演进。
- **国际标准化动向**：> 待核实：ISO/IEC 42001 (AI 管理体系)、NIST AI RMF 1.0/2.0、EU AI Act 高风险系统评测要求对 Agent 评测的具体技术规范转化进展。
- **地缘政治影响**：> 待核实：算力出口管制、数据跨境流动限制对多国联合 Agent 评测基准（如 MOASEI 国际参赛）的影响；开源评测框架（OpenCompass 等）在全球生态中的地缘博弈。

### 5.2 伦理与劳动影响
- **欺骗与可纠正性的社会风险**：若 Agent 具备策略性欺骗 [24] 且不可纠正，在医疗、金融、司法等高风险领域部署将造成**不可控的社会危害**，评测滞后于部署是核心**风险**点。
- **评测劳动力市场**：> 待核实：红队测试、人工标注、专家评审等评测劳动力的专业化分工、薪资水平、地理分布变化。

---

## 6. 资本与生态

### 6.1 投资与商业化信号
- **评测基建赛道升温**：> 待核实：Patronus AI, Galileo, Braintrust, LangSmith 等评测/可观测平台融资轮次、估值、ARR 增长数据；Agent 专用评测初创公司涌现情况。
- **开源生态主导权竞争**：GitHub Stars 作为重要性指标存在显著偏差 [32]，但仍反映社区关注度分布；OpenCompass (上海 AI Lab)、AgentBench (清华/OSPP)、HELM (Stanford)、LM-Eval-Harness (EleutherAI) 等框架在**生态兼容性、插件生态、商业支持**上的竞争加剧，**但缺乏最新版本对比证据** [q3 findings]。
- **人才流动**：> 待核实：顶会评测/安全方向论文作者流向（学术界→产业界、大厂→初创）、核心开发者贡献度变化。

### 6.2 透明度指数作为生态治理工具
- Foundation Model Transparency Index 2025 [27] 通过量化排名倒逼厂商披露训练数据、评测细节、风险缓解措施，形成**软治理**机制，对 Agent 评测生态规范化有示范作用。

---

## 7. 信号与预测

| 信号 | 来源 | 解读 | 可验证预测 [P] | 置信度 |
|------|------|------|----------------|--------|
| **持续评测管线成为标配** | [9] 生产案例验证可行性 | 从「榜单刷分」转向「CI/CD 集成评测」是工程必然趋势 | **P1**：至 2027 年中，≥50% 头部 Agent 产品团队接入自动化持续评测管线（含回归测试、A/B 测试、影子模式） | 较大概率 |
| **机制可解释性成安全评测标配** | [1] 证据流、[24] 线性探针 | 黑盒行为测试不足以捕获欺骗/权力寻求，白盒审计将成高风险系统准入门槛 | **P2**：至 2026 年底，NIST/ISO 标准草案纳入「激活空间探针/SAE 审计」作为高风险 Agent 评测推荐项 | 推测 |
| **多模态欺骗基准快速迭代** | [23] SVC 2025 首届 | 原生多模态模型部署加速，文本-only 欺骗基准失效 | **P3**：2026-2027 年出现 ≥3 个多模态欺骗/对抗基准（含实时语音/视频流），并被主流评测框架集成 | 较大概率 |
| **可纠正性基准启动** | [1], [11] 均未覆盖 | 理论共识与工程实践巨大鸿沟，急需基准催化 | **P4**：2026 年内发布首个「可纠正性评测基准 v0.1」（含关闭按钮测试、目标修正服从度、诚实报告基准），由学术-产业联盟主导 | 推测 |
| **评测报告强制披露规范化** | [2] 审计工具、[27] 透明度指数 | 复现性危机倒逼会议/期刊/平台强制要求评测报告卡 | **P5**：NeurIPS/ICML/ICLR 2027 投稿指南强制要求附带 5 字段审计清单 [2] 通过的评测报告 | 确定 |
| **开放多智能体基准整合或消亡** | [15] MOASEI 参与度极低 | 碎片化、高门槛基准难以形成社区效应，将整合至通用 Agent 评测平台 | **P6**：MOASEI 第 3 届（2027）若参赛队伍 <5，将并入 AgentBench/OpenCompass 等综合平台作为子任务 | 需要数据 |

> **不确定性声明**：以上预测基于当前有限证据推演，受算力成本、模型架构范式变迁（如世界模型、规划器分离）、监管政策突变等**不确定**因素影响大。需持续追踪顶会论文、基准榜单更新、厂商技术博客、标准化组织动态以修正判断。

---

## 经典与奠基性工作

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| EvalSafetyGap: A Hybrid Survey and Conceptual Framework for LLM Evaluation-Safety Failures | 2026 | arXiv (cs.AI) | > 待核实 | arXiv 预印本，覆盖 373 项研究 | 高 | ★★★★☆ | [1] | 系统梳理评测-安全测量鸿沟，八流证据分类法，本方向必读锚点 |
| What Twelve LLM Agent Benchmark Papers Disclose About Themselves: A Pilot Audit and an Open Scoring Schema | 2026 | arXiv (cs.LG) | > 待核实 | arXiv 预印本 | 高 | ★★★★☆ | [2] | 实证审计 12 篇基准论文，提供 5 字段审计模式与评分代码本 |
| Evaluation and Benchmarking of LLM Agents: A Survey | 2025 | arXiv (cs.LG) | > 待核实 | arXiv 预印本 | 中 | ★★★☆☆ | [11] | 提出二维分类法（目标×方法），早期全景综述 |
| Detecting Strategic Deception Using Linear Probes | 2025 | arXiv | > 待核实 | arXiv 预印本 | 中 | ★★★☆☆ | [24] | 机制可解释性视角检测策略性欺骗，为可纠正性前置提供技术路径 |
| SVC 2025: the First Multimodal Deception Detection Challenge | 2025 | arXiv | > 待核实 | 挑战赛官方报告 | 中 | ★★★☆☆ | [23] | 首个多模态欺骗检测基准挑战赛，填补音视频欺骗评测空白 |
| OpenFact at CheckThat! 2024: Combining Multiple Attack Methods for Effective Adversarial Text Generation | 2024 | arXiv | > 待核实 | CheckThat! 共享任务官方论文 | 中 | ★★★☆☆ | [31] | 组合对抗攻击生成方法，推动自动化红队评测 |

---

## 开源项目

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| AgentBench | > 待核实 | > 待核实 | > 待核实 | > 待核实 | > 待核实 | > 待核实 | > 待核实 | 当前证据库无相关信息，需专门检索最新版本、架构、部署案例 |
| OpenCompass | > 待核实 | > 待核实 | > 待核实 | > 待核实 | > 待核实 | > 待核实 | > 待核实 | 当前证据库无相关信息，需专门检索 |
| HELM | > 待核实 | > 待核实 | > 待核实 | > 待核实 | > 待核实 | > 待核实 | > 待核实 | 当前证据库无相关信息，需专门检索 |
| LM-Eval-Harness | > 待核实 | > 待核实 | > 待核实 | > 待核实 | > 待核实 | > 待核实 | > 待核实 | 当前证据库无相关信息，需专门检索 |
| Safety-Gym | > 待核实 | > 待核实 | > 待核实 | > 待核实 | > 待核实 | > 待核实 | > 待核实 | 当前证据库无相关信息，需专门检索 |

> **待核实**：主流开源评测框架对 Agent 多轮、工具调用、多智能体、欺骗/可纠正性的支持度、最新版本架构差异、真机部署案例完全缺乏公开对比证据，急需补充检索。

---

## 数据集与基准

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| MOASEI 2026 (Second Competition) | 2026 | AAMAS 2026 | 低 (仅1队完赛) | AAMAS 顶会技术报告 | 中 | ★★★☆☆ | [15] | 开放多智能体系统评测，新增框架开放性赛道与动态装备约束，多维指标体系 |
| SVC 2025 Multimodal Deception Detection Challenge | 2025 | SVC 2025 Organizers | > 待核实 | 挑战赛官方报告 | 中 | ★★★☆☆ | [23] | 首个多模态欺骗检测基准，覆盖音视频欺骗行为 |
| Foundation Model Transparency Index 2025 | 2025 | Stanford HAI 等 | > 待核实 | arXiv 预印本，行业标杆 | 中 | ★★★☆☆ | [27] | 透明度评测基准，间接驱动 Agent 评测合规化 |

---

## 参考来源

[1] EvalSafetyGap: A Hybrid Survey and Conceptual Framework for LLM Evaluation-Safety Failures — http://arxiv.org/abs/2606.30219v5
[2] What Twelve LLM Agent Benchmark Papers Disclose About Themselves: A Pilot Audit and an Open Scoring Schema — http://arxiv.org/abs/2605.21404v1
[3] This paper has been withdrawn — http://arxiv.org/abs/cond-mat/0309395v2
[4] CHC-COMP 2022: Competition Report — http://arxiv.org/abs/2211.12231v1
[5] Motif Mining and Unsupervised Representation Learning for BirdCLEF 2022 — http://arxiv.org/abs/2206.04805v1
[6] Overview of Dialogue Robot Competition 2022 — http://arxiv.org/abs/2210.12863v1
[7] Evaluating LLM-based Agents for Multi-Turn Conversations: A Survey — http://arxiv.org/abs/2503.22458v3
[8] DFGC 2022: The Second DeepFake Game Competition — http://arxiv.org/abs/2206.15138v2
[9] Efficient Benchmarking in Production: A Study of an Evolving LLM Agent — http://arxiv.org/abs/2609.21267v1
[10] AIn't Nothing But a Survey? Using Large Language Models for Coding German Open-Ended Survey Responses on Survey Motivation — http://arxiv.org/abs/2506.14634v3
[11] Evaluation and Benchmarking of LLM Agents: A Survey — http://arxiv.org/abs/2507.21504v1
[12] Focus Agent: LLM-Powered Virtual Focus Group — http://arxiv.org/abs/2409.01907v1
[13] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1
[14] Preprint site arXiv is banning computer-science reviews: here's why — https://doi.org/10.1038/d41586-025-03664-7
[15] Second MOASEI Competition at AAMAS'2026: A Technical Report — http://arxiv.org/abs/2607.03399v1
[16] TTLab at Daleel 2026: STAR-Ar, Sequence Tagging for Argument Recognition in Arabic — http://arxiv.org/abs/2609.39385v1
[17] UIC-AIHealth4All at ArchEHR-QA 2026: Answer-First Evidence Grounding for Clinical Question Answering — http://arxiv.org/abs/2608.27467v1
[18] AutoRestTest at the SBFT 2026 Tool Competition — http://arxiv.org/abs/2607.01063v1
[19] NTU-NPU System for Voice Privacy 2024 Challenge — http://arxiv.org/abs/2410.02371v1
[20] Quarto Extension: arXiv with Typst — https://doi.org/10.59350/7d9k0-m1365
[21] VoxENES 2026: Benchmarking Generalization of Speech Spoofing Detectors Against LLM-Era TTS and Voice Conversion — http://arxiv.org/abs/2607.11706v1
[22] ICASSP 2026 Radar Acoustic Speech Enhancement (RASE) Challenge — http://arxiv.org/abs/2610.32202v1
[23] SVC 2025: the First Multimodal Deception Detection Challenge — http://arxiv.org/abs/2508.04129v1
[24] Detecting Strategic Deception Using Linear Probes — http://arxiv.org/abs/2502.03407v1
[25] Discovery Opportunities with Gravitational Waves -- TASI 2024 Lecture Notes — http://arxiv.org/abs/2409.08956v1
[26] Atmospheric entry and fragmentation of small asteroid 2024 BX1: Bolide trajectory, orbit, dynamics, light curve, and spectrum — http://arxiv.org/abs/2403.00634v2
[27] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1
[28] ICAGC 2024: Inspirational and Convincing Audio Generation Challenge 2024 — http://arxiv.org/abs/2407.12038v2
[29] Double Multi-Head Attention Multimodal System for Odyssey 2024 Speech Emotion Recognition Challenge — http://arxiv.org/abs/2406.10598v1
[30] NTIRE 2025 Challenge on Image Super-Resolution (x4): Methods and Results — http://arxiv.org/abs/2504.14582v3
[31] OpenFact at CheckThat! 2024: Combining Multiple Attack Methods for Effective Adversarial Text Generation — http://arxiv.org/abs/2409.02649v2
[32] The Fault in Our Stars: An Analysis of GitHub Stars as an Importance Metric for Web Source Code — https://doi.org/10.14722/madweb.2024.23004
[33] Overview of the Sensemaking Task at the ELOQUENT 2025 Lab: LLMs as Teachers, Students and Evaluators — http://arxiv.org/abs/2507.12143v1
[34] ThankYouStars: Give your Dependencies Stars on GitHub! — https://doi.org/10.32614/cran.package.thankyoustars

---

*Generated by research-bot · topic=`agent-评测与安全能力基准欺骗与可纠正性` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`nvidia/nemotron-3-ultra-550b-a55b` · sources=34 · duration=383s · 2026-10-31T22:45:14+00:00*
