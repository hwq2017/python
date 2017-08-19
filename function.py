#coding=utf-8




a = input('please input string:')
for i in a:
    if i == ' ':
        b = a.replace(i,'-')
print b


def func(str):
    for i in str:
        if i == ' ':
            b = str.replace(i,'-')
    print b
