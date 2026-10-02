---
name: embodied-ai
description: 具身智能（Embodied AI）领域知识。覆盖仿真环境、世界模型、导航与操作、Sim2Real、评测基准，用于梳理该方向的方法谱系与代表工作。
---

# 具身智能（Embodied AI）

## 研究范围
智能体通过身体与环境交互来完成任务：感知 → 决策 → 行动 → 反馈。核心子领域：
- **操作 Manipulation**：抓取、装配、灵巧操作
- **导航 Navigation**：VLN、ObjectNav、PointNav
- **移动操作 Mobile Manipulation**：家庭/仓储长程任务
- **人形与全身控制 Humanoid / Whole-body**：运动、平衡、locomotion
- **世界模型 World Models**：预测未来观测/状态以支撑规划

## 仿真平台与基准
| 平台 | 特点 | 关联基准 |
|------|------|----------|
| Habitat 2/3 | 真实感室内导航与重排 | ObjectNav, HRL |
| AI2-THOR / ProcTHOR | 交互式室内 | ALFRED, ManipulaTHOR |
| ManiSkill 2/3 | GPU 并行操作 | 大量操作任务 |
| Isaac Sim / Isaac Lab | 物理精确、可大规模并行 | 常用于 RL/Sim2Real |
| OmniGibson / BEHAVIOR-1K | 1000 项日常活动 | BEHAVIOR Challenge |
| MuJoCo / Genesis | 轻量物理 / 生成式仿真 | locomotion, 通用 |
| RoboSuite / RLBench | 机械臂操作 | 多任务基准 |

## 关键方法脉络
1. **模块化**：感知 + 规划 + 控制（SayCan、Code as Policies）
2. **端到端模仿**：行为克隆（ACT/ALOHA、Diffusion Policy）
3. **基础模型**：VLA（RT-2、OpenVLA、π0）
4. **世界模型驱动**：UniSim、Dreamer、Genie 类
5. **Sim2Real**：域随机化、系统辨识、real-to-sim-to-real

## 评测要看清的口径
- 仿真 vs 真机、单任务 vs 多任务、是否见过该物体/场景（generalization split）
- 成功率的分母与尝试次数；是否多随机种子
- 控制频率、动作空间（关节/末端/EE pose）

## 种子资源
- Open X-Embodiment：跨本体大规模真机数据集
- DROID：分布式机器人交互数据集（~76k trajectories）
- AgiBot World / RoboMIND / ARIO：新一代大规模真机数据集
- LIBERO / SimplerEnv / CALVIN：常用策略学习基准
