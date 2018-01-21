# import the necessary packages
import argparse
import datetime
import imutils
import time
import cv2
import numpy as np
import keyboard_test as music


music.unmute()
mute=False

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="path to the video file")
ap.add_argument("-a", "--min-area", type=int, default=350, help="minimum area size")
args = vars(ap.parse_args())
'''
# if the video argument is None, then we are reading from webcam
if args.get("video", None) is None:
	camera = cv2.VideoCapture(0)
	time.sleep(0.25)

# otherwise, we are reading from a video file
else:
	'''
camera = cv2.VideoCapture(0)
time.sleep(0.25)


# initialize the first frame in the video stream
firstFrame = None
temp = None
num=0
rev_num=0

# loop over the frames of the video
while True:

	# grab the current frame and initialize the occupied/unoccupied
	# text
	(grabbed, frame) = camera.read()
	text = "Unoccupied"

	# if the frame could not be grabbed, then we have reached the end
	# of the video
	if not grabbed:
		break

	# resize the frame, convert it to grayscale, and blur it
	frame = imutils.resize(frame, width=500)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (21, 21), 0)

	# if the first frame is None, initialize it
	if firstFrame is None:
		firstFrame = gray
		continue
	else:
		for i in range(3):
			(grabbed, frame) = camera.read()
			if not grabbed:
				break
		if not grabbed:
			break
		frame = imutils.resize(frame, width=500)
		grayy= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		grayy = cv2.GaussianBlur(grayy, (21, 21), 0)
		firstFrame = grayy


	# compute the absolute difference between the current frame and
	# first frame
	frameDelta = cv2.absdiff(firstFrame, gray)
	thresh = cv2.threshold(frameDelta,0, 150, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]
	#!st NUMBER IS SENSITIVITY

	# dilate the thresholded image to fill in holes, then find contours
	# on thresholded image
	kernel = np.ones((13,13),np.uint8)
	thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
	(_,cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)

	# loop over the contours
	for c in cnts:


		#print ('we made it ',num)

		# if the contour is too small, ignore it
		if cv2.contourArea(c) <= args["min_area"]:
			continue
			''''
			if mute == False:
				music.mute()
			#	time.sleep(1)

				mute = True

			elif mute == True:
				continue

		if cv2.contourArea(c) > args["min_area"]:
			if mute == True:
				music.unmute()
			#	time.sleep(1)
				mute = False
			#elif mute == False:
			'''

		# compute the bounding box for the contour, draw it on the frame,
		# and update the text
		(x, y, w, h) = cv2.boundingRect(c)
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
		text = "Occupied"


	# draw the text and timestamp on the frame
	cv2.putText(frame, "(Team Gucci Main() Room Status: {}".format(text), (10, 20),
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
	cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
		(10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

	# show the frame and record if the user presses a key
	#cv2.imshow("Security Feed", frame)
	cv2.imshow("Thresh", thresh)
	cv2.imshow("Frame Delta", frameDelta)
	cv2.imshow("Security Feed", frame)

	key = cv2.waitKey(1) & 0xFF




	if text == "Occupied":
		num=0
		rev_num=rev_num+1
		if mute == True and rev_num>2:
			music.unmute()
		#	time.sleep(1)
			mute = False
		#elif mute == FALSE:
	else:
		rev_num=0
		num=num+1
		if mute == False and num>3:
			music.mute()
		#	time.sleep(1)
			mute = True
		#elif mute == True:

	# if the `q` key is pressed, break from the lop
	if key == ord("q"):
		break

	print ('consecutive periods of NO movement: '+str(num))
	print ('consecutive periods of movement: '+str(rev_num))

# cleanup the camera and close any open windows
camera.release()
cv2.destroyAllWindows()
