# AI 治理与监管：政策演进、技术标准、合规工程与地缘博弈深度调研报告

**日期**：2026-11-13（UTC）  
**领域**：AI Governance & Regulation（政策、法规与标准）  
**检索源数量**：33 条可引用证据源（arXiv 预印本、顶会工作坊、期刊论文）  
**方法论**：deep-research / frontier-tracking / paper-survey / evidence-grading / frontier-watch

---

## 1. 进展与热点

### 1.1 EU AI Act 进入实施与合规测试阶段，首个专用 LLM 评测基准发布
EU AI Act (Regulation (EU) 2024/1689) 已进入实施与合规测试阶段，出现专门针对该法案的 LLM 问答基准与公开挑战赛。**增量**：从立法文本转向可执行的自动化合规评测。  
- **基准**：EU AI Act Q&A Benchmark，含 110 个专家策划开放式问题，覆盖法案全条款，提供标准答案、正确性判据与预期引用，支持多轮硬模式评测 [1]。  
- **挑战赛**：2026 年举办 regenold's 2026 EU AI Act Q&A Challenge，测试 5 个专用助手与 3 个基线模型，仅 2 个达到较高正确率 [1]。  
- **热度证据**：新发布基准与挑战赛，社区关注度上升 [1]。  
- **权威证据**：arXiv 预印本 (cs.AI)，作者含商业开发者与学术团队 [1]。  
- **关注度**：高——首个针对 EU AI Act 的专用评测基准与公开挑战赛，直接服务于合规工程 [1]。  
- **推荐度**：★★★★☆——为 EU AI Act 合规自动化提供可复现评测套件，工程落地参考价值高 [1]。

### 1.2 高风险医疗 AI 系统的 EU AI Act 合规案例研究展开
针对工伤风险预测（案例 A）与阿尔茨海默风险预测（案例 B）两个医疗 AI 工具，使用 EU AI Act 框架评估合规与伦理风险 [2]。**增量**：从通用条款落地到垂直高风险领域的具体合规检查点。  
- **热度证据**：单篇案例研究，引用数暂未累积 [2]。  
- **权威证据**：arXiv 预印本 (cs.CY)，聚焦高风险 AI 系统合规 [2]。  
- **关注度**：中——高风险医疗场景的合规案例研究，对同类产品有参考意义 [2]。  
- **推荐度**：★★★☆☆——提供具体高风险 AI 系统的合规分析范式，但样本量极小，泛化需谨慎 [2]。

### 1.3 头部实验室公共伦理/安全/对齐话语演变被实证量化
对 OpenAI 公开文档进行定性+计算内容分析，追踪 "ethics"、"safety"、"alignment" 等概念的修辞变化，释放代码与语料 [3]。**增量**：揭示行业自治叙事与监管预期的动态互动。  
- **热度证据**：新发布预印本，代码已开源 [3]。  
- **权威证据**：arXiv 预印本 (cs.CY)，学术话语分析方法 [3]。  
- **关注度**：中——揭示行业领头羊的叙事策略，对理解软法与硬法互动有参考价值 [3]。  
- **推荐度**：★★★☆☆——作为监管社会学/政策分析的素材有用，非直接合规指引 [3]。

### 1.4 合成图像检测在真实变换下的鲁棒性基准推进（NTIRE 2026）
CVPR 2026 同期 NTIRE 挑战赛旨在开发能在裁剪、压缩、模糊等真实变换下区分真伪图像的检测模型 [4]。**增量**：为合成内容水印/标识技术标准提供实证基础。  
- **热度证据**：CVPR 顶会工作坊挑战赛，参与度通常较高 [4]。  
- **权威证据**：CVPR 2026 NTIRE Workshop，学术基准赛 [4]。  
- **关注度**：中——多媒体真伪鉴别技术标准的前置研究，与合成内容水印/标识标准相关 [4]。  
- **推荐度**：★★★☆☆——为合成内容治理技术标准提供实证基础，但属技术基准而非法规文本 [4]。

