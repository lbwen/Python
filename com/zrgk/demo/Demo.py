#coding=utf-8
import uniout
print"hello word"

print"你好"

a = "qwaszxerdfv"
b = 123456879
c = "前往而他岁的犯罪现场"

print a[1]      #访问
print c[2]

print a[1:5]       #截取
print a[1:7:2]     #切片
print a[1:7:3]

name = "张三"
print "名字是：%s"%name     #print "名字是：%r"%name
age = 22
print "年龄是：%d"%age      #print "年龄是：%r"%age
price = 22.5
print "价格是：%f"%price    #print "价格是：%r"%price

print "名字是：%s\t\t年龄是：%d"%(name,age)
print "名字是：%s\n年龄是：%d"%(name,age)

print "名字是：{}".format(name)
print "名字是：{a}".format(a=name)
q = "EWFSDF"
print q.lower()  #转化成小写

print "fewjfsjfsdjf\
      fdgdfgdfgdf"

print "c:coco\new\table"
print r"c:coco\new\table"  #原始字符串输出
print "c:coco\\new\\table"

#换行
print """fksdkfndsk
fmdslfmsd
mslfdm;lds
sd;lnfsd
"""         #''''''  也可以
#多行注释
# """ gjghj """或
# ''' hgjgh '''

h = input("请输入数字：")   #只能输入数字
print h
j = raw_input("输入：")    #输入什么都可以
print j

print len(j)    #取字符串长度