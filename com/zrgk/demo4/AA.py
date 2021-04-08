#coding:utf-8
import xlrd

a = xlrd.open_workbook("text.xlsx")
b = a.sheet_by_name("Sheet1")
k = b.row_values(0)
print k
print type (k)
print k[0]
c = b.nrows
print c

{a:b}