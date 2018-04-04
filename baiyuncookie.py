import requests
import re
class BaiyunCookie():
	username = ''
	password = ''
	cookie = ''

	def __init__(self,username,password):
		self.username = username
		self.password = password
	def getCookie(self):
		params = {'id':self.username,'pw':self.password}
		headers = {}
		url = 'http://bbs.whnet.edu.cn/cgi-bin/bbslogin'
		response = requests.post(url,headers=headers,params = params,stream=True)
		#print (response.text)
		pattern = re.compile(r'cookie=\'(.+?);path')
		match = pattern.findall(response.text)
		result_cookie = ''
		try:
			for i in range(2,5):
				result_cookie = result_cookie+match[-i]+';'
		except:
			pass
		return result_cookie
if __name__ == '__main__':
	cookie = BaiyunCookie('Swimmingcome','zaiaswm.')
	cookie_to_get = cookie.getCookie()
	print (cookie_to_get)


	