from tkinter import *
import pandas
import random

GREEN = "#B1DDC7"
to_dict = {}

try:
    data = pandas.read_csv("./data/saved_data.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/functions_and_methods.csv")
    to_dict = original_data.to_dict(orient="records")
else:
    to_dict = data.to_dict(orient="records")


def handleNextCard():
    global flip_timer, current_card
    window.after_cancel(flip_timer)
    current_card = random.choice(to_dict)
    canvas.itemconfig(
        card_title, text="Python Functions and Methods", fill="black")
    canvas.itemconfig(
        card_description, text=f"{current_card['Python Functions and Methods']}", fill="black")
    canvas.itemconfig(card, image=card_front)
    flip_timer = window.after(3000, func=handleFlipCard)


def handleFlipCard():
    canvas.itemconfig(card_title, text="Functionality", fill="white")
    canvas.itemconfig(
        card_description, text=f"{current_card['Functionality']}", fill="white")
    canvas.itemconfig(card, image=card_back)


def isKnown():
    to_dict.remove(current_card)
    new_data = pandas.DataFrame(to_dict)
    new_data.to_csv("./data/saved_data.csv", index=False)
    handleNextCard()


window = Tk()
window.title("Flashcards")
window.config(padx=50, pady=50, bg=GREEN)
flip_timer = window.after(3000, func=handleFlipCard)

canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="./image/card_front.png")
card_back = PhotoImage(file="./image/card_back.png")
card = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text((400, 150), text="",
                                fill="black", font=("Ariel", 30, "italic"))
card_description = canvas.create_text((400, 263), text="",
                                      fill="black", font=("Ariel", 12, "bold"))
canvas.config(bg=GREEN, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

correct_img = PhotoImage(file="./image/right.png")
correct_button = Button(
    image=correct_img, highlightthickness=0, command=isKnown)
correct_button.grid(column=1, row=1)

wrong_img = PhotoImage(file="./image/wrong.png")
wrong_button = Button(
    image=wrong_img, highlightthickness=0, command=handleNextCard)
wrong_button.grid(column=0, row=1)

handleNextCard()

window.mainloop()
