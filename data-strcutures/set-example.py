# set is collection of unordered elements
# contains only unique elements 
myset = {1, 2 ,3, 3, 3, 2, "Jagdish"}
print("value in set is ", myset)

myset.add(27)
print("value in set is ", myset)

mysetA = {1,2, 5, 4}
mysetB = {3, 4, 5, 6}

# prints  all elements 
print("union = ", mysetA.union(mysetB))

# prints  common elements from intersection point
print("intersection = ", mysetA.intersection(mysetB))
# prints  common element from first group
print("difference = ", mysetA.difference(mysetB))
# prints not common element from both groups
print("symmetric_difference  = ", mysetA.symmetric_difference(mysetB))