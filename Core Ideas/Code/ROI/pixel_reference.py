import cv2

im = cv2.imread("<IMAGE FILE PATH GOES HERE>")
cv2.imshow("Original Image", im)

#Accessing pixels: do not approach image manipulation this way!
#Use vectorized operations with ROIs
pixel = im[100,100]
print(pixel)

#ROI accessing
im[100:150,100:150] = [255,255,255]
cv2.imshow("ROI", im)

#Image attributes
print(im.shape)
print(im.dtype)

cv2.imsave("<OUTPUT FILE PATH GOES HERE>", im)

cv2.waitKey(0)
cv2.destroyAllWindows()
