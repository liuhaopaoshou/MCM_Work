import scipy.integrate as integrate
import numpy as np
import matplotlib.pyplot as plt

# 设置字体以支持中文
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号

# 定义被积函数
def integrand(x, y):
    return x**2 + 2*y**2

# 第一部分：x从0到1，y的上下限为 -sqrt(x) 和 sqrt(x)
def y_lower_1(x):
    return -np.sqrt(x)

def y_upper_1(x):
    return np.sqrt(x)

# 第二部分：x从1到4，y的上下限为 sqrt(x) 和 x-2
def y_lower_2(x):
    return x - 2

def y_upper_2(x):
    return np.sqrt(x)

# 计算双重积分，分两段
result_part1, error_part1 = integrate.dblquad(integrand, 0, 1, y_lower_1, y_upper_1)
result_part2, error_part2 = integrate.dblquad(integrand, 1, 4, y_lower_2, y_upper_2)

# 总结果
total_result = result_part1 + result_part2
print("Integral result =", total_result)

# 画出区域D
y = np.linspace(-2, 2, 400)
x1 = y**2
x2 = y + 2

plt.figure()
plt.plot(x1, y, label=r'$x = y^2$')
plt.plot(x2, y, label=r'$x = y + 2$')
plt.fill_betweenx(y, x1, x2, where=(x2 > x1), color='gray', alpha=0.5)
plt.title(r'区域 $D$')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
