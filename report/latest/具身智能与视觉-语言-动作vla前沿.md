# 具身智能与视觉-语言-动作（VLA）前沿调研报告

**日期**：2026-10-28 | **领域**：Embodied AI / Vision-Language-Action (VLA) / Robotics | **检索源数量**：34

---

## 1. 进展与热点

### 1.1 最新架构范式与算法突破（2025-2026 增量）

| 名称 | 年份 | 机构/作者 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|----------|----------|--------|--------|------|------|
| Inference-Time Attention Steering (ITAS) | 2026 | Alpamayo-R1 / Qwen3-VL backbone | arXiv 2026 预印本，引用数 > 待核实 | arXiv cs.CV 预印本 [2] | 中 — 针对 VLA 驾驶安全关键场景的新范式 [2] | ★★★★☆ — 解决推理时可控性痛点，无需重训练 [2] | [2] | 双阶段架构（推理阶段+扩散轨迹解码器），通过有界加性 pre-softmax 注意力偏置实现 fail-open 前向 pre-hook 干预 [2] |
| Compositional Context Fine-Tuning (CCFT) | 2026 | 未明确机构 | arXiv 2026 预印本，引用数 > 待核实 | arXiv cs.CV 预印本 [7] | 中 — 面向复杂装配动作理解的 VLM 微调新范式 [7] | ★★★☆☆ — 为精细操作语义分解提供思路，但侧重理解而非生成 [7] | [7] | 将装配动作分解为 Verb/Object/Tool 语义元素，适配 VLM 用于人机协作装配 [7] |
| LingBot-VLA 2.0 / Pragmatic VLA Foundation Model | 2026 | LingBot 团队 | arXiv 2026 预印本 (v4)，引用数 > 待核实 | arXiv cs.RO 预印本 [13, 21] | 中高 — 强调实用化、跨任务/跨平台泛化与成本效率 [13, 21] | ★★★★☆ — 从基础模型走向应用的工程化尝试 [13] | [13, 21] | 在三大功能域改进 LingBot-VLA，关注真机部署落地 [13, 21] |
| Robotic VLA + Motion Image Diffusion | 2025 | 未明确机构 | arXiv 2025 预印本，引用数 > 待核实 | arXiv cs.RO 预印本 [14] | 中 — 引入运动图像扩散联合学习，增强预测性运动推理 [14] | ★★★★☆ — 解决 VLA 仅模仿专家轨迹缺乏推理的问题 [14] | [14] | 通过联合学习运动图像扩散，赋予 VLA 预测性运动推理能力 [14] |
| Running VLAs at Real-time Speed (π0-FAST) | 2025 | Physical Intelligence | arXiv 2025-10 提交，近期关注度高 [15] | arXiv cs.RO 预印本 [15] | 高 — 单张消费级 GPU 实现 30Hz/480Hz 实时推理，真机 100% 成功率 [15] | ★★★★★ — VLA 工程落地关键突破，官方开源代码 [15, 32] | [15, 32] | 全流式推理框架，配套 OpenPI 代码开源，验证真机抓取掉落笔任务 [15] |
| VLA-Adapter | 2025 | 17 人作者团队 | arXiv 2025-09 提交，关注度中等 [25] | arXiv cs.RO 预印本 [25] | 中 — 轻量化适配器降低训练成本，适合小规模模型快速迁移 [25] | ★★★☆☆ — 训练端创新，部署端无直接贡献 [25] | [25] | 提出有效范式减少大规模预训练依赖，降低训练开销 [25] |

> **增量判断**：相对 2024 年基线，2025-2026 年核心增量在于 **(1) 推理时干预范式 (ITAS [2]) 解决安全可控性；(2) 实时推理框架 (π0-FAST [15]) 打破部署延迟瓶颈；(3) 联合生成式建模 (Motion Image Diffusion [14]) 增强运动推理；(4) 实用化基础模型 (LingBot-VLA [13, 21]) 与轻量化适配器 [25] 推动工程落地。**

### 1.2 经典与奠基性工作（基线参考）

