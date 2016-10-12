#coding=utf-8
# 第四章 字典:当索引不好用时

# 映射:可以使用任何不可变对象标识元素。最常用的类型是字符串和元组。Python唯一内建的映射类型是字典。


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
da['name'] = 'Jack'
print da.get('name')

#has_key:检查字典中是否含有给出的键。表达式d.has_key(k) 相同于表达式k in d.
db = {}
print dd.has_key('name')
db['name'] = 'Eric'
print db.has_key('name')

#items和iteritems
#items:将所有的字典项以列表方式返回,每项都来自于(键,值),但没有特殊的顺序。
dc = {'title':'Python web site','url':'http://www.baidu.com','spam':0}
print dc.items()
#iteritems:返回一个迭代器对象而不是列表。
it = d.iteritems()
print type(it)

#keys和iterkeys
#keys:将字典中的键以列表形式返回,而iterkeys则返回针对键的迭代器。
print dc.keys()
print dc.iterkeys()

# pop:获得对应于给定键的值,然后将这个键-值对从字典中移除。
dd = {'x':1,'y':2}
print dd.pop('x')
print dd

# popitem:类似list.pop,后者会弹出列表的最后一个元素,popitem弹出随机项。适合循环的一个一个移除。
de = {'title':'Python web site','url':'http://www.baidu.com','spam':0}
print de.popitem()
print de

# setdefault:获得于给定键相关联的值,还能在字典中不含有给定键的情况下设定相应的键值。
df = {}
df.setdefault('name','N/A')
print df
df['name'] = 'Gumby'
print df.setdefault('name','N/A')

# update:可以利用一个字典项更新另外一个字典。
dg = {
    'title':'Python Web Site',
    'url':'http://www.163.com',
    'changed':'Mar 14 22:09:15 MET 2008'
}
x = {
    'title':'Python Language Website'
}
dg.update(x)
print dg

# values和itervalues
# values:以列表形式返回字典的值(itervalues返回值的迭代器)。
dh = {}
dh['a'] = 1
dh['b'] = 2
dh['c'] = 3
dh['d'] = 4
print dh.values()
print dh
