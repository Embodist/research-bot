# Vision-Language-Action (VLA) 基础模型调研报告

**元信息**｜调研日期：2026-10-02（UTC）｜领域：具身智能 / 机器人学习 / Vision-Language-Action｜检索源数量：36 条候选来源，其中与 VLA 直接相关约 21 条，无关噪声约 15 条｜证据分级：A 同行评审 / B 一手预印本与官方仓库 / C 第三方复现与榜单 / D 二手解读

> **检索质量与证据缺口声明（重要）**
> 本轮针对子问题 q1（VLA 经典奠基与技术演进脉络）的 4 条候选来源**全部偏航**：检索词「RT」在中文语境下被高概率歧义解析为俄罗斯官方媒体 Russia Today [1][2][4] 与网络流行语「如题」[3]，命中率 0/4。因此本文「经典与奠基性工作」章节的部分条目**依赖领域种子资源而非本轮实时检索结果**，凡未经本轮一手来源核实的条目，均在表中单独标注 `种子资源·未实时核实`，正文对应论断标注 `> 待核实`。请勿将种子资源中的链接与年份当作本轮已核验结论使用。

---

## 摘要（Executive Summary）

1. **动作表征是近两年 VLA 最实质的架构变化。** Physical Intelligence 的 π0（2024-10 首发，v4 修订至 2026-01-08）在预训练 VLM 之上叠加 **flow matching** 动作生成架构，明确以「继承互联网规模语义知识」为目标 [13]，标志着头部 VLA 从**离散动作 token 自回归**向**连续生成式动作建模**的关键转向。证据等级：B（一手 arXiv 摘要）[13]。
2. **两条动作表征路线并非替代而是并存。** 官方 openpi 仓库同时托管三类模型：基于 flow 的 π0、基于 **FAST action tokenizer** 的自回归 π0-FAST、以及 π0.5 [15]。这直接证明「流匹配」与「动作 tokenization」在工程上是并行分支，而非单线演进。证据等级：B（官方仓库）[15]。
3. **开源工程实践的两极：OpenVLA 与 openpi。** OpenVLA 是 7B 参数开源 VLA，官方仓库持续维护，并**专门增设「VLA Performance Troubleshooting」章节**以应对微调后性能不佳这一普遍问题 [25][26]——这是 VLA 复现困难的**一手工程证据**，价值高于任何二手抱怨。证据等级：B [25][26]。
4. **跨本体泛化是这一代 VLA 的核心卖点，但缺乏独立第三方评测。** π0 的训练数据来自多种灵巧机器人平台 [13]；中文二手来源进一步声称「一套框架控制 7 种不同品牌机械臂」[14]，但**未给出任务数、成功率口径、真机/仿真区分**。证据等级：C/D，数字 `> 待核实`。
5. **评测基准正在扩张。** 除经典仿真基准（LIBERO 等种子资源）外，本轮检索到 **VLA-Arena**（PKU-Alignment 的开源系统化评测基准）[33]，以及 2026 年 IEEE RA-L 关于**免微调推理时策略引导**的部署方向工作 [34]。
6. **最大缺口**：本轮**未获得任何一手实验表格**，π0-FAST「训练快 5 倍且效果相当」等数字仅见于中文二手解读 [14][16]，属高优先级待核实项。

---

## 一、关键前沿进展（近 12–24 个月，即 2024-10 → 2026-10）

### 1.1 π0 系列：从流匹配到版本谱系

| 时间 | 事项 | 来源 | 证据等级 |
|------|------|------|----------|
| 2024-10-31 | π0 预印本 v1 提交，提出在预训练 VLM 上构建 flow matching VLA | [13] | B（一手） |
| 2026-01-08 | π0 更新至 v4，说明工作被持续修订，**引用须注意版本号** | [13] | B（一手） |
| 2025 | openpi 官方仓库同时开源 π0（flow）、π0-FAST（自回归 + FAST tokenizer）、π0.5 | [15] | B（官方仓库） |
| 2025 | π0.5 论文（*A Vision-Language-Action Model with Open-World Generalization*）出现中文详解 | [17] | C（二手解读） |

