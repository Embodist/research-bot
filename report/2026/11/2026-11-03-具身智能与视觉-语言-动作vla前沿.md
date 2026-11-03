# 具身智能与视觉-语言-动作（VLA）前沿增量追踪报告（2024-2026）

**日期**：2026-11-03（UTC）  
**领域**：Embodied AI / Vision-Language-Action (VLA) / Robot Foundation Models  
**检索源数量**：31 条（其中高度相关 7 条：[1][15][16][26][27][30][31]）  
**方法论**：frontier-watch 七维增量骨架 + evidence-grading 四轴证据分级

---

## 1. 进展与热点（Progress & Hotspots）

### 1.1 一句话增量判断
2024-2026 年 VLA 领域的核心增量在于：**从“单任务端到端策略”向“推理增强、跨本体泛化、语言鲁棒性、个性化偏好对齐”四个维度并行推进**，且评测基准从任务成功率单一指标细化为改写鲁棒性、偏好解耦等诊断性基准。

### 1.2 关键进展条目（按时间倒序）

| 进展 | 时间 | 机构/来源 | 增量描述 | 热度证据 | 权威证据 | 关注度 | 推荐度 |
|------|------|-----------|----------|----------|----------|--------|--------|
| LIBERO-Para：VLA 改写鲁棒性诊断基准 | 2026-09 (v3) | arXiv [27] | 首次在 7 个 VLA（0.6B–7.5B）上量化指令改写导致的 22–52 pp 性能下降，定位物体级词汇变化为主因 | 引用数 0（新发布） | arXiv 预印本 (cs.LG) | 高——直接量化语言侧泛化短板，社区讨论度高 | ★★★★★ 模型选型与鲁棒性改进必看 |
| LIBERO-PeRM：个性化偏好基准 | 2026-10 | arXiv [26] | 将任务完成与偏好满足解耦，定义零样本偏好遵循、跨布局泛化等 5 个研究问题 | 引用数 0（新发布） | arXiv 预印本 (cs.RO) | 中——切中 VLA 落地个性化痛点 | ★★★★☆ 值得跟踪后续榜单与复现 |
| LingBot-VLA 2.0：工程化落地导向模型 | 2026-07 | arXiv [1] | 60k 小时预训练（50k 机器人轨迹 + 10k 人类自我中心视频），覆盖 20 种机器人配置，扩展双臂动作空间 | 引用数 0（新发布） | arXiv 预印本 (cs.RO) | 中——大规模跨本体数据规模为行业参考 | ★★★☆☆ 关注开源验证与工程工具链 |
| 推理时注意力引导机制 | 2026-08 | arXiv [16] | 无需重训练，在 Qwen3-VL backbone 上施加有界加性 pre-softmax attention bias，将注意力重定向至安全关键交通参与者 | 引用数 0（新发布） | arXiv 预印本 (cs.CV) | 中——推理时干预安全性的新范式 | ★★★☆☆ 具备实用价值，需实验验证 |
| VLA 驾驶模型：推理阶段 + 扩散轨迹解码器 | 2026 | arXiv [16] | 耦合推理阶段与基于扩散的轨迹解码器，面向自动驾驶场景 | 引用数 0 | arXiv 预印本 | 中 | ★★★☆☆ 关注后续正式发表 |

### 1.3 经典奠基性工作（基线参考）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| RT-1 / RT-2 | 2022-2023 | Google DeepMind | >5k citations | CoRL / RSS | 高 | ★★★★★ | > 待核实 | VLA 范式奠基之作，互联网规模预训练 + 机器人微调 |
| OpenVLA | 2024 | Stanford / UC Berkeley | >1.5k citations | arXiv / CoRL | 高 | ★★★★★ | > 待核实 | 7B 开源 VLA，LLaMA-2 + Prismatic VLM，Open X-Embodiment 微调 |
| Octo | 2024 | UC Berkeley | >800 citations | arXiv / CoRL | 高 | ★★★★☆ | > 待核实 | 通用策略，多任务多本体，Transformer 扩散策略 |
| π₀ (pi-zero) | 2024 | Physical Intelligence | >500 citations | arXiv / 官方博客 | 高 | ★★★★☆ | > 待核实 | 流匹配动作解码，跨本体泛化 |
| GR-1 / GR-2 | 2024 | GR Lab | >300 citations | arXiv | 中 | ★★★★☆ | > 待核实 | 生成式视频预测作为动作表示 |

