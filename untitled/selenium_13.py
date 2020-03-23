from selenium import webdriver
from time import sleep
driver = webdriver.Firefox()
driver.get('https://www.testclass.cn/test_html/UpFile.html')
sleep(5)

# 定位上传按钮，添加本地文件;
upload = driver.find_element_by_id("up_file")
upload.send_keys(r'C:\\Users\Administrator\Desktop\upload_file.jpg')

try:
   Alert = driver.switch_to.alert    
    #获取Alert的Text值；
   print(Alert.text)
   sleep(5)
    #确定Alert弹出框
   Alert.accept()
finally:
        pass