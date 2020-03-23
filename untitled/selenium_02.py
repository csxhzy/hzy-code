from selenium import webdriver
from time import sleep
driver=webdriver.Ie()
driver.get("https://www.126.com")
sleep(2)

driver.find_element_by_id("switchAccountLogin").click()
login_frame=driver.find_element_by_css_selector("iframe[id^='x-URS-iframe']")
driver.switch_to.frame(login_frame)
driver.find_element_by_name("email").send_keys("sunnyhzy0317")
driver.find_element_by_name("password").send_keys("sun110")
driver.find_element_by_id("dologin").click()
driver.switch_to.default_content()
