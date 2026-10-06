# 网络安全攻防前沿调研报告（2024–2026）

> **元信息**
> - 报告日期：2026-10-06（UTC）
> - 领域：Cybersecurity（网络安全）——漏洞与利用、模糊测试与程序分析、供应链与 SBOM、恶意软件、密码学工程、LLM/Agent 安全
> - 检索源数量：候选来源 122 条（引用编号 [1]–[122]），另含 11 条领域种子资源（OWASP / CWE / AFL++ / angr 等）
> - 证据分级：A（同行评审）/ B（arXiv 预印本、官方仓库）/ C（第三方复现、榜单）/ D（社区帖）；本批次以 B 级为主，A 级标注有限
> - 免责：本报告严格只引用给定编号来源；凡候选块未提供引用数、star、榜单排名者，一律标注 `> 待核实`，不做数字推测。

---

## 摘要（Executive Summary）

- **LLM/Agent 安全已成为网络安全中增长最快、但方法论最不稳定的子领域。** 攻击侧从"直接提示注入"走向"间接提示注入（IPI）+ 工具调用" [39][89][94][97]，防御侧从"输入过滤"走向"结构化查询 [44]、偏好优化 [40]、工具依赖图 [101]、多智能体流水线 [92]"。但**防御评估范式本身正被质疑**：以静态攻击串或弱优化方法评估的防御，可被针对该防御定制的自适应攻击绕过 [58]，护栏系统（含 Azure Prompt Shield、Meta Prompt Guard）在实验中被字符注入与 AML 逃逸方法规避 [56]。

- **漏洞发现侧的核心矛盾仍是"路径爆炸 vs 覆盖率"。** 符号执行综述将应对策略归纳为 Scope Reduction 与 Guidance Heuristics 两条路线 [13]；定向灰盒模糊测试（DGF）与动态符号执行的混合方案成为主流工程形态 [14]，最新工作 S²F 指出 SOTA 混合工具存在"符号执行过度剪枝"与"采样未作用于合适分支"两个结构性缺陷 [17]。

- **供应链安全从"组件清单"走向"攻击链图分析"与"密码学溯源"。** SBOM 落地研究显示，SPDX 与 CycloneDX 的工具生态是当前讨论焦点 [60]，但**尚无候选证据证明 SBOM 采用直接降低安全事件**；新方向包括从 SBOM 图预测多漏洞攻击链 [114]、用密码学注册表溯源结构性防御依赖混淆 [115]。

- **模糊测试与二进制分析的"可复现性危机""基准污染"在本批次候选中证据缺口明显** `> 待核实`（见第七章）。该缺口本身是本次调研最重要的方法论发现之一。

- **后量子密码（PQC）迁移出现"AI 辅助迁移"这一新议题**：编码智能体（coding agents）被用于 PQC 代码迁移评估 [67]，量子就绪 WAN 的风险评估与迁移框架亦被提出 [68]；经典侧有 MFKDF 密钥管理 [7]。

- **值得警惕的三个结构性风险**：① 基础模型透明度从 2024 年 58/100 降至 2025 年 40/100 [50]；② LLM Agent 安全基准的披露质量参差，已有研究对 12 篇基准论文做审计并提出开放评分 schema [78]；③ 相同 ASR（攻击成功率）在不同实验设置下可能对应不同安全保证 [77]。

---

## 一、关键前沿进展（近 1–2 年）

> 本节按时间线梳理 2024–2026 的关键节点，并标注证据强度。所有条目均给 [n]；未提供的热度/榜单条目写 `> 待核实`。

| 时间 | 进展 | 子领域 | 证据强度 | 来源 |
|---|---|---|---|---|
| 2024 | JailbreakBench：开源越狱鲁棒性基准发布 | LLM 安全基准 | arXiv 预印本（候选块未标同行评审） | [41] |
| 2024 | StruQ：用结构化查询防御提示注入 | LLM 防御 | arXiv 预印本 | [44] |
| 2024 | SecAlign：用偏好优化防御提示注入 | LLM 防御 | arXiv 预印本 | [40] |
| 2024 | AgentDojo：评估 LLM Agent 提示注入攻防的动态环境 | Agent 基准 | arXiv 预印本 | [80] |
| 2024-03 | 自动且通用的提示注入攻击 | 攻击方法 | arXiv 预印本 | [39] |
| 2025 | WebInject：面向 Web Agent 的多模态提示注入攻击 | Agent 攻击 | arXiv 预印本（cs.LG） | [89] |
| 2025 | 绕过 LLM 护栏：对六大护栏系统的逃逸实证 | 防御评估 | arXiv 预印本（cs.CR） | [56] |
| 2025 | 针对 IPI 的自适应攻击（Adaptive Attacks Break Defenses） | 防御评估 | arXiv 预印本 | [54] |
| 2025-10 | The Attacker Moves Second：自适应攻击绕过越狱/提示注入防御 | 方法论批判 | arXiv 预印本（cs.LG） | [58] |
| 2025 | SoK：越狱护栏的系统化评测 | 综述/评测 | arXiv 预印本（cs.CR） | [105] |
| 2025 | MELON：可证明的 IPI 防御 | Agent 防御 | arXiv 预印本 | [90] |
| 2025 | UniGuardian：统一检测提示注入 / 后门 / 对抗攻击 | LLM 防御 | arXiv 预印本 | [91] |
| 2025 | 混合定向模糊测试（Sydr-Fuzz 实现） | 模糊测试 | arXiv 预印本（cs.CR），v2 2026-01 | [14] |
| 2025 | 符号执行实践综述（漏洞/恶意软件/固件/协议） | 程序分析 | arXiv 预印本（cs.CR） | [13] |
| 2025 | VulBinLLM：LLM 检测剥离二进制漏洞 | LLM+二进制 | arXiv 预印本（cs.CR） | [20] |
| 2025 | 2025 基础模型透明度指数（第三版） | 治理 | arXiv 预印本（cs.AI） | [50] |
| 2025 | SBOM 工具生态比较（SPDX vs CycloneDX） | 供应链 | arXiv 预印本（cs.SE） | [60] |
| 2026 | S²F：fuzzing + 符号执行 + 采样统一混合测试架构 | 混合测试 | arXiv 预印本（cs.SE） | [17] |
| 2026 | KLEE 中的 LLM 引导定向符号执行 | 程序分析 | arXiv 预印本（cs.SE） | [38] |
| 2026 | SoK：DARPA AI Cyber Challenge（AIxCC）设计、架构与经验 | 竞赛/SoK | arXiv 预印本（cs.CR） | [87] |
| 2026 | OSS-CRS：把 AIxCC 网络推理系统释放到开源安全场景 | 竞赛/工程 | arXiv 预印本（cs.CR） | [88] |
| 2026 | NetInjectBench：网络运维工具的 IPI 基准（130 场景） | Agent 基准 | arXiv 预印本（cs.CR） | [99] |
| 2026 | SoK：交易智能体的鲁棒性与安全失效 | Agent 安全 SoK | arXiv 预印本（cs.CR） | [74] |
| 2026 | 自适应对手：多轮多 LLM 的 Agent 安全基准 | Agent 基准 | arXiv 预印本 | [79] |
| 2026 | Injection-Execution Dissociation：有状态 Agent 持久记忆攻击 | Agent 攻击 | arXiv 预印本 | [57] |
| 2026 | 密码学注册表溯源：结构性防御依赖混淆 | 供应链 | arXiv 预印本（cs.CR） | [115] |
| 2026 | 从 SBOM 图预测多漏洞攻击链 | 供应链 | arXiv 预印本（cs.SE） | [114] |
| 2026 | 编码智能体能否迁移到后量子密码（PQC）？ | PQC 工程 | arXiv 预印本 | [67] |
| 2026 | 量子就绪安全 WAN：风险评估与迁移框架 | PQC 工程 | arXiv 预印本 | [68] |

