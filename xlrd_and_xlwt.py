# coding=utf-8

import xlrd
import xlwt

file_path = r'C:/Users/ASUS/Desktop/HLD评审-counter_REVIEW FORM.xls'
# 获取excel文件对象
data = xlrd.open_workbook(file_path)
# 获取sheet对象
table_read = data.sheet_by_name('TotalDefect')

line_numbers = table_read.nrows
column_numbers = table_read.ncols

# 新建一个excel文件
file = xlwt.Workbook()
# 新建一个sheet
table_write = file.add_sheet('info', cell_overwrite_ok=True)
# 写入数据table.write(行,列,value)
for line in range(line_numbers):
    for column in range(column_numbers):
        table_write.write(line, column, table_read.cell_value(line, column))
# 保存文件
file.save('file.xls')
