# AgentGuard: LLM 护栏与 Agent 安全深度调研报告

> 本报告在 LLM 不可用时由检索结果自动生成（降级模式），结论需人工复核。

## 摘要
系统梳理大模型 Agent 安全护栏的前沿进展、经典奠基工作、开源工程实践、评测基准与开放争议，为具身智能场景下的 Agent 安全架构选型提供证据支撑。

## 最近 1-2 年（2024-2026）Agent 护栏与 LLM 防火墙的前沿架构演进与关键技术突破有哪些？

## 直接/间接提示注入、越狱与工具调用滥用的最新攻击面与防御机制（含分类器、宪法护栏、上下文隔离）有哪些实证进展？
- Second MOASEI Competition at AAMAS'2026: A Technical Report [7]
- AutoRestTest at the SBFT 2026 Tool Competition [5]
- Will the User Ever Know? Covert Indirect Prompt Injection Attacks on Tool-Using LLM Agents [50]
- Beyond Instruction Override: Benchmarking Indirect Prompt Injection with Task-Tampering Attacks [51]
- IPIGuard: A Novel Tool Dependency Graph-Based Defense Against Indirect Prompt Injection in LLM Agents [52]
- The Framing Gap: Indirect Prompt-Injection Exfiltration Defeats Surface-Level Defenses in Tool-Using Agents [54]

## 主流开源护栏框架与沙箱/最小权限工程实践的成熟度、延迟特性、集成复杂度与生产案例如何？
- 现有学术工作主要集中在护栏的基准测试与脆弱性分析，而非主流开源护栏框架的工程成熟度、延迟、集成复杂度或生产落地案例 [10] [86] [87] [88] [92] [93]
- CS-Guard 为代码生成场景建立了首个护栏系统基准，覆盖 9 个护栏 × 7 个 LLM，揭示越狱后攻击成功率约 50% [86]
- 基于意图检测的内容审核护栏在意图操纵下存在脆弱性，提出两阶段 IntentPrompt 框架可提升鲁棒性 [87]
- 控制论视角重新定义护栏：从拒绝转向恢复，将安全建模为序贯决策问题 [88]
- 护栏有效性评估方法论空白：现有方法多基于标签分类，缺乏与专家期望对齐的系统性评估框架 [92]
- 医疗诊断场景下的 LLM 护栏系统 Med-Guard 已在会议发表，属少数有具体应用场景的护栏工作 [93]

## Agent 安全评测基准与红队框架的覆盖维度、任务多样性、评测指标与当前 SOTA 结果有哪些？
- Agentic-level red teaming reveals vulnerabilities not captured by model-level red teaming alone [70]
- EvalSafetyGap survey identifies shared measurement problem in LLM evaluation and safety: benchmark scores can improve while actual capabilities/alignment remain uncertain [74]
- Sola-Visibility-ISPM proposes first standardized benchmark for agentic AI in Identity Security Posture Management (ISPM) visibility [80]
- MOASEI 2026 competition benchmarks multi-agent decision-making under open-system conditions with expanded reporting metrics [7]

## 合规基线（OWASP LLM Top 10 / Agentic AI、NIST AI RMF、MITRE ATLAS）与人在回路审批机制在工程落地中的映射关系与实施难点？
- Incident-Data Robustness Analysis of the OWASP Top 10 for LLM Applications (2026): How a Community-Expert Ranking Holds Up Against a Large-Scale LLM Incident Corpus [27]
- When the Agent Is the Adversary: Architectural Requirements for Agentic AI Containment After the April 2026 Frontier Model Escape [28]
- Towards trustworthy agentic AI: a comprehensive survey of safety, robustness, privacy, and system security [29]
- Mitigating the OWASP Top 10 For Large Language Models Applications using Intelligent Agents [30]
- Security, privacy, and agentic AI in a regulatory view: From definitions and distinctions to provisions and reflections [31]
- LLM-INSTRUCT at UZH Shared Task 2026: Constraint-Aware Retrieval and Selective Debate for Paragraph-Level Argument Mining [2]

## 当前 Agent 安全领域的核心开放问题、争议焦点（如过度代理定义、数据外泄量化、自适应攻击鲁棒性）及研究空白有哪些？
- Second MOASEI Competition at AAMAS'2026: A Technical Report [7]
- VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results [8]
- Measuring Google AI Overviews: Activation, Source Quality, Claim Fidelity, and Publisher Impact [102]
- Network Hexagons Under Attack: Secure Crowdsourcing of Geo-Referenced Data [103]
- Tracing MCP Security Vulnerabilities: Constructing and Analyzing an MCP Security Vulnerability Dataset [105]
- Your LLM Agent Can Leak Your Data: Data Exfiltration via Backdoored Tool Use [110]

