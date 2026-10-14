# 具身智能与视觉-语言-动作（VLA）前沿调研报告

**日期**：2026-10-14（UTC） ｜ **领域**：Embodied AI / Vision-Language-Action (VLA) / 具身基础模型 ｜ **基线窗口**：2024–2026 ｜ **检索源数量**：36 条候选来源（其中与主题直接相关约 12 条，主题相关但跨域约 4 条，关键词污染/完全无关约 20 条）

> **证据池健康度披露（必须先读）**：本轮证据池存在严重的**关键词污染**——`RT`（Robot Technology）与 `VLA`（Vision-Language-Action）双缩写检索命中了大量无关文献，例如 CORONAS-PHOTON 卫星 RT-2 仪器 [20]、RT-Middleware 组件模型 [21]、Who's Who 人物词条 [22][23][24]、实时系统基准 RT-Bench [17]、钻石开放获取出版政策 [31]、GitHub 赞助 [35][36]、短视频参与度预测挑战 [1]。上述来源**不构成 VLA 领域证据**，本报告仅将其作为"检索噪声"列出，不用于任何结论。此外，本次证据池**完全缺失** Open X-Embodiment、DROID、LIBERO、SimplerEnv、RoboArena 等核心数据集/榜单的一手来源，因此本报告中一切涉及"SOTA 是否被独立验证"的判断均标注 `> 待核实`。以下所有热度数字均来自给定字段，未取到的一律写 `> 待核实`，**无任何编造**。

---

## 1. 进展与热点（Progress & Hotspots）

**一句话增量判断**：相对 2024 年"端到端 VLA 开源基线"阶段，2025–2026 年的增量集中在三处——**推理范式（从文本 CoT 转向可执行/视觉 CoT）**、**小模型化与端侧化**、**新本体（空中机械臂）与无演示适配**；但"SOTA 是否被独立第三方验证"在本轮证据中**无法回答**。

### 1.1 最新进展（近 1–2 年，2025–2026）

| 时间 | 名称 | 增量贡献（相对上一基线） | 证据强度 | 引用 |
|---|---|---|---|---|
| 2025-05 | Impromptu VLA | 在**驾驶域**同时开放权重与开放数据，把"开放"从模型扩展到数据层 | arXiv preprint（自评） | [8] |
| 2025-09 | VLA-Adapter | 面向**tiny-scale（小参数）VLA** 的有效范式，指向端侧/低算力部署 | arXiv preprint | [7] |
| 2025-02 | Fine-Tuning VLA: Optimizing Speed and Success | 把"微调效率 vs 成功率"作为显式优化目标，直指推理延迟瓶颈 | arXiv preprint | [28] |
| 2026-02 | LeRobot | 端到端机器人学习的开源库，工程栈层面论文化 | arXiv preprint | [27] |
| 2026-03 | VLA-Thinker | 提出 **thinking-with-image** 推理，突破"视觉仅作静态上下文"的文本 CoT 范式 | arXiv preprint | [4] |
| 2026-03 | Attention Heads For Path Deviation Detection | 声称 VLA **已内蕴**路径偏差检测注意力头，指向免训练失效检测 | arXiv preprint | [9] |
| 2026-08 | XCoT-VLA | **可执行 Chain-of-Thought**，明确针对自然语言 CoT "开放式、解码昂贵、难优化"的实时控制缺陷 | arXiv preprint | [3] |
| 2026-08 | Inference-Time Attention Steering | 在**推理时**干预注意力，面向驾驶 VLA 的可控性 | arXiv preprint | [5] |
| 2026-08 | RL Bootstrapping of OpenVLA-OFT | 面向**形态差异大的新本体**、无需本体专属演示的适配（以 OpenVLA-OFT 为基座） | arXiv preprint | [26] |
| 2026-09 | AeroManip-VLA | 把 VLA 扩展到**空中机械臂**，用 RL 生成演示解决数据稀缺 | arXiv preprint（最新一条） | [25] |
| 2026 | VLA-Touch | 引入**双层触觉反馈**增强 VLA（IEEE RA-L 关联视频） | 期刊/视频材料 | [10] |
| 2026 | IRL-VLA | 用**奖励世界模型**做 VLA 训练（IRL 路线） | 已投 CVPR 系 venue，具体 track `> 待核实` | [11] |
| 2026 | FAG-VLA | 融合注意力图（fused attention graph）以稳健跟随自然语言指令 | SSRN 工作论文，权威性低 | [12] |
| 2026 | Turkish OpenVLA 评估 | 用**土耳其语**指令评测 OpenVLA，暴露非英语鲁棒性缺口 | 会议论文（SIU 2026） | [34] |
| 2024-09 | RT-1-X → SCARA | 把 RT-1-X 基础模型迁移到 SCARA 机械臂，属跨本体落地工程证据 | arXiv preprint | [16] |

