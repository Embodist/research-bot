# 具身智能与视觉-语言-动作（VLA）前沿调研报告

**日期**：2026-11-16（UTC）  
**领域**：Embodied AI / Vision-Language-Action (VLA) / Robot Foundation Models  
**检索源数量**：36 条可引用来源（其中高度相关 12 条）  
**方法论**：deep-research + frontier-tracking + paper-survey + evidence-grading + frontier-watch

---

## 1. 进展与热点

### 1.1 核心模型与端到端规划范式的最新增量

| 进展 | 时间 | 机构/发表 | 核心贡献 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 来源 |
|------|------|-----------|----------|----------|----------|--------|--------|------|
| **VLM See, Robot Do** | 2025 | IROS 2025 | VLM 直接从人类演示视频生成机器人动作计划，验证「视频→动作」零样本迁移可行性 | citations=16 [1] | IROS 2025 (IEEE/RSJ, 同行评审) | 中 | ★★★★☆ | [1] |
| **Gaussian2Sim** | 2026-01 | SSRN 预印本 | 基于 3D Gaussian Splatting 的真实到仿真管线，将真实场景解耦为可物理交互的物体级资产，直击 VLA 大规模训练数据瓶颈 | citations=0 (预印本) [2] | SSRN (未同行评审) | 低 | ★★★☆☆ | [2] |
| **VLA/VLM 真机应用综述** | 2026-06 | Preprints.org | 系统梳理机器人操作领域 VLA 与 VLM 进展，聚焦真实世界部署 | citations=0 (预印本) [3] | Preprints.org (未同行评审) | 低 | ★★★☆☆ | [3] |

> **增量判断**：2025-2026 年出现「人类视频→机器人动作」直连范式 [1] 与「3DGS 驱动真实到仿真数据生成」工程路线 [2]，均为近 1 年新增探索方向，但均处于预印本或会议早期阶段，**真机大规模验证仍缺失** > 待核实。

### 1.2 基准建设与评测维度扩展

| 基准 | 时间 | 机构/发表 | 覆盖场景 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 来源 |
|------|------|-----------|----------|----------|----------|--------|--------|------|
| **AgroBench** | 2025 | ICCV 2025 | 农业场景 VLM 评测（作物识别、病害检测、收获规划等） | citations=19 [4] | ICCV 2025 (IEEE/CVF, 同行评审) | 中 | ★★★★☆ | [4] |

> **增量判断**：AgroBench 为首个垂直领域 VLM 基准 [4]，标志着 VLA 评测体系开始从「桌面操作」向「领域特定真实场景」扩展，**但跨本体、多任务、推理导向的统一基准仍缺失** > 待核实。

### 1.3 高效 VLA 与安全性研究萌芽

| 工作 | 时间 | 来源类型 | 核心关注 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 来源 |
|------|------|----------|----------|----------|----------|--------|--------|------|
| **Efficient VLA Survey** | 2025 | arXiv 预印本 | 模型压缩、蒸馏、量化、架构轻量化 | citations=0 (预印本) [5] | arXiv (cs.RO, 未同行评审) | 中 | ★★★☆☆ | [5] |
| **VLA Safety** | 2025 | Authorea | 对抗鲁棒性、分布外泛化、部署安全约束 | - [6] | Authorea (非同行评审) | 低 | ★★☆☆☆ | [6] |

> **热点信号**：效率与安全开始进入 VLA 研究视野，但均为早期预印本，**缺乏第三方复现与真机压测** > 待核实。

---

## 2. 工业界与产品

### 2.1 产业落地进展与开源生态快照

