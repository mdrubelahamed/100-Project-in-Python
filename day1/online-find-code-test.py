# #quiz1
# str1 = "Programming"
# var2 = list(str1)
# var2[1:6] = list("Python")
# # print(var2)
# print("".join(var2))


#follow calender code

import calendar
# mm = int(input("your date of month number?"))
# yy = int(input("your date of year?"))
# print(calendar.month(yy,mm))

# ---
year = int(input("Which calender year do you want?"))

print(f"The calendar of {year} is:")
print(calendar.calendar(year))