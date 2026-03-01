#Task:
#Given a list of integers, determine whether the sum of its elements is odd or even.

#Give your answer as a string matching "odd" or "even".

#If the input array is empty consider it as: [0] (array with a zero).

def odd_or_even(arr):
    # Handle empty list
    if not arr:
        arr = [0]
    
    total = sum(arr)
    if total % 2 == 0:
        return 'even'
    else:
        return 'odd'

