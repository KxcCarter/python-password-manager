from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    """
    Generates a random password.
    Inserts password into password field.
    Copies password to clipboard.

    """
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password_info():
    """
    Gets input from website, email, and password fields.
    Checks to make sure all fields have been filled.
    If not, returns.
    If yes, saves data and clears form.
    "a" means it appends to the file

    """
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {website: {
        "email": email,
        "password": password,
    }}

    if len(password) == 0:
        messagebox.showerror(title="You done messed up, A-Aron!", message="You can't store an empty field.")
        return
    else:
        try:
            with open("dummy_data.json", "r") as data_file:
                # Read old data
                data = json.load(data_file)
        except FileNotFoundError:
            # Create file in file not found
            with open("dummy_data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=2)
        else:
            # Update old data with new data
            data.update(new_data)

            with open("dummy_data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=2)
        finally:
            clear_fields()


def clear_fields():
    website_entry.delete(0, END)
    password_entry.delete(0, END)


# ---------------------------- PASSWORD SEARCH ------------------------------- #
def password_search():
    try:
        with open("dummy_data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="File not found!", message="There is no password data file. \nTry saving a password and then searching.")
    else:
        try:
            search_results = data[website_entry.get()]
            results_email = search_results["email"]
            results_password = search_results["password"]
            messagebox.showinfo(title=f"{website_entry.get()} password", message=f"Email: {results_email} \nPassword: {results_password}")
        except:
            messagebox.showerror(title="Uh oh!", message="Looks like that website is not in the records.")






# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)



canvas = Canvas(height=200, width=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)


# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(index=0, string="email.me@email.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
search_for_password_button = Button(text="Search Password", command=password_search)
search_for_password_button.grid(row=1, column=2)
add_button = Button(text="Add", width=36, command=save_password_info )
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()