| 名称 | 年份 | 机构/作者 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|----------|----------|--------|--------|------|------|
| Octo: Open-Source Generalist Robot Policy | 2024 | Octo 团队 | GitHub Stars > 待核实，引用数 > 待核实 | arXiv cs.RO 预印本 [1] | 高 — 通用机器人策略开源基石 [1, 34] | ★★★★★ — 多任务、多本体开源基准 [1] | [1] | 统一 Transformer 架构，支持多模态输入与动作分块预测 [1, 34] |
| RT-2 / RT-1 / PaLM-E | 2022-2023 | Google DeepMind | 引用数极高（RT-2 > 2k+），业界标杆 > 待核实 | 顶会/期刊 (RSS/CoRL/ICRA) > 待核实 | 极高 — VLA 领域奠基性工作 [34] | ★★★★★ — 必读经典，确立 VLM+Policy 范式 [34] | [34] | 博客 [34] 系统梳理：RT-1 端到端，RT-2 引入 VLM 共同嵌入，PaLM-E 具身多模态语言模型 [34] |
| OpenVLA | 2024 | Stanford / UC Berkeley 等 | GitHub Stars > 待核实，HuggingFace 下载量高 > 待核实 | 顶会 (ICRA/CoRL) > 待核实 | 高 — 开源 7B VLA 模型，基于 Prismatic-7B + Open X-Embodiment [34] | ★★★★★ — 学术界复现 RT-2 主流选择 [34] | [34] | 博客 [34] 介绍：开源权重、数据、代码，支持微调 [34] |
| π0 (pi0) | 2024 | Physical Intelligence | 官方博客/技术报告，闭源权重 > 待核实 | 技术报告/官方博客 [32, 34] | 高 — 流式动作分块、多视角、高频控制 [15, 34] | ★★★★★ — 实时控制架构参考标杆 [15, 34] | [15, 32, 34] | 博客 [34] 介绍：流式动作专家，后经 [15] 实现消费级 GPU 实时化 [15] |
| Decision Transformer / Perceiver-Actor | 2021-2022 | Facebook AI / DeepMind | 引用数高，RL/序列建模基石 > 待核实 | 顶会 (ICML/NeurIPS) > 待核实 | 高 — 离线 RL 与感知编码器经典范式 > 待核实 | ★★★★☆ — 理解 VLA 序列建模根源必读 > 待核实 | > 待核实 | 当前检索源未直接覆盖原文，仅通过 [34] 间接提及，需补全一手文献 |

> **注**：经典工作部分信息源自综述性博客 [34]（二手来源，证据等级 C），核心指标（引用数、Stars、Venue）标注 `> 待核实`，需后续补全一手论文来源。

---

## 2. 工业界与产品

### 2.1 主要玩家与产品进展

| 公司/项目 | 产品/模型 | 关键进展 (2024-2026) | 证据来源 | 部署形态 | 备注 |
|-----------|-----------|----------------------|----------|----------|------|
| Physical Intelligence | π0 / π0-FAST / OpenPI | 官方开源 OpenPI 训练管线 [32]；实时推理框架单消费级 GPU 30Hz/480Hz [15]；真机抓取任务 100% 成功率 [15] | [15, 32] | 真机部署 (实时推理) | 官方出品，代码开源，工程成熟度高 [15, 32] |
| LingBot (灵伴) | LingBot-VLA / LingBot-VLA 2.0 | 提出 Pragmatic VLA Foundation Model [21]；v2.0 面向应用改进三大功能域 [13] | [13, 21] | 实验室/原型机 | 强调跨任务泛化与成本效率，论文为预印本 [13, 21] |
| Alpamayo (推测) | Alpamayo-R1 (驾驶 VLA) | 提出 ITAS 推理时注意力引导，Qwen3-VL 骨干 [2] | [2] | 仿真/合成数据验证 | 驾驶垂类 VLA，安全干预创新 [2] |
| 其他 (Figure, Tesla, 1X, Agility 等) | 未在证据中覆盖 | 无直接证据 | > 待核实 | > 待核实 | **缺口**：主流人形/具身公司最新产品进展、量产节点、Sim2Real 细节在当前 34 条来源中缺失 |

> **增量判断**：Physical Intelligence 通过 [15, 32] 实现了 **从闭源演示到开源实时推理框架** 的关键增量；LingBot 通过 [13, 21] 推进 **实用化基础模型** 落地；驾驶垂类出现 **推理时安全干预** 新范式 [2]。**风险**：多数进展仍停留在论文/预印本或受控实验，规模化量产证据缺失。

---

## 3. 蓝海与缺口

