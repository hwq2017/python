def outer():
    print ('outer....')
    a = 10
    def inner():
        nonlocal a
        a += 1
        print (a)
        print ('inner....')
    inner()

outer()


def funout(x):
     def funin(y):
         return x * y
     return funin
f = funout(2)
print (f(4))
