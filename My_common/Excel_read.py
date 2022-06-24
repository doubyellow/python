# coding=utf-8
import xlrd


def read_product_data(file_path, sheet_name='Sheet1'):
    # 获取excel文件对象
    data = xlrd.open_workbook(file_path)
    # 获取sheet对象
    table_read = data.sheet_by_name(sheet_name)
    # 获取行列数
    line_numbers = table_read.nrows
    column_numbers = table_read.ncols
    for i in range(1, line_numbers):
        fund_product_no = str((table_read.cell_value(i, 2))).strip()
        fund_product_name = str(table_read.cell_value(i, 3)).strip()
        if fund_product_name.strip():
            # print(fund_product_no, fund_product_name)
            yield fund_product_no, fund_product_name


file_pat = r"C:\Users\ASUS\Desktop\中电惠融项目\惠融e信通平台短信&站内信0421(1).xls"
sheet_name = "短信模板"

with open("sql.txt","w+", encoding="utf-8") as f:
    for a, b in read_product_data(file_pat, sheet_name):
        f.write('update `sun_msg_template` set msg_template_content="%s" where msg_template_no="%s";\n' % (b, a))
