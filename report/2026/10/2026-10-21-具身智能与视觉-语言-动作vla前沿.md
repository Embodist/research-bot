# 具身智能与视觉-语言-动作（VLA）前沿快照（2024–2026）

**报告日期**：2026-10-21（UTC）
**领域**：具身智能 / Vision-Language-Action（VLA）/ 机器人学习工程栈（训练框架、推理部署、数据集与基准）
**检索源**：候选证据共 33 条编号来源；经主题筛查剔除 8 条明显无关来源（临床问答 [11]、短视频参与度评测 [10]、机器生成文本检测 [14]、量子最优控制 [17]、eLife 视频条目 [19]、RT-middleware 日语报告 [20]、PE-RT 管材 DIN 标准 [21]、微分博弈 [26]），实际纳入引用 24 条。
**证据分级说明**：本批来源**全部为 arXiv 预印本或非顶会预印本/期刊**，未见 RSS/CoRL/ICRA/NeurIPS 等同行评审标注，故权威等级整体为 **B（预印本）/ C（二手综述）**；所有来源的**引用数、GitHub star、下载量在候选块中均未提供**，凡涉及热度一律标注 `> 待核实`，不做数字推测。表中“机构”为公开常识性归属，候选块未列作者名单，**具体作者以论文页为准（待核实）**。

---

## 1. 进展与热点（Progress & Hotspots）

**一句话增量判断**：2024–2026 的实质增量不在“更大的 VLA 主干”，而在 **① 推理层工程化（实时化、异步、推理时可控）② 数据与后训练效率 ③ 工具化/技能化的动作表征 ④ 开放权重与开放数据**；但**在本候选集合内没有任何一条给出公认 VLA 基准（LIBERO / SimplerEnv / Open X-Embodiment / RoboArena）上的 SOTA 刷新、第三方复现或真机部署证据** `> 待核实` [1][3][5][8][22]。

