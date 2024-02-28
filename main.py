from tkinter import *
import pandas
import random

data = pandas.read_csv("./data/functions_and_methods.csv")
to_dict = data.to_dict(orient="records")


GREEN = "#B1DDC6"


def handleNextCard():
    current_card = random.choice(to_dict)
    canvas.itemconfig(card_title, text="Python Functions and Methods")
    canvas.itemconfig(
        card_description, text=f"{current_card['Python Functions and Methods']}")


window = Tk()
window.title("Flashcards")
window.config(padx=50, pady=50, bg=GREEN)

card_back = PhotoImage(file="./image/card_back.png")


canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="./image/card_front.png")
canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text((400, 150), text="",
                                fill="black", font=("Ariel", 40, "italic"))
card_description = canvas.create_text((400, 263), text="",
                                      fill="black", font=("Ariel", 60, "bold"))
canvas.config(bg=GREEN, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

correct_img = PhotoImage(file="./image/right.png")
correct_button = Button(
    image=correct_img, highlightthickness=0, command=handleNextCard)
correct_button.grid(column=1, row=1)

wrong_img = PhotoImage(file="./image/wrong.png")
wrong_button = Button(
    image=wrong_img, highlightthickness=0, command=handleNextCard)
wrong_button.grid(column=0, row=1)

handleNextCard()

window.mainloop()
