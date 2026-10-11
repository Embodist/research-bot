# 具身智能与视觉-语言-动作（VLA）前沿增量调研快照

**元信息**：日期 2026-10-11（UTC）｜领域：Embodied AI / Vision-Language-Action（VLA）/ 机器人操作与评测｜检索源：本次可用来源共 **33 条**（编号 [1]–[33]），其中与具身智能/VLA 直接或间接相关者 **21 条**，明确与主题无关者 **12 条**（[1][14][23][24][26][27][28][29][30][31][32][33]）｜引用规范：仅引用给定编号，凡无来源支撑处标 `> 待核实`。

> **证据基础声明（先说结论的边界）**：本快照的来源集合存在显著**主题漂移**：12 条来源属于临床问答、表情包分类、语音防伪、铁路安检、机械加工等无关领域 [1][26][27][28][29][31][32][33]。剩余来源中，多数为 arXiv 预印本与综述，**缺少厂商一手公告、榜单原始表格、GitHub star/下载量等热度数据**。因此本报告遵循"缺口外显"原则：能证实的写实，不能证实的写 `> 待核实`，不以模型记忆补足。此外，部分来源的编号段（如 26xx 系列）与 DOI 未在本次调研中被独立打开核验，报告仅按给定编号引用，**不对其链接可达性作断言**，读者引用前应自行核验。

---

## 1. 进展与热点（Progress & Hotspots）

**一句话增量判断**：相对 2024 年"堆 VLA 模型刷榜"的基线，2025–2026 年的增量重心正从**能力侧**（造更大的 VLA）转向**部署侧**——推理期可干预性、失败/偏差可检测性、以及"人类视频替代机器人演示"的数据路线；同时领域进入**综述整合期**。

| # | 增量条目 | 时间 | 类型 | 相对基线的"新" | 证据强度 |
|---|---|---|---|---|---|
| 1 | **Learning to Fold**（LeHome Challenge 2026，ICRA 2026 双臂叠衣竞赛） | 2026 | 竞赛方案（作者自述） | 用 RL 回路增强 VLA 策略；在线仿真 62 队中第 1、真机决赛第 2 | 自评/竞赛排名，**无第三方复现** [2] |
| 2 | **Inference-Time Attention Steering for VLA Driving Models** | 2026 | 方法论文 | 在不重训的前提下，于推理期对视觉 token 加有界 pre-softmax 注意力偏置，把注意力重定向到安全关键目标 | 预印本，单篇 [3] |
| 3 | **From Human Videos to Robot Manipulation: A Survey** | 2026 | 综述 | 指出机器人演示"昂贵且与本体强耦合"，将 human-centric data 作为可扩展 VLA 学习主线 | 综述，无实验数据 [5] |
| 4 | **Evolve VLA Model into an Agent with On-the-fly Tool-use** | 2026 | 方法论文 | 从"单一策略"走向"带即时工具调用的 agent 化 VLA" | 预印本，单篇 [9] |
| 5 | **注意力头可用于路径偏差检测 / 时间感知失败检测** | 2026 / — | 方法论文 + 学位论文 | 把 VLA 内部注意力和时序信号当作**监控与故障诊断接口** | [10] 预印本；[12] 博士论文（NTU 体系） |
| 6 | **VLA 综述密集出现**（操作、装配、真实应用三类） | 2025–2026 | 综述群 | 领域 taxonomy 从分散走向收敛，标志"从爆发到整合" | [4][7][11] |

**"已被验证"与"仅官方演示/自评"的区分**：
- **仅自评/竞赛排名，未获独立复现**：LeHome 冠军方案明确是作者自述其成绩（1st of 62 teams online；2nd offline），属于竞赛自评口径而非第三方复现 [2]。其"RL 回路改进 VLA"的增益幅度、真机成功率数字在本快照中不可得 `> 待核实`。
- **仅方法声明，无跨任务/多本体验证证据**：推理期注意力引导 [3]、注意力头偏差检测 [10]、agent 化 VLA [9] 在本快照中均只有单篇来源，未见第三方复现报告或榜单纳入 `> 待核实`。
- **本快照未检索到任何第三方排行榜（如操作类真机榜单）的原始表格**，因此**无法断言任何模型在 2026 年处于 SOTA** `> 待核实`。

