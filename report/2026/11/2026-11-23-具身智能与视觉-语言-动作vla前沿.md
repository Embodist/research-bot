# 具身智能与视觉-语言-动作（VLA）前沿调研报告：七维增量快照

**日期**：2026-11-23（UTC）  
**领域**：Embodied AI / Vision-Language-Action (VLA) / Robotics Software Stack (ROS2/C++)  
**检索源数量**：36 条可引用证据（编号 [1]–[2]）  
**方法论**：deep-research / frontier-tracking / paper-survey / evidence-grading / frontier-watch  

---

## 1. 进展与热点

### 1.1 核心判断：证据层面的“进展真空”  
> 待核实：当前提供的 36 条证据中，**不存在任何一条**直接记录 2024-2026 年 VLA 领域（RT-2, Octo, OpenVLA, π0, GR-1, Diffusion Policy 等）的核心进展、SOTA 变动或多任务/多本体真机独立验证结果。子问题 q1 的四个候选证据 [3][4][5][6] 全部与 VLA 无关（家禽养殖、具身认知社论、MLLM 综述、基础模型透明度指数）[q1-finding-1]。这构成了本次调研的**首要增量发现**：**可用证据集与研究主题严重错位**，导致无法基于现有材料给出任何有引用支撑的“最新进展”结论。

### 1.2 唯一可引用的 VLA 相关新论文（2026）  
| 维度 | 内容 | 证据 |
|------|------|------|
| 论文 | *Inference-Time Attention Steering for Vision-Language-Action Driving Models* | [7] |
| 年份/来源 | 2026 / arXiv 预印本 (cs.CV) | [7] |
| 核心贡献 | 揭示当前 VLA 驾驶模型采用「推理阶段 + 扩散轨迹解码器」架构，但缺乏**无需重训练即可在推理时将注意力重定向至安全关键目标**的机制 | [7] |
| 热度证据 | citations=0（刚发布）、GitHub star 未公开 | > 待核实 |
| 权威证据 | arXiv 预印本，未经同行评审 | [7] |
| 关注度 | 低 —— 单篇最新预印本，无引用/社区讨论信号 | [7] |
| 推荐度 | ★★★☆☆ —— 可作为 VLA 驾驶子方向“推理时干预”这一开放问题的参考，但非经典奠基工作 | [7] |

### 1.3 经典/奠基性工作**完全缺失**  
子问题 q2 的候选证据 [8][9][7][10] 中，**零篇**覆盖公认的 VLA 里程碑：RT-1/RT-2 (Brohan et al.), OpenVLA (Kim et al.), Octo (Octo Model Team), PaLM-E, PerAct, BridgeData, Open X-Embodiment 等 [q2-finding-3]。唯一 VLA 相关论文 [7] 为 2026 年驾驶子方向最新作，无法构成技术演进脉络（模块化→端到端→基础模型→统一动作空间）的关键节点。

> 待核实：经典工作清单需另行检索（建议关键词：`RT-1 OR RT-2 OR OpenVLA OR Octo OR PaLM-E OR PerAct OR "Open X-Embodiment" OR "BridgeData" site:arxiv.org OR site:openreview.net`）。

---

## 2. 工业界与产品

### 2.1 可引用的开源 VLA 工程实践  
| 名称 | 年份 | 机构/作者 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|----------|----------|--------|--------|------|------|
| OpenGalaxea/GalaxeaVLA | 2026 | OpenGalaxea 组织 | GitHub star > 待核实 | GitHub 官方仓库 | 中 —— 少数提供真机部署文档的开源 VLA 项目 | ★★★☆☆ —— 直接提供 Server/Client 真机部署架构参考，但缺乏延迟/硬件适配量化基准 | [11] | GPU 机器跑 G0.5 策略服务端，机器人端作客户端推理 |

