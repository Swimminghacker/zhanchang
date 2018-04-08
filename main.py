from zhanchang import Zhanchang
from timeInfo import timeInfo
import time
if __name__ == '__main__':

	select = eval(input("请选择发帖模式：1.定时发帖；2.即使发帖\n"))
	if select == 1:

		targetTime = timeInfo.getTargetTime()
		currentTime = timeInfo.getCurrentTime()
		if currentTime > targetTime:
			print('时间有误')
		while True:
			currentTime = timeInfo.getCurrentTime()
			diffTime = targetTime - currentTime
			if diffTime > 1000 and diffTime%600 == 0:
				print('距离目标发帖时间还有'+str(int(diffTime/600))+'0分钟'+'\t请等待...')
			elif 1000 > diffTime >60 and diffTime%60 == 0:
				print('距离目标发帖时间还有'+str(int(diffTime/60))+'分钟'+'\t请等待...')
			elif diffTime < 60:
				print('距离目标发帖时间还有'+str(diffTime)+'s'+'\t请等待...')
			if diffTime < 0:
				break
			elif diffTime < 2:
				zc = Zhanchang()
				zc.doZhanchang()
				print("发帖成功")
				time.sleep(1)
				break
			time.sleep(1)
		input('按任意键继续...')
	elif select == 2:
		print("正在发帖...")
		zc = Zhanchang()
		zc.doZhanchang()
		print("发帖成功~")
		input('按任意键继续...')
	else:
		#print(select,type(select))
		input("输入有误，按任意键继续...")