- π0 的核心技术主张可用其摘要原句概括：构建于预训练 VLM 之上的 flow matching 架构，以「inherit Internet-scale semantic knowledge」[13]。这是 2024 年后 VLA 动作表征转向的**一手锚点**。
- π0.5 已在官方 openpi 仓库中列明 [15]，**属于已确认存在的官方模型**；而社区材料中出现的 π0.6、π0.7 提法 [14] 仅有栏目命名，缺参数、指标与官方链接。
  > 待核实：π0.6 / π0.7 是否真实存在、是否有正式技术报告或权重发布。当前证据等级 D。
- 二手来源称 π0-FAST「比扩散/流匹配版 π0 训练速度快约 5 倍但效果相当」[14][16]。
  > 待核实：该数字为二手解读，本轮**无官方实验表格或第三方复现支撑**，不可作为结论引用。

### 1.2 部署侧：免微调的推理时策略引导

本轮检索到 2026 年 IEEE Robotics and Automation Letters 的补充材料条目 *Towards Deploying VLA Without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering Via Embodied Evolutionary Diffusion* [34]。该工作指向一个明确痛点：**真机部署中为每个新任务微调 VLA 成本过高**，转而尝试推理时（inference-time）策略引导。证据等级：A（期刊条目）/ 但本轮仅见补充视频材料页，正文内容 `> 待核实`。

### 1.3 评测侧：VLA-Arena

**VLA-Arena**（PKU-Alignment 维护）定位为「open-source benchmark for systematic evaluation」[33]，指向当前 VLA 评测碎片化问题。证据等级：B（官方仓库），但榜单规模、任务集与 SOTA 数值 `> 待核实`。

### 1.4 中文社区脉络梳理

一篇标题为「具身智能模型发展脉络：从 RT-1 到 π*0.6」的博客文章 [5] 提供了中英文术语对照与演进叙事，本轮将其作为**线索性**来源（D 级二手）。注：该条目的 URL 在检索结果中呈编码/截断状态，**链接可访问性存疑**，不宜作为唯一依据。

---

## 二、方法范式对比（离散动作 / 扩散 / Flow Matching / 双系统）

| 范式 | 动作表征 | 代表工作 | 关键特征 | 本轮证据状态 |
|------|----------|----------|----------|--------------|
| **离散动作 token 自回归** | 动作离散化为 token，与语言 token 共用序列空间 | RT-2（种子资源）、OpenVLA [26] | 复用 VLM 权重与语言接口，天然支持多模态提示 | OpenVLA 为一手 [26][25]；RT-2 仅种子资源 `种子资源·未实时核实` |
| **扩散式动作生成（Diffusion）** | 连续动作轨迹作为去噪目标 | Diffusion Policy（种子资源） | 可建模多模态动作分布，推理需多步去噪 | 仅种子资源，本轮无一手来源 `种子资源·未实时核实` |
| **Flow Matching** | 连续时间流场，直接回归速度场 | π0 [13] | 构建于预训练 VLM 之上；训练目标比扩散更直接 | B（一手 arXiv 摘要）[13][14] |
| **自回归 + FAST 动作 tokenizer** | 压缩后的动作 token | π0-FAST [15] | 与 flow 版并存；据二手来源称训练更快、适配高频灵巧任务 | 官方仓库确认存在 [15]；性能数字 `> 待核实` [14][16] |
| **双系统 / 分层（System 1 + System 2）** | 慢速语义规划 + 快速动作执行解耦 | π0 的「预训练 VLM + 动作专家」结构可作类比 | 兼顾语义泛化与实时控制频率 | **归纳性判断**，本轮无直接来源 `> 待核实` |

**要点说明**

1. **「离散 vs 连续」是主分界线，而非「谁取代谁」。** openpi 同时托管 flow 版 π0 与自回归版 π0-FAST [15]，是最直接的并存证据。二者的取舍更像是**训练效率 / 高频任务适配**与**生成质量**之间的工程权衡。
2. **Flow Matching 的推广逻辑在于「复用 VLM 权重」** [13]。相较从零训练的扩散策略（种子资源），π0 路线把互联网规模语义知识当作免费先验。
3. **「双系统」在本文中属谨慎归纳。** 严格意义上的 System 1/System 2 双系统 VLA（如慢思考 VLM + 快反射动作头）需要独立一手来源支撑；本轮未检索到，因此不列为已证实范式。
   > 待核实：双系统 VLA 的代表性工作、机构与指标。

