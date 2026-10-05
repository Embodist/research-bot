# 人形与腿足学习式运动控制（Humanoid & Legged Locomotion）技术调研报告

**日期**：2026-10-05（UTC） | **领域**：具身智能 · 人形与腿足运动（Humanoid & Legged Locomotion） | **检索源**：本次可用编号来源 99 条（其中与腿足/人形运动直接相关约 55 条，领域无关噪声约 30 条），另含领域种子资源 9 条（3 篇论文 + 4 个开源项目 + 2 个数据集，均为人工维护清单，无本次检索编号）

**证据说明**：本报告全部论断仅引用给定编号来源 [1]–[99]。候选块中 `heat` 字段普遍为空，**所有引用数、GitHub star、下载量、榜单排名一律标注 `> 待核实`，不作任何数字推断**。arXiv 编号（如 2512.01996 = 2025 年 12 月）可用于判断发表时间，但不等同于同行评审 venue。检索命中中混入大量跨领域条目（高能物理 [8][9][10][30]、量子控制 [27]、语音/图像/法律/天文等评测挑战 [58][59][67][69][93][95][96][97][98][99]、撤回稿 [35]），本报告已在相应位置标注为噪声。

---

## 摘要（Executive Summary）

1. **训练效率的量级压缩成为 2025 年最显眼的叙事**：大规模并行仿真把 RL 训练从"天"压到"分钟"级，[2] 直接以《Learning Sim-to-Real Humanoid Locomotion in 15 Minutes》为题，但摘要同时承认高维动作空间与域随机化仍是 sim2real 的主要难点 [2]。该数字为**论文自称**，未见第三方复现，且本体、任务数与真机指标 `> 待核实`。

2. **学习式策略与传统模型控制正在合流而非替代**：2025 年出现分层降阶模型 MPC [3]、基于降阶模型的推扰恢复与行走统一框架 [15]、以及 capture point 与推进器混合的双足控制 [25]，说明"降阶模型 + 学习/优化"仍是真机鲁棒性的主要来源。

3. **本体感知盲行与视觉感知式运动的分界尚未被受控实验回答**：teacher-student 特权信息蒸馏是本体感知路线的主流范式 [73][74][75]，视觉路线以深度图解决"盲区" [82][84]，导航侧则试图融合地形、障碍与本体感知 [76][80]；但候选证据中**不存在同一本体、同一地形上的跨模态对照基准**，需补充后再下结论。

4. **全身控制的外延在扩大**：从 locomotion 走向 loco-manipulation [11][18]、全身接触式运动（《Locomotion Beyond Feet》覆盖椅子下低净空、齐膝平台与陡楼梯）[81]，以及全身动态交互（羽毛球）[5]。

5. **遥操作 + 动作重定向成为数据获取主路径**：H2O / OmniH2O / TWIST / CLOT / CHILD 构成 2024–2026 年的连续谱系 [21][20][22][23][17]，配套的重定向与运动跟踪工作密集出现 [19][61][62][63][64][65][66]。

6. **主要证据缺口**：(a) 缺乏真机 vs 仿真的统一评测口径 [55][60]；(b) 多数论文仅在摘要层面宣称泛化性，缺任务数/成功率/能耗等可比数字；(c) 检索噪声比例高，说明本子问题的证据密度低于表面命中数。

---

## 一、关键前沿进展（近 1–2 年）

### 1.1 [2] Learning Sim-to-Real Humanoid Locomotion in 15 Minutes（2025-12）
- **贡献**：以大规模并行仿真压缩人形 sim2real RL 训练时间至分钟级，摘要自述仍需应对高维与域随机化带来的困难 [2]。
- **热度**：`> 待核实`（候选块未提供 citations/stars）[2]
- **权威**：arXiv 预印本 cs.RO（2512.01996v1），未见同行评审标注 [2]
- **关注度**：`> 待核实`——无引用/star/榜单信号 [2]
- **推荐度**：★★★☆☆ —— 主题高度相关且标题主张强，但需核实本体、任务数与真机成功率 [2]

### 1.2 [3] Hierarchical Reduced-Order Model Predictive Control for Robust Locomotion on Humanoid Robots（2025-09）
- **贡献**：提出计算高效的分层控制框架，基于降阶模型实现多样化步态规划与增量控制，面向真实环境鲁棒行走 [3]。
- **热度**：`> 待核实` [3] ｜ **权威**：arXiv 预印本 cs.RO（2509.04722v1）[3]
- **关注度**：`> 待核实` [3]
- **推荐度**：★★★★☆ —— 模型控制路线的当代代表作，与学习式路线形成对照，值得精读 [3]

### 1.3 [4] Learning Humanoid Locomotion over Challenging Terrain（2024-10）
- **贡献**：面向挑战地形的学习式人形行走（候选块仅提供标题与编号，方法细节 `> 待核实`）[4]。
- **热度/关注度**：`> 待核实` [4]
- **权威**：arXiv 预印本（2410.03654v1）[4]
- **推荐度**：★★★☆☆ —— 属 2024 年该方向时间线锚点，但本次未取到摘要级细节 [4]

### 1.4 [81] Locomotion Beyond Feet（2026-01）
- **贡献**：将人形运动从足部步态扩展到多接触全身运动（低净空、齐膝墙/平台、陡上下楼梯），把"物理可仿真的关键帧动画"与 RL 结合，把参考动作转为鲁棒行为 [81]。
- **热度/关注度**：`> 待核实` [81]
- **权威**：arXiv 预印本 cs.RO（2601.03607v1）；候选块记录作者含 Shuran Song、C. Karen Liu（团队权威性较高，但仍在预印本阶段）[81]
- **推荐度**：★★★★☆ —— 代表"足部以外全身接触"的新前沿，建议持续跟踪 [81]

### 1.5 [82] No More Blind Spots: Learning Vision-Based Omnidirectional Bipedal Locomotion（2025-08）
- **贡献**：用深度图实现全向双足地形感知，目标场景为杂乱室内与不平地形，直接回应盲行盲区问题 [82]。
- **热度/关注度**：`> 待核实` [82] ｜ **权威**：arXiv 预印本 cs.RO（2508.11929v2）[82]
- **推荐度**：★★★☆☆ —— 与本体感知盲行形成直接对照，但缺量化对比 [82]

### 1.6 [5] Humanoid Whole-Body Badminton via an Annealed Reinforcement Learning Curriculum（2025-11）
- **贡献**：以退火式 RL 课程训练统一全身策略，面向快速移动物体的动态交互 [5]。
- **热度/关注度**：`> 待核实` [5] ｜ **权威**：arXiv 预印本（2511.11218v4）[5]
- **推荐度**：★★★★☆ —— 把全身控制推向动态交互，是"locomotion → 动态任务"演进的清晰样本 [5]

