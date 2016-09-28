#coding=utf-8
__author__ = 'Administrator'

import json

# 序列化
# 我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，
# 在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。
# Python提供两个模块来实现序列化：cPickle和pickle。
# 这两个模块功能是一样的，区别在于cPickle是C语言写的，速度快，pickle是纯Python写的，速度慢，
# 跟cStringIO和StringIO一个道理。用的时候，先尝试导入cPickle，如果失败，再导入pickle：

try:
    import cPickle as pickle
except ImportError:
    import pickle

# ickle.dumps()方法把任意对象序列化成一个str，然后，就可以把这个str写入文件。
# 或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object：
f = open("C:\\Users\\Administrator\\PycharmProjects\\test\\testdir\\dump.txt",'wb')
d = dict(name='Bob', age=20,score=88)
pickle.dump(d,f)
f.close()
print '--------------------------------'
f = open("C:\\Users\\Administrator\\PycharmProjects\\test\\testdir\\dump.txt",'rb')
d = pickle.load(f)
f.close()
print d

# JSON
# dumps()方法返回一个str，内容就是标准的JSON。
# 类似的，dump()方法可以直接把JSON写入一个file-like Object。
# 要把JSON反序列化为Python对象，用loads()或者对应的load()方法，
# 前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化：

d = dict(name='Jack', age=34, score=99)
print 'json:', json.dumps(d)

# 要把JSON反序列化为Python对象，用loads()或者对应的load()方法，
# 前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化

json_str = '{"age":20, "score":77, "name":"Neil"}'
json.loads(json_str)

# 有一点需要注意，就是反序列化得到的所有字符串对象默认都是unicode而不是str。
# 由于JSON标准规定JSON编码是UTF-8，
# 所以我们总是能正确地在Python的str或unicode与JSON的字符串之间转换。

# JSON进阶
# Python的dict对象可以直接序列化为JSON的{}，
# 不过，很多时候，我们更喜欢用class表示对象，比如定义Student类，然后序列化：
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


def student2dict(std):
    return {
        'name':std.name,
        'age':std.age,
        'score':std.score
    }
s = Student('Sam', 19, 100)
print(json.dumps(s,default=student2dict))

# Python语言特定的序列化模块是pickle，但如果要把序列化搞得更通用、更符合Web标准，就可以使用json模块。
# json模块的dumps()和loads()函数是定义得非常好的接口的典范。
# 当我们使用时，只需要传入一个必须的参数。
# 但是，当默认的序列化或反序列机制不满足我们的要求时，
# 我们又可以传入更多的参数来定制序列化或反序列化的规则，
# 既做到了接口简单易用，又做到了充分的扩展性和灵活性