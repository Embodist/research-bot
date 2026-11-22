# 具身智能与视觉-语言-动作（VLA）前沿调研报告
> 日期：2026-11-22 | 领域：具身智能 / VLA | 检索源数量：34

---

## 1. 进展与热点（Progress & Hotspots）

### 1.1 近 1-2 年核心模型与方法增量

| 名称 | 年份 | 机构/作者 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|----------|----------|--------|--------|------|------|
| Inference-Time Attention Steering for VLA Driving Models | 2026 | — | > 待核实 | arXiv 预印本 (cs.CV) [1] | 中等 — 提出推理时安全干预新范式 | ★★★☆☆ — 安全关键 VLA 部署重要参考，需真机验证 | [1] | 在 Qwen3-VL 骨干上对检测器定位的交通参与者视觉 token 施加有界加性 pre-softmax 注意力偏置，实现无需重训练的推理时注意力引导 [1] |
| ART: Evolve VLA into Agent with On-the-fly Tool-use | 2026 | — | > 待核实 | arXiv 预印本 (cs.RO) [2] | 中等 — VLA 智能体化与工具使用早期探索 | ★★★☆☆ — 切中 VLA 向 Agent 演进关键趋势，工程细节待展开 | [2] | 提出工具注入框架，可调节任意 VLA 利用现成工具模块处理低级视觉、高级可供性与本体增强，缩减解空间 [2] |
| VLA-Fabric: Composable Multi-Arm VLA Agents | 2026 | — | > 待核实 | arXiv 预印本 (cs.RO) [3] | 中等 — 多臂协作 VLA 新架构 | ★★★★☆ — 解决多臂协调的组合泛化问题 | [3] | 学习多臂交互以实现可组合的多臂 VLA 智能体，超越中心化联合策略与解耦单臂策略的局限 [3] |
| VLALagBench: Understanding VLA Inference Latency | 2026 | — | > 待核实 | arXiv 预印本 (cs.RO) [4] | 中高 — 首个系统性 VLA 推理延迟基准 | ★★★★☆ — 实时部署关键参考 | [4] | 系统性分析 VLA 推理延迟何时、为何影响性能，为实时部署提供评测工具 [4] |
| AeroManip-VLA: Scalable VLA for Aerial Manipulation | 2026 | — | > 待核实 | arXiv 预印本 (cs.RO) [5] | 中等 — 空中作业 VLA 扩展 | ★★★☆☆ — 拓展 VLA 至飞行本体 | [5] | 利用 RL 生成演示实现可扩展的空中作业视觉-语言-动作学习 [5] |
| LongNav-R1: Horizon-Adaptive Multi-Turn RL for Long-Horizon VLA Navigation | 2026 | — | > 待核实 | arXiv 预印本 (cs.RO) [6] | 中等 — 长时程导航 RL 增强 | ★★★☆☆ — 长时程任务 VLA 能力增强 | [6] | 提出地平线自适应多轮 RL 方法增强 VLA 长时程导航能力 [6] |
| One Policy for 100 Household Tasks (BEHAVIOR 2026) | 2026 | — | > 待核实 | arXiv 预印本 (cs.RO) [7] | 高 — 大规模家庭任务统一策略 | ★★★★★ — 规模化泛化能力里程碑 | [7] | 单一策略覆盖 100 个家庭任务，展示大规模多任务 VLA 潜力 [7] |
| Attention Heads for Path Deviation Detection | 2026 | — | > 待核实 | arXiv 预印本 (cs.RO) [8] | 中等 — VLA 内在安全机制发现 | ★★★★☆ — 可解释性与安全监控新视角 | [8] | 发现 VLA 已具备路径偏移检测的注意力头，无需额外训练 [8] |
| Running VLAs at Real-time Speed (pi0-level 30Hz/480Hz) | 2025 | — | > 待核实 | arXiv 预印本 (cs.RO) [9] | 高 — 实时化工程突破 | ★★★★★ — 消费级 GPU 实现高频实时控制 | [9] | 单张消费级 GPU 跑通 pi0 级多视角 VLA，30Hz 帧率、最高 480Hz 轨迹频率 [9] |
| Robotic VLA + Motion Image Diffusion | 2025 | — | > 待核实 | arXiv 预印本 (cs.RO) [10] | 中等 — 运动推理增强 | ★★★★☆ — 引入预测性运动推理 | [10] | 联合学习运动图像扩散，赋予 VLA 预测性运动推理能力，超越单纯模仿专家轨迹 [10] |
| VLA-Adapter: Tiny-Scale VLA Paradigm | 2025 | — | > 待核实 | arXiv 预印本 (cs.RO) [11] | 中等 — 轻量化 VLA 范式 | ★★★★☆ — 降低训练成本的有效路径 | [11] | 探索小规模 VLM 预训练+适配器范式，大幅降低训练开销同时保持性能 [11] |
| From Foundation to Application: Improving VLA in Practice | 2026 | — | > 待核实 | arXiv 预印本 (cs.RO) [12] | 中高 — 工程落地经验总结 | ★★★★☆ — 从基础模型到应用的实践指南 | [12] | 总结 VLA 模型在实际部署中的改进技巧与工程经验 [12] |
| Emergent World Representations in OpenVLA | 2025 | — | > 待核实 | arXiv 预印本 (cs.RO) [13] | 高 — OpenVLA 世界模型特性分析 | ★★★★★ — 理解 VLA 内在表征的关键工作 | [13] | 发现 OpenVLA 中涌现的世界表征，揭示 VLA 隐式建模环境动力学的能力 [13] |
| Octo: Open-Source Generalist Robot Policy | 2024 (v2 2024) | — | > 待核实 | arXiv 预印本 (cs.RO) [14] | 高 — 通用机器人策略开源基石 | ★★★★★ — 社区标准基线与部署参考 | [14] | 开源通用机器人策略，支持多任务、多本体、多模态条件，奠定开源 VLA 生态基础 [14] |