### 1.7 [53] Robot Trains Robot: Automatic Real-World Policy Adaptation and Learning for Humanoids（2025-08）
- **贡献**：指出仿真 RL 已显著推进人形行走，但"从零真机 RL 或从预训练策略做真机适配"仍罕见，据此提出真机自动适配方案 [53]。
- **热度/关注度**：`> 待核实` [53] ｜ **权威**：arXiv 预印本（2508.12252v2）[53]
- **推荐度**：★★★★☆ —— 直击"真机学习稀缺"这一开放问题 [53]

### 1.8 [7] Humanoid Manipulation Interface（2026-02）与 [41] The Open Ant（2026-07）
- [7] 提出"无机器人演示"的人形全身操作方法，批评现有遥操作/视觉 sim2real 受硬件物流与奖励工程所限 [7]。
- [41] 是一个面向 RL 研究的机器人平台，明确指出 RL 研究仍以仿真为主、向物理现实迁移存在不确定性 [41]。
- **热度/关注度**：均 `> 待核实` [7][41] ｜ **权威**：均为 arXiv 预印本 cs.RO [7][41]
- **推荐度**：★★★☆☆ —— 两篇共同指向"演示数据获取"与"真机落地"的瓶颈 [7][41]

---

## 二、学习式 locomotion 与全身控制

- **统一全身控制器**：[16] HOVER 提出面向人形的多功能神经全身控制器（标题级证据）[16]；热度 `> 待核实` [16]。
- **域随机化与扩散策略**：[6] 系统考察域随机化在全身人形控制的扩散策略训练中的作用，是 sim2real 正则化方向的方法学证据 [6]；关注度 `> 待核实` [6]。
- **全身 loco-manipulation**：[18] 以"主动空间大脑 + 可泛化动作小脑"分层架构处理复杂 3D 空间关系下的全身操作 [18]；[11] 以具身 chain-of-action 推理结合多模态基础模型做零样本 loco-manipulation [11]。二者共同标志"行走"正被并入"全身任务"框架 [11][18]；热度均 `> 待核实` [11][18]。
- **分层与降阶模型控制**：[3] 的分层降阶 MPC 与 [15] 的"行走 + 推扰恢复统一框架"是模型控制一侧的代表 [3][15]；[15] 特别强调动态行走中用双臂辅助推扰恢复 [15]。
- **方法论缺口**：候选证据中缺少把"神经全身控制器"与"分层降阶 MPC"放在同一本体、同一任务集上的受控对比 [3][15][16]，因此"学习式是否已全面超越模型控制"`> 待核实`。

---

## 三、sim2real 与地形适应

**（1）本体感知 / 特权信息蒸馏路线**
- [73] CTS 提出并发 teacher-student 强化学习用于腿足运动 [73]；[74] VMTS 将视觉辅助引入 teacher-student，面向双足多地形 [74]；[75] Teacher Motion Priors 先以特权信息训练教师、再把运动分布迁移到仅用带噪本体感知的学生策略，用于挑战地形 [75]。
- 该范式的共同逻辑是"用仿真特权信息跨过信息差"，但**部署成本、传感器依赖与失败模式的横向对比在候选证据中缺失** [73][74][75]，`> 待核实`。

**（2）纯本体感知**
- [57] Hybrid Internal Model 以"模拟机器人响应"学习敏捷腿足运动 [57]；[33] ATRos 在轮足平台上用本体感知估计外部环境状态以协调行走—驱动混合运动，声称改善地形适应性与能效 [33]。
- 热度：均 `> 待核实` [33][57]。**盲行在何种地形上必然失效仍无受控结论** [33][57][82]。

**（3）视觉 / 多模态感知**
- [82] 用深度图做全向双足地形感知 [82]；[84] 早前提出基于视觉的双足挑战地形运动 [84]；[76] TOP-Nav 融合地形、障碍与本体感知做腿足导航 [76]；[80] 在不确定粗糙地形上统一地形建图与运动稳定性 [80]。
- 热度：均 `> 待核实` [76][80][82][84]。
- **边界判断（低置信）**：三类方法的输入模态分裂明确，但候选集合内**没有统一的跨模态基准**，故"本体感知 vs 视觉 vs 多模态"的性能边界只能间接推断 [33][75][81][82]。

**（4）综述、评估与真机持续学习**
- [43] 提供 sim2real 迁移的早期综述框架 [43]；[32] 专门综述双足 locomotion 的 DRL sim2real 迁移，并剖析"仿真诅咒"的来源 [32]；[55] 从基准化视角讨论机器人策略的 sim2real 评估 [55]；[50] 以精准农业为例指出 sim2real 的重要性与**局限** [50]。
- 真机侧：[34] 提出在真实世界微调 locomotion 策略以持续学习 [34]；[53] 提出真机自动策略适配 [53]。热度均 `> 待核实` [32][34][43][50][53][55]。
- **本节结论**：sim2real 的"真实差距有多大"在候选证据中只能得到**方法多样性**证据，得不到**统一量化结论** `> 待核实` [32][43][50][55]。

---

## 四、敏捷动作、跑跳与恢复

- **跑酷（parkour）三连**：[85] Robot Parkour Learning（2023-09）是该方向早期代表作 [85]；[86] PIE 提出隐式-显式结合的学习框架 [86]；[87] Humanoid Parkour Learning 把人形带入跑酷任务 [87]。三者构成"四足 → 框架化 → 人形"的演进链 [85][86][87]。热度均 `> 待核实`。
- **跳跃**：[92] 以端到端 RL 做力矩级变高度跳跃 [92]；热度 `> 待核实` [92]。
- **起立/恢复**：[90] 学习真机人形的起身策略 [90]；[91] 学习跨多样姿态的站起控制 [91]；[15] 用降阶模型统一行走与推扰恢复 [15]；[25] 把 capture point 与推进器结合以扩展双足姿态操纵模态 [25]。热度均 `> 待核实` [15][25][90][91]。
- **故障与异常**：[83] DreamFLEX 面向四足在粗糙地形下异常情境的故障感知控制器 [83]；热度 `> 待核实` [83]。
- **缺口**：上述工作分布在不同本体（四足 / 人形 / 带推进器双足）与不同任务上，**跨本体可比性不足** [25][83][85][87][90][91][92]，`> 待核实`。

---

## 五、遥操作与动作先验

