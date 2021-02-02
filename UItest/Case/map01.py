import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#进入地图查看搜索兴趣点
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
driver.switch_to.window(all_handles[1])
driver.maximize_window()
time.sleep(3)
driver.find_element_by_xpath("//div[3]/div[1]/div[1]/div[1]/div/span/span/i").click()#点击下拉箭头
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[1]/ul/li/i").click()#点击右边箭头
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div[1]/ul/li[3]/label/span[1]/span").click()#选择吴中区
time.sleep(1)
driver.find_element_by_xpath("//div[3]/div[1]/div[1]/div[2]/input").send_keys("学校")#输入学校
time.sleep(2)
driver.find_element_by_xpath("//div[1]/div/div[2]/div[3]/div[1]/div[1]/button/i").click()#点击搜索
time.sleep(8)
driver.find_element_by_xpath("//div/div[1]/div/div[2]/div[3]/div[1]/div[2]/i").click()#收起兴趣点的搜索
driver.quit()