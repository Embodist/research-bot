# AgentGuard：LLM Agent 护栏与安全架构深度调研报告（2024-2026）

**日期**：2026-11-12（UTC） | **领域**：具身智能 / VLA / Agent 安全 / LLM 护栏 | **检索源数量**：195 条可引用证据源

---

## 摘要（Executive Summary）

本报告系统梳理 2024-2026 年大模型 Agent 安全护栏的前沿进展、经典奠基工作、开源工程实践、评测基准与开放争议。核心发现：① **提示词注入（直接/间接）仍是首要攻击面**，已形成从漏洞分类到运行时防御的完整研究链条 [1][2][3][4]；② **护栏架构正从静态分类转向“运行时契约/技能化/控制理论”新范式**，SDB 架构契约 [5] 与 Defense-as-Skill [6] 成为代表性进展；③ **评测基准向“可执行环境/多步工具链/运行时验证”演进**，AgentDojo [7][8]、InjecAgent [7][8]、AgentHarm [9]、MalSkillBench [10] 形成梯次覆盖；④ **开源框架（NeMo Guardrails、Guardrails AI、PurpleLlama、LLM Guard）已进入生产级安全自动化管线**，但横向性能基准缺失 [11][12][13]；⑤ **合规基线（OWASP LLM Top 10、NIST AI RMF、MITRE ATLAS、ATX-1）与 Agent 威胁建模初步对齐**，但事件数据显示专家排序与实战偏差显著 [14][15][16]。报告指出：计划级安全盲区、多模态/代码混合泛化、护栏与推理引擎低延迟集成、真机具身场景端到端验证为四大核心开放问题。

---

## 一、威胁模型与攻击面

### 1.1 直接/间接提示注入
- **直接注入**：攻击者通过用户输入直接覆盖系统提示词，导致模型执行非预期指令。系统性综述覆盖 2023-2025 年 45 个关键来源，确立漏洞分类与防御机制全景 [1]。
- **间接注入（IPI）**：攻击者通过外部数据源（网页、文档、邮件、工具返回）植入恶意指令，劫持 Agent 工具调用链。最新基准从“指令覆盖”转向“任务篡改”，揭示现有基准低估真实风险 [2][4][17][18]。
- **跨模态/代码混合注入**：TanglishGuard 揭示主流护栏在泰米尔-英语代码混合提示上近乎失效 [19]；多模态注入（图像/语音载荷）尚无统一基准 [20][21]。

### 1.2 工具滥用与过度代理
- **过度权限工具选择**：Agent 倾向选择高权限工具而非最小权限，扩大攻击面 [22]。
- **MCP 协议供应链风险**：MCP 生态快速扩张伴随漏洞激增，已构建专用漏洞数据集 [23] 与实战基准 MCP-Universe [24]、MCP Security Bench [25]。
- **工具投毒与信任边界**：工具描述被篡改诱导恶意调用，需条件非升级不变量约束 [26][27]。

### 1.3 数据外泄与隐私越界
- **污点流追踪**：Tool-Flow Taint Analysis 从工具调用链建模数据外泄路径 [28]。
- **RAG 语料投毒**：DeRAG 通过差分进化优化对抗后缀，操纵检索排序导致错误输出 [29]。
- **持久上下文秘密泄露**：Defense-as-Skill 指出恶意技能可在持久上下文中分阶段窃取秘密、污染代码、绕过审批、暂存数据外泄 [6]。

### 1.4 计划级分解攻击
- **逐步检查 ≠ 整体安全**：现有护栏多在单步工具调用或单步 (observation, action) 级别判断，分解攻击利用步级与计划级鸿沟绕过防护 [30]。
- **多步工具链危害**：AgentHarm 基准覆盖多步工具链危害性评测 [9]。

> 待核实：具身智能场景下（VLA/运动规划实时回路）的注入向量与物理危害映射关系尚无系统性文献。

---

## 二、护栏架构与运行时防护

### 2.1 输入/输出过滤与结构化约束
- **分类器检测**：基于 HackAPrompt 语料训练 LSTM/Transformer 分类器检测注入 [31]。
- **结构化查询防御**：StruQ 通过结构化查询将用户输入与系统指令隔离 [32]。
- **令牌级引导**：Microsoft Guidance / Guardrails AI 通过语法约束限制输出格式 [12][13]。

