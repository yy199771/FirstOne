#coding=utf-8
'''
习题：
定义一个列表的操作类：Listinfo

包括的方法:

1 列表元素添加: add_key(keyname)  [keyname:字符串或者整数类型]
2 列表元素取值：get_key(num) [num:整数类型]
3 列表合并：update_list(list)	  [list:列表类型]
4 删除并且返回最后一个元素：del_key()

list_info = Listinfo([44,222,111,333,454,'sss','333'])

定义一个集合的操作类：Setinfo

包括的方法:

1 集合元素添加: add_setinfo(keyname)  [keyname:字符串或者整数类型]
2 集合的交集：get_intersection(unioninfo) [unioninfo :集合类型]
3 集合的并集： get_union(unioninfo)[unioninfo :集合类型]
4 集合的差集：del_difference(unioninfo) [unioninfo :集合类型]

set_info =  Setinfo(你要操作的集合)
'''


class Listinfo(list):

    def __init__(self, l):
        self.l = l

        if not isinstance(l, list):
            return '请输入一个list!'

    def add_setinfo(self, keyname):

        self.keyname = keyname

        if (not isinstance(keyname, str)) and (not isinstance(keyname, int)):
            return '新加入的key不是字符串或者不是整数!'

        self.l.append(keyname)
        return self.l

    def get_key(self, num):
        self.num = num

        for x in self.l:
            if not isinstance(self.num, int):
                return '请输入一个整数!'
            if self.num == x:
                return self.num

    def update_list(self, extendlist):
        self.extendList = extendlist
        if not isinstance(self.extendList, list):
            return '请输入一个list!'
        # extend 将2个list合并成一个list
        self.l.extend(self.extendList)
        return self.l


    def del_key(self):
        # 删除最后一个元素,并返回剩下的最后一个元素
        self.l.pop()
        return self.l

list_info = Listinfo([44,222,111,333,454,'sss','333'])
print type(list_info)
print list_info.get_key('222')
print list_info.get_key(44)
print list_info.add_setinfo('ABC')
#print list_info.add_setinfo([12,3,2,'3'])
print list_info.update_list([12,3,2,'3'])
print list_info.update_list('CDE')
print list_info.del_key()


#class Setinfo():