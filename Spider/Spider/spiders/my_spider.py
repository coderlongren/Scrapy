# -*- coding:utf-8 -*-
import sys
from Spider.items import teacher_item
import scrapy
import json
class firstSpider(scrapy.Spider):
    name = "teacher"
    #allowd_domains  = ["http://itcast.cn"]
    #终于可以使用中文了 哈哈哈
    def start_requests(self):
        urls = [
            "http://www.itcast.cn/channel/teacher.shtml#ac"
        ]
        for url in urls:
            yield scrapy.Request(url = url,callback = self.parse)
    def parse(self,response):
	reload(sys)
	sys.setdefaultencoding('utf-8')
        items = []
        #file_name = "teacher.html"
        f = open("teacher.txt",'a')
        for site in response.xpath('//div[@class="li_txt"]'):
	    item = teacher_item()
            teacher_name = site.xpath('h3/text()').extract()
            teacher_level = site.xpath('h4/text()').extract()
            teacher_info = site.xpath('p/text()').extract()
	    teacher_list = teacher_name + teacher_level + teacher_info
	    f.write(str(teacher_list))
            #f.write(teacher_name )
	    #f.write(teacher_level )
	    #f.write(teacher_info )
	    print(teacher_name[0])
	    print(teacher_level[0])
	    print(teacher_info[0])
	    print("===============")
	    item["name"] = teacher_name[0]
	    item["level"] = teacher_level[0]
	    item["info"] = teacher_info[0]
	    items.append(item)
       #open("teacher.txt",'w').write(str(items))
       #print(json.dumps(items))
