# Agent 评测与安全（能力基准、欺骗与可纠正性）七维增量追踪报告

**日期**：2026-10-22（UTC）｜**领域**：Agent Evaluation & Safety（LLM/具身 Agent 能力基准、欺骗与破坏评测、可纠正性）｜**检索源数量**：候选证据池 36 条，其中与"Agent 评测/安全"直接相关 8 条（[9][10][11][12][28][31][33][35]），弱相关 3 条（[6][7][26]），其余 25 条为主题不重合的 NLP/CV/天体物理/法律问答类共享任务论文。

> **证据范围声明（必读）**：本次调研的候选证据池在"长任务时程（time horizon）""真实计算机/网页/软件工程 Agent 基准""scheming / sabotage / alignment faking 安全评测套件""可纠正性（corrigibility）""AgentDojo / InjecAgent / AgentHarm""Inspect / Petri 评测框架"等核心维度上**存在系统性覆盖缺口**（q1 的三项关键主题均判为零覆盖，q3 的召回结果为视频热度预测、主观性检测等无关论文）。以下报告严格限于可用证据，凡证据池未覆盖者一律标注 `> 待核实`，**不引用池外编号、不虚构论文、不给未见于来源的数字**。因此本报告的主要价值在于：可核查的增量（SE/代码类 Agent 基准与权限安全）+ 明确的证据缺口清单 + 可证伪预测。

---

## 1. 进展与热点（Progress & Hotspots）

**一句话增量判断**：相对 2024 年基线，2026 年 Agent 评测的真实增量集中在"**基准的抗污染与抗虚高**"这一条线上——从静态 SWE-bench 走向持续更新的 live 基准、并首次用对抗性手段量化"测试即 oracle"导致的成功率虚高；而欺骗/破坏/可纠正性评测在本次证据池中**无任何增量证据**。

### 1.1 软件工程（SWE）Agent 基准：从"刷榜"转向"防作弊"
- **SWE-bench Goes Live**（[9]）：把 SWE-bench 从固定快照改为持续刷新的 live 版本，直接针对训练数据污染与过拟合问题。这是"基准生命周期管理"层面的增量，而非模型能力增量。
- **SWE-Bench Pro Verified**（[12]）：定位为"可靠基准"，强调任务筛选与验证流程，说明社区已承认原始 SWE-bench 的可靠性质疑是结构性问题。
- **SWE-ABS**（[10]）：提出对抗性基准强化方法，并**报告了基于测试的基准上成功率被高估**（inflated success rates）。这是 2024-2026 间最具方法论意义的增量之一：它把"通过测试 ≠ 解决问题"从经验抱怨升级为可量化的偏差度量。
- **SWE-Gym**（[11]）：提供可执行环境与训练/验证（verifier）流程，属于"训练-评测同栈"的工程化增量，使得 verifier 本身成为可评测对象。
- 证据强度：以上 4 条均为 arXiv 预印本（B 级）；`[10][12]` 的 ID 时间戳落在 2026 年，`[9]` 为 2025-05 前后，`[11]` 为 2024-12。**是否已被独立复现或写入第三方榜单：`> 待核实`**（候选块未提供引用数、榜单排名或复现报告）。

### 1.2 Agent 行为安全：从"越狱"转向"权限最小化"
- **When Lower Privileges Suffice: Investigating Over-Privileged Tool Selection in LLM Agents**（[35]）：把安全评测对象从"输出是否有害"移到"**工具调用是否授予了超出必要的权限**"，这是 Agent 安全评测中一条可操作、可量化的口径（权限过度授予率）。相对 2024 年主流的提示注入/越狱评测，这是**评测对象**的增量而非仅是样本增量。
- 证据强度：B 级（arXiv，2026-06 前后）。`> 该工作是否提供开源 harness 与第三方复现：待核实`。

### 1.3 评测方法论：可测试的高层标准与纵向失效
- **ELOQUENT 2025 Sensemaking 共享任务**（[26]）：目标是"为生成模型建立易于测试的高层判据"，其思路（把抽象能力拆成可判分的分级步骤）与 Agent 能力基准的构建方法论同源，可作为"高层能力→可测指标"设计范式的外部参照。
- **LongEval at CLEF 2025**（[28]）：纵向（longitudinal）追踪 IR 模型性能随时间的**退化**，为"基准会随时间失效"提供了可复用的实验设计与度量口径，可直接迁移到 Agent 基准的时效性管理。
- **SBFT 2025 Java 测试生成赛道**（[33]）：自动化测试生成竞赛——与 §1.1 中"测试作为 oracle 是否可靠"（[10]）构成互补：oracle 本身正在成为被评测对象。
- 证据强度：B 级（共享任务/竞赛描述论文）。

