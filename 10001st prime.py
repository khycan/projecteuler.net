# -*- coding: cp949 -*-
# Problem 7
# 나는 brute force 방법으로 풀었지만
# 효율적인 풀이는 "에라토스테네스의 체"의 알고리즘이다.
"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
# In fact, 'factorization' is 'insu boonhae'. 'soinsu boonhae' is 'factorization in prime factors'.
def isFactorization( number ):
    # prime factor
    sosu=3
    while(sosu<number):
        if number%sosu == 0:
            return False
        sosu+=2
    return True


a=1
cnt=1
while cnt<10001:
    a+=2
    if isFactorization(a):
        cnt+=1

print a
