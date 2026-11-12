# AgentGuard：大模型 Agent 安全护栏与防御体系深度调研报告（2024-2026）

**日期**：2026-11-12（UTC） | **领域**：LLM Agent Safety / Guardrails / Red-Teaming / Compliance | **检索源数量**：157 条可引用证据 + 15 个种子资源

---

## 摘要（Executive Summary）

本报告系统梳理 2024-2026 年大模型 Agent 安全护栏的前沿进展、经典奠基工作、开源工程实践、评测基准与开放争议。核心发现：

1. **威胁模型已从单轮提示注入演进为多步工具链攻击**：间接提示注入、任务篡改、RAG 投毒、MCP 协议漏洞、过度代理成为核心攻击面 [1][2][3][4][5][6]。
2. **护栏架构呈现“分类→控制→形式化验证”三阶段演进**：从小模型分类器 [7]、语义防火墙 [8][9]、可编程规则引擎 [10] 向控制理论恢复机制 [11] 与运行时形式化验证 [12] 推进。
3. **评测基准从模型级转向 Agentic 级**：AgentDojo、InjecAgent、AgentHarm、HarmBench、MCP Security Bench 等构建可执行环境与动作图观测 [13]，但跨基准横向对比与复现脚本完备性仍有缺口 [q4-open]。
4. **主流开源框架（Guardrails AI、NeMo Guardrails、PurpleLlama、LLM Guard）缺乏统一的端到端延迟、误报率、DSL 表达力、热更新、集成难度的第三方横向实测** [q3-open][r2q2-open]。
5. **合规基线与工程落地存在“分类法—控制点”断层**：OWASP LLM Top 10 已用 7,714 真实事件实证校验 [14]，但 NIST AI RMF 与 MITRE ATLAS 向验证器门控、有界修复、策略护栏的显式映射缺失 [15][16][q6-open]。
6. **真实事件语料揭示专家排序与攻击面分布偏差**，企业级护栏部署仍处早期，零点击注入、AI 钓鱼、供应链投毒等失败模式频发 [17][18][19]。

> 待核实：具身智能/VLA/机器人本体上 Agent 护栏的专用适配与实测数据在现有证据中极少覆盖。

---

## 一、威胁模型与攻击面

### 1.1 直接/间接提示注入

| 攻击类型 | 代表性工作 | 核心机制 | 证据 |
|----------|------------|----------|------|
| 直接注入 | Automatic and Universal Prompt Injection Attacks [1] | 构造通用对抗后缀，绕过指令遵循约束 | [1] |
| 间接注入（奠基） | Not What You've Signed Up For [seed] | 通过外部数据源（网页、文档、邮件）植入恶意指令劫持 Agent | [seed] |
| 任务篡改型间接注入 | Beyond Instruction Override [2] | 攻击者控制内容不改变任务目标，而是篡改进行中任务的结果（如伪造退款证据） | [2] |
| RAG 投毒/黑盒对抗 | DeRAG [3] | 差分进化优化注入后缀，黑盒攻击多种 RAG 管线，导致检索重排与错误输出 | [3] |
| 视觉模态注入 | Mind Mapping Prompt Injection [20] | 图像中嵌入视觉提示词，诱导多模态模型执行恶意指令 | [20] |
| 取证溯源 | Prompt Scene Investigation [21] | 从 LLM 输出痕迹重构注入证据链，类数字取证 | [21] |

**关键演进**：2023 年奠基性工作确立间接注入威胁 [seed]；2024 年出现通用自动化攻击 [1]；2025-2026 年转向任务篡改 [2]、RAG 黑盒对抗 [3]、多模态注入 [20] 与取证溯源 [21]，攻击面从“指令覆盖”扩展到“任务完整性破坏”。

> 待核实：直接注入与间接注入在真实生产系统中的相对发生频次与损失量级对比。

### 1.2 工具滥用与过度代理

| 威胁 | 代表性工作 | 核心发现 | 证据 |
|------|------------|----------|------|
| 过度代理 | When Lower Privileges Suffice [6] | Agent 倾向选择高权限工具而非最小权限工具，导致权限提升风险 | [6] |
| 权限感知缺失 | Does Showing Agents the Privilege of Their Tools Reduce Over-Privileged Tool Selection? [22] | 显式展示工具权限可降低过度代理，但未根除 | [22] |
| 工具投毒/供应链 | Tool Poisoning and Trust Boundaries in MCP Ecosystems [19] | MCP 生态中工具元数据被篡改，导致下游 Agent 执行恶意动作 | [19] |
| 真实工具调用基准 | MCP-Universe [23] | 真实 MCP 服务器基准揭示现有评测过于简化，未捕捉真实工具调用复杂性 | [23] |

**核心洞察**：工具选择的最小权限原则在 Agent 自主决策中系统性缺失 [6][22]，MCP 等协议将工具作为一等可组合对象，放大了供应链投毒面 [19][23]。

### 1.3 数据外泄与隐私泄露

| 威胁 | 代表性工作 | 核心发现 | 证据 |
|------|------------|----------|------|
| 输出清洗残留 | Residual Privacy Leakage after Output Scrubbing [24] | 间接注入下，工具使用型 Agent 的输出清洗仍残留隐私泄露 | [24] |
| 指令认证中间件 | Real User Instruction: Black-Box Instruction Authentication Middleware [25] | 提出指令认证中间件对抗间接注入，但部署开销未量化 | [25] |
| 曝光先于成功 | Exposure Before Success in Indirect Prompt Injection Measurement [26] | 注入载荷在攻击成功前即可能泄露敏感上下文 | [26] |

