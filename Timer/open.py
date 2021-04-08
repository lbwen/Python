#coding:utf-8
import os
import time
from selenium import webdriver
path = r'E:\Program Files\Microvirt\MEmu\MEmu.exe'
os.startfile(path)
time.sleep(50)

capabilities = {
    "platformName" : "Android",
    "deviceName" : "127.0.0.1:21503",
    "app" : "E:\\apk\\shidonghui.apk",
    # "appWaitActivity": "cn.com.open.mooc.user.register.MCPhoneRegisterAty",
    "noReset": "true"
    }
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", capabilities)
time.sleep(10)