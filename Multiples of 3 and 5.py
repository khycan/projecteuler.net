# Problem 1
"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""
sumresult = 0

iterator = 0

while iterator<1000:
    sumresult += iterator
    iterator += 3

iterator = 0
while iterator<1000:
    sumresult += iterator
    iterator += 5

iterator = 0
while iterator<1000:
    sumresult -= iterator
    iterator += 15

print sumresult
