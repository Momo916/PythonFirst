#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

#去掉开头或结尾的不需要的字符
s='  Hello,     world!   '
print (s)
l=s.strip()  #strip只能去掉开头或结尾的字符，不会对字符串中间对任何文本起作用
print (l)

l2=re.sub('\s+',' ',l)  #\s代表空格，\s+代表多个空格
print (l2)

s='--上海---!--'
l=s.strip('-')
print (l)
l3=re.sub('-+','',l)
print (l3)

s=' {{{}{A:a, B:b}{}}} '
print (s.strip().lstrip('{').rstrip('}')) #lstrip,rsctrip分别从左或右侧开始执行去除操作
