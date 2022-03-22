"""
Largest prime factor
https://projecteuler.net/problem=3

Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import time
from math import sqrt
t0 = time.time()

def check_if_prime(n):
    for f in range(2, int(sqrt(n))):
        if n % f == 0:
            return False
    return True

num = 600851475143
prime_factors = []
for i in range(2, int(sqrt(num))):
    if num % i == 0:
        if check_if_prime(i):
            prime_factors.append(i)

print(prime_factors)
answer = max(prime_factors)

t1 = time.time()

print('The prime factors of 600851475143 are: {}:'.format(prime_factors))
print('The largest prime factor of 600851475143 is: {}'.format(answer))

print('\ntime:', t1-t0)

#print('\nAnswer = 6857')

