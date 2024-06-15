# -------------------------- INTRO ---------------------------- #
# Simplistic mining calculator
# Returns a Value (positive/negative) depending on the given conditions.
#
# ------------------------- CHANGELOG --------------------------- #
# v0.1 - 12/08/2022 -> Simplistic Mining Calculator
# You can assume the Returned Value is equal to the input currency, as in this version all fields are still manual.
# -------------------------- MODULES ---------------------------- #
import tkinter as tk


# ------------------------- FUNCTIONS --------------------------- #
def kw_per_hours(_watts_h: float, _hours: float):
    return round((_watts_h / 1000) * _hours, 2)


def daily_block_rewards(_block_reward):
    return _block_reward * 720


def daily_block_rewards_in_value(_block_reward: float, _price: float):
    return round(daily_block_rewards(_block_reward) * _price, 2)


def daily_spent_in_value(_watts_h: float, _hours: float, _kw_h_price: float):
    total_price_spent_day = kw_per_hours(_watts_h, _hours) * _kw_h_price
    return round(total_price_spent_day, 3)


def daily_block_rewards_in_value_for_hashrate(_block_reward: float, _price: float, _network_hashrate: float):
    return daily_block_rewards_in_value(_block_reward, _price) / _network_hashrate


def _call():
    price = float(input_1.get())
    network_hashrate = float(str(input_2.get().replace(".", "")) + "0000")
    block_reward = float(input_3.get())
    user_watts_h = float(input_4.get())
    user_kw_h_price = float(input_5.get())
    user_hours = float(input_6.get())
    user_hashrate = float(input_7.get())
    list_var = [price, network_hashrate, block_reward, user_watts_h, user_kw_h_price, user_hours, user_hashrate]
    if False in list_var:
        tk.Label(window, text=f"Add values to the fields", font=FONT, bg="white", fg="orange").place(x=100, y=540, anchor="w")
    result = str(
        round(daily_block_rewards_in_value_for_hashrate(block_reward, price, network_hashrate) * user_hashrate, 3))
    daily_spent = daily_spent_in_value(user_watts_h, user_hours, user_kw_h_price)
    tk.Label(window,
             text=f"You're making {result} €/$ with your {user_hashrate} MH/s\nduring {user_hours} hours you've mined.\n"
                  f"You're spending {daily_spent} €/$ in electricity.", font=FONT, bg="white", fg="orange").place(x=100, y=540, anchor="w")


# ---------------------------- MAIN ------------------------------ #
window = tk.Tk()
window.title("Simplistic Mining Calculator || POW to the People || Ergo Manifesto")
window.minsize(600, 600)
window.maxsize(600, 600)
window.config(pady=5, padx=5, bg="white")
picture_file = tk.PhotoImage(file="ERGO_300.png")
# tk.Label(window, image=picture_file).place(x=0, y=0) # for 600x600
tk.Label(window, image=picture_file).place(x=150, y=155)  # for 300x300

# LABEL CREATION
FONT = ("Comic Sans", 16, "bold")
lb_1: tk.Label = tk.Label(window, text=":Price", font=FONT, fg="orange", bg="white")
lb_2: tk.Label = tk.Label(window, text=":Network in TH/s", font=FONT, fg="orange", bg="white")
lb_3: tk.Label = tk.Label(window, text=":Block Reward", font=FONT, fg="orange", bg="white")
lb_4: tk.Label = tk.Label(window, text=":Watts/h", font=FONT, fg="orange", bg="white")
lb_5: tk.Label = tk.Label(window, text=":Price per KW/h", font=FONT, fg="orange", bg="white")
lb_6: tk.Label = tk.Label(window, text=":Hours", font=FONT, fg="orange", bg="white")
lb_7: tk.Label = tk.Label(window, text=":Hashrate", font=FONT, fg="orange", bg="white")
lb_result: tk.Label = tk.Label(window, text="", font=FONT, fg="orange", bg="white")

# INPUTS CREATION
input_1: tk.Entry = tk.Entry(window, width=15)
input_2: tk.Entry = tk.Entry(window, width=15)
input_3: tk.Entry = tk.Entry(window, width=15)
input_4: tk.Entry = tk.Entry(window, width=15)
input_5: tk.Entry = tk.Entry(window, width=15)
input_6: tk.Entry = tk.Entry(window, width=15)
input_7: tk.Entry = tk.Entry(window, width=15)
input_1.insert(0, "0.0")
input_2.insert(0, "0.0")
input_3.insert(0, "0.0")
input_4.insert(0, "0.0")
input_5.insert(0, "0.0")
input_6.insert(0, "0.0")
input_7.insert(0, "0.0")

# SHOW GRID
input_1.grid(row=0, column=0, padx=5, pady=5)
input_2.grid(row=1, column=0, padx=5, pady=5)
input_3.grid(row=2, column=0, padx=5, pady=5)
input_4.grid(row=0, column=2, padx=5, pady=5)
input_5.grid(row=1, column=2, padx=5, pady=5)
input_6.grid(row=2, column=2, padx=5, pady=5)
input_7.grid(row=3, column=2, padx=5, pady=5)
lb_1.grid(row=0, column=1, sticky="w", padx=5, pady=5)
lb_2.grid(row=1, column=1, sticky="w", padx=5, pady=5)
lb_3.grid(row=2, column=1, sticky="w", padx=5, pady=5)
lb_4.grid(row=0, column=3, sticky="w", padx=5, pady=5)
lb_5.grid(row=1, column=3, sticky="w", padx=5, pady=5)
lb_6.grid(row=2, column=3, sticky="w", padx=5, pady=5)
lb_7.grid(row=3, column=3, sticky="w", padx=5, pady=5)
tk.Button(text="What is your revenue?", command=_call).place(x=240, y=460)

window.mainloop()