### 1.1 近 1–2 年关键进展（2025–2026）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| ART: Evolve VLA into an Agent with On-the-fly Tool-use | 2026（v1 08-14 / v3 09-24） | 论文作者团队（待核实） | `> 待核实` | arXiv 预印本 cs.RO，未见 venue [3] | 中 — 两个月内迭代至 v3，修订活跃，但无引用/star 数据 [3] | ★★★★☆ 与 VLA 主线最直接相关：工具注入压缩连续动作解空间、自建 30K 轨迹论证低数据依赖 [3] | http://arxiv.org/abs/2608.14047v3 | 泛化与数据效率为作者自评，缺独立基线 `> 待核实` |
| Inference-Time Attention Steering for VLA Driving Models | 2026-08-17 | 论文作者团队（待核实） | `> 待核实` | arXiv 预印本 cs.CV [1] | 低 — 无引用/讨论证据 [1] | ★★★☆☆ 不重训、不改权重的推理时可控性，量化剂量响应（约 17 cm 平均位移、最大约 140 cm 横向偏移）[1] | http://arxiv.org/abs/2608.17095v1 | 仅驾驶域 + 50 个合成场景，域外迁移未知 [1] |
| Your VLA Model Already Has Attention Heads For Path Deviation Detection | 2026-03-14 | 论文作者团队（待核实） | `> 待核实` | arXiv 预印本 cs.RO [5] | 低 — 摘要级片段，无数字 [5] | ★★★☆☆ 指向 VLA 幻觉与内部可解释信号复用，是可靠性方向的早期线索 [5] | http://arxiv.org/abs/2603.13782v1 | 候选证据缺实验指标，需读全文 `> 待核实` |
| XCoT-VLA: Executable Chain-of-Thought for VLA Driving | 2026-08 | 论文作者团队（待核实） | `> 待核实` | arXiv 预印本 cs.AI [15] | 低 — 无热度信号 [15] | ★★★☆☆ 指出自然语言 CoT 解码昂贵、难作动作表征，提出可执行 CoT [15] | http://arxiv.org/abs/2608.10976v1 | 与“语言 CoT 能否作动作表征”的路线之争相关（见 §4 [Debated]）[15] |
| Running VLAs at Real-time Speed | 2025 | 论文作者团队（待核实） | `> 待核实` | arXiv 预印本 cs.RO [22] | 中 — 实时推理是工程侧核心关切，但无量化热度 [22] | ★★★★☆ 单消费级 GPU 上 pi0 级多视角 VLA 达 30 Hz 帧率、最高 480 Hz 轨迹频率 [22] | http://arxiv.org/abs/2510.26742v1 | 直接回答“VLA 能否做动态任务”，是本批次最强的部署侧进展 [22] |
| EagleVLA: Onboard Real-Time Robot Control via Foresight-Aligned Asynchronous Inference | 2026（v6） | 论文作者团队（待核实） | `> 待核实` | arXiv 预印本，未见 venue [33] | 中 — 已迭代至 v6，说明作者持续打磨 [33] | ★★★★☆ 用异步推理逼近车载/机载实时控制，与 [22] 同属“推理栈重构”路线 [33] | http://arxiv.org/abs/2607.12659v6 | 开源与否未说明 `> 待核实` |
| BLURR: Boosted Low-Resource Inference for VLA | 2025-12 | 论文作者团队（待核实） | `> 待核实` | arXiv 预印本 cs.RO [8] | 中 — 推理加速为热点议题 [8] | ★★★★☆ 可插拔轻量 wrapper，实例化于 pi-zero，声称免重训/免改 checkpoint 即可在 commodity GPU 上高频控制 [8] | http://arxiv.org/abs/2512.11769v1 | 提示基准应报告时延/算力口径 [8] |
| Robotic VLA Benefits from Joint Learning with Motion Image Diffusion | 2025-12 | 论文作者团队（待核实） | `> 待核实` | arXiv 预印本 cs.RO [23] | 低 — 无热度信号 [23] | ★★★★☆ 指出纯模仿专家轨迹缺预测性运动推理，加入运动图像扩散联合学习 [23] | http://arxiv.org/abs/2512.18007v1 | 属“动作/未来预测表征”流派 [23] |
| How (and How Not) to Use Data Augmentation in VLA Post-Training | 2026-10 | 论文作者团队（待核实） | `> 待核实` | arXiv 预印本 [31] | 中 — 发布时间极新（本月），方法学争议性强 [31] | ★★★★☆ 系统讨论 VLA 后训练数据增强的正确/错误用法，直接对应“数据瓶颈” [31] | http://arxiv.org/abs/2610.05994v1 | 结论需独立复现 `> 待核实` |
| Impromptu VLA: Open Weights and Open Data for Driving VLA | 2025 | 论文作者团队（待核实） | `> 待核实` | arXiv 预印本 cs.CV [28] | 中 — 开放权重+8 万级数据，工程价值高 [28] | ★★★★☆ 面向非结构化 corner case 的开放权重/开放数据（80,000+ 片段）[28] | http://arxiv.org/abs/2505.23757v1 | 驾驶域，非通用操作基准 [28] |
| Generalist Robot Manipulation beyond Action Labeled Data | 2025-09 | 论文作者团队（待核实） | `> 待核实` | arXiv 预印本 [7] | 低 — 无热度信号 [7] | ★★★★☆ 明确指向“脱离动作标注数据”的通用操作学习，是数据瓶颈的正面回应 [7] | http://arxiv.org/abs/2509.19958v1 | 结论强度 `> 待核实` |
| Large VLM-based VLA Models for Robotic Manipulation: A Survey | 2025（v3） | 综述团队（待核实） | `> 待核实` | arXiv 综述 [6] | 中 — 领域内少见的系统性综述，便于建骨架 [6] | ★★★★★ 建议作为方法分类主骨架 [6] | http://arxiv.org/abs/2508.13073v3 | 综述时效 <2 年，覆盖较新 [6] |
| VLA and VLM for Robot Manipulation: A Comprehensive Review Towards Real-World Applications | 2026 | 综述团队（待核实） | `> 待核实` | Preprints.org 预印本（非同行评审）[12] | 低 — 平台权威性较弱 [12] | ★★★☆☆ 强调“面向真实应用”，可作二手线索，不宜作一手依据 [12] | https://doi.org/10.20944/preprints202606.0400.v1 | 证据等级 C [12] |

