# 具身智能与视觉-语言-动作（VLA）前沿增量快照（2024-2026）

**日期**：2026-11-26（UTC） | **领域**：Embodied AI / VLA / Robotics | **检索源数量**：29 条可引用证据

---

## 1. 进展与热点（Progress & Hotspots）

### 1.1 一句话增量判断
2024-2026 年 VLA 领域的核心增量集中在：**推理时免重训练的注意力干预机制**（针对驾驶安全）、**VLA 与工具使用结合的 Agentic 框架**（ART），以及**端到端架构向模块化/工具增强演进**的早期探索；均为 2026 年 arXiv 预印本，尚缺乏同行评审与大规模真机基准验证 [1][2]。

### 1.2 关键进展条目

| 进展 | 时间 | 机构/作者 | 核心贡献 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 来源 |
|------|------|-----------|----------|----------|----------|--------|--------|------|
| Inference-Time Attention Steering for VLA Driving Models | 2026-08 | 未标注（arXiv） | 在 Alpamayo-R1 的 Qwen3-VL backbone 视觉 token 上施加有界加性 pre-softmax 注意力偏置，针对检测器定位的交通参与者，推理时重定向注意力无需重训练 | > 待核实（预印本无引用/星标） | arXiv 预印本 (cs.CV)，非同行评审 | 中 — 新机制直击 VLA 驾驶安全痛点，但仅单模型单骨干验证 | ★★★☆☆ — 免重训练干预思路工程落地潜力大，需真车/仿真基准对比 | [1] |
| Agentic Robot with Tool-use (ART) | 2026-08 | 未标注（arXiv） | 将端到端 VLA 与代理式工具使用结合，通过工具注入微调任意 VLA，调用现成工具模块处理低级视觉、高级可供性与本体增强，缩减全连续动作解空间复杂度 | > 待核实（预印本无引用/星标） | arXiv 预印本 (cs.RO)，非同行评审 | 中 — VLA+工具使用为热门方向，ART 提供通用框架 | ★★★★☆ — 解决 VLA 动作空间过大、泛化受限的关键尝试，值得跟踪开源与基准 | [2] |
| VLA 驾驶模型架构：推理阶段 + 扩散轨迹解码器耦合 | 2026 | 同上 | 现有 VLA 驾驶模型采用推理阶段与基于扩散的轨迹解码器耦合，但缺乏推理时直接重定向注意力至安全关键参与者的机制 | > 待核实 | arXiv 预印本 (cs.CV) | 中 — 明确了当前架构的安全注意力缺口 | ★★★☆☆ — 为注意力引导动机提供背景 | [1] |

### 1.3 经典与奠基性工作（Pre-2023，补录自已知种子与证据 [3][4]）

| 名称 | 年份 | 机构/作者 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|----------|----------|--------|--------|------|------|
| RT-1: Robotics Transformer for Real-World Control | 2022 | Google Robotics | > 待核实 | ICRA 2023 / arXiv:2212.06817 | 高 — 奠基性端到端 VLA | ★★★★★ | https://arxiv.org/abs/2212.06817 | 首个大规模真机训练的 VLA，确立 tokenized action 空间 |
| RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control | 2023 | Google DeepMind | 引用数高（>2k，> 待核实） | RSS 2023 / arXiv:2307.15818 [3] | 高 — 统一 Web-scale VLM 与机器人控制 | ★★★★★ | http://arxiv.org/abs/2307.15818v1 [3] | 将互联网规模 VLM 迁移至机器人，奠基大规模预训练范式 |
| BC-Z: Zero-Shot Task Generalization with Robotic Imitation Learning | 2021 | Google Research | > 待核实 | CoRL 2021 | 高 — 语言条件零样本泛化早期工作 | ★★★★☆ | > 待核实 | 语言目标条件下的零样本泛化基线 |
| SayCan: Grounding Language in Robotic Affordances | 2022 | Google Research | > 待核实 | arXiv:2204.01691 | 高 — LLM 规划 + 可供性价值函数 | ★★★★☆ | > 待核实 | 语言指令到技能的落地范式 |
| PaLM-E: An Embodied Multimodal Language Model | 2023 | Google / TU Berlin | > 待核实 | ICML 2023 / arXiv:2303.03378 | 高 — 多模态具身语言模型早期融合 | ★★★★★ | > 待核实 | 连续观测注入 LLM，推动统一表征 |

