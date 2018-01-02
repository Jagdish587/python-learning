def decorator_func(my_display):
    print("I ama in decorator_func ")

    def inner_func():
        print("I am in inner func ")
        my_display()

    return inner_func

@decorator_func
def display():
    print("I am in display ")

#inner_fun = decorator_func(display)
#inner_fun()
display()
