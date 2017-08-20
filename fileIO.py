#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 读文件
filePath = '/Users/momo/Documents/GitHub/PythonFirst/source/A.txt'

with open(filePath, 'r') as f:
    for line in f.readlines():
        print (line.strip())

f = open(filePath, 'r')
print (f.read())
f.close()

# 写文件
with open(filePath, 'at') as f:  # at模式在文件末尾追加；w模式重写整个文件
    f.write('\nhello, world')

with open(filePath, 'r') as f:
    print(f.read())