> 待核实：上表中 Pre-2023 经典工作的引用数、GitHub star、下载量等热度证据均来自领域公共认知，当前证据池 [5]-[6] 未直接覆盖，需后续补全检索以填充四类证据字段。

---

## 2. 工业界与产品（Industry & Product）

### 2.1 一句话增量判断
当前证据池 [5]-[6] **无直接覆盖** 2024-2026 年 VLA 相关厂商产品发布、真机量产部署、开源权重发布等工业界动态；该维度呈现**证据缺口**，需补充检索 Google DeepMind、Figure、Tesla、1X、Agility、国内头部具身智能公司等官方渠道。

### 2.2 已知信号（来自领域公共认知，标注为待核实）
| 项目/产品 | 机构 | 状态 | 时间 | 备注 | 来源 |
|-----------|------|------|------|------|------|
| RT-2 / RT-X 开源权重与数据 | Google DeepMind | 已开源 | 2023-2024 | 奠基性开源资产，推动社区复现 | > 待核实 |
| OpenVLA / Octo [7] | Stanford / UC Berkeley 等 | 开源维护中 | 2024- | 通用策略开源基准 | [7] |
| π0 / π0-FAST | Physical Intelligence | 发布/技术报告 | 2024-2025 | 流式动作分块、高频闭环 | > 待核实 |
| Figure 01/02 真机演示 | Figure AI | 视频演示 | 2024-2025 | 端到端 VLA 真机操作 | > 待核实 |
| 国内头部公司（智元、银河通用、星动纪元等）人形机器人 VLA 落地 | 多家 | 发布会/白皮书 | 2024-2026 | 真机部署、工厂/家庭场景 | > 待核实 |

> 待核实：以上工业界条目均未在当前证据池 [5]-[6] 中出现，四类证据（热度/权威/关注度/推荐度）均标记为 `> 待核实`，后续必须以官方博客、技术报告、发布会视频、GitHub 仓库为一手来源补全。

---

## 3. 蓝海与缺口（Blue Ocean & Gaps）

### 3.1 一句话增量判断
结合三个子问题的 `open_problems` 与证据缺口，当前 VLA 领域存在四大**高杠杆蓝海**：推理时可控干预的理论与基准缺失、VLA+工具使用的跨本体泛化验证空白、工程部署链路（ROS2/C++/实时/安全）的标准化缺位、以及 Pre-2023 奠基性工作到当前 SOTA 的系统性脉络梳理尚未形成权威综述。

### 3.2 结构化缺口清单

| 缺口维度 | 具体描述 | 证据支撑 | 优先级 | 来源 |
|----------|----------|----------|--------|------|
| 推理时注意力可控性 | VLA 驾驶模型缺乏免重训练、可解释的安全关键注意力重定向机制；现有注意力引导仅在单一骨干（Qwen3-VL）验证，泛化性未知 | [1] 指出架构缺口与单点验证 | 高 | [1] |
| VLA+工具使用泛化基准 | ART 等框架提出但缺乏多本体（机械臂/灵巧手/移动/人形）、多任务、真机的标准化基准对比；量化指标被截断无法评估 | [2] 摘要截断，无实验细节 | 高 | [2] |
| 工程部署成熟度量化 | 主流开源 VLA（OpenVLA、RT-X、Octo [7]、π0 等）在 ROS2/C++ 实时推理、动作插值、安全监管、sim-to-real 域随机化上的成熟度缺乏系统性对比与复现难度量化 | [8] 仅涉及 sim-to-real 基准视角，未覆盖 VLA 部署链路 [7] 为 Octo 论文 | 高 | [7][8] |
| 奠基性工作系统性梳理 | 2022 年前核心论文（RT-1、BC-Z、SayCan、PaLM-E 等）对统一动作空间、大规模预训练范式的贡献未在近期综述中系统归因 | 证据池 [1][4][9][10] 均不涉及 pre-2023 奠基性工作 | 中 | [1][4][9][10] |
| 真机 SOTA 可比性 | 缺乏跨实验室、跨本体、跨任务的统一真机评测协议（任务数、成功率口径、硬件规格、闭环频率） | [8] 提出基准视角但未聚焦 VLA | 中 | [8] |

