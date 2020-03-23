from time import sleep
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.126.com")

# 登录
sleep(2)
driver.find_element_by_id("switchAccountLogin").click()
login_frame=driver.find_element_by_css_selector('iframe[id^="x-URS-iframe"]')
driver.switch_to.frame(login_frame)
driver.find_element_by_name("email").clear()
driver.find_element_by_name("email").send_keys("sunnyhzy0317@126.com")
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("sun110")
driver.find_element_by_id("dologin").click()
driver.switch_to.default_content()
sleep(5)
driver.find_element_by_partial_link_text("退出").click()
driver.quit()