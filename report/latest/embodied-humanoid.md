# 人形与腿足运动（Humanoid & Legged Locomotion）学习式控制调研报告

**日期**：2026-10-02（UTC） ｜ **领域**：具身智能 · 人形与腿足运动（learning-based locomotion / whole-body control / sim2real） ｜ **检索源**：32 条候选来源（编号 [1]–[32]），其中与本主题直接相关约 20 条，其余为题录漂移或术语类来源 ｜ **证据基线**：以 arXiv 预印本（cs.RO / cs.LG）为主，含 1 篇机构库学位论文、1 篇综述、2 条词典/百科术语源；**本批次未取得任何公认数据集/榜单的一手来源**

---

## 摘要（Executive Summary）

本报告基于 32 条候选来源，梳理人形与腿足机器人**学习式运动控制**（RL locomotion）、**全身控制**（Whole-Body Control, WBC）与 **sim2real** 的前沿进展、奠基工作、开源工程栈与开放争议。需要首先声明一个贯穿全文的限制：**本批次证据以「论文摘要级」信息为主，普遍缺少本体型号、自由度、任务数量、成功率、训练成本等可横向对比的量化口径；热度类信号（引用数、GitHub star、榜单排名）在候选块中全部缺失**。因此本报告的结论强度普遍为「方法方向可辨、性能对比不可做」。

**已取得的可核查要点：**

1. **动态全身交互是 2025–2026 年的活跃方向**：[6] 提出以退火式强化学习课程（annealed RL curriculum）训练**统一全身控制器**，协调步法（footwork）与击球（striking）完成人形羽毛球任务，且明确**不依赖运动先验（motion priors）或专家数据**；该预印本已迭代至 v4，说明仍在持续修订 [6]。
2. **遥操作 + RL 的身体分工范式向小型人形下移**：上身 VR 遥操作、下身 RL 平衡与运动的控制栈此前主要见于昂贵的全尺寸平台，[1] 报告了一套面向**小型人形**的顺应式全身临场感（compliant full-body telepresence）控制栈 [1]。
3. **sim2real 的核心痛点被明确表述**：[27] 摘要直接指出「大规模并行仿真已把 RL 训练时间从数天压缩到分钟级，但快速可靠的人形 sim-to-real 仍因高维度与域随机化（domain randomization）而困难」，并以标题主张「15 分钟完成 sim-to-real 人形运动学习」[27]。这是本批次中对 sim2real 归因问题**最直接**的一条表述。
4. **真机验证的稀疏性得到实例化**：本批次中**唯一**明确写出真机平台型号的条目是 [25]（`Unitree G1`，同时报告仿真与硬件实验），方法为高层 ALIP 步态动力学非线性 MPC + 低层扩展 SRB-MPC 线性 MPC [25]；与之对照，[24] 的验证表述为「Extensive simulation results」，属**仿真结论**而非真机 SOTA [24]。
5. **模型式与学习式的对照已有初步尝试**：[13] 以「Benchmarking MPC and RL for Legged Robot Locomotion」为题，是本批次中唯一以**基准对比**为定位的条目，但载体为机构库学位论文（DOI 指向 MTU 学位论文库），权威等级低于同行评审期刊 [13]。
6. **奠基脉络可辨但需外部补充**：腿足 RL 综述 [22]（2020, IEEE）、RMA 快速运动适应 [23]（2021）、真机在线微调 [19]（2021）、野外敏捷自然步态 [15]（2023）、机器人跑酷 [20]（2023）构成「端到端 RL → 在线适应 → 敏捷化」的演进骨架；但本批次仅提供标题/题录级信息，细节均 `> 待核实`。

**主要缺口（必须在后续检索中补齐）：**

- 本批次**没有任何**人形/腿足方向的公认数据集、仿真基准或真机榜单（Open X-Embodiment、DROID、LIBERO、SimplerEnv、RoboArena 等均未出现在候选来源中）→ 第七节相关结论 **`> 待核实`**。
- **热度轴全线缺失**：所有 32 条来源均未附带引用数、star 数或下载量 → 每条的「热度」均标 `> 待核实`，不得以记忆填补。
- **候选来源存在明显题录漂移**：如 [28] 医学腹部创伤 CT 数据集、[29] 短视频 UGC 超分数据集 KwaiSR、[32] 金融领域 LLM 数值推理基准、[21] 对话机器人竞赛、[10][11][12] 词典/百科条目，与本主题无实质关联，本报告仅作为检索质量问题的披露保留，**不作为论据使用**。