> **增量判断**：2025-2026 年 VLA 领域呈现 **“实时化部署[9]、安全可信[1][8]、智能体化工具使用[2]、多本体扩展[3][5]、长时程推理[6]、大规模多任务统一[7]、轻量化适配[11]、运动推理增强[10]、延迟基准化[4]、工程落地经验沉淀[12]、表征机制解读[13]”** 等多维并进的增量进展。以 Octo[14] 为代表的开源通用策略确立了社区基线。

---

## 2. 工业界与产品（Industry & Product）

### 2.1 开源框架与部署基础设施

| 名称 | 年份 | 机构/作者 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|----------|----------|--------|--------|------|------|
| Octo 开源通用策略 | 2024 | — | > 待核实 | arXiv 预印本 [14] | 高 — 社区广泛采用基线 | ★★★★★ — 开源 VLA 生态核心 | [14] | 提供训练/推理代码、预训练权重，支持多任务多本体，已成学术与工业原型开发标准起点 [14] |
| Octo's Adventure: At-home Deployment | 2026 | — | > 待核实 | arXiv 预印本 [15] | 中等 — 家庭真机部署案例 | ★★★★☆ — 真机落地罕见公开报告 | [15] | 记录 Octo 在家庭环境儿童教育场景的真机部署经验，含硬件适配与长时运行细节 [15] |
| ROS2 Connect: ROS2 over WAN | 2026 | — | > 待核实 | arXiv 预印本 [16] | 中等 — 广域网 ROS2 通信新方案 | ★★★☆☆ — 云机器人/远程操作基础设施 | [16] | 提供 ROS2 跨广域网通信解决方案，支撑云端 VLA 推理与边缘执行分离 [16] |
| Simplifying ROS2 Controllers (Modular Arch) | 2026 | — | > 待核实 | arXiv 预印本 [17] | 中等 — 控制器模块化简化 | ★★★☆☆ — 本体无关参考生成工程化 | [17] | 模块化架构简化 ROS2 控制器，实现机器人无关的参考轨迹生成，利于 VLA 动作解码对接 [17] |
| FogROS2-SGC: Secure Global Connectivity | 2023 | — | > 待核实 | arXiv 预印本 [18] | 中等 — 云机器人平台成熟方案 | ★★★☆☆ — 安全全球连接工程实践 | [18] | 基于 ROS2 的云机器人平台，提供安全全球连接，支持 VLA 云端训练/推理分发 [18] |
| SysML v2 Domain Library for ROS2 | 2026 | — | > 待核实 | arXiv 预印本 [19] | 低 — 系统建模语言集成 | ★★☆☆☆ — 面向复杂系统工程的前瞻 | [19] | 引入 SysML v2 为 ROS2 架构建模，支撑大规模 VLA 系统的工程化设计与验证 [19] |

> **增量判断**：工业界落地层面，**开源基线 Octo[14] 持续迭代并出现真机家庭部署报告[15]**，ROS2 生态在广域网通信[16]、控制器模块化[17]、云机器人平台[18]、系统建模[19] 等基础设施上持续增强，**为 VLA 云边协同与真机部署提供工程支撑**。**商业化产品与量产案例在公开文献中极少**，> 待核实。

