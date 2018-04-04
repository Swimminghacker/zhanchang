from timeInfo import timeInfo
import time

targetTime = timeInfo.getTargetTime()

while True:
	currentTime = timeInfo.getCurrentTime()
	if((targetTime - currentTime) < 5):
		zhanchang = Zhanchang()
		
		print("ok")
		break;
	time.sleep(5)