### 2.2 LLM Firewall 与代理层
- **NeMo Guardrails 代理层**：在 SIEM/XDR 场景拦截 LLM 输出，执行受控动作（封禁 IP、杀进程、隔离文件）[11]。
- **ControlNET**：面向 RAG 系统的防火墙，实施检索-生成管线访问控制 [33]。
- **VEPA**：经验证的演化形式化策略，为终身 Agent 护栏提供可验证策略更新 [34][35][36]。

### 2.3 权限与沙箱、人在回路
- **最小权限工具选择**：When Lower Privileges Suffice 量化过度权限风险，主张权限感知工具选择 [22]。
- **按需行为沙箱**：Runtime Protection Practice 提出按需行为沙箱，动态隔离高风险工具调用 [37]。
- **人在回路审批绕过风险**：恶意技能可绕过审批流程，需运行时持久上下文监控 [6]。

### 2.4 新防御范式：架构契约、控制理论、技能化护栏
| 范式 | 核心机制 | 代表作 | 证据 |
|------|----------|--------|------|
| **SDB 架构契约** | proposer/verifier/commit/reject 四部件，形式化随机-确定性边界 | A Methodology for Selecting and Composing Runtime Architecture Patterns [5] | 热度：> 待核实；权威：arXiv 预印本；关注度：中；推荐度：★★★★☆ |
| **控制理论护栏** | 从静态拒绝转向序列决策与恢复闭环，预防下游物理/金融危害 | From Refusal to Recovery [38] | 热度：citations=0；权威：arXiv 预印本（CMU 作者）；关注度：中；推荐度：★★★★☆ |
| **Defense-as-Skill** | 护栏本身封装为可进化技能，持久上下文中动态拦截秘密泄露/代码污染/审批绕过/数据窃取 | Defense-as-Skill [6] | 热度：> 待核实；权威：arXiv cs.CR；关注度：高；推荐度：★★★★★ |
| **概率预测监控** | ProbGuard 通过概率预测实现主动运行时监控 | ProbGuard [39] | 热度：> 待核实；权威：arXiv 预印本；关注度：低；推荐度：★★★☆☆ |

### 2.5 推理时越狱防御
- **TEL-OS v3.0**：球面线性插值（SLERP）引导有害激活向拒答流形，推理时无需微调 [40]。
- **剪枝增强抗越狱**：WANDA 剪枝在不微调前提下提升抗越狱鲁棒性 [41]。
- **优化型越狱改进**：GCG 变体持续刷新攻击上限，防御需跟进 [42][43][44][45][46]。

---

## 三、安全评测与红队基准

### 3.1 Agent 级可执行环境基准
| 基准 | 年份 | 机构/发布 | 核心特征 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|----------|------|------|--------|--------|------|------|
| AgentDojo | 2024 | ETH Zurich (NeurIPS D&B) | 可执行环境评测提示注入攻防，支持动态工具链 | citations=高 | 顶会 | 高 | ★★★★★ | [7][8] | 奠基性 Agent 级评测环境 |
| InjecAgent | 2024 | UIUC (ACL Findings) | 工具集成 Agent 的间接注入基准，多工具场景 | citations=高 | 顶会 | 高 | ★★★★★ | [7][8] | 间接注入基准标杆 |
| AgentHarm | 2024 | CAIS (ICLR) | 352 任务多步工具链危害性评测，覆盖 11 危害类别 | citations=高 | 顶会 | 高 | ★★★★★ | [9] | Agent 危害性标准基准 |
| MalSkillBench | 2026 | Cornell (arXiv) | 3,944 运行时验证恶意技能，108 分类单元三维分类 | citations=28 | arXiv 预印本 | 中 | ★★★★☆ | [10] | 首个运行时验证恶意技能基准 |

