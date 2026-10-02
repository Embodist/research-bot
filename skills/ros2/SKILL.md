---
name: ros2
description: ROS 2 生态系统知识。覆盖发行版、rclcpp/rclpy、DDS、执行器、生命周期、ros2_control、Nav2、MoveIt2、仿真与部署，用于追踪 ROS2 工程前沿。
---

# ROS 2 生态

## 发行版节奏（以检索为准）
- LTS：Humble Hawksbill (2022)、Jazzy Jalisco (2024)，其后为 Kilted Kaiju (2025) 等
- 非 LTS：Iron、Rolling（滚动开发）
- 选型建议：生产用 LTS；尝鲜/上游贡献用 Rolling

## 核心概念
| 概念 | 说明 |
|------|------|
| Node | 最小计算单元 |
| Topic / Service / Action | 发布订阅 / 请求响应 / 长任务 |
| QoS | Reliability、Durability、History、Deadline、Liveliness |
| Executor | 单线程/多线程，回调组（CallbackGroup）并发控制 |
| Composition | 组件化进程内组合，降低拷贝与延迟 |
| Lifecycle Node | 受管状态机（unconfigured→inactive→active→finalized） |
| tf2 | 坐标变换树 |
| rosbag2 | 录制/回放，支持 MCAP |
| DDS | 中间件：Fast DDS、Cyclone DDS、Zenoh（桥接） |
| RMW | ROS Middleware 抽象层 |

## 工具链
- 构建：colcon、ament_cmake、ament_python、`rosdep` 依赖
- 调试：`ros2 topic hz/echo/delay`、`ros2 doctor`、rqt、RViz2、Foxglove
- 测试：`launch_testing`、`colcon test`、pytest、gtest
- 仿真：Gazebo (gz-sim)、Isaac Sim 的 ROS 桥
- 导航：Nav2（行为树 + 规划器/控制器插件）
- 操作：MoveIt2（规划、碰撞、抓取）
- 控制：ros2_control（hardware_interface + controller_manager）
- 嵌入式：micro-ROS

## 追踪要点
- **实时性**：`use_intra_process_comms`、执行器模型、DDS 调参
- **多机/分布式**：DDS discovery、ROS_DOMAIN_ID、DDS Security、Zenoh
- **确定性**：QoS 不匹配导致丢包、回调阻塞事件循环
- **可观测性**：rosbag2 MCAP、Foxglove、tracing（ros2_tracing / LTTng）
- **AI 集成**：VLA/策略节点作为 ROS2 组件，动作接口与实时约束

## 常见坑
- QoS 不兼容导致「topic 无数据」
- 大消息（点云/图像）拷贝开销 → 用零拷贝与组件
- 生命周期节点未激活
- DDS 默认配置在多播受限网络下发现失败
