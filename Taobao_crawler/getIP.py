#! python 3

import requests
import re
from redis import Redis
headers={ 'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36' }

r=Redis()

IPsrcBasic="http://www.kuaidaili.com/free/inha/"			

for i in range(1,10):
	IPsrc=IPsrcBasic+str(i)+"/"
	myweb=requests.get(url=IPsrc,headers=headers)
	IPs=re.findall("<td data-title=\"IP\">(.*?)</td>",myweb.text)
	usefulIP=[]
	for IP in IPs:
		print (IP)
		try:
			requests.get(url="https://detail.tmall.com/item.htm?&id=551106135353&ns=1&abbucket=10",headers=headers,proxies={"http": "http://"+IP})
			usefulIP.append(IP)
			print("OK")
			r.rpush('IPs',IP)
		except:
			continue
print(usefulIP)
