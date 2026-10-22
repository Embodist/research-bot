# 具身智能与视觉-语言-动作（VLA）前沿：2024–2026 增量证据快照

**日期**：2026-10-22（UTC）｜**领域**：Embodied AI / Vision-Language-Action（VLA）/ 机器人学习工程栈｜**检索源数量**：候选来源 34 条，其中与本主题直接相关且可核查者 13 条（[1][2][3][5][7][12][13][14][19][21][24][31][34]），主题漂移或无关者 21 条（[4][6][8][9][10][11][15][16][17][18][20][22][23][25][26][27][28][29][30][32][33]）

> **阅读须知（证据边界）**：本报告严格基于给定候选块中的摘要级信息与标题级信息撰写。凡候选块未提供摘要细节、引用数、star 数或榜单排名的条目，一律写 `> 待核实`，**不做任何数字补全**。本批次证据在若干经典方向（RT-1/RT-2、Diffusion Policy、ACT、Open X-Embodiment、DROID、CALVIN、SimplerEnv、RoboArena、政策与资本）存在**系统性覆盖缺口**，相关章节以“证据缺口 + 可观测指标建议”形式呈现，而非以记忆填充。

---

## 1. 进展与热点（Progress & Hotspots）

**一句话增量判断**：2025–2026 年的增量不在“又一个大一统 VLA”，而在三条侧翼路线的实证化——**推理栈轻量化与部署可行性**、**推理期可控性/可解释性**、**跨本体与少样本迁移的显式建模**；而奠基模型之间的架构对比在本批证据中仍属空白。

### 1.1 最新进展（近 1–2 年）

| 方向 | 代表条目 | 时间 | 增量（相对上一基线） | 证据等级 |
|---|---|---|---|---|
| VLA 推理栈轻量化 | BLURR [3] | 2025-12 | 把“推理栈过重”列为一等问题，提出可插入现有控制器、**免重训、免改 checkpoint** 的轻量封装，以 pi-zero（π0）为实例 [3] | B（arXiv 预印本，未见 venue） |
| 推理期可控性 | Inference-Time Attention Steering [1] | 2026-08 | 在 VLA 驾驶模型上以**有界加性 pre-softmax 注意力偏置**重导向安全关键交通参与者，不改权重，给出剂量响应与层消融定位 [1] | B（arXiv 预印本） |
| 跨本体 / 少样本迁移 | CM-VLA [31]、GET-Zero [34]、Embodiment Scaling Laws [24] | 2025-05 ~ 2026 | 分别从相机空间 MoE、图结构 embodiment transformer、embodiment 数量缩放三个角度处理跨本体泛化 [24][31][34] | [34] A（ICRA 2025）；[24][31] B |
| VLA 智能体化 | On-the-fly Tool-use [5] | 2026-08 | 把 VLA 扩展为可**即时调用工具**的 agent，属能力边界外扩而非策略精度提升 [5] | B（仅标题级信息，`> 待核实`） |
| 语义前端细化 | CCFT + LP-AT [2] | 2026-07 | 把装配动作分解为 Verb/Object/Tool 语义元素，用层分区交替训练做多任务微调；**属动作理解，非动作生成** [2] | B（无闭环执行证据） |
| 长程任务适配 | BEHAVIOR Challenge 2025 冠军方案 [7] | 2025-12 | 面向长程家务类基准的任务适配解法，说明该赛道已形成竞赛化评测 [7] | B（竞赛方案，`> 待核实` 榜单口径） |

**关键区分：演示 vs 验证**
- [1] 的评测**完全建立在合成数据**（Physical AI World Model Synthetic dataset，50 个换道场景）之上，指标是轨迹位移（平均约 17 cm、clamp 处横向可达约 140 cm），**不是**成功率、接管率或碰撞率 [1]。这属于“演示级验证”，不能等同于真车 SOTA。
- [2] 摘要未报告机器人闭环执行、成功率或跨本体泛化结果 [2]，属感知层证据。
- [3] 未给出加速比、延迟、吞吐与硬件型号 [3]，因此**无法与其他推理优化方案横向比较**。
- 本批证据中**没有任何一条**提供第三方复现、公开榜单排名或同行评审录用信息（除 [34]）[1][2][3][5][7][31]。

