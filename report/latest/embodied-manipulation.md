# 具身智能·灵巧操作（Dexterous Manipulation & Grasping）技术调研报告

**日期**：2026-10-02（UTC）
**领域**：具身智能 · 灵巧操作与抓取（Dexterous Manipulation & Grasping）
**检索源数量**：本次可引用的结构化证据来源 27 条（编号 [1]–[27]），另有 10 条领域人工维护种子资源（以原始链接直接给出）
**方法说明**：本报告严格基于 [1]–[27] 与种子资源清单中可核查的条目撰写。凡本次检索未取得一手来源支撑的判断，一律以 `> 待核实` 标注，**不进行任何数字、榜单或引用的推测**。提示中给出的检索结果包含若干与主题无关的条目（[13][14][15][17][18][19][20][22][26]），本报告不予使用。

---

## 摘要（Executive Summary）

近 1–2 年（2024–2026）灵巧操作与抓取领域呈现出五条值得注意的主线：

1. **手内操作（in-hand manipulation）从"单一模态"走向"视触觉融合 + 高效学习"**。FBI 提出动态视触觉 shortcut policy，主张视觉与触觉不应二选一 [10]；在真实拟人手（anthropomorphic hand）上的手内书写任务，开始用实时雅可比估计（Jacobian estimation）降低建模与数据采集成本 [12]。这些工作均以 arXiv cs.RO 预印本形式出现，尚无第三方复现报告 [10][12]，关注度与影响力 `> 待核实`。

2. **扩散策略（diffusion policy）成为灵巧手策略学习的主流生成式主干**。多指手的视觉运动扩散策略（visuomotor diffusion）被用于灵巧手内操作 [11]；该路线的最早奠基是 Diffusion Policy（种子资源），而其"动作分块（action chunking）"思想则源自 ACT/ALOHA（种子资源）。

3. **VLA（Vision-Language-Action）模型正式进入长时程双臂灵巧操作**。2025 BEHAVIOR Challenge 的冠军方案基于 Pi0.5 架构改造，在 50 个长时程家庭任务、需双臂操作 + 导航 + 上下文决策的仿真基准上夺冠 [9]。这是目前本次检索中**唯一的、明确带有竞赛排名性质的 SOTA 信号**。

4. **接触丰富任务（contact-rich）的核心矛盾是"力/接触的实时调控"**。全手抓取的实时力调节框架被提出用于对抗物体运动、建模误差与外部扰动 [21]；线缆（cable）这类可变形物体也从两指夹爪走向多指手的长时程操作分类学 [2]。

5. **低成本、可仿真的开源灵巧手硬件快速迭代**。LEAP Hand 系列（含 2025 年 V2 刚柔混合版本，citations=5）[23][25]、面向仿真就绪的腱驱动 Aero Hand Open [24]，以及刚柔/线驱动一体化臂手系统 [27] 共同在压低硬件门槛。

**主要结论**：本方向当前处于"生成式策略主干（扩散/分块）+ 多模态感知（视+触+力）+ 低成本开源硬件"三线并进的阶段；但**统一评测基准、触觉基础模型、动作分块与流匹配在灵巧手上的系统对比**三大缺口依然存在，详见第七章。

---

## 一、关键前沿进展（近 1–2 年）

### 1.1 VLA + 长时程双臂操作：2025 BEHAVIOR Challenge 冠军方案 [9]

- **point**：基于 VLA 的任务自适应方案在 2025 BEHAVIOR Challenge 获得第 1 名，该基准包含 50 个真实感仿真下的长时程家庭任务，要求双臂操作（bimanual manipulation）、导航与上下文感知决策 [9]。
- **证据**：摘要原文明确说明"won 1st place in the 2025 BEHAVIOR Challenge"，并说明其建立在 Pi0.5 架构之上 [9]。
- **热度证据**：> 待核实（本次检索未取到 citations / stars 数值）。
- **权威证据**：arXiv 预印本，arXiv 分类 cs.RO；编号形态 2512.06951（对应 2025 年 12 月提交）[9]。
- **关注度**：中（依据：挑战赛第 1 名的竞赛排名信号具有可比性，但尚无引用数或第三方复现数据支撑；`> 待核实`）[9]。
- **推荐度**：★★★★☆ — 若要研究"VLA 如何适配长时程双臂灵巧任务"，这是目前证据链最清晰、带竞赛排名的少数条目之一 [9]。

