student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}
for name in student_scores:
    x = student_scores[name]
    if x >= 91:
        student_grades[name] = "Outstanding"
    elif x >= 81:
        student_grades[name] = "Exceeds Expectations"
    elif x >= 71:
        student_grades[name] = "Acceptable"
    elif x <= 70:
        student_grades[name] = "Fail"
    else :
        print("Invalid Input")
print(student_grades)
        


