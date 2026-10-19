# 具身智能与 Vision-Language-Action（VLA）前沿增量快照（2024–2026）

**日期**：2026-10-19（UTC）｜**领域**：具身智能 / Vision-Language-Action（VLA）/ 机器人软件栈｜**检索源**：29 条（其中与 VLA/具身智能直接相关 13 条、经典与工程方法 5 条、边缘相关 5 条、检索噪声 6 条）

> **证据基础与方法说明（必读）**
> 本报告严格遵守“只用可核查来源”的纪律。本次证据集 **29 条全部为 arXiv 链接**，**不含任何 GitHub 仓库、HuggingFace 权重页、榜单页面、厂商官方博客或融资公告**。因此：
> 1. **热度证据（引用数 / star / 下载量 / 榜单排名）在本报告中几乎全部为 `> 待核实`**——不是遗漏，而是证据集内确实不存在这些字段，任何具体数字都将是编造。
> 2. **权威证据**只能标注为“arXiv 预印本 + arXiv 分类（cs.RO / cs.CV / cs.CL 等）”，**无法确认是否已被 RSS/CoRL/ICRA/NeurIPS 等接收**，故一律不写会议名。
> 3. 结构化发现中存在明确误召回，本报告已剔除并在正文标注：[5] 为短视频互动度预测挑战赛、[6] 为图像超分辨率挑战赛、[9] 为 AudioMOS 语音评测、[11] 为强引力透镜宇宙学、[18] 为 RowHammer 硬件安全、[22] 为越南语交通标志法律问答——**六者与 VLA/具身智能无关，不得作为本领域证据使用**。
> 4. 报告中所有论文结论均基于摘要片段，**未做全文精读**，涉及具体指标/任务数/本体的判断一律标注 `> 待核实`。

---

## 1. 进展与热点（Progress & Hotspots）

**一句话增量判断**：2025–2026 年 VLA 的增量不在“更大的端到端模型”，而在**推理时干预（inference-time steering）、工具注入（tool-use）、低资源推理、跨本体缩放律**四个“模型外围”方向；但本证据集内**没有任何一条给出可与 LIBERO / SimplerEnv / Open X-Embodiment 榜单对齐的数字**，因此“SOTA 是否迁移”无法核实。

### 1.1 最新进展（2025–2026，相对 2024 基线的增量）

| # | 进展 | 时间 | 相对基线的增量 | 证据强度 |
|---|------|------|----------------|----------|
| P1 | **ART（Agentic Robot with Tool-use）**：把任意 VLA 模型改造成可调用现成工具模块（低层视觉、高层 affordance、本体增强）的 agent [15] | 2026（arXiv 2608.14047v3） | 从“VLA 输出动作”转向“VLA 调度工具”，是**能力解耦**而非参数扩张 | 仅摘要，cs.RO 预印本；无实验数字可核 [15] |
| P2 | **推理时注意力偏置（pre-softmax additive attention bias）** 用于 VLA 驾驶模型，无需重训即可把注意力重定向到安全关键目标 [13] | 2026（arXiv 2608.17095v1） | 首次（在本证据集内）把“推理时可控制性”引入 VLA，替代重训练/微调 | 仅摘要；cs.CV；驾驶域单一场景 [13] |
| P3 | **Embodied-R1.5**：统一 Embodied Foundation Model（EFM），把具身认知、任务规划、纠错、pointing 收敛到单一架构 [27] | 2026（arXiv 2606.11324v2） | 从“VLA=动作策略”扩展为“具身基础模型=推理+规划+指向+纠错” | 仅摘要，且摘要关于“three automated da…”处截断，数据构建细节 `> 待核实` [27] |
| P4 | **Embodiment Scaling Laws**：系统检验“训练本体数量↑ → 未见本体泛化↑”假设 [26] | 2025（arXiv 2505.05753v2） | 把 scaling law 从“数据/参数”搬到“本体多样性”，为跨本体数据采集提供定量依据 | 摘要明确写“enabling factors remain poorly understood”，说明结论仍初步 [26] |
| P5 | **BLURR**：面向 VLA 的低资源推理加速 [19] | 2025（arXiv 2512.11769v1） | 承认 VLA 推理开销是部署瓶颈，从算法侧压缩 | 仅摘要；加速比/硬件 `> 待核实` [19] |
| P6 | **BEHAVIOR Challenge 2025 第一名方案**：VLA 的任务适配（task adaptation）[20] | 2025（arXiv 2512.06951v2） | 提供本证据集内**唯一带公开竞赛榜单背书**的 VLA 工程化路径 | 竞赛名次可核，但属“自评+赛事自设指标”，非第三方独立复现 [20] |
| P7 | **X-Nav**：单一统一策略跨多种移动机器人本体做端到端导航 [12] | 2025（arXiv 2507.14731v2） | 跨本体泛化从“操作”外溢到“导航” | 仿真/真机比例 `> 待核实` [12] |
| P8 | **VLA 注意力头可用于路径偏差检测**（探针式可解释性）[16] | 2026（arXiv 2603.13782v1） | 把 VLA 内部表征当作可读取的“故障检测器”，呼应 P2 的“推理时干预”线索 | 仅摘要 [16] |
| P9 | **VLM 适配装配动作理解**（Compositional Context Fine-Tuning, CCFT）[14] | 2026（arXiv 2607.10797v1） | 面向人机协作装配的细粒度手-物交互理解，属“感知侧”而非“控制侧”增量 | 仅摘要；cs.CV [14] |
| P10 | 两篇综述提供脉络骨架：**人类视频→机器人操作的 VLA 可扩展学习综述** [17]（2026）、**具身 AI 综合综述** [23]（2024，v8 更新） | 2024–2026 | 前者锁定“人类中心数据”这一数据侧主线，后者提供“仿真—真机—基础模型”taxonomy | 综述本身为二手综合，引用其结论需回溯原始文献 [17][23] |

