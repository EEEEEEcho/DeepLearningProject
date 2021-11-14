import numpy as np
# numpy测试

# 算数运算
x = np.array([1.0,2.0,3.0])
y = np.array([2.0,3.0,4.0])
print(x)
print(x + y)
print(x - y)
print(x * y)
# 只有元素数目相同才可以进行算数运算

# 标量运算
print(x / 2)

# 二维数组
A = np.array([[1,2],[3,4]])
print(A)
print(A.shape)  # A 的形状
print(A.dtype)  # A 中数据的类型

# 广播
B = np.array([10,20])
print(A * B)

# 访问元素
X = np.array([[51,55],[14,19],[0,4]])
print(X)
print(X[0]) # 第0行
print(X[0][1])  # 0行1列

# for循环遍历
for row in X:
    print(row)

# 扁平化，将二维数组，转换为一维数组
xx = X.flatten()
print(xx)
# 获取索引为0、2、4的元素
print(xx[np.array([0,2,4])])
# 过滤
print(xx > 15)
# 抽取
print(xx[xx > 15])
