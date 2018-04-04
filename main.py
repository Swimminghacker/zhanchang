from zhanchang import Zhanchang
from timeInfo import timeInfo
import time
if __name__ == '__main__':

	targetTime = timeInfo.getTargetTime()
	currentTime = timeInfo.getCurrentTime()
	if currentTime > targetTime:
		print('时间有误')
	while True:
		currentTime = timeInfo.getCurrentTime()
		diffTime = targetTime - currentTime
		print('距离目标时间还有'+str(diffTime)+'s')
		if diffTime < 0:
			break
		elif diffTime < 2:
			zc = Zhanchang()
			zc.doZhanchang()
			print("ok")
			break
		time.sleep(1)
