#coding=utf-8
# 第四章 字典:当索引不好用时

from copy import deepcopy

phonebook = {'Alice':'2341','Beth':'3214','Cecil':'3258'}
print phonebook

#dict函数 : 通过其他映射建立字典。
items =[('name','Gumby'),('age',42)]
d = dict(items)
print d

#clear方法:清除字典中所有的项
returned_value = d.clear()
print d

# copy方法(浅复制):返回一个具有相同健-值对的新字典.
# 如果修改了某个值(原地修改,不是替换,)原字典也会发生变化。因为同样的值也存储在原字典中
# deepcopy(深复制)。
x = {'username':'admin','machines':['foo','bar','baz']}
y = x.copy()
y['username'] = 'mlh'
y['machines'].remove('bar')
print y
print x

dd ={}
dd['names'] = ['Alfred','Bertrand']
c = dd.copy()
dc = deepcopy(dd)
dd['names'].append('Clive')
print c
print dc

#fromkeys:使用给定的键建立新的字典,每个键默认对应的值为None。
n = {}.fromkeys(['name','age'])
print n

#get:更为轻松的访问字典项的方法。
da = {}
print da.get('name')
print 'name'