### 1.2 经典与奠基性工作

> **重要说明**：Q1 明确要求对比 RT-1、RT-2、Diffusion Policy、ACT、OpenVLA、π0/π0.5、GR00T N1、Gemini Robotics、RDT。**本批候选块未收录其中多数工作的可核查链接与摘要**，下表据实标注缺口，**不补造论文、数字或 URL**。

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| RT-1 / RT-2 | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实（本批证据集未收录）` | 作为“VLA 范式起点”的公认锚点，但本轮无一手来源，不得引用具体指标 |
| Diffusion Policy | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实（本批证据集未收录）` | 扩散式动作表征的奠基工作；其思想在 [12] 的 latent action diffusion 中可见延续 [12] |
| ACT（Action Chunking Transformer） | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实（本批证据集未收录）` | 动作分块范式的代表；与 LeRobot 生态常并提，但本轮无来源 [14] |
| OpenVLA | 2025（被研究） | `> 待核实` | `> 待核实` | B（作为 arXiv 研究对象出现）[19] | 中：已被用于内部表征分析，暗示权重可获取 [19] | ★★★★☆ 可作为“开放权重 VLA 已进入机理研究阶段”的信号 [19] | http://arxiv.org/abs/2509.24559v1 | [19] 研究 OpenVLA 中的涌现世界表征；**是否等同于 OpenVLA 原始发布文献，`> 待核实`** |
| GR00T N1 | 2025 | NVIDIA（据标题推断，`> 待核实` 作者列表） | `> 待核实` | B（官方技术报告形态的 arXiv 预印本）[13] | 中：标题即定位为“开放基础模型”，指向人形通用机器人 [13] | ★★★★☆ 人形方向少有的开放基础模型一手来源，需精读架构与数据配方 [13] | http://arxiv.org/abs/2503.14734v2 | 面向 generalist humanoid robots 的 open foundation model [13]；动作表征、参数规模、数据配方本批未提供，`> 待核实` |
| π0 / π0.5 | 2025（π0 被复用） | `> 待核实` | `> 待核实` | B（经第三方封装间接证实可获取）[3] | 中：被第三方作为可复用基座封装加速，说明生态扩散 [3] | ★★★★☆ “被第三方复用”是比自评更强的生态信号，但 π0.5 无任何证据 [3] | `> 待核实（π0 原始链接未在证据集内；[3] 仅以其为实现实例）` | [3] 以 pi-zero VLA 控制器为实例实现轻量推理封装 [3] |
| Gemini Robotics / RDT | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实（本批证据集未收录）` | 本批证据**零覆盖**，任何关于其架构或性能的陈述均无依据 |

### 1.3 新增 VLA 与相关前沿条目（含四类证据轴）

**条目 A：BLURR（VLA 推理加速）** — 热度：`> 待核实`（候选块未给引用数/star）[3]；权威：arXiv 预印本 2512.11769v1，未见同行评审 [3]；关注度：**低**（无引用/star/榜单信号，仅摘要可见）[3]；推荐度：**★★★☆☆** 直接命中“VLA 能否高频实时运行”这一工程要害，但缺量化结果，需精读原文核实加速比与硬件口径 [3]。

**条目 B：Inference-Time Attention Steering for VLA Driving Models** — 热度：`> 待核实` [1]；权威：arXiv 2608.17095v1（cs.CV），未见同行评审 [1]；关注度：**低**（2026-08 新预印本，无引用或复现信号）[1]；推荐度：**★★★☆☆** 为 VLA 可解释性与推理期干预提供可核查一手证据，但仅合成 50 场景，属演示级 [1]。

**条目 C：CM-VLA** — 热度：citations = 0 [31]；权威：SSRN 预印本（DOI 10.2139/ssrn.6915199），未见同行评审 [31]；关注度：**低**（citations=0）[31]；推荐度：**★★★☆☆** 少样本跨本体迁移的直接对手方法，可与 [34] 对照阅读 [31][34]。

