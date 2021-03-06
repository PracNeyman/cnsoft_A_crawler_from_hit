# -*- coding: utf-8 -*-
import requests
import re
from redis import Redis
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from wordcloud import WordCloud,ImageColorGenerator,STOPWORDS
import jieba
import numpy as np
import chardet
from PIL import Image
import sys
headers={ 'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36' }


#goods=sys.argv[1]
goods="手表"

MaxErrorTimes=5
IP="211.140.151.220"

def wordCloud(path):
	#读取要生成词云的文件
	file = open(path + u"\\rate.txt")
	line = file.readline()
	space_split = ""
	while line:
		wordlist_after_jieba = jieba.cut(line, cut_all=True)
		wl_space_split = " ".join(wordlist_after_jieba)
		space_split += " "
		space_split += wl_space_split
		line = file.readline()
	my_wordcloud = WordCloud(background_color='white', font_path=u"C:\\Windows\\Fonts\\STHUPO.TTF").generate(
		space_split)
	plt.figure(figsize=(10, 8), dpi=600)
	plt.imshow(my_wordcloud)
	plt.axis("off")
	plt.savefig(path + "/wordCloud.png", dpi=600)
	file.close()
	plt.close('all')

# def wordCloud(Path):
# 	#读取要生成词云的文件
# 	text_from_file_with_apath = open(Path+"/rate.txt").read()
#
# 	wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all = True)
# 	wl_space_split = " ".join(wordlist_after_jieba)
# 	my_wordcloud = WordCloud(background_color='white',font_path='C:\Windows\Fonts\simkai.ttf').generate(wl_space_split)
#
# 	# 以下代码显示图片
# 	plt.figure(figsize = (10,8),dpi = 600)
# 	plt.imshow(my_wordcloud)
# 	plt.axis("off")
# 	plt.savefig(Path+"/wordCloud.png",dpi = 600)
# 	#plt.close('all')

def crawl_tianMao(IP):
	#good_url="https://detail.tmall.com/item.htm?spm=a230r.1.14.6.4bRmel&id=537441459334&cm_id=140105335569ed55e27b&abbucket=10"
	r=Redis()
	if r.exists('goods_urls')==False:
		print("over!")
		exit(0)
	good_url=r.lpop('goods_urls')
	print(good_url)
	try:
		text=requests.get(url=good_url,headers=headers,proxies={"http": "http://"+IP}).text
	except Exception as e:
		if r.exists('goods_urls')==False:
			print("over!")
			exit(0)
		else:
			IP=r.lpop('IPs')
	shopName=re.findall(r'<input type="hidden" name="seller_nickname" value="(.*?)" />',text)[0]
	goodName=re.findall(r'<input type="hidden" name="title" value="(.*?)" />',text)[0]
	defaultPrice=re.findall(r'"defaultItemPrice":"(.*?)"',text)[0]
	place=re.findall(r'<input type="hidden" name="region" value="(.*?)" />',text)[0]
	r['NUM']=int(r['NUM'])+1
	print(goodName)
	try:
		what="./"+goods+"/"+goodName
		os.mkdir(what)
	except:
		print("ok")
		exit(0)
	infoText=open("./"+goods+"/"+goodName+"/"+"info.txt",'w')
	infoText.write("goodName "+goodName+"\n")
	infoText.write("defaultPrice "+defaultPrice+'\n')
	infoText.write("place "+place+'\n')
	infoText.write("shopName "+shopName+'\n')
	infoText.write("goodUrl "+good_url.decode('ascii')+'\n')
	infoText.close()
	Ids=re.findall(r'w.g_config={(.*?)}',text)[0]
	itemId=re.findall(r'itemId:"(.*?)"',Ids)[0]
	sellerId=re.findall(r'sellerId:"(.*?)"',Ids)[0]

	errorTime=0
	output=open("./"+goods+"/"+goodName+"/rate.txt",'w')
	
	for currentPage in range(1,200):
		try:
			rateUrl="https://rate.tmall.com/list_detail_rate.htm?itemId="+itemId+"&sellerId="+sellerId+"&currentPage="+(str)(currentPage)
			print(rateUrl)
			try:
				myweb=requests.get(url=rateUrl,headers=headers,proxies={"http": "http://"+IP})
			except Exception as e:
				IP=r.lpop('IPs')
				continue
			rates=re.findall(r'"rateContent":"(.*?)"',myweb.text)
			if len(rates)==0:
				print("NO Content")
				errorTime+=1
			for rate in rates:
				print(rate)
				output.write(rate)
				output.write('\n')
			try:
				if(currentPage==int(re.findall(r'"lastPage":(.*?),',myweb.text)[0])):
					print("到达评论最后一页")
					break
			except Exception as e:
				continue
		except Exception as e:
			print(e)
			errorTime+=1
			continue
		if errorTime==MaxErrorTimes:
			break
	output.close()
	wordCloud("./"+goods+"/"+goodName)
	crawl_tianMao(IP)

if __name__ == '__main__':
	print("slaver爬取每一个商品")
	r=Redis()
	r['NUM']=0
	crawl_tianMao(IP)
	#https://rate.tmall.com/list_detail_rate.htm?itemId=539974531928&sellerId=1926988776&currentPage=1
	#text=requests.get(url="https://rate.tmall.com/list_detail_rate.htm?itemId=539974531928&sellerId=1926988776&currentPage=1",headers=headers).text
	#rate=re.findall(r'"rateContent":"(.*?)"',text)[0]
	#print(rate)
	#fout=open("testascii.txt",'a')
	#fout.write(rate)
