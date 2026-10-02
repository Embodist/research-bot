# 网络安全前沿调研报告：LLM/Agent 安全、漏洞挖掘与软件供应链（2024–2026）

- **日期**：2026-10-02（UTC）
- **领域**：Cybersecurity — ①LLM/Agent 安全（prompt injection / jailbreak / guardrail / 数据外泄）②软件与二进制漏洞挖掘（fuzzing / 符号执行 / 内存安全）③软件供应链与恶意软件分析 ④后量子密码迁移
- **检索源**：36 条编号证据（[1]–[36]，其中 [36] 与主题不相关，未采用）+ 3 类领域种子资源（papers / projects / datasets，未纳入编号引用体系，热度数据一律标注 `> 待核实`）
- **证据总体强度**：本批 36 条证据中仅 [1] 具备可核查的引用数（citations=116）与顶级会议 venue；其余条目引用数均为 0 或未知 `> 待核实`，且大量来自 SSRN / Research Square / Preprints.org / 工作坊论文集等弱评审渠道。**本报告因此明确区分「论文宣称」与「第三方复现/榜单结果」，凡无第三方证据者一律加限定词或标注 `> 待核实`。**

---

## 摘要（Executive Summary）

1. **LLM/Agent 安全是 2025–2026 年数量增长最快、但证据质量最弱的一条主线。** 本批命中 12 条相关文献（[13]–[24]），全部 `citations=0`，且多数来自 SSRN [14][18][22]、Research Square [19]、Preprints.org [21]、InterConf [23] 等非同行评审渠道。唯一具备较强权威性的判断来自 [13] 的转述：prompt injection 在 OWASP 2025 年 LLM Applications Top 10 中位列第一，且「largely unsolved」[13]。Agentic 场景的攻击面系统化梳理见 arXiv 预印本 [15]。
2. **模糊测试方向「经典清晰、SOTA 分散」。** 奠基性性能优化工作为 *Full-Speed Fuzzing*（IEEE S&P 2019，citations=116）[1]；2025–2026 年的前沿不再是通用二进制 fuzzing，而是向**特定协议栈**（RPKI，IEEE S&P 2026）[3]、**有状态服务接口**（REST API，ICISSP 2026）[4]、**移动端 intent**（NDSS 2025）[5]、**环境敏感恶意软件**（EuroS&P 2025）[6]、**机器人中间件**（ROS，IEEE TIFS 2025）[7]、**硬件描述语言**（SpinalHDL）[8] 等垂直域扩散。
3. **软件供应链安全已从「概念倡导」进入「可测量 + 可攻击」阶段。** 攻击侧出现新的构建期攻击面 Maven-Hijack（打包顺序攻击，SCORED 2025）[31]；防守侧出现 SBOM 在 GitHub Actions 生态的大规模实证 [33]、SBOM 驱动的容器镜像风险筛查（128 微服务 / 三云环境）[26]、以及用 SBOM 元数据做 ML 漏洞预测 [25][30]；官方基线为 NIST SP 1800-44 [27]。
4. **两个明确的证据缺口，必须如实标注。** 本批 36 条证据中，**没有任何一条**涉及①恶意软件分析的公开数据集与评测基准、②后量子密码（PQC）迁移的工程实践（混合密钥交换、代码签名/固件/证书迁移路径、迁移时间表）。这两部分**无法给出可核查结论**，第 五、六 章相应小节将标注 `> 待核实` 并给出待检索问题清单。
5. **横向可比性缺失是三条主线的共同短板。** 本批论文几乎全部**未提供可横向比较的量化指标**（CVE 数量、吞吐量、攻击成功率、准确率）与**开源仓库/star 信息**，因此「谁更强」在本批证据下不可判定。

---

## 一、关键前沿进展（近 1–2 年）

### 1.1 最新进展速览（2025–2026）

