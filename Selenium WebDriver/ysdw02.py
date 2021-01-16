"""
##############定位多个元素##################
"""

from selenium import webdriver

from time import sleep

#打开chrome浏览器
driver =webdriver.Chrome(executable_path="./driver/chromedriver.exe")
#打开测试页面peroid3.html
driver.get("http://localhost/peroid4.html")

#定位标签为label的一组元素，并输出元素文本值
elements = driver.find_elements_by_tag_name("label")

text01 = elements[0].text
print("text01:"+text01)

for element in elements:
    print(element.text)

#关闭浏览器
driver.close()