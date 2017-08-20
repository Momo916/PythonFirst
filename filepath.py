#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

path = '/Users/momo/Documents/GitHub/PythonFirst/source/A.txt'
s = os.path.basename(path)
print (s)

s = os.path.dirname(path)
print (s)

print (os.path.split(path))

path2 = '~/Documents/GitHub/PythonFirst/source'
homedir = os.path.expanduser(path2)
print (homedir)

print (os.path.join('temp',path2))

print (os.path.exists(s))
print (os.path.isfile(s))
print (os.path.isdir(s))
print (os.path.islink(s))

import time
time.ctime(os.path.getmtime(s))  ##???

