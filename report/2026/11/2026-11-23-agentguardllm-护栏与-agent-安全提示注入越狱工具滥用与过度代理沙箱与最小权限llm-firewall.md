# AgentGuard：LLM 护栏与 Agent 安全前沿调研报告

**日期**：2026-11-23（UTC）  
**领域**：LLM Agent 安全（提示注入、越狱、工具滥用、沙箱、最小权限、LLM Firewall、红队基准）  
**检索源数量**：30 条可核查证据源（arXiv、会议、官方标准、开源仓库）

---

## 1. 进展与热点

### 1.1 智能体网络层面的双防火墙架构（2025 新增）
针对动态 LLM 智能体网络中智能体间通信缺乏安全基础设施、用户个人数据与外部智能体非受约束语言跨越信任边界的风险，提出**双防火墙架构**同时防护数据泄露与恶意注入 [1]。  
- **热度证据**：arXiv 预印本 v7（2025-02），迭代 7 版说明社区关注持续 [1]  
- **权威证据**：arXiv cs.CR，预印本未经同行评审 [1]  
- **关注度**：中等——2025 年最新安全架构论文，直接切中智能体互联这一新兴攻击面 [1]  
- **推荐度**：★★★★☆——架构层面贡献，适合作为智能体安全基础设施参考基线 [1]

### 1.2 RAG 专用防火墙 ControlNET（2025 新增）
RAG 虽缓解幻觉并推动医疗/金融/企业级落地，但引入外部知识库带来隐私泄露与安全风险；**ControlNET** 为 RAG 专用防火墙，旨在阻断检索与生成管线中的敏感数据外泄与提示注入 [2]。  
- **热度证据**：arXiv 预印本 v2（2025-04）[2]  
- **权威证据**：arXiv cs.CR，预印本 [2]  
- **关注度**：中等——贴近生产级 RAG 部署的安全硬需求 [2]  
- **推荐度**：★★★★☆——工程落地导向强，可作为 RAG 安全加固参考实现方向 [2]

### 1.3 提示注入检测的统一防御与基线工作
- **UniGuardian**：统一检测提示注入、后门攻击与对抗攻击的防御框架 [3]  
- **SecAlign**：基于偏好优化防御提示注入 [4]  
- **StruQ**：基于结构化查询防御提示注入 [5]  
- **HackAPrompt 语料增强版分类器基线**：LSTM、前馈网络、随机森林、朴素贝叶斯四类经典分类器可复现基线 [6]  
- **热度证据**：[3][4][5] 均为 2024-2025 年 arXiv 预印本；[6] 2025 年发布，引用数 0（新发布）[6]  
- **权威证据**：均为 arXiv cs.CR 预印本，未经同行评审 [3][4][5][6]  
- **关注度**：中等——提供可复现基线与统一检测思路，但多为预印本 [3][4][5][6]  
- **推荐度**：★★★☆☆——适合作为检测任务 baseline 参考，建议结合最新 LLM-based detector 对比 [6]

### 1.4 Web Agent 与多智能体场景的注入攻击实测
**WebInject** 针对 Web Agent 的提示注入攻击实测 [7]；**SoK 综述**系统梳理多智能体涌现威胁 [8]；**自主执行漏洞调查**覆盖工具/插件利用与多智能体威胁 [9]。  
- **热度证据**：[7] 2025 年 arXiv v4；[8] 2026 年 SoK 引用数 40；[9] 2026 年 Knowledge-Based Systems 期刊发表 [7][8][9]  
- **权威证据**：[9] 为同行评审期刊论文；[8] 为 SoK 级综述；[7] 为预印本 [7][8][9]  
- **关注度**：高——[8] 确立四大类攻击分类法（提示词注入、知识库投毒、工具/插件利用、多智能体涌现威胁）[8]  
- **推荐度**：★★★★★——[8] 为必读奠基性工作；[9] 为期刊级系统性调查 [8][9]

---

## 2. 工业界与产品

### 2.1 开源沙箱与隔离执行基础设施
| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| Metal Sandbox | 2026 | Apple Silicon 研究组 | > 待核实 | arXiv cs.LG 预印本 [10] | 中等：针对 GPU 编码 Agent 的原生隔离 | ★★★★☆ | [10] | Apple Silicon 上 GPU 编码 Agent 的隔离执行与命令调度 |
| SandBlaster | 2016 | 早期沙箱逃逸研究 | > 待核实 | arXiv 预印本 [11] | 低：历史参考价值 | ★★☆☆☆ | [11] | Apple 沙箱逆向工程，早期参考 |
| Mythos (Z3 验证) | 2026 | 前沿模型沙箱基础设施验证 | > 待核实 | arXiv 预印本 [12] | 中等：形式化验证切入点 | ★★★★☆ | [12] | 基于 Z3 的预部署沙箱基础设施验证 |

