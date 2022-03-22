"""
Capital indexes
https://pythonprinciples.com/challenges/Capital-indexes/

Write a function named capital_indexes. The function takes a single parameter, which is a string. Your function should return a list of all the indexes in the string that have capital letters.

For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].
"""


def capital_indexes(word):
    index_list = []
    for i,w in enumerate(word):
        if w.isupper():
            index_list.append(i)
    return index_list
    
    
print(capital_indexes("Let's pretend that you're the Red Queen, Kitty!")) # [0, 30, 34, 41]
print(capital_indexes("There's the White Queen running across the country! She came flying out of the wood over yonder—How fast those Queens can run!")) # [0, 12, 18, 52, 96, 111]
print(capital_indexes("Now, here, you see, it takes all the running you can do, to keep in the same place. If you want to get somewhere else, you must run at least twice as fast as that!")) # [0, 84]
      

