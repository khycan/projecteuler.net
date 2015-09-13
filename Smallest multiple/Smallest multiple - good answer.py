# -*- coding: cp949 -*-
# Problem 5
# 최대공약수 알고리즘을 이용한 최소공배수 찾
"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
from fractions import gcd

# lcm (least common multiple)
def lcm(a,b):
    "Calculate the lowest common multiple of two integers a and b"
    return a*b/gcd(a,b)

nlcm = 1
for i in range(2,20+1):
    nlcm = lcm(nlcm,i)

print nlcm