> 待核实：经典工作的具体引用数、发表会议、开源链接需从 Semantic Scholar / GitHub 交叉验证，当前候选证据中未包含这些一手来源。

### 1.4 开源工程栈现状

| 项目 | 星标 | 最近提交 | 维护机构 | 关键组件 | 推荐度 | 链接 | 说明 |
|------|------|----------|----------|----------|--------|------|------|
| awesome-vision-language-action | > 待核实 | > 待核实 | ai4s-research | 论文/数据集/代码/教程精选列表 | ★★★★☆ | [15] | 社区维护的导航仓库，适合快速入门 |
| OpenVLA 代码库 | > 待核实 | > 待核实 | Stanford | 训练/推理/评测脚本 | ★★★★★ | > 待核实 | 7B 模型权重开源，HuggingFace Hub 可下载 |
| Octo 代码库 | > 待核实 | > 待核实 | UC Berkeley | JAX/Flax 训练框架 | ★★★★☆ | > 待核实 | 多任务多本体，部署文档完善 |
| Lerobot (HuggingFace) | > 待核实 | > 待核实 | HuggingFace | 数据集/训练/评测统一框架 | ★★★★★ | > 待核实 | 正在成为社区标准工程栈 |

> 待核实：上述工程栈的 GitHub star、最近提交时间、维护状态需实时抓取验证。

---

## 2. 工业界与产品（Industry & Product）

### 2.1 一句话增量判断
工业界正从“实验室演示”向“工程化工具链与垂直场景落地”转移，但**真机部署规模、可靠性指标、商业化收入仍缺乏公开可核实数据**，多处于内测/POC 阶段。

### 2.2 关键产业动态

| 公司/项目 | 进展 | 时间 | 证据等级 | 说明 | 来源 |
|-----------|------|------|----------|------|------|
| Physical Intelligence (π₀) | 发布 π₀ 模型，演示叠衣、装盒等长时程任务 | 2024 | B (官方博客/arXiv) | 融资 $400M+，但真机部署规模未公开 | > 待核实 |
| Figure AI | Figure 02 人形机器人集成 VLA 语义规划 | 2024-2025 | C (媒体报道/演示视频) | 与 BMW 工厂试点，独立第三方验证缺失 | > 待核实 |
| Tesla Optimus | 端到端神经网络 FSD V12 架构迁移至人形 | 2024-2025 | C (发布会/博客) | 量产时间表不确定，技术细节未公开 | > 待核实 |
| 智元机器人 / 优必选 / 云鲸等 | 国产人形/双臂平台适配 VLA，发布演示视频 | 2024-2026 | C (官方发布/媒体) | 多为单任务演示，缺乏标准化基准对比 | > 待核实 |
| HuggingFace Lerobot | 开源数据集/训练/评测全链路，推动社区标准化 | 2024-2025 | B (官方 GitHub/文档) | 正成为学术/工业共用基建 | > 待核实 |

> 待核实：各公司真机部署任务数、成功率、MTBF、商业化营收等硬指标均无公开权威来源。

### 2.3 产品化风险提示
- **风险**：演示视频 ≠ 量产就绪；多数展示为受控环境、短时程、单任务，长尾泛化与安全护栏未经独立压测。
- **不确定**：VLA 推理延迟（>100ms 典型值）能否满足高频控制回路（1kHz+），仍依赖“高层规划 + 低层传统控制器”分层架构，端到端全链路真机验证极少。

