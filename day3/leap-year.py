print("Welcome to the leap year checker.")

year = int(input("Which year you want to check? "))

if year % 4 == 0 :
    if year % 100 == 0 :
        if year % 400 == 0:
            print("leap year")
        else:
            print("Not leap year")
    else:
        print("leap year")
else: 
    print("Not leap year")

"""
--------------------------------------------------------------------
if year % 4 == 0 and year%100 != 0:
    print("leap year")
elif year%400 == 0: 
    print("leap year")
else :
    print("not leap year")
--------------------------------------------------------------------
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")
----------------------------------------------------------------- 
"""