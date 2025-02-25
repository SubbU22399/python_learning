nums = [1,2,3,4,5]
for prime in nums:
    print(prime)    # 1,2,3,4,5

for x in range(10):   # 0,1,2,3,4,5,6,7,8,9
    print(x)

for x in range(10,20):    # 10,11,12,13,14,15,16,17,18,19
    print(x)

for x in range(10,20,2):    # 10,12,14,16,18
    print(x)
print("__________")  

for x in range(20,10,-1):   # 20,19,18,17,16,15,14,13,12,11
    print(x)

print("__________")
for x in range(20,10,-2):   # 20,18,16,14,12
    print(x)
print("__________")
for x in range(3,20,10):    # 3,13
    print(x)

print("_____While loop_____")

count = 0;
while count <= 5:
    print(count)
    count += 1
print("_____Break loop_____")

count = 0;
while True:
    print(count)
    count += 1
    if count > 5:
        break
print("_____Break loop_____")

for x in range(10):
    if x % 2 == 0:
        continue
    print(x)

print("_____Continue loop_____")

for x in range(10):
    if x % 2 != 0:
        continue
    print(x)
print("_____Continue loop_____")

for x in range(10):
    if x % 2 == 0:
        pass
    else:
        print(x)
print("_____Pass loop_____")

for x in range(1,10):
    if x % 2 == 0 and x % 3 == 0:
       continue 
    else:
        print(x)
print("_____Continue loop_____")
