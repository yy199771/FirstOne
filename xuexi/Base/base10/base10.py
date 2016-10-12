#coding=utf-8

#一: 已知：元组 a = (1,2,3) 利用list方法，输出下面的结果：(1,2,4)

a = (1,2,3)

b = list(a)
b = [1,2,4]

a = tuple(b)
print a


print [x for x in range(1,11)]

#for x in range(1,11):
#    print x, ' love python'

aa = [1,2,3]
bb = aa[:]
del aa

print bb
print 'abc test!'
