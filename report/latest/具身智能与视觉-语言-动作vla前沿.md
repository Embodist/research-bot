# 具身智能与视觉-语言-动作（VLA）前沿增量调研报告（2024–2026）

**日期**：2026-10-24（UTC）｜**领域**：具身智能 / Vision-Language-Action（VLA）/ 机器人软件栈｜**检索源**：候选证据 32 条，相关性筛查后采用 21 条，排除 11 条检索噪声（见文末标注）｜**证据口径**：本报告全部结论基于候选块的**标题+摘要片段**，未逐篇精读全文；候选块的 `citations`/`stars` 字段为空，故所有**热度证据一律标注 `> 待核实`，不做任何数字推测**。

> **方法学声明**：本次检索的召回集合包含明显跨域噪声（RowHammer 硬件安全、短视频参与度预测、LHC 机器学习、临床问答、图像超分、Rip Current 检测、REST API 测试、多智能体竞赛、对话机器人竞赛、RT-Middleware 等）。这些条目虽命中关键词，但与 VLA 主题无关，已列入文末「排除清单」，**未用于任何论断**。少量条目（如 [20][32]）标题与经典工作高度相似、易被误引，报告中已单独标注。

---

## 1. 进展与热点（Progress & Hotspots）

**一句话增量判断**：2024–2026 年 VLA 的真正增量**不在"更大更新的基座架构"，而在四条改造既有基座的工程线**——数据规模化、推理加速、工具化 agent 化、竞赛驱动的任务适配。相对 RT-2 [15] 奠定的"VLM 直接输出动作 token"基线，当前热点是**如何把已有 VLA 用得更快、更省、更可控**。

### 1.1 最新进展（近 1–2 年，按增量类型归并）

| 增量类型 | 代表工作 | 相对基线的增量 | 证据强度 | 引用 |
|---|---|---|---|---|
| 真机数据规模化 | Xiaomi-Robotics-1 | 以 **>100K 小时真实世界轨迹**扩展 VLA，宣称可零样本（out-of-the-box）执行未见环境中的移动操作，并支持少样本微调 | 厂商自评（B 级，未见第三方复现） | [14] |
| 实时执行与开源 | Xiaomi-Robotics-0 | 以"实时执行（real-time execution）"为核心卖点的**开源** VLA | 厂商自评（B 级） | [18] |
| 低资源推理 | BLURR | 面向 VLA 的**Boosted Low-Resource Inference**，把推理成本单列为问题 | 预印本（B 级） | [8] |
| 微调效率 | Fine-Tuning VLA: Optimizing Speed and Success | 把"微调速度 vs 成功率"作为显式权衡目标 | 预印本（B 级） | [31] |
| 高效控制架构 | RT-K | 关键点感知（key point-aware）Transformer，追求高效 vision-language 机器人控制 | 期刊（DOI，同行评审状态待核实） | [19] |
| Agent 化 / 工具调用 | ART（Agentic Robot with Tool-use） | 工具注入框架，可为**任意 VLA** 挂载低层视觉、高层 affordance、本体增强等现成工具模块 | 预印本（B 级） | [2] |
| 标准化竞赛评测 | BEHAVIOR Challenge 2025 冠军方案 | 基于 **Pi0.5 架构**做任务适配，在 50 项长时程家务任务（双臂操作+导航+上下文决策）仿真基准中夺冠 | 竞赛结果（C 级：自评+榜单，仿真） | [4] |
| 数据合成 | Gaussian2Sim | 用真实世界 3D Gaussian Splatting 生成 VLA 训练数据 | 预印本（B 级） | [12] |
| 可解释性 / 可控性 | 注意力头用于路径偏差检测；推理时注意力引导 | 主张 VLA **已内含**可用于路径偏差检测的注意力头；对驾驶类 VLA 施加有界加性 pre-softmax 注意力偏置，无需重训即可把注意力导向安全关键目标 | 预印本（B 级） | [5] [1] |
| 安全性 / 鲁棒性 | 部分可观测对抗 patch 攻击 | 首次? 放宽"需完整执行轨迹"的不现实假设，在部分可观测下攻击 VLA（原文措辞："largely unexplored"） | 预印本（B 级） | [17] |
| 表征分析 | Emergent World Representations in OpenVLA | 用实验方法检验策略型 RL 训练的 VLA 是否**隐式学到世界模型** | 预印本（B 级） | [30] |