**（1）全身遥操作谱系（2024–2026）**
- [21] H2O 实现人→人形实时全身遥操作（种子清单标注 IROS 2024，[21] 为 arXiv 版）[21]；
- [20] OmniH2O 扩展为通用灵巧全身遥操作与学习 [20]；
- [22] TWIST 提出遥操作全身模仿系统 [22]；
- [23] CLOT 做闭环全局运动跟踪 [23]；
- [17] CHILD 指出既有工作很少支持人形的**关节级全身遥操作**，并给出相应系统 [17]；
- [52] 面向小型人形，用 VR 做上半身遥操作 + RL 做下半身平衡的 tele-loco-manipulation [52]。
- 热度：全部 `> 待核实` [17][20][21][22][23][52]。

**（2）重定向与运动跟踪（动作先验的工程接口）**
- [19] 较早提出人形全身几何重定向 [19]；[62] 面向四足的时空运动重定向 [62]；[61] 提出腿足机器人的**稠密时间**运动重定向，强调跳跃等动态动作需按机器人动力学特性调整 [61]；[63] 直接以《Retargeting Matters》为题论证重定向对人形运动跟踪的决定性作用 [63]；[64] 用人体—人形重定向模拟婴儿第一人称感觉运动经验 [64]；[65] UniTracker 学习通用全身运动跟踪器 [65]；[66] 提出无监督神经重定向用于人形遥操作 [66]。
- 热度：全部 `> 待核实` [19][61][62][63][64][65][66]。
- **观察**：该方向的密集产出说明"人体动捕 → 人形可执行动作"这一具身差距（embodiment gap）是当前工程瓶颈 [61][63][66]。

**（3）动捕数据资源**：AMASS 与 LAFAN1 为领域种子数据集（链接见第七章表格），本次未取得实时下载量或引用数据，热度 `> 待核实`。

---

## 六、经典与奠基性工作

> 说明：以下"经典"依据**发表时间 + 是否为后续工作反复引用的方法论锚点**判断。热度列因候选块未提供引用/star 数据，一律 `> 待核实`；推荐度为本报告的编辑判断（依据权威性 + 与主题相关性），不依赖数字。

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| Dynamic Walking: Toward Agile and Efficient Bipedal Robots [26] | 2010 | 未在候选证据中标明 `> 待核实` | `> 待核实` | arXiv 综述（2010.07451v1）[26] | `> 待核实` | ★★★★☆ —— 动态行走的经典综述骨架，理解"为何学 RL"的起点 [26] | http://arxiv.org/abs/2010.07451v1 | 被动动态行走与敏捷高效双足的方法论综述 [26] |
| Capture Point Control in Thruster-Assisted Bipedal Locomotion [25] | 2024 | 未标明 `> 待核实` | `> 待核实` | arXiv 预印本（2406.14799v1）[25] | `> 待核实` | ★★★★☆ —— capture point 经典概念在现代本体上的延伸 [25] | http://arxiv.org/abs/2406.14799v1 | 用推进器扩展双足姿态操纵模态 [25] |
| Feedback Regularization and Geometric PID Control（平面三连杆混合双足）[28] | 2017 | 未标明 `> 待核实` | `> 待核实` | arXiv 预印本（1710.02066v1）[28] | `> 待核实` | ★★★☆☆ —— 混合动力学 + 几何控制的奠基式方法论 [28] | http://arxiv.org/abs/1710.02066v1 | 混合双足模型的鲁棒镇定 [28] |
| Robust Dynamic Walking for a 3D Dual-SLIP Model [29] | 2022 | 未标明 `> 待核实` | `> 待核实` | arXiv 预印本（2203.07471v2）[29] | `> 待核实` | ★★★☆☆ —— 降阶模型（SLIP）路线的代表性理论工作 [29] | http://arxiv.org/abs/2203.07471v2 | 面向柔性地形的单侧刚度扰动鲁棒行走 [29] |
| Online Balanced Motion Generation for Humanoid Robots [71] | 2018 | 未标明 `> 待核实` | `> 待核实` | arXiv 预印本（1810.08388v1）[71] | `> 待核实` | ★★★☆☆ —— 人形在线平衡运动生成的早期工程范式 [71] | http://arxiv.org/abs/1810.08388v1 | 在线平衡运动生成 [71] |
| NimbRo-OP 开源人形平台与 ROS 框架 [1] | 2018 | 未标明 `> 待核实` | `> 待核实` | arXiv 预印本（1809.11051v1）[1] | `> 待核实` | ★★★☆☆ —— 开源人形硬件/软件栈的历史基线 [1] | http://arxiv.org/abs/1809.11051v1 | ROS 软件框架 [1] |
| NimbRo-OP2 [12] / NimbRo-OP2X [70] | 2018 | 未标明 `> 待核实` | `> 待核实` | arXiv 预印本 [12][70] | `> 待核实` | ★★★☆☆ —— 3D 打印开源人形平台演进 [12][70] | http://arxiv.org/abs/1809.11144v1 ; http://arxiv.org/abs/1810.08395v1 | 开源人形平台 [12][70] |
| Oncilla robot（开源四足，柔性缩放腿）[39] | 2018 | 未标明 `> 待核实` | `> 待核实` | arXiv 预印本（1803.06259v2）[39] | `> 待核实` | ★★☆☆☆ —— 开源硬件线索，与方法学主线关联较弱 [39] | http://arxiv.org/abs/1803.06259v2 | 开源四足研究平台 [39] |
| A Legged Soft Robot Platform for Dynamic Locomotion [40] | 2020 | 未标明 `> 待核实` | `> 待核实` | arXiv 预印本（2011.06749v2）[40] | `> 待核实` | ★★☆☆☆ —— 软体腿足分支，非主流主线 [40] | http://arxiv.org/abs/2011.06749v2 | 软体腿足平台 [40] |
| Real-World Humanoid Locomotion with RL [14] | 2023 | 未标明 `> 待核实` | `> 待核实` | arXiv 预印本（2303.03381v2）；后续发表情况 `> 待核实` [14] | `> 待核实` | ★★★★★ —— 真机人形 RL 行走的转折点之一，必读 [14] | http://arxiv.org/abs/2303.03381v2 | 真机人形 RL 行走 [14] |
| Learning Robust, Agile, Natural Legged Locomotion Skills in the Wild [36] | 2023 | 未标明 `> 待核实` | `> 待核实` | arXiv 预印本（2304.10888v3）[36] | `> 待核实` | ★★★★☆ —— 野外复杂地形敏捷运动的代表工作 [36] | http://arxiv.org/abs/2304.10888v3 | 野外敏捷腿足运动 [36] |
| Hybrid Internal Model (HIM) [57] | 2023 | 未标明 `> 待核实` | `> 待核实` | arXiv 预印本（2312.11460v3）[57] | `> 待核实` | ★★★★☆ —— 本体感知隐式环境建模的关键前作 [57] | http://arxiv.org/abs/2312.11460v3 | 用模拟机器人响应学习敏捷运动 [57] |
| Legged Robots that Keep on Learning [34] | 2021 | 未标明 `> 待核实` | `> 待核实` | arXiv 预印本（2110.05457v1）[34] | `> 待核实` | ★★★★☆ —— 真机微调/持续学习范式的早期奠基 [34] | http://arxiv.org/abs/2110.05457v1 | 真机微调 locomotion 策略 [34] |
| Sim-to-Real Transfer in DRL for Robotics: a Survey [43] | 2020 | 未标明 `> 待核实` | `> 待核实` | arXiv 综述（2009.13303v2）[43] | `> 待核实` | ★★★★☆ —— sim2real 综述的标准入口（注意已 >2 年时效）[43] | http://arxiv.org/abs/2009.13303v2 | sim2real 方法学综述 [43] |
| Learning Agile and Dynamic Motor Skills for Legged Robots（ANYmal）| 2019 | ETH（种子清单） | `> 待核实` | Science Robotics（种子清单，本次未取得编号） | `> 待核实` | ★★★★★ —— 学习式腿足 sim2real 的奠基之作 [种子] | https://www.science.org/doi/10.1126/scirobotics.aau5872 | sim2real 强化学习 [种子] |
| Learning Quadrupedal Locomotion over Challenging Terrain | 2020 | ETH（种子清单） | `> 待核实` | Science Robotics（种子清单，本次未取得编号） | `> 待核实` | ★★★★★ —— 挑战地形学习式运动的奠基之作 [种子] | https://www.science.org/doi/10.1126/scirobotics.abc5986 | 学习式腿足运动奠基 [种子] |
| Learning Human-to-Humanoid Real-Time Whole-Body Teleoperation (H2O) | 2024 | IROS（种子清单） | `> 待核实` | 种子清单标注 IROS 2024；arXiv 版见 [21] | `> 待核实` | ★★★★★ —— 全身实时遥操作的转折点 [21][种子] | https://arxiv.org/abs/2403.04436 | 人形全身实时遥操作 [21] |