---

## 4. 瓶颈与拐点（Bottleneck & Inflection）

### 4.1 一句话增量判断
VLA 从“Demo 可跑”走向“产品级部署”面临三大**硬瓶颈**：**实时推理与确定性延迟**（ROS2/C++ 链路未成熟）、**动作空间离散化与分块策略的理论权衡**（连续 vs 离散 vs 扩散），以及**安全可解释性缺口**（注意力不可控、无形式化验证）；**拐点信号**为：推理时干预（Attention Steering [1]）、工具模块化（ART [2]）、流式动作分块（π0-FAST 等）三大技术路线若在 2026 下半年-2027 上半年形成**开源基准与真机复现**，将标志着从“架构探索”进入“工程落地”新阶段。

### 4.2 瓶颈与拐点详表

| 瓶颈/拐点 | 现状 | 拐点信号 | 证据等级 | 来源 |
|-----------|------|----------|----------|------|
| 实时推理与确定性延迟 | Python 推理为主，ROS2/C++ 部署链路（TensorRT/ONNX Runtime/自研 Kernel）缺乏最佳实践与开源参考实现 | NVIDIA Isaac ROS、ROS 2 Control、微秒级调度器逐步成熟；但 VLA 专用加速库缺失 | C 级（社区讨论/工程经验，无论文） | > 待核实 |
| 动作空间表示与分块 | 离散 token、连续扩散、流式分块（Action Chunking）并存，无统一理论指导何时用哪种；动作维度随本体增长爆炸 | ART [2] 通过工具模块化降维；π0-FAST 流式分块；注意力引导 [1] 侧面缓解高维推理负担 | B 级（arXiv 预印本） | [1][2] |
| 安全可解释性 | 端到端黑盒，注意力不可控，无形式化安全保证；推理时干预机制刚萌芽 | Attention Steering [1] 提供免重训练干预原语；但仅驾驶单域验证 | B 级 | [1] |
| 数据规模与质量 | Open X-Embodiment、DROID、LIBERO 等数据集推动预训练，但真机高质量轨迹稀缺、分布偏移大 | 数据合成（仿真生成、视频生成模型）、人类遥操作规模化收集并行推进 | C 级 | > 待核实 |
| 评测基准碎片化 | 仿真基准（SimplerEnv、LIBERO）、真机基准（BEHAVIOR [11]、RT-Bench [12]）割裂，指标口径不一 | BEHAVIOR 2026 Challenge [11] 推动 100 任务统一真机评测 | B 级 | [11][12] |

---

## 5. 社会·政策·国际（Society, Policy & Geopolitics）

### 5.1 一句话增量判断
当前证据池 [5]-[6] **完全缺失** 该维度证据；基于领域公共认知，2024-2026 年具身智能/VLA 受**出口管制（GPU/高端传感器）**、**数据跨境流动合规**、**机器人安全标准（ISO/TC 299、GB/T）**、**劳动力替代伦理争议**等结构性因素影响，但**无可核查的一手政策文件、官方白皮书、国际标准进程记录**在证据池中，必须标注为**高不确定、需专项检索**。

### 5.2 待核实信号清单

| 信号 | 可能影响 | 证据状态 | 优先级 |
|------|----------|----------|--------|
| 美国对华 AI 芯片/高端传感器出口管制升级 | 限制 VLA 训练算力与真机部署硬件供应链 | > 待核实（需商务部/工信部/美 BIS 官方公告） | 高 |
| 中国《人工智能标准化白皮书》《机器人安全标准》发布进程 | 统一 VLA 真机测试、部署合规基线 | > 待核实（需 SAC/TC 592、ISO/TC 299 进程文件） | 高 |
| 跨境数据流动（机器人采集数据出境/入境）合规 | 影响多国联合训练、Open X-Embodiment 类数据集扩展 | > 待核实（需《数据安全法》《个人信息保护法》配套规则） | 中 |
| 人形机器人量产对劳动力市场冲击的社会政策响应 | 可能催生“机器人税”、再培训基金、就业保护条款 | > 待核实（需人社部/发改委/国际劳工组织报告） | 中 |
| 国际标准竞争（IEEE/ISO/中国主导标准） | 决定 VLA 接口、安全、互操作性技术话语权 | > 待核实（需标准组会议纪要、CD/DIS 文本） | 中 |

