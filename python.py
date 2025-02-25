from Functions import Addition

from Addition  import Addition


print("Hello_world form myside as a python Learner")
a,b = 10,20
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)
print(a**b)
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print(a and b)
print(a or b)
print(not a)
print(not b)
print(a&b)
print(a|b)
print(a^b)
print(~a)
print(~b)
print(a<<b)
print(a>>b)
print(a is b)
print(a is not b)


mystr = "subbu"
print(mystr)
print(mystr[0])
print(mystr[1])
print(mystr[2])
print(mystr[3])
print(mystr[4])

# add = Addition(10, 20)
# print(add.add1())
# print("Hello_world form myside as a python Learner")

add = Addition(10, 20, 30)
print(add.add())



PhoneBook = {}
PhoneBook["subbu"] = 1234567890
PhoneBook["sai"] = 1234567891
PhoneBook["siva"] = 1234567892
PhoneBook["sadhu"] = 1234567893

print(PhoneBook)


PhoneBook2 = {
    "subbu": 1234567890,
    "sai": 1234567891,
    "siva": 1234567892,
    "sadhu": 1234567893
}
print(PhoneBook2)

print("________________________________________________________________________________________________________________________________________________________________")

PhoneBook3 = dict(subbu=1234567890, sai=1234567891, siva=1234567892, sadhu=1234567893)
print(PhoneBook3)

print(PhoneBook3["subbu"])
print(PhoneBook3.get("subbu"))  # get() is used to get the value of the specified key
print(PhoneBook3.keys())  # keys() is used to get the keys of the dictionary
print(PhoneBook3.values())  # values() is used to get the values of the dictionary
print(PhoneBook3.items())  # items() is used to get the key-value pairs of the dictionary
print(PhoneBook3.pop("subbu"))  # pop() is used to remove the specified key
print(PhoneBook3)
print("________________________________________________________________________________________________________________________________________________________________")
for name, number in PhoneBook3.items():
    print(name, number)

del PhoneBook3["sai"]  # del is used to remove the specified key
print(PhoneBook3)