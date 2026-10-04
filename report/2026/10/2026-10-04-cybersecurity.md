# 网络安全攻防全景调研报告（2024–2026）：从漏洞利用到 LLM/Agent 安全与后量子迁移

**日期**：2026-10-04（UTC）
**领域**：Cybersecurity（网络安全）——漏洞与利用、模糊测试与程序分析、软件供应链/SBOM、恶意软件分析、后量子密码迁移、LLM/Agent 安全
**检索源**：本轮候选证据池共 127 条编号来源（arXiv 预印本、DOI 期刊/会议条目为主），正文实际引用 74 条；其余编号经相关性审查判定为主题噪声（见下文说明）
**证据基线**：A 级 = 同行评审会议/期刊（含 ICSE、FSE、QRS、APSEC、CCS Workshop 等 DOI 条目）；B 级 = arXiv 预印本 / 官方仓库；C 级 = 第三方评测与调查；D 级 = 社区与二手内容；E 级 = 不可用，已丢弃

> **证据基础与检索噪声说明（重要）**
> 本轮候选池中相当一部分条目与网络安全无关，属检索召回噪声，本报告已剔除且不予引用，例如：短视频参与度挑战 [2]、图像超分辨率挑战 [19]、天文强透镜宇宙学 [23]、IEEE VIS 多模态远程协作工作坊 [51]、SemEval 主题标引 [45]、科学方程发现基准 [112]、引文预测共享任务 [116]、金融分析基准 [124]、以及一组关于数学中 "magma"（泛代数结构）的论文 [121][122]。特别提醒：**模糊测试基准 Magma** [117][118] 与数学对象 magma 及无线接入网络项目 Magma 属同名不同物，检索时极易混淆，引用前必须核对 arXiv 编号。
> 此外，部分条目仅有 DOI 而无 arXiv 编号（如 [28][33][35][98][100][101][105][109]），其同行评审状态与完整元数据本轮**未能核验**，相关结论一律降级表述或标注 `> 待核实`。

---

## 摘要（Executive Summary）

1. **LLM/Agent 安全已成为该领域增长最快、但证据最不成熟的分支。** 2024–2026 年出现了从「单轮提示注入」向「间接注入 + Agent 工具链 + 多模态 Web Agent」的明确迁移：攻击侧从自动通用注入 [125] 走到针对网页环境的 WebInject [27]；防御侧从结构化查询 StruQ [25]、偏好优化 SecAlign [26]，演进到 MELON 的可证明防御 [30]、工具依赖图 IPIGuard [29]、多 Agent 流水线 [32] 与零样本嵌入漂移检测 [34]。**但防御的独立验证仍是最大缺口**：自适应攻击研究直接表明现有间接提示注入防御可被攻破 [31]，而绝大多数防御结论仅来自预印本自评，属 B 级证据。

2. **模糊测试的主线已从「覆盖率驱动」转向「定向 + 混合 + LLM 辅助」。** 经典脉络由 coverage-guided tracing 降开销 [82]、二进制专用 fuzzing [50]、fork-awareness 评测 [49]、在线随机控制 FOX [53] 等构成；近两年新增长点集中在定向灰盒（DGF）的结合 LLM 路径/调用栈预测 [66][70]、库漏洞从客户端触发 [69]、嵌入式网络栈协议感知 rehosting [123]、以及覆盖率引导 + LLM 突变的 JS 引擎 fuzzing（CovRL）[89]。混合测试（fuzzing + 符号执行 + 采样）以 S²F [60]、PathFuzzing [61] 为代表，试图在原理层面统一三类技术。

3. **符号执行正在被「LLM 化」和「工程化」两条腿同时拉动。** 工程侧关注真实可用性：闭盒函数处理 IFSE [80]、分支覆盖驱动 [81]、具体约束引导 [84]、KLEE 确定性分配器 KDAlloc [83]、LLM 生成测试用例 [85]；LLM 侧则出现用 LLM 模拟 KLEE 输出 [74] 与 LLM 引导 KLEE 定向探索 [78] 的对立性探索。2025 年综述 [56] 与混合测试综述 [57] 可作为分类骨架。

