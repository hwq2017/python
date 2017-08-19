#coding=utf-8

# 函数返回值,没有默认返回 None,可以有多个返回值,以元组的形式返回,可以有多个变量接受返回值
def fun():
    return 1,2,3,4
a = fun()
print a   # (1,2,3,4)

a,b,c,d = fun()
print a,b,c,d   # 1,2,3,4 
