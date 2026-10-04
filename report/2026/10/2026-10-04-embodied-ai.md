# 具身智能（Embodied AI）调研报告：从模块化流水线到 VLA 基础模型

**日期**：2026-10-04（UTC） ｜ **领域**：具身智能 / VLA（Vision-Language-Action）/ 机器人学习 / 仿真与 Sim2Real ｜ **检索源数量**：118 条编号来源（其中含明显主题漂移条目，见 §6.4） ｜ **证据纪律**：本报告仅引用编号来源 [1]–[118]；无编号的经典/种子资源以官方链接形式列出并标注 `> 待核实`；所有数字均标注口径来源，未取到热度信号者一律写 `> 待核实`。

---

## 摘要（Executive Summary）

1. **主线已从「单一 VLA 模型」转向「分层/双系统 VLA + 世界模型 + 效率优化」的组合范式**。双系统 VLA 已成为明确研究热点，但开源工作稀缺，[104] 是针对该缺口的综述＋实证＋开源模型；效率问题被单独系统化成综述议题 [100]。证据强度以 arXiv 预印本为主（B 级），仅 [20] 有明确同行评审 venue（RA-L，A 级）。
2. **世界模型的定位正从「视频生成演示」转向「与 VLA 联合训练 / 跨本体统一表征 / 部署期策略引导」**：[22] 声称统一 VLA 与世界模型并在 LIBERO 仿真达 97.4% 成功率（论文自报，未同行评审）；[24] 用 3D 流世界模型做跨本体操作；[20] 是有同行评审的 RGB-D 世界模型；[84] 声称潜在世界模型可在部署期引导 VLA 而无需微调。**但候选证据中没有一条给出世界模型在「策略评估」上的可验证增益，该维度证据缺失**。
3. **评测侧的可信度问题被两篇 2026 年预印本量化**：LIBERO-Para [113] 报告 VLA 在受控指令改写下性能下降 22–52 个百分点（7 个 0.6B–7.5B 配置）；LIBERO-VPro [114] 指出标准操作基准隐含「视觉观测干净、及时、一致」假设并施加闭环视觉扰动。这说明**现有 LIBERO 榜单排名可能高估真实泛化能力（待核实）**。
4. **Sim2Real 的关键结论是「评测层落后于仿真层」**：[116] 明确指出现有基于视觉的机器人仿真基准显著推进了操作研究，但面向真实应用的评测落后；因此**仿真 SOTA 与真机 SOTA 不可直接互换**。
5. **开源工程实践的复现瓶颈集中在数据/硬件/算力门槛与延迟约束**：[68] 将 LeRobot 定位为端到端机器人学习开源库；[81] 声称可在单张消费级 GPU 上以 30Hz 帧率、最高 480Hz 轨迹频率运行 π0 级别多视角 VLA（论文自报）。**GitHub star、下载量等热度信号在本轮证据中普遍缺失（待核实）**。
6. **证据池质量警告**：本轮候选证据含大量主题外条目（[1] 短视频参与度、[69] 越南语法律问答、[87] 单细胞 RNA 测序、[111] 短视频超分、[31] 神经影像等），说明召回对齐度不足；凡依赖这些条目的结论均不可用于具身智能判断。

---

## 一、关键前沿进展

### 1.1 VLA 架构：从单模型走向分层/双系统

- 双系统（Dual-System）VLA 已被明确定位为「具身智能研究的热点」，但社区缺少足够的开源实现用于性能分析与优化；[104] 以此为切口，给出结构设计总结对比＋实证分析＋开源双系统 VLA 模型。
  **证据四轴**：热度 citations=94（候选抽取块口径）[104]；权威 arXiv.org 预印本，未见同行评审 [104]；关注度 高（在候选证据中引用数最高之一）[104]；推荐度 ★★★★★（与本主题最直接相关且热度最高）[104]。