4. **软件供应链安全从「单点 CVE 扫描」转向「级联攻击链与 SBOM 图推理」。** 代表工作是 2026 年把 SBOM 图用于多漏洞攻击链预测 [8] 与级联漏洞攻击建模 [9]；SBOM 生态本身（SPDX vs CycloneDX 工具链）已被系统性比较 [1]，设计属性层面的 SoK [3] 与区块链/AIBOM 方向 [5] 提供了架构视角。恶意包检测从 NPM/PyPI 双生态单模型 [10]、跨语言检测 [11]、动态分析 DySec [13]，走到强调对抗变换鲁棒性与可调 FPR 的「One Detector Fits All」[15]，以及 NPM 低/无功能包治理 [17]。

5. **后量子密码（PQC）已从「算法标准化」进入「工程迁移与性能博弈」阶段。** 迁移侧的实证工作包括：九大开源密码库的 PQC 支持评估 [96]、ML-DSA/SLH-DSA 在 TLS 1.3 证书层级中的签名放置实验 [102]、TLS 1.3 经典/混合/纯后量子握手的分层性能分析 [103]、2026 年互联网 PQC 就绪度测量 [104]，以及「策略 vs 现实」的部署差距研究 [110]。编码 Agent 被尝试用于自动迁移（RSA→ML-DSA-44）[93]，企业 WAN 的迁移风险评估框架亦已提出 [94]。经典约束仍来自移动端能耗 [92] 与密码敏捷性研究挑战 [99]。

6. **评测可复现性是贯穿全领域的结构性争议。** 对 12 篇 LLM Agent 基准论文的审计 [111] 直接指出「同名基准

## 参考来源

