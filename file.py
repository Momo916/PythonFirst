#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#read
filePath = '/Users/momo/Documents/GitHub/PythonFirst/source/A.txt'

with open(filePath, 'r') as f:
    for line in f.readlines():
        print (line.strip())

f = open(filePath, 'r')
print (f.read())
f.close()

#write
with open(filePath, 'at') as f:
    f.write('\nhello, world')
with open(filePath, 'r') as f:
    print(f.read())