> **关于 DeepMimic / Raibert 弹跳 / ZMP 原始文献**：本次给定来源列表中**未出现** DeepMimic、Raibert 弹跳控制或 ZMP 原始论文的可核查条目，因此不列入表格，相关承上启下叙述 `> 待核实`。检索命中 [26][28][29] 属降阶模型与动态行走的理论谱系，可作为间接起点。

---

## 七、开源项目、数据集、基准与开放问题

### 7.1 开源项目与工程栈

> 以下 4 项来自领域种子资源清单，**无本次检索编号**，故其热度（star/commit）无法在本报告内核实，一律 `> 待核实`。

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| legged_gym | `> 待核实` | leggedrobotics（种子清单） | `> 待核实` | 官方 GitHub 仓库（种子清单） | `> 待核实` | ★★★★★ —— 腿足 RL 训练框架的事实基线，复现门槛最低的入口 | https://github.com/leggedrobotics/legged_gym | 腿足 RL 训练框架 |
| IsaacLab | `> 待核实` | isaac-sim（种子清单） | `> 待核实` | 官方 GitHub 仓库（种子清单） | `> 待核实` | ★★★★★ —— GPU 并行仿真的基础设施层，[2] 类"分钟级训练"依赖此类栈 | https://github.com/isaac-sim/IsaacLab | GPU 仿真训练 |
| unitree_rl_gym | `> 待核实` | unitreerobotics（种子清单） | `> 待核实` | 官方 GitHub 仓库（种子清单） | `> 待核实` | ★★★★☆ —— 面向 Unitree 硬件的 RL 训练环境 | https://github.com/unitreerobotics/unitree_rl_gym | Unitree RL 训练环境 |
| ProtoMotions | `> 待核实` | NVlabs（种子清单） | `> 待核实` | 官方 GitHub 仓库（种子清单） | `> 待核实` | ★★★★☆ —— 人形物理仿真运动，与第五章重定向/跟踪方向互补 | https://github.com/NVlabs/ProtoMotions | 人形物理仿真运动 |

**观察**：本子问题的命中几乎全是论文而非仓库 [2][3][5][7][15][17]，说明"哪些工作真正开源了代码/权重"在本次检索中**证据不足**，无法给出可复现性排名 `> 待核实`。

### 7.2 数据集与基准

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| HumanoidBench [60] | 2024 | 未标明 `> 待核实` | `> 待核实` | arXiv 预印本（2403.10506v2）[60] | `> 待核实` | ★★★★☆ —— 人形全身 locomotion + manipulation 仿真基准，可比性讨论的核心载体 [60] | http://arxiv.org/abs/2403.10506v2 | 全身人形仿真基准 [60] |
| Open X-Embodiment [68] | 2023 | 未标明 `> 待核实` | `> 待核实` | arXiv 预印本（2310.08864v9）[68] | `> 待核实` | ★★★★☆ —— 跨本体机器人学习数据集与 RT-X 模型，跨本体可比性的参考 [68] | http://arxiv.org/abs/2310.08864v9 | 机器人学习数据集与模型 [68] |
| AMASS（动捕） | `> 待核实` | 种子清单 | `> 待核实` | 官方数据集主页（种子清单） | `> 待核实` | ★★★★★ —— 运动先验的事实来源，[61][63][66] 类重定向工作的上游 | https://amass.is.tue.mpg.de/ | 人体动作捕捉数据 |
| Lafan1 / LAFAN1 retargeted | `> 待核实` | Ubisoft La Forge（种子清单） | `> 待核实` | 官方 GitHub 仓库（种子清单） | `> 待核实` | ★★★★☆ —— 人形动作先验的常用来源，已有重定向版本 | https://github.com/ubisoft/ubisoft-laforge-animation-dataset | 人形动作先验 |
| Bamboo [72] | 2022 | 未标明 `> 待核实` | `> 待核实` | arXiv 预印本（2203.07845v2）[72] | `> 待核实` | ★☆☆☆☆ —— **注意口径错配**：检索到的 [72] 是"人机协同构建超大规模视觉数据集"，非人形运动基准；研究目标中提到的 Bamboo 基准与 [72] 是否为同一对象 `> 待核实` | http://arxiv.org/abs/2203.07845v2 | 视觉数据集（非人形运动基准） |
| MuJoCo Playground / RoboArena | — | — | — | — | — | — | — | 本次给定来源列表中**未出现**对应条目，`> 待核实`，不作描述 |

> **DeepMimic**：本次来源列表中无对应条目，`> 待核实`，不作为基准引用。

### 7.3 开放问题与争议