**热度证据**：上表所有条目在候选块中**均未提供引用数、GitHub star 或榜单排名** `> 待核实`；仅有 [70][73] 等非安全域挑战赛给出参与队伍数，不可用于本表。
**权威证据**：全部为 arXiv 预印本（含 cs.CR / cs.LG / cs.SE / cs.AI），候选块未显示同行评审 venue；[74][87] 标注为 SoK 体裁。
**关注度**：中——依据是这些条目集中于 2025–2026，且覆盖 agent 安全、模糊测试、供应链三条主线；但候选块缺少引用/讨论等外部热度信号。
**推荐度**：★★★☆☆–★★★★☆，取用前需核实正式发表状态。

---

## 二、Web / 系统 / 供应链攻防

### 2.1 Web 与 LLM 应用风险基线（经典/标准）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| OWASP Top 10（Web & LLM Applications） | 2021/2025 | OWASP | `> 待核实` | A（行业标准，官方维护） | 高（业界事实基线） | ★★★★★ | https://owasp.org/www-project-top-ten/ | Web 与 LLM 应用风险基线清单 |
| CWE（Common Weakness Enumeration） | ongoing | MITRE | `> 待核实` | A（官方标准） | 高 | ★★★★★ | https://cwe.mitre.org/ | 弱点分类标准 |

> 注：OWASP/CWE 属种子资源，其 star/引用数候选块未提供 `> 待核实`；作为标准其权威性不依赖热度。

### 2.2 软件供应链安全进展

- **SBOM 落地现状**：对 SPDX 与 CycloneDX 两大格式的工具生态比较，覆盖 108 个开源工具与 62 个专有工具，聚焦"生成/分析/管理 SBOM 的工具是否可用"而非因果效力。候选块未提供引用数 `> 待核实` [60]。
  - 热度证据：`> 待核实`（候选块未给引用/star）
  - 权威证据：arXiv 预印本（cs.SE），未经同行评审 [60]
  - 关注度：中——SBOM 是供应链安全政策焦点，但缺少采用度量化信号
  - 推荐度：★★★☆☆——可支撑工具生态现状，**不可**被解读为"SBOM 降低风险"的效力证明

- **依赖混淆的结构性防御**：论文指出依赖混淆利用软件分发的结构性缺口——包一旦安装，就缺少"由哪个注册表分发"的密码学证明；现有防御均为配置式、误配时静默失败。作者提出密码学分发溯源机制 [115]。热度 `> 待核实`；权威为 arXiv（cs.CR）预印本；关注度中（对准已知攻击类别）；推荐度 ★★★★☆（若需防御工程落地可精读）。

- **攻击链图分析**：SBOM 分析流程通常把扫描器发现当作独立的 per-CVE 条目处理，本文提出从 SBOM 图预测"多漏洞级联攻击链"，弥补该盲区 [114]。热度 `> 待核实`；权威 arXiv（cs.SE）预印本；关注度中；推荐度 ★★★★☆。

- **其他供应链工作**：
  - SoK：以安全设计属性分析软件供应链安全 [107]；信任与区块链启用的 SBOM/AIBOM 未来 [108]；供应链攻击、风险评估与安全控制综述 [113]。
  - 具体攻击面：GoSurf 识别 Go 生态供应链攻击向量 [109]；Maven-Hijack 利用打包顺序实施攻击 [112]；SpellBound 防御包名抢注（typosquatting）[116]。
  - 领域扩展：Web3 软件供应链安全（dApp / 智能合约依赖复杂）[111]；GitHub 开源软件开发挑战的系统文献综述 [71]。

### 2.3 漏洞数据可信度

- **NVD 漏洞版本数据不可靠**：对 Google Chrome 漏洞的实证实验指出 NVD "脆弱版本"数据存在问题 [86]。该文为 2013 年 arXiv 预印本，是**经典奠基性的数据质量警示**。热度 `> 待核实`；权威为早期预印本（已被大量后续工作引用，但本候选块未给引用数）；关注度：中（数据质量问题长期存在）；推荐度 ★★★★☆（做漏洞数据研究前必读）。

### 2.4 恶意软件分析

- **基于操作码图的恶意软件变体检测**：使用聚类生成操作码图 [118]。
- **IMCDCF**：使用隐马尔可夫模型的增量式恶意软件检测 [119]。
- **LLM/生成式 AI 的双刃性**：综述覆盖 AI 生成恶意软件、可解释性与防御策略 [122]。

三类证据均 `> 待核实`（候选块未给引用/star/榜单）；权威为 arXiv 预印本与 IEEE SVCC 2025 会议论文 [122]；关注度中；推荐度 ★★★☆☆（恶意软件方向的候选证据整体偏薄，缺口见第七章）。