- **推理范式迁移是本周期最明确的增量信号**：文本 CoT 的开放性/解码成本被两份独立工作（[3]、[4]）同时指认为实时控制的障碍，前者给出可执行 CoT，后者给出视觉 CoT，二者路径不同但问题意识一致——构成"同一瓶颈、两种解法"的交叉验证（**去重后仍属同源社区，非独立第三方评测**，故只能算方法层交叉印证）。
- **新本体扩张**：空中机械臂 [25] 与强形态差异机器人 [26] 表明 VLA 正从"固定机械臂"向更宽本体谱系外推。
- **失效检测与可解释性成为独立子方向**：[9] 与 [18]（可解释的机器人行为基础模型）分属两个时间点（2026-03 / 2024-07），显示该议题已持续 2 年。

### 1.2 独立第三方验证 vs 演示/自评（关键缺口）

- 本轮证据池中，**没有任何**榜单排名、第三方复现报告或统一基准对比表的来源。所有 2025–2026 进展均为 arXiv 预印本或会议论文中的**自评数字**。
- 因此：**"哪些 SOTA 变动有独立第三方验证"——`> 待核实`**，需补检 LIBERO / SimplerEnv / RoboArena 等榜单的一手页面。
- 真机部署方面，仅能确认**研究层面的真机/硬件相关工作**存在（ALOHA 2 双臂遥操作硬件 [14]、RT-1-X 迁移到 SCARA 真机 [16]、空中机械臂真机平台 [25]），但**部署规模、量产与现场可靠性数据均无来源支撑** → `> 待核实`。

### 1.3 热度/权威/关注度/推荐度（本节代表条目）

- **VLA-Thinker [4]**：热度 `> 待核实`（未取到引用数/star）｜权威：arXiv preprint，cs.CV，同行评审状态 `> 待核实`｜关注度：中（属 2026 年 VLA 推理范式热点集群，与 [3] 同期同议题）｜推荐度：★★★★★（视觉 CoT 是当前最具范式意义的一支，主题相关度极高）。
- **XCoT-VLA [3]**：热度 `> 待核实`｜权威：arXiv preprint，cs.AI｜关注度：中（可执行 CoT 直接回应实时性痛点）｜推荐度：★★★★★（驾驶域 VLA 推理加速的代表性思路）。
- **AeroManip-VLA [25]**：热度 `> 待核实`｜权威：arXiv preprint，cs.RO｜关注度：中低（新本体方向，2026-09 最新）｜推荐度：★★★★☆（蓝海方向抓手，但尚无第三方复现）。
- **FAG-VLA [12]**：热度 `> 待核实`｜权威：SSRN 工作论文，非同行评审｜关注度：低｜推荐度：★★☆☆☆（仅作线索，须另找高等级来源）。

---

## 2. 工业界与产品（Industry & Product）

**一句话增量判断**：本周期**可核查的厂商产品与量产信号为零**；能观察到的最强"工业侧"信号是**研究机构把工程栈本身产品化并开源**（LeRobot [27]、Octo [13]、OpenVLA [32]、Impromptu VLA [8]）。

