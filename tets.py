import requests
def getResponse(url,params,headers):
    response = requests.post(url,headers=headers,params=params)
    print(response.text)   
if __name__ == '__main__':
    url = 'http://bbs.whnet.edu.cn/cgi-bin/bbssnd'
    file = open('text.txt','rb')
    text = file.read()
    params = {'board':'Football',\
              'file':'M.1508934884.A',\
              'title':'Re:【公告】绿茵场预约留言墙暨预约公告'.encode('gb2312'),\
              'text':text.decode('utf-8').encode('gb2312')}
    headers = {'Cookie':'titletype=forum; __utma=125160537.964021553.1520932000.1521682177.1522665850.4; __utmz=125160537.1522665850.4.4.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmt=1; __utmc=125160537; fingerprint=2229170977; utmpnum=17; utmpkey=33191553; utmpuserid=Swimmingcome; __utmb=125160537.74.6.1522669645789'
               ,'content-Type':'application/x-www-form-urlencoded'}
    getResponse(url,params,headers)

