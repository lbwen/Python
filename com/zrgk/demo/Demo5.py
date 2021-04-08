#coding:utf-8
# def price(n):
#     if n==1:
#         return 1
#     else:
#         return price(n-1)*3
# print price(5)

# 写个字符串，通过遍历的方式计算字符串的长度
# def getLen(str):
#     l=0
#     for s in str:
#         l+=1
#     print "该字符串的长度为：%d"%l
#     return l
# getLen("woareyoudoing")
# def strjoin(*num):
#     return num[0]+num[-1]
# print  strjoin("22","33","4")
# //写入不定个数的字符串拼接第一个和最后一个字符串//
# 函数写出菲波那切数列\\编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,
# 当输入n为奇数时，调用函数1/1+1/3+...+1/n

def fab(n):
  if n==1:
    return 1
  if n==0:
    return 0
  else:
    result=int(fab(n-1))+int(fab(n-2))
    return result
#奇数

# def even(num):
#     s = 0
#     for i in range(2, num+1, 2):
#         s += 1 / i
#     return s
# def odd(num):
#     s = 0
#     for i in range(1, num+1, 2):
#         s +=1 / i
#     return s
# num = int(input("请输入一个整数："))
# if num % 2 == 0:
#    print("偶数")
#    sum = even(num)
# else:
#     print("奇数")
#     sum = odd(num)
# print sum

