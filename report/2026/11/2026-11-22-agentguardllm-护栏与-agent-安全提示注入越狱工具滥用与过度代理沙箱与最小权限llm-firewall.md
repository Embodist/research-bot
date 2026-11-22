# AgentGuard：LLM 护栏与 Agent 安全 前沿调研报告

**日期**：2026-11-22（UTC）  
**领域**：LLM 护栏、Agent 安全、提示注入、越狱、工具滥用、沙箱、LLM Firewall、红队基准  
**检索来源数量**：32 条（含 13 条领域强相关证据：[1][2][3][4][5][6][7][8][9][10][11][12][13]）

---

## 1. 进展与热点（Progress & Hotspots）

> **增量判断**：2025-2026 年核心增量集中在 **提示注入检测的实用基线构建**、**零样本/轻量级防御范式**、以及 **基础模型透明度下降对护栏可审计性的冲击**；真机/多模态 Agent 场景下的端到端评测仍缺失。

| 进展 | 时间 | 机构/作者 | 一句话贡献 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 来源 |
|------|------|-----------|------------|----------|----------|--------|--------|------|
| 基于 HackAPrompt 语料训练分类器检测提示注入 | 2025-12 | arXiv (cs.CR) | 整理增强真实攻击语料，评估 LSTM/FFN/RF/NB 等分类器，给出可复现工程基线 | > 待核实（arXiv 新发布，引用数未形成） | arXiv 预印本，未经同行评审 | 中 — 直接针对 LLM 应用层核心威胁，社区关注度上升 | ★★★☆☆ — 实用基线，适合工程起点，需独立基准验证 | [5] |
| 零样本嵌入漂移检测防御提示注入 | 2026-01 | arXiv (cs.CR) | 利用嵌入空间漂移信号实现无监督、即插即用的注入检测，直击间接注入难点 | > 待核实（2026 年最新预印本） | arXiv 预印本，未经同行评审 | 中 — 新防御范式，工程部署成本低 | ★★★☆☆ — 创新思路，泛化性与鲁棒性待验证 | [6] |
| 2025 基础模型透明度指数（FMTI v3） | 2025-12 | Stanford CRFM 等 | 头部模型商透明度均分从 58 降至 40，训练数据/算力/部署影响最不透明，IBM 为少数正面例外 | > 待核实（年度权威报告，被广泛引用） | arXiv 预印本，核心作者含 Percy Liang、Rishi Bommasani | 高 — 权威团队年度基准，被政策与产业界广泛引用 | ★★★★☆ — 为护栏治理、合规审计提供宏观量化证据 | [1] |
| 统一防御框架 UniGuardian | 2025-02 | arXiv (cs.CL) | 统一检测提示注入、后门攻击、对抗攻击，探索三者内在关联 | > 待核实（预印本） | arXiv 预印本 | 中 — 统一视角有参考价值 | ★★★☆☆ — 理论整合强，工程落地细节缺失 | [8] |
| 间接提示注入任务篡改基准 | 2026-11 | arXiv (cs.CR) | 超越指令覆盖，基准化“任务篡改”类间接注入，揭示现有防御盲区 | > 待核实（2026 年最新预印本） | arXiv 预印本 | 中 — 细化攻击面，推动评测颗粒度 | ★★★☆☆ — 基准建设贡献大，需社区采纳验证 | [9] |
| 自动通用提示注入攻击构造 | 2024-03 | arXiv (cs.AI) | 系统性构造自动化、通用的注入攻击，揭示 LLM 集成应用的普遍脆弱性 | > 待核实（2024 年早期工作，被后续引用） | arXiv 预印本 | 中 — 奠基性攻击方法论 | ★★★★☆ — 攻击侧基线，防御评测必参考 | [4] |
| 偏好优化防御注入 | 2024-10 | arXiv (cs.CR) | 通过偏好优化（SecAlign）在模型层面对齐抗注入能力 | > 待核实（预印本 v3） | arXiv 预印本 | 中 — 模型内在防御路线 | ★★★☆☆ — 正交于外挂护栏，值得对比 | [2] |
| 结构化查询防御注入 | 2024-02 | arXiv (cs.CR) | 引入结构化查询（StruQ）将非结构化提示转为可验证结构，降低注入面 | > 待核实（预印本 v2） | arXiv 预印本 | 中 — 架构层面缓解思路 | ★★★☆☆ — 工程可落地，需评估延迟与表达力损失 | [3] |
| Web Agent 专用注入攻击 | 2025-05 | arXiv (cs.CR) | 面向 Web Agent 的注入攻击基准，覆盖浏览器环境下的工具调用劫持 | > 待核实（预印本 v4） | arXiv 预印本 | 中 — 场景化攻击基准 | ★★★☆☆ — Agent 安全评测关键补充 | [7] |
| LLM 自我防御越狱愿景 | 2024-02 | arXiv (cs.CR) | 提出 LLM 可通过内在机制实用防御越狱，而非仅依赖外部护栏 | > 待核实（愿景类论文） | arXiv 预印本 | 中 — 概念引导性强 | ★★★☆☆ — 长期研究方向参考 | [10] |