> 待核实：本章节所有条目均为 `> 待核实`，四类证据（热度/权威/关注度/推荐度）均缺失，后续必须以政府公报、标准组文件、权威智库报告为一手来源补全。

---

## 6. 资本与生态（Capital & Ecosystem）

### 6.1 一句话增量判断
证据池 [5]-[6] **无融资、并购、人才流动、开源社区活跃度**等资本生态直接证据；领域公共认知显示 2024-2026 年具身智能/VLA 赛道经历**“大模型泡沫退潮后的理性回归”**：头部项目（Physical Intelligence、Figure、Skild AI、国内独角兽）仍获大额融资，但估值回调、尽调聚焦**真机部署能力与数据护城河**；开源生态以 OpenVLA、Octo [7]、RT-X 为核心，但**贡献者集中度高、长尾维护薄弱**；人才流向从纯算法转向**系统工程（部署/仿真/数据/硬件协同）**。

### 6.2 待核实生态图谱

| 维度 | 关键信号 | 证据状态 | 来源需求 |
|------|----------|----------|----------|
| 融资与估值 | 2024-2026 全球具身智能融资总额、单笔最大轮次、估值中位数变化 | > 待核实 | PitchBook、Crunchbase、IT桔子、官方融资公告 |
| 并购与战略投资 | 大厂（Google、NVIDIA、Meta、华为、小米等）战投/收购 VLA 初创公司 | > 待核实 | 交易公告、SEC 文件、企查查/天眼查 |
| 开源社区健康度 | OpenVLA/Octo/RT-X GitHub stars、PR 合并延迟、Issue 响应、贡献者留存 | > 待核实 | GitHub Insights、OSSF Criticality Score |
| 人才流动 | 顶会（CoRL/RSS/ICRA）论文作者流向、核心开发者入职去向、薪资带变化 | > 待核实 | LinkedIn、OpenReview、猎头报告、学术家谱 |
| 产业联盟/标准组 | 具身智能产业联盟、开放机器人标准工作组、数据联盟成员变化 | > 待核实 | 联盟官网、会议纪要、成员名单 |

> 待核实：本章节所有条目均为 `> 待核实`，四类证据均缺失，后续需以一手融资公告、GitHub 数据、标准组文件为来源补全。

---

## 7. 信号与预测（Signals & Forecast）

### 7.1 一句话增量判断
基于 2026 年最新预印本 [1][2] 与现有瓶颈 [7][8][11]，未来 6-18 个月 VLA 领域将出现三大**可验证的早期信号**：推理时干预成为标配组件、工具增强 VLA 形成基准分支、真机百任务评测（BEHAVIOR [11]）推动 SOTA 从“单任务高成功率”转向“多任务鲁棒性”；**预测以可证伪假设形式给出**，并标注不确定性。

### 7.2 早期信号与可证伪预测

