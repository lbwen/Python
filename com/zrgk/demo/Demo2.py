#coding:utf-8
# 1、将msg='hello word'中的word替换成hero
msg = "hello word"
# print msg.replace("word","hero")
# 2、将msg='hello word'中的o替换成hh
# print msg.replace("o","hh")
# 3、info = [1,2,3,4,5]，用两种方法，把列表变成:info=[5,4,3,2,1]
info = [1,2,3,4,5]
# print info[::-1]      #3
# info.reverse()
# print info
# info.sort()       #正序
# 4、 x = "abc1z" 用两种方法，把字符串x变成 x="abc2z"
x  = "abc1z"
print x.replace("1","2")
# 5、字符串 s = "i,am,lilei",请用两种办法取出“am”字符
s = "i,am,lilei"
# print s[2:4]

list = s.split(",")
print list[1]
# 6、bool("2012" == 2012) 的结果是什么。
print bool("2012"==2012)
# 7、已知如下变量
a = "字符串拼接1"
b = "字符串拼接2"
#  1.请用2种以上的方式将a与b拼接成字符串c。并指出每一种方法的优劣。
print a+b
#  2.请将a与b拼接成字符串c，并用逗号分隔。
print "%s,%s"%(a,b)
#  3.请计算出新拼接出来的字符串长度，并取出其中的第七个字符。
c = a+b
print len(c)
# 8、a = "i,am,a,boy,in,china"
#  1.请使用2种办法取出其间的字符"boy"和"china"。
a = "i,am,a,boy,in,china"

#  2.请找出第一个"i"出现的位置。
#  3.请找出"china"中的"i"字符在字符串a中的位置。
#  4.请计算该字符串一共有几个逗号
# 9、testList=[10086,'中国移动',[1,2,4,5]]
#  1、弹出列表的最后一个元素
#  2、向列表添加元素 'am'
# 10、将一个列表的数据复制到另一个列表中，使用列表[:]把列表a = [1, 2, 3] 复制到列表b


testList=[10086,'中国移动',[1,2,4,5]]
#取4
# print testList[2][2]

testList=[10086,'中国移动',[1,2,4,["aa",54,5,"test"]]]
# print testList[2][3][3]

# a = "aaa"
# print a

print 9.1//4.2

#复制
# list2 = list1     复制值
# list2 = list1[:]  复制地址