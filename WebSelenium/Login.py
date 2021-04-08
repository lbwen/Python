#coding:utf-8
import MySQLdb
from selenium import webdriver
# db = MySQLdb.connect("123.207.150.226","root","huatai110%!","sdhui")
# db=MySQLdb.connect(host='123.207.150.226',port=3306,user='root',passwd='huatai110%!',charset='utf8',db='sdhui')
# cursor = db.cursor()
# sql = "SELECT * FROM `t_user` where msisdn = '12345678914';"


#建立和数据库的连接
db = MySQLdb.connect(host= '123.207.150.226',user="root",passwd="huatai110%!",db = "sdhui")
#获取操作游标
cursor = db.cursor()
#执行sql
cursor.execute("select * from t_user where msisdn = '12345678914'")
print cursor.fetchall()

#关闭
cursor.close()
db.close()

driver = webdriver.Firefox()
driver.get("https://www.baidu.com")

