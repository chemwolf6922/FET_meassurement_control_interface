import cv2
import numpy as np

capture=cv2.VideoCapture(1)
capture.set(3,640)
capture.set(4,360)
while not capture.isOpened(): pass

while True:
    ret,frame = capture.read()
    cv2.imshow('camera',frame)
    key = cv2.waitKey(1)
    if (key & 0xFF) ==0x71:
        break
