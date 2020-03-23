# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

caps = {}
caps["automationName"] = "Appium"
caps["platformName"] = "Android"
caps["platformVersion"] = "7.0"
caps["appPackage"] = "com.android.calculator2"
caps["appActivity"] = ".Calculator"
caps["deviceName"] = "emulator-5554"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

TouchAction(driver).tap(x=618, y=836).perform()
TouchAction(driver).tap(x=904, y=1622).perform()
TouchAction(driver).tap(x=416, y=1345).perform()
TouchAction(driver).tap(x=660, y=1584).perform()

driver.quit()