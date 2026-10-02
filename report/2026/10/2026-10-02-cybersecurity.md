# 网络安全攻防前沿调研报告：从软件供应链到 LLM/Agent 安全

> **日期**：2026-10-02（UTC）
> **领域**：Cybersecurity（漏洞与利用 · 模糊测试与程序分析 · 密码学工程 · 大模型/Agent 安全 · 软件供应链与 SBOM · 内存安全）
> **检索源**：57 条可核查引用来源（以 arXiv 预印本与少量期刊/会议 DOI 为主）+ 3 类人工维护种子资源（OWASP / MITRE / 开源工具链）
> **证据分级**：A 同行评审 | B 预印本 / 官方仓库 | C 第三方复现 / 榜单 | D 社区 / 聚合 | E 不可用
> **本报告证据强度总评**：**偏低**。除少数经典工作（如 [2][3]）具备明确的顶会历史与影响力外，本次候选集中绝大多数条目为 2025–2026 年 arXiv 预印本或机构知识库材料，`citations` 多为 0，**无第三方复现、无榜单排名、无官方发布确认**。

---

## 摘要（Executive Summary）

1. **LLM/Agent 安全已从"内容越狱"扩散到"交互面攻击"**。OWASP 2025 将 prompt injection 列为 LLM 应用第一风险（[34] 转述），新证据显示攻击面正沿 Web Agent 的多模态屏幕输入 [27]、工具调用与 RAG 检索链路 [36]、对话式系统的交互状态 [37] 继续扩张。**但这些 2026 年新条目引用数均为 0，尚无同行评审背书，结论应视为方向性线索而非定论。**

2. **软件供应链安全的主战场从"出 SBOM"转向"用 SBOM"**。SBOM 工具生态的系统性综述 [48] 与"基于 SBOM 图预测多漏洞攻击链"的工作 [46] 共同揭示：SBOM 的实用价值取决于其准确性与可分析性，而非覆盖率。Web3 [42] 与 NPM/PyPI/Docker Hub [45] 的实证分析把攻击面延伸到区块链与公共包仓库。

3. **模糊测试领域出现"传统 coverage-guided"与"LLM 辅助生成"两条并行路线**。FOX 把调度器与变异器统一为在线随机控制 [5]；与此同时，LLM 合成输入生成器开始覆盖 images/videos/PDF 等非文本输入 [8]。**但本子问题在候选集中完全未命中任何 2025 年 USENIX Security 论文，属明确的召回缺口。**

4. **内存安全成为 2024–2026 的独立热点**。deepSURF 用 LLM 增强 harness 检测 Rust `unsafe` 代码中的内存漏洞 [51]；同时出现"反自动化乐观论"的证据——用户研究表明人工 C→Rust 翻译困难 [52]，且"C-to-Rust 自动重构 ≠ 内存安全" [57]、RustCompCert 尝试给出经形式化验证的 Rust 子集编译器 [55]。

5. **密码学与后量子迁移在本候选集中证据极稀薄**。仅能引用到密钥管理方向 [6] 与资源受限 IoT 的 PSA 证明令牌评估 [50]，**无 PQC（后量子密码）迁移的一手证据**，该章应整体标注 `> 待核实`。

6. **方法论警示**：本候选集混入大量与主题无关的检索噪声（如德语开放式问卷编码 [32]、短视频参与度挑战 [13]、SemEval 主题标引 [15]、Ego4D 定位 [56]、小行星碎裂 [24]）。**这些条目不应作为网络安全结论使用，仅作为检索式需收窄的证据。**

---

## 一、关键前沿进展（近 1–2 年，2024-10 → 2026-10）

以下按"是否真前沿四问"（多任务/多本体验证、开源可复现、提升可归因、独立评测）筛选。**本候选集几乎没有任何条目通过全部四问**，故均标注限制条件。

### 1.1 Agentic AI 攻击面的系统化（SoK）

