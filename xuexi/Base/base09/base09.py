#coding=utf-8
__author__ = 'yangyang'

#    list 序列
# 检查成员资格
permissions = 'rwafsffdadf'
d = 'sff' in permissions
print d

permissions1 = [1,2,3,4,5,6,'a','b','c']
e = 'a' in permissions1
print e
print len(permissions1)
print max(permissions1)
print min(permissions1)

a = [1,2,3,4,5]
b = a * 2
print a[-3:]
print b

print 2 in a
print 6 in b

# 步长
number1 = [1,2,3,4,5,6,7,8,9,0]
print number1[1:9:3]
print number1[::-2]

# 序列相加
a = [1,2,3]
b = [4,5,6]
print a+b


# list函数
#   str与list相互转换
#   list 将类型转换成序列。
c = list('str')
c1 = c.append('x')
print c
#print c1
#通过''.join(c)，将序列再转成字符串。
d = ''.join(c)
print d
del(c[0])
print c


#分片赋值
name = list('Perl')
print name
name[2:3] = list('a')
print name
name[2:] = list('XX')
print name
#   通过分片方式在不替换任何原有元素的情况下插入新的元素
numbers = [1,5]
numbers[1:1] = [2,3,4,'x','y','z']
print numbers
numbers2 = [1,2,3,4,5]
#   替换空的分片
numbers2[1:4] = []
print numbers2

# 列表的方法
#     append：在列表末尾追加新的对象。
lst = [1,2,3]
lst.append(4)
print lst
#    count：某个元素在列表中的出现的次数。
count = ['to','be','or','to','be']
counts = count.count('to')
print counts
#    extend:在列表尾一次性追加另一个序列中的多个值。
a = [1,2,3]
b = [4,5,6]
print a + b
print a
a.extend(b)
print a
#    index 从列表中找出某个值第一个匹配项的索引位置
kingths = ['We','are','the','knights','who','say','ni']
print kingths.index('who')
#    insert 用于将对象插入到列表中
number2 = [1,2,3,5,6,7]
number2.insert(3,'four')
print number2
#     pop移除列表中的一个元素（默认是最后一个），并且返回该元素的值：
#     pop是唯一一个既能修改列表，又返回元素值（除了None）的列表方法。
x = [1,2,3]
x.pop(1)
print x

#   通过此方式实现栈。
#   后进先出法
x = [1,2,3]
x.append(x.pop())
print x
#   先进先出法
y = [4,5,6]
x.insert(0,x.pop())
print y
#    remove移除列表中某个值的第一个匹配项
z = ['We','are','the','knights','who','say','ni']
z.remove('the')
print z
#    reverse将列表元素反向存放
z.reverse()
print z
#    sort用于在“原位置”对列表进行排序，直接改变列表，而不是返回一个列表副本.
#    另外一种获取原位置和副本的方式。sorted
xx = [1,4,65,23,3,54,13,6,87,542]
yy = xx[:]
xx.sort()
print yy
print xx

xx = [3,4,2,8,3,90,42,5,3]
yy = sorted(xx)
print xx
print yy
#    高级排序
print cmp(32,49)
print cmp(44,22)
number3 = [4,1,7,8]
number3.sort()
print number3

x = ['We','are','the','knights','who','say','ni']
x.sort(key=len)
print x

#    元组：不可变序列
x = (1,2,3)
print type(x)
y = list(x)
print y
#    tuple函数
x = ['We','are','the','knights','who','say','ni']
y = tuple(x)
print y
