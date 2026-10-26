# AI 治理与监管：全球政策演进、合规工程落地与前沿缺口深度调研报告

**日期**：2026-10-26 | **领域**：AI Governance & Regulation | **检索源数量**：31

---

## 1. 进展与热点

### 1.1 全球三大治理支柱形成“硬法+软标+认证制”三元结构
- **核心进展**：全球 AI 治理已围绕 **ISO/IEC 42001:2023**（首个可认证 AI 管理体系标准）、**NIST AI RMF 1.0**（自愿性社会技术风险模型）、**EU AI Act**（Regulation (EU) 2024/1689，具有约束力的分级风险法律）形成三大结构异构工具融合态势 [13]。
- **法律地位差异**：EU AI Act 为强制性法规（硬法），NIST AI RMF 为自愿性框架（软法），ISO 42001 为可认证标准（认证制），三者在法律地位、治理主体、风险概念上存在根本差异 [13]。
- **交叉映射缺失**：当前常见的控制级交叉映射既不完整又在部分地方具有误导性，三大框架在操作层面的互操作性尚未建立 [13]。
- **证据评估**：
  - 热度证据：arXiv 预印本 2026 年发布，系统对比三大框架 [13]。
  - 权威证据：arXiv preprint (cs.CY)，未经同行评审 [13]。
  - 关注度：中 —— 2026 年预印本，直接回应 EU/US/国际标准最新进展 [13]。
  - 推荐度：★★★☆☆ —— 覆盖核心框架，适合作为梳理切入点 [13]。

### 1.2 EU AI Act 生效与高风险合规要求落地
- **生效状态**：EU AI Act (Regulation (EU) 2024/1689) 已生效，对高风险 AI 系统设定强制性要求，旨在确保可信 AI 的开发与运行 [13, 15]。
- **高风险要求映射鸿沟**：EU AI Act 的高风险要求需系统映射至 AI 专用风险分类法，现有法律文本与技术风险分类之间存在映射鸿沟，合规落地缺乏结构化方法 [15]。
- **医疗高风险场景实证**：在工伤残风险预测、阿尔茨海默病风险预测等医疗 AI 场景中，EU AI Act 合规性与伦理审查面临具体落地挑战，需结合个案评估 [14]。
- **证据评估**：
  - 热度证据：两篇 2026 年预印本独立确认 [13, 15]；医疗案例研究一篇 [14]。
  - 权威证据：arXiv preprint (cs.CY, cs.AI)，未经同行评审 [13, 14, 15]。
  - 关注度：高 —— 多源佐证 EU AI Act 法律地位与高风险要求 [13, 15]。
  - 推荐度：★★★★☆ —— 直接对应 EU 核心法规生效进展 [13, 15]。

### 1.3 前沿 AI 政策与监管俘获风险并存
- **加州前沿 AI 政策报告**：加州发布前沿 AI 政策报告，探讨前沿 AI 创新带来的机遇与政策挑战，确立重要司法辖区治理基调 [6]。
- **监管俘获实证**：美国 AI 企业在通用 AI 系统监管对话中获得广泛影响力，存在监管俘获风险，即行业将监管制度用于优先考虑私人而非公共福利 [2]。
- **AI 权威感知改变人类决策**：1,305 名参与者实验显示，40% 以上参与者将 AI 视为预测自身行为的权威，放弃保证奖励几率增加 3.39 倍，收益减少 10.7-42.9%，即使预测反复失败效应仍存在 [1]。
- **证据评估**：
  - 热度证据：加州官方报告预印本 [6]；监管俘获实证分析 [2]；行为实验 N=1305 [1]。
  - 权威证据：arXiv preprint (cs.CY, cs.HC) [1, 2, 6]。
  - 关注度：中-高 —— 官方政策视角与实证行为科学双重支撑 [1, 2, 6]。
  - 推荐度：★★★★☆ —— 监管俘获与 AI 权威感知为治理核心议题 [1, 2]。

