#-*- coding: utf-8 -*-
import csv
import sys
import os
import subprocess
import threading
from scrapy import cmdline
from tkinter import *
from tkinter.ttk import Treeview
from tkinter.ttk import Progressbar
import random
import time

# reload(sys)
# sys.setdefaultencoding("utf-8")
# class crawler_Gui:

#     def __init__(self,master):
#         # l = Label(root, text = "welcome", font = ('Monospace',15), width = 15, height = 2)
#         # l.grid(row = 0,column = 1)
#         photo = PhotoImage(file = '/Users/luodian/Desktop/Free-Converter.com--9v3zzly-82891714.gif')
#         photoLabel = Label(master,image = photo)
#         photoLabel.pack()


# class DownLoader(threading.Thread):
#     def __init__(self, *args, **kwargs):
# 		# self.setDaemon(True)
# 		super(DownLoader, self).__init__(*args, **kwargs)
# 		self.__flag = threading.Event()     # 用于暂停线程的标识
# 		self.__flag.set()       # 设置为True
# 		self.__running = threading.Event()      # 用于停止线程的标识
# 		self.__running.set()      # 将running设置为True

#     def run(self):
#         while self.__running.isSet():
#             self.__flag.wait()      # 为True时立即返回, 为False时阻塞直到内部的标识位为True后返回
#             print "*************"

#     def pause(self):
#         self.__flag.clear()     # 设置为False, 让线程阻塞

#     def resume(self):
#         self.__flag.set()    # 设置为True, 让线程停止阻塞

#     def stop(self):
#         self.__flag.set()       # 将线程从暂停状态恢复, 如何已经暂停的话
#         self.__running.clear()        # 设置为False    

# download_thread = DownLoader()

# def background_thread(threadName,delay):
# 	path = os.getcwd()
# 	operation = 'cd ' + path
# 	# print operation
# 	# cmdline.execute("scrapy crawl csdnblog".split())
# 	# subprocess.call('scrapy','crawl','csdnblog')
# 	# returncode = subprocess.call(['cd','/Users/luodian/PycharmProjects/csdn-crawler/crawler','scrapy','crawl','csdnblog'],shell=True)
# 	# os.system('start.py')
# 	os.system(operation + ' && chmod 777 ./st.sh && ./st.sh')


class PopupDialog(Toplevel):
	def __init__(self,parent):
		Toplevel.__init__(self)
		self.title('Settings')
		self.parent = parent

		SpeedLimitedLabel = Frame(self)
		SpeedLimitedLabel.pack(fill="x", ipadx=1, ipady=1)
		Label(SpeedLimitedLabel, text = '限速：', width = 8).pack(side=LEFT)
		self.SpeedLimited = IntVar(value = int(self.parent.SpeedLimited))
		Entry(SpeedLimitedLabel, textvariable=self.SpeedLimited, width=20).pack(side=LEFT)

		rowThreadNum = Frame(self)
		rowThreadNum.pack(fill="x", ipadx=1, ipady=1)
		Label(rowThreadNum, text = '线程数：', width = 8).pack(side=LEFT)
		self.ThreadNum = IntVar(value = int(self.parent.ThreadNum))
		Entry(rowThreadNum, textvariable=self.ThreadNum, width=20).pack(side=LEFT)

		# 第二行
		row2 = Frame(self)
		row2.pack(fill="x", ipadx=1, ipady=1)
		Label(row2, text = '延时：', width = 8).pack(side=LEFT)
		self.DelayTime = IntVar(value = int(self.parent.DelayTime))
		Entry(row2, textvariable=self.DelayTime, width=20).pack(side=LEFT)

		# 第一行（两列）
		row1 = Frame(self)
		row1.pack(fill="x")
		Label(row1, text = '爬取时间：', width=8).pack(side=LEFT)
		self.CrawlTime = IntVar(value = int(self.parent.CrawlTime))
		Entry(row1, textvariable=self.CrawlTime, width = 20).pack(side=LEFT)

		# 第三行
		row3 = Frame(self)
		row3.pack(fill="x")
		Button(row3, text="取消", command=self.cancel).pack(side = LEFT)
		Button(row3, text="确定", command=self.ok).pack(side = RIGHT)

	def cancel(self):
		self.destroy()

	def ok(self):
		# 显式地更改父窗口参数
		self.parent.CrawlTime = self.CrawlTime.get()
		self.parent.DelayTime = self.DelayTime.get()
		self.parent.ThreadNum = self.ThreadNum.get()
		self.parent.SpeedLimited = self.SpeedLimited.get()
		# 显式地更新父窗口界面
		self.parent.crawlTimeLabel.config(text= u"爬取时间：" + str(self.parent.CrawlTime))
		self.parent.delayTime.config(text = u"下载延时：" + str(self.parent.DelayTime))
		self.parent.threadingNum.config(text= u"线程数：" + str(self.parent.ThreadNum))
		self.destroy()

