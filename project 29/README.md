# Project - Tkinter Password Manger

---
### Day 29 //Project 29
### What?
- Topic - Using Tkinter Generate a password manager

## What I learn so far?
- columnspan, insert(index,string)  
```
#1
for char in range(nr_letters):
  password_list.append(choice(letters))
for char in range(nr_symbols):
  password_list += choice(symbols)
for char in range(nr_numbers):
  password_list += choice(numbers)

#2
for char in password_list:
  password += char

#3
def find_password():
    website = website_entry.get()
    try:
        with open("project 29/data.json") as file:
            data_dict = json.load(file)
            try:
                email = data_dict[website]["email"]
                password = data_dict[website]["password"]
                messagebox.showinfo(title=website, message=f"Email:{email}\nPassword:{password}")
            except KeyError:
                messagebox.showinfo(title="Error", message="Data is not found")
    except FileNotFoundError:
        messagebox.showinfo(title="File Not Found", message="The data file doesn't exits.")
```

https://tkdocs.com/tutorial/canvas.html
---
---