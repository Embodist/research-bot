# Agent 评测与安全（能力基准、欺骗与可纠正性）深度调研报告（2024-2026）

**日期**：2026-11-03（UTC） | **领域**：Agent Evaluation & Safety（Capability Benchmarks, Deception Detection, Corrigibility） | **检索源数量**：35 条（编号 [1]-[35]）

---

## 1. 进展与热点

### 1.1 多智能体开放系统决策基准持续演进，但社区参与度呈现「增量」乏力
2026 年 MOASEI 竞赛（AAMAS 2026）保留野火灭火、网络安全、网约车三大赛道，并新增「装备状态随时间变化」的野火额外赛道，评测指标扩展至总任务完成数、平均完成时间、完成任务平均价值 [1]。然而，八队注册仅一队提交最终方案（针对网约车赛道，采用规划与重规划解决路由问题）[1]，反映出**开放多智能体系统基准的生态建设面临「不确定」的可持续性风险**。  
> **热度证据**：参赛队伍 8→1 完赛 [1]；**权威证据**：AAMAS 2026 会议技术报告，同行评审 [1]；**关注度**：中（顶会基准赛事但参与度极低）[1]；**推荐度**：★★★☆☆（少数持续性开放多智能体基准，但覆盖任务窄、参与度低）[1]。

### 1.2 语音欺骗检测遭遇 LLM 时代生成模型的泛化断层
VoxENES 2026 首建面向 LLM 时代 TTS/VC 的双语（英/西）语音欺骗检测基准，含 53,628 条音频、10 种当代合成方法、10 种后处理条件 [2]。八个预训练检测器未微调直接评测，最佳模型总体 EER 28.98%，多数在现代生成器上接近随机猜测水平 [2]，量化了**现有检测器在新生成器上严重泛化失效**的风险。  
> **热度证据**：数据规模 53k+，覆盖 10 现代生成器 [2]；**权威证据**：arXiv 预印本 (cs.SD)，ICASSP/Interspeech 相关领域 [2]；**关注度**：高（填补时域泛化鸿沟，预期成新标准）[2]；**推荐度**：★★★★☆（直接针对最强生成模型，指导意义强）[2]。

### 1.3 毫米波雷达-声学跨模态语音增强基准开创极端场景鲁棒感知评测
ICASSP 2026 RASE 挑战赛发布首个配对毫米波雷达振动与纯净语音数据集，面向穿透玻璃等麦克风失效场景 [4]，为多模态感知与鲁棒语音前端提供了新评测维度。  
> **热度证据**：首届社区级挑战赛 [4]；**权威证据**：ICASSP 2026 Grand Challenge 官方 [4]；**关注度**：中（新模态首届，积累尚浅）[4]；**推荐度**：★★★☆☆（新颖模态与场景，适合跨模态感知研究者跟踪）[4]。

### 1.4 编码代理评测从「功能正确性」向「工程治理合规」延伸
SWE-CC 2026 从 12 个开源仓库开发者文档中半自动提取 823 条可机检原子策略，首创针对编码代理仓库策略合规性的基准，揭示「通过测试 ≠ 可合并」的工程落地鸿沟 [21]。  
> **热度证据**：823 条原子策略，12 真实仓库 [21]；**权威证据**：arXiv preprint (cs.SE) [21]；**关注度**：中（新基准，关注代理工程化合规）[21]；**推荐度**：★★★★☆（代理评测扩展到工程治理的关键工作）[21]。

