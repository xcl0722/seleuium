#coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#进入处警，查看统计汇总导出pdf
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
driver.find_element_by_xpath("//div[3]/div/div/div/div/div/div[1]/div/span[2]/i").click()#点击右边箭头
time.sleep(3)
driver.find_element_by_css_selector("#tab-statistics > div > div.label-content").click()#查看统计汇总
time.sleep(3)
driver.find_element_by_css_selector("div.statistics-first-line > div > div:nth-child(2) > span.kircp-btn__text").click()#导出pdf
time.sleep(5)
driver.quit()