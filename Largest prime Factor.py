# -*- coding: cp949 -*-
# Problem 3
# ���� ū ���μ� ã�� 
"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
number = 600851475143

prmfactor = 3

while number>prmfactor :
    if number%prmfactor != 0:
        prmfactor = prmfactor + 1
        continue
    number /= prmfactor

print prmfactor
