---
name: vla
description: Vision-Language-Action (VLA) 模型领域知识。覆盖架构范式、动作 token 化、跨本体泛化、代表模型与数据集，用于追踪 VLA 前沿。
---

# Vision-Language-Action (VLA)

## 定义
VLA 把视觉观测 + 语言指令直接映射为机器人动作，通常以预训练 VLM 为骨干，输出离散动作 token 或连续动作 chunk。

## 架构范式
1. **离散动作 token 化**：把动作分箱成 token，复用 LLM 词表
   - RT-1（2022）→ RT-2（2023，VLM 直接输出动作 token）
2. **连续动作头 / Diffusion / Flow Matching**
   - Diffusion Policy（2023）、π0 系列（flow matching action expert）
   - ACT（CVAE + chunking，ALOHA）
3. **双系统 System1/System2**
   - 高层 VLM 规划 + 低层高频动作策略（如 GR 系列、Helix、Gemini Robotics）
4. **空间/3D 增强**：SpatialVLA、3D-VLA、point-cloud 输入
5. **跨本体（Cross-embodiment）**：统一动作空间、本体 token、Open X-Embodiment 训练

## 代表模型（按时间）
| 模型 | 年份 | 机构 | 要点 |
|------|------|------|------|
| RT-1 | 2022 | Google | Transformer 模仿，大规模真机 |
| PaLM-E | 2023 | Google | 具身多模态 LLM |
| RT-2 | 2023 | Google DeepMind | VLM→动作 token，涌现泛化 |
| Octo | 2023 | Berkeley | 开源通用策略，Transformer 扩散头 |
| OpenVLA | 2024 | Stanford 等 | 开源 7B VLA，基于 Prismatic VLM |
| RDT-1B | 2024 | 清华 | 扩散式双手机器人基础模型 |
| π0 | 2024 | Physical Intelligence | flow matching + VLM，跨本体 |
| GR-1 / GR-2 / GR-3 | 2024-25 | 字节 | 视频预训练 + 机器人数据 |
| Gemini Robotics | 2025 | Google DeepMind | VLM + 动作，强调泛化与安全 |
| OpenVLA-OFT | 2025 | Stanford | 优化微调，吞吐与成功率提升 |

> 具体年份/指标请以检索到的一手论文为准，禁止凭记忆填数。

## 关键数据集
- Open X-Embodiment (OXE)：22 种本体、100 万+ episodes
- DROID：多样场景真机操作
- BridgeData V2、RH20T、RoboSet
- AgiBot World、RoboMIND、ARIO（2025 前后）
- 仿真：LIBERO、CALVIN、SimplerEnv、ManiSkill

## 评测要点
- 泛化维度：新物体 / 新指令 / 新场景 / 新本体
- 动作表示：离散 vs 连续、chunk size、控制频率
- 推理成本：参数量、显存、控制频率是否满足闭环

## 常见问题
- 语言 grounding 是否真实，还是只用了视觉？
- 数据规模与多样性对性能的边际收益
- 是否支持长程任务与失败恢复
