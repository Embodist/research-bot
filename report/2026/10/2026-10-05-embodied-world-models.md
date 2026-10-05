# 具身智能 · 世界模型与仿真（World Models & Simulation）证据化调研报告

**日期**：2026-10-05（UTC） ｜ **领域**：Embodied AI / World Models / Physics Simulation / Model-Based RL ｜ **检索源数量**：候选来源 107 条（编号 [1]–[107]），其中与本主题直接相关约 40 条 ｜ **方法论**：deep-research 四阶段 + frontier-tracking 时间线 + paper-survey 图谱 + evidence-grading 分级

> **证据可得性声明（重要）**：本批候选块**未携带引用数（citations）、GitHub star、下载量等热度字段**。因此下文所有「热度」栏一律标注 `> 待核实`，或以「定性描述 + 待核实」形式给出，**不编造任何数字**。「权威」栏依据可核查的载体类型（arXiv 预印本 / 会议 / 官方仓库 / 期刊 DOI）判定。「关注度」为基于载体、主题位置与被引用场景的编辑判断，依据写在括号中。

> **检索噪声提醒**：本批来源中含大量与主题无关的召回（如短视频参与度预测挑战赛 [4]、图像超分辨率挑战赛 [9]、单图去模糊 [7]、越南语法律问答 [8]、RO-MAN TRUST 工作坊 [39]、ACM MM 事件图像分析 [40]、天文学/粒子物理 [13][26][27]）。这类条目**在正文中不作为证据使用**，其存在本身反映「世界模型 / simulation」一词的多义性对检索召回的污染，已计入证据链风险（见第七章）。

---

## 摘要（Executive Summary）

1. **「视频生成模型 = 世界模型」是 2024–2026 年最热也最受质疑的命题。** 支持方以 Genie 系列（生成式可交互环境）[89] 与 Genie Envisioner（面向机器人操作的世界基础平台）[84] 为代表；质疑方以《Sora as a World Model? A Complete Survey on Text-to-Video Generation》[65] 系统性质疑文本到视频模型的物理一致性，GEM-4D 则实证指出视频世界模型「画面可信但跨时间无法跟踪同一物理点」[66]。
2. **世界模型开始从「策略生成器」转向「策略评测环境」。** WorldGym 提出自回归、动作条件视频生成模型作为策略评估环境，以替代昂贵真机测试与手工仿真器 [76]；与之呼应的是机器人评测体系对 sim-to-real 口径的系统性反思 [77][104]。
3. **世界模型 × 强化学习的经典脉络在本批来源中可核实到两条锚点**：World Models（2018，循环世界模型驱动策略演化）[20] 与 DreamerV3（Nature 系通用世界模型 RL）[3]。PlaNet→Dreamer→MuZero 的完整链条中，**PlaNet 与 MuZero 在本批检索源内无一手引用，`> 待核实`**。
4. **仿真工程栈的主战场是 GPU 并行与多模态保真度**：Isaac Lab 作为 Isaac Gym 的继任者，主张 GPU 原生并行物理 + 照片级渲染 + 模块化组合架构 [50][51]；ManiSkill3 以 GPU 并行仿真与渲染、开源、面向 sim2real 与泛化 [41]；MJX/Brax 路线用于人形运动的大规模并行学习 [37]。
5. **可微/神经仿真仍是「窄而深」的工具**：可微物理引擎用于弹簧-杆系统的参数辨识 [36]，SOFA 框架用于软体机器人触觉的在线固体力学仿真 [31]，前向仿真用于探索规划 [34]。**「神经仿真整体替代物理引擎」在本次检索中未找到可信的正面证据，`> 待核实`**。
6. **sim2real 的方法学共识是「缩小差距」而非「消除差距」**：视觉编码器预训练 [58]、Isaac Sim→Gazebo→ROS 2 真机的迁移链路 [52]、音频等多模态生成式补全 [103][63]、真机自学习（Robot Trains Robot）[78] 均是「补丁式」方案；R:SS 2020 工作坊总结 [59] 与精准农业场景的限制分析 [61] 提供了负结果视角。
7. **评测基准正在从「仿真内排名」走向「real-to-sim / 世界模型内评估」**：LIBERO 作为终身机器人学习迁移基准 [96] 已派生视觉鲁棒性变体 LIBERO-VPro [101]；PolaRiS 主张可扩展的 real-to-sim 评测 [104]；WorldModelBench 专门评判视频生成模型作为世界模型的质量 [107]。

---

## 一、关键前沿进展（近 1–2 年）

近 12–24 个月真正的结构性变化是：**世界模型的角色从「训练策略的内部组件」外化为「可独立评测的环境 / 数据引擎」**，同时仿真栈全面 GPU 化、多模态化。

