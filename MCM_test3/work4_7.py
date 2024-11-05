import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import scipy.stats as stats


# 设置字体为 SimHei (黑体)
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    # 用来正常显示负号

# 体重x和体积y数据
x = np.array([17.1, 10.5, 13.8, 15.7, 11.9, 10.4, 15.0, 16.0, 17.8, 15.8, 15.1, 12.1, 18.4, 17.1, 16.7, 16.5, 15.1, 15.1])
y = np.array([16.7, 10.4, 13.5, 15.7, 11.6, 10.2, 14.5, 15.8, 17.6, 15.2, 14.8, 11.9, 18.3, 16.7, 16.6, 15.9, 15.1, 14.5])

# 绘制散点图
plt.scatter(x, y, color='blue', label='Data Points')
plt.xlabel('体重 (kg)')
plt.ylabel('体积 (dm^3)')
plt.title('体重与体积的散点图')

# 线性回归
x_reshaped = x.reshape(-1, 1)  # 将x转换为二维数组
model = LinearRegression()
model.fit(x_reshaped, y)
y_pred = model.predict(x_reshaped)

# 绘制回归直线
plt.plot(x, y_pred, color='red', label=f'Regression Line: y = {model.coef_[0]:.2f}x + {model.intercept_:.2f}')
plt.legend()
plt.show()

# 输出线性回归方程系数
print(f'回归方程: y = {model.coef_[0]:.2f}x + {model.intercept_:.2f}')

# 假设检验 (检验斜率是否为 0)
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
print(f"斜率: {slope:.2f}, p值: {p_value:.4f}")

if p_value < 0.05:
    print("拒绝原假设 H0，斜率显著不等于 0")
else:
    print("接受原假设 H0，斜率不显著")