**热度/权威/关注度/推荐度（关键条目）**
- LeHome 方案 [2]：热度 `> 待核实`（无引用数）；权威=cs.RO 预印本 + ICRA 2026 竞赛背景；关注度**中**（有竞赛排名与 62 队规模这一可观测信号）；推荐度 **★★★★☆**——具身"真机决赛"样例稀缺，值得读其 RL+VLA 组合细节。
- 注意力引导 [3]：热度 `> 待核实`；权威=cs.CV 预印本；关注度**低**（无引用/无复现证据）；推荐度 **★★★☆☆**——思路（免重训的可控性）比结果更有价值。
- Human-centric data 综述 [5]：热度 `> 待核实`；权威=预印本综述；关注度**中**（切中数据成本这一公认痛点）；推荐度 **★★★★☆**——适合作为数据路线选型的起点文献。
- 操作 VLA 综述 [4]：热度 `> 待核实`；权威=cs.RO 综述（v3 版本说明在持续更新）；关注度**中高**（同题材综述同期出现多篇，本身即热度信号 [4][7][11]）；推荐度 **★★★★☆**——taxonomy 骨架可直接复用。

---

## 2. 工业界与产品（Industry & Product）

**一句话增量判断**：**本周期在本次检索中，缺少可核查的产业一手证据**；所有"厂商发布/出货/部署"类判断均无法在本来源集内成立，全部标 `> 待核实`。

- **可确证的相关事实（弱）**：来源 [15] 为 **2025 Foundation Model Transparency Index**（该年度性透明度量化工作的**第三版**），其证据文本将基础模型开发者描述为"世界上最重要的一批公司"，并追问其透明度实践如何演变 [15]。这与 VLA 的关系是**间接的**——大量 VLA 建立在基础模型之上，但该指数**并非机器人专用**，不能据此推断任何机器人厂商或具身产品的透明度/合规状况 [15]。
- **仅可作线索、不足以立论者**：来源 [20] 为一篇 Medium 平台上的"机器人基础模型技术综述"，按证据分级属 **D 级（个人/平台发布）**，仅可作检索线索，其中的任何数字与结论都必须另找高等级来源，否则 `> 待核实` [20]。
- **开源权重与闭源对照（产品化视角的结构性观察）**：本快照能定位到的开放权重/开源路线包括 **Octo**（Open-Source Generalist Robot Policy）[13]、**OpenVLA**（Open-Source VLA Model）[18]、**CLIP-RT**（语言条件策略的自然语言监督）[19]；而 **RT-2** 是奠基性的闭源工作，仅有论文可依 [17][21]。**这些仓库的 star 数、最近提交时间、权重可下载性在本快照中均无数据** `> 待核实`——请勿据此判断项目活跃度。
- **竞赛即"工程落地压力测试"**：LeHome Challenge 2026 设置了**在线仿真轮 + 真机决赛**两段式赛制，这本身是"从仿真走向真机"的工程化信号 [2]；但赛制细节、真机硬件与任务成功率 `> 待核实`。

> **产业维度的缺口结论**：本快照**不足以**支撑"哪家厂商在 2026 年实现 VLA 真机量产/部署"的任何排序。需要补充的来源类型：厂商官方博客/技术报告、产品发布页、批量出货或部署数量的官方口径。

---

## 3. 蓝海与缺口（Blue Ocean & Gaps）

**一句话增量判断**：**"部署侧基础设施"是当前最明显的无人区**——能力侧论文拥挤，而**可干预性、可监控性、可诊断性、跨本体数据**四条线仍处于单篇试点阶段。

