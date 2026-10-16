# 具身智能与视觉-语言-动作（VLA）前沿增量快照（2024-10 → 2026-10）

- **报告日期**：2026-10-16（UTC）
- **领域**：具身智能（Embodied AI）/ 视觉-语言-动作模型（Vision-Language-Action, VLA）/ 机器人学习软件栈（ROS 2、仿真、数据集与基准）
- **检索源数量**：35 条编号来源；其中与主题**直接相关**约 15 条（[1][2][3][4][5][7][8][9][10][11][12][13][15][19][24][26][27][28][29][30][31]），其余为召回噪声（见文末说明）
- **框架**：frontier-watch 七维增量框架（增量优先 / 带日期 / 不确定性外显）
- **证据分级**：A=同行评审论文或官方技术报告；B=arXiv 预印本、官方仓库/数据集主页；C=第三方复现、榜单、权威媒体；D=社区二手解读；E=不可访问
- **标记约定**：`[R]` 传闻待证实；`[P]` 预测（附依据与置信度、写成可证伪假设）；`[Debated]` 存在分歧；`> 待核实` 证据不足

> **数据可得性声明（必读）**：本次抽取结果中 `heat`（citations / GitHub star / 下载量）字段**全部为空**，`authority` 仅保留 arXiv 分类或 DOI 宿主。因此下文"热度证据"栏除个别可自来源文本推断者外一律为 `> 待核实`；**本报告不给出任何引用数、star 数或榜单排名的具体数字**。凡涉及 SOTA 数值比较的表述，均需待榜单/复现报告核实。

> **检索噪声说明**：[6][14][18][20][21][22][23][25][32][33][34][35] 与本主题无实质关联（分别涉及 RowHammer 实时性、医学影像数据集、儒家文本、量子行走、车载边缘计算、电机故障诊断等），说明本次召回管道存在污染；这些来源**未被采信**，也提示后续需对检索式加领域约束（`cs.RO`、`VLA`、`robot manipulation`）。

---

## 1. 进展与热点（Progress & Hotspots）

**一句话增量判断**：过去 24 个月 VLA 的增量**不再主要来自"更大的端到端模型"**，而来自四类工程化/方法化补丁——①推理时干预与可解释诊断、②VLA 智能体化与工具调用、③实时与低资源推理、④后训练与数据规模化（人类视频 / 合成数据）。

### 1.1 关键节点时间线（近 1–2 年，相对 [15][13] 基线）

| 时间 | 名称 | 机构/来源类型 | 相对基线的增量 | 证据等级 | 引用 |
|---|---|---|---|---|---|
| 2023-10 | Open X-Embodiment / RT-X | 跨机构数据集与模型（预印本） | 建立"多本体混合训练"的公共基线与数据聚合范式 | B（venue 待核实） | [15] |
| 2024-03 | DROID | 大规模真实世界操作数据集（预印本） | 把"野外多样性"从仿真推向真机采集 | B | [13] |
| 2025-03 | GR00T N1 | NVIDIA，人形机器人开放基础模型（技术报告/预印本） | 首个明确面向**人形全身**的开放基础模型叙事 | B | [26] |
| 2025-08 | Sim-to-Real 策略评测基准视角 | 预印本（cs.RO） | 指出仿真基准与真机通用策略评测之间存在系统性缺口 | B | [19] |
| 2025-10 | Running VLAs at Real-time Speed | 预印本（cs.RO） | 声称单张消费级 GPU 上实现 pi0 级多视角 VLA 的 30Hz 推理（**自评，未独立复现**） | B | [24] |
| 2025-11 | Isaac Lab | NVIDIA，GPU 并行仿真框架（预印本/官方框架） | 从 Isaac Gym 的单模态并行物理升级为多模态学习基础设施 | B | [27] |
| 2025-12 | BLURR | 预印本（cs.RO） | 面向 VLA 的低资源推理加速 | B | [7] |
| 2025-12 | BEHAVIOR Challenge 2025 第一名方案 | 竞赛方案（预印本） | 把 VLA 从"通用预训练"拉回**长程家务任务适配**，竞赛名次属自评 | B/C | [8] |
| 2025-12 | VLA + 运动图像扩散联合学习 | 预印本（cs.RO） | 把运动表征作为辅助监督信号注入 VLA | B | [31] |
| 2026-02 | LeRobot（工程化论文） | 开源库论文（预印本） | 把端到端机器人学习从论文沉淀为可用库 | B | [28] |
| 2026-06 | 人类视频→机器人操作综述 | Survey（预印本） | 系统化"人类中心数据"作为可扩展监督来源 | B | [5] |
| 2026-06 | VLA/VLM 面向真实应用综述 | Preprint（MDPI Preprints 平台） | 面向落地场景的综合评述，权威性低于同行评审期刊 | B/C（平台待核实） | [9] |
| 2026-08 | ART（VLA + 即时工具使用） | 预印本（cs.RO） | 把 VLA 从"端到端单模型"改写为**可插拔工具调用的智能体** | B | [3] |
| 2026-08 | 推理时注意力引导（驾驶 VLA） | 预印本（cs.CV） | 无需重训即可把注意力重定向到安全关键目标（**自动驾驶域**，可迁移性待验证） | B | [1] |
| 2026-10 | VLA 后训练中的数据增强 | 预印本（cs.RO） | 首次系统讨论"增强怎么做/不该怎么做"的负面结论取向 | B | [30] |