---

## 三、经典与奠基性工作

> 本章为**证据薄弱区**：q1 检索全部偏航 [1][2][3][4]，多数条目来自领域种子资源，未在本轮实时核验。表中「证据」列明确区分。

| 名称 | 年份 | 机构/作者 | 链接 | 说明 | 证据 |
|------|------|-----------|------|------|------|
| **RT-1**（Robotics Transformer for Real-World Control at Scale） | 2022 | Google Research | https://arxiv.org/abs/2212.06817 | 大规模真机 Transformer 模仿学习奠基工作 | 本轮命中一手 arXiv [12] 与二手解读 [10][11]；未精读全文 |
| **RT-2**（Vision-Language-Action Models Transfer Web Knowledge to Robotic Control） | 2023 | Google DeepMind | https://arxiv.org/abs/2307.15818 | VLM 直接输出动作 token，展现涌现泛化 | `种子资源·未实时核实` |
| **Diffusion Policy**（Visuomotor Policy Learning via Action Diffusion） | 2023 | Columbia / Toyota | https://arxiv.org/abs/2303.04137 | 扩散式动作生成范式 | `种子资源·未实时核实` |
| **ACT / ALOHA**（Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware） | 2023 | Stanford | https://arxiv.org/abs/2304.13705 | 低成本双臂遥操作 + ACT 算法 | `种子资源·未实时核实` |
| **Open X-Embodiment / RT-X** | 2023 | Open X-Embodiment Collaboration | https://arxiv.org/abs/2310.08864 | 跨本体大规模数据集与 RT-X 模型 | `种子资源·未实时核实` |
| **Octo**（An Open-Source Generalist Robot Policy） | 2024 | UC Berkeley | https://arxiv.org/abs/2405.12213 | 开源通用策略，灵活观测/动作头 | `种子资源·未实时核实` |
| **OpenVLA** | 2024 | Stanford et al. | https://arxiv.org/abs/2406.09246 | 7B 开源 VLA，广泛用作基线 | 一手 arXiv [26] + 官方仓库 [25] + 项目页 [27]（本轮验证存在） |
| **π0**（A Vision-Language-Action Flow Model for General Robot Control） | 2024（v4 2026） | Physical Intelligence | https://arxiv.org/abs/2410.24164 | flow matching 动作专家，跨本体 | 一手 arXiv [13] + 官方仓库 [15]（本轮验证存在） |

**承上启下关系（谨慎表述）**

按种子资源与命中来源可勾勒的粗线索是：**模块化模仿学习（RT-1 / ACT / Diffusion Policy）→ 端到端 VLA（RT-2 / Octo / OpenVLA）→ 生成式动作建模（π0 flow matching）**。但必须强调：

> 待核实：上述演进链条中「动作离散化 / token 化 → 流匹配」的技术继承细节，以及每一步相对前作的具体增量（数据规模、架构、训练目标），在**本轮证据中完全没有一手支撑**，系依据种子资源与标题层面的推断。任何用于正式汇报的版本都必须回到 arXiv 原文与官方仓库重建证据链。

唯一可确认的相邻事实是：RT-1 有可访问的一手 arXiv 记录 [12]，且中文二手来源提及其在约 700 条指令上的真机评测 [11]。
> 待核实：RT-1 的指令数与成功率具体数值，需回原文核实 [11][12]。

---

## 四、开源项目与工程实践