---

## 三、模糊测试与程序分析

### 3.1 覆盖引导模糊测试（Coverage-Guided Fuzzing）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Evaluating the Fork-Awareness of Coverage-Guided Fuzzers | 2023 | arXiv 预印本 | `> 待核实` | B | 中 | ★★★☆☆ | http://arxiv.org/abs/2301.05060v1 | 评估模糊器的 fork 感知能力 [2] |
| Same Coverage, Less Bloat（覆盖保持的覆盖引导追踪） | 2022 | arXiv 预印本 | `> 待核实` | B | 中 | ★★★★☆ | http://arxiv.org/abs/2209.03441v1 | 加速 binary-only 模糊测试 [4] |
| FOX: Coverage-guided Fuzzing as Online Stochastic Control | 2024 | arXiv 预印本 | `> 待核实` | B | 中 | ★★★★☆ | http://arxiv.org/abs/2406.04517v1 | 把覆盖引导模糊测试建模为在线随机控制 [6] |
| Greybox fuzzing as a contextual bandits problem | 2018 | arXiv 预印本 | `> 待核实` | B（经典） | 中 | ★★★★☆ | http://arxiv.org/abs/1806.03806v1 | 上下文多臂老虎机视角 [30] |
| Learning Inputs in Greybox Fuzzing | 2018 | arXiv 预印本 | `> 待核实` | B（经典） | 中 | ★★★★☆ | http://arxiv.org/abs/1807.07875v1 | 学习型输入构造，破解复杂检查 [28] |
| Low-Cost and Comprehensive Non-textual Input Fuzzing with LLM-Synthesized Input Generators | 2025 | arXiv 预印本 | `> 待核实` | B | 中 | ★★★★☆ | http://arxiv.org/abs/2501.19282v1 | LLM 合成输入生成器处理非文本输入 [9] |

### 3.2 定向灰盒模糊测试与混合测试（DGF / Hybrid）

- **DGF 的演进线**：从 Munch（2017，混合 fuzzing + 定向符号执行）[11]、多目标 DGF [16]、MC²（2022，严格且高效的定向灰盒模糊测试）[12]，到 2020 年前后的进展与挑战综述 [15]、2017 年的混合测试技术探索性综述 [10]。
- **最新工程形态**：混合定向模糊测试把 LibAFL-DiFuzz 与 Sydr（动态符号执行器）组合，提出基于"目标相关有趣度 + 覆盖率"的种子调度、种子最小化与排序，用 Time to Exposure 评估 [14]。
- **2026 最新批判**：S²F 指出 SOTA 混合测试的两个缺陷——(a) 定制符号执行引擎过度剪枝，导致大量时间等待模糊器种子、错过崩溃机会；(b) 采样未作用于合适分支。作者提出统一架构 [17]。

四类证据：热度 `> 待核实`（候选块未给引用数）；权威为 arXiv 预印本（cs.CR / cs.SE）；关注度中（DGF 与混合测试持续有人推进，[14] 在 2026 年初仍修订至 v2）；推荐度 ★★★★☆（[14][17] 建议对照阅读）。

### 3.3 符号执行（Symbolic Execution / Concolic）

- **综述**：`Symbolic Execution in Practice` 提出应对路径爆炸的 taxonomy——Scope Reduction（限制符号执行到可管理代码）与 Guidance Heuristics（引导引擎走向有希望路径），并综述其在漏洞、恶意软件、固件与协议分析中的应用 [13]。
- **比较与引导**：
  - cozy：面向二进制程序的比较式符号执行 [19]。
  - LLM 能否模拟 KLEE 的符号执行输出 [34]。
  - LLM 引导的 KLEE 定向符号执行（2026），用于漏洞发现 [38]。
  - KLEE Sonar-Search 策略在灰盒模糊测试语境下的回顾（2018，经典）[33]。
  - 高阶符号执行用于合约验证与反驳（2015）[35]。

四类证据：候选块均无引用数 `> 待核实`；权威为 arXiv 预印本；关注度中（LLM 与符号执行结合是 2025–2026 新热点 [34][38]）；推荐度 ★★★★☆（[13] 作入口，[34][38] 作前沿）。

### 3.4 内核、二进制与 LLM 辅助漏洞检测

- **SyzScope**：揭示 fuzzer 在 Linux 内核中发现的 bug 的高风险安全影响 [3]。这是内核漏洞评估的经典工作。
- **剥离二进制漏洞检测**：VulBinLLM 明确把 stripped binary 漏洞检测定义为开放问题，探索 LLM 在该场景的应用 [20]。
- **神经反编译辅助**：用神经反编译改善二进制代码漏洞预测 [21]。
- **VulCatch**：CodeT5 反编译 + KAN 特征提取增强二进制漏洞检测 [24]。
- **硬件侧信道经典**：SoK 梳理针对推测执行攻击的硬件防御 [36]。

四类证据：热度 `> 待核实`；权威为 arXiv 预印本；关注度中；推荐度 ★★★☆☆–★★★★☆。

### 3.5 相关但弱关联

- 车载软件更新框架 UniSUF 的形式化验证（ProVerif 建模），与漏洞发现主线仅间接相关 [8]。推荐度 ★★☆☆☆。

---

## 四、大模型与 Agent 安全（提示注入 / 越狱 / 数据外泄）

### 4.1 攻击侧：从直接注入到间接注入与持久记忆投毒

- **自动且通用的提示注入攻击**（2024）：奠定"注入可自动化、可跨模型迁移"的早期范式 [39]。
- **WebInject**：通过操纵网页环境，诱导基于 MLLM 的 Web Agent 执行攻击者动作 [89]。
- **Backdoor-Powered Prompt Injection**：论文称后门驱动的注入可"使防御方法失效" [94]。
- **隐蔽间接注入**：`Will the User Ever Know?` 指出标准 ASR 指标只看注入是否成功，忽略"用户在 Agent 最终回复中是否察觉"，并提出隐蔽性评估视角 [97]。
- **持久记忆攻击**：`Injection-Execution Dissociation` 对有状态 Agent 的持久记忆做机制性评估 [57]。

