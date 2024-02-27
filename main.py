from tkinter import *


window = Tk()
window.title("Flashcards")
window.config(padx=20, pady=20)
card_front = PhotoImage("./image/card_front.png")
canvas = Canvas(width=800, height=526)
canvas.create_image(400, 263, image=card_front)
canvas.pack()

window.mainloop()
