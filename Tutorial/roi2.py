import cv2
import numpy as np
from matplotlib import pyplot as plt

#直方图反向投影

def bitwise_and():
    small = cv2.imread("C:/1/11112.png")
    big = cv2.imread("C:/1/1111.png")
    big = cv2.GaussianBlur(big, (5, 5), 0)
    # big = cv2.GaussianBlur(big, (5, 5), 0)
    small_hsv = cv2.cvtColor(small, cv2.COLOR_BGR2HSV)
    big_hsv = cv2.cvtColor(big, cv2.COLOR_BGR2HSV)

    h, s, v = cv2.split(small_hsv)
    print(h)
    print(s)
    print(v)

    lower_hsv = np.array([24, 14, 51])
    upper_hsv = np.array([60, 28, 54])
    mask = cv2.inRange(big_hsv, lower_hsv, upper_hsv)
    dest = cv2.bitwise_and(big_hsv, big_hsv, mask=mask)
    dest = cv2.cvtColor(dest, cv2.COLOR_HSV2BGR)
    # 转灰度
    dest = cv2.cvtColor(dest, cv2.COLOR_BGR2GRAY)
    # 二值化
    ret, binary = cv2.threshold(dest, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    # 形态学操作     腐蚀
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (6, 6))
    # dest = cv2.erode(dest, kernel)
    dest = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)  # 去除小的干扰块
    # dest = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)  # 填充闭合区域
    cv2.imshow('mask', cv2.cvtColor(dest,cv2.COLOR_GRAY2BGR))
    # return dest
    # cv2.imshow('video', big)

"""
def back_projection_demo():
    target = cv2.imread("C:/1/1111.png")
    sample = cv2.imread("C:/1/11112.png")
    target = cv2.GaussianBlur(target, (5, 5), 0)
    sample = cv2.GaussianBlur(sample, (5, 5), 0)
    roi_hsv = cv2.cvtColor(sample,cv2.COLOR_BGR2HSV)
    target_hsv = cv2.cvtColor(target,cv2.COLOR_BGR2HSV)

    #show images
    # cv2.imshow("sample",sample)
    # cv2.imshow("target",target)

    roiHist = cv2.calcHist([roi_hsv],[0,1],None,[32,32],[0,180,0,256])            #求出样本直方图
    cv2.normalize(roiHist,roiHist,0,256,cv2.NORM_MINMAX)                           #直方图归一化
    dest = cv2.calcBackProject([target_hsv],[0,1],roiHist,[0,180,0,256],1)        #直方图反向投影

    # dest = cv2.bitwise_not(dest,dest)

    ret, binary = cv2.threshold(dest, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    # 形态学操作     腐蚀
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    # dest = cv2.erode(dest, kernel)
    dest = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)  # 去除小的干扰块
    # dest = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)  # 填充闭合区域

    cv2.imshow("back_projection_demo", dest)

"""

src = cv2.imread("C:/1/1.jpg")
# cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
# cv.imshow("input_image",src)

# back_projection_demo()

bitwise_and()

cv2.waitKey(0)
cv2.destroyAllWindows()