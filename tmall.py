# -*- coding: utf-8 -*-
import csv
import sys
import os
import subprocess
import threading
import queue
from scrapy import cmdline
from tkinter import *
from tkinter.ttk import Treeview
from tkinter.ttk import Progressbar
import random
import time
from PIL import Image, ImageTk

def foo(progressbar,time):
    progressbar.start()
    progressbar['maximum'] = time * 10
    for i in range(time * 100):
        time.sleep(0.01)
        progressbar.step(0.1)
        progressbar.update_idletasks()
    progressbar.stop()

class PopupDialog( Toplevel ):
    def __init__(self, parent):
        Toplevel.__init__( self )
        self.title( 'Settings' )
        self.parent = parent

        SpeedLimitedLabel = Frame( self )
        SpeedLimitedLabel.pack( fill="x", ipadx=1, ipady=1 )
        Label( SpeedLimitedLabel, text='限速：', width=8 ).pack( side=LEFT )
        self.SpeedLimited = IntVar( value=int( self.parent.SpeedLimited ) )
        Entry( SpeedLimitedLabel, textvariable=self.SpeedLimited, width=20 ).pack( side=LEFT )

        rowThreadNum = Frame( self )
        rowThreadNum.pack( fill="x", ipadx=1, ipady=1 )
        Label( rowThreadNum, text='线程数：', width=8 ).pack( side=LEFT )
        self.ThreadNum = IntVar( value=int( self.parent.ThreadNum ) )
        Entry( rowThreadNum, textvariable=self.ThreadNum, width=20 ).pack( side=LEFT )

        # 第二行
        row2 = Frame( self )
        row2.pack( fill="x", ipadx=1, ipady=1 )
        Label( row2, text='延时：', width=8 ).pack( side=LEFT )
        self.DelayTime = IntVar( value=int( self.parent.DelayTime ) )
        Entry( row2, textvariable=self.DelayTime, width=20 ).pack( side=LEFT )

        # 第一行（两列）
        row1 = Frame( self )
        row1.pack( fill="x" )
        Label( row1, text='爬取时间：', width=8 ).pack( side=LEFT )
        self.CrawlTime = IntVar( value=int( self.parent.CrawlTime ) )
        Entry( row1, textvariable=self.CrawlTime, width=20 ).pack( side=LEFT )

        # 第三行
        row3 = Frame( self )
        row3.pack( fill="x" )
        Button( row3, text="取消", command=self.cancel ).pack( side=LEFT )
        Button( row3, text="确定", command=self.ok ).pack( side=RIGHT )

    def cancel(self):
        self.destroy()

    def ok(self):
        # 显式地更改父窗口参数
        self.parent.CrawlTime = self.CrawlTime.get()
        self.parent.DelayTime = self.DelayTime.get()
        self.parent.ThreadNum = self.ThreadNum.get()
        self.parent.SpeedLimited = self.SpeedLimited.get()
        # 显式地更新父窗口界面
        self.parent.crawlTimeLabel.config( text=u"爬取时间：" + str( self.parent.CrawlTime ) )
        self.parent.delayTime.config( text=u"下载延时：" + str( self.parent.DelayTime ) )
        self.parent.threadingNum.config( text=u"线程数：" + str( self.parent.ThreadNum ) )

        # 修改setting.txt
        f = open( "./cralwer/crawls/setting.txt", "w" )
        crawTime_mod_value = self.parent.CrawlTime
        delayTime_mod_value = self.parent.DelayTime
        ThreadNum_mod_value = self.parent.ThreadNum
        modified_value = "CrawTime: " + str( crawTime_mod_value ) + "\nDelay: " + str(
            delayTime_mod_value ) + "\nThread: " + str( ThreadNum_mod_value ) + "\n"
        f.writelines( modified_value )
        f.close()
        self.destroy()


class MyApp( Tk ):
    def __init__(self):
        Tk.__init__( self )
        self.title( 'CSDN-Crawler' )
        self.geometry( '800x650' )

        self.CrawlTime = 20
        self.DelayTime = 1
        self.ThreadNum = 24
        self.SpeedLimited = 200
        self.downloadSpeed = 0
        self.startFlag = 0
        self.setUI()

    def refresh_pb(self):
        self.ProgressBar['value'] += (10 / (self.CrawlTime) * 1.0)
        if self.ProgressBar['value'] >= 99:
            print ("Done")
        else:
            self.after(100,self.refresh_pb)

    def refresh_downloadSpeed(self):
        L = self.SpeedLimited - 100
        if L < 0:
            L = 0
        R = self.SpeedLimited
        self.downloadSpeed = random.randint(L,R)
        self.downloadingSpeed.config(text=u"下载速度：" + str( self.downloadSpeed ) + 'kb / s')
        self.after(1000,self.refresh_downloadSpeed)

    def start_crawl(self):
        file = open( 'info.csv', 'w' )
        line = "标题,作者,日期,浏览量,关键词,链接\n"
        file.write( line )
        file.close()
        path = os.getcwd()
        operation = 'cd ' + path
        os.system( operation + ' && chmod 777 ./startScrapy.sh && ./startScrapy.sh' )
        self.startFlag = 1
        self.after(3300,self.refresh_pb)
        self.after(3300,self.refresh_downloadSpeed)
        # self.spawnthread()

# def stop_progressbar(self):
#     self.progressbar.stop()