> 待核实：多轮长上下文交互中 PII 泄露的累积概率与现有脱敏工具（如 Presidio [seed]）的实测拦截率对比。

### 1.4 MCP 协议专用攻击面

| 漏洞类别 | 代表性工作 | 核心贡献 | 证据 |
|----------|------------|----------|------|
| 漏洞数据集构建 | Tracing MCP Security Vulnerabilities [4] | 构建并分析 MCP 安全漏洞数据集，量化生态扩张带来的漏洞增长 | [4] |
| 威胁建模对比 | Security Threat Modeling for Emerging AI-Agent Protocols [5] | 对比 MCP、A2A、Agora、ANP 四大协议的威胁模型差异 | [5] |
| 生态系统全景 | Security of The Model Context Protocol Ecosystem [18] | 系统梳理 MCP 生态的新兴威胁、实证攻击证据、信任授权失效、供应链风险与防御策略 | [18] |
| 攻击基准 | MCP Security Bench (MSB) [27] | 专门针对 MCP 的攻击基准，覆盖工具发现、描述、调用全链路 | [27] |
| 多框架分析 | MCP Under the Lens [28] | 多安全框架视角分析 MCP | [28] |
| 攻击框架 | Mcploit [29] | MCP 枚举与利用框架 | [29] |
| 企业级防护 | Enterprise-Grade Security for MCP [30] | 企业级 MCP 安全框架与缓解策略 | [30] |
| 景观综述 | Model Context Protocol (MCP): Landscape, Security Threats, and Future Research Directions [31] | MCP 全景、威胁与未来方向综述 | [31] |
| 安全审计 | MCP Safety Audit [32] | 实测 MCP 允许重大安全漏洞利用 | [32] |
| 攻击证据 | MCP Under Attack [33] | MCP 生态安全风险实证 | [33] |

**趋势判断**：MCP 相关安全研究在 2025-2026 年爆发式增长，形成从漏洞收集 [4]、威胁建模 [5]、生态全景 [18] 到专用基准 [27]、攻击框架 [29]、企业级防护 [30] 的完整研究链条。

---

## 二、护栏架构与运行时防护

### 2.1 技术流派演进脉络

| 阶段 | 核心范式 | 代表性工作 | 防御原理 | 适用场景 | 已知局限 | 证据 |
|------|----------|------------|----------|----------|----------|------|
| 1.0 分类器时代 | 小模型分类器 | Detecting Prompt Injection Using Classifiers [7] | LSTM/前馈网络/随机森林/朴素贝叶斯在 HackAPrompt 语料上训练检测注入 | 低延迟、离线部署、明确攻击模式 | 易被自适应攻击绕过 [3]；泛化性依赖训练数据覆盖 | [7] |
| 1.5 统一检测 | 多威胁统一防御 | UniGuardian [34] | 单一模型同时检测提示注入、后门攻击、对抗攻击 | 统一检测入口，降低部署复杂度 | 未见大规模 Agentic 环境验证 | [34] |
| 2.0 语义防火墙 | 结构化查询/语义隔离 | StruQ [35]、ControlNET [9]、Firewalls to Secure Dynamic LLM Agentic Networks [8] | 结构化查询隔离用户输入与系统指令；RAG 专用防火墙；动态 Agent 网络防火墙 | RAG 系统、多 Agent 网络、需强隔离场景 | 规则维护成本高；动态环境策略同步难 | [35][9][8] |
| 2.5 可编程规则 | 对话护栏 DSL | NeMo Guardrails [10] | Colang 可编程对话护栏，支持话题限制、对话路径、事实核查 | 对话系统、需精细控制对话流场景 | 非对话型 Agent 适配性弱；DSL 学习曲线 | [10] |
| 3.0 控制理论 | 拒绝→恢复 | From Refusal to Recovery [11] | 控制理论方法：从输出分类转向预防下游物理/金融危害，引入恢复机制 | 安全关键场景（自动驾驶、金融助手）、需连续控制场景 | 理论模型与 LLM 离散生成的映射挑战；实测案例少 | [11] |
| 3.5 形式化验证 | 运行时可检查策略 | VEPA [12] | 形式化验证的演化策略，运行时在不可逆动作前做出确定性允许/拒绝决策，支持策略终身演化 | 高风险工具调用、需审计追踪、合规强制场景 | 可扩展性待验证；策略编写专业门槛高 | [12] |
| 3.5+ 正向安全 | 提示防火墙 | Beyond Injection Detection [36] | 正向安全模型：仅允许已知安全模式，关闭分类器遗漏的作用域与 PHI 缺口 | 医疗等高合规领域、PHI 保护 | 误报率与业务灵活性权衡未量化 | [36] |

**关键转折**：2024 年以分类器 [7]、结构化查询 [35]、可编程规则 [10] 为主；2025 年出现控制理论 [11]、RAG 防火墙 [9]、动态网络防火墙 [8]；2026 年推进形式化验证 [12] 与正向安全 [36]，标志着从“事后检测”向“事前可验证预防”跨越。

### 2.2 输入/输出过滤与 LLM Firewall

