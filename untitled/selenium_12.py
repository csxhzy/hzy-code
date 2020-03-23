from time import sleep
from selenium import webdriver
from selenium.webdriver.support.select import Select

#引入ActionChains类
from selenium.webdriver import ActionChains

driver=webdriver.Ie()
driver.get("http://www.baidu.com")

#定位到要悬停的元素
above=driver.find_element_by_link_text("设置")
#对定位到的元素执行鼠标悬停操作
ActionChains(driver).move_to_element(above).perform()
#打开搜索设置
driver.find_element_by_class_name("setpref").click()
#搜索结果显示条数
sel=driver.find_element_by_css_selector("#nr")
#value="20"
Select(sel).select_by_value("20")
sleep(5)
Select(sel).select_by_visible_text("每页显示50条")
sleep(5)
Select(sel).select_by_index(0)