[1] The State of the SBOM Tool Ecosystems: A Comparative Analysis of SPDX and CycloneDX — http://arxiv.org/abs/2512.21781v2
[2] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1
[3] SoK: Analysis of Software Supply Chain Security by Establishing Secure Design Properties — http://arxiv.org/abs/2406.10109v1
[4] Exploitation of material consolidation trade-offs in multi-tier complex supply networks — http://arxiv.org/abs/2210.11479v3
[5] Trust in Software Supply Chains: Blockchain-Enabled SBOM and the AIBOM Future — http://arxiv.org/abs/2307.02088v4
[6] GoSurf: Identifying Software Supply Chain Attack Vectors in Go — http://arxiv.org/abs/2407.04442v2
[7] Maven-Hijack: Software Supply Chain Attack Exploiting Packaging Order — http://arxiv.org/abs/2407.18760v4
[8] Towards Predicting Multi-Vulnerability Attack Chains in Software Supply Chains from Software Bill of Materials Graphs — http://arxiv.org/abs/2604.04977v2
[9] Cascaded Vulnerability Attacks in Software Supply Chains — http://arxiv.org/abs/2601.20158v1
[10] Killing Two Birds with One Stone: Malicious Package Detection in NPM and PyPI using a Single Model of Malicious Behavior Sequence — http://arxiv.org/abs/2309.02637v2
[11] On the Feasibility of Cross-Language Detection of Malicious Packages in npm and PyPI — http://arxiv.org/abs/2310.09571v1
[12] SpellBound: Defending Against Package Typosquatting — http://arxiv.org/abs/2003.03471v1
[13] DySec: A Machine Learning-based Dynamic Analysis for Detecting Malicious Packages in PyPI Ecosystem — http://arxiv.org/abs/2503.00324v1
[14] Practical Automated Detection of Malicious npm Packages — http://arxiv.org/abs/2202.13953v1
[15] One Detector Fits All: Robust and Adaptive Detection of Malicious Packages from PyPI to Enterprises — http://arxiv.org/abs/2512.04338v1
[16] A Survey on Common Threats in npm and PyPi Registries — http://arxiv.org/abs/2108.09576v1
[17] Detecting and Characterizing Low and No Functionality Packages in the NPM Ecosystem — http://arxiv.org/abs/2510.04495v1
[18] Supply Chain Attacks Through Open Source Software: A Comprehensive Analysis of NPM, PyPI, and Docker Hub Vulnerabilities — https://doi.org/10.25776/h5ez-vq70
[19] NTIRE 2025 Challenge on Image Super-Resolution (x4): Methods and Results — http://arxiv.org/abs/2504.14582v3
[20] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1
[21] VLSP 2025 MLQA-TSR Challenge: Vietnamese Multimodal Legal Question Answering on Traffic Sign Regulation — http://arxiv.org/abs/2510.20381v1
[22] The AudioMOS Challenge 2025 — http://arxiv.org/abs/2509.01336v1
[23] TDCOSMO 2025: Cosmological constraints from strong lensing time delays — http://arxiv.org/abs/2506.03023v4
[24] TRUST 2025: SCRITA and RTSS @ RO-MAN 2025 — http://arxiv.org/abs/2509.11402v1
[25] StruQ: Defending Against Prompt Injection with Structured Queries — http://arxiv.org/abs/2402.06363v2
[26] SecAlign: Defending Against Prompt Injection with Preference Optimization — http://arxiv.org/abs/2410.05451v3
[27] WebInject: Prompt Injection Attack to Web Agents — http://arxiv.org/abs/2505.11717v4
[28] Securing LLM Powered AI Browsers Against Prompt Injection: A Comprehensive Survey, Threat Taxonomy, and Defense Framework — https://doi.org/10.2139/ssrn.6340078
[29] IPIGuard: A Novel Tool Dependency Graph-Based Defense Against Indirect Prompt Injection in LLM Agents — http://arxiv.org/abs/2508.15310v1
[30] MELON: Provable Defense Against Indirect Prompt Injection Attacks in AI Agents — http://arxiv.org/abs/2502.05174v4
[31] Adaptive Attacks Break Defenses Against Indirect Prompt Injection Attacks on LLM Agents — http://arxiv.org/abs/2503.00061v2
[32] A Multi-Agent LLM Defense Pipeline Against Prompt Injection Attacks — http://arxiv.org/abs/2509.14285v4
[33] Hijacking the Prompt: A Survey of Prompt Injection Attacks, Detection, and Defense in Large Language Models — https://doi.org/10.25776/mvhf-w867
[34] Zero-Shot Embedding Drift Detection: A Lightweight Defense Against Prompt Injections in LLMs — http://arxiv.org/abs/2601.12359v1
[35] Security Threats in the Model Context Protocol: A Comprehensive Survey and Trust Boundary Mitigation Framework for Agentic AI Systems — https://doi.org/10.21275/sr26316110418
[36] Caging the Agents: A Zero Trust Security Architecture for Autonomous AI in Healthcare — http://arxiv.org/abs/2603.17419v1
[37] Internet Service Providers' and Individuals' Attitudes, Barriers, and Incentives to Secure IoT — http://arxiv.org/abs/2210.02137v1
[38] SoK: The Attack Surface of Agentic AI - Tools and Autonomy — https://doi.org/10.48550/arxiv.2603.22928
[39] SyzScope: Revealing High-Risk Security Impacts of Fuzzer-Exposed Bugs in Linux kernel — http://arxiv.org/abs/2111.06002v1
[40] Detecting Prompt Injection Attacks Against Application Using Classifiers — http://arxiv.org/abs/2512.12583v1
[41] Multi-Factor Key Derivation Function (MFKDF) for Fast, Flexible, Secure, & Practical Key Management — http://arxiv.org/abs/2208.05586v3
[42] LLMs Can Defend Themselves Against Jailbreaking in a Practical Manner: A Vision Paper — http://arxiv.org/abs/2402.15727v2
[43] Overview of the Sensemaking Task at the ELOQUENT 2025 Lab: LLMs as Teachers, Students and Evaluators — http://arxiv.org/abs/2507.12143v1
[44] Jailbreak Distillation: Renewable Safety Benchmarking — http://arxiv.org/abs/2505.22037v1
[45] Annif at SemEval-2025 Task 5: Traditional XMTC augmented by LLMs — http://arxiv.org/abs/2504.19675v2
[46] DARWIN: Evolving Jailbreak Adversary and Guardrail for LLM Safety Evaluation and Protection — http://arxiv.org/abs/2607.19829v2
[47] SoK: Evaluating Jailbreak Guardrails for Large Language Models — http://arxiv.org/abs/2506.10597v2
[48] TeleAI-Safety: A comprehensive LLM jailbreaking benchmark towards attacks, defenses, and evaluations — http://arxiv.org/abs/2512.05485v2
[49] Evaluating the Fork-Awareness of Coverage-Guided Fuzzers — http://arxiv.org/abs/2301.05060v1
[50] Same Coverage, Less Bloat: Accelerating Binary-only Fuzzing with Coverage-preserving Coverage-guided Tracing — http://arxiv.org/abs/2209.03441v1
[51] The 2nd MERCADO Workshop at IEEE VIS 2025: Multimodal Experiences for Remote Communication Around Data Online — http://arxiv.org/abs/2504.15859v1
[52] Improving the Security of the IEEE 802.15.6 Standard for Medical BANs — http://arxiv.org/abs/2201.06354v4
[53] FOX: Coverage-guided Fuzzing as Online Stochastic Control — http://arxiv.org/abs/2406.04517v1
[54] Network Hexagons Under Attack: Secure Crowdsourcing of Geo-Referenced Data — http://arxiv.org/abs/2506.05601v1
[55] cozy: Comparative Symbolic Execution for Binary Programs — http://arxiv.org/abs/2504.00151v1
[56] Symbolic Execution in Practice: A Survey of Applications in Vulnerability, Malware, Firmware, and Protocol Analysis — http://arxiv.org/abs/2508.06643v1
[57] An Exploratory Survey of Hybrid Testing Techniques Involving Symbolic Execution and Fuzzing — http://arxiv.org/abs/1712.06843v1
[58] Badger: Complexity Analysis with Fuzzing and Symbolic Execution — http://arxiv.org/abs/1806.03283v1
[59] Improving Function Coverage with Munch: A Hybrid Fuzzing and Directed Symbolic Execution Approach — http://arxiv.org/abs/1711.09362v2
[60] S$^2$F: Principled Hybrid Testing With Fuzzing, Symbolic Execution, and Sampling — http://arxiv.org/abs/2601.10068v1
[61] PathFuzzing: Worst Case Analysis by Fuzzing Symbolic-Execution Paths — http://arxiv.org/abs/2507.09892v1
[62] Overview of the 2024 ALTA Shared Task: Detect Automatic AI-Generated Sentences for Human-AI Hybrid Articles — http://arxiv.org/abs/2412.17848v1
[63] Multiple Targets Directed Greybox Fuzzing — http://arxiv.org/abs/2206.14977v1
[64] ODDFUZZ: Discovering Java Deserialization Vulnerabilities via Structure-Aware Directed Greybox Fuzzing — http://arxiv.org/abs/2304.04233v1
[65] $MC^2$: Rigorous and Efficient Directed Greybox Fuzzing — http://arxiv.org/abs/2208.14530v1
[66] Directed Greybox Fuzzing via Large Language Model — http://arxiv.org/abs/2505.03425v1
[67] The Progress, Challenges, and Perspectives of Directed Greybox Fuzzing — http://arxiv.org/abs/2005.11907v5
[68] Learning Inputs in Greybox Fuzzing — http://arxiv.org/abs/1807.07875v1
[69] Triggering and Detecting Exploitable Library Vulnerability from the Client by Directed Greybox Fuzzing — http://arxiv.org/abs/2604.04102v1
[70] Beyond Imprecise Distance Metrics: Trace-Guided Directed Greybox Fuzzing via LLM-Predicted Call Stacks — http://arxiv.org/abs/2510.23101v2
[71] This paper has been withdrawn — http://arxiv.org/abs/cond-mat/0309395v2
[72] Higher-order symbolic execution for contract verification and refutation — http://arxiv.org/abs/1507.04817v3
[73] SoK: Hardware Defenses Against Speculative Execution Attacks — http://arxiv.org/abs/2301.03724v1
[74] Can Large Language Models Simulate Symbolic Execution Output Like KLEE? — http://arxiv.org/abs/2511.08530v1
[75] Reviewing KLEE's Sonar-Search Strategy in Context of Greybox Fuzzing — http://arxiv.org/abs/1803.04881v1
[76] Obstructions to weak decomposability for simplicial polytopes — http://arxiv.org/abs/1206.6143v1
[77] Extracting a Micro State Transition Table Using the KLEE Symbolic Execution Engine — https://doi.org/10.1109/APSEC53868.2021.00072
[78] Directed Symbolic Execution for Vulnerability Discovery: An LLM-Guided Approach in KLEE — http://arxiv.org/abs/2607.21676v1
[79] Malware Analysis: A Perspective from Dynamic Symbolic Execution of Binary Code — https://doi.org/10.54654/isj.v2i25.1093
[80] IFSE: Taming Closed-Box Functions in Symbolic Execution via Fuzz Solving — https://doi.org/10.1109/ICSE-Companion66252.2025.00019
[81] Compatible Branch Coverage Driven Symbolic Execution for Efficient Bug Finding — https://doi.org/10.1145/3656443
[82] Full-speed Fuzzing: Reducing Fuzzing Overhead through Coverage-guided Tracing — http://arxiv.org/abs/1812.11875v2
[83] KDAlloc: The KLEE Deterministic Allocator: Deterministic Memory Allocation during Symbolic Execution and Test Case Replay — https://doi.org/10.1145/3597926.3604921
[84] Concrete Constraint Guided Symbolic Execution — https://doi.org/10.1145/3597503.3639078
[85] Symbolic Execution with Test Cases Generated by Large Language Models — https://doi.org/10.1109/QRS62785.2024.00031
[86] Industry Practice of Coverage-Guided Enterprise-Level DBMS Fuzzing — http://arxiv.org/abs/2103.00804v1
[87] Multi-Pass Targeted Dynamic Symbolic Execution — https://arxiv.org/abs/2408.07797
[88] $μ$AFL: Non-intrusive Feedback-driven Fuzzing for Microcontroller Firmware — http://arxiv.org/abs/2202.03013v3
[89] CovRL: Fuzzing JavaScript Engines with Coverage-Guided Reinforcement Learning for LLM-based Mutation — http://arxiv.org/abs/2402.12222v1
[90] Rust for Secure Backend Development: A Critical Review and Extended Vulnerability Comparison with Node.js and Django — http://arxiv.org/abs/2608.22624v1
[91] A new spin on quantum cryptography: Avoiding trapdoors and embracing public keys — http://arxiv.org/abs/1109.3235v1
[92] Mobile Energy Requirements of the Upcoming NIST Post-Quantum Cryptography Standards — http://arxiv.org/abs/1912.00916v4
[93] Can Coding Agents Migrate to Post-Quantum Cryptography? — http://arxiv.org/abs/2512.12989v3
[94] Quantum-Ready Secure WAN: A Risk Assessment and Migration Framework — http://arxiv.org/abs/2609.26225v1
[95] NIST Post-Quantum Cryptography Standard Algorithms Based on Quantum Random Number Generators — http://arxiv.org/abs/2507.21151v1
[96] A Survey of Post-Quantum Cryptography Support in Cryptographic Libraries — http://arxiv.org/abs/2508.16078v1
[97] Towards post-quantum blockchain: A review on blockchain cryptography resistant to quantum computing attacks — http://arxiv.org/abs/2402.00922v1
[98] QRSec 2025: ACM CCS First Workshop on Quantum-Resistant Cryptography and Security — https://doi.org/10.1145/3719027.3767669
[99] Identifying Research Challenges in Post Quantum Cryptography Migration and Cryptographic Agility — http://arxiv.org/abs/1909.07353v1
[100] Post-Quantum Cryptography: A Systematic Review of Algorithms, Standardization, Challenges, and Future Research Directions — https://doi.org/10.2139/ssrn.7128678
[101] Lattice-based cryptography and post-quantum security: Algebraic number theory in the design of quantum-resistant cryptographic schemes — https://doi.org/10.33545/26648636.2026.v8.i2a.256
[102] Signature Placement in Post-Quantum TLS Certificate Hierarchies: An Experimental Study of ML-DSA and SLH-DSA in TLS 1.3 Authentication — http://arxiv.org/abs/2604.06100v3
[103] Layered Performance Analysis of TLS 1.3 Handshakes: Classical, Hybrid, and Pure Post-Quantum Key Exchange — http://arxiv.org/abs/2603.11006v2
[104] Measurement Study of Post-Quantum Readiness of Internet: 2026 — http://arxiv.org/abs/2606.16473v1
[105] The Role of Cryptography in Network Security: A Systematic Review and Emerging Trends — https://doi.org/10.5281/zenodo.20084740
[106] OpenSSLNTRU: Faster post-quantum TLS key exchange — http://arxiv.org/abs/2106.08759v3
[107] The Role of Cryptography in Network Security: A Systematic Review and Emerging Trends — https://doi.org/10.5281/zenodo.20084741
[108] Exploration of Evolving Quantum Key Distribution Network Architecture Using Model-Based Systems Engineering — http://arxiv.org/abs/2508.15733v1
[109] Quantum Computing and Its Implications for Information Technology Security — https://doi.org/10.64388/irev10i1-1720192
[110] Mind the Gap: Policy vs Reality in Post-Quantum TLS Deployment — http://arxiv.org/abs/2607.29005v1
[111] What Twelve LLM Agent Benchmark Papers Disclose About Themselves: A Pilot Audit and an Open Scoring Schema — http://arxiv.org/abs/2605.21404v1
[112] LLM-SRBench: A New Benchmark for Scientific Equation Discovery with Large Language Models — http://arxiv.org/abs/2504.10415v2
[113] CyberGym: Evaluating AI Agents' Real-World Cybersecurity Capabilities at Scale — http://arxiv.org/abs/2506.02548v3
[114] Efficient Benchmarking in Production: A Study of an Evolving LLM Agent — http://arxiv.org/abs/2609.21267v1
[115] Focus Agent: LLM-Powered Virtual Focus Group — http://arxiv.org/abs/2409.01907v1
[116] Overview of SCIDOCA 2025 Shared Task on Citation Prediction, Discovery, and Placement — http://arxiv.org/abs/2509.24283v1
[117] The Impact of Magma: A Ground-Truth Fuzzing Benchmark — http://arxiv.org/abs/2608.28016v1
[118] Magma: A Ground-Truth Fuzzing Benchmark — http://arxiv.org/abs/2009.01120v2
[119] A Human-Grounded Evaluation Benchmark for Local Explanations of Machine Learning — http://arxiv.org/abs/1801.05075v2
[120] Building Flexible, Low-Cost Wireless Access Networks With Magma — http://arxiv.org/abs/2209.10001v1
[121] Unitary magma actions — http://arxiv.org/abs/2408.08721v1
[122] Arithmetic and $k$-maximality of the cyclic free magma — http://arxiv.org/abs/2407.17692v1
[123] Protocol-Aware Firmware Rehosting for Effective Fuzzing of Embedded Network Stacks — http://arxiv.org/abs/2509.13740v1
[124] SECQUE: A Benchmark for Evaluating Real-World Financial Analysis Capabilities — http://arxiv.org/abs/2504.04596v1
[125] Automatic and Universal Prompt Injection Attacks against Large Language Models — http://arxiv.org/abs/2403.04957v1
[126] AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents — http://arxiv.org/abs/2406.13352v3
[127] NTU-NPU System for Voice Privacy 2024 Challenge — http://arxiv.org/abs/2410.02371v1


---

*Generated by research-bot · topic=`cybersecurity` · depth=`standard` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading · model=`deepseek-v4-flash` · sources=127 · duration=318s · 2026-10-04T03:04:27+00:00*
