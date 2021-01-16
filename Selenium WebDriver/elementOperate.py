#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
项目名称 ：PythonWebTest 
脚本名称 ：elementOperate.py
开发环境 ：PyCharm 
开发人员 ：林
脚本功能：对象操作
编写时间 ：2020/11/22 15:02 
'''

from selenium import webdriver
import time

#浏览器初始化操作
driver = webdriver.Chrome(executable_path="./driver/chromedriver.exe")
driver.maximize_window()

#打开测试页面
driver.get("http://localhost/FirstProject.html")

#输入文本内容:输入邮箱地址
driver.find_element_by_id("email").send_keys("12345567@163.com")
time.sleep(2)

#获取邮箱地址的属性placeholder
placeholder = driver.find_element_by_id("email").get_attribute("placeholder")
print("placeholder:"+placeholder)

#清空文本内容
driver.find_element_by_id("email").clear()
time.sleep(2)

#输出登录按钮的文本值
text = driver.find_element_by_class_name("text").text
print("text:"+text)

#点击【登录】
#driver.find_element_by_class_name("text").click()

driver.get("http://localhost/period5-3.html")

#判定元素是否显示
text01 = driver.find_element_by_class_name("show-text").is_displayed()
print("text01:"+str(text01))

#判定元素是否勾选
text02 = driver.find_element_by_name("python").is_selected()
print("text02:"+str(text02))

#判定元素是否可编辑
text03 = driver.find_element_by_class_name("disabled-text").is_enabled()
print("text03:"+str(text03))

#关闭浏览器
driver.quit()