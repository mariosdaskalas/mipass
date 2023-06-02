from tkinter import *
from tkinter import messagebox
import random


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
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
    all_get = f"{website_get} | {username_get} | {password_get} \n"
    print(all_get)

    if len(website_get) == 0 or len(password_get) == 0:
        messagebox.showinfo(title="Warning", message=f"Do not leave any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website_get,
                                       message=f"These are the details entered: \nEmail: {username_get}\n Password: {password_get}\n It is ok to save?")
        if is_ok:
            f = open("data.txt", "a")
            f.write(f"{all_get}")
            f.close()

    website_input.delete(0, END)
    username_input.delete(0, END)
    password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
root = Tk()
root.title("Password Manager")
root.config(padx=50, pady=50)

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
website_input = Entry(root, width=35)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()
username_input = Entry(root, width=35)
username_input.grid(column=1, row=2, columnspan=2)
password_input = Entry(root, width=21)
password_input.grid(column=1, row=3)

# Buttons
btn_password = Button(text="Generate", width=10, command=generate_password)
btn_password.grid(column=2, row=3)
btn_add = Button(text="Add", width=36, command=save)
btn_add.grid(column=1, row=4, columnspan=2)

root.mainloop()
