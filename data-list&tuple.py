#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#list
L=[['Apple','Google','Microsoft'],[1,2,3],[True,False]]
#打印Apple：
print(L[0][0])
#打印True：
print(L[-1][0])
#打印2
print(L[1][-2])
#追加
L.append('ABC')
print(L)
#插入
L[1].insert(1,'o')
print(L[1])
#删除
L[2].pop()
print(L[2])
#修改
L[0][0]='Applepen'
print(L[0])

#tuple
t=(1,)
print(t)
t=(1,'A',False)
print(t[1])