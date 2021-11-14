# numpy实现多维数组运算
import numpy as np
# 一维
A = np.array([1,2,3,4])
print(A)
print(np.ndim(A))
print(A.shape)
print(A.shape[0])
# 二维
B = np.array([[1,2],[3,4],[5,6]])
print(B)
print(np.ndim(B))
print(B.shape)
# 点乘
C = np.array([[1,2],[3,4]])
D = np.array([[5,6],[7,8]])
print(np.dot(C,D))

# 使用NumPy矩阵实现神经网络，不考虑偏置和激活函数
X = np.array([1,2]) # 输入层
W = np.array([[1,3,4],[2,4,6]]) #权重
Y = np.dot(X,W) # 输出层
print(Y)