> **关于 SOTA 的诚实结论**：本证据集中**没有任何一条**报告在 LIBERO、SimplerEnv、RoboArena、Open X-Embodiment 标准划分上的可比数字，也没有说明任务数、本体型号、真机/仿真比例。因此“2024–2026 年 VLA 的 SOTA 是否迁移、迁移多少”在本证据集内 **`> 待核实`**。原始抽取把 [5]（短视频互动度预测）列为 q1 的 VLA 增量，属**检索噪声，已剔除**。

### 1.2 经典与奠基性工作（对照基线，非本周期增量）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| On-Policy Robot Imitation Learning from a Converging Supervisor | 2019 | `> 待核实`（证据集未提供作者） | `> 待核实` | arXiv 预印本，cs.LG [2] | 低—中（无引用数据；仅据其被后续 IL 工作反复引用的一般认知，**具体引用数 `> 待核实`**） | ★★★☆☆ | http://arxiv.org/abs/1907.03423v7 | 把 DAgger 的“固定监督者”放宽为“演进中的监督者”，是 on-policy IL 的理论前身 [2] |
| Open-Ended Learning Leads to Generally Capable Agents | 2021 | `> 待核实` | `> 待核实` | arXiv 预印本 [10] | 中（开放-ended 训练范式的代表工作，具体引用数 `> 待核实`） | ★★★★☆ | http://arxiv.org/abs/2107.12808v2 | “开放-ended 任务生成 → 通用 agent”，是今天 VLA 数据规模化的思想祖先 [10] |
| One-Shot Reinforcement Learning for Robot Navigation with Interactive Replay | 2017 | `> 待核实` | `> 待核实` | arXiv 预印本 [7] | 低（无数据） | ★★☆☆☆ | http://arxiv.org/abs/1711.10137v2 | 单样本 + 交互回放的导航 RL，属前基础模型时代的样本效率探索 [7] |
| Learning to Discern: Imitating Heterogeneous Human Demonstrations with Preference and Representation Learning | 2023 | `> 待核实` | `> 待核实` | arXiv 预印本，cs.RO [1] | 低—中（无数据） | ★★★☆☆ | http://arxiv.org/abs/2310.14196v1 | 直接命中“人类演示质量参差”这一至今未解的数据瓶颈 [1] |
| A ROS-based Software Framework for the NimbRo-OP Humanoid Open Platform | 2018 | `> 待核实` | `> 待核实` | arXiv 预印本 [21] | 低（无数据） | ★★☆☆☆ | http://arxiv.org/abs/1809.11051v1 | ROS1 时代人形平台软件框架，是“ROS2 部署 VLA”议题的历史参照系 [21] |

