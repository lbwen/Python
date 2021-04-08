#coding:utf8
import uniout
import MySQLdb
conn=MySQLdb.connect(host='169.254.180.116',port=3306,user='root',passwd='root',charset='utf8',db='ems')
cusor=conn.cursor()
#sql="insert welfare values(15,'py数据');"
#sql="select * from welfare;"
sql=" delete from welfare  where we_id=15;"
#upsql="update  welfare set we_name='五险一金1' WHERE  we_id=1;"
cusor.execute(sql)
conn.commit()
# rows = cusor.fetchall()
# print rows
# list1=list(rows)
# print list1
# for x in list1:
#     print x
# print type(x)
# cusor.execute(sql)
# conn.commit()
cusor.close()
conn.close()