### 1.4 明确判定为"本周期无增量证据"的维度
| 维度 | 判定 | 依据 |
|---|---|---|
| 长任务时程（time horizon，按人类完成时长度量） | **零覆盖** | 候选池无任何 time horizon / long-horizon 评测设定，[2][3][4][5] 分别为物理常识、篇章关系分类、法律多模态 QA、ESG 承诺核验 [2][3][4][5] |
| 真实计算机/网页交互基准（OSWorld/WebArena 类） | **零覆盖** | [4] 为静态文档检索问答，无 GUI/浏览器可执行交互；[3] 为单步分类，macro-accuracy 71.28，非任务完成度 [3][4] |
| scheming / sabotage / alignment faking | **零覆盖** | [5] 虽名含"promise verification"，但核验对象是企业 ESG 文本承诺，非模型自身策略性欺骗，**必须排除误引** [5] |
| 可纠正性（corrigibility）/ 安全中断 | **零覆盖** | 仅命中 1974 年"安全停机系统可靠性"（航电/可靠性工程语境），与 AI 可纠正性非同一问题域 [23] |

结论：**"能力评测与安全评测是否脱节"这一争议，在本次证据池中无法回答**（`> 待核实`），但可从结构上观察到一个信号：能力侧证据（[9][10][11][12]）与安全侧证据（[35]）**出自完全不同的文献群，互不引用**——这本身是脱节的间接（弱）证据，等级 C，**不作为结论**。

---

## 2. 工业界与产品（Industry & Product）

**一句话增量判断**：工业界在 Agent 评测上的可见动作以"**把基准做成持续运行的服务/榜单**"为主（Live 化 [9]、Pro Verified 认证化 [12]），而非发布新的安全评测产品；实验室 RSP/Preparedness Framework 与 Inspect/Petri 等评测框架在本证据池中**无一手证据**。

- **榜单/基准产品化**：SWE-bench Goes Live（[9]）与 SWE-Bench Pro Verified（[12]）代表两种产品形态——*滚动更新的 live 榜单*与*带验证徽章的静态集*。二者的共同前提是承认原基准已被污染/饱和，这已成为工业界共识性假设（B 级）。
- **训练-评测一体栈**：SWE-Gym（[11]）把可执行环境、轨迹数据与 verifier 训练打包，说明"评测 harness"正被吸收进训练管线——副作用是评测与训练的边界模糊，**scaffold 敏感性上升**（见 §4）。
- **安全侧产品化缺证**：企业 RSP / Preparedness Framework、第三方评测机构（UK/US AISI 等）如何把欺骗/破坏评测写入发布门禁，本次仅拿到**政策研究类**证据（[30][31]），**无任何厂商一手文档或评测报告**，`> 待核实`。
- **评测框架（Inspect / Petri / 可复现 harness）**：本次检索**完全未召回**相关一手文档或仓库，`> 待核实`。**不得**据此推断其不存在或未被采用——这是检索覆盖缺陷，不是事实判断。

> [R] 传闻级：社区普遍认为"Agent 榜单分数与真实部署表现存在系统性差距"，本证据池仅提供间接支持（[10] 的成功率虚高），**其余为待证实**。

---

## 3. 蓝海与缺口（Blue Ocean & Gaps）

**一句话增量判断**：最大的蓝海不是"再造一个能力基准"，而是**三类当前几乎无人做、但杠杆极高的评测基础设施**——(a) 时程/持续性与可纠正性度量；(b) 欺骗检测的假阳性-假阴性权衡曲线；(c) oracle 可靠性审计。

