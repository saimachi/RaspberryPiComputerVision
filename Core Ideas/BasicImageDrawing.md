If you have not already viewed the previous tutorial on loading images with OpenCV, I would highly recommend that you do so now. Today's concepts will build upon those ideas. More specifically, we will be drawing basic shapes and text onto loaded images: though this may seem silly now, it has practical applications in visualizing vision algorithms.

Let's get started by loading an image into memory for manipulation. I'll use the same dog image as last time, but feel free to use your own image. Regardless of which image you choose, import OpenCV and read the image in color:

```python
import cv2

im = cv2.imread('dog.jpg')
```

Note that by default, OpenCV will load the image in the BGR color format without the alpha channel. Now, let's add a line:

```python
cv2.line(im, (0, 0), (75, 75), (255, 0, 0), 10)
``` 

And of course, to display the modified image in a window, add the event handling code:

```python
cv2.imshow('Line', im)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

In general, the cv2.line(_image_, _p1_, _p2_, _color_, _thick_) overlays a line of color tuple _color_ and thickness _thick_ stretching from point tuple _p1_ to _p2_ on top of _image_.

Obviously, OpenCV gives you more shape commands. cv2.rectangle() is similar; however, instead of specifying a start and end point, we must specify the top left vertex and the bottom right vertex. 

```python
cv2.rectangle(im, (5, 5), (75, 75), (0, 255, 0), 10)
``` 

The first tuple represents the top-left vertex, and the second tuple the bottom-right vertex.

Putting text onto an image is important too. Luckily, OpenCV provides a function for just that!

```python
cv2.putText(im, "Displaying Text!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (128, 128, 128), 3, cv2.LINE_AA)
``` 

In this example, "Displaying Text!" is written to the image such that the bottom-left corner of the text is at (50, 50). The font is "Hershey Simplex", but there are other options (like "Hershey Plain" or "Hershey Complex"). Each font is given a base size, and in our example, we do not change it (we scale it by a factor of 1). The text is rendered gray with a line thickness of 3. The text is antialiased (it uses software to refine the jagged lines that result from trying to draw a continuous line).

That's all for today! Notice that I didn't go very in-depth on this topic. The reason is that I don't want to show you too many commands which may not seem applicable now. My goal is to teach you computer vision concepts as they relate to OpenCV, and if you need some specific capabilities for your project, you can research those features and use them.

In the next tutorial, we will start discussing actual computer vision concepts. First, we will talk about how images are encoded at the pixel level, and reference portions of images (also known as ROIs--Regions of Interest). We will also cover some basic operations on image(s), like overlaying.