**条目 D：GET-Zero** — 热度：citations = 2 [34]；权威：**ICRA 2025 同行评审**（DOI 10.1109/icra55743.2025.11127922）[34]；关注度：**低**（citations=2，属早期）[34]；推荐度：**★★★★☆** 本批证据中**唯一 A 级同行评审**的跨本体零样本泛化工作，可信度最高 [34]。

**条目 E：Towards Embodiment Scaling Laws in Robot Locomotion** — 热度：`> 待核实` [24]；权威：arXiv 2505.05753v2（cs.RO），未见同行评审 [24]；关注度：**低**（无引用信号）[24]；推荐度：**★★★★☆** 提出“embodiment 数量缩放律”假设——训练本体数增加可提升对未见本体的泛化，是跨本体问题少见的**可证伪命题** [24]。

**条目 F：CLAD（约束潜动作扩散）** — 热度：`> 待核实` [12]；权威：**RO-MAN 2026 同行评审**（DOI 10.1109/ro-man72286.2026.11714614）[12]；关注度：**低**（新会议论文，无社区信号）[12]；推荐度：**★★★☆☆** 显示扩散式潜动作表征向“过程规划 + 约束”延伸，与端到端 VLA 形成互补 [12]。

---

## 2. 工业界与产品（Industry & Product）

**一句话增量判断**：本批证据中工业界信号集中于**“开放基础模型 + 开源全栈库”两条产品化路径**（NVIDIA GR00T N1 [13]、Hugging Face LeRobot [14]），但**真机部署、量产、商业合同类证据为零**。