- **名称**：SoK: The Attack Surface of Agentic AI - Tools and Autonomy
- **时间**：2026
- **一句话贡献**：把 LLM + 工具 + RAG + 多 Agent 决策环统一刻画为攻击面，指出能力扩张同时扩大攻击面 [36]。
- **证据轴**：热度证据 `> 待核实`（citations=0）；权威证据 = arXiv 预印本，未见同行评审与官方发布 [36]；关注度 = **低**（引用数 0，无社区量化信号）；推荐度 = **★★★☆☆**（主题高度相关、可作为攻击面清单起点，但需等待同行评审）。
- **局限**：candidate block 中为空摘要，无法确认是否给出可复现实验或威胁模型量化。

### 1.2 Web Agent 的多模态提示注入

- **名称**：WebInject: Prompt Injection Attack to Web Agents
- **时间**：2025
- **一句话贡献**：通过操纵网页环境（而非直接投喂文本）诱导基于 MLLM 的 Web Agent 执行攻击者动作 [27]。
- **证据轴**：热度证据 `> 待核实`（候选块未提供引用数）；权威证据 = arXiv cs.LG 预印本，未见会议 [27]；关注度 = **中**（Web Agent 是 2025 年热点，但本条无量化热度）；推荐度 = **★★★★☆**（Web Agent 安全的关键一手工作，建议精读并核实正式发表）。
- **局限**：需核实是否在真实浏览器/多站点环境中评测，而非单一沙箱。

### 1.3 SBOM 从"清单"到"图分析"

- **名称**：Towards Predicting Multi-Vulnerability Attack Chains in Software Supply Chains from Software Bill of Materials Graphs
- **时间**：2026
- **一句话贡献**：批评现有 SBOM 流水线把扫描结果按独立 CVE 处理，提出用 SBOM 图预测多漏洞级联攻击链 [46]。
- **证据轴**：热度证据 `> 待核实`（citations 未给出）；权威证据 = arXiv cs.SE 预印本 [46]；关注度 = **低**（尚无引用/榜单）；推荐度 = **★★★★☆**（抓住了 SBOM 实用化的核心痛点，方向性高价值）。
- **补充证据**：SBOM 工具生态的系统性文献综述指出 SBOM 价值"完全取决于其准确性与完整性" [48]；SoK: Analysis of Software Supply Chain Security by Establishing Secure Design Properties [38] 提供设计属性框架。

### 1.4 Rust 内存安全的攻防双面

- **进攻侧**：deepSURF 用 LLM 增强 harness 来 fuzz Rust `unsafe` 代码，弥补现有工具对 Rust 特有类型处理不足的问题 [51]（2025，cs.CR）。
- **防御/冷静侧**：C-to-Rust 自动重构 != 内存安全 [57]；用户研究表明人工翻译真实 C 代码到 Rust 存在实际困难 [52]；RustCompCert 尝试为 Rust 顺序子集提供端到端经验证的编译器 [55]。
- **证据轴**：热度 `> 待核实`（候选块均未给出引用数/star）；权威 = 均为 arXiv 预印本（cs.CR / cs.PL / cs.SE），无同行评审确认 [51][52][55][57]；关注度 = **中**（Rust 内存安全是 2024–2026 明确的社区热点，但本条证据无量化）；推荐度 = **★★★★☆**（[57] 的"反自动化乐观论"对工程决策最有用；[51] 可作攻防对照）。
- **补充**：SACTOR 提出 LLM 驱动的 C→Rust 正确且地道翻译 + 静态分析 + FFI 验证 [53]（未在本子问题候选摘要中出现，仅列入引用清单，`> 待核实`）。

### 1.5 符号执行回归"实践应用"叙事

- **名称**：Symbolic Execution in Practice: A Survey of Applications in Vulnerability, Malware, Firmware, and Protocol Analysis
- **时间**：2025
- **一句话贡献**：以路径爆炸为核心挑战，梳理符号执行在漏洞、恶意软件、固件、协议四大场景的落地方式 [21]。
- **证据轴**：热度 `> 待核实`（未给出引用数）；权威 = arXiv cs.CR 预印本 [21]；关注度 = **中**（综述形态、覆盖面广）；推荐度 = **★★★★☆**（适合作为该子问题的分类骨架）。
- **配套工具工作**：cozy 用比较符号执行分析同一二进制两版本差异，主用例是验证 micropatch [20]。

