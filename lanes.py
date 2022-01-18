import cv2

# Read the image from the file 
image = cv2.imread('test_image.jpeg')
# Display Image
cv2.imshow('result', image)
cv2.waitKey(0)