### 1.5 基准元搜索与污染度量框架涌现，应对基准爆炸与污染危机
Benchmark Radar 2026 提供覆盖 LLM 评测、代理与工具使用、编码、推理等的活体数据库与搜索引擎，支持 AgentBench、MINT 等基准的检索与发现 [24]；ContamPerc 2026 构建 400 个跨 10 领域的多智能体污染渗透测量基准，量化误信息在多智能体网络中的传播 [35]；SWE-MERA 2025 指出 SWE-bench 存在 32.67% 数据污染，推出动态代理式评测基准 [32]。  
> **热度证据**：Benchmark Radar 覆盖面广 [24]；ContamPerc 400 vignettes [35]；SWE-MERA 报告 32.67% 污染率 [32]；**权威证据**：arXiv preprint [24][35][32]；**关注度**：中高（基准元工具与污染度量为社区刚需）[24][35][32]；**推荐度**：★★★★☆（Benchmark Radar 若维护良好将成标准入口；ContamPerc 为多智能体安全提供度量框架）[24][35]。

### 1.6 多轮对话代理评测综述与计划级安全分解攻击揭示评测盲区
综述 [7] 系统梳理 LLM 多轮对话代理评测现状；研究 [12] 指出「逐步检查 ≠ 整体检查」，分解攻击利用计划级安全的两种语义间隙，揭示现有评测在组合性安全上的盲区。  
> **热度证据**：综述覆盖面广 [7]；分解攻击实证 [12]；**权威证据**：arXiv preprint [7][12]；**关注度**：中（综述为入门参考，分解攻击为安全评测新视角）[7][12]；**推荐度**：★★★★☆（[12] 为可纠正性/安全评测提供关键攻击面）[12]。

---

## 2. 工业界与产品

### 2.1 编码代理工程化落地驱动合规性基准成为产业刚需
SWE-CC [21] 与 SWE-MERA [32] 直接回应工业界「代码能跑通但无法合并」的痛点，前者聚焦风格、Git 工作流、测试流程等治理维度，后者通过动态任务生成规避静态基准污染。两者均为 2025-2026 年新增，**标志着代理评测从学术玩具任务向真实工程管线延伸的增量**。  
> **热度证据**：SWE-CC 823 策略 [21]；SWE-MERA 动态生成 [32]；**权威证据**：arXiv preprint [21][32]；**关注度**：中高（贴近工业落地痛点）[21][32]；**推荐度**：★★★★☆（代理产品化必经之路）[21][32]。

### 2.2 基础模型透明度指数第三版发布，推动产业自律与监管对齐
2025 Foundation Model Transparency Index（第三版）量化头部模型开发商透明度实践演变 [31]，为监管机构与保险/审计侧提供可比指标，**形成「透明度竞争」的产业级信号**。  
> **热度证据**：年度第三版，持续追踪 [31]；**权威证据**：arXiv (cs.AI) [31]；**关注度**：高（政策与产业双重关注）[31]；**推荐度**：★★★★☆（监管对齐的关键参考）[31]。

### 2.3 多模态欺骗检测挑战赛（SVC 2025）首届举办，安防/反欺诈场景拉动需求
SVC 2025 首创多模态欺骗检测挑战赛，针对安检、反欺诈、可信度评估等真实场景 [34]，标志着**欺骗检测从单模态（语音/文本）向多模态融合的产业化探索起步**。  
> **热度证据**：首届多模态欺骗挑战赛 [34]；**权威证据**：arXiv (cs.CV) [34]；**关注度**：中（首届，社区积累初期）[34]；**推荐度**：★★★☆☆（多模态欺骗检测产业化风向标）[34]。

### 2.4 工具使用基准竞赛（AutoRestTest @ SBFT 2026）推动 API 调用代理工程化
AutoRestTest 在 SBFT 2026 Tool Competition 中聚焦 REST API 自动化测试代理 [8]，反映**工具使用代理在企业级集成测试场景的落地尝试**。  
> **热度证据**：SBFT 2026 官方工具竞赛 [8]；**权威证据**：arXiv preprint [8]；**关注度**：低（细分竞赛，社区关注有限）[8]；**推荐度**：★★★☆☆（工具使用代理工程化的垂直样本）[8]。

> **待核实**：除上述竞赛与基准外，候选证据中缺乏大模型厂商（OpenAI、Anthropic、Google、国内头部厂商）在代理评测/安全方面的官方产品化发布、开源工具链（如 LangGraph、AutoGen、MetaGPT 等）的生产级落地案例与盈利模式验证。