> **待核实**：上述所有论文均为 arXiv 预印本，缺乏同行评审与独立复现基准；真机/多模态/多轮 Agent 场景下的鲁棒性指标（误报率、漏报率、P99 延迟）尚无公开统一评测。

---

## 2. 工业界与产品（Industry & Product）

> **增量判断**：主流生产级开源护栏框架（NeMo Guardrails、Guardrails AI、LLM Guard、LangChain 官方护栏模块）在**架构对比、插件机制、流式处理、生产指标**上**缺乏实证覆盖**；LangChain Deep Agents 仅有二手播客摘要且来源已失效 [13]，需直接查阅官方仓库确认。

| 项目/产品 | 类型 | 状态 | 关键特性 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 来源/备注 |
|-----------|------|------|----------|----------|----------|--------|--------|-----------|
| NeMo Guardrails | 开源框架 | 活跃 | 策略引擎、对话轨道、工具调用拦截、可编程规则 | > 待核实（GitHub stars/下载未在证据中） | NVIDIA 官方维护 | 高 — 产业界广泛采用 | ★★★★☆ — 生产级首选，需实测延迟/吞吐 | 官方文档/GitHub（证据集未覆盖，**需补查**） |
| Guardrails AI | 开源框架 | 活跃 | Pydantic 风格输出约束、流式验证、纠错重试 | > 待核实 | Guardrails AI 官方 | 高 — 社区活跃 | ★★★★☆ — 结构化输出场景强 | 官方文档/GitHub（**需补查**） |
| LLM Guard | 开源库 | 活跃 | 提示注入/PII/有害内容检测、低延迟、可组合 | > 待核实 | 社区维护 | 中高 — 轻量级插件化 | ★★★★☆ — 适合微服务网关集成 | GitHub（**需补查**） |
| LangChain 官方护栏模块 | 框架内置 | 随 LangChain 迭代 | Runnable 配合、输出解析器约束、回调拦截 | > 待核实 | LangChain 官方 | 高 — 生态集成度高 | ★★★☆☆ — 耦合框架，灵活性受限 | 官方文档（**需补查**） |
| LangChain Deep Agents | 代理框架 | 2026 | 终端 CLI、子代理隔离、异步委托、文件系统/Shell 结构化安全边界 | stars 未知（Zenodo 记录已移除） | 仅有播客二手摘要 [13] | 低 — 无法直接访问源码验证 | ★★☆☆☆ — **需直接查阅 GitHub 官方仓库确认** | [13] |
| 控制理论护栏：从拒绝到恢复 | 理论/原型 | 2025-10 | 将护栏建模为序贯决策，引入控制理论实现动作修正而非单纯拒绝 | 无引用数据（arXiv 2025-10） | arXiv 预印本 [12] | 中 — 理论创新未经验证 | ★★★☆☆ — 适合理论参考，工程落地需自行实现 | [12] |
| 可定制伦理护栏框架 | 理论/架构 | 2024-11 | 规则/策略/助手三层设计，强调多元价值对齐 | 无引用数据（arXiv 2024-11） | arXiv 预印本 [11] | 中 — 伦理对齐视角 | ★★★☆☆ — 架构设计参考，生产细节缺失 | [11] |

> **证据缺口**：候选证据集**未覆盖**上述主流生产级框架的架构对比、集成模式（中间件/装饰器/策略引擎）、生产指标（P99 延迟、误拦率、规则热更新、多租户隔离）[12][13][11][14]。**必须补查官方文档、GitHub 仓库、基准测报告**。

---

## 3. 蓝海与缺口（Blue Ocean & Gaps）

