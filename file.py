file.py
import requests
files = {"file":open('xwp.jpg','rb')}
r = requests.post(url,files = files)
print(r.text)
