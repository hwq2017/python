#!/usr/bin/env python
#coding=utf-8
import math

a = math.pow(2,3)
print a
print 'hello world'
print '你好'
print '''hahaha
             hehehe'''
#a = raw_input('input:')
#print a

print 'a = %(a)d,b = %(b)d'%({'a':12,'b':10}),
print '123456'

# 向流中输出
with open('file.text','w+') as fd:
    #print >> fd,'hello world'
    print ('hello world',file = fd) python3
