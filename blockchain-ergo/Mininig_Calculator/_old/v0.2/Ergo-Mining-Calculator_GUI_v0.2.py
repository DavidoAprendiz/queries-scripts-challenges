# -------------------------- INTRO ---------------------------- #
# Simplistic mining calculator
# Completely offline. The next versions will bring API connectors for price and network values.
# Returns a Value (positive/negative) depending on the given values.
#
# Assume that the 'ReturnedValue' is equal to the inserted values for currency.
# A file is stored in the same folder as the script called 'Ergo-Mining-Calculator.json'
# This file will store the values for each day only (as 'day-index').
# If you insert multiple values in the same day, it will only save the last inserted.
# The 'miner-revenue' and 'miner-spending' are stored as last pair values in json file.
#
# ------------------------- CHANGELOG --------------------------- #
# v0.1 - 12/08/2022
#     Initial release: Simplistic Mining Calculator
# v0.2 - 14/08/2022
#     Layout bugs fixed
#     Adjusted Ergo Logo
#     Added function to save Miner Results to a json file.
#     The function "_call" was split into multiple functions
#
# -------------------------- MODULES ---------------------------- #
import tkinter as tk
from datetime import datetime
import json


# ------------------------- FUNCTIONS --------------------------- #
def kw_per_hours(_watts_h: float, _hours: float):
    return round((_watts_h / 1000) * _hours, 2)


def daily_block_rewards(_block_reward):
    return _block_reward * 720


def daily_block_rewards_in_value(_block_reward: float, _price: float):
    return round(daily_block_rewards(_block_reward) * _price, 2)


def daily_spent_in_value(_watts_h: float, _hours: float, _kw_h_price: float):
    total_price_spent_day = kw_per_hours(_watts_h, _hours) * _kw_h_price
    return round(total_price_spent_day, 2)


def daily_block_rewards_in_value_for_hashrate(_block_reward: float, _price: float, _network_hashrate: float):
    return daily_block_rewards_in_value(_block_reward, _price) / _network_hashrate


def get_user_inputs():
    price = float(input_1.get())
    network_hashrate = float(str(input_2.get().replace(".", "")) + "0000")
    block_reward = float(input_3.get())
    user_watts_h = float(input_4.get())
    user_kw_h_price = float(input_5.get())
    user_hours = float(input_6.get())
    user_hashrate = float(input_7.get())
    list_var = [price, network_hashrate, block_reward, user_watts_h, user_kw_h_price, user_hours, user_hashrate]
    return list_var


def save_to_file():
    user_inputs = get_user_inputs()
    filename = "Ergo-Mining-Calculator.json"
    current_date = datetime.today().strftime('%d-%m-%Y')

    new = {
        current_date: {
            "price": user_inputs[0],
            "network_hashrate": user_inputs[1],
            "block_reward": user_inputs[2],
            "watts_h": user_inputs[3],
            "kw_h_price": user_inputs[4],
            "hours": user_inputs[5],
            "hashrate": user_inputs[6],
            "miner-revenue": round(daily_block_rewards_in_value_for_hashrate(user_inputs[2], user_inputs[0], user_inputs[1]) * user_inputs[6], 2),
            "miner-spending": daily_spent_in_value(user_inputs[3], user_inputs[5], user_inputs[4]),
        }}
    try:
        with open(filename) as file:
            dados = json.load(file)
    except FileNotFoundError:
        with open(filename, "w") as file:
            json.dump(new, file, indent=4)
    else:
        with open(filename, "w") as file:
            dados.update(new)
            json.dump(dados, file, indent=4)


def resultados(has_values: bool):
    global canvas
    if canvas:
        canvas.destroy()

    canvas = tk.Canvas(window)
    var_text = tk.StringVar()
    user_inputs = get_user_inputs()

    if has_values:
        result = str(round(
            daily_block_rewards_in_value_for_hashrate(user_inputs[2], user_inputs[0], user_inputs[1]) * user_inputs[6], 2))
        daily_spent = daily_spent_in_value(user_inputs[3], user_inputs[5], user_inputs[4])
        var_text.set(f"You're making {result} €/$ with your {user_inputs[6]} MH/s\nduring {user_inputs[5]} hours you've mined.\nYou're spending {daily_spent} €/$ in electricity.")
        tk.Label(canvas, textvariable=var_text, font=FONT, bg=BG_COLOR, fg="black").pack()
    else:
        var_text.set("Add values to the fields")
        tk.Label(canvas, textvariable=var_text, font=FONT, bg=BG_COLOR, fg="black").pack()

    canvas.grid(row=4, column=0, columnspan=2, rowspan=2)