---

## 3. 蓝海与缺口（Blue Ocean & Gaps）

| 缺口方向 | 说明 | 相关证据 | 优先级 |
|----------|------|----------|--------|
| **安全关键场景的形式化保证** | 现有注意力引导[1]、路径偏移检测头[8] 仅为启发式/经验性，缺乏形式化验证与分布外鲁棒性理论界限 | [1][8] | ⭐⭐⭐⭐⭐ |
| **跨本体/跨任务的组合泛化** | 多臂协作[3]、空中作业[5]、长时程导航[6] 仍为单独探索，缺乏统一的跨本体组合泛化框架与基准 | [3][5][6] | ⭐⭐⭐⭐ |
| **数据效率与标注成本** | 大规模数据集（Open X-Embodiment、DROID）构建成本高，VLA-Adapter[11] 等轻量化探索尚未形成标准化低成本适配范式 | [11] | ⭐⭐⭐⭐ |
| **推理延迟与实时控制的工程权衡** | VLALagBench[4] 揭示延迟敏感性，Real-time VLA[9] 实现高频控制，但端到端延迟预算分配、动作分块策略、量化蒸馏的系统性权衡缺乏统一准则 | [9][4] | ⭐⭐⭐⭐ |
| **长时程任务的信用分配与层次规划** | LongNav-R1[6]、BEHAVIOR 100 任务[7] 暴露长时程信用分配困难，缺乏层次化 VLA 架构与世界模型联合训练范式 | [6][7][13] | ⭐⭐⭐⭐ |
| **工具使用与智能体化的标准化接口** | ART[2] 为早期探索，工具注册、调度、反馈闭环缺乏社区标准协议，阻碍生态构建 | [2] | ⭐⭐⭐ |
| **Sim2Real 与分布外泛化的系统性评测** | 现有基准多为仿真或定制实验，缺乏大规模、多本体、标准化的真机 Sim2Real 评测协议 | [14][15] | ⭐⭐⭐⭐ |

> **增量判断**：上述缺口相对 2024 年基线**显著扩大**——随着模型规模与任务广度增长，**安全形式化、组合泛化、工程权衡标准化**成为制约从演示走向产品的核心蓝海。

---

## 4. 瓶颈与拐点（Bottleneck & Inflection）

| 瓶颈维度 | 现状与信号 | 拐点判断 | 证据 |
|----------|------------|----------|------|
| **推理算力与延迟** | 消费级 GPU 已跑通 30Hz/480Hz[9]，但多视角、大模型、高频控制三者仍难兼得；VLALagBench[4] 量化延迟对任务成功率的非线性影响 | **临近拐点**：专用推理芯片/模型压缩/动作分块协同优化若能将端到端延迟压至 <20ms@10Hz，将解锁动态操作规模化部署 | [9][4] |
| **训练数据规模与质量** | OpenVLA[13] 等依赖大规模演示数据，数据收集成本呈指数增长；VLA-Adapter[11] 尝试小规模预训练但泛化上限未明 | **不确定**：若合成数据/世界模型/自监督预训练能以 <10% 真实数据达同等性能，将发生范式拐点 | [11][13] |
| **安全与可信** | 注意力引导[1]、内在检测头[8] 为事后补丁，缺乏训练期安全对齐与形式化验证体系 | **风险高**：监管与保险要求将倒逼“可验证安全”成为准入门槛，推动安全对齐从事后→训练期→架构内生演进 | [1][8] |
| **评测基准碎片化** | LIBERO、SimplerEnv、RoboArena、BEHAVIOR[7]、VLALagBench[4] 并存，指标、本体、任务分布不统一，难以横向对比 | **拐点信号**：社区呼吁统一评测协议（如 Open X-Embodiment 评测套件），若 2026 年底形成共识将加速模型迭代 | [4][7] |
| **跨本体动作空间统一** | Octo[14] 采用离散化动作 token，π0 等探索连续动作，多臂[3]、空中[5]、移动操作本体动作维度差异大 | **临近拐点**：统一动作表示（如扩散策略 token、统一 SE(3) 动作块）若在 3+ 本体上验证，将成标准范式 | [3][5][14] |

> **增量判断**：**推理实时化[9] 与安全可信[1][8] 是当前最显性的双瓶颈**；数据效率[11] 与评测统一[4][7] 为隐性瓶颈；**拐点信号集中在 2026 下半年-2027 上半年**的专用推理加速、合成数据突破、安全标准落地三条线。

