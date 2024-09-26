import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 设置字体以支持中文
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号

# 参数范围
t = np.linspace(0, 2 * np.pi, 100)  # t 的范围
s = np.linspace(-1, 1, 50)           # s 的范围

# 创建网格
T, S = np.meshgrid(t, s)

# 计算参数方程
X = (2 + S / 2 * np.cos(T / 2)) * np.cos(T)
Y = (2 + S / 2 * np.cos(T / 2)) * np.sin(T)
Z = (S / 2) * np.sin(T / 2)

# 绘制默比乌斯带
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')

# 设置标题和轴标签
ax.set_title('默比乌斯带')
ax.set_xlabel('X 轴')
ax.set_ylabel('Y 轴')
ax.set_zlabel('Z 轴')

plt.show()
