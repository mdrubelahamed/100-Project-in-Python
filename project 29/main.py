from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    password_entry.delete(0,END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    #list = [new_item for item in list] -- List Comprehension

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def take_and_save_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }


    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title="Warning!", message="Please don't leave any fields empty!")
    else:
        try:
            with open("project 29/data.json","r") as file:
                # read old data
                data = json.load(file)
        except FileNotFoundError:
            with open("project 29/data.json", mode="w") as file:
                json.dump(new_data, file, indent=4)
        else:
            # Update old data with new data
            data.update(new_data)
               
            with open("project 29/data.json", mode="w") as file:
                # Saving the updated data
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0,END)
            password_entry.delete(0,END)
            website_entry.focus()

# ---------------------------- Search Command FIND PASSWORD ---------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("project 29/data.json") as file:
            data_dict = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="File Not Found", message="The data file doesn't exits.")
    else:
        if website in data_dict:
            email = data_dict[website]["email"]
            password = data_dict[website]["password"]
            messagebox.showinfo(title=website, message=f"Email:{email}\nPassword:{password}")
        else:
            messagebox.showinfo(title="Error", message=f"'{website}' data is not found in the data store.")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="project 29/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)


# Label's
website_label = Label(text="Website")
website_label.grid(column=0, row=1)
email_label = Label(text="Emain/Username")
email_label.grid(column=0, row=2)
password_label = Label(text="Password")
password_label.grid(column=0, row=3)


# Entry's
website_entry = Entry(width=17)
website_entry.grid(column=1, row=1)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0,"example@gmail.com")
password_entry = Entry(width=17)
password_entry.grid(column=1, row=3)


# Button's
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)
add_button = Button(text="Add", width=30, command=take_and_save_data)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", command=find_password)
search_button.grid(column=2,row=1)


window.mainloop()