> **"已验证 vs 仅演示"判定**：[4] 是**仿真基准上的竞赛名次**，属"标准化但非真机"的验证；[14][18] 为**厂商自评+宣称**，属演示级；[1][2][5][8][12][17][19][30][31] 均为 arXiv/期刊单篇声明，**本次检索未命中任何独立第三方复现报告或跨基准榜单交叉验证** → 整体可复现性 `> 待核实`。

### 1.2 经典与奠基性工作（严格区分于上表）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control | 2023 | `> 待核实`（Google DeepMind，据公开信息，未在本次来源中确认） | `> 待核实` | arXiv 预印本，VLA 范式奠基文献（A/B 级） | 高（作为被后续工作反复引用的范式起点） | ★★★★★ | http://arxiv.org/abs/2307.15818v1 | 把 web 知识迁移到机器人控制的原始论文，是"VLA"一词的锚点 [15] |
| Large VLM-based Vision-Language-Action Models for Robotic Manipulation（综述） | 2025 | `> 待核实` | `> 待核实` | arXiv 综述（B 级） | 中 | ★★★★☆ | https://arxiv.org/html/2508.13073v3 | 用于校准"大 VLM 驱动的 VLA"分类骨架 [10] |
| Vision-Language-Action and Vision Language Models for Robot Manipulation: A Comprehensive Review | 2026 | `> 待核实` | `> 待核实` | Preprints.org 预印本（**同行评审状态待核实**） | 低-中（新发布） | ★★★☆☆ | https://doi.org/10.20944/preprints202606.0400.v1 | 面向真实应用的综述，时效最新、权威最低 [11] |
| RT-2: … A Comprehensive Review | 2025 | `> 待核实` | `> 待核实` | 期刊/会议集（AETR），同行评审 `> 待核实` | `> 待核实` | ★★☆☆☆ | https://doi.org/10.56028/aetr.15.1.1423.2025 | **易混淆警示**：这是对 RT-2 的二手综述，不是 RT-2 原文；不可替代 [15] [20] |
| One-Shot Reinforcement Learning for Robot Navigation with Interactive Replay | 2017 | `> 待核实` | `> 待核实` | arXiv 预印本（B 级） | 低（历史价值） | ★★★☆☆ | http://arxiv.org/abs/1711.10137v2 | 样本效率与交互式回放的早期奠基，属"前 VLA 时代"脉络 [13] |
| Grasp and Motion Planning for Dexterous Manipulation（Real Robot Challenge） | 2021 | `> 待核实` | `> 待核实` | arXiv + 竞赛（B/C 级） | 低 | ★★☆☆☆ | http://arxiv.org/abs/2101.02842v1 | 灵巧操作+竞赛评测的早期范式，可对比今日 BEHAVIOR 的评测思路 [9] |

### 1.3 数据集与基准

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| BEHAVIOR Challenge（2025 届） | 2025 | `> 待核实` | `> 待核实` | 大规模基准+竞赛（C 级，摘要可核） | 中（有公开冠军方案） | ★★★★☆ | http://arxiv.org/abs/2512.06951v2 | 50 项长时程家务任务、照片级仿真、需双臂+导航+上下文决策；是本周期少见的**可比**评测 [4] |
| Real Robot Challenge（灵巧操作） | 2021 | `> 待核实` | `> 待核实` | 竞赛（C 级） | 低 | ★★☆☆☆ | http://arxiv.org/abs/2101.02842v1 | 真机/仿真混合竞赛的历史参照 [9] |
| Open X-Embodiment / DROID / LIBERO / SimplerEnv / RoboArena | — | — | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | **本次检索未命中，无可用链接** | 这些跨本体数据集/榜单是判断"可比性"的关键，但本轮召回为空，**结论留白，不得据记忆断言** `> 待核实` |

