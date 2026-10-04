# 具身智能（Embodied AI）方法演进与前沿进展调研报告

**日期**：2026-10-04（UTC）｜**领域**：Embodied AI / VLA / 机器人学习 / Sim2Real｜**检索源数量**：候选证据 119 条编号来源，其中与具身智能主线直接相关者约 65 条，其余为跨领域噪音条目（已在正文中剔除不用）｜**证据分级**：以 arXiv 一手预印本（B 级）为主，少量同行评审期刊/DOI 来源（A/B 级），第三方复现与榜单证据整体缺失

---

## 摘要（Executive Summary）

1. **VLA（Vision-Language-Action）已成为具身智能主线架构**：从 RT-2 的"网络知识迁移到机器人控制"[5]、OpenVLA 的开源复现[106][109]，演进到 2025–2026 年的**任务适配 + 推理效率 + 推理期可控性**三条工程化支线[50][4][2][6]。近一年最具体的进展是 2025 BEHAVIOR Challenge 冠军方案基于 **Pi0.5 架构**、以 flow matching 的 correlated noise 为主要贡献，在 50 项长时程家庭任务（双臂操作 + 导航 + 上下文决策）上取得第一[50]。
2. **世界模型（World Model）开始进入规划回路**：Embodied Tree of Thoughts 明确批评纯视频生成模型"缺乏严格物理 grounding"，转而用具身世界模型做审慎操纵规划[37]；另有工作尝试把 world-action model 从合成先验迁移到真机[24]，以及"潜在世界模型 + 形式化验证"的双系统动作 Transformer[60][61]。
3. **人形全身控制走 RL 课程 + 真机自适应的路线**：如 annealing RL 课程实现全身羽毛球[62]、"Robot Trains Robot"的真人形真机策略自适应[118]，以及双足 locomoation 的 sim-to-real 系统性综述式章节[85]。
4. **评测与数据侧**：Open X-Embodiment[69]、DROID[74]、LIBERO[79] 构成跨本体/大规模真机/终身学习的经典三件套；2025–2026 年出现 VLA-Arena[115]、Embodied Agent Arena[35] 等面向 VLA/VLM 泛化性的新基准。
5. **结构性风险**：2025 FMTI 显示基础模型透明度平均分从 58 降至 40（满分 100），训练数据与算力披露最不透明[49]——这意味着具身基础模型的可核查性同样受限。
6. **本报告的最大缺口（必须明示）**：本轮候选证据中，**世界模型、人形全身控制、导航代理三个维度的一手证据显著薄弱**，且几乎所有前沿条目均为自述型 arXiv 预印本，**缺少第三方复现、榜单交叉验证与开源状态确认**；相关结论一律降级表述。`> 待核实`

---

## 一、关键前沿进展（2024–2026，最新进展单列）

### 1.1 VLA 基础模型：从"能不能做"转向"做得多长、多大算力、可不可控"

- **长时程多技能任务适配**：2025 BEHAVIOR Challenge 第一名方案建立在 Pi0.5 架构之上，主要技术贡献是 flow matching 的 correlated noise，基准含 50 项 photo-realistic 仿真长时程家庭任务，要求双臂操作、导航与情境感知决策[50]。
  - **热度**：`> 待核实`（候选块未给引用数或 star）｜**权威**：arXiv 预印本（cs.RO, v2），第一方竞赛方案报告，未见同行评审或第三方复现[50]｜**关注度**：中——竞赛冠军方案通常受 VLA/长时程操作社区关注，但无第三方榜单确认[50]｜**推荐度**：★★★★☆——直接对应 VLA 能力边界，且基于已有 Pi0.5 架构，改进可归因[50]。
- **推理侧轻量化**：BLURR 提出轻量推理封装，可**不重训、不改权重**地插入现有 VLA 控制器，以支撑高频机器人控制或消费级 GPU[4][116]。
  - **热度**：`> 待核实`｜**权威**：arXiv 预印本（cs.RO），未见会议/期刊标注与开源仓库信息[4][116]｜**关注度**：中——切中 VLA 真机高频部署的工程痛点[4]｜**推荐度**：★★★☆☆——问题真实，证据仅限摘要[4]。
- **推理期可控性（不重训干预）**：在 Alpamayo-R1 的 Qwen3-VL backbone 上，对检测器定位的交通参与者视觉 token 施加**有界加性 pre-softmax 注意力偏置**，作为 fail-open forward pre-hook、不改变权重；在 50 个合成 lane-change 场景中，轨迹解码器对偏置幅度呈**单调剂量-响应**，均值位移约 17 cm、clamp 处横向偏移约 140 cm[2]。
  - **热度**：`> 待核实`｜**权威**：arXiv 预印本（cs.CV），未见同行评审[2]｜**关注度**：中——VLA 安全可控性的新方向[2]｜**推荐度**：★★★☆☆——实验仅 50 个合成场景、单一 backbone，真机泛化未证实[2]。
- **VLA 自省能力**：有工作主张 VLA 模型内部**已存在可用于路径偏差检测的注意力头**，针对导航任务中视觉推理幻觉问题[6]。
  - **热度**：`> 待核实`｜**权威**：arXiv 预印本（cs.RO）[6]｜**关注度**：中——把 VLA 幻觉问题转化为可解释性/自省问题[6]｜**推荐度**：★★★☆☆。