### 1.4 基础模型透明度指数呈下降趋势
- **透明度退步**：2025 年 Foundation Model Transparency Index (FMTI) 平均分从 2024 年的 58 跌至 40，企业在训练数据、算力及部署后影响方面最为不透明 [23]。
- **工具链采纳率低**：透明度下降表明模型卡、数据血缘、红队自动化、水印嵌入/检测等工具链在主流开发流程中采纳率极低 [23, 26]。
- **证据评估**：
  - 热度证据：连续三年透明度指数，业界公认基准 [23]。
  - 权威证据：arXiv preprint (cs.AI) [23]。
  - 关注度：高 —— 量化透明度退步，支撑合规工具链迫切需求 [23]。
  - 推荐度：★★★★☆ —— 高价值基准数据 [23]。

---

## 2. 工业界与产品

### 2.1 合规保证基础设施缺失：标准与工具链的“最后一公里”断层
- **核心痛点**：AI 合规保证框架（EU AI Act、ISO/IEC 42001、NIST AI RMF）规定了“要保证什么”，但缺乏可执行的机器可读证据基础设施，导致组织难以落地合规工程化 [26]。
- **工程化缺口**：成熟的政策脚手架缺乏运营化基础设施，三大框架均未提供可执行形式的合规证据格式 [26]。
- **证据评估**：
  - 热度证据：2026 年预印本直接切中三大框架落地鸿沟 [26]。
  - 权威证据：arXiv 预印本 (cs.CY) [26]。
  - 关注度：高 —— 精准对标合规工程化核心痛点 [26]。
  - 推荐度：★★★★★ —— 必读，为工具链调研提供问题锚点 [26]。

### 2.2 头部实验室“说-做”鸿沟与透明度实践
- **话语演变与实践脱节**：OpenAI 等头部实验室的伦理/安全话语随时间演变，但公开话语与实际工程工具链（红队、水印、联邦审计等）的对应关系缺乏系统性披露 [24]。
- **系统性风险模型合规探讨**：ESM3 等通用模型在 EU AI Act 下被讨论为具有系统性风险的通用 AI 模型，合规路径尚在探索 [19]。
- **LLM 对抗鲁棒性与合规**：针对 EU AI Act 合规性与 LLM 对抗鲁棒性的联合保障研究启动，工程化验证工具链初现 [16]。
- **证据评估**：
  - 热度证据：OpenAI 案例研究 [24]；ESM3 系统性风险分析 [19]；LLM 鲁棒性合规预印本 [16]。
  - 权威证据：arXiv preprint (cs.CY, cs.AI) [16, 19, 24]。
  - 关注度：中 —— 侧重话语分析与前沿模型合规探讨，工程工具链清单缺失 [16, 19, 24]。
  - 推荐度：★★★☆☆ —— 可作为企业承诺与工具链覆盖度对比的背景材料 [24]。

### 2.3 内部部署与网络安全合规细则浮现
- **内部部署合规**：EU AI Act 对内部部署的合规要求被单独剖析，工程落地细节进一步细化 [28]。
- **网络安全韧性要求**：EU AI Act 下的鲁棒性与网络安全要求成为产品级合规的硬性指标 [17]。
- **算法公平与非歧视条款**：高风险系统中算法公平与非歧视条款的复杂关系需工程化实现 [18]。
- **证据评估**：
  - 热度证据：内部部署 [28]、网络安全 [17]、公平性 [18] 专题预印本 2024-2025 年发布。
  - 权威证据：arXiv preprint (cs.CY, cs.AI) [17, 18, 28]。
  - 关注度：中 —— 细分合规工程需求浮现 [17, 18, 28]。
  - 推荐度：★★★☆☆ —— 为合规工具链功能模块提供细分需求清单 [17, 18, 28]。

---

## 3. 蓝海与缺口

