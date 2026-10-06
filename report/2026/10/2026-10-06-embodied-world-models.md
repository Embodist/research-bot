# 具身智能 · 世界模型与仿真（World Models & Simulation）调研报告

**日期**：2026-10-06（UTC） | **领域**：具身智能 / 世界模型 / 仿真 / sim2real | **可引用检索源**：151 条（编号 [1]–[151]） | **方法论**：deep-research 四阶段 + frontier-tracking + paper-survey + evidence-grading

---

## 摘要（Executive Summary）

- **生成式/视频世界模型正从"演示"走向"评估基础设施"**：WorldGym 把动作条件自回归视频生成模型当作策略评估环境，声称其内部成功率与真机成功率高度相关并能保持策略排序 [52]；Genie Envisioner 试图把策略学习、评估与仿真统一进单一视频生成框架（GE-Base 为指令条件视频扩散模型）[60]。这两条构成本轮证据中最接近"可验证机器人决策"的一手材料。
- **核心瓶颈被明确指认为"物理 grounding / 几何一致性"**：GEM-4D 指出视频世界模型常无法跨时间一致跟踪同一物理点，生成视频"看起来合理"但缺乏可靠动作执行所需的物理接地 [36]；Causal Physics Steering 进一步尝试在推理期干预模型的物理预期 [117]。
- **基准生态呈现"LIBERO 家族化 + 自我批判"两条线**：LIBERO 仍是 VLA 评测主力 [140]，但同时出现 LIBERO-PRO 对 LIBERO 训练/评测设置导致"性能虚高、无法公平比较"的系统性质疑 [144]，以及 VPro / Para / Safety / RECOVER 等诊断性子基准 [31][32][138][143]。
- **明显的证据缺口（必须标注）**：域随机化（domain randomization）、real2sim 系统辨识（system identification）、real2sim2real 闭环流水线，在本轮候选中**没有任何专门来源** > 待核实；神经仿真与可微引擎的**可比吞吐量/梯度正确性数据**同样缺失 > 待核实；WorldModelBench、SimplerEnv、RoboCasa 的专门文献在本轮候选中缺失 > 待核实。
- **争议主线**：世界模型能否**提升**（而非仅**评估**）控制性能，目前缺少闭环真机成功率一手证据 > 待核实；同时"仿真基准 SOTA ≠ 真机 SOTA"的评估方法论问题被持续提出 [30][91]。

---

## 一、关键前沿进展（近 1–2 年）

| 进展 | 时间 | 机构/团队（据候选块） | 一句话贡献 | 证据强度 | 引用 |
|---|---|---|---|---|---|
| WorldGym | 2025（v1 2025-05-31） | 作者含 Percy Liang、Sherry Yang | 用动作条件视频世界模型做策略评估环境，报告与真机相关性及排序保持 | arXiv 预印本（cs.RO），未标注会议 | [52] |
| GEM-4D | 2026（v1 2026-05-20） | 作者含 Yilun Du、Zhuang Liu、Paul Pu Liang | 用几何基础模型蒸馏的稠密 4D 对应监督弥补视频世界模型物理接地缺失 | arXiv 预印本（cs.CV） | [36] |
| Genie Envisioner | 2025 | 候选块未提供 | 统一世界基础平台，video-generative 框架内集成策略/评估/仿真 | arXiv 预印本（cs.RO） | [60] |
| PolaRiS | 2025 | 候选块未提供 | 可扩展 real-to-sim 评估，缓解真机 rollout 的随机性与耗时问题 | 热度：citations=39；venue 标为 "Robotics" | [91] |
| LIBERO-PRO | 2025 | 候选块未提供 | 揭示 LIBERO 训练/评测设置导致性能虚高、阻碍公平比较 | 热度：citations=177（本轮候选中最高） | [144] |
| Isaac Lab | 2025 | NVIDIA（据候选块标题/摘要口径） | 继承 Isaac Gym，把 GPU 原生仿真扩展到多模态大规模学习 | arXiv 预印本（cs.RO） | [114] |
| What-If World | 2026 | 候选块未提供 | 面向具身场景的因果世界模型基准：不是"视频像不像"，而是"输入变了输出是否跟着变" | arXiv 预印本（cs.CV） | [37] |
| Cosmos 系列（WFM / Transfer1 / Cosmos 3） | 2025–2026 | NVIDIA（据候选块标题口径） | 面向 Physical AI 的世界基础模型与可控多模态条件生成 | arXiv 预印本（cs.CV/cs.RO 未逐条标注） | [122][123][125][126] |

- **判读**：真正把世界模型接入**策略决策/评估闭环**的，本轮候选中主要是 WorldGym [52]、Genie Envisioner [60]、Cosmos-Surg-dVRK [124]；其余多停留在生成质量层面。
- 四类证据（以 WorldGym 为例）：**热度**：候选块未提供引用数/star/下载/榜单 > 待核实 [52]；**权威**：arXiv (cs.RO) 预印本，未标注同行评审 venue [52]；**关注度**：中——作者团队在具身/世界模型方向可见度高、问题定位直击评测痛点，但缺量化信号 [52]；**推荐度**：★★★★☆——最直接回答"世界模型能否成为可验证决策依据"，但相关性数字需核实任务数与真机硬件 [52]。

---

