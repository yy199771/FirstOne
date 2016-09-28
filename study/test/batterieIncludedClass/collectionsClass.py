#coding=utf-8
# 2016-6-27
__author__ = 'Administrator'



# namedtuple.
# namedtuple是一个函数，它用来创建一个自定义的tuple对象，
# 并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
# 这样一来，我们用namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用，使用十分方便。
# 可以验证创建的Point对象是tuple的一种子类：
from collections import namedtuple
from collections import deque
from collections import defaultdict
from collections import OrderedDict
from collections import Counter

Point = namedtuple('Point', ['x', 'y','z'])
p = Point(1, 2,3)
print 'namedtuple'
print p.x
print p.y
print p.z

# deque
# 使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，
# 因为list是线性存储，数据量大的时候，插入和删除效率很低。
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈。
q = deque(['a', 'b', 'c','d','e','f'])
q.append('x')
q.appendleft('y')
print 'deque'
#q.pop()
#q.popleft()
print q


# defaultdict
# 使用dict时，如果引用的Key不存在，就会抛出KeyError。
# 如果希望key不存在时，返回一个默认值，就可以用defaultdict：
# 注意默认值是调用函数返回的，而函数在创建defaultdict对象时传入。
# 除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的。
dd = defaultdict(lambda :'N/A')
dd['key1'] ='abc'
print 'defaultdict'
print dd['key1']
print dd['key2']

# OrderedDict
# 使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
# 如果要保持Key的顺序，可以用OrderedDict：
# 注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序：
d = dict([('a',1),('b',2),('c',3)])
print 'OrderedDict1'
print d

od = OrderedDict([('a',1),('b',2),('c',3)])
print 'OrderedDict2'
print od

#  OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key：
class LastUpdateOrderDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdateOrderDict,self).__iter__()
        self._capacity = capacity
    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print 'remove:', last
        if containsKey:
            del self[key]
            print 'set:', (key, value)
        else:
            print 'add:', (key, value)
        OrderedDict.__setitem__(self, key,value)

'''
print 'OrderedDict3'
ss = LastUpdateOrderDict(OrderedDict([('a',1),('b',2),('c',3)]))
pp = ss.__setitem__(self,'d',4)
print pp
'''

# Counter
# Counter是一个简单的计数器，例如，统计字符出现的个数：
# Counter实际上也是dict的一个子类，上面的结果可以看出，
# 字符'g'、'm'、'r'各出现了两次，其他字符各出现了一次。
print 'Counter'
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print c