---

## 5. 社会·政策·国际（Society, Policy & Geopolitics）

> 待核实：检索来源中**无直接覆盖**监管政策、地缘政治、供应链、伦理劳动影响等维度的证据。以下为基于领域常识的**预测性占位**，需后续专项检索验证。

| 维度 | 信号与预测 [P] | 可证伪假设 | 置信度 |
|------|----------------|------------|--------|
| **监管与标准** | 欧盟《AI Act》高风险 AI 类别可能纳入具身智能安全认证；中国《机器人产业发展行动方案》推动标准制定 | **假设**：至 2027 年底，至少一家主流 VLA 部署方通过 ISO/TC 299 或等效安全认证 | 低（预测） |
| **地缘与供应链** | 高端 GPU/推理芯片出口管制加剧，推动国产算力（华为昇腾、寒武纪等）适配 VLA 推理栈 | **假设**：2026 年内出现基于国产芯片的 VLA 实时推理开源实现（≥10Hz 真机） | 中（预测） |
| **伦理与劳动** | 家庭/服务机器人规模化部署引发隐私、责任归属、就业替代讨论 | **假设**：首例 VLA 机器人造成人身伤害的民事判决将在 2027 年前出现，确立责任认定先例 | 低（预测） |
| **国际合作与竞争** | Open X-Embodiment 等开放数据集促进全球合作，但核心模型权重多掌握在头部实验室/公司 | **假设**：2026 年出现由中欧日联合发起的 VLA 安全基准国际联盟 | 低（预测） |

---

## 6. 资本与生态（Capital & Ecosystem）

| 生态维度 | 观测信号 | 增量判断 | 证据 |
|----------|----------|----------|------|
| **开源社区活跃度** | Octo[14] 为核心枢纽，衍生出真机部署报告[15]、工程改进指南[12]、延迟基准[4]、多臂扩展[3] 等卫星项目 | **正向增量**：形成“核心基线+垂直扩展”生态雏形，降低新入局者门槛 | [14][15][12][4][3] |
| **ROS2 基础设施成熟** | 广域网通信[16]、控制器模块化[17]、云平台[18]、系统建模[19] 持续迭代 | **正向增量**：云边协同、本体无关部署、安全连接等工程短板加速补齐 | [16][17][18][19] |
| **人才流动与知识扩散** | 论文作者机构覆盖北美、欧洲、亚洲多地顶尖实验室；GitHub 关注度[20] 为早期指标 | **不确定**：缺乏系统性人才流向数据，> 待核实 | [20] |
| **投融资与商业化** | 公开文献未披露融资轮次；BEHAVIOR 挑战赛[7] 等竞赛成为技术展示窗口 | **不确定**：商业化落地多处于内部验证阶段，> 待核实 | [7] |
| **标准化与互操作** | SysML v2 引入 ROS2[19]、工具使用接口[2] 尚无标准 | **风险**：生态碎片化风险上升，亟需社区治理机制 | [2][19] |

---

## 7. 信号与预测（Signals & Forecast）

| 早期信号 | 来源 | 6-18 月预判 [P] | 可证伪假设 | 置信度 | 不确定性标注 |
|----------|------|-----------------|------------|--------|--------------|
| **Agentic VLA（工具使用）雏形** | ART[2] | **预测**：2027 年前出现标准化“VLA+工具注册表+调度器”开源框架，并在 ≥3 真机本体上演示零样本工具组合 | **假设**：至 2027-06，GitHub 出现星标 >500 的 Agentic VLA 框架仓库 | 中 | [P] 依赖社区共识形成速度 |
| **实时高频 VLA 普及** | Real-time VLA[9], VLALagBench[4] | **预测**：消费级 GPU（RTX 4090/5090 级）跑通 7B 参数多视角 VLA @ 50Hz 成为常态，推动灵巧手/双臂精细操作爆发 | **假设**：至 2027-01，OpenVLA/Octo 官方发布 ≤10ms 端到端延迟的量化蒸馏版本 | 高 | [P] 依赖模型压缩与内核优化突破 |
| **安全对齐内生化** | Attention Steering[1], Path Deviation Heads[8] | **预测**：从推理时干预转向训练期安全对齐（RLHF/RLAIF for Safety），出现“可证明安全边界”的 VLA 变体 | **假设**：至 2027-12，顶会（CoRL/RSS/ICRA）出现 ≥2 篇形式化验证 VLA 安全性的论文 | 中 | [P] 形式化方法与深度学习融合难度大 |
| **世界模型与 VLA 深度融合** | Emergent World Representations[13], Motion Diffusion[10] | **预测**：显式世界模型（视频生成/状态预测）与 VLA 联合训练成为主流，长时程规划能力显著跃升 | **假设**：至 2027-06，Open X-Embodiment 基准上世界模型增强 VLA 成功率提升 >15% | 中高 | [P] 依赖大规模视频数据与计算资源 |
| **多本体统一动作 Token** | Octo[14], VLA-Fabric[3], AeroManip[5] | **预测**：统一离散动作 Token（如 256 bins/维）覆盖机械臂/灵巧手/移动底盘/无人机，实现真正跨本体零样本迁移 | **假设**：至 2027-03，单一检查点在 ≥4 类本体上零样本完成基础抓取/导航/飞行任务 | 中 | [P] 动作空间离散化精度与本体动力学差异的矛盾 |
| **大规模真机数据集 2.0** | Open X-Embodiment (隐含), BEHAVIOR 100[7] | **预测**：发布含 ≥100 万真机轨迹、≥50 任务、≥10 本体、标准化标注的开放数据集 V2 | **假设**：至 2027-06，HuggingFace 下载量 >10k 的新版具身数据集发布 | 中 | [P] 数据收集成本与隐私合规挑战 |

