In the last article, we explored basic image manipulation with OpenCV, and introduced Numpy array indexing for image processing. Today's post will cover much more capable image transforms.

Let's start by adding two images. For this example, we're going to need two images of the same size. Check the 'Code' folder for image examples. 

Let's start by loading our two images into memory. OpenCV allows three methods to add images: /
	a. Using the cv2.add() function: given two input image matrices of the same shape, this function computes their element-wise sum. Note that a matrix and a scalar can be passed to this function, in which case the scalar is added to each element of the input matrix (on a per-channel basis). This operation saturates--in other words, if the sum of two values (a matrix value-scalar sum or matrix value-matrix value sum) is greater than 255, the output volume will represent that position with 255. \

	b. Overloading the Python "+" operator: this operation is similar to the cv2.add() function, but does not saturate; instead, it takes each sum modulo 256. The first operand can be a matrix, while the second operand can be a matrix or a scalar. However, using this operator to add images in general is not recommended. \

	c. Using the cv2.addWeighted() function: A twist on traditional image addition. With this function, you can provide a weight for each of the image matrices provided. Note that the inputted image matrices must have the same shape! Suppose that m and n are our input image matrices. For the position (i, j, k), where k is the channel number, the output volume equals m_{i, j, k} * alpha + n_{i, j, k} * (1 - alpha) + gamma. In literature, you will also see 1 - alpha referred to as beta. gamma is an additional scalar added to each element-wise weighted sum. This function also saturates. \

The OpenCV documentation gives us good information about how these functions should be applied:

```python
#Using the saturating cv2.add() function
#image_matrix_one and image_matrix_two are input matrices with the same shape
#However, image_matrix_two can be a scalar
output = cv2.add(image_matrix_one, image_matrix_two)
```

```python
#Using the overloaded Python "+" operator
#image_matrix_one and image_matrix_two are input matrices with the same shape
#However, image_matrix_two can be a scalar
#Remember that each element-wise sum is computed modulo 256
output = image_matrix_one + image_matrix_two
```

```python
#Using the weighted and saturating cv2.addWeighted() function
#image_matrix_one and image_matrix_two are input matrices with the same shape
#alpha represents how opaque image_matrix_one is in the output volume
#The higher the alpha (closer to 1), the more opaque image_matrix_one is in the output volume
#beta = 1 - alpha
#gamma is the scalar value added to each element-wise weighted sum
output = cv2.addWeighted(image_matrix_one, alpha, image_matrix_two, beta, gamma)
```

That's all the material I'll cover for today. Tomorrow, we'll discuss more image operations, including bitwise operations and thresholding. 
