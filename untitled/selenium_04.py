from time import sleep
from selenium import webdriver
#引入ActionChains类
from selenium.webdriver import ActionChains
driver=webdriver.Firefox()
driver.get("http://www.baidu.com")

#定位到要悬停的元素
above=driver.find_element_by_link_text("设置")
#对定位到的元素执行鼠标悬停操作
ActionChains(driver).move_to_element(above).perform()

#打开搜索设置
driver.find_element_by_class_name("setpref").click()
sleep(2)

#保存设置
driver.find_element_by_class_name("prefpanelgo").click()

#获取警告框
alert=driver.switch_to.alert

#获取警告框提示信息
alert_text=alert.text
print(alert_text)
sleep(5)

#提取警告框
alert.accept()

