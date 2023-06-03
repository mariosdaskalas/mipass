from tkinter import *
from tkinter import messagebox
import random
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def search():
    print(f"Search executed.")
    # Fetch values
    website_get = website_input.get()
    try:
        f = open("data.json", "r")
        data = json.load(f)
    except FileNotFoundError:
        messagebox.showinfo(title=f"Not Found", message=f"No Data File Found. Creating it now...")
        f = open("data.json", "w")
    else:
        if website_get in data:
            mail = (data[f"{website_get}"][f"email"])
            password = (data[f"{website_get}"][f"password"])
            messagebox.showinfo(title=f"{website_get}", message=f"Email: {mail}\n Password: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website_get} found.")


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    # print(f"Your password is: {password}")
    password_input.insert(0, f"{password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    # Fetch values
    website_get = website_input.get()
    username_get = username_input.get()
    password_get = password_input.get()
    new_data = {
        website_get: {
            "email": username_get,
            "password": password_get,
        }
    }

    all_get = f"{website_get} | {username_get} | {password_get} \n"
    print(all_get)

    if len(website_get) == 0 or len(password_get) == 0:
        messagebox.showinfo(title="Warning", message=f"Do not leave any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website_get,
                                       message=f"These are the details entered: \nEmail: {username_get}\n Password: {password_get}\n It is ok to save?")
        if is_ok:
            try:
                f = open("data.json", "r")
                # Reading old data
                data = json.load(f)
            except (FileNotFoundError, json.decoder.JSONDecodeError):
                f = open("data.json", "w")
                json.dump(new_data, f, indent=4)
            else:
                # Updating old data with new data
                data.update(new_data)
                f = open("data.json", "w")
                # Saving updated data
                json.dump(data, f, indent=4)
            finally:
                website_input.delete(0, END)
                username_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
root = Tk()
root.title("Password Manager")
root.config(padx=50, pady=50)
root.iconphoto(False,PhotoImage(file="logo.png"))

# Canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

# Label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entry
website_input = Entry(root, width=23)
website_input.grid(column=1, row=1)
website_input.focus()
username_input = Entry(root, width=37)
username_input.grid(column=1, row=2, columnspan=2)
password_input = Entry(root, width=23)
password_input.grid(column=1, row=3)

# Buttons
btn_search = Button(text="Search", width=10, command=search)
btn_search.grid(column=2, row=1)
btn_password = Button(text="Generate", width=10, command=generate_password)
btn_password.grid(column=2, row=3)
btn_add = Button(text="Add", width=36, command=save)
btn_add.grid(column=1, row=4, columnspan=2)

root.mainloop()
