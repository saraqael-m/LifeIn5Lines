import cv2, numpy as np, scipy.ndimage # import necessary libraries
img = (cv2.cvtColor(cv2.imread("start.png"),cv2.COLOR_BGR2GRAY)/255+.5).astype("uint8") # get start image
while cv2.imshow("Life in 5 lines", img*255) == None and cv2.waitKey(1) != 27 and cv2.getWindowProperty("Life in 5 lines", cv2.WND_PROP_VISIBLE) > 0: # main loop (ends when esc is pressed or window is closed)
	neighbor_count = scipy.ndimage.correlate(img,np.array([[1,1,1],[1,0,1],[1,1,1]]),mode="constant") # neighbor count of each cell
	img = (np.logical_and((neighbor_count == 2) + (neighbor_count == 3), img) + np.logical_and(neighbor_count == 3, 1-img)).astype("uint8") # game of life rules
