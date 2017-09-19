import requests
res=requests.get("http://www.taobao.com")
savefile=open("taobao.html","w")
savefile.write(res.content)
savefile.close()
