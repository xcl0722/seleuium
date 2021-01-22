import subprocess
a1 = "python ./jiechujing01.py"#新建警情预调派-调派-结案
a2 = "python ./jiechujing02.py"#电话弹屏创建警情立案-调派-结案
a3 = "python ./jiechujing03.py"#新建警情直接进行自定义调派-结案
a4 = "python ./jiechujing04.py"#进入处警，点击筛选火灾扑救2级的警情查看警情文书
a5 = "python ./jiechujing05.py"#新建警情预调派-多次调派-结案
a6 = "python ./jiechujing06.py"#进入处警，点击筛选火灾扑救2级的警情查看警情文书、现场信息、录音、指令、统计、关联警情
def main():
    p1 = subprocess.Popen(a1, shell=True)
    print(p1.wait())
    p2 = subprocess.Popen(a2, shell=True)
    print(p2.wait())
    p3 = subprocess.Popen(a3, shell=True)
    print(p3.wait())
    p4 = subprocess.Popen(a4, shell=True)
    print(p4.wait())
    p5 = subprocess.Popen(a5, shell=True)
    print(p5.wait())
    p6 = subprocess.Popen(a6, shell=True)
    print(p6.wait())

if __name__ == '__main__':
    main()