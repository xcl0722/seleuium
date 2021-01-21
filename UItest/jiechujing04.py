#coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#进入处警，点击筛选火灾扑救2级的警情查看警情文书
options = Options()
options.add_experimental_option("excludeSwitches", ['enable-automation']) # 禁止谷歌弹出正在被自动化软件控制消息
driver = webdriver.Chrome(r"E:\python\chromedriver.exe", 0, options=options,keep_alive=True)
driver.get("http://192.168.7.7/ers/#/")
time.sleep(1)
driver.find_element_by_xpath("//div/div[2]/form/div[1]/div/div[1]/input").send_keys("on_suzhou")
driver.find_element_by_xpath("//div/div[2]/form/div[2]/div/div[1]/input").send_keys("keda123#")
driver.find_element_by_css_selector("#keybtn").click()
time.sleep(8)
all_handles = driver.window_handles
driver.switch_to.window(all_handles[-1])
driver.maximize_window()
time.sleep(3)
driver.find_element_by_xpath("//div/div[1]/div/div/ul/li[2]/span[2]").click()#切换到处警Tab
time.sleep(3)
driver.find_element_by_xpath("//div[2]/div/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]").click()#更多查询
time.sleep(3)
driver.find_element_by_xpath("//div/div/form/div[1]/div/div/div/div[2]").click()#警情类型选择火灾扑救
time.sleep(2)
driver.find_element_by_xpath("//div/form/div[2]/div/div/div/div[3]").click()#警情等级选择二级
time.sleep(2)
driver.find_element_by_xpath("//div/div/form/div[5]/div/div/div/input").send_keys("郭巷")#事发地址输入郭巷
time.sleep(3)
driver.find_element_by_css_selector("#tab-writs > div > div.label-content").click()#查看警情文书
time.sleep(5)
driver.find_element_by_class_name("label-content").click()#查看参战力量
time.sleep(3)
driver.quit()