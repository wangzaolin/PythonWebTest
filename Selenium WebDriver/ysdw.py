##############功能：元素定位--定位单个元素########################

from selenium import webdriver
from time import sleep

#打开chrome浏览器
driver =webdriver.Chrome(executable_path="./driver/chromedriver.exe")
#打开测试页面peroid3.html
driver.get("http://localhost/peroid3.html")
#sleep(3)
#id定位:获取id定位搜索框，输出搜索框maxlength属性值
max_length = driver.find_element_by_id("search").get_attribute("maxlength")
print("maxlength="+max_length)

#class定位：通过class定位检索按钮，输出检索按钮的value值
text = driver.find_element_by_class_name("btn-search").get_attribute("value")
print("text:"+text)

#name定位：通过name定位多选框，输出多选框的type属性值
type = driver.find_element_by_name("language").get_attribute("type")
print("type:"+type)

#tag定位：通过tag_name定位【tag定位】元素，并输出元素文本值
tag_text = driver.find_element_by_tag_name("h4").text
print("tag_text:"+tag_text)

#xpath定位：通过xpath定位【xpath定位】元素，并输出元素文本值
#绝对路径：/html/body/div/p
xpath_text = driver.find_element_by_xpath("/html/body/div/p").text
print("xpath_text:"+xpath_text)

#相对路径：//标签值[@属性=‘属性值'],例如://input[@id='search'],定位搜索文本框元素
xpath_text02 = driver.find_element_by_xpath("//input[@id='search']").get_attribute("maxlength")
print("xpath_text02:"+xpath_text02)

#相对路径模糊定位：//标签值[contains(@属性,属性值)],例如：//input[contains(@id,'sear')]，定位搜索文本框
xpath_text03 = driver.find_element_by_xpath("//input[contains(@id,'sear')]").get_attribute("maxlength")
print("xpath_text03:"+xpath_text03)

#link定位：通过文字链接的文本值定位元素Tynam,并输出href属性值
link_href = driver.find_element_by_link_text("Tynam").get_attribute("href")
print("link_href:"+link_href)

#partial_link定位：通过部分文字链接的文本值定位元素Partial link定位，并输出完整文本值
partial_link_text = driver.find_element_by_partial_link_text("link定位").text
print("partial_link_text:"+partial_link_text)

#css定位：
# 通过class属性定位【css定位】元素，并输出文本值
css_text = driver.find_element_by_css_selector(".css").text
print("css_text:"+css_text)

#通过id元素定位搜索框，并输出maxlength
css_maxlength = driver.find_element_by_css_selector("#search").get_attribute("maxlength")
print("css_maxlength:"+css_maxlength)

#通过name元素定位多选框，并输出type属性值
css_name = driver.find_element_by_css_selector("[name='language']").get_attribute("type")
print("css_name:"+css_name)

#定位div下的第一个子元素，并输出其type值
css_firstchild = driver.find_element_by_css_selector("div:first-child").text
print("css_firstchild:"+css_firstchild)

#定位div下class=css的元素，并输出文本值
css_text = driver.find_element_by_css_selector("div>.css").text
print("css_text:"+css_text)

#关闭浏览器
driver.close()