name = "Subbu"
age = 25
print("My name is", name, "and age is", age)  # using comma
print("My name is " + name + " and age is " + str(age))  # using + operator
print("My name is {} and age is {}".format(name, age))  # using format() method
print("my name is %s!" %name)   # using %s
print("my age is %d!" %age)   # using %d
print("my name is %s and age is %d!" %(name, age))   # using %s and %d


list = [1,2,3,4,5]
print("List is:", list) # using comma
print("List is: %s" %list)  # using %s
print("List is: %s" %(list))    # using %s
print("List is: %s" %str(list)) # using %s





# Here are some basic argument specifiers you should know:

# %s - String (or any object with a string representation, like numbers)

# %d - Integers

# %f - Floating point numbers

# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

# %x/%X - Integers in hex representation (lowercase/uppercase)