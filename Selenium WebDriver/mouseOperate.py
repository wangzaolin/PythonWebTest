#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
项目名称 ：PythonWebTest 
脚本名称 ：mouseOperate.py
开发环境 ：PyCharm 
开发人员 ：林
脚本功能：模拟鼠标操作
编写时间 ：2021/1/16 16:55 
'''

import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver =webdriver.Chrome(executable_path="./driver/chromedriver.exe")
driver.maximize_window()
driver.get("http://www.baidu.com")

# #鼠标右击搜索框
# element = driver.find_element_by_id("kw")
# ActionChains(driver).context_click(element).perform()
# time.sleep(3)
#
# #模拟键盘取消ESC
# ActionChains(driver).send_keys(Keys.ESCAPE)

#鼠标悬停到设置菜单
element = driver.find_element_by_id("s-usersetting-top")
ActionChains(driver).move_to_element(element).perform()
time.sleep(3)

driver.close()
