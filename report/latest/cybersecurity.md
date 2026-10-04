# 网络安全（Cybersecurity）前沿调研报告

> **日期**：2026-10-04（UTC）｜**领域**：Cybersecurity（漏洞与利用 / 模糊测试与程序分析 / 软件供应链与 SBOM / 密码学工程含后量子迁移 / LLM-Agent 安全）
> **检索源数量**：候选编号来源共 **116 条**（本报告实际引用其中约 60 条与主题相关的证据），另纳入 3 类领域种子资源（OWASP/CWE 标准、NVD 漏洞库、5 个开源项目主页）。
> **证据纪律说明**：本次候选块中**绝大多数条目未附带引用数（citations）、GitHub star、下载量或榜单排名**，因此下文凡涉热度/影响力之处一律标注 `> 待核实`，**不做任何数字推测**。所有结论的"权威"等级以"是否同行评审 + 是否官方标准"判定。

---

## 摘要（Executive Summary）

1. **LLM/Agent 安全的信任边界已从"用户输入"迁移到"工具与环境返回的不可信数据"**。间接提示注入（Indirect Prompt Injection, IPI）被两条独立工作同时定义为此新边界的核心威胁 [71][74]，防御范式正从"输入级语义判别"转向"动作级因果归因" [74] 与"系统级架构约束" [71][72]。（置信度：中—高）
2. **多模态攻击面出现**：针对基于 MLLM 的 Web Agent，攻击者可通过向渲染网页的**原始像素**添加扰动完成注入（WebInject）[70]，这是"直接/间接注入"二分法之外的新维度。
3. **模糊测试与程序分析的主线仍是"路径爆炸"与"混合技术集成"**：2025 年综述将符号执行工程化策略归纳为 Scope Reduction 与 Guidance Heuristics 两类 [91]；S²F 主张 fuzzing + 符号执行 + sampling 三者集成优于单一技术，并批评 SOTA 混合工具未充分利用符号执行能力 [93]。
4. **LLM 辅助 fuzzing 的两条落地路径已被证据覆盖**：LLM 合成非文本输入生成器 [85]、LLM/多智能体驱动的 **fuzz harness / fuzz driver 生成** [32][35]。
5. **供应链安全的矛盾从"有没有 SBOM"转向"SBOM 对不对、工具是否合规"**：多项大规模实证研究指出 SBOM 与标准之间存在 adherence gap、字段缺失与不一致 [53][57][58]，依赖混淆的**结构性**防御（密码学注册表溯源）被提出 [20]。
6. **后量子迁移进入"标准落地后的工程摩擦期"**：研究焦点从算法本身转向**签名在证书层级中的位置** [96]、**资源受限设备基准** [99]、**策略与部署现实落差** [110] 与 **TLS 1.3 握手性能分层** [112]。
7. **总体证据强度偏弱**：本批证据**几乎全部为 arXiv 预印本或 Zenodo/SSRN 预印本**，未见同行评审 venue 标注；防御方之间缺乏可比评测基准。这是本报告最重要的元结论。

---

## 一、关键前沿进展（近 1–2 年）

> 时间口径：以"最新进展"= 2024-10 至 2026-10 的发表为准；2023 年及以前归入第二章起的"经典/奠基"表格。

| # | 进展 | 时间 | 一句话贡献 | 证据 |
|---|---|---|---|---|
| 1 | AttriGuard | 2026 | 提出 **action-level causal attribution**：用并行反事实测试判定工具调用由"用户意图"还是"不可信观测"驱动，批评既有防御困于 input-level semantic discrimination 而无法泛化到 unseen payload [74] | 置信度中 |
| 2 | IPIGuard | 2025 | 用**工具依赖图（Tool Dependency Graph）** 对 Agent 行为施加结构性约束，明确批评检测式防御"fundamentally rely on assumptions about the model's inherent security" [71] | 置信度中 |
| 3 | Architecting Secure AI Agents | 2026 | Position paper：主张系统级防御，允许 LLM 参与安全决策但**严格限制其可见与可决策范围**；作者含 IPI 早期奠基作者 Kai Greshake [72] | 置信度中 |
| 4 | WebInject | 2025 | 把提示注入从文本域推进到**渲染像素域**，将扰动求解形式化为不可微映射下的优化问题，训练神经网络近似映射以回传梯度 [70] | 置信度中 |
| 5 | S²F | 2026 | 混合测试（fuzzing + 符号执行 + sampling）集成框架，指出 SOTA 混合工具因使用定制符号执行引擎而未充分利用能力 [93] | 置信度低（仅截断摘要） |
| 6 | 符号执行实践综述 | 2025 | 以路径爆炸为核心瓶颈，给出 Scope Reduction / Guidance Heuristics 双分支 taxonomy，覆盖漏洞、恶意软件、固件、协议四类应用 [91] | 置信度中 |
| 7 | SBOM 工具生态实证 | 2025–2026 | SPDX 与 CycloneDX 工具生态对比 [3]；GitHub SBOM 完整性与一致性大规模研究 [53]；标准与工具 adherence gap 实证 [58]；异构 SBOM 整合框架 [57] | 置信度低（多为 cs.SE 预印本） |
| 8 | 依赖混淆的结构性防御 | 2026 | 指出所有既有防御均为 configuration-based 且配置错误时静默失效，提出密码学分发溯源 [20]；ConfuGuard 用元数据大规模检测包混淆 [21] | 置信度低 |
| 9 | PQC 迁移工程化 | 2026 | ML-DSA/SLH-DSA 在 TLS 1.3 证书层级中的**位置效应**实验 [96]；ML-KEM/ML-DSA 在 ARM Cortex-M0+（RP2040）上的首次隔离算法级基准 [99] | 置信度低 |
| 10 | 编码 Agent 迁移 PQC | 2025 | 提出 contract-based 任务，把 Go 文件签名器从 RSA 迁移到 ML-DSA-44，对比有无结构化检查的编码 Agent 表现 [100] | 置信度低 |

