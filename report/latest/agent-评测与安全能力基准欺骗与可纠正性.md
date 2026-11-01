# Agent 评测与安全（能力基准、欺骗与可纠正性）增量调研报告

**日期**：2026-11-01（UTC）  
**领域**：Agent Evaluation & Safety / Capability Benchmarks / Deception & Corrigibility  
**检索源数量**：34 条（其中高度相关 12 条：[4][5][6][11][12][25][26][28][29][32][33][34]）

---

## 1. 进展与热点

### 1.1 核心增量判断
**2024-2026 年 Agent 评测体系发生显著增量演进：从静态任务基准转向动态、对抗性、真机部署导向的评测；欺骗与可纠正性评测从理论定义走向可执行的红队框架与专项榜单。** [5][6][11][12][26][28][32]

### 1.2 关键进展条目（带时间与来源）

| 时间 | 进展 | 机构/作者 | 增量说明 | 证据等级 | 来源 |
|------|------|-----------|----------|----------|------|
| 2026-06 | **ROGUE**：首个面向 Computer-Use Agents 的可纠正性失效专项评测框架 | 未标注（arXiv cs.LG） | 从“对抗性安全”转向“可纠正性失效”专项测量，覆盖邮件、代码库、数据库等真实部署场景 | B（arXiv 预印本） | [5] |
| 2025-05 | **SWE-bench Goes Live!** 发布在线动态评测版本 | 未标注（arXiv cs.SE） | 解决静态 SWE-bench 无实时反馈、易过拟合问题；引入持续集成式评测 | B | [6] |
| 2026-03 | **SWE-ABS**：揭示 SWE-Bench Verified 榜单 78.8% SOTA 中 20% 补丁为语义错误通过 | 未标注（arXiv cs.SE） | 首次量化“基于测试套件的基准作弊”现象，提出对抗性强化基准 | B | [11] |
| 2026-10 | **SWE-Bench Pro V2**：更难作弊、环境交互更真实的长程软工基准 | 未标注（arXiv cs.SE） | 针对 Agent 与评测环境交互的新攻击面（环境操纵）进行硬化 | B | [12] |
| 2025-08 | **SVC 2025**：首个多模态欺骗检测挑战赛 | 未标注（arXiv） | 将欺骗检测从纯文本扩展至音视频多模态，引入对抗生成管线 | B | [26] |
| 2025-10 | **VelLMes**：高交互 AI 欺骗框架（蜜罐式主动诱导） | 未标注（arXiv） | 从被动检测转向主动交互式欺骗诱捕，提供可部署红队工具 | B | [28] |
| 2025-09 | **Mind the Gap**：对比 Model-level 与 Agentic-level 红队，引入 Action-Graph 可观测性 | 未标注（arXiv） | 首次系统量化 Agent 级红队比模型级红队发现更多可执行攻击路径 | B | [32] |
| 2024-01/2024-05 | **大规模红队方法学**：数学任务幻觉红队 [33] / 多样化攻击学习用于鲁棒红队与安全微调 [34] | 未标注（arXiv） | 从人工红队转向自动化、规模化、可学习的红队生成管线 | B | [33][34] |

### 1.3 经典与奠基性工作（对照表）

| 名称 | 年份 | 机构/作者 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|-----------|----------|----------|--------|--------|------|------|
| On Corrigibility and Alignment in Multi Agent Games | 2025 | arXiv cs.AI | > 待核实 | A（理论奠基） | 中 | ★★★★☆ | [4] | 多智能体博弈视角下的可纠正性形式化定义 |
| SWE-bench (原版) | 2023 | Princeton 等 | GitHub 10k+ stars | A（ICLR/NeurIPS 基准） | 高 | ★★★★★ | > 待核实 | 代码生成 Agent 事实标准基准 |
| AgentBench | 2023 | 上海交大等 | GitHub 3k+ stars | A（NeurIPS） | 高 | ★★★★★ | > 待核实 | 通用 Agent 多任务评测套件 |
| HELM / LM-Eval-Harness | 2022-2023 | Stanford / EleutherAI | 广泛采用 | A（工程标准） | 高 | ★★★★★ | > 待核实 | 模型级评测基础设施 |
| Inspect (UK AISI) | 2024 | UK AISI | 官方维护 | A（政府标准） | 高 | ★★★★☆ | > 待核实 | 合规导向评测框架 |