---

## 一、关键前沿进展（近 1–2 年）

本节只收录时间戳落在 2024-10 之后、且与本主题直接相关的条目。**「最新」的判定依据是来源链接中的 arXiv 提交/版本时间与候选块给出的日期，而非模型内部知识。**

### 1.1 统一全身控制器：动态任务与课程的结合

**[6] Humanoid Whole-Body Badminton via an Annealed Reinforcement Learning Curriculum**（arXiv:2511.11218v4，2025-11-14，cs.RO）

- **核心贡献**：以 RL 训练管线产出用于**人形羽毛球**的统一全身控制器，协调步法与击球；摘要强调不依赖 motion priors 或专家数据 [6]。
- **验证口径**：候选块**未提供**本体型号、仿真/真机划分、任务数量与成功率 → `> 待核实` [6]。
- **热度**：`> 待核实`（候选块未提供引用数/star）[6]。
- **权威**：arXiv 预印本（cs.RO），候选块未标注会议或期刊，**同行评审状态未确认** [6]。
- **关注度**：**中** —— 依据为该预印本已更新至 **v4**（URL 版本号可核），说明作者持续修订；但无引用/榜单信号 [6]。
- **推荐度**：**★★★★☆** —— 与本主题「WBC + 动态任务」交叉点相关性最高，建议优先精读并补齐量化口径 [6]。

### 1.2 小型人形平台的遥操作—移动—操作控制栈

**[1] Towards Miniature Humanoid Tele-Loco-Manipulation Using Virtual Reality and Reinforcement Learning**（arXiv:2607.20399v1，2026-07-22，cs.RO）

- **核心贡献**：面向**小型人形**提出顺应式全身临场感控制栈；摘要指出「VR 遥操作上身 + RL 控制下身平衡与运动」是厂商常用做法，但此前多局限于昂贵的全尺寸机器人，小型人形因传感器与自由度较少、仿生程度较低而缺少类似进展 [1]。
- **验证口径**：本体具体型号、自由度、验证规模 → `> 待核实` [1]。
- **热度**：`> 待核实` [1]。
- **权威**：arXiv 预印本（cs.RO），**同行评审状态未确认** [1]。
- **关注度**：**低** —— 无引用数/star/社区讨论信号，仅可判定为 2026 年新近预印本 [1]。
- **推荐度**：**★★★☆☆** —— 对「小型人形 + RL 下身控制」这一细分本体有补充价值，但证据仅限摘要 [1]。

### 1.3 RL 研究的物理平台与 sim2real 迁移

**[4] The Open Ant: A Robot Platform for Reinforcement Learning Research**（arXiv:2607.18488v1，2026-07-20，cs.RO）

- **核心贡献**：摘要指出 RL 研究虽在物理与仿真领域均有成功案例，但主流方法仍植根于仿真，使算法与研究者向物理现实迁移充满不确定性，并据此提出一个旨在简化该迁移的物理平台 [4]。
- **验证口径**：**摘要被截断于 "introducing the…"**，本体的形态细节（是否为腿足/人形）与任务数 → `> 待核实` [4]。
- **热度**：`> 待核实` [4]。
- **权威**：arXiv 预印本（cs.RO），未见官方仓库说明 [4]。
- **关注度**：**低** —— 无热度信号，且摘要信息不完整 [4]。
- **推荐度**：**★★☆☆☆** —— 与 sim2real 维度相关，但需先核实全文与本体形态 [4]。

### 1.4 通用 RL 探索算法（非机器人本体工作）

**[3] Value Bonuses using Ensemble Errors for Exploration in Reinforcement Learning (VBE)**（arXiv:2602.12375v1，2026-02-12，cs.LG）