> 说明：**ROS2 原生 VLA 部署栈在本证据集中完全没有出现**。[21] 是 2018 年的 ROS1 框架，不能作为 2024–2026 工程栈成熟度的证据；`ROS2 + VLA 推理节点 / 实时性 / DDS QoS` 相关结论 **`> 待核实`**。

### 1.3 开源项目与工程实践栈

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| Open X-Embodiment / RT-X | 2023 | Open X-Embodiment 协作组（作者列表 `> 待核实`） | `> 待核实`（无 GitHub star 数据） | arXiv 预印本，cs.RO [3] | 高（跨本体机器人数据的事实标准基座，社区讨论热度高；**star/下载量数字 `> 待核实`**） | ★★★★★ | http://arxiv.org/abs/2310.08864v9 | 统一多机构、多本体机器人数据格式并训练 RT-X，是 VLA 数据侧的地基 [3] |
| ART（tool-injection 框架） | 2026 | `> 待核实` | `> 待核实` | arXiv 预印本，cs.RO [15] | 低（新近发布，无社区信号） | ★★★☆☆ | http://arxiv.org/abs/2608.14047v3 | 声称可“tune any VLA model”，但**代码/权重是否开源 `> 待核实`**，复现难度未知 [15] |

> 诚实声明：本证据集**不含任何 GitHub / HuggingFace 链接**，因此“开源成熟度（star、最近提交、issue 活跃度、权重是否放出）”在本报告中**无法评估**，一律 `> 待核实`。任何“某项目已开源、可直接微调”的表述都不应据本报告采信。

### 1.4 数据集与基准

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| Open X-Embodiment（OXE） | 2023 | 协作组，`> 待核实` | `> 待核实` | arXiv 预印本 [3] | 高（跨本体数据基座；量化热度 `> 待核实`） | ★★★★★ | http://arxiv.org/abs/2310.08864v9 | 本证据集内唯一可称“数据集基座”的资源；其标准划分上的最新 SOTA `> 待核实` [3] |
| BEHAVIOR Challenge 2025 | 2025 | 赛事组织方 `> 待核实` | `> 待核实` | 竞赛（赛事评审），配套论文为 arXiv 预印本 [20] | 中（有公开榜单与名次，是本证据集内**评测可信度最高**的一项） | ★★★★☆ | http://arxiv.org/abs/2512.06951v2 | 家庭级长程操作 benchmark；第一名方案公开，但**是否真机、任务数 `> 待核实`** [20] |
| Dialogue Robot Competition 2023 | 2023 | `> 待核实` | `> 待核实` | 竞赛论文集，arXiv [4] | 低（与操作类 VLA 关联弱） | ★★☆☆☆ | http://arxiv.org/abs/2312.14430v5 | 对话机器人竞赛，仅作“机器人竞赛生态”旁证，**不作为 VLA 基准** [4] |

---

## 2. 工业界与产品（Industry & Product）

**一句话增量判断**：在本证据集范围内，**本周期无显著可核实的产业化增量**——没有厂商产品发布、量产公告、真机部署规模数据或商业模式证据；仅有“产业界开始系统性讨论安全与部署”的间接信号。

- 唯一直接触及产业侧的是 **SAE World Congress 2026 的 embodied AI 专题综述**，主题为 safety、trust、robotics 与 real-world deployment，指出具身 AI 正从研究走向自动驾驶、移动机器人、工业机械等真实系统，并带来新的安全与信任挑战 [29]。**注意证据等级**：这是**会议综述性论文**，反映“产业界在讨论什么”，**不是**“某产品已部署”的证据 [29]。
- **BEHAVIOR Challenge 2025 第一名方案**说明存在“竞赛→工程化方案”的转化路径，属生态信号而非产品信号 [20]。
- **BLURR** 针对 VLA 低资源推理 [19]，可解读为“边缘/嵌入式部署压力真实存在”的**间接**证据；但其目标硬件、吞吐、延迟数字均 `> 待核实` [19]。
- 历史对照：**Lumen 社交人形机器人作为电子工程日活动导览员**（2016）是早期“实验室→公共场景”的部署案例，可用于说明服务机器人落地的时间尺度，但**不构成本周期增量** [24]。
- **人形本体设计优化**（面向人机工效的负重搬运）[28] 属本体设计侧工作，与 VLA 软件栈正交，仅作“人形硬件仍是独立研究线”的旁证 [28]。

