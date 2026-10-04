# Vision-Language-Action (VLA) 基础模型调研报告

**日期**：2026-10-04（UTC） | **领域**：具身智能 / VLA 基础模型 / 机器人策略学习 | **检索源**：本次抽取提供 125 条编号来源，其中与 VLA / 机器人策略直接相关的约 45 条；另有 8 篇论文、5 个开源项目、5 个数据集来自领域种子资源（无编号，保留其原始链接） | **证据基线说明**：候选块绝大多数为 arXiv 预印本（B 级），仅少量为同行评审（A 级，如 [115]），因此本报告的量化热度（引用数 / star / 榜单数值）大多为 `> 待核实`，结论以「方向性判断 + 可核查出处」为主，不作数字外推。

---

## 摘要（Executive Summary）

1. **范式已从「VLM 直接输出动作 token」演进到「动作专家 + 生成式动作解码」**。2023 年 RT-2 证明 VLM 可通过动作 token 迁移 Web 知识 [4]；2023–2024 年 Diffusion Policy 确立扩散式动作生成范式 [24]；2025–2026 年检索到的工作则集中在 flow matching 变体 [36][87][88]、双系统（System 1/2）[41][27] 与动作 token 化接口 [72][74][75] 三条线上。

2. **近 12 个月最具体的工程化信号是「不改权重、不重训」的推理侧优化**：BLURR 作为可插拔推理 wrapper 实例化于 π0 控制器 [5]，另有以实时推理速度为题的工作 [92]（细节 `> 待核实`）。这直接回应了 VLA 推理栈过重、商品级 GPU 上难以高频控制的问题。

3. **长程任务适配出现可核查的竞赛级结果**：2025 BEHAVIOR Challenge 冠军方案在 Pi0.5 上引入 flow matching 的 correlated noise、可学习混合层注意力与 System 2 stage tracking，在 50 个长程家庭任务上取得第 1 名 [27]。但该结果**仅在 photo-realistic 仿真中评测**，不能等同于真机能力。

4. **跨本体泛化仍以「数据集 + 表征对齐」为主**：Open X-Embodiment 提供跨本体数据基石 [49]，零样本跨本体路线包括跨绘画（cross-painting）[70]、图本体 Transformer [80]、掩码末端执行器 [81]，2026 年出现受控对比研究 [82] 与驾驶域跨本体尝试 [85]；本体缩放律在运动任务上有初步探索 [65]。

5. **失败案例与争议已有实证雏形**：VLA 的「视觉压倒语言」反事实失败被系统性刻画 [90]；在统一评测协议（n=450 episodes，PushT 与 ALOHA 14-DOF 双臂）下，不同架构呈现**可预测但彼此不同的失败签名** [91]；扩散/流匹配策略的「采样轨迹的轨迹」计算开销被明确批评 [36]。

6. **可复现性环境在恶化**：2025 Foundation Model Transparency Index 显示基础模型开发者透明度平均分从 2024 年的 58 降至 2025 年的 40，训练数据与训练算力披露最差 [25]。这对 VLA 的数据/算力可比性是直接的负面外部条件。

7. **本报告的诚实边界**：候选证据中所有 VLA 相关结果均为 arXiv 预印本，缺少 RSS/CoRL/ICRA/NeurIPS 级别确认；多数条目**未提供真机成功率、任务数、推理延迟数字**；`π0`、`RT-1`、`Octo`、`ACT/ALOHA` 等经典条目来自领域种子资源而非本次检索的编号来源，其量化热度一律标注 `> 待核实`。

---

## 一、关键前沿进展（近 12–24 个月）

> 筛选口径：仅采用与 VLA 动作策略直接相关的条目。本次检索中的噪声项已剔除并在文末说明，例如短视频参与度预测 [26]、机器生成文本检测 [1]、对话机器人竞赛 [17]、GitHub 仓库内容实证研究 [118][124] 等。

