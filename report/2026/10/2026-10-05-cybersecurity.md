# 网络安全攻防前沿调研报告（2024–2026）

**日期**：2026-10-05（UTC）
**领域**：Cybersecurity（漏洞与利用 / 模糊测试与程序分析 / 软件供应链与 SBOM / 后量子密码迁移 / 大模型与 Agent 安全）
**检索源规模**：124 条候选引用（[1]–[124]）+ 3 类领域种子资源（论文 / 开源项目 / 数据集）
**证据说明**：本批候选块**未提供**引用数、GitHub star、下载量或榜单排名字段（唯一例外为 [58] 标注 `citations=236`）。因此除 [58] 外，所有「热度证据」一律记 `> 待核实`；**本报告不编造任何热度数字**。多数条目为 arXiv 预印本（含 `cs.CR`/`cs.SE`/`cs.LG` 分类），同行评审状态需逐条核实。本批候选证据在「CVE 补丁数据集」「注入/越狱基准」「自动化攻防竞赛基准」三处存在明显召回缺口，已在第六、七章显式标注。

---

## 摘要（Executive Summary）

1. **LLM/Agent 安全是本轮证据最密集、迭代最快的前沿**，已形成「注入攻击 → 系统级防御 → 自适应攻击破防」的军备竞赛闭环：攻击侧有 WebInject 对网页 Agent 的环境投毒 [2]、通用自动注入 [11]；防御侧有结构化查询 StruQ [3]、偏好优化 SecAlign [1]、工具依赖图 IPIGuard [5]、可证明防御 MELON [13]、因果归因 AttriGuard [9]、系统级架构 ACE [8] 与多 Agent 防御流水线 [14]；而 [7] 用自适应攻击证明多数防御可被绕过——这是本领域最值得警惕的结论。
2. **越狱（jailbreak）研究已从文本单模态扩展到 MLLM 与 Agent 生态**，出现人格化提示攻击 [16]、主动式防御 [17]、生成对抗式统一攻防 [19]、护栏规避实证分析 [18]，并有面向 MLLM/Agent 的系统综述 [21] 与聊天机器人越狱综述 [64]。
3. **模糊测试的前沿重心在「定向灰盒 fuzzing（DGF）」与「持续 fuzzing 的工程实证」两端**：前者有 `MC²` [72]、多目标 DGF [73]、步进式约束聚焦 [77]、时序逻辑引导 [79] 与 DGF 进展综述 [74]；后者有百万级 session 的连续 fuzzing 实证 [89]、fuzz harness 退化研究 [94]、OSS-Fuzz 假崩溃消减 [95]。内核侧的关键视角是 SyzScope——回答「fuzzer 发现的 bug 真实危害有多大」[26]。
4. **程序分析路线出现「LLM 与符号执行融合」的新范式**：LLM 引导 KLEE 的定向符号执行 [40]、LLM 模拟 KLEE 输出 [35]，与符号执行应用综述 [33]、二进制符号执行 [96][98] 构成「经典 + 新范式」的双层结构。
5. **软件供应链：SBOM 已从「合规交付物」被实证研究证伪为「合规 ≠ 安全」**。78K 真实 SBOM 的依赖图研究 [107]、GitHub SBOM 完整性与一致性的大规模审计 [102]、标准与工具之间的「遵循度鸿沟」[106]、SPDX vs CycloneDX 工具生态对比 [101] 共同指向：SBOM 的数据质量与消费端可用性仍是开放问题。
6. **后量子密码（PQC）重心已从「算法标准化」转向「迁移工程」**：迁移挑战与密码敏捷性 [117]、密码库 PQC 支持现状 [116]、WAN 迁移风险评估框架 [114]、Agent 辅助 RSA→ML-DSA 代码迁移 [113]、LLM 辅助静态审计与量子风险评分 [43]，以及移动端能耗约束 [41]。
7. **内存安全路线之争已进入「可验证迁移」阶段**：C→Rust 用户研究 [119]、LLM 驱动且带静态分析与 FFI 验证的迁移工具 SACTOR [120]、经形式化验证的 Rust 编译器子集 RustCompCert [121]，但同时出现直接反论 **[124]「自动重构 ≠ 内存安全」**——这是本章最有价值的分歧点。
8. **检索缺口（必须显式承认）**：本批候选证据**未召回**任何关于 CVEfixes/BigVul/PrimeVul 数据集口径、AgentDojo/JailbreakBench/HarmBench 基准、CyberGym/Cybench 竞赛基准的一手来源；相关结论一律标 `> 待核实`（见第六、七章）。
9. **最大的开放性争议**：自动化攻防（LLM 自主发现与利用漏洞）的能力边界与失控风险。AIxCC 的 SoK 复盘 [59]、可复用于真实开源仓库的 CRS 框架 OSS-CRS [61]、agentic 内存安全漏洞检测 Revelio [62]、LLM 自主网络防御者 [110] 与自改进安全 Agent [66] 分别提供了设计侧、能力侧与防御侧的三种证据，但**尚无独立第三方的统一能力评测口径**。

---

## 一、关键前沿进展（近 1–2 年）

> 本节只收录 2024 年及以后发表的条目；经典奠基工作见第二至六章各表的「经典」分区。

### 1.1 LLM/Agent 安全（2024–2026，最活跃）

