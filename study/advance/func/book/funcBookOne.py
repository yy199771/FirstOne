#coding=utf-8

import math

x = 1
y = math.sqrt
    # 判断是否为函数
print callable(x)
print callable(y)
    # return 跳出函数,不执行后面的内容

    # 参数魔法
def change(n):
    n[0] = 'Mr.Gumby'

names = ['Mrs.Entity', 'Mrs.Thing']

change(names)
print names

# 位置参数

# 初始化数据结构
def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}

storage = {}
# 将此数据结构代入变量中
init(storage)
print storage

'''
def lookup(data, label, name):
    return data[label].get(name)

lookup(storage, 'middle', 'Lie')

def store(data, full_name):
    names = full_name.split()
    if len(names) == 2:
        names.insert(1, '')
    labels = 'first', 'middle', 'last'

for labels, names in zip(labels, names):
    people = lookup(data, label, name)
    if people:
        people.append(full_name)
    else:
        data[label][name] = [full_name]

'''

'''
   关键字参数和默认值
    # 关键字参数最厉害的地方是提供了默认值
'''
def hello4(name, greeting='Hello', punctuation='!'):
    print '%s, %s%s' % (greeting, name, punctuation)

hello4('Mars')
hello4('Mars', 'Howdy')
hello4('Mars', 'Howdy','...')
hello4('Mars', punctuation='.')
hello4('Mars', greeting='Top of the morning to ya')
'''
    收集参数:提供任意数量的参数。
'''
def print_params_3(**params):
    print 'params3'
    print params
    print '-------------'

print_params_3(x=1, y=2, z=3)

def print_params_4(x, y, z=3, *pospar, **keypar):
    print x, y, z
    print 'pospar is ', pospar
    print 'keypar is ', keypar

print_params_4(1,2,3,4,5,6,7,foo=1, bar=2)

'''
反转过程:使用元组和字典进行参数收集,如果使用*和**,也可以执行相反的操作。
'''
def add(x, y):
    return x + y

params = (1,2)
f = add(*params)
print f

params_ = {'name':'Sir.Robin', 'greeting':'Well met'}
print_params_3(**params_)

def with_stars(**kwds):
    print kwds['name'], 'is', kwds['age'], 'years old.'

def without_stars(kwds):
    print kwds['name'], 'is', kwds['age'], 'years old.'

args ={'name': 'Mr.Gumby', 'age':42}
# 星号只在定义函数(允许使用不定数目的参数)或者调用('分割'字典或者序列)时才有用。
with_stars(**args)
without_stars(args)

'''
练习使用参数
'''
def story(**kwds):
    return 'Once upon a time, there was a ' \
           '%(job)s called %(name)s.' % kwds

def power(x, y, *others):
    if others:
        print 'Received redundant paramenters:', others
    return pow(x, y)

def interval(start, stop=None, step=1):
    'Imitates range() for step >0'
    if stop is None:            # 如果没有为stop提供值
        start, stop=0, start    # 指定参数
    result = []
    i = start                   # 计算start索引
    while i< stop:              # 直到计算到stop索引
        result.append(i)        # 将索引添加到result内
        i += step               # 用step(>0)增加索引
    return result

print story(job='king', name='Gumby')
print story(name='Sir Robin', job='brave knight')

params_story = {'job': 'language', 'name':'Python'}
print story(**params_story)

del params_story['job']
print story(job='stroke of genius', **params_story)

print power(2,3)
print power(y=3, x=2)
params_power = (5,) * 2
print power(*params_power)
print power(3, 3, 'Hello world')

print interval(10)
print interval(1, 5)
print interval(3, 12, 4)
#print power(interval(3, 7))

'''
作用域:全局变量与局部变量重名时,全局会被覆盖,除非使用globals()
'''

'''
递归
'''
# 二元搜索
# bisect模块可以非常有效的实现二元查找

def search(sequence, number, lower, upper):
    if lower ==upper:
        assert number ==sequence[upper]
        return upper
    else:
        middle = (lower + upper)  // 2
        if number > sequence[middle]:
            return search(sequence, number, middle+1, upper)
        else:
            return search(sequence, number, lower, middle)

seq = [34,67,8, 123,4,100,95]
seq.sort()
print seq
#print search(seq, 34)

'''
map、filer:在当前版本并不是特别有用,并且可以使用列表推到式代替。不过可以使用map函数将序列中的元素全部传递给一个函数。
reduce: 一般来说不能轻松被列表推到式,通常不用到这个功能,它会将序列的前2个元素与给定的函数联合使用。并将返回值与第三个元素继续联合使用,直到整个序列都处理完毕。
'''

# map
# map(function, sequence) ：对sequence中的item依次执行function(item)，见执行结果组成一个List返回：
print map(str, range(10))

# filter函数可以基于一个返回布尔值的函数对元素进行过滤。
# 对sequence中的item依次执行function(item)，将执行结果为True的item组成一个List/String/Tuple（取决于sequence的类型）返回：

def func_filter(x):
    return x.isalnum()

seq = ['foo', 'x41', '?!', '***']
print filter(func_filter, seq)

# 使用推到式可以不用专门定义一个函数:
print [x for x in seq if x.isalnum()]

# reduce(function, sequence, starting_value)：对sequence中的item顺序迭代调用function，如果有starting_value，还可以作为初始值调用，例如可以用来对List求和：
def add(x, y):
    return x + y

print reduce(add, range(1, 11))
print reduce(add, range(1, 11), 20)