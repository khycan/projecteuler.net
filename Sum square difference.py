# -*- coding: utf-8 -*-
# Problem 6
# 등차수열의 합과 제곱들의 합 공식을 이용하여야 효율적
"""
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102(2 is square) = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552(2 is square too) = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
sumOfSquares = 0
squareOfSum = 0

n = 100

# sum of squares fomula
sumOfSquares = (n*(n+1)*(2*n+1))/6

# sum of natural numbers fomula
squareOfSum = (n*(n+1))/2
squareOfSum *= squareOfSum

print squareOfSum - sumOfSquares
