#!/usr/bin/env python3
# -*- coding: utf-8 -*-
l = ['apple', 'pear', 'banana']
for fruit in l:
    print(fruit)

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    sum = sum + x
print(sum)

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    sum = sum + x
    print(sum)

for i in range(1,10):
    print(i)

sum=0
for x in range(1,101):
    sum=sum+x
print(sum)

print(list(range(1,101)))

sum =0
n=99
while n>0:
    sum=sum+n
    n=n-2
print(sum)

#利用循环一次打印出Hello, xxx!
L=['Bart','Lisa','Adam']
for name in L:
    print('Hello,',name,'!')
    print('Hello, {0}!'.format(name))

n=0
while n<10:
    n=n+1
    if n%2==0:
        continue
    print(n)


n=1
while n<=100:
    if n>10:
        break
    print(n)
    n=n+1  #如果此条件注释掉，程序将进入死循环
print('END')