| 缺口 | 为什么是缺口（依据） | 杠杆点 | 风险 |
|---|---|---|---|
| **G1. 推理期可控/可干预** | 现有 VLA 通常"不重训就无法把注意力拉向安全关键目标"，这一约束被明确指出 [3] | 免重训的干预接口（注意力偏置、解码约束）可低成本接入已有策略 [3][10] | 缺乏跨任务验证，可能只对特定驾驶/操作域有效 `> 待核实` |
| **G2. 失败与偏差的在线检测** | 出现"VLA 已有注意力头可用于路径偏差检测"[10]与"VLA 时间感知失败检测"[12]两类独立探索，说明需求已被提出但尚未形成标准组件 | 把 VLA 内部表征当**运行时监控信号**，而非只做端到端黑箱 | 学位论文[12]与预印本[10]之间无交叉验证 `> 待核实` |
| **G3. 跨本体数据规模化** | 机器人演示"昂贵且与特定本体强耦合"，而人类视频被视为可扩展替代 [5] | 人类视频 → 机器人策略的迁移与统一动作空间 | 综述自承这是难点；本快照无成功率的可核查数字 [5] |
| **G4. Agent 化 / 工具调用** | 有工作尝试把 VLA 进化为"带即时工具调用（on-the-fly tool-use）的 agent"[9] | 让策略在运行时调用外部工具/求解器补足精度 | 单篇、早期，泛化性未知 [9] |
| **G5. 跨本体 + 真机的统一评测** | 本快照能定位的评测均为**竞赛/挑战**形态（叠衣竞赛[2]、开放多智能体系统评测 MOASEI 2026[25]），而非可长期追踪的模型榜单 | 建立跨本体、真机、可复现、公开榜单的评测基础设施 | 竞赛结果不等同于榜单化能力度量；MOASEI 面向多智能体开放系统而非操作任务 [25] |

**注意 G5 的一个细节**：MOASEI 2026 是**多智能体开放系统**评测（保留 wildfire fighting、cybersecurity 等赛道），并非机械臂操作基准 [25]。把它误读为"VLA 操作榜单"是典型陷阱——本报告明确不作此关联。

> **待补检索项（本快照未获得可引用来源，故不给链接以免臆造）**：具身操作领域公认的若干基准/数据集（如 Open X-Embodiment、DROID、LIBERO、SimplerEnv 一类）**在本次 33 条来源中一条都未出现**。因此本报告**不列出**它们的名称化条目、年份、机构与链接，仅在"缺口"层面提示：**评测维度的证据链是本次调研最薄弱的一环**，必须补检后再下任何"谁领先"的结论。

---

## 4. 瓶颈与拐点（Bottleneck & Inflection）

**一句话增量判断**：瓶颈分布正从**算力/模型规模**转向**数据成本、评测可信度与推理时可控性**三类；"仿真→真机"的评测迁移是最清晰的可观测拐点信号，但**尚未出现可确认的能力阶跃**。

**四类瓶颈（按本快照证据）**

1. **数据瓶颈（最硬）**：机器人演示获取昂贵、与本体强耦合，是公认的结构性约束，人类视频被提出为替代路径 [5]。这是**公认共识级**的判断（多篇综述同调 [4][5][7]）。
2. **评测瓶颈**：本快照内没有第三方跨本体真机榜单；可比性依赖竞赛 [2][25]，而竞赛的赛题窄（如双臂叠衣）[2]。**"论文宣称"与"第三方评测"之间的鸿沟未被填补**。
3. **工程瓶颈（微调的成本-性能权衡）**：有工作直接以"Fine-Tuning VLA Models: Optimizing Speed and Success"为题，说明**微调速度与成功率之间的权衡**被视为一个真实工程问题 [16]。这暗示"重训/微调代价高"是实际约束——与 [3] 追求"免重训干预"的动机一致，构成**相互印证的两条证据** [3][16]。
4. **可信性与安全瓶颈**：失败检测 [12]、偏差检测 [10] 的出现，反证"VLA 在真机上的失败不可解释/不可预测"仍是未解问题。

