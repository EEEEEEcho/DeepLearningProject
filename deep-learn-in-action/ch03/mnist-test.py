import sys, os
sys.path.append(os.pardir) # 为了导入父目录中的文件而进行的设定
from dataset.mnist import load_mnist
# 第 1 个参数normalize设置是否将输入图像正规化为0.0～1.0的值。如果将该参数设置
# 为False，则输入图像的像素会保持原来的0～255。第2个参数flatten设置
# 是否展开输入图像（变成一维数组）。如果将该参数设置为False，则输入图
# 像为1 × 28 × 28的三维数组；若设置为True，则输入图像会保存为由784个
# 元素构成的一维数组。第3个参数one_hot_label设置是否将标签保存为one_hot表示（one-hot representation）。
# one-hot表示是仅正确解标签为1，其余皆为0的数组，就像[0,0,1,0,0,0,0,0,0,0]这样。当one_hot_label为False时，
# 只是像7、2这样简单保存正确解标签；当one_hot_label为True时，标签则保存为one-hot表示。
# (训练图像 ,训练标签 )，(测试图像，测试标签 )
(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True,
normalize=False)
# 输出各个数据的形状
print(x_train.shape) # (60000, 784)
print(t_train.shape) # (60000,)
print(x_test.shape) # (10000, 784)
print(t_test.shape) # (10000,)