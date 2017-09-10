# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

class TaobaoSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    originPrice = scrapy.Field()
    #nowPrice = scrapy.Field()
    comment = scrapy.Field()
    shop = scrapy.Field()
    address = scrapy.Field()
    id = scrapy.Field()
    pass

# class TaobaoSpiderLoader(ItemLoader):
#     default_item_class = TaobaoSpiderItem
#     default_input_processor = MapCompose(lambda s: s.strip())
#     default_output_processor = TakeFirst()
#     description_out = Join()


