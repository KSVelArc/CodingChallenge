"""
Multiples of 3 or 5
https://projecteuler.net/problem=1

Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
import time
t0 = time.time()

def multiples_3_or_5(num):
    nums = []
    for i in range(0,num):
        if i % 3 == 0 or i % 5 == 0:
            nums.append(i)
    return sum(nums)

answer = multiples_3_or_5(1000)

t1 = time.time()

print('The sum of the multiples of 3 or 5 is: {}'.format(answer))

print('\ntime:', t1 - t0)

#print('\nAnswer = 233168')

