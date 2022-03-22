"""
Type check
https://pythonprinciples.com/challenges/Type-check/

Write a function named only_ints that takes two parameters. Your function should return True if both parameters are integers, and False otherwise.

For example, calling only_ints(1, 2) should return True, while calling only_ints("a", 1) should return False.
"""


"""
def only_ints(first,second):
    if isinstance(first, int) and isinstance(second, int):
        return True
    else:
        return False


print(only_ints(1, 2))
print(only_ints("a", 1))
"""


def only_ints(first,second):
    if type(first) == int and type(second) == int:
        return True
    else:
        return False


print(only_ints(1, 2)) # True
print(only_ints("a", 1)) # False
