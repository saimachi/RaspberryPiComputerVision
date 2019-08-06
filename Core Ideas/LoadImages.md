Welcome back! I hope you all set up your OpenCV environment!

To start, test that your install succeeded:
```python
import cv2
print(cv2.__version__)
```

If you don't get any import errors and your OpenCV version is fairly recent (the current OpenCV stable release is 4.1.1), review the installation steps provided in the previous guide. In the last guide, I only mentioned installing OpenCV; in my opinion, most confusion stems from installing the package. You are also going to need numpy and matplotlib, both of which I recommend installing through pip. Test the installs as follows: 
```python
import numpy as np
import matplotlib

print(np.__version__)
print(matplotlib.__version__)
```

With the software packages out of the way, let's read in an image. How about this picture of a dog? 
