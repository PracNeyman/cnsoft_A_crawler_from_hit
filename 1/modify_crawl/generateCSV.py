# -*- coding:utf-8 -*-
import csv
import codecs
import os
goods="手表"
out = open(goods+r'/'+goods+r'.csv', "w", newline="")
myWriter = csv.writer(out, dialect = "excel")
mylist =["商品名", "价格", "产地", "商店名","链接", "同店同种商品数"]
myWriter.writerow(mylist)
p = goods+r'\shops.txt'
t = open(p, 'r',encoding="utf-8")
c = t.readlines()
dict={}
t.close()
for line in c:
    temp, num = line.split()
    dict[temp] = num
root = goods
for root, dirs, files in os.walk(goods):
    for name in files:
        a = os.path.join(root, name)
        path=""
        if (a[-8:-4] == "info"):
            path=a
            text = open(path, 'r',encoding="utf-8")
            content = text.readlines()
            temp=""
            goodName = content[0][9:-1]
            defaultPrice = content[1][13:-1]
            place = content[2][6:-1]
            shopName = content[3][9:-1]
            goodUrl = content[4][8:-1]
            num = 0
            if (shopName in dict):
                num = dict[shopName]
            list = [goodName, defaultPrice, place, shopName, goodUrl, num]
            myWriter.writerow(list)
            text.close()
    for name in dirs:
        a = os.path.join(root, name)
out.close()
