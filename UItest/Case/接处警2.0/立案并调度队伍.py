# -*- coding: utf-8
import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from sys_info import *


#持续拷机测试
options = Options()
options.add_argument("--kiosk")  # 加载启动项页面全屏效果，相当于F11。
options.add_experimental_option("excludeSwitches", ['enable-automation']) # 禁止谷歌弹出正在被自动化软件控制消息
driver = webdriver.Chrome(r"E:\python\chromedriver.exe", 0, options=options,keep_alive=True)
driver.get("https://10.20.66.9/ers-web/#/")
#driver.maximize_window()
#driver.get("https://dolphin-dev.kedacom.com/ers-web/#/")
driver.implicitly_wait(10)
driver.find_element_by_xpath("//div/div[2]/form/div[1]/div/div[1]/input").send_keys("ers-xcl")
driver.find_element_by_xpath("//div/div[2]/form/div[2]/div/div[1]/input").send_keys("000000")
time.sleep(2)
driver.find_element_by_css_selector("#keybtn").click()
time.sleep(5)
all_handles = driver.window_handles
driver.switch_to.window(all_handles[-1])
driver.maximize_window()
driver.implicitly_wait(8)
i = 1
while (i < 100000000):
      j = random.randint(10000,50000)

      driver.find_element_by_xpath("//div/form/div[1]/div/div/div/div[1]/div[1]/div[1]/input").send_keys("乌鲁木齐站")
      time.sleep(4)
      driver.find_element_by_xpath("//div/form/div[1]/div/div/div/div[1]/div[1]/div[2]/div[1]/div[1]/ul/li[1]/span[1]").click()  # 选择地址
      driver.implicitly_wait(3)
      #driver.find_element_by_xpath("//div/form/div[2]/div[1]/div/div/div/span/span[1]").click()  # 下拉
      #time.sleep(1)
      #driver.find_element_by_xpath("/html/body/div[last()]/div/div[1]/ul/li[1]/span").click()  # 管辖单位
      #time.sleep(2)
      #driver.find_element_by_xpath("//div/form/div[3]/div[1]/div/div/div/div/span/span").click()  # 下拉
      #time.sleep(4)
      #driver.find_element_by_xpath("/html/body/div[last()]/div/div[1]/ul/li[1]").click()  # 火灾扑救
      #time.sleep(3)
      driver.find_element_by_xpath("//div/form/div[3]/div[2]/div/div/div/div[1]/span/span/i").click()  # 下拉
      driver.implicitly_wait(3)
      driver.find_element_by_xpath("//div/div/div/div[2]/div/div[1]/ul/div/div[1]/div/span[2]").click()  # 易燃易爆
      driver.implicitly_wait(3)
      driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[2]/div/div[1]/div/div[2]/section/div/div[2]/div/form/div[4]/div[2]/span").click()  # 案件描述自动生成
      driver.implicitly_wait(2)
      driver.find_element_by_xpath("//div/form/div[7]/div[1]/div/div/div/input").send_keys("188565" + str(j))  # 报警电话
      driver.implicitly_wait(2)
      driver.find_element_by_xpath("//div/form/div[8]/div[1]/div/div/div/input").send_keys("张国庆" + str(j))  # 报警人姓名
      driver.implicitly_wait(2)

      driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[2]/div/div[1]/div/div[3]/div/div/div/div/div[1]/div[1]/div/span[1]/span").click() #自定义调派
      driver.implicitly_wait(2)
      driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[2]/div/div[1]/div/div[3]/div/div/div/div/div[1]/div[2]/div[2]/div[3]/div/div[2]/div/ul[2]/li[1]/div[2]/span").click() #选择队伍
      driver.implicitly_wait(2)
      driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[2]/div/div[1]/div/div[2]/section/div/div[2]/div/div[1]/div/div[1]/span").click() # 立案
      #driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[2]/div/div[1]/div/div[2]/section/div/div[2]/div/div[1]/div/div[2]/span").click() #存草稿
      #time.sleep(25)
      driver.implicitly_wait(30)
      driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/label").click()#当前灾情
      time.sleep(3)
      driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div/div[3]/div[1]/div[2]").click()  # 编辑
      time.sleep(4)
      driver.find_element_by_id("select").click()
      time.sleep(5)
      #driver.find_element_by_xpath("/html/body/div[last()]/div/div[1]/ul/li[12]/span").click()  # 结案
      driver.find_element_by_xpath("/html/body/div[last()]/div/div[1]/ul/li[last()]/span").click()  # 结案
      time.sleep(3)
      driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div/div[2]/ul/li[1]/span[2]").click()
      driver.refresh()
      time.sleep(3)
      print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
      print(i)
      print("cpu利用率: " + str(get_cpu_info())+"%")
      print(get_memory_info())
      i = i + 1
print("1亿次新建警情立案结束了")
driver.quit()
