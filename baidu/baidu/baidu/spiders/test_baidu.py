# -*- coding: utf-8 -*-
import scrapy


class TestBaiduSpider(scrapy.Spider):
    name = "test_baidu"
    allowed_domains = ["http://www.baidu.com"]
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
	print(response.body)
        pass
