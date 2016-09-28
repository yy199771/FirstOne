#coding=utf-8
__author__ = 'Administrator'
import logging

# 错误处理
try:
    print 'try...'
    r = 10 / 2
    print 'result...', r
except ZeroDivisionError, e:
    print 'except:', e
finally:
    print 'finally...'
print 'END'

print '---------------------------'

def foo(s):
    return 10 /int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except StandardError, e:
        logging.exception(e)

main()
print 'END'

print '---------------------------'

class FooError(StandardError):
    pass

def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

print foo(2)
