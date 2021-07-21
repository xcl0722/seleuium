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
driver = webdriver.Chrome(r"E:\lijie\chromedriver.exe", 0, options=options,keep_alive=True)
driver.get("http://192.168.7.7/ers-web/#/")
#driver.maximize_window()
#driver.get("https://dolphin-dev.kedacom.com/ers-web/#/")
driver.implicitly_wait(10)
driver.find_element_by_xpath("//div/div[2]/form/div[1]/div/div[1]/input").send_keys("kunmingzd001")
driver.find_element_by_xpath("//div/div[2]/form/div[2]/div/div[1]/input").send_keys("keda123!")
time.sleep(2)
driver.find_element_by_css_selector("#keybtn").click()
time.sleep(5)
all_handles = driver.window_handles
driver.switch_to.window(all_handles[-1])
driver.maximize_window()
driver.implicitly_wait(8)
i = 1
while (i < 100000000):
      #j = random.randint(10000,50000)
      #driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div/div[2]/ul/li[2]/span[2]").click() #处警
      #time.sleep(5)
      #driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div/div[2]/ul/li[1]/span[2]").click() #接警
      #time.sleep(1)
      #driver.find_element_by_xpath("//*[@id=‘app’]/div/div[1]/div/div/div[2]/ul/li[3]/span[2]").click()  # 出警管理

      for j in range(1,10):

            time.sleep(2)
            driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/div/div/div[2]/div["+ str(j) +"]").click()  # 共10个页面
            #driver.find_element_by_xpath("/html/body/div[2]/ul/li["+ str(j) +"]").click() #人员信息等共9个页面
            time.sleep(5)
            print("page:", str(j))

      print(i)
      print("cpu利用率: " + str(get_cpu_info())+"%")
      print(get_memory_info())
      i = i + 1
print("1亿次新建警情立案结束了")
driver.quit()