> `> 待核实`：厂商名称、产品型号、出货量、客户数、真机部署时长、单位成本——本证据集**全部缺失**。任何“某公司已量产 VLA 机器人”的表述在本报告框架下不可采信。

---

## 3. 蓝海与缺口（Blue Ocean & Gaps）

**一句话增量判断**：缺口不在“再训一个更大的 VLA”，而在**推理时可控制性、边缘部署、操作域的本体缩放律、以及可信评测**四处，且每一处目前都只有单点论文、无竞品、无标准。

| 缺口 | 现状（证据） | 为何是蓝海 | 可核查依据 |
|------|--------------|------------|------------|
| G1 **操作域的推理时干预 / 安全护栏** | 仅 [13] 在**驾驶域**做 pre-softmax attention bias；[16] 只做“检测”不做“干预” | 机械臂/人形的高危动作（切割、人机共融）需要“不重训即可限幅/改向”的机制，本证据集内**无操作域工作** | [13][16] |
| G2 **VLA 的边缘/低资源推理** | 仅 [19] 一篇 | 真机部署的功耗/延迟约束是硬门槛，缺少硬件-算法协同设计 | [19] |
| G3 **操作域的本体缩放律** | [26] 只在 **locomotion** 上检验 scaling law 假设 | “加本体”是否比“加数据/加参数”更划算，决定数据采集预算分配；操作域空白 | [26] |
| G4 **人类视频 → 机器人动作的可扩展迁移** | [17] 综述将其列为主线，但数据对齐、视角域差、动作空间映射仍未解 | 人类视频是唯一“互联网规模”的具身数据源 | [17] |
| G5 **VLA 的可解释性与故障探针** | 仅 [16] 一篇（注意力头→路径偏差） | 若能把内部表征变成运行时监控信号，可直接用于功能安全认证 | [16] |
| G6 **统一、可复现的真机评测** | 本证据集内仅 [20] 有公开榜单；其余论文均无第三方复现 | 没有共享评测就没有可比较的 SOTA，整个领域的“进展”无法被外部验证 | [20]；其余 `> 待核实` |
| G7 **VLA 与工具调用的标准化接口** | 仅 [15] 提出 tool-injection | 若接口标准化，VLA 可像 LLM 一样接入外部工具生态 | [15] |
| G8 **异构人类演示的质量筛选** | [1]（2023）已提出 preference + representation learning 方案，但**是否被后续 VLA 数据管线采纳 `> 待核实`** | 数据质量而非数量，可能是下一阶段的主要瓶颈 | [1] |

---

## 4. 瓶颈与拐点（Bottleneck & Inflection）

**一句话增量判断**：瓶颈已从“模型容量”转移到**推理成本、跨本体泛化的可预测性、以及评测可信度**；拐点的早期信号是“不重训即可干预”（[13]）与“能力外置为工具”（[15]），但尚未形成范式。

**四类瓶颈与对应证据**

1. **推理成本瓶颈**：VLA 推理开销已大到需要专门的加速方法 [19]；这从“有人写加速论文”反推瓶颈真实存在，但**加速比 `> 待核实`** [19]。
2. **跨本体泛化瓶颈**：[26] 的摘要明确写“其 enabling factors 仍未被很好理解”，即**连“为什么能泛化”都还没有定论** [26]；[12] 用统一策略覆盖多移动本体，但**未见本体数量与成功率的曲线 `> 待核实`** [12]。
3. **长程任务与规划瓶颈**：[27] 需要把 planning、correction、pointing 全部塞进一个 EFM 才能覆盖长程，说明**单一 VLA 策略不足以支撑长程** [27]。
4. **评测可信度瓶颈**：本证据集 13 篇 VLA/具身相关论文中，仅 [20] 挂靠公开竞赛榜单；其余均为自设实验，**无第三方复现、无统一划分** → “SOTA”一词在本领域当前**不可跨论文比较** [20]。
5. **数据质量瓶颈**：异构人类演示的质量参差早在 2023 年就被明确建模 [1]，而 2026 年的综述仍把人类中心数据列为“可扩展 VLA 学习”的核心挑战 [17] → **三年未解，属结构性瓶颈** [1][17]。

**拐点信号（可观测）**

