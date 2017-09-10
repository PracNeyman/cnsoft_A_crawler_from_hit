
# -*- coding: utf-8 -*-
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
from PIL import Image, ImageTk

class MyApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title('Crawler')
        self.geometry('850x650')

        self.setUI()

    def tmall(self):
        os.system('chmod 777 ./goTmall.sh && ./goTmall.sh')
        os._exit(0)

    def tmallANDtaobao(self):
        os.system('chmod 777 ./goTaobaoandtmall.sh && ./goTaobaoandtmall.sh')
        os._exit(0)


    def csdn(self):
        os.system( 'chmod 777 ./goCSDN.sh && ./goCSDN.sh')
        self.destroy()



    def setUI(self):
        img0 = Image.open('标题.png').resize((650, 140), Image.ANTIALIAS)
        self.photo0 = ImageTk.PhotoImage(img0)
        self.photoLabel = Label(self, image=self.photo0, width=650, height=200)
        self.photoLabel.place(x=6,y=3)

        img1 = Image.open('天猫.jpg').resize((200,360),Image.ANTIALIAS)
        self.photo1=ImageTk.PhotoImage(img1)


        img2=Image.open('淘宝&天猫.jpg').resize((200,360),Image.ANTIALIAS)
        self.photo2=ImageTk.PhotoImage(img2)

        img3=Image.open('CSDN.jpg').resize((200,360),Image.ANTIALIAS)
        self.photo3=ImageTk.PhotoImage(img3)

        # self.photoLabel1 = Label(self, image=self.photo1, width=150, height=150)
        # self.photoLabel1.place(x=30,y=100)



        # self.photo = PhotoImage(file='F:\图片\科赫曲线.gif')
        # self.photoLabel = Label(self, image=self.photo, width=320, height=320)
        # start_button = Button(self, text=u"开始", width=7, height=2, command=self.start_crawl)
        # stop_button = Button(self, text=u"暂停", width=7, height=2, command=self.stop_crawl)
        # setting_button = Button(self, text=u"设置", width=7, height=2, command=self.setup_config)
        # directory_button = Button(self, text=u"目录", width=7, height=2)

        tmallButton = Button(self,text=u"天猫（No Scrapy）",width=200,height=360,state=ACTIVE,relief=GROOVE,command=self.tmall,image=self.photo1)
        taobaoButton = Button(self,text=u"淘宝+天猫(Scrapy)",width=200,height=360,state=ACTIVE,relief=GROOVE,command=self.tmallANDtaobao,image=self.photo2)
        csdnButton = Button(self,text=u"CSDN",width=200,height=360,state=ACTIVE,relief=GROOVE,command=self.csdn,image=self.photo3)

        tmallButton.place(x=590,y=200)
        taobaoButton.place(x=310,y=200)
        csdnButton.place(x=30,y=200)


if __name__ == '__main__':
    # os.system('robo3t.exe.lnk')
    app = MyApp()
    app.resizable(width=False, height=False)
    app.mainloop()