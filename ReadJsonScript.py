from os import listdir
from os.path import isfile, join
import json
from shutil import copyfile
import os
import numpy as np
import cv2

gray_image =cv2.imread("D:\\DonkeyCar\\DonkeyImages\\log_canny\\0_cam-image_array_.jpg")

img2 = np.zeros_like(gray_image)
img2[:,:,0] = gray_image
img2[:,:,1] = gray_image
img2[:,:,2] = gray_image

cv2.circle(img2, (10,10), 5, (255,255,0))
cv2.imshow("colour again", img2)
cv2.waitKey()


input('asd')