"""
Double letters
https://pythonprinciples.com/challenges/Double-letters/

The goal of this challenge is to analyze a string to check if it contains two of the same letter in a row. For example, the string "hello" has l twice in a row, while the string "nono" does not have two identical letters in a row.

Define a function named double_letters that takes a single parameter. The parameter is a string. Your function must return True if there are two identical letters in a row in the string, and False otherwise.
"""


"""
def double_letters(word):
    for l in range(len(word)):
        if l < len(word)-1:
            a = word[l]
            b = word[l+1]
            if a == b:
                return True
    return False

print(double_letters("Jabberwock"))
print(double_letters("Bandersnatch"))
"""


def double_letters(word):
    for l in range(len(word)-1):
        a = word[l]
        b = word[l+1]
        if a == b:
            return True
    return False


print(double_letters("Jabberwock")) # True
print(double_letters("Bandersnatch")) # False