| 名称 | 年份 | 方向 | 热度证据 | 权威证据 | 关注度 | 推荐度 |
|---|---|---|---|---|---|---|
| WebInject [2] | 2025 | 网页 Agent 提示注入攻击 | `> 待核实`（候选块无引用数/star） | arXiv 预印本（候选块标 `cs.LG`），未见同行评审信息 | 中 —— 首个针对 MLLM 网页 Agent 的"环境侧投毒"攻击面，与 Web Agent 落地同步升温 | ★★★★（攻击面新、与 Agent 部署强相关；但热度与中稿状态待核实） |
| StruQ [3] | 2024 | 结构化查询防御 | `> 待核实` | arXiv 预印本（`arXiv:2402.06363v2`），未见 venue 字段 | 高 —— 属提示注入防御的早期范式性工作，被后续工作反复对照 [1][7] | ★★★★（范式清晰、被后续文献引用为基线） |
| SecAlign [1] | 2024 | 偏好优化防御 | `> 待核实` | arXiv 预印本（`arXiv:2410.05451v3`） | 中 —— 将偏好优化引入注入防御，方法新颖 | ★★★★（与 StruQ 同源团队思路，方法可迁移） |
| MELON [13] | 2025 | 可证明防御（间接注入） | `> 待核实` | arXiv 预印本（`arXiv:2502.05174v4`） | 中 —— "可证明"定位在经验防御泛滥中稀缺 | ★★★★（理论保证是稀缺卖点；实际开销待核实） |
| AttriGuard [9] | 2026 | 工具调用因果归因防御 | `> 待核实` | arXiv 预印本（`arXiv:2603.10749v2`），候选块标 `cs.CR` | 中 —— 从"输入语义判别"转向"执行因果归因"，视角新 | ★★★★（问题重构有启发性） |
| ACE [8] | 2025 | LLM 集成应用安全架构 | `> 待核实` | arXiv 预印本（`arXiv:2504.20984v3`），`cs.CR` | 中 —— 针对第三方 app 的完整性违规 | ★★★★（系统级视角，适合工程落地参考） |
| 自适应攻击破防 [7] | 2025 | 防御失效分析 | `> 待核实` | arXiv 预印本（`arXiv:2503.00061v2`） | 高 —— 直接质疑既有防御的有效性，属"泼冷水"型关键文献 | ★★★★★（做注入防御前必读的负结果类工作） |

**要点**：提示注入已从「输入文本层」扩展到「环境层」（网页渲染 [2]）与「执行层」（工具调用 [9]、第三方 app [8]）。防御范式可归为四类：① 输入结构化隔离 [3]；② 训练侧偏好对齐 [1]；③ 执行图/数据流约束 [5][9]；④ 系统性架构隔离 [6][8]。**但 [7][18] 表明：在自适应攻击者面前，经验性防御普遍存在被绕过风险**，这是本方向当前最大共识性风险。

### 1.2 越狱（jailbreak）与护栏规避

| 名称 | 年份 | 方向 | 热度证据 | 权威证据 | 关注度 | 推荐度 |
|---|---|---|---|---|---|---|
| Persona Prompts 越狱 [16] | 2025 | 人格化越狱攻击 | `> 待核实` | arXiv 预印本（`arXiv:2507.22171v3`） | 中 —— 人格设定是低成本高成功率的攻击向量 | ★★★★（攻击面易复现） |
| Proactive defense [17] | 2025 | 主动式越狱防御 | `> 待核实` | arXiv 预印本（`arXiv:2510.05052v2`） | 中 | ★★★（需核实其威胁模型是否覆盖自适应攻击） |
| CAVGAN [19] | 2025 | 生成对抗式统一攻防 | `> 待核实` | arXiv 预印本（`arXiv:2507.06043v2`） | 中 —— 攻防同框架，视角统一 | ★★★★（方法学上有整合价值） |
| 护栏规避实证 [18] | 2025 | 检测系统规避 | `> 待核实` | arXiv 预印本（`arXiv:2504.11168v3`） | 高 —— 直接测评商用护栏的鲁棒性 | ★★★★★（部署护栏前必读） |
| LLM→MLLM→Agent 越狱综述 [21] | 2025 | 综述 | `> 待核实` | arXiv 预印本（`arXiv:2506.15170v3`） | 中 —— 生态级分类骨架 | ★★★★（适合作为分类骨架） |
| Prompt Jailbreaking 综述 [64] | 2026 | 综述 | `> 待核实` | DOI 指向 IEEE TAI（`10.1109/TAI.2026.3665656`），**期刊级** | 中高 —— 期刊综述通常较预印本更稳 | ★★★★（权威性相对更高，但需核实刊期） |

### 1.3 攻防自动化与 Agent 化

- **AIxCC 的 SoK 复盘** [59]（`arXiv:2602.07666v5`）：系统梳理竞赛设计、系统架构与经验教训；热度 `> 待核实`；关注度中高（DARPA 项目自带公共关注度）；推荐度 ★★★★（了解自动攻防现状的最佳单点入口）。
- **OSS-CRS** [61]（`arXiv:2603.08566v2`）：将 AIxCC 的 Cyber Reasoning Systems 释放到真实开源安全场景；关注度中；推荐度 ★★★★（"竞赛 → 生产"的关键桥梁）。
- **Revelio** [62]（`arXiv:2606.22263`）：面向仓库级代码库的 agentic 内存安全漏洞检测，强调成本效率；推荐度 ★★★★（与内存安全主线呼应）。
- **LLM-HyPZ** [57]（`arXiv:2509.00647`）：LLM 辅助硬件漏洞发现；推荐度 ★★★（硬件方向旁支）。
- **SelfOp** [66]（`arXiv:2609.22792`）：自改进安全 Agent 优化算法；推荐度 ★★★（能力增强与安全风险的张力未充分展开）。
- **LLM 作为自主网络防御者** [110]（`arXiv:2505.04843v2`）：ACD 场景下 LLM 规划与执行；推荐度 ★★★★（与进攻侧 [59][61] 形成对照）。
- **LLM 在网络安全中的 PRISMA-ScR 范围综述** [68]（DOI `10.1109/ACCESS.2026.3719163`，IEEE Access）：可作为全局分类骨架；推荐度 ★★★★。
- **PrompTrend** [55]（`arXiv:2507.19185`）：LLM 漏洞的社区驱动持续发现与评估；推荐度 ★★★（连续监测视角有价值）。

