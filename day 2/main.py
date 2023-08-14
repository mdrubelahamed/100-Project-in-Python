# tip calculator

print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? ₹"))
tip = int(input("What pecentage tip would you like to give? "))
persons = int(input("How many People to split the bill? "))
bill_with_tip = ((tip / 100) * bill) + bill
bill_per_person = bill_with_tip / persons
bill_per_person = "{:.2f}".format(bill_per_person)
print(f"Each Person should pay ₹{bill_per_person}")

# print(f"Each Person Should Pay ₹{bill_per_person:.2f}")