**拐点信号（可观测）**

| 信号 | 观测值 | 判定 |
|---|---|---|
| 竞赛增设真机决赛 | LeHome 2026 设在线仿真轮 + 真机决赛，作者取得 1st online / 2nd real [2] | **弱信号**：评测开始惩罚"只在仿真里能跑"的方案 |
| 综述数量与版本迭代 | 同期出现多篇 VLA 综述，且部分为 v2/v3 持续更新 [4][7] | **中等信号**：领域进入整合期（此为**推测**，标 `[P]`，见第 7 章） |
| 免重训干预类方法出现 | [3] 明确以"不重训"为卖点 | **弱信号**：部署成本已成为方法设计的显式约束 |
| 第三方透明度指数持续发布 | FMTI 已出至第三版 [15] | **间接信号**：治理侧对"可核查性"的要求在机制化，但**不针对机器人** |

> **明确的否定结论**：本快照**没有**任何证据支持"VLA 在 2026 年已跨过通用操作的能力拐点"这一说法。任何此类断言均 `> 待核实`。

---

## 5. 社会·政策·国际（Society, Policy & Geopolitics）

**一句话增量判断**：**本维度在本次来源集中几乎无覆盖**；唯一可引用的治理类证据是通用基础模型透明度指数，与具身智能仅间接相关。

- **可引用事实（间接）**：**The 2025 Foundation Model Transparency Index** 是该年度性工作的**第三版**，目标是"刻画并量化基础模型开发者的透明度实践"，并指出随着这些公司影响力上升，其透明度实践如何演变成为一个值得追问的问题 [15]。**可迁移性**：若 VLA 的上游基础模型受此类透明度压力约束，则具身侧的数据来源、评测公开性可能间接受影响——**这属于合理推演而非事实，标 `[P]`**。
- **不可引用的陷阱**：来源 [1]（临床问答）、[28]（BioASQ 生物医学）、[29]（语音防伪）分别属于医疗与语音安全领域；[31]（铁路客站安检流程瓶颈）、[32][33]（传统机械加工瓶颈）属于工业工程。**这些均不能作为具身智能政策、监管或国际格局的证据**，本报告一律不采用。
- **本周期无显著变化**：关于具身智能/机器人的**专门法规、标准、出口管制、供应链与地缘政治**，本次来源集中**没有任何一条可核查来源**。因此本报告在此明确写：**本周期无显著变化的可核查证据** `> 待核实`，而非用常识填充。

> **待补检索建议**：机器人安全标准（如 ISO 体系）、各国 AI 法案对具身系统的适用范围、数据跨境与隐私对"人类视频训练"的合规约束（这一点与缺口 G3 [5] 直接耦合）。

---

## 6. 资本与生态（Capital & Ecosystem）

**一句话增量判断**：**本维度同样缺乏一手证据**；能做的只有"开源 vs 闭源生态结构"的静态描述，**不能**给出融资、并购、人才流动的任何数字。

**生态结构（基于可引用来源的静态观察，非增量结论）**

- **闭源奠基线**：RT-2 代表"把互联网规模多模态知识迁移到机器人控制"的路线，且由 Google DeepMind 提出 [17][21]。对 RT-2 的第三方综述明确指出其"transformative step"定位，该综述发表于 *Advances in Engineering Technology Research*，**citations=3**，属**低热度** [21]。
- **开源权重线**：Octo（Open-Source Generalist Robot Policy）[13]、OpenVLA（Open-Source VLA Model）[18]、CLIP-RT（自然语言监督下的语言条件机器人策略）[19]。**三者的 star/下载/维护活跃度在本快照中均无数据** `> 待核实`。
- **新近工程线**：RT-K 提出关键点感知的 Transformer 框架以提升视觉-语言机器人控制效率，发表于 *Biomimetic Intelligence and Robotics*（2026），**citations=0**，热度极低 [22]。
- **工具与微调生态**：存在面向"微调速度 vs 成功率"优化的专门工作 [16]，以及把 VLA 扩展为工具调用 agent 的探索 [9]——反映生态开始出现"围绕 VLA 的外围工具层"。

