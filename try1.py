#coding=utf-8

class MyError(Exception):
    pass

try:
    s = None
    if s is None:
        print 's 是空对象'
        # 抛出异常后,后面的代码不执行
        raise MyError('error')
    print len(s)
except MyError as e:
    print '空对象没有长度'
    print e.args     # 打印异常信息,即 error
