"""
Smallest multiple
https://projecteuler.net/problem=5

Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
import time
t0 = time.time()

def smallest_multiple(n):
    cont = True
    increasing_num = n

    while cont:
        increasing_num += 1
        c = 0
        for i in range(1,n+1):
            if increasing_num % i == 0:
                continue
            else:
                c += 1
        if c == 0:
            print(increasing_num)
            cont = False
            break
        else:
            continue

    return increasing_num

answer = smallest_multiple(20)

t1 = time.time()

print('The smallest positive number that is evenly divisible by all the numbers in range 1-20 is: {}'.format(answer))

print('\ntime:', t1-t0)

#print('\nAnswer: 232792560')
#EXTREMELY SLOW SCRIPT RUNS AT 408 SECONDS!