**SOTA 判定**：本候选集合中**无任何一条**报告公认基准的 SOTA 刷新或榜单排名 [1][3][5][22]。这只能说明“本批次存在证据缺口”，**不能推断领域没有 SOTA 刷新** `> 待核实`。

### 1.2 经典与奠基性工作（与上表严格区分）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| RT-2: VLA Models Transfer Web Knowledge to Robotic Control | 2023 | Google DeepMind（待核实作者名单） | `> 待核实` | arXiv 预印本；VLA 概念奠基作 [16] | 高 — 该文定义了“VLA”范式并被广泛引用（具体引用数 `> 待核实`）[16] | ★★★★★ 必读：VLM 知识迁移到机器人控制的范式起点 [16] | http://arxiv.org/abs/2307.15818v1 | 本报告“经典”与“最新”的分界线由此文起算 [16] |
| Open X-Embodiment: Robotic Learning Datasets and RT-X Models | 2023 | 多机构联合（待核实） | `> 待核实` | arXiv 预印本；跨本体数据联盟代表作 [13] | 高 — 跨本体数据集/模型的基准性资源（引用数 `> 待核实`）[13] | ★★★★★ 跨本体评测与数据谱系的锚点 [13] | http://arxiv.org/abs/2310.08864v9 | 任务数/本体清单需从原文表格核对 `> 待核实` [13] |
| OpenVLA: An Open-Source Vision-Language-Action Model | 2024-06 | 学术团队（待核实） | `> 待核实` | arXiv 预印本；开源 VLA 代表 [29] | 高 — 开源 VLA 的事实基线（star/下载 `> 待核实`）[29] | ★★★★★ 复现与二次开发的首选起点 [29] | http://arxiv.org/abs/2406.09246v3 | 权重与代码开放，具体许可 `> 待核实` [29] |
| Isaac Gym: GPU-Based Physics Simulation for Robot Learning | 2021 | NVIDIA（待核实） | `> 待核实` | arXiv 预印本；仿真基础设施经典 [30] | 高 — 大规模并行 RL/仿真的基础设施（引用 `> 待核实`）[30] | ★★★★☆ 理解“仿真侧算力拐点”的历史前提 [30] | http://arxiv.org/abs/2108.10470v2 | 非 VLA 专属，但支撑数据合成 [30] |
| Grasp and Motion Planning for Dexterous Manipulation (Real Robot Challenge) | 2021 | 竞赛团队（待核实） | `> 待核实` | arXiv 预印本 [2] | 低 — 本轮无新增引用信号 [2] | ★★★☆☆ 灵巧操作经典问题设定，提示“灵巧手”方向在 2024–2026 候选中几乎缺席 [2] | http://arxiv.org/abs/2101.02842v1 | 与 VLA 主线弱相关，仅作谱系补齐 [2] |
| RT-2 综述（二手） | 2025 | 期刊 AETR（待核实） | `> 待核实` | 非顶会期刊，二手综述 [18] | 低 [18] | ★★☆☆☆ 仅作背景解读，不作一手依据（证据等级 C）[18] | https://doi.org/10.56028/aetr.15.1.1423.2025 | 慎用其数字 [18] |

