#!/usr/local/bin/python

import os
import cv
import datetime
from threading import Timer

cascade_name = "/usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml"

def detect_and_draw(src_img):
    cascade = cv.Load(cascade_name)
    faces = cv.HaarDetectObjects(src_img, cascade, cv.CreateMemStorage())
    for (x,y,w,h),n in faces:
        cv.Rectangle(src_img, (x,y), (x+w,y+h), 255)

    return src_img

def captureFromCam():
    try:
        date = datetime.datetime.today()

        if not (os.path.isdir('photo')):
            os.mkdir('photo')

        os.chdir('photo')
        
        dirname = date.strftime('%Y-%m-%d')
        if not (os.path.isdir(dirname)):
            os.mkdir(dirname)
        
        os.chdir(dirname)

        filename = date.strftime('%Y-%m-%d_%H-%M-%S')
        capture = cv.CaptureFromCAM(0)
        img = cv.QueryFrame(capture)
        
        face_img = detect_and_draw(img)
        
        cv.SaveImage('%s.jpg' % filename, face_img)
 
        os.chdir('..' + os.sep + '..')

        printLog('Capture', 'Success ...')

    except:
        printLog('Capture', 'Falied ...')

def printLog(section, log):
    date = datetime.datetime.today()
    print '[%s - %s] %s' % (date.strftime('%Y-%m-%d %H:%M:%S'), section, log)

if __name__ == "__main__":
    printLog('SYSTEM', 'Starting Face detection ...')
    
    captureFromCam()
    
    sec = 15.0
    
    printLog('SYSTEM', 'Timer Setting ... (%d sec)' % sec)
    
    while True:
        t = Timer(sec, captureFromCam)
        t.run()
