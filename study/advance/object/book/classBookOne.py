#coding=utf-8
'''
多态：是python式编程的核心，也被称为“鸭子类型”
封装
继承
'''
from random import choice

x = choice(['Hello world!',[1,2,'e','e',4]])
print x.count('e')