- **VLA 与工具调用结合**：ART（Agentic Robot with Tool-use）是 tool-injection 框架，可微调任意 VLA 模型以调用现成工具模块（低层视觉、高层 affordance、本体增强）[8]。
  - **热度**：`> 待核实`｜**权威**：arXiv 预印本（cs.RO, v3）[8]｜**关注度**：中——"VLA + agentic tool use"是 2026 年明显升温的范式[8]｜**推荐度**：★★★☆☆。
- **跨本体与统一动作空间**：One Policy, Many Embodiments 提出统一的 camera-centric action geometry 预训练以支持异构本体[54]；MiMo-Embodied 为 X-Embodied 基础模型技术报告[55]；Embodied-R1.5[40]、Hy-Embodied-VLM-1.0[41]、ME-VLM[56] 分别推进具身基础模型与统一 VLM 智能体协同。这些条目均为 2025-11 至 2026-09 期间的一手预印本/技术报告。
  - **热度**：`> 待核实`｜**权威**：arXiv 预印本/技术报告，未见同行评审[40][41][54][55][56]｜**关注度**：中——跨本体统一是社区公认的核心开放问题[29][54]｜**推荐度**：★★★☆☆——方向重要，但技术报告类证据难以独立验证[55]。

### 1.2 速度与微调实践

- 微调效率成为独立议题：有工作系统研究 VLA 微调的**速度与成功率权衡**[107]；扩散策略推理加速方面出现动态缓存策略 OnlineCache（面向迭代去噪的静态缓存局限）[13]。其中 [13] 属通用扩散加速，与机器人策略仅为间接相关。

### 1.3 透明度与可核查性（跨领域但方法学相关）

- **2025 FMTI** 为第三版年度评估，新增 data acquisition、usage data、monitoring 指标并首次评估 Alibaba、DeepSeek、xAI；平均分从 2024 年 58 分降至 2025 年 40 分；公司在 training data、training compute 与旗舰模型 post-deployment usage/impact 上最不透明[49]。
  - **热度**：`> 待核实`（候选块未给引用数）｜**权威**：arXiv 预印本（cs.AI），作者含 Percy Liang、Rishi Bommasani，年度系列第三版[49]｜**关注度**：高——政策与学术界持续跟踪的年度指数[49]｜**推荐度**：★★★★☆——为评估具身基础模型数据/算力披露提供方法论背景[49]。

---

## 二、方法谱系：模块化 → 端到端 → 基础模型 → 世界模型

| 阶段 | 代表范式 | 代表工作 | 关键转折 | 引用 |
|---|---|---|---|---|
| 模块化流水线 | 感知 / 规划 / 控制分层，任务规划依赖符号或搜索形式化 | 任务规划形式化传统（HTN 形式与语义） | 依赖人工建模，难以泛化到开放环境 | [58] |
| LLM 规划 + 技能 grounding | LLM 生成高层计划，底层由可行技能/代码落地 | SayCan、Code as Policies（种子资源） | 把语言模型的语义先验接入真实机器人，但底层技能仍为手工定义 | 种子资源（无本次检索编号） |
| 端到端模仿学习 | 视觉-动作直接映射，无需显式状态估计 | One-Shot Visual Imitation via Meta-Learning；Self-Supervised Correspondence in Visuomotor Policy Learning；Diffusion Policy | 从"少样本模仿"到"动作扩散"生成建模，动作分布建模能力大幅提升 | [22][10][16] |
| 基础模型（VLA） | 视觉-语言预训练知识迁移到动作输出；统一 token 化动作 | RT-2；OpenVLA；VLA 综述 | 网络知识成为机器人泛化来源，开源权重使社区可复现 | [5][106][109][51] |
| 基础模型 + 可靠性工程 | 推理加速、工具调用、推理期干预、细粒度感知 | BLURR；ART；推理期注意力引导；CCFT/LP-AT 装配动作理解 | 从"提升上限"转向"可部署、可干预、可解释" | [4][8][2][3] |
| 世界模型 / 双系统 | 潜在世界模型 + 慢思考规划 + 快动作执行；世界模型用于规划前推演 | Embodied Tree of Thoughts；Latent World Models + Formal Verification；World-Action Model Sim2Real；多模态世界模型与扩散策略协同训练 | 从"反应式策略"转向"执行前推演"，并引入形式化验证 | [37][60][61][24][91] |

**谱系判断（含限定）**：
- 方法上，"模块化 → 端到端 → 基础模型"这一主线在综述性材料中有一致叙述：VLA 综述系统整理了具身操作中的 VLA 方法[51]；Robot Learning 教程把领域描述为"从经典模型驱动方法转向数据驱动学习范式的拐点"[32]（**推荐度**：★★★★☆；**权威**：arXiv cs.RO 教程类[32]；**热度**：`> 待核实`）。
- 模块化并未消失，而是以"工具模块被 VLA 调用"的形式回归（ART[8]），这与早期 LLM 规划 + 技能 grounding 的思路形成呼应。
- `> 待核实`：本报告未检索到权威的、时间连续的谱系综述能同时覆盖 2023 年前模块化方法与 2026 年世界模型范式，[51][57][32] 可作部分替代，但完整谱系仍需补充检索。

---

## 三、仿真平台与基准对比

> 说明：候选证据中**缺少仿真平台本体的一手论文证据**（如 IsaacLab、Genesis、ManiSkill 的官方技术报告未出现在 119 条编号来源中）。以下平台信息来自种子资源链接，属**未经本次实时检索确认**的条目。

