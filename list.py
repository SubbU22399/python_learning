my_list =[]
my_list.append("Subbu")     # append() is used to add the element at the end of the list
my_list.append("Hari")
my_list.append("Raju")
my_list.append("Ravi")
print(my_list)  

my_list.insert(1,"Sai")    # insert() is used to add the element at the specified index
print(my_list)

my_list.remove("Ravi")      # remove() is used to remove the specified element
print(my_list)

my_list.pop(2)        # pop() is used to remove the element at the specified index
print(my_list)

my_list.clear()     # clear() is used to remove all the elements from the list
print(my_list)  

my_list = ["Subbu","Hari","Raju","Ravi"]    # list is reinitialized
print(my_list)

my_list1 = my_list.copy()    # copy() is used to copy the list
print(my_list1)

my_list2 = list(my_list)    # list() is used to copy the list
print(my_list2) 

my_list3 = my_list1 + my_list2    # + is used to concatenate the two lists
print(my_list3)

my_list4 = my_list1 * 2    # * is used to repeat the list
print(my_list4)     

my_list5 = list(("Subbu","Hari","Raju","Ravi"))    # list() is used to create a list
print(my_list5) 

my_list6 = my_list5[1:3]    # slicing is used to get the elements from the specified range
print(my_list6)

my_list7 = my_list5[-3:-1]    # negative indexing is used to get the elements from the specified range
print(my_list7)

my_list8 = my_list5[1:]    # slicing is used to get the elements from the specified range
print(my_list8)

my_list9 = my_list5[:3]    # slicing is used to get the elements from the specified range
print(my_list9)

my_list10 = my_list5[1:3:2]    # slicing is used to get the elements from the specified range
print(my_list10)

my_list11 = my_list5[::-1]    # reverse the list
print(my_list11)

my_list12 = my_list5[-1::-1]    # reverse the list
print(my_list12)

my_list13 = my_list5[::2]    # slicing is used to get the elements from the specified range
print(my_list13)

my_list14 = my_list5[-1::-2]    # slicing is used to get the elements from the specified range
print(my_list14)

my_list15 = my_list5[-1:1:-1]    # slicing is used to get the elements from the specified range
print(my_list15)

my_list16 = my_list5[-1:1:-2]    # slicing is used to get the elements from the specified range
print(my_list16)

my_list17 = my_list5[-1:1:2]    # slicing is used to get the elements from the specified range
print(my_list17)