"""
Min-maxing
https://pythonprinciples.com/challenges/Minmaxing/

Define a function named largest_difference that takes a list of numbers as its only parameter.

Your function should compute and return the difference between the largest and smallest number in the list.

For example, the call largest_difference([1, 2, 3]) should return 2 because 3 - 1 is 2.

You may assume that no numbers are smaller or larger than -100 and 100.
"""


def largest_difference(nums):
    smallest = min(nums)
    largest = max(nums)
    
    return largest - smallest


print(largest_difference([1, 2, 3])) # 2
print(largest_difference([22, 3, 22])) # 19
print(largest_difference([12, 9, 83])) # 74

