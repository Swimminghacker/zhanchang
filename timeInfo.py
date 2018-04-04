import time
class timeInfo(object):
	"""docstring for currentTime"""

	@staticmethod
	def getCurrentTime():
		current_time = int(time.time())
		return current_time

	@staticmethod
	def getTargetTime(fileName='targetTime.txt'):
		file = open(fileName,'r')
		timeStr = file.read() 
		timeArray = time.strptime(timeStr,'%Y-%m-%d %H:%M:%S')
		timeStamp = int(time.mktime(timeArray))
		return timeStamp
