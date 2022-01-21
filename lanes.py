import cv2
import numpy as np

# Read the image from the file 
image = cv2.imread('test_image.jpeg')
lane_image = np.copy(image)
gray = cv2.cvtColor(lane_image, cv2.COLOR_RGB2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), 0)
canny = cv2.Canny(blur, 50, 150)
# Display Image
cv2.imshow('result', canny)
cv2.waitKey(0)