| 名称 | 时间 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 |
|---|---|---|---|---|---|---|---|
| WorldGym：世界模型作为策略评估环境 [76] | 2025-06 | 未获取（arXiv cs.RO） | > 待核实 | arXiv 预印本（B 级） | 中（切中「评测昂贵」痛点） | ★★★★☆：把视频世界模型用于 policy evaluation，方向价值高 | http://arxiv.org/abs/2506.00613v3 |
| GEM-4D：几何增强视频世界模型 [66] | 2026-05 | 未获取（arXiv cs.CV） | > 待核实 | arXiv 预印本（B 级） | 中高（直击物理一致性痛点） | ★★★★☆：明确指出「画面合理但物理不落地」的失效模式 | http://arxiv.org/abs/2605.22882v4 |
| Causal Physics Steering（PEZ / CAV）[67] | 2026-05 | 未获取（arXiv cs.CV） | > 待核实 | arXiv 预印本（B 级） | 中（可解释性 + 控制交叉） | ★★★☆：推理期物理可控性，方法有启发性但需复现验证 | http://arxiv.org/abs/2605.24322v1 |
| Genie Envisioner：机器人操作世界基础平台 [84] | 2025-08 | 未获取（arXiv） | > 待核实 | arXiv 预印本（B 级） | 中高（Genie 品牌延续） | ★★★★☆：从通用视频世界模型走向操作专用平台 | http://arxiv.org/abs/2508.05635v3 |
| 仿真路线图《Simulating the Visual World with AI》[68] | 2025-11 | 未获取（arXiv） | > 待核实 | arXiv 综述（B 级） | 中（综述类） | ★★★★☆：适合作为领域地图入口 | http://arxiv.org/abs/2511.08585v4 |
| 多模态生成模型统一综述 [69] | 2025-03 | 未获取（arXiv） | > 待核实 | arXiv 综述（B 级） | 中 | ★★★★☆：世界仿真视角下的生成模型谱系 | http://arxiv.org/abs/2503.04641v3 |
| 物理仿真器与世界模型综述 [93] | 2025-07 | 未获取（arXiv） | > 待核实 | arXiv 综述（B 级） | 中高（主题高度对口） | ★★★★★：本主题最对口的中文/英文综述入口 | http://arxiv.org/abs/2507.00917v3 |
| Isaac Lab：GPU 加速多模态机器人学习仿真 [50] | 2025-11 | 未获取（arXiv cs.RO） | > 待核实 | arXiv 预印本（B 级） | 高（NVIDIA 生态事实标准） | ★★★★★：选型必经 | http://arxiv.org/abs/2511.04831v1 |

**四轴证据说明（逐条）**

- **WorldGym [76]**——热度：`> 待核实`（无 citations 字段）；权威：arXiv cs.RO 预印本，**未经同行评审确认**；关注度：中，依据是「策略评测成本」被 [77][104] 同向确认，属被多篇独立工作指向的痛点；推荐度 ★★★★☆。
- **GEM-4D [66]**——热度：`> 待核实`；权威：arXiv cs.CV 预印本；关注度：中高，依据其摘要直接给出可检验的失效断言（跨时间物理点跟踪不一致）；推荐度 ★★★★☆。
- **Causal Physics Steering [67]**——热度：`> 待核实`；权威：arXiv cs.CV 预印本，**PEZ（Physics Emergence Zone）为作者自述发现，未见独立复现**；关注度：中；推荐度 ★★★☆。
- **Genie Envisioner [84]**——热度：`> 待核实`；权威：arXiv 预印本（作者与机构信息未在本次抽取中获取）；关注度：中高，依据 Genie 系列的品牌延续性 [89]；推荐度 ★★★★☆。
- **Isaac Lab [50]**——热度：`> 待核实`；权威：arXiv 预印本 + NVIDIA 官方仓库（种子资源 `isaac-sim/IsaacLab`）双重存在；关注度：高，依据整个 Isaac Sim/Gym 生态在 sim2real 文献中的高频出场 [52][53][54][55]；推荐度 ★★★★★。

**方法学要点（含负结果）**

- 世界模型用于评测时，其**自身误差会直接注入评测结论**，WorldGym 的自回归生成范式 [76] 与 GEM-4D 指出的物理不落地问题 [66] 构成同一枚硬币的两面。
- 真机侧仍不可省略：人形机器人真机策略自适应（Robot Trains Robot）显式以「真机学习稀缺」为前提 [78]；GPT-6-Astra 类工作把 body knowledge / 经验复用 / sim2real 作为组合手段 [62]。

---

## 二、生成式/视频世界模型

### 2.1 生成式交互环境

- **Genie（Generative Interactive Environments）[89]**：从单张图像提示生成可交互环境，是「生成式环境」范式的奠基性代表（2024）。
- **Genie Envisioner [84]**：把该范式推进到机器人操作领域，定位为「统一的世界基础平台」。
- **DiLA：Disentangled Latent Action World Models [21]**：面向潜在动作解耦的世界模型（2026-05），属该方向较新的架构探索。

### 2.2 视频世界模型的能力边界

| 能力维度 | 正面证据 | 反面证据 | 结论 |
|---|---|---|---|
| 视觉真实感 | 视频生成模型可生成逼真未来帧 [76][66] | 真实感 ≠ 可执行性 [66] | 真实感已被较好解决，**物理落地未解决** |
| 跨时间物理一致性 | 几何增强试图修复 [66] | 无法稳定跟踪同一物理点 [66] | **核心短板**，`> 待核实` 是否有通用解 |
| 推理期物理可控性 | PEZ 层可被概念激活向量引导 [67] | 依赖作者自述的层定位，未见第三方复现 | 有前景，**证据等级 C** |
| 作为评测环境 | WorldGym 以自回归动作条件生成模型做策略评估 [76] | 尚无第三方对其保真度的独立审计 | 方法论成立，**精度待核实** |
| 作为世界模型的「资格」 | — | 综述系统质疑文本到视频模型即世界模型 [65] | **学院派主流持保留态度** |

### 2.3 四轴证据

- **[89] Genie**——热度：`> 待核实`（无 citations 字段，但为 DeepMind 2024 高关注工作）；权威：arXiv 2402.15391v1，`> 待核实` 是否已中稿；关注度：高；推荐度 ★★★★★（范式奠基）。
- **[65] Sora as a World Model? Survey**——热度：`> 待核实`；权威：arXiv 综述 v3，被本领域反复用作质疑入口；关注度：高；推荐度 ★★★★★（**必读的怀疑派文本**）。
- **[67] Causal Physics Steering**——热度：`> 待核实`；权威：预印本（B 级）；关注度：中；推荐度 ★★★☆。
- **[107] WorldModelBench**——热度：`> 待核实`；权威：arXiv 2502.20694v1 预印本；关注度：中高（基准类工作直接影响可比性）；推荐度 ★★★★☆；**其具体任务数、评测口径 `> 待核实`**。

