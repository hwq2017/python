#coding=utf-8

def func():
    print 'hello world'
    return
func()


def fun(a,b):
    return a+b
a = fun(1,2)
print a

def fun1(str):
    '打印'
    print str
    return
fun1('你好 世界')





# 可变参数(列表,字典)和不可变参数(数字,字符串,元组)

def fun2(a):
    a = 10
    print '函数:', a # 10

a = 100
fun2(a)
print a  # 100


def fun3(c):
    c[0] = 10
    print '函数:', c # [10,2,3,4]

l = [1,2,3,4]
fun3(l)
print l   # [10,2,3,4]


def fun4(c):
    c[0] = 10
    print '函数:', c # [10,2,3,4]

l = [1,2,3,4]

l1 = l[:]    # 通过复制,解决可变参数值改变的缺陷

fun4(l1)
print l   # [1,2,3,4]
