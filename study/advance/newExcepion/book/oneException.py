#coding=utf-8

'''
异常

8.2.1、raise语句:raise显示地引发异常,一旦执行了raise语句，raise后面的语句将不能执行.

8.2.2、自定义异常类:从Exception类继承

8.3、捕捉异常
    捕捉异常:try/except。
    如果捕捉到异常,但是又想传递异常,那么可以调用不带参数的raise


8.4、 不止一个except语句

8.5、用一个块捕捉2个异常:多个异常时,可以except(元组)

8.6、捕捉对象:在except子句中访问异常对象本身,可以使用2个参数(注意,就算要捕捉到多个异常,也只需except子句提供一个参数--一个元祖)。比如场景:让程序继续运行,记录错误。

8.7、真正的全捕捉
    无法捕捉到所有的异常,这种情况下,与其用try/except语句来隐藏异常,还不如让程序立刻崩溃。
    但是如果真的想用一段代码捕捉所有异常,可以在except子句中忽略所有的异常类。
    警告:这样处理异常是非常危险的,它会隐藏所有程序员未想到并且未做好准备处理的错误。

8.8、万事大吉
    一些坏事发生时执行一段代码是很有用的。可以在try/except 后面增加一个else语句。

8.9、最后。。。
    Finally子句:用来在可能的异常后进行清理。它和try子句联合使用。

8.10、异常和函数
    如果异常在函数内引发而不被处理,它就会传播至函数调用的地方。

8.11、异常之禅

本章新函数:
warnings.filterwarnings(action,...): 用于过滤报告
'''

# 8.2.2、自定义异常类
class SomeCustomeException(Exception):
    pass

# 8.3、& 8.4

def x(a, b):
    try:
        print a / b
    except ZeroDivisionError:
        print "The second number can't be Zero!"
    except TypeError:
        print "That wasn't a number, was it?"

#x(1, 0)
#x(1, 'aa')

# 8.5、
def y(a, b):
    try:
        print a / b
    except (ZeroDivisionError, TypeError, NameError):
        print "The second number can't be Zero!"

#y(1, 0)
#y(1, 'aa')

# 8.6、捕捉对象
def z(a, b):
    try:
        print a / b
    except (ZeroDivisionError, TypeError), e:
        print e

#z(1, 0)
#z(1, 'aa')

# 8.7、真正的全捕捉
def w(a, b):
    try:
        print a / b
    except:
        print "Something wrong happend..."

w(1, 0)
w(1, 'aa')

# 8.9、最后finally
def t():
    x = None
    try:
        x =1 / 0
    finally:
        print 'Cleaning up...'
        del x
t()


class MuffledCalculator:

    muffled = False

    def calc(self, expr):
        try:
            return eval(expr)
        except ZeroDivisionError:
            if self.muffled:
                print 'Division by zero is illegal!'
            else:
                raise

calculator = MuffledCalculator()
calculator.calc('10/2')
#calculator.calc('10/0')
calculator.muffled = True
#calculator.calc('10/0')






'''

常见的异常如下表所示：
异常名称	描述
BaseException	所有异常的基类
SystemExit	解释器请求退出
KeyboardInterrupt	用户中断执行(通常是输入^C)
Exception	常规错误的基类
StopIteration	迭代器没有更多的值
GeneratorExit	生成器(generator)发生异常来通知退出
StandardError	所有的内建标准异常的基类
ArithmeticError	所有数值计算错误的基类
FloatingPointError	浮点计算错误
OverflowError	数值运算超出最大限制
ZeroDivisionError	除(或取模)零 (所有数据类型)
AssertionError	断言语句失败
AttributeError	对象没有这个属性
EOFError	没有内建输入,到达EOF 标记
EnvironmentError	操作系统错误的基类
IOError	输入/输出操作失败
OSError	操作系统错误
WindowsError	系统调用失败
ImportError	导入模块/对象失败
LookupError	无效数据查询的基类
IndexError	序列中没有此索引(index)
KeyError	映射中没有这个键
MemoryError	内存溢出错误(对于Python 解释器不是致命的)
NameError	未声明/初始化对象 (没有属性)
UnboundLocalError	访问未初始化的本地变量
ReferenceError	弱引用(Weak reference)试图访问已经垃圾回收了的对象
RuntimeError	一般的运行时错误
NotImplementedError	尚未实现的方法
SyntaxError	Python 语法错误
IndentationError	缩进错误
TabError	Tab 和空格混用
SystemError	一般的解释器系统错误
TypeError	对类型无效的操作
ValueError	传入无效的参数
UnicodeError	Unicode 相关的错误
UnicodeDecodeError	Unicode 解码时的错误
UnicodeEncodeError	Unicode 编码时错误
UnicodeTranslateError	Unicode 转换时错误
Warning	警告的基类
DeprecationWarning	关于被弃用的特征的警告
FutureWarning	关于构造将来语义会有改变的警告
OverflowWarning	旧的关于自动提升为长整型(long)的警告
PendingDeprecationWarning	关于特性将会被废弃的警告
RuntimeWarning	可疑的运行时行为(runtime behavior)的警告
SyntaxWarning	可疑的语法的警告
UserWarning	用户代码生成的警告

'''