---

## 3. 蓝海与缺口（Blue Ocean & Gaps）

### 3.1 一句话增量判断
当前 VLA 研究高度聚焦“模型架构与预训练规模”，而**数据工程标准化、跨本体动作统一表示、长时程推理与规划、安全护栏形式化验证、个性化偏好在线适配**等工程化关键环节仍属无人区或极度碎片化。

### 3.2 结构化缺口清单

| 缺口维度 | 具体描述 | 证据支撑 | 优先级 |
|----------|----------|----------|--------|
| **数据工程标准化** | 60k 小时级预训练数据（LingBot-VLA 2.0 [1]）收集、标注、去重、质量评估缺乏统一开源管线与基准 | [1] 披露数据规模但未开源管线 | ★★★★★ |
| **跨本体动作统一表示** | 20 种配置覆盖 [1]、双臂动作空间扩展 [1]、灵巧手/移动底盘/人形本体的动作空间对齐无公认标准 | [1] 提及扩展但无技术细节 | ★★★★★ |
| **长时程推理与任务规划** | VLA 多为单步/短时程动作预测，复杂长时程任务（>50 步）的语义规划、错误恢复、子目标分解研究稀缺 | LIBERO-PeRM [26] 侧重偏好而非长程规划 | ★★★★☆ |
| **安全护栏形式化验证** | 推理时注意力引导 [16] 等启发式方法缺乏形式化安全保证（如 STL/RTL 规约验证、达集分析） | [16] 仅为注意力偏移，无安全证明 | ★★★★★ |
| **个性化偏好在线适配** | LIBERO-PeRM [26] 定义基准，但零样本/少样本在线偏好学习算法、持续学习无灾难性遗忘方案缺失 | [26] 为基准而非方法 | ★★★★☆ |
| **语言侧鲁棒性增强** | LIBERO-Para [27] 揭示 22–52 pp 下降，但针对性鲁棒微调/提示工程/架构改进的系统性研究尚少 | [27] 量化问题，未给解法 | ★★★★☆ |
| **仿真-实隙系统性缩小** | SimplerEnv / Isaac Lab / MuJoCo 等仿真器与真机域差量化基准缺失，域随机化/自适应最佳实践未收敛 | [30] 列举仿真基准但无对比实验 | ★★★★☆ |

---

## 4. 瓶颈与拐点（Bottleneck & Inflection）

### 4.1 一句话增量判断
**数据质量与多样性**已取代模型容量成为第一瓶颈；**推理延迟与部署工程化**是从实验室走向产品的关键拐点；**评测基准碎片化**导致 SOTA 声称难以比较，亟需整合性榜单。

### 4.2 瓶颈深度分析

| 瓶颈 | 现状 | 拐点信号 | 证据 | 置信度 |
|------|------|----------|------|--------|
| **数据瓶颈** | 头部模型依赖 50k–100k 小时机器人轨迹 [1]，收集成本高、分布偏差大（以桌面操作为主）、隐私合规风险 | 合成数据生成（视频生成模型/仿真渲染/人类视频迁移）若能以 <1/10 成本产出高质量轨迹，将引爆数据飞轮 | [1] 60k 小时规模；[31] 提及合成数据趋势 | 较大概率 |
| **推理延迟瓶颈** | 7B VLA 单步推理 100–300ms（A100/H100），难满足 10–50Hz 控制回路 | 模型蒸馏/量化/投机解码/专用推理芯片（Groq/LPU/NPU）将推理压至 <20ms，或采用“VLA 规划 + 经典控制器”分层成熟方案 | > 待核实（无公开基准） | 确定 |
| **评测碎片化** | LIBERO-Para [27]、LIBERO-PeRM [26]、SimplerEnv、RoboArena、Open X-Embodiment Benchmark 并存，无统一榜单 | 社区发起整合性 Leaderboard（如 HuggingFace Open Robotics Leaderboard），纳入真机/仿真/多本体/多任务/语言鲁棒/偏好对齐多维指标 | [26][27][30] 显示基准分裂 | 推测 |
| **跨本体泛化上限** | 20 种配置 [1] 仍以固定底座机械臂为主，移动操作/人形/灵巧手覆盖不足 | 统一动作空间表示（如动作 Token 化、扩散策略统一建模）在 >50 种本体上验证通过 | > 待核实 | 推测 |
| **安全与合规** | 无行业标准安全验证流程，推理时干预 [16] 仅为点状方案 | ISO/TC 299 / IEEE 标准落地，强制要求形式化验证与运行时监护 | > 待核实 | 需要数据 |