四类证据：热度 `> 待核实`；权威为 arXiv 预印本（cs.LG / cs.CR / cs.AI）；关注度：中–高（IPI 是 2024–2026 Agent 安全主线，[97] 提出指标层面的反思故关注度较高）；推荐度 ★★★★☆。

### 4.2 防御侧：结构化、偏好优化、工具图与多智能体

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| StruQ: Defending Against Prompt Injection with Structured Queries | 2024 | arXiv 预印本 | `> 待核实` | B | 中 | ★★★★☆ | http://arxiv.org/abs/2402.06363v2 | 结构化查询隔离指令与数据 [44] |
| SecAlign: Defending Against Prompt Injection with Preference Optimization | 2024 | arXiv 预印本 | `> 待核实` | B | 中 | ★★★★☆ | http://arxiv.org/abs/2410.05451v3 | 用偏好优化做对齐式防御 [40] |
| MELON: Provable Defense Against Indirect Prompt Injection | 2025 | arXiv 预印本 | `> 待核实` | B | 中 | ★★★★☆ | http://arxiv.org/abs/2502.05174v4 | 宣称可证明的 IPI 防御 [90] |
| UniGuardian: A Unified Defense for Detecting Prompt Injection, Backdoor and Adversarial Attacks | 2025 | arXiv 预印本 | `> 待核实` | B | 中 | ★★★★☆ | http://arxiv.org/abs/2502.13141v2 | 统一检测三类威胁 [91] |
| IPIGuard: Tool Dependency Graph-Based Defense Against IPI | 2025 | arXiv 预印本（cs.CR） | `> 待核实` | B | 中 | ★★★★☆ | http://arxiv.org/abs/2508.15310v1 | 用工具依赖图约束工具响应 [101] |
| A Multi-Agent LLM Defense Pipeline Against Prompt Injection | 2025 | arXiv 预印本（cs.CR） | `> 待核实` | B | 中 | ★★★★☆ | http://arxiv.org/abs/2509.14285v4 | 多智能体防御流水线 [92] |
| ACE: A Security Architecture for LLM-Integrated App Systems | 2025 | arXiv 预印本 | `> 待核实` | B | 中 | ★★★★☆ | http://arxiv.org/abs/2504.20984v3 | LLM 集成应用的安全架构 [75] |
| Detecting Prompt Injection Attacks Against Application Using Classifiers | 2025 | arXiv 预印本（cs.CR） | `> 待核实` | B | 低–中 | ★★★☆☆ | http://arxiv.org/abs/2512.12583v1 | 基于 HackAPrompt 语料训练分类器 [45] |

### 4.3 越狱（Jailbreak）

- **JailbreakBench**：开源越狱鲁棒性基准 [41]，是最常被引用的评测起点之一（热度 `> 待核实`）。
- **Benign-to-Toxic Jailbreaking**：论文发现既有 LVLM 优化式越狱采用 Toxic-Continuation 设定存在问题，提出"从无害提示诱导有害响应"的新设定 [42]。
- **Evolving Security in LLMs**：越狱攻击与防御的研究 [104]。
- **LLMs Can Defend Themselves**：以 vision paper 形式提出实用自防御路线 [102]。
- **SoK：越狱护栏评测** [105]，系统梳理护栏机制评测方法。

### 4.4 Agent 安全基准与元评测

- **AgentDojo**：动态环境评估 LLM Agent 的提示注入攻防 [80]——本节最重要的基准类证据。
- **NetInjectBench**：面向网络运维工具使用 Agent 的 130 场景 IPI 基准，分离非信任产物文本与可信策略元数据 [99]。
- **Adaptive Adversaries**：多轮、多 LLM 的 Agent 安全基准 [79]。
- **基准的元评测**：`What Twelve LLM Agent Benchmark Papers Disclose About Themselves` 对 12 篇 Agent 基准论文做审计并提出开放评分 schema [78]。
- **指标语义学**：`The Same Zero: Why Identical ASR Can Imply Different Guarantees` 说明相同 ASR 可对应不同安全保证 [77]。
- **其他**：ISPM 语义下的 Agentic AI 身份安全姿态管理基准 [76]。

### 4.5 综述与 SoK

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| SoK: The Attack Surface of Agentic AI – Tools and Autonomy | 2026 | arXiv 预印本 | `> 待核实` | B | 中 | ★★★★☆ | https://doi.org/10.48550/arxiv.2603.22928 | Agentic AI 攻击面系统化梳理 [96] |
| Hijacking the Prompt: A Survey of Prompt Injection | — | DOI 正式出版物 | `> 待核实` | A/B（DOI 指向正式出版） | 中 | ★★★★☆ | https://doi.org/10.25776/mvhf-w867 | 提示注入攻防综述 [93] |
| Securing LLM Powered AI Browsers: Survey, Taxonomy, Defense | — | SSRN | `> 待核实` | C（SSRN 预印） | 中 | ★★★☆☆ | https://doi.org/10.2139/ssrn.6340078 | AI 浏览器安全 [95] |
| Security Threats in the Model Context Protocol | — | IJSR 类期刊 | `> 待核实` | C | 中 | ★★★☆☆ | https://doi.org/10.21275/sr26316110418 | MCP 信任边界缓解框架 [100] |
| Interaction-Centric Cybersecurity Risks in LLM-Powered Dialogue Systems | 2026 | IEEE CCWC 2026 | `> 待核实` | A（IEEE 会议） | 中 | ★★★★☆ | https://doi.org/10.1109/ccwc67433.2026.11393850 | 对话系统交互安全风险 [98] |
| SoK: Trading Agents or Market Crashers? | 2026 | arXiv 预印本（cs.CR） | `> 待核实` | B | 中 | ★★★☆☆ | http://arxiv.org/abs/2609.19705v1 | 金融交易 Agent 安全失效 [74] |

---

## 五、密码学与后量子迁移

本节候选证据较少，且**经典密码学奠基（如 RSA、ECC、Shor 算法、NIST PQC 标准 FIPS 203/204/205）未在候选块中出现**，需明确标为证据缺口。

### 5.1 密钥管理与秘密工程

- **MFKDF（Multi-Factor Key Derivation Function）**：面向快速、灵活、安全的实用密钥管理（arXiv v3）[7]。热度 `> 待核实`；权威 arXiv 预印本（有 v3 表明持续修订）；关注度中；推荐度 ★★★☆☆（与"密码学工程"主题相关但非后量子主线）。

