class User(object):
	"""docstring for user"""
	userName = ''
	password = ''
	user = ['','']
	
	def __init__(self,fileName):
		try:
			file = open(fileName,'r')
			self.user = file.read().split()
		except Exception as e:
			pass
		

	def getUsername(self):
		return self.user[0]
	def getPassword(self):
		return self.user[1]
	