> **数据外泄（data exfiltration）专项证据不足**：本批候选中，数据外泄主要以「间接注入导致越权工具调用 / 完整性违规」的间接形式出现 [6][8][9]，缺少专门的「外泄通道建模 + 量化防护评测」研究，**> 待核实**。

---

## 二、Web / 系统 / 供应链攻防

### 2.1 Web 与系统层

- **Web Agent 新攻击面**：WebInject 通过在网页环境中植入内容，诱导基于 MLLM 的网页 Agent 执行攻击者意图的动作 [2]。与 Web 应用侧的传统清单（OWASP Top 10，含 LLM 应用版）形成互补：**OWASP 提供风险条目基线，而 [2][11] 提供具体可执行攻击构造**。
- **LLM 集成应用系统**：ACE 指出第三方 app 可造成完整性违规，并提出安全架构 [8]；系统级防御立场文 [6] 主张把注入防御从「模型内」上移到「系统架构层」。两者共同指向一个判断：**仅靠 Prompt 工程无法解决注入，需在系统层做能力隔离与数据流控制**。
- **硬件与微架构侧信道**：本批候选覆盖了硬件防御 SoK（对抗推测执行攻击）[39]，属经典系统安全战线；具体新进展 `> 待核实`。
- **IoT 与关键基础设施**：种子资源含运营商与个人对 IoT 安全的动因/障碍研究 [30]、CPS 防御机制从功能需求推导 [69]、网络靶场自动化设计 [63]；均与"攻防工程化"相关，但与本报告主线相关性中等。

### 2.2 软件供应链与 SBOM

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| SBOM 工具生态对比（SPDX vs CycloneDX）[101] | 2025 | 候选块标 `cs.SE` | `> 待核实` | arXiv 预印本（`arXiv:2512.21781v2`） | 中 —— 两大主流格式的工具生态是落地必答题 | ★★★★（格式选型第一参考） | http://arxiv.org/abs/2512.21781v2 | 对比主流 SBOM 格式的生成/分析/管理工具 |
| GitHub SBOM 完整性与一致性大规模研究 [102] | 2026 | 候选块标 `cs.SE` | `> 待核实` | arXiv 预印本（`arXiv:2607.04614v1`） | 中高 —— "平台自动生成 SBOM 是否可信"是产业刚需 | ★★★★★（直接挑战"平台已合规"的假设） | http://arxiv.org/abs/2607.04614v1 | 标题即结论：Beyond Compliance |
| 78K 真实 SBOM 的依赖图实证 [107] | 2026 | 候选块标 `cs.SE` | `> 待核实` | arXiv 预印本（`arXiv:2607.22140v2`） | 中高 —— "No Edges, No Verdict"直击依赖图缺失导致无法判定影响面 | ★★★★★（供应链影响面分析的核心痛点） | http://arxiv.org/abs/2607.22140v2 | 大规模野外观测 |
| 标准与工具的遵循度鸿沟 [106] | 2026 | 候选块标 `cs.SE` | `> 待核实` | arXiv 预印本（`arXiv:2601.05622v1`） | 中 | ★★★★ | http://arxiv.org/abs/2601.05622v1 | 标准合规 ≠ 工具正确实现 |
| SBOM 消费工具评测数据集 [103] | 2025 | 候选块标 `cs.SE` | `> 待核实` | arXiv 预印本（`arXiv:2504.06880v1`） | 中 —— 消费端（而非生成端）评测数据稀缺 | ★★★★（可直接用作评测集，需核实版本） | http://arxiv.org/abs/2504.06880v1 | 面向 SBOM 消费工具的评测数据集 |
| Python 生态 SBOM 生成工具剖析 [104] | 2024 | 候选块标 `cs.SE` | `> 待核实` | arXiv 预印本（`arXiv:2409.01214v1`） | 中 | ★★★ | http://arxiv.org/abs/2409.01214v1 | 语言生态特化分析 |
| sbom-unifier [105] | 2026 | 候选块标 `cs.SE` | `> 待核实` | arXiv 预印本（`arXiv:2608.30708v1`） | 中 —— 异构 SBOM 整合是工程痛点 | ★★★ | http://arxiv.org/abs/2608.30708v1 | 集成框架 |
| UniBOM [108] | 2025 | 候选块标 `cs.SE` | `> 待核实` | arXiv 预印本（`arXiv:2511.22359v1`） | 中 | ★★★ | http://arxiv.org/abs/2511.22359v1 | IoT 等场景的统一分析与可视化 |

**供应链经典事件与政策**：SolarWinds 事件本身、以及其后的 SBOM 行政要求，在本批候选证据中**没有一手学术复盘或政策原文来源**，故其详细史实与条款 **> 待核实**；本报告仅以 SBOM 工具生态与数据质量的实证研究 [101][102][106][107] 作为「供应链可见性未达预期」的间接证据。签名与制品可信链方向，领域种子资源指向 Sigstore（https://github.com/sigstore/sigstore），热度与版本状态 **> 待核实**。

**结论性判断**：SBOM 方向已形成一条清晰的实证批判链——**生成工具生态分裂 [101] → 平台生成物不完整/不一致 [102] → 标准与实现存在鸿沟 [106] → 依赖图缺失导致无法定责 [107]**。热度证据全为 `> 待核实`，但**多方独立实证指向同一结论，构成高一致性证据**。