### 2.1 开源项目

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| LeRobot | 2026 | Hugging Face 生态团队（Remi Cadene、Thomas Wolf 等 17 人）[14] | `> 待核实`（无 star/下载数据）[14] | B：arXiv 2602.22818v1（cs.RO），作者即项目维护方，属官方方法性文献；未见会议录用 [14] | **中**：无 star 数据，但为项目官方论文，工程社区相关度高 [14] | ★★★★☆ 唯一直接命中“VLA 开源工程栈”的一手文献 [14] | http://arxiv.org/abs/2602.22818v1 | 定位为“整合整个机器人学习栈、从底层中间件到……（摘要截断）”的开源库 [14]；GitHub 仓库地址、许可证、支持本体清单 `> 待核实` |
| GR00T N1 | 2025 | NVIDIA（`> 待核实` 作者列表）[13] | `> 待核实` [13] | B：arXiv 2503.14734v2，官方技术报告形态 [13] | **中**：标题即“open foundation model”，指向人形通用机器人产品线 [13] | ★★★★☆ 人形赛道开放权重的最重要候选，需核实“开放”具体边界（权重/数据/仅代码）[13] | http://arxiv.org/abs/2503.14734v2 | 权重开放范围与许可证 `> 待核实` |
| openpi（Physical Intelligence） | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实（本批证据集未收录）` | 仅有 π0 被第三方复用为基座的间接证据 [3]；**注意**：来源 [18] 的“OpenPI-C”是开放词表状态跟踪基准，与 openpi 代码库**无关**，检索时极易混淆 [18] |
| OpenVLA | `> 待核实` | `> 待核实` | `> 待核实` | B（作为被研究对象）[19] | **中**：已被用于内部世界表征分析，间接说明权重可获取 [19] | ★★★★☆ 开放权重 VLA 进入机理研究阶段的标志 [19] | http://arxiv.org/abs/2509.24559v1 | 原始发布文献与许可证 `> 待核实` |

### 2.2 工程落地的真实门槛（作者侧论断，非第三方验证）

LeRobot 摘要明确将进展归因于三点：**低成本遥操作硬件、大规模公开数据集、可扩展学习方法**；并把主要障碍定位为“碎片化、闭源、只覆盖特定子组件的工具” [14]。这构成“复现门槛 = 硬件成本 + 数据 + 工具链割裂”的**论文宣称**，尚无独立第三方评测支撑 [14]。

**产业证据缺口（本节必须明示）**：
- 人形/机械臂厂商的量产数量、订单、客户案例：`> 待核实`（本批 0 条）
- ROS2 集成路径（ros2_control / MoveIt 与学习策略接口、实时性约束）：`> 待核实`（本批 0 条）
- 微调算力门槛（GPU 型号/时长/显存）：`> 待核实`（本批 0 条）
- Gemini Robotics、RDT 的产品化状态：`> 待核实`（本批 0 条）

---

## 3. 蓝海与缺口（Blue Ocean & Gaps）

**一句话增量判断**：本批证据自身暴露出的空白，恰好与领域公认空白高度重合——**评测独立性、跨本体数据效率、推理时延的量化口径**三处最缺一手材料。

### 3.1 高杠杆缺口（有证据支撑的“没人做/没做好”）

1. **VLA 推理效率缺乏统一度量口径**。 [3] 只提出“推理栈过重”的动机，未报告延迟、吞吐、硬件与加速比，因此业界无法横向比较不同推理优化方案 [3]。→ 机会：建立 **VLA inference benchmark**（统一硬件、统一控制频率、统一 batch/精度设定）。证据：B 级 [3]。
2. **跨本体泛化的“缩放律”尚未被独立验证**。[24] 提出“训练本体数量↑ → 未见本体泛化↑”的假设，但本批无第三方复现 [24]；[31] citations=0 [31]、[34] citations=2 [34] 说明该子方向引用密度极低，属**低竞争区**。
3. **推理期可控性只在合成场景验证**。[1] 的注意力偏置仅在 50 个合成换道场景、以轨迹位移度量 [1]。→ 机会：把“推理期干预”接到**闭环安全指标**（接管率/碰撞率/舒适度）上，这是明确的空白。
4. **VLA × 工具调用的能力边界未定义**。[5] 提出把 VLA 演进为可即时调用工具的 agent [5]，但本批无任何基准或失败案例分析，`> 待核实`。
5. **个性化/长尾操作几乎无基准**。[21] LIBERO-PeRM 直接以“个性化机器人操作”为评测对象（2026-10），说明**个性化**这一维度刚被形式化 [21]。证据：B 级，无引用信号。

### 3.2 数据集与基准

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| LIBERO-PeRM | 2026 | `> 待核实` | `> 待核实` [21] | B：arXiv 2610.22372v1，未见同行评审 [21] | **低**：2026-10 新预印本，无引用信号 [21] | ★★★☆☆ 把“个性化操作”形式化为基准，填补长尾评测空白；与原始 LIBERO 的关系 `> 待核实` [21] | http://arxiv.org/abs/2610.22372v1 | 首个以 personalized manipulation 为对象的 LIBERO 家族基准 [21] |
| BEHAVIOR Challenge 2025 | 2025 | `> 待核实` | `> 待核实` [7] | B：arXiv 2512.06951v2（冠军方案）[7] | **中**：已形成竞赛与冠军方案，说明有组织化评测 [7] | ★★★★☆ 长程家务任务的可比评测入口；榜单口径与独立性 `> 待核实` [7] | http://arxiv.org/abs/2512.06951v2 | 冠军方案为“任务适配”路线 [7] |
| Physical AI World Model Synthetic dataset | 2026 | `> 待核实` | `> 待核实` [1] | C：仅见于单篇预印本的自建合成设定，是否公开未确认 [1] | **低**：无社区使用信号 [1] | ★★☆☆☆ 作为 [1] 实验背景必要，作为通用基准价值 `> 待核实` [1] | http://arxiv.org/abs/2608.17095v1 | 50 个换道场景 [1] |
| EgoDatasets（自视角数据集综述） | 2026 | `> 待核实` | `> 待核实` [9] | B：Preprints 预印本（DOI 10.20944/preprints202608.0778.v1），**非同行评审** [9] | **低**：预印本平台，无引用信号 [9] | ★★☆☆☆ 数据侧综述线索，与 VLA 操作数据仅间接相关 [9] | https://doi.org/10.20944/preprints202608.0778.v1 | 自视角视觉与动作预测的数据集分类学 [9] |
| Open X-Embodiment / DROID / LIBERO / CALVIN / SimplerEnv / RoboArena | — | — | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实（本批证据集完全未覆盖）` | ⚠️ Q2 点名的六大基准在本批证据中**零覆盖**，其任务范围、本体分布、仿真/真机口径差异、榜单独立性均无依据 |

---

## 4. 瓶颈与拐点（Bottleneck & Inflection）

