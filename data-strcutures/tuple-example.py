mytuple = (1, "Jagdish", 2, "Sai Prasad ", 3, "AJay", 2.14, 2 , 2)
print("my tuple is ",mytuple)
print("address of  tuple is ",id(mytuple))

# 2 is repeated 3 times ,use method count
print("my tuple length is ",mytuple.count(2))

# returns index of value mentioned , like 3 is at index at 4
print("my tuple index is ",mytuple.index(3))
print("address of  tuple is ",id(mytuple))


# extend  tuple  , it creates new tuple i guess
mytuple = mytuple + (5, 8, 7)
print("my tuple is ",mytuple)
print("address of  tuple is ",id(mytuple))


