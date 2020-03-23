from selenium import webdriver

from time import sleep

#打开火狐浏览器

driver=webdriver.Firefox()

driver.get("http://www.baidu.com")

#设置浏览器窗口大小

driver.set_window_size(600,600)

#文本框里输入值

driver.find_element_by_id("kw").send_keys("测试")

#点击百度一下按钮

driver.find_element_by_id("su").click()

#暂停5秒时间

sleep(5)

#设置网页滚动条停留的位置

js="window.scrollTo(100,450);"

#执行javascript代码

driver.execute_script(js)