| 平台 / 基准 | 类型 | 年份 | 关键特征 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 链接 |
|---|---|---|---|---|---|---|---|---|
| BEHAVIOR-1K / OmniGibson | 仿真基准 | 2024 | 1000 项以人为中心的日常活动基准 | `> 待核实` | 种子资源，本次未取得一手论文条目 | 中——被 2025 BEHAVIOR Challenge 沿用为任务来源[50] | ★★★★☆ | https://behavior.stanford.edu/ ／ https://github.com/StanfordVL/BEHAVIOR-1K |
| IsaacLab | GPU 并行机器人学习框架 | — | GPU 并行训练基础设施 | `> 待核实` | 种子资源（官方 GitHub），未见本次检索论文证据 | 中——Isaac 系列在机器人 RL 社区广泛使用 | ★★★★☆ | https://github.com/isaac-sim/IsaacLab |
| ManiSkill | GPU 并行操作基准 | — | 操作任务并行评测 | `> 待核实` | 种子资源（官方 GitHub） | 中 | ★★★☆☆ | https://github.com/haosulab/ManiSkill |
| Genesis | 生成式物理仿真引擎 | — | 生成式物理仿真 | `> 待核实` | 种子资源（官方 GitHub） | 中——发布期社区讨论较多，但本次未取得可核查热度数字 | ★★★☆☆ | https://github.com/Genesis-Embodied-AI/Genesis |
| VLA-Arena | VLA 评测框架 | 2025 | 开源 VLA benchmark 框架 | `> 待核实` | arXiv 预印本[115] | 中 | ★★★☆☆ | http://arxiv.org/abs/2512.22539 |
| Embodied Agent Arena | 前沿 VLM 智能体真机/任务就绪度实证评测 | 2026 | 检验前沿 VLM 是否可作为"机器人通才" | `> 待核实` | arXiv 预印本（cs.RO）[35] | 中——直面"VLM 能力 ≠ 机器人能力"的争议 | ★★★★☆ | http://arxiv.org/abs/2610.00854v1 |
| LIBERO | 终身学习知识迁移基准 | 2023 | 面向 lifelong robot learning | `> 待核实` | arXiv 预印本[79] | 中高——长期被用作迁移学习基准 | ★★★★☆ | http://arxiv.org/abs/2306.03310v2 |
| Sim-to-Real 策略评测基准视角 | 评测方法学 | 2025 | 指出仿真基准与真机评测脱节 | `> 待核实` | arXiv 预印本[89] | 中 | ★★★★☆ | http://arxiv.org/abs/2508.11117v1 |

**对比结论（限定表述）**：仿真侧的"GPU 并行物理 + 大规模任务套件"与评测侧的"VLA 泛化性/就绪度"正在分化成两套基础设施——前者服务训练吞吐，后者服务可信度审计[115][35][89]。**二者之间尚无公认的映射关系**：`> 待核实`。

---

## 四、经典与奠基性工作

> 下表"最新进展"与"经典工作"严格分节：本节仅收录 2024 年及以前的奠基性/经典条目。

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control | 2023 | Google DeepMind 等 | `> 待核实` | arXiv 预印本（cs.RO）；同行评审状态 `> 待核实` | 高——VLA 命名的奠基条目，后续工作普遍以其为起点[51] | ★★★★★ | http://arxiv.org/abs/2307.15818v1 | 首次系统证明网络规模视觉-语言知识可迁移为机器人动作 token[5] |
| Diffusion Policy: Visuomotor Policy Learning via Action Diffusion | 2023 | 学术团队 | `> 待核实` | arXiv 预印本（v5）[16] | 高——动作扩散成为后续策略学习主流组件，被 2026 年工作继续引用/扩展[15][13] | ★★★★★ | http://arxiv.org/abs/2303.04137v5 | 用扩散生成建模替代高斯策略，显著改善多模态动作分布拟合[16] |
| PaLM-E: An Embodied Multimodal Language Model | 2023 | Google | `> 待核实` | 种子资源，本次未取得一手编号条目 | 高——具身多模态 LLM 奠基 | ★★★★☆ | https://arxiv.org/abs/2303.03378 | 把具身观测直接注入多模态 LLM 的早期范式 |
| SayCan: Do As I Can, Not As I Say | 2022 | Google | `> 待核实` | 种子资源 | 高——LLM 规划 × 技能可行性 grounding 的经典组合 | ★★★★★ | https://arxiv.org/abs/2204.01691 | 确立"语言规划必须受可行性约束"的原则 |
| Code as Policies | 2022 | Google | `> 待核实` | 种子资源 | 高——LLM 生成策略代码的开创工作 | ★★★★☆ | https://arxiv.org/abs/2209.07753 | 把策略表达为可执行代码，为后续工具调用范式埋下伏笔[8] |
| One-Shot Visual Imitation Learning via Meta-Learning | 2017 | 学术团队 | `> 待核实` | arXiv 预印本[22] | 中高——少样本模仿学习经典 | ★★★★☆ | http://arxiv.org/abs/1709.04905v1 | 元学习框架下的单次视觉模仿[22] |
| Self-Supervised Correspondence in Visuomotor Policy Learning | 2019 | 学术团队 | `> 待核实` | arXiv 预印本[10] | 中——视觉对应表征的前置工作 | ★★★☆☆ | http://arxiv.org/abs/1909.06933v1 | 用自监督对应关系改善视觉运动策略泛化[10] |
| Open X-Embodiment: Robotic Learning Datasets and RT-X Models | 2023 | 跨机构协作 | `> 待核实` | arXiv 预印本（v9）[69] | 高——跨本体真机数据的事实标准之一 | ★★★★★ | http://arxiv.org/abs/2310.08864v9 | 汇集多机构多本体真机数据并训练 RT-X 模型[69] |
| DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset | 2024 | 跨机构协作 | `> 待核实` | arXiv 预印本（v2）[74] | 高——大规模"野外"真机操作数据集 | ★★★★☆ | http://arxiv.org/abs/2403.12945v2 | 强调场景与任务的野外多样性[74] |
| LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning | 2023 | 学术团队 | `> 待核实` | arXiv 预印本（v2）[79] | 中高——终身机器人学习基准 | ★★★★☆ | http://arxiv.org/abs/2306.03310v2 | 面向知识迁移与终身学习的标准化评测[79] |
| ALOHA 2: An Enhanced Low-Cost Hardware for Bimanual Teleoperation | 2024 | 学术/工业团队 | `> 待核实` | arXiv 预印本[17] | 中高——低成本双臂遥操作硬件范式 | ★★★★☆ | http://arxiv.org/abs/2405.02292v1 | 让双臂数据采集在实验室尺度可负担[17] |
| Understanding Domain Randomization for Sim-to-real Transfer | 2021 | 学术团队 | `> 待核实` | arXiv 预印本（v2）[87] | 中高——域随机化的理论化工作 | ★★★★☆ | http://arxiv.org/abs/2110.03239v2 | 为域随机化提供分析框架[87] |
| DROPO: Sim-to-Real Transfer with Offline Domain Randomization | 2022 | 学术团队 | `> 待核实` | arXiv 预印本（v2）[86] | 中——离线域随机化代表 | ★★★☆☆ | http://arxiv.org/abs/2201.08434v2 | 用离线数据估计随机化分布，减少真机调参[86] |
| One-Shot Reinforcement Learning for Robot Navigation with Interactive Replay | 2017 | 学术团队 | `> 待核实` | arXiv 预印本（v2）[28] | 中——导航代理早期 RL 工作 | ★★★☆☆ | http://arxiv.org/abs/1711.10137v2 | 交互回放实现单次导航 RL[28] |
| Learning to Act without Actions（世界模型线代表） | 2023 | 多机构 | `> 待核实` | 种子资源，本次未取得一手编号条目 | 中——世界模型驱动策略学习代表 | ★★★☆☆ | https://arxiv.org/abs/2312.10807 | 从无动作标签视频中学习可执行策略的思路 |

