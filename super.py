#coding=utf-8

class Person(object):
    def __init__(self,name):
        self.name = name
    def about(self,height):
        print '%s is about %d'%(self.name,height)

class Girl(Person):
    def __init__(self,name,breast):
        super(Girl,self).__init__(name)
        self.breast = breast
    def about(self,height):
        super(Girl,self).about(height)
        print self.breast


li = Girl('lili',80)
li.about(160)

super(Girl,li).about(170)
