#coding=utf-8


a = input('input:')
b = input('input:')
c = input('input:')
if a > b:
    tmp = a
    a = b
    b = tmp
if a > c:
    tmp = a
    a = c
    c = tmp
if b > c:
    tmp = b
    b = c
    c = tmp
print '%d,%d,%d'%(a,b,c)