### 3.2 越狱与拒答评测
| 基准 | 年份 | 机构/发布 | 核心特征 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|----------|------|------|--------|--------|------|------|
| JailbreakBench | 2024 | 开源社区 | 越狱攻防标准评测，开放排行榜 | citations=高 | GitHub/社区 | 高 | ★★★★★ | [47] | 越狱评测事实标准 |
| HarmBench | 2024 | CAIS | 自动化红队与拒答评测，标准化指标 | citations=高 | 顶会/社区 | 高 | ★★★★★ | 种子资源 | 红队自动化基准 |
| OR-Bench | 2026 | 社区 | 80k+ 过度拒答基准，量化误拦截 | > 待核实 | 社区基准 | 中 | ★★★★☆ | [48] | 过度拒答专用评测 |

### 3.3 间接注入专用基准
- **Beyond Instruction Override**：任务篡改攻击基准，揭示指令覆盖类基准盲区 [2][4][17][18]。
- **MAMORI**：跨语言间接注入基准，覆盖多语言工具调用场景 [49][50]。
- **Execution-Aware Stage-Wise**：邮件 Agent 场景的执行感知分阶段评测 [4]。
- **DeRAG**：RAG 系统黑盒对抗攻击基准，差分进化优化后缀 [29]。

### 3.4 协议与多智能体基准
- **MCP-Universe**：真实 MCP 服务器基准，超越简化模拟 [24]。
- **MCP Security Bench (MSB)**：针对 MCP 的攻击基准 [25]。
- **MOASEI Competition**：开放多智能体决策评测竞赛（野火救援/网络安全/网约车）[51]。
- **ATX-1 威胁矩阵**：Agentic AI 专用对抗知识库，区别于 MITRE ATLAS/ATT&CK [15][16]。

### 3.5 垂直领域基准
- **FinProof v1**：银行/金融/保险对抗性护栏基准，填补高风险垂直评测空白 [52]。
- **TanglishGuard**：泰米尔-英语代码混合提示护栏基准，揭示多语言泛化缺口 [19]。

---

## 四、框架与工程实践

### 4.1 主流开源护栏框架对比
| 框架 | 机构/维护 | 核心机制 | GitHub Stars | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|-----------|----------|--------------|------|--------|--------|------|------|
| **NeMo Guardrails** | NVIDIA | 可编程对话护栏，Colang DSL 定义流程/权限/话题控制 | > 待核实 | 官方技术报告 [12] | 高 | ★★★★★ | [12][53] | 生产级可编程护栏，已用于 SIEM/XDR 代理层 [11] |
| **Guardrails AI** | Guardrails AI Inc. | 输入输出校验器、结构化输出、PII/注入检测 | > 待核实 | 官方文档/社区 | 高 | ★★★★★ | 种子资源 | 验证器生态丰富，支持流式验证 |
| **PurpleLlama / Llama Guard** | Meta | Llama Guard（分类器）、Prompt Guard（注入检测）、CodeShield、LlamaFirewall | > 待核实 | 官方发布/顶会 | 高 | ★★★★★ | 种子资源 | 模型级护栏，可微调部署 |
| **LLM Guard** | Protect AI | 输入输出扫描器（注入、PII、敏感内容、恶意 URL） | > 待核实 | 官方文档 | 中 | ★★★★☆ | 种子资源 | 轻量级扫描器，易集成 |
| **Presidio** | Microsoft | PII 检测与脱敏，出站数据防泄露 | > 待核实 | 官方维护 | 中 | ★★★★☆ | 种子资源 | 隐私合规专用，非通用护栏 |

### 4.2 生产落地实证
- **NeMo Guardrails 在 SIEM/XDR 代理式补救**：IEEE CSR 会议论文展示代理层拦截 LLM 命令并执行受控动作，解决告警过载 [11]。
- **控制理论护栏架构**：From Refusal to Recovery 提出序列决策与恢复闭环，而非单纯拒绝 [38]。
- **图数据库护栏**：建模实体依赖验证动作约束，优于纯规则/LLM 校验 [54]。
- **AI Ethics by Design**：可定制护栏工程化实践 [55]。

### 4.3 工程痛点与缺口
> 待核实：主流框架横向性能对比（延迟 P50/P99、吞吐、误拦截率、绕过鲁棒性）缺乏第三方基准。
> 待核实：护栏与推理引擎集成最佳实践缺失。
> 待核实：多模态/代码混合场景泛化评测标准未形成共识。

