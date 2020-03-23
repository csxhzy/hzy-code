from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

desired_caps = {
        'platformName': 'Android',
        'deviceName': 'emulator-5554',
        'platformVersion': '7.0',
        'appPackage': 'com.android.contacts',
        'appActivity': '.activities.PeopleActivity',
        'noReset':True
    }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
#单击添加按钮
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.Button[1]
")