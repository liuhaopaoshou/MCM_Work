import numpy as np
from pulp import LpProblem, LpVariable, LpMaximize, lpSum, LpStatus, value

# 创建线性规划问题
model = LpProblem("Candy_Production", LpMaximize)

# 决策变量
x11 = LpVariable("x11", lowBound=0)  # 原料A用于生产糖果甲
x12 = LpVariable("x12", lowBound=0)  # 原料A用于生产糖果乙
x13 = LpVariable("x13", lowBound=0)  # 原料A用于生产糖果丙
x21 = LpVariable("x21", lowBound=0)  # 原料B用于生产糖果甲
x22 = LpVariable("x22", lowBound=0)  # 原料B用于生产糖果乙
x23 = LpVariable("x23", lowBound=0)  # 原料B用于生产糖果丙
x31 = LpVariable("x31", lowBound=0)  # 原料C用于生产糖果甲
x32 = LpVariable("x32", lowBound=0)  # 原料C用于生产糖果乙
x33 = LpVariable("x33", lowBound=0)  # 原料C用于生产糖果丙

# 目标函数：最大化利润
model += (
    (3.40 - 0.50) * (x11 + x21 + x31) +
    (2.85 - 0.40) * (x12 + x22 + x32) +
    (2.25 - 0.30) * (x13 + x23 + x33) -
    2.0 * (x11 + x12 + x13) -
    1.5 * (x21 + x22 + x23) -
    1.0 * (x31 + x32 + x33),
    "Total_Profit"
)

# 约束条件
# 原材料资源约束
model += (x11 + x12 + x13 <= 2000), "Raw_Material_A"
model += (x21 + x22 + x23 <= 2500), "Raw_Material_B"
model += (x31 + x32 + x33 <= 1200), "Raw_Material_C"

# 成分比例约束
model += (x11 >= 0.6 * (x11 + x21 + x31)), "Candy_A_Lower_Bound"
model += (x31 <= 0.2 * (x11 + x21 + x31)), "Candy_A_Upper_Bound"
model += (x12 >= 0.3 * (x12 + x22 + x32)), "Candy_Y_Lower_Bound"
model += (x32 <= 0.5 * (x12 + x22 + x32)), "Candy_Y_Upper_Bound"
model += (x33 <= 0.6 * (x13 + x23 + x33)), "Candy_Z_Upper_Bound"

# 求解模型
model.solve()

# 输出结果矩阵
results = np.array([
    ["原料", "糖果甲 (kg)", "糖果乙 (kg)", "糖果丙 (kg)"],
    ["A", value(x11), value(x12), value(x13)],
    ["B", value(x21), value(x22), value(x23)],
    ["C", value(x31), value(x32), value(x33)],
])

print(results)
print(f"最大利润: {value(model.objective)} 元")
