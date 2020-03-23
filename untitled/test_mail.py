from time import sleep
from selenium import webdriver
from module import Mail

driver = webdriver.Firefox()
driver.get("http://www.126.com")
# 调用Mail类并传入driver驱动
mail = Mail(driver)

# 登录
mail.login()

# 登录之后的动作...
sleep(5)

# 退出
mail.logout()

driver.quit()