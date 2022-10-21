
## Quiz Application

# Find Quiz api 

import tkinter as tk
from matplotlib.ft2font import HORIZONTAL
import requests

from numpy import place, var 

screen = tk.Tk()

def initialise_screen():
    screen.geometry("800x400")
    screen.configure(background="lightblue")

def create_title_label():
    text = tk.Label(screen, text="Quiz Application" , height = 4, width = 40, bg = "lightblue", font = ("Helvetica", 15))
    text.pack()

# So I do not need a menu button, I can just use a normal button but have four of them.


def create_category_buttons():

    def select1():
        selection = "General Knowledge"
        print(selection)
    def select2():
        selection = "Science"
        print(selection)
    def select3():
        selection = "Entertainment"
        print(selection)
    def select4():
        selection = "Miscellaneous"
        print(selection)

    button1 = tk.Button(text = "General Knowledge", command = select1)
    button1.place(x=100, y=100)

    button2 = tk.Button(text = "Science", command = select2)    
    button2.place(x=100, y=140)

    button3 = tk.Button(text = "Entertainment", command = select3)
    button3.place(x=100, y=180)

    button4 = tk.Button(text = "Miscellaneous", command = select4)
    button4.place(x=100, y=220)






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
    create_category_buttons()

    screen.mainloop()


main()