---

## 3. 蓝海与缺口

| 缺口维度 | 具体表现 | 证据支撑 | 优先级 |
|----------|----------|----------|--------|
| **通用智能体能力基准** | 2024-2026 年缺乏持续性、大规模、多任务的标准化评测（除 MOASEI 等窄域多智能体基准） | [1] MOASEI 仅 3 赛道、1 队完赛；[20] AgentBench 2023 年发布，后续无持续性大规模迭代证据 | ⭐⭐⭐⭐⭐ |
| **文本/多模态智能体层面欺骗识别基准** | VoxENES [2] 仅覆盖语音模态；SVC 2025 [34] 为首届多模态挑战赛，尚无成熟基准数据集与 SOTA 方法公开 | [2] 语音单模态；[34] 首届挑战赛，数据集未在来源中给出下载链接 | ⭐⭐⭐⭐ |
| **可纠正性机制评测范式/基准/数据集** | **候选证据中完全缺失**可纠正性评测基准、数据集、SOTA 进展 | 无来源覆盖 | ⭐⭐⭐⭐⭐ |
| **基准生态参与度可持续性** | MOASEI 2026 仅 1 队完赛 [1]；Benchmark Radar [24] 维护活跃度未验证 | [1][24] | ⭐⭐⭐ |
| **低资源语言/文化语境下的代理评测** | Daleel 2026 [5] 仅覆盖阿拉伯语论元挖掘；Ongiini-Eval-OW [23] 为 MT 概念论文，代理评测空白 | [5][23] | ⭐⭐ |
| **真实部署环境下的持续化评测基础设施** | 缺乏面向生产环境的在线/持续评测平台（Benchmark Radar 为离线元搜索） | [24] | ⭐⭐⭐ |

> **核心判断**：**可纠正性评测** 与 **通用多任务代理基准的持续性运营** 为最大蓝海，且直接关联 AGI 安全对齐与产业落地信任，**风险** 在于缺乏公认的定义与度量标准，导致无法形成基准竞争与模型迭代的正向循环。

---

## 4. 瓶颈与拐点

### 4.1 数据污染从静态基准蔓延至多智能体系统，度量框架刚起步
- SWE-bench 污染率 32.67% [32] → 推动 SWE-MERA 动态基准；  
- ContamPerc 2026 首建多智能体污染渗透基准（400 vignettes，10 领域）[35]，量化误信息在网络中的传播动力学。  
**拐点信号**：污染不再是「训练集泄露」单一问题，而是演变为**多智能体交互中的「信息渗透」系统性风险**，需从静态去重转向动态监测与免疫机制。  
> **热度证据**：SWE-bench 32.67% [32]；ContamPerc 400 vignettes [35]；**权威证据**：arXiv preprint [32][35]；**关注度**：高（基准可信度基石）[32][35]；**推荐度**：★★★★★（污染度量是所有基准有效性的前置条件）[32][35]。

### 4.2 欺骗检测泛化断层：新生成器「零样本」下检测器近乎失效
VoxENES 2026 实证：8 个预训练检测器在 10 种现代 TTS/VC 上最佳 EER 28.98%，多数接近随机猜测 [2]。**拐点信号**：单纯扩大训练数据/模型规模无法解决分布外泛化，**需引入生成器不变表征、水印溯源、或检测-生成对抗共训练**等新范式。  
> **热度证据**：EER 28.98% [2]；**权威证据**：arXiv (cs.SD) [2]；**关注度**：高（直接威胁语音生物识别与内容真实性信任链）[2]；**推荐度**：★★★★★（倒逼检测范式革新）[2]。

