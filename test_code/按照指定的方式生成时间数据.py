import xlrd, xlwt
import random

"""创建一个excel对象"""
book = xlwt.Workbook(encoding='utf-8',style_compression=0)
"""创建sheet"""
sheet = book.add_sheet('test',cell_overwrite_ok=True)
"""添加字段"""
sheet.write(0, 0, 'Tag')
sheet.write(0, 1, 'Create Tag')
sheet.write(0, 2, 'Sensor Code')
sheet.write(0, 3, 'Sensor Description')

# """写入编号字段数据"""
for id in range(100):
    sheet.write(id + 1, 0, "dashuju_tagtest"+str(id) )
    sheet.write(id + 1, 1, 'yes')
    sheet.write(id + 1, 2, 'dashujusensorcode'+str(id))
book.save(r'C:\Users\Z0043B9N\Desktop\xcl.xls')
