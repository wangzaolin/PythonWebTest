from selenium import webdriver
import time

#chrome浏览器并操作
driver = webdriver.Chrome(executable_path='./driver/chromedriver.exe')
driver.get("http://localhost/FirstProject.html")
time.sleep(3)
driver.find_element_by_id("email").send_keys("1234567@qq.com")
time.sleep(3)
driver.find_element_by_name("password").send_keys("123456")
time.sleep(3)
driver.find_element_by_class_name("text").click()
time.sleep(3)
driver.quit()

#ie浏览器操作
driver02 = webdriver.Ie(executable_path='./driver/IEDriverServer.exe')
driver02.get("http://www.baidu.com")
driver02.quit()

#Firefox浏览器操作
driver03 = webdriver.Firefox(executable_path='./driver/geckodriver.exe')
driver03.get("http://www.baidu.com")
driver03.quit()
