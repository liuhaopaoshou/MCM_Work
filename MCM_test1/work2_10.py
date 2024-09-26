# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# import sympy as sp
#
# # 定义符号
# x, y, z = sp.symbols('x y z')
#
# # 定义曲面方程
# surfaces = [
#     sp.Eq(x**2 / 8 + y**2 / 10 - z**2 / 6, 1),  # 单叶双曲面
#     sp.Eq(x**2 / 8 - y**2 / 12 - z**2 / 8, 1), # 双叶双曲面
#     sp.Eq(x**2 / 10 + y**2 / 6, z)              # 椭圆抛物面
# ]
#
# # 绘制每个曲面
# fig = plt.figure(figsize=(18, 6))
#
# for i, surface in enumerate(surfaces):
#     ax = fig.add_subplot(1, 3, i + 1, projection='3d')
#     ax.set_title(f'Surface {i + 1}')
#
#     # 生成网格数据
#     x_vals = np.linspace(-10, 10, 100)
#     y_vals = np.linspace(-10, 10, 100)
#     X, Y = np.meshgrid(x_vals, y_vals)
#
#     # 计算 Z 值
#     if i == 0:  # 单叶双曲面
#         Z_pos = np.sqrt(6 * (X**2 / 8 + Y**2 / 10 - 1))
#         Z_pos[Z_pos < 0] = 0  # 确保 Z 不小于 0
#         ax.plot_surface(X, Y, Z_pos, alpha=0.5, rstride=100, cstride=100)
#         ax.plot_surface(X, Y, -Z_pos, alpha=0.5, rstride=100, cstride=100)
#     elif i == 1:  # 双叶双曲面
#         Z_pos = np.sqrt(8 * (X**2 / 8 - 1 - Y**2 / 12))
#         Z_pos[Z_pos < 0] = 0  # 确保 Z 不小于 0
#         Z_neg = -np.sqrt(8 * (X**2 / 8 - 1 - Y**2 / 12))
#         Z_pos[Z_pos < 0] = 0  # 只绘制非负部分
#         ax.plot_surface(X, Y, Z_pos, alpha=0.5, rstride=100, cstride=100)
#     elif i == 2:  # 椭圆抛物面
#         Z = (X**2 / 10 + Y**2 / 6)
#         ax.plot_surface(X, Y, Z, alpha=0.5)
#
#     ax.set_xlabel('X axis')
#     ax.set_ylabel('Y axis')
#     ax.set_zlabel('Z axis')
#
# plt.tight_layout()
# plt.show()

import numpy as np
import matplotlib.pyplot as plt

# 创建一个3D图形
fig = plt.figure(figsize=(18, 6))

# 设置字体以支持中文
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号

# 单叶双曲面
ax1 = fig.add_subplot(1, 3, 1, projection='3d')
ax1.set_title('单叶双曲面')
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)
Z1 = np.sqrt(6 * (X**2 / 8 + Y**2 / 10 - 1))
Z1[Z1 < 0] = 0  # 确保 Z >= 0
ax1.plot_surface(X, Y, Z1, alpha=0.5, rstride=100, cstride=100)

# 双叶双曲面
ax2 = fig.add_subplot(1, 3, 2, projection='3d')
ax2.set_title('双叶双曲面')
Z2_pos = np.sqrt(8 * (X**2 / 8 - 1 - Y**2 / 12))
Z2_pos[Z2_pos < 0] = 0  # 确保 Z >= 0
Z2_neg = -np.sqrt(8 * (X**2 / 8 - 1 - Y**2 / 12))
Z2_pos[Z2_pos < 0] = 0  # 只绘制非负部分
ax2.plot_surface(X, Y, Z2_pos, alpha=0.5, rstride=100, cstride=100)

# 椭圆抛物面
ax3 = fig.add_subplot(1, 3, 3, projection='3d')
ax3.set_title('椭圆抛物面')
Z3 = (X**2 / 10 + Y**2 / 6)
ax3.plot_surface(X, Y, Z3, alpha=0.5)

# 设置轴标签
for ax in [ax1, ax2, ax3]:
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')

plt.tight_layout()
plt.show()