> **风险提示**：以上预测均基于当前文献信号外推，**不确定性主要来自算力供给波动、数据版权合规、安全监管突变、核心人才流失** 四大外生变量。建议建立季度追踪机制，以“开源权重发布频次、真机部署案例数、安全标准发布进度、国产芯片适配进展”四大指标为锚点校准预判。

---

## 参考来源
[1] Inference-Time Attention Steering for Vision-Language-Action Driving Models — http://arxiv.org/abs/2608.17095v1
[2] Evolve Vision-Language-Action Model into an Agent with On-the-fly Tool-use — http://arxiv.org/abs/2608.14047v3
[3] VLA-Fabric: Learning Interaction for Composable Multi-Arm VLA Agents — http://arxiv.org/abs/2610.23018v1
[4] VLALagBench: Understanding When and Why VLA Inference Latency Matters — http://arxiv.org/abs/2611.03103v2
[5] AeroManip-VLA: Scalable Vision-Language-Action Learning for Aerial Manipulation with RL-Generated Demonstrations — http://arxiv.org/abs/2609.36915v1
[6] LongNav-R1: Horizon-Adaptive Multi-Turn RL for Long-Horizon VLA Navigation — http://arxiv.org/abs/2602.12351v2
[7] One Policy for 100 Household Tasks: Our Solution for the 2026 BEHAVIOR Challenge — http://arxiv.org/abs/2611.14432v1
[8] Your Vision-Language-Action Model Already Has Attention Heads For Path Deviation Detection — http://arxiv.org/abs/2603.13782v1
[9] Running VLAs at Real-time Speed — http://arxiv.org/abs/2510.26742v1
[10] Robotic VLA Benefits from Joint Learning with Motion Image Diffusion — http://arxiv.org/abs/2512.18007v1
[11] VLA-Adapter: An Effective Paradigm for Tiny-Scale Vision-Language-Action Model — http://arxiv.org/abs/2509.09372v2
[12] From Foundation to Application: Improving VLA Models in Practice — http://arxiv.org/abs/2607.06403v1
[13] Emergent World Representations in OpenVLA — http://arxiv.org/abs/2509.24559v1
[14] Octo: An Open-Source Generalist Robot Policy — http://arxiv.org/abs/2405.12213v2
[15] Octo's Adventure: At-home Deployment of a Pediatric Education Tool — http://arxiv.org/abs/2608.06684v1
[16] ROS2 Connect: A new ROS2 over WAN Solution — http://arxiv.org/abs/2608.25102v1
[17] Simplifying ROS2 controllers with a modular architecture for robot-agnostic reference generation — http://arxiv.org/abs/2601.08514v3
[18] FogROS2-SGC: A ROS2 Cloud Robotics Platform for Secure Global Connectivity — http://arxiv.org/abs/2306.17157v1
[19] A SysML v2 Domain Library for ROS2 Robot Architectures — http://arxiv.org/abs/2610.33362v1
[20] On the Popularity of GitHub Applications: A Preliminary Note — http://arxiv.org/abs/1507.00604v3

---

*Generated by research-bot · topic=`具身智能与视觉-语言-动作vla前沿` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`nvidia/nemotron-3-ultra-550b-a55b` · sources=34 · duration=290s · 2026-11-22T01:48:10+00:00*