- **核心贡献**：指出既有 value bonus 方法只能在见到更高奖励后回溯提升，无法鼓励**首次访问某状态动作**；VBE 维护一组随机动作价值函数（RQFs），以估计误差构造价值奖励，提供首次访问乐观性与深度探索 [3]。
- **验证口径**：本工作属**通用 RL 算法**，候选块未涉及任何机器人本体、仿真/真机或运动控制任务 [3]。
- **热度**：`> 待核实` [3]。
- **权威**：arXiv 预印本（cs.LG），**同行评审状态未确认** [3]。
- **关注度**：**低** —— 无引用信号，且方向属机器学习基础算法 [3]。
- **推荐度**：**★★☆☆☆** —— 与腿足/人形运动控制**无直接本体或任务关联**，仅作为底层探索方法线索保留 [3]。

### 1.5 其他近 1–2 年内相关条目（题录级）

| 条目 | 时间 | 方向 | 可用信息等级 |
|---|---|---|---|
| [7] The Role of Domain Randomization in Training Diffusion Policies for Whole-Body Humanoid Control | 2024-11 | 域随机化 × 扩散策略 × 人形全身控制 | 标题级，`> 待核实` |
| [9] Humanoid Manipulation Interface (HuMI) | 2026-02 | 无机器人演示（robot-free demonstrations）的人形全身操作 | 标题级，`> 待核实` |
| [14] ATRos: Learning Energy-Efficient Agile Locomotion for Wheeled-legged Robots | 2025-10 | 轮足混合本体的能效敏捷运动，全身控制被明确称为难点 | 摘要级 [14] |
| [18] Causal-Paced Deep Reinforcement Learning | 2025-07 | 课程 RL 的任务序列设计（因果节奏） | 摘要级 [18] |
| [26] Learning Humanoid Locomotion over Challenging Terrain | 2024-10 | 人形复杂地形运动 | 标题级，`> 待核实` |
| [30] Bridging the Sim2Real Gap: Vision Encoder Pre-Training for Visuomotor Policy Transfer | 2025-01 | 视觉编码器预训练的 sim2real 迁移 | 标题级，`> 待核实` |

**四轴证据（本节合并）**：热度：全部 `> 待核实`（候选块无引用数/star/下载量）[7][9][14][18][26][30]；权威：均为 arXiv 预印本，候选块未标注同行评审 venue [7][9][14][18][26][30]；关注度：**低**（无任何热度或榜单信号可依据）[7][9][14][18][26][30]；推荐度：**★★☆☆☆**（仅 [14][18] 有摘要级内容，其余为标题级线索，需补检全文）[7][9][14][18][26][30]。

---

## 二、学习式 locomotion 与全身控制

### 2.1 方法流派：从模块化管线到统一控制器

本批次证据可辨识出三条并行路线，但**均缺少可直接对比的量化口径**：

1. **模型式（MPC/降阶模型）路线**：[25] 采用分层设计 —— 高层为 ALIP 步态动力学的非线性 MPC（同时优化步周期、步长、踝力矩），低层为扩展 SRB-MPC 线性 MPC（额外纳入简化的手臂与躯干动力学）；作者为 Adrian B. Ghansah、Sergio A. Esteban、Aaron D. Ames [25]。
   - 热度：`> 待核实` [25]；权威：arXiv 预印本（cs.RO, 2509.04722v1, 2025-09-05），**未标注同行评审 venue**，作者团队在双足控制领域知名（属弱推断，非热度信号）[25]；关注度：**低**（无引用/star 信号）[25]；推荐度：**★★★☆☆**（真机口径讨论的核心示例）[25]。
2. **降阶模型 + 环境接触利用路线**：[24] 以 SRB-MPC 结合 HLIP 动力学，**利用墙壁等环境**辅助推挤恢复；验证表述为「Extensive simulation results on a humanoid robot demonstrate improved perturbation rejection and tr…」（截断），**未出现真机实验语句** [24]。
   - 热度：`> 待核实` [24]；权威：arXiv 预印本（cs.RO, 2505.11495v2，提交 2025-05-16，v2 修订 2026-06-22），作者含 Aaron D. Ames，**未标注同行评审 venue** [24]；关注度：**低**（无热度信号；v2 修订说明作者仍在迭代）[24]；推荐度：**★★★☆☆**（仿真/真机证据口径区分的示例）[24]。
