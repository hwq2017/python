#coding=utf-8

class FirstClass(object):
    def staticfun():
        print 'hello world'
    staticfun = staticmethod(staticfun)

class TwoClass(object):
    def fun(cls):
        print '你好,世界'
    fun = classmethod(fun)

FirstClass.staticfun()
TwoClass.fun()


class Demo(object):
    def fun(self):
        print 'hahaha'

d = Demo()

def func(self):
    print 'add function'

Demo.func = func
d.f = func()
d.f()