### 1.2 四类增量热点（带四轴证据）

1. **推理时可控性与安全**：无需重训，通过 pre-softmax 加性注意力偏置把 VLA 驾驶模型的注意力转向安全关键参与者 [1]；同时有工作指出 VLA 内部**已经存在**可用于路径偏离检测的注意力头，可作为免训练诊断信号 [4]。这是一个从"提高成功率"转向"运行时可靠性/可解释性"的明确增量。
   - 热度证据：`> 待核实`（无引用数据）｜权威证据：均为 arXiv 预印本（cs.CV / cs.RO），未见同行评审标注 [1][4]｜关注度：`> 待核实`（缺引用/榜单信号）｜推荐度：**★★★★☆**——安全关键推理时干预是 2026 年新出现的接口型问题，值得读，但结论尚属自评。
2. **智能体化与工具使用**：ART 提出工具注入框架，把任意 VLA 改造为可调用现成工具模块（低层视觉、高层可操作 affordance、本体增强）的智能体 [3]。
   - 热度：`> 待核实`｜权威：arXiv cs.RO 预印本，非同行评审 [3]｜关注度：`> 待核实`｜推荐度：**★★★★☆**——"VLA 作为策略"与"VLA 作为智能体"的路线分歧是当前关键争论点。
3. **实时性与资源受限推理**：单卡消费级 GPU 上 30Hz 多视角 VLA 推理 [24]；低资源推理加速方案 BLURR [7]。
   - 热度：`> 待核实`｜权威：arXiv 预印本 [24][7]｜关注度：`> 待核实`｜推荐度：**★★★★☆**——直接决定 VLA 能否上动态任务与边缘硬件，但 [24] 的性能数字为作者自评，**未获独立复现**。
4. **后训练与数据规模化**：后训练数据增强的系统性讨论（含"不该怎么做"）[30]；以人类视频为监督源的规模化路径综述 [5]；由 3D Gaussian Splatting 生成真机风格 VLA 数据 [11]。
   - 热度：`> 待核实`｜权威：[30][5] 为 arXiv 预印本；[11] 为 SSRN 平台预印本，权威性更低 [11][30][5]｜关注度：`> 待核实`｜推荐度：**★★★☆☆（[11]）/ ★★★★☆（[30][5]）**——数据是当前公认瓶颈，[11] 的平台与同行评审状态 `> 待核实`。