1. **可纠正性（corrigibility）的可测量化——明显无人区**。本次证据池零覆盖（[23] 属可靠性工程，不可类比）。缺口具体为：如何构造"人类中断/纠正"的干预实验，并给出可复现指标（纠正响应延迟、纠正后行为保持率、隐性抵触率）。`> 待核实`：是否已有团队给出标准协议。
2. **时程（time horizon）度量口径**。缺口：以人类完成时长分位（如 50%/95% 人类时长）为横轴、成功率为纵轴的能力曲线，以及"成功率-时程"外推的方法学争议。本次零证据（[2][3][4][5] 均非交互式长任务）。
3. **欺骗/破坏评测的判别效度（discriminant validity）**。缺口：假阳性（把探索性行为误判为 scheming）与假阴性（评测情境被模型识别后"表现良好"）的量化；本次仅 [5] 的"承诺核验"在术语上易混淆，需明确排除 [5]。
4. **oracle 审计（最被低估的缺口）**。[10] 证明"测试即 oracle"会系统性高估成功率；配套缺口是：**没有任何证据表明社区已建立 oracle 强度分级标准**（弱测试/强测试/对抗测试）。[33]（自动测试生成竞赛）提供了可复用的算力与人才池，但两者尚未合流。
5. **评测污染与 scaffold 敏感性的联合度量**。「Live 化」（[9]）+「纵向退化」（[28]）各自成立，但"同一模型在不同 harness 下的分数方差"这一项在本次证据池中**零覆盖**。`> 待核实`。
6. **权限/能力边界评测**。目前仅见单一工作（[35]）把"过度权限工具选择"作为评测对象，属**高杠杆低竞争**方向：可扩展为工具调用最小权限的自动化审计。

---

## 4. 瓶颈与拐点（Bottleneck & Inflection）

**一句话增量判断**：拐点信号出现在"**基准的可信度成本超过其构建成本**"——当基准本身需要对抗性强化（[10]）、持续 Live 化（[9]）与 Pro 验证（[12]）三重维护才能使用时，评测已从"一次性数据集"变成"需长期运营的基础设施"。

| 瓶颈 | 具体表现（带证据） | 拐点信号 | 证据强度 |
|---|---|---|---|
| **Oracle 失效** | 基于测试的基准成功率被证明虚高 [10]；测试生成本身成为竞赛对象 [33] | 出现"oracle 强度分级"成为论文标配要求 | B（预印本） |
| **污染与饱和** | SWE-bench 需 Live 化 [9]、需 Pro Verified 认证 [12] | 静态基准被期刊/会议拒收为唯一证据 | B |
| **评测时效衰减** | IR 领域已系统测量模型性能随时间退化 [28] | Agent 基准开始报告"发布时间戳 + 复查周期" | B（跨领域类比，C 级迁移） |
| **scaffold 敏感性** | 训练与评测同栈（[11]）使 harness 成为混杂变量 | 榜单要求同时提交 scaffold 配置与消融 | `> 待核实`（本次无直接证据） |
| **安全评测不可测量** | 可纠正性/欺骗检测零覆盖；仅权限维度可操作 [35] | 出现可复现的干预式（intervention-based）协议 | `> 待核实` |
| **成本/人力** | 对抗性强化 [10]、Live 维护 [9] 均需持续人力 | 基准维护方从学术团队转为机构化运营 | C（推断） |

**判断**：能力评测侧已过拐点（进入"运营化"阶段）；安全评测侧**尚未到拐点**，卡点在"缺乏可干预、可判分的实验范式"，而非缺数据或缺算力（此判断置信度：中，依据为证据池中安全类仅 1 条且为权限维度 [35]）。

---

## 5. 社会·政策·国际（Society, Policy & Geopolitics）

**一句话增量判断**：可见增量集中在"**AI 安全研究所（AISI）之间的国际信息共享机制设计**"，仍处政策研究阶段，尚未看到评测标准被写入法规或采购条款的一手证据。

- **国际 AISI 网络的信息共享**（[31]）：讨论 UK 与 US AISI 应向国际 AISI 网络共享何种信息、机会与风险，并给出试探性提案。这直接关系到"某国做出的 Agent 欺骗/破坏评测结果能否跨境互认"——即**评测结果的政治可比性**问题（B 级，2025）。
- **政府作为 AI 数据提供者的评估方法**（[30]）：方法学讨论 UK 政府当前作为 AI 数据提供者的角色。与"公共数据用于训练/评测带来的污染与合规"间接相关（B 级）。
- **监管落地（EU AI Act、各国 GPAI 行为准则、NIST 评测指南）**：本次证据池**零覆盖**，`> 待核实`。**不得**据本报告推断任何条款生效状态。
- **伦理与劳动影响**：本次零覆盖（[27] 讨论"对 AI 预测的信任会收窄个体考虑的未来"，属人-AI 决策的行为学，非 Agent 安全治理），`> 待核实` [27]。
- **地缘/供应链**：无证据，`> 待核实`。

