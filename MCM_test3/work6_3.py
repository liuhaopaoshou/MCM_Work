import itertools

# 面试时间（单位：分钟）
times = {
    '甲': [14, 16, 21],
    '乙': [19, 17, 10],
    '丙': [10, 15, 12],
    '丁': [9, 12, 13]
}

students = list(times.keys())
min_exit_time = float('inf')
optimal_order = []

# 计算结束时间的函数
def calculate_end_time(order):
    # 每个阶段的结束时间
    stage_1_end_time = 0
    stage_2_end_time = 0
    stage_3_end_time = 0

    for student in order:
        # 当前同学的初试结束时间
        stage_1_end_time += times[student][0]  # 当前同学的初试时间
        # 当前同学的复试结束时间
        stage_2_end_time = max(stage_2_end_time, stage_1_end_time) + times[student][1]
        # 当前同学的经理面试结束时间
        stage_3_end_time = max(stage_3_end_time, stage_2_end_time) + times[student][2]

    return stage_3_end_time  # 返回所有同学的经理面试结束时间中的最大值

# 生成所有可能的初试顺序
for order in itertools.permutations(students):
    exit_time = calculate_end_time(order)
    if exit_time < min_exit_time:
        min_exit_time = exit_time
        optimal_order = order

# 输出最优顺序和最早离开时间
earliest_hour = 8 + (min_exit_time // 60)  # 计算小时
earliest_minute = min_exit_time % 60  # 计算分钟
print("最优面试顺序:", optimal_order)
print("他们最早能在 {:02d}:{:02d} 离开公司。".format(earliest_hour, earliest_minute))