| 进展 | 时间 / 机构 | 一句话贡献 | 热度证据 | 权威证据 | 关注度 | 推荐度 |
|---|---|---|---|---|---|---|
| **BEHAVIOR 2025 冠军：VLA 长程任务适配** [27] | 2025，arXiv:2512.06951v2 | 在 Pi0.5 上做长程双臂操作适配：flow matching 的 correlated noise、可学习混合层注意力、System 2 stage tracking 消解任务歧义；训练用 multi-sample flow matching 降方差，推理用动作压缩 | `> 待核实`（候选块未给引用数） | arXiv 预印本（cs.RO），**非同行评审**；权威性来自 2025 BEHAVIOR Challenge 官方第 1 名 | 中 —— 依据：大规模长程具身基准的冠军方案具社区话题性，但无量化热度信号 | ★★★★☆ —— 与本主题架构/训练范式最相关且带可核查竞赛排名；但仅仿真验证 |
| **BLURR：VLA 低资源推理 wrapper** [5] | 2025，arXiv:2512.11769v1 | 可插入既有 VLA 控制器的轻量推理层，实例化于 π0，**不需重训、不改 checkpoint** | `> 待核实` | arXiv 预印本（cs.RO），非同行评审；未见官方仓库 | 低 —— 依据：仅摘要级信息，无引用/star 信号 | ★★★☆☆ —— 对真机部署可用性直接相关，但缺延迟与成功率数字 |
| **VLA 实时推理** [92] | 2025，arXiv:2510.26742v1 | 以「让 VLA 跑到实时速度」为题 | `> 待核实` | arXiv 预印本；候选块**仅有标题级证据** | `> 待核实` —— 依据：候选块未提供摘要与热度信号 | ★★☆☆☆ —— 主题重要但证据不足，需取全文 |
| **推理期注意力干预（驾驶 VLA）** [2] | 2026，arXiv:2608.17095v1 | 对视觉 token 施加有界加性 pre-softmax 注意力偏置（前向 pre-hook，不改权重），把注意力导向安全关键交通参与者；在 Alpamayo-R1 的 Qwen3-VL backbone 上，50 个换道场景呈单调剂量响应，平均位移约 17 cm，clamp 处横向偏移可达约 140 cm | `> 待核实` | arXiv 预印本（cs.CV），非同行评审，**无第三方复现** | 低 —— 依据：无引用/榜单信号 | ★★★☆☆ —— 方向新颖（推理期可控性），但样本仅 50 个合成场景 |
| **VLA 已有的路径偏差检测注意力头** [6] | 2026，arXiv:2603.13782v1 | 指出 VLA 导航模型内部已存在可复用的注意力头用于路径偏差检测，以缓解视觉推理幻觉 | `> 待核实` | arXiv 预印本（cs.RO） | 低 —— 依据：候选块仅摘要片段 | ★★★☆☆ —— 与「免训练探针」思路相关，细节待核实 |
| **ART：把 VLA 变成会用工具的 Agent** [8] | 2026，arXiv:2608.14047v3 | 工具注入框架，调优任意 VLA 以调用现成工具模块（低层视觉、高层 affordance、本体增强） | `> 待核实` | arXiv 预印本（cs.RO） | 低 —— 依据：无量化热度信号 | ★★★☆☆ —— 代表 VLA→Agent 化的接口扩展方向 |
| **Xiaomi-Robotics-1：10 万小时级真机轨迹** [10] | 2026，arXiv:2607.15330v2 | 以 >100K 小时真机轨迹扩展 VLA，支持未见环境下的移动操作零样本开箱与少量微调下游适配 | `> 待核实` | arXiv 预印本（cs.RO）；自述性质 | 中 —— 依据：数据规模量级在本次候选中最高，但无第三方验证 | ★★★★☆ —— 若数据规模与结论可核实，是「数据规模化」路线的关键样本 |
| **动作 token 化新一批工作** [72][74][75] | 2026，arXiv:2609.27513 / 2610.00899 / 2607.21670 | 分别从行为对齐、随机性建模（TOAST，对 FAST 的改进）与有序 token 化角度改造自回归动作表示 | `> 待核实` | 均为 arXiv 预印本（cs.RO） | 低 —— 依据：候选块无引用数 | ★★★☆☆ —— 统一动作空间的关键接口层，值得跟读 |
| **CLAM：无标注演示的连续隐动作模型** [76] | 2025，arXiv:2505.04999v2 | 从无标注演示中学习连续隐动作，缓解动作标注瓶颈 | `> 待核实` | arXiv 预印本 | 低 —— 依据：无热度信号 | ★★★☆☆ —— 与跨本体动作空间统一问题直接相关 |
| **几何/物理一致性路线** [73][20][21][87] | 2026 / 2025 | Geometric Action Model 强调 3D 物理交互推理 [73]；RealD²iff 用深度扩散弥合视觉 sim2real 差距 [20]；运动学感知扩散策略统一 3D 观测与动作空间 [21]；affordance + flow matching [87] | `> 待核实` | 均为 arXiv 预印本（cs.RO） | 低 —— 依据：候选块无量化热度 | ★★★☆☆ —— 对「仿真 SOTA ≠ 真机 SOTA」的差距提供了部分技术回应 |
| **效率与小模型** [95][105] | 2025 / 2025 | VLA-Adapter 提出 tiny-scale VLA 范式 [95]；[105] 聚焦 VLA 微调的速度与成功率权衡 | `> 待核实` | arXiv 预印本 | 低 —— 依据：无引用/star 信号 | ★★★☆☆ —— 与推理频率、部署成本议题相关 |
| **运动图像联合学习** [93] | 2025，arXiv:2512.18007v1 | 让 VLA 与运动图像扩散联合学习以获益 | `> 待核实` | arXiv 预印本 | 低 | ★★☆☆☆ —— 仅标题级证据，需核实 |
| **人形与链式动作推理** [44] | 2025，arXiv:2504.09532v3 | 多模态基础模型 + 具身 chain-of-action 推理实现零样本 loco-manipulation | `> 待核实` | arXiv 预印本 | 低 | ★★☆☆☆ —— 与人形 VLA 相关，细节待核实 |
| **领域外延：驾驶 / 空中 / 实验室 / 装配** [106][97][94][100][3] | 2025–2026 | Impromptu VLA 面向驾驶 corner case 并开放权重与数据 [106]；SafeAlign-VLA 做风险感知对齐 [97]；AeroManip-VLA 用 RL 生成演示做空中操作 [94]；BioProVLA-Agent 面向生物实验室操作 [100]；CCFT 把装配动作分解为 Verb/Object/Tool 语义元素微调 VLM [3] | `> 待核实` | 均为 arXiv 预印本 | 低 —— 依据：候选块多为摘要级，无热度量化 | ★★☆☆☆ / ★★★☆☆ —— 说明 VLA 正在横向铺开到非桌面域，但各自成熟度待核实 |
| **基础模型透明度下滑（背景性）** [25] | 2025，arXiv:2512.10169v1 | 2025 FMTI 第三版：平均分由 2024 年 58 降至 2025 年 40；训练数据、训练算力、部署后使用与影响最不透明；首次评估 Alibaba、DeepSeek、xAI | `> 待核实`（候选块未给引用/下载） | arXiv 预印本（cs.AI），作者含 Percy Liang、Rishi Bommasani 等知名研究者，**非同行评审** | 中 —— 依据：连续年度指数，具政策与社区关注度 | ★★★☆☆ —— 非 VLA 专属，但为评估 VLA 数据/算力披露与可复现性提供旁证 |
| **方向综述与工程化反思** [28][33][30] | 2025–2026 | [28] 具身操作 VLA 综述；[33] 从基础模型到应用的实践改进；[30] 自称 pragmatic VLA foundation model | `> 待核实` | arXiv 预印本；[30][33] 候选块仅标题/片段 | 中 —— 依据：方向综述通常被用作入口，但无引用数 | ★★★☆☆ —— 适合作为分类骨架，需注意综述时效 |

**本节小结（含待核实项）**：近 12–24 个月的实质性变化集中在**推理侧工程化**（[5][92]）、**长程任务适配范式**（[27]）、**动作接口重构**（[72][74][75][76]）与**失败模式实证**（[90][91]）。所有条目均缺同行评审确认与真机第三方复现；「提升来自数据、架构还是算力」在本次证据中**无法归因** `> 待核实`。

---

## 二、方法范式对比（离散动作 / 扩散 / Flow Matching / 双系统）

| 范式 | 代表工作 | 动作生成机制与特点 | 热度证据 | 权威证据 | 关注度 | 推荐度 |
|---|---|---|---|---|---|---|
| **离散动作 token（自回归）** | RT-2 [4]、OpenVLA [104][110]、TOAST [74]、Ordered Action Tokens [75]、Behavior-Aligned Action Tokenization [72] | 连续动作离散化为 token，用标准 next-token 目标预测；可直接复用 VLM 权重与 Web 先验，但 token 序列长度与动作精度存在张力，需要在 tokenizer 设计上做补偿 | `> 待核实`（[104][110] 候选块未给引用/star） | [4] arXiv 预印本；[104][110] arXiv 预印本（官方开源模型） | 高 —— 依据：本次候选中多篇工作直接以 OpenVLA 为微调/基线对象（[107] 以 OpenVLA 为微调对象，[105] 讨论 VLA 微调速度与成功率） | ★★★★★ —— 工程可复现性最高的一条线，OpenVLA 是事实基线 |
| **扩散策略（Diffusion Policy）** | Diffusion Policy [24]、DPPO [23]、RealD²iff [20]、Kinematics-Aware Diffusion Policy [21] | 把动作序列生成建模为去噪过程，天然表达多模态动作分布；代价是采样需多步迭代，推理成本高 | `> 待核实` | [24] arXiv 预印本（原始论文）；[23][20][21] arXiv 预印本 | 高 —— 依据：[91] 在统一评测协议（n=450 episodes）中把 Diffusion Policy 列为被评测架构；[23] 为其策略优化后续工作 | ★★★★★ —— 理解多模态动作建模的必修项，也是被反复对标的基线 |
| **Flow Matching** | Streaming Flow Policy [36]、FlowPolicy [88]、Affordance-based + Flow Matching [87]、BEHAVIOR 冠军的 correlated noise flow matching [27] | 把动作轨迹本身当作流轨迹来积分，目标是在保留多模态表达能力的同时压缩采样开销；[27] 进一步在噪声相关性与方差上做文章（multi-sample flow matching 降方差、correlation-aware inpainting） | `> 待核实` | 均为 arXiv 预印本（cs.RO） | 中 —— 依据：[36] 直接批评扩散/流匹配「采样轨迹的轨迹」的计算开销，属路线内的自我批判信号；[27] 带竞赛第 1 名 | ★★★★☆ —— 当前最活跃的动作生成路线，[27] 提供了可核查的训练细节 |
| **双系统 / System 1–System 2** | GR00T N1 [41]、BEHAVIOR 冠军的 System 2 stage tracking [27]、ART 工具调用 [8] | 高层语义/任务分解（慢思考）与低层高频动作（快执行）分工；[27] 用 stage tracking 消解长程任务歧义，[8] 用工具注入扩展能力边界 | `> 待核实` | [41] arXiv 预印本（**官方开源**人形基础模型）；[27][8] arXiv 预印本 | 中 —— 依据：[41] 标题即宣称 open foundation model，开源属性带来关注；但 star/引用数候选块未提供 | ★★★★☆ —— 与长程任务和推理频率两个痛点同时相关 |

**路线间的争议点（据现有证据）**