### 2.2 ROS2/C++ 部署与通信层最新进展（非 VLA 专用但高度相关）  
| 项目/论文 | 年份 | 核心增量 | 证据 | 热度/权威 | 推荐度 |
|-----------|------|----------|------|-----------|--------|
| ROS2 Connect | 2026 | 基于 WebSocket 的 ROS2 跨 WAN 通信，实测**更低延迟、更高稳定性、更好扩展性**，支持双向 Topic/Service/Action 透传 | [12] | arXiv 预印本 (cs.RO)，citations=0 | ★★★☆☆ —— 为 VLA 云边/远程部署提供通信层参考 |
| Low-Latency Async Visual Inference on ROS2 Mobile Platform | 2026 | CCDC 2026 同行评审会议论文，针对 ROS2 移动平台异步视觉推理延迟优化 | [13] | CCDC 2026（同行评审），citations=0 | ★★★☆☆ —— 主题高度贴近 VLA 推理工程优化 |
| Homomorphic Encryption Inference Deployment Assessment | 2026 | 揭示同态加密推理在传感器-网关-云系统中**工程落地极难**（密钥 GB 级、需网关回调、中间值泄露） | [14] | Sensors 期刊（同行评审），citations=0 | ★★☆☆☆ —— 为 VLA 隐私部署提供反面工程经验 |

### 2.3 产业化部署证据缺口  
> 待核实：证据集中**无任何**厂商级 VLA 产品发布、量产案例、商业化进度、真机闭环性能指标（成功率、任务数、本体类型）的独立验证报告。子问题 q3 的所有工程证据均来自学术会议/预印本/单一开源仓库，缺乏产业界一手来源。

---

## 3. 蓝海与缺口

基于三个子问题的 `open_problems` 汇总，结合证据分级，梳理如下**高确定性蓝海/缺口**（均有 [n] 支撑）：

| # | 蓝海/缺口描述 | 来源证据 | 证据等级 | 关键词 |
|---|--------------|----------|----------|--------|
| 1 | **VLA 核心文献与基准的系统性缺失**：现有证据集零覆盖 RT-1/RT-2/OpenVLA/Octo 等奠基工作，导致无法构建技术演进脉络 | [q2-finding-3] | A（调研元证据） | 文献缺口 |
| 2 | **多任务/多本体真机独立验证基准缺失**：无第三方复现报告、RoboArena/SimplerEnv 等榜单数据 | [q1-finding-1] | A（调研元证据） | 评测缺口 |
| 3 | **开源 VLA 项目缺乏标准化推理延迟基准**：GalaxeaVLA 等无 P50/P99 延迟、吞吐率、硬件适配矩阵（GPU/NPU/CPU）实测数据 | [q3-finding-1][11] | B（GitHub 官方文档） | 工程基准缺口 |
| 4 | **ROS2 原生 DDS 跨子网/WAN 不可用**：导致 VLA 远程/云边部署必须依赖额外通信层（如 ROS2 Connect），但该类方案未在 VLA 真机闭环大规模验证 | [12][q3-finding-3] | B/C | 通信层缺口 |
| 5 | **VLA 实时控制回路确定性延迟保障最佳实践缺失**：含预处理/推理/后处理/通信抖动的端到端工程化压测报告不公开 | [q3-open-3] | C（社区共识） | 实时性缺口 |
| 6 | **隐私保护推理（同态加密/TEE/联邦学习）在 VLA 场景工程可行性极低**：密钥体积大、需网关交互、中间值泄露 | [14][q3-open-4] | A（同行评审期刊） | 隐私部署缺口 |
| 7 | **VLA 驾驶模型推理时注意力引导机制缺失**：无需重训练即可重定向注意力至安全关键目标 | [7][q2-finding-2] | B（arXiv 预印本） | 安全对齐缺口 |

> **增量判断**：上述缺口均为**相对“已有证据基线”新增识别**的结构性空白，而非常识复述。其中第 1、2 项为**元层面缺口**（证据集本身不足），第 3-7 项为**工程/算法层面缺口**（有文献/项目直接指证）。