---

## 五、开源项目与工程实践栈

> **重要限定**：候选证据中**未见任何官方 GitHub 仓库的 star 数、最近提交时间或下载量**，因此"热度"列几乎全部为 `> 待核实`。本节项目线索均来自 arXiv 论文标题/摘要或种子资源，**开源可用性与许可证未经验证**。

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| OpenVLA: An Open-Source Vision-Language-Action Model | 2024 | 学术团队 | `> 待核实` | arXiv 预印本（v3）；另有同题条目[109] | 高——被广泛作为开源 VLA 基线[51] | ★★★★★ | http://arxiv.org/abs/2406.09246v3 | 开源 VLA 权重的关键节点[106][109] |
| LeRobot: An Open-Source Library for End-to-End Robot Learning | 2026 | 学术/社区 | `> 待核实` | arXiv 预印本（cs.RO）[112] | 中——端到端机器人学习库定位 | ★★★★☆ | http://arxiv.org/abs/2602.22818v1 | 端到端机器人学习工具库[112]；**是否为已知同名主流库的正式论文，`> 待核实`** |
| Dexbotic: Open-Source Vision-Language-Action Toolbox | 2025 | 学术团队 | `> 待核实` | arXiv 预印本[110] | 中 | ★★★★☆ | https://arxiv.org/abs/2510.23511 | VLA 工具箱，面向数据/训练/部署流水线[110] |
| RealMirror: Open-Source VLA Platform for Embodied AI | 2025 | 学术团队 | `> 待核实` | arXiv 预印本[111] | 中 | ★★★☆☆ | https://arxiv.org/abs/2509.14687 | 综合性开源 VLA 平台[111] |
| StemVLA: Open-Source VLA with 3D Spatial Geometry & 4D Historical Representation | 2026 | 学术团队 | `> 待核实` | arXiv 预印本[114] | 中——3D/4D 表征是 VLA 新方向 | ★★★☆☆ | https://arxiv.org/abs/2602.23721 | 未来 3D 几何知识与 4D 历史表征[114] |
| BLURR（推理封装） | 2025 | 学术团队 | `> 待核实` | arXiv 预印本[4][116] | 中 | ★★★☆☆ | https://arxiv.org/abs/2512.11769 | 可插拔、不重训的 VLA 轻量推理层[4][116] |
| 开源 VLA 综述（期刊） | 2025 | 期刊综述 | `> 待核实` | Springer 期刊文章（DOI 存在）[113] | 中 | ★★★★☆ | https://doi.org/10.1007/s42791-025-00108-1 | 对开源 VLA 生态的系统梳理[113] |
| AI Robotics Open Source R&D Survey (2023–2025) | 2025 | 综述作者 | citations = 1[75] | TechRxiv 预印本[75] | 低——引用数仅 1[75] | ★★★☆☆ | https://doi.org/10.36277/techrxiv.175756484.48648133/v1 | 覆盖基础模型/数据集/仿真/基准四支柱[75]；**引用数偏低，宜作为索引而非结论来源** |
| IsaacLab | — | NVIDIA（种子资源） | `> 待核实` | 官方 GitHub（种子资源） | 中 | ★★★★☆ | https://github.com/isaac-sim/IsaacLab | GPU 并行机器人学习框架 |
| ManiSkill | — | 社区（种子资源） | `> 待核实` | 官方 GitHub | 中 | ★★★☆☆ | https://github.com/haosulab/ManiSkill | GPU 并行操作基准 |
| Genesis | — | 社区（种子资源） | `> 待核实` | 官方 GitHub | 中 | ★★★☆☆ | https://github.com/Genesis-Embodied-AI/Genesis | 生成式物理仿真引擎 |
| BEHAVIOR-1K / OmniGibson | — | Stanford（种子资源） | `> 待核实` | 官方 GitHub + 基准主页 | 中高 | ★★★★☆ | https://github.com/StanfordVL/BEHAVIOR-1K | 1000 项日常活动基准与配套仿真 |