- **采样成本 vs 表达力**：[36] 明确指出扩散/流匹配策略「采样的是轨迹的轨迹」，丢弃中间信息、计算昂贵 [36]；[88] 走 consistency flow matching 以加速 [88]。哪个方向胜出在本次证据中 `> 待核实`。
- **离散 vs 连续**：2026 年集中出现多篇动作 token 化改进（[72][74][75]）与连续隐动作 [76]，说明「统一动作空间」尚未收敛。
- **架构相关的失败不对称**：在相同评测协议下，VQ-BeT、Diffusion Policy、ACT 呈现不同的失败签名（如方向反转率差异），意味着**不能用单一失败模式概括"VLA 失败"** [91]。
- **仿真冠军的外推风险**：[27] 的第 1 名成绩限于 photo-realistic 仿真与 50 个长程家庭任务，真机成功率 `> 待核实`。

---

## 三、经典与奠基性工作

> 说明：`[链接]` 列可直接点击。标注「种子资源」的条目来自本领域人工维护的种子清单，**未在本次 125 条编号来源中出现**，其量化热度一律 `> 待核实`，切勿当作本次实时检索所得。

| 名称 | 年份 | 机构 / 作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| **RT-2: Vision-Language-Action Models** [4] | 2023 | Google DeepMind | `> 待核实` | arXiv 预印本（cs.RO），非同行评审但为该方向公认起点 [4] | 高（定性）—— 依据：VLA 术语与「VLM 输出动作 token」范式由其确立，本次检索的后续工作均在此范式下讨论（如 [105][107][90] 均针对 VLA 微调/泛化/失败）；量化热度 `> 待核实` | ★★★★★ —— 定义 VLA 范式的必读奠基作 | http://arxiv.org/abs/2307.15818v1 | 把 Web 知识迁移到机器人控制，涌现泛化 |
| **Diffusion Policy** [24] | 2023 | Columbia / Toyota | `> 待核实` | arXiv 预印本；官方开源实现 | 高 —— 依据：[91] 将其列为统一评测协议下的被评测架构之一，[23] 为其后续策略优化工作 | ★★★★★ —— 扩散式动作生成的奠基作，理解多模态动作分布必读 | https://arxiv.org/abs/2303.04137 | Visuomotor policy learning via action diffusion |
| **Open X-Embodiment (OXE) / RT-X** [49] | 2023 | Open X-Embodiment Collaboration | `> 待核实` | arXiv 预印本；官方项目主页（种子资源） | 高 —— 依据：跨本体 VLA 的标准数据源，本次跨本体子问题的条目均围绕同类问题（[65][70][80][82]）；量化热度 `> 待核实` | ★★★★★ —— 跨本体训练的公共基座 | http://arxiv.org/abs/2310.08864v9 | 跨本体大规模数据集与 RT-X 模型 |
| **DROID** [53] | 2024 | 多机构协作 | `> 待核实` | arXiv 预印本；官方数据集主页（种子资源） | 中高 —— 依据：in-the-wild 真机操作的规模化数据代表，本次数据集子问题中被明确召回 [53] | ★★★★☆ —— 真机数据多样性的关键来源 | http://arxiv.org/abs/2403.12945v2 | 大规模 in-the-wild 机器人操作数据集 |
| **LIBERO** [59] | 2023 | 学术机构 | `> 待核实` | arXiv 预印本；官方项目页（种子资源） | 中高 —— 依据：终身学习操作基准，本次数据/基准子问题中被明确召回 [59] | ★★★★☆ —— 知识迁移与终身学习评测的标准入口 | http://arxiv.org/abs/2306.03310v2 | Benchmarking knowledge transfer for lifelong robot learning |
| **OpenVLA** [104][110] | 2024 | Stanford 等 | `> 待核实`（候选块未给 star/引用） | arXiv 预印本 + 官方 GitHub（种子资源）；**开放权重** | 高 —— 依据：本次候选中多篇工作以 OpenVLA 为微调对象或改进目标（[107][105]） | ★★★★★ —— 最被广泛使用的开源 VLA 基线 | http://arxiv.org/abs/2406.09246v3 | 7B 开源 VLA，生态基线 |
| **GR00T N1** [41] | 2025 | NVIDIA | `> 待核实` | arXiv 预印本，标题即宣称 **open** foundation model for generalist humanoid robots [41] | 中 —— 依据：人形方向的开源基础模型，属关注焦点；star/引用数 `> 待核实` | ★★★★☆ —— 人形 + 开源 + 双系统设计的代表性节点 | http://arxiv.org/abs/2503.14734v2 | 通用人形机器人开放基础模型 |
| **Mirage: Cross-Embodiment Zero-Shot Transfer** [70] | 2024 | 学术机构 | `> 待核实` | arXiv 预印本（cs.RO） | 中 —— 依据：跨本体零样本迁移的代表路线之一（cross-painting） | ★★★★☆ —— 跨本体零样本迁移的关键思路 | http://arxiv.org/abs/2402.19249v3 | 用 cross-painting 弥合本体差异 |
| **GET-Zero** [80] | 2024 | 学术机构 | `> 待核实` | arXiv 预印本（cs.RO） | 中 —— 依据：以图本体 Transformer 做零样本本体泛化，属该议题代表工作 | ★★★☆☆ —— 本体表征建模的可参考设计 | http://arxiv.org/abs/2407.15002v2 | Graph Embodiment Transformer |
| **CLAM** [76] | 2025 | 学术机构 | `> 待核实` | arXiv 预印本 | 低 —— 依据：候选块无热度信号 | ★★★☆☆ —— 连续隐动作学习，绕开动作标注 | http://arxiv.org/abs/2505.04999v2 | 从无标注演示学连续隐动作 |
| **Open-Ended Learning Leads to Generally Capable Agents** [50] | 2021 | DeepMind | `> 待核实` | arXiv 预印本 | 中 —— 依据：通用能力智能体的开放端学习前身，常被引为「通用具身体」思想来源；量化热度 `> 待核实` | ★★★☆☆ —— 理解「通用具身体」目标的历史脉络 | http://arxiv.org/abs/2107.12808v2 | 开放端学习得到通用能力智能体 |
| **RT-1**（种子资源） | 2022 | Google Research | `> 待核实`（本次未检索到对应编号） | 领域种子资源，未在本次编号来源中 | `> 待核实` —— 依据：无实时检索热度数据 | ★★★★☆ —— 大规模真机 Transformer 模仿学习先驱 | https://arxiv.org/abs/2212.06817 | 大规模真机模仿学习 |
| **Octo**（种子资源） | 2024 | UC Berkeley | `> 待核实` | 领域种子资源，未在本次编号来源中；有官方开源仓库 | `> 待核实` | ★★★★☆ —— 开源通用策略、灵活观测/动作头，常作轻量基线 | https://arxiv.org/abs/2405.12213 | 开源通用机器人策略 |
| **π0**（种子资源） | 2024 | Physical Intelligence | `> 待核实`（[5][27] 提及 π0/Pi0.5 作为基座，但未给引用数） | 种子资源 + 开源实现（openpi）；本次仅由 [5][27] 间接印证其被广泛用作基座 | 中高 —— 依据：[5] 在 π0 上实例化推理 wrapper，[27] 在 Pi0.5 上做适配，说明其作为基座被反复采用 | ★★★★★ —— flow matching 动作专家 + 跨本体的关键基座 | https://arxiv.org/abs/2410.24164 | flow matching 动作专家，跨本体 |
| **ACT / ALOHA**（种子资源） | 2023 | Stanford | `> 待核实` | 种子资源；有官方硬件与代码仓库 | 中 —— 依据：[91] 把 ACT 纳入统一评测协议的被评测架构之一 | ★★★★★ —— 低成本双臂操作与动作分块（action chunking）的事实标准 | https://arxiv.org/abs/2304.13705 | 低成本双臂遥操作 + ACT |
| **One-Shot RL for Robot Navigation** [34] | 2017 | 学术机构 | `> 待核实` | arXiv 预印本 | 低 —— 依据：2017 年工作，被本次数据集/基准子问题误召回，与 VLA 无直接关系 | ★★☆☆☆ —— 仅作为「真实世界交互成本高」这一动机的历史注脚 | http://arxiv.org/abs/1711.10137v2 | 交互式回放的单样本 RL 导航 |
| **Deception Game: 安全-学习闭环** [52] | 2023 | 学术机构 | `> 待核实` | arXiv 预印本 | 低 | ★★☆☆☆ —— 交互式机器人自主性的安全议题旁证 | http://arxiv.org/abs/2309.01267v2 | 人机交互中的安全-学习闭环 |