---

## 三、模糊测试与程序分析

### 3.1 定向灰盒 fuzzing（DGF）：本方向方法论主线

| 名称 | 年份 | 热度 | 权威 | 关注度 | 推荐度 | 引用 |
|---|---|---|---|---|---|---|
| `MC²`: Rigorous and Efficient Directed Greybox Fuzzing | 2022 | `> 待核实` | arXiv 预印本（`2208.14530v1`） | 中高 —— DGF 的严格化与效率改进代表工作 | ★★★★ | [72] |
| Multiple Targets Directed Greybox Fuzzing | 2022 | `> 待核实` | arXiv 预印本（`2206.14977v1`） | 中 —— 多目标场景 | ★★★ | [73] |
| The Progress, Challenges, and Perspectives of DGF | 2020/后续修订 | `> 待核实` | arXiv 预印本（`2005.11907v5`，v5 表明持续维护） | 中高 —— DGF 方向的分类骨架 | ★★★★ | [74] |
| Greybox fuzzing time-intensive programs | 2023 | `> 待核实` | arXiv 预印本（`2311.17200v1`） | 中 —— 长耗时程序的调度问题 | ★★★ | [76] |
| DGF with Stepwise Constraint Focusing | 2023 | `> 待核实` | arXiv 预印本（`2303.14895v1`） | 中 —— 约束聚焦策略 | ★★★ | [77] |
| Efficient Greybox Fuzzing to Detect Memory Errors | 2022 | `> 待核实` | arXiv 预印本（`2204.02773v2`） | 中 —— 与内存安全主线呼应 | ★★★ | [78] |
| LTL-guided Greybox Fuzzing | 2021 | `> 待核实` | arXiv 预印本（`2109.02312v3`） | 中 —— 时序性质引导，属"性质定向"路线 | ★★★★ | [79] |

### 3.2 覆盖率引导与执行开销优化（经典→近年的延续）

- **覆盖率引导的评估与加速**：Fork-Awareness 评估 [25]、二进制 fuzzing 的覆盖率保持型追踪加速 [27]、Full-speed Fuzzing [31]、把 fuzzing 建模为在线随机控制的 FOX [29]。这组工作共同主题是**「如何在保持覆盖率信号质量的前提下降低插桩/追踪开销」**——这是该方向十年不变的核心矛盾。
- **经典参照**：KLEE 的 Sonar-Search 策略在灰盒 fuzzing 语境下的再评估 [34]（2018）；`AFL`/`libFuzzer` 本身无编号来源，其状态见第五章开源项目表。
- **内核漏洞危害量化（关键视角）**：SyzScope 提出揭示 fuzzer 暴露 bug 的"高风险安全影响"，挑战"崩溃 ≠ 可利用"的默认假设 [26]。这是把 fuzzing 输出与真实风险对齐的关键一环。
- **OSS/持续 fuzzing 的大规模实证（近年重心）**：
  - 百万级 session 的连续 fuzzing 实证分析 [89]（`2510.16433v1`，2025）——**关注度高**，是目前规模最大的连续 fuzzing 观测之一；推荐度 ★★★★。
  - fuzz harness 退化研究 [94]（`2505.06177v2`，2025）——揭示持续 fuzzing 平台中 harness 随项目演进失维，导致覆盖率/有效性衰退；**这是被长期忽视的工程负结果**；推荐度 ★★★★。
  - OSS-Fuzz-Gen 假崩溃消减（FalseCrashReducer）[95]（`2510.02185v1`，2025）——用 agentic AI 降误报；推荐度 ★★★★。
  - AI 修复 OSS-Fuzz 中的安全漏洞 [92]（`2411.03346v2`）——从"发现"到"修复"的延伸；推荐度 ★★★★。
  - OSS-Fuzz bug 历史研究 [88][91]；推荐度 ★★★。
  - Java 库 fuzzing 的覆盖率引导多 Agent harness 生成 [90]（`2603.08616v1`，2026）——harness 自动化生成的代表；推荐度 ★★★★。
  - 混合 fuzzing 与动态分析工程链 Sydr-Fuzz [93]；推荐度 ★★★。

### 3.3 符号执行与二进制分析（经典 + LLM 新范式）

| 名称 | 年份 | 定位 | 热度 | 权威 | 关注度 | 推荐度 | 引用 |
|---|---|---|---|---|---|---|---|
| Symbolic Execution in Practice: A Survey | 2025 | 应用综述（漏洞/恶意软件/固件/协议） | `> 待核实` | arXiv 预印本（`2508.06643v1`），候选块标 `cs.CR` | 中高 —— 覆盖四大应用域的近期综述 | ★★★★ | [33] |
| Can LLMs Simulate Symbolic Execution Output Like KLEE? | 2025 | LLM 替代/近似符号执行 | `> 待核实` | arXiv 预印本（`2511.08530v1`），`cs.SE` | 中 —— 直击 KLEE 路径爆炸痛点 | ★★★★ | [35] |
| Directed Symbolic Execution (LLM-Guided in KLEE) | 2026 | LLM 引导定向符号执行 | `> 待核实` | arXiv 预印本（`2607.21676v1`），`cs.SE` | 中高 —— 把 LLM 用作路径优先级启发式 | ★★★★ | [40] |
| cozy: Comparative Symbolic Execution for Binary Programs | 2025 | 二进制符号执行对比分析 | `> 待核实` | arXiv 预印本（`2504.00151v1`） | 中 | ★★★ | [96] |
| Symbolic Execution based on Formal ISA Semantics | 2024 | 二进制符号执行的 ISA 语义基础 | `> 待核实` | arXiv 预印本（`2404.04132v2`） | 中 —— 正确性根基 | ★★★★ | [98] |
| **经典**：Higher-order symbolic execution | 2015 | 高阶符号执行（合约验证与反证） | `> 待核实` | arXiv 预印本（`1507.04817v3`） | 低中 —— 理论奠基类 | ★★★ | [37] |
| **经典**：KLEE Sonar-Search 再评估 | 2018 | 符号执行 vs 灰盒 fuzzing | `> 待核实` | arXiv 预印本（`1803.04881v1`） | 中 —— 两条路线对照的经典参照 | ★★★★ | [34] |
| **经典**：自动生成安全关键软件测试用例 | 2022 | 符号执行工程化 | `> 待核实` | arXiv 预印本（`2209.11138v1`） | 低中 | ★★★ | [38] |

