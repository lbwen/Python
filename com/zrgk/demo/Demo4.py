#coding:utf-8
import uniout
# 功能：使用while循环输出1到10
# num = 1
# while num<shidonghui:
#     print num
#     num+=1

# 功能：求1-100的所有数的和
# num = 0
# sum = 0
# while num<101:
#     sum+=num
#     num+=1
# print sum

# 功能：输出1-100内的所有奇数
# num = 1
# sum = 0
# while num<101:
#     if num%2!=0:
#         sum+=num
#     num+=1
# print sum

# 功能：输出1-100内的所有偶数
# num = 1
# sum = 0
# while num<101:
#     if num%2==0:
#         sum+=num
#     num+=1
# print sum

# x = 1
# sum = 0
# sum1 = 0
# while x in range(1,101):
#     if x%2==0:
#         sum+=x
#     else:
#         sum1+=x
#     x+=1
# print "偶数和：%d"%sum
# print "奇数和：%d"%sum1

# num = 1
# sum = 0
# for x in range(1,101):
#     sum+=x
# print sum

# 功能：求1-2+3-4+5 ... 99的所有数的和
# num = 0
# for i in range(1,100):
#      if i % 2 == 0:
#         num = num - i
#      else:
#         num = num + i
# print num

# 功能：用户登录(三次机会尝试)    name = "admin"     password = 123
# for i in range(1,4):
#     name = raw_input("请输入用户名：")
#     password = raw_input("请输入密码：")
#     if name == "admin" and password == "123":
#         print "登录成功！"
#         break
#     else:
#         print "用户名或密码错误，请重新登录！"
# else:
#     print "输入次数超过三次，无法再次输入"

#素数

for i  in range(2,101):
    fg = 0
    for j in range(2,i-1):
        if i%j==0:
            fg = 1
            break
    if fg == 0:
        print i

# 上课共屏(9CB654475A06对话) 16:40:20
# 1、有两个列表，分别存放来老男孩报名学习linux和python课程的学生名字
linux=['钢弹','小壁虎','小虎比','alex','wupeiqi','yuanhao']
python=['dragon','钢弹','zhejiangF4','小虎比']
# 提示：使用for循环嵌套
# 问题一：得出既报名linux又报名python的学生列表
# student = []
# for stu in linux:
#     if stu in python:
#         student.append(stu)
# print student
# 问题二：得出只报名linux，而没有报名python的学生列表
# student = []
# for stu in linux:
#     if stu not in python:
#         student.append(stu)
# print student
# 问题三：得出只报名python，而没有报名linux的学生列表
# student = []
# for stu in python:
#     if stu not in linux:
#         student.append(stu)
# print student
# 上课共屏(9CB654475A06对话) 16:48:26
# 企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，
# 低于10万元的部分按10%提成，高于10万元的部分，可可提成7.5%；20万到40万之间时，高于20万元的部分，
# 可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，
# 可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
# profit = float(raw_input("请输入当月利润(万)： "))
# if profit<=10:
#         print "利润是：{}万".format(profit*0.1)
# elif profit<=20 and profit>10:
#         print "利润是：{}万".format((profit-10)*0.075+10*0.1)
# elif profit<=40 and profit>20:
#         print (profit-20)*0.05+10*0.1+10*0.075
# elif profit<=60 and profit>40:
#         print "利润是：{}万".format((profit-40)*0.03+20*0.05+10*0.075+10*0.1)
# elif profit<=100 and profit>60:
#         print "利润是：{}万".format((profit-60)*0.015+20*0.03+20*0.05+10*0.075+10*0.1)
# elif profit>100:
#         print "利润是：{}万".format((profit-100)*0.01+40*0.015+20*0.03+20*0.05+10*0.075+10*0.1)

# 上课共屏(9CB654475A06对话) 16:49:32
# 输入三个整数x,y,z，请把这三个数由小到大输出。
# list1 = []
# for i in range(1,4):
#     a = input("请输入数：")
#     list1.append(a)
# list1.sort()
# print list1
# 上课共屏(9CB654475A06对话) 16:51:36
# 给一个字符串，统计其中的数字、字母和其他类型字符的个数；
# 比如输入“124mid-=”，输出：数字=3，字母=3，其他=2。
# intCount = 0
# strCount = 0
# otherCount = 0
# a = raw_input("请输入：")
# for i in a:
#     if i.isdigit():
#         intCount += 1
#     elif i.isalpha():
#         strCount += 1
#     else:
#         otherCount += 1
# print "数字=%d，字母=%s，其他=%r"%(intCount,strCount,otherCount)
# 上课共屏(9CB654475A06对话) 16:53:34
# 合并两个列表，相同的元素不要
#  li1 = [1,2,34,5,6]
#     li2 = [2,3,4,5,67,8,89,9,34]

# li1 = [1,2,34,5,6]
# li2 = [2,3,4,5,67,8,89,9,34]
# li3 = li1[:]
# for i in li2:
#         if i in li3:
#             continue
#         else:
#             li3.append(i)
# print li3
# 水仙花
# for i in range(100, 1000):
#     a = i // 100
#     b = (i % 100) // 10
#     c = (i % 100) % 10
#     if i == a ** 3 + b ** 3 + c ** 3:
#         print(i)