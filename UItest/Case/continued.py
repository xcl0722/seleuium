import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#持续拷机测试
options = Options()
options.add_experimental_option("excludeSwitches", ['enable-automation']) # 禁止谷歌弹出正在被自动化软件控制消息
driver = webdriver.Chrome(r"C:\Users\huarui\AppData\Local\KedaChromium\Application\chromedriver.exe", 0, options=options,keep_alive=True)
driver.get("http://192.168.7.7/ers-web/#/")
time.sleep(1)
driver.find_element_by_xpath("//div/div[2]/form/div[1]/div/div[1]/input").send_keys("on_suzhou")
driver.find_element_by_xpath("//div/div[2]/form/div[2]/div/div[1]/input").send_keys("keda123#")
driver.find_element_by_css_selector("#keybtn").click()
time.sleep(8)
all_handles = driver.window_handles
driver.switch_to.window(all_handles[-1])
driver.maximize_window()
try:
  i = 1
  while (i<100000000):
      driver.find_element_by_xpath("//div/div[1]/div/div/ul/li[2]/span[2]").click()  # 切换到处警Tab
      time.sleep(5)
      driver.find_element_by_css_selector("div.kiaf-nav-bar > div > div > ul > li:nth-child(1) > span:nth-child(2)").click() #切换到接警tab
      time.sleep(5)
      i=i+1
except:
 print("1亿次切换结束了")
driver.quit()
