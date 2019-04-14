def my_decorator(func):
    def display(*args, **kwargs):
        print("calling before decorator func ")
        func(*args, **kwargs)
        return func(*args, **kwargs) #Needed this https://realpython.com/primer-on-python-decorators/
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

print(say_jagdish) # For introspection
print(say_jagdish.__name__) # For introspection prints name of decorator func
