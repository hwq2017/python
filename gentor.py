
def fid(max):
    a,b = 0,1
    while a < max:
        print '====',a
        yield a
        a,b = b,a + b
        print '*********'
fid(20)
t = fid(10)
t.next()
print '-------------------'
t.next()
# for i in t:
#     print i
