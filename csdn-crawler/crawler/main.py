#-*- coding: utf-8 -*-
import csv
import os
import subprocess
import threading
from scrapy import cmdline
from tkinter import *
from tkinter.ttk import Treeview

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

def start_crawl():
	file = open('info.csv','w')
	file.close()
	path = os.getcwd()
	operation = 'cd ' + path
	# subprocess.Popen([sys.executable, 'start.py'], creationflags = subprocess.CREATE_NEW_CONSOLE) avaiable in windows
	subprocess.Popen([sys.executable,'start.py'], shell = False)
	
def stop_crawl():
	pass

def GUI():
	root = Tk()

	root.title('CSDN-Crawler')
	root.geometry('800x650')

	photo = PhotoImage(file = '/Users/luodian/Desktop/Free-Converter.com--9v3zzly-82891714.gif')

	photoLabel = Label(root,image = photo,width = 320,height = 320)

	start_button = Button(root,text = u"开始",width = 4,height = 6,command = start_crawl)

	stop_button = Button(root,text = u"暂停",width = 4,height = 6,command = stop_crawl)

	setting_button = Button(root,text = u"设置",width = 4,height = 6)

	directory_button = Button(root,text = u"目录",width = 4,height = 6)

	downloadingSpeed = Label(root,text = u"下载速度：")

	threadingNum = Label(root,text = u"线程数：")

	delayTime = Label(root,text = u"延迟：")

	photoLabel.grid(row = 0,rowspan = 4,pady = 20, padx = 20)
	start_button.grid(row = 0,column = 1,padx = 60)
	setting_button.grid(row = 1,column = 1,padx = 60)
	stop_button.grid(row = 2,column = 1,padx = 60)
	directory_button.grid(row = 3,column = 1,padx = 60)

	downloadingSpeed.grid(row = 0, column = 2,padx = 60)
	threadingNum.grid(row = 1,column = 2,padx = 60)
	delayTime.grid(row = 2,column = 2,padx = 60)

	bottomFrame = Frame(root,width = 80)
	bottomFrame.grid(row = 4,column = 0, columnspan = 3,padx = 24)
	scrollBar = Scrollbar(bottomFrame)
	scrollBar.pack(side  = RIGHT,fill = Y)

	# listBox = Listbox(bottomFrame,yscrollcommand = scrollBar.set,width = 80,height = 12,relief = RIDGE)

	# for i in range(1000):
	# 	listBox.insert(END,str(i))

	# listBox.pack()
	# scrollBar.config(command = listBox.yview)

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
	#插入演示数据

	# for i in range(100):
	#     tree.insert('', i, values=[str(i)]*6)

	root.resizable(width = False,height = False)
	root.mainloop()

if __name__ == '__main__':
	GUI();