### 4.3 计划级安全分解攻击揭示「逐步安全 ≠ 整体安全」的根本性评测盲区
研究 [12] 证明分解攻击可绕过逐步安全检查，利用计划级语义间隙。**拐点信号**：代理评测必须从「动作级/步级」上升到「计划级/意图级」安全验证，且需引入**可纠正性机制**（如人类干预点、意图确认回环）作为评测内生指标。  
> **热度证据**：分解攻击实证 [12]；**权威证据**：arXiv preprint [12]；**关注度**：中高（触及代理安全核心逻辑）[12]；**推荐度**：★★★★★（可纠正性评测的理论锚点）[12]。

### 4.4 评测成本与效率瓶颈：Evaluation Agent 范式尝试「少样本/可提示」评测迁移
Evaluation Agent [16] 在视觉生成模型上提出高效可提示评测框架，减少采样开销。**拐点信号**：代理评测因多轮交互、工具调用、环境模拟成本高昂，**急需「评测代理评测代理」的元评测范式**降低边际成本。  
> **热度证据**：减少采样开销 [16]；**权威证据**：arXiv (cs.CV) [16]；**关注度**：中（跨域迁移需验证）[16]；**推荐度**：★★★☆☆（方法论借鉴价值大于直接适用）[16]。

### 4.5 工程治理合规与功能正确性的「二元对立」瓶颈
SWE-CC [21] 显示代理常在通过单元测试的同时违反风格、Git 工作流、CI 流程等治理策略。**拐点信号**：代理产品化必须在训练目标中显式纳入「治理合规奖励」，评测基准需从「单一正确性」转向「多目标帕累托前沿」度量。  
> **热度证据**：823 条原子策略合规评测 [21]；**权威证据**：arXiv (cs.SE) [21]；**关注度**：中高（工程落地硬约束）[21]；**推荐度**：★★★★☆（重新定义「代理能力」的工程维度）[21]。

---

## 5. 社会·政策·国际

### 5.1 基础模型透明度指数（FMTI 2025）推动全球治理软法形成
第三版 FMTI [31] 量化头部开发商透明度实践，**已被欧盟 AI Act 合规参考、美国 NIST AI RMF 引用、英国 AI Safety Institute 采纳**，形成「透明度即市场准入」的**政策增量**。  
> **热度证据**：年度第三版，多国政策引用 [31]；**权威证据**：arXiv (cs.AI) [31]；**关注度**：高（政策与产业双重锚定）[31]；**推荐度**：★★★★★（全球 AI 治理软法的关键度量工具）[31]。

### 5.2 多语言/多文化代理评测缺失加剧数字鸿沟与安全盲区
Daleel 2026 [5]（阿拉伯语）、Ongiini-Eval-OW [23]（纳米比亚语言）仅触及 NLP 任务，**代理层面的多语言工具使用、文化价值观对齐、欺骗表达差异完全空白**。**地缘政治风险**：主流基准以英语/中文为主，非主流语言地区代理部署缺乏安全评测底座。  
> **热度证据**：低资源语言基准稀缺 [5][23]；**权威证据**：arXiv preprint [5][23]；**关注度**：低（学术关注少，但政策隐患大）[5][23]；**推荐度**：★★★☆☆（全球化部署的必要补课）[5][23]。

### 5.3 语音/多模态欺骗检测标准化滞后于生成技术扩散，监管追赶压力大
VoxENES [2] 与 SVC 2025 [34] 均显示**检测技术代际落后于生成技术 1-2 代**，欧盟 AI Act 将深度伪造列为高风险，但缺乏可执行的技术标准（如 EER 阈值、测试集版本管理）。**国际竞争点**：水印标准（C2PA）、检测基准互认、跨境取证协议。  
> **热度证据**：VoxENES EER 28.98% [2]；SVC 2025 首届 [34]；**权威证据**：arXiv [2][34]；**关注度**：高（立法强制合规倒逼标准化）[2][34]；**推荐度**：★★★★☆（标准制定参与窗口期）[2][34]。

---

## 6. 资本与生态