**代际提升的可核查表述**：现有候选证据支持如下定性判断——**LLM 的引入被定位为对"路径爆炸"这一符号执行/定向 fuzzing 长期瓶颈的启发式改进手段**（[35] 针对 KLEE 慢、[40] 针对路径优先级陷入循环控制流区域、[90] 针对 harness 手工编写耗时）。但**缺少统一的跨代量化口径**（覆盖率、time-to-crash、真实 CVE 复现率），因此「相比上一代提升多少」在本批证据下 **无法量化，> 待核实**。

> **检索缺口**：本批证据中**没有**直接覆盖「内核灰盒 fuzzing（syzkaller 谱系）新进展」「LLM 自动生成 PoC/exploit（自动利用生成）」的一手来源。q2 的候选块中多篇为 NLP/CV 检测类论文 [80][81][82][84][85]，**不可**作为 LLM 辅助漏洞检测的证据使用（存在范式误迁移风险）。

---

## 四、大模型与 Agent 安全（提示注入 / 越狱 / 数据外泄）

### 4.1 攻击面分类（基于本批证据归纳）

| 攻击类型 | 代表工作 | 关键结论 | 引用 |
|---|---|---|---|
| 直接提示注入 | 通用自动注入攻击 | 可自动、通用地构造有效注入 | [11] |
| 间接提示注入（数据侧） | IPIGuard 的问题设定 | 工具返回的非可信数据可携带恶意指令 | [5] |
| 间接提示注入（环境侧） | WebInject | 通过操纵网页环境诱导 MLLM Web Agent 执行攻击者动作 | [2] |
| 多步/应用集成 | ACE | 第三方 app 在规划-执行交错中造成完整性违规 | [8] |
| 工具调用劫持 | AttriGuard | 把 IPI 建模为工具调用的因果归因问题 | [9] |
| 越狱（人格化） | Persona Prompts | 人格设定提升越狱成功率 | [16] |
| 护栏规避 | Evasion against guardrails | 实证提示注入/越狱检测系统可被规避 | [18] |
| 自适应攻击 | Adaptive Attacks Break Defenses | **多数现有防御在自适应攻击下失效** | [7] |

### 4.2 防御范式与有效性

- **训练/对齐类**：SecAlign 用偏好优化让模型倾向忽略注入指令 [1]。
- **输入隔离类**：StruQ 用结构化查询把指令与数据在通道上分离 [3]。
- **可证明类**：MELON 提出针对间接注入的可证明防御 [13]（**热度待核实，但"可证明"在经验防御泛滥下具有稀缺价值**）。
- **执行图类**：IPIGuard 用工具依赖图做防御 [5]；AttriGuard 用因果归因判定工具调用是否被注入驱动 [9]。
- **架构隔离类**：ACE 给出 LLM 集成应用的安全架构 [8]；立场文 [6] 主张系统级防御路线；多 Agent 防御流水线 [14] 用多角色协同做检测/裁决。
- **统一检测类**：UniGuardian 尝试用统一框架同时检测提示注入、后门与对抗攻击 [10]；分类器路线（含 LSTM、前馈等）在 HackAPrompt 语料上做检测 [12]。
- **模型自防御**：视点文主张 LLM 可实用地自我防御越狱 [15]；主动式防御 [17] 与生成对抗式 CAVGAN [19] 提供不同实现路径。

**核心结论（有争议但证据一致）**：**防御有效性的证据强度低于攻击有效性的证据强度**。[7] 的自适应攻击结果与 [18] 的护栏规避结果为这一判断提供了两个独立支撑；而 [13] 的"可证明"路线是当前唯一可能跳出该困境的方向，但其实际部署开销与威胁模型完整性 **> 待核实**。

### 4.3 数据外泄

本批候选证据中，**没有**专门研究「Agent 数据外泄通道（如外发请求、日志、工具副作用）建模与防护」的论文。相关风险仅以「危险 Agent 动作」[6]、「完整性违规」[8]、「工具调用被劫持」[9] 的形式间接出现。因此：

> **数据外泄的量化攻击成功率、外泄检测基准、防护有效性均 `> 待核实`**，建议下一轮以 `data exfiltration LLM agent`、`agent side-channel leakage`、`tool-call exfiltration benchmark` 定向召回。

---

## 五、密码学与后量子迁移

### 5.1 标准化与算法层（经典/依据）

