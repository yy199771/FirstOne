#coding=utf-8
'''
1、别管那么多复杂的,先直接把功能实现了
2、抽象成函数:
    命名规范:
        1、下划线命名法 get_doc
        2、驼峰命名法 getDocFromUrl
    伪代码:
    参数默认值:
        1、更省事,
        2、更可配置
3、将函数变得更健壮,让它可以跑很多地方:
    1、假设你写的函数是要交给你的基友用 --》功能完整
    2、假设你写的函数是要交给你的基友用 --》异常处理完善

4、测试:
    1、asset
    2、对函数返回进行一个值和类型的测试
    3、单元测试
'''


'''
习题:
今天习题：
1 定义一个方法get_fundoc(func),func参数为任意一个函数对象，返回该函数对象的描述文档，如果该函数没有描述文档，则返回"not found"
2 定义一个方法get_cjsum(),求1-100范围内的所有整数的平方和。返回结果为整数类型。
3 定义一个方法list_info(list), 参数list为列表对象，怎么保证在函数里对列表list进行一些相关的操作，不会影响到原来列表的元素值，比如：

a = [1,2,3]

def list_info(list):
    要对list进行相关操作，不能直接只写一句return[1,2,5]，这样就没意义了

print list_info(a):返回结果：[1,2,5]

print a 输出结果：[1,2,3]

写出函数体内的操作代码。

4 定义一个方法get_funcname(func),func参数为任意一个函数对象，需要判断函数是否可以调用，如果可以调用则返回该函数名(
类型为str)，否则返回 “fun is not function"。
'''


'''
1 定义一个方法get_fundoc(func),func参数为任意一个函数对象，返回该函数对象的描述文档，如果该函数没有描述文档，则返回"not found"
'''
import inspect
import os
def get_fundoc(func):
    #if inspect.isclass(func):
    if isinstance(func,str):
        a = 'Pydoc is %s' %func
        m = os.popen(a).read()
        return m
    else:
        return 'not found!'

fundoc = 'os.isfile'
fundoc_m = get_fundoc(fundoc)
#print fundoc_m

'''
2 定义一个方法get_cjsum(),求1-100范围内的所有整数的平方和。返回结果为整数类型。
'''

def get_cisum():
    numSum = 0
    for i in range(1,101):
        x = i * i
        numSum = numSum + x
    return numSum

num = get_cisum()
print num


'''
3 定义一个方法list_info(list), 参数list为列表对象，怎么保证在函数里对列表list进行一些相关的操作，不会影响到原来列表的元素值.
'''
import copy
def list_info(a):
    if isinstance(a, list):
        # 拷贝list方法一,深度拷贝:
        b = copy.deepcopy(a)
        b[0] = (['d', 'e', 'f'])
        return b
        # 拷贝list方法二,深度拷贝:
        c = a[:]


a = ['a', 'b', 'c', [1, 2, 3]]
c = list_info(a)
print a
print c

'''
4 定义一个方法get_funcname(func),func参数为任意一个函数对象，需要判断函数是否可以调用，如果可以调用则返回该函数名(
类型为str)，否则返回 “fun is not function"。
'''
import sys
def get_funcname(func):
    # 判断参数是否为一个函数对象。
    if callable(func):
        # 如果是一个函数对象,就打印出该函数的名字。
        print func.__name__
        return func
    else:
        '参数不是一个函数对象!'

def demo():
    a = 1
    return a

#get_funcname(demo)
assert get_funcname(demo) == demo
assert get_funcname(list_info) == list_info
assert get_funcname(test) == test





