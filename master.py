#! python3
#coding=utf-8
import requests
import re
from redis import Redis
import sys
headers={ 'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36' }


#https://detail.tmall.com/item.htm?&id=537441459334&ns=1&abbucket=10

def get_goods_url(goods):
	r=Redis()
	r.delete('goods_urls')
	r['NUM']=1
	IP="163.125.223.124"		#这是一个有效的的IP，默认就用这个好了
	print(r.keys('*'))
	searchUrl = "https://s.taobao.com/search?s=1&ie=utf-8&q="+goods+"&cd=false&tab=all"
	search_text = requests.get(url=searchUrl,headers=headers).text
	totalPage = int(re.findall(r'"totalPage":(.*?),',search_text)[0])
	for currentPage in range(0,totalPage):
		searchUrl = "https://s.taobao.com/search?s=1&ie=utf-8&q="+goods+"&s="+str(currentPage*44)+"&cd=false&tab=all"
		try:
			search_text = requests.get(url=searchUrl,headers=headers,proxies={"http": "http://"+IP}).text
		except Exception as e:
			print("Not OK")
			IP=r.lpop('IPs')
			continue
		raw_urls = re.findall(r'//detail.tmall.com/item.htm?(.*?),"view_price":',search_text)
		flag = 1
		for raw_url in raw_urls:
			id = re.findall(r'id\\u003d(.*?)\\u',raw_url)[0]
			ns = re.findall(r'\\u0026ns\\u003d(.*?)\\u',raw_url)[0]
			abbucket = re.findall(r'\\u0026abbucket\\u003d(.*?)"',raw_url)[0]
			goods_url = "https://detail.tmall.com/item.htm?&id="+id+"&ns="+ns+"&abbucket="+str(10)
			print(goods_url)
			if flag % 2 == 1:
				flag += 1
				r.rpush('goods_urls',goods_url)
			

if __name__ == '__main__':
	get_goods_url("鼠标")
	#requests.get(url="https://detail.tmall.com/item.htm?&id=551106135353&ns=1&abbucket=10",headers=headers,proxies={"http": "http://172.20.139.246",})
	print("ok")