## 参考来源
[1] Firewalls to Secure Dynamic LLM Agentic Networks — http://arxiv.org/abs/2502.01822v7
[2] LLM-INSTRUCT at UZH Shared Task 2026: Constraint-Aware Retrieval and Selective Debate for Paragraph-Level Argument Mining — http://arxiv.org/abs/2607.20430v1
[3] TTLab at Daleel 2026: STAR-Ar, Sequence Tagging for Argument Recognition in Arabic — http://arxiv.org/abs/2609.39385v1
[4] Refined CMA-ES for CEC 2026 Bound-Constrained Single-Objective Optimization — http://arxiv.org/abs/2611.04620v1
[5] AutoRestTest at the SBFT 2026 Tool Competition — http://arxiv.org/abs/2607.01063v1
[6] UIC-AIHealth4All at ArchEHR-QA 2026: Answer-First Evidence Grounding for Clinical Question Answering — http://arxiv.org/abs/2608.27467v1
[7] Second MOASEI Competition at AAMAS'2026: A Technical Report — http://arxiv.org/abs/2607.03399v1
[8] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1
[9] A Scalable VLSI Architecture for Soft-Input Soft-Output Depth-First Sphere Decoding — http://arxiv.org/abs/0910.3427v4
[10] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1
[11] NTU-NPU System for Voice Privacy 2024 Challenge — http://arxiv.org/abs/2410.02371v1
[12] A Methodology for Selecting and Composing Runtime Architecture Patterns for Production LLM Agents — http://arxiv.org/abs/2605.20173v2
[13] Policy-as-Prompt: Turning AI Governance Rules into Guardrails for AI Agents — http://arxiv.org/abs/2509.23994v2
[14] Discovery Opportunities with Gravitational Waves -- TASI 2024 Lecture Notes — http://arxiv.org/abs/2409.08956v1
[15] Atmospheric entry and fragmentation of small asteroid 2024 BX1: Bolide trajectory, orbit, dynamics, light curve, and spectrum — http://arxiv.org/abs/2403.00634v2
[16] An agent-based intelligent environmental monitoring system — http://arxiv.org/abs/cs/0407024v1
[17] Tactical Edge IoT in Defense and National Security — http://arxiv.org/abs/2411.00511v1
[18] ControlNET: A Firewall for RAG-based LLM System — http://arxiv.org/abs/2504.09593v2
[19] Internet Service Providers' and Individuals' Attitudes, Barriers, and Incentives to Secure IoT — http://arxiv.org/abs/2210.02137v1
[20] SyzScope: Revealing High-Risk Security Impacts of Fuzzer-Exposed Bugs in Linux kernel — http://arxiv.org/abs/2111.06002v1
[21] CoVault: Secure, Scalable Analytics of Personal Data — http://arxiv.org/abs/2208.03784v4
[22] Multi-Factor Key Derivation Function (MFKDF) for Fast, Flexible, Secure, & Practical Key Management — http://arxiv.org/abs/2208.05586v3
[23] GuardRails-as-Code and Audit Economics: Reducing Compliance Costs Through Policy Automation — https://doi.org/10.70924/uv4px7jt//qfh0iaoc
[24] An Empirical Case Study of Prompt Engineering Strategies for Bypassing Multi-Layer Agent Security Defenses — http://arxiv.org/abs/2610.14116v1
[25] "ATX-1 v2.3: AEGIS Threat Matrix for Agentic AI Systems" — https://doi.org/10.21227/jr43-0571
[26] "ATX-1 v2.4: AEGIS Threat Matrix for Agentic AI Systems" — https://doi.org/10.21227/edxj-ka42
[27] Incident-Data Robustness Analysis of the OWASP Top 10 for LLM Applications (2026): How a Community-Expert Ranking Holds Up Against a Large-Scale LLM Incident Corpus — http://arxiv.org/abs/2608.19266v1
[28] When the Agent Is the Adversary: Architectural Requirements for Agentic AI Containment After the April 2026 Frontier Model Escape — http://arxiv.org/abs/2604.23425v1
[29] Towards trustworthy agentic AI: a comprehensive survey of safety, robustness, privacy, and system security — http://arxiv.org/abs/2605.23989v1
[30] Mitigating the OWASP Top 10 For Large Language Models Applications using Intelligent Agents — http://arxiv.org/abs/2601.18105v1
[31] Security, privacy, and agentic AI in a regulatory view: From definitions and distinctions to provisions and reflections — http://arxiv.org/abs/2603.18914v1
[32] POLARIS: Typed Planning and Governed Execution for Agentic AI in Back-Office Automation — http://arxiv.org/abs/2601.11816v1
[33] mdok of KInIT: Robustly Fine-tuned LLM for Binary and Multiclass AI-Generated Text Detection — http://arxiv.org/abs/2506.01702v2
[34] Security Threats in the Model Context Protocol: A Comprehensive Survey and Trust Boundary Mitigation Framework for Agentic AI Systems — https://doi.org/10.21275/sr26316110418
[35] Governed Agentic RAG: Reference Architecture — https://doi.org/10.5281/zenodo.22727448
[36] Actionable Guidance for High-Consequence AI Risk Management: Towards Standards Addressing AI Catastrophic Risks — http://arxiv.org/abs/2206.08966v3
[37] SCITUS: A Multi-Jurisdictional Framework for Adapting NIST AI RMF to the Canadian Regulatory Context — http://arxiv.org/abs/2607.15051v1
[38] AAGATE: A NIST AI RMF-Aligned Governance Platform for Agentic AI — http://arxiv.org/abs/2510.25863v2
[39] Mapping Human Anti-collusion Mechanisms to Multi-agent AI Systems — http://arxiv.org/abs/2601.00360v3
[40] AI Ethics by Design: Implementing Customizable Guardrails for Responsible AI Development — http://arxiv.org/abs/2411.14442v2
[41] AI Exposure and the Changing Responsibilities in Job Postings — http://arxiv.org/abs/2611.09870v1
[42] Faith in AI can narrow the futures individuals consider — http://arxiv.org/abs/2603.28944v2
[43] Performance of pile-up mitigation techniques for jets in $pp$ collisions at $\sqrt{s} = 8$ TeV using the ATLAS detector — http://arxiv.org/abs/1510.03823v2
[44] A continuous calibration of the ATLAS flavour-tagging classifiers via optimal transportation maps — http://arxiv.org/abs/2505.13063v2
[45] Measurement of the azimuthal anisotropy of charged particles in $\sqrt{s_{\mathrm{NN}}}=5.36$ TeV $^{16}$O$+^{16}$O and $^{20}$Ne$+^{20}$Ne collisions with the ATLAS detector — http://arxiv.org/abs/2509.05171v2
[46] New techniques for jet calibration with the ATLAS detector — http://arxiv.org/abs/2303.17312v2
[47] SecAlign: Defending Against Prompt Injection with Preference Optimization — http://arxiv.org/abs/2410.05451v3
[48] WebInject: Prompt Injection Attack to Web Agents — http://arxiv.org/abs/2505.11717v4
[49] MELON: Provable Defense Against Indirect Prompt Injection Attacks in AI Agents — http://arxiv.org/abs/2502.05174v4
[50] Will the User Ever Know? Covert Indirect Prompt Injection Attacks on Tool-Using LLM Agents — http://arxiv.org/abs/2608.30362v3
[51] Beyond Instruction Override: Benchmarking Indirect Prompt Injection with Task-Tampering Attacks — http://arxiv.org/abs/2611.07640v1
[52] IPIGuard: A Novel Tool Dependency Graph-Based Defense Against Indirect Prompt Injection in LLM Agents — http://arxiv.org/abs/2508.15310v1
[53] Automatic and Universal Prompt Injection Attacks against Large Language Models — http://arxiv.org/abs/2403.04957v1
[54] The Framing Gap: Indirect Prompt-Injection Exfiltration Defeats Surface-Level Defenses in Tool-Using Agents — http://arxiv.org/abs/2608.27092v1
[55] Capability-Mediated Perimeters for Secure AI Agent Tool Execution: Conditional Non-Escalation Invariants and Empirical Evaluation Against Indirect Prompt Injection — https://doi.org/10.2139/ssrn.7505299
[56] Capability-Mediated  Perimeters for Secure AI Agent Tool Execution: Conditional  Non-Escalation Invariants and Empirical Evaluation Against Indirect  Prompt Injection — https://doi.org/10.21203/rs.3.rs-10889863/v1
[57] Constitutional Classifiers++: Efficient Production-Grade Defenses against Universal Jailbreaks — http://arxiv.org/abs/2601.04603v1
[58] Residual Privacy Leakage after Output Scrubbing in Tool-Using LLM Agents under Indirect Prompt Injection — https://doi.org/10.21203/rs.3.rs-11428254/v1
[59] LLMs Can Defend Themselves Against Jailbreaking in a Practical Manner: A Vision Paper — http://arxiv.org/abs/2402.15727v2
[60] Ariadne: Adaptive, Human-in-the-Loop Defense for AI Agents against Indirect Prompt Injection — https://doi.org/10.2139/ssrn.6870178
[61] GraphShield: A Graph-Structured Defense Framework for Prompt Injection in RAG and Multi-Agent LLM Systems — https://doi.org/10.2139/ssrn.7082874
[62] Evaluating Indirect Prompt Injection Defenses in Tool-Using LLM Agents: Security, Utility, and Replication — https://doi.org/10.3390/computers15090570
[63] MAMORI: A Cross-Lingual Benchmark for Indirect Prompt Injection in Tool-Using LLM Agents — https://doi.org/10.1109/idap71869.2026.11727885
[64] Attenuation, Not Amplification: Measuring Indirect Prompt Injection Propagation and Containment in Multi-Agent LLM Delegation Chains — https://doi.org/10.21203/rs.3.rs-11162232/v1
[65] Overview of the Sensemaking Task at the ELOQUENT 2025 Lab: LLMs as Teachers, Students and Evaluators — http://arxiv.org/abs/2507.12143v1
[66] VoxENES 2026: Benchmarking Generalization of Speech Spoofing Detectors Against LLM-Era TTS and Voice Conversion — http://arxiv.org/abs/2607.11706v1
[67] ICASSP 2026 Radar Acoustic Speech Enhancement (RASE) Challenge — http://arxiv.org/abs/2610.32202v1
[68] The ICASSP 2026 Automatic Song Aesthetics Evaluation Challenge — http://arxiv.org/abs/2601.07237v1
[69] Overview of BioASQ 2026: The fourteenth BioASQ Challenge on Large-Scale Biomedical Semantic Indexing and Question Answering — http://arxiv.org/abs/2609.39975v1
[70] Mind the Gap: Comparing Model- vs Agentic-Level Red Teaming with Action-Graph Observability on GPT-OSS-20B — http://arxiv.org/abs/2509.17259v1
[71] Red Teaming for Large Language Models At Scale: Tackling Hallucinations on Mathematics Tasks — http://arxiv.org/abs/2401.00290v1
[72] Learning diverse attacks on large language models for robust red-teaming and safety tuning — http://arxiv.org/abs/2405.18540v3
[73] Evaluation Agent: Efficient and Promptable Evaluation Framework for Visual Generative Models — http://arxiv.org/abs/2412.09645v3
[74] EvalSafetyGap: A Hybrid Survey and Conceptual Framework for LLM Evaluation-Safety Failures — http://arxiv.org/abs/2606.30219v5
[75] LongEval at CLEF 2025: Longitudinal Evaluation of IR Model Performance — http://arxiv.org/abs/2503.08541v1
[76] Safety, Hallucination, and Failure Modes in Agentic Health AI: A State-of-the-Art Review — https://doi.org/10.20944/preprints202604.1409.v1
[77] Multi-Agent Orchestration: Coordination, Trust, and Cascading Failures — https://doi.org/10.2139/ssrn.6734798
[78] Agentic AI Systems: Architectures, Autonomy, and Emergent Behaviours — https://doi.org/10.2139/ssrn.6702761
[79] Quantifying the Irreducible: A Systematic Survey of Adversarial Jailbreak Vectors, Red Team Methodologies, and Enterprise Threat Exposure in Large Language Model Deployments — https://doi.org/10.2139/ssrn.6475399
[80] Sola-Visibility-ISPM: Benchmarking Agentic AI for Identity Security Posture Management Visibility — http://arxiv.org/abs/2601.07880v1
[81] Beyond Sovereign AI: A Unified Framework for National AI Governance and Constraint-Aligned Intelligence Systems Integrating Australia's National AI Plan (2025) with the CollectiveOS Architecture — https://doi.org/10.5281/zenodo.17791470
[82] Towards a Formal Verification of Secure Vehicle Software Updates — http://arxiv.org/abs/2511.15479v1
[83] The Current State and Future Trends of Automotive AI Safety Governance — https://doi.org/10.5281/zenodo.21752296
[84] NeMo Guardrails: A Toolkit for Controllable and Safe LLM Applications with Programmable Rails — http://arxiv.org/abs/2310.10501v1
[85] Status Report on the double-βdecay experiment NEMO-3 — http://arxiv.org/abs/hep-ex/0006031v1
[86] CS-Guard: Benchmarking LLM Guardrails for Code Generation Security — http://arxiv.org/abs/2609.09798v1
[87] Exploring the Vulnerability of the Content Moderation Guardrail in Large Language Models via Intent Manipulation — http://arxiv.org/abs/2505.18556v2
[88] From Refusal to Recovery: A Control-Theoretic Approach to Generative AI Guardrails — http://arxiv.org/abs/2510.13727v2
[89] No Free Lunch with Guardrails — http://arxiv.org/abs/2504.00441v2
[90] Sensitivity and pointing accuracy of the NEMO km$^3$ telescope — http://arxiv.org/abs/astro-ph/0605067v1
[91] SoK: Hardware Defenses Against Speculative Execution Attacks — http://arxiv.org/abs/2301.03724v1
[92] "Do Your Guardrails Even Guard?'' Method for Evaluating Effectiveness of Moderation Guardrails in Aligning LLM Outputs with Expert User Expectations — https://doi.org/10.1609/aies.v8i1.36583
[93] Med-Guard: LLM-Based Diagnostic System with Safety Guardrails — https://doi.org/10.1109/aimlsystems67835.2025.11331206
[94] SandBlaster: Reversing the Apple Sandbox — http://arxiv.org/abs/1608.04303v1
[95] AI Guardrails - Spotting &amp;amp; Fixing Common LLM Failure Modes — https://doi.org/10.2139/ssrn.5401993
[96] ICAGC 2024: Inspirational and Convincing Audio Generation Challenge 2024 — http://arxiv.org/abs/2407.12038v2
[97] NEMO GUARDRAILS FOR SAFE AND SECURE INSURANCE AI — https://doi.org/10.5121/ijci.2025.140510
[98] Red-Teaming Medical AI: Systematic Adversarial Evaluation of LLM Safety Guardrails in Clinical Contexts — https://doi.org/10.64898/2026.02.26.26347212
[99] Safety Guardrails for LLM-Enabled Robots_supp1-3667488.mp4 — https://doi.org/10.1109/lra.2026.3667488/mm1
[100] An integrated framework for ethical healthcare chatbots using LangChain and NeMo guardrails — https://doi.org/10.1007/s43681-025-00696-7
[101] Knowledge Graph as Guardrails: Achieving Conceptually Sound LLM Complaint Classification Without Fine-Tuning — https://doi.org/10.2139/ssrn.5258401
[102] Measuring Google AI Overviews: Activation, Source Quality, Claim Fidelity, and Publisher Impact — http://arxiv.org/abs/2605.14021v2
[103] Network Hexagons Under Attack: Secure Crowdsourcing of Geo-Referenced Data — http://arxiv.org/abs/2506.05601v1
[104] When Security Meets Usability: An Empirical Investigation of Post-Quantum Cryptography APIs — http://arxiv.org/abs/2602.14539v1
[105] Tracing MCP Security Vulnerabilities: Constructing and Analyzing an MCP Security Vulnerability Dataset — http://arxiv.org/abs/2611.11104v1
[106] Data Encoding for Byzantine-Resilient Distributed Optimization — http://arxiv.org/abs/1907.02664v2
[107] Byzantine-Resilient SGD in High Dimensions on Heterogeneous Data — http://arxiv.org/abs/2005.07866v1
[108] Constraints on dark energy from H II starburst galaxy apparent magnitude versus redshift data — http://arxiv.org/abs/1110.5626v1
[109] Annif at SemEval-2025 Task 5: Traditional XMTC augmented by LLMs — http://arxiv.org/abs/2504.19675v2
[110] Your LLM Agent Can Leak Your Data: Data Exfiltration via Backdoored Tool Use — http://arxiv.org/abs/2604.05432v1
[111] TerraGen: A Unified Multi-Task Layout Generation Framework for Remote Sensing Data Augmentation — http://arxiv.org/abs/2510.21391v1
[112] Focus Agent: LLM-Powered Virtual Focus Group — http://arxiv.org/abs/2409.01907v1
[113] UniGuardian: A Unified Defense for Detecting Prompt Injection, Backdoor Attacks and Adversarial Attacks in Large Language Models — http://arxiv.org/abs/2502.13141v2
[114] DeRAG: Black-box Adversarial Attacks on Multiple Retrieval-Augmented Generation Applications via Prompt Injection — http://arxiv.org/abs/2507.15042v1
[115] Backdoor-Powered Prompt Injection Attacks Nullify Defense Methods — http://arxiv.org/abs/2510.03705v1
[116] Adaptive Attacks Break Defenses Against Indirect Prompt Injection Attacks on LLM Agents — http://arxiv.org/abs/2503.00061v2

---

*Generated by research-bot · topic=`agentguard` · depth=`standard` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading · model=`nvidia/nemotron-3-ultra-550b-a55b` · sources=116 · duration=1418s · 2026-11-12T11:34:27+00:00*
