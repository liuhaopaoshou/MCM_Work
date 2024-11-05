import pulp
import pandas as pd

# 创建线性规划问题
model = pulp.LpProblem("Warehouse_Rental", pulp.LpMinimize)

# 定义变量
x = pulp.LpVariable.dicts("x", [(i, j) for i in range(1, 5) for j in range(1, 5)], lowBound=0, cat='Continuous')

# 租金费用
cost = {
    1: 2800,
    2: 4500,
    3: 6000,
    4: 7300
}

# 需求
demand = {
    1: 15,
    2: 10,
    3: 20,
    4: 12
}

# 目标函数：最小化总租借费用
model += pulp.lpSum(cost[j] * x[(i, j)] for i in range(1, 5) for j in range(1, 5)), "Total_Cost"

# 约束条件
for i in range(1, 5):
    model += pulp.lpSum(x[(j, k)] for j in range(1, i+1) for k in range(1, 5) if j + k - 1 >= i) >= demand[i], f"Demand_Constraint_{i}"

# 求解模型
model.solve()

# 输出结果
result_matrix = pd.DataFrame(0.0, index=range(1, 5), columns=range(1, 5))

for (i, j) in x.keys():
    result_matrix.at[i, j] = x[(i, j)].varValue

print("租用合同数量矩阵:")
print(result_matrix.astype(float))

print("最小总租金费用 = ", pulp.value(model.objective))
