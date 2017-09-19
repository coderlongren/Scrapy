import requests
url = "http://www.baidu.com"
rq = requests.get(url)
print(rq.text)