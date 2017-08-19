#coding=utf-8

import traceback


def fun():
    try:
        print a
    except NameError as e:
        # 打印异常
        # print e
        # 打印异常
        traceback.print_exc()
        # 将异常信息 写到 一个文件中
        traceback.print_exc(file = open('error.txt','w+'))

fun()

def fun1(a,b):
    try:
        print (a + b + c)
    except (TypeError,NameError):
        print 'TypeError,NameError'
f = fun1(2,'a')
print f


# 处理多个异常
def fun2(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        print 'ZeroDivisionError'
    except TypeError:
        print 'TypeError'
f1 = fun2(2,0)
f2 = fun2(2,'b')
print f1,f2

def fun3():
    a = {'b1':1,'b2':2}
    try:
        return a['b3']
    except KeyError as e:
        print e
        print 'KeyError'
    # 只要发生异常,else 就不会执行 ,即执行了except语句后,else不执行
    else:
        print 'else....'
    # 无论如何都执行
    finally:
        print 'finally...'
    return a
f3 = fun3()
print f3
