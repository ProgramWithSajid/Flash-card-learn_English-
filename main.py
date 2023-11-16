BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas as pd
import random
to_learn = {}


#messagebox.showinfo(title="Info", message="Learn English words!!\n NOTE- Memorise the word by clicking the ✔Button ")


try:
    df = pd.read_csv("Flash card/data/words to learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("Flash card/data/word.csv")
    to_learn = original_data.to_dict(orient= "records")
else:
    to_learn = df.to_dict(orient="records")




random_word = {}

def next_word():
    global random_word, flip_timer
    window.after_cancel(flip_timer)
    random_word = random.choice(to_learn)
    canvas.itemconfig(card_title,text = "Hindi", fill = "black")
    canvas.itemconfig(card_word,text = f"{random_word['Hindi']}", fill = "black")
    canvas.itemconfig(card_background, image = card_front)
    flip_timer = window.after(3000,func=flip_card)


def flip_card():
    canvas.itemconfig(card_title,text = "English", fill = "white")
    canvas.itemconfig(card_word,text = f"{random_word['English']}", fill = "white")
    canvas.itemconfig(card_background, image = card_back)
    
def is_known():
    to_learn.remove(random_word)
    print(len(to_learn))
    data = pd.DataFrame(to_learn)
    data.to_csv("Flash card/data/words to learn.csv", index= False)


    next_word()



window = Tk()
window.title("Flashyy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_timer = window.after(3000,func=flip_card)




canvas = Canvas(height=526, width=800)
card_front = PhotoImage(file="Flash card/images/card_front.png")
card_back = PhotoImage(file="Flash card/images/card_back.png")
card_background = canvas.create_image(400,263,image=card_front)
canvas.grid(row=0, column=1,columnspan=2)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)


card_title = canvas.create_text(400,150, text="", font=("Arial",40, "italic"))
card_word = canvas.create_text(400,250, text="", font=("Arial",60, "bold"))



right_image = PhotoImage(file="Flash card/images/right.png")
button = Button(image=right_image, highlightthickness=0,command=is_known)
button.grid(row=1,column=1)


wrong_image = PhotoImage(file="Flash card/images/wrong.png")
button = Button(image=wrong_image, highlightthickness=0,command=next_word)
button.grid(row=1,column=2)




next_word()



window.mainloop()
