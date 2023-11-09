import tkinter

window = tkinter.Tk()
window.title("My GUI Interface")
window.minsize(500, 500)

#Label
my_label = tkinter.Label(text="I am a Label", font=("Roman", 20, "bold"))
my_label.pack(side="bottom", fill="x", expand=False)


window.mainloop()