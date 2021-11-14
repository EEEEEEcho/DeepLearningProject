import numpy as np
import matplotlib.pylab as plt


# 阶跃函数,numpy实现
# 功能：传递一个numpy数组传递，返回一个numpy数组如果传入数组的元素>=0，则对应返回的数组的元素为1
# 例：x = [-1.0,1.0,2.0] 返回 y = [0,1,1]
# def step_function(x):
#     y = x > 0
#     return y.astype(np.int)

# 阶跃函数的图形

# def step_function(x):
#     return np.array(x > 0, dtype=np.int)
#
#
# x = np.arange(-5.0, 5.0, 0.1)  # 在−5.0到5.0的范围内，以0.1为单位，生成NumPy数组（[-5.0, -4.9, ... 4.9]）
# y = step_function(x)  # 返回一个判断每个元素是否 >= 0的结果集，是的话返回1
# plt.plot(x, y)
# plt.ylim(-0.1, 1.1)  # 指定y轴的范围
# plt.show()


# sigmoid函数实现
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


m = np.arange(-5,5,0.1)
n = sigmoid(m)
plt.plot(m,n)
plt.show()

# ReLU函数：输入> 0,直接输出该值，输入 < 0,输出0
def relu(x):
    return np.maximum(0,x)