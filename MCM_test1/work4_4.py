import numpy as np
from scipy.stats import chisquare, poisson

# 数据：观察频数
observed_freq = np.array([22, 37, 20, 13, 6, 2, 0])  # 表4.20中的频数数据
total_count = 100  # 样本总数

# 泊松分布参数 λ = 1
lambda_poisson = 1

# 计算泊松分布下每个次数的期望频数
expected_prob = np.array([poisson.pmf(k, lambda_poisson) for k in range(6)])  # 泊松分布 pmf
expected_prob = np.append(expected_prob, 1 - expected_prob.sum())  # 合并大于等于6的部分
expected_freq = expected_prob * total_count  # 期望频数

# 合并 i>=5 和 i>=6 的观测频数与期望频数
observed_freq_combined = np.append(observed_freq[:5], observed_freq[5:].sum())  # 合并大于等于5的观测频数
expected_freq_combined = np.append(expected_freq[:5], expected_freq[5:].sum())  # 合并大于等于5的期望频数

# 进行卡方拟合优度检验
chi2_stat, p_value = chisquare(f_obs=observed_freq_combined, f_exp=expected_freq_combined)

# 输出结果
print("卡方统计量:", chi2_stat)
print("p 值:", p_value)

# 显著性水平 alpha = 0.05
alpha = 0.05
if p_value < alpha:
    print("拒绝原假设，数据不服从均值为 λ = 1 的泊松分布")
else:
    print("不拒绝原假设，数据可能服从均值为 λ = 1 的泊松分布")
