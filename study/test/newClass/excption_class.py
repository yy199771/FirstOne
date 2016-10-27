#coding=utf-8
__author__ = 'Administrator'
import logging

# 错误处理
def try_Fun(num):
    try:
        print 'try...'
        r = 10 / num
        print 'result...', r
    except ZeroDivisionError as e:
        print e.message
    finally:
        print 'finally...'
    print 'END'

print '---------------------------'
if __name__ == '__main__':
    try_Fun(0)

def foo(s):
    return 10 /int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except StandardError, e:
        logging.exception(e)

#main()

class FooError(StandardError):
    pass

def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

print foo(2)
