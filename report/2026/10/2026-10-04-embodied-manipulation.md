# 具身智能·灵巧操作（Dexterous Manipulation & Grasping）深度调研报告

**日期**：2026-10-04（UTC）
**领域**：具身智能 / 灵巧手与多指操作、抓取合成、接触丰富任务、模仿学习与扩散策略、触觉力感知、双臂协同
**检索源**：候选证据来源 54 条（编号 [1]–[54]）；本报告实际引用 40 条
**证据分级口径**：A = 同行评审论文 / 官方技术报告；B = arXiv 预印本 / 官方仓库 / 官方数据集主页；C = 第三方复现 / 榜单；D = 社区内容；E = 不可用

> **证据覆盖声明（必读）**：本轮结构化检索在子问题 **q1（2024–2026 前沿进展与 SOTA）**、**q4（数据集与基准）**、**q6（开放问题与争议）** 上返回的 `findings` 为**空**；q2、q3、q5 的候选中包含明显跨域噪声条目（如 [30] 短视频参与度预测挑战、[52] 拓扑深度学习挑战赛、[12] RowHammer 实时性安全分析）。因此本报告在「SOTA 定量对比」「数据集可比性」「争议与负面结果」三处主要以**证据缺口说明 + `> 待核实` 标注**呈现，而非给出结论性判断。本批证据中**没有任何一条被确认为同行评审主会论文（A 级）**，绝大多数为 arXiv 预印本（B 级），请按此权重使用本报告。

---

## 摘要（Executive Summary）

1. **本轮检索的覆盖度极不均衡，这本身就是最重要的发现。** 六个子问题中三个（q1/q4/q6）零 findings，而 q2/q3/q5 的候选池混杂了大量与具身智能无关的论文（[30][52][12]）。因此本文**无法给出「2024–2026 灵巧操作 SOTA 榜单」**，只能给出可核查的证据点与明确的缺口清单。任何需要「哪个模型在哪个 benchmark 上达到多少成功率」的决策，都必须先补齐一次针对 arXiv cs.RO + OpenReview + GitHub/HuggingFace 的定向深潜。

2. **触觉与 VLA 的融合是当前最清晰的「新范式信号」。** T-Rex（2026）明确指出当代 VLA 操作模型「要么忽略触觉模态，要么只限于静态线索编码器」，并提出触觉反应式（tactile-reactive）灵巧操作 [51]。这与更早的触觉表征自监督预训练 [48]、触觉皮肤剪切/法向力感知 [53]、GelSight 触觉图像 sim2real 生成 [50]、低成本触觉手指硬件 [47] 形成一条可辨识的技术链，但**该链条上的量化增益（相对纯视觉策略提升多少）在本批证据中完全缺失** `> 待核实`。

3. **长程/柔性物体灵巧操作正在形成独立子领域。** 线缆操作的首个系统性 taxonomy + 多指手设计 + 长程操作工作（2025）指出既有研究依赖两指夹爪、难以复现人类级线缆操作 [24]；双臂绳索操作工作则以 ACT 为基线，比较不同观察空间对少样本泛化的影响 [4]。

4. **「模仿学习 + 任务与运动规划（TAMP）」的混合栈是长程任务工程化的现实答案。** SViP（2025）用语义场景图监控器把人类示教切分为可调度的双臂/单臂原语，并训练切换条件生成器，明确针对 visuomotor 策略在少样本示教下泛化受限、长程误差累积的问题 [9]。同类工程范式在双臂动作分块系列（InterACT [40]、Bi-ACT [43]、Stabilize to Act [41]）中亦有体现。

5. **扩散策略的改进重心正在从「架构」移向「推理与轨迹选择」。** KDPE（2025）针对 Diffusion Policy 的轨迹选择环节引入核密度估计策略 [16]；Diffusion Policy Policy Optimization（2024）把策略优化引入扩散策略 [15]；而官方实现仓库仍是社区事实上的复用基线 [46]。**注意**：本批证据中未出现 LeRobot / OpenVLA / RoboCasa 等训练框架的一手评估数据，q3 的「开源工程栈」问题在当前证据下无法回答（仅有 [17] 的 LeRobot 库论文条目）。

