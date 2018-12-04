import cv2

import numpy as np

src = np.zeros((200, 200), dtype=np.uint8)  # 创建 200 x 200 的黑色空白图像
src[50:150, 50:150] = 255   # 接着在图像中央放置一个白色的方块

ret, thresh = cv2.threshold(src, 127, 255, cv2.THRESH_BINARY)   # 对图像进行二值化操作

"""
src： 输入图，只能输入单通道图像，通常来说为灰度图
dst： 输出图
thresh： 阈值
maxval： 当像素值超过了阈值（或者小于阈值，根据type来决定），所赋予的值
type：二值化操作的类型，包含以下5种类型： cv2.THRESH_BINARY;cv2.THRESH_BINARY_INV;cv2.THRESH_TRUNC;cv2.THRESH_TOZERO;cv2.THRESH_TOZERO_INV.
"""

src, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
"""
该函数的三个参数 输入图像、层次类型、和轮廓逼近方法. 这个函数会修改输入图像，因此建议使用原始图像的一份拷贝 (src.copy()) 作为输入图像.

由函数返回的层次树很重要, cv2.RETR_TREE　参数会得到图像中轮廓的整体层次结构, 以此来建立轮廓之间的关系, 如果只想得到最外面的轮廓, 可使用 cv2.RETR_EXTERNAL。
这对消除包含在其他轮廓中的轮廓很有用, (比如, 在大多数情形下,　不需要检测一个目标包含在另一个与之不同的目标里面)

三个返回值 修改后的图像图像的轮廓、以及它们的层次.
"""

# 使用轮廓画出图像的彩色版本(即把轮廓画成绿色)　并显示出来.

color = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)


src = cv2.drawContours(color, contours, -1, (0, 255, 0), 2)
cv2.imshow("contours", color)

cv2.waitKey()
cv2.destroyAllWindows()
