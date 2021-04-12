"""
Challenge #1:

Write a function that retrieves the last n elements from a list.

Examples:
- last([1, 2, 3, 4, 5], 1) ➞ [5]
- last([4, 3, 9, 9, 7, 6], 3) ➞ [9, 7, 6]
- last([1, 2, 3, 4, 5], 7) ➞ "invalid"
- last([1, 2, 3, 4, 5], 0) ➞ []

Notes:
- Return "invalid" if n exceeds the length of the list.
- Return an empty list if n == 0.
"""

def last(a, n):
    # Your code here
    if n == 0:
        return []
    elif len(a) < n:
        return 'invalid'
    return a[-n:]
​
my_list = [4, 3, 9, 9, 7, 6, 12]
​
# print(last(my_list, 9))
​
# print(my_list[0:3])
​
# print(my_list[:5]) #From zero to 5th index
​
# print(my_list[5:]) # from index 5 to end 
​
# print(my_list[-3:]) # The last 3 elements!
​
print(my_list[5:1:-1]) # Go backwards