| 缺口 | 说明 | 证据支撑 | 优先级 |
|------|------|----------|--------|
| **统一、持续更新的 Agent 安全评测基准** | 缺乏覆盖工具调用、记忆投毒、多 Agent 协作攻击、沙箱逃逸、最小权限违规的端到端基准 | [7][9] 仅覆盖 Web Agent 注入与任务篡改两个子面 | ⭐⭐⭐⭐⭐ |
| **真机/多模态/多轮交互下的注入检测鲁棒性** | 现有分类器 [5]、零样本漂移 [6]、统一防御 [8] 均在文本单轮或合成数据上评估 | [5][6][8] 均为预印本，无真机部署报告 | ⭐⭐⭐⭐ |
| **零样本/少样本防御在自适应攻击下的泛化-误报权衡** | 嵌入漂移 [6] 等轻量级方法面对分布外、自适应攻击的理论边界未知 | [6] 提出方法但无红队对抗评估 | ⭐⭐⭐⭐ |
| **护栏与 VLA/机器人控制回路的集成模式** | 同步阻塞 vs 异步监控 vs 动作修正，在实时控制（10-100ms 预算）下的可行性无公开基准 | [12] 提出控制理论范式但未接入机器人实验 | ⭐⭐⭐⭐ |
| **生产环境关键指标的公开测评数据** | P99 延迟、误拦率、规则热更新、多租户隔离、版本灰度发布等工程指标缺失 | [12][13][11][14] 证据集分析确认缺口 | ⭐⭐⭐⭐ |
| **基础模型透明度下降下的供应链可审计性** | FMTI 2025 显示透明度恶化 [1]，导致下游护栏无法溯源模型行为边界 | [1] 量化证据 | ⭐⭐⭐ |
| **从拒绝到恢复的控制理论方法在实时机器人中的计算预算验证** | [12] 理论框架未给出推理延迟、采样频率、稳定性裕度等工程数字 | [12] 理论贡献为主 | ⭐⭐⭐ |

---

## 4. 瓶颈与拐点（Bottleneck & Inflection）

| 瓶颈 | 现状 | 拐点信号 | 不确定性/风险 | 证据 |
|------|------|----------|---------------|------|
| **评测基准碎片化、静态化** | 现有基准多为单任务、单模态、静态数据集 [4][5][7][9] | 社区呼吁“持续红队基准平台”（如 RoboArena 风格） | 若无统一基准，SOTA 声称不可比，**风险**：虚假进步 | [4][5][7][9] |
| **防御与实用性的误报-漏报困境** | 分类器 [5]、漂移检测 [6]、结构化查询 [3] 均面临误拦正常指令 vs 漏报变种攻击 | 零样本方法降低训练成本但泛化未证；偏好优化 [2] 需高质量偏好数据 | **不确定**：自适应攻击下误报率曲线；**风险**：生产环境误拦导致业务中断 | [2][3][5][6] |
| **模型层 vs 系统层防御的责任边界模糊** | SecAlign [2]、UniGuardian [8] 尝试模型内在对齐；NeMo/LLM Guard 等为系统外挂 | 趋势：模型内在安全（对齐）+ 系统外挂（护栏）双层防御 | **不确定**：模型更新后外挂规则失效频率；**风险**：供应链不透明 [1] 导致模型行为漂移不可知 | [1][2][8] |
| **实时性与计算预算** | 控制理论护栏 [12] 需序贯决策推理；结构化查询 [3] 增加解析开销 | 硬件加速（NPU/GPU 推理）、模型蒸馏、规则编译优化 | **风险**：机器人控制回路（<10ms）下护栏成为瓶颈 | [3][12] |
| **透明度下降导致的合规与审计断层** | FMTI 2025 平均分 40/100 [1]，训练数据/算力/部署影响最不透明 | 监管趋势（EU AI Act、美行政命令）要求模型卡、风险评估、事后审计 | **不确定**：闭源模型商是否配合；**风险**：护栏厂商面临“黑箱上游”合规责任 | [1] |

---

## 5. 社会·政策·国际（Society, Policy & Geopolitics）

