from functools import reduce


def my_sum(valueA, valueB):
    return valueA + valueB


def addHundred(num):
    return num


def reduce_example():
    # syntax reduce(function, iterable[, initializer])

    numbers = [2, 1, 2, 3, 4]
    result = reduce(my_sum, numbers)

    print("result = ", result)

    # using lambda
    resultlambda = reduce(lambda valueA, valueB: valueA + valueB, numbers)
    print("resultlambda = ", resultlambda)

    # using lambda
    multiplylambda = reduce(lambda valueA, valueB: valueA * valueB, numbers)
    print("multiplylambda = ", multiplylambda)

    numbers = [3, 5, 2, 4, 7, 1]
    minResult = reduce(lambda a, b: a if a < b else b, numbers)
    print("minResult = ", minResult)

    maxResult = reduce(lambda a, b: a if a > b else b, numbers)
    print("maxResult = ", maxResult)


if __name__ == "__main__":

    reduce_example()
