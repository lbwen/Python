#coding:utf-8
import uniout
t="test test test tset"
print t.split()

print t.replace("e","l")    #替换

list = [1,54,78,"dsf","发生的"]
list1 = [23,45,"dsf"]
print list

#修改
list[3]="we"

#添加
list.append("df")
print list

list.extend(list1)
print list

#删除
list2 = [1,2,5,456,12]
del list2[3]
print list2

del list2[2:4]
print list2

# del list2
# print list2