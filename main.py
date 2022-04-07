from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"

df = pandas.read_csv("./data/french_words.csv")
word_dict = df.to_dict(orient="records")


def generate_new_card():
    current_card = choice(word_dict)
    flash_card.itemconfig(card_title, text="French")
    flash_card.itemconfig(card_word, text=current_card["French"])


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
card_title = flash_card.create_text(400, 150, font=("Ariel", 40, "italic"))
card_word = flash_card.create_text(400, 263, font=("Ariel", 60, "bold"))
right_btn = Button(image=right_btn_img, highlightthickness=0, command=generate_new_card)
wrong_btn = Button(image=wrong_btn_img, highlightthickness=0, command=generate_new_card)

flash_card.grid(row=0, column=0, columnspan=2)
wrong_btn.grid(row=1, column=0)
right_btn.grid(row=1, column=1)


generate_new_card()


window.mainloop()
