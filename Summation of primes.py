# -*- coding: cp949 -*-
# Problem 10
# 나는 brute force 방법으로 풀었지만
# 효율적인 풀이는 "에라토스테네스의 체"의 알고리즘이다.
"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
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

a=3
sumOfprimes = 2
while a<2000000:
    if isFactorization(a):
        sumOfprimes+=a
    a+=2

print sumOfprimes
