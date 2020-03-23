import time
from selenium import webdriver
driver=webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")

#获得百度搜索窗口句柄
search_windows=driver.current_window_handle
driver.find_element_by_link_text("登录").click()
driver.find_element_by_link_text("立即注册").click()

#获得当前所有打开的窗口句柄
all_handles=driver.window_handles

#进入注册窗口
for handle in all  handles:
    if handle !=search_windows:
        driver.switch_to.window(handle)
        print(driver.title)
        driver.find_element_by_name("userName").send_keys("")