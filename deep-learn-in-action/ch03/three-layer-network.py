# 3层神经网络的实现
# 3层神经网络：输入层（第0层）有2个神经元，第1个隐藏层（第1层）有3个神经元，
# 第2个隐藏层（第2层）有2个神经元，输出层（第3层）有2个神经元
import numpy as np


# 激活函数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


X = np.array([1.0, 0.5])
W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
B1 = np.array([0.1, 0.2, 0.3])
print(W1.shape)
print(X.shape)
print(B1.shape)

# 第一层
A1 = np.dot(X, W1) + B1
# 第一层激活
Z1 = sigmoid(A1)

# 第一层到第二层的传递
W2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
B2 = np.array([0.1, 0.2])
print(Z1.shape)
print(W2.shape)
print(B2.shape)

# 第二层
A2 = np.dot(Z1, W2) + B2
# 第二层激活
Z2 = sigmoid(A2)
print(Z2)

# 第二层到输出层的信号传递
W3 = np.array([[0.1, 0.3], [0.2, 0.4]])
B3 = np.array([0.1, 0.2])
A3 = np.dot(Z2, W3) + B3


# 激活函数：恒等函数
def identity_function(x):
    return x


# 输出层结果
Y = identity_function(A3)
print(Y)


# 整合代码
def init_network():
    network = {}
    network['W1'] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    network['b1'] = np.array([0.1, 0.2, 0.3])
    network['W2'] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    network['b2'] = np.array([0.1, 0.2])
    network['W3'] = np.array([[0.1, 0.3], [0.2, 0.4]])
    network['b3'] = np.array([0.1, 0.2])
    return network


def forward(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)

    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)

    a3 = np.dot(z2, W3) + b3
    y = identity_function(a3)

    return y


network = init_network()
x = np.array([1.0, 0.5])
y = forward(network, x)
print(y)
