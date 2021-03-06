import numpy as np
from PIL import ImageGrab
import cv2
import time
from directkeys import ReleaseKey, PressKey, W, A, S, D
import pyautogui



def draw_lines(img, lines):
    try:
        for line in lines:
            coords = line[0]
            cv2.line(img, (coords[0],coords[1]), (coords[2],coords[3]), [255,255,255], 3)
    except:
        pass


def roi(img, vertices):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, vertices, 255)
    masked = cv2.bitwise_and(img, mask)
    return masked


def process_img(original_image):
    h, w, ch = original_image.shape
    src2 = np.zeros([h, w, ch], original_image.dtype)
    # original_image = cv2.addWeighted(original_image, 1.2, src2, 1 - 1.2, 5)
    # cv2.imshow('original_image',original_image)

    # GaussianBlur
    img = cv2.GaussianBlur(original_image, (5, 5), 0)
    # convert BGR to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # defined the range of a color
    lower_color = np.array([0, 0, 30])
    upper_color = np.array([180, 43, 190])
    # get mask
    mask = cv2.inRange(hsv, lower_color, upper_color)
    # get result
    res = cv2.bitwise_or(img, img, mask=mask)

    processed_img = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    # ret,processed_img =  cv2.threshold(processed_img,0,255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    processed_img = cv2.Canny(processed_img, threshold1=40, threshold2=140)
    cv2.imshow('processed_img',processed_img)
    processed_img = cv2.GaussianBlur(processed_img, (5,5), 0 )
    vertices = np.array([[10,500],[10,300], [300,200], [500,200], [800,300], [800,500]], np.int32)
    processed_img = roi(processed_img, [vertices])

    #                       edges                      ，未知,最短长度,最大间断
    lines = cv2.HoughLinesP(processed_img, 1, np.pi/180,300,10,80,80)
    draw_lines(processed_img,lines)

    return processed_img


def main():
    last_time = time.time()
    while(True):
        screen =  np.array(ImageGrab.grab(bbox=(0,150, 800, 640)))
        new_screen = process_img(screen)
        print('Loop took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        cv2.imshow('window', new_screen)
        #cv2.imshow('window2', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

main()