### 1.3 经典与奠基性工作（表格）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Open X-Embodiment / RT-X | 2023 | 跨机构合作（21 家机构级合作，具体名单 `> 待核实`） | `> 待核实`（无引用数） | arXiv 预印本 [15]；后续会议收录情况 `> 待核实` | `> 待核实` | ★★★★★ | http://arxiv.org/abs/2310.08864v9 | 多本体数据聚合与"机器人数据规模化"的分水岭，本主题最常被引用的基线 |
| DROID | 2024 | 多机构合作（作者名单 `> 待核实`） | `> 待核实` | arXiv 预印本 [13] | `> 待核实` | ★★★★★ | http://arxiv.org/abs/2403.12945v2 | 真机"野外"大规模操作数据集，定义真机数据多样性口径 |
| Isaac Gym | 2021 | NVIDIA | `> 待核实` | arXiv 预印本/官方框架 [29] | `> 待核实` | ★★★★☆ | http://arxiv.org/abs/2108.10470v2 | GPU 并行仿真奠基工作，VLA 时代仍作为训练基础设施前身被继承 |
| Real Robot Challenge 抓取与运动规划 | 2021 | 竞赛获胜方案（作者 `> 待核实`） | `> 待核实` | arXiv 预印本 [16] | `> 待核实` | ★★★☆☆ | http://arxiv.org/abs/2101.02842v1 | 灵巧操作竞赛的真机闭环代表，作为"评测驱动研究"的历史参照 |
| One-Shot RL for Robot Navigation | 2017 | 作者 `> 待核实` | `> 待核实` | arXiv 预印本 [17] | `> 待核实` | ★★☆☆☆ | http://arxiv.org/abs/1711.10137v2 | 早期交互式回放/单样本 RL，与当前 VLA 仅弱相关，作为历史脉络保留 |
| RT-1 / RT-2 / SayCan / Diffusion Policy / ACT-ALOHA | 2022–2023 | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | **本次检索未取得可引用的来源编号**，按引用纪律不得列出 URL 与结论；这些奠基工作应在补充检索后回填 |

> 引用纪律说明：上表末行的经典工作虽为领域公认奠基作，但**未出现在本次可引用来源清单中**，因此不写链接、不给数字、不下结论，统一标 `> 待核实`，避免编造。

### 1.4 数据集与基准（表格）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明与评测口径 |
|---|---|---|---|---|---|---|---|---|
| Open X-Embodiment | 2023 | 跨机构 | `> 待核实` | 预印本 [15] | `> 待核实` | ★★★★★ | http://arxiv.org/abs/2310.08864v9 | 口径：多本体、多任务混合训练；可比性依赖统一动作/观测空间，细节 `> 待核实` |
| DROID | 2024 | 多机构 | `> 待核实` | 预印本 [13] | `> 待核实` | ★★★★★ | http://arxiv.org/abs/2403.12945v2 | 口径：真机、多环境、真实场景扰动；采集成本是其主要批评点 |
| BEHAVIOR Challenge 2025 | 2025 | 竞赛（第一名方案见 [8]） | `> 待核实` | 竞赛 + 预印本 [8]，竞赛官方榜单 `> 待核实` | 中（依据：存在公开竞赛与多队提交，具体队伍数/榜单 `> 待核实`） | ★★★★☆ | http://arxiv.org/abs/2512.06951v2 | 口径：长程家务任务适配；**名次为参赛者自述，非第三方复现** |
| Sim-to-Real 策略评测基准（方法论） | 2025 | 预印本 [19] | `> 待核实` | 预印本 [19] | `> 待核实` | ★★★★★ | http://arxiv.org/abs/2508.11117v1 | 口径：指出现有仿真基准无法代表真机通用策略能力，是评测可信度问题的关键文献 |
| LIBERO / SimplerEnv / RoboArena / CALVIN | 2023–2025 | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | **本次来源清单中无对应编号**，其成功率口径、任务数与是否真机均需补充检索后填写 |
| Isaac Lab | 2025 | NVIDIA | `> 待核实` | 预印本/官方框架 [27] | `> 待核实` | ★★★★☆ | http://arxiv.org/abs/2511.04831v1 | 作为数据生成与评测的仿真底座；其与真机一致性 `> 待核实` |

---

## 2. 工业界与产品（Industry & Product）

**一句话增量判断**：本周期工业侧可核查的增量集中在**"开放基础模型 + 开源工程栈 + 仿真基础设施"三件套**，而非量产机器人产品；产品化/量产/部署量的直接证据在本轮检索中缺失。