### 1.2 视触觉融合的手内操作：FBI [10]

- **point**：提出 Flow-Ba……（摘要片段截断）的动态视触觉 shortcut policy，针对手内操作中复杂的接触动力学与部分可观测性（partial observability）；核心论点是人类协同使用视觉与触觉，而机器人方法常偏重单一模态，从而限制了适应性 [10]。
- **热度证据**：> 待核实。
- **权威证据**：arXiv 预印本，cs.RO 分类（编号 2508.14441，2025 年 8 月）[10]。
- **关注度**：中（依据：话题处于"视触觉融合"热点，但无引用/榜单数据 `> 待核实`）[10]。
- **推荐度**：★★★★☆ — 是"接触丰富任务为什么需要触觉"的较新直接论据 [10]。

### 1.3 实时雅可比估计实现快速手内书写 [12]

- **point**：面向拟人手的手内笔书写（in-hand pen writing），指出接触丰富性与高动态性通常要求大量建模或数据采集，并提出用实时雅可比估计实现"快速学习" [12]。
- **热度证据**：> 待核实。
- **权威证据**：arXiv 预印本，cs.RO（编号 2609.11775，2026 年 9 月）[12]。
- **关注度**：中（依据：发布时间极新，属"刚发布"而非"已被验证"；`> 待核实`）[12]。
- **推荐度**：★★★★☆ — 代表"用解析结构（雅可比）替代海量数据"这一在灵巧操作中颇具吸引力的技术路线 [12]。

### 1.4 多指手视觉运动扩散策略 [11]

- **point**：Learning Dexterous In-Hand Manipulation with Multifingered Hands via Visuomotor Diffusion —— 将扩散策略用于多指手的手内操作 [11]。
- **热度证据**：> 待核实。
- **权威证据**：arXiv 预印本，cs.RO（编号 2503.02587，2025 年 3 月）[11]。
- **关注度**：中（依据：扩散策略 + 多指手是当前高关注组合，但无引用数据 `> 待核实`）[11]。
- **推荐度**：★★★★☆ — 是"扩散策略 × 多指手"这一交叉点的直接锚点 [11]。

### 1.5 可变形物体的多指灵巧操作：线缆分类学与长时程 [2]

- **point**：指出既有线缆操作研究依赖两指夹爪，难以完成人类式的线缆操作；与刚性物体灵巧操作不同，多指手的线缆技能发展仍不成熟，论文给出分类学（taxonomy）、多指手设计与长时程操作方案 [2]。
- **热度证据**：> 待核实。
- **权威证据**：arXiv 预印本，cs.RO（编号 2502.00396，2025 年 2 月）[2]。
- **关注度**：中（依据：可变形物体是接触丰富的极端形态，但无引用数据 `> 待核实`）[2]。
- **推荐度**：★★★★☆ — 若研究对象不限于刚体，这是当前少见的系统性梳理 [2]。

### 1.6 全手抓取的实时力调节 [21]

- **point**：论证仅靠预计算力分布会在物体运动、建模误差或外部扰动下失效，提出面向整只手的实时力调节框架 [21]。
- **热度证据**：> 待核实。
- **权威证据**：arXiv 预印本，cs.RO（编号 2609.30082，2026 年 9 月）[21]。
- **关注度**：中（依据：极新发布，尚未被验证；`> 待核实`）[21]。
- **推荐度**：★★★★☆ — 直接回应"抓取稳定性的闭环控制"这一工程刚需 [21]。

### 1.7 开源灵巧手硬件前沿：[23][24][25][27]

