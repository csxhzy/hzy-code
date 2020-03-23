import yagmail

#连接邮箱服务器
yag = yagmail.SMTP(user="sunnyhzy0317@126.com", password="hzy110", host='smtp.126.com')

# 邮箱正文
contents = ['This is the body, and here is just text http://somedomain/image.png',
            'You can find an audio file attached.']

# 发送邮件
yag.send('sun1658489684@126.com', 'send email subject', contents)