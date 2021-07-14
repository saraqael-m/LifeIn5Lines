import cv2, numpy as np, scipy.ndimage
img = (cv2.cvtColor(cv2.imread("startDot.png"),cv2.COLOR_BGR2GRAY)/255+.5).astype("uint8")
while cv2.waitKey(1) != 27: # main loop (ends when esc is pressed)
	summed = scipy.ndimage.correlate(img,np.array([[1,1,1],[1,0,1],[1,1,1]]),mode="constant") # neighbor count of each cell
	img = (np.logical_and((summed == 2) + (summed == 3), img) + np.logical_and(summed == 3, 1-img)).astype("uint8") # game of life rules
	cv2.imshow("Conway's Game of Life", img*255) # show image