| 工作 | 年份 | 关键点 | 热度 | 权威 | 关注度 | 推荐度 |
|---|---|---|---|---|---|---|
| LEAP Hand [23] | 2023 | 低成本、高效、拟人手，面向机器人学习 | > 待核实 | arXiv cs.RO 预印本 [23] | 高（该系列被后续 V2 延续，说明持续影响力；具体 star `> 待核实`）[23][25] | ★★★★★ |
| Leap Hand V2 Advanced [25] | 2025 | 刚柔混合（hybrid rigid-soft）灵巧手，面向机器人学习 | citations=5 [25] | **2025 IEEE-RAS Humanoids（同行评审会议）**[25] | 中（citations=5；会议背书）[25] | ★★★★★ |
| Aero Hand Open [24] | 2026 | 仿真就绪（simulation-ready）腱驱动手；腱驱动使执行器可移出关节从而降低成本 | > 待核实 | arXiv cs.RO 预印本 [24] | 中（新发布，`> 待核实`）[24] | ★★★★☆ |
| Flexible Cable-Driven Dexterous Hand & Arm–Hand System [27] | 2025 | 柔性线驱动灵巧手与臂–手一体化系统 | citations=0 [27] | IEEE T-Mech 配套多媒体（DOI 后缀 `/mm1`）[27] | 低（citations=0）[27] | ★★★☆☆ |

> 注：[27] 的条目类型为补充多媒体文件（supplementary mp4），其 citation 计数为 0，说明该工作尚未获得社区引用验证 [27]。

---

## 二、模仿学习与扩散 / 动作分块策略

### 2.1 扩散策略作为生成式主干

- **核心论断**：扩散策略（Diffusion Policy）通过动作扩散建模多模态动作分布，已成为视觉运动策略学习的重要奠基路线（种子资源：*Diffusion Policy: Visuomotor Policy Learning via Action Diffusion*，RSS 2023，https://arxiv.org/abs/2303.04137 ）；其官方实现在 `real-stanford/diffusion_policy`（https://github.com/real-stanford/diffusion_policy ）。
  - **热度证据**：> 待核实（本次检索未取到该仓库的 star 数）。
  - **权威证据**：RSS（Robotics: Science and Systems）为同行评审顶会；官方仓库由原作者团队维护（种子资源）。
  - **关注度**：高（依据：被公认为该方向奠基工作，并被灵巧手工作直接沿用，如 [11] 的 visuomotor diffusion 路线）。
  - **推荐度**：★★★★★ — 若要理解"为什么 2024–2026 的灵巧策略大量用扩散模型"，这是必读起点。

- **近期延伸**：多指手的视觉运动扩散策略 [11] 将上述主干落到多指灵巧手上。
  - 热度：> 待核实；权威：arXiv cs.RO 预印本 [11]；关注度：中（`> 待核实`）；推荐度：★★★★☆ [11]。

### 2.2 动作分块（action chunking）与低成本双臂模仿学习

- **核心论断**：ACT/ALOHA 提出用低成本硬件完成细粒度双臂操作，其"动作分块"思路成为后续模仿学习栈的基础组件（种子资源：*Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware (ACT/ALOHA)*，RSS 2023，https://arxiv.org/abs/2304.13705 ；代码：https://github.com/tonyzhaozh/aloha ）。
  - **热度证据**：> 待核实。
  - **权威证据**：RSS 2023 同行评审；官方代码仓库（种子资源）。
  - **关注度**：高（依据：ALOHA 硬件栈被后续 ALOHA 2 直接继承 [16]，形成可追踪的版本谱系）。
  - **推荐度**：★★★★★ — 低成本双臂精细操作的事实标准起点。

- **硬件迭代**：ALOHA 2 作为增强型低成本双臂遥操作硬件被正式提出（arXiv 2405.02292，2024）[16]。
  - 热度：> 待核实；权威：arXiv 预印本 [16]；关注度：中高（依据：作为 ACT/ALOHA 生态的官方延续版本，`> 待核实`）；推荐度：★★★★★ [16]。

### 2.3 真机微调范式

- **核心论断**：DEFT（Dexterous Fine-Tuning for Real-World Hand Policies）提出面向真实世界手部策略的灵巧微调 [3]。
  - 热度：> 待核实；权威：arXiv 预印本（2310.19797，2023）[3]；关注度：中（`> 待核实`）；推荐度：★★★★☆ — 是"仿真预训练 → 真机微调"这条 sim2real 路线的显式代表 [3]。

### 2.4 覆盖缺口（Coverage Gaps）

以下概念在本次检索中**未获得一手可引用来源**，不做结论性陈述：

