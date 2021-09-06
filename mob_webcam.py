# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 18:40:00 2021

@author: MANJEET KUMAR YADAV
"""

import cv2
import numpy as np
url="192.168.43.1"
cp=cv2.VideoCapture()
while(True):
    camara, frame =cp.read()
    if frame is not None:
        cv2.imshow("frame",frame)
    q=cv2.waitKey(1)
    if q==ord("q"):
        break
cv2.destroyAllWindows()











