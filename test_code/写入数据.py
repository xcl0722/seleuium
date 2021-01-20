# txt文件中写入数据
#调用open() 时提供了两个实参（见❶）。第一个实参也是要打开的文件的名称；第二个实参（'w' ）告诉Python，
# 我们要以写入模式 打开这个文件。打开文件 时，可指定读取模式 （'r' ）、
# 写入模式 （'w' ）、附加模式 （'a' ）或让你能够读取和写入文件的模式（'r+' ）。
# 如果你省略了模式实参，Python将以默认的只读模式打 开文件。 如果你要写入的文件不存在，函数open() 将自动创建它。
# 然而，以写入（'w' ）模式打开文件时千万要小心，因为如果指定的文件已经存在，Python将在返回文件对象前清空 该文件。



filename = 'C:\\Users\\Z0043B9N\\Desktop\\注册测点.txt'
# 用附近模式写入，不会覆盖文件里原来的内容
with open(filename, 'a') as file_object:
    file_object.write("I love programming. \n")


with open(filename,'r') as file_object:
    contents = file_object.read()
    print(contents)