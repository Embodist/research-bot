# 具身智能与视觉-语言-动作（VLA）前沿增量调研（2024–2026）

**日期**：2026-10-18（UTC）｜**领域**：Embodied AI / Vision-Language-Action（VLA）/ 机器人操作与导航｜**检索源数量**：31 条候选来源（其中与 VLA/具身智能**直接相关 14 条**、相邻领域 4 条、主题无关噪声 13 条）｜**方法**：七维增量骨架（frontier-watch）+ 证据分级（evidence-grading）+ 论文图谱（paper-survey）

> **证据基座与检索偏差声明（必读）**
> 本次可用来源池 [1]–[31] 存在严重的**召回漂移**：13 条为短视频参与度、图像超分、生成图像检测、法律问答、REST API 测试、多智能体竞赛等完全无关主题（如 [1][3][4][5][14][15][23][30][31]）。因此本报告的**大量已知关键条目（OpenVLA、π0/π0.5、GR00T、RDT、Diffusion Policy、Open X-Embodiment、DROID、LIBERO、SimplerEnv、RoboArena、CALVIN、LeRobot、ACT/ALOHA）在本次来源池中没有任何可引用条目**，一律标注 `> 待核实`，且**不提供链接、不提供数字**。本报告的价值在于：把"已确证增量"与"证据缺口"严格分开，而不是用记忆填补空白。
> 另注：[7] 为已撤稿条目（withdrawn），按 evidence-grading 的 E 级规则丢弃。

---

## 1. 进展与热点（Progress & Hotspots）

**一句话增量判断**：相对 2023 年 RT-2 奠定的"VLM + 动作 token"范式 [12]，2024–2026 年的真实增量集中在**四个方向**——动作表征/动作 tokenizer 的语义化 [11]、长程任务与长程导航 [26][27]、**失败模式与反事实鲁棒性**被单独列为研究对象 [28]、以及**推理时/低资源部署**优化 [6][20]；但**没有任何一条来源提供主流基准上的 SOTA 数字**，因此"谁刷新了 SOTA"在本批证据下**不可回答**。

### 1.1 时间线增量（按年份-季度，含证据强度）

| 时间 | 条目 | 机构/作者 | 一句话增量 | 证据强度 |
|---|---|---|---|---|
| 2023-07 | RT-2 [12] | 候选块未提供作者字段，公开记录为 Google DeepMind `> 待核实` | 奠基：主张把 web 规模的视觉-语言知识**迁移到机器人控制**，确立 VLA 术语与范式 | B（arXiv 预印本）[12] |
| 2024-07 | Aligning Cyber Space with Physical World（Embodied AI 综述，v8）[22] | `> 待核实` | 把具身智能整体版图（含 VLA）系统化，是理解"承上启下"的分类骨架 | B（综述预印本）[22] |
| 2025-08 | Survey of VLA Models for Embodied Manipulation [21] | `> 待核实` | VLA 领域**专门的分类学综述**，可作为检索主流模型与基准的入口 | B（综述预印本）[21] |
| 2025-08 | Long-VLA [26] | `> 待核实` | 明确以"释放 VLA 的**长程**能力"为目标，把长程从隐含缺陷变为显式设计对象 | B [26] |
| 2025-12 | BLURR [20] | `> 待核实` | 面向 VLA 的**低资源推理**加速，把部署成本问题前置为一等方法问题 | B [20] |
| 2025-12 | BEHAVIOR Challenge 2025 冠军方案（任务适配）[19] | `> 待核实` | 以**竞赛冠军技术报告**形式给出 VLA 任务适配方案，属"竞赛自评"级证据 | B/C（竞赛技术报告）[19] |
| 2026-02 | LongNav-R1 [27] | `> 待核实` | 把**多轮 RL + 自适应视界**用于长程 VLA 导航，长程问题从操作扩展到导航 | B [27] |
| 2026-02 | When Vision Overrides Language [28] | `> 待核实` | 首次（在本批证据内）把 VLA 的**反事实失败**（视觉压倒语言指令）作为独立评测与缓解对象 | B [28] |
| 2026-05 | Embodied AI in Action（SAE World Congress 2026 白皮书）[24] | `> 待核实` | 行业会议层面把 safety / trust / governance / operational reliability 列为一等议题 | B（会议白皮书，非同行评审）[24] |
| 2026-06 | X-Tokenizer [11] | `> 待核实` | 指出既有动作 tokenizer **只为重建而离散化**、语义监督弱，提出多模态动作 tokenizer | B [11] |
| 2026-06 | Learning to Fold（LeHome Challenge 2026）[16] | `> 待核实`（候选块未列作者，正文称单作者） | **策略即价值函数**：同一网络同时预测动作与成功/进度，用 RL 回路自提升 VLA；ICRA 2026 双臂折衣**在线（仿真）轮 1/62、真机决赛第 2** | C（竞赛官方名次 + 自述预印本）[16] |
| 2026-07 | Compositional Context Fine-Tuning VLM（复杂装配动作理解）[17] | `> 待核实` | 把 VLM 用于**工业装配**的视频动作理解，属 VLA 上游（理解而非控制） | B [17] |
| 2026-08 | Inference-Time Attention Steering for VLA Driving Models [6] | `> 待核实` | 在**推理时**对 VLA 驾驶模型施加 pre-softmax 注意力偏置，无需重训即可把注意力导向安全关键目标 | B [6] |

