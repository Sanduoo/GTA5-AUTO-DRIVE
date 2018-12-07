import cv2
import numpy as np
import matplotlib.pyplot as plt

def image(img):

    #GaussianBlur
    img = cv2.GaussianBlur(img, (5,5), 0 )
    #convert BGR to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #defined the range of a color
    lower_color = np.array([0,0,30])
    upper_color = np.array([180,43,190])
    #get mask
    mask = cv2.inRange(hsv, lower_color, upper_color)
    #get result
    res = cv2.bitwise_or(img, img, mask= mask)
    # res = cv2.cvtColor(res, cv2.COLOR_HSV2BGR)
    # res = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)

    cv2.imshow('res',res)
    # return  res
    """
    #Because cv2's color system is BGR, but matplotlib's color system is RGB,
    #must convert BGR to RGB
    imgrgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    resrgb = cv2.cvtColor(res, cv2.COLOR_BGR2RGB)
    img_data = [imgrgb, hsv, mask, resrgb]
    titles = ['Original image', 'HSV image', 'Mask image', 'Result image']
    

    # color_value = np.uint8([[[53,52,48]]])
    # color_hsv_value = cv2.cvtColor(color_value, cv2.COLOR_BGR2HSV)
    # print(color_hsv_value)

    
    for i in range(4):
        plt.subplot(2,2,i+1)
        plt.imshow(img_data[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    plt.show()
    """

# read image
img = cv2.imread("C:/1/1111.png")

cv2.namedWindow('res', cv2.WINDOW_AUTOSIZE)
image(img)

cv2.waitKey(0)
cv2.destroyAllWindows()