**四类证据示例（进展 1–4 合并）**
- **热度证据**：> 待核实 —— 候选块对 [70][71][72][74] 均未提供引用数或 star；[70] 标注为 v4、[74] 标注为 v2，仅能反映修订迭代 [70][74]。
- **权威证据**：四条均为 arXiv 预印本（cs.CR / cs.LG），**非同行评审**；[72] 作者含 Kai Greshake、Chaowei Xiao、G. Edward Suh [72]。
- **关注度**：中 —— [70] 2025-05 首发、2025-10-17 更新至 v4 [70]；[74] v1→v2 修订 [74]；依据是版本迭代频率，而非引用/榜单。
- **推荐度**：★★★★☆ —— 这四条共同定义"Agent 时代安全边界迁移"这一主线，是当前最值得精读的一组 [70][71][72][74]。

---

## 二、Web / 系统 / 供应链攻防

### 2.1 结构性缺陷：从"事件复盘"到"设计属性"

SoK 类工作尝试把软件供应链安全从个案复盘中提炼出**安全设计属性** [7]，这标志着该方向从"讲故事"走向"可验证属性"。但需注意：SolarWinds、Log4Shell、XZ Utils 三大事件本身**未出现在本批可引用证据中**，其细节属于本轮检索缺口 —— `> 待核实`。

### 2.2 SBOM：从"生成"到"可信"

- **格式与工具**：SPDX 与 CycloneDX 是两大主导格式，其实用价值取决于生成/分析/管理工具生态 [3]。
- **质量危机**：大规模研究显示 GitHub 上的 SBOM 存在**完整性与一致性**问题 [53]；标准与工具之间存在**adherence gap**（工具输出缺失或仅部分填充 SPDX 定义字段）[58]；异构 SBOM 需要专门整合框架 [57]。
- **生成器差异会影响漏洞评估结论**：Python 生态的 SBOM 生成器对比研究指出不同生成器会导向不同漏洞评估结果 [59]；另有工作专门构建 SBOM 数据集以评估消费工具 [56]。

### 2.3 依赖混淆 / 仿冒包 / AI 引入的新型供应链风险

- **依赖混淆**：密码学注册表溯源方案指出结构性缺口 —— "包一旦安装，就没有密码学证明它是哪个 registry 分发的"，且既有防御全部是 configuration-based、配置错误即静默失效 [20]。ConfuGuard 用元数据大规模检测主动与隐蔽的包混淆攻击 [21]。早期经典工作 SpellBound 针对 typosquatting [22]。
- **AI 诱导供应链风险（新）**：系统综述覆盖 **package hallucination** 与 **slopsquatting**（攻击者抢注 LLM 幻觉出的包名）[23]；该文热度标注为 `citations=0`，属极新、尚未形成引用积累的方向 [23]。另有工作分析 NPM/PyPI/Docker Hub 三类生态的攻击面 [24]。

### 2.4 系统与垂直领域

- 车载：对软件定义汽车（SDV）的 UniSUF 统一软件更新框架做 ProVerif 形式化安全分析 [8]。
- 电动汽车充电桩：指出充电站供电设备软件是"最脆弱元素"且长期作为攻击面暴露 [12]。

### 2.5 标准基线（经典/种子）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| SoK: Software Supply Chain Security | 2024 | arXiv cs.CR [7] | > 待核实 | arXiv 预印本（非同行评审）[7] | 中（供应链安全体系化梳理）[7] | ★★★★☆ 建立安全设计属性视角，适合作为供应链章节骨架 [7] | http://arxiv.org/abs/2406.10109v1 | 供应链安全设计属性 SoK |
| OWASP Top 10 (Web & LLM) | 2021 / 2025 | OWASP | > 待核实 | 行业权威官方清单（非论文） | 高（Web 与 LLM 应用风险事实基线） | ★★★★★ 入门与合规必读基线 | https://owasp.org/www-project-top-ten/ | Web 与 LLM 应用风险清单 |
| CWE (Common Weakness Enumeration) | ongoing | MITRE | > 待核实 | 官方标准 | 高（弱点分类事实标准） | ★★★★★ 漏洞分类与标注的通用语言 | https://cwe.mitre.org/ | 弱点分类标准 |
| CWE Top 25 | ongoing | MITRE | > 待核实 | 官方排行 | 高（最危险弱点年度排行） | ★★★★☆ 优先级排序依据 | https://cwe.mitre.org/top25/ | 弱点排行 |
| NVD / CVE | ongoing | NIST | > 待核实 | 官方数据库 | 高（漏洞编号与缺陷事实源） | ★★★★★ 所有漏洞研究的数据底座 | https://nvd.nist.gov/ | 漏洞数据库 |

> 注：以上四条种子资源的引用数/访问量/榜单排名在本轮**未实时检索**，故热度一律 `> 待核实`。

---

## 三、模糊测试与程序分析

### 3.1 最新进展（近 1–2 年）

- **符号执行工程化**：2025 年综述将实用化策略归纳为两大类 —— **Scope Reduction**（把符号执行范围收缩到可管理代码片段）与 **Guidance Heuristics**（引导引擎走向有希望路径），覆盖漏洞、恶意软件、固件、协议分析 [91]。
- **混合测试集成化**：S²F 主张 fuzzing + 符号执行 + sampling 三者集成优于单一技术，并指出 SOTA 混合工具"在两个关键方面未充分利用符号执行与采样的能力"，症结在于其使用**定制的符号执行引擎** [93]。⚠️ 该条目仅有截断摘要，"优于单一技术"目前只到**作者宣称**层级，benchmark、基线与提升幅度均不可核实。
- **LLM 辅助输入生成**：低成本、面向**非文本输入**的 fuzzing 通过 LLM 合成输入生成器实现 [85] —— 这填补了"LLM 辅助 fuzzing"在此前抽取中的证据缺口。
- **LLM/多智能体 harness 生成**：覆盖引导的多智能体方法为 **Java 库 fuzzing** 自动生成 fuzz harness，解决"手工 harness 编写耗时且需深入理解 API 语义"的痛点 [32]；Prompt Fuzzing 用于 **fuzz driver 生成** [35]。
- **覆盖率引导 fuzzing 的理论侧**：FOX 把覆盖引导 fuzzing 建模为**在线随机控制**问题 [49]；CovRL 用覆盖引导强化学习驱动 LLM 变异，针对 JavaScript 引擎 [52]。
- **二进制与硬件侧**：`cozy` 面向二进制程序的**比较式符号执行** [60]；Binary BPE 提供跨平台二进制分析分词器族 [67]；CveBinarySheet 构建面向 IoT 漏洞分析的大规模预编译二进制数据库 [64]；覆盖率引导的**pre-silicon fuzzing** 结合泄漏契约（leakage contracts）验证开源处理器的侧信道保证 [51]。
- **AI 修漏洞闭环**：OSS-Fuzz 场景下用 AI 修复安全漏洞 [34]；AutoPatch 用多智能体框架修补真实 CVE [42]；早期 SyzScope 揭示 fuzzer 暴露 bug 的**高风险安全影响**（把"崩溃"升级为可利用性判断）[9]。