- **工程栈开源化**：LeRobot 以"开源库"形式发表 [27]，Octo 定位为开源通用机器人策略 [13]，Impromptu VLA 提供开放权重与开放数据 [8]。三者共同表明**开源工具链/基座已成为研究基础设施**，而非某家厂商的封闭资产。
- **用户点名的 RDT-1B 与 GR00T**：本轮检索到的 36 条来源中**没有任何一条**覆盖 RDT-1B 或 GR00T → `> 待核实`（必须补检其官方仓库与发布博客，否则不得写入结论）。
- **真机落地**：仅有"研究级真机"证据——ALOHA 2 降低双臂遥操作硬件成本与复杂度 [14]、RT-1-X 迁移到 SCARA 工业构型 [16]、空中机械臂平台 [25]。**商业化/量产/客户部署**：`> 待核实`。
- **边缘与成本线**：VLA-Adapter 的 tiny-scale 定位 [7] 与 "speed vs success" 优化 [28] 共同指向**推理成本是产品化前置条件**；但无任何厂商成本/延迟实测数据 → `> 待核实`。
- **安全与合规产品**：[9] 的"免训练路径偏差检测"若成立，是安全关键场景（驾驶/工业）最易产品化的一环；但仅有 arXiv 声明，**无第三方验证** → `> 待核实`。

---

## 3. 蓝海与缺口（Blue Ocean & Gaps）

**一句话增量判断**：缺口高度集中在**"评测与真机可靠性"**与**"新模态/新本体/新语种"**两条线上；前者是基础设施型无人区，后者是增量竞争面。

### 3.1 无人区（基础设施型，高杠杆）

1. **统一口径的真机评测与第三方复现**：证据池中完全没有榜单来源，而 [28] 把"速度与成功率"并列为优化目标，说明评测口径本身尚未收敛。**这是最大的蓝海**——谁定义可比口径，谁掌握话语权。`> 待核实`（需补检 RoboArena / SimplerEnv / LIBERO 一手页面）。
2. **失败与负结果披露**：本轮 36 条来源中**没有任何一篇**报告失败案例或复现困难，全部为方法正向报告 → 结构性缺口。
3. **跨本体"零演示"适配**：[26] 明确把"无本体专属演示"定义为更难设定，说明该问题**刚被提出、尚未拥挤**。
4. **非英语/多语种指令鲁棒性**：[34] 对 OpenVLA 的土耳其语评测是目前唯一的多语种证据点，中文/低资源语种评测基本空白。

### 3.2 增量竞争面（已有玩家但未饱和）

| 缺口方向 | 现有信号 | 缺口在哪 | 引用 |
|---|---|---|---|
| 触觉/力觉融合 | VLA-Touch 双层触觉反馈 | 仅单点工作，缺少统一触觉基准 | [10] |
| 空中/三维操作 | AeroManip-VLA + RL 生成演示 | 数据稀缺、无真机可靠性数据 | [25] |
| 推理时可控性 | attention steering / CoT 改造 | 缺统一"可解释性-性能"权衡指标 | [3][5][9] |
| 端侧小模型 | VLA-Adapter tiny-scale | 缺端侧延迟实测与精度损失曲线 | [7] |
| 视觉前端选择 | 基础模型时代分割综述 | 视觉骨干与动作头的耦合设计无系统结论 | [6] |

- **注意**：上表"缺口在哪"一列属**基于单点证据的推断**，非确证结论，须视为研究方向假设。

---

## 4. 瓶颈与拐点（Bottleneck & Inflection）

**一句话增量判断**：**推理延迟/成本**已从工程细节升级为**范式级矛盾**（文本 CoT 与实时控制不可兼容），这是本周期最清晰的**拐点信号**；**数据与评测**则是尚未见拐点的硬瓶颈。

