def my_decorator(func):
    def display(*args, **kwargs):
        print("calling before decorator func ")
        func(*args, **kwargs)
<<<<<<< HEAD
=======
        return func(*args, **kwargs) #Needed this one https://realpython.com/primer-on-python-decorators/
>>>>>>> added example 2 on decorators
        print("calling after decorator func ")
    
    return display

@my_decorator
def say_jagdish(*argv, **kwargs):
    print("say jagdish..!! ",end = ' ')
    for arg in argv:
        print(arg,end = ' ')
    print()

<<<<<<< HEAD
say_jagdish("Hello","I am ","from" ,"main")
=======
    return "thanks..!!"

print(say_jagdish("Hello","I am ","from" ,"main"))
>>>>>>> added example 2 on decorators