---

## 二、Web / 系统 / 供应链攻防

### 2.1 软件供应链攻击实证

| 名称 | 年份 | 机构/作者 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Supply Chain Attacks Through Open Source Software: NPM, PyPI, Docker Hub | 2025 | ODU Digital Commons | citations=1（[45]） | 机构知识库，同侪评审状态未确认 [45] | 低（citations=1） | ★★★☆☆ | https://doi.org/10.25776/h5ez-vq70 | 三大生态实证分析，样本"23 doc..."摘要截断 [45] |
| Software Supply Chain Security of Web3 | 2025 | arXiv cs.CR | `> 待核实` | arXiv 预印本 [42] | 低 | ★★★☆☆ | http://arxiv.org/abs/2511.12274v1 | dApps/智能合约的供应链漏洞 [42] |
| S3C2 Summit 2025-07: Government Secure Supply Chain Summit | 2026 | arXiv | citations=0 [47] | arXiv 预印本，社区峰会纪要 [47] | 低（citations=0） | ★★☆☆☆ | https://doi.org/10.48550/arxiv.2605.29140 | 政府视角，非研究性论文，适合政策线索 |
| SBOM Tooling Ecosystem: A Systematic Literature Review | 2026 | Applied Research（Wiley 系列，`> 待核实`） | citations=0 [48] | 综述期刊（同行评审状态待核实）[48] | 低 | ★★★★☆ | https://doi.org/10.1002/appl.70209 | SBOM 准确性/完整性决定其价值 [48] |
| SN Coherence Patch for Wallet Supply Chains | 2026 | Zenodo (CERN) | citations=0 [49] | Zenodo 预印本，形式化框架自述 [49] | 低 | ★★☆☆☆ | https://doi.org/10.5281/zenodo.18837490 | 比特币钱包 NPM/Electron 供应链，理论新颖但实证 `> 待核实` |

### 2.2 供应链经典与框架性工作（引用清单内）

| 名称 | 年份 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 链接 |
|---|---|---|---|---|---|---|
| SoK: Analysis of Software Supply Chain Security by Establishing Secure Design Properties | 2024 | `> 待核实` | arXiv 预印本 [38] | 中 | ★★★★☆ | http://arxiv.org/abs/2406.10109v1 |
| Trust in Software Supply Chains: Blockchain-Enabled SBOM and the AIBOM Future | 2023（v4） | `> 待核实` | arXiv 预印本 [39] | 中 | ★★★★☆ | http://arxiv.org/abs/2307.02088v4 |
| GoSurf: Identifying Software Supply Chain Attack Vectors in Go | 2024 | `> 待核实` | arXiv 预印本 [40] | 中 | ★★★★☆ | http://arxiv.org/abs/2407.04442v2 |
| Maven-Hijack: Supply Chain Attack Exploiting Packaging Order | 2024（v4） | `> 待核实` | arXiv 预印本 [43] | 中 | ★★★★☆ | http://arxiv.org/abs/2407.18760v4 |
| Software supply chain: review of attacks, risk assessment strategies and security controls | 2023 | `> 待核实` | arXiv 预印本 [44] | 中 | ★★★★☆ | http://arxiv.org/abs/2305.14157v1 |

> **待核实**：上述条目均未在本次检索中取得引用数、GitHub star 或官方榜单数据。判断其为"经典"仅依据摘要自述的主题覆盖度，**不足以定性为领域奠基工作**。

### 2.3 系统侧与 Web 侧

- 本候选集中，**系统级内存破坏/内核利用**主题除了 fuzzing 相关条目（见第三节）外，几乎无新证据。SyzScope 讨论 Linux 内核 fuzzer 暴露 bug 的高风险影响 [2]，属"发现→定级"闭环，而非新攻击面。
- **IoT/固件**：S3C2 峰会 [47] 与 PSA 证明令牌 [50] 涉及，但前者为纪要、后者为评估研究，均非攻击方法论。
- **信息操作（Information Operations）**：候选集含协调性跨平台信息操作研究 [22]，但摘要缺失，**与本报告"应用/系统/供应链"主线相关性弱**，`> 待核实`。

