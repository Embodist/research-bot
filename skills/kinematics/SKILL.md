---
name: kinematics
description: 机器人运动学知识。覆盖正/逆运动学、DH 与旋量表示、雅可比、冗余与奇异性、轨迹规划与动力学库，用于梳理运动学方法与工具。
---

# 机器人运动学（Kinematics）

## 基础概念
- **正运动学 (FK)**：关节角 → 末端位姿
- **逆运动学 (IK)**：末端位姿 → 关节角（可能多解/无解）
- **位姿表示**：旋转矩阵 SO(3)、四元数、欧拉角、李群 SE(3)/so(3)/se(3)
- **雅可比 J**：关节速度 ↔ 末端速度；用于奇异分析、力映射
- **奇异性**：det(J)=0，末端失去某方向自由度
- **可操作性 (Manipulability)**：√det(JJᵀ)，用于避奇异

## 建模表示
| 表示 | 特点 | 常见手册 |
|------|------|----------|
| DH 参数（标准/改进） | 经典、直观 | Craig, Siciliano |
| 旋量 / 指数积 (PoE) | 全局、无奇异参数化 | Murray-Li-Sastry, Lynch-Park |
| URDF | 工程描述格式 | ROS |
| MJCF | MuJoCo 描述 | MuJoCo |

## IK 求解方法
- **解析解**：特定构型（如 6-DOF 球形腕）可闭式求解
- **数值解**：Newton-Raphson、Levenberg-Marquardt、DLS（阻尼最小二乘，处理奇异）
- **优化法**：把 IK 写成带约束的 NLP（关节限位、碰撞、任务优先级）
- **学习法**：IK 网络、diffusion IK
- 工程常用：IKFast（解析）、TRAC-IK、KDL、Pinocchio + Ceres

## 轨迹与规划
- 关节空间：多项式/样条插值、梯形速度
- 任务空间：笛卡尔直线、圆弧
- 时间参数化：给定路径求速度曲线（满足速度/加速度/力矩约束）
- 规划：RRT/RRT*/PRM（高维）、CHOMP/STOMP/TrajOpt（优化型）、OMPL 库

## 动力学
- 拉格朗日 / 牛顿-欧拉
- 递归算法：RNEA（逆动力学）、CRBA（质量矩阵）
- 库：Pinocchio、Drake、RBDL、Orocos KDL、MuJoCo

## 常用工具链
Eigen、Sophus（李群）、Pinocchio、Drake、Orocos KDL、IKFast、TRAC-IK、Ceres、GTSAM、MoveIt2

## 追踪关键词
`differentiable kinematics`, `whole-body control`, `task-space control`, `operational space control`,
`contact-implicit trajectory optimization`, `SE(3) equivariant policy`
