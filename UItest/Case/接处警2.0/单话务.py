#coding=utf-8
import time
import paramiko
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from sys_info import *
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


#电话弹屏创建警情立案-调派-结案
options = Options()
options.add_argument("--kiosk")  # 加载启动项页面全屏效果，相当于F11。
options.add_experimental_option("excludeSwitches", ['enable-automation']) # 禁止谷歌弹出正在被自动化软件控制消息
driver = webdriver.Chrome(r"E:\lijie\chromedriver.exe", 0, options=options,keep_alive=True)
driver.get("http://192.168.7.7/ers-web/#/")
time.sleep(2)
driver.find_element_by_xpath("//div/div[2]/form/div[1]/div/div[1]/input").send_keys("kunming001")
driver.find_element_by_xpath("//div/div[2]/form/div[2]/div/div[1]/input").send_keys("keda123!")
driver.find_element_by_css_selector("#keybtn").click()
time.sleep(10)
all_handles = driver.window_handles
driver.switch_to.window(all_handles[-1])
driver.maximize_window()
time.sleep(3)
driver.refresh()
time.sleep(3)
#print(driver.window_handles)
i = 1
while (i < 10000):

    try:
        ssh_client = paramiko.SSHClient()
        ssh_client.load_system_host_keys()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect('192.168.7.38', 22, 'root', 'kedacom888')
        std_in, std_out, std_err = ssh_client.exec_command('cd /opt/sipp-3.4.0/;sh uac_sendbye.sh 17751237537 1009 5080', get_pty=True)
        # 在command命令最后加上 get_pty=True，执行多条命令 的话用；隔开，另外所有命令都在一个大的单引号范围内引用
        std_in.write('PWD' + '\n')  # 执行输入命令，输入sudo命令的密码，会自动执行
        time.sleep(2)

        driver.implicitly_wait(10)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[3]/div/div/div').click()  # 点击接听
        for line in std_out:
            print(line.strip('\n'))
        ssh_client.close()
    except:
        print("voice send fail!")
    time.sleep(10)
    '''
    time.sleep(3)
    print("1111111111111111111111")

    #handle = driver.current_window_handle
    #print(handle)
    #driver.switch_to.window(handle)
    #driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[3]/div/div/div').click()  # 点击接听
    #driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[3]/div/div[3]/div/div/div').click()  # 点击接听
    #driver.find_element(By.CSS_SELECTOR, ".accpet-call").click()
    #driver.key_down(Keys.F11, element=None)
	#电话录音文件
    time.sleep(20)
    j = random.randint(10000,50000)

    driver.find_element_by_xpath("//div/form/div[1]/div/div/div/div[1]/div[1]/div[1]/input").send_keys("昆明长水国际机场")
    time.sleep(3)
    driver.find_element_by_xpath("//div/form/div[1]/div/div/div/div[1]/div[1]/div[2]/div[1]/div[1]/ul/li[1]/span[1]").click()  # 选择地址
    time.sleep(3)

    driver.find_element_by_xpath("//div/form/div[3]/div[2]/div/div/div/div[1]/span/span/i").click()  # 下拉
    time.sleep(3)
    driver.find_element_by_xpath("//div/div/div/div[2]/div/div[1]/ul/div/div[1]/div/span[2]").click()  # 易燃易爆
    time.sleep(3)
    driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[2]/div/div[1]/div/div[2]/section/div/div[2]/div/form/div[4]/div[2]/span").click()  # 案件描述自动生成
    time.sleep(2)
    driver.find_element_by_xpath("//div/form/div[7]/div[1]/div/div/div/input").send_keys("188565" + str(j))  # 报警电话
    time.sleep(2)
    driver.find_element_by_xpath("//div/form/div[8]/div[1]/div/div/div/input").send_keys("张国庆" + str(j))  # 报警人姓名
    time.sleep(2)

    driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[2]/div/div[1]/div/div[3]/div/div/div/div/div[1]/div[1]/div/span[1]/span").click()  # 自定义调派
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[2]/div/div[1]/div/div[3]/div/div/div/div/div[1]/div[2]/div[2]/div[3]/div/div[2]/div/ul[2]/li[1]/div[2]/span").click()  # 选择队伍
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[2]/div/div[1]/div/div[2]/section/div/div[2]/div/div[1]/div/div[1]/span").click()  # 立案
    # driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[2]/div/div[1]/div/div[2]/section/div/div[2]/div/div[1]/div/div[2]/span").click() #存草稿
    time.sleep(25)
    # driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/label").click()#当前灾情
	# time.sleep(5)
    driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]").click()  # 编辑
    time.sleep(5)
    driver.find_element_by_id("select").click()
    time.sleep(3)
    driver.find_element_by_xpath("/html/body/div[last()]/div/div[1]/ul/li[last()]/span").click()  # 结案
    time.sleep(5)

    driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div/div[2]/ul/li[1]/span[2]").click()
    time.sleep(3)
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    print(i)
    print("cpu利用率: " + str(get_cpu_info())+"%")
    print(get_memory_info())
    i = i + 1
print("Test Pass!")
driver.quit()
    '''