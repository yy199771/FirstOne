#coding=utf-8
__author__ = 'yangyang'

#字符串不可变。

a = 'abcd'
# 返回找到的字符换索引
b = a.find('d')
print a[3]

c ='efhj'
# index如果找不到，会抛出error
d = c.index('j')
print c[d]

e = 'jay'
f = 'Python'
g = e,f
print 'my name is ' + e +',' + 'i love ' + f
print 'my name is %s , i love %s' %(e,f)
print 'my name is %s , i love %s' %g

# join:添加元素,添加内容必须是字符串。
seq = ['1','2','3','4','5']
sep = '+'
print sep.join(seq)

dirs = '','usr','bin','env'
print '/'.join(dirs)
print 'C:'+ '\\'.join(dirs)

aaa = 'abc'
print 'abc'+'d'

# split:分割字符串
aa = '1+2+3+4+5'
print aa.split('+')

# ------------------------------
# replace替换字符串
bb = 'This is a test.'
print bb.replace('is','eez')
# translate和replace方法类似，只处理单个字符。速度快
# translate需要先创建一张table表。
from string import maketrans
dd = 'That is a tester.'
table = maketrans('at','ZZ')
print dd.translate(table)

# ------------------------------

# strip 返回去除两侧（不包括内部空格的字符串）
cc = '        internal whitespace is kept     '
print cc.strip()