#coding=utf-8

'''
关键字参数:
可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
'''

# 1 函数基本概念
# 显性返回值 return

#函数的健壮性
'''
1.你永远知道你的方法会返回什么（异常处理，条件判断）
2.返回你想要的结果
'''

def func_name():
    return '112233'
    #默认return None

print func_name()

# 函数参数
'''
必选参数:

可选参数: 参数有默认值。默认值和没有默认值的区别在于"="。

'''

'''
函数的健壮性:
1、永远知道方法返回的是什么?(异常处理,条件判断)
2、返回你想要的结果
'''

def add(num1, num2,num3=10):
    if isinstance(num1, int) and isinstance(num2, int):
        return num1 + num2 + num3
    else:
        return '参数不是整数!'

print add(2, 5)
print add(1, 8)

assert add(1,8) == 19
assert add(1,8) == 19

'''
可变参数: *将参数集合成元组(tuple)。
'''

def add1(*num):
    print type(num)
    d =0
    for i in num:
        d += i
    return d

print add1(1,2,3,4,5,6,7,8,9)


def add2(**num2):
    print type(num2)
    return num2

print add2(x=1, y=2, z=3)
