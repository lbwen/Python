#coding:utf-8
import time
import os
from selenium import webdriver

while True:
    time_now = time.strftime("%H:%M:%S", time.localtime())  # 刷新
    if time_now == "11:20:20":  # 此处设置每天定时的时间
        # os.system("kill task sometask")
        path = r'E:\Program Files\Microvirt\MEmu\MEmu.exe'  # 打开模拟器
        os.startfile(path)
        time.sleep(50)

import time
while True:
    time_now = time.strftime("%H:%M:%S", time.localtime())  # 刷新
    if time_now == "11:14:10":  # 此处设置每天定时的时间
        driver = webdriver.Firefox()
        driver.maximize_window()  # 最大化浏览器窗口
        driver.get(r"http://dev.shidonghui.cn/sdhui/static/wr/newOam/login.html")
        time.sleep(2)

import time
while True:
    time_now = time.strftime("%S", time.localtime())  # 刷新
    if time_now == "10":  # 此处设置每天定时的时间
        # 此处3行替换为需要执行的动作
        print("hello")
        subject = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " 定时发送测试"
        print(subject)
        time.sleep(2)  # 因为以秒定时，所以暂停2秒，使之不会在1秒内执行多次