---

## 2. 工业界与产品（Industry & Product）

**一句话增量判断**：本周期最明确的产业化增量是**大厂以"开源权重 + 真机数据规模"双线争夺 VLA 生态位**，其中 Xiaomi 与 NVIDIA、Hugging Face 形成三种不同开放策略。

- **Xiaomi 双线推进**：Robotics-0 主打**开源 + 实时执行** [18]；Robotics-1 主打 **>100K 小时真机轨迹**与零样本移动操作 [14]。二者构成"开放可用性"与"数据护城河"的分工，属典型的"开源小模型 + 闭源大数据"策略。证据等级 B（厂商技术报告/预印本），真机部署规模 `> 待核实`。
- **NVIDIA GR00T N1**：定位**人形机器人通用基础模型**，标题明示 "Open Foundation Model" [28]。开放权重范围与许可证 `> 待核实`。
- **Hugging Face LeRobot**：定位**端到端机器人学习开源库**，是当前工程落地的事实入口之一 [29]；其 star/下载量/版本迭代速度 `> 待核实`（本轮未采集）。
- **Hugging Face / 社区侧 VLA 复现生态**：OpenVLA 已成为被第三方做表征分析的公共对象 [30]，说明其已具备"可被外部研究者拿来做实验"的开放度；但 OpenVLA 官方仓库链接本次未召回 `> 待核实`。
- **产品化程度判断**：本周期证据全部停留在**研究原型 / 开源权重 / 仿真竞赛**层面，**未命中任何量产量产、客户交付、单位经济性数据** → 商业化拐点 `> 待核实`，不应宣称"已落地"。

### 2.1 开源项目

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| LeRobot | 2026 | `> 待核实`（据公开信息为 Hugging Face，未在本次来源确认） | `> 待核实` | arXiv 预印本（B 级）+ 开源库 | 高（端到端机器人学习的公共基座） | ★★★★★ | http://arxiv.org/abs/2602.22818v1 | 降低 VLA 复现门槛的工程入口 [29] |
| GR00T N1 | 2025 | `> 待核实`（据公开信息为 NVIDIA） | `> 待核实` | arXiv（B 级），标题自称 Open Foundation Model | 高（人形赛道标杆） | ★★★★★ | http://arxiv.org/abs/2503.14734v2 | 人形通用基础模型，开放程度待核实 [28] |
| Xiaomi-Robotics-0 | 2026 | `> 待核实`（小米） | `> 待核实` | arXiv（B 级），标题明示 Open-Sourced | 中 | ★★★★☆ | http://arxiv.org/abs/2602.12684v2 | 开源 + 实时执行，适合做部署侧基线 [18] |
| BLURR | 2025 | `> 待核实` | `> 待核实` | arXiv（B 级） | 低-中 | ★★★☆☆ | http://arxiv.org/abs/2512.11769v1 | 低资源推理；**是否开源代码/权重 `> 待核实`** [8] |
| ART（Agentic Robot with Tool-use） | 2026 | `> 待核实` | `> 待核实` | arXiv（B 级） | 中（工具化方向新） | ★★★★☆ | http://arxiv.org/abs/2608.14047v3 | 工具注入框架，宣称可调任意 VLA；代码开放情况 `> 待核实` [2] |
| OpenVLA（作为被分析对象） | 2025 | `> 待核实` | `> 待核实` | 由第三方论文 [30] 佐证其公开可用 | 中-高 | ★★★★☆ | http://arxiv.org/abs/2509.24559v1 | **注意**：该链接是"分析 OpenVLA"的论文，非 OpenVLA 本体仓库 `> 待核实` [30] |

