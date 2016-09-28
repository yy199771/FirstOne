#coding=utf-8
__author__ = 'Administrator'

# __getattr__
# Python还有另一个机制，那就是写一个__getattr__()方法，动态返回一个属性
# 注意，只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找。
# 此外，注意到任意调用如s.abc都会返回None，这是因为我们定义的__getattr__默认返回就是None。要让class只响应特定的几个属性，我们就要按照约定，抛出AttributeError的错误：
class Student(object):
    def __init__(self):
        self.name = 'Jack'

    def __getattr__(self, attr):
        if attr == 'age':
            return lambda:25
        if attr == 'score':
            return 99
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
s =  Student()
print s.name
print s.score    #返回动态属性值
print s.age()    #返回函数
# 这实际上可以把一个类的所有属性和方法调用全部动态化处理了，不需要任何特殊手段。
# 这种完全动态调用的特性有什么实际作用呢？作用就是，可以针对完全动态的情况作调用。

# __call__
# 一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用。
# 能不能直接在实例本身上调用呢？类似instance()？在Python中，答案是肯定的。
class Student1(object):
    def __init__(self, name):
        self.name = name
    def __call__(self):
        print('My name is %s.' % self.name)

s1 = Student1('Michael')
s1()


# 要创建一个class对象，type()函数依次传入3个参数：
# class的名称；
# 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。

def fn(self, name='jack'):
    print('Hello, %s.' % name)

Hello = type('Hello', (object, ), dict(hello=fn))
h = Hello()
h.hello()

'''
metaclass
除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass。
metaclass，直译为元类，简单的解释就是：
当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。

但是如果我们想创建出类呢？那就必须根据metaclass创建出类，所以：先定义metaclass，然后创建类。
连接起来就是：先定义metaclass，就可以创建类，最后创建实例。
所以，metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”。
metaclass是Python面向对象里最难理解，也是最难使用的魔术代码。
正常情况下，你不会碰到需要使用metaclass的情况，所以，以下内容看不懂也没关系，因为基本上你不会用到。
'''