#coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#进入处警，点击筛选火灾扑救2级的警情查看警情文书、现场信息、录音、指令、统计、关联警情
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
driver.find_element_by_xpath("//div[2]/div/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]").click()#更多查询
time.sleep(3)
driver.find_element_by_xpath("//div/div/form/div[1]/div/div/div/div[2]").click()#警情类型选择火灾扑救
time.sleep(2)
driver.find_element_by_xpath("//div/form/div[2]/div/div/div/div[3]").click()#警情等级选择二级
time.sleep(2)
driver.find_element_by_xpath("//div/div/form/div[5]/div/div/div/input").send_keys("郭巷")#事发地址输入郭巷
time.sleep(3)
driver.find_element_by_css_selector("#tab-writs > div > div.label-content").click()#查看警情文书
time.sleep(3)
driver.find_element_by_css_selector("div.writs-types > div > span:nth-child(5)").click()#查看警情状态变更
time.sleep(3)
driver.find_element_by_css_selector("#tab-logBox > div > div.label-content").click()#查看接警录音
time.sleep(3)
driver.find_element_by_css_selector("#tab-information > div > div.label-content").click()#查看现场信息
time.sleep(3)
driver.find_element_by_xpath("//div[2]/div[4]/div/div/div[1]/div/div[1]/span").click()#编辑现场信息
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div/input").clear()#清空上次的输入内容
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div/div[2]/div[2]/div/input").send_keys("1")#设置参战车辆
time.sleep(2)
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[3]/div[1]/span").click()#保存现场信息
time.sleep(2)
driver.find_element_by_css_selector("#tab-handle > div > div.label-content").click()#查看处置指令
time.sleep(3)
driver.find_element_by_xpath("//div/div[2]/ul/div[1]/div[1]/span[4]").click()#置顶处置指令
time.sleep(3)
driver.find_element_by_css_selector("div.instructions-btn-group > div > span.kircp-btn__text").click()#下发指令
time.sleep(2)
driver.find_element_by_css_selector("div.new-instruction-content-input.kc-textarea > textarea").send_keys("现场情况严峻，火速前往支援！")#输入指令内容
time.sleep(3)
driver.find_element_by_css_selector("div.kircp-btn.kircp-modal-content__btn.kircp-btn.kircp-btn--large.kircp-btn.kircp-btn--primary.kircp-btn > span").click()#提交指令
time.sleep(2)
driver.find_element_by_css_selector("#tab-linkage > div > div.label-content").click()#查看关联警情
time.sleep(3)
driver.find_element_by_xpath("//div/div/div/div[1]/div/span[2]/i").click()#点击右边箭头
time.sleep(3)
driver.find_element_by_css_selector("#tab-statistics > div > div.label-content").click()#查看统计汇总
time.sleep(3)
driver.quit()