---

## 五、企业落地与合规基线

### 5.1 OWASP LLM Top 10 与 Agentic AI 扩展
- **OWASP LLM Top 10 (2025)**：LLM01 提示注入、LLM06 过度代理、LLM07 系统提示泄露等 [种子资源]。
- **事件数据鲁棒性分析**：专家排序与大规模事件语料显著偏离，提示基线需数据驱动校准 [14]。
- **智能体缓解 OWASP Top 10**：用智能体自身缓解风险的反讽范式 [56]。

### 5.2 NIST AI RMF 与监管对齐
- **NIST AI RMF 映射**：SCITUS 将 NIST AI RMF 适配加拿大监管语境 [57]。
- **AAGATE**：NIST AI RMF 对齐的 Agentic AI 治理平台 [58]。
- **高后果 AI 风险管理标准**：Actionable Guidance 推动灾难性风险标准化 [59]。

### 5.3 MITRE ATLAS 与 ATX-1 威胁矩阵
- **MITRE ATLAS**：针对 AI 系统的 ATT&CK 式对抗战术知识库 [种子资源]。
- **ATX-1 v2.3/v2.4**：AEGIS 威胁矩阵，专门针对无治理约束的自主 AI Agent 失效模式，区别于 ATLAS/ATT&CK [15][16]。
- **零信任 Agent 架构**：Caging the Agents 在医疗场景落地零信任 [60]。

### 5.4 威胁建模与供应链
- **MCP 威胁建模**：Security Threat Modeling 对比 MCP/A2A/Agora/ANP [61]。
- **MCP 安全全景**：Security of the Model Context Protocol Ecosystem 系统梳理新兴威胁、实证攻击、信任授权失效、供应链风险 [62]。
- **工具投毒系统性综述**：Tool Poisoning and Trust Boundaries 覆盖 2025-2026 漏洞与防御参考架构 [27]。
- **企业级 MCP 安全框架**：Enterprise-Grade Security for MCP [63]。

### 5.5 合规基线落地缺口
> 待核实：具身智能/机器人实时控制回路的合规映射指南缺失。
> 待核实：护栏审计日志与证据链在监管审计中的可采纳性标准尚未统一。

---

## 六、真实事件与失败模式

### 6.1 基础模型透明度倒退加剧下游风险
- **2025 基础模型透明度指数**：平均分 58→40，训练数据/算力/部署后影响最不透明，间接增加 Agent 护栏外部依赖风险评估难度 [64]。

### 6.2 过度拒答与效用损失
- **When Your AI Says No to Everything**：OR-Bench (80k+) 量化过度拒答，如 "how to kill a mosquito" 被误拦 [48]。
- **Jev 护栏实证研究**：输入过滤/选择性输出审查/过度拒答三方式权衡 [65]。

### 6.3 分解攻击绕过逐步检查
- **Checked at Every Step Is Not Checked as a Whole**：计划级安全盲区实证，分解攻击利用步级与计划级鸿沟 [30]。

### 6.4 表层防御失效与框架差距
- **The Framing Gap**：间接注入外泄击败表层防御，工具使用 Agent 尤其脆弱 [17][66]。
- **Ignored, Not Refused**：低注入成功率掩盖小型工具 Agent 中的忽略而非拒绝模式 [67]。

### 6.5 MCP 生态实战漏洞
- **MCP Safety Audit**：MCP 允许重大安全利用 [68]。
- **Mcploit**：MCP 枚举与利用框架 [69]。
- **Tracing MCP Security Vulnerabilities**：构建 MCP 漏洞数据集 [23]。

### 6.6 推理风格投毒与运行时监控
- **Reasoning-Style Poisoning**：隐蔽风格迁移的过程级攻击，RSV 空间运行时监控 [70]。
- **CAITLYN**：Agent 自主合成针对新兴注入的防御 [71]。

---

## 七、争议与开放问题