| 缺口维度 | 具体描述 | 证据支撑 | 优先级 |
|----------|----------|----------|--------|
| **Sim2Real 与真机泛化验证不足** | ITAS [2] 仅在合成数据集 (50 变道场景) 验证；π0-FAST [15] 仅单任务真机演示；缺乏多任务、多本体、长时真机基准 | [2, 15, q1-open_problems] | ⭐⭐⭐⭐⭐ |
| **Scaling Law 系统性研究缺失** | 候选证据中未覆盖 VLA 专用 Scaling Law (数据/模型/算力三要素) 系统实验 | [q1-open_problems] | ⭐⭐⭐⭐ |
| **语义理解到动作生成的端到端桥接** | CCFT [7] 仅做动作理解分解，未接动作生成头；缺乏 "语义元素 → 连续动作" 统一架构 | [7, q1-open_problems] | ⭐⭐⭐⭐ |
| **工程化标准化缺失 (ROS2/硬件/实时)** | OpenVLA、Octo、GR-1、RoboKit 等主流项目 ROS2 节点、硬件驱动适配、ONNX/TensorRT 量化、多相机同步、安全停止无成熟最佳实践 | [q3-open_problems] | ⭐⭐⭐⭐⭐ |
| **第三方独立复现与基准测试缺失** | 不同 GPU/CPU 组合下吞吐率、端到端延迟、成功率统计无社区公认基准 | [q3-open_problems] | ⭐⭐⭐⭐ |
| **多任务/多本体推理时干预通用性** | ITAS [2] 仅验证驾驶变道场景，通用操作任务、灵巧手、移动底盘迁移未验证 | [2, q1-open_problems] | ⭐⭐⭐ |
| **数据集多样性与质量** | 依赖 Open X-Embodiment、DROID 等现有数据集，合成数据 [2] 真机迁移价值未知；精细操作高质量数据稀缺 | [2, 15, 34] | ⭐⭐⭐⭐ |

> **不确定**：上述缺口是否在近 3 个月内被新工作 (如 CoRL 2026 / RSS 2026 新论文) 部分填补，当前检索源截止 2026-08/09，**需持续追踪**。

---

## 4. 瓶颈与拐点

| 瓶颈 | 现状与证据 | 拐点信号与时间窗口 | 置信度 |
|------|------------|---------------------|--------|
| **推理延迟与实时性** | 传统 VLA 推理 >100ms，难满足高频控制；π0-FAST [15] 在单张消费级 GPU (RTX 4090 级) 实现 30Hz 帧率 / 480Hz 轨迹频率，**拐点已现** | 2025-Q4 论文 [15] + 代码开源 [32] → 2026-H1 社区复现与移植 → 2026-H2 成为部署标配 | 高 (有真机实测 [15]) |
| **训练成本与数据饥渴** | 7B+ VLA 全微调需百张 A100 天级；VLA-Adapter [25] 提出轻量化适配，**早期信号** | 2025-Q3 论文 [25] → 2026 适配器/LoRA/蒸馏技术成熟 → 单卡/少卡微调常态化 | 中 (仅单篇预印本 [25]) |
| **安全性与可控性** | 端到端 VLA 黑盒，难保证安全关键行为；ITAS [2] 提出推理时注意力引导，**范式创新** | 2026-Q3 论文 [2] → 2026-Q4 扩展至操作任务 → 2027 形成 "推理时对齐" 标准流程 | 中高 (原理通用，但仅驾驶验证 [2]) |
| **运动推理与规划能力** | 纯模仿学习缺乏预测性推理；Motion Image Diffusion 联合学习 [14] 引入生成式运动先验，**架构演进** | 2025-Q4 论文 [14] → 2026 世界模型/扩散策略融合 VLA 主流化 | 中 (需更多独立验证) |
| **评测基准碎片化** | LIBERO、SimplerEnv、DROID、Open X-Embodiment 并存，指标不统一；RT-Bench [17] 关注实时性而非任务成功率 | 2026 亟需统一 "真机泛化基准"，预测 CoRL/RSS 2026 将有新基准发布 | 预测 [P] |

> **拐点总结**：**实时推理 [15] 与推理时干预 [2] 是确信度最高的两个拐点**，分别解决 "能不能跑得动" 与 "敢不敢用"；轻量化训练 [25] 与生成式运动推理 [14] 为跟进信号。

---

## 5. 社会·政策·国际

> **待核实**：当前 34 条检索来源 **均无覆盖** 监管政策、出口管制、数据合规、劳动替代伦理、国际标准 (ISO/TC 299)、地缘政治供应链 (GPU/传感器/本体) 等维度信息。
> **建议**：需补充检索：中国《新一代人工智能治理专项》、欧盟《AI Act》机器人附件、美国 NIST 机器人标准、中美实体清单对算力/传感器影响、IFR 世界机器人报告 2024/2025。

---

## 6. 资本与生态

### 6.1 开源生态版图 (基于可核实来源)