---

## 4. 瓶颈与拐点

### 4.1 算法/数据瓶颈（证据支撑较弱，标注不确定性）  
> 待核实：当前证据集**无任何**关于 VLA 预训练数据规模、统一动作空间标准化、世界模型集成、长时程推理等算法层面瓶颈的一手论文或基准数据。子问题 q1/q2 的证据完全覆盖不到这些主题。

### 4.2 工程/部署瓶颈（有直接证据）  
| 瓶颈 | 表现 | 证据 | 严重度 | 拐点信号 |
|------|------|------|--------|----------|
| **推理延迟与确定性** | ROS2 移动平台异步视觉推理仍需专门优化；端到端抖动无公开压测基准 | [13][q3-open-3] | 高 | CCDC 2026 同行评审论文出现，说明学术界开始系统攻关 |
| **跨网通信** | ROS2 DDS 原生不支持 WAN/跨子网，需额外 WebSocket 层（ROS2 Connect） | [12] | 高 | 2026-08 预印本提出完整方案并实测 WAN 环境 |
| **隐私/安全部署** | 同态加密方案工程不可行（GB 密钥、网关回调、中间值泄露） | [14] | 中 | Sensors 2026 期刊给出基于测量的准入评估框架，否定快速实现路径 |
| **硬件适配矩阵缺失** | 无 GPU/NPU/CPU 不同算力平台上的 VLA 推理实测对比表 | [11][q3-open-1] | 高 | OpenGalaxea 仅给出 Server/Client 架构图，无量化指标 |

### 4.3 拐点预判（基于工程瓶颈的信号）  
- **通信层标准化拐点**：若 ROS2 Connect 或类似方案在 2027 年前被纳入 ROS2 官方发行版（如 Rolling/Jazzy 后续版本），将标志着 VLA 云边部署通信瓶颈**实质性缓解** [P, 置信度 0.6, 依据：[12] 为预印本，尚未进入官方 REP 流程]。  
- **推理延迟基准建立拐点**：若出现面向 VLA 的 **MLPerf Inference / ROS2 Benchmark 官方套件**（含 P50/P99、硬件矩阵），将标志着工程评测从“缺失”走向“可比” [P, 置信度 0.5, 依据：[13] 显示学术界已开始单点攻关，但无统一基准]。  
- **隐私路线切换拐点**：同态加密被学术界确证为“快速实现≠可部署” [14]，预测 2026-2027 年 VLA 隐私方案将**集体切向 TEE（可信执行环境）或联邦学习**路线 [P, 置信度 0.7, 依据：[14] 给出否定性工程证据，倒逼路线转换]。

---

## 5. 社会·政策·国际

> 待核实：提供的 36 条证据**零覆盖**具身智能/VLA 相关的监管政策、标准制定（ISO/TC 299、IEEE RAS）、地缘政治供应链（GPU/高端传感器出口管制）、伦理劳动影响、国际合作/竞争格局等内容。子问题 q1-q3 的所有证据均为技术论文/工程项目，无任何政策/社会维度来源。

### 5.1 需持续监测的政策/国际信号（基于领域常识，标注为预测/不确定）  
| 维度 | 可能的增量信号 | 当前证据状态 | 监测建议 |
|------|----------------|--------------|----------|
| 标准化 | ISO/IEC 22989 (AI 概念) / ISO 18646 (机器人性能) 向 VLA 扩展 | 无证据 | 关注 ISO/TC 299/WG 9 会议纪要 |
| 出口管制 | 高端 GPU (H100/H200)、高精度力触觉传感器对华管制升级 | 无证据 | 跟踪 BIS/商务部公告 |
| 劳动伦理 | 通用机器人替代蓝领岗位的社会接受度、最低工资法关联 | 无证据 | 关注 ILO/各国劳动部门报告 |
| 国际竞争 | 中美欧在 Open X-Embodiment 类数据集主导权、基础模型权重开放度博弈 | 无证据 | 监测 HuggingFace Hub 下载地理分布、arXiv 投稿机构分布 |

