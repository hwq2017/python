#coding=utf-8

class Person(object):
    def __init__(self):
        self.gender = 'man'
        self.__name = 'wang'
    def __fun(self):
        print 'i am Person'


    # @property
    # def name(self):
    #     return self.__name
    # @name.setter
    # def name(self,name):
    #     if 4 <= len(name) <= 8:
    #         self.__name = name
    #     else:
    #         pass
    def getName(self):
        return self.__name

    def setName(self,name):
        if 4 <= len(name) <= 8:
            self.__name = name
        else:
            pass


    def fun(self):
        self.__fun()


class Girl(Person):
    pass



t = Person()

# t.name = 'lisi'
# print t.name



t.setName('lal')
print t.getName()
t.fun()
