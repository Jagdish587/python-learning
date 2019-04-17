def outer_func(message):

    def inner_func():
        print("inside inner miessage = ", message)

    return inner_func

inner_func_hello = outer_func("hello")
inner_func_hello()

