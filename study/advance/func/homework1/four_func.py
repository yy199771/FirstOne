#coding=utf-8

'''
2、lambda
    1、是一个表达式
    2、它没有名称,存储的也不是代码块,而是表达式
    3、它被用作执行很小的功能,不能在里面使用条件语句。

3、参数总结
    1、位置匹配
    2、关键字匹配
    3、收集匹配
        1、元组收集
        2、字典收集

4、接触递归
    1、递归是调用自身
    2、理解下面的函数
'''

d = lambda x:x+1 if x > 0 else 'error!'

g = lambda x:[(x, i) for i in xrange(0,10)]

t = [1,2,3,4,5]

x =filter(lambda x:x > 3, t)

print d(2)
print d(4)
print d(5)
print d(-2)
print g(3)

print x

def e(x):
    return x+1

# 3:

def func31(arg1,arg2,arg3):
    return arg1,arg2,arg3

def func32(k1='',k2=None,k3=''):
    return k1, k2, k3

print func31(1,2,3)
print func32(k1=3,k3=7,k2=19)


'''
* kargs 元组

** kwargs 字典

参数位置:
1、先是位置匹配的参数
2、再是关键字匹配的参数
3、收集匹配的元组参数
4、收集匹配的关键字参数


'''

def func33(*kargs, **kwargs):
    return kargs

print func33(1,2,3,4,5,6,7,8,9,[1,2,3,4,5],{1:2,3:4,5:6})


# 4

def func41(i):
    if i <100:
        return i + func41(i+1)
    return i

print func41(10)