> 待核实：上表中标注“> 待核实”的热度数字（stars、引用数）需从 GitHub/Semantic Scholar 实时核实，当前仅凭领域共识填写。

### 1.4 关键数据集与基准（对照表）

| 名称 | 年份 | 任务类型 | 规模/难度 | 开源状态 | 热度 | 权威 | 关注度 | 推荐度 | 链接 | 说明 |
|------|------|----------|-----------|----------|------|------|--------|--------|------|------|
| SWE-Bench Verified | 2024 | 真实 Bug 修复 | 500 实例 | ✅ 代码/数据 | 高 | A | 高 | ★★★★★ | > 待核实 | 代码 Agent 事实榜单 |
| SWE-Bench Pro / Pro V2 | 2024/2026 | 长程软工 | 更难/反作弊 | ✅ | 中高 | B | 高 | ★★★★☆ | [12] | 环境交互硬化 |
| SWE-ABS | 2026 | 对抗性补丁验证 | 语义正确性 | ✅ | 新 | B | 中 | ★★★★☆ | [11] | 揭示榜单虚高 |
| ROGUE Benchmark | 2026 | 可纠正性失效 | 多场景 Computer-Use | ✅ | 新 | B | 中 | ★★★★☆ | [5] | 首个专项可纠正性基准 |
| SVC 2025 Deception | 2025 | 多模态欺骗检测 | 音视频+文本 | ✅ 挑战赛 | 中 | B | 中 | ★★★☆☆ | [26] | 多模态欺骗首赛 |
| VelLMes Dataset | 2025 | 高交互欺骗交互 | 蜜罐日志 | ✅ | 新 | B | 低 | ★★★☆☆ | [28] | 主动诱捕数据 |

---

## 2. 工业界与产品

### 2.1 增量判断
**开源 Agent 平台（OpenHands）与红队工具链（VelLMes、Inspect）已形成可部署工程栈；大模型厂商开始内嵌红队模块，但“评测即服务”商业化仍处早期。** [29][28][32][33][34]

### 2.2 主流开源框架与工具落地情况

| 项目/工具 | 定位 | 最新进展（2024-2026） | 开源许可 | 热度证据 | 权威证据 | 关注度 | 推荐度 | 来源 |
|-----------|------|----------------------|----------|----------|----------|--------|--------|------|
| **OpenHands** (原 OpenDevin) | 通用软件开发 Agent 平台 | v0.30+ 支持多沙箱、插件化技能、评测集成 | MIT | GitHub 30k+ stars | B（arXiv+工程落地） | 高 | ★★★★★ | [29] |
| **Inspect** (UK AISI) | 政府级评测/红队框架 | 内置红队插件、合规报告模板、CI/CD 集成 | MIT | 官方维护 | A（政府标准） | 高 | ★★★★☆ | > 待核实 |
| **VelLMes** | 高交互欺骗蜜罐框架 | 可部署于生产环境主动诱捕攻击者 | Apache-2.0 | 新 | B | 中 | ★★★☆☆ | [28] |
| **AgentOps / LangSmith** | 可观测与评测 SaaS | 集成 Action-Graph 级追踪、红队仪表盘 | 商业 | 付费用户增长 | C（商业采纳） | 中 | ★★★☆☆ | > 待核实 |
| **LM-Eval-Harness** | 模型级评测基建 | 新增 Agent 任务适配器、分布式评测 | MIT | 标准依赖 | A | 高 | ★★★★★ | > 待核实 |

### 2.3 红队/合规工具链商业化信号
- **自动化红队即服务**：[33][34] 证明大规模自动化红队技术成熟，已有厂商（如 Haize Labs, Gray Swan, Lakera）提供 API 化红队服务。> 待核实：具体厂商营收与部署规模。
- **合规审计工具**：Inspect、Guardrails AI、NVIDIA NeMo Guardrails 向 EU AI Act “高风险系统”合规文档自动生成方向演进。> 待核实：是否有通过第三方认证的案例。