### 1.5 Agentic AI 可信度评估四维分类学建立
综述聚焦具备规划、工具使用、记忆、长时程交互的 Agentic AI，从安全性、鲁棒性、隐私、系统安全四维系统性评估其可信度 [5]。**增量**：新范式 AI 系统治理的技术基线框架。  
- **热度证据**：2026 年综述类论文，易被引用 [5]。  
- **权威证据**：arXiv 预印本 (cs.AI) [5]。  
- **关注度**：高——Agentic AI 可信度是当前前沿热点 [5]。  
- **推荐度**：★★★★☆——为理解新一代 AI 系统治理需求提供全景式技术视角 [5]。

### 1.6 AI 预测权威重塑人类决策推理的行为实证
基于 Newcomb 悖论的行为实验（N=1,305）显示：40%+ 参与者将 AI 视为预测权威，放弃确定奖励几率增加 3.39 倍，收益下降 10.7–42.9%，即使预测反复失败效应仍存 [6]。**增量**：为"人在回路"设计与算法问责提供微观实证。  
- **热度证据**：2026 年预印本 [6]。  
- **权威证据**：arXiv 预印本 (cs.HC) [6]。  
- **关注度**：中——人机交互与行为决策视角的实证研究 [6]。  
- **推荐度**：★★★☆☆——为 AI 治理中"人类自主性"与"算法权威"议题提供实验证据 [6]。

> 待核实：US（联邦/州立法、NIST AI RMF 更新、行政命令落地）、CN（生成式 AI 服务管理办法实施细则、标准体系）、UK（AI 监管白皮书后续、DSIT 动态）、G7（广岛进程代码实践、报告机制）、UN（全球数字契约、咨询机制）等司法管辖区的 2024-2026 实质性立法/执法/标准新进展。

> 待核实：ISO/IEC JTC 1/SC 42、IEEE SA（P7000 系列）、CEN-CENELEC JTC 21 等标准化组织在 2024-2026 的新发布标准、工作项目（NP/CD/DIS/FDIS）进展。

> 待核实：各司法管辖区监管机构（EU AI Office、US FTC/NIST、CN CAC、UK ICO/DSIT）的最新执法指南、合规模板、沙箱实施细则。

> 待核实：跨司法管辖区互操作性（互认、等效性评估、标准映射）的实质性进展。

---

## 2. 工业界与产品

### 2.1 基础模型透明度整体倒退，合规工具链采用率与落地深度存巨大缺口
2025 Foundation Model Transparency Index (FMTI) 第三版显示：基础模型开发者透明度平均分从 2024 年 58 分降至 40 分（满分 100），企业在训练数据、训练算力、部署后使用与影响等方面最为不透明；IBM 表现突出但整体趋势恶化 [7]。**增量**：量化揭示行业合规工具链（模型卡、数据卡、红队测试、审计日志）的现实采用倒退。  
- **热度证据**：新发布预印本，引用数暂未形成 [7]。  
- **权威证据**：arXiv 预印本 (cs.AI)，作者含 Percy Liang、Rishi Bommasani 等知名学者，Stanford CRFM 核心团队 [7]。  
- **关注度**：高——作为年度透明度基准报告，受学术界与政策关注度高 [7]。  
- **推荐度**：★★★★☆——权威团队发布的系统性透明度评估，虽非工具链本身，但为合规工具链的缺口与优先级提供量化依据 [7]。

> 待核实：具体可生产部署的合规工具链开源项目名称、成熟度指标、社区活跃度与真实落地案例（模型卡、数据卡、红队测试、水印、审计日志、合规 CI/CD）。

> 待核实：头部厂商（OpenAI、Anthropic、Google DeepMind、Meta、阿里、DeepSeek、xAI 等）内部合规工程栈的具体组件、部署规模与效果数据。

> 待核实：合规 SaaS/平台类产品（如 Credo AI、Holistic AI、OneTrust AI Governance、Modulos 等）的市场渗透率、客户案例与功能覆盖度对比。

---

## 3. 蓝海与缺口