### 1.3 开源项目与工程栈

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| LeRobot: Open-Source Library for End-to-End Robot Learning | 2026 | Hugging Face 生态（待核实） | `> 待核实`（star 未提供） | arXiv 预印本 + 开源库 [25] | 高 — 端到端机器人学习的开源入口，降低遥操作/数据采集门槛（社区规模 `> 待核实`）[25] | ★★★★★ 工程落地首选脚手架 [25] | http://arxiv.org/abs/2602.22818v1 | 与 ROS2 的集成方式未在候选块说明 `> 待核实` [25] |
| OpenVLA | 2024 | 学术团队（待核实） | `> 待核实` | 开源权重 [29] | 高 [29] | ★★★★★ 开源 VLA 基线 [29] | http://arxiv.org/abs/2406.09246v3 | — |
| GR00T N1: Open Foundation Model for Generalist Humanoid Robots | 2025-03 | NVIDIA（待核实） | `> 待核实` | arXiv 预印本 + 厂商开源模型 [24] | 高 — 人形通用基础模型的厂商级开源，产业关注度高（star/下载 `> 待核实`）[24] | ★★★★★ 人形本体的开源基础模型参考 [24] | http://arxiv.org/abs/2503.14734v2 | 真机部署规模 `> 待核实` [24] |
| Impromptu VLA（开放权重+开放数据） | 2025 | 论文作者团队（待核实） | `> 待核实` | arXiv 预印本，开放权重/数据 [28] | 中 [28] | ★★★★☆ 驾驶域开放权重与 8 万级数据 [28] | http://arxiv.org/abs/2505.23757v1 | 许可条款 `> 待核实` [28] |
| BLURR（pi-zero 推理 wrapper） | 2025-12 | 论文作者团队（待核实） | `> 待核实` | 预印本，可插拔工程件 [8] | 中 [8] | ★★★★☆ 免重训加速，适合作为部署层对照 [8] | http://arxiv.org/abs/2512.11769v1 | 是否开源 `> 待核实` [8] |
| EagleVLA | 2026 | 论文作者团队（待核实） | `> 待核实` | 预印本 [33] | 中 [33] | ★★★★☆ 异步推理的实时控制方案 [33] | http://arxiv.org/abs/2607.12659v6 | 代码/权重 `> 待核实` [33] |
| Isaac Gym | 2021 | NVIDIA（待核实） | `> 待核实` | 官方仿真基础设施 [30] | 高 [30] | ★★★★☆ 数据合成与并行仿真底座 [30] | http://arxiv.org/abs/2108.10470v2 | — |

### 1.4 数据集与基准

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Open X-Embodiment | 2023 | 多机构联合（待核实） | `> 待核实` | 跨本体数据集联盟 [13] | 高 [13] | ★★★★★ 可比性最高的跨本体资源之一 [13] | http://arxiv.org/abs/2310.08864v9 | 任务数/本体数需查原文表 `> 待核实` [13] |
| Impromptu VLA Dataset | 2025 | 论文作者团队（待核实） | `> 待核实` | 开放数据（80,000+ 片段）[28] | 中 [28] | ★★★★☆ 驾驶 corner case 的开放数据集 [28] | http://arxiv.org/abs/2505.23757v1 | 真机/仿真口径 `> 待核实` [28] |
| ART 工具使用数据集（30K 轨迹/示范） | 2026 | 论文作者自建 [3] | `> 待核实` | 非公开基准，未说明是否开源 [3] | 低 [3] | ★★★☆☆ 评估“数据效率”主张的关键对象，但可用性 `> 待核实` [3] | http://arxiv.org/abs/2608.14047v3 | 作者称“远小于基线方法所用数据” [3] |
| Physical AI World Model Synthetic dataset（50 lane-change 子集） | 2026 | 未说明发布方 [1] | `> 待核实` | 合成数据，无独立主页 [1] | 低 — 仅 1 篇预印本使用 [1] | ★★☆☆☆ 仅作“评测口径碎片化”的实例 [1] | http://arxiv.org/abs/2608.17095v1 | 50 场景、单模型、纯合成 [1] |
| LIBERO / SimplerEnv / RoboArena / DROID | — | — | `> 待核实` | `> 待核实` | `> 待核实` | — | — | **本候选集合未提供任何来源**，无法给出任务数/本体/仿真-真机口径，须补充检索 [1][5] |

