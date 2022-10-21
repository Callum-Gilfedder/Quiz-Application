
## Quiz Application

# Find Quiz api 

import tkinter as tk
from turtle import color
from matplotlib.ft2font import HORIZONTAL
import requests

from numpy import place, var 

screen = tk.Tk()

def initialise_screen():
    screen.geometry("800x400")
    screen.configure(background="lightblue")

def create_title_label():
    text = tk.Label(screen, text="Quiz Application" , height = 4, width = 40, bg = "lightblue", font = ("Helvetica", 15))

# So I do not need a menu button, I can just use a normal button but have four of them.





    



def contact_api(number_of_questions, category_code, difficulty):
    response = requests.get(f"https://opentdb.com/api.php?amount={number_of_questions}&category={category_code}&difficulty={difficulty}&type=multiple")
    data = response.json()
    print(data)


contact_api(10,16,"easy")

# this is working.
# maybe have seperate module for gui and for API calls.

# could add def main with try except blocks for every section.
# put original functions into a module maybe.
# possibly add decorators to time functions?
# requirements.txt file?

def main():
    try:
        initialise_screen()
    except:
        print("Initialising screen error")
    try:
        create_title_label()
    except:
        print("Error in creating title label")


    selection = ''


    def assign_value(value):
        global selection
        selection = value
        lbl["text"] = value
        print(selection)

    lbl = tk.Label(screen, text='Selection Goes Here')
    lbl.grid(row=0, column=0)
    tk.Button(text="General Knowledge", command=lambda: assign_value("General Knowledge")).grid(row=1, column=0)
    tk.Button(text="Science", command=lambda: assign_value("Science")).grid(row=2, column=0)
    tk.Button(text="Entertainment", command=lambda: assign_value("Entertainment")).grid(row=3, column=0)
    tk.Button(text="Miscellaneous", command=lambda: assign_value("Miscellaneous")).grid(row=4, column=0)

    print(selection)

    screen.mainloop()


main()