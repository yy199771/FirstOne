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
9.2.2、调用未绑定de超类构造方法: 本节内容主要是历史遗留问题,在目前的python版本中,使用super函数的方法简单明了。
9.2.3、使用super函数
        当前类或者对象都可以作为super函数的参数使用,调用函数返回的对象的任何方法都是调用超类的方法,而不是当前类的方法。可以解决9.2.2例子中出现的问题。
        直接使用super(SongBird,self)。除此之外,__init__方法能以一个普通的(绑定)方式被调用。

9.3、成员访问:本节讨论一个有用的魔法方法集合,它可以创建行为类似于序列或者映射的对象。
9.3.1、基本的序列和映射规则
    __len__(self):
    __getitem__(self, key):
    __setitem__(self, key, value):
    __delitem__(self, kye):
9.3.2、子类化列表,字典和字符串

9.4、更多魔力

9.5、属性
9.5.1、property函数
    需要增加:__metaclass__ = type
9.5.2、静态方法和类成员方法
    静态方法:被装入Staticmethod。静态方法的定义没有self参数,且能够被类本身直接调用。
    类成员方法:被装入Classmethod。类方法在定义时需要名为cls的类似于self的参数。类成员方法可以直接用类的具体对象调用。
    为这样的包装方法引入了一个叫装饰器(decorators)的新语法。(它能对任何可调用的对象进行包装,即能够用于方法也能用于函数)。使用@操作符。可以使用多个装饰器,装饰器执行顺序与指定顺序相反。
9.5.3、__getattr__,__setattr__和它的朋友们
    拦截对象的所有特性访问是可能的,为了访问特性的时候可以执行代码,必须使用一些魔法方法。
    下面的4种方法提供了需要的功能。
    __getattribute__(self, name):当特性name被访问时自动被调用(只能在新式类中使用)
    __getattr__(self, name):当特性name被访问且对象没有相应的特性时被自动调用。
    __setattr__(self, name, value):当试图给特性name赋值时会被自动调用。
    __delattr__(self, name):试图删除特性name时被自动调用。
'''

# 9.2.1
__metaclass__ = type    # super函数只在新式类中起作用

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

# 9.2.1
class Bird:
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print 'Aaaah...'
            self.hungry =False
        else:
            print 'No, thanks.'

b = Bird()
b.eat()
b.eat()

'''
class SongBird(Bird):
    def __init__(self):
        self.sound = 'Squawk.'
    def sing(self):
        print self.sound

sb = SongBird()
sb.sing()
# 重写了Bird的__init__方法,所以调用eat方法会报错
sb.eat()
'''
# 9.2.3
class SongBird(Bird):
    def __init__(self):
        super(SongBird, self).__init__()
        self.sound = 'Squawk.'
    def sing(self):
        print self.sound

sb = SongBird()
sb.sing()
sb.eat()

# 9.3.2
class CounterList(list):
    def __init__(self, *args):
        super(CounterList, self).__init__(*args)
        self.counter = 0
    def __getitem__(self, index):
        self.counter += 1
        return super(CounterList, self).__getitem__(index)

cl = CounterList(range(10))
print cl
print cl.counter

# 9.5.1、
__metaclass__ = type
class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0
    def setSize(self, size):
        self.width, self.height = size
    def getSize(self):
        return self.width, self.height
    # 创建了一个属性,其中访问器函数被用作参数(先取值, 然后赋值),这个属性命名为size。这样一来就不再需要担心是如何实现的了。
    size = property(getSize, setSize)

r = Rectangle()
r.width = 10
r.height = 5
print type(r.size)
print r.size

# 9.5.2
'''
传统方式:
class MyClass:
    def smeth():
        print 'This is a static method!'
    smeth = staticmethod(smeth)

    def cmeth(cls):
        print 'This is a class method of', cls
    cmeth = classmethod(cmeth)
'''
class MyClass:
    @staticmethod
    def smeth():
        print 'This is a static method!'
    @classmethod
    def cmeth(cls):
        print 'This is a class method of', cls

MyClass.smeth()
MyClass.cmeth()

# 9.5.3