3. **端到端 RL 统一控制器路线**：[6]（羽毛球全身控制）、[27]（15 分钟 sim2real 人形运动）、[2]（多样姿态起立控制，标题级）。其中 [6] 明确不依赖 motion priors [6]，[2] 从标题看聚焦「跨多样姿态的起立控制」[2]，但**本体、任务数与成功率均 `> 待核实`** [2][6][27]。

### 2.2 全身控制与遥操作/操作任务的交叉

- [1] 的全身临场感栈把「上身遥操作 + 下身 RL」这一分工明确化，并指出小型人形因传感器/自由度受限而仿生度较低 [1]。
- [8] CHILD（Controller for Humanoid Imitation and Live Demonstration）自我定位为「全身人形遥操作系统」（arXiv:2508.00162v2，2025-08）[8]。
- [9] HuMI 提出「从无机器人演示（robot-free demonstrations）出发的人形全身操作」（arXiv:2602.06643v2，2026-02）[9]。
- [7] 研究域随机化在**扩散策略（diffusion policies）** 训练中的作用，面向全身人形控制（2024-11）[7]。

**四轴证据**：热度：`> 待核实`（[7][8][9] 均无引用/star 数据）[7][8][9]；权威：三条均为 arXiv 预印本，候选块未标注会议/期刊，**同行评审状态未确认** [7][8][9]；关注度：**低**（无可核查热度信号；仅能从标题判断方向归属）[7][8][9]；推荐度：**★★★☆☆**（与遥操作/动作先验章节直接相关，建议在补检时优先获取全文与实验表）[7][8][9]。

### 2.3 本节小结与争议线索

> `> 待核实`：本批次**无法**回答「统一全身控制器相较分层 MPC 在多少任务、何种本体上更优」这一问题。原因：所有条目均缺失统一任务集与成功率口径，且 [25] 的单平台（`Unitree G1`）验证是唯一明确的真机实例 [25]，[24] 的结论为仿真结论 [24]。**「仿真 SOTA vs 真机 SOTA」的区分在本批次内只能定性说明，不能定量比较。**

---

## 三、sim2real 与地形适应

### 3.1 sim2real 困难的可核查表述与主张

**[27] Learning Sim-to-Real Humanoid Locomotion in 15 Minutes**（arXiv:2512.01996v1，2025-12-01，cs.RO）是本批次中**唯一直接陈述 sim2real 归因**的条目：

> 「Massively parallel simulation has reduced reinforcement learning (RL) training time for robots from days to minutes. However, achieving fast and reliable sim-to-real RL for humanoid control remains difficult due to the challenges introduced by factors such as high dimensionality and domain randomization.」[27]

该文据此提出一套基于 **off-policy RL** 的「简易配方」，标题主张 15 分钟完成 sim-to-real 人形运动学习 [27]。

- **热度**：`> 待核实` [27]。
- **权威**：arXiv 预印本（cs.RO），候选块**未标注同行评审 venue** [27]。
- **关注度**：**低** —— 无引用数或社区讨论热度信号，主张强度仅来自摘要自述 [27]。
- **推荐度**：**★★★★☆** —— 与「sim2real 归因不清」「训练成本瓶颈」两个议题直接相关，可作为候选一手来源；但**真机实验设置与可复现条件必须先核实**（含基线、本体、任务定义）[27]。

### 3.2 域随机化与策略表征

- [7] 以标题指向「域随机化在扩散策略训练中的作用」，对象为人形全身控制（2024-11）[7]。这与 [27] 把 domain randomization 列为 sim-to-real 难点因素形成**潜在张力**：一方把域随机化视为困难来源 [27]，另一方以标题暗示其可被系统研究并利用 [7]。**该张力属编者观察，两文的具体结论均 `> 待核实`** [7][27]。
- [30] 从**视觉编码器预训练**角度切入 sim2real 迁移（2025-01，标题级）[30]。
- [31] 讨论精密农业操作中 sim2real 的重要性与**局限**（2020，标题级；本体域为操作而非腿足，跨域外推需谨慎）[31]。

**四轴证据**：热度：`> 待核实` [7][30][31]；权威：均为 arXiv 预印本，未标注同行评审 [7][30][31]；关注度：**低**（无热度信号）[7][30][31]；推荐度：**★★☆☆☆**（[7] 与本节主题最贴近，建议优先于 [30][31] 精读）[7][30][31]。

