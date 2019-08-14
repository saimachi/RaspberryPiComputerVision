import cv2

#Feel free to provide your own images!
dog_image = cv2.imread("dog.jpg")
cat_image = cv2.imread("CatForAddition.jpg")

#Comment out this assertion if cat_image (the second image) is a scalar
assert dog_image.shape == cat_image.shape

overloaded_sum = dog_image + cat_image
cv2.imshow("Overloaded '+' Operator", overloaded_sum)

saturating_sum = cv2.add(dog_image, cat_image)
cv2.imshow("Saturating Sum", saturating_sum)

#Between 0 and 1
#The closer (alpha) to 1, the more opaque the dog image will be in the output
alpha = .5
beta = 1 - alpha
gamma = 0
output_weighted_sum = cv2.addWeighted(dog_image, alpha, \
	cat_image, beta, gamma)
cv2.imshow("Weighted Addition Result", output_weighted_sum)

cv2.waitKey(0)
cv2.destroyAllWindows()