### 2.1 开源项目与工程实践（表格）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| GR00T N1 | 2025 | NVIDIA（预印本自称"open foundation model"） | `> 待核实`（star/权重下载量未知） | 技术报告/预印本 [26]；**权重许可与可获取性 `> 待核实`** | 中（依据：人形基础模型题材 + 厂商主推，但无社区量化信号 → `> 待核实`） | ★★★★☆ | http://arxiv.org/abs/2503.14734v2 | 面向通用人形机器人的开放基础模型叙事，是"人形 = VLA 落地载体"路线的代表 |
| Isaac Lab | 2025 | NVIDIA | `> 待核实` | 官方框架 + 预印本 [27] | 中（依据：被多篇机器人学习工作当作仿真底座使用，量化信号 `> 待核实`） | ★★★★☆ | http://arxiv.org/abs/2511.04831v1 | GPU 并行物理 + 照片级渲染 + 模块化组合，多模态学习基础设施 |
| Isaac Gym | 2021 | NVIDIA | `> 待核实` | 官方框架 + 预印本 [29] | 中（同上，`> 待核实`） | ★★★★☆ | http://arxiv.org/abs/2108.10470v2 | 前代基础设施，仍在大量工作中使用 |
| LeRobot | 2026 | 开源社区库（维护机构 `> 待核实`） | `> 待核实` | 库论文（预印本）[28] | 中（依据：面向端到端机器人学习的开源库定位，社区规模 `> 待核实`） | ★★★★☆ | http://arxiv.org/abs/2602.22818v1 | 降低复现门槛的关键工程载体：遥操作硬件、数据集格式、训练/推理管线 |
| ART（工具注入框架） | 2026 | 预印本 [3] | `> 待核实` | 预印本 [3]，**开源状态 `> 待核实`** | `> 待核实` | ★★★★☆ | http://arxiv.org/abs/2608.14047v3 | 声称可调优任意 VLA 以调用现成工具模块，能否复现取决于代码是否释放 |
| BLURR | 2025 | 预印本 [7] | `> 待核实` | 预印本 [7]，开源状态 `> 待核实` | `> 待核实` | ★★★☆☆ | http://arxiv.org/abs/2512.11769v1 | 面向低资源部署的 VLA 推理优化 |
| openpi / π0（π-zero）生态 | 2025 | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | [24] 提到"pi0 级"性能，但 **π0/openpi 本身未在本次来源清单中**，不得展开 |
| ROS 2 部署链路 | — | — | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | 本轮检索未取得任何 ROS 2 + VLA 部署的一手来源，需专项补检 |

### 2.2 从 lab 走向落地的信号（弱）

- **人形路线**：GR00T N1 把"通用人形机器人基础模型"作为明确产品化方向 [26]；但**真机部署规模、客户、量产数据均无来源支持** `> 待核实`。
- **垂直域外溢**：VLA 架构已被用于**自动驾驶**决策（推理时注意力引导）[1]，说明 VLA 正从操作任务外溢到其他具身决策域；其安全性与车规合规状态 `> 待核实`。
- **工程可复现性**：LeRobot 这类库的存在意味着复现门槛下降 [28]；但"模型权重可用性/许可"在本次来源中均无明确说明 `> 待核实`。

---

## 3. 蓝海与缺口（Blue Ocean & Gaps）

**一句话增量判断**：竞争空白从"谁的模型更大"转移到**"运行时安全、工具化、数据合成与评测可信度"四个新接口**，其中多数方向尚无成熟 benchmark 与独立复现。

| 缺口 | 为什么是蓝海（无人在做的依据） | 现有微弱信号 | 引用 |
|---|---|---|---|
| **VLA 运行时安全与干预接口** | 现有工作只提出"可用注意力头做偏离检测"[4] 与"推理时引导注意力"[1]，**缺少统一 benchmark、失败率口径与真机验证**；两篇均为预印本 | [1][4] | [1][4] |
| **工具/智能体化 VLA 的标准化接口** | ART 提出工具注入，但工具集、调度策略、失败回滚**无共识标准** | [3] | [3] |
| **人类视频→真机策略的可规模迁移** | 综述承认这是可扩展监督来源，但**跨本体运动学对齐、视角/动作空间鸿沟未解** | [5] | [5] |
| **合成数据（3DGS 等）到真机的有效性边界** | 仅有数据生成方法出现，**缺乏第三方对"合成数据训练的策略在真机是否变好"的系统评测** | [11] | [11] |
| **真机泛化与评测可信度** | 已有工作明确指出现有仿真基准无法代表真机通用能力，但**替代性评测协议尚未建立** | [19] | [19] |
| **失败案例与 negative results 的公开机制** | 检索到的均为方法性能宣称；唯一带"不该怎么做"取向的是数据增强后训练讨论 | [30] | [30] |
| **长程任务的评测口径统一** | BEHAVIOR 等竞赛提供了场景，但**名次自述、跨队可比性依赖官方榜单**，本次未能核验榜单 | [8] | [8] |

---

## 4. 瓶颈与拐点（Bottleneck & Inflection）

**一句话增量判断**：瓶颈已从"模型容量"明确迁移到**数据获取成本、推理延迟、评测可信度**三处；其中"实时推理"最接近拐点（已有单卡 30Hz 级宣称，但缺独立复现）。

