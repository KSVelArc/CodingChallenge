"""
10001st prime
https://projecteuler.net/problem=7

Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
import time
t0 = time.time()

def nth_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

prime_nums = []
limit = True
n = 1

while limit:
    n += 1
    answer = (nth_prime(n))
    if answer:
        prime_nums.append(n)
    if len(prime_nums)==10001:
        limit = False

answer = prime_nums[-1]

t1 = time.time()

print('The 10,001st prime number: {}'.format(answer))

print('\ntime:', t1-t0)

#print('\nAnswer: 104743')


