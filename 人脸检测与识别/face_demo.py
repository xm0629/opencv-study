import cv2
import numpy as np

"""
静态图人脸检测的程序 demo
视频人脸检测的程序 demo
2018-10-19 下午
"""

filename = '/home/xm/repository/opencv-study/人脸检测与识别/lena.jpg'

#
# def detect(filename):
#     face_cascade = cv2.CascadeClassifier('./cascades/haarcascade_frontalface_default.xml')
#     eye_cascade = cv2.CascadeClassifier('./cascades/haarcascade_eye.xml')
#     img = cv2.imread(filename)
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     faces = face_cascade.detectMultiScale(gray, 1.3, 5)
#     #eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)  # 眼睛标注的框算法
#     for (x, y, w, h) in faces:
#         img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
#
#     cv2.namedWindow('face-image-demo')
#     cv2.imshow('face-image-demo', img)
#     cv2.waitKey(0)


def detcet():
    face_cascade = cv2.CascadeClassifier('./cascades/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('./cascades/haarcascade_eye.xml')
    camera = cv2.VideoCapture(0)
    while True:
        ret, frame = camera.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            img = cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

            roi_gray = gray[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray, 1.03, 5, 0, (40, 40))

            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(img, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

        cv2.imshow("camera", frame)
        if cv2.waitKey(1000//12) & 0xff == ord("q"):
            break

    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    detcet()

# 眼睛的标注框不正确的原因是摄像头视频左右翻转.