---

## 3. 蓝海与缺口（Blue Ocean & Gaps）

**一句话增量判断**：方法与数据侧已相当拥挤，**"安全可控 + 边缘部署 + 跨本体可比性"三块几乎无人区**，且本周期出现了明确的"缺口自我暴露"式论文。

1. **VLA 的安全与对抗鲁棒性（最大蓝海）**：原文直言 VLA 的对抗鲁棒性 "largely unexplored"，且既有工作依赖"完整执行轨迹可见"这一不现实假设 [17]。同时 [1][5] 才刚开始讨论"推理时能否不改权重地干预注意力"——意味着 **VLA 缺少运行时护栏（runtime guardrail）**这一整层。推荐度 ★★★★★（[17]）。
2. **VLA 的可解释性与可干预性接口**：[5] 主张注意力头里已存在路径偏差信号，[1] 给出免重训的注意力偏置手段，但两者都未形成通用工具 → **"VLA 调试器/审计器"是空白产品位**。推荐度 ★★★★☆。
3. **低资源 / 边缘侧推理**：[8][31] 把推理成本单列，说明学界开始承认"VLA 跑不动"是首要落地障碍；但**功耗、时延、内存的标准化报告口径尚未建立** `> 待核实`。推荐度 ★★★★☆。
4. **跨本体、跨基准可比性缺口**：本轮唯一命中的可比评测是仿真的 BEHAVIOR [4]；Open X-Embodiment / DROID / LIBERO / SimplerEnv / RoboArena 等**本轮未召回**，无法判断其现状 `> 待核实`。**"真机榜单缺位"是可确证的结构性缺口**（因为 21 条采用证据中无一条提供真机横向对比）。
5. **负面结果与复现研究缺口**：21 条采用证据中**零篇复现报告、零篇 negative results** → 这是本领域方法论层面的蓝海（也是隐患）。`> 待核实`（可能存在于本轮未召回文献）。
6. **仿真→真机的数据合成闭环**：[12] 用 3D Gaussian Splatting 从真实场景生成 VLA 数据，属早期探索，**生成数据的分布偏移与有效性尚无第三方验证** `> 待核实`。
7. **细粒度接触型任务**：装配动作理解因"细微运动 + 精细手-物交互"而困难，需专门微调 VLM [3] → 说明 VLA 在**接触-rich、力觉缺失**场景仍是缺口。推荐度 ★★★☆☆。

---

## 4. 瓶颈与拐点（Bottleneck & Inflection）

**一句话增量判断**：瓶颈已从"模型能力"迁移到**数据规模、推理成本、评测可信度**三处；且出现一个明确拐点信号——**研究重心从"造新 VLA"转向"改造/加速/适配既有 VLA"**。

| 瓶颈 | 具体表现（带证据） | 是否临近拐点 | 拐点信号 |
|---|---|---|---|
| 数据 | 真机轨迹进入 **10^5 小时**量级 [14]，意味着新进入者的数据门槛被抬高；合成数据 [12] 是对冲手段但未验证 | 是（数据获取方式正在分叉） | 若 2027 年出现"合成数据 > 真机数据"的配比报告并被复现，则拐点确认 [P] |
| 推理成本/实时性 | 独立成篇的低资源推理 [8]、实时执行 [18]、微调提速 [31]、高效控制架构 [19] | 是 | 若主流 VLA 论文开始**标配 latency/吞吐表格**（当前仅少数），则拐点确认 [P] |
| 评测可信度 | 只有仿真竞赛级可比结果 [4]；真机横向对比缺位；复现报告为零（本轮） | 未到 | 若 12 个月内出现真机多本体公共榜单，则拐点确认 [P] |
| 安全/鲁棒 | 对抗 patch 可在部分可观测下攻击 VLA [17]；运行时干预手段刚起步 [1][5] | 未到 | 若安全评测进入 BEHAVIOR 类基准的评分项，则拐点确认 [P] |
| 细粒度操作 | 装配类任务需专门 VLM 微调 [3]；力觉/触觉通路在本轮证据中完全缺席 `> 待核实` | 未知 | — |