**四条证据轴（本条目的可核查性）**

| 条目 | 热度证据 | 权威证据 | 关注度 | 推荐度 |
|---|---|---|---|---|
| RT-2 [17][21] | 第三方综述 citations=3 [21] | 奠基论文 [17] + 期刊综述 [21]（后者为 *Advances in Engineering Technology Research*） | **中**：作为历史基线被反复引用，但综述热度数字低 [21] | ★★★★☆：必读基线，但请直接读原始论文 [17] 而非综述 [21] |
| Octo [13] | `> 待核实` | 预印本 v2，标题自述开源 [13] | `> 待核实` | ★★★★☆：开源通用策略的代表入口 [13] |
| OpenVLA [18] | `> 待核实` | 预印本 v3，标题自述开源 [18] | `> 待核实` | ★★★★★：VLA 工程复现的首选起点（本主题相关性最高）[18] |
| CLIP-RT [19] | `> 待核实` | 预印本 v4 [19] | `> 待核实` | ★★★☆☆：语言监督路线，作为对照项 [19] |
| RT-K [22] | citations=0 [22] | *Biomimetic Intelligence and Robotics*（2026）[22] | **低**（零引用）[22] | ★★☆☆☆：可作效率优化线索，暂不建议作为主要依据 [22] |

> **资本维度结论**：本次来源集中**没有**任何融资、并购、估值、人才流动、公司格局变化的可核查来源。因此本节**不给出任何资本结论**，全部标 `> 待核实`。

---

## 7. 信号与预测（Signals & Forecast）

**一句话增量判断**：本周期最强的新增信号是**"部署侧研究"开始成体系出现**（可控性 [3] + 可监控性 [10][12] + 成本权衡 [16]），而非新的能力 SOTA。

**可证伪假设（每条给依据链 + 置信度 + 证伪条件）**

- **H1 `[P]` 推理期可干预性将成为 VLA 部署的标配组件。**
  - 依据链：现状是"不重训无法重定向注意力"[3] → 微调存在速度/成功率权衡 [16] → 因而免重训干预有明确需求 → 已有注意力头可作检测接口 [10]。
  - **置信度：中低**（依据为少量单篇预印本，无复现）。
  - **证伪条件**：若到 **2027-06** 仍未出现 ≥3 篇 VLA 推理期干预工作，或没有任何第三方基准把"可干预性"纳入评测项，则本假设不成立。

- **H2 `[P]` 人类视频（human-centric data）将成为 VLA 预训练的主流数据路线之一。**
  - 依据链：机器人演示被明确指为"昂贵且与本体强耦合"[5]，而综述将其作为可扩展主线提出 [5]；同题材综述群印证数据问题是核心痛点 [4][7]。
  - **置信度：中**（痛点共识度高，但迁移效果无本快照内证据）。
  - **证伪条件**：若到 **2027-06** 主流 VLA 预训练仍以机器人演示为绝对主数据源、人类视频仅作辅助且无跨本体正迁移的可复现报告，则本假设不成立。

- **H3 `[P]` 失败/偏差检测将从论文走向可独立评测的运行时组件。**
  - 依据链：已同时出现"注意力头做偏差检测"[10]与"时间感知失败检测"[12]两条独立路线 → 说明该问题被独立提出两次以上。
  - **置信度：中低**（两条证据之间无交叉验证，其中一条为学位论文 [12]）。
  - **证伪条件**：若到 **2027-06** 仍无任何公开的、跨任务的 VLA 失败检测基准或可复现评测协议出现，则本假设不成立。

- **H4 `[P]` "仿真到真机"的评测迁移会继续推进，但不会在 12 个月内形成统一榜单。**
  - 依据链：LeHome 已采用仿真轮 + 真机决赛两段式 [2]；但本快照内**不存在**任何跨本体真机统一榜单（缺口 G5）；MOASEI 的评测对象是多智能体开放系统而非操作任务 [25]。
  - **置信度：中**。
  - **证伪条件**：若到 **2027-10** 出现被 ≥3 个独立团队在真机上报告结果的公开 VLA 统一榜单，则本假设不成立。