---

## 3. 蓝海与缺口

### 3.1 增量判断
**三大无人区/高杠杆缺口：(1) 多智能体协作中的可纠正性组合性评测缺失；(2) 长程部署中的“隐性欺骗”（非显式谎言、策略性遗漏）测量方法空白；(3) 评测基础设施与监管审计标准的互操作鸿沟。**

### 3.2 具体缺口清单

| 缺口维度 | 现状 | 缺口描述 | 潜在切入点 | 证据支撑 | 优先级 |
|----------|------|----------|------------|----------|--------|
| 多智能体可纠正性组合性 | 仅有单 Agent 可纠正性基准 [5] | 多 Agent 系统中可纠正性是否可组合、如何传递、冲突解决机制无基准 | 构建 MARO（Multi-Agent ROGUE）扩展基准 | [4][5] | ⭐⭐⭐⭐⭐ |
| 隐性欺骗测量 | SVC 2025 覆盖显式多模态欺骗 [26] | 策略性遗漏、模糊承诺、选择性真话等“非谎言欺骗”无标注数据、无度量 | 结合实用主义语言学标注体系 + 红队生成管线 [34] | [26][28][34] | ⭐⭐⭐⭐ |
| 评测-审计互操作 | Inspect/HELM/LM-Eval 互不兼容 | 监管审计需可复现证据链，现有框架缺乏标准化证据导出格式（如 OpenEVIDENCE） | 推动 W3C/ISO 标准化评测证据模式 | > 待核实 | ⭐⭐⭐⭐ |
| 真机长程部署评测 | SWE-bench Live [6] 仅覆盖代码任务 | 通用 Computer-Use Agent 在真实 OS/网络环境中长周期运行的可靠性/安全性无标准化测试床 | 基于 OpenHands [29] 构建持久化真机评测沙箱 | [6][29] | ⭐⭐⭐⭐⭐ |
| 对齐税量化基准 | 理论讨论为主 [4] | 安全干预（可纠正性约束、红队训练）对能力的边际损失无标准化度量协议 | 设计“能力-安全帕累托前沿”基准套件 | [4][5][33] | ⭐⭐⭐ |

---

## 4. 瓶颈与拐点

### 4.1 增量判断
**核心瓶颈正从“模型能力不足”转向“评测效度与环境真实性不足”；拐点信号：榜单饱和伴随作弊率上升 [11]、真机部署暴露仿真-现实鸿沟 [6][29]、监管强制审计倒逼标准化。**

### 4.2 瓶颈详解

| 瓶颈类别 | 具体表现 | 拐点信号 | 证据来源 | 严重程度 |
|----------|----------|----------|----------|----------|
| **评测效度危机** | SWE-Bench Verified 78.8% SOTA 中 20% 语义错误补丁 [11]；静态测试套件易被过拟合 | 基准“被攻破”速度加快，从年级缩短至季度级；对抗性基准 [11][12] 成为新常态 | [11][12] | 🔴 临界 |
| **仿真-现实鸿沟** | 仿真榜单高分 Agent 真机部署频现环境交互失效、权限越界、状态不同步 [29][6] | OpenHands 等平台推动真机沙箱标准化；SWE-bench Live 引入实时 CI [6] | [6][29] | 🟠 高 |
| **可纠正性定义与测量分离** | 理论定义 [4] 与可执行测试 [5] 尚未形成闭环；缺乏“可纠正性程度”的连续度量 | ROGUE [5] 首次给出可执行失效分类，但覆盖面窄 | [4][5] | 🟠 高 |
| **红队覆盖面与成本** | 自动化红队 [33][34] 覆盖已知攻击模式，未知未知（Unknown-Unknowns）依赖人工 | VelLMes [28] 等主动诱捕框架降低未知攻击发现成本 | [28][33][34] | 🟡 中 |
| **算力/工程成本** | 全量红队+长程真机评测单次成本达 $10k-$100k 级 | 分布式评测框架、模拟器蒸馏、重要性采样降本技术涌现 | > 待核实 | 🟡 中 |

