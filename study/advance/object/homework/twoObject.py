#coding=utf-8


"""
进阶课 面向对象


1 习题讲解

2.class的基本定义

3.构造，析构函数

"""


class test(object):

	a = 1

	def func_1(self):
		return self.arg1,self.arg2

	def __init__(self,arg1,arg2):##构造函数
		self.arg1 = arg1
		self.arg2 = arg2

	def __del__(self):##析构函数,大多数情况下不使用此方法
		del self.arg1
		del self.arg2


# a 被称为 test的 属性
# func_1  被称为 test的 方法
# 我们所有的class都是object的派生类

t = test(1,4)
print t.a
print t.func_1()