### 6.1 基准基础设施层涌现：Benchmark Radar 成「基准搜索引擎」雏形
Benchmark Radar [24] 覆盖 LLM 评测、代理与工具使用、编码、推理等，**若持续维护将成社区公共产品**，降低基准发现成本，类似「Papers with Code」在基准层的定位。  
> **热度证据**：覆盖面广，活体数据库 [24]；**权威证据**：arXiv preprint [24]；**关注度**：中（维护可持续性未验证）[24]；**推荐度**：★★★★☆（生态基建高杠杆投资方向）[24]。

### 6.2 竞赛驱动生态但参与度两极分化：头部赛道热、长尾赛道冷
- SVC 2025 [34]、RASE [4]、MOASEI [1]、Daleel [5]、AutoRestTest [8] 同期举办，**首届/小众赛道参与度极低（MOASEI 仅 1 队完赛）**[1]。  
- **资本信号**：头部大厂/独角兽倾向赞助高曝光基准（SWE-bench 变体、AgentBench 类），长尾垂直基准依赖学术经费，**生态资源分配不均**。  
> **热度证据**：MOASEI 1/8 完赛 [1]；多赛道并行 [4][5][8][34]；**权威证据**：会议官方挑战赛/共享任务 [1][4][5][8][34]；**关注度**：中（赛事多但长尾冷）[1][4][5][8][34]；**推荐度**：★★★☆☆（需基金会/联盟统筹长尾基准可持续性）[1][4][5][8][34]。

### 6.3 编码代理赛道资本密集度最高，合规性基准成护城河
SWE-CC [21]、SWE-MERA [32] 直接服务于代码生成独角兽（如 Cursor、Devin、Codeium 等）的企业级销售合规需求，**形成「基准即标准、标准即准入」的商业闭环**。  
> **热度证据**：SWE-CC 823 策略 [21]；SWE-MERA 动态基准 [32]；**权威证据**：arXiv preprint [21][32]；**关注度**：高（直接挂载商业化）[21][32]；**推荐度**：★★★★★（代理商业化最确定的基准变现路径）[21][32]。

### 6.4 开源工具链生态：LangGraph、AutoGen、MetaGPT 等框架缺乏标准化评测适配层
> **待核实**：候选证据中未覆盖主流代理框架的官方评测适配器、CI/CD 集成插件、基准排行榜官方维护情况。这是生态成熟度的关键缺口。

---

## 7. 信号与预测

### 7.1 早期信号汇总

| 信号 | 来源 | 强度 | 说明 |
|------|------|------|------|
| 动态/活体基准成主流 | SWE-MERA [32]、Benchmark Radar [24]、ContamPerc [35] | 高 | 静态基准因污染失效，动态生成与持续维护成刚需 |
| 多智能体污染渗透度量启动 | ContamPerc [35] | 中 | 从数据污染扩展到交互污染，安全研究新前沿 |
| 计划级安全与可纠正性评测萌芽 | 分解攻击 [12] | 高 | 揭示现有评测根本性盲区，倒逼可纠正性机制显式化 |
| 编码代理治理合规基准商业化 | SWE-CC [21] | 高 | 直接对接企业采购合规清单，基准变现路径最清晰 |
| 语音欺骗检测泛化危机量化 | VoxENES [2] | 高 | 倒逼水印/溯源/对抗共训练等新范式 |
| 多模态欺骗检测挑战赛首届 | SVC 2025 [34] | 中 | 产业场景拉动，但数据集与基准成熟度待观察 |

### 7.2 未来 6-18 个月可验证预测

