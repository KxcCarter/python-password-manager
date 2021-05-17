from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def copy_to_clipboard():
    pass


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password_info():
    """
    "a" means it appends to the file
    :return:
    """
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    concated_data = f"Website: {website} | Email: {email} | Password: {password}"

    is_ok_to_save = messagebox.askokcancel(title=website, message=f"These are the details entered: \n {concated_data} \n Is it okay to save?")

    if is_ok_to_save:
        with open("my_passwords.txt", "a") as data_file:
            data_file.write(f"{concated_data} \n")
            clear_fields()


def clear_fields():
    website_entry.delete(0, END)
    password_entry.delete(0, END)
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
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(index=0, string="email.me@email.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password")
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save_password_info )
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()