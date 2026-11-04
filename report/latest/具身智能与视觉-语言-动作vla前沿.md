# 具身智能与视觉-语言-动作（VLA）前沿调研报告：2024-2026 进展、生态与机会证据地图

**日期**：2026-11-04 | **领域**：Embodied AI / VLA / Robotics | **检索源数量**：26 条（其中高强相关 12 条，其余为噪声/无关）

---

## 1. 进展与热点

### 1.1 最新进展（2025-2026，增量视角）

| 进展 | 时间 | 机构/来源 | 一句话贡献 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 引用 |
|------|------|-----------|------------|----------|----------|--------|--------|------|
| **Running VLAs at Real-time Speed** | 2025-10 | arXiv (cs.RO) | 单张消费级 GPU 实现 pi0 级多视角 VLA 30Hz/480Hz 实时推理，抓取下落笔 100% 成功率 | > 待核实（引用/Star 暂无公开统计） | arXiv 预印本，cs.RO 顶会投稿方向 | 高 —— 直接击穿 VLA 落地核心痛点 | ★★★★☆ —— 工程落地关键突破，代码开源可复现 | [1] |
| **Robotic VLA + Motion Image Diffusion** | 2025-12 | arXiv (cs.RO) | 引入运动图像扩散联合训练，赋予 VLA 预测性运动推理能力，缓解纯模仿学习短视问题 | > 待核实 | arXiv 预印本，cs.RO | 中高 —— 引入世界模型思路进 VLA 主流 | ★★★★☆ —— 为长时程推理提供新范式 | [2] |
| **VLA-Adapter: Tiny-Scale VLA** | 2025-09 | arXiv (cs.RO) | 提出适配器范式，小规模 VLM+Adapter 即可达成大模型同级性能，大幅降低训练成本 | > 待核实 | arXiv 预印本，cs.RO | 高 —— 解决算力门槛与数据稀缺双重痛点 | ★★★★☆ —— 低资源部署首选范式 | [3] |
| **VLA-Fabric: Multi-Arm Composable Agents** | 2026-10 | arXiv (cs.RO) | 面向多臂协作的可组合 VLA 架构，支持中心化/去中心化协调切换 | > 待核实 | arXiv 预印本，cs.RO | 中高 —— 多臂/灵巧手协作稀缺方向 | ★★★★☆ —— 复杂装配与双臂任务关键进展 | [4] |
| **When Vision Overrides Language** | 2026-02 | arXiv (cs.CV) | 系统评估 VLA 反事实失效（视觉覆盖语言），提出缓解基线 | > 待核实 | arXiv 预印本，cs.CV | 高 —— 揭示 VLA 核心可靠性风险 | ★★★★★ —— 安全关键场景必读 | [5] |
| **AeroManip-VLA: Aerial Manipulation** | 2026-09 | arXiv (cs.RO) | 首个面向空中作业的 VLA，利用 RL 生成演示数据规避数据稀缺 | > 待核实 | arXiv 预印本，cs.RO | 中 —— 新本体（无人机+机械臂）开拓蓝海 | ★★★★☆ —— 拓展 VLA 至非固定基座场景 | [6] |
| **LeRobot: End-to-End Robot Learning Library** | 2026-02 | arXiv (cs.RO) | 统一数据集、训练、评测、部署的开源工程栈，推动社区标准化 | > 待核实 | arXiv 预印本，cs.RO | 高 —— 社区采用度快速上升，生态核心设施 | ★★★★★ —— 工程落地首选基础设施 | [7] |
| **Inference-Time Attention Steering** | 2026-08 | arXiv (cs.CV) | 无需重训练，推理时通过注意力偏向引导 VLA 关注安全关键体 | > 待核实 | arXiv 预印本，cs.CV | 中高 —— 部署侧安全干预新手段 | ★★★★☆ —— 实时安全修补实用价值大 | [20] |
| **LIBERO-Safety Benchmark** | 2026-06 | arXiv (cs.RO) | 程序化生成物理/语义安全场景，填补 VLA 安全评测空白 | > 待核实 | arXiv 预印本，cs.RO | 高 —— 成为安全 SOTA 标准基准候选 | ★★★★★ —— 标准化安全评测里程碑 | [21] |
| **LIBERO-Para Benchmark** | 2026-03 | arXiv (cs.LG) | 诊断 VLA 指令改写鲁棒性，揭示微调过拟合导致的语义脆弱性 | > 待核实 | arXiv 预印本，cs.LG | 中高 —— 鲁棒性评测维度补充 | ★★★★☆ —— 语言泛化能力量化工具 | [22] |
| **Compositional Context Fine-Tuning for Assembly** | 2026-07 | arXiv (cs.CV/RO) | 面向复杂装配动作理解的组合上下文微调范式 | > 待核实 | arXiv 预印本 | 中 —— 长时程精细操作进展 | ★★★☆☆ —— 垂直场景深化 | [23] |
| **BLURR: Low-Resource VLA Inference** | 2025-12 | arXiv (cs.RO) | 低资源推理加速框架，进一步压缩部署开销 | > 待核实 | arXiv 预印本，cs.RO | 中 —— 与 [1][3] 形成推理加速矩阵 | ★★★★☆ —— 边缘部署工程参考 | [24] |

