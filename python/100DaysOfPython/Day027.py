# # Day 27
# # GUI and advance functions !!!
#
import tkinter as tk


# from tkinter import *

def exercise1():
    # Variables initialization
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 400
    SCREEN_COLOR = "lightgray"

    LABEL_TEXT: str = "New label"
    LABEL_FONT: tuple = ("Comic Sans", 20, "bold")

    BUTTON_TEXT: str = "New Button"
    BUTTON_FONT: tuple = ("Comic Sans", 20, "bold")

    # Screen/Window creation
    screen = tk.Tk()
    screen.title("MY FIRST REAL GUI!!! :)")
    screen.minsize(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.maxsize(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.configure(bg=SCREEN_COLOR)

    # Label Creation
    label1 = tk.Label(text=LABEL_TEXT, font=LABEL_FONT, bg=SCREEN_COLOR)
    label1.pack()

    label2 = tk.Label(text="0", font=LABEL_FONT, bg=SCREEN_COLOR)
    label2.pack()

    # Button Creation
    def button_to_text():
        label2["text"]: tk = int(label2["text"]) + 1
        label1["text"]: tk = f"You've clicked {label2['text']} times on the button."
        button1["text"]: tk = f"You've clicked {label2['text']} times on the button."
        entrada.insert(0, string=f"You've clicked {label2['text']} times on the button.")

    button1 = tk.Button(text=BUTTON_TEXT, font=BUTTON_FONT, command=button_to_text)
    button1.pack()

    # Entry
    entrada = tk.Entry()
    entrada.insert(0, string="0")
    entrada.pack()

    # MAIN
    screen.mainloop()


def exercise2():
    # Creating a new window and configurations
    window = tk.Tk()
    window.title("Widget Examples")
    window.minsize(width=500, height=500)

    # Labels
    label = tk.Label(text="This is old text")
    label.config(text="This is new text")
    label.pack()

    # Buttons
    def action():
        print("Do something")

    # calls action() when pressed
    button = tk.Button(text="Click Me", command=action)
    button.pack()

    # Entries
    entry = tk.Entry(width=30)
    # Add some text to begin with
    entry.insert(tk.END, string="Some text to begin with.")
    # Gets text in entry
    print(entry.get())
    entry.pack()

    # Text
    text = tk.Text(height=5, width=30)
    # Puts cursor in textbox.
    text.focus()
    # Adds some text to begin with.
    text.insert(tk.END, "Example of multi-line text entry.")
    # Get's current value in textbox at line 1, character 0
    print(text.get("1.0", tk.END))
    text.pack()

    # Spinbox
    def spinbox_used():
        # gets the current value in spinbox.
        print(spinbox.get())

    spinbox = tk.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
    spinbox.pack()

    # Scale
    # Called with current scale value.
    def scale_used(value):
        print(value)

    scale = tk.Scale(from_=0, to=100, command=scale_used)
    scale.pack()

    # Checkbutton
    def checkbutton_used():
        # Prints 1 if On button checked, otherwise 0.
        print(checked_state.get())

    # variable to hold on to checked state, 0 is off, 1 is on.
    checked_state = tk.IntVar()
    checkbutton = tk.Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
    checked_state.get()
    checkbutton.pack()

    # Radiobutton
    def radio_used():
        print(radio_state.get())

    # Variable to hold on to which radio button value is checked.
    radio_state = tk.IntVar()
    radiobutton1 = tk.Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
    radiobutton2 = tk.Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
    radiobutton1.pack()
    radiobutton2.pack()

    # Listbox
    def listbox_used(event):
        # Gets current selection from listbox
        print(listbox.get(listbox.curselection()))

    listbox = tk.Listbox(height=4)
    fruits = ["Apple", "Pear", "Orange", "Banana"]
    for item in fruits:
        listbox.insert(fruits.index(item), item)
    listbox.bind("<<ListboxSelect>>", listbox_used)
    listbox.pack()
    window.mainloop()


def exercise3():
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 400

    screen = tk.Tk()
    screen.title("Grid System")
    screen.minsize(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.maxsize(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.config(padx=50, pady=50)

    label1 = tk.Label(text="Beautiful Label")
    button1 = tk.Button(text="Beautiful Button")
    entry1 = tk.Entry()
    entry1.insert(tk.END, string="Beautiful Entry")
    button2 = tk.Button(text="Beautiful Button nº2")

    label1.grid(column=0, row=0)
    button1.grid(column=1, row=1)
    entry1.grid(column=3, row=2)
    button2.grid(column=2, row=0)

    screen.mainloop()


def main_exercise():
    def miles_to_kms():
        result = float(et_result.get()) * 0.621371
        lb_result_kms.config(text=str(result) + " miles")

    def kms_to_miles():
        result = float(et_value.get()) * 1.609344
        lb_result_mls.config(text=str(result) + " kilometers")

    screen = tk.Tk()
    screen.title("Miles <-> Kilometers - SUPER Calculator")
    screen.minsize(380, 150)
    screen.maxsize(380, 150)
    screen.config(padx=100, pady=15)

    lb_miles = tk.Label(text="Miles")
    lb_kms = tk.Label(text="Kilometers")
    lb_compare = tk.Label(text="is equal to")
    lb_result_kms = tk.Label(text="0")
    lb_result_mls = tk.Label(text="0")

    bt_calculate_kms = tk.Button(text="in KMs", command=kms_to_miles)
    bt_calculate_mls = tk.Button(text="in Miles", command=miles_to_kms)

    et_value = tk.Entry()
    et_result = tk.Entry()
    et_value.insert(0, "0")
    et_result.insert(0, "0")

    et_value.grid(column=0, row=0)
    lb_miles.grid(column=1, row=0)
    lb_compare.grid(column=0, row=1)
    et_result.grid(column=0, row=2)
    lb_kms.grid(column=1, row=2)
    bt_calculate_kms.grid(column=0, row=3)
    bt_calculate_mls.grid(column=0, row=4)
    lb_result_mls.grid(column=1, row=3)
    lb_result_kms.grid(column=1, row=4)

    screen.mainloop()


# exercise1()
# exercise2()
# exercise3()
main_exercise()
