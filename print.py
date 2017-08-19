#!/usr/bin/env python
#coding=utf-8

a ,b = 123,10.456
print 'a = %10d'%a  # 10 表示宽度
print 'a = %10f'%b  # 10 表示宽度






# 向流中输出
with open('demo.text','w+') as fd:
    print >> fd,'你好,世界'
    # print ('2017年后',file = fd)  # python3写法