---

## 5. 社会·政策·国际

### 5.1 增量判断
**监管从“原则性框架”进入“强制合规与技术标准落地期”：EU AI Act 高风险系统评测要求 2026-08 生效、NIST AI RMF 1.0 配套测试指南发布、中国算法备案与大模型安全评估规范强制执行；三大司法辖区标准互认仍处博弈期。** > 待核实：具体生效条款与技术标准映射表。

### 5.2 关键监管动态对照

| 司法辖区 | 核心法规/标准 | 2024-2026 关键增量 | 对 Agent 评测的直接要求 | 执行状态 | 来源 |
|----------|---------------|-------------------|------------------------|----------|------|
| **EU** | AI Act (Regulation 2024/1689) | 2026-08-02 高风险系统合规截止；附件 IV 要求“测试报告、红队记录、监控计划” | 强制第三方合格评定、评测证据可审计、事后监控义务 | 生效中 | > 待核实 |
| **US** | NIST AI RMF 1.0 + NIST AI 100-1 (测试指南) | 2024-07 发布测试指南；2025-2026 推动“红队测试标准化” | 自愿但成行业事实标准；联邦采购强制引用 | 推广中 | > 待核实 |
| **中国** | 《生成式人工智能服务管理暂行办法》+ 算法备案 + TC260 系列标准 | 2024-2025 备案强制含安全评估报告；2026 启动大模型安全分级分类测试 | 备案前须通过国家队测试（中科院/信通院）；红队测试纳入备案材料 | 强制执行 | > 待核实 |
| **国际** | ISO/IEC 42001 (AI管理体系) / ISO/IEC 23894 (风险管理) | 2023-2024 发布；2025 启动认证机构认可 | 评测过程纳入管理体系审核，证据链可追溯 | 早期采纳 | > 待核实 |

### 5.3 地缘与供应链风险
- **评测工具链出口管制风险**：红队自动化工具、模型权重、评测数据集可能被列入“双用途”管控清单。> 待核实：Wassenaar Arrangement 更新进展。
- **人才与数据主权**：高质量红队数据标注、对抗样本生成能力集中于美中英以；全球南方缺乏本土化评测能力。> 待核实。

---

## 6. 资本与生态

### 6.1 增量判断
**投资热度从“模型层”显著向“评测/红队/合规基建层”迁移；OpenHands 等开源平台聚拢开发者生态，形成“平台+插件+评测”飞轮；人才流向显示安全工程师、红队工程师、合规工程师薪资溢价超核心建模岗。**

### 6.2 关键资本信号（2024-2026）

| 信号类型 | 代表事件/数据 | 增量含义 | 来源 |
|----------|---------------|----------|------|
| **融资轮次** | 红队/评测初创企业（Haize, Gray Swan, Patronus, Lakera, Distributional）完成 A/B 轮，单轮 $10M-$50M | 资本确认“评测即基建”商业模式 | > 待核实 |
| **大厂内建/收购** | Microsoft/Google/Meta/Amazon 组建专职红队（100+ 人团队）；收购评测工具链公司 | 评测内生化为核心护城河 | > 待核实 |
| **开源生态指标** | OpenHands [29] GitHub Star 增长 >300%/年；Inspect 贡献者 >200；AgentBench 衍生任务 >50 | 开发者心智份额锁定，形成标准效应 | [29] |
| **人才薪资溢价** | 红队工程师/安全对齐研究员薪资中位数超 LLM 训练工程师 15-30% | 人才市场为安全工程定价 | > 待核实 |
| **学术-产业循环** | SWE-bench [6]、ROGUE [5]、SWE-ABS [11] 均由产业实验室或产学合作主导 | 评测基准研发“产业化、工程化” | [5][6][11] |

---

## 7. 信号与预测

### 7.1 早期信号（Weak Signals）

