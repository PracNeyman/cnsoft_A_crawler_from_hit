#! coding=utf-8
import requests
import re
from redis import Redis
headers={ 'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36' }

r=Redis()

IPsrcBasic="http://www.goubanjia.com/free/gngn/index2.shtml"			
r.delete('IPs')
print("获取代理IP")
for i in range(1,5):
	IPsrc=IPsrcBasic+str(i)+"/"
	myweb=requests.get(url=IPsrc)
	print(myweb)
	IPs=re.findall("<td data-title=\"IP\">(.*?)</td>",myweb.text)
	print(IPs)
	usefulIP=[]
	for IP in IPs:
		print (IP)
		try:
			requests.get(url="https://detail.tmall.com/item.htm?&id=551106135353&ns=1&abbucket=10",proxies={"http": "http://"+IP})
			usefulIP.append(IP)
			print("OK")
			r.rpush('IPs',IP)
		except:
			continue
print("获取完毕，有效IP如下")
print(usefulIP)