**工程实践侧观察**：
- 2025–2026 年开源工作的重心明显从"发布模型"转向"发布工具箱/推理层/评测框架"（Dexbotic[110]、RealMirror[111]、LeRobot[112]、VLA-Arena[115]、BLURR[4]），说明社区瓶颈已从算法原型转向**部署与可比性**。
- ROS2 集成：本轮候选中**未见任何 ROS2 相关的 VLA 部署一手论文**。`> 待核实`（需要在下一轮补充 `ros2 VLA deployment`、`ros2_control policy inference` 等检索词）。

---

## 六、数据集与评测协议

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Open X-Embodiment | 2023 | 跨机构协作 | `> 待核实` | arXiv 预印本（v9）[69] | 高 | ★★★★★ | https://robotics-transformer-x.github.io/ ；http://arxiv.org/abs/2310.08864v9 | 跨本体真机数据聚合，RT-X 训练基座[69] |
| DROID | 2024 | 跨机构协作 | `> 待核实` | arXiv 预印本（v2）[74] | 高 | ★★★★☆ | http://arxiv.org/abs/2403.12945v2 | 大规模 in-the-wild 真机操作数据[74] |
| BEHAVIOR-1K | 2024 | Stanford | `> 待核实` | 种子资源 + 基准主页；2025 Challenge 沿用其任务体系[50] | 中高 | ★★★★☆ | https://behavior.stanford.edu/ | 1000 项日常活动、以人为中心[50] |
| LIBERO | 2023 | 学术团队 | `> 待核实` | arXiv 预印本[79] | 中高 | ★★★★☆ | http://arxiv.org/abs/2306.03310v2 | 终身学习/知识迁移评测[79] |
| AgiBot World | — | 机构数据集 | `> 待核实` | 种子资源（未取得一手论文编号） | 中——大规模真机具身数据集定位 | ★★★☆☆ | https://agibot-world.com/ | 大规模真机数据——**规模数字与许可 `> 待核实`** |
| VLA-Arena | 2025 | 学术团队 | `> 待核实` | arXiv 预印本[115] | 中 | ★★★☆☆ | http://arxiv.org/abs/2512.22539 | 开源 VLA 基准框架[115] |
| Embodied Agent Arena | 2026 | 学术团队 | `> 待核实` | arXiv 预印本[35] | 中 | ★★★★☆ | http://arxiv.org/abs/2610.00854v1 | 用实证研究检验前沿 VLM 智能体作为机器人通才的就绪度[35] |
| LongCoT | 2026 | 学术团队 | `> 待核实` | arXiv 预印本[34] | 中 | ★★★☆☆ | http://arxiv.org/abs/2604.14140v1 | 长程思维链推理可扩展基准；**非机器人专用**，可作为长时程推理评测参照[34] |
| LongDS-Bench | 2026 | 学术团队 | `> 待核实` | arXiv 预印本（v3）[39] | 中 | ★★☆☆☆ | http://arxiv.org/abs/2605.30434v3 | 长时程智能体数据分析失败模式；与具身仅为间接相关[39] |
| Physical AI World Model Synthetic dataset | — | — | `> 待核实` | 仅见于 [2] 的引用，发布方与主页未在候选中给出 | 低 | ★★☆☆☆ | `> 待核实` | VLA 驾驶注意力引导实验用 50 个 lane-change 场景[2]；**来源不可核实** |

**评测协议的关键问题**：
1. **仿真真机口径割裂**：仿真基准（BEHAVIOR-1K / LIBERO / VLA-Arena）与真机数据（Open X-Embodiment / DROID）之间缺少统一的迁移评价协议，[89] 明确指出真机泛化策略的评测"落后于"仿真基准的发展[89]。
2. **基准要求 ≠ 能力证明**：BEHAVIOR Challenge 的基准要求包含 navigation，但 [50] 未给出导航子能力的独立方法证据[50]。
3. **失败模式被系统化评测的尝试**：Embodied Agent Arena 明确以"局部能力是否构成完整任务能力"为问题[35]，LongDS-Bench 则以失败为研究对象[39]，代表评测从"排名"转向"归因"。
4. 数据层的方法论整理可参考 Data Pyramid for Embodied Manipulation[57]（**权威**：arXiv 预印本（v2）；**热度**：`> 待核实`；**推荐度**：★★★☆☆）。

---

## 七、Sim2Real 与开放问题

### 7.1 Sim2Real 技术路线（近 1–2 年）