---

## 三、神经仿真与可微物理

**核心判断：可微仿真的证据集中在「参数辨识 / 系统辨识」与「局部接触力学」，尚无整体替代通用物理引擎的实证。**

| 工作 | 年份 | 梯度信息用途 | 热度 | 权威 | 关注度 | 推荐度 | 链接 |
|---|---|---|---|---|---|---|---|
| Spring-Rod System Identification via Differentiable Physics Engine [36] | 2020 | 以离散化控制方程的模块化可微引擎做系统辨识，而非黑盒学习动力学 | > 待核实 | arXiv cs.RO 预印本 | 中（可微仿真早期代表） | ★★★★☆：可微引擎「白盒化」思路清晰 | http://arxiv.org/abs/2011.04910v1 |
| SOFA + 电容触觉在线固体力学仿真 [31] | 2025 | 在线固体力学仿真做任意形状接触检测 | > 待核实 | arXiv cs.RO 预印本 | 低-中（软体 HRI 细分） | ★★★☆：软体触觉方向参考 | http://arxiv.org/abs/2503.02280v1 |
| Brax + MJX 大规模并行人形运动学习 [37] | 2024 | MJX 的可微/加速物理支撑大规模并行 RL | > 待核实 | arXiv cs.RO 预印本 | 中高（MJX 生态代表引用） | ★★★★☆：GPU 并行 + 运动控制的实操参考 | http://arxiv.org/abs/2407.05148v1 |
| 基于前向仿真的机器人探索规划 [34] | 2015 | 以前向仿真做信息增益最大化（POMDP） | > 待核实 | arXiv cs.RO 预印本（IROS 系） | 中（经典） | ★★★☆：前向仿真规划的思想源头之一 | http://arxiv.org/abs/1502.02474v2 |
| 最大熵 model-based RL [14] | 2021 | — | > 待核实 | arXiv cs.LG 预印本 | 低-中 | ★★☆：与本主题相关性偏弱 | http://arxiv.org/abs/2112.01195v1 |
| 高效 model-based 多智能体 mean-field RL [15] | 2021 | — | > 待核实 | arXiv cs.LG 预印本 | 低 | ★★☆：多机器人场景周边 | http://arxiv.org/abs/2107.04050v2 |

**四轴证据（择要）**

- **[36]**——热度：`> 待核实`；权威：预印本（B 级），属可微物理早期被引用工作；关注度：中；推荐度 ★★★★☆（可微引擎=白盒参数辨识的代表性论证）。
- **[37]**——热度：`> 待核实`；权威：预印本（B 级）；关注度：中高，依据 MJX/Brax 已成为 GPU 并行物理的主流选项之一；推荐度 ★★★★☆。
- **sim2real/策略优化上的实证优势**：本次检索**未获得**「可微仿真 vs 传统仿真」的受控对照实验结果。`> 待核实`。

**扩展阅读（同向但非核心）**：[11] 多模态转移动力学学习（2017）、[12] 面向机器人控制的实时 model-based RL 架构（2011）、[60] 交互式回放的一次性 RL 导航（2017）——三者构成 model-based RL 在机器人上的早期工程脉络。

---

## 四、sim2real 迁移与方法

**核心判断：领域共识已从「追求无缝 sim2real」转向「承认差距、系统性测量差距、并显式补偿差距」。**

| 方法族 | 代表工作 | 主张 | 热度 | 权威 | 关注度 | 推荐度 |
|---|---|---|---|---|---|---|
| 感知侧预训练 | Bridging the Sim2Real Gap: Vision Encoder Pre-Training [58] | 用大规模视觉编码器预训练缩小视觉域差 | > 待核实 | arXiv 预印本（B 级） | 中 | ★★★★☆ |
| 引擎/中间件链路 | Isaac Sim → Gazebo → ROS 2 真机迁移 [52] | 给出可复现的迁移工程链路 | > 待核实 | arXiv 预印本（B 级） | 中 | ★★★★☆ |
| 差距量化 | TIAGo + Isaac Sim/Gym 的 sim2real gap 用例 [53] | 以具体机器人量化 RL 的 sim2real 差距 | > 待核实 | arXiv 预印本（B 级） | 中 | ★★★★☆ |
| 触觉模态 | TacEx：Isaac Sim 中的 GelSight 触觉仿真 [54] | 软体 + 视觉触觉联合仿真 | > 待核实 | arXiv 预印本（B 级） | 中 | ★★★★☆ |
| 声学/音频模态 | 生成式音频的多模态 sim2real 策略 [103]；音频-视觉导航的频率自适应声场预测 [63] | 生成式音频补齐仿真缺失的听觉模态 | > 待核实 | arXiv 预印本（B 级） | 低-中 | ★★★☆ |
| 真机自学习 | Robot Trains Robot：人形真机策略自适应 [78] | 真机侧自动适配与学习，缓解「仿真到真机」单向依赖 | > 待核实 | arXiv 预印本（B 级） | 中高 | ★★★★☆ |
| 反思与负结果 | R:SS 2020 Sim2Real 工作坊总结 [59]；精准农业场景的 Sim2Real 局限 [61] | 明确 sim2real 的适用边界与失败场景 | > 待核实 | arXiv（工作坊总结 / 预印本） | 中（长期被引用作为免责依据） | ★★★★☆ |
| 端到端 agent + sim2real | GPT-6-Astra 的机器人操作 [62] | body knowledge / 经验复用 / 涌现技能 / sim2real 组合 | > 待核实 | arXiv cs.RO 预印本 | 中（2026 新作） | ★★★☆（**结论需谨慎，`> 待核实`**） |

