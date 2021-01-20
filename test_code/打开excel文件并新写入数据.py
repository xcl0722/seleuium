import xlwt
import xlrd

#xlrd.open_workbook(r'原文件的路径+文件名') 打开原工作簿；formatting_info = True表示保留工作簿中的格式
xls2 = xlrd.open_workbook(r'C:\Users\Z0043B9N\Desktop\lds.xls', formatting_info=True)

#通过from xlutils.copy import copy 来引入模块，然后copy(xlrd工作簿变量)来复制为新工作簿
from xlutils.copy import copy
xls3 = copy(xls2)
#.get_sheet(sheet编号)引用到目标sheet
#.write(行,列,值)写入数据
sheet3 = xls3.get_sheet(0)

#初始化样式
style = xlwt.XFStyle()
#为样式创建字体
font = xlwt.Font()
font.name = u'宋体'
#字体颜色为红色
font.colour_index = 0x0A
#字体大小，260就是13号字体，大概就是13*20得来的吧
font.height= 260
# 定义格式
style.font = font


sheet3.write(7,0,u'lds_dump_zhuce_0428',style)
sheet3.write(7,1,'yes')
sheet3.write(7,2,'lds_dump_sensorcode_0428python')
sheet3.write(7,3,'python_NB')
xls3.save(r'C:\Users\Z0043B9N\Desktop\lds_python.xls')