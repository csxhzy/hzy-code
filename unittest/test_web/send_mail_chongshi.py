import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 发送邮箱服务器
smtpserver = 'smtp.qq.com'
# 发送邮箱用户/密码
user = '1658489684@qq.com'
password = 'zujzjvbkqbtybhih'
# 发送邮箱
sender = '1658489684@qq.com'
# 接收邮箱
receiver = 'sun1658489684@126.com'
# 发送邮件主题
subject = 'Python email test'

# 编写HTML类型的邮件正文
msg = MIMEText('<html><h1>你好！</h1></html>','html','utf-8')
msg['Subject'] = Header(subject, 'utf-8')


# 连接发送邮件
smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(user, password)
smtp.sendmail("1658489684@qq.com", "sunnyhzy0317@126.com",msg.as_string())
smtp.quit()