---

## 四、开源项目与工程实践

> 关键结论：**本次候选证据中没有任何一条给出 VLA 与 ROS2（rclpy / ros2_control / DDS 中间件）集成的官方文档或代码链接**，因此「VLA 如何与 ROS2 及现有控制栈集成」在本次调研中属**证据缺口**，详见本节末尾。

| 项目 | 年份 | 机构 / 维护方 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| **openvla/openvla** | 2024 | 官方团队 | `> 待核实`（star 未取到） | 官方 GitHub 仓库（种子资源）+ 论文 [104][110] | 高 —— 依据：[107] 明确以 OpenVLA 为微调对象，[105] 讨论其微调效率，生态使用面最广 | ★★★★★ —— 上手 VLA 的首选开源实现与权重 | https://github.com/openvla/openvla | OpenVLA 官方实现与权重 |
| **Physical-Intelligence/openpi** | 2024–2025 | Physical Intelligence | `> 待核实` | 官方 GitHub 仓库（种子资源）；[5][27] 间接印证 π0/Pi0.5 作为基座被使用 | 中高 —— 依据：多个候选工作以其为基座（[5][27]），但 star 数据 `> 待核实` | ★★★★★ —— π0 系列开源实现，流匹配路线的最佳入口 | https://github.com/Physical-Intelligence/openpi | π0 系列开源实现 |
| **octo-models/octo** | 2024 | UC Berkeley | `> 待核实` | 官方 GitHub 仓库（种子资源） | 中 —— 依据：通用策略开源实现，常作轻量基线；量化热度 `> 待核实` | ★★★★☆ —— 观测/动作头灵活，适合做架构消融 | https://github.com/octo-models/octo | Octo 通用策略 |
| **tonyzhaozh/aloha** | 2023 | Stanford | `> 待核实` | 官方 GitHub 仓库（种子资源，含硬件清单） | 中 —— 依据：[91] 使用 ALOHA 14-DOF 双臂设置做统一评测，说明其仍是主流真机平台 | ★★★★★ —— 真机双臂实验的硬件与代码基准 | https://github.com/tonyzhaozh/aloha | ALOHA / ACT 硬件与代码 |
| **real-stanford/diffusion_policy** | 2023 | Stanford / Columbia | `> 待核实` | 官方 GitHub 仓库（种子资源）+ 论文 [24] | 高 —— 依据：[23] 为其策略优化后续，[91] 以其为被评测架构之一 | ★★★★★ —— 扩散策略的标准实现 | https://github.com/real-stanford/diffusion_policy | Diffusion Policy 官方实现 |
| **RealMirror** [121] | 2025 | 学术机构 | `> 待核实` | arXiv 预印本（自述 open-source 平台） | 低 —— 依据：候选块无 star/引用 | ★★★☆☆ —— 声称提供端到端 VLA 开源平台，适合做仿真-真机流程参考 | https://arxiv.org/abs/2509.14687 | 面向具身智能的综合性开源 VLA 平台 |
| **VLA-Arena** [112] | 2025 | 学术机构 | **citations=35** [112] | arXiv（候选块 authority 记为 arXiv.org），非同行评审；

## 五、数据集与评测基准

VLA 的数据与评测生态可粗分为三层：**跨本体预训练语料**（OXE、DROID、BridgeData V2）、**终身/多任务操作基准**（LIBERO）、以及**仿真复现与压力测试基准**（SimplerEnv、VLA-Arena、BEHAVIOR Challenge）；此外还有面向垂直场景的新数据集（Impromptu VLA 驾驶数据）。下表汇总可核查条目；凡候选块未给出引用数/star 的，一律标 `> 待核实`，不作数字推测。

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Open X-Embodiment (OXE) | 2023 | Open X-Embodiment Collaboration | `> 待核实`（候选块未提供引用数）[49] | arXiv 预印本 cs.RO [49]；种子资源列为跨本体核心数据集 | 高 + 依据：被作为跨本体预训练与 RT-X 的通用参照基座，但无量化热度数据 [49] | ★★★★★ + 跨本体 VLA 预训练的事实参照，必读 | http://arxiv.org/abs/2310.08864v9 | 多本体大规模数据集与 RT-X 模型，22 种本体、100 万+ episodes（种子资源说明） |
| DROID | 2024 | DROID 团队 | `> 待核实`（候选块未提供引用数）[53] | arXiv 预印本 cs.RO [53] | 中 + 依据：定位为"in-the-wild"真机操作数据，是评估真机泛化的常用语料，但无量化热度 [53] | ★★★★☆ + 真机多样性语料，适合检验跨场景泛化 | http://arxiv.org/abs/2403.12945v2 | 分布式采集的大规模真机操作数据集 |
| LIBERO | 2023 | LIBERO 团队 | `> 待核实` [59] | arXiv 预印本 [59] | 中 + 依据：终身机器人学习基准，被长期用于知识迁移评测，但候选块无引用数 [59] | ★★★★☆ + 研究"终身学习/遗忘"时的标准选择 | http://arxiv.org/abs/2306.03310v2 | 终身学习操作基准；与灾难性遗忘研究配套 [62] |
| VLA-Arena | 2025 | VLA-Arena 团队 | citations=35 [112] | arXiv.org（预印本平台，非会议页面）[112] | 中 + 依据：citations=35，是本表中唯一给出量化热度的条目 [112] | ★★★★☆ + 明确以"能力边界与失败模式"为目标的评测框架，契合本主题 | https://arxiv.org/abs/2512.22539 | 结构化任务设计的开源 VLA 基准，目标量化能力边界与 failure modes [112] |
| BEHAVIOR Challenge（2025 赛题） | 2025 | BEHAVIOR 组织方（经冠军方案转述） | `> 待核实` [27] | 竞赛官方基准，但本报告仅能经 arXiv 预印本转述 [27] | 中 + 依据：长程双臂家庭任务大规模基准，具竞赛社区话题性 [27] | ★★★★☆ + 目前唯一被候选证据明确引用的长程双臂 VLA 评测平台，但需核实官网与榜单 | http://arxiv.org/abs/2512.06951v2 | 50 个长程家庭任务、photo-realistic 仿真，含双臂操作+导航+上下文决策 [27] |
| Impromptu VLA Dataset | 2025 | Impromptu VLA 团队 | `> 待核实` [106] | arXiv 预印本 cs.CV [106] | 中 + 依据：面向自动驾驶 corner case 的开放权重与开放数据，属驾驶 VLA 细分生态 [106] | ★★★☆☆ + 若关注驾驶 VLA 才优先；与操作类 VLA 相关性中等 | http://arxiv.org/abs/2505.23757v1 | 论文自述 80,000+ 精心整理样本，面向非结构化 corner case [106] |
| SimplerEnv | — | 种子资源（real-stanford 生态） | `> 待核实`（引用编号缺失） | `> 待核实`：种子资源链接，未在可引用来源列表中获得编号 | `> 待核实` | ★★★★☆ + 仿真复现真机策略评测的关键工具，但本报告未能给出编号级证据 | https://simpler-env.github.io/ | 用仿真复现真机策略评测，缓解真机评测成本（种子资源说明） |
| BridgeData V2 | — | 种子资源（RAIL Berkeley） | `> 待核实`（引用编号缺失） | `> 待核实`：种子资源链接，未在可引用来源列表中获得编号 | `> 待核实` | ★★★☆☆ + 多场景桌面操作语料，作为补充数据源 | https://rail-berkeley.github.io/bridgedata/ | 多场景桌面操作数据（种子资源说明） |