---

## 2. 工业界与产品（Industry & Product）

**一句话增量判断**：本批次可核实的“产业信号”基本是**厂商/学术团队的开源发布 + 推理栈工程化**，而非量产、出货或客户部署数据；商业化数字全为 `> 待核实`。

- **厂商级开源基础模型**：NVIDIA GR00T N1 作为“开放通用人形机器人基础模型”发布，是候选集合中唯一的明确厂商开源基础模型条目 [24]；其真机部署规模、许可与生态采用度 `> 待核实`。
- **开源工程栈下沉**：LeRobot 定位为端到端机器人学习开源库，强调低成本遥操作与数据采集的可获得性，说明“数据采集-训练-部署”链路正在被工具化 [25]；具体 star、下载量与工业采用案例 `> 待核实`。
- **实时性从论文卖点变成产品前提**：单消费级 GPU 上 pi0 级 VLA 达到 30 Hz 帧率、最高 480 Hz 轨迹频率 [22]，配合免重训的轻量推理 wrapper（BLURR on pi-zero）[8] 与异步推理的 EagleVLA [33]，构成“VLA 上机可用”的工程三角；但三者均为预印本自评，**无独立第三方在真机长时间运行下的复现** `> 待核实` [8][22][33]。
- **开放权重/开放数据的商业含义**：Impromptu VLA 以开放权重+8 万级片段降低驾驶域 VLA 的准入门槛 [28]；其对供应链与差异化竞争的影响属推测（见 §7 假设 H3）。
- **ROS2 部署层**：候选集合中**没有任何一条**讨论 ROS2 集成、实时控制节点、通信时延或 DDS 配置 `> 待核实`。这意味着本报告无法对“VLA 在 ROS2 工程栈中的落地现状”给出有证据的判断——这是本次调研最明显的工业界证据缺口。

---

## 3. 蓝海与缺口（Blue Ocean & Gaps）

**一句话增量判断**：最大的蓝海不在“再训一个更大的 VLA”，而在 **评测基础设施、推理时延口径、可靠性监控、工具/技能库标准化、以及 ROS2 部署中间件**——这些方向在候选集合中出现频率极低或完全缺席。

1. **第三方独立评测与复现平台（缺口最大）**：候选证据中所有实验均为作者自评，典型如单模型、50 个合成换道场景 [1]；没有榜单、没有第三方复现报告 [1][3][5]。谁先做出“VLA 版 lm-eval-harness + 真机抽检”的可信评测，谁就占据基础设施位。
2. **基准应纳入推理时延/算力口径**：现有 VLA 评测只报成功率类指标，而 [8][22][33] 证明时延是硬约束；“成功率 + 时延 + 显存 + 轨迹频率”的联合指标尚无标准 `> 待核实` [8][22][33]。
3. **VLA 可靠性 / 幻觉在线监控**：把模型内部注意力头复用于路径偏离检测 [5]，以及推理时有界注意力偏置 [1]，共同指向“不改权重即可诊断/纠偏”的低成本可靠性层；但 [5] 缺量化指标，[1] 仅限驾驶 `> 待核实` [1][5]。
4. **工具化 / 技能库的动作表征**：ART 用工具注入把连续动作解空间压缩、并以 30K 轨迹论证低数据依赖 [3]；与之互补的是 motion image diffusion 的预测性联合学习 [23]。**“技能库接口标准 + 工具调用失败恢复”尚无人系统研究** `> 待核实` [3][23]。
5. **脱离动作标注的学习**：[7] 明确以“beyond action labeled data”为题，说明数据瓶颈已被识别，但候选集合中没有该路线的可复现基准 `> 待核实` [7]。
6. **后训练数据增强的方法学**：[31] 直接讨论“该用/不该用”数据增强，属于少见的方法学纠偏型工作，但结论待独立复现 `> 待核实` [31]。
7. **灵巧手 / 灵巧操作**：候选集合中唯一相关条目是 2021 年的 Real Robot Challenge 抓取与运动规划 [2]，2024–2026 窗口内**无新增灵巧操作 VLA 证据** `> 待核实`。
8. **ROS2 / 实时中间件层**：完全缺席（同 §2）`> 待核实`。

