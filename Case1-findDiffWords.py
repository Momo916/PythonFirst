#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import os
# 找出两篇英文文档中彼此不包含的单词，测试文件/PythonFirst/source
# 输入：两篇文档的绝对路径，输出文档的绝对路径
# 输出：包含查询结果的文档

# 判断输入的文件路径是否存在
def typeFilePath(path):
    flag=os.path.isfile(path)
    while not flag:
        path = raw_input('please type correct path with file name:\n')
        flag = os.path.isfile(path)
    return path

pathA = typeFilePath(raw_input('please type the file path include file name A:\n'))
pathB = typeFilePath(raw_input('please type the file path include file name B:\n'))


pathOut = raw_input('please type the file out path include file name:\n')
flag=os.path.isdir(pathOut)
while flag:
    pathOut = raw_input('please type correct path with file name:\n')
    flag = os.path.isdir(pathOut)

#拆分文件A
with open(pathA, 'r') as f1:
    sA = f1.read()

l1 = re.split(r'[],.;!:\s]', sA)

#拆分文件B
with open(pathB, 'r') as f2:
    sB = f2.read()
l2 = re.split(r'[],.;!?:\s]', sB)

# 找出彼此不包含的元素
set1 = set(l1)
set2 = set(l2)
set3 = (set1 - set2) | (set2 - set1)

set4 = set()
for i in set3:
    set4.add(i.lower())  # 统一小写，排除同一单词的不同书写形式

with open(pathOut, 'w') as f3:
    for i in set4:
        f3.write(i)  # 换行写入文件f3
        f3.write('\n')
print (f3)