### 3.1 三大框架控制级交叉映射的标准化空白
- **缺口描述**：ISO/IEC 42001、NIST AI RMF、EU AI Act 三大框架在控制层面的完整、准确交叉映射尚不存在，现有映射不完整且具误导性 [13]。
- **机会方向**：构建可机器执行的跨框架控制映射标准（如 OSCAL for AI），支撑多司法管辖区合规“一次认证、多地互认” [13, 26]。
- **证据评估**：
  - 热度证据：系统对比论文明确指出映射缺失 [13]。
  - 权威证据：arXiv preprint (cs.CY) [13]。
  - 关注度：中 —— 学术界已识别，工业界标准化组织（ISO/IEC JTC 1/SC 42）尚未发布成果 [13]。
  - 推荐度：★★★★☆ —— 高杠杆标准化机会，直接降低跨境合规成本 [13]。

### 3.2 法律文本到技术风险源的系统性映射方法缺失
- **缺口描述**：EU AI Act 高风险要求与 AI 专用技术风险分类法之间的系统性映射方法缺失，合规审计缺乏结构化证据链 [15]。
- **机会方向**：开发“法条-风险源-测试用例”三元知识图谱与自动化映射工具，支撑高风险 AI 系统的持续合规审计 [15, 26]。
- **证据评估**：
  - 热度证据：系统分析论文揭示映射鸿沟 [15]。
  - 权威证据：arXiv preprint (cs.AI) [15]。
  - 关注度：中 —— 前沿治理技术（可审计训练/合规映射）核心缺口 [15]。
  - 推荐度：★★★★☆ —— 对标准制定与审计工具开发有直接指导价值 [15]。

### 3.3 高风险垂直领域（医疗、金融、关键基础设施）合规工具链不成熟
- **缺口描述**：高风险医疗 AI 场景下，伦理审查与 AI Act 合规性评估的实操标准与工具链不成熟，缺乏可复用的合规证据模板 [14]。
- **机会方向**：垂直领域合规 SaaS 平台（医疗器械软件 MDR+AI Act 双合规、金融模型 SR 11-7+AI Act 映射） [14, 26]。
- **证据评估**：
  - 热度证据：医疗案例研究展示实操难点 [14]。
  - 权威证据：arXiv preprint (cs.CY) [14]。
  - 关注度：中 —— 单一案例研究，但揭示垂直领域通用痛点 [14]。
  - 推荐度：★★★☆ —— 垂直合规工具链为蓝海市场切入点 [14]。

### 3.4 机器可读合规证据基础设施（MRCE）完全空白
- **缺口描述**：EU AI Act / ISO 42001 / NIST RMF 要求的合规证据缺乏标准化的机器可读格式与开源工具链支撑 [26]。
- **机会方向**：基于 OSCAL、Linked Data 或 Verifiable Credentials 构建 AI 合规证据交换协议与开源参考实现 [26]。
- **证据评估**：
  - 热度证据：核心痛点论文明确指出基础设施缺失 [26]。
  - 权威证据：arXiv 预印本 (cs.CY) [26]。
  - 关注度：高 —— 合规工程化“最后一公里”核心基建 [26]。
  - 推荐度：★★★★★ —— 基础设施层机会，生态锚定价值极高 [26]。

---

## 4. 瓶颈与拐点

### 4.1 合规成本与创新速度的剪刀差扩大（瓶颈）
- **现状**：基础模型透明度指数下降（58→40）表明合规成本上升导致企业主动披露意愿下降，合规负担与创新速度形成剪刀差 [23]。
- **拐点信号**：若 EU AI Act 罚款落地（全球营收 7%/3500 万欧元），强制合规成本将倒逼工具链采纳率跃升，形成“合规即产品特性”的拐点 [13, 23]。
- **证据评估**：
  - 热度证据：FMTI 量化透明度退步 [23]；EU AI Act 罚款条款 [13]。
  - 权威证据：arXiv preprint (cs.AI, cs.CY) [13, 23]。
  - 关注度：高 —— 量化指标与法律强制力双重挤压 [13, 23]。
  - 推荐度：★★★★☆ —— 判断工具链市场爆发时机的关键变量 [13, 23]。