---

## 4. 瓶颈与拐点（Bottleneck & Inflection）

**一句话增量判断**：瓶颈正在从“**模型能力**”迁移到“**推理成本 + 数据质量 + 评测可信度**”；三个可观测的拐点信号已经出现，但均由作者自评，尚未被独立验证。

| 瓶颈 | 证据 | 拐点信号 | 判断 |
|---|---|---|---|
| 推理算力/时延 | pi0 级 VLA 需专门优化才能在单消费级 GPU 上达 30 Hz/480 Hz [22]；免重训 wrapper 才使 pi-zero 可用于高频控制 [8]；车载侧需异步推理 [33] | 消费级 GPU 上的实时化方案密集出现（2025-12 至 2026-07）[8][22][33] | **临近拐点**（较大概率）；但均为预印本自评，缺少跨硬件第三方基准 `> 待核实` |
| 数据规模与标注成本 | ART 以“远小于基线”的 30K 轨迹论证低数据依赖 [3]；[7] 直接研究脱离动作标注；[31] 讨论后训练数据增强的对错 [7][31] | 从“堆数据”转向“数据配方 + 工具化压缩解空间” [3][31] | **方向已变，量级未定**（推测） |
| 评测可信度 | 单模型 + 50 个合成场景 + 自选指标 [1]；候选集合无榜单/复现 [1][5] | 尚无；这是**最未解决的瓶颈** | **未见拐点** `> 待核实` |
| 动作表征 `[Debated]` | 自然语言 CoT 开放式、解码昂贵、难作面向动作的表征 [15] vs 工具/离散技能调用压缩连续空间 [3] vs 运动图像扩散做预测性推理 [23] | 多条路线并行、无共识指标 | **存在争议**，短期内不会收敛 [3][15][23] |
| 真机与跨本体验证 | 全部候选以自建数据/合成子集评估 [1][3]；跨本体仅见 2023 年 Open X-Embodiment [13] | 无 2024–2026 新增跨本体大规模验证证据 | **证据真空** `> 待核实` |

---

## 5. 社会·政策·国际（Society, Policy & Geopolitics）

**一句话增量判断**：**本周期在候选证据中无显著变化**——33 条来源中没有任何监管文件、标准草案、出口管制或劳动影响类材料，因此本章只能给出“证据缺口声明 + 可检验的推测”，不做事实断言。

- **证据缺口（确定）**：候选集合不含政策/标准/法规来源；任何关于“VLA 监管”“人形机器人准入”“数据跨境”的结论均 `> 待核实`。
- **可观察的结构性事实（较大概率）**：开放权重与开放数据范式在扩散——OpenVLA [29]、GR00T N1 [24]、Impromptu VLA [28]、Open X-Embodiment [13] 构成“开放模型 + 开放数据 + 跨机构数据联盟”的组合。这类开放范式客观上降低了单一机构对基础模型的垄断度 [13][24][28][29]。
- **[P] 推测（低置信度）**：随着 VLA 进入车载与人身附近场景，“可监控/可解释”可能成为准入要求，而内部注意力头诊断 [5] 与推理时可控偏置 [1] 恰好提供了低成本合规接口。**若到 2027 年底出现引用此类内省方法的监管/标准文本，则该推测成立**；否则否证。依据链：可靠性方法出现 [1][5] → 监管通常滞后于能力 → 可能被引用为合规手段。
- **国际协作与供应链**：仿真基础设施（Isaac Gym [30]）与开源训练库（LeRobot [25]）集中在少数厂商/社区手中，可能形成“工具链依赖”；具体地缘影响 `> 待核实`。

