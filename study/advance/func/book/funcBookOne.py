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
    print params

print_params_3(x=1, y=2, z=3)

def print_params_4(x, y, z=3, *pospar, **keypar):
    print x, y, z
    print pospar
    print keypar

print_params_4(1,2,3,4,5,6,7,foo=1, bar=2)

'''
反转过程:使用元组和字典进行参数收集,如果使用*和**,也可以执行相反的操作。
'''
def add(x, y):
    return x + y

params = (1,2)
f = add(*params)
print f