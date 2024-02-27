from tkinter import *

GREEN = "#B1DDC6"

window = Tk()
window.title("Flashcards")
window.config(padx=50, pady=50, bg=GREEN)

card_back = PhotoImage(file="./image/card_back.png")
correct_img = PhotoImage(file="./image/right.png")
wrong_img = PhotoImage(file="./image/wrong.png")


canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="./image/card_front.png")
canvas.create_image(400, 263, image=card_front)
canvas.create_text((400, 150), text="Flashcard",
                   fill="black", font=("Ariel", 40, "italic"))
canvas.create_text((400, 263), text="Description",
                   fill="black", font=("Ariel", 60, "bold"))
canvas.config(bg=GREEN, highlightthickness=0)
canvas.grid(column=0, row=0)

# canvas.create_image(100, 100, image=correct_img)
# canvas.create_image(100, 100, image=wrong_img)

window.mainloop()