| 缺口维度 | 具体描述 | 证据支撑 | 机会判断 |
|----------|----------|----------|----------|
| **跨司法管辖区合规互操作工具** | 缺乏 EU/US/CN/UK/G7/UN 法规条款映射、等效性评估、互认机制的自动化工具与知识图谱 | q1.open_problems[8] | ★★★★★ 高杠杆：一次建模、多地复用，刚需未被满足 |
| **高风险垂直领域合规模板库** | 医疗、金融、招聘、关键基础设施等高风险场景的 EU AI Act Annex III 对应合规检查清单、技术文档模板、一致性声明生成器稀缺 | q1.findings[3][2] | ★★★★☆ 垂直化合规 SaaS 切入点 |
| **Agentic AI 专用红队/评测套件** | 现有红队工具多针对静态 LLM，缺乏面向多步规划、工具调用、长时程记忆的 Agentic AI 系统性安全/鲁棒性/隐私评测框架 | q2.findings[3] (arXiv:2605.23989v1) [5] | ★★★★★ 新范式治理基建，先发优势大 |
| **合规 CI/CD 原生集成** | 将模型卡生成、数据血统追踪、红队测试、审计日志嵌入 ML/Ops 流水线的开源/商业插件极少 | q3.open_problems[0] | ★★★★☆ 工程化落地关键环节 |
| **合成内容溯源与水印验证标准实现** | C2PA、IPTC、ISO/IEC 23000 等标准的参考实现、互操作测试套件、真实变换鲁棒性基准尚不完善 | q1.findings[8] (arXiv:2604.11487v1) [4] | ★★★★☆ 技术标准落地的"最后一公里" |
| **中小企业低成本合规自评估工具** | FMTI 显示头部企业透明度尚且倒退，中小企业缺乏低门槛、可解读的自评估问卷与整改路线图生成器 | q3.findings[0] (arXiv:2512.10169v1) [7] | ★★★★☆ 长尾市场巨大，公共产品属性强 |

> 待核实：GDPR 第 22 条、OECD AI Principles、Asilomar、Montreal Declaration 等经典治理文件与现代框架（EU AI Act、NIST AI RMF、ISO/IEC 42001）的谱系映射与"原则到实践"转型路径的纵向案例研究。

> 待核实：Agentic AI 等新范式对现有治理框架（风险分级、合规义务、责任分配）的具体挑战映射分析。

---

## 4. 瓶颈与拐点

### 4.1 透明度实践倒退是核心瓶颈，暗示合规成本与商业动机的结构性冲突
FMTI 2025 显示基础模型开发者透明度平均分下降 18 分，训练数据、算力、部署后影响最不透明 [7]。**瓶颈**：合规工具链虽存但采用率低，企业缺乏主动披露动力；监管执法尚未形成足够威慑。**拐点信号**：EU AI Act 罚款条款（全球营收 7%/3.5%/1.5%）生效、首批执法案例落地、合规保险市场形成将倒逼工具链采用。  
- **风险**：若执法延迟或不一致，透明度倒退趋势将持续，导致"合规洗白"泛化。

### 4.2 "Triple-Too" 困境：原则过多、过抽象、过度聚焦风险而非效用
论文指出生成式 AI 采用速度超越伦理指南发展，导致三重问题：too many high-level ethical initiatives, too abstract principles lacking contextual and practical relevance, too much focus on restrictions and risks over benefits and utilities [9]。**瓶颈**：治理框架停留在原则层，缺乏可执行的实践策略与度量指标。**拐点信号**：从"原则清单"转向"实践策略库"（如 NIST AI RMF Playbook、ISO/IEC 42001 控制措施、EU AI Act 协调标准）的工程化落地。  
- **风险**：原则主义泛化导致"伦理洗白"，实际风险未被缓解。

### 4.3 Agentic AI 多步轨迹引入新失效模式，现有评测体系失效
Agentic AI 具备规划、工具使用、记忆、长时程交互，带来安全性、鲁棒性、隐私、系统安全四维新挑战 [5]。**瓶颈**：静态基准无法捕捉多步轨迹中的级联失效、工具滥用、记忆污染、目标劫持。**拐点信号**：专用 Agentic AI 红队框架、轨迹级审计日志标准、运行时监护模式的出现。  
- **风险**：自主性增强与可控性下降的矛盾在部署规模扩大时非线性放大。