## 二、生成式/视频世界模型

**2.1 从"生成未来"到"评估策略"**

- WorldGym 的定位是 **action-conditioned autoregressive video generation model 作为真实环境代理**，策略通过世界模型内 Monte Carlo rollouts 由 VLM 给奖励，并用仅来自真机的初始帧评估一组 VLA 真机策略；论文声称 world-model 内成功率与真机成功率高度相关，且跨 policy versions / sizes / checkpoints 保持相对排序 [52]。
  - **热度**：> 待核实（候选块无引用数/star/榜单）[52]
  - **权威**：arXiv:2506.00613v3 (cs.RO)，未标注会议/同行评审 [52]
  - **关注度**：中——问题定位（真机评测贵、手工仿真器难维护）为领域共识痛点 [52]
  - **推荐度**：★★★★☆——子问题核心证据，但"高度相关"的具体口径需抓全文核对 [52]

**2.2 物理合理性与几何 grounding 是公认短板**

- GEM-4D：视频世界模型"常无法一致跟踪同一物理点"，导致**看似合理却缺少可靠动作执行的物理接地**；其方案是向视频生成主干注入稠密 4D 对应监督（蒸馏自预训练几何基础模型），并保持 single-stream 架构、无额外推理开销 [36]。
  - **热度**：> 待核实 [36]；**权威**：arXiv:2605.22882v4 (cs.CV) 预印本 [36]；**关注度**：中——精准切中"生成视频不可作为可靠动作依据"这一核心缺陷 [36]；**推荐度**：★★★★☆——代表"生成式世界模型走向可执行"的关键技术路线 [36]。
- Causal Physics Steering：尝试用概念激活向量在推理期控制视频世界模型的物理预期，提及 VideoMAE 中层的 "Physics Emergence Zone (PEZ)" [117]。
  - **热度**：> 待核实 [117]；**权威**：arXiv:2605.24322v1 (cs.CV) 预印本 [117]；**关注度**：中——可解释性 × 物理可控性的交叉点 [117]；**推荐度**：★★★☆☆——方法有趣但下游真机决策收益未在候选块中给出 [117]。

**2.3 平台化与综述化**

- Genie 系：Genie 2024 提出 generative interactive environments [62]；Genie Envisioner 2025 进一步做成"统一世界基础平台"，GE-Base 为指令条件视频扩散模型，集成策略学习/评估/仿真 [60]。
- Cosmos 生态：World Foundation Model Platform for Physical AI [122]、Cosmos-Transfer1 的自适应多模态条件生成 [123]、视频基础模型的 world simulation [125]、Cosmos 3 的 omnimodal world models [126]；医疗机器人方向的在线策略评估应用 Cosmos-Surg-dVRK [124]。
- 综述与批判：Towards Interactive Video World Modeling 系统梳理前沿、挑战与基准 [118]；Sora as a World Model? 对 T2V 生成作为世界模型的综述 [42]；Learning Embodied Intelligence from Physical Simulators and World Models 综述仿真与世界模型的结合 [57]。
- 推理期与轻量化：Grounding Video Reasoning in Physical Signals [129]、Nano World Models（最小化未来视频预测实现）[40]。

> **缺口**：本轮候选中**未出现** Genie 系列、Cosmos、GAIA-2 [128] 在**第三方基准榜单**上的独立评测结果，绝大多数证据为**作者自述**。因此"是否已被第三方验证"这一问题 > 待核实。

---

## 三、神经仿真与可微物理

**3.1 神经/学习型仿真器**

- GNS（Graph Neural Network-based simulator）面向颗粒与流体建模的**可泛化**神经仿真器 [23]，是本轮候选中少见的"神经代理模型替代数值求解器"证据。
  - **热度**：> 待核实 [23]；**权威**：arXiv:2211.10228v1 预印本 [23]；**关注度**：低—中；**推荐度**：★★★☆☆——与"神经仿真替代物理引擎"主题相关，但年份较早（2022），且不在机器人操作域 [23]。
- **结论性判断**：本轮候选**无法**回答"神经仿真如何替代/增强传统物理引擎"的保真度、可扩展性与收敛性证据 > 待核实。

**3.2 可微物理引擎**

- Dojo：面向机器人的可微物理引擎 [94] —— 是可微仿真路线的经典工程锚点。
  - **热度**：> 待核实 [94]；**权威**：arXiv:2203.00806 预印本 [94]；**关注度**：中（可微仿真长期议题）[94]；**推荐度**：★★★★☆——选型时必读的可微引擎代表工作，但性能数字需另行核实 [94]。
- Guiding Evolutionary Strategies by Differentiable Robot Simulators [45]：说明可微仿真在**梯度引导搜索**中的实际用法。
- Isaac Gym [116] → Isaac Lab [114]：GPU 原生并行仿真的代际演进，Isaac Lab 强调 GPU 并行物理 + 真实感渲染 + 模块化可组合架构，面向大规模多模态学习 [114]。
  - **热度**：> 待核实 [114][116]；**权威**：arXiv 预印本（cs.RO）[114][116]；**关注度**：中—高（生态与工程采用度需以 GitHub star 核实）> 待核实；**推荐度**：★★★★★（工程选型）——GPU 并行仿真是当前大规模机器人学习的事实基础设施 [114][116]。