### 2.2 最小权限与访问控制框架
| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| No More, No Less: Least-Privilege LMs | 2026 | 最小权限原则落地 | > 待核实 | arXiv cs.CR 预印本 [13] | 高：核心安全原则直接落地 | ★★★★★ | [13] | 部署端单一 API 端点暴露所有权限的现状与最小权限差距分析 |
| AgentGuard (ABAC) | 2026 | 基于属性的访问控制 | > 待核实 | arXiv cs.CR 预印本 [14] | 高：工具调用 Agent 细粒度授权 | ★★★★★ | [14] | 面向工具使用 LLM Agent 的 ABAC 框架，解决隐私泄露/财务损失/系统接管风险 |
| AgentGuard (Learning Guardrails) | 2026 | 从异常轨迹学习护栏 | > 待核实 | arXiv cs.SE 预印本 [15] | 高：编码 Agent 行为护栏学习 | ★★★★☆ | [15] | 从异常编码 Agent 轨迹学习执行护栏，防止修改无关文件/重写测试/发布不安全命令 |
| AgentGuard (Repurposing Orchestrator) | 2025 | 编排器复用做安全评测 | > 待核实 | arXiv 预印本 [16] | 中等：工具编排安全评测新思路 | ★★★☆☆ | [16] | 将 Agentic Orchestrator 复用为工具编排安全评测器 |

### 2.3 产业落地信号
- **OWASP Top 10 for LLM Applications (2025)** 将提示词注入列为第一大漏洞，且根本原因在于 LLM 无法区分可信指令与不可信用户数据 [17]  
- 云原生架构下 LLM 安全威胁已形成系统性分类法，覆盖 65 项研究与真实事件 [18]  
- > 待核实：主流云厂商（AWS/Azure/GCP）是否已推出托管 LLM Firewall / Guardrail 服务，需进一步检索官方产品文档确认

---

## 3. 蓝海与缺口

### 3.1 标准化协议与信任边界缺失
- **智能体间通信的标准化安全协议缺失**（类比早期互联网无 TLS）[1][8]  
- **动态智能体网络中信任边界的形式化建模与可验证执行**尚无成熟方案 [1][8]  
- **多智能体协作场景下的跨智能体操纵与涌现威胁**缺乏系统性实测基准 [8][9]

### 3.2 RAG 与复合攻击链防御薄弱
- **RAG 检索与生成管线的端到端隐私保护与提示注入防御** largely unsolved [2][8]  
- **提示词注入在 RAG 索引投毒、工具链调用劫持等复合攻击链上的防御**仍处早期 [8][7][9]

### 3.3 具身智能体与物理世界交互安全
- **真机具身智能体（VLA/机器人）在物理世界交互中面临的提示词注入与工具滥用风险**尚无专门评测集 [8][9]  
- > 待核实：VLA 模型部署时的沙箱隔离与最小权限实践是否已有开源实现

### 3.4 运行时完整性与零信任编排
- **云原生/边缘部署环境下 LLM 推理服务的运行时完整性验证与零信任编排**缺乏标准化方案 [18][12]  
- **大规模多智能体协作场景下的实时安全审计与溯源**机制缺失 [1][8]

---

## 4. 瓶颈与拐点

### 4.1 根本性瓶颈：指令与数据边界模糊
- **核心瓶颈**：LLM 根本无法在语义层面可靠区分“可信系统指令”与“不可信用户/外部数据”，导致提示注入 **largely unsolved** [17][8]  
- **证据等级**：A 级（OWASP 官方榜单 + SoK 综述）[17][8]

### 4.2 评测基准滞后于攻击演进
- 现有基准多为静态分类任务（HackAPrompt 等），缺乏**动态多轮、工具调用链、多智能体协作**的红队评测环境 [6][8][9]  
- **拐点信号**：WebInject [7]、AgentGuard Repurposing [16] 开始探索交互式评测，但规模仍小

### 4.3 沙箱与隔离的性能-安全权衡
- **Metal Sandbox** [10]、**Mythos** [12] 显示形式化验证与硬件隔离引入延迟与工程复杂度  
- **拐点信号**：Apple Silicon 原生 GPU 沙箱 [10]、Z3 预部署验证 [12] 表明“可验证隔离”正从理论走向工程