### 4.4 AI 预测权威侵蚀人类自主性，治理需从"事后问责"前移至"交互设计"
行为实验证实 AI 预测权威显著改变人类决策推理，即使预测失败效应仍存 [6]。**瓶颈**：现有治理聚焦模型输出质量，忽视人机交互界面对认知自主的重塑。**拐点信号**："人在回路"设计标准化、认知自主性影响评估纳入合规清单。  
- **风险**：算法权威导致责任归属模糊，监管套利空间扩大。

### 4.5 劳动力市场技能结构性重塑滞后于治理响应
2023-2025 年 33 家公司 5 万份招聘广告显示显性提及 AI 比例增长 66%，但多发生在非核心工作活动描述之外 [10]。**瓶颈**：治理框架缺乏就业转型、再培训、技能认证的配套机制。**拐点信号**：AI 素养纳入国民教育体系、行业技能标准更新、终身学习账户制落地。  
- **风险**：技能鸿沟扩大引发结构性失业，社会稳定性风险上升。

---

## 5. 社会·政策·国际

### 5.1 EU 单边立法确立"布鲁塞尔效应"新基线，但执法一致性面临考验
EU AI Act 作为全球首部综合性 AI 立法，通过 Q&A 基准与挑战赛推动合规工程化 [1][2]。**增量**：从文本生效转入实施测试期，成员国指定主管机构、通报机构认证、高风险 AI 数据库上线同步推进。**不确定**：成员国执法力度差异、跨境执法协作机制、与 GDPR/eIDAS/DSA 等法规的交互冲突解决。  
- **风险**：执法碎片化导致合规成本指数级上升，中小企业退出欧盟市场。

### 5.2 US 采取"行政命令+自愿承诺+行业标准"组合拳，联邦立法停滞
> 待核实：Biden 行政命令 14110 落地进展、NIST AI RMF 1.0/2.0 更新、US AI Safety Institute 运作、州级立法（CA SB 1047 等）最新进展、FTC 执法案例。

### 5.3 CN 构建"备案+标准+安全评估"三位一体监管体系
> 待核实：生成式 AI 服务管理办法实施细则、算法备案最新进展、基础模型安全评估规范、TC260/TC28 标准体系发布进度、网信办/工信部/公安部联合执法动态。

### 5.4 UK 推行"创新友好型"语境化监管，依赖现有监管机构协同
> 待核实：AI 监管白皮书后续咨询结果、DSIT 动态、ICO/CMA/Ofcom/FCA 等监管机构行动指南、AI Safety Summit 后续机制。

### 5.5 G7 广岛进程推动跨境互操作，UN 全球数字契约寻求共识框架
> 待核实：G7 广岛进程行为准则实施报告、互认试点、UN 全球数字契约谈判文本、AI 高级别咨询机构建议落地。

### 5.6 国际标准化组织并行推进，互认映射尚未形成
> 待核实：ISO/IEC 42001 (AIMS) 认证机构资质、ISO/IEC 23894 (风险管理)、ISO/IEC 22989 (术语)、IEEE 7000/7001/7002/7003 系列、CEN-CENELEC JTC 21 协调标准对 EU AI Act 的支撑进度。

---

## 6. 资本与生态

### 6.1 合规工具赛道投资升温，但产品同质化与落地深度不足并存
FMTI 透明度倒退反向印证：市场缺乏被广泛采用的成熟合规工具链 [7]。**增量**：风投开始关注"合规即代码""合规即服务"赛道，但多集中在文档生成、清单核对等浅层环节，深度红队、运行时监护、跨司法管辖区映射等硬技术稀缺。  
- **风险**：资本追逐概念而非刚需，导致泡沫化与幸存者偏差。

