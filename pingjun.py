import cv2 as cv
import numpy as np

cap = cv.VideoCapture(r'D:\vehicle_data\CheDao\高速公路匝道\032701.mp4')
img_sum = 0
zhen = 0
while (True):
    ret, frame = cap.read()
    if zhen < 1000:
        zhen = zhen + 1
        continue

    frame = frame.astype(np.float32)
    img_sum += frame
    zhen=zhen+1
    if zhen == 2000:
        break
img=img_sum/(zhen-1000)
img = img.astype(np.uint8)
cv.namedWindow("input_image", 0)  # 0可调大小，注意：窗口名必须imshow里面的一窗口名一致
cv.resizeWindow("input_image", 800, 450)  # 设置长和宽
cv.imshow('input_image', img)
cv.imwrite("./pic/AVERAGE.jpg",img)
cv.waitKey(0)
cv.destroyAllWindows()
