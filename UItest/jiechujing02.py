#coding=utf-8
import time
import paramiko
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
#电话弹屏创建警情立案-调派-结案
options = Options()
#options.add_argument("--kiosk") # 加载启动项页面全屏效果，相当于F11。
options.add_experimental_option("excludeSwitches", ['enable-automation']) # 禁止谷歌弹出正在被自动化软件控制消息
driver = webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe", 0, options=options,keep_alive=True)
driver.get("http://192.168.7.7/ers/#/")
time.sleep(2)
driver.find_element_by_xpath("//div/div[2]/form/div[1]/div/div[1]/input").send_keys("on_suzhou")
driver.find_element_by_xpath("//div/div[2]/form/div[2]/div/div[1]/input").send_keys("keda123#")
driver.find_element_by_css_selector("#keybtn").click()
time.sleep(10)
all_handles = driver.window_handles
driver.switch_to.window(all_handles[-1])
driver.maximize_window()
time.sleep(3)
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
#driver.find_element_by_xpath('//*[@id="app"]/div/div[3]/div/div[3]/div/div/div').click()#点击电话弹屏
#driver.key_down(Keys.F11, element=None)
time.sleep(3)
driver.find_element_by_xpath("//div/div[2]/div/form/div[9]/div/div/div/span/span/i").click()#下拉
time.sleep(4)
driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/ul/li[1]").click()#火灾扑救
time.sleep(3)
driver.find_element_by_xpath("//div/form/div[10]/div/div/div[1]/span/span/i").click()#下拉
time.sleep(2)
driver.find_element_by_xpath("//div/div[1]/ul/div/div[1]/div[1]/div[1]/div/div/span[2]").click()#易燃易爆
time.sleep(3)
driver.find_element_by_xpath("//div[1]/div/div[2]/div/form/div[11]/div/div[1]/input").send_keys("郭巷")
time.sleep(3)
driver.find_element_by_css_selector("body > ul > li:nth-child(2)").click()#选择有经纬度的地址
time.sleep(4)
driver.find_element_by_xpath("//div/div[1]/div/div[2]/div/form/div[14]/div/div/span").click()#案件描述自动生成
time.sleep(5)
driver.find_element_by_xpath("//div/div[2]/div/div[2]/div/div[1]/div/div[2]/div/form/div[13]/div/span[2]").click()
time.sleep(5)
driver.find_element_by_xpath("//div/div[1]/div/div[2]/div/div[2]/div/div[2]/span").click()#立案
time.sleep(5)
driver.find_element_by_xpath("//div[2]/div/div[1]/div/div[2]/div/div[2]/div/div/div[5]/div[1]/span").click()#调派
time.sleep(6)
driver.find_element_by_css_selector("#tab-car > div > div.tab-name").click()#车辆调派
time.sleep(2)
driver.find_element_by_css_selector("#pane-car > div > div.kircp-empty-wrap > div > ul > li > div:nth-child(2) > div").click()#第一个车
time.sleep(2)
driver.find_element_by_xpath("//div[2]/div/div/div/div[2]/div/span").click()#立即下达
time.sleep(5)
driver.find_element_by_xpath("//div[2]/div/div[2]/div/div/div[4]/div[1]/div[2]").click()#状态编辑
time.sleep(2)
driver.find_element_by_id("select").click()#点击警情状态流转框
time.sleep(5)
driver.find_element_by_xpath("/html/body/div[last()]/div/div[1]/ul/li[11]").click()
time.sleep(2)
driver.quit()