6. **ROS2 / 机器人中间件集成的证据为零。** q3 的候选证据中没有出现 DDS、rclcpp、MoveIt、ros2_control 等任何中间件内容，唯一被抽取到的「系统底层」论文 [12] 主题为 RowHammer 对实时可预测性的影响，与机器人工程栈无直接关联。**这是一条明确且严重的证据缺口**，若选型需要 ROS2 落地路径，必须重新检索。

7. **sim2real 的评测规范已有原则性建议，但缺可执行基准。** Robot Policy Evaluation for Sim-to-Real Transfer（RSS 2025 Workshop，2025）提出三条建议：使用高视觉保真度仿真、按任务复杂度与场景扰动系统化加大难度、量化真机与仿真表现的一致性 [10]。该文属 workshop 观点性文章，**不是可运行工具链**，且本批证据中未提供任何对齐指标的实现 `> 待核实`。

8. **可复现性与维护活跃度无法评估。** 除 [46]（GitHub star = 4609，检索快照）外，本批候选论文**均未在摘要中提供代码/权重链接、任务数、硬件配置或成功率口径**，无法交叉验证「可复现性」与「维护活跃度」；GitHub 生态层面的度量方法论可参考开源软件挑战的系统综述 [5] 与基于 GitHub 内容的缺陷预测模型 [6]，但这两篇并非机器人领域。

---

## 一、关键前沿进展（近 1–2 年）

> **本节定位说明**：q1 的 findings 为空，故本节不构成「SOTA 综述」，而是**从 q2/q3/q5 候选中筛出的 2024–2026 年条目重组**，并对每条标注「验证口径是否可得」。凡候选块未给出 benchmark / 任务数 / 硬件 / 成功率者，一律标 `> 待核实`。

### 1.1 触觉反应式 VLA（Tactile-Reactive VLA）

**T-Rex: Tactile-Reactive Dexterous Manipulation（2026，cs.RO）**
- **证据**：摘要称「动态响应触觉信号的能力长期被视为敏捷人类级灵巧性的关键」，但当代基于学习的 VLA 操作模型「一般要么忽略触觉模态，要么受限于静态线索编码器」[51]。
- **热度证据**：`> 待核实`（候选块无引用数、star、下载量）[51]
- **权威证据**：arXiv 预印本（cs.RO），候选块未标注会议/期刊，无同行评审信息 [51]
- **关注度**：低 — 依据为本批证据中无引用/star/榜单信号 [51]
- **推荐度**：★★★★☆ — 直接命中「触觉 × VLA」这一前沿交叉点，是 q5 中与「触觉集成方式」最相关的一条；但**在补齐真机硬件、任务数与成功率口径前不应作为选型依据** [51]
- **验证口径**：benchmark / 任务数 / 硬件 `> 待核实` [51]

### 1.2 生成式策略的推理侧工程

**KDPE: A Kernel Density Estimation Strategy for Diffusion Policy Trajectory Selection（2025）**
- **证据**：摘要指出 Diffusion Policy 依赖扩散模型把随机点去噪为机器人动作轨迹，并称近期方法用生成模型建模条件动作分布；KDPE 提出以核密度估计（KDE）策略进行轨迹选择 [16]。
- **热度证据**：`> 待核实` [16]
- **权威证据**：arXiv 预印本（arXiv:2508.10511v2，cs.RO），候选块未标注会议/期刊 [16]
- **关注度**：低 — 无引用数、star、下载量或榜单信号 [16]
- **推荐度**：★★★☆☆ — 对 Diffusion Policy 训练/推理栈是**低改造成本的改进方向**，但候选块未提供开源实现与实验口径，复用前必须核实代码可用性 [16]
- **验证口径**：任务数 / 硬件 / 成功率 `> 待核实` [16]

**Diffusion Policy Policy Optimization（2024）**
- **证据**：候选块仅给出标题与编号，未提供摘要细节 [15]。
- **热度/权威/关注度**：`> 待核实`（候选块无摘要、引用数、venue 信息）[15]
- **推荐度**：★★★☆☆ — 作为「扩散策略 × 策略优化」方向的关键词入口值得检索原文，但**当前证据不足以支撑任何结论** [15]

