#coding=utf-8
import os
from threading import Thread
sim = "E: & cd E:\\tomcat\\apache-tomcat-7.0.76\\apache-tomcat-7.0.76\\bin & startup.bat"
# print sim
r = os.system(sim)
# print r
# os.system("E:")
# os.system("cd E:\tomcat\apache-tomcat-7.0.76\apache-tomcat-7.0.76\bin")
# os.system("startup.bat")


# import subprocess
# process = subprocess.Popn("ls", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)