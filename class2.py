#coding=utf-8

class Person(object):
    eye = 2
    mouse = 1
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name
    def setName(self,n):
        self.name = n
    def run(self):
        print 'run'

class Child(Person):
    pass

class Adult(Person):
    def run(self):
        print 'run quickly!'


class Old(Person):
    age = 80

c = Child('小强')
a = Adult('大白')
o = Old('老李')

c.setName('小明')
print c.getName()
print c.eye

a.run()

print o.age
