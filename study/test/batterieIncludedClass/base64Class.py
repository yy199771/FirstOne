#coding=utf-8
# 206-06-27
__author__ = 'yangyang'
'''
Base64是一种用64个字符来表示任意二进制数据的方法。
用记事本打开exe、jpg、pdf这些文件时，我们都会看到一大堆乱码，
因为二进制文件包含很多无法显示和打印的字符，
所以，如果要让记事本这样的文本处理软件能处理二进制数据，就需要一个二进制到字符串的转换方法。
Base64是一种最常见的二进制编码方法。

Base64的原理很简单，首先，准备一个包含64个字符的数组：
'''

import base64

s64en = base64.b64encode('binary\x00string')
print 's64en:', s64en

s64de = base64.b64decode(s64en)
print 's64de:', s64de

'''
由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，
所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_：
'''
ss64en = base64.b64encode('i\xb7\x1d\xfb\xef\xff')
print 'ss64en:', ss64en
urlS64en = base64.urlsafe_b64encode('i\xb7\x1d\xfb\xef\xff')
print 'urlS64en:', urlS64en

