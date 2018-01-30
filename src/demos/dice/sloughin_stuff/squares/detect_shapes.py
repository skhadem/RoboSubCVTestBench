from pyimagesearch.shapedetection import ShapeDetection
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the input image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
#resized = cv2.resize(image, (480,300))
resized = cv2.resize(image, (480, 360))
ratio = image.shape[0] / float(resized.shape[0])

gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
# thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]
# cv2.imshow("thresh", thresh)
# cv2.waitKey(0)
cnts = cv2.findContours(blurred.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]
sd = ShapeDetection()
# cv2.imshow('shapes', image)
# print(len(cnts));
for c in cnts:
	print(c)
	M = cv2.moments(c)
	if M["m00"] != 0:
		cX = int((M["m10"] / M["m00"]) * ratio)
		cY = int((M["m01"] / M["m00"]) * ratio)
	else:
		cX = 1
		cY = 1
	shape = sd.detect(c)
	c = c.astype("float")
	c *= ratio
	c = c.astype("int")
	cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
	#cv2.putText(image, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
	cv2.imshow("Image", image)
	ch = cv2.waitKey(0)
cv2.destroyAllWindows()