**Watchlist（值得持续关注的观察点）**
1. 竞赛类评测是否从"单任务赛事"（叠衣 [2]）扩展为多任务、跨本体 [2][25]。
2. 免重训干预与运行时监控是否在方法论文中形成可复用的接口规范 [3][10][12][16]。
3. 人类视频路线的**跨本体正迁移**是否出现可复现报告 [5]。
4. 基础模型透明度机制是否外溢到机器人/具身系统 [15]。

**传闻与不确定性**：本次检索**未获得**任何可标注为 `[R]` 的行业传闻素材（也无融资/发布会类来源），故不设传闻条目；`[Debated]` 争议项同样**无来源可依**，不作虚构。

---

## 附：经典与奠基性工作

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| **RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control** | 2023 | Google DeepMind（据第三方综述[21]表述） | `> 待核实`（无引用数数据） | 奠基性论文（预印本 v1）[17] | 中（被后续综述反复作为基线 [21]） | ★★★★☆ 必读基线 | http://arxiv.org/abs/2307.15818v1 | 将互联网规模多模态知识迁移至机器人控制的里程碑 [17] |
| **RT-2 综述（Comprehensive Review）** | 2025 | *Advances in Engineering Technology Research* | **citations=3** [21] | 期刊综述 [21] | 低（引用数低）[21] | ★★★☆☆ 二手参考 | https://doi.org/10.56028/aetr.15.1.1423.2025 | 对 RT-2 的定位与影响回顾，但请以原始论文 [17] 为准 [21] |
| **Octo: An Open-Source Generalist Robot Policy** | 2024 | `> 待核实` | `> 待核实` | 预印本 v2，标题自述开源 [13] | `> 待核实` | ★★★★☆ 开源入口 | http://arxiv.org/abs/2405.12213v2 | 开源通用机器人策略的代表工作 [13] |
| **OpenVLA: An Open-Source Vision-Language-Action Model** | 2024 | `> 待核实` | `> 待核实` | 预印本 v3（迭代至 v3，说明持续维护）[18] | `> 待核实` | ★★★★★ 本主题相关性最高 | http://arxiv.org/abs/2406.09246v3 | 开源 VLA 的工程复现首选起点 [18] |
| **Grasp and Motion Planning for Dexterous Manipulation (Real Robot Challenge)** | 2021 | `> 待核实` | `> 待核实` | 预印本 [6] | `> 待核实` | ★★☆☆☆ 历史参考 | http://arxiv.org/abs/2101.02842v1 | 灵巧操作抓取与运动规划的早期竞赛类工作 [6] |

## 附：开源项目

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| **OpenVLA** | 2024 | `> 待核实` | `> 待核实`（无 star/下载数据） | 预印本 v3 [18] | `> 待核实` | ★★★★★ | http://arxiv.org/abs/2406.09246v3 | 开源 VLA 模型与权重（可下载性需自行核验）[18] |
| **Octo** | 2024 | `> 待核实` | `> 待核实` | 预印本 v2 [13] | `> 待核实` | ★★★★☆ | http://arxiv.org/abs/2405.12213v2 | 开源通用机器人策略 [13] |
| **CLIP-RT** | 2024 | `> 待核实` | `> 待核实` | 预印本 v4 [19] | `> 待核实` | ★★★☆☆ | http://arxiv.org/abs/2411.00508v4 | 自然语言监督下的语言条件策略 [19] |
| **VLA 微调优化（Speed vs Success）** | 2025 | `> 待核实` | `> 待核实` | 预印本 v2 [16] | `> 待核实` | ★★★★☆ 工程实用 | http://arxiv.org/abs/2502.19645v2 | 直击"微调速度-成功率"权衡这一真实工程瓶颈 [16] |
| **RT-K（关键点感知 Transformer）** | 2026 | `> 待核实` | **citations=0** [22] | *Biomimetic Intelligence and Robotics* [22] | 低（零引用）[22] | ★★☆☆☆ | https://doi.org/10.1016/j.birob.2026.100341 | 面向效率的视觉-语言机器人控制框架 [22] |