---

## 6. 资本与生态

> 待核实：证据集**无任何**融资轮次、并购案例、人才流动（核心作者入职/创业）、开源社区活跃度（GitHub star 趋势、PR/issue 响应）、公司格局变化等资本/生态层面的一手数据。

### 6.1 可推断的生态弱信号（仅基于现有技术证据的间接推断）  
| 信号 | 间接依据 | 置信度 | 说明 |
|------|----------|--------|------|
| **开源 VLA 生态处于极早期** | 仅发现 1 个有真机部署文档的开源仓库 (GalaxeaVLA) [11]，且无 star 数/贡献者数据 | 低 | 与 LLM 生态（Llama, Mistral 等百星仓库）差距巨大 |
| **ROS2 生态正向 VLA 适配演进** | ROS2 Connect [12]、低延迟异步推理 [13] 等 2026 新作聚焦通信/推理层痛点 | 中 | 说明中间件层厂商/社区感知到 VLA 部署需求 |
| **学术界工程化投入上升** | CCDC 2026、Sensors 2026、arXiv cs.RO 连续出现部署评估类论文 | 中 | 从“模型设计”向“部署评估”转移的早期信号 |

> **风险提示**：以上均为**间接推断**，缺乏融资数据库、招聘数据、GitHub Archive 等量化支撑，决策前必须补齐。

---

## 7. 信号与预测

### 7.1 早期信号汇总（有证据支撑）  
| 信号 | 来源 | 类型 | 说明 |
|------|------|------|------|
| VLA 驾驶模型架构固化为「推理 + 扩散解码器」，但**推理时注意力可控性缺失** | [7] | 算法局限 | 2026 预印本直接指证 |
| ROS2 跨 WAN 通信**已有可工作原型**（WebSocket 方案）并在真实 WAN 实测 | [12] | 工程突破 | 2026-08 预印本给出延迟/稳定性/扩展性实测数 |
| 同态加密推理在边云协同中**工程不可行**（密钥大、需交互、泄露中间值） | [14] | 负面验证 | 2026-11 同行评审期刊给出基于测量的准入评估框架 |
| 学术会议/期刊**开始系统发表 VLA/ROS2 部署优化论文**（CCDC, Sensors, arXiv cs.RO） | [13][14][12] | 社区关注点迁移 | 从纯模型创新转向工程落地评测 |

### 7.2 未来 6-18 月可验证预测（按 frontier-watch 要求写成可证伪假设）  

| # | 预测假设（可证伪） | 依据链 | 置信度 | 验证指标与截止期 |
|---|-------------------|--------|--------|------------------|
| P1 | **至 2027-06，ROS2 官方发行版（Jazzy/Kilted 后续）将合并类 ROS2 Connect 的跨 WAN 通信功能**（或发布 REP 标准化提案） | [12] 给出完整原型与实测 → 社区需求明确 → ROS 2 TSC 推进标准化 | 0.6 | 观测 ROS 2 GitHub REP 仓库、Rolling 发行版 Release Notes |
| P2 | **至 2027-03，将出现首个面向 VLA 的标准化推理基准套件（类 MLPerf Inference），包含 P50/P99 延迟、吞吐、GPU/NPU/CPU 矩阵** | [13] 显示单点优化论文出现 → [q3-open-1] 指出基准缺失 → 产业界（NVIDIA/Qualcomm/ROS Industrial）有动力主导 | 0.5 | 观测 MLPerf 官网、ROS Industrial SIG 会议记录、GitHub benchmark 仓库 |
| P3 | **至 2027-06，主流 VLA 隐私方案技术路线将从同态加密集体切向 TEE（Intel TDX/AMD SEV-SNP/ARM CCA）或联邦学习** | [14] 同行评审否定同态加密工程可行性 → 隐私需求客观存在 → TEE 硬件已量产可用 | 0.7 | 观测 arXiv cs.CR/cs.RO 新投稿关键词分布、HuggingFace Hub 模型卡标签 |
| P4 | **至 2027-12，将有 ≥3 篇第三方独立复现报告在 OpenReview/ICRA/CoRL/RSS 公开，覆盖 ≥2 个本体（双臂/灵巧手/移动操作）的 VLA 真机闭环成功率** | [q1-finding-1] 现有零独立验证 → Open X-Embodiment/Octo/OpenVLA 权重开源降低复现门槛 → 社区激励机制（RoboArena/SimplerEnv）成熟 | 0.4 | 观测 OpenReview/ICRA/CoRL/RSS 2027 投稿/录用列表、RoboArena 排行榜更新 |

