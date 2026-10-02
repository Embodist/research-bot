# 网络安全前沿调研报告（2024–2026）：大模型/Agent 安全、漏洞挖掘与程序分析、软件供应链与后量子密码迁移

> **元信息**
> - 完成日期（UTC）：2026-10-02
> - 领域：Cybersecurity（系统安全 / 软件与供应链安全 / AI 安全 / 密码学迁移）
> - 目标会议：USENIX Security、IEEE S&P、ACM CCS、NDSS
> - 可引用证据来源：35 条编号来源（[1]–[35]）+ 11 项人工维护种子资源（**未实时检索**）
> - 检索源数量说明：编号来源 35 条；结构化为 3 个子问题（q1 大模型/Agent 安全、q2 漏洞挖掘与程序分析、q3 供应链/PQC）
> - 证据分级：A = 同行评审论文 / 官方标准；B = arXiv 预印本 / 官方仓库；C = 第三方评测 / 出处不明的 DOI 期刊；D = 社区内容；E = 不可访问
> - **纪律声明**：本报告只使用 [1]–[35] 编号来源作为论断依据；凡编号来源未覆盖之处一律标 `> 待核实`，**不编造 citation、GitHub star、榜单排名或未在来源中出现的 URL**。

---

## 摘要（Executive Summary）

1. **证据强度整体偏低，需先降低预期。** 在 35 条可引用来源中，可确认为正式会议论文或官方标准的仅 4–5 条：DSN-S 2025 的 Polymorphic Prompt [11]、APSEC 2025 的 Web3 供应链安全 [17]、NIST SP 1800-44（供应链与 DevOps 安全实践）[23]、SANER-C 2026 的语法感知模糊测试 [35]；另有 Computer Science Bulletin 的航空 SBOM 论文 [22] 出处权威性 `> 待核实`。**其余绝大多数为 arXiv 预印本 [1]–[9]、[12]–[21]、[24]–[34]**，其"作者自我宣称"与"社区验证结论"必须严格区分。

2. **大模型/Agent 安全（LLM/Agent Security）是 2024–2026 最密集的攻击面。** 攻防已从"直接提示注入（direct prompt injection）"演进到"间接注入 + 环境操纵 + 后门耦合"：WebInject 通过操纵网页环境诱导多模态 Web Agent 执行攻击者动作 [2]；Backdoor-Powered Prompt Injection 声称后门驱动的注入可使现有防御失效 [9]；MELON 则声称对 AI Agent 的间接提示注入提供**可证明（provable）防御** [8]。**但本轮证据中没有任何独立第三方复现或榜单评测**，因此"防御是否真的被绕过""可证明防御是否成立"均 `> 待核实`。

3. **软件供应链安全的分析重心正从"单点漏洞告警"转向"攻击链与可验证属性"。** SoK 论文把供应链攻击归纳为四个阶段，并提出 transparency / validity / separation 三项安全属性作为评估骨架 [13]；最新的 SBOM 图学习工作直接批评现有 SBOM 管线把扫描结果当作互相独立的 per-CVE 记录，提出用异构图建模多漏洞级联攻击链 [20]。工程侧已出现 SBOM 驱动容器镜像筛查的规模化案例（128 微服务、三云环境）[22]。

4. **模糊测试与程序分析的"新进展"目前主要是 LLM 辅助输入生成、覆盖率开销优化与符号执行工程化，而非范式级突破。** 有综述系统盘点符号执行在漏洞、恶意软件、固件与协议分析中的应用 [34]；LLM 合成非文本输入生成器被用来降低复杂格式 fuzzing 的建模成本 [29]；语法感知 fuzzing 已工程化到 Grammarinator + AFL++ 的集成 [35]。经典奠基工作（覆盖率引导追踪 [31]、fork 感知 [25]）仍是该方向的评价基线。

5. **后量子密码（PQC）迁移是本次调研的最大空白。** 本轮 35 条编号来源中**没有任何一条**涉及 PQC 迁移标准、迁移评估或密码敏捷性；恶意软件分析方向的专用数据集/基准同样缺失（仅有一条 2018 年的 AiDroid [24] 与综述 [34] 间接涉及）。这两部分在下文被明确写成**缺口声明**而非结论 [13][17][20][22]。

6. **检索管道存在可识别的噪声与术语歧义，已在报告中剔除。** 子问题 q1/q2 的候选块中混入了与安全完全无关的短视频参与度预测挑战赛 [5]，以及"物理供应链"（material consolidation trade-offs）而非"软件供应链"的论文 [16]。**[5] 与本研究主题无关，不予采信；[16] 仅在术语辨析处引用。**

---

## 一、关键前沿进展（近 1–2 年）

下表按时间排序列出可归因于 2024–2026 年的关键节点。时间按 arXiv 编号 YYMM 或来源给定年份推断，**精确发表日期以官方页面为准**。

