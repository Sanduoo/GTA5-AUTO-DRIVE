import numpy as np
import cv2
import time
from grabscreen import grab_screen

from getkeys import key_check
import os

def keys_to_out(keys):
    #[A,W,D]        A = [1,0,0]
    output = [0,0,0]
    if 'A' in keys:
        output[0] = 1
    elif 'W' in keys:
        output[1] = 1
    else:
        output[2] = 1
    return  output


file_name = 'tranining_data.npy'

if os.path.isfile(file_name):
    print('File exists,loading previous data!')
    training_data = list(np.load(file_name))
else:
    print('File does not exists,starting fresh!')
    training_data = []




def main():
    for i in list(range(4))[::-1]:
        print(i + 1)
        time.sleep(1)

    last_time = time.time()

    while True:
        screen = grab_screen(region=(0, 150, 800, 640))
        screen = cv2.cvtColor(screen,cv2.COLOR_BGR2GRAY)
        screen = cv2.resize(screen,(80,60))
        keys = key_check()
        output = keys_to_out(keys)
        training_data.append([screen,output])
        print('Frame took {} seconds'.format(time.time() - last_time))
        last_time = time.time()

        if len(training_data) % 500 == 0:
            print(len(training_data))
            np.save(file_name,training_data)


main()