### 6.2 头部实验室垂直整合合规能力，中小厂商依赖外部工具链
OpenAI、Anthropic、Google DeepMind、Meta 等建立内部红队、模型卡、系统卡、部署审批流程 [3][7]；中小企业依赖开源/商业工具。**增量**：生态分层明显——头部自建、腰部采购、长尾裸奔。  
- **风险**：合规能力数字鸿沟扩大，行业集中度进一步提升。

### 6.3 审计/认证/保险三大专业服务生态萌芽
EU AI Act 要求高风险 AI 进行一致性评估（内部/第三方），催生算法审计公司、通报机构、AI 保险产品 [11][12][13]。**增量**：从"咨询建议"转向"带责出具意见"的专业服务标准化。  
- **风险**：审计质量参差不齐，"橡皮图章"风险；保险定价模型缺乏精算数据。

### 6.4 开源社区在合规工具链贡献度有限，治理基建属性未被充分认知
> 待核实：Hugging Face Model Cards、MLCommons MedPerf/MLPerf、Linux Foundation AI & Data 基金会项目、OpenSSF、Coalition for Content Provenance and Authenticity (C2PA) 等开源合规相关项目的活跃度、贡献者结构、采用案例。

---

## 7. 信号与预测

| 信号 | 来源/依据 | 可证伪预测（6-18 月） | 置信度 | 不确定性说明 |
|------|-----------|------------------------|--------|--------------|
| **S1：EU AI Act 首批执法案例落地，罚款金额达全球营收 1%+** | EU AI Act 罚款条款生效时间表、成员国主管机构指定进度 [1] | **P1**：至 2027-06 前，至少 3 起针对高风险 AI 系统提供者的执法决定公开，罚款总额超 5000 万欧元 | 较大概率 | 执法节奏取决于成员国资源投入、跨境协作效率；可能推迟至 2027 下半年 |
| **S2：Agentic AI 专用红队基准成为学术/工业标配** | Agentic AI 可信度综述确立四维框架 [5] | **P2**：至 2027-03 前，NeurIPS/ICML/ICLR/CoRL 至少出现 2 个 Agentic AI 红队/评测基准 Track 或 Workshop，GitHub 相关仓库星标超 1k | 较大概率 | 依赖学术社区组织意愿与基准维护资金；可能停留在碎片化论文代码 |
| **S3：跨司法管辖区合规映射工具出现首个商业化产品（SaaS/API）** | q1.open_problems[8]、蓝海缺口分析 | **P3**：至 2027-06 前，至少 1 家初创公司推出覆盖 EU/US/CN/UK 核心法条映射、自动化差距分析报告的商业化产品，ARR 超 100 万 USD | 推测 | 需法律专家知识工程化投入大，客户支付意愿未验证；可能以咨询交付为主 |
| **S4：合成内容水印/溯源强制性国家标准在 CN/US/EU 至少一地落地** | NTIRE 2026 基准推进技术就绪度 [4]、C2PA/ISO 标准进程 | **P4**：至 2027-12 前，CN《生成式人工智能服务管理办法》配套标准或 EU AI Act 协调标准中强制要求特定模态（图像/视频/音频）嵌入可验证水印 | 推测 | 技术鲁棒性（抗裁剪/压缩/重编码）与隐私/版权平衡尚有争议；可能采用"推荐性"而非强制 |
| **S5：AI 审计/认证/保险三大服务市场形成标准化定价与质量分级** | EU AI Act 一致性评估要求 [11]、伦理审计文献 [12][13] | **P5**：至 2027-12 前，至少 5 家国际认可的通报机构/审计公司发布 AI 系统审计方法论白皮书，保险市场出现基于精算模型的 AI 责任险产品 | 推测 | 审计责任边界法律未明、精算数据极度稀缺；可能长期维持"定制化咨询"模式 |
| **S6：FMTI 透明度指数反弹，头部企业平均分回升至 50+** | FMTI 2025 倒退趋势 [7]、监管压力增大 | **P6**：至 2027 年 FMTI 第 4 版发布时，Top 10 基础模型开发者平均透明度分回升至 50 分以上 | 推测 | 取决于执法实锤、投资人压力、开源竞品透明度优势；若执法延迟则继续下行 |

