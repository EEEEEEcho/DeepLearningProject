# 感知机
import numpy as np


# 逻辑与门
# def AND(x1,x2):
#     # 权重和阈值
#     w1,w2,theta = 0.5,0.5,0.7
#     tmp = x1 * w1 + x2 * w2
#     if tmp <= theta:
#         return 0
#     elif tmp > theta:
#         return 1


#        0 (b + w1*x1 + w2*x2 <= 0)
#   y =
#        1 (b + w1*x1 + w2*x2 > 0)
x = np.array([0,1]) # 输入0 1
w = np.array([0.5,0.5]) # 权重
b = -0.7    # 偏置
print(w * x)
print(np.sum(w * x))
print(np.sum(w * x) + b)

#与门
def AND(x1,x2):
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    b = -0.7
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1
#与非门
def NAND(x1,x2):
    x = np.array([x1,x2])
    w = np.array([-.05,-0.5])
    b = 0.7
    tmp = np.sum(x * w) + b
    if tmp <= 0:
        return 0
    else:
        return 1

#或门
def OR(x1,x2):
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    b = -0.2
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

# 单层感知机无法表示异或门，可以通过组合感知机（叠加层）实现异或门
def XOR(x1,x2):
    s1 = NAND(x1,x2)
    s2 = OR(x1,x2)
    y = AND(s1,s2)
    return y