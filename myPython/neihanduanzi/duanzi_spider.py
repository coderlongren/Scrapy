#-*- coding:utf-8 -*-  
import requests
import sys
import urllib2
import re
class Spider:
    '''
	内涵段子的一个爬虫类
    '''
    def __init__(self):
        self.page = 1
	self.key = True

    def load_page(self,page):
	#print("start catch.......")
	url = "http://www.neihan8.com/article/list_5_" + str(page) + ".html" 
	user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36"
	headers = {"USer-Agent":user_agent}
	req = requests.get(url,headers=headers)
	html = req.content
	'''	req = urllib2.Request(url,headers = headers)
		response = urllib2.urlopen(req)
		html = response.read()
        '''
	gbk_html = html.decode('gbk').encode('utf-8')
	#print(gbk_html)
	#用正则表达式 过滤段子的内容 得到所有的段子
	#所有的段子在<div class="f18 mb20">.........</div>中间
	pattern = re.compile(r'<div.*?class="f18 mb20">(.*?)</div>',re.S)
	item_list = pattern.findall(gbk_html)
	#for item in item_list:
	# item.replace("<p>","").replace("</p>","").replace("br /","")
	return item_list
    def action_page(self,item_list,the_page):
	#print("这是第 %d的段子", %(the_page))
	for item in item_list:
	    print("============================")
	    print(item.replace("<p>","").replace("</p>","").replace("<br />",""))
	    self.write_to_file(item.replace("<p>","").replace("</p>","").replace("<br />",""))

		
    def write_to_file(self,txt):
	f = open("./myStory.txt",'a')
	f.write(txt)
	f.write("=========================")
	f.close()
    def work(self):
	while (self.key):
	    print("press anykey to cotinue,")
            print("press 'quit' to end")
	    str = raw_input()
	    if (str == "quit"):
	        break
	    item_list = self.load_page(self.page)
	    self.action_page(item_list, self.page)
	    self.page += 1



#main
if __name__ == "__main__":
    #创建一个Spider对象
    reload(sys)
    sys.setdefaultencoding('utf-8')
    mySpider = Spider()

    mySpider.work()  
