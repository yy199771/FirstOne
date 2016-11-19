#coding=utf-8

"""
进阶 面向对象第一节 初识class


1.如何去定义一个最基本的class
2.class最基本的子元素
3.class传参
4.__init__方法
5.class和函数的区别

"""

'''
object:原生类
'''

class test(object):

	'''
    get被称之为test对象的方法
	'''

	def __init__(self,var1):
		self.var1 = var1


	def get(self, a=None):
		return self.var1

	pass



def get(a):
	return a


"""
t是类test的一个实例
"""
t = test('test str heiheihei')
print t.get()

"""
如何去使用对象内置的方法
1.实例化这个class （test） t = test()
2.使用 class.method()的方式去调用 class 的内置方法

注意：
1.当定义一个class的内置方法method时，method的参数的第一个永远是self,self代表的是class对象本身,在class内部是可以全局调用的。

def __init__:初始化参数
"""

# new_var = 4

# print t.get(new_var)

# print get(new_var)

'''
new_love = love(boy_object, girl_object)
print new_love.get_children()
print new_love.get_father()
print new_love.get_house()
'''