1. **sim2real 真实差距无法量化**：候选证据支持"方法多样"（域随机化 [6]、特权蒸馏 [73][74][75]、视觉编码器预训练 [49]、真机适配 [34][53]），但没有统一的 gap 度量；[55] 从基准化视角指出评估本身的困难 [55]，[50] 明确讨论 sim2real 的局限 [50]。**结论：gap 的绝对值 `> 待核实`。**
2. **真机 SOTA 与仿真 SOTA 错位**：多处方法仅在摘要层面声明地形适应与泛化 [33][75][82]，缺任务数、成功率、能耗等可比数字 [33][75][82]；[41] 亦指 RL 研究仍以仿真为主、向物理现实迁移存在不确定性 [41]。
3. **复现困难与失败案例**：本次检索**未取到任何负面结果或复现报告**，这是一个显著证据缺口 `> 待核实`（注意：缺少负面证据 ≠ 不存在问题）。
4. **安全与硬件耐久**：[54] 提出在交互式机器人自主中"闭合安全—学习回路"（deception game 设定）[54]，是少量直接触及安全—学习张力的来源；但针对人形硬件耐久、跌倒损伤的定量证据 `> 待核实` [54]。
5. **reward 工程可持续性**：[7] 明确指出既有全身操作方法受"复杂奖励工程"阻碍 [7]；[5] 用退火课程替代部分人工设计 [5]。是否有系统化的 reward 设计方法论，`> 待核实`。
6. **跨本体迁移**：轮足 [33]、纯腿足四足 [83][85]、人形 [87][90]、带推进器双足 [25] 的方法是否互通，候选证据未提供跨本体验证 [25][33][83][85][87][90] `> 待核实`。
7. **检索噪声本身是一个元问题**：约 30 条命中（[8][9][10][27][30][35][42][44][45][46][47][48][51][56][58][59][67][69][77][88][89][93][94][95][96][97][98][99]）与本主题无关，提示"人形/腿足"这一查询词在 arXiv 全库中的语义漂移风险，后续检索应叠加 `cs.RO` 与具体本体名约束。

---

## 八、建议关注清单（Watchlist）

| 优先级 | 条目 | 理由（含证据） | 待跟踪的具体问题 |
|---|---|---|---|
| P0 | [2] Learning Sim-to-Real Humanoid Locomotion in 15 Minutes | "分钟级 sim2real"是被引用的强主张，但仅有预印本与摘要级证据 [2] | 是否中稿？本体与任务数？真机成功率？ |
| P0 | [81] Locomotion Beyond Feet | 全身接触式运动的新前沿，团队权威性较高 [81] | 是否有量化地形清单与真机视频外的评测？ |
| P0 | [14] Real-World Humanoid Locomotion with RL | 真机人形 RL 行走的转折点，也是后续工作的公共基线 [14] | 后续发表 venue 与引用量 `> 待核实` |
| P1 | [3] 分层降阶 MPC + [15] 推扰恢复 | 模型控制路线的当代代表，与学习式路线构成可比较的两极 [3][15] | 与神经全身控制器同任务集对比是否存在？ |
| P1 | [75] Teacher Motion Priors / [74] VMTS / [73] CTS | 本体感知与视觉感知两条 teacher-student 分支的对照样本 [73][74][75] | 是否有统一基准上的跨模态对照？ |
| P1 | [63] Retargeting Matters / [61] Dense Temporal Motion Retargeting | 直指 embodiment gap 这一工程瓶颈 [61][63] | 重定向质量如何量化？是否开源？ |
| P1 | [53] Robot Trains Robot | 针对"真机学习稀缺"的直接回应 [53] | 真机训练的安全边界与成本 |
| P2 | [60] HumanoidBench / [68] Open X-Embodiment | 可比性的两个关键载体 [60][68] | 榜单当前排名与参与方法数 `> 待核实` |
| P2 | [85][86][87] parkour 三连 | 敏捷跑跳演进链的完整样本 [85][86][87] | 人形跑酷是否已复现？真机成功率？ |
| P2 | [90][91] 起身策略 | 落地可用性高的任务，容易形成真机可比指标 [90][91] | 跨姿态泛化边界 |
| P2 | 种子项目 legged_gym / IsaacLab / ProtoMotions / unitree_rl_gym | 工程栈是复现的前提 | star/最近提交/issue 活跃度需实时核实 `> 待核实` |

---

## 七、数据集、基准与开放问题

> 本节说明：本次可引用来源清单（[1]–[99]）**未携带 citations / stars / 下载量等量化热度字段**，因此下表中“热度证据”一列凡无来源支撑者一律标注 `> 待核实`，不做任何数字推测。四类证据均给出引用编号或明确标注待核实。

