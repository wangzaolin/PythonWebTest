#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
项目名称 ：PythonWebTest 
脚本名称 ：browseOperate02.py
开发环境 ：PyCharm 
开发人员 ：林
脚本功能：切换浏览器窗口
编写时间 ：2020/11/22 14:10 
'''

from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="./driver/chromedriver.exe")

#打开第一个窗口
driver.get("http://localhost/period5-1-1.html")
time.sleep(2)

#输出第一个窗口页面title
title01 = driver.title
print("title01:"+title01)

#获取当前页面句柄
handle01 = driver.current_window_handle
print("handle01:"+handle01)

#点击链接，打开页面第二个窗口,此时driver还停留在第一个窗口，需要切换到第二个窗口
driver.find_element_by_class_name("test").click()
time.sleep(2)

#获取当前所有窗口的句柄
handles = driver.window_handles
#切换到第二个页面的句柄
for handle in handles:
    print(handle)
    if handle != handle01:
        driver.switch_to.window(handle)

#获取第二个页面的title
title02 = driver.title
print("title02:"+title02)

#关闭所有窗口
driver.quit()