- 综述层面已形成多篇并行梳理：[97][98] 面向具身操作的 VLA 综述（同文两版链接）、[102] 从模块到里程碑与挑战的 VLA 解剖、[100] 面向效率的系统综述。
  **证据四轴**：热度 [100] citations=27（候选块口径），[97][98][102] `> 待核实`；权威 均为 arXiv 预印本，未见同行评审 [97][98][100][102]；关注度 中（[100] 有 27 次引用支撑）[100]，其余 `> 待核实`；推荐度 ★★★★☆（作为分类骨架可用，但需注意综述时效）[100][102]。
- 小规模与低资源路线同样活跃：[83] 提出 tiny-scale VLA 的有效范式，[96] 提出低资源推理加速方案 BLURR。**二者具体增益数字`> 待核实`**（候选块仅含摘要）。
  **证据四轴**：热度 `> 待核实`；权威 arXiv 预印本，未见同行评审 [83][96]；关注度 `> 待核实`；推荐度 ★★★☆☆（作为效率方向的补充线索，需核实实验口径）。

### 1.2 实时性与推理效率成为独立工程命题

- [81] 声称可将 π0 级别的多视角 VLA 在**单张消费级 GPU** 上以 30Hz 帧率、最高 480Hz 轨迹频率运行，从而支撑此前被认为大 VLA 无法完成的动态实时任务（论文自报，未同行评审）。
  **证据四轴**：热度 `> 待核实`；权威 arXiv 预印本 [81]，未见同行评审；关注度 中（实时 VLA 是部署核心瓶颈，但候选块无量化热度信号）；推荐度 ★★★★☆（若结论可复现，对 ROS2 部署路径意义重大，需核实硬件型号与模型版本）。
- [100] 指出 VLA 系统的核心瓶颈来自**巨大的计算与内存需求**，这是效率综述的立论前提。
  **证据四轴**：热度 citations=27 [100]；权威 arXiv 预印本 [100]；关注度 中 [100]；推荐度 ★★★★☆（效率维度的首选入口综述）。

### 1.3 世界模型 × VLA 的联合与引导

- [22] RynnVLA-002：世界模型以动作与视觉输入预测未来图像状态以学习环境物理并精炼动作生成，VLA 再从图像观测产生后续动作、反哺世界模型图像生成；论文声称统一框架在仿真与真机任务上均超过单独的 VLA 与世界模型，LIBERO 仿真成功率 **97.4%**。
  **证据四轴**：热度 citations=65（Semantic Scholar，候选块口径）[22]；权威 arXiv 预印本（cs.RO），候选块未标注同行评审，v1 2025-11-21、v3 2026-05-30 [22]；关注度 高（候选集中引用最高）[22]；推荐度 ★★★★☆（相关性最强，但 97.4% 必须标注为论文自报的仿真口径）。
- [84] DREAMSTEER：声称潜在世界模型可在**部署期引导 VLA 策略且无需任何微调**。**具体增益`> 待核实`**（候选块仅摘要）。
  **证据四轴**：热度 `> 待核实`；权威 arXiv 预印本 [84]，未见同行评审；关注度 `> 待核实`；推荐度 ★★★☆☆（若成立，对「世界模型如何低成本介入部署」是关键线索）。
- [86] 主张 VLA 可从与运动图像扩散（motion image diffusion）的联合学习中获益。**具体指标`> 待核实`**。
  **证据四轴**：热度 `> 待核实`；权威 arXiv 预印本 [86]；关注度 `> 待核实`；推荐度 ★★★☆☆（与 [22] 属同一「联合训练」思路的旁证）。

> **缺口**：候选证据中**没有任何一条**提供世界模型/生成式仿真在**策略评估（policy evaluation）**上相对端到端 VLA 的协议、一致性指标或与真机结果相关性的数据 [22][24][20]。该维度 `> 待核实`。

### 1.4 鲁棒性与失效模式成为新关注点