### 7.1 数据集、基准与运动资源对照表

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| HumanoidBench: Simulated Humanoid Benchmark for Whole-Body Locomotion and Manipulation | 2024 | arXiv 预印本（cs.RO）[60] | `> 待核实`（来源清单未给引用数）[60] | arXiv 预印本，未在来源中标注同行评审 venue [60] | 中——标题即定位“人形全身 locomotion+manipulation 基准”，是本主题可引用来源中唯一显式以 humanoid benchmark 命名的条目，具备基准排他性 [60] | ★★★★☆——若研究人形全身控制评测，这是首选可比入口；但须核实其是否已中稿及任务口径 [60] | http://arxiv.org/abs/2403.10506v2 | 明确为 **simulated** 基准，不含真机口径 [60] |
| Open X-Embodiment: Robotic Learning Datasets and RT-X Models | 2023 | 跨机构联合（arXiv 预印本）[68] | `> 待核实`（来源清单未给引用数/star）[68] | arXiv 预印本 + 公开数据集与 RT-X 模型，版本号已达 v9，提示为长期维护文档（基于编号推断）[68] | 高——跨机构联合数据集与通用策略模型，是本领域规模最大的公开机器人数据聚合之一 [68] | ★★★★☆——数据规模与生态影响力大，但主体是操作/多本体数据，对腿足 locomotion 步态评测覆盖有限 [68] | http://arxiv.org/abs/2310.08864v9 | 需注意：不是腿足运动专用基准 [68] |
| Bamboo: Building Mega-Scale Vision Dataset Continually with Human-Machine Synergy | 2022 | arXiv 预印本 [72] | `> 待核实` [72] | arXiv 预印本 [72] | 低（对本主题）——其为视觉识别数据集，与机器人运动控制无直接关系 [72] | ★☆☆☆☆——不建议作为 locomotion 证据引用，仅用于标注“同名/跨域数据集的检索噪声” [72] | http://arxiv.org/abs/2203.07845v2 | **口径警示**：名为数据集但与腿足运动无关 [72] |
| LAFAN1 / Ubisoft La Forge Animation Dataset | `> 待核实` | Ubisoft La Forge（主题 YAML 种子资源，未纳入本次编号引用） | `> 待核实` | 主题 YAML 种子资源，本次未取得可编号来源 [—] | `> 待核实` | ★★★☆☆——常被作为人形动作先验来源，但本次检索未取得可核查条目，须补证 | https://github.com/ubisoft/ubisoft-laforge-animation-dataset（种子资源提供） | 用途为动作先验/动作模仿，具体帧数、本体、许可 `> 待核实` |
| AMASS (motion capture) | `> 待核实` | MPI（主题 YAML 种子资源，未纳入本次编号引用） | `> 待核实` | 主题 YAML 种子资源，本次未取得可编号来源 [—] | `> 待核实` | ★★★☆☆——人体动作捕捉的通用底座，但本次无编号证据支撑其口径 | https://amass.is.tue.mpg.de/（种子资源提供） | 需经 retargeting 才能用于人形；重定向质量直接决定可比性 [63] |
| MuJoCo Playground | `> 待核实` | `> 待核实` | `> 待核实` | **本次可引用来源列表中无对应条目** | `> 待核实` | `> 待核实`——无编号来源，暂不评估 | `> 待核实` | 主题提及但本次未取得证据，不得凭记忆描述 |
| 运动重定向方法与资源链路（Spatio-Temporal Motion Retargeting / Retargeting Matters / Dense Temporal Motion Retargeting / UniTracker） | 2024–2026 | arXiv 预印本（cs.RO）[62][63][61][65] | `> 待核实`（来源清单未给引用数）[62][63][61][65] | 均为 arXiv 预印本，未见同行评审标注 [62][63][61][65] | 中——重定向是“人体动捕→人形/四足可用动作”的必要环节，多篇工作集中出现说明其为当前瓶颈环节 [61][62][63][65] | ★★★★☆——若使用 AMASS/LAFAN1 类数据，必须先过这一环；“Retargeting Matters”标题本身即指出该环节被低估 [63] | http://arxiv.org/abs/2404.11557v3 ；http://arxiv.org/abs/2510.02252v1 ；http://arxiv.org/abs/2609.38617v1 ；http://arxiv.org/abs/2507.07356v3 | 重定向误差会传导为策略性能差异，破坏跨论文可比性 [63] |
| 评测方法论：Sim-to-Real 政策评测基准视角 | 2025 | arXiv 预印本 [55] | `> 待核实` [55] | arXiv 预印本 [55] | 中——正面处理“如何公平比较 sim-to-real 策略”这一问题，属基准方法论层面 [55] | ★★★☆☆——对建立可比评测有参考价值，但本身不是数据集/榜单 [55] | http://arxiv.org/abs/2508.11117v1 | 与 [43] 的 sim2real 综述可并读 [43][55] |

### 7.2 口径与可比性问题（为什么这些资源难以直接横比）

1. **仿真基准与真机结果的错位**：HumanoidBench 明确为 simulated 基准 [60]，而近年的代表性进展多以真机验证为主（如 15 分钟 sim2real 人形控制 [2]、挑战地形人形运动 [4]、真机 RL 人形行走 [14]）。两类结果不在同一口径上，不能直接排序 [2][4][14][60]。
2. **数据集主体不是腿足运动**：Open X-Embodiment 虽为大规模跨本体数据与 RT-X 模型 [68]，但其重心在操作与多本体泛化，腿足步态评测覆盖有限 [68]；将其当作 locomotion 榜单会误判 [68]。
3. **同名/跨域数据集的混淆风险**：Bamboo 为视觉识别数据集 [72]，与腿足运动无关，出现在本主题检索结果中属召回噪声 [72]。
4. **动作数据的可用性受 retargeting 制约**：人体动捕资源需经形态差异适配（embodiment gap）才能被人形使用，重定向质量差异会直接改变策略训练结果，破坏跨论文可比性 [61][63]；这一点在“Retargeting Matters”中被直接点名为关键问题 [63]。
5. **缺少跨输入模态的受控基准**：现有方法输入分裂为本体感知+特权信息蒸馏 [75]、深度图像视觉 [82]、本体感知环境状态估计 [33]、人类关键帧先验+RL [81]，但未在统一地形/统一本体上做受控对照，因此“本体感知 vs 视觉 vs 多模态”的边界只能间接推断 [33][75][81][82]。
6. **教师—学生路线的训练设定不统一**：并发教师—学生（CTS）[73]、视觉辅助教师—学生（VMTS）[74]、教师运动先验 [75] 三者在教师信息、学生输入与地形设置上各不相同，缺乏共享评测协议 [73][74][75]。

### 7.3 开放问题与争议

**（1）sim2real 真实差距到底有多大？**
- sim2real 是系统性难题而非单一技巧问题，已有综述性工作专门梳理其来源与对策 [43]；面向双足 locomotion 的章节式梳理进一步把“仿真诅咒（curse of simulation）”拆解为主要误差来源 [32]。
- 有工作主张把仿真到真机的训练压缩到 15 分钟量级 [2]，也有工作主张直接做真机适配与在线学习（Robot Trains Robot [53]；真机微调持续学习 [34]），两条路线隐含对 sim2real 差距严重程度的**相反判断**：前者认为差距可被大规模并行仿真+域随机化高效跨越 [2]，后者认为必须回到真实世界继续学 [34][53]。这一分歧在本次证据中**未被任何统一基准裁决**。
- 证据缺口：sim2real 局限具有任务与场景依赖性（在精密农业操作场景中已被明确讨论 [50]），但该来源属操作域，**不能直接外推到腿足**，只能作为方法学类比 [50]。腿足域内的量化差距 `> 待核实`。

**（2）复现困难与失败案例的缺失**
- 现有可引用来源几乎全部报告成功案例，negative results 与失败模式描述稀缺；评测方法论工作 [55] 提供了一个改进方向，但尚未形成社区通用协议 [55]。
- 故障/异常场景有少量专门工作（如 DreamFLEX 面向崎岖地形异常情况的容错控制器 [83]），可作为“承认失败模式”的少数代表 [83]。
- 结论：**“哪些方法在什么条件下必然失败”在本次证据中基本空白** `> 待核实`。

**（3）安全与硬件耐久**
- 安全—学习闭环问题已被作为独立问题提出（Deception Game [54]），说明安全约束与探索效率的冲突尚未解决 [54]。
- 摔倒后的恢复能力被单独建模（真机人形起身策略 [90]、多姿态起身控制 [91]），这从侧面反映**跌倒仍是常态风险**，而非边缘事件 [90][91]。
- 硬件耐久、关节磨损、长期运行退化在本次可引用来源中**无量化证据** `> 待核实`。

