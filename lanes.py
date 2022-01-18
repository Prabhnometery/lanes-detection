import cv2
import numpy as np

# Read the image from the file 
image = cv2.imread('test_image.jpeg')
lane_image = np.copy(image)
gray = cv2.cvtColor(lane_image, cv2.COLOR_RGB2GRAY)
# Display Image
cv2.imshow('result', gray)
cv2.waitKey(0)