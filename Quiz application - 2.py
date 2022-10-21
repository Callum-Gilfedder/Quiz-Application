
## Quiz Application

# Find Quiz api 

import tkinter as tk
from matplotlib.ft2font import HORIZONTAL

from numpy import place 

screen = tk.Tk()

def initialise_screen():
    screen.geometry("800x400")
    screen.configure(background="lightblue")

def create_title_label():
    text = tk.Label(screen, text="Quiz Application" , height = 4, width = 40, bg = "lightblue", font = ("Helvetica", 15))
    text.pack()

def create_category_button():
    menubutton = tk.Menubutton(screen, text = "Category")   
    menubutton.menu = tk.Menu(menubutton)  
    menubutton["menu"]= menubutton.menu  
    menubutton.config(font=("Helvetica", 15))
    var1 = 1
    var2 = 2
    var3 = 3
    var4 = 4
    menubutton.menu.add_checkbutton(label = "General Knowledge",
                                    variable = var1)  
    menubutton.menu.add_checkbutton(label = "Science",
                                    variable = var2)
    menubutton.menu.add_checkbutton(label = "Entertainment",
                                    variable = var3)
    menubutton.menu.add_checkbutton(label = "Miscellaneous",
                                    variable = 4)                       
    menubutton.place(x= 80, y=80 )

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


# could add def main with try except blocks for every section.
# put original functions into a module maybe.
# possibly add decorators to time functions?
# requirements.txt file?

initialise_screen()
create_title_label()
create_category_button()
create_difficulty_button()
create_number_of_questions_button()
generate_button()
screen.mainloop()