### 4.2 监管俘获导致治理有效性失真（瓶颈）
- **现状**：AI 企业在监管对话中获得广泛影响力，可能导致监管制度服务于私人而非公共福利，削弱治理有效性 [2]。
- **拐点信号**：若出现重大 AI 安全事件引发公众舆情反弹，或 G7/UN 层面达成强制透明度公约，可能打破俘获平衡 [2, 6]。
- **证据评估**：
  - 热度证据：实证分析监管俘获机制 [2]；加州报告呼吁公共利益优先 [6]。
  - 权威证据：arXiv preprint (cs.CY) [2, 6]。
  - 关注度：中 —— 政治经济学视角揭示结构性瓶颈 [2]。
  - 推荐度：★★★★☆ —— 核心治理议题，预判政策窗口期关键 [2]。

### 4.3 AI 权威感知侵蚀人类自主决策（新兴风险）
- **现状**：AI 预测被感知为权威时会改变人类推理并缩小决策未来空间，过度信任导致放弃保证收益，即使预测反复失败效应仍存在 [1]。
- **拐点信号**：随着 AI Agent 在高风险决策（医疗、司法、招聘）中部署，算法影响评估 (AIA) 必须纳入“心理自主性侵蚀”指标，否则合规评估将系统性低估风险 [1]。
- **证据评估**：
  - 热度证据：行为实验 N=1305，效应量显著 [1]。
  - 权威证据：arXiv preprint (cs.HC) [1]。
  - 关注度：中 —— 行为科学实证为算法治理提供新风险维度 [1]。
  - 推荐度：★★★★☆ —— 为 AIA 方法论升级提供实证基础 [1]。

### 4.4 评测基准与红队方法论的标准化滞后（瓶颈）
- **现状**：NTIRE 2026 等鲁棒 AI 生成检测挑战赛启动，但红队、水印、模型卡等评测基准缺乏跨厂商互认标准 [20]。
- **拐点信号**：NIST 牵头的 AI 安全研究院 (AISI) 联盟若发布统一红队方法论 v1.0，将催生合规评测工具链标准化爆发 [20]。
- **证据评估**：
  - 热度证据：NTIRE 2026 Challenge 论文 [20]。
  - 权威证据：arXiv preprint (cs.CV) [20]。
  - 关注度：中 —— 评测基准建设处于早期竞争阶段 [20]。
  - 推荐度：★★★☆ —— 关注 NIST AISI 标准化进程 [20]。

---

## 5. 社会·政策·国际

### 5.1 EU AI Act 确立“布鲁塞尔效应”新锚点
- **增量进展**：EU AI Act 作为全球首部综合性 AI 硬法生效，确立高风险分级、合格评定、市场监督全链条法律制度，输出“布鲁塞尔效应” [13, 15]。
- **国际协调**：G7 广岛进程、UN 高级别咨询机构报告均以 EU AI Act 为参照系推动国际互操作性 [13]。
- **证据评估**：
  - 热度证据：系统对比论文确认法律地位 [13]；高风险要求系统分析 [15]。
  - 权威证据：arXiv preprint (cs.CY, cs.AI) [13, 15]。
  - 关注度：高 —— 全球合规基线事实标准 [13, 15]。
  - 推荐度：★★★★★ —— 必须跟踪的政策锚点 [13, 15]。

### 5.2 美国“行政命令+州立法+自愿承诺”多层并行
- **增量进展**：联邦层面 EO 14110 推动 NIST RMF 与 AISI 建设；加州等州推动前沿 AI 立法（SB 1047 等）；白宫协调头部实验室自愿承诺 [6, 24]。
- **政策张力**：联邦-州权力分配、创新与安全平衡、监管俘获风险并存 [2, 6]。
- **证据评估**：
  - 热度证据：加州前沿 AI 政策报告 [6]；监管俘获实证 [2]；OpenAI 话语分析 [24]。
  - 权威证据：arXiv preprint (cs.CY) [2, 6, 24]。
  - 关注度：高 —— 美国治理模式直接影响全球科技巨头合规策略 [2, 6, 24]。
  - 推荐度：★★★★☆ —— 多层博弈格局下的合规策略制定参考 [2, 6]。

