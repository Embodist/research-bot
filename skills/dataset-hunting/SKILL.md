---
name: dataset-hunting
description: 数据集与基准调研。用于为一个机器人/具身智能方向找出权威数据集、评测基准、排行榜与许可信息，并核对规模与可复现性。
---

# 数据集与基准猎取（Dataset Hunting）

## 必须记录的信息
| 字段 | 说明 |
|------|------|
| 名称 / 链接 | 官方主页与论文链接 |
| 规模 | episodes / frames / 小时数 / 任务数 |
| 本体 | 机械臂型号 / 灵巧手 / 移动 / 人形 / 多本体 |
| 模态 | RGB、深度、点云、触觉、力、语言标注 |
| 采集方式 | 遥操作 / 自主 / 仿真 / 混合 |
| 场景多样性 | 家庭 / 工厂 / 厨房 / 桌面 |
| 许可 | 研究/商用、是否需申请 |
| 评测协议 | 成功判定、train/val/test 划分、榜单 |
| 维护状态 | 最近更新、issue 响应 |

## 权威来源
- Open X-Embodiment (OXE) 汇总了 20+ 数据集
- DROID、BridgeData V2、RH20T、RoboSet、MIME
- AgiBot World、RoboMIND、ARIO（新一代大规模真机）
- 仿真基准：LIBERO、CALVIN、SimplerEnv、ManiSkill、BEHAVIOR-1K、Meta-World、RLBench
- 视频/世界模型：Something-Something、Ego4D、Open X-Embodiment 视频子集

## 质量核查清单
- [ ] 数据是否可下载（不是「即将发布」）
- [ ] 是否有官方 baseline 与榜单
- [ ] 评测是否防泄漏（同一场景/物体不出现在 train）
- [ ] 是否有已知 issue（标注错误、控制频率不一致）
- [ ] 许可是否允许目标用途

## 输出格式
用表格对比，并给出「推荐用于 X 场景」的建议与理由；标注哪些数据集存在版权/申请门槛。
