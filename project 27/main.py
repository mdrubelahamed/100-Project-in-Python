from tkinter import *

window = Tk()
window.title("My GUI Interface")
window.minsize(500, 500)

#Label
my_label = Label(text="I am a Label", font=("Comic Sans MS", 20, "bold"))
my_label.pack(side="top", expand=False)

# change text in two way - 1. dict key, 2.config
my_label["text"] = "New Text"
my_label.config(text="New text")

def label_text_changed():
    my_label.config(text=input1.get())

def button_clicked():
    print("I got Clicked")

# Button
button = Button(text="Click Now", command=label_text_changed)
button.pack()


# Entry
input1 = Entry(width=50)
input1.pack()

window.mainloop()