> **待核实**：flow matching（流匹配）策略在灵巧操作上的系统性对比；动作分块（action chunking）与扩散策略在同一灵巧手基准上的正面对比；RT-1 / RT-2 / MT-Opt / Dexterity from Scratch / R3M 等常被提及的里程碑工作，本次检索未捕获可引用来源，故不在本报告中给出具体结论。

---

## 三、灵巧手与手内操作

### 3.1 手内操作的奠基与经典

- **Learning Dexterous In-Hand Manipulation（OpenAI, 2018）** [1]：在物理 Shadow Dexterous Hand 上学习到可执行**基于视觉的物体重定向（vision-based object reorientation）**的 RL 策略；训练在仿真中完成，并对系统的大量物理属性做随机化（domain randomization）[1]。
  - **热度证据**：> 待核实（未取到确切引用数）。
  - **权威证据**：arXiv 预印本，cs.LG 分类（1808.00177v5）[1]；正式发表 venue `> 待核实`。
  - **关注度**：高（依据：作为"仿真训练 + 域随机化 → 真机灵巧手"这一范式的开创性工作，被后续文献持续引用；确切引用数 `> 待核实`）[1]。
  - **推荐度**：★★★★★ — 理解 sim2real 灵巧手操作必读 [1]。

- **Learning Complex Dexterous Manipulation with Deep RL and Demonstrations（2017）** [4]：将深度强化学习与演示（demonstrations）结合，用于复杂灵巧操作 [4]。
  - 热度：> 待核实；权威：arXiv 预印本，cs.LG（1709.10087）[4]；关注度：高（依据：确立了"演示 + RL"的混合监督范式，被后续工作广泛沿用；确切数据 `> 待核实`）；推荐度：★★★★★ [4]。

### 3.2 手内操作的最新方法

- **实时雅可比估计的快速手内书写** [12]：见 §1.3。将"快速学习"归因于实时雅可比估计而非大规模数据 [12]。
- **基于 3D 手–物交互的学习（博士学位论文）** [6]：研究单目视频中 3D 手部运动与手–物交互，并展示如何将这些知识用于学习 [6]。
  - 热度：citations=0 [6]；权威：DOI 学位论文，无 venue 信息；关注度：低（citations=0）[6]；推荐度：★★★☆☆ [6]。
- **手内操作规划以复现熟练灵巧任务（博士论文，法语）** [5]：以规划（planning）路线复现人类熟练灵巧操作 [5]。
  - 热度：citations=0 [5]；权威：DOI 学位论文；关注度：低（citations=0）[5]；推荐度：★★★☆☆ — 提供"规划 vs 学习"的另一条技术路线的视角，但尚未被引用验证 [5]。
- **未知物体的手内灵巧操作** [7]：book chapter（DOI 10.1016/b978-0-32-390445-2.00023-4），聚焦对未知物体的手内操作 [7]。
  - 热度：> 待核实；权威：Elsevier 书籍章节（同行评审程度 `> 待核实`）；关注度：中（`> 待核实`）；推荐度：★★★★☆ [7]。

### 3.3 硬件与手部设计

见 §1.7 表格（[23][24][25][27]）。补充一条：

- **刚柔混合与腱驱动的成本逻辑**：Aero Hand Open 明确指出腱驱动的价值在于"把执行器移出关节"，从而使手在同等能力下更廉价、可使用更小的电机 [24]。这是一条清晰的**成本归因论证**，而非单纯性能宣称 [24]。

---

## 四、接触丰富任务与触觉 / 力感知

### 4.1 视触觉融合

- **FBI（Dynamic Visuotactile Shortcut Policy）** [10]：核心论点是手内操作面临复杂接触动力学与部分可观测性；人类协同使用视觉与触觉，而机器人方法常偏重单一模态，从而限制适应性 [10]。
  - 热度：> 待核实；权威：arXiv cs.RO 预印本 [10]；关注度：中（`> 待核实`）；推荐度：★★★★☆ — 为"触觉是否必要"提供较新的直接论述 [10]。

### 4.2 力/接触的实时闭环

- **全手抓

## 参考来源

