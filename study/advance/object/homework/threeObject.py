#coding=utf-8

'''
1.面向对象编程，是面向对象，而不是面向类。

2.对于新手，一开始就进行类设计是傻傻的类设计。
"""
1、伪代码 小程序->直接写流程    大项目->先分析结构
"""

3.有趣的面向对象。
"""
1、继承
"""


4.先实现，再优化，过早优化是万恶之源

5.kiss原则


案例讲解:
1、先分析需求
2、找到共通性
3、找到最小节点
4、上述3点,从3往1倒序分析

男人和女人的恋爱 1 + 0 = 1
男人和男人的恋爱 1 + 1 = 2
女人和女人的恋爱 0 + 0 = 0
'''

class boy(object):

    gender = 1

    def __init__(self, name):
        self.name = name

class girl(object):

    gender = 0

    def __init__(self, name):
        self.name = name

class love(object):

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def meet(self):
        return '这是%s和%s的恋爱' %(self.first.name, self.second.name)

    def marry(self):
        return '这是%s和%s的结婚' %(self.first.name, self.second.name)

    def children(self):
        return '这是%s和%s的孩子' %(self.first.name, self.second.name)

class normal(love):

    """
        男人和女人的恋爱
    """

    def __init__(self, first, second):
        if 1 != first.gender + second.gender:
            print '对象引起错误'
        else:
            love.__init__(self,first, second)

    def meet(self):
        pass

    def marry(self):
        pass

    def children(self):
        pass