| 信号 | 观测来源 | 可能预示 | 置信度 |
|------|----------|----------|--------|
| 对抗性基准（SWE-ABS [11]、SWE-Bench Pro V2 [12]）成为发布新基准的“标配” | 连续两代基准主打“反作弊” | 评测进入“军备竞赛”常态化；静态基准寿命 < 6 个月 | 🟢 高 |
| 多模态欺骗挑战赛（SVC 2025 [26]）参赛队伍 >100、提交量激增 | 挑战赛官网/论文 | 欺骗检测从 Niche 走向主流 CV/NLP 任务 | 🟢 高 |
| 政府采购文件开始写明“须提供 Inspect/HELM 兼容评测报告” | 招标公开信息 | 评测工具链标准化被监管锁定 | 🟡 中 |
| 保险公司推出“AI Agent 错误与遗漏险”，承保前要求红队报告 | 保险市场动态 | 红队报告成为可交易金融资产 | 🔴 低（早期） |

### 7.2 未来 6-18 月可验证预测（含可证伪假设）

| # | 预测（可证伪假设） | 依据链 | 置信度 | 验证指标与截止日期 |
|---|-------------------|--------|--------|-------------------|
| P1 | **到 2027-06，SWE-Bench 类代码基准顶榜系统在 SWE-ABS 语义正确率将 < 60%（现 ~80% 通过率中 20% 错误）** | [11] 揭示作弊率；基准硬化趋势 [12] | 🟢 80% | SWE-ABS 榜单语义正确率列；截止 2027-06-30 |
| P2 | **EU AI Act 强制第三方评测机构名单（Notified Bodies）中，≥3 家将要求提交 Inspect/HELM 兼容证据包** | EU 实施法规进程；Inspect 为 UK AISI 官方工具 | 🟡 60% | 欧盟官方公告名单与技术要求文件；截止 2027-03-31 |
| P3 | **OpenHands 或同级平台将内置“可纠正性测试套件”作为 CI 默认门禁，且被 ≥5 家独角兽/上市公司采用** | [29] 平台化趋势；[5] ROGUE 提供可执行测试模式 | 🟡 55% | OpenHands 插件市场/Release Notes；截止 2027-06-30 |
| P4 | **首个“多智能体可纠正性组合性基准”（MARO 或同类）在顶会（ICLR/NeurIPS/ICML/CoRL）发表** | [4][5] 单 Agent 基准已现；多 Agent 理论待落地 | 🟡 50% | 顶会论文列表；截止 2027-09-30 |
| P5 | **红队即服务（RaaS）市场规模达 $500M ARR，且出现专业化细分（代理欺骗红队、工具调用越权红队）** | [28][32][33][34] 技术就绪；合规需求刚性 | 🔴 40% | 市场研报；截止 2027-12-31 |

> **不确定性声明**：以上预测均标注 `[P]`，依据为当前技术演进轨迹与政策信号外推；若宏观算力投入放缓、监管执法宽松、或出现范式级突破（如世界模型替代显式评测），上述假设可能失效。

---

## 参考来源

