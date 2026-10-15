# 具身智能与视觉-语言-动作（VLA）前沿增量快照（2024–2026）

**元信息**
- 报告日期：2026-10-15（UTC）
- 领域：具身智能（Embodied AI）／视觉-语言-动作模型（Vision-Language-Action, VLA）／机器人软件栈（C++、ROS2 语境）
- 本次可引用来源数量：**36 条**（编号 [1]–[36]）
- 基线定义：以 RT-2 [28]、OpenVLA [15]、Open X-Embodiment/RT-X [35] 作为“上一代基线”，本报告只讨论**相对该基线的新增变化**。
- **证据基础的重要限制（须先读）**：本次 36 条来源中，与 VLA/具身智能**直接相关**的仅约 9 条（[3][9][10][11][15][26][28][33][35][36]），其余多为跨领域噪声（短视频互动预测 [1]、图像超分 [4]、语音 MOS [6]、越南语法律问答 [7]、强透镜宇宙学 [8]、HLS 数据集 [20]、开源软件工程综述 [13][14][23] 等）。因此本报告在多处**只能给出定性判断并标注 `> 待核实`**，不做数字外推。

---

## 1. 进展与热点（Progress & Hotspots）

**一句话增量判断**：相对 RT-2/OpenVLA 的“离散动作 token + 自回归”基线，可核查的最大增量有两项——(a) 竞赛级 SOTA 已转向 **flow matching 连续动作生成**架构；(b) 真机数据规模被推到 **10 万小时级**。但本次证据集中**没有任何真机成功率或榜单数字**，故“SOTA 变动”只能定性陈述。

**1.1 竞赛级 SOTA 的架构更替（2025-12）**
- point：2025 BEHAVIOR Challenge 冠军方案建立在 **Pi0.5** 架构之上，首要创新是 flow matching 的 **correlated noise**；摘要明确其击败的是离散动作 token 路线的上一代范式。
  - 热度：`> 待核实` —— 候选块未提供 citations/star/榜单排名 [3]
  - 权威：arXiv 预印本（arXiv:2512.06951v2, cs.RO），候选块**未标注会议或期刊录用**，未见同行评审信息 [3]
  - 关注度：中 —— 依据为“2025 BEHAVIOR Challenge 第 1 名”，属挑战赛头名结果；无引用/下载数据 [3]
  - 推荐度：★★★★☆ —— 本次证据集中**唯一直接命中 VLA 架构代际变化**的论文，但仅有摘要级证据，需全文核实 [3]

**1.2 评测任务形态上移：从短程桌面到长时序双手家务（2025）**
- point：BEHAVIOR Challenge 2025 是含 **50 个长时序家务任务**的大规模照片级真实感仿真基准，同时要求**双手操作、导航与上下文感知决策**。
  - 热度：`> 待核实` [3]
  - 权威：候选块仅称其为 large-scale benchmark，**未给出主办方、版本号或官方基准主页** [3]
  - 关注度：中 —— 被挑战赛冠军方案作为主评测环境提及 [3]
  - 推荐度：★★★★☆ —— 对判断“任务难度相对上一代的提升”很有价值，建议核对官方基准页后引用 [3]

**1.3 证据纪律：仿真头名 ≠ 真机 SOTA**
- point：该冠军结果**仅有仿真证据**，环境被明确限定为 photo-realistic simulation；候选块中不含真机平台、真机任务数或真机成功率。
  - 热度：`> 待核实` [3]
  - 权威：基于候选块对评测环境的直接描述，属一手摘要信息 [3]
  - 关注度：中 —— “仿真 vs 真机”是 VLA 领域公认关键区分点 [3]
  - 推荐度：★★★★☆ —— 用于回答“哪些已被独立验证而非仅演示”，提醒不要把仿真头名等同于真机 SOTA [3]

