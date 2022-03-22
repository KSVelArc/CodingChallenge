"""
Online status
https://pythonprinciples.com/challenges/Online-status/

The aim of this challenge is, given a dictionary of people's online status, to count the number of people who are online.

For example, consider the following dictionary:

statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}
In this case, the number of people online is 2.

Write a function named online_count that takes one parameter. The parameter is a dictionary that maps from strings of names to the string "online" or "offline", as seen above.

Your function should return the number of people who are online.
"""


"""
def online_count(d):
    values = list(statuses.values())
    return values.count('online')


statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}

print(online_count(statuses))
"""


"""
def online_count(d):
    c=0
    for k,v in statuses.items():
        if v == "online":
            c+=1
    return c


statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}

print(online_count(statuses))
"""


def online_count(statuses):
    c = 0
    for key in statuses:
        if statuses[key] == "online":
            c += 1
    return c


statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}


print(online_count(statuses)) # 2



