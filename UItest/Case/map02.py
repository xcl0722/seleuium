import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#进入地图屏，展开收起右侧工具栏
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
driver.find_element_by_xpath("//div/div[1]/div/div/ul/li[2]/span[2]").click()#切换到处警Tab
time.sleep(3)
driver.switch_to.window(all_handles[1])#切换到地图屏
driver.maximize_window()
time.sleep(10)
# driver.find_element_by_xpath("//div[2]/div/div/div[2]/div/div[1]/div").click()#点击一下第一个警情
# time.sleep(3)
# driver.find_element_by_xpath("//div[2]/div/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]").click()#更多查询
# time.sleep(3)
# driver.find_element_by_xpath("//form/div[3]/div/div/div/div/span/span/i").click()#点击下拉箭头
# time.sleep(7)
# driver.find_element_by_css_selector("/html/body/div[2]/div/div[1]/ul/li[4]").click()#筛选下达状态
# time.sleep(3)
#driver.switch_to.window(all_handles[1])#切换到地图屏
# driver.find_element_by_css_selector("div.slotbox > div > div:nth-child(2)").click()#切换到地图屏
# driver.maximize_window()
# time.sleep(10)
driver.find_element_by_xpath("//div/div[2]/ul/li[2]/div/div/ul/li[2]").click()#查看属地资源
time.sleep(3)
driver.find_element_by_xpath("//div[1]/div/div[4]/ul/li[2]/div[2]").click()#查看微型消防站信息
time.sleep(3)
driver.find_element_by_xpath("//div/div[1]/div/div[4]/ul/li[3]/div[2]").click()#查看专业队伍
time.sleep(3)
driver.find_element_by_xpath("//div[1]/div/div[4]/ul/li[4]/div[2]").click()#查看重点单位
time.sleep(3)
driver.find_element_by_xpath("//div/div[1]/div/div[4]/ul/li[5]/div[2]").click()#查看天然水源
time.sleep(3)
driver.find_element_by_xpath("//div[1]/div/div[4]/ul/li[6]/div[2]").click()#查看消防水源
time.sleep(3)
#点击收起地图右侧工具栏
driver.find_element_by_xpath("//div/div[2]/div/div[1]/div/div[7]/div[1]").click()
time.sleep(5)
#展开地图屏右侧工具栏
driver.find_element_by_xpath("//div/div[2]/div/div[1]/div/div[7]/div[1]").click()
time.sleep(3)
driver.find_element_by_css_selector("div > div.weather-header").click()#查看天气信息
time.sleep(3)
#关闭天气详情弹窗
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[1]/div").click()
time.sleep(3)
#查看周边资源
driver.find_element_by_xpath("//div[3]/div[2]/div/div[2]/ul/li[2]/div/div/ul/li[1]").click()
time.sleep(4)
#切换战备值守模式
driver.find_element_by_xpath("//div/div[2]/ul/li[2]/div/div/ul/li[2]").click()
time.sleep(3)
driver.quit()