| 机制 | 代表工作 | 核心技术 | 部署位置 | 证据 |
|------|----------|----------|----------|------|
| 输入分类器 | [7] | 小模型分类器（LSTM/FFN/RF/NB） | 用户输入入口 | [7] |
| 结构化查询隔离 | StruQ [35] | 将用户输入结构化为参数化查询，防止指令注入 | RAG 检索前 | [35] |
| 统一多威胁检测 | UniGuardian [34] | 单模型多任务检测 | 统一入口 | [34] |
| RAG 专用防火墙 | ControlNET [9] | 监控检索-生成管线，拦截恶意检索结果 | RAG 生成前 | [9] |
| 动态 Agent 网络防火墙 | [8] | 网络层面的 Agent 间通信防火墙 | 多 Agent 通信层 | [8] |
| 正向安全防火墙 | [36] | 仅允许白名单模式，关闭作用域与 PHI 缺口 | 医疗/高合规出站 | [36] |

### 2.3 权限与沙箱隔离

| 机制 | 代表工作 | 核心技术 | 适用场景 | 证据 |
|------|----------|----------|----------|------|
| 最小权限工具选择 | [6][22] | 权限感知工具选择、显式权限展示 | Agent 自主工具调用 | [6][22] |
| MCP 沙箱/授权 | [30][19][27] | 企业级 MCP 框架、供应链信任边界、攻击基准 | MCP 生态部署 | [30][19][27] |
| 零信任架构 | Caging the Agents [37] | 医疗场景零信任 Agent 架构 | 高监管行业 | [37] |
| 沙箱反向工程 | SandBlaster [38] | Apple 沙箱反向分析（参考价值） | 系统级隔离研究 | [38] |

### 2.4 人在回路（HITL）与治理执行

| 机制 | 代表工作 | 核心技术 | 落地形态 | 证据 |
|------|----------|----------|----------|------|
| 自适应 HITL | Ariadne [39] | 人在回路自适应防御间接注入 | Web Agent | [39] |
| 类型化规划+治理执行 | POLARIS [16] | 类型检查 DAG 规划、鲁布里克引导推理、验证器门控、有界修复循环、编译期策略护栏三层防线 | 金融后办自动化 | [16] |
| NIST RMF 对齐治理平台 | AAGATE [40] | NIST AI RMF 对齐的 Agentic AI 治理平台 | 企业级合规 | [40] |
| 可审计决策制品 | POLARIS [16] | 完整执行轨迹、决策级制品、策略对齐 | 审计合规 | [16] |

**工程模式总结**：POLARIS [16] 展示了“类型化规划 → 鲁布里克引导 → 三层运行时护栏（验证器门控/有界修复/编译期策略）”的端到端治理执行范式，可直接映射为 HITL 审批点与策略强制机制。

---

## 三、安全评测与红队基准

### 3.1 主流 Agent 安全基准对比矩阵

| 基准 | 年份 | 机构 | 任务类型覆盖 | 攻击向量多样性 | 环境真实度 | 评测指标标准化 | 复现脚本完备性 | 热度/关注度 | 证据 |
|------|------|------|--------------|----------------|------------|----------------|----------------|-------------|------|
| AgentDojo | 2024 | ETH Zürich | 可执行环境中的提示注入攻防 | 直接/间接注入、工具滥用 | 高（可执行沙箱） | 攻击成功率、防御拦截率 | 开源环境 [seed] | 高 | [seed] |
| InjecAgent | 2024 | UIUC | 工具集成 Agent 的间接注入 | 间接注入、任务劫持 | 中（模拟工具） | 注入成功率、任务完成率 | 开源 [seed] | 高 | [seed] |
| AgentHarm | 2024 | CAIS | 多步工具链危害性 | 越狱、工具滥用、数据外泄 | 中（模拟环境） | 危害分数、拒答率 | 开源 [seed] | 高 | [seed] |
| JailbreakBench | 2024 | JailbreakBench | 越狱攻防标准评测 | 越狱提示词、多轮对抗 | 低（纯文本） | ASR、拒答一致性 | 开源 [seed] | 高 | [seed] |
| HarmBench | 2024 | CAIS | 自动化红队与拒答评测 | 标准化有害目标库 | 低（模型级） | 攻击成功率、拒答率 | 开源 [seed] | 高 | [seed][13] |
| MCP Security Bench | 2025 | - | MCP 协议攻击全链路 | 工具发现/描述/调用注入 | 高（真实 MCP 服务器） | 攻击成功率、漏洞覆盖 | [27] | 中 | [27] |
| AgentSeer + HarmBench | 2025 | - | Agentic 级红队对比 | 动作图观测下的迭代红队 | 中（GPT-OSS-20B + 工具） | 模型级 vs Agentic 级漏洞差距 | [13] | 中 | [13] |
| MOASEI Competition | 2026 | AAMAS | 多智能体决策（非安全导向） | 任务完成而非对抗 | 高（真实场景：野火/网安/网约车） | 任务完成数、时间、价值 | [41] | 低（非安全） | [41] |

**关键发现**：
- AgentDojo/InjecAgent/AgentHarm 形成 2024 年“三大基准”奠基 [seed]，但横向对比矩阵在证据中缺失 [q4-open][r2q3-open]。
- HarmBench 被作为 Agentic 红队的有害目标来源 [13]，AgentSeer 提供动作图观测能力 [13]。
- MCP Security Bench [27] 填补协议层评测空白，但复现脚本完备性待核实。
- MOASEI [41] 关注任务完成而非安全，参与度极低（8 队仅 1 队提交）。

