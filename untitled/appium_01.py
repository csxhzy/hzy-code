from appium import webdriver

desired_caps = {
        'platformName': 'Android',
        'deviceName': 'emulator-5554',
        'platformVersion': '7.0',
        'appPackage': 'com.android.calculator2',
        'appActivity': 'com.android.calculator2.Calculator'
    }
driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.find_element_by_id("com.android.calculator2:id/digit_1").click()
driver.find_element_by_id("com.android.calculator2:id/digit_5").click()
driver.find_element_by_id("com.android.calculator2:id/digit_9").click()
driver.find_element_by_id("com.android.calculator2:id/del").click()
driver.find_element_by_id("com.android.calculator2:id/op_add").click()
driver.find_element_by_id("com.android.calculator2:id/digit_6").click()
driver.find_element_by_id("com.android.calculator2:id/eq").click()
driver.quit() #退出
