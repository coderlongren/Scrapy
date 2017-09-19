# -*- coding: utf-8 -*-
import scrapy


class RentSpider(scrapy.Spider):
    name = "rent"
    allowed_domains = ["http://3g.ganjin.com"]
    start_urls = (
        'http://www.http://3g.ganjin.com/',
    )

    def parse(self, response):
        item = MyrentItem()
        print(response.body)
        #item_list = response.xpath()
        pass
