#coding=utf-8
import urllib
def getHtml(url):
	#get html from the url
	page = urllib.urlopen(url)
	html = page.read()
	return html
html = getHtml("http://www.baidu.com")
print(html)