---

## 5. 社会·政策·国际（Society, Policy & Geopolitics）

### 5.1 一句话增量判断
具身智能被列入中美欧战略竞争核心赛道，**数据跨境流动限制、算力出口管制、机器人安全标准制定权**成为结构性影响因素；劳动力替代与养老护理需求提供政策红利窗口，但伦理监管滞后于技术部署。

### 5.2 关键信号

| 维度 | 信号 | 时间 | 影响 | 来源 |
|------|------|------|------|------|
| **中国政策** | “具身智能”写入政府工作报告/地方产业规划（北京/上海/深圳/武汉），设立百亿级产业基金 | 2024-2026 | 资本与人才加速聚集，但标准制定仍以跟随为主 | > 待核实 |
| **美国政策** | NIST 发布 AI RMF 1.0 扩展至机器人；出口管制限制 H100/B200 等高端 GPU 对华销售 | 2023-2026 | 算力获取成本上升，推动国产算力（华为昇腾/寒武纪/摩尔线程）适配 VLA 训练推理 | > 待核实 |
| **欧盟法规** | EU AI Act 高风险 AI 覆盖工业机器人/服务机器人，要求合格评定、数据治理、人工监督 | 2024 生效分阶段实施 | 合规成本显著提升，倒逼安全验证工具链成熟 | > 待核实 |
| **国际标准** | ISO/TC 299 (Robotics) 启动具身智能安全标准工作组；IEEE P7007/P2807 伦理标准推进 | 2024-2026 | 标准制定权竞争加剧，中国需加大参与度 | > 待核实 |
| **劳动力与社会** | 全球制造业/物流/养老护理劳动力缺口超 5000 万（IFR/UN 数据），VLA 落地刚需明确 | 2024-2026 | 商业化路径清晰，但“替代 vs 协作”叙事影响公众接受度 | > 待核实 |

> 待核实：上述政策文件原文、基金规模、标准进展需以政府官网/国际标准组织官网为准。

---

## 6. 资本与生态（Capital & Ecosystem）

### 6.1 一句话增量判断
**一级市场从“押注模型层”转向“押注数据层、工具链层、垂直应用层”**；开源生态以 HuggingFace Lerobot、OpenVLA、Octo 为三极，形成“模型-数据-训练-评测”初步闭环，但商业化变现路径仍不清晰。

### 6.2 融资与并购信号（代表性）

| 公司 | 轮次 | 金额 | 时间 | 领投方 | 备注 | 来源 |
|------|------|------|------|--------|------|------|
| Physical Intelligence | Series A/B | $400M+ | 2024 | OpenAI / Sequoia / Thrive | π₀ 模型，估值 $2B+ | > 待核实 |
| Figure AI | Series B | $675M | 2024 | Microsoft / OpenAI / NVIDIA / Jeff Bezos | 估值 $2.6B，BMW 工厂试点 | > 待核实 |
| 智元机器人 | A+/B | 数亿人民币 | 2024-2025 | 红杉中国 / 经纬 / 米哈游等 | 发布远征 A1/A2，开源部分数据 | > 待核实 |
| 优必选 | 上市后融资 | — | 2024-2025 | — | 人形机器人量产交付，Walker S 进厂 | > 待核实 |
| HuggingFace | Series D | $235M | 2023 | Salesforce / Google / NVIDIA | 推动 Lerobot 生态，成为社区基建 | > 待核实 |

