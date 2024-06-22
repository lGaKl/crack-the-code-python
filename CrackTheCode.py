from tkinter import *
from tkinter import ttk
import random

def check_code(guess):
    global attempts, code, try_label, good_position_label, good_number_label

    if len(guess) == 3:
        attempts += 1
        correct_position = sum([1 for i in range(3) if guess[i] == code[i]])
        correct_number = sum([1 for i in range(3) if guess[i] in code]) - correct_position
        
        try_txt = f"Try number : {attempts}"
        good_position_txt = f"Good position : {correct_position}"
        good_number_txt = f"Good number : {correct_number}"


        try_label.config(text=try_txt)
        good_position_label.config(text=good_position_txt)
        good_number_label.config(text=good_number_txt)
        
        if correct_position == 3:
            disable_buttons()

def disable_buttons():
    for button in button_frame.winfo_children():
        button.config(state=DISABLED)

def button_click(value):
    global current_guess

    if len(current_guess) < 3:
        current_guess.append(value)
        current_guess_label.config(text=" ".join(map(str, current_guess)))
        
        if len(current_guess) == 3: 
            check_code(current_guess)
            current_guess = []

Gui = Tk()
Gui.title("Crack The Code")
Gui.geometry("400x650")
Gui.configure(background='lightpink2')
Gui.iconbitmap("CrackTheCode.ico")

# Generate a random 3-digit code
code = [random.randint(1, 9) for _ in range(3)]
attempts = 0
current_guess = []

number_frame = Frame(Gui, relief=GROOVE, borderwidth=2, bg="plum3")
number_frame.pack(side=TOP, padx=5, pady=5)

current_guess_label = Label(number_frame, text=" ", font="Arial 35", bg="plum3")
current_guess_label.pack(padx=35, pady=20)

mid_frame = Frame(Gui, relief=GROOVE, borderwidth=2, bg="plum3")
mid_frame.pack(padx=5, pady=5)

try_label = Label(mid_frame,text="Try number : ", font="Arial 15", bg="plum3")
try_label.pack(side=TOP, padx=3, pady=3)

good_position_label = Label(mid_frame, text="Good position : ", font="Arial 15", bg="plum3")
good_position_label.pack(side=BOTTOM, padx=3, pady=3)

good_number_label = Label(mid_frame, text="Good numbers : ", font="Arial 15", bg="plum3")
good_number_label.pack(side=BOTTOM, padx=3, pady=3)

button_frame = Frame(Gui, relief=GROOVE, borderwidth=2, bg="palevioletred3")
button_frame.pack(side=BOTTOM, padx=10, pady=10)

for line in range(3):
    for column in range(3):
        value = 7 - 3 * line + column
        btn = Button(button_frame, text=value, font="Arial 25", relief='raised', bg="plum3",
                     activebackground="plum4", compound="center", borderwidth=5, height=2, width=4,
                     command=lambda v=value: button_click(v))
        btn.grid(row=line, column=column, padx=4, pady=4)

Gui.mainloop()