| 名称 | 年份 | 机构/作者 | 链接 | 说明 |
|------|------|-----------|------|------|
| **openvla/openvla** | 2024 | Stanford et al. | https://github.com/openvla/openvla | OpenVLA 官方实现；含微调排错指南与 LIBERO 复现说明 [25] |
| **Physical-Intelligence/openpi** | 2025 | Physical Intelligence | https://github.com/Physical-Intelligence/openpi | 官方托管 π0（flow）、π0-FAST（FAST tokenizer）、π0.5 [15] |
| **octo-models/octo** | 2024 | UC Berkeley | https://github.com/octo-models/octo | Octo 通用策略官方实现 `种子资源·未实时核实` |
| **tonyzhaozh/aloha** | 2023 | Stanford | https://github.com/tonyzhaozh/aloha | ALOHA / ACT 硬件与代码 `种子资源·未实时核实` |
| **real-stanford/diffusion_policy** | 2023 | Columbia / Toyota | https://github.com/real-stanford/diffusion_policy | Diffusion Policy 官方实现 `种子资源·未实时核实` |
| **PKU-Alignment/VLA-Arena** | — | PKU-Alignment | https://github.com/PKU-Alignment/VLA-Arena | 开源 VLA 系统化评测基准 [33] |
| **LeRobot π0 集成页** | — | Hugging Face | https://hugging-face.cn/docs/lerobot/pi0 | 第三方框架对 π0 的封装文档 [19] |

### 4.1 复现困难的**一手**证据

本轮最有价值的工程发现来自 OpenVLA 官方仓库的更新记录：官方于 2024-10-15 **专门增设「VLA Performance Troubleshooting」章节**，提供微调后性能不佳的调试最佳实践 [25]。这意味着：

- 「微调后效果不如预期」不是个别用户的误用，而是**官方认可的普遍现象**；
- 复现难度不仅在于算力，更在于**超参、数据配比、观测/动作归一化等隐性工程细节**。

同时，OpenVLA 官方将 **LIBERO 仿真基准的微调实验纳入论文 v2，并提供在 LIBERO 中复现结果的说明** [25]，说明该基准已进入其复现链路。

### 4.2 第三方封装的效果争议

中文二手来源称「LeRobot 对 π0 的封装在效果上逊于官方 openpi」[14]，而 Hugging Face LeRobot 确实提供了 π0 集成页面 [19]。

> 待核实：该性能差异**无任何量化对比**，仅为主观陈述，证据等级 D。工程选型时应以官方 openpi [15] 为基准实现，第三方封装的性能损失需自行复现测量。

### 4.3 工程栈成熟度评估

- **可复现性好**：openpi [15]、openvla/openvla [25] 均为官方维护、README 持续更新。
- **可复现性存疑**：Octo / ALOHA / Diffusion Policy 仓库本轮**未被实时访问**，仅有种子链接。
- **部署门槛**：π0 部署涉及 PyTorch / CUDA 版本与驱动兼容问题，中文二手来源有专门整理 [22][24]。
  > 待核实：这些兼容性表格的准确性未经官方文档交叉验证。

---

## 五、数据集与评测基准

| 名称 | 年份 | 机构/作者 | 链接 | 说明 | 证据 |
|------|------|-----------|------|------|

## 参考来源