> 待核实：AgentDojo、InjecAgent、AgentHarm 在相同 Agentic 系统上的评测一致性与相关性分析。

### 3.2 红队方法论演进

| 方法 | 代表工作 | 核心贡献 | 证据 |
|------|----------|----------|------|
| 多样化攻击学习 | Learning diverse attacks [42] | 学习多样化攻击用于鲁棒红队与安全调优 | [42] |
| 大规模数学幻觉红队 | Red Teaming at Scale [43] | 大规模数学任务幻觉红队 | [43] |
| Agentic 级 vs 模型级对比 | Mind the Gap [13] | 动作图观测下对比模型级与 Agentic 级红队，揭示部署层额外风险 | [13] |
| 意图操纵绕过内容审核 | Exploring Vulnerability of Content Moderation Guardrail [44] | 意图操纵绕过内容审核护栏 | [44] |

---

## 四、框架与工程实践

### 4.1 主流开源护栏框架对比

| 框架 | 年份 | 维护机构 | 核心特性 | DSL/规则语言 | 集成生态 | GitHub Stars | 热度/关注度 | 证据 |
|------|------|----------|----------|--------------|----------|--------------|-------------|------|
| Guardrails AI | 2023+ | guardrails-ai | 输入输出校验、结构化护栏、Pydantic 风格 | Rail 规范（XML/JSON） | LangChain、LlamaIndex | > 待核实 | 高 | [seed] |
| NeMo Guardrails | 2023 | NVIDIA | 可编程对话护栏、Colang、事实核查、话题控制 | Colang | LangChain、自有生态 | > 待核实 | 高 | [10][seed] |
| PurpleLlama | 2023+ | Meta | Llama Guard/CodeShield/Prompt Guard/LlamaFirewall 系列模型 | 模型权重+推理脚本 | HuggingFace、自有 | > 待核实 | 高 | [seed] |
| LLM Guard | 2023+ | ProtectAI | 输入输出扫描（注入、PII、敏感内容）、可插拔 | Python API | LangChain、自有 | > 待核实 | 中高 | [seed] |
| Presidio | 2022+ | Microsoft | PII 检测与脱敏、出站数据防泄露 | Python SDK、配置文件 | Azure、自有 | > 待核实 | 中 | [seed] |

> 待核实：上述框架在真实 Agent 部署中的端到端延迟（p50/p99）、误报率/漏报率、DSL 表达力、动态规则热更新、与 LangChain/LlamaIndex/AutoGen 集成难度的横向实测数据 [q3-open][r2q2-open]。

### 4.2 基准评测框架

| 基准 | 目标 | 覆盖框架 | 关键指标 | 证据 |
|------|------|----------|----------|------|
| CS-Guard | 代码生成安全护栏评测 | 多框架 | 攻击成功率、误报率 | [45] |
| Poly-Guard | 多领域安全策略护栏数据集 | 多框架 | 策略覆盖、检测准确率 | [46] |
| Benchmarking LLM Guardrails in Handling Multilingual Toxicity | 多语言毒性护栏评测 | 多框架 | 多语言检测 F1 | [47] |

### 4.3 工程成熟度关键缺口

1. **缺乏统一的延迟-准确率权衡基准**：CS-Guard [45]、Poly-Guard [46] 仅覆盖特定领域。
2. **动态规则热更新能力未量化**：NeMo Guardrails Colang 支持运行时更新 [10]，但生产级热加载稳定性无第三方报告。
3. **集成适配器维护负担**：LangChain/LlamaIndex/AutoGen 版本迭代快，框架适配器易失效。
4. **多语言/多模态支持不均**：Poly-Guard [46]、多语言毒性基准 [47] 显示非英语覆盖仍有短板。

---

## 五、企业落地与合规基线

### 5.1 合规基线映射现状

| 基线/标准 | 版本/年份 | 核心内容 | 与工程控制点映射 | 证据 |
|-----------|-----------|----------|------------------|------|
| OWASP LLM Top 10 | 2025/2026 | LLM01 提示注入、LLM06 过度代理等 10 大风险 | 事件驱动动态校验：7,714 真实事件实证专家排序偏差 [14] | [14][seed] |
| NIST AI RMF | 1.0/持续更新 | 治理、映射、度量、管理四功能 | AAGATE 平台声称对齐 [40]，但具体控制点映射缺失 [q6-open] | [40][q6-open] |
| MITRE ATLAS | 持续更新 | AI 系统 ATT&CK 式战术技术矩阵 | 与运行时护栏（验证器/修复/策略）显式映射缺失 [q6-open] | [seed][q6-open] |
| EU AI Act | 2024/2026 生效 | 高风险 AI 系统合规要求 | Agentic AI 责任边界定义滞后 [48] | [48] |
| 美国行政命令 | 2023/2024 | AI 安全标准化、红队要求 | 工程落地细则待细化 | [48] |
| 中国算法备案 | 2023-2026 | 生成式 AI 服务备案、安全评估 | 跨司法辖区责任边界不一 [q6-open] | [q6-open] |

### 5.2 工程落地范式对比