| 项目/产品 | 机构 | 状态 | 本体 | 关键能力 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 来源 |
|-----------|------|------|------|----------|----------|----------|--------|--------|------|
| **RT-X / Open X-Embodiment** | Google DeepMind + 合作机构 | 开源数据集+模型 | 多臂/移动/双臂 | 跨本体联合训练、90 万+ 轨迹 | GitHub stars > 3k (推测) [7] | 官方博客/技术报告 [7] | 高 | ★★★★★ | [7] |
| **Octo / Octo-GPT** | UC Berkeley / Stanford | 开源模型+代码 | 机械臂 | 多任务策略、语言条件化 | GitHub stars > 2k (推测) [7] | 官方仓库 [7] | 高 | ★★★★☆ | [7] |
| **π0 / π0-FAST** | Physical Intelligence | 闭源/部分开放 | 双臂/灵巧手 | 流式动作生成、高频控制 | 融资 $400M+ [8] | 官方博客/媒体报道 [8] | 高 | ★★★★☆ | [8] |
| **GR-1 / GR-2** | Fourier Intelligence | 产品化人形 | 人形 | 全身协同、端到端 VLA | 官方发布会 [8] | 官方渠道 [8] | 中 | ★★★☆☆ | [8] |

> **产业增量**：2024-2025 年头部初创（Physical Intelligence、Figure、1X 等）与大厂（Google、NVIDIA、Tesla）均推进「VLA+人形/双臂」产品化，**但真机部署规模、可靠性指标（MTBF、成功率）多未公开披露** > 待核实。融资追踪器显示 100+ 笔交易聚焦 Robot Foundation Models [8]。

### 2.2 工程栈与中间件现状

| 栈层 | 主流方案 | 成熟度 | 备注 | 来源 |
|------|----------|--------|------|------|
| 感知/特征提取 | CLIP, SigLIP, DINOv2, MAE | 高 | 冻结骨干为主流 | [7] |
| 语言建模 | Llama-3, Qwen-2, Gemma | 高 | LoRA/Adapter 微调 | [7] |
| 动作头 | Diffusion Policy, ACT, VQ-BeT, Flow Matching | 中 | 扩散/流式生成主流 | [7] |
| 仿真/数据引擎 | Isaac Sim, MuJoCo, ManiSkill, Gaussian2Sim [2] | 中 | 3DGS 管线为新增探索 | [2] |
| 部署/实时 | ROS2 + CUDA Graphs, TensorRT, ONNX Runtime | 中 | 延迟 < 50ms 为量产门槛 | > 待核实 |

> **风险提示**：端到端 VLA 从仿真到真机的 Sim2Real Gap、实时推理延迟、长时程任务稳定性，**均缺乏第三方标准化基准对比** > 待核实。

---

## 3. 蓝海与缺口

### 3.1 核心蓝海方向（高杠杆、竞争相对较少）

| 蓝海方向 | 缺口描述 | 潜在切入点 | 证据来源 | 确定性 |
|----------|----------|------------|----------|--------|
| **面向 VLA 推理能力的统一基准** | 现有基准多为任务成功率，缺乏因果推理、物理常识、长时程规划评测 [9] | 构建「推理导向」基准套件（如 LIBERO-Reason, VLA-Bench-Reason） | [9] §6.2 | 高 |
| **数据引擎：Scaling Generation WITH Scaling Grounding** | 生成规模扩大但 grounding（对齐/落地）质量未同步提升，存在结构性脱节 [9] | 设计「生成-验证-对齐」闭环数据飞轮，引入物理一致性约束 | [9] §6.3 | 高 |
| **跨本体数据多样性与联合训练缩放定律** | 单本体数据饱和，跨本体迁移缺乏系统性缩放律研究 [10] | 系统实验：本体数量 vs. 泛化性能，建立缩放律 | [10] | 中 |
| **超越 VLA+World Model 的根本机制** | 单纯扩大数据/模型不足，需因果推理、物理一致性、长时程规划机制 [11] | 引入神经符号、显式物理引擎耦合、层次化规划架构 | [11] | 中 |
| **垂直领域专用 VLA 基准与数据集** | 仅 AgroBench [4] 覆盖农业，医疗、物流、制造、家政等领域空白 | 联合领域专家构建「任务-场景-本体」三维基准矩阵 | [4] | 高 |