**评测口径的三个结构性缺口（可核查）**

1. **仿真 vs 真机口径不统一。** 专门的讨论指出，当前基于视觉的机器人仿真基准虽推动了操作研究，但真实世界评测（尤其是泛化策略）明显滞后 [32]；本报告中最具规模的 VLA 结果（BEHAVIOR 冠军方案）本身也是仿真评测 [27]。
2. **可比性受数据/算力披露限制。** 2025 Foundation Model Transparency Index 显示基础模型开发者透明度平均分由 2024 年的 58 降至 2025 年的 40，训练数据与训练算力最不透明 [25]；这直接削弱"提升来自数据、架构还是算力"的归因能力（与第七节 Watchlist 呼应）。
3. **跨本体覆盖度参差。** OXE 以多本体为卖点 [49]，而 BEHAVIOR 等长程基准以单一人形/双臂平台为主 [27]，两者结论不可直接互换。

> 本章热度轴的绝大多数条目为 `> 待核实`：候选块仅对 VLA-Arena 给出 citations=35 [112]，其余数据集均无引用数、star 或下载量数据；本报告不作补全性推测。

---

## 六、跨本体泛化与真机部署的开放问题

### 6.1 跨本体泛化：三条技术路线与各自证据强度

**路线 A：以数据规模换本体泛化（scaling 视角）。** 有工作明确提出"本体缩放律"（embodiment scaling laws）假设，并系统检验"增加训练本体数量是否提升对未见本体的泛化"，同时承认其使能因素仍理解不足 [65]。小标题级别的一手证据，但候选块仅给出摘要级信息，缺少本体数量—性能曲线的具体数字 `> 待核实` [65]。Xiaomi-Robotics-1 则从数据侧给出另一极：以"over 100K Hours of Real-World Trajectories"为标题自述进行规模化，并声称可零样本执行未见环境中的移动操作、且可用少量微调适配新任务（均为论文自述，无第三方复现）[10]。**结论强度：中低。** 两条证据都指向"规模有效"，但都属预印本自述 [10][65]。

**路线 B：以表征/几何对齐实现零样本跨本体迁移。** 这一路线的代表包括：跨本体零样本策略迁移的 cross-painting 思路 [70]、面向零样本本体泛化的图本体 Transformer（GET-Zero）[80]、通过"从 VLA 中屏蔽末端执行器"实现零样本跨本体操作（Cloak）[81]、面向桌面操作的零样本跨本体 VLA 迁移受控研究（ZETA）[82]，以及面向驾驶 VLA 的跨本体零样本迁移 [85]。**价值与争议**：ZETA 以"controlled study"自居 [82]，是本主题中最接近"可复现对比"的形态；但候选块未提供各方法的任务数、本体数与成功率，横向可比性 `> 待核实` [70][80][81][82][85]。

**路线 C：统一动作空间 / 动作 tokenization。** 一批 2026 年工作集中攻击"连续动作如何离散化"这一接口问题：Behavior-Aligned Action Tokenization 强调跨演示的行为对应关系监督不足 [72]；Geometric Action Model 主张在 3D 物理世界中推理物体—相机—动作交互 [73]；TOAST 针对自回归 VLA 提出随机动作 tokenization，并明确以 FAST 为改进基线 [74]；Ordered Action Tokens 指出现有方法要么序列过长、要么潜表征缺乏可解释性 [75]；CLAM 则走连续潜动作路线，从未标注演示中学习 [76]。**判断**：动作空间统一是当前跨本体最"卷"的工程切口，但除摘要外无统一 benchmark 上的横向数字，无法判断哪条路线占优 `> 待核实` [72][73][74][75][76]。

### 6.2 真机部署：四个被反复点名但尚未闭合的问题

1. **推理频率 vs 控制带宽。** "Running VLAs at Real-time Speed"直接以实时速度为标题命题 [92]；BLURR 则把问题定义为"推理栈过重、商品级 GPU 上难以高频控制或跑 Web 演示"，并给出"不重训、不改 checkpoint 的插入式 wrapper"方案，实例化于 π0（pi-zero）控制器 [5]。两者都指出瓶颈，但候选块未提供延迟毫秒数、控制频率或真机成功率 `> 待核实` [5][92]。
2. **语言跟随的崩塌（counterfactual failure）。** 有工作指出：当指令缺乏强场景监督时，VLA 会"基于视觉而非语言"行动，即 vision overrides language，并尝试评估与缓解该失效模式 [90]。这说明"跨本体可用"不等于"指令可控"。
3. **失效模式与架构强相关。** 一项在黑盒动作层面监控 VLA 的研究，在相同评测协议下（n=450 episodes，覆盖 PushT 与 ALOHA 14-DOF 双臂）比较 VQ-BeT、Diffusion Policy、ACT，报告"方向反转率"等指标在不同架构间存在可预测的差异 [91]。**这是本主题中少见的、给出明确实验规模（n=450）的失效分析** [91]，但仍是预印本，无第三方复核 `> 待核实`。
4. **工具化/系统化的补偿路线。** ART 提出把端到端 VLA 改造为可"on-the-fly tool-use"的智能体，注入现成工具模块以补足底层视觉、高层可操作性（affordance）与本体增强 [8]；AeroManip-VLA 把 VLA 扩展到空中操作，并用 RL 生成示教以缓解数据稀缺 [94]；BioProVLA-Agent 面向生物实验室的多智能体闭环操作 [100]；有工程侧工作则直接讨论开源机械臂上 VLA 基础模型的微调与部署 [115]。**趋势判断**：当端到端单体能力不足时，社区正以"外挂工具/外挂模块"绕过本体与技能瓶颈，但这也削弱了"单一基础模型"的叙事 [8][94][100][115]。

### 6.3 争议点（明确列出分歧，而非掩盖）

- **扩散策略 vs 流匹配（flow matching）。** Streaming Flow Policy 直接批评扩散/流匹配策略"采样的是轨迹的轨迹"（a diffusion/flow trajectory of action trajectories）、丢弃中间量、计算昂贵，并主张把动作轨迹当作流轨迹以简化 [36]；而被广泛引用的 Diffusion Policy 仍是扩散式动作生成的奠基性表述 [24]。二者并非简单替代关系，效率—多模态建模能力的权衡尚无公认结论 `> 待核实` [24][36]。相关方向还有一致性流匹配用于快速 3D 流策略（FlowPolicy）[88] 与 affordance + flow matching [87]。
- **双系统（System 1/System 2）的实际收益未定。** BEHAVIOR 冠军方案在 Pi0.5 基座上引入 System 2 阶段追踪（stage tracking）以消解任务歧义 [27]，可视为"分层/双系统"在长程任务上有效的单一强证据；但该结论仅来自一场仿真竞赛的头名方案，且为参赛方自述，缺少受控消融之外的独立复现 `> 待核实` [27]。
- **跨本体"通用 VLA"的宣称强度。** 标题层面的"pragmatic VLA foundation model"[30]与"From Foundation to Application: Improving VLA Models in Practice"[33]反映了从基础模型向落地迁移的叙事，但候选块未提供可比较的成功率矩阵 `> 待核实` [30][33]。

> **本章证据总评**：跨本体与真机部署两个子方向的高等级（A 级）证据在本轮候选块中几乎缺席——全部为 arXiv 预印本，且"真机成功率 / 任务数 / 本体数"三要素大多缺失，故本章多处结论只能以"研究方向"而非"已验证结论"陈述。

---

## 七、建议关注清单（Watchlist）