| 时间 | 节点 | 类型 | 证据强度 |
|---|---|---|---|
| 2024-02 | StruQ：用结构化查询（structured queries）防御提示注入 [3] | 防御 | B（arXiv 预印本） |
| 2024-03 | 自动且通用的提示注入攻击 [7] | 攻击 | B |
| 2024-06 | SoK：以安全设计属性分析软件供应链安全 [13] | SoK | B |
| 2024-06 | FOX：把覆盖率引导模糊测试建模为在线随机控制 [28] | fuzzing | B |
| 2024-07 | GoSurf：识别 Go 生态供应链攻击向量 [15] | 供应链 | B |
| 2024-07 | Maven-Hijack：利用打包顺序的供应链攻击 [18] | 供应链 | B |
| 2024-10 | SecAlign：用偏好优化防御提示注入 [1] | 防御 | B |
| 2025-01 | LLM 合成输入生成器驱动的低成本非文本 fuzzing [29] | fuzzing | B |
| 2025-02 | MELON：面向 AI Agent 间接提示注入的可证明防御 [8] | 防御 | B |
| 2025-02 | UniGuardian：统一检测提示注入/后门/对抗攻击 [4] | 防御 | B |
| 2025-04 | cozy：二进制的比较式符号执行 [33] | 程序分析 | B |
| 2025-05 | WebInject：面向 Web Agent 的提示注入攻击 [2] | 攻击 | B |
| 2025-08 | 符号执行实践综述（漏洞/恶意软件/固件/协议）[34] | 综述 | B |
| 2025-09 | 多智能体 LLM 防御流水线对抗提示注入 [6] | 防御 | B |
| 2025-10 | 后门驱动的提示注入攻击使防御失效 [9] | 攻击 | B |
| 2025 | Web3 软件供应链安全 [17] | 供应链 | **A（APSEC 2025）** |
| 2026 | 基于 SBOM 图预测多漏洞攻击链 [20] | 供应链 | B |
| 2026 | 航空系统多云 SBOM 风险筛查（128 微服务/3 云）[22] | 工程 | C（出处待核实） |
| 2026 | 简历筛选场景真实世界提示注入测量 [12] | 测量 | B |
| 2026 | 语法感知覆盖率引导 fuzzing（Grammarinator + AFL++）[35] | fuzzing | **A（SANER-C 2026）** |

**三条可归因的趋势判断：**

- **趋势一：攻击面从"文本通道"扩展到"环境通道"。** WebInject 的贡献点在于不再把注入限制在用户输入文本，而是操纵网页环境本身来影响多模态 Agent 的截图—动作循环 [2]。这使"输入过滤"类防御在原理上不充分——`> 待核实`：本报告未取得该论文的完整实验章节以确认其攻击成功率与模型覆盖范围。
- **趋势二：防御主张从"经验有效"走向"可证明"。** MELON 以 provable defense 为标题主张对间接注入的可证明鲁棒性 [8]，UniGuardian 则试图用统一框架同时覆盖提示注入、后门与对抗攻击三类威胁 [4]。同期仍有工作声称后门耦合注入可使防御整体失效 [9]。**这三条证据互相冲突，且全部为 preprint、无第三方复现，因此当前无法判定哪一方成立。**
- **趋势三：供应链安全从"清单合规"走向"图结构与攻击链建模"。** [13] 提供属性化分类骨架，[20] 提供具体方法（异构图学习预测多漏洞攻击链），[21] 提供基于机器学习的 SBOM 漏洞优先级排序，[22] 提供规模化工程落地数字。四者构成"分类 → 方法 → 排序 → 部署"的连续链条，但彼此**没有共同的评测基准**，跨论文比较 `> 待核实`。

**热度 / 权威 / 关注度 / 推荐度（趋势层）**
- 热度证据：全部 `> 待核实`——候选块未提供引用数、star 或下载量，仅 [35] 明确 `citations=0`、[22] 明确 `citations=0`。
- 权威证据：B 级为主，A 级仅 [13] 之外的 [17][35] 与官方标准 [23]（[13] 本身仍为预印本）。
- 关注度：**中**——依据是 2024–2026 年新预印本在上述三个方向持续产出（[2][4][8][9][20]），但缺少引用/榜单佐证。
- 推荐度：★★★★☆——方向相关性与时效性高，但引用时必须标注 preprint 状态。

---

## 二、Web / 系统 / 供应链攻防

### 2.1 经典与奠基性工作

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Branch Shadowing（SGX 侧信道） | 2017 | USENIX Security | `> 待核实`（种子资源，未实时检索引用数） | A（USENIX Security，种子清单标注）[种子] | 高（侧信道方向长期被引用的经典，但本轮未取得可核查数字） | ★★★★☆ 作为 A 级来源示例与侧信道方法论范本 | https://www.usenix.org/conference/usenixsecurity17 | 种子资源提供，非本轮检索所得 |
| CWE（Common Weakness Enumeration） | ongoing | MITRE | `> 待核实`（未实时检索） | 官方标准 [种子] | 高（弱点分类事实标准；

## 参考来源

