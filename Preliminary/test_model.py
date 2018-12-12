import numpy as np
import cv2
import time

from grabscreen import grab_screen
from directkeys import PressKey,ReleaseKey,W, A, S, D
from getkeys import key_check
from alexnet import alexnet


WIDTH = 80
HEIGHT = 60
LR = 1e-3       #学习效率
EPOCHS = 8
MODEL_NAME = 'py-car-{}-{}-{}-epochs.model'.format(LR,'alexnetv2',EPOCHS)


def straight():
    PressKey(W)
    ReleaseKey(A)
    ReleaseKey(D)
    print(straight)
def left():
    PressKey(A)
    PressKey(W)
    ReleaseKey(D)
    ReleaseKey(A)
    print(left)
def right():
    PressKey(D)
    PressKey(W)
    ReleaseKey(A)
    ReleaseKey(D)
    print(right)

model = alexnet(WIDTH,HEIGHT,LR)
model.load(MODEL_NAME)


def main():
    for i in list(range(4))[::-1]:
        print(i + 1)
        time.sleep(1)

    last_time = time.time()

    paused = False

    while True:

        if not paused:
            screen = grab_screen(region=(0, 150, 800, 640))
            screen = cv2.cvtColor(screen,cv2.COLOR_BGR2GRAY)
            screen = cv2.resize(screen,(80,60))

            print('Frame took {} seconds'.format(time.time() - last_time))
            last_time = time.time()

            prediction = model.predict([screen.reshape(WIDTH,HEIGHT,1)])[0]
            moves = list(np.around(prediction))
            print(moves,prediction)

            if moves == [1,0,0]:
                left()
            elif moves == [0,1,0]:
                straight()
            elif moves == [0,0,1]:
                right()


        keys = key_check()
        if 'T' in keys:
            if paused:
                paused = False
                time.sleep(1)
            else:
                paused = True
                ReleaseKey(W)
                ReleaseKey(A)
                ReleaseKey(D)
                time.sleep(1)


main()

