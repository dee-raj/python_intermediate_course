"""
Comprihencing is a fast way of creating new list from existing one.
"""
numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers)

numbers_square= [i*i for i in numbers]
print(numbers_square)

is_even = [i%2==0 for i in numbers]
print(is_even)

