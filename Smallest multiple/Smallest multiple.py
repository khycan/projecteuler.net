# -*- coding: cp949 -*-
# Problem 5
# 비효율(inefficiency)적으로 풀었다. "최소공배수" 알고리즘을 이용하는 것이 효율적이다.
"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
a=20
result=1

Flag = []
tmpFlag = []

def compareFlag(src, dst, i):
    if dst[i]<src[i]:
        dst[i]=src[i]

# In fact, 'factorization' is 'insu boonhae'. 'soinsu boonhae' is 'factorization in prime factors'.
def factorization( number ):
    while(number%2 == 0):
        tmpFlag[2]+=1
        number/=2
    compareFlag(tmpFlag, Flag, 2)
    tmpFlag[2]=0
    # prime factor
    sosu=3
    while(number!=1):
        while(number%sosu == 0):
            tmpFlag[sosu]+=1
            number/=sosu
        compareFlag(tmpFlag, Flag, sosu)
        tmpFlag[sosu]=0
        sosu+=2

# initialize list value
for i in range(a+1):
    Flag.append(0)
    tmpFlag.append(0)

# factorize in prime factors from 20 to 3
while a>2:
    factorization(a)
    a-=1

for i in range(2,21):
    for j in range(Flag[i]):
        result*=i

print result
