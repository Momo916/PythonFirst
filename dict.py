#!/usr/bin/env python3
# -*- coding: utf-8 -*-
d={'Michael':95,'Tom':98,'Lily':80}
print(d['Tom'])

d['Amy']=92
print(d)

d['Tom']=100
print(d)

if 'Kanm' in d:
    print(d['Kanm'])
else:
    print('not exist Kanm')