**（4）仿真 SOTA 与真机 SOTA 的错位**
- 仿真侧有统一基准 [60]，真机侧则多为单团队、单本体的自建任务（人形挑战地形 [4]、真机 RL 行走 [14]、快速 sim2real [2]），任务数、成功率、硬件型号口径互不一致 [2][4][14][60]。
- 因此“谁是当前 SOTA”在本主题内**没有统一的第三方裁决**；跨论文数字直接比较不成立 `> 待核实`。
- 改善路径：以基准化视角审视 sim-to-real 评测 [55]，并依赖公开评测协议而非论文自述 [55]。

**（5）奖励工程（reward engineering）的可持续性**
- 有工作明确指出人形全身操作受困于硬件流程复杂与 **reward engineering 复杂**，导致可展示的自主技能仍然有限 [7]；这与人形全身羽毛球采用“退火式 RL 课程（annealed RL curriculum）”来规避直接奖励设计的做法形成呼应 [5]。
- 现有缓解手段包括：课程退火 [5]、动作先验/关键帧引导 [81]、重定向后的动作跟踪 [63][65]、以及避免奖励工程的演示驱动接口 [7]。但这些手段之间的可迁移性 `> 待核实`。
- 争议点：奖励工程究竟是可通过课程与先验被“消解”的工程细节 [5][81]，还是根本性瓶颈 [7]，本次证据**未给出裁决性结论**。

**（6）检索噪声与证据卫生（对本主题结论的直接影响）**
- 以下来源经核对与“人形与腿足运动”无关，属检索噪声，不应作为本领域证据引用：语音评测挑战赛 [93]、LLM 评测共享任务 [77]、基座模型透明度指数 [89]、视频参与度预测挑战赛 [58]、图像超分挑战赛 [59]、越南法律问答挑战赛 [95]、AudioMOS 挑战赛 [96]、强透镜宇宙学 [97]、RO-MAN 社会机器人工作坊 [98]、ACM MM 事件图像挑战赛 [99]、H1 量能器/结构函数（高能物理）[8][9][10]、量子控制综述 [27]、AGN 巡天 [30]、微分博弈/分数阶控制综述 [31]、已撤稿论文 [35]、ML4H 工作坊 [46]、Vicinity Vision Transformer [88]、大规模敏捷开发回顾 [94]、价值奖励探索方法 [47]、极噪观测多智能体 RL [42]、DRL 综述 [44]、Transcoder 网络 [45]、演化方法对比 [48]、一次性导航 RL [51]、抓取与运动规划挑战赛 [56]、Waymo 语义分割 [67]、RSNA 医学影像数据集 [69]。
- **对子问题 q1/q3/q6 的直接后果**：这些子问题的候选发现中存在大量上述噪声条目（例如 q1 引用了 [93]，q3 引用了 [31]，q6 引用了 [47]），其 `confidence=low` 与 `recommendation=★★★★☆` 的组合属于**抽取阶段的评分错配**，在本报告中被降级处理，不作为论断依据。
- 同理，Open Ant 为通用 RL 研究平台 [41]，与腿足/人形运动仅有平台层面弱相关，不宜作为 locomotion 方法学证据 [41]。

**（7）跨本体迁移未验证**
- 轮足混合平台 [33]、四足与双足、人形三类本体的 sim2real 方法是否互通，在本次证据中**没有跨本体验证实验** `> 待核实` [33][4][14]。
- 运动重定向工作分散在四足 [62] 与人形 [61][63][65] 两侧，说明形态适配知识尚未统一 [61][62][63][65]。

**（8）本节结论性判断**
- 可确证：本主题**已有仿真基准** [60] 与**大规模公开数据** [68]，但二者都**不是腿足 locomotion 的专用评测口径** [60][68]；**运动数据的可用性瓶颈在 retargeting** [61][63]。
- 待核实：LAFAN1 与 AMASS 的具体版本、帧数、许可与真机验证记录 `> 待核实`；MuJoCo Playground 在本主题中的定位 `> 待核实`。
- 尚空缺：跨模态受控基准、统一真机评测协议、系统性 negative results、长期硬件耐久数据。

## 参考来源