| 瓶颈 | 现状证据 | 拐点信号（可观测） | 是否临近拐点 |
|---|---|---|---|
| **数据** | 真机数据采集"野外多样性"成本高，是 DROID 类工作的核心挑战 [13]；人类视频被视为可扩展替代，但存在跨本体鸿沟 [5]；合成数据路径刚起步 [11] | 若出现多篇论文在**同一真机任务集**上用纯合成/人类视频数据追平真机采集训练的策略 → 拐点成立 | 推测：**未到**（缺独立对比） |
| **推理延迟** | 单卡消费级 GPU 上 30Hz 多视角 VLA 推理的自评结果 [24]；低资源推理方案 [7] | 若第三方在相同硬件上复现 30Hz 并以真机动态任务（接抛/动态抓取）验证 → 拐点成立 | 较大概率：**接近**（但全部为作者自评） |
| **评测可信度** | 明确指出仿真基准与真机通用策略评测存在系统性落差 [19]；多模态仿真底座快速迭代 [27][29] | 若有独立机构发布真机多本体策略排行榜并被论文普遍引用 → 拐点成立 | 未知：**榜单生态存在性 `> 待核实`** |
| **后训练/OOD 泛化** | VLA 在大视觉域外偏移下仍缺乏泛化，后训练 + RL 的增强策略存在明显"用错会更差"的风险 [30] | 若出现"无真机数据、仅后训练即显著提升 OOD 成功率"的可复现方案 → 拐点成立 | 未知 |
| **知识/算力/人力/成本** | 本轮检索**无可用一手证据**（成本、人力、集群规模） | — | `> 待核实` |

---

## 5. 社会·政策·国际（Society, Policy & Geopolitics）

**一句话增量判断**：**本周期在本次检索范围内无可用证据**——所有已检索来源均为技术论文/框架，未包含任何监管、标准、地缘政治、供应链或劳动影响的直接材料。按研究纪律，本节不作推测性填充。

- 监管与标准（如机器人安全标准、AI 法案对具身系统的适用）：`> 待核实`（本次无来源）
- 出口管制 / 供应链（算力、传感器、减速器）：`> 待核实`（本次无来源）
- 伦理与劳动影响：`> 待核实`（本次无来源）
- 国际竞争格局（中美欧人形机器人路线差异）：`> 待核实`（本次无来源；[26] 仅为厂商技术报告，不构成政策证据 [26]）
- **唯一可提的结构性线索（弱）**：VLA 被引入自动驾驶安全关键决策 [1]，若相关方法进入量产，将自动落入各国自动驾驶功能安全监管框架；但**当前无任何合规证据** `> 待核实`。

> 检索建议：下一轮应以 `policy`、`regulation`、`standard`、`robot safety`、`humanoid national strategy` 等关键词单独拉取官方文件（政府/标准化组织官网），方能填补本维。

---

## 6. 资本与生态（Capital & Ecosystem）

**一句话增量判断**：**本周期在本次检索范围内无可用证据**（无融资、并购、人才流动、市场规模来源）；仅能观察到**厂商主导的开源生态信号**，且这些信号不足以推断资本流向。

- 融资/并购/估值：`> 待核实`（本次无来源）
- 人才流动与团队格局：`> 待核实`（本次无来源）
- 社区与生态（可观测部分）：
  - NVIDIA 系基础设施连续覆盖仿真（Isaac Gym → Isaac Lab）[29][27] 与基础模型（GR00T N1）[26]，形成"仿真 + 预训练模型"的垂直栈；**这是生态位信号，不是资本数据**。
  - 开源库化趋势明显（LeRobot [28]），利于中小团队进入；其社区规模与采用度 `> 待核实`。
  - 学术侧竞赛（BEHAVIOR Challenge [8]）承担了部分"公共评测"职能，替代了缺失的第三方榜单生态 `[Debated]`：竞赛名次可激励进展，但自述名次不等价于独立验证 [8]。

---

## 7. 信号与预测（Signals & Forecast）

**一句话增量判断**：早期信号指向"VLA 从单一大模型走向**可控、可插工具、可实时、可诊断**的系统工程形态"；以下预判均为 `[P]`，附依据链与置信度，并写成**可证伪假设**。

**6–18 个月预判（到 2027-Q4）**

