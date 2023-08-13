#create a discount calculator


"""Welcome to our online store!
Please enter the total purchase amount: $120

Original Amount: $120.00
Discount Applied: 10%
Final Amount to Pay: $108.00
--
If the total purchase amount is less than $50, there is no discount.
If the total purchase amount is between $50 (inclusive) and $100 (exclusive), apply a 5% discount.
If the total purchase amount is between $100 (inclusive) and $200 (exclusive), apply a 10% discount.
If the total purchase amount is $200 or more, apply a 15% discount.
"""
print("Welcome to our Online Store")

bill = float(input("What is your bill amount $"))
print()

discount = 0
if bill < 0:
    print("Tell me the correct bill amount.")
elif bill < 50:
    discount += 0
elif bill < 100:
    discount += 5
elif bill < 200:
    discount += 10
elif bill >= 200:
    discount += 15
# else : 
#     print("Enter the correct amount")

after_dis_bill = bill - ((discount / 100) * bill ) 

print(f"Discount Applied: {discount}%")
print(f"Your Final Bill is ${after_dis_bill}")