| 路线 | 代表工作 | 要点 | 证据强度 | 引用 |
|---|---|---|---|---|
| 域随机化（含离线估计） | Understanding Domain Randomization；DROPO | 域随机化的理论刻画与离线随机化分布估计 | B 级预印本，2021–2022 经典 | [87][86] |
| 世界-动作模型的合成先验迁移 | Efficient Sim-to-Real Transfer of World-Action Models from Synthetic Priors | 用可扩展合成数据替代昂贵真机示教，**此前未见 world-action model 从仿真迁移到真机的证明** | B 级预印本（cs.RO, 2026） | [24] |
| 双足运动 sim-to-real | Sim-to-Real Transfer in DRL for Bipedal Locomotion | 系统解剖 "curse of simulation" 的主要来源 | B 级预印本（cs.RO, 2025，章节形式） | [85] |
| 数字孪生 / real2sim | MATTERIX（机器人化学实验室数字孪生）；DTaaS；实时数字孪生研究方向 | 把物理实验室/设备状态镜像为可反复求解的数字对象，减少 make-and-test 迭代 | 混合：MATTERIX 为 arXiv 预印本[95]，DTaaS 为 arXiv 预印本[90]，实时数字孪生为 6G 综述[94] | [95][90][94] |
| GPU 并行物理仿真 | 种子资源 IsaacLab / ManiSkill / Genesis | 训练吞吐基础设施 | **本次候选证据中无一手论文支撑**，`> 待核实` | 种子资源 |

**Sim2Real 证据强度总评**：
- 所有 Sim2Real 条目均为 2021–2026 年预印本，**无第三方复现报告或统一榜单**（[24][85][89][86][87]）。**热度**：`> 待核实`；**权威**：arXiv 预印本为主；**关注度**：中高（Sim2Real 是部署必需环节[24][89]）；**推荐度**：★★★★☆（[24][89]）／★★★☆☆（[86][87] 较旧）。
- 数字孪生方向与具身智能主线存在**术语漂移风险**：[95][97][90][94] 中部分工作属于化学实验室自动化、经颅超声、6G 波束成形，与机器人本体策略的 real2sim 不是同一问题，**不宜混为一谈**。`> 待核实`

### 7.2 开放问题与争议

1. **数据瓶颈与规模化规律**：Towards Embodiment Scaling Laws in Robot Locomotion 直接检验"增加训练本体数量能否提升对未见本体的泛化"，作者明确指出该假设的 enabling factors "仍知之甚少"[29]。
   - **热度**：`> 待核实`｜**权威**：arXiv 预印本（cs.RO, v2, 2025）[29]｜**关注度**：高——规模化规律是具身基础模型的核心争议[29]｜**推荐度**：★★★★☆。
2. **泛化与长程任务**：VLA 在长时程多技能任务上已有竞赛级方案[50]，但导航子能力受视觉推理幻觉限制[6]；VLM 是否足以支撑"机器人通才"存在直接实证质疑[35]。
3. **评测可复现性**：真机评测滞后于仿真[89]；VLA 基准框架刚起步[115]；竞赛方案缺少独立复现[50]。
4. **透明度与可核查性**：FMTI 2025 显示基础模型透明度整体倒退（58 → 40 分），训练数据与算力披露最弱[49]，这对具身基础模型（含 VLA 与世界模型）的数据来源审计构成结构性障碍。
5. **失败案例与负结果**：候选证据中含明确负向/失败导向的研究，如长时程智能体数据分析的失败基准[39]、VLA 导航的视觉推理幻觉[6]、装配动作理解因"细微运动与细粒度手物交互"而困难的表述[3]。**这是本报告中少见的负结果证据，建议在后续调研中刻意放大检索**。
6. **工业与协作场景的落地争议**：汽车制造业具身智能的 mini review 被更正（correction）[27]，**citations = 0**[27]，说明该方向的一手证据在本轮候选中非常薄弱；手术机器人协作方面有综述与歧义检测工作[45][44]（**权威**：arXiv 预印本；**热度**：`> 待核实`；**推荐度**：★★☆☆☆，与移动操作主线相关度有限）。

### 7.3 尚不能确认的事项（显式列出）

- 世界模型方向**缺乏跨任务、跨本体的第三方验证**：现有条目 [37][24][60][61][91] 中，[60][61] 为 Zenodo 存档（同一工作两个 DOI），[91] 为 Research Square 预印本，均非同行评审顶会证据。`> 待核实`
- 人形全身控制条目 [62][118] 的**真机成功率、任务数与硬件平台**在候选摘要中未给出。`> 待核实`
- 导航代理方向**未检索到专用的具身导航基础模型证据**（仅有 [6][28]）。`> 待核实`
- 所有开源项目的 **star 数、最近提交时间、许可证**均未取得。`> 待核实`

---

## 八、建议关注清单（Watchlist）

