"""
Project: Unique Password Generator.
Created on Tue Oct 12 14:03:35 2021
@author: Thadimarri Sameer
"""

from tkinter import *
from tkinter import messagebox
import random
from random import shuffle

# ------------------------------ PASSWORD GENERATOR ---------------------------------------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    random_letters = random.randint(0, 8)
    random_numbers = random.randint(0, 4)
    random_symbols = random.randint(0, 4)

    password_letters = [random.choice(letters) for _ in range(random_letters)]
    password_numbers = [random.choice(numbers) for _ in range(random_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(random_symbols)]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)


# --------------------------------------- SAVE DATA ---------------------------------------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message=f"Please make sure you haven't left any field empty.")
    else:
        data_filled = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
                                             f"\nPassword: {password} \nIs it ok to save?")
        
        if data_filled:
            with open("Data.txt", "a") as data_file:
                 data_file.write(f"{website} || {email} || {password}\n")
        website_entry.delete(0,END)
        email_entry.delete(0,END)
        password_entry.delete(0,END)
        
# ---------------------------------------- GUI SETUP --------------------------------------------------------------- #

window = Tk()
window.title("Password Generator")
window.config(padx=20,pady=20)

canvas = Canvas(height=200,width=200)
logo = PhotoImage(file="Logo.png")
canvas.create_image(100,100,image=logo)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1 , column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2,column=0)
Password_label = Label(text="Password:")
Password_label.grid(row=3,column=0)

#Entries
website_entry = Entry(width=52)
website_entry.grid(row=1 , column=1 , columnspan=2)
website_entry.focus()
email_entry = Entry(width=52)
email_entry.grid(row=2 , column=1 , columnspan=2)
password_entry = Entry(width=32)
password_entry.grid(row=3 , column=1 , columnspan=1)

#Buttons
generate_password_button = Button(text="Generate Password" , command=generate_password)
generate_password_button.grid(row=3 , column=2)
add_button = Button(text = "Add" , width = 49, command=save)
add_button.grid(row=4 , column=1 , columnspan=2)

window.mainloop()

# ------------------------------------------------------- END ------------------------------------------------------ #