- 闭合运动链支持不足的问题被指出：多数 RL 框架因**仿真器对闭合运动链支持有限**，无法建模并联驱动中的机械智能，可能带来不准确 [100]。
  - **权威**：arXiv:2507.00273v3 (cs.RO) [100]；**关注度**：中；**推荐度**：★★★☆☆——提示"引擎能力边界"这一选型关键点 [100]。

> **待核实（重要）**：MJX / Warp / Brax / Genesis 的**同任务同硬件吞吐量、梯度正确性、接触稳定性**可比数据，在本轮候选中**完全没有**可用来源。Genesis 仅以种子项目形式存在（见第六节），其性能宣称需回到官方仓库与实测报告核实。

---

## 四、sim2real 迁移与方法

**4.1 经典议题与立场性文献**

- R:SS 2020 Workshop 总结：为 sim2real 迁移提供问题框架与社区共识背景 [77]。
- 精农业机器人操作的 sim2real 局限：明确讨论"重要性"与"局限性"两面 [74]。
- 视觉编码器预训练以桥接 sim2real gap（visuomotor policy transfer）[76]。
- 音频-视觉导航的 sim2real 迁移（频率自适应声场预测）[75]；生成式音频用于多模态 sim2real 策略学习 [44]——说明 sim2real 已从视觉扩展到**多模态**。
  - 上述各条：**热度** > 待核实；**权威**：arXiv 预印本 [44][74][75][76][77]；**关注度**：低—中；**推荐度**：★★★☆☆（背景与方法参考）。

**4.2 人形机器人 real-world RL 与 sim2real**

- Real-World Humanoid Locomotion with RL [89]、Learning Sim-to-Real Humanoid Locomotion in 15 Minutes [90]、Sim-to-Real Transfer in Deep RL for Bipedal Locomotion [88]：构成"从仿真到真机行走"的证据簇。
  - **权威**：arXiv 预印本（其中 [89] 为 2303.03381v2）[88][89][90]；**热度**：> 待核实 [88][89][90]；**关注度**：中—高（人形 sim2real 是热点）> 部分待核实；**推荐度**：★★★★☆——[90] 的"15 分钟"宣称属强口径，需核实任务与硬件 [90]。
- Robot Trains Robot：指出**从零开始的直接真机 RL 或从预训练策略自适应仍属罕见**，并强调真机学习面临安全性、奖励设计与学习效率挑战 [47]。
  - **权威**：arXiv:2508.12252v2 (cs.RO) [47]；**热度**：> 待核实 [47]；**关注度**：低（与生成式世界模型主题相关性弱）[47]；**推荐度**：★★☆☆☆（仅作"真机学习仍困难"的背景佐证）[47]。

**4.3 单一 sim2real 量化数据点（需谨慎）**

- Robot Manipulation with GPT-6-Astra：在 XLeRobot 上做电梯按钮任务，30 次固定起点仿真试验中，提供完整机器人几何与相机信息使平均完成时间相对基线下降 **57.4%**，提供与动作/状态同步的图像下降 **68.6%**；真机侧仅报告 9 组配对比较（起点偏移 10–100 cm）[79]。
  - **热度**：> 待核实（候选块无引用数/star/榜单）[79]
  - **权威**：arXiv:2609.31770v1 (cs.RO) 预印本，**未见同行评审 venue**；作者含 Lingxi Xie、Qi Tian 等 [79]
  - **关注度**：低——单任务单本体，无社区量化信号 [79]
  - **推荐度**：★★☆☆☆——可作"先验本体知识 + 经验复用辅助 sim2real"的线索，但**全部量化结果均来自仿真**，真机无成功率/落差指标 [79]
  > **待核实**：真机成功率、迁移前后性能落差、失败率均未在候选块中提供 [79]。

**4.4 三条经典路线的证据状态**

| 方法路线 | 解决什么 | 本轮证据状态 |
|---|---|---|
| 域随机化 domain randomization | 用参数/视觉分布扰动提升策略鲁棒性 | **无专门来源** > 待核实 |
| real2sim 系统辨识 system identification | 标定质量/摩擦/延迟/接触模型以缩小差距 | **无专门来源**；仅 PolaRiS 从 real-to-sim 评估角度间接相关 [91] > 待核实 |
| real2sim2real 闭环 | 真机数据回传→再校准→再训练 | **无完整案例、无迭代次数/收敛判据** > 待核实 |

---

## 五、仿真引擎与基准

**5.1 仿真引擎与平台**

- GPU 并行：Isaac Gym [116] → Isaac Lab [114]；ManiSkill3 提供 GPU 并行仿真与渲染以支撑可泛化具身 AI [136]。
- 可微：Dojo [94]；可微仿真引导进化策略 [45]。
- 经典通用：MuJoCo（种子资源，见第六节表格）；RoboCasa / BEHAVIOR-1K 作为场景级基准 [35]。
- 评测基础设施：PolaRiS 提供可扩展 real-to-sim 评估，直接针对真机 rollout 的随机性、可复现性与耗时问题 [91]（citations=39 [91]）。
- 辅助 RL 测试床：Assistax（多智能体、硬件加速、辅助机器人）[103]（citations=0 [103]）。

**5.2 基准与评测口径**

