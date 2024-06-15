# Day 29
# Password Generator
# ---------------------------- MODULES ------------------------------ #
import random
import string
import tkinter as tk
from tkinter import messagebox
import pandas as pd

# ---------------------------- VARIABLES ------------------------------ #
file_name = "Day029_pass.csv"


# ---------------------------- GENERATOR ------------------------------ #
def generator():
    ip_pass.delete(0, "end")
    new_pass = []

    while len(new_pass) < 4:
        new_pass += random.choice(string.ascii_letters)

    while len(new_pass) < 6:
        new_pass += random.choice(string.digits)

    while len(new_pass) < 8:
        new_pass += random.choice(string.punctuation)

    ip_pass.insert(0, "".join(new_pass))
    window.clipboard_clear()
    window.clipboard_append(ip_pass.get())


# ---------------------------- CHECK FILE ------------------------------ #
def check_file():
    try:
        return pd.read_csv(file_name)
    except FileNotFoundError:
        new = pd.DataFrame({
            "website": [],
            "user": [],
            "pass": []
        })
        new.to_csv(file_name, index=False, header=True)
        return pd.read_csv(file_name)


# ---------------------------- SEARCH FILE ------------------------------ #
def search_file():
    check_file()
    try:
        with open(file_name) as file:
            for line in file.readlines():
                if ip_website.get() in line[0].split(","):
                    messagebox.showinfo(title="PassGen - Search Results", message=f"{line}")
    finally:
        messagebox.showinfo(title="PassGen - Search Results", message="Results finished!")


# ---------------------------- SAVE TO FILE ------------------------------ #
def add_to_file():
    check_file()

    if ip_website.get() and ip_email.get() and ip_pass.get():
        to_save = messagebox.askyesno(title="PassGen - Saving file...", message="Is the information correct?")
        if to_save:
            new = pd.DataFrame({
                "website": [ip_website.get()],
                "user": [ip_email.get()],
                "pass": [ip_pass.get()]
            })

            new.to_csv(file_name, mode="a", index=False, header=False)

            window.clipboard_clear()
            window.clipboard_append(ip_pass.get())

            ip_website.delete(0, "end")
            ip_email.delete(0, "end")
            ip_pass.delete(0, "end")
    else:
        messagebox.showwarning(title="PassGen - Warning", message="Please input information in all fields.")

    ip_website.focus()


# ---------------------------- UI SETUP ------------------------------ #
window = tk.Tk()
window.title("PassGen")
window.minsize(410, 345)
window.maxsize(410, 345)
window.config(padx=20, pady=20, width=200, height=200)

# Canvas
canvas = tk.Canvas(window, width=200, height=200)
LOGO = tk.PhotoImage(file="Day029_logo.png")
canvas.create_image(100, 100, image=LOGO)
canvas.grid(row=0, column=0, columnspan=3)

# Labels
lb_website = tk.Label(window, text="Website:")
lb_email = tk.Label(window, text="Email/Username:")
lb_pass = tk.Label(window, text="Password:")
lb_website.grid(row=1, column=0)
lb_email.grid(row=2, column=0)
lb_pass.grid(row=3, column=0)

# Inputs
ip_website = tk.Entry(width=21)
ip_email = tk.Entry(width=41)
ip_pass = tk.Entry(width=21)
ip_website.grid(row=1, column=1, columnspan=1)
ip_website.focus()
ip_email.grid(row=2, column=1, columnspan=2)
ip_pass.grid(row=3, column=1)

# Buttons
bt_generate = tk.Button(text="Generate Password", width=15, command=generator)
bt_add = tk.Button(text="Add", width=35, command=add_to_file)
bt_search = tk.Button(text="Search", width=15, command=search_file)
bt_generate.grid(row=3, column=2, pady=3)
bt_add.grid(row=4, column=1, columnspan=2, pady=5)
bt_search.grid(row=1, column=2, pady=3)

window.mainloop()
