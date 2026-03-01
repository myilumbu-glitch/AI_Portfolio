#You are going to be given a non-empty string. Your job is to return the middle character(s) of the string.

#If the string's length is odd, return the middle character.
#If the string's length is even, return the middle 2 characters.


def get_middle(s):
    x = len(s)
    middle = x // 2
    if x % 2 == 0:
            return s[middle-1:middle+1]
    else:
            return s[middle]

#Created 23.02.26