1. `[P]` **推理时安全/可控性会成为独立子领域。**
   - 依据链：已出现无需重训的注意力引导 [1] 与免训练的诊断性注意力头 [4]；两者都指向"不改权重、改运行时"的低成本路径。
   - 可证伪假设：**若到 2027-Q2，仍无 ≥3 篇在真机操作任务上做推理时安全干预并公开失败率的工作（含独立复现），则本判断不成立。**
   - 置信度：中高。
2. `[P]` **"VLA + 工具/智能体"将与"纯端到端 VLA"并存，形成两种架构叙事，但短期不会取代。**
   - 依据链：ART 展示了工具注入的可行性 [3]；同时端到端模型仍在持续演进（多视角实时推理 [24]、运动图像辅助监督 [31]）。
   - 可证伪假设：**若到 2027-Q4 主流真机 benchmark 的前列方案全部为纯端到端、无任何工具调用组件，则本判断不成立。**
   - 置信度：中。
3. `[P]` **实时性将不再是瓶颈叙事，取而代之的是"评测可信度"。**
   - 依据链：单卡 30Hz 级推理已出现宣称 [24] + 低资源优化方案 [7]；而评测缺口已被明确点名 [19]。
   - 可证伪假设：**若到 2027-Q2 出现被多篇论文共同引用、且覆盖 ≥3 种本体的真机策略排行榜，则"评测可信度成为新瓶颈"的判断成立；若无，则说明该缺口仍未被工程界重视。**
   - 置信度：中。
4. `[P]` **数据合成 + 人类视频将成为"预训练"主流，真机数据退居"后训练/对齐"角色。**
   - 依据链：人类中心数据综述 [5]、3DGS 合成数据 [11]、后训练增强方法论 [30] 三条线同时出现。
   - 可证伪假设：**若 2027 年前后发布的新一代开放 VLA 基础模型在方法部分仍以大规模真机采集为主、合成/人类视频仅为辅助，则本判断不成立。**
   - 置信度：中低（[11] 的平台权威性弱，`> 待核实`）。
5. `[P]` **人形全身控制与 VLA 的合流将主要由厂商推动，学术侧独立验证滞后。**
   - 依据链：GR00T N1 为厂商开放基础模型 [26]；仿真栈同样由厂商主导 [27][29]。
   - 可证伪假设：**若到 2027-Q2 出现 ≥2 篇由非厂商团队完成、在第三方人形硬件上复现的人形 VLA 真机结果，则本判断不成立。**
   - 置信度：中。

**Watchlist（建议持续监测）**
- 推理时干预 / 可解释诊断：`attention steering`、`attention head probing`、`runtime safety for VLA` [1][4]
- 工具化与智能体化：`tool-use VLA`、`agentic robot` [3]
- 实时/边缘推理：`real-time VLA inference`、`low-resource VLA` [24][7]
- 数据路径：`human-centric VLA`、`synthetic robot data`、`3DGS-to-robot` [5][11]
- 评测：`sim-to-real policy evaluation`、真机多本体排行榜 [19]
- 生态：`Isaac Lab`、`LeRobot`、`GR00T` 的版本迭代与权重开放策略 [27][28][26]

**本轮明确的证据缺口（须补检）**：①RT-1/RT-2/SayCan/Diffusion Policy/ACT-ALOHA 的一手来源；②LIBERO/SimplerEnv/RoboArena/CALVIN 的评测口径与榜单；③π0/openpi 与 ROS 2 部署链路；④政策、资本、量产部署数据。

---

## 参考来源

**采信来源（与主题相关）**

