
def mycalc():

    try:
        print("I am in try block")
        #rm -rf raise NameError("Hi there , error occured")  # Raise Error
    except NameError as myerror:
        print("An exception occured ", myerror)
    else:
        print("entered in else cause")
    finally:
        print("Finally came here ")

    print("End of Python fucntion happened")


if __name__ == '__main__':
    mycalc()
