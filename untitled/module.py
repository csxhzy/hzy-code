class Mail:
    def __init__(self,driver):
        self.driver = driver
    def login(self):
        """"登录"""
        self.driver.find_element_by_id("switchAccountLogin").click()
        login_frame = self.driver.find_element_by_css_selector('iframe[id^="x-URS-iframe"]')
        self.driver.switch_to.frame(login_frame)
        self.driver.find_element_by_name("email").clear()
        self.driver.find_element_by_name("email").send_keys("sunnyhzy0317@126.com")
        self.driver.find_element_by_name("password").clear()
        self.driver.find_element_by_name("password").send_keys("sun110")
        self.driver.find_element_by_id("dologin").click()
    def logout(self):
        """退出"""
        self.driver.switch_to.default_content()
        self.driver.find_element_by_partial_link_text("退出").click()