---

## 6. 资本与生态（Capital & Ecosystem）

**一句话增量判断**：候选证据只能支撑“**开源生态在扩张、工具链在收敛**”这一定性判断；融资额、并购、人才流动数据在来源中**完全缺席**，一律 `> 待核实`。

- **生态收敛信号（较大概率）**：LeRobot 把端到端机器人学习工具化 [25]，OpenVLA 提供开源基线 [29]，GR00T N1 提供人形开源基础模型 [24]，Open X-Embodiment 提供跨机构数据 [13]——四者叠加使“小团队复现 VLA”的边际成本显著下降。
- **推理侧创业/工程机会（推测）**：BLURR [8]、实时化方案 [22]、EagleVLA [33] 显示“VLA 推理加速与部署”已成独立技术层，通常是工程型团队/厂商的切入口 `> 待核实`（无融资数据）。
- **开源治理风险（C 级证据）**：一般性 GitHub 开源项目治理研究综述指出开源项目在维护者激励、可持续性上存在系统性挑战 [27]；该文非机器人领域，仅作类比线索，**不可直接套用于 VLA 项目** `> 待核实` [27]。
- **数据/榜单的“准公共品”属性**：谁维护榜单与数据，谁就获得生态话语权——但本候选集合未提供任何榜单运营方信息 `> 待核实` [13][28]。

---

## 7. 信号与预测（Signals & Forecast）

**一句话增量判断**：未来 6–18 个月最可能发生的变化不是“新 SOTA 模型”，而是**评测口径与部署层的标准化**；以下预测均写成可证伪假设。

| 编号 | 可证伪假设 [P] | 依据链 | 置信度 | 否证条件 |
|---|---|---|---|---|
| H1 | 到 2027-Q2，主流 VLA 论文/榜单将把**推理时延、吞吐（Hz）、显存**列为标准报告项 | 实时化工作密集出现 [8][22][33]，且实时性是产品前提 | 较大概率（中） | 2027-Q2 前检索到的主流 VLA 基准页面仍只报成功率类指标 |
| H2 | 12 个月内出现**≥1 个跨本体的工具化/技能库 VLA 第三方复现** | ART 提出工具注入并自建 30K 轨迹 [3]，路线可插拔、易复现 | 推测（低-中） | 2027-10 前未检索到任何独立团队复现工具化 VLA 的代码或报告 [3] |
| H3 | **开放权重 + 开放数据**成为驾驶域 VLA 的默认发布方式 | Impromptu VLA 提供开放权重与 80,000+ 片段 [28] | 推测（中） | 2027 年内新发布的驾驶 VLA 论文中，开放权重比例未上升（需榜单/仓库统计） |
| H4 | 出现**VLA 可靠性/幻觉在线监控**的独立模块（非端到端重训） | 内部注意力头可检测路径偏离 [5] + 推理时有界注意力偏置 [1] | 推测（低-中） | 2027-10 前该方向仍只有单篇摘要级证据、无量化基准 [5] |
| H5 | **ROS2 部署层**出现标准化 VLA 推理节点/接口（如统一 action server） | 当前候选集合零覆盖，说明工程需求未被论文层承接 `> 待核实` | 未知（需数据） | 若 2027 年前 ROS2 生态仍无相关标准包，则假设失效 |

**Watchlist（持续关注）**

