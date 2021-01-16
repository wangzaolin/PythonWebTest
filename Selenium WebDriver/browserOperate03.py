#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
项目名称 ：PythonWebTest 
脚本名称 ：browserOperate03.py
开发环境 ：PyCharm 
开发人员 ：林
开发功能：滚动条操作
编写时间 ：2020/11/22 12:59 
'''

from selenium import webdriver
import time

#浏览器初始化
driver = webdriver.Chrome(executable_path='./driver/chromedriver.exe')

#浏览器最大化
driver.maximize_window()

#打开测试页面period5-2.html
driver.get("http://localhost/period5-2.html")
time.sleep(1)

#滚动条移动到页面底部
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(2)

#滚动条移动到页面顶部
driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")
time.sleep(2)

#滚动条移动到元素顶部与窗口顶部对齐的位置
element = driver.find_element_by_class_name("part1")
driver.execute_script("arguments[0].scrollIntoView();",element)
time.sleep(2)

#滚动条移动到元素底部与窗口底部对齐的位置
element = driver.find_element_by_class_name("part2")
driver.execute_script("arguments[0].scrollIntoView(false);",element)
time.sleep(2)

#关闭浏览器，并结束进程，如果浏览器有多个窗口，则关闭多个窗口并停止进程
driver.quit()