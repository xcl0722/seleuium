#coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#新建警情预调派-多次调派-结案
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
driver.find_element_by_xpath("//div/div[2]/div/form/div[2]/div/div/input").send_keys("17751235678")#报警电话
time.sleep(2)
driver.find_element_by_xpath("//div/form/div[3]/div/div/input").send_keys("国庆")#报警人姓名
time.sleep(2)
driver.find_element_by_xpath("//div/div[2]/div/form/div[9]/div/div/div/span/span/i").click()#下拉
time.sleep(5)
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
time.sleep(3)
driver.find_element_by_css_selector(" div.btn-group-wrap > div > div:nth-child(1) > span").click()#预调派
time.sleep(3)
driver.find_element_by_xpath("//div/div[1]/div/div/ul/li[2]/span[2]").click()#切换到处警Tab
time.sleep(3)
driver.find_element_by_xpath("//div[1]/div/div[3]/div[2]/span[4]").click()#调派
time.sleep(5)
driver.find_element_by_css_selector("#tab-car > div > div.tab-name").click()#车辆调派
time.sleep(2)
driver.find_element_by_css_selector("#pane-car > div > div.kircp-empty-wrap > div > ul > li > div:nth-child(2) > div").click()#第一个车
time.sleep(2)
driver.find_element_by_xpath("//div[2]/div/div/div/div[2]/div/span").click()#立即下达
time.sleep(3)
driver.find_element_by_xpath("//div[1]/div/div[3]/div[2]/span[4]").click()#再次调派
time.sleep(5)
driver.find_element_by_css_selector("#tab-car > div > div.tab-name").click()#车辆调派
time.sleep(2)
driver.find_element_by_css_selector("#pane-car > div > div.kircp-empty-wrap > div > ul > li > div:nth-child(2) > div").click()#第一个车
time.sleep(2)
driver.find_element_by_xpath("//div[2]/div/div/div/div[2]/div/span").click()#立即下达
time.sleep(5)
driver.find_element_by_xpath("//div[2]/div/div/div[3]/div[1]/div[2]").click()#状态编辑
time.sleep(2)
driver.find_element_by_id("select").click()#点击警情状态流转框
time.sleep(5)
driver.find_element_by_xpath("/html/body/div[last()]/div/div[1]/ul/li[11]").click()
time.sleep(2)
driver.quit()