
## Quiz Application

# Find Quiz api 

import tkinter as tk
from matplotlib.ft2font import HORIZONTAL

from numpy import place, var 

screen = tk.Tk()

def initialise_screen():
    screen.geometry("800x400")
    screen.configure(background="lightblue")

def create_title_label():
    text = tk.Label(screen, text="Quiz Application" , height = 4, width = 40, bg = "lightblue", font = ("Helvetica", 15))
    text.pack()

# So I do not need a menu button, I can just use a normal button but have four of them.

def create_category_button():
    global category_button
    global category
    category_button = tk.Menubutton(screen, text = "Category")   
    category_button.menu = tk.Menu(category_button)  
    category_button["menu"]= category_button.menu  
    category_button.config(font=("Helvetica", 15))
    global var1
    var1 = tk.IntVar()
    var2 = tk.IntVar()
    var3 = tk.IntVar()
    var4 = tk.IntVar()

    def print_variable(variable):
        print(variable)

    category_button.menu.add_checkbutton(label = "General Knowledge",
                                  variable= var1, command = print_variable(var1))
    category_button.menu.add_checkbutton(label = "Science",
                                    variable = var2)
    category_button.menu.add_checkbutton(label = "Entertainment",
                                     variable=var3)
    category_button.menu.add_checkbutton(label = "Miscellaneous",
                                     variable=var4)
    category_button.place(x= 80, y=80 )

def get_category_input():
    print(category)

def create_difficulty_button():
    menubutton = tk.Menubutton(screen, text = "Difficulty")   
    menubutton.menu = tk.Menu(menubutton)  
    menubutton["menu"]= menubutton.menu  
    menubutton.config(font=("Helvetica", 15))
    var1 = 1
    var2 = 2
    var3 = 3
    menubutton.menu.add_checkbutton(label = "Easy",
                                    variable = var1)  
    menubutton.menu.add_checkbutton(label = "Medium",
                                    variable = var2)
    menubutton.menu.add_checkbutton(label = "Hard",
                                    variable = var3)
    menubutton.place(x= 350, y=80 )

def create_number_of_questions_button():
    menubutton = w = tk.Scale(screen, label= "Number", from_=1, to=50, orient="horizontal")
    menubutton.menu = tk.Scale(menubutton)  
    menubutton.config(font=("Helvetica", 15))
    menubutton.place(x= 600, y=80 )

def generate_button():
    menubutton = tk.Button(screen, text = "Generate Questions")   
    menubutton.menu = tk.Button(menubutton)  
    menubutton.config(font=("Helvetica", 15))          
    menubutton.place(x= 300, y=160 )

def question_label():
    pass

def question_answer():
    pass

import requests

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
    try:
        create_category_button()
    except:
        print("Error in creating category button")
        
    get_category_input()

    try:
        create_difficulty_button()
    except:
        print("Error in creating difficulty button")
    try:
        create_number_of_questions_button()
    except:
        print("Error in creating number of questions slider")
    try:
        generate_button()
    except:
        print("Error in creating the generate questions button")
    screen.mainloop()


main()