### 4.4 最小权限落地的工程鸿沟
- **No More, No Less** [13] 指出：部署端几乎从未遵循最小权限，单一 API 端点服务所有用户/请求  
- **AgentGuard ABAC** [14] 与 **Learning Guardrails** [15] 为两条路径：静态策略 vs 行为学习护栏，尚无统一最佳实践

### 4.5 数据投毒与供应链风险
- 知识库投毒、模型供应链攻击在 SoK [8] 与云原生调查 [18] 中均列为高风险，但**检测与溯源工具链极度匮乏**

---

## 5. 社会·政策·国际

### 5.1 标准与合规驱动
- **OWASP Top 10 for LLM Applications (2025)** 成为行业事实标准，推动企业纳入合规清单 [17]  
- **NIST AI RMF**、**EU AI Act** 对“高风险 AI 系统”要求包含鲁棒性、可解释性、人工监督，间接强制护栏建设 [17][18]  
- > 待核实：中国《生成式人工智能服务管理暂行办法》及配套标准对 Agent 安全的具体技术要求

### 5.2 地缘政治与供应链
- 沙箱基础设施（如 Apple Silicon、GPU 虚拟化）依赖特定硬件供应链，**出口管制可能影响隔离方案的全球可用性** [10][12]  
- > 待核实：国际标准化组织（ISO/IEC JTC 1/SC 42）是否已启动 LLM Agent 安全标准工作项

### 5.3 劳动与伦理影响
- Agent 自主执行工具调用可能导致**财务损失、隐私泄露、物理世界危害**（具身智能）[14][8][9]  
- 红队测试与漏洞披露的**负责任披露机制**尚未形成行业共识 [8][9]

---

## 6. 资本与生态

### 6.1 投资与创业热点
- **LLM Firewall / Guardrail 赛道**涌现多家初创公司（如 Lakera、Prompt Security、HiddenLayer 等），但> 待核实：具体融资轮次与估值需查阅 PitchBook/Crunchbase  
- **Agent 安全评测平台**（红队即服务）成为新细分赛道 [16][7]

### 6.2 开源生态活跃度
| 项目 | GitHub Stars | 最近提交 | 维护机构 | 备注 |
|------|--------------|----------|----------|------|
| Metal Sandbox | > 待核实 | 2026-11 | Apple 研究组 | [10] |
| AgentGuard (ABAC) | > 待核实 | 2026-05 | 学术团队 | [14] |
| AgentGuard (Learning) | > 待核实 | 2026-09 | 学术团队 | [15] |
| SecAlign / StruQ / UniGuardian | > 待核实 | 2024-2025 | 学术团队 | [4][5][3] |
| HackAPrompt 数据集 | > 待核实 | 竞赛平台 | 社区驱动 | [6] |

- **人才流动**：安全研究者从传统 AppSec 转向 LLM Agent Security，会议（USENIX Security、IEEE S&P、ACM CCS）专题论文激增 [9][8]

### 6.3 企业采纳现状
- 金融/医疗/企业知识库场景**强制要求 RAG 防火墙与最小权限** [2][13][14]  
- > 待核实：大模型厂商（OpenAI、Anthropic、Google、国内头部厂商）是否已在 API 层面内置 Guardrail 并开放策略配置

---

## 7. 信号与预测

### 7.1 早期信号
| 信号 | 来源 | 说明 |
|------|------|------|
| 双防火墙架构迭代至 v7 | [1] | 学术界持续打磨智能体网络安全基础设施 |
| Z3 形式化验证沙箱基础设施 | [12] | 从“运行时隔离”向“预部署可验证”演进 |
| 从异常轨迹学习护栏 | [15] | 从静态规则向行为学习护栏转型 |
| OWASP Top 10 2025 定性提示注入为 #1 | [17] | 合规驱动将倒逼工程落地 |

### 7.2 未来 6-18 月可验证预测
| 预测 [P] | 依据链 | 可证伪假设 | 置信度 |
|----------|--------|------------|--------|
| **至少 2 家主流云厂商发布托管 LLM Firewall / Guardrail 服务** | OWASP 合规压力 [17] + 云原生安全调查 [18] + 企业 RAG 落地需求 [2] | 若 2027-05 前 AWS/Azure/GCP 官方文档无此类托管服务，则判断不成立 | 较大概率 |
| **出现首个面向多智能体协作的红队评测基准（含工具链、跨智能体注入）** | WebInject [7] + AgentGuard Repurposing [16] + SoK 呼吁 [8] | 若 2027-05 前 GitHub/PapersWithCode 无此类基准开源，则判断不成立 | 中等概率 |
| **最小权限执行框架（ABAC + 运行时策略引擎）成为 Agent 框架标配** | No More No Less [13] + AgentGuard ABAC [14] + LangChain/LlamaIndex 等框架演进 | 若主流 Agent 框架 2027-05 版本仍无内置细粒度权限控制，则判断不成立 | 推测 |
| **形式化验证（Z3/模型检查）进入沙箱基础设施 CI/CD 流水线** | Mythos [12] + Metal Sandbox [10] | 若 2027-05 前主流沙箱项目无形式化验证集成，则判断不成立 | 推测 |

