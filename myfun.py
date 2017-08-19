#coding=utf-8

def dec1(func):
    def fun(b):
        print '----',b
        func(b)
    return fun

@dec1
def fun1(a):
    print a
fun1(4)



def dec(defauf):
    def dec2(func):
        def fun(str):
            l = len(str)
            if l < 4:
                print '不能小于四位',defauf
            elif l > 8:
                print '不能大于八位',defauf
            else:
                func(str)
        return fun
    return dec2

# def reg(name):
#     return name
name = raw_input()

@dec('he')
def fun2(name):
    print name


fun2(name)
