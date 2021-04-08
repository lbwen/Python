#coding:utf-8
import xlrd
class ExcelR():
    def __init__(self,excelpath,sheetname="Sheet1"):
        self.data=xlrd.open_workbook("text.xlsx")
        self.table=self.data.sheet_by_name(sheetname)
        self.keys=self.table.row_values(0)
        self.rownum=self.table.nrows
        self.colnum=self.table.ncols
    def dict_data(self):
        if self.rownum<=1:
            print "总行数小于1"
        else:
            r=[]
            j=1
            for i in range(self.rownum-1):
                s={}
                #从第二行取对应的value值
                values=self.table.row_values(j)

                for x in range(self.colnum):
                    s[self.keys[x]]=values[x]
                r.append(s)
                j+=1
            return r

if __name__=="__main__":
    filepath="text.xlsx"
    sheetname="Sheet1"
    data=ExcelR(filepath,sheetname)
    print data.dict_data()