### 7.1 核心技术争议
| 争议点 | 正方观点 | 反方观点 | 证据 |
|--------|----------|----------|------|
| **护栏是否应内嵌模型还是外挂代理** | 内嵌分类器（Llama Guard/Prompt Guard）延迟低、上下文感知强 | 外挂代理（NeMo Guardrails/Guardrails AI）解耦合、可热更新、多模型复用 | [12][11][13] |
| **静态规则 vs LLM 判断 vs 概率监控** | 规则确定性强、可审计 | LLM 判断泛化强、适应语义变体 | 概率监控主动预测而非被动拦截 | [38][39][54] |
| **拒绝 vs 恢复** | 拒绝简单安全 | 控制理论主张恢复闭环，预防下游危害 | [38] |
| **基准是否反映真实风险** | AgentDojo/InjecAgent/AgentHarm 已覆盖核心场景 | 任务篡改/跨模态/代码混合/具身物理回路仍有巨大盲区 | [2][4][19][30] |

### 7.2 四大开放问题
1. **计划级安全盲区**：逐步检查无法保证整体安全，分解攻击通用化 [30]。
2. **多模态/代码混合泛化**：主流护栏在非英语、代码混合、图像/语音载荷上近乎失效 [19][20]。
3. **护栏与推理引擎低延迟集成**：vLLM/TensorRT-LLM/SGLang 管线中护栏热更新、版本灰度、P99 延迟 < 10ms 无成熟方案 [13]。
4. **具身智能真机端到端验证**：VLA/运动规划实时回路中护栏误触发/漏触发的定量指标、物理危害映射、安全完整性等级（SIL）认证路径缺失 [q3.open_problems]。

### 7.3 评测方法学分歧
- **静态基准 vs 动态红队**：HarmBench/JailbreakBench 静态基准 vs MOASEI/红队竞赛动态对抗 [51][47][72]。
- **模型级 vs Agent 级红队**：Mind the Gap 揭示模型级红队无法覆盖 Agent 级行动图可观测性 [73]。

### 7.4 供应链与治理博弈
- **基座模型不透明 vs 下游护栏责任**：透明度指数下降 [64] 导致护栏厂商承担不可知风险。
- **开源 vs 商业护栏责任边界**：The Plumbing of AI Safety 探讨开源与商业格局张力 [13]。

---

## 八、个人可落地项目与 Watchlist

### 8.1 可落地项目建议（按工程成熟度排序）
| 项目 | 目标 | 关键技术栈 | 预估周期 | 参考证据 |
|------|------|------------|----------|----------|
| **最小化护栏代理** | 基于 NeMo Guardrails/Guardrails AI 搭建代理层，拦截工具调用、执行最小权限策略 | NeMo Guardrails (Colang) / Guardrails AI Validators / FastAPI | 2-4 周 | [12][11][13] |
| **运行时沙箱原型** | 按需行为沙箱：高风险工具调用动态隔离、污点流追踪 | gVisor/Firecracker + Tool-Flow Taint Analysis | 4-6 周 | [37][28] |
| **计划级安全验证器** | 实现 proposer/verifier/commit/reject SDB 契约，检测分解攻击 | LangGraph/Autogen + 形式化验证 | 6-8 周 | [5][30] |
| **Defense-as-Skill 最小闭环** | 将护栏封装为可进化技能，持久上下文监控秘密泄露/代码污染 | Skill Library + Vector DB + 运行时监控 | 8-12 周 | [6] |
| **具身场景护栏基准** | 基于 AgentDojo 扩展 VLA/运动规划任务，量化误触发/漏触发与物理危害映射 | AgentDojo + Isaac Sim/ROS2 + 安全指标 | 12+ 周 | [7][q3.open_problems] |

### 8.2 Watchlist（持续跟踪清单）
| 条目 | 类型 | 关注理由 | 来源 |
|------|------|----------|------|
| **Defense-as-Skill 后续开源实现** | 代码/论文 | 新范式能否落地为可复用库 | [6] |
| **VEPA 形式化策略演化** | 论文/工具 | 终身 Agent 护栏可验证更新 | [34][35][36] |
| **MalSkillBench 社区采纳度** | 基准 | 恶意技能检测标准地面真值 | [10] |
| **MCP 安全审计工具链** | 工具 | Mcploit/MSB/漏洞数据集成熟度 | [23][25][69] |
| **NIST AI RMF / ATX-1 更新版** | 标准 | 合规基线与威胁矩阵同步演进 | [15][16][58] |
| **OR-Bench / 过度拒答缓解** | 基准/方法 | 效用-安全帕累托前沿 | [48][65] |
| **多模态/代码混合注入基准** | 基准 | TanglishGuard 后续扩展 | [19] |
| **ProbGuard / TEL-OS v3.0 开源** | 代码 | 推理时/概率监控可复用性 | [39][40] |
| **AgentDojo 具身扩展分支** | 代码/环境 | 真机/仿真一体化评测 | [7] |
| **OWASP LLM Top 10 2026 版** | 标准 | 事件数据驱动的基线修订 | [14] |

