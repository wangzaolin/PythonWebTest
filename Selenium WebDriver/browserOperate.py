#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
项目名称 ：PythonWebTest 
脚本名称 ：browserOperate.py
开发环境 ：PyCharm 
开发人员 ：林
开发功能：浏览器操作
编写时间 ：2020/11/22 12:59 
'''

from selenium import webdriver
import time

#浏览器初始化
driver = webdriver.Chrome(executable_path='./driver/chromedriver.exe')

#浏览器最大化
driver.maximize_window()

#设置浏览器的宽和高
#driver.set_window_size(500,900)

#访问网页
driver.get("https://www.baidu.com/")

#浏览器后退
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
time.sleep(1)
driver.back()

#浏览器前进
time.sleep(1)
driver.forward()

#浏览器刷新
time.sleep(1)
driver.refresh()

#获取页面title
driver.get("http://www.51testing.com")
title01 = driver.title
print("title01:"+title01)
driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[1]/div[1]/ul/li[1]/a").click()
title02 = driver.title
print("title02:"+title02)

#获取当前页面url
url = driver.current_url
print("url:"+url)

#获取页面源码
page_source = driver.page_source
print("pageSource:"+page_source)

#关闭浏览器当前窗口
driver.close()
time.sleep(3)

#关闭浏览器，并结束进程，如果浏览器有多个窗口，则关闭多个窗口并停止进程
driver.quit()