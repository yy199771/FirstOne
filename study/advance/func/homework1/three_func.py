#coding=utf-8

'''
1、自醒函数
2、函数的作用域
'''


def func1(arg1,arg2):
    return arg1 + arg2

#print dir(func1.__code__)

#print func1.__code__.co_varnames
#print func1.__code__.co_filename

'''
函数的作用域
global 全局变量定义,函数内外都需要定义
'''


global arg

arg = 1

def func2():

    global arg
    arg = 3
    return arg

func2()
print arg


def func3(arg):
    arg[0] =5
    return arg

tlist = [1,2,3]
print func3(tlist)
print tlist