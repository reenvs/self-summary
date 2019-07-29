#coding:utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver=webdriver.Firefox()
driver.get(r"file:///e:\cc.html")
#操作下拉菜单
select=Select(driver.find_element_by_xpath("/html/body/form/select"))
select.select_by_index(1)
usernameEle=driver.find_element_by_name("username")
passwordEle=driver.find_element_by_name("password")
print usernameEle
print passwordEle
usernameEle.clear()
usernameEle.send_keys(u"张三")
time.sleep(2)

passwordEle.clear()
passwordEle.send_keys(u"123456")
time.sleep(2)
#获取登录按钮
loginEle=driver.find_element_by_xpath("//input[@value='Login']")
print loginEle
loginEle.click()
time.sleep(2)