> 注：[26][27][20][19][11][6][16][17][28] 均只读到标题/摘要片段级信息，**方法细节、量化增益、基线身份均未获取**，故一律 `> 待核实`。

### 1.2 四条技术主线（本批证据可支撑的归纳）

1. **动作表征成为独立战场**：X-Tokenizer [11] 的核心批评是"现有 tokenizer 为重建而离散化，保留运动几何但语义监督弱"，说明社区已把"动作如何被 token 化"视为 VLA 预训练的关键瓶颈，而非实现细节。
2. **长程（long-horizon）从缺陷变成显式目标**：Long-VLA [26] 与 LongNav-R1 [27] 分别在操作与导航上攻关；[27] 引入多轮 RL 与自适应视界。
3. **鲁棒性/失败模式被单独研究**：When Vision Overrides Language [28] 直接命名"视觉压倒语言"的反事实失败；[6] 用推理时注意力干预做安全导向——两者共同指向"VLA 会忽略指令"这一被承认的失效类别。
4. **部署成本与推理时延进入论文标题层**：BLURR [20] 主打低资源推理，[6] 主打免重训的推理时干预，说明"能不能跑得动/改得动"已成为一等公民。

### 1.3 基准 SOTA 核查表（关键：本批证据**全部无法核查**）

| 基准 | 本批证据中的 SOTA 数字 | 证据性质（仿真自评/论文宣称/第三方复现/真机） | 结论 |
|---|---|---|---|
| Open X-Embodiment | 无 | — | `> 待核实`（来源池无条目） |
| DROID | 无 | — | `> 待核实` |
| LIBERO | 无 | — | `> 待核实` |
| SimplerEnv | 无 | — | `> 待核实` |
| RoboArena | 无 | — | `> 待核实` |
| CALVIN | 无 | — | `> 待核实` |
| BEHAVIOR Challenge 2025 | 仅有"1st Place Solution"标题 [19]，**无任何指标数字** | 竞赛自评（非独立复现） | 名次类事实可引用，**数字不可引用** |
| ICRA 2026 LeHome（双臂折衣） | 在线轮 1/62、真机决赛第 2 [16] | **竞赛官方排名**（在线轮为仿真，真机决赛由竞赛方评判） | 本批**唯一**"仿真+真机双赛道"VLA 名次证据 |

**判断**：本批证据**不足以**回答"RT-2 / OpenVLA / π0 / π0.5 / GR00T / RDT / Diffusion Policy 在哪些基准上刷新 SOTA"。[16] 的 1/62 与第 2 名是**竞赛名次**，不是跨论文可比 SOTA，且方案未披露基线模型身份 `> 待核实`。

