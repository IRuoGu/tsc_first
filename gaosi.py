import copy

import numpy as np
import cv2
#经典的测试视频
cap = cv2.VideoCapture(r'D:\vehicle_data\CheDao\高速公路匝道\032701.mp4')
#形态学操作需要使用
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
#创建混合高斯模型用于背景建模
fgbg = cv2.createBackgroundSubtractorMOG2()

_ , framePro = cap.read()
count = 0
while(True):
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)

    #形态学开运算去噪点
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)#寻找视频中的轮廓
    # contours, hierarchy = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # for c in contours:
    #     #计算各轮廓的周长
    #     perimeter = cv2.arcLength(c, True)
    #     if (perimeter > 188) and (perimeter < 2000):
    #     #找到一个直矩形（不会旋转)
    #         x, y, w, h = cv2.boundingRect(c)
    #     #画出这个矩形
    #         cv2.rectangle(frame,(x,y), (x+w, y+h), (0,255,0), 2)


    cv2.namedWindow("fgmask", 0)  # 0可调大小，注意：窗口名必须imshow里面的一窗口名一致
    cv2.resizeWindow("fgmask", 800, 450)  # 设置长和宽

    fgmask = cv2.bitwise_not(fgmask)
    cv2.imshow('fgmask', fgmask)

    cv2.namedWindow("frame", 0)  # 0可调大小，注意：窗口名必须imshow里面的一窗口名一致
    cv2.resizeWindow("frame", 800, 450)  # 设置长和宽

    frame = cv2.bitwise_and(frame, frame, mask=fgmask)#获得无车辆的图片
    if count % 50 == 0:
        frame = cv2.addWeighted(frame, 0.5, framePro, 0.5, 0)
        framePro = copy.deepcopy(frame)
        cv2.imshow('frame', frame)


    k = cv2.waitKey(10)
    if k == 113:
        break
cap.release()
cv2.destroyWindow()