### 5.2 后量子密码（PQC）迁移

- **编码智能体能否迁移到 PQC？**：把 PQC 迁移当作代码迁移任务，评估 coding agents 的能力边界 [67]。这是 2025–2026 的新议题。热度 `> 待核实`；权威 arXiv 预印本（v3，说明修订多次）；关注度：中（AI for 安全工程属新兴交叉点）；推荐度 ★★★★☆（对"AI 辅助安全工程"方向有代表性）。
- **量子就绪安全 WAN**：提出风险评估与迁移框架 [68]，切中"PQC 迁移的成本与兼容性"这一争议。热度 `> 待核实`；权威 arXiv 预印本；关注度中；推荐度 ★★★☆☆。
- **量子密码学的历史路径**：`A new spin on quantum cryptography: Avoiding trapdoors and embracing public keys`（2011）[66]，属早期量子密码思路文献。热度 `> 待核实`；权威 arXiv 预印本；关注度低；推荐度 ★★☆☆☆（历史参考）。

> 待核实：NIST PQC 标准（FIPS 203/204/205）的官方版本号、发布时间与迁移时间线，本批次候选证据未覆盖，不得据记忆补充。

---

## 六、数据集、基准与红蓝对抗

### 6.1 数据集

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| NVD / CVE | ongoing | NIST | `> 待核实` | A（官方数据库） | 高 | ★★★★★ | https://nvd.nist.gov/ | 漏洞数据库；但版本数据可靠性存疑 [86] |
| CWE / CWE Top 25 | ongoing | MITRE | `> 待核实` | A（官方标准） | 高 | ★★★★★ | https://cwe.mitre.org/top25/ | 弱点排行 |
| CVEfixes | 2021 | arXiv 预印本 | `> 待核实` | B | 中 | ★★★★☆ | http://arxiv.org/abs/2107.08760v1 / https://github.com/secureIT-project/CVEfixes | 自动采集漏洞与修复 [81] |
| Big-Vul | — | 种子资源 | `> 待核实` | `> 待核实` | `> 待核实` | ★★★☆☆ | （种子资源给出 CVEfixes 链接） | 漏洞修复数据集 |

> 注意：`OSV`、`MalwareBazaar`、`EMBER` 在本批次候选中**完全未被覆盖**，属证据缺口 `> 待核实`。

### 6.2 开源工具链与项目

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| AFL++ | ongoing | AFLplusplus 社区 | `> 待核实`（候选块未给 star） | B（事实标准开源项目） | 高（覆盖引导模糊测试事实标准） | ★★★★★ | https://github.com/AFLplusplus/AFLplusplus | 覆盖率引导模糊测试框架 |
| OSS-Fuzz | ongoing | Google | `> 待核实` | B（官方基础设施） | 高 | ★★★★★ | https://github.com/google/oss-fuzz | 持续模糊测试基础设施 |
| angr | ongoing | angr 团队 | `> 待核实` | B | 高 | ★★★★★ | https://github.com/angr/angr | 二进制符号执行框架 |
| Semgrep | ongoing | Semgrep（Trail of Bits 出身） | `> 待核实` | B | 中–高 | ★★★★☆ | https://github.com/semgrep/semgrep | 静态分析（SAST） |
| Sigstore | ongoing | sigstore 社区 | `> 待核实` | B（供应链签名事实标准之一） | 高 | ★★★★★ | https://github.com/sigstore/sigstore | 软件供应链签名 |
| OSS-CRS | 2026 | arXiv 预印本（cs.CR） | `> 待核实` | B | 中 | ★★★★☆ | http://arxiv.org/abs/2603.08566v2 | 将 AIxCC 网络推理系统释放到真实开源场景 [88] |

> 说明：种子资源给出的仓库均来自 memory 提示，其 star / 最近提交 / 许可**未在候选块中被核实**，故热度列写 `> 待核实`，不得编造数字。

### 6.3 基准与红蓝对抗生态

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| AgentDojo | 2024 | arXiv 预印本（v3） | `> 待核实` | B | 中–高 | ★★★★★ | http://arxiv.org/abs/2406.13352v3 | 动态评估 LLM Agent 提示注入攻防 [80] |
| JailbreakBench | 2024 | arXiv 预印本（v5） | `> 待核实` | B | 中–高 | ★★★★★ | http://arxiv.org/abs/2404.01318v5 | 开源越狱鲁棒性基准 [41] |
| SoK: 越狱护栏评测 | 2025 | arXiv 预印本（cs.CR） | `> 待核实` | B | 中 | ★★★★☆ | http://arxiv.org/abs/2506.10597v2 | 护栏评测方法的 SoK [105] |
| NetInjectBench | 2026 | arXiv 预印本（cs.CR） | `> 待核实` | B | 中 | ★★★★☆ | http://arxiv.org/abs/2607.10490v2 | 130 场景运维 IPI 基准 [99] |
| Adaptive Adversaries | 2026 | arXiv 预印本（v2） | `> 待核实` | B | 中 | ★★★★☆ | http://arxiv.org/abs/2607.18063v2 | 多轮多 LLM Agent 安全基准 [79] |
| SoK: DARPA AIxCC | 2026 | arXiv 预印本（v5） | `> 待核实` | B | 中（AIxCC 为最受关注的安全竞赛之一） | ★★★★☆ | http://arxiv.org/abs/2602.07666v5 | AIxCC 竞赛设计、架构与经验 [87] |
| FMTI 2025 | 2025 | arXiv 预印本（cs.AI） | `> 待核实` | B | 中 | ★★★☆☆ | http://arxiv.org/abs/2512.10169v1 | 基础模型透明度年度指数第三版 [50] |

> **候选证据错配提示**：本批次关于"工具链/基准/数据集/竞赛"的候选池中，4/6 条为视觉、多媒体与 NLP 的竞赛概览（[1][69][70][73]），与安全工具链无关；相关子问题主要依赖种子资源与跨子问题证据补齐，故本表部分条目源自其他子问题的证据。

---

## 七、争议与开放问题

### 7.1 争议一：LLM 安全防御的"自适应攻击缺口"