### 1.4 经典与奠基性工作（表格）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control | 2023 | Google DeepMind（依公开记录；候选块未含作者字段）`> 待核实` | 引用数 `> 待核实`（候选块未提供） | arXiv 预印本 [12]；是否已中稿 `> 待核实` | 高——VLA 范式的命名与奠基文献，后续 2025/2026 年工作均以其为方向前提；具体引用数 `> 待核实` | ★★★★★ 读 VLA 必读的起点，"web 知识 → 机器人控制"这一迁移命题至今是领域主线 [12] | http://arxiv.org/abs/2307.15818v1 | 标题即主张：把 web 规模视觉-语言知识迁移到机器人控制 [12] |
| Aligning Cyber Space with Physical World: A Comprehensive Survey on Embodied AI | 2024（v8） | `> 待核实` | `> 待核实` | arXiv 综述（v8 说明经多轮修订）[22] | 中——综述类，权威但非首创方法 [22] | ★★★★☆ 作为具身智能整体版图与术语对照的骨架，适合入门与定位 [22] | http://arxiv.org/abs/2407.06886v8 | 具身智能全景综述 [22] |
| Survey of Vision-Language-Action Models for Embodied Manipulation | 2025 | `> 待核实` | `> 待核实` | arXiv 综述（v2）[21] | 中高——VLA 专项综述，是检索主流模型/基准的**唯一可用入口** [21] | ★★★★★ 本次来源池中唯一能系统补齐 OpenVLA/π0/RT 系列谱系的文献，应优先精读 [21] | http://arxiv.org/abs/2508.15201v2 | VLA 操作方向专项综述 [21] |
| OpenVLA / π0 / π0.5 / GR00T / RDT / Diffusion Policy / RT-1 / ACT / ALOHA | 2022–2025 | — | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实`（本次来源列表**不含**这些条目，禁止编造链接） | 均**未**在本批来源中出现；其"承上启下"关系须经 [21] 综述正文核实 |

> **检索缺口（高优先）**：上述 6+ 个主流模型与 6 个基准在 31 条来源中**零命中**，说明本轮查询式对"模型名/基准名锚定"失效。补检索建议：`"OpenVLA" "LIBERO" site:arxiv.org`、`"pi0" OR "pi0.5" robot "Open X-Embodiment"`、`RoboArena leaderboard`、`SimplerEnv reproduced results`。

### 1.5 开源项目（表格）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| LeRobot（HuggingFace） | — | — | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实`（本批来源**无**该仓库条目） | 无法核实其 star/权重/数据集开放状态；**禁止**用记忆填充 |
| OpenVLA 权重与代码 | — | — | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | 同上 |
| BLURR（低资源推理） | 2025 | `> 待核实` | `> 待核实` | arXiv 预印本 [20] | 低——无引用/star 信号 [20] | ★★★☆☆ 若关注端侧/低算力 VLA 部署值得读，但是否开源未披露 [20] | http://arxiv.org/abs/2512.11769v1 | 头注为"Boosted Low-Resource Inference for VLA" [20] |
| X-Tokenizer | 2026 | `> 待核实` | `> 待核实` | arXiv 预印本 [11] | 低——无热度信号 [11] | ★★★★☆ 动作 tokenizer 是预训练关键环节，与工程栈选型直接相关 [11] | http://arxiv.org/abs/2606.14752v2 | 多模态动作 tokenizer [11] |

> 结论：**本批证据无法回答"哪些仓库真正开源了代码/权重/数据、复现难度多大"**，也无法回答 ROS2 / Franka / UR5 / SO-101 / 人形的部署路径与工程坑。全部 `> 待核实`。这是本次调研最大的交付缺口。

