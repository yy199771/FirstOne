#coding=utf-8
__author__ = 'yangyang'

from email.mime.text import MIMEText
import smtplib
import datetime
from email.header import Header

#输入email地址和口令：
from_addr = 'yangyang@we.com'
password = 'XXXXXX'

# 输入收件人地址：
to_addr = 'yangyang@we.com'

#标题与内容
subject = '杨阳测试邮件'

msg = MIMEText('hello', 'plain', 'utf-8')

#msg['Subject'] = Header(subject,'uft-8')
msg['Subject'] = 'subject'
msg['From'] = 'hello<yangyang@we.com>'
msg['To'] = 'yangyang@we.com'
smtp_server = 'mail.we.com'

server = smtplib.SMTP() #smtp协议默认端口是25
server.connect(smtp_server)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()