- **主张**：现有越狱与提示注入防御通常用静态恶意串评估，或用并非针对该防御设计、算力较弱的优化方法评估；更强的自适应攻击可绕过这些防御 [58]。
- 热度证据：`> 待核实`（候选块未给引用数）
- 权威证据：arXiv cs.LG 预印本（2510.09023v1），未经同行评审 [58]
- 关注度：中（直接对撞评测范式，属高敏感议题）
- 推荐度：★★★★☆——主题契合度最高，建议优先精读并核对其攻击协议
- 旁证：[54] 同样以"自适应攻击"为主题针对 IPI 防御；[56] 对六大护栏系统给出实证绕过结果。

**关键细节**：[56] 摘要称部分场景规避率"最高可达 100%"，但**统计口径（样本量、判据、任务设置）在候选块中被截断**，引用该数字前必须回原文表格核实 `> 待核实`。

### 7.2 争议二：护栏机制的性能—误报权衡

候选证据仅覆盖"护栏可被绕过"的攻击侧结论 [56][105]，**检测率、误报率、延迟、可用性等部署成本维度在候选块中缺失** `> 待核实`。这意味着"护栏是否值得部署"在当前证据下无法回答。

### 7.3 争议三：Agent 安全基准的指标可比性

- **相同 ASR ≠ 相同安全保证** [77]。
- **基准自体披露质量参差**：12 篇 Agent 基准论文的审计与开放评分 schema 提出 [78]。
- 两者共同构成"Agent 安全是否已有可比较评测"的开放争议。

### 7.4 争议四：SBOM 是否真正降低风险

- 现有研究聚焦工具生态健康度（108 开源 + 62 专有工具），**未给出 SBOM 采用与漏洞/事件下降的因果关系**，故"SBOM 是否降低风险"在候选证据中仍未决 [60]。
- 支持方向：从 SBOM 图预测多漏洞攻击链 [114]、密码学注册表溯源 [115]。

### 7.5 争议五：漏洞数据可信度

- NVD "脆弱版本"数据可靠性存疑（2013 年实证，Chrome 漏洞）[86]。
- 该问题与 [114] 的"扫描器发现被当作独立 per-CVE"批评在逻辑上相互支持：**数据层与聚合层都存在系统性偏差**。

### 7.6 争议六：AI 时代的透明度倒退

- 2025 FMTI 平均分从 2024 年 58/100 降至 2025 年 40/100；训练数据、训练算力、部署后影响最不透明 [50]。
- 与安全审计与责任归属直接相关，但**候选证据未给出"透明度下降是否直接恶化安全事件"的因果链条** `> 待核实`。

### 7.7 明确记录的证据缺口（必须补检索）

- **模糊测试 SOTA 可复现性危机**：候选块无 fuzzing 基准榜单、复现失败调查、基准污染证据 `> 待核实`（[1][53] 为无关的挑战赛/系统报告，不构成证据）。
- **PQC 迁移成本与兼容性争议**：仅 [67][68] 两条相关预印本，未见 NIST 标准原文、厂商迁移报告或成本量化研究 `> 待核实`。
- **负结果与复现困难报告**：候选块中**没有任何**负面结果论文或复现报告 `> 待核实`。
- **内存安全方向（Rust/C++/内核）**：仅有 SyzScope [3] 与硬件事务性侧信道 SoK [36] 沾边，缺 Rust 迁移、内核内存安全专题 `> 待核实`。
- **恶意软件数据集（MalwareBazaar、EMBER）**：完全缺失 `> 待核实`。

---

## 八、建议关注清单（Watchlist）

| 优先级 | 条目 | 理由 | 关键引用 |
|---|---|---|---|
| P0 | Agent 安全评测的"指标语义"问题 | ASR 相同可对应不同保证，直接决定基准结论能否跨论文比较 | [77][78][80][99] |
| P0 | 自适应攻击 vs 静态评估的方法论批判 | 可能推翻一批防御论文的有效性宣称 | [54][56][58] |
| P0 | AIxCC 与 OSS-CRS 的工程产出 | AI 驱动漏洞发现第一个大规模真实竞赛，工程可复用性高 | [87][88] |
| P1 | 混合测试架构的结构性缺陷与修复 | S²F 直指 SOTA 工具的两个瓶颈，可与 Sydr 方案对照 | [14][17] |
| P1 | LLM 辅助符号执行与二进制漏洞检测 | LLM + KLEE、LLM + stripped binary 是最活跃交叉点 | [20][34][38] |
| P1 | SBOM 攻击链图分析与密码学溯源 | 供应链安全从清单走向结构性防御 | [114][115] |
| P2 | 依赖混淆与包名抢注防御 | 有明确攻击类别与可落地防御 | [112][115][116] |
| P2 | LLM Agent 持久记忆攻击 | 有状态 Agent 的特有攻击面，未被主流基准覆盖 | [57] |
| P2 | MCP 与 AI 浏览器信任边界 | 新协议/新载体带来新攻击面，尚缺同行评审共识 | [95][100] |
| P3 | Coding agents for PQC 迁移 | AI 辅助安全工程的新方向，成本/兼容性争议待解 | [67][68] |
| P3 | 基础模型透明度年度指数 | 治理与安全的交叉参照，需跟踪 2026 版 | [50] |

---

## 参考来源