| 名称 | 时间 | 机构 / 作者 | 热度 | 权威 | 链接 | 一句话贡献 |
|---|---|---|---|---|---|---|
| Hijacking the Prompt: A Survey of Prompt Injection Attacks, Detection, and Defense in LLMs | 2026 | Old Dominion University（ODU Digital Commons） | citations=0 [13] | 机构知识库收录综述；同行评审状态 `> 待核实` | https://doi.org/10.25776/mvhf-w867 | 系统梳理 prompt injection 攻/检/防，并解释其为何在 OWASP LLM Top 10 位列第一后仍「largely unsolved」[13] |
| SoK: The Attack Surface of Agentic AI - Tools and Autonomy | 2026 | arXiv（Cornell University） | citations=0 [15] | arXiv 预印本（B 级） | https://doi.org/10.48550/arxiv.2603.22928 | 将「LLM + 工具 + RAG + 多 Agent 决策环」的攻击面系统化（SoK）[15] |
| Securing LLM Powered AI Browsers Against Prompt Injection | 2026 | SSRN Electronic Journal | citations=0 [14] | SSRN 预印本/工作论文，非同行评审 | https://doi.org/10.2139/ssrn.6340078 | 面向 AI 浏览器的 prompt injection 威胁分类与防御框架 [14] |
| Interaction-Centric Cybersecurity Risks in LLM-Powered Dialogue Systems | 2026 | IEEE（CCWC 2026，据 DOI 命名推断） | citations=0 [16] | 据 DOI 前缀 `10.1109/ccwc67433.2026` 推断为 IEEE 会议论文；`> 待核实` | https://doi.org/10.1109/ccwc67433.2026.11393850 | 提出传统 AI 安全框架无法覆盖的「交互中心」风险概念 [16] |
| Cross-Agent Multimodal Provenance-Aware Framework for Robust Prompt Injection Defense | 2025 | IEEE（ICCA 2025，据 DOI 推断） | `> 待核实` | 据 DOI 前缀 `10.1109/icca66035.2025` 推断；`> 待核实` | https://doi.org/10.1109/icca66035.2025.11430791 | 跨 Agent、多模态、来源溯源（provenance）导向的注入防御 [17] |
| Evaluating Hybrid Guardrail Architectures for Prompt Injection Defense | 2025 | SSRN | `> 待核实` | SSRN 预印本 | https://doi.org/10.2139/ssrn.6246379 | 对混合式 guardrail 架构进行评测 [18] |
| A Multi-Agent Framework for Explainable Prompt Injection Detection | 2025 | Research Square 预印本 | `> 待核实` | 预印本，未同行评审 | https://doi.org/10.21203/rs.3.rs-10302085/v1 | 多 Agent + 可解释性的注入检测框架 [19] |
| Prompt Injection Attacks on LLMs: Multi-Model Security Analysis with Categorized Attack Types | 2025 | SciTePress（据 DOI 推断） | `> 待核实` | 据 DOI `10.5220/...` 推断为会议论文；`> 待核实` | https://doi.org/10.5220/0013838400004000 | 跨多模型、按攻击类型分类的安全对比分析 [24] |
| MALintent: Coverage Guided Intent Fuzzing Framework for Android | 2025 | NDSS 2025（据 DOI `10.1109/ndss.2025` 推断） | `> 待核实` | 顶级安全会议（推断）；`> 待核实` | https://doi.org/10.14722/ndss.2025.230125 | 将覆盖引导 fuzzing 应用于 Android intent 层 [5] |
| Detecting Lifecycle-Related Concurrency Bugs in ROS Programs via Coverage-Guided Fuzzing | 2025 | IEEE TIFS（据 DOI `10.1109/tifs.2025` 推断） | `> 待核实` | IEEE 期刊（推断）；`> 待核实` | https://doi.org/10.1109/tifs.2025.3592562 | **机器人中间件 ROS 的生命周期并发缺陷**可用覆盖引导 fuzzing 检出 [7] |
| Pfuzzer: Multi-path Analysis of Environment-sensitive Malware with Coverage-guided Fuzzing | 2025 | IEEE EuroS&P 2025 | citations=0 [6] | 同行评审（EuroS&P） | https://doi.org/10.1109/eurosp63326.2025.00068 | 用覆盖引导 fuzzing 对**环境敏感恶意软件**做多路径分析 [6] |
| Batch Me If You Can: Coverage-Guided RPKI Fuzzing at Scale | 2026 | IEEE S&P 2026 | citations=0 [3] | 同行评审（顶级安全会议） | https://doi.org/10.1109/sp63933.2026.00188 | 对 RPKI 路由安全协议栈做大规模覆盖引导 fuzzing [3] |
| WuppieFuzz: Coverage-Guided, Stateful REST API Fuzzing | 2026 | ICISSP 2026（SciTePress） | citations=0 [4] | 同行评审，但非安全四大顶会 | https://doi.org/10.5220/0014327000004061 | 有状态 REST API 的覆盖引导 fuzzing，面向真实服务接口 [4] |
| Maven-Hijack: Software Supply Chain Attack Exploiting Packaging Order | 2025 | SCORED 2025（ACM 工作坊） | citations=0 [31] | 工作坊论文，同行评审（强度弱于主会） | https://doi.org/10.1145/3733827.3765523 | 揭示**打包顺序**这一新型供应链攻击面 [31] |
| An Empirical Study of SBOM Usage Through GitHub Actions | 2026 | IEEE Access | citations=0 [33] | 同行评审期刊 | https://doi.org/10.1109/access.2026.3698914 | 以 GitHub Actions 生态为样本实证 SBOM 的真实采用情况 [33] |
| RISK-AWARE SOFTWARE SUPPLY CHAIN SECURITY FOR AVIATION SYSTEMS USING SBOM | 2026 | Computer Science Bulletin | citations=0 [26] | Crossref 收录；同行评审状态 `> 待核实` | https://doi.org/10.71465/csb213 | SBOM 驱动的容器镜像风险筛查，测试系统含 128 微服务 / 三云环境 [26] |
| A ML-Based Vulnerability Prediction System Using SBOM Metadata | 2026 | 韩国通信与信息科学学会期刊（KICS） | citations=0 [30] | 同行评审期刊 | https://doi.org/10.7840/kics.2026.51.4.792 | 把 SBOM 从「清单」变为「风险预测特征源」[30] |
| SBOM-Based Vulnerability Prioritization Using Machine Learning | 2025 | 据 DOI `10.17721/ait.2025.2.04` 推断 | `> 待核实` | `> 待核实`（期刊信息需回原文核实） | https://doi.org/10.17721/ait.2025.2.04 | 用 ML 对 SBOM 漏洞做优先级排序 [25] |
| BC-SBOM: Blockchain-based SBOM Management System | 2025 | ICACT 2025（据 DOI 推断） | `> 待核实` | 据 DOI 前缀推断为 IEEE 会议；`> 待核实` | https://doi.org/10.23919/icact63878.2025.10936765 | 用区块链管理 SBOM 的完整性与可信 [34] |
| cozy: Comparative Symbolic Execution for Binary Programs | 2025 | BAR 2025（Workshop on Binary Analysis Research，据 DOI 推断） | `> 待核实` | 工作坊论文；`> 待核实` | https://doi.org/10.14722/bar.2025.23004 | 面向二进制的**比较式符号执行**（comparative symbolic execution）[12] |
| CBGF: Callback Coverage Guided Fuzzing | 2025 | IEEE Access | `> 待核实` | 同行评审期刊（据 DOI `10.1109/access.2025` 推断） | https://doi.org/10.1109/access.2025.3561135 | 以回调覆盖为反馈信号的新型覆盖引导 fuzzing [2] |
| NIST SP 1800-44: Software Supply Chain and DevOps Security Practices | 2025（据编号推断） | NIST | `> 待核实` | 美国政府官方标准/实践指南（最高权威档） | https://doi.org/10.6028/nist.sp.1800-44 | 软件供应链与 DevOps 安全实践的官方基线 [27] |

