from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pd.read_csv("project 31/data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("project 31/data/urdu_words.csv")
    to_learn = data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')


def next_card():
    """Choosing a random dictionary from to_learn nested dictionary"""
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="Urdu", fill="black")
    canvas.itemconfig(card_word, text=current_card["Urdu"], fill="black")
    canvas.itemconfig(card_background, image=card_front_image)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_image)

def is_known():
    try:
        to_learn.remove(current_card)
    except ValueError:
        print(f"{current_card} not found in to_learn")
    else:
        data = pd.DataFrame(to_learn)
        data.to_csv("project 31/data/words_to_learn.csv", index=False)
        if not to_learn:
            # Refill to_learn with all words from the original data
            to_learn.extend(data.to_dict(orient='records'))

    next_card()

window = Tk()
window.title("Flash Cards!")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

# Canvas
canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="project 31/images/card_front.png")
card_back_image = PhotoImage(file="project 31/images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_image)  # Pass 'image=' explicitly
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40,"italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)


# Button
cross_image = PhotoImage(file="project 31/images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="project 31/images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

next_card()


window.mainloop()