### 3.2 经典与奠基性工作

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Evaluating the Fork-Awareness of Coverage-Guided Fuzzers | 2023 | arXiv cs.CR [50] | > 待核实 | arXiv 预印本，未标 venue [50] | 低（已非前沿）[50] | ★★★☆☆ 覆盖反馈可信度（fork 语义/插桩失真）的经典边界问题 [50] | http://arxiv.org/abs/2301.05060v1 | 覆盖引导 fuzzer 的 fork 感知评估 |
| An Exploratory Survey of Hybrid Testing (Symbolic Execution + Fuzzing) | 2017 | arXiv [90] | > 待核实 | arXiv 预印本 [90] | 低（历史脉络价值）[90] | ★★★☆☆ 混合测试的早期综述，用于建立演进起点 [90] | http://arxiv.org/abs/1712.06843v1 | 混合测试早期综述 |
| Improving Function Coverage with Munch | 2017 | arXiv [92] | > 待核实 | arXiv 预印本 [92] | 低 [92] | ★★★☆☆ 混合 fuzzing + 定向符号执行的代表早期工作 [92] | http://arxiv.org/abs/1711.09362v2 | 混合模糊测试早期方法 |
| Badger: Complexity Analysis with Fuzzing and Symbolic Execution | 2018 | arXiv [95] | > 待核实 | arXiv 预印本 [95] | 低 [95] | ★★★☆☆ 展示 fuzzing+符号执行在复杂度分析上的组合用法 [95] | http://arxiv.org/abs/1806.03283v1 | 复杂度分析 |
| Full-speed Fuzzing | 2018 | arXiv [46] | > 待核实 | arXiv 预印本 [46] | 低 [46] | ★★★☆☆ 覆盖率引导追踪降低 fuzzing 开销的早期方案 [46] | http://arxiv.org/abs/1812.11875v2 | 降低 fuzzing 开销 |
| SyzScope | 2021 | arXiv [9] | > 待核实 | arXiv 预印本 [9] | 中（Linux kernel fuzzing 影响评估）[9] | ★★★★☆ 把"崩溃"升级为"高风险可利用性"的关键思路 [9] | http://arxiv.org/abs/2111.06002v1 | 揭示 fuzzer 暴露 bug 的安全影响 |
| Industry Practice of Coverage-Guided Enterprise-Level DBMS Fuzzing | 2021 | arXiv [47] | > 待核实 | arXiv 预印本 [47] | 低 [47] | ★★★☆☆ 工业级 DBMS fuzzing 实践参考 [47] | http://arxiv.org/abs/2103.00804v1 | 企业级 DBMS fuzzing |
| Same Coverage, Less Bloat | 2022 | arXiv [48] | > 待核实 | arXiv 预印本 [48] | 低 [48] | ★★★☆☆ 仅二进制场景下的覆盖率保持型追踪 [48] | http://arxiv.org/abs/2209.03441v1 | 加速 binary-only fuzzing |
| An Empirical Study of OSS-Fuzz Bugs | 2021 | arXiv [30] | > 待核实 | arXiv 预印本 [30] | 中 [30] | ★★★★☆ OSS-Fuzz 缺陷分布的经验事实来源 [30] | http://arxiv.org/abs/2103.11518v1 | OSS-Fuzz 缺陷实证 |
| What Happens When We Fuzz? | 2023 | arXiv [31] | > 待核实 | arXiv 预印本 [31] | 低 [31] | ★★★☆☆ 追踪 OSS-Fuzz bug 生命周期 [31] | http://arxiv.org/abs/2305.11433v1 | OSS-Fuzz bug 历史 |

### 3.3 开源项目与工具链（种子资源）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| AFL++ | ongoing | Google / 社区 | > 待核实（未实时检索 star） | 官方 GitHub 仓库 | 高（覆盖引导 fuzzing 事实标准之一） | ★★★★★ 覆盖率引导模糊测试首选工程底座 | https://github.com/AFLplusplus/AFLplusplus | 覆盖率引导模糊测试 |
| oss-fuzz | ongoing | Google | > 待核实 | 官方 GitHub 仓库 | 高（持续模糊测试基础设施） | ★★★★★ 大规模持续 fuzzing 的事实基础设施 | https://github.com/google/oss-fuzz | 持续模糊测试基础设施 |
| angr | ongoing | angr 社区 | > 待核实 | 官方 GitHub 仓库 | 高（二进制符号执行常用框架） | ★★★★★ 二进制符号执行与程序分析首选 | https://github.com/angr/angr | 二进制符号执行框架 |
| Semgrep | ongoing | Semgrep / Trail of Bits 生态 | > 待核实 | 官方 GitHub 仓库 | 高（SAST 广泛使用） | ★★★★★ 轻量静态分析（SAST）工程实践 | https://github.com/semgrep/semgrep | 静态分析 |
| sigstore | ongoing | OpenSSF / sigstore 社区 | > 待核实 | 官方 GitHub 仓库 | 高（软件供应链签名事实标准之一） | ★★★★★ 供应链签名与来源证明工程实践 | https://github.com/sigstore/sigstore | 软件供应链签名 |
| Magma | 2020 | 学术团队 [37] | > 待核实 | 开源 ground-truth fuzzing benchmark [37] | 中（fuzzer 统一评测的常用基准）[37][36] | ★★★★☆ 模糊测试横向评测的基准选择 | http://arxiv.org/abs/2009.01120v2 | Ground-truth fuzzing benchmark |

> **说明**：所有 GitHub star / 贡献者活跃度 / 最近提交时间在本轮**未实时检索**，故热度列一律 `> 待核实`，不得据此声称"最活跃"。

---

## 四、大模型与 Agent 安全（提示注入 / 越狱 / 数据外泄）

### 4.1 提示注入的攻击面演进（时间线）