**关键工程结论**

- 触觉 [54]、音频 [103][63] 等非视觉模态的仿真保真度长期落后于视觉（[103] 摘要明确承认这一点），是 sim2real 的下一个瓶颈带。
- 真机侧仍有不可替代价值：人形真机 RL 的稀缺性被 [78] 直接作为动机陈述。
- 安全维度：世界模型被用于「梦见」不安全状态并提前规划（Nightmare Dreamer）[91]，指向 sim2real 之外的第二类风险——**在世界模型里犯错也可能被放大**；系统性风险梳理见《Safety in Embodied AI》[94]。

---

## 五、仿真引擎与基准

### 5.1 仿真引擎与工程栈（选型权衡）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Isaac Lab [50] | 2025 | NVIDIA（arXiv 未列作者） | > 待核实 | arXiv 预印本 + 官方仓库（B 级） | 高 | ★★★★★ | http://arxiv.org/abs/2511.04831v1 | Isaac Gym 继任者；GPU 原生并行物理 + 照片级渲染 + 模块化组合 |
| Isaac Gym [51] | 2021 | NVIDIA | > 待核实 | arXiv 预印本 + 官方仓库 | 高（历史基线） | ★★★★☆ | http://arxiv.org/abs/2108.10470v2 | GPU 物理仿真做机器人学习的奠基工程 |
| ManiSkill3 [41] | 2024 | haosulab（UC San Diego） | > 待核实 | arXiv 预印本 + 官方仓库 + 官方文档 | 高 | ★★★★★ | http://arxiv.org/abs/2410.00425v2 | GPU 并行仿真与渲染；开源；直指 sim2real 与泛化 |
| MJX / Brax [37] | 2024 | 未获取 | > 待核实 | arXiv 预印本 | 中高 | ★★★★☆ | http://arxiv.org/abs/2407.05148v1 | JAX 生态的加速物理，适合大规模并行 RL |
| MuJoCo | 2012 | Todorov 等（IROS） | > 待核实 | IROS 论文（A 级，种子资源） | 高（社区事实标准） | ★★★★★ | https://ieeexplore.ieee.org/document/6386109 | 经典物理引擎，`google-deepmind/mujoco` 维护 |
| MuJoCo Menagerie | — | Google DeepMind | > 待核实 | 官方仓库 | 高 | ★★★★☆ | https://github.com/google-deepmind/mujoco_menagerie | 高质量模型集 |
| Genesis | 2024 起 | Genesis-Embodied-AI | > 待核实 | 官方仓库 | 中高（社区热度曾极高，**本次无一手评测**） | ★★★☆（`> 待核实`） | https://github.com/Genesis-Embodied-AI/Genesis | 生成式物理仿真引擎，**独立基准表现待核实** |
| SAPIEN / PyBullet / Drake | — | — | > 待核实 | 本次检索源中**无一手引用** | > 待核实 | `> 待核实` | — | **证据缺口**，选型时须另行核实 |
| SOFA [31] | 2025 | 未获取 | > 待核实 | arXiv 预印本 | 低-中 | ★★★☆ | http://arxiv.org/abs/2503.02280v1 | 软体/固体力学在线仿真，触觉场景可用 |

**选型权衡（基于可核查证据）**

- **GPU 并行吞吐**：Isaac Lab [50]、ManiSkill3 [41]、MJX/Brax [37] 三线并进；ManiSkill3 明确把「现有框架场景/任务窄、缺乏泛化与 sim2real 关键特性」作为设计动机 [41]。
- **多模态保真度**：视觉已较成熟，触觉 [54]、声学 [103][63] 是短板。
- **可视化/物理精度与吞吐的权衡**：Isaac 系列以照片级渲染 + GPU 物理换取大规模并行 [50][51]；`> 待核实` 各引擎在同一任务上的绝对精度对照数据（本次检索未获得）。

### 5.2 数据集与基准

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| LIBERO [96] | 2023 | 未获取（arXiv） | > 待核实 | arXiv 预印本（B 级） | 高（终身机器人学习迁移常用基准） | ★★★★★ | http://arxiv.org/abs/2306.03310v2 | Benchmarking knowledge transfer for lifelong robot learning |
| LIBERO-VPro [101] | 2026 | 未获取（arXiv cs.RO） | > 待核实 | arXiv 预印本 | 中（新，鲁棒性视角） | ★★★★☆ | http://arxiv.org/abs/2609.24350v1 | 闭环视觉鲁棒性：质疑标准基准「干净观测」假设 |
| WorldModelBench [107] | 2025 | 未获取（arXiv） | > 待核实 | arXiv 预印本 | 中高 | ★★★★☆ | http://arxiv.org/abs/2502.20694v1 | 把视频生成模型当世界模型来评判 |
| WorldGym [76] | 2025 | 未获取（arXiv cs.RO） | > 待核实 | arXiv 预印本 | 中高 | ★★★★☆ | http://arxiv.org/abs/2506.00613v3 | 世界模型即评测环境 |
| PolaRiS [104] | 2025 | 未获取（arXiv cs.RO） | > 待核实 | arXiv 预印本 | 中高 | ★★★★☆ | http://arxiv.org/abs/2512.16881v2 | 可扩展 real-to-sim 评测，直面真机 rollout 的随机性与耗时 |
| ManiSkill3 / ManiSkill benchmarks | 2024 起 | haosulab | > 待核实 | 官方文档 + 代码 | 高 | ★★★★★ | https://maniskill.readthedocs.io/ | 操作仿真基准（种子资源） |
| RoboCasa | 2024 起 | UT Austin 等 | > 待核实 | 官方主页 | 高 | ★★★★☆ | https://robocasa.ai/ | 日常任务仿真基准（种子资源） |
| BEHAVIOR-1K | 2022 起 | Stanford | > 待核实 | 官方主页 | 高 | ★★★★☆ | https://behavior.stanford.edu/ | 大规模家务仿真基准（种子资源） |
| DROID / Open X-Embodiment / SimplerEnv / RLBench / RoboArena | — | — | > 待核实 | 本次检索源中**无一手引用** | > 待核实 | `> 待核实` | — | **证据缺口**：本报告不对其任务数、口径作任何断言 |