**1.4 真机数据规模化的新信号（2026）**
- point：**Xiaomi-Robotics-1** 标题即为 “Scaling Vision-Language-Action Models with over 100K Hours of Real-World Trajectories”，声称可在**未见环境开箱即用**执行移动操作任务，并可用极少样本微调适配下游任务。
  - 热度：`> 待核实` [26]
  - 权威：arXiv 预印本（arXiv:2607.15330v2, cs.RO），候选块**未见同行评审**；且为厂商自研模型，属**厂商自述** [26]
  - 关注度：中 —— 依据为“10 万小时真机轨迹”这一规模声明本身；无引用/star 数据 [26]
  - 推荐度：★★★★☆ —— 是本次证据集中最直接的“数据规模增量”信号，但**独立验证缺失** [26]

**1.5 持续学习与流匹配的交叉（2025）**
- point：**Action Flow Matching for Continual Robot Learning** 将流匹配用于机器人持续学习，摘要点出**灾难性遗忘、安全适应、离群**等挑战。
  - 热度：`> 待核实` [33]
  - 权威：arXiv 预印本（arXiv:2504.18471v2, cs.RO）[33]
  - 关注度：低 —— 候选块无引用/star/榜单数据 [33]
  - 推荐度：★★★☆☆ —— 与“流匹配是否只是单任务技巧”的质疑直接相关，属线索级证据 [33]

**1.6 VLA 向“可编排组件”外溢（2026）**
- point：两条 2026 年线索表明 VLA 正从单一策略走向可干预组件：**Evolve VLA into an Agent with On-the-fly Tool-use** [11]，以及 **Inference-Time Attention Steering for VLA Driving Models** [9]（后者作用于驾驶类 VLA）。
  - 热度：`> 待核实` [9][11]
  - 权威：均为 arXiv 预印本；发表时间据 arXiv ID（2607/2608）推断为 2026 年，`> 待核实` [9][11]
  - 关注度：低 —— 候选块未提供引用或社区讨论数据 [9][11]
  - 推荐度：★★★☆☆ —— 提示 VLA 能力边界正从“动作生成”扩到“工具调用/推理时控制”，但证据强度弱 [9][11]

### 1.7 经典与奠基性工作（相对基线，**非**最新进展）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| PaLM-E: An Embodied Multimodal Language Model | 2023（据 arXiv ID 2303 推断） | `> 待核实` | `> 待核实`（候选块无 citations）[36] | arXiv 预印本 [36] | `> 待核实` —— 无引用/star/讨论数据 [36] | ★★★★★ —— 具身多模态语言模型的奠基节点，理解“语言模型接入机器人”的起点 [36] | http://arxiv.org/abs/2303.03378v1 | 把 LLM 与具身感知/规划连起来的早期代表作 |
| RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control | 2023（据 arXiv ID 2307 推断） | `> 待核实` | `> 待核实` [28] | arXiv 预印本 [28] | `> 待核实` —— 候选块未提供引用数 [28] | ★★★★★ —— “动作即语言 token”范式的定义性工作，是本报告基线 [28] | http://arxiv.org/abs/2307.15818v1 | 将 VLM 协同微调为输出机器人动作 |
| Open X-Embodiment: Robotic Learning Datasets and RT-X Models | `> 待核实` | `> 待核实` | `> 待核实` [35] | 项目主页（官方站点）[35] | `> 待核实` [35] | ★★★★★ —— 跨本体数据混合训练的公共基座，任何跨本体泛化讨论都需回溯此处 [35] | https://robotics-transformer-x.github.io/ | 在机器人数据混合上训练 RT-1 与 RT-2（RT-X） |
| OpenVLA: An Open-Source Vision-Language-Action Model | 2024（据 arXiv ID 2406 推断） | `> 待核实` | `> 待核实` [15] | arXiv 预印本 [15] | `> 待核实` [15] | ★★★★★ —— 开源 VLA 的关键锚点，是“可复现性”讨论的基线 [15] | http://arxiv.org/abs/2406.09246v3 | 开源 VLA 模型 |
| On-Policy Robot Imitation Learning from a Converging Supervisor | 2019（据 arXiv ID 1907 推断） | `> 待核实` | `> 待核实` [27] | arXiv 预印本 [27] | `> 待核实` [27] | ★★★☆☆ —— 模仿学习理论侧经典，用于理解 VLA 数据依赖的理论根源 [27] | http://arxiv.org/abs/1907.03423v7 | 收敛监督者下的在策略模仿学习 |