### 5.3 中国“备案制+标准引领”治理模式持续演进
> 待核实：结构化发现未覆盖中国最新备案制进展、TC260 标准体系、算法备案与模型备案的工程化落地细节。需补充官方文件（网信办、工信部、标准委）与权威智库报告。

### 5.4 全球南方与数字主权诉求上升
> 待核实：UN 全球数字契约、非盟 AI 战略、东盟 AI 治理指南等新兴市场治理主张的增量变化。需补充 UN/非盟/东盟官方文件。

---

## 6. 资本与生态

### 6.1 合规科技投资早期信号显现
- **增量判断**：风投开始关注 AI Governance, Risk, and Compliance (GRC) 赛道，但缺乏系统性融资数据披露 [21]。
- **量化框架雏形**：风险调整智能红利框架尝试整合 ISO 42001 与监管敞口量化 AI ROI，为投资决策提供理论锚点 [21]。
- **证据评估**：
  - 热度证据：量化框架预印本 2025 年发布 [21]。
  - 权威证据：arXiv preprint (cs.CY) [21]。
  - 关注度：低 —— 学术探索阶段，市场端数据不透明 [21]。
  - 推荐度：★★★☆ —— 为合规投资估值模型提供理论参考 [21]。

### 6.2 人才流动：政策/法律/工程复合型人才稀缺
> 待核实：缺乏招聘数据、薪资趋势、高校课程设置等量化证据。需补充 LinkedIn/猎头报告/高校课程目录。

### 6.3 开源生态：合规工具链碎片化，缺乏“Linux 级”核心项目
- **现状**：模型卡生成、数据血缘、红队自动化、水印嵌入/检测、联邦学习审计、差分隐私训练等工具链分散在不同 GitHub 仓库，缺乏统一框架与企业级采纳案例 [26, 23]。
- **关键缺失**：结构化发现中 key_projects 为空，表明无主导开源项目浮现 [26]。
- **证据评估**：
  - 热度证据：核心痛点论文指出基础设施缺失 [26]；FMTI 显示透明度工具采纳率低 [23]。
  - 权威证据：arXiv preprint (cs.CY, cs.AI) [23, 26]。
  - 关注度：高 —— 开源生态断层直接制约合规工程化普及 [23, 26]。
  - 推荐度：★★★★☆ —— 基础设施层开源机会窗口期 [23, 26]。

---

## 7. 信号与预测

### 7.1 信号：机器可读合规证据（MRCE）将成为下一代基建标准
- **观测依据**：EU AI Act/ISO 42001/NIST RMF 三大框架均缺可执行证据格式 [26]；OSCAL 在联邦信息系统授权中已成熟，向 AI 领域延伸为自然路径 [26]。
- **可证伪假设 (P)**：若到 2027 年 Q2，ISO/IEC JTC 1/SC 42 或 NIST 发布 AI 合规证据交换规范草案（基于 OSCAL/JSON-LD），则判断成立；否则推迟至 2028 年。置信度：较大概率 [26]。
- **证据评估**：
  - 热度证据：核心痛点论文明确呼吁 MRCE [26]。
  - 权威证据：arXiv 预印本 (cs.CY) [26]。
  - 关注度：高 —— 基建标准竞争早期信号 [26]。
  - 推荐度：★★★★★ —— 押注方向明确，工程可行性高 [26]。

