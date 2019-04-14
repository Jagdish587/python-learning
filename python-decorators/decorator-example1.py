def my_decorator(func):
    def display():
        print("calling before decorator func ")
        func()
        print("calling after decorator func ")
    
    return display

@my_decorator
def say_whee():
    print("Whee..!!")

#value_func = my_decorator(say_whee) 
#value_func()

say_whee()