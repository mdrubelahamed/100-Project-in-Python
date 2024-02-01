# dealing with error!
try :
    # value = 10/x
    num= int(input("enter a number: "))
    print(num)
except ZeroDivisionError as err:
    print(err)
except ValueError as err:
    print(err)
except NameError as err:
    print(err)