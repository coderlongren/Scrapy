import requests
def getText(url):
	try:
	  r = requests.get(url,timeout = 30)
	  r.raise_for_status()
	  r.encoding = r.apparent_encoding
	  return r.text
	except:
	  return "exception"	
url = "http://www.baidu.com"
print(getText(url))
	
	
	
	