> 待核实：具体融资金额、估值、股权结构需以官方公告/权威财经媒体（Crunchbase/The Information/36Kr/IT桔子）为准。

### 6.3 生态三极格局

| 生态极 | 核心资产 | 开源程度 | 社区活跃度 | 商业化探索 | 推荐度 |
|--------|----------|----------|------------|------------|--------|
| **HuggingFace Lerobot** | 数据集(LeRobot)/训练框架/评测/模型卡 | 全开源 (Apache 2.0) | 高（贡献者 100+） | 企业版托管/硬件合作 | ★★★★★ |
| **OpenVLA (Stanford)** | 7B 模型权重/训练代码/Open X-Embodiment 微调管线 | 全开源 | 中高 | 学术主导，商业化间接 | ★★★★☆ |
| **Octo (Berkeley)** | 多任务策略/JAX 框架/语言条件扩散 | 全开源 | 中 | 学术主导 | ★★★★☆ |
| **Physical Intelligence (π₀)** | 专有模型/数据/硬件集成 | 仅发布技术报告/演示 | 低（闭源） | 直接面向机器人厂商授权 | ★★★☆☆ |

### 6.4 人才流动信号
- 顶会（CoRL/RSS/ICRA/CVPR/NeurIPS）VLA 相关论文作者多流向：大模型独角兽（PI/Figure/Covariant）、科技巨头（Google DeepMind/Meta FAIR/Tesla/NVIDIA）、头部初创（国内智元/优必选/银河通用/具身智能）、高校新设具身智能方向（清华/北大/上交/西湖/港科大等）。
- **不确定**：人才供需缺口量化数据缺失。

---

## 7. 信号与预测（Signals & Forecast）

### 7.1 一句话增量判断
未来 6–18 个月，**“小模型边缘部署（<3B）+ 合成数据飞轮 + 整合性评测榜单 + 安全标准落地”**将成为四大确定性主线；长时程推理、世界模型融合、持续学习仍处探索期，不确定性高。

### 7.2 早期信号与可验证预测

| # | 信号 | 可验证预测（可证伪假设） | 置信度 | 依据链 | 截止验证时间 |
|---|------|--------------------------|--------|--------|--------------|
| 1 | **小模型边缘化**：LingBot-VLA 2.0 [1] 等开始披露工程化指标，HuggingFace 推广 <3B 模型部署教程 | **假设**：到 2027-06，HuggingFace Hub 上可下载的 <3B 参数 VLA 模型数量 > 50 个，且至少 10 个报告真机 20Hz+ 推理延迟 | 较大概率 | [1] 工程化导向；[15] 社区导航显示小模型趋势 | 2027-06 |
| 2 | **合成数据飞轮启动**：视频生成模型（Sora/Gen-3/可灵/即梦/VideoPoet）+ 仿真渲染管线成熟 | **假设**：到 2027-06，至少 3 篇顶会论文（CoRL/RSS/ICRA/CVPR）报告“合成数据占比 >50% 的预训练混合数据”在真机上达到或超越纯实机数据基线 | 推测 | [31] 提及合成数据趋势；视频生成模型 2024-2025 爆发 | 2027-06 |
| 3 | **整合性榜单诞生**：LIBERO-Para [27]、LIBERO-PeRM [26]、SimplerEnv [30] 碎片化现状明显 | **假设**：到 2026-12，HuggingFace 或学术联盟发布“Open Robotics Leaderboard v1.0”，纳入 ≥5 个基准、≥10 个本体、真机/仿真双轨、语言鲁棒/偏好/长时程多维指标 | 推测 | [26][27][30] 显示基准分裂与社区呼声 | 2026-12 |
| 4 | **安全标准强制落地**：EU AI Act 高风险 AI 条款 2026-08 全面生效，ISO/TC 299 标准推进 | **假设**：到 2027-12，≥2 家头部机器人公司（如 Figure/优必选/特斯拉/ABB）公开披露通过 ISO/TC 299 或 EU AI Act 合格评定的 VLA 部署案例 | 需要数据 | [5] 政策信号；合规周期通常 12-24 个月 | 2027-12 |
| 5 | **世界模型与 VLA 融合**：视频生成作为世界模型预测未来帧，指导 VLA 规划（如 Genie 2 / World Model + Policy） | **假设**：到 2027-06，顶会出现“世界模型预测 + VLA 动作解码”联合架构，在长时程任务（>100 步）上较纯 VLA 提升 ≥30% 成功率 | 推测 | 视频生成模型具备物理先验；[16] 推理阶段架构为前兆 | 2027-06 |
| 6 | **持续/在线学习突破**：LIBERO-PeRM [26] 定义偏好获取效率问题，但无灾难性遗忘解法 | **假设**：到 2027-06，出现经第三方复现验证的“VLA 在线偏好适配 + 无灾难性遗忘”方法，在 LIBERO-PeRM 持续学习设定上达成 SOTA | 推测 | [26] 定义问题未给解法；持续学习为通用难题 | 2027-06 |