- **NIST PQC 标准算法**：有工作讨论基于量子随机数发生器的 NIST PQC 标准算法实现 [44]（`2507.21151v1`）。NIST 已发布多项 FIPS 后量子标准（文中提及）；**具体 FIPS 编号与算法集（ML-KEM/ML-DSA/SLH-DSA 等）应以 NIST 官方文档为准，本报告不据记忆断言，> 待核实**。
- **历史与理论背景**：量子密码学的替代路线讨论 [42]；面向量子抗性的区块链密码综述 [45]；阈值签名综合综述（覆盖 NIST 标准与 PQC）[48]。
- **性能约束（被低估的落地障碍）**：移动端对即将到来的 NIST PQC 标准的能耗需求分析 [41]（`1912.00916v4`，多版本修订表明长期维护）——**这是"算法可标准化 ≠ 设备可承载"的关键证据**；推荐度 ★★★★。

### 5.2 迁移工程（近两年重心）

| 名称 | 年份 | 方向 | 热度 | 权威 | 关注度 | 推荐度 | 引用 |
|---|---|---|---|---|---|---|---|
| Identifying Research Challenges in PQC Migration and Cryptographic Agility | 2019 | 迁移挑战与密码敏捷性（奠基性） | `> 待核实` | arXiv 预印本（`1909.07353v1`） | 中高 —— 密码敏捷性概念的早期系统论述 | ★★★★★ | [117] |
| A Survey of PQC Support in Cryptographic Libraries | 2025 | 密码库支持现状 | `> 待核实` | arXiv 预印本（`2508.16078v1`） | 中高 —— 回答"现在能换吗" | ★★★★★ | [116] |
| Quantum-Ready Secure WAN: Risk Assessment and Migration Framework | 2026 | 网络侧迁移框架 | `> 待核实` | arXiv 预印本（`2609.26225v1`） | 中 —— 从算法到网络工程的落地 | ★★★★ | [114] |
| Can Coding Agents Migrate to Post-Quantum Cryptography? | 2025 | Agent 辅助代码迁移 | `> 待核实` | arXiv 预印本（`2512.12989v3`），候选块标 `cs.MA` | 中高 —— 提出基于契约的 RSA→ML-DSA-44 迁移任务，并对比有无结构化检查的 coding agent | ★★★★★（把 PQC 迁移与 Agent 能力测评结合，方法学新颖） | [113] |
| Quantum-Safe Code Auditing | 2026 | LLM 辅助静态分析 + 量子风险评分 | `> 待核实` | arXiv 预印本（`2604.00560v1`），`cs.CR` | 中 —— 给出"量子感知风险评分"的审计思路 | ★★★★ | [43] |
| Quantum-Resistant Networks Using PQC | 2025 | 网络实现 | `> 待核实` | arXiv 预印本（`2510.24534v1`） | 中 | ★★★ | [118] |
| Enhancing Quantum Security over Federated Learning via PQC | 2024 | 联邦学习 + PQC | `> 待核实` | arXiv 预印本（`2409.04637v1`） | 中 | ★★★ | [47] |

**关键判断**：PQC 迁移的真实成本由三层构成——**① 密码库与协议栈支持度 [116]；② 设备/网络侧性能与能耗约束 [41][114]；③ 存量代码审计与改造工作量 [43][113]**。其中 [113] 特别指出一个工程陷阱：**迁移后的程序可能"自验通过但他方实现拒绝"**（自洽但互操作性失败），这正是密码迁移与普通重构的本质区别。**总体迁移成本的具体数字（人月、性能损耗百分比）本批证据未提供，> 待核实**。

---

## 六、数据集、基准与红蓝对抗

### 6.1 有证据支撑的条目

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| AIxCC SoK [59] | 2026 | 候选块标 `cs.CR` | `> 待核实` | arXiv 预印本（`2602.07666v5`，v5 表明持续更新） | 中高 —— DARPA 自动攻防竞赛的权威复盘（SoK 体裁） | ★★★★★ | http://arxiv.org/abs/2602.07666v5 | 竞赛设计、CRS 架构、经验教训 |
| OSS-CRS [61] | 2026 | 候选块标 `cs.CR` | `> 待核实` | arXiv 预印本（`2603.08566v2`） | 中 —— AIxCC 技术向真实开源迁移 | ★★★★ | http://arxiv.org/abs/2603.08566v2 | 把 CRS 用于真实 OSS 安全 |
| Revelio [62] | 2026 | 候选块标 `cs.CR` | `> 待核实` | arXiv 预印本（`2606.22263`） | 中 —— 仓库级内存安全漏洞检测 | ★★★★ | http://arxiv.org/abs/2606.22263 | 成本高效的 agentic 检测 |
| Agent/LLM 评测综述 [58] | 2025 | IEEE Access（候选块标注） | **citations=236**（候选块 Semantic Scholar 字段） | IEEE Access（同行评审期刊）+ arXiv `2504.19678v2` | **高 —— 依据 citations=236 与跨约 60 个 benchmark 的综述定位** | ★★★★ | https://arxiv.org/abs/2504.19678 | 提供 2019–2025 基准分类骨架；**不含** CVE/攻防竞赛/注入基准细粒度口径 |
| SBOM 消费工具评测数据集 [103] | 2025 | 候选块标 `cs.SE` | `> 待核实` | arXiv 预印本（`2504.06880v1`） | 中 —— 消费端评测数据稀缺 | ★★★★ | http://arxiv.org/abs/2504.06880v1 | 面向 SBOM 消费工具评测 |
| NVD / CVE | ongoing | NIST | `> 待核实` | 官方数据库（领域种子资源） | 高 —— 漏洞标识与评分的事实标准 | ★★★★★ | https://nvd.nist.gov/ | 漏洞数据库；本报告未实时检索其当前条目数 |
| CWE / CWE Top 25 | ongoing | MITRE | `> 待核实` | 官方标准（领域种子资源） | 高 —— 弱点分类事实标准 | ★★★★★ | https://cwe.mitre.org/ ; https://cwe.mitre.org/top25/ | 弱点分类与排行 |
| Big-Vul / CVEfixes | 2021 起 | secureIT-project | `> 待核实` | 官方数据集仓库（领域种子资源） | 中高 —— 漏洞修复数据集常用基线 | ★★★★ | https://github.com/secureIT-project/CVEfixes | 漏洞修复数据集；样本量/去重/时间切分 **> 待核实** |
| OWASP Top 10 | 2021/2025 | OWASP | `> 待核实` | 社区权威清单（领域种子资源） | 高 —— Web/LLM 应用风险通用基线 | ★★★★★ | https://owasp.org/www-project-top-ten/ | 含 LLM 应用版本 |

