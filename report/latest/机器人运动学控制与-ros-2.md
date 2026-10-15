# 机器人运动学、控制与 ROS 2 生态：7-Facet 增量追踪报告（2024–2026）

**报告日期**：2026-10-15（UTC） ｜ **领域**：机器人运动学、运动/力控制、学习型策略工程化、ROS 2 软件栈 ｜ **可引用来源**：33 条（其中与本主题直接相关者约 12 条，其余为检索噪声） ｜ **证据基座**：仅使用本次给定候选证据集，未新增实时联网检索 ｜ **报告性质**：带日期的增量快照，而非领域教材

> **证据基座警示（请先读）**
> 1. 与「ROS 2 / 运动学 / 控制」**直接相关**的候选证据仅 [22] 一条；其余相关项集中在 VLA 策略与全身控制（[1][5][6][7][8][9][10][11][12][27][29][30][31]）。
> 2. 大量候选来源属**检索噪声**，与主题无关：[2][13][14][15][16][17][18][19][24][25][26][28][32][33]（涵盖短视频热度预测、图像超分、尼泊尔语迷因分类、LHC 机器学习综述、疾病传播 SIS 模型等）。
> 3. **命名陷阱**：候选来源 [20] *“PINOCCHIO and the hierarchical build-up of dark matter haloes”* 是**天体物理学**论文（arXiv astro-ph/0109324），与刚体动力学库 **Pinocchio** 仅为同名巧合，二者不可互相引用。[21] *“The Relativistic Elasticity of Rigid Bodies”* 属物理学，非机器人学。
> 4. 因此本报告在多个 facet 上只能给出「**证据缺口**」结论。**缺口 ≠ 领域无进展**，仅表示本次证据集无法支撑可核查陈述。所有经典奠基文献（阻抗控制、OSC、刚体动力学算法）均不在可引用编号内，本报告**不编造引用**，统一标 `> 待核实`。

---

## 1. 进展与热点（Progress & Hotspots）

**一句话增量判断**：相对 2024 年前的基线，本窗口最清晰的增量不是「又出现一个更强策略」，而是**评测范式从「跑通 demo / 刷单基准分数」转向「诊断性基准 + 鲁棒性度量 + sim-and-real 一致性」**；控制层的增量集中在**全身控制 + 强化学习/扩散策略 + 遥操作**三支。

