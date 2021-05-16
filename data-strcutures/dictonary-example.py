
mydict = {1 : 'T. Jagdish', 2: "Sai Prasad ", 3: "Ajay Tirumala"}
print("dictonary value is {} " .format(mydict))

# printing whole keys 
print("The value of keys is ", mydict.keys())
# whole values 
print("The value of values is ", mydict.values())

#print whole key and values , items() method returns all keys and values
print("printing whole key and values : ",mydict.items())

#print individual items
print("printing value at key 1  = ",mydict[1])
print("printing value at key 2  = ",mydict[2])
print("printing value at key 3  = ",mydict[3])

#priniting dictionary size 
print("dictionary size = ", len(mydict))

#looping techniques 
for keys, value in mydict.items():
    print(keys, " ", value)

