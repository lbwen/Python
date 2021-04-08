#coding:utf-8

# year = input("输入年份：\n")
# if ((year%4 == 0) and (year % 100 != 0) or year % 400 == 0):
#     print "{}年是闰年".format(year)
# else:
#     print "{}年是平年".format(year)

# 上课共屏(9CB654475A06对话) 18:01:15
# 已知元组:
a = (1,4,5,6,7)
# 1 判断元素4是否在元组里
# if 4 in a:
#     print "在元组内"
# else:
#     print "不再元组内"
# 2 把元素5修改成8
# list1 = list(a)
# list1[2]=8
# a = tuple(list1)
# print a

# ##########################
b = [23,45,22,44,25,66,78]
# 用列表解析完成下面习题：
# 1 生成所有奇数组成的列表
list2 = []
# for qq in b:
#     if qq%2!=0:
#         list2.append(qq)
# print list2
# 2 输出结果: ['the content 23','the content 45']
# print "the content{},the content{}".format(b[0],b[1])
# print "the content%rb[0],the content%rb[1]"
# 3 输出结果: [25, 47, 24, 46, 27, 68, 80]
# ##############################
# 1 用2种方法输出下面的结果：
# [1,2,3,4,5,6,7,8]
list3 = [1,2,3,4,5,6,7,8]
# print list3
#
# 2 用列表的2种方法返回结果：[5,4]
list3.reverse()
# print list3[3:5]

# list4 = []
# for ww in list3:
#     if ww ==5 or ww == 4:
#         list4.append(ww)
# print list4
# 3 判断2是否在列表里
# if 2 in list3:
#     print "在"
# else:
#     print "不在"
# #######################
# 列表a = [shidonghui,22,24,29,30,32]
a = [11,22,24,29,30,32]
# 1 把28插入到列表的末端
# a.append(28)
# print a

# a.insert(6,28)
# print a
# 2 在元素29后面插入元素57
# a.insert(3,57)
# print a
# 3 把元素11修改成6
# a[0]=6
# print a
# 3 删除元素32
# a.pop()
# print a

# a.remove(32)
# print a
# 4 对列表从小到大排序
# a.sort()
# print a
# ######################
# ##习题7：
#
# 用字典的方式完成下面一个小型的学生管理系统。
#
# 1 学生有下面几个属性：姓名，年龄，考试分数包括：语文，数学，英语得分。
#
# 比如定义2个同学：
# 姓名：李明，年龄25，考试分数：语文80，数学75，英语85
# 姓名：张强，年龄23，考试分数：语文75，数学82，英语78
lm = {"name":"liming","age":25,"score":["yw80","sx75","yy85"]}
zq = {"name":"zhangqiang","age":23,"score":["yw75","sx82","yy78"]}
student = {"name":"liming","age":25,"score":{"Chinese":80,"Math":75,"English":85}}
# print lm
# 2 给学生添加一门python课程成绩，李明60分，张强：80分
# lm["score"].append("py60")
# print lm
# zq["score"].append("py80")
# print zq

# lm.setdefault("py",60)
# print lm
# 3 把张强的数学成绩由82分改成89分
# zq["score"][1]="sx89"
# print zq
# 4 删除李明的年龄数据
# del lm["age"]
# print lm
# 5 对张强同学的课程分数按照从低到高排序输出。
# zq = {"name":"zhangqiang","age":23,"score":[75,82,78]}
# zq["score"].sort()
# print zq["score"]
# 6 外部删除学生所在的城市属性，不存在返回字符串 beijing

dict1 = {"name":"zhngsan","age":18}
# print dict1["age"]
#
# print dict1.items()

# for y , v in dict1.items():
#     print y , v
#
# for y , v in dict1.keys() , dict1.values():
#     print y , v

import random
f = True
while f:
    s = int(random.uniform(1, 10))
    m = input("请输入一个整数\n")
    if m==s:
        print "随机数是：%d"%s
        print "恭喜你，猜对了！"
        f = False
    elif m>s:
        print "随机数是：%d"%s
        print "大了"
    else:
        print "随机数是：%d"%s
        print "小了"