# -*- coding: utf-8 -*-
import scrapy
from Tencent.items import TencentItem


class TencentSpider(scrapy.Spider):
    name = "tencent"
    allowed_domains = ["tencent.com"]
    #start_urls = (
        #'http://www.tencent.com/',
         #http://hr.tencent.com/position.php?lid=&tid=&keywords=&start=0#a
        #'http://hr.tencent.com/position.php?lid=&tid=&keywords=请输入关键词&start=0#a'
    baseUrl = 'http://hr.tencent.com/position.php?lid=&tid=&keywords=请输入关键词&start='
    offset = 0
    start_urls = [
        baseUrl + str(offset)
    ]

    def parse(self, response):
        node_list = response.xpath('//tr[@class="even"] | //tr[@class="odd"]')
 
        for node in node_list:
            item = TencentItem() 
            #xpath数组下表 从一开始
            print(len(node_list))
            print("真在获取页面。。。。。。")
            item['positionName'] = node.xpath('./td[1]/a/text()').extract()[0].encode('utf-8')
            item['positionLink'] = node.xpath('./td[1]/a/@href').extract()[0].encode('utf-8')
            if len(node.xpath('./td[2]/text()')):
                item['positionType'] = node.xpath('./td[2]/text()').extract()[0].encode('utf-8')
            else:
                item['positionType'] = "".encode('utf-8')

            item['peopleNumber'] = node.xpath('./td[3]/text()').extract()[0].encode('utf-8')
            item['workLocation'] = node.xpath('./td[4]/text()').extract()[0].encode('utf-8')
            item['publishTime'] = node.xpath('./td[5]/text()').extract()[0].encode('utf-8')
            print(node.xpath('./td[5]/text()').extract()[0].encode('utf-8'))
            yield item

        #self.offset = 10
        '''
        if self.offset < 200:
            self.offset += 10
            url = self.baseUrl + str(self.offset)
            yield scrapy.Request(url, callback = self.parse)
        '''
        #另一中方法不断 提取下一页的链接 
        if len(response.xpath('//a[@class="noactive" and @id="next"]')) == 0:
            url = response.xpath('//a[@id="next"]/@href').extract()[0]
            yield scrapy.Request("http://hr.tencent.com/" + url,callback = self.parse)


