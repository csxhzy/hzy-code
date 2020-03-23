#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from time import sleep
import os

def setFireFoxProfile():
    '''#配置Firefox：修改firefox_profile
    1. 配置保存文件的路径
    2. 设置文件是否保存在默认下载文件夹中
    3. 设置文件类型允许下载
    '''
    # 获取到火狐浏览器的配置选项
    profile = webdriver.FirefoxProfile()
    # 配置火狐浏览器的下载路径
    profile.set_preference("browser.download.dir",os.getcwd()+'\\download')
    # 设置成 0 代表下载到浏览器默认下载路径， 设置成 2 则可以保存到指定目录。
    profile.set_preference("browser.download.folderList",2)
    # 指定要下载页面的 Content-type 值， “binary/octet-stream” 为文件的类型
    # 响应头中的Content-Type: application/x-zip-compressed（zip压缩包）     image/png（png图片）
    profile.set_preference("browser.helperApps.neverAsk.saveToDisk","application/x-zip-compressed")
    # 设置不弹出窗口
    profile.set_preference("profile.default_content_settings.popups", 0);
    #实例化浏览器webdriver
    driver = webdriver.Firefox(firefox_profile=profile)
    #设置全局等待时间
    driver.implicitly_wait(10)
    #最大浏览器窗口
    driver.maximize_window()
    return driver

def loadAndDownload(driver):
    '''点击下载
    :param driver: 浏览器对象
    :return: None
    '''
    # 打开bugfree主页（前置条件:已搭建bugfree）
    driver.get(r'http://192.168.7.19:8080/bugfree')
    driver.find_element_by_id('LoginForm_username').clear()
    # 输入用户名
    driver.find_element_by_id('LoginForm_username').send_keys('admin')
    driver.find_element_by_id('LoginForm_password').clear()
    # 输入密码
    driver.find_element_by_id('LoginForm_password').send_keys('123456')
    # 登录
    driver.find_element_by_id('SubmitLoginBTN').click()
    sleep(3)
    #选择产品
    ele = driver.find_element_by_id('product_name')
    Select(ele).select_by_visible_text('Sample Product')
    sleep(3)
    #通过部分文本进行定位:  标签名[contains(.,'部分文本值')]
    #d.find_element_by_xpath('td[contains(.,\'12\')]')
    #ActionChains(d).click_and_hold(d.find_element_by_xpath('//td[contains(.,\'12\')]')).perform()
    '''
        contains：模糊查询
        .,  :根据文本匹配
        ../  ：父节点
        //td[contains(.,\'12\')]：  查找HTML页面上标签名为td的且文本包含12的元素
    '''
    # ../元素的父节点路径
    driver.find_element_by_xpath('//td[contains(.,\'12\')]/../td[5]/span/a').click()
    # 切换到bug详情页面
    driver.switch_to.window(driver.window_handles[-1])
    # 定位到zip文件，并点击
    driver.find_element_by_css_selector('#file3>a').click()


if __name__ == '__main__':
    # 调用配置并返回浏览器
    driver = setFireFoxProfile()
    # 调用点击下载
    loadAndDownload(driver)