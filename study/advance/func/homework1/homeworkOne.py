#coding=utf-8

'''
习题：

1.定义一个方法 func，该func可以引入任意多的整型参数，结果返回其中最大与最小的值。
2.定义一个方法func，该func可以引入任意多的字符串参数，结果返回（长度）最长的字符串。
3.定义一个方法get_doc(module)，module参数为该脚本中导入或定义的模块对象，该函数返回module的帮助文档。
例 print get_doc(urllib),则会输出urllib这个模块的帮助文档。
4.定义一个方法get_text(f),f参数为任意一个文件的磁盘路径，该函数返回f文件的内容。
5.定义一个方法get_dir(folder),folder参数为任意一个文件夹，该函数返回folder文件夹的文件列表。提示（可以了解python的glob模块）
'''

# 1:

def MaxMinNum(*num):
    for x in num:
        if not isinstance(x, int):
            return '请输入数字!'
    print type(num)
    a = list(num)
    return max(a), min(a)

# 2:

def MaxLengStr(*sen):
    for s in sen:
        if not isinstance(s,str):
           return '请输入字符串!'

    a = sorted(sen, key=lambda k:len(k))
    return 'MaxStr is %s ' %(len(a[-1]))


# 3:
import os

def get_doc(module):
    a = 'pydoc %s' % module
    m = os.popen(a).read()
    return m


n = MaxMinNum(111,2,3,4,32,42,35,12)
print n

s = MaxLengStr('ad','fafs','fdasfdsfsa','fasfs')
print s

q3 = get_doc('aaa')
print q3