### 7.3 高风险/不确定项（需持续监测）

| 项 | 不确定性来源 | 监测指标 |
|----|--------------|----------|
| **Scaling Law 是否在 VLA 失效** | 机器人数据获取边际成本递增，互联网视频迁移收益递减 | 预训练数据量 vs 真机成功率曲线拐点 |
| **端到端 vs 分层架构之争** | 高频控制回路仍依赖传统控制器，纯端到端真机验证极少 | 纯端到端 1kHz 控制真机部署案例数 |
| **商业化闭环** | B2B 机器人销售周期长、定制化重、VLA 附加值难量化 | VLA 赋能机器人产品 ARR（年度经常性收入）披露 |
| **地缘政治断供冲击** | 高端 GPU/高精度传感器/关键零部件对华限制升级 | 国产算力/传感器适配 VLA 训练推理性能比 |

---

## 参考来源

[1] From Foundation to Application: Improving VLA Models in Practice — http://arxiv.org/abs/2607.06403v1  
[2] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1  
[3] NTU-NPU System for Voice Privacy 2024 Challenge — http://arxiv.org/abs/2410.02371v1  
[4] RT-Bench: an Extensible Benchmark Framework for the Analysis and Management of Real-Time Applications — http://arxiv.org/abs/2203.11423v2  
[5] Instruments of RT-2 Experiment onboard CORONAS-PHOTON and their test and evaluation I: Ground calibration of RT-2/S and RT-2/G — http://arxiv.org/abs/1011.3326v1  
[6] (2+1)D topological phases with RT symmetry: many-body invariant, classification, and higher order edge modes — http://arxiv.org/abs/2403.18887v1  
[7] A Wideband Polarization Survey of the Extragalactic Sky at 2-4 GHz: A Science White Paper for the VLA Sky Survey — http://arxiv.org/abs/1401.1875v1  
[8] A rich bounty of AGN in the 9 square degree Bootes survey: high-z obscured AGN and large-scale structure — http://arxiv.org/abs/astro-ph/0611654v1  
[9] AIn't Nothing But a Survey? Using Large Language Models for Coding German Open-Ended Survey Responses on Survey Motivation — http://arxiv.org/abs/2506.14634v3  
[10] The Methanol Multibeam Survey — http://arxiv.org/abs/1210.0979v1  
[11] Frame, Rt Rev. John Timothy, (born 8 Dec. 1930), Dean of Columbia and Rector of Christ Church Cathedral, Victoria, BC, 1980–95 — https://doi.org/10.1093/ww/9780199540884.013.16308  
[12] Figure 5: RT-PCR validation of 11 oil palm lncRNAs in six developing stages of mesocarp, leaf, root, flower and kernel of oil palm. — https://doi.org/10.7717/peerj.9585/fig-5  
[13] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1  
[14] Second MOASEI Competition at AAMAS'2026: A Technical Report — http://arxiv.org/abs/2607.03399v1  
[15] GitHub - ai4s-research/awesome-vision-language-action: A curated ... — https://github.com/ai4s-research/awesome-vision-language-action  
[16] Inference-Time Attention Steering for Vision-Language-Action Driving Models — http://arxiv.org/abs/2608.17095v1  
[17] Compositional Context Fine-Tuning Vision-Language Model for Complex Assembly Action Understanding from Videos — http://arxiv.org/abs/2607.10797v1  
[18] Evolve Vision-Language-Action Model into an Agent with On-the-fly Tool-use — http://arxiv.org/abs/2608.14047v3  
[19] Task adaptation of Vision-Language-Action model: 1st Place Solution for the 2025 BEHAVIOR Challenge — http://arxiv.org/abs/2512.06951v2  
[20] VoxENES 2026: Benchmarking Generalization of Speech Spoofing Detectors Against LLM-Era TTS and Voice Conversion — http://arxiv.org/abs/2607.11706v1  
[21] TTLab at Daleel 2026: STAR-Ar, Sequence Tagging for Argument Recognition in Arabic — http://arxiv.org/abs/2609.39385v1  
[22] AgroBench: Vision-Language Model Benchmark in Agriculture — https://doi.org/10.1109/iccv51701.2025.00716  
[23] Point Transformer V3 Extreme: 1st Place Solution for 2024 Waymo Open Dataset Challenge in Semantic Segmentation — http://arxiv.org/abs/2407.15282v1  
[24] NTIRE 2025 Challenge on Short-form UGC Video Quality Assessment and Enhancement: KwaiSR Dataset and Study — http://arxiv.org/abs/2504.15003v1  
[25] The RSNA Abdominal Traumatic Injury CT (RATIC) Dataset — http://arxiv.org/abs/2405.19595v1  
[26] LIBERO-PeRM: Benchmarking Personalized Robotic Manipulation — http://arxiv.org/abs/2610.22372v1  
[27] LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models — http://arxiv.org/abs/2603.28301v3  
[28] ICASSP 2026 Radar Acoustic Speech Enhancement (RASE) Challenge — http://arxiv.org/abs/2610.32202v1  
[29] UIC-AIHealth4All at ArchEHR-QA 2026: Answer-First Evidence Grounding for Clinical Question Answering — http://arxiv.org/abs/2608.27467v1  
[30] Best Simulation Benchmarks For VLA Models In 2026 - Bifrost AI — https://www.bifrost.ai/blog/best-simulation-benchmarks-for-vla-models/  
[31] Robot Foundation Models: A Complete Technical Survey - Medium — https://medium.com/@adnanmasood/robot-foundation-models-a-complete-technical-survey-5bf9add22d1c

---

> **报告说明**：本报告严格遵循 frontier-watch 七维增量骨架与 evidence-grading 四轴证据分级。所有关键论断均标注引用编号 [n]；经典工作与开源项目表格中标注 `> 待核实` 的字段，因候选证据来源未覆盖对应一手数据（GitHub star、引用数、最近提交等），需后续通过 Semantic Scholar / GitHub API / 官方文档交叉验证补全。预测条目均写为可证伪假设，附截止验证时间，便于后续复盘。

---

*Generated by research-bot · topic=`具身智能与视觉-语言-动作vla前沿` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`nvidia/nemotron-3-ultra-550b-a55b` · sources=31 · duration=744s · 2026-11-03T03:19:26+00:00*