### 1.8 数据集与基准

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| BEHAVIOR Challenge 2025 基准 | 2025 | `> 待核实`（主办方未在候选块给出） | `> 待核实` [3] | 由挑战赛冠军方案摘要描述，官方主页缺失 [3] | 中 —— 挑战赛头名论文的主评测环境 [3] | ★★★★☆ —— 50 个长时序家务任务 + 双手 + 导航，是当前最接近“真家务”的仿真评测之一；**评分口径与是否有第三方复现待核实** [3] | http://arxiv.org/abs/2512.06951v2 | 照片级真实感仿真，长时序复合任务 |
| Open X-Embodiment / RT-X 数据与模型 | `> 待核实` | `> 待核实` | `> 待核实` [35] | 官方项目站点 [35] | `> 待核实` [35] | ★★★★★ —— 跨本体数据集，是判断泛化的公共基准 [35] | https://robotics-transformer-x.github.io/ | 机器人数据混合 + RT-1/RT-2 协同训练 |
| LIBERO / SimplerEnv / DROID / RoboArena | — | — | — | — | — | — | `> 待核实` —— **本次证据集完全未覆盖**，无法评估，需补充检索 | 本次检索的明确缺口，不得据记忆填数 |

---

## 2. 工业界与产品（Industry & Product）

**一句话增量判断**：本次证据集中唯一可核查的产业侧增量是**手机/消费电子大厂自研 VLA**（Xiaomi-Robotics-1 [26]）；ROS2 部署、推理延迟、量产落地等信息**在本证据集内全部缺失**。

**2.1 厂商自研 VLA 进入预印本公开（2026）**
- point：**Xiaomi-Robotics-1** 由厂商署名发布，主张 10 万小时真机轨迹与开箱即用移动操作 [26]。
  - 热度：`> 待核实` [26]
  - 权威：arXiv 预印本（cs.RO），**非同行评审**；厂商自述，无第三方复现 [26]
  - 关注度：中 —— 依据为规模声明（100K 小时）本身具备话题性，但无引用/star/报道数据 [26]
  - 推荐度：★★★★☆ —— 判断“产业方是否已越过研究原型阶段”的关键线索，但必须标注为厂商自述 [26]
- point：从 lab 走向落地的**第二条间接线索**是 VLA 的“智能体化”与工具调用（on-the-fly tool-use）[11]，以及驾驶场景的推理时干预 [9]——说明 VLA 被尝试嵌入更大系统而非独立策略。
  - 热度：`> 待核实` [9][11]
  - 权威：arXiv 预印本 [9][11]
  - 关注度：低 —— 无引用/讨论数据 [9][11]
  - 推荐度：★★★☆☆ —— 产品化路径的早期信号，证据弱 [9][11]

**2.2 未获证据的落地问题（明确缺口）**
- ROS2 集成方式、C++/Python 推理栈、端侧延迟与算力占用、真机任务成功率：`> 待核实` —— 本次证据集中**无任何一条**提供相关数据。
- 特别提示：[29] 标题含 “RT-Bench”，但实为**实时应用基准框架**，与机器人 VLA 推理无关；[34] 标题含 “RT-2” 但实为 **CORONAS-PHOTON 卫星载荷地面标定**。二者**不可**用作 VLA 证据（避免误引）。