## 附：数据集与基准

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| **LeHome Challenge 2026** | 2026 | ICRA 2026 竞赛（参赛方案作者自述 [2]） | `> 待核实`（仅知在线轮 62 队）[2] | 竞赛（赛制含仿真轮 + 真机决赛）[2] | 中（有真机决赛这一可观测信号）[2] | ★★★★☆ | http://arxiv.org/abs/2606.27163v3 | 双臂叠衣任务；冠军方案为 VLA + RL 回路 [2] |
| **MOASEI 2026（AAMAS）** | 2026 | AAMAS'2026 竞赛组织方 [25] | `> 待核实` | 会议技术报告 [25] | 中（第二届，沿用首届赛道）[25] | ★★☆☆☆（**与机械臂操作任务不直接相关**） | http://arxiv.org/abs/2607.03399v1 | 多智能体**开放系统**评测（wildfire/cybersecurity 等），**不是** VLA 操作榜单 [25] |
| **Foundation Model Transparency Index (2025)** | 2025 | 第三方研究项目 [15] | `> 待核实` | 年度性量化项目第三版 [15] | 中（治理侧持续发布）[15] | ★★☆☆☆（间接相关） | http://arxiv.org/abs/2512.10169v1 | 通用基础模型透明度指数，**非机器人专用** [15] |

> **经典具身基准缺失声明**：具身操作领域若干广为人知的公开数据集与仿真基准**在本次 33 条来源中均未出现**。为避免编造链接与数字，本报告**不列出**这些名称化条目；它们应作为下一轮检索的**优先补检清单**（评测维度的证据链是本快照最大缺口）。

---

## 附：证据缺口清单（Gap Check）

| 检查项 | 是否覆盖 | 说明 |
|---|---|---|
| 最新进展（近 1–2 年） | ⚠️ 部分 | 有 2025–2026 的综述与方法类来源 [2][3][4][5][9][10][11][12][16]，但**缺少任何 SOTA 榜单原始数据** |
| 经典工作 | ✅ | RT-2 [17][21]、Octo [13]、OpenVLA [18]、CLIP-RT [19] |
| 开源实现 | ⚠️ 部分 | 有名称与论文链接 [13][18][19]，但**无 star/下载/维护状态数据** |
| 数据集与基准 | ❌ 严重不足 | 仅竞赛类 [2][25] 与一个泛化指数 [15]；主流具身基准**零覆盖** |
| 争议与失败案例 | ❌ 不足 | 无 `[Debated]` 可引来源；失败检测仅作方法出现，无失败率数据 [10][12] |
| 产业/资本/政策 | ❌ 不足 | 产业一手来源 0 条；资本 0 条；政策仅间接 [15] |
| 来源主题相关率 | ⚠️ | **12/33 条与主题无关** [1][14][23][24][26][27][28][29][30][31][32][33] |

---

## 参考来源

