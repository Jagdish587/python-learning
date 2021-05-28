
def mycalc():

    try:
        print("I am in try block")
        print("div value = ", k = 5//0)
        raise NameError("Hi there , error occured")  # Raise Error
    except NameError as myerror:
        print("An exception occured ", myerror)
    except ZeroDivisionError as zerror:
        print("Zero dicision error occured ",zerror )
    except:
        print("some random exception ")
    else:
        print("entered in else cause")
    finally:
        print("Finally came here ")

    print("End of Python fucntion happened")


if __name__ == '__main__':
    mycalc()