### 7.2 信号：高风险 AI 合规审计将从“事后抽查”转向“持续自动化监控”
- **观测依据**：EU AI Act 要求高风险系统全生命周期合规 [13, 15]；法律文本到技术风险源映射缺失倒逼自动化工具研发 [15]；LLM 对抗鲁棒性联合合规研究启动 [16]。
- **可证伪假设 (P)**：若到 2026 年底，出现首个通过 EU 指定通知机构认证的“持续合规监控 SaaS 平台”（覆盖数据漂移、模型退化、对抗攻击实时检测），则判断成立。置信度：推测 [13, 15, 16]。
- **证据评估**：
  - 热度证据：高风险要求系统分析 [15]；LLM 鲁棒性合规预印本 [16]。
  - 权威证据：arXiv preprint (cs.AI, cs.CY) [13, 15, 16]。
  - 关注度：中 —— 技术就绪度与市场需求双向奔赴 [15, 16]。
  - 推荐度：★★★★☆ —— 合规服务商业化核心赛道 [15, 16]。

### 7.3 信号：基础模型透明度立法强制化趋势不可逆
- **观测依据**：FMTI 连续三年下降证明自愿透明度失效 [23]；EU AI Act 第 53 条要求通用模型提供技术文档与训练内容摘要 [13]；加州报告呼吁强制透明度 [6]。
- **可证伪假设 (P)**：若 2026-2027 年美国联邦或加州通过强制模型透明度立法（含训练数据版权披露、能耗报告、红队结果公开），则 FMTI 评分将在 2028 年反弹。置信度：较大概率 [6, 13, 23]。
- **证据评估**：
  - 热度证据：FMTI 量化退步 [23]；EU AI Act 条款 [13]；加州报告 [6]。
  - 权威证据：arXiv preprint (cs.AI, cs.CY) [6, 13, 23]。
  - 关注度：高 —— 立法时间表与透明度指数形成正反馈 [6, 13, 23]。
  - 推荐度：★★★★★ —— 确定性最高的政策趋势，直接催生合规工具刚需 [6, 13, 23]。

### 7.4 不确定因素：地缘政治碎片化导致合规标准分裂
- **风险判断**：中美欧在 AI 定义、风险分级、数据跨境流动、出口管制上的分歧可能导致“双轨制”甚至“多轨制”合规体系并存，大幅增加跨国企业合规成本 [13, 2]。
- **监测指标**：WTO/TBT 通报数量、ISO/IEC JTC 1/SC 42 中方提案采纳率、中美 AI 安全对话机制是否常态化 [13]。
- **证据评估**：
  - 热度证据：三大框架异构性分析 [13]；监管俘获分析暗示地缘博弈 [2]。
  - 权威证据：arXiv preprint (cs.CY) [2, 13]。
  - 关注度：高 —— 结构性不确定性，影响全球化部署策略 [2, 13]。
  - 推荐度：★★★★☆ —— 必须纳入企业全球合规战略的压力测试场景 [2, 13]。

### 7.5 预测：算法影响评估 (AIA) 将纳入“认知自主性”维度并强制化
- **预测依据**：行为实证证明 AI 权威感知侵蚀人类自主决策 [1]；EU AI Act 附件 IV 要求评估对基本权利的影响 [13]；NIST RMF 核心功能包含“治理/映射/测量/管理” [13]。
- **可证伪假设 (P)**：若到 2027 年，NIST AISI 发布的 AIA 指南草案明确包含“认知自主性/心理操纵”测试用例库，则判断成立。置信度：推测 [1, 13]。
- **证据评估**：
  - 热度证据：行为实验实证 [1]；框架系统对比 [13]。
  - 权威证据：arXiv preprint (cs.HC, cs.CY) [1, 13]。
  - 关注度：中 —— 新兴风险维度，标准化滞后于技术部署 [1]。
  - 推荐度：★★★★☆ —— 重新定义“高风险”边界的关键变量 [1]。

---