### 3.3 地形适应

- [26] Learning Humanoid Locomotion over Challenging Terrain（2024-10，人形）[26] 与 [15] Learning Robust, Agile, Natural Legged Locomotion Skills in the Wild（2023，腿足）[15] 构成本批次中「复杂地形 / 野外地形」的两条题录线索，但候选块**未提供任务集、本体与成功率** → `> 待核实` [15][26]。
- 热度：`> 待核实` [15][26]；权威：arXiv 预印本 [15][26]；关注度：**低**（无热度信号）[15][26]；推荐度：**★★★☆☆**（[15] 与 [26] 是本节少数的直接对口工作，补检时需确认是否使用统一地形评测协议）[15][26]。

---

## 四、敏捷动作、跑跳与恢复

### 4.1 恢复与扰动拒斥

- **[2] Learning Humanoid Standing-up Control across Diverse Postures**（arXiv:2502.08378v2，2025）[2]：标题表明研究**跨多样姿态的人形起立控制**，属跌倒后恢复能力链的关键环节。
  - 热度：`> 待核实` [2]；权威：arXiv 预印本，候选块未标注 venue [2]；关注度：**低**（无热度信号）[2]；推荐度：**★★★☆☆**（起立/恢复在本批次中仅此一条直接对口，值得补检）[2]。
  - `> 待核实`：是否为零样本（zero-shot）起立、是否为真机、跨姿态数量的具体规模 —— 候选块均未提供。
- **[24] Bracing for Impact**：以「利用环境（如墙壁）」辅助推挤恢复为关键创新，组合 SRB-MPC 与 HLIP 动力学 [24]。**验证以仿真为主**（摘要仅称 Extensive simulation results）→ 不能作为真机恢复能力的证据 [24]。
- **[25] Hierarchical Reduced-Order MPC**：以分层降阶 MPC 达成「鲁棒运动」，并给出 `Unitree G1` 仿真+硬件实验 [25]（详见 2.1）。

### 4.2 敏捷与跑酷

- **[20] Robot Parkour Learning**（arXiv:2309.05665v2，2023）[20]：本批次中敏捷动作方向的核心题录，时间早于近 1–2 年窗口，归入「经典/奠基」更合适。
- **[14] ATRos**（2025-10）：面向**轮足（wheeled-legged）** 本体的能效敏捷运动；摘要指出「随着性能扩展，轮足机器人的**全身控制仍然困难**」[14]。
  - 热度：`> 待核实` [14]；权威：arXiv 预印本（cs.RO），未标注 venue [14]；关注度：**低**（无热度信号）[14]；推荐度：**★★★☆☆**（把「敏捷 + 能效 + 全身控制」三者耦合，与本主题最相关的非人形本体工作）[14]。

### 4.3 本节小结

> `> 待核实`：本批次**无法**给出「跑跳 / 跌倒恢复」的横向对比。可核查的硬事实仅有三点：(a) [6] 的动态全身控制**不使用 motion priors** [6]；(b) [24] 的恢复结论为**仿真结论** [24]；(c) [25] 是唯一写出真机本体型号（`Unitree G1`）的条目 [25]。

---

## 五、遥操作与动作先验

### 5.1 遥操作系统

| 工作 | 时间 | 关键点 | 引用 |
|---|---|---|---|
| [1] Miniature Humanoid Tele-Loco

## 参考来源

