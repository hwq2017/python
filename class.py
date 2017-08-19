#coding=utf-8

class FirstClass(object):

    def __init__(self,name):
        self.name = name
    def changAge(self,n):
        self.age = self.age + n
    def getName(self):
        return self.name
    def getage(self):
        return self.age
    def fname(self):
        print 'lalala'


two = FirstClass('two')
two.age = 12
two.changAge(5)
print two.getName()
print two.getage()




class Person(object):
    gender = '男'
    age = 20
    first = FirstClass('first')
    def __init__(self,name):
        self.name = name
    def getName(self):
        return self.name
    def fun(self):
        print '===',self.age
    def func(self,hobby):
        print self.name ,"'s hobby is",hobby



lisi = Person('lisi')
lisi.age = 19
lisi.fun()
lisi.first.fname()
lisi.func('read book')
print lisi.getName()
print lisi.gender
print Person.gender