def _call():
    user_inputs = get_user_inputs()

    if False not in user_inputs:
        resultados(True)
        save_to_file()
    else:
        resultados(False)


# ---------------------------- MAIN ------------------------------ #
FONT = ("Comic Sans", 17, "bold")
FG_COLOR = "white"#Blue
BG_COLOR = "#EC4337"

# Windows Setting
window = tk.Tk()
window.title("Simplistic Mining Calculator || POW to the People || Ergo Manifesto")
window.config(pady=15, padx=5, bg=BG_COLOR)

# Picture Settings
picture_file = tk.PhotoImage(file="ERGO_300.png")
tk.Label(window, image=picture_file, compound="center").grid(row=0, column=0, columnspan=4)

# Labels
lb_1: tk.Label = tk.Label(window, text=":Price", font=FONT, fg=FG_COLOR, bg=BG_COLOR)
lb_2: tk.Label = tk.Label(window, text=":Network in TH/s", font=FONT, fg=FG_COLOR, bg=BG_COLOR)
lb_3: tk.Label = tk.Label(window, text=":Block Reward", font=FONT, fg=FG_COLOR, bg=BG_COLOR)
lb_4: tk.Label = tk.Label(window, text=":Watts/h", font=FONT, fg=FG_COLOR, bg=BG_COLOR)
lb_5: tk.Label = tk.Label(window, text=":Price per KW/h", font=FONT, fg=FG_COLOR, bg=BG_COLOR)
lb_6: tk.Label = tk.Label(window, text=":Hours", font=FONT, fg=FG_COLOR, bg=BG_COLOR)
lb_7: tk.Label = tk.Label(window, text=":Hashrate", font=FONT, fg=FG_COLOR, bg=BG_COLOR)



# Inputs
input_1: tk.Entry = tk.Entry(window, width=8, font=FONT)
input_2: tk.Entry = tk.Entry(window, width=8, font=FONT)
input_3: tk.Entry = tk.Entry(window, width=8, font=FONT)
input_4: tk.Entry = tk.Entry(window, width=8, font=FONT)
input_5: tk.Entry = tk.Entry(window, width=8, font=FONT)
input_6: tk.Entry = tk.Entry(window, width=8, font=FONT)
input_7: tk.Entry = tk.Entry(window, width=8, font=FONT)
input_1.insert(0, "0.0")
input_2.insert(0, "0.0")
input_3.insert(0, "0.0")
input_4.insert(0, "0.0")
input_5.insert(0, "0.0")
input_6.insert(0, "0.0")
input_7.insert(0, "0.0")

# Grid Layout
input_1.grid(row=1, column=0, padx=5, pady=5)
input_2.grid(row=2, column=0, padx=5, pady=5)
input_3.grid(row=3, column=0, padx=5, pady=5)
input_4.grid(row=1, column=2, padx=5, pady=5)
input_5.grid(row=2, column=2, padx=5, pady=5)
input_6.grid(row=3, column=2, padx=5, pady=5)
input_7.grid(row=4, column=2, padx=5, pady=5)
lb_1.grid(row=1, column=1, sticky="w", padx=5, pady=5)
lb_2.grid(row=2, column=1, sticky="w", padx=5, pady=5)
lb_3.grid(row=3, column=1, sticky="w", padx=5, pady=5)
lb_4.grid(row=1, column=3, sticky="w", padx=5, pady=5)
lb_5.grid(row=2, column=3, sticky="w", padx=5, pady=5)
lb_6.grid(row=3, column=3, sticky="w", padx=5, pady=5)
lb_7.grid(row=4, column=3, sticky="w", padx=5, pady=5)
tk.Button(text="⛏⛏⛏ Calculate ⛏⛏⛏", width=24, height=2, font=("Comic Sans", 15, "bold"), command=_call).grid(row=5, column=2, columnspan=2)

# Canvas for result
canvas = tk.Canvas(window, bg=BG_COLOR, height=100, width=100, highlightthickness=0)
canvas.grid(row=4, column=0, columnspan=2, rowspan=3)

window.mainloop()