**一句话增量判断**：瓶颈已从“模型能力不足”**部分转向“部署经济学”**——推理栈开销被明确列为一等问题 [3]，而评测口径不统一成为判断拐点的最大障碍 [1][3][7]。

### 4.1 瓶颈清单（按证据强度排序）

| # | 瓶颈 | 一手证据 | 证据等级 | 是否临近拐点 |
|---|---|---|---|---|
| 1 | **推理时延 / 推理栈过重** | 现有 VLA 推理栈对“响应式 web demo”和“消费级 GPU 上高频机器人控制”均过重 [3] | B | 是——已出现免重训、免改 checkpoint 的封装路线 [3]，但缺量化拐点信号（延迟数字 `> 待核实`） |
| 2 | **评测口径缺失（合成 vs 真机、位移 vs 成功率）** | [1] 全部在 50 个合成场景、以轨迹位移度量，无接管率/碰撞率 [1] | B | 否——尚无统一基准出现 |
| 3 | **跨本体数据稀缺** | “跨本体演示本质上是稀缺的”，与视觉/语言数据规模不可比 [31]；本体数量缩放律仍属假设 [24] | B | 待观察——缩放律若被独立复现则构成拐点 [24] |
| 4 | **工具链碎片化与闭源** | LeRobot 立论前提：工具“碎片化、闭源、只覆盖特定子组件” [14] | B（作者自述） | 是——开源全栈整合正在推进 [14]，但覆盖率 `> 待核实` |
| 5 | **长程任务可靠性** | 仅见 BEHAVIOR 长程赛道冠军方案 [7]，无失败率/退化分析 | B | `> 待核实` |
| 6 | **动作理解 vs 动作生成割裂** | 装配场景的 VLM 微调停留在语义元素识别，无闭环执行 [2] | B | 否 |
| 7 | **算力门槛 / 微调成本** | 本批 0 条 | `> 待核实` | `> 待核实` |

### 4.2 拐点信号（可观测）

- **信号 1（已出现）**：第三方不再重训模型，而是**包裹推理层**来提升可用性 [3] —— 这是“模型趋稳、工程补位”的典型拐点特征。
- **信号 2（已出现）**：研究焦点从“策略精度”外溢到“**推理期可控性**”[1] 与“**工具调用**”[5] —— 表明基础策略能力已不再是唯一瓶颈。
- **信号 3（未出现）**：**没有任何一条**证据提供真机闭环安全指标或第三方复现报告 [1][2][3][5][7]。因此“真机可靠性拐点”目前**无法判定**，`> 待核实`。

---

## 5. 社会·政策·国际（Society, Policy & Geopolitics）

**一句话增量判断**：本周期在本批证据中**无显著变化可报告**——监管、标准、地缘与供应链维度为**零覆盖**，本节仅陈述结构性判断与所需的可观测指标，全部标注待核实。

**证据缺口陈述**：
- AI/机器人监管法规（生效时间、适用范围、对具身系统的分类）：`> 待核实`（本批 0 条来源）
- 机器人安全标准（如功能安全等级、人机协作规范）：`> 待核实`（本批 0 条）
- 出口管制、关键零部件（减速器、灵巧手、算力芯片）供应链约束：`> 待核实`（本批 0 条）
- 数据隐私与真机数据采集的合规边界：`> 待核实`（本批 0 条）
- 劳动替代相关的实证研究：`> 待核实`（本批 0 条）

**可间接观察的结构性信号（弱证据，需谨慎）**：
- 开放基础模型由大型芯片厂商发布 [13]、全栈开源库由大型模型社区团队维护 [14]，提示**具身智能的基础设施层正在被“平台型公司”占位**。这是生态结构信号，**不构成政策结论**。
- [9] 显示自视角（egocentric）数据集的系统性梳理已出现 [9]，间接反映**人类第一视角数据**作为数据来源受到关注；其隐私与采集合规影响 `> 待核实`。

**建议补充的检索方向**：官方监管机构公告、标准组织文档、厂商合规声明、海关/出口管制清单更新——本轮均未检索，故不作任何趋势判断。

---

## 6. 资本与生态（Capital & Ecosystem）

