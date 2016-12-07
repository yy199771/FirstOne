#coding=utf-8
'''
多态：是python式编程的核心，也被称为“鸭子类型”
封装
继承

私有化

类的命名空间

'''
from random import choice

x = choice(['Hello world!',[1,2,'e','e',4]])
print x.count('e')


# 多态
def add(a, b):
    return a + b


print add(1,2)
print add('abc','xyz')

# 私有化:为了让方法或者特性变为私有化(无法从外部访问),只要在它的名字前面加上"__"即可。
class secretive:
    # 私有化方法,在类内部可以访问,无法志杰对外提供访问。
    def __inaccessibile(self):
        print "Bet you can't see me..."

    def accessible(self):
        print 'The secret message is:'
        self.__inaccessibile()

class subSecretive(secretive):
    pass

s = secretive()
s.accessible()


# 类的命名空间:所有位于class语句中的代码都在特殊的命名空间中执行。这个命名空间可由类内所有成员访问。

# 指定超类

# 调查继承
# 判断子类是否存在父类(超类)
print issubclass(subSecretive, secretive)
# 查看类具有的父类:__bases__
print subSecretive.__bases__
# isinstance判断一个对象是否是一个类的实例。 使用isinstance不是一个好习惯,多使用多态。
s = subSecretive()
assert isinstance(s, subSecretive) == True  # 子类的实例
assert isinstance(s, secretive) == True     # 也是父类的实例

# 多个超类,也称为多重继承,应该尽量避免使用。

class Calculator:

    def calculate(self, expression):
        self.value = eval(expression)

class Talker:

    def talk(self):
        print 'Hi, my value is ', self.value

class TalkingCalculator(Calculator, Talker):
    pass

tc = TalkingCalculator()
tc.calculate('1+2*3')
tc.talk()

'''
接口和内省

接口:不用像java一样显式地编写接口
'''
print hasattr(tc, 'talk')
print hasattr(tc, 'fnord')

'''
常用方法

callable(Object): 确定对象是否可调用(比如函数或者方法)
getattr(object, name[, default]) :确定特性的值,可选择提供默认值
hasattr(object, name):确定对象是否给定的特性。
isinstance(object, class):确定对象是否是类的实例
issubclass(A, B):确定A是否为B的子类。
random.choice(sequence):从非空序列中随机选择元素
setattr(object, name, value):设定对象的给定特定为value
type(object):返回对象的类型

'''
