#! python3
# -*- coding: utf-8 -*-
import requests
import re
from redis import Redis
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
headers={ 'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36' }

MaxErrorTimes=5
IP="211.140.151.220"

def crawl_tianMao(IP):
	#goods_url="https://detail.tmall.com/item.htm?spm=a230r.1.14.6.4bRmel&id=537441459334&cm_id=140105335569ed55e27b&abbucket=10"
	r=Redis()
	print(r.keys('*'))
	if r.exists('goods_urls') == False:
			print("over!")
			exit(0)
	goods_url=r.lpop('goods_urls')
	try:
		text = requests.get(url=goods_url,headers=headers,proxies={"http": "http://"+IP}).text
		#print("到了")
		#text=unicode(text,'GBK').encode('UTF-8')
		#print("这里可以啊")
	except Exception as e:
		if r.exists('goods_urls')==False:
			print("over!")
			exit(0)
		else:
			IP = r.lpop('IPs')
	Ids = re.findall(r'w.g_config={(.*?)}',text)[0]
	itemId = re.findall(r'itemId:"(.*?)"',Ids)[0]
	sellerId = re.findall(r'sellerId:"(.*?)"',Ids)[0]

	errorTime = 0
	NUM = int(r['NUM'])
	output = open(str(NUM)+".txt",'w')
	r['NUM'] = NUM + 1
	
	for currentPage in range(1,200):
		try:
			rateUrl="https://rate.tmall.com/list_detail_rate.htm?itemId="+itemId+"&sellerId="+sellerId+"&currentPage="+(str)(currentPage)
			print(rateUrl)
			try:
				myweb = requests.get(url=rateUrl,headers=headers,proxies={"http": "http://"+IP})
			except Exception as e:
				IP = r.lpop('IPs')
				continue
			rates = re.findall(r'"rateContent":"(.*?)"',myweb.text)
			if len(rates) == 0:
				print("NO Content")
				errorTime += 1
			for rate in rates:
				print(rate)
				output.write(rate)
				output.write('\n')
			try:
				if(currentPage == int(re.findall(r'"lastPage":(.*?),',myweb.text)[0])):
					print("到达评论最后一页")
					break
			except Exception as e:
				continue
		except Exception as e:
			print(e)
			errorTime += 1
			continue
		if errorTime == MaxErrorTimes:
			break
	output.close()
	crawl_tianMao(IP)

if __name__ == '__main__':
	crawl_tianMao(IP)
	#https://rate.tmall.com/list_detail_rate.htm?itemId=539974531928&sellerId=1926988776&currentPage=1
	#text=requests.get(url="https://rate.tmall.com/list_detail_rate.htm?itemId=539974531928&sellerId=1926988776&currentPage=1",headers=headers).text
	#rate=re.findall(r'"rateContent":"(.*?)"',text)[0]
	#print(rate)
	#fout=open("testascii.txt",'a')
	#fout.write(rate)