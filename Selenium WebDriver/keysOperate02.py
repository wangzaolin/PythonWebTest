#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
项目名称 ：PythonWebTest 
脚本名称 ：keysOperate02.py
开发环境 ：PyCharm
脚本功能：键盘操作keyUp/keyDown
开发人员 ：林
编写时间 ：2021/1/16 16:21 
'''

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("./driver/chromedriver.exe")

#模拟键盘ctrl+shift+x操作
ActionChains(driver).key_down(Keys.CONTROL).key_down(Keys.SHIFT).send_keys('x').perform()
time.sleep(3)

driver.close()