| # | 条目 | 时间 | 类型 | 四类证据 |
|---|---|---|---|---|
| 1.1 | **诊断性基准成为一等公民**：RoboDojo 提出 sim-and-real 统一评测 [8]；LIBERO-Para 针对 VLA 的**指令释义鲁棒性**给出诊断基准与度量 [27]；LIBERO-VPro 针对机器人基础模型的**闭环视觉鲁棒性** [30]；[1] 从基准视角指出「机器人本质是真机问题，但通用策略的真机评测长期落后」[1] | 2025-08 ~ 2026-09（由 arXiv 编号 2508/2603/2607/2609 推断） | preprint（标题级/摘要级） | 热度：`> 待核实`（候选块未提供引用数）｜权威：均为 arXiv 预印本（B 级），[1][8] 属 cs.RO，[27] 属 cs.LG ｜关注度：**中**（依据：四条独立工作同指"鲁棒性/一致性评测"这一细分问题，属方向性信号，非单一团队行为）｜推荐度：★★★★☆（评测口径是本领域当前最缺的公共品） |
| 1.2 | **策略的推理期可干预性 / 可解释性**：[7] 用 VLA 已有的 attention heads 做路径偏差检测（无需额外训练）；[3] 提出有界加性 pre-softmax 注意力偏置，在**不重训**的前提下把注意力导向安全关键目标 | 2026-03 [7] / 2026-08 [3] | preprint（摘要级） | 热度：`> 待核实`｜权威：arXiv 预印本，[3][7] 均属 cs.CV，且 [3] 面向 **VLA 驾驶模型**而非机械臂 ｜关注度：**中**（依据：两条独立工作共享"推理期干预"的技术动机）｜推荐度：★★★☆☆（机理可迁移到机械臂安全层，但需本体迁移验证，当前无证据）**跨域迁移性 `> 待核实`** |
| 1.3 | **多任务长程操作被竞赛级评测推动**：[5] 为 2025 BEHAVIOR Challenge 第一名方案，基于 **Pi0.5** 架构，基准含 **50 个**长程家务任务、需双臂操作 + 导航 + 上下文决策，**在仿真中** | 2025-12 | 竞赛技术报告 / preprint | 热度：`> 待核实`｜权威：arXiv 预印本（B 级，cs.RO），属**竞赛自评方案**而非第三方复现论文 ｜关注度：**中**（依据：挑战赛为公开基准，方案公开）｜推荐度：★★★★☆（提供了大规模多任务口径下的 VLA 任务适配样板，但**无真机证据**） |
| 1.4 | **全身控制 / 人形三支路线**：[10] 系统研究**域随机化**对扩散策略训练全身人形控制的作用；[11] 用**退火 RL 课程**实现人形全身羽毛球；[12] 提出 CHILD——人形**全身遥操作**系统 | 2024-11 [10] / 2025-11 [11] / 2025-08 [12] | preprint（标题级） | 热度：`> 待核实`｜权威：均为 arXiv 预印本（B 级），[10] 见 2411.01349 ｜关注度：**中高**（依据：全身控制 + 人形是当前社区集中投入方向，三条线索分别覆盖训练机制、任务能力、遥操作数据采集）｜推荐度：★★★★☆（[10] 的"域随机化归因"问题最值得精读） |
| 1.5 | **摆脱动作标签的数据路线**：Generalist Robot Manipulation beyond Action Labeled Data [6] | 2025-09 | preprint（标题级） | 热度：`> 待核实`｜权威：arXiv 预印本（B 级）｜关注度：**中**｜推荐度：★★★☆☆（与"数据瓶颈"直接对应） |
| 1.6 | **控制与学习的交汇**：用控制框架弥合模仿学习 MPC 的 sim-to-real gap [31] | 2025-03 | preprint（标题级） | 热度：`> 待核实`｜权威：arXiv 预印本（B 级）｜关注度：**中**｜推荐度：★★★★☆（本证据集中最贴近"经典控制 × 学习"这条主线的条目） |

**SOTA 变动**：`> 待核实`。本次候选证据**未提供任何榜单数值、任务成功率或口径说明**，因此无法给出可核查的 SOTA 变动陈述。所有「提升多少」类结论本报告一律不写。

**是否被独立验证**：本证据集中，[5] 为**竞赛公开榜单**级证据（强于纯 demo，弱于第三方复现）；[1][6][7][8][9][10][11][12][22][27][30][31] 均为**预印本级别**，未见独立复现报告或第三方基准复测。**「多个任务/多个本体上被独立验证」在本证据集中不成立** → `> 待核实`。

---

## 2. 工业界与产品（Industry & Product）

**一句话增量判断**：本周期在**本次证据集内无显著可核查增量**。ROS 2 侧唯一一手证据是一条医疗场景预印本；机器人中间件与动力学库的官方发布、架构变更、真机部署案例**全部缺失**。

**唯一相关一手证据：**

- **[22] Surgical Vision ROS2: a ROS2 Humble pipeline for intraoperative wound assessment and variable-autonomy arm control**（2026，Research Square 预印本，DOI 10.21203/rs.3.rs-10362132/v1）
  - 内容：vision node 用改编自皮肤科的 **ABCDE** 五部分框架给伤口评分；behaviour manager 把分数映射到**三档自主性**——full execution（直接执行）／reduced-speed execution with per-motion confirmation（降速并对每个动作逐次确认）／hold state（保持/停机）；由 **MoveIt 2** 控制的机械臂执行。
  - **热度证据**：citations=0（候选块给出）[22]。
  - **权威证据**：[22] 为 Research Square 预印本，**未标注同行评审 venue**，属 B/C 之间偏弱等级。
  - **关注度**：**低**——零引用，无第三方复现、无榜单、无社区讨论信号 [22]。
  - **推荐度**：★★★☆☆ —— 主题相关度最高的 ROS 2 落地线索，且给出了「感知打分 → 自主等级 → 运动执行」的分层安全设计；但证据强度仅到预印本摘要级，**只能作线索**。
