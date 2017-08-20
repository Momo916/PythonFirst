#!/usr/bin/env python3
# -*- coding: utf-8 -*-
age = 10
if age > 18:
    print('your age is', age)
elif age > 10 and age <= 18:
    print('teenager')
else:
    print('child')

l = []
if l:
    print(True)
else:
    print(False)

str = input('please input a integer:')
birth = int(str)
if birth > 2000:
    print('00后')
else:
    print('00前')