| 范式 | 代表工作 | 核心机制 | 合规对齐 | 落地成熟度 | 证据 |
|------|----------|----------|----------|------------|------|
| 事件驱动动态基线 | OWASP LLM Top 10 实证分析 [14] | 贝叶斯测量误差模型修正分类器，7,714 事件语料校验专家排序 | OWASP 社区共识 | 高（数据驱动） | [14] |
| 威胁建模骨架 | Towards trustworthy agentic AI [15] | 多步轨迹 Safety/Robustness/Privacy/System Security 两大维度、阶段化缓解 | 通用威胁模型 | 中（综述层面） | [15] |
| 类型化规划+治理执行 | POLARIS [16] | 类型检查 DAG、鲁布里克引导、三层运行时护栏（验证器门控/有界修复/编译期策略）、可审计轨迹 | 企业级金融合规 | 高（端到端实现） | [16] |
| NIST RMF 治理平台 | AAGATE [40] | NIST AI RMF 对齐的治理平台 | NIST RMF 显式对齐 | 中（平台早期） | [40] |
| 零信任医疗架构 | Caging the Agents [37] | 零信任 Agent 架构 | HIPAA/医疗合规 | 低（概念验证） | [37] |
| 多辖区适配框架 | SCITUS [49] | 加拿大语境下适配 NIST RMF | 跨司法辖区 | 低（区域性） | [49] |
| 企业级 MCP 安全 | Enterprise-Grade Security for MCP [30] | MCP 企业级框架与缓解 | 企业合规 | 中 | [30] |
| 合规控制操作化 | Operationalizing OWASP LLM Top 10 Controls [50] | 企业 AI 平台落地 OWASP 控制 | OWASP 控制操作化 | 中 | [50] |

### 5.3 核心断层与开放问题

1. **“分类法—控制点”映射缺失**：NIST AI RMF 与 MITRE ATLAS 向验证器门控、有界修复、编译期策略护栏的显式映射研究缺失 [15][16][q6-open]。
2. **动态基线工程化流水线缺失**：OWASP Top 10 与真实事件分布的动态校准未形成自动化流水线 [14][q6-open]。
3. **跨司法辖区责任边界不一**：EU AI Act、美行政命令、中国算法备案对 Agentic AI 定义差异导致统一合规栈难落地 [48][q6-open]。
4. **HITL 在高频低延迟控制回路的可行性缺乏量化基准** [q6-open]。

---

## 六、真实事件与失败模式

### 6.1 大规模事件语料实证

| 事件语料 | 规模 | 来源 | 核心发现 | 证据 |
|----------|------|------|----------|------|
| OWASP LLM Top 10 事件语料 | 7,714 快照、6,639 标注 | CVE、GHSA、OSV、AIAAIC | 专家排序与事件分布存在显著偏差；提示注入（LLM01）与过度代理（LLM06）占比高于专家预期 | [14] |
| 企业 AI 文档风险 | 2024-2025 记录 | 零点击注入、AI 钓鱼、供应链投毒 | 组织必须重新评估安全态势并部署企业级护栏 | [17] |
| MCP 生态漏洞 | 持续增长 | 漏洞数据集构建 [4] | 生态扩张导致漏洞增长；供应链、信任授权、工具投毒为主 | [4][18][19] |

### 6.2 典型失败模式分类

| 失败模式 | 触发条件 | 后果 | 代表性事件/论文 | 证据 |
|----------|----------|------|-----------------|------|
| 零点击提示注入 | 恶意邮件/文档自动处理 | 无需用户交互即执行恶意指令 | 企业 AI 助手零点击漏洞 [17] | [17] |
| 任务篡改型间接注入 | 外部数据源植入篡改载荷 | 正常任务结果被篡改（如伪造退款证据） | Beyond Instruction Override [2] | [2] |
| RAG 检索投毒 | 知识库注入对抗文档 | 生成错误/有害输出 | DeRAG 黑盒攻击 [3] | [3] |
| 过度代理权限提升 | Agent 自主选择高权限工具 | 敏感操作越权执行 | When Lower Privileges Suffice [6] | [6] |
| MCP 工具投毒 | 恶意工具元数据发布 | 下游 Agent 执行恶意动作 | Tool Poisoning in MCP [19] | [19] |
| 供应链漏洞传播 | 依赖组件含漏洞 | 全链路受影响 | MCP 生态供应链风险 [18][19] | [18][19] |
| 内容审核绕过 | 意图操纵构造对抗输入 | 有害内容通过审核 | Exploring Vulnerability of Content Moderation Guardrail [44] | [44] |
| 多模态注入 | 图像嵌入视觉提示词 | 多模态模型执行恶意指令 | Mind Mapping Prompt Injection [20] | [20] |
| 输出清洗残留泄露 | 间接注入下工具调用 | PII 经清洗仍泄露 | Residual Privacy Leakage [24] | [24] |

### 6.3 防御失效根因分析

1. **静态规则/分类器易被自适应攻击绕过**：DeRAG [3] 证明差分进化可黑盒优化注入后缀绕过静态护栏。
2. **单层防御缺乏纵深**：POLARIS 三层护栏 [16]、控制理论恢复机制 [11]、形式化验证 [12] 均指向多层/动态防御必要性。
3. **策略与执行脱节**：合规基线（OWASP/NIST/MITRE）未显式映射到运行时控制点 [q6-open]。
4. **观测盲区**：Agentic 系统内部动作图缺乏可观测性，AgentSeer [13] 尝试填补但复现性待验证。

