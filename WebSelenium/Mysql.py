 #! /usr/bin/env python
# -*- coding: utf-8 -*-
import MySQLdb

class Database:
    #定义变量
    def __init__(self,user,passwd,db,host,port):
        self.user=user
        self.passwd=passwd
        self.db=db
        self.host=host
        self.port=port
        #链接数据库
        try:
            self.conn=MySQLdb.connect(user=self.user,passwd=self.passwd,db=self.db,host=self.host,port=self.port)
            self.cur=self.conn.cursor()
        except MySQLdb.Error as e:
            print(e)

    def is_User_exists(self,username):
        sql="select salary from employee where name='%s';" %username
        try:
            self.cur.execute(sql)
            data=self.cur.fetchall()        #输出mysql语句
            if len(data)==0:
                return False
            else:
                return True
        except MySQLdb.Error as e:
                print (e)

    #查询数据
    def opt_Select(self,username):
        sql="select salary from employee where name='%s';" %username
        try:
            self.cur.execute(sql)
            data=self.cur.fetchall()
            for i in data:
                print ('工资：        %d') %(i[0])
            print('查询数据')
        except MySQLdb.Error as e:
            print(e)

    #插入数据
    def opt_Insert(self,username,value):
        sql='insert into employee(name,salary) values(\'%s\',%s);' %(username,value)
        try:
            self.cur.execute(sql)
            self.conn.commit()
            print ('插入数据')
        except MySQLdb.Error as e:
            print(e)

    #修改员工工资
    def opt_Update(self,username,value):
        sql='update  employee set salary=%s where name=\'%s\';' %(value,username)
        try:
            self.cur.execute(sql)
            self.conn.commit()
            print ('修改数据')
        except MySQLdb.Error as e:
            print(e)

    #删除员工数据
    def opt_Delete(self,username):
        sql='delete from employee where name=\'%s\';' % username
        try:
            self.cur.execute(sql)
            self.conn.commit()
            print('删除数据')
        except MySQLdb.Error as e:
           print(e)

    def close_Conn(self):
        try:
            self.cur.close()
            self.conn.close()
        except MySQLdb.Error as e:
            print(e)


tips='''
 81 
 82 1: 查询
 83 2: 新增
 84 3: 修改 
 85 4: 删除
 86 5: 退出
 87 
 88 请选择:   
 89 '''
options=[1,2,3,4,5]

if __name__=='__main__':
    conn_mysql=Database('root','1','test','localhost',3306)
    while True:
        # 选择操作
        try:
            choose=input(tips)
        except(EOFError,KeyboardInterrupt):
            choose=5
        if choose not in options:
            continue
        elif choose==1:
            username = raw_input('输入要查询员工姓名:  ')
            if conn_mysql.is_User_exists(username) is False:
                print ('员工不存在')
            else:
                conn_mysql.opt_Select(username)
        elif choose==2:
            username,value = raw_input('输入新增员工姓名,工资:  ').split(',')
            conn_mysql.opt_Insert(username,value)
        elif choose==3:
            username,value= raw_input('输入要更新员工的姓名,工资:  ').split(',')
            conn_mysql.opt_Update(username,value)
        elif choose==4:
            username= raw_input('输入要删除员工的姓名:  ')
            conn_mysql.opt_Delete(username)
        elif choose==5:
            print('退出程序......')
            sys.exit()