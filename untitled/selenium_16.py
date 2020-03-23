from selenium import webdriver
driver=webdriver.Ie()
driver.get("http://www.baidu.com")
driver.set_window_size(800,600)
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
#通过javascript设置浏览器窗口的滚动条位置
js="window.scrollTo(100,450);"
driver.execute_script(js)