**结构性含义（推断，C 级）**：若评测结果需跨境互认（[31]），则**评测协议的可复现性与 oracle 可靠性**（[10]）将从学术规范升级为准入条件——这是能力评测与安全治理之间目前最可能率先打通的接口。

---

## 6. 资本与生态（Capital & Ecosystem）

**一句话增量判断**：本周期在本证据池中**无显著变化的可核查证据**（无融资、并购、人才流动、公司格局的一手来源），仅能观察到"基准维护方生态位"的形成。

- **基准即生态位**：SWE 系基准已形成"live 榜单（[9]）+ 认证集（[12]）+ 训练环境（[11]）+ 对抗审计（[10]）+ 自动测试生成社区（[33]）"的分工，这构成事实上的评测生态（B 级，由 4 篇独立论文的结构关系推断，**非机构声明**）。
- **投资/并购/融资额**：`> 待核实`（候选池无任何来源）。
- **人才流动**：`> 待核实`。
- **社区规模信号（GitHub star、下载量、榜单提交数）**：候选块**未提供任何 stars/citations 字段**，全部标 `> 待核实`，**不填数字**。
- **评测框架生态（Inspect / Petri / HELM 式规范）**：零召回，`> 待核实`。

> 结论：本章为**证据不足章**。为避免虚构成因，本章不给出任何量化判断；下一周期应定向检索基准仓库 star 增速、榜单提交曲线与厂商评测团队招聘信号。

---

## 7. 信号与预测（Signals & Forecast）

### 7.1 早期信号（带证据）
- **S1（较强）**：评测重心从"模型能否通过测试"转向"测试是否可信"——[10] 量化虚高、[33] 把测试生成列为竞赛、[12] 强调 Verified。三者独立指向同一方向。
- **S2（中）**：基准从"数据集"变为"服务"——[9] 的 Live 化与 [28] 的纵向复查机制同构。
- **S3（弱）**：Agent 安全评测从"内容有害性"转向"行为权限边界"——[35] 为唯一证据，N=1，`> 待核实` 是否形成趋势。
- **S4（弱，跨域类比）**：评测结果的跨境互认需求已被政策研究提出（[31]），但尚无标准草案证据。

### 7.2 可证伪预测（6–18 个月，即 2026-10 至 2028-04）

| # | 预测（标 [P]） | 依据链 | 置信度 | 证伪条件 |
|---|---|---|---|---|
| P1 | 到 2027 年底，主流 SE/计算机 Agent 榜单将**强制要求**报告 oracle 强度或对抗测试设置 | S1：[10] 已量化虚高 + [12] 已引入 Verified 概念 | 中高 | 若 2027-12 前 arXiv/榜单中仍无以 oracle 可靠性为必备报告项的基准，则判为不成立 |
| P2 | 出现至少一个**干预式可纠正性基准**（含人类中断/纠正协议与可复现指标），并被 ≥2 个独立团队使用 | S3 缺口 + [23] 仅可靠性工程类比 → 需求明确但供给为零 | 中 | 若 2028-04 前无任何带开源协议的可纠正性评测集，则判为不成立 |
| P3 | "权限最小化"成为 Agent 安全评测的标准子项（而不只是单篇工作） | [35] 提供可操作口径；与工具调用生态天然契合 | 中 | 若 2027-12 前无第二个独立团队发布同类工具权限评测，则判为不成立 |
| P4 | 静态能力基准（非 live、非验证）在顶会作为主要贡献被接受的比率显著下降 | [9][12] 的双重挤压 | 中低 | 若 2027 年顶会仍大量接收纯静态新基准且无污染/验证讨论，则判为不成立 |
| P5 | 欺骗/破坏（scheming/sabotage）评测在 2027 年前**仍不会有被第三方独立复现的标准化套件** | 本次证据池零覆盖 + 判别效度难题未解 | 低-中 | 若 2027-06 前出现 ≥2 篇独立复现同一 deception 评测套件的论文，则判为不成立 |

