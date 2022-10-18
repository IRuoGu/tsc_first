import os

import cv2 as cv
import numpy as np
import cv2
from glob import glob
import imageio
from skimage.transform import resize

pth = r"D:\vehicle_data\CheDao\suidao"
for i in range(23):
    new_path = os.path.join(pth, str(i + 1), "*.jpg")
    datas = sorted(glob(new_path)) # 获取所有图片
    d1, d2, channels = imageio.imread(datas[0]).shape
    print(d1, d2, channels)
    print(datas[0])

    img_sum = 0
    zhen = 0

    for j in range(len(datas)):
        frame = imageio.imread(datas[j]).astype(np.float32)
        img_sum += frame

    img = img_sum / len(datas)
    img = img.astype(np.uint8)

    cv.namedWindow("input_image", 0)  # 0可调大小，注意：窗口名必须imshow里面的一窗口名一致
    cv.resizeWindow("input_image", 800, 450)  # 设置长和宽
    cv.imshow('input_image', img)

    save_path = os.path.join("D:\\vehicle_data\\CheDao\\suidaoBG", str(i + 1) + ".jpg")
    cv.imwrite(save_path, img)
    cv.waitKey(0)
    cv.destroyAllWindows()