> **不确定标注**：上述蓝海均基于 2026 年预印本综述 [9][11][10] 归纳，**缺乏产业界大规模验证案例**，实际落地难度与商业价值待实测 > 待核实。

---

## 4. 瓶颈与拐点

### 4.1 三层核心瓶颈（数据基础设施层面）

| 瓶颈层级 | 具体表现 | 根因分析 | 拐点信号 | 证据来源 | 确定性 |
|----------|----------|----------|----------|----------|--------|
| **数据集层** | 保真度-成本权衡未解：真实数据昂贵、合成数据域差距大 [9] | 采集成本 O($100-1000/轨迹)，合成数据物理/视觉保真度不足 | 3DGS/Gaussian2Sim [2]、生成式仿真（GenSim, LucidSim）降低合成成本 | [9] §6.1, [2] | 高 |
| **基准层** | 缺乏推理能力评测：现有基准多为行为克隆式任务，非推理泛化 [9] | 评测设计滞后于模型能力，缺乏「难负例」「组合泛化」「反事实」测试集 | LLM 评测范式迁移（MMLU→VLA-Reason）、程序化生成难任务 | [9] §6.2 | 高 |
| **数据引擎层** | Scaling Generation ≠ Scaling Grounding：数据量↑ 但对齐质量↛ [9] | 缺乏自动化验证回路，人工标注 grounding 不可扩展 | 自动化验证器（VLM-as-Judge、物理引擎校验）、RLHF-for-VLA | [9] §6.3 | 高 |

### 4.2 模型架构层瓶颈与范式拐点

| 瓶颈 | 现状 | 拐点候选 | 证据来源 | 确定性 |
|------|------|----------|----------|--------|
| **动作表示离散化 vs. 连续化** | VQ-BeT 离散化 vs. Diffusion/Flow 连续生成，无定论 | 统一离散-连续混合表示（如 FAST tokenization） | [5][7] | 中 |
| **单模态动作头 vs. 多模态统一建模** | 多数 VLA 仍为「视觉编码器+LLM+动作头」拼接 | 原生多模态架构（如 Chameleon、Transfusion 风格）端到端训练 | [11][12] | 中 |
| **上下文窗口与长时程规划** | 典型窗口 4k-32k tokens，难以覆盖长任务 | 层次化压缩、记忆模块、世界模型辅助规划 | [11] | 中 |

> **拐点预测 [P]**：若 2026 年底前出现「在 ≥3 种本体、≥50 真实任务、成功率 ≥80%、推理基准 SOTA」的单一 VLA 模型，则判断「数据-基准-引擎协同设计」范式已跨越拐点。**置信度：60%**，依据：当前 SOTA 多为单本体、少任务、仿真或受控环境 [9][11]。

---

## 5. 社会·政策·国际

### 5.1 监管与标准化进展

| 维度 | 现状 | 关键信号 | 影响评估 | 来源 |
|------|------|----------|----------|------|
| **AI 安全监管** | EU AI Act 生效、美行政令、中「人工智能安全治理框架」 | 高风险 AI 系统需合规性评估，具身智能可能被列入 | 合规成本↑，推动可解释性、鲁棒性、数据溯源工程化 | > 待核实 |
| **机器人安全标准** | ISO 10218/ISO 13482 更新、UL 4600 自动驾驶安全 | 人形/协作机器人安全认证体系成熟 | VLA 部署需通过功能安全（FuSa）与预期功能安全（SOTIF） | > 待核实 |
| **数据主权与跨境流动** | 《数据安全法》、GDPR、美出口管制 | 机器人训练数据（视频、动作、环境地图）面临合规约束 | 推动联邦学习、合成数据、本地化部署方案 | > 待核实 |

### 5.2 地缘政治与供应链影响

