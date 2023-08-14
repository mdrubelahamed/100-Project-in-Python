import random
# It's a game where we give people name who is going to pay the bill
name_string = input("Give me eveybody's name seperated by comma(,): ")

#use split
names = name_string.split(",")
# print(names)

num_item = len(names)-1 #because len print how may item for ex if 5 item it's print 5 but index 5 is out of range so because index start from 0 to len - 1 that's we did this
random_index = random.randint(0,num_item)
random_name = names[random_index]

#or
# random_name = random.choice(names)



print(f"{random_name} is going to pay the bill today!")
