import json
import requests
mydata = {"wd":"linux","name":"xwp"}
r = requests.post('http://httpbin.org/post',data = mydata)
print(r.text)