### 2.3 开源项目与工程实践现状

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| OpenVLA（开源权重与代码） | 2024（据 arXiv ID 2406 推断） | `> 待核实` | `> 待核实` —— 候选块未提供 GitHub star/下载量 [15] | arXiv 预印本 + 开源项目 [15] | `> 待核实` [15] | ★★★★★ —— 本次证据集中**唯一明确“open-source”的 VLA 模型**，是评估复现难度的唯一起点 [15] | http://arxiv.org/abs/2406.09246v3 | 开源 VLA；实际 star 数、许可证、推理延迟均待核实 |
| Open X-Embodiment / RT-X（数据 + 模型发布） | `> 待核实` | `> 待核实` | `> 待核实` [35] | 官方项目站点 [35] | `> 待核实` [35] | ★★★★☆ —— 可作为工程侧数据基础设施参考 [35] | https://robotics-transformer-x.github.io/ | 开放数据集与模型 |
| 其余 VLA 训练框架（如 LeRobot 类工具链） | — | — | — | — | — | — | `> 待核实` —— **本次证据集完全未覆盖**，需补充检索 | 不得据记忆填写 star 或功能 |
| Pi0.5 及其实现 | 2025 | `> 待核实` | `> 待核实` [3] | 仅在冠军方案摘要中被引用为架构基础 [3] | 中 —— 作为冠军方案基座被提及 [3] | ★★★★☆ —— 是“当前竞赛级 SOTA 基座”的关键词，但**其是否开源、权重是否可得，本证据集未说明** [3] | http://arxiv.org/abs/2512.06951v2 | 架构来源，非本报告的独立来源 |

**可复现性结论**：本次证据集**无法评估**任何 VLA 项目的复现难度——没有 star、issue 数、权重许可、硬件门槛数据。

---

## 3. 蓝海与缺口（Blue Ocean & Gaps）

**一句话增量判断**：本周期最清晰的“无人区”不是模型架构，而是**从仿真 SOTA 到真机可复现验证的中间层**——评测口径、真机复现报告与工程延迟基准三者同时缺失。

1. **真机验证缺口**：BEHAVIOR Challenge 2025 头名仅有仿真证据 [3]；候选证据中无任何真机成功率。→ 谁先给出**第三方真机复现**，谁就占据可信度高地。`> 待核实`（是否存在此类报告，本次未检索到）
2. **量化对比缺口**：本次无 RT-2 [28]、OpenVLA [15] 的任何任务数/成功率/引用数，**无法量化**“相对上一代新增了多少”。
3. **数据集与榜单覆盖缺口**：LIBERO、SimplerEnv、DROID、RoboArena 在证据集内**零覆盖**（`> 待核实`）。
4. **长时序 + 双手 + 失败恢复**：50 个长时序家务任务 [3] 暴露的是“复合任务编排”而非单步抓取——该方向的方法论文（如何做长程记忆与错误恢复）在本次证据集中**缺席**。
5. **持续学习 / 灾难性遗忘**：仅 [33] 一条线索，且为预印本；真机长期运行的“退化”问题基本无人验证 [33]。
6. **推理时可控性**：attention steering [9] 与 on-the-fly tool-use [11] 指向“运行时可干预”，但**缺少统一评测**。
7. **检索层面的缺口（方法学）**：本次 36 条来源中约 2/3 为跨领域噪声（[1][4][6][7][8][12][13][14][20][23] 等），说明主题检索的关键词与过滤策略需重构，否则后续增量追踪会持续失真。

---

## 4. 瓶颈与拐点（Bottleneck & Inflection）

**一句话增量判断**：瓶颈正从“模型够不够大”迁移到“数据从哪来、评测算不算数”；拐点信号是**架构换代**与**真机数据规模化**同时出现，但两者都尚未被独立验证。

