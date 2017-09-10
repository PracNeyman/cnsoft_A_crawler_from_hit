# -*- coding: utf8-*-
import requests
import re
from redis import Redis
import sys
import os
headers={ 'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36' }


def get_goods_url(goods):
	print(("爬取的商品为"+goods))
	shops=[]
	if not os.path.exists(goods):
		os.mkdir("./"+goods)
	r=Redis()
	r['NUM']=int(0)
	r.delete('goods_urls')
	IP="163.125.223.124"		#这是一个有效的的IP，初始就用这个好了
	searchUrl="https://s.taobao.com/search?s=1&ie=utf-8&q="+goods+"&cd=false&tab=all&sort=sale-desc"
	search_text=requests.get(url=searchUrl,headers=headers).text
	totalPage=int(re.findall(r'"totalPage":(.*?),',search_text)[0])
	for currentPage in range(0,totalPage):
		#print("totalPage"+str(totalPage))
		eachPageUrl="https://s.taobao.com/search?s=1&ie=utf-8&q="+goods+"&s="+str(currentPage*44)+"&cd=false&tab=all&sort=sale-desc"
		try:
			search_text=requests.get(url=eachPageUrl,headers=headers,proxies={"http": "http://"+IP}).text
		except Exception as e:
			print("Not OK")
			IP=r.lpop('IPs')
			continue
		tmpShops=(re.findall(r'"nick":"(.*?)","shopcard"',search_text))
		for shop in tmpShops:
			shops.append(shop)
		raw_urls=re.findall(r'//detail.tmall.com/item.htm?(.*?),"view_price":',search_text)
		before_url='abcdefg'
		for raw_url in raw_urls:
			id=re.findall(r'id\\u003d(.*?)\\u',raw_url)[0]
			ns=re.findall(r'\\u0026ns\\u003d(.*?)\\u',raw_url)[0]
			abbucket=re.findall(r'\\u0026abbucket\\u003d(.*?)"',raw_url)[0]
			goods_url="https://detail.tmall.com/item.htm?&id="+id+"&ns="+ns+"&abbucket="+abbucket
			if before_url in goods_url:
				continue
			else:
				print(goods_url)
				before_url=goods_url
				r.rpush('goods_urls',goods_url)
	shopsFile=open("./"+goods+"/shops.txt",'a')
	for shop in shops:
		shopsFile.write(shop+" "+str(shops.count(shop))+'\n')
		shops.remove(shop)

if __name__ == '__main__':
	print("master获取商品链接及店铺信息")
	get_goods_url("手表")
	#get_goods_url("水杯")
	#requests.get(url="https://detail.tmall.com/item.htm?&id=551106135353&ns=1&abbucket=10",headers=headers,proxies={"http": "http://172.20.139.246",})
	print("ok")
