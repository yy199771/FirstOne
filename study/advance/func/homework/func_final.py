#coding=utf-8

'''
1.定义一个func(name)，该函数效果如下。
assert func("lilei") = "Lilei"
assert func("hanmeimei") = "Hanmeimei"
assert func("Hanmeimei") = "Hanmeimei"
'''
def upWord(nameStr):
    if isinstance(nameStr, str):
        #字符串的首字母转换成大写， 其余转换成小写
        return nameStr.capitalize()
    else:
        return '请输入字符串!'
print upWord('lilei')
assert upWord("lilei") == "Lilei"
assert upWord("hanmeimei") == "Hanmeimei"
assert upWord("Hanmeimei") == "Hanmeimei"

"""
2.定义一个func(name,callback=None),效果如下。
assert func("lilei") == "Lilei"
assert func("LILEI",callback=string.lower) == "lilei"
assert func("lilei",callback=string.upper) == "LILEI"
"""

def upWordAdvance(name, callback=None):
    if isinstance(name,list):
        nameStr = name.capitalize()
    name1 = name.lower
    print type(name)
upWordAdvance('lilei')


"""
3.定义一个func(*kargs),效果如下。

l = func(1,2,3,4,5)
for i in l:
	print i,
#输出 1 2 3 4 5

l = func(5,3,4,5,6)
for i in l:
	print i
#输出 5 3 4 5 6
"""

def func(*kargs):
    l = list(kargs)
    for i in l:
        return i

l = func(1,2,3,4,5)


"""
4.定义一个func(*kargs)，该函数效果如下。

assert func(222,1111,'xixi','hahahah') == "xixi"
assert func(7,'name','dasere') == 'name'
assert func(1,2,3,4) == None

"""

def funcFirstStr(*kargs):
    l = list(kargs)
    for i in l:
        if isinstance(i, str):
            return i

l = funcFirstStr(222,1111,'xixi','hahahah')
print l

"""
5.定义一个func(name=None,**kargs),该函数效果如下。

assert func(“lilei”) == "lilei"
assert func("lilei",years=4) == "lilei,years:4"
assert func("lilei",years=10,body_weight=20) == "lilei,years:4,body_weight:20"

"""
def funcAll(name=None, **kargs):
    data = []
    # items():Return a copy of the dictionary’s list of (key, value) pairs.
    for x,y in kargs.items():

        data.extend([',', str(x), ':', str(y)])

    info = ''.join(data)
    return '%s%s'%(name,info)

s = funcAll('lilei', years = 4, body_weight = 20)
print s