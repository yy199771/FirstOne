#coding=utf-8
__author__ = 'yangyang'

#    1
a = [1,2,3,4,5,333,11,44]
print a[3:6]
#    2
a = [1,2,3]
b = [4,5,6]
print a + b
a.extend(b)
print a

#    3.
#a = [1,99,33,44,55,22]

#    4.
print [x for x in range(2,101) if x > 20 and x % 2 ==0]