| 瓶颈 | 现状证据 | 是否临近拐点 | 拐点信号 |
|---|---|---|---|
| 数据 | 真机轨迹被推到 100K 小时级（厂商自述）[26] | 可能（未证实） | 若出现第三方基于该量级数据的复现或对比，即视为拐点 [26] |
| 评测 | 任务从短程桌面升级为 50 个长时序家务 [3] | 是（评测侧） | 仿真基准成为竞赛主战场 [3]；但**仿真-真机 gap 未解决** |
| 算法/架构 | 竞赛级 SOTA 转向 flow matching 连续动作生成 [3]；流匹配亦进入持续学习 [33] | 是 | 相对 RT-2/OpenVLA 的离散 token 路线 [28][15] 出现明确替代方案 [3] |
| 工程/成本 | ROS2 部署、推理延迟、算力占用数据全缺 | `> 待核实` | 无信号；[29] 为实时系统基准，**与机器人推理无关，不可借用** |
| 泛化 | 跨本体仍是公共议题（Open X-Embodiment [35]） | `> 待核实` | 无新证据 |
| 治理/透明度 | 基础模型透明度指数续版并新增数据获取指标 [5] | 可能 | 逐年连续评估本身是制度化信号 [5]；对具身厂商的覆盖度 `> 待核实` |

---

## 5. 社会·政策·国际（Society, Policy & Geopolitics）

**一句话增量判断**：本证据集内**唯一可核查的政策侧增量**是基础模型透明度评估的第三版；与机器人相关的监管、标准、地缘与劳动影响**无证据**，本周期不作判断。

- point：**The 2025 Foundation Model Transparency Index** 为第三版年度评估，新增与**数据获取（data acquisition）**相关的指标。
  - 热度：`> 待核实` [5]
  - 权威：arXiv 预印本（arXiv:2512.10169v1, cs.AI），候选块未标注录用会议 [5]
  - 关注度：中 —— 依据为“连续第三版年度报告”的连续性 [5]；未见引用数或被评厂商名单
  - 推荐度：★★☆☆☆ —— 与 VLA 技术进展仅**间接相关**，仅在讨论具身厂商开放/透明度生态时作背景引用 [5]
  - **覆盖范围限制**：该指数针对“基础模型开发者”整体，**是否覆盖 VLA/具身智能厂商，候选块未说明** → `> 待核实` [5]
- 其他维度（机器人安全标准、出口管制、供应链、数据合规、劳动替代）：**本周期在本证据集内无显著可核查变化**，不做推测性叙述。
- 国际竞争格局：仅有“厂商自研 VLA 公开发布”这一单一信号 [26]，不足以支撑地缘结论 → `> 待核实`。

---

## 6. 资本与生态（Capital & Ecosystem）

**一句话增量判断**：本证据集内**没有任何**融资、并购、人才流动或市场规模数据——该维度只能给出“结构性信号”，不能给出“增量事实”。

- 信号（弱）：消费电子大型厂商以署名预印本形式发布 VLA 模型 [26]，可解读为公司级研发投入的**外部可见痕迹**；但金额、团队规模、产品化时间表均无证据 → `> 待核实` [26]。
- 开源生态锚点：OpenVLA [15] 与 Open X-Embodiment/RT-X [35] 构成目前可核实的两个开放锚点；其 star、下载、贡献者增长等**生态度量全部缺失** → `> 待核实` [15][35]。
- **证据剔除说明**：来源 [21][22]（GitHub sponsor，DOI 类）、[23]（R 语言 GitHub 质检工具）、[13][14]（通用开源软件工程综述）虽属“开源生态”关键词命中，但**与具身智能/VLA 无实质关联**，按证据纪律不予采信为主题结论。
- 结论：资本与生态维度在本周期内**无显著可核查变化**（不是“没有发生”，而是**本次证据不足以判断**）。

---

## 7. 信号与预测（Signals & Forecast）

**信号清单（Signal）**

