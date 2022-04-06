from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

# UI SETUP
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_back_img = PhotoImage(file="./images/card_back.png")
card_front_img = PhotoImage(file="./images/card_front.png")
right_btn_img = PhotoImage(file="./images/right.png")
wrong_btn_img = PhotoImage(file="./images/wrong.png")
flash_card = Canvas(width=810, height=530, highlightthickness=0, bg=BACKGROUND_COLOR)
flash_card.create_image(411, 273, image=card_front_img)
title_text = flash_card.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word_text = flash_card.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
right_btn = Button(image=right_btn_img, highlightthickness=0)
wrong_btn = Button(image=wrong_btn_img, highlightthickness=0)

flash_card.grid(row=0, column=0, columnspan=2)
wrong_btn.grid(row=1, column=0)
right_btn.grid(row=1, column=1)


window.mainloop()
