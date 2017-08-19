#coding=utf-8

def func(a,b):
    print 'a:',a
    print 'b:',b

# 作为调用者,传参的四种方式

func(1,2)  # 位置传参

func(a = 1,b = 3) # 关键字传参 可颠倒位置,一般不这么做

l = (2,30)   # *传参 以元组(),或列表[]传参
func(*l)

d = {'a':1,'b':2} # **传参 键 必须与 函数形参名对应
func(**d)




# 函数声明形参的四种方式

def fun1(a,b):
    print 'a:',a
    print 'b:',b
fun1(3,4)


def fun2(a,b = 10):   # 设置默认参数的形参必须写后面
    print 'a:',a
    print 'b:',b
fun2(100)
fun2(100,100)


def fun3(a,c = 12,*b): # 收集参数写后面(python2)
    print a,b,c
fun3(1,2,3,4)


def fun4(**d):    # 字典参数,必须以键值对的方式传参
    print d
fun4(a = 1,b = 2)
