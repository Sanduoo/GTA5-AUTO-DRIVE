import numpy as np
import cv2
import time

def roi(img, vertices):
    # blank mask:
    mask = np.zeros_like(img)
    # filling pixels inside the polygon defined by "vertices" with the fill color
    cv2.fillPoly(mask, vertices, 255)
    # returning the image only where mask pixels are nonzero
    masked = cv2.bitwise_and(img, mask)
    return masked


def road_hsv(image):
    vertices1 = np.array([[390, 310], [400, 310], [400, 330], [390, 330]
                          ], np.int32)
    image1 = roi(image, [vertices1])
    # image1 = cv2.GaussianBlur(image1, (5, 5), 0)
    # image1 = cv2.GaussianBlur(image1, (5, 5), 0)
    image1 = cv2.GaussianBlur(image1, (5, 5), 0)
    # image = cv2.GaussianBlur(image, (5, 5), 0)
    # image = cv2.GaussianBlur(image, (5, 5), 0)
    image = cv2.GaussianBlur(image, (5, 5), 0)
    image1 = cv2.medianBlur(image1, 5)
    image = cv2.medianBlur(image, 5)
    original_image = image


    small_hsv = cv2.cvtColor(image1,cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(small_hsv)
    # min_h = np.min(h)

#   提取路面中的车道线条

    big_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # lower_hsv = np.array([10, 0, 35])
    # upper_hsv = np.array([75, 45, 70])
    lower_hsv = np.array([np.min(h),np.min(s),np.min(v)])
    upper_hsv = np.array([np.max(h),np.max(s),np.max(v)])
    mask = cv2.inRange(big_hsv, lower_hsv, upper_hsv)
    # cv2.imshow('mask',mask)
    dest = cv2.bitwise_and(big_hsv, big_hsv, mask=mask)
    dest = cv2.cvtColor(dest, cv2.COLOR_HSV2BGR)
    # 转灰度
    dest = cv2.cvtColor(dest, cv2.COLOR_BGR2GRAY)

    # 二值化
    ret, binary = cv2.threshold(dest, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    # 形态学操作     腐蚀
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))
    # dest = cv2.erode(dest, kernel)
    dest = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)  # 去除小的干扰块
    # cv2.imshow('original_image',dest)
    # time.sleep(1)
    return dest
