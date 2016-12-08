#coding=utf-8
'''
9.1、准备工作:
    确保类是新型的:__metaclass__=type

9.2、构造方法(第一个魔法方法):当一个对象被创建后，会立即调用构造方法。
    创建一个构造方法就是__init__
9.2.1、重写一般方法和特殊的构造方法。
    重写是继承机制中的一个重要内容，对于构造方法尤其重要。
    构造方法用来初始化新创建对象的状态。
    当一个类的构造方法被重写，那么就需要调用超类的构造方法，否则对象可能不会被正确地初始化。


'''

# 9.2.1
class A:
    def hello(self):
        print "Hello, I'm A."

class B(A):
    def hello(self):
        print "Hello, I'm B."

a = A()
b = B()
a.hello()
b.hello()