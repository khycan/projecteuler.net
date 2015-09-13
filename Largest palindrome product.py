# Problem 4
"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
# palindromic number : ex) 9009,11 ...

def checkPalindromic(n):
    return n == int(str(n)[::-1])

a = 999
b = 999

result = 0

while a>99:
    while b>99:
        if checkPalindromic(a*b) and result<a*b:
            result = a*b
        b = b-1
    b=999
    a=a-1

print result