[1] UIC-AIHealth4All at ArchEHR-QA 2026: Answer-First Evidence Grounding for Clinical Question Answering — http://arxiv.org/abs/2608.27467v1
[2] Learning to Fold: prizewinning solution at LeHome Challenge 2026 (1st place online, 2nd offline) — http://arxiv.org/abs/2606.27163v3
[3] Inference-Time Attention Steering for Vision-Language-Action Driving Models — http://arxiv.org/abs/2608.17095v1
[4] Large VLM-based Vision-Language-Action Models for Robotic Manipulation: A Survey — http://arxiv.org/abs/2508.13073v3
[5] From Human Videos to Robot Manipulation: A Survey on Scalable Vision-Language-Action Learning with Human-Centric Data — http://arxiv.org/abs/2606.00054v1
[6] Grasp and Motion Planning for Dexterous Manipulation for the Real Robot Challenge — http://arxiv.org/abs/2101.02842v1
[7] Survey of Vision-Language-Action Models for Embodied Manipulation — http://arxiv.org/abs/2508.15201v2
[8] Compositional Context Fine-Tuning Vision-Language Model for Complex Assembly Action Understanding from Videos — http://arxiv.org/abs/2607.10797v1
[9] Evolve Vision-Language-Action Model into an Agent with On-the-fly Tool-use — http://arxiv.org/abs/2608.14047v3
[10] Your Vision-Language-Action Model Already Has Attention Heads For Path Deviation Detection — http://arxiv.org/abs/2603.13782v1
[11] Vision-Language-Action and Vision Language Models for Robot Manipulation: A Comprehensive Review Towards Real-World Applications — https://doi.org/10.20944/preprints202606.0400.v1
[12] Time-aware failure detection for vision-language-action models in robot manipulation — https://doi.org/10.32657/10356/218808
[13] Octo: An Open-Source Generalist Robot Policy — http://arxiv.org/abs/2405.12213v2
[14] Proceedings of the Dialogue Robot Competition 2023 — http://arxiv.org/abs/2312.14430v5
[15] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1
[16] Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success — http://arxiv.org/abs/2502.19645v2
[17] RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control — http://arxiv.org/abs/2307.15818v1
[18] OpenVLA: An Open-Source Vision-Language-Action Model — http://arxiv.org/abs/2406.09246v3
[19] CLIP-RT: Learning Language-Conditioned Robotic Policies from Natural Language Supervision — http://arxiv.org/abs/2411.00508v4
[20] Robot Foundation Models: A Complete Technical Survey - Medium — https://medium.com/@adnanmasood/robot-foundation-models-a-complete-technical-survey-5bf9add22d1c
[21] RT-2: Vision-Language-Action Models for Generalizable Robotic Control: A Comprehensive Review — https://doi.org/10.56028/aetr.15.1.1423.2025
[22] RT-K: A key point-aware transformer framework for efficient vision-language robot control — https://doi.org/10.1016/j.birob.2026.100341
[23] Video 1. RT-DC in action. — https://doi.org/10.7554/elife.29213.011
[24] AutoRestTest at the SBFT 2026 Tool Competition — http://arxiv.org/abs/2607.01063v1
[25] Second MOASEI Competition at AAMAS'2026: A Technical Report — http://arxiv.org/abs/2607.03399v1
[26] NTIRE 2026 Rip Current Detection and Segmentation (RipDetSeg) Challenge Report — http://arxiv.org/abs/2604.17070v2
[27] ZeroR@CHiPSAL 2026: Two-Stage Vision-Language Adaptation with Contrastive Learning for Nepali Meme Classification — http://arxiv.org/abs/2607.28637v1
[28] Overview of BioASQ 2026: The fourteenth BioASQ Challenge on Large-Scale Biomedical Semantic Indexing and Question Answering — http://arxiv.org/abs/2609.39975v1
[29] VoxENES 2026: Benchmarking Generalization of Speech Spoofing Detectors Against LLM-Era TTS and Voice Conversion — http://arxiv.org/abs/2607.11706v1
[30] Writerslogic at PAN 2026: Process over Content for Robust Detection under Domain Shift — http://arxiv.org/abs/2610.03565v1
[31] 铁路客站安检流程瓶颈识别与智能分流组织优化研究 — https://doi.org/10.67328/xf0027
[32] 传统机械加工瓶颈问题及数字化优化策略研究 — https://doi.org/10.70693/hj0715
[33] 传统机械加工瓶颈问题及数字化优化策略研究 — https://doi.org/10.67328/bt1209

---

*Generated by research-bot · topic=`具身智能与视觉-语言-动作vla前沿` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`deepseek-v4-flash` · sources=33 · duration=225s · 2026-10-11T22:06:32+00:00*
