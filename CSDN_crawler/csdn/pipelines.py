# -*- coding: utf-8 -*-
 
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.conf import settings
import pymongo

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class CsdnPipeline(object):
    def __init__(self):
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        dbName = settings['MONGODB_DBNAME']
        client = pymongo.MongoClient(host=host,port=port)
        tdb = client[dbName]
        self.post = tdb[settings['MONGODB_DOCNAME']]
    def process_item(self, item, spider):
        csdnblog = dict(item)
        self.post.insert(csdnblog)
        print ("*********************\n")

        filepath = ""

        file_buffer = ""

        for it in item['title']:
            filepath = it
            a = open("/Users/luodian/Desktop/csdn/data/" + filepath + '.md','w')
            file_buffer += ("# " + it + '\n')

        for it in item['author']:
            file_buffer += ("作者：" + it + '\n')

        for it in item['date']:
            file_buffer += ("日期：" + it + '\n')

        for it in item['count']:
            file_buffer += ("浏览量：" + it + '\n')

        for it in item['jianjie']:
            file_buffer += ("> 简介：" + it + '\n')

        
        file_buffer += ('\n 链接：' + item['url'][1:] + '\n')
        item['url'] = item['url'][1:]
        print (file_buffer)
        a.write(file_buffer)
        a.close()
        print ("*********************\n")
        return item