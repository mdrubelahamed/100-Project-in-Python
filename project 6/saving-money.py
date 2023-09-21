saving_goal = int(input("What is your saving goal? "))
initial_saving = int(input("What is your initial saving "))

add_amount = 0
month = 0

need_to_save = saving_goal - initial_saving

while add_amount < need_to_save :
    add_in_saving = int(input("How much you would like to add in this month to your saving? "))
    add_amount += add_in_saving
    month += 1

# print(f"You Finally reach your saving goal.")
print(f"Total amount you saved {add_amount}")
print(f"Currently you have in your savings {add_amount + initial_saving}")
print(f"It took {month} month to reach the goal")