1. **2024 — 早期防御与前缀攻击**：StruQ 提出**结构化查询（structured queries）** 把指令与数据分离以抵御提示注入 [69]；SecAlign 用**偏好优化（preference optimization）** 训练模型抵抗注入 [68]；Automatic and Universal Prompt Injection Attacks 给出自动化通用注入攻击 [77]。AgentDojo 提供动态环境以评测 Agent 的注入攻击与防御 [76]。
2. **2025 — 攻击面横向扩展**：
   - **多模态/像素级**：WebInject 针对依据网页截图生成动作的 MLLM Web Agent，向**原始像素值**加扰动，经映射后进入截图并诱导 Agent 执行攻击者指定动作；因像素→截图映射不可微，训练神经网络近似以回传梯度 [70]。
   - **防御侧两条平行路线**：IPIGuard 用**工具依赖图**做结构性约束 [71]；多智能体流水线用专门化 LLM Agent 协同**实时**检测与中和注入 [75]；传统分类器路线基于 HackAPrompt Playground Submissions 语料扩增数据集，训练 LSTM/FFNN/Random Forest/Naive Bayes 检测器 [78]。
   - **防御被自适应攻击击穿**：Adaptive Attacks Break Defenses Against IPI on LLM Agents 直接针对"防御易被绕过"这一问题 [73]。
3. **2026 — 范式转移**：
   - **动作级因果归因**：AttriGuard 批评既有防御把 IPI 当作 input-level semantic discrimination problem、无法泛化到 unseen payloads，转而判定工具调用是由**用户意图支撑**还是由**不可信观测因果驱动**，运行时用并行反事实测试验证每个候选调用 [74]。
   - **系统级架构**：position paper 主张把安全决策限制在严格受限的可见/可决策范围内，并承认动态重规划与安全策略更新在真实环境中的必要性 [72]。

### 4.2 越狱（Jailbreak）与护栏绕过（Guardrail Bypass）

- **自我防御愿景**：LLMs Can Defend Themselves Against Jailbreaking in a Practical Manner（vision paper）[79]。
- **人格化攻击**：persona prompts 被用于增强越狱攻击效果 [80]。
- **主动防御**：Proactive defense against LLM Jailbreak [81]。
- **护栏绕过实证**：针对**提示注入与越狱检测系统**的规避攻击做了经验分析 [82]。
- **攻防统一建模**：CAVGAN 在 LLM 内部表征上以生成对抗方式统一越狱与防御 [84]。

> **关键缺口**：本批证据中**没有一条给出量化的攻击成功率（ASR）或防御成功率**，也没有统一的越狱评测榜单。因此"哪个防御更强"在本轮**无法排序** —— `> 待核实`。

### 4.3 经典与前沿工作表

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| StruQ: Defending Against Prompt Injection with Structured Queries | 2024 | arXiv cs.CR [69] | > 待核实 | arXiv 预印本 [69] | 中（结构化查询防御代表）[69] | ★★★★★ 指令/数据分离思想的奠定性防御 [69] | http://arxiv.org/abs/2402.06363v2 | 结构化查询防御 |
| SecAlign: Defending Against Prompt Injection with Preference Optimization | 2024 | arXiv [68] | > 待核实 | arXiv 预印本 [68] | 中（偏好优化防御代表）[68] | ★★★★☆ 训练侧对齐防御的代表 [68] | http://arxiv.org/abs/2410.05451v3 | 偏好优化防御 |
| AgentDojo | 2024 | arXiv [76] | > 待核实 | arXiv 预印本 [76] | 中（Agent 注入评测环境）[76] | ★★★★★ Agent 注入攻防的动态评测基准 [76] | http://arxiv.org/abs/2406.13352v3 | Agent 注入评测环境 |
| Automatic and Universal Prompt Injection Attacks | 2024 | arXiv [77] | > 待核实 | arXiv 预印本 [77] | 中 [77] | ★★★★☆ 自动化通用注入攻击代表 [77] | http://arxiv.org/abs/2403.04957v1 | 自动化注入攻击 |
| WebInject | 2025 | Shuyan Zhou, Neil Zhenqiang Gong 等 [70] | > 待核实（v4 迭代）[70] | arXiv cs.LG 预印本，非同行评审 [70] | 中（v1→v4 多次修订）[70] | ★★★★☆ 多模态/Web Agent 攻击侧必读 [70] | http://arxiv.org/abs/2505.11717v4 | 像素级提示注入 |
| IPIGuard | 2025 | 含 Shouling Ji [71] | > 待核实 [71] | arXiv cs.CR v1 预印本 [71] | 中（结构约束流派代表）[71] | ★★★★☆ 与检测式防御正交的结构化思路 [71] | http://arxiv.org/abs/2508.15310v1 | 工具依赖图防御 |
| AttriGuard | 2026 | arXiv cs.CR [74] | > 待核实（v2 迭代）[74] | arXiv cs.CR v2 预印本 [74] | 中（v1→v2 修订）[74] | ★★★★☆ 输入级→动作级归因的范式节点 [74] | http://arxiv.org/abs/2603.10749v2 | 因果归因防御 |
| Architecting Secure AI Agents | 2026 | 含 Kai Greshake, Chaowei Xiao, G. Edward Suh [72] | > 待核实 [72] | arXiv position paper [72] | 中（衔接 IPI 奠基作者）[72] | ★★★★☆ 系统级防御设计清单 [72] | http://arxiv.org/abs/2603.30016v1 | 系统级防御观点文 |
| Adaptive Attacks Break Defenses Against IPI | 2025 | arXiv [73] | > 待核实 [73] | arXiv v2 预印本 [73] | 中（直击防御鲁棒性）[73] | ★★★★☆ 评估任何 IPI 防御时的对抗基线 [73] | http://arxiv.org/abs/2503.00061v2 | 自适应攻击 |
| Bypassing LLM Guardrails | 2025 | arXiv [82] | > 待核实（v3 迭代）[82] | arXiv v3 预印本 [82] | 中 [82] | ★★★★☆ 护栏绕过（检测系统规避）的关键实证 [82] | http://arxiv.org/abs/2504.11168v3 | 护栏规避攻击 |
| CAVGAN | 2025 | arXiv [84] | > 待核实 [84] | arXiv v2 预印本 [84] | 中 [84] | ★★★☆☆ 越狱与防御的统一生成对抗建模 [84] | http://arxiv.org/abs/2507.06043v2 | 越狱-防御统一 |
| Persona Prompts for Jailbreak | 2025 | arXiv [80] | > 待核实（v3 迭代）[80] | arXiv v3 预印本 [80] | 中 [80] | ★★★☆☆ 人格化提示攻击线索 [80] | http://arxiv.org/abs/2507.22171v3 | 人格化越狱 |
| Proactive Defense against LLM Jailbreak | 2025 | arXiv [81] | > 待核实（v2 迭代）[81] | arXiv v2 预印本 [81] | 中 [81] | ★★★☆☆ 主动式越狱防御 [81] | http://arxiv.org/abs/2510.05052v2 | 主动防御 |
| Detecting Prompt Injection with Classifiers | 2025 | arXiv [78] | > 待核实 [78] | arXiv cs.CR v1 预印本 [78] | 低（无指标、无热度）[78] | ★★★☆☆ 检测数据集线索 [78] | http://arxiv.org/abs/2512.12583v1 | 分类器检测 |
| A Multi-Agent LLM Defense Pipeline | 2025 | arXiv [75] | > 待核实（v4 迭代）[75] | arXiv cs.CR v4 预印本 [75] | 中（迭代至 v4）[75] | ★★★☆☆ "用 Agent 防 Agent"的工程形态 [75] | http://arxiv.org/abs/2509.14285v4 | 多智能体防御 |

