from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email_username = email_username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email_username,
            "password": password,
    }}

    if len(website) == 0 or len(email_username) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email_username} \nPassword: {password}\nIs it ok to save?")
        if is_ok:
            try:
                with open("data.json", "r") as f:
                    #Reading old data
                    data = json.load(f)
            except FileNotFoundError:
                with open("data.json", "w") as f:
                    json.dump(new_data, f, indent=4)
            else:
                #Updating old data with new data
                data.update(new_data)
                with open("data.json", "w") as f:
                    #Saving updated data
                    json.dump(data, f, indent=4)
            finally:
                reset_entries()
        

def reset_entries():
    website_entry.delete(0, END)
    email_username_entry.delete(0, END)
    password_entry.delete(0, END)
    website_entry.focus()

# ------------------------- FIND PASSWORD ---------------------------- #
def find_password():
    website = website_entry.get().lower()
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showerror(title="Error", message="No details for the website exists.")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

logo = PhotoImage(file="logo.png")
canvas = Canvas(height=200, width=200)
canvas.create_image(100,100,image=logo)
canvas.grid(column=1, row=0)

#Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

#Entries
website_entry = Entry(width=21)
website_entry.grid(column=1, row=1, sticky="news")
website_entry.focus()
email_username_entry = Entry(width=35)
email_username_entry.grid(column=1, row=2, columnspan=2, sticky="news")
email_username_entry.insert(0, "dummy@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="news")

#Buttons
search_btn = Button(text="Search", command=find_password)
search_btn.grid(column=2, row=1, sticky="news")
gen_pass_btn = Button(text="Generate Password", command=gen_pass)
gen_pass_btn.grid(column=2, row=3, sticky="news")
add_btn = Button(text="Add", width=36, command=save)
add_btn.grid(column=1, row=4, columnspan=2, sticky="news")

window.mainloop()