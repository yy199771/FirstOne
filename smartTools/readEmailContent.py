#coding=utf-8
__author__ = 'yangyang'

import getpass, imaplib

#输入邮件地址，口令和pop3服务器地址：
email_adr = 'yangyang@we.com'
password = '1@qWaSzX'
exchange_server = 'mail.we.com'

#连接到pop3服务器：
server = imaplib.IMAP4(exchange_server)
print server
try:
    try:
        # 登录
        server.login(email_adr,password)
    except Exception,e:
        print 'login error: %s' % e
        server.close()
    # 获取邮箱文件夹列表。
    aa = server.list()
    print type(aa)
    for a in aa[1]:
        print a
    print '--------------------------'
    # 获取company文件夹中的邮件数量。
    result, n = server.select('INBOX/company')
    print 'result: %s' % result
    print 'n: %s' % n


    typ, data = server.search(None, 'ALL')
    print '--------------------------'
    print type(data)
    print data[0]
    print type(data[0])
    print type(list(data[0]))
    for num in data[0].split( ):
        print num
        #typ, data = server.fetch(num,'(RFC822)')
        #print 'Message %s\n%s\n' % (num, data[0][1])


    print '--------------------------'
    for x in n:
        print 'name: %s' % x
except Exception,e:
    print 'imap error: %s' % e
    server.close()

# 获取字符编码方式
def get_charset(message, default='ascii'):
    #Get the message charset
    return message.get_charset()
    return default

#typ, message = server.search(None,'(FROM,"IT管理部")')

#type, data = server.search(None,'(SUBJECT "lync代替工具IMO来啦！")')
# 可以打开或关闭调试信息:
# server.set_debuglevel(1)
# 可选:打印POP3服务器的欢迎文字:


#身份认证：
#server.user(email_adr)
#server.pass_(password)

#stat()返回所有邮件的数量和所占空间：
#print 'Message: %s. Size: %s', %server.stat()