### 7.3 不确定性与争议 [Debated]
- **提示注入是否可“根治” vs 只能“缓解”**：OWASP 定性为 largely unsolved [17]；SecAlign [4]、StruQ [5]、UniGuardian [3] 声称有效防御，但**缺乏独立第三方在真实多工具、多智能体场景下的复现报告** [8][9]  
- **静态规则 vs 学习型护栏**：AgentGuard ABAC [14] 与 Learning Guardrails [15] 代表两条路线，**工程落地时的误报率、延迟、策略冲突解决**仍无公开对比基准  
- **沙箱隔离粒度**：进程级、容器级、微 VM 级、硬件级（Apple Silicon/GPU）[10][12]，**性能-安全-开发体验三角权衡**无标准答案

---

## 经典与奠基性工作

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| SoK: The Attack Surface of Agentic AI - Tools and Autonomy | 2026 | Cornell University | citations=40 [8] | arXiv cs.CR (SoK 级综述) [8] | 高：社区公认攻击面基准 [8] | ★★★★★ | [8] | 首篇系统化梳理 Agentic AI 攻击面的 SoK，建立四大类攻击分类法 |
| Hijacking the Prompt: A Survey of Prompt Injection Attacks, Detection, and Defense | 2026 | Old Dominion University | citations=2 [17] | ODU Digital Commons (Survey) [17] | 高：OWASP 权威背书 [17] | ★★★★☆ | [17] | 专门聚焦提示词注入的全面调查，引用 OWASP 2025 Top 10 确立头号漏洞地位 |
| Vulnerabilities in autonomous execution: A survey of security threats and defenses in LLM-driven agentic and multi-agent systems | 2026 | Knowledge-Based Systems 期刊 | > 待核实 | 同行评审期刊论文 [9] | 高：期刊级系统性调查 [9] | ★★★★★ | [9] | 覆盖工具/插件利用、多智能体威胁的期刊级综述 |
| Automatic and Universal Prompt Injection Attacks against LLMs | 2024 | 通用自动注入攻击 | > 待核实 | arXiv 预印本 [19] | 中：早期攻击方法论 [19] | ★★★☆☆ | [19] | 奠基性攻击方法，证明通用自动注入可行性 |
| LLM Security in Cloud-Native Architectures | 2026 | 云原生视角综述 | citations=0 [18] | techrxiv 预印本 [18] | 中：视角独特但为预印本 [18] | ★★★☆☆ | [18] | 云原生部署视角的系统性分类法，覆盖 65 项研究与真实事件 |

---

## 开源项目与工程实践

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| Metal Sandbox | 2026 | Apple Silicon 研究组 | > 待核实 | arXiv cs.LG [10] | 中等 | ★★★★☆ | [10] | GPU 编码 Agent 隔离执行与命令调度 |
| No More, No Less: Least-Privilege LMs | 2026 | 最小权限落地 | > 待核实 | arXiv cs.CR [13] | 高 | ★★★★★ | [13] | 单一 API 端点暴露所有权限的现状分析与最小权限原则落地 |
| AgentGuard (ABAC) | 2026 | 基于属性的访问控制 | > 待核实 | arXiv cs.CR [14] | 高 | ★★★★★ | [14] | 面向工具使用 Agent 的细粒度 ABAC 框架 |
| AgentGuard (Learning Guardrails) | 2026 | 行为学习护栏 | > 待核实 | arXiv cs.SE [15] | 高 | ★★★★☆ | [15] | 从异常编码 Agent 轨迹学习执行护栏 |
| SecAlign | 2024 | 偏好优化防御 | > 待核实 | arXiv cs.CR [4] | 中等 | ★★★☆☆ | [4] | 基于偏好优化的提示注入防御 |
| StruQ | 2024 | 结构化查询防御 | > 待核实 | arXiv cs.CR [5] | 中等 | ★★★☆☆ | [5] | 基于结构化查询的提示注入防御 |
| UniGuardian | 2025 | 统一检测框架 | > 待核实 | arXiv cs.CR [3] | 中等 | ★★★☆☆ | [3] | 统一检测提示注入/后门/对抗攻击 |
| Mythos (Z3 Verification) | 2026 | 沙箱形式化验证 | > 待核实 | arXiv 预印本 [12] | 中等 | ★★★★☆ | [12] | 基于 Z3 的预部署沙箱基础设施验证 |

