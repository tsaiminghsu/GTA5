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
def roi(img, vertices):
    #blank mask:
    mask = np.zeros_like(img)
    # fill the mask
    cv2.fillPoly(mask, vertices, 255)
    # now only show the area that is the mask
    masked = cv2.bitwise_and(img, mask)
    return masked
def draw_lines(img,lines):
    try:
        for line in lines:
            #[[x1,y1,x2,y2]]
            #[[2,2,6,2]]
            coords = line[0]
            #              x1,y1      x2,y2 
            cv2.line(img, (coords[0], coords[1]), (coords[2], coords[3]), [255,255,255], 3)
    except:
        pass
def process_img(original_image):
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    processed_img = cv2.Canny(processed_img, threshold1=200, threshold2=300)
    vertices = np.array([[10,500],[10,300],[300,200],[500,200],[800,300],[800,500],
                         ], np.int32)

    processed_img = cv2.GaussianBlur(processed_img,(5,5),0)
    processed_img = roi(processed_img, [vertices])

    # more info: http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_imgproc/py_houghlines/py_houghlines.html
    #                          edges       rho   theta   thresh         # min length, max gap:        
    lines = cv2.HoughLinesP(processed_img, 1, np.pi/180, 180,      20,         15)
    draw_lines(processed_img,lines)
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
    while (True):
        screen =  np.array(ImageGrab.grab(bbox=(0,40,800,640)))
        print('Frame took {} seconds'.format(time.time()-last_time))
        new_screen = process_img(screen)
        last_time = time.time()
        cv2.imshow('window', new_screen)
        #cv2.imshow('window',cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

main()