---

## 三、模糊测试与程序分析

### 3.1 明确的召回缺口（必须先声明）

> **q2 子问题（"coverage-guided fuzzing 2025 USENIX Security"）在候选集中零命中。** 候选 6 条中仅 2 条落在 2025 年（[7] 汽车软件更新形式化验证、[8] LLM 合成输入生成器），均未标注 USENIX Security 或任何会议录用；其余 coverage-guided 相关条目 [1][2][3][5] 时间跨度为 2021-11 至 2024-06，且候选块中全部登记为 arXiv cs.CR 预印本，无 venue 字段。
> **结论**：该子问题**无法由现有候选集回答**，必须改用 USENIX Security 2025 proceedings、dblp、OpenReview 定向补检。本节的"最新进展"因此仅覆盖 **方法演进线**，不覆盖 **2025 顶会 SOTA**。

### 3.2 技术脉络（2021 → 2025）

| 阶段 | 代表工作 | 年份 | 核心贡献 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 链接 |
|---|---|---|---|---|---|---|---|---|
| 覆盖率粒度与追踪开销 | Same Coverage, Less Bloat (CGT) | 2022 | binary-only 场景下覆盖追踪加速，解决 basic block 粒度与 edge coverage/hit counts 需求的矛盾 [3] | `> 待核实` | arXiv 预印本 [3] | 中 | ★★★★☆ | http://arxiv.org/abs/2209.03441v1 |
| 真实系统适应性 | Evaluating the Fork-Awareness of Coverage-Guided Fuzzers | 2023 | 评估 fuzzer 在含 fork/密码原语/校验和目标上的适应性，指出全自动化仍是难题 [1] | `> 待核实` | arXiv 预印本 [1] | 低 | ★★★☆☆ | http://arxiv.org/abs/2301.05060v1 |
| 调度与变异统一 | FOX: Coverage-guided Fuzzing as Online Stochastic Control | 2024 | 把 scheduler + mutator 联合建模为在线随机控制，缓解深层漏洞难触达 [5] | `> 待核实` | arXiv 预印本 [5] | 中 | ★★★★☆ | http://arxiv.org/abs/2406.04517v1 |
| LLM 辅助生成 | Low-Cost Non-textual Input Fuzzing with LLM-Synthesized Input Generators | 2025 | 用 LLM 合成输入生成器覆盖 images/videos/PDF 等非文本输入，绕开 LLM 直接生成非文本的高成本 [8] | `> 待核实` | arXiv cs.SE 预印本 [8] | 中 | ★★★★☆ | http://arxiv.org/abs/2501.19282v1 |
| 发现后的影响定级 | SyzScope | 2021 | 连续 fuzzing 平台忽视 bug 安全影响评估，从 syzbot 上千低风险 bug 中识别新高风险影响 [2] | `> 待核实` | arXiv 预印本 [2] | 中 | ★★★☆☆ | http://arxiv.org/abs/2111.06002v1 |

### 3.3 程序分析（符号执行与二进制）

| 名称 | 年份 | 一句话贡献 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 链接 |
|---|---|---|---|---|---|---|---|
| Symbolic Execution in Practice（综述） | 2025 | 梳理路径爆炸挑战下符号执行在漏洞/恶意软件/固件/协议的应用 [21] | `> 待核实` | arXiv cs.CR [21] | 中 | ★★★★☆ | http://arxiv.org/abs/2508.06643v1 |
| cozy: Comparative Symbolic Execution for Binary Programs | 2025 | 比较符号执行，验证二进制 micropatch 的差异可视化 [20] | `> 待核实` | arXiv cs

## 参考来源

