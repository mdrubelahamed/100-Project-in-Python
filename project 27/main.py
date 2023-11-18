from tkinter import *

# def take_text_from_entry():
#     my_label.config(text=user_input.get())

# def button_clicked():
#     my_label.config(text="Button Got Clicked")
#     print("I got Clicked")



# window = Tk()
# window.title("My GUI Interface")
# window.minsize(500, 150)
# window.config(padx=150, pady=150)

# #Label
# my_label = Label(text="I am a Label", font=("Comic Sans MS", 15, "normal"))
# # change text in two way - 1. dict key, 2.config
# my_label["text"] = "New Text"
# my_label.config(text="New text")
# my_label.grid(column=1, row=1)
# my_label.config(padx=50, pady=50)

# # New Button
# new_button = Button(text="New Button")
# new_button.grid(column=3, row=1)

# # Button
# button = Button(text="Click Now", command=take_text_from_entry)
# button.grid(column=2, row=2)


# # Entry
# user_input = Entry(width=15,)
# user_input.grid(column=4, row=4)



# Mile to Km Converter
# 1 Mile = 1 * 1.60934 km 

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=500)
window.config(padx=25, pady=25)

def mile_to_km():
    mile = float(mile_entry.get())
    km = round((mile * 1.60934), 2)
    km_result.config(text=str(km))

my_label1 = Label(text="is equal to", font=("Comic Sans MS", 15, "normal"))
my_label1.grid(column=1, row=2)

my_label2 = Label(text="Miles", font=("Comic Sans MS", 15, "normal"))
my_label2.grid(column=3, row=1)

my_label3 = Label(text="Km", font=("Comic Sans MS", 15, "normal"))
my_label3.grid(column=3, row=2)


mile_entry = Entry(width=15)
mile_entry.grid(column=2, row=1)
mile_entry.focus()

km_result = Label(text="0", font=("Comic Sans MS", 15, "normal"))
km_result.grid(column=2, row=2)

cal_button = Button(text="Caculate", command=mile_to_km, font=("Comic Sans MS", 20, "normal"))
cal_button.grid(column=2, row=3)


window.mainloop()

