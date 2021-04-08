#coding:utf-8

# ll = open("text.txt","r")
# for i in ll.readlines():
#     if not i.strip().startswith("#"):
#         print i
# ll.close()

ll = open("text.txt","r")
for i in ll.readlines():
    if i <= 10:
        print i
