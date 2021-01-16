#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
项目名称 ：PythonWebTest 
脚本名称 ：KysOperate.py
开发环境 ：PyCharm 
开发人员 ：林
脚本功能：键盘操作
编写时间 ：2021/1/16 15:54 
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path='./driver/chromedriver.exe')
driver.maximize_window()
driver.get("http://localhost/period7.html")
time.sleep(3)

#使用send_keys模拟ctrl+a全选操作
driver.find_element_by_class_name("ctrl-c").send_keys(Keys.CONTROL,'a')

#使用send_keys模拟ctrl+c复制操作
driver.find_element_by_class_name("ctrl-c").send_keys(Keys.CONTROL,'c')

#使用send_keys模拟ctrl+v粘贴操作
driver.find_element_by_class_name("ctrl-v").send_keys(Keys.CONTROL,'v')
time.sleep(3)

#清空
driver.find_element_by_class_name("ctrl-v").clear()

#模拟输入数字
driver.find_element_by_class_name("ctrl-v").send_keys(Keys.NUMPAD0)
driver.find_element_by_class_name("ctrl-v").send_keys(Keys.NUMPAD0)
driver.find_element_by_class_name("ctrl-v").send_keys(Keys.NUMPAD1)

#模拟空格键
driver.find_element_by_class_name("ctrl-v").send_keys(Keys.SPACE)

#直接输入数字
driver.find_element_by_class_name("ctrl-v").send_keys("002")

#模拟键盘输入制表键
driver.find_element_by_class_name("ctrl-v").send_keys(Keys.TAB)
time.sleep(3)

driver.close()
