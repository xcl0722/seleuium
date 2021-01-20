# import xlrd, xlwt
# import random
#
# """创建一个excel对象"""
# book = xlwt.Workbook(encoding='utf-8',style_compression=0)
# """创建sheet"""
# sheet = book.add_sheet('test',cell_overwrite_ok=True)
# """添加字段"""
# sheet.write(0, 0, '编号')
# sheet.write(0, 1, '名称')
# sheet.write(0, 2, 'DISPLAY_X')
# sheet.write(0, 3, 'DISPLAY_Y')
# sheet.write(0, 4, '销售数量')
# sheet.write(0, 5, '销售单价')
# sheet.write(0, 6, '销售收入')
# sheet.write(0, 7, '单位成本')
# sheet.write(0, 8, '销售成本')
# sheet.write(0, 9, '销售毛利')
#
# """写入编号字段数据"""
# for id in range(10000):
#     sheet.write(id + 1, 0, id)
#     sheet.write(id + 1, 1, "肯德基餐厅"+str(id))
#     sheet.write(id + 1, 2, round(random.uniform(3, 52), 2))
#     sheet.write(id + 1, 3, round(random.uniform(73, 135), 2))
#     sheet.write(id + 1, 4, round(random.uniform(1, 10001), 2))
#     sheet.write(id + 1, 5, round(random.uniform(1, 10001), 2))
#     sheet.write(id + 1, 6, round(random.uniform(1, 10001), 2))
#     sheet.write(id + 1, 7, round(random.uniform(1, 10001), 2))
#     sheet.write(id + 1, 8, round(random.uniform(1, 10001), 2))
#     sheet.write(id + 1, 9, round(random.uniform(1, 10001), 2))
# book.save(r'C:\Users\Z0043B9N\Desktop\xcl.xls')

# 离线数据导入构建测试数据脚本
import xlwt
import random
import datetime
start = '07/04/2020 09:00:00'
end = '07/14/2020 08:59:59'
datestart = datetime.datetime.strptime(start, '%m/%d/%Y %H:%M:%S')
dateend = datetime.datetime.strptime(end, '%m/%d/%Y %H:%M:%S')
# 生成按照一定规律递增的时间列表
data_list = list()
while datestart <= dateend:
    data_list.append(datestart.strftime('%m/%d/%Y %H:%M:%S'))
    datestart += datetime.timedelta(seconds=10)
"""创建一个excel对象"""
book = xlwt.Workbook(encoding='utf-8', style_compression=0)
"""创建sheet"""
sheet = book.add_sheet('test', cell_overwrite_ok=True)
"""添加字段"""
sheet.write(0, 0, 'SiemensSensorCode')
sheet.write(0, 1, 'Time')
sheet.write(0, 2, 'Value')

"""写入编号字段数据"""
for id in range(60000):
    sheet.write(id + 1, 0, 'xcl_XNDF-666666-1-SENSOR94')
# 依次取出列表里的时间值
    sheet.write(id + 1, 1, data_list[id])
    sheet.write(id + 1, 2, round(random.uniform(20, 90), 0))

# 保存文件到指定路径
book.save(r'C:\Users\Z0043B9N\Desktop\zhuce00.xls')