| 瓶颈 | 证据 | 是否临近拐点 | 拐点信号 |
|---|---|---|---|
| **推理延迟与 CoT 实时性** | [3] 明确指出自然语言 CoT"开放式、解码昂贵、难优化"，不适配实时控制 | **是**（最明确） | 2026 年同时出现可执行 CoT [3]、视觉 CoT [4]、推理时注意力干预 [5] 三条替代路线 |
| **微调效率 vs 成功率权衡** | [28] 将二者作为显式优化目标 | 较大概率 | 若无第三方基准，"拐点"无法量化 `> 待核实` |
| **真机数据成本** | [14] 需专门设计低成本高鲁棒硬件来降低采集门槛 | 否（持续投入型） | 硬件成本下降 [14]、RL 生成演示替代人工 [25] |
| **3D 几何信息缺失** | [15] 指出现有机器人基础模型"仅依赖 2D 图像观测，忽略 3D 几何" | 是（架构层已开始修补） | 3D 基础策略 [15] 出现 |
| **本体泛化** | [26] 强形态差异下假设失效 | 较大概率 | 无演示适配工作出现 [26] |
| **模态缺失（触觉）** | [10] 需显式引入双层触觉反馈 | 早期 | 单点工作 [10] |
| **评测不可比** | 证据池无任何榜单来源 | 否（无信号） | `> 待核实` |
| **算力/模型规模** | [7] 小模型化路线 | 早期 | VLA-Adapter [7] |

- **拐点判读**：把 [3][4][5] 三条 2026 年工作并列看，VLA 的"推理层"正在从"LLM 式长链文本推理"转向"紧凑/可执行/视觉化推理"——这是可观测的**范式切换窗口**，而非单纯效率优化。
- **未形成拐点的部分**：数据规模与评测口径。没有任何来源给出数据量、任务数或榜单名次变化 → 本周期**无显著变化可判**。

---

## 5. 社会·政策·国际（Society, Policy & Geopolitics）

**一句话增量判断**：本周期与 VLA 直接相关的**监管/标准/地缘证据几乎为零**；唯一可核的一手治理信号来自**通用基础模型透明度**而非机器人专项，属间接相关。

- **基础模型透明度治理**：《The 2025 Foundation Model Transparency Index》为**第三版年度评估**，量化基础模型开发者的透明度实践 [2]。这是本证据池中唯一可采信的治理类一手来源，但它**不针对具身智能/机器人**，仅可作为"基础模型监管压力向具身模型外溢"的前提条件 → 关联性 `> 待核实`。
- **开放权重与数据治理**：Impromptu VLA 同时开放权重与数据 [8]，涉及驾驶场景数据合规与再分发许可问题；但该来源**未提供许可条款细节** → `> 待核实`。
- **多语种可用性与语言公平**：[34] 针对土耳其语指令系统性评测 OpenVLA，是目前唯一的多语种社会影响线索，暗示非英语地区部署存在性能落差。
- **出版与科研政策**：[31] 讨论钻石开放获取与欧洲科研政策，属**检索噪声**（与 VLA 无关）；仅可作为"研究成果可及性"的旁证，不用于领域结论。
- **地缘政治、供应链、劳动影响、行业标准（如 ISO/安全认证）**：本轮证据池**无任何来源** → 全部 `> 待核实`，本周期**无显著变化可判**。

---

## 6. 资本与生态（Capital & Ecosystem）

**一句话增量判断**：**融资、并购、人才流动类一手证据为零**；可观测的增量是"开源生态的学术制度化"——工具链与基座开始以论文形式确立引用锚点。