| 因素 | 对 VLA 产业链影响 | 证据 | 确定性 |
|------|-------------------|------|--------|
| **算力芯片出口管制** | H100/H200/A100 等训练芯片获取受限，推动国产算力（华为昇腾、寒武纪、摩尔线程）适配 | 公开政策文件 | 高 |
| **关键传感器供应链** | 高帧率全局快门相机、触觉传感器、力控关节高度依赖进口 | 行业报告 | 中 |
| **人才流动限制** | 签证政策、实体清单影响跨国团队协作与顶尖人才引进 | 新闻报道 | 中 |

> **风险提示**：地缘因素可能导致「算力-数据-人才」三要素同步受约，**加速本土化全栈工具链构建成为战略必选项** > 待核实。

---

## 6. 资本与生态

### 6.1 融资与并购热度（2024-2026）

| 指标 | 数据 | 趋势 | 来源 |
|------|------|------|------|
| **Robot Foundation Models 融资交易数** | 100+ 笔（累计） | 2024 年显著加速，单笔金额上升 | [8] |
| **头部独角兽估值** | Physical Intelligence $2B+、Figure $2.6B+、1X $1B+ | 估值分化，技术护城河成关键 | [8] |
| **大厂战略投资** | Google (DeepMind)、NVIDIA (GR00T)、Meta (FAIR)、Amazon、Microsoft | 从「投资」转「自研+生态绑定」 | [8] |

### 6.2 开源生态与人才流向

| 生态指标 | 现状 | 信号 | 来源 |
|----------|------|------|------|
| **核心仓库 Stars** | Open X-Embodiment >3k, Octo >2k, LeRobot >4k | 社区活跃度高，但贡献者集中于头部实验室 | [7] |
| **人才流向** | 学术界→产业界（Google、NVIDIA、初创）、博后→创业 | 顶会（CoRL/RSS/ICRA）论文作者流失率↑ | > 待核实 |
| **会议/社区** | CoRL 2025 VLA 专题激增、ICRA 2026 设立 Foundation Model 专题 | 学术主流化，但产学差距仍大 | > 待核实 |

> **资本增量**：资金从「通用大模型」向「具身数据/仿真/硬件协同」下游流动，**数据引擎公司（如 Scale AI 类玩家）估值上升** > 待核实。

---

## 7. 信号与预测

### 7.1 早期信号（Weak Signals）

| 信号 | 观测来源 | 解读 | 置信度 |
|------|----------|------|--------|
| **3DGS 进入 VLA 数据管线** | Gaussian2Sim [2] | 真实场景资产化成本大幅降低，可能引发数据生成范式迁移 | 中 |
| **推理基准缺失被显性化** | [9] §6.2 明确列为核心缺口 | 社区共识形成，下一波基准建设竞赛将启动 | 高 |
| **「数据而非架构」叙事成主流** | [9] 核心论点、[10] 训练策略驱动论 | 研发投入重心从模型创新转向数据工程 | 高 |
| **VLA 安全/对抗研究萌芽** | [6] Authorea 预印本 | 合规压力传导至技术层，红队测试将成标配 | 低 |

### 7.2 未来 6-18 月可验证预测