> **跨领域注记**：[2] The 2025 Foundation Model Transparency Index 反复出现在本批供应链/密码学子问题中，但其内容实为**基础模型透明度治理**，与 SBOM 或 PQC **无直接关系**，属检索噪声；仅建议作为"AI 治理透明度"参照，不纳入本报告五大方向的论证链 [2]。

---

## 五、密码学与后量子迁移

### 5.1 标准与算法综述（经典/背景）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Post-Quantum Cryptography: A Systematic Review of Algorithms, Standardization, Challenges | 2026 | SSRN [115] | > 待核实 | SSRN 预印本（非同行评审）[115] | 中（标准化全景）[115] | ★★★★☆ 算法/标准化/挑战的系统梳理 [115] | https://doi.org/10.2139/ssrn.7128678 | PQC 系统综述 |
| Post-Quantum Cryptography and Quantum-Safe Security: A Comprehensive Survey | 2025 | arXiv [116] | > 待核实 | arXiv 预印本 [116] | 中（综合综述）[116] | ★★★★☆ 量子安全全景综述 [116] | http://arxiv.org/abs/2510.10436 | PQC 综合综述 |
| MFKDF: Multi-Factor Key Derivation Function | 2022 | arXiv [13] | > 待核实 | arXiv v3 预印本 [13] | 低 [13] | ★★★☆☆ 密钥管理工程实践的经典旁支 [13] | http://arxiv.org/abs/2208.05586v3 | 多因素密钥派生 |
| Branch Shadowing（侧信道经典） | 2017 | USENIX Security | > 待核实 | **同行评审顶会（A 级）** | 中（侧信道经典） | ★★★★★ 侧信道方向必读奠基工作 | https://www.usenix.org/conference/usenixsecurity17 | 侧信道经典（示例性 A 级来源） |

> ⚠️ **重要纪律**：本轮证据中，**ML-KEM（FIPS 203）/ ML-DSA（FIPS 204）/ SLH-DSA（FIPS 205）的实现层侧信道与故障注入攻击论文未被检索到**。这意味着"实现层攻击"这一维度在本批证据中为**空白**，需补充检索后方可下结论 —— `> 待核实`。

### 5.2 迁移工程与测量（近 1–2 年最新进展）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Signature Placement in PQ TLS Certificate Hierarchies | 2026 | arXiv cs.CR [96] | > 待核实（v3 迭代）[96] | arXiv v3 预印本 [96] | 中（v1→v3 说明迭代）[96] | ★★★★★ 回答"签名放在证书层级哪一层"的实操问题 [96] | http://arxiv.org/abs/2604.06100v3 | ML-DSA/SLH-DSA 在 TLS 1.3 的位置效应 |
| Benchmarking ML-KEM and ML-DSA on ARM Cortex-M0+ (RP2040) | 2026 | arXiv cs.CR [99] | > 待核实（迭代至 v6）[99] | arXiv v6 预印本；自称首个隔离算法级基准 [99] | 中—高（v6 多次迭代）[99] | ★★★★★ 资源受限 IoT 迁移的关键实测数据 [99] | http://arxiv.org/abs/2603.19340v6 | 延迟/拒绝采样方差/内存 |
| Mind the Gap: Policy vs Reality in PQ TLS Deployment | 2026 | arXiv [110] | > 待核实 [110] | arXiv 预印本 [110] | 中（政策-现实落差）[110] | ★★★★★ 迁移落地现实检视，避免纸面合规 [110] | http://arxiv.org/abs/2607.29005v1 | PQ TLS 部署的政策落差 |
| Measurement Study of Post-Quantum Readiness of Internet: 2026 | 2026 | arXiv [107] | > 待核实 [107] | arXiv 预印本 [107] | 中（互联网级测量）[107] | ★★★★★ 全局 readiness 基线测量 [107] | http://arxiv.org/abs/2606.16473v1 | 互联网 PQC 就绪度测量 |
| Layered Performance Analysis of TLS 1.3 Handshakes | 2026 | arXiv [112] | > 待核实（v2）[112] | arXiv v2 预印本 [112] | 中 [112] | ★★★★☆ 经典/混合/纯 PQ 密钥交换的分层性能对比 [112] | http://arxiv.org/abs/2603.11006v2 | 握手性能分层分析 |
| Quantum-Ready Secure WAN | 2026 | arXiv cs.CR [98] | > 待核实 [98] | arXiv 预印本 [98] | 中（企业 WAN 迁移框架）[98] | ★★★★☆ 企业级迁移风险评估框架；含 harvest-now-decrypt-later 威胁 [98] | http://arxiv.org/abs/2609.26225v1 | WAN 迁移框架 |
| Towards PQ Secure Pharmacovigilance with ML-KEM and ML-DSA | 2026 | arXiv cs.CR [97] | > 待核实 [97] | arXiv 预印本 [97] | 低（垂直行业）[97] | ★★★☆☆ 行业迁移案例 [97] | http://arxiv.org/abs/2606.09412v1 | 药物警戒场景迁移 |
| From Public-Key Linting to Operational PQ X.509 Assurance | 2026 | arXiv [104] | > 待核实（v2）[104] | arXiv v2 预印本 [104] | 中 [104] | ★★★★☆ 注册表驱动策略 + 变异评估 + 导入校验的工程闭环 [104] | http://arxiv.org/abs/2604.17003v2 | X.509 PQC 保障 |
| Can Coding Agents Migrate to Post-Quantum Cryptography? | 2025 | arXiv cs.MA [100] | > 待核实（v3）[100] | arXiv v3 预印本 [100] | 中 [100] | ★★★★☆ Agent 自动化密码迁移的契约式评测设计 [100] | http://arxiv.org/abs/2512.12989v3 | 编码 Agent 迁移 PQC |
| A Non-Invasive Cloud-Based Migration Strategy for PQ in Smart HVAC | 2026 | arXiv [101] | > 待核实 [101] | arXiv 预印本 [101] | 低（楼宇场景）[101] | ★★☆☆☆ 垂直场景参考 [101] | http://arxiv.org/abs/2609.27828v1 | 智能 HVAC 迁移 |
| Active TLS Stack Fingerprinting | 2022 | arXiv [114] | > 待核实（v3）[114] | arXiv v3 预印本 [114] | 低 [114] | ★★★☆☆ 大规模 TLS 部署刻画方法，可复用于迁移测量 [114] | http://arxiv.org/abs/2206.13230v3 | TLS 指纹测量 |