| 项目 | 维护方 | 代码/权重开源度 | 社区热度 (Stars/Forks) | ROS2/硬件适配现状 | 证据 |
|------|--------|-----------------|------------------------|-------------------|------|
| **OpenPI** | Physical Intelligence (官方) | 训练管线代码开源 [32]；π0 权重闭源，π0-FAST 近似实现 [15] | 近期发布，关注度快速上升 > 待核实 | 官方仓库文档待细读，论文 [15] 未详述 ROS2 集成 | [15, 32] |
| **Octo** | Octo 团队 | 代码、权重、数据全开源 [1] | GitHub Stars > 待核实 | 基于 JAX/Flax，ROS2 桥接需社区自行实现 > 待核实 | [1, 34] |
| **OpenVLA** | Stanford 等 | 代码、权重 (7B/13B)、微调脚本开源 > 待核实 | HuggingFace 下载量高 > 待核实 | PyTorch 实现，ROS2 适配社区贡献为主 > 待核实 | [34] |
| **GR-1 / RoboKit** | 未在证据中覆盖 | > 待核实 | > 待核实 | > 待核实 | > 待核实 |

### 6.2 投融资与人才信号
> **待核实**：当前来源无融资轮次、估值、并购、高管流动数据。Physical Intelligence 融资背景 (公开报道数亿美金) 需补查；LingBot 团队融资情况未见。

### 6.3 生态协作与标准化
- **碎片化风险**：各项目自行实现 ROS2 Control / MoveIt 2 集成，缺乏统一 `vla_msgs` / `vla_controller_interface` 标准 [q3-open_problems]。
- **数据许可**：Open X-Embodiment 等数据集许可证 (CC-BY-4.0 等) 商用合规性需法务审查 > 待核实。

---

## 7. 信号与预测

| # | 早期信号 (来源) | 预测假设 (可证伪) | 置信度 | 验证窗口与指标 |
|---|-----------------|-------------------|--------|----------------|
| 1 | π0-FAST 单消费级 GPU 实时推理 [15] + OpenPI 开源 [32] | **假设**：至 2026-Q4，≥3 个开源项目 (OpenVLA/Octo/GR-1 等) 合并或复现 π0-FAST 流式推理内核，在 RTX 4090/5090 上跑通 30Hz+ 多视角真机闭环。 | 较大概率 | 指标：GitHub PR 合并记录、社区复现报告、ROS2 驱动发布 |
| 2 | ITAS 推理时注意力引导无需重训练干预行为 [2] | **假设**：至 2027-Q1，出现通用 "VLA Safety Shield" 开源库，支持通过自然语言/检测器触发注意力偏置，覆盖 ≥5 种本体 (机械臂/灵巧手/移动/人形/驾驶)。 | 推测 | 指标：arXiv 新论文引用 [2]、GitHub 专用仓库 Stars > 500 |
| 3 | VLA-Adapter 轻量化适配器范式 [25] | **假设**：至 2026-Q4，HuggingFace Hub 上出现 ≥20 个基于 OpenVLA/Octo/π0-FAST 的 LoRA/Adapter 微调权重，单卡 24GB 显存可在 4h 内完成新任务适配。 | 较大概率 | 指标：HF Model Card 标签、微调教程、社区 Benchmark |
| 4 | LingBot-VLA 2.0 强调跨平台泛化与成本效率 [13, 21] | **假设**：至 2026-Q4，LingBot 发布技术报告展示在 ≥3 种商用机械臂 (Franka/UR/国产) + 移动底盘上零样本/少样本完成 ≥10 个长时任务，成功率 > 80%。 | 推测 | 指标：官方博客/技术报告/视频、第三方邀请测评 |
| 5 | 世界模型/扩散策略与 VLA 融合趋势 [14] | **假设**：CoRL 2026 / RSS 2026 将有 ≥5 篇论文显式融合 "VLA + 视频扩散/世界模型"，且在真机长时任务上显著优于纯 VLA 基线。 | 预测 [P] | 指标：会议录用列表、OpenReview 讨论、开源代码 |

> **不确定性声明**：上述预测基于当前 34 条来源的 **早期信号外推**，受算力供给、数据版权、人才流动、宏观资本环境等外部因素影响大，**需滚动更新**。

---

## 参考来源