---

## 参考来源编号列表
[1] Prompt Injection Attacks in Large Language Models and AI Agent Systems: A Comprehensive Review of Vulnerabilities, Attack Vectors, and Defense Mechanisms — https://doi.org/10.3390/info17010054
[2] Beyond Instruction Override: Benchmarking Indirect Prompt Injection with Task-Tampering Attacks — http://arxiv.org/abs/2611.07640v1
[3] Adaptive Attacks Break Defenses Against Indirect Prompt Injection Attacks on LLM Agents — http://arxiv.org/abs/2503.00061v2
[4] Execution-Aware Stage-Wise Evaluation Framework for Indirect Prompt Injection in LLM-Based Email Agents — https://doi.org/10.1109/ACCESS.2026.3723800
[5] A Methodology for Selecting and Composing Runtime Architecture Patterns for Production LLM Agents — http://arxiv.org/abs/2605.20173v2
[6] Defense-as-Skill: Evolving Runtime Guard Skill for Skill-Augmented Agents — http://arxiv.org/abs/2609.01487v4
[7] InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated Large Language Model Agents — http://arxiv.org/abs/2403.02691v3
[8] InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated Large Language Model Agents — https://doi.org/10.18653/v1/2024.findings-acl.624
[9] AgentHarm: A Benchmark for Measuring Harmfulness of LLM Agents — http://arxiv.org/abs/2410.09024v3
[10] MalSkillBench: A Runtime-Verified Benchmark of Malicious Agent Skills — https://doi.org/10.48550/arxiv.2606.07131
[11] Constrained-Action AI Remediation for SIEM/XDR via a NeMo-Guardrails Proxy — https://doi.org/10.1109/csr69374.2026.11759868
[12] NeMo Guardrails: A Toolkit for Controllable and Safe LLM Applications with Programmable Rails — http://arxiv.org/abs/2310.10501v1
[13] The Plumbing of AI Safety: Guardrails, Not Vibes — https://doi.org/10.5281/zenodo.19422909
[14] Incident-Data Robustness Analysis of the OWASP Top 10 for LLM Applications (2026): How a Community-Expert Ranking Holds Up Against a Large-Scale LLM Incident Corpus — http://arxiv.org/abs/2608.19266v1
[15] "ATX-1 v2.3: AEGIS Threat Matrix for Agentic AI Systems" — https://doi.org/10.21227/jr43-0571
[16] "ATX-1 v2.4: AEGIS Threat Matrix for Agentic AI Systems" — https://doi.org/10.21227/edxj-ka42
[17] The Framing Gap: Indirect Prompt-Injection Exfiltration Defeats Surface-Level Defenses in Tool-Using Agents — https://arxiv.org/abs/2608.27092
[18] Evaluating Indirect Prompt Injection Defenses in Tool-Using LLM Agents: Security, Utility, and Replication — https://doi.org/10.3390/computers15090570
[19] TanglishGuard: Benchmarking AI Safety Guardrails on Tamil-English Code-Mixed Prompts — https://doi.org/10.38124/ijisrt/26jul962
[20] Benign-to-Toxic Jailbreaking: Inducing Harmful Responses from Harmless Prompts — http://arxiv.org/abs/2505.21556v1
[21] Universal Jailbreak Suffixes Are Strong Attention Hijackers — https://doi.org/10.48448/9bvn-ex71
[22] When Lower Privileges Suffice: Investigating Over-Privileged Tool Selection in LLM Agents — http://arxiv.org/abs/2606.20023v2
[23] Tracing MCP Security Vulnerabilities: Constructing and Analyzing an MCP Security Vulnerability Dataset — http://arxiv.org/abs/2611.11104v1
[24] MCP-Universe: Benchmarking Large Language Models with Real-World Model Context Protocol Servers — http://arxiv.org/abs/2508.14704v1
[25] MCP Security Bench (MSB): Benchmarking Attacks Against Model Context Protocol in LLM Agents — http://arxiv.org/abs/2510.15994v2
[26] Capability-Mediated Perimeters for Secure AI Agent Tool Execution: Conditional Non-Escalation Invariants and Empirical Evaluation Against Indirect Prompt Injection — https://doi.org/10.2139/ssrn.7505299
[27] Tool Poisoning and Trust Boundaries in Model Context Protocol (MCP) Ecosystems: A Systematic Review of 2025-2026 Vulnerabilities and a Defensive Reference Architecture — https://doi.org/10.2139/ssrn.7668659
[28] Tool-Flow Taint Analysis for Data Exfiltration Defense in Large Language Model Agents — https://doi.org/10.66857/jirt.v3i2.52
[29] DeRAG: Black-box Adversarial Attacks on Multiple Retrieval-Augmented Generation Applications via Prompt Injection — http://arxiv.org/abs/2507.15042v1
[30] Checked at Every Step Is Not Checked as a Whole: Two Senses of Plan-Level Safety for LLM Agents, and Why Decomposition Attacks Exploit the Gap Between Them — https://doi.org/10.5281/zenodo.22961077
[31] Detecting Prompt Injection Attacks Against Application Using Classifiers — http://arxiv.org/abs/2512.12583v1
[32] StruQ: Defending Against Prompt Injection with Structured Queries — http://arxiv.org/abs/2402.06363v2
[33] ControlNET: A Firewall for RAG-based LLM System — http://arxiv.org/abs/2504.09593v2
[34] [2610.12813] VEPA: Verified Evolving Formal Policy for Lifelong  LLM   Agent Guardrails — https://arxiv.org/abs/2610.12813
[35] [2610.12813] VEPA: Verified Evolving Formal Policy for Lifelong  LLM   Agent Guardrails — https://arxiv.org/abs/2610.12813?context=cs.LG
[36] [2610.12813] VEPA: Verified Evolving Formal Policy for Lifelong  LLM   Agent Guardrails — https://arxiv.org/abs/2610.12813?context=cs
[37] Runtime Protection Practice for LLM Agent Security: An On-Demand Behavioral Sandbox Approach — https://doi.org/10.1109/isaeece70502.2026.11635191
[38] From Refusal to Recovery: A Control-Theoretic Approach to Generative AI Guardrails — http://arxiv.org/abs/2510.13727v2
[39] ProbGuard: Proactive Runtime Monitoring for LLM Agent Safety via Probabilistic Prediction — http://arxiv.org/abs/2508.00500v4
[40] TEL-OS v3.0: Inference-Time Jailbreak Defense via Spherical Representation Steering — https://doi.org/10.5281/zenodo.19355057
[41] Pruning for Protection: Increasing Jailbreak Resistance in Aligned LLMs Without Fine-Tuning — https://doi.org/10.18653/v1/2024.blackboxnlp-1.26
[42] Faster-GCG: Efficient Discrete Optimization Jailbreak Attacks against Aligned Large Language Models — http://arxiv.org/abs/2410.15362v2
[43] Improved Techniques for Optimization-Based Jailbreaking on Large Language Models — https://doi.org/10.48550/arxiv.2405.21018
[44] AutoDAN: Generating Stealthy Jailbreak Prompts on Aligned Large Language Models — http://arxiv.org/abs/2310.04451v2
[45] AutoDAN-Turbo: A Lifelong Agent for Strategy Self-Exploration to Jailbreak LLMs — http://arxiv.org/abs/2410.05295v4
[46] Sockpuppetting: Jailbreaking LLMs by Combining Prefilling with Optimization — https://doi.org/10.48550/arxiv.2601.13359
[47] JailbreakBench: An Open Robustness Benchmark for Jailbreaking Large Language Models — http://arxiv.org/abs/2404.01318v5
[48] When Your AI Says No to Everything — https://doi.org/10.5281/zenodo.19766558
[49] MAMORI: A Cross-Lingual Benchmark for Indirect Prompt Injection in Tool-Using LLM Agents — https://doi.org/10.1109/idap71869.2026.11727885
[50] MAMORI: A Cross-Lingual Benchmark for Indirect Prompt Injection in Tool-Using LLM Agents — https://doi.org/10.1109/IDAP71869.2026.11727885
[51] Second MOASEI Competition at AAMAS'2026: A Technical Report — http://arxiv.org/abs/2607.03399v1
[52] FinProof v1: An Adversarial Benchmark for AI Guardrail Evaluation in Banking, Financial Services, and Insurance — https://doi.org/10.2139/ssrn.7464798
[53] lukaskellerstein/nemo-guardrails-tutorial — https://github.com/lukaskellerstein/nemo-guardrails-tutorial
[54] Graph Database-Based Guardrails for Agentic AI Systems: A Comparative Evaluation Against Rule-Based and LLM Based Policy Validation — https://doi.org/10.5281/zenodo.23120325
[55] AI Ethics by Design: Implementing Customizable Guardrails for Responsible AI Development — http://arxiv.org/abs/2411.14442v2
[56] Mitigating the OWASP Top 10 For Large Language Models Applications using Intelligent Agents — http://arxiv.org/abs/2601.18105v1
[57] SCITUS: A Multi-Jurisdictional Framework for Adapting NIST AI RMF to the Canadian Regulatory Context — http://arxiv.org/abs/2607.15051v1
[58] AAGATE: A NIST AI RMF-Aligned Governance Platform for Agentic AI — http://arxiv.org/abs/2510.25863v2
[59] Actionable Guidance for High-Consequence AI Risk Management: Towards Standards Addressing AI Catastrophic Risks — http://arxiv.org/abs/2206.08966v3
[60] Caging the Agents: A Zero Trust Security Architecture for Autonomous AI in Healthcare — http://arxiv.org/abs/2603.17419v1
[61] Security Threat Modeling for Emerging AI-Agent Protocols: A Comparative Analysis of MCP, A2A, Agora, and ANP — http://arxiv.org/abs/2602.11327v2
[62] Security of The Model Context Protocol Ecosystem: Emerging Threats, Empirical Attack Evidence, Trust and Authorization Failures, Supply-Chain Risks, And Defensive Strategies — https://doi.org/10.64388/irev10i3-1723420
[63] Enterprise-Grade Security for the Model Context Protocol (MCP): Frameworks and Mitigation Strategies — http://arxiv.org/abs/2504.08623v2
[64] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1
[65] Jev as an LLM Safety Guardrail: An Empirical Study of Input Filtering, Selective Output Review, and Over-Refusal — http://arxiv.org/abs/2611.08845v1
[66] The Framing Gap: Indirect Prompt-Injection Exfiltration Defeats Surface-Level Defenses in Tool-Using Agents — http://arxiv.org/abs/2608.27092v1
[67] Ignored, Not Refused: What Low Prompt-Injection Success Rates Hide in Small Tool-Using Agents — https://arxiv.org/abs/2610.23254
[68] MCP Safety Audit: LLMs with the Model Context Protocol Allow Major Security Exploits — http://arxiv.org/abs/2504.03767v2
[69] Mcploit: a Model Context Protocol Enumeration and Exploitation Framework — https://doi.org/10.1109/icdscnc70670.2026.11746266
[70] Reasoning-Style Poisoning of LLM Agents via Stealthy Style Transfer: Process-Level Attacks and Runtime Monitoring in RSV Space — https://doi.org/10.48550/arxiv.2512.14448
[71] CAITLYN: Can LLM Agents Autonomously Synthesize Defenses against Emerging Injection Attacks? — https://doi.org/10.48550/arxiv.2608.27990
[72] Red Teaming for Large Language Models At Scale: Tackling Hallucinations on Mathematics Tasks — http://arxiv.org/abs/2401.00290v1
[73] Mind the Gap: Comparing Model- vs Agentic-Level Red Teaming with Action-Graph Observability on GPT-OSS-20B — http://arxiv.org/abs/2509.17259v1