**开源/工程线索（未核实维护状态）**：Zenodo 上存在若干 PQC 迁移模拟器与统一引擎条目 [103][105][106][108]，以及政策类评估 [111][113]。这些条目的**代码质量、许可、维护活跃度在本轮均未核实** —— `> 待核实`，不建议在未见仓库活跃度前直接用于生产。

---

## 六、数据集、基准与红蓝对抗

### 6.1 数据集与基准表

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| CVE-Bench | 2025 | arXiv [44] | > 待核实（v4 迭代）[44] | arXiv v4 预印本 [44] | 中—高（AI Agent 真实漏洞利用评测）[44] | ★★★★★ 红队（AI Agent 攻真实 Web 应用）的核心基准 [44] | http://arxiv.org/abs/2503.17332v4 | AI Agent 利用真实 Web 漏洞能力基准 |
| AgentDojo | 2024 | arXiv [76] | > 待核实 | arXiv 预印本 [76] | 中 [76] | ★★★★★ Agent 提示注入攻防动态评测环境 [76] | http://arxiv.org/abs/2406.13352v3 | 动态攻防评测环境 |
| SecBench | 2024 | arXiv [25] | > 待核实（v3）[25] | arXiv v3 预印本 [25] | 中（LLM 网络安全多维基准）[25] | ★★★★★ LLM 安全能力多维评测数据集 [25] | http://arxiv.org/abs/2412.20787v3 | LLM 网络安全基准 |
| CYBERSECEVAL 3 | 2024 | arXiv [26] | > 待核实（v2）[26] | arXiv v2 预印本；Meta 系评测线 [26] | 中—高（LLM 网络安全风险与能力评测）[26] | ★★★★★ LLM 安全风险评测主线之一 [26] | http://arxiv.org/abs/2408.01605v2 | LLM 网络安全风险评测 |
| Purple Llama CyberSecEval | 2023 | arXiv [29] | > 待核实 | arXiv 预印本（CyberSecEval 起点）[29] | 中（安全编码基准奠基）[29] | ★★★★☆ CyberSecEval 谱系的奠基文档 [29] | http://arxiv.org/abs/2312.04724v1 | 安全编码基准 |
| Rethinking CyberSecEval | 2024 | arXiv [28] | > 待核实 | arXiv 预印本 [28] | 中（对基准本身的批判）[28] | ★★★★☆ 评测口径批判，直接对应"基准争议"[28] | http://arxiv.org/abs/2411.08813v1 | LLM 辅助的评测批判 |
| Magma | 2020 | 学术团队 [37] | > 待核实 | 开源 ground-truth benchmark，原论文 ACM SIGMETRICS 2021 [36][37] | 中—高（fuzzer 统一评测常用）[36][37] | ★★★★★ fuzzer 横向对比的基准首选 [37] | http://arxiv.org/abs/2009.01120v2 | Ground-truth fuzzing benchmark |
| The Impact of Magma | 2026 | arXiv cs.CR [36] | > 待核实 [36] | arXiv 预印本 [36] | 中（基准影响力回顾）[36] | ★★★★☆ Magma 的动机、设计与影响总结 [36] | http://arxiv.org/abs/2608.28016v1 | Magma 影响回顾 |
| SBOM 数据集（评估消费工具） | 2025 | arXiv [56] | > 待核实 | arXiv 预印本 [56] | 中（SBOM 消费工具评测数据）[56] | ★★★★☆ 评估 SBOM 消费工具的数据集 [56] | http://arxiv.org/abs/2504.06880v1 | SBOM 评测数据集 |
| CveBinarySheet | 2025 | arXiv [64] | > 待核实 | arXiv 预印本 [64] | 中（IoT 漏洞分析预编译二进制库）[64] | ★★★★☆ IoT 二进制漏洞分析数据底座 [64] | http://arxiv.org/abs/2501.08840v1 | IoT 预编译二进制数据库 |
| NVD / CVE | ongoing | NIST | > 待核实 | 官方数据库 | 高 | ★★★★★ 通用漏洞语料底座 | https://nvd.nist.gov/ | 漏洞数据库 |
| CVEfixes / Big-Vul | ongoing | secureIT-project | > 待核实 | 开源数据集仓库 | 中（漏洞修复语料常用） | ★★★★☆ 修复型漏洞数据集 | https://github.com/secureIT-project/CVEfixes | 漏洞修复数据集 |
| CWE Top 25 | ongoing | MITRE | > 待核实 | 官方排行 | 高 | ★★★★☆ 弱点优先级依据 | https://cwe.mitre.org/top25/ | 弱点排行 |

### 6.2 红蓝对抗的"评测基础设施"缺口

- **CVE → CWE 自动映射**：将 CVE 记录映射到 MITRE CWE 弱点，是连接"漏洞库"与"弱点分类"的桥梁 [41]。
- **自动化修补**：AutoPatch 用多智能体框架修补真实 CVE [42]；OSS-Fuzz 上以 AI 修复安全漏洞 [34] —— 这两者构成"红队发现 → 蓝队修补"闭环的另一半。
- **对抗性评测警示**：Adaptive Attacks 表明防御在**自适应对手**下会被击穿 [73]，而 Bypassing LLM Guardrails 表明**检测系统本身**可被规避 [82]。因此任何"防御有效率"数字都必须标注是否针对自适应攻击 —— 这是本报告的**核心评测纪律建议**。

