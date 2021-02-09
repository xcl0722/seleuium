#coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#新建警情预调派-调派-结案
options = Options()
#options.add_argument("--kiosk") # 加载启动项页面全屏效果，相当于F11。
options.add_experimental_option("excludeSwitches", ['enable-automation']) # 禁止谷歌弹出正在被自动化软件控制消息
driver = webdriver.Chrome(r"E:\python\chromedriver.exe", 0, options=options,keep_alive=True)
driver.get("https://dolphin-dev.kedacom.com/ers-web/#/")
time.sleep(1)
driver.find_element_by_xpath("//div/div[2]/form/div[1]/div/div[1]/input").send_keys("poc-xcl")
driver.find_element_by_xpath("//div/div[2]/form/div[2]/div/div[1]/input").send_keys("000000")
driver.find_element_by_css_selector("#keybtn").click()
time.sleep(10)
all_handles = driver.window_handles
driver.switch_to.window(all_handles[1])
driver.maximize_window()
time.sleep(6)
driver.switch_to.window(all_handles[-1])
driver.maximize_window()
time.sleep(3)
driver.find_element_by_xpath("//div/form/div[1]/div[1]/div/div/div/input").send_keys("17751235678")#报警电话
time.sleep(2)
driver.find_element_by_xpath("//div/form/div[2]/div[1]/div/div/div/input").send_keys("国庆")#报警人姓名
time.sleep(2)
driver.find_element_by_xpath("//div[4]/div/div/div/div[1]/div[1]/div[1]/input").send_keys("郭巷")
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/div/div[2]/div/form/div[4]/div/div/div/div[1]/div[1]/div[2]/div[1]/div[1]/ul").click()#选择有经纬度的地址
time.sleep(4)
driver.find_element_by_xpath("//form/div[6]/div[1]/div/div/div/div/span/span").click()#下拉
time.sleep(5)
driver.find_element_by_xpath("/html/body/div[last()]/div/div[1]/ul/li[1]").click()#火灾扑救
time.sleep(3)
driver.find_element_by_xpath("//div/form/div[6]/div[2]/div/div/div/div[1]/span/span/i").click()#下拉
time.sleep(2)
driver.find_element_by_xpath("//div/div/div/div[2]/div/div[1]/ul/div/div[1]/div/span[2]").click()#易燃易爆
time.sleep(3)
driver.find_element_by_xpath("//div/div[1]/div/div[2]/div/form/div[7]/div/div/div/span").click()#案件描述自动生成
time.sleep(3)
driver.find_element_by_css_selector("//div/div[2]/div/div[2]/div/div[3]/span").click()#预调派
time.sleep(3)
driver.find_element_by_xpath("//div/div[1]/div/div/ul/li[2]/span[2]").click()#切换到处警Tab
time.sleep(3)
driver.find_element_by_xpath("//div[1]/div/div[3]/div[2]/span[4]").click()#调派
time.sleep(4)
driver.find_element_by_css_selector("#tab-custom > div > div.tab-name").click()#自定义调派
time.sleep(3)
driver.find_element_by_css_selector("#pane-custom > div > label > span.kc-checkbox__input > span").click()#只显示可用车辆
time.sleep(3)
driver.find_element_by_xpath("//div/div[2]/div/ul[2]/li[1]/div[1]/div").click()#选择车辆
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