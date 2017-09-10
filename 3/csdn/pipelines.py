# -*- coding: utf-8 -*-
 
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.conf import settings
import pymongo
import sys
import os
reload(sys)
sys.setdefaultencoding("utf-8")

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
        # print ("*********************\n")

        parentFilePath = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

        cloud_path = parentFilePath + "/3/cloud.txt"

        cloud_file = open(cloud_path,"a")

        filepath = ""

        file_buffer = ""

        csv_buffer = ""

        for it in item['title']:
            filepath = it
            fileloc = 'data/' + filepath + '.md'
            fileloc = str(fileloc).replace(" ","_")
            a = open(str(fileloc).decode('utf-8'),'wb')
            file_buffer += ("# " + it + '\n')
            cloud_file.write(str(filepath).decode('utf-8') + "\n")

            # print ("# " + it)

        for it in item['author']:
            file_buffer += ("作者：" + it + '\n')

        for it in item['date']:
            file_buffer += ("日期：" + it + '\n')

        for it in item['count']:
            file_buffer += ("浏览量：" + it + '\n')

        for it in item['jianjie']:
            file_buffer += ("> 简介：" + it + '\n')

        file_buffer += ('\n 链接：' + item['url'] + '\n')
        csv_buffer += (it + item['url'] + "\n")

        print (file_buffer)

        # print (csv_buffer)
        a.write(file_buffer)
        # f.write(csv_buffer)
        
        a.close()

        cloud_file.close()
        # print ("*********************\n")
        return item

# class DuplicatePipeline(object):
#     def __init__(self):
#         self.ids_seen = set()

#     def process_item(self, item, spider):
#         if item['id'] in self.ids_seen:
#             raise DropItem("Duplicate item found: %s" % item)
#         else
#             