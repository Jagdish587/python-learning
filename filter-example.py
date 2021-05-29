
def is_even(num):
    return num % 2 == 0


def filter_example():
    mylist = [20, 30, 15, 17, 23, 60]

    print("mylist values = ", mylist, "type of mylist = ", type(mylist))

    # Synatx : filter(function, sequence)
    evenNum = list(filter(is_even, mylist))

    print("even number list = ", evenNum)

    # Using lamdas
    evenNumlabda = list(filter(lambda num: (num % 2 == 0), mylist))
    print("evenNumlabda = ", evenNumlabda)


if __name__ == "__main__":
    filter_example()