- LIBERO-Para [113]：在独立变化动作表达与物体指代的受控改写条件下，7 个 VLA 配置（0.6B–7.5B）出现**一致的 22–52 个百分点性能下降**，退化主要由物体层面的词汇替换驱动，即便简单同义词替换也会触发。
  **证据四轴**：热度 `> 待核实`（候选块未提供引用数）；权威 arXiv 预印本 arXiv:2603.28301v3（cs.LG，v1 2026-03-30，v3 2026-09-26），未见同行评审 [113]；关注度 低（无引用/star/榜单信号）；推荐度 ★★★☆☆（数字具体但仅来自摘要，需核实实验设置）。
- [85] 评估并缓解 VLA 中的**反事实失败（vision overrides language）**，即视觉证据压倒语言指令。**具体指标`> 待核实`**。
  **证据四轴**：热度 `> 待核实`；权威 arXiv 预印本 [85]；关注度 `> 待核实`；推荐度 ★★★★☆（与 [113] 构成「语言侧鲁棒性」与「视觉侧鲁棒性」的一对诊断视角）。
- LIBERO-VPro [114]：把评测焦点从静态任务成功率转向执行过程中的**闭环视觉鲁棒性**，通过扰动执行期可用视觉证据进行评估，并指出标准操作基准普遍假设视觉观测「干净、及时、一致」。
  **证据四轴**：热度 `> 待核实`；权威 arXiv 预印本 arXiv:2609.24350v1（cs.RO），未见同行评审 [114]；关注度 低；推荐度 ★★★☆☆（对「仿真评测是否反映真机鲁棒性」提供直接切入点，需核实任务/本体覆盖）。

### 1.5 新本体与新场景扩展

- [82] AeroManip-VLA：把 VLA 扩展到**空中操作**，用 RL 生成的演示解决数据稀缺。**具体成功率`> 待核实`**。
  **证据四轴**：热度 `> 待核实`；权威 arXiv 预印本（cs.RO）[82]，未见同行评审；关注度 `> 待核实`；推荐度 ★★★☆☆（代表「VLA 外推到非地面本体」的方向）。
- [58] Robot Trains Robot：面向人形机器人的真机策略自适应与学习，指出仿真 RL 已显著推进人形运动任务，但**从零开始的真机 RL 或从预训练策略自适应的做法仍罕见**。
  **证据四轴**：热度 `> 待核实`；权威 arXiv 预印本（cs.RO）[58]，未见同行评审；关注度 中（触及真机学习这一公认瓶颈）；推荐度 ★★★★☆（人形 + 真机自适应的直接线索）。
- [92] 面向 VLA 驾驶模型的推理期注意力引导（attention steering）；[94] 用组合式上下文微调 VLM 做复杂装配动作理解。**二者指标`> 待核实`**。
  **证据四轴**：热度 `> 待核实`；权威 arXiv 预印本 [92][94]，未见同行评审；关注度 `> 待核实`；推荐度 ★★★☆☆（体现 VLA 向驾驶/装配等垂直场景扩散）。

### 1.6 安全、认证与治理

- [88] 系统性梳理具身 AI 的风险、攻击与防御，指出具身 AI 把感知、认知、规划与交互整合进开放世界安全关键环境中的智能体。**为 2026 年条目（cs.CR）**。
  **证据四轴**：热度 `> 待核实`；权威 arXiv 预印本（cs.CR）[88]，未见同行评审；关注度 `> 待核实`；推荐度 ★★★★☆（安全维度目前最直接的系统性来源）。
- [74] 提出基于成熟度的具身 AI 认证框架与量化评分机制。**具体机制`> 待核实`**。
  **证据四轴**：热度 `> 待核实`；权威 arXiv 预印本（cs.AI）[74]；关注度 `> 待核实`；推荐度 ★★★☆☆（治理/认证方向的早期线索）。
- [2] 2025 年基础模型透明度指数（第三版）属通用基础模型治理，**与具身智能仅有间接关系**，不建议作为具身结论依据。
  **证据四轴**：热度 `> 待核实`；权威 arXiv（cs.AI）[2]；关注度 `> 待核实`；推荐度 ★★☆☆☆（相关度低）。