- LIBERO 及其诊断扩展生态：LIBERO 原始（lifelong robot learning 知识迁移）[140]；LIBERO-PRO（记忆化与公平性）[144]；LIBERO-VPro（闭环视觉鲁棒性）[31]；LIBERO-Para（指令改写鲁棒性）[32]；LIBERO-Safety（物理与语义安全）[138]；LIBERO-RECOVER（失败恢复）[143]。
- 具身活动级：BEHAVIOR-1K（1000 项日常活动 + 真实感仿真）[35]。
- 双臂与触觉：RoboTwin 双臂协作挑战赛（CVPR 2025 MEIS Workshop）[16]；ManiSkill-ViTac 2025（视觉 + 触觉操作技能）[17]。
- 世界模型专项：What-If World（因果性而非画质）[37]；PhysicsBench（面向工程设计与仿真的生成/预测模型统一榜单）[133]。

| 基准 | 测什么（据候选块） | 仿真/真机口径 | 可比性关键风险 | 引用 |
|---|---|---|---|---|
| LIBERO | VLA 终身学习/知识迁移 | 仿真 | 训练/评测设置可能导致性能虚高 | [140][144] |
| LIBERO-PRO | 抗记忆化、公平比较 | 仿真 | 与原生 LIBERO 分数不可直接横向比 | [144] |
| LIBERO-VPro | 闭环视觉扰动鲁棒性 | 仿真 | 扰动分布定义影响结论 | [31] |
| LIBERO-Para | 指令改写鲁棒性 | 仿真 | 与语义安全/视觉鲁棒性正交 | [32] |
| LIBERO-Safety | 物理与语义安全 | 仿真（参数化生成安全关键场景） | 安全判定标准需核实 | [138] |
| LIBERO-RECOVER | 失败恢复 | 仿真 | 恢复成功率口径需核实 | [143] |
| BEHAVIOR-1K | 1000 项日常活动 | 仿真 | 任务定义与算力门槛待核实 | [35] |
| ManiSkill3 | GPU 并行仿真与渲染 | 仿真 | 版本差异与评测协议待核实 | [136] |
| PolaRiS | real-to-sim 策略评估 | real-to-sim | 与真机 SOTA 的可比性待核实 | [91] |
| What-If World | 因果响应（输入变化→输出变化） | 视频世界模型 | 指标与下游策略成功率关系待核实 | [37] |
| PhysicsBench | 工程设计与仿真中的生成/预测模型 | 跨域榜单 | 与本领域操作基准不可直接比 | [133] |

> **待核实**：ManiSkill3、LIBERO、SimplerEnv、RoboCasa、BEHAVIOR-1K 各自的**任务数、本体清单、成功判定口径**在本轮候选中均缺少可核查细节；**WorldModelBench 在本轮候选中无任何来源** > 待核实。

---

## 六、经典与奠基性工作

**6.1 奠基性论文**

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| World Models | 2018 | NeurIPS（种子块标注） | > 待核实（种子资源，未在本次编号列表内） | 同行评审（NeurIPS，据种子块） | 高——世界模型概念开创，领域通用引用基准 | ★★★★★——概念源头，必读 | https://arxiv.org/abs/1803.10122 | 世界模型概念开创（种子） |
| Mastering Diverse Domains through World Models (DreamerV3) | 2023 | Nature（种子块标注） | > 待核实 | 同行评审（Nature，据种子块） | 高——通用世界模型 RL 奠基 | ★★★★★——理解"世界模型如何提升控制"的最佳经典入口 | https://arxiv.org/abs/2301.04104 | 通用世界模型 RL 奠基（种子） |
| MuJoCo: A physics engine for model-based control | 2012 | IROS（种子块标注） | > 待核实 | 同行评审（IROS，据种子块） | 高——机器人仿真事实标准 | ★★★★★——物理引擎选型的基线 | https://ieeexplore.ieee.org/document/6386109 | 经典物理引擎（种子） |
| Dojo: A Differentiable Physics Engine for Robotics | 2022 | 候选块未提供 | > 待核实 [94] | arXiv:2203.00806 预印本 [94] | 中——可微物理代表性工作 | ★★★★☆——可微仿真路线锚点 | https://arxiv.org/abs/2203.00806 | 可微物理引擎 [94] |
| Isaac Gym | 2021 | NVIDIA（据标题口径） | > 待核实 [116] | arXiv:2108.10470v2 预印本 [116] | 高——GPU 并行仿真范式开创者 | ★★★★★——理解 Isaac Lab 之前必读 | http://arxiv.org/abs/2108.10470v2 | GPU 并行仿真 [116] |
| GNS: A generalizable GNN-based simulator | 2022 | 候选块未提供 | > 待核实 [23] | arXiv:2211.10228v1 预印本 [23] | 低—中 | ★★★☆☆——神经仿真替代理代模型代表 | http://arxiv.org/abs/2211.10228v1 | 神经仿真器（颗粒/流体）[23] |
| Genie: Generative Interactive Environments | 2024 | 候选块未提供 | > 待核实 [62] | arXiv:2402.15391v1 预印本 [62] | 高——生成式可交互环境开创性工作 | ★★★★★——Genie Envisioner 的直接前身 | http://arxiv.org/abs/2402.15391v1 | 生成式交互环境 [62] |
| LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning | 2023 | 候选块未提供 | > 待核实 [140] | arXiv:2306.03310v2 预印本 [140] | 高——VLA 评测主流基准 | ★★★★★——评测选型必读 | http://arxiv.org/abs/2306.03310v2 | 终身学习基准 [140] |
| BEHAVIOR-1K | 2024 | 候选块未提供（human-centered benchmark） | > 待核实 [35] | arXiv:2403.09227v1 预印本 [35] | 中—高——大规模家务仿真基准 | ★★★★☆——活动级评测参考 | http://arxiv.org/abs/2403.09227v1 | 1000 项日常活动 [35] |
| ManiSkill3 | 2024 | 候选块未提供 | > 待核实 [136] | arXiv:2410.00425v2 预印本 [136] | 中—高——GPU 并行操作基准 | ★★★★★——操作仿真选型核心 | http://arxiv.org/abs/2410.00425v2 | GPU 并行仿真与渲染 [136] |
| Sora as a World Model? A Complete Survey on Text-to-Video Generation | 2024 | 候选块未提供 | > 待核实 [42] | arXiv:2403.05131v3 预印本 [42] | 中——T2V 作为世界模型的综述入口 | ★★★★☆——视频世界模型背景综述 | http://arxiv.org/abs/2403.05131v3 | T2V 世界模型综述 [42] |
| A Survey: Learning Embodied Intelligence from Physical Simulators and World Models | 2025 | 候选块未提供 | > 待核实 [57] | arXiv:2507.00917v3 预印本 [57] | 中——直接对应本报告主题 | ★★★★★——本主题最对口的综述 | http://arxiv.org/abs/2507.00917v3 | 仿真 + 世界模型综述 [57] |

