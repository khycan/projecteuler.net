# -*- coding: utf-8 -*-
# Problem 9
# 이거는 걍 brute force 
"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
result = 0

def t():
    for i in range(3,500):
        for j in range(i+1,500):
            for k in range(j+1,500):
                if i*i+j*j == k*k:
                    if i+j+k == 1000:
                        return i*j*k


print t()