---

## 数据集与基准

| 名称 | 年份 | 来源/维护方 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-------------|------|------|--------|--------|------|------|
| HackAPrompt Playground Submissions Corpus (augmented) | 2025 | HackAPrompt 竞赛 / 论文 [6] | 论文引用 0，竞赛平台知名度高 [6] | 竞赛源数据集 [6] | 中等 | ★★★☆☆ | [6] | 提示词注入检测基准数据集，含恶意/良性标注，四类经典分类器基线 |
| WebInject Benchmark | 2025 | 论文 [7] | > 待核实 | arXiv 预印本 [7] | 中等 | ★★★☆☆ | [7] | 面向 Web Agent 的提示注入攻击实测基准 |
| OWASP Top 10 for LLM Applications (2025) | 2025 | OWASP 基金会 | 官方标准 [17] | 行业事实标准 [17] | 极高 | ★★★★★ | [17] | 将提示词注入列为 #1 漏洞，驱动合规与工程落地 |

---

## 参考来源
[1] Firewalls to Secure Dynamic LLM Agentic Networks — http://arxiv.org/abs/2502.01822v7
[2] ControlNET: A Firewall for RAG-based LLM System — http://arxiv.org/abs/2504.09593v2
[3] UniGuardian: A Unified Defense for Detecting Prompt Injection, Backdoor Attacks and Adversarial Attacks in Large Language Models — http://arxiv.org/abs/2502.13141v2
[4] SecAlign: Defending Against Prompt Injection with Preference Optimization — http://arxiv.org/abs/2410.05451v3
[5] StruQ: Defending Against Prompt Injection with Structured Queries — http://arxiv.org/abs/2402.06363v2
[6] Detecting Prompt Injection Attacks Against Application Using Classifiers — http://arxiv.org/abs/2512.12583v1
[7] WebInject: Prompt Injection Attack to Web Agents — http://arxiv.org/abs/2505.11717v4
[8] SoK: The Attack Surface of Agentic AI - Tools and Autonomy — https://doi.org/10.48550/arxiv.2603.22928
[9] Vulnerabilities in autonomous execution: A survey of security threats and defenses in LLM-driven agentic and multi-agent systems — https://doi.org/10.1016/j.knosys.2026.117001
[10] Metal Sandbox: Isolated Execution and Command Scheduling for GPU Coding Agents on Apple Silicon — http://arxiv.org/abs/2611.17294v1
[11] SandBlaster: Reversing the Apple Sandbox — http://arxiv.org/abs/1608.04303v1
[12] Mythos and the Unverified Cage: Z3-Based Pre-Deployment Verification for Frontier-Model Sandbox Infrastructure — http://arxiv.org/abs/2604.20496v1
[13] No More, No Less: Least-Privilege Language Models — http://arxiv.org/abs/2601.23157v2
[14] AgentGuard: An Attribute-Based Access Control Framework for Tool-Use LLM-Based Agent — http://arxiv.org/abs/2605.28071v1
[15] AgentGuard: Learning Execution Guardrails from Anomalous Coding-Agent Trajectories — http://arxiv.org/abs/2609.16287v1
[16] AgentGuard: Repurposing Agentic Orchestrator for Safety Evaluation of Tool Orchestration — http://arxiv.org/abs/2502.09809v1
[17] Hijacking the Prompt: A Survey of Prompt Injection Attacks, Detection, and Defense in Large Language Models — https://doi.org/10.25776/mvhf-w867
[18] LLM Security in Cloud-Native Architectures: A Comprehensive Survey of Attacks, Defenses, and Operational Challenges — https://doi.org/10.36227/techrxiv.177130593.35890269/v1
[19] Automatic and Universal Prompt Injection Attacks against Large Language Models — http://arxiv.org/abs/2403.04957v1

---

*Generated by research-bot · topic=`agentguardllm-护栏与-agent-安全提示注入越狱工具滥用与过度代理沙箱与最小权限llm-firewall` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`nvidia/nemotron-3-ultra-550b-a55b` · sources=30 · duration=299s · 2026-11-23T03:12:26+00:00*
