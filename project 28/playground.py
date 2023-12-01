# print(245//60)
# print(245%60)

# # ------------------------- AGE CALCULATOR -------------------------- #
# import tkinter as tk
# from datetime import datetime

# def calculate_age():
#     # Get the input dates from the user
#     birth_date_str = entry_birth_date.get()
#     current_date_str = entry_current_date.get()

#     # Convert string dates to datetime objects
#     birth_date = datetime.strptime(birth_date_str, "%d-%m-%Y")
#     current_date = datetime.strptime(current_date_str, "%d-%m-%Y")

#     # Calculate the difference between the dates
#     age = current_date - birth_date
#     print(age)
#     # Extract years, months, and days from the timedelta object
#     years = age.days // 365
#     months = (age.days % 365) // 30
#     days = (age.days % 365) % 30

#     # Display the result
#     result_label.config(text=f"You have lived for {years} years, {months} months, and {days} days.")

# # Create the main window
# root = tk.Tk()
# root.title("Age Calculator")
# root.minsize(width=500, height=500)

# # Create and place input widgets
# label_birth_date = tk.Label(root, text="Enter Birth Date (DD-MM-YYYY):")
# label_birth_date.pack()

# entry_birth_date = tk.Entry(root)
# entry_birth_date.focus()
# entry_birth_date.pack()

# label_current_date = tk.Label(root, text="Enter Current Date (DD-MM-YYYY):")
# label_current_date.pack()

# entry_current_date = tk.Entry(root)
# entry_current_date.pack()

# # Create and place the button to trigger the calculation
# calculate_button = tk.Button(root, text="Calculate Age", command=calculate_age)
# calculate_button.config(padx=8, pady=8)
# calculate_button.pack()

# # Create and place a label to display the result
# result_label = tk.Label(root, text="")
# result_label.pack()

# # Start the Tkinter event loop
# root.mainloop()


# ----------------- TRYING DIFFERENT WIDGET PROBLEM TO SOLVE ------------------ #

FONT = ("Georgia", 20, "normal")
from tkinter import *

root = Tk()
root.title("Practicing widgets")
root.minsize(width=600, height=400)
root.config(padx=200, pady=50)

# -- Problem: Create a program that updates the label text when a button is clicked. Initially, the label should display "This is old text," and when the button is clicked, it should change to "This is new text." --#

# def change_text():
#     label_text.config(text="This is new text.")

# label_text = Label(text="This is old text.", font=FONT)
# label_text.pack()

# action_button = Button(text="Change Text", command=change_text)
# action_button.pack()

# -- Problem: Implement a counter using a button. Clicking the button should increase the counter, and the updated count should be displayed on the button. --#

# high_number = 0

# def count_number():
#     global high_number
#     high_number += 1
#     label_counter.config(text=f"{high_number}")


# label_counter = Label(text="0", font=FONT)
# label_counter.pack()

# counter_button = Button(text="Click Me", command=count_number)
# counter_button.pack()


# -- Problem: Develop a simple password checker. Create an entry widget for the user to input a password. When a button is clicked, check if the password meets a certain criteria (e.g., length, containing both letters and numbers) and print a corresponding message.--#

# def password_checker():
#     entered_password = password_entry.get()

#     min_length = 8
#     special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|', '\\', ':', ';', '<', '>', ',', '.', '?', '/']


#     if len(entered_password) < min_length:
#         label_validation.config(text=f"Password is too short, minimun length is {min_length}")
#     elif not any(char.isalpha() for char in entered_password):
#         label_validation.config(text=f"Password must contain letters")
#     elif not any(char.isdigit() for char in entered_password):
#         label_validation.config(text=f"Password must contain numbers")
#     elif not any(char in special_characters for char in entered_password):
#         label_validation.config(text=f"Password must contain One Special Character")
#     elif any(char.isspace() for char in entered_password):
#         label_validation.config(text=f"Password must not contain any Whitespace")
#     else:
#         label_validation.config(text=f"Password is valid")


# password_entry = Entry(width=30)
# password_entry.focus()
# password_entry.pack()

# password_validation_button = Button(text="Check Password", command=password_checker)
# password_validation_button.config(padx=12, pady=12)
# password_validation_button.pack()

# label_validation = Label(text="", font=FONT)
# label_validation.pack()


# --------------------------- Create a simple program that has multiple Checkbuttons, each representing a different option (e.g., Red, Green, Blue). -------------------------- #

RED = "#FF0000"
GREEN = "#00FF00"
BLUE = "#0000FF"
BLACK = "#000000"

def change_color():
    if red_check.get():
        red_check_button.config(fg=RED)
    elif green_check.get():
        green_check_button.config(fg=GREEN)
    elif blue_check.get():
        blue_check_button.config(fg=BLUE)
    else:
        red_check_button.config(fg=BLACK)
        green_check_button.config(fg=BLACK)
        blue_check_button.config(fg=BLACK)



red_check = BooleanVar()
red_check_button = Checkbutton(text="Become Red", variable=red_check, command=change_color, font=FONT, fg=BLACK)
red_check_button.grid(column=1, row=1)

green_check = BooleanVar()
green_check_button = Checkbutton(text="Become Green", variable=green_check, command=change_color, font=FONT, fg=BLACK)
green_check_button.grid(column=1, row=2)

blue_check = BooleanVar()
blue_check_button = Checkbutton(text="Become Blue", variable=blue_check, command=change_color, font=FONT, fg=BLACK)
blue_check_button.grid(column=1, row=3)


# Start the tkinter event loop
root.mainloop()