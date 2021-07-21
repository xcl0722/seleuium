#coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#新建警情预调派-多次调派-结案
options = Options()
options.add_experimental_option("excludeSwitches", ['enable-automation']) # 禁止谷歌弹出正在被自动化软件控制消息
driver = webdriver.Chrome(r"E:\python\chromedriver.exe", 0, options=options,keep_alive=True)
driver.get("https://dolphin-dev.kedacom.com/ers-web/#/")
time.sleep(1)
driver.find_element_by_xpath("//div/div[2]/form/div[1]/div/div[1]/input").send_keys("poc-xcl")
driver.find_element_by_xpath("//div/div[2]/form/div[2]/div/div[1]/input").send_keys("000000")
driver.find_element_by_css_selector("#keybtn").click()
time.sleep(8)
all_handles = driver.window_handles
driver.switch_to.window(all_handles[-1])
driver.maximize_window()
time.sleep(3)
driver.find_element_by_xpath("//div/form/div[1]/div[1]/div/div/div/input").send_keys("17751235678")  # 报警电话
time.sleep(3)
driver.find_element_by_xpath("//div/form/div[2]/div[1]/div/div/div/input").send_keys("国庆")  # 报警人姓名
time.sleep(3)
driver.find_element_by_xpath("//div[4]/div/div/div/div[1]/div[1]/div[1]/input").send_keys("苏州中心")
time.sleep(6)
driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/div/div[2]/div/form/div[4]/div/div/div/div[1]/div[1]/div[2]/div[1]/div[1]/ul").click()  # 选择有经纬度的地址
time.sleep(5)
driver.find_element_by_xpath("//form/div[6]/div[1]/div/div/div/div/span/span").click()  # 下拉
time.sleep(5)
driver.find_element_by_xpath("/html/body/div[last()]/div/div[1]/ul/li[1]").click()  # 火灾扑救
time.sleep(5)
driver.find_element_by_xpath("//div/form/div[6]/div[2]/div/div/div/div[1]/span/span/i").click()  # 下拉
time.sleep(5)
driver.find_element_by_xpath("//div/div/div/div[2]/div/div[1]/ul/div/div[1]/div/span[2]").click()  # 易燃易爆
time.sleep(5)
driver.find_element_by_xpath("//div/div[1]/div/div[2]/div/form/div[7]/div/div/div/span").click()  # 案件描述自动生成
time.sleep(5)
driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div[1]/span").click()  # 立案
time.sleep(6)
driver.find_element_by_xpath("//div[1]/div/div[2]/div/div[2]/div/div/div[6]/div[4]/span").click()#调派
time.sleep(5)
driver.find_element_by_xpath("//div[2]/div[2]/div/div/div[1]/div[1]/div[1]/div/span[3]/span").click()#自定义调派
time.sleep(2)
driver.find_element_by_xpath("//div/div[2]/div/ul[2]/li[1]/div[1]/div").click()#第一个车
time.sleep(3)
driver.find_element_by_xpath("//div[2]/div[2]/div[2]/div/div/div[3]/div/span").click()#立即下达
time.sleep(3)
driver.find_element_by_xpath("//div/div[1]/div/div[2]/div/div[2]/div/div/div[6]/div[3]/span").click()#再次调派
time.sleep(5)
driver.find_element_by_xpath("//div[2]/div[2]/div/div/div[1]/div[1]/div[1]/div/span[3]/span").click()#自定义调派
time.sleep(2)
driver.find_element_by_xpath("//div/div[2]/div/ul[2]/li[1]/div[1]/div").click()#第一个车
time.sleep(3)
driver.find_element_by_xpath("//div[2]/div[2]/div[2]/div/div/div[3]/div/span").click()#立即下达
time.sleep(3)
driver.find_element_by_xpath("//div[2]/div/div/div[3]/div[1]/div[2]").click()#状态编辑
time.sleep(2)
driver.find_element_by_id("select").click()#点击警情状态流转框
time.sleep(5)
driver.find_element_by_xpath("/html/body/div[last()]/div/div[1]/ul/li[11]").click()
time.sleep(5)
driver.quit()