| # | 关注对象 | 类型 | 为什么值得盯 | 下一步验证动作 | 引用 |
|---|---|---|---|---|---|
| 1 | BEHAVIOR Challenge 后续赛季与 Pi0.5 系方案 | 基准 + 方法 | 长时程双臂+导航+情境决策的最强公开赛场，任务数明确（50 项） | 跟踪官方排行榜与第三方复现；确认冠军方案开源状态 | [50] |
| 2 | VLA 推理期干预（注意力引导/剂量-响应） | 安全可控性 | 不重训即可引导安全关键注意力，是 VLA 上真机的低成本安全补丁思路 | 在非驾驶域、更多 backbone、真机上复现；确认是否有开源 hook 实现 | [2][6] |
| 3 | VLA 轻量推理封装（BLURR 类） | 部署工程 | 直接击中"高频真机控制 + 消费级 GPU"的落地瓶颈 | 确认代码是否开放、在 OpenVLA/pi-zero 上的实测延迟 | [4][116] |
| 4 | World-Action Model 的 sim-to-real 迁移 | 世界模型 × Sim2Real | 若成立，可用合成数据替代昂贵真机示教 | 核查是否给出真机成功率与本体清单 | [24] |
| 5 | Embodied Tree of Thoughts / 潜在世界模型 + 形式化验证 | 规划 + 世界模型 | 把"执行前推演"与"可验证性"结合，是差异化的技术路线 | 核查形式化验证的适用范围与实际开销；[60][61] 为 Zenodo 存档，需找正式发表版本 | [37][60][61] |
| 6 | Embodied Agent Arena | 评测方法学 | 直接质询"前沿 VLM 是否已是机器人通才"，属于必要的降温型研究 | 复现其失败模式分类，与其他基准做交叉对照 | [35] |
| 7 | VLA-Arena + LIBERO + Sim-to-Real 评测视角 | 评测基础设施 | 训练侧与评测侧正在分化，需要统一口径 | 对比三者的任务分布、本体覆盖与真机/仿真比例 | [115][79][89] |
| 8 | 跨本体统一动作空间（camera-centric / X-Embodied） | 表征与预训练 | 跨本体泛化是具身基础模型的核心未解问题 | 核查 [54][55] 的本体数量与迁移评测设置 | [54][55][29] |
| 9 | 人形全身控制：RL 课程 + 真机自适应 | 全身控制 | 高动态全身任务（如羽毛球）与"机器人训练机器人"代表两条互补路线 | 核查真机硬件、成功率与是否开源 | [62][118][85] |
| 10 | 具身数据方法学：Data Pyramid | 数据 | 数据金字塔可为"仿真-真机-互联网数据"配比提供框架 | 核查其分类维度是否可操作化 | [57][75] |
| 11 | FMTI 年度透明度指数 | 元证据 | 决定具身基础模型结论能否被审计 | 每年跟踪平均分与 data/compute 披露项变化 | [49] |
| 12 | VLA 触觉反馈（VLA-Touch） | 感知扩展 | 本轮候选中**唯一带明确引用数（citations = 68）的具身条目**，属相对高热度方向 | 核查触觉硬件依赖与在接触密集任务上的成功率 | [117] |

---

## 参考来源

> 以下编号与正文引用一一对应；正文未引用的编号（跨领域噪音条目，如天体物理、选举信息操作、语音隐私等）未列入。

