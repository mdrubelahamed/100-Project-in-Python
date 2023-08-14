#how many time you left, cosider you live for 90 years
age = input("what is your age? ")

years = 90 - int(age)

months = years * 12
weeks = years * 52
days = years * 365

print(f"you have {days} days, {weeks} weeks and {months} months left")