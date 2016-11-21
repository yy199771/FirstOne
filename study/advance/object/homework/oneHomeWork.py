#coding=utf-8
'''
面向对象习题：

一：定义一个学生类。有下面的类属性：

1 姓名
2 年龄
3 成绩（语文，数学，英语)[每课成绩的类型为整数]

类方法：

1 获取学生的姓名：get_name() 返回类型:str
2 获取学生的年龄：get_age() 返回类型:int
3 返回3门科目中最高的分数。get_course() 返回类型:int

写好类以后，可以定义2个同学测试下:

zm = student('zhangming',20,[69,88,100])
返回结果：
zhangming
20
100

lq = student('liqiang',23,[82,60,99])

返回结果：
liqiang
23
99

二：定义一个字典类：dictclass。完成下面的功能：

dict = dictclass({你需要操作的字典对象})

1 删除某个key

del_dict(key)


2 判断某个键是否在字典里，如果在返回键对应的值，不存在则返回"not found"

get_dict(key)

3 返回键组成的列表：返回类型;(list)

get_key()

4 合并字典，并且返回合并后字典的values组成的列表。返回类型:(list)

update_dict({要合并的字典})

'''


class student(object):

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_course(self):
        if not isinstance(self.score, list):
            return '请输入一个list'
        return max(self.score)

zm = student('zhangming',20,[69,88,100])
print zm.get_name()
print zm.get_age()
print zm.get_course()

lq = student('liqiang',23,[82,60,99])
print lq.get_name()
print lq.get_age()
print lq.get_course()


class dictclass(dict):

    def __init__(self, d):
        self.d = d
        # 判断d是否为一个dict
        if not isinstance(self.d, dict):
            return '请输入一个dict.'

    def del_dict(self, key):
        self.key = key
        # 判断key是否在dict里面
        if not self.no_key in self.d.keys():
            return 'key is not in dict.'
        del self.d[key]
        return self.d

    def get_dict(self, no_key):

        self.no_key = no_key
        # 判断key是否在dict,如果在输入key对应的value。
        if not no_key in self.d.keys():
            return 'not found.'
        return self.d[self.no_key]

    # 将key组成新的list。
    def get_key(self):
        keyList=[]
        for key in self.d.keys():
            keyList.append(key)
        return keyList

    # 将value组成新的list。
    def update_dict(self):
        valueList = []
        for value in self.d.values():
            valueList.append(value)
        return valueList

test_dict =  {"a" : "apple", "b" : "banana", "g" : "grape", "o" : "orange"}
dd = dictclass(test_dict)
#print dd.del_dict('a')
#print dd.get_dict('g')
#print dd.get_key()
print dd.update_dict()