---

## 七、争议与开放问题

### 7.1 技术争议

| 争议点 | 支持方观点 | 反对/质疑方观点 | 现有证据倾向 | 证据 |
|--------|------------|-----------------|--------------|------|
| 分类器 vs 形式化验证 | 形式化验证提供确定性保证 [12] | 可扩展性差、策略编写门槛高、LLM 离散生成难建模 | 早期阶段，仅 VEPA [12] 等少数工作，大规模实证缺失 | [12][r2q1-open] |
| 正向安全 vs 负向检测 | 正向安全关闭分类器盲区 [36] | 误报率高、业务灵活性受损、维护白名单成本大 | 仅医疗等高合规场景验证 [36]，通用性待证 | [36] |
| HITL 必要性 | 高风险决策必须人工审批 [16][39] | 高频低延迟场景（机器人控制）HITL 不可行 | 共识：分场景分风险等级，无银弹 | [16][39][q6-open] |
| 开源框架生产就绪度 | 社区活跃、生态集成好 [seed] | 缺乏第三方横向实测、延迟/误报/热更新数据缺失 | 证据不足，需独立基准 [q3-open][r2q2-open] | [q3-open][r2q2-open] |
| 合规基线动态化 | 事件驱动动态调整优于静态专家排序 [14] | 事件语料偏向已披露漏洞、零日攻击覆盖盲区 | 数据驱动优于纯专家，但需结合威胁情报 | [14] |

### 7.2 开放研究问题（汇总）

| 编号 | 问题 | 相关章节 | 紧迫度 |
|------|------|----------|--------|
| OP-1 | 形式化验证护栏在多智能体长周期任务中的可扩展性与策略演化机制实证 | 二、七 | 高 |
| OP-2 | 小模型分类器面对自适应黑盒攻击（DeRAG 类）的鲁棒性边界定量评估 | 二、七 | 高 |
| OP-3 | 主流开源框架端到端延迟、误报率、DSL 表达力、热更新、集成难度的第三方横向实测 | 四、七 | 高 |
| OP-4 | AgentDojo/InjecAgent/AgentHarm/MSB 跨基准横向对比与复现一致性验证 | 三、七 | 高 |
| OP-5 | NIST AI RMF / MITRE ATLAS 向运行时控制点（验证器/修复/策略）的标准化映射 | 五、七 | 高 |
| OP-6 | OWASP Top 10 等基线与真实事件分布的动态校准工程化流水线 | 五、七 | 中 |
| OP-7 | 跨司法辖区 Agentic AI 责任边界定义统一与合规栈适配 | 五、七 | 中 |
| OP-8 | HITL 在高频低延迟机器人控制回路中的可行性与性能权衡量化基准 | 二、五、七 | 中 |
| OP-9 | 具身智能/VLA/机器人本体上 Agent 护栏的专用适配与实测 | 全局 | 中 |
| OP-10 | 语义防火墙、规则引擎、多层防御流派 2024-2026 代表性学术论文与开源实现系统性梳理 | 二、七 | 中 |

---

## 八、个人可落地项目与 Watchlist

### 8.1 可落地项目建议（按工程投入排序）

| 项目 | 目标 | 核心技术栈 | 预计周期 | 关键里程碑 | 参考资源 |
|------|------|------------|----------|------------|----------|
| **最小权限工具选择器** | 在 Agent 工具调用链路植入权限感知选择策略 | LangChain/LlamaIndex + 自定义工具包装器 + 权限元数据注解 | 2-4 周 | 1) 权限元数据标准化 2) 选择器策略实现 3) 在 AgentDojo/InjecAgent 上评测过度代理降低率 | [6][22][seed-AgentDojo][seed-InjecAgent] |
| **运行时护栏中间件原型** | 基于 Colang/Guardrails Rail 实现可热更新的输入输出/工具调用拦截 | NeMo Guardrails / Guardrails AI + FastAPI 中间件 + Redis 配置中心 | 4-6 周 | 1) DSL 规则引擎选型 2) 热更新机制 3) 延迟/误报基准测试 4) 集成 AutoGen 多 Agent 场景 | [10][seed-Guardrails][seed-NeMo] |
| **MCP 沙箱与工具信任评分器** | 对 MCP 服务器工具进行静态分析与运行时沙箱执行，输出信任评分 | MCP SDK + 静态分析 + gVisor/Firecracker 沙箱 + 信任评分模型 | 6-8 周 | 1) MCP 工具元数据解析 2) 静态恶意模式检测 3) 沙箱执行观测 4) 在 MSB [27] 上验证 | [4][23][27][30][seed-MCP] |
| **Agentic 红队自动化流水线** | 基于 HarmBench 目标 + AgentSeer 观测，构建可复现的 Agentic 级红队 CI/CD | HarmBench + AgentSeer [13] + 自定义攻击插件 + GitHub Actions | 4-6 周 | 1) 部署 AgentSeer 观测 2) 接入 HarmBench 目标库 3) 实现迭代攻击循环 4) 生成漏洞报告制品 | [13][seed-HarmBench] |
| **合规控制点映射工具** | 将 OWASP LLM Top 10 / NIST AI RMF / MITRE ATLAS 条目映射为可执行的运行时护栏规则 | YAML/JSON 映射表 + 规则编译器（生成 Colang/Rail）+ 审计日志 | 6-10 周 | 1) 建立映射表（参考 POLARIS [16]、AAGATE [40]） 2) 规则编译器 3) 合规审计报告自动生成 | [14][15][16][40][seed-OWASP][seed-NIST][seed-MITRE] |