# self.after(10000, self.stop_progressbar)

    def stop_crawl(self):
        self.ProgressBar['value'] = 0

    def open_finder(self):
        path = os.getcwd()
        operation = 'cd ' + path
        os.system( operation + ' && chmod 777 ./openFinder.sh && ./openFinder.sh' )

    def returnPrimary(self):
        path = os.getcwd()
        operation = 'cd ' + path
        os.system('return.bat')
        os._exit(0)

    def robo3t(self):
        os.system('robo3t.exe.lnk')


    def setUI(self):
        self.photo = ImageTk.PhotoImage(Image.open('淘宝&天猫.jpg').resize((320,320),Image.ANTIALIAS))
        self.photoLabel = Label( self, image=self.photo, width=320, height=320 )
        # start_button = Button( self, text=u"开始", width=4, height=6, command=self.start_crawl )
        # stop_button = Button( self, text=u"停止", width=4, height=6, command=self.stop_crawl )
        # setting_button = Button( self, text=u"设置", width=4, height=6, command=self.setup_config )
        # directory_button = Button( self, text=u"目录", width=4, height=6, command=self.open_finder )

        start_button = Button(self, text=u"开始", width=7, height=2, command=self.start_crawl,state=ACTIVE)
        stop_button = Button(self, text=u"暂停", width=7, height=2, command=self.stop_crawl,state=ACTIVE)
        setting_button = Button(self, text=u"设置", width=7, height=2, command=self.setup_config,state=ACTIVE)
        directory_button = Button(self, text=u"查询", width=7, height=2,command=self.robo3t,state=ACTIVE)

        returnImg = Image.open('返回.jpg').resize((30, 30), Image.ANTIALIAS)
        self.returnPhoto = ImageTk.PhotoImage(returnImg)

        return_button = Button(self,width=30,height=30,command=self.returnPrimary,image=self.returnPhoto,text = u'返回',state=ACTIVE)
        return_button.place(x=2,y=2)



        # 无需设置修改
        if self.startFlag == 1:
            time.sleep( 1 )
            print( "******" )
            self.downloadSpeed = random.randint( SpeedLimited - 100, SpeedLimited )

        self.downloadingSpeed = Label( self, text=u"下载速度：" + str( self.downloadSpeed ) + 'kb / s')

        # 需要用设置修改
        self.threadingNum = Label( self, text=u"线程数：" + str( self.ThreadNum ) )
        self.delayTime = Label( self, text=u"下载延时：" + str( self.DelayTime ) )
        self.crawlTimeLabel = Label( self, text=u"爬取时间：" + str( self.CrawlTime ) )

        # self.photoLabel.grid( row=0, rowspan=4, pady=20, padx=20 )
        # start_button.grid( row=0, column=1, padx=60 )
        # setting_button.grid( row=2, column=1, padx=60 )
        # stop_button.grid( row=1, column=1, padx=60 )
        # directory_button.grid( row=3, column=1, padx=60 )
        #
        # self.downloadingSpeed.grid( row=0, column=2, padx=60, sticky=W )
        # self.threadingNum.grid( row=1, column=2, padx=60, sticky=W )
        # self.delayTime.grid( row=2, column=2, padx=60, sticky=W )
        # self.crawlTimeLabel.grid( row=3, column=2, padx=60, sticky=W )

        self.photoLabel.place(x=20, y=20)
        start_button.place(x=420, y=65)
        setting_button.place(x=540, y=65)
        stop_button.place(x=420, y=180)
        directory_button.place(x=540, y=180)

        self.downloadingSpeed.place(x=680, y=65)
        self.threadingNum.place(x=680, y=120)
        self.delayTime.place(x=680, y=175)
        self.crawlTimeLabel.place(x=680, y=230)



        bottomFrame = Frame( self, width=80 )
        # bottomFrame.grid( row=5, column=0, columnspan=3, padx=24 )

        bottomFrame.place(x=35, y=390)


        scrollBar = Scrollbar( bottomFrame )
        scrollBar.pack( side=RIGHT, fill=Y )

        # 进度条位置
        self.ProgressBar = Progressbar( self, orient="horizontal", length=320, mode='determinate' )

        # self.ProgressBar.grid( row=4, column=2, columnspan=2, sticky=W + E)
        self.ProgressBar.place(x=400, y=300)

        tree = Treeview( bottomFrame, column=('c1', 'c2', 'c3', 'c4', 'c5', 'c6'), show="headings",
                         yscrollcommand=scrollBar.set )
        tree.column( 'c1', width=220, anchor='center' )
        tree.column( 'c2', width=80, anchor='center' )
        tree.column( 'c3', width=80, anchor='center' )
        tree.column( 'c4', width=80, anchor='center' )
        tree.column( 'c5', width=120, anchor='center' )
        tree.column( 'c6', width=120, anchor='center' )
        # 设置每列表头标题文本
        tree.heading( 'c1', text='标题' )
        tree.heading( 'c2', text='日期' )
        tree.heading( 'c3', text='作者' )
        tree.heading( 'c4', text='浏览量' )
        tree.heading( 'c5', text='关键词' )
        tree.heading( 'c6', text='链接' )

        tree.pack( side=LEFT, fill="both" )

        scrollBar.config( command=tree.yview )

        items = tree.get_children()
        for item in items:
            tree.delete( item )
        # if os.path.exists( 'info.csv' ):
        #     csvfile = open( 'info.csv', 'r' )
        #     if csvfile:
        #         lines = []
        #         reader = csv.reader( csvfile )
        #         i = 0
        #         for line in reader:
        #             # 不读取title
        #             if i > 0:
        #                 lines.append( line )
        #             i = i + 1
        #         print( lines )
        # else:
        #     print ("No file")

    def setup_config(self):
        pw = PopupDialog( self )
        self.wait_window( pw )
        return

class ThreadedClient(threading.Thread):

    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        for x in range(1, 5):
            time.sleep(2)
            msg = "Function %s finished..." % x
            self.queue.put(msg)


if __name__ == '__main__':
    app = MyApp()
    app.resizable( width=False, height=False )
    app.mainloop()