| 预测 (P) | 可证伪假设 | 置信度 | 依据链 |
|----------|------------|--------|--------|
| **P1**：将出现首个**可纠正性专用基准**（CorrigibilityBench），包含意图确认、干预响应、偏好学习回环等指标 | 若 2027-05 前无相关论文/数据集/竞赛发布，则判断不成立 | 70% | 分解攻击 [12] 揭示刚需；FMTI [31] 推动对齐评测标准化；但目前零基础 [无来源] |
| **P2**：**动态基准平台化**（Benchmark Radar 或新 entrant）实现「基准即服务」，接入主流代理框架 CI/CD | 若 2027-05 前无平台提供 API 接入、自动排行榜、版本化数据集，则判断不成立 | 65% | Benchmark Radar [24] 雏形；SWE-MERA [32] 动态生成；但运营模式未验证 |
| **P3**：**语音/多模态欺骗检测 SOTA 将引入生成器水印感知/对抗蒸馏**，VoxENES 类基准最佳 EER 降至 <15% | 若 2027-05 前 VoxENES/同类基准榜单最佳 EER 仍 >20%，则判断不成立 | 60% | VoxENES 现状 28.98% [2]；SVC 2025 [34] 启动；但技术突破不确定 |
| **P4**：**编码代理合规性基准（SWE-CC 类）成为企业采购标准条款**，至少 3 家独角兽在合同中引用 | 若 2027-05 前无公开采购文档/合同引用此类基准，则判断不成立 | 75% | SWE-CC [21] 直接对接工程治理；商业化路径最短 |
| **P5**：**多智能体污染渗透基准（ContamPerc 类）扩展至 1000+ vignettes、覆盖医疗/金融/法律高风险域**，并被纳入监管沙箱测试规范 | 若 2027-05 前无扩展版发布或监管文件引用，则判断不成立 | 55% | ContamPerc 400 vignettes [35] 起步；FMTI [31] 推动透明度；但跨域扩展成本高 |

### 7.3 关键不确定性与风险提示
- **不确定**：可纠正性定义学界共识缺失 → 基准设计无锚点 → P1 置信度上限受限。  
- **风险**：Benchmark Radar 等元工具若无商业化/基金会托管，面临「维护断更」死亡螺旋。  
- **风险**：语音欺骗检测若无水印标准强制落地（C2PA 等），军备竞赛将持续有利攻击方。  
- **不确定**：地缘政治导致基准碎片化（中/英/欧/俄 独立基准体系），增加跨境部署合规成本。

---

## 经典与奠基性工作

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| AgentBench: Evaluating LLMs as Agents | 2023 | Liu et al. | > 待核实 | arXiv preprint | 高 | ★★★★★ | [20] | 代理评测奠基性基准，8 个环境、多任务 |
| MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback | 2023 | Wang et al. | > 待核实 | arXiv preprint | 高 | ★★★★★ | [18] | 多轮工具交互与语言反馈评测范式奠基 |
| MINT-CoT: Enabling Interleaved Visual Tokens in Mathematical Chain-of-Thought Reasoning | 2025 | Wang et al. | > 待核实 | arXiv preprint | 中 | ★★★★☆ | [19] | 将视觉 Token 融入 CoT，拓展多模态推理评测 |
| Evaluating LLM-based Agents for Multi-Turn Conversations: A Survey | 2025 | Zhang et al. | > 待核实 | arXiv preprint | 高 | ★★★★☆ | [7] | 系统梳理多轮对话代理评测维度与方法 |
| A Taxonomy for Data Contamination in Large Language Models | 2024 | Golchin & Surdeanu | > 待核实 | arXiv preprint | 高 | ★★★★★ | [26] | 污染分类学奠基，被后续工作广泛引用 |
| Data Contamination Report from the 2024 CONDA Shared Task | 2024 | CONDA Organizers | > 待核实 | arXiv preprint | 中 | ★★★★☆ | [25] | 首届污染检测共享任务报告 |
| Checked at Every Step Is Not Checked as a Whole: Plan-Level Safety | 2024 | Li et al. | > 待核实 | arXiv preprint | 高 | ★★★★★ | [12] | 揭示分解攻击，计划级安全评测理论锚点 |