### 7.3 不确定性声明
- **未知（需数据）**：时程基准现状、OSWorld/WebArena 类基准的最新版本与任务数、AgentDojo/InjecAgent/AgentHarm 的当前指标、Inspect/Petri 的采用率、各实验室 RSP 中欺骗评测的具体阈值——**本次均无一手证据，全部 `> 待核实`**。
- **争议（[Debated]）**："能力评测与安全评测是否脱节"——本证据池无法判定；正反双方证据均缺失。
- **本报告最大风险**：候选证据池严重偏斜（36 条中约 25 条为主题无关的共享任务论文），任何"领域整体趋势"的强断言都不成立。本报告因此**主动降级**了 §2、§5、§6 的结论强度。

---

## 附：经典与奠基性工作（本次证据池可支撑部分）

> 说明：候选池中**缺少**可纠正性（corrigibility）、安全中断（safely interruptible agents）、提示注入（prompt injection）、AgentDojo/InjecAgent/AgentHarm 等奠基文献的一手来源，故下表**不含**这些条目——`> 待核实`，需补充检索后再补全，不得以记忆填充。

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| SWE-bench Goes Live! | 2025 | `> 待核实`（候选块未给作者/机构） | `> 待核实` | arXiv 预印本（B），主题为基准方法学 [9] | 中：直接回应污染问题，属结构性议题 [9] | ★★★★☆ 理解"基准生命周期"必读 | http://arxiv.org/abs/2505.23419v2 | 把 SWE-bench 改为持续更新的 live 基准 [9] |
| SWE-ABS: Adversarial Benchmark Strengthening | 2026 | `> 待核实` | `> 待核实` | arXiv 预印本（B）[10] | 中高：给出成功率虚高的量化证据 [10] | ★★★★★ 本报告认为最关键的评测方法学增量 | http://arxiv.org/abs/2603.00520v1 | 对抗性强化暴露 test-based 基准成功率虚高 [10] |
| SWE-Bench Pro Verified | 2026 | `> 待核实` | `> 待核实` | arXiv 预印本（B），自述"可靠基准" [12] | 中：Verified 认证思路 [12] | ★★★★☆ 观察"验证徽章"制度化路径 | http://arxiv.org/abs/2609.08149v3 | 强调任务筛选与可靠性 [12] |
| When Lower Privileges Suffice | 2026 | `> 待核实` | `> 待核实` | arXiv 预印本（B）[35] | 中：唯一命中 Agent 行为安全的证据 [35] | ★★★★☆ Agent 安全评测中少见的可量化口径 | http://arxiv.org/abs/2606.20023v2 | 过度权限工具选择调查 [35] |
| LongEval at CLEF 2025 | 2025 | `> 待核实` | `> 待核实` | 评测实验室共享任务（B）[28] | 中：纵向评测设计被广泛复用 [28] | ★★★☆☆ 迁移其"时效衰减"度量到 Agent 基准 | http://arxiv.org/abs/2503.08541v1 | IR 模型性能的纵向评测 [28] |
| Reliability and availability of a safely shutdown system | 1974 | `> 待核实` | citations=0 [23] | Microelectronics Reliability（A 级期刊，但**非 AI 领域**）[23] | 低：citations=0，且问题域不同 [23] | ★☆☆☆☆ 仅作"可纠正性"术语溯源时的反例，勿误引 | https://doi.org/10.1016/0026-2714(74)90036-5 | 航电/可靠性工程中的安全停机，非 AI 可纠正性 [23] |

## 附：开源项目（本次证据池可支撑部分）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| SWE-Gym | 2024 | `> 待核实` | `> 待核实`（stars 未提供） | arXiv 预印本（B）[11] | 中：训练+verifier 一体栈 [11] | ★★★★☆ 想复现 SE Agent 训练-评测闭环的起点 | http://arxiv.org/abs/2412.21139v2 | 用可执行环境训练 SE Agent 与 verifier [11] |
| （Inspect / Petri / AgentDojo / InjecAgent / AgentHarm） | — | — | `> 待核实` | `> 待核实` | `> 待核实` | — | `> 待核实` | **本次检索零召回，不得臆测其仓库状态** |