**6.2 开源项目（种子资源 + 候选引用）**

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| google-deepmind/mujoco | — | Google DeepMind | > 待核实（star 数需现场核实） | 官方仓库（厂商/实验室） | 高——机器人仿真默认选项 | ★★★★★——主力物理引擎 | https://github.com/google-deepmind/mujoco | MuJoCo 主仓库（种子） |
| google-deepmind/mujoco_menagerie | — | Google DeepMind | > 待核实 | 官方仓库 | 高——模型资产标配 | ★★★★★——省去建模成本 | https://github.com/google-deepmind/mujoco_menagerie | MuJoCo 模型集（种子） |
| Genesis-Embodied-AI/Genesis | — | Genesis Embodied AI | > 待核实 | 官方仓库 | 中—高——生成式物理仿真引擎，社区讨论热度较高 > 待核实 | ★★★★☆——宣称口径需以实测核实 | https://github.com/Genesis-Embodied-AI/Genesis | 生成式物理仿真引擎（种子） |
| haosulab/ManiSkill | — | Hao Su Lab（UC San Diego） | > 待核实 | 官方仓库 | 中—高 | ★★★★★——操作仿真与基准 | https://github.com/haosulab/ManiSkill | 操作仿真与基准（种子） |
| isaac-sim/IsaacLab | — | NVIDIA | > 待核实 | 官方仓库 | 高——GPU 并行仿真主流 | ★★★★★——大规模并行训练首选 | https://github.com/isaac-sim/IsaacLab | GPU 并行仿真（种子）；对应论文 [114] |

**6.3 数据集与基准（种子 + 候选）**

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| ManiSkill3 / ManiSkill benchmarks | 2024 | 候选块未提供 | > 待核实 | arXiv 预印本 [136]；官方文档站 | 中—高 | ★★★★★ | https://maniskill.readthedocs.io/ | 操作仿真基准（种子）[136] |
| RoboCasa | — | 候选块未提供 | > 待核实 | 官方站点 | 中—高 | ★★★★☆ | https://robocasa.ai/ | 日常任务仿真基准（种子） |
| BEHAVIOR-1K | 2024 | 候选块未提供 | > 待核实 | arXiv 预印本 [35]；官方站点 | 中—高 | ★★★★☆ | https://behavior.stanford.edu/ | 大规模家务仿真基准（种子）[35] |
| LIBERO | 2023 | 候选块未提供 | > 待核实 [140] | arXiv 预印本 [140] | 高——VLA 评测主力 | ★★★★★ | http://arxiv.org/abs/2306.03310v2 | 终身学习基准 [140] |
| LIBERO-PRO | 2025 | 候选块未提供 | citations=177 [144] | arXiv.org（候选块标注）[144] | 高——直接质疑既有排行榜可信度 | ★★★★★ | https://arxiv.org/abs/2510.03827 | 抗记忆化公平评测 [144] |
| SimplerEnv | — | — | > 待核实 | > 待核实 | > 待核实 | — | > 待核实 | 本轮候选无来源 |
| WorldModelBench | — | — | > 待核实 | > 待核实 | > 待核实 | — | > 待核实 | 本轮候选无来源 |

---

## 七、评测、争议与开放问题

**7.1 争议一：仿真基准的分数是否可信？**