### 6.2 明确缺失的基准（本批证据未覆盖）

| 缺口项 | 应有内容 | 状态 |
|---|---|---|
| CVEfixes / BigVul / PrimeVul 口径 | 样本量、漏洞类型分布、函数级 vs 提交级标签、去重与时间切分 | **> 待核实**（本批候选块无任何相关条目；仅种子资源给出 CVEfixes 链接） |
| DARPA AIxCC 评分与最终结果 | 赛制、漏洞发现/修补计分、任务规模、真实二进制环境 | 部分覆盖：[59][61] 提供设计与架构，**具体分数与结果 > 待核实** |
| CyberGym / Cybench | 评测任务集、评分口径 | **> 待核实**（本批候选块无相关条目） |
| AgentDojo | 工具调用场景下的注入 ASR 与任务效用权衡 | **> 待核实**（本批候选块无相关条目） |
| JailbreakBench / HarmBench | 有害请求拒答率 / 攻击成功率 / 裁判模型一致性 | **> 待核实**（本批候选块无相关条目；越狱方向仅有综述 [21][64] 与攻击/防御方法 [16][17][19]） |

> **口径可比性提醒**：CVE 数据集的静态检测指标（如 F1/VulD，等级 B/C）、攻防竞赛的端到端解题得分（等级 B）、注入基准的 ASR/效用指标（等级 B/C）属于**三种不同度量体系**，本批证据中**没有任何来源**尝试将其统一为同一 Agent 能力评估框架，**> 待核实**。

### 6.3 红蓝对抗工具与靶场

- 网络靶场自动化设计（需求—供给匹配）[63]；`> 待核实`（无热度信号）。
- 自动化网络防御者（ACD）以 LLM 替换/增强 RL 策略 [110]；关注度中。
- **红队工具链（如 LLM 护栏红队专用工具）在本批候选中无具体开源项目来源，> 待核实**。

---

## 七、争议与开放问题

1. **注入防御是否真的有效？** 争议核心在「静态防御评测」与「自适应攻击」的差距。[7] 显示自适应攻击可击破多数针对间接注入的防御；[18] 显示护栏检测器可被规避。**反方立场**是 [13] 的可证明防御与 [6][8] 的系统级架构路线，主张把问题从"分类正确率"转向"能力隔离"。本批证据**尚不足以裁定**哪条路线最终胜出，**> 待核实**。
2. **SBOM 的「合规 ≠ 安全」**：[102][106][107] 从完整性、标准遵循度、依赖图三个独立角度给出负面证据，是证据一致性较高的结论（等级 B，多方独立）。但**是否应强制包含依赖边（edges）**、以及强制化对生态的副作用，仍无定论 **> 待核实**。
3. **PQC 迁移的真实成本与优先级**：算法已标准化 [44]，但库支持 [116]、设备能耗 [41]、网络改造 [114]、存量代码审计 [43] 与互操作性陷阱 [113] 共同构成成本的"长尾"。**"先迁移什么"的排序方法学尚无统一结论**，[117] 在 2019 年已提出密码敏捷性框架，近两年工作（[114][116][113]）可视为对其的具体化，但**成本量化数据缺失**。
4. **内存安全路线：Rust 迁移是不是银弹？** 支持侧：C→Rust 用户研究揭示迁移中的实际痛点 [119]、SACTOR 用 LLM + 静态分析 + FFI 验证做正确且地道的迁移 [120]、RustCompCert 为 Rust 顺序子集提供经验证的编译器 [121]、航天安全关键系统的 Rust 可行性 [122]。**反方**：`C-to-Rust Fallacy: Automatic Refactoring != Memory Security` [124] 直接主张自动重构**不产生**内存安全保证。**这是本报告中最值得追踪的技术分歧**，双方均为 arXiv 预印本（`> 待核实` 同行评审状态）。
5. **自动化攻防的能力边界与失控风险**：AIxCC 的 SoK [59] 与 OSS-CRS [61] 证明"竞赛环境可行"，但对**真实仓库规模、真实漏洞可利用性、误报成本**的外推仍有争议；Revelio [62] 的"成本高效"主张需要独立复现。**是否存在失控风险（自主利用生成、能力外溢）在本批证据中无直接研究，> 待核实**。
6. **漏洞检测评测的可复现性与负结果**：这是本方向最被低估的系统性问题。已有证据包括 harness 退化 [94]、假崩溃 [95]、OSS-Fuzz bug 历史 [88][91]、连续 fuzzing 百万 session 实证 [89]。**共同指向：以"崩溃数"为 KPI 的持续 fuzzing 会系统性高估有效性**。但**跨工具的统一可复现性基准仍缺失，> 待核实**。
7. **政府监管路线之争（内存安全强制、SBOM 强制）**：本批候选证据**未覆盖**政策原文与监管效果评估，**> 待核实**。

---

## 八、建议关注清单（Watchlist）

**第一优先级（高相关 + 有方法学新意）**

