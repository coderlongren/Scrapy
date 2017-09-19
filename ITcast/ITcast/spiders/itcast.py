# -*- coding: utf-8 -*-
import scrapy

from ITcast.items import TeacherItem
import json
import sys

class ItcastSpider(scrapy.Spider):
    name = "itcast"
    allowed_domains = ["http://www.itcast.cn/channel/teacher.shtml"]
    start_urls = (
	"http://www.itcast.cn/channel/teacher.shtml",
    )

    def parse(self, response):
	reload(sys)
	sys.setdefaultencoding('utf-8')
	#print(response.body)
	node_list = response.xpath('//div[@class="li_txt"]')
	for node in node_list:
	    #.extract()
	    item = TeacherItem()
	    name = node.xpath('h3/text()').extract()
        level = node.xpath('h4/text()').extract()
        info = node.xpath('p/text()').extract()
	    #此处的 错误 叫我 排查了 如此长的时间 最后竟然是 xpath表达 不能用双 		引号  只能用单引号  我真是操了 摘抄在这里 
	    #name = node.xpath(".h3/text()").extract()
	    #level = node.xpath(".h4/text()").extract()
	    #info = node.xpath("./p/text()").extract()
	    print(info)
     	item['name'] = name[0]
	    item['level'] = level[0]
	    item['info'] = info[0]
	    yield item
        
