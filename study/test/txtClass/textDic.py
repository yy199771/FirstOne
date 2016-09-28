#coding=utf-8
__author__ = 'Administrator'

# 操作文件和目录
# 操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，这一点要注意一下。
# 查看、创建和删除目录可以这么调用：

import os

#print os.name
#print os.environ
# 查看当前目录
print os.path.abspath('.')

# 在某个目录下创建一个新目录，
# 首先把新目录的完整路径表示出来:
print os.path.join("C:\\Users\\Administrator\\PycharmProjects\\test\\", 'testdir')
# 然后创造一个目录：
os.mkdir("C:\\Users\\Administrator\\PycharmProjects\\test\\testdir1")
# 最后删掉一个目录：
os.rmdir("C:\\Users\\Administrator\\PycharmProjects\\test\\testdir1")


for x in os.listdir("C:\\Users\\Administrator"):
    print x