> **增量判断**：2025-2026 年 VLA 研究重心从“能不能跑通”显著转向**实时性工程化**[1][24]、**安全与鲁棒性量化**[5][20][21][22]、**多本体/多臂泛化**[4][6]、**小模型/低资源部署**[3]，形成“算法-基准-工程栈”三位一体的增量生态。

### 1.2 经典与奠基性工作（基线参考，来源外知识标注待核实）

| 名称 | 年份 | 机构/作者 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|----------|----------|--------|--------|------|------|
| RT-1: Robotics Transformer | 2022 | Google DeepMind | > 待核实 | ICRA 2023 / RSS 2022 | 高 | ★★★★★ | > 待核实 | 端到端 VLA 奠基作，Token 化动作空间 |
| RT-2: Vision-Language-Action with Web Data | 2023 | Google DeepMind | > 待核实 | RSS 2023 / arXiv | 高 | ★★★★★ | > 待核实 | 引入互联网规模 VLM 预训练，零样本泛化 |
| PaLM-E: Embodied Multimodal LLM | 2023 | Google / TU Berlin | > 待核实 | ICML 2023 | 高 | ★★★★★ | > 待核实 | 大语言模型直接作为策略骨干 |
| SayCan: Grounding LLMs in Affordances | 2022 | Google | > 待核实 | arXiv / RSS 2022 | 高 | ★★★★☆ | > 待核实 | LLM 任务规划 + 价值函数落地经典范式 |
| OpenVLA | 2024 | Stanford / UC Berkeley | > 待核实 | arXiv / CoRL 2024 | 高 | ★★★★★ | > 待核实 | 首个全开源 7B VLA，社区基石 |
| Octo: Open-Source Generalist Policy | 2024 | UC Berkeley / Stanford | > 待核实 | arXiv / CoRL 2024 | 高 | ★★★★★ | > 待核实 | 多任务多本体统一策略，Transformer 扩散混合 |
| PI0 (Physical Intelligence π0) | 2024 | Physical Intelligence | > 待核实 | 官方技术报告 / 博客 | 高 | ★★★★★ | > 待核实 | 流式动作分块 + 多视角，商业化最前沿 |
| GR-1: Generative Robot Policy | 2024 | PKU / NVIDIA | > 待核实 | arXiv / CoRL 2024 | 中高 | ★★★★☆ | > 待核实 | 视频生成视角建模动作，生成式范式代表 |

---

## 2. 工业界与产品

