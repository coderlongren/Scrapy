# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
#from scrapy.contrib.pipeline.images import ImagesPipeline
#from pipelines.images import ImagesPipeline
import scrapy
from scrapy.pipelines.images import ImagesPipeline
import hashlib
import six

class DouyuPipeline(ImagesPipeline):
    def get_media_requests(self,item,info):
        vertical_src = item['vertical_src']
        yield scrapy.Request(vertical_src)

    # def item_
