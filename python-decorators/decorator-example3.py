def my_decorator(func):
    def display(*args, **kwargs):
        print("calling before decorator func ")
        func(*args, **kwargs)
        return func(*args, **kwargs)
        print("calling after decorator func ")
    
    return display

@my_decorator
def say_jagdish(*argv, **kwargs):
    print("say jagdish..!! ",end = ' ')
    for arg in argv:
        print(arg,end = ' ')
    print()

    return "finnaly done..!!"

print(say_jagdish("Hello","I am ","from" ,"main"))
