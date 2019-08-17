Hello everyone! Today, we'll cover thresholding, an important tool for computer vision.

The logical next step from the last post would be to cover bitwise operations with OpenCV. However, as it turns out, using these functions in a vacuum would seem pointless; I will instead introduce these bitwise operations as they're needed.

You can guess what thresholding does based upon the word: it likely performs some element-wise operation when a pixel exceeds some *threshold*. That intuition is almost correct! When a pixel of a grayscale image exceeds a given threshold, that pixel is assigned a provided value. Each pixel that exceeds the threshold in the input volume is assigned the same value. This is simple thresholding.

OpenCV implements simple thresholding with the cv2.threshold() function, and as mentioned before, requires a grayscale image to be passed to it. Let's look at an example of using the function:

```python
grayscale = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
THRESHOLD_REQUIREMENT = 125
THRESHOLD_REPLACEMENT = 255
OPERATION = cv2.THRESH_BINARY
(thresh_val, thresh_image) = cv2.threshold(grayscale, THRESHOLD_REQUIREMENT, \
	THRESHOLD_REPLACEMENT, OPERATION)

print(thresh_val)		#Should be the same as THRESHOLD_REQUIREMENT
```

This code works, but it's difficult to choose the thresholding test value. That's where adaptive thresholding comes in. However, there are other tricks that simple thresholding has. Namely, we can apply different forms of thresholding:

	a. cv2.THRESH_BINARY: Given our grayscale image, this transform sets each pixel to a replacement value if it is greater than the threshold requirement. In other words, the desired part of the image is black against a white background. 
	b. cv2.THRESH_BINARY_INV: Performs the same operation as above, but renders the segmented part of the image as white against a black background. 
	c. cv2.THRESH_TRUNC: Each pixel intensity is kept the same if it is not greater than the threshold. 
	d. cv2.THRESH_TOZERO: If the given pixel does not have an intensity greater than the threshold, it is set to 0. 
	e. cv2.THRESH_TOZERO_INV: Functions opposite to cv2.THRESH_TOZERO, segmenting the region to white against a black background. 

Let's cover adaptive thresholding next. The previous examples set the threshold to a static value, but this may not work for all lighting conditions. Adaptive thresholding algorithmically determines the threshold to apply at certain portions of the image. Let's see how adaptive thresholding is used in practice:

```python
REPLACEMENT = 255
OPERATION = cv2.THRESH_BINARY
CALC_SIZE = 11
C = 2
thresh_image = cv2.adaptiveThreshold(grayscale,REPLACEMENT,cv2.ADAPTIVE_THRESH_MEAN_C,
            OPERATION,CALC_SIZE,C)
```

The adaptiveThreshold() function is somewhat similar to simple thresholding. The first argument that we pass in is the grayscale image to be thresholded. The second argument serves the same function as mentioned for simple thresholding. However, cv2.ADAPTIVE_THRESH_MEAN_C refers to the threshold calculation method for each portion. The section below will give more information about these methods. The next argument describes the simple thresholding algorithm for each portion in the input volume. The next argument depicts the size of the window used for the threshold calculation: the window size is CALC_SIZE by CALC_SIZE, and choose a value for CALC_SIZE that is odd and greater than or equal to 3. The final argument refers to the value subtracted from the calculated threshold for each window.

There are some important details about this function:

	a.  The thresholding operation (OPERATION) must either be cv2.THRESH_BINARY or cv2.THRESH_BINARY_INV. 
	b. The function only returns a single value to unpack, rather than a tuple. 
	c. cv2.ADAPTIVE_THRESH_MEAN_C: The threshold for each window is the mean of the window pixel values minus the C constant.
	d. cv2.ADAPTIVE_THRESH_GAUSSIAN_C: Uses a Gaussian-weighted sum for each window minus the specified constant to determine the threshold. 

I know that this article is starting to get pretty long. However, there's one more trick that I want to show you: Otsu's Binarization. I won't get into how it works, but realize that it calculates a global threshold value. Just use the standard cv2.threshold() function, but add the cv2.THRESH_OTSU constant and don't worry about setting an ideal global threshold.

```python
(otsu_thresh_val, otsu_thresh_image) = cv2.threshold(grayscale, 255, 255,
	cv.THRESH_BINARY + cv2.THRESH_OTSU)
```

That's it for today! In the next post, we'll be starting our adventures with filtering!