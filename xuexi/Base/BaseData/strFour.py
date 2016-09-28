#coding=utf-8
__author__ = 'yangyang'

#1.
s = "i,am,lilei"
f = 'am'
str = s.find(f)
c = s.split(',')[1]
print c
print s[2:4]

#2.
s = 'i am a boy.'
print s.replace('boy','girl')

print bool('2012' == 2012)
