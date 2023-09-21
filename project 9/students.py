# student_records = [
#     {'name': 'Alice', 'age': 20, 'course': ['Math', 'Physics']},
#     {'name': 'Bob', 'age': 22, 'course': ['Chemistry', 'Biology', 'English']}
# ]

student_records = []

def update_student_info():
    name_to_update = input("Enter the name of the student you want to update: ")
    
    for student in student_records:
        if student["name"] == name_to_update :
            print("Student found. Enter new information:")
            new_name = input("New name: ")
            new_age = int(input("New age: "))
            new_courses = input("New courses (comma-separated): ").split(",")
            
            student["name"] = new_name
            student["age"] = new_age
            student["courses"] = new_courses
            print("Student information updated.")
            return
    
    print("Student not found.")

def add_new_student(s_name, s_age, s_course):
    new_student = {}
    new_student["name"] = s_name
    new_student["age"] = s_age
    new_student["course"] = s_course
    student_records.append(new_student)

student_left = True
while student_left:
    name = input("What is your name? ")
    age = int(input("How much Old are you? "))
    courses = input("which courses are you enrolled in? ").split(",")
    add_new_student(s_name=name, s_age=age, s_course=courses)

    quit = input("Is there anymore student you want to add. Type 'yes' or 'no'\n").lower()
    if quit == "no":
        student_left = False



update_student = True
while update_student :
    quit = input("Do you want to update student details. Type 'yes' or 'no'\n").lower()
    if quit == "no":
        update_student = False
    else :
        update_student_info()

print(student_records)