---

## 二、方法谱系（模块化 / 端到端 / 基础模型 / 世界模型）

### 2.1 模块化流水线（2018 之前 → 至今仍在使用）

**特征**：感知 → 任务/运动规划 → 控制器分离；可解释、可验证，但接口信息损失大、泛化差。

- 规划与形式化：HDDL 2.1 讨论时序 HTN 规划的形式化与语义 [6]；Isaacs 方法求解微分博弈的**最优控制律综合** [48]。
- 语言→任务的模块化衔接：[5] 面向协作手术机器人的 LLM 自然语言指令歧义检测；[3] 人机交互中的信任与接受度（TRUST 2025 workshop）。
- 抓取与运动规划：[117] 面向 Real Robot Challenge 的灵巧操作抓取与运动规划。

**证据四轴（代表条目 [5][6][117]）**：热度 `> 待核实`；权威 均为 arXiv 预印本 [5][6][117]，未见同行评审；关注度 低–中（属传统模块化路线的延续）；推荐度 ★★☆☆☆（作为谱系起点保留，非当前主线）。

### 2.2 端到端模仿学习（2022–2023 的范式转折）

**特征**：视觉/状态 → 动作 的直接映射，以行为克隆（BC）与扩散策略为主。

- **[47] ACT（Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware）**：用低成本硬件 + 动作分块实现精细双臂操作，发表于 **Robotics: Science and Systems（RSS）**，**citations=2553**（候选块口径）。这是把高精度双臂操作从「高端机器人 + 精确传感」拉低到「低成本 + 数据驱动」的转折点。
  **证据四轴**：热度 citations=2553 [47]；权威 RSS（同行评审会议，A 级）[47]；关注度 高（候选证据中引用数最高）[47]；推荐度 ★★★★★（端到端模仿学习的必读基石）。
- 演示质量与异构性：[25] 用偏好与表示学习区分并模仿异构人类演示，处理次优演示对数据质量的损害；[35] 从「收敛监督者」进行 on-policy 机器人模仿学习；[42] 在异构动作空间下做强化模仿。
  **证据四轴**：热度 `> 待核实`；权威 均 arXiv 预印本 [25][35][42]；关注度 低–中；推荐度 ★★★☆☆（数据质量问题在 VLA 时代以「数据引擎」形式复现）。
- 生成式策略：Diffusion Policy 类方法的轨迹选择问题被 [37] KDPE

## 参考来源

