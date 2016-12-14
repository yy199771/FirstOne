#coding=utf-8
'''
1 已知字符串:
info = '<a href="http://www.baidu.com">baidu</a>'
用正则模块提取出网址："http://www.baidu.com"和链接文本:"baidu"
2 字符串："one1two2three3four4" 用正则处理，输出 "1234"
3 已知字符串：text = "JGood is a handsome boy, he is cool, clever, and so on..." 查找所有包含'oo'的单词。
4 为什么在unix里，grep后面的正则有些时候要加引号，有些时候不需要。
'''

import re
# 1.
info = '<a href="http://www.baidu.com">baidu</a>'
pattern = re.compile('http.*?com')
pattern1 = re.compile('>\w+')
items = re.findall(pattern1, info)
for item in items:
    print items[0].split('>')

# 2.
str = 'one1two2three3four4'
pattern = re.compile('\d+')
print re.findall(pattern, str)