- LIBERO-PRO 明确指出 LIBERO 现有训练与评测设置"存在问题，常导致性能估计虚高并妨碍公平比较" [144]；其热度为本轮最高（citations=177 [144]），**权威**：arXiv.org（候选块标注，未见同行评审信息）[144]；**关注度**：高；**推荐度**：★★★★★——任何引用 LIBERO 分数的结论都应先读它 [144]。
- 配套诊断基准从鲁棒性 [31]、改写 [32]、安全 [138]、恢复 [143] 多角度拆解单一成功率指标；另有语言扰动下的持续模仿学习基准 [145]。
- 基准方法学层面：benchmark suite 比较方法论 [139]、PMLB 大规模基准套件 [141]、语义密度重加权 [146]、多保真优化方法评估框架（citations=5）[150]、榜单运营"坏味道"研究 [130]。

**7.2 争议二：世界模型能否提升/替代真机评估？**

- 支持侧：WorldGym 声称世界模型内评估与真机高度相关并保持策略排序 [52]；PolaRiS 主张 real-to-sim 评估可解决真机评测的随机性、可复现性与耗时问题 [91]。
- 质疑侧：Robot Policy Evaluation for Sim-to-Real Transfer 指出机器人本质是真实世界问题，通用策略的**真机评估落后于仿真基准**，并给出基准设计的 desiderata [30]。
- **结论**：相关性在多大任务分布上成立、能否替代真机评估，**尚无定论** > 待核实 [30][52][91]。

**7.3 争议三：物理合理性的度量**

- 生成视频"看似合理"但缺乏物理接地 [36]；推理期物理可控性探索 [117]；因果性基准主张"不是单条视频对不对，而是输入变了输出是否跟着变" [37]。
- **缺口**：缺少把"物理合理性指标"与"下游真机成功率"做相关性分析的证据 > 待核实 [36][37][117]。

**7.4 争议四：算力门槛与可复现性**

- 本轮候选中**没有**关于 MJX/Warp/Brax/Genesis/Isaac Lab 同硬件吞吐量、显存占用、梯度正确性的可比数据 > 待核实。
- 可复现性基础设施讨论见于 ML for Health 的可复现性研究 [72]，但未覆盖机器人仿真 > 待核实。
- 透明度视角：2025 Foundation Model Transparency Index 报告基础模型开发者平均透明度从 2024 年 58 分降至 2025 年 40 分（第三版年度评测，首次评估 Alibaba、DeepSeek、xAI）[3]。
  - **热度**：> 待核实 [3]；**权威**：arXiv:2512.10169v1 (cs.AI) 预印本，作者含 Percy Liang、Rishi Bommasani [3]；**关注度**：中——年度系列评测，但**与机器人基准无可比性**[3]；**推荐度**：★★☆☆☆——仅其"评分协议设计"思路有方法论参考价值 [3]。

**7.5 证据缺口清单（必须显式声明）**

- 域随机化最佳实践/参数分布/失败模式：**无来源** > 待核实。
- real2sim 系统辨识（质量/摩擦/延迟/接触模型、精度度量）：**无来源** > 待核实。
- real2sim2real 闭环完整案例、迭代次数、收敛判据：**无来源** > 待核实。
- 世界模型用于**闭环控制**并给出真机成功率的一手证据：**本轮未见** > 待核实。
- 神经仿真器（learned simulator）在机器人操作域的保真度与可扩展性对比：**未见** > 待核实。
- 检索噪声提示：候选集中混入大量非具身主题（短视频参与度预测 [1]、越南语法律问答 [26]、事件级图像分析 [27]、音频主观质量 [28]、人机信任工作坊 [15] 等），说明自动召回存在明显域外污染，需人工过滤。

---

## 八、建议关注清单（Watchlist）

| 关注对象 | 为什么关注 | 下一步核实动作 | 引用 |
|---|---|---|---|
| WorldGym | 把世界模型当策略评估环境，最接近"可验证决策依据" | 抓全文核对任务数、真机硬件、成功率相关系数与第三方复现 | [52] |
| GEM-4D | 直指视频世界模型的几何一致性缺陷 | 核实是否在真机操作任务上验证及基线对比口径 | [36] |
| Genie Envisioner | 统一策略/评估/仿真的世界基础平台 | 核实 GE-Base 规模、开源情况与跨本体泛化 | [60] |
| Cosmos 3 / Cosmos-Transfer1 / Cosmos WFM | Physical AI 世界基础模型平台化路线 | 核实是否被第三方基准评测，而非仅演示 | [122][123][125][126] |
| GAIA-2 | 可控多视图生成式世界模型（自动驾驶域） | 核实能否迁移到操作域 | [128] |
| PolaRiS | 可扩展 real-to-sim 策略评估（citations=39） | 核实与真机 SOTA 的可比性 | [91] |
| LIBERO-PRO 及 LIBERO 诊断家族 | 基准可信度是当前最尖锐争议 | 核实各诊断基准的任务数与判定口径 | [144][31][32][138][143][140] |
| Isaac Lab / ManiSkill3 | 工程选型的事实基础设施 | 实测同硬件吞吐量与版本兼容性 | [114][136][116] |
| What-If World | 把世界模型评测从画质转向因果响应 | 核实其指标与下游成功率的关联 | [37] |
| 域随机化 / real2sim 系统辨识 / real2sim2real | 本报告最大证据缺口 | 定向检索 arXiv cs.RO（domain randomization、system identification、real2sim2real） | > 待核实 |
| 神经仿真与可微引擎可比基准 | 缺吞吐量/梯度正确性/接触稳定性数据 | 复现 MJX / Warp / Brax / Dojo / Genesis 同任务对比 | [94][45] > 待核实 |

