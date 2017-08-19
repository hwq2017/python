#coding=utf-8

# 拦截

# 魔法属性: __doc__ (文档字符串), __class__ , __dict__ (类与对象的所有成员,类输出的是全局的函数,变量等信息,对象输出的是对象拥有的普通变量),

# 魔法方法: __getattr__ , __setattr__ ,__init__, __new__ , __call__(模拟函数行为)
class A(object):
    ''' magic 魔法方法 '''
    pass

a = A()

print a.__doc__
print a.__class__
print a.__dict__


class B(object):

    # 对象的初始化,一个实例方法,第一个参数是self
    def __init__(self):
        print '__init__ ...'
        self.dict = {}

    # 用于对象的创建,是一个静态方法,第一个参数为cls,执行完new后在执行init,且参数要一一对应
    def __new__(cls):
        print '__new__ ...'
        return super(B,cls).__new__(cls)

    #  当程序结束后,所有的实例都会被析构(垃圾回收机制),即调用此方法
    def __del__(self):
        print '__del__ ...'

    # 模拟函数的行为
    def __call__(self,n):
        print '__call__ ...',n


    # 如果 name 被访问,但同时它又不存在,就会调用此方法,从对象中读取某个属性时，首先需要从self.__dicts__中搜索该属性，再从__getattr__中查找。
    def __getattr__(self,name):
        print 'you use getattr'


    # 如果要给 name 赋值,就会调用此方法,设置对象的属性
    def __setattr__(self,name,data):
        print 'you use setattr'
        self.__dict__[name] = data
        print name

    # 用来删除对象的属性时调用
    def __delattr__(self,name):
        print 'you use delattr'


    #  用于索引操作,如字典. 分别表示获取,设置
    def __getitem__(self,key):
        return self.dict[key]
    def __setitem__(self,key,value):
        self.dict[key] = value

    # 返回元素的数量
    def __len__(self):
        return len(self.dict)

b = B()
b('hello')
b['a'] = 1     # 调用setitem
print b['a']   # 调用getitem
b.value
b.value = 5
del b.value
print len(b)
print b.__dict__
# print B.__dict__