**一句话增量判断**：本批证据只有**生态结构信号**（谁在维护开源栈、谁在发布基础模型），**没有任何投融资、并购、估值或人才流动的一手数据**。

### 6.1 可核查的生态信号

| 信号 | 内容 | 证据 | 强度 |
|---|---|---|---|
| 平台型公司占位基础模型 | NVIDIA 发布面向通用人形机器人的 open foundation model（GR00T N1）[13] | B（官方技术报告形态）[13] | 中 |
| 模型社区占位全栈工具链 | Hugging Face 生态团队（Cadene、Wolf 等 17 人）以论文形式定义 LeRobot 的全栈定位 [14] | B（项目官方文献）[14] | 中 |
| 基座模型的“被复用度”成为新竞争维度 | 第三方以 pi-zero 为实例做推理封装，说明 π0 已成为事实上的复用基座 [3] | B（间接证据）[3] | 中弱（仅 1 篇，`> 待核实`） |
| 竞赛化评测形成（生态组织度） | BEHAVIOR Challenge 2025 已产生冠军方案 [7] | B [7] | 中 |
| 学术共同体对跨本体的低引用密度 | CM-VLA citations=0 [31]；GET-Zero citations=2 [34] | B/A [31][34] | 中——说明该子方向**尚未形成资本/注意力聚集** |

### 6.2 资本证据缺口（明确标注）

- 融资轮次与金额、并购交易、估值：`> 待核实`（本批 0 条）
- 人才流动（学术界→产业界的具体案例）：`> 待核实`（本批 0 条）
- GitHub star 增速、HuggingFace 模型下载量：`> 待核实`（本批未提供任何 star/下载数字）[13][14]
- 公司格局与市场份额：`> 待核实`（本批 0 条）

> **纪律提示**：本节不得以“行业普遍认为”“据报道”等模糊表述填充。任何金额、轮次、排名数字在无一手来源时一律不写。

---

## 7. 信号与预测（Signals & Forecast）

**一句话增量判断**：本周期最可靠的早期信号是**“VLA 从模型竞赛转入部署竞赛”**（推理封装 [3]、推理期控制 [1]、工具调用 [5] 三条独立线索同向），而最不可靠的是**任何关于真机可靠性的断言**（零闭环证据）。

### 7.1 早期信号清单

| 信号 | 时间 | 含义 | 标记 |
|---|---|---|---|
| 出现“免重训、免改 checkpoint”的推理封装，并以 π0 为实例 [3] | 2025-12 | 模型侧趋于稳定，工程侧开始补位；基座可复用性成为资产 [3] | 确定（有摘要证据） |
| 推理期注意力干预在不改权重前提下产生单调剂量响应，动作相关信号定位于较晚层 [1] | 2026-08 | 可解释性从“事后分析”走向“运行时控制” [1] | 确定（但仅合成场景） |
| VLA 被扩展为可即时调用工具的 agent [5] | 2026-08 | 能力边界从“动作生成”扩到“任务编排” [5] | 较大概率（仅标题级，`> 待核实`） |
| “embodiment 缩放律”被提出 [24] | 2025-05 | 跨本体问题开始获得可证伪的定量假设 [24] | 较大概率（未被独立验证） |
| 个性化操作被形式化为基准 [21] | 2026-10 | 长尾/个性化从“demo 特性”变成“可测维度” [21] | 确定（新预印本） |
| 跨本体子方向引用极低（0 与 2 次）[31][34] | 2025–2026 | 该方向尚未形成注意力聚集，属低竞争区 [31][34] | 确定（有引用数） |

### 7.2 可证伪预测（未来 6–18 个月）

> 以下均为 `[P]` 预测，附依据链、置信度与证伪条件。

**[P1] VLA 推理性能基准将出现（置信度：中）**
- 依据链：推理栈过重已被列为一等问题 [3] → 但现有工作不报延迟/吞吐/硬件 [3] → 无法横向比较的痛点会催生统一基准。
- 证伪条件：若到 **2027-06** 仍无任何公开的、跨模型统一的 VLA 推理延迟/吞吐基准（含硬件规格与控制频率口径），则本预测不成立。