[1] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1
[2] Evaluating the Fork-Awareness of Coverage-Guided Fuzzers — http://arxiv.org/abs/2301.05060v1
[3] SyzScope: Revealing High-Risk Security Impacts of Fuzzer-Exposed Bugs in Linux kernel — http://arxiv.org/abs/2111.06002v1
[4] Same Coverage, Less Bloat: Accelerating Binary-only Fuzzing with Coverage-preserving Coverage-guided Tracing — http://arxiv.org/abs/2209.03441v1
[5] Internet Service Providers' and Individuals' Attitudes, Barriers, and Incentives to Secure IoT — http://arxiv.org/abs/2210.02137v1
[6] FOX: Coverage-guided Fuzzing as Online Stochastic Control — http://arxiv.org/abs/2406.04517v1
[7] Multi-Factor Key Derivation Function (MFKDF) for Fast, Flexible, Secure, & Practical Key Management — http://arxiv.org/abs/2208.05586v3
[8] Towards a Formal Verification of Secure Vehicle Software Updates — http://arxiv.org/abs/2511.15479v1
[9] Low-Cost and Comprehensive Non-textual Input Fuzzing with LLM-Synthesized Input Generators — http://arxiv.org/abs/2501.19282v1
[10] An Exploratory Survey of Hybrid Testing Techniques Involving Symbolic Execution and Fuzzing — http://arxiv.org/abs/1712.06843v1
[11] Improving Function Coverage with Munch: A Hybrid Fuzzing and Directed Symbolic Execution Approach — http://arxiv.org/abs/1711.09362v2
[12] $MC^2$: Rigorous and Efficient Directed Greybox Fuzzing — http://arxiv.org/abs/2208.14530v1
[13] Symbolic Execution in Practice: A Survey of Applications in Vulnerability, Malware, Firmware, and Protocol Analysis — http://arxiv.org/abs/2508.06643v1
[14] Hybrid Approach to Directed Fuzzing — http://arxiv.org/abs/2507.04855v2
[15] The Progress, Challenges, and Perspectives of Directed Greybox Fuzzing — http://arxiv.org/abs/2005.11907v5
[16] Multiple Targets Directed Greybox Fuzzing — http://arxiv.org/abs/2206.14977v1
[17] S$^2$F: Principled Hybrid Testing With Fuzzing, Symbolic Execution, and Sampling — http://arxiv.org/abs/2601.10068v1
[18] mdok of KInIT: Robustly Fine-tuned LLM for Binary and Multiclass AI-Generated Text Detection — http://arxiv.org/abs/2506.01702v2
[19] cozy: Comparative Symbolic Execution for Binary Programs — http://arxiv.org/abs/2504.00151v1
[20] VulBinLLM: LLM-powered Vulnerability Detection for Stripped Binaries — http://arxiv.org/abs/2505.22010v1
[21] Can Neural Decompilation Assist Vulnerability Prediction on Binary Code? — http://arxiv.org/abs/2412.07538v2
[22] Hallucination Detection and Mitigation in Scientific Text Simplification using Ensemble Approaches — http://arxiv.org/abs/2508.11823v1
[23] SINAI at eRisk@CLEF 2025 — http://arxiv.org/abs/2509.19861v1
[24] VulCatch: Enhancing Binary Vulnerability Detection through CodeT5 Decompilation and KAN Advanced Feature Extraction — http://arxiv.org/abs/2408.07181v1
[25] Summary of the EDS Blois 2013 Workshop — http://arxiv.org/abs/1310.7047v1
[26] The Reactive Synthesis Competition: SYNTCOMP 2016 and Beyond — http://arxiv.org/abs/1611.07626v1
[27] This paper has been withdrawn — http://arxiv.org/abs/cond-mat/0309395v2
[28] Learning Inputs in Greybox Fuzzing — http://arxiv.org/abs/1807.07875v1
[29] The TTC 2013 Flowgraphs Case — http://arxiv.org/abs/1312.0341v1
[30] Greybox fuzzing as a contextual bandits problem — http://arxiv.org/abs/1806.03806v1
[31] Solving the TTC 2013 Flowgraphs Case with FunnyQT — http://arxiv.org/abs/1312.0347v1
[32] Neutron-Antineutron Oscillations: A Snowmass 2013 White Paper — http://arxiv.org/abs/1310.8593v1
[33] Reviewing KLEE's Sonar-Search Strategy in Context of Greybox Fuzzing — http://arxiv.org/abs/1803.04881v1
[34] Can Large Language Models Simulate Symbolic Execution Output Like KLEE? — http://arxiv.org/abs/2511.08530v1
[35] Higher-order symbolic execution for contract verification and refutation — http://arxiv.org/abs/1507.04817v3
[36] SoK: Hardware Defenses Against Speculative Execution Attacks — http://arxiv.org/abs/2301.03724v1
[37] Obstructions to weak decomposability for simplicial polytopes — http://arxiv.org/abs/1206.6143v1
[38] Directed Symbolic Execution for Vulnerability Discovery: An LLM-Guided Approach in KLEE — http://arxiv.org/abs/2607.21676v1
[39] Automatic and Universal Prompt Injection Attacks against Large Language Models — http://arxiv.org/abs/2403.04957v1
[40] SecAlign: Defending Against Prompt Injection with Preference Optimization — http://arxiv.org/abs/2410.05451v3
[41] JailbreakBench: An Open Robustness Benchmark for Jailbreaking Large Language Models — http://arxiv.org/abs/2404.01318v5
[42] Benign-to-Toxic Jailbreaking: Inducing Harmful Responses from Harmless Prompts — http://arxiv.org/abs/2505.21556v1
[43] Overview of AuTexTification at IberLEF 2023 — http://arxiv.org/abs/2309.11285v1
[44] StruQ: Defending Against Prompt Injection with Structured Queries — http://arxiv.org/abs/2402.06363v2
[45] Detecting Prompt Injection Attacks Against Application Using Classifiers — http://arxiv.org/abs/2512.12583v1
[46] NTU-NPU System for Voice Privacy 2024 Challenge — http://arxiv.org/abs/2410.02371v1
[47] Overview of the Sensemaking Task at the ELOQUENT 2025 Lab — http://arxiv.org/abs/2507.12143v1
[48] LongEval at CLEF 2025 — http://arxiv.org/abs/2503.08541v1
[49] OpenFact at CheckThat! 2024 — http://arxiv.org/abs/2409.02649v2
[50] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1
[51] Discovery Opportunities with Gravitational Waves — TASI 2024 Lecture Notes — http://arxiv.org/abs/2409.08956v1
[52] Atmospheric entry and fragmentation of small asteroid 2024 BX1 — http://arxiv.org/abs/2403.00634v2
[53] Annif at SemEval-2025 Task 5 — http://arxiv.org/abs/2504.19675v2
[54] Adaptive Attacks Break Defenses Against Indirect Prompt Injection Attacks on LLM Agents — http://arxiv.org/abs/2503.00061v2
[55] CEA-LIST at CheckThat! 2025 — http://arxiv.org/abs/2507.07539v1
[56] Bypassing LLM Guardrails: An Empirical Analysis of Evasion Attacks against Prompt Injection and Jailbreak Detection Systems — http://arxiv.org/abs/2504.11168v3
[57] Injection-Execution Dissociation: A Mechanistic Evaluation of Persistent Memory Attacks and Defenses in Stateful LLM Agents — http://arxiv.org/abs/2605.08442v5
[58] The Attacker Moves Second: Stronger Adaptive Attacks Bypass Defenses Against LLM Jailbreaks and Prompt Injections — http://arxiv.org/abs/2510.09023v1
[59] Sequential Design and Spatial Modeling for Portfolio Tail Risk Measurement — http://arxiv.org/abs/1710.05204v2
[60] The State of the SBOM Tool Ecosystems: A Comparative Analysis of SPDX and CycloneDX — http://arxiv.org/abs/2512.21781v2
[61] A generic nonparametric value-at-risk estimator for high dimensions — http://arxiv.org/abs/2608.17481v1
[62] Evaluating Range Value at Risk Forecasts — http://arxiv.org/abs/1902.04489v3
[63] On the Selection of Loss Severity Distributions to Model Operational Risk — http://arxiv.org/abs/2107.03979v1
[64] Statistical Emulators for Pricing and Hedging Longevity Risk Products — http://arxiv.org/abs/1508.00310v2
[65] Robust blue-green urban flood risk management — http://arxiv.org/abs/2502.12174v2
[66] A new spin on quantum cryptography: Avoiding trapdoors and embracing public keys — http://arxiv.org/abs/1109.3235v1
[67] Can Coding Agents Migrate to Post-Quantum Cryptography? — http://arxiv.org/abs/2512.12989v3
[68] Quantum-Ready Secure WAN: A Risk Assessment and Migration Framework — http://arxiv.org/abs/2609.26225v1
[69] NTIRE 2025 Challenge on Image Super-Resolution (x4) — http://arxiv.org/abs/2504.14582v3
[70] Event-Enriched Image Analysis Grand Challenge at ACM Multimedia 2025 — http://arxiv.org/abs/2508.18904v1
[71] Open Source Software Development Challenges: A Systematic Literature Review on GitHub — http://arxiv.org/abs/2003.10750v3
[72] TDCOSMO 2025: Cosmological constraints from strong lensing time delays — http://arxiv.org/abs/2506.03023v4
[73] Team Anotheroption at SemEval-2025 Task 8 — http://arxiv.org/abs/2506.09657v2
[74] SoK: Trading Agents or Market Crashers? — http://arxiv.org/abs/2609.19705v1
[75] ACE: A Security Architecture for LLM-Integrated App Systems — http://arxiv.org/abs/2504.20984v3
[76] Sola-Visibility-ISPM: Benchmarking Agentic AI for Identity Security Posture Management Visibility — http://arxiv.org/abs/2601.07880v1
[77] The Same Zero: Why Identical ASR Can Imply Different Guarantees in LLM-Agent Security — http://arxiv.org/abs/2610.04504v1
[78] What Twelve LLM Agent Benchmark Papers Disclose About Themselves — http://arxiv.org/abs/2605.21404v1
[79] Adaptive Adversaries: A Multi-Turn, Multi-LLM Benchmark for LLM Agent Security — http://arxiv.org/abs/2607.18063v2
[80] AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents — http://arxiv.org/abs/2406.13352v3
[81] CVEfixes: Automated Collection of Vulnerabilities and Their Fixes from Open-Source Software — http://arxiv.org/abs/2107.08760v1
[82] The RSNA Abdominal Traumatic Injury CT (RATIC) Dataset — http://arxiv.org/abs/2405.19595v1
[83] NTIRE 2025 Challenge on Short-form UGC Video Quality Assessment and Enhancement — http://arxiv.org/abs/2504.15003v1
[84] The RSNA Intracranial Aneurysm (RSNA-ICA) Dataset — http://arxiv.org/abs/2610.01135v2
[85] VLSP 2025 MLQA-TSR Challenge — http://arxiv.org/abs/2510.20381v1
[86] The (Un)Reliability of NVD Vulnerable Versions Data: an Empirical Experiment on Google Chrome Vulnerabilities — http://arxiv.org/abs/1302.4133v1
[87] SoK: DARPA's AI Cyber Challenge (AIxCC): Competition Design, Architectures, and Lessons Learned — http://arxiv.org/abs/2602.07666v5
[88] OSS-CRS: Liberating AIxCC Cyber Reasoning Systems for Real-World Open-Source Security — http://arxiv.org/abs/2603.08566v2
[89] WebInject: Prompt Injection Attack to Web Agents — http://arxiv.org/abs/2505.11717v4
[90] MELON: Provable Defense Against Indirect Prompt Injection Attacks in AI Agents — http://arxiv.org/abs/2502.05174v4
[91] UniGuardian: A Unified Defense for Detecting Prompt Injection, Backdoor Attacks and Adversarial Attacks in LLMs — http://arxiv.org/abs/2502.13141v2
[92] A Multi-Agent LLM Defense Pipeline Against Prompt Injection Attacks — http://arxiv.org/abs/2509.14285v4
[93] Hijacking the Prompt: A Survey of Prompt Injection Attacks, Detection, and Defense in LLMs — https://doi.org/10.25776/mvhf-w867
[94] Backdoor-Powered Prompt Injection Attacks Nullify Defense Methods — http://arxiv.org/abs/2510.03705v1
[95] Securing LLM Powered AI Browsers Against Prompt Injection — https://doi.org/10.2139/ssrn.6340078
[96] SoK: The Attack Surface of Agentic AI – Tools and Autonomy — https://doi.org/10.48550/arxiv.2603.22928
[97] Will the User Ever Know? Covert Indirect Prompt Injection Attacks on Tool-Using LLM Agents — http://arxiv.org/abs/2608.30362v3
[98] Interaction-Centric Cybersecurity Risks in LLM-Powered Dialogue Systems — https://doi.org/10.1109/ccwc67433.2026.11393850
[99] NetInjectBench: Benchmarking Indirect Prompt Injection in Tool-Using LLM Agents for Network Operations — http://arxiv.org/abs/

---

*Generated by research-bot · topic=`cybersecurity` · depth=`standard` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading · model=`deepseek-v4-flash` · sources=122 · duration=340s · 2026-10-06T22:19:39+00:00*