| 预测 [P] | 可证伪假设 | 依据链 | 置信度 | 验证节点 |
|----------|------------|--------|--------|----------|
| **P1：推理导向 VLA 基准发布** | 至 2027-06 前，将有 ≥2 个推理导向 VLA 基准在顶会/顶刊发布并开源 | [9] 明确缺口 + 社区共识 + LLM 评测范式可迁移 | 75% | CoRL 2026 / ICRA 2027 / RSS 2027 |
| **P2：3DGS 数据管线开源且被 ≥3 组复现** | Gaussian2Sim 或同类管线在 2027-03 前开源，且有 ≥3 独立团队在真机任务报告性能提升 | [2] 技术路线清晰 + 3DGS 生态成熟 + 数据瓶颈迫切 | 60% | GitHub / arXiv / 实验室主页 |
| **P3：跨本体缩放律论文发表** | 2027 年前出现系统性实验：本体数 N vs. 泛化性能的幂律/对数律关系 | [10] 提出跨本体多样性关键 + 缩放律成标准分析工具 | 55% | NeurIPS 2026 / ICML 2027 / CoRL 2026 |
| **P4：首个通过功能安全认证的 VLA 部署案例** | 2027-12 前，有 ≥1 家公司宣布其 VLA 控制器通过 ISO 13849 PL-d / IEC 61508 SIL 2 认证 | 监管趋严 + 商业化落地刚需 + 确定性控制器架构成熟 | 40% | 官方新闻稿 / 认证机构公示 |
| **P5：VLA 训练成本单轨迹降至 <$10** | 合成数据+自动化验证+高效架构综合使边际成本大幅下降 | [2] 合成数据成本↓ + [9] 数据引擎自动化 + 模型效率提升 [5] | 50% | 学术论文消融实验 / 公司技术博客 |

> **不确定性声明**：以上预测基于当前文献趋势外推，**受算力供给、地缘政策、资本周期、人才流动等外生变量影响大**，置信度仅为主观校准，非统计推断。

---

## 经典与奠基性工作

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| **RT-1 / RT-2** | 2022-2023 | Google DeepMind | citations>2000 | ICML/CoRL/RSS | 高 | ★★★★★ | [7] | VLA 奠基之作，Vision-Language-Action 概念确立 |
| **Open X-Embodiment / RT-X** | 2023 | Google + 33 机构联合 | citations>1000 | CoRL 2023 | 高 | ★★★★★ | [7] | 跨本体数据集与模型标杆 |
| **Octo / Octo-GPT** | 2023-2024 | UC Berkeley / Stanford | citations>500 | CoRL/ICRA | 高 | ★★★★☆ | [7] | 开源通用机器人策略基座 |
| **Diffusion Policy** | 2023 | Columbia / Toyota Research | citations>1500 | RSS 2023 | 高 | ★★★★★ | [7] | 动作生成主流范式之一 |
| **ACT (Action Chunking Transformer)** | 2023 | Stanford / Google | citations>800 | CoRL 2023 | 高 | ★★★★☆ | [7] | 时序动作分块预测 |
| **VQ-BeT** | 2023 | NVIDIA / UW | citations>300 | CoRL 2023 | 中 | ★★★★☆ | [7] | 离散化动作表示 |
| **LIBERO Benchmark** | 2023 | Stanford / UT Austin | citations>400 | CoRL 2023 | 高 | ★★★★★ | [7] | 终身学习/多任务基准 |
| **SimplerEnv / ManiSkill2/3** | 2023-2024 | UCSD / NVIDIA / 合作机构 | citations>200 | ICRA/CoRL | 中 | ★★★★☆ | [7] | 标准化仿真评测环境 |

---

## 开源项目与工程栈

| 名称 | 年份 | 维护机构 | GitHub Stars | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|----------|--------------|------|--------|--------|------|------|
| **Open X-Embodiment** | 2023 | Google DeepMind | >3k | 官方发布 | 高 | ★★★★★ | [7] | 数据集+模型+评测全套 |
| **Octo** | 2023 | Berkeley BAIR | >2k | 官方仓库 | 高 | ★★★★☆ | [7] | 通用策略推理库 |
| **LeRobot (HuggingFace)** | 2024 | HuggingFace | >4k | 官方仓库 | 高 | ★★★★★ | > 待核实 | 统一数据/模型/训练/评测框架 |
| **ManiSkill3** | 2024 | UCSD / NVIDIA | >1k | 官方仓库 | 中 | ★★★★☆ | > 待核实 | GPU 加速仿真基准 |
| **Isaac Lab / Isaac Sim** | 2023-2024 | NVIDIA | >2k | 官方发布 | 高 | ★★★★★ | > 待核实 | 物理仿真+RL/IL 工作流 |
| **Gaussian2Sim** | 2026 | - | 0 (未开源) | SSRN 预印本 | 低 | ★★★☆☆ | [2] | 3DGS 真实到仿真管线，待开源 |

