import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread
# pyplot测试

# 生成数据
x = np.arange(0,6,0.1)  # 以0.1为单位，生成0到6的数据
y = np.sin(x)       # y是对x中的每个元素取sin值
# 绘制图形
# plt.plot(x,y)
# plt.show()

# 添加标题和x轴标签名
y2 = np.cos(x)

# 绘制图形
plt.plot(x,y,label="sin")
plt.plot(x,y2,linestyle="--",label="cos")   #用虚线绘制
plt.xlabel("x") #x轴标签
plt.ylabel("y") #y轴标签
plt.title('sin & cos')  #标题
plt.legend()    #添加图例
plt.show()

# 读入图像
# img = imread('/home/echo/图片/壁纸/wallhaven-e7e1qr.png')
# plt.imshow(img)

plt.show()