1. **推理实时化**：pi0 级 30 Hz / 480 Hz 路线 [22] 与异步推理 [33]、免重训 wrapper [8] 是否被独立复现并给出跨硬件曲线。
2. **工具化 VLA**：ART [3] 的 v3 后续版本与是否开源 30K 轨迹数据集。
3. **可靠性内省**：注意力头故障检测 [5] 是否补出量化指标与对比实验。
4. **数据配方**：后训练数据增强的方法学结论 [31] 能否被独立复现。
5. **综述基线**：[6] 的 taxonomy 是否被后续工作广泛采用，可作为“领域共识度”的代理指标。
6. **空白区**：ROS2 集成、灵巧手 VLA、第三方榜单——本批次零覆盖，建议下一轮定向检索 `> 待核实`。

---

## 参考来源

[1] Inference-Time Attention Steering for Vision-Language-Action Driving Models — http://arxiv.org/abs/2608.17095v1
[2] Grasp and Motion Planning for Dexterous Manipulation for the Real Robot Challenge — http://arxiv.org/abs/2101.02842v1
[3] Evolve Vision-Language-Action Model into an Agent with On-the-fly Tool-use — http://arxiv.org/abs/2608.14047v3
[4] Compositional Context Fine-Tuning Vision-Language Model for Complex Assembly Action Understanding from Videos — http://arxiv.org/abs/2607.10797v1
[5] Your Vision-Language-Action Model Already Has Attention Heads For Path Deviation Detection — http://arxiv.org/abs/2603.13782v1
[6] Large VLM-based Vision-Language-Action Models for Robotic Manipulation: A Survey — http://arxiv.org/abs/2508.13073v3
[7] Generalist Robot Manipulation beyond Action Labeled Data — http://arxiv.org/abs/2509.19958v1
[8] BLURR: A Boosted Low-Resource Inference for Vision-Language-Action Models — http://arxiv.org/abs/2512.11769v1
[12] Vision-Language-Action and Vision Language Models for Robot Manipulation: A Comprehensive Review Towards Real-World Applications — https://doi.org/10.20944/preprints202606.0400.v1
[13] Open X-Embodiment: Robotic Learning Datasets and RT-X Models — http://arxiv.org/abs/2310.08864v9
[15] XCoT-VLA: Executable Chain-of-Thought for Vision-Language-Action Driving — http://arxiv.org/abs/2608.10976v1
[16] RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control — http://arxiv.org/abs/2307.15818v1
[18] RT-2: Vision-Language-Action Models for Generalizable Robotic Control: A Comprehensive Review — https://doi.org/10.56028/aetr.15.1.1423.2025
[22] Running VLAs at Real-time Speed — http://arxiv.org/abs/2510.26742v1
[23] Robotic VLA Benefits from Joint Learning with Motion Image Diffusion — http://arxiv.org/abs/2512.18007v1
[24] GR00T N1: An Open Foundation Model for Generalist Humanoid Robots — http://arxiv.org/abs/2503.14734v2
[25] LeRobot: An Open-Source Library for End-to-End Robot Learning — http://arxiv.org/abs/2602.22818v1
[27] Open Source Software Development Challenges: A Systematic Literature Review on GitHub — http://arxiv.org/abs/2003.10750v3
[28] Impromptu VLA: Open Weights and Open Data for Driving Vision-Language-Action Models — http://arxiv.org/abs/2505.23757v1
[29] OpenVLA: An Open-Source Vision-Language-Action Model — http://arxiv.org/abs/2406.09246v3
[30] Isaac Gym: High Performance GPU-Based Physics Simulation For Robot Learning — http://arxiv.org/abs/2108.10470v2
[31] How (and How Not) to Use Data Augmentation in VLA Post-Training — http://arxiv.org/abs/2610.05994v1
[33] EagleVLA: Towards Onboard Real-Time Robot Control via Foresight-Aligned Asynchronous Inference — http://arxiv.org/abs/2607.12659v6

---

*Generated by research-bot · topic=`具身智能与视觉-语言-动作vla前沿` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`deepseek-v4-flash` · sources=33 · duration=185s · 2026-10-21T22:18:49+00:00*