**口径提醒（[77] 的核心论点）**：机器人本质是真实世界问题，当前基于视觉的仿真基准虽推动了操作研究，但**面向通用策略的真机评测长期滞后** [77]。因此任何「仿真 SOTA」都不应被等同于「真机 SOTA」——该限定同样适用于 [41][76][104] 的结论。

---

## 六、经典与奠基性工作

> 本节严格区分：以下为**奠基/经典**（2012–2023），不与第一章「最新进展」混同。

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| World Models（Recurrent World Models Facilitate Policy Evolution）[20] | 2018 | D. Ha, J. Schmidhuber | > 待核实（领域内公认高被引，**具体数值待核实**） | NeurIPS 2018（A 级） | 高 | ★★★★★ | http://arxiv.org/abs/1809.01999v1 | 「在世界模型里做梦训练策略」的开创性文本 |
| DreamerV3（Mastering Diverse Domains through World Models）[3] | 2023（arXiv）/ Nature 版 | Google DeepMind（Hafner 等） | > 待核实（**公认高被引，数值待核实**） | 期刊 + arXiv v2（A 级） | 高 | ★★★★★ | http://arxiv.org/abs/2301.04104v2 | 通用世界模型 RL 的集大成者，跨域单一超参 |
| MuJoCo: A physics engine for model-based control | 2012 | Todorov, Erez, Tassa（IROS） | > 待核实 | IROS 2012（A 级，种子资源） | 高 | ★★★★★ | https://ieeexplore.ieee.org/document/6386109 | 面向 model-based control 的经典引擎，至今仍是事实基线 |
| Learning Multimodal Transition Dynamics for Model-Based RL [11] | 2017 | 未获取 | > 待核实 | arXiv 预印本 | 中 | ★★★☆ | http://arxiv.org/abs/1705.00470v2 | 多模态转移动力学，世界模型的前身之一 |
| A Real-Time Model-Based RL Architecture for Robot Control [12] | 2011 | 未获取 | > 待核实 | arXiv 预印本 | 中 | ★★★☆ | http://arxiv.org/abs/1105.1749v2 | 早期 model-based RL 的机器人实时架构 |
| One-Shot RL for Robot Navigation with Interactive Replay [60] | 2017 | 未获取 | > 待核实 | arXiv 预印本 | 低-中 | ★★★☆ | http://arxiv.org/abs/1711.10137v2 | 交互式回放的一次性 RL 导航 |
| R:SS 2020 Sim2Real 工作坊总结 [59] | 2020 | 多机构工作坊 | > 待核实 | 工作坊总结（C 级） | 中 | ★★★★☆ | http://arxiv.org/abs/2012.03806v1 | sim2real 争议的经典议题清单 |

**脉络梳理（仅就可核查来源）**

- **世界模型 → 策略**：[20]（2018，循环世界模型内训练策略）→ [3]（2023，跨域通用世界模型 RL）。二者之间的 **PlaNet（2019）与 MuZero（2019/2020）在本次检索源中无一手引用，`> 待核实`**，本报告不代之以记忆叙述。
- **物理引擎 → 并行化 → 多模态**：MuJoCo（2012）→ Isaac Gym [51]（2021）→ Isaac Lab [50]（2025）/ ManiSkill3 [41]（2024）/ MJX-Brax [37]（2024）。
- **model-based RL → 世界模型评测**：[12][60][11] → WorldGym [76]、WorldModelBench [107]、PolaRiS [104]。

---

## 七、评测、争议与开放问题

### 7.1 争议一：视频生成模型是否等价于物理仿真器？

| 立场 | 代表证据 | 证据强度 |
|---|---|---|
| **怀疑派**：不等于，物理一致性不足 | 综述系统质疑文本到视频模型作为世界模型 [65]；GEM-4D 实证指出「画面合理但缺乏可靠动作执行所需的物理落地」[66] | B 级（预印本 + 综述，含可检验断言） |
| **技术乐观派**：可被工程修补 | 几何增强 [66]；推理期物理引导（PEZ / 概念激活向量）[67]；世界模型作为评测环境 [76]；世界模型专用评判基准 [107] | B 级，且 [67] 的 PEZ 定位**未见第三方复现** |
| **应用侧审慎** | 外科手术视频 + 世界模型的临床视角，提示「下一计算层」尚需临床验证 [82] | C 级（期刊 DOI 评论性文章，链接 https://doi.org/10.1007/s11701-026-04000-5） |

**结论**：当前证据**支持**「视频世界模型不等于物理仿真器」，且缺口被具体化为**跨时间物理点跟踪一致性** [66]；「可修补」一派有方法但缺独立复现 [67]。`> 待核实`：是否存在多本体、多任务的第三方统一评测结论。

