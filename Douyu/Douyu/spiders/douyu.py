# -*- coding: utf-8 -*-
import scrapy
import json
from Douyu.items import DouyuItem
class DouyuSpider(scrapy.Spider):
    name = "douyu"
    allowed_domains = ["douyucdn.cn"]
    baseUrl = "http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=208&offset="
    offset = 0
    start_urls = [baseUrl + str(offset),]

    def parse(self, response):
        data_list = json.loads(response.body)['data']
        #在data_list为空的时候 ,return:关闭程序
        if len(data_list) == 0:
            return 
        for data in data_list:
            item = DouyuItem()
            item['nickname'] = data["nickname"]
            item['vertical_src'] = data["vertical_src"]
            yield item
        #offset递增 然后调用回调函数parse() 
        self.offset += 20
        scrapy.Request(self.baseUrl+str(self.offset),callback = self.parse)
