def outer_func(message):

    def inner_func():
        print("inside inner miessage = ", message)

    return inner_func

inner_func_hello = outer_func("hello")
inner_func_hello()

inner_func_hi = outer_func("hi")
inner_func_hi()


inner_func_good = outer_func("hello")
inner_func_good()


inner_func_message = outer_func("message")
inner_func_message()