## 附：数据集与基准

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| SWE-bench Live | 2025 | `> 待核实` | `> 待核实` | 预印本（B）[9] | 中高 [9] | ★★★★☆ 抗污染首选 | http://arxiv.org/abs/2505.23419v2 | 持续更新的 SWE 任务流 [9] |
| SWE-Bench Pro Verified | 2026 | `> 待核实` | `> 待核实` | 预印本（B）[12] | 中 [12] | ★★★★☆ 需"已验证子集"时使用 | http://arxiv.org/abs/2609.08149v3 | 经筛选验证的 SE Agent 基准 [12] |
| SWE-ABS（对抗强化协议） | 2026 | `> 待核实` | `> 待核实` | 预印本（B）[10] | 中高 [10] | ★★★★★ 作为"基准体检工具"而非新数据集 | http://arxiv.org/abs/2603.00520v1 | 用于检测既有 test-based 基准的虚高 [10] |
| ELOQUENT 2025 Sensemaking | 2025 | `> 待核实` | `> 待核实` | 共享任务（B）[26] | 中低：评测设计范式参考 [26] | ★★☆☆☆ 仅借其"高层判据可测试化"思路 | http://arxiv.org/abs/2507.12143v1 | 分层可判分的高层能力评测 [26] |
| LongEval 2025 | 2025 | `> 待核实` | `> 待核实` | 评测实验室（B）[28] | 中 [28] | ★★★☆☆ 时效性管理参照 | http://arxiv.org/abs/2503.08541v1 | 纵向性能退化评测 [28] |
| VLSP 2025 MLQA-TSR | 2025 | `> 待核实` | `> 待核实` | 挑战赛描述（B）[4] | 低：区域赛事，非 Agent 交互 [4] | ★☆☆☆☆ 与 Agent 评测无关，列入仅为界定边界 | http://arxiv.org/abs/2510.20381v1 | 越南语交通标志法规多模态 QA [4] |
| FormaMentis（MRL 2025） | 2025 | `> 待核实` | `> 待核实` | 共享任务提交（B）[2] | 低 [2] | ★☆☆☆☆ 静态常识 QA，非 Agent 基准 [2] | http://arxiv.org/abs/2510.22631v1 | 意/英物理常识基准 [2] |

---

## 下一周期必补检索清单（Gap Checklist）

1. **time horizon / long-horizon agent benchmark**（含人类时长分位口径）——本次零覆盖。
2. **OSWorld / WebArena / VisualWebArena** 最新版本、任务数与独立复现——本次零覆盖。
3. **AgentDojo / InjecAgent / AgentHarm / Petri / Inspect** 一手论文与仓库——本次零覆盖。
4. **corrigibility / safely interruptible agents** 奠基文献——本次仅有 1974 年非 AI 文献 [23]，不可用。
5. **RSP / Preparedness Framework / AISI 评测协议** 一手文档——本次仅有政策研究 [30][31]。
6. **GitHub star / 引用数 / 榜单提交数**等热度字段——本次候选块全缺，须改从 GitHub API 与 Semantic Scholar/OpenAlex 补齐。

> 再次声明：以上 6 项缺口内的任何具体结论，本报告**一律未作断言**，全部标注 `> 待核实`。

---

## 参考来源

