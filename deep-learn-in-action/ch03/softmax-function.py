import numpy as np

a = np.array([0.3,2.9,4.0])
# 计算array中的每个数字的指数函数的值
exp_a = np.exp(a)
print(exp_a)

# 指数函数的和
sum_exp_a = np.sum(exp_a)
print(sum_exp_a)

y = exp_a / sum_exp_a
print(y)

# 解决溢出问题的正确softmax函数
def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c) # 溢出对策
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y


