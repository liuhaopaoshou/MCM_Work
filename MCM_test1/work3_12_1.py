import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# (1) 计算积分 ∫[0, +∞] e^(-x) * sin(√(x² + 2)) dx
def integrand1(x):
    return np.exp(-x) * np.sin(np.sqrt(x**2 + 2))

result1, error1 = quad(integrand1, 0, np.inf)
print("Integral (1):", result1)

# 绘制函数图形
x_values = np.linspace(0, 10, 400)
y_values = integrand1(x_values)

plt.figure(figsize=(8, 4))
plt.plot(x_values, y_values, label='e^(-x) * sin(√(x² + 2))')
plt.title('Function for Integral (1)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid()
plt.savefig('integral1_plot.png')  # 保存图形
plt.show()
