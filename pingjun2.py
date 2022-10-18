import os

import cv2 as cv
import numpy as np
import os

# 获取视频名字列表
def get_videos(path):
    videonames = os.listdir(path)
    return videonames

path = r'D:\vehicle_data\CheDao\高速公路匝道test'
videonames = get_videos(path)
for video in videonames:
    print(video)
    video_path = os.path.join(path, video)
    cap = cv.VideoCapture(video_path)
    img_sum = 0
    zhen = 0
    while (True):
        ret, frame = cap.read()
        if zhen < 500:
            zhen = zhen + 1
            continue

        frame = frame.astype(np.float32)
        img_sum += frame
        zhen=zhen+1
        if zhen == 1000:
            break
    img=img_sum/(zhen-500)
    img = img.astype(np.uint8)
    cv.namedWindow("input_image", 0)  # 0可调大小，注意：窗口名必须imshow里面的一窗口名一致
    cv.resizeWindow("input_image", 800, 450)  # 设置长和宽
    cv.imshow('input_image', img)
    outpath = os.path.join("D:\\vehicle_data\CheDao\\test", video.split('.')[0] + '.jpg')
    print(outpath)
    cv.imwrite(outpath, img)
    print('???????????')
    cv.waitKey(0)
    cv.destroyAllWindows()
