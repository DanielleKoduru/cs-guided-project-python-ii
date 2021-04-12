"""
Challenge #2:

Given a list of numbers, create a function that returns the list but with each
element's index in the list added to itself. You should add 0 to the number at
index 0, add 1 to the number at index 1, etc.

Examples:
- add_indexes([0, 0, 0, 0, 0]) ➞ [0, 1, 2, 3, 4]
- add_indexes([1, 2, 3, 4, 5]) ➞ [1, 3, 5, 7, 9]
- add_indexes([5, 4, 3, 2, 1]) ➞ [5, 5, 5, 5, 5]

Notes:
- The input list will only contain integers.
"""

def add_indexes(numbers):
    # Your code here
    new_list = []
    for index, value in enumerate(numbers):
        sum = index + value
        # Add this value to the new_list
        new_list.append(sum)
​
    return new_list
​
​
my_list = [1, 2, 3, 4, 5] 
print(add_indexes(my_list))
​
# x = 5
# while x > 0:
#     print(x)
#     x -= 1
​
# for(var i = 0; i < length, i++)
# # If you want just the indeces use range
# for index in range(len(my_list)):
#     print(index)
​
# # Print all values in the list
# for val in my_list:
#     print(val)
​
​
# #Print both value AND index in a list? 
# print(list(enumerate(my_list)))
​
# for index, value in enumerate(my_list):
#     print(index, value)