[1] SecAlign: Defending Against Prompt Injection with Preference Optimization — http://arxiv.org/abs/2410.05451v3
[2] WebInject: Prompt Injection Attack to Web Agents — http://arxiv.org/abs/2505.11717v4
[3] StruQ: Defending Against Prompt Injection with Structured Queries — http://arxiv.org/abs/2402.06363v2
[4] UniGuardian: A Unified Defense for Detecting Prompt Injection, Backdoor Attacks and Adversarial Attacks in Large Language Models — http://arxiv.org/abs/2502.13141v2
[5] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1
[6] A Multi-Agent LLM Defense Pipeline Against Prompt Injection Attacks — http://arxiv.org/abs/2509.14285v4
[7] Automatic and Universal Prompt Injection Attacks against Large Language Models — http://arxiv.org/abs/2403.04957v1
[8] MELON: Provable Defense Against Indirect Prompt Injection Attacks in AI Agents — http://arxiv.org/abs/2502.05174v4
[9] Backdoor-Powered Prompt Injection Attacks Nullify Defense Methods — http://arxiv.org/abs/2510.03705v1
[10] GraphShield: A Graph-Structured Defense Framework for Prompt Injection in RAG and Multi-Agent LLM Systems — https://doi.org/10.2139/ssrn.7082874
[11] To Protect the LLM Agent Against the Prompt Injection Attack with Polymorphic Prompt — https://doi.org/10.1109/dsn-s65789.2025.00037
[12] Measuring Real-World Prompt Injection Attacks in LLM-based Resume Screening — http://arxiv.org/abs/2605.28999v1
[13] SoK: Analysis of Software Supply Chain Security by Establishing Secure Design Properties — http://arxiv.org/abs/2406.10109v1
[14] Trust in Software Supply Chains: Blockchain-Enabled SBOM and the AIBOM Future — http://arxiv.org/abs/2307.02088v4
[15] GoSurf: Identifying Software Supply Chain Attack Vectors in Go — http://arxiv.org/abs/2407.04442v2
[16] Exploitation of material consolidation trade-offs in multi-tier complex supply networks — http://arxiv.org/abs/2210.11479v3
[17] Software Supply Chain Security of Web3 — http://arxiv.org/abs/2511.12274v1
[18] Maven-Hijack: Software Supply Chain Attack Exploiting Packaging Order — http://arxiv.org/abs/2407.18760v4
[19] Software supply chain: review of attacks, risk assessment strategies and security controls — http://arxiv.org/abs/2305.14157v1
[20] Towards Predicting Multi-Vulnerability Attack Chains in Software Supply Chains from Software Bill of Materials Graphs — http://arxiv.org/abs/2604.04977v2
[21] SBOM-BASED VULNERABILITY PRIORITIZATION IN SOFTWARE SUPPLY CHAIN USING MACHINE LEARNING — https://doi.org/10.17721/ait.2025.2.04
[22] RISK-AWARE SOFTWARE SUPPLY CHAIN SECURITY FOR AVIATION SYSTEMS USING SBOM — https://doi.org/10.71465/csb213
[23] Software Supply Chain and DevOps Security Practices — https://doi.org/10.6028/nist.sp.1800-44
[24] AiDroid: When Heterogeneous Information Network Marries Deep Neural Network for Real-time Android Malware Detection — http://arxiv.org/abs/1811.01027v2
[25] Evaluating the Fork-Awareness of Coverage-Guided Fuzzers — http://arxiv.org/abs/2301.05060v1
[26] SyzScope: Revealing High-Risk Security Impacts of Fuzzer-Exposed Bugs in Linux kernel — http://arxiv.org/abs/2111.06002v1
[27] Same Coverage, Less Bloat: Accelerating Binary-only Fuzzing with Coverage-preserving Coverage-guided Tracing — http://arxiv.org/abs/2209.03441v1
[28] FOX: Coverage-guided Fuzzing as Online Stochastic Control — http://arxiv.org/abs/2406.04517v1
[29] Low-Cost and Comprehensive Non-textual Input Fuzzing with LLM-Synthesized Input Generators — http://arxiv.org/abs/2501.19282v1
[30] Internet Service Providers' and Individuals' Attitudes, Barriers, and Incentives to Secure IoT — http://arxiv.org/abs/2210.02137v1
[31] Full-speed Fuzzing: Reducing Fuzzing Overhead through Coverage-guided Tracing — http://arxiv.org/abs/1812.11875v2
[32] Multi-Factor Key Derivation Function (MFKDF) for Fast, Flexible, Secure, & Practical Key Management — http://arxiv.org/abs/2208.05586v3
[33] cozy: Comparative Symbolic Execution for Binary Programs — http://arxiv.org/abs/2504.00151v1
[34] Symbolic Execution in Practice: A Survey of Applications in Vulnerability, Malware, Firmware, and Protocol Analysis — http://arxiv.org/abs/2508.06643v1
[35] Grammar-Aware Coverage-Guided Fuzzing with Grammarinator and AFL++ — https://doi.org/10.1109/saner-c67878.2026.00055


---

*Generated by research-bot · topic=`cybersecurity` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading · model=`deepseek-v4-flash` · sources=35 · duration=173s · 2026-10-02T10:45:02+00:00*
