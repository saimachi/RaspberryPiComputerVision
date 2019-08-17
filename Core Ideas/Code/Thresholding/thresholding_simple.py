import cv2

im = cv2.imread("dog_new.jpg")
grayscale = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

THRESHOLD_REQUIREMENT = 100
THRESHOLD_REPLACEMENT = 255
OPERATION = cv2.THRESH_BINARY

(thresh_val, thresh_image) = cv2.threshold(grayscale, THRESHOLD_REQUIREMENT, \
	THRESHOLD_REPLACEMENT, OPERATION)
cv2.imshow("Thresholding Binary", thresh_image)
print(thresh_val)		#Should be the same as THRESHOLD_REQUIREMENT

OPERATION = cv2.THRESH_BINARY_INV
(thresh_val, thresh_image) = cv2.threshold(grayscale, THRESHOLD_REQUIREMENT, \
	THRESHOLD_REPLACEMENT, OPERATION)
cv2.imshow("Thresholding Binary Inverse", thresh_image)
print(thresh_val)

OPERATION = cv2.THRESH_TRUNC
(thresh_val, thresh_image) = cv2.threshold(grayscale, THRESHOLD_REQUIREMENT, \
	THRESHOLD_REPLACEMENT, OPERATION)
cv2.imshow("Thresholding Truncation", thresh_image)
print(thresh_val)

OPERATION = cv2.THRESH_BINARY + cv2.THRESH_OTSU
(thresh_val, thresh_image) = cv2.threshold(grayscale, THRESHOLD_REQUIREMENT, \
	THRESHOLD_REPLACEMENT, OPERATION)
cv2.imshow("Thresholding Otsu", thresh_image)
print(thresh_val)

cv2.waitKey(0)
cv2.destroyAllWindows()