### 7.2 争议二：神经仿真能否替代物理引擎？

- **支持替代的间接证据**：可微引擎可完成系统辨识并保持物理结构（模块化控制方程）[36]；加速物理（MJX/Brax）在大规模运动学习中已被常规使用 [37]；多模态生成式仿真的统一综述立场 [69]、视觉仿真路线图 [68]。
- **反对/限制的必要证据**：非视觉模态（如声音）仿真保真度长期不足，需生成式音频补全 [103]；触觉仿真才刚开始与视觉仿真整合 [54]；精准农业等场景显示 sim2real 在真实物理约束下失效 [61]。
- **裁定**：本批来源**不足以支持「神经仿真整体替代物理引擎」**，`> 待核实`。更稳妥的表述是：**可微/神经仿真在参数辨识、局部接触与大规模并行策略优化上具备可核查优势；在通用物理保真度与可验证性上，物理引擎仍是基准。**

### 7.3 争议三：基准口径与「仿真 SOTA ≠ 真机 SOTA」

- **问题陈述**：真机 rollout 的随机性、可复现性与耗时使机器人基准化本身困难，这是 PolaRiS 存在的直接动机 [104]；sim-to-real 评测面向真机应用的滞后被明确批评 [77]。
- **现有一点缓解**：LIBERO-VPro 针对「标准基准假定干净、及时、一致的视觉观测」这一宽松假设，提出闭环视觉鲁棒性评测 [101]。
- **开放问题**：世界模型自回归生成误差如何传播到评测结论 [76][66]？`> 待核实`。

### 7.4 争议四：安全与失效

- 世界模型可被用来「梦见」不安全状态并提前规划（Nightmare Dreamer）[91]，方向积极但**其安全收益未经独立验证**，`> 待核实`。
- 具身智能的风险、攻击与防御已有系统性梳理 [94]，可作为安全评估框架入口。

### 7.5 证据链自身的问题（必须披露）

1. **热度字段整体缺失**：所有 citations / star 均无法从本批候选块获得，四轴中的「热度」栏几乎全为 `> 待核实`。
2. **同义词污染严重**：「simulation」「world model」在医学仿真、流体/粒子物理、社会科学等领域高频共现，导致 [4][7][9][13][26][27][39][40][79][81][85][86][88][90] 等大量无关条目被召回。
3. **预印本占比过高**：本报告核心结论大多建立在 arXiv 预印本（B 级）上，仅 [3][20] 等少数有明确会议/期刊归属。**任何基于本报告的技术选型，都应在落地前用一手论文表格与官方榜单二次核实。**

---

## 八、建议关注清单（Watchlist）

| 优先级 | 对象 | 理由（含证据链） | 建议核查动作 |
|---|---|---|---|
| P0 | **WorldGym** [76] | 世界模型作为策略评测环境的范式转移 | 抓全文：生成保真度如何量化？与真机评测的相关性？ |
| P0 | **WorldModelBench** [107] | 世界模型评判的专门基准，直接决定可比性 | 抓全文：任务数、口径、是否覆盖机器人操作 |
| P0 | **Isaac Lab** [50] + **ManiSkill3** [41] | 工程选型两大主流 | 对照官方文档与 release notes，核实版本与维护状态 |
| P0 | **LIBERO** [96] → **LIBERO-VPro** [101] | 基准的鲁棒性转向 | 核实 vPro 的扰动类型与任务数 |
| P1 | **GEM-4D** [66] | 把「物理不落地」变成可测量的失效 | 核实其几何约束是否带来真机收益 |
| P1 | **PolaRiS** [104] | real-to-sim 评测的可扩展方案 | 核实与真机 CORRELATION，而非仅 simulator fidelity |
| P1 | **Genie Envisioner** [84] / **Genie** [89] | 生成式环境 → 操作平台 | 核实是否开源权重与数据 |
| P1 | **Causal Physics Steering / PEZ** [67] | 推理期物理可控性 | **等待第三方复现**；当前证据等级 C |
| P1 | **DreamerV3** [3] + **Nightmare Dreamer** [91] | 世界模型 RL 主线 + 安全延伸 | 核实 [91] 在安全约束下的实证收益 |
| P2 | **DiLA** [21] | 潜在动作解耦世界模型（2026 新作） | 核实与 VLA 策略的结合方式 |
| P2 | **Genesis**（种子资源） | 社区热度高但**本次无一手评测证据** | **必须**另行检索独立基准与复现报告，`> 待核实` |
| P2 | **DROID / Open X-Embodiment / SimplerEnv / RLBench / RoboArena** | 本次检索**未召回一手来源** | 列为证据缺口，需下一轮定向检索补全 |
| P2 | **SAPIEN / PyBullet / Drake** | 本次检索**未召回一手来源** | 同上，选型前必须补齐 |

---

## 参考来源