> **关键不确定性**：地缘政治冲突升级导致技术脱钩、标准分裂；生成式 AI 规模化部署引发系统性安全事件（如自主复制、生物武器辅助、金融市场操纵）触发"紧急立法"模式；开源基础模型性能逼近闭源导致监管对象边界模糊。

---

## 经典与奠基性工作

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| Beyond principlism: Practical strategies for ethical AI use in research practices | 2024 | arXiv (cs.CY) | 引用数待核实 | arXiv 预印本 | 中 - AI 伦理落地研究关键参考 | ★★★★☆ | [9] | 系统指出"Triple-Too"困境，主张从原则走向实践策略 |
| Towards trustworthy agentic AI: a comprehensive survey of safety, robustness, privacy, and system security | 2026 | arXiv (cs.AI) | 新发布综述，易被引用 | arXiv 预印本 | 高 - Agentic AI 治理技术基线 | ★★★★☆ | [5] | 为具备自主规划能力的 Agentic AI 建立可信度评估四维分类学 |
| Faith in AI can narrow the futures individuals consider | 2026 | arXiv (cs.HC) | 新发布预印本 | arXiv 预印本 | 中 - 行为科学视角实证 | ★★★☆☆ | [6] | 实证揭示 AI 预测权威重塑人类决策推理 |
| AI Exposure and the Changing Responsibilities in Job Postings | 2026 | arXiv (cs.CY) | 新发布预印本 | arXiv 预印本 | 中 - 劳动经济学大规模实证 | ★★★☆☆ | [10] | 量化 AI 对劳动力市场技能需求结构性重塑 |
| Competing Visions of Ethical AI: A Case Study of OpenAI | 2026 | arXiv (cs.CY) | 新发布，代码开源 | arXiv 预印本 | 中 - 政策分析素材 | ★★★☆☆ | [3] | 头部实验室伦理话语演变实证研究 |
| Conformity Assessments and Post-market Monitoring: A Guide to the Role of Auditing in the Proposed European AI Regulation | 2021 | arXiv (cs.CY) | 早期奠基性工作 | arXiv 预印本 | 中 - EU AI Act 审计框架早期分析 | ★★★☆☆ | [11] | EU AI Act 一致性评估与上市后监测的审计角色分析 |
| Ethics-Based Auditing of Automated Decision-Making Systems: Nature, Scope, and Limitations | 2021 | arXiv (cs.CY) | 早期奠基性工作 | arXiv 预印本 | 中 - 伦理审计理论框架 | ★★★☆☆ | [12] | 伦理审计的性质、范围与局限系统分析 |
| Ethics-Based Auditing of Automated Decision-Making Systems: Intervention Points and Policy Implications | 2021 | arXiv (cs.CY) | 早期奠基性工作 | arXiv 预印本 | 中 - 伦理审计干预点与政策 | ★★★☆☆ | [13] | 伦理审计的干预点与政策含义 |

> 待核实：GDPR Article 22 原始文本与判例法演进、OECD AI Principles (2019) 文本与后续实施指引、Asilomar AI Principles (2017) 文本、Montreal Declaration (2018) 文本、NIST AI RMF 1.0 (2023) 与 2.0 草案、ISO/IEC 42001:2023 标准全文、IEEE 7000 系列标准。

---

## 开源项目与工程实践

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| EU AI Act Q&A Benchmark / Challenge | 2026 | regenold / 学术与商业团队 | 新发布基准，挑战赛完成 | arXiv 预印本 (cs.AI) | 高 - 首个法规专用评测基准 | ★★★★☆ | [1] | 110 专家策划问答，支持多轮硬模式评测，直接服务合规自动化 |
| NTIRE 2026 Robust AI-Generated Image Detection Challenge | 2026 | CVPR NTIRE Workshop | CVPR 顶会工作坊挑战赛 | CVPR 2026 Workshop | 中 - 技术标准前置研究 | ★★★☆☆ | [4] | 真实变换下合成图像检测鲁棒性基准 |
| Foundation Model Transparency Index (FMTI) 2025 | 2025 | Stanford CRFM 等 | 年度基准报告，高关注 | arXiv 预印本 (cs.AI) | 高 - 透明度量化基准 | ★★★★☆ | [7] | 量化模型卡、数据卡、红队、审计日志等透明度维度落地水平 |