[1] A ROS-based Software Framework for the NimbRo-OP Humanoid Open Platform — http://arxiv.org/abs/1809.11051v1
[2] Learning Sim-to-Real Humanoid Locomotion in 15 Minutes — http://arxiv.org/abs/2512.01996v1
[3] Hierarchical Reduced-Order Model Predictive Control for Robust Locomotion on Humanoid Robots — http://arxiv.org/abs/2509.04722v1
[4] Learning Humanoid Locomotion over Challenging Terrain — http://arxiv.org/abs/2410.03654v1
[5] Humanoid Whole-Body Badminton via an Annealed Reinforcement Learning Curriculum — http://arxiv.org/abs/2511.11218v4
[6] The Role of Domain Randomization in Training Diffusion Policies for Whole-Body Humanoid Control — http://arxiv.org/abs/2411.01349v1
[7] Humanoid Manipulation Interface: Humanoid Whole-Body Manipulation from Robot-Free Demonstrations — http://arxiv.org/abs/2602.06643v2
[8] The Electronics of the H1 Lead/Scintillating-Fibre Calorimeters — http://arxiv.org/abs/physics/9812042v1
[9] Measurement of the Charm and Beauty Structure Functions using the H1 Vertex Detector at HERA — http://arxiv.org/abs/0907.2643v2
[10] Measurement of F_2^ccbar and F_2^bbbar at High Q^2 using the H1 Vertex Detector at HERA — http://arxiv.org/abs/hep-ex/0411046v1
[11] Humanoid Agent via Embodied Chain-of-Action Reasoning with Multimodal Foundation Models for Zero-Shot Loco-Manipulation — http://arxiv.org/abs/2504.09532v3
[12] NimbRo-OP2: Grown-up 3D Printed Open Humanoid Platform for Research — http://arxiv.org/abs/1809.11144v1
[13] The Synthesis of Optimal Control Laws Using Isaacs' Method for the Solution of Differential Games — http://arxiv.org/abs/2112.10849v2
[14] Real-World Humanoid Locomotion with Reinforcement Learning — http://arxiv.org/abs/2303.03381v2
[15] Bracing for Impact: Robust Humanoid Push Recovery and Locomotion with Reduced Order Models — http://arxiv.org/abs/2505.11495v2
[16] HOVER: Versatile Neural Whole-Body Controller for Humanoid Robots — http://arxiv.org/abs/2410.21229v2
[17] CHILD (Controller for Humanoid Imitation and Live Demonstration): a Whole-Body Humanoid Teleoperation System — http://arxiv.org/abs/2508.00162v2
[18] Humanoid Whole-Body Manipulation via Active Spatial Brain and Generalizable Action Cerebellum — http://arxiv.org/abs/2605.21133v2
[19] Whole-Body Geometric Retargeting for Humanoid Robots — http://arxiv.org/abs/1909.10080v1
[20] OmniH2O: Universal and Dexterous Human-to-Humanoid Whole-Body Teleoperation and Learning — http://arxiv.org/abs/2406.08858v1
[21] Learning Human-to-Humanoid Real-Time Whole-Body Teleoperation — http://arxiv.org/abs/2403.04436v1
[22] TWIST: Teleoperated Whole-Body Imitation System — http://arxiv.org/abs/2505.02833v1
[23] CLOT: Closed-Loop Global Motion Tracking for Whole-Body Humanoid Teleoperation — http://arxiv.org/abs/2602.15060v2
[24] Dynamic Locomotion Teleoperation of a Wheeled Humanoid Robot Reduced Model with a Whole-Body Human-Machine Interface — http://arxiv.org/abs/2109.03906v1
[25] Capture Point Control in Thruster-Assisted Bipedal Locomotion — http://arxiv.org/abs/2406.14799v1
[26] Dynamic Walking: Toward Agile and Efficient Bipedal Robots — http://arxiv.org/abs/2010.07451v1
[27] Quantum control theory and applications: A survey — http://arxiv.org/abs/0910.2350v3
[28] Feedback Regularization and Geometric PID Control for Robust Stabilization of a Planar Three-link Hybrid Bipedal Walking Model — http://arxiv.org/abs/1710.02066v1
[29] Robust Dynamic Walking for a 3D Dual-SLIP Model under One-Step Unilateral Stiffness Perturbations: Towards Bipedal Locomotion over Compliant Terrain — http://arxiv.org/abs/2203.07471v2
[30] A rich bounty of AGN in the 9 square degree Bootes survey: high-z obscured AGN and large-scale structure — http://arxiv.org/abs/astro-ph/0611654v1
[31] Fractional Calculus in Optimal Control and Game Theory: Theory, Numerics, and Applications -- A Survey — http://arxiv.org/abs/2512.12111v1
[32] Sim-to-Real Transfer in Deep Reinforcement Learning for Bipedal Locomotion — http://arxiv.org/abs/2511.06465v1
[33] ATRos: Learning Energy-Efficient Agile Locomotion for Wheeled-legged Robots — http://arxiv.org/abs/2510.09980v1
[34] Legged Robots that Keep on Learning: Fine-Tuning Locomotion Policies in the Real World — http://arxiv.org/abs/2110.05457v1
[35] This paper has been withdrawn — http://arxiv.org/abs/cond-mat/0309395v2
[36] Learning Robust, Agile, Natural Legged Locomotion Skills in the Wild — http://arxiv.org/abs/2304.10888v3
[37] Deploying COTS Legged Robot Platforms into a Heterogeneous Robot Team — http://arxiv.org/abs/2106.07182v1
[38] On Terrain-Aware Locomotion for Legged Robots — http://arxiv.org/abs/2212.00683v1
[39] Oncilla robot: a versatile open-source quadruped research robot with compliant pantograph legs — http://arxiv.org/abs/1803.06259v2
[40] A Legged Soft Robot Platform for Dynamic Locomotion — http://arxiv.org/abs/2011.06749v2
[41] The Open Ant: A Robot Platform for Reinforcement Learning Research — http://arxiv.org/abs/2607.18488v1
[42] Multi-agent Deep Reinforcement Learning with Extremely Noisy Observations — http://arxiv.org/abs/1812.00922v1
[43] Sim-to-Real Transfer in Deep Reinforcement Learning for Robotics: a Survey — http://arxiv.org/abs/2009.13303v2
[44] Deep Reinforcement Learning: An Overview — http://arxiv.org/abs/1701.07274v6
[45] Model-Based Regularization for Deep Reinforcement Learning with Transcoder Networks — http://arxiv.org/abs/1809.01906v2
[46] Machine Learning for Health (ML4H) Workshop at NeurIPS 2018 — http://arxiv.org/abs/1811.07216v2
[47] Value Bonuses using Ensemble Errors for Exploration in Reinforcement Learning — http://arxiv.org/abs/2602.12375v1
[48] Comparing Deep Reinforcement Learning and Evolutionary Methods in Continuous Control — http://arxiv.org/abs/1712.00006v2
[49] Bridging the Sim2Real Gap: Vision Encoder Pre-Training for Visuomotor Policy Transfer — http://arxiv.org/abs/2501.16389v2
[50] The Importance and the Limitations of Sim2Real for Robotic Manipulation in Precision Agriculture — http://arxiv.org/abs/2008.03983v1
[51] One-Shot Reinforcement Learning for Robot Navigation with Interactive Replay — http://arxiv.org/abs/1711.10137v2
[52] Towards Miniature Humanoid Tele-Loco-Manipulation Using Virtual Reality and Reinforcement Learning — http://arxiv.org/abs/2607.20399v1
[53] Robot Trains Robot: Automatic Real-World Policy Adaptation and Learning for Humanoids — http://arxiv.org/abs/2508.12252v2
[54] Deception Game: Closing the Safety-Learning Loop in Interactive Robot Autonomy — http://arxiv.org/abs/2309.01267v2
[55] Robot Policy Evaluation for Sim-to-Real Transfer: A Benchmarking Perspective — http://arxiv.org/abs/2508.11117v1
[56] Grasp and Motion Planning for Dexterous Manipulation for the Real Robot Challenge — http://arxiv.org/abs/2101.02842v1
[57] Hybrid Internal Model: Learning Agile Legged Locomotion with Simulated Robot Response — http://arxiv.org/abs/2312.11460v3
[58] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1
[59] NTIRE 2025 Challenge on Image Super-Resolution (x4): Methods and Results — http://arxiv.org/abs/2504.14582v3
[60] HumanoidBench: Simulated Humanoid Benchmark for Whole-Body Locomotion and Manipulation — http://arxiv.org/abs/2403.10506v2
[61] Dense Temporal Motion Retargeting for Legged Robots — http://arxiv.org/abs/2609.38617v1
[62] Spatio-Temporal Motion Retargeting for Quadruped Robots — http://arxiv.org/abs/2404.11557v3
[63] Retargeting Matters: General Motion Retargeting for Humanoid Motion Tracking — http://arxiv.org/abs/2510.02252v1
[64] Simulating Infant First-Person Sensorimotor Experience via Motion Retargeting from Babies to Humanoids — http://arxiv.org/abs/2604.27583v2
[65] UniTracker: Learning Universal Whole-Body Motion Tracker for Humanoid Robots — http://arxiv.org/abs/2507.07356v3
[66

---

*Generated by research-bot · topic=`embodied-humanoid` · depth=`standard` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading · model=`deepseek-v4-flash` · sources=99 · duration=389s · 2026-10-05T22:31:07+00:00*
