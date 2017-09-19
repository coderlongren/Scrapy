import requests
res=requests.get("http://www.baidu.com")
savefile=open("baidu.html","w")
savefile.write(res.content)
savefile.close()
