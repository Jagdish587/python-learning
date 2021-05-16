
# create and print list 
mylist = [1, "Jagdish", 2, "Sai Prasad", 2, 3, "Ajay", 3.14]
print("value of list is ", mylist)
print("inital address of  list is ",id(mylist))

#print len of list 
print("length of list = ", len(mylist))

#print by index
print("value at pos 3 = {} {} " .format(mylist[3], mylist.index(3)))
print("3 is present at index  = {} " .format(mylist.index(3)))

#append a element in list 
mylist.append(27)
print(mylist)

#Removes Sai Prasad elemnet from list
mylist.remove("Sai Prasad")
print(mylist)

# pop's last element of list i.e 37 here 
mylist.pop()
print(mylist)

#print elements ny for loop 
for val in mylist:
    print(val, end=" ")

print("final address of  list is ",id(mylist))



