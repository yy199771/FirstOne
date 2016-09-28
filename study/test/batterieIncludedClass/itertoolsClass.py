#coding=utf-8
# 2016-06-27
__author__ = 'yangyang'

'''
itertools:

Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数。
首先，我们看看itertools提供的几个“无限”迭代器：

'''
import itertools
# natuals = itertools.count(1)
# for n in natuals:
#     print n

'''
因为count()会创建一个无限的迭代器，所以上述代码会打印出自然数序列，根本停不下来，只能按Ctrl+C退出。
cycle()会把传入的一个序列无限重复下去：
'''

# cs = itertools.cycle('ABC')
# for c in cs:
#     print c

'''
repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数：
'''

# ns = itertools.repeat('A',10)
# for n in ns:
#     print n

'''
无限序列只有在for迭代时才会无限地迭代下去，如果只是创建了一个迭代对象，
它不会事先把无限个元素生成出来，事实上也不可能在内存中创建无限多个元素。

无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列：
'''
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x<=10, natuals)
for n in ns:
    print n

'''
chain():可以把一组迭代对象串联起来，形成一个更大的迭代器：
'''
for c in itertools.chain('ABC','DEF'):
    print c

'''
groupby()把迭代器中相邻的重复元素挑出来放在一起：
'''
for key, group in itertools.groupby('AAABBBCCAAA'):
    print key, list(group)
print '----------------groupby-----------------'
for key, group in itertools.groupby('AaaBbBcCAAa',lambda c:c.upper()):
    print key,list(group)

'''
imap()和map()的区别在于，imap()可以作用于无穷序列，
并且，如果两个序列的长度不一致，以短的那个为准。
'''
r = map(lambda x: x*x,[1,2,3])
print r

for x in r:
    print x
print '---------------imap----------------------'
r = itertools.imap(lambda x: x*x, itertools.count(1))
for n in itertools.takewhile(lambda x:x<100,r):
    print n