| # | 信号 | 时间 | 证据 | 强度 |
|---|---|---|---|---|
| S1 | 竞赛级 SOTA 基座从离散动作 token 转向 flow matching 连续动作生成 | 2025-12 | [3] | 中（预印本，无同行评审） |
| S2 | 真机数据规模被推至 10 万小时级 | 2026 | [26] | 中低（厂商自述，无第三方验证） |
| S3 | 评测任务上移为长时序双手家务 + 导航 | 2025 | [3] | 中 |
| S4 | VLA 走向可编排组件：工具调用、推理时干预 | 2026 | [9][11] | 低 |
| S5 | 流匹配扩展至持续学习场景 | 2025 | [33] | 低 |
| S6 | 基础模型透明度评估制度化、续版并纳入数据获取指标 | 2025-12 | [5] | 中（与具身间接相关） |

**预测 [P]（均写成可证伪假设）**

- **[P] P1｜架构判断（置信度：中）**
  假设：**若到 2027 年中，新发布的主流 VLA（含开源权重）中 ≥ 半数采用 flow matching / diffusion 类连续动作头，则“离散 token 自回归退居次要路线”成立**；否则证伪。
  依据链：S1（竞赛头名采用该架构 [3]）→ S5（该范式已外溢到持续学习 [33]）→ 与基线 RT-2/OpenVLA 的离散路线形成对照 [28][15]。
- **[P] P2｜验证缺口（置信度：中低）**
  假设：**若到 2026 年底仍无 BEHAVIOR Challenge 2025 头名方案的第三方真机复现报告，则“仿真 SOTA 不可当真机 SOTA”这一判断继续成立**。
  依据：该结果明确限定于 photo-realistic simulation [3]。
- **[P] P3｜数据壁垒（置信度：低）**
  假设：**若出现基于 10 万小时级真机轨迹的第三方评测或公开榜单排名，则“真机数据规模即竞争壁垒”成立**；若长期无第三方验证，则该声明停留于厂商自述 [26]。
- **[P] P4｜工程拐点（置信度：低，且当前无证据）**
  假设：**若未来 12 个月内出现公开的 VLA-on-ROS2 推理延迟与真机吞吐对比基准，则工程落地拐点到来**。
  当前状态：本证据集**零覆盖**；[29] 为实时系统基准框架，**不可**用作代理证据。

**Watchlist（值得持续关注）**
1. BEHAVIOR Challenge 2025 冠军方案的**全文与官方榜单**，以及是否出现真机章节 [3]
2. **Pi0.5 及其生态**是否开源、权重与许可证 [3]
3. **Xiaomi-Robotics-1** 是否出现第三方复现或独立评测 [26]
4. **OpenVLA 生态**的后续版本、star/贡献者增长与真机复现报告 [15]
5. **Open X-Embodiment / RT-X** 的数据与模型更新 [35]
6. **LIBERO / SimplerEnv / DROID / RoboArena** 等基准的实际进展（本次未覆盖，需补检）
7. 流匹配范式在**持续学习/长期真机运行**上的实证结果 [33]
8. 基础模型透明度评估是否开始覆盖具身智能厂商 [5]

**不确定性说明**：本报告的多数量化需求（引用数、star、成功率、延迟）在给定证据集中**不存在**；所有此类位置均已标注 `> 待核实`，未做任何数字估计或榜单推断。

---

## 参考来源

