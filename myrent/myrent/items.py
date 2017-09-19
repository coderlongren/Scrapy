# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyrentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #赶集网的id信息
    id = scrapy.Field()
    #链接信息
    link = scrapy.Field()
    #文章的链接
    title = scrapy.Field()
    drwxrwxr-x
