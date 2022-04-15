import cv2
import numpy as np
import pyautogui
import time
import datetime



import cv2
capture = cv2.VideoCapture(0)
time = datetime.datetime.now()

fgbg = cv2.createBackgroundSubtractorMOG2(300, 400, True)

frameCount = 0

while(1):
	ret, frame = capture.read()

	if not ret:
		break

	frameCount += 1
	resizedFrame = cv2.resize(frame, (0, 0), fx=0.50, fy=0.50)

	fgmask = fgbg.apply(resizedFrame)

	count = np.count_nonzero(fgmask)

	if (frameCount > 1 and count > 100):
		print('Someone is in your house')
	cv2.imshow('Frame', resizedFrame)
	cv2.imshow('Mask', fgmask)
	print(time)


	k = cv2.waitKey(1) & 0xff
	if k == 27:
		break

capture.release()
cv2.destroyAllWindows()