> **可核查性说明**：上表「机构/作者」列中凡标注「据 DOI 推断」者，均为根据 DOI 前缀（如 `10.1109/ndss.2025`、`10.5220`、`10.23919/icact`）作出的**推断**，未在本批检索中取得原文首页确认，一律视为 `> 待核实`。所有 `citations=0` 均来自候选块的原始字段，未做推断或放大。

### 1.2 与「经典工作」的分界

本报告将 **≤2022 年发表且已被后续工作反复引用的工作** 列为经典（见 1.3 节与第三章表格），将 **2025–2026 年发表** 的工作列为最新进展。需要强调：2025–2026 年条目 `citations=0` **不代表影响力低**，而是引用时滞所致（本批证据中 [3][4][6] 明确标注为「新近发表，引用时滞」）。

### 1.3 经典与奠基性工作

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 链接 | 说明 |
|---|---|---|---|---|---|---|
| Full-Speed Fuzzing: Reducing Fuzzing Overhead through Coverage-Guided Tracing | 2019 | IEEE S&P 2019 | **citations=116** [1] | 同行评审顶级安全会议（A 级） | https://doi.org/10.1109/sp.2019.00069 | 覆盖引导模糊测试的**性能优化奠基工作**，通过覆盖引导追踪降低 fuzzing 开销 [1]；本批中唯一具备可核查引用数的条目 |
| A hybrid symbolic execution assisted fuzzing method | 2017 | IEEE TENCON 2017（据 DOI 推断） | `> 待核实` | 会议论文；`> 待核实` | https://doi.org/10.1109/tencon.2017.8227972 | 混合符号执行辅助 fuzzing 的早期代表性工作 [9] |
| A Survey of Hybrid Fuzzing based on Symbolic Execution | 2020（据 DOI 编号推断） | ACM（据 DOI `10.1145/3444370.3444570` 推断） | `> 待核实` | `> 待核实` | https://doi.org/10.1145/3444370.3444570 | 混合 fuzzing（concolic / 符号执行 + 模糊测试）的方法学综述，可作为该分支的分类骨架 [10] |
| Fuzzing and Symbolic Execution for Multipath Malware Tracing: Bridging Theory and Practice via Survey and Experiments | 2024（据 DOI 编号推断） | ACM（据 DOI `10.1145/3700147` 推断） | `> 待核实` | `> 待核实` | https://doi.org/10.1145/3700147 | 连接「模糊测试/符号执行」与「多路径恶意软件追踪」的综述 + 实验，是跨越第二、三主线的关键桥梁文献 [11] |
| SpinalFuzz: Coverage-Guided Fuzzing for SpinalHDL Designs | 2022 | IEEE ETS 2022（据 DOI 推断） | `> 待核实` | 会议论文；`> 待核实` | https://doi.org/10.1109/ets54262.2022.9810421 | 将覆盖引导 fuzzing 从软件扩展到硬件描述语言设计 [8] |
| Inferring Fine-grained Control Flow Inside SGX Enclaves with Branch Shadowing | 2017 | USENIX Security | `> 待核实`（种子资源，无编号引用） | 同行评审顶级安全会议（A 级，种子资源标注） | https://www.usenix.org/conference/usenixsecurity17 | 侧信道攻击经典（种子资源示例性 A 级来源）；本批检索未取得其引用数，热度 `> 待核实` |
| OWASP Top 10 (Web & LLM Applications) | 2021 / 2025 | OWASP | `> 待核实`（种子资源） | 行业权威风险基线清单；非同行评审但被广泛引用 | https://owasp.org/www-project-top-ten/ | Web 与 LLM 应用的风险基线；[13] 引述其 2025 LLM Top 10 将 prompt injection 列为第一 [13] |
| CWE (Common Weakness Enumeration) | ongoing | MITRE | `> 待核实`（种子资源） | 官方标准/权威分类法 | https://cwe.mitre.org/ | 弱点分类标准，漏洞挖掘与供应链风险命名的公共词汇表 |