> **口径不一的具体证据**：SBOM 方向多项研究显示不同**生成工具**会导致不同字段填充与不同漏洞评估结果 [58][59]，即"同一软件、不同工具、不同结论"。这是"评测口径不一"在供应链领域最明确的一手证据。

---

## 七、争议与开放问题

1. **防御评测缺乏统一基准与自适应攻击口径**。
   IPIGuard [71]、AttriGuard [74]、多智能体流水线 [75]、分类器检测 [78]、SecAlign [68]、StruQ [69] 各自在不同设定下报告效果，**本批证据未提供任何统一 benchmark 上的可比数字**；而 Adaptive Attacks 已证明自适应对手可击穿既有防御 [73]。→ **争议点：现有"防御有效"的宣称普遍缺乏自适应攻击下的验证**。`> 待核实`：本批证据中无任何 ASR/防御率数字。

2. **结构约束 vs. 语义检测 vs. 动作归因，三条路线谁更可扩展？**
   结构约束派批评检测派"依赖模型固有安全性假设" [71]；归因派批评检测派"无法泛化到 unseen payloads" [74]；系统级观点派主张限制模型可见/可决策范围 [72]。**三条路线之间没有交叉评测**。→ 开放问题。

3. **多模态攻击面（像素级注入）尚无对应防御**。
   WebInject 已展示像素域注入可行 [70]，但本批证据中**未见任何针对像素级/多模态注入的防御工作**。→ 明确的攻防不对称缺口。`> 待核实`。

4. **符号执行的路径爆炸仍无通用解**。
   综述将其归为 Scope Reduction 与 Guidance Heuristics 两类策略 [91]，但**两类策略各自的适用边界与代价未在候选证据中量化对比**。S²F 声称混合集成更优，但仅有截断摘要支撑，属**作者宣称层级** [93]。→ 开放问题。

5. **SBOM 的"合规≠安全"**。
   多项实证显示 SBOM 存在完整性/一致性缺陷 [53]、标准-工具落差 [58]、工具间结果分歧 [59]。→ **争议点：把 SBOM 当作合规交付物而非安全工程产物**。另有研究指出既有依赖混淆防御"全部是配置式、配置错误即静默失效" [20]，说明**流程性控制不可靠**。

6. **AI 自身成为供应链风险源**。
   package hallucination 与 slopsquatting 把 LLM 幻觉直接转化为供应链攻击面 [23]，但该文 `citations=0`、尚属极新方向，**缺乏独立复现与量化影响评估**。`> 待核实`。

7. **后量子迁移的"纸面合规 vs 实际部署"落差**。
   Mind the Gap 直接以"政策 vs 现实"为题 [110]，且有互联网级 readiness 测量 [107] 与签名位置效应实验 [96] 佐证迁移的工程复杂性。→ **争议点：是否存在"宣布 PQC-ready 但实际未端到端迁移"的普遍现象**。

8. **实现层侧信道/故障注入证据缺失**。
   ML-KEM/ML-DSA/SLH-DSA 的**实现层攻击**在本批证据中**未被覆盖** —— 这是本轮最大的方向性缺口。`> 待核实`。

9. **证据等级整体偏低**。
   本报告引用的核心论文几乎全部为 **arXiv 预印本 / SSRN / Zenodo**，仅 [13] 相关的 USENIX Security 侧信道经典为明确 A 级同行评审来源。→ **元结论：本报告所有"前沿"结论均应按"中高可信度预印本"对待，不宜直接作为采购或合规依据**。

10. **检索噪声问题**。
    本批候选来源中混入大量与网络安全无关的条目（如短视频观看量预测 [1]、图像超分挑战 [4][38]、语音隐私 [15]、天体物理 [16][17][61][62][63][65][66]、德语问卷编码 [83] 等）。→ 提示自动化检索管线的**领域过滤**需要加强；本报告已剔除，不用作任何论断。

---

## 八、建议关注清单（Watchlist）

**优先级 P0（立刻跟踪，直接决定架构选型）**
1. **Agent 工具调用安全的范式之争**：AttriGuard（动作级因果归因）[74] vs IPIGuard（工具依赖图结构约束）[71] vs 系统级防御观点 [72]。**跟踪信号**：是否出现三者在同一 benchmark 上的对比 —— `> 待核实` 目前无此实验。
2. **AgentDojo [76] 与 CVE-Bench [44]**：前者是注入攻防动态环境，后者是 AI Agent 攻击真实 Web 应用的能力基准。**建议**：把这两个基准作为内部 Agent 安全回归测试的起点。
3. **Adaptive Attacks [73] 作为"防御验收门槛"**：任何新防御方案上线前，应先在自适应攻击设定下评估。

**优先级 P1（中期跟踪，影响工程栈）**
4. **Magma 基准 [37][36] + AFL++ / oss-fuzz 工程链**（含 [30][31] 的 OSS-Fuzz 实证），用于构建可复现的 fuzzing 评测流程。
5. **LLM 辅助 harness/driver 生成**：[32]（Java 库 fuzz harness 多智能体生成）、[35]（fuzz driver 生成）、[85]（非文本输入生成器）。**跟踪信号**：是否出现跨语言通用方案。
6. **SBOM 质量与工具分歧**：[3]（SPDX vs CycloneDX 工具生态）、[53]（GitHub SBOM 完整性）、[57]（异构 SBOM 整合）、[58]（标准-工具 adherence gap）、[59]（生成器影响漏洞评估）。**建议**：不要只选一个 SBOM 工具，做交叉校验。
7. **依赖混淆的结构性防御**：[20]（密码学注册表溯源）、[21]（ConfuGuard 元数据检测）、[22]（typosquatting 经典）。**跟踪信号**：CI/CD 是否原生集成 provenance 校验。