[1] The Open Ant: A Robot Platform for Reinforcement Learning Research — http://arxiv.org/abs/2607.18488v1
[2] Value Bonuses using Ensemble Errors for Exploration in Reinforcement Learning — http://arxiv.org/abs/2602.12375v1
[3] Mastering Diverse Domains through World Models — http://arxiv.org/abs/2301.04104v2
[4] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1
[5] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1
[6] LongEval at CLEF 2025: Longitudinal Evaluation of IR Model Performance — http://arxiv.org/abs/2503.08541v1
[7] Efficient Real-World Deblurring using Single Images: AIM 2025 Challenge Report — http://arxiv.org/abs/2510.12788v1
[8] VLSP 2025 MLQA-TSR Challenge: Vietnamese Multimodal Legal Question Answering on Traffic Sign Regulation — http://arxiv.org/abs/2510.20381v1
[9] NTIRE 2025 Challenge on Image Super-Resolution (x4): Methods and Results — http://arxiv.org/abs/2504.14582v3
[10] AIM 2025 Rip Current Segmentation (RipSeg) Challenge Report — http://arxiv.org/abs/2508.13401v3
[11] Learning Multimodal Transition Dynamics for Model-Based Reinforcement Learning — http://arxiv.org/abs/1705.00470v2
[12] A Real-Time Model-Based Reinforcement Learning Architecture for Robot Control — http://arxiv.org/abs/1105.1749v2
[13] The 1995 Pilot Campaign of PLANET: Searching for Microlensing Anomalies through Precise, Rapid, Round-the-Clock Monitoring — http://arxiv.org/abs/astro-ph/9807299v1
[14] Maximum Entropy Model-based Reinforcement Learning — http://arxiv.org/abs/2112.01195v1
[15] Efficient Model-Based Multi-Agent Mean-Field Reinforcement Learning — http://arxiv.org/abs/2107.04050v2
[16] Rating-based Reinforcement Learning — http://arxiv.org/abs/2307.16348v2
[17] Latent-Y: A Lab-Validated Autonomous Agent for De Novo Drug Design — http://arxiv.org/abs/2603.29727v2
[18] Latent-X: An Atom-level Frontier Model for De Novo Protein Binder Design — http://arxiv.org/abs/2507.19375v1
[19] Drug-like antibodies with low immunogenicity in human panels designed with Latent-X2 — http://arxiv.org/abs/2512.20263v1
[20] Recurrent World Models Facilitate Policy Evolution — http://arxiv.org/abs/1809.01999v1
[21] DiLA: Disentangled Latent Action World Models — http://arxiv.org/abs/2605.15725v1
[22] ETH-DS3Lab at SemEval-2018 Task 7 — http://arxiv.org/abs/1804.02042v1
[23] QCD and High Energy Interactions: Moriond 2018 Theory Summary — http://arxiv.org/abs/1806.04982v2
[24] Evaluation of an open-source implementation of the SRP-PHAT algorithm within the 2018 LOCATA challenge — http://arxiv.org/abs/1812.05901v1
[25] The AudioMOS Challenge 2025 — http://arxiv.org/abs/2509.01336v1
[26] Physics Briefing Book — http://arxiv.org/abs/1910.11775v2
[27] Physics and Technology of the Next Linear Collider — http://arxiv.org/abs/hep-ex/9605011v1
[28] Xiaomi-Robotics-1: Scaling Vision-Language-Action Models with over 100K Hours of Real-World Trajectories — http://arxiv.org/abs/2607.15330v2
[29] A Survey of Robot Manipulation in Contact — http://arxiv.org/abs/2112.01942v3
[30] Action Flow Matching for Continual Robot Learning — http://arxiv.org/abs/2504.18471v2
[31] Model-Based Capacitive Touch Sensing in Soft Robotics — http://arxiv.org/abs/2503.02280v1
[32] Scalable Aerial GNSS Localization for Marine Robots — http://arxiv.org/abs/2505.04095v2
[33] Using Physiological Measures, Gaze, and Facial Expressions to Model Human Trust in a Robot Partner — http://arxiv.org/abs/2504.05291v1
[34] Planning for robotic exploration based on forward simulation — http://arxiv.org/abs/1502.02474v2
[35] Influence of Operator Expertise on Robot Supervision and Intervention — http://arxiv.org/abs/2601.15069v2
[36] Spring-Rod System Identification via Differentiable Physics Engine — http://arxiv.org/abs/2011.04910v1
[37] Learning Velocity-based Humanoid Locomotion: Massively Parallel Learning with Brax and MJX — http://arxiv.org/abs/2407.05148v1
[38] TDCOSMO 2025: Cosmological constraints from strong lensing time delays — http://arxiv.org/abs/2506.03023v4
[39] TRUST 2025: SCRITA and RTSS @ RO-MAN 2025 — http://arxiv.org/abs/2509.11402v1
[40] Event-Enriched Image Analysis Grand Challenge at ACM Multimedia 2025 — http://arxiv.org/abs/2508.18904v1
[41] ManiSkill3: GPU Parallelized Robotics Simulation and Rendering for Generalizable Embodied AI — http://arxiv.org/abs/2410.00425v2
[42] High-level robot programming based on CAD — http://arxiv.org/abs/1309.2086v1
[43] Exploring Large Language Models to Facilitate Variable Autonomy for Human-Robot Teaming — http://arxiv.org/abs/2312.07214v3
[44] Performance Comparison on Parallel CPU and GPU Algorithms for Unified Gas-Kinetic Scheme — http://arxiv.org/abs/1810.08137v3
[45] Random number generators for massively parallel simulations on GPU — http://arxiv.org/abs/1204.6193v1
[46] Unwinding Rotations Improves User Comfort with Immersive Telepresence Robots — http://arxiv.org/abs/2201.02392v1
[47] The RobotSlang Benchmark: Dialog-guided Robot Localization and Navigation — http://arxiv.org/abs/2010.12639v1
[48] High-level programming and control for industrial robotics — http://arxiv.org/abs/1309.2093v1
[49] The Synthesis of Optimal Control Laws Using Isaacs' Method — http://arxiv.org/abs/2112.10849v2
[50] Isaac Lab: A GPU-Accelerated Simulation Framework for Multi-Modal Robot Learning — http://arxiv.org/abs/2511.04831v1
[51] Isaac Gym: High Performance GPU-Based Physics Simulation For Robot Learning — http://arxiv.org/abs/2108.10470v2
[52] Sim-to-Real Transfer for Mobile Robots with Reinforcement Learning: from NVIDIA Isaac Sim to Gazebo and Real ROS 2 Robots — http://arxiv.org/abs/2501.02902v1
[53] Sim-to-Real gap in RL: Use Case with TIAGo and Isaac Sim/Gym — http://arxiv.org/abs/2403.07091v2
[54] TacEx: GelSight Tactile Simulation in Isaac Sim — http://arxiv.org/abs/2411.04776v1
[55] Integration of the TIAGo Robot into Isaac Sim with Mecanum Drive Modeling and Learned S-Curve Velocity Profiles — http://arxiv.org/abs/2510.10273v2
[56] ISAAC Newton: Input-based Approximate Curvature for Newton's Method — http://arxiv.org/abs/2305.00604v1
[57] Federated and Transfer Learning: A Survey on Adversaries and Defense Mechanisms — http://arxiv.org/abs/2207.02337v1
[58] Bridging the Sim2Real Gap: Vision Encoder Pre-Training for Visuomotor Policy Transfer — http://arxiv.org/abs/2501.16389v2
[59] Perspectives on Sim2Real Transfer for Robotics: A Summary of the R:SS 2020 Workshop — http://arxiv.org/abs/2012.03806v1
[60] One-Shot Reinforcement Learning for Robot Navigation with Interactive Replay — http://arxiv.org/abs/1711.10137v2
[61] The Importance and the Limitations of Sim2Real for Robotic Manipulation in Precision Agriculture — http://arxiv.org/abs/2008.03983v1
[62] Robot Manipulation with GPT-6-Astra: Body Knowledge, Experience Reuse, Emergent Skills, and Sim2Real Transfer — http://arxiv.org/abs/2609.31770v1
[63] Sim2Real Transfer for Audio-Visual Navigation with Frequency-Adaptive Acoustic Field Prediction — http://arxiv.org/abs/2405.02821v2
[64] State-of-the-art in Robot Learning for Multi-Robot Collaboration: A Comprehensive Survey — http://arxiv.org/abs/2408.11822v1
[65] Sora as a World Model? A Complete Survey on Text-to-Video Generation — http://arxiv.org/abs/2403.05131v3
[66] GEM-4D: Geometry-Enhanced Video World Models for Robot Manipulation — http://arxiv.org/abs/2605.22882v4
[67] Causal Physics Steering in Video World Models via Concept Activation Vectors — http://arxiv.org/abs/2605.24322v1
[68] Simulating the Visual World with Artificial Intelligence: A Roadmap — http://arxiv.org/abs/2511.08585v4
[69] Simulating the Real World: A Unified Survey of Multimodal Generative Models — http://arxiv.org/abs/2503.04641v3
[70] Culturally Grounded Physical Commonsense Reasoning in Italian and English — http://arxiv.org/abs/2510.22631v1
[71] Augmented Reality Appendages for Robots — http://arxiv.org/abs/2205.06747v1
[72] LLM-based ambiguity detection in natural language instructions for collaborative surgical robots — http://arxiv.org/abs/2507.11525v1
[73] Improving Human Legibility in Collaborative Robot Tasks through Augmented Reality — http://arxiv.org/abs/2311.05562v1
[74] Fitted avatars: automatic skeleton adjustment for self-avatars in virtual reality — http://arxiv.org/abs/2307.09558v1
[75] Interactive Multi-User 3D Visual Analytics in Augmented Reality — http://arxiv.org/abs/2002.05305v1
[76] WorldGym: World Model as An Environment for Policy Evaluation — http://arxiv.org/abs/2506.00613v3
[77] Robot Policy Evaluation for Sim-to-Real Transfer: A Benchmarking Perspective — http://arxiv.org/abs/2508.11117v1
[78] Robot Trains Robot: Automatic Real-World Policy Adaptation and Learning for Humanoids — http://arxiv.org/abs/2508.12252v2
[79] Global Inflation After COVID-19 and Monetary-Policy Responses — https://doi.org/10.63544/ijss.v5i5.338
[80] A Simulation and Modeling of Access Points with Definition Language — http://arxiv.org/abs/1304.1836v2
[81] The Green Structural Transformation — https://doi.org/10.63544/ijss.v5i5.335
[82] Autonomous robotic surgery, surgical video and world models — https://doi.org/10.1007/s11701-026-04000-5
[83] PushT Start: Exploring Video Generation for Robot Learning — https://www.semanticscholar.org/paper/7105a46f97440aa9de04ae28ede0d48d52f2ad9c
[84] Genie Envisioner: A Unified World Foundation Platform for Robotic Manipulation — http://arxiv.org/abs/2508.05635v3
[85] AI-Driven Media Evolution — https://doi.org/10.63544/ijss.v5i2.242
[86] From Task Automation to Job Transformation — https://doi.org/10.63544/jbii.v5i9.214
[87] Neutrino-Nucleon Cross-Section Model Tuning in GENIE v3 — http://arxiv.org/abs/2104.09179v2
[88] Growth, Carbon Emissions, and Public Health Spending — https://doi.org/10.63544/jbii.v5i9.230
[89] Genie: Generative Interactive Environments — http://arxiv.org/abs/2402.15391v1
[90] Structural Transformation, Productivity Growth, and Sustainable Development — https://doi.org/10.63544/ij

---

*Generated by research-bot · topic=`embodied-world-models` · depth=`standard` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading · model=`deepseek-v4-flash` · sources=107 · duration=312s · 2026-10-05T22:41:16+00:00*
