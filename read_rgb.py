# http://www.bogotobogo.com/python/OpenCV_Python/python_opencv3_basic_image_operations_pixel_access_image_load.php
import cv2
import numpy as np
from builtins import print

img = cv2.imread('palm.jpg')

# print(img[:, :, 0]) #red
# print(img[:, :, 1]) #green
# print(img[:, :, 2]) #blue