[1] Annif at SemEval-2025 Task 5: Traditional XMTC augmented by LLMs — http://arxiv.org/abs/2504.19675v2
[2] Culturally Grounded Physical Commonsense Reasoning in Italian and English: A Submission to the MRL 2025 Shared Task — http://arxiv.org/abs/2510.22631v1
[3] DeDisCo at the DISRPT 2025 Shared Task: A System for Discourse Relation Classification — http://arxiv.org/abs/2509.11498v4
[4] VLSP 2025 MLQA-TSR Challenge: Vietnamese Multimodal Legal Question Answering on Traffic Sign Regulation — http://arxiv.org/abs/2510.20381v1
[5] CLaC at SemEval-2025 Task 6: A Multi-Architecture Approach for Corporate Environmental Promise Verification — http://arxiv.org/abs/2505.23538v1
[6] NALA_MAINZ at BLP-2025 Task 2: A Multi-agent Approach for Bangla Instruction to Python Code Generation — http://arxiv.org/abs/2511.16787v1
[7] MRT at IberLEF-2025 PRESTA Task: Maximizing Recovery from Tables with Multiple Steps — http://arxiv.org/abs/2507.12981v1
[8] DNB-AI-Project at SemEval-2025 Task 5: An LLM-Ensemble Approach for Automated Subject Indexing — http://arxiv.org/abs/2504.21589v1
[9] SWE-bench Goes Live! — http://arxiv.org/abs/2505.23419v2
[10] SWE-ABS: Adversarial Benchmark Strengthening Exposes Inflated Success Rates on Test-based Benchmark — http://arxiv.org/abs/2603.00520v1
[11] Training Software Engineering Agents and Verifiers with SWE-Gym — http://arxiv.org/abs/2412.21139v2
[12] SWE-Bench Pro Verified: A Reliable Benchmark for Software Engineering Agents — http://arxiv.org/abs/2609.08149v3
[13] NTU-NPU System for Voice Privacy 2024 Challenge — http://arxiv.org/abs/2410.02371v1
[14] The Reactive Synthesis Competition: SYNTCOMP 2016 and Beyond — http://arxiv.org/abs/1611.07626v1
[15] The 3rd Reactive Synthesis Competition (SYNTCOMP 2016): Benchmarks, Participants & Results — http://arxiv.org/abs/1609.00507v2
[16] 2nd Workshop on Cognitive Architectures for Social Human-Robot Interaction 2016 (CogArch4sHRI 2016) — http://arxiv.org/abs/1602.01868v1
[17] 5th International Symposium on New Frontiers in Human-Robot Interaction 2016 (NF-HRI 2016) — http://arxiv.org/abs/1602.05456v2
[18] Theory @ Hard Probes 2015 — http://arxiv.org/abs/1510.04133v2
[19] Exponential Speedups by Rerooting Levin Tree Search — http://arxiv.org/abs/2412.05196v2
[20] CHARM-2015 Theory Summary — http://arxiv.org/abs/1510.05797v1
[21] Historical light-curve and the 2016 outburst of the symbiotic star StHa 169 — http://arxiv.org/abs/1607.06312v1
[22] Discovery Opportunities with Gravitational Waves -- TASI 2024 Lecture Notes — http://arxiv.org/abs/2409.08956v1
[23] Reliability and availability of a safely shutdown system — https://doi.org/10.1016/0026-2714(74)90036-5
[24] Atmospheric entry and fragmentation of small asteroid 2024 BX1 — http://arxiv.org/abs/2403.00634v2
[25] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1
[26] Overview of the Sensemaking Task at the ELOQUENT 2025 Lab: LLMs as Teachers, Students and Evaluators — http://arxiv.org/abs/2507.12143v1
[27] Faith in AI can narrow the futures individuals consider — http://arxiv.org/abs/2603.28944v2
[28] LongEval at CLEF 2025: Longitudinal Evaluation of IR Model Performance — http://arxiv.org/abs/2503.08541v1
[29] DeBiasMe: De-biasing Human-AI Interactions with Metacognitive AIED (AI in Education) Interventions — http://arxiv.org/abs/2504.16770v1
[30] Methods to Assess the UK Government's Current Role as a Data Provider for AI — http://arxiv.org/abs/2412.09632v2
[31] Which Information should the UK and US AISI share with an International Network of AISIs? Opportunities, Risks, and a Tentative Proposal — http://arxiv.org/abs/2503.04741v1
[32] AI Wizards at CheckThat! 2025: Enhancing Transformer-Based Embeddings with Sentiment for Subjectivity Detection in News Articles — http://arxiv.org/abs/2507.11764v1
[33] SBFT Tool Competition 2025 -- Java Test Case Generation Track — http://arxiv.org/abs/2504.09168v1
[34] AIRCC-Clim: a user-friendly tool for generating regional probabilistic climate change scenarios and risk measures — http://arxiv.org/abs/2111.01762v1
[35] When Lower Privileges Suffice: Investigating Over-Privileged Tool Selection in LLM Agents — http://arxiv.org/abs/2606.20023v2
[36] NTIRE 2025 Challenge on Image Super-Resolution (x4): Methods and Results — http://arxiv.org/abs/2504.14582v3

---

*Generated by research-bot · topic=`agent-评测与安全能力基准欺骗与可纠正性` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`deepseek-v4-flash` · sources=36 · duration=180s · 2026-10-22T22:32:43+00:00*