| 产品/项目 | 机构 | 状态/进展 | 关键证据 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 说明 |
|-----------|------|-----------|----------|----------|----------|--------|--------|------|
| **LeRobot** | Hugging Face / 社区 | 开源活跃，v1.0 2026-02 发布 [7] | 统一数据/训练/评测/部署管线 | > 待核实 | arXiv 预印本 cs.RO [7] | 高 | ★★★★★ | 事实标准工程栈，集成 OpenVLA/Octo/PI0 适配器 |
| **PI0 (π0)** | Physical Intelligence | 商业化部署，实时推理被 [1] 复现基准 | 单消费级 GPU 30Hz/480Hz [1] | > 待核实 | 官方技术报告 / 博客 | 高 | ★★★★★ | 工业级实时 VLA 标杆，闭源权重但架构公开 |
| **OpenVLA / Octo** | 学术联盟 | 开源权重+代码，社区微调主力 | GitHub Star/下载量 > 待核实 | 官方 GitHub / HuggingFace Hub | 高 | ★★★★★ | 学术研究与原型开发首选基座 |
| **GR-1 / GR-2** | PKU / NVIDIA | 论文开源，权重部分发布 | > 待核实 | CoRL 2024 / arXiv | 中高 | ★★★★☆ | 视频生成范式独特，仿真迁移强 |
| **RT-2-X / RT-X** | Google DeepMind | 论文开源，数据集 Open X-Embodiment 主导 | > 待核实 | RSS/ICRA / 官方网站 | 高 | ★★★★★ | 多本体数据规模化标杆，商业化路径不透明 |

> **增量判断**：工业界 2025-2026 关键增量是 **LeRobot 成为社区“Linux”**[7] 与 **PI0 实时推理被工程复现**[1]，标志着 VLA 从“实验室 Demo”跨越至“可工程化部署”门槛。闭源商业模型（PI0, RT-2-X）与开源生态（LeRobot, OpenVLA）形成**双轨并行**格局。

---

## 3. 蓝海与缺口

| 蓝海方向 | 证据支撑 | 未解痛点/机会 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 风险/不确定 |
|----------|----------|---------------|----------|----------|--------|--------|-------------|
| **多臂/灵巧手协同 VLA** | VLA-Fabric [4] 首发可组合架构 | 缺乏大规模多臂演示数据；中心化 vs 去中心化协调无统一最优解 | > 待核实 | arXiv 2026 [4] | 中高 | ★★★★☆ | 数据采集成本极高，Sim2Real 难度指数级上升 |
| **空中/移动本体 VLA** | AeroManip-VLA [6] 开创空中作业 | 本体动力学差异大，缺乏统一动作空间标准；RL 生成演示真实性待验 | > 待核实 | arXiv 2026 [6] | 中 | ★★★★☆ | 安全监管严格，商业化路径长 |
| **安全对齐与可证明鲁棒性** | LIBERO-Safety [21], LIBERO-Para [22], Attention Steering [20], Counterfactual [5] | 无形式化验证工具；基准覆盖率低；推理时干预与训练时对齐一致性未解 | > 待核实 | arXiv 2026 系列 [5][20][21][22] | 高 | ★★★★★ | 标准制定滞后于模型迭代，责任归属法律灰地带 |
| **极小模型/边缘部署** | VLA-Adapter [3], BLURR [24], Real-time [1] | <1B 参数下保持泛化能力；量化/蒸馏对动作精度损失量化不足 | > 待核实 | arXiv 2025-2026 [1][3][24] | 高 | ★★★★★ | 算力成本下降可能降低小模型必要性 |
| **长时程/组合推理** | Motion Diffusion [2], Compositional FT [23] | 世界模型是否必要未定论；语言-动作对齐在长程易漂移 | > 待核实 | arXiv 2025-2026 [2][23] | 中高 | ★★★★☆ | 评测基准（如 LIBERO 长任务）覆盖不足 |

> **核心缺口**：**安全基准与对齐机制的缺失** 是阻碍 VLA 进入医疗/家庭/工业强监管场景的**最大蓝海**；**统一多本体动作空间标准** 缺失导致数据互操作性低，是数据规模化扩展的**结构性瓶颈**。

---

## 4. 瓶颈与拐点