- 信号 A：出现“推理时”而非“训练时”的可控性方法 → 已出现 [13]。
- 信号 B：VLA 从“输出动作”变为“调度工具” → 已出现 [15]。
- 信号 C：把 scaling law 用于本体数量 → 已出现，但仅在 locomotion [26]。
- 信号 D（缺失）：跨机构共享的真机评测榜单 → **尚未出现**（本证据集内）[20]。

> 拐点判据（可证伪）：**若到 2027-06 出现 ≥2 个独立团队在真实机械臂上实现推理时干预并公开代码，则“推理时可控 VLA”可判定为独立子方向；否则本判断失败。**

---

## 5. 社会·政策·国际（Society, Policy & Geopolitics）

**一句话增量判断**：本证据集内**唯一可核实的治理侧增量是“基础模型透明度”被量化成年度指数**；具身智能专属的监管、标准、出口管制与地缘政治证据**全部缺失**。

- **透明度治理**：*The 2025 Foundation Model Transparency Index* 提供了对基础模型透明度的年度量化评估 [8]。**限定**：该指数是否覆盖具身/VLA 模型、其指标是否包含“机器人数据来源披露”，`> 待核实` [8]。
- **功能安全社区入场**：SAE World Congress 2026 的 embodied AI 专题把 safety、trust 与 real-world deployment 并列讨论 [29]，说明**汽车/工业标准社区**开始把具身系统纳入安全议题；但这是“讨论”而非“标准发布”，**无标准编号、无生效日期** `> 待核实` [29]。
- **劳动影响与伦理**：本证据集仅有间接理论参考——*Intelligent behavior depends on the ecological niche* 主张智能依赖社会文化生态位 [25]，可用于论证“具身智能的能力评估不能脱离部署场景”，但**它不是劳动经济学或伦理治理证据**，不可过度引用 [25]。
- **国际竞争格局 / 出口管制 / 供应链**：本证据集内**无任何来源**。→ **本周期在该维度无显著可核实变化**，任何“中美欧三极格局”“芯片管制影响 VLA 训练”的表述均 `> 待核实`。
- **检索噪声剔除**：原始抽取把 [22]（越南语交通标志法律问答）当作“政策/瓶颈证据”，属误召回，**与具身智能治理无关**，已剔除。

---

## 6. 资本与生态（Capital & Ecosystem）

**一句话增量判断**：本证据集内**无任何融资、并购、估值、人才流动数据**，因此“资本侧增量”在本报告中**无法成立**，只能给出生态结构层面的观察。

**可核实的生态结构信号（非资本数据）**

| 生态位 | 观察 | 证据 |
|--------|------|------|
| 数据基座 | Open X-Embodiment 仍是跨本体数据与 RT-X 模型的公共基座，2023 年发布、被持续引用为起点 | [3] |
| 评测组织形态 | 以“挑战赛 + 公开名次”的方式组织社区（BEHAVIOR 2025、Dialogue Robot Competition 2023） | [20][4] |
| 工程基础设施 | ROS 生态是长期存在的机器人软件底座，但本证据集内只有 2018 年的 ROS1 人形框架，**ROS2 + VLA 的现代工程栈缺失** | [21] |
| 治理侧机构 | 基础模型透明度指数构成外部监督型生态参与者 | [8] |
| 学术综述生态 | 2024–2026 连续出现具身 AI 综合综述与人类视频 VLA 综述，说明领域进入“体系化整理期” | [23][17] |

> **明确留白**：融资金额、投资机构、并购事件、团队规模、薪资与人才流向 —— 本证据集 **0 条**。全部 `> 待核实`。不做任何推测性填补。
> 特别提示：结构化发现中给多条论文标注了“★★★★☆（venue=cs.CV）”式推荐度，该评分实际只依据 arXiv 分类，**不构成权威性或热度判断**，本报告已弃用该评分逻辑（见各表“推荐度”列的实际理由）。

---

## 7. 信号与预测（Signals & Forecast）

### 7.1 早期信号清单