| 维度 | 进展/信号 | 对护栏/Agent 安全的影响 | 证据/备注 |
|------|-----------|------------------------|-----------|
| **监管合规** | EU AI Act 高风险 AI 系统要求风险管理、数据治理、人工监督、事后审计；美 NIST AI RMF、行政命令 14110 推动红队测试、模型卡 | 护栏成为合规“必选件”：需提供可审计的拦截日志、误报/漏报率证据、规则版本管理 | > 待核实（政策文本公开，但具体执行细则与护栏技术标准映射尚在演进） |
| **标准化** | ISO/IEC 42001 AI 管理体系、OWASP Top 10 for LLM Applications（2023/2025 版）将提示注入、越狱、工具滥用列为核心风险 | 推动护栏功能标准化：检测接口、日志格式、红队基准协议 | OWASP LLM Top 10 社区广泛引用，**需补查官方版本** |
| **地缘与供应链** | 头部模型集中于美/中少数厂商，FMTI 2025 显示透明度下降 [1]；出口管制限制高端算力流动 | 下游护栏厂商面临“单一来源”风险：模型行为变更无预警、无法溯源、无法自主微调防御 | [1] 量化透明度下降趋势 |
| **劳动与伦理** | Agent 自主决策涉及金融交易、医疗建议、物理机器人控制，失控风险外部性大 | 推动“最小权限”、“沙箱”、“人在回路”成为法律注意义务基线 | > 待核实（判例法与行业规范尚在形成期） |
| **国际治理** | G7 广岛进程、联合国 AI 咨询机构报告、全球 AI 安全峰会（Bletchley/Seoul/Paris）推动跨境红队、评测互认 | 长期看：护栏评测结果可能需跨境互认，类似金融压力测试 | > 待核实（进程早期，技术细节未定） |

---

## 6. 资本与生态（Capital & Ecosystem）

| 信号 | 说明 | 证据/备注 |
|------|------|-----------|
| **安全基础设施赛道融资持续** | 专注 LLM 护栏/红队/审计的初创（如 Lakera, Protect AI, HiddenLayer, Prompt Security, Guardrails AI 商业化）近 18 个月获 A/B 轮融资 | > 待核实（Crunchbase/PitchBook 数据需补查，证据集未覆盖融资信息） |
| **大厂内化 vs 开源生态** | NVIDIA (NeMo)、Microsoft (Guidance/LLMOps)、Databricks (MLflow Gateway) 内化护栏能力；开源社区 (Guardrails AI, LLM Guard, LangChain) 竞争插件生态 | 证据集仅覆盖 LangChain 片段 [13]、**需补查官方路线图与插件市场活跃度** |
| **人才流动** | 红队、对抗机器学习、形式化验证人才从学术/大厂流向安全创业公司 | > 待核实（LinkedIn/学术会议服务委员会变动为代理指标） |
| **社区基准建设** | OpenAI Evals、Hugging Face Open LLM Leaderboard、LMSYS Chatbot Arena 开始纳入安全维度；但 Agent 专用榜单（工具调用、沙箱逃逸）仍缺 | [7][9] 为学术侧尝试，**产业侧统一榜单缺失** |
| **保险与认证雏形** | 网络保险开始询问 LLM 护栏部署情况；ISO 42001 认证机构出现 | > 待核实（早期信号，规模未形成） |

---

## 7. 信号与预测（Signals & Forecast）

| 早期信号 | 推演依据链 | 可证伪预测（6-18 月） | 置信度 | 标记 |
|----------|------------|------------------------|--------|------|
| 零样本/少样本防御论文激增 [6][10] | 训练数据获取难、模型更新快 → 需无监督/即插即用防御 | **P1**：至 2027-06，主流护栏框架将内置零样本漂移/一致性检测作为默认插件，且在 OWASP LLM Top 10 基准上误报率 < 5% | 中 | [P] |
| 统一红队基准平台雏形出现 [7][9] | 碎片化基准不可比 → 社区/基金会主导持续评测平台 | **P2**：至 2027-03，出现类似 “AgentArena” 的持续榜单，覆盖 ≥5 类工具调用攻击、≥3 种本体（文本/浏览器/代码/机器人），且有 ≥3 家独立机构提交结果 | 中高 | [P] |
| 控制理论护栏进入机器人实机实验 [12] | 理论框架就绪 → 需实时性验证 | **P3**：至 2027-09，有 ≥2 篇 CoRL/ICRA/RSS 论文报告在真机机械臂/人形上部署“从拒绝到恢复”护栏，控制频率 ≥50Hz，P99 延迟 < 8ms | 中 | [P] |
| 透明度法规强制模型卡与护栏审计日志 [1] | FMTI 下降趋势 + EU AI Act 生效 → 合规倒逼 | **P4**：至 2027-12，进入 EU 市场的 LLM 应用必须提供模型卡（含训练数据摘要）、护栏规则版本库、红队测试报告，否则面临市场准入限制 | 中高 | [P] |
| 保险定价挂钩护栏成熟度 | 网络保险索赔案例积累 → 精算模型纳入护栏指标 | **P5**：至 2028-06，主流网络保险条款将“部署通过 OWASP LLM Top 10 认证的护栏”作为保费折扣/免赔额调整因子 | 低 | [P] |
| 多模态注入成主流攻击面 | 图像/音频/视频注入 PoC 增加（如视觉提示注入） | **P6**：至 2027-03，首个多模态 Agent 红队基准（含视觉/语音注入、工具链劫持）发布并被 ≥5 篇论文引用 | 中 | [P] |

