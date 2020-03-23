from selenium import webdriver
driver=webdriver.Firefox()
#引入ActionChains类
from selenium.webdriver import ActionChains

driver.get("http://bbs.boox.com/forum.php")

#定位到要悬停的元素
above=driver.find_element_by_class_name("nickname")
#对定位到的元素执行鼠标悬停操作
ActionChains(driver).move_to_element(above).perform()
driver.find_element_by_xpath("/html/body/div[3]/div[1]/div/div[3]/div/div[2]/ul/li[1]/a").click()