- **证据缺口（高置信）**：本次候选证据中**不含** `ros2_control`、`Pinocchio`、`Drake`、`MuJoCo`、`MoveIt 2` 的任何官方发布记录、架构变更说明或真机部署案例；也不含阻抗控制、操作空间控制（OSC）、轨迹优化、刚体动力学库相关论文 [2][16][18][22]。**无法判断哪些组件已进入产品化阶段** → `> 待核实`。
- **命名陷阱提示**：若以关键词 "pinocchio" 检索，注意 [20] 是天体物理学的暗物质晕层级构建论文，**不是**刚体动力学库 Pinocchio [20]。

### 表 2-1 开源项目

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| MoveIt 2 | 2026（仅依据 [22]） | `> 待核实` | `> 待核实`（无 stars/采用度数据） | `> 待核实`（未取得官方文档/维护方来源） | 低（仅在 [22] 摘要中被点名） | ★★☆☆☆（仅能证明被用于一个医疗预印本，项目本身发布记录缺失） | `> 待核实` | [22] 明确写到 "MoveIt2-controlled arm" [22] |
| ros2_control | — | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | 本次候选证据**零覆盖** |
| Pinocchio（刚体动力学库） | — | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | 本次候选证据**零覆盖**；[20] 为同名天体物理论文，勿混淆 [20] |
| Drake | — | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | 本次候选证据**零覆盖** |
| MuJoCo | — | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | 本次候选证据**零覆盖** |

> 表 2-1 中除 MoveIt 2 行外，全部单元格为 `待核实`：这本身就是本报告最重要的缺口结论之一——**本证据集不足以回答"ROS 2 工程栈近一年发生了什么"**。

---

## 3. 蓝海与缺口（Blue Ocean & Gaps）

**一句话增量判断**：本窗口暴露出三类明确缺口——**真机评测基础设施**、**分布外鲁棒性（指令 + 视觉）**、**ROS 2 与学习型策略的工程整合**；运动学/控制理论层与学习策略的接口则在本证据集中**完全空白**。

| # | 缺口 | 依据 | 证据等级 | 四类证据 |
|---|---|---|---|---|
| 3.1 | **真机评测基础设施缺位**：策略多在仿真中比较，真机评测口径不统一；sim-and-real 统一基准刚起步 | [1][8] | preprint [1][8] | 热度 `> 待核实`；权威 arXiv 预印本（B 级）；关注度 **中高**（[1] 直接以"benchmarking perspective"立论）；推荐度 ★★★★☆ |
| 3.2 | **指令表述鲁棒性**：VLA 在下游仅用有限数据微调，**过拟合到特定指令措辞**，释义（paraphrase）下的行为一致性缺乏度量 | [27] | preprint（摘要级） | 热度 `> 待核实`；权威 arXiv（B 级）；关注度 **中**（首篇把"释义鲁棒性"单列为诊断靶点）；推荐度 ★★★★☆ |
| 3.3 | **闭环视觉鲁棒性**：视觉扰动下的闭环失效模式缺少系统评测 | [30] | preprint（标题级） | 热度 `> 待核实`；权威 arXiv（B 级）；关注度 **中**；推荐度 ★★★☆☆ |
| 3.4 | **ROS 2 × 学习型策略的部署中间层**：唯一线索 [22] 只做了"评分 → 自主等级 → MoveIt 2 执行"的**浅层分层**，未见共享的部署参考栈、安全监控器或仿真—真机一致性工具链 | [22] | 预印本，citations=0 | 热度 **低**（零引用）；权威 Research Square 预印本（非同行评审）；关注度 **低**；推荐度 ★★★☆☆ |
| 3.5 | **经典控制层与学习策略的接口**：阻抗控制、OSC、轨迹优化在本证据集中**零出现**；唯一擦边条目 [31] 处理的是 MPC 模仿学习的 sim-to-real | [31] 及缺口判断 | preprint [31] | 热度 `> 待核实`；权威 arXiv（B 级）；关注度 `> 待核实`；推荐度 ★★★☆☆ |
| 3.6 | **工具链的术语污染**：库名与学术词（Pinocchio）同名，导致检索召回被天体物理文献污染 | [20][21] | 直接可验证的候选事实 | 热度 不适用；权威 不适用；关注度 **低**；推荐度 ★☆☆☆☆（记录用） |