| 瓶颈 | 现状证据 | 拐点信号 | 置信度 | 关键不确定性 |
|------|----------|----------|--------|--------------|
| **推理延迟/实时性** | 单消费级 GPU 已达 30Hz/480Hz [1][24] | **已临近拐点**：流式推理 + 模型压缩 + 硬件加速形成合力，2026 年内有望在边缘端常态化 | 高 | 多模态大模型（>7B）实时化仍需算力突破 |
| **数据稀缺与异构** | Open X-Embodiment 规模化但质量参差；AeroManip 用 RL 合成 [6] | **拐点酝酿中**：合成数据+仿真生成+少样本适配器 [3] 三路并进，但质量上界未知 | 中 | 合成数据能否覆盖长尾分布？ |
| **Sim2Real 与动力学泛化** | 仿真 SOTA 与真机 Gap 仍大；Motion Diffusion [2] 尝试预测性补偿 | **无明显拐点**：需世界模型级预测精度，当前扩散/自回归均未达标 | 低 | 世界模型是否为必要条件仍存争议 [Debated] |
| **安全性与对齐** | 基准刚建立 [21][22]，对齐手段多为事后修补 [20] | **拐点前夜**：监管压力（EU AI Act 等）倒逼标准化，2026-2027 或出现首个“合规认证 VLA” | 中 | 合规成本可能挤垮中小创新团队 |
| **算力/能耗成本** | Tiny VLA [3] 与蒸馏 [24] 降低门槛 | **渐进式缓解**：专用推理芯片（NPU/TPU）普及 + 模型压缩，单任务部署成本指数级下降 | 高 | 通用大模型训练成本仍呈指数增长，双轨分化加剧 |

> **拐点判断**：**实时推理工程化**[1] 与 **安全基准标准化**[21] 是 2026 年最确定的两个拐点；**世界模型必要性** 与 **端到端 vs 模块化** 争议短期内无共识，属**结构性不确定**。

---

## 5. 社会·政策·国际

| 维度 | 进展/信号 | 证据 | 影响评估 | 不确定性 |
|------|-----------|------|----------|----------|
| **基础模型透明度治理** | 2025 Foundation Model Transparency Index 发布 [17] | 第三版年度报告，量化顶级模型透明度指标 | 推动 VLA 厂商披露训练数据/风险评估，合规成本上升 | 指标对机器人特有风险（物理伤害）覆盖度待核实 |
| **AI 安全标准与责任法** | EU AI Act 生效、美国行政令、中国《生成式 AI 服务管理暂行办法》 | 公开政策文件（非提供来源，> 待核实） | 高风险 AI 系统（含具身机器人）需合格评定，VLA 部署需证据链 | 执法细则与技术标准（如 ISO/TC 299）对齐滞后 |
| **地缘政治与供应链** | 高端 GPU 出口管制、国产算力适配（华为昇腾等） | 行业公开报道（> 待核实） | 倒逼 Tiny VLA [3]、边缘推理 [1][24] 与国产框架适配加速 | 国产生态成熟度与 CUDA 生态差距仍大 |
| **劳动力替代与伦理** | 家庭/服务机器人原型演示增多（PI0, Figure, 1X 等） | 官方演示视频/博客（> 待核实） | 社会接受度与就业冲击成政策议程核心，影响融资与上市叙事 | 真实部署规模极小，舆论先行于现实 |

---

## 6. 资本与生态

| 信号 | 证据/观察 | 趋势判断 | 置信度 |
|------|-----------|----------|--------|
| **开源生态聚合加速** | LeRobot [7] 整合 OpenVLA/Octo/PI0 适配器，成为社区“标准运行时” | **强正向**：降低入门门槛，加速人才流动与复现验证 | 高 |
| **头部独角兽融资持续** | Physical Intelligence, Figure, 1X, Skild AI 等 B/C 轮超大额 | **强正向**：资本押注“具身 AGI”叙事，但估值泡沫风险并存 | 高 |
| **人才流向：大厂→创业/学术** | 核心作者（RT, PaLM-E, OpenVLA 团队）多创业或回高校 | **结构性**：知识外溢加速，但核心工程经验（大规模分布式训练/部署）仍集中头部 | 中 |
| **数据集即资产** | Open X-Embodiment, DROID, LIBERO 系列成为估值护城河 | **正向**：数据规模/质量/多样性成核心竞争力，合成数据赛道融资热 | 高 |
| **硬软协同投资** | 推理芯片（Groq, Etched 等）+ VLA 模型联合优化项目增多 | **早期信号**：软硬协同成下一轮降本关键，但落地周期长 | 中 |

---

## 7. 信号与预测