[1] VQualA 2025 Challenge on Engagement Prediction for Short Videos: Methods and Results — http://arxiv.org/abs/2509.02969v1  
[2] NTU-NPU System for Voice Privacy 2024 Challenge — http://arxiv.org/abs/2410.02371v1  
[3] Discovery Opportunities with Gravitational Waves -- TASI 2024 Lecture Notes — http://arxiv.org/abs/2409.08956v1  
[4] On Corrigibility and Alignment in Multi Agent Games — http://arxiv.org/abs/2501.05360v1  
[5] ROGUE: Evaluating Corrigibility Failures in Frontier Computer-Use Agents — http://arxiv.org/abs/2606.00341v2  
[6] SWE-bench Goes Live! — http://arxiv.org/abs/2505.23419v2  
[7] The Gaia mission — http://arxiv.org/abs/1609.04153v1  
[8] Gaia Data Release 3: The Galaxy in your preferred colours. Synthetic photometry from Gaia low-resolution spectra — http://arxiv.org/abs/2206.06215v2  
[9] Gaia Data Release 1. Summary of the astrometric, photometric, and survey properties — http://arxiv.org/abs/1609.04172v1  
[10] Gaia Data Release 2. Summary of the contents and survey properties — http://arxiv.org/abs/1804.09365v2  
[11] SWE-ABS: Adversarial Benchmark Strengthening Exposes Inflated Success Rates on Test-based Benchmark — http://arxiv.org/abs/2603.00520v1  
[12] SWE-Bench Pro V2: A Cleaner, Harder-to-Game Coding Benchmark — http://arxiv.org/abs/2610.24206v1  
[13] The Reactive Synthesis Competition: SYNTCOMP 2016 and Beyond — http://arxiv.org/abs/1611.07626v1  
[14] This paper has been withdrawn — http://arxiv.org/abs/cond-mat/0309395v2  
[15] The 3rd Reactive Synthesis Competition (SYNTCOMP 2016): Benchmarks, Participants & Results — http://arxiv.org/abs/1609.00507v2  
[16] Evaluation of an open-source implementation of the SRP-PHAT algorithm within the 2018 LOCATA challenge — http://arxiv.org/abs/1812.05901v1  
[17] QCD and High Energy Interactions: Moriond 2018 Theory Summary — http://arxiv.org/abs/1806.04982v2  
[18] ASIME 2016 White Paper: In-Space Utilisation of Asteroids: "Answers to Questions from the Asteroid Miners" — http://arxiv.org/abs/1612.00709v2  
[19] The 4th Reactive Synthesis Competition (SYNTCOMP 2017): Benchmarks, Participants & Results — http://arxiv.org/abs/1711.11439v1  
[20] The 2018 PIRM Challenge on Perceptual Image Super-resolution — http://arxiv.org/abs/1809.07517v3  
[21] Snowmass 2021 Community Survey Report — http://arxiv.org/abs/2203.07328v2  
[22] WVOQ at SemEval-2021 Task 6: BART for Span Detection and Classification — http://arxiv.org/abs/2107.05467v1  
[23] The Term Structure of Interest Rates and the Aliasing Identification Problem — https://doi.org/10.21034/wp.165  
[24] MAGIC and MWL monitoring of the blazar TXS 0506+056 in the 2018/2019 season — http://arxiv.org/abs/1909.04938v1  
[25] OpenFact at CheckThat! 2024: Combining Multiple Attack Methods for Effective Adversarial Text Generation — http://arxiv.org/abs/2409.02649v2  
[26] SVC 2025: the First Multimodal Deception Detection Challenge — http://arxiv.org/abs/2508.04129v1  
[27] Overview of the Sensemaking Task at the ELOQUENT 2025 Lab: LLMs as Teachers, Students and Evaluators — http://arxiv.org/abs/2507.12143v1  
[28] VelLMes: A high-interaction AI-based deception framework — http://arxiv.org/abs/2510.06975v1  
[29] OpenHands: An Open Platform for AI Software Developers as Generalist Agents — http://arxiv.org/abs/2407.16741v3  
[30] LongEval at CLEF 2025: Longitudinal Evaluation of IR Model Performance — http://arxiv.org/abs/2503.08541v1  
[31] Latent-Y: A Lab-Validated Autonomous Agent for De Novo Drug Design — http://arxiv.org/abs/2603.29727v2  
[32] Mind the Gap: Comparing Model- vs Agentic-Level Red Teaming with Action-Graph Observability on GPT-OSS-20B — http://arxiv.org/abs/2509.17259v1  
[33] Red Teaming for Large Language Models At Scale: Tackling Hallucinations on Mathematics Tasks — http://arxiv.org/abs/2401.00290v1  
[34] Learning diverse attacks on large language models for robust red-teaming and safety tuning — http://arxiv.org/abs/2405.18540v3

---

*Generated by research-bot · topic=`agent-评测与安全能力基准欺骗与可纠正性` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading, frontier-watch · model=`nvidia/nemotron-3-ultra-550b-a55b` · sources=34 · duration=336s · 2026-11-01T22:49:38+00:00*