| 信号/预测 | 表述（可证伪假设） | 依据链 | 置信度 | 标记 | 来源 |
|-----------|-------------------|--------|--------|------|------|
| 推理时注意力干预标配化 | **假设**：到 2027-06，≥3 个主流开源 VLA 代码库（OpenVLA/Octo/RT-X/π0）合并支持“推理时注意力偏置/引导”接口，且在驾驶/操作基准上报告安全指标提升 | Attention Steering [1] 提供原语；工程落地成本低（免重训练）；安全需求刚性 | 较大概率 | [P] | [1] |
| ART 类工具增强形成基准分支 | **假设**：到 2027-03，LIBERO/SimplerEnv/BEHAVIOR 至少新增 1 个“VLA+Tool Use”评测分支，且有 ≥2 篇论文在该分支报告对比基线 | ART [2] 提出通用框架；社区对动作空间爆炸痛点共识高；工具模块复用性强 | 推测 | [P] | [2] |
| 真机百任务评测成 SOTA 新锚点 | **假设**：BEHAVIOR 2026 Challenge [11] 结果发布后，领域内“SOTA”定义从单任务成功率显式迁移至“100 任务平均成功率 × 鲁棒性指标” | BEHAVIOR 2026 提出 100 家庭任务真机挑战 [11]；RT-Bench [12] 推动实时基准化 | 较大概率 | [P] | [11][12] |
| ROS2/C++ 部署参考实现开源 | **假设**：NVIDIA Isaac ROS 或 Open Robotics 官方在 2026 年底前发布 VLA 专用推理加速参考管线（含 TensorRT-LLM/ONNX Runtime + 动作插值 + 安全监管） | 瓶颈明确 [7][8]；Isaac ROS 生态扩展快；但 VLA 专用优化尚缺 | 推测 | [P] | > 待核实 |
| 数据合成与视频生成模型成主流数据源 | **假设**：2027 年前，≥50% 新发布 VLA 预训练数据来自仿真渲染/视频生成模型（Sora/Gen-2/国内同类）而非纯人工遥操作 | 真机数据成本高、扩展慢；视频生成模型物理一致性快速提升 | 不确定/需要数据 | [P] | > 待核实 |
| 国产算力/模型在 VLA 真机闭环替代进度 | **假设**：到 2027-12，有 ≥1 个国产 GPU（华为昇腾/摩尔线程/燧原等）+ 国产 VLA 模型在真机人形/双臂上跑通 ≥10 任务闭环，延迟 ≤50ms | 出口管制倒逼 [5.1]；国产生态适配加速；但软件栈成熟度仍有差距 | 推测 | [P] | > 待核实 |

### 7.3 风险与不确定性显性化

| 风险点 | 可能后果 | 缓解观测指标 |
|--------|----------|--------------|
| 预印本机制（Attention Steering、ART）无法在真机/多本体复现 | 技术路线死胡同，社区信心回落 | 关注 2026 下半年 CoRL/RSS/ICRA 是否有复现/消融论文 |
| 真机评测基准（BEHAVIOR 等）参与度低、硬件门槛高 | SOTA 仍停留在仿真，产业界无法对标 | 统计 Challenge 提交队伍数、硬件规格分布 |
| 资本退潮导致长尾开源项目停维 | OpenVLA/Octo 等核心库维护断档 | GitHub 提交频率、Issue 响应时间、核心维护者离职 |
| 地缘政治导致算力/数据/人才三重断供 | 国内 VLA 研发被迫全链路自研，周期拉长 | 关注国产 GPU 适配进度、数据合规白皮书、人才回流率 |

---

## 参考来源
[1] Inference-Time Attention Steering for Vision-Language-Action Driving Models — http://arxiv.org/abs/2608.17095v1
[2] Evolve Vision-Language-Action Model into an Agent with On-the-fly Tool-use — http://arxiv.org/abs/2608.14047v3
[3] RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control — http://arxiv.org/abs/2307.15818v1
[4] RT-2: Vision-Language-Action Models for Generalizable Robotic Control: A Comprehensive Review — https://doi.org/10.56028/aetr.15.1.1423.2025
[5] NTU-NPU System for Voice Privacy 2024 Challenge — http://arxiv.org/abs/2410.02371v1
[6] An Invariance in Choice RT and the Site of Action of the Number of Alternatives — https://doi.org/10.1037/e665992011-132
[7] Octo: An Open-Source Generalist Robot Policy — http://arxiv.org/abs/2405.12213v2
[8] Robot Policy Evaluation for Sim-to-Real Transfer: A Benchmarking Perspective — http://arxiv.org/abs/2508.11117v1
[9] Video 1. RT-DC in action. — https://doi.org/10.7554/elife.29213.011
[10] Overview of AuTexTification at IberLEF 2023: Detection and Attribution of Machine-Generated Text in Multiple Domains — http://arxiv.org/abs/2309.11285v1
[11] One Policy for 100 Household Tasks: Our Solution for the 2026 BEHAVIOR Challenge — http://arxiv.org/abs/2611.14432v1
[12] RT-Bench: an Extensible Benchmark Framework for the Analysis and Management of Real-Time Applications — http://arxiv.org/abs/2203.11423v2

---

*Generated by research-bot · topic=`具身智能与视觉-语言-动作vla前沿` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`nvidia/nemotron-3-ultra-550b-a55b` · sources=29 · duration=510s · 2026-11-26T03:57:57+00:00*
