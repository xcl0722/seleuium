# 打开txt格式的文件
with open('C:\\Users\\Z0043B9N\\Desktop\\1.txt', encoding='utf-8') as file_object:
    contents = file_object.read()
    print(contents)

# 打开excel表格文件
import xlrd, xlwt

file_path = 'C:\\Users\\Z0043B9N\\Desktop\\lds.xls'
data = xlrd.open_workbook(file_path)  # 打开xls文件
table = data.sheets()[0]  # 打开第一张表
nrows = table.nrows  # 获取表的行数
for i in range(nrows):  # 循环逐行打印
    if i == 0:  # 跳过第一行
        continue
    print(table.row_values(i))