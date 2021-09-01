from tkinter import *
from data_manager import Data
import time


def new_card():
    global should_continue
    if should_continue:
        time.sleep(0.1)
        data_manager.random_row()
        row_dict = data_manager.row
        card_c.itemconfig(card_lang, text=LANGUAGE[0], fill='black')
        card_c.itemconfig(card_word, text=row_dict['German'], fill='black')
        card_c.itemconfig(card_image, image=card_front)
        window.after(3000, display_back)
        should_continue = False


def save():
    global should_continue
    if should_continue:
        data_manager.remove_row()
        new_card()
        should_continue = False


def display_back():
    global should_continue
    should_continue = True
    row_dict = data_manager.row
    card_c.itemconfig(card_lang, text=LANGUAGE[1], fill='white')
    card_c.itemconfig(card_word, text=row_dict['English'], fill='white')
    card_c.itemconfig(card_image, image=card_back)


BACKGROUND_COLOR = "#B1DDC6"
LANG_FONT = ('Ariel', 40, 'italic')
WORD_FONT = ('Ariel', 60, 'bold')
LANGUAGE = ['German', 'English']
should_continue = True

window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
data_manager = Data()

# Card
card_c = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front = PhotoImage(file='./images/card_front.png')
card_back = PhotoImage(file='./images/card_back.png')
card_image = card_c.create_image(400, 263, image=card_front)
card_lang = card_c.create_text(400, 150, font=LANG_FONT)
card_word = card_c.create_text(400, 263, font=WORD_FONT)
card_c.grid(column=0, row=0, columnspan=2)

# Cross Button
cross_img = PhotoImage(file='./images/wrong.png')
cross_b = Button(image=cross_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=new_card)
cross_b.grid(column=0, row=1)

# Tick Button
tick_img = PhotoImage(file='./images/right.png')
tick_b = Button(image=tick_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=save)
tick_b.grid(column=1, row=1)

new_card()


window.mainloop()
