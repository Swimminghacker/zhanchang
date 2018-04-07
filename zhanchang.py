import requests
import baiyuncookie
from user import User

class Zhanchang():
  def getResponse(self,url,data,headers):
      response = requests.post(url,headers=headers,data=data)
      #print(response.text)
      print('end')

  def doZhanchang(self):
      url = 'http://bbs.whnet.edu.cn/cgi-bin/bbssnd'
      file = open('text.txt','r',encoding='utf-8')
      text = file.read()
      data = {'board':'Football',\
                'file':'M.1508934884.A',\
                'title':'Re: 【公告】绿茵场预约留言墙暨预约公告'.encode('gb2312'),\
                'text':text.encode('gb2312','ignore')}
      user = User('user.txt')
      userName = user.getUsername()
      password = user.getPassword()
      cookie = baiyuncookie.BaiyunCookie(userName,password)
      cookie_to_get = cookie.getCookie()
      #print(cookie_to_get)
      headers = {'Cookie':cookie_to_get,'content-Type':'application/x-www-form-urlencoded'}
      self.getResponse(url,data,headers)

if __name__ == '__main__':
  zc = Zhanchang()
  zc.doZhanchang()