---

## 参考来源

> 以下为本报告实际引用的编号来源（完整候选列表共 151 条）。未引用编号（如 [2][6]–[14][18]–[22][24][25][29][33][34][38][39][41][43][46][48]–[51][55][56][58][61][63]–[65][67]–[73][78][80]–[87][92][93][95]–[99][101][102][104]–[113][115][119]–[121][127][131][132][134][135][137][142][147]–[149][151]）因与主题无关或为检索噪声而未在本报告中作为论据使用。

[1] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1
[3] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1
[15] TRUST 2025: SCRITA and RTSS @ RO-MAN 2025 — http://arxiv.org/abs/2509.11402v1
[16] Benchmarking Generalizable Bimanual Manipulation: RoboTwin Dual-Arm Collaboration Challenge at CVPR 2025 MEIS Workshop — http://arxiv.org/abs/2506.23351v2
[17] ManiSkill-ViTac 2025: Challenge on Manipulation Skill Learning With Vision and Tactile Sensing — http://arxiv.org/abs/2411.12503v1
[23] GNS: A generalizable Graph Neural Network-based simulator for particulate and fluid modeling — http://arxiv.org/abs/2211.10228v1
[26] VLSP 2025 MLQA-TSR Challenge — http://arxiv.org/abs/2510.20381v1
[27] Event-Enriched Image Analysis Grand Challenge at ACM Multimedia 2025 — http://arxiv.org/abs/2508.18904v1
[28] The AudioMOS Challenge 2025 — http://arxiv.org/abs/2509.01336v1
[30] Robot Policy Evaluation for Sim-to-Real Transfer: A Benchmarking Perspective — http://arxiv.org/abs/2508.11117v1
[31] LIBERO-VPro: Benchmarking Closed-Loop Visual Robustness of Robotic Foundation Models — http://arxiv.org/abs/2609.24350v1
[32] LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models — http://arxiv.org/abs/2603.28301v3
[35] BEHAVIOR-1K: A Human-Centered, Embodied AI Benchmark with 1,000 Everyday Activities and Realistic Simulation — http://arxiv.org/abs/2403.09227v1
[36] GEM-4D: Geometry-Enhanced Video World Models for Robot Manipulation — http://arxiv.org/abs/2605.22882v4
[37] What-If World: A Causal Benchmark for General World Models in Embodied Scenarios — http://arxiv.org/abs/2605.27589v1
[40] Nano World Models: A Minimalist Implementation of Future Video Prediction — http://arxiv.org/abs/2605.23993v2
[42] Sora as a World Model? A Complete Survey on Text-to-Video Generation — http://arxiv.org/abs/2403.05131v3
[44] The Sound of Simulation: Learning Multimodal Sim-to-Real Robot Policies with Generative Audio — http://arxiv.org/abs/2507.02864v2
[45] Guiding Evolutionary Strategies by Differentiable Robot Simulators — http://arxiv.org/abs/2110.00438v3
[47] Robot Trains Robot: Automatic Real-World Policy Adaptation and Learning for Humanoids — http://arxiv.org/abs/2508.12252v2
[52] WorldGym: World Model as An Environment for Policy Evaluation — http://arxiv.org/abs/2506.00613v3
[57] A Survey: Learning Embodied Intelligence from Physical Simulators and World Models — http://arxiv.org/abs/2507.00917v3
[60] Genie Envisioner: A Unified World Foundation Platform for Robotic Manipulation — http://arxiv.org/abs/2508.05635v3
[62] Genie: Generative Interactive Environments — http://arxiv.org/abs/2402.15391v1
[72] Reproducibility in Machine Learning for Health — http://arxiv.org/abs/1907.01463v1
[74] The Importance and the Limitations of Sim2Real for Robotic Manipulation in Precision Agriculture — http://arxiv.org/abs/2008.03983v1
[75] Sim2Real Transfer for Audio-Visual Navigation with Frequency-Adaptive Acoustic Field Prediction — http://arxiv.org/abs/2405.02821v2
[76] Bridging the Sim2Real Gap: Vision Encoder Pre-Training for Visuomotor Policy Transfer — http://arxiv.org/abs/2501.16389v2
[77] Perspectives on Sim2Real Transfer for Robotics: A Summary of the R:SS 2020 Workshop — http://arxiv.org/abs/2012.03806v1
[79] Robot Manipulation with GPT-6-Astra: Body Knowledge, Experience Reuse, Emergent Skills, and Sim2Real Transfer — http://arxiv.org/abs/2609.31770v1
[88] Sim-to-Real Transfer in Deep Reinforcement Learning for Bipedal Locomotion — http://arxiv.org/abs/2511.06465v1
[89] Real-World Humanoid Locomotion with Reinforcement Learning — http://arxiv.org/abs/2303.03381v2
[90] Learning Sim-to-Real Humanoid Locomotion in 15 Minutes — http://arxiv.org/abs/2512.01996v1
[91] PolaRiS: Scalable Real-to-Sim Evaluations for Generalist Robot Policies — https://arxiv.org/abs/2512.16881
[94] Dojo: A Differentiable Physics Engine for Robotics — https://arxiv.org/abs/2203.00806
[100] Mechanical Intelligence-Aware Curriculum Reinforcement Learning for Humanoids with Parallel Actuation — http://arxiv.org/abs/2507.00273v3
[103] Assistax: A Multi-Agent Hardware-Accelerated Reinforcement Learning Benchmark for Assistive Robotics — https://arxiv.org/abs/2507.21638
[114] Isaac Lab: A GPU-Accelerated Simulation Framework for Multi-Modal Robot Learning — http://arxiv.org/abs/2511.04831v1
[116] Isaac Gym: High Performance GPU-Based Physics Simulation For Robot Learning — http://arxiv.org/abs/2108.10470v2
[117] Causal Physics Steering in Video World Models via Concept Activation Vectors — http://arxiv.org/abs/2605.24322v1
[118] Towards Interactive Video World Modeling: Frontiers, Challenges, Benchmarks, and Future Trends — http://arxiv.org/abs/2606.01164v1
[122] Cosmos World Foundation Model Platform for Physical AI — http://arxiv.org/abs/2501.03575v3
[123] Cosmos-Transfer1: Conditional World Generation with Adaptive Multimodal Control — http://arxiv.org/abs/2503.14492v2
[124] Cosmos-Surg-dVRK: World Foundation Model-based Automated Online Evaluation of Surgical Robot Policy Learning — http://arxiv.org/abs/2510.16240v2
[125] World Simulation with Video Foundation Models for Physical AI — http://arxiv.org/abs/2511.00062v2
[126] Cosmos 3: Omnimodal World Models for Physical AI — http://arxiv.org/abs/2606.02800v4
[128] GAIA-2: A Controllable Multi-View Generative World Model for Autonomous Driving — http://arxiv.org/abs/2503.20523v1
[129] Grounding Video Reasoning in Physical Signals — http://arxiv.org/abs/2604.21873v1
[130] On the Workflows and Smells of Leaderboard Operations (LBOps): An Exploratory Study of Foundation Model Leaderboards — http://arxiv.org/abs/2407.04065v4
[133] PhysicsBench: A Unified Leaderboard for Generative and Predictive Models in Engineering Design and Simulation — http://arxiv.org/abs/2608.24056v1
[136] ManiSkill3: GPU Parallelized Robotics Simulation and Rendering for Generalizable Embodied AI — http://arxiv.org/abs/2410.00425v2
[138] LIBERO-Safety: A Comprehensive Benchmark for Physical and Semantic Safety in Vision-Language-Action Models — http://arxiv.org/abs/2606.23686v2
[139] On the Assessment of Benchmark Suites for Algorithm Comparison — http://arxiv.org/abs/2104.07381v1
[140] LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning — http://arxiv.org/abs/2306.03310v2
[141] PMLB: A Large Benchmark Suite for Machine Learning Evaluation and Comparison — http://arxiv.org/abs/1703.00512v1
[143] LIBERO-RECOVER: Beyond Task Success Towards Failure Recovery in Robotic Manipulation Models — http://arxiv.org/abs/2609.05178v3
[144] LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization — https://arxiv.org/abs/2510.03827
[145] Does Continual Imitation Learning Remain Grounded? A Language-Perturbed Benchmark for Robotic Task Retention — http://arxiv.org/abs/2610.00542
[146] Balance of Benchmarks: Semantic Density Reweighting for Task-Conditioned Model Comparison — http://arxiv.org/abs/2608.30044
[150] Analytical benchmark problems and methodological framework for the assessment and comparison of multifidelity optimization methods — https://doi.org/10.1007/s11831-025-10392-8