> **必须明确**：以上 3.1–3.6 是**本次检索的缺口**，不等于"领域无人做"。相反，3.1–3.3 已被多个独立团队同时盯上，说明它们是"已被识别但尚未解决"的缺口，而非蓝海；真正的蓝海更可能在 3.4 与 3.5（**把 ROS 2 实时约束与学习型策略接口形式化**），但该判断属推测 `[P]`，置信度低。

---

## 4. 瓶颈与拐点（Bottleneck & Inflection）

**一句话增量判断**：本窗口的瓶颈集中在**评测口径、分布外鲁棒性、数据标注依赖、人形全身控制训练稳定性**四处；拐点信号是「评测从演示/自评转向诊断基准」与「从重训转向推理期干预」。

| # | 瓶颈 | 依据 | 强度 | 四类证据 |
|---|---|---|---|---|
| 4.1 | **仿真—真机 gap 与评测口径不统一** | [1][8][31] | 确定（三条独立线索） | 热度 `> 待核实`；权威 arXiv 预印本（B 级）；关注度 **中高**；推荐度 ★★★★☆ |
| 4.2 | **指令分布外泛化**：有限数据微调导致措辞过拟合 | [27] | 较大概率 | 热度 `> 待核实`；权威 arXiv（B 级）；关注度 **中**；推荐度 ★★★★☆ |
| 4.3 | **视觉闭环鲁棒性**：开环/短时评估掩盖闭环失效 | [30] | 较大概率 | 热度 `> 待核实`；权威 arXiv（B 级）；关注度 **中**；推荐度 ★★★☆☆ |
| 4.4 | **数据瓶颈：动作标签依赖** | [6][29] | 较大概率（两条线索互为对偶：[6] 试图绕过动作标签，[29] 代表大规模真实数据路线） | 热度 `> 待核实`；权威 [29] 为 arXiv 预印本（B 级）；关注度 **中高**（DROID 属公认公开数据资产）；推荐度 ★★★★☆ |
| 4.5 | **人形全身控制的训练稳定性与课程设计** | [10][11][12] | 推测 | 热度 `> 待核实`；权威 arXiv（B 级）；关注度 **中高**；推荐度 ★★★★☆ |

**拐点信号（`[P]` 预测，见 §7）**：

- **信号 A**：评测类工作在同一时间窗内成簇出现（[1][8][27][30] 的 arXiv 编号横跨 2025-08 至 2026-09），说明"评测"已从论文的附属实验升级为独立研究对象 `[P]`。
- **信号 B**：推理期干预范式出现（[3][7]），指向"安全/可控性不必以重训为代价" `[P]`。注意 [3] 属驾驶域，机械臂域证据缺失。
- **信号 C**：`> 待核实`——是否存在产业侧的拐点（如某中间件被广泛用于量产），本次证据集**无法判断**。

---

## 5. 社会·政策·国际（Society, Policy & Geopolitics）

**一句话增量判断**：本周期在本次证据集内**无显著可核查增量**——没有任何监管、标准、地缘政治或供应链来源被召回。

- **监管与标准**：本次候选来源中**不含**任何法规、标准（如功能安全标准、医疗器械法规）或政策文本 `> 待核实`。本报告**不以记忆补写**相关条款，以避免不可核查引用。
- **伦理与劳动影响**：无来源 `> 待核实`。
- **国际与供应链**：无来源 `> 待核实`。
- **唯一可外推的弱线索（`[P]`，置信度低）**：[22] 在**术中（intraoperative）**场景下采用三档自主性（全执行 / 降速逐动作确认 / 保持）[22]，其设计动因高度符合医疗器械领域对"自主等级与操作者可覆写"的合规取向；若该取向成立，则"**可变自主性（variable autonomy）会成为医疗机器人 ROS 2 栈的默认架构模式**"是可检验的假设。依据链：术中场景 × 高风险 × 分级自主 → 合规约束 → 架构模式。**该推断未经任何法规来源核实** `[P]` `> 待核实`。

