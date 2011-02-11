#!/usr/local/bin/python

import os
import cv
import datetime
from threading import Timer

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
        cv.SaveImage('%s.jpg' % filename, img)

        os.chdir('..' + os.sep + '..')

        printLog('Capture', 'Success ...')

    except:
        printLog('Capture', 'Falied ...')

def printLog(section, log):
    date = datetime.datetime.today()
    print '[%s - %s] %s' % (date.strftime('%Y-%m-%d %H:%M:%S'), section, log)

if __name__ == "__main__":
    printLog('SYSTEM', 'Starting Look at me ...')
    
    captureFromCam()
    
    sec = 15.0
    
    printLog('SYSTEM', 'Timer Setting ... (%d sec)' % sec)
    
    while True:
        t = Timer(sec, captureFromCam)
        t.run()
