print("Welcome to the BMI calculator!")
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))


bmi = round(weight / (height**2))

# print(round(bmi))
if bmi < 18.5 :
    print(f"Your BMI is {bmi:.1f}, you are underweight.")
elif bmi < 25 :
    print(f"Your BMI is {bmi:.1f}, you have a normal weihgt")
elif bmi < 30 :
    print(f"Your BMI is {bmi:.1f}, you are slightly overweihgt")
elif bmi < 34.9 :
    print(f"Your BMI is {bmi:.1f}, you are obese")
else:
    print(f"Your BMI is {bmi:.1f}, you are  clinically obese")