### 8.2 Watchlist（持续跟踪清单）

| 类别 | 关注对象 | 关注理由 | 跟踪信号 |
|------|----------|----------|----------|
| **前沿架构** | VEPA 形式化验证护栏 [12] | 首个面向 LLM Agent 的运行时形式化验证架构 | arXiv 更新、开源实现、第三方复现 |
| **前沿架构** | 控制理论护栏 [11] | 从拒绝走向恢复的范式转换 | 后续会议版本、真机部署案例 |
| **前沿架构** | 正向安全提示防火墙 [36] | 医疗合规场景的正向安全实践 | 开源发布、多语言扩展 |
| **基准演进** | AgentDojo/InjecAgent/AgentHarm v2+ | 三大基准的下一版本与统一评测协议 | GitHub Release、论文更新、榜单刷新 |
| **基准演进** | MCP Security Bench (MSB) [27] | 协议层攻击基准的标准化 | 新攻击向量覆盖、框架集成 |
| **基准演进** | HarmBench + AgentSeer 组合 [13] | Agentic 级红队方法论标准化 | 社区采用度、自动化程度 |
| **开源框架** | NeMo Guardrails 2.x / Guardrails AI 1.x | 核心框架大版本迭代（DSL、热更新、多模态） | GitHub Release Notes、Breaking Changes |
| **开源框架** | PurpleLlama 系列模型更新 | Llama Guard / Prompt Guard / CodeShield / LlamaFirewall 权重更新 | HuggingFace Hub、Meta 博客 |
| **合规标准** | OWASP LLM Top 10 2026/2027 版 | 事件驱动动态基线的工程化落地 | OWASP 官网、社区讨论、[14] 后续工作 |
| **合规标准** | NIST AI RMF 2.0 / MITRE ATLAS vNext | 标准与运行时控制点映射的官方指引 | NIST/MITRE 官方发布 |
| **协议安全** | MCP / A2A / Agora / ANP 安全演进 | 多协议共存下的统一威胁模型 [5] | 协议规范更新、漏洞披露、[5] 后续对比 |
| **真实事件** | AIAAIC / CVE / GHSA / OSV 中 LLM Agent 相关条目 | 事件语料驱动威胁模型迭代 | 定期爬取、聚类分析、趋势报告 |

---