| 编号 | 信号 | 时间 | 类型 | 证据 |
|------|------|------|------|------|
| S1 | VLA 的“推理时注意力干预”出现（无需重训） | 2026 | 技术范式信号 | [13] |
| S2 | VLA 与 agentic tool-use 融合（能力外置） | 2026 | 架构范式信号 | [15] |
| S3 | 本体数量作为 scaling 维度的假设被正式提出 | 2025 | 科学假设信号 | [26] |
| S4 | 面向 VLA 的低资源推理被单独立题 | 2025 | 部署压力信号 | [19] |
| S5 | “具身基础模型（EFM）”统一推理/规划/纠错/指向 | 2026 | 架构收敛信号 | [27] |
| S6 | VLA 内部注意力头被当作可读的故障检测器 | 2026 | 可解释性/安全信号 | [16] |
| S7 | 产业安全社区（SAE）将 embodied AI 纳入安全与信任议题 | 2026 | 治理信号 | [29] |
| S8 | 基础模型透明度被年度量化 | 2025 | 治理量化信号 | [8] |

### 7.2 未来 6–18 个月预判（全部标 [P]，写成可证伪假设）

- **[P] P1（推理时可控 VLA 成为子方向）** 依据链：S1 已出现 → 安全关键场景需要“不重训即可限幅” → 若被复现将快速扩散。**证伪条件**：到 **2027-06** 若仍**只有 ≤1 个团队**在真实机械臂上公开推理时干预的代码与实验，则本判断失败。**置信度：中**。
- **[P] P2（评测瓶颈缓解）** 依据链：当前仅 [20] 有公开榜单 → 跨论文不可比 → 社区有动机建共享榜单。**证伪条件**：到 **2027-12** 若仍未出现“≥3 个独立团队提交、含真机划分”的 VLA 榜单，则本判断失败。**置信度：低—中**。
- **[P] P3（本体缩放律外溢到操作域）** 依据链：S3 在 locomotion 成立 → 操作域数据采集成本更高，动机更强。**证伪条件**：若在 ≥3 类操作本体上，“未见本体成功率”**不随**训练本体数量单调上升，则 scaling law 不可迁移。**置信度：中**。
- **[P] P4（边缘 VLA 落地加速）** 依据链：S4 立题 → 若 [19] 类方法被独立复现并在 Jetson 级硬件达到控制频率实时，则边缘部署门槛下降。**证伪条件**：到 **2027-06** 若无任何独立复现报告在 ≤30W 级硬件上达到 ≥10Hz 闭环控制，则本判断失败。**置信度：低**。
- **[P] P5（EFM 与 VLA 分层）** 依据链：S5 显示“推理/规划”与“动作生成”被拆到不同层级 → 可能形成“EFM 做高层 + 轻量 VLA 做低层”的两层栈。**证伪条件**：若 2027 年前主流方案仍是单一端到端模型直接输出动作、且性能不劣于分层方案，则本判断失败。**置信度：低—中**。

### 7.3 不确定性与争议

- **[Debated] 端到端 vs 分层**：本证据集同时存在“单一统一策略”（[12]）与“统一 EFM + 工具注入”（[15][27]）两条路线，**孰优无定论**，且两类工作均未在同一 benchmark 上对比 `> 待核实`。
- **[Debated] 仿真 SOTA 是否等于真机能力**：本证据集内**无一篇**给出“同一策略在仿真与真机上的对照数字”，该争议在本证据集内**无法裁决**。
- **最大的不确定性**：所有结论建立在**摘要级阅读**之上；[27] 的摘要本身在数据构建处被截断 [27]，[17][23] 为综述（二手综合）。因此本报告的“进展”应被理解为**方向性信号**，而非性能结论。

### 7.4 Watchlist（值得持续关注）

1. **ART 系列**（tool-injection 是否被社区采纳为通用封装层）[15]
2. **推理时注意力干预**是否从驾驶域 [13] 迁移到操作域
3. **Embodiment Scaling Laws** 是否在操作/人形上复现 [26]
4. **Embodied-R1.5 / EFM 路线**的数据构建与评测细节（摘要截断，需读全文）[27]
5. **BEHAVIOR Challenge 2026** 是否形成连续榜单并引入真机赛道 [20]
6. **Foundation Model Transparency Index** 是否新增具身/机器人数据披露维度 [8]
7. **ROS2 + VLA 部署栈**（本证据集完全缺失，属最高优先级补检项）

---

## 参考来源

