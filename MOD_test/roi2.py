
import cv2
import numpy as np


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

    lower_hsv = np.array([10, 0, 35])
    upper_hsv = np.array([75, 45, 70])
    mask = cv2.inRange(big_hsv, lower_hsv, upper_hsv)
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
    # dest = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)  # 填充闭合区域
    # dest = cv2.cvtColor(dest,cv2.COLOR_GRAY2BGR)
    cv2.imshow('mask',dest )
    # return dest
    cv2.imshow('video', big)
    # print(dest.type())

src = cv2.imread("C:/1/1.jpg")
# cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)
# cv.imshow("input_image",src)

# back_projection_demo()

bitwise_and()

cv2.waitKey(0)
cv2.destroyAllWindows()