student_records = [
    {'name': 'Alice', 'age': 20, 'course': ['Math', 'Physics']},
    {'name': 'Bob', 'age': 22, 'course': ['Chemistry', 'Biology', 'English']}
]

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

# ... rest of your existing code ...

# Call update_student_info function
update_student_info()

# Print updated student_records
print(student_records)
