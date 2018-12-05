# Done by Frannecklp

import cv2
import numpy as np
import win32gui, win32ui, win32con, win32api


def grab_screen(region=None):
    hwin = win32gui.GetDesktopWindow()

    if region:
        left, top, x2, y2 = region
        width = x2 - left + 1
        height = y2 - top + 1
    else:
        width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
        height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
        left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
        top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)

    hwindc = win32gui.GetWindowDC(hwin)
    srcdc = win32ui.CreateDCFromHandle(hwindc)
    memdc = srcdc.CreateCompatibleDC()
    bmp = win32ui.CreateBitmap()
    bmp.CreateCompatibleBitmap(srcdc, width, height)
    memdc.SelectObject(bmp)
    memdc.BitBlt((0, 0), (width, height), srcdc, (left, top), win32con.SRCCOPY)

    signedIntsArray = bmp.GetBitmapBits(True)
    img = np.fromstring(signedIntsArray, dtype='uint8')
    img.shape = (height, width, 4)

    srcdc.DeleteDC()
    memdc.DeleteDC()
    win32gui.ReleaseDC(hwin, hwindc)
    win32gui.DeleteObject(bmp.GetHandle())

    img = cv2.cvtColor(img, cv2.COLOR_BGRA2RGB)

    small = cv2.imread("C:/1/11112.png")
    big = img
    big = cv2.GaussianBlur(big, (5, 5), 0)
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
    dest = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)  # 去除小的干扰块
    cv2.imshow('mask', dest)
    return dest
