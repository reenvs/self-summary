#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver=webdriver.Firefox()
#打开浏览器，输入网址http://www.baidu.com
driver.get("http://www.baidu.com")
#inputEle=driver.find_element_by_id("kw")
inputEle=driver.find_element(By.ID,"kw")
inputEle.send_keys(u"网络爬虫")
inputEle.send_keys(Keys.RETURN)
time.sleep(5)
inputEle.clear()#清空元素
inputEle.send_keys(u"SKII")
inputEle.send_keys(Keys.RETURN)
driver.close()