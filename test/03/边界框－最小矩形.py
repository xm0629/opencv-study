import cv2
import numpy as np


# 找到一个正方形轮廓很简单, 要想找不规则的、外斜的以及旋转的形状可以用 opencv　的 cv2.findContours 函数.　它能得到最好的结果.
"""
目标的边界框、最小矩形面积、最小闭圆特性.
将 cv2.findContours 函数与少量的 opencv 功能相结合很容易实现这些功能.
"""

src = cv2.pyrDown(cv2.imread("hammer.jpg", cv2.IMREAD_UNCHANGED))
ret, thresh = cv2.threshold(cv2.cvtColor(src.copy(),
                                         cv2.COLOR_BGR2GRAY), 127, 255, cv2.THRESH_BINARY)
src, contours, hier = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for c in contours:
    # find bounding box coordinates

    x, y, w, h = cv2.boundingRect(c)

    cv2.rectangle(src,(x,y),(x+w, y+h),(0, 255, 0), 2)
    # find minimum　area

    rect = cv2.minAreaRect(c)
    # calculate coordinates of the minimum area rectangle

    box = cv2.boxPoints(rect)

    # normalize coordinate to integers
    box = np.int0(box)

    # draw contours
    cv2.drawContours(src, [box], 0, (0, 0, 255), 3)

    # calculate center and radius of minimum enclosing circle

    (x, y), radius = cv2.minEnclosingCircle(c)

    # cast t integers

    center = (int(x), int(y))
    radius = int(radius)

    # draw the circle

    src = cv2.circle(src, center, radius, (0, 255, 0), 2)
cv2.drawContours(src, contours, -1, (255, 0, 0), 1)
cv2.imshow("contours", src)
cv2.waitKey()
