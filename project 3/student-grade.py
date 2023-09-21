#Student Grade Checking Calculator
"""
Welcome to the Student Grade Calculator!

Enter the score for Math: 85
Enter the score for Science: 72
Enter the score for English: 91

Average Score: 82.67
Final Grade: B
--------
A: 90-100
B: 80-89
C: 70-79
D: 60-69
F: Below 60
-------------
"""
print("Welcome to the Student Grade Calculator!")

math = int(input("What is your math score: "))
science = int(input("What is your Science score: "))
english = int(input("What is your English score: "))

avg_score = round((math + science + english) / 3,2)
grade = ""


if math<33 or science<33 or english<33:
   print("YOU Failed.")
   grade = 'F'
elif 90 <= avg_score <= 100:
   grade = "A"
elif 80 <= avg_score <= 89:
   grade = "B"
elif 70 <= avg_score <= 79:
   grade = "C"
elif 60 <= avg_score <= 69:
   grade = "D"
elif avg_score < 60:
   grade = "F"
else:
    print("Enter correct Score--")

print()
print(f"Avarage Score: {avg_score}")
print(f"Final Grade {grade}")