- **生态制度化信号**：开源库/基座被写成正式论文并进入 arXiv（LeRobot [27]、Octo [13]、OpenVLA [32]、Impromptu VLA [8]），意味着生态竞争从"仓库维护"扩展到"可引用性"。
- **被采用度（可核查的弱信号）**：OpenVLA 被后续工作作为基座使用（RL Bootstrapping of **OpenVLA-OFT** [26]），可作为其生态位的一手旁证；但**star 数、下载量、贡献者数均未取到** → `> 待核实`。
- **开源可持续性方法学**：[29] 是 GitHub 开源软件挑战的系统性文献综述，[35][36] 讨论 GitHub 赞助机制。三者**与 VLA 无直接关系**，仅在"如何评估开源项目健康度"这一方法论层面可参考。
- **公司格局变化、投资额、并购**：`> 待核实`（本周期**无显著变化可判**，不得以印象补写）。
- **社区讨论热度**：本轮所有条目的 `heat`/`stars` 字段均为空，唯一带引用数的是 [21]（citations=22），但该文为 2005 年 RT-Middleware，**属噪声**。因此"关注度"判断仅能基于议题聚集度（如三篇同期推理类工作 [3][4][5]）作弱推断。

---

## 7. 信号与预测（Signals & Forecast）

**一句话增量判断**：可观测信号指向"**推理层重构 + 端侧小型化 + 新本体扩张**"三线并进；但所有预测都受制于**评测缺失**这一根本不确定性。

### 7.1 早期信号（已确证事实层）

1. 2026 年出现三种并行的"反文本 CoT"路线：可执行 CoT [3]、视觉 CoT [4]、推理时注意力干预 [5]。
2. 小模型化成为独立议题：VLA-Adapter 明确面向 tiny-scale [7]。
3. 新本体外推：空中机械臂 [25]、强形态差异本体 [26]。
4. 失效检测被论证为"VLA 已内蕴能力" [9]，与可解释性工作 [18] 形成连续议题。
5. 非英语评测出现首个样本 [34]。

### 7.2 可证伪预测（全部标 [P]，附置信度）

- **[P1] 评测标准化将成为 2027 年前最关键的竞争面。** 依据链：证据池无任何榜单来源（缺口）→ 方法论文快速增殖使自评数字不可比 → 社区必然要求统一口径。**可证伪假设**：若至 2027-Q2 仍未出现被 ≥3 个独立团队采用的统一真机 VLA 评测协议，则本预测不成立。**置信度：较大概率。**
- **[P2] 文本 CoT 将在 VLA 控制回路中被系统性淘汰。** 依据：[3] 与 [4] 同时指认其解码成本与开放性问题。**可证伪假设**：若 2027 年前主流 VLA 论文仍以自然语言 CoT 作为默认推理接口，则本预测不成立。**置信度：较大概率。**
- **[P3] 触觉/力觉将从"增强项"变为"标配项"。** 依据：VLA-Touch 已给出双层触觉反馈范式 [10]，但当前仅单点。**可证伪假设**：若 2027 年前未出现 ≥3 篇独立团队的触觉-VLA 工作，则本预测不成立。**置信度：推测。**
- **[P4] 空中/移动操作将形成独立子社区。** 依据：AeroManip-VLA 用 RL 生成演示解决数据瓶颈 [25]，方法可复制性强。**可证伪假设**：若 2027 年前该方向仍只有 ≤2 篇工作，则本预测不成立。**置信度：推测。**
- **[P5] 端侧 VLA 的"精度-延迟"权衡曲线将公开化。** 依据：tiny-scale 范式 [7] 与 speed/success 联合优化 [28] 双向施压。**可证伪假设**：若 2027 年前没有任何工作发布统一硬件上的端侧延迟-成功率曲线，则本预测不成立。**置信度：推测。**
- **[P6] 多语种/跨文化指令鲁棒性会被纳入主流评测。** 依据：[34] 已暴露非英语性能落差。**置信度：未知（需数据）。**

### 7.3 不确定性声明

- 本报告全部预测建立在**无第三方基准来源**的证据池上，[P1]–[P6] 的置信度**可能整体高估**。
- 需优先补检：Open X-Embodiment / DROID / LIBERO / SimplerEnv / RoboArena 一手页面；RDT-1B 与 GR00T 官方仓库；OpenVLA/Octo/LeRobot 的 star 与下载量；各工作的真机任务数与本体数。上述任一项缺失，本报告第 1、2、3 章的对比结论均须降级为 `> 待核实`。

---

