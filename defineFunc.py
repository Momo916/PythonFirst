#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


print (my_abs(9))
print (my_abs(-9))

print (my_abs('A'))  # 如何处理的？？
