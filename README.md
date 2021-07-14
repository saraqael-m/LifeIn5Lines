# LifeIn5Lines
This is a python simulation of the game of life by John Conway written in 5 lines of code.

## Usage and Dependencies

Tested with [**Python 3.7.9**](https://www.python.org/downloads/release/python-379/) but should work for other python versions quite good with maybe minimal adjustments. You need to install three python modules (can be installed via pip):

* [cv2](https://pypi.org/project/opencv-python/) (`pip install opencv-python`)
* [numpy](https://numpy.org/install/) (`pip install numpy`)
* [scipy](https://www.scipy.org/install.html) (`pip install scimpy`)

When you run the script either by cmd or via IDE you need to have the start image (black and white image to show which cells should live in first iteration) in the same folder as the .py file. It should be named "start.png" (unless you specified otherwise in the code) and shouldn't have a bigger resolution than your screen, so that you can see everything and it doesn't lag.

You can always quit the simulation by pressing the escape button while having the window selected or by clicking the "X" on the top of the window.

## Explanation

### First Line: Imports

`import cv2, numpy as np, scipy.ndimage`

It imports the necessary libraries. Namely **opencv-python** to display the image, **numpy** (as np) to include logical operators (like and-/or-gates) to apply to numpy arrays, and scipy (specifically scipy.ndimage.correlate) to count the number of living neighbors each cell has.

### Second Line: Reading Start Image

`img = (cv2.cvtColor(cv2.imread("start.png"),cv2.COLOR_BGR2GRAY)/255+.5).astype("uint8")`

This line reads the file (which has to be in the same directory as the .py file) named "start.png" and changes its colors first to grayscale, then to black and white (0's and 1's). These are the living cells (white pixels from start image) and dead cells (black cells from start image) in the first iteration.

### Third Line: While Loop

`while cv2.imshow("Life in 6 lines", img*255) == None and cv2.waitKey(1) != 27 and cv2.getWindowProperty("Life in 6 lines", cv2.WND_PROP_VISIBLE) > 0:`

This is the main loop which just repeats and executes one iteration of life. `cv2.imshow()` shows the img and is called inside this condition, so that the third condition can run properly, it returns nothing. The `cv2.waitKey(n)` function waits for n milliseconds for an ASCII input, where 27 is encoded to be the escape key. Without this command to wait for atleast 1 millisecond (like it is here) cv2 wouldn't display anything. Also this command allows the user to end the sim by pressing esc. The last bool if false, when the window was closed by the "X" button on the window and this ends the sim as well. Otherwise the window would just reopen.

### Fourth Line: Neighbor Counting

`summed = scipy.ndimage.correlate(img,np.array([[1,1,1],[1,0,1],[1,1,1]]),mode="constant")`

The [correlate function](https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.correlate.html) does the following:

> Correlation is the process of moving a filter mask often referred to as kernel over the image and computing the sum of products at each location.

Because we want the values of our neighboring cells to be added together but not the own of the central cell, we need this mask/kernel: 
`[[1,1,1],[1,0,1],[1,1,1]]`. With this the central cell is multiplied by zero and is thus never counted. We also pass in our image to this function and another parameter, called "mode", which just defines what should happen with cells at the edge of the image. "constant" means there are constant zero's around the edge of the image so that cells at the edge just come to a stop. You could also use "wrap" to make them appear on the other side of the image.

### Fifth Line: Logic of Life

`img = (np.logical_and((summed == 2) + (summed == 3), img) + np.logical_and(summed == 3, 1-img)).astype("uint8")`

Here I implement all the four rules in one line. From the beginning all cells are considered dead. Then the cells which have two or three neighbors (`(summed == 2) + (summed == 3)`) **and** (`np.logical_and()`) were already alive (`img`; ones are alive cells -> converted to true) are updated to living status. Finally the cells which have exactly three neighbors (`summed == 3`) **and** were dead (`1-img`; all dead cells become ones -> converted to true) also become living. These are then combined together and converted to an integer array for the new image of cells. One iteration done.

Done! That's all there is to it.
