#coding:utf-8
import uniout
import time
import datetime

def port():
    port_list = []
    port_list = 123456
    print port_list

def dtime():
    # print time.time()
    nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print nowTime

if __name__ == '__main__':
    dtime()