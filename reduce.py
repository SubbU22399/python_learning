from functools import reduce
numbers = [1, 2, 3, 4, 5]

def custom_sum(first, second):
    return first + second

result = reduce(custom_sum, numbers)
print("Normal usual sum :", result)
 
Extended_result = reduce(custom_sum, numbers, 100)
print("Extended_result using Reduce initial aurgment :" , Extended_result)