[1] RT  News —  RT — https://www.rt.com/on-air/
[2] RT  中国 — https://rtchina.cn/
[3] rt （网络流行语）_百度百科 — https://baike.baidu.com/item/rt/1474
[4] News  —  RT — https://www.rt.com/bulletin-board/news/
[5] 具身智能模型发展脉络:从  RT-1   到π*  0  .6 - sasasatori - 博客园 — hedJjaC291P3yGwc7N55kLSc2ls_Ks2xOzRb1UlDTtolAAi3AZwQct0IqRBhsoin
[6] 今日俄罗斯_百度百科 — https://baike.baidu.com/item/%E4%BB%8A%E6%97%A5%E4%BF%84%E7%BD%97%E6%96%AF/9238633
[7] 运费如何计算以及海运报价50usd/ RT 中的 RT 是啥意思？ — https://zhuanlan.zhihu.com/p/476123091
[8] 货代海运报价的 RT 是指什么？（海运 RT 如何计算）-百运网 — https://www.by56.com/news/37140.html
[9] RT -Thread — https://www.rt-thread.org/
[10] 学习笔记— RT-1 :  ROBOTICS TRANSFORMER  FOR REAL-WORLD CONTROL AT SCALE_, google   rt-1 ( robotics transformer  1)架构-CSDN博客 — https://blog.csdn.net/wdwjw/article/details/156381744
[11] 谷歌    RT-1  模型让一个  机器人  干几份活,700条指令成功..._知乎 — hedJjaC291OfPyaFZYFLI4KQWvqt63NBCQYmS-LeT41zs3L1v0fEFQ..
[12] RT-1: Robotics Transformer for Real-World Control at Scale - arXiv — https://arxiv.org/abs/2212.06817
[13] [2410.24164] $π_0$: A Vision-Language-Action Flow Model for … — https://arxiv.org/abs/2410.24164
[14] π0——用于通用机器人控制的VLA模型：一套框架控制7种 ... — https://blog.csdn.net/v_JULY_v/article/details/143472442
[15] GitHub - Physical-Intelligence/openpi — https://github.com/Physical-Intelligence/openpi
[16] 2025 | π0、π0-FAST、π0.5通用具身智能技术解读 - 知乎 — https://zhuanlan.zhihu.com/p/1918794606549636945
[17] 结合代码 介绍一下 π0.5: a  Vision-Language-Action  Model with Open-World Generalization 这篇论文_ pi0 .5代码详解-CSDN博客 — https://blog.csdn.net/luoganttcc/article/details/153639287
[18] 地表最强机器人大模型? π0 模型详细解读 - 知乎 — https://zhuanlan.zhihu.com/p/11883552553
[19] π₀ ( Pi0 ) · Hugging Face - 抱抱脸文档 — https://hugging-face.cn/docs/lerobot/pi0
[20] Physical Intelligence (π) — https://www.pi.website/
[21] Model 复现系列（三）π0 -- Physical Intelligence Pi-zero（ Pi0 ） — https://blog.csdn.net/nenchoumi3119/article/details/148688800
[22] Pi0 视觉语言动作流模型部署:PyTorch 2.7 CUDA版本匹配与驱动兼容表-CSDN博客 — https://blog.csdn.net/weixin_31800911/article/details/158756110
[23] Comment on the Paper Titled ’The Origin of Quantum Mechanical Statistics: Insights from Research on Human Language’ (arXiv preprint arXiv:2407.14924, 2024) — https://doi.org/10.20944/preprints202411.2377.v1
[24] Pi0 视觉-语言-动作流模型企业应用:低成本GPU算力适配方案详解-CSDN博客 — https://blog.csdn.net/weixin_29781865/article/details/157661185
[25] OpenVLA: An open-source vision-language-action model - GitHub — https://github.com/openvla/openvla
[26] [2406.09246] OpenVLA: An  Open-Source  Vision-Language-Action  Model — https://arxiv.org/abs/2406.09246
[27] OpenVLA: An Open-Source Vision-Language-Action Model — https://openvla.github.io/
[28] OpenFrp  开放映射 — 免费内网穿透_免费端口映射_高速_不 ... — https://www.openfrp.net/
[29] Opensource VLA.com for sale | Spaceship.com — http://opensourcevla.com/
[30] Fine-tuning Llama For Better Performance With the MMLU Benchmark — https://doi.org/10.31219/osf.io/e3v5x
[31] Open  VPN官网中文站 — https://www.openvpncn.com/
[32] Demo Bytes:  Fine-Tuning   Open-Source  Models made easy with KAITO | Microsoft Reactor — https://developer.microsoft.com/zh-cn/reactor/events/23697/
[33] VLA-Arena is an open-source benchmark for systematic evaluation ... — https://github.com/PKU-Alignment/VLA-Arena
[34] Towards Deploying VLA Without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering Via Embodied Evolutionary Diffusion_supp1-3678455.mp4 — https://doi.org/10.1109/lra.2026.3678455/mm1
[35] open （英文单词）_百度百科 — https://baike.baidu.com/item/open/497859
[36] OpenVLA: An  Open-Source  Vision-Language-Action  Model — https://arxiv.org/html/2406.09246v1


---

*Generated by research-bot · topic=`vla` · depth=`quick` · rounds=1 · engines=arxiv, openalex, crossref, semantic_scholar, github, bing, sogou, so360, searxng · skills=deep-research, frontier-tracking, paper-survey, evidence-grading · model=`deepseek-v4-flash` · sources=36 · duration=607s · 2026-10-02T03:56:38+00:00*