### 1.3 模仿学习 + TAMP 的混合架构

**SViP: Sequencing Bimanual Visuomotor Policies with Object-Centric Motion Primitives（2025）**
- **证据**：摘要称其「seamlessly integrates visuomotor policies into task and motion planning (TAMP)」，用语义场景图监控器（semantic scene graph monitor）把人类示

## 参考来源

[1] One-Shot Reinforcement Learning for Robot Navigation with Interactive Replay — http://arxiv.org/abs/1711.10137v2
[2] ALOHA 2: An Enhanced Low-Cost Hardware for Bimanual Teleoperation — http://arxiv.org/abs/2405.02292v1
[3] Mobile ALOHA: Learning Bimanual Mobile Manipulation with Low-Cost Whole-Body Teleoperation — http://arxiv.org/abs/2401.02117v1
[4] Learning Sim-Grounded Policies for Bimanual Rope Manipulation from Human Teleoperation Data — http://arxiv.org/abs/2605.16043v1
[5] Open Source Software Development Challenges: A Systematic Literature Review on GitHub — http://arxiv.org/abs/2003.10750v3
[6] Estimating defectiveness of source code: A predictive model using GitHub content — http://arxiv.org/abs/1803.07764v1
[7] DAIR: Disentangled Attention Intrinsic Regularization for Safe and Efficient Bimanual Manipulation — http://arxiv.org/abs/2106.05907v4
[8] SPARK-Remote: A Cost-Effective System for Remote Bimanual Robot Teleoperation — http://arxiv.org/abs/2504.05488v3
[9] SViP: Sequencing Bimanual Visuomotor Policies with Object-Centric Motion Primitives — http://arxiv.org/abs/2506.18825v1
[10] Robot Policy Evaluation for Sim-to-Real Transfer: A Benchmarking Perspective — http://arxiv.org/abs/2508.11117v1
[11] Grasp and Motion Planning for Dexterous Manipulation for the Real Robot Challenge — http://arxiv.org/abs/2101.02842v1
[12] JENGA: Exploiting Counter-Based RowHammer Countermeasures to Break Real-Time Predictability — http://arxiv.org/abs/2609.01077v1
[13] Diffusion Co-Policy for Synergistic Human-Robot Collaborative Tasks — http://arxiv.org/abs/2305.12171v4
[14] ENPIRE: Agentic Robot Policy Self-Improvement in the Real World — http://arxiv.org/abs/2606.19980v2
[15] Diffusion Policy Policy Optimization — http://arxiv.org/abs/2409.00588v3
[16] KDPE: A Kernel Density Estimation Strategy for Diffusion Policy Trajectory Selection — http://arxiv.org/abs/2508.10511v2
[17] LeRobot: An Open-Source Library for End-to-End Robot Learning — http://arxiv.org/abs/2602.22818v1
[18] Robot Learning: A Tutorial — http://arxiv.org/abs/2510.12403v1
[19] Open-Ended Learning Leads to Generally Capable Agents — http://arxiv.org/abs/2107.12808v2
[20] panda-gym: Open-source goal-conditioned environments for robotic learning — http://arxiv.org/abs/2106.13687v2
[21] On-Policy Robot Imitation Learning from a Converging Supervisor — http://arxiv.org/abs/1907.03423v7
[22] Benchmarking Reinforcement Learning Algorithms on Real-World Robots — http://arxiv.org/abs/1809.07731v1
[23] Multi-objective Model-based Policy Search for Data-efficient Learning with Sparse Rewards — http://arxiv.org/abs/1806.09351v3
[24] Dexterous Cable Manipulation: Taxonomy, Multi-Fingered Hand Design, and Long-Horizon Manipulation — http://arxiv.org/abs/2502.00396v2
[25] Overview of AuTexTification at IberLEF 2023: Detection and Attribution of Machine-Generated Text in Multiple Domains — http://arxiv.org/abs/2309.11285v1
[26] Learning Complex Dexterous Manipulation with Deep Reinforcement Learning and Demonstrations — http://arxiv.org/abs/1709.10087v2
[27] Learning Dexterous In-Hand Manipulation — http://arxiv.org/abs/1808.00177v5
[28] Vision Mamba: A Comprehensive Survey and Taxonomy — http://arxiv.org/abs/2405.04404v1
[29] DEFT: Dexterous Fine-Tuning for Real-World Hand Policies — http://arxiv.org/abs/2310.19797v2
[30] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1
[31] Aerial Mobile Manipulator System to Enable Dexterous Manipulations with Increased Precision — http://arxiv.org/abs/2010.09618v1
[32] Ground-Based Optical Deep Pencil Beam Surveys — http://arxiv.org/abs/astro-ph/0208209v1
[33] Shear-selected clusters from the Deep Lens Survey — http://arxiv.org/abs/astro-ph/0303381v1
[34] Learn to Accumulate Evidence from All Training Samples: Theory and Practice — http://arxiv.org/abs/2306.11113v2
[35] The Modern Mathematics of Deep Learning — http://arxiv.org/abs/2105.04026v2
[36] Dex-Net 2.0: Deep Learning to Plan Robust Grasps with Synthetic Point Clouds and Analytic Grasp Metrics — http://arxiv.org/abs/1703.09312v3
[37] Oriented object detection in optical remote sensing images using deep learning: a survey — http://arxiv.org/abs/2302.10473v6
[38] Deep Learning and Computational Physics (Lecture Notes) — http://arxiv.org/abs/2301.00942v1
[39] A rich bounty of AGN in the 9 square degree Bootes survey: high-z obscured AGN and large-scale structure — http://arxiv.org/abs/astro-ph/0611654v1
[40] InterACT: Inter-dependency Aware Action Chunking with Hierarchical Attention Transformers for Bimanual Manipulation — http://arxiv.org/abs/2409.07914v3
[41] Stabilize to Act: Learning to Coordinate for Bimanual Manipulation — http://arxiv.org/abs/2309.01087v2
[42] Reinforced Imitation in Heterogeneous Action Space — http://arxiv.org/abs/1904.03438v2
[43] Bi-ACT: Bilateral Control-Based Imitation Learning via Action Chunking with Transformer — http://arxiv.org/abs/2401.17698v1
[44] Strategies to Harness the Transformers' Potential: UNSL at eRisk 2023 — http://arxiv.org/abs/2310.19970v1
[45] UZH_CLyp at SemEval-2023 Task 9: Head-First Fine-Tuning and ChatGPT Data Generation for Cross-Lingual Learning in Tweet Intimacy Prediction — http://arxiv.org/abs/2303.01194v2
[46] real-stanford/diffusion_policy — https://github.com/real-stanford/diffusion_policy
[47] GelSight Svelte Hand: A Three-finger, Two-DoF, Tactile-rich, Low-cost Robot Hand for Dexterous Manipulation — http://arxiv.org/abs/2309.10886v1
[48] Dexterity from Touch: Self-Supervised Pre-Training of Tactile Representations with Robotic Play — http://arxiv.org/abs/2303.12076v1
[49] ManiSkill-ViTac 2025: Challenge on Manipulation Skill Learning With Vision and Tactile Sensing — http://arxiv.org/abs/2411.12503v1
[50] Generation of GelSight Tactile Images for Sim2Real Learning — http://arxiv.org/abs/2101.07169v1
[51] T-Rex: Tactile-Reactive Dexterous Manipulation — http://arxiv.org/abs/2606.17055v2
[52] ICML Topological Deep Learning Challenge 2024: Beyond the Graph Domain — http://arxiv.org/abs/2409.05211v1
[53] Learning In-Hand Translation Using Tactile Skin With Shear and Normal Force Sensing — http://arxiv.org/abs/2407.07885v2
[54] Learning Cross-Lingual Sentence Representations via a Multi-task Dual-Encoder Model — http://arxiv.org/abs/1810.12836v4


---

*Generated by research-bot · topic=`embodied-manipulation` · depth=`standard` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading · model=`deepseek-v4-flash` · sources=54 · duration=908s · 2026-10-04T03:36:27+00:00*