## 参考来源（引用编号列表）
[1] Automatic and Universal Prompt Injection Attacks against Large Language Models — http://arxiv.org/abs/2403.04957v1
[2] Beyond Instruction Override: Benchmarking Indirect Prompt Injection with Task-Tampering Attacks — http://arxiv.org/abs/2611.07640v1
[3] DeRAG: Black-box Adversarial Attacks on Multiple Retrieval-Augmented Generation Applications via Prompt Injection — http://arxiv.org/abs/2507.15042v1
[4] Tracing MCP Security Vulnerabilities: Constructing and Analyzing an MCP Security Vulnerability Dataset — http://arxiv.org/abs/2611.11104v1
[5] Security Threat Modeling for Emerging AI-Agent Protocols: A Comparative Analysis of MCP, A2A, Agora, and ANP — http://arxiv.org/abs/2602.11327v2
[6] When Lower Privileges Suffice: Investigating Over-Privileged Tool Selection in LLM Agents — http://arxiv.org/abs/2606.20023v2
[7] Detecting Prompt Injection Attacks Against Application Using Classifiers — http://arxiv.org/abs/2512.12583v1
[8] Firewalls to Secure Dynamic LLM Agentic Networks — http://arxiv.org/abs/2502.01822v7
[9] ControlNET: A Firewall for RAG-based LLM System — http://arxiv.org/abs/2504.09593v2
[10] NeMo Guardrails: A Toolkit for Controllable and Safe LLM Applications with Programmable Rails — http://arxiv.org/abs/2310.10501v1
[11] From Refusal to Recovery: A Control-Theoretic Approach to Generative AI Guardrails — http://arxiv.org/abs/2510.13727v2
[12] VEPA: Verified Evolving Formal Policy for Lifelong LLM Agent Guardrails — http://arxiv.org/abs/2610.12813v1
[13] Mind the Gap: Comparing Model- vs Agentic-Level Red Teaming with Action-Graph Observability on GPT-OSS-20B — http://arxiv.org/abs/2509.17259v1
[14] Incident-Data Robustness Analysis of the OWASP Top 10 for LLM Applications (2026): How a Community-Expert Ranking Holds Up Against a Large-Scale LLM Incident Corpus — http://arxiv.org/abs/2608.19266v1
[15] Towards trustworthy agentic AI: a comprehensive survey of safety, robustness, privacy, and system security — http://arxiv.org/abs/2605.23989v1
[16] POLARIS: Typed Planning and Governed Execution for Agentic AI in Back-Office Automation — http://arxiv.org/abs/2601.11816v1
[17] Artificial Intelligence and Cybersecurity: Documented Risks, Enterprise Guardrails, and Emerging Threats in 2024–2025 — https://doi.org/10.36948/ijfmr.2025.v07i04.62200
[18] Security of The Model Context Protocol Ecosystem: Emerging Threats, Empirical Attack Evidence, Trust and Authorization Failures, Supply-Chain Risks, And Defensive Strategies — https://doi.org/10.64388/irev10i3-1723420
[19] Tool Poisoning and Trust Boundaries in Model Context Protocol (MCP) Ecosystems: A Systematic Review of 2025-2026 Vulnerabilities and a Defensive Reference Architecture — https://doi.org/10.2139/ssrn.7668659
[20] Mind Mapping Prompt Injection: Visual Prompt Injection Attacks in Modern Large Language Models — https://doi.org/10.3390/electronics14101907
[21] Prompt Scene Investigation: Uncovering the Evidence in LLMs — https://doi.org/10.6084/m9.figshare.34905075
[22] Does Showing Agents the Privilege of Their Tools Reduce Over-Privileged Tool Selection? — http://arxiv.org/abs/2610.40975v1
[23] MCP-Universe: Benchmarking Large Language Models with Real-World Model Context Protocol Servers — http://arxiv.org/abs/2508.14704v1
[24] Residual Privacy Leakage after Output Scrubbing in Tool-Using LLM Agents under Indirect Prompt Injection — https://doi.org/10.21203/rs.3.rs-11428254/v1
[25] Real User Instruction: Black-Box Instruction Authentication Middleware Against Indirect Prompt Injection — https://doi.org/10.20944/preprints202603.1023.v1
[26] Exposure Before Success in Indirect Prompt Injection Measurement — https://doi.org/10.20944/preprints202610.1741.v1
[27] MCP Security Bench (MSB): Benchmarking Attacks Against Model Context Protocol in LLM Agents — http://arxiv.org/abs/2510.15994v2
[28] MCP Under the Lens: A Multi-Framework Security Analysis of the Model Context Protocol — https://doi.org/10.5281/zenodo.18742289
[29] Mcploit: a Model Context Protocol Enumeration and Exploitation Framework — https://doi.org/10.1109/icdscnc70670.2026.11746266
[30] Enterprise-Grade Security for the Model Context Protocol (MCP): Frameworks and Mitigation Strategies — http://arxiv.org/abs/2504.08623v2
[31] Model Context Protocol (MCP): Landscape, Security Threats, and Future Research Directions — http://arxiv.org/abs/2503.23278v3
[32] MCP Safety Audit: LLMs with the Model Context Protocol Allow Major Security Exploits — http://arxiv.org/abs/2504.03767v2
[33] MCP Under Attack: Security Risks in the Model Context Protocol Ecosystem — https://doi.org/10.2139/ssrn.7330358
[34] UniGuardian: A Unified Defense for Detecting Prompt Injection, Backdoor Attacks and Adversarial Attacks in Large Language Models — http://arxiv.org/abs/2502.13141v2
[35] StruQ: Defending Against Prompt Injection with Structured Queries — http://arxiv.org/abs/2402.06363v2
[36] Beyond Injection Detection: A Positive-Security Prompt Firewall that Closes the Scope and PHI Gap SOTA Classifiers Miss in Healthcare — https://doi.org/10.64898/2026.06.04.26354950
[37] Caging the Agents: A Zero Trust Security Architecture for Autonomous AI in Healthcare — http://arxiv.org/abs/2603.17419v1
[38] SandBlaster: Reversing the Apple Sandbox — http://arxiv.org/abs/1608.04303v1
[39] Ariadne: Adaptive, Human-in-the-Loop Defense for AI Agents against Indirect Prompt Injection — https://doi.org/10.2139/ssrn.6870178
[40] AAGATE: A NIST AI RMF-Aligned Governance Platform for Agentic AI — http://arxiv.org/abs/2510.25863v2
[41] Second MOASEI Competition at AAMAS'2026: A Technical Report — http://arxiv.org/abs/2607.03399v1
[42] Learning diverse attacks on large language models for robust red-teaming and safety tuning — http://arxiv.org/abs/2405.18540v3
[43] Red Teaming for Large Language Models At Scale: Tackling Hallucinations on Mathematics Tasks — http://arxiv.org/abs/2401.00290v1
[44] Exploring the Vulnerability of the Content Moderation Guardrail in Large Language Models via Intent Manipulation — http://arxiv.org/abs/2505.18556v2
[45] CS-Guard: Benchmarking LLM Guardrails for Code Generation Security — http://arxiv.org/abs/2609.09798v1
[46] Poly-Guard: Massive Multi-Domain Safety Policy-Grounded Guardrail Dataset — http://arxiv.org/abs/2506.19054v3
[47] Benchmarking LLM Guardrails in Handling Multilingual Toxicity — http://arxiv.org/abs/2410.22153v1
[48] Security, privacy, and agentic AI in a regulatory view: From definitions and distinctions to provisions and reflections — http://arxiv.org/abs/2603.18914v1
[49] SCITUS: A Multi-Jurisdictional Framework for Adapting NIST AI RMF to the Canadian Regulatory Context — http://arxiv.org/abs/2607.15051v1
[50] Operationalizing OWASP LLM Top 10 Controls in Enterprise AI Platforms — https://doi.org/10.47941/jts.4051

---

*Generated by research-bot · topic=`agentguard` · depth=`standard` · rounds=2 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading · model=`nvidia/nemotron-3-ultra-550b-a55b` · sources=157 · duration=1544s · 2026-11-12T12:33:29+00:00*
