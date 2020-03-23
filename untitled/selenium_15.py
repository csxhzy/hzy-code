from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://www.baidu.com")
cookie=driver.get_cookies()
print(cookie)
#添加cookie信息
driver.add_cookie({'name':'key-aaaaaaa','value':'value-bbbbbbb'})
#遍历指定的cookies
for cookie in driver.get_cookies():
    print("%s -> %s" % (cookie['name'],cookie['value']))