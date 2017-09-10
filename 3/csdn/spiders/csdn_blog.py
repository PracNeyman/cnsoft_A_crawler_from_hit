# -*- coding: utf-8 -*-
import scrapy
from csdn.items import CsdnItem
import sys
import os
reload(sys)
sys.setdefaultencoding("utf-8")
 
class CsdnblogSpider(scrapy.Spider):
    name = "csdnblog"
    allowed_domains = ["csdn.net"]
    start_urls = ['http://blog.csdn.net']
 
    def parse(self, response):
        for  eveUrl in response.xpath('//dl[@class="blog_list clearfix"]'):
            fullUrl = eveUrl.xpath('dd/h3/a/@href').extract()
            url = str(fullUrl).replace('\'', '').replace('[', '').replace(']', '')
            title = eveUrl.xpath('dd/h3/a/text()').extract()
            jianjie = eveUrl.xpath('dd/div[1]/text()').extract()
            cete = eveUrl.xpath('dd/div[2]/div[1]/span/a/text()').extract()
            date = eveUrl.xpath('dd/div[2]/div[2]/label/text()').extract()
            count = eveUrl.xpath('dd/div[2]/div[2]/span/em/text()').extract()
            author = eveUrl.xpath('dt/a[2]/text()').extract()
            ans = {'url':url,'jianjie':jianjie,'cete':cete,'date':date,'count':count,'author':author,'title':title}
            full_url = response.urljoin(url)
            full_url = full_url[1:]
            # print (full_url)
            yield scrapy.Request(url[1:],self.parse_content,meta=ans)
#             ,meta=ans
         
         
        for pageCount in range(2,248):
            nextUrl = "http://blog.csdn.net/?&page=" + str(pageCount)
            yield scrapy.Request(nextUrl,self.parse)
             
    def parse_content(self, response):
        content = response.xpath('//div[@class="markdown_views"]').extract()
        item = CsdnItem()
        item['url'] = response.meta['url'][1:]
        item['jianjie'] = response.meta['jianjie']
        item['cete'] = response.meta['cete']
        item['date'] = response.meta['date']
        item['count'] = response.meta['count']
        item['author'] = response.meta['author']
        item['title'] = response.meta['title']
        item['content'] = content
        yield item