[1] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1
[2] TRUST 2025: SCRITA and RTSS @ RO-MAN 2025 — http://arxiv.org/abs/2509.11402v1
[3] Task adaptation of Vision-Language-Action model: 1st Place Solution for the 2025 BEHAVIOR Challenge — http://arxiv.org/abs/2512.06951v2
[4] NTIRE 2025 Challenge on Image Super-Resolution (x4): Methods and Results — http://arxiv.org/abs/2504.14582v3
[5] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1
[6] The AudioMOS Challenge 2025 — http://arxiv.org/abs/2509.01336v1
[7] VLSP 2025 MLQA-TSR Challenge: Vietnamese Multimodal Legal Question Answering on Traffic Sign Regulation — http://arxiv.org/abs/2510.20381v1
[8] TDCOSMO 2025: Cosmological constraints from strong lensing time delays — http://arxiv.org/abs/2506.03023v4
[9] Inference-Time Attention Steering for Vision-Language-Action Driving Models — http://arxiv.org/abs/2608.17095v1
[10] Compositional Context Fine-Tuning Vision-Language Model for Complex Assembly Action Understanding from Videos — http://arxiv.org/abs/2607.10797v1
[11] Evolve Vision-Language-Action Model into an Agent with On-the-fly Tool-use — http://arxiv.org/abs/2608.14047v3
[12] UIC-AIHealth4All at ArchEHR-QA 2026: Answer-First Evidence Grounding for Clinical Question Answering — http://arxiv.org/abs/2608.27467v1
[13] Open Source Software Development Challenges: A Systematic Literature Review on GitHub — http://arxiv.org/abs/2003.10750v3
[14] OSS PESTO: An Open Source Software Project Evaluation and Selection TOol — http://arxiv.org/abs/2102.12267v1
[15] OpenVLA: An Open-Source Vision-Language-Action Model — http://arxiv.org/abs/2406.09246v3
[16] CoReCon: an open, community-powered collection of Reionization constraints — http://arxiv.org/abs/2309.06480v1
[17] OpenPodcar: an Open Source Vehicle for Self-Driving Car Research — http://arxiv.org/abs/2205.04454v2
[18] GitHub open source project recommendation system — http://arxiv.org/abs/1602.02594v1
[19] BotHawk: An Approach for Bots Detection in Open Source Software Projects — http://arxiv.org/abs/2307.13386v1
[20] HLSFactory-Agent: Large-Scale Agentic HLS Dataset Construction from Academic and Open-Source Projects — http://arxiv.org/abs/2609.09519v1
[21] Support open source software as a GitHub sponsor — https://doi.org/10.53731/r8n4c91-97aq74v-ag6v9
[22] Support open source software as a GitHub sponsor — https://doi.org/10.53731/y79qt-zf894
[23] Ghqc: An R-based Open-Source Tool for Semi-Automated Quality Control on GitHub — https://doi.org/10.70534/qevr6966
[24] Summary Analysis of the 2017 GitHub Open Source Survey — https://doi.org/10.31235/osf.io/qps53
[25] Overview of AuTexTification at IberLEF 2023: Detection and Attribution of Machine-Generated Text in Multiple Domains — http://arxiv.org/abs/2309.11285v1
[26] Xiaomi-Robotics-1: Scaling Vision-Language-Action Models with over 100K Hours of Real-World Trajectories — http://arxiv.org/abs/2607.15330v2
[27] On-Policy Robot Imitation Learning from a Converging Supervisor — http://arxiv.org/abs/1907.03423v7
[28] RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control — http://arxiv.org/abs/2307.15818v1
[29] RT-Bench: an Extensible Benchmark Framework for the Analysis and Management of Real-Time Applications — http://arxiv.org/abs/2203.11423v2
[30] A Simulation and Modeling of Access Points with Definition Language — http://arxiv.org/abs/1304.1836v2
[31] Design of an Adaptive Lightweight LiDAR to Decouple Robot-Camera Geometry — http://arxiv.org/abs/2302.14334v2
[32] Secure and secret cooperation in robotic swarms — http://arxiv.org/abs/1904.09266v3
[33] Action Flow Matching for Continual Robot Learning — http://arxiv.org/abs/2504.18471v2
[34] Instruments of RT-2 Experiment onboard CORONAS-PHOTON and their test and evaluation I: Ground calibration of RT-2/S and RT-2/G — http://arxiv.org/abs/1011.3326v1
[35] Open X-Embodiment: Robotic Learning Datasets and RT-X Models — https://robotics-transformer-x.github.io/
[36] PaLM-E: An Embodied Multimodal Language Model — http://arxiv.org/abs/2303.03378v1

---

*Generated by research-bot · topic=`具身智能与视觉-语言-动作vla前沿` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`deepseek-v4-flash` · sources=36 · duration=181s · 2026-10-15T22:16:53+00:00*
