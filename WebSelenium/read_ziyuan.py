#coding:utf-8
import xlrd
import uniout
class ExcelR():
    def __init__(self,excelpath,sheetName = "Sheet1"):
        self.date = xlrd.open_workbook("ziyuan.xlsx")
        self.table = self.date.sheet_by_name(sheetName)
        self.keys = self.table.row_values(0)# 获取第一行值
        # self.keys = self.table.col_values(0)  # 获取第一列值
        self.rownum = self.table.nrows  # 获取总行数
        self.colnum = self.table.ncols  # 获取总列数

    def dict_data(self):
        if self.rownum<=1:
            print "总行数小于1"
        else:
            list1=[]
            j=1
            for i in range(self.rownum-1):
                s={}
                #从第二行取对应的value值
                values=self.table.row_values(j)

                for x in range(self.colnum):
                    s[self.keys[x]]=values[x]
                list1.append(s)
                j+=1
            return list1

if __name__=="__main__":
    filepath="E:\python\word\WebSelenium\ziyuan.xlsx"
    sheetName="Sheet1"
    data=ExcelR(filepath,sheetName)
    print data.dict_data()