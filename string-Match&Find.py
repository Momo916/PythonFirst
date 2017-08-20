#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

# 查找字符串 index, find, rindex, rfind
sParent = 'apple I have an appapplepine'
sKid = 'apple'
matchStart = sParent.index(sKid)
print (matchStart)  # index()返回匹配串第一个匹配字符的index，查不到时会抛出异常
print (sParent.rindex(sKid))  # rindex从字符串的末尾开始找

sKid = 'applo'
print (sParent.find(sKid))  # find()查不到时返回-1
print (sParent.find('apple', 2))  # 从下标2开始，查找在字符串里第一个出现的子串

print (sParent.find('apple'))
print (sParent.rfind('apple'))  # rfind()从字符串的末尾开始找


# 匹配特定文本模式match, findall
if (re.match('apple', sParent)):
    print 'yes'
else:
    print 'no'

aa = re.compile('apple')
l = aa.findall(sParent)
print (len(l))

date1 = 'today is 11/21/2017, and tomorrow is 11/22/2017'
datepattern = re.compile(r'\d+/\d+/\d+')  #模式，\d+匹配多个数字；\s+匹配多个字符
l = datepattern.findall(date1)  # 匹配到的值存入list
print (l)