**优先级 P2（长期跟踪，前瞻布局）**
8. **PQC 迁移的"最后一公里"**：[96]（签名在证书层级中的位置）、[99]（Cortex-M0+/RP2040 实测）、[110]（政策 vs 现实）、[107]（互联网 readiness 测量）、[112]（TLS 1.3 分层性能）、[104]（X.509 保障闭环）。**建议**：优先解决"签名放在哪一层"和"资源受限端能否承载"这两个最具体的工程问题。
9. **编码 Agent 自动化密码迁移**：[100] 的 contract-based 评测设计值得作为内部迁移工具的自测框架。
10. **slopsquatting / package hallucination**：[23] 极新（`citations=0`）。**跟踪信号**：是否出现量化影响研究或注册表侧防御机制。
11. **LLM 安全评测谱系**：SecBench [25] → Purple Llama CyberSecEval [29] → CYBERSECEVAL 3 [26] → Rethinking CyberSecEval [28]。**建议**：使用基准时**同时阅读其对基准本身的批判**，避免把评测分数当作安全能力。
12. **待补检索的空白**：ML-KEM/ML-DSA/SLH-DSA 的**实现层侧信道与故障注入攻击**、**SolarWinds / Log4Shell / XZ Utils 三案的学术复盘文献** —— 本报告均 `> 待核实`，需在下一轮补充检索。

---

## 参考来源

[1] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1
[2] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1
[3] The State of the SBOM Tool Ecosystems: A Comparative Analysis of SPDX and CycloneDX — http://arxiv.org/abs/2512.21781v2
[4] NTIRE 2025 Challenge on Image Super-Resolution (x4): Methods and Results — http://arxiv.org/abs/2504.14582v3
[5] VLSP 2025 MLQA-TSR Challenge: Vietnamese Multimodal Legal Question Answering on Traffic Sign Regulation — http://arxiv.org/abs/2510.20381v1
[6] The AudioMOS Challenge 2025 — http://arxiv.org/abs/2509.01336v1
[7] SoK: Analysis of Software Supply Chain Security by Establishing Secure Design Properties — http://arxiv.org/abs/2406.10109v1
[8] Towards a Formal Verification of Secure Vehicle Software Updates — http://arxiv.org/abs/2511.15479v1
[9] SyzScope: Revealing High-Risk Security Impacts of Fuzzer-Exposed Bugs in Linux kernel — http://arxiv.org/abs/2111.06002v1
[10] Internet Service Providers' and Individuals' Attitudes, Barriers, and Incentives to Secure IoT — http://arxiv.org/abs/2210.02137v1
[11] Software Security Rules, SDLC Perspective — http://arxiv.org/abs/0911.0494v1
[12] Wicked Problem, Parsimonious Solution: Securing Electric Vehicle Charging Station Software — http://arxiv.org/abs/2609.10502v1
[13] Multi-Factor Key Derivation Function (MFKDF) for Fast, Flexible, Secure, & Practical Key Management — http://arxiv.org/abs/2208.05586v3
[14] The Everyday Security of Living with Conflict — http://arxiv.org/abs/2506.09580v1
[15] NTU-NPU System for Voice Privacy 2024 Challenge — http://arxiv.org/abs/2410.02371v1
[16] Discovery Opportunities with Gravitational Waves -- TASI 2024 Lecture Notes — http://arxiv.org/abs/2409.08956v1
[17] Atmospheric entry and fragmentation of small asteroid 2024 BX1 — http://arxiv.org/abs/2403.00634v2
[18] Uncovering Coordinated Cross-Platform Information Operations Threatening the Integrity of the 2024 U.S. Presidential Election Online Discussion — http://arxiv.org/abs/2409.15402v2
[19] Double Multi-Head Attention Multimodal System for Odyssey 2024 Speech Emotion Recognition Challenge — http://arxiv.org/abs/2406.10598v1
[20] Cryptographic Registry Provenance: Structural Defense Against Dependency Confusion in AI Package Ecosystems — http://arxiv.org/abs/2605.03309v2
[21] ConfuGuard: Using Metadata to Detect Active and Stealthy Package Confusion Attacks Accurately and at Scale — http://arxiv.org/abs/2502.20528v3
[22] SpellBound: Defending Against Package Typosquatting — http://arxiv.org/abs/2003.03471v1
[23] AI-Induced Supply-Chain Compromise: A Systematic Review of Package Hallucinations and Slopsquatting Attacks — https://doi.org/10.21203/rs.3.rs-8007192/v1
[24] Supply Chain Attacks Through Open Source Software: A Comprehensive Analysis of NPM, PyPI, and Docker Hub Vulnerabilities — https://doi.org/10.25776/h5ez-vq70
[25] SecBench: A Comprehensive Multi-Dimensional Benchmarking Dataset for LLMs in Cybersecurity — http://arxiv.org/abs/2412.20787v3
[26] CYBERSECEVAL 3: Advancing the Evaluation of Cybersecurity Risks and Capabilities in Large Language Models — http://arxiv.org/abs/2408.01605v2
[27] Annif at SemEval-2025 Task 5: Traditional XMTC augmented by LLMs — http://arxiv.org/abs/2504.19675v2
[28] Rethinking CyberSecEval: An LLM-Aided Approach to Evaluation Critique — http://arxiv.org/abs/2411.08813v1
[29] Purple Llama CyberSecEval: A Secure Coding Benchmark for Language Models — http://arxiv.org/abs/2312.04724v1
[30] An Empirical Study of OSS-Fuzz Bugs — http://arxiv.org/abs/2103.11518v1
[31] What Happens When We Fuzz? Investigating OSS-Fuzz Bug History — http://arxiv.org/abs/2305.11433v1
[32] Coverage-Guided Multi-Agent Harness Generation for Java Library Fuzzing — http://arxiv.org/abs/2603.08616v1
[33] OpenFact at CheckThat! 2024: Combining Multiple Attack Methods for Effective Adversarial Text Generation — http://arxiv.org/abs/2409.02649v2
[34] Fixing Security Vulnerabilities with AI in OSS-Fuzz — http://arxiv.org/abs/2411.03346v2
[35] Prompt Fuzzing for Fuzz Driver Generation — http://arxiv.org/abs/2312.17677v2
[36] The Impact of Magma: A Ground-Truth Fuzzing Benchmark — http://arxiv.org/abs/2608.28016v1
[37] Magma: A Ground-Truth Fuzzing Benchmark — http://arxiv.org/abs/2009.01120v2
[38] NTIRE 2025 Challenge on Short-form UGC Video Quality Assessment

---

*Generated by research-bot · topic=`cybersecurity` · depth=`standard` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading · model=`deepseek-v4-flash` · sources=116 · duration=349s · 2026-10-04T22:19:39+00:00*