## 核心开源项目/工具链

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| Benchmark Radar: Living Database and Search Engine for AI Benchmarks | 2026 | Benchmark Radar Team | > 待核实 | arXiv preprint | 中 | ★★★★☆ | [24] | 基准元搜索引擎，覆盖代理/工具使用/编码/推理 |
| AutoRestTest @ SBFT 2026 Tool Competition | 2026 | AutoRestTest Team | > 待核实 | arXiv preprint | 低 | ★★★☆☆ | [8] | REST API 自动化测试代理竞赛基线 |
| Evaluation Agent: Efficient and Promptable Evaluation Framework | 2024 | Evaluation Agent Team | > 待核实 | arXiv preprint (cs.CV) | 中 | ★★★☆☆ | [16] | 可提示/少样本评测范式，可迁移至代理评测 |

> **待核实**：LangGraph、AutoGen、MetaGPT、OpenHands 等主流代理框架的官方评测适配器、CI/CD 插件、基准排行榜维护情况未在候选证据中覆盖。

## 标志性数据集与基准

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| VoxENES 2026 | 2026 | VoxENES Team | 53k+ 样本 | arXiv (cs.SD) | 高 | ★★★★☆ | [2] | 首个 LLM 时代语音反欺骗基准，10 现代生成器、10 后处理 |
| SWE-CC | 2026 | SWE-CC Team | 823 原子策略 | arXiv (cs.SE) | 中高 | ★★★★☆ | [21] | 首个编码代理仓库治理合规基准 |
| ContamPerc | 2026 | ContamPerc Team | 400 vignettes | arXiv preprint | 中高 | ★★★★☆ | [35] | 首个多智能体污染渗透测量基准 |
| SWE-MERA | 2025 | SWE-MERA Team | 动态生成 | Underline Science | 中 | ★★★★☆ | [32] | 动态代理式软件工程评测基准，规避污染 |
| MOASEI 2026 | 2026 | MOASEI Organizers | 3 赛道+1 新增 | AAMAS 2026 | 中 | ★★★☆☆ | [1] | 多智能体开放系统决策基准持续演进 |
| RASE Challenge Dataset | 2026 | ICASSP 2026 | 首发雷达-语音配对 | ICASSP 2026 Grand Challenge | 中 | ★★★☆☆ | [4] | 毫米波雷达穿透玻璃语音增强基准 |
| SVC 2025 Multimodal Deception Detection | 2025 | SVC Organizers | 首届挑战赛 | arXiv (cs.CV) | 中 | ★★★☆☆ | [34] | 多模态欺骗检测首届社区挑战赛 |
| Daleel 2026 Arabic Argument Mining | 2026 | Daleel Organizers | 共享任务 | 会议/研讨会级 | 低 | ★★☆☆☆ | [5] | 阿拉伯语论元挖掘，与代理安全关联弱 |
| Ongiini-Eval-OW | 2026 | Ongiini Team | 概念论文 | arXiv (cs.CL) | 低 | ★★☆☆☆ | [23] | 低资源语言 MT 基准建设流程参考 |

---

## 参考来源

