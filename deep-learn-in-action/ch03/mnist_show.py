import sys,os
print(sys.path)
print(os.pardir)
sys.path.append(os.pardir)
import numpy as np
from dataset.mnist import load_mnist
from PIL import Image

def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()

(x_train,t_train),(x_test,t_test) = load_mnist(flatten = True,normalize = False)
img = x_train[0]
label = t_train[0]
print(label)

print(img.shape)    # 现在是扁平化的一维数组
img = img.reshape(28,28)    # 将图像形状变为原来的尺寸
print(img.shape)

img_show(img)