[1] Learning Dexterous In-Hand Manipulation — http://arxiv.org/abs/1808.00177v5
[2] Dexterous Cable Manipulation: Taxonomy, Multi-Fingered Hand Design, and Long-Horizon Manipulation — http://arxiv.org/abs/2502.00396v2
[3] DEFT: Dexterous Fine-Tuning for Real-World Hand Policies — http://arxiv.org/abs/2310.19797v2
[4] Learning Complex Dexterous Manipulation with Deep Reinforcement Learning and Demonstrations — http://arxiv.org/abs/1709.10087v2
[5] Planning robotic in-hand manipulation to reproduce skilled dexterous manipulation tasks — https://doi.org/10.70675/bf4f1352z2fddz454cz8f3ezebb41418497e
[6] Learning dexterous manipulation from 3D hand and object interaction — https://doi.org/10.70675/a5b55fc1z8706z4710z9ed5zf2b7365c5cf3
[7] Towards dexterous in-hand manipulation of unknown objects — https://doi.org/10.1016/b978-0-32-390445-2.00023-4
[8]  — https://doi.org/10.55776/i3969
[9] Task adaptation of Vision-Language-Action model: 1st Place Solution for the 2025 BEHAVIOR Challenge — http://arxiv.org/abs/2512.06951v2
[10] FBI: Learning Dexterous In-hand Manipulation with Dynamic Visuotactile Shortcut Policy — http://arxiv.org/abs/2508.14441v1
[11] Learning Dexterous In-Hand Manipulation with Multifingered Hands via Visuomotor Diffusion — http://arxiv.org/abs/2503.02587v1
[12] Rapid Learning of Dexterous In-Hand Pen Writing through Real-Time Jacobian Estimation — http://arxiv.org/abs/2609.11775v1
[13] Machine Learning for Health (ML4H) Workshop at NeurIPS 2018 — http://arxiv.org/abs/1811.07216v2
[14] The 2018 PIRM Challenge on Perceptual Image Super-resolution — http://arxiv.org/abs/1809.07517v3
[15] The Barbados 2018 List of Open Issues in Continual Learning — http://arxiv.org/abs/1811.07004v1
[16] ALOHA 2: An Enhanced Low-Cost Hardware for Bimanual Teleoperation — http://arxiv.org/abs/2405.02292v1
[17] Strategies to Harness the Transformers' Potential: UNSL at eRisk 2023 — http://arxiv.org/abs/2310.19970v1
[18] Overview of AuTexTification at IberLEF 2023: Detection and Attribution of Machine-Generated Text in Multiple Domains — http://arxiv.org/abs/2309.11285v1
[19] OpenPodcar: an Open Source Vehicle for Self-Driving Car Research — http://arxiv.org/abs/2205.04454v2
[20] SnapperGPS: Open Hardware for Energy-Efficient, Low-Cost Wildlife Location Tracking with Snapshot GNSS — http://arxiv.org/abs/2207.06310v3
[21] Real-Time Force Regulation for Whole-Hand Dexterous Grasping — http://arxiv.org/abs/2609.30082v1
[22] Open Source, Open Hardware Hand-Held Mobile Mapping System for Large Scale Surveys — https://doi.org/10.2139/ssrn.4618683
[23] LEAP Hand: Low-Cost, Efficient, and Anthropomorphic Hand for Robot Learning — http://arxiv.org/abs/2309.06440v1
[24] Aero Hand Open: A Simulation-Ready Tendon-Driven Hand for Dexterous Manipulation Learning — http://arxiv.org/abs/2608.28578v2
[25] Leap Hand V2 Advanced: Dexterous, Low-Cost Hybrid Rigid-Soft Hand for Robot Learning — https://doi.org/10.1109/humanoids65713.2025.11203038
[26] Open source, open hardware hand-held mobile mapping system for large scale surveys — https://doi.org/10.1016/j.softx.2023.101618
[27] Development of a Flexible Cable-Driven Dexterous Hand and Arm–Hand Integrated System_supp1-3574817.mp4 — https://doi.org/10.1109/tmech.2025.3574817/mm1


---

*Generated by research-bot · topic=`embodied-manipulation` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading · model=`deepseek-v4-flash` · sources=27 · duration=184s · 2026-10-02T10:57:10+00:00*
