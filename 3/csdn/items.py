# -*- coding: utf-8 -*-
 
# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
 
import scrapy
import sys
import os
reload(sys)
sys.setdefaultencoding("utf-8")
 
class CsdnItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    url = scrapy.Field()
    count = scrapy.Field()
    content = scrapy.Field()
    cete = scrapy.Field()
    jianjie = scrapy.Field()
    date = scrapy.Field()