[1] Inference-Time Attention Steering for Vision-Language-Action Driving Models — http://arxiv.org/abs/2608.17095v1
[2] Compositional Context Fine-Tuning Vision-Language Model for Complex Assembly Action Understanding from Videos — http://arxiv.org/abs/2607.10797v1
[3] Evolve Vision-Language-Action Model into an Agent with On-the-fly Tool-use — http://arxiv.org/abs/2608.14047v3
[4] Your Vision-Language-Action Model Already Has Attention Heads For Path Deviation Detection — http://arxiv.org/abs/2603.13782v1
[5] From Human Videos to Robot Manipulation: A Survey on Scalable Vision-Language-Action Learning with Human-Centric Data — http://arxiv.org/abs/2606.00054v1
[7] BLURR: A Boosted Low-Resource Inference for Vision-Language-Action Models — http://arxiv.org/abs/2512.11769v1
[8] Task adaptation of Vision-Language-Action model: 1st Place Solution for the 2025 BEHAVIOR Challenge — http://arxiv.org/abs/2512.06951v2
[9] Vision-Language-Action and Vision Language Models for Robot Manipulation: A Comprehensive Review Towards Real-World Applications — https://doi.org/10.20944/preprints202606.0400.v1
[10] CLAD: Constrained Latent Action Diffusion for Vision-Language Procedure Planning — https://doi.org/10.1109/ro-man72286.2026.11714614
[11] Gaussian2Sim: Generating Robot Vision-Language-Action Data from Real-World 3D Gaussian Splatting — https://doi.org/10.2139/ssrn.7619747
[12] MiVLA: Towards Generalizable Vision-Language-Action Model with Human-Robot Mutual Imitation Pre-Training — https://doi.org/10.1109/cvprf71909.2026.00152
[13] DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset — http://arxiv.org/abs/2403.12945v2
[15] Open X-Embodiment: Robotic Learning Datasets and RT-X Models — http://arxiv.org/abs/2310.08864v9
[16] Grasp and Motion Planning for Dexterous Manipulation for the Real Robot Challenge — http://arxiv.org/abs/2101.02842v1
[17] One-Shot Reinforcement Learning for Robot Navigation with Interactive Replay — http://arxiv.org/abs/1711.10137v2
[19] Robot Policy Evaluation for Sim-to-Real Transfer: A Benchmarking Perspective — http://arxiv.org/abs/2508.11117v1
[24] Running VLAs at Real-time Speed — http://arxiv.org/abs/2510.26742v1
[26] GR00T N1: An Open Foundation Model for Generalist Humanoid Robots — http://arxiv.org/abs/2503.14734v2
[27] Isaac Lab: A GPU-Accelerated Simulation Framework for Multi-Modal Robot Learning — http://arxiv.org/abs/2511.04831v1
[28] LeRobot: An Open-Source Library for End-to-End Robot Learning — http://arxiv.org/abs/2602.22818v1
[29] Isaac Gym: High Performance GPU-Based Physics Simulation For Robot Learning — http://arxiv.org/abs/2108.10470v2
[30] How (and How Not) to Use Data Augmentation in VLA Post-Training — http://arxiv.org/abs/2610.05994v1
[31] Robotic VLA Benefits from Joint Learning with Motion Image Diffusion — http://arxiv.org/abs/2512.18007v1

**未采信来源（检索噪声，仅登记备查，不用于任何论断）**

[6] JENGA: Exploiting Counter-Based RowHammer Countermeasures to Break Real-Time Predictability — http://arxiv.org/abs/2609.01077v1
[14] The RSNA Abdominal Traumatic Injury CT (RATIC) Dataset — http://arxiv.org/abs/2405.19595v1
[18] The RSNA Intracranial Aneurysm (RSNA-ICA) Dataset — http://arxiv.org/abs/2610.01135v2
[20] A Kinesis-Driven Paradigm: Utilizing The Primal Kinesis Thesis (活论) for Efficient Cross-Cultural AI Translation — https://doi.org/10.2139/ssrn.5650730
[21] 图4.* .dat文件中的"原始"射频数据的存储方案 — https://doi.org/10.17816/dd76511-51555
[22] 原始儒家考述 — https://doi.org/10.24112/sinohumanitas.42333
[23] 原始重力波の検出を目指すサイモンズ天文台 — https://doi.org/10.1038/ndigest.2024.240710
[25] The Synthesis of Optimal Control Laws Using Isaacs' Method for the Solution of Differential Games — http://arxiv.org/abs/2112.10849v2
[32] Real-Time Service Subscription and Adaptive Offloading Control in Vehicular Edge Computing — http://arxiv.org/abs/2512.14002v1
[33] Hierarchical adaptive control for real-time dynamic inference at the edge — http://arxiv.org/abs/2604.26470v1
[34] Real time state monitoring and fault diagnosis system for motor based on LabVIEW — http://arxiv.org/abs/1806.09998v1
[35] Edge-state enhanced transport in a 2-dimensional quantum walk — http://arxiv.org/abs/1411.3958v3

---

*Generated by research-bot · topic=`具身智能与视觉-语言-动作vla前沿` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`deepseek-v4-flash` · sources=35 · duration=232s · 2026-10-16T22:18:36+00:00*