**结构性拐点判断（较大概率）**：[2][4][8][19][31] 五篇的共同特征是**不提出新基座，而是对既有 VLA 做工具注入、任务适配、推理加速、架构替换**。这说明领域已进入"**基座收敛、适配繁荣**"阶段——与 2023 年 RT-2 [15] 的"范式开创"阶段形成清晰对照。

---

## 5. 社会·政策·国际（Society, Policy & Geopolitics）

**一句话增量判断**：**本周期本次检索未命中任何政策、监管、标准、出口管制或供应链的直接一手证据**，因此本节只做**有限结构推演**，并明确标注不确定性，不填充无源内容。

- **确定（基于已核事实）**：VLA 训练依赖大规模**真实世界轨迹**（Xiaomi-Robotics-1 宣称 >100K 小时 [14]），且多家主体选择**开源权重**（[18][28][29]）。这两点客观构成"数据资产"与"模型权重"两类可监管对象。
- **[P] 推测（置信度：低-中）**：真机轨迹数据的采集涉及隐私与场所授权，一旦规模达到 10^5 小时量级 [14]，**数据合规成本将成为比算力更硬的进入壁垒**。可证伪假设：若到 2027-Q4 出现至少一份针对机器人操作数据的合规/授权框架文件（企业或行业级），则本判断成立。
- **[P] 推测（置信度：低）**：开源权重 [18][28] 的扩散会使"模型出口"成为政策议题。可证伪假设：若 18 个月内出现针对机器人基础模型权重的许可限制条款，则成立。
- **国际格局**：本轮证据中，Xiaomi（[14][18]）、NVIDIA（[28]）、Hugging Face（[29]）代表中美欧三方生态位，但**机构归属均为据公开信息推断，未在本次来源中确认** `> 待核实`。
- **劳动影响 / 伦理**：本轮零证据 → **本周期无显著变化可报告**，不作臆测。

---

## 6. 资本与生态（Capital & Ecosystem）

**一句话增量判断**：**未命中任何融资、并购、估值、人才流动的一手数据**，故资本侧"无显著变化可报告"；但**开源生态的竞争格局变化是可核的**。

- **可核事实**：三个不同量级的主体同时选择开放路线——Hugging Face 以库的形式（LeRobot [29]）、NVIDIA 以基础模型的形式（GR00T N1 [28]）、Xiaomi 以完整 VLA 的形式（Robotics-0 [18]）。**较大概率**：开放权重正从"研究善意"变为"生态位争夺手段"（依据：三者均在标题中显式标注 Open-Sourced / Open Foundation Model / Open-Source Library）。
- **社区活跃度代理指标**：OpenVLA 已被外部团队作为公共研究对象做表征分析 [30]，说明其形成了**可被第三方复用的公共基线**——这是生态成熟的一个可观测信号（较大概率）。
- **竞赛生态**：BEHAVIOR Challenge 2025 产生了公开冠军方案 [4]，说明**竞赛正在承担"临时公共榜单"的职能**，弥补真机榜单缺位。
- **资本数据（融资额、并购、团队流动）**：`> 待核实`（本轮零召回，不编造）。

---

## 7. 信号与预测（Signals & Forecast）

**一句话增量判断**：未来 6–18 个月最值得押注的不是"更强的 VLA"，而是**"让 VLA 可信、可跑、可比"的三类基础设施**。

### 7.1 已观测到的早期信号