[1] Towards Miniature Humanoid Tele-Loco-Manipulation Using Virtual Reality and Reinforcement Learning — http://arxiv.org/abs/2607.20399v1
[2] Learning Humanoid Standing-up Control across Diverse Postures — http://arxiv.org/abs/2502.08378v2
[3] Value Bonuses using Ensemble Errors for Exploration in Reinforcement Learning — http://arxiv.org/abs/2602.12375v1
[4] The Open Ant: A Robot Platform for Reinforcement Learning Research — http://arxiv.org/abs/2607.18488v1
[5] A ROS-based Software Framework for the NimbRo-OP Humanoid Open Platform — http://arxiv.org/abs/1809.11051v1
[6] Humanoid Whole-Body Badminton via an Annealed Reinforcement Learning Curriculum — http://arxiv.org/abs/2511.11218v4
[7] The Role of Domain Randomization in Training Diffusion Policies for Whole-Body Humanoid Control — http://arxiv.org/abs/2411.01349v1
[8] CHILD (Controller for Humanoid Imitation and Live Demonstration): a Whole-Body Humanoid Teleoperation System — http://arxiv.org/abs/2508.00162v2
[9] Humanoid Manipulation Interface: Humanoid Whole-Body Manipulation from Robot-Free Demonstrations — http://arxiv.org/abs/2602.06643v2
[10] HUMANOID 中文 (简体)翻译：剑桥词典 - Cambridge Dictionary — https://dictionary.cambridge.org/zhs/%E8%AF%8D%E5%85%B8/%E8%8B%B1%E8%AF%AD-%E6%B1%89%E8%AF%AD-%E7%AE%80%E4%BD%93/humanoid
[11] Humanoid （英语单词）_百度百科 — https://baike.baidu.com/item/Humanoid/62902926
[12] humanoid 是什么意思_ humanoid 的翻译_音标_读音_用法_例句 ... — https://www.iciba.com/word?w=humanoid
[13] BENCHMARKING MODEL PREDICTIVE CONTROL AND REINFORCEMENT LEARNING FOR LEGGED ROBOT LOCOMOTION — https://doi.org/10.37099/mtu.dc.etdr/1677
[14] ATRos: Learning Energy-Efficient Agile Locomotion for Wheeled-legged Robots — http://arxiv.org/abs/2510.09980v1
[15] Learning Robust, Agile, Natural Legged Locomotion Skills in the Wild — http://arxiv.org/abs/2304.10888v3
[16] Stabilizing Extreme Q-learning by Maclaurin Expansion — http://arxiv.org/abs/2406.04896v2
[17] A Tutorial on Meta-Reinforcement Learning — http://arxiv.org/abs/2301.08028v4
[18] Causal-Paced Deep Reinforcement Learning — http://arxiv.org/abs/2507.02910v1
[19] Legged Robots that Keep on Learning: Fine-Tuning Locomotion Policies in the Real World — http://arxiv.org/abs/2110.05457v1
[20] Robot Parkour Learning — http://arxiv.org/abs/2309.05665v2
[21] Proceedings of the Dialogue Robot Competition 2023 — http://arxiv.org/abs/2312.14430v5
[22] Learning Locomotion For Legged Robots Based on Reinforcement Learning: A Survey — https://doi.org/10.1109/ceect50755.2020.9298680
[23] RMA: Rapid Motor Adaptation for Legged Robots — http://arxiv.org/abs/2107.04034v1
[24] Bracing for Impact: Robust Humanoid Push Recovery and Locomotion with Reduced Order Models — http://arxiv.org/abs/2505.11495v2
[25] Hierarchical Reduced-Order Model Predictive Control for Robust Locomotion on Humanoid Robots — http://arxiv.org/abs/2509.04722v1
[26] Learning Humanoid Locomotion over Challenging Terrain — http://arxiv.org/abs/2410.03654v1
[27] Learning Sim-to-Real Humanoid Locomotion in 15 Minutes — http://arxiv.org/abs/2512.01996v1
[28] The RSNA Abdominal Traumatic Injury CT (RATIC) Dataset — http://arxiv.org/abs/2405.19595v1
[29] NTIRE 2025 Challenge on Short-form UGC Video Quality Assessment and Enhancement: KwaiSR Dataset and Study — http://arxiv.org/abs/2504.15003v1
[30] Bridging the Sim2Real Gap: Vision Encoder Pre-Training for Visuomotor Policy Transfer — http://arxiv.org/abs/2501.16389v2
[31] The Importance and the Limitations of Sim2Real for Robotic Manipulation in Precision Agriculture — http://arxiv.org/abs/2008.03983v1
[32] Fin-Grained: A Fine-Grained Benchmark Dataset and Evaluation Protocol for Llms’ Numerical Reasoning Capabilities in Financial Domain — https://doi.org/10.2139/ssrn.5292853


---

*Generated by research-bot · topic=`embodied-humanoid` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading · model=`deepseek-v4-flash` · sources=32 · duration=184s · 2026-10-02T10:54:00+00:00*
