#coding=utf-8

class C1(object):
    text = 'hello world'
    age = 12

class C2(object):
    text = '你好 世界'
    gender = '男'

class C(C1,C2):
    pass

c = C()
print c.text
print c.age
print c.gender

print issubclass(C,C1) # True 'C 是否继承 C1',判断是否有继承关系
print isinstance(c,C1) # True 判断一个对象是不是某一个类的对象


print C.__mro__ # 方法解析顺序
