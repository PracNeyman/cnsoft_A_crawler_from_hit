# -*- coding: utf8-*-
import re
import requests

#print requests.get("https://s.taobao.com/search?s=1&s=4136&ie=utf-8&q=%E6%89%8B%E8%A1%A8&cd=false&tab=all&sort=sale-desc&bcoffset=-276&ntoffset=-276").text

searchUrl = "https://s.taobao.com/search?s=1&ie=utf-8&q=%E6%89%8B%E8%A1%A8&cd=false&tab=all&sort=sale-des"
search_text=requests.get(url=searchUrl).text
totalPage=int(re.findall(r'"totalPage":(.*?),',search_text)[0])
print totalPage
for currentPage in range(0,3):
    eachPageUrl="https://s.taobao.com/search?s=1&ie=utf-8&q=手表&s="+str(currentPage*44)+"&cd=false&tab=all&sort=sale-desc"
    #print eachPageUrl
    #print requests.get(eachPageUrl).text
    tmpShops=re.findall(r'"nick":"(.*?)","shopcard"',search_text)
    for shop in tmpShops:
        print shop
    raw_urls=re.findall(r'//detail.tmall.com/item.htm?(.*?),"view_price":',search_text)
    beforeUrl='abcdefg'
    for raw_url in raw_urls:
        id=re.findall(r'id\\u003d(.*?)\\u',raw_url)[0]
        #print id
        ns=re.findall(r'\\u0026ns\\u003d(.*?)\\u',raw_url)[0]
        #print ns
        abbucket=re.findall(r'\\u0026abbucket\\u003d(.*?)"',raw_url)[0]
        goodsUrl="http://detail.tmall.com/item.htm?&id="+id+"&ns="+ns+"&abbucket="+abbucket
        if beforeUrl in goodsUrl:
            continue
        else:
            print goodsUrl
            beforeUrl=goodsUrl