以下条目按"与 VLA 基础模型核心议题的相关性 × 可追踪性"排序；热度缺失一律标 `> 待核实`，不补数字。

1. **π0 / Pi0.5 系列的架构与推理优化线**：以 π0 控制器为实例化对象的推理封装工作（BLURR，不重训、不改权重）[5]，以及在 Pi0.5 上做长程双臂适配的竞赛方案（correlated noise flow matching + 混合层注意力 + System 2 stage tracking）[27]。
   — 热度 `> 待核实`；权威：arXiv 预印本、非同行评审 [5][27]；关注度：中（长程基准冠军方案具社区话题性，但无量化热度）[27]；推荐度 ★★★★☆ — 唯一同时触碰"架构改动"与"长程真机级任务"的可核查线索，但需第三方复现。
2. **实时推理与部署工程**：Running VLAs at Real-time Speed [92] + BLURR [5]。
   — 热度 `> 待核实`；权威：arXiv 预印本 [5][92]；关注度：中（"能否高频控制"是落地第一道门槛）[5][92]；推荐度 ★★★★☆ — 部署可行性判断的起点，但缺延迟/频率数字，`> 待核实`。
3. **动作 tokenization / 统一动作空间**：TOAST [74]、Ordered Action Tokens [75]、Behavior-Aligned Action Tokenization [72]、Geometric Action Model [73]、CLAM（连续潜动作）[76]。
   — 热度 `> 待核实`；权威：均为 arXiv 预印本 cs.RO [72][73][74][75][76]；关注度：中高（2026 年集中出现，说明社区已把它视为跨本体的接口瓶颈）[72][73][74][75][76]；推荐度 ★★★★☆ — 跨本体泛化的"最后一公里"接口，值得持续跟踪但须警惕同质化。
4. **零样本跨本体迁移的受控研究**：ZETA（受控对比，桌面操作）[82]、Cloak（屏蔽末端执行器）[81]、GET-Zero（图本体 Transformer）[80]、Mirage（cross-painting）[70]。
   — 热度 `> 待核实`；权威：arXiv 预印本 [70][80][81][82]；关注度：中 [70][80][81][82]；推荐度 ★★★★☆ — 若要做"跨本体到底行不行"的判断，这组是最直接的证据候选。
5. **本体缩放律与数据规模化**：Towards Embodiment Scaling Laws in Robot Locomotion [65]、Xiaomi-Robotics-1（自述 100K+ 小时真机轨迹）[10]。
   — 热度 `> 待核实`；权威：arXiv 预印本 [10][65]；关注度：中（"要多少本体/多少数据"是立项必答题）[10][65]；推荐度 ★★★★☆ — 直接关系数据预算与采集策略。
6. **失效分析与安全**：How VLAs Fail Differently（n=450 episodes，架构特异失效签名）[91]、When Vision Overrides Language（反事实失效）[90]、SafeAlign-VLA（风险感知驾驶安全对齐）[97]。
   — 热度 `> 待核实`；权威：arXiv 预印本 [90][91][97]；关注度：中（VLA 安全与可靠性的少数系统化工作）[90][91][97]；推荐度 ★★★★☆ — 是"negative results 也要写"的正面样本 [91]。
7. **推理期可控性与注意力干预**：Inference-Time Attention Steering for VLA Driving Models（有界加性 pre-softmax 偏置、前向 pre-hook、不改权重，50 个合成换道场景、平均位移约 17 cm）[2]；相关的前置工作指出 VLA 内部已存在可用于路径偏差检测的注意力头 [6]。
   — 热度 `> 待核实`；权威：arXiv 预印本 cs.CV/cs.RO，非同行评审、无第三方复现 [2][6]；关注度：低（无引用/榜单/社区讨论信号）[2][6]；推荐度 ★★★☆☆ — 方向新颖（不改权重的可控性），但场景数小、仅仿真合成数据 [2]。
8. **评测与透明度基础设施**：VLA-Arena（citations=35，唯一有量化热度）[112]、Sim-to-Real 基准视角 [32]、2025 FMTI（平均分 58→40）[25]。
   — 热度：VLA-Arena citations=35 [112]，其余 `> 待核实`；权威：arXiv 预印本 [25][32][112]，FMTI 由 Percy Liang、Rishi Bommasani 等参与撰写但非同行评审 [25]；关注度：中（透明度下降直接影响 VLA 归因能力）[25]；推荐度 ★★★★☆ — 做横向对比前必读的先决条件。
9. **本体边界扩展**：GR00T N1（人形通用基础模型）[41]、AeroManip-VLA（空中操作）[94]、BioProVLA-Agent（实验室操作）[100]、RealMirror（开源 VLA 平台）[121]、VLA-Adapter（tiny-scale VLA）[95]。
   — 热度 `> 待核实`；权威：arXiv 预印本 [41][94][95][100][121]；关注度：中（人形与垂直场景是 2025-2026 的扩张方向）[41][94][100]；推荐度 ★★★☆☆ — 与本体泛化议题相关，但各自证据以自述为主。
10. **低阶动作生成的替代范式**：Streaming Flow Policy（批评"轨迹的轨迹"采样）[36]、FlowPolicy（一致性流匹配）[88]、Affordance-based Manipulation with Flow Matching [87]、Diffusion Policy Policy Optimization [23]。
    — 热度 `> 待核实`；权威：arXiv 预印本 [23][36][87][88]；关注度：中（扩散 vs 流匹配的路线之争仍未收敛）[24][36]；推荐度 ★★★★☆ — 若关心推理效率与多模态动作建模的取舍，这组是核心论战材料。

**Watchlist 的判定纪律**：以上十条中，第 8 条（VLA-Arena, citations=35 [112]）是唯一具备量化热度信号的条目；其余条目的"热度证据"均为 `> 待核实`。因此本清单应被读作"待跟踪线索"，而非"已验证 SOTA 排名"。任何进一步的强弱排序，都需先补齐三类数字：真机成功率与任务数、参与评测的本体数量、以及独立第三方复现或榜单排名 [25][32][91]。

## 参考来源

