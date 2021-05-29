
def squared_numbers(num):
    return num ** 2

def addAndSub(valueA, valueB):
    return valueA + valueB , valueA - valueB 

def powersValidate(num):
    return num ** 2, num ** 3

def map_example():
    # syntax map(function, iterable)

    mylist = [1,2, 5, 25]
    mylist2 = [3,7, 9, 25]
    squared_list = list(map(squared_numbers, mylist))

    print("squared list  = ",squared_list)

    #using lambda 
    squared_list_lambda =  list(map(lambda num : num ** 2, mylist))
    print("squared_list_lambda  = ",squared_list_lambda)


    listresult = list(map(addAndSub, mylist, mylist2))
    print("listresult  = ",listresult)
    # same example using lambda
    listresult2 = list(map(lambda valueA, valueB : (valueA + valueB, valueA - valueB) ,  mylist, mylist2))
    print("listresult2  = ",listresult2)

    powersresult1 = list(map(powersValidate, mylist))
    print("powersresult  = ",powersresult1)
    # same  result using lambda
    powersresult2 = list(map(lambda num : (num **2 , num ** 3) ,  mylist))
    print("powersresult  = ",powersresult2)


if __name__ == "__main__":
    # More example on https://realpython.com/python-map-function/
    map_example()