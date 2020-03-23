import os
from selenium import webdriver
# 获取到火狐浏览器的配置选项
fp=webdriver.FirefoxProfile()
# 设置成 0 代表下载到浏览器默认下载路径， 设置成 2 则可以保存到指定目录。
fp.set_preference("browser.download.folderList",2)
# 配置火狐浏览器的下载路径
fp.set_preference("browser.download.dir", os.getcwd())
# 指定要下载页面的 Content-type 值， “binary/octet-stream” 为文件的类型
# 响应头中的Content-Type:binary/octet-stream
fp.set_preference("browser.helperApps.neverAsk.saveToDisk","binary/octet-stream")
driver=webdriver.Firefox(firefox_profile=fp)
driver.get("https://pypi.org/project/selenium/#files")
driver.find_element_by_partial_link_text("selenium-3.141.0.tar.gz").click()