[1] Learning to Discern: Imitating Heterogeneous Human Demonstrations with Preference and Representation Learning — http://arxiv.org/abs/2310.14196v1
[2] On-Policy Robot Imitation Learning from a Converging Supervisor — http://arxiv.org/abs/1907.03423v7
[3] Open X-Embodiment: Robotic Learning Datasets and RT-X Models — http://arxiv.org/abs/2310.08864v9
[4] Proceedings of the Dialogue Robot Competition 2023 — http://arxiv.org/abs/2312.14430v5
[5] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1
[6] NTIRE 2025 Challenge on Image Super-Resolution (x4): Methods and Results — http://arxiv.org/abs/2504.14582v3
[7] One-Shot Reinforcement Learning for Robot Navigation with Interactive Replay — http://arxiv.org/abs/1711.10137v2
[8] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1
[9] The AudioMOS Challenge 2025 — http://arxiv.org/abs/2509.01336v1
[10] Open-Ended Learning Leads to Generally Capable Agents — http://arxiv.org/abs/2107.12808v2
[11] TDCOSMO 2025: Cosmological constraints from strong lensing time delays — http://arxiv.org/abs/2506.03023v4
[12] X-Nav: Learning End-to-End Cross-Embodiment Navigation for Mobile Robots — http://arxiv.org/abs/2507.14731v2
[13] Inference-Time Attention Steering for Vision-Language-Action Driving Models — http://arxiv.org/abs/2608.17095v1
[14] Compositional Context Fine-Tuning Vision-Language Model for Complex Assembly Action Understanding from Videos — http://arxiv.org/abs/2607.10797v1
[15] Evolve Vision-Language-Action Model into an Agent with On-the-fly Tool-use — http://arxiv.org/abs/2608.14047v3
[16] Your Vision-Language-Action Model Already Has Attention Heads For Path Deviation Detection — http://arxiv.org/abs/2603.13782v1
[17] From Human Videos to Robot Manipulation: A Survey on Scalable Vision-Language-Action Learning with Human-Centric Data — http://arxiv.org/abs/2606.00054v1
[18] JENGA: Exploiting Counter-Based RowHammer Countermeasures to Break Real-Time Predictability — http://arxiv.org/abs/2609.01077v1
[19] BLURR: A Boosted Low-Resource Inference for Vision-Language-Action Models — http://arxiv.org/abs/2512.11769v1
[20] Task adaptation of Vision-Language-Action model: 1st Place Solution for the 2025 BEHAVIOR Challenge — http://arxiv.org/abs/2512.06951v2
[21] A ROS-based Software Framework for the NimbRo-OP Humanoid Open Platform — http://arxiv.org/abs/1809.11051v1
[22] VLSP 2025 MLQA-TSR Challenge: Vietnamese Multimodal Legal Question Answering on Traffic Sign Regulation — http://arxiv.org/abs/2510.20381v1
[23] Aligning Cyber Space with Physical World: A Comprehensive Survey on Embodied AI — http://arxiv.org/abs/2407.06886v8
[24] Design and implementation of computational platform for social-humanoid robot Lumen as an exhibition guide in Electrical Engineering Days 2015 — http://arxiv.org/abs/1607.04763v1
[25] Intelligent behavior depends on the ecological niche: Scaling up AI to human-like intelligence in socio-cultural environments — http://arxiv.org/abs/2103.06769v1
[26] Towards Embodiment Scaling Laws in Robot Locomotion — http://arxiv.org/abs/2505.05753v2
[27] Embodied-R1.5: Evolving Physical Intelligence via Embodied Foundation Models — http://arxiv.org/abs/2606.11324v2
[28] Optimization of Humanoid Robot Designs for Human-Robot Ergonomic Payload Lifting — http://arxiv.org/abs/2211.13503v1
[29] Embodied AI in Action: Insights from SAE World Congress 2026 on Safety, Trust, Robotics, and Real-World Deployment — http://arxiv.org/abs/2605.10653v1

> **来源使用声明**：本报告仅引用上述 29 条。其中 [5][6][9][11][18][22] 经核验与本主题无关（检索噪声），已在正文标注剔除，**未作为任何论断的依据**；[4][24][25][28] 仅作边缘旁证并已注明其局限。

---

*Generated by research-bot · topic=`具身智能与视觉-语言-动作vla前沿` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`deepseek-v4-flash` · sources=29 · duration=175s · 2026-10-19T22:18:54+00:00*