## 经典与奠基性工作

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| OpenVLA: An Open-Source Vision-Language-Action Model | 2024 | `> 待核实`（来源未给作者/机构） | `> 待核实` | arXiv preprint（cs.RO），同行评审状态 `> 待核实` | 高（被后续工作作为基座，如 OpenVLA-OFT [26]） | ★★★★★ 开源 VLA 锚点，主题核心 | http://arxiv.org/abs/2406.09246v3 | 开源 VLA 基座 [32] |
| Octo: An Open-Source Generalist Robot Policy | 2024 | `> 待核实` | `> 待核实` | arXiv preprint（cs.RO） | 中高（开源通用策略基线） | ★★★★★ 通用策略开源代表作 | http://arxiv.org/abs/2405.12213v2 | 强调少样本微调与广泛化 [13] |
| ALOHA 2: Enhanced Low-Cost Hardware for Bimanual Teleoperation | 2024 | `> 待核实` | `> 待核实` | arXiv preprint（cs.RO） | 中高（双臂数据采集硬件事实标准之一） | ★★★★★ 数据供给侧奠基工作 | http://arxiv.org/abs/2405.02292v1 | 降低双臂遥操作成本与门槛 [14] |
| Diffusion Co-Policy for Synergistic Human-Robot Collaborative Tasks | 2023 | `> 待核实` | `> 待核实` | arXiv preprint（v4） | 中（扩散策略用于人机协作） | ★★★★☆ 扩散策略谱系参考 | http://arxiv.org/abs/2305.12171v4 | 协作任务扩散共策略 [19] |
| High-level robot programming based on CAD | 2013 | `> 待核实` | `> 待核实` | arXiv preprint | 低（历史文献） | ★★☆☆☆ 仅作"模块化→端到端"脉络注脚 | http://arxiv.org/abs/1309.2086v1 | 模块化/几何规划时代代表 [33] |
| Towards Interpretable Foundation Models of Robot Behavior | 2024 | `> 待核实` | `> 待核实` | arXiv preprint | 低中（可解释性小众议题） | ★★★☆☆ 可解释性脉络起点 | http://arxiv.org/abs/2407.08065v1 | 任务特定策略生成以提升可解释性 [18] |
| Robot Learning: A Tutorial | 2025 | `> 待核实` | `> 待核实` | arXiv preprint | 中（教程类高查阅） | ★★★★☆ 入门与术语对齐 | http://arxiv.org/abs/2510.12403v1 | 机器人学习系统性教程 [30] |
| RT-1-X Foundation Model on a SCARA robot | 2024 | `> 待核实` | `> 待核实` | arXiv preprint | 低（工程迁移案例） | ★★★☆☆ 跨本体落地证据点 | http://arxiv.org/abs/2409.03299v1 | 基础模型迁移到工业构型 [16] |

> 说明：经典谱系中更早的 RT-1/RT-2、Diffusion Policy、ACT、π0 等**在本证据池中无任何来源**，故不列入表格，避免编造。`> 待核实`。

## 开源项目

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| LeRobot | 2026 | `> 待核实` | `> 待核实`（star/下载未取到） | arXiv preprint（cs.RO） | 高（端到端机器人学习工具链） | ★★★★★ 工程栈首选参考 | http://arxiv.org/abs/2602.22818v1 | 开源库，含遥操作与学习流程 [27] |
| OpenVLA | 2024 | `> 待核实` | `> 待核实` | arXiv preprint | 高 | ★★★★★ 开源 VLA 基座 | http://arxiv.org/abs/2406.09246v3 | 被 [26] 作为微调/RL 基座 | 
| Octo | 2024 | `> 待核实` | `> 待核实` | arXiv preprint | 中高 | ★★★★★ 通用策略开源 | http://arxiv.org/abs/2405.12213v2 | 跨本体开源策略 [13] |
| Impromptu VLA | 2025 | `> 待核实` | `> 待核实` | arXiv preprint | 中（驾驶域） | ★★★★☆ 少见的"权重+数据"双开放 | http://arxiv.org/abs/2505.23757v1 | 驾驶 VLA 开放权重与数据 [8] |
| RDT-1B | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | **本证据池无来源，须补检官方仓库** |
| GR00T | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | **本证据池无来源，须补检官方发布页** |

