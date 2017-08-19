#coding=utf-8

#locals 收集当前的所有局部变量并返回一个字典
def fun():
    a = 1
    b = 2
    return locals()
print fun()

# global 收集所有的.. 并返回一个字典
m = 4
def func():
    n = 3
print globals()



class Demo(object):
    '''hello'''
    # init 用来初始化对象
    def __init__(self,name):
        self.name = name
        print '__init__ ...'

    # new用来创建一个对象 , 执行完new后在执行init,且参数要一一对应
    def __new__(cls,name):
        print '__new__...'
        return super(Demo,cls).__new__(cls)
    # __del__相当于析构函数,当程序执行完毕后,会调用析构函数,Demo已被垃圾回收,所以会出现异常
    def __del__(self,name):
        print '__del__ ...',Demo.name

    # 该方法可以模拟函数行为  demo(2)
    def __call__(self,n):
        print '__call__ ...',n

demo = Demo('123')
demo(2)
print demo.__doc__
