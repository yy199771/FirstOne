#coding=utf-8
'''
1.先实现，再优化，过早优化是万恶之源
2.kiss原则  记忆

最小惊讶原则

s同学  追求机巧

简单，白痴都能看懂

复杂：你代码的行数

'''


class test(object):

    @staticmethod #静态方法的装饰
    def d():
        return 4
    @property #将方法修改成属性的装饰器
    def f(self):
        return 5

print test.d()
to = test()
print to.f


'''
def test(a,b):

    if isinstance(object, classinfo):
    #逻辑错误
        return a+b
'''