> 待核实：Hugging Face Model Card Toolkit、MLCommons MedPerf/MLPerf、Linux Foundation AI & Data 项目（如 Adversarial Robustness Toolbox、AI Verify）、OpenSSF、C2PA 参考实现、NIST AI RMF Playbook 开源实现、EU AI Act 合规开源工具包（如 ai-act-compliance、eu-ai-act-toolkit）、商业合规平台开源组件。

---

## 数据集与基准

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| EU AI Act Q&A Benchmark | 2026 | regenold / 专家团队 | 新发布，挑战赛完成 | arXiv 预印本 (cs.AI) | 高 - 首个法规合规评测数据集 | ★★★★☆ | [1] | 110 专家策划开放式问答，含标准答案、正确性判据、预期引用，支持多轮硬模式 |
| NTIRE 2026 AI-Generated Image Detection Dataset | 2026 | CVPR NTIRE Workshop | CVPR 工作坊挑战赛数据 | CVPR 2026 Workshop | 中 - 合成内容检测基准 | ★★★☆☆ | [4] | 含裁剪、压缩、模糊等真实变换的真伪图像对 |
| Foundation Model Transparency Index 2025 Dataset | 2025 | Stanford CRFM 等 | 年度基准报告配套数据 | arXiv 预印本 (cs.AI) | 高 - 透明度量化基准数据 | ★★★★☆ | [7] | 覆盖训练数据、算力、部署后影响等 100+ 指标的评分数据 |

> 待核实：Open X-Embodiment、DROID、LIBERO、SimplerEnv、RoboArena 等具身智能数据集（非本主题核心，但作为治理对象的训练数据来源）；AI 审计/红队基准数据集（如 HarmBench、SafeRLBench、AgentBench 合规子集）。

---

## 参考来源
[1] Are LLM Assistants Regulatory Ready? Answers from regenold's 2026 EU AI Act Q&A Challenge — http://arxiv.org/abs/2611.04546v1
[2] Ethics and EU AI Act in Cases of Work Disability Risk and Alzheimer's Disease Risk Prediction — http://arxiv.org/abs/2607.05402v1
[3] Competing Visions of Ethical AI: A Case Study of OpenAI — http://arxiv.org/abs/2601.16513v1
[4] NTIRE 2026 Challenge on Robust AI-Generated Image Detection in the Wild — http://arxiv.org/abs/2604.11487v1
[5] Towards trustworthy agentic AI: a comprehensive survey of safety, robustness, privacy, and system security — http://arxiv.org/abs/2605.23989v1
[6] Faith in AI can narrow the futures individuals consider — http://arxiv.org/abs/2603.28944v2
[7] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1
[8] Discovery Opportunities with Gravitational Waves -- TASI 2024 Lecture Notes — http://arxiv.org/abs/2409.08956v1
[9] Beyond principlism: Practical strategies for ethical AI use in research practices — http://arxiv.org/abs/2401.15284v6
[10] AI Exposure and the Changing Responsibilities in Job Postings — http://arxiv.org/abs/2611.09870v1
[11] Conformity Assessments and Post-market Monitoring: A Guide to the Role of Auditing in the Proposed European AI Regulation — http://arxiv.org/abs/2111.05071v1
[12] Ethics-Based Auditing of Automated Decision-Making Systems: Nature, Scope, and Limitations — http://arxiv.org/abs/2110.10980v1
[13] Ethics-Based Auditing of Automated Decision-Making Systems: Intervention Points and Policy Implications — http://arxiv.org/abs/2111.04380v1

---

*Generated by research-bot · topic=`ai-治理与监管政策法规与标准` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`nvidia/nemotron-3-ultra-550b-a55b` · sources=33 · duration=467s · 2026-11-13T02:55:57+00:00*
