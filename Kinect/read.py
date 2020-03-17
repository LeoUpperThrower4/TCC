from cv2 import cv2 as cv
import os
import numpy as np
import time

os.chdir(r"c:\Users\Leo\Documents\VSC\TCC\Kinect")
operation = input("Start image gathering [y/n]: ")

if operation == "y":
    images_to_save = []
    vid_stream = cv.VideoCapture(0)
    while vid_stream.isOpened():
        _, frame = vid_stream.read()
        
        frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        frame = cv.flip(frame, 1)
        cv.imshow("image", frame)
        print("Camera`s recording at: " + str(vid_stream.get(cv.CAP_PROP_FPS)))

        images_to_save.append(frame)
        key = cv.waitKey(1)
        if key == ord("q"):
            break

    for img in images_to_save:
        name = str(time.time())+".jpg"
        cv.imwrite(name, img, )
else:
    exit()