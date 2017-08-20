#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 复制字符串
s1 = 'abc'
print (s1)
s2 = s1
print (s2)
s1 = '123'
print (s1, s2)

# 连接字符串
s = s1 + s2  # 使用加号连接字符串，实际上是new一个str，当连接数较多时，浪费资源
print (s)

l = ['hello', 'kitty', '!', 'bye']
sCombine = ' '.join(l)  # 使用join连接字符串更高效
print (sCombine)
print ('{} and {}'.format(s1,s2)) #format组合复杂的拼接

# 字符串长度
print (len(s))


# 大小写转换
def UpperWords(s):
    return s.upper()


print (UpperWords(s))


# 追加指定长度的字符串
def AddSubStr(s1, s2, n):
    return s1 + s2[0:n]


print (AddSubStr(s1, s2, 2))

# 取出字符串中指定位置的字符
print (s[1])  # 截取第二个字符
print (s[1:3])  # 截取第二位到第三位的字符
print (s[:])  # 截取字符串的全部字符
print (s[1:])  # 截取第二个至结尾的所有字符
print (s[-3:])  # 截取倒数第三位到结尾
print (s[:-2])  # 截取从开头到倒数第二个字符之前的所有字符
print (s[::-1])  # 创造一个与原字符串顺序相反的字符串  ###字符串倒序／反转
print (s[:-2:-1])  # 逆序截取
