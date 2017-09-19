#-*- coding:utf-8 -*-
# 识别中文
import urllib2
import requests
import sys
def load_page(url):
    '''
        get html of url 
    '''

    user_agent="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36"
    headers = {"User-Agent":user_agent}
    ''' 
        req = urllib2.Request(url,headers = headers)
        response = urllib2.urlopen(req)
        html = response.read()B
    '''
    #呵呵呵呵
    response = requests.get(url,headers=headers)
    html = response.text
    return html
def write_to_file(file_name,txt):
    f  = open(file_name,'w')
    f.write(txt)
    f.close()
def tieba_spider(url,begin_page,end_page):
    '''
	贴吧小助手的方法
    '''
    for i in range(begin_page,end_page + 1):
    # i = 1 pn = 0
    # i = 2 pn = 100
    # i = 3 pn = 150
    
        pn = 50*(i - 1)
        #组成一个完整的url地址
    
        my_url = url + str(pn)
        # print(my_url)
        lolhtml = load_page(my_url)
	file_name = str(i) + ".html"
	print(file_name)
	write_to_file(file_name,lolhtml)

#mian
if __name__ == "__main__":
    reload(sys)  
    sys.setdefaultencoding('utf8')   
    url = raw_input("请输入贴吧的url地址")
    # print(url)

    begin_page = int(raw_input("起始页码"))
    end_page = int(raw_input("终止页码"))
    tieba_spider(url,begin_page,end_page)
    print(begin_page)
    print(end_page)
    print("sdfsdfs")
    
