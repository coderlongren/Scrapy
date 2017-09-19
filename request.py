import requests
#可以　获得百度搜索的html代码
myparams = {'wd':'linux'}
r = requests.get('http://www.baidu.com/s',params = myparams)
fp = open("linux.html","w")
fp.write(r.content)
fp.close()
