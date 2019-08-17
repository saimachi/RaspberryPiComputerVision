import cv2

grayscale = cv2.imread("dog_new.jpg", 0)

#Let's use the mean of a window to calculate thresholds for an image
#We will set every pixel greater than the mean in the window to 255
#The window size is 11x11, and 2 is subtracted from the calculated mean for each window

mean_threshold = cv2.adaptiveThreshold(grayscale, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
	cv2.THRESH_BINARY, 11, 2)
cv2.imshow("Mean Threshold", mean_threshold)

#Instead of using mean thresholding, we are using Gaussian-weighted sums
#In this case, the pixels closer to the center of the window will have a higher weight

gaussian_threshold = cv2.adaptiveThreshold(grayscale, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
	cv2.THRESH_BINARY, 11, 2)
cv2.imshow("Gaussian Threshold", gaussian_threshold)

cv2.waitKey(0)
cv2.destroyAllWindows()