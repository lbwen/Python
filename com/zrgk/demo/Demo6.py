#coding:utf-8
import os
#os.getcwd()
# os.makedirs(r"d:\ceshi\test")
fg1 = open("text.txt","a")
# fg1.write("23456")

for i in fg1.readline():
    print i
fg1.close()