[1] Overview of AuTexTification at IberLEF 2023: Detection and Attribution of Machine-Generated Text in Multiple Domains — http://arxiv.org/abs/2309.11285v1
[2] Inference-Time Attention Steering for Vision-Language-Action Driving Models — http://arxiv.org/abs/2608.17095v1
[3] Compositional Context Fine-Tuning Vision-Language Model for Complex Assembly Action Understanding from Videos — http://arxiv.org/abs/2607.10797v1
[4] RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control — http://arxiv.org/abs/2307.15818v1
[5] BLURR: A Boosted Low-Resource Inference for Vision-Language-Action Models — http://arxiv.org/abs/2512.11769v1
[6] Your Vision-Language-Action Model Already Has Attention Heads For Path Deviation Detection — http://arxiv.org/abs/2603.13782v1
[7] A Simulation and Modeling of Access Points with Definition Language — http://arxiv.org/abs/1304.1836v2
[8] Evolve Vision-Language-Action Model into an Agent with On-the-fly Tool-use — http://arxiv.org/abs/2608.14047v3
[9] Overview of Dialogue Robot Competition 2022 — http://arxiv.org/abs/2210.12863v1
[10] Xiaomi-Robotics-1: Scaling Vision-Language-Action Models with over 100K Hours of Real-World Trajectories — http://arxiv.org/abs/2607.15330v2
[11] ViTAL: Vision-Based Terrain-Aware Locomotion for Legged Robots — http://arxiv.org/abs/2212.01246v1
[12] ditlab system for Dialogue Robot Competition 2022 — http://arxiv.org/abs/2210.06646v1
[13] CHC-COMP 2022: Competition Report — http://arxiv.org/abs/2211.12231v1
[14] Scalable Simulation and Demonstration of Jumping Piezoelectric 2-D Soft Robots — http://arxiv.org/abs/2202.13521v1
[15] IEEE Trust, Acceptance and Social Cues in Human-Robot Interaction -- SCRITA 2022 Workshop — http://arxiv.org/abs/2208.11090v2
[16] Active Uncertainty Reduction for Human-Robot Interaction: An Implicit Dual Control Approach — http://arxiv.org/abs/2202.07720v2
[17] Proceedings of the Dialogue Robot Competition 2023 — http://arxiv.org/abs/2312.14430v5
[18] Diffusion Co-Policy for Synergistic Human-Robot Collaborative Tasks — http://arxiv.org/abs/2305.12171v4
[19] Overview of Dialogue Robot Competition 2023 — http://arxiv.org/abs/2401.03547v1
[20] RealD$^2$iff: Bridging Real-World Gap in Robot Manipulation via Depth Diffusion — http://arxiv.org/abs/2511.22505v2
[21] Kinematics-Aware Diffusion Policy with Consistent 3D Observation and Action Space for Whole-Arm Robotic Manipulation — http://arxiv.org/abs/2512.17568v1
[22] ActivePose: Active 6D Object Pose Estimation and Tracking for Robotic Manipulation — http://arxiv.org/abs/2509.11364v2
[23] Diffusion Policy Policy Optimization — http://arxiv.org/abs/2409.00588v3
[24] Diffusion policy: Visuomotor policy learning via action diffusion — https://arxiv.org/abs/2303.04137
[25] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1
[26] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1
[27] Task adaptation of Vision-Language-Action model: 1st Place Solution for the 2025 BEHAVIOR Challenge — http://arxiv.org/abs/2512.06951v2
[28] Survey of Vision-Language-Action Models for Embodied Manipulation — http://arxiv.org/abs/2508.15201v2
[29] AIn't Nothing But a Survey? Using Large Language Models for Coding German Open-Ended Survey Responses on Survey Motivation — http://arxiv.org/abs/2506.14634v3
[30] A Pragmatic VLA Foundation Model — http://arxiv.org/abs/2601.18692v4
[31] Grasp and Motion Planning for Dexterous Manipulation for the Real Robot Challenge — http://arxiv.org/abs/2101.02842v1
[32] Robot Policy Evaluation for Sim-to-Real Transfer: A Benchmarking Perspective — http://arxiv.org/abs/2508.11117v1
[33] From Foundation to Application: Improving VLA Models in Practice — http://arxiv.org/abs/2607.06403v1
[34] One-Shot Reinforcement Learning for Robot Navigation with Interactive Replay — http://arxiv.org/abs/1711.10137v2
[35] JENGA: Exploiting Counter-Based RowHammer Countermeasures to Break Real-Time Predictability — http://arxiv.org/abs/2609.01077v1
[36] Streaming Flow Policy: Simplifying diffusion/flow-matching policies by treating action trajectories as flow trajectories — http://arxiv.org/abs/2505.21851v2
[37] Flow Matching Ergodic Coverage — http://arxiv.org/abs/2504.17872v1
[38] LLM-based ambiguity detection in natural language instructions for collaborative surgical robots — http://arxiv.org/abs/2507.11525v1
[39] TRUST 2025: SCRITA and RTSS @ RO-MAN 2025 — http://arxiv.org/abs/2509.11402v1
[40] Topological Flow Matching — http://arxiv.org/abs/2606.15897v1
[41] GR00T N1: An Open Foundation Model for Generalist Humanoid Robots — http://arxiv.org/abs/2503.14734v2
[42] A ROS-based Software Framework for the NimbRo-OP Humanoid Open Platform — http://arxiv.org/abs/1809.11051v1
[43] Towards Miniature Humanoid Tele-Loco-Manipulation Using Virtual Reality and Reinforcement Learning — http://arxiv.org/abs/2607.20399v1
[44] Humanoid Agent via Embodied Chain-of-Action Reasoning with Multimodal Foundation Models for Zero-Shot Loco-Manipulation — http://arxiv.org/abs/2504.09532v3
[45] NimbRo-OP2: Grown-up 3D Printed Open Humanoid Platform for Research — http://arxiv.org/abs/1809.11144v1
[46] The RSNA Abdominal Traumatic Injury CT (RATIC) Dataset — http://arxiv.org/abs/2405.19595v1
[47] NTU-NPU System for Voice Privacy 2024 Challenge — http://arxiv.org/abs/2410.02371v1
[48] Discovery Opportunities with Gravitational Waves -- TASI 2024 Lecture Notes — http://arxiv.org/abs/2409.08956v1
[49] Open X-Embodiment: Robotic Learning Datasets and RT-X Models — http://arxiv.org/abs/2310.08864v9
[50] Open-Ended Learning Leads to Generally Capable Agents — http://arxiv.org/abs/2107.12808v2
[51] Learning to Discern: Imitating Heterogeneous Human Demonstrations with Preference and Representation Learning — http://arxiv.org/abs/2310.14196v1
[52] Deception Game: Closing the Safety-Learning Loop in Interactive Robot Autonomy — http://arxiv.org/abs/2309.01267v2
[53] DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset — http://arxiv.org/abs/2403.12945v2
[54] Point Transformer V3 Extreme: 1st Place Solution for 2024 Waymo Open Dataset Challenge in Semantic Segmentation — http://arxiv.org/abs/2407.15282v1
[55] Uncovering Coordinated Cross-Platform Information Operations Threatening the Integrity of the 2024 U.S. Presidential Election Online Discussion — http://arxiv.org/abs/2409.15402v2
[56] Unfiltered Conversations: A Dataset of 2024 U.S. Presidential Election Discourse on Truth Social — http://arxiv.org/abs/2411.01330v1
[57] Atmospheric entry and fragmentation of small asteroid 2024 BX1: Bolide trajectory, orbit, dynamics, light curve, and spectrum — http://arxiv.org/abs/2403.00634v2
[58] An Introduction to Lifelong Supervised Learning — http://arxiv.org/abs/2207.04354v2
[59] LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning — http://arxiv.org/abs/2306.03310v2
[60] Latent Properties of Lifelong Learning Systems — http://arxiv.org/abs/2207.14378v1
[61] Lifelong Learning using Eigentasks: Task Separation, Skill Acquisition, and Selective Transfer — http://arxiv.org/abs/2007.06918v1
[62] Forgetting and Imbalance in Robot Lifelong Learning with Off-policy Data — http://arxiv.org/abs/2204.05893v2
[63] TAG: Task-based Accumulated Gradients for Lifelong learning — http://arxiv.org/abs/2105.05155v3
[64] OpenFact at CheckThat! 2024: Combining Multiple Attack Methods for Effective Adversarial Text Generation — http://arxiv.org/abs/2409.02649v2
[65] Towards Embodiment Scaling Laws in Robot Locomotion — http://arxiv.org/abs/2505.05753v2
[66] Robot Trains Robot: Automatic Real-World Policy Adaptation and Learning for Humanoids — http://arxiv.org/abs/2508.12252v2
[67] On-Policy Robot Imitation Learning from a Converging Supervisor — http://arxiv.org/abs/1907.03423v7
[68] Federated and Transfer Learning: A Survey on Adversaries and Defense Mechanisms — http://arxiv.org/abs/2207.02337v1
[69] Multi-objective Model-based Policy Search for Data-efficient Learning with Sparse Rewards — http://arxiv.org/abs/1806.09351v3
[70] Mirage: Cross-Embodiment Zero-Shot Policy Transfer with Cross-Painting — http://arxiv.org/abs/2402.19249v3
[71] Transfer Learning Toolkit: Primers and Benchmarks — http://arxiv.org/abs/1911.08967v1
[72] Behavior-Aligned Action Tokenization for Robot Policy Learning — http://arxiv.org/abs/2609.27513v1
[73] Geometric Action Model for Robot Policy Learning — http://arxiv.org/abs/2606.17046v2
[74] TOAST: Stochastic Robot Action Tokenization for Autoregressive Vision-Language-Action Models — http://arxiv.org/abs/2610.00899v1
[75] Ordered Action Tokens for Visuomotor Policy Learning — http://arxiv.org/abs/2607.21670v1
[76] CLAM: Continuous Latent Action Models for Robot Learning from Unlabeled Demonstrations — http://arxiv.org/abs/2505.04999v2
[77] High-level robot programming based on CAD: dealing with unpredictable environments — http://arxiv.org/abs/1309.2086v1
[78] Explainable Machine Learning for Public Policy: Use Cases, Gaps, and Research Directions — http://arxiv.org/abs/2010.14374v3
[79] End-User Programming of Low- and High-Level Actions for Robotic Task Planning — http://arxiv.org/abs/2103.14342v1
[80] GET-Zero: Graph Embodiment Transformer for Zero-shot Embodiment Generalization — http://arxiv.org/abs/2407.15002v2
[81] Cloak: Zero-Shot Cross-Embodiment Manipulation by Masking the End-Effector from the VLA — http://arxiv.org/abs/2606.22836v2
[82] ZETA: A Controlled Study of Zero-Shot Cross-Embodiment VLA Transfer for Tabletop Manipulation — http://arxiv.org/abs/2609.02546v2
[83] FlashSpeech: Efficient Zero-Shot Speech Synthesis — http://arxiv.org/abs/2404.14700v4
[84] Zero-shot Imitation Learning from Demonstrations for Legged Robot Visual Navigation — http://arxiv.org/abs/1909.12971v2
[85] Towards Zero-Shot Transfer Across Embodiments For Driving VLAs — http://arxiv.org/abs/2609.02341v1
[86] Diffusion and Flow Matching Models for Tabular Data: A Survey — http://arxiv.org/abs/2502.17119v2
[87] Affordance-based Robot Manipulation with Flow Matching — http://arxiv.org/abs/2409.01083v5
[88] FlowPolicy: Enabling Fast and Robust 3D Flow-based Policy via Consistency Flow Matching for Robot Manipulation — http://arxiv.org/abs/2412.04987v2
[89] ToolFlowNet: Robotic Manipulation with Tools via Predicting Tool Flow from Point Clouds — http://arxiv.org/abs/2211.09006v1
[90] When Vision Overrides Language: Evaluating and Mitigating Counterfactual Failures in VLAs — http://arxiv.org/abs/2602.17659v2
[91] How VLAs Fail Differently: Black-Box Action Monitoring Reveals Architecture-Specific Failure Signatures — http://arxiv.org/abs/2605.28726v1
[92] Running VLAs at Real-time Speed — http://arxiv.org/abs/2510.26742v1
[93] Robotic VLA Benefits from Joint Learning with Motion Image Diffusion — http://arxiv.org/abs/2512.18007v1
[94] AeroManip-VLA: Scalable Vision-Language-Action Learning for Aerial Manipulation with RL-Generated Demonstrations — http://arxiv.org/abs/2609.36915v1
[95] VLA-Adapter: An Effective Paradigm for Tiny-Scale Vision-Language-Action Model — http://arxiv.org/abs/2509.09372v2
[96] Understanding Build Reproducibility in the F-Droid Ecosystem — http://arxiv.org/abs/2607.01890v1
[97] SafeAlign-VLA: A Negative-Enhanced Safe Alignment Framework for Risk-Aware Autonomous Driving — https://arxiv.org/abs/2605.19524
[98] Blood pressure response and symptoms during active standing test among hospitalized and outpatients with heart failure: results from the GRAVITY-HF prospective observational cohort study. — https://doi.org/10.1016/j.cardfail.2023.12.017
[99] On Multi-Cause Approaches to Causal Inference with Unobserved Counfounding: Two Cautionary Failure Cases and A Promising Alternative — https://www.semanticscholar.org/paper/86f85544cce0b29be6d2b3e73a102653bae5bece
[100] BioProVLA-Agent: An Affordable, Protocol-Driven, Vision-Enhanced VLA-Enabled Embodied Multi-Agent System with Closed-Loop-Capable Reasoning for Biological Laboratory Manipulation — https://arxiv.org/abs/2605.07306
[101] Small effect size leads to reproducibility failure in resting-state fMRI studies — https://doi.org/10.1101/285171
[102] Open Source Software Development Challenges: A Systematic Literature Review on GitHub — http://arxiv.org/abs/2003.10750v3
[103] On the Popularity of GitHub Applications: A Preliminary Note — http://arxiv.org/abs/1507.00604v3
[104] OpenVLA: An Open-Source Vision-Language-Action Model — http://arxiv.org/abs/2406.09246v3
[105] Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success — http://arxiv.org/abs/2502.19645v2
[106] Impromptu VLA: Open Weights and Open Data for Driving Vision-Language-Action Models — http://arxiv.org/abs/2505.23757v1
[107] Enhancing Linguistic Generalization of VLA: Fine-Tuning OpenVLA via Synthetic Instruction Augmentation — http://arxiv.org/abs/2603.16044v1
[108] Fine-tuning with Very Large Dropout — http://arxiv.org/abs/2403.00946v3
[109] Differentially Private Fine-tuning of Language Models — http://arxiv.org/abs/2110.06500v2
[110] OpenVLA: An Open-Source Vision-Language-Action Model — https://arxiv.org/abs/2406.09246
[111] Fine-T2I: An Open, Large-Scale, and Diverse Dataset for High-Quality T2I Fine-Tuning — http://arxiv.org/abs/2602.09439v1
[112] VLA-Arena: An Open-Source Framework for Benchmarking Vision-Language-Action Models — https://arxiv.org/abs/2512.22539
[113] LLM Fine-Tuning With Biomedical Open-Source Data — https://www.semanticscholar.org/paper/05c37b8ebc33243e5ae13d55442432e542747923
[114] Predicting the Popularity of GitHub Repositories — http://arxiv.org/abs/1607.04342v1
[115] Fine-Tuning and Deployment of a Vision-Language-Action Based Robotic Foundation Model for Open-Source Robot Arms — https://doi.org/10.1109/ICHORA69329.2026.11537253
[116] Generating GitHub Repository Descriptions: A Comparison of Manual and Automated Approaches — http://arxiv.org/abs/2110.13283v1
[117] OpenViGA: Video Generation for Automotive Driving Scenes by Streamlining and Fine-Tuning Open Source Models with Public Data — https://arxiv.org/abs/2509.15479
[118] LLM-based Content Classification Approach for GitHub Repositories by the README Files — http://arxiv.org/abs/2507.21899v1
[119] Fine-Tuning LLMs for Low-Resource Dialect Translation: The Case of Lebanese — https://arxiv.org/abs/2505.00114
[120] Analyzing the Accessibility of GitHub Repositories for PyPI and NPM Libraries — http://arxiv.org/abs/2404.17403v2
[121] RealMirror: A Comprehensive, Open-Source Vision-Language-Action Platform for Embodied AI — https://arxiv.org/abs/2509.14687
[122] Automatically Categorising GitHub Repositories by Application Domain — http://arxiv.org/abs/2208.00269v1
[123] An exploratory study on fine-tuning large language models for secure code generation — https://arxiv.org/abs/2408.09078
[124] What's Inside a GitHub Repository? An Empirical Study on the Contents of 10K Projects — http://arxiv.org/abs/2605.16701v2
[125] GitHub Repositories with Links to Academic Papers: Public Access, Traceability, and Evolution — http://arxiv.org/abs/2004.00199v3


---

*Generated by research-bot · topic=`vla` · depth=`standard` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading · model=`deepseek-v4-flash` · sources=125 · duration=427s · 2026-10-04T23:05:36+00:00*
