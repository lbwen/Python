#coding:utf-8
import xlrd
# excel = xlrd.open_workbook('E:/case.xls')
# data = excel.sheets()[0]
# print data.nrows
# print data.cell(4,4).value

class OperaExcel:
    def __init__(self,file_path=None):
        if file_path == None:
            self.file_path = 'E:/case.xls'
        else:
            self.file_path = file_path
        self.excel = self.get_excel()

    #获取excel
    def get_excel(self):
        excle = xlrd.open_workbook(self.file_path)
        return excle

    #获取sheets的内容
    def get_sheets(self,i):
        tables = self.excel.sheets()[i]
        return tables