> **不确定性提示**：以上预测均标 `[P]`，依据为当前论文趋势、政策进程与产业信号的定性推演；**若到预测时间点未出现所述里程碑，判断即被证伪**。关键风险变量：基础模型闭源化加剧 [1]、算力出口管制升级、重大安全事故触发监管突变。

---

## 经典与奠基性工作（Classic & Foundational Works）

| 名称 | 年份 | 机构/作者 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| Automatic and Universal Prompt Injection Attacks against LLMs | 2024 | arXiv (cs.AI) | > 待核实 | arXiv 预印本 | 中 — 奠基性攻击方法论 | ★★★★☆ | [4] | 系统性构造自动化通用注入，防御评测必参考基线 |
| Detecting Prompt Injection Attacks Against Application Using Classifiers | 2025 | arXiv (cs.CR) | > 待核实 | arXiv 预印本 | 中 — 实用检测基线 | ★★★☆☆ | [5] | 基于 HackAPrompt 真实语料，多种分类器对比 |
| Zero-Shot Embedding Drift Detection | 2026 | arXiv (cs.CR) | > 待核实 | arXiv 预印本 | 中 — 新防御范式 | ★★★☆☆ | [6] | 无监督、轻量级，直击间接注入 |
| UniGuardian: Unified Defense for Prompt Injection, Backdoor, Adversarial | 2025 | arXiv (cs.CL) | > 待核实 | arXiv 预印本 | 中 — 统一视角 | ★★★☆☆ | [8] | 三类攻击内在关联探索 |
| Beyond Instruction Override: Benchmarking Indirect Prompt Injection with Task-Tampering | 2026 | arXiv (cs.CR) | > 待核实 | arXiv 预印本 | 中 — 细化攻击面 | ★★★☆☆ | [9] | 任务篡改类间接注入基准 |
| SecAlign: Defending Against Prompt Injection with Preference Optimization | 2024 | arXiv (cs.CR) | > 待核实 | arXiv 预印本 | 中 — 模型内在对齐路线 | ★★★☆☆ | [2] | 正交于外挂护栏 |
| StruQ: Defending Against Prompt Injection with Structured Queries | 2024 | arXiv (cs.CR) | > 待核实 | arXiv 预印本 | 中 — 架构层面缓解 | ★★★☆☆ | [3] | 结构化查询降低注入面 |
| WebInject: Prompt Injection Attack to Web Agents | 2025 | arXiv (cs.CR) | > 待核实 | arXiv 预印本 | 中 — 场景化基准 | ★★★☆☆ | [7] | 浏览器环境工具调用劫持 |
| LLMs Can Defend Themselves Against Jailbreaking (Vision) | 2024 | arXiv (cs.CR) | > 待核实 | arXiv 预印本 | 中 — 长期方向 | ★★★☆☆ | [10] | 模型自我防御愿景 |
| The 2025 Foundation Model Transparency Index | 2025 | Stanford CRFM 等 | > 待核实 | arXiv 预印本，核心作者权威 | 高 — 行业治理基线 | ★★★★☆ | [1] | 透明度下降量化，关联护栏可审计性 |

---

## 开源项目（Open-Source Projects）—— 需补查官方源

