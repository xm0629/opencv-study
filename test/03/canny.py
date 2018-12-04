import cv2

src = cv2.imread("/home/xm/repository/opencv-study/test/03/canny.jpg", 0)
cv2.imshow("canny.jpg", cv2.Canny(src, 200, 300))
cv2.waitKey()
cv2.destroyAllWindows()

"""
canny 边缘检测算法非常复杂也很有趣，这里有五个步骤:
1. 使用高斯滤波器对图像进行去噪
2. 计算梯度
3. 在边缘上使用菲最大抑制(NMS) 
4. 在检测边缘上使用双 double 阈值去除假阳性
5. 最后分析所有的边缘及其之间的链接, 以保证真正的边缘并消除不明显的边缘

"""