| 信号 | 观测依据 | 强度 |
|---|---|---|
| 论文标题从"提出 VLA"转为"适配/加速/攻击/分析 VLA" | [2][4][8][17][19][30][31] 七篇均以既有 VLA 为对象 | 强（可数） |
| 注意力/表征被当作"可利用的现成接口" | [1] 推理时注意力偏置；[5] 注意力头即偏差检测器 | 中 |
| 安全议题从"是否存在"进入"威胁模型细化" | [17] 放弃"完整轨迹可见"的强假设 | 中 |
| 数据来源从"采集"扩展到"生成" | [12] 3DGS 合成 VLA 数据 | 弱-中 |

### 7.2 可证伪预测

- **[P] H1（置信度：中）**：到 2027-Q2，VLA 顶会论文将**普遍报告推理时延/资源占用**。判据：若 CoRL/RSS/ICRA 2027 接收的 VLA 论文中 >50% 含 latency 或吞吐指标，则成立；当前仅 [8][18][19][31] 一小簇关注此问题。
- **[P] H2（置信度：中-低）**：VLA 对抗鲁棒性将在 12 个月内进入标准评测套件。判据：若 BEHAVIOR 或同类基准新增"攻击/扰动"评分项，则成立；依据 [17] 明确指出该方向 "largely unexplored"。
- **[P] H3（置信度：中）**："Agentic / tool-use VLA"将分化为独立子方向。判据：若 2027 年出现 ≥3 篇以"VLA + 外部工具模块"为核心贡献的论文（当前基线为 [2] 一篇），则成立。
- **[P] H4（置信度：中）**：真机数据规模竞赛持续，**10^5 小时**成为新的引用基线。判据：若 ≥2 个团队在 2027 年前公开宣称 ≥100K 小时真机数据（当前基线 [14]），则成立。
- **[P] H5（置信度：高）**：**跨本体真机公共榜单在 18 个月内仍将缺位**。依据：本轮 21 条采用证据中，唯一可比评测为仿真竞赛 [4]，其余均为单模型自评；这是可核的结构性事实。
- **[Debated] 争议点**：VLA 是否隐式学到世界模型尚无共识——[30] 以实验方法提出该问题而非给出定论；同时"扩大真机数据"（[14]）与"用合成数据替代"（[12]）两条路线存在资源分配上的张力，本周期无对比实验可裁决。

### 7.3 Watchlist（持续关注）

1. Xiaomi-Robotics 系列后续是否发布**第三方可复现的评测协议**（[14][18] 目前仅自评）。
2. GR00T N1 的**开放权重范围与实际人形部署案例** [28]。
3. LeRobot 是否成为 VLA 复现的**事实标准**（star/下载/贡献者增速）[29]。
4. 是否出现 **VLA 安全基准**（承接 [17]）。
5. 是否出现**真机多本体公共榜单**（当前最大空白）。
6. 合成数据（[12]）的有效性是否被独立验证。

---

## 参考来源

> 标注 `[噪声]` 者为关键词误召回的跨域条目，**未用于任何论断**；标注 `[易混淆]` 者为标题近似经典工作、易被误引的条目。