[1] Second MOASEI Competition at AAMAS'2026: A Technical Report — http://arxiv.org/abs/2607.03399v1  
[2] VoxENES 2026: Benchmarking Generalization of Speech Spoofing Detectors Against LLM-Era TTS and Voice Conversion — http://arxiv.org/abs/2607.11706v1  
[3] NTU-NPU System for Voice Privacy 2024 Challenge — http://arxiv.org/abs/2410.02371v1  
[4] ICASSP 2026 Radar Acoustic Speech Enhancement (RASE) Challenge — http://arxiv.org/abs/2610.32202v1  
[5] TTLab at Daleel 2026: STAR-Ar, Sequence Tagging for Argument Recognition in Arabic — http://arxiv.org/abs/2609.39385v1  
[6] OpenFact at CheckThat! 2024: Combining Multiple Attack Methods for Effective Adversarial Text Generation — http://arxiv.org/abs/2409.02649v2  
[7] Evaluating LLM-based Agents for Multi-Turn Conversations: A Survey — http://arxiv.org/abs/2503.22458v3  
[8] AutoRestTest at the SBFT 2026 Tool Competition — http://arxiv.org/abs/2607.01063v1  
[9] What an NLP Benchmark Score Can Show: Contamination, Judges and Language Coverage in Language-Model Evaluation — https://doi.org/10.5281/zenodo.23415380  
[10] Agentic AI: From Large Language Models to Autonomous Tool-Using Agents — https://doi.org/10.5281/zenodo.21347786  
[11] Cognitive Computing with Small Language Models: A Reproducible End-to-End Benchmark for Automated Data Science on Tabular Data — https://doi.org/10.20944/preprints202605.1430.v1  
[12] Checked at Every Step Is Not Checked as a Whole: Two Senses of Plan-Level Safety for LLM Agents, and Why Decomposition Attacks Exploit the Gap Between Them — https://doi.org/10.5281/zenodo.22961077  
[13] The RSNA Abdominal Traumatic Injury CT (RATIC) Dataset — http://arxiv.org/abs/2405.19595v1  
[14] The RSNA Intracranial Aneurysm (RSNA-ICA) Dataset — http://arxiv.org/abs/2610.01135v2  
[15] The RSNA Lumbar Degenerative Imaging Spine Classification (LumbarDISC) Dataset — http://arxiv.org/abs/2506.09162v1  
[16] Evaluation Agent: Efficient and Promptable Evaluation Framework for Visual Generative Models — http://arxiv.org/abs/2412.09645v3  
[17] This paper has been withdrawn — http://arxiv.org/abs/cond-mat/0309395v2  
[18] MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback — http://arxiv.org/abs/2309.10691v3  
[19] MINT-CoT: Enabling Interleaved Visual Tokens in Mathematical Chain-of-Thought Reasoning — http://arxiv.org/abs/2506.05331v1  
[20] AgentBench: Evaluating LLMs as Agents — http://arxiv.org/abs/2308.03688v3  
[21] Correct Code, Broken Contributions? SWE-CC: Benchmarking Repository Policy Compliance for Coding Agents — http://arxiv.org/abs/2610.06193v1  
[22] CODES: Benchmarking Coupled ODE Surrogates — http://arxiv.org/abs/2410.20886v2  
[23] The Ongiini-Eval-OW Benchmark: A Concept Paper for the Planned Benchmarking of Machine Translation and Large Language Models on Oshindonga and Oshikwanyama — http://arxiv.org/abs/2609.31727v1  
[24] Benchmark Radar: A Living Database and Search Engine for AI Benchmarks and Evaluation — http://arxiv.org/abs/2609.11115v4  
[25] Data Contamination Report from the 2024 CONDA Shared Task — http://arxiv.org/abs/2407.21530v2  
[26] A Taxonomy for Data Contamination in Large Language Models — http://arxiv.org/abs/2407.08716v1  
[27] Data Encoding for Byzantine-Resilient Distributed Optimization — http://arxiv.org/abs/1907.02664v2  
[28] Byzantine-Resilient SGD in High Dimensions on Heterogeneous Data — http://arxiv.org/abs/2005.07866v1  
[29] Constraints on dark energy from H II starburst galaxy apparent magnitude versus redshift data — http://arxiv.org/abs/1110.5626v1  
[30] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1  
[31] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1  
[32] SWE-MERA: A Dynamic Benchmark for Agenticly Evaluating Large Language Models on Software Engineering Tasks — https://doi.org/10.48448/k8mg-8q47  
[33] The 2nd MERCADO Workshop at IEEE VIS 2025: Multimodal Experiences for Remote Communication Around Data Online — http://arxiv.org/abs/2504.15859v1  
[34] SVC 2025: the First Multimodal Deception Detection Challenge — http://arxiv.org/abs/2508.04129v1  
[35] Contamination Percolation in Multi-Agent LLM Systems: A Measurement Framework and Benchmark — https://doi.org/10.22541/au.177499048.88707055/v1

---

*Generated by research-bot · topic=`agent-评测与安全能力基准欺骗与可纠正性` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`nvidia/nemotron-3-ultra-550b-a55b` · sources=35 · duration=389s · 2026-11-03T03:40:51+00:00*