### 7.3 高风险/不确定判断（必须外显）  
- **[Debated] VLA “统一动作空间”是否已成共识**：证据集零覆盖 BridgeData v2 / Open X-Embodiment 统一标准的采纳情况，无法判断是否为主流范式还是仍在争议中。  
- **[R] 传闻：某头部具身公司已在内部实现 100+ 任务 90%+ 成功率真机闭环**：证据集无任何厂商技术报告/演示视频/招聘 JD 佐证，标记为传闻待证实。  
- **[不确定] 资本热度拐点**：无融资数据，无法判断 2026 下半年是否已过“VLA 估值峰值”。  

---

## 参考来源（引用编号对照表）
[1] Overview of AuTexTification at IberLEF 2023: Detection and Attribution of Machine-Generated Text in Multiple Domains — http://arxiv.org/abs/2309.11285v1
[2] NTIRE 2025 Challenge on Image Super-Resolution (x4): Methods and Results — http://arxiv.org/abs/2504.14582v3
[3] Artificial intelligence in precision poultry farming: opportunities, challenges, and future features — https://doi.org/10.1093/af/vfag004
[4] Editorial: Narrow and general intelligence: embodied, self-referential social cognition and novelty production in humans, AI and robots — https://doi.org/10.3389/frobt.2025.1766766
[5] Multimodal Large Language Models: A Survey of Vision-Language Integration, Architectures, and Applications — https://doi.org/10.5281/zenodo.21365120
[6] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1
[7] Inference-Time Attention Steering for Vision-Language-Action Driving Models — http://arxiv.org/abs/2608.17095v1
[8] Object Detection with Multimodal Large Vision-Language Models: An In-depth Review — http://arxiv.org/abs/2508.19294v2
[9] Beyond Surface Forms: A Comprehensive, Mechanism-Oriented Taxonomy of Indirect Linguistic Encoding for LLM-Based Coded Language Detection — http://arxiv.org/abs/2606.27314v3
[10] EgoDatasets: A Dataset-Centric Survey and Taxonomy for Egocentric Vision and Action Anticipation — https://doi.org/10.20944/preprints202608.0778.v1
[11] OpenGalaxea/GalaxeaVLA: Galaxea's open-source VLA repository — https://github.com/OpenGalaxea/GalaxeaVLA
[12] ROS2 Connect: A new ROS2 over WAN Solution — http://arxiv.org/abs/2608.25102v1
[13] Study of Low-Latency Asynchronous Visual Inference on ROS2 Mobile Platform — https://doi.org/10.1109/ccdc69976.2026.11559929
[14] Beyond Latency: Deployment Assessment of Homomorphically Encrypted Inference in Sensor–Gateway–Cloud Systems — https://doi.org/10.3390/s26227289

---

*Generated by research-bot · topic=`具身智能与视觉-语言-动作vla前沿` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`nvidia/nemotron-3-ultra-550b-a55b` · sources=36 · duration=574s · 2026-11-23T02:12:11+00:00*
