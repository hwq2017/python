#coding=utf-8

class Demo(object):
    def __init__(self,name):
        self.name = name
    def getName(self):
        return self.name


def fun(a,b):
    return a + b

# 在本模块中 __name__ == '__main__',导入到顶层模块中,__name__是导入的模块名
print '=====',__name__

if __name__ == '__main__':
    print '顶层代码,可以做代码测试'
