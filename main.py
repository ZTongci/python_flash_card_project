from tkinter import *
import pandas as pd
from random import *

BACKGROUND_COLOR = "#B1DDC6"


# ------------------------pop word-----------------------------
def check():
    global df
    word_map.pop(word_random)
    show_card()

    new_df = pd.DataFrame(word_map.items(), columns=["French", "English"]).set_index("French")
    print(f"data_length: {len(new_df)}")
    new_df.to_csv("./storage.csv")


# ------------------------show card-----------------------------
df = pd.read_csv("./data/french_words.csv", )
word_map = {row.French: row.English for (index, row) in df.iterrows()}
word_random = ""


def show_card():
    global word_random, id
    window.after_cancel(id)
    word_random = choice(list(word_map.keys()))
    canvas.itemconfig(card_background, image=card_front_img)
    canvas.itemconfig(card_title, text="French", fill='black')
    canvas.itemconfig(card_word, text=f"{word_random}", font=("Ariel", 60, "bold"), fill='black')
    window.after(1000, show_english)


def show_english():
    canvas.itemconfig(card_background, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=f"{word_map[word_random]}", fill='white')


# ------------------------UI-----------------------------
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)
id = window.after(1000, show_card)

cross_image = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=cross_image, command=show_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="./images/right.png")
known_button = Button(image=check_image, command=check)
known_button.grid(row=1, column=1)

window.mainloop()