| 名称 | 年份/状态 | 维护机构 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|-----------|----------|------|------|--------|--------|------|------|
| NeMo Guardrails | 活跃 | NVIDIA | > 待核实 | 官方维护 | 高 | ★★★★☆ | github.com/NVIDIA/NeMo-Guardrails | 策略引擎、对话轨道、工具拦截，**需实测生产指标** |
| Guardrails AI | 活跃 | Guardrails AI Inc. | > 待核实 | 官方维护 | 高 | ★★★★☆ | github.com/guardrails-ai/guardrails | Pydantic 约束、流式验证、纠错重试 |
| LLM Guard | 活跃 | 社区 | > 待核实 | 社区维护 | 中高 | ★★★★☆ | github.com/protectai/llm-guard | 注入/PII/有害内容检测、低延迟插件化 |
| LangChain 官方护栏模块 | 随框架迭代 | LangChain | > 待核实 | 官方生态 | 高 | ★★★☆☆ | python.langchain.com/docs/modules/agents/guardrails | Runnable 集成、输出解析器约束 |
| LangChain Deep Agents | 2026 | LangChain | stars 未知（记录失效） | 仅二手播客 [13] | 低 | ★★☆☆☆ | github.com/langchain-ai/langchain (需核实子仓库) | **需直接查阅官方仓库确认安全边界实现** |

---

## 数据集与基准（Datasets & Benchmarks）

| 名称 | 年份 | 来源/论文 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|------|------|--------|--------|------|------|
| HackAPrompt Playground Submissions (augmented) | 2025 | [5] | > 待核实 | 竞赛平台真实攻击语料 | 中 | ★★★☆☆ | [5] | 论文 [5] 基于此增强，含真实注入样本 |
| WebInject Benchmark | 2025 | [7] | > 待核实 | 学术基准 | 中 | ★★★☆☆ | [7] | Web Agent 专用注入攻击基准 |
| Indirect Prompt Injection Task-Tampering Benchmark | 2026 | [9] | > 待核实 | 学术基准 | 中 | ★★★☆☆ | [9] | 细化任务篡改类间接注入 |
| OWASP Top 10 for LLM Applications | 2023/2025 | OWASP 社区 | > 待核实 | 行业标准 | 高 | ★★★★★ | owasp.org/www-project-top-10-for-large-language-model-applications | **行业公认风险清单，护栏选型必对齐** |
| FMTI 2025 数据集 | 2025 | [1] | > 待核实 | 权威年度报告配套 | 高 | ★★★★☆ | [1] | 透明度指标原始数据，供合规审计二次分析 |

---

## 参考来源（引用编号列表）
[1] The 2025 Foundation Model Transparency Index — http://arxiv.org/abs/2512.10169v1
[2] SecAlign: Defending Against Prompt Injection with Preference Optimization — http://arxiv.org/abs/2410.05451v3
[3] StruQ: Defending Against Prompt Injection with Structured Queries — http://arxiv.org/abs/2402.06363v2
[4] Automatic and Universal Prompt Injection Attacks against Large Language Models — http://arxiv.org/abs/2403.04957v1
[5] Detecting Prompt Injection Attacks Against Application Using Classifiers — http://arxiv.org/abs/2512.12583v1
[6] Zero-Shot Embedding Drift Detection: A Lightweight Defense Against Prompt Injections in LLMs — http://arxiv.org/abs/2601.12359v1
[7] WebInject: Prompt Injection Attack to Web Agents — http://arxiv.org/abs/2505.11717v4
[8] UniGuardian: A Unified Defense for Detecting Prompt Injection, Backdoor Attacks and Adversarial Attacks in Large Language Models — http://arxiv.org/abs/2502.13141v2
[9] Beyond Instruction Override: Benchmarking Indirect Prompt Injection with Task-Tampering Attacks — http://arxiv.org/abs/2611.07640v1
[10] LLMs Can Defend Themselves Against Jailbreaking in a Practical Manner: A Vision Paper — http://arxiv.org/abs/2402.15727v2
[11] AI Ethics by Design: Implementing Customizable Guardrails for Responsible AI Development — http://arxiv.org/abs/2411.14442v2
[12] From Refusal to Recovery: A Control-Theoretic Approach to Generative AI Guardrails — http://arxiv.org/abs/2510.13727v2
[13] Ep. 2535: Inside LangChain's Deep Agents: What's Actually in the Box — https://doi.org/10.5281/zenodo.20181035
[14] Sensitivity and pointing accuracy of the NEMO km$^3$ telescope — http://arxiv.org/abs/astro-ph/0605067v1

---

*Generated by research-bot · topic=`agentguardllm-护栏与-agent-安全提示注入越狱工具滥用与过度代理沙箱与最小权限llm-firewall` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`nvidia/nemotron-3-ultra-550b-a55b` · sources=32 · duration=326s · 2026-11-22T02:32:38+00:00*
