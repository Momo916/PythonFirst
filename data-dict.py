#!/usr/bin/env python3
# -*- coding: utf-8 -*-
d = {'Michael': 95, 'Tom': 98, 'Lily': 80}
print(d['Tom'])

d['Amy'] = 92
print(d)

d['Tom'] = 100
print(d)

# 如果key不存在，两种方式避免发生错误
if 'Kanm' in d:
    print(d['Kanm'])
else:
    print('not exist Kanm')

print (d.get('Ton'))
print (d.get('Ton', -1))

# 删除一个key
d.pop('Tom')
print (d)