### 1.6 数据集与基准（表格）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|---|---|---|---|---|---|---|---|---|
| BEHAVIOR Challenge 2025 | 2025 | `> 待核实` | `> 待核实` | 竞赛 + 技术报告 [19] | 中——有冠军方案产出，说明参赛规模存在 [19] | ★★★☆☆ 可作为"任务适配"竞赛型证据，但指标数字缺失 [19] | http://arxiv.org/abs/2512.06951v2 | 2025 BEHAVIOR 挑战赛冠军方案 [19] |
| ICRA 2026 LeHome Challenge（双臂折衣） | 2026 | ICRA 2026 竞赛方 | `> 待核实` | 官方竞赛，62 队参赛、设真机决赛 [16] | 中高——62 队规模 + 真机决赛，是本批最强"社区参与度"信号 [16] | ★★★★☆ 罕见的"仿真轮 + 真机决赛"双轨评测设计，值得作为评测范式参考 [16] | http://arxiv.org/abs/2606.27163v3 | 在线轮仿真、决赛真机 [16] |
| Open X-Embodiment / DROID / LIBERO / SimplerEnv / RoboArena / CALVIN | 2023–2025 | — | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实` | `> 待核实`（本批来源**零命中**） | 无法核实规模、许可、榜单现状 |

---

## 2. 工业界与产品（Industry & Product）

**一句话增量判断**：本周期在可用证据中**无显著工业界增量**——没有任何厂商产品发布、量产、真机部署规模的来源；唯一可归入"从 lab 走向落地"的信号是**竞赛设置真机决赛** [16] 与**行业会议把真实部署列为中心议题** [24]，二者都是"意图/议题"级证据，不是"部署量"级证据。

| 条目 | 时间 | 证据 | 关注度 | 推荐度 | 判断 |
|---|---|---|---|---|---|
| ICRA 2026 双臂折衣竞赛设**真机决赛**，冠军方案在线轮 1/62、真机第 2 [16] | 2026-06 | 竞赛官方排名 [16]；热度 `> 待核实`；权威=C 级（竞赛+自述预印本） | 中高——62 队规模 [16] | ★★★★☆ 是"仿真→真机"闭环正在被制度化评测的直接证据 [16] | 较大概率：真机评测正在从"可选项"变为"竞赛标配"（单例，不外推） |
| SAE World Congress 2026 指出 embodied AI 正快速进入 autonomous vehicles、mobile robots、industrial machines [24] | 2026-05 | 会议白皮书 [24]；热度 `> 待核实`；权威=B 级（非同行评审） | 中——行业会议层级 [24] | ★★★☆☆ 定性框架可用，无可量化部署数据 [24] | 表述为"行业共识性判断"，**非**部署量证据 |
| VLM 用于工业**装配动作理解**（Compositional Context Fine-Tuning）[17] | 2026-07 | 预印本 [17]；热度 `> 待核实` | 低 [17] | ★★★☆☆ 说明工业装配是最先被 VLM/VLA 触达的场景之一，但止于"理解"非"控制" [17] | 推测：工业装配是近期落地优先场景 `> 待核实` |
| 厂商产品（GR00T 出货、Figure/Tesla 人形量产、RT 系列商用化） | — | **无来源** | `> 待核实` | `> 待核实` | 本周期**无可用证据**，不作任何陈述 |

---

## 3. 蓝海与缺口（Blue Ocean & Gaps）

**一句话增量判断**：本批证据反而**清晰地暴露了研究缺口本身**——动作语义表征 [11]、反事实/指令遵循失效 [28]、推理时可控性 [6]、长程 [26][27]、低资源推理 [20] 这五个方向各自只有 0–2 篇来源，且都缺少统一基准，属于"已被命名但远未收敛"的高杠杆区。

| 缺口 | 为何是缺口（证据） | 关注度 | 推荐度 | 可操作性 |
|---|---|---|---|---|
| **动作 tokenizer 的语义监督** | [11] 明确指出既有 tokenizer"为重建而离散化，只保留运动几何、语义监督弱"——这是被作者亲口承认的系统性缺陷 | 低（无热度信号）[11] | ★★★★★ | 高：可直接改造 tokenizer 并在现有 VLA 预训练管线验证 |
| **VLA 的反事实失败 / 指令被视觉压倒** | [28] 将其作为独立问题"evaluate and mitigate"，说明此前缺专门评测；[6] 从推理时干预角度呼应 | 低 [6][28] | ★★★★★ | 高：可构造反事实指令数据集 + 免重训干预，两篇已给出方法骨架 |
| **长程任务的可评测性** | 长程被 [26][27] 分别从操作/导航切入，但**本批无任何长程基准条目**；[29] 虽是 long-horizon CoT 基准但属 LLM 推理域，**不可外推**到机器人 | 低 [26][27][29] | ★★★★☆ | 中：需要先解决"长程如何度量" |
| **推理时延/算力成本的标准化报告** | 仅 [20] 一篇以低资源推理为标题，且是否给出时延/功耗对比 `> 待核实` | 低 [20] | ★★★★☆ | 高：属于低成本、高可比性的补白 |
| **跨本体泛化的使能因素** | [25] 明言"enabling factors remain poorly understood"，并提出 embodiment scaling laws 作为可检验假设 | 低 [25] | ★★★★☆ | 中：需 ~1,000 本体的程序化生成能力 |
| **安全/治理的可量化指标** | [24] 只给议题清单，**无基准、无指标定义** | 中 [24] | ★★★★☆ | 高：指标定义本身即贡献 |

> **无人区判断**：本批证据中**没有任何**工作同时做到（a）多本体、（b）长程、（c）反事实鲁棒、（d）报告推理成本——四项的交叉处是明确的竞争空白。此判断为**推测**级，需更多来源验证。

---

## 4. 瓶颈与拐点（Bottleneck & Inflection）

**一句话增量判断**：瓶颈已从"能不能学会"迁移到"**能不能被相信、被度量、被跑起来**"——证据是 2026 年出现的三篇论文分别处理可靠性 [24]、可控性 [6][28]、成本 [20]，而非继续堆能力。

| 瓶颈 | 状态 | 拐点信号 | 证据 |
|---|---|---|---|
| **数据规模 vs 数据质量** | **未收敛**。规模化证据主要来自仿真程序化生成本体（约 1,000 个拓扑/形态不同的本体）[25]；真机多本体规模化的收益与边际成本 `> 待核实` | 若出现"真机数据量 vs 泛化"的公开缩放曲线，即为拐点 | [25]（B 级，预印本） |
| **跨本体泛化** | 假设级。作者自认使能因素未知 [25] | 若 scaling law 在 VLA 操作任务（非 locomotion）复现，即为拐点 | [25] |
| **长程任务失败** | 被显式攻关但仍无统一评测 [26][27]；长程基准在机器人域 `> 待核实` | 若出现机器人域长程标准榜（类似 LIBERO 的地位），即为拐点 | [26][27] |
| **指令遵循 / 反事实鲁棒** | 刚被命名 [28]，缓解方法已有雏形；[6] 提供免重训推理时干预 | 若反事实失败率成为 VLA 论文常规报告项，即为拐点 | [6][28] |
| **推理时延与算力成本** | 单点工作 [20]，缺标准化口径 | 若论文开始统一报告 tokens/s、显存、端侧可行性，即为拐点 | [20] |
| **benchmark 与真机鸿沟 / 评测不可复现** | **最硬的瓶颈**。本批唯一"仿真+真机"双轨证据是竞赛 [16]，说明学界常规论文仍普遍缺真机独立验证 | 竞赛设真机决赛 [16] 是制度性拐点的**早期信号** | [16][19] |
| **安全与运行可靠性** | 议题化 [24]，缺指标 | 若 SAE/ISO 类标准引用具体 VLA 评测项，即为拐点 | [24] |

**拐点判断（附不确定性）**：
- **较大概率**：2026 年 VLA 论文的"标配实验"将从"单基准成功率"转向"长程 + 反事实 + 时延"三元组。依据链：三篇 2026 年论文恰好各占其一 [26/28/20] → 推演 → 结论。[P]
- **未知**：真机数据规模化是否已达可观测收益递减点。缺数据 `> 待核实`。

---

## 5. 社会·政策·国际（Society, Policy & Geopolitics）

**一句话增量判断**：本周期唯一可用增量是**治理议题被行业会议正式列为一等议题** [24]；监管细则、标准编号、地缘供应链、出口管制、劳动影响**均无来源**，一律 `> 待核实`。

| 条目 | 时间 | 证据与等级 | 关注度 | 推荐度 | 说明 |
|---|---|---|---|---|---|
| embodied AI 的 safety / trust / governance / operational reliability 被与自动驾驶、移动机器人、工业设备并列讨论 [24] | 2026-05 | SAE World Congress 2026 白皮书，B 级（非同行评审，无论文实验数据）[24]；热度 `> 待核实` | 中——行业会议层级 [24] | ★★★☆☆ 定性框架价值高，**不可**用于陈述任何指标或标准条款 [24] | 标志讨论重心从"能力演示"转向"真实系统部署" [24] |
| 基础模型**透明度**被年度指数化度量（2025 Foundation Model Transparency Index，第三届）[2] | 2025 | arXiv，B 级 [2]；热度 `> 待核实` | 中——年度指数类工作具政策可见度 [2] | ★★★☆☆ 为"透明度可被量化"提供方法论类比，**但该指数覆盖基础模型开发者，非机器人本体厂商**，不可直接外推至 VLA | 相邻证据，仅作方法论参照 [2] |
| 机器人专项监管（如 ISO 10218 修订、EU AI Act 对具身系统的适用、中美出口管制） | — | **无来源** | `> 待核实` | `> 待核实` | 本周期**无可用证据**，不作陈述 |
| 地缘与供应链（减速器/灵巧手/算力芯片） | — | **无来源** | `> 待核实` | `> 待核实` | 同上 |
| 劳动影响与伦理 | — | 仅 [24] 提及 trust/governance 议题，未涉劳动 | 低 [24] | ★★☆☆☆ | `> 待核实` |

---

## 6. 资本与生态（Capital & Ecosystem）

**一句话增量判断**：**本周期在可用证据中无显著变化**——31 条来源里没有任何融资、并购、人才流动、公司格局、社区增长（star/下载）数据。

| 维度 | 结论 | 证据 |
|---|---|---|
| 融资额 / 估值 / 并购 | `> 待核实`（无来源） | — |
| 人才流动 | `> 待核实`（无来源） | — |
| 开源社区活跃度（star、下载、PR） | `> 待核实`：本批全部仓库类热度字段缺失 | [11][16][19][20] 均未提供 star/下载 |
| 生态格局（谁在做 VLA 基础模型） | 只能通过综述 [21] 与奠基文献 [12] 间接定位，**无法**给出当前格局 | [12][21] |
| 竞赛生态（可作为生态活跃度的替代指标） | **有信号**：ICRA 2026 LeHome **62 支队伍**参赛并设真机决赛 [16]；BEHAVIOR Challenge 2025 产出冠军方案 [19] | [16][19] |

> **方法说明**：竞赛参赛队伍数 [16] 是本批唯一接近"生态活跃度"的可核查数字。除此之外，任何关于"VLA 融资火热""某公司估值"的表述都属 `> 待核实`，本报告不予写入。

---

## 7. 信号与预测（Signals & Forecast）

**一句话增量判断**：早期信号指向"**评测制度化 + 失效模式显性化 + 成本约束前置**"三条线同时收紧；预测全部写成可证伪假设。

### 7.1 早期信号（已确证事实）

| 信号 | 时间 | 证据 | 解读 |
|---|---|---|---|
| 竞赛设**真机决赛**，且方案同时报告在线轮与真机名次 [16] | 2026-06 | [16]，C 级（竞赛官方名次 + 自述预印本） | 评测正从"仿真自评"向"真机制度性验证"迁移 |
| 反事实失败被写成"evaluate **and mitigate**"的独立问题 [28] | 2026-02 | [28]，B 级 | 失效模式从"附录讨论"升级为"标题级问题" |
| 动作 tokenizer 被批评为"弱语义监督" [11] | 2026-06 | [11]，B 级 | 表征层仍有结构性改进空间 |
| 低资源推理成为论文标题 [20]；免重训推理时干预出现 [6] | 2025-12 / 2026-08 | [20][6]，B 级 | 部署侧约束开始反向影响方法设计 |
| 治理议题进入行业会议主议程 [24] | 2026-05 | [24]，B 级 | 监管压力可能先于技术成熟到来 |

### 7.2 可证伪预测（[P]，附依据链与置信度）

| # | 预测（可证伪假设） | 依据链 | 置信度 | 证伪条件（若出现则判断不成立） |
|---|---|---|---|---|
| P1 | 到 **2027-06**，至少 3 篇 VLA 论文会在主实验表中**同时**报告长程任务指标与推理时延/算力成本 | [26][27] 已将长程显式化 → [20] 已将成本问题化 → 二者合流是自然下一步 | 中 | 若 2027-06 前主流 VLA 论文实验表仍只有单基准成功率，则 P1 不成立 |
| P2 | 到 **2027-06**，"反事实/指令遵循失败率"会成为至少一个公开榜单或竞赛的**评分项** | [28] 提出评测与缓解 → [16] 证明竞赛可设真机双轨 → 竞赛是最可能承载新指标的载体 | 中低 | 若无任何榜单/竞赛纳入该指标，则 P2 不成立 |
| P3 | 到 **2027-12**，"本体数量↑ ⇒ 未见本体泛化↑"的 scaling law 会在**操作类 VLA 任务**上被复现或明确反驳（而非停留在 locomotion 仿真 [25]） | [25] 只在 locomotion 提出假设并自认使能因素未知 → 该假设的高价值必然引来跨域检验 | 中 | 若 2027-12 前仍无操作域检验（既无复现也无反驳），则 P3 不成立（注意：这**同时**意味着该假设被边缘化） |
| P4 | 到 **2027-06**，带**真机决赛**的 VLA 竞赛数量 ≥ 2（以 [16] 为基线 1） | [16] 的 62 队规模说明参与度足够支撑第二个竞赛 → 竞赛方有动机复制该模式 | 中低 | 若 2027-06 前无第二个真机决赛类竞赛，则 P4 不成立 |
| P5 | 未来 6–18 个月内，动作 tokenizer 语义化 [11] 会成为一个被独立复现/对比的子赛道 | [11] 的批评直指预训练核心环节，改动成本低、可比性强 | 低（仅单篇来源支撑，`> 待核实`） | 若无后续工作在同一基准上对比 tokenizer，则 P5 不成立 |

### 7.3 Watchlist（值得持续关注）

1. **动作表征**：X-Tokenizer [11] 后续是否被主流 VLA 预训练采用（需查引用与代码）。
2. **反事实鲁棒**：When Vision Overrides Language [28] 是否催生标准测试集。
3. **推理时可控性**：Inference-Time Attention Steering [6] 的免重训思路能否跨域（驾驶 → 操作）。
4. **竞赛评测范式**：LeHome [16] 的"在线轮 + 真机决赛"是否被复制。
5. **综述入口**：[21]（VLA 操作）与 [22]（具身智能全景）的后续版本，是补齐本报告大量 `> 待核实` 缺口的最高效路径。
6. **治理落地**：[24] 的议题清单是否转化为可引用标准或指标。

### 7.4 本次调研自身的元信号（重要）

- **信号**：31 条来源中 13 条完全无关、6 个主流模型与 6 个基准零命中——说明**查询式与意图不匹配**，而非领域无进展。
- **行动**：下一轮必须以"模型名 + 基准名"逐对锚定检索，并优先取用 RoboArena / SimplerEnv 等**第三方榜单与复现报告**（C 级），否则任何 SOTA 陈述都违反引用纪律。
- **风险**：若下一轮仍无法获取 [1.3] 表中的基准数字，本报告第 1 章必须保持"名次可引、数字不可引"的结论强度，**不得**用训练记忆补写。

---

## 参考来源

> 说明：以下 31 条为本轮候选来源全集，按引用编号原样保留。经核查，[1][3][4][5][7][8][10][13][14][15][23][30][31] 与本主题无关或已撤稿（[7] 为 withdrawn，按 E 级丢弃），仅在被用于说明"检索漂移/证据缺口"时引用。所有 URL 均来自给定候选列表，未新增或改写。

[1] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1
[2] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1
[3] NTIRE 2025 Challenge on Image Super-Resolution (x4): Methods and Results — http://arxiv.org/abs/2504.14582v3
[4] The AudioMOS Challenge 2025 — http://arxiv.org/abs/2509.01336v1
[5] VLSP 2025 MLQA-TSR Challenge: Vietnamese Multimodal Legal Question Answering on Traffic Sign Regulation — http://arxiv.org/abs/2510.20381v1
[6] Inference-Time Attention Steering for Vision-Language-Action Driving Models — http://arxiv.org/abs/2608.17095v1
[7] This paper has been withdrawn — http://arxiv.org/abs/cond-mat/0309395v2
[8] Overview of AuTexTification at IberLEF 2023: Detection and Attribution of Machine-Generated Text in Multiple Domains — http://arxiv.org/abs/2309.11285v1
[9] Multiverse Transformer: 1st Place Solution for Waymo Open Sim Agents Challenge 2023 — http://arxiv.org/abs/2306.11868v1
[10] Proceedings of the 3rd Workshop on Open-Source Design Automation (OSDA), 2023 — http://arxiv.org/abs/2303.18024v1
[11] X-Tokenizer: A Multimodal Action Tokenizer for Vision-Language-Action Pretraining — http://arxiv.org/abs/2606.14752v2
[12] RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control — http://arxiv.org/abs/2307.15818v1
[13] UIC-AIHealth4All at ArchEHR-QA 2026: Answer-First Evidence Grounding for Clinical Question Answering — http://arxiv.org/abs/2608.27467v1
[14] Second MOASEI Competition at AAMAS'2026: A Technical Report — http://arxiv.org/abs/2607.03399v1
[15] AutoRestTest at the SBFT 2026 Tool Competition — http://arxiv.org/abs/2607.01063v1
[16] Learning to Fold: prizewinning solution at LeHome Challenge 2026 (1st place online, 2nd offline) — http://arxiv.org/abs/2606.27163v3
[17] Compositional Context Fine-Tuning Vision-Language Model for Complex Assembly Action Understanding from Videos — http://arxiv.org/abs/2607.10797v1
[18] Vision Mamba: A Comprehensive Survey and Taxonomy — http://arxiv.org/abs/2405.04404v1
[19] Task adaptation of Vision-Language-Action model: 1st Place Solution for the 2025 BEHAVIOR Challenge — http://arxiv.org/abs/2512.06951v2
[20] BLURR: A Boosted Low-Resource Inference for Vision-Language-Action Models — http://arxiv.org/abs/2512.11769v1
[21] Survey of Vision-Language-Action Models for Embodied Manipulation — http://arxiv.org/abs/2508.15201v2
[22] Aligning Cyber Space with Physical World: A Comprehensive Survey on Embodied AI — http://arxiv.org/abs/2407.06886v8
[23] NTIRE 2026 Challenge on Robust AI-Generated Image Detection in the Wild — http://arxiv.org/abs/2604.11487v1
[24] Embodied AI in Action: Insights from SAE World Congress 2026 on Safety, Trust, Robotics, and Real-World Deployment — http://arxiv.org/abs/2605.10653v1
[25] Towards Embodiment Scaling Laws in Robot Locomotion — http://arxiv.org/abs/2505.05753v2
[26] Long-VLA: Unleashing Long-Horizon Capability of Vision Language Action Model for Robot Manipulation — http://arxiv.org/abs/2508.19958v2
[27] LongNav-R1: Horizon-Adaptive Multi-Turn RL for Long-Horizon VLA Navigation — http://arxiv.org/abs/2602.12351v2
[28] When Vision Overrides Language: Evaluating and Mitigating Counterfactual Failures in VLAs — http://arxiv.org/abs/2602.17659v2
[29] LongCoT: Benchmarking Long-Horizon Chain-of-Thought Reasoning — http://arxiv.org/abs/2604.14140v1
[30] Overview of the Sensemaking Task at the ELOQUENT 2025 Lab: LLMs as Teachers, Students and Evaluators — http://arxiv.org/abs/2507.12143v1
[31] LongEval at CLEF 2025: Longitudinal Evaluation of IR Model Performance — http://arxiv.org/abs/2503.08541v1

---

### 附：本报告的证据强度自检

- [x] 七维章节全部覆盖，无省略
- [x] 每条关键论断带 [n]；未出现候选列表之外的编号；未新增 URL
- [x] 区分"最新进展（2024–2026）"与"经典工作（RT-2 2023 等）"
- [x] 四类证据（热度/权威/关注度/推荐度）逐条给出；**热度字段全部为 `> 待核实`，因候选块确未提供引用数与 star，未编造任何数字**
- [x] 传闻/预测分级：[P] 5 条，均写成可证伪假设；无 [R]（本批无可靠传闻来源）
- [x] 明确区分"竞赛名次（可引）"与"SOTA 数字（不可引）"
- [ ] **未完成项（须下一轮补齐）**：OpenVLA / π0 / π0.5 / GR00T / RDT / Diffusion Policy 的基准成绩；Open X-Embodiment / DROID / LIBERO / SimplerEnv / RoboArena / CALVIN 的 SOTA 与第三方复现；LeRobot 等仓库的开源与复现难度；ROS2 实机部署工程坑；融资与监管细则 —— 全部 `> 待核实`。

---

*Generated by research-bot · topic=`具身智能与视觉-语言-动作vla前沿` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`deepseek-v4-flash` · sources=31 · duration=159s · 2026-10-18T22:11:30+00:00*