[1] Evaluating the Fork-Awareness of Coverage-Guided Fuzzers — http://arxiv.org/abs/2301.05060v1
[2] SyzScope: Revealing High-Risk Security Impacts of Fuzzer-Exposed Bugs in Linux kernel — http://arxiv.org/abs/2111.06002v1
[3] Same Coverage, Less Bloat: Accelerating Binary-only Fuzzing with Coverage-preserving Coverage-guided Tracing — http://arxiv.org/abs/2209.03441v1
[4] Internet Service Providers' and Individuals' Attitudes, Barriers, and Incentives to Secure IoT — http://arxiv.org/abs/2210.02137v1
[5] FOX: Coverage-guided Fuzzing as Online Stochastic Control — http://arxiv.org/abs/2406.04517v1
[6] Multi-Factor Key Derivation Function (MFKDF) for Fast, Flexible, Secure, & Practical Key Management — http://arxiv.org/abs/2208.05586v3
[7] Towards a Formal Verification of Secure Vehicle Software Updates — http://arxiv.org/abs/2511.15479v1
[8] Low-Cost and Comprehensive Non-textual Input Fuzzing with LLM-Synthesized Input Generators — http://arxiv.org/abs/2501.19282v1
[9] LLMs Can Defend Themselves Against Jailbreaking in a Practical Manner: A Vision Paper — http://arxiv.org/abs/2402.15727v2
[10] Enhancing Jailbreak Attacks on LLMs via Persona Prompts — http://arxiv.org/abs/2507.22171v3
[11] Proactive defense against LLM Jailbreak — http://arxiv.org/abs/2510.05052v2
[12] Bypassing LLM Guardrails: An Empirical Analysis of Evasion Attacks against Prompt Injection and Jailbreak Detection Systems — http://arxiv.org/abs/2504.11168v3
[13] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1
[14] CAVGAN: Unifying Jailbreak and Defense of LLMs via Generative Adversarial Attacks on their Internal Representations — http://arxiv.org/abs/2507.06043v2
[15] Annif at SemEval-2025 Task 5: Traditional XMTC augmented by LLMs — http://arxiv.org/abs/2504.19675v2
[16] Securing LLM Powered AI Browsers Against Prompt Injection: A Comprehensive Survey, Threat Taxonomy, and Defense Framework — https://doi.org/10.2139/ssrn.6340078
[17] DARWIN: Evolving Jailbreak Adversary and Guardrail for LLM Safety Evaluation and Protection — http://arxiv.org/abs/2607.19829v2
[18] WEAPONIZING LARGE LANGUAGE MODELS: AUTOMATED PHISHING, SOCIAL ENGINEERING, AND MALWARE GENERATION — https://doi.org/10.5281/zenodo.18144131
[19] WEAPONIZING LARGE LANGUAGE MODELS: AUTOMATED PHISHING, SOCIAL ENGINEERING, AND MALWARE GENERATION — https://doi.org/10.5281/zenodo.18144132
[20] cozy: Comparative Symbolic Execution for Binary Programs — http://arxiv.org/abs/2504.00151v1
[21] Symbolic Execution in Practice: A Survey of Applications in Vulnerability, Malware, Firmware, and Protocol Analysis — http://arxiv.org/abs/2508.06643v1
[22] Uncovering Coordinated Cross-Platform Information Operations Threatening the Integrity of the 2024 U.S. Presidential Election Online Discussion — http://arxiv.org/abs/2409.15402v2
[23] NTU-NPU System for Voice Privacy 2024 Challenge — http://arxiv.org/abs/2410.02371v1
[24] Atmospheric entry and fragmentation of small asteroid 2024 BX1: Bolide trajectory, orbit, dynamics, light curve, and spectrum — http://arxiv.org/abs/2403.00634v2
[25] Jacobi Stability Analysis for Systems of ODEs Using Symbolic Computation — http://arxiv.org/abs/2405.10578v3
[26] Event-Enriched Image Analysis Grand Challenge at ACM Multimedia 2025 — http://arxiv.org/abs/2508.18904v1
[27] WebInject: Prompt Injection Attack to Web Agents — http://arxiv.org/abs/2505.11717v4
[28] Automatic and Universal Prompt Injection Attacks against Large Language Models — http://arxiv.org/abs/2403.04957v1
[29] SecAlign: Defending Against Prompt Injection with Preference Optimization — http://arxiv.org/abs/2410.05451v3
[30] Learning From Failure: Integrating Negative Examples when Fine-tuning Large Language Models as Agents — http://arxiv.org/abs/2402.11651v2
[31] UniGuardian: A Unified Defense for Detecting Prompt Injection, Backdoor Attacks and Adversarial Attacks in Large Language Models — http://arxiv.org/abs/2502.13141v2
[32] AIn't Nothing But a Survey? Using Large Language Models for Coding German Open-Ended Survey Responses on Survey Motivation — http://arxiv.org/abs/2506.14634v3
[33] StruQ: Defending Against Prompt Injection with Structured Queries — http://arxiv.org/abs/2402.06363v2
[34] Hijacking the Prompt: A Survey of Prompt Injection Attacks, Detection, and Defense in Large Language Models — https://doi.org/10.25776/mvhf-w867
[35] Scaling Behavior of Machine Translation with Large Language Models under Prompt Injection Attacks — http://arxiv.org/abs/2403.09832v1
[36] SoK: The Attack Surface of Agentic AI - Tools and Autonomy — https://doi.org/10.48550/arxiv.2603.22928
[37] Interaction-Centric Cybersecurity Risks in LLM-Powered Dialogue Systems — https://doi.org/10.1109/ccwc67433.2026.11393850
[38] SoK: Analysis of Software Supply Chain Security by Establishing Secure Design Properties — http://arxiv.org/abs/2406.10109v1
[39] Trust in Software Supply Chains: Blockchain-Enabled SBOM and the AIBOM Future — http://arxiv.org/abs/2307.02088v4
[40] GoSurf: Identifying Software Supply Chain Attack Vectors in Go — http://arxiv.org/abs/2407.04442v2
[41] Exploitation of material consolidation trade-offs in multi-tier complex supply networks — http://arxiv.org/abs/2210.11479v3
[42] Software Supply Chain Security of Web3 — http://arxiv.org/abs/2511.12274v1
[43] Maven-Hijack: Software Supply Chain Attack Exploiting Packaging Order — http://arxiv.org/abs/2407.18760v4
[44] Software supply chain: review of attacks, risk assessment strategies and security controls — http://arxiv.org/abs/2305.14157v1
[45] Supply Chain Attacks Through Open Source Software: A Comprehensive Analysis of NPM, PyPI, and Docker Hub Vulnerabilities — https://doi.org/10.25776/h5ez-vq70
[46] Towards Predicting Multi-Vulnerability Attack Chains in Software Supply Chains from Software Bill of Materials Graphs — http://arxiv.org/abs/2604.04977v2
[47] S3C2 Summit 2025-07: Government Secure Supply Chain Summit — https://doi.org/10.48550/arxiv.2605.29140
[48] SBOM Tooling Ecosystem: A Systematic Literature Review — https://doi.org/10.1002/appl.70209
[49] SN Coherence Patch for Wallet Supply Chains — https://doi.org/10.5281/zenodo.18837490
[50] Performance Analysis and Security Evaluation of RFC 9783 PSA Attestation Tokens in Resource-Constrained IoT Environments — https://doi.org/10.1109/acdsa67686.2026.11467770
[51] deepSURF: Detecting Memory Safety Vulnerabilities in Rust Through Fuzzing LLM-Augmented Harnesses — http://arxiv.org/abs/2506.15648v2
[52] Translating C To Rust: Lessons from a User Study — http://arxiv.org/abs/2411.14174v2
[53] SACTOR: LLM-Driven Correct and Idiomatic C to Rust Translation with Static Analysis and FFI-Based Verification — http://arxiv.org/abs/2503.12511v3
[54] Rust for Secure Backend Development: A Critical Review and Extended Vulnerability Comparison with Node.js and Django — http://arxiv.org/abs/2608.22624v1
[55] RustCompCert: A Verified and Verifying Compiler for a Sequential Subset of Rust — http://arxiv.org/abs/2602.07455v1
[56] OSGNet @ Ego4D Episodic Memory Challenge 2025 — http://arxiv.org/abs/2506.03710v1
[57] C-to-Rust Fallacy: Automatic Refactoring != Memory Security — http://arxiv.org/abs/2609.25682v1


---

*Generated by research-bot · topic=`cybersecurity` · depth=`standard` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading · model=`deepseek-v4-flash` · sources=57 · duration=205s · 2026-10-02T22:15:55+00:00*
