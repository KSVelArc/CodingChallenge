"""
Sum square difference
https://projecteuler.net/problem=6

Problem 6
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 3025
Hence, the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .
3025 - 385 = 2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
import time
t0 = time.time()

def sum_square_difference(n):
    first_nums = []
    for i in range(1,n+1):
        first_nums.append(i)

    square_sum = sum(first_nums)**2
    sum_squares = sum([i**2 for i in first_nums])
    return square_sum - sum_squares

answer = sum_square_difference(100)

t1 = time.time()

print('The difference between the sum of the squares of the first 100 natural numbers and the square of the sum is: {}'.format(answer))

print('\ntime:', t1-t0)

#print('Answer: 25164150')