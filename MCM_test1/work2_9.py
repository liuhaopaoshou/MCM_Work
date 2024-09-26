import numpy as np
import matplotlib.pyplot as plt

# 定义 x 的范围
x = np.linspace(-10, 10, 400)

# 创建 2 行 3 列的子图
fig, axs = plt.subplots(2, 3, figsize=(15, 10))

# 绘制曲线
for k in range(1, 7):
    y = k * x**2 * np.sin(x) + 2 * k + np.cos(x**3)
    axs[(k-1)//3, (k-1)%3].plot(x, y)
    axs[(k-1)//3, (k-1)%3].set_title(f'k = {k}')
    axs[(k-1)//3, (k-1)%3].grid(True)

plt.tight_layout()
plt.show()