[1] Octo: An Open-Source Generalist Robot Policy — http://arxiv.org/abs/2405.12213v2  
[2] Inference-Time Attention Steering for Vision-Language-Action Driving Models — http://arxiv.org/abs/2608.17095v1  
[3] TTLab at Daleel 2026: STAR-Ar, Sequence Tagging for Argument Recognition in Arabic — http://arxiv.org/abs/2609.39385v1  
[4] ZeroR@CHiPSAL 2026: Two-Stage Vision-Language Adaptation with Contrastive Learning for Nepali Meme Classification — http://arxiv.org/abs/2607.28637v1  
[5] UIC-AIHealth4All at ArchEHR-QA 2026: Answer-First Evidence Grounding for Clinical Question Answering — http://arxiv.org/abs/2608.27467v1  
[6] Second MOASEI Competition at AAMAS'2026: A Technical Report — http://arxiv.org/abs/2607.03399v1  
[7] Compositional Context Fine-Tuning Vision-Language Model for Complex Assembly Action Understanding from Videos — http://arxiv.org/abs/2607.10797v1  
[8] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1  
[9] Technical Report for Ego4D Long-Term Action Anticipation Challenge 2025 — http://arxiv.org/abs/2506.02550v2  
[10] TTLab at AlexandriaX-2026: A Fine-Tuned Surface Tagger for Arabic Machine-Translation Error-Span Detection and Classification — http://arxiv.org/abs/2609.29633v1  
[11] Double Multi-Head Attention Multimodal System for Odyssey 2024 Speech Emotion Recognition Challenge — http://arxiv.org/abs/2406.10598v1  
[12] Hierarchical Pre-Training of Vision Encoders with Large Language Model — http://arxiv.org/abs/2604.00086v2  
[13] From Foundation to Application: Improving VLA Models in Practice — http://arxiv.org/abs/2607.06403v1  
[14] Robotic VLA Benefits from Joint Learning with Motion Image Diffusion — http://arxiv.org/abs/2512.18007v1  
[15] Running VLAs at Real-time Speed — http://arxiv.org/abs/2510.26742v1  
[16] Overview of AuTexTification at IberLEF 2023: Detection and Attribution of Machine-Generated Text in Multiple Domains — http://arxiv.org/abs/2309.11285v1  
[17] RT-Bench: an Extensible Benchmark Framework for the Analysis and Management of Real-Time Applications — http://arxiv.org/abs/2203.11423v2  
[18] Instruments of RT-2 Experiment onboard CORONAS-PHOTON and their test and evaluation I: Ground calibration of RT-2/S and RT-2/G — http://arxiv.org/abs/1011.3326v1  
[19] (2+1)D topological phases with RT symmetry: many-body invariant, classification, and higher order edge modes — http://arxiv.org/abs/2403.18887v1  
[20] Indian Payloads (RT-2 Experiment) Onboard CORONAS-PHOTON Mission — http://arxiv.org/abs/0912.4126v2  
[21] A Pragmatic VLA Foundation Model — http://arxiv.org/abs/2601.18692v4  
[22] RT-DETR-Palm A Transformer Based Approach for Oil Palm Tree Detection Using UAV Imagery — https://doi.org/10.1109/icatei67676.2025.11404965  
[23] MOAC-RT: Personalized Multi-Objective Radiotherapy using Actor-Critic Deep Reinforcement Learning — https://doi.org/10.21203/rs.3.rs-5637868/v1  
[24] Figure 5: RT-PCR validation of 11 oil palm lncRNAs in six developing stages of mesocarp, leaf, root, flower and kernel of oil palm. — https://doi.org/10.7717/peerj.9585/fig-5  
[25] VLA-Adapter: An Effective Paradigm for Tiny-Scale Vision-Language-Action Model — http://arxiv.org/abs/2509.09372v2  
[26] A Tutorial for Evaluating Cure Model Appropriateness — http://arxiv.org/abs/2605.04999v2  
[27] Octo's Adventure: At-home Deployment of a Pediatric Education Tool — http://arxiv.org/abs/2608.06684v1  
[28] A Tutorial on Linear Least Square Estimation — http://arxiv.org/abs/2211.15347v1  
[29] Deep Learning for MIR Tutorial — http://arxiv.org/abs/2001.05266v1  
[30] Multimodal Pretraining and Generation for Recommendation: A Tutorial — http://arxiv.org/abs/2405.06927v1  
[31] A Bird's-Eye Tutorial of Graph Attention Architectures — http://arxiv.org/abs/2206.02849v1  
[32] OpenPI - Physical Intelligence - GitHub — https://github.com/Physical-Intelligence/openpi  
[33] On-Device Recommender Systems: A Tutorial on The New-Generation Recommendation Paradigm — http://arxiv.org/abs/2312.10864v1  
[34] Generalist Robot Policies Explained: RT-2, OpenVLA, pi0, Octo — https://robocloud-dashboard.vercel.app/learn/blog/generalist-robot-policies-2025

---

*Generated by research-bot · topic=`具身智能与视觉-语言-动作vla前沿` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`nvidia/nemotron-3-ultra-550b-a55b` · sources=34 · duration=522s · 2026-10-28T22:33:37+00:00*