## 经典与奠基性工作

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Bridging AI Risk Frameworks: Reconciling ISO/IEC 42001, the NIST AI Risk Management Framework, and the EU AI Act into a Unified Governance Taxonomy | 2026 | arXiv Authors | > 待核实 | arXiv preprint (cs.CY) | 中 | ★★★☆☆ | [13] | 系统对比全球三大核心 AI 治理框架，奠基性综述性贡献 |
| How Do AI Companies "Fine-Tune" Policy? Examining Regulatory Capture in AI Governance | 2024 | arXiv Authors | > 待核实 | arXiv preprint (cs.CY) | 中 | ★★★★☆ | [2] | 实证分析 AI 企业监管俘获机制，治理政治经济学奠基性工作 |
| Faith in AI can narrow the futures individuals consider | 2026 | arXiv Authors | > 待核实 | arXiv preprint (cs.HC) | 中 | ★★★★☆ | [1] | 行为实证揭示 AI 权威感知侵蚀人类自主性，算法影响评估方法论奠基 |
| The California Report on Frontier AI Policy | 2025 | California Government | > 待核实 | arXiv preprint (cs.CY) | 中 | ★★★☆☆ | [6] | 重要司法辖区前沿 AI 系统性政策思考，政策制定参考价值高 |
| Beyond Citations: Comparing Scholarly, Policy, and Patent Impact Across the FT50 Journals | 2026 | arXiv Authors | > 待核实 | arXiv preprint (cs.DL) | 低 | ★★★☆☆ | [5] | 多维影响力评估框架，可用于评估 AI 治理文献政策渗透力 |

> 待核实：OECD AI Principles (2019)、EU Ethics Guidelines for Trustworthy AI (2019)、Asilomar AI Principles (2017)、Montreal Declaration (2018) 等经典框架的引用演进与影响力数据在候选证据中缺失，需补充 Google Scholar / Semantic Scholar 数据。

---

## 开源项目与工具链

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| > 待核实：主流合规工具链（模型卡生成、数据血缘、红队自动化、水印嵌入/检测、联邦学习审计、差分隐私训练）的 GitHub 活跃度、企业级采纳案例、与 EU AI Act / NIST RMF / ISO 42001 映射覆盖度 | - | - | > 待核实 | - | - | - | - | 结构化发现中 key_projects 为空，缺乏系统性开源项目调研数据 |

---

## 数据集与评测基准

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Foundation Model Transparency Index (FMTI) | 2023-2025 | Stanford CRFM / HAI | 高 (连续三年发布，广泛被引) | arXiv preprint (cs.AI) / 官方网站 | 高 | ★★★★☆ | [23] | 基础模型透明度量化基准，连续追踪 100+ 指标，直接支撑合规工具链需求论证 |
| NTIRE 2026 Challenge on Robust AI-Generated Image Detection in the Wild | 2026 | NTIRE / CVPR Workshop | 中 (挑战赛基准) | arXiv preprint (cs.CV) | 中 | ★★★☆☆ | [20] | 鲁棒 AI 生成内容检测基准，关联水印/检测工具链评测 |
| > 待核实：Open X-Embodiment, DROID, LIBERO, SimplerEnv, RoboArena 等具身智能基准在 AI 治理/合规维度的适用性 | - | - | - | - | - | - | - | 需补充评测维度映射分析 |

---

## 参考来源

