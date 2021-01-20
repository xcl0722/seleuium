#coding=utf-8
import time
import paramiko
from selenium import webdriver


driver = webdriver.Chrome()
driver.get("http://192.168.7.7/ers/#/")

time.sleep(2)
driver.find_element_by_xpath("//div/div[2]/form/div[1]/div/div[1]/input").send_keys("on_suzhou")
driver.find_element_by_xpath("//div/div[2]/form/div[2]/div/div[1]/input").send_keys("keda123#")
driver.find_element_by_css_selector("#keybtn").click()
driver.maximize_window()
time.sleep(10)

all_handles = driver.window_handles
driver.switch_to.window(all_handles[-1])
time.sleep(5)
driver.find_element_by_xpath("//div/div[1]/div/div/div[2]/div[1]/div/i").click()#点击登录话机
# all= driver.window_handles
# driver.switch_to.window(all[1])
print(all)
time.sleep(5)
driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div/div[2]/div[1]/div/div[2]/span").click()#点击登录坐席
time.sleep(5)
try:
    ssh_client = paramiko.SSHClient()
    ssh_client.load_system_host_keys()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect('192.168.7.83',22,'root','kedacom888')
    std_in,std_out,std_err = ssh_client.exec_command('cd /root/sipp-3.3.990/;sh uac_sendbye.sh 17751237537 1009 5080',get_pty=True)
# 在command命令最后加上 get_pty=True，执行多条命令 的话用；隔开，另外所有命令都在一个大的单引号范围内引用
    std_in.write('PWD'+'\n') #执行输入命令，输入sudo命令的密码，会自动执行
    for line in std_out:
        print (line.strip('\n'))
    ssh_client.close()
except:
    print()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[3]/div/div/div').click()#点击电话弹屏
time.sleep(2)
driver.find_element_by_xpath("//div/div[2]/div/form/div[9]/div/div/div/span/span/i").click()#下拉
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[7]/div/div[1]/ul/li[1]/span").click()#火灾扑救
time.sleep(1)
driver.find_element_by_xpath("//div/form/div[10]/div/div/div[1]/span/span/i").click()#下拉
time.sleep(1)
driver.find_element_by_xpath("//div/div[1]/ul/div/div[1]/div[1]/div[1]/div/div/span[2]").click()#易燃易爆
time.sleep(1)
driver.find_element_by_xpath("//div[1]/div/div[2]/div/form/div[11]/div/div[1]/input").send_keys("郭巷")
time.sleep(2)
driver.find_element_by_css_selector("body > ul > li:nth-child(4)").click()#选择有经纬度的地址
time.sleep(1)
driver.find_element_by_xpath("//div/div[1]/div/div[2]/div/form/div[14]/div/div/span").click()#案件描述自动生成
driver.find_element_by_xpath("//div/div[1]/div/div[2]/div/div[2]/div/div[2]/span").click()#立案
time.sleep(5)
# while True:
#     print("等待")
#     time.sleep(10)
#
#     if element.is_displayed():
#         print("有此元素,点击按钮")
#         driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[3]/div/div/div').click()
#         time.sleep(5)
#     else:
#         print("无此元素")
driver.quit()