**[P2] 跨本体缩放律将被至少一次独立复现或反驳（置信度：中低）**
- 依据链：假设已被明确提出 [24] → 该子方向引用密度极低（[31] citations=0、[34] citations=2）[31][34] → 低竞争 + 高杠杆通常吸引跟进。
- 证伪条件：若到 **2027-10** [24] 的 scaling law 仍未获得任何第三方引用式复现或明确反驳，则本预测不成立。

**[P3] 推理期干预将从合成数据迁移到至少一个闭环安全指标（置信度：中低）**
- 依据链：[1] 已证明剂量响应存在且可定位到层 [1] → 但仅 50 个合成场景、以位移度量 [1] → 下一步自然是在闭环指标上验证。
- 证伪条件：若到 **2027-10** 仍无任何工作把推理期注意力/激活干预与接管率、碰撞率或任务成功率之一关联评测，则本预测不成立。

**[P4] 个性化/长尾操作基准将出现并列对比榜单（置信度：低）**
- 依据链：[21] 刚把个性化操作形式化 [21] → 新基准通常在 12 个月内形成对比表格与榜单。
- 证伪条件：若到 **2027-10** [21] 仍无任何第三方在其设定上报告对比结果，则本预测不成立。

### 7.3 Watchlist（值得持续关注）

1. **π0 / openpi 的权重与许可证边界**——[3] 只证明可被第三方封装，未证明权重开放范围 [3]，`> 待核实`。
2. **GR00T N1 的“开放”具体含义**（权重 / 数据 / 仅代码）[13]，`> 待核实`。
3. **LeRobot 的栈覆盖清单与 ROS2 接口**——摘要截断，需读全文 [14]。
4. **LIBERO-PeRM 与原始 LIBERO 的评测口径差异** [21]，`> 待核实`。
5. **BEHAVIOR 赛道的榜单独立性与真机/仿真比例** [7]，`> 待核实`。
6. **跨本体三件套的相互可比性**：[24]（本体数量缩放）vs [31]（相机空间 MoE）vs [34]（图结构 embodiment transformer），三者是否在同一设定上对比，`> 待核实`。

### 7.4 本周期未能判定的关键问题（诚实收口）

- 哪些 VLA SOTA 已被**独立验证**：`> 待核实`——除 [34] 外，本批全为预印本，无第三方复现或榜单排名 [1][2][3][5][7][31]。
- RT-1/RT-2/Diffusion Policy/ACT 与新一代模型在**架构、动作表征、数据配方**上的逐项差异：`> 待核实`——本批无相应一手来源。
- Open X-Embodiment / DROID / LIBERO / CALVIN / SimplerEnv / RoboArena 的覆盖范围与榜单可信度：`> 待核实`——本批零覆盖。
- 真机部署规模、政策监管、资本流向：`> 待核实`——本批零覆盖。
- 检索质量问题：候选集中混入 21 条无关文献（如 [4][22] 视频质量评测、[15][16][28] 天体物理、[17] 部分子分布函数、[25][26] 拜占庭容错优化、[27][30] 遥感数据生成），提示本轮召回存在**明显主题漂移**，建议以“模型名 + benchmark 名 + 年份”重构精确查询后重检。

---

## 参考来源

