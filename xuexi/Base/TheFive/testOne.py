#coding=utf-8

# 将模块导入函数的时候,可以使用。
# import somemodule
# from somemodule import somefunction
# from somemodule import *

# 序列解包
values =1,2,3
print values
x,y,z = values
print x

# 链式赋值
#x = y = somefunction()

# 增量赋值

# in:成员资格运算符

# 字符串和序列比较:字符串可以按照字母顺序排列进行比较。

# 布尔运算符:and、or、not

# 断言:
a, b =1, 2
c = a + b
assert c == 3

# 循环
# while
x =1
while x <=10:
    print x
    x += 1

# for
words = ['this','is','an','ex','parrot']
for word in words:
    print word

# 遍历元素字典
d = {'x':1,'y':2,'z':3}
for key in d:
    print key,d[key]

# 并行迭代
names = ['anne','beth','george','damon']
ages = [12,45,32,105]
for i in range(len(names)):
    print names[i], 'is', ages[i], 'years old.'
# zip函数可以用来进行并行迭代,把两个序列压缩在一起,然后返回一个元组的列表。
print zip(names,ages)

for name,age in zip(names,ages):
    print name, 'is', age, 'years old.'

# 编号迭代
# enumerate函数。


# 翻转和排序迭代
# reversed和sorted:不是原地修改对象。


