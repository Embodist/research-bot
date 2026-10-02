---
name: cpp-robotics
description: C++ 机器人工程栈知识。覆盖 Eigen/Sophus/Ceres/Pinocchio 等数值与优化库、实时 C++ 实践、构建与包管理、性能与安全，用于梳理工程最佳实践与生态。
---

# C++ 机器人工程栈

## 核心库
| 库 | 用途 |
|----|------|
| Eigen | 线性代数（矩阵/向量/稀疏） |
| Sophus | 李群/李代数（SO3/SE3） |
| Ceres Solver | 非线性最小二乘（BA、标定、IK） |
| g2o / GTSAM | 图优化 / 因子图（SLAM、状态估计） |
| Pinocchio | 刚体动力学与运动学（含解析导数） |
| Orocos KDL | FK/IK/Jacobian |
| Drake | 优化与控制的 C++ 工具箱 |
| PCL | 点云处理 |
| OpenCV | 视觉 |
| nlohmann/json | JSON |
| fmt / spdlog | 格式化与日志 |
| Abseil / Boost | 基础设施 |

## 构建与依赖
- **CMake**（现代 target-based：`target_link_libraries`, `find_package`, `FetchContent`）
- 包管理：vcpkg / Conan / conda-forge / ROS 的 rosdep
- 编译：C++17/20，`-O3 -march=native`，`-Wall -Wextra`
- 可选：Bazel（Drake 生态）、Meson

## 实时与安全（Real-time C++）
- 避免运行期动态分配（预分配、内存池）、避免异常穿越实时边界
- 锁-free 队列 / 双缓冲；优先级反转与优先级继承
- 固定步长控制循环，测量 jitter 与 worst-case 执行时间
- 确定性：避免 `rand()`、系统时钟抖动；用单调时钟
- 工具：`perf`、`valgrind`、`heaptrack`、`ros2 topic delay`、tracing

## 性能实践
- 表达式模板（Eigen）避免临时对象；`noalias()`；固定尺寸矩阵
- 自动微分（Ceres Jet、Pinocchio 解析导数）替代手推导数
- SIMD/并行：OpenMP、TBB、CUDA
- 基准：Google Benchmark

## 工程规范
- RAII、智能指针、`const` 正确性、`[[nodiscard]]`
- 单元测试：GoogleTest/Catch2；sanitizer（ASan/UBSan/TSan）
- 静态分析：clang-tidy、cppcheck、IWYU
- 接口稳定：ABI 兼容、版本化、pkg-config/CMake config

## 与 Python 协作
pybind11 / nanobind / pybind 生成绑定；C++ 做实时内核，Python 做编排与训练。
