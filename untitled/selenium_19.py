from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')

# 对当前窗口截图，并指定图片的保存位置
driver.save_screenshot("C:/Users/Administrator/Desktop/baidu_img.png")