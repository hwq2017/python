#coding=utf-8

# 在非顶层模块(完成相应功能)中,一般不允许除函数,类之外的顶层代码出现,否则在导入该模块时就会执行该顶层代码
# 顶层模块(调用)

# 可以在一个import下同时导入多个模块,用 , 隔开, 允许多个模块下变量名相同
# import m2,m3

# 如果模块名太长,可以起别名
# import m2 as M

# 重复导入同一模块时,代码只执行一次,可以用内建函数 reload(模块名) 使重复执行,一般针对第三方模块
# import m2
# reload(m2)

import m2
import m3

# from import 用来将模块的部分属性导入到当前的命名空间,如果原来有重名的变量将会被覆盖
# * 将全部导入到当前命名空间
from m3 import *
# 导入模块中受保护成员,不能用 *,如下:
from m3 import _fun

m = m2.Demo('hello')
print m.getName()
print m2.fun(10,20)

m3.func()
m3._fun()



# 包的导入路径内每个目录必须有__init__.py文件,可以写入代码,也可以不写.这样就可以在__init__.py中导入我们所需要的模块

from package import ctime,fun # *

print ctime()
fun()

# 包的导入两种方式:

from package.p import fun
import package.package1.p1
# import package.p

fun()
package.package1.p1.fun()
# package.p.fun()
