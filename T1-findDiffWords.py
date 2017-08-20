#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

#找出两篇英文文档中彼此不包含的单词
#输入：两篇文档的绝对路径，输出文档的绝对路径
#输出：包含查询结果的txt文档

# split words into list
pathA = raw_input('please type the file path A:\n')  # 使用raw_input()代替input()
pathB = raw_input('please type the file path B:\n')
pathOut = raw_input('please type the file out path:\n')

with open(pathA, 'r') as f1:
    sA = f1.read()

l1 = re.split(r'[],;!:\s]', sA)

# print (sA)
# print (l1,len(l1))

with open(pathB, 'r') as f2:
    sB = f2.read()
l2 = re.split(r'[],;!?:""\s]', sB)

# print (sB)
# print (l2,len(l2))

set1=set(l1)
set2=set(l2)
print (set1)
print (set2)

set3 = (set1 - set2)|(set2-set1)  #找出彼此不包含的元素
set4 = set()

print (set3)
for i in set3:
    set4.add(i.lower())   #统一小写，排除同一单词的不同书写形式

with open(pathOut,'w') as f3:
    for i in set4:
        f3.write(i)   #换行写入文件f3
        f3.write('\n')
print (f3)

