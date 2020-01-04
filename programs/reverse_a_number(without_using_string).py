#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 10:08:36 2020

@author: trinity
"""

a = 1
n = int(input("A number to be reversed should be entered by you: "))
for i in range(n+1):
    if a*10 == i:
        a *= 10
backup, new_backup,one_more= a,a,a
l = []
while a > 0.1:
    l.append(int(n/a))
    a //= 10
new_list = [l[0]*new_backup]
v = 0
while backup > 1:
    new_list.append(l[v+1]*backup//10 - l[v]*backup)
    backup //= 10
    v += 1
reverse = 0
b = 0
for i in new_list:
    new_list[b] /= one_more
    one_more /= 10
    b += 1
for i in range(1,len(new_list)+1):
    reverse += new_list[-i] * new_backup
    new_backup /= 10
print(int(reverse))
