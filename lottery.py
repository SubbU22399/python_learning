import random

def lottery():
    # Returns 6 numbers between 1 and 40
    for i in range(6):
        yield random.randint(1, 40)

    # Returns a 7th number between 1 and 15
    yield random.randint(1,15)

for random_number in lottery():
    print("And the next number is... %d!" %(random_number))

a = set(["Jake", "John", "Eric"]) 
b = set(["John", "Jill"]) 
a.add("Subbu")
b.add("Sai")
a.add("Siva")
b.add("Subbu")
print(a.intersection(b)) 
print(b.intersection(a))