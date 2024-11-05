from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpStatus, value

# 创建线性规划问题
problem = LpProblem("Minimize_Z", LpMinimize)

# 定义变量
x1 = LpVariable('x1', lowBound=0)
x2 = LpVariable('x2', lowBound=0)
x3 = LpVariable('x3', lowBound=0)
x4 = LpVariable('x4', lowBound=0)
x5 = LpVariable('x5', lowBound=0)

# 目标函数
problem += 20 * x1 + 90 * x2 + 80 * x3 + 70 * x4 + 30 * x5, "Objective"

# 约束条件
problem += x1 + x2 + x5 >= 30, "Constraint_1"
problem += x3 + x4 >= 30, "Constraint_2"
problem += 3 * x1 + 2 * x3 <= 120, "Constraint_3"
problem += 3 * x2 + 2 * x4 + x5 <= 48, "Constraint_4"

# 求解问题
problem.solve()

# 输出结果
print("Status:", LpStatus[problem.status])
print("Optimal values:")
print("x1 =", value(x1))
print("x2 =", value(x2))
print("x3 =", value(x3))
print("x4 =", value(x4))
print("x5 =", value(x5))
print("Minimum Z =", value(problem.objective))
