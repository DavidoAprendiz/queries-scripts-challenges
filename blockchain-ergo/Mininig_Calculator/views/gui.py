import tkinter as tk
from datetime import datetime
import json
import webbrowser
from Ergo_Mining_Calc.src import functions
from Ergo_Mining_Calc.src import api_calls


class Ergo:
    def __init__(self) -> None:
        self.FONT: tuple = ("Comic Sans", 17, "bold")
        self.FG_COLOR: str = "white"
        self.BG_COLOR: str = "#FF5E18"

        # Windows Setting
        self.window: tk.Tk = tk.Tk()
        self.window.title("Simplistic Mining Calculator || POW to the People || Ergo Manifesto")
        self.window.config(pady=15, padx=5, bg=self.BG_COLOR)

        # Banner Settings
        bt_banner_img: tk.PhotoImage = tk.PhotoImage(file="./data/images/ergo_banner.png")
        bt_banner: tk.Button = tk.Button(text="READ ERGO MANIFESTO", font=self.FONT, image=bt_banner_img, bg=self.BG_COLOR, height=200,
                                         command=lambda: webbrowser.open("https://ergoplatform.org/en/discover/", new=1))
        bt_banner.grid(row=0, column=0, columnspan=4)

        # Labels
        self.lb_1: tk.Label = tk.Label(self.window, text=":Price", font=self.FONT, fg=self.FG_COLOR, bg=self.BG_COLOR)
        self.lb_2: tk.Label = tk.Label(self.window, text=":Network in TH/s", font=self.FONT, fg=self.FG_COLOR,
                                       bg=self.BG_COLOR)
        self.lb_3: tk.Label = tk.Label(self.window, text=":Block Reward", font=self.FONT, fg=self.FG_COLOR,
                                       bg=self.BG_COLOR)
        self.lb_4: tk.Label = tk.Label(self.window, text=":Watts/h", font=self.FONT, fg=self.FG_COLOR, bg=self.BG_COLOR)
        self.lb_5: tk.Label = tk.Label(self.window, text=":Price per KW/h", font=self.FONT, fg=self.FG_COLOR,
                                       bg=self.BG_COLOR)
        self.lb_6: tk.Label = tk.Label(self.window, text=":Hours", font=self.FONT, fg=self.FG_COLOR, bg=self.BG_COLOR)
        self.lb_7: tk.Label = tk.Label(self.window, text=":Hashrate", font=self.FONT, fg=self.FG_COLOR,
                                       bg=self.BG_COLOR)

        # Inputs
        self.input_1: tk.Entry = tk.Entry(self.window, width=8, font=self.FONT)
        self.input_2: tk.Entry = tk.Entry(self.window, width=8, font=self.FONT)
        self.input_3: tk.Entry = tk.Entry(self.window, width=8, font=self.FONT)
        self.input_4: tk.Entry = tk.Entry(self.window, width=8, font=self.FONT)
        self.input_5: tk.Entry = tk.Entry(self.window, width=8, font=self.FONT)
        self.input_6: tk.Entry = tk.Entry(self.window, width=8, font=self.FONT)
        self.input_7: tk.Entry = tk.Entry(self.window, width=8, font=self.FONT)

        # Call API or insert 0(zero) in all fields
        test_apis = api_calls.test_api()
        if test_apis:
            results_api_coin = test_apis[0]
            results_api_price = test_apis[1]
            self.input_1.insert(0, str(results_api_price["price"] / 100_000_000))
            self.input_2.insert(0, str(results_api_coin["nethash"]))
            self.input_3.insert(0, str(results_api_coin["block_reward"]))
            self.input_4.insert(0, str(0.0))
            self.input_5.insert(0, str(0.0))
            self.input_6.insert(0, str(24))
            self.input_7.insert(0, str(0.0))

        else:
            self.input_1.insert(0, "0.0")
            self.input_2.insert(0, "0.0")
            self.input_3.insert(0, "0.0")
            self.input_4.insert(0, "0.0")
            self.input_5.insert(0, "0.0")
            self.input_6.insert(0, "0.0")
            self.input_7.insert(0, "0.0")

        # Grid Layout
        self.input_1.grid(row=1, column=0, padx=5, pady=5)
        self.input_2.grid(row=2, column=0, padx=5, pady=5)
        self.input_3.grid(row=3, column=0, padx=5, pady=5)
        self.input_4.grid(row=1, column=2, padx=5, pady=5)
        self.input_5.grid(row=2, column=2, padx=5, pady=5)
        self.input_6.grid(row=3, column=2, padx=5, pady=5)
        self.input_7.grid(row=4, column=2, padx=5, pady=5)
        self.lb_1.grid(row=1, column=1, sticky="w", padx=5, pady=5)
        self.lb_2.grid(row=2, column=1, sticky="w", padx=5, pady=5)
        self.lb_3.grid(row=3, column=1, sticky="w", padx=5, pady=5)
        self.lb_4.grid(row=1, column=3, sticky="w", padx=5, pady=5)
        self.lb_5.grid(row=2, column=3, sticky="w", padx=5, pady=5)
        self.lb_6.grid(row=3, column=3, sticky="w", padx=5, pady=5)
        self.lb_7.grid(row=4, column=3, sticky="w", padx=5, pady=5)

        bt_calculate_picture: tk.PhotoImage = tk.PhotoImage(file="./data/images/ergo_button.png")
        bt_calculate: tk.Button = tk.Button(image=bt_calculate_picture, bg=self.BG_COLOR, width=245, height=80, command=self.to_call)
        bt_calculate.grid(row=5, column=2, columnspan=2)

        # Canvas for result
        self.canvas: tk.Canvas = tk.Canvas(self.window, bg=self.BG_COLOR, height=100, width=100, highlightthickness=0)
        self.canvas.grid(row=4, column=0, columnspan=2, rowspan=3)

        self.window.mainloop()

    def get_user_inputs(self) -> list:
        self.price: float = float(self.input_1.get())
        self.network_hashrate: float = float(self.input_2.get()) / 1_000_000
        self.block_reward: float = float(self.input_3.get())
        self.user_watts_h: float = float(self.input_4.get())
        self.user_kw_h_price: float = float(self.input_5.get())
        self.user_hours: float = float(self.input_6.get())
        self.user_hashrate: float = float(self.input_7.get())
        return [self.price, self.network_hashrate, self.block_reward, self.user_watts_h, self.user_kw_h_price,
                self.user_hours, self.user_hashrate]

    def save_to_file(self) -> None:
        user_inputs: list = self.get_user_inputs()
        filename: str = "./data/MinersData/MinerResults.json"
        current_date: str = datetime.today().strftime('%d-%m-%Y')

        new: dict = {
            current_date: {
                "price": user_inputs[0],
                "network_hashrate": user_inputs[1],
                "block_reward": user_inputs[2],
                "watts_h": user_inputs[3],
                "kw_h_price": user_inputs[4],
                "hours": user_inputs[5],
                "hashrate": user_inputs[6],
                "miner-revenue": round(functions.daily_block_rewards_in_value_for_hashrate(user_inputs[2], user_inputs[0], user_inputs[1]) * user_inputs[6], 2),
                "miner-spending": functions.daily_spent_in_value(user_inputs[3], user_inputs[5], user_inputs[4]),
            }}
        try:
            with open(filename) as file:
                dados: json = json.load(file)
        except FileNotFoundError:
            with open(filename, "w") as file:
                json.dump(new, file, indent=4)
        else:
            with open(filename, "w") as file:
                dados.update(new)
                json.dump(dados, file, indent=4)

    def resultados(self, has_values: bool) -> None:
        if self.canvas:
            self.canvas.destroy()

        canvas: tk.Canvas = tk.Canvas(self.window)
        var_text: tk.StringVar = tk.StringVar()
        user_inputs: list = self.get_user_inputs()

        if has_values:
            result: str = str(round(
                functions.daily_block_rewards_in_value_for_hashrate(user_inputs[2], user_inputs[0], user_inputs[1]) *
                user_inputs[6], 2))
            daily_spent: float = functions.daily_spent_in_value(user_inputs[3], user_inputs[5], user_inputs[4])
            var_text.set(f"Miner Revenue: {result}$\nMiner Spending: {daily_spent}$")
            tk.Label(canvas, textvariable=var_text, font=self.FONT, bg=self.BG_COLOR, fg="black").pack()
        else:
            var_text.set("\nAdd values to the fields\n")
            tk.Label(canvas, textvariable=var_text, font=self.FONT, bg=self.BG_COLOR, fg="black").pack()

        canvas.grid(row=4, column=0, columnspan=2, rowspan=2)

    def to_call(self) -> None:
        user_inputs: list = self.get_user_inputs()

        if False not in user_inputs:
            self.resultados(True)
            self.save_to_file()
        else:
            self.resultados(False)