## 数据集与基准

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Open X-Embodiment | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | **本轮未检索到一手来源** |
| DROID | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | **本轮未检索到一手来源** |
| LIBERO | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | **本轮未检索到一手来源** |
| SimplerEnv | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | **本轮未检索到一手来源** |
| RoboArena | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | **本轮未检索到一手来源** |
| Impromptu VLA 开放数据 | 2025 | `> 待核实` | `> 待核实` | arXiv preprint | 中 | ★★★★☆ 驾驶域开放数据 | http://arxiv.org/abs/2505.23757v1 | 唯一可确认的"开放数据"声明 [8] |
| ALOHA 2 双臂遥操作数据/硬件 | 2024 | `> 待核实` | `> 待核实` | arXiv preprint | 中高 | ★★★★★ 数据采集底座 | http://arxiv.org/abs/2405.02292v1 | 硬件可用性提升数据规模上限 [14] |
| RT-Bench（实时系统基准） | 2022 | `> 待核实` | `> 待核实` | arXiv preprint | 低 | ★☆☆☆☆ **噪声，非机器人学习基准** | http://arxiv.org/abs/2203.11423v2 | "RT" 关键词误匹配 [17] |

---

## 参考来源

> 标注 **[采信]** 者为正文实际引用的证据；**[噪声]** 者经核查与 VLA/具身智能主题无关（多为 "RT"/"VLA"/"Foundation" 缩写误匹配），仅存档以证检索可追溯性，不用于任何结论。

