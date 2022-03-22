"""
Anagrams
https://pythonprinciples.com/challenges/Anagrams/

Two strings are anagrams if you can make one from the other by rearranging the letters.

Write a function named is_anagram that takes two strings as its parameters. Your function should return True if the strings are anagrams, and False otherwise.

For example, the call is_anagram("typhoon", "opython") should return True while the call is_anagram("Alice", "Bob") should return False.
"""


def is_anagram(s1,s2):
    s1_sorted = sorted(s1.lower())
    s2_sorted = sorted(s2.lower())
    
    if s1_sorted == s2_sorted:
        return True
    else:
        return False


print(is_anagram("typhoon", "opython")) # True
print(is_anagram("Alice", "Bob")) # False 