[1] Inference-Time Attention Steering for Vision-Language-Action Driving Models — http://arxiv.org/abs/2608.17095v1
[2] Compositional Context Fine-Tuning Vision-Language Model for Complex Assembly Action Understanding from Videos — http://arxiv.org/abs/2607.10797v1
[3] BLURR: A Boosted Low-Resource Inference for Vision-Language-Action Models — http://arxiv.org/abs/2512.11769v1
[4] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1
[5] Evolve Vision-Language-Action Model into an Agent with On-the-fly Tool-use — http://arxiv.org/abs/2608.14047v3
[6] Vision Mamba: A Comprehensive Survey and Taxonomy — http://arxiv.org/abs/2405.04404v1
[7] Task adaptation of Vision-Language-Action model: 1st Place Solution for the 2025 BEHAVIOR Challenge — http://arxiv.org/abs/2512.06951v2
[8] UIC-AIHealth4All at ArchEHR-QA 2026: Answer-First Evidence Grounding for Clinical Question Answering — http://arxiv.org/abs/2608.27467v1
[9] EgoDatasets: A Dataset-Centric Survey and Taxonomy for Egocentric Vision and Action Anticipation — https://doi.org/10.20944/preprints202608.0778.v1
[10] Bridging the Dimensionality Gap: A Taxonomy and Survey of 2D Vision Model Adaptation for 3D Analysis — https://doi.org/10.5220/0014289900004084
[11] Taxonomy Classification of Large Language Model Survey Papers — https://doi.org/10.31224/3975
[12] CLAD: Constrained Latent Action Diffusion for Vision-Language Procedure Planning — https://doi.org/10.1109/ro-man72286.2026.11714614
[13] GR00T N1: An Open Foundation Model for Generalist Humanoid Robots — http://arxiv.org/abs/2503.14734v2
[14] LeRobot: An Open-Source Library for End-to-End Robot Learning — http://arxiv.org/abs/2602.22818v1
[15] The YREC Stellar Evolution Code: Public Data Release — http://arxiv.org/abs/2603.25792v1
[16] The LOFAR Two-metre Sky Survey: Deep Fields Data Release 2. I. The ELAIS-N1 field — http://arxiv.org/abs/2501.04093v1
[17] HOPPET v2 release note — http://arxiv.org/abs/2510.09310v3
[18] OpenPI-C: A Better Benchmark and Stronger Baseline for Open-Vocabulary State Tracking — http://arxiv.org/abs/2306.00887v2
[19] Emergent World Representations in OpenVLA — http://arxiv.org/abs/2509.24559v1
[20] Multi-lingual Evaluation of Code Generation Models — http://arxiv.org/abs/2210.14868v3
[21] LIBERO-PeRM: Benchmarking Personalized Robotic Manipulation — http://arxiv.org/abs/2610.22372v1
[22] VQualA 2025 Challenge on Visual Quality Comparison for Large Multimodal Models: Methods and Results — http://arxiv.org/abs/2509.09190v1
[23] Figure 9: Less than half of the participants preserve their code for more than eight years without maintaining and 76.2% of them use code hosting site (e.g., GitHub) for preserving their code. — https://doi.org/10.7717/peerjcs.163/fig-9
[24] Towards Embodiment Scaling Laws in Robot Locomotion — http://arxiv.org/abs/2505.05753v2
[25] Data Encoding for Byzantine-Resilient Distributed Optimization — http://arxiv.org/abs/1907.02664v2
[26] Byzantine-Resilient SGD in High Dimensions on Heterogeneous Data — http://arxiv.org/abs/2005.07866v1
[27] TerraGen: A Unified Multi-Task Layout Generation Framework for Remote Sensing Data Augmentation — http://arxiv.org/abs/2510.21391v1
[28] Constraints on dark energy from H II starburst galaxy apparent magnitude versus redshift data — http://arxiv.org/abs/1110.5626v1
[29] LLM-INSTRUCT at UZH Shared Task 2026: Constraint-Aware Retrieval and Selective Debate for Paragraph-Level Argument Mining — http://arxiv.org/abs/2607.20430v1
[30] AeroGen: Enhancing Remote Sensing Object Detection with Diffusion-Driven Data Generation — http://arxiv.org/abs/2411.15497v3
[31] CM-VLA: Camera-Space-Guided Mixture-of-Experts Policy for Few-shot Cross-Embodiment Transfer — https://doi.org/10.2139/ssrn.6915199
[32] Data Scaling and Generalization Insights for Medicinal Chemistry Deep Learning Models — https://doi.org/10.1021/acs.jcim.5c00538.s002
[33] Data Scaling and Generalization Insights for Medicinal Chemistry Deep Learning Models — https://doi.org/10.1021/acs.jcim.5c00538.s001
[34] GET-Zero: Graph Embodiment Transformer for Zero-Shot Embodiment Generalization — https://doi.org/10.1109/icra55743.2025.11127922

---

*Generated by research-bot · topic=`具身智能与视觉-语言-动作vla前沿` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`deepseek-v4-flash` · sources=34 · duration=208s · 2026-10-22T22:19:48+00:00*