1. **[噪声]** VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1 （短视频参与度预测，非机器人）
2. **[采信]** The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1
3. **[采信]** XCoT-VLA: Executable Chain-of-Thought for Vision-Language-Action Driving — http://arxiv.org/abs/2608.10976v1
4. **[采信]** VLA-Thinker: Boosting Vision-Language-Action Models through Thinking-with-Image Reasoning — http://arxiv.org/abs/2603.14523v1
5. **[采信]** Inference-Time Attention Steering for Vision-Language-Action Driving Models — http://arxiv.org/abs/2608.17095v1
6. **[采信]** Image Segmentation in Foundation Model Era: A Survey — http://arxiv.org/abs/2408.12957v3
7. **[采信]** VLA-Adapter: An Effective Paradigm for Tiny-Scale Vision-Language-Action Model — http://arxiv.org/abs/2509.09372v2
8. **[采信]** Impromptu VLA: Open Weights and Open Data for Driving Vision-Language-Action Models — http://arxiv.org/abs/2505.23757v1
9. **[采信]** Your Vision-Language-Action Model Already Has Attention Heads For Path Deviation Detection — http://arxiv.org/abs/2603.13782v1
10. **[采信]** VLA-Touch: Enhancing Vision-Language-Action Model with Dual-Level Tactile Feedback_supp1-3692345.mp4 — https://doi.org/10.1109/lra.2026.3692345/mm1
11. **[采信]** IRL-VLA: Vision-Language-Action Training via Reward World Model — https://doi.org/10.1109/cvprf71909.2026.00098
12. **[采信]** FAG-VLA: Vision-Language-Action Model With Fused Attention Graph for Robustly Following Natural-Language Instructions — https://doi.org/10.2139/ssrn.7417887
13. **[采信]** Octo: An Open-Source Generalist Robot Policy — http://arxiv.org/abs/2405.12213v2
14. **[采信]** ALOHA 2: An Enhanced Low-Cost Hardware for Bimanual Teleoperation — http://arxiv.org/abs/2405.02292v1
15. **[采信]** FP3: A 3D Foundation Policy for Robotic Manipulation — http://arxiv.org/abs/2503.08950v1
16. **[采信]** Bringing the RT-1-X Foundation Model to a SCARA robot — http://arxiv.org/abs/2409.03299v1
17. **[噪声]** RT-Bench: an Extensible Benchmark Framework for the Analysis and Management of Real-Time Applications — http://arxiv.org/abs/2203.11423v2 （实时系统，非机器人学习）
18. **[采信]** Towards Interpretable Foundation Models of Robot Behavior: A Task Specific Policy Generation Approach — http://arxiv.org/abs/2407.08065v1
19. **[采信]** Diffusion Co-Policy for Synergistic Human-Robot Collaborative Tasks — http://arxiv.org/abs/2305.12171v4
20. **[噪声]** Instruments of RT-2 Experiment onboard CORONAS-PHOTON … — http://arxiv.org/abs/1011.3326v1 （卫星仪器，"RT" 误匹配）
21. **[噪声]** RT-Component Object Model in RT-Middleware—Distributed Component Middleware for RT (Robot Technology) — https://doi.org/10.1109/cira.2005.1554319 （2005 年中间件，heat: citations=22，与 VLA 无关）
22. **[噪声]** Bruce, Rt Hon. Sir Gainsford … — https://doi.org/10.1093/ww/9780199540884.013.u184184 （人物词条）
23. **[噪声]** Sinclair, Rt Hon. Ian (McCahon) … — https://doi.org/10.1093/ww/9780199540884.013.u34987 （人物词条）
24. **[噪声]** Sinclair, Rt Hon. Ian (Mccahon) … — https://doi.org/10.1093/ww/9780199540884.013.34987 （人物词条，与 [23] 重复）
25. **[采信]** AeroManip-VLA: Scalable Vision-Language-Action Learning for Aerial Manipulation with RL-Generated Demonstrations — http://arxiv.org/abs/2609.36915v1
26. **[采信]** RL Bootstrapping of OpenVLA-OFT for a Novel Robot Embodiment — http://arxiv.org/abs/2608.01013v1
27. **[采信]** LeRobot: An Open-Source Library for End-to-End Robot Learning — http://arxiv.org/abs/2602.22818v1
28. **[采信]** Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success — http://arxiv.org/abs/2502.19645v2
29. **[弱相关/方法论]** Open Source Software Development Challenges: A Systematic Literature Review on GitHub — http://arxiv.org/abs/2003.10750v3
30. **[采信]** Robot Learning: A Tutorial — http://arxiv.org/abs/2510.12403v1
31. **[噪声]** Research on Diamond Open Access in the Long Shadow of Science Policy — http://arxiv.org/abs/2511.22965v1 （出版政策）
32. **[采信]** OpenVLA: An Open-Source Vision-Language-Action Model — http://arxiv.org/abs/2406.09246v3
33. **[采信（历史脉络）]** High-level robot programming based on CAD: dealing with unpredictable environments — http://arxiv.org/abs/1309.2086v1
34. **[采信]** Performance Analysis of Vision-Language-Action Models: Evaluating Turkish Command Understanding in OpenVLA — https://doi.org/10.1109/siu71813.2026.11636432
35. **[弱相关/方法论]** Support open source software as a GitHub sponsor — https://doi.org/10.53731/r8n4c91-97aq74v-ag6v9
36. **[弱相关/方法论]** Support open source software as a GitHub sponsor — https://doi.org/10.53731/y79qt-zf894

**未获来源、必须补检的关键项（不得凭记忆填写）**：Open X-Embodiment、DROID、LIBERO、SimplerEnv、RoboArena 一手页面；RDT-1B 与 GR00T 官方仓库/发布博客；OpenVLA / Octo / LeRobot 的 GitHub star 与 HuggingFace 下载量；各方法在真机上的任务数、本体数与独立复现报告。上述任一项补齐前，本报告第 1–4 章的相关对比结论应视为 `> 待核实`。

---

*Generated by research-bot · topic=`具身智能与视觉-语言-动作vla前沿` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`deepseek-v4-flash` · sources=36 · duration=194s · 2026-10-14T22:17:44+00:00*
