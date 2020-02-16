# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 13:04:46 2020

@author: Attlie
"""

import numpy as np
from PIL import ImageGrab
import cv2
import time
from directkeys import PressKey,W,A,S,D

def process_img(image):
    original_image = image
    # convert to gray
    processed_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # edge detection
    processed_img =  cv2.Canny(processed_img, threshold1 = 200, threshold2=300)
    return processed_img
def screen_record(): 
    last_time = time.time()
    while(True):
        # 800x600 windowed mode
        printscreen =  np.array(ImageGrab.grab(bbox=(0,40,800,640)))
        print('loop took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        cv2.imshow('window',cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
def main():
    last_time = time.time()
    while True:
        screen =  np.array(ImageGrab.grab(bbox=(0,40,800,640)))
        #print('Frame took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        new_screen = process_img(screen)
        cv2.imshow('window', new_screen)
        #cv2.imshow('window',cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
for i in list(range(4))[::-1]:
    print(i+1)
    time.sleep(1)

print('down')
PressKey(W) 
time.sleep(3)
print('up')
PressKey(W) 
main()
