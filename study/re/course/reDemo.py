#coding=utf-8

'''
正则表达式，是字符串检索引擎，最早起源于unix。

1.unix下的正则 awk grep egrep
2.正则的几个基本概念

[0-9] \d 全部数字

\w 单词类字符 a-z A-Z 0-9 _
\W 非单词类字符

{2}  {n}  前面的表达式匹配n次
{0,2} {m,n} 前面的表达式匹配m到n次

+ 前面的表达式，出现1到无限次  最少，出现1次
? 前面的表达式，出现0到1次  最多，出现1次
* 前面的表达式，出现0到无限次 出现不出现，都没关系
$：完全匹配。
^：以X开头

3.python里的正则模块 re
4.一些基本操作

4.1 一次取配 match:"hello lilei"  r'(\w+) (\w+)'
4.2 切割 split
4.3 查找全部 findall
4.4 finditer 迭代器什么的最有爱了
'''

import re

# match 匹配



# 切割

pattern_str = re.compile('\d+')
pattern_num = re.compile('\d+')
str = 'a1b2c3d4'
num = '1a2b3c4d'

re_str = re.split(pattern_str, str)
print re_str
re_num = re.split(pattern_num, num)
print re_num