> 本 facet 的空缺应被解读为**检索覆盖失败**（候选集中出现大量与主题无关的竞赛/评测类论文，说明检索式对"政策/生态"维度未作定向召回），而非"该维度无变化"。

---

## 6. 资本与生态（Capital & Ecosystem）

**一句话增量判断**：本周期在本次证据集内**无显著可核查增量**；仅能识别出两项可观测的**公共生态资产**与一项弱信号。

| # | 条目 | 依据 | 四类证据 |
|---|---|---|---|
| 6.1 | **公共数据资产**：DROID —— 大规模野外（in-the-wild）机器人操作数据集，作为基础设施型资产被公开 | [29]（arXiv 2403.12945v2, 2024） | 热度 `> 待核实`（未采集引用数/下载量）；权威 arXiv 预印本（B 级）；关注度 **中高**（依据：作为"in-the-wild"路线代表被独立引用）；推荐度 ★★★★☆（本证据集中最像"生态资产"的条目） |
| 6.2 | **公共基准资产**：LIBERO 系（经 LIBERO-Para [27] / LIBERO-VPro [30] 间接出现）与 BEHAVIOR Challenge [5] 形成"基础基准 + 诊断扩展"的生态位 | [5][27][30] | 热度 `> 待核实`；权威 arXiv 预印本（B 级）；关注度 **中**；推荐度 ★★★★☆ |
| 6.3 | **学术产出增速的弱信号**：VLA 综述 *Large VLM-based Vision-Language-Action Models for Robotic Manipulation: A Survey* 已迭代到 **v3** | [9]（arXiv 2508.13073v3） | 热度 `> 待核实`；权威 arXiv 预印本（B 级，survey）；关注度 **中**（依据：版本迭代至 v3 表明作者持续更新，间接提示领域文献增速快——**该归因为推测**）；推荐度：★★★★☆（入门骨架可用） |
| 6.4 | **融资、并购、人才流动、公司格局** | 无来源 | `> 待核实` —— 本次候选证据**零覆盖**，本报告不编造任何金额、轮次或机构名 |

**生态结构观察（`[P]`，置信度低）**：投入正在从"造策略"向"造评测与诊断"迁移（§4 信号 A）；若该迁移成立，则公共基准与诊断工具将成为下一轮生态竞争的入口 `[P]`。

---

## 7. 信号与预测（Signals & Forecast）

以下预测均写成**可证伪假设**，并标注依据链与置信度。全部为 `[P]`（prediction），非既成事实。

| 编号 | 可证伪假设 | 依据链 | 置信度 | 证伪条件 |
|---|---|---|---|---|
| `[P1]` | **评测范式迁移**：到 **2027 年年中**，机器人操作/ VLA 主流论文的默认评测将从"单基准成功率"转为"多基准 + sim-and-real 一致性 + 鲁棒性维度（指令/视觉）" | 评测类工作已成簇出现：[1][8][27][30]，编号横跨 2025-08 至 2026-09 | **中** | 若到 2027-06，顶会主流操作论文仍以单一仿真成功率作为唯一评测指标，则假设失败 |
| `[P2]` | **ROS 2 × 学习策略整合栈出现**：到 **2027 年底**，出现 ≥3 个基于 `ros2_control`/MoveIt 2 的公开开源"学习型策略部署参考栈"（含安全监控与自主性分级） | 唯一孤证 [22] 展示了该模式的雏形（感知评分 → 三档自主性 → MoveIt 2 执行），但当前 citations=0、无同类工作 | **低** | 若到 2027-12 仍无 ≥3 个公开仓库，则假设失败 |
| `[P3]` | **推理期可控性成为安全层手段**：12–18 个月内出现 ≥2 个**在真机上验证**的、基于注意力/激活干预（不重训）的机器人安全干预方法 | [3][7] 已分别验证"注意力可被推理期引导"与"注意力头可用于偏差检测"，但 [3] 为驾驶域、[7] 未见真机证据 | **低-中** | 若 18 个月内相关方法仍全部停留在仿真/离线分析，则假设失败 |
| `[P4]` | **人形全身控制走向可复现**：12 个月内出现对 [10][11][12] 路线的**第三方独立复现 + 真机长时稳定运行**报告 | 三条线索分别覆盖训练机制 [10]、任务能力 [11]、遥操作数据 [12]；但当前全部为预印本级别 | **低** | 若无第三方复现且无真机长时运行记录，则假设失败 |
| `[P5]` | **可变自主性进入医疗机器人 ROS 2 栈**：术中/临床场景的多档自主性设计成为该类系统的默认架构模式 | 依据 [22] 的三档设计，但其为单一预印本（citations=0） | **低** | 若后续该类系统普遍采用全自主或全手动二值模式，则假设失败 |