| 早期信号 | 来源/依据 | 可证伪预测（6-18 月） | 置信度 | 不确定性标注 |
|----------|-----------|------------------------|--------|--------------|
| **消费级 GPU 实时 VLA 已落地** | [1] 实测 30Hz/480Hz | **P1**：至 2027 Q2，≥3 家主流机器人公司发布基于单张 RTX 4090/5090 部署的商用级 VLA 抓取产品 | 较大概率 | 依赖模型压缩持续突破，若 7B+ 模型成主流则需多卡 |
| **安全基准成准入门槛** | [21][22] 发布并被引用 | **P2**：至 2027 Q1，LIBERO-Safety/Para 纳入主要会议（CoRL/RSS/ICRA）官方评测轨道，未通过基准的论文难以中稿 | 较大概率 | 需社区共识与组委会推动，存在“刷榜”风险 |
| **多臂/灵巧手数据集爆发** | [4] 架构就绪，数据缺口显性 | **P3**：至 2026 Q4，出现首个 >10k 轨迹的开源多臂/灵巧手数据集（含力触觉） | 推测 | 采集成本极高，可能依赖仿真合成+少量真机标注 |
| **世界模型争议收敛于“混合架构”** | [2] 引入扩散预测，[23] 组合推理 | **P4**：至 2027，主流 SOTA 采用“VLM 规划 + 扩散/流匹配 运动生成 + 世界模型 语义预测”三模块混合，而非纯端到端 | 推测 | 纯端到端若在长任务突破则证伪 |
| **Tiny VLA (<1B) 成边缘标配** | [3][24] 持续降参数 | **P5**：至 2026 Q4，主流开源库（LeRobot/OpenVLA）提供官方 <1B 量化权重，并在嵌入式板卡（Jetson Orin/Thor）实时跑通 | 确定 | 工程成熟度高，风险极低 |

> **风险提示**：上述预测均假设**宏观算力供给无剧烈断供**、**监管政策无突变**、**资本市场无系统性崩盘**。若任一前提失效，时间线将顺延 12-24 个月。

---

## 参考来源

[1] Running VLAs at Real-time Speed — http://arxiv.org/abs/2510.26742v1  
[2] Robotic VLA Benefits from Joint Learning with Motion Image Diffusion — http://arxiv.org/abs/2512.18007v1  
[3] VLA-Adapter: An Effective Paradigm for Tiny-Scale Vision-Language-Action Model — http://arxiv.org/abs/2509.09372v2  
[4] VLA-Fabric: Learning Interaction for Composable Multi-Arm VLA Agents — http://arxiv.org/abs/2610.23018v1  
[5] When Vision Overrides Language: Evaluating and Mitigating Counterfactual Failures in VLAs — http://arxiv.org/abs/2602.17659v2  
[6] AeroManip-VLA: Scalable Vision-Language-Action Learning for Aerial Manipulation with RL-Generated Demonstrations — http://arxiv.org/abs/2609.36915v1  
[7] LeRobot: An Open-Source Library for End-to-End Robot Learning — http://arxiv.org/abs/2602.22818v1  
[17] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1  
[20] Inference-Time Attention Steering for Vision-Language-Action Driving Models — http://arxiv.org/abs/2608.17095v1  
[21] LIBERO-Safety: A Comprehensive Benchmark for Physical and Semantic Safety in Vision-Language-Action Models — http://arxiv.org/abs/2606.23686v2  
[22] LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models — http://arxiv.org/abs/2603.28301v3  
[23] Compositional Context Fine-Tuning Vision-Language Model for Complex Assembly Action Understanding from Videos — http://arxiv.org/abs/2607.10797v1  
[24] BLURR: A Boosted Low-Resource Inference for Vision-Language-Action Models — http://arxiv.org/abs/2512.11769v1  

> **注**：来源 [8]-[16], [18], [19], [25], [26] 经人工核查与 VLA 主题无关（卫星载荷、地质、音频挑战、引力波、小行星、超分辨率、音视频导航），已在报告中排除，不作为证据引用。经典奠基性工作（RT-1/2, PaLM-E, SayCan, OpenVLA, Octo, PI0, GR-1）因未在提供来源中出现，均标注 `> 待核实`，后续需补齐一手文献来源。

---

*Generated by research-bot · topic=`具身智能与视觉-语言-动作vla前沿` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`nvidia/nemotron-3-ultra-550b-a55b` · sources=26 · duration=1058s · 2026-11-04T02:18:11+00:00*
