#coding=utf-8
'''
1.模块的基本概念
    模块就是文件。
2.模块的基本操作
（1）import module：导入module的全部方法。调用方式：module.method
（2）from module import sth(method)：只引入需要引用的方法，这样引入的方法较少，性能开销较小。
（3）from module import all（*）：与第一个的区别是：在引起方法时，此类引用可以直接写方法调用，和在函数中调用一样，而方法一中需要
    module.method
（4）在module中如果有__all__之类的魔术方法，可以到达private方法的效果，之后在__all__中的方法才可以被外部调用。

3.包的创建
    包就是模块的组合，是一个文件夹，还具有模块的特性。
    包里面：必须含有__init__.py的文件。包中也用__all__方式来实现模块针对包的进出控制。
4.搜索模块
'''