### Watchlist（值得持续关注）

1. **诊断性基准簇**：[27] LIBERO-Para、[30] LIBERO-VPro、[8] RoboDojo —— 关注是否被第三方采纳为默认评测。
2. **sim-and-real 一致性方法**：[1][8][31] —— 关注是否有量化的真机—仿真相关性指标被提出并被复现。
3. **人形全身控制**：[10][11][12] —— 关注域随机化的**归因分析**是否被独立验证（提升来自随机化、架构还是算力？）。
4. **数据路线之争**：[6]（绕过动作标签） vs [29]（大规模真实数据）—— 2026–2027 谁在真机上更占优。
5. **ROS 2 工程侧**：`ros2_control` / MoveIt 2 / Pinocchio / Drake / MuJoCo 的官方发布记录 —— **本次完全缺失，需优先补充定向检索**；检索时须规避 [20] 的同名污染。

### 方法论自检与后续检索建议

- 本次检索在 **facet 5（社会·政策）与 facet 6（资本·生态）** 上召回为零，在 **facet 2（ROS 2 工程栈）** 上召回高度不足；建议下一轮针对性检索式：`MoveIt 2 release notes 2025..2026`、`ros2_control architecture changes`、`pinocchio rigid body dynamics library`（须排除天体物理）、`Drake toolbox release`、`MuJoCo release notes`、以及 `人形机器人 量产 2025 2026 融资`、`robot safety standard functional safety 2026`。
- 本次所有相关条目**均无引用数/star 数据**，四轴中的"热度证据"普遍为 `> 待核实`。**结论强度因此受限**：本报告应被视为"证据地图与缺口清单"，而非"结论性综述"。

---

## 参考来源

**本报告实际引用：**

[1] Robot Policy Evaluation for Sim-to-Real Transfer: A Benchmarking Perspective — http://arxiv.org/abs/2508.11117v1
[2] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1
[3] Inference-Time Attention Steering for Vision-Language-Action Driving Models — http://arxiv.org/abs/2608.17095v1
[4] Grasp and Motion Planning for Dexterous Manipulation for the Real Robot Challenge — http://arxiv.org/abs/2101.02842v1
[5] Task adaptation of Vision-Language-Action model: 1st Place Solution for the 2025 BEHAVIOR Challenge — http://arxiv.org/abs/2512.06951v2
[6] Generalist Robot Manipulation beyond Action Labeled Data — http://arxiv.org/abs/2509.19958v1
[7] Your Vision-Language-Action Model Already Has Attention Heads For Path Deviation Detection — http://arxiv.org/abs/2603.13782v1
[8] RoboDojo: A Unified Sim-and-Real Benchmark for Comprehensive Evaluation of Generalist Robot Manipulation Policies — http://arxiv.org/abs/2607.04434v3
[9] Large VLM-based Vision-Language-Action Models for Robotic Manipulation: A Survey — http://arxiv.org/abs/2508.13073v3
[10] The Role of Domain Randomization in Training Diffusion Policies for Whole-Body Humanoid Control — http://arxiv.org/abs/2411.01349v1
[11] Humanoid Whole-Body Badminton via an Annealed Reinforcement Learning Curriculum — http://arxiv.org/abs/2511.11218v4
[12] CHILD (Controller for Humanoid Imitation and Live Demonstration): a Whole-Body Humanoid Teleoperation System — http://arxiv.org/abs/2508.00162v2
[16] Second MOASEI Competition at AAMAS'2026: A Technical Report — http://arxiv.org/abs/2607.03399v1
[18] Machine learning for the LHC physics program: a 2025-2026 stocktake — http://arxiv.org/abs/2609.32874v1
[20] PINOCCHIO and the hierarchical build-up of dark matter haloes — http://arxiv.org/abs/astro-ph/0109324v1
[21] The Relativistic Elasticity of Rigid Bodies — http://arxiv.org/abs/physics/0307019v3
[22] Surgical Vision ROS2: a ROS2 Humble pipeline for intraoperative wound assessment and variable-autonomy arm control — https://doi.org/10.21203/rs.3.rs-10362132/v1
[27] LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models — http://arxiv.org/abs/2603.28301v3
[29] DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset — http://arxiv.org/abs/2403.12945v2
[30] LIBERO-VPro: Benchmarking Closed-Loop Visual Robustness of Robotic Foundation Models — http://arxiv.org/abs/2609.24350v1
[31] Bridging the Sim-to-real Gap: A Control Framework for Imitation Learning of Model Predictive Control — http://arxiv.org/abs/2503.19228v4