> **注意**：种子资源（SGX 侧信道、OWASP、CWE 等）来自本地 skills 的领域预置清单，**未纳入本次 [n] 编号引用体系，也未在本批检索中实时核验**，其链接与年份可直接复用，但热度数据一律 `

## 参考来源

[1] Full-Speed Fuzzing: Reducing Fuzzing Overhead through Coverage-Guided Tracing — https://doi.org/10.1109/sp.2019.00069
[2] CBGF: Callback Coverage Guided Fuzzing — https://doi.org/10.1109/access.2025.3561135
[3] Batch Me If You Can: Coverage-Guided RPKI Fuzzing at Scale — https://doi.org/10.1109/sp63933.2026.00188
[4] WuppieFuzz: Coverage-Guided, Stateful REST API Fuzzing — https://doi.org/10.5220/0014327000004061
[5] MALintent: Coverage Guided Intent Fuzzing Framework for Android — https://doi.org/10.14722/ndss.2025.230125
[6] Pfuzzer: Practical, Sound, and Effective Multi-path Analysis of Environment-sensitive Malware with Coverage-guided Fuzzing — https://doi.org/10.1109/eurosp63326.2025.00068
[7] Detecting Lifecycle-Related Concurrency Bugs in ROS Programs via Coverage-Guided Fuzzing — https://doi.org/10.1109/tifs.2025.3592562
[8] SpinalFuzz: Coverage-Guided Fuzzing for SpinalHDL Designs — https://doi.org/10.1109/ets54262.2022.9810421
[9] A hybrid symbolic execution assisted fuzzing method — https://doi.org/10.1109/tencon.2017.8227972
[10] A Survey of Hybrid Fuzzing based on Symbolic Execution — https://doi.org/10.1145/3444370.3444570
[11] Fuzzing and Symbolic Execution for Multipath Malware Tracing: Bridging Theory and Practice via Survey and Experiments — https://doi.org/10.1145/3700147
[12] cozy: Comparative Symbolic Execution for Binary Programs — https://doi.org/10.14722/bar.2025.23004
[13] Hijacking the Prompt: A Survey of Prompt Injection Attacks, Detection, and Defense in Large Language Models — https://doi.org/10.25776/mvhf-w867
[14] Securing LLM Powered AI Browsers Against Prompt Injection: A Comprehensive Survey, Threat Taxonomy, and Defense Framework — https://doi.org/10.2139/ssrn.6340078
[15] SoK: The Attack Surface of Agentic AI - Tools and Autonomy — https://doi.org/10.48550/arxiv.2603.22928
[16] Interaction-Centric Cybersecurity Risks in LLM-Powered Dialogue Systems — https://doi.org/10.1109/ccwc67433.2026.11393850
[17] Cross-Agent Multimodal Provenance-Aware Framework for Robust Prompt Injection Defense in Large Language and Vision-Language Models — https://doi.org/10.1109/icca66035.2025.11430791
[18] Evaluating Hybrid Guardrail Architectures for Prompt Injection Defense in Large Language Models — https://doi.org/10.2139/ssrn.6246379
[19] A Multi-Agent Framework for Explainable Prompt Injection Detection in Large Language Models — https://doi.org/10.21203/rs.3.rs-10302085/v1
[20] Prompt Injection Attacks Risks and Defense Mechanisms — https://doi.org/10.4018/979-8-3373-7133-7.ch005
[21] Prompt Injection Attacks in Large Language Models and AI Agent Systems: A Comprehensive Review of Vulnerabilities, Attack Vectors, and Defense Mechanisms — https://doi.org/10.20944/preprints202511.0088.v1
[22] Prompt Injection and Jailbreak Attacks in Large Language Model-Based Agents — https://doi.org/10.2139/ssrn.6740060
[23] Taxonomy of Prompt Injection Attacks and Analysis of Defense Mechanisms in Large Language Model-Based Chatbots — https://doi.org/10.51582/interconf.19-20.05.2026.017
[24] Prompt Injection Attacks on Large Language Models: Multi-Model Security Analysis with Categorized Attack Types — https://doi.org/10.5220/0013838400004000
[25] SBOM-BASED VULNERABILITY PRIORITIZATION IN SOFTWARE SUPPLY CHAIN USING MACHINE LEARNING — https://doi.org/10.17721/ait.2025.2.04
[26] RISK-AWARE SOFTWARE SUPPLY CHAIN SECURITY FOR AVIATION SYSTEMS USING SBOM — https://doi.org/10.71465/csb213
[27] Software Supply Chain and DevOps Security Practices — https://doi.org/10.6028/nist.sp.1800-44
[28] Case Studies in Software Supply Chain Security — https://doi.org/10.1007/979-8-8688-0799-2_8
[29] Emerging Trends in Software Supply Chain Security — https://doi.org/10.1007/979-8-8688-0799-2_10
[30] A Machine Learning-Based Vulnerability Prediction System Using SBOM Metadata for Software Supply Chain Security — https://doi.org/10.7840/kics.2026.51.4.792
[31] Maven-Hijack: Software Supply Chain Attack Exploiting Packaging Order — https://doi.org/10.1145/3733827.3765523
[32] Implementing Comprehensive Security in Your Software Supply Chain — https://doi.org/10.1007/979-8-8688-0799-2_9
[33] An Empirical Study of SBOM Usage Through GitHub Actions — https://doi.org/10.1109/access.2026.3698914
[34] BC-SBOM: Blockchain-based SBOM Management System — https://doi.org/10.23919/icact63878.2025.10936765
[35] Strengthening License Compliance and Software Security with SBOM Adoption: A Definitive SBOM Guide for Enterprises — https://doi.org/10.70828/vhin7583
[36] EVALUATION OF TRAINING EFFECTIVENESS IN EDUCATION SECTOR: AN EMPIRICAL STUDY — https://doi.org/10.2139/ssrn.5229932


---

*Generated by research-bot · topic=`cybersecurity` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading · model=`deepseek-v4-flash` · sources=36 · duration=388s · 2026-10-02T10:22:17+00:00*