**种子资源（领域已知，非本次检索编号）**
- World Models (2018) — https://arxiv.org/abs/1803.10122
- DreamerV3 (Nature, 2023) — https://arxiv.org/abs/2301.04104
- MuJoCo (IROS, 2012) — https://ieeexplore.ieee.org/document/6386109
- google-deepmind/mujoco — https://github.com/google-deepmind/mujoco
- google-deepmind/mujoco_menagerie — https://github.com/google-deepmind/mujoco_menagerie
- Genesis-Embodied-AI/Genesis — https://github.com/Genesis-Embodied-AI/Genesis
- haosulab/ManiSkill — https://github.com/haosulab/ManiSkill
- isaac-sim/IsaacLab — https://github.com/isaac-sim/IsaacLab
- ManiSkill3 / ManiSkill benchmarks — https://maniskill.readthedocs.io/
- RoboCasa — https://robocasa.ai/
- BEHAVIOR-1K — https://behavior.stanford.edu/

> **总体可靠性声明**：本报告绝大多数条目为 arXiv 预印本（B 级证据），未标注同行评审 venue；除 [91]（citations=39）、[103]（citations=0）、[144]（citations=177）、[150]（citations=5）外，候选块未提供任何引用数、GitHub star 或榜单排名，故相关条目一律标注 `> 待核实`，未作任何数字推测。所有"世界模型/仿真能提升控制性能"的强结论在本轮证据下均不成立，需补充真机闭环实验与第三方复现后再行定论。

---

*Generated by research-bot · topic=`embodied-world-models` · depth=`standard` · rounds=2 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading · model=`deepseek-v4-flash` · sources=151 · duration=639s · 2026-10-06T22:46:05+00:00*