class MyApp(Tk):
	def __init__(self):
		Tk.__init__(self)
		self.title('CSDN-Crawler')
		self.geometry('800x650')

		self.CrawlTime = 20
		self.DelayTime = 1
		self.ThreadNum = 12
		self.SpeedLimited = 200
		self.downloadSpeed = 0
		self.startFlag = 0
		self.setUI()

	def start_crawl(self):
		file = open('info.csv','w')
		file.close()
		path = os.getcwd()
		operation = 'cd ' + path
		os.system(operation + ' && chmod 777 ./st.sh && ./st.sh')
		self.startFlag = 1
		self.ProgressBar["value"] = 0
		self.ProgressBar["maximum"] = 500
		increment = 500 / CrawlTime
		for i in range(0,self.CrawlTime):
			time.sleep(1)
			self.ProgressBar.step(increment)

	def stop_crawl(self):
		pass

	def setUI(self):
		self.photo = PhotoImage(file = '/Users/luodian/Desktop/Free-Converter.com--9v3zzly-82891714.gif')
		self.photoLabel = Label(self,image = self.photo,width = 320,height = 320)
		start_button = Button(self,text = u"开始",width = 4,height = 6,command = self.start_crawl)
		stop_button = Button(self,text = u"暂停",width = 4,height = 6,command = self.stop_crawl)
		setting_button = Button(self,text = u"设置",width = 4,height = 6,command = self.setup_config)
		directory_button = Button(self,text = u"目录",width = 4,height = 6)


		# 无需设置修改
		if self.startFlag == 1:
			time.sleep(1)
			print ("******")
			self.downloadSpeed = random.randint(SpeedLimited-100,SpeedLimited)

		self.downloadingSpeed = Label(self,text = u"下载速度：" + str(self.downloadSpeed))

		# 需要用设置修改
		self.threadingNum = Label(self,text = u"线程数：" + str(self.ThreadNum))
		self.delayTime = Label(self,text = u"下载延时：" + str(self.DelayTime))
		self.crawlTimeLabel = Label(self,text = u"爬取时间：" + str(self.CrawlTime))

		self.photoLabel.grid(row = 0,rowspan = 4,pady = 20, padx = 20)
		start_button.grid(row = 0,column = 1,padx = 60)
		setting_button.grid(row = 2,column = 1,padx = 60)
		stop_button.grid(row = 1,column = 1,padx = 60)
		directory_button.grid(row = 3,column = 1,padx = 60)

		self.downloadingSpeed.grid(row = 0, column = 2,padx = 60,sticky = W)
		self.threadingNum.grid(row = 1,column = 2,padx = 60,sticky = W)
		self.delayTime.grid(row = 2,column = 2,padx = 60,sticky = W)
		self.crawlTimeLabel.grid(row = 3,column = 2,padx = 60,sticky = W)


		bottomFrame = Frame(self,width = 80)
		bottomFrame.grid(row = 5,column = 0, columnspan = 3,padx = 24)
		scrollBar = Scrollbar(bottomFrame)
		scrollBar.pack(side  = RIGHT,fill = Y)

		# 进度条位置
		self.ProgressBar = Progressbar(self, orient = "horizontal", length = 200, mode = 'determinate')
		self.ProgressBar.grid(row = 4,column = 2,columnspan = 2,sticky = W + E)
		tree = Treeview(bottomFrame,column = ('c1','c2','c3','c4','c5','c6'),show = "headings",yscrollcommand = scrollBar.set)
		tree.column('c1', width=220, anchor='center')
		tree.column('c2', width=80, anchor='center')
		tree.column('c3', width=80, anchor='center')
		tree.column('c4', width=80, anchor='center')
		tree.column('c5', width=120, anchor='center')
		tree.column('c6', width=120, anchor='center')
		#设置每列表头标题文本
		tree.heading('c1', text='标题')
		tree.heading('c2', text='日期')
		tree.heading('c3', text='作者')
		tree.heading('c4', text='浏览量')
		tree.heading('c5', text='关键词')
		tree.heading('c6', text='链接')

		tree.pack(side = LEFT, fill = "both")

		scrollBar.config(command=tree.yview)

		items = tree.get_children()
		for item in items:
			tree.delete(item)
		if os.path.exists('info.csv'):
			csvfile = open('info.csv','rb')
			if csvfile:
				lines = []
				reader = csv.reader(csvfile)
				i = 0
				for line in reader:
					# 不读取title
					if i > 0:
						lines.append(line)
					i = i + 1
				print (lines)
	
	def setup_config(self):
		pw = PopupDialog(self)
		self.wait_window(pw)
		return

def GUI():
	root = Tk()
	root.title('CSDN-Crawler')
	root.geometry('800x650')
	root.resizable(width = False,height = False)
	root.mainloop()

if __name__ == '__main__':
	app = MyApp()
	app.resizable(width = False,height = False)
	app.mainloop()