[1] Faith in AI can narrow the futures individuals consider — http://arxiv.org/abs/2603.28944v2
[2] How Do AI Companies "Fine-Tune" Policy? Examining Regulatory Capture in AI Governance — http://arxiv.org/abs/2410.13042v1
[3] Foundations of GenIR — http://arxiv.org/abs/2501.02842v1
[4] Beyond principlism: Practical strategies for ethical AI use in research practices — http://arxiv.org/abs/2401.15284v6
[5] Beyond Citations: Comparing Scholarly, Policy, and Patent Impact Across the FT50 Journals — http://arxiv.org/abs/2606.17610v1
[6] The California Report on Frontier AI Policy — http://arxiv.org/abs/2506.17303v1
[7] Citation count distributions for large monodisciplinary journals — http://arxiv.org/abs/1607.04125v1
[8] MAGIC and MWL monitoring of the blazar TXS 0506+056 in the 2018/2019 season — http://arxiv.org/abs/1909.04938v1
[9] A Comparative Study of Removal Noise from Remote Sensing Image — http://arxiv.org/abs/1002.1148v1
[10] AIn't Nothing But a Survey? Using Large Language Models for Coding German Open-Ended Survey Responses on Survey Motivation — http://arxiv.org/abs/2506.14634v3
[11] A rich bounty of AGN in the 9 square degree Bootes survey: high-z obscured AGN and large-scale structure — http://arxiv.org/abs/astro-ph/0611654v1
[12] CAGI, the Critical Assessment of Genome Interpretation, establishes progress and prospects for computational genetic variant interpretation methods — http://arxiv.org/abs/2205.05897v1
[13] Bridging AI Risk Frameworks: Reconciling ISO/IEC 42001, the NIST AI Risk Management Framework, and the EU AI Act into a Uni ed Governance Taxonomy — http://arxiv.org/abs/2608.07515v1
[14] Ethics and EU AI Act in Cases of Work Disability Risk and Alzheimer's Disease Risk Prediction — http://arxiv.org/abs/2607.05402v1
[15] From Legal Text to AI-specific Risk Sources: A Systematic Analysis of the EU AI Act's High-Risk Requirements — http://arxiv.org/abs/2609.13535v1
[16] Towards Assuring EU AI Act Compliance and Adversarial Robustness of LLMs — http://arxiv.org/abs/2410.05306v1
[17] Robustness and Cybersecurity in the EU Artificial Intelligence Act — http://arxiv.org/abs/2502.16184v4
[18] It's complicated. The relationship of algorithmic fairness and non-discrimination provisions for high-risk systems in the EU AI Act — http://arxiv.org/abs/2501.12962v6
[19] The Case for ESM3 as a General-Purpose AI Model with Systemic Risk Under the EU AI Act — http://arxiv.org/abs/2605.01611v1
[20] NTIRE 2026 Challenge on Robust AI-Generated Image Detection in the Wild — http://arxiv.org/abs/2604.11487v1
[21] The Risk-Adjusted Intelligence Dividend: A Quantitative Framework for Measuring AI Return on Investment Integrating ISO 42001 and Regulatory Exposure — http://arxiv.org/abs/2511.21975v1
[22] Actionable Guidance for High-Consequence AI Risk Management: Towards Standards Addressing AI Catastrophic Risks — http://arxiv.org/abs/2206.08966v3
[23] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1
[24] Competing Visions of Ethical AI: A Case Study of OpenAI — http://arxiv.org/abs/2601.16513v1
[25] Docling: An Efficient Open-Source Toolkit for AI-driven Document Conversion — http://arxiv.org/abs/2501.17887v1
[26] Making AI Compliance Evidence Machine-Readable — http://arxiv.org/abs/2604.13767v1
[27] DeBiasMe: De-biasing Human-AI Interactions with Metacognitive AIED (AI in Education) Interventions — http://arxiv.org/abs/2504.16770v1
[28] Internal Deployment in the AI Act — http://arxiv.org/abs/2512.05742v4
[29] Intent-Aware Authorization for Zero Trust CI/CD — http://arxiv.org/abs/2504.14777v1
[30] Scalable CI/CD for Legacy Modernization: An Industrial Experience Addressing Internal Challenges Related to the 2025 Japan Cliff — http://arxiv.org/abs/2510.17430v1
[31] Decoupling Identity from Access: Credential Broker Patterns for Secure CI/CD — http://arxiv.org/abs/2504.14761v1

---

*Generated by research-bot · topic=`ai-治理与监管政策法规与标准` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`nvidia/nemotron-3-ultra-550b-a55b` · sources=31 · duration=404s · 2026-10-26T23:02:25+00:00*
