import time
import unittest
import yagmail
from HTMLTestRunner import HTMLTestRunner
#把测试报告作为附件发送到指定邮箱
def send_mail(report):
    yag = yagmail.SMTP(user="sunnyhzy0317@126.com",
                       password ="hzy110",
                       host='smtp.126.com')
    subject = "主题，自动化测试报告"
    contents = "正文，请查看附件。"
    yag.send('1658489684@qq.com',subject,contents,report)
    print('email has send out!')
if __name__=='__main__':
   test_dir='./test_web'
   suits=unittest.defaultTestLoader.discover(test_dir,pattern='test_baidu3.py')
#取当前时间
now_time = time.strftime("%Y-%m-%d %H_%M_%S")
html_report='./test_report/'+ now_time +'result.html'
fp=open(html_report,'wb')
runner=HTMLTestRunner(stream=fp,title="百度搜索测试报告",description="运行环境：Windows10,Chrome浏览器")
runner.run(suits)
fp.close()
send_mail(html_report)