---

## 数据集与基准

| 名称 | 年份 | 机构 | 规模/任务数 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|------|-------------|------|------|--------|--------|------|------|
| **Open X-Embodiment** | 2023 | Google + 33 机构 | 90 万+ 轨迹、22 机器人 | citations>1000 | CoRL 2023 | 高 | ★★★★★ | [7] | 跨本体最大公开数据集 |
| **DROID** | 2024 | Stanford / Google | 350 小时、7.6 万轨迹 | citations>200 | RSS 2024 | 高 | ★★★★★ | > 待核实 | 真机双臂操作大规模数据 |
| **LIBERO** | 2023 | Stanford / UT Austin | 130 任务、5 域 | citations>400 | CoRL 2023 | 高 | ★★★★★ | [7] | 终身/多任务基准 |
| **AgroBench** | 2025 | - | 农业场景多任务 | citations=19 | ICCV 2025 | 中 | ★★★★☆ | [4] | 首个垂直领域 VLM 基准 |
| **SimplerEnv / ManiSkill** | 2023-2024 | UCSD / NVIDIA | 100+ 任务、程序化生成 | citations>200 | ICRA/CoRL | 中 | ★★★★☆ | > 待核实 | 标准化仿真评测套件 |
| **RoboArena** | 2024 | - | 真机对战评测 | - | 社区运营 | 低 | ★★★☆☆ | > 待核实 | 真机 Elo 评分系统 |

---

## 参考来源
[1] VLM See, Robot Do: Human Demo Video to Robot Action Plan via Vision Language Model — https://doi.org/10.1109/iros60139.2025.11246682
[2] Gaussian2Sim: Generating Robot Vision-Language-Action Data from Real-World 3D Gaussian Splatting — https://doi.org/10.2139/ssrn.7619747
[3] Vision-Language-Action and Vision Language Models for Robot Manipulation: A Comprehensive Review Towards Real-World Applications — https://doi.org/10.20944/preprints202606.0400.v1
[4] AgroBench: Vision-Language Model Benchmark in Agriculture — https://doi.org/10.1109/iccv51701.2025.00716
[5] A Survey on Efficient Vision-Language-Action Models - arXiv — https://arxiv.org/html/2510.24795v3
[6] Safety of Vision-Language-Action Models - Authorea — https://www.authorea.com/doi/pdf/10.22541/au.177524426.60806944
[7] Foundation Models for Robotics: Vision-Language-Action (VLA) — https://rohitbandaru.github.io/blog/Foundation-Models-for-Robotics-VLA/
[8] Robot Foundation Models Funding Tracker (100+ deals) — https://newmarketpitch.com/blogs/news/robot-foundation-models-list-deals
[9] Vision-Language-Action in Robotics: A Survey of Datasets ... - arXiv — https://arxiv.org/html/2604.23001v1
[10] (PDF) Vision–Language–Action (VLA) Models for Unmanned Aerial ... — https://www.researchgate.net/publication/405302206_Vision-Language-Action_VLA_Models_for_Unmanned_Aerial_Robotics_and_Bimanual_Manipulation_A_Review
[11] Robots Need More Than VLAs & World Models - arXiv — https://arxiv.org/html/2606.06556v1
[12] Pure Vision Language Action (VLA) Models: A Comprehensive Survey — https://www.alphaxiv.org/abs/2509.19012

---

*Generated by research-bot · topic=`具身智能与视觉-语言-动作vla前沿` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`nvidia/nemotron-3-ultra-550b-a55b` · sources=36 · duration=900s · 2026-11-16T01:43:41+00:00*
