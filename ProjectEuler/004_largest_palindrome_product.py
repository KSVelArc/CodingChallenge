"""
Largest palindrome product
https://projecteuler.net/problem=4

Problem 4
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
import time
t0 = time.time()

three_digit = []

for i in range(100,1000):
    for j in range(100,1000):
        x = i * j
        if str(x) == str(x)[::-1]:
            three_digit.append(x)

answer = max(three_digit)

t1 = time.time()

print('The largest palindrome made from the product of two 3-digit numbers is: {}'.format(answer))

print('\ntime:', t1-t0)

#print('Answer: 906609')