[2] Inference-Time Attention Steering for Vision-Language-Action Driving Models — http://arxiv.org/abs/2608.17095v1
[3] Compositional Context Fine-Tuning Vision-Language Model for Complex Assembly Action Understanding from Videos — http://arxiv.org/abs/2607.10797v1
[4] BLURR: A Boosted Low-Resource Inference for Vision-Language-Action Models — http://arxiv.org/abs/2512.11769v1
[5] RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control — http://arxiv.org/abs/2307.15818v1
[6] Your Vision-Language-Action Model Already Has Attention Heads For Path Deviation Detection — http://arxiv.org/abs/2603.13782v1
[8] Evolve Vision-Language-Action Model into an Agent with On-the-fly Tool-use — http://arxiv.org/abs/2608.14047v3
[10] Self-Supervised Correspondence in Visuomotor Policy Learning — http://arxiv.org/abs/1909.06933v1
[13] OnlineCache: Learning Dynamic Caching Policies with Error Correction for Efficient Diffusion Inference — http://arxiv.org/abs/2607.29398v1
[15] Factorizing Diffusion Policies for Observation Modality Prioritization — http://arxiv.org/abs/2509.16830v1
[16] Diffusion Policy: Visuomotor Policy Learning via Action Diffusion — http://arxiv.org/abs/2303.04137v5
[17] ALOHA 2: An Enhanced Low-Cost Hardware for Bimanual Teleoperation — http://arxiv.org/abs/2405.02292v1
[22] One-Shot Visual Imitation Learning via Meta-Learning — http://arxiv.org/abs/1709.04905v1
[24] Efficient Sim-to-Real Transfer of World-Action Models from Synthetic Priors — http://arxiv.org/abs/2606.31101v1
[27] Correction: Neurorobotics for automotive manufacturing industry in era of embodied intelligence: a mini review — https://doi.org/10.3389/fnbot.2026.1829525
[28] One-Shot Reinforcement Learning for Robot Navigation with Interactive Replay — http://arxiv.org/abs/1711.10137v2
[29] Towards Embodiment Scaling Laws in Robot Locomotion — http://arxiv.org/abs/2505.05753v2
[32] Robot Learning: A Tutorial — http://arxiv.org/abs/2510.12403v1
[34] LongCoT: Benchmarking Long-Horizon Chain-of-Thought Reasoning — http://arxiv.org/abs/2604.14140v1
[35] Are Frontier VLM Agents Ready to Be Robot Generalists? An Empirical Study with the Embodied Agent Arena — http://arxiv.org/abs/2610.00854v1
[37] Embodied Tree of Thoughts: Deliberate Manipulation Planning with Embodied World Model — http://arxiv.org/abs/2512.08188v1
[39] LongDS-Bench: On the Failure of Long-Horizon Agentic Data Analysis — http://arxiv.org/abs/2605.30434v3
[40] Embodied-R1.5: Evolving Physical Intelligence via Embodied Foundation Models — http://arxiv.org/abs/2606.11324v2
[41] Hy-Embodied-VLM-1.0: Efficient Physical-World Agents — http://arxiv.org/abs/2607.12894v1
[44] LLM-based ambiguity detection in natural language instructions for collaborative surgical robots — http://arxiv.org/abs/2507.11525v1
[45] Human-Robot collaboration in surgery: Advances and challenges towards autonomous surgical assistants — http://arxiv.org/abs/2507.11460v1
[49] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1
[50] Task adaptation of Vision-Language-Action model: 1st Place Solution for the 2025 BEHAVIOR Challenge — http://arxiv.org/abs/2512.06951v2
[51] Survey of Vision-Language-Action Models for Embodied Manipulation — http://arxiv.org/abs/2508.15201v2
[54] One Policy, Many Embodiments: Unified Camera-Centric Action Geometry Pre-training for Heterogeneous Embodied Manipulation — http://arxiv.org/abs/2608.26058v1
[55] MiMo-Embodied: X-Embodied Foundation Model Technical Report — http://arxiv.org/abs/2511.16518v2
[56] ME-VLM: A Unified VLM for Embodied Cognition and Agent Coordination — http://arxiv.org/abs/2609.24526v2
[57] Data Pyramid for Embodied Manipulation: A Survey — http://arxiv.org/abs/2607.24744v2
[58] HDDL 2.1: Towards Defining a Formalism and a Semantics for Temporal HTN Planning — http://arxiv.org/abs/2306.07353v1
[60] Breaking the Loop: A Hierarchical Dual-System Action Transformer with Latent World Models and Formal Verification — https://doi.org/10.5281/zenodo.21381253
[61] Breaking the Loop: A Hierarchical Dual-System Action Transformer with Latent World Models and Formal Verification — https://doi.org/10.5281/zenodo.21381252
[62] Humanoid Whole-Body Badminton via an Annealed Reinforcement Learning Curriculum — http://arxiv.org/abs/2511.11218v4
[69] Open X-Embodiment: Robotic Learning Datasets and RT-X Models — http://arxiv.org/abs/2310.08864v9
[74] DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset — http://arxiv.org/abs/2403.12945v2
[75] AI Robotics Open Source R&D Survey: Foundation Models, Datasets, Simulation, and Benchmarks Platforms (2023-2025) — https://doi.org/10.36227/techrxiv.175756484.48648133/v1
[79] LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning — http://arxiv.org/abs/2306.03310v2
[82] Forgetting and Imbalance in Robot Lifelong Learning with Off-policy Data — http://arxiv.org/abs/2204.05893v2
[85] Sim-to-Real Transfer in Deep Reinforcement Learning for Bipedal Locomotion — http://arxiv.org/abs/2511.06465v1
[86] DROPO: Sim-to-Real Transfer with Offline Domain Randomization — http://arxiv.org/abs/2201.08434v2
[87] Understanding Domain Randomization for Sim-to-real Transfer — http://arxiv.org/abs/2110.03239v2
[89] Robot Policy Evaluation for Sim-to-Real Transfer: A Benchmarking Perspective — http://arxiv.org/abs/2508.11117v1
[90] Digital Twin as a Service (DTaaS): A Platform for Digital Twin Developers and Users — http://arxiv.org/abs/2305.07244v2
[91] Co-Training Multimodal World Models and Diffusion-Guided Policies for Zero-Shot Contact-Rich Manipulation — https://doi.org/10.21203/rs.3.rs-7347334/v1
[94] Real-Time Digital Twins: Vision and Research Directions for 6G and Beyond — http://arxiv.org/abs/2301.11283v1
[95] MATTERIX: toward a digital twin for robotics-assisted chemistry laboratory automation — http://arxiv.org/abs/2601.13232v1
[97] tFUSOperator: Operator Learning for Transcranial Focused Ultrasound Digital Twins — http://arxiv.org/abs/2608.01839v1
[106] OpenVLA: An Open-Source Vision-Language-Action Model — http://arxiv.org/abs/2406.09246v3
[107] Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success — http://arxiv.org/abs/2502.19645v2
[109] OpenVLA: An Open-Source Vision-Language-Action Model — https://arxiv.org/abs/2406.09246
[110] Dexbotic: Open-Source Vision-Language-Action Toolbox — https://arxiv.org/abs/2510.23511
[111] RealMirror: A Comprehensive, Open-Source Vision-Language-Action Platform for Embodied AI — https://arxiv.org/abs/2509.14687
[112] LeRobot: An Open-Source Library for End-to-End Robot Learning — http://arxiv.org/abs/2602.22818v1
[113] Open-source vision-language-action models for robotics — https://doi.org/10.1007/s42791-025-00108-1
[114] StemVLA: An Open-Source Vision-Language-Action Model with Future 3D Spatial Geometry Knowledge and 4D Historical Representation — https://arxiv.org/abs/2602.23721
[115] VLA-Arena: An Open-Source Framework for Benchmarking Vision-Language-Action Models — https://arxiv.org/abs/2512.22539
[116] BLURR: A Boosted Low-Resource Inference for Vision-Language-Action Model — https://arxiv.org/abs/2512.11769
[117] VLA-Touch: Enhancing Vision-Language-Action Models

---

*Generated by research-bot · topic=`embodied-ai` · depth=`standard` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading · model=`deepseek-v4-flash` · sources=119 · duration=340s · 2026-10-04T22:25:19+00:00*
