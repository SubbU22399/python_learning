Names =["Sara", "David", "Warner", "Sandy", "Tom", "Shiva"]

Upper_Names = list(map(str.upper, Names))
print(Names)
print(Upper_Names)

circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013] 
result = list(map(round, circle_areas, range(1, 7))) 
print(result)

numbers = [1, 2, 3, 4, 5]

output = zip(Names, numbers)
print(list(output))