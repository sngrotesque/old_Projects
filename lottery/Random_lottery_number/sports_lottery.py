#-*- coding:utf-8 -*-
import os
import time
import random

print("现在的时间是: "+time.strftime("%Y-%m-%d - %H:%M:%S", time.localtime()))

print("(超级大乐透)你需要出几注号码？请输入: ",end="")
touzhushu=int(input())

os.system("clear")
def demo1():

    list_red = [x for x in range(1, 36)]            #1-35红球
    list_blue = [x for x in range(1, 13)]          #1-12蓝球

    res_red = random.sample(list_red, 5)       #随机选择5个红球
    res_blue = random.sample(list_blue, 2)   #随机选择2个蓝球

    res_red.sort()          #排序
    res_blue.sort()        #排序

    res_=res_red+res_blue
    res=str(res_)

    print("号码为: ",res)
    file=open("cp0912.txt","a+")
    file.write(res+"\n")
    file.close()
a=0
while a<touzhushu:
    demo1()
    a=a+1