**可引用但本报告未采用（与主题无关 / 检索噪声，仅登记以确保编号完整）：**

[13] NTIRE 2025 Challenge on Image Super-Resolution (x4): Methods and Results — http://arxiv.org/abs/2504.14582v3
[14] UIC-AIHealth4All at ArchEHR-QA 2026: Answer-First Evidence Grounding for Clinical Question Answering — http://arxiv.org/abs/2608.27467v1
[15] ZeroR@CHiPSAL 2026: Two-Stage Vision-Language Adaptation with Contrastive Learning for Nepali Meme Classification — http://arxiv.org/abs/2607.28637v1
[17] AutoRestTest at the SBFT 2026 Tool Competition — http://arxiv.org/abs/2607.01063v1
[19] ICDAR 2025 Competition on End-to-End Document Image Machine Translation Towards Complex Layouts — http://arxiv.org/abs/2603.09392v1
[23] Engineering Documentation Release — https://doi.org/10.1201/9781482273427-13
[24] VLSP 2025 MLQA-TSR Challenge: Vietnamese Multimodal Legal Question Answering on Traffic Sign Regulation — http://arxiv.org/abs/2510.20381v1
[25] Event-Enriched Image Analysis Grand Challenge at ACM Multimedia 2025 — http://arxiv.org/abs/2508.18904v1
[26] Open-LLM-Leaderboard: From Multi-choice to Open-style Questions for LLMs Evaluation, Benchmark, and Arena — http://arxiv.org/abs/2406.07545v1
[28] The ML.ENERGY Benchmark: Toward Automated Inference Energy Measurement and Optimization — http://arxiv.org/abs/2505.06371v2
[32] A Human-Vector Susceptible-Infected-Susceptible Model for Analyzing and Controlling the Spread of Vector-Borne Diseases — http://arxiv.org/abs/2510.14787v2
[33] Moving Peaks Benchmark Survey: An Open, Interactive Leaderboard — https://doi.org/10.2139/ssrn.7541489

**在本次可引用来源中缺失、因而无法给出引用的经典/奠基主题（需下一轮定向检索，本报告不编造引用）：** 阻抗控制（impedance control）、操作空间控制（operational space control）、刚体动力学算法（rigid-body dynamics algorithms）、轨迹优化（trajectory optimization）、MoveIt 2 / `ros2_control` / Pinocchio（库） / Drake / MuJoCo 的官方发布与架构变更、Open X-Embodiment / SimplerEnv / RoboArena 的官方主页与榜单。以上条目均标 `> 待核实`。

---

*Generated by research-bot · topic=`机器人运动学控制与-ros-2` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`deepseek-v4-flash` · sources=33 · duration=179s · 2026-10-15T22:23:17+00:00*