1. **[7] Adaptive Attacks Break Defenses Against Indirect Prompt Injection** —— 任何注入防御工作的必读负结果基线。
2. **[124] C-to-Rust Fallacy** vs. **[120] SACTOR** / **[121] RustCompCert** —— 内存安全迁移的核心分歧对，建议成对跟踪。
3. **[59] AIxCC SoK** + **[61] OSS-CRS** —— 自动攻防从竞赛走向生产的唯一可见路径。
4. **[107] No Edges, No Verdict** + **[102] Beyond Compliance** —— SBOM 实证批判链的两端，供应链可见性问题的硬证据。
5. **[113] Can Coding Agents Migrate to Post-Quantum Cryptography?** —— 首次把 PQC 迁移做成可评测的 Agent 契约任务。

**第二优先级（方向代表或分类骨架）**

6. **[33] Symbolic Execution in Practice（2025 综述）** + **[40] LLM-Guided Directed Symbolic Execution** —— 程序分析「经典 + LLM 新范式」组合。
7. **[89] 1 Million Fuzzing Sessions** + **[94] Fuzz Harness Degradation** —— 持续 fuzzing 的规模化实证与工程负结果。
8. **[21] Jailbreak Survey (LLM→MLLM→Agent)** + **[64] IEEE TAI Jailbreak Survey** —— 越狱方向的生态级骨架（后者为期刊级，权威性更高，刊期需核实）。
9. **[116] PQC Support in Cryptographic Libraries** + **[117] PQC Migration & Cryptographic Agility** —— 迁移工程"现状 + 框架"组合。
10. **[58] From LLM Reasoning to Autonomous AI Agents**（citations=236）—— 建立评测基准分类骨架的入口，但需注意其**不含**安全专项基准口径。

**待补齐的检索任务（下一轮必做）**

- `CVEfixes dataset`、`PrimeVul benchmark`、`BigVul label noise` —— 补齐数据集口径（**> 待核实**）。
- `AgentDojo prompt injection benchmark`、`HarmBench evaluation`、`JailbreakBench judge agreement` —— 补齐注入/越狱基准（**> 待核实**）。
- `AIxCC final results scoring`、`CyberGym benchmark`、`Cybench` —— 补齐攻防竞赛基准（**> 待核实**）。
- `LLM exploit generation`、`automatic PoC synthesis benchmark`、`kernel fuzzing syzkaller 2025` —— 补齐 q2 的空白（**> 待核实**）。
- `data exfiltration LLM agent`、`agent tool-call leakage` —— 补齐第四章的外泄缺口（**> 待核实**）。

---

## 参考来源

- [1] SecAlign: Defending Against Prompt Injection with Preference Optimization — http://arxiv.org/abs/2410.05451v3
- [2] WebInject: Prompt Injection Attack to Web Agents — http://arxiv.org/abs/2505.11717v4
- [3] StruQ: Defending Against Prompt Injection with Structured Queries — http://arxiv.org/abs/2402.06363v2
- [4] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1
- [5] IPIGuard: A Novel Tool Dependency Graph-Based Defense Against Indirect Prompt Injection in LLM Agents — http://arxiv.org/abs/2508.15310v1
- [6] Architecting Secure AI Agents: Perspectives on System-Level Defenses Against Indirect Prompt Injection Attacks — http://arxiv.org/abs/2603.30016v1
- [7] Adaptive Attacks Break Defenses Against Indirect Prompt Injection Attacks on LLM Agents — http://arxiv.org/abs/2503.00061v2
- [8] ACE: A Security Architecture for LLM-Integrated App Systems — http://arxiv.org/abs/2504.20984v3
- [9] AttriGuard: Defeating Indirect Prompt Injection in LLM Agents via Causal Attribution of Tool Invocations — http://arxiv.org/abs/2603.10749v2
- [10] UniGuardian: A Unified Defense for Detecting Prompt Injection, Backdoor Attacks and Adversarial Attacks in Large Language Models — http://arxiv.org/abs/2502.13141v2
- [11] Automatic and Universal Prompt Injection Attacks against Large Language Models — http://arxiv.org/abs/2403.04957v1
- [12] Detecting Prompt Injection Attacks Against Application Using Classifiers — http://arxiv.org/abs/2512.12583v1
- [13] MELON: Provable Defense Against Indirect Prompt Injection Attacks in AI Agents — http://arxiv.org/abs/2502.05174v4
- [14] A Multi-Agent LLM Defense Pipeline Against Prompt Injection Attacks — http://arxiv.org/abs/2509.14285v4
- [15] LLMs Can Defend Themselves Against Jailbreaking in a Practical Manner: A Vision Paper — http://arxiv.org/abs/2402.15727v2
- [16] Enhancing Jailbreak Attacks on LLMs via Persona Prompts — http://arxiv.org/abs/2507.22171v3
- [17] Proactive defense against LLM Jailbreak — http://arxiv.org/abs/2510.05052v2
- [18] Bypassing LLM Guardrails: An Empirical Analysis of Evasion Attacks against Prompt Injection and Jailbreak Detection Systems — http://arxiv.org/abs/2504.11168v3
- [19] CAVGAN: Unifying Jailbreak and Defense of LLMs via Generative Adversarial Attacks on their Internal Representations — http://arxiv.org/abs/2507.06043v2
- [20] AIn't Nothing But a Survey? Using Large Language Models for Coding German Open-Ended Survey Responses on Survey Motivation — http://arxiv.org/abs/2506.14634v3
- [21] From LLMs to MLL

---

*Generated by research-bot · topic=`cybersecurity` · depth=`standard` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading · model=`deepseek-v4-flash` · sources=124 · duration=306s · 2026-10-05T22:18:53+00:00*
