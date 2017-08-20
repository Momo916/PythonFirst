#!/usr/bin/env python3
# -*- coding: utf-8 -*-
s = set([1, 2, 8, 1, 8])
print (s)  # 打印的集合从小到大排列，并去重
s.add(9)
print (s)
s.add(9)
print (s)
s.remove(8)
print (s)

t = ([2, 3, 0])
# print (s & t)
# print (s | t)
s.discard(1)
print (s)

l = [1, 2, 8, 9, 0, 2, 3, 'A']
print (len(l))
s2 = set(l)
print (s2)
s3 = set([1, 2, 8, 9, 0, 2, 3])
print (s3)
print (len(s2))
tu = (1, 2, 3)
print (set(tu))
tu2 = (1, [1, 2])
print (tu2)
# print (set(tu2)) #TypeError:unhashable type: 'list'，tu2包含list