[1] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1
[2] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1
[3] TRUST 2025: SCRITA and RTSS @ RO-MAN 2025 — http://arxiv.org/abs/2509.11402v1
[4] One-Shot Reinforcement Learning for Robot Navigation with Interactive Replay — http://arxiv.org/abs/1711.10137v2
[5] LLM-based ambiguity detection in natural language instructions for collaborative surgical robots — http://arxiv.org/abs/2507.11525v1
[6] HDDL 2.1: Towards Defining a Formalism and a Semantics for Temporal HTN Planning — http://arxiv.org/abs/2306.07353v1
[7] A Simulation and Modeling of Access Points with Definition Language — http://arxiv.org/abs/1304.1836v2
[8] Breaking the Loop: A Hierarchical Dual-System Action Transformer with Latent World Models and Formal Verification — https://doi.org/10.5281/zenodo.21381253
[9] LongEval at CLEF 2025: Longitudinal Evaluation of IR Model Performance — http://arxiv.org/abs/2503.08541v1
[10] Breaking the Loop: A Hierarchical Dual-System Action Transformer with Latent World Models and Formal Verification — https://doi.org/10.5281/zenodo.21381252
[11] Closing the Sim-to-Real Loop Through Representation, Interface, and Feedback: How Dynamics-Aware Perception, Factored Policy Structure, and Embodied Feedback Jointly Determine Transfer Fidelity in Robot Learning — https://doi.org/10.5281/zenodo.20608583
[12] Closing the Sim-to-Real Loop Through Representation, Interface, and Feedback: How Dynamics-Aware Perception, Factored Policy Structure, and Embodied Feedback Jointly Determine Transfer Fidelity in Robot Learning — https://doi.org/10.5281/zenodo.20642294
[13] Is Sora a World Simulator? A Comprehensive Survey on General World Models and Beyond — http://arxiv.org/abs/2405.03520v2
[14] Correction: Neurorobotics for automotive manufacturing industry in era of embodied intelligence: a mini review — https://doi.org/10.3389/fnbot.2026.1829525
[15] AIn't Nothing But a Survey? Using Large Language Models for Coding German Open-Ended Survey Responses on Survey Motivation — http://arxiv.org/abs/2506.14634v3
[16] Agricultural Disruption — https://doi.org/10.1093/biosci/biz012
[17] State, Action, and Transition: A Bottleneck-Driven Survey of World Models — https://doi.org/10.2139/ssrn.6757578
[18] A Brief Survey on the Integration of Large Language Models with Marine Robotic Systems — https://doi.org/10.1109/MetroSea66681.2025.11245673
[19] Multimodal Large Language Models: A Survey of Vision-Language Integration, Architectures, and Applications — https://doi.org/10.5281/zenodo.21365120
[20] FlowDreamer: A RGB-D World Model With Flow-Based Motion Representations for Robot Manipulation — https://arxiv.org/abs/2505.10075
[21] Multimodal Large Language Models: A Survey of Vision-Language Integration, Architectures, and Applications — https://doi.org/10.5281/zenodo.21365121
[22] RynnVLA-002: A Unified Vision-Language-Action and World Model — https://arxiv.org/abs/2511.17502
[23] Plastic and Reconstructive Surgery Best Paper Awards 2025 — https://doi.org/10.1097/prs.0000000000012340
[24] 3DFlowAction: Learning Cross-Embodiment Manipulation from 3D Flow World Model — https://arxiv.org/abs/2506.06199
[25] Learning to Discern: Imitating Heterogeneous Human Demonstrations with Preference and Representation Learning — http://arxiv.org/abs/2310.14196v1
[26] Machine Learning for Health (ML4H) Workshop at NeurIPS 2018 — http://arxiv.org/abs/1811.07216v2
[27] The Barbados 2018 List of Open Issues in Continual Learning — http://arxiv.org/abs/1811.07004v1
[28] Deep-CLASS at ISIC Machine Learning Challenge 2018 — http://arxiv.org/abs/1807.08993v1
[29] QCD and High Energy Interactions: Moriond 2018 Theory Summary — http://arxiv.org/abs/1806.04982v2
[30] Evaluation of an open-source implementation of the SRP-PHAT algorithm within the 2018 LOCATA challenge — http://arxiv.org/abs/1812.05901v1
[31] Domain-randomized deep learning for neuroimage analysis — http://arxiv.org/abs/2507.13458v1
[32] The 4th Reactive Synthesis Competition (SYNTCOMP 2017): Benchmarks, Participants & Results — http://arxiv.org/abs/1711.11439v1
[33] DexPoint: Generalizable Point Cloud Reinforcement Learning for Sim-to-Real Dexterous Manipulation — http://arxiv.org/abs/2211.09423v2
[34] Proceedings of the Dialogue Robot Competition 2023 — http://arxiv.org/abs/2312.14430v5
[35] On-Policy Robot Imitation Learning from a Converging Supervisor — http://arxiv.org/abs/1907.03423v7
[36] Multi-objective Model-based Policy Search for Data-efficient Learning with Sparse Rewards — http://arxiv.org/abs/1806.09351v3
[37] KDPE: A Kernel Density Estimation Strategy for Diffusion Policy Trajectory Selection — http://arxiv.org/abs/2508.10511v2
[38] Deception Game: Closing the Safety-Learning Loop in Interactive Robot Autonomy — http://arxiv.org/abs/2309.01267v2
[39] Diffusion Co-Policy for Synergistic Human-Robot Collaborative Tasks — http://arxiv.org/abs/2305.12171v4
[40] Overview of AuTexTification at IberLEF 2023: Detection and Attribution of Machine-Generated Text in Multiple Domains — http://arxiv.org/abs/2309.11285v1
[41] Strategies to Harness the Transformers' Potential: UNSL at eRisk 2023 — http://arxiv.org/abs/2310.19970v1
[42] Reinforced Imitation in Heterogeneous Action Space — http://arxiv.org/abs/1904.03438v2
[43] UZH_CLyp at SemEval-2023 Task 9: Head-First Fine-Tuning and ChatGPT Data Generation for Cross-Lingual Learning in Tweet Intimacy Prediction — http://arxiv.org/abs/2303.01194v2
[44] Imitation Learning for End to End Vehicle Longitudinal Control with Forward Camera — http://arxiv.org/abs/1812.05841v1
[45] One-Shot Visual Imitation Learning via Meta-Learning — http://arxiv.org/abs/1709.04905v1
[46] MarsEclipse at SemEval-2023 Task 3: Multi-Lingual and Multi-Label Framing Detection with Contrastive Learning — http://arxiv.org/abs/2304.14339v1
[47] Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware — https://arxiv.org/abs/2304.13705
[48] The Synthesis of Optimal Control Laws Using Isaacs' Method for the Solution of Differential Games — http://arxiv.org/abs/2112.10849v2
[49] Isaac Lab: A GPU-Accelerated Simulation Framework for Multi-Modal Robot Learning — http://arxiv.org/abs/2511.04831v1
[50] Isaac Gym: High Performance GPU-Based Physics Simulation For Robot Learning — http://arxiv.org/abs/2108.10470v2
[51] ISAAC Newton: Input-based Approximate Curvature for Newton's Method — http://arxiv.org/abs/2305.00604v1
[52] SSM-CGM: Interpretable State-Space Forecasting Model of Continuous Glucose Monitoring for Personalized Diabetes Management — http://arxiv.org/abs/2510.04386v1
[53] TacEx: GelSight Tactile Simulation in Isaac Sim -- Combining Soft-Body and Visuotactile Simulators — http://arxiv.org/abs/2411.04776v1
[54] Multiresolution analysis on compact Riemannian manifolds — http://arxiv.org/abs/1404.5037v1
[55] Sim-to-Real gap in RL: Use Case with TIAGo and Isaac Sim/Gym — http://arxiv.org/abs/2403.07091v2
[56] The Sound of Simulation: Learning Multimodal Sim-to-Real Robot Policies with Generative Audio — http://arxiv.org/abs/2507.02864v2
[57] Physics Briefing Book — http://arxiv.org/abs/1910.11775v2
[58] Robot Trains Robot: Automatic Real-World Policy Adaptation and Learning for Humanoids — http://arxiv.org/abs/2508.12252v2
[59] Untangling Dense Knots by Learning Task-Relevant Keypoints — http://arxiv.org/abs/2011.04999v1
[60] Real2Sim or Sim2Real: Robotics Visual Insertion using Deep Reinforcement Learning and Real2Sim Policy Adaptation — http://arxiv.org/abs/2206.02679v1
[61] CMU's IWSLT 2025 Simultaneous Speech Translation System — http://arxiv.org/abs/2506.13143v1
[62] MLLP-VRAIN UPV system for the IWSLT 2025 Simultaneous Speech Translation Translation task — http://arxiv.org/abs/2506.18828v1
[63] RMIT-ADM+S at the SIGIR 2025 LiveRAG Challenge — http://arxiv.org/abs/2506.14516v2
[64] NTU Speechlab LLM-Based Multilingual ASR System for Interspeech MLC-SLM Challenge 2025 — http://arxiv.org/abs/2506.13339v2
[65] TalTech Systems for the Interspeech 2025 ML-SUPERB 2.0 Challenge — http://arxiv.org/abs/2506.01458v1
[66] DeDisCo at the DISRPT 2025 Shared Task: A System for Discourse Relation Classification — http://arxiv.org/abs/2509.11498v4
[67] NTIRE 2025 Challenge on Image Super-Resolution (x4): Methods and Results — http://arxiv.org/abs/2504.14582v3
[68] LeRobot: An Open-Source Library for End-to-End Robot Learning — http://arxiv.org/abs/2602.22818v1
[69] VLSP 2025 MLQA-TSR Challenge: Vietnamese Multimodal Legal Question Answering on Traffic Sign Regulation — http://arxiv.org/abs/2510.20381v1
[70] The AudioMOS Challenge 2025 — http://arxiv.org/abs/2509.01336v1
[71] TDCOSMO 2025: Cosmological constraints from strong lensing time delays — http://arxiv.org/abs/2506.03023v4
[72] Aligning Cyber Space with Physical World: A Comprehensive Survey on Embodied AI — http://arxiv.org/abs/2407.06886v8
[73] PANORAMA: The Rise of Omnidirectional Vision in the Embodied AI Era — http://arxiv.org/abs/2509.12989v1
[74] Toward Maturity-Based Certification of Embodied AI: Quantifying Trustworthiness Through Measurement Mechanisms — http://arxiv.org/abs/2601.03470v2
[75] Multi-Step Guided Diffusion for Image Restoration on Edge Devices: Toward Lightweight Perception in Embodied AI — http://arxiv.org/abs/2506.07286v1
[76] Docling: An Efficient Open-Source Toolkit for AI-driven Document Conversion — http://arxiv.org/abs/2501.17887v1
[77] Faith in AI can narrow the futures individuals consider — http://arxiv.org/abs/2603.28944v2
[78] Open Source Software Development Challenges: A Systematic Literature Review on GitHub — http://arxiv.org/abs/2003.10750v3
[79] Self-Supervised Policy Adaptation during Deployment — http://arxiv.org/abs/2007.04309v3
[80] Explainable Machine Learning for Public Policy: Use Cases, Gaps, and Research Directions — http://arxiv.org/abs/2010.14374v3
[81] Running VLAs at Real-time Speed — http://arxiv.org/abs/2510.26742v1
[82] AeroManip-VLA: Scalable Vision-Language-Action Learning for Aerial Manipulation with RL-Generated Demonstrations — http://arxiv.org/abs/2609.36915v1
[83] VLA-Adapter: An Effective Paradigm for Tiny-Scale Vision-Language-Action Model — http://arxiv.org/abs/2509.09372v2
[84] DREAMSTEER: Latent World Models Can Steer VLA Policies During Deployment Without Any Finetuning — http://arxiv.org/abs/2607.02865v1
[85] When Vision Overrides Language: Evaluating and Mitigating Counterfactual Failures in VLAs — http://arxiv.org/abs/2602.17659v2
[86] Robotic VLA Benefits from Joint Learning with Motion Image Diffusion — http://arxiv.org/abs/2512.18007v1
[87] DeepSeq: High-Throughput Single-Cell RNA Sequencing Data Labeling via Web Search-Augmented Agentic Generative AI Foundation Models — http://arxiv.org/abs/2506.13817v1
[88] Safety in Embodied AI: A Survey of Risks, Attacks, and Defenses — http://arxiv.org/abs/2605.02900v2
[89] A Survey: Learning Embodied Intelligence from Physical Simulators and World Models — http://arxiv.org/abs/2507.00917v3
[90] Robust Tabular Foundation Models — http://arxiv.org/abs/2512.03307v1
[91] Foundations of GenIR — http://arxiv.org/abs/2501.02842v1
[92] Inference-Time Attention Steering for Vision-Language-Action Driving Models — http://arxiv.org/abs/2608.17095v1
[93] Self-Evolving Autonomous Software Architectures Using Large-Scale Graph Neural Networks and Real-Time Big Data Feedback Loops for Economic Optimization and Cost-Efficient Resource Allocation — https://doi.org/10.63544/jbii.v5i5.188
[94] Compositional Context Fine-Tuning Vision-Language Model for Complex Assembly Action Understanding from Videos — http://arxiv.org/abs/2607.10797v1
[95] Task adaptation of Vision-Language-Action model: 1st Place Solution for the 2025 BEHAVIOR Challenge — http://arxiv.org/abs/2512.06951v2
[96] BLURR: A Boosted Low-Resource Inference for Vision-Language-Action Models — http://arxiv.org/abs/2512.11769v1
[97] Survey of Vision-Language-Action Models for Embodied Manipulation — http://arxiv.org/abs/2508.15201v2
[98] Survey of Vision-Language-Action Models for Embodied Manipulation — https://arxiv.org/abs/2508.15201
[99] Denghaoyuan123/Awesome-RL-VLA: Awesome-RL-VLA v0.1.0 — https://doi.org/10.5281/zenodo.17713487
[100] Efficient Vision-Language-Action Models for Embodied Manipulation: A Systematic Survey — https://arxiv.org/abs/2510.17111
[101] Denghaoyuan123/Awesome-RL-VLA: Awesome-RL-VLA v0.1.0 — https://doi.org/10.5281/zenodo.17713146
[102] An Anatomy of Vision-Language-Action Models: From Modules to Milestones and Challenges — https://arxiv.org/abs/2512.11362
[103] Denghaoyuan123/Awesome-RL-VLA: Awesome-RL-VLA v0.1.0 — https://doi.org/10.5281/zenodo.17713147
[104] OpenHelix: A Short Survey, Empirical Analysis, and Open-Source Dual-System VLA Model for Robotic Manipulation — https://arxiv.org/abs/2505.03912
[105] Overview of the Sensemaking Task at the ELOQUENT 2025 Lab: LLMs as Teachers, Students and Evaluators — http://arxiv.org/abs/2507.12143v1
[106] DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset — http://arxiv.org/abs/2403.12945v2
[107] Point Transformer V3 Extreme: 1st Place Solution for 2024 Waymo Open Dataset Challenge in Semantic Segmentation — http://arxiv.org/abs/2407.15282v1
[108] Open X-Embodiment: Robotic Learning Datasets and RT-X Models — http://arxiv.org/abs/2310.08864v9
[109] Open-Ended Learning Leads to Generally Capable Agents — http://arxiv.org/abs/2107.12808v2
[110] The RSNA Abdominal Traumatic Injury CT (RATIC) Dataset — http://arxiv.org/abs/2405.19595v1
[111] NTIRE 2025 Challenge on Short-form UGC Video Quality Assessment and Enhancement: KwaiSR Dataset and Study — http://arxiv.org/abs/2504.15003v1
[112] Autonomous Improvement of Instruction Following Skills via Foundation Models — http://arxiv.org/abs/2407.20635v2
[113] LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models — http://arxiv.org/abs/2603.28301v3
[114] LIBERO-VPro: Benchmarking Closed-Loop Visual Robustness of Robotic Foundation Models — http://arxiv.org/abs/2609.24350v1
[115] Annif at SemEval-2025 Task 5: Traditional XMTC augmented by LLMs — http://arxiv.org/abs/2504.19675v2
[116] Robot Policy Evaluation for Sim-to-Real Transfer: A Benchmarking Perspective — http://arxiv.org/abs/2508.11117v1
[117] Grasp and Motion Planning for Dexterous Manipulation for the Real Robot Challenge — http://arxiv.org/abs/2101.02842v1
[118] JENGA: Exploiting Counter-Based RowHammer Countermeasures to Break Real-Time Predictability — http://arxiv.org/abs/2609.01077v1


---

*Generated by research-bot · topic=`embodied-ai` · depth=`standard` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading · model=`deepseek-v4-flash` · sources=118 · duration=321s · 2026-10-04T03:09:48+00:00*
