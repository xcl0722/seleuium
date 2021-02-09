import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#持续拷机测试
options = Options()
options.add_experimental_option("excludeSwitches", ['enable-automation']) # 禁止谷歌弹出正在被自动化软件控制消息
driver = webdriver.Chrome(r"E:\python\chromedriver.exe", 0, options=options,keep_alive=True)
driver.get("https://dolphin-dev.kedacom.com/ers-web/#/")
time.sleep(1)
driver.find_element_by_xpath("//div/div[2]/form/div[1]/div/div[1]/input").send_keys("poc-xcl")
driver.find_element_by_xpath("//div/div[2]/form/div[2]/div/div[1]/input").send_keys("000000")
driver.find_element_by_css_selector("#keybtn").click()
time.sleep(5)
all_handles = driver.window_handles
driver.switch_to.window(all_handles[-1])
driver.maximize_window()
time.sleep(8)
i = 1
while (i < 100000000):
      driver.find_element_by_xpath("//div/form/div[1]/div[1]/div/div/div/input").send_keys("17751235678")  # 报警电话
      time.sleep(3)
      driver.find_element_by_xpath("//div/form/div[2]/div[1]/div/div/div/input").send_keys("国庆")  # 报警人姓名
      time.sleep(3)
      driver.find_element_by_xpath("//div[4]/div/div/div/div[1]/div[1]/div[1]/input").send_keys("苏州中心")
      time.sleep(6)
      driver.find_element_by_xpath(
          "/html/body/div[1]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/div/div[2]/div/form/div[4]/div/div/div/div[1]/div[1]/div[2]/div[1]/div[1]/ul").click()  # 选择有经纬度的地址
      time.sleep(5)
      driver.find_element_by_xpath("//form/div[6]/div[1]/div/div/div/div/span/span").click()  # 下拉
      time.sleep(6)
      driver.find_element_by_xpath("/html/body/div[last()]/div/div[1]/ul/li[1]").click()  # 火灾扑救
      time.sleep(6)
      driver.find_element_by_xpath("//div/form/div[6]/div[2]/div/div/div/div[1]/span/span/i").click()  # 下拉
      time.sleep(5)
      driver.find_element_by_xpath("//div/div/div/div[2]/div/div[1]/ul/div/div[1]/div/span[2]").click()  # 易燃易爆
      time.sleep(5)
      driver.find_element_by_xpath("//div/div[1]/div/div[2]/div/form/div[7]/div/div/div/span").click()  # 案件描述自动生成
      time.sleep(5)
      driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div[1]/span").click() # 立案
      time.sleep(6)
      driver.find_element_by_css_selector("div.kiaf-nav-bar > div > div > ul > li:nth-child(1) > span:nth-child(2)").click()  # 切换到接警tab
      time.sleep(5)
      i = i + 1
print("1亿次新建警情立案结束了")
driver.quit()
