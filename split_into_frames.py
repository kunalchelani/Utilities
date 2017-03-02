import cv2 as cv
import math
import sys
import os

arglen = len(sys.argv)
if arglen == 1:
	print "The first argument needs to be the path for the video"
	sys.exit()

videoPath  = sys.argv[1]
videoName = ((videoPath.split("/"))[-1]).split(".")[0]

vidcap = cv.VideoCapture(videoPath)
success,image  = vidcap.read()
print success
#Uncomment to change the starting time of split process
#vidcap.set(0,100);
#This gives you roughly framerate/5 frames per second. Adjust as per needs
frameRate = vidcap.get(5)

count = 0

if (arglen > 2):
	frameDirectory = sys.argv[2]
else :
	newPath = "./" + videoName + "_frames"
	if not os.path.exists(newPath):
		os.makedirs(newPath)
	frameDirectory = newPath

while success:
	success, image = vidcap.read()
	frameId = vidcap.get(1);
	if (frameId % (math.floor(frameRate/5)) == 0):
		imagePath = (frameDirectory + "/" + videoName + "frame%d" % count  + ".JPEG")
		cv.imwrite(imagePath, image)
		count+= 1
	if (cv.waitKey(10) == 27):
		break
