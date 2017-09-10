import scrapy
import requests
from scrapy.http import Request
from taobao_spider.items import TaobaoSpiderItem
import re
from scrapy_redis.spiders import RedisSpider
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

#class TaobaoSpider(scrapy.Spider):
class TaobaoSpider(RedisSpider):
    name = 'taobao'
    # redis_key = 'TaobaoSpider:start_urls'
    allowed_domains = ['taobao.com']
    start_urls = ['http://taobao.com/']
    def parse(self, response):
        key = "taideng"
        pages = 100
        for i in range(0,pages):
            url="http://s.taobao.com/search?q="+key+"&s="+str(44*i)+"&cd=false&tab=all&sort=sale-desc"
            yield Request(url=url,callback=self.page)
        pass

    def page(self, response):
        body = response.body.decode('utf-8','ignore')

        ids = re.compile('"nid":"(.*?)"').findall(body)
        shops=re.compile('"nick":"(.*?)"').findall(body)
        addresses=re.compile('"item_loc":"(.*?)"').findall(body)

        for i in range(0,len(ids)):
            id = ids[i]
           # nowPrice=nowPrices[i]
            shop=shops[i]
            address=addresses[i]
            url = "http://item.taobao.com/item.htm?id="+str(id)
            #yield Request(url=url,callback=self.next,meta={'nowPrice':nowPrice,'address':address,'shop':shop})
            yield Request(url=url, callback=self.next, meta={ 'address': address, 'shop': shop})
            pass
        pass

    def next(self, response):
        item = TaobaoSpiderItem()
        url = response.url
       # print("\n\n\nurl="+url+"\n\n\n")
        web = re.compile("https://(.*?).com").findall(url)
        comment=[]
        if web[0]=='item.taobao':
            title=response.xpath("//h3[@class='tb-main-title']/@data-title").extract()
            originPrice=response.xpath("//em[@class='tb-rmb-num']/text()").extract()
            id = re.compile('id=(.*?)$').findall(url)[0]
            for i in range(1,20):
                commentUrl = 'https://rate.taobao.com/feedRateList.htm?auctionNumId='+id+'&currentPageNum='+str(i)
                tmpComment=re.findall('"content":"(.*?)"',requests.get(commentUrl).text)
                if(len(tmpComment)==0):
                    break
                comment.extend(tmpComment)
            pass
        elif web[0]=='detail.tmall':
            urlText=requests.get(url).text
            #print("\n\nurlText:"+urlText)
            #title=response.xpath("//div[@class='tb-detailed-hd']/h1/text()").extract()
            title=re.findall('<title>(.*?)</title>',urlText)
            originPrice=re.findall('"defaultItemPrice":"(.*?)"',urlText)

            #originPrice=response.xpath("//span[@class='tm-price']/text()").extract()
            id = re.compile('id=(.*?)&').findall(url)[0]
            sellerId=re.findall('",sellerId:"(.*?)"',urlText)[0]
            for i in range(1,20):
                commentUrl = 'https://rate.tmall.com/list_detail_rate.htm?itemId='+id+'&sellerId='+sellerId+'&currentPage='+str(i)
                tmpComment=re.findall('"rateContent":"(.*?)"',requests.get(commentUrl).text)
                if(len(tmpComment)==0):
                    break
                comment.extend(tmpComment)
            pass

        #commentUrl='http://dsr-rate.tmall.com/list_dsr_info.htm?itemId='+str(id)
        #commentData=urllib.request.urlopen(commentUrl).read().decode('utf-8','ignore')
        #comment=re.compile('"count":(.*?)}').findall(commentData)


        item['title']=title
        item['link']=url
        item['shop']=response.meta['shop']
        item['address']=response.meta['address']
        item['originPrice']=originPrice
     #   item['nowPrice']=response.meta['nowPrice']
        item['comment']=comment
        item['id']=id

        yield item
