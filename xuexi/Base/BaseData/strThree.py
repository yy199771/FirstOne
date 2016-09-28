#coding=utf-8
__author__ = 'yangyang'

# 模版字符串
from string import Template
# 完成替换
s = Template('$x, glorious $x!')
print s.substitute(x = 'slurm')

# 替换单词的一部分
x = Template("It's ${x}tastic!")
print x.substitute(x = 'slurm')

a = 'pyer'
b = 'apple'
s = a,b
print 'my name is %s, i love %s.' %s

'''
fileadd = 'E:\\python_script\\testTxt.txt'
try:
    open(fileadd)
except:
'''