1. Inference-Time Attention Steering for Vision-Language-Action Driving Models — http://arxiv.org/abs/2608.17095v1
2. Evolve Vision-Language-Action Model into an Agent with On-the-fly Tool-use — http://arxiv.org/abs/2608.14047v3
3. Compositional Context Fine-Tuning Vision-Language Model for Complex Assembly Action Understanding from Videos — http://arxiv.org/abs/2607.10797v1
4. Task adaptation of Vision-Language-Action model: 1st Place Solution for the 2025 BEHAVIOR Challenge — http://arxiv.org/abs/2512.06951v2
5. Your Vision-Language-Action Model Already Has Attention Heads For Path Deviation Detection — http://arxiv.org/abs/2603.13782v1
6. `[噪声]` JENGA: Exploiting Counter-Based RowHammer Countermeasures to Break Real-Time Predictability — http://arxiv.org/abs/2609.01077v1
7. `[噪声]` VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1
8. BLURR: A Boosted Low-Resource Inference for Vision-Language-Action Models — http://arxiv.org/abs/2512.11769v1
9. Grasp and Motion Planning for Dexterous Manipulation for the Real Robot Challenge — http://arxiv.org/abs/2101.02842v1
10. Large VLM-based Vision-Language-Action Models for Robotic Manipulation — https://arxiv.org/html/2508.13073v3
11. Vision-Language-Action and Vision Language Models for Robot Manipulation: A Comprehensive Review Towards Real-World Applications — https://doi.org/10.20944/preprints202606.0400.v1
12. Gaussian2Sim: Generating Robot Vision-Language-Action Data from Real-World 3D Gaussian Splatting — https://doi.org/10.2139/ssrn.7619747
13. One-Shot Reinforcement Learning for Robot Navigation with Interactive Replay — http://arxiv.org/abs/1711.10137v2
14. Xiaomi-Robotics-1: Scaling Vision-Language-Action Models with over 100K Hours of Real-World Trajectories — http://arxiv.org/abs/2607.15330v2
15. RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control — http://arxiv.org/abs/2307.15818v1
16. `[噪声]` Proceedings of the Dialogue Robot Competition 2023 — http://arxiv.org/abs/2312.14430v5
17. Partially Observable Adversarial Patch Attacks on Vision-Language-Action Models in Robotics — http://arxiv.org/abs/2606.03556v1
18. Xiaomi-Robotics-0: An Open-Sourced Vision-Language-Action Model with Real-Time Execution — http://arxiv.org/abs/2602.12684v2
19. RT-K: A key point-aware transformer framework for efficient vision-language robot control — https://doi.org/10.1016/j.birob.2026.100341
20. `[易混淆]` RT-2: Vision-Language-Action Models for Generalizable Robotic Control: A Comprehensive Review — https://doi.org/10.56028/aetr.15.1.1423.2025
21. `[噪声/易混淆]` RT-Component Object Model in RT-Middleware—Distributed Component Middleware for RT (Robot Technology) — https://doi.org/10.1109/cira.2005.1554319
22. `[噪声]` UIC-AIHealth4All at ArchEHR-QA 2026: Answer-First Evidence Grounding for Clinical Question Answering — http://arxiv.org/abs/2608.27467v1
23. `[噪声]` Second MOASEI Competition at AAMAS'2026: A Technical Report — http://arxiv.org/abs/2607.03399v1
24. `[噪声]` AutoRestTest at the SBFT 2026 Tool Competition — http://arxiv.org/abs/2607.01063v1
25. `[噪声]` Machine learning for the LHC physics program: a 2025-2026 stocktake — http://arxiv.org/abs/2609.32874v1
26. `[噪声]` NTIRE 2026 Rip Current Detection and Segmentation (RipDetSeg) Challenge Report — http://arxiv.org/abs/2604.17070v2
27. `[噪声]` NTIRE 2025 Challenge on Image Super-Resolution (x4): Methods and Results — http://arxiv.org/abs/2504.14582v3
28. GR00T N1: An Open Foundation Model for Generalist Humanoid Robots — http://arxiv.org/abs/2503.14734v2
29. LeRobot: An Open-Source Library for End-to-End Robot Learning — http://arxiv.org/abs/2602.22818v1
30. Emergent World Representations in OpenVLA — http://arxiv.org/abs/2509.24559v1
31. Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success — http://arxiv.org/abs/2502.19645v2
32. `[易混淆]` OpenPI-C: A Better Benchmark and Stronger Baseline for Open-Vocabulary State Tracking — http://arxiv.org/abs/2306.00887v2

---

*Generated by research-bot · topic=`